# TOOL-dHonouredPark-3 — the dead-path waiver registry keys on line TEXT plus an occurrence ordinal, not a line NUMBER

**Status:** SPECCED · rev-2 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 2 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-4 |

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
- **S2** — the ORDINAL is the audit's correction and is not an invention. `memory/project/
  unarmed-branches.txt` is `gate<TAB>check<TAB>ordinal<TAB>signature` — shrink-only, stale on
  rewording, and its own header records the SAME insertion-above-a-pin failure that earned this
  ruling. Its ordinal field is exactly the disambiguator a text key needs. The ordinal counts
  occurrences of the TEXT, never lines of the file, so an insertion above a waived hit does not move
  it; only adding another identical line does, which is the case it exists to name.
- **S3** — staleness keeps the meaning it has today. `tools/check-dead-paths.sh:156` computes
  `stale_rows` as a set difference of `waived_rows` against the HIT set, and the hits derive from the
  needle set built at lines 71-108 (deleted basenames minus tracked basenames). A row is therefore
  stale when its needle leaves the derivation, NOT merely when its line vanishes. rev-1's predicate —
  "a row whose text matches no line in that file" — is weaker and would let the four rows covering
  `check-memory-hygiene.sh:554` and `.test.sh:1314/1319/1375` survive silently the moment any tracked
  file is named `STATUS.md`, waiving nothing while reporting green. Both conditions red: a row whose
  needle left the derivation, and a row whose text matches no line.
- **S4** — the SET-DIFFERENCE machinery is restructured, because it cannot survive the key change
  unmodified. `check-dead-paths.sh:133-152` parses rows with `awk '{print $1}'` — whitespace-split,
  which a tab-delimited grammar breaks outright — and computes `unwaived` and `stale_rows` with
  `grep -vxF -f` over single `<path>:<line>` tokens. Text keying makes both sides multi-field records,
  so the comparison is rebuilt rather than having one operator swapped. This is the largest part of the
  diff and rev-1 described it as "one string comparison per hit instead of one integer comparison".
- **S5** — the existing rows are MIGRATED, each keeping its reason verbatim and gaining the text of the
  line it currently points at plus its ordinal. There are EIGHT, across THREE files: two in
  `WIRE-INTO-PROJECT.md`, two in `tools/memory-tree/check-memory-hygiene.sh` (including the `:554` row
  the parent build's park entry names as the incident that earned this ruling), and four in
  `tools/memory-tree/check-memory-hygiene.test.sh`.
- **S6** — the three OTHER documentation sites are corrected in the same commit, because each states
  the old grammar as fact: `check-dead-paths.sh:50-51`, which pins the grammar as "matching
  `install-prefix-waivers.txt` exactly" and becomes permanently false rather than merely stale;
  `dead-path-waivers.txt:15-18`, which documents a line-keyed re-stamp protocol this unit deletes; and
  `tools/govkit/registry.toml:191-192`, whose exemption reason reads "Its rows are gov paths and gov
  line numbers".
- **S7** — arms for: a matching row, a row whose needle left the derivation, a row whose text matches
  no line, an ambiguous row with no ordinal, an ambiguous row WITH an ordinal, an insertion above a
  waived hit (which must now be a no-op), and a REWORDING of a waived line (which must red).

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
No waived line carries a tab today — verified over all eight — but fourteen tracked files do carry
tabs and two of them already hold waived hits, so the class is reachable and the parse rule is stated
rather than discovered.

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
- testing + left-shift gates — seven arms, each observed RED against a staged break before it lands.
- migration / rollback — one commit, invertible; the old rows are recoverable from git.
- user docs — the file's own header states the new grammar and why the key moved; S6 corrects the three
  other sites that assert the old one.

## 6. Acceptance criteria

- **AC1** — When a row's text matches exactly one line in its file and its ordinal is 1,
  `bash tools/check-dead-paths.sh` waives that mention and exits 0.
- **AC2** — When a line is INSERTED above a waived hit, `bash tools/check-dead-paths.sh` still exits 0
  with no row edited. This is the failure the ruling exists to remove, and it is staged and observed.
- **AC3** — When a waived line is REWORDED, `bash tools/check-dead-paths.sh` exits 1 naming that row
  as stale.
- **AC4** — When a row's needle leaves the derived set — staged by re-adding a tracked file named
  `STATUS.md` — `bash tools/check-dead-paths.sh` exits 1 naming the affected rows, exactly as it does
  at BASE. This is the property rev-1's predicate silently dropped.
- **AC5** — When a row's text matches more than one line in its file and the row carries no ordinal,
  `bash tools/check-dead-paths.sh` exits 1 naming the row and the count. When the same row carries an
  ordinal in range, it exits 0 and waives that occurrence alone.
- **AC6** — When a row names a file that no longer exists, `bash tools/check-dead-paths.sh` exits 1
  naming it stale.
- **AC7** — When **all eight** existing rows are migrated, `git diff` shows each keeping its reason
  verbatim, and `bash tools/check-dead-paths.sh` exits 0 on the migrated tree. Eight, derived by
  `grep -vcE '^[[:space:]]*(#|$)' tools/dead-path-waivers.txt` at BASE rather than read from this
  sentence.
- **AC8** — When `bash tools/run-gates/run-gates.sh` runs, the `dead-path carriers` leg, its
  self-test leg and `govkit selfcheck` are all green. The last two are named because S6 edits
  `registry.toml` and S7 edits the test file, and rev-1's §7 omitted both.
- **AC9** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both totals
  are recorded and `.memory-tree.conf` carries this unit's own movement line, per this build's rules
  slot.

## 7. Gates

`dead-path carriers` · `dead-path carriers self-test` · `govkit selfcheck` (unguarded — runs on every
bar) · `memory hygiene` (incl. check 16) · `check-testsuite-counts.sh` · `check-arms.py` floors ONLY
IF the rewrite adopts the `fail` helper, which it does not today.

## 8. Open questions

- **F1 — is whitespace normalisation the right tolerance?** Leading and trailing only. Tabs inside a
  line are part of its text and the parse rule in §4 handles them. Recommendation: as specced — a
  re-indent should not unpin a waiver, and anything wider starts matching lines the author did not
  mean.
- **F2 — does `install-prefix-waivers.txt` follow?** It is the file `check-dead-paths.sh:51` claims
  parity with, twelve rows in the same shape with the same exposure. The owner ruled one file, and S6
  corrects the parity sentence rather than the sibling. Recommendation: no, and it moves only when its
  own keying has actually failed — but the corrected sentence should say the divergence is deliberate,
  so the next reader does not "restore" it.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s fifth park.
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
