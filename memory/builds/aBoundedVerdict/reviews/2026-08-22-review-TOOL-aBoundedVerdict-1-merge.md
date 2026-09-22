**Serves:** diff-review TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-22 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 TOOL-aShardedFloor-4

# Review — the cross-build integration of dUnstalledConvoy into aBoundedVerdict

**Range:** `76c010c7...5472dde9` — the merge commit `397a5a64` ("two builds, one kit", 25 files / 40 hunks)
plus the floor re-measurement `5472dde9` that follows it. Parents: `76c010c7` (this branch,
aBoundedVerdict) and `d163804c` (origin/main, carrying dUnstalledConvoy and the aShardedFloor closeout).

**Round:** 1. First review of the integration.

**Kind:** INTEGRATION REVIEW. Neither build was re-reviewed. aBoundedVerdict had four adversarial rounds
(33 / 15 / 15 confirmed) and dUnstalledConvoy a closing review of 16 plus a re-review of 10; those
verdicts stand and nothing here re-litigates them. The only question asked of every hunk is whether the
RESOLUTION is correct and coherent — what the merge creates, breaks, or leaves saying two things.

**Measured on:** node c, primary tree `C:/projects/coding-governance` at `5472dde9`, clean.

## Verdict: BLOCKED

Four merge-bar legs are RED on the merged tree, right now, and none of them is red on either parent.

**Shape:** raw 33 · confirmed 33 · refuted 0 · unverified 0 · precision 1.00. The 33 fold to **14 distinct
defects** after collapsing cross-lens duplicates; the fold is recorded in the `folds` line of each finding.
Severity here is cluster-level: **4 blockers · 2 highs · 8 mediums**. The raw label tally was 7 / 4 / 19 / 3,
which differs because duplicates of one defect were labelled differently by different lenses, and because
I raised one high (F4) to blocker after measuring that it reds a registered leg. One further defect (N1)
is a reviewer addendum found while verifying decision (1) — it is not part of the 33 and not counted in
the shape.

### Merge-bar status, measured

| Leg | Result | Cause |
|---|---|---|
| `bash tools/unattended/check-unattended.sh` | **RED**, exit 1 | F1 — one failure, `check 22 … documented but in no example: LANDED` |
| `bash tools/check-dead-paths.sh --check` | **RED**, exit 1 | F2 — six unwaived citations |
| `bash tools/memory-tree/check-memory-hygiene.sh` | **RED**, exit 1 | F3 — `check 22 … numbers no criterion: TOOL-aBoundedVerdict-22` |
| `tools/unattended/check-unattended.test.sh` (leg "unattended gate selftest") | **RED** | F4 — the documentation join, reproduced arm-verbatim; F1 also reds 14 of its arms |
| everything else | not run | see "What I did not check" |

## The seven resolution decisions, audited

| # | Decision | Verdict |
|---|---|---|
| 1 | ADV_NAME grafted onto the bounded capture | **Correct, ungraded.** The parse reads `$adv_f` after `_rc1=0`, gated identically to `ADV_HEAD`; it parses the same bytes (see N1 for the one wrinkle). No unbounded remote call survives: the leg's only two remote reads are `observe_remote` at `check-unattended.sh:511` and `:523`, and the source-level arm at `unattended.test.sh:2584-2609` greps BOTH the driver and the leg for an `ls-remote` outside the helper. What nothing does is prove the parse RESOLVES — F14. |
| 2 | `GIT()` collapsed into the lib, pins moved beside it | **Half done.** One definition, driver copy deleted, driver's bounded helper expands the constants (`unattended.sh:134`, `:142`). The gate leg's bounded helper still spells the pins as literals — F12 — which falsifies the library's own comment. |
| 3 | Fixture conf taken as a union | **Correct, and the class hunt is clean at key level.** I diffed the KEY SETS of `.memory-tree.conf`, `.unattended.conf`, `.unattended.conf.example` and the three selftest fixtures against BOTH parents: nothing a parent declared is missing from the merge. The class does recur twice, in populations that are not `KEY=` lists and so were invisible to that probe — the flag denylist (F4) and the acceptance-ledger grandfather list (F3). That is the lesson worth keeping: the union hunt found nothing because it was pointed at the shape that had already been fixed. |
| 4 | Floors re-measured at 622/205/430 → 500/165/346 | **Numbers right, record wrong.** The prologue identity `205 + 430 − 622 = 13` holds and is the only evidence no arm block straddles the split. The comment block that is supposed to BE that documented manual check now gives three different measurements and prices a constant that no longer exists — F13. |
| 5 | BUILD-METHOD budget raised to ≤24 KB / ≤310 | **Figures agree, prose broken.** Both carriers measure 309 lines (23732 B rendered, 23743 B template) against the declared pair, and no other carrier states the old figure as current — `tools/memory-tree/README.md:139` correctly points at the method instead of restating it. The paragraph itself was spliced mid-sentence — F11. |
| 6 | M12's double statement closed by deleting the README section | **Correct and complete.** Every surviving `M12` reference points at `BUILD-METHOD.md:282`, its real home (`SKILL.template.md:40,41,182`, the method's own `:154-155`). Nothing points at the deleted README section. |
| 7 | Verb lists unioned across the driver's three strings, the protocol and the Skill | **Not coherent.** The usage line and the refusal name 14 verbs; the header names 12 and names `--abort` twice with contradictory signatures (F8). The protocol lists `--abort` twice, the first copy stale (F9). The leg's dispatch-documentation join still grades — but its population gained four flags and reds on all four (F4), and its floor is now slack by four. |

---

# Findings

## F1 — BLOCKER — the unattended gate leg is RED: a phase name read as a conf key

`memory/guides/UNATTENDED-PROTOCOL.md:457` · `tools/unattended/PROTOCOL.template.md:457` (identical byte) ·
extractor at `tools/unattended/check-unattended.sh:1030` · folds: 1, 17, 25

Main's new `LANDED_ANCHOR_CUTOFF` row spells a PHASE name in backticks — "the date from which a `LANDED`
record must name its anchor kind". This branch's check 22 scrapes every backticked `[A-Z_]+` token out of
section 8 and joins the result against `.unattended.conf.example`. `LANDED` is a phase, not a key, so it
lands in the phantom set.

Measured: `bash tools/unattended/check-unattended.sh` exits 1 with exactly one failure —
`documented but in no example: LANDED`. Re-ran the join by hand: phantom `{LANDED}`, undocumented empty.
Neither parent reds: `76c010c7` has the join and no such token, `d163804c` has the token and no join. The
two files are byte-identical and check 10 compares them, so any fix touches both. It also reds 14 arms of
the leg's own selftest, whose fixture copies `PROTOCOL.template.md` in as the live doc.

**Fix.** Root-cause it in the extractor, which its own comment already claims to be scoped to the key
column: read the first table cell rather than the whole row.

```sh
doc_keys=$(printf '%s\n' "$sec8" | awk -F'|' 'NF>2 {print $2}' | grep -oE '`[A-Z_]+`' | tr -d '`' | sort -u)
```

I ran that substitution against the shipped pair: phantom becomes empty, undocumented stays empty, and the
`·`-joined `KEEPALIVE_CREATE`/`KEEPALIVE_DELETE` row still yields both keys. Unbackticking `LANDED` in both
carriers also clears it, but leaves the next prose token free to re-break the leg.

**Left-shift gate.** Add a fixture row to the leg's selftest whose prose backticks a non-key ALL-CAPS token
and assert check 22 stays silent. Stage the break, confirm RED with the current extractor, then land the
first-cell read.

## F2 — BLOCKER — `check-dead-paths.sh` is RED: six waiver rows re-stamped in the wrong direction

`tools/dead-path-waivers.txt:22-27` · folds: 10, 18

All six line-keyed memory-tree waiver rows now read `286 / 548 / 1109 / 1218 / 1223 / 1279` while both
parents inserted lines ABOVE those carriers. Measured: `bash tools/check-dead-paths.sh --check` exits 1 and
names the six real carriers — `check-memory-hygiene.sh:288`, `:550`, `check-memory-hygiene.test.sh:1175`,
`:1284`, `:1289`, `:1345`. The branch side already carried `288/550` correctly and the merge took main's
older stamps, so two rows regressed to values that were right on neither parent. The file's own header
names this exact hazard: a merge landing edits above a carrier moves it and the row goes stale.

**Fix.** Re-stamp rows 22-27 to `288`, `550`, `1175`, `1284`, `1289`, `1345`. Text and count unchanged.
Confirm with `bash tools/check-dead-paths.sh --list`, which prints `waived` per row when the pin lands.

**Left-shift gate.** Key each row by a stable quoted fragment of the carrier LINE and treat the number as a
hint the checker re-derives, so a row cannot be stranded by an insertion above it. Failing that, put
`bash tools/check-dead-paths.sh --check` in the post-merge diff-scoped gate that §1 already requires — this
class only ever fires on a merge.

## F3 — BLOCKER — the memory-hygiene leg is RED: main's acceptance ledger meets this branch's records

`memory/builds/aBoundedVerdict/spec/2026-08-21-spec-TOOL-aBoundedVerdict-22.md:57` ·
`.memory-tree.conf:337` · folds: 3, 11, 26

Measured: `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 with one failure —
`a CLOSED Tier-2 spec carries an acceptance-criteria section that numbers no criterion: TOOL-aBoundedVerdict-22`.
Every predicate fires: filename date `2026-08-21` sorts after `ACCEPTANCE_LEDGER_CUTOFF="2026-08-20"`, the
header is `CLOSED · rev-1 · 2026-08-21 · node c · Tier-2`, `## 6. Acceptance criteria` matches the heading
selector, section 6 is six unlabelled bullets, and the id is absent from `ACCEPTANCE_LEDGER_GRANDFATHER`.
The merge imported main's cutoff and grandfather list verbatim — the list names only main's own post-cutoff
closures (aMeteredTurnstile, aShardedFloor, dScriptedRepeat, dSettledRoster) — and never asked whether THIS
branch had post-cutoff closures. It had exactly one.

**Fix.** Label the six bullets `AC1`…`AC6` and write the matching `**Evidences:**` block in a journal-kind
record under `memory/builds/aBoundedVerdict/build/`; or, if back-filling is out of scope for this landing,
add `TOOL-aBoundedVerdict-22` to `ACCEPTANCE_LEDGER_GRANDFATHER` with its reason inline, the way the merge
already did for main's units. Re-run the leg afterwards — the `algap` arm may name more once labels exist.

**Left-shift gate.** Move the label requirement to spec CLOSE rather than to merge: assert numbered AC
labels when a Tier-2 spec's status header flips to `CLOSED`, so a spec cannot become CLOSED unlabelled and a
future cutoff can never arrive to a corpus it has not graded.

## F4 — BLOCKER — the flag denylist was not unioned, so four flags entered the verb population

`tools/unattended/check-unattended.test.sh:317` (denylist), `:327` (floor) · folds: 2
*Labelled high by its lens; raised here because it reds a registered leg.*

Main added `--pass`, `--writes`, `--act` and `--successor`. The denylist that removes flags from the derived
verb population still holds this branch's ten names. Reproduced by running the arm's own code verbatim: the
population reads **18** names, and the three-surface join emits exactly

```
FAIL a dispatched verb is absent from a surface an agent reads: --act(refusal) --pass(refusal) --successor(refusal) --writes(refusal)
```

Worse than the red: the shrink-only floor is `-ge 12` against a population of 18 while the kit dispatches
**14** real verbs, so two verbs could stop being dispatched and the floor would still pass. The pin that
exists to stop a verb going undocumented is slack by four. The tempting repair — adding the four flags to
the refusal string — would make the driver tell an operator that `--writes` is a verb.

**Fix.** Extend `_denied` to `'--keepalive-id --item --value --override --waive --reason --code --subject
--verdict --blockers --pass --writes --act --successor'` and raise the floor from 12 to 14. The
stale-exemption loop directly below already proves each denied name is still a case arm, so the additions
cannot rot silently.

**Left-shift gate.** Derive the denylist instead of typing it: classify a case arm as a FLAG when its body
assigns and does not dispatch (no `verb_*` call, no `exit`), and assert the derived flag set equals the
denylist. Then a new flag arriving by merge cannot be left behind by a list nobody remembered to union.

## F5 — HIGH — hygiene check id 22 was minted twice; the ratchet that should catch it is vacuous

`tools/memory-tree/check-memory-hygiene.sh:651` and `:1165-1167` · folds: 12, 19

Both builds minted hygiene check 22 independently and the merge kept both: `fail 22` at `:651` is this
branch's review-verdict vocabulary, `fail 22` at `:1165-1167` is main's acceptance ledger. Twenty-three
distinct checks now emit twenty-two ids, and `pop_guard 22` appears twice (`:621`, `:1124`).

Nothing can see it. The derived-count arm at `check-memory-hygiene.test.sh:1519-1530` dedupes with
`sort -n -u`, computes 22, matches `tools/memory-tree/README.md:18`'s "22 checks" and passes — the arm
written because that figure had already been wrong three times is now structurally blind to being wrong a
fourth. `HYGIENE check 22 FAILED` is ambiguous between two unrelated rules with different remedies;
`memory/HYGIENE.md:243` numbers only the review-verdict one and the ledger merged in as unnumbered prose;
`memory/map/features/memory-tree-hygiene.md:31` also still says 22. `check-arms.py` cannot help — it signs
branches by fail MESSAGE, not by id.

**Fix.** Renumber the later arrival to 23: the three `fail 22` calls at `:1165-1167`, the `pop_guard 22` at
`:1124` and the block header comment. Add the numbered entry to `HYGIENE.template.md` and re-render
`memory/HYGIENE.md`; bump the counts in the kit README and the map dossier; update the four message
assertions at `check-memory-hygiene.test.sh:552-560`.

**Left-shift gate.** Alongside `_hy_derived`, assert that the count of distinct `fail <n>` SITES opening a
check block equals the count of distinct ids. Two blocks sharing an id then reds instead of collapsing.
Same arm belongs in the unattended selftest, where F6 is the same defect.

## F6 — MEDIUM — unattended check id 22 was also minted twice, and four arms now grade the wrong check

`tools/unattended/check-unattended.sh:1023`, `:1048` (conf-key join) and `:1431`, `:1437`, `:1445`
(rescope roster) · folds: 28

Same collision, other kit. `UNATTENDED check 22 FAILED` no longer identifies which check fired, and the
remedies differ completely. The four `miss "$(run)" "check 22 FAILED"` arms at
`check-unattended.test.sh:1735`, `:1743`, `:1762`, `:1770` were written to prove the rescope check stays
silent and now also grade the key-table check — today they red for F1's reason, not the one they were
written for. The header's own derivation returns 23 ids for 24 distinct checks.

**Fix.** Renumber main's rescope-roster check to 24 at `:1431`, `:1437`, `:1445` and in its block comment;
update the four arm literals and the block comment at `check-unattended.test.sh:1699`.

**Left-shift gate.** The distinct-sites-equals-distinct-ids arm from F5, ported here.

## F7 — HIGH — the `LANDER_MARKER` gate runs before anchor selection, so the local-landing fallback is dead

`tools/unattended/unattended.sh:1643-1666` (marker block), `:1696-1717` (arm split) · folds: 27

`verb_landed` evaluates the marker block and returns 1 on a missing or non-matching marker BEFORE
`observe_anchor` and before the remote/local split. `tools/push-main.sh` writes the marker only inside
`if [ "$rc" -eq 0 ]`, after a successful push (`:71-104`). On the exact state main's local arm exists for —
merged into local `main`, push did not land HEAD — the marker cannot exist, so `fail 34` fires first. A
stale marker from an earlier push reds too, since the check greps for the current HEAD sha.

This repo declares `LANDER_MARKER="unattended-landed"` (`.unattended.conf:129`) and
`ANCHOR_SCOPE="published"` (`:89`) — the mode where `branch-ref` is written and the local arm is meaningful
— so the fallback is dead HERE, and a run in that state must abort. That is the deadlock
TOOL-dUnstalledConvoy-1 was built to remove. `.claude/skills/unattended/SKILL.md:365` still documents the
fallback as available. Nothing covers the pair: the local-arm fixture (`unattended.test.sh:1995-2010`)
declares no marker, and the marker fixtures (`:3101-3130`) never reach the local arm.

**Fix.** Move the marker check after the anchor arms and require it only when `akind=remote`, comparing it
against the witness the taken arm validated rather than against HEAD. Keep today's equality semantics on the
remote arm.

**Left-shift gate.** One driver arm holding both features at once: `LANDER_MARKER` declared, no marker file,
`branch-ref` recorded, work merged into local `main` — expect `phase LANDED · anchor LOCAL`, not `fail 34`.
Every fixture in the suite today varies one of those two and nothing varies both.

## F8 — MEDIUM — the driver's header synopsis documents an `--abort` the driver refuses

`tools/unattended/unattended.sh:15` and `:17` · folds: 4, 14, 20, 31

The header hunk took both sides. Line 15 is main's `--abort <slug> --reason <text>`; line 17 is this
branch's, with `--code <halt-code>`. `--code` is mandatory — `:1814` is
`fail 33 "--abort requires --code…"` — so line 15 documents an invocation that always exits 33, sitting
directly above the one that works. The union also skipped `--attest` and `--version`: the header names 12
verbs where the usage line (`:3063`) and the refusal (`:3055`) each name 14, while the S10 comment at
`:3058` asserts all three spell THE SAME SET.

Nothing catches it. The S10 arm at `unattended.test.sh:1578-1583` asserts `grep -c … -ge 1` per verb, which
two lines satisfy as easily as one, and its hardcoded list omits `--review`, `--attest` and `--version`.

**Fix.** Delete line 15. Add header rows for `--attest` and `--version`.

**Left-shift gate.** Tighten the S10 arm to `-eq 1` per verb on the header grep, and derive its verb list
from the refusal string rather than typing it, so the comment's claim becomes a measurement.

## F9 — MEDIUM — the protocol lists `--abort` twice and answers its own question two ways

`memory/guides/UNATTENDED-PROTOCOL.md:389` and `:420` · `tools/unattended/PROTOCOL.template.md`, identical
lines · folds: 5, 32

Section 7 carries two `--abort` bullets. The first (main's) requires "a recorded reason and both
agent-attested items"; the second (this branch's) requires "a recorded reason, a HALT CODE from the
effective vocabulary, and both agent-attested items". Item 12 of the same document says the halt code is
written by `--abort` and by nothing else. A reader working down the list hits the stale contract first and
builds a call the driver refuses. `diff` of the guide against the template is empty, so check 10 is green
and every adopter inherits the contradiction. AGENTS.md declares this document BINDING.

**Fix.** Delete lines 389-391 in both carriers, keep the halt-code bullet at 420-425, re-render so the pair
stays byte-identical.

**Left-shift gate.** An arm asserting each verb appears exactly once as a `- \`--verb\`` bullet in §7, and
that the §7 bullet set equals the driver's refusal set. Check 10 proves the two copies AGREE; nothing proves
either is coherent.

## F10 — MEDIUM — the leg's header states two check counts and a stale range

`tools/unattended/check-unattended.sh:2` and `:3-6` · folds: 6, 21, 29

Both parents' opening sentences survived, adjacent, sharing the identical stem. Line 2 says "TWENTY-THREE
checks over the tree." Line 3 says "Its check ids run 1..22; the count is NOT retyped in prose anywhere,
because it has now been wrong twice". The file's own prescribed derivation returns **1..23**, so the range
is stale, and the retained line 2 breaks the rule printed on the line below it — §7's "NO count of a derived
population is written in prose", in the file that states it.

**Fix.** Delete line 2 and drop the `1..22` clause from line 3, leaving only the derivation instruction.

**Left-shift gate.** Port the derived-count arm from `check-memory-hygiene.test.sh:1519-1530` into
`check-unattended.test.sh` — round 3 asked for it and it was never added — and have it also assert the
header contains no spelled-out or numeric count.

## F11 — MEDIUM — BUILD-METHOD's budget paragraph was spliced mid-sentence, in both carriers

`memory/guides/BUILD-METHOD.md:10` and `:15` · `tools/memory-tree/BUILD-METHOD.template.md:10` and `:15` ·
folds: 7, 13, 22, 30

Line 10 reads "…because the figure is a stated constraint of a It rose again to ≤24 KB / ≤310 on
2026-08-21, also an owner call:" and the severed tail — "governance carrier and M3's veto 2 makes changing
one an owner turn rather than an agent's." — dangles four lines below as its own paragraph. M7 re-reads this
file WHOLE at every pass boundary, so every future build pays for it, and the mangled sentence is the one
that says who may move the budget. Both carriers are byte-identical here, so the kit/dogfood parity leg is
green over the corruption.

**Fix.** Close the original sentence first, then start the 2026-08-21 rise as its own sentence, and delete
the orphan. Apply the identical edit to both files. There is no room to fix this by adding lines: 309 of 310
used, 23732 B of 24576.

**Left-shift gate.** A cheap one that would have caught the class: read the declared
`**Budget: ≤N KB, ≤M lines**` line and measure the file against it, in both carriers. It does not read
grammar, but it forces a human back to the paragraph on every change to it. The grammar half stays a
documented manual check — §1's "diff the merge against BOTH parents" is the check, and it is the one this
merge skipped on prose hunks.

## F12 — MEDIUM — the named GIT pins reached the driver and not the gate leg

`tools/unattended/check-unattended.sh:484` and `:492` · `tools/unattended/lib-unattended.sh:19-27` ·
`tools/unattended/unattended.test.sh:1723` · folds: 9, 15, 23, 33

The library says the pins are NAMED "so `GIT` and the bounded remote observation cannot drift apart", and
that they live there "because the driver and the gate leg both source this file". That is now true of the
driver (`unattended.sh:134`, `:142`) and false of the leg, whose `observe_remote` still spells
`-c core.useReplaceRefs=false -c advice.graftFileDeprecated=false` literally while sourcing the library at
`:53`. Before the merge the leg's own `GIT()` carried the same literals one screen away, so co-location kept
them honest; the merge removed the co-location and left the literals. Nothing grades it — the counting arm
reads `$SCRIPT`, which is the driver. The suite DOES grade the leg's helper for transport options
(`unattended.test.sh:2622`), which shows this is an omission rather than a scope decision.

Values agree today, so nothing misbehaves. The defect is the second unguarded spelling of a rule the
constants were introduced to make single.

**Fix.** Replace both literal pairs with `-c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV"`.

**Left-shift gate.** Widen the arm at `:1723` to require the expanded form in `$HERE/check-unattended.sh` as
well. Then stage a pin-VALUE change and confirm the widened arm goes RED before landing it — a pin arm
nobody has seen fail is an assertion about nothing.

## F13 — MEDIUM — the floor comment block gives three answers to the one question no gate can ask

`tools/unattended/unattended.test.sh:3586-3648` · folds: 8, 24

The block took both sides' measurement notes and now states three mutually exclusive triples, all framed as
the merged tree: `519/205/327` "unchanged by this merge" (`:3605`), `520/205/328` (`:3616`), and
`622/205/430` (`:3624`) — not even in chronological order. Only the last reconciles with the constants in
force (`FLOOR_ASSERTIONS=500`, `FLOOR_SHARD_1=165`, `FLOOR_SHARD_2=346`). The ratio paragraph appears twice
with different arithmetic and both copies price a `338` floor that no longer exists.

This is not cosmetic. The block's own line 3638 declares itself the sole documentation of a manual check no
static predicate over the floors can perform — the prologue identity `n(shard1) + n(shard2) − n(unsharded) =
13`, which is the only evidence that no arm block straddles the shard split. A documented manual check whose
documentation gives three baselines cannot be performed.

**Fix.** Collapse to one measurement paragraph naming `622 / 205 / 430`, the identity `205 + 430 − 622 = 13`
and the single ratio actually applied (0.805 → 500 / 165 / 346). Delete the two superseded paragraphs and
the duplicate ratio note; the commit messages already record them.

**Left-shift gate.** Stop documenting the identity and compute it: have the three suites emit their executed
counts in a parseable line and assert `shard1 + shard2 − unsharded == PROLOGUE_ARMS`. It is a runtime
comparison across three runs, not a static predicate over the constants, which is exactly why the comment
concluded no gate could do it.

## F14 — MEDIUM — the re-grafted ADV_NAME parse is ungraded: the arms pass whether it resolves or is empty

`tools/unattended/check-unattended.sh:522` (assignment), `:807` (sole reader) ·
`tools/unattended/check-unattended.test.sh:1996` and `:2005` · folds: 16

`ADV_NAME` is assigned once and read at exactly one place, inside the `ak = local` branch. With it set, the
branch takes the silent `refs/heads/$ADV_NAME` arm; with it empty, it falls through to the `$b`-ancestry
elif (also silent) or to `report()`, which prints nothing unless `GOV_UNATTENDED_REPORT=1`. Neither path
emits check 15's "not an ancestor of the anchor" text, so the positive arm's `miss` passes on both, and the
skip arm's `hit` is produced on the empty path too. Verified by forcing `ADV_NAME=""` in a mutant: output
was byte-identical to the baseline through the portion that completed.

The merge changed this parse's data source from a fresh command substitution to the bounded capture file —
the single most consequential rewrite in the range — and nothing in the suite distinguishes the working
implementation from a broken one.

**Fix.** Nothing to fix in the code; the parse is correct.

**Left-shift gate.** Run the positive local-anchor arm under `GOV_UNATTENDED_REPORT=1` and `miss` the
"a local-anchored LANDED names a witness this clone does not carry on its own default branch" skip line, so
an empty or mis-parsed `ADV_NAME` reds. Add a control fixture whose remote HEAD points at a default branch
NOT named `main`, so the arm proves the value came from the advertisement rather than from a coincidence.

---

## N1 — LOW — reviewer addendum, not part of the 33: the grafted awk spells two control bytes raw

`tools/unattended/check-unattended.sh:522`

Found while verifying decision (1). Main's original (`d163804c:270`) reads
`awk -F'\t' '{ sub(/\r$/,"",$2) } …'`. The grafted line carries a **literal TAB** as the field separator and
a **literal CR** inside the regex — confirmed with `cat -A`, which prints `-F'^I'` and `sub(/^M$/,…)`. The
line directly above it (`ADV_HEAD`, `:512`) keeps the escaped spelling.

Behaviour is identical today: `/<CR>$/` and `/\r$/` are the same regex and `-F'<TAB>'` the same separator.
The hazard is that a raw CR now lives in a tracked `.sh` file this repo pins to LF, invisible to every
text-mode read, in a file whose §11 rule is to verify the staged BYTES. Any trailing-CR cleanup turns
`sub(/<CR>$/,…)` into `sub(/$/,…)` — a silent no-op that deletes the CR strip main deliberately wrote — and
any tab-expanding pass turns `-F'<TAB>'` into an empty separator. Two adjacent lines now spell the same two
bytes two different ways, and one of the two spellings cannot be seen.

**Fix.** Rewrite the grafted line with the escaped `\t` / `\r` spelling its neighbour uses.

**Left-shift gate.** A byte-level scan for raw CR and raw TAB inside tracked `.sh` sources, sibling to the
existing "line length" leg. The repo mandates byte verification in prose and gates it nowhere.

---

## The three shapes behind fourteen defects

**Both sides taken whole where only one could be.** F8, F9, F10, F13 — a header, a bullet list, a comment
block and a synopsis, each now stating two things. Every one of them is a surface a human reads and no gate
parses, which is why they survived a merge that resolved 40 hunks of code correctly.

**A new gate meeting the other build's records for the first time.** F3 is the pure case: main's check was
correct, this branch's spec was acceptable under the rules it was written against, and the merge is where
they meet. F1 and F4 are the same shape with the populations reversed — this branch's checker meeting main's
new prose, and this branch's exemption list meeting main's new flags. This class cannot be found by reading
either side's diff; only by running each side's gates against the other side's tree, which is the cheap
thing that was not done.

**Two independent mints of one id.** F5 and F6, in two kits, in the same merge — and in both, the ratchet
that exists to catch an undocumented check dedupes ids and so cannot see it.

## What I did not check

- The full bar. `bash tools/run-gates/run-gates.sh` was not run; on this node it costs ~873 s of wall clock
  and four legs are already known RED. The four in the status table were run individually
  (`check-memory-hygiene.sh` completed once and is quoted verbatim; the F4 arm was reproduced arm-verbatim
  rather than by a full selftest run, which exceeds ten minutes here).
- Either build's own correctness. Out of scope by construction, per the round-4 and dUnstalledConvoy
  closing reviews.
- Prose in the dUnstalledConvoy build records and specs — the diff carries ~4000 lines of them and this
  review scoped to carriers the two builds SHARE.
- `TOOL-dUnstalledConvoy-13` and `-14` appear in the range as records-only ids with no spec, so they are
  absent from the Serves line above rather than overlooked; check 21 refuses an id no spec defines.

## Landing order

1. F1, F2, F3, F4 — the four RED legs. F1 and F2 are one edit each. F3 needs an owner call between
   back-filling and grandfathering. F4 is two edits in one arm.
2. F5, F6 — renumber both id collisions before anything else lands on either engine, because every message
   assertion in both suites keys off the id.
3. F7 — the only finding that changes runtime behaviour on a path an unattended run actually takes.
4. F8-F14, N1 — carriers and coverage. F14 and N1 are both about the same hunk and should land together.
