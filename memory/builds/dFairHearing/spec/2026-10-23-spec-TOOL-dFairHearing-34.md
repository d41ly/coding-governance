# TOOL-dFairHearing-34 — the version check reads every gov:kit marker in every file the build changed, not four typed directories

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 23 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-34-deviation-341.md](../build/2026-10-23-build-TOOL-dFairHearing-34-deviation-341.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-33 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |
| [2026-10-23-prompt-TOOL-dFairHearing-34-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-34-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md) | spec-audit | TOOL-dFairHearing-35 TOOL-dFairHearing-33 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit's finding id 31 (item H1, HIGH, shared with id 22,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) is
closed. `TOOL-dFairHearing-31` S3 diffs only `tools/hooks`, `tools/roles`, `.claude/skills/build` and
`tools/workflows`, while unit 27 S15's rule covers every commit of the build. The build changes files
holding a `gov:kit` marker outside those four: `tools/check-wiring.sh:51` and
`tools/memory-tree/HYGIENE.template.md:1`, whose rendered copy `memory/HYGIENE.md:1` carries the same
marker. A hand bump in any of them exits 0. This unit closes the marker half of item H1: its
population is every file the build modified, read at the base and at `HEAD`, and it reports a kit
whose marker number changed. The constant half, the typed pattern, is id 22's, in
`TOOL-dFairHearing-33`.

## 2. Scope (IN)

- **S1** — The population is the build's write set as git records it: every path
  `git diff --name-only -z --no-renames --diff-filter=M <base> HEAD` prints, with no pathspec. The
  check prints `files <n>` for it. Observed by AC1.
- **S2** — The comparison. In each such file, every `gov:kit <kit>@<n>` marker is read at the base and
  at `HEAD`, with the marker grammar of `write_version_carriers` (`tools/govkit/govkit.py:820`). A kit
  whose marker appears at both ends and carries a number at `HEAD` that the file did not hold at the
  base prints `<path> <kit> <old> -> <new>`, and the check exits 1 when it printed one and 0 otherwise.
  A prose edit that keeps a quoted marker's number moves nothing. Observed by AC1 and AC2.
- **S3** — Every refusal names its cause and exits 2: an end that is not a commit, and a `git` call that
  exits non-zero, each its own call with its own status. Observed by AC3.
- **S4** — Supersession. Unit 31 S3's four-directory pathspec and its `gov:kit [a-z-]+@` alternative,
  and the clause of its AC1 that no marker line changed, are answered by this unit's S1 to S3 and AC1
  to AC3. Unit 31's S1 and S2, the base, stand. Unit 31's acceptance ledger records them superseded
  here (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by a criterion of this unit: it is a ledger
  entry in unit 31's record, read there.

## 3. Non-goals (OUT)

- No declared constant. A constant read by its own `version_from` pattern is id 22's mechanism,
  `TOOL-dFairHearing-33`; the two checks share no state and hold independently.
- No change to the version rule (unit 27 S15), and no marker in an added file: a new file's marker
  carrying its kit's version is the rule's second half, graded by `kit version markers`.
- No new gate leg and no committed checker: a scratch probe run at this unit's pass.
- No help page: `help/` covers no build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-31` — the resolved base its probe prints, `base <sha> from <source>`; without it this check has no first end to read
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors on this spec, ids 2, 3, 20, 26 and 34: AC1's build-wide Red when half re-read at the build's last pass commit on `base.py`'s sha, this unit's ledger naming whether `GATE_BASE` was set when AC1 ran, and §3's attribution of an added file's marker corrected to `govkit selfcheck` check 5c (its S1 to S4 and S32)


## 4. Design

### Evidence

Measured on 2026-10-23 with the script below, PINNED. Over `3708a705..HEAD` it printed `files 7`,
equal to the count of modified paths in that range, and exited 0. Over `e7d256af4~1..e7d256af4`, a
mint commit, it printed `files 10` and nine lines, among them `memory/HYGIENE.md memory-tree 2.144 ->
2.145`, `tools/memory-tree/HYGIENE.template.md memory-tree 2.144 -> 2.145` and
`tools/memory-tree/check-memory-hygiene.sh memory-tree 2.144 -> 2.145`, and exited 1. None of the nine
sits under the four directories unit 31 reads. A base of `nosuchref` exited 2.

### The check

```python
# markers.py <repo root> <base> [<head>] — every gov:kit marker in every file the range modified
import re, subprocess, sys
root, base = sys.argv[1], sys.argv[2]
head = sys.argv[3] if len(sys.argv) > 3 else "HEAD"
MK = re.compile(r"gov:kit ([a-z0-9-]+)@([0-9]+(?:\.[0-9]+)*)")
def refuse(why):
    print(f"version-markers: nothing compared: {why}", file=sys.stderr)
    sys.exit(2)
def git(*a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.returncode:
        refuse(f"git {a[0]} exited {p.returncode}: {p.stderr.strip()}")
    return p.stdout
for end in (base, head):
    git("rev-parse", "--verify", "-q", f"{end}^{{commit}}")
paths = [p for p in git("-c", "core.quotePath=false", "diff", "--name-only", "-z", "--no-renames",
                         "--diff-filter=M", base, head).split("\0") if p]
def markers(ref, path):
    out = {}
    for m in MK.finditer(git("show", f"{ref}:{path}")):
        out.setdefault(m.group(1), set()).add(m.group(2))
    return out
hits = []
for p in paths:
    a, b = markers(base, p), markers(head, p)
    for kit in sorted(a.keys() & b.keys()):
        if b[kit] - a[kit]:
            hits.append(f"{p} {kit} {' '.join(sorted(a[kit]))} -> {' '.join(sorted(b[kit]))}")
print(f"files {len(paths)}")
for h in hits:
    print(h)
sys.exit(1 if hits else 0)
```

The pass writes it with its file-writing tool under its scratch directory.

### Why the write set and not the carrier manifest

`derive_marker_basis` (`tools/govkit/govkit.py:767`) is the population `selfcheck` check 5c grades,
built from each entry's claimed paths and its `marker_carriers`. A dogfood copy such as
`memory/HYGIENE.md` is a rendered file that a carrier list may not name, and `DEPL-aHoistedPass-10`
records a marker carrier outside both of the populations `tools/check-kit-versions.sh` reads. The
diff's modified paths hold every file the build changed, so no carrier can sit outside them.

### What it does not check

A marker in an added file, which is the rule's second half; a file the range renamed, which
`--no-renames` reads as a deletion and an addition; a file whose marker was taken out entirely, which
is no number changed; and a marker spelled at run time. A prose edit that quotes a marker with a new
number reads as a bump, which fails closed and names the file.

### Files touched (estimate)

None. The check is a scratch probe, and its result is a line in this unit's acceptance ledger.

### Alternatives rejected

- **Keep the pathspec and add the files unit 16 and unit 23 list.** That is another typed list, and the
  next unit's write set is missed the same way.
- **Read only `-` lines of the whole-tree diff, as unit 31 does.** A spec or record that edits a line
  quoting a marker without changing its number would read as a hit; pairing the two ends by kit reads
  only a moved number.

## 5. Production-readiness checklist

- security — N/A: a read-only scratch probe; git runs with argv lists and no shell.
- perf / scale — two `git show` reads per modified file; this build modifies at most a few hundred.
- error / empty / loading states — S3's refusals, exit 2 naming the call; the file count prints so an
  empty population is visible, and AC1 compares it with git's own count.
- observability — `files <n>` prints before any finding.
- risks — a prose quote of a marker with a new number fails closed; the pass reads the named file.
- testing — AC1 to AC3 as probes over this repository's own history.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`markers.py` is the script of §4, written under the pass's scratch directory, and `<base>` is the sha
unit 31's probe prints at this unit's commit.

- **AC1** — When `python markers.py . <base>` runs at this unit's commit, it prints `files <n>`, where
  `<n>` equals the line count `git diff --name-only --no-renames --diff-filter=M <base> HEAD` prints,
  prints no `->` line, and exits 0.
  Red when: a marker number moved in any file the build modified, or the file count is short of git's.
  figure: `<n>` is DERIVED at observation time; it was 7 over `3708a705..HEAD` on 2026-10-23.
- **AC2** — When `python markers.py . e7d256af4~1 e7d256af4` runs, it prints `memory/HYGIENE.md
  memory-tree 2.144 -> 2.145` and `tools/memory-tree/HYGIENE.template.md memory-tree 2.144 -> 2.145`
  among its lines and exits 1.
  Red when: it exits 0, which means a marker bump outside the four directories reads as unchanged, the
  defect id 31 names.
  figure: the lines are PINNED, measured on 2026-10-23 at mint commit `e7d256af4`.
- **AC3** — When the probe runs with `nosuchref` as its base, it exits 2 printing `version-markers:
  nothing compared` before any `files` line.
  Red when: it exits 0 on a base it could not read.

## 7. Gates

`kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the check is a scratch probe, observed directly by §6.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 31 (item H1, HIGH, shared with id 22) of
  the round-4 spec audit of specs 28 to 32.
- rev-2 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (five minors).

## 10. Reuse audit

The marker grammar is govkit's, `gov:kit ([a-z0-9-]+)@([0-9]+(?:\.[0-9]+)*)` in
`write_version_carriers` (`tools/govkit/govkit.py:820`), copied into the scratch probe because that
function writes and this one only reads. `python tools/codebase-map/reuse_lookup.py "find gov:kit
version markers whose number changed between two commits"` ranked `changed` in
`tools/run-gates/run-gates.sh`, the bar's path filter, and generic `kit` and `commit` stems; no
existing function compares markers across two commits, so no existing seam fits the comparison. The
carrier manifest `derive_marker_basis` was weighed and declined in §4. The recall query returned
`TOOL-aBoundedVerdict-29` and `DEPL-aHoistedPass-10`, two marker sites outside a gate's population,
and the audit's H1 item.

Recall terms used: `python tools/memory-recall/query.py "a version check that reads only some directories while the rule covers the whole build" --terms "version line hand bump kit marker gov:kit version_from carrier pathspec scope epoch mint"`
