# TOOL-aHonedRuleset-3 — the kickoff engine's unattended exits move to the kit that owns them

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

Move the six numbered interactive exits out of `skills/session-kickoff/SKILL.md` Step 5b and into
`tools/unattended/PROTOCOL.template.md`, which is the contract that owns them, leaving a pointer
behind. The engine is a universal, project-agnostic skill sitting 207 bytes under a declared 18 KiB
ceiling, and Step 5b is its largest section; the destination has kilobytes of room and is where every
other unattended rule already lives.

## 2. Scope (IN)

- **S1 — the exits land in the contract.** `tools/unattended/PROTOCOL.template.md` gains a new
  `## 13.` section carrying the intro sentence and the six numbered exits verbatim, appended after
  `## 12. The pass sequence is DRIVEN, not remembered`. The rendered half
  `memory/guides/UNATTENDED-PROTOCOL.md` is produced by re-running the kit's adopter, never
  hand-edited.
- **S2 — the engine keeps a pointer, not a summary.** Step 5b's lines 223–241 are replaced by one
  short paragraph naming `<MEMORY_ROOT>/guides/UNATTENDED-PROTOCOL.md` §13 and stating that the
  exception exists, so a reader of the engine alone still learns an unattended run resolves those
  stops. Everything else in Step 5b — the heading, the default-stop paragraph, the authorization
  paragraph, the build-method load, the ABORT-is-a-verb paragraph — is untouched.
- **S3 — the `KICKOFF_EXITS` floor follows its subject.** Check 12's exit-count arm in
  `tools/unattended/check-unattended.sh` counts in the installed protocol instead of the engine, its
  failure text is rewritten to name what it now reads, and the key's documented meaning is corrected
  in its three prose carriers.
- **S4 — the moved branch is re-armed.** `tools/unattended/check-unattended.test.sh` stages the
  exit-drop break in the protocol pair rather than in its synthetic engine fixture, and its
  assertions match check 12's new failure text so `check-arms.py` still sees the branch armed.
- **S5 — the three cross-references that name the old location are repointed.**
  `tools/memory-tree/BUILD-METHOD.template.md:60` and `:274`, and
  `tools/unattended/SKILL.template.md:258`, each name "Step 5b exit 5" or "Step 5b … per exit". Each
  is repointed at the protocol section, subject to the byte budget in §4.
- **S7 — the kickoff manifest is re-stamped in the same commit.** `memory/guides/SESSION-KICKOFF.md`
  gets its `last-audit` re-stamp bundled into this unit's commit, because three files this unit
  stages are `watch:` pathspecs on line 6 of that file: `skills/session-kickoff/SKILL.md`,
  `.unattended.conf` and `memory/guides/BUILD-METHOD.md`. `.githooks/pre-commit` runs
  `manifest-check.sh --staged` unconditionally, so a commit that stages a watched file without the
  bundled re-stamp is refused before it exists.

There is no S6. Rev-1 numbered the engine's high-water bump S6, this revision deleted it, and the
slot is left vacant so a citation of the removed item still lands on nothing rather than on a
different rule. §3 says where that decision went and §9 records the removal.

## 3. Non-goals (OUT)

- No rule is dropped, reworded or renumbered. The six exits move as bytes; their content is out of
  scope, and so is any argument about whether five of them should still abort.
- No protocol section is renumbered. `§1`, `§5`, `§9`, `§10`, `§11` and `§12` are cited by name from
  `tools/unattended/SKILL.template.md`, `memory/guides/BUILD-METHOD.md`, `UNATTENDED-VERBS.md` and
  `tools/unattended/check-pass-order.sh`; the new section appends as `## 13.` for that reason.
- `memory/DECISIONS.md:38` ("the mandate buys exactly ONE of the kickoff engine's six interactive
  exits") is NOT edited. The decision log is append-only and legacy records are cited verbatim.
- The other four ranked cut-list entries are not touched. This unit is one mechanism.
- No ceiling is created, raised or lowered, and `BUILD-METHOD`'s ungated prose budget is not
  converted to a registry row. `TOOL-aHonedRuleset-6` is that question, in this same build, and the
  README's parked owner decision is now that unit's §8 F1. This unit routes the question there rather
  than back to the README.
- The `skills/session-kickoff/SKILL.md` high-water row in `tools/template-size-highwater.txt` is NOT
  re-recorded here. `TOOL-aHonedRuleset-5` §8 F1 is the owner call on that row, unit 5 is `order 2`
  and this unit is `order 1`, and two siblings state the no-bump-on-a-shrink rule with a reason —
  unit 2 §3 and unit 4 §3. A bump taken at order 1 would record a figure order 2 immediately
  supersedes.
- Section 5's parked-field rule, the ABORT verb and the hand-back trigger stay in the engine. Only
  the enumeration moves.

## 4. Design

### Inventory — every number here was measured, not estimated

| fact | measured value | how |
|---|---|---|
| engine size / ceiling | 18225 B of 18432, 207 free | `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` |
| engine high-water | 18215, currently WARNing at +10 | same command, first output line |
| Step 5b total | 3395 B, the file's largest section | `awk` section split over `^## ` |
| the block that moves (lines 223–241) | 1467 B | `sed -n '223,241p' … \| wc -c` |
| protocol size / cap | 54772 B of `GUIDE_CAP_BYTES` 61440, 6668 free | `wc -c`; cap at `check-memory-hygiene.sh:63` |
| protocol lines / cap | 649 of `GUIDE_CAP_LINES` 750 | `wc -l` |
| `BUILD-METHOD.template.md` | 24564 B of a self-declared 24576, 12 free | `wc -c`; budget at its own line 8 |
| exits matching the counter today | 6, all in Step 5b | `grep -cE '^[0-9]+\. \*\*Step ' skills/session-kickoff/SKILL.md` |
| same pattern in the protocol today | 0 | `grep -cE '^[0-9]+\. \*\*Step ' tools/unattended/PROTOCOL.template.md` |

The census estimated this cut at 1200–1400 B moved. The measurement is 1467 B of block minus a
pointer of roughly 230 B, so a net recovery near 1237 B — inside the census range, and the
measurement is what binds.

### The render row, confirmed before anything else

`tools/unattended/kit.toml` lines 19–23 declare `include = ["PROTOCOL.template.md"]`,
`role = "rendered"`, `to = "{memory_root}/guides/UNATTENDED-PROTOCOL.md"`, `placeholders = []`. Both
halves measure 54772 B today, so the pair is byte-identical and the template *is* the shipped
document. Check 10 of `tools/unattended/check-unattended.sh` byte-compares them after a
`sed 's/\r$//'` and a kit-prefix normalisation. The edit is made in the template and rendered down.
An empty `placeholders` list also means the moved prose must introduce no `{{TOKEN}}`, or
`python tools/check-kit-placeholders.py` reds; the block carries none.

`tools/unattended/PROTOCOL.template.md` is absent from `tools/install-prefix-carried.txt`, so its
carried-prefix count is zero and the ratchet is shrink-only. The moved block spells no
`tools/<kit>/<file>` path, so it stays at zero. For the same reason the pointer left in the engine
names `<MEMORY_ROOT>/guides/UNATTENDED-PROTOCOL.md` and never
`tools/unattended/PROTOCOL.template.md`: the engine's carried count is 2 and adding a kit path would
raise it.

### The coupling: what `KICKOFF_EXITS` counts, and why moving the list breaks its stated meaning

Every reader of the placeholder, found by grep over the tracked tree:

| reader | what it does |
|---|---|
| `tools/unattended/check-unattended.sh:1441–1444` | the only consumer: `nex=$(grep -cE '^[0-9]+\. \*\*Step ' <<<"$eng")`, then refuses when `nex < KICKOFF_EXITS` |
| `tools/unattended/check-unattended.sh:120` | the default-blank initialiser |
| `tools/unattended/kit.toml:62` | lists it in `optional_keys` |
| `tools/unattended/PROTOCOL.template.md:464` and its render | the §8 key table row that check 22 joins against the example conf |
| `tools/unattended/.unattended.conf.example:77–81` | the adopter-facing comment and the blank default |
| `.unattended.conf:53–57` | this repo's declaration, `KICKOFF_EXITS="6"` |
| `tools/unattended/check-unattended.test.sh:937–970` | the fixture and the arm for check 12 branch 4 |

The counter reads `$eng`, the file named by `KICKOFF_ENGINE`. Move the list and `nex` becomes 0
against a floor of 6, so the leg reds on a correct implementation. That is the mechanical half.

The semantic half is sharper and is why this cannot be an afterthought.
`tools/unattended/.unattended.conf.example` says of the key, in the shipped bytes an adopter copies:
"MEASURE it against your own engine, because the count is a property of that document and not of this
kit." After the move that sentence is false. The enumeration becomes kit-owned, so an adopter has
nothing of their own to measure.

**The proposed fix, and the precedent that makes it cheap.** The key stays, and it joins the family
it now belongs to. `CORE_FLOOR`, `DIRECTIVES_FLOOR` and `HALT_FLOOR` are already conf-declared
shrink-only floors on KIT-OWNED sets, documented three and four rows above `KICKOFF_EXITS` in the
same §8 table. `KICKOFF_EXITS` becomes the fourth member of that family rather than a new shape.
Concretely:

1. The counter's subject becomes `$LIVEDOC` (`$M/guides/UNATTENDED-PROTOCOL.md`), already bound at
   `check-unattended.sh:1324`. Guard it with `[ -f "$LIVEDOC" ]` and skip when absent: check 10
   already owns the missing-half refusal, and two reports for one problem is the shape that file's
   own header warns about.
2. The failure text stops saying "the kickoff engine" and names the protocol. The rule it states —
   a dropped exit is a place an unattended run silently regains to stop — is unchanged.
3. The §8 table row, the example-conf comment and this repo's `.unattended.conf` comment are
   rewritten to say the floor counts the protocol's own enumeration. The "measure it against your own
   engine" instruction is deleted rather than left standing beside a contradicting mechanism.
4. `KICKOFF_EXITS="6"` in `.unattended.conf` keeps its value; the count does not change.

**Summing the two files was considered and rejected.** Counting `$eng` plus `$LIVEDOC` would keep the
floor green through the move with no edit at all, and it is wrong for a reason this repo has already
written down: `tools/memory-tree/check-arms.py`'s own docstring refuses aggregate floors because
"an aggregate total lets one gate's DELETED guard be masked by another gate's added one". A sum lets
an exit deleted from the protocol be masked by an unrelated numbered line appearing in the engine.

**Whether the arm stays gated on `KICKOFF_ENGINE` is a fork** — see §8 F1.

### The three stale cross-references

| file:line | text today | after the move |
|---|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md:60` | "the disposition is the kickoff engine's Step 5b exit 5 — read it there" | names the protocol section |
| `tools/memory-tree/BUILD-METHOD.template.md:274` | "Step 5b says which one per exit" | names the protocol section |
| `tools/unattended/SKILL.template.md:258` | "the kickoff engine's Step 5b exit 5 does not reach here" | names the protocol section |

None of them breaks outright — Step 5b survives as a forwarding pointer, so a reader arrives one hop
late rather than nowhere. They are in scope anyway because leaving them is the
`amendment-leaves-its-other-half-standing` class the census named for unit 1.

`BUILD-METHOD.template.md` has **12 bytes free** against a budget its own line 8 declares and its own
line 16 admits no gate enforces. Its house convention, stated at its line 20, is that `§<n>` names a
section of another document, so `protocol §13` is the correct spelling there. The repoint must be
measured, not assumed to fit: `wc -c tools/memory-tree/BUILD-METHOD.template.md` must stay at or
below 24576 after the edit. `tools/unattended/SKILL.template.md` has no ceiling anywhere and is
unconstrained. §8 F2 carries the branch for a repoint that will not fit.

### Migration

There is no data migration. Two ordering constraints:

1. `tools/unattended/PROTOCOL.template.md` is edited, then
   `bash tools/unattended/adopt-unattended.sh` re-renders both it and
   `.claude/skills/unattended/SKILL.md`; `tools/memory-tree/adopt-memory-tree.sh` re-renders
   `memory/guides/BUILD-METHOD.md` from its template. Hand-editing either rendered copy reds check 10
   or the `kit/dogfood doc parity` leg, and the edit is lost at the next render.
2. The checker, the checker's test and both halves of the protocol move in ONE commit. A commit that
   moves the prose without moving the counter is red, and one that moves the counter without the
   prose is red the other way.

`tools/unattended/check-unattended.test.sh` already ships the seam for step 2's staging: `pedit()` at
line 1576 mutates both protocol copies through `mutate`, which fails loudly when its locator stops
matching. It is defined below the check-12 block at line 937, so the builder either hoists the
definition or writes the two-file edit inline — the helper is the reuse, its current position is not.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/PROTOCOL.template.md` | +1 section, roughly +1530 B |
| `memory/guides/UNATTENDED-PROTOCOL.md` | rendered, not authored |
| `skills/session-kickoff/SKILL.md` | −1467 B, +~230 B pointer |
| `tools/unattended/check-unattended.sh` | check 12's exit-count arm: subject, guard, message |
| `tools/unattended/check-unattended.test.sh` | fixture + two assertions |
| `tools/unattended/.unattended.conf.example` | the key's comment |
| `.unattended.conf` | the key's comment |
| `tools/memory-tree/BUILD-METHOD.template.md` | two pointers, ≤12 B net |
| `tools/unattended/SKILL.template.md` | one pointer |
| `.claude/skills/unattended/SKILL.md`, `memory/guides/BUILD-METHOD.md` | rendered |
| `memory/guides/SESSION-KICKOFF.md` | S7 — re-verify §B, re-stamp `last-audit` |
| `memory/map/features/session-kickoff.md`, `memory/map/features/unattended.md` | dossier prose refreshed on touch |

`tools/template-size-highwater.txt` is deliberately absent from this table — see §3.

### Alternatives rejected

- **Move the exits to `tools/unattended/SKILL.template.md`** (the agent-facing Skill) instead of the
  protocol. It is the document an agent actually reads at run time, and neither half of it has a
  ceiling anywhere: the template measures 52471 B and its render `.claude/skills/unattended/SKILL.md`
  measures 53234 B, both by `wc -c` at base. Rejected: the exits are a binding rule about what a
  mandate does and does not buy, which is contract material, and `TOOL-aScouredKit-23` already has
  that uncapped Skill open as a row — growing it is answering that row's question from inside this
  unit. That row names the RENDERED `.claude/skills/unattended/SKILL.md` as its subject and records
  it at 48767 B, a figure measured when the row was written and 4467 B stale today; the template is
  not the file it names.
- **Keep a shrunken enumeration in the engine and move only the resolutions.** The engine-specific
  half (which step, which condition) and the kit-policy half (abort, park, hand-back) do split
  cleanly in principle. Rejected: a table of six conditions with their resolutions elsewhere is
  useless to both readers, and it recovers a few hundred bytes instead of twelve hundred.
- **Delete the floor.** Rejected: it is the only thing that notices an exit silently disappearing,
  and it costs one line to keep.

## 5. Production-readiness checklist

- security — N/A. No write path, no authorization surface, no egress. The protocol's §9 boundary is
  untouched and the moved prose makes no claim about what binds a run.
- perf / scale — N/A. One `grep -c` changes which file it reads.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the new counter arm needs its absent-file case decided, not
  discovered: a missing `$LIVEDOC` skips rather than counting 0, because check 10 already refuses it.
- observability — the check-12 failure message is the only signal, and it must name the file it
  actually read or the next reader debugs the wrong document.
- risks — the whole risk is a partial landing. Prose moved without the counter reds the bar; counter
  moved without the prose reds it differently. One commit, per §4 Migration.
- testing + left-shift gates — no new gate. The existing check 12 branch 4 stays armed by moving its
  fixture with its subject; `python3 tools/memory-tree/check-arms.py --check` is what catches a
  message edited without its assertion.
- migration / rollback — a single revert restores both halves; nothing outside the tree holds state.
- user docs — the engine's pointer IS the user doc, and `.unattended.conf.example` is the adopter's.
  Both are in scope, not follow-ups.

## 6. Acceptance criteria

- **AC1** — When the block has moved, `grep -cE '^[0-9]+\. \*\*Step ' tools/unattended/PROTOCOL.template.md`
  returns 6 and the same command over `skills/session-kickoff/SKILL.md` returns 0.
- **AC2** — When the engine is measured, `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`
  reports at least 1200 bytes under 18432, against the 207 measured at base `102e98f0`.
- **AC3** — When the protocol is measured, `bash tools/memory-tree/check-memory-hygiene.sh` is green,
  so `memory/guides/UNATTENDED-PROTOCOL.md` is still inside `GUIDE_CAP_BYTES` 61440 and
  `GUIDE_CAP_LINES` 750.
- **AC4** — When both halves are rendered, `bash tools/unattended/check-unattended.sh` exits 0, so
  check 10's byte-compare of the protocol pair and check 22's §8 key-table join both hold with the
  new section and the rewritten `KICKOFF_EXITS` row present.
- **AC5** — When one numbered exit is deleted from BOTH protocol copies through the
  `check-unattended.test.sh` `pedit` helper, `bash tools/unattended/check-unattended.sh` fails naming
  check 12 and printing `5 against 6`; restoring it returns the leg to exit 0. Staged, observed RED,
  unstaged.
- **AC6** — When the engine's Step 5b heading or the READY prompt string is deleted,
  `bash tools/unattended/check-unattended.sh` still fails check 12 with its existing two messages, so
  moving the count did not disarm the other two arms.
- **AC7** — When the suite runs, `bash tools/unattended/check-unattended.test.sh` passes and
  `python3 tools/memory-tree/check-arms.py --check` exits 0 with check 12 branch 4 reported ARMED by
  `--report`.
- **AC8** — When the cross-references are repointed, `wc -c tools/memory-tree/BUILD-METHOD.template.md`
  reports at most 24576, and `grep -rn 'Step 5b exit' tools/ memory/guides/ .claude/` returns, outside
  `memory/builds/` and `memory/archive/`, exactly what the §8 F2 ruling permits: nothing at all if F2
  goes the all-three-repoints way, or only `tools/memory-tree/BUILD-METHOD.template.md:60` and its
  render `memory/guides/BUILD-METHOD.md:60` if F2 goes the fallback way. Under either branch
  `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` return no hit, because
  that repoint is unconditional.
- **AC9** — When the renders are re-run, `bash tools/memory-tree/kit-dogfood-parity.test.sh` and
  `bash tools/unattended/adopt-unattended.sh --check` both exit 0.
- **AC10** — When the shipped surface is scanned, `bash tools/check-install-prefix.sh` reports
  `none rising` against the 118 recorded files measured at base, so the moved prose added no kit-path
  literal to `tools/unattended/PROTOCOL.template.md`.
- **AC11** — When the engine is measured after the cut,
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` prints no `TEMPLATE-SIZE WARN`
  line, because `tools/check-template-size.sh:183` WARNs only when the measured bytes exceed the
  recorded high-water and the cut puts the file below the 18215 already on record. The row itself is
  not written by this unit — see §3.
- **AC12** — When the pointer replaces the moved block, the engine's Step 5b section still routes a
  reader to the contract:
  `sed -n '/^## Step 5b/,/^## Scaffolding/p' skills/session-kickoff/SKILL.md | grep -c 'guides/UNATTENDED-PROTOCOL.md'`
  returns at least 1. Measured at base it returns 0, because the engine names that document nowhere,
  so a build that deletes the block and leaves no pointer fails this.
- **AC13** — When the cross-references are repointed,
  `grep -rn 'Step 5b says which one per exit' tools/ memory/guides/ .claude/` returns, outside
  `memory/builds/` and `memory/archive/`, nothing if §8 F2 goes the all-three-repoints way, or only
  `tools/memory-tree/BUILD-METHOD.template.md:274` and its render `memory/guides/BUILD-METHOD.md:274`
  if F2 goes the fallback way. This criterion exists because AC8's `Step 5b exit` pattern does not
  match line 274's wording — verified at base, where that pattern matches line 60 of
  `BUILD-METHOD.template.md` and never line 274, so line 274 could be left untouched with AC8 green.
- **AC14** — When the key's documented meaning is corrected,
  `grep -c 'MEASURE it against your own engine' tools/unattended/.unattended.conf.example` PRINTS 0.
  It prints 1 at base, at line 78. A zero count exits non-zero, so terminate the probe with `;` or
  `|| true` rather than chaining it — a passing check reads as a failure otherwise. Check 22 cannot carry this: its own header at
  `tools/unattended/check-unattended.sh:1379-1381` states it grades presence of the key name in the
  table region and that a row whose prose is wrong is green there.

## 7. Gates

- `kickoff engine size <=18KiB` — `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`
- `unattended kit gate` — `bash tools/unattended/check-unattended.sh` (checks 10, 12, 16, 22)
- `unattended skill wiring` — `bash tools/unattended/adopt-unattended.sh --check`
- `memory hygiene` — `bash tools/memory-tree/check-memory-hygiene.sh`
- `kit/dogfood doc parity` — `bash tools/memory-tree/kit-dogfood-parity.test.sh`
- `harness arms (fail branches armed or pinned)` — `python3 tools/memory-tree/check-arms.py --check`
- `install-prefix (shipped surface)` — `bash tools/check-install-prefix.sh`
- `kit placeholders (a declared token its adopter substitutes)` — `python tools/check-kit-placeholders.py`
- `kit version markers` — `bash tools/check-kit-versions.sh`
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Three files this unit
  stages are `watch:` pathspecs on line 6 of `memory/guides/SESSION-KICKOFF.md`:
  `skills/session-kickoff/SKILL.md`, `.unattended.conf` and `memory/guides/BUILD-METHOD.md`. S7 is
  the bundled `last-audit` re-stamp that keeps this leg and the pre-commit hook green.
- Off the bar, on demand for this unit's own subject — `bash tools/unattended/check-unattended.test.sh`
  and `bash tools/unattended/run-unattended-gates.sh`. A kit's self-tests are not merge-bar legs
  (owner ruling, 2026-08-23) and `unattended` is the kit that ruling was taken on, so this unit runs
  them itself rather than expecting the bar to.
- New gate added: none. The mechanism is a repointed subject on an existing armed branch.

## 8. Open questions

- **F1 — does the exit-count arm stay inside `if [ -n "$KICKOFF_ENGINE" ]`?** Once the enumeration is
  kit-owned, its shrink is a kit regression whether or not the adopting project ships a kickoff
  skill, which argues for lifting the arm out of that block. Against: an adopter with no kickoff
  engine has no interactive exits to protect, `.unattended.conf.example` ships
  `KICKOFF_EXITS=""` for exactly that case, and lifting it changes the blank-turns-it-off contract
  documented in the §8 key table. **Recommendation: keep it inside the block.** It is the smaller
  diff, it preserves the documented off-switch, and this repo declares `KICKOFF_ENGINE`, so the floor
  keeps binding here either way.
- **F2 — the `BUILD-METHOD` repoint against its last 12 bytes.** Two pointers must be rewritten in a
  file with 24564 of a self-declared 24576 bytes. A spelling like "the unattended protocol's §13
  exit 5" is roughly one byte longer than "the kickoff engine's Step 5b exit 5", and line 274's
  rewrite costs a few more; the pair plausibly fits, and plausibly does not. **Recommendation:**
  attempt the repoint, measure with `wc -c`, and if it does not fit within 24576, repoint only
  `tools/unattended/SKILL.template.md:258` and leave BUILD-METHOD's two pointers forwarding through
  Step 5b's stub — then say so in the build record. AC8 and AC13 are written against both branches,
  so neither outcome makes the acceptance set unsatisfiable. **Landing `TOOL-aHonedRuleset-6` first
  makes this fork moot:** that unit is the carrier for the parked budget question, it edits the same
  file's lines 8–18, and either of its branches frees roughly 950 B (option a) or 1101 B (option b) —
  disjoint from the lines 60 and 274 this unit repoints. With that space recovered the 12-byte
  squeeze disappears and the repoint simply fits. Unit 6 is `order 3` and this unit is `order 1`, so
  under the declared order the fork is live; a re-order is the owner's to make, not this spec's.
- **F3 — bump `KIT_UNATTENDED_VERSION` from 1.17, or not?** The kit's shipped contract gains a
  section and its checker changes a subject, which is an argument for a bump; against it,
  `tools/check-kit-versions.sh` asserts presence and marker agreement rather than movement, no
  verdict-epoch gate covers this kit (`check-verdict-epoch.sh` scans only
  `check-memory-hygiene.sh` and six memory-tree/memory-recall delegates), and a bump must move the
  `gov:kit unattended@` marker in **16 tracked carriers** at once or `govkit selfcheck` 5c reds.
  **Recommendation: do not bump.** Nothing mechanically owes it, and a sixteen-file stamp sweep
  inside a prose-move unit is a second mechanism.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Every figure in §4 measured at base `102e98f0`; the census's
  1200–1400 B estimate for this cut was confirmed at 1467 B moved.
- rev-2 · 2026-09-04 · folded the round-1 spec audit
  (`2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md`), findings S1, S2, S3, A4, A5, A6, A7, P2
  and P4. Rev-1's **S6** — the `check-template-size.sh --bump` of the engine's high-water row — was
  DELETED and the slot left vacant so the audit's citation still points at the removed item; §3 now
  states that the row is `TOOL-aHonedRuleset-5` §8 F1's to rule. AC11 lost its bump clause and now
  observes only the absent `WARN`. The bundled `memory/guides/SESSION-KICKOFF.md` `last-audit`
  re-stamp entered as **S7**, with a §4 files-touched row and a widened §7 leg note. AC8 became
  conditional on §8 F2 instead of presuming its non-recommended branch, and F2 gained the note that
  landing `TOOL-aHonedRuleset-6` first makes it moot. Three criteria were added: **AC12** observes
  S2's pointer, **AC13** covers `BUILD-METHOD.template.md:274`, whose wording AC8's pattern never
  matched, and **AC14** observes the false sentence in `.unattended.conf.example` that check 22
  cannot grade. Two figures were corrected against source: the BUILD-METHOD budget is declared at its
  line **8**, not line 7 (two occurrences), and `tools/unattended/SKILL.template.md` measures
  **52471 B** — 48767 was `TOOL-aScouredKit-23`'s figure for the RENDERED
  `.claude/skills/unattended/SKILL.md`, which measures 53234 B today. No §8 fork was resolved; F1, F2
  and F3 remain UNRESOLVED and unsigned.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "counting an enumeration in a governing document against
a shrink-only floor"` over 645 symbols, 188 inventory keys and 19 affordance seams returned no seam
for this unit, and correctly so: the ranked candidates are Python symbols
(`count_never_falls`, `parse_floors`, `signal_shrink_only`) and affordance-seam prose, while the
mechanism here is shell inside one checker. **This unit adds no mechanism** — it repoints three that
already exist, named by path: the exit-count arm at `tools/unattended/check-unattended.sh:1441-1444`,
the `$LIVEDOC` binding it will read at `:1324`, and the `pedit()` two-copy mutator at
`tools/unattended/check-unattended.test.sh:1576` which stages a break in both halves of the protocol
pair through `mutate`. The floor family it joins — `CORE_FLOOR`, `DIRECTIVES_FLOOR`, `HALT_FLOOR` —
is the existing pattern for a conf-declared shrink-only count over a kit-owned set, and it is the
reason no new shape is invented here.

Recall terms used: `python tools/memory-recall/query.py "why does the unattended kit floor the
kickoff engine's interactive exit count, and what may move that enumeration" --terms "KICKOFF_EXITS
shrink-only floor kickoff engine Step 5b hand-back unattended protocol parity render byte-compare
interactive exits abort park"` — 39 hits, of which `TOOL-aUnmannedHelm-8`,
`memory/builds/aUnmannedHelm/spec/2026-08-10-spec-aUnmannedHelm-8-u6-handback.md` (S3 and S4, which
built check 12 and the floor) and
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-3.md:217` (an AC that turns
on the exit floor being unchanged) are the records that bind this change.
