# TOOL-aHonedRuleset-8 — the micro-format gate reaches the adopter who takes the charter

**Status:** SPECCED · rev-4 · 2026-09-05 · node a · Tier-2 · base 94958534 · streams deployer · order 4

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
- **S3 — the runbook names the entry, ANCHORED.** Two edits to `WIRE-INTO-PROJECT.md`, resolved by
  §8 F4 in favour of the anchored form rev-2 recommended against. First, `WIRE-INTO-PROJECT.md:82` is
  the `intake --kits` example an operator copies; it gains `check-microformats` in the id list.
  Second, the mention is carried under a `<!-- govkit:entry check-microformats -->` anchor, which is
  this repo's own machine-readable convention for "this deployable exists" and the key
  `tools/govkit/check_runbook_parity.py` joins on. One sentence sits under the anchor as its body,
  saying the gate arrives with the charter and grades its definition block. **The sentence names the
  ENTRY ID and no file path** — see the §4 carried-prefix constraint, which makes that a correctness
  requirement rather than a style choice.
- **S4 — the `why_conditional` REASON gate**, the first of the two guards §8 F1 rules must be BUILT
  here. One arm in `cmd_selfcheck` at `tools/govkit/govkit.py`, failing any `selectable =
  "conditional"` entry whose `why_conditional` is absent or blank. Its second half is forced by its
  first: `tools/govkit/entries/check-line-length.kit.toml` gains a `why_conditional`, because with
  S2 landed that descriptor is the arm's one remaining violator and the arm would otherwise red the
  bar on its own landing commit. The value is not new prose — that descriptor's header at lines 6 to
  10 already carries the argument, and the field lifts it into a place a machine can grade.
- **S5 — the reachability arm on the `requires` edge**, the second guard §8 F1 rules must be BUILT.
  One arm in `cmd_selfcheck` beside S4's, failing any entry whose `requires` names a member of the
  declared default set while the entry itself is **reachable by no declared selection**. The
  quantifier is load-bearing and §4 establishes what it means mechanically; the literal reading
  "default-reachable" is a different and wrong arm.

## 3. Non-goals (OUT)

- **No charter byte moves.** `coding-governance-agents.template.md` and `AGENTS.md` are untouched.
  `TOOL-aHonedRuleset-2` owns the §16 grammar cut; the two units share a subject and no file, land
  independently, and neither waits on the other.
- **The charter does not name the gate.** `TOOL-aHonedRuleset-2` §4 left that question here; §8 F3
  answers it as no, and no `{{MICROFORMAT_GATE}}` placeholder is added either.
- **No new deployer machinery, in the SELECTION-EXPANDING sense.** No `implied_by`, no
  reverse-`requires`, no rule that selecting an entry drags in a conditional one that requires it.
  `resolve_selection` returns exactly what it returns today. **This bullet's justification is
  narrower than it looks and §8 F2 is still OPEN over it**: the opt-in variant F2 raises escapes
  every argument written against `implied_by`, and the owner re-opened that fork knowingly. What
  makes the ban safe to carry at this rev is that nothing in this unit turns on the answer — S1 and
  S2 land identically either way.
- **The two guards this unit BUILDS assert, they do not expand.** S4 and S5 are `r.fail` arms in
  `cmd_selfcheck`. They read declarations and grade them; neither adds a member to any selection,
  writes a descriptor key, or touches `resolve_selection`. That distinction is what keeps S5 clear of
  F2 and of `DEPL-aHoistedPass-1`.
- **The other four conditional entries keep their CLASSIFICATION.** `check-agent-cap-restatement`,
  `check-install-prefix`, `check-line-length` and `check-placeholders` all stay
  `selectable = "conditional"` and none is re-examined on the merits. S4 adds a `why_conditional`
  value to one of them; that is a field a machine can now grade, not a change to what the entry is.
- **No `last-audit` re-stamp.** Verified against the `watch:` list at `memory/guides/SESSION-KICKOFF.md:6`:
  none of this unit's SIX files is on it, and the two added by the F1 ruling
  (`tools/govkit/govkit.py`, `tools/govkit/selftest.py`) are not on it either. Units 2 through 6 of
  this build all bundle that re-stamp and this one must not, or it stamps a line no staged path
  obliged. AC8 re-observes this against the widened file set rather than carrying rev-2's reading.
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

### S4's seam — the `why_conditional` reason gate

The seam is copied, not invented. `cmd_selfcheck`'s arm 8 already applies exactly this discipline to
the registry's OTHER escape hatch: at `tools/govkit/govkit.py:1910-1917` it walks every `[[exempt]]`
row and fails one whose `why` strips to empty, with the reason "an exemption without one is an
omission wearing a label". The same sentence is spelled twice more in the file, at `:1575` for
`exempt_leg` and at `:2508` for a `[[decline]]` row, so a fourth application of it is this codebase's
established shape rather than a new idea. S4's arm is that loop with `exempts` swapped for the
conditional entries and `why` swapped for `why_conditional`.

`selectable = "conditional"` is the only escape from arm 7b's reachability predicate
(`govkit.py:1350-1353`), and it is the one escape in the registry that has never had to argue for
itself: `why_conditional` is free text read by NO code path and NO gate — `git grep` finds it in
three descriptors and nowhere else. Measured live over the 25 entries, the five conditional ones
carry three values between them; the two that omit it are `check-line-length` and
`check-microformats`, the latter being precisely the entry whose justification failed measurement in
§4 above. That is the arm's argument in one sentence: the mark whose reason nobody could grade is the
mark whose reason turned out to be wrong.

**The failing case is observable before the arm is wired**, which is what charter §7 demands, and
running the candidate predicate over the real tree did what §7 says it routinely does — it surfaced a
live instance the original symptom never reached. At this unit's base the predicate hits TWO entries.
After S2 lands, `check-microformats` leaves the population and `check-line-length` is the sole
remaining violator, so **the arm reds its own landing commit unless S4's second half lands with it**.
That is not a snag to route around; it is the guard doing its job on the first tree it ever sees, and
it is why S4 is specified as two halves rather than one.

### S5's seam — and what "reachable" has to mean

The seam is `cmd_selfcheck`'s arm 7b, which already grades reachability and already carries the
comment explaining why (`an entry cannot exist that no selection reaches — the state the unattended
kit was found in`). S5 sits beside it as the case 7b cannot see: 7b exempts a conditional entry
outright, so an entry can be declared, claimed, payload-complete, gate-emitting and reachable by
nobody, and red nothing. That is the state this entry has been in for its whole life.

**The quantifier is the whole design, and the literal one is wrong.** Write the arm as "an entry
whose `requires` names a default-set member must itself be DEFAULT-reachable" and it demands three
innocent entries join the default set. Resolved live: SIX entries have a `requires` naming a
default-set member, and FOUR of them sit outside it.

| entry | `requires` | in default set | in `all_kits()` |
|---|---|---|---|
| `check-microformats` | `["playbook"]` | no | no — conditional |
| `codebase-map` | `["memory-tree"]` | yes | yes |
| `drift-audit` | `["memory-tree"]` | no | yes |
| `memory-recall` | `["memory-tree"]` | yes | yes |
| `playbook-render` | `["playbook"]` | no | yes |
| `unattended` | `["memory-tree"]` | no | yes |

`playbook-render` declares `requires = ["playbook"]` byte-for-byte as this entry does and is
deliberately `--all`-only. An arm that reds it is an arm that reds a correct declaration, and the arm
somebody builds in three months from a literal reading is the wrong arm.

**Mechanically, "reachable by some selection" is `e ∈ default_kits(reg) ∪ all_kits(descs)`.** Those
two are the selections govkit DERIVES; the other two paths into `resolve_selection` — `--kits` and a
target's own `deploy.toml` `kits` — are operator-authored and reach any entry in the registry by
construction, so a predicate that counted them would pass vacuously for every entry and assert
nothing. Excluding them is not a simplification, it is the difference between a check and the
green-by-absence shape charter §7 exists to prevent.

Measured over the live tree, the union is 20 and equals `all_kits()` exactly, because the default set
is a strict subset of it today. The arm is still written as the union rather than as
`selectable != "conditional"`, because `resolve_selection`'s default branch does NOT filter on the
mark — §4's first rejected alternative establishes that a conditional entry may legally sit in the
default set — so the two spellings are equal today and would diverge under a registry this arm is
supposed to survive.

Under that quantifier the violating set has **exactly one member today, `check-microformats`**, and
zero members once S1 and S2 land. So S5's RED case is this unit's own base state, and its acceptance
observation is the cheapest kind there is: revert S1 and S2, watch it fail, restore.

**One antecedent was tried and rejected on measurement.** Broadening the trigger from "`requires`
names a DEFAULT-set member" to "`requires` names anything reachable by some declared selection" takes
the antecedent from 6 entries to 9 and adds a second violator, `check-agent-cap-restatement`. That is
the entry §8 F2 establishes would RED a target's bar on install day if anything pulled it in — so the
broad reading demands the exact outcome F2 spends a page arguing is harmful. The narrow antecedent is
the one specified.

### The carried-prefix constraint on S3

`tools/check-install-prefix.sh` carries a second arm, the carried-prefix BAN, whose population is the
descriptor-resolved shipped set PLUS `WIRE-INTO-PROJECT.md` as one named addition. Its predicate is
at epoch 2, which counts `tools/<kit>/<file>.<ext>` AND a loose file directly under `tools/` that
exists in the tree — and `tools/check-microformats.sh` is exactly such a loose file.
`tools/install-prefix-carried.txt:11` records `WIRE-INTO-PROJECT.md` at 47, and the arm is a ban
rather than a ratchet: `--write-ratchet` may lower a count and may not raise one.

So a runbook sentence spelling `tools/check-microformats.sh` reds the bar, and the remedy the gate
prints cannot absorb it. S3's sentence names the bare entry id, which is not a path and matches no
arm. **The anchor F4 adds is clear of the arm for the same reason** — `<!-- govkit:entry
check-microformats -->` carries no `tools/` segment at all, so it matches neither epoch-2 shape. Base
state re-measured for this rev: the gate exits 0 with `carried-prefix clean — 118 recorded file(s),
5 hand-justified, none rising`, and `tools/install-prefix-carried.txt:11` still records
`WIRE-INTO-PROJECT.md` at 47. AC6 observes that the recorded count did not move.

### Migration

None. Declaration edits and two selfcheck arms; no data shape changes and no target is re-installed
by this unit. S4's second half is a value added to an existing descriptor key, not a schema change.

### Rollout

One commit, and the F1 ruling makes that a requirement rather than a preference. `registry.toml` and
the descriptor must move together for `govkit selfcheck` to stay coherent; the runbook sentence
describes what those two lines do, so splitting it off would leave the runbook describing a selection
that does not exist yet; and S4's two halves cannot be split at all, because the arm reds the tree
between them. Six files, one atom.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/govkit/registry.toml` | S1 — one id added to `[selection] default` at line 36 |
| `tools/govkit/entries/check-microformats.kit.toml` | S2 — line 14 deleted, header paragraph at lines 6 to 8 rewritten |
| `WIRE-INTO-PROJECT.md` | S3 — the id added to the `--kits` example at line 82, plus an anchor line and one sentence as its body |
| `tools/govkit/govkit.py` | S4 + S5 — two arms in `cmd_selfcheck`, beside arms 7b and 8 |
| `tools/govkit/entries/check-line-length.kit.toml` | S4 second half — a `why_conditional` value, lifted from the descriptor's own header |
| `tools/govkit/selftest.py` | S4 + S5 — the arms that exercise both guards' failing cases |

Three files at rev-2, six at rev-3. The three added are what the F1 ruling costs, and §5 prices the
review consequence rather than only the edit count.

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
- risks — **the unit now carries two mechanisms, and that is the M2 condition that made it a separate
  unit in the first place.** Stated plainly and without relitigating: BUILD-METHOD M2 is why this work
  was split out of `TOOL-aHonedRuleset-2`, and the F1 ruling puts an ADOPTER PAYLOAD change (S1 to S3
  — which entries an install reaches, and what the runbook tells an operator) and TWO GOVKIT CONTRACT
  ASSERTIONS (S4, S5 — new arms that can red gov's own bar) inside one atom. The cost lands at review
  time and it is specific: **a closing diff cannot tell which half a finding belongs to.** A reviewer
  who reds on the reachability arm's quantifier and a reviewer who reds on the default set growing are
  reading the same commit, and there is no smaller thing to revert — §4's Rollout establishes the six
  files cannot be split, because S4's two halves red the tree between them. The concrete exposure is
  that a defect in either half forces a revert of both, which puts a proven adopter fix back in the
  drawer over a guard's wording. Accepted on the owner's ruling, recorded here so nobody re-derives it
  from a confusing diff three weeks from now. The mitigation available is small and worth taking: the
  commit message separates the two mechanisms explicitly, and the acceptance ledger answers S1-S3 and
  S4-S5 in two runs rather than one.
- risks — the default selection grows, and gov's own suite has arms keyed on the default plan. The
  one measured hazard is `tools/govkit/selftest.py:2366`, which asserts the default selection previews
  exactly four `SIDE|rendered` rows. The two added rows are `role = "engine"` under a plain `to`, so
  they classify as `write` through `KIND_MARKS` at `tools/govkit/govkit.py:1992` and not as
  `SIDE|rendered`; AC5 runs the arm rather than trusting that reading. The strict-subset arm at
  `selftest.py:2354` compares a one-kit target's writes against the default's and survives a larger
  default by construction.
- testing + left-shift gates — TWO new arms, per the F1 ruling. The left-shift for "does this gate
  work in an adopter" already exists at `tools/govkit/matrix.py`; what S1 and S2 change is the input
  to `govkit selfcheck`'s arm 7b. The residual gap rev-2 identified — nothing stops a future edit
  re-adding the conditional mark — is now CLOSED by S5 rather than filed, and S4 closes the wider one
  arm 7b could never see: a conditional mark whose stated reason nobody grades. Both are `r.fail`
  arms, so neither adds a `Refusal` branch and the `govkit refusal join` floor is unmoved; both are
  Python, so `tools/memory-tree/check-arms.py` does not see them either — its `discover()` at line 127
  reads tracked `.sh` files only, verified rather than assumed.
- migration / rollback — `git revert` of one commit restores all six files, and reverts both halves
  together for the reason §5's first risk bullet states. A target already installed is unaffected
  until it next runs `govkit update`.
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
  returns 0, and `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns at least 3 against the 0
  measured at base — the `--kits` id, the anchor and the sentence.
- **AC11** — When `python tools/govkit/check_runbook_parity.py` runs, its output no longer contains
  `registry entry 'check-microformats' has no anchored runbook section`, and its census line reports
  `8 anchored section(s)` against the 7 measured at base. The checker still exits 1 on the other 17
  problems, which this unit does not touch and §8 F4 flags separately — so the observation is the
  named line's absence, never the exit code.
- **AC12 — S4's staged break, confirmed RED before the arm is trusted.** When
  `why_conditional` is removed from `tools/govkit/entries/check-placeholders.kit.toml` and `python
  tools/govkit/govkit.py selfcheck` is run, it exits non-zero naming `check-placeholders`; when the
  line is restored and the same command re-run, it exits 0. Both halves, and the break is staged on a
  descriptor this unit does not otherwise edit so the arm is proven over the population and not over
  its own fix.
- **AC13 — S4's second half, observed as the live instance it is.** When the arm is wired and
  `tools/govkit/entries/check-line-length.kit.toml` still carries no `why_conditional`, `python
  tools/govkit/govkit.py selfcheck` exits non-zero naming `check-line-length`; when the value lands,
  it exits 0. This is the AC that records the guard finding a violator the original defect never
  pointed at.
- **AC14 — S5's staged break, which is this unit's own base state.** When S1's id is removed from
  `tools/govkit/registry.toml` and `selectable = "conditional"` is restored to
  `tools/govkit/entries/check-microformats.kit.toml`, `python tools/govkit/govkit.py selfcheck` exits
  non-zero naming `check-microformats` as required-by-a-default-member and reachable by no declared
  selection; when both are restored, it exits 0.
- **AC15 — S5 reds no innocent entry.** When the arm runs over the unmodified live registry, the
  violating set it reports is EMPTY, and specifically it names none of `drift-audit`,
  `playbook-render` or `unattended` — the three a literal `default-reachable` predicate would demand
  join the default set. Measured at base, the antecedent holds for six entries and the literal
  reading would red four of them; this AC is what proves the specified quantifier shipped instead.
- **AC16** — When `python tools/govkit/selftest.py` runs, arms named for S4 and S5 are present and
  `ok`, so both guards' failing cases are exercised by the suite rather than only by hand at
  landing time.
- **AC10** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary it is GREEN, and
  because this unit edits `tools/govkit/`, `GATE_FULL=1 GATE_SELFTESTS=1 bash
  tools/run-gates/run-gates.sh` is GREEN too — the total run a Definition of Done owes for kit work.

## 7. Gates

Leg names as `tools/gate-legs.json` spells them:

- `govkit selfcheck` — `chunk: declarations`, `subject: repo`, unguarded, so it runs on every bar.
  **This is the leg both new guards belong to.** S4 and S5 are arms inside `cmd_selfcheck`, so they
  need no manifest row of their own and inherit an unguarded leg that runs on every bar — which is
  the right home for an assertion about declarations that any commit can break. Its arm 7b is also
  the predicate whose input S1 and S2 change. Green at base, must stay green, and AC12 through AC15
  are all read off this one leg.
- `govkit selftest` — **also the home of the arms that EXERCISE S4 and S5**, per AC16, and the reason
  the leg appears twice in this list. A guard whose failing case is only ever staged by hand at
  landing is a guard nobody re-observes; the suite arms are what keep both predicates honest after
  this unit closes.
- `govkit acceptance matrix` — guarded on `tools/govkit/`, which S1 and S2 stage, so it is owed. It is
  the only leg that executes the shipped gate inside a scratch adopter, and it is therefore the real
  evidence behind AC4.
- `govkit selftest` — guarded on `tools/govkit/` and `subject: kit`, so a default bar HOLDS it. AC10
  is what runs it, and this unit is kit work, so the held run is owed rather than optional.
- `govkit refusal join` — guarded on `tools/govkit/`. It is a shrink-only branch floor over `Refusal`
  call sites, which `refusal_join.py:133` matches by ast node name. S4 and S5 are `r.fail` arms and
  raise nothing, so the floor is unmoved even though this unit now edits `govkit.py`. Verified rather
  than assumed, because "we added two arms and the branch floor did not move" is exactly the claim a
  reader should distrust.
- `harness arms (fail branches armed or pinned)` — unguarded, `subject: repo`. Named to record a
  NEGATIVE that would otherwise look like an oversight: it does not cover the new arms.
  `check-arms.py:127` builds its population from tracked `.sh` files, so `govkit.py`'s fail branches
  are outside it entirely. AC16's selftest arms are the coverage, and this leg is not.
- `install-prefix (shipped surface)` and `install-prefix self-test` — the constraint §4 states on S3's
  wording. AC6 reads the first one's carried-prefix arm.
- `micro-format definitions` — the gov-side twin of the leg this unit makes reachable in a target.
  Untouched here, green at base with `11 definition(s) graded, 11 keyword(s) derived`, and named so a
  reader is not left wondering whether the charter moved.
- `kit version markers` — the descriptor declares `version_from = { none = ... }`, so S2 owes no
  version bump. Stated rather than left as an unexplained absence.
- `playbook render wiring` — untouched, because AC7 forbids a charter edit. Named for the same reason.

**Two new gate ARMS, no new gate LEG.** §8 F1's recommendation was to file both and it was overruled;
what survives of it is the shape, which is that neither guard earns a manifest row. Both ride
`govkit selfcheck`, which already exists, already runs unguarded on every bar, and already owns the
reachability question — so the merge bar's leg count does not move and no adopter receives anything
new. `tools/govkit/check_runbook_parity.py` remains unwired and out of scope; §8 F4 flags it for its
own row rather than adopting it here.

## 8. Open questions

**THREE OF FOUR ARE RESOLVED AND F2 IS NOT. Do not read this section's marks as covering it.** Both
machine readers grade §8 as ONE whitespace-squeezed string and neither grades per item — the gap
`memory/TEMPLATE-SPEC.md` pins in its own §8 guidance — so the three conforming marks below make this
section read RESOLVED to a machine while F2 is genuinely open. That is why the header carries no
`ratified` token and why the status stays SPECCED: **the status is the only honest signal here, and
flipping it to a terminal token would let a real open fork through.**

- **F1 — is this one script's problem, or does the playbook adopter have no general answer for gov
  scripts that gate the charter's own claims?** **RESOLVED (owner, 2026-09-04): BUILD BOTH GUARDS, IN
  THIS UNIT** — the `why_conditional` reason gate AND the reachability arm on the `requires` edge,
  both as arms in the govkit selfcheck surface. They are S4 and S5.
  - **This overrules the spec's own recommendation, which is left standing below rather than
    rewritten.** *Recommendation was: treat it as the instance it is, land S1 to S3, and FILE the
    regression guard rather than build it.* It is preserved verbatim because a recommendation quietly
    edited to agree with the ruling teaches a later reader that the two never differed, and the
    disagreement here is the useful part of the record.
  - **It also overrides a precedent, deliberately.** `TOOL-aPacedTurnstile-1` §8 fork B declined a
    govkit contract assertion inside a unit for this identical shape — "add the runner to the default
    selection, add a selfcheck arm ... or rely on the wiring leg" — shipping the default-selection
    line and deferring the arm, on the reasoning that "adding the arm there would change govkit's
    contract inside a unit that only moves the runner". That produced `TOOL-aPacedTurnstile-11`
    (`memory/backlog/TOOL.md:179`), which is still OPEN today and still unbuilt. The precedent is
    therefore cited as OVERRIDDEN, not distinguished: the shapes match, the earlier ruling went the
    other way, and the owner has ruled the other way here. §5's first risk bullet prices what the
    override costs at review time, and `TOOL-aPacedTurnstile-11` is untouched by this unit — it asks
    for a different arm, keyed on the command string an entry declares.
  - The two guards are specified at S4 and S5, their seams are in §4, their staged-break observations
    are AC12 through AC15, and their leg is `govkit selfcheck` per §7.
  - What survives of rev-2's analysis, unchanged: `tools/govkit/registry.toml` IS the general
    mechanism, 25 `[[entry]]` rows and 23 `[[exempt]]` rows, asserted in both directions by selfcheck
    arm 8 (`tools/govkit/govkit.py:1896-1932`), which reds on an unclaimed tracked path, on an
    exemption naming a path that no longer exists, and on a claim that is not tracked. Measured live:
    `surface 64 tracked path(s) · 25 entr(y|ies) · 23 exemption(s) · 0 unclaimed`. Of the five
    conditional entries, only this one's stated reason fails on measurement, so the class is not
    systematically broken. **The ruling does not disturb that reading** — it accepts the class is
    sound and still wants the two assertions that would have caught the one bad member.
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
    `requires = ["playbook"]` exactly as this entry does and is deliberately `--all`-only. **Write the
    arm as "reachable by SOME selection", never "default-reachable"** — under that reading the
    violating set has exactly one member today, and under the literal one the arm is the wrong arm.
    **This correction is now BUILT rather than filed**, and it is the single most load-bearing
    sentence the ruling acted on: §4's S5 section fixes the quantifier mechanically as
    `e ∈ default_kits(reg) ∪ all_kits(descs)`, AC15 is the observation that no innocent entry reds,
    and §4 records a second measurement the ruling prompted — broadening the ANTECEDENT rather than
    the quantifier takes it from 6 entries to 9 and drags in `check-agent-cap-restatement`, the one
    entry F2 establishes is actively harmful to install.
  - **Correction 5 — "a new gate cannot land undeclared" is true of DECLARATION only.** Arm 8 grades
    declaration completeness. REACHABILITY is arm 7b at `govkit.py:1350-1353`, whose predicate is
    `e not in derived_all and selectable != "conditional"` — the conditional mark is the explicit
    escape. A new charter-grading gate can land fully declared, reach no adopter, and red nothing.
    That is the gap that let this entry sit unreachable for its entire life while `matrix.py:48`
    hand-named it in `SCRATCH_KITS`. **It is the gap S5 closes**, and it is why S5 sits BESIDE arm 7b
    rather than modifying it: 7b's conditional escape is correct for the four entries that earn it.
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
    the mark was written, by forcing its argument into a field somebody could grade. **The owner ruled
    BOTH, and both are BUILT** — this one is S4, and the ruling's instruction to copy the
    `[[exempt]]` empty-reason seam rather than invent one is followed at §4, which pins it at
    `govkit.py:1910-1917` and notes the same sentence is already spelled at `:1575` and `:2508`.
  - **The observable failing case turned out to be observable twice, and the second one is the
    finding.** Two violators at base is what rev-2 recorded. What rev-2 did not carry forward is what
    happens AFTER S2: `check-microformats` leaves the conditional population, `check-line-length`
    remains, and S4 reds its own landing commit. Hence S4's second half. That is charter §7's "run a
    candidate gate predicate over the real tree before wiring it" paying out exactly as advertised —
    a live instance the original symptom never reached.
- **F2 — should the deployer INFER the selection instead, so a conditional entry is pulled in when
  everything it `requires` is selected?** **STILL OPEN. The owner RE-OPENED this fork on 2026-09-04**,
  declining to close it against their own prior ruling and asking specifically that the OPT-IN
  inference variant be considered on its merits rather than left as a footnote. It is elevated out of
  the "missing option" position below and stated as the live alternative it is.
  - **The live alternative — an entry DECLARES itself inferable**, via a new descriptor key or a
    third `selectable` value, and the deployer expands only on that declaration. It is mechanically
    real at this base and that was verified at source rather than assumed: `selectable` is consumed at
    exactly TWO places, `govkit.py:483` (`all_kits`) and `:1351` (arm 7b), both spelled
    `!= "conditional"`, so there is no closed value set a third value would violate; and no descriptor
    key schema exists anywhere that would reject a new key, which is itself the reason a mis-spelled
    key would be invisible.
  - **The tension, stated plainly, because the owner re-opened this knowing it.** The owner ruled D4
    on 2026-09-04 in
    `memory/builds/aHoistedPass/build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md` —
    re-decided the same day, after being told the earlier framing was false — that `resolve_selection`
    REFUSES rather than expands. `DEPL-aHoistedPass-1` §3 (`:40-41`) states the consequence in one
    line: "`requires` does not pull a kit in, and this unit does not make it. Arm B refuses and names
    what to add; the owner ruled refuse, not expand." **Opt-in inference IS expansion.** Declaring it
    per-entry changes who authorizes the expansion, not whether one happens: a selection would come
    back holding an id the operator did not name, which is exactly the property D4 chose against.
    Nothing here is being smuggled past that ruling — the fork is a request to revisit it, made by
    the person who made it, and it is recorded as such.
  - **Three supporting statements from rev-1 need correcting, and two of them are the premises the
    verification pass found wrong.** They are corrected below and neither is repaired by the opt-in
    variant, since both describe the AUTOMATIC rule.
  - **The ruling rev-1 did not cite**, cited in full above. What rev-1 argued instead — "a specced
    sibling points the other way" — is the weaker of the two available fact bases, and it is the one
    that made this fork look like an open design question rather than a standing ruling under review.
    The measured fact behind D4 stands unchanged: `resolve_selection` "never expands a selection at
    any of its four call sites".
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
  - **What opt-in inference actually escapes, and what it does not.** It escapes BOTH of rev-1's
    reasons: `check-agent-cap-restatement` simply would not carry the declaration, so the harm above
    never arises; and an explicit key is not the `requires` edge `DEPL-aHoistedPass-1` governs, so
    arm B and the declaration cannot fight. **§3's ban on `implied_by` is therefore justified by an
    argument that does not reach this shape**, which is why §3 now says so instead of implying the
    ban covers it. What it does NOT escape is D4 itself, for the reason stated above: the ruling is
    about whether a selection may come back larger than what was named, and a declared expansion is
    still an expansion.
  - **Recommendation, unchanged in direction and honest about its basis: reject, on COST rather than
    on argument.** The build is a descriptor key, a `resolve_selection` branch, a selfcheck arm
    (without one a mis-spelled key is invisible — the exact class `DEPL-aHoistedPass-1` §3 already
    files) and selftest arms. The population it would serve is ONE entry, and the one-token edit at
    `registry.toml:36` already serves it. Post-S1/S2 the automatic rule's population is zero
    beneficiaries and one victim; the opt-in rule's is zero and zero, since nothing would carry the
    declaration. A mechanism with no current member is a mechanism whose first member defines it, and
    that is a decision better made when one exists.
  - **Nothing in this unit turns on the answer, and that is the reason this fork can stay open
    without blocking.** S1 and S2 land identically under every option here: the registry line and the
    descriptor edit neither depend on inference nor foreclose it, and S4 and S5 are `r.fail`
    assertions that read declarations without touching `resolve_selection`. Whatever the owner
    decides, it decides a future unit's scope, not this one's. §3's ban stays as written for the
    duration, scoped to `implied_by` and explicitly not to the opt-in shape.
- **F3 — now that the gate reaches adopters, should the rendered charter name it?**
  `TOOL-aHonedRuleset-2` §4 deliberately left its connective path-free and routed this question here.
  **RESOLVED (owner, 2026-09-04): NO — and the ruling rests on the HARD CEILING, not on the advisory
  high-water and not on any of the reasoning rev-1 offered.** The recommendation was `no` and the
  answer is `no`, but the argument underneath it is replaced rather than endorsed: rev-1's supporting
  claims were three-quarters false at source, and a right answer resting on wrong facts is a right
  answer nobody can re-derive.
  - **The dispositive reason — there is no room.** The binding number is the ceiling in
    `tools/template-size-limits.txt`, whose rows are `coding-governance-agents.template.md 49152`
    (`:27`) and `AGENTS.md 64512` (`:54`). Measured for this rev with the gate's own LF-normalized
    rule (`tr -d '\r' | wc -c`, `check-template-size.sh:101`): the template is **49144 bytes, 8
    free**; `AGENTS.md` is **64481, 31 free**. A sentence naming the gate does not fit in either
    carrier, so **any charter sentence naming the gate reds the bar today.** That settles the fork on
    its own, before any question of whether the sentence would be desirable.
  - **The high-water is NOT the binding number**, and rev-1 leaned on it. `tools/template-size-highwater.txt`
    records 48378 and 60930; both are already exceeded by the measurements above, and
    `check-template-size.sh:183` emits `TEMPLATE-SIZE WARN — … Advisory only` without touching the
    exit code. A record that is already exceeded and cannot fail is not a reason for anything.
  - **The second reason is charter §16, not §7.** `coding-governance-agents.template.md:354`, inside
    §16 (§16 opens at `:347`; §7 spans `:165-:223`), reads: "the expected set is whatever the gate
    manifest defines, READ at emission time, never a list typed into this document or into a
    project's charter." That is a direct prohibition on the thing this fork asks about, and it is
    stronger than rev-1's paraphrase ("routes a session to the leg manifest"). A single leg name is
    the degenerate case of the list it bans. (`TOOL-aHonedRuleset-2` carried the same miscitation,
    in its §4 connective block rather than its §8, and it was corrected there at that spec's rev-6.)
  - **DELETED — "a decliner gets a dangling pointer".** False, and struck rather than softened.
    `render_playbook.py:388-389` drops every `kit:` fence whose name the target's `deploy.toml`
    `kits` omits, and `remove_fenced` (`:228-247`) deletes the body AND the markers — its own comment
    says a surviving block loses its markers and a dropped one loses its body too. `check-microformats`
    is a registry entry id, so `check_fences` (`:204-207`) accepts `<!-- kit:check-microformats -->`
    as legal. Fences strip cleanly in both directions and a fenced mention dangles nowhere.
  - **DELETED — "a placeholder costs an answer from every adopter".** False. Only `class = "asked"`
    refuses on an absent answer (`render_playbook.py:420-426`); `derived` runs a probe (`:400-419`)
    and falls back to a supplied answer, and `defaulted` takes a declared default (`:427-433`).
    `LEXICON_CONF` at `tools/govkit/entries/playbook.kit.toml:111-116` is already exactly this shape —
    a `derived` placeholder living inside a conditional kit block — and ships today.
  - **DELETED — "fence removal runs after placeholder resolution".** False, and backwards.
    `remove_fenced` is called at `:389`; the placeholder loop begins at `:394`. Substitution runs
    strictly AFTER fence removal, so a placeholder inside a dropped fence is never found, never
    resolved and never emitted. Placeholders are conditional the way kit blocks are.
  - **The third option the spec never had — a FENCED sentence with NO placeholder.** Two fence lines
    plus one sentence in the template, and nothing else: no descriptor key, no `[[placeholder]]` row,
    no adopter answer, no probe. It is strictly cheaper than the placeholder variant rev-1 argued
    against, and it defeats every argument rev-1 actually made — which is precisely why naming it
    matters, since rev-1 dismissed the expensive variant on false grounds and never noticed the cheap
    one existed. **It still loses, on the ceiling.** The two marker lines alone are ~65 bytes carried
    by the SOURCE template for every target whether or not anyone selects the entry, against 8 bytes
    of headroom — so the option is refused by arithmetic before §16:354 refuses the sentence in
    words. And gov's own `.governance/deploy.toml:18-22` does not list `check-microformats`, so a
    fenced block would drop out of gov's own `AGENTS.md` until that array is edited, adding a seventh
    file to a unit that already grew from three to six.
  - The option taken is S3: `WIRE-INTO-PROJECT.md` carries the mention, and the charter does not need
    to be the carrier. §3's "the charter does not name the gate" holds, and AC7 observes it.
- **F4 — do S3's bytes earn their place in an uncapped document?** `WIRE-INTO-PROJECT.md` is the
  subject of `TOOL-aScouredKit-23` (`memory/backlog/TOOL.md:302`, OPEN, cited exactly as recorded —
  though its own figure of 59833 B is now 68069 B, which strengthens its concern). Neither that row
  nor `TOOL-dSpentCeiling-4` is answered here. **RESOLVED (owner, 2026-09-04): keep S3 and ANCHOR IT,
  using the runbook's own `<!-- govkit:entry <id> -->` convention.** The spec recommended an
  unanchored id plus sentence; the owner took the anchored form, and S3 is rewritten to it.
  - **The convention and its checker, verified at source.** The marker is
    `<!-- govkit:entry <id> -->`, matched by `check_runbook_parity.py:35` as
    `<!--\s*govkit:entry\s+([a-z0-9-]+)\s*-->`. The population is asserted in BOTH directions: every
    registry entry needs an anchored section (`:66-67`), and every anchor must name a registry entry
    (`:68-69`). A third half is LIVENESS rather than presence — the body under an anchor, read to the
    next anchor, must be non-empty (`:71-81`), on the checker's own reasoning that an empty section
    "satisfies a presence check and is worse than an absent one, because it reads as covered". So the
    sentence S3 already budgets is not decoration under the anchored form; it is the half that makes
    the anchor mean anything.
  - **This scope item's observable failing case, which is the checker's ACTUAL current output.** Run
    at this rev, `python tools/govkit/check_runbook_parity.py` exits 1 with `18 problem(s)` over
    `7 anchored section(s) · 25 registry entr(y|ies) · 0 exempt`, and **it already names this entry**:
    `runbook-parity: registry entry 'check-microformats' has no anchored runbook section`. The gate
    that would grade S3 is already saying S3-as-rev-2-specced is not enough. AC11 is the observation
    that this named line goes away and the census reaches 8 anchored sections; it deliberately does
    NOT assert exit 0, because the other 17 problems are outside this unit.
  - **CORRECTED — "the only way an operator learns the entry exists is reading `registry.toml`" is
    FALSE.** After S1, four surfaces name it and none of them is the registry: `govkit plan` prints
    `selection: …` on its first line (`govkit.py:2625`); `plan` prints the payload rows
    `write  [engine       ] tools/check-microformats.sh`; `intake` WRITES the id into the target's own
    committed `.governance/deploy.toml` `kits` list (`govkit.py:8158`), the file govkit's own help
    calls the standing authorization; and the entry's two `[[gate_leg]]` rows land in the target's own
    `tools/gate-legs.json`. The operator is told four times, in files they own. S3 does not exist to
    tell them a fifth.
  - **What actually earns S3 — and it is stronger than what it replaces.** `--kits` REPLACES the
    default set; it does not add to it. Verified at source in `resolve_selection`: the `mode == "kits"`
    branch (`govkit.py:559-568`) returns `derive_install_order(sorted(kits), descs)` and consults
    neither `default_kits(reg)` nor the target's `deploy.toml` — the default branch that would read
    them sits below and is never reached. `cmd_intake` compounds it by calling the resolver with no
    `deploy` argument at all (`:8131`). And `WIRE-INTO-PROJECT.md:82` — the runbook's own documented
    charter-install command — is a `--kits` invocation. **So an operator following the runbook
    bypasses S1 entirely, and the id at line 82 is not documentation of S1; it is what makes S1 reach
    the runbook's reader.** Without it this unit ships a default-set change the runbook's copy-paste
    command silently excludes.
  - **The carried-prefix constraint, re-measured for this rev.** `tools/install-prefix-carried.txt:11`
    still records `WIRE-INTO-PROJECT.md` at 47, and the gate is green at base:
    `carried-prefix clean — 118 recorded file(s), 5 hand-justified, none rising`, exit 0. The
    constraint is real and rev-2 stated it correctly — staging a sentence spelling
    `tools/check-microformats.sh` was observed to red the gate with
    `ROSE  WIRE-INTO-PROJECT.md 47 -> 48`, and the printed remedy excludes `--write-ratchet` for a
    ROSE verdict. **The anchored form does not change that exposure**, because
    `<!-- govkit:entry check-microformats -->` carries no `tools/` segment and matches neither
    epoch-2 shape (`check-install-prefix.sh:170-171`: `tools/<kit>/<file>.<ext>`, or a loose file
    directly under `tools/`). AC6 is the observation.
  - **The real byte cost against what was budgeted.** The `--kits` id is 19 bytes (`,check-microformats`)
    and the sentence ~193, which is the 212 rev-2 measured. The anchor line is **40 bytes**, 41 with
    its newline and 42 with a blank line separating it — so the anchored form costs ~254 rather than
    ~212, a **20% increase on a scope item that was 0.31% of the document**, taking it to roughly
    0.37%. That is the whole price of closing a machine gap this repo's own convention already
    declares, and it is the cheapest of the three options F4 considered: the `[[runbook_exempt]]`
    alternative costs zero runbook bytes but answers the question NO, and the unanchored form costs
    212 and leaves the checker still naming this entry.
  - **The consistency argument the sentence now also rests on**, stated so the ruling is not read as
    resting on it alone: an unglossed id in a copy-paste list is the first thing an operator trims,
    and every other selectable kit in §2 gets a sentence. Under the anchored form this stops being
    the sentence's ONLY justification — the liveness half of `check_runbook_parity.py` requires a
    non-empty body, so the sentence is now load-bearing for the anchor rather than optional beside
    the id.
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
  - **The option TAKEN, raised at rev-2 as a missing one.** The anchor convention is present 7 times
    in the runbook today (`:55`, `:73`, `:150`, `:215`, `:299`, `:346`, `:486`, for
    `kickoff-manifest`, `playbook`, `memory-tree`, `drift-audit`, `codebase-map`, `memory-recall` and
    `push-main`), so S3 joins an established pattern rather than inventing one. Placement matters and
    is a build-time detail worth stating once: the checker reads a section's body as every line from
    the anchor to the NEXT anchor, so S3's anchor goes immediately above its own sentence and not at
    the end of the file, where it would swallow everything after it.
  - **The option REJECTED — DECLARE IT EXEMPT.** `check_runbook_parity.py:41-49` reads a
    `[[runbook_exempt]]` table from `registry.toml`, requiring a non-empty `why` and refusing a row
    naming a dead entry. That is this repo's first-class way of answering "does this entry need
    runbook bytes?" with NO, at zero runbook bytes and with the reason recorded where a future reader
    finds it. Zero rows exist today — the table is defined and unused. It loses for the reason the
    `--kits` fact establishes above: an exemption would be a written claim that the runbook's reader
    does not need this id, and the runbook's own install command is precisely the path that fails
    without it. Exempting the one entry whose absence breaks the documented flow would be the
    exemption-is-not-coverage shape charter §7 names.
  - **Flagged, explicitly NOT in this unit's scope.** `check_runbook_parity.py` is tracked, sits in no
    row of `tools/gate-legs.json`, is invoked by nothing, and is RED. An unwired red gate on exactly
    the question this fork asks is the green-by-absence shape the charter §7 exists to prevent, and it
    wants its own backlog row rather than a scope expansion here.

## 9. Revision log

- rev-3 · 2026-09-05 · **owner rulings folded on all four forks; every figure re-verified at source
  before it was written.** Status stays SPECCED and NO `ratified` token is added, because F2 is still
  open. **F1 RESOLVED — build BOTH guards in this unit**, against the spec's own recommendation
  (preserved, not rewritten) and overriding the `TOOL-aPacedTurnstile-1` §8 fork B precedent that
  declined the identical shape and produced the still-OPEN `TOOL-aPacedTurnstile-11`. Downstream:
  S4 (the `why_conditional` reason gate, copying the `[[exempt]]` empty-reason seam at
  `govkit.py:1910-1917`) and S5 (the reachability arm, quantified as
  `e ∈ default_kits(reg) ∪ all_kits(descs)`) added to §2; two §4 design sections naming both seams;
  §3's "no selfcheck arm is built" deleted and replaced by an assert-not-expand boundary; §5's
  testing bullet flipped from filed to built; AC12 through AC16 added, each a staged break; §7 names
  `govkit selfcheck` as both guards' leg and records two negatives — `govkit refusal join`'s floor is
  unmoved because `r.fail` is not a `Refusal`, and `harness arms` does not cover them because
  `check-arms.py:127` reads `.sh` files only. Measured for this rev: 6 entries have a `requires`
  naming a default-set member and 4 sit outside the default set, so the literal `default-reachable`
  predicate would red `drift-audit`, `playbook-render` and `unattended`; under the specified
  quantifier the violating set is exactly `check-microformats`, and broadening the ANTECEDENT instead
  takes it from 6 to 9 and drags in `check-agent-cap-restatement`, the entry F2 shows is harmful.
  **The guard also found a violator the defect never pointed at**: after S2, `check-line-length` is
  S4's sole remaining violator, so S4 reds its own landing commit and carries a second half. **F2 NOT
  resolved — the owner RE-OPENED it**, declining to close it against their own D4 ruling; opt-in
  inference elevated from a footnote to the live alternative, its mechanics verified (`selectable` is
  read at exactly two places, both `!= "conditional"`, no closed value set, no descriptor key
  schema), and the tension stated plainly — D4 (owner, 2026-09-04) and `DEPL-aHoistedPass-1` §3 rule
  refuse-not-expand, and declared inference is still expansion. Recommendation kept (reject, on cost),
  with the note that S1 and S2 land either way. **F3 RESOLVED — no**, rested on the HARD ceiling
  rather than the advisory high-water: measured with the gate's own LF rule the template is 49144 of
  49152 (**8 free**) and `AGENTS.md` 64481 of 64512 (31 free), so any charter sentence naming the gate
  reds the bar; second reason re-cited to §16:354, not §7. Three false claims DELETED — the dangling
  pointer (fences strip cleanly), the adopter answer (only `class = "asked"` costs one), and the
  ordering (fence removal at `:389` runs BEFORE substitution at `:394`). Third option named and
  refused: a fenced sentence with no placeholder, ~65 marker bytes against 8 of headroom. **F4
  RESOLVED — anchor it** with `<!-- govkit:entry check-microformats -->`; S3 rewritten,
  `check_runbook_parity.py` RUN and its actual output recorded (exit 1, 18 problems, 7 anchored of 25
  entries, naming this entry by name), the false "only registry.toml names it" justification replaced
  by the `--kits`-REPLACES fact verified at `govkit.py:559-568` and `:8131`, and the byte cost
  re-measured — the 40-byte anchor takes S3 from ~212 to ~254, a 20% rise on 0.31% of the document.
  Scope grew from three files to six; §5 flags the BUILD-METHOD M2 one-mechanism condition this
  creates and what it costs at review time.
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

- rev-4 · 2026-09-05 · three corrections from the ruling-application verify pass. F3 claimed
  `TOOL-aHonedRuleset-2` §8 carried the same §7-for-§16 miscitation; both halves were false — it
  was that spec's §4 connective and it was already fixed at its rev-6. F3's LF-normalisation
  citation read `check-template-size.sh:103`, a blank line; the measurement is at `:101`, and it
  sits in the paragraph this ruling rests on. The header stamped 2026-09-04 for an edit made on
  2026-09-05, against `TEMPLATE-SPEC.md`'s last-change-date rule.

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
