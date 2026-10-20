# **Serves:** research PLAY-dClosedLoop-1
"""The bare-id predicate (execution plan P0.6): every id in a chain build's slug that a tracked file under `memory/`
cites, which the build-index generator would join into that build's `ids:` once the build's folder exists.

It is the generator's own grammar, never a second one. The id pattern is `gen_build_index.build_roster_id_re` over
the declared families; each line is read through `gen_build_index.extract_roster_ids`, which blanks every `missing:`
citation first (`tree_lib.scan_missing_citations`), so a marked id joins nothing while an id behind any other colon
still joins. The read set is the generator's too: each tracked file is put to `gen_build_index.rosters()` itself, so
`memory/LIVE.md`, `memory/ledger/`, `memory/backlog/` under the `builds` backlog mode, and a build's own README for its
own slug are skipped exactly as the renderer skips them. The chain slugs are the rows of v2's `[chain]`.

`--opened` (P0.7, the revision record's finding 11) reads the tree the opening leaves: it prints each of those ids
whose build has an opened README, unless it is a `roster:units` id of that README or that build's carry-forward ask,
an ask row of its own `BACKLOG.md` in its own slug. Each build's joined ids are then exactly the ids the opening
minted. P0.7 runs the plain predicate at the opening commit's parent and `--opened` at the opening commit.

`read_roster` is the `roster:units` pair's one reader, for this file, `deviations.py` (through `read_roster_units`)
and `packet.py` and the opening (through `packet.read_roster`): one unit per table row, the row's first id.

Usage (from the worktree root):
  python bare-ids.py            one line per hit, `<path>:<line>: <id>`
  python bare-ids.py --opened   the same, less each opened build's roster ids and its carry-forward ask
Exit 0 with nothing printed on a clean tree, 1 with one line per hit, 2 when v2 names no chain build.

What it does not read: untracked files, which the generator does not read either; whether an id it reports has been
minted since, which only `--opened` reads, and only as the opening mints them; and, under `--opened`, an id of a
chain build with no README, which the generator joins nowhere until that build opens.
"""
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join("tools", "memory-tree"))
import gen_build_index as gbi  # noqa: E402  the generator whose grammar and read set this predicate is
import row_grammar  # noqa: E402  the memory-tree kit's one row regex, which reads a BACKLOG.md's ask rows

V2 = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
DISPOSED = ("CLOSED", "WONTDO")       # the status verbs that dispose of an ask (backlog.STATUS_VERBS)


def read_chain_slugs(v2_text):
    chain = v2_text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    return set(re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M))


def read_roster(text, id_re, slug=None):
    """[(unit id, line number, row)] of a README's authored `roster:units` pair, in its order: each table row's first
    id read with the generator's markers and id grammar, so a `missing:` citation is no unit, and of `slug` alone when
    one is given. The pair's one reader: `read_roster_units` below and `packet.read_roster` read it through this."""
    out, inside = [], False
    for n, ln in enumerate(text.split("\n"), 1):
        if ln.strip() == gbi.PLAN_OPEN:
            inside = True
        elif ln.strip() == gbi.PLAN_CLOSE:
            break
        elif inside and ln.startswith("|"):
            ids = [i for i, s in gbi.extract_roster_ids(ln, id_re) if slug is None or s == slug]
            if ids:
                out.append((ids[0], n, ln.strip()))
    return out


def read_roster_units(text, id_re):
    """The unit ids of a README's `roster:units` pair, in its order, each once: `read_roster`'s units."""
    return list(dict.fromkeys(u for u, _n, _row in read_roster(text, id_re)))


def read_asks(text, conf):
    """[(ask id, open)] of a BACKLOG.md: each row the kit's row regex (`row_grammar.derive_row_re`) reads as id-led,
    open unless a `CLOSED` or `WONTDO` status row, as the backlog classifier reads it, disposes of that id."""
    rowre = row_grammar.derive_row_re(conf)
    families = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    grammar = gbi.backlog.build_grammar(families)
    asks, disposed = [], set()
    for ln in text.split("\n"):
        m = rowre.match(ln)
        if m:
            asks.append(m.group(1))
            continue
        row = gbi.backlog.extract_row(ln, grammar)
        if row is not None and row.cls == "status" and row.verb in DISPOSED:
            disposed.add(row.target)
    return [(a, a not in disposed) for a in dict.fromkeys(asks)]


def scan_bare_ids(root, chain):
    """[(path, line number, id)] for every chain-slug id the generator would join, in path and line order."""
    conf = gbi.load_conf(root)
    m = conf["MEMORY_ROOT"]
    families = {pair.split(":")[1] for pair in conf["FAMILIES"].split() if ":" in pair}
    id_re = gbi.build_roster_id_re(families)
    skip_backlog = gbi.backlog.read_conf(conf).mode == "builds"
    tracked = [p for p in subprocess.run(["git", "ls-files", "--", m + "/"], cwd=root, capture_output=True, text=True,
                                         encoding="utf-8", check=True).stdout.split("\n") if p]
    hits = []
    for p in tracked:
        if not chain & set(gbi.rosters(root, [p], m, families, skip_backlog=skip_backlog)):
            continue
        text, _why = gbi.read_text_or_none(os.path.join(root, p))
        for n, line in enumerate(text.split("\n"), 1):
            hits += [(p, n, i) for i, slug in gbi.extract_roster_ids(line, id_re) if slug in chain]
    return hits


def scan_opened_ids(root, chain):
    """The hits of `scan_bare_ids` whose build has an opened README, less that README's roster ids and that build's
    carry-forward ask."""
    conf = gbi.load_conf(root)
    m = conf["MEMORY_ROOT"]
    families = {pair.split(":")[1] for pair in conf["FAMILIES"].split() if ":" in pair}
    id_re = gbi.build_roster_id_re(families)
    minted = {}
    for b in sorted(chain):
        readme, _why = gbi.read_text_or_none(os.path.join(root, m, "builds", b, "README.md"))
        if readme is None:
            continue
        backlog, _why = gbi.read_text_or_none(os.path.join(root, m, "builds", b, "BACKLOG.md"))
        asks = [a for a, _open in read_asks(backlog, conf)] if backlog is not None else []
        minted[b] = set(read_roster_units(readme, id_re)) | {a for a in asks if a.split("-")[1] == b}
    return [(p, n, i) for p, n, i in scan_bare_ids(root, chain)
            if i.split("-")[1] in minted and i not in minted[i.split("-")[1]]]


def main(argv):
    with open(V2, encoding="utf-8") as fh:
        chain = read_chain_slugs(fh.read())
    if not chain:
        print(f"bare-ids: {V2} names no chain build, so nothing is filtered and the run is never green")
        return 2
    hits = scan_opened_ids(".", chain) if "--opened" in argv else scan_bare_ids(".", chain)
    for p, n, i in hits:
        print(f"{p}:{n}: {i}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
