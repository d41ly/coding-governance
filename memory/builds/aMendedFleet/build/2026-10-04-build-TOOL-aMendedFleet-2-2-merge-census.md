# TOOL-aMendedFleet-2 — the definition-level merge census since 2026-09-01

**Serves:** journal TOOL-aMendedFleet-2

Run once, read-only, at HEAD `b93c1133d` on 2026-10-05, node a, from the repository root.

## Population

- Merges read: **196**, every merge reachable from HEAD with a committer date on or after
  2026-09-01. `git rev-list --merges --since=2026-09-01 HEAD | wc -l` printed 196 at the same commit.
- Parents replayed: 392. Octopus merges: none, so no parent was adjudicated against
  `git merge-base --octopus`.
- Files read per parent: every `.sh`, `.py`, `.js` and `.mjs` path the parent changed over its
  merge-base, at the base, the parent and the merge.
- Parse-failure rows: **0**. No revision of any such file failed to tokenize or parse.
- Flagged rows: **5**, in three merges, which re-derives the source review's three merges.

## Flagged rows and their dispositions

| Merge | Parent | File | Name | Disposition |
|---|---|---|---|---|
| `01c22e155` | `ef1dcdb61` | `tools/unattended/unattended.sh` | `write_ask_views` | owned by `TOOL-aMendedFleet-1` |
| `5cb052dab` | `1f9158708` | `tools/check-install-prefix.sh` | `print_offender_key` | superseded by `seen_keys` |
| `5cb052dab` | `1f9158708` | `tools/check-install-prefix.sh` | `print_probe_key` | superseded by `graded` |
| `5cb052dab` | `1f9158708` | `tools/check-install-prefix.sh` | `scan_carried_hits` | superseded by `scan_line` |
| `e2e840d08` | `5491f7bc6` | `tools/push-main.sh` | `parse_push_class` | superseded by `derive_push_failure` |

**`write_ask_views`, owned by `TOOL-aMendedFleet-1`.** The probe's moved pre-fill named
`tools/unattended/unattended.test.sh` as defining it at the merge. That hit is a test double, the
one-line `write_ask_views() { echo "f4-views-double: $1 filed"; }` the F4 block installs and then
unsets, so the row is not a move. The product definition was lost, and `TOOL-aMendedFleet-1`
restored it at `fa55c1465`. `git grep -c -w write_ask_views` over the driver at HEAD prints 3.

**The three install-prefix rows, superseded by the merge's own documented rewrite.** All three came
from node d's `--offenders` signature on the carried-prefix gate (the dDerivedDocket build's
unit 23, plus its repair `3bd4e18b7`). Merge `5cb052dab` deleted the carried registries and rebuilt
`--offenders` over the pure ban's one counter. Its message says so, and so does the record
`memory/builds/aRepatriatedFork/build/2026-10-01-build-TOOL-aRepatriatedFork-23-reconcile-main.md`
under "The pure ban and `--offenders`". The counter is the embedded Python of
`tools/check-install-prefix.sh`, and each lost name maps onto one part of it:

- `scan_carried_hits` produced one row per carried literal. Its successor is `scan_line`, which
  yields every counted spelling. `scan_line` was on the first parent already; the merge keyed it.
- `print_offender_key` printed a key with its occurrence ordinal. Its successor is the
  `seen_keys` ordinal rule, which `5cb052dab` introduced: `seen_keys` is absent at the first parent
  `aa660634` and present at the merge.
- `print_probe_key` printed a probe key before a refusal exited. Its successor is the
  `graded` dead-probe refusal with the counter's single write at its end. A refusal now leaves NO
  key, which the attribution reads as a probe that could not answer. The behaviour changed on
  purpose: the merge message lists "no key on a refusal". No code at HEAD still reads a probe key:
  `git grep` for `runtime-dead-probe` and for each lost name finds only records' prose under
  `memory/`.

**`parse_push_class`, superseded by `derive_push_failure`.** Neither parent of `e2e840d08` defines
`derive_push_failure`, and the merge does, five mentions in `tools/push-main.sh`. The merge's
resolver lifted main's inline failure classifier at `869209edc`, which read the pre-push hook's
verdict file, then probed the push URL, then fell back to fetch and ancestry. It made that a named
function shared by both call sites that had called `parse_push_class`. `parse_push_class`
classified on the push's captured output (`rejected`, `connection` and so on), which is the method
`TOOL-aHonedRuleset-10` refuses: a leg that printed `connection` would report a red bar as an
unreachable remote. Main's comment cites that id at `869209edc` and still does at HEAD. So the
candidate disposition in spec §4 is CONFIRMED, not refuted. The merge message does not mention
`tools/push-main.sh`, so this row was undocumented until now.

## Restores

`none restored here`. The only confirmed loss is `write_ask_views`, and `TOOL-aMendedFleet-1`
owns it and has restored it. The other four rows are supersessions, so nothing was routed to
`--rescope --act add` either. Fact-question F1 had no case to decide beyond its liveness row.

## The gap — what this census cannot see

- **Losses below definition level.** A merge that keeps a function's name and loses part of its
  body is clean here. So is a lost prose section, a lost verb entry, or a lost config key.
  `TOOL-dMendedRecall-3`'s lost verb entry is exactly that shape. The other half of
  `TOOL-aMendedFleet-1`'s loss, the `--status` entry of `tools/unattended/VERBS.template.md`, is
  also that shape and was not flagged here.
- **Definitions the three parsers do not read.** That covers Python embedded in a shell heredoc,
  such as the ban counter inside `tools/check-install-prefix.sh`. It also covers a definition made
  by `eval` or `source`, and every file class outside `.sh`, `.py`, `.js` and `.mjs`.
- **Names that existed at the merge-base.** A name a parent changed and the merge dropped is not
  flagged, because the parent did not ADD it. The carried-registry helpers in `5cb052dab` such as
  `carried_rows` are such names. That merge's message documents them as deliberate deletions.
- **Merges main does not reach**, and merges committed before 2026-09-01.

## The probe, verbatim

Run as `python census.py` from the repository root. It printed the population, the five `FLAG`
rows and the parse-failure count above in 95 s of wall clock.

```python
"""Definition-level replay of every merge reachable from HEAD since 2026-09-01 (TOOL-aMendedFleet-2).

Run from the repository root: `python census.py [SINCE]`. Read-only. Definitions come from the
lexicon kit's own parsers, never a retyped regex.
"""
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "tools/lexicon")
from lexicon import parse_shell_defs, _python_defs, parse_ts_defs  # noqa: E402

SINCE = sys.argv[1] if len(sys.argv) > 1 else "2026-09-01"
EXTS = (".sh", ".py", ".js", ".mjs")


def git(*args):
    return subprocess.run(("git",) + args, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", check=True).stdout


class Blobs:
    """ONE `git cat-file --batch` process; parses cached by blob sha."""

    def __init__(self):
        self.p = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE)
        self.cache = {}

    def read(self, rev, path):
        self.p.stdin.write(f"{rev}:{path}\n".encode())
        self.p.stdin.flush()
        head = self.p.stdout.readline().decode().split()
        if head[-1] == "missing":
            return None, None
        body = self.p.stdout.read(int(head[2]))
        self.p.stdout.read(1)
        return head[0], body.decode("utf-8", errors="replace")

    def defs(self, rev, path):
        """Set of defined names, None when the file is absent, or a SyntaxError string."""
        sha, src = self.read(rev, path)
        if sha is None:
            return None
        if sha not in self.cache:
            try:
                if path.endswith(".sh"):
                    f, t, _ = parse_shell_defs(src)
                elif path.endswith(".py"):
                    f, t, _ = _python_defs(src)
                else:
                    f, t, _ = parse_ts_defs(src)
                self.cache[sha] = {n for n, _ in f} | {n for n, _ in t}
            except SyntaxError as e:
                self.cache[sha] = f"unparseable: {e}"
        return self.cache[sha]


def main():
    merges = [l.split() for l in git("log", "--merges", f"--since={SINCE}", "--format=%H %P",
                                     "HEAD").splitlines()]
    octopus = [m[0] for m in merges if len(m) > 3]
    jobs = []
    for m in merges:
        base_args = ["merge-base", "--octopus"] + m[1:] if len(m) > 3 else None
        for p in m[1:]:
            jobs.append((m[0], p, base_args or ["merge-base", m[1], m[2]]))

    def prep(job):
        merge, parent, mb = job
        base = git(*mb).strip()
        files = [f for f in git("diff", "--name-only", base, parent).splitlines() if f.endswith(EXTS)]
        return merge, parent, base, files

    with ThreadPoolExecutor(8) as ex:
        prepared = list(ex.map(prep, jobs))

    blobs = Blobs()
    flagged, unparsed = [], []
    for merge, parent, base, files in prepared:
        for f in files:
            sets = {k: blobs.defs(r, f) for k, r in (("base", base), ("parent", parent), ("merge", merge))}
            bad = {k: v for k, v in sets.items() if isinstance(v, str)}
            if bad:
                for k, v in bad.items():
                    unparsed.append((merge, parent, f, k, v))
                continue
            added = (sets["parent"] or set()) - (sets["base"] or set())
            for name in sorted(added - (sets["merge"] or set())):
                flagged.append([merge, parent, f, name, "merge lacks file" if sets["merge"] is None else ""])

    for row in flagged:  # moved pre-fill: defined in another file of the merge's tree?
        merge, _, f, name, _ = row
        hits = subprocess.run(["git", "grep", "-l", "-w", name, merge, "--"] + [f"*{e}" for e in EXTS],
                              capture_output=True, text=True).stdout.splitlines()
        where = [h.split(":", 1)[1] for h in hits if h.split(":", 1)[1] != f]
        moved = [w for w in where if isinstance(blobs.defs(merge, w), set) and name in blobs.defs(merge, w)]
        if moved:
            row[4] = (row[4] + "; " if row[4] else "") + "defined at merge in " + ", ".join(moved)

    print(f"merges read: {len(merges)} (since {SINCE}); parents replayed: {len(jobs)}; octopus: {len(octopus)} {' '.join(octopus)}")
    print(f"flagged rows: {len(flagged)}")
    for merge, parent, f, name, note in flagged:
        print(f"FLAG {merge[:9]} parent {parent[:9]} {f} {name}" + (f" [{note}]" if note else ""))
    print(f"parse-failure rows: {len(unparsed)}")
    for merge, parent, f, k, v in unparsed:
        print(f"UNPARSED {merge[:9]} parent {parent[:9]} {f} at {k}: {v}")


if __name__ == "__main__":
    main()
```

## Output, verbatim

```
merges read: 196 (since 2026-09-01); parents replayed: 392; octopus: 0 
flagged rows: 5
FLAG 01c22e155 parent ef1dcdb61 tools/unattended/unattended.sh write_ask_views [defined at merge in tools/unattended/unattended.test.sh]
FLAG 5cb052dab parent 1f9158708 tools/check-install-prefix.sh print_offender_key
FLAG 5cb052dab parent 1f9158708 tools/check-install-prefix.sh print_probe_key
FLAG 5cb052dab parent 1f9158708 tools/check-install-prefix.sh scan_carried_hits
FLAG e2e840d08 parent 5491f7bc6 tools/push-main.sh parse_push_class
parse-failure rows: 0
```
