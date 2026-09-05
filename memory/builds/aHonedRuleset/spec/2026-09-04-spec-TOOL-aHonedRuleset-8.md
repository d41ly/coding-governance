# TOOL-aHonedRuleset-8 — the micro-format gate reaches the adopter who takes the charter

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 94958534 · streams deployer · order 4

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

`govkit selfcheck` is silent about this by design. Its arm 7b at `tools/govkit/govkit.py:1349-1353`
fails an entry "reached by no selection and is not marked conditional" — the conditional mark is
exactly the escape this entry takes, so the state is declared rather than undetected.

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
  selected.** This is the class-shaped fix and §8 F2 rejects it: the rule would fire for a second
  entry (`check-agent-cap-restatement`, whenever `agent-cap` is selected) whose descriptor's stated
  reason for being conditional is not a dependency question at all, and it points the deployer the
  opposite way from `DEPL-aHoistedPass-1`, which is SPECCED to REFUSE a selection with an unsatisfied
  `requires` rather than to complete it.
- **Ship the gate through `tools/playbook/adopt-playbook.sh` instead.** That adopter renders the
  charter region and copies nothing else; giving it a payload would create a second install path
  beside the registry for a file the registry already declares, which is the two-answers-to-one-question
  shape `registry.toml`'s own header opens with.
- **Add a runbook bullet to the "What the renderer cannot decide for you" list.** That list is about
  render-time judgement calls, and a gate is not one. The sentence goes beside the `--kits` command
  it changes.

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
  scripts that gate the charter's own claims?** The question was answered by reading, not reasoned
  about, and the answer is that the class is already handled. `tools/govkit/registry.toml` is the
  general mechanism, and every gov script in this family already carries a decided row in it:
  `check-placeholders` and `check-line-length` are entries that ship, while `check-playbook-parity.sh`,
  `check-template-size.sh` and the four declaration files those two read are `[[exempt]]` rows whose
  reasons all turn on one distinction — they grade GOV's own product, whose subject does not exist in
  an adopter tree. `govkit selfcheck` asserts that population in both directions and reds on an
  unclaimed path, so a new gate cannot land undeclared. There is no missing class answer; there is one
  entry whose selection is wrong. *Recommendation: treat it as the instance it is, land S1 to S3, and
  FILE the regression guard rather than build it.* The guard worth filing is a `selftest.py` arm
  asserting that an entry whose `requires` name a default-set member is itself default-reachable —
  that is the class predicate, it has one member today, and adding a govkit contract assertion inside
  this unit is the scope creep `TOOL-aPacedTurnstile-1` §8 fork B declined for the identical shape,
  producing `TOOL-aPacedTurnstile-11`.
- **F2 — should the deployer INFER the selection instead, so a conditional entry is pulled in when
  everything it `requires` is selected?** This is the tempting general fix and it should be rejected
  for two reasons rather than one. It would fire for `check-agent-cap-restatement` whenever `agent-cap`
  is selected, and that entry's `why_conditional` says it is for a target that "writes governance prose
  of its own" — a project property no dependency edge encodes, so the inference would install it on
  evidence it does not have. And it points the opposite way from `DEPL-aHoistedPass-1`, SPECCED at
  `order 2` on this repo's own board, whose arm B REFUSES a selection whose `requires` are unsatisfied
  instead of completing it. Two rules reading the same edge in opposite directions is worse than the
  gap either one closes. *Recommendation: reject; keep `requires` an ORDERING and a REFUSAL edge, and
  keep selection a declaration.*
- **F3 — now that the gate reaches adopters, should the rendered charter name it?**
  `TOOL-aHonedRuleset-2` §4 deliberately left its connective path-free and routed this question here.
  *Recommendation: no.* The entry is declinable by construction, so a charter naming the gate is a
  dangling pointer in every target that declines it — the exact objection unit 2 raised, and removing
  the mark does not remove it. The bytes land in two carriers this build exists to shrink, against
  `tools/template-size-highwater.txt`'s recorded 48378 and 60930, and `§7` of the charter already
  routes a session to the leg manifest for leg names. The `{{MICROFORMAT_GATE}}` placeholder variant
  costs a descriptor key and an answer from every adopter for the same dangling pointer.
- **F4 — do S3's bytes earn their place in an uncapped 69030-byte document?** `WIRE-INTO-PROJECT.md`
  is the subject of `TOOL-aScouredKit-23`, which records it as one of two instruction documents with
  no declared ceiling anywhere, and `TOOL-dSpentCeiling-4` is the adjacent row about a kit spending an
  adopter's read budget. Neither is answered here. *Recommendation: keep S3, at one id and one
  sentence.* Without it the only way an operator learns the entry exists is reading `registry.toml`,
  and a payload nobody is told about is the same defect as a payload that does not ship. Holding the
  addition to the existing code block plus one sentence is the smallest form that closes it.

## 9. Revision log

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
