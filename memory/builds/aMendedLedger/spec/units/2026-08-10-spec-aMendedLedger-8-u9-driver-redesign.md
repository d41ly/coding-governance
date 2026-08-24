# TOOL-aMendedLedger-8 — U9: the merge driver, redesigned around what git already gets right

**Status:** SPECCED · rev-2 · 2026-08-10 · node a · Tier-2 · base 663ca427 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md](../../build/2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md) | journal | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 |
| [2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 |
| [2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 |
| [2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 |
| [2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md](../../reviews/2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 |

<!-- /gen:spec-records -->

## 1. Goal

Replace the merge algorithm in `tools/memory-tree/merge-rows.py` with one that delegates every
non-row line to `git merge-file` and key-merges only the row set, because three adversarial review
rounds established that `git merge-file` is correct at exactly the thing the driver keeps corrupting
(structure) and wrong at exactly the thing the driver exists for (a row line duplicated at rc 0).
Six defects are live at HEAD after three patch attempts, two of them regressions that a green 38-leg
bar did not see, so this unit redesigns rather than repairs.

## 2. Scope (IN)

- **S1** Replace the merge algorithm in `tools/memory-tree/merge-rows.py` with the two-plane
  pipeline of §4 Data model: tokenize every row-shaped line, merge the resulting skeleton with
  `git merge-file`, key-merge the row set separately, then reconcile the two.
- **S2** Delete the machinery the redesign retires, named in §4 Migration, rather than leaving it
  unreachable: `split_regions`, `rows`, `lead` and its two dedup regimes, the `%B`-only splice with
  its `%A`-only skip, and the emit-site audit counters.
- **S3** Add the row-conservation postcondition: for every key, the COUNT of that key's row lines in
  the written file equals the count the row plane resolved to, multiplicity counted on both sides.
  This is the assertion that makes "the driver never drops a row" a checked property on every merge
  instead of an unverified replay claim. It is a CONSERVATION check and explicitly not a uniqueness
  check — a file may legitimately carry the same row-shaped line twice (§4 The postconditions).
- **S4** Add the structure-identity postcondition: the written file's non-row, non-marker lines
  equal the merged skeleton's non-token, non-marker lines, in order and byte for byte. Markers are
  excluded on BOTH sides; excluding them on one side only makes the check fire on every conflicted
  merge (§4 The postconditions).
- **S5** Rebuild the audit line so every number is derived from the written bytes and the three
  inputs after the fact, and so it reports the keyed-versus-hashed split of the row population.
- **S6** Make every synthesized marker line carry the file's dominant line terminator, at all three
  synthesis sites (§4 Newline contract).
- **S7** Rebuild `tools/memory-tree/merge-rows.test.sh` around the never-worse bar: every case runs a
  live `git merge-file` control on the identical three blobs, the comparison is mechanical, and the
  count of cases where the driver conflicts and git resolves is asserted against a shrink-only
  constant in the test file.
- **S8** Add fixtures for the eight corpus cases that have no fixture group today — C2, C4, C8, C15,
  C16, C19, C21, C22 — as enumerated in §6.
- **S9** Re-verify `tools/check-wiring.sh`'s merge smoke against the new pipeline and close the new
  inertness channel the redesign opens (§4 Rollout, `check-wiring.sh:332-346` and `:357-371`).
- **S10** Land the coupled edits: the kit version bump, `check-verdict-epoch.sh`'s `DELEGATES`, the
  `memory/map/features/memory-tree-merge-driver.md` dossier, `tools/memory-tree/README.md:27-28`,
  `AGENTS.md:76`, and the reword of the `memory/backlog/TOOL.md:21` row that scopes this work as a
  fourth patch.
- **S11** Neutralise `merge.conflictStyle`. The reconciliation rules are defined over a two-sided
  conflict region; a node-local `diff3`/`zdiff3` config makes `git merge-file` emit a third
  `||||||| base` section, which silently deletes rule 3 and with it every auto-resolve this unit
  exists for (§4 The conflict-style hazard). The requirement is that the region shape reaching rules
  3 and 4 cannot be changed by an adopter's git config; the MECHANISM is §8 F8 and is not the
  builder's to pick alone.

## 3. Non-goals (OUT)

- **Deciding whether the driver stays wired in this repo.** The two `merge=rows` lines in
  `.gitattributes` and each node's `merge.rows.driver` config are an OWNER decision. This repo has
  had 13 merges and zero index collisions, so nothing here is urgent; the kit is copy-installed and
  the adopter it is for saw 312 index conflicts. The builder must NOT add, remove or edit a
  `.gitattributes` `merge=rows` line, and must not change the wiring doctrine in
  `tools/memory-tree/README.md:82-107`.
- **Widening the anchor grammar.** `tools/memory-recall/extract.py` is out of bounds. The remaining
  unkeyable population is a SEPARATOR gap, not an era gap — `extract.py:115` (`A_BOLD_LI`) requires
  `[-—:·]` after the id and `extract.py:119` (`A_DASH`) requires `[·|]` — and no era widening can
  grant a separator. The redesign is built so that keying is not what unlocks the auto-resolve.
- **Packaging the kit for adopters.** `adopt-memory-tree.sh` still does not install the driver, and a
  copy-installed kit at `<root>/memory-tree/` cannot reach `tools/lib/pyrun.sh`. Recorded in the
  dossier §Gaps and left there.
- **A scoped-hunk refusal.** A postcondition violation stays a whole-file conflict. Ordinary
  conflicts become naturally scoped as a side effect of the redesign (§4 Reconciliation), which is
  most of what the ergonomics complaint was about.
- **A degraded mode when the anchor grammar cannot be read.** The redesign could fall back to
  hashing every row and still beat `git merge-file`, and it must not: silently merging under a
  different rule than the one configured is this repo's `two-answers-to-one-question` class. See §4
  Alternatives rejected.
- **A new `memory/project/*.txt` registry** for the conservative-case tally. See §4 Alternatives
  rejected.
- **A second driver module beside the existing one.** See §4 Alternatives rejected.

## 4. Design

### Data model

The file is partitioned into two planes by ONE stateless predicate applied to each line in
isolation.

| plane | predicate | who merges it |
|---|---|---|
| ROW | `_ROW_RE` — `^\s*[-*]\s`, `merge-rows.py:276`, unchanged | the driver, keyed |
| STRUCTURE | every other line | `git merge-file`, positionally |

The partition is the ROW SHAPE, never the anchor grammar, and that is carve-out 1. Measured at HEAD,
`memory/DECISIONS.md` is 74 of 74 rows keyed and `memory/backlog/TOOL.md` 18 of 18 after the
`TOOL-aMendedLedger-7` widening, but a row carrying an id and no separator still does not key and
never will. Partitioning by the grammar would hand `git merge-file` exactly the row lines it is
measured to duplicate at rc 0 — the one corruption git commits — and rebuild the defect on the other
side of the split.

The two planes are recombined through a SKELETON, and the skeleton is what makes the recombination
ordered rather than guessed.

**The skeleton.** For each of `%O`, `%A`, `%B`, produce a line list of the same length and order in
which every ROW line is replaced by a single token line and every STRUCTURE line is passed through
byte for byte. The token is:

| row | token |
|---|---|
| `key(line)` returns an id | `\x01row:<id>\x01` |
| `key(line)` returns None | `\x01raw:<hex digest of the STRIPPED line text>\x01` |

The token carries the source row's own line terminator, including the empty terminator of an
unterminated final line. Hashing the STRIPPED text is what makes line form unable to smuggle a
duplicate: a final copy with no newline and an interior copy with one produce the same token.

**And the terminator does not survive the round trip.** Tokenization is the only place the SOURCE
row's terminator is used. On the way back, a row line substituted for a token takes the terminator of
the TOKEN's position in the merged skeleton, never the terminator it carried in its source blob.
This is newline Site 7 and it is a fold-in, not a refinement: measured on 2026-08-10, ours appending
an unterminated `- TOOL-zOurs-<n> · ours` while theirs appends a terminated row makes rule 3 emit ours'
token first, the empty terminator rides along, and `"".join(out)` fuses two records into one line —
`- TOOL-zOurs-<n> · ours- TOOL-zTheirs-<n> · theirs`, rc 0, no markers, audit line `clean`. The control
`git merge-file` returns rc 1 with both rows intact. The same glue reaches rule 2 whenever the merge
relocates a formerly-final row away from end of file. Both are silent rc-0 corruption of an
append-only record on the ordinary input "one node's editor left no trailing newline", which is the
exact signature §5 risks names.

Two preconditions, both fail-closed: no input line may contain `\x01`, and no line of the final
output may contain `\x01`. The first makes tokenization unambiguous; the second catches a
reconstruction bug before it reaches the worktree.

**Why the token for a keyed row is its id and not its text.** An edit to a keyed row must be
invisible to the structure plane, otherwise every row edit becomes a structural change and git
starts arbitrating record text — which is where duplication comes from. Measured on a reconstructed
C14 (a heading renamed on theirs, the row under it edited on ours): the skeleton of ours is
byte-identical to the skeleton of base, `text_merge`'s `o == a` short-circuit takes theirs, the
rename survives, and the row plane independently takes ours' edit. `git merge-file` on the raw blobs
returns rc 1 on that same input.

**The row plane** is a pure per-key decision with no ordering. Build `O`, `A`, `B` as key → the LIST
of row lines carrying that key, in input order — **never key → a single line**. A markdown file may
legitimately carry the same row-shaped line twice (two identical `  - notes` sub-bullets under two
different rows is ordinary), and a `key → line` plane collapses those two copies into one before any
postcondition can see it. Then decide `resolved[key]`, which is itself a LIST:

| state | `resolved[key]` |
|---|---|
| in `%A` only | ours' line |
| in `%B` only | theirs' line |
| in `%A` and `%B`, not `%O`, identical | that line |
| in `%A` and `%B`, not `%O`, different | conflict block |
| in all three, `%A` = `%B` | that line |
| in all three, `%O` = `%A` | theirs' line |
| in all three, `%O` = `%B` | ours' line |
| in all three, all different | conflict block |
| in `%O` and `%A`, `%O` = `%A` | empty — theirs deleted it, honour |
| in `%O` and `%A`, `%O` ≠ `%A` | conflict block — delete/modify |
| in `%O` and `%B`, `%O` = `%B` | empty — ours deleted it, honour |
| in `%O` and `%B`, `%O` ≠ `%B` | conflict block — modify/delete |
| in `%O` only | empty — both deleted |

**Multiplicity.** Each cell above compares the key's list, and the resolved list's LENGTH is
`max(len(A[key]), len(B[key]))` on every branch that keeps content — the same max-over-inputs rule
`_over()` already applies at `merge-rows.py:360-372`, applied here instead of being left to a
postcondition. Two consequences, both measured on 2026-08-10 against a `key → line` prototype and
both fatal to it. (a) An IDENTITY merge (`%O` = `%A` = `%B`) of a file carrying a repeated row line
resolved that key to ONE line while the skeleton carried its token TWICE, so rule 2 wrote it twice
and a uniqueness-shaped `no_row_loss` refused — `RowLoss: key 'raw:377dbc1c9ca5618c': written 2x,
resolved to 1`, a 15-line whole-file marker sandwich where both `git merge-file` and the driver at
HEAD return the input byte for byte. That is a permanent whole-file conflict on every merge of that
path with no author action that stops it. (b) Inside a conflict region the same collapse runs the
other way and silently UNDER-writes; that is rule 3's half of the defect and it is stated there.

Neither reaches a fixture drawn from the governed files: measured at HEAD, `memory/DECISIONS.md` and
all four `memory/backlog/*.md` shards carry zero duplicate row lines and zero nested rows, so AC18
passes on them by accident. §4 Ambiguous lines declares `  - sub-bullet` to be ROW and hashed, this
kit is copy-installed, and the adopter's corpus has not been measured. The fixture must therefore be
authored rather than harvested — AC21.

The delete comparison is now the row LINE alone, and that is correct rather than a relapse. The
defect that forced the lead-in-plus-anchor comparison was that a side which filed content ABOVE a
deleted row read as untouched and the `continue` past `lead(k)` discarded what it filed. In the
redesign there is no lead-in: adjacent structure lines are on the other plane and are merged by git,
and an adjacent ROW is a separate key with its own decision. The concept the repair repaired no
longer exists.

A `raw:` key cannot be "in both sides with different text", because different text is a different
key. Editing an unkeyable row therefore reads as a delete of the old key plus an add of the new one,
which resolves correctly in the one-sided case and keeps both wordings in the both-sides case. That
last outcome is deliberate and is guarded: if the row carries an id, the id postcondition refuses it
(the C11 mechanism); if it carries none, it is a note and not a record, and keeping both is what an
append-only record does.

### Reconciliation

Merge the three skeletons with `git merge-file` through the existing `text_merge` contract, then
walk the merged skeleton and apply four rules in this order:

1. **A structure line outside a conflict region** is emitted byte for byte.
2. **A token outside a conflict region** is replaced by the NEXT UNCONSUMED entry of
   `resolved[key]` — one line, or nothing when a delete was honoured, or a marker block. Each
   occurrence of a key's token consumes one entry, so a key of multiplicity 2 whose token appears
   twice writes both entries and a key of multiplicity 1 whose token appears twice is a conservation
   failure that `no_row_loss` refuses (that is the C7 mechanism, and it is now stated rather than
   emergent). The substituted line carries the TOKEN's terminator, never its source blob's — Site 7.
3. **A conflict region whose ours-side and theirs-side both consist ENTIRELY of tokens** is resolved
   by POSITIONAL concatenation: ours' tokens in order, then theirs' tokens in order, each token
   substituted through rule 2. A token on THEIRS' side is suppressed only when the same key also
   occurs on OURS' side. **Dedup happens across sides and never within a side.** An empty side counts
   as token-only.
4. **Any other conflict region** is emitted as a conflict, the verdict becomes CONFLICT, and each
   token inside it is replaced by the row line from the SIDE OF THE REGION IT APPEARS ON — never by
   `resolved[key]`. No marker is ever written inside a region.

Rule 3 is the whole design. Both sides of a diff hunk sit between the same context lines, so when
every disputed line is a row, section membership is not in dispute — only order among siblings,
which is not semantic, because ids are labels and not ranks. Rule 4 is its converse: the moment a
structure line is in dispute, the structure is in dispute, and structure is precisely the class git
is right about and the driver has been wrong about three times.

Stated as one sentence a reviewer can hold: **the driver may auto-resolve where git conflicts only
when every disputed line is a row token; a disputed structure line is always a conflict.**

**Why rule 3 dedups across sides and never within one.** An earlier wording — "each distinct key
emitted once" — rebuilt the file-wide lead-in dedup on the row plane, where nothing guards it.
Measured on 2026-08-10: base `# t` plus one row; ours appends `- repeated bullet`,
`- TOOL-zOurs-<n> · ours`, `- repeated bullet`; theirs appends one row at the same point. `git
merge-file` refuses at rc 1 with the structure intact, the driver at HEAD returns rc 0 with both
copies of ours' note present and is CORRECT, and the distinct-key prototype returns rc 0 having
DELETED one of ours' own lines from an append-only record, audit line `clean`. No postcondition sees
it: `no_new_duplicates` is a max-cap so under-writing is invisible, `no_misfiled_rows` inspects only
keyed rows' headings, `structure_identity` covers non-row lines, and a `resolved[key]` that is a
single line does appear exactly once. It is also a REGRESSION the redesign would introduce — HEAD is
right here — which is why the fixture is mandatory (AC22) and why the rule is stated as positional
concatenation rather than as set union.

**Why rule 4 substitutes per side.** Rule 3 says its tokens go through rule 2, and rule 2's value can
itself be a marker block; read across, rule 4 would nest a conflict inside a conflict. `settled()`
(`merge-rows.py:305-327`, retained unchanged) tracks a single boolean, so the inner `>>>>>>>` closes
the outer region early and the remainder of the outer region leaks into the view all four
postconditions run over. Reachable through the delete/modify branch, measured on 2026-08-10: base one
row under `## H`; ours edits that row and appends a second; theirs deletes the row and renames the
heading. The merged skeleton is one region, ours' side is `['## H', row:aOne-<n>, row:aOne-<m>]` — not
token-only, so rule 4 — while `resolved['row:TOOL-aOne-<n>']` is a conflict block. Nested, `settled()`
returns four lines of an unresolved region as if they were output; per side it returns two. Nothing
catches the difference: `no_row_loss` excludes both conflict-block keys and rule-4-region keys by its
own wording, and `structure_identity` compares equal.

### The conflict-style hazard

`git merge-file` honours the invoking repo's `merge.conflictStyle`. Measured on git
2.54.0.windows.1 on 2026-08-10: with the repo config unset, `git merge-file -p -L ours -L base -L
theirs` emits the two-sided form; with `diff3` OR `zdiff3` set it emits a third `||||||| base`
section carrying the base lines, at rc 1. It is a no-op only when the cwd is outside a repository —
git runs a merge driver from the top of the worktree and `text_merge` (`:459-486`) passes no cwd, so
the driver inherits the config INSIDE the repo. Neither this repo's local nor global config sets it
(both `git config --get` return rc 1), so a fixture suite authored here is blind to the shape.

Rules 3 and 4 are defined over an ours side and a theirs side. Under three sides a stranger has two
natural implementations and both are wrong:

- split only on `=======`, so `||||||| base` and the base lines land on the ours side — the region is
  no longer token-only, and where it is, base tokens both sides deleted get re-emitted;
- treat `||||||| base` as a non-token line — then EVERY region falls to rule 4.

Measured on the C1 shape (two nodes each opening the empty `## DEPL` section, base `*(none yet)*`):
default style gives ours 1 token / theirs 1 token, rule 3, rc 0, heading once, both rows filed. With
`merge.conflictStyle=diff3` the same three blobs give ours 1 token / base 1 STRUCTURE line
(`*(none yet)*`) / theirs 1 token, the token-only predicate fails, and C1 flips to rc 1 with markers.
So C1, C2, C9 and C15 — every BETTER-than-git row in the §6 table, the auto-resolves carve-out 2 says
rule 3 exists to buy back — vanish on any node that set a conflict style, and the same driver returns
different verdicts per node on identical blobs, which §3 names as this repo's own
`two-answers-to-one-question` class.

The driver already knows the shape and the redesign was dropping the knowledge: `merge-rows.py:296-300`
records that `|||||||` is written "under `diff3` style, which is a per-node config this driver does
not set", and `settled()` is written diff3-safe by discarding everything between the outer pair. HEAD
survives on that; the redesign makes a region's INTERNAL shape load-bearing for the first time.

The remedy is verified — `git -c merge.conflictStyle=merge merge-file …` restores the two-sided form
with the repo config set — but it amends `text_merge`, which §4 Migration and §10 both currently
declare untouched, and it overrides a config the adopter chose. **F8 decides which remedy lands; the
builder must not pick it alone.** Either way AC23 requires a fixture that sets
`merge.conflictStyle=diff3` in the scratch repo and asserts C1 still resolves at rc 0.

### Carve-out 2 — furniture that rides with a row

Four of the corpus's thirteen corruption cases live on the boundary where a `## FAMILY` heading or a
`*(none yet)*` placeholder is consumed by the first row of an empty section. **The choice is: such
furniture is on the STRUCTURE plane, attached to nothing, and merged positionally by git.** There is
no lead-in, no lead-in dedup and no adjacency scope. Both narrowings the third round made — the
adjacency dedup at `merge-rows.py:580-582` and the blank-lead-in exemption at `:578-579` — are
deleted rather than re-tuned, because their intersection is what produced C2 and each of them
individually was load-bearing for a different case.

The cost this choice is normally expected to carry is the headline auto-resolve: `git merge-file`
returns rc 1 on C1 and C2, so pure delegation would lose the case the unit exists for. Rule 3 buys
it back. Measured on reconstructed fixtures in a scratch directory on 2026-08-10:

| shape | `git merge-file` on the raw blobs | `git merge-file` on the SKELETON | region shape |
|---|---|---|---|
| C1, one row per side into the same empty section | rc 1 | rc 1, one region | ours 1 token, theirs 1 token — token-only |
| C2, three lines per ours including an unkeyable row | rc 1 | rc 1, one region | ours 3 tokens, theirs 1 token — token-only |
| C3, `### ` sub-heading added in two sections | rc 0 correct | rc 0, both sub-headings present | no region |
| C4, a lead-in note that legitimately repeats | rc 0 correct | rc 0, both note copies present | no region |
| C5, an insert in each of two sections | rc 0 correct | rc 0, both rows in their own sections | no region |
| C14, heading renamed on theirs, row edited on ours | rc 1 | rc 0, ours' skeleton equals base's | no region |
| C15, a different unkeyable row appended on each side | rc 1 | rc 1, one region | token-only |
| C16, two DIFFERENT empty sections opened | rc 0 correct | rc 0, four headings once each | no region |

So C1 and C2 reach rule 3 and auto-resolve with one heading and every row filed under it, which is
better than git; C3, C4, C5 and C16 resolve without the driver making any decision at all, which is
where the file-wide dedup destroyed content and the splice misfiled it; and C15's permanent
conservatism becomes an auto-resolve, because rule 3 keys on the row SHAPE and not on the grammar.

**What this does not fix.** Structure disputed on both sides in the same region still conflicts, and
it should: two nodes renaming the same heading differently, or one node deleting a section another
is filling, is a decision no merge driver should make. The fixtures must include at least one such
shape so the refusal is exercised rather than assumed.

These measurements were taken on fixtures RECONSTRUCTED from the corpus's prose descriptions, not on
the corpus's own blobs, which were not available to this pass. The builder must re-measure every row
of the table against the reproduction the reports carry before treating any of it as settled; a row
that disagrees falsifies the design, and the spec is amended rather than the arm.

### Carve-out 3 — deletes and cross-section moves

| shape | what git does | what the redesign does | why |
|---|---|---|---|
| a row deleted on one side, untouched on the other | refuses when the deletion abuts a change | honours the delete, rc 0 | the row plane's `%O` = `%A` branch; the auto-resolve survives |
| a row deleted on one side, EDITED on the other | refuses | conflict block on that key, rc 1 | neither the edit nor the delete is the driver's to discard |
| a row deleted on one side, with new content filed ADJACENT to it on the other | refuses, rc 1 | honours the delete AND keeps the adjacent row, rc 0 | measured: the skeleton region is ours-side empty, theirs-side two tokens — token-only, so rule 3 applies and rule 2 drops the deleted key |
| a shared row MOVED across a section boundary by one side, the other side untouched | **rc 0, honours the move — NOT a refusal; see below** | honours the move, rc 0 | the untouched side's skeleton equals base's, so `text_merge` takes theirs wholesale |
| a shared row moved by one side, the other side editing a DIFFERENT keyed row | refuses, rc 1 | honours the move AND the edit, rc 0 | measured 2026-08-10: raw `git merge-file` rc 1; the skeleton is base-identical because a keyed row tokenizes to its id, so `text_merge` takes theirs with zero regions — the C14 mechanism |
| a shared row moved by one side with a new row filed behind it on the other | refuses, rc 1 | refuses, rc 1, naming the key | measured: the moved key's token appears TWICE in the merged skeleton, so conservation refuses |

**The C8 control was carried from the corpus and is wrong for the fixture as written.** Re-measured
on 2026-08-10: with ours leaving the file alone, `%O` and `%A` are byte-identical, so `git
merge-file` cannot conflict — it returns theirs at rc 0 with the move correctly honoured. Row 4 above
therefore MATCHES git rather than beating it, and its own rationale ("the untouched side's skeleton
equals base's") applies verbatim to the raw blobs, which is the contradiction. The BETTER claim does
hold for the variant now stated as row 5. The rev-1 log claimed every existing-code claim was
re-verified at HEAD; this cell was not, and §6's mapping table repeats the same wrong `rc 1`.
**F9 decides whether C8 is restated to the row-5 variant or reclassified SAME; the builder must not
absorb the disagreement silently** — §4 Carve-out 2's rule is that a row that disagrees falsifies the
design and the SPEC is amended, not the arm.

One or two auto-resolves are gained here, depending on F9 — the adjacent-delete case always, and the
cross-section move only in its row-5 form; both are cases the current driver gets wrong (C9's
regression and C8's silent discard). One refusal is retained, and unlike today's it is attributable:
the failure names the key that would have been written twice instead of naming a heading mismatch.

The delete-adjacent case is the one place the redesign resolves where git refuses, on the strength
of rule 3 plus the ratified delete rule. Its fixture must therefore assert the exact bytes on both
halves — the incoming row present AND the deleted row absent — not merely an exit code. This is a
DELIBERATE change to fixture group 13, which asserts rc 1 today; the new expectation is rc 0 with
both halves proven.

### Ambiguous lines

The class of a line is decided by one regex on that line alone, with no parser state, because state
is where all three rounds of defects lived.

| line | class | consequence |
|---|---|---|
| `*(none yet)*` | STRUCTURE — no whitespace after the `*` | merged by git; measured at `memory/DECISIONS.md:12` and `:92`, the only two such lines in the governed corpus |
| `---` or `***` | STRUCTURE — same reason | merged by git |
| a nested `  - sub-bullet` | ROW | tokenized; keys if it carries an id and a separator, otherwise hashed |
| a `- ` bullet inside a fenced code block | ROW | tokenized. Measured: zero fenced blocks exist in `memory/DECISIONS.md` and all four backlog shards today |
| a row-shaped line carrying an id and no separator | ROW, hashed | rule 3 still auto-resolves an append collision on it; the id postcondition still refuses a re-worded duplicate |

Fences are deliberately not parsed. The cost is bounded and conservative: two identical bullet-shaped
lines inside two code fences can trip the duplicate cap and produce a refusal. A refusal is an
acceptable outcome; a fence-tracking state machine on the merge path of an append-only record is not.

### The postconditions

Kept, unchanged in intent, all running over `settled(merged)` on EVERY verdict:

- `no_new_duplicates` line half — no row-shaped line written more often than the most any one input
  carried it. This is what refuses C10, the one shape where `git merge-file` itself corrupts.
- `no_new_duplicates` id half — no id leading more rows than in any one input. This is what refuses
  a re-worded duplicate of an unkeyable row, and the redesign makes it more load-bearing, not less.
- `no_misfiled_rows` — no keyed row under a heading no input filed it under. Rule 3 makes misfiling
  structurally unreachable, so this becomes a backstop; it stays because it is the one postcondition
  that has already caught real damage, and it costs a single pass.

New:

- `no_row_loss` — a CONSERVATION check, not a uniqueness check. For every key, the number of that
  key's row lines in `settled(merged)` equals `len(resolved[key])`; for every key resolved to
  nothing, it is zero; no row in the output belongs to a key `resolved` does not carry. Keys resolved
  to a conflict block, and keys inside a rule-4 region, are excluded, because `settled()` excises
  their lines by design. This is the check that closes the audit-line defect at its root: loss and
  duplication become refusals rather than numbers a reader has to reconcile.
  **The uniqueness wording is banned.** "That row appears exactly once" is false for a file carrying
  a legitimately repeated row line, and stating it that way turns an IDENTITY merge into a permanent
  whole-file conflict — measured, §4 The row plane, Multiplicity (a).
- `structure_identity` — the output's non-row, **non-marker** lines equal the merged skeleton's
  non-token, **non-marker** lines, in order, byte for byte. Cheap, total, and it is the assertion
  that says out loud that structure correctness is a property of CONSTRUCTION rather than of a
  heuristic. **Markers are excluded on BOTH sides and that word is load-bearing.** The skeleton
  carries git's `<<<<<<< ours`, `=======` and `>>>>>>> theirs` as non-token lines; excluding them on
  the output side only makes the two lists unequal by construction on every conflicted merge, and
  `main()`'s fail-closed handler then converts a scoped conflict into a whole-file one. Measured
  2026-08-10 on a rule-4 heading rename: skeleton non-token lines are `['# t', '', '<<<<<<< ours',
  '## TOOL — ours rename', '=======', '## TOOL — theirs rename', '>>>>>>> theirs']` against output
  non-row non-marker `['# t', '', '## TOOL — ours rename', '## TOOL — theirs rename']`. It also fires
  on rule-3 AUTO-RESOLVES, where the skeleton carries markers the output does not — so the asymmetric
  form breaks AC5, the C1/C2 headline this unit exists for, and falsifies §3's "ordinary conflicts
  become naturally scoped". The symmetric form passes both.

**Where the postconditions are evaluated.** Over the WRITTEN BYTES — the output re-read after write,
or equivalently `"".join(out).splitlines(keepends=True)` — never over the in-memory emit list. Both
new postconditions are about what the worktree receives, and a terminator defect is invisible in a
list where two glued records are still two elements: the Site 7 corruption above passed a
list-level `no_row_loss` AND a list-level `structure_identity` in the 2026-08-10 prototype. Site 7
is what makes the byte-level reading safe to state; without it, evaluating over bytes converts an
ordinary missing trailing newline into a whole-file refusal on the commonest collision shape.

### The audit line

One line on stderr, every number derived from the written bytes and the three inputs after the fact,
never from a counter incremented at an emit site:

```
merge-rows: rows O/A/B <o>/<a>/<b> -> <w> written (<k> keyed, <h> hashed), <d> deletes honoured,
<x> row conflicts, <s> structure conflicts, <verdict>
```

`k` and `h` are what make an inert grammar visible during a real merge: on the governed indexes `h`
should be 0 today, and a FAMILIES drift turns every row into a hashed one without changing any other
number. The line is printed only after the postconditions have run, so a run that is about to refuse
never first announces a clean result.

### Migration

Deleted outright from `tools/memory-tree/merge-rows.py`, with the reason each is retired:

| symbol | today | why it goes |
|---|---|---|
| `split_regions` (`:220-225`) | the preamble/row-block/trailer model | the whole file is one skeleton; the block-boundary rule was the source of the append-past-the-block misfile |
| `rows` (`:228-260`) | lead-in attachment to the following anchor | furniture is on the other plane and attaches to nothing |
| `lead` (`:538-583`) | two dedup regimes and a blank exemption | replaced by positional delegation; the exemption at `:578-579` is the live C4 loss and the adjacency scope at `:580-582` is the live C2 doubling |
| the splice (`:515-526`) | `%B`-only key placement with the `%A`-only skip | placement now comes from git's own diff |
| `kept` / `took_b` / `dropped` (`:535`) | counters at emit sites | replaced by after-the-fact derivation |

Kept, and the redesign must not disturb them: `_anchor_root` (`:154-170`), `_kit_dir` (`:173-186`),
`anchors` (`:189-211`) with its deferred import, `key` (`:214-217`), `settled` (`:305-327`), `census`
(`:330-345`), `row_ids` (`:348-357`), `_over` (`:360-372`), `sections` (`:411-427`),
`no_misfiled_rows` (`:430-456`), `read` (`:686-690`) and `main` (`:693-725`) with its fail-closed
handler and `write_bytes`. `_ROW_RE` (`:276`), `_ID_RE` (`:295`), `_HEADING_RE` (`:302`) and the
marker constants (`:301`) are unchanged.

Kept but AMENDED, and it is the only one: `text_merge` (`:459-486`) stays the single `git merge-file`
call site and keeps its signature, but its contract gains a conflict-style obligation — the region
shape it returns must not depend on the invoking node's `merge.conflictStyle`. See §4 The
conflict-style hazard and §8 F8. rev-1 listed it as undisturbed and §10 still reuses it "unchanged";
both are corrected here.

No data migrates. The governed files are not rewritten by this unit.

### Newline contract

The existing four sites stay: `read`'s `newline=""` at `:689`, `text_merge`'s `newline=""` write at
`:474`, its byte capture and manual decode at `:486`, and `main`'s `write_bytes` at `:718` and
`:724`. Three are added.

- **Site 5, tokenization.** A token line carries the terminator of the row it replaces. Without it
  the skeleton is a mixed-terminator file and `git merge-file` picks its marker terminator from the
  wrong neighbourhood.
- **Site 6, synthesized markers.** Every marker line the DRIVER writes carries the file's dominant
  terminator, computed over `%A`'s lines, defaulting to LF when `%A` is empty or tied. Three
  synthesis sites: the row plane's conflict blocks, rule 4's re-emission, and `main`'s fail-closed
  body at `:716-717`.
- **Site 7, substitution (rules 2 and 3).** A row line written in place of a token carries the
  terminator of the TOKEN it replaces in the merged skeleton, not the terminator it carried in its
  source blob. Only the line that ends the OUTPUT may carry an empty terminator. Without this, a row
  that was the unterminated final line of its own side keeps the empty terminator after the merge
  moves it — rule 3 emits ours' tokens before theirs', rule 2 relocates a formerly-final row — and
  `"".join(out)` fuses two records into one line at rc 0 with no markers, on a clean verdict, where
  the `git merge-file` control refuses at rc 1. Measured 2026-08-10; the corruption is present at
  HEAD and the rev-1 wording re-specified it rather than closing it. Carrying the token's terminator
  instead yields the correct two lines.

This closes C22 exactly, and the measurement narrows it usefully: `git merge-file` was measured on
2026-08-10 writing its own markers with CRLF into an all-CRLF file, so the LF markers the corpus
observed are entirely the driver's own synthesis and not git's. Rule 4's markers therefore need no
correction; only the driver's do.

### Rollout

One unit, landing as few commits as the couplings allow.

| step | work | stages a WATCHED path? |
|---|---|---|
| 1 | the engine rewrite (S1-S6) plus the rebuilt suite (S7, S8) in one commit — a suite that cannot see the engine it ships with is what this whole build is about | no |
| 2 | `check-wiring.sh` re-verification (S9) | no |
| 3 | the kit version bump and `check-verdict-epoch.sh`'s `DELEGATES`, plus doc and dossier truth (S10) | **yes** — `tools/memory-tree/check-memory-hygiene.sh` |

Step 3 stages a kickoff-manifest pathspec (`.claude/SESSION-KICKOFF.md:6`), so that commit carries
its own `last-audit` re-stamp; `manifest-check.sh --staged` accepts only a re-stamp bundled in the
same commit.

**The new inertness channel, and why S9 is not a formality.** Today a `.memory-tree.conf` FAMILIES
drift makes the driver key zero rows, every governed collision conflicts forever, and that is loud.
Under the redesign a drift makes every row a `raw:` token and rule 3 still auto-resolves the append
collision — so the failure stops being loud and becomes a quiet loss of the id postcondition's
reach. The wiring arm's FAMILIES check at `check-wiring.sh:357-371` therefore becomes MORE
load-bearing than it is now. The smoke at `:332-346` writes `- <FAMILY>-001 | base` rows, which do
anchor (the flat era plus the `|` separator), so it is not vacuous — but it must gain an assertion
on the audit line's keyed count, because the shape it exercises now passes with a dead grammar.

**And the FAMILIES-drift scenario cannot exercise that assertion.** Measured at HEAD on 2026-08-10 in
a throwaway clone: with `merge.rows.driver` set, `bash tools/check-wiring.sh --check` prints
`ok merge — merge.rows.driver wired`; after drifting `.memory-tree.conf` FAMILIES by one token it
prints `UNWIRED merge — … .memory-tree.conf FAMILIES does not declare TOOL …`. That is the
pre-existing undeclared-prefix HARVEST arm at `:357-371`, and control only reaches it because the
smoke PASSED. It passes because `fams` is derived from the same drifted conf (`:320-321`), so the
fixture writes `- TOOLS-001 | base` and `grammar_for` keys it normally — 100% keyed under exactly the
drift the scenario applies. A builder satisfies the scenario literally, observes UNWIRED, and ships
the keyed-count assertion with nothing proving it can fire: "an arm no fixture can reach is a
comment", which is the standard AC14 already invokes. The channel is real — with `key()` returning
None on the smoke's own 4-family/12-row fixture the prototype auto-resolved at rc 0 with all 12 rows
present exactly once, where `git merge-file` on the same three blobs returns rc 1 — so the guard
needs its own arm, and AC16 is split into AC16a and AC16b for that reason.

### Files touched (estimate)

`tools/memory-tree/merge-rows.py` (rewritten algorithm, retained scaffolding),
`tools/memory-tree/merge-rows.test.sh` (rebuilt), `tools/check-wiring.sh` (`:332-346` smoke
assertion), `tools/memory-tree/check-verdict-epoch.sh:60` (`DELEGATES`),
`tools/memory-tree/check-memory-hygiene.sh:13`, `tools/memory-tree/HYGIENE.template.md:1` **and
`memory/HYGIENE.md:1`** (the kit version TRIPLE — three literals, see §7 coupling 1),
`.claude/SESSION-KICKOFF.md:5` (re-stamp),
`memory/map/features/memory-tree-merge-driver.md` (Constraints, Shared seams, Reuse affordance,
Gaps), `memory/map/generated/*` (re-render), `tools/memory-tree/README.md:27-28`, `AGENTS.md:76`,
`memory/backlog/TOOL.md:21`, `memory/DECISIONS.md` (one appended row).

**Not touched:** `.gitattributes`, `tools/memory-recall/extract.py`, `tools/gate-legs.json` (the leg
name and argv are unchanged), `tools/lib/pyrun.sh`, `tools/memory-tree/adopt-memory-tree.sh`.

### Alternatives rejected

**A new module beside `merge-rows.py`.** Rejected. `merge.rows.driver` is a per-node repo-local git
config carrying a literal script path, set on three nodes here and on whatever an adopter ran; a new
path means a node that has not re-run `bash tools/check-wiring.sh --fix` keeps executing the old
engine with no signal, which is the class of failure C18 already books as the worst in the corpus.
The path is also hand-kept in six places — `check-wiring.sh:265`, `tools/gate-legs.json`,
`AGENTS.md:76`, `tools/memory-tree/README.md:27-28` and `:105-107`, and the dossier's `[paths]`
globs. One driver, one path, one config string.

**A helper module imported by the driver.** Rejected for the same reason at a smaller scale: the
driver must resolve with the fewest possible dependencies, and `adopt-memory-tree.sh` does not
install the driver at all today, so a second file is a second thing an adopter's install would have
to learn about.

**Degrading to hashed rows when the anchor grammar cannot be read.** Rejected. It is tempting
because the degraded pipeline still beats `git merge-file`, and that is exactly the trap: the file
would then merge under a different rule than the one configured, silently, on the path where the
kit is already broken. `anchors()` keeps its deferred import and any failure keeps landing in
`main()`'s fail-closed handler as markers.

**A sixth `memory/project/*.txt` registry for the conservative-case tally.** Rejected.
`check-memory-hygiene.sh:238-239` enumerates exactly the five registry names, so a sixth file reds
check 3 and drags a hygiene edit, a kit bump and a `--render` into a driver change. The tally lives
as a constant in `merge-rows.test.sh` beside the list of which cases are conservative and why.

**Restoring `census()`'s pre-round-3 breadth over headings**, which is the fix direction the third
review named. Rejected as the primary mechanism, though it would close C2: it re-opens C3 and C4,
where a legitimately repeated structure line must be allowed twice. The two questions — is this
record duplicated, is this heading duplicated — have opposite correct answers, and collapsing them
onto one predicate in either direction is what produced the C2/C3 oscillation. The redesign answers
the heading question by never deciding it.

## 5. Production-readiness checklist

- security — N/A. The driver reads three local blobs and writes one, and spawns only
  `git merge-file`; no network, no auth, no untrusted input beyond the repo's own files.
- perf / scale — one extra `git merge-file` subprocess per conflicted file relative to today, over a
  ~92-line index. Not measurable against a merge.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings beyond the stderr audit line.
- error / empty / loading states — an empty `%O`, a file with no rows at all, a file that is entirely
  rows, an unterminated final line, and an unreadable anchor grammar are each a named case in §6.
  rev-1 asserted that and was half true: the unterminated final line was reachable only through
  C13's line-form row, which asserts the HASH property and not the terminator one, and no AC named
  the shape. AC24 names it now, with its `git merge-file` control recorded. A file that carries the
  same row-shaped line twice was not a named case at all and is AC21.
- observability — the rebuilt audit line (S5) plus the keyed/hashed split; the reconciliation numbers
  are derived from the written bytes so the line cannot claim a state the file does not hold.
- risks — **this sits on the merge path of an append-only record of record, and its failure mode is
  silent.** Every recorded corruption in this corpus was rc 0 with no markers, and two of them were
  auto-committed by a real `git merge` before anyone looked. A green bar has failed to catch this
  twice: `merge-rows.test.sh` reported `PASS — 28 fixture groups held` and `tools/run-gates.sh`
  reported `38/38` on a tree that doubled a heading in `memory/DECISIONS.md` at rc 0. The mitigation
  is not more fixtures of the same kind; it is that the never-worse comparison against
  `git merge-file` becomes a per-case control (S7) rather than a property two of twenty-eight groups
  happen to check, and that loss and duplication become refusals (S3) rather than numbers.
  Secondary risk: the redesign resolves where git refuses (the adjacent-delete, and the cross-section
  move in its row-5 form), so those fixtures must assert exact bytes and not exit codes.
  Rollback is `git revert`; no external state, and the governed files are not rewritten.
  **Third risk, and it is the one this rev exists for: a spec-faithful prototype of rev-1 shipped
  three NEW rc-0 corruptions that HEAD does not have** — the within-side dedup in rule 3, the
  terminator that survives substitution, and the singular row plane. All three were found by building
  rev-1 as written and measuring it against a live `git merge-file` control on the same blobs, which
  is exactly what S7 makes the suite do. Two of them are invisible to every postcondition rev-1
  declared. The lesson is booked, not merely noted: a rule stated as set-shaped ("each distinct key
  once", "appears exactly once") re-imports the file-wide-uniqueness assumption whose deletion is
  this unit's premise, and the reviewer must read every such phrase as a defect until it is restated
  as a count.
- testing + left-shift gates — the existing leg keeps its name and argv; every case gains a live
  control; the conservative tally becomes a shrink-only constant.
- migration / rollback — none. No file format changes and no adopter data moves. A node that never
  re-runs `check-wiring.sh` keeps the same config string and picks up the new engine on its next
  pull, which is the intended behaviour of a same-path rewrite.
- user docs — `tools/memory-tree/README.md:27-28` describes the retired mechanism (regions, lead-ins,
  the splice) and must be re-written to the two planes; `AGENTS.md:76` likewise. The wiring section
  at `README.md:82-107` is unchanged.

## 6. Acceptance criteria

- **AC1** When `bash tools/memory-tree/merge-rows.test.sh` is run, it passes, and every case in it
  runs `git merge-file -p -L ours -L base -L theirs` on the identical three blobs and records that
  control's exit code and output alongside the driver's.
- **AC2** When any case's driver output LOSES a line that the control's output carries while the
  control exits 0, or writes a row-shaped line more often than the control does while the control
  exits 0, or files a keyed row under a heading no input filed it under, the suite FAILS and names
  the case, the class and both outputs.
- **AC3** When a case's control exits 0 with a correct result and the driver exits 1, the case is
  counted in the suite's conservative tally, printed by name, and asserted at or below a constant
  declared in `merge-rows.test.sh` beside the reason for each member. The tally is shrink-only: a
  redesign that trades one fix for one new conflict is visible rather than absorbed.
- **AC4** When the mapping table below is walked, every corpus case C1 through C22 has a case in the
  suite whose expected outcome is the one stated, and the suite fails if any is absent.
- **AC5** When two nodes each open the same currently-empty section — one row on one side and three
  lines including an unkeyable row on the other — the driver exits 0, the section heading appears
  exactly once, every row appears exactly once and under that heading, and no conflict marker is
  written. This is C1 and C2 in one arm.
- **AC6** When ours appends a note line, two rows, the same note line again and a third row at the
  end of a section while theirs edits only preamble prose, the driver exits 0 and BOTH copies of the
  note survive, matching the control byte for byte.
- **AC7** When ours deletes a row and theirs files a different row immediately above it, the driver
  exits 0, the incoming row is present, and the deleted row is absent. Both halves are asserted; an
  exit code alone does not satisfy this.
- **AC8** When theirs moves a shared row to another section and ours edits a DIFFERENT keyed row's
  text, the driver exits 0, the row appears exactly once in theirs' section, and ours' edit survives.
  The arm records the live control, which is rc 1. The ours-untouched variant is ALSO run, and its
  control is recorded as rc 0 — it matches git rather than beating it, and the arm must not claim
  otherwise (§4 Carve-out 3, F9).
- **AC9** When ours moves a shared row across a heading and theirs files a new row behind it, the
  driver exits 1 and the refusal names the key that would have been written twice.
- **AC10** When the same unkeyable row is minted on both nodes in different regions, the driver exits
  1 with a duplicate refusal, and the arm records that the control exits 0 having written the row
  twice — the one shape where the driver must beat git.
- **AC11** When two nodes each append a DIFFERENT row carrying an id and no anchor separator at the
  same insertion point, the driver exits 0 with both rows present exactly once.
- **AC12** When a structure line is edited differently on both sides in the same region, the driver
  exits 1, both versions are written between one marker pair, and no row is lost.
- **AC13** When any fixture is run on a CRLF worktree file and the driver exits 1, every line of the
  written file ends in CRLF, including every marker line. The existing group asserts this on clean
  merges only.
- **AC14** When `no_row_loss` is deliberately disabled and the suite is re-run, at least one case
  reds; likewise for `structure_identity`, the line half of `no_new_duplicates`, the id half, and
  `no_misfiled_rows`. Five sabotage arms, one per postcondition, because a postcondition no fixture
  can reach is a comment.
- **AC15** When the audit line is compared against the written file for every case at BOTH exit codes,
  every number reconciles: the written row count equals the count of row-shaped lines outside
  conflict regions, the keyed count plus the hashed count equals it, and the deletes-honoured count
  equals the number of keys resolved to nothing. Group 8's helper asserts this today at exit 0 only.
- **AC16a** When `.memory-tree.conf`'s FAMILIES is drifted by one token and `bash
  tools/check-wiring.sh --check` is run, it reports UNWIRED. This is a REGRESSION guard on the
  existing undeclared-prefix harvest arm (`check-wiring.sh:357-371`), and it passes at HEAD; it does
  not and cannot exercise the keyed-count assertion, because the smoke fixture is built FROM the
  drifted conf and its rows key normally (§4 Rollout).
- **AC16b** When the smoke is run against a grammar under which its own rows do NOT key — a fixture
  conf whose families do not match the smoke rows, or an equivalent that leaves the import intact —
  `check-wiring.sh --check` reports UNWIRED, and the reason it gives is that the driver's audit line
  reports a non-zero HASHED count for the smoke rows. This is the arm that proves the guard against
  the inertness channel §4 Rollout names; AC16a alone does not.
- **AC17** When `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py` is invoked with the
  memory-recall kit moved aside, the driver exits 1 and writes `%A` containing both sides between
  markers, never a truncated take-ours. The C18 property is unchanged by this unit and must be
  re-proven, not assumed.
- **AC18** When an identity merge of the real `memory/DECISIONS.md` and each `memory/backlog/*.md`
  against itself is run, the output is byte-identical to the input, and a file with no row-shaped
  lines at all round-trips unchanged. The population additionally includes the AUTHORED file of
  AC21: measured at HEAD the four governed files carry zero duplicate row lines and zero nested
  rows, so on their own they satisfy this by accident and prove nothing about multiplicity.
- **AC19** When `bash tools/run-gates.sh` is run at the end of each of the three rollout steps, it is
  green, and `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` has been run BEFORE the
  review rather than after.
- **AC20** When `memory/map/features/memory-tree-merge-driver.md` is read after step 3, its
  Constraints section describes the two planes rather than the three regions, its Reuse affordance no
  longer offers `merge-rows.split_regions` as a seam, and
  `python tools/codebase-map/test_codebase_map.py` exits 0 against freshly rendered artifacts.
- **AC21** When a file carrying the SAME row-shaped line twice — an authored fixture with two
  identical `  - notes` sub-bullets under two different keyed rows, since no governed file has one —
  is merged against itself (`%O` = `%A` = `%B`), the driver exits 0 and the output is byte-identical
  to the input; and when both sides append a different row to that same file, the driver exits 0,
  both appended rows are present, and BOTH copies of the repeated line survive. Any refusal on either
  arm fails the AC: an identity merge that conflicts is a permanent whole-file conflict the author
  cannot clear.
- **AC22** When ours appends a repeated note line, a keyed row and that same note line again at the
  point theirs appends one row, the driver exits 0 and BOTH copies of ours' note are present. The arm
  records the control (`git merge-file` refuses, rc 1) and asserts exact bytes, not an exit code.
  This is the within-side dedup regression; the driver at HEAD is CORRECT on this shape, so the arm
  is a never-regress bar and not an improvement claim.
- **AC23** When the C1 fixture is run in a scratch repo with `git config merge.conflictStyle diff3`
  set — and again with `zdiff3` — the driver exits 0, the heading appears once and both rows are
  filed under it, byte-identical to the default-config run. No fixture may rely on the ambient
  config being unset.
- **AC24** When one side's copy of a row is the file's final line with NO terminator and the merge
  relocates it away from end of file, the driver's output carries the two records on two lines. Both
  the rule-3 path (both sides append, ours' side unterminated) and the rule-2 path (a formerly-final
  row substituted mid-file) are arms, each recording its control; `git merge-file` refuses at rc 1 on
  the rule-3 shape. Exact bytes, and the assertion is made over the file ON DISK.
- **AC25** When a token whose row-plane verdict is a conflict block falls inside a rule-4 region —
  reachable through the delete/modify branch: ours edits a row and appends another, theirs deletes
  that row and renames its heading — the written region contains exactly one marker pair, no nested
  markers, and `settled()` over the output returns only the settled lines. The arm asserts the
  `settled()` view directly, because that view is what all four postconditions read.

### The corpus mapping — this table IS the acceptance suite

`control` records whether a live `git merge-file` control exists TODAY. Every row must have one after
this unit. `git` is the control's behaviour on the identical three blobs as recorded or measured.

| case | git | required outcome after the redesign | group today | control today |
|---|---|---|---|---|
| C1 doubled heading, simple | rc 1 | rc 0, heading once, both rows filed — BETTER than git | 10 | no |
| C2 doubled heading, middle row | rc 1 | rc 0, heading once, all four rows filed — BETTER | **none** | no |
| C3 repeated `### ` in two sections | rc 0 correct | rc 0, byte-equal to the control | 17 | yes |
| C4 repeated note lead-in | rc 0 correct | rc 0, both copies, byte-equal to the control | **none** | no |
| C5 misfile, append past block | rc 0 correct | rc 0, byte-equal to the control | 11 | no |
| C6 ours under theirs' new heading | rc 0 correct | rc 0, byte-equal to the control | 14 | yes |
| C7 misfile behind a moved neighbour | rc 1 | rc 1, refusal names the doubled key — SAME as git | 15 | no |
| C8 cross-section move discarded | **rc 0** as the corpus fixture is written (ours untouched ⇒ `%O` = `%A`); rc 1 on the keyed-edit variant | rc 0, move honoured, row once — BETTER only on the keyed-edit variant; SAME as git on the corpus fixture. **F9** | **none** | no |
| C9 delete eats adjacent content | rc 1 | rc 0, delete honoured AND adjacent row kept — BETTER | 13 | no |
| C10 same unkeyable row, two regions | rc 0, DUPLICATES | rc 1, duplicate refusal — BETTER, the case that justifies the unit | 12 | no |
| C11 same id, different wording | unmeasured | rc 1; **the control must be measured and recorded** | 16 | no |
| C12 duplicate beside an unrelated conflict | unmeasured | rc 1, duplicate refusal reached on a non-clean verdict; **measure the control** | 18 | no |
| C13 duplicate smuggled by line form | n/a | rc 1; the token hashes the STRIPPED text, so line form cannot smuggle | 20 | no |
| C14 heading rename vs row edit | rc 1 | rc 0, both survive — BETTER | 19 | no |
| C15 inert on separator-less rows | rc 1 | rc 0, both rows present — BETTER; the conservatism is fixed | **none** | no |
| C16 two different empty sections | rc 0 correct | rc 0, byte-equal to the control | **none** | no |
| C17 whole-file refusal ergonomics | rc 0 correct | a rule-4 conflict is a scoped hunk from git's own merge; only a postcondition refusal stays whole-file, and each such case is a counted member of the AC3 tally | partial | no |
| C18 driver cannot start, silent take-ours | n/a | unchanged and re-proven: every start failure becomes markers | 0a/0b/0c | n/a |
| C19 vacuous wiring smoke | n/a | the smoke asserts the keyed count, not only presence; re-verified end to end | **none** | n/a |
| C20 attribute ungated | n/a | unchanged; `git check-attr merge` still reports `rows` on both pathspecs | 9 | n/a |
| C21 audit line does not reconcile | n/a | AC15 at both exit codes, plus `no_row_loss` making loss a refusal | **none** (rc 0 only) | n/a |
| C22 LF markers into a CRLF file | n/a | AC13; every synthesized marker carries the dominant terminator | **none** (clean only) | n/a |

Eight cases have no fixture group today — C2, C4, C8, C15, C16, C19, C21, C22 — and each must gain
one. Two of twenty-eight groups run a live control today (14 and 17); after this unit every case
does, because the control is the bar.

**The table is necessary and not sufficient, and rev-2 is the proof.** AC21 through AC25 correspond
to NO corpus case. They are failure classes the REDESIGN introduces — three of them regressions
against HEAD, all five found by building rev-1 as specified and measuring it against a live control —
so a suite that satisfies AC4 completely still ships them. The `git` column above is "as recorded or
measured"; C8's cell was recorded, not measured, and was wrong (F9). Every remaining cell whose
provenance is the corpus rather than this build must be re-measured before it is treated as a bar,
under §4 Carve-out 2's rule: a row that disagrees falsifies the design and the SPEC is amended.

## 7. Gates

The full bar `bash tools/run-gates.sh` stays green at each rollout step. The leg
`row-keyed merge driver replay` keeps its name and its argv
(`bash tools/memory-tree/merge-rows.test.sh`), so `tools/gate-legs.json` and
`tools/run-gates.test.sh`'s no-hardcoded-leg canary are unaffected.

Six couplings a builder will otherwise discover the hard way.

1. **The kit version is a THREE-place obligation, and the order matters.**
   `KIT_MEMORY_TREE_VERSION` is **1.9** at HEAD (`check-memory-hygiene.sh:13`);
   `tools/check-kit-versions.sh:30-32` requires the `<!-- gov:kit memory-tree@1.9 -->` marker in
   `tools/memory-tree/HYGIENE.template.md:1` to agree; and **`memory/HYGIENE.md:1` carries the same
   marker as a third live copy**. rev-1 named two of the three and that walks the builder into a gate
   loop: bump only those two and `kit/dogfood doc parity`
   (`tools/memory-tree/kit-dogfood-parity.test.sh`, a leg in `tools/gate-legs.json`) reds, and the
   remedy it prints — `--render` — runs `norm "$live" > "$ship"`, rewriting the SHIPPED template FROM
   the stale live copy, reverting it to 1.9 and redding `kit version markers` instead. **Edit the
   LIVE copy first, then re-render.** `check-verdict-epoch.sh:151-157` — the gate this unit extends
   in coupling 2 — already prints the instruction verbatim, and it is the text to follow:
   `Bump it in ALL THREE places, which must move together`, naming `$ENGINE`,
   `tools/memory-tree/HYGIENE.template.md (line 1)`, and
   `memory/HYGIENE.md (line 1) — then: bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.
2. **`check-verdict-epoch.sh` DELEGATES.** Measured at HEAD, `:59-60` sets `ENGINE` to
   `check-memory-hygiene.sh` and `DELEGATES` to `gen_build_index.py corpus_ids.py gotchas.py
   extract.py`. **`merge-rows.py` is not in that scan set**, so nothing today forces a kit bump when
   the driver's verdicts change — the same one-hop-short defect the file's own comment at `:55-58`
   records for the grammar. Add `tools/memory-tree/merge-rows.py` to `DELEGATES` in this unit, which
   then requires the bump in coupling 1 to land in the same commit as the engine rewrite or in a
   commit that descends from it; the gate's rule is topological, so one correctly placed bump per
   range is enough.
3. **The arms floor does NOT cover this file, and that is the finding.** `check-arms.py` discovers a
   gate as a tracked `*.sh` that defines `fail() {`, so a Python driver is structurally outside its
   population and `ARMS_FLOORS` in `.memory-tree.conf:62` names only `manifest-check.sh` and
   `check-memory-hygiene.sh`. The redesign moves neither floor. It also means the meta-gate that
   would have caught the two unarmed branches the third review found cannot see them, which is why
   AC14 hand-writes the five sabotage arms. `memory/project/unarmed-branches.txt` is empty and
   SHRINK-ONLY: this unit must not add a row to it.
4. **`.gitattributes` wiring is an OWNER decision and the builder must NOT make it.** Do not add,
   remove or edit a `merge=rows` line, and do not change `merge.rows.driver` on any node beyond what
   `check-wiring.sh --fix` already does. Whether a repo with 13 merges and zero index collisions
   should run this on its merge path is not a question a build commit answers.
5. **The kickoff manifest and the codebase map.** The rollout's step 3 stages
   `tools/memory-tree/check-memory-hygiene.sh`, one of the seven watched pathspecs at
   `.claude/SESSION-KICKOFF.md:6`, so that commit carries its own `last-audit` re-stamp. Deleting
   `split_regions` invalidates the dossier's declared seam
   (`memory/map/features/memory-tree-merge-driver.md:142`) and changes `memory/map/generated/`, so
   the dossier edit and a fresh render land in the same commit or the coverage-and-freshness leg
   reds.
6. **The `drift-audit records` leg, which rev-1 omitted, and which TWO of this unit's own mandated
   edits can red.** Both pins in `tools/drift-audit/drift_signals.py:120-142` are shrink-only and
   both sit EXACTLY at their value at HEAD, so either one incrementing fails
   `python tools/drift-audit/drift_report.py --check`.
   (a) `non_terminal_specs_cited_by_product_source: 2` — this repo's kit source routinely stamps its
   originating spec id into the file header (`tools/push-main.sh:2`, `tools/run-gates.sh:24`,
   `tools/memory-tree/check-verdict-epoch.sh:57`). A rewritten `merge-rows.py` header citing
   `TOOL-aMendedLedger-8` while this spec is still SPECCED takes the signal to 3; verified by
   appending the id and re-running the check, which prints `OVER PIN 2 — gateable`. So: the new
   header must NOT cite a non-terminal spec id, or this spec must be terminal before step 1 lands.
   (b) `handkept_inventories_disagreeing_with_source: 7` — `_charter_mentions_every_leg` matches each
   leg's argv SCRIPT PATH inside `AGENTS.md`'s `## The gate suite` section, and `AGENTS.md:76` is the
   ONLY citation anywhere in that file of `tools/memory-tree/merge-rows.test.sh`. §5 mandates
   rewriting that bullet; dropping the literal path takes mentioned from 32 to 31 and the pin to 8,
   and the leg that falls out is `row-keyed merge driver replay` — this unit's own. So: the rewrite
   must keep the literal string `tools/memory-tree/merge-rows.test.sh` inside that section.
   With AC19 requiring a green bar at each of three rollout steps, either miss costs a cycle per step.
   Secondary: coupling 3 is right that a Python driver is outside `check-arms`' population, but S7
   rebuilds a SHELL file. The rebuilt `merge-rows.test.sh` currently defines no `fail() {`; if the
   rebuild adopts that idiom with `fail <n> "` call sites it JOINS that population and needs armed
   branches or a pin, and `memory/project/unarmed-branches.txt` is shrink-only and empty.

## 8. Open questions

- **F1 — rewrite in place, or a new module beside `merge-rows.py`?**
  **RESOLVED (build, 2026-08-10): rewrite `tools/memory-tree/merge-rows.py` in place, one file.**
  The wiring is path-keyed and per-node, so a new path leaves any node that has not re-run
  `check-wiring.sh --fix` executing the old engine silently — C18's class. The path is hand-kept in
  six places. Reasoning and the rejected variants are in §4 Alternatives rejected.
- **F2 — what happens to furniture consumed by a row?**
  **RESOLVED (build, 2026-08-10): it is STRUCTURE, attached to nothing, merged positionally by git,
  and the lead-in concept is deleted rather than re-tuned.** The expected cost — losing the
  empty-section auto-resolve, which git refuses — is bought back by reconciliation rule 3, measured
  on reconstructed C1 and C2 fixtures. §4 Carve-out 2 carries the measurement and the cases it does
  and does not fix.
- **F3 — may the driver resolve where `git merge-file` refuses?**
  **RESOLVED (build, 2026-08-10): yes, and only when every disputed line is a row token.** That
  single rule is what delivers C1, C2, C9 and C15, and its converse — any disputed structure line is
  a conflict — is what keeps the driver out of the class of decision it has been wrong about three
  times. Both fixtures that exercise it (the adjacent delete, the cross-section move) assert exact
  bytes rather than exit codes.
- **F4 — where does the conservative-case tally live?**
  **RESOLVED (build, 2026-08-10): a shrink-only constant in `merge-rows.test.sh`**, beside the named
  list of members and the reason each is conservative. A sixth `memory/project/*.txt` registry is
  rejected in §4 Alternatives rejected; `check-memory-hygiene.sh:238-239` enumerates exactly five.
- **F5 — does `merge-rows.py` join `check-verdict-epoch.sh`'s DELEGATES?**
  **RESOLVED (build, 2026-08-10): yes.** The constant DATES the kit's verdicts and the driver's
  verdicts are kit verdicts; leaving it out is the same one-hop-short shape `:55-58` already records
  for the grammar. The cost is one bump per range, and the gate's own doc argues the over-count is
  the safe direction.
- **F6 — does the redesign parse fenced code blocks before classifying a line?**
  **RESOLVED (build, 2026-08-10): no.** One stateless regex per line. Measured: zero fenced blocks
  exist in `memory/DECISIONS.md` or any backlog shard today, and the failure mode of getting it
  wrong is a conservative refusal, not corruption. A parser on the merge path of an append-only
  record buys a rare case and pays in exactly the state-machine complexity all three defect rounds
  lived inside.

Three forks opened by the rev-2 fold-in. **These are OPEN and the builder must not decide them
alone** — each one changes a bar the suite is written against, and each was reached by measurement
rather than by reading.

- **F7 — OPEN. Does a `row:` key ever carry multiplicity greater than 1?**
  §4 now makes the row plane key → LIST with `max(len(A[key]), len(B[key]))` on every content-keeping
  branch, which is unambiguously right for `raw:` keys — a repeated note is content and `_over()`
  already reasons that way. For `row:` keys it collides with a rule the unit already has: an id
  leading two rows is exactly what `no_new_duplicates`' id half exists to refuse (the C10/C11
  mechanism). Two answers. **(i)** Multiplicity is universal, a `row:` key can resolve to two lines,
  and the id postcondition is the thing that then refuses — one rule, one place, and the refusal is
  attributable. **(ii)** `row:` keys are pinned at multiplicity ≤ 1 in the row plane, so the id
  invariant is structural and the postcondition becomes a backstop. The choice changes what AC9/C7
  assert (a conservation refusal versus a duplicate refusal), what the audit line's row counts mean,
  and whether `no_row_loss` or `no_new_duplicates` is the arm that fires. Do not pick by
  implementation convenience.
- **F8 — OPEN. How is `merge.conflictStyle` neutralised?**
  §4 The conflict-style hazard establishes that it MUST be — a node-local `diff3`/`zdiff3` silently
  deletes rule 3 and every BETTER-than-git row with it. Two remedies. **(i)** Pin at the single call
  site: `git -c merge.conflictStyle=merge merge-file …`, one line, measured to override a configured
  `diff3`. It amends `text_merge`, which §4 Migration and §10 both declared untouched, and it
  overrides a config the adopter deliberately set. **(ii)** Define rules 3 and 4 over three sections
  and discard the base section, which keeps the adopter's config meaningful and costs a marker
  grammar the spec currently does not state. This is a copy-in kit and the config belongs to the
  adopter, not to this repo, which is why it is not the builder's call.
- **F9 — OPEN. What happens to C8 now its control is measured?**
  Re-measured 2026-08-10, the corpus fixture as written (`%O` = `%A`) gives `git merge-file` rc 0
  with the move honoured, so C8 is not BETTER than git. **(i)** Restate the fixture as the keyed-edit
  variant, which genuinely beats git by the C14 mechanism, and keep the BETTER classification.
  **(ii)** Keep the corpus fixture and reclassify C8 as SAME, which reduces carve-out 3's "two
  auto-resolves are gained" to one and removes a row from the headline table. §4 Carve-out 2 binds
  the builder to escalate rather than choose: a row that disagrees falsifies the design and the spec
  is amended, not the arm. Whether any OTHER `git` cell carried from the corpus is also wrong is part
  of this fork — the re-measurement pass is not optional.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft. Written against the three review reports in
  `memory/builds/aMendedLedger/reviews/` and the reproduction corpus they produced, with every claim
  about existing code re-verified at HEAD (`390a87e`) rather than carried from the reports: the
  driver is 74 of 74 rows keyed on `memory/DECISIONS.md` and 18 of 18 on
  `memory/backlog/TOOL.md` after `TOOL-aMendedLedger-7`, `KIT_MEMORY_TREE_VERSION` is 1.9 not 1.7,
  the blank-lead-in exemption is at `merge-rows.py:578-579` and not the `:551` the backlog row cites,
  and `check-verdict-epoch.sh:59-60` does not scan the driver at all. The design rests on a
  measurement taken in this pass rather than inferred: `git merge-file` was run on SKELETON forms of
  eight reconstructed corpus fixtures, and the conflict regions it produces for C1, C2 and C15 are
  token-only on both sides, which is what makes reconciliation rule 3 available and what buys back
  the auto-resolve that pure delegation would have cost. Two further measurements corrected received
  facts: `git merge-file` writes its own markers with CRLF into an all-CRLF file, so C22 is entirely
  the driver's own synthesis, and `git merge-file` returns rc 1 on the C14 shape, where the corpus
  recorded no control. All six §8 forks are resolved at build level; the `.gitattributes` wiring
  question is deliberately NOT a fork here — it is an owner decision recorded in §3 and guarded by
  §7 coupling 4.
- rev-2 · 2026-08-10 · folded the surviving findings of the spec review. Twelve findings survived
  verification out of twenty-eight filed; sixteen were refuted and are not folded. The method is
  worth recording: the review built a SPEC-FAITHFUL prototype of rev-1 and ran it against a live
  `git merge-file` control and against the driver at HEAD on identical blobs — the procedure S7
  makes the suite perform — and it found three rc-0 corruptions rev-1 would have shipped, all three
  invisible to the postconditions rev-1 declared, and all three REGRESSIONS against HEAD.
  **Blocking, folded into §4 and §6.** (1) Rule 3's "each distinct key emitted once" rebuilt the
  deleted file-wide-uniqueness assumption on the row plane and DELETED a legitimately repeated row
  from an append-only record at rc 0; the rule is now positional concatenation with dedup across
  sides only, and AC22 pins it. (2) The row plane was `key → line`, so a file carrying the same row
  line twice failed its own IDENTITY merge — a permanent whole-file conflict no author can clear;
  the plane is now `key → list` with max-over-inputs multiplicity, `no_row_loss` is restated from
  uniqueness to CONSERVATION, AC21 is new and AC18 is widened past the four governed files, which
  pass it only by accident. (3) The mandated empty terminator of an unterminated final line survived
  substitution and fused two records onto one line at rc 0 on both the rule-3 and rule-2 paths;
  newline Site 7 closes it, the postconditions are now stated to run over the WRITTEN BYTES, and
  AC24 exercises both paths. (4) `git merge-file` honours the repo's `merge.conflictStyle`, so a
  node with `diff3`/`zdiff3` gets a third `||||||| base` section that deletes rule 3 and every
  BETTER-than-git row with it; new §4 subsection, new S11, AC23, and F8 opened. (5) AC16's
  FAMILIES-drift scenario is answered by the pre-existing harvest arm and its fixture keys normally
  under the drift, so it could never exercise the keyed-count guard the new inertness channel needs;
  split into AC16a and AC16b. (6) The kit bump is a THREE-place obligation and rev-1 named two,
  walking the builder into a `--render` loop that reverts the template; §7 coupling 1 now quotes
  `check-verdict-epoch.sh:151-157` and §4 Files touched names `memory/HYGIENE.md:1`.
  **Non-blocking, folded.** (7) `structure_identity` excluded markers on one side only, which fires
  on every conflicted merge AND on rule-3 auto-resolves — stated symmetrically now, in §2 S4 and §4
  alike. (8) Rule 4 never said what a token inside a region becomes; per-side substitution is stated,
  with the delete/modify reachability the review demonstrated and AC25. (9) C8's control was carried
  from the corpus rather than measured; measured it is rc 0, so C8 as written is not BETTER than git
  — corrected in carve-out 3 and in the §6 table, with F9 opened. (10) §7 omitted the
  `drift-audit records` leg, which two of this unit's own mandated edits can red from pins sitting
  exactly at their values; added as coupling 6 with both mechanisms verified and the `fail() {`
  hazard in the rebuilt suite noted. Also corrected: §4 Migration and §10 listed `text_merge` as
  undisturbed, which F8 may change; §5 claimed the unterminated final line was already a named case
  in §6, which it was not. Three forks are OPEN for the first time in this unit — F7 multiplicity for
  `row:` keys, F8 the conflict-style remedy, F9 C8's classification — and the §6 note now says out
  loud that the corpus table is necessary and not sufficient, because five of the new arms map to no
  corpus case at all.

## 10. Reuse audit

`CODEBASE_MAP_ROOT="$(git rev-parse --show-toplevel)" python tools/codebase-map/reuse_lookup.py` over
"three-way merge index rows keyed by record id, conflict markers, tokenize lines and delegate to git
merge-file" returns a corpus of 259 symbols, 71 inventory keys, 3 affordance seams and 2 dossiers.
The top-ranked seams are this unit's own subject: `merge-rows.key` (fan-in 19, SEAM),
`merge-rows.rows` (fan-in 11, SEAM), and the declared affordance seams `merge-rows.split_regions` and
`pyrun.sh`. `settings-merge.merge` (fan-in 6) and `gotchas.records` (fan-in 7) surface and neither
fits, for the reason the master spec already recorded: one is a recursive dict union for JSON
settings, the other parses front matter.

So the reuse decision is: **no external seam fits, and the seams this unit wires through are its
own.** `anchors()`/`key()` keep importing the grammar from `tools/memory-recall/extract.py` rather
than vendoring it, `text_merge()` keeps being the single call site for `git merge-file` and is reused
for the skeleton merge with its signature intact but its CONTRACT amended — the region shape it
returns must not depend on the invoking node's `merge.conflictStyle` (§4 The conflict-style hazard,
§8 F8). rev-1 said "unchanged" here and that was wrong: reuse of a seam whose behaviour a per-node
git config can change is reuse of an ambiguity. `tools/lib/pyrun.sh` stays the launcher. The one seam this
unit RETIRES is `merge-rows.split_regions`, which the dossier at
`memory/map/features/memory-tree-merge-driver.md:142` currently offers to future callers as "reuse
for any three-way merge of a file that is prose-then-rows" — that offer is withdrawn in the same
commit, because the three-region model is the thing being replaced.

Two caveats, stated rather than hidden. The lookup reports `corpus: 0 symbols` and "no seam fits"
when run without `CODEBASE_MAP_ROOT`, which reads as a real answer and is not; that prefixed-install
defect is recorded at `.codebase-map.conf:12-17` and in `memory/map/features/codebase-map.md` §Gaps,
and is out of scope here. And the map's corpus is bash-recall-dark, so the shell gates this unit
couples to (`check-wiring.sh`, `check-verdict-epoch.sh`, `check-kit-versions.sh`) cannot appear in
that shortlist and were found by reading them.
