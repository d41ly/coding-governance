# Pre-code review, round 4 — part 2 of 2, the receipt and reach units, DEPL-dCarriedReceipt-9..15

**Serves:** spec-audit DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15

**Reviewed:** all 15 specs plus the build README, in ONE pass, against the round-3 fold at
`2f9d7a4f`. **Base:** `f39cf548`, worktree clean. Source read at `9ddcc5c9`; `tools/govkit/govkit.py`
and `tools/govkit/refusal_join.py` are byte-identical between the two, so every line citation holds
at either sha.
**Harness:** four primed finder lenses over the folded set (contradiction, underspecification,
unstated assumption, fold regression), then batched default-refute skeptics over every finding, then
one synthesis. Ten agents, all returned. Thirty-six confirmed entries arrived; deduplicated they are
the 21 defects across both parts of this record, and eleven were refuted and are named so round 5
does not re-file them.
**Why this record is in two parts:** the Serves id list renders into one build-README table row and
15 ids blow its entry cap. That is DEPL-dCarriedReceipt-16, and round 1 split on the same boundary.

This record carries the convergence answer, all three blockers, and the findings against units
9-15. Units 1-8 are part 1, `2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md`.

## Verdict: BLOCKED

Three blockers, all one shape, and they land on two specs: `-13` carries B1 and B2, `-14` carries
B3.

## The convergence question, answered

**No — the 15 specs do not yet describe one build.** They describe one build's *vocabulary* and one
build's *order*; they do not yet describe one **receipt**.

What converged, and should now be treated as settled: `gov_oid`, `oid`, `carry`,
`verbatim`/`eol`/`relocate`, `forked` and `evidence` are used identically in all 15 documents with
no synonym anywhere; the round-3 blockers really are fixed (the receipt envelope's key set, the
`gov_commit` stamp, the build-wide definition of "dirty"); the dependency graph is acyclic and every
`§3` land-alone line agrees with the README's `deps` column except one cell (M5).

What did not converge is a single seam, wearing four hats. `-13` specifies `adopt` as a walk over
`resolve_entry`'s two row channels **and nothing else**, so everything `cmd_apply` synthesizes
*outside* that function is absent from the bootstrapped receipt: the one `role: "attributes"` row
(`:2350`), the real `merged` row with its `block_id`/`marker_style`/`block_sha256` (`:2417`), and the
`sha256` field (`:2459`). Downstream, `-2`'s entire `pins` disposition never dispatches on any real
adopter, `cmd_check` raises on any adopted target carrying a merged rule, and `install.sums` ships
empty while the check that grades it compares zero against zero. The fourth hat is the input rather
than the output: the `relocate` rung's needle map is defined by `-9` as derived **from the receipt**,
which is the artifact `adopt` is creating. `-14` is the same class one layer down — it snapshots four
of the six fields `-11` rewrites as a set, so a rolled-back rename splits exactly the pair `-7` S9
refuses on.

That is B1–B3 and H2, and it is one question nobody asked: *what is in a row, and who writes it?*
The build has one unit that writes a receipt and seven that read one, and no pass has ever
reconciled them field by field. The rest of this record is smaller. The fold half-landed in five
places — S7's scoping propagated to one of four sites, `BRANCH_PIN`'s repair to one of four, the arm
counts to none of six, the ordering table's new row to the wrong slot — and none of that needs a
design decision, only a careful diff.

---

## How the rounds were recorded

`--review` makes a `CONVERGED` subject TERMINAL: it refuses a later round for that subject, on the
reasoning that recording more would make the sequence say the opposite of what happened. M4 makes a
spec whose rev moved since its last review unreviewed again. Those two rules meet head-on for any
spec this round both cleared of blockers AND edited in the fold, so the round was recorded only
where it is final:

- `DEPL-dCarriedReceipt-13` (2 blockers) and `DEPL-dCarriedReceipt-14` (1 blocker) are recorded now,
  and are the two subjects still open.
- The four specs this round leaves untouched -- no finding at any severity -- are recorded now as
  converged, because nothing will edit them.
- The nine specs that take a fold have their round recorded once their text is final, so that a
  defect the fold itself introduces still has a round to be recorded in. This corpus has a measured
  history of fold text being the least-reviewed surface in the tree.

## Blockers

**B1 — `-13` S4/AC4/AC5: `adopt` has no needle map, so the `relocate` rung cannot fire.**
`-13` S4 makes attribution RUNG-MAJOR — "every commit in the walk is tested at `verbatim` first, then
`eol`, then `relocate`, and the newest commit within the FIRST rung that matches wins" — and AC4 and
AC5 each require a proven `relocate` match. The rung's only input is `-9`'s `alpha` map, and `-9` S3
says it "is DERIVED from the receipt and never authored. Each row contributes one pair,
`(dirname(source), dirname(path))`... There is no override key and no descriptor field". `-9` §8 F3
ratifies that derivation and rejects the descriptor route by name, because "re-resolving would also
make the map drift the moment a descriptor's `to` changes", and `-9` §10 records "one caller inside
`cmd_update`". The strings `alpha` and `needle` do not appear in `-13` at all.

`adopt` exists precisely because no receipt exists: `-13` §1 states that `cmd_update` refuses without
`<target>/.governance/install.json` (`:2932`) and that neither live target has one. So the rung `-13`
§4's own inventory leans on — "the `eol` and `relocate` rungs are what must reduce the remaining 25"
— has no map, the ladder collapses to `verbatim`/`eol`, and every relocated row bootstraps as
`evidence: "unattributed"`, including the five rows `-9` §4 measures as `relocate`. S7 then skips
those rows forever. AC4 and AC5 are unbuildable as written, and a builder cannot resolve it alone
because the answer is a ratified fork in another spec.

**Edit:** add `-13` S4a — "`adopt` derives `alpha` from the planned `(src, dest)` pairs
`resolve_entry` returns for THIS run, lifted by `dirname` and deduplicated, with the ambiguity drop
and the report line of `-9` S3. The receipt derivation `-9` F3 ratifies is unavailable before a
receipt exists, and the descriptor pair is the only record of where a file would land." Add a closing
sentence to `-9` §8 F3: "`adopt` is the derivation's SECOND caller and reads the descriptor pairs
instead, because at bootstrap there is no receipt to read; the drift objection above is about
`update`, where a receipt exists." Correct `-9` §10 to name both callers. Add `-13` AC12 asserting
that the map `adopt` derives over the AC5 fixture drops an ambiguous gov directory by name and emits
the same needle count `-9` AC2 asserts.

**B2 — `-13` S2/S5/§4: the destination set is `resolve_entry`-only, so two row classes have no
producer and two dispositions are dead on every adopted target.**
`-13` S2: "the destination set comes from `load_deploy` (`:553`), `target_context` (`:535`) and
`resolve_entry` (`:270`), one entry at a time, and it takes BOTH of that function's row channels: the
landable `writes` map (`:307`) and the `unlanded` list (`:309`)." Verified in source: `resolve_entry`
(`:270-312`) partitions only the descriptor's `files` rules into those two channels. The
`role: "attributes"` row is synthesized elsewhere — one aggregated row at `:2350` carrying `path`,
`role`, `kit: "(govkit)"`, `version: "(synthesized)"`, `block_id`, `marker_style`, `mode`,
`normalized: "lf"`, `block_sha256`, `patterns` and `written` — and the real `merged` row is written
at `:2417` with `block_id`, `marker_style` and `block_sha256`, after `cmd_apply` deliberately
`continue`s past merged entries in the unlanded loop at `:2427-2428` ("written above, or delegated at
configure"). None of those keys appear in `-13` S5's row list or in §4's Data model.

Two consequences, both on real adopters. An adopt-bootstrapped receipt carries no `attributes` row,
so `UPDATE_ROLE["attributes"]` is never dispatched and `-2`'s whole `pins` disposition — the unit
whose §1 is "One `attributes` row in a target makes every future `update` on that target exit 1" —
never fires; `-13` S10's own table cites "`-2`'s pins arm" as a downstream reader of `kits` while the
row that arm dispatches on is never written. And because `-13` takes the `unlanded` channel whole, it
writes merged rows in the stripped shape `apply` refuses to write: `cmd_check`'s merged loop filters
on `role == "merged"` at `:1563` and then reads `row["block_id"]` unguarded at `:1570` inside
`marker_pair(row.get("marker_style"), row["block_id"])` — a `KeyError` on a row that has neither, and
a by-design `Refusal` at `:1706` if only the style is missing. So `check` breaks on any adopted
target with a merged rule. One correction to keep the fixer honest: `UPDATE_ROLE["merged"]`'s block
arm (`:2996-3005`) compares gov blobs at `commit` versus `to_commit` and never reads `block_sha256`
— the reader is `cmd_check`.

**Edit:** add `-13` S11 — "the row classes `resolve_entry` does not produce. `adopt` writes the ONE
`attributes` row `cmd_apply` synthesizes at `:2350`, recomputed by `lf_pins()` (`:1805`) over the
claimed kits at `--to` and compared against the target's existing govkit-owned block: same keys
(`block_id`, `marker_style`, `mode`, `normalized`, `block_sha256`, `patterns`), with
`written: false` because this verb wrote no block. It also writes each `merged` row in `apply`'s
shape (`:2417`), not the unlanded one — `block_id`, `marker_style` and `block_sha256` measured from
the block the target actually holds — and skips merged entries in the unlanded channel exactly as
`apply` does at `:2427-2428`. Without both, `-2`'s `pins` arm never dispatches and `cmd_check`'s
merged loop raises on `row['block_id']` at `:1570`." Add AC12: "on a fixture declaring one
`[[lf_pin]]` and one merged rule, `adopt --write` then `update --write` prints one `pins` row and one
`block` row rather than nothing, `install.json` carries exactly one row with `role: \"attributes\"`
and `path: \".gitattributes\"`, and `govkit.py check --target <fixture>` reports the merged block
intact rather than raising." If the owner instead rules that `adopt` must not claim a block it did
not write, then `-2` §3 must state that its `pins` arm is unreachable on adopted receipts and `-13`
S10's table must stop citing it — but the merged half has no such escape.

**B3 — `-14` S3/§4/AC4: the rollback snapshot omits `path` and `source`, wedging every later run
after a rolled-back rename.**
`-14` S3 reads "the snapshot also captures each touched ROW's `sha256`, `commit`, `gov_oid` and
`oid` **before** the loop mutates them in place at `:3072-3073` and `:3098-3099`", and §4's Data
model and AC4 repeat the same four; rev-4's own log calls them "the receipt's four identity fields".
`-11` S4 rewrites six: "the row's `path`, `source`, `commit` and `gov_oid` are rewritten TOGETHER,
never one without the others". `-14` S5 restores a renamed row's paths from S2's index entries, which
are `(mode, oid)` per path, and its row fields from S3 — which has no `path` and no `source`.

So a rename that lands and then reds its kit's `[check].argv` rolls back to `commit`/`gov_oid` at
their pre-rename values beside `path`/`source` at their post-rename ones. On the next run `-7` S9's
preamble asserts `gov_oid == blob_at(root, row["commit"], row["source"])` over every row carrying
both — gov's blob at the old commit for a source that does not exist there — which is S9's
exactly-one-of-the-two corruption shape, and it refuses the whole run by name. The state persists:
at `:3115` the `if r.problems` arm still writes the receipt back, withholding only `schema` and
`gov_commit`, so the mutated rows reach `install.json` on the very run that rolled back. `-14` §3
refuses `--force` and S6's pre-existing-red escape does not reach it, so the only remedies are
hand-editing `install.json` or `adopt --re-adopt`, which by `-13` F2 discards every row's measured
base. This is fold damage of a specific kind: rev-4 added `oid` and audited the field set against
`-7`'s, never against `-11` S4's.

**Edit:** in `-14` S3, §4 Data model and AC4, change the enumeration to "`path`, `source`, `sha256`,
`commit`, `gov_oid` and `oid` — every field `-11` S4 rewrites as a set, plus the two identities", and
cite `-11` S4 as the third mutation site beside `:3072-3073` and `:3098-3099`. Add to S5: "restoring
a renamed row restores `path` and `source` together with `commit` and `gov_oid`, because `-7` S9
asserts them against each other and a partial restore is the split that assertion exists to refuse."
Extend AC3's rename arm with: "and the rolled-back row's `path` and `source` both carry the OLD
spelling, so `-7` S9's preamble assertion holds on the next run."

## High

**H1 — `-13` S7: the fold's scoping sentence contradicts the ordering sentence directly above it, and
three other documents still state the old reading.** Filed by three lenses; merged here.
`-13` S7 still opens "a row carrying `evidence: \"unattributed\"` is printed, counted and skipped
BEFORE `UPDATE_ROLE.get(role)` at `:2974` is consulted", and fifteen lines later the fold's new
paragraph says "The skip is therefore scoped to rows whose role carries a WRITING disposition;
`skip`, `adopter`, `block` and `report` roles continue to dispatch through `UPDATE_ROLE` exactly as
they do today." Verified in source: `how = UPDATE_ROLE.get(role)` at `:2974` is the first statement
of the row loop, so "does this role write?" is a fact only `:2974` supplies — a skip scoped by the
answer cannot precede the question. The exemption list is also short: `UPDATE_ROLE` at `:2857-2866`
carries `table`, `report-reseed`, `skip`, `adopter`, `block` and `refuse`, and after `-2` and `-10`
the live set is `table`, `report-reseed`, `skip`, `adopter`, `block`, `pins`, `report` — `refuse`
leaves the table entirely, and `report-reseed` (role `seed`) and `pins` (role `attributes`) are named
nowhere, so an unattributed `seed` row has no stated treatment. Three documents still carry the
pre-fold reading verbatim: `-13` AC6 ("never reaches `UPDATE_ROLE.get(role)` (`:2974`) for it"),
`-12` §4 table row 5 ("print, count, skip the ROW, before `UPDATE_ROLE`", edited by the same commit),
and `-7` S9's closing sentence ("ahead of `UPDATE_ROLE.get(role)` at `:2974`"). The build README
already states the scoped reading, so the specs are the wrong documents.

Source settles the predicate, and it is narrower than either sentence: `table` is the only
disposition that puts bytes on disk (`if a["how"] != "table": continue`, `:3063`). Everything else is
report-only, and three of those read a base and will report against `base = None` on an unattributed
row — `report-reseed` prints `reseed-available` via the seed override at `:3016-3020`, `adopter`
prints a capped `re-rendered` at `:3021`, and `block` prints `block-moved` because `base2` is `None`
at `:3000` and `_sha(None)` never equals gov's blob. None of the three writes anything, but `block`'s
line is an unearned claim that gov's block moved, and S7's paragraph names that compare as something
it rescued, so it should say so.

**Edit:** in `-13` S7, replace the opening clause with "a row carrying `evidence: \"unattributed\"`
whose role resolves at `:2974` to the `table` disposition is printed, counted and skipped before
`classify_row` at `:3014` — after `how` resolves, before the verdict table it feeds." Replace the
scoping paragraph with: "`table` is the only disposition that can put bytes on disk (`:3063`), and
this skip exists to stop a write against a base that does not exist. Every other disposition
dispatches exactly as today: `skip` counts at `:3006-3008`, `block` runs its own compare at
`:2996-3005`, `adopter` caps at `re-rendered` at `:3021`, `report-reseed` runs the seed override at
`:3016-3020`, and `-2`'s `pins` and `-2`/`-10`'s `report` are report-only by construction. Three of
those read a base and report against `base = None` on an unattributed row — `reseed-available`, a
capped `re-rendered`, and `block-moved` — and the tally §5 requires is where an operator sees them."
Then propagate: `-13` AC6's closing clause becomes "never reaches `classify_row` (`:3014`) for it";
`-12` §4 row 5's decision cell becomes "does this ROW carry `evidence: \"unattributed\"` AND resolve
to the `table` disposition?" and its failure cell "print, count, skip the ROW, after `how` resolves
and before `classify_row`"; `-7` S9's closing sentence takes the same wording. Add an AC over an
unattributed `seed` row and an unattributed `attributes` row asserting which path each takes.

**H2 — `-13` §4/S5/§3: `sha256` is dropped from the row shape, so `adopt` writes an empty
`install.sums` and `check` grades zero against zero.** Filed by three lenses; merged here.
`-13` §4's Data model claims completeness while mis-quoting its own citation: "Each written row
carries the receipt shape `apply` already produces at `:2458-2460` — `path`, `role`, `kit`,
`version`, `source`, `commit`". That literal is seven keys, not six: `"sha256":
hashlib.sha256(data).hexdigest(),` sits at `:2459`. S5's field list omits it too, and a grep of `-13`
for `sha256` returns nothing. `-7` S1 says the opposite ("`sha256` is still written, is still what
`install.sums` lists") and `-7` §8 F3 ratifies retaining it ("Dropping it breaks `install.sums`").

`-13` §3 nevertheless commits the verb: "`adopt` writes `install.json` and `install.sums` under
`--write` and nothing else." The sidecar writer at `:2828-2830` renders `f['sha256']` only `for f in
rows if "sha256" in f`, so `adopt` produces a **zero-byte** `install.sums`; `cmd_check`'s join builds
`want_pairs` with the same filter at `:1551` and prints a clean "0 line(s) compared against 0 hashed
row(s)"; and `cmd_update` re-writes the sidecar with that filter at `:3117` and `:3128`, so it stays
empty forever. Worse, `cmd_check`'s integrity loop reads `want = row.get("sha256")` and its arm is
`if want and _sha(...) != want: fail / else: n_ok += 1` (`:1513-1518`), so every field-less row counts
as VERIFIED without a byte being hashed. That is the reads-zero-on-both-arms shape, on the artifact
an adopter is told they can verify with bash alone. The counter-argument — a builder who opens the
cited literal lands the field anyway — is real but does not save it: two prose enumerations omit it,
prose is what gets typed, and `-7` F3 already ratified the opposite.

The edit must also decide something no spec has: for a carried (`eol`/`relocate`) row, gov's bytes at
`commit` and the target's bytes on disk diverge for the first time, and `sha256` cannot be both.
`cmd_apply` hashes the bytes it wrote to the target (`data` at `:2459`), `-8`'s ratified Alternatives
bullet keeps `_sha(merged)` for the same reason, and `cmd_check`'s integrity loop compares the field
against the target's file — so the field is the TARGET's bytes at receipt-write time, which is also
the only reading under which `install.sums` survives a plain `sha256sum -c`.

**Edit:** add `sha256` to `-13` S5's field list and correct §4's quotation to "`path`, `role`, `kit`,
`version`, `sha256`, `source`, `commit`", with the sentence "`sha256` is `_sha` of the TARGET's bytes
at the moment the receipt is written — the same quantity `apply` records at `:2459` and the quantity
`cmd_check`'s integrity loop compares at `:1513-1518` — so `install.sums` stays verifiable with
`sha256sum -c` on a tree `adopt` did not touch. Without it, `install.sums` (`:2828`) is empty,
`cmd_check`'s sidecar join (`:1551`) compares zero rows against zero lines and passes, and its
integrity loop counts every row as verified without hashing anything." Record that choice as a
resolved fork in `-13` §8 rather than leaving it implicit. Extend AC10: "and `install.sums` is
non-empty, carrying one line per row that carries a `commit`, with `govkit.py check --target
<fixture>` reporting N lines compared against N hashed rows for that same N."

**H3 — `-14` AC6 asserts one check subprocess where S4 mandates two, so it reds a correct build.**
AC6: "Only touched kits run. In a fixture claiming three kits where one moves rows, exactly one
`[check].argv` subprocess is observed and the tally names the other two as `not-run`." S4 says the
opposite — "S1's helper runs TWICE for every TOUCHED kit: once as a BASELINE before the first byte
moves, and once after the write loop" — and §5's perf note agrees with S4: "two checks per TOUCHED
kit, one baseline and one after ... On a run that moves rows in two kits, four checks run." One
touched kit is two subprocesses. AC6 counts subprocesses, not kits, so there is no reading that
reconciles them. The baseline arrived in the rev-2 fold of round 1's wedge finding and AC6 was never
revisited. A builder who implements S4 reds AC6; a builder who satisfies AC6 has built the wedge the
rev-2 fold exists to prevent, and AC9's pre-existing-red arm then has no baseline to be red at.

**Edit:** rewrite AC6 — "**AC6** — Only touched kits run, twice each. In a fixture claiming three
kits where one moves rows, exactly TWO `[check].argv` subprocesses are observed — S4's baseline and
S4's after-pass over the one touched kit — and the tally names the other two kits as `not-run` with
zero subprocesses for them. The arm fails both against a draft that baselines every claimed kit (six
subprocesses, the whole-bar behaviour §3 refuses) and against one that skips the baseline (one
subprocess, the wedge AC9 exists to close)."

**H4 — `-11`: the fold's headline scope item has no acceptance criterion, no arm, and the arm count
is still rev-3's nine.**
S0c, new in the fold, calls itself "the sharpest thing in the unit": "`renamed` is EXEMPT from the
seed override at `:3016-3020` ... Without the exemption a seed row whose gov source gov RENAMED
classifies `t_state = \"absent\"` → `withdrawn` (`:2846`) → **rewritten to `current`** — the run
reports the row healthy while the source behind it no longer exists, which is a silent-green." The
hazard is real in source: the override is `if how == "seed" or how == "report-reseed": ... elif v not
in ("missing",): v = "current" if ...`, so without `renamed` beside `"missing"` the rewrite happens.
Nothing observes it. AC1–AC9 run on `engine` rows except AC4 (a withdrawn row), AC6 (a file count)
and AC7 (the refusal join); none names a `seed` row, and none puts a non-`table` role through the
write loop, which is S0b's `:3064` tuple edit. AC9 does not reach it — it asserts `patched` is absent
over an engine fixture, while the silent-green produces `current` on a seed row. Meanwhile §4 still
reads "(9 arms, the ninth being S11's and landing with `-9`)", §5 "nine `selftest.py` arms" and §7
"Adds nine arms", all set at rev-3. The build's standing rule is that a gate is not landed until its
failing case has been observed, and it is unmet on this unit's own headline item.

**Edit:** add two criteria and raise all three counts to eleven. "**AC10** — S0c. In a fixture where
gov renames the source behind a `seed` row between `base_commit` and `--to`, `update` prints
`renamed` for that row and the string `current` appears nowhere in its output. Observe RED first:
without the `:3016-3020` exemption the same row classifies `withdrawn` and the seed override rewrites
it to `current` while its gov source no longer exists." "**AC11** — S0b. In a fixture where gov
renames the source behind a `rendered` row, the write loop's reported-only line at `:3064` names
`renamed` for it, in addition to the `:3024` verdict line. Observe RED first: with `renamed` absent
from that tuple the row falls through to the bare `continue` and only the first line prints."

**H5 — `-12` S4 and `-9` AC9, written in the same fold, disagree about whether a staged-uncommitted
deletion refuses.**
`-12` S4 defines dirty as "differs index-versus-HEAD or worktree-versus-index — `git diff --cached`
and `git diff` over that path", then carves out: "A claimed path absent from BOTH the index and the
worktree is **not dirty**. There is nothing to compare ... Without this carve-out `-9` AC9 and AC10
can never go green." `-9` AC9, added in the same commit, says: "The deletion is COMMITTED in the
fixture on purpose: `-12` S4 refuses a run over a dirty claimed path ... an uncommitted deletion is
refused at `-12`'s step 2 and this AC could never go red." A `git rm` that is staged and not
committed leaves the path absent from index and worktree while `git diff --cached` still reports a
deletion against HEAD: the base predicate says dirty, the carve-out says not, and `-9` says refuse.
No AC in either unit covers that state, so nothing catches whichever reading a builder picks — and
the two readings differ by whether `update --write` silently restores a deletion the operator staged
deliberately, which is the exact class this build exists to prevent. `-12`'s stated justification is
false as well: once `-9`'s deletion is COMMITTED, the path is absent from index, worktree and HEAD,
both diffs are empty, the base predicate already yields not-dirty, and the carve-out buys AC9/AC10
nothing.

**Edit:** state the safe reading once in `-12` S4 — "A claimed path absent from both the index and
the worktree is dirty when HEAD still carries it: a STAGED deletion is an operator decision and the
run refuses, naming the path. It is NOT dirty when HEAD does not carry it either, which is the
committed deletion `-9` S11 restores and `-9` AC9 requires; that is the only state this carve-out
covers, and the reason is that there is nothing left to diff." Delete the "Without this carve-out
`-9` AC9 and AC10 can never go green" sentence. Add `-12` AC9: "A claimed path deleted with `git rm`
and NOT committed refuses by name; the same path once committed proceeds to the `missing` cell."

## Medium

**M1 — `-12` §4: the build's one ordering authority is out of order and incomplete.** Filed by five
lenses; merged here, because the fix is one table and a fixer must not half-apply it.
Under the heading "A `--write` run passes in this sequence and stops at the first refusal", the rows
now read 1, 2, 3, 4, **5**, **4b**, 6, 7, 8, 9. Row `4b` is `-7` S4, "refuse, whole run", printed
below row 5, which is `-13` S7's per-ROW in-loop skip. The two readings disagree materially: `-7` S2
takes its `ls-files -s -z` read in one batch in the preamble and `-7` §8 F2 puts it "into a dict
before the classification loop", so a whole-run refusal ordered after a per-row loop step emits
partial per-row output and then aborts — an operator-visible ordering nobody chose. The explanatory
paragraph was not updated either: it still names only "**Step 4 is in the PREAMBLE and step 5 is
inside the classification loop**" and "**steps 1–3 precede everything per-row**". Separately the
table claims to run "from the preamble to the write" while omitting `-14`'s two strictly pre-write
entries — S2's snapshot ("taken before the first byte moves, keyed on the ROW", the rollback's only
input) and S4's baseline ("once as a BASELINE before the first byte moves", what decides whether
step 9 may roll back at all) — so a builder implementing the order from this table alone reaches the
post-write check with nothing to compare against and nothing to restore from. `-12` rev-4 calls the
table "corrected and completed".

**Edit:** renumber 1..12 with no letter suffixes, so a label and a position can never disagree again:

| # | owner | what it decides | on failure |
|---|---|---|---|
| 1 | this unit, S1–S3 | is the target mid-operation? | refuse, whole run |
| 2 | this unit, S4–S5 | is any receipt-claimed path dirty, and can the lock be taken? | refuse, whole run |
| 3 | this unit, S7–S8 | is `--to` a descendant of the receipt's `gov_commit`, and reachable from a ref? | refuse, whole run |
| 4 | `-7` S9 | for a row carrying BOTH `commit` and `gov_oid`, do they agree? | refuse, whole run |
| 5 | `-7` S4 | is a claimed path present in the worktree and absent from the index? | refuse, whole run |
| 6 | `-13` S7 | does this ROW carry `evidence: "unattributed"` AND resolve to the `table` disposition? | print, count, skip the ROW |
| 7 | `-9` S1/S5 | which `carry` rung, if any, proves itself over the whole file? | no failure mode; it classifies |
| 8 | `-11` S2 | did gov rename this row's source between the two vintages? | verdict `renamed`; `-11`'s own two refusals |
| 9 | `-9` S6 | apply the proven rung to `base` and `theirs` before `three_way` | no failure mode; it feeds the merge |
| 10 | `-14` S2–S3 | snapshot every touched row's paths and its six identity fields | none; it is the rollback's only input |
| 11 | `-14` S4 | run each touched kit's `[check].argv` as a BASELINE | none; it decides whether step 12 may roll back |
| 12 | `-14` S4–S5 | re-run each touched kit's `[check].argv` AFTER the write | roll back from the recorded OIDs; `r.fail` |

Then amend the header sentence to "`-14`'s post-write verification is step 12 and is the only entry
AFTER bytes land; its snapshot and baseline are steps 10 and 11, whose relative order is free."
Amend the paragraph below to "**Steps 4 and 5 are in the PREAMBLE and step 6 is inside the
classification loop**" and "**steps 1–5 precede everything per-row**", and change its "the row is
skipped by name one step later" to "two steps later". Add one sentence to `-7` S4: "The predicate is
evaluated in the PREAMBLE, over the same batched `ls-files -s` read S2 takes, before any row is
classified — it is a whole-run refusal and must not depend on which rows the loop has already
reached."

**M2 — `-9` AC1's RED-first count is one row larger than the population its own §1 and §4 declare.**
AC1: "Observe RED first: at `9ddcc5c9` the returned dict has no `carry` key at all and all 32
non-identical rows classify with `o_state` as `differs`." §1 fixes the population — "of the 52 rows
whose commit resolves, 21 are byte-identical, 6 differ only in line endings, and 5 differ only by the
prefix relocation" — and §4's rung table sums 21 + 6 + 5 + 20 = 52. Non-identical is 31. The nearest
derivable 32 is 52 − 20, the rows matching SOME rung, which is not the population AC1 names. This is
the one arm whose job is to prove the ladder is absent at base, so an unreachable 32nd row is exactly
what a builder goes looking for; the figure has ridden rev-1 through rev-5 untouched while everything
around it was re-measured.

**Edit:** in `-9` AC1 replace "all 32 non-identical rows" with "all 31 non-identical rows — 52
resolvable rows less the 21 §4 records as `verbatim`, which is the same 6 + 5 + 20 that table sums".

**M3 — `-9` AC1 and AC2 run on a fixture no scope item creates, and §4 and §7 count one fixture.**
Both criteria require "a fixture receipt built from inCMS's 52 resolvable rows", and AC2 additionally
requires it to yield "exactly `13` directory pairs and `26` needles" and to drop `tools/memory-recall`
and `tools/workflows` by name. §2 owns no fixture item; §4's Files touched names exactly one — "a
non-default prefix, a deliberately ambiguous gov directory, a `relocate` row whose gov copy moved,
and a `relocate` row the target deleted" — and §7 says "Adds ten arms and one fixture". §4's
Inventory line describes how the design pass *reconstructed* the 52-row population from a live
external repo ("`.governance/kits.json` plus `.governance/install.index`" at inCMS `2cff5855`), which
is provenance, not a construction recipe, and nothing in this tree holds the result. Round 1 already
asked this unit to name its population; the fold named the vintage in §1 and §4 and never gave the
fixture an owner. Two further inconsistencies ride along: the vintage is named nowhere inside §6, and
AC2's 13 pairs and 26 needles were measured over §4's 86 source-resolving rows rather than over the
52 commit-resolving rows AC2 names as its fixture, so those two numbers may not reproduce over the
population the AC states.

**Edit:** add `-9` S13 — "the inCMS-derived fixture is COMMITTED, not reconstructed per run: a
checked-in receipt JSON of the 52 rows measured at inCMS `2cff5855` against gov `9ddcc5c9`, generated
once by a script recorded beside it, so AC1's and AC2's counts are re-runnable without either live
target." Correct §4's Files touched and §7 to "two fixtures". Name the vintage inside AC1 and AC2.
Re-derive AC2's 13 and 26 over the 52-row population and state which population they were measured
over, or move AC2 onto the 86-row one explicitly.

**M5 — `-13` AC11 can only be observed with `-12` landed, which three authorities exclude.**
AC11, added by the fold: "immediately after that `adopt --write`, `govkit.py update --to <an older
sha> --write` REFUSES by `-12` S7, naming both shas. Observe RED first: with `gov_commit` absent,
`-12` S7 skips its own check by its own words..." Both arms are assertions about `-12` S7's guard,
and `-12` is not in this unit's dependency set: §3 states it as "`adopt` needs `-1` (destinations),
`-7` (two identities), `-9` (the rungs) and `-10` (role `forked`) beneath it", §8 F3 ratifies the
same four, and the README's `deps` cell reads `1, 7, 9, 10` under the rule "Each unit's §3 land-alone
line is the authority". As ratified, `-13` may land with `-12` absent and AC11 is then unobservable
in both directions. The README's numbered order happens to put `-12` at step 2, which hides it. The
corpus already treats AC-observability as a recordable landing dependency: `-7` §3 says "Land-alone:
no, and `-2` lands first" for exactly this reason, and `-14` F3 does the same for `-11`.

**Edit:** add `-12` to `-13` §3's land-alone bullet and to §8 F3's resolution line ("lands after
`-1`, `-7`, `-9`, `-10`, and after `-12`, whose S7 vintage guard AC11 observes"), and change the
README's `deps` cell for `-13` to `1, 7, 9, 10, 12`. If the dependency is unwanted, restate AC11
against the receipt file alone — assert `gov_commit` equals the resolved `--to`, and that a hand-run
`merge-base --is-ancestor` over the two shas returns non-zero — and move the refusal arm into `-12`'s
own criteria.

**M6 — `-13` S7 and `-7` S9 equate the unlanded CHANNEL with `UNLANDED_REASON`'s key set, and that
sentence is what hid B2.**
Both read "that is `UNLANDED_REASON`'s population at `:236`, meaning `project-owned`, `generated` and
`rendered`". The three-role list is right about what `apply` writes and wrong about the dict:
`UNLANDED_REASON` (`:236-240`) has four keys — the fourth is `merged` — and `-10` S3 adds a fifth,
`forked`. `apply` gets three only because it `continue`s past merged entries at `:2427-2428` and
writes the real merged row at `:2417` instead. `resolve_entry`'s `unlanded` list, which `-13` S2
takes whole, still carries them. So the sentence tells `-13`'s builder that the channel yields three
harmless roles when it yields four, one of which needs `apply`'s special case — which is B2, arriving
through a gloss.

**Edit:** in `-13` S7 and `-7` S9, replace the clause with "those are the rows `apply` writes at
`:2440` — `project-owned`, `generated` and `rendered`. `UNLANDED_REASON` (`:236`) carries a fourth
key, `merged`, and `resolve_entry`'s `unlanded` list carries merged entries too; `apply` skips them
at `:2427-2428` and writes the real merged row at `:2417` instead. `-10` S3 adds a fifth key,
`forked`." Carry the same `continue` into `-13` S2 as part of B2's edit.

## Low

**L1 — `-13`'s three arm counts were not raised when the fold added AC10, AC11 and S10's demand.**
§4 reads "`tools/govkit/selftest.py` (11 arms)", §5 "eleven `selftest.py` arms", §7 "Adds eleven arms
and the two standing predicates" — all set when §6 ended at AC9. The fold added AC10 (the envelope's
key set), AC11 (the envelope is LIVE) and S10's third demand ("S9's arms assert that a receipt
without them classifies without refusal"), and moved none of the three. Every sibling moves this
number in the fold that changes it. The figure is soft here — §4 labels itself an estimate and S9
counts arms per BRANCH rather than per criterion — so the count is the fixer's to re-derive rather
than mine to assert. **Edit:** raise all three to fourteen and enumerate the additions in §5 the way
`-10` §5 does: "...plus AC10's envelope key-set arm, AC11's live-envelope arm — an `adopt --write`
followed by a backwards `update --to` that must refuse by `-12` S7 — and S10's absent-optional-keys
arm, asserting a receipt carrying none of `orders`, `baseline`, `after`, `hook_block`, `gate_runner`
classifies without refusal." Log the raise in the §9 entry beside the S10 note, and re-derive the
figure against the enumerated branches when the arms are written.

**L3 — `-11` S0c's incident-comment citation is off by four lines.** S0c reads "which is a
silent-green of exactly the kind the comment at `:3054-3058` records a measured incident for".
`:3053-3055` is the tail of the escapes-the-tree `r.fail` message and `:3056` its `continue`; the
incident comment ("THE ROLE DECIDES, not the verdict...") spans `:3058-3062`, with the guard at
`:3063`. Every other citation the same fold added is exact, so this is a slip, and this corpus's
practice is that a builder opens the cited lines. **Edit:** change `:3054-3058` to `:3058-3062`.

---

## What the fold got right — do not re-litigate

The skeptic refuted eleven findings this round, and several were re-files of settled questions. The
README's architecture paragraph is already scoped correctly ("skipped before any WRITING disposition
is consulted") and does not state the unconditional skip. `-8`'s merged rows keep `_sha(merged)` by a
ratified Alternatives bullet, and its three-column table is deliberately scoped to `gov_oid` and
`oid`. `-3` S2 and AC4 are a constraint and its no-regression arm, not a task already done. `-4`
AC3's hand-placed descriptor in a local checkout is by design, matching AC2's live-NicoCares shape.
`-13` §8 F2 (`--re-adopt` preserves nothing) and F4 (`--pin` overrides no refusal) are both answered
questions with their reasoning recorded. `evidence` needs no post-write lifecycle while
`"unattributed"` is its only verb-read value, because an unattributed row is never written. `-12`
S4's "DIRTY IS DEFINED HERE, once" is scoped to the three criteria in two units it names, and does
not overturn `-13` F1's index-only ruling for `adopt`. And `-13` §9's newest-first revision order is
the corpus convention, not a defect — seven of the twelve multi-rev specs are strictly descending.

## What remains unverified

Nothing was executed. Every finding above is a spec read plus a source read at `9ddcc5c9`; no fixture
was built, no arm run, no verb invoked. Specifically:

- B3's wedge is mechanism-verified end to end in source, including the persistence seam at `:3115`,
  but no rename was landed, red and rolled back to observe the refusal on the following run.
- B2's `cmd_check` breakage is read, not reproduced: `row["block_id"]` at `:1570` is unguarded and
  `marker_pair(None, ...)` refuses at `:1706`, but no adopted receipt with a merged rule was built.
- H2's chosen answer — that `sha256` holds the TARGET's bytes at receipt-write time — is inferred
  from `cmd_apply` (`:2459`), `-8`'s ratified bullet and `cmd_check`'s integrity loop. It is a
  decision the owner should ratify in `-13` §8, not a fact I measured.
- The inCMS populations were not re-measured. M2 is arithmetic internal to `-9`; M3's 13 pairs and 26
  needles were not re-derived over either candidate population, and I cannot say which one they
  reproduce over.
- L1's "fourteen" is not derivable from `-13` as written, because S9 counts arms per branch rather
  than per criterion. The fixer must re-derive it against the enumerated branches.
- The adopter-side specs under the other repo's slug were not read this round, so cross-repo
  consistency of the descriptor prerequisite H6 and `-4` §3 both depend on is unchecked here.
- The fold's line-length pass was spot-checked at the sites findings pointed to, not diffed
  exhaustively across all 15 specs; L6 is the only rewrap regression I looked for and found.
