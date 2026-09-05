# TOOL-aHonedRuleset-8 — the micro-format gate reaches the adopter who takes the charter

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 94958534 · streams deployer · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/check-microformats.sh` arrive in a target that takes the governance charter, by moving
its registry entry onto the two selections an adopter actually walks. The entry, the payload and the
gate legs already exist and are proven to run in a scratch install; what does not exist is any path
from an operator's install command to them.

## 2. Scope (IN)

- **S1 — `check-microformats` joins the declared default selection.** One id added to the list at
  `tools/govkit/registry.toml:36`. Measured at base, `govkit.resolve_selection(reg, descs, 'default',
  [], None)` returns six ids and none of them is this one.
- **S2 — the entry stops being conditional.** Delete `selectable = "conditional"` at
  `tools/govkit/entries/check-microformats.kit.toml:14`, so `govkit.all_kits()` reaches it. Rewrite
  the descriptor's header paragraph at lines 6 to 8, whose argument is the `--all` exclusion this
  scope item removes; the replacement states why the gate now travels with the charter and how a
  target that does not want it declines. `requires = ["playbook"]` at line 15 stays exactly as it is.
- **S3 — the runbook names the entry.** `WIRE-INTO-PROJECT.md:82` is the `intake --kits` example an
  operator copies; it gains `check-microformats` in the id list. One sentence follows the code block
  saying the gate arrives with the charter and grades its definition block. **The sentence names the
  ENTRY ID and no file path** — see the §4 carried-prefix constraint, which makes that a correctness
  requirement rather than a style choice.

## 3. Non-goals (OUT)

- **No charter byte moves.** `coding-governance-agents.template.md` and `AGENTS.md` are untouched.
  `TOOL-aHonedRuleset-2` owns the §16 grammar cut; the two units share a subject and no file, land
  independently, and neither waits on the other.
- **The charter does not name the gate.** `TOOL-aHonedRuleset-2` §4 left that question here; §8 F3
  answers it as no, and no `{{MICROFORMAT_GATE}}` placeholder is added either.
- **No new deployer machinery.** No `implied_by`, no reverse-`requires`, no rule that selecting an
  entry drags in a conditional one that requires it. §8 F1 records why the registry is already the
  general answer and F2 records why an inference rule would fight a specced sibling.
- **No selfcheck arm is built.** The regression guard §8 F1 discusses is FILED, following the
  precedent `TOOL-aPacedTurnstile-1` §8 fork B set for exactly this shape and the backlog row
  `TOOL-aPacedTurnstile-11` it produced.
- **No `last-audit` re-stamp.** Verified against the `watch:` list at `memory/guides/SESSION-KICKOFF.md:6`:
  none of this unit's three files is on it. Units 2 through 6 of this build all bundle that re-stamp
  and this one must not, or it stamps a line no staged path obliged.
- **The other four conditional entries keep their classification.** `check-agent-cap-restatement`,
  `check-install-prefix`, `check-line-length` and `check-placeholders` are not re-examined.
- **`TOOL-aScouredKit-23` and `TOOL-dSpentCeiling-4` are cited, not answered.** The first owns whether
  `WIRE-INTO-PROJECT.md` gets a ceiling; the second owns whether a kit may spend an adopter's read
  budget. S3 adds bytes to an uncapped document and §8 F4 prices that, without ruling on either row.

## 4. Design

### What is already true, and why the ruling's premise needs correcting

`TOOL-aHonedRuleset-2` §8 F3 states that `tools/check-microformats.sh` does not ship. Read against
the deployer at this unit's base, that is false in its literal form and true in its consequence.

| fact | evidence at base 94958534 |
|---|---|
| the gate is a declared registry entry | `tools/govkit/registry.toml` names `check-microformats` with descriptor `tools/govkit/entries/check-microformats.kit.toml` |
| its payload is declared | that descriptor's `[[files]]` includes `check-microformats.sh` and `check-microformats.test.sh`, `role = "engine"` |
| it emits two gate legs into a target | `[[gate_leg]] micro-format definitions` and `micro-format gate selftest` |
| the repo-subject leg is wired to the target's own charter | its argv is `["bash", "{prefix}/check-microformats.sh", "{playbook_path}"]` |
| it is proven to install AND RUN in an adopter | `tools/govkit/matrix.py:48` lists it in `SCRATCH_KITS`, and `:61` pins the leg's output at `microformats OK —` |

So the gate ships, installs, and executes against a deployed charter, and a merge-bar leg proves it.
The defect is narrower and entirely in the SELECTION layer.

**One caveat on that last row, added at rev-2.** The proof is manufactured by a harness typing the
id: `SCRATCH_KITS` is a hand-written list, so the matrix installs an entry no operator's command
reaches. The evidence that the gate RUNS is real; the evidence that anyone would ever GET it is not,
and that is the defect restated from the other side.

### The defect, measured

Resolved live through `govkit.read_descriptors` and `govkit.resolve_selection` rather than read off
the registry by eye:

| selection | members | reaches `check-microformats` |
|---|---|---|
| `[selection] default`, `tools/govkit/registry.toml:36` | 6 | no |
| `--all`, derived by `all_kits()` at `tools/govkit/govkit.py:483` | 20 | no |
| the registry as a whole | 25 entries, 5 of them conditional | — |

`all_kits()` returns every entry NOT marked conditional, and the default set is a literal declaration
that does not name this one. An operator therefore reaches the gate only by typing its id into
`--kits`, and the id appears nowhere an operator reads: `git grep -l check-microformats` returns no
hit in `WIRE-INTO-PROJECT.md`, and the runbook's §2 kit menu does not offer it.

`govkit selfcheck` is silent about this by design. Its arm 7b at `tools/govkit/govkit.py:1350-1353`
fails an entry "reached by no selection and is not marked conditional" — the conditional mark is
exactly the escape this entry takes, so the state is declared rather than undetected.

**`--kits` REPLACES the default set; it does not add to it.** Added at rev-2, because S3's
justification turns on it and rev-1 did not state it. `resolve_selection`'s `mode == "kits"` branch
at `tools/govkit/govkit.py:559-568` returns `derive_install_order(sorted(kits), descs)` and consults
neither the default set nor the target's `deploy.toml`; `cmd_intake` calls the resolver with no
`deploy` argument at all (`:8131`). `WIRE-INTO-PROJECT.md:82` — the §2 command an operator copies —
passes `--kits` explicitly. **So S1 alone does not reach an operator who follows the runbook**, and
S3's id is what closes that, not merely what documents it.

A second consequence, noted rather than acted on: gov's own `.governance/deploy.toml:18-22` declares
19 kits explicitly and takes the target's-own-list branch, so S1 changes nothing about gov's own
install. The default set's audience is a fresh adopter with no declaration, and gov is not one.

### Why the mark is wrong

The descriptor's own header argues the mark from `--all`: an adopter who does not take the charter
should not have the gate forced on them. That argument does not survive the measurement above,
because `--all` includes `playbook` and `playbook-render`, both non-conditional. A target installing
`--all` receives the charter and its renderer, and then does not receive the gate over the block the
renderer produced. The default set has the same shape: it names `playbook`, so it deploys a charter,
and it names no gate for it.

There is no selection in which the gate would arrive without a charter to grade. Dropping the mark
therefore costs nothing it was protecting, and a target that genuinely wants the charter ungated
declines the entry the way any other entry is declined, through `--kits` or the target's own
`deploy.toml` `kits` list.

### Inventory

The five conditional entries, with what each one's `requires` names, because F1 and F2 turn on this:

| entry | requires | in the default set today |
|---|---|---|
| `check-agent-cap-restatement` | `agent-cap` | no; `agent-cap` is not in the default set either |
| `check-install-prefix` | none | no |
| `check-line-length` | none declared | no |
| `check-microformats` | `playbook` | no; `playbook` IS in the default set |
| `check-placeholders` | none | no |

`check-microformats` is the only one of the five whose dependency the default selection already
installs. That asymmetry is the whole finding: the other four are conditional on something a target
may genuinely lack, and this one is conditional on something the default install always has.

### The carried-prefix constraint on S3

`tools/check-install-prefix.sh` carries a second arm, the carried-prefix BAN, whose population is the
descriptor-resolved shipped set PLUS `WIRE-INTO-PROJECT.md` as one named addition. Its predicate is
at epoch 2, which counts `tools/<kit>/<file>.<ext>` AND a loose file directly under `tools/` that
exists in the tree — and `tools/check-microformats.sh` is exactly such a loose file.
`tools/install-prefix-carried.txt:11` records `WIRE-INTO-PROJECT.md` at 47, and the arm is a ban
rather than a ratchet: `--write-ratchet` may lower a count and may not raise one.

So a runbook sentence spelling `tools/check-microformats.sh` reds the bar, and the remedy the gate
prints cannot absorb it. S3's sentence names the bare entry id, which is not a path and matches no
arm. AC6 observes that the recorded count did not move.

### Migration

None. Three declaration edits to tracked files; no data shape changes and no target is re-installed
by this unit.

### Rollout

One commit. `tools/govkit/registry.toml` and the descriptor must move together for `govkit selfcheck`
to stay coherent, and the runbook sentence describes what those two lines do, so splitting the commit
would leave the runbook describing a selection that does not exist yet.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/govkit/registry.toml` | S1 — one id added to `[selection] default` at line 36 |
| `tools/govkit/entries/check-microformats.kit.toml` | S2 — line 14 deleted, header paragraph at lines 6 to 8 rewritten |
| `WIRE-INTO-PROJECT.md` | S3 — the id added to the `--kits` example at line 82, plus one sentence |

### Alternatives rejected

- **Add to the default set and keep `selectable = "conditional"`.** Legal — `resolve_selection`'s
  default branch does not filter on the mark — and it leaves the `--all` half of the gap open, while
  producing a registry where `--all` installs strictly less than the default in one respect. Two
  reachability answers for one entry is the shape this repo's own declarations exist to prevent.
- **Teach the deployer that a conditional entry is implied when everything it `requires` is
  selected.** This is the class-shaped fix and §8 F2 rejects it. Corrected at rev-2: as worded the
  rule fires for FOUR of the five conditional entries over the default selection and all five over
  `--all`, because an absent or empty `requires` satisfies it vacuously — it deletes the conditional
  class rather than adding one entry. It also points the deployer the opposite way from
  `DEPL-aHoistedPass-1`, which is SPECCED to REFUSE a selection with an unsatisfied `requires` rather
  than to complete it, and the owner has already ruled refuse-not-expand (see §8 F2).
- **Ship the gate through `tools/playbook/adopt-playbook.sh` instead.** That adopter renders the
  charter region and copies nothing else; giving it a payload would create a second install path
  beside the registry for a file the registry already declares, which is the two-answers-to-one-question
  shape `registry.toml`'s own header opens with.
- **Add a runbook bullet to the "What the renderer cannot decide for you" list.** Rejected, but the
  rev-1 reason was wrong and is replaced here. That list is not confined to render-time judgement
  calls: its own intro at `WIRE-INTO-PROJECT.md:91-92` calls it "the answers `intake` will ask for,
  and the kits whose blocks the charter carries", and it already carries a gate kit in drop-it-if
  terms at `:115` (`gate-lint`). The real reason is the §4 carried-prefix constraint: a bullet in
  that list SPELLS A PATH, which is exactly what the carried-prefix ban fires on. The sentence goes
  beside the `--kits` command it changes, and names the bare id.

## 5. Production-readiness checklist

- security — N/A. Three declaration edits; no write path, no new surface, no credential handling.
- perf / scale — a default install gains two engine files and two emitted gate legs. One of them,
  `micro-format gate selftest`, carries `subject = "kit"`, so an adopter's runner holds it by default
  the way gov's does.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No runtime and no user interface.
- observability — the adopter's leg prints `microformats OK — <n> definition(s) graded`, and
  `tools/govkit/matrix.py:61` pins that prefix, so a change in what the leg says surfaces on gov's own
  bar rather than in a target.
- risks — the default selection grows, and gov's own suite has arms keyed on the default plan. The
  one measured hazard is `tools/govkit/selftest.py:2366`, which asserts the default selection previews
  exactly four `SIDE|rendered` rows. The two added rows are `role = "engine"` under a plain `to`, so
  they classify as `write` through `KIND_MARKS` at `tools/govkit/govkit.py:1992` and not as
  `SIDE|rendered`; AC5 runs the arm rather than trusting that reading. The strict-subset arm at
  `selftest.py:2354` compares a one-kit target's writes against the default's and survives a larger
  default by construction.
- testing + left-shift gates — no new gate. The left-shift for "does this gate work in an adopter"
  already exists at `tools/govkit/matrix.py`; what this unit changes is the input to `govkit
  selfcheck`'s arm 7b, which already grades reachability. The residual gap — nothing stops a future
  edit re-adding the conditional mark — is §8 F1's fork and is filed rather than built.
- migration / rollback — `git revert` of one commit restores all three files. A target already
  installed is unaffected until it next runs `govkit update`.
- user docs — S3 is the doc change, and `WIRE-INTO-PROJECT.md` is the only doc that describes an
  install.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py plan --target <scratch>` runs with NO `--kits` and the
  scratch target's `deploy.toml` declares no `kits` list, the preview's write set contains
  `check-microformats.sh`; and when the id is removed from `tools/govkit/registry.toml:36` and the same
  plan is re-run, it does not. Both halves, because the positive alone is satisfied by any selection
  that installs everything.
- **AC2** — When `govkit.all_kits(descs)` is resolved over the live registry, it returns 21 entries
  and `check-microformats` is among them, against the 20 measured at base.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and its closing line still
  reports `0 unclaimed` over 25 entries, proving no entry was orphaned by the mark's removal.
- **AC4** — When `python tools/govkit/matrix.py` runs, it exits 0 and shape 5 still reports the
  `micro-format definitions` leg printing `microformats OK —` from a scratch install.
- **AC5** — When `python tools/govkit/selftest.py` runs, it exits 0, and specifically the arm named
  `the default selection previews exactly 4 SIDE|rendered rows` is `ok`.
- **AC6** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and prints
  `carried-prefix clean`, and `git diff -- tools/install-prefix-carried.txt` is empty — so S3's
  sentence raised no file's recorded count, and `WIRE-INTO-PROJECT.md` still stands at 47.
- **AC7** — When `git diff -- coding-governance-agents.template.md AGENTS.md` runs at the end of the
  unit, it is empty, proving this unit moved no charter byte and left `TOOL-aHonedRuleset-2`'s subject
  alone.
- **AC8** — When every change is staged and `bash skills/session-kickoff/manifest-check.sh --staged`
  runs, it exits 0 with `git diff -- memory/guides/SESSION-KICKOFF.md` empty — proving no watched
  pathspec was touched and no `last-audit` re-stamp was owed or taken.
- **AC9** — When `grep -c '^selectable' tools/govkit/entries/check-microformats.kit.toml` runs, it
  returns 0, and `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns at least 2 against the 0
  measured at base.
- **AC10** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary it is GREEN, and
  because this unit edits `tools/govkit/`, `GATE_FULL=1 GATE_SELFTESTS=1 bash
  tools/run-gates/run-gates.sh` is GREEN too — the total run a Definition of Done owes for kit work.

## 7. Gates

Leg names as `tools/gate-legs.json` spells them:

- `govkit selfcheck` — `chunk: declarations`, `subject: repo`, unguarded, so it runs on every bar. Its
  arm 7b is the predicate whose input this unit changes. Green at base, must stay green.
- `govkit acceptance matrix` — guarded on `tools/govkit/`, which S1 and S2 stage, so it is owed. It is
  the only leg that executes the shipped gate inside a scratch adopter, and it is therefore the real
  evidence behind AC4.
- `govkit selftest` — guarded on `tools/govkit/` and `subject: kit`, so a default bar HOLDS it. AC10
  is what runs it, and this unit is kit work, so the held run is owed rather than optional.
- `govkit refusal join` — guarded on `tools/govkit/`. It is a shrink-only branch floor; this unit adds
  no refusal branch, so the floor is unmoved and the leg is named here only because its guard fires.
- `install-prefix (shipped surface)` and `install-prefix self-test` — the constraint §4 states on S3's
  wording. AC6 reads the first one's carried-prefix arm.
- `micro-format definitions` — the gov-side twin of the leg this unit makes reachable in a target.
  Untouched here, green at base with `11 definition(s) graded, 11 keyword(s) derived`, and named so a
  reader is not left wondering whether the charter moved.
- `kit version markers` — the descriptor declares `version_from = { none = ... }`, so S2 owes no
  version bump. Stated rather than left as an unexplained absence.
- `playbook render wiring` — untouched, because AC7 forbids a charter edit. Named for the same reason.

No new gate. §8 F1 recommends filing one and explains why building it inside this unit would be a
deployer contract change smuggled into a two-line declaration edit.

## 8. Open questions

- **F1 — is this one script's problem, or does the playbook adopter have no general answer for gov
  scripts that gate the charter's own claims?** *Recommendation: treat it as the instance it is, land
  S1 to S3, and FILE the regression guard rather than build it.* **The recommendation stands. Four of
  rev-1's premises for it do not, and are corrected below — do not ratify this fork on the rev-1
  reading.** What survives: `tools/govkit/registry.toml` IS the general mechanism, 25 `[[entry]]` rows
  and 23 `[[exempt]]` rows, asserted in both directions by selfcheck arm 8
  (`tools/govkit/govkit.py:1896-1932`), which reds on an unclaimed tracked path, on an exemption
  naming a path that no longer exists, and on a claim that is not tracked. Measured live:
  `surface 64 tracked path(s) · 25 entr(y|ies) · 23 exemption(s) · 0 unclaimed`. Of the five
  conditional entries, only this one's stated reason fails on measurement, so the class is not
  systematically broken.
  - **Correction 1 — `check-placeholders` and `check-line-length` do NOT ship.** Both carry
    `selectable = "conditional"` (`check-placeholders.kit.toml:17`, `check-line-length.kit.toml:16`),
    so neither reaches the default set nor `--all`; an operator gets them only by typing the id, the
    identical state this unit is fixing. §4's own inventory table says so and the rev-1 bullet
    contradicted it. Their stated reasons DO survive measurement, unlike this entry's:
    `check-line-length` grades a declaration that is gov's own (`tools/line-length-limits.txt`, and
    `matrix.py:66` pins its install-day verdict as `NOT ADOPTED — no declaration at`), and
    `check-placeholders` hardcodes `TEMPLATE="coding-governance-agents.template.md"`.
  - **Correction 2 — THREE declaration files, not four.** `tools/template-size-limits.txt` and
    `tools/template-size-highwater.txt` (`check-template-size.sh:54` and `:96`) and
    `tools/playbook-kit-waivers.txt` (`check-playbook-parity.sh:40`). Counting the two self-tests
    gives five.
  - **Correction 3 — the exemption reasons do not share one distinction.** `registry.toml:223` and
    `:231` do rest on the subject being absent from an adopter tree ("an adopter's instantiated
    playbook has no kit population to check"). `:178` and `:239` rest on something else entirely: the
    adopter's instantiated charter EXISTS, and what it lacks is a DECLARED SIZE CEILING. The gov-only
    conclusion survives; the unifying sentence does not.
  - **Correction 4 — the filed guard's population is wrong, and this one matters most.** rev-1 wrote
    the predicate as "an entry whose `requires` name a default-set member is itself default-reachable"
    and claimed one member. Resolved live, SIX entries have a `requires` naming a default-set member —
    `check-microformats`, `codebase-map`, `drift-audit`, `memory-recall`, `playbook-render`,
    `unattended` — and FOUR of those sit outside the default set. Read literally the guard demands
    `drift-audit`, `playbook-render` and `unattended` join it; `playbook-render` declares
    `requires = ["playbook"]` exactly as this entry does and is deliberately `--all`-only. **File the
    row as "reachable by SOME selection", never "default-reachable"** — under that reading the
    violating set has exactly one member today, and under the literal one the arm somebody builds in
    three months is the wrong arm.
  - **Correction 5 — "a new gate cannot land undeclared" is true of DECLARATION only.** Arm 8 grades
    declaration completeness. REACHABILITY is arm 7b at `govkit.py:1350-1353`, whose predicate is
    `e not in derived_all and selectable != "conditional"` — the conditional mark is the explicit
    escape. A new charter-grading gate can land fully declared, reach no adopter, and red nothing.
    That is the gap that let this entry sit unreachable for its entire life while `matrix.py:48`
    hand-named it in `SCRATCH_KITS`. It belongs in the filed row.
  - **Missing option, added at rev-2 — gate the conditional mark's REASON instead of its `requires`
    edge.** `why_conditional` is free text that NOTHING reads: it appears in three descriptors, in no
    code path and in no gate. The two entries that OMIT it are `check-line-length` and
    `check-microformats` — the latter being precisely the one whose justification just failed
    measurement. `registry.toml` already applies this exact discipline to the other escape hatch: arm
    8 reds an `[[exempt]]` row with an empty reason, "an omission wearing a label"
    (`govkit.py:1913-1915`). A one-arm selfcheck addition requiring a non-empty `why_conditional` on
    every `selectable = "conditional"` entry is cheaper than the `requires`-edge arm, has an
    immediately observable failing case (two violators today, so the charter §7 stage-the-break rule
    is satisfiable on the spot), and never touches the `requires` edge — so it cannot collide with F2
    or with `DEPL-aHoistedPass-1`. It is the guard that would have caught THIS defect at the moment
    the mark was written, by forcing its argument into a field somebody could grade. **Owner rules
    which of the two guards is filed, or both.**
  - The filing precedent is unchanged and holds verbatim: `TOOL-aPacedTurnstile-1` §8 fork B declined
    the identical shape ("add the runner to the default selection, add a selfcheck arm ... or rely on
    the wiring leg"), producing `TOOL-aPacedTurnstile-11` at `memory/backlog/TOOL.md:179`, still OPEN.
- **F2 — should the deployer INFER the selection instead, so a conditional entry is pulled in when
  everything it `requires` is selected?** *Recommendation: reject; keep `requires` an ORDERING edge
  and keep selection a declaration.* **The recommendation stands and the question is in fact already
  owner-ruled**, which rev-1 failed to say. Three supporting statements need correcting.
  - **The ruling rev-1 did not cite.**
    `memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md` records
    **D4 (owner, 2026-09-04, "CORRECTED AND RE-DECIDED THE SAME DAY")**: the owner was told the
    earlier framing was FALSE, that `resolve_selection` "never expands a selection at any of its four
    call sites", and chose the edge plus install-time validation plus a gate-time announcement.
    `DEPL-aHoistedPass-1` §3 states the consequence flatly: "the owner ruled refuse, not expand." F2
    is therefore a request to REVISIT a standing ruling, not an open design question, and arguing it
    from "a specced sibling points the other way" is the weaker of the two available fact bases.
  - **Correction 1 — the count.** "It would fire for a second entry" understates the rule's reach. An
    absent or empty `requires` is satisfied vacuously: `check-install-prefix` and `check-placeholders`
    declare `requires = []`, `check-line-length` declares no `requires` key at all. Measured, the rule
    as worded fires for FOUR of the five conditional entries over the default selection and for ALL
    FIVE over `--all`. It does not add one entry; it DELETES the conditional class. Note also that
    `agent-cap` is not in the default set, so the harm rev-1 names arises only under `--all` or an
    explicit selection.
  - **Correction 2 — the tense.** rev-1 says the rejection preserves `requires` as "an ORDERING and a
    REFUSAL edge". At this base it is ORDERING ONLY. `requires` is read at exactly one place,
    `govkit.py:504` inside `derive_install_order`, filtered `if d in want` so an out-of-selection edge
    is dropped before it constrains anything, and the only `Refusal` that function raises is a cycle.
    The refusal half is `DEPL-aHoistedPass-1`'s specced arm B and does not exist yet. Written in the
    present tense it invites the owner to believe a control is already in place that is not.
  - **Correction 3 — "two rules reading the same edge in opposite directions" is loose.** Arm B fires
    when the dependency is ABSENT; inference would fire when it is PRESENT. The triggers are disjoint,
    so the two rules are logically compatible and could coexist. What actually forbids inference is
    D4, not a logical conflict.
  - **The kill rev-1 does not make.** Simulate the post-S1/S2 registry: `all_kits` becomes 21, the
    default becomes 7, and the inference rule's entire remaining population is
    `check-agent-cap-restatement` over `--all` — the one case rev-1 itself calls harmful. Once S1
    lands, the general rule has zero beneficiaries and exactly one victim. `check-agent-cap-restatement`'s
    `why_conditional` (`kit.toml:8`, "writes governance prose of its own") is confirmed verbatim, and
    the harm is worse than rev-1 states: `check-agent-cap-restatement.sh:119` enumerates the target's
    whole tracked markdown, and its descriptor seeds the waiver registry EMPTY on purpose, so an
    inferred install into a target that also took `playbook` would RED that target's bar on install
    day rather than sit inert. That last step is reasoned from source, not observed — the entry is
    absent from `matrix.py`'s `SCRATCH_KITS`, so no shape runs it in a scratch adopter.
  - **Missing option, added at rev-2 — OPT-IN inference.** Let an entry DECLARE itself inferable (a
    new descriptor key, or a third `selectable` value) and expand only on that declaration.
    Mechanically real: `selectable` is consumed at exactly two places, `govkit.py:483` and `:1351`,
    both as `!= "conditional"` with no closed value set, and no descriptor key schema exists that
    would reject a new key. It escapes BOTH of rev-1's reasons — `check-agent-cap-restatement` simply
    would not carry the declaration, and an explicit key is not the `requires` edge
    `DEPL-aHoistedPass-1` governs. **§3's ban on `implied_by` is therefore currently justified by an
    argument that does not reach the shape §3 names.** It still loses, on COST rather than on
    argument: a descriptor key, a `resolve_selection` branch, a selfcheck arm (without one a
    mis-spelled key is invisible, the exact class `DEPL-aHoistedPass-1` §3 already files) and selftest
    arms, to serve a population of ONE that the one-token edit at `registry.toml:36` already serves.
    **Owner says explicitly whether this is filed or dropped, rather than leaving it silently out.**
- **F3 — now that the gate reaches adopters, should the rendered charter name it?**
  `TOOL-aHonedRuleset-2` §4 deliberately left its connective path-free and routed this question here.
  *Recommendation: no.* **The recommendation stands, but THREE of rev-1's four supporting claims are
  false at source and are struck below.** The two facts that actually earn the ruling were mis-cited
  or unstated, and are supplied here.
  - **The rule that settles it is §16, not §7.** `coding-governance-agents.template.md:354`, inside
    §16 (§16 opens at `:347`; §7 spans `:165-:223`), reads: "the expected set is whatever the gate
    manifest defines, READ at emission time, never a list typed into this document or into a
    project's charter." That is a direct prohibition on the thing this fork asks about, and it is
    stronger than rev-1's paraphrase ("routes a session to the leg manifest"). A single leg name is
    the degenerate case of the list it bans. `TOOL-aHonedRuleset-2` §8 F3 carries the same wrong
    section number and should be corrected there too.
  - **The binding number is the CEILING, not the high-water.** `tools/template-size-highwater.txt`'s
    48378 and 60930 are ADVISORY: `check-template-size.sh` emits `TEMPLATE-SIZE WARN` and never
    changes the exit code, and both records are already exceeded. The HARD fail is
    `tools/template-size-limits.txt:27` (49152) and `:54` (64512). Measured with the gate's own
    LF-normalized rule: the template is 49144, **8 bytes free**; `AGENTS.md` is 64481, 31 free (6 at
    this spec's base). Any charter sentence naming the gate reds the bar today. That is dispositive
    on its own and rev-1 did not use it.
  - **STRUCK — "dangling pointer".** False. `render_playbook.py:387-389` drops every `kit:` fence
    whose name the target's `deploy.toml` `kits` omits, and `remove_fenced` (`:228-247`) deletes the
    body AND the markers. `check-microformats` is a registry entry id, so `check_fences` (`:204`)
    accepts `<!-- kit:check-microformats -->` as legal. The template already carries five such fences
    and the rendered `AGENTS.md` shows none surviving. A fenced mention dangles nowhere.
  - **STRUCK — "an answer from every adopter".** False. Only `class = "asked"` refuses on an absent
    answer (`render_playbook.py:420-426`); `derived` runs a probe (`:400-419`) and `defaulted` takes a
    declared default (`:427-433`). `LEXICON_CONF` at `tools/govkit/entries/playbook.kit.toml:111-116`
    is already exactly this shape — a `derived` placeholder living inside a conditional kit block —
    and ships today.
  - **STRUCK — "for the same dangling pointer".** False. Substitution runs strictly AFTER fence
    removal (`render_playbook.py:389` then `:394`), so a placeholder inside a dropped fence is never
    found, never resolved and never emitted. Placeholders are conditional the way kit blocks are.
  - **Missing option, added at rev-2 — a FENCED sentence with NO placeholder.** Two fence lines plus
    one sentence in the template. It costs no descriptor key, no adopter answer and produces no
    dangling pointer, which is to say it defeats every argument rev-1 actually made; rev-1 named the
    placeholder variant, dismissed it on two false grounds, and never named the cheaper one at all.
    **It still loses, on the two facts above.** The markers alone are ~65 bytes carried by the SOURCE
    template for every target whether or not anyone selects the entry, against 8 bytes of headroom.
    §16:354 forbids the sentence in words. And gov's own `.governance/deploy.toml:18-22` does not
    list `check-microformats`, so a fenced block would drop out of gov's own `AGENTS.md` until that
    array is edited — a fourth file in a unit whose §3 promises three.
  - The option already taken is S3: `WIRE-INTO-PROJECT.md` carries the mention, and the charter does
    not need to be the carrier.
- **F4 — do S3's bytes earn their place in an uncapped document?** `WIRE-INTO-PROJECT.md` is the
  subject of `TOOL-aScouredKit-23` (`memory/backlog/TOOL.md:302`, OPEN, cited exactly as recorded —
  though its own figure of 59833 B is now 68069 B, which strengthens its concern). Neither that row
  nor `TOOL-dSpentCeiling-4` is answered here. *Recommendation: keep S3.* **It stands, but the
  sentence rev-1 hung it on is FALSE and the load-bearing reason was missing.**
  - **STRUCK — "the only way an operator learns the entry exists is reading `registry.toml`".** After
    S1, four surfaces name it and none of them is the registry: `govkit plan` prints
    `selection: …` on its first line (`govkit.py:2625`); `plan` prints the payload rows
    `write  [engine       ] tools/check-microformats.sh`; `intake` WRITES the id into the target's own
    committed `.governance/deploy.toml` `kits` list (`govkit.py:8158`), the file govkit's own help
    calls the standing authorization; and the entry's two `[[gate_leg]]` rows land in the target's own
    `tools/gate-legs.json`. The operator is told four times, in files they own.
  - **What actually earns S3 — and it is stronger than what was struck.** `--kits` REPLACES the
    default set (§4, added at rev-2), and `WIRE-INTO-PROJECT.md:82` is a `--kits` command. An operator
    following the runbook's own documented charter-install path bypasses S1 entirely, so **the id at
    line 82 is not documentation of S1; it is what makes S1 reach the runbook's reader.** Without it
    this unit ships a default-set change the runbook's copy-paste command silently excludes.
  - **Consequence for S3's two halves, which are not one atom.** Measured on a copy: the id is 19
    bytes and the sentence ~193, 212 on disk in total, 0.31% of the document, and the carried-prefix
    occurrence count does not move either way (AC6 holds; §4's constraint on the wording is real and
    correctly stated — staging a sentence that spells `tools/check-microformats.sh` was observed to
    red the gate with `ROSE  WIRE-INTO-PROJECT.md 47 -> 48`, and the printed remedy excludes
    `--write-ratchet` for a ROSE verdict). **The ID is mandatory** for the reason above. **The
    SENTENCE, 91% of the cost, now rests on a consistency argument** — an unglossed id in a
    copy-paste list is the first thing an operator trims, and every other selectable kit in §2 gets a
    sentence — **not on the defect-closing one rev-1 claimed. Owner rules the sentence knowing that.**
  - **Correction — `TOOL-dSpentCeiling-4` is cited at the wrong population.** That row
    (`memory/backlog/TOOL.md:245`) is about RENDERED kit docs spending an adopter's read budget,
    measured over `memory/guides/BUILD-METHOD.md` and `memory/guides/UNATTENDED-PROTOCOL.md`.
    `WIRE-INTO-PROJECT.md` is neither rendered from a kit template nor inside govkit's declared
    shipping surface (`registry.toml`'s `[surface]` globs are `tools/*`, `.githooks/**`,
    `skills/session-kickoff/**` and the root template), so S3's bytes land in no adopter's read budget
    at all. The row is still correctly left unanswered; it simply does not contain this file.
  - **Correction — the byte figure is node-local.** 69030 is the CRLF on-disk size on node `a`; the
    committed blob is 68069 (961 CR bytes, no `eol=lf` row). The file is byte-identical at this
    spec's base and at HEAD.
  - **Missing option, added at rev-2 — ANCHOR it.** The runbook's own machine-readable convention for
    "this deployable exists" is `<!-- govkit:entry <id> -->`, present 7 times, and
    `tools/govkit/check_runbook_parity.py` asserts that population in both directions with a
    non-empty-body liveness half. Run today it exits 1 with 18 problems, one of them by name:
    `runbook-parity: registry entry 'check-microformats' has no anchored runbook section`. S3 as
    specced adds prose that this repo's own convention cannot see. An anchor is ~40 bytes and the
    sentence S3 already budgets can be its body, so it closes the machine gap for ~40 bytes more.
  - **Missing option, added at rev-2 — DECLARE IT EXEMPT.** `check_runbook_parity.py:41-49` reads a
    `[[runbook_exempt]]` table from `registry.toml`, requiring a non-empty `why` and refusing a row
    naming a dead entry. That is this repo's first-class way of answering "does this entry need
    runbook bytes?" with NO, at zero runbook bytes and with the reason recorded where a future reader
    finds it. Zero rows exist today — the table is defined and unused.
  - **Flagged, explicitly NOT in this unit's scope.** `check_runbook_parity.py` is tracked, sits in no
    row of `tools/gate-legs.json`, is invoked by nothing, and is RED. An unwired red gate on exactly
    the question this fork asks is the green-by-absence shape the charter §7 exists to prevent, and it
    wants its own backlog row rather than a scope expansion here.

## 9. Revision log

- rev-2 · 2026-09-04 · fork-verification pass, one verifier per §8 fork, every correction re-checked
  against source before it was written in. **All four forks stay OPEN and unsigned; every
  recommendation survives, and none is ratified here.** Struck as false at source: F1's
  "`check-placeholders` and `check-line-length` are entries that ship", its "four declaration files",
  its single unifying exemption reason and its one-member guard predicate; F2's "a second entry" and
  its present-tense "REFUSAL edge"; F3's dangling-pointer, adopter-answer and same-pointer claims and
  its `§7` citation; F4's "the only way an operator learns the entry exists". Added: the `--kits`
  REPLACES fact in §4, which is what actually makes S3's id load-bearing rather than merely
  informative; four options rev-1 omitted (a `why_conditional` reason gate, opt-in inference, a fenced
  charter sentence, and the `govkit:entry` anchor plus its `[[runbook_exempt]]` counterpart); the D4
  owner ruling F2 argues around without citing; and one out-of-scope flag, that
  `tools/govkit/check_runbook_parity.py` is unwired and red. No scope item changed.
- rev-1 · 2026-09-04 · initial draft. Written after the owner's `TOOL-aHonedRuleset-2` §8 F3 ruling of
  2026-09-04 to close the adopter gap rather than accept it, and separated from unit 2 per BUILD-METHOD
  M2. The design pass corrected that ruling's premise: the gate already ships and already runs in a
  scratch adopter, so the unit is a selection fix and not a payload build.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "ship the charter micro-format gate to an adopter through
the deployer registry selection"` names the seam this unit extends directly: `registry.toml [govkit]`,
the declaration that owns which entries an install reaches. Two adjacent affordance seams came back
with it and both were read rather than assumed — `check-template-size.sh [playbook]` and
`check-dead-paths.sh [install-prefix]`, which are the exemption side of the same registry and are what
§8 F1's class answer rests on. No function seam fits, and that is the correct answer here: the
extension point is a data row in `tools/govkit/registry.toml` plus a key in
`tools/govkit/entries/check-microformats.kit.toml`, and this unit writes no code. The corpus probe
supplied the governing precedent, `TOOL-aPacedTurnstile-1` §8 fork B — "add the runner to the default
selection, add a selfcheck arm ... or rely on the wiring leg", resolved as the default-selection line
with the arm filed as its own govkit unit — which is the shape §8 F1 follows and the source of the
two-sided acceptance criterion AC1 uses.

Recall terms used: `python tools/memory-recall/query.py "why is the micro-format gate a conditional
govkit entry rather than part of the adopter default selection" --terms "govkit registry selection
default conditional entry adopter payload charter micro-format gate leg playbook install-prefix
carried"`
