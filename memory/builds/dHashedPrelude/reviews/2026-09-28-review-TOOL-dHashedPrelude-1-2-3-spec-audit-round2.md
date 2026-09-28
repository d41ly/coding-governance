**Serves:** spec-audit TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

# dHashedPrelude — spec audit, ROUND 2: the fold itself

*Tier-2 adversarial review · 2026-09-28 · node d · ROUND 2 · subject: the round-1 fold, `f8e38c70..c243e75b`.*

Subjects, each pinned at the blob reviewed:
`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-1.md@14cebec3d57bf3903fba3baa2b603947248adf1c` ·
`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md@50886f228bf28224a60abee0cf9ab5ce7e784f28` ·
`memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-3.md@77bdc7190a8b92903274df9e623d11e30ebe157f`.
Target of the specs: `tools/memory-recall/selftest.py`, blob `523ac3079a4ad7c34153f8713e9190216b47d701`, identical at BASE `3cf05f29` and at HEAD `c243e75b`.

## Verdict: BLOCKED

One blocker, unchanged in kind from round 1: unit 2's ordering arm still cannot be built without
guessing, because the scope item and the acceptance criterion that scope item names as its own
observer demand opposite verdicts on the same observation. The fold that was written to close D-1
reproduced D-1 inside the mechanism it added. Four independent lenses found it separately.

## Review shape

- Round 2, narrowed brief: the fold diff only. Round 1 returned precision 0.29, below the floor, so
  this round hunted four named things rather than re-auditing the specs.
- Raw 28 · confirmed 18 · refuted 10 · unverified 0 · **precision 0.64**. Above the floor, and more
  than double round 1 — narrowing the brief to the unreviewed fold text was the whole of the gain.
- Adjudicated **by item**: 1 blocker · 4 high · 4 medium · 1 low = 10 items.
- Adjudicated **by raw confirmed finding**: 4 blocker · 9 high · 4 medium · 1 low = 18 findings.
  The two tallies differ because seven items are merges; every confirmed id appears in exactly one.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every count is zero, so
this run is complete and a zero below is evidence rather than an absence of evidence.

## The measurement that settles three items

Every anchor figure in the fold was re-derived here, on `tools/memory-recall/selftest.py` at BASE,
under all four plausible read modes. The worktree copy is CRLF (151,442 bytes, 2,745 CRLF pairs);
the tracked blob is LF (148,697 bytes).

| read mode | `@check(` | newline + `@check(` | `def main() -> int:` | newline + `def main() -> int:` |
|---|---|---|---|---|
| worktree, raw bytes | 7985 | 14748 | 129252 | 144324 |
| worktree, decoded with CRs preserved | **7955** | **14712** | 129022 | 144090 |
| worktree, `read_text(encoding="utf-8")` | 7811 | 14426 | 126644 | 141457 |
| BASE blob, decoded | 7811 | 14426 | 126644 | 141457 |
| BASE blob, raw bytes | 7841 | 14462 | 126874 | 141691 |

Occurrence counts are identical under every mode: `@check(` 72, newline-anchored 71;
`def main() -> int:` **2**, newline-anchored **1**.

Two consequences, both load-bearing below. The pinned pair 7955 / 14712 is produced by exactly one
reading — the CRLF working copy decoded without newline translation — and by no reading of the file
at BASE, including the file's own idiom at `selftest.py:2378`. And `def main() -> int:` is not
unique; its first hit is line 2379, inside the pin arm's own `src.partition(...)` literal.

## What the fold got right

Stated because a review that reports only defects lets a correct figure be re-litigated next round.
Re-derived and TRUE: the live query log measures 1,545,472 bytes and carries 597 rows, so spec-1 §5
and AC4's account of rows 596-597 are exact. Spec-3 AC2's grep prints exactly three lines, all
carrying 1.12, so the D-3 fold did run the command before writing it down. `SELFTEST_ARMS` reads 71
at `selftest.py:111`, unit 2 adds two arms, so 71 → 73 is right. `main()` appends five run-property
rows when the repo resolves and four when it does not, so spec-1 S4's figures and spec-2 AC6's
76 → 78 are both correct and agree with each other — the set is arithmetically self-consistent on
scope and count. Unit 1 adding `_live_log_row` while its own S4 says nothing outside the guard moves
is NOT a contradiction: S4 enumerates the arms, their order, the arity assertion and the pin, and
none of those moves. `_live_log_row`'s signature and its four returns are specified well enough to
build. The gap in unit 1 is not what the function returns — it is that nothing observes where
`main()` calls it, which is item D.

---

# BLOCKER

## A — S3 and AC5 mandate opposite verdicts on the same observation

*ids folded: 1, 8, 15, 21. Address:* `spec-TOOL-dHashedPrelude-2.md` §2 S3, against §6 AC5 (and AC1's
"Given this file it reports ok"). Both texts are new in rev-2; S3 names AC5 as its own observer.

S3: the arm "reds if the unanchored form of an anchor resolves to a different offset than the
anchored form". AC5: the arm "asserts ... that for `@check(` the unanchored offset and the anchored
offset differ — today 7955 against 14712", and reports ok.

Those are the same observation with opposite verdicts, and the observation is TRUE of the shipped
file: the offsets differ for two of the three anchors in every read mode (table above). An
implementer who builds S3 ships an arm that reds against a correct file on day one — D-1, the
round-1 blocker, reproduced inside the fix commissioned to close it. An implementer who builds AC5
leaves S3 unimplemented and ships an assertion that cannot fail, because a newline-anchored search
returns the offset OF the newline, so anchored and unanchored differ by at least one byte for every
anchor on every input. Both readings are defective; nothing in §4, §5 or §7 picks between them.

**Fix.** Rewrite S3 to state the polarity AC5 wants, and give it a frame: the arm asserts each anchor
occurs at least once in its newline-anchored form and USES the anchored offset; it reds when an
anchor's newline-anchored form is ABSENT. Do not make divergence a red — it is the normal state. Do
not make uniqueness a red either: `\n@check(` legitimately occurs 71 times. If a divergence check is
genuinely wanted, state it on normalised offsets (anchored + 1 against unanchored) and say which
direction reds. Then re-point AC5 at the rewritten S3 and restate it as asserting that the
comparison used the ANCHORED offsets despite an earlier bare hit — see item G for why the bare
offsets should leave the criterion entirely.

**Left-shift gate.** Two, and the cheap one is machine-checkable today. (1) A spec-lint leg that
parses every `Observed by AC<n>` in §2 and reds when that criterion does not exist, or when a scope
item declares a RED condition whose subject string also appears in an ASSERT clause of its named
observer — the second half is a heuristic and should print near-misses before it is wired, per §7.
(2) A `memory/gotchas/` row for the class this is the second instance of in one build:
`scope-item-and-its-own-observer-mandate-opposite-verdicts`. Round 1 filed
`criterion-asserts-what-its-own-command-cannot-show`; this is its polarity sibling and the same
audit found both.

---

# HIGH

## B — the anchors table's occurrence census stopped one anchor short

*ids folded: 9, 16, 23. Address:* `spec-TOOL-dHashedPrelude-2.md` §4 "The anchors, by their exact
bytes", table row 3; and §10, final paragraph.

Row 3 answers the column "the unanchored form resolves to" with "unique today, anchored anyway".
Measured: `def main() -> int:` occurs TWICE. Its first hit is line 2379 —
`body = src.partition("\ndef main() -> int:")[2]`, inside
`test_the_selftest_pin_carries_an_unbroken_provenance_chain` (def at line 2364) — and only its
second is the definition at line 2634. Only the newline-anchored form is unique.

This is the identical string-constant decoy the table's own row 1 documents for `@check(`, sitting
inside the very arm §4's Inventory and §10 name as the convention both new arms copy. So the census
caught the trap for one anchor and missed it for the other, and §10's claim that "every anchor this
design depends on was counted in the target file" is false as it stands — in the paragraph that
presents the census as the answer to why the round-1 blocker went unseen. Impact is real though
partly held by "anchored anyway": an implementer who trusts the cell and drops the leading newline
partitions the file at 2379, and AC2's negative direction ("`main()` body does not mention
`_LIVE_LOG_BEFORE`") is then graded over a span that starts 255 lines early and contains the new
arms' own `_LIVE_LOG_BEFORE` literals, making AC2 unfalsifiable.

**Fix.** Replace the cell with the measured answer — "2 occurrences; the bare form resolves first to
line 2379, inside the pin arm's own `src.partition` literal; the newline-anchored form is unique" —
and give every row an explicit count for BOTH forms: `@check(` 72 bare / 71 anchored,
`def main() -> int:` 2 bare / 1 anchored. Name the pin arm as the decoy's owner so a later edit to
that arm is known to move this anchor. Correct §10 to say the census found two collisions, not one.

**Left-shift gate.** Extend the spec-audit leg round 1 proposed (execute every shell command a spec
quotes inside a criterion) to cover FIGURE tables: a table cell asserting a count or an offset must
carry the command that produces it, and the leg runs it at the spec's declared BASE. Corpus row:
`occurrence-census-stopped-one-anchor-short`.

## C — the pinned offsets are CRLF-working-copy character offsets, not the file at BASE

*ids folded: 10, 17, 22. Address:* `spec-TOOL-dHashedPrelude-2.md` §4 table rows 1-2 (14712, 7955,
"near 14600") and its heading; §6 AC5's figure line; §5 perf row ("151 KB file").

AC5 labels the pair "PINNED, measured on 2026-09-28 at BASE". That is the one reading that does not
reproduce. 7955 / 14712 come only from decoding the CRLF working copy with CRs preserved. At BASE
the blob is LF and gives 7811 / 14426 decoded or 7841 / 14462 in bytes; the worktree read the way
this file already reads itself (`read_text(encoding="utf-8")`, `selftest.py:2378`) also gives
7811 / 14426. The section heading says "by their exact bytes" and the numbers are not bytes under
any reading. §5's "151 KB file" is the same CRLF measurement; the committed file is 148,697 bytes.

`git check-attr` reports `text: auto`, `eol: unspecified` for this path, so a Windows checkout
smudges it and CI, node `a`, node `b` and node `c` do not — the same file legitimately yields two
offset pairs, and this kit already ships `test_crlf_working_copy_is_not_drift`, which rules that a
CRLF working copy is a checkout artifact rather than the file's state. The line numbers (145, 287,
2634) reproduce everywhere, so two of four pinned figures agree and two do not, which is the worst
shape a pinned figure can have: a verifier re-running AC5's stated observation on any other node
gets neither number and cannot tell whether the spec, the tree or their own command is wrong. AC5's
"the arm does not read them" bounds the blast radius; it does not make the figures right. This is
the repo's own `worktree-crlf-beyond-the-pinned-set` / `text-mode-read-eats-embedded-cr` class,
landing inside a table written to prevent an offset mistake.

**Fix.** Pin the LINE numbers 145, 287, 2379 and 2634, which are identical under every read mode and
on every checkout, and either delete the character offsets or name their frame explicitly: "character
offsets over `read_text(encoding='utf-8')` on the blob at BASE: 7811 and 14426; a CRLF working copy
shifts every absolute offset and leaves the ordering invariant, which is why the arm derives them and
this table is evidence only." Change the heading to "The anchors, and where each one resolves".
Correct §5 to 148 KB or drop the figure.

**Left-shift gate.** The durable one is a product fix that deletes the class: add `*.py eol=lf` (or
at least `tools/memory-recall/*.py`) to `.gitattributes`, so the working copy and the blob stop
disagreeing and every offset anybody measures on any node is the same number. The repo already
forces LF on `.sh` and the memory-tree data files; this is the same rule one filetype wider. Beside
it, a corpus row: `figure-pinned-from-a-smudged-working-copy`.

## D — nothing observes that `main()` appends the live-log row unconditionally

*ids folded: 3, 14. Address:* `spec-TOOL-dHashedPrelude-1.md` §2 S4 (final clause), §4 paragraph 3,
and §6 AC5's Red-when, against AC4.

The unconditional append is the build's central payoff — it is what turns the unresolvable state's
silence into S2's announced `skip`. No criterion in the set reaches it. AC5 calls `_live_log_row`
directly, and the function returns the same triples whether or not `main()` still wraps the append in
`if live is not None:` (`selftest.py:2700`). Spec-2 AC3 also only calls it directly. AC1 and AC2 run
the suite in a reachable repository, where the row appears either way. AC5's own Red-when
nevertheless claims it catches exactly this — "or `main()` keeps a conditional append" — a coverage
claim its observation cannot support, which is round-1 D-4's shape.

S4's clause "in every reachable-repository state the count of appended run-property rows is unchanged
at five, and in the unresolvable state it rises from four to five" says "Observed by AC4". AC4
observes the live QUERY LOG's digest and row count and re-reads `SELFTEST_ARMS` at 71. It never
counts appended check rows, so the clause is attributed to a criterion that cannot see it.

Concrete failure this leaves open: the implementer adds the unconditional `_live_log_row(...)` append
per §4 and leaves the existing `if live is not None:` block in place. The suite then emits the row
`the live query log is byte-identical after this run` TWICE. `assert len(order) == len(_checks)` runs
before the appends so it cannot see it, both rows read ok, and the summary prints 77/77 green. The
duplicate surfaces only at unit 2, against AC6's 78 — a criterion that also says the summary line is
"deliberately not the instrument". The green-by-absence class this build exists to close, surviving
inside the build that closes it.

**Fix.** Add an observation that reaches `main()`. Either extend AC5 with a source-text clause — the
body of `main()` contains no conditional guarding the `_live_log_row` append, and the call is a
statement at the same indentation as the pin and sweep appends — or give unit 2's ordering arm a
fourth assertion and cite it from AC5; its `src` parameter already makes a synthetic `main()` with a
conditional append drivable. Then add to AC4, or as a sixth criterion: when the suite runs on this
repository, exactly one row named `the live query log is byte-identical after this run` is printed
and the summary denominator reads 76, with 76 marked DERIVED and the row name quoted. Re-point S4's
four-to-five clause at that criterion instead of at AC4.

**Left-shift gate.** The product form is the real one and it lands inside this build: unit 2's
ordering arm gains the `main()`-body assertion, so a leftover conditional reds an arm rather than
surviving to a later unit's count. Corpus row for the spec class:
`a-red-when-names-a-failure-its-own-observation-cannot-reach`.

## E — §4's relocation mechanism is false under rev-2's anchoring, and AC1 is unreachable

*id: 11. Address:* `spec-TOOL-dHashedPrelude-2.md` §4 "How each arm decides", first paragraph,
against §2 S3 and §6 AC1.

The paragraph says that when the baseline is moved into `main()`, "the first occurrence of the
assignment literal becomes this arm's own string constant ... so the ordering assertion still fires".
Under S3's newline anchoring neither match exists. The arm's own constant is written
`"\n_LIVE_LOG_BEFORE = "`, whose leading characters are a backslash and an `n` in the file's bytes,
so a real-newline anchor never matches it; a relocated assignment inside `main()` is indented, so it
never matches either. The anchored search returns not-found, the arm takes AC4's branch, and AC1's
required outcome — "FAIL and its detail names the ordering it expected" — is unreachable, since AC1
and AC4 are distinguished only by the message. Reaching both needs a fallback branch no section
describes.

This is rev-1's unanchored justification left standing after rev-2 moved the search: the paragraph is
verbatim from `f8e38c70`. It is the repo's `amendment-leaves-its-other-half-standing` class, and it
is the reason this round's brief pointed at counterparts.

**Fix.** Either declare the `_LIVE_LOG_BEFORE` search deliberately UNANCHORED and say in §4's table
row 2 why that one anchor is exempt, or keep the anchoring and rewrite AC1 to require a FAIL naming
"no module-scope baseline", then add the relocation case as its own criterion driven by a search that
tolerates indentation. Rewrite the paragraph to match whichever is chosen; it currently describes a
mechanism that cannot occur.

**Left-shift gate.** Extend the spec-lint proposed under item A with a revision-log leg: when a
`## 9. Revision log` entry names a section as amended (here §2 S3), red if a paragraph elsewhere that
quotes the amended construct by its literal bytes was not touched in the same revision. Cheap,
lexical, and it is the machine form of "did the fold leave its other half standing". Corpus row:
`amendment-moved-the-search-and-left-its-justification`.

---

# MEDIUM

## F — "the search cannot return the not-found value" is false once the searches are anchored

*id: 5. Address:* `spec-TOOL-dHashedPrelude-2.md` §4 "How each arm decides", second paragraph, and §5
error/empty/loading states.

§4 says "the arm's own source always contains both literals, so the search cannot return the
not-found value", and §5 repeats it as "unreachable by construction". A Python constant written
`"\n@check("` holds a backslash and an `n`, not a newline byte, so the arm's own constants are
invisible to the anchored searches S3 mandates. The stated reason holds only for the UNANCHORED
search, so a reader who takes the reasoning at face value writes the bare-string search and lands
back on D-1. The claim also contradicts this spec's own Edges bullet, which says both arms red on a
tree that has not landed unit 1: that red IS the not-found branch firing under the default argument,
which §5 says cannot happen. The conclusion survives on a landed tree for a different reason; the
spec's reason is wrong, and under item E one criterion is unsatisfiable alongside it.

**Fix.** Replace the sentence with what anchoring actually buys: the anchored literals do not match
the arm's own string constants, because a Python `"\n..."` constant holds no newline byte; on a
landed tree both anchors resolve to the real statements, and on a tree without unit 1 the
`_LIVE_LOG_BEFORE` anchor is not found, which is the correct red. Correct §5's row from "unreachable
by construction" to "reachable, and driven by AC4 from a synthetic source rather than left to the
tree's state".

**Left-shift gate.** Same leg as item E. Additionally, a §10 checklist row worth carrying beyond this
build: an escaped-newline literal in a spec is a BYTE claim, and any argument that a source contains
its own search literal must state which of the two forms it means.

## G — AC5 couples a merge-bar leg to an unrelated docstring sentence

*id: 20. Address:* `spec-TOOL-dHashedPrelude-2.md` §6 AC5, the assertion clause.

AC5 makes the arm assert that the decoy EXISTS. Exactly one unanchored-only `@check(` occurrence is
in the file — line 145, inside `check_provenance_chain()`'s docstring, the phrase "counting `@check(`
decorators by reading the source". All 71 others are newline-anchored. Reword or delete that one
documentation sentence — a pure docs improvement, unrelated to this guard — and the bare and anchored
searches collapse onto the same offset, the assertion fails, and a merge-bar leg reds against a
correct file. The property the arm exists for is that the ANCHORED form is unambiguous, which is a
property of the anchor; whether unrelated prose elsewhere happens to contain the bare substring is
not. This is the same "reds against a correct file" class the fold was written to close, one step
removed.

**Fix.** Restate AC5's assertion as a property of the anchored form alone: each anchor occurs at
least once in its newline-anchored form and the arm uses that offset. Keep 7955 / 14712 — corrected
per item C — in §4 as the census that motivated anchoring, and drop them from the acceptance
criterion, so no criterion depends on the decoy surviving.

**Left-shift gate.** A §10 checklist row, since the machine form is not cheap: an acceptance criterion
may not assert a property of code outside its unit's declared scope; when it does, name the file and
line it has just made load-bearing. Corpus row: `a-gate-that-depends-on-its-decoy-surviving`.

## H — the FAIL row's new detail is observed by no criterion

*id: 18. Address:* `spec-TOOL-dHashedPrelude-1.md` §2 S2, state table row 2 ("`FAIL`, detail carries
BOTH digests"), and §5 observability.

The fold introduced one behavioural change to an existing row: the FAIL detail moves from the literal
`the gate wrote to it` (`selftest.py:2705`) to a detail carrying both digests. S2 claims it is
"Observed by AC2 and AC5". AC2 observes the `ok` detail; AC5 observes a `skip` triple and an `ok`
triple; neither reaches the FAIL branch at all. AC1 requires only that the row "reports FAIL and the
process exits 1", and spec-2 AC3 asserts "the state token of each" and nothing more. A build that
leaves the literal exactly as it is today satisfies every criterion in the set while failing the one
thing §5 lists under observability, so the scope item will silently not be built.

**Fix.** Extend AC5, or add AC6: drive `_live_log_row` with two differing digests and assert the
returned detail contains both hex values — for example that the before-digest prefix and the
after-digest prefix both appear in the detail string. Correct S2's "Observed by" pointer to name it.

**Left-shift gate.** Machine-checkable and general: a spec-lint leg asserting that every ROW of a §2
state table is named by at least one acceptance criterion, matched on the row's state token plus its
quoted detail string. This build's S2 table is four rows and two of them are unobserved, so the leg
would have redded on the fold that introduced them.

## I — a non-goal defers work to a backlog row that does not exist and nothing creates

*id: 26. Address:* `spec-TOOL-dHashedPrelude-2.md` §3 Non-goals, final sentence, and the identical
clause in `spec-TOOL-dHashedPrelude-3.md` §3.

"No change to the summary line, which is recorded as a backlog row instead" points at a row that is
not in `memory/backlog/`. Greps over the family files return nothing about the memory-recall
selftest's summary line or this build; the only nearby row, `TOOL-aProbedToolkit-14`, is about the
README's typed "18 checks" and is the row unit 3 edits for a different reason — and AC3's Red-when
forbids closing it outright, so it cannot absorb this one. `git show --stat c243e75b` confirms the
fold wrote no backlog file. No scope item or criterion in any of the three units creates the row.

Round 1's D-5 left-shift was declined into that record, and so was D-3's spec-audit leg. Both are now
owned by nobody: nothing in the build's Definition of Done reds if the row is never written, so the
declined work evaporates at landing and the next spec that reaches for the summary line as an
arm-count instrument repeats D-5. An exemption is not coverage.

**Fix.** Give the row an owner. Unit 3 already edits `memory/backlog/TOOL.md` under S3 and lists it in
Files touched, so extend S3 and AC3 to mint both rows and assert them; or, if they are minted
elsewhere, cite each row's family-qualified id inline in both §3s.

**Left-shift gate.** Purely lexical and it generalises across the whole corpus: a spec-lint leg that
reds when a §3 Non-goal says "recorded as", "tracked as" or "filed as a backlog row" without a
family-qualified id on the same line. A deferral with no id is a deferral with no owner, and this
corpus writes that sentence often.

---

# LOW

## J — the build README's authored roster still describes the pre-fold design

*id: 28. Address:* `memory/builds/dHashedPrelude/README.md`, the authored `roster:units` table, rows
1 and 2.

The fold regenerated the `gen:build-units` region to unit 2's new title but left the authored roster
untouched. Row 2's Mechanism cell still reads "an arm reads the suite's own source and reds when the
baseline does not precede the first decorated arm" — one arm, no state arm — three lines above a
generated row that now titles the same unit "two arms red when the live-log guard stops bracketing
the arms". Row 1's cell omits `_live_log_row` and the skip ruling, which are now unit 1's main
deliverables and the reason unit 1 gained S2 at all.

The roster is the build's own authored description of its units and is now the only place still
describing the pre-fold design. A session that reads the README before the specs — the normal order —
plans unit 2 as a single arm and unit 1 as a two-line move, and budgets the pin at 71 → 72 rather
than 71 → 73.

**Fix.** Rewrite unit 2's Mechanism cell to name both arms and the four-state table the second one
drives, and add `_live_log_row` and the skip ruling to unit 1's. Neither cell is generated, so the
renderer will not do it.

**Left-shift gate.** A hygiene ratchet in the shape this repo already uses: red when a spec's `rev-N`
increments in a commit that does not also touch the build README's authored `roster:units` region.
Cheap, commit-scoped, and it catches the general case — an authored summary left behind by a fold —
rather than this instance.

---

## What was hunted and found clean

Stated so a later round does not re-spend tokens here, and because run integrity was clean, a zero is
evidence.

- **Every other measured figure in the fold reproduces.** The live log's 1,545,472 bytes, spec-3
  AC2's three-line grep and its three 1.12 literals, the 76 → 78 row counts, the 71 → 73 pin, and
  spec-1 S4's five-reachable / four-unresolvable split were each re-derived against the tree and are
  correct. The two false figure classes are items B and C and nothing else.
- **The three-spec set is self-consistent on scope, ordering and count.** Spec-1 adds no arm, spec-2
  adds two, 71 + 5 = 76, 73 + 5 = 78, and spec-3's Goal now credits unit 2 alone. The
  interface inconsistencies found are about OBSERVATION (items D and H), not about arithmetic.
- **`_live_log_row` is specified well enough to build.** Signature, the four returns and unit 2's
  direct-call driver are unambiguous. Unit 1 adding a function while S4 says nothing outside the
  guard moves is not a contradiction: S4 enumerates the arms, their order, the arity assertion and
  the pin, and the fold moves none of them.

## Note on the round

Round 1 returned precision 0.29 over a full-surface spec audit. Round 2 narrowed to the 457-line fold
and returned 0.64. The repo's own `fold-text-is-unreviewed-surface` gotcha predicted both the yield
and the location, and it was right twice: the blocker is in fold-new prose, and item E is fold-stale
prose the amendment left standing. The cheapest durable answer to this round is not any single fix
above — it is the spec-lint leg items A, E, H and I each ask for in a different shape, which would
have redded on four of this round's ten items before a human read the fold.
