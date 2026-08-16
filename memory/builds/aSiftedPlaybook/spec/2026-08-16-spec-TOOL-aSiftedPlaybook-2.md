# TOOL-aSiftedPlaybook-2 — the size gate's failing case gets observed for the first time

**Status:** SPECCED · rev-7 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams tooling · ratified 2026-08-16

## 1. Goal

`tools/check-template-size.sh` has no test anywhere in the repo, no `fail()` helper, and therefore
no entry in `check-arms.py`'s population. Its failing case has never been observed by any committed
harness. The repo's own `parallel-coding-governance.domain-rules.md:44-45` states that "a new gate is
not landed until its failing case has been observed. A gate you have only ever seen pass is an
assertion about nothing." Pay that debt at the moment the gate's constant changes, because a
constant change is exactly when an unproven gate is most likely to be silently wrong.

## 2. Scope (IN)

- **S1 — the harness.** A new `tools/check-template-size.test.sh` in the shape the repo's other
  self-tests use: a `mktemp -d` scratch dir, one arm per branch, red and green both observed, no
  writes into the real tree.
- **S2 — the arms**, each an OBSERVED failure or pass, never an assertion about a constant. The
  table below is the count; no number is spelled here, because this unit's own rev history already
  shows one going stale when arms were added:

  | Arm | Input | Expected |
  |---|---|---|
  | A1 | a file of exactly `MAX_BYTES` bytes | exit 0 |
  | A2 | a file of `MAX_BYTES + 1` bytes | exit 1, message names the overage |
  | A3 | a missing path | exit 2 |
  | A4 | a file at `MAX_BYTES` bytes with every LF turned into CRLF | exit 0 |
  | A5 | `MAX_BYTES` set in the environment | the override is honoured, both directions |
  | A6 | a file of `H`+1 bytes, `H` = the value on the record's row **keyed by that subject file** | exit 0 **and** the warn line, naming `H`, the size and the delta |
  | A7 | a file of exactly `H` bytes, same keying | exit 0 and **no** warn line |
  | A8 | `--bump` on an over-high-water file | **that subject's row** is rewritten to the measured size and the delta reported |
  | A9 | `--bump` on one subject, with a second subject's row present | the second row is **byte-identical** afterwards |
  | A10 | the high-water record absent | exit 0, no ratchet, and **one explicit line saying the record is absent** — never silence, never a `set -u` failure |
  | A11 | the high-water record present but non-numeric for the subject | a NAMED failure, not a shell error |

  A6-A9 arm `TOOL-aSiftedPlaybook-1` S8's high-water ratchet. A6 and A7 together are what prove the
  ratchet is ADVISORY: A6 alone passes if the warn were accidentally built as a second blocker (it
  would exit 1 and the arm would still see the line), and A7 alone passes if the warn never fires.

  **A9 is the arm that proves the KEYING, and it is not optional.** S8 requires one `<path>\t<bytes>`
  row per measured subject precisely because this gate has two consumers: `skills/session-kickoff/SKILL.md`
  measures 18215 against a template of 32682, so a single shared value can never warn for the
  kickoff leg, and a `--bump` on that leg's argv would rewrite the shared value and make the
  template leg warn on every run forever. A6-A8 are all satisfiable by the single un-keyed number
  S8 forbids; only A9 distinguishes them.

  **A10 and A11 arm S8's degenerate-case contract**, which S8 states and hands to this unit by name.
  They are not covered by A3: A3 is a missing TEMPLATE (the gate's `file not found` branch at
  `tools/check-template-size.sh:22`, exit 2), not a missing RECORD. `set -u` is live at
  `tools/check-template-size.sh:11` and the numeric comparison at `:28` is `[ "$bytes" -gt "$MAX_BYTES" ]`,
  so an empty operand is a shell error on a leg the bar runs twice — the failure mode the contract
  exists to forbid and the one nothing observed until round 4.

  **How A6-A8 learn `H`** — the question that made the original threshold arms unbuildable. They
  **read the high-water record through the path override `TOOL-aSiftedPlaybook-1` S8 specifies**
  (a positional, then an environment variable, then the tracked default), which is the whole advantage of the ratchet
  over a constant: the value lives in a tracked file the harness can read, so no arm has to export
  its own and test the override path while never observing the shipped value. Each arm runs against
  a scratch copy of that file, never the tracked one.

  **How the harness learns `MAX_BYTES` decides whether these arms mean anything.** The gate reads
  `MAX_BYTES=${2:-${MAX_BYTES:-49152}}` — a positional, then the environment, then the default — so a
  harness that simply exports its own value tests the override path every time and never once
  observes the SHIPPED ceiling — the arms would stay green
  through any edit to the default. A1, A2 and A4 therefore run the gate with **no override** and
  read the limit back out of its own OK line (`printf … %d / %d bytes`, `:35`); only A5 sets the
  environment, because exercising the override is its whole purpose.

  A4 is the one that matters most and the one a hand-written test would omit. The gate normalizes
  CR before measuring (`:23-25`) precisely so a Windows `autocrlf` smudge cannot inflate the count
  and spuriously fail; on this fleet that smudge is the normal state, so the arm guards the
  behaviour the gate was actually written for.
- **S3 — the merge-bar leg.** An entry in `tools/gate-legs.json` so the harness rides the bar rather
  than being a file somebody remembers to run — the charter's own standard for its self-tests.
- **S4 — the charter citation.** The new leg's script path added to `AGENTS.md`'s gate-suite section.
  This is not bookkeeping: the drift-audit signal `handkept_inventories_disagreeing_with_source`
  measures 0 at pin 0 with **zero tolerance**, so an uncited leg reds the bar immediately.
- **S5 — the map dossier.** `memory/map/features/playbook.md`, minted by this unit (§8 F2), claiming
  the new leg key. Follows the pinned heading contract in `tools/codebase-map/map_lib.py:58`
  (`## Constraints & why`, `## Shared seams`, `## Gaps`) plus the graced `## Reuse affordance`,
  modelled on the 76-line `memory/map/features/codebase-map.md`. It appeared in §4, §4's Files
  touched and AC6 but never in Scope, which is the same defect this build fixed in `PLAY-3`.
- **S6 — the `fail()` refactor** (F1, resolved). `tools/check-template-size.sh`'s exit paths become
  a `fail()` helper, which pulls the gate into `check-arms.py`'s population. The source is the count;
  no number is spelled here.

  **The refactor must satisfy the discovery predicate, which imposes more than a rename.**
  `check-arms.py`'s `FAIL_RE` matches `fail <n> "…`, so every call site needs a CHECK NUMBER this
  gate has never had; `branches()` raises unless each message carries a literal run of at least
  twelve characters; and a bare positional inside a `fail` message cannot be armed, so bind the
  value to a name and put it after the literal sentence.

  **An `ARMS_FLOORS` entry is required, and NOT because an undeclared floor refuses.** It does not:
  `check-arms.py` reads `want = floors.get(gate_rel)` and `continue`s when it is absent, so a
  discovered gate with no entry is **silently skipped** — §4 of this spec states that correctly two
  sections earlier. The entry is what makes the pin real, and its grammar is
  `<gate>:<branches>:<armed>`, values read from `--report` after the refactor.

## 3. Non-goals (OUT)

- **Changing what the gate enforces.** The constant is `TOOL-aSiftedPlaybook-1`. This unit proves
  whatever number that one lands. Sequenced after it so the arms are written against the live value.
- **Testing the other untested gates.** `check-template-size.sh` is almost certainly not the only
  gate outside `check-arms.py`'s population, and a repo-wide sweep is its own unit. Recorded as a
  follow-up row rather than absorbed here.
- **Retrofitting `fail()` into every gate that lacks it.** The owner resolved F1 to refactoring
  THIS gate (S6); a repo-wide sweep of every gate outside `check-arms.py`'s population remains its
  own unit and a follow-up row.

## 4. Design

### Inventory — why this gate is currently unguarded

Three independent mechanisms could have caught the gap and none does:

| Mechanism | Why it misses |
|---|---|
| `tools/memory-tree/check-arms.py` | Its population is tracked `*.sh` that define `fail() {` and call `fail <n> "`. This gate uses plain `echo` + `exit`, so it is never discovered. |
| `.memory-tree.conf` `ARMS_FLOORS` | Five gates are pinned; this one is not among them, and an undeclared floor is the quietest way to be outside a pin. |
| `tools/run-gates.test.sh` | The canary asserts the manifest is well-formed and that `run-gates.sh` hardcodes no leg command. It says nothing about whether a leg's own failure has been observed. |

### The four-gate trap fires here, and here it really is four

`TOOL-aSiftedPlaybook-1`'s rename trips three gates. This unit ADDS a leg, which is the case the
charter's trap was written for, and all four fire:

1. **codebase-map coverage** — the new leg name becomes an inventory key and must be claimed in a
   dossier. `baseline.toml` additions are reserved for the initial backfill.
2. **codebase-map freshness** — `memory/map/generated/{MAP.md,inventories.json}` must be
   regenerated with `python tools/codebase-map/gen_map.py --write`, never hand-edited.
3. **kickoff-manifest ratchet** — `tools/gate-legs.json` is a watched pathspec, so `last-audit`
   re-stamps with a delta line.
4. **drift-audit hand-kept signal** — S4's charter citation, pin 0, tolerance 0, no slack.

**F1 of `TOOL-aSiftedPlaybook-1` resolved to the in-place `baseline.toml` swap, so THIS UNIT MINTS
`memory/map/features/playbook.md`.** That unit renames an existing key and mints no dossier; this
one adds a genuinely NEW leg, and a new key is an addition rather than a rename — the case
`baseline.toml` reserves for the initial backfill and the coverage gate's own docstring sends to a
dossier. `TOOL-aSiftedPlaybook-3` then extends it. The dossier follows the pinned heading contract
in `tools/codebase-map/map_lib.py:58` plus the graced `## Reuse affordance`, modelled on the
76-line `memory/map/features/codebase-map.md`.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/check-template-size.test.sh` | new |
| `tools/govkit/registry.toml` | the harness above DECLARED. **Mandatory and measured:** in a scratch clone of BASE, `python tools/govkit/govkit.py selfcheck` exits 0 with `0 unclaimed`, and exits 1 the moment `tools/check-template-size.test.sh` is staged — "neither an entry member nor an exemption". Exemptions are exact-path (`tools/govkit/govkit.py:501-519`), so the sibling gate's own `[[exempt]]` row at `registry.toml:150` does NOT cover it; the `run-gates.sh` / `.test.sh` / `.evidence.test.sh` trio at `:134`/`:142`/`:146` is the precedent that each path needs its own row |
| `tools/check-template-size.sh` | S6's `fail()` refactor — F1 is RESOLVED, this is unconditional |
| `tools/gate-legs.json` | one leg entry |
| `AGENTS.md` | one gate-suite bullet |
| `memory/map/features/playbook.md` | new — minted by S5 |
| `memory/map/generated/*` | regenerated, never hand-edited |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

### Alternatives rejected

- **Rely on `AC2` of `TOOL-aSiftedPlaybook-1`** (the one-shot by-hand boundary check). Rejected: it
  proves the constant took effect once, on one machine, on one day. It is an observation, not a
  gate, and the class it guards recurs at every future ceiling change.
- **Write the test but do not wire it as a leg.** Rejected explicitly. The charter's phrasing for
  its self-test legs is that they ride the bar "so a gate and the proof it can fail are both
  visible", and that "a self-test nobody cites is a leg nobody notices going quiet". An unwired
  test is that exact failure with extra steps.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the arms build small scratch files; the leg is sub-second and will schedule early
  in the runner's longest-first order without displacing anything.
- a11y / i18n — N/A.
- error / empty / loading states — A3 (missing file, exit 2) is the gate's error path and is armed.
- observability — the harness prints one line per arm, naming the arm that failed.
- risks — the notable one is **arm vacuity**. A2 must assert on the OBSERVED exit code and on the
  message naming the overage, not merely that the command was non-zero; and A1/A2 must bracket the
  boundary exactly, because a test that feeds a 10 MB file proves only that the gate dislikes very
  large files. The repo has been bitten by the vacuous-arm class repeatedly and
  `domain-rules.md:98` names it.
- testing + left-shift gates — this unit IS the left-shift.
- migration / rollback — new file plus one manifest row; revert cleanly.
- user docs — N/A, gov-internal tooling.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.test.sh` runs on a clean tree, it exits 0 and prints
  one line per arm in S2's table — **that table is the expected set**, since S2 deliberately states no
  arm count and an unanchored "one line per arm" cannot detect an omitted arm.
- **AC2** — When the gate's comparison operator is inverted by hand (`-gt` to `-lt`) and the harness
  is re-run, it exits non-zero naming the arm that caught it. This proves the harness can fail,
  which is the entire point of the unit and is itself an instance of the rule it enforces.
- **AC3** — When A4 runs, a CRLF file of exactly `MAX_BYTES` normalized bytes exits 0. When the
  gate's `tr -d '\r'` is removed by hand, A4 reds.
- **AC4** — When `bash tools/run-gates.sh` runs, the new leg appears in the output by name and is
  green; when `bash tools/run-gates.test.sh` runs, the canary is green with the new manifest entry.
- **AC5** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0 — i.e. S4's charter
  citation landed. A red here means the leg was added and the charter was not told.
- **AC7** — When `python tools/memory-tree/check-arms.py --report` runs, it names
  `tools/check-template-size.sh` with a NUMERIC floor rather than `unset`; when the floor is lowered
  by hand, `--check` reds. Without this the whole S6 half can be skipped with every other AC and
  `bash tools/run-gates.sh` green, because nothing else reads `.memory-tree.conf`.
- **AC8** — When the warn comparison in `tools/check-template-size.sh` is inverted by hand,
  `bash tools/check-template-size.test.sh` reds naming A6 or A7;
  when the high-water record's path resolution is broken, A8 reds; when `--bump` is made to rewrite
  the whole record instead of the subject's row, **A9** reds; when the absent-record branch is made
  to fall through silently, **A10** reds. The ratchet arms were the
  only ones in this unit with no proof they can fail, inside the unit whose §1 quotes "a gate you
  have only ever seen pass is an assertion about nothing" — AC2's inversion touches the ceiling
  comparison, not the warn branch.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` runs, it is green with
  `tools/check-template-size.test.sh` declared in `tools/govkit/registry.toml`. This unit creates a
  depth-1 path under `tools/` and the registry asserts that surface, so the declaration and the
  harness land in the same commit. Reproduced at BASE rather than argued: without the row the leg
  exits 1, and the leg carries no `guard` in `tools/gate-legs.json`, so it reds on diff-scoped runs
  as well as at the push boundary — AC4's `bash tools/run-gates.sh` cannot be green without this.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage and freshness are
  both green, with the new key claimed in a dossier and NOT in `baseline.toml`.

## 7. Gates

- `bash tools/check-template-size.test.sh` — the new leg itself.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — coverage + freshness.
- `python tools/drift-audit/drift_report.py --check` — the zero-slack citation signal.
- `bash skills/session-kickoff/manifest-check.sh` — `tools/gate-legs.json` is watched.
- `python tools/memory-tree/check-arms.py` — F1 resolved to the refactor, so this is mandatory. Note
  it CANNOT catch a missing `ARMS_FLOORS` entry: an undeclared floor is skipped, not refused. AC7 is
  what observes the entry.
- `python tools/govkit/govkit.py selfcheck` — **mandatory, and the one this unit was missing.** S1
  creates `tools/check-template-size.test.sh`, a depth-1 path under the `tools/*` surface
  `tools/govkit/registry.toml` asserts; undeclared, the leg exits 1. It carries no `guard` in
  `tools/gate-legs.json`, so it is not scoped away on a records-only or diff-scoped run. AC9
  observes it.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — both forks below are RESOLVED.

- **F1 — does `check-template-size.sh` get refactored to use a `fail()` helper?**
  **RESOLVED (owner, 2026-08-16): yes, refactor.** Built as S6, with the mandatory `ARMS_FLOORS`
  entry. The reasoning the owner ratified: a test proves the gate can fail once; the meta-gate proves
  the test keeps proving it. The original framing:

  Doing so pulls it
  into `check-arms.py`'s population automatically, which then demands a sibling `.test.sh` with a
  positive arm per branch (this unit supplies it) plus an `ARMS_FLOORS` entry in `.memory-tree.conf`.
  The payoff is durable: the harness meta-gate would thereafter notice an arm being deleted or a
  branch going unasserted, which is a different guarantee from "a test exists today".
  The cost is that the gate's three `echo`+`exit` sites change shape, and the charter records a trap
  here — a positional `$1` inside a `fail` message cannot be armed, so any value must be bound to a
  name and placed after the literal sentence.
  **Recommendation: yes, refactor.** A test proves the gate can fail once; the meta-gate proves the
  test keeps proving it. The whole unit exists because "somebody will remember" was already tried
  and produced a gate with no test at all. Owner's call because it widens the diff on a merge-bar
  gate, which the tier rule prices as a contract change.

- **F2 — who mints `memory/map/features/playbook.md`?**
  **RESOLVED (agent, 2026-08-16, downstream of TOOL-1 F1): THIS UNIT mints it;
  `TOOL-aSiftedPlaybook-3` extends it and reds if it is absent.** The owner's F1 choice sent
  `TOOL-aSiftedPlaybook-1` to the in-place baseline swap, which mints no dossier, and this unit adds
  the first genuinely new key. Marked `(agent, …)` and not `(owner, …)` deliberately: the owner
  decided F1, not this; this is the mechanical consequence, and signing it as theirs would make the
  two indistinguishable later. The original framing:

  **THREE units need it**, not two:
  `TOOL-aSiftedPlaybook-1` under F1 option 3, this unit for its new leg key, and
  `TOOL-aSiftedPlaybook-3` for its own leg key. The README fixes the order TOOL-1 → TOOL-2 → TOOL-3.
  **Recommendation: the first unit that needs it mints it; the later two EXTEND it and red if it is
  absent** — never mint a second. Concretely: if `TOOL-aSiftedPlaybook-1` F1 resolves to option 3,
  TOOL-1 mints; under options 1 or 2 it does not need a dossier at all and this unit mints. Either
  way `TOOL-aSiftedPlaybook-3` always extends. Written into all three §9s at build time. Not an
  owner decision on its own — it is downstream of F1 — but it must not be left implicit, because two
  dossiers claiming overlapping keys reds coverage in both directions.

## 9. Revision log

- rev-7 · 2026-08-16 · folded round-4's **blocker B1**, plus M1 and H3. **B1**: S1 creates
  `tools/check-template-size.test.sh`, a depth-1 path under the `tools/*` surface
  `tools/govkit/registry.toml` asserts, and this spec named the registry in no section — no §4 row,
  no §7 gate line, no AC. Reproduced rather than argued: in a scratch clone of BASE,
  `govkit selfcheck` exits 0 with `0 unclaimed` and exits 1 the moment that path is staged, and the
  leg carries no `guard`, so it reds diff-scoped runs too. Round 3's fold enumerated four new
  depth-1 paths and there are five; the count in `TOOL-aSiftedPlaybook-1` AC12 that certified
  otherwise is deleted there. Added the §4 row, the §7 line and **AC9**. **M1**: `TOOL-aSiftedPlaybook-1`
  S8 ends "Both are armed in `TOOL-aSiftedPlaybook-2` S2" and neither was — A3 is a missing TEMPLATE,
  not a missing RECORD, and `set -u` is live at the numeric comparison. Added **A10** (absent record)
  and **A11** (non-numeric), with AC8 extended. **H3**: A6-A8 read `H` from an un-keyed value while
  S8 requires one row per measured subject; the arms are now bound to a subject row and **A9** proves
  a `--bump` on one subject leaves the other byte-identical — the arm round-3 H1 asked for and the
  only one that distinguishes the keyed record from the single number S8 forbids. (Round 4's fold
  list named rev-6 as the target; this spec was already at rev-6.)
- rev-6 · 2026-08-16 · folded round-3 M4, M5 and H3's second half. Three carriers still gated
  RESOLVED forks on conditionals — §4's two rows and §7's `check-arms.py` line, which is the section
  a builder reads to know what must run. AC8 added: A6-A8 were the only arms with no red proof, and
  AC1's "one line per arm" is now anchored to S2's table, since S2 states no count and an omitted arm
  was undetectable. S2 now points at TOOL-1's path override rather than naming the tracked file.
- rev-5 · 2026-08-16 · folded round-3 H2, H3 and M1. **H2**: "an undeclared floor is its own
  refusal" is FALSE — `check-arms.py` skips a gate with no `ARMS_FLOORS` entry — and that false
  premise was the entire justification for S6's mandatory conf entry, with no AC reading the conf at
  all. Replaced with the refusals that exist, plus AC7 observing the entry directly. S6 also now
  states the discovery predicate's real requirements: numbered checks, a twelve-character literal
  run per message, and the floor grammar. The exit-site count is deleted; the source is the count.
- rev-4 · 2026-08-16 · owner resolved F1 (refactor) and the round-2 audit `wf_98677a7a-009` closed
  three findings. **S5 and S6 added**: the map dossier mint appeared in §4, Files touched and AC6
  but never in Scope, and the `fail()` refactor had no scope item at all. A6/A7 rewritten against
  `TOOL-1`'s high-water ratchet, which also answers how they learn the value — they read the
  tracked file, where a threshold constant left them no route but exporting their own value, the
  vacuity rev-3 folded this section to prevent. A8 added for `--bump`. Deleted the arm COUNT from
  S2's lead sentence: it said "five" over a seven-row table, which is the ratcheting-count class
  this build exists to close, reproduced inside it.
- rev-3 · 2026-08-16 · absorbed the owner's resolutions on `TOOL-aSiftedPlaybook-1`. F1's in-place
  baseline swap makes THIS unit the minter of `memory/map/features/playbook.md`, resolving F2. F2's
  WARN threshold adds arms A6 and A7, which together prove the threshold is advisory — either alone
  passes under a plausible wrong implementation. F1 of this spec (the `fail()` refactor) was not put
  to the owner and remains OPEN.
- rev-2 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`. S2 never said how the harness learns
  `MAX_BYTES`; a harness exporting its own value would have tested the override path five times and
  never observed the shipped ceiling, leaving every arm green through an edit to the default.
  F2 counted two contenders for the map dossier where there are three. Corrected the
  `drift_report.py` gate spelling to `--check` in §7 and AC5.
- rev-1 · 2026-08-16 · initial draft. The absence of any test was established by direct search
  (no `tools/check-template-size.test.sh`, no `fail()` in the gate, no `ARMS_FLOORS` entry) and
  confirmed independently by the `blast-radius` lens of `wf_4e13d9e7-550`.

## 10. Reuse audit

The seam is `tools/gate-legs.json` plus the self-test harness shape the repo already ships eight
times over. **A new harness copies the nearest existing sibling rather than inventing a shape**:
`tools/check-install-prefix.test.sh` is the closest analogue — same directory, same
scratch-dir-and-arms structure, same "no writes into the real tree" discipline — and
`tools/memory-tree/check-verdict-epoch.test.sh` is the model for an arm that inverts a comparison to
prove the gate reds.

`python tools/codebase-map/reuse_lookup.py "template size ceiling gate enforcement"` also surfaced
`t_gate_template_boundary` and `t_gate_template_finds_the_kit` in
`tools/codebase-map/selftest.py` — **these are NOT this gate's tests** despite the promising names;
they exercise the codebase-map gate template's own boundary resolution. Recorded because the name
collision is exactly the sort of thing that makes a future session believe coverage exists.

Recall terms used, recorded per M5: `template size gate byte ceiling externalize companion
domain-rules headroom strict limit raise refuse stub`. No prior record proposes testing this gate;
the nearest is `TOOL-aRootedPrefix-3` (OPEN), which notes hygiene checks 6/7 measure raw
working-tree bytes "as `check-template-size.sh` already does" — citing this gate as the correct
model while nothing verifies that it works.
