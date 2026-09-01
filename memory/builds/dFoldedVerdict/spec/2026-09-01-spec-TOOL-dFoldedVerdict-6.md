# TOOL-dFoldedVerdict-6 — the whole-document compression pass

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Recover headroom in the unattended protocol by removing words without removing claims, over the
document that remains once `TOOL-dFoldedVerdict-5` has moved the verb list out. This unit specifies a
METHOD and a review discipline, not a list of edits: the danger here is not that too little is cut,
it is that a claim is cut, and the two parity legs that grade this file cannot tell the difference.

## 2. Scope (IN)

- **S1 — THE CONSTRAINT, and it governs every item below. A compression that DROPS OR REVERSES A
  CLAIM is a defect far worse than the verbosity it removes.** The protocol's own header says two
  legs byte-compare this file against the template it ships from, and that they compare the two
  copies TO EACH OTHER — so a claim false in BOTH is green, forever. Three defects survived exactly
  that way, and a fourth is live at BASE: `memory/guides/UNATTENDED-PROTOCOL.md:336` opens the
  sentence "The override is named (it cites the item), recorded (it writes a", an inserted paragraph
  runs from `:337` to `:342`, and the sentence resumes at `:344` with "parked entry), and surfaced in
  the wrap-up." Both copies carry it identically, because they are byte-identical. Nothing on the
  merge bar sees any of this. The reviewer is the only instrument, which is why S5 exists.
- **S2 — three classes of passage, and ONLY these three, are safe to cut.** A passage that RESTATES
  something stated elsewhere in the same document, where the surviving statement is complete on its
  own and can be cited by section and line. A passage that NARRATES THE HISTORY of a rule whose
  statement survives without it — "this said X for four kit versions", "an earlier revision of this
  line called the verb …" — where the rule as it now stands loses nothing. And genuine local
  redundancy: a restated subject, a doubled connective, a parenthetical that repeats its own clause.
- **S3 — six things may NEVER be cut, and this list is exhaustive rather than illustrative.** A RULE:
  anything a run is bound by, including every refusal, permission and ordering. A MEASUREMENT: any
  number observed against this tree or this corpus. A stated COST: section 1's three spends and its
  five trades, and section 9's whole reduction. A REFUSAL'S REASON: why a check refuses, and why a
  rejected design was rejected. A "what this does NOT do" clause, which is the charter's own rule
  that a gate's header states its blind spot. And a LIVENESS assertion. A passage that is BOTH
  history and one of these six is kept.
- **S4 — every cut is checked against the PRE-IMAGE, one at a time.** For each removed hunk the
  builder records which of S2's three classes it falls in, and — for the first class — the section
  and line of the statement that survives it. A cut with no class named is not a cut, it is a
  deletion, and it is reverted rather than argued for.
- **S5 — the reviewer is handed the DIFF, never the result.** The closing review's scope line names a
  `<BASE>..<HEAD>` range over the two protocol halves, so a lens reads what LEFT the document. A
  reviewer handed the compressed file reads a fluent document and has nothing to compare it against;
  that is how a dropped claim becomes invisible in one pass.
- **S6 — the split sentence at `:336`/`:344` is REPAIRED, and the repair is recorded as a repair and
  not as a cut.** It is a pre-existing defect this unit's own reading found; folding it in silently
  would make the diff harder to review, which is the opposite of S5.
- **S7 — every machine-read anchor in the document still resolves after the pass.** They are
  enumerated in §4 and each is a literal or a line shape that a rewording breaks. This is the ONLY
  machine half a compression has, and it covers six literals out of a fifty-three-kilobyte document.
- **S8 — no byte target is set, and none is accepted.** §6 asserts a property. The measured saving is
  recorded in the unit's build record AFTER the pass, as an outcome.

## 3. Non-goals (OUT)

- **N1** — the new verb carrier `memory/guides/UNATTENDED-VERBS.md` and its template are OUT of this
  unit's subject. `TOOL-dFoldedVerdict-5` moves that text verbatim and this unit does not compress
  it, so the verb list is compressed by neither unit in this build. Its own budget is separate and
  its own headroom is large.
- **N2** — no section is renumbered, added, deleted or merged. The section structure is fixed by
  `TOOL-dFoldedVerdict-5`, whose §4 records the three costs of moving it.
- **N3** — no cap is moved, in the kit or in `.memory-tree.conf`.
- **N4** — no rule is CHANGED, softened or strengthened. A passage that reads as wrong is a finding
  for the build record, not an edit: correcting a rule is a different act from compressing prose, and
  mixing them makes the diff unreviewable, which is what S5 exists to prevent.
- **N5** — no script, conf, gate or Skill is touched. The subject is two markdown files.
- **N6** — the kit self-tests are not RUN. Nothing in §6 depends on them; §7 names what does.

## 4. Design

### Inventory — the caps that bind, and the current values

The binding cap is the GUIDE cap, not the INDEX cap. Both are declared at
`tools/memory-tree/check-memory-hygiene.sh:63`, the guide branch that swaps them in is `:493`, and
the comparison at `:503` is strictly greater, so a file sitting exactly ON the byte cap passes with
nothing to spare.

| Cap | Declared | Value at BASE | Overridden in `.memory-tree.conf`? |
|---|---|---|---|
| `GUIDE_CAP_BYTES` | `check-memory-hygiene.sh:63` | 61440 | no — the kit default holds |
| `GUIDE_CAP_LINES` | `check-memory-hygiene.sh:63` | 750 | no — the kit default holds |
| `INDEX_CAP_BYTES` | `.memory-tree.conf` | 61440 | yes, and it is NOT the cap on a guide |
| `INDEX_CAP_LINES` | `.memory-tree.conf` | 0 (retired) | yes |

The two BYTE figures are identical, which is why this cap is mis-attributed in this build's own prose
and in the `TOOL-dBriefedPass-8` backlog row, both of which name `INDEX_CAP_BYTES`. The LINE figures
are the discriminator: 750 for a guide, 0 — no independent line cap at all — for the index class.

Measured at BASE `adc0543c` by `wc -lc`, on two byte-identical files: `memory/guides/
UNATTENDED-PROTOCOL.md` is 61,440 bytes over 725 lines. That is ZERO bytes of headroom against 61,440
and 25 lines against 750. After `TOOL-dFoldedVerdict-5` removes lines 422 to 517 the remainder is
52,986 bytes over 629 lines, plus whatever its pointer stub costs. This unit therefore does NOT run
against a breach; it runs to buy budget for rules not yet written, which is exactly the pressure that
makes a byte target dangerous.

### Where the mass is

Measured per section at BASE. Section 7 is listed for completeness and leaves before this unit runs.

| Section | Bytes | Lines |
|---|---|---|
| preamble | 1071 | 18 |
| 1. The authorization | 8778 | 113 |
| 2. The run-state file | 9309 | 121 |
| 3. The phase vocabulary | 4012 | 60 |
| 4. The Definition of Done | 7487 | 42 |
| 5. The keepalive | 3404 | 44 |
| 6. Landing | 1593 | 23 |
| 7. The verbs | 8454 | 96 |
| 8. What a project declares | 4975 | 39 |
| 9. The boundary this kit claims | 3548 | 48 |
| 10. The default directive set | 3295 | 44 |
| 11. The adoption rule | 4050 | 56 |
| 12. The pass sequence is DRIVEN | 1465 | 22 |

Sections 1, 2 and 4 hold 25,574 bytes, roughly 48% of the post-split remainder. They are also where
sections 1 and 2 carry cost lists and section 4 carries the Definition-of-Done table, so the densest
sections are also the ones S3 protects most. That is the honest shape of this work.

### The prior estimate, and why it is a floor rather than a target

The build's own pre-spec probe reports about 2,965 bytes of exactly-identified verbatim cuts and
estimates 4,800 to 6,500 bytes for a careful pass. **UNVERIFIED here**: no record carrying those
figures is reachable in the tracked tree at BASE `adc0543c`, so this spec cites them as an input from
the build's orchestration rather than as a measurement it re-derived. Treat both as a FLOOR to
verify, never a target to hit. A byte target is precisely the pressure that makes someone cut a
claim, and this document has already paid once: `TOOL-dBriefedPass-5` funded one new section by
compressing fourteen passages across five sections, so the cheapest rewordings are already spent and
the remaining ones cost more judgement per byte.

### The machine-read anchors — the only tripwires a compression has

Each was verified at BASE by running the named extractor against the live document. A rewording that
breaks any of these reds a leg, which is the good case; everything NOT in this table is graded by a
reader alone.

| Anchor | Read by | Where in the document at BASE |
|---|---|---|
| the literal `RUN.<phase>.<blob8>.md` | `check-unattended.sh:1267` | line 154 |
| a line ending `in run order:`, then the next paragraph's backticked ALL-CAPS tokens | `check-unattended.sh:1568-1571` | line 255 |
| a line ending `PASS kinds:`, then the next paragraph's tokens | `check-unattended.sh:1586-1589` | line 260 |
| `^<Word> kit-owned core items\.` — the spelled-out count above the table | `check-unattended.sh:1625` | line 315, currently `Twelve` |
| every line matching `^\| \`[a-z][a-z-]*\` \|` — the DoD item names | `check-unattended.sh:1612` | 12 rows in section 4 |
| the `^## 8[.] ` heading, then each row's FIRST table cell | `check-unattended.sh:1293` | 29 conf keys in section 8 |
| a line `- ?<verb>? — ` per declared verb | `check-unattended.sh:2046` | moves to the new carrier at order 5 |
| the literal `BUILD-METHOD.md` | `check-method-carriers.sh` registry row `:16` | lines 119 and 608 |

The last row is the one most likely to be tripped by an honest compression. `memory/project/
method-carriers.txt:16` declares `tools/unattended/PROTOCOL.template.md` a carrier because section 1
names the build method a run-time dependency and section 10 names it the target every directive
points into. Check 4 of that gate reds when a declared row stops hitting, so cutting either sentence
turns a registry row stale and reds `method carriers (every pointer declared)`.

### Method — the pass, in order

1. Pin the pre-image: `git rev-parse HEAD` after `TOOL-dFoldedVerdict-5` lands, and keep the blob.
2. Read the document whole, once, marking candidate passages by S2 class. Nothing is edited on this
   pass; a compression made while reading is a compression nobody classified.
3. Edit the TEMPLATE half. The installed half is produced from it, never edited in parallel — two
   hand edits are how two copies stop agreeing while their parity leg stays green.
4. Per hunk, record the class and — for class one — the surviving statement's section and line.
5. Re-run the anchor extractors in the table above, each as its own command, before any gate.
6. Re-install the pair and run the two parity legs.
7. Hand the reviewer the diff, per S5.

### Alternatives rejected

**A byte target, or a percentage.** Rejected on the stated failure mode: a target converts every
remaining passage into a candidate and rewards the builder for cutting the ones that are hardest to
defend, which are the measurements and the refusal reasons.

**Compressing by section, one commit each.** Rejected: the class-one test — "this restates something
stated elsewhere in the SAME document" — is a whole-document question, and a per-section pass cannot
answer it without re-reading the whole document each time anyway.

**Trusting the parity legs.** Rejected by the document's own header, and by the count: three defects
survived that way and this unit's own reading found a fourth.

### Files touched (estimate)

`tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, in one commit or
neither. The unit's build record under `memory/builds/dFoldedVerdict/build/` carries the per-hunk
classification S4 requires.

## 5. Production-readiness checklist

- security — N/A. No code, no write path, no input. The one adjacent risk is a compression that
  weakens section 9's statement of what this kit does NOT close; S3 forbids it explicitly.
- perf / scale — N/A. A smaller document is cheaper to read, which is the whole point, and no gate's
  cost changes measurably.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — N/A. Nothing executes.
- observability — the per-hunk classification in the build record IS the observability, and it is the
  only record of what left the document.
- risks — one, and it dominates: a dropped or reversed claim, green in both copies. S2, S3, S4 and S5
  are four independent controls on that one risk and none of them is machine-enforced.
- testing + left-shift gates — no new gate. Nothing here can be gated: a checker that could tell a
  restatement from a claim would be reading prose for meaning. Said plainly rather than implied away,
  which is the same disclosure this kit's own parity legs carry in their headers.
- migration / rollback — one commit over two files; `git revert` restores the pre-image exactly.
- user docs — N/A. The protocol is the doc.

## 6. Acceptance criteria

Every criterion below asserts a PROPERTY. None names a number of bytes saved, deliberately.

- **AC1** — When `git diff <BASE>..HEAD -- tools/unattended/PROTOCOL.template.md` is read hunk by
  hunk, every removed hunk is named in the unit's build record with one of S2's three classes; and
  for every class-one hunk that record cites, by section and line, the statement that survives it.
  A hunk with no class named appears nowhere in the diff.
- **AC2** — When the build record's class-one citations are checked against the post-image with
  `grep -n`, every cited surviving statement is present in the shipped document.
- **AC3** — When `diff tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  runs, it reports no difference — the two copies are the same document, edited once.
- **AC4** — When `wc -lc memory/guides/UNATTENDED-PROTOCOL.md` runs, the byte count is strictly below
  61440 and the line count is at or below 750, and both figures are lower than the post-split
  measurement `TOOL-dFoldedVerdict-5` recorded.
- **AC5** — When the four in-document anchor extractors named in §4 are re-run against the shipped
  document, each yields exactly what it yielded at BASE, and each observation is recorded in the
  build record beside the command that made it. The conf-key extractor, anchored on the
  `## 8. What a project declares` heading, yields 29 keys. The Definition-of-Done row extractor
  yields 12 item names. The count sentence still opens `Twelve kit-owned core items.` The archive
  grammar literal `RUN.<phase>.<blob8>.md` is still present at its section 2 sentence.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs, it exits 0. That carries checks
  10, 16 and 22, which is every machine reader of this document's own prose.
- **AC7** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports
  `unattended: in sync`, which is the second parity leg over the same pair.
- **AC8** — When `bash tools/memory-tree/check-method-carriers.sh` runs, it exits 0, which asserts
  the registry row for `tools/unattended/PROTOCOL.template.md` still hits — the compression did not
  cut either `BUILD-METHOD.md` citation.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it exits 0, which is check 6
  over the guide caps.
- **AC10** — When `sed -n '/BLOCKS on any unmet item/,+1p' memory/guides/UNATTENDED-PROTOCOL.md` is
  read, the sentence that begins "The override is named" completes on consecutive lines rather than
  resuming after an intervening paragraph. This is S6's repair, observed.
- **AC11** — When the closing review record for this unit is read, its scope line names a
  `<BASE>..<HEAD>` diff range over the two protocol halves rather than the post-image file, and its
  finder brief names S3's six never-cut categories. A review handed the result instead of the diff
  does not satisfy this unit, whatever its verdict.

## 7. Gates

Named legs, each resolving in `tools/gate-legs.json`:

- `unattended kit gate` — checks 10, 16 and 22, the parity pair and every prose anchor a machine
  reads in this document.
- `unattended skill wiring` — the adopter's own byte-compare of the installed half.
- `memory hygiene` — check 6's guide caps.
- `method carriers (every pointer declared)` — the registry row that goes stale if either
  `BUILD-METHOD.md` citation is cut.

Deliberately NOT named, with the compensating check stated because an exemption is not coverage:
`codebase-map coverage + freshness` is unaffected because this unit adds and removes no inventory
key, and `harness arms (fail branches armed or pinned)` is unaffected because it touches no script.
The compensating check for everything these four legs cannot see is AC1, AC2 and AC11 — a human
reading the diff — and there is no machine substitute for it.

## 8. Open questions

- **F1 — is a rule that reads as WRONG corrected here, or filed?** Options: fold the correction into
  this pass, or record it and leave the text. RECOMMENDATION: file it. N4 already says so and the
  reason is the diff: a review that must separate "this claim was cut" from "this claim was changed"
  over the same hunks is a review that finds neither reliably. A correction is its own unit with its
  own record. The exception is S6, which is not a rule correction but the repair of a sentence
  physically severed by an insertion.
- **F2 — does the pass edit the template half only, or both halves in parallel?** Options: edit the
  template and re-install, or hand-edit both. RECOMMENDATION: the template only, then re-install.
  Hand-editing both is how two copies stop agreeing, and the leg that would catch it compares them to
  each other, so it catches a divergence and never a shared error.
- **F3 — FACT-QUESTION · is the ~2,965-byte figure reproducible in this tree?** The probe:
  `git log --all --oneline -S'2,965' -- memory/` and a `git grep` for the figure across every ref, run
  before the pass begins. The observation that decides it: whether any tracked or reachable record
  carries the measurement. LIVENESS: the same probe run for `61440` returns hits at BASE, so it can
  produce a positive and its negative is therefore informative. If the record does not exist, the
  figure stays cited as UNVERIFIED input and this unit re-derives its own saving from `wc -c` before
  and after, which is the number §6 records anyway.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. The caps, the per-section byte table, the anchor table and the
  split sentence at lines 336 and 344 were each verified at BASE `adc0543c` by reading or running the
  named source. The 2,965 and 4,800-to-6,500 figures are carried as UNVERIFIED input, per §4.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "splitting a capped governance document into a second
byte-compared carrier file"` was run for this build's spec set and returned 39 candidates; **no
existing seam fits this unit**, and the evidence is that none can. Every candidate it named is a
symbol or an affordance seam, and this unit adds no code: its deliverable is a method for editing two
markdown files and a review discipline over the diff. The nearest thing to prior art in this tree is
the compression `TOOL-dBriefedPass-5` performed on this same document — fourteen passages across five
sections, recorded at `memory/builds/dBriefedPass/build/2026-09-01-build-TOOL-dBriefedPass-5-1-carriers.md:25-29`
— and that is a precedent to learn the cost from rather than a seam to extend, because it left no
reusable mechanism behind and no per-hunk classification. What this unit reuses instead is the set of
anchor extractors already living in `tools/unattended/check-unattended.sh`, cited line by line in §4;
they are not extended, they are the tripwires the pass is run against.

Recall terms used: `python tools/memory-recall/query.py "why is the unattended protocol capped and
what decided how a second byte-compared carrier file is registered" --terms "unattended protocol
GUIDE_CAP_BYTES index cap parity leg check 10 byte-compare PROTOCOL.template.md adopt-unattended
kit.toml rendered artifact verb carrier check 26 guides inventory"` — 39 hits. The three that decided
this design are the `TOOL-dBriefedPass-5` closing review's cap attribution and its zero-headroom
measurement, the `TOOL-dBriefedPass-8` backlog row recording the three options the owner was shown,
and the `TOOL-dBriefedPass-5` carriers record naming the fourteen-passage compression already spent.
