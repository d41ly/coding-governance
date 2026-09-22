# TOOL-dFoldedVerdict-6 — the compression pass, and what it measured instead

**Serves:** journal TOOL-dFoldedVerdict-6

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## The headline is the measurement, not the saving

The pass ran over every section of the protocol against S2's three safe classes and S3's six
never-cut categories. **It saved 16 bytes.** 54621 to 54605.

That is not a failed pass, it is the pass's finding, and S8 is what makes it reportable rather than
embarrassing: *no byte target is set, and none is accepted.* Had one been set, the only way to hit it
would have been to cut S3-protected text.

**The document contains no duplicated prose, and that is measured rather than asserted.** A
near-duplicate scan over its 85 substantive paragraphs — Jaccard over lowercased word sets, five
characters and up — found **zero pairs above 0.30 similarity and a maximum of 0.267**. The one pair
at that maximum is the only genuine class-1 restatement in fifty-four kilobytes: §1 and §10 both say
a directive points into a `BUILD-METHOD.md` section. §1 now cites §10 for the definition and keeps
only its own rule, which is that `--preflight` refuses a tree where the file is absent.

The second cut is class 3, local redundancy: a sentence that restated its own subject.

**So the owner's reading — "genuinely too prose-heavy" — is about DENSITY, not redundancy.** Every
long passage sampled carries a rule, a measurement, a stated cost, a refusal's reason, a "what this
does NOT do" clause, or a liveness assertion. S3 forbids cutting all six, and it is right to: those
are the sentences the document exists for. The verbosity that remains is the price of stating them.

## What else this unit did

**S6 — the severed sentence is REPAIRED, and recorded as a repair.** At the pre-image
`--close` BLOCKS on any unmet item. The override is named (it cites the item), recorded (it writes a`
ran straight into an inserted paragraph about `--attest`, and the sentence resumed six lines later
with `parked entry), and surfaced in the wrap-up.` Both halves of the pair carried it identically,
because they are byte-identical — which is precisely the class the protocol's own header warns
about: two legs compare the copies TO EACH OTHER, so a defect false in both is green forever. The
inserted paragraph now follows the completed one. Nothing was cut.

**S9 — `KIT_UNATTENDED_VERSION` moves ONCE, from 1.14 to 1.15, and it moves here.** Owner ruling of
2026-09-01: one release for an adopter, not six. The carrier population was DERIVED from
`tools/check-kit-versions.sh`'s own globs rather than counted from a spec — three shell files
carrying the constant AND a same-line marker, plus every `tools/unattended/*.template.md`, which is
now FOUR files because `TOOL-dFoldedVerdict-5` added the verb carrier. Ten markers across seven
files, then the adopter re-rendered all four installed copies. A count typed into a spec would have
said three templates.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-6

- **AC1** — every cut is recorded with its `S2` class above, and there are two of them. A cut with
  no class named is a deletion, and none was made.
- **AC2** — `diff` reports the protocol pair byte-identical after the pass, so check 10 is satisfied
  over both halves.
- **AC3** — the severed sentence reads whole after the repair; the inserted `--attest` paragraph
  moved below the completed one rather than through the middle of it.
- **AC4** — `bash tools/check-kit-versions.sh` exits 0 at 1.15, and `git grep -l 'unattended@1.14'`
  outside `memory/builds/` returns NOTHING, so no carrier was left behind.
- **AC5** — the `## 8[.]` conf-key anchor is 30, not the 29 this spec pinned, and the spec was right
  to make the expectation RELATIONAL rather than absolute. `TOOL-dFoldedVerdict-2` added `DISPOSITION_CUTOFF`
  to that table at order 3, exactly as its S12a said it would. The anchor is compared against THIS
  unit's pre-image, which is 30, and it is still 30 after the pass.
- **AC6** — all seven machine-read anchors resolve after the pass: the `RUN.<phase>.<blob8>.md`
  literal, the `in run order:` and `PASS kinds:` line shapes, the spelled-out core count still
  reading `Twelve kit-owned core items.`, the twelve DoD item rows, the section-8 key table at 30,
  and both `BUILD-METHOD.md` literals.
- **AC7** — `bash tools/unattended/adopt-unattended.sh --check` reports `unattended: in sync` over
  all four rendered artifacts after the version moved.
- **AC8** — `bash tools/memory-tree/check-memory-hygiene.sh` names no failing check; the protocol is
  54605 bytes against `GUIDE_CAP_BYTES` of 61440, with 6835 bytes of headroom that
  `TOOL-dFoldedVerdict-5` created at order 1.
- **AC9** — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0, which is check 6 over the
  guide caps. Same observation as AC8 and recorded once, under both numbers rather than under
  neither.
- **AC10** — `sed -n '/BLOCKS on any unmet item/,+1p'` over the render prints the two consecutive
  lines that now complete the sentence: `The override is named (it cites the item), recorded (it
  writes a` / `parked entry), and surfaced in the wrap-up.` S6's repair, observed on the record
  rather than on the diff.
- **AC11** — OWED to the closing review, which must scope itself `<BASE>..<HEAD>` over the two
  protocol halves. Not claimable here: it requires that review's scope line to name that range over the two protocol halves rather than the post-image, and its
  finder brief to name S3's six never-cut categories. A review handed the RESULT reads a fluent
  document with nothing to compare it against, which is how a dropped claim survives one pass. Marked
  as owed rather than asserted, because this ledger is written before that review runs.
- **AC12** — the derived marker probe prints exactly ONE line, `gov:kit unattended@1.15`, and the
  same command run against this unit's PRE-IMAGE prints exactly one line reading `1.14`. Both halves
  matter and neither substitutes for the other: one line is AGREEMENT, a different value is
  MOVEMENT, and `check-kit-versions.sh` can only see the first.
- **AC13** — `bash tools/check-kit-versions.sh` exits 0 and
  `bash tools/unattended/adopt-unattended.sh --check` reports `unattended: in sync`. That is the
  AGREEMENT half, stated separately from AC12 on purpose: a criterion that reads as proof of a bump
  while only proving agreement is the shape the round-1 audit named three times in this spec set.

## What this pass did NOT do

It did not touch `memory/guides/UNATTENDED-VERBS.md`. That carrier is `TOOL-dFoldedVerdict-5`'s and
N1 excludes it; the handoff is written in both specs rather than assumed.

It did not correct any rule it found reading as wrong. F1 resolved to FILE those, so that a reviewer
of this diff never has to separate "this claim was cut" from "this claim was changed" over the same
hunks. S6's repair is the one exception and it is a severed sentence, not a rule.

**It did not hit a byte target, because none exists.** If a future pass wants this document
materially smaller, the honest route is the one `TOOL-dFoldedVerdict-5` took: move a section out to
its own carrier. Compression of what remains buys tens of bytes and risks a claim.
