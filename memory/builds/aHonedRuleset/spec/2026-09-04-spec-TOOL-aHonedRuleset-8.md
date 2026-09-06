# TOOL-aHonedRuleset-8 — the micro-format gate reaches the adopter who takes the charter

**Status:** SPECCED · rev-9 · 2026-09-06 · node a · Tier-2 · base 94958534 · streams deployer · order 4 · ratified 2026-09-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round2.md) | spec-audit | — |
| [2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round3.md](../reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round3.md) | spec-audit | — |
| [2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit.md](../reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit.md) | spec-audit | — |

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
- **S3 — the runbook names the entry, ANCHORED, PLACED and WIRED.** Three edits to
  `WIRE-INTO-PROJECT.md`, resolved by §8 F4 in favour of the anchored form rev-2 recommended against.
  First, the `intake --kits` example an operator copies gains `check-microformats` in its id list.
  Second, the mention is carried under a `<!-- govkit:entry check-microformats -->` anchor, which is
  this repo's own machine-readable convention for "this deployable exists" and the key
  `tools/govkit/check_runbook_parity.py` joins on. One sentence sits under the anchor as its body,
  saying the gate arrives with the charter and grades its definition block. **The sentence names the
  ENTRY ID and no file path** — see the §4 carried-prefix constraint, which makes that a correctness
  requirement rather than a style choice.

  **PLACEMENT is pinned against the EXISTING anchors, never against the `--kits` line.** The new
  anchor goes at the END of the `playbook` section, immediately ABOVE
  `<!-- govkit:entry memory-tree -->`. `check_runbook_parity.py:71-81` derives a section body as
  every line from one anchor to the NEXT, and the runbook's anchors sit at `:55 :73 :150 :215 :299
  :357 :497`; the `--kits` example is mid-`playbook` between `:73` and `:150`, so an anchor beside it
  would RE-PARENT roughly sixty lines — the `adopt-playbook.sh` invocations, the
  `<!-- governance-template: vN.N -->` note and the whole *What the renderer cannot decide for you*
  list — into `check-microformats`, leaving the `playbook` body as the intake command alone. Both
  bodies stay non-empty, the census still reads 8, and rev-5's AC11 could not see any of it. rev-5
  priced only the end-of-file swallow and its own *beside the command* instruction steered into the
  one placement that breaks a neighbour.

  **Third, the WIRING step.** The anchored body also carries a wire-this-leg-into-your-gate-runner-
  and-CI instruction, because a leg nobody wires is a leg nobody runs, and §4's *What the runbook path
  actually yields* states what the §2 path does and does not leave behind.

  **It DIVERGES from the sibling sections' form, deliberately, and rev-6 claimed the opposite.** Every
  sibling wiring step spells a literal `tools/` command — `bash tools/memory-tree/check-memory-hygiene.sh`,
  `python tools/drift-audit/selftest.py`, `python3 tools/memory-recall/selftest.py`,
  `bash tools/check-wiring.test.sh` — and not one names a govkit entry id. So "exactly as the sibling
  sections name theirs" was false at all six lines rev-6 cited, and following it literally writes
  `bash tools/check-microformats.sh`, which the epoch-2 carried-prefix predicate counts as a loose file
  directly under `tools/` that exists in the tree, taking `WIRE-INTO-PROJECT.md` from 47 to 48 in
  `tools/install-prefix-carried.txt` — a `ROSE` verdict `--write-ratchet` cannot absorb, and a straight
  AC6 failure. The two halves of that sentence could not both be satisfied.

  **The path-free form this unit uses instead — ONE spelling is REQUIRED, not two offered.** The
  instruction spells the `{prefix}`-token argv the descriptor itself declares at
  `check-microformats.kit.toml:44`, `bash {prefix}/check-microformats.sh <playbook>`. The leg NAME
  `tools/gate-legs.json` gives it, `micro-format definitions`, may be named IN ADDITION and never
  instead. **rev-7 offered the two with an `and/or` and that made two of its own folds
  unsatisfiable**: `gate-legs.json:34` carries no `check-microformats` substring while the argv does,
  `grep -c` counts LINES, so a builder taking the first option lands all three S3 edits and returns
  **3** against AC9's threshold of 4 — reddening the criterion by following the scope item exactly.
  Both are path-free by construction and neither trips the ban. The divergence from the siblings is stated in the
  runbook sentence itself, so a later editor does not "fix" it back into a literal path.
- **S4 — the `why_conditional` REASON gate**, the first of the two guards §8 F1 rules must be BUILT
  here. One arm in `selfcheck()` at `tools/govkit/govkit.py`, failing any `selectable =
  "conditional"` entry whose `why_conditional` is absent or blank. Its second half is forced by its
  first: `tools/govkit/entries/check-line-length.kit.toml` gains a `why_conditional`, because with
  S2 landed that descriptor is the arm's one remaining violator and the arm would otherwise red the
  bar on its own landing commit. The value is not new prose — that descriptor's header at lines 6 to
  10 already carries the argument, and the field lifts it into a place a machine can grade.
- **S6 — the refusal-join pin ledger records the two new branches.** A ledger comment in
  `tools/govkit/refusal_join.py` names both, with AC16's selftest arms as what reaches them, and
  AC18 observes it.

  **The convention, stated WHOLE at rev-7 — rev-6 stated the half it kept and invoked the file's
  authority for it.** Read at `refusal_join.py:42-118`, every ledger row in that file's history is an
  `X -> Y` PIN RAISE: 216→217, 215→216, 214→215, 212→214, 210→212, 208→210, 197→208, 190→197, 185→190,
  180→185, 161→180, 141→161, 135→141. The convention is name the branches, state armed or unarmed,
  AND raise the pin. The `141 -> 161` row (`TOOL-dUnstalledConvoy-26`) is the precedent that says why:
  it calls a trailing floor "the state this file's own convention forbids: a floor that trails the
  population stops catching the matcher going blind", and raises to the live count for that reason.
  S6 writes the first row in that file's history that names branches WITHOUT moving the pin, and
  saying so is the point of this paragraph.

  **This unit DECLINES the raise, on a recorded reason that is not its own.**
  `memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md` — SPECCED, same `deployer`
  stream — makes "Moving `BRANCH_PIN` or `FILE_PIN`" a §3 non-goal at `:47` and gives the reason at
  `:179-184`: a `217 → 219` move "would write a ledger entry claiming two new branches took the pin to
  the population, when the population is 246". Re-baselining is its own act with its own reason and
  that sibling files it as its own row. So the trailing floor is a KNOWN DEFERRAL with an owner, not
  an acceptable property, and the ledger comment says which row owns it.

  **The count is a DELTA, never the absolute.** `BRANCH_PIN` is 217 and the live population measured
  for this rev is 244; S4 and S5 add **+2**. The absolute after landing depends on which of the two
  units lands first, because `DEPL-aHoistedPass-1`'s AC9 at `:262-263` already claims "exactly two
  higher than the 244 measured at this base" for ITS OWN two branches in the same file. Two SPECCED
  units each writing 246 means whichever lands second lands with a false figure in its own spec and a
  ledger comment wrong on the day it is written. Stating the delta and deriving the absolute at
  landing is what makes both correct. This spec cites `DEPL-aHoistedPass-1` six times and rev-6 still
  missed its `BRANCH_PIN` non-goal seven lines above a section it quoted, which is the same
  recall-failure the rev-6 H4 fold corrected for `TOOL-dScaffoldedMirror-15`.

  **What makes the +2 true, and it is a constraint on S4 and S5 rather than on S6.** `_is_refusal` at
  `refusal_join.py:135-138` matches `<obj>.fail(...)` ONLY as a bare `ast.Expr` statement, so each arm
  must be written as a bare `r.fail(...)` expression directly in `selfcheck()`. An arm written as an
  assignment, a ternary or a comprehension contributes ZERO and the ledger comment is false the day it
  lands. **rev-7 also wrote "or routed through a helper" and that half is FALSE**, corrected at rev-8:
  `enumerate_branches` at `:146-153` walks EVERY `FunctionDef`, so a bare call in a module-level helper
  still counts once — what the subtree walk causes is DOUBLE-counting for a NESTED def, not zero for a
  sibling one. `selfcheck()` has no nested defs today, so that shape appears only if the builder
  introduces one. The constraint AC18's exact-+2 actually rests on is the `ast.Expr` shape, and that is
  the one stated positively above.
- **S5 — the reachability arm on the `requires` edge**, the second guard §8 F1 rules must be BUILT.
  One arm in `selfcheck()` beside S4's, failing any entry whose `requires` names a member of the
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
  narrower than it looks, and §8 F2 now closes the gap rather than leaving it open**: the opt-in
  variant F2 raises escapes every argument written against `implied_by`, so the ban does not reach it
  and never did. F2 rejects that variant on its own terms — a new public surface M3's veto 2 discards,
  serving a population of zero — which is what makes the ban safe to carry as a scope line instead of
  an open question. Nothing in this unit turned on the answer in any case: S1 and S2 land identically
  either way.
- **The two guards this unit BUILDS assert, they do not expand.** S4 and S5 are `r.fail` arms in
  `selfcheck()`. They read declarations and grade them; neither adds a member to any selection,
  writes a descriptor key, or touches `resolve_selection`. That distinction is what keeps S5 clear of
  F2 and of `DEPL-aHoistedPass-1`.
- **The other four conditional entries keep their CLASSIFICATION.** `check-agent-cap-restatement`,
  `check-install-prefix`, `check-line-length` and `check-placeholders` all stay
  `selectable = "conditional"` and none is re-examined on the merits. S4 adds a `why_conditional`
  value to one of them; that is a field a machine can now grade, not a change to what the entry is.
- **No `last-audit` re-stamp.** Verified against the `watch:` list at `memory/guides/SESSION-KICKOFF.md:6`:
  none of this unit's SEVEN files is on it — re-verified at rev-7 over the widened set, since the
  rev-6 wording asserted a six-path check while S6 had already made it seven. The two added by the F1
  ruling (`tools/govkit/govkit.py`, `tools/govkit/selftest.py`) are not on it, and neither is S6's
  `tools/govkit/refusal_join.py`. Units 2 through 6 of
  this build all bundle that re-stamp and this one must not, or it stamps a line no staged path
  obliged. AC8 re-observes this against the widened file set rather than carrying rev-2's reading.
- **`TOOL-aScouredKit-23` and `TOOL-dSpentCeiling-4` are cited, not answered.** The first owns whether
  `WIRE-INTO-PROJECT.md` gets a ceiling; the second owns whether a kit may spend an adopter's read
  budget. S3 adds bytes to an uncapped document and §8 F4 prices that, without ruling on either row.
- **TWO defects in the runbook's own install path are measured here and repaired by neither this unit
  nor any other.** Added at rev-7, in §3 where it belongs — rev-6 wrote this bullet at the END of §4
  while three documents said §3 carried it, which is the one copy of that error that escaped the spec.
  Both are stated in §4's *What the runbook path actually yields*, filed together as
  `TOOL-aHonedRuleset-15`, and observed by AC17.
  **(a) No fenced command block in the runbook invokes `govkit.py apply`** — narrowed at rev-8 from a
  universal that did not reproduce. `update` IS run, at `:602` inside `## 5b`, whose documented
  sequence is intake → adopt → adopt --write → update and which is the path that lands bytes;
  `cmd_update` at `govkit.py:5722` emits no `gate legs:` line at all. §2 — the section an operator
  following the charter install copies — runs neither verb. **And §2's three lines do not run as
  written**: `grep -c -- '--answer' WIRE-INTO-PROJECT.md` is **0**, so the copy-paste line REFUSES
  before writing anything, which is a third defect in the same install path and is why this bullet
  says three and not two. With answers supplied the descriptor lands and the payload is still absent
  until `apply`. (The rev-7 evidence for this bullet was `grep -n apply`, which returns **TEN** hits
  and not the eight rev-7 counted — `:309 :373 :589 :635 :638 :843 :847 :876 :878 :883`, the two extra
  being `git apply --check` prose on the contribute path — and which does not test the `update` half at
  all. The narrowed claim above is what the fenced blocks at `:81-85` and `:598-603` actually show.)
  **(b) `run-gates` is absent from the `--kits` example**, and it is the sole `[gate_runner_seed]`
  declarer, so whenever an operator does reach `apply`, the legs are ORDERED and not emitted — for
  every kit that example lists, not only this one.
  **(c) The `--answer` requirement is documented nowhere in the runbook**, which is what makes (a)'s
  §2 line refuse. Repairing any of the three would rewrite an install flow every kit shares, which is
  answering somebody else's question from inside a selection fix.

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

### What the runbook path actually yields, and why S3 needs a third edit

**Added at rev-6 as a BLOCKER fold and REWRITTEN at rev-7, because rev-6 traced the right mechanism
on the wrong command.** The paragraph above says S3's id "closes" the runbook gap. It does not, and
what it leaves is measured here rather than assumed.

**FIRST, and this is what rev-6 got wrong: the runbook's fresh path never runs `apply` or `update`.**
`grep -n apply WIRE-INTO-PROJECT.md` returns `:309 :373 :589 :635 :638 :876 :878 :883` and every one
is PROSE — there is no `govkit.py apply` command block anywhere in the document. (Ten, not the eight
rev-7 wrote: `:843` and `:847` are `git apply --check` prose on the contribute path. And that grep
tests only one of the two verbs rev-7's §3 quantified over — `update` IS run, at `:602` inside `## 5b`,
whose sequence is intake → adopt → adopt --write → update and whose `cmd_update` at `govkit.py:5722`
emits no `gate legs:` line at all. §3 carries the narrowed claim.) §2's install is exactly three
lines: one `intake --kits …` and two `adopt-playbook.sh` calls — **and as written they do not run**:
`grep -c -- '--answer' WIRE-INTO-PROJECT.md` is 0, `needed_answers` returns `['playbook_path']` for
that selection, and `cmd_intake` refuses at `govkit.py:8139-8145` before writing anything. So the
literal §2 outcome is no descriptor at all; with the answer supplied it is a descriptor and no
engine. `cmd_intake` writes
`.governance/deploy.toml` and RETURNS (`govkit.py:8225-8229`); it copies nothing and emits nothing,
and `adopt-playbook.sh` renders the charter region and copies nothing else, which §4's own
*Alternatives rejected* bullet already recorded. Every per-kit section installs by hand with `cp -r`.
Only §5b at `:589` asserts `apply` IS the fresh path, and no numbered section runs it. **So the §2
outcome today is a `deploy.toml` naming the entry with no engine in the tree at all** — not a leg
that fails to run, but a script that was never copied.

**SECOND, the gate-runner gap, which is real and survives the correction.** A selection reaching
`apply` gets its legs EMITTED only when it carries an entry declaring `[gate_runner_seed]`, a key
declared in exactly ONE file (`tools/run-gates/kit.toml:105`) and read at `govkit.py:8171-8176`.
Neither `run-gates` nor `gate_runner` appears anywhere in `WIRE-INTO-PROJECT.md`. And `cmd_intake`
REFUSES to overwrite an existing `deploy.toml` — that file is the standing authorization — so the
`--kits` list an operator copies from §2 is that target's PERMANENT selection. Whenever they do reach
`apply`, by §5b's path or their own, they get the ordered-not-emitted branch at
`govkit.py:5064-5107`, the legs written to `.governance/outbox/gate-legs.md`, the line
`gate legs: ORDERED, not emitted` (`:5066` and `:5104`), and **exit 0**. Reaching `apply` is on them:
§5b's documented path ends at `update`, which emits no such line, so neither of those outcomes comes
from following the runbook. The deployer's own comment at
`:8165` calls that branch "the silent-green direction this deployer refuses by name everywhere else".

**The disposition, and its bound.** S3 gains a wiring instruction, because a leg nobody wires is a
leg nobody runs — but it is written for an operator whose engine IS in the tree, and it does not
pretend the §2 path put it there. Neither runbook defect is repaired here: fixing (a) rewrites the
install flow every kit in that section shares, and fixing (b) edits a `--kits` example that omits the
runner for all of them. Both are filed as `TOOL-aHonedRuleset-15`, §3 carries the boundary as a
non-goal, and AC17 OBSERVES which of three outcomes a scratch install actually produces — emitted,
ordered, or payload absent — so this unit ships knowing the answer instead of asserting one. Recording
a third admissible outcome is the point: rev-6 admitted only the two an `apply` run can produce, which
made its own criterion grade a command the builder would have had to invent.

The DEFAULT adopter is unaffected by all of this and the distinction is worth keeping: `run-gates` IS
in the default selection (`registry.toml:36`), so a default install does get emitted legs, exactly as
§5's perf bullet says. The runbook adopter is the one who does not, and the runbook adopter is S3's
entire audience.

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

The seam is copied, not invented. `selfcheck()`'s arm 8 already applies exactly this discipline to
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

The seam is `selfcheck()`'s arm 7b, which already grades reachability and already carries the
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
between them. SEVEN files, one atom — six at rev-6, and S6's ledger comment in
`tools/govkit/refusal_join.py` is the seventh, which rev-6 added as a scope item and left out of
every count in this document.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/govkit/registry.toml` | S1 — one id added to `[selection] default` at line 36 |
| `tools/govkit/entries/check-microformats.kit.toml` | S2 — line 14 deleted, header paragraph at lines 6 to 8 rewritten |
| `WIRE-INTO-PROJECT.md` | S3 — THREE edits: the id in the `--kits` example, the anchor placed above `memory-tree`'s, and a body carrying one sentence plus the path-free wiring instruction |
| `tools/govkit/govkit.py` | S4 + S5 — two arms in `selfcheck()` at `:976`, beside arms 7b and 8 |
| `tools/govkit/entries/check-line-length.kit.toml` | S4 second half — a `why_conditional` value, lifted from the descriptor's own header |
| `tools/govkit/selftest.py` | S4 + S5 — the arms that exercise both guards' failing cases |
| `tools/govkit/refusal_join.py` | S6 — a ledger comment naming the two new branches; `BRANCH_PIN` unmoved |

Three files at rev-2, six at rev-3, seven at rev-7. The three added at rev-3 are what the F1 ruling
costs; the seventh is S6's ledger comment. §5 prices the
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
  terms (`gate-lint`). **The rev-3 reason was ALSO wrong and is replaced in turn at rev-6.** It read
  "a bullet in that list SPELLS A PATH, which is exactly what the carried-prefix ban fires on" — but
  every bullet in that list names a bare kit directory (`codebase-map/`, `drift-audit/`,
  `memory-recall/`, `agent-instructions/`, `pytest-parallel-guardrails/`, `gate-lint/`, `govkit/`,
  `lexicon/`, `unattended/`) and not one spells a `tools/` segment. The epoch-2 predicate needs a
  literal `tools/` prefix AND an extension, so a bullet in that list's own style matches neither arm —
  which is what §4 already establishes two paragraphs earlier for S3's own sentence. **The true
  reason is placement, not prefix:** the mention belongs beside the `--kits` command it changes, and
  F4's anchored form already satisfies `check_runbook_parity.py`, so the list bullet would be a second
  carrier of one fact rather than a cheaper one. Recorded this way because F3 in this same section
  sets the standard that a right answer resting on wrong facts is a right answer nobody can
  re-derive, and this bullet had now failed it twice.

## 5. Production-readiness checklist

- security — N/A, re-priced against §4's SEVEN files rather than rev-2's three: THREE declaration
  edits, one runbook edit, two `r.fail` arms plus their selftest arms, and S6's comment — a list that
  sums to the seven it claims, which the rev-7 wording did not.
  The verdict is
  unchanged and the premise is what moved — the arms READ declarations and write nothing, so there is
  still no write path, no new surface and no credential handling. The rev-3 F1 fold updated every
  other bullet in this section to six files and left this one at three, four bullets above a risks
  entry that contradicted it.
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
  reading the same commit, and there is no smaller thing to revert — §4's Rollout establishes the seven
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
  arms, so neither adds a `raise Refusal` branch — but both ARE counted by `refusal_join.py`, whose
  second channel is the bare `.fail(...)` call, so the population grows BY TWO and only the
  shrink-only pin keeps the leg green; §7 states the corrected mechanism and S6 records the growth, and
  S6 is also why this reads as a delta and not as an absolute. Both are
  Python, so `tools/memory-tree/check-arms.py` does not see them either — its `discover()` at line 127
  reads tracked `.sh` files only, verified rather than assumed.
- migration / rollback — `git revert` of one commit restores all seven files, and reverts both halves
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
  `the default selection previews exactly 5 SIDE|rendered rows` is `ok`. **FIVE, not the four rev-8
  wrote, and the arm was RENAMED to match at rev-9.** Both figures are TREE-STATE snapshots and the
  arm's own comment says so — *the count is a MEASUREMENT of this tree and moves when the tree does*
  — so S1 putting one more entry in the default selection moves them by construction: measured live,
  `SIDE|rendered` goes 4 to 5 and `ORDER|project-owned` in the sibling arm goes 4 to 5, each by
  exactly the one entry. The counts were left at four by every rev of this spec, which would have
  reds this unit's own landing on two arms that are working correctly. Naming the arm by its post-
  landing spelling is what keeps this criterion checkable; the comment beside it records the cause.
- **AC6** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and prints
  `carried-prefix clean`, and `git diff 94958534..HEAD -- tools/install-prefix-carried.txt` is empty
  — so S3's sentence raised no file's recorded count, and `WIRE-INTO-PROJECT.md` still stands at 47.
- **AC7** — When `git diff 94958534..HEAD -- coding-governance-agents.template.md AGENTS.md` runs
  after the commit, it is empty, proving this unit moved no charter byte and left
  `TOOL-aHonedRuleset-2`'s subject alone.
- **AC8** — When every change is staged and `bash skills/session-kickoff/manifest-check.sh --staged`
  runs, it exits 0 with `git diff --cached -- memory/guides/SESSION-KICKOFF.md` empty — proving no
  watched pathspec was touched and no `last-audit` re-stamp was owed or taken.

  **The revision is load-bearing in all three, and rev-5 omitted it in all three.** A bare
  `git diff -- <path>` compares WORKING TREE to INDEX, so it is empty for every path once the change
  is staged or committed; AC8 stages first and then asserted its own tautology. That is not academic
  here: measured live with the gate's own LF-normalised rule, `coding-governance-agents.template.md`
  stands at 49144 B against its 49152 ceiling — **8 free bytes** — and `AGENTS.md` at 64481 against
  64512, **31 free**. AC7 is the only thing between that headroom and an accidental charter edit, and
  as written it could not fail. The one partial mitigation, recorded so the correction is not
  overstated: the charter template IS on the manifest `watch:` list, so `manifest-check.sh` check 5
  would have caught a staged template edit with no re-stamp. `AGENTS.md` is only in `verify-paths`
  and nothing guarded it at all.
- **AC9** — Three observations over the two files S2 and S3 touch.
  **(i)** `grep -c 'selectable = "conditional"' tools/govkit/entries/check-microformats.kit.toml`
  returns 0 with comments included — a WHOLE-FILE grep at rev-8, where the rev-7 form was anchored
  `^selectable` and a descriptor whose header still argued for the mark it no longer carries shipped
  green. **(ii)** A POSITIVE grep asserts the rewritten header names the default selection, so S2's
  second half is observed present and not only its first half observed absent — S2 was the last scope
  item with an unobserved half. **(iii)** `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns
  at least **4** against the 0 measured at base — the `--kits` id, the anchor, the body sentence and
  the WIRING instruction, which S3 now REQUIRES in its `{prefix}`-argv form and which therefore
  carries the substring. **The threshold is derived from S3's edit count and moves with it**: rev-6
  added S3's third edit and left this criterion enumerating rev-5's two, so omitting the wiring step —
  B1's entire remedy — returned 3 and passed; and rev-7 raised the threshold while independently
  making the wiring spelling optional, so the two folds graded each other into an unsatisfiable pair.
  rev-8 closes it in S3 rather than here, and (iii) states which of S3's forms it is written against.
- **AC11** — When `python tools/govkit/check_runbook_parity.py` runs, **NO `runbook-parity:` line
  names `check-microformats` at all** — not merely the `has no anchored runbook section` line — its
  problem count falls from 18 to 17, and its census line reports `8 anchored section(s)` against the
  7 measured at base. **And the anchor SEQUENCE is
  `… playbook, check-microformats, memory-tree …`**, observed by `grep -n 'govkit:entry'` and comparing
  the order, with the `playbook` body's `What the renderer cannot decide for you` grep kept as the
  corroborating half. The checker still
  exits 1 on the other 17 problems, which this unit does not touch and §8 F4 flags separately — so
  the observation is the named lines' absence, never the exit code.

  **Both strengthenings answer criteria that could not fail.** rev-5 asserted one line's absence plus
  a census of 8; an anchor landing with an EMPTY body removes that line, raises the census, adds a
  distinct `EMPTY body` problem and passes the criterion word for word — while §8 F4 itself calls the
  non-empty body "the half that makes the anchor mean anything". The no-line-names-it form covers
  presence, uniqueness and non-empty body in one observation. The sequence clause is what observes S3's
  PLACEMENT, and at rev-7 it observes the RULE rather than one instance of breaking it. An anchor
  beside the `--kits` line re-parents ~60 lines of the `playbook` section into this one; but an anchor
  dropped anywhere AFTER `memory-tree` — end of file, mid-`drift-audit`, mid-`push-main` — leaves the
  renderer list exactly where it is, keeps both bodies non-empty, takes problems 18 to 17 and the
  census to 8, and passed every clause rev-6 wrote while re-parenting a DIFFERENT section's tail. The
  checker grades emptiness only (`check_runbook_parity.py:71-81`) and its anchor regex at `:35` imposes
  no position, so nothing else covers order; and since that checker is in no `tools/gate-legs.json`
  row, AC10's bar cannot see it either. Grading the instance rev-6 happened to find, rather than the
  class S3's rule forbids, is the shape charter §7 names by hand.
- **AC17** — The runbook path's outcome is OBSERVED rather than assumed, over the exact command
  sequence, named because rev-6 said "the runbook's own command" and the runbook's own §2 command is
  `intake` alone. Two runs against a scratch target: **(1)** `govkit.py intake --target <scratch>
  --kits playbook,playbook-render,check-microformats` — exactly §2's line with this unit's id added —
  then observe whether `tools/check-microformats.sh` exists in that tree; **(2)** `govkit.py apply
  --target <scratch>`, the verb §5b names as the fresh path and no numbered section runs, then observe
  which of the two lines it prints.

  **THREE admissible outcomes, and the third is the one rev-6 could not report**: the legs are
  EMITTED into the target's gate runner; or `gate legs: ORDERED, not emitted` with them written to
  `.governance/outbox/gate-legs.md`; or the PAYLOAD IS ABSENT, which is what run (1) alone yields.
  Whichever is observed is what §4's *What the runbook path actually yields* must say, and this
  criterion is what keeps the two in agreement. Admitting only the outcomes an `apply` run can produce
  made rev-6's criterion grade a command the builder had to invent, and asserting the outcome the unit
  hopes for would reproduce the defect it exists to remove.

  **AND RUN (1) NEEDS `--answer`, which rev-7 omitted and the round-3 audit EXECUTED.** Spelled as
  rev-7 wrote it, `intake` exits **2** with *the selected kits need answer(s) playbook_path and none
  was supplied* and writes no `.governance/` at all — `needed_answers` returns `['playbook_path']` for
  this selection and `cmd_intake` refuses at `govkit.py:8139-8145` before writing anything — so run (2)
  then exits 2 with *no target descriptor* and NONE of the three outcomes was reachable. The criterion
  added so the outcome would be observed named a command that refuses, which is the defect it was
  folded in to remove, reproduced by the fold. **Run (1) is therefore whatever `needed_answers`
  returns for the selection, supplied as `--answer key=value`** — today that is
  `--answer playbook_path=<file>`, and the general form is written rather than the literal one because
  a future kit's new token would silently re-break a literal. Verified working end to end by the
  audit: with the answer supplied `intake` exits 0, `tools/check-microformats.sh` is ABSENT from the
  target (outcome three, observable at last), and `apply` then exits 0 printing
  `gate legs: ORDERED, not emitted` (outcome two).
- **AC18 — S6 is observed, and rev-6 was the only scope item with no criterion at all.** After the
  commit, `python tools/govkit/refusal_join.py` exits 0 and reports a branch count **exactly two
  higher** than the count measured immediately BEFORE the commit — a delta, taken at landing, for the
  reason S6 gives — `BRANCH_PIN` is unmoved at 217, and the ledger comment names both new branches
  with their armed/unarmed status and the row that owns the deferred raise. Modelled on
  `DEPL-aHoistedPass-1` AC9, which already carries this observation over the same file. **No gate
  substitutes**: §7 states the pin is shrink-only and 27 behind, so it cannot detect growth at all,
  and AC10's bar runs the leg only to confirm it still exits 0.
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
  **This is the leg both new guards belong to.** S4 and S5 are arms inside `selfcheck()`, so they
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
- `govkit refusal join` — guarded on `tools/govkit/`. **Corrected at rev-6: the rev-5 negative here
  was stamped "verified" on a FALSE mechanism, and this is the correction.** `_is_refusal` matches
  TWO channels, and its own docstring at `:130` says so: `raise Refusal(...)` at `:131-134`, and a
  bare `<obj>.fail(...)` expression statement at `:135-138`. rev-5 cited `:133` — the raise half —
  and stopped four lines short of the half that counts its own arms. `r.fail` sites are the MAJORITY
  of the population, not outside it: measured live `refusal-join: 244 branch(es) across 4 module(s)`,
  exit 0, against `BRANCH_PIN = 217` at `:41`. **S4 and S5 add TWO branches, which is GROWTH; the
  absolute is derived at landing, because `DEPL-aHoistedPass-1` adds two of its own to the same file
  (S6).** rev-7 rewrote S6 to forbid the absolute and left `246` standing here and in §5 — the two
  sections a builder reads immediately before writing the ledger comment S6 exists to keep true.
  Nothing reds, but for a different reason than rev-5 recorded: the pin is shrink-only and already 27 behind,
  so it cannot detect growth at all. S6 is the written record that a shrink-only floor structurally
  cannot be. Two further consequences, budgeted here rather than discovered later: the join half at
  `:175-181` reports both new branches as reached by NO arm the moment a reached-set is passed, and
  the anchor is `(module, function, ordinal-within-function)`, so inserting arms mid-`selfcheck()`
  renumbers every later branch in it should a reached-set ever be committed. A negative stated with a
  false mechanism and stamped "verified" is the false-confidence class charter §7 names by hand, and
  it would have taught the next reader that `r.fail` sites license skipping arms.
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

**ALL FOUR ARE NOW RESOLVED, and the last of them was resolved by a run rather than by the owner.**
Both machine readers grade §8 as ONE whitespace-squeezed string and neither grades per item — the gap
`memory/TEMPLATE-SPEC.md` pins in its own §8 guidance — so while F2 stood open this section already
read RESOLVED to a machine and the status header was the only honest signal. F2's mark below names
its resolver and its authority; the header now carries `ratified` and the two signals agree for the
first time. **The header's `ratified` token therefore does not mean the owner ratified all four** —
three are the owner's and one is delegated, and each mark says which.

- **F1 — is this one script's problem, or does the playbook adopter have no general answer for gov
  scripts that gate the charter's own claims?** **RESOLVED (owner, 2026-09-04): BUILD BOTH GUARDS, IN
  THIS UNIT** — the `why_conditional` reason gate AND the reachability arm on the `requires` edge,
  both as arms in the govkit selfcheck surface. They are S4 and S5.
  - **This overrules the spec's own recommendation, which is left standing below rather than
    rewritten.** *Recommendation was: treat it as the instance it is, land S1 to S3, and FILE the
    regression guard rather than build it.* It is preserved verbatim because a recommendation quietly
    edited to agree with the ruling teaches a later reader that the two never differed, and the
    disagreement here is the useful part of the record.
  - **It also overrides a precedent, deliberately — and rev-6 corrects BOTH the precedent's
    authority and its ground.** The source mark reads `RESOLVED (agent, 2026-08-18, delegated)` at
    `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md:360-364`, quoted
    with its full `(actor, date, authority)` triple because a paraphrase drops exactly the field that
    decides how much authority an override needs. rev-3 framed this as the owner overruling an
    earlier OWNER ruling, which is a harder override than the one that actually happened. And the
    ground the source rested on was M3 **veto 2** — "adding the arm inside this spec would change
    another kit's contract mid-unit, which M3 veto 2 reaches as a governance carrier change" — which
    rev-3 dropped in favour of the backlog row's paraphrase. That matters here specifically: veto 2 is
    an OWNER TURN, and **the owner's 2026-09-04 F1 ruling IS that turn**, which is what clears it for
    a govkit contract assertion inside this unit. F2 one fork later invokes the same veto to DISCARD
    the opt-in build, and the two dispositions are consistent for exactly this reason — F1 has an
    owner turn clearing it and F2 has none. `TOOL-aPacedTurnstile-1` §8 fork B declined a govkit
    contract assertion inside a unit for this identical shape — "add the runner to the default
    selection, add a selfcheck arm ... or rely on the wiring leg", shipping the default-selection
    line and deferring the arm, on the reasoning that "adding the arm there would change govkit's
    contract inside a unit that only moves the runner". That produced `TOOL-aPacedTurnstile-11`
    (`memory/backlog/TOOL.md`, OPEN), which is still unbuilt today and still unbuilt. The precedent is
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
    `matrix.py:63` pins its install-day verdict as `NOT ADOPTED — no declaration at`; rev-6 cited
    `:66`, which is a blank line, and the pin was wrong when written rather than drifted), and
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
    (`govkit.py:1916-1917`; the loop is `:1910-1917`). A one-arm selfcheck addition requiring a non-empty `why_conditional` on
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
  everything it `requires` is selected?** **RESOLVED (agent, 2026-09-06, delegated): NO — reject
  inference in both its automatic and its opt-in forms, which is the direction this spec's own
  recommendation already carried.** The owner RE-OPENED this fork on 2026-09-04, declining to close it
  against their own prior ruling and asking specifically that the OPT-IN inference variant be
  considered on its merits rather than left as a footnote. That consideration is the record below, it
  is what this mark ratifies, and the alternative stays stated as the live option it was rather than
  being demoted back to a footnote.
  - **Why a run may resolve this one.** `memory/guides/BUILD-METHOD.md` M3 ratifies the most
    feature-rich option that survives its three vetoes. The opt-in build is a new descriptor key or a
    third `selectable` value, a `resolve_selection` branch, a selfcheck arm and its selftest arms — a
    NEW PUBLIC SURFACE on the deployer, which veto 2 discards before any of its merits are weighed.
    Rejection trips no veto: it builds no surface, needs no dependency, widens nothing, and leaves the
    standing D4 ruling exactly where the owner put it. One survivor, and it is also the option leaving
    fewest follow-ups open, so the tie-break never runs. **A veto is not a licence to take the vetoed
    option** — this mark declines the expansion, it does not authorize it, and the park rule does not
    fire because the survivor is not the vetoed one.
  - **What this mark does NOT decide.** Whether `resolve_selection` should ever expand is D4's
    question and stays the owner's. This decides only that THIS unit does not build the expansion,
    which is what the fork asked. Nothing downstream moves either way: S1 and S2 land byte-identically
    under both answers, S4 and S5 are `r.fail` assertions that never touch `resolve_selection`, and
    §3's ban stays scoped to `implied_by` exactly as rev-3 left it.
  - **The cost argument below is unchanged and is the substance of the answer.** A mechanism with no
    current member is a mechanism its first member would define, and post-S1/S2 the opt-in rule has
    zero beneficiaries and zero victims because nothing would carry the declaration. The veto is why a
    run may write the mark; the cost is why the mark reads NO.
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
    fenced block would drop out of gov's own `AGENTS.md` until that array is edited, adding one more
    file to a unit that had already grown from three to six. (rev-7: the unit is now at seven on its
    own account, so the marginal-file argument is weaker than rev-3 wrote it — the ruling stands on
    the CEILING, which is the ground F3 says it stands on, and this clause is colour rather than
    load-bearing.)
  - The option taken is S3: `WIRE-INTO-PROJECT.md` carries the mention, and the charter does not need
    to be the carrier. §3's "the charter does not name the gate" holds, and AC7 observes it.
- **F4 — do S3's bytes earn their place in an uncapped document?** `WIRE-INTO-PROJECT.md` is the
  subject of `TOOL-aScouredKit-23` (`memory/backlog/TOOL.md`, OPEN, cited by id because that shard is
  edited in place and a line pin into it is stale by construction —
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
  - **The real byte cost against what was budgeted, RE-PRICED at rev-7 over all three edits.** The
    `--kits` id is 19 bytes (`,check-microformats`) and the sentence ~193, which is the 212 rev-2
    measured. The anchor line is **40 bytes**, 41 with its newline and 42 with a blank line separating
    it. **The wiring instruction is the edit this bullet was never shown**: it arrived at rev-6 as
    B1's remedy, and the sibling blocks it is modelled on measure 287 B at `:262-266` and 473 B at
    `:351-355`, so a comparable step is **~300 B** and the true S3 cost is roughly **550 B**, not 254.
    Against `WIRE-INTO-PROJECT.md`'s live 68747 B that is about **0.80% of the document**, against
    0.31% for the rev-2 scope and the 0.37% this bullet claimed. **The ANCHORING ruling does not flip**,
    and that is stated rather than assumed: the 254-versus-212 comparison is anchored against
    unanchored, and the wiring step sits on BOTH sides of it, so it cancels. What is understated is
    `TOOL-aScouredKit-23`'s uncapped-growth concern, by about the same factor — which F4 declines to
    answer while citing its figure, and which is now cited at the right magnitude. That is the whole price of closing a machine gap this repo's own convention already
    declares. **rev-8 strikes "the cheapest of the three options F4 considered", which its own next
    clause refutes**: of the three it is the only one that
    CLOSES the machine gap, and it is the more expensive of the two that put bytes in the runbook. The
    `[[runbook_exempt]]` alternative costs zero runbook bytes precisely BECAUSE it answers the question
    NO, and the unanchored form costs 212 and leaves the checker still naming this entry.
  - **The consistency argument the sentence now also rests on**, stated so the ruling is not read as
    resting on it alone: an unglossed id in a copy-paste list is the first thing an operator trims,
    and every other selectable kit in §2 gets a sentence. Under the anchored form this stops being
    the sentence's ONLY justification — the liveness half of `check_runbook_parity.py` requires a
    non-empty body, so the sentence is now load-bearing for the anchor rather than optional beside
    the id.
  - **Correction — `TOOL-dSpentCeiling-4` is cited at the wrong population.** That row
    (`memory/backlog/TOOL.md`, by id) is about RENDERED kit docs spending an adopter's read budget,
    measured over `memory/guides/BUILD-METHOD.md` and `memory/guides/UNATTENDED-PROTOCOL.md`.
    `WIRE-INTO-PROJECT.md` is neither rendered from a kit template nor inside govkit's declared
    shipping surface (`registry.toml`'s `[surface]` globs are `tools/*`, `.githooks/**`,
    `skills/session-kickoff/**` and the root template), so S3's bytes land in no adopter's read budget
    at all. The row is still correctly left unanswered; it simply does not contain this file.
  - **Correction — the byte figure is node-local, and the byte-IDENTITY claim was false.** 69030 was
    the CRLF on-disk size on node `a` when rev-3 measured; the committed blob at this spec's base
    `94958534` is `0d217e3d`, 68069 B. **rev-5 asserted the file is byte-identical at base and at
    HEAD; it is not.** At HEAD the blob is `22383488`, 68747 B — 11 lines added by `36af6f9f`
    (`TOOL-aTunedCompass-6`, 2026-09-05 12:33), during this spec's own life and 48 minutes after
    rev-3 landed. F4's own restatement of `TOOL-aScouredKit-23`'s figure as 68069 is likewise now
    68747. Nothing in the ruling flips — re-measured at rev-6, the anchor census is still 7, the
    `--kits` example line is unmoved, `tools/install-prefix-carried.txt` still records 47, and
    `bash tools/check-install-prefix.sh` is green at `118 recorded file(s), 5 hand-justified, none
    rising` — so AC6 and AC11 hold as written. What was wrong was an asserted identity in the bullet
    whose whole job is to tell a builder the figures need no re-check, pinned against the MOVING ref
    `HEAD`, which charter §14 bans outright.
  - **The option TAKEN, raised at rev-2 as a missing one.** The anchor convention is present 7 times
    in the runbook today, for `kickoff-manifest`, `playbook`, `memory-tree`, `drift-audit`,
    `codebase-map`, `memory-recall` and `push-main` — cited by ENTRY ID at rev-6, because rev-3's line
    pins `:346` and `:486` for the last two are already 11 lines stale after `36af6f9f`. So S3 joins an
    established pattern rather than inventing one. **Placement is NOT merely a build-time detail and
    rev-5's rule for it was wrong**: the checker reads a section's body as every line from the anchor
    to the NEXT anchor, and "immediately above its own sentence" puts the anchor mid-`playbook`, where
    it re-parents that section's body into this one. The rule is now stated in S3's own placement
    paragraph and pinned against the EXISTING anchors — immediately above `memory-tree`'s — and AC11
    observes it. Rev-5 priced only the end-of-file swallow, which is the failure mode that is easy to
    see.
  - **The option REJECTED — DECLARE IT EXEMPT.** `check_runbook_parity.py:41-49` reads a
    `[[runbook_exempt]]` table from `registry.toml`, requiring a non-empty `why` and refusing a row
    naming a dead entry. That is this repo's first-class way of answering "does this entry need
    runbook bytes?" with NO, at zero runbook bytes and with the reason recorded where a future reader
    finds it. Zero rows exist today — the table is defined and unused. It loses for the reason the
    `--kits` fact establishes above: an exemption would be a written claim that the runbook's reader
    does not need this id, and the runbook's own install command is precisely the path that fails
    without it. Exempting the one entry whose absence breaks the documented flow would be the
    exemption-is-not-coverage shape charter §7 names.
  - **Flagged, explicitly NOT in this unit's scope — and it already HAS rows, which rev-5 did not
    cite.** `check_runbook_parity.py` is tracked, sits in no row of `tools/gate-legs.json`, is invoked
    by nothing, and is RED. An unwired red gate on exactly the question this fork asks is the
    green-by-absence shape the charter §7 exists to prevent. **What it does NOT want is a fresh row.**
    `TOOL-dScaffoldedMirror-15` (DEFERRED, verified 2026-08-24) records this checker exiting 1 with
    the same 18 problems, zero callers and absence from the leg manifest, and carries the context that
    the unwired checker is the mechanical reason an adopter is never told a kit is deployable.
    `TOOL-dRetiredFork-28` (OPEN) records the same fact. And
    `memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-lens-unwired.md:42-44`
    explicitly DECLINED to re-report it as new *because* that row exists — a decision this fork then
    made again in ignorance of it. rev-5's run duly filed a THIRD, `TOOL-aHonedRuleset-9`, so one
    measured fact sat in three rows with three framings and none citing another. At rev-6
    `TOOL-aHonedRuleset-9` is rewritten to lead with the two prior rows and to state the only thing it
    adds — that AC11 of this unit becomes a criterion graded by nothing on the bar. The wiring question
    stays where `TOOL-dScaffoldedMirror-15` already had it.

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
  re-measured — the 40-byte anchor takes S3 from ~212 to ~254, and rev-7's wiring step to roughly
  550 B, about 0.80% of the document.
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

- rev-5 · 2026-09-06 · **F2 RESOLVED by the unattended run under its delegated resolver authority,
  and nothing else changed.** The answer is the direction rev-3's recommendation already pointed —
  reject inference in both forms — but it is now a mark rather than a recommendation, and it records
  the AUTHORITY as well as the answer. The route is `memory/guides/BUILD-METHOD.md` M3: the opt-in
  build is a new public surface on the deployer, so veto 2 discards it; rejection trips no veto and is
  the sole survivor, which is the case M3 ratifies rather than the case it parks. The mark states
  explicitly what it does not decide — D4's expand-versus-refuse question stays the owner's — because
  a delegated mark that reads like a governance ruling is the failure mode M3's two bounds exist to
  prevent. §8's preamble is rewritten from *three of four* to *all four*, and it now says the header's
  `ratified` token covers three owner marks and one delegated one rather than four owner marks. The
  header gains `ratified 2026-09-06` and the status stays SPECCED, which is now the accurate pair:
  every fork carries a conforming mark and no code has been written. No acceptance criterion, design
  section or figure moved. **One §3 bullet did move**, and it was found by the M6 bug-class checklist
  rather than by re-reading: the `implied_by` ban's justification said in its own words that F2 was
  still open over it, which is `amendment-leaves-its-other-half-standing` — the clause that only made
  sense under the old status, left behind. It now states what F2 decided and why the ban does not
  reach the opt-in shape. The ban itself is unchanged.

- rev-6 · 2026-09-06 · **round-1 spec audit folded — 2 blockers, 5 HIGH, 6 MEDIUM, 1 LOW, all
  fourteen.** Report:
  `memory/builds/aHonedRuleset/reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit.md`.
  **B1** — §4 said S3's id "closes" the runbook gap; it does not. A `--kits` selection gets legs
  EMITTED only if it carries the one `[gate_runner_seed]` entry (`tools/run-gates/kit.toml:105`), and
  `run-gates` appears nowhere in the runbook, so the operator gets `ORDERED, not emitted` and exit 0 —
  this unit's own defect one layer down, on the path §4 elevates to load-bearing. New §4 section
  states the mechanism, S3 gains the WIRING step its six sibling sections carry, §3 records that
  fixing the runbook's missing gate RUNNER is out (filed as `TOOL-aHonedRuleset-15`), and AC17
  observes which outcome an install actually produces. **B2** — S3's "anchor beside the `--kits`
  command" places it MID-`playbook`, and `check_runbook_parity.py:71-81` derives a body anchor-to-next-
  anchor, so ~60 lines including the renderer list re-parent into this entry with both bodies
  non-empty and rev-5's AC11 blind to it. Placement is now pinned above `memory-tree`'s anchor and
  AC11 grades the `playbook` body. **H1** — AC6, AC7 and AC8 all ran revisionless `git diff`, which is
  empty once staged; AC8 staged first and asserted its own tautology. Pinned to `94958534..HEAD` and
  `--cached`. This guards 8 free charter bytes and 31 in `AGENTS.md`. **H2** — AC11 could not fail on
  an EMPTY-body anchor; restated as no `runbook-parity:` line naming the entry, plus 18 to 17.
  **H3** — §7's refusal-join negative was stamped "verified" on a false mechanism: `_is_refusal`
  matches `.fail(...)` at `:135-138` as well as `raise` at `:131-134`, live 244 against a shrink-only
  pin of 217, and S4/S5 take it to 246, which is GROWTH. Both bullets rewritten, S6 added for the pin
  ledger, and the join and ordinal-renumber consequences budgeted. **H4** — F4 asked for a backlog row
  that has had one since 2026-08-24 (`TOOL-dScaffoldedMirror-15`, plus `TOOL-dRetiredFork-28`, plus a
  2026-08-30 review that declined to re-report it); rev-5's run filed a third. F4 now cites the prior
  art and `TOOL-aHonedRuleset-9` is rewritten to lead with it. **H5** — the overridden precedent's mark
  is `(agent, 2026-08-18, delegated)`, not an owner ruling, and its ground was M3 veto 2; both restored,
  with the sentence recording that the owner's F1 ruling IS the owner turn veto 2 requires — which is
  why F1 and F2 apply the same veto to opposite dispositions. **M1/M3** — §10 said the unit writes no
  code (false since the rev-3 F1 fold) and that it FOLLOWS the fork-B precedent (F1 says in bold it
  OVERRIDES it); both corrected and §4's function seams carried in. **M2** — §5's security bullet
  priced three files against §4's six. **M4** — `cmd_selfcheck` does not exist; the function is
  `selfcheck()` at `govkit.py:976`, wrong in seven places including both scope items. **M5** — the
  alternatives bullet's carried-prefix ground is false (no bullet in that list spells a `tools/`
  segment); replaced with the real one. **M6/L1** — three backlog line pins and two runbook anchor pins
  had drifted, and the byte-identical claim was false: base blob `0d217e3d` 68069 B, HEAD `22383488`
  68747 B, 11 lines added by `36af6f9f` during this spec's life. All pins now cite by id. No fork was
  re-opened and no ruling reversed.

- rev-7 · 2026-09-06 · **round-2 spec audit folded — 1 blocker, 5 HIGH, 4 MEDIUM, 2 LOW.** Report:
  `memory/builds/aHonedRuleset/reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round2.md`.
  Blockers fell 2 to 1, so the loop converged rather than stalling — and the surviving blocker was
  introduced by the rev-6 fold, not left by it. **B1 — rev-6 traced the right mechanism on the wrong
  command.** The runbook's fresh path runs no `apply` and no `update`: all eight `apply` hits in
  `WIRE-INTO-PROJECT.md` are prose, §2's install is one `intake` plus two `adopt-playbook.sh` calls,
  and `cmd_intake` writes `deploy.toml` and returns. So §2's real outcome is a descriptor naming the
  entry with NO ENGINE IN THE TREE — not a leg that fails to run. §4's paragraph is rewritten around
  that, the gate-runner gap is kept because it survives the correction, S3's wiring step is rewritten
  for an operator whose engine IS present, and AC17 now names the exact two-run command sequence and
  admits a THIRD outcome, payload absent, which rev-6 could not report. **H2 — three documents said §3
  carried the boundary and rev-6 wrote it at the end of §4**; it is now a §3 non-goal carrying BOTH
  runbook defects, and the backlog row that repeated the false pointer outside this spec is corrected
  in the same commit. **H1 — S6 made this a SEVEN-file unit and every count still read six**; the
  table gains its row and five counts move, including §3's watch-list verification, which was asserted
  over seven paths and performed over six (its conclusion holds — `refusal_join.py` is not on the
  `watch:` list). **H3 — "exactly as the sibling sections name theirs" was false at all six lines it
  cited**: four spell literal `tools/` paths and none names an entry id, and following it would write
  `bash tools/check-microformats.sh`, taking the carried-prefix count 47 to 48 and redding AC6. S3 now
  states that it DIVERGES, and names the two path-free forms it uses instead — the
  `tools/gate-legs.json` leg name and the descriptor's own `{prefix}` argv. **H4 — AC9 still
  enumerated rev-5's two edits**, so B1's own remedy could be omitted and the criterion passed at 3;
  raised to 4 with the enumeration spelled out. **H5 — `DEPL-aHoistedPass-1` already claims 244 → 246
  for a DIFFERENT pair of branches in the same file**, and this spec cites that sibling six times
  while missing its `BRANCH_PIN` non-goal seven lines above a section it quotes. S6 now states the
  count as a **delta of +2** and derives the absolute at landing, so whichever unit lands second is
  still correct. **M1 — S6 stated half the ledger convention as the whole of it**: every row in that
  file's history is a pin RAISE, and the `141 -> 161` precedent says why a trailing floor is the state
  the convention forbids. S6 states the convention whole, then declines the raise explicitly on
  `DEPL-aHoistedPass-1`'s recorded reason, so the 27-behind floor reads as a deferral with an owner.
  **M2 — S6 was the only scope item with no criterion and no gate can see it**; AC18 added, modelled on
  the sibling's AC9, with the constraint that makes its figure true: each arm must be a bare
  `r.fail(...)` expression statement written directly in `selfcheck()`, because `_is_refusal` matches
  nothing else. **M3 — AC11 graded the one wrong placement rev-6 found, not the class S3's rule
  forbids**; it now asserts the anchor SEQUENCE and keeps the renderer-list grep as corroboration.
  **M4 — F4 priced two edits of a three-edit S3**; re-priced at roughly 550 B and 0.80% of the
  document, with the note that the anchoring ruling does not flip because the wiring step sits on both
  sides of that comparison. **L1** — F4's pointer said S2's placement paragraph; it is S3's. **L2** —
  `matrix.py:66` is a blank line and the pin was wrong when written; re-pinned to `:63`. Nothing was
  re-opened, no ruling reversed, and no scope item removed.

- rev-8 · 2026-09-06 · **round-3 spec audit folded — 1 blocker, 3 HIGH, 4 MEDIUM, 4 LOW — and this
  is the LOOP'S EXIT.** Report:
  `memory/builds/aHonedRuleset/reviews/2026-09-06-review-TOOL-aHonedRuleset-8-spec-audit-round3.md`.
  Blockers went 2 → 1 → 1: not strictly smaller, so under BUILD-METHOD M4 the loop is NON-CONVERGENT
  and STOPS. B1 is DISPOSED by **FOLD** — a defect in this document, needing no mechanism this build
  lacks — and the disposition is recorded on the run's `--review` row. Nothing is promoted, parked or
  waived, and there is no round 4.
  **B1 — the criterion added so the outcome would be OBSERVED named a command that REFUSES.** The
  auditors executed it: AC17's run (1) as rev-7 spelled it exits 2 with *the selected kits need
  answer(s) playbook_path and none was supplied* and writes nothing, so run (2) exits 2 with *no target
  descriptor* and none of the three outcomes was reachable. `grep -c -- '--answer'
  WIRE-INTO-PROJECT.md` is 0, so the runbook's own §2 line refuses identically — which makes §4's and
  §3(a)'s "a `deploy.toml` naming the entry with no engine" false in the OTHER direction: there is no
  descriptor either. AC17 now takes whatever `needed_answers` returns, written as the general form
  because a future kit's token would silently re-break a literal; §4 and §3 carry the measured
  outcome; and the `--answer` gap becomes defect (c) of `TOOL-aHonedRuleset-15`. This is round 2's B1
  surviving its own fold a second time, which is what a non-convergent loop looks like from inside.
  **H1 — two rev-7 folds graded each other into an unsatisfiable pair.** The H3 fold made S3's wiring
  spelling `and/or`, and only the `{prefix}` argv carries the `check-microformats` substring; the H4
  fold independently raised AC9 to 4 counting that line. A builder taking the first option returns 3
  and reds AC9 by following the scope item exactly. S3 now REQUIRES the argv form and permits the leg
  name only as an addition. **H2 — §3(a)'s universal was false for `update`**: `:602` runs it inside
  `## 5b`, whose path is intake → adopt → adopt --write → update and whose `cmd_update` emits no
  `gate legs:` line at all, so §5b produces neither outcome §4 routed the reader to. Narrowed to what
  reproduces. **H3 — rev-7 rewrote S6 to forbid the absolute and left `246` in §5 and §7**, the two
  sections read immediately before writing the ledger comment S6 exists to keep true. Both are deltas
  now. **M1** — `grep -n apply` returns TEN hits, not eight, in four carriers. **M2** — the last two
  of the seven-file counts, one of which said SEVEN and then listed six. **M3** — S2's header rewrite
  had no criterion and AC9's `^selectable` grep was anchored, so a self-contradicting descriptor could
  ship green; AC9 gains a whole-file zero AND a positive assertion. **M4** — S6's "routed through a
  helper contributes ZERO" is false: `enumerate_branches` walks every `FunctionDef`, so a module-level
  helper counts once and the subtree walk causes DOUBLE-counting for a nested def, not zero. AC18's
  exact-+2 rests on the `ast.Expr` shape, which is now the constraint stated. **L1** — AC9's orphaned
  pre-fold enumeration deleted. **L2** — §10 misquoted and misattributed §4. **L3** — F4's "cheapest of
  the three" is refuted by its own next clause. **L4** — the `[[exempt]]` sentence is at `:1916-1917`,
  not `:1913-1915`. Three defects reached outside this spec into
  `memory/backlog/TOOL.md` and are corrected in the same commit.

- rev-9 · 2026-09-06 · **built. One acceptance criterion moved, and it was the build that found
  it.** AC5 named the selftest arm `…exactly 4 SIDE|rendered rows`; S1 adds an entry to the default
  selection, so that count and its sibling `ORDER|project-owned` each rise by one. Both are declared
  tree-state snapshots — the arm's own comment says the count moves when the tree does — so the arms
  were updated to 5 and the criterion now names the post-landing spelling. No rev of this spec caught
  it, and it would have red the unit's own landing on two arms behaving correctly.
  **Everything else landed as specced and every guard was observed RED before it was trusted.**
  S4's arm found its predicted violator on the live tree the moment it was wired — `check-line-length`,
  the entry the original defect never pointed at — and AC12 staged its break on `check-placeholders`,
  a descriptor this unit does not otherwise edit. S5's arm was proven by restoring this unit's OWN
  base state, and AC15 holds: its violating set over the live registry is empty, naming none of
  `drift-audit`, `playbook-render` or `unattended`, which is what proves the specified quantifier
  shipped rather than the literal `default-reachable` reading. AC18's delta is exact: refusal-join
  reports 246 against the 244 measured before, and `BRANCH_PIN` is unmoved at 217 with S6's ledger
  entry naming both branches and the sibling ruling that defers the raise.
  **Two build-time facts.** A literal `tools/` path in unit 5's hoisted comment raised this repo's
  carried-prefix count and red `install-prefix`; it was derived instead, and this unit's own wiring
  sentence uses the `{prefix}` argv form for the same reason. And the first selftest fixture copied
  gov without `.git`, so `selfcheck` could not walk its surface — caught by the liveness half of the
  arm, which asserts the copy is green BEFORE either break is provoked.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "ship the charter micro-format gate to an adopter through
the deployer registry selection"` names the seam this unit extends directly: `registry.toml [govkit]`,
the declaration that owns which entries an install reaches. Two adjacent affordance seams came back
with it and both were read rather than assumed — `check-template-size.sh [playbook]` and
`check-dead-paths.sh [install-prefix]`, which are the exemption side of the same registry and are what
§8 F1's class answer rests on. The DECLARATION extension point is a data row in
`tools/govkit/registry.toml` plus a key in `tools/govkit/entries/check-microformats.kit.toml`.
**And since the rev-3 F1 ruling this unit also writes CODE, which this section asserted it did not
until rev-6** — S4 and S5 are two arms in `tools/govkit/govkit.py` plus their exercising arms in
`tools/govkit/selftest.py`, which is why §4's *Files touched (estimate)* reads *three files at rev-2,
six at rev-3, seven at rev-7*.
The function seams they extend, found by hand in §4 and carried here because finding a seam is this
section's job: the `[[exempt]]` empty-reason loop at `govkit.py:1910-1917`, whose "an omission wearing
a label" sentence is spelled again at `:1575` and `:2508`, is the seam S4 copies; and arm 7b at
`:1350-1353` is the reachability seam S5 sits BESIDE rather than modifies.

The corpus probe supplied the governing precedent, `TOOL-aPacedTurnstile-1` §8 fork B — "add the
runner to the default selection, add a selfcheck arm ... or rely on the wiring leg", resolved as the
default-selection line with the arm filed as its own govkit unit. **§8 F1 OVERRIDES that shape rather
than following it**, deliberately and in bold, and rev-5 recorded it here as followed — the reading a
future session would grep this section for. The two-sided acceptance criterion AC1 uses is what
survives from the precedent and is unaffected by the override.

Recall terms used: `python tools/memory-recall/query.py "why is the micro-format gate a conditional
govkit entry rather than part of the adopter default selection" --terms "govkit registry selection
default conditional entry adopter payload charter micro-format gate leg playbook install-prefix
carried"`
