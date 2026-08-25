# TOOL-dHonouredPark-3 — the dead-path waiver registry keys on line TEXT plus an occurrence ordinal, not a line NUMBER

**Status:** CLOSED · rev-5 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 2 · streams tooling · ratified 2026-08-25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-TOOL-dHonouredPark-3-acceptance.md](../build/2026-08-25-build-TOOL-dHonouredPark-3-acceptance.md) | journal | — |
| [2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round1.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round2-graded.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round2-graded.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |
| [2026-08-26-review-TOOL-dHonouredPark-1-diff-review-round2.md](../reviews/2026-08-26-review-TOOL-dHonouredPark-1-diff-review-round2.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/dead-path-waivers.txt` keys each waiver on `<path>:<line>`, so any insertion above a waived hit
unpins it and reds the bar for a reason unrelated to the change. It happened twice inside one build,
and the second re-key was performed by proximity and scrambled three rows onto the wrong reasons. The
owner ruled the key becomes the surrounding line's TEXT, which survives the failure that actually
occurs and breaks only on rewording.

The spec audit changed two things about how that is built. The population is **eight rows across three
files**, not four in one. And the checker does not compare line numbers at all — it computes set
differences over `<path>:<line>` tokens against a git-DERIVED needle set, so a naive text predicate
would be strictly weaker than what ships today.

## 2. Scope (IN)

- **S1** — the waiver row grammar becomes `<path>\t<ordinal>\t<line-text>\t<reason>`: the path, which
  occurrence of that text in that file the row means, the exact text of the line carrying the waived
  mention, and the reason. The line NUMBER leaves the key entirely.
- **S2** — the ORDINAL disambiguates two identical lines in one file. It counts occurrences of the
  TEXT, never lines of the file, so inserting any DIFFERENT line above a waived hit does not move it —
  which is the whole failure this ruling exists to remove. Inserting an IDENTICAL line above one does
  move it, and that residual is real, bounded and armed by S7.

  **`memory/project/unarmed-branches.txt` is the shape borrowed and NOT the validation.** rev-2 cited
  it as prior art proving insertion-stability; round 2 established the opposite. `check-arms.py` keys
  its call sites on a number plus an ordinal WITHIN that number, and that file's own header records a
  row's ordinal moving 2→4 because two branches were inserted above it, with a message that read like
  a rewording. What is borrowed is the four-field row and the idea of an occurrence index. What is
  deliberately NOT borrowed is the positional semantics that made it drift. An implementer copying that
  file's shape must not copy its counting rule.
- **S3** — staleness keeps the meaning it has today, and is stated as a MEMBERSHIP test rather than as
  a needle test. `check-dead-paths.sh` computes `stale_rows` as a set difference of the waived rows
  against the HIT set, and the hits derive from a needle set that is itself derived (deleted basenames
  minus tracked basenames). So the property to preserve is: **resolve each row's text to the line it
  names, and test whether that line is in `hits`.** A row is stale when it is not — which covers both
  the line vanishing AND its needle leaving the derivation, without the checker ever having to know
  which needle a row was about.

  That distinction is not pedantry. Round 2 found the obvious phrasing — "a row whose needle left the
  derivation" — is not computable as written: the checker greps ONE alternation and reduces to
  `<path>:<line>` tokens, attributing no needle to any row, and two of the eight waived LINES name two
  needles each, for which "any needle left" and "all needles left" give opposite verdicts. Membership
  in `hits` has neither problem and is exactly what ships.

  rev-1's predicate — "a row whose text matches no line in that file" — is the one that must not be
  used: it would let the four rows covering the `STATUS.md` needle survive silently the moment any
  tracked file is named `STATUS.md`, waiving nothing while reporting green.
- **S4** — the SET-DIFFERENCE machinery is restructured, because it cannot survive the key change
  unmodified. `check-dead-paths.sh` parses rows with `awk '{print $1}'` — whitespace-split, which a
  tab-delimited grammar breaks outright — and computes `unwaived` and `stale_rows` with `grep -vxF -f`
  over single `<path>:<line>` tokens. Text keying makes both sides multi-field records, so the
  comparison is rebuilt rather than having one operator swapped. This is the largest part of the diff
  and rev-1 described it as "one string comparison per hit instead of one integer comparison".
- **S5** — the existing rows are MIGRATED, each keeping its reason verbatim and gaining the text of the
  line it currently points at plus its ordinal. There are EIGHT, across THREE files: two in
  `WIRE-INTO-PROJECT.md`, two in `tools/memory-tree/check-memory-hygiene.sh` (including the `:554` row
  the parent build's park entry names as the incident that earned this ruling), and four in
  `tools/memory-tree/check-memory-hygiene.test.sh`.
- **S10** — this unit prices its own read-path charge and moves `READ_PATH_CEILING` by it, per owner
  ruling 2 and this build's rules slot. It touches no capped read-path member except its own
  `memory/DECISIONS.md` row, which the conf's precedent prices at about +122 against 60 B of headroom —
  so the movement is not optional. rev-2 carried this as a checklist bullet and an acceptance
  criterion, which is not declared scope; round 2 caught that only unit 2 had actually taken it as one.
- **S11** — `memory/map/features/install-prefix.md` is refreshed. That dossier CLAIMS
  `tools/check-dead-paths.sh`, `tools/check-dead-paths.test.sh`, `tools/dead-path-waivers.txt` and both
  dead-path gate legs, so the Definition of Done's "dossier prose refreshed on touch" binds here and
  the `codebase-map coverage + freshness` leg — unguarded, so it runs on every bar — grades it.
- **S6** — the three OTHER documentation sites are corrected in the same commit, because each states
  the old grammar as fact: `check-dead-paths.sh:50-51`, which pins the grammar as "matching
  `install-prefix-waivers.txt` exactly" and becomes permanently false rather than merely stale;
  `dead-path-waivers.txt:15-18`, which documents a line-keyed re-stamp protocol this unit deletes; and
  `tools/govkit/registry.toml:191-192`, whose exemption reason reads "Its rows are gov paths and gov
  line numbers".
- **S7** — **N identical hit-carrying lines need N rows.** Waiving one occurrence does not waive the
  others, and an unwaived hit reds the run before any staleness is reported. rev-2's AC5 implied a
  single ordinal-bearing row could clear an ambiguous case; it cannot, and the shipped arm asserting
  exactly that exit-1 outcome is already in `check-dead-paths.test.sh`. The ordinal buys each
  occurrence its OWN reason, which is what path-alone keying could not give and is why the owner
  rejected path-alone.
- **S8** — the ordinal is MANDATORY. Every row carries four fields; there is no three-field form and no
  "row with no ordinal". A row whose ordinal is absent, zero, non-numeric or out of range is a MALFORMED
  ROW and refuses by that name, distinct from a stale one. rev-2 required a mandatory field in §4 and
  then wrote arms for a row lacking it, which the stated parse rule cannot even represent.
- **S9** — arms for: a matching row · a row whose line left the hit set · a row whose text matches no
  line · a malformed ordinal in each of its four forms · two identical lines with one row (reds) and
  with two rows (passes) · a DIFFERENT line inserted above a waived hit (must be a no-op) · an IDENTICAL
  line inserted above a waived hit (must red, and is the residual S2 names) · and a REWORDING (must
  red). Three of these are GREEN arms and are not staged breaks; the stage-the-break rule binds the
  refusal branches, which is the rest.

## 3. Non-goals (OUT)

- No change to which mentions are waived. The population is identical before and after; only the key
  changes.
- No change to the three waiver CLASSES the file's header declares, nor to its shrink-only rule.
- No re-keying of any OTHER registry. `tools/install-prefix-waivers.txt` carries twelve rows in the
  same `<path>:<line>` shape with the same drift exposure and is the file `check-dead-paths.sh:51`
  names as the parity target — it is deliberately left alone, and S6 corrects the sentence claiming
  the two match rather than making the claim true. rev-1's non-goal named `memory/project/` here,
  which was the wrong sibling.
- No attempt to make the key survive rewording. That needs a content hash or a stable marker in the
  source line, and both are heavier than the failure they would prevent.

## 4. Design

### Data model

Four tab-separated fields per row. Tab-separated rather than space, because a line's text contains
spaces and a reason contains spaces, and a two-space-delimited grammar would be ambiguous the first
time a waived line ended in whitespace.

A waived line that itself contains a TAB is representable: the parser splits on the FIRST tab for the
path, the second for the ordinal, and the LAST for the reason, leaving everything between as the text.
A REASON containing a tab is therefore NOT representable, which is a constraint on the author and is
stated so nobody discovers it.

No waived line carries a tab today, verified over all eight. Of the three files holding waived hits,
exactly ONE carries tabs at all — `tools/memory-tree/check-memory-hygiene.sh` — and rev-2 said two.
Fourteen tracked files outside `memory/` carry tabs, so the class is reachable and the parse rule is
stated rather than discovered.

Comment lines: "a line with no tab is a comment", the rule the memory-tree kit settled on after this
class bit it twice. rev-1's §4 worried that a waived line beginning with `#` would collide with a
leading-`#` convention. **It cannot**: a row begins with the PATH, so a waived line's own `#` never
lands at column 0. Two of the eight rows do point at `#` comment lines and neither collides. The
worry is withdrawn and the rule kept, because it is the right rule for a different reason.

### Inventory

Eight rows across three files, plus the header. Measured at HEAD and identically at BASE `60ba1d60`
with `grep -vE '^[[:space:]]*(#|$)' tools/dead-path-waivers.txt`, and confirmed by
`bash tools/check-dead-paths.sh --list`, which prints eight waived hits over three files.

Re-keying all eight by line text today yields exactly one match each, and none contains a tab. **The
ambiguity case has an empty population at BASE** — a green starting state worth pinning here rather
than leaving as an unknown, and the reason S7's ambiguity arms need staged fixtures.

`tools/check-dead-paths.sh` defines no `fail() {` helper and has zero `fail <n> "` call sites, so it
is outside `check-arms.py`'s discovered population today (that checker reports ten pairs and no
dead-paths checker). It enters that population only if the rewrite adopts the helper, which is why
§7's mention of that leg is conditional rather than asserted.

### Refusal ORDER, which rev-2 got wrong by not thinking about it

`check-dead-paths.sh` reports UNWAIVED carriers and exits before it reaches the stale-row loop. So for
any change that leaves a line both a hit and no longer waived — a rewording is exactly that — the
message a reader sees is "this hit is not waived", never "this row is stale". rev-2's AC3 asserted the
stale message for a rewording and could not have been satisfied.

This unit does NOT reorder those two reports; reordering them is a behaviour change nobody ruled and it
would hide an unwaived carrier behind a bookkeeping complaint. It states the order, and AC3 asserts the
message the checker actually emits.

### Migration

One commit. Every row is rewritten and the checker changes with them; a half-migrated file matches
nothing and would red every row as stale, so the two halves cannot be split. That property is what
keeps the population error below blocker severity — but AC6 in rev-1 said "the four existing rows",
which would have certified four of eight and is corrected.

### Alternatives rejected

**Key on PATH alone.** The keying `adopt-memory-tree.sh`'s own comment recommends, and immune to line
drift. Rejected by the owner: a file carrying several waived mentions would get one waiver covering
all of them, which is wider than the fault and hides the next one. The measured population makes this
concrete — `check-memory-hygiene.test.sh` alone carries four rows with four different reasons.

**Text alone, with an ambiguity REFUSAL and no ordinal.** rev-1's design. Rejected on the audit's
finding that it leaves the ambiguity case with no legal remedy: two identical hit-carrying lines in one
file would red permanently, with no row an author could write to waive them and nothing in the spec
saying what to do. The ordinal makes the case representable, and it reuses a shape this tree already
runs.

**Leave it line-keyed.** Rejected. It cost this repo two cycles in one build, and the second re-key was
first performed by proximity and scrambled three rows onto the wrong reasons — a failure the keying
invites rather than merely permits.

### The awk trap, recorded because it will be hit during implementation

Comparing a row's text with `awk -v t="$txt" '$0==t'` is WRONG and fails on live data: awk expands
backslash sequences in a `-v` assignment, so a waived line containing `\n` compares unequal to itself.
Measured on the real row at `check-memory-hygiene.test.sh:1314`, awk reports 0 matches where Python
reports 1. It fails RED rather than green, so it would be caught — but it would be caught as a
mysterious stale row, so it is named here. Pass the text through a file or an environment variable, or
compare outside awk.

### Files touched (estimate)

`tools/check-dead-paths.sh` · `tools/dead-path-waivers.txt` · `tools/check-dead-paths.test.sh` (the
three arms at lines 109-125 all need rewriting) · `WIRE-INTO-PROJECT.md` and
`tools/memory-tree/check-memory-hygiene.sh` are NOT edited — they are the waived subjects, not
carriers of the grammar · `tools/govkit/registry.toml` for S6 · `memory/DECISIONS.md` for this unit's
ruling row.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the comparison is rebuilt as a multi-field set difference over eight rows. Not "one
  string comparison instead of one integer comparison": see S4.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an empty registry is legal and means nothing is waived, which is
  the file's stated fully-strict state and is unchanged.
- observability — the refusal messages name the row and the file, as they do now; the ambiguity
  refusal also names the occurrence count and the ordinal an author would have to supply.
- risks — the staleness semantics (S3) are the real risk, because the weaker predicate looks correct
  and passes every arm written against today's tree. The `STATUS.md` needle is the concrete case and
  it gets its own arm.
- read path — this unit touches no capped read-path member except its own `memory/DECISIONS.md` row.
  That row is priced and the ceiling moved with it, per this build's rules slot; at BASE the path has
  60 B of headroom and one decision row has historically cost ~122 B, so the movement is not optional.
- testing + left-shift gates — S9's arms. THREE of them are green by construction (a matching row, a
  different line inserted above a waived hit, two identical lines with two rows) and are not staged
  breaks; the stage-the-break rule binds the refusal branches, which is the rest. rev-2 said "seven
  arms, each observed RED", which would have been impossible for three of them.
- migration / rollback — one commit, invertible; the old rows are recoverable from git.
- user docs — the file's own header states the new grammar and why the key moved; S6 corrects the three
  other sites that assert the old one.

## 6. Acceptance criteria

Every criterion below names a witness. Where one is GREEN AT BASE it says so and is kept as a
regression guard, not offered as coverage this unit adds.

- **AC1** — When a row's text matches exactly one line in its file and its ordinal is 1,
  `bash tools/check-dead-paths.sh` waives that mention and exits 0.
- **AC2** — When a DIFFERENT line is inserted above a waived hit, `bash tools/check-dead-paths.sh`
  still exits 0 with no row edited. This is the failure the ruling exists to remove; staged and
  observed.
- **AC3** — When a waived line is REWORDED, `bash tools/check-dead-paths.sh` exits 1. The message is
  the UNWAIVED-CARRIER one, not the stale-row one, because that report comes first and exits — the
  criterion asserts what the checker emits rather than what would read better.
- **AC4** — When a waived line leaves the HIT set — staged by re-adding a tracked file named
  `STATUS.md` — `bash tools/check-dead-paths.sh` exits 1 naming the affected rows, exactly as it does
  at BASE. This is the property rev-1's predicate silently dropped.
- **AC5** — When a file holds TWO identical hit-carrying lines and the registry holds ONE row for
  them, `bash tools/check-dead-paths.sh` exits 1 on the unwaived occurrence. When it holds TWO rows,
  ordinals 1 and 2, it exits 0. Waiving one of N never clears the other N−1.
- **AC6** — When a row's ordinal is absent, zero, non-numeric, or greater than the occurrence count,
  `bash tools/check-dead-paths.sh` exits 1 naming the row MALFORMED, in a message distinct from the
  stale one.
- **AC7** — When an IDENTICAL line is inserted above a waived hit,
  `bash tools/check-dead-paths.sh` exits 1. This is the residual S2 names, and it is armed rather than
  argued away.
- **AC8** — When a row names a file that no longer exists, `bash tools/check-dead-paths.sh` exits 1
  naming it stale. **GREEN AT BASE** — the set difference already produces this — and kept as a
  regression guard.
- **AC9** — When all eight existing rows are migrated, `git diff` shows each keeping its reason
  verbatim, and `bash tools/check-dead-paths.sh` exits 0 on the migrated tree. Eight is derived by
  `grep -vcE '^[[:space:]]*(#|$)' tools/dead-path-waivers.txt` at BASE, not read from this sentence.
- **AC10** — When `bash tools/run-gates/run-gates.sh` runs, the `dead-path carriers` leg, its
  self-test leg, `govkit selfcheck` and `codebase-map coverage + freshness` are all green.
- **AC11** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both totals
  are recorded and `.memory-tree.conf` carries this unit's own movement line, per S10.

## 7. Gates

`dead-path carriers` · `dead-path carriers self-test` · `govkit selfcheck` (unguarded — runs on every
bar) · `codebase-map coverage + freshness` (unguarded, and S11's subject) · `memory hygiene` (incl.
check 16) · `check-testsuite-counts.sh` · `check-arms.py` floors ONLY IF the rewrite adopts the `fail`
helper, which it does not today.

## 8. Open questions

- **F1 — is whitespace normalisation the right tolerance?** RESOLVED (agent, 2026-08-25, delegated) —
  leading and trailing only. Tabs inside a line are part of its text and §4's parse rule handles them.
  A re-indent must not unpin a waiver, and anything wider starts matching lines the author did not
  mean.
- **F2 — does `install-prefix-waivers.txt` follow?** RESOLVED (agent, 2026-08-25, delegated) — NO. It
  carries twelve rows in the same shape with the same exposure and is the file `check-dead-paths.sh`
  claims parity with, but the owner ruled ONE file and a registry moves when its own keying has
  actually failed, not by association. S6's corrected parity sentence must say the divergence is
  DELIBERATE, so the next reader does not "restore" it — that clause is the whole cost of this
  answer.

## 9. Revision log

- rev-5 · 2026-08-25 · BUILT and CLOSED. All eleven criteria observed against the REAL tree before
  any arm was written; the ledger is in this unit's build record. Arms 3 -> 13.
- rev-4 · 2026-08-25 · M3 fork sweep. F1 and F2 resolved as specced; F2's answer carries a cost —
  S6's corrected parity sentence must say the divergence from the sibling registry is deliberate.
- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s fifth park.
- rev-3 · 2026-08-25 · round-2 fold. Restated S3's staleness as a MEMBERSHIP test after round 2 found
  the needle formulation is not computable — the checker attributes no needle to any row, and two
  waived lines name two needles each. Added S7 (N identical lines need N rows) and rewrote AC5, which
  rev-2 had asserting an outcome the checker's own shipped arm contradicts. Made the ordinal mandatory
  and gave malformed ordinals their own refusal (S8, AC6), removing rev-2's contradiction between a
  four-field grammar and arms for a row with no ordinal. Corrected the `unarmed-branches.txt` citation:
  its ordinal is POSITIONAL and its header records it drifting on insertion, so the shape is borrowed
  and the counting rule deliberately is not. Added the refusal-ORDER section and fixed AC3 to assert
  the message that actually prints. Took the read-path charge as declared scope (S10) and the
  install-prefix dossier refresh (S11) with its unguarded gate leg. Corrected the tab claim from two
  files to one, named the reason-field constraint, added the grammar sentence S6 had missed, and
  dropped line-number citations after round 2 found one off by three.
  AC numbering was RESEQUENCED in this revision; AC labels in the entries below refer to the
  numbering of the revision that wrote them, not to this one.

- rev-2 · 2026-08-25 · spec-audit fold. Population corrected from four rows in one file to eight across
  three, at BASE as well as HEAD (S5, AC7). Staleness semantics corrected: the checker derives its hit
  set and rev-1's predicate was strictly weaker (S3, AC4). Added the ordinal, reusing
  `unarmed-branches.txt`'s shape, because the bare ambiguity refusal had no legal remedy (S2, AC5).
  Took the set-difference restructure into scope, which rev-1 described as swapping one comparison
  (S4). Added S6 for the three other sites asserting the old grammar. Corrected the reuse audit's
  false negative finding and the non-goal that named the wrong sibling. Recorded the awk `-v` trap and
  withdrew the `#`-collision worry.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `dead path waiver registry keyed line number text stale
row insertion unpin shrink only carriers ordinal signature`.

**rev-1 recorded that no checker in this tree matches a waiver by line text. That was false, and the
way it was false matters more than the fact.** `memory/project/unarmed-branches.txt` is
`gate<TAB>check<TAB>ordinal<TAB>signature` — shrink-only, stale on rewording, with a header recording
the same insertion-above-a-pin failure that earned this ruling — and `check-arms.py`'s docstring
explains its capture rule. The evidence rev-1 cited was a grep over `tools/*.sh`, and the checker is a
`.py` file, so the predicate could not have found the answer whatever the answer was. That is this
tree's vacuous-selector class appearing in a reuse audit rather than in a gate, and it is why S2 now
reuses that shape instead of inventing a refusal.

The second seam is `tools/install-prefix-waivers.txt` with the parity claim at
`check-dead-paths.sh:51` — a sibling deliberately not changed, whose claim S6 corrects.
`memory/project/method-carriers.txt` keys on PATH alone and is what `adopt-memory-tree.sh` recommends;
it is rejected above on the owner's ruling, not overlooked.
