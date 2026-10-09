# TOOL-aSparedSpawn-14 — a refusal retirement review, and a growth budget beside the floors

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 3

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
review, its proof, and the budget. It retires nothing itself: every batch is the owner's.

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
- **S6** — The first candidate batch, listed in §4 for the owner and decided in F2. NOT OBSERVED: a
  proposal this unit does not act on.

## 3. Non-goals (OUT)

- Retiring or consolidating any site. Every batch, the first included, is the owner's ruling and
  lands in its own commit after it.
- Building the family helpers (`require_run_state`, a per-verb required-flag table, a field-shape
  helper at the write boundary). S5 freezes the families' counts; the helpers are a consolidation
  batch's work. Until a family's helper exists, raising its ceiling with a dated reason is the only
  way to add a site to it, and that is stated rather than hidden.
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

### Files touched (estimate)

- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `.memory-tree.conf`
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
- migration: one new conf key, blank in the example conf; the memory-tree and unattended kits each owe a version bump.
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

## 7. Gates

`kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `straggler-guard arms` · `transition-audit arms` · `harness arms (fail branches armed or pinned)` · `check-arms selftest` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

New arm: tools/memory-tree/check-arms.py · covers AC1 AC2 AC3 AC4 AC5 AC7 · a survivor signature absent, a ceiling exceeded, a malformed token, a family over its ceiling, a dead family pattern · none

## 8. Open questions

- **F1 — The review's cadence.**
  - (a) On every minor version bump of the unattended kit, or monthly, whichever comes first, and
    mandatory whenever a ceiling reds.
  - (b) Only when a ceiling reds.
  - (c) Monthly only.
  - Recommendation: (a). A ceiling red alone waits until the budget is spent, which is late.
- **F2 — Approval of the first batch.** The table in §4 is the candidate list; the owner approves,
  narrows or rejects each row. Before ruling, the research asks for two things: per-arm timings of
  the candidate arms by slice, and the local runlog stores of nodes `b`, `c` and `d`, since node `a`
  has none and R1 rests on prose records alone.
  - (a) Approve rows 1, 2, 4, 5 and 15 now, the classes whose condition survives by construction.
  - (b) Approve after the timings and the other nodes' stores are read.
  - (c) Reject the batch; build the budget only.
  - Recommendation: (b). R1 is the criterion the research is least sure of, and the two readings
    it asks for are cheap next to a retirement that has to be walked back.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "count refusal sites against a floor per gate"` ranks generic
`counts`/`refusal` symbols and no budget seam. The seam this unit extends is
`tools/memory-tree/check-arms.py`: its `classify` census, `parse_floors` and the floor compare in
`cmd_check`, plus the `<stem>.local.test.sh` convention for a per-gate sidecar. No second counter
is built beside them.

Recall terms used: ARMS_FLOORS floor raise lower check-arms refusal sites armed branches
unarmed-branches census emit-floors tombstone retire
