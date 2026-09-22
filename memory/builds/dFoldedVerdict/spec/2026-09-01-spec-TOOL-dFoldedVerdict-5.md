# TOOL-dFoldedVerdict-5 — section 7 becomes its own carrier

**Status:** CLOSED · rev-4 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-TOOL-dFoldedVerdict-5-1-verb-carrier.md](../build/2026-09-01-build-TOOL-dFoldedVerdict-5-1-verb-carrier.md) | journal | — |
| [2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md) | spec-audit | TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-6 |
| [2026-09-02-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-closing-diff-round1.md](../reviews/2026-09-02-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-closing-diff-round1.md) | diff-review | TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-6 |

<!-- /gen:spec-records -->

## 1. Goal

Move the unattended protocol's fastest-growing section — the verb list — out of a file that renders
at exactly its cap, into its own byte-compared carrier pair. The move recovers 8,454 bytes of
headroom in the contract every unattended run reads whole. The work is not the move: it is the set of
readers that resolve a verb against that section today, each of which must be repointed in the same
commit or the bar reds on a section that no longer holds what it is asked for.

## 2. Scope (IN)

- **S1** — a new kit source `tools/unattended/VERBS.template.md`, carrying the whole of the
  protocol's section 7 body: the eighteen `- \`--verb\` — …` bullets, moved VERBATIM. It opens with a
  `<!-- gov:kit unattended@<version> -->` marker and one H1, and nothing else is added or reworded.
  The marker is mandatory rather than decorative: `tools/check-kit-versions.sh:159` globs
  `tools/unattended/*.template.md` and reds a template carrying no marker at all, and `:168` reds one
  whose version disagrees with `KIT_UNATTENDED_VERSION`.
- **S2** — a new installed copy `memory/guides/UNATTENDED-VERBS.md`, byte-identical to S1 after the
  same CR normalisation check 10 already applies to the protocol pair. The `memory/guides/` location
  is chosen, not incidental: `tools/memory-tree/check-memory-hygiene.sh:449` selects
  `^memory/guides/[^/]+\.md$` into the index set, so the new file inherits the guide caps in S4's
  table without any conf edit.
- **S3** — the protocol keeps `## 7. The verbs` as a heading whose body is a POINTER at the new
  carrier and nothing else. Sections 8 through 12 are NOT renumbered, for the three reasons in §4.
- **S4** — `tools/unattended/check-unattended.sh` check 10 gains the second pair. Today it holds one
  hard-coded `SHIP`/`LIVEDOC` comparison at `:1248-1260`, including the arm that refuses when either
  half is missing because "a parity check with one file is a check that cannot fail". The second pair
  needs that same both-halves refusal, so it is added as a row rather than as a copy.
- **S5** — check 26's protocol arm is repointed. At `:2032-2033` it reads `$SHIP` — which is
  `tools/unattended/PROTOCOL.template.md`, bound at `:1248` — and at `:2046` it requires a line
  matching `- ?<verb>? — ` for each of the eighteen declared verbs. That arm reads the WHOLE file, not
  section 7, so after the move it fails eighteen times unless it is pointed at the new carrier.
- **S6** — `tools/unattended/adopt-unattended.sh` installs and `--check`-compares the new pair, in the
  shape it already uses twice. The install path is `:283-288` and the two `--check` refusals — NOT
  INSTALLED and DRIFTED kept as separate messages — are at `:268-273`.
- **S7** — `tools/unattended/kit.toml` gains one `[[files]]` row with `role = "rendered"`,
  `to = "{memory_root}/guides/UNATTENDED-VERBS.md"` and `placeholders = []`, and one `[[lf_pin]]` row
  for the installed half. The existing `[[lf_pin]] pattern = "{kit}/*.md"` already covers the kit
  half.
- **S8** — `tools/unattended/SKILL.template.md:9` says "The binding contract is
  `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`". That sentence names both carriers after this
  unit, and the rendered `.claude/skills/unattended/SKILL.md` is regenerated so the wiring leg's
  byte-compare stays green.
- **S9** — `memory/map/features/unattended.md` claims the new inventory key. Its `guides = [...]` list
  at `:27` and its `[paths] globs` at `:31-35` both name only `UNATTENDED-PROTOCOL.md` today, and the
  `guides` inventory is machine-enumerated from `memory/guides/*.md` by
  `tools/codebase-map/map_extractors.py:119`, so an unclaimed new key reds the coverage gate. The
  generated map artifacts are re-rendered in the same commit.
- **S10** — two stale backlog rows are corrected rather than left to be re-read as true.
  `TOOL-dUnstalledConvoy-17` says section 7 "lists eight of them, omitting `--park` and `--attest`"
  and that "nothing joins it to the other three"; measured at BASE the section carries eighteen
  bullets covering every declared verb, and check 26 is the join. `TOOL-dBriefedPass-8` names
  `INDEX_CAP_BYTES` as the cap the protocol renders at; the binding cap is `GUIDE_CAP_BYTES`, and the
  two are numerically identical, which is exactly why the mis-attribution is invisible.
- **S11 — the `--review` bullet moves VERBATIM, false sentence and all, and its correction is
  handed forward one unit.** The bullet sits inside section 7 and is cited by SECTION rather than by
  a line number this move invalidates. At BASE `adc0543c` its sentence reads "at the exit every
  blocker still standing is promoted to a unit rather than parked", and it enumerates the verb's
  refusals as exactly three. Both halves go FALSE once `TOOL-dFoldedVerdict-1` makes `fold` a legal
  exit disposition and adds refusals. **Rev-1 through rev-3 read the sequence the other way round**,
  with unit 1 landing first and this unit amending the bullet mid-move as a backstop; the rev-3
  reorder inverts it. This unit is now order 1 and `TOOL-dFoldedVerdict-1` is order 2, so the
  pre-image DOES still carry the false sentence, and the correction lands one unit later inside the
  carrier this unit creates. The verbatim property is worth more than a one-unit exposure: AC2, AC3
  and AC14 all grade this move by byte-identity, and an amendment made during the move is the single
  edit that would make a pure move unverifiable. So the sentence is copied unchanged and AC13
  observes that it was. It does not survive the build — `TOOL-dFoldedVerdict-1` S9 names this
  carrier and its AC17 grades the corrected text there — which answers the original worry that the
  false sentence would acquire a second permanent home nothing revisits.
- **S12 — the handoff to `TOOL-dFoldedVerdict-6` is STATED, not assumed.** This unit MOVES section 7
  and rewords nothing in it beyond S11's single bullet. `TOOL-dFoldedVerdict-6` compresses the
  REMAINDER of the protocol and does not touch the new carrier. The two units share an author and one
  file, which is where a handoff is likeliest to be assumed rather than written, so it is written
  here and in that unit's S10. The kit version bump belongs to that unit and not to this one, per N9.
- **S13 — the protocol sanctions the provenance form, in one sentence.** Owner ruling of 2026-09-01,
  taken on `TOOL-dFoldedVerdict-3` Q2. `memory/guides/UNATTENDED-PROTOCOL.md:167` says the run-state
  file's authored half carries the declared facts "and nothing else", while four landed records
  already carry a hand-reconstructed key with a `-source:` line stating why no verb could write it —
  so the corpus already contradicts the clause and nothing enforces either side. The sentence admits
  a source-suffixed line whose value states why a verb could not write the key it names, and it says
  nothing about WHICH keys qualify. It lands in this unit rather than in `TOOL-dFoldedVerdict-6`
  for two reasons and both are about the DIFF: this unit is order 1, so the permission exists three
  units before `TOOL-dFoldedVerdict-3` writes rows relying on it, and a one-sentence addition stays
  separable inside a diff that is otherwise a move, where in unit 6's document-wide compression a
  reader could not tell an addition from a reword. It goes in the run-state section and NOT in
  section 7, so N2's verbatim rule does not reach it — stated because a reader who sees this unit
  adding protocol prose will reach for N2 first. `TOOL-dFoldedVerdict-3` writes the rows and owns
  their correctness; this unit writes only the permission, and AC13a is the observation.

## 3. Non-goals (OUT)

- **N1** — the protocol's sections 8 through 12 are NOT renumbered. §4 gives the three costs.
- **N2** — no verb TEXT is reworded, with ONE named exception. This unit is a move; every byte of the
  eighteen bullets arrives in the new file unchanged. Compression of the protocol's REMAINDER is
  `TOOL-dFoldedVerdict-6`, and the new carrier is explicitly outside that unit's subject as well —
  the verb list is compressed by neither unit in this build. The exception is S11's `--review`
  bullet, and it is carved HERE rather than left to be discovered mid-move: a verbatim rule with no
  carved exception is what would force this unit to copy a sentence it knows to be false. No other
  bullet may be touched under it, and it is spent only if order 1 left that sentence false.
- **N3** — no verb is added, removed, renamed or re-ordered. `VERBS_SLUG` and `VERBS_INLINE` at
  `tools/unattended/unattended.sh:87` and `:90` are untouched.
- **N4** — `.gitattributes` is NOT edited. `memory/**/*.md text eol=lf` at `:47` and
  `tools/unattended/*.md text eol=lf` at `:140` already pin both new halves; adding a row would be a
  second spelling of a pin that already holds.
- **N5** — no cap moves. Neither `GUIDE_CAP_BYTES` nor `GUIDE_CAP_LINES` is touched, in the kit or in
  `.memory-tree.conf`. Raising a declared cap is the option the owner ruled against when this build
  was scoped, and M3 reserves a project declaration from a mandate's delegated authority anyway.
- **N6** — `ARMS_FLOORS` is not moved. Measured by `python tools/memory-tree/check-arms.py --report`
  at BASE: `tools/unattended/check-unattended.sh` carries 169 fail branches and 161 armed, against
  floors of 101 and 100. The floors are one-sided upward, so added branches cannot breach them.
- **N7** — no governance carrier is edited. `AGENTS.md` and
  `coding-governance-agents.template.md` name the protocol and not its sections, so the pointer they
  carry stays true; F3 in §8 is the fork about whether the new file should be charter-cited at all.
- **N8** — the kit self-tests are not RUN. §6 states how each arm is otherwise witnessed.
- **N9** — `KIT_UNATTENDED_VERSION` is NOT bumped here. Owner ruling of 2026-09-01, recorded in this
  build's README: the kit version moves ONCE, on the build's LAST landing unit, which is
  `TOOL-dFoldedVerdict-6`, so an adopter sees one release rather than six. This unit ADDS two
  carriers of the `gov:kit unattended@` marker, and both carry whatever version is live when it
  lands. The round-1 spec audit found three specs naming three different owners for this bump; the
  ruling settles it, and this spec states the ruling rather than restating what a sibling says.

## 4. Design

### Inventory — the caps that bind, and the current values

The binding cap is the GUIDE cap, not the INDEX cap. Both are declared at
`tools/memory-tree/check-memory-hygiene.sh:63`; the guide branch that swaps them in is `:493`, and
the comparison at `:503` is `b[f]+0>cb || (cl>0 && l[f]+0>cl)` — strictly greater, so a file sitting
exactly ON the byte cap passes with zero bytes to spare.

| Cap | Declared | Value at BASE | Overridden in `.memory-tree.conf`? |
|---|---|---|---|
| `GUIDE_CAP_BYTES` | `check-memory-hygiene.sh:63` | 61440 | no — the kit default holds |
| `GUIDE_CAP_LINES` | `check-memory-hygiene.sh:63` | 750 | no — the kit default holds |
| `INDEX_CAP_BYTES` | `.memory-tree.conf` | 61440 | yes, and it is NOT the cap on a guide |
| `INDEX_CAP_LINES` | `.memory-tree.conf` | 0 (retired) | yes |

The two BYTE figures are identical, which is why this cap has been mis-attributed in this build's own
prose and in `TOOL-dBriefedPass-8`. The LINE figures are the discriminator: the guide class carries
750 and the index class carries 0, meaning no independent line cap at all. A guide is therefore bound
on both axes and an index shard on one.

Measured at BASE `adc0543c` with `wc -lc`, on files that are byte-identical to each other:

| File | Bytes | Headroom | Lines | Headroom |
|---|---|---|---|---|
| `memory/guides/UNATTENDED-PROTOCOL.md` | 61440 | 0 | 725 | 25 |
| `tools/unattended/PROTOCOL.template.md` | 61440 | n/a — not a guide | 725 | n/a |

Section 7 spans lines 422 to 517 and measures 8,454 bytes over 96 lines. Removing exactly that range
leaves 52,986 bytes over 629 lines, so the stub in S3 is written against 8,454 bytes of recovered
budget minus its own size. The new carrier's own cap is the same guide pair — 61,440 bytes and 750
lines — so at roughly 8.7 KB and 100 lines it lands with about 52 KB and 650 lines of headroom, which
is the property this move buys: the section that grows once per verb stops sharing a budget with the
contract.

### The readers that resolve a verb against section 7, enumerated by reading

Each row was found by reading the named source at BASE, not by grep alone. The two rows marked *no
action* are stated because a reviewer would otherwise have to re-derive that they are safe.

| Reader | What it resolves | Where | Must be repointed to |
|---|---|---|---|
| `check-unattended.sh` check 26 | for each of 18 declared verbs, a line `- ?<verb>? — ` in `$SHIP` | `:2032`, `:2044-2049` | the new kit template, and it must REFUSE when that file is absent |
| `check-unattended.sh` check 10 | byte parity of the protocol pair | `:1248-1260` | a second pair row, carrying the same both-halves refusal |
| `adopt-unattended.sh` | installs the pair, and `--check` byte-compares it | `:183-190`, `:268-273`, `:283-288` | a third artifact, on the `PLAYBOOK-TEMPLATE` shape |
| `check-kit-versions.sh` | every `tools/unattended/*.template.md` carries a matching marker | `:159-171` | nothing — but the new template must CARRY the marker or the leg reds |
| `check-memory-hygiene.sh` check 6 | the guide caps, over `memory/guides/*.md` | `:449`, `:493`, `:503` | nothing — the new file is graded automatically, which is the point of S2's location |
| `map_extractors.py` `guides` | the `memory/guides/*.md` inventory | `:119` | the dossier `memory/map/features/unattended.md`, both its `guides` list and its `[paths] globs` |
| `SKILL.template.md` | names the ONE binding contract to a reading agent | `:9` | both carriers, and the render regenerated |
| `check-unattended.sh` check 22 | the conf-key table, anchored on `^## 8[.] ` in the live doc | `:1293` | nothing, PROVIDED §8 keeps its number — see N1 |
| `govkit.py selfcheck` | every kit source is claimed by a declared role rule | arm 3, arm 4 | nothing — the `include = "**"` engine row already claims the kit half; the `[[files]]` row in S7 declares the destination |
| `check-method-carriers.sh` | *no action.* Its registry row for `PROTOCOL.template.md` stays valid: the two `BUILD-METHOD.md` literals sit at protocol lines 119 and 608, both OUTSIDE 422-517 | registry `:16` | nothing, and the new file must not acquire that literal without a registry row |
| `kit-dogfood-parity.test.sh` | *no action.* Its `PAIRS` at `:53` holds only the three memory-tree pairs; the unattended pairs are check 10 and the adopter | `:53` | nothing |

### The ordinal trap, stated because it is invisible in a diff

`check-arms.py` assigns each `fail` branch an ordinal by line order WITHIN its check number
(`check-arms.py:150-163`), and `memory/project/unarmed-branches.txt` pins eight rows for this file:
check 2 branches 9, 10 and 11, and check 16 branches 13 through 17. Inserting a `fail` branch ABOVE a
pinned one renumbers every pin below it at once, and the resulting message reads like a rewording
rather than an insertion. Checks 10 and 26 carry no pinned rows, so S4 and S5 are safe; a builder who
decides to touch check 16 instead is not.

### The `--review` bullet, and why this unit observes it

The bullet is the one passage in section 7 whose truth changes under this build. Two properties of
the machinery make it worth a criterion rather than a note.

Check 10 compares the two copies of a pair to each other, and its own header at
`tools/unattended/check-unattended.sh:1244-1247` says a parity leg is a copy check. A sentence false
in BOTH halves is green forever. This unit CREATES a second such pair, so at rev-2 the worry was
that a falsified sentence copied here acquires a second permanent home nothing later reads — the new
carrier being out of `TOOL-dFoldedVerdict-6`'s subject by that unit's own N1.

**The reorder answered that worry without a criterion.** This unit is order 1 and
`TOOL-dFoldedVerdict-1` is order 2, so the sentence is read and corrected one unit later, in this
carrier, and graded there by that unit's AC17. What remains for this unit is the opposite assertion
from the one rev-2 wrote: AC13 now observes that the bullet arrived UNCHANGED, because a mid-move
amendment is the one edit that would defeat AC2, AC3 and AC14, which grade this move by
byte-identity. AC14 is the same discipline applied to the move as a whole.

Owner ruling of 2026-09-01: at CEILING the driver accepts EITHER disposition, because a forced value
is a constant and a constant is not evidence for the clause that reads it. That permits something
`memory/guides/BUILD-METHOD.md` M4 does not describe — M4's sentence says a run reaching the runaway
ceiling promotes and lands anyway, and names no fold there. The corrected bullet must therefore
describe a CEILING exit that admits both dispositions, or the contract a run is measured against
disagrees with the driver measuring it. What that sentence SAYS is `TOOL-dFoldedVerdict-1`'s to
write; AC13 only observes that it no longer says the false thing.

### Alternatives rejected

**Renumbering sections 8 through 12 down to 7 through 11.** Rejected on three verified costs.
`check-unattended.sh:1293` anchors the conf-key join on `^## 8[.] `, so check 22 would grade the
wrong section or an empty one. `SKILL.template.md:93` cites "protocol section 12" and `:756` cites
"protocol section 9"; both become false, and neither is machine-joined, so both would go stale
silently. And thirteen internal `§N` cross-references inside the protocol point at 1, 3, 4, 5, 8, 9
and 10, every one of which would need re-checking by hand against a document whose own parity leg
cannot tell a wrong number from a right one. The stub costs one paragraph and breaks nothing.

**Letting check 26 accept a hit in EITHER file.** Rejected: a half-completed move — the new file
created, the protocol section not emptied — would then pass, which is the exact state the leg exists
to catch. F1 in §8 carries the decision.

**Raising `GUIDE_CAP_BYTES`.** Not this unit's to take. It is a kit-shipped default and a project
declaration, and M3's veto 2 reserves a change to a governance carrier from a mandate's delegated
resolver authority. The owner ruled for the split when this build was scoped.

### Files touched (estimate)

`tools/unattended/VERBS.template.md` (new) · `memory/guides/UNATTENDED-VERBS.md` (new) ·
`tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` (the section
becomes a stub, in both halves or neither) · `tools/unattended/check-unattended.sh` (checks 10 and
26) · `tools/unattended/check-unattended.test.sh` (arms for the new branches) ·
`tools/unattended/adopt-unattended.sh` · `tools/unattended/kit.toml` ·
`tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` ·
`memory/map/features/unattended.md` and the generated map artifacts · `memory/backlog/TOOL.md`.

`tools/unattended/unattended.sh` is NOT edited. At rev-1 this list named it and "every
`gov:kit unattended@` marker" as the version bump, which is a deliverable no §2 item here ever
scoped and which owner ruling (b) assigns to `TOOL-dFoldedVerdict-6`. The row is deleted rather than
left to read as covered. See N9.

## 5. Production-readiness checklist

- security — N/A. No new write path, no new input, no change to the authorization or landing rules.
- perf / scale — N/A. Two file reads replace one in check 10 and check 26; both are already reading
  the whole file into a shell variable once.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — the both-halves refusal is the empty state and is required, not
  optional: a parity check with one file cannot fail, which check 10's own message already says.
- observability — every new refusal names both the file it read and the verb or pair it was grading,
  matching the messages already in that file.
- risks — the one real risk is a HALF-MOVE: the new carrier lands and the protocol section is not
  emptied, or the reverse. F1's resolution is what makes that state red rather than green.
- testing + left-shift gates — the new `fail` branches are armed in
  `tools/unattended/check-unattended.test.sh` by positive assertions naming each branch's own failure
  text. Those arms are WRITTEN and NOT RUN: a standing owner instruction forbids running this kit's
  self-test suites. `check-arms.py` reads the test file's TEXT statically
  (`check-arms.py:167-187`), so `harness arms` grades the arms without executing them, and that is
  how they are witnessed here.
- migration / rollback — the move is a single commit touching both halves of two pairs. Reverting it
  restores a green tree, because the caps it leaves behind are the caps it started from.
- user docs — the Skill sentence in S8 is the user-facing half; there is no `help/` page for this kit.

## 6. Acceptance criteria

- **AC1** — When `wc -lc memory/guides/UNATTENDED-VERBS.md tools/unattended/VERBS.template.md` runs,
  both halves report the same byte and line counts, and both sit under 61440 bytes and 750 lines.
- **AC2** — When `diff tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs, it
  reports no difference.
- **AC3** — When the new carrier is searched for check 26's own bullet shape — a list marker, one
  sentinel character, the verb, one sentinel character, then the em-dash separator — it yields 18
  bullets, the same count `sed -n '422,517p' memory/guides/UNATTENDED-PROTOCOL.md` yields over the
  pre-image at BASE. Both counts are recorded in the unit's build record.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, it exits 0. That single command
  carries check 26's verb-carrier join over the NEW file and check 10's parity over BOTH pairs, which
  is the only observation that proves the repoint in S4 and S5 landed together.
- **AC5** — When the verb bullets are deleted from `tools/unattended/VERBS.template.md` and
  `bash tools/unattended/check-unattended.sh` is re-run, it exits non-zero naming check 26 and a
  verb; and when that file is deleted outright, it exits non-zero naming check 10 and the missing
  half. The break is staged and unstaged, never committed, and both observations are recorded in the
  unit's build record — a gate whose failing case has not been seen is an assertion about nothing.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs on a tree whose installed
  copy has been perturbed, it names `memory/guides/UNATTENDED-VERBS.md` and tells the reader to
  re-run the adopter; on an unperturbed tree it reports `unattended: in sync`.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it exits 0, which asserts the new template
  carries a `gov:kit unattended@` marker EQUAL to `KIT_UNATTENDED_VERSION`. It asserts agreement and
  never movement: the comparator at `tools/check-kit-versions.sh:159-171` compares each marker to the
  constant, so an unbumped kit satisfies it exactly as well as a bumped one. This unit does not bump
  the version (N9) and this criterion is not evidence that anything did.
- **AC8** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it exits 0, and
  `wc -lc memory/guides/UNATTENDED-PROTOCOL.md` reports a byte count strictly below 61440 AND strictly
  below this unit's own PRE-IMAGE, measured before the pass with
  `git show HEAD:memory/guides/UNATTENDED-PROTOCOL.md | wc -c` and recorded in the build record. The
  pre-image is measured and never assumed. At order 1 this unit runs before every sibling that
  touches the file — `TOOL-dFoldedVerdict-1`'s amendment is order 2 and `TOOL-dFoldedVerdict-2`'s
  section 8 row is order 3 — so the pre-image SHOULD equal the BASE 61440 and the re-measurement is
  what PROVES that rather than a step that assumes it. Rev-3 had this backwards, naming unit 2 as
  order 2 and treating its row as already landed.
- **AC9** — When `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f' memory/guides/UNATTENDED-PROTOCOL.md`
  runs, it still yields the conf-key table, and `grep -n '^## ' memory/guides/UNATTENDED-PROTOCOL.md`
  still reports `## 7. The verbs` at a heading of its own with sections 8 through 12 unrenumbered.
- **AC10** — When `python3 tools/codebase-map/test_codebase_map.py` runs, it exits 0, which asserts
  the new `guides` key is claimed by `memory/map/features/unattended.md` and that the generated map
  artifacts were re-rendered in the same commit.
- **AC11** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0, and
  `python tools/memory-tree/check-arms.py --report` shows this file's branch and armed counts BOTH
  risen from the BASE measurement of 169 and 161. The arms themselves are not executed: the
  compensating check is `bash tools/unattended/run-unattended-gates.sh --checks`, which runs the
  three record and wiring checks and NOT the forbidden suites. The bare invocation defaults to
  `--selftests` (`run-unattended-gates.sh:60`) and is not run by this unit.
- **AC12** — When `grep -n 'TOOL-dUnstalledConvoy-17\|TOOL-dBriefedPass-8' memory/backlog/TOOL.md`
  runs, neither row still asserts what S10 measured false: no claim that section 7 omits `--park` or
  `--attest`, and no claim that `INDEX_CAP_BYTES` is the cap that binds it.
- **AC13** — When the `--review` bullet is extracted from the PRE-IMAGE section 7 and from BOTH
  halves of the new pair with `sed -n '/^- .--review. — /,/^- .--version. — /p'`, all three extracts
  are byte-identical, and each still contains the literal `promoted to a unit rather than parked`.
  **This is the inverse of what rev-2 and rev-3 asserted, and the inversion is the point.** This
  unit is order 1: it moves the bullet unchanged per S11, and a criterion demanding the CORRECTED
  text here would grade `TOOL-dFoldedVerdict-1`'s work inside the one unit that must not perform it.
  The three extracts and the commands that produced them go in the build record. The correction is
  graded by `TOOL-dFoldedVerdict-1` AC17 at order 2, over this same pair.
- **AC13a** — When the protocol's run-state authored-half clause is read in BOTH halves of the
  protocol pair, each carries S13's sentence, and `bash tools/unattended/check-unattended.sh` reports
  no check 10 failure over that pair. This is a READER observation for the sentence's CONTENT and is
  written as one: no grep distinguishes a clause that SANCTIONS the source-suffixed form from one
  that merely mentions it, and an honest unobservable beats a criterion that cannot fail. The reading
  and its verdict go in the build record. The CEILING-and-refusals reading that rev-2 put at this
  number moved to `TOOL-dFoldedVerdict-1` AC17, together with the sentence it grades.
- **AC14** — When `grep -cE '^- .--[a-z-]+. — '` runs over each half of the PROTOCOL pair it reports
  0, and over each half of the NEW pair it reports 18. Measured at BASE with the same command: the
  protocol reports 18 and every one of them sits inside section 7, so the zero is an observation with
  a failing case rather than a restatement of AC3. This is the criterion that distinguishes a
  completed move from a HALF-MOVE, and neither existing leg can: check 10 compares the two protocol
  copies to each other and passes when neither was emptied, and check 26 under F1 reads only the new
  carrier. Additionally `sed -n '/^## 7[.] The verbs$/,/^## 8[.] /p'` over each protocol half yields a
  body that names `UNATTENDED-VERBS.md` and carries no verb bullet.
- **AC15** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 with the `[[files]]`
  destination S7 declares present and unique. Stated because nothing else reaches S7: verified by
  reading, `tools/unattended/adopt-unattended.sh` contains ZERO references to `kit.toml` and
  hard-codes its artifact paths at `:183-190`, so AC6's adopter `--check` cannot observe a missing
  descriptor row, and the kit half is already claimed by the `include = "**"` engine rule.
- **AC16** — When `grep -n 'UNATTENDED-VERBS' tools/unattended/SKILL.template.md
  .claude/skills/unattended/SKILL.md` runs, both files return a hit in the sentence naming the binding
  contract, and `bash tools/unattended/adopt-unattended.sh --check` then reports `unattended: in sync`
  over the regenerated render. AC6 grades the render's BYTES and would pass on a Skill that still
  names one carrier, so S8 needs an observation of its own.

## 7. Gates

Named legs, each resolving in `tools/gate-legs.json`:

- `unattended kit gate` — checks 10, 22 and 26; the primary witness for S3, S4 and S5.
- `unattended skill wiring` — the adopter's `--check`, covering S6 and the S8 render.
- `memory hygiene` — check 6's guide caps over both the shrunk protocol and the new carrier.
- `kit version markers` — the marker on the new template.
- `codebase-map coverage + freshness` — the new `guides` inventory key and the regenerated artifacts.
- `harness arms (fail branches armed or pinned)` — every new `fail` branch armed or pinned.
- `method carriers (every pointer declared)` — asserts the registry row for `PROTOCOL.template.md`
  still hits after the move, and reds if the new carrier acquires a `BUILD-METHOD.md` citation
  without a row of its own.
- `install-prefix (shipped surface)` — reds if the new carrier spells a `tools/<kit>/<file>` path.
  The protocol carries zero `tools/` occurrences at BASE and the new file inherits that discipline.
- `dead-path carriers (deleted files still named)` — the move creates paths rather than deleting
  them, and this leg is what says so.
- `govkit selfcheck` — the new `[[files]]` row's destination is declared and unique.

No new gate is added. The move is graded by legs that already exist, which is the argument for
putting the new file where check 6 and check 26 can already reach it.

## 8. Open questions

- **F1 — does check 26's protocol arm read ONLY the new carrier, or either file?** RESOLVED (agent,
  2026-09-01): the new carrier only, with its own named refusal when that file is absent. Options: point
  `$SHIP` at the new template and refuse when it is absent; or accept a hit in either file. The
  second is cheaper to write and is wrong: a half-completed move leaves the verbs in both places and
  passes. RECOMMENDATION: the new carrier only, with its own named refusal when the file is missing,
  on the same reasoning check 10 already records for a one-file parity check.
- **F2 — does the second pair become a new check number, or a row inside check 10?** RESOLVED
  (agent, 2026-09-01): a row inside check 10. Options: a
  `PAIRS` list inside check 10, iterated; or a new check with its own number. A new number costs a
  new entry in every place check numbers are enumerated and gains nothing, because check 10 already
  carries the both-halves refusal the second pair needs. RECOMMENDATION: a row inside check 10.
  Neither option disturbs a pinned ordinal — check 10 has no pinned rows — but a new check inserted
  in file order could, depending on where it lands.
- **F3 — should `AGENTS.md` cite `memory/guides/UNATTENDED-VERBS.md`?** RESOLVED (agent,
  2026-09-01): do not cite it. Editing the charter is a governance-carrier change and M3's veto 2
  reserves it for the owner, so citing it here would be this unit taking a decision it may not take.
  A charter citation would put
  the file in check 16's read path, which it does not need: `check-memory-hygiene.sh:449` already
  caps it by location, and check 16 rule 3 only asks that a charter-cited member IS capped.
  RECOMMENDATION: do not cite it. The protocol's §7 stub reaches it in one hop, and editing the
  charter and its template is a change to a governance carrier, which M3's veto 2 reserves for the
  owner. If the owner wants it cited, that is a separate act and not this unit's.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Every cap, line number and count in §4 verified at BASE
  `adc0543c` by reading the named source.
- rev-2 · 2026-09-01 · round-1 spec-audit fold. **H4** — S11, the N2 carve-out, the new §4
  subsection and AC13 with AC13a: the protocol's `--review` sentence goes false under
  `TOOL-dFoldedVerdict-1` and rev-1 would have copied it verbatim into a new byte-compared pair. The
  correction is owned by order 1 and this unit is now the backstop that observes it, cited by section
  rather than by a line number this move invalidates. **H9 and owner ruling (b)** — N9 added, and the
  version-bump row deleted from Files touched with the deletion stated: the bump moves ONCE, on
  `TOOL-dFoldedVerdict-6`, and AC7 now says plainly that `check-kit-versions.sh` asserts agreement and
  never movement. **M4's class** — AC14 added: at rev-1 no criterion observed that section 7's body
  LEFT the protocol, and every leg touching that pair passes on a half-move. **M5** — AC15 and AC16
  added for S7 and S8, which had no criterion and which the adopter check cannot reach; folded here
  because this spec is the only document the finding addresses. AC8 re-stated against this unit's
  pre-image rather than the BASE constant, which `TOOL-dFoldedVerdict-2` moves at order 2. **S12**
  states the handoff to `TOOL-dFoldedVerdict-6` explicitly in both directions.
- rev-3 · 2026-09-01 · MOVED TO ORDER 1, and the move is load-bearing rather than cosmetic. `memory/guides/UNATTENDED-PROTOCOL.md` renders at EXACTLY `GUIDE_CAP_BYTES` (61440 of 61440, measured) with 725 of 750 lines, and two units sequenced BEFORE this one added bytes to it — `TOOL-dFoldedVerdict-2` S12 adds a section-8 key row and `TOOL-dFoldedVerdict-1` S9 amends a bullet. Either would have red hygiene check 6 before the relief this unit provides had landed, which is M2's ordering rule broken: a unit depending on one sequenced after it. This unit now runs first and frees the 8.1 KB the rest spend. N2 is unchanged — the move is still verbatim, and the bullet it carries is corrected by unit 1 afterwards in the new carrier.

- rev-4 · 2026-09-01 · the fork sweep, one owner ruling that added scope, and the assumptions the
  rev-3 reorder inverted. F1, F2 and F3 marked; the spec is no longer FORKED. **The inversion is the
  substantive change.** Rev-2 wrote S11, the §4 subsection and AC13 on the premise that
  `TOOL-dFoldedVerdict-1` lands FIRST and this unit is the backstop that observes a corrected
  sentence. The reorder made this unit order 1 and that one order 2, so the premise is exactly
  backwards: the pre-image still carries the false `--review` sentence and this unit copies it
  unchanged. S11, the subsection and AC13 now say so, and AC13 asserts byte-identity across the
  pre-image and both new halves rather than demanding the corrected text — a criterion demanding it
  here would grade a sibling's work inside the one unit forbidden to do it. The falsified sentence
  still does not survive the build: unit 1's S9 names this carrier and its AC17, repointed at rev-4,
  grades the correction there. AC13a was freed by that move and now carries S13. AC8's pre-image note
  named unit 2 as order 2 and treated its section 8 row as already landed; unit 2 is order 3, so the
  pre-image should equal the BASE 61440 and the re-measurement is what proves it. **S13 is new**: the
  owner ruled on `TOOL-dFoldedVerdict-3` Q2 that the protocol sanctions the source-suffixed
  provenance form in one sentence, and it is assigned here because at order 1 the permission precedes
  the rows that rely on it and stays separable in a diff that is otherwise a move.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "splitting a capped governance document into a second
byte-compared carrier file"` returned 39 candidates, all of them name-stem or affordance matches
(`tracked_files`, `derive_carried`, `kit-dogfood-parity.PAIRS`), and NONE of them is the seam this
unit extends. The seam was found by reading and is cited by path: the `PLAYBOOK-TEMPLATE` pair is
already the third placeholder-free document this kit ships, and it is the exact shape a fourth takes
— `tools/unattended/adopt-unattended.sh:188-190` binds its `PBT_SHIP`/`PBT_REL`/`PBT_OUT` triple,
`:268-273` holds its two separate `--check` refusals, `:285-288` its install, and
`tools/unattended/kit.toml:26-31` its `[[files]]` row beside a `[[lf_pin]]`. The parity half of the
seam is `tools/unattended/check-unattended.sh:1248-1260`. This unit extends both rather than
inventing a mechanism. One cited candidate was checked and found NOT to fit:
`tools/memory-tree/kit-dogfood-parity.test.sh:53` carries a `PAIRS` table of exactly the right shape,
but its three rows are memory-tree's own, and reaching across a kit boundary to use it is the
cross-kit edge this repo forbids.

Recall terms used: `python tools/memory-recall/query.py "why is the unattended protocol capped and
what decided how a second byte-compared carrier file is registered" --terms "unattended protocol
GUIDE_CAP_BYTES index cap parity leg check 10 byte-compare PROTOCOL.template.md adopt-unattended
kit.toml rendered artifact verb carrier check 26 guides inventory"` — 39 hits, of which the four that
decided this design are the `TOOL-dBriefedPass-5` closing review's cap attribution, the
`TOOL-dBriefedPass-8` backlog row that mis-attributes it, the `TOOL-dBriefedPass-1` spec-audit round 2
finding that section 7's list IS the check-26 carrier, and `TOOL-cFinalBerth-3`, which is why every
shipped doc in this kit carries a version marker.
