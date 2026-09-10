# TOOL-aLeakedHandle-1 — the pipe whose write end nobody closed, and the gate for its class

**Status:** CLOSED · rev-5 · 2026-09-10 · node a · Tier-2 · base 013b1af9 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md](../build/2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md) | research | TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3 |
| [2026-09-10-build-TOOL-aLeakedHandle-1-2-acceptance-ledger.md](../build/2026-09-10-build-TOOL-aLeakedHandle-1-2-acceptance-ledger.md) | journal | — |
| [2026-09-10-prompt-TOOL-aLeakedHandle-1-0-run-mandate.md](../prompts/2026-09-10-prompt-TOOL-aLeakedHandle-1-0-run-mandate.md) | journal | — |
| [2026-09-10-prompt-TOOL-aLeakedHandle-1-1-build-brief.md](../prompts/2026-09-10-prompt-TOOL-aLeakedHandle-1-1-build-brief.md) | journal | — |
| [2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit-round2.md](../reviews/2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit-round2.md) | spec-audit | TOOL-aLeakedHandle-2 |
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
  because it currently states that the kit ships no leg of its own. A leg NAME is a `gate-legs`
  inventory key, so the same step claims both new names in the codebase map and re-renders the
  generated map artifacts in that commit. Observed by AC7, AC8 and AC10.
  Both rows declare all four fields the manifest requires; a row is otherwise unbuildable, because
  `run-gates.gov.test.sh:260` reds a row whose `ceiling` is absent or is not a positive integer, and
  `govkit.py`'s 7h reds a leg no descriptor claims. Every one of the 104 rows in the manifest carries
  `name`, `argv`, `chunk`, `subject` and `ceiling`, and 61 of them carry `guard`; of the 51 rows in
  `chunk: selftests`, 45 declare `subject: kit` and 47 carry a `guard`. Those five figures are
  PINNED, read out of `tools/gate-legs.json` on 2026-09-10 at base `013b1af9`.
  - `shell hygiene (a loop fed by a command substitution)`, the tree scan — `chunk: product`,
    `subject: repo`, NO guard, `ceiling: 300`. All eleven `chunk: product` rows are repo-wide source
    scans and every one of them carries no guard, `line length` and
    `install-prefix (shipped surface)` included — PINNED, counted on 2026-09-10 at base `013b1af9`.
    This leg grades every tracked `*.sh`, so no subset of paths bounds it and a guard could only make
    it skip the file that just broke. `subject: repo` because a failure of this leg is a statement
    about THIS repository's shell tree, not about the kit that ships the scanner.
  - `shell-hygiene selftest`, the `--selftest` arm — `chunk: selftests`, `subject: kit`,
    `guard: ["tools/gate-lint/"]`, `ceiling: 300`. That is the majority shape among the self-test
    rows counted above, and it puts this leg under the 2026-08-23 kit-self-test hold deliberately: a
    suite that stages breaks into a copy of a scanner has a job only when that scanner's source
    changes. The guard names the kit dir the scanner lives in, so the leg runs when the thing it
    grades moves and skips when it has not.
  - Both ceilings are 300, which is the value every fast leg in the manifest carries and which clears
    `ceiling-margin.txt`'s declared headroom of `max(120s, 1.0 x max)` for a scan measured in
    seconds. Neither row is added to `tools/run-gates/ceiling-evidence.txt`: a leg with no evidence
    row is REPORTED by `derive-ceilings.py --check` and is not a failure, verified by reading that
    function on 2026-09-10.
  - The held row takes a `tools/run-gates/selftest-budgets.txt` row and the unheld one does not.
    `run-selftests.sh --check` demands a budget row for every leg whose `subject` is `kit` OR whose
    `chunk` is `selftests`, which is the self-test row alone.
  - `tools/gate-lint/kit.toml` gains a `[[gate_leg]]` block per row, each naming the same `subject`
    the manifest declares. `govkit.py`'s 7h compares the two spellings in both directions and reds a
    descriptor that disagrees with the manifest about which side of the bar a leg sits on.
- **S6** — `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` gains a gating clause naming this
  leg and the construct its predicate actually matches. The record's existing sentence that nothing
  sweeps other kits for the `out=$(timeout` form STAYS, because this leg does not scan for that form.
  Observed by AC9.
- **S7** — `.unattended.conf`'s `SHARED_RECORDS` gains `memory/project/readme-contract.txt`. An
  ADDED scope item, per the build method's AMEND rule: building uncovered it and speccing could
  not have. Observed by AC11.

## 3. Non-goals (OUT)

- The other nineteen sites the scan finds are NOT fixed here. They are carried in the registry and
  drained by a separate unit, if the owner wants them drained at all; see §8 fork B. Those nineteen
  sit in six files spread over the tool root, the memory-tree kit and the unattended kit, and the §4
  population table owns the per-file split. Draining them is a different diff with a different risk
  profile from fixing the one that deadlocked.
- The `done < <(…)` process-substitution form is NOT banned. It is counted and reported by the scan
  and is out of the failing population; see §8 fork A.
- No EXISTING ceiling is raised, lowered or re-derived. `unattended kit gate` keeps the 16040 s it
  has, and `derive-ceilings.py` is not re-run. The non-goal is scoped to the ceilings that exist at
  the base sha, because a leg row that declares no ceiling is refused by
  `run-gates.gov.test.sh:260`: the two rows S5 mints each declare one of their own, and S5 states
  both numbers.
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

There is a prior decision in the neighbourhood and it is cited rather than quietly stepped over.
`memory/gotchas/bounded-through-a-pipe-is-unbounded.md` records, in its gating section, that adding a
repo-wide source scan is cheap and is not done there. That sentence is about the `out=$(timeout`
form, and this unit does not build a scan for it. What this unit builds is a repo-wide scan for the
sibling construct, and the decision not to sweep for the substitution-captured timeout stands
untouched — the seam now exists if a later unit wants it, which is a fact for that unit's author and
not a licence this one takes.

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
| `tools/gate-lint/sh_hygiene.py` | `py.file`, and it is UN-ARMED | UNDERSCORE, not the sibling's hyphen, and NOTHING GRADES THAT. The cell for a file basename is `py.file`; `.lexicon.conf`'s `CELLS:` block declares four rows and that is not one of them, so `lexicon naming predicates` cannot fail on this name either way. The underscore is a documented convention with no gate behind it. `ps-hygiene.py` is one of the hyphenated Python basenames `TOOL-aSurfacedLexicon-15` exists to rename, and matching it would grow a debt that already has a unit waiting. |
| `memory/project/substitution-fed-loops.txt` | none | Declared in `PROJECT_REGISTRY_EXTRA`; hygiene check 3 admits `memory/project/` members only through that key. |
| leg `shell hygiene (a loop fed by a command substitution)` | none | The tree scan. |
| leg `shell-hygiene selftest` | none | The `--selftest` arm. |

Every function the new file mints is snake_case. `sh.function` is armed with `sh.function.conv` pinned
at 6 as a two-sided equality, so a non-conforming shell function name added by the fix would move a
pin in the wrong direction; the fix mints no shell function.

### The map claim, and why it is not optional

Rows 3 and 4 of that table are not only leg names. `map_extractors.py` builds the `gate-legs`
inventory by reading every leg's `name` out of `tools/gate-legs.json`, so each new name is a new
inventory key, and `codebase-map coverage + freshness` refuses an unclaimed one.

This was REPRODUCED on 2026-09-10 against base `013b1af9`, not predicted. `compute_coverage` over the
live map tree returns clean today; with the two declared names added to that inventory it returns
`unclaimed: {'gate-legs': [both new names]}`. That leg carries no `guard` in the manifest, so it runs
on every bar including a diff-scoped one, and `baseline.toml` cannot absorb the keys — its own header
reserves additions for the initial backfill.

The claim is a NEW dossier, `gate-lint.md` under `memory/map/features/`. `gate-lint` is today an
unclaimed `kits` key sitting in `baseline.toml` with no dossier, so the kit gets its first one and it
claims both new leg names and that kit key. Claiming the kit key deletes its `baseline.toml` row in
the same commit, because the ratchet's fourth assert refuses a key that is both claimed and
baselined. A new dossier is also graded for a `## Reuse affordance` section: `affordance-exempt.toml`
is shrink-only and graces only the dossiers that existed when it was seeded.

The three artifacts under `memory/map/generated/` are byte-compared by that same leg and are
re-rendered with `python3 tools/codebase-map/gen_map.py --write`. `symbols.json` moves too, and for a
reason unrelated to the legs: the symbol tier indexes the Python under `tools/`, `ps-hygiene.py`
included, so a new Python file in this kit adds rows to it.

The remedy is authored prose, not a script run. Budget it as such — the regen is seconds and the
dossier is not.

### The population, measured

Measured on 2026-09-10 against base `013b1af9`, by a scan written to the predicate this unit ships and
recorded with this spec. Every figure below is PINNED at that base; the leg DERIVES its own counts at
run time and prints them.

| Class | Sites | Files | In the failing population |
|---|---|---|---|
| Loop fed by a heredoc holding a command substitution | 19 | 6 | yes |
| Loop fed by a here-string holding a command substitution | 1 | 1 | yes |
| Loop fed by a heredoc with NO command substitution | 29 | 13 | no |
| Non-loop heredoc holding a command substitution | 3 | 2 | no |
| Non-loop here-string holding a command substitution | 21 | 3 | no |
| Loop fed by a process substitution, `done < <(…)` | 27 | 10 | no, counted and reported |

The twenty in the failing population sit in seven files: `check-microformats.sh` (1),
`check-verdict-epoch.sh` (2), `check-unattended.sh` (8), `lib-unattended.sh` (1), `unattended.sh` (6),
`unattended.test.sh` (1) and `check-memory-hygiene.sh` (1, the here-string). S1 removes the
`lib-unattended.sh` one, so the registry seeds at 19.

The near-miss rows matter as much as the hit rows. The 29 loop-heredocs with no substitution are the
false-positive class: their bodies are a plain `$var` expansion, they fork nothing, and a predicate
that redded them would red thirteen innocent files. The 21 non-loop here-strings are assertion
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
| `tools/gate-legs.json` | two rows, each declaring `chunk`, `subject`, guard-or-none and `ceiling` |
| `tools/run-gates/selftest-budgets.txt` | one row, for the held self-test leg only |
| `tools/govkit/subject-pins.tsv` | regenerated, because a new leg reds `govkit selfcheck` unpinned |
| `memory/map/features/gate-lint.md` | new, the dossier claiming both new leg names and the `gate-lint` kit key |
| `memory/map/baseline.toml` | the `gate-lint` row under `kits` is deleted |
| `memory/map/generated/MAP.md` | re-rendered |
| `memory/map/generated/inventories.json` | re-rendered |
| `memory/map/generated/symbols.json` | re-rendered, because the new Python file adds symbols |
| `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` | the gating paragraph |
| `.unattended.conf` | S7's one member on `SHARED_RECORDS` — the AMEND, added at rev-5 |
| `tools/gate-lint/README.md` | the sentence saying the kit ships no leg of its own, which S5 made false |
| `memory/gotchas/INDEX.md` | re-rendered; the record's anchor count moved |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped, twice; three watched files moved |

### Alternatives rejected

- **`done < <(GIT log …)`, the process-substitution form.** Rejected on the mechanism.
  `TOOL-dScriptedRepeat-13` records process substitution as the form that keeps a loop in the current
  shell, and it is correct about that, but it does not close this hole: `GIT` is a shell function, so
  the substitution forks a bash subshell which forks `git`, and the reader still depends on a
  grandchild's write end closing. It replaces one pipe with another.
- **A ban with no registry, draining every measured site in this unit.** Rejected on blast radius.
  That is every row of the population table above, spread over seven files in the unattended kit, the
  memory-tree kit and the tool root — a bigger and riskier diff than the deadlock it closes, and the
  registry ratchets the same outcome without one landing. The table owns the per-file split; no
  count is restated here.
- **A new top-level `tools/check-*.sh`.** Rejected for `tools/gate-lint/`, which already owns this
  kind. A second scanner for the same kind at the tool root is the copy-instead-of-extend shape §12
  names, and it would owe a `govkit` entry descriptor that the kit route does not.
- **An arm in `tools/unattended/unattended.test.sh`, beside the existing `out=$(timeout` ban.**
  Rejected because that suite is scoped to one kit and, by the owner ruling of 2026-08-23, is not on
  the bar at all. An arm there gates the class in one directory and runs on demand.

## 5. Production-readiness checklist

- security — N/A. No new write path, no untrusted input, no egress. The scan reads tracked source and
  writes only its own registry under `--write`.
- perf / scale — the scan is a single pass over 105 tracked `*.sh` and costs milliseconds; each new
  leg row declares its own ceiling of 300 s, which S5 states and defends. The fix trades one subshell
  fork for one `mktemp` spawn per (anchor, unit) pair.
- error / empty / loading states — an empty scan population is a REFUSAL, not a pass, because a scan
  that graded nothing reports the same zero as a clean tree. An unreadable registry is a refusal. A
  `mktemp` failure in the fix is the named refusal S2 specifies.
- observability — the scan prints EVERY measured population on every run — the six rows of §4's
  population table, in that order — green included, so the
  reported-not-gated process-substitution count is never mistaken for coverage. The leg header states
  what it does NOT check.
- risks — each with its remedy, and the first of them is the one the round-1 spec audit caught
  missing. `codebase-map coverage + freshness` reds on both new leg names as unclaimed inventory
  keys; it carries no guard, so it runs on every bar, and the remedy is the dossier §4 specifies
  rather than a regen. `every held leg is budgeted, every budget row resolves` refuses a HELD leg
  with no budget row, and S5 declares exactly one of the two rows held, so one budget row is added
  with it. `govkit selfcheck` reds a new leg until `tools/govkit/subject-pins.tsv` carries a row for
  it, so both names are pinned in the same commit with
  `python tools/govkit/govkit.py selfcheck --write`; that file is GENERATED and is regenerated
  rather than hand-edited. `harness arms (fail branches armed or pinned)` grades the new file's
  refusal branches, which may want an `ARMS_FLOORS` row.
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
  Red when: the fix puts the loop behind a pipe, so `return 0` exits the SUBSHELL rather than the
  function, execution falls through to the trailing `return 1`, and the function answers "this
  pass has not committed" for a pass that has. OBSERVED at rev-4 on a staged copy: `rc=1` with
  the correct sha still on stdout, because stdout is shared with the pipeline's subshell. An arm
  asserting only the printed value is satisfied by the broken shape; the return code is the half
  that moves.
- **AC2** — When `bash tools/run-gates/run-gates.sh` runs on node `a` with the fix in place, the row
  for `unattended kit gate` in `<git-dir>/gate-ledger.tsv` reads status `ok` with a seconds figure
  below that leg's declared ceiling of 16040.
  Red when: the row still reads `fail`, or its seconds exceed 16040, or the run's wall guard kills
  the leg and it writes no `.sec` at all, so no row for it is rewritten this run.
  cost: one bar. The leg alone measured 4168 s on the killed run of 2026-09-10.
  fixture: a tree carrying dispatch rows for that leg to walk; this worktree has one.
  figure: DERIVED — the seconds and the status are read from the ledger at observation time. The
  4168 s and the ceiling of 16040 are PINNED at 2026-09-10 on base `013b1af9`.
  THE THIRD `Red when:` CLAUSE CONTRADICTS `TOOL-aLeakedHandle-3` §4, and this side is the one that
  matches source. That spec's *The value to print* paragraph says `run_leg_reap` kills the leg's own
  process and leaves the `runleg` subshell to finish, so `.sec` is written there too. It is not:
  `runleg` writes its own `$BASHPID` to `$WORK/<i>.pid` at `run-gates.sh:1367`, the wall watcher
  feeds that pid to `run_leg_reap` at `run-gates.sh:1604`, and `scan_descendants` seeds its kill set
  with the pid it was given at `run-gates.sh:429`. The subshell dies before `run-gates.sh:1409`
  writes `.sec`, the ledger loop's `[ -f "$WORK/$i.sec" ] || continue` at `run-gates.sh:1673` skips
  it, and the awk carry-forward at `run-gates.sh:1690` preserves the previous run's row — which is
  the whole reason this clause exists, because a stale `fail` row surviving a killed run is how an
  observer records a green from a row the run did not produce. Verified against source on
  2026-09-10 at base `013b1af9`. Unit 3's CONCLUSION survives: `report_one` returns early when `.rc`
  is absent, so its rc=137 branch is unreachable on the wall path and its new `.sec` read is safe —
  safe because the branch is unreachable, not because the file exists. Reconcile the pair before
  either lands; nothing in this unit changes either way.
  ONE INVOCATION, deliberately. A direct `bash tools/unattended/check-unattended.sh` run emits the
  verdict and nothing else: that script contains no reference to a ledger, and every row of
  `<git-dir>/gate-ledger.tsv` is written by the one block in `tools/run-gates/run-gates.sh` that owns
  it. Splitting the observation across two commands is how an observer records a green from the half
  that could not produce it. A green here does not by itself PROVE the deadlock is gone, because the
  hang was intermittent and the leg passed on other runs with the defect present. AC3 is the
  criterion that proves it, by absence of the construct.
- **AC3** — When the scan runs over the tree, `lib-unattended.sh` appears in neither its hit list nor
  the registry, and `grep -c 'PASSCOMMITS'` over that file returns 0.
  Red when: the fix leaves the substitution in place and the site is carried in the registry instead.
- **AC4** — When the scan runs over the tree at the base sha with the fix applied, it reports 19 sites
  in 6 files as its failing population, and names none of the 29 substitution-free loop heredocs, the
  3 non-loop heredocs, the 21 non-loop here-strings or the 27 process-substitution loops.
  Red when: the predicate names a loop heredoc whose body holds no command substitution, which is the
  false-positive class and the one that would red thirteen innocent files.
  figure: DERIVED — the scan prints every count; the six figures above are PINNED at 2026-09-10 on
  base `013b1af9`, and three of the NEAR-MISS figures moved at rev-4 when the shipped predicate
  re-measured them. No figure in the failing population moved.
- **AC5** — When the scan runs with `--selftest`, it builds a fixture holding one loop fed by a
  command substitution and one fed by a plain heredoc, and asserts that the predicate names the first
  and not the second, printing its executed assertion count.
  Red when: an arm is stranded past an early exit and the count falls, or the selftest passes on a
  fixture whose failing case was never built.
  Run it directly, as the `--selftest` arm of `tools/gate-lint/sh_hygiene.py`, rather than
  through the bar. The leg S5 wraps it in is `chunk: selftests` and `subject: kit`, so no push
  boundary and no default bar executes it; AC8 is the criterion that observes it as a LEG, and it
  pays a flagged bar to do so. The full path resolves because `check-spec-tokens.py` joins §6's
  backticked path tokens against `git ls-files`, and the unit's own commit stages that file.
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
- **AC8** — When `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs with the new rows in
  place, both new legs appear in the reported set and every leg named in §7 is green, the two
  canaries and the budget leg included.
  Red when: a new leg lands with no budget row, which `every held leg is budgeted, every budget row
  resolves` refuses; or with a guard naming an untracked path, which `run-gates canary` refuses.
  cost: a bar with every self-test run, which is the most expensive form of this observation.
  THE DEFAULT BAR CANNOT OBSERVE THE SECOND HALF. `run-gates canary` and `run-gates gov canary` are
  both `chunk: selftests`, and the runner holds every `subject = kit` or `chunk = selftests` leg
  unless `GATE_SELFTESTS=1` is set, which no boundary sets. Held legs still print, as
  `GATE held <name> (self-test, set GATE_SELFTESTS=1 to run)`, so a plain
  `bash tools/run-gates/run-gates.sh` shows the untracked-path arm as a row and never runs it. That
  matters here rather than in the abstract: `run-gates gov canary`'s own guard names
  `tools/gate-legs.json`, which S5 edits.
  ONE FLAG IS ENOUGH HERE AND IS NOT ENOUGH IN GENERAL. `GATE_SELFTESTS=1` lifts the HOLD; a leg's
  `guard` is a separate pass that only `GATE_FULL=1` or an unresolvable BASE short-circuits. This
  criterion needs no `GATE_FULL=1` because every guard involved is dirty on this unit's own diff:
  `run-gates gov canary` guards on `tools/gate-legs.json`, `shell-hygiene selftest` guards on
  `tools/gate-lint/`, `run-gates canary` guards on `tools/`, and S5 edits all three. A later session
  re-running this observation on a tree where those paths are clean gets an announced skip rather
  than a reading, and needs `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.
- **AC9** — When `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` is re-read, its gating
  section carries a NEW clause naming this leg and the construct its predicate matches, which is a
  `while` loop fed by a heredoc or here-string whose body holds a command substitution; the section
  still carries its existing sentence that nothing sweeps other kits for the `out=$(timeout` form;
  and hygiene check 18 stays green over the record under `check-memory-hygiene.sh`.
  Red when: the added clause claims the leg covers the `out=$(timeout` form, or the existing sentence
  is deleted or weakened to make room for it.
  WHY THE SENTENCE STAYS, because the obvious edit is the wrong one. `out=$(timeout N cmd)` is a
  plain assignment, and this unit's §4 population table puts every non-loop command substitution
  OUTSIDE the failing population. So that sentence is TRUE before this unit lands and TRUE after it,
  and a criterion that reds until somebody rewrites it would go green only once a correct coverage
  claim had been replaced by a false one — inside the record that exists to catalogue exactly that
  failure. The gap this leg closes is a sibling construct, and the record says so in its own words.
- **AC10** — When `python3 tools/codebase-map/test_codebase_map.py` runs over the tree with both new
  leg rows and the new dossier in place, it passes: neither new leg name is reported unclaimed,
  neither is reported as a stale claim, `gate-lint` no longer appears in `memory/map/baseline.toml`,
  and the three artifacts under `memory/map/generated/` byte-match a fresh render.
  Red when: the leg rows land without the dossier, which is the reproduced failure — that suite then
  names both leg names under UNCLAIMED. It reds a second way if the dossier claims the `gate-lint`
  kit key while the `baseline.toml` row survives, because a key that is both claimed and baselined
  fails the ratchet's fourth assert.
  figure: DERIVED — the suite names every offending key itself.
  This is the criterion that makes the map claim an observation rather than an intention, and it runs
  on an ordinary bar: `codebase-map coverage + freshness` is `chunk: declarations` and carries no
  guard, so nothing about this one is held.

- **AC11** — When `bash tools/unattended/check-pass-order.sh` and
  `bash tools/unattended/check-brief-recorded.sh` run over the tree with this unit CLOSED and its
  build commit landed, both exit 0 and neither names `TOOL-aLeakedHandle-1`; the corpus-wide
  populations are unchanged at 150 closed units graded by the first, and both rows in
  `memory/project/pass-order-waiver.txt` still resolve rather than reporting as stale.
  Red when: the exclusion is widened far enough to change another unit's selected build commit,
  which shows up as a moved graded-unit count or a waiver row that has gone stale — the shape a
  blanket cutoff move would have.
  figure: DERIVED — both legs print their own populations. 150 is PINNED at 2026-09-10.
  WHY THIS IS AN AMENDMENT AND NOT A FIX TO THIS UNIT'S OWN CODE. Neither leg is about
  `pass_commit` or the scan. They went red the moment this unit's status header read CLOSED,
  because that is when a unit becomes graded, and the commit they misread is this build's SPEC
  commit — which appended the README-contract row a new build folder owes. History is append-only
  and that commit cannot be re-shaped, so the choice was between a declared exemption and naming
  the file what it is. `pass-order history` has a waiver registry and `brief-recorded`
  deliberately has none, so an exemption could only have closed half of it.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit selfcheck` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `every held leg is budgeted, every budget row resolves` · `testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)` · `line length` · `codebase-map coverage + freshness` · `run-gates canary` · `run-gates gov canary`

The three unattended legs are named because all three source the changed library; `pass-order history`
and `brief-recorded` both source `lib-unattended.sh` without calling `pass_commit`, so they are the
regression surface for the file rather than for the function.

`codebase-map coverage + freshness` is named because S5's two leg names are two new `gate-legs`
inventory keys. It is `chunk: declarations` with no guard, so it runs on every bar and reds on this
unit unless the map claim lands with the leg rows. §4 has the reproduction.

**Two of the legs above are HELD on an ordinary bar, and the list would lie without this line.**
`run-gates canary` and `run-gates gov canary` are both `chunk: selftests`, which the runner holds
unless `GATE_SELFTESTS=1` is set — and no boundary sets it, by the owner ruling of 2026-08-27. They
are named anyway because `run-gates gov canary`'s guard names `tools/gate-legs.json`, which S5 edits,
and because the canaries hold the arm that refuses a guard naming an untracked path, which is exactly
the mistake a new leg row can make. Run them by hand for this unit; AC8 names the invocation. Every
other leg on that line runs on an ordinary bar with no flag.

**Of the two legs S5 mints, an ordinary bar runs the tree scan and holds the self-test.**
`shell hygiene (a loop fed by a command substitution)` is `chunk: product`, `subject: repo` and
carries no guard, so every bar runs it, diff-scoped ones included — which is the point, since the
construct it refuses can arrive in any tracked `*.sh`. `shell-hygiene selftest` is `chunk: selftests`
and `subject: kit`, so the runner holds it unless `GATE_SELFTESTS=1` is set, and no boundary sets
that. AC5 is therefore observed by running the file directly and AC8 by the flagged bar; neither
observation is bought by a push.

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
  ratchet's clothes. That phrase is this repo's own, from the `.lexicon.conf` comment recording why
  `py.file` and `py.constant` were left UN-ARMED rather than pinned over rows nobody can drain; there
  is no live `py.file` pin, and the four-row `CELLS:` block is the check. Against draining: nineteen
  edits across six files in the unattended kit, the memory-tree kit and the tool root, none of which
  has been observed to hang. The §4 population table owns the per-file split.
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
unit of this build. Draining is nineteen edits across six files in the unattended kit, the
memory-tree kit and the tool root, none of which has been observed to hang, while this build is
repairing that same machinery. M3 tie-breaks on fewer open questions and on reuse; the row records
the debt where the next session reads it, and it cites the §4 population table for the split rather
than carrying a per-file count of its own.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft.
- rev-2 · 2026-09-10 · §2 S5 · S6 · §3 · §4 · §5 · §6 AC2 · AC8 · AC9 · AC10 · §7 · §8 · folded the
  round-1 spec audit's D1, D2, D5, D8, D9 and D10.
  D1, the blocker: a leg NAME is a `gate-legs` inventory key, and `compute_coverage` returns both new
  names UNCLAIMED against the live map tree — reproduced here, not taken on the reviewer's word. §4
  gains the map-claim section and five `memory/map/` rows in the files table, §5's risks gains the
  leg it had missed, §7 names the gate, and AC10 observes the claim.
  D2: §7 discloses that both run-gates canaries are `chunk: selftests` and held on an ordinary bar,
  and AC8 moved to the invocation that actually runs them.
  D5: S6 and AC9 no longer demand that the gotcha's true `out=$(timeout` coverage sentence be
  deleted. The record gains a clause naming this leg's own class and keeps the sentence.
  D8: the "twenty edits in two files" figure is gone from §3, §4 Alternatives, fork B and fork B's
  RESOLVED mark. The mark's DECISION is unchanged; only its blast-radius figure moved, to agree with
  the §4 population table, which the four passages now point at instead of restating.
  D9: the Inventory row's cell is `py.file` and is marked UN-ARMED, so the underscore is disclosed as
  a convention nothing grades. Fork B's "waiver wearing a ratchet's clothes" is re-attributed to the
  `.lexicon.conf` comment; no `py.file` pin exists. The stale count of hyphenated Python basenames
  came out of the same row rather than being re-measured.
  D10: AC2 is one invocation. `check-unattended.sh` writes no ledger row and applies no ceiling, so
  the criterion now rides the bar run that produces both halves.
- rev-3 · 2026-09-10 · §2 S5 · §3 · §4 · §5 · §6 AC2 · AC5 · AC8 · §7 · folded the round-2 spec
  audit's D4 and D6, the two mediums it assigns to this unit.
  D4: S5 declares `chunk`, `subject`, guard-or-none-with-its-reason and `ceiling` for each of the two
  new manifest rows, plus the budget row and the descriptor `[[gate_leg]]` blocks those values imply.
  The tree scan is `product`/`repo`/unguarded/300 and the self-test is `selftests`/`kit`/guarded on
  `tools/gate-lint/`/300. §3's ceiling non-goal is scoped to EXISTING ceilings, which removes its
  contradiction with §5 perf/scale; §5 risks now says the budget rule reaches the HELD row only and
  names the `subject-pins.tsv` regeneration a new leg owes; the files table gains that pin file and
  the budget file; §7 says which of the two an ordinary bar runs. AC5 and AC8 disclose the hold and
  the guard separately, because `GATE_SELFTESTS=1` lifts only the first.
  D6: AC2 is unchanged and now carries a pointer that its third `Red when:` clause contradicts
  `TOOL-aLeakedHandle-3` §4, with the five source lines that decide it. The wall guard kills the
  `runleg` subshell, so a wall-killed leg writes no `.sec` and the ledger carries its previous row
  forward. Unit 3's conclusion holds for a different reason than the one it writes down, and that
  repair is unit 3's to make.

- rev-4 · 2026-09-10 · §4 · §5 · §6 AC1 · AC4 · AC5 · the build pass, correcting four figures the
  shipped predicate re-measured and one failure mode a staged control disproved.
  §4's population table and AC4: the three NEAR-MISS counts moved — 29 substitution-free loop
  heredocs sit in 13 files and not 17, the non-loop heredocs holding a substitution are 3 and not
  2, and the process-substitution loops are 27 and not 21. Nothing in the FAILING population
  moved: 19 heredoc sites in 6 files plus 1 here-string at the base sha, 19 sites in 6 files with
  the fix applied, and the seven-file split §3 names is exact. The corrected figures are what
  `tools/gate-lint/sh_hygiene.py` prints, so prose and source now agree and the source is the one
  that cannot go stale.
  §5 observability: the scan prints SIX populations, which is §4's table, not four.
  AC1's `Red when:` was wrong about the failure it describes, and the control that proves it was
  run rather than reasoned. A copy of the library with the loop behind a pipe returns 1 and STILL
  PRINTS the sha, because the pipeline's subshell shares stdout — so the criterion as written
  ("prints nothing") named a symptom the defect does not have, and an arm built to it would have
  passed on the broken shape.
  AC5's basename note is retired: the file is staged by this unit's own commit, so the full path
  resolves against `git ls-files` and the token join is satisfied.

- rev-5 · 2026-09-10 · §2 S7 · §6 AC11 · the build pass, one AMEND the method's own rule covers.
  `.unattended.conf`'s `SHARED_RECORDS` gains `memory/project/readme-contract.txt`. Both
  commit-reading legs in §7 went RED the moment this unit's header read CLOSED, and neither was
  about this unit's code: `build_commit` excludes the build folder, the generated indexes and the
  declared shared records from selection, this file is in none of them, and a new build folder is
  OBLIGED to append its README row to it — so this build's spec commit carried one path outside
  the build folder and both legs read the SPEC commit as the build commit.
  It is an ADD rather than a waiver because the file IS a shared mutable record by condition 3's
  own definition, and because only one of the two legs has a waiver registry at all — the other
  says in its own source that an exemption is not coverage. Measured over the whole corpus before
  and after: same 150 closed units graded, both existing waiver rows still resolve, no other
  verdict moved. AC11 is the observation.

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
