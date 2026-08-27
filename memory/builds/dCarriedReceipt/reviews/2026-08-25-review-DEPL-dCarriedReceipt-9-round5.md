# Pre-code review, round 5 — part 2 of 2, the receipt and reach units, DEPL-dCarriedReceipt-9..15

**Serves:** spec-audit DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15

**Reviewed:** all 15 specs plus the build README, against the round-4 fold at `8e98a381`.
**Base:** `8e98a381`. Source read at `9ddcc5c9`; `tools/govkit/govkit.py` is byte-identical between
the two, so every line citation holds at either sha.
**Harness:** five primed finder lenses over the fold diff (fold fidelity, fold collateral, citation
integrity, residual contradiction, acceptance observability), then batched default-refute skeptics,
then one synthesis. Eleven agents, all returned. Seventeen confirmed entries arrived; deduplicated
they are the 11 defects across both parts, and 21 were refuted.
**Scope:** this round audits the FOLD, not the design. Every finding is either a round-4 edit that
landed wrong, or collateral the fold created while landing a correct one.
**Why two parts:** the Serves id list renders into one build-README row and 15 ids blow its entry
cap. That is DEPL-dCarriedReceipt-16; rounds 1 and 4 split on the same boundary.

This record carries the convergence answer, the blocker, the fork ruling and the findings against
units 9-15. Units 1-8 are part 1, `2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md`.

## Verdict: BLOCKED

One blocker, B1, down from three. It lands edits in `-7` and in `-13`, and it is carried in
part 2 with the convergence answer.

## The convergence question, answered

**Still no — but the distance closed from four seams to one field set.**

Round 4's answer was that the 15 specs describe one build's *vocabulary* and one build's *order*, and not one **receipt**. `-13` specified `adopt` as a walk over `resolve_entry`'s two row channels and nothing else, so three things `cmd_apply` synthesizes outside that function had no writer at all: the one `role: "attributes"` row (`:2350`), the real `merged` row (`:2417`), and the `sha256` field (`:2459`). The fourth hat was the input rather than the output — `-9` defined the `relocate` rung's needle map as derived from the receipt, which is the artifact `adopt` is creating.

**All four of those are now answered, and the answers are good ones.** `-13` gained S4a, which derives `alpha` from the planned `(src, dest)` pairs and delegates the ambiguity drop and the report line to `-9` S3 rather than restating them. It gained S11, which names both synthesized row classes and points at the source literal that owns each shape instead of re-typing its keys — the form this build prefers everywhere else. `-9` §8 F3 and §10 now name `adopt` as the derivation's second caller with its own input. `-14`'s rollback snapshot moved from four fields to six in `-14` S3, `-14` §4's Data model and `-14` AC4 independently, so an under-glossed appositive cannot subtract one. `sha256` is back in `-13` S5 and §4, with F5 recording whose bytes it hashes.

**What did not converge is the merged row's field set, and it is the row class this same fold put on the record.** `-13` S11 says `adopt` writes each merged row "in `apply`'s shape (`:2417`)", and the fold names `:2417` four separate times across `-7` S9 and `-13` S7/S11. In the same pass, M4 narrowed `-7` S1 from an unqualified quantifier to a two-channel enumeration — the `writes` channel at `:2443-2460` and the `unlanded` channel at `:2440` — and `:2417` is neither channel. So the build now states precisely where the merged row is written and no longer states which identities it carries.

That silence is not neutral. `-7` S9's preamble refuses any row carrying exactly one of `commit`/`gov_oid`, over the whole receipt, before any row is classified. Verified in source: `:2417-2424` appends `{"path": dest, "role": "merged", …, "block_sha256": …, "source": src, "commit": commit, "written": True}` — `commit` present, `gov_oid` absent, `oid` absent, whole-file `sha256` absent. That is exactly one of the two. `tools/pytest-parallel-guardrails/kit.toml:15` and `tools/govkit/entries/push-main.kit.toml:29-33` both declare a merged rule today, the second with `marker_style = "hash-comment"`, which is the branch that reaches `:2417` (`settings-merge`'s `json-pointer` rule `continue`s at `:2392` and writes no row). `-13` §4 declares a third deliberately, in the fixture family the fold built for AC13.

**So the receipt converges everywhere except on one row class, and closing it is one owner ruling rather than four seams of work.** The two directions are laid out under B1; this record does not pick between them, because the choice is about what a receipt row MEANS for a file gov only owns a region of, and that is not a reviewer's call.

## Did the fold hold?

**Mostly, and honestly.** All three blockers' core edits landed and are right. The fold also declared five defects it created and fixed in the same pass, in its own commit message, including catching that its own remedy for L6 was worse than L6. That is the behaviour this build wants.

Seven round-4 edits landed wrong or landed incompletely, and they are the seven findings below with a fold provenance:

- **M4 (`-7` S1) landed verbatim and is the blocker.** Its intent was right — stop stamping `gov_oid` onto rows carrying no `commit` — but it enumerated two producers where the tree has three, and the third is the one the same fold was documenting two sentences later.
- **M6 (`-7` S9) landed byte-identical in `-7` S9 and `-13` S7, and its conclusion sentence is now false.** "S9 passes over all of them for the one reason that covers every case — no operand" does not hold for a merged row, which has both `source` and `commit`. M6 enlarged the enumerated set past the reason that justified it.
- **H2's `install.sums` clause (`-13` AC10) landed with the wrong predicate.** It counts rows carrying a `commit`; all three call sites filter on `sha256`.
- **H2's other half (`-13` §4 + F5) landed and left `-7` §4's field dictionary contradicting it.** One stored field, two live definitions, differing on exactly the carried rows this build exists to create.
- **M5 (`-13`'s landing dependency on `-12`) landed correctly, and the same fold re-created the identical defect one AC later** by adding AC13 and AC14, which observe `-2`'s `pins` disposition, without adding `-2` to the same three places.
- **H1's skip rescoping landed in three specs at once and left the README on the old reading.** `-13` S7, `-12` §4 step 6 and `-7` S9 all moved; README line 54 did not.
- **B1's propagation reached `-9` §8 F3 and §10 but not `-9` S3**, the normative scope item a builder implements from.

One more: **L6's repair was made, then reverted inside the same commit for a good reason, and the revision log kept the reverted version.** The commit message records the reversal; `-4` §9 rev-4 does not.

## The fork B1 raises, and how it was resolved

B1 is an owner fork by the reviewer's own words, and under a standing mandate the build method
delegates the owner's resolver authority for the forks this build's specs state. It was resolved to
**Direction A**, and the reasoning is recorded here because the mark in `-7` §8 cannot carry it.

Both directions close the refusal. Direction B -- give the merged row both identities -- was
DISCARDED, and not on size. The reviewer states that under it `oid != gov_oid` is permanently true
on every merged row by construction, because the target's file is gov's block plus content gov does
not own. The build README's ratified architecture paragraph says, at line 55, that `oid != gov_oid`
**is** the local-delta predicate. Direction B therefore makes a whole row class read as carrying a
local delta forever, which does not fail an acceptance criterion but falsifies a ratified sentence,
and the method's tie-break is fewest follow-ups left open. Direction A leaves one: the sentence in
S9 saying the preamble is scoped by field presence and not by role must be narrowed, which Direction
A itself specifies.

Direction A was checked against all three vetoes before ratifying, since a surviving option that
trips one is a park rather than a resolution. It needs no new dependency, install location or public
surface, and it changes no governance carrier. It widens no write surface: `UPDATE_ROLE["merged"]`
is `block`, and that arm at `:2996-3005` computes a verdict, tallies, prints and `continue`s without
writing a byte. It fails no criterion already written.

Two facts the fold must carry, both verified in source rather than taken from the finding. The row
at `:2417-2424` carries `path`, `role`, `kit`, `version`, `block_id`, `marker_style`, `block_sha256`,
`normalized`, `mode`, `source`, `commit` and `written` -- `commit` present, `gov_oid`, `oid` and
whole-file `sha256` all absent, which is exactly one of the two. And TWO kits in this tree reach it,
not one: `tools/govkit/entries/push-main.kit.toml` and `tools/pytest-parallel-guardrails/kit.toml`
are both `marker_style = "hash-comment"`. `settings-merge` is `json-pointer` and `continue`s at
`:2392` without writing a row, so it is not a third.

## Blocker

**B1 — the `merged` row carries `commit` and no `gov_oid`, which is `-7` S9's own whole-run refusal shape.**
*Units: `-7` §2 S1 (:40-44) and S9 (:75-99); `-13` §2 S11 (:136-143) and §6 AC13 (:346-353). Provenance: round-4 part 1 M4 and part 2 M6.*

M4's edit landed exactly as written. `-7` S1 now covers two channels: the `writes` channel at `:2443-2460`, which carries `gov_oid` and `oid`, and the `unlanded` channel at `:2440`, which "carries neither, as it carries no `commit` today". Pre-fold S1 was unqualified — `git show 8e98a381^` reads "every receipt row gov writes carries `gov_oid` and `oid`" — and therefore covered every row `apply` produces, including `:2417`.

There is a third channel, and this same fold put it on the record. M6's new sentence, now byte-identical in `-7` S9 and `-13` S7, says `apply` skips merged entries in the unlanded list at `:2428-2429` and "writes the real merged row at `:2417` instead". Verified in source at `tools/govkit/govkit.py:2417-2424`: that row carries `source`, `commit` and `block_sha256`, and no `sha256`, no `gov_oid`, no `oid`. Correctly so — gov's bytes at that destination are a BLOCK inside a file the target owns, so there is no whole-file gov blob to hash, which is exactly why `-8` keeps `block_sha256` for it.

After the fold, a merged row therefore carries exactly one of `commit`/`gov_oid`, which is `-7` S9's third arm at `:89`: "A row carrying exactly ONE of the two is its own REFUSAL." S9 runs "in the preamble … over the whole receipt before any row is classified", beside the existing `raise Refusal` at `:2946`, so it is a whole-run stop and `-13` AC10's own words confirm such a refusal writes nothing and leaves the receipt byte-identical.

Three consequences, in descending order of how loudly they fail:

1. **The first `update` against any target that ever ran `apply` with `push-main` refuses everything**, the moment `-7` lands. Not hypothetical: `push-main.kit.toml:29-33` is `role = "merged"` with `marker_style = "hash-comment"`, the branch that reaches `:2417`.
2. **`-13` AC13 is unbuildable.** It requires `adopt --write` then `update --write` to print "one `pins` row and one `block` row rather than nothing" over a fixture `-13` §4 gives a merged rule, and the `block` row sits behind a preamble refusal.
3. **S9's own conclusion is now false.** With M6's gloss enlarging the enumerated set, "S9 passes over all of them for the one reason that covers every case — no operand" does not describe the merged row, which has both `source` and `commit`.

**This is an owner fork, not a mechanical fix.** Both directions close it; they mean different things.

**Direction A — exempt the merged row BY ROLE (smaller, and the reviewer's read of the design's intent).** In `-7` S1, name the third channel after the `unlanded` sentence: *"The `merged` row `apply` writes at `:2417` carries `source` and `commit` but NEITHER identity — gov's bytes at that destination are a BLOCK inside a file the target owns, so there is no whole-file gov blob to hash, which is why `-8` keeps `block_sha256` for it."* In S9, add a fourth arm immediately before the exactly-one sentence: *"A row whose `role` is `merged` is passed over whatever `commit` it carries. That `commit` names the vintage the BLOCK was taken from, `UPDATE_ROLE['merged']`'s own compare at `:2996-3005` is its reader, and S9 has no whole-file gov blob to assert against — so this is an exemption by ROLE, the one place this preamble is not scoped by field presence, and it is stated here rather than left to fall through the exactly-one branch."* Then narrow M6's conclusion to *"S9 passes over the `:2440` rows for the one reason that covers every case — no operand — and over a `merged` row by the role arm above."* The cost is real and should be paid consciously: S9 states in terms that it is "scoped by field presence and not by `role` or by `evidence`", and that sentence must be narrowed rather than left standing beside its own exception.

**Direction B — give the merged row both identities.** `gov_oid` from `blob_at(root, commit, source)`, `oid` from the target's index entry for the file the block sits in. S9's first arm then asserts it and the assertion holds. The cost: `oid != gov_oid` is permanently true on every merged row by construction, since the target's file is gov's block plus content gov does not own — harmless only because role `merged` dispatches to `block` at `:2996-3005` and never to the write arm, but it does add two fields to a row class whose bytes gov does not own, and it needs a sentence in `-13` S11 saying `adopt`'s merged rows carry them too.

**Under either direction:** `-13` S11 states the choice explicitly rather than inheriting it, a `refusal_join.py` arm asserts that a merged row does NOT refuse, and an acceptance criterion runs `update` over a fixture declaring one hash-comment merged rule so the arm is observed rather than assumed. A gate whose failing case has never been staged is an assertion about nothing, and this one currently fires on the whole tree.

## High

**H1 — `-13` AC10 counts `install.sums` lines by `commit` where every call site filters on `sha256`, so the criterion reds a correct build on its own fixture family.**
*Unit: `-13` §6 AC10 (:327-332). Provenance: round-4 part 2 H2.*

The fold applied H2's wording verbatim: "`install.sums` is non-empty, carrying one line per row that carries a `commit`, with `govkit.py check --target <fixture>` reporting N lines compared against N hashed rows for that same N."

All three call sites filter on `sha256`-presence, verified in source: the writer at `:2828-2830` is `"".join(f"{w['sha256']}  {w['path']}\n" for w in rows if "sha256" in w)`, `cmd_check`'s join at `:1551` is `want_pairs = {(f["sha256"], f["path"]) for f in rows if "sha256" in f}`, and `cmd_update` re-writes the sidecar with the same filter at `:3117-3119`. The fold's own §4 paragraph already says so — "Without it, `install.sums` (`:2828`) is empty".

The two populations diverge in **both** directions, and `-13` §4 puts both divergences in ONE fixture family. An `evidence: "unattributed"` row has no `commit` per S7 but carries `sha256` per §4's unconditional Data-model sentence, so it emits a sums line while carrying no commit. A `merged` row in `apply`'s `:2417` shape carries `commit` and `block_sha256` and never a whole-file `sha256`, so AC10 counts it and the sidecar omits it. §4 declares unattributable copies AND the merged rule in the same family, which is the family AC10 grades. A builder who implements the sidecar correctly reads N_sums ≠ N_commit and reds AC10; one who satisfies AC10 literally writes a second, divergent filter and then trips both `r.fail` arms at `:1552-1555`.

**Edit:** in AC10, replace "carrying one line per row that carries a `commit`" with *"carrying one line per row that carries a `sha256` — the filter the writer at `:2828-2830` applies, `cmd_check`'s join re-applies at `:1551` and `cmd_update` re-applies at `:3117-3119`, and which is NOT the same set as the rows carrying a `commit`: an `evidence: \"unattributed\"` row carries `sha256` with no `commit`, and a `merged` row carries `commit` with no `sha256`"*. Keep the N-against-N clause and add "and N greater than zero", since both sides render from one list and the equality is otherwise structural. Then state the split once in S5, beside F5: *"every destination row `adopt` writes carries `sha256`, attributed or `unattributed`, because F5 makes it the target's own bytes. S11's two synthesized classes do not — `apply` gives neither the `attributes` row at `:2350` nor the merged row at `:2417` a `sha256`, and `adopt` matches that — so neither appears in `install.sums`."*

**H2 — one receipt field, two live definitions: `-7` §4 says `sha256` is gov's bytes, `-13` §4 and F5 say it is the target's.**
*Units: `-7` §4 Data model (:130); `-13` §4 Data model (:173) and §8 F5. Provenance: round-4 part 2 H2.*

The fold added `-13` §4 line 173 — "`sha256` is `_sha` of the TARGET's bytes at the moment the receipt is written" — and ratified it as F5. `-7` §4's Data-model table, untouched by the fold and the build's only field dictionary, still reads `| sha256 | sha256 of gov's bytes at install | apply, update | install.sums and its join, and no verdict |`.

For a `verbatim` row the two readings coincide. For an `eol` or `relocate` row they are different bytes by construction, and those are the 11 rows `-9` §4 measures on inCMS and the entire reason `carry` exists. `-8` settles it the target's way independently — its rejected Alternatives bullet ("Stamp `sha256` with gov's bytes instead of the merge result") is refused because it "reds every merged target forever" — so `-7`'s cell is already wrong for merged rows at gov HEAD, before this build changes anything.

One of F5's three instruments is genuinely undercut and should not be cited: `-8` S6 moves `cmd_check`'s integrity loop onto `oid` and the provenance loop onto `gov_oid`, and `-8` is README step 3 while `-13` is step 5, so `:1513-1518` no longer reads this field by the time `adopt` lands. The `:2453`/`:2459` cite is weaker than F5 makes it sound rather than wrong: `cmd_apply` sets `data = blob_at(root, commit, w["src"])` and hashes that, which is gov's blob — indistinguishable from the target's only because `apply` then writes it.

**Edit:** define the field ONCE, in `-7` §4's table, and make `-13` point rather than restate. Change `-7` line 130 to *"sha256 of the bytes the row's destination holds in the TARGET at the moment the row is written — identical to gov's blob at `commit` for a `verbatim` row, the CARRIED bytes for an `eol`/`relocate` row (`-13` §8 F5), the merge result after `-8`"*, keeping the `install.sums`/no-verdict reader cell. In `-13` §4 line 173, replace "the same quantity `apply` records at `:2459`" with *"a NARROWING of what `apply` records at `:2459`, which hashes `data = blob_at(root, commit, src)` (`:2453`) — gov's blob, indistinguishable from the target's only while every row is `verbatim`"*. In F5, drop the `:1513-1518` instrument and say why: *"`-8` S6 moves both `cmd_check` loops onto `gov_oid` and `oid`, so by the time `adopt` lands no check reads this field and `install.sums` is its only reader — which is what makes the choice free, and what makes stating it in one place mandatory."*

## Medium

**M1 — `-13`'s land-alone line, F3 and the README `deps` cell all omit `-2`, whose `pins` disposition two of the fold's new criteria observe.**
*Unit: `-13` §3 land-alone (:160-162), §8 F3 (:383-388); build README `deps` row and landing-order step 5. Provenance: this fold's own AC13 and AC14.*

AC13 asserts that after `adopt --write` then `update --write` the run "prints one `pins` row and one `block` row rather than nothing", and its RED arm names "`-2`'s `pins` arm never dispatches". AC14 asserts "the `attributes` row reaches `-2`'s `pins` arm and reports". The `pins` disposition is `-2`'s entire deliverable — `-2` S1 changes `UPDATE_ROLE["attributes"]` from `refuse` to `pins`, and `-2` §1 records that until it lands, one `attributes` row makes "every future `update` on that target exit 1". So with `-2` absent, AC13's `update --write` exits 1 and never prints a `pins` row.

`-13` §3, F3 and the README all resolve to the same five units — `-1`, `-7`, `-9`, `-10`, `-12`. This is the exact criterion-dependency shape M5 filed against `-12`, re-created one AC later by the fold that fixed it, and the README designates §3 as the authority: "Each unit's §3 land-alone line is the authority; the `deps` column above mirrors it."

**Why medium and not high:** no landing can actually go out of order. `-13` requires `-7`, and `-7` §3 states "Land-alone: no, and `-2` lands first", so `-2` is guaranteed beneath `-13` by a recorded chain. The defect is an incomplete governing line, not a broken order.

**Edit:** add `-2` to `-13` §3's land-alone bullet — *"…and `-12` (the S7 vintage guard AC11 observes) and `-2` (the `pins` disposition AC13 and AC14 observe) beneath it"* — and to §8 F3's resolution line in the same shape it just took for `-12`. Change the README `deps` cell to `1, 2, 7, 9, 10, 12` and amend step 5 to *"…and `-2` beneath it; `-2`'s `pins` disposition is what AC13 and AC14 observe, and step 1 already puts it below this one."*

**M2 — `-13` AC6 does not name its fixture's role, and after H1's rescoping the assertion holds only for `table` roles.**
*Unit: `-13` §6 AC6 (:307-312). Provenance: round-4 part 2 H1's propagation.*

H1's propagation rewrote AC6's closing clause to "never reaches `classify_row` (`:3014`) for it", but AC6's fixture is still described only as "one destination that matches no gov vintage … keeps the `role` its rule declared". Under the fold's own S7 the skip is scoped: "a row carrying `evidence: \"unattributed\"` whose role resolves at `:2974` to the `table` disposition is printed, counted and skipped before `classify_row`". `UPDATE_ROLE` at `:2857-2866` maps only `engine` to `table`; `seed` is `report-reseed`, `attributes` is `refuse` (`pins` after `-2`), and `-10` gives `forked` `report`.

A `seed` destination matching no gov vintage is a natural reading of AC6's sentence and a natural fixture to build — and AC14, added by the same fold, asserts the *opposite* outcome for exactly that row. A builder who declares the AC6 fixture's rule as `seed`, `rendered` or `forked` watches the row reach `classify_row`, reds AC6, and spends the cycle hunting a scoping bug in a correct implementation. The role is the only field that decides which of the two criteria applies, and AC6 is the one that does not name it.

**Edit:** amend AC6's first sentence to *"A fixture carrying one destination whose rule declares role `engine` — so the row resolves at `:2974` to the `table` disposition — and which matches no gov vintage writes that row with `evidence: \"unattributed\"` …"*, and close it with *"AC14 owns the non-`table` roles, which dispatch instead of skipping; the two criteria partition the population and neither generalizes to the other's half."*

**M3 — `-13` AC14 requires a bootstrapped receipt carrying an "unattributed `attributes` row", a state S11 never writes, and `-13` never decides whether S11's classes carry `evidence`.**
*Unit: `-13` §6 AC14 (:353-359) against §2 S11 (:136-145) and S7. Provenance: round-4 part 2 H1.*

The `seed` half of AC14's fixture is producible — `seed` is in `LANDABLE_ROLES` (`:230`), so a seed destination comes through the `writes` channel and takes S5's row shape, `evidence` included. The `attributes` half is not. S11, added by the same fold, writes that row "in `apply`'s shape" from `:2350` and enumerates its keys as `block_id`, `marker_style`, `mode`, `normalized`, `block_sha256`, `patterns`, with `written: false`. Verified at `govkit.py:2350-2355`: no `evidence`, no `commit`, no `gov_oid`. S7's skip keys on `evidence: "unattributed"` and explicitly rejects field-absence as an equivalent, so an attributes row with no `evidence` is never a skip candidate under the folded reading, and the fixture AC14 describes cannot be produced by `adopt` at all.

Both of AC14's arms remain discriminating — the RED-first half is a field-absence skip, which does swallow the row — so this is not a build-stopper. But a builder is told to construct a receipt state the writing verb does not emit, and cannot resolve the question from the text.

**Edit:** decide it in S11, in one sentence: *"Neither synthesized class carries `evidence`. Both are measured from the target's own bytes rather than attributed to a gov vintage, and S7's skip is keyed on `evidence: \"unattributed\"`, so both dispatch through `UPDATE_ROLE` unconditionally."* Then reword AC14's fixture clause to *"a bootstrapped receipt carrying an unattributed `seed` row and S11's synthesized `attributes` row"*, and its RED-first arm to *"under a skip scoped by FIELD ABSENCE, both rows are swallowed — the `seed` row carries no `commit` and no `gov_oid`, and the `attributes` row carries neither by construction — and neither disposition ever runs."*

**M4 — `-9` S3 still says the needle map is receipt-derived; the fold amended F3 and §10 and left the scope item alone.**
*Unit: `-9` §2 S3 (:40-43), against `-13` §2 S4a and `-9` §8 F3 / §10. Provenance: round-4 part 2 B1's propagation.*

S3, unchanged, reads: "`alpha` is DERIVED from the receipt and never authored … There is no override key and no descriptor field: an authored map is a second answer to a question the receipt already answers." The fold's `-13` S4a has `adopt` derive `alpha` "from the planned `(src, dest)` pairs `resolve_entry` returns for THIS run", and propagated that into `-9` §8 F3 ("`adopt` is the derivation's SECOND caller and reads the descriptor pairs instead") and `-9` §10 ("two callers… The second is the `adopt` verb `-13` adds, which feeds it the planned descriptor pairs") — and stopped there.

S3 is the normative scope item and the one other specs CITE: `-13` S4a defers to it for "the ambiguity drop and the report line of `-9` S3". Its stated input source is now false for one of two ratified callers. A builder reading S3 writes a helper whose parameter is a receipt row list, and `-13`'s builder, holding descriptor pairs and no receipt, has nothing to call. This is the same unqualified-quantifier shape the fold repaired one spec over in `-7` S1.

**Not high**, because the correct two-caller shape is stated plainly in §10 and F3, so a `-9` builder reading the spec whole is not misled into duplicating the derivation. The risk is a helper signature, and no acceptance criterion becomes unbuildable. The narrower half of the original finding is also wrong and is not carried here: `-13` S4a adds no descriptor FIELD, so S3's "no override key and no descriptor field" clause is not contradicted — only the receipt-source sentence is.

**Edit:** rewrite S3's opening two sentences to *"`alpha` is DERIVED, never authored, and the derivation takes a SEQUENCE OF PAIRS rather than a receipt, because it has two callers. `cmd_update` feeds it the receipt: each row contributes one pair, `(dirname(source), dirname(path))`. `adopt` feeds it the planned `(src, dest)` pairs of its own run, lifted the same way — `-13` S4a, and §8 F3 records why that is not a re-opening of the fork. The pairs are deduplicated; any gov directory that yields two DIFFERENT target directories is DROPPED and reported by name."* Then narrow the closing sentence to what it actually forbids: *"There is no override key and no AUTHORED descriptor field: a hand-written map is a second answer to a question the caller's own pairs already answer."*

**M5 — `-14` AC6 asserts a tally state `not-run` that S1's return set, S8 and §5's enumeration all omit.**
*Unit: `-14` §6 AC6 (:188-193) against §2 S1 (:30), S8 (:71) and §5 observability (:147). Provenance: round-4 H3's rewrite carried the tail forward.*

H3 corrected AC6's subprocess count from one to two and left its tail unchanged: "the tally names the other two kits as `not-run` with zero subprocesses for them." Grepped over the whole spec, `not-run` occurs exactly once — in AC6 — and is defined nowhere. S1's helper returns exactly three states (`adopted`, `landed-but-inert`, `landed-unmeasured`); S8 names the fourth printed word, `unverified`; §5's observability line enumerates the tallies as "verified, unverified, rolled back and pre-existing red" and closes "Every one of those counts is printed even when it is zero", which reads exhaustive, and §5 gives untouched kits no line at all ("one line per touched kit").

A builder who implements §5 as written prints four tallies, none naming an untouched claimed kit, and reds AC6 — the one criterion that fences S4's baseline against both over- and under-running, so the arm least able to afford an unbuildable half. The tally is arguably the wrong instrument anyway: a kit that was never executed has no state to tally, which is presumably why §5 never listed one. The subprocess half of AC6 is correct and should not move.

**Edit:** pick one and make it the same in both places. Either add the state where it is owned — S4 gains *"a kit the run did not touch is printed once as `not-run` and counted under its own tally"* and §5's enumeration becomes "verified, unverified, not-run, rolled back and pre-existing red" — or restate AC6's tail against what §5 already prints: *"and the other two kits appear in the run's per-kit output with zero `[check].argv` subprocesses recorded against them, under whatever S4 calls the untouched state."*

## Low

**L2 — `-13` S10's envelope table still routes `files` to "the rows S1–S7 describe" after S11 added two row classes to that array.**
*Unit: `-13` §2 S10, the envelope table (:124). Provenance: this fold's own B2.*

The cell reads `| files | the rows S1–S7 describe | everything |`. It was set when the last row-producing scope item was S7. B2 added S11 — "the row classes `resolve_entry` does not produce" — which puts the synthesized `attributes` row and the merged rows into that same array. AC10 asserts the envelope's key set against this table, and AC13 asserts `install.json` "carries exactly one row with `role: \"attributes\"`", a row S10 says is not in `files`.

Nothing breaks at build time — S11 is the very next scope item and states both classes explicitly — but S10 is the unit's one normative statement of what the envelope holds and it under-describes its own largest key.

**Edit:** change the cell to "the rows S1–S7 describe, plus S11's two synthesized classes". The same table's `kits` cell is correct and needs no change.

**L3 — the build README states the pre-fold ordering for the unattributed skip that H1 moved in three specs.**
*Document: build README (:53-54), against `-13` S7, `-12` §4 step 6 and `-7` S9. Provenance: round-4 part 2 H1's propagation.*

README line 54 says the unattributed state is "printed, counted and skipped before any writing disposition is consulted". The fold moved that skip everywhere else: `-13` S7 now reads "skipped before `classify_row` at `:3014` — after `how` resolves, before the verdict table it feeds"; `-12` §4 step 6's failure cell reads "after `how` resolves and before `classify_row`"; `-7` S9 takes the same wording, and `-7` rev-5 records H1 as moving it "NOT ahead of `:2974`". Resolving `how` at `:2974` **is** consulting the disposition — that is the whole of H1 — so the README states precisely the ordering the fold removed from three specs, and it is the document a reader opens first.

Behaviourally harmless: the row is still never written either way. But it is the architecture-of-record and the only text left on the old reading.

**Edit:** change README line 54 to *"printed, counted and skipped once its role resolves to the one disposition that writes, before the verdict table"* — the ordering the three specs now share, with no line-number citation, which keeps the README's architecture prose free of source pins.

---

## What the fold got right

Named specifically, because a fold that closes three blockers and creates one deserves the ledger read both ways.

- **B1's core is a good answer, not a patch.** S4a states the bootstrap-side derivation completely and delegates the ambiguity drop and the report line to `-9` S3 rather than restating them, so there is one derivation with two inputs instead of two derivations.
- **B2's core is in the build's own preferred form.** S11 names both synthesized classes and points at the source literal that owns each shape (`:2350`, `:2417`) instead of re-typing key lists that would rot. It came with two new criteria, AC13 and AC14, that actually observe them.
- **B3 landed redundantly on purpose.** `-14` S3, §4's Data model and AC4 each independently enumerate all six snapshot fields, so the under-glossed appositive that two round-5 lenses attacked cannot subtract a field from the list it follows. Both attacks were refuted on exactly that ground.
- **The fold verified before folding.** Its commit message records checking that `:1570` really is a bare `row["block_id"]` subscript and that `:2828` really filters on `"sha256" in w` — both confirmed here — rather than trusting the review's citations.
- **It corrected the review that commissioned it.** Five defects the fold introduced or exposed were fixed in the same pass and declared, including an off-by-one in the round-4 record's own `:2427-2428` citation, propagated to all five sites.
- **L6's judgment was right even though its log was not.** The fold made the AC2 split, discovered the newline broke the inline code span, and reverted it in the same pass. Only the revision log was left behind, which is L1 and is the cheapest defect in this record.
- **M3 was disposed of honestly.** `-9` AC2's `13`/`26` are flagged UNVERIFIED, with the population they were measured over named against the population the criterion runs on, and an instruction to re-measure before the arm is written — and an explicit refusal to edit the numbers until they fit. Four separate round-5 findings tried to re-file this as a defect; all four were refuted, and the flag is the better of the states available in a tree that does not contain inCMS.
- **The vocabulary held.** `gov_oid`, `oid`, `carry`, `verbatim`/`eol`/`relocate`, `forked` and `evidence` are still used identically across all 15 documents with no synonym introduced anywhere by the fold. Round 4 called that settled and it stayed settled.
- **L1's arm count was re-derived rather than copied.** The fold took twenty per BRANCH instead of the review's asserted fourteen, which predated the fold's own new branches, and put the enumeration in §5 so the arithmetic is checkable.

## What remains unverified

Stated plainly, because a green convergence answer over unmeasurable ground would be worth nothing.

- **`-9` AC2's `13` pairs and `26` needles cannot be closed in this tree.** They must be measured over inCMS at `2cff5855`, a population this repo does not contain. Round 5 could not verify or falsify them either, and neither could round 4's fold. The spec's flag is the honest state; it stays a DoR item for whoever has that checkout.
- **`-6` AC6's and `-4` AC3's inCMS readings depend on a descriptor this build does not write.** `ABL-dPinnedVintage-1` lands `.governance/deploy.toml` in `d41ly/incms`, outside this build's carry, and both criteria's `[kit.*]` layout overrides are only checkable there.
- **F5 is an agent inference the owner has not ratified.** `-13` F5 says so itself — "Recorded as the round-4 reviewer's inference from those three instruments rather than as a measured fact, and flagged there as a decision the owner should ratify." H2 above makes the definition consistent; it does not make it ratified, and one of F5's three instruments is removed by `-8` before `adopt` ever runs.
- **B1's remedy is an owner fork and this record does not pick.** Direction A costs S9 its field-presence purity; direction B adds two fields to a row class whose bytes gov does not own. Both close the refusal; they say different things about what a merged row means.
- **No arm has ever been run.** All 15 specs are SPECCED, every line citation is a source read at `9ddcc5c9`, and no gate, selftest or `refusal_join.py` arm in this build has been observed either green or red. In particular B1's refusal has been derived from source and from the two kit descriptors, not reproduced by running `update` against a target carrying a merged row — that reproduction is the cheapest way to confirm this record's blocker and is worth doing before folding it.
- **The AC13/AC14 fixture family exists only as a §4 estimate.** `-13` §4 is headed "Files touched (estimate)" and declares one family carrying verbatim, `eol`, `relocate`, unattributable, declared-forked, one `[[lf_pin]]`, one merged rule and one ambiguous gov directory. Whether one family can carry all of that without arms interfering is unmeasured, and three round-5 findings turn on which fixture a criterion runs over.
- **One observation outside the confirmed set, flagged as such.** `-13` §9's rev-4 entry labels itself "round-5 fold" while rev-5 labels itself "round-4 fold"; rev-4 was written by commit `2f9d7a4f`, the third-round fold, so the label is wrong and inverted against its neighbour. It is pre-fold text this round's subject never touched, no skeptic verified it, and it is recorded here only so round 6 does not spend a lens rediscovering it.
