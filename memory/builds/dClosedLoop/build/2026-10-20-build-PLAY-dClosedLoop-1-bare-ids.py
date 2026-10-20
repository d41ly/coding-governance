# **Serves:** research PLAY-dClosedLoop-1
"""The bare-id predicate (execution plan P0.6): every id in a chain build's slug that a tracked file under `memory/`
cites, which the build-index generator would join into that build's `ids:` once the build's folder exists.

It is the generator's own grammar, never a second one. The id pattern is `gen_build_index.build_roster_id_re` over
the declared families; each line is read through `gen_build_index.extract_roster_ids`, which blanks every `missing:`
citation first (`tree_lib.scan_missing_citations`), so a marked id joins nothing while an id behind any other colon
still joins. The read set is the generator's too: each tracked file is put to `gen_build_index.rosters()` itself, so
`memory/LIVE.md`, `memory/ledger/`, `memory/backlog/` under the `builds` backlog mode, and a build's own README for its
own slug are skipped exactly as the renderer skips them. The chain slugs are the rows of v2's `[chain]`.

Usage (from the worktree root):
  python bare-ids.py      one line per hit, `<path>:<line>: <id>`
Exit 0 with nothing printed on a clean tree, 1 with one line per hit, 2 when v2 names no chain build.

What it does not read: untracked files, which the generator does not read either; and whether an id it reports has
been minted since. Once the opening mints a build's roster and its ask, those ids are cited legitimately, and this
predicate still reports every citation outside the generator's own skips.
"""
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join("tools", "memory-tree"))
import gen_build_index as gbi  # noqa: E402  the generator whose grammar and read set this predicate is

V2 = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"


def read_chain_slugs(v2_text):
    chain = v2_text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    return set(re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M))


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


def main(argv):
    with open(V2, encoding="utf-8") as fh:
        chain = read_chain_slugs(fh.read())
    if not chain:
        print(f"bare-ids: {V2} names no chain build, so nothing is filtered and the run is never green")
        return 2
    hits = scan_bare_ids(".", chain)
    for p, n, i in hits:
        print(f"{p}:{n}: {i}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
