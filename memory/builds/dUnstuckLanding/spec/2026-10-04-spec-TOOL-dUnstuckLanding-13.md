# TOOL-dUnstuckLanding-13 — `--handoff`: a run whose work is sound, but which an owner must land or decide, ends HELD instead of ABORTED

**Status:** CLOSED · rev-4 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 1 · closes TOOL-dUnstuckLanding-3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-1-runlog-2e793a3b.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-1-runlog-2e793a3b.md) | journal | TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2 TOOL-dUnstuckLanding-12 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-25 TOOL-dUnstuckLanding-27 |
| [2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-13-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md) | diff-review | TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-25 |
| [2026-10-04-review-TOOL-dUnstuckLanding-27-implementation-diff-round2.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-27-implementation-diff-round2.md) | diff-review | TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-27 |

<!-- /gen:spec-records -->

## 1. Goal

A run that finished its work and cannot land it today has one honest-looking exit, `--abort`, and the
census shows what that costs: 36 of 37 aborted runs' work reached the default branch anyway, so the
terminal says the run was discarded while git says it landed. This unit gives that run a verb of its
own. `--handoff` ends it `HELD` under one of two new hold codes, `owner-landing` or `owner-decision`,
writes the recipe a person runs to land it and the landing facts a landed record needs, and refuses
`owner-landing` over a red the run itself caused. `--abort` keeps its meaning, now stated as DISCARD,
and points at `--handoff` on the four halt codes that the census found hand-off-shaped.

## 2. Scope (IN)

- **S1 — the verb.** `--handoff <slug> --code owner-landing|owner-decision --reason "<text>"` plus
  exactly one of `--reaped <id>` and `--keepalive-unreachable <node>`, implemented as `run_handoff`
  in `tools/unattended/unattended.sh`. It joins `VERBS_SLUG`, the header's invocation lines and the
  dispatch. It routes through `run_hold` with the release condition fixed at `owner`, so every
  refusal `--hold` already makes holds here unchanged: a terminal or already-HELD record, a dirty
  tree, an unpublished tip under `ANCHOR_SCOPE=published`, an unreaped keepalive, and a live process.
  Observed by AC1, AC2.
- **S2 — the two codes, and their single producer.** `owner-landing` and `owner-decision` join
  `HOLD_CODES_CORE`, and a new driver constant `HOLD_CODES_HANDOFF` names exactly those two. A
  `--hold` naming either is refused, numbered and before any write, naming `--handoff`: a HELD
  record under a hand-off code carries the recipe and the landing facts, and a hold written without
  them would be a hand-off nothing can land or settle. Observed by AC3.
- **S3 — the attribution guard on `owner-landing`.** A new predicate, `check_handoff_bar`, admits the
  hand-off when the bar the record's `gates-run` fact names reads `verdict GREEN` and is tied to this
  tree, and otherwise delegates to `check_inherited_override`, whose fail 83 refuses unless every red
  leg reads INHERITED. No `gates-run` fact at all is refused through the same fail 83 branch that
  already names that condition. `owner-decision` is not guarded: it is the exit for an OWN red that
  needs a decision. Observed by AC4, AC5.
- **S4 — the tie, widened by exactly the run's own record.** `gates-green` writes its `gates-run`
  fact and stages it, and `run_hold`'s clean-tree refusal then makes the run commit that record
  before it can hold, which moves HEAD off the bar's head. So the tie `check_handoff_bar` applies,
  and the one it passes to `check_inherited_override` as a new optional third argument
  `record-only`, admits a bar head that differs from HEAD only in the run-state file:
  `git diff --quiet <bar head> HEAD -- . ":(exclude)<run-state file>"`. Without the argument,
  `check_inherited_override` is byte-unchanged for `--close` and `--abort`. Observed by AC5.
- **S5 — `owner-decision` requires a parked decision.** The verb refuses, numbered and before any
  write, when the run-state file's parked region holds no row of kind `decision`. Observed by AC6.
- **S6 — the landing facts.** The hand-off writes `units-at-landing` from `unit_rows` over the build
  README, in the spelling `--close` uses under `in-place`, and `asks-at-landing` from
  `derive_ask_freeze` at HEAD wherever that freeze is non-empty. Both are computed before any write,
  and a freeze that cannot be derived refuses with nothing written. They are written inside
  `run_hold`'s single write block, after `hold-run` and before its history row, through a global the
  hand-off sets and `--hold` leaves empty. Observed by AC1, AC7.
- **S7 — the recipe.** A new parked kind, `handoff`, joins `PARK_KINDS` and `PARK_KINDS_OWED`, so the
  owner is shown it and `parked-decisions-surfaced` counts it. `render_handoff_recipe` renders the
  commands from `LANDER_MODE`, `LANDER` and the record's `run-branch` fact, joined with ` && ` on one
  line: under `in-place`, `<LANDER> --prepare --slug <slug>` then `<LANDER> --land --slug <slug>`,
  run from the run's worktree; under `primary`, the `--no-ff` merge of the run branch from the
  primary tree, then `<LANDER>`. The row is `handoff · item <code> · reason <recipe>`, and the verb
  prints the recipe after its HELD line. Observed by AC1, AC8.
- **S8 — `HANDOFF_CUTOFF`.** A new conf key, the date from which `ABORTED` means DISCARD. It is
  initialised and read in the driver, initialised in `tools/unattended/check-unattended.sh` and
  added to its import allow-list, shipped blank with its comment in
  `tools/unattended/.unattended.conf.example`, given a row in PROTOCOL §8, and declared dated in
  this repo's `.unattended.conf`. Blank turns the notice off, announced. Observed by AC9.
- **S9 — the `--abort` notice.** A new driver constant, `HALT_CODES_HANDOFF`, names
  `external-prerequisite`, `gate-red-out-of-scope`, `scope-approval-needed` and
  `repo-state-out-of-mandate`. An `--abort` naming one of them, on a record first committed on or
  after `HANDOFF_CUTOFF` by `read_first_commit_date` or not committed yet, prints a notice naming
  `--handoff` and aborts exactly as before. It never refuses. Observed by AC10.
- **S10 — the floor.** `HOLD_FLOOR` moves from 5 to 7 in this repo's `.unattended.conf` and in the
  kit's example conf, so the shrink-only pin guards the two new members. Observed by AC11.
- **S11 — the carriers.** `VERBS.template.md` gains a `--handoff` entry. `STOPS.template.md` §2
  lists the two codes and says `--handoff` is their only producer, §4 points at the hand-off's three
  added refusals, and §11 says a hand-off owes no durable restart. `PROTOCOL.template.md` §3 gains
  the sentence that `ABORTED` means DISCARD from `HANDOFF_CUTOFF`, and §8 the key row.
  `SKILL.template.md` gains a section, "If it is done but you may not land it — hand it off", placed
  before "If it cannot finish". The renders under `memory/guides/` and the installed Skill are
  re-copied by `bash tools/unattended/adopt-unattended.sh` in the same pass. The protocol render
  has 103 bytes of headroom under its declared cap at BASE, so the protocol's additions, the
  §3 sentence, the §8 row and `handoff` in §2's parked-kind and surfaced lists, are paid for by
  trimming history prose in §2 and §3, and the render's net growth stays inside that headroom.
  Observed by AC12, AC13.
- **S13 — the two mirrors of the parked-kind sets.** Two sibling kits spell the driver's
  `PARK_KINDS` and `PARK_KINDS_OWED` because a kit reads no sibling kit at run time, and each
  self-test holds its copy to the driver in both directions. `handoff` joins
  `_RUN_PARK_KINDS` and `_RUN_PARK_KINDS_OWED` in `tools/drift-audit/drift_report.py`, and
  `PARK_KINDS`, `PARK_KINDS_OWED` and `LEDGER_SOURCES` in `tools/runlog/model.py`, where it sits
  after `waiver` so the owed kinds still lead that tuple. In `tools/runlog/selftest.py` the
  parity arm reads the owed-kinds-and-acts count off the driver instead of a typed six, and the
  ledger fixture parks one `handoff` row, so its "every source has an entry" check keeps a
  population. A committed run record stays valid: its ledger tables are graded by membership,
  and its excluded-rows template is unchanged because `handoff` is owed. Both kit versions move
  at VERIFYING, with the unattended one. Observed by AC15.
- **S12 — the arms.** Every new numbered branch gets an arm in the driver's sibling suite asserting
  a literal slice of its own text, so the harness meta-gate reads it armed. Observed by AC14.

## 3. Non-goals (OUT)

- Deriving `LANDED (attended)` from a handed record, the `--settle` verb, the `--settle` line in the
  recipe, and the fail-26 exception. Those are `TOOL-dUnstuckLanding-14`'s.
- The refresh helper `--handoff` will call before its verdict. `TOOL-dUnstuckLanding-19` adds that
  call to this verb, and this unit leaves no hook for it.
- `LANDING_NODES` and `--close` naming `--handoff` on a non-landing node: `TOOL-dUnstuckLanding-20`.
- The drift-audit signals that read `HANDOFF_CUTOFF`: `TOOL-dUnstuckLanding-15`.
- A refusal on `--abort`. The verb cannot know the work is sound; the run does.
- The kit version marker. The orchestrator moves it once, at VERIFYING.
- Carrying the kit into inCMS and NicoCares, which is ask `TOOL-dUnstuckLanding-11`.

### Edges

- **hands-off** `TOOL-dUnstuckLanding-14` — the two codes in `HOLD_CODES_HANDOFF`, which the
  derivation admits and no other; the `handoff` recipe row, which gains the `--settle` line there;
  `HANDOFF_CUTOFF`, which dates the ABORTED records `--settle` may touch; and the
  `units-at-landing` fact a settled record carries.
- **hands-off** `TOOL-dUnstuckLanding-15` — `HANDOFF_CUTOFF`, the date the two drift classes split
  on.
- **hands-off** `TOOL-dUnstuckLanding-19` — the `--handoff` verb, which that unit's refresh helper is
  called from.
- **hands-off** `TOOL-dUnstuckLanding-20` — `--handoff` with `owner-landing`, the exit a run on a
  non-landing node takes by design.
- **hands-off** `TOOL-dUnstuckLanding-18` — `--handoff` with `owner-landing` and `owner-decision`,
  the HAND OFF exit the close-decision table maps decision kinds onto.

## 4. Design

### Evidence

Read at `98926870` on 2026-10-04, PINNED to that sha. `git diff --stat 0c16a66b 98926870 -- tools/`
is empty, so every line reference the design record cites at `0c16a66b` still holds.

- `HOLD_CODES_CORE` is five members at `tools/unattended/unattended.sh:821`, and `HOLD_FLOOR="5"` sits
  at `.unattended.conf:322` and `tools/unattended/.unattended.conf.example:354`. The leg's pin reads
  the core count against that floor at `tools/unattended/check-unattended.sh:828-835`.
- `run_hold` (`unattended.sh:4833`) validates every argument, refuses a dirty tree through
  `check_clean`, checks the published tip, reaps orphans, and only then writes, in one block, from
  `phase HELD` to `hold-run`, then one history row, then stages. `--until owner` yields
  `resume-owed none · owner`, so a hand-off owes no durable restart by construction.
- `check_inherited_override` (`unattended.sh:7115`) reads the `gates-run` fact and refuses with
  fail 83 unless the bar's header reads `head` equal to HEAD and `tree_clean yes`, its verdict reads
  `tree_moved no`, and every leg in its attribution reads INHERITED. A GREEN bar writes no
  attribution, so that function alone refuses a green bar.
- `gates-green` writes and stages `gates-run` even when the close then blocks
  (`unattended.sh:7657-7659`), and `check_clean` (`:1971`) refuses any dirty path, so the record is
  committed before a hold and HEAD moves. This is S4's reason.
- The bar's `verdict` file carries `verdict GREEN|RED|REFUSED` (`tools/run-gates/run-gates.sh:3313`).
- `--close` under `in-place` writes `units-at-landing` and `asks-at-landing` at `:7505-7511`.
  `--landed` under `primary` writes the same pair at `:4603-4625`. The derived population of the
  fact-set arm requires `units-at-landing` and `landed-derived`
  (`tools/unattended/lib-unattended.sh:1156`).
- `PARK_KINDS` and `PARK_KINDS_OWED` are at `unattended.sh:669` and `:683`. The leg's dead-member
  loop greps the driver for a `park "$rel" <member> ` call site per kind, so `handoff` needs one.
- The verb-carrier join (`check-unattended.sh:3992-4040`) requires a declared verb in the driver
  header, as a `- ` entry in the verbs carrier and invoked in the Skill.
- Check 22 (`check-unattended.sh:2796-2886`) joins the example conf to PROTOCOL §8's key column, and
  the example's initialised keys to the import allow-list between the `gov:conf-allow-*` sentinels.
- The lander's two in-place verbs are spelled `{{LANDER}} --prepare --slug <slug>` and
  `{{LANDER}} --land --slug <slug>` in `SKILL.template.md:939` and `:1116`.

### Data model

New facts and rows, all in the run-state file's authored region:

| Name | Kind | Written by | Value |
|---|---|---|---|
| `hold-code` | fact, existing | `run_hold` | `owner-landing` or `owner-decision` |
| `hold-until` | fact, existing | `run_hold` | `owner`, always, under a hand-off |
| `units-at-landing` | fact, existing | the hand-off | the roster at the hand-off, as `--close` spells it |
| `asks-at-landing` | fact, existing | the hand-off | the freeze, only where non-empty |
| `handoff · item <code> · reason <recipe>` | parked row, new kind | the hand-off | the landing commands, one line |

The hand-off writes no new fact name, so no fact-set reader changes in this unit.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--handoff` | verb | none; verbs are joined by the leg's check 26 |
| `run_handoff` | shell function | `sh.function`, asked `--suggest run_handoff --as sh.function` on 2026-10-04: OK |
| `check_handoff_bar` | shell function | `sh.function`, `check` leads, snake |
| `check_handoff_code` | shell function | `sh.function`, asked on 2026-10-04: OK; the canon names `check`, not `is` |
| `render_handoff_recipe` | shell function | `sh.function`, `render` leads, snake |
| `print_abort_notice` | shell function | `sh.function`, `print` leads, snake |
| `HOLD_CODES_HANDOFF` | driver constant | no `sh.constant` cell is declared in `.lexicon.conf`, asked on 2026-10-04 |
| `HALT_CODES_HANDOFF` | driver constant | the same |
| `HANDOFF_CUTOFF` | conf key | none; conf keys are joined by check 22 |
| `owner-landing` · `owner-decision` | hold codes | none |
| `handoff` | parked kind | none |
| `record-only` | argument value | none |

The builder asks `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` for each
function before writing it. `run_handoff` follows `run_hold`, because `verb` is not a declared verb.

### The refusal order

`run_handoff` validates in this order, and nothing is written until `run_hold` reaches its write
block:

1. The slug, the record, and a terminal record, through the checks `run_hold` makes first.
2. `--code` is present and a member of `HOLD_CODES_HANDOFF`. A new numbered refusal names the two.
3. Under `owner-decision`, a `decision` row exists. A new numbered refusal.
4. Under `owner-landing`, `check_handoff_bar` admits the bar, or fail 83 refuses.
5. The roster and the freeze are derived; a freeze that cannot be derived is refused.
6. The recipe is rendered; a `LANDER` that is blank is refused, because a recipe naming no lander
   is not a recipe.
7. `run_hold "$slug" "$code" owner "$reason" "$reaped" "$unreach" ""`, with the hand-off globals
   set, and unset again on every return path.

`run_hold`'s own validation of `--code` against the effective vocabulary then passes, because both
codes are core members. Its new branch for S2 refuses a hand-off code only when the hand-off global
is empty, which is how `--hold` reaches it.

### Fail numbers

The new refusals take the next free numbers when they are written; 88 is the highest at BASE. No
number is pinned here, because siblings in this build also allocate, and the acceptance criteria
grep each refusal's own text instead.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/unattended/SKILL.md`
- `.unattended.conf`
- `tools/drift-audit/drift_report.py`
- `tools/runlog/model.py`
- `tools/runlog/selftest.py`
- `tools/drift-audit/selftest.py`

### Rollout

The verb is new and nothing calls it until a run chooses it, so it lands inert. `HANDOFF_CUTOFF` is
declared in this repo at the date this build lands, re-derived at the close as the repo's cutoff
idiom requires: strictly past the newest record any branch can still write under the old meaning.
The example ships it blank, so an adopter's notice is off until that adopter dates it.

### Alternatives rejected

- **A new phase, `HANDED`.** The design record's §1 counted 85 lines across 9 files that special-case
  `HELD`, each a site for a missed twin. Rejected there on cost, and not re-opened.
- **Redefining two halt codes to mean hand-off.** It keeps a terminal that says the run finished,
  which is the falsehood this unit exists to remove.
- **Letting `--hold` write a hand-off code.** Rejected by S2's reason: a HELD record under a hand-off
  code is what `TOOL-dUnstuckLanding-14` derives LANDED from, and one written without the guard,
  recipe and facts would derive a landing nobody vetted.

## 5. Production-readiness checklist

- security — no new write path outside the run's own record. The recipe is rendered from declared
  conf values and validated facts, never from the free-text reason, and the reason keeps every
  refusal `run_hold` applies, the bypass-flag ban included. The guard closes one hole and opens
  none: an OWN red can no longer leave as "only the landing remains".
- perf / scale — one extra `git diff --quiet` and one roster read per hand-off.
- error / empty / loading states — every refusal is numbered and comes before the first write; the
  hand-off globals are cleared on every return path, so a refused hand-off cannot leak them into a
  later `--hold` in the same process.
- observability — the HELD line, the recipe line, and the parked row `--status` counts as surfaced.
- risks — a run may take `owner-decision` to dodge the guard. That code requires a parked decision,
  and the decision row is what the owner reads, so the dodge is visible rather than silent.
- testing — the direct fixture observations below, and one arm per new branch in the driver's suite.
- migration — none; no existing record carries either code.
- user docs — the Skill section and the VERBS entry.

## 6. Acceptance criteria

- **AC1** — When `--handoff tRun --code owner-landing --reason r --reaped <the recorded keepalive>`
  runs over a fixture whose last bar reads GREEN at HEAD, the record reads `phase: HELD`,
  `hold-code: owner-landing`, `hold-until: owner`, `resume-owed: none · owner` and a non-empty
  `units-at-landing:` line, and its parked region carries one `handoff · item owner-landing` row
  whose reason contains `--prepare --slug tRun` and `--land --slug tRun` under `in-place`.
  Red when: any of those lines is absent, or the row carries the free-text reason instead of the
  recipe.
  fixture: none in the tree. The pass builds one under `%TEMP%/<short-name>` the way the suite's
  `bcsetup` and `seed_gates_run` helpers do: a bare origin, the kit copied, a committed `tRun` build
  folder, a preflighted record, and a seeded bar record under the git dir.
- **AC2** — When the same call runs over a dirty tree, and again over a record already HELD, each is
  refused with `run_hold`'s existing text and `git diff --stat` over the record is empty.
  Red when: either refusal is missing, or the record changed.
- **AC3** — When `--hold tRun --code owner-landing --until owner --reason r --reaped k1` runs, it is
  refused before any write with a message naming `--handoff`, and the record is byte-unchanged.
  Red when: the hold is written, which would make a hand-off with no guard, recipe or facts.
- **AC4** — When the seeded bar reads RED with an attribution file carrying one leg as `OWN`, the
  `--handoff --code owner-landing` call prints `fail 83`'s text ending in `its attribution reads`
  and that leg, and the record is byte-unchanged; with the same leg seeded `INHERITED` it is
  admitted; and with no `gates-run` fact in the record it is refused with the same branch's text
  `no gates-run fact in this record names a bar`.
  Red when: an OWN red is admitted, which is the defect review item M4 named.
- **AC5** — When the bar was seeded at the parent of HEAD and HEAD is a commit touching only
  the fixture's run-state file, the hand-off is admitted; when HEAD also touches a second path it is
  refused with `ran at`. And `--close tRun --override gates-green --reason r` over the first tree is
  still refused with `ran at`, so `check_inherited_override` without `record-only` is unchanged.
  Red when: the records-only commit is refused, or the relaxation reaches `--close` or `--abort`.
- **AC6** — When `--handoff tRun --code owner-decision` runs over a record with no `decision` row, it
  is refused before any write; after `--park tRun --item q --reason r` writes one, it is admitted
  over an OWN red.
  Red when: the empty record is admitted, or the guard of AC4 is applied to `owner-decision`.
- **AC7** — When the fixture build README declares an `asks:` key, the hand-off writes an
  `asks-at-landing:` line equal to what `--close` writes over the same tree; when the ask generator
  is made to fail, the hand-off is refused and the record is byte-unchanged.
  Red when: the freeze is absent, differs from the close's, or a failed freeze leaves a HELD record.
  fixture: the suite's existing ask fixture shape, which declares `ASKS_CMD` in the fixture conf.
- **AC8** — When the fixture conf sets `LANDER_MODE="primary"`, the `handoff` row's reason names the
  `--no-ff` merge of the record's `run-branch` and then `LANDER`; with `LANDER` blank the hand-off is
  refused before any write.
  Red when: the primary recipe names `--prepare`, or a blank lander yields an empty recipe.
- **AC9** — When `bash tools/unattended/check-unattended.sh --skip 28` runs over a fixture whose
  example conf declares `HANDOFF_CUTOFF` and whose PROTOCOL §8 lacks the row, it prints check 22's
  `undocumented in the protocol: HANDOFF_CUTOFF`; with the row restored and the key removed from
  the import allow-list, it prints `missing from the import allow-list`; with all three present,
  neither line appears.
  Red when: either staged break prints nothing.
  cost: one scoped leg run per arm over a small fixture, not over this repo's corpus.
- **AC10** — When `--abort tRun --code external-prerequisite --reason r` runs on a fixture record
  first committed after a `HANDOFF_CUTOFF` of `2026-01-01`, it prints a notice naming `--handoff`
  and still writes `phase: ABORTED`; with `HANDOFF_CUTOFF` set after the record's first commit, or
  blank, no notice prints; with `--code fork-unresolvable`, no notice prints.
  Red when: the notice is missing in the first case, appears in any other, or the abort is refused.
- **AC11** — When `grep -c '^HOLD_FLOOR="7"$'` runs over `.unattended.conf` and
  `tools/unattended/.unattended.conf.example`, each prints 1; and when
  `bash tools/unattended/check-unattended.sh --skip 28` runs over a fixture whose driver copy drops
  `owner-decision` from `HOLD_CODES_CORE`, it prints `has shrunk below its floor` with `6 against 7`.
  Red when: the floor stays 5, or the dropped member goes unreported.
  cost: as AC9.
- **AC12** — When `grep -c 'unattended.sh --handoff '` runs over `tools/unattended/SKILL.template.md`
  it prints at least 1, `grep -c '^- `--handoff` — '` over `tools/unattended/VERBS.template.md`
  prints 1, `grep -c 'owner-landing'` over `tools/unattended/STOPS.template.md` prints at least 1,
  and `grep -c 'HANDOFF_CUTOFF'` over `tools/unattended/PROTOCOL.template.md` prints at least 2.
  Red when: any carrier lacks its line, which check 26 or check 22 would red at the close.
- **AC13** — When `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` runs, and
  the same for PROTOCOL and VERBS, each reports no difference, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0 over the installed Skill.
  Red when: a render differs from its template, or the Skill was edited without the re-render.
- **AC14** — When `python tools/memory-tree/check-arms.py --report` runs after the arms are written,
  every new numbered branch of `tools/unattended/unattended.sh` reads armed, and none is added to
  `tools/unattended/unarmed-branches.txt` or `memory/project/unarmed-branches.txt`.
  Red when: a new branch reads unarmed or pinned.
- **AC15** — When the driver's `PARK_KINDS` and `PARK_KINDS_OWED` lines are read and compared, as
  sets, with `_RUN_PARK_KINDS` and `_RUN_PARK_KINDS_OWED` imported from the drift-audit engine and
  with `PARK_KINDS` and `PARK_KINDS_OWED` imported from the runlog model, each pair is equal and
  each holds `handoff`; and the runlog model's `LEDGER_SOURCES` opens with the owed kinds then the
  two `rescope-` acts.
  Red when: either mirror lacks `handoff`, which the two self-tests red at the close.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `drift-audit selftest` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/unattended/unattended.test.sh · the AC1 to AC10 fixtures, each staging its refusal or its notice · the suite's own arm count moves by the arms added
New arm: tools/unattended/check-unattended.test.sh · the AC11 dropped hold code against a floor of 7 · none

## 8. Open questions

- **F1 — Does `--hold` stay able to write a hand-off code?** (a) Yes, as any core code. (b) No: the
  two codes are written by `--handoff` only, and `--hold` refuses them naming it. (a) lets a record
  carry `owner-landing` with no attribution guard, no recipe and no landing facts, and
  `TOOL-dUnstuckLanding-14` derives LANDED from exactly that record. (b) costs one refusal.
  Recommendation (b). RESOLVED (agent, 2026-10-04, delegated): (b), the option satisfying the most
  stated criteria with the fewest follow-ups, M3's rule; no veto applies.
- **F2 — How does the guard tie a bar to the tree when the record was committed after the bar?**
  (a) Strict: bar head equals HEAD, as `check_inherited_override` reads today. (b) Records-only: the
  bar head and HEAD differ only in the run-state file. (c) Let `run_hold` accept a staged run-state
  difference, so the run never commits before the hand-off. (a) refuses every hand-off that follows
  a red close, because the clean-tree refusal forces a records commit first. (c) widens `--hold`'s
  clean-tree rule for every hold, which this unit did not price. (b) is scoped to the hand-off by an
  argument and leaves `--close` and `--abort` unchanged. Recommendation (b). RESOLVED (agent,
  2026-10-04, delegated): (b), the most feature-rich survivor; (c) is discarded by veto 3, since it
  widens a write-surface rule beyond this unit's tier pricing.
- **F3 — Is `owner-landing` admitted when no bar has run?** (a) Admit: the lander's bar runs at the
  push anyway. (b) Refuse through fail 83's existing "no gates-run fact" branch. (a) lets a run
  claim "only the landing remains" over work no bar graded, which is the claim the guard exists to
  back. Recommendation (b). RESOLVED (agent, 2026-10-04, delegated): (b), the survivor satisfying
  the ask's guard clause in full.
- **F4 — Does this unit print the `--settle` hint?** (a) Yes, as the design's §1 lists. (b) No: the
  line is added with the verb, by `TOOL-dUnstuckLanding-14`. Each unit is committed alone, and (a)
  would ship a commit printing a verb that does not exist yet. Recommendation (b). RESOLVED (agent,
  2026-10-04, delegated): (b); the edge is declared in §3.
- **F5 — What date does the `--abort` notice compare against `HANDOFF_CUTOFF`?** (a) Today's date.
  (b) The record's first-commit date, read by `read_first_commit_date`. The cutoff dates a record's
  MEANING, and `TOOL-dUnstuckLanding-14` and `TOOL-dUnstuckLanding-15` split ABORTED records on that
  same first-commit date; (a) would warn a legacy run whose record is graded as legacy. Recommendation
  (b). RESOLVED (agent, 2026-10-04, delegated): (b), one date for one meaning.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from ask TOOL-dUnstuckLanding-3, the design record's §1 at
  rev-2, review items M4, M6 and M11, and the spec brief for units 13 to 20.
- rev-2 · 2026-10-04 · the build pass found an interface S7 did not name: `drift_report.py`
  and the runlog model each spell the driver's parked-kind sets and hold them to it both ways,
  so a `handoff` kind added to the driver alone reds two self-tests at the close. S13 adds both
  mirrors, the runlog fixture row and AC15, and §4 lists the three files. S11 also records that
  the protocol's 103-byte headroom is met by trimming history prose in §3. No acceptance
  criterion of rev-1 moved.
- rev-3 · 2026-10-04 · the bug-class checklist over the build commit selected
  amendment-leaves-its-other-half-standing: protocol §2 listed the parked kinds and the surfaced
  set without `handoff`. S11 now names that edit and the §2 trim that pays for it, and the
  drift-audit run-record fixture gains a `handoff` owed row beside the owed kinds it carried.
- rev-4 · 2026-10-04 · §9 · implementation review round 1 M3 (id 10), the correctness lens's
  duplicate of H3, is closed by `TOOL-dUnstuckLanding-27`, whose record-only tie excludes exactly
  the paths the bar's own close step staged. No scope, design or criterion of this unit moved.

## 10. Reuse audit

The probe, run on 2026-10-04:

```
python tools/codebase-map/reuse_lookup.py "end an unattended run held for an owner to land, with a landing recipe and an attribution guard"
```

It ranked name-stem seams only (`run`, `owners_of`, `render_relocation_recipe`) and reported `.sh`
as an unscanned layer, so it cannot see the driver this unit edits. None of its hits is a hold or a
landing path. The seams reused are read from source instead, in `tools/unattended/unattended.sh`:
`run_hold` for every hold refusal and the one write block, `check_inherited_override` for fail 83,
`unit_rows` and `derive_ask_freeze` for the landing facts exactly as the in-place `--close` writes
them, `park` for the row, and `read_first_commit_date` in `tools/unattended/lib-unattended.sh` for
the notice's date. For the recipe no existing seam fits: nothing in the driver renders landing
commands, and the lookup's `render_relocation_recipe` renders a backlog move, not a landing.

Recall terms used: HELD hold-code run_hold abort halt-code owner-landing check_inherited_override fail-83 HOLD_FLOOR handoff ABORTED inherited-red

The question passed with them: "how does an unattended run hand off to the owner instead of
aborting, and what refuses a hold over an own red". It returned this build's own ask, review item
M4 and the census's account of fail 83, and nothing that contradicts the source read above.
