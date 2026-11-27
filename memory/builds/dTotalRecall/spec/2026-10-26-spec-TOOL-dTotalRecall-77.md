# TOOL-dTotalRecall-77 — manifest-check is read at one commit by its exit status and its own failure line, never through a grep pipe, and the read is seen red on a staged C9 stall

**Status:** CLOSED · rev-4 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-77-deviation-771.md](../build/2026-10-26-build-TOOL-dTotalRecall-77-deviation-771.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-77-deviation-772.md](../build/2026-10-26-build-TOOL-dTotalRecall-77-deviation-772.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-77-round7-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-77-round7-fix-return.md) | research | — |
| [2026-11-24-build-TOOL-dTotalRecall-77-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-77-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-77-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-77-1-builder-return.md) | journal | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-77-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-77-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-77-round7-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-77-round7-fix-brief.md) | research | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-77-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-77-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-77-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-77-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-77-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-77-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 23 at BLOCKER**. It shares item **B1** with ids 1, 16 and 34, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-80` and `TOOL-dTotalRecall-78`.

The finding reads `TOOL-dTotalRecall-76` (order 35) at its S19: a sweep of `manifest-check.sh` over
every pass commit, piped through `grep -E 'fail (5|9)'`. The checker prints a failure through
`fail() { echo "MANIFEST check $1 FAILED — $2"; status=1; }`
(`skills/session-kickoff/manifest-check.sh@aec378661:2396`) and exits with that status
(`skills/session-kickoff/manifest-check.sh@aec378661:2815`). So the text the pipe wanted never reaches
output, and the pipe discards the exit status: a red commit and a green one both print nothing.

Unit 76 rev-4 spells the repair in its own sweep. Its `print_read` prints each run's status and each
`MANIFEST check` failure line, and its last read is a staged `live` red. The main loop runs it before
unit 76's pass, the only run of the checker this unit's question needs (§8 F2).

This unit is the reading of one commit, as a shell function the later units run: the checker run in a
worktree of that commit, its exit status recorded as its own line, and each failure line matched by
the checker's own format. It is seen red on a stub that carries the checker's own `fail()` line, and
the checker's real red is read from unit 76's sweep, before any later sweep relies on either. It
repairs `TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The read. §4's `read_checker` runs `manifest-check.sh` in a given worktree and prints one
  line `<label> rc=<status>` for every run, then each output line matching
  `^MANIFEST check [0-9]+ FAILED`, prefixed by the label. The status is captured before any filter
  runs, so no pipe can discard it, and an empty or missing worktree prints a non-zero status. §4's
  stub probe sees it red and green. Observed by AC1.
- **S2** — The staged red. No second run is made. Unit 76's sweep stages a check-9 failure in its
  scratch clone and reads it last, under the label `live`, in the two line shapes of S1. Its `live`
  lines are read from unit 76's ledger and quoted in this unit's. The staging makes
  `last-body-change` a commit unknown to the repository, the unknown-baseline arm of C9 and not its
  count arm. Both arms print through the one `fail()`, which is all this read keys on, so the count
  arm's staging is cut (§8 F2). Observed by AC1.
- **S3** — The unstaged read. The sweep's last unit line before `live` is the same checkout read
  before the staging. It is quoted with every failure line beneath it, so S2's red is set beside a
  read of the same tree unstaged. A read at this pass's own base is cut: the base's verdict is unit
  79's S4 (§8 F2). Observed by AC2.

## 3. Non-goals (OUT)

- Running the checker. The main loop ran it, in unit 76's sweep.
- Visiting every pass commit: `TOOL-dTotalRecall-78`.
- The red spans and unit 76's AC13: `TOOL-dTotalRecall-79`.
- Unit 69's AC1 pair and unit 76's S20: `TOOL-dTotalRecall-80`.
- Fixing a red the read finds at the base: unit 79 owns the tip's verdict.
- A check the checker skipped with a `WARN` or `NOTE` line at exit 0: `TOOL-dTotalRecall-91`.
- Editing unit 76's spec, frozen once its unit builds.
- The output-format lint the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S19 sweep's output, the `live` lines and the last unit line its AC13 answer carries, whose grep this read replaces
- **hands-off** `TOOL-dTotalRecall-78` — `read_checker`, the read each pass commit gets where that unit's sweep runs one
- **hands-off** `TOOL-dTotalRecall-79` — `read_checker` and S2's `live` lines, the known red that unit's span derivation must find
- **hands-off** `TOOL-dTotalRecall-80` — `read_checker`, the read unit 69's pass commit and its parent get where that unit runs one
- **hands-off** `TOOL-dTotalRecall-91` — `read_checker`'s line format, which that unit classifies by status and failed checks for unit 69's AC1 (the round-1 audit of units 77 to 88, id 23)
- **hands-off** `TOOL-dTotalRecall-92` — `read_checker`, which that batch reads at unit 79's pass, and the `mc77` worktree path, which this unit no longer makes and that batch finds clear at the tip (the round-1 audit of units 77 to 88, ids 5, 13, 19)
- **hands-off** `TOOL-dTotalRecall-97` — `read_checker`'s two line shapes, which define a placed line of that unit's extraction (the round-1 audit of units 89 to 92, id 30)

## 4. Design

### The read

```bash
# a caller names the worktree by path
read_checker() {  # worktree path, label -> "<label> rc=<n>", then each failure line of the checker, labelled
  local out rc
  out=$(cd "${1:?no worktree}" && bash skills/session-kickoff/manifest-check.sh 2>&1); rc=$?
  printf '%s rc=%s\n' "$2" "$rc"
  printf '%s\n' "$out" | grep -E '^MANIFEST check [0-9]+ FAILED' | sed "s|^|$2 |"
  return 0
}
```

`rc` is the status of the substitution, taken on the next statement, so the filter below it cannot
change it. A `cd` that fails gives a non-zero `rc`, never a silent green. `cd ""` would stay in the
caller's tree at status 0, so the `:?` refuses an empty path inside the substitution. The match is the
checker's own line format at `skills/session-kickoff/manifest-check.sh@aec378661:2396`, every check
number, so a red from a check other than 5 or 9 is still printed. An environment refusal, exit 2,
prints its status and no failure line.

### The stub probe

`fail()` is lifted from the checker at the tip, never retyped, so a checker that changes its line
reds the probe. The stub is placed at the checker's path in a scratch tree, and the checker itself is
never run. The builder saves the function above and this body in one file with the Write tool and runs
it by its path, the repository root as its one argument. The role hook reads the command text, where
the function's checker line is the leg's argv.

```bash
CHECKER=$1/skills/session-kickoff/manifest-check.sh
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
write_stub() {  # case, body -> a tree whose checker is the real fail() line and that body
  mkdir -p "$T/$1/skills/session-kickoff"
  { echo 'status=0'; grep '^fail() ' "$CHECKER"; printf '%s\n' "$2"; echo 'exit "$status"'; } \
    > "$T/$1/skills/session-kickoff/manifest-check.sh"
}
echo "fail lines $(grep -c '^fail() ' "$CHECKER")"
write_stub stall 'fail 9 "stalled
  a second line"'
write_stub two 'fail 5 "stale"; fail 9 "stalled"'
write_stub crash 'echo "MANIFEST env ERROR"; exit 2'
write_stub green 'echo "WARN: skipped C9"'
for c in stall two crash green absent; do read_checker "$T/$c" "$c"; done
read_checker "" empty
echo "old pipe $(cd "$T/stall" && bash skills/session-kickoff/manifest-check.sh 2>&1 | grep -cE 'fail (5|9)')"
```

It was run 2026-11-24 on node a against the checker at `aec378661` and printed the lines AC1 states
(DERIVED 2026-11-24, this probe). Its last line is the audited defect: the old pipe over the same
failing stub counts no line.

### The sweep's lines

Unit 76 §4 prints each unit's read as `<n> <sha> rc=<status>` and the staged read as
`live rc=<status>`, each followed by its labelled failure lines, then a `population` line. Those are
`read_checker`'s two shapes with the labels `<n> <sha>` and `live`. The read before `live` is the last
unit of its loop, in the one scratch clone. A `<n> red checkout-failed` there means `live` was staged
on another tree.

### Why order 36

The read replaces unit 76's grep, so it lands after unit 76's pass at step 35. Units 78, 79 and 80
share step 36 and read through it, so the §3 edges run this pass first.

### Inventory

Minted: the probe functions `read_checker` and `write_stub`, spec text only. Naming cell: none, no
product symbol.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **`grep -E 'MANIFEST check (5|9) FAILED'` alone.** It mends the literal and still reads nothing on
  a run that fails another check or crashes before printing. The exit status is the leg's verdict.
- **`grep` with `set -o pipefail`.** It returns grep's status where no line matched, which is 1 on a
  green commit, so a green and a red still look alike to the caller.
- **A staged red by editing a watched file.** It moves C5 as well, so the line expected would depend
  on two checks; editing `last-body-change` alone reaches C9 only, as unit 76's staging does.

## 5. Production-readiness checklist

- security — no surface. Nothing is run but a stub in a scratch tree the probe removes.
- perf / scale — seconds. No checker run and no worktree.
- error / empty / loading states — a run that prints nothing still prints its `rc=` line, so an empty
  read cannot occur. An empty or missing worktree reads as a non-zero status.
- observability — every run prints its status and every failure line.
- risks — a check the checker skips at exit 0, on a shallow clone or a file with no manifest marker,
  reads `rc=0` and no line. That is the checker's verdict, and unit 91 classifies it. The sweep's
  scratch clone shares the object store of the run's checkout, which is a full clone.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's stub probe runs at the tip by its file path, it prints `fail lines 1`,
  `stall rc=1` with one `stall MANIFEST check 9 FAILED` line, `two rc=1` with a check-5 and a check-9
  line, `crash rc=2` and `green rc=0` with none, `absent rc=1` and `empty rc=1` with none, and
  `old pipe 0` (DERIVED 2026-11-24, the probe). And when
  `git grep -nE "live (rc=|MANIFEST check 9 FAILED)" -- "memory/builds/dTotalRecall/build/*TOOL-dTotalRecall-76-*acceptance-ledger.md"`
  runs, it prints `live rc=1` and a `live MANIFEST check 9 FAILED` line.
  Red when: a run prints no `rc=` line, a stub that fails reads `rc=0`, `empty` reads `rc=0`, a failure
  line is missing from either read, or the sweep's `live` read is green.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-77" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 line quotes the two `live` lines and the probe's output, and its AC2
  line quotes the sweep's last unit line before `live`, an `rc=` line, with every failure line beneath
  it. That line carries no check-9 failure, so the staging alone put one in `live`.
  Red when: the ledger records a verdict with no `rc=` value, or the last unit line is a named red or
  carries a check-9 failure, so the staged read distinguishes nothing.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the stub probe and unit 76's staged red prove the read prints a failure.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Does this unit run the checker again, when unit 76's sweep already reads a staged red?**
  Options: (a) the main loop runs a worktree of this pass's base, staged on the count arm of C9, and a
  read of the base; (b) this unit reads the sweep's `live` lines and its last unit line, and proves
  `read_checker` on a stub. Each meets AC1 and AC2. (a) is a second run of the question unit 76's AC13
  answers, and its base read repeats unit 79's S4. RESOLVED (agent, 2026-11-24, delegated): (b), the
  tie-break's reuse of a seam, per `2026-11-24-prompt-TOOL-dTotalRecall-77-reground-brief`. The count
  arm is not staged, as S2 states. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 23
  (BLOCKER, item B1, shared with ids 1, 16 and 34).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-91, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-97, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.
- rev-4 · 2026-11-24 · §1 · S1 to S3 · §3 · §4 · §5 · AC1, AC2 · §7 · §8 F2 · §10 · re-grounded at `aec378661`
  per `2026-11-24-prompt-TOOL-dTotalRecall-77-reground-brief`, over unit 76 rev-4: the second run of the
  checker and the `mc77` worktree are cut, S2 and S3 reading the sweep's `live` and last unit lines (F2);
  `read_checker` is seen red on a stub of the checker's own `fail()` line and refuses an empty worktree
  path; the `kickoff-manifest ratchet` leg leaves the gates line; citations are pinned.

## 10. Reuse audit

The seams are the checker's own line format at
`skills/session-kickoff/manifest-check.sh@aec378661:2396`, lifted and not retyped, and unit 76 §4's
sweep, whose `print_read` already prints the two shapes and whose output is read rather than made
again. The run of `python tools/codebase-map/reuse_lookup.py "read a checker's exit status and its failure lines at a commit"`
on 2026-11-24 ranked name-stem neighbours of `read` and `check`, none of which reads a checker's
status. The recall query below was made when the spec was written. It found the audit's B1 item,
`TOOL-dTotalRecall-75` and an inherited-red ask of `aLevelledCopy` naming this leg, and none of them
reads the checker's status at a past commit. The class a filter on a word belongs to is
`memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md`. No existing seam is a shell read of the
checker's verdict with its failure lines; the function is three lines.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
