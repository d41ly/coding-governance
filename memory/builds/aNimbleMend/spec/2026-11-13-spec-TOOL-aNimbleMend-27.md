# TOOL-aNimbleMend-27 — the close's three red legs repaired: three no-fork forms in the pass-leg adapter, five guards that cover what they import, one manifest bullet inside its cap, and four re-declared rows

**Status:** CLOSED · rev-1 · 2026-11-13 · node a · Tier-1 · base 2ba17e9d · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aNimbleMend-1-runlog-91ca33f2.md](../build/2026-11-13-build-TOOL-aNimbleMend-1-runlog-91ca33f2.md) | journal | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 TOOL-aNimbleMend-13 TOOL-aNimbleMend-14 TOOL-aNimbleMend-15 |
| [2026-11-13-build-TOOL-aNimbleMend-27-1-acceptance-ledger.md](../build/2026-11-13-build-TOOL-aNimbleMend-27-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-prompt-TOOL-aNimbleMend-27-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aNimbleMend-27-brief.md](../prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-brief.md) | research | — |
| [2026-11-13-prompt-TOOL-aNimbleMend-27-build-brief.md](../prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's full bar on the prepared landing merge `b61832752` went red on three legs, each green at
`cac14c195`, the default branch's tip before this build merged. This unit repairs the three, so the
close's bar can read green.

## 2. Scope (IN)

- **S1** — `tools/run-gates/pass-legs.sh` computes `KITDIR`, `PL_STARTED` and `PL_RUN` with no fork
  spent on builtin work: a `case` on `$0` with `${0%/*}`, and two `TZ=UTC0 printf -v` stamps. Each
  variable holds the bytes it held. Observed by AC1, AC2 and AC9.
- **S2** — Three rows of `memory/project/spawn-idiom-sites.txt` are re-declared at the counts the
  close's bar measured, each with a reason naming this build. This is the main loop's decision
  (PINNED, 2026-11-13), stated in §4, and no site of the three suites is converted here.
  Observed by AC3 and AC4.
- **S3** — Five rows of `tools/gate-legs.json` gain one guard path each, so each leg's guard covers
  the module its entry now imports, and the `pass_leg` field is re-applied by
  `python tools/run-gates/pass_legs.py --apply`. Observed by AC5 and AC6.
- **S4** — The bullet of `memory/guides/SESSION-KICKOFF.md` that opens `- A card's` and that this
  build lengthened past the line cap is split at its sentence boundary into two bullets, each inside
  the cap, so the `manifest-check` row of `memory/project/fork-ceilings.txt` measures a passing run
  again and its ceiling stays. Observed by AC7 and AC8.
- **S5** — The `memory-hygiene` row of `memory/project/fork-ceilings.txt` rises by one, to the
  measured count, with its reason appended: the one call check 31 delegates. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- Draining the fork idioms of the three suites of S2. An ask files the drain, and the main loop
  files the ask.
- Any change to `skills/session-kickoff/manifest-check.sh` or to
  `tools/memory-tree/check-memory-hygiene.sh`.
- Moving `read_policy_value` out of `tools/memory-tree/tree_lib.py` (§4, "Alternatives rejected").
- A new suite arm. No suite file is edited, so no suite run is owed and no count of S2 moves again.
- Any kit version, which the lander's `mint` moves.
- Any edit to a CLOSED spec of this build. Each correction is stated here.
- The disposal of asks TOOL-aNimbleMend-25 and TOOL-aNimbleMend-26, which is the main loop's.

### Edges

- **consumes-from** external — the code of this build's CLOSED units 5, 8 and 9: the pass-leg
  adapter, the policy read in `tree_lib.py`, and check 31 of the hygiene engine.
- **hands-off** external — the ask that drains the three suites' idiom sites, filed by the main loop.
- **hands-off** external — the re-audit of the kickoff manifest's audit block after S4's body edit
  and S3's edit of a watched file, which the main loop makes as it does after every such pass.

## 4. Design

### Evidence

Read at `602f8952`, the branch tip. The red lines are in `gate-logs/` of this worktree's git
directory, beside the failure record `gate-last-failure.txt`.

| Leg | What it printed | Cause, verified |
|---|---|---|
| shell hygiene (a fork spent on builtin work) | 2 `date-fmt` and 1 `path-subst` site in `pass-legs.sh`, no row | `tools/run-gates/pass-legs.sh@602f8952:43`, `:326` and `:329`, landed by unit 5 |
| the same leg | three registry counts rose | arms this build added to three suites; table under "S2" |
| python reads | `backlog.py` outside four guards, `id_grammar.py` outside one | one import, `tools/memory-tree/tree_lib.py@602f8952:71`, landed by unit 8 at `93bb9b87a` |
| spawn budget | `memory-hygiene` one over its ceiling | `tools/memory-tree/check-memory-hygiene.sh@602f8952:2015`, check 31, landed by unit 9 |
| spawn budget | `manifest-check` 6 over its ceiling (PINNED, 2026-11-13) | the fixture's run of the ratchet REFUSES at check 8; see "S4" |

### S1 — the three forms

Line 43 becomes the form this file already uses for `_rp_here`, then the location probe it had:

```bash
case "$0" in */*) KITDIR=${0%/*} ;; *) KITDIR=. ;; esac
KITDIR=$(cd "$KITDIR" && pwd)
```

The `case` is owed. A bare `${0%/*}` on a `$0` with no slash yields the script's name, where
`dirname` yields `.`, and the `cd` then fails.

The two stamps become, each on one line and spelled exactly so, because AC2 reads them by pattern:

```bash
TZ=UTC0 printf -v PL_STARTED '%(%Y-%m-%dT%H:%M:%SZ)T' -1
TZ=UTC0 printf -v PL_RUN 'pass-%(%Y%m%dT%H%M%SZ)T-%s' -1 "$$"
```

The second sits where the `PL_RUN=` assignment sits today, inside the `if`. The `TZ=UTC0` prefix is
owed: `date -u` prints UTC and a bare `printf -v` prints local time. Probed on node a under bash
5.3.9, 2026-11-13: the prefixed form equals `date -u` byte for byte and `TZ` is unset after the line.
The bare form read two hours ahead there (PINNED, 2026-11-13). UNVERIFIED: the same equality on a
Linux bash, which no probe of this unit reaches.

### S2 — the three rows, a decision made

The main loop decided this on 2026-11-13: re-declare, do not convert. Converting the sites would owe
a whole run of each of the three suites, about two hours of suite time on node a (PINNED, 2026-11-13).

| Row of `spawn-idiom-sites.txt` | Class | Declared | Measured at `b61832752` |
|---|---|---|---|
| `tools/run-gates/run-gates.evidence.test.sh` | `var-pipe` | 43 | 72 (PINNED, 2026-11-13) |
| `tools/run-gates/run-gates.test.sh` | `var-pipe` | 141 | 156 (PINNED, 2026-11-13) |
| `tools/workflows/unattended-build.test.sh` | `printf-subst` | 66 | 74 (PINNED, 2026-11-13) |

Each row's count becomes the measured one. Each reason follows the shape the `printf-subst` row of
`run-gates.evidence.test.sh` carries for an earlier reconcile: it says the count rose from the old
figure with the arms TOOL-aNimbleMend added, names the close's bar at `b61832752`, and keeps the
row's own sentence naming the no-fork form and the drain by a follow-up unit.

### S3 — guards added, and why not the import taken out

`tools/run-gates/py_reads.py#derive_closure` walks every static import, a function-level one
included. Unit 8 put `from backlog import resolve_kit_dir` inside
`tools/memory-tree/tree_lib.py#read_policy_value`, and `tree_lib.py` is in the closure of all five
legs. `backlog.py` then imports `id_grammar` at `tools/memory-tree/backlog.py@602f8952:1806`. A walk
of the same rule over the tree reproduced the leg's five lines, and with that one import left out it
printed none.

| Leg | Guard path appended |
|---|---|
| `memory-recall kit selftest` | `{prefix}/memory-tree/backlog.py` |
| `recall floor` | `{prefix}/memory-tree/backlog.py` |
| `recall floor arms` | `{prefix}/memory-tree/backlog.py` |
| `drift-audit selftest` | `{prefix}/memory-tree/backlog.py` |
| `policy fixtures` | `{prefix}/memory-tree/id_grammar.py` |

Each path is appended last in its row's `guard`. Then `python tools/run-gates/pass_legs.py --apply`
runs, and `--check` after it.

Guards are added because the leg's contract is the static closure, and the manifest edit is five
lines of data with no suite owed. The cost is stated: an edit of `backlog.py` now starts four more
guarded legs, though none of them calls the function that imports it.

### S4 — the manifest bullet, where the brief and the source disagree

The brief reads the added forks as the cost of grading manifest lines this build added, and
allows a raise. The site diff says otherwise. `--only manifest-check --sites` at this tree and over
an extract of `cac14c195` differ at four sites of `manifest-check.sh`, lines 1655, 1656, 1673 and
1714, summing to the 6 added forks (PINNED, 2026-11-13).
Line 1714 is reached only when check 8 is about to fail. This build lengthened one bullet of the
manifest to 516 bytes against the 400-byte line cap (PINNED, 2026-11-13).
The repository's own ratchet passes on it with a `BUDGET WARN` line, because `.governance/policy.toml`
sets `budgets.enforce` to `warn`. The fork fixture copies the manifest and no policy file, so there
the cap refuses, and the row has been counting a refusing run.

A raise would bank a failing run's count as the ceiling. So the bullet is split after its first
sentence, the one that ends by citing two units of aRoutedQuill, and the sentence opening
`The one exception is the red-fix lane` becomes its own bullet directly beneath. No other byte of
either sentence moves.
The halves measure 227 and 290 bytes (PINNED, 2026-11-13), and the section's own rule is one line per bullet.
The row then measures its ceiling again, and the ratchet's warning goes with the breach.

### S5 — the hygiene row is raised

The one added fork is the command substitution of check 31, which captures the output of
`build_records.py join red-fix`. That is a process the check must start, and no builtin form
captures a child's output: a redirect to a file would hide the start from the counter and cost a
temp file of its own. Check 31 follows check 30's delegation. So the ceiling moves 191 to 192 (PINNED, 2026-11-13).
The reason gains a clause in the row's own style: the raise, this unit, check 31's one delegated
call, and the builder's three `--only memory-hygiene` readings on node a under bash 5.3.

### What it does not check

- A `$0` naming a script at the filesystem root, where `${0%/*}` is empty. No kit installs there.
- The bare-name branch of the `case` at runtime. AC1 reads its shape; no criterion runs it.
- Whether the three suites' counts are as low as they could be. S2 records what is, by decision.
- Whether a guard path is needed at runtime. The leg grades the static closure, and so does S3.
- The fork counter is a lower bound, by its own header: a python child is unseen beyond its subshell.

### Files touched (estimate)

- `tools/run-gates/pass-legs.sh`
- `tools/gate-legs.json`
- `memory/project/spawn-idiom-sites.txt`
- `memory/project/fork-ceilings.txt`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Taking the import out of `tree_lib.py`.** It is the one cause of all five lines, and the
  narrower guard. It moves `read_policy_value` to another module, re-points its two callers, and
  rewrites the arm of `tools/memory-tree/routed_commits.py` that pins the function in `tree_lib`,
  which a CLOSED unit's criterion names and which owes a suite run the close does not make.
- **Raising the `manifest-check` ceiling.** It records the refusal path's count; see "S4".
- **Capturing check 31's output through a temp file.** The process count is unchanged, a `mktemp`
  is a fork the row already paid for once, and a fixed-name temp is what another hygiene leg polices.
- **Declaring three registry rows for `pass-legs.sh`.** The sites are new product code with a
  builtin form each, which is the case the leg exists for.

## 5. Acceptance criteria

A role agent's hook refuses the argv of a manifest leg, so each criterion that runs a leg's own
command says it is the main loop's. The others are probes a builder runs.

- **AC1** — When `grep -c '\$(date' tools/run-gates/pass-legs.sh` runs it prints 0,
  `grep -c 'dirname' tools/run-gates/pass-legs.sh` prints 0, `grep -c 'TZ=UTC0 printf -v' tools/run-gates/pass-legs.sh`
  prints 2, and `grep -c 'case "$0" in' tools/run-gates/pass-legs.sh` prints 1.
  Red when: a site keeps its substitution, a stamp lost its zone prefix, or `KITDIR` took the bare
  expansion. At `602f8952` they print 2, 1, 0 and 0.
- **AC2** — When `bash -c 'eval "$(grep "TZ=UTC0 printf -v PL_" tools/run-gates/pass-legs.sh )"; case "$PL_STARTED" in "$(date -u +%Y-%m-%dT%H)":??:??Z) echo utc ;; esac; echo "$PL_RUN"'`
  runs, it prints `utc` and then a line of the shape `pass-<8 digits>T<6 digits>Z-<digits>`.
  Red when: a stamp is written in local time, which on node a misses the hour, or the run id's
  fields are out of order. A run across the turn of an hour misses once and passes on a second run.
- **AC3** — When `awk -F'\t' '($1=="tools/run-gates/run-gates.evidence.test.sh" || $1=="tools/run-gates/run-gates.test.sh") && $2=="var-pipe" || $1=="tools/workflows/unattended-build.test.sh" && $2=="printf-subst" { print $3, ($4 ~ /TOOL-aNimbleMend/) }' memory/project/spawn-idiom-sites.txt`
  runs, it prints `72 1`, `156 1` and `74 1`. And when
  `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . | grep -cE '^  [^ ]*[^-a-z](pass-legs|run-gates\.evidence\.test|run-gates\.test|unattended-build\.test)\.sh: '`
  runs, it prints 0.
  Red when: a row keeps its old count or a reason names no build, or a site of S1 survives. The
  second command prints 5 at `602f8952`.
  figure: the three counts are PINNED, 2026-11-13, from the close's bar at `b61832752`.
- **AC4** — When `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  runs, it exits 0.
  Red when: any of the five findings stands, or a suite's count moved again after S2.
  permission: the main loop's; the command is a leg's own.
- **AC5** — When `python tools/run-gates/py_reads.py --guards "<leg>"` runs for each of the five
  legs of S3, no output holds a line opening `py-reads: RED`; and `python tools/run-gates/pass_legs.py --check`
  exits 0.
  Red when: a row lacks its appended path, or `--apply` did not run after the manifest moved.
- **AC6** — When `python tools/run-gates/py_reads.py` runs, it prints no line opening
  `py-reads: RED`.
  Red when: a sixth leg reaches a module outside its guard, which the five probes of AC5 cannot see.
  permission: the main loop's; the command is a leg's own.
- **AC7** — When `grep -E '^- (A card.s|The one exception is the red-fix lane)' memory/guides/SESSION-KICKOFF.md | LC_ALL=C awk '{ print (length($0) <= 400) }'`
  runs, it prints `1` twice. And `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only manifest-check`
  prints a line opening `fork-count: ok manifest-check`, and the same with `--only memory-hygiene`
  prints a line opening `fork-count: ok memory-hygiene`.
  Red when: the bullet is unsplit, which prints one line reading `0`, or a ceiling was raised for
  the ratchet's row, or the hygiene row's ceiling is not its measured count.
  figure: the cap is PINNED, 2026-11-13, the constant `MANIFEST_LINE_MAX` of the ratchet.
- **AC8** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` runs, its
  last line holds `0 red`; and `bash skills/session-kickoff/manifest-check.sh` prints no line
  opening `BUDGET WARN — manifest-line`.
  Red when: either row of S4 or S5 is over or slack, or another line of the manifest is over its cap.
  permission: the main loop's; both commands are legs' own.
- **AC9** — When `bash tools/run-gates/pass-legs.sh --base HEAD~1` runs at the unit's pass commit,
  the record `gate-pass-legs.txt` in the worktree's git directory holds a `started` line matching
  `^started\t[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$` whose hour is the UTC hour, and
  a `run_id` line matching `^run_id\tpass-[0-9]{8}T[0-9]{6}Z-[0-9]+$`.
  Red when: `KITDIR` resolves wrongly, so the runner beside the adapter is not found and no record
  is written, or a stamp is local time.
  permission: the main loop's; a role agent's hook refuses the pass-leg runner.
  cost: one pass-leg run, 209 s of wall at `bde79f210` (PINNED, 2026-11-12).

## 6. Gates

`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` · `python reads (a name never bound, an import outside its guard)` · `kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures`

The first three are the legs this unit repairs. The last six are owed by a guard the estimate trips:
the two recall legs by the memory root, the other four by the manifest. Five of those six are held
self-tests, every one but `recall floor`, and the brief's close does not run the held tier.

The close is the brief's: the full bar once more, with every leg guard ignored, without the
self-tests and without the unattended kit gate leg. The main loop runs it. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 9. Reuse audit

The seams are the ones each leg names. For S1, the script-directory `case` this file already
carries for `_rp_here` at `tools/run-gates/pass-legs.sh@602f8952:151`, and the `printf -v` time form
`tools/run-gates/run-gates.sh` already uses for its epoch reads. For S2 and S5, the reason shape of
the rows beside them. For S3, the leg's own `guard` list. `python tools/codebase-map/reuse_lookup.py
"convert a date command substitution and a dirname substitution to the no-fork builtin form in a
shell script"` ranked name-stem neighbours only and named no helper, so for a shared no-fork
date helper no existing seam fits, and one site pair does not earn one. `gotchas.py --for-paths` over
the estimate selected `fixture-passes-by-finding-nothing`, which is S4's finding from the other
side: a fixture that fails for a reason nobody staged measures the wrong run.

Recall terms used: `fork idiom date-fmt path-subst printf -v registry row guard closure import
outside guard fork ceiling manifest-check budget warn manifest-line`
