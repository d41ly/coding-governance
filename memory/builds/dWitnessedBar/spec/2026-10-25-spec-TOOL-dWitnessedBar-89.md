# TOOL-dWitnessedBar-89 — the round-1 audit of units 85 to 88, 13 minors batched: a visited failure on its own code, a whole-token match, one owner line and pinned records

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 46 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-build-TOOL-dWitnessedBar-89-round11-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-89-round11-fix-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-89-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-89-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-89-round11-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-89-round11-fix-brief.md) | research | — |
| [2026-10-25-review-TOOL-dWitnessedBar-89-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-89-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 85 to 88
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md`)
exited CONVERGED with 13 confirmed findings, none at BLOCKER or HIGH. BUILD-METHOD M4 batches every
MEDIUM and LOW into one unit, or two only where they split into disjoint write sets by M6's clauses.
§4 "Why one unit" says why these stay one. Each finding is named by report id and is its own scope
item, including where the report merged two ids into one item. The minors land on units 84 to 88, so
this unit repairs no single unit and builds above every unit in the build (order 46).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 2 | unit 87 S1, AC1; unit 84 S14 | S1 |
| M1 | MEDIUM | 6 | unit 87 §4 Evidence, §3 Edges, AC1 | S2 |
| M2 | MEDIUM | 1 | unit 88 S19, AC19; unit 81 S3, S4 | S3 |
| M3 | MEDIUM | 7 | unit 88 S3, AC3; unit 84 S14 | S4 |
| M4 | MEDIUM | 13 | unit 85 S1, §5, AC1, §7 | S5 |
| M5 | MEDIUM | 14 | unit 88 S10, §5, AC10 | S6 |
| M6 | MEDIUM | 16 | unit 86 S1, AC1; unit 85 S1; unit 84 S14 | S7 |
| L1 | LOW | 3 | unit 88 S13, AC13 | S8 |
| L1 | LOW | 8 | unit 88 S13, AC13, §4, §5 | S9 |
| L2 | LOW | 4 | unit 85 S2; unit 88 S7, AC18 | S10 |
| L3 | LOW | 5 | unit 87 AC2 | S11 |
| L4 | LOW | 10 | unit 88 S6, §4 | S12 |
| L5 | LOW | 12 | unit 88 §4 Files touched, S11, S19 | S13 |

That is 7 MEDIUM and 6 LOW findings by raw id. Ids 2 and 6 share item M1, and ids 3 and 8 share item
L1.

## 2. Scope (IN)

- **S1** — id 2. Unit 87's break, pinned against the visited count. The staged `check_canary_keys` of
  87 S1 and AC1 still visits and counts the `rec_fp` pair under `TOOL-dWitnessedBar-84` S14, and skips
  only the printing of `rec_fp`. The canary therefore visits 2 of 2 and prints no visited line, and
  87 AC1 holds as written. At the close the main loop also stages the other placement, a copy whose
  skip sits before the count. Under S4 that copy prints a line holding `the canary visited 1 of 2` on
  stderr, and no line holding `rec_sha byte check` or `lost its CR`. Unit 76's ledger beside AC2
  records that line, naming `TOOL-dWitnessedBar-84` S14 and this unit. Observed by AC1.
- **S2** — id 6. Unit 87's grounding answered. Unit 87's ledger beside AC1 names
  `TOOL-dWitnessedBar-84` S14 as the sibling check inside `check_canary_keys`. It records the break
  form S1 pins and the visited count of 2 of 2 under it. It states that 87 §4 Evidence's fifth
  bullet, that `rec_sha`'s variants are untouched by the break, holds for that form only, and it names
  this unit. Observed by AC2.
- **S3** — id 1. Break records carry `break:`. Each break record that `TOOL-dWitnessedBar-81` S3 and
  S4 write in the ledgers of units 74 and 76 carries the token `break:` on the line grep prints,
  beside `TOOL-dWitnessedBar-81`. So does each owed record `TOOL-dWitnessedBar-88` S19 writes in its
  place. 88 S19's platform rule binds exactly the lines holding both tokens. A line naming 81 without
  `break:`, such as 81 S3's statement line or a line of unit 87 or 88 citing 81, is outside the rule.
  Unit 88's ledger beside AC19 records that its selection is read through this unit's AC3, and names
  this unit. Observed by AC3.
- **S4** — id 7. `check_canary_keys` on every failure path. It returns 3 when its visited count
  fails, that is when `<n>` differs from `<m>` or `<m>` is below 2, whatever else happened. Otherwise
  it returns 2 when any call of `check_cr_reached` returned 2, 1 when it printed at least one variable,
  and 0 when it printed nothing. On a 3 it prints 84 S14's
  `gov-canary: the canary visited <n> of <m> CANARY_KEYS pairs` to stderr, so the line never enters
  the output a caller captures. On a 3 the liveness loop sets `fail=1` and prints neither 84 S13's
  `could not be sourced or read (rc 2)` reason nor a per-variable line. On a 3 the canary prints no
  `TOOL-dWitnessedBar-75` S1 line with `<what>` set to `unread`. The runner captures a leg's stderr
  with its stdout, so 84 AC14's lines still print. Observed by AC4.
- **S5** — id 13. The tail variant's gating, seen red. At the close the main loop runs the arm in a
  scratch clone of the built tree whose suite copy's `check_cr_reached` keeps the count at forty-one
  and holds no last-byte test, `TOOL-dWitnessedBar-81` S1's second break. The tail variant is then
  not seen red on any key, so the arm prints `below the pinned floor` with an executed count at least
  the number of words in `${CANARY_KEYS[*]}` below the floor. Unit 85's ledger beside AC1 records this
  clone's floor line and difference beside those of 85 AC1's `-ge 0` clone. It states that 85 §5's
  risk line rests on both clones, and names this unit. Observed by AC5.
- **S6** — id 14. The `<key>)` match closes on a whole token. The liveness loop's match is
  `\(<key>)[[:space:]]*<var>=\)"\{0,1\}\(\$_rg_v\|\${_rg_v}\)"\{0,1\}\([[:space:];]\|$\)`, and the
  replacement is `\1<replacement>\3`, written unquoted. It edits the five spellings 88 S10 lists in
  one line each and changes no line of an arm carrying a parameter modifier, so an arm spelled
  `${_rg_v%$'\r'}` or `${_rg_v:-}` reaches `variant changed 0 lines`. Unit 88's ledger beside AC10
  names this unit and records that 88 §5's sentence, that bash refuses every extra spelling the match
  admits, is struck. Observed by AC6.
- **S7** — id 16. The visited increments, once per loop. The body of `check_canary_keys` adds nothing
  to `a`. The canary's visited check adds one to `a` at its single top-level call site, and the
  liveness loop's visited check adds one after the loop. A missing variant therefore moves `a` by the
  `TOOL-dWitnessedBar-85` S1 increments alone, which is 86 AC1's equality. Unit 86's ledger beside AC1
  records the difference each of its two clones printed, and names this unit. Observed by AC7.
- **S8** — id 3. Unit 88 AC13 recorded as a pin. Unit 88's ledger beside AC13 records S13 as
  `NOT OBSERVED` by the build. The reason it gives is that AC13 reads `86a690d64`, the commit that
  added spec 88, which no build act can change. It names this unit. Observed by AC8.
- **S9** — id 8. The New-arm list's length, re-derived at the close. At the close the main loop runs
  §4's owner derivation, whose first printed line is the list's length. Unit 88's ledger beside AC13
  records that length beside the 26 pinned at `86a690d64`, names the units the list gained since, and
  names this unit. Observed by AC9.
- **S10** — id 4. One owner line, the floor's history gone. This unit moves a gov-canary arm (§7), so
  `TOOL-dWitnessedBar-88` S6's derivation names it the floor's owner at the close. Its builder
  restates `FLOOR_ASSERTIONS` absolutely, at the count the suite executes on a passing run at this
  pass, by `TOOL-dWitnessedBar-82` S1's counting rule. The one comment line directly above
  `FLOOR_ASSERTIONS=<n>` reads
  `# Raised to <n> by TOOL-dWitnessedBar-89, counting every arm through order 46; stated ABSOLUTELY.`
  That line is the only floor comment the built suite keeps: the two `TOOL-aShardedFloor-2` comment
  lines above the constant and the `TOOL-dDerivedDocket-23` line below it are not carried into the
  built file, and the assignment carries nothing after the number. Unit 88's ledger beside
  AC7 records that this unit restates the floor after it, and names this unit. Observed by AC10.
- **S11** — id 5. Each reason credited to its own unit. Of the two `rec_fp` lines
  `TOOL-dWitnessedBar-87` S2 records in unit 76's ledger beside AC2, the length line names
  `TOOL-dWitnessedBar-79` and the tail line names `TOOL-dWitnessedBar-80`. Each also names `rec_fp`
  and `TOOL-dWitnessedBar-87`. Unit 87's ledger beside AC2 records that its AC2 is graded through
  this unit's AC11, and names this unit. Observed by AC11.
- **S12** — id 10. The owner derivation through the shipped region reader. §4's owner derivation cuts
  `region` from `tools/unattended/unattended.sh` and reads the `gen:build-units` slice through it, so
  a malformed pair prints `MALFORMED REGION` and exits 3 where `--plan` refuses. 88 S6, AC6 and AC18
  and this unit's S9 run this derivation. Unit 88's ledger beside AC6 names this unit. Observed by
  AC12.
- **S13** — id 12. The renders move with an ask row. Each ask row this build files in
  `memory/builds/dWitnessedBar/BACKLOG.md` from here on, 88 S11's at its pass and 88 S19's at a close
  off Windows, is followed by `python tools/memory-tree/gen_build_index.py --write`. The commit that
  carries the row carries the renders it moves: `memory/builds/dWitnessedBar/README.md`,
  `memory/backlog/TOOL.md` and `memory/LIVE.md`, declared in that pass's `--writes`. This unit's pass
  runs the same `--write` and commits what it moves. Unit 88's ledger beside AC11 names the three
  renders and this unit. Observed by AC13.

## 3. Non-goals (OUT)

- Rewording the spec text of units 84 to 88. Each item is closed by what this pass builds or
  observes. A claim or criterion it answers is answered in that unit's acceptance ledger by name, as
  `TOOL-dWitnessedBar-88` §3 does for units 76 to 84.
- The left-shift gates the report names: the checklist items, and any spec-tokens or hygiene check
  for an unpinned break, an id-keyed selector, a restated return contract, an exact counter delta, a
  modifier spelling, a pinned-commit criterion, a `-B1`-only read, a per-line attribution, a
  re-sliced region or an unlisted render. No clause of this build names them. S4's code, S6's match,
  S7's placement and S10's owner line are the regressions this batch builds.
- New assertions in the suite. S4 to S7 change which line a failure prints and where an increment
  sits, and S10 restates the floor over the count the suite already executes.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-81` — S3 and S4's break records, which S3 marks with `break:` so 88 S19's platform rule selects them alone (id 1)
- **consumes-from** `TOOL-dWitnessedBar-82` — S1's counting rule, by which S10 restates the floor last (id 4)
- **consumes-from** `TOOL-dWitnessedBar-84` — S13's return codes and S14's visited counts with their increments, which S1, S2, S4 and S7 pin, route and place (ids 2, 6, 7 and 16)
- **consumes-from** `TOOL-dWitnessedBar-85` — S1's per-variant increments, AC1's `-ge 0` clone and S2's owner line, which S5 widens, S7 isolates and S10 restates (ids 4, 13 and 16)
- **consumes-from** `TOOL-dWitnessedBar-86` — AC1's exact difference, which S7 makes hold by placing the visited increments outside `check_canary_keys` (id 16)
- **consumes-from** `TOOL-dWitnessedBar-87` — S1's staged break, §4 Evidence and S2's ledger lines, which S1, S2 and S11 pin, correct and grade line by line (ids 2, 5 and 6)
- **consumes-from** `TOOL-dWitnessedBar-88` — S3's contract, S6's derivation, S7's restatement, S10's match, S11's and S19's ask rows, AC13 and AC19, which S3, S4, S6, S8 to S10, S12 and S13 complete (ids 1, 3, 4, 7, 8, 10, 12 and 14)
- **hands-off** `TOOL-dWitnessedBar-90` — S4's return code 3, S6's match, S7's placement, S10's owner line, S11's attribution, S12's derivation, S13's render rule, §4 Rollout and §5, and AC1, AC3, AC4, AC6, AC7 and AC10 to AC13, which unit 90 completes (ids 1, 2, 4, 6, 7, 9, 12, 13, 14, 16, 17, 18, 19, 20 and 21 of the round-1 spec audit of unit 89)
- **hands-off** `TOOL-dWitnessedBar-92` — its ledger's `- AC<n>` answers, under which unit 92 places the notes of units 90 and 92 and which it counts exactly, and its §5 schedule, which unit 92 restates in unit 90's note (ids 3, 4, 5 and 11 of the round-1 spec audit of unit 90)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The suite half, S4, S6, S7
and S10, writes `tools/run-gates/run-gates.gov.test.sh`. The ledger half, S1 to S3, S5, S8, S9 and
S11, records arm runs over that built suite, so it reads the suite half's output as an acceptance
input, M6 clause 2: S1's contrast copy prints its visited line on stderr only under S4. S9 and S12 run
one derivation, and S13 regenerates indexes beside the ledger records, M6 clause 3. No split leaves
two disjoint write sets, and dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js:76`), so a split would buy no concurrency.

### Evidence

- `tools/run-gates/run-gates.gov.test.sh:91-95`, read on 2026-10-25: `a=0`, the two
  `TOOL-aShardedFloor-2` comment lines at `:92-93`, `FLOOR_ASSERTIONS=16` at `:94`, and
  `# Raised 15 -> 16 by TOOL-dDerivedDocket-23` at `:95`. `grep -n Raised` prints `:92` and `:95`, and
  no other line. The suite increments with `a=$((a+1))` (`:115` and others), and `:459` fails only
  when `a` is below the floor.
- `check_canary_keys`, `check_cr_reached`, `CANARY_KEYS` and the liveness loop are not in the tree
  yet: units 74, 76, 79, 80 and 84 specify them, and none is built. Every claim here about them is a
  claim about those specs. 84 S14 (spec-84 lines 123-130) adds the visited counts and does not say
  where their increments run. 88 S3 (spec-88 lines 72-76) states return codes 0, 1 and 2 only.
- `tools/run-gates/run-gates.sh:3889` runs each leg with `>"$WORK/$i$sfx.raw" 2>&1`, so a line a suite
  prints on stderr is part of the leg's output.
- `region()` (`tools/unattended/unattended.sh:1310-1318`) requires exactly one open and one close,
  close after open, and exits 3 otherwise. `verb_plan` (`:5922`) refuses a malformed units pair with
  `not exactly one well-formed pair` (`:5950`). Probed on 2026-10-25: `region` cut with
  `sed -n '/^region() {/,/^}/p'` and evaluated exits 3 on a scratch copy of the README with a second
  pair appended, where the bare `.split()` of 88 §4 returns the first slice. Over the live README the
  derivation below printed 26 and `spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md`, the same as 88 §4.
  Once the index is re-rendered with this unit, it names this spec. PINNED on 2026-10-25; S9
  re-derives it at the close.
- Probed on this node on 2026-10-25 (GNU sed 4.9): S6's match with the replacement `${_rg_v:1}`
  rewrote `sha) rec_sha=$_rg_v ;;`, `"$_rg_v"`, `${_rg_v}`, `"${_rg_v}"`, `sha)   rec_sha=$_rg_v`, a
  line ending at the token and `$_rg_v;;` in one line each, keeping the alignment and the boundary. It
  left `${_rg_v%$'\r'}`, `${_rg_v:-}`, `$_rg_vx` and the `fingerprint)` arm unchanged.
- `memory/backlog/TOOL.md` and `memory/LIVE.md` each open with
  `generated by tools/memory-tree/gen_build_index.py --write`, and the README's `ids:` line lists every
  id of the build. `.unattended.conf:418` names neither render in `GENERATED_INDEXES`.
- `build_commit` (`tools/unattended/lib-unattended.sh:1186`) answers which commit is a unit's pass, as
  `TOOL-dWitnessedBar-62` S16 rules.
- `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records that a ledger grep
  reads one physical line, so every token a criterion greps sits on the line grep prints.

### The owner derivation

Run as a script with `bash` from the repository root. It prints the New-arm list's length, then the
owner's spec path, or `MALFORMED REGION` and exit 3.

```bash
eval "$(sed -n '/^region() {/,/^}/p' tools/unattended/unattended.sh)"
b=memory/builds/dWitnessedBar/
r=$(region "${b}README.md" '<!-- gen:build-units -->' '<!-- /gen:build-units -->') || { echo 'MALFORMED REGION'; exit 3; }
printf '%s\n' "$r" | python -c "import sys, importlib.util as u, re; s = u.spec_from_file_location('cst', 'tools/check-spec-tokens.py'); m = u.module_from_spec(s); s.loader.exec_module(m); b = 'memory/builds/dWitnessedBar/'; o = [p for p in re.findall(r'\]\((spec/[^)]+)\)', sys.stdin.read()) if any(l.startswith('New arm: tools/run-gates/run-gates.gov.test.sh') for l in (m.extract_gates(open(b + p, encoding='utf-8').read()) or '').splitlines())]; print(len(o)); print(o[-1] if o else 'NO OWNER')"
```

### Inventory

Minted: `check_canary_keys`'s return code 3; the ledger token `break:`; S6's match; the owner line
naming this unit, with the restated `FLOOR_ASSERTIONS`. No function, plant, flag or file. Naming
cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 46, after every other unit of the build, the last of them
`TOOL-dWitnessedBar-88` at order 45. S1 to S3, S5, S8, S9, S11 and S13's ledger lines are written at
the close.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/builds/dWitnessedBar/README.md`
- `memory/backlog/TOOL.md`
- `memory/LIVE.md`
- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Two batches, suite half and ledger half.** §4 "Why one unit".
- **Fold the floor's history into the owner line, the report's other option for id 4.** It keeps two
  stories about one value on one line. Git history already owns the earlier values.
- **Assert one marker pair inside the Python one-liner, the report's other option for id 10.** That
  is a second copy of `region`'s contract, the class the finding names.
- **Derive 86 AC1's expected difference at observation time, the report's other option for id 16.**
  It relaxes an exact equality to a lower bound, so a per-call increment would stay invisible.

## 5. Production-readiness checklist

- security — no new write path. The scratch clones sit under `%TEMP%`.
- perf / scale — none: S4 adds a return branch, S7 moves two increments, and the close's clones run
  once.
- error / empty / loading states — S4 gives a visited failure its own code and line, apart from a read
  failure; S12 names a malformed region instead of reading its first slice.
- observability — S4's visited line reaches the leg output on stderr; S10's owner line names its unit.
- risks — a builder who prints S4's line on stdout puts it into the captured output, and S1's contrast
  copy then prints a `rec_sha byte check` line; AC1 catches it. S6's match still admits an unbalanced
  quote, `"$_rg_v ;;`, which bash refuses before the loop runs.
- testing — AC3, AC4, AC6, AC7, AC10 and AC12 by probe or fixture at the pass; AC1, AC5 and AC9 by
  scratch clone at the close; the rest by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone of the built tree whose suite copy's `check_canary_keys` counts `rec_fp`
  and skips only its printing, the arm prints no line holding `visited`, `lost its CR` or
  `rec_sha byte check`. In one whose skip sits before the count, the arm's stderr holds
  `the canary visited 1 of 2` and its output holds no line holding `rec_sha byte check`. When
  `grep -n 'visited 1 of 2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*`
  runs at the close, it prints a line naming `TOOL-dWitnessedBar-84` and `TOOL-dWitnessedBar-89`.
  Red when: the same named break gets opposite verdicts depending on where the skip sits.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-87*acceptance-ledger*`
  runs at the close, it prints a line holding `TOOL-dWitnessedBar-84`, `2 of 2` and
  `TOOL-dWitnessedBar-89`.
  Red when: unit 87's ledger certifies its break with the visited count it shares a function with
  unnamed.
  permission: the ledger is written at the close.
- **AC3** — In a scratch ledger holding one line naming `TOOL-dWitnessedBar-81` with no `break:` and
  two lines holding both, `grep 'TOOL-dWitnessedBar-81' <file> | grep -c 'break:'` prints 2. At the
  close, the same pipeline over each of the ledgers
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger*` prints at least 2,
  and every line it selects holds a `uname -s` value beginning `MINGW` or `MSYS`, or `owed` with the id
  of an ask row in `memory/builds/dWitnessedBar/BACKLOG.md`.
  Red when: a statement line naming 81 trips the platform rule, or a break record escapes it.
  fixture: a scratch file under the run's scratch directory.
  permission: the ledgers are written at the close.
- **AC4** — When a probe cuts `check_cr_reached`, `check_canary_keys` and the `CANARY_KEYS` definition
  out of the built suite with `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh`
  and its like, sources them, empties `CANARY_KEYS`, and calls
  `out=$(check_canary_keys <file> <record> 2>err)`, it returns 3, `out` is empty, and `err` holds
  `the canary visited 0 of 0`. In a scratch clone whose two loops each stop after the first pair, the
  arm prints a line holding `the canary visited 1 of 2` and no line holding
  `could not be sourced or read (rc 2)`.
  Red when: a skipped or emptied key list returns the pass code, or reads as a read failure.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
  permission: the arm's run is the main loop's, at the close.
- **AC5** — In a scratch clone of the built tree whose suite copy's `check_cr_reached` keeps the count
  at forty-one and holds no last-byte test, the arm prints `below the pinned floor` with an executed
  count at least the number of words in `${CANARY_KEYS[*]}` below the floor, and exits non-zero. When
  `grep -n 'below the pinned floor' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-85*acceptance-ledger*`
  runs at the close, it prints a line holding `-ge 0` and one holding `last-byte`, each with
  `TOOL-dWitnessedBar-89`.
  Red when: the tail variant adds to `a` whether or not it was seen red.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  figure: the counts are DERIVED at observation time; the word count reads 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC6** — When a probe applies S6's match for `sha` with `${_rg_v:1}` to scratch arms reading
  `rec_sha=$_rg_v`, `rec_sha="$_rg_v"`, `rec_sha=${_rg_v}`, `rec_sha="${_rg_v}"` and
  `sha)   rec_sha=$_rg_v`, each `diff` counts one changed line; over arms reading
  `rec_sha=${_rg_v%$'\r'}` and `rec_sha=${_rg_v:-}` it counts none. In a scratch clone whose
  `.githooks/pre-push` spells the `sha)` arm `rec_sha=${_rg_v%$'\r'}`, the arm prints a line holding
  `variant changed 0 lines`.
  Red when: the match takes the prefix of an arm carrying a modifier and certifies the variant.
  fixture: scratch arms and a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC7** — When `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh | grep -c 'a=\$((a'`
  runs on the built tree it prints 0. When
  `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-86*acceptance-ledger*` runs at
  the close, it prints a line for each of the two clones holding the difference and
  `TOOL-dWitnessedBar-89`.
  Red when: a per-call increment inside `check_canary_keys` makes a missing variant move `a` twice.
  permission: the ledger is written at the close.
- **AC8** — When `grep -n 'AC13' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88*acceptance-ledger*`
  runs at the close, it prints a line holding `NOT OBSERVED`, `86a690d64` and `TOOL-dWitnessedBar-89`.
  Red when: the ledger counts a criterion no build act could fail as an observation.
  permission: the ledger is written at the close.
- **AC9** — When §4's owner derivation runs at the close, the first line it prints equals the length
  that `grep -n 'AC13' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88*acceptance-ledger*`
  prints beside `26` on a line naming `TOOL-dWitnessedBar-89`.
  Red when: the recorded length is a pin no run at the close re-derived.
  figure: the length is DERIVED at the close; 26 is PINNED at `86a690d64`.
  permission: the ledger is written at the close.
- **AC10** — On the built tree, `grep -c 'Raised' tools/run-gates/run-gates.gov.test.sh` prints 1, and
  the line number `grep -n 'Raised'` prints is one less than the one `grep -n '^FLOOR_ASSERTIONS='`
  prints. `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` names
  `TOOL-dWitnessedBar-89` and no other unit id, and
  `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$' tools/run-gates/run-gates.gov.test.sh` prints 1. At the close
  the arm prints `PASS (<n> assertions)` with `<n>` equal to that value, and
  `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88*acceptance-ledger*` prints a
  line naming `TOOL-dWitnessedBar-89`.
  Red when: a stale history comment survives beside the restated value, where `grep -B1` cannot see it.
  figure: both numbers are DERIVED at observation time; `grep -c 'Raised'` prints 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC11** — When
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*` runs at
  the close, the line quoting `one byte short` holds `TOOL-dWitnessedBar-79`, and the line quoting
  `last byte is not CR` holds `TOOL-dWitnessedBar-80`; each holds `rec_fp` and `TOOL-dWitnessedBar-87`.
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-87*acceptance-ledger*` prints a
  line naming `TOOL-dWitnessedBar-89`.
  Red when: a ledger crediting the length reason to unit 80 passes.
  permission: the ledgers are written at the close.
- **AC12** — When §4's owner derivation runs on the built tree, it prints a non-zero length and a spec
  path. In a scratch clone whose `memory/builds/dWitnessedBar/README.md` carries a second
  `gen:build-units` pair, it prints `MALFORMED REGION` and exits 3, and
  `bash tools/unattended/unattended.sh --plan dWitnessedBar` there prints a line holding
  `not exactly one well-formed pair`. When
  `grep -n 'AC6' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88*acceptance-ledger*` runs at
  the close, it prints a line naming `TOOL-dWitnessedBar-89`.
  Red when: the derivation reads a slice the dispatcher refuses.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC13** — When
  `grep -oE '^- TOOL-dWitnessedBar-[0-9]+' memory/builds/dWitnessedBar/BACKLOG.md | cut -c3- | awk -F- '$3 > 88'`
  runs at the close, each id it prints appears in `memory/backlog/TOOL.md` and on the `ids:` line of
  `memory/builds/dWitnessedBar/README.md`. After this unit's pass commit,
  `python tools/memory-tree/gen_build_index.py --write` leaves
  `git status --porcelain -- memory/backlog/TOOL.md memory/LIVE.md memory/builds/dWitnessedBar/README.md`
  empty. `grep -n 'AC11' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88*acceptance-ledger*`
  prints a line naming `memory/backlog/TOOL.md` and `TOOL-dWitnessedBar-89`.
  Red when: an ask row lands with the renders that list it stale.
  permission: the ledger is written at the close.

## 7. Gates

`run-gates gov canary` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close, which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf:40`). `testsuite counts (every bar self-test
prints one)` reads the assignment line S10 writes. `recall floor` and `recall floor arms` are owed for
the paths under `memory/`.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC4 AC5 AC6 · the visited failure's own return code and the whole-token `<key>)` match, staged red by a scratch suite whose `check_canary_keys` returns 2 on a visited failure (reaches `could not be sourced or read (rc 2)` where the visited line belongs) and by a match whose braces are independently optional (a modifier arm changes one line and `variant changed 0 lines` never prints) · FLOOR_ASSERTIONS restated absolutely by S10, its owner this unit

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 84 to 88 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Where does unit 87's skip sit against 84 S14's count (ids 2 and 6)?** Options: (a) the skip
  suppresses only the printing of `rec_fp`, after the count, with the other placement staged as a
  contrast; (b) the skip sits before the count, the visited line is required, and 87 AC1's `rec_sha`
  exclusion is relaxed to match. (b) relaxes a criterion 87 states and records a third failure line
  87 S2 does not name. (a) keeps 87 AC1 as written and still observes the other placement. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none
- **F3 — Which return code does the visited failure take (id 7)?** Options: (a) 3, on stderr; (b) 2,
  the finder's fix. (b) reaches 84 S13's read-failure reason, which fails AC4's Red-when; veto 1
  discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor.
  widens: none · relaxes: none
- **F4 — Does this unit declare a gov-canary arm, and so own the floor (id 4)?** Options: (a) yes: it
  declares a `New arm:` line, restates the floor and writes the one owner line; (b) no: unit 88 stays
  the owner and the history lines are only deleted. Under (b) S4's and S6's changed failure routes
  land with no RED-first observation at the close. (a) observes them and closes id 4 at the owner
  line. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 85 to 88: 7
  MEDIUM and 6 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-90, the minors batch of the round-1 spec audit of unit 89; nothing else
  moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-92, the minors batch of the round-1 spec audit of unit 90; nothing else
  moved.

## 10. Reuse audit

Each item extends the seam its finding names. S4 extends `check_canary_keys` and 84 S13's return
codes; S6 narrows 88 S10's match; S7 moves 84 S14's increments; S10 follows `TOOL-dWitnessedBar-82`
S1's rule. S12 reuses `region` (`tools/unattended/unattended.sh:1310`), the reader `verb_plan` uses,
by cutting it as the build's probes cut suite functions.
`python tools/codebase-map/reuse_lookup.py "read the slice between a marker pair and refuse a malformed pair"`
ranked `read`, `read_text`, `slice` and `pair`, none of them `region`, so no existing seam fits beyond
`region` and the seams named above. The ledger items use the acceptance ledger of `memory/HYGIENE.md`
"Acceptance ledger".

Recall terms used: `python tools/memory-recall/query.py "how does a canary function report that it visited fewer key pairs than declared" --terms "canary check_canary_keys visited count return code stderr liveness loop floor owner region marker"`
