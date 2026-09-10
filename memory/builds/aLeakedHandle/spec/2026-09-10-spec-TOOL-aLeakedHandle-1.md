# TOOL-aLeakedHandle-1 — the pipe whose write end nobody closed, and the gate for its class

**Status:** SPECCED · rev-1 · 2026-09-10 · node a · Tier-2 · base 013b1af9 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md](../build/2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md) | research | TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3 |
| [2026-09-10-prompt-TOOL-aLeakedHandle-1-0-run-mandate.md](../prompts/2026-09-10-prompt-TOOL-aLeakedHandle-1-0-run-mandate.md) | journal | — |
| [2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit.md](../reviews/2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit.md) | spec-audit | TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3 |

<!-- /gen:spec-records -->

## 1. Goal

`pass_commit` in `tools/unattended/lib-unattended.sh` feeds its `while read` loop from a heredoc whose
body is a command substitution, and on 2026-09-10 that substitution never saw EOF: the `unattended kit
gate` leg sat at zero CPU for 63 minutes until an operator killed it. This unit removes the pipe from
that read and adds a scan that refuses the same shape anywhere in the tracked shell tree, so the third
occurrence of a class this repo has recorded twice is also the last one found by hand from `/proc`.

## 2. Scope (IN)

- **S1** — Replace the heredoc-plus-command-substitution feed in `pass_commit` with a scratch-file
  feed. The walk writes to a file, the `while` loop reads that file by redirect, and the loop stays in
  the current shell so its `return 0` still returns from the function rather than from a subshell.
  Observed by AC1, AC2 and AC3.
- **S2** — A scratch file that cannot be created is a NAMED refusal on stderr with its own return
  code, not a silent fall-through to the "this pass is still open" answer that `return 1` already
  means. Observed by AC1.
- **S3** — A project-agnostic source scan that finds the CLASS across every tracked `*.sh`: a
  `while … done` loop whose input redirect is an unquoted heredoc whose body holds a command
  substitution, or a here-string that holds one. It derives its own population and takes the registry
  path as an argument, so no kit file names anything outside itself. Observed by AC4 and AC5.
- **S4** — A shrink-only registry carrying the sites that predate this gate, keyed on the file, the
  redirect delimiter and an occurrence count, never on a line number. A row naming a site the scan no
  longer finds is a refusal, so a stale exception cannot hide a live hit. Observed by AC6.
- **S5** — The scan and its self-test wired as legs in `tools/gate-legs.json`, the registry filename
  declared in `.memory-tree.conf`, and `tools/gate-lint/kit.toml`'s `[check]` declaration rewritten,
  because it currently states that the kit ships no leg of its own. Observed by AC7 and AC8.
- **S6** — `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` updated where it says nothing
  sweeps the tree for this class, which this unit falsifies. Observed by AC9.

## 3. Non-goals (OUT)

- The other nineteen sites the scan finds are NOT fixed here. They are carried in the registry and
  drained by a separate unit, if the owner wants them drained at all; see §8 fork B. Fixing twenty
  call sites inside `check-unattended.sh` and `unattended.sh` is a different diff with a different
  risk profile from fixing the one that deadlocked.
- The `done < <(…)` process-substitution form is NOT banned. It is counted and reported by the scan
  and is out of the failing population; see §8 fork A.
- No ceiling is declared, raised or re-derived. `unattended kit gate` keeps the ceiling it has.
- The leg's own timeout and kill REPORTING is untouched.
- The performance shape `TOOL-aQuenchedHarness-7` landed is preserved, not revisited. The subject and
  the sha still come out of one walk.

One side effect is worth stating even though it is not an edge: once this leg returns instead of
deadlocking it earns an `ok` row of its own, which is an input `TOOL-aLeakedHandle-2` reasons about.
That runs one way and needs nothing from this unit's authors or that unit's, so it is recorded here
rather than declared as a handoff.

### Edges

- **consumes-from** external — nothing from a sibling unit. The fix and the scan rest on the tracked
  `*.sh` surface as it stands at the base sha and on `tools/gate-lint/`, which exists today. No
  criterion in §6 rests on anything either sibling unit builds.
- **hands-off** external — the drain of the sites the registry carries, deferred to a backlog row
  outside this build. §8 fork B is where that is decided.

## 4. Design

### The mechanism, verified against source

`tools/unattended/lib-unattended.sh:153-155` reads:

```sh
  done <<PASSCOMMITS
$(GIT log --reverse --format="%H%x09%s" "$_pa..$_pto" 2>/dev/null)
PASSCOMMITS
```

`GIT` is a shell FUNCTION, defined at `lib-unattended.sh:45`. So `$(GIT log …)` forks a bash subshell
which then forks `git` as a grandchild, which is exactly the two-level shape
`memory/gotchas/bounded-through-a-pipe-is-unbounded.md` records: the substitution reads until EOF, EOF
arrives when the LAST inherited write end closes, and under MSYS that is not reliably the direct
child. The root-cause trace read the surviving processes from `/proc` before the kill and found the
forked subshell holding BOTH ends of its own pipe on fd 3 and fd 4 with no descendant alive.

Both callers wrap the function in a second command substitution — `check-unattended.sh:2301` and
`unattended.sh:4802` both spell `$(pass_commit …)` — so the inner substitution runs one substitution
deep, which is the nesting the trace's fd picture shows.

The comment at `lib-unattended.sh:142` says `A HEREDOC, NEVER A PIPE`, and it is correct about the
thing it is defending: a piped `while` runs in a subshell and this loop RETURNS from the function.
The heredoc solved that and walked into the pipe class instead. The fix has to hold both properties
at once.

### The fix

A file, not a pipe. The walk runs in the CURRENT shell with its stdout redirected to a scratch file,
so no pipe exists and no EOF has to arrive; the loop then reads that file by redirect, which creates
no subshell, so `return 0` still returns from `pass_commit`.

```sh
  _pf=$(mktemp) || { printf 'lib-unattended: pass_commit cannot create a scratch file, so it cannot say whether this pass committed\n' >&2; return 2; }
  GIT log --reverse --format="%H%x09%s" "$_pa..$_pto" >"$_pf" 2>/dev/null || :
  while IFS=$'\t' read -r _pc _psub; do
    …
  done <"$_pf"
```

The scratch file is removed on every exit from the function, the early `return 0` included. Both
callers already spell `$(pass_commit … || true)`, so the new return code 2 reaches them as an empty
answer exactly as a failure does today — the difference is the stderr line, which is what makes a
broken `TMPDIR` visible instead of turning every pass into a silently open one. The house idiom for
this refusal is already in the kit at `unattended.sh:757`.

`mktemp` costs one spawn per call, and `pass_commit` is called once per (anchor, unit) pair rather
than once per commit, so this does not re-enter the spawn population `TOOL-aQuenchedHarness-7`
measured. The 1528 spawns that unit removed were `id_in` calls inside the loop body, which this
change does not touch.

### The gate, and why it lives where it does

`tools/gate-lint/` is this repo's declared home for source-hygiene scans over a language whose
failures are SILENT — it ships `ps-hygiene.py` for PowerShell's two such classes, and the charter
states the rule in §7 in exactly those terms. A shell reader that blocks forever at zero CPU with no
output is the same kind of failure one language over. The kit's own `kit.toml` declares a hole,
`gate-lint-leg-wiring`, saying it declares no legs and nothing in a target observes it; this unit is
what discharges that.

The engine goes in the kit; the REGISTRY does not. A kit file names nothing outside itself by literal
(`tools/hooks/README.md`), and a registry of this repo's own sites is nothing but literals naming
files outside the kit. So the registry lives at `memory/project/`, beside the other gate registries,
and its path arrives as the leg's argv. That also makes the scan usable by an adopter with their own
registry, which a hard-coded path would not.

### Data model

The registry is one row per site, tab-separated, keyed and never line-numbered:

```
<path>	<delimiter>	<count>	<reason>
tools/unattended/check-unattended.sh	KEYEOF	1	predates the gate
tools/memory-tree/check-verdict-epoch.sh	EOF	2	predates the gate
```

`<delimiter>` is the heredoc tag, or the literal `<<<` for a here-string. `<count>` is how many sites
in that file carry that delimiter, which is what makes `EOF` keyable where a file holds several. This
is check 15's shape and it is chosen for check 15's reason: a line number moves on unrelated edits, a
gate whose steady state is red gets bypassed, and this repo has already paid two cycles for a
line-keyed waiver registry.

Set equality in both directions. A measured site with no row fails. A row whose site the scan no
longer finds fails, so draining a site forces the row out rather than leaving a widened exemption
behind. The count may fall and may not rise.

### Inventory

| Identifier | Cell that grades it | Note |
|---|---|---|
| `tools/gate-lint/sh_hygiene.py` | `py.function` snake | UNDERSCORE, not the sibling's hyphen. `ps-hygiene.py` is one of the eight hyphenated Python basenames `TOOL-aSurfacedLexicon-15` exists to rename; adding a ninth grows a debt that already has a unit waiting. |
| `memory/project/substitution-fed-loops.txt` | none | Declared in `PROJECT_REGISTRY_EXTRA`; hygiene check 3 admits `memory/project/` members only through that key. |
| leg `shell hygiene (a loop fed by a command substitution)` | none | The tree scan. |
| leg `shell-hygiene selftest` | none | The `--selftest` arm. |

Every function the new file mints is snake_case. `sh.function` is armed with `sh.function.conv` pinned
at 6 as a two-sided equality, so a non-conforming shell function name added by the fix would move a
pin in the wrong direction; the fix mints no shell function.

### The population, measured

Measured on 2026-09-10 against base `013b1af9`, by a scan written to the predicate this unit ships and
recorded with this spec. Every figure below is PINNED at that base; the leg DERIVES its own counts at
run time and prints them.

| Class | Sites | Files | In the failing population |
|---|---|---|---|
| Loop fed by a heredoc holding a command substitution | 19 | 6 | yes |
| Loop fed by a here-string holding a command substitution | 1 | 1 | yes |
| Loop fed by a heredoc with NO command substitution | 29 | 17 | no |
| Non-loop heredoc holding a command substitution | 2 | 2 | no |
| Non-loop here-string holding a command substitution | 21 | 3 | no |
| Loop fed by a process substitution, `done < <(…)` | 21 | 10 | no, counted and reported |

The twenty in the failing population sit in seven files: `check-microformats.sh` (1),
`check-verdict-epoch.sh` (2), `check-unattended.sh` (8), `lib-unattended.sh` (1), `unattended.sh` (6),
`unattended.test.sh` (1) and `check-memory-hygiene.sh` (1, the here-string). S1 removes the
`lib-unattended.sh` one, so the registry seeds at 19.

The near-miss rows matter as much as the hit rows. The 29 loop-heredocs with no substitution are the
false-positive class: their bodies are a plain `$var` expansion, they fork nothing, and a predicate
that redded them would red seventeen innocent files. The 21 non-loop here-strings are assertion
helpers in test files, where the substitution's output is an argument and not a stream. Running the
candidate predicate over the real tree before wiring it is what separated those four populations, and
it is why the ban is written against the loop-feeding forms alone.

### Migration

None. The fix is behaviour-preserving on every input where the old code returned at all, and the gate
lands green because its registry is seeded from the measurement above.

### Rollout

The fix and the gate land together. Landing the gate first would red the bar on a site this unit is
about to remove; landing the fix first leaves the class ungated for the length of a review.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/lib-unattended.sh` | the `pass_commit` feed and its refusal, roughly 8 lines |
| `tools/gate-lint/sh_hygiene.py` | new, the scan plus `--selftest` |
| `tools/gate-lint/kit.toml` | the `[check]` declaration and the `gate-lint-leg-wiring` hole |
| `memory/project/substitution-fed-loops.txt` | new, 19 rows |
| `.memory-tree.conf` | `PROJECT_REGISTRY_EXTRA` gains the filename |
| `tools/gate-legs.json` | two rows |
| `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` | the gating paragraph |

### Alternatives rejected

- **`done < <(GIT log …)`, the process-substitution form.** Rejected on the mechanism.
  `TOOL-dScriptedRepeat-13` records process substitution as the form that keeps a loop in the current
  shell, and it is correct about that, but it does not close this hole: `GIT` is a shell function, so
  the substitution forks a bash subshell which forks `git`, and the reader still depends on a
  grandchild's write end closing. It replaces one pipe with another.
- **A ban with no registry, draining all twenty sites in this unit.** Rejected on blast radius. Twenty
  edits across `check-unattended.sh` and `unattended.sh` is a bigger and riskier diff than the
  deadlock it closes, and the registry ratchets the same outcome without one landing.
- **A new top-level `tools/check-*.sh`.** Rejected for `tools/gate-lint/`, which already owns this
  kind. A second scanner for the same kind at the tool root is the copy-instead-of-extend shape §12
  names, and it would owe a `govkit` entry descriptor that the kit route does not.
- **An arm in `tools/unattended/unattended.test.sh`, beside the existing `out=$(timeout` ban.**
  Rejected because that suite is scoped to one kit and, by the owner ruling of 2026-08-23, is not on
  the bar at all. An arm there gates the class in one directory and runs on demand.

## 5. Production-readiness checklist

- security — N/A. No new write path, no untrusted input, no egress. The scan reads tracked source and
  writes only its own registry under `--write`.
- perf / scale — the scan is a single pass over 105 tracked `*.sh` and costs milliseconds; a ceiling
  is declared with its leg row. The fix trades one subshell fork for one `mktemp` spawn per
  (anchor, unit) pair.
- error / empty / loading states — an empty scan population is a REFUSAL, not a pass, because a scan
  that graded nothing reports the same zero as a clean tree. An unreadable registry is a refusal. A
  `mktemp` failure in the fix is the named refusal S2 specifies.
- observability — the scan prints its four measured populations on every run, green included, so the
  reported-not-gated process-substitution count is never mistaken for coverage. The leg header states
  what it does NOT check.
- risks — three, each with its remedy. `every held leg is budgeted, every budget row resolves` refuses
  a new leg with no budget row, so the two rows are added with the leg. `harness arms (fail branches
  armed or pinned)` grades the new file's refusal branches, which may want an `ARMS_FLOORS` row.
  `install-prefix (shipped surface)` grades tool-root and kit files for carried kit-path literals;
  the registry lives under `memory/project/` partly for that reason, and `tools/dead-path-waivers.txt`
  is the precedent for a registry that names kit paths and passes today.
- testing — `--selftest` proves the predicate in both directions over a fixture, and the tree scan's
  failing case is staged by hand and observed RED before the unit lands. §7 names both.
- migration — none; see §4.
- user docs — none. This is agent-facing tooling with no `help/` surface. The gotcha record is the
  reader-facing carrier and S6 updates it.

## 6. Acceptance criteria

- **AC1** — When the probe recorded with this build sources `lib-unattended.sh`, calls `pass_commit`
  over a range whose first qualifying commit is not the last, and checks the printed sha, the function
  prints that sha and returns 0; and when `TMPDIR` is set to a path that cannot be created, the same
  call prints the refusal on stderr and returns 2.
  Red when: the fix puts the loop behind a pipe, so `return 0` exits a subshell, the function falls
  through and prints nothing.
- **AC2** — When `bash tools/unattended/check-unattended.sh` runs to completion on node `a`, it emits
  a verdict and the run's own gate ledger carries a seconds figure for the leg below its declared
  ceiling.
  Red when: the leg again produces no verdict inside its ceiling.
  cost: the leg's own wall clock, measured at 4168 s on the killed run of 2026-09-10.
  fixture: a full run of that leg on a tree carrying dispatch rows; this worktree has one.
  figure: DERIVED — the seconds are read from the ledger at observation time; the 4168 s is PINNED at
  2026-09-10. A green here does not by itself PROVE the deadlock is gone, because the hang was
  intermittent and the leg passed on other runs with the defect present. AC3 is the criterion that
  proves it, by absence of the construct.
- **AC3** — When the scan runs over the tree, `lib-unattended.sh` appears in neither its hit list nor
  the registry, and `grep -c 'PASSCOMMITS'` over that file returns 0.
  Red when: the fix leaves the substitution in place and the site is carried in the registry instead.
- **AC4** — When the scan runs over the tree at the base sha with the fix applied, it reports 19 sites
  in 6 files as its failing population, and names none of the 29 substitution-free loop heredocs, the
  2 non-loop heredocs, the 21 non-loop here-strings or the 21 process-substitution loops.
  Red when: the predicate names a loop heredoc whose body holds no command substitution, which is the
  false-positive class and the one that would red seventeen innocent files.
  figure: DERIVED — the scan prints every count; the six figures above are PINNED at 2026-09-10 on
  base `013b1af9`.
- **AC5** — When the scan runs with `--selftest`, it builds a fixture holding one loop fed by a
  command substitution and one fed by a plain heredoc, and asserts that the predicate names the first
  and not the second, printing its executed assertion count.
  Red when: an arm is stranded past an early exit and the count falls, or the selftest passes on a
  fixture whose failing case was never built.
- **AC6** — When a row in `substitution-fed-loops.txt` is edited to name a delimiter that no longer
  appears in its file, the leg REFUSES and names that row; and when a row is written with a line
  number in its key, the leg refuses it as malformed.
  Red when: a stale row passes, which is how an exemption silently widens the surface it was written
  to narrow.
- **AC7** — When the `done <<PASSCOMMITS` construct is staged back into a DIFFERENT tracked shell file
  with no registry row, the leg exits non-zero and names that file and delimiter; unstaging restores
  green. This is the gate's failing case, observed before the unit lands.
  Red when: the staged break passes, which would mean the leg is graded by its registry rather than by
  the tree.
- **AC8** — When `bash tools/run-gates/run-gates.sh` runs with the new rows in place, both new legs
  appear in the reported set, and the legs named in §7 stay green — the budget leg included, which
  refuses a held leg carrying no budget row.
  Red when: a new leg lands with no budget row, or with a guard naming an untracked path, which the
  run-gates canary refuses.
- **AC9** — When `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is re-read, its gating
  section names this leg rather than saying nothing sweeps the tree, and hygiene check 18 stays green
  over it under `check-memory-hygiene.sh`.
  Red when: the record still reads "Nothing sweeps other kits", which is the stale-claim class this
  repo audits for.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit selfcheck` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `every held leg is budgeted, every budget row resolves` · `testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)` · `line length`

The three unattended legs are named because all three source the changed library; `pass-order history`
and `brief-recorded` both source `lib-unattended.sh` without calling `pass_commit`, so they are the
regression surface for the file rather than for the function.

New arm: tools/gate-lint/sh_hygiene.py --selftest · a fixture shell file carrying one loop fed by a command substitution and one fed by a plain heredoc, asserting the scan names the first and not the second · none

New arm: tools/gate-lint/sh_hygiene.py (the tree scan) · stage the banned construct into a tracked shell file that carries no registry row, confirm the leg names it RED, then unstage · none

## 8. Open questions

- **Fork A — does the ban cover `done < <(…)`, the process-substitution form?** It has the same EOF
  dependency: the reader blocks until the last write end closes, and with `GIT` being a shell function
  the writer is a bash subshell with a `git` grandchild, which is the same two-level shape that bit.
  Against banning it: `TOOL-dScriptedRepeat-13` records that a NUL stream CANNOT ride a heredoc,
  because command substitution strips NUL bytes, so process substitution is the only form left for
  those consumers — and there are 21 sites in 10 files, several of them exactly that case.
  Recommendation: leave it out of the failing population, count it and print the count on every run so
  a green line is never read as covering it. This is the owner's because it is a choice between an
  incomplete gate that lands and a complete one that contradicts a landed decision.
- **Fork B — are the 19 carried sites drained, and by whom?** The registry is shrink-only, so they can
  sit at 19 forever without redding anything, and a ratchet that never drains is a waiver wearing a
  ratchet's clothes — this repo's own phrase, from the `py.file` pin. Against draining: twenty edits
  inside the two largest gate scripts in the tree, none of which has been observed to hang.
  Recommendation: a backlog row against the tooling family rather than a unit of this build, so the
  drain is scheduled rather than either forgotten or forced into this diff.

RESOLVED (agent, 2026-09-10, delegated) Fork A: the failing population is the
substitution-carrying heredoc only. The process-substitution form is COUNTED and its count
PRINTED on every run, so a green line never reads as covering it. Banning it would contradict
TOOL-dScriptedRepeat-13, which records that a NUL stream cannot ride a heredoc, and M3 veto 1
refuses an option that breaks a landed decision this spec does not own. Charter section 7's
skip-must-announce-itself rule is what makes the incomplete gate honest rather than green by
absence.

RESOLVED (agent, 2026-09-10, delegated) Fork B: a backlog row against the tooling family, not a
unit of this build. Draining is twenty edits inside the two largest gate scripts in the tree,
none of which has been observed to hang, while this build is repairing that same machinery. M3
tie-breaks on fewer open questions and on reuse; the row records the debt where the next session
reads it.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` reports `unscanned layers: .sh` on this subject and is
therefore BLIND to the entire surface this unit touches, which is shell. No "no existing seam fits"
claim rests on it and none is made here; the trace records the same result for all three of this
build's subjects. The seam was found by hand instead and this unit EXTENDS it:
`tools/gate-lint/ps-hygiene.py`, the repo's existing source-hygiene scan over a language whose
failures are silent, whose kit declares a hole for the leg wiring it has never had. Two candidate
seams were examined and rejected in §4: `tools/unattended/unattended.test.sh`'s existing
`out=$(timeout` ban, which is scoped to one kit and is not on the bar, and a new top-level
`tools/check-*.sh`, which would be a second scanner for a kind that already has a home.

Recall terms used: `python tools/memory-recall/query.py "why does a while-read loop in this repo take
a heredoc instead of a pipe, and what gates the command-substitution EOF class in shell" --terms
"heredoc pipe subshell command substitution EOF deadlock while read return pass_commit shell gate ban
scan"`. That query is what surfaced `TOOL-dScriptedRepeat-13`'s NUL finding, which is the whole of
fork A's counter-argument and is not reachable from the trace.
