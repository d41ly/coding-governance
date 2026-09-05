# TOOL-aHonedRuleset-6 — BUILD-METHOD's self-declared budget becomes enforceable or goes away

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/BUILD-METHOD.template.md` declares a byte and line budget for itself in its own
opening prose, says at line 16 that no gate enforces the pair, and sits 12 bytes under the byte half.
Resolve that state in one direction or the other, so the ceiling either binds mechanically or stops
claiming to exist.

## 2. Scope (IN)

The executable scope is selected by the §8 F1 ruling. S1 through S6 are option (a), the recommended
path. S7 is the whole of option (b). S8 is owed under EITHER branch and is not selected by the
ruling. Option (c) has no scope.

- **S1** — a row in `tools/template-size-limits.txt` for `tools/memory-tree/BUILD-METHOD.template.md`
  at `24576`, with a comment carrying the value's history, per that file's stated grammar.
- **S2** — a leg in `tools/gate-legs.json` invoking
  `bash tools/check-template-size.sh tools/memory-tree/BUILD-METHOD.template.md`, shaped like the
  three legs already riding that script.
- **S3** — a seeded row in `tools/template-size-highwater.txt`, written by `--bump` and never by
  hand, so the leg does not print `no-ratchet` on every bar.
- **S4** — a regenerated `tools/govkit/subject-pins.tsv` carrying the new leg's `subject` and `chunk`.
- **S5** — the budget passage in `tools/memory-tree/BUILD-METHOD.template.md` shrinks to a pointer at
  the declaration, and its raise history moves into the S1 comment.
- **S6** — `memory/guides/BUILD-METHOD.md` re-rendered from the edited template in the same commit.
- **S7** — option (b) only: delete the budget passage from the template, re-render, and add nothing.
- **S8** — either branch: `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp bundled
  into the same commit, §B re-verified first. Option (a) stages two watched pathspecs off line 6 of
  that file, `tools/gate-legs.json` and `memory/guides/BUILD-METHOD.md`; option (b) stages the second
  of them alone. Either way the obligation fires, so this item sits outside the F1 selection.

## 3. Non-goals (OUT)

- **Ceilings for the documents that have none.** `TOOL-aScouredKit-23` owns that question and names
  `WIRE-INTO-PROJECT.md` and `.claude/skills/unattended/SKILL.md`. BUILD-METHOD is a different state:
  it has a ceiling and no gate, rather than no ceiling anywhere. This unit does not widen to that set.
- **A size discipline on rendered kit docs, owned by the kit that renders them.** That is
  `TOOL-dSpentCeiling-4`, whose candidates are a per-template ceiling in `kit.toml` beside the
  `[[render]]` row or a rendered-versus-authored drift signal. Option (a) here is gov-local by
  construction and leaves that row entirely open — see §4, "What option (a) does not reach".
- **Generalising the high-water ratchet to the `.memory-tree.conf` class caps.** That is
  `TOOL-dFoldedVerdict-7`. This unit gives one file the ratchet; it does not touch `GUIDE_CAP_BYTES`,
  `DOSSIER_CAP_BYTES` or `INDEX_CAP_BYTES`.
- **Any other cut on the aHonedRuleset ranked list.** Rows 1 through 5 of that list are other units.
- **The census script.** `memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py`
  belongs to `TOOL-aHonedRuleset-1`. It needs no edit either way, verified in §4, and its one stale
  docstring phrase predates this unit.

## 4. Design

### Inventory

Every figure measured on this worktree at base `102e98f0`. The gate measures LF-normalized bytes
(`tr -d '\r' | wc -c` in `tools/check-template-size.sh`); on this checkout that equals `wc -c`, so
the two agree and both are quoted below as the same number.

| fact | value | how it was measured |
|---|---|---|
| template bytes | 24564 | `wc -c tools/memory-tree/BUILD-METHOD.template.md` |
| template lines | 317 | `wc -l` on the same file |
| declared byte budget | 24576 | the file's own line 8, `≤24 KB` |
| free against it | 12 B | 24576 minus 24564 |
| declared line budget | 350 | the file's own line 8 |
| rendered bytes | 24553 | `wc -c memory/guides/BUILD-METHOD.md` |
| rendered lines | 317 | `wc -l` on the same file |
| ceiling on the render today | 61440 B / 750 lines | `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES`, `tools/memory-tree/check-memory-hygiene.sh:63` |
| ceiling on the template today | none | no row in `tools/template-size-limits.txt`, no leg in `tools/gate-legs.json`, and it sits outside `MEMORY_ROOT` so hygiene check 6 never sees it |
| budget passage weight | 1101 B | `sed -n '8,18p' … \| wc -c` |
| raise history within it | 825 B | `sed -n '10,18p' … \| wc -c` |

The census reported 12 bytes free from its own script. This unit re-measured and got the same
number, so the census stands unamended on this carrier.

Two figures are worth stating together. The passage that declares a ceiling with 12 bytes of room
costs 1101 of the 24564 bytes it constrains, which is 4.5% of the file.

### The state today, precisely

Line 8 declares `**Budget: ≤24 KB, ≤350 lines**` and gives the reason: M7 re-reads this file whole at
every pass boundary, so a method too expensive to re-read is skipped exactly when it is needed. Lines
10 through 14 carry three raises and the argument for each. Line 15 says the byte half binds first,
line 16 says `No gate enforces the pair`, and line 18 says whether one is ever added is a separate
question nobody has ruled. This spec is that ruling being asked for.

### Which file the row belongs on

The budget is declared on the TEMPLATE and the reason it gives is about the RENDER, so the question
is real. Four measured facts settle it on the template.

**The render is already bounded and the template is not.** `memory/guides/BUILD-METHOD.md` sits
under `MEMORY_ROOT`, so hygiene check 6 caps it at 61440 B and 750 lines. A 24576 row on the render
would be a second and tighter bound over an already-bounded file, which is the shape
`TOOL-dSpentCeiling-1` retired when it killed `READ_PATH_CEILING`. The template is under `tools/`,
where check 6 never looks, so a row there adds a bound where none exists instead of stacking one.

**The render's byte count is partly spent by the install prefix.** The template carries four
`{{KIT_DIR}}` and five `{{TOOL_ROOT}}` tokens, counted with
`grep -o '{{[A-Z_]*}}' … | sort | uniq -c`. `tools/memory-tree/kit-dogfood-parity.test.sh` derives
both from where the kit sits and substitutes them, so the rendered size is a function of the install
path. Predicted here: `24564 + 4 × (17 − 11) + 5 × (6 − 13) = 24553`, and the measured render is
24553, so the model is exact. The same model gives 24499 at a root install and 24616 at a
`vendor/tools/` prefix. That last one breaches a 24576 ceiling by 40 bytes with no prose changed at
all. A ceiling on a rendered file is a ceiling an adopter's directory layout helps spend.

**Parity makes the template bound the render, and not the other way round.** The parity leg forces
render equals substitute(template), so a bounded template bounds the render to within the
substitution delta. The converse is weaker, because that delta's sign depends on the prefix.

**A failure must name a file the author may edit.** This build's own rule and the census both say
cuts are made in the template and rendered down, because hand-editing the copy under
`memory/guides/` reds the parity leg and loses the edit at the next render. A gate whose message
names `memory/guides/BUILD-METHOD.md` names the one file the author must not touch.

The registry precedent cuts neither way on its own. `tools/template-size-limits.txt` already holds
both halves of the charter pair, `coding-governance-agents.template.md` at 49152 and `AGENTS.md` at
64512, but at different numbers and with a separate argument beside each. The precedent is therefore
"declare the file whose number you can argue", and here only the template's number is arguable,
because only the template's bytes are prose.

### What option (a) costs, corrected

The build README's parked decision calls this "a one-line change". Measured against the tree, it is
four carriers, and `TOOL-aScouredKit-23` already recorded the first half of the reason: a row alone
is inert, because `check-template-size.sh` only measures a subject it is invoked on.

| carrier | what changes | why it is needed |
|---|---|---|
| `tools/template-size-limits.txt` | one row plus its justification comment | the declared ceiling, resolved by an `awk` lookup keyed on the repo-relative path |
| `tools/gate-legs.json` | one leg naming the subject | without it nothing ever invokes the script on this file |
| `tools/template-size-highwater.txt` | one row, seeded by `--bump` | otherwise the leg prints `no-ratchet — growth is unpriced` on every bar |
| `tools/govkit/subject-pins.tsv` | one generated row | it is a GENERATED per-leg pin of `subject` and `chunk`, regenerated with `python tools/govkit/govkit.py selfcheck --write` |

Wall-clock cost is measured rather than assumed. `.git/gate-ledger.tsv` records the three sibling
size legs at 1.286 s, 1.277 s and 1.282 s. A fourth adds about 1.28 s of leg-sum into a bounded pool
whose longest leg is three orders of magnitude larger, so the "cost is a verdict" rule is satisfied
by inspection rather than by a new ceiling argument.

### What happens to the prose

Under option (a) the passage does not vanish, it relocates. `tools/template-size-limits.txt` states
its own grammar as "Comments carry the justification for a value and every movement of it, because a
number with no history beside it is a number nobody can question". The 825 B of raise history is
exactly that content, and the limits file is the carrier designed to hold it. What stays in
BUILD-METHOD is a pointer sentence naming the declaration and keeping the local reason, because the
reason is about M7 and belongs beside M7. Line 16's sentence goes, because it becomes false.

This is the charter's §6 rule applied to itself: a value stated in prose beside the source that owns
it rots between changes, so point at the source or gate the pair. Option (a) does both.

### The ceiling value after the cut

Keep 24576. After S5 the file sits roughly 950 B under it, and a ceiling with 950 B of slack invites
the next 950 B — but that is precisely the job the high-water ratchet already does, and re-seeding
the ceiling lower would be a fourth owner-called movement of a number this unit has no reason to
move. The `--bump` in S3 records the post-cut measurement, so the next growth is priced against what
the file actually became rather than against what it is permitted to be.

### What option (a) does not reach

An adopter who installs the memory-tree kit still receives `memory/guides/BUILD-METHOD.md` with a
budget nothing enforces, because `tools/check-template-size.sh` and `tools/template-size-limits.txt`
are gov-internal and appear in no `kit.toml`. Making the leg ship would mean moving the script into
the kit and declaring a `[[gate_leg]]` there, which is a kit-boundary change and is
`TOOL-dSpentCeiling-4`'s territory, not this unit's. This is the strongest argument for option (b),
which closes the adopter half by deletion, and it is stated here rather than buried in §8.

### The census script needs no change either way

Verified by reading. `ceiling_for` in the census script prefers `template-size-limits.txt` over the
prose reading, so option (a) flips the reported source with no edit. `load_prose_budgets` extracts
the number with a regex against the live file rather than holding a constant, and its own comment
says a budget edited away "stops being reported instead of silently persisting as a stale constant",
so option (b) degrades by design. The docstring's phrase "the two live instances" already disagrees
with the single-row dict at base; that is a pre-existing inaccuracy in another unit's file and is not
fixed here.

### Files touched (estimate)

| file | option (a) | option (b) |
|---|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | passage to pointer, about 950 B recovered | passage deleted, 1101 B recovered |
| `memory/guides/BUILD-METHOD.md` | re-rendered | re-rendered |
| `tools/template-size-limits.txt` | one row plus comment | untouched |
| `tools/gate-legs.json` | one leg | untouched |
| `tools/template-size-highwater.txt` | one seeded row | untouched |
| `tools/govkit/subject-pins.tsv` | regenerated | untouched |
| `memory/guides/SESSION-KICKOFF.md` | S8 — re-verify §B, re-stamp `last-audit` | same, S8 fires either way |

Both branches stage a watched pathspec, which is why the last row has no "untouched" column. Line 6
of `memory/guides/SESSION-KICKOFF.md` lists `tools/gate-legs.json` and `memory/guides/BUILD-METHOD.md`
among its ten `watch:` entries, verified by reading that line whole rather than its first clause.
`.githooks/pre-commit` runs `manifest-check.sh --staged` unconditionally, so a commit staging either
one without the re-stamp is refused at check 5.

### Alternatives rejected

- **The row on `memory/guides/BUILD-METHOD.md`.** Rejected on the four measured grounds above, the
  decisive one being that the render is already capped by check 6 and its byte count moves with the
  install prefix.
- **A new sibling script that measures bytes and lines together.** Rejected: the byte seam already
  exists and is declared as a reuse affordance, and the line half is argued in F2 to be droppable
  rather than worth new machinery.
- **Raising the ceiling to fund this build's other cuts.** Rejected: raising a ceiling is an owner
  decision and never a fix for the edit that hit it, which `tools/check-template-size.sh`'s own
  failure message says outright.

## 5. Production-readiness checklist

- security — N/A, no write path, no untrusted input, no new surface.
- perf / scale — one added leg measured at about 1.28 s against sibling ledger rows.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — the gate's own paths are already named: exit 5 on a non-numeric
  declared limit, exit 3 on a non-numeric high-water row, exit 2 on a missing subject.
- observability — the leg prints one line per run and `<git-dir>/gate-logs/` persists it.
- risks — the one real hazard is a template edit landing without the re-render, caught by
  `kit/dogfood doc parity`. A second is landing the row without the leg, which would be silently
  inert; AC1 and AC2 exist to catch exactly that.
- testing + left-shift gates — the new leg IS the left-shift, and §7's staged-break rule applies to
  it before it is called landed.
- migration / rollback — reverting is deleting four rows and restoring the passage; nothing is
  generated downstream that would go stale.
- user docs — N/A, this is an internal gate. `tools/template-size-limits.txt`'s own comment is the
  documentation, by that file's design.

## 6. Acceptance criteria

The first four criteria are branch-conditional on the §8 F1 ruling, which this spec does not sign.
Each carries an (a) half and a (b) half, and exactly one half is graded once the owner rules. The
remaining five hold under either branch. This is the shape the last criterion already had, and the
other four now match it. (No line of this paragraph opens with a criterion label, deliberately: check
12 reads a column-0 label as a new bullet and would invent one here.)

- **AC1(a)** — When `bash tools/check-template-size.sh tools/memory-tree/BUILD-METHOD.template.md`
  runs on the landed tree, it exits 0, reports the limit as 24576, and does not print `no-ratchet`.
- **AC1(b)** — `grep -c 'BUILD-METHOD.template.md' tools/template-size-limits.txt` and the same grep
  over `tools/gate-legs.json` each return 0, as they do at base. The absence is asserted rather than
  assumed, because option (b)'s whole product is that nothing measures this file.
- **AC2(a)** — The append is sized from the POST-S5 file, not from base. Measure
  `M = wc -c tools/memory-tree/BUILD-METHOD.template.md` after S5 lands, append `24576 − M + 1`
  bytes, run the new leg: it exits 1 with a `TEMPLATE-SIZE check 2 FAILED` line naming the overage.
  The break is then unstaged and the leg re-run green, and the RED observation is recorded in the
  build record. Base arithmetic does not survive this unit — 13 bytes reds the file at 24564, but S5
  takes roughly 950 B out of the same file, so a 13-byte append against the landed tree stays GREEN
  and the new gate's failing case would never be observed.
- **AC2(b)** — No leg is added, so §7's staged-break rule has no subject and no RED is owed. The
  witness is the absence: `grep -c 'check-template-size.sh' tools/gate-legs.json` returns the same
  count as at base, 3. Recorded as a named skip in the build record, never omitted, because a skip
  that looks like a pass is indistinguishable from coverage.
- **AC3(a)** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and
  `tools/govkit/subject-pins.tsv` carries a row for the new leg.
- **AC3(b)** — When the same command runs it exits 0 and `git diff --stat -- tools/govkit/subject-pins.tsv`
  is empty: no leg was added, so no pin moves.
- **AC4(a)** — When
  `python memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py`
  runs, the BUILD-METHOD carrier's ceiling source reads `template-size-limits.txt` and no longer
  reads `PROSE (ungated)`.
- **AC4(b)** — The same run prints that carrier with source `NONE`, a `-` ceiling and a `-` free
  column, and the file joins the `# uncapped:` tally. `load_prose_budgets`'s regex finds nothing once
  the passage is deleted, and `ceiling_for` then falls through both branches — the template is not
  under `memory/guides/`, so `GUIDE_CAP_BYTES` never catches it. That is the degradation the
  function's own docstring calls designed, and the criterion observes it rather than trusting it.
- **AC5** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the template edit, it
  exits 0, proving `memory/guides/BUILD-METHOD.md` was re-rendered rather than hand-edited.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, check 6 passes on the
  re-rendered `memory/guides/BUILD-METHOD.md`.
- **AC7** — When `wc -c tools/memory-tree/BUILD-METHOD.template.md` is run after the cut — S5 under
  option (a), S7 under option (b) — it reports at least 800 bytes below the base measurement of
  24564. The floor is set below both branches' recovery, roughly 950 B and 1101 B, so the criterion
  is scoped to what holds either way rather than to one ruling.
- **AC8** — When `grep -n 'No gate enforces the pair' tools/memory-tree/BUILD-METHOD.template.md`
  runs, it returns no hit, and `grep -n 'template-size-limits' ` on the same file returns the pointer
  sentence. Under option (b), the first half holds and the second is replaced by
  `grep -n 'Budget:' ` returning no hit.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs after the commit, it exits 0,
  proving the S8 `last-audit` re-stamp landed in the same commit as the watched pathspec. Holds under
  either branch, because both stage at least one.

## 7. Gates

New gate this unit adds, under option (a): one `tools/gate-legs.json` leg invoking
`bash tools/check-template-size.sh tools/memory-tree/BUILD-METHOD.template.md`, shaped like its three
siblings at `subject: repo` and `chunk: product`, and unguarded as they are.

`§7`'s staged-break rule binds it: the leg is not landed until its failing case has been observed,
which is AC2.

Legs that must stay green, all of them named from `tools/gate-legs.json` rather than from memory:

- `template size <=48KiB`, `charter size`, `kickoff engine size <=18KiB` — the three existing readers
  of `tools/template-size-limits.txt`, which this unit edits.
- `kit/dogfood doc parity` — catches a template edit landed without the render.
- `memory hygiene` — check 6 over the re-rendered guide.
- `govkit selfcheck` and `govkit acceptance matrix` — the generated subject pins.
- `dead-path carriers (deleted files still named)` — the new row names a repo path.
- `run-gates canary` — validates manifest rows, including a guard naming an untracked path.
- `line length` — the edited template and the rendered guide.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed under either
  branch, because option (a) stages two watched pathspecs and option (b) stages one. S8 is the scope
  item that keeps it green; AC9 observes it.

`template size gate selftest` is `subject: kit`, so it is held off an ordinary bar and is not owed:
this unit changes the script's DATA and not the script. That skip is stated rather than omitted.

## 8. Open questions

**F1 — what happens to the budget.** UNRESOLVED. This is an owner call and this spec does not sign
one.

- **(a) Declare it.** A row in `tools/template-size-limits.txt` at 24576, a leg, a seeded high-water
  row, a regenerated subject pin, and the raise history relocated into the row's comment. The row
  goes on `tools/memory-tree/BUILD-METHOD.template.md`, not on the rendered guide, for the four
  measured reasons in §4. Recovers about 950 B in a file with 12 B free. Costs about 1.28 s a bar.
  Leaves the adopter-side gap open for `TOOL-dSpentCeiling-4`.
- **(b) Delete it.** Drop the passage and let `GUIDE_CAP_BYTES` govern the rendered copy. Recovers
  1101 B, which is 151 B more than (a). Closes the adopter question by removing the claim. Against
  it: 61440 is 2.5x the current size, so 36887 B of slack means "the guide cap governs" is
  functionally "no ceiling for a long time"; the template itself stays capped by nothing at all; and
  the stated reason for the budget, that M7 re-reads this file whole at every pass boundary, is a
  real reason that survives the deletion of the sentence carrying it.
- **(c) Leave it.** The status quo. A constraint that binds whoever remembers to read the paragraph,
  on a file with 12 bytes free, whose own line 16 admits nothing enforces it. No argument is offered
  for this option because none was found.

*Recommendation: (a).* The seam exists, the codebase map already declares its extension recipe, the
cost is measured and small, the history is preserved rather than deleted, and it recovers all but
151 B of what (b) recovers while keeping the constraint. (b)'s single genuine advantage is the
adopter half, and that advantage is `TOOL-dSpentCeiling-4`'s to bank properly rather than this
unit's to buy by deletion.

**F2 — the line half.** UNRESOLVED, and downstream of F1(a). `tools/check-template-size.sh` measures
bytes only and has no line arm, and `tools/check-line-length.sh` measures line LENGTH in characters
rather than line COUNT, so `≤350 lines` cannot be enforced by any existing seam. Check 6 does bound
the rendered guide's line count, at `GUIDE_CAP_LINES` 750, which is more than twice the declared 350.

- **Drop the line half.** The file already argues against it: at its own stated ~100 B prose line the
  bytes run out near line 316, so most of the 350 is headroom the bytes do not grant. Measured, the
  file is at 317 lines and 12 bytes free, which confirms the byte half binds first.
- **Keep it as an explicitly unenforced note.** Honest, but it re-creates in one line the state this
  unit exists to end.

*Recommendation: drop it.* A pair where one half is gated and the other is prose is the same defect
at half the size, and the file's own measurement says the line half never binds.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Design pass only, no target file edited.
- rev-2 · 2026-09-04 · folded the three spec-audit findings addressed to this unit, from
  `2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md`. **B3** — AC1 through AC4 presumed option
  (a) while §8 F1 stays unsigned; each is now split into an (a) half and a (b) half, the shape AC8
  already had. F1 is NOT resolved by this rev. **S1** — the unit stages `tools/gate-legs.json` and
  `memory/guides/BUILD-METHOD.md`, both watched on line 6 of `memory/guides/SESSION-KICKOFF.md`, with
  no re-stamp in scope; added S8 (branch-independent), its files-touched row, the
  `kickoff-manifest ratchet` leg in §7, and AC9. **A3** — AC2's 13-byte append could not go red on the
  landed tree, because S5 takes roughly 950 B out of the same file it appends to; the append is now
  sized from the post-S5 measurement as `24576 − M + 1`. Re-measured against source: the template at
  24564 B and 317 lines, its budget on line 8 and `No gate enforces the pair` on line 16, the ten
  `watch:` entries on `SESSION-KICKOFF.md:6`, `.githooks/pre-commit:54` running the staged arm
  unconditionally, and the two greps AC1(b) asserts both returning 0. AC7 was rescoped in the same
  pass: it named S5, which does not exist under option (b), and now names the cut under either
  branch with a floor below both recoveries. Every §8 fork stays UNRESOLVED and unsigned.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a byte ceiling for a document and enforce it with
a size gate"` ranked `check-template-size.sh [playbook]` as an affordance seam and returned the
inventory keys `template size <=48KiB`, `charter size` and `kickoff engine size <=18KiB` from
`gate-legs`. The seam this unit extends is named verbatim in `memory/map/features/playbook.md` under
"Reuse affordance": "check-template-size.sh subject resolution — reuse for gating ANY file's byte
size on the merge bar without writing a sibling script; extend via one `tools/gate-legs.json` entry
naming the subject alone, one row in `tools/template-size-limits.txt` giving its ceiling and the
reason for it, and one `--bump` to seed its high-water row." No new script is written. The dossier's
recipe is three carriers and the tree now needs four: `tools/govkit/subject-pins.tsv` is a generated
per-leg pin that did not exist when that affordance was written, verified by finding `charter size`,
`kickoff engine size <=18KiB` and `template size <=48KiB` at its lines 21, 43 and 94.

Recall terms used: `python tools/memory-recall/query.py "why does a document declare its own byte
ceiling in prose instead of taking a row in the declared size registry" --terms "template-size-limits
high-water ratchet declared ceiling GUIDE_CAP_BYTES rendered template parity gate-legs leg subject
BUILD-METHOD budget uncapped"` — 40 hits, of which `TOOL-aScouredKit-23`, `TOOL-dSpentCeiling-4`,
`TOOL-dFoldedVerdict-7`, `TOOL-aDeclaredCeiling-1` and `memory/map/features/playbook.md:105` are the
records that bind this change.
