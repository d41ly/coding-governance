# TOOL-aSparedSpawn-14 — a refusal retirement review, and a growth budget beside the floors

**Status:** OPEN · rev-2 · 2026-10-10 · node a · Tier-2 · base 22efab65 · streams tooling · order 3 · ratified 2026-10-10

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Give the refusal surface a way down and a ceiling on the way up. `ARMS_FLOORS` in `.memory-tree.conf`
is a shrink-guard and has only ever been raised, and the repo's two retirements of a mechanism each
ADDED a refusal. aMeteredSweep's round-two research counted the unattended driver going from 168 to
359 refusal sites and its leg from 154 to 264 between 2026-08-23 and 2026-10-09, found real-run
evidence of firing for about 8% of them, and estimated a first consolidation at 1.9 to 4.9 ks of the
driver suite and 4.3 to 8.4 ks serial of the leg suite
(`2026-10-09-build-TOOL-aMeteredSweep-1-research2-retirement.md` §0 and §5; PINNED, counted at
6bc6c949c on 2026-10-09, the savings proportional estimates and not timings). This unit builds the
review, its proof, and the budget, and retires the first batch the owner approved on 2026-10-10:
rows 1, 2, 4, 5 and 15 of §4's table, exactly those, with the per-row proof. Every later batch is
the owner's.

## 2. Scope (IN)

- **S1** — The review procedure, written into `tools/memory-tree/README.md` beside the `check-arms`
  section. A site is a candidate only when all four hold: R1, never observed firing in a real run
  (run records, backlogs, gotchas, the decision log and every node's local runlog store; a suite or
  an acceptance ledger does not count); R2, it cites no record whose Goal shows an observed
  occurrence; R3, its condition survives in another refusal or leg cited by file, in a family's
  shared table, or in one structural check; R4, it is not security-shaped (self-authorization, git
  object or config substitution, record forgery at a write boundary, any charter §9 surface). The
  owner decides each batch; an agent only proposes, with the evidence columns filled. NOT OBSERVED:
  a procedure in prose; S2 grades the record each retirement leaves.
- **S2** — The retirement commit and its proof. One commit per batch carries: a `memory/DECISIONS.md`
  row of the grammar in §4, superseding the originating record; the floor in `ARMS_FLOORS` lowered,
  with a comment line naming that row's id; the arm gone from the gate's suite; any pinning row gone
  from the unarmed-branches registry; and no tombstone refusal. Each row names its SURVIVOR, a file
  and a signature, and its REPLAY, the refusal line the retiring arm's fixture produced when run once
  against the post-batch tree. `check-arms.py` gains a pass, run inside `--check`, that reads every such row
  and reds when a survivor file no longer carries its signature or a row lacks either field.
  **Readers:** by name: `ARMS_FLOORS` is spelled by `check-arms.py`, `drift_signals.py` and
  `check-kit-placeholders.py`; the unarmed-branches registry by `check-arms.py` and `drift_signals.py`.
  by value: `check-arms.py` compares each floor to the armed count it measures, and `drift_signals.py`
  reports the floors' distance from that count; a lowered floor is read by both as the new minimum.
  Observed by AC1, AC2.
- **S3** — The growth budget. `REFUSAL_CEILINGS` in `.memory-tree.conf`, beside `ARMS_FLOORS`, one
  `<gate>:<count>:<date>:<id>` token per budgeted gate, where count is the census the floor's first
  number already counts. `--check` reds a gate above its ceiling and names the review as the way to
  raise it; reds a token missing its date or its id, or naming an id that no `memory/DECISIONS.md`
  row carries; and prints every ceiling with its date and id on every run. Observed by AC3, AC4.
- **S4** — Seeding. The two unattended gates, `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh`, get ceilings at the census `check-arms.py --report` measures
  on the build date, with this unit's id. A gate with no token is unbudgeted, and `--report` lists the
  unbudgeted gates so the omission is visible. Observed by AC6.
- **S5** — The per-verb family rule. A gate may carry a sidecar of variant families beside it, by
  the same stem convention as `<stem>.local.test.sh`: one row per family holding its name, ceiling,
  date, decision id and an extended regex over the refusal message. `--check` counts the gate's
  refusal sites whose message matches each family and reds a family above its ceiling with "a new
  per-verb site: extend the family's shared table instead". A family pattern matching no site reds,
  because a pattern that cannot match cannot refuse anything. The driver's sidecar is seeded with the
  three families the research counted: missing run-state file, missing required flag, and a field
  carrying a newline, carriage return, separator or the bypass flag. Observed by AC5, AC7.
- **S6** — The first candidate batch, listed in §4 for the owner and decided in F2. Rows 1, 2, 4, 5
  and 15 are approved (owner ruling F2 (a)) and built by S7 to S11; every other row waits for a later
  review. Observed by AC13.
- **S7** — Row 1, class V, under S1's procedure: the driver's missing-run-state refusals across
  checks 10, 37, 43, 47, 48, 49, 51, 52 and 88 route through one helper, `require_run_state`, which
  keeps one arm, and a structural route check in the leg reds a verb that reads its run-state file
  without it. The per-site refusals it replaces are removed with their arms. Observed by AC8.
  **Readers:** by name: the arms of `tools/unattended/unattended.test.sh` that pin these refusals
  spell their messages. by value: `tools/memory-tree/check-arms.py` counts the sites against the
  `ARMS_FLOORS` token for `tools/unattended/unattended.sh` in `.memory-tree.conf`, and
  `tools/drift-audit/drift_signals.py` reports that floor's distance; S11 lowers the token.
- **S8** — Row 2, class V: the driver's required-flag refusals across eleven checks route through a
  per-verb table, `VERB_REQUIRES`, that one reader enforces and that also renders the required flags
  in `usage` (`tools/unattended/unattended.sh:121`). Check 14's unknown-argument refusal, which fired
  in a real run, is outside the row and stays. The per-site refusals and their arms are removed.
  Observed by AC9.
  **Readers:** by name: the arms of `tools/unattended/unattended.test.sh` that pin these refusals
  spell their messages. by value: `tools/memory-tree/check-arms.py` counts the sites against the
  `ARMS_FLOORS` token for `tools/unattended/unattended.sh` in `.memory-tree.conf`, and
  `tools/drift-audit/drift_signals.py` reports that floor's distance; S11 lowers the token.
- **S9** — Row 4, class G: driver checks 110 and 111, which refuse a claim mode outside `CLAIM_MODES`
  and a read class outside `CLAIM_READS` at run time (`tools/unattended/unattended.sh:1972-1977`),
  give way to a static join in the leg between those two declarations and the claim function's case
  arms. Both fixture arms are dropped. Observed by AC10.
  **Readers:** by name: the arms of `tools/unattended/unattended.test.sh` that pin these refusals
  spell their messages. by value: `tools/memory-tree/check-arms.py` counts the sites against the
  `ARMS_FLOORS` token for `tools/unattended/unattended.sh` in `.memory-tree.conf`, and
  `tools/drift-audit/drift_signals.py` reports that floor's distance; S11 lowers the token.
- **S10** — Row 5, class F: the driver's environment and internal-failure exits at checks 27, 29, 48,
  56, 69 and 88 route through one exit-2 helper, `die_env`, which `check-arms.py` exempts by class as
  it does other environment refusals. The shim arms are dropped, and the pins for checks 27 and 29
  are removed from `tools/unattended/unarmed-branches.txt` (`:33-34`). Observed by AC11.
  **Readers:** by name: the arms of `tools/unattended/unattended.test.sh` that pin these refusals
  spell their messages, and `tools/unattended/unarmed-branches.txt` spells checks 27 and 29 in its
  pin rows. by value: `tools/memory-tree/check-arms.py` reads those pin rows and counts the sites
  against the `ARMS_FLOORS` token for `tools/unattended/unattended.sh` in `.memory-tree.conf`, and
  `tools/drift-audit/drift_signals.py` reports that floor's distance; S11 lowers the token.
- **S11** — Row 15, tombstones: the leg's check 23 site that refuses a retired key
  (`tools/unattended/check-unattended.sh:3994`) and its check 47 sites that refuse a retired premise
  (`:6063`, `:6065`) are retired with no tombstone in their place, per S2. The batch's single commit
  carries S2's proof for all five rows: one `memory/DECISIONS.md` row each with R1 to R4, survivor and
  replay filled, both unattended gates' floors and seeded ceilings lowered with comment lines naming
  those rows, and no refusal site outside the five rows removed. Observed by AC12 and AC13.
  **Readers:** by name: the arms of `tools/unattended/check-unattended.test.sh` that pin checks 23 and
  47 spell their messages. by value: `tools/memory-tree/check-arms.py` counts the sites against the
  `ARMS_FLOORS` token for `tools/unattended/check-unattended.sh`, and
  `tools/drift-audit/drift_signals.py` reports that floor's distance; this item lowers the token.

## 3. Non-goals (OUT)

- Retiring or consolidating any site outside rows 1, 2, 4, 5 and 15. Rows 3, 6 to 14 and 16 wait for
  a later review and the owner's ruling on it, each batch in its own commit.
- The field-shape helper at the write boundary (row 3). It is security-shaped under R4, so it is
  consolidated by a later batch and never retired. Until it exists, raising that family's ceiling with
  a dated reason is the only way to add a site to it, and that is stated rather than hidden.
- Generating the candidate list automatically from run records. The research's extraction scripts
  were one-off and node `a` has no local runlog store; the review reads every node's store by hand.
- Budgets for gates outside the unattended kit. One token adds one, when the owner wants it.

### Edges

none

## 4. Design

`tools/memory-tree/check-arms.py` already discovers every gate, counts its fail branches and refusal
sites (`classify`), parses `ARMS_FLOORS` (`parse_floors`) and reds a count below its floor. This unit
adds three readers to the same walk, so the harness-arms leg stays one process:

1. `parse_floors`'s sibling for `REFUSAL_CEILINGS`, compared against the same `got[0]` count.
2. A sidecar reader for variant families, matching each site's message text, which the walk already
   holds.
3. A retirement-row reader over `memory/DECISIONS.md`, joining each row's survivor to its file.

### Data model

The retirement row, one per batch line in `memory/DECISIONS.md`:

```
- TOOL-<slug>-<n> · RETIRES <gate> check <k> "<signature head>" (x<sites>) · R1 <query and stores read> · R2 <ids, none incident> · survivor <file> "<signature>" · replay "<refusal line>" · supersedes <id>
```

The ceiling token: `<gate>:<count>:<date>:<decision id>`. The family row:
`<family><TAB><ceiling><TAB><date><TAB><decision id><TAB><ERE>`.

### The first candidate batch (for F2)

From the research's §6 table, re-read on this tree by check number and class. Line numbers have
moved since the research's tree, so the review re-derives them with `check-arms.py --report`.

| Row | Gate · check | Class | Proposed action |
|---|---|---|---|
| 1 | driver · missing run-state, across checks 10, 37, 43, 47, 48, 49, 51, 52, 88 | V | one helper, one arm, one structural route check |
| 2 | driver · missing required flag, across 11 checks (check 14 fired and is not in it) | V | a per-verb required-flag table that also renders the synopsis |
| 3 | driver · newline, carriage return, separator or bypass flag in a field | V, R4 | consolidate at the write boundary; never retire |
| 4 | driver · checks 110 and 111, the driver's own claim tables | G | a static join of the declarations; drop both fixture arms |
| 5 | driver · checks 27, 29, 56, 69, 88, 48: environment or internal failure | F | one exit-2 helper exempt by class |
| 6-10 | driver and leg duplicate pairs: 85 with 42, 24 and 27 with 9, the load-time overlap with 38, the load-time mode with 45, 97 with 15 | D | keep one side, in the library where one exists |
| 11 | driver check 49's spec-token re-run, beside the `spec tokens` leg | D | owner call: early warning, or drop |
| 12 | leg · liveness branches across many checks | G | one `require_population` helper |
| 13 | leg · check 28, parser certification | G | one in-process parser self-test, one branch kept |
| 14 | leg · Skill and protocol doc-parity joins | H | render the tables from the driver's declarations, one byte compare |
| 15 | leg · checks 47 and 23 tombstones | tombstone | retire, per the no-tombstone rule |
| 16 | driver singletons with no survivor | H | case by case; R3 fails, so each needs its own ruling |

Never candidates (R4): the driver's environment git-config and object guards, the `may:` and
`spec-audit:` self-authorization refusals on both sides, and the authorization-mode closed set.

### The first batch (owner ruling F2 (a): rows 1, 2, 4, 5 and 15)

The batch is built after S1 to S5 land, in one commit. Its sites are re-derived with
`check-arms.py --report` on the batch's parent, never taken from the research's line numbers. For
each row the builder fills R1 to R4 from the sources S1 names, and records which stores were read:
node `a` holds no local runlog store, so R1 for this batch rests on the committed records and on any
other node's store the owner supplies before the commit.

The REPLAY field is the refusal line the retiring arm's fixture prints when run once against the
post-batch tree, from a slice of the suite rather than the whole suite. For rows 1 and 2 the line
comes from the helper's or the table's single arm; for row 4 from the leg's static join; for row 5
from the helper's exit-2 path; for row 15 from the survivor the decision row names.

S4's seeded ceilings land before the batch, at the census on the build date, and the batch lowers
them in its own commit, which is the end state the alternatives below argue for. S5's families are
seeded after the batch, so rows 1 and 2's families start at the single site each helper leaves.

### Inventory

The batch mints two shell functions and one table in `tools/unattended/unattended.sh`, spelled here
as the research spelled them: `require_run_state`, `die_env` and `VERB_REQUIRES`. The functions sit
in the `lexicon naming predicates` shell cell, so each name is confirmed through
`python3 tools/lexicon/lexicon.py --suggest` before it is written, and a refused verb is renamed
there rather than added to the table.

### Files touched (estimate)

- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `.memory-tree.conf`
- `memory/DECISIONS.md` — the five retirement rows
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh` — rows 1, 2, 4 and 5
- `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh` — the route
  check, the claim-table join, and row 15
- `tools/unattended/unarmed-branches.txt` — the check 27 and 29 pins
- `tools/unattended/kit.toml`, `tools/memory-tree/kit.toml` — each kit's version, once
- the driver's family sidecar, beside `tools/unattended/unattended.sh` (new)

### Alternatives rejected

- **An aggregate ceiling across gates.** The floors are per gate for the reason `check-arms.py`'s
  header gives: an aggregate lets one gate's growth hide behind another's shrink.
- **A tombstone refusal per retirement.** It is the pattern the research found ADDING sites on every
  past retirement; the survivor join proves the condition still refuses without a new branch.
- **Seeding ceilings at the census minus the consolidation.** The research's preference, but the
  consolidation is not approved yet; the first approved batch lowers the seeded ceiling in its own
  commit, which is the same end state with no guess in between.
- **A new leg for the budget.** A second process over the same walk; the harness-arms leg already
  reads every gate.

## 5. Production-readiness checklist

- security: R4 makes security-shaped sites ineligible whatever R1 to R3 say; forgery guards consolidate and are never retired.
- perf / scale: three readers inside the existing check-arms walk; one extra file read for `memory/DECISIONS.md`.
- error / empty / loading states: a malformed token, family row or retirement row reds naming the token; an empty `REFUSAL_CEILINGS` leaves every gate unbudgeted and `--report` says so.
- observability: every ceiling and family prints with its date and id on every `--check`; `--report` lists unbudgeted gates.
- risks: a family regex that over-matches reds an innocent site; the zero-match rule catches the under-match, and each pattern is run over the real tree with hits and near-misses printed before seeding.
- testing: new arms in `check-arms.py --selftest`, each staged red first; the seeded tree green under `--check`.
- migration: one new conf key, blank in the example conf; the memory-tree and unattended kits each owe a version bump; the batch lowers two floors and two ceilings in one commit, and reverting that commit restores all four.
- user docs: `tools/memory-tree/README.md` gains the review procedure, the row grammar, the ceiling and the family sidecar.

## 6. Acceptance criteria

- **AC1** — When `check-arms.py --selftest` plants a retirement row whose survivor file lacks the
  named signature, `--check` reds naming the row's id; with the signature present it passes.
  Red when: the absent signature passes.
- **AC2** — When a planted retirement row lacks its `survivor` field or its `replay` field, `--check`
  reds naming the missing field. Red when: either row passes.
- **AC3** — When a fixture gate's census is one above its `REFUSAL_CEILINGS` token, `--check` reds
  naming the gate and the review; at the ceiling it passes. Red when: the excess passes.
- **AC4** — When a ceiling token lacks its date, lacks its id, or names an id no `memory/DECISIONS.md`
  row carries, `--check` reds naming the token; a well-formed token is printed with its date and id.
  Red when: any of the three passes, or a valid ceiling is not printed.
- **AC5** — When a fixture gate gains one refusal site whose message matches a family pattern at its
  ceiling, `--check` reds with `extend the family's shared table`. Red when: the new site passes.
- **AC6** — When `python tools/memory-tree/check-arms.py --check` runs on the seeded tree, it is green
  and prints both unattended ceilings, and `--report` lists the unbudgeted gates. Red when: the
  seeded census disagrees with the ceiling, or a ceiling is not printed. figure: the two ceilings are
  PINNED at the census `--report` measures on the build date.
- **AC7** — When a family's pattern matches no refusal site in its gate, `--check` reds naming the
  family. Red when: the dead pattern passes. fixture: the selftest's planted gate, never this tree.
- **AC8** — Row 1: when `check-arms.py --report` runs after the batch, the driver's missing-run-state
  refusals count one site, inside `require_run_state`, and its arm still reds a verb run with no
  run-state file; a scratch verb reading the file without the helper reds the leg's route check.
  Red when: a second site remains, the arm passes, or the route check passes the scratch verb.
- **AC9** — Row 2: when a verb runs without a flag `VERB_REQUIRES` lists for it, the driver refuses
  naming the flag, and the required flags `usage` prints for each verb equal the table's row byte for
  byte. Red when: a per-site required-flag refusal remains, a listed flag goes unenforced, or the
  synopsis disagrees with the table.
- **AC10** — Row 4: when a scratch driver gains a claim mode in its case arms that `CLAIM_MODES` lacks,
  and separately a read class `CLAIM_READS` lacks, the leg's static join reds naming it, and
  `grep -c 'check 110\|check 111'` over the driver suite prints 0. Red when: the undeclared mode or
  class passes, or an arm for either check remains.
- **AC11** — Row 5: when `check-arms.py --check` runs after the batch, the six checks' environment
  exits route through `die_env`, exempt by class, and `tools/unattended/unarmed-branches.txt` carries
  no row for checks 27 or 29; a scratch call of the helper exits 2. Red when: a listed exit remains
  outside the helper, a pin row survives, or the helper exits anything but 2.
- **AC12** — Row 15: when `grep -n 'is retired\|retired premise'` runs over the leg after the batch, it
  finds none of the three tombstone sites, and no new refusal names the retired key or premise.
  Red when: a tombstone remains, or one is re-added in another form.
- **AC13** — The proof: when `check-arms.py --check` runs on the post-batch tree, its retirement pass
  reads one `memory/DECISIONS.md` row per approved row, 1, 2, 4, 5 and 15, each with R1 to R4, a
  survivor carrying its signature and a replay line; both unattended gates' `ARMS_FLOORS` and
  `REFUSAL_CEILINGS` tokens sit below the batch parent's, each lowered beside a comment naming a row
  id; and `check-arms.py --report` at parent and child differ only in the five rows' sites.
  Red when: a row or field is missing, a survivor lacks its signature, a floor or ceiling did not
  move, or a site outside the five rows left the census.
  fixture: R1 cites the stores actually read; node `a` has none, and other nodes' stores are read
  only if the owner supplies them before the commit.
  cost: one suite slice per retiring arm for its replay line, seconds to minutes each.

## 7. Gates

`backlog migration selftest` · `build-index selftest` · `check-arms selftest` ·
`check-wiring self-test` · `corpus-ids selftest` · `dead-path carriers self-test` ·
`foreign-prefix parity (every self-test at three prefixes)` · `gotchas selftest` ·
`install-prefix self-test` · `kit-placeholders self-test` · `kit/dogfood doc parity` ·
`lexicon naming predicates` · `memory-hygiene self-test` · `push-main self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` ·
`row-grammar selftest` · `row-keyed merge driver replay` · `run-gates canary` ·
`run-gates evidence` · `settings-merge selftest` · `spec-tokens self-test` ·
`straggler-guard arms` · `transition-audit arms` · `verdict-epoch self-test` ·
`harness arms (fail branches armed or pinned)` · `unattended kit gate` ·
`kit epoch (shipped bytes move, the version moves)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-arms.py · covers AC1 AC2 AC3 AC4 AC5 AC7 · a survivor signature absent, a ceiling exceeded, a malformed token, a family over its ceiling, a dead family pattern · none
New arm: tools/unattended/check-unattended.sh, the route check and the claim-table join · covers AC8 AC10 · a scratch verb reading its run state directly, and a scratch claim mode left undeclared · its floor in `ARMS_FLOORS` moves with the batch
New arm: tools/unattended/unattended.test.sh, one arm each for `require_run_state`, `VERB_REQUIRES` and `die_env` · covers AC8 AC9 AC11 · the helper bypassed, a listed flag unenforced, the helper exiting 1 · its `FLOOR_ASSERTIONS` falls by the arms the batch drops

## 8. Open questions

- **F1 — The review's cadence.**
  - (a) On every minor version bump of the unattended kit, or monthly, whichever comes first, and
    mandatory whenever a ceiling reds.
  - (b) Only when a ceiling reds.
  - (c) Monthly only.
  - Recommendation: (a). A ceiling red alone waits until the budget is spent, which is late.
  - RESOLVED (owner, 2026-10-10): (a) each minor bump of the unattended kit or monthly, and on any ceiling red.
- **F2 — Approval of the first batch.** The table in §4 is the candidate list; the owner approves,
  narrows or rejects each row. Before ruling, the research asks for two things: per-arm timings of
  the candidate arms by slice, and the local runlog stores of nodes `b`, `c` and `d`, since node `a`
  has none and R1 rests on prose records alone.
  - (a) Approve rows 1, 2, 4, 5 and 15 now, the classes whose condition survives by construction.
  - (b) Approve after the timings and the other nodes' stores are read.
  - (c) Reject the batch; build the budget only.
  - Recommendation: (b). R1 is the criterion the research is least sure of, and the two readings
    it asks for are cheap next to a retirement that has to be walked back.
  - RESOLVED (owner, 2026-10-10): (a) approve rows 1, 2, 4, 5 and 15 now.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §1 §2 §3 §4 §5 §6 §7 S6 S7 S8 S9 S10 S11 AC8 AC9 AC10 AC11 AC12 AC13 · folded the
  owner's F2 ruling (a): rows 1, 2, 4, 5 and 15 are retired in this unit's first batch under the
  review procedure, one scope item and one criterion per row plus the batch's proof; the non-goals now
  exclude only the other rows and row 3's helper.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "count refusal sites against a floor per gate"` ranks generic
`counts`/`refusal` symbols and no budget seam. The seam this unit extends is
`tools/memory-tree/check-arms.py`: its `classify` census, `parse_floors` and the floor compare in
`cmd_check`, plus the `<stem>.local.test.sh` convention for a per-gate sidecar. No second counter
is built beside them.

Recall terms used: ARMS_FLOORS floor raise lower check-arms refusal sites armed branches
unarmed-branches census emit-floors tombstone retire
