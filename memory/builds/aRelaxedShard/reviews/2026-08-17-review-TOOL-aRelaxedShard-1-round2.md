## Verdict: CLEAN WITH FIXES

*Review shape: raw 43, confirmed 29, refuted 14, unverified 0, precision 0.67, lenses 3/3, verify
batches 5. Round 2 of the M4 audit over `spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md`, scoped to what
rev-4 and rev-5 CHANGED — the ratified retirement of the row line bound and the second conf key
`DOSSIER_CAP_BYTES` with its three-class cap block — read against this worktree at the spec's declared
base `43eb6b10`. Round 1 returned BLOCKED on 21 distinct defects, all folded; nothing here re-reports
one. Every number below was re-measured against source, and the 29 confirmed findings collapse to 17
distinct defects.*

No blocker. Four highs, six mediums, seven lows. The mechanism rev-5 added is sound and the owner's
ratified choice is correctly recorded as a relaxation rather than a claim of inertness — but the fold
that added it did two things imperfectly, and both recur across lenses.

First, the **three new arms cannot make the observations they claim**. Two of the three
(`AC5b`'s between-bounds dossier and `AC5c`'s inert branch) are unfalsifiable as specified, because
S3 pins BOTH shipped defaults at 20,480 and no S-item asks the fixture conf to declare them apart.
The spec believes it has armed the one observation that distinguishes a dossier class from a row class
under a larger bound; it has not. That converged from the mechanism and arms lenses independently.

Second, **the figures that PRICE the ratified decision are wrong at the class edges**, and the wording
that describes the new mechanism to adopters was written at rev-2 for two classes and never updated
for three. The pricing error names the best case as the worst; the wording error would ship a rule-set
document that mis-describes its own gate, with no criterion able to see it. Both are the shape round 1
found in H5 and M2 — a correct conclusion resting on a stated basis that does not reproduce.

## High

### H1 — §6 AC5b / §2 S9b: the load-bearing dossier arm has an EMPTY band, so it cannot distinguish a dossier class from its absence

*Converged from the mechanism and arms lenses.*

AC5b names its second arm "the observation that proves the dossier class exists rather than a row class
under a larger bound", and S9b calls the alternative "the arms pass by finding nothing". Both then state
the precondition as a `.codebase-map.conf` in the fixture tree and nothing else. That is not enough. The
suite grades scratch trees only — every `bash "$SCRIPT"` invocation in
`tools/memory-tree/check-memory-hygiene.test.sh` runs inside a `mktemp` tree — and the ONE tree where
`MAP_SUB` resolves is the codebase-map fixture at `:867-881`, whose conf at `:871` is
`MEMORY_ROOT=memory`, `DISCIPLINES`, `FAMILIES` plus `MAP_ROOT=memory/map` at `:872`. It declares no cap
key. With S3 keeping both shipped defaults at 20,480, `DOSSIER_CAP_BYTES == ROW_DOC_CAP_BYTES` in that
tree, the interval "BETWEEN `DOSSIER_CAP_BYTES` and `ROW_DOC_CAP_BYTES`" is empty, and the arm collapses
into the first one (over 20,480, named) — which an implementation carrying NO dossier branch at all
satisfies identically. The band is a property of the fixture conf, and no S-item, files-touched row or
criterion asks for it.

**Fold.** §2 S9b: state the precondition in full — the dossier fixture tree's `.memory-tree.conf`
DECLARES the two keys apart (`ROW_DOC_CAP_BYTES=61440`, `DOSSIER_CAP_BYTES=20480`) as well as carrying
the `.codebase-map.conf`, because with both keys absent the two bounds are one number and the
between-bounds arm has nowhere to sit. §6 AC5b: add that the fixture tree declares distinct values, and
name the third fixture the band makes possible — a ROW document sized between the two, asserted named
against the row cap. That one conf line is also what makes H2 constructible, so write it once and cite
it from both.

### H2 — §6 AC5c: the inertness arm cannot fail, and S4 forgoes a guard on the strength of a precedent that has one

*Converged from the mechanism and arms lenses; the strongest form of the vacuity class in this batch.*

AC5c asserts that in a tree with NO codebase map the dossier branch is inert and "no row document is
judged against `DOSSIER_CAP_BYTES`". Neither half is observable. `index_set` adds
`$M/$MAP_SUB/README.md`, `FOUNDATION.md` and `features/*.md` only inside `if [ -n "$MAP_SUB" ]`
(`tools/memory-tree/check-memory-hygiene.sh:341-344`), and `MAP_SUB` is empty without a
`.codebase-map.conf` (`:33-38`) — so a fixture `memory/map/features/big.md` is never in check 6's
population at all. Silence is guaranteed by MEMBERSHIP, one layer above the branch under test, and the
arm therefore passes under a `MAP_SUB`-keyed branch, a hardcoded-literal branch, and no branch
whatsoever. The slip it exists to catch is a selector built as `index(f, M "/" MAP_SUB) == 1`, which
under an empty `MAP_SUB` resolves to `memory/` and prefix-matches EVERY row document — silently capping
the whole class at 20,480 and undoing the unit. With both caps numerically equal in a fixture that
declares neither key, even that produces an identical verdict.

Compounding it, S4 declines a guard on cited authority that runs the other way: "the same variable check
7's `ex7` already uses, so it is inert by construction … rather than needing its own guard". `ex7`'s map
alternatives are added under an explicit emptiness guard, `[ -n "$MAP_SUB" ] && ex7="$ex7|…"` at `:401`.
The precedent guards; the spec reads it as licence not to.

**Fold.** §6 AC5c: make the observation discriminating — a no-map fixture tree that DECLARES
`ROW_DOC_CAP_BYTES` above `DOSSIER_CAP_BYTES` and carries a row document sized between them, asserted
SILENT, so a degenerate `memory/`-prefixing selector reds. §2 S4: drop the "rather than needing its own
guard" clause and state the truth — the branch reuses `MAP_SUB`, and like `ex7` at `:401` it is written
under an emptiness guard so an empty `MAP_SUB` cannot degenerate into a prefix that matches the whole
tree.

### H3 — §2 S14 / §6 AC9: the prescribed prose shape is the rev-2 TWO-class sentence, so the shipped rule-set would document two classes for a three-class gate

*Converged from the mechanism, arms and consistency lenses — three of three.*

S14 was authored at rev-2, when the design had two classes, and still instructs every carrier to "state
the new shape: rows carry a declared byte bound and no line bound; guides carry both". §5's user-docs
bullet delegates entirely to S14. But S4 makes the engine THREE classes, and two of S14's own listed
carriers state the class structure rather than a figure: `memory/HYGIENE.md:127` opens rule 6 with
"index size caps — TWO classes, because prose and rows fail for different reasons", and `:276` gives ONE
cap to all three map documents — "`README.md`, `FOUNDATION.md` and `features/*.md` carry the size caps
(check 6: 20 KB / 250 lines)" — with the SPLIT remedy at `:277-278` hanging off that bound. Under S4
`features/*.md` take `DOSSIER_CAP_BYTES` while `map/README.md` and `FOUNDATION.md` take
`ROW_DOC_CAP_BYTES` (§4 prices `FOUNDATION.md` among "the other line-bound members", i.e. row class), so
the map subtree now splits across two bounds and the SPLIT remedy needs re-attaching. I diffed both
carriers: `tools/memory-tree/HYGIENE.template.md` is byte-identical at `:127-137` and `:270-280`, so
this is what an adopter receives.

Nothing can see the omission. AC9's predicate is only that no listed carrier "still states a retired
figure", which a two-class rule 6 satisfies; AC9's pattern `20 ?KB|20,?480|250 lines` does not match
`:127` at all (`git grep` confirms `:128` matches and `:127` does not); and AC8's parity gate compares
the dogfood copy to the template, so both being equally wrong is green.

**Fold.** §2 S14: rewrite the prescribed shape for three classes — guides carry both bounds, codebase-map
dossiers carry `DOSSIER_CAP_BYTES` and no line bound, every other row document carries
`ROW_DOC_CAP_BYTES` and no line bound — and name `memory/HYGIENE.md:127` and its mirror explicitly as
the class-COUNT carriers, since AC9's figure pattern cannot reach them. Add to S14 that `:276-278`
splits the map subtree across the two byte bounds and re-attaches the SPLIT remedy to the dossier one.
§6 AC9: state the retired figure PER carrier rather than once for the list, and add a clause that rule 6
and its mirror name three classes and both keys. Keep the two carriers byte-identical, and use S14's own
"a declared byte bound" idiom rather than spelling gov's 61,440 into the shipped template.

### H4 — §4 Design: the "roughly 350 lines / 39%" price of the F3 answer is the class MEAN presented as the densest case, and the ceiling range states the mean as its floor

*Converged from the mechanism, arms and consistency lenses — three of three, and the single most-repeated
figure in the record.*

Measured over all 12 `memory/map/features/*.md` at base `43eb6b10`, densities run 51.22 B/line
(`codebase-map.md`, 3,944 B / 77 L) to 74.69 (`memory-tree-merge-driver.md`, 14,713 B / 197 L). Three
consequences, none of which the spec states:

Today's line-derived ceiling (250 x density) runs **12,805 B to 18,671 B**, not §4's "between about 14.5
KB and 18.7 KB". Six of the twelve sit below 14,500 — `agent-cap.md` 14,413, `row-grammar.md` 14,047,
`session-kickoff.md` 13,613, `testsuite-counts.md` 12,939, `install-prefix.md` 12,907, `codebase-map.md`
12,805 — and 14,698 B is the class MEAN, so the stated floor is the average.

Lines reachable under a 20,480-byte bound with no line count are **274 for the densest** (a +9.7%
loosening) and **400 for the sparsest** (+59.9%). "Lets the densest of them reach roughly 350 lines
instead of 250 … about a **39% effective loosening**" is arithmetically the mean: mean density 58.79
B/line gives 348 lines, and 20,480/14,698 = +39.3%. The spec labels the best case as the worst and
understates the true worst case by roughly half.

The rejected single-key range is likewise **3.29x to 4.80x**, not "3.3x to 4.3x" — 4.26x is
`agent-cap.md`, a mid-density member (61,440/12,805 = 4.80 is the class maximum).

The conclusion survives every correction: the dossier key does bound the loosening far below the
single-key alternative, which is what the owner ratified on. What fails is the basis, and it is
load-bearing for the record of that decision — the pair repeats in §4 Data model, §4's costs section,
§3's closing paragraph, §8 F5, §9 rev-5 and `memory/builds/aRelaxedShard/README.md:95` and `:104-107`.
Same shape as round 1's H5.

**Fold.** §4 Data model and §4 "What retiring the row line bound costs": state the range with both ends
NAMED — today's effective ceilings run 12.8 KB (`codebase-map.md`, 51.2 B/line) to 18.7 KB
(`memory-tree-merge-driver.md`, 74.7 B/line); a 20,480-byte bound with no line count reaches 274 lines
for the densest and 400 for the sparsest, so the per-document loosening is +10% to +60% and about +39%
on the class mean. Correct the single-key figure to 3.3x-to-4.8x. Then propagate the corrected pair to
§3's closing paragraph, §8 F5, §9 rev-5 and the README's F3 and F5 bullets — measured at base
`43eb6b10` only.

## Medium

### M1 — §2 S14 / S16: `tools/memory-tree/README.md:138` carries the third instance of the mis-citation S16 exists to correct, and S14 hands it the wrong remedy

That file's ONLY cap carrier is `:138` — "`memory/guides/BUILD-METHOD.md` is capped at 250 lines by
hygiene rule 6 and is re-read WHOLE at every pass boundary" — verified with
`git grep -nE '20 ?KB|20,?480|250 lines|250-line|750'` over the file, one hit. That is false TODAY, not
merely after this unit: rule 6 caps `guides/*.md` at 60 KB / 750 lines
(`memory/HYGIENE.md:128`, `check-memory-hygiene.sh:385`). It is the identical wrong attribution S16
corrects at `memory/guides/BUILD-METHOD.md:8` and `tools/memory-tree/BUILD-METHOD.template.md:8`. S14
nevertheless covers this file with the row-class remedy ("rows carry a declared byte bound and no line
bound"), the files-touched row describes its change as "the figures" when it holds no row-class figure,
and AC9 forces `250 lines` out of the line while grading nothing about what replaces it — so the
mis-attribution half can survive the sweep verbatim. Separately, S3 commits that "the kit README says
so" about the non-opt-outable line retirement, which no scope item or files-touched row attributes.

**Fold.** §2: move `tools/memory-tree/README.md:138` from S14 to S16, whose population becomes three
carriers, and correct it the same way — the 250-line budget is BUILD-METHOD's own re-read discipline,
not rule 6's cap. Add to S3 or S14 the sentence that file must GAIN: the line bound is retired for every
class below `guides/` and an adopter cannot opt out. §4's files-touched row for it changes from "the
figures" to those two edits.

### M2 — §2 S4 / §4 Files touched: the engine's own justification comment states the refusal this unit reverses, and nothing scopes, sweeps or gates it

`tools/memory-tree/check-memory-hygiene.sh:376-378` reads "So guides carry 3x and every row document
keeps the original cap: tripling the allowance for a backlog shard or a map dossier would loosen a
curation discipline nobody asked to loosen, and the two classes fail for different reasons." Every
clause of that is false on landing — rows get 61,440, dossiers get their own key, there are three
classes. §3's closing paragraph and §10 cite these words in the PRESENT tense as the ground being
relaxed, which invites preserving them; but no S-item edits the comment, §4's files-touched row for the
engine lists only "two conf reads and re-normalisation · the three-class cap block · the message · kit
version", AC9's pattern cannot match a sentence carrying no digits, and the engine is outside S14's path
list anyway. Nothing else reads `.sh` comments: kit/dogfood parity pairs `.md` files,
`check-method-carriers.sh` is structural, and `check-verdict-epoch.sh` keys on NON-comment lines. So the
kit ships a comment contradicting its own code, in the one file this unit rewrites — the same
stale-carrier class S14 to S16 exist for, and the class this repo's charter calls out by name.

**Fold.** §2 S4: add the comment block at `:372-378` to the scope item — rewritten to state the three
classes and to record `TOOL-aWidenedGuide-1`'s refusal as REOPENED by a ratified decision rather than as
current policy — and add it to §4's files-touched row for the engine.

### M3 — §4 Inventory: the sub-population table reports `memory/DECISIONS.md` against a group that excludes it, and counts 5 where there are 4

Re-measured at base. After the three correct rows (12 dossiers max 14,713/197; 5 `RUN.md` max 13,806/151;
4 backlog shards max 19,152/78), the residual 8 members split as: `memory/LIVE.md` 2,054/25,
`memory/ledger/2026-08.md` 3,240/40 and `memory/ledger/2026-07.md` 1,324/19 — three members, maxima
**3,240 B / 40 L**; and `memory/README.md` 2,427/35, `memory/map/README.md` 2,410/35,
`memory/map/FOUNDATION.md` 732/30, `memory/builds/aPrunedCeremony/STATUS.md` 2,695/34 — four members,
maxima 2,695 B / 35 L. The table prints "generated indices and ledgers | 3 | 12,328 | 69", which is
`memory/DECISIONS.md` — an authored append-only log that is neither generated nor a ledger, and which §4
two sections later defines out of the group ("The generated indices — `memory/LIVE.md` and the ledger
shards are rendered"). It then prints the four-file maxima against a count of 5. The two errors offset,
which is the only reason 12+5+4+3+5 reaches 29. This is the table round 1's H2 fold created to stop a
wrong per-group maximum hiding a class member, and `two-answers-to-one-question` is a class §7 selects.

**Fold.** §4 Inventory: split the residual honestly — "generated indices and ledgers | 3 | 3,240 | 40"
and "other authored row documents | 4 | 2,695 | 35" — and give `memory/DECISIONS.md` its own row at
12,328 / 69, or fold it into a row whose label admits it. Re-check that the members column still sums
to 29 after the split.

### M4 — §2 S9 / §6 AC5: the tRunBig fixture carries THREE contracts and the spec preserves two; the third needs a band neither S9 nor AC5 states

`tools/memory-tree/check-memory-hygiene.test.sh:591-597` documents the arm as (a) the only proof
`RUN.md` entered `index_set`, and (b) — verbatim — "ALSO the scoping control for the per-class cap: at
265 lines it sits over the ROW document cap and well under the guide cap, so it proves the widening did
not leak out of `guides/` into the row documents". `memory/builds/aRelaxedShard/README.md:120` says
"three separate contracts are asserted THROUGH it"; S9 and AC5 enumerate two, and the word "scoping"
appears nowhere in the spec. The line-axis form of that control dies with the bound. Its byte-axis
replacement exists only if the regrown fixture sits BETWEEN the row cap in force in that tree (the
shipped 20,480 — that conf declares no key) and the guide's 61,440: grow it to 70 KB and the arm still
fires while a guide-cap leak into the row class becomes invisible. In the real repo the band is empty
because `ROW_DOC_CAP_BYTES` equals the guide cap, so the fixture is the only place the leak is
observable at all. Second unstated precondition: the check-7 exemption arm at `:602-604` is an ABSENCE
assertion over the 340-char unfenced row written at `:427`, so a regrow that rebuilds rather than appends
silences it too.

**Fold.** §2 S9: state the band and the preserved row — the fixture is grown past the row byte cap in
force in that tree and kept UNDER 61,440, so it remains the scoping control on the byte axis, and the
340-char unfenced row at `:427` survives the regrow. §6 AC5: observe all three — named by check 6 on the
byte axis, still exempt from check 7, and still under the guide cap.

### M5 — §2 S5 / §6 AC2, AC4: only the ROW message shape is graded, so the likeliest edit ships a guide finding whose stated reason is under its own cap

Check 6 emits ONE statement for every class: `printf "%s (%dB %dL > %dB/%dL)\n"` at
`check-memory-hygiene.sh:386`. S5 scopes bytes-plus-applied-cap "for a row document" and AC2 grades that
shape; nothing grades the guide shape. The minimal implementation — one bytes-only `printf` for all
classes — then renders a guide's LINE breach as a byte figure far under its own byte cap: I rebuilt the
fixture from `:366-367` and `memory/guides/tfixture.md` is 761 lines / 7,509 B, so the finding would read
about 7,509 B against a 61,440 B cap. A gate stating a reason that is under its own threshold is a gate
that lies. AC4 cannot see it — `chit`/`cnot` are `cblock "$out" <n> | grep -qF <path>` (`:497-498`),
fixed-string greps on the PATH with no assertion on message text — and `check-arms.py` keys on the
`fail 6` string, not the per-file format, so AC10 misses it as well.

**Fold.** §2 S5: state the message per class — a row document reports bytes and the applied byte cap; a
guide keeps both figures and both caps. §6 AC4: add that `memory/guides/tfixture.md`'s finding still
carries its LINE count and the guide line cap, which is the pair that makes AC2 a split rather than a
deletion.

### M6 — §5 closing line: F3 is still offered to the owner as an open scope item

Spec `:314` reads "One item for the owner scope menu: F3, the dossier byte sub-bound, which the F5
decision opened." §8 F3 at `:405` is "RESOLVED (owner, 2026-08-17): its own conf key", S1b builds it, the
status header at `:3` carries `ratified 2026-08-17`, and `README:88` and `:110` state "All five forks
resolved by the owner" and "Every fork is resolved, so the spec carries `ratified`". A reader of §5 alone
concludes an owner decision is outstanding and the unit is not READY. Stale line left by the rev-5 fold,
which records the F3 resolution and does not mention updating §5.

**Fold.** §5: delete the line, or replace it with "No open scope item: F3 resolved to
`DOSSIER_CAP_BYTES` (§8)."

## Low

### L1 — §2 S14 / §6 AC9: `.gitattributes:30` is a dated measurement, not a present-tense cap claim, and AC9 would have the builder falsify it

`.gitattributes:26` is present tense ("check 6  caps index files at 20 KB;"). `:30` is the middle of a
past-tense evidential sentence — "Measured — DECISIONS.md at 20466 B (LF) reported 20559 B against the
20480 B cap in the primary tree and blocked a push, while the worktree that wrote it read green" — which
is the incident justifying the whole `eol=lf` block. S14 and the files-touched row call both "the two
present-tense cap claims" and require each to "state the new shape"; AC9 then requires that no listed
carrier still states a retired figure and does not name `:30` among its expected survivors. Restating a
dated 20,480-byte measurement in 61,440 terms makes it false. (AC9's survivor list also names
`.memory-tree.conf:57` while a second `READ_PATH_CEILING` headroom figure sits at `:70` in the comma
spelling.)

**Fold.** §2 S14: describe `:26` as the present-tense claim and `:30` as a dated measurement that stays,
or reword `:30` to "the then-20480 B cap". §6 AC9: add `.gitattributes:30` and `.memory-tree.conf:70` to
the expected-survivor list with their reasons.

### L2 — §4 "What retiring the row line bound costs": the residual bullet counts seven members where there are six, and its 16.4% ceiling reproduces at no tree

"Both ledgers, three READMEs, a STATUS file, `FOUNDATION.md`" enumerates seven. §4's own 22-file
enumeration four paragraphs earlier gives the residual after dossiers and run-state files as SIX, with
exactly TWO READMEs — `index_set` (`check-memory-hygiene.sh:337-359`) admits only `$M/README.md` and
`$M/$MAP_SUB/README.md`; build-folder READMEs are not in check 6's population. Range: `FOUNDATION.md`
732 B is 3.57% of 20,480, so the stated 3.6% floor reproduces, but the maximum is
`memory/ledger/2026-08.md` at 3,240 B = **15.82%**, not 16.4% (which would need 3,359 B). The same file
is 3,423 B = 16.71% at the local default tip, so the printed figure matches neither tree — the two-tree
mix round 1's closing note warned any re-measurement against.

**Fold.** §4: "both ledgers, two READMEs, a STATUS file, `FOUNDATION.md`" and "between 3.6% and 15.8% of
the byte cap", measured at base `43eb6b10`.

### L3 — §5 risks and §7 classes: two enumerations the rev-5 fold outgrew

§5 `:298-307` opens "**risks** — Three, and rev-1 named the wrong one as silent" and then lists First,
Second, Third, **Fourth** — the fourth being rev-5's inert-branch item, which §9 rev-5 confirms it added.
§7 `:384` credits `fixture-passes-by-finding-nothing` to "(S8, S9, S10 exist for it)" while S9b's own
text is "without it the branch is inert and the arms pass by finding nothing" — the same class, added in
the same revision, uncredited.

**Fold.** §5: "Four". §7: add S9b to that class's citation list.

### L4 — §4 "Why rotation cannot be the answer here": the 633-byte head carries TWO rotation announcements, not three

`git show 43eb6b10:memory/backlog/TOOL.md | sed -n '1,5p' | wc -c` is 633 B and reproduces; the head's
only announcements are line 4 ("Rotated 2026-08-14") and line 5 ("Rotated 2026-08-17"), with line 6
already a dash row. Three TOOL archives exist at base, so the second same-day rotation is unannounced —
which is check 10's known blindness (`TOOL-cTracedPromise-6`, out of scope) rather than a miscount to
fix in the archive. Round 1's M10 measured this correctly as "two ~275 B per-rotation announcements"; the
rev-2 fold wrote the wrong count on top of it. The paragraph's 19,152 B / 93.5% floor is unaffected.

**Fold.** §4: "the 633-byte head with its two rotation announcements", and if the third rotation's
missing announcement is worth a sentence, attribute it to `TOOL-cTracedPromise-6` rather than treating
it as a figure.

### L5 — §9 Revision log: rev-5 is entered above rev-4, so the history reads backwards at the two revisions this round audits

Spec `:432-465` runs rev-1, rev-2, rev-3, rev-5, rev-4. The two are causally ordered: rev-4 folded F1 and
F5 and RE-OPENED F3, and rev-5's own text leans on it ("F5's answer removed that ground"). The template's
own shape ascends (`tools/memory-tree/SPEC-TEMPLATE.template.md:160-163`), as does every other spec
sampled. A log's order is part of its content.

**Fold.** §9: swap the two entries so the log ascends.

### L6 — §2 S11 + S12 / §6: the one deliverable an adopter actually receives still has no criterion

No §6 bullet names `tools/memory-tree/.memory-tree.conf.example`; AC6 is scoped to "its new check-6 row
arms" and `FLOOR_ASSERTIONS`, and the S11 arm is neither. Nothing else reads that file's key set:
`adopt-memory-tree.sh:40` only copies it, `check-install-prefix.sh` excludes `*.conf.example`, and
`kit.toml` compares only its `DISCIPLINES|FAMILIES` lines. So if S11 and S12 are skipped, no leg and no
criterion reds, and AC6's "raised to the new executed count" is vacuously satisfiable at the lower count.
Round 1's M8 fold prescribed both halves; the §2 half landed as S11/S12 and the §6 half did not. (S12's
idiom claim does reproduce: `UNIVERSAL_BUDGET="3"` and `ROW_DUPLICATE_PIN="0"` ship with values and say
why, while every measured pin ships blank.)

**Fold.** §6: add a criterion — when the hygiene self-test runs, its example-conf arm asserts
`tools/memory-tree/.memory-tree.conf.example` declares BOTH keys at the shipped default in the
policy-ceiling idiom. That is the arm S11 already specifies; it just needs grading.

### L7 — README "What the adopters inherit" item 3: 5 + 22 does not make 29

`README:61-63` reads "The byte bound decides the backlog shards and the decision log; the line bound
decides the other 22 row documents". Four shards plus the decision log is 5, and 5 + 22 = 27 against a
29-member class. Measured at base, exactly SEVEN are byte-bound: the four shards, `memory/DECISIONS.md`,
`memory/LIVE.md` (2,054 B / 25 L = 82.16 B/line, over the 81.92 break-even) and
`memory/builds/cBriefedPilot/RUN.md` (13,806 / 151 = 91.4). Spec §4 `:171-175` states exactly that; the
overview drops the two members that make the arithmetic close, on the very measurement round 1's blocker
was about.

**Fold.** README item 3: "the byte bound decides the four backlog shards, the decision log,
`memory/LIVE.md` and one run-state file — seven; the line bound decides the other 22."

## Refuted

Fourteen of the 43 raw findings were refuted on measurement (precision 0.67). Two are instructive. Three
separate passes attacked the dossier class's MEMBERSHIP — that S4's pointer at `MAP_SUB` leaves
`$MAP_SUB/README.md` and `FOUNDATION.md` ambiguous between two readings differing 3x — and all three
failed: S4 cites the variable to justify inertness, not to define a path set, and the population is
fixed by §4's Inventory row (`memory/map/features/*.md` dossiers, 12), by the whole pricing being computed
over `features/*.md` only, and by §4 placing `FOUNDATION.md` explicitly among "the other line-bound
members". Two more attacked the "conf-validation precedent at `:101`" label; the adjective is loose (the
engine validates no conf value and sources the conf unvalidated at `:27`), but `:101` reproduces the
IDIOM the citation is for — a named refusal before any scan on `exit 2` — and the phrase is round 1's own
H7 fold instruction verbatim, so it penalises the fold for adopting the reviewer's wording. Also refuted:
that S15/S16 are unobserved (round 1's M6 fold explicitly moved that observation onto
`kit-dogfood-parity.test.sh`, and no gate in this repo grades prose semantics — both carriers say so in
their own headers); that the kit README's "No conf keys here change" is falsified by `DOSSIER_CAP_BYTES`
(the sentence answers "does adopting the map require editing `.memory-tree.conf`", and the answer stays
no); and F1's third candidate arithmetic, which is round 1's L1 restated at the corrected B/day.

## Unverified

None. Every raw finding received a skeptic verdict.

## Is the design clean enough to build?

Yes, with the folds above landed as rev-6. No confirmed blocker: the mechanism rev-5 added — two keys,
one resolution helper, a three-class ordered cap block keyed on `MAP_SUB` — is buildable exactly as
written, and nothing here reopens a ratified fork. Fifteen of the seventeen defects are text: figures to
re-derive at base, a sentence to re-scope, a stale line to delete, two counts to move. The two that
change what the builder WRITES (H1 and H2) share one fold — the dossier fixture tree declares the two
caps apart — and they announce themselves at construction, because you cannot size a file between 20,480
and 20,480. Round 3 is not warranted; building is now the stricter test, and the remaining risk is in the
fold's discipline rather than in the design.

## What the fold must not do

The tempting repair to H1 is the wrong one: **do not raise the shipped default** to open the
between-bounds band. S3's 20,480 for BOTH keys is what keeps this unit out of
`pin-copied-from-another-corpus` and what makes AC1a and the migration bullet true. The band belongs in
the FIXTURE conf, and only there.

The guide arms are untouchable. `memory/guides/tfixture.md` past 750 lines stays NAMED and
`memory/guides/twide.md` at 401 lines stays SILENT — they are the only proof the classes are still
separate. M5's fold adds a message clause to AC4; it must not rebuild `twide.md` on the byte axis, and
S10 already forbids that.

H4's corrections move figures §9 asserts were measured at base `43eb6b10`. Re-measure at that base and
nowhere else: the local default is 37 commits ahead and `memory/ledger/2026-08.md` reads 3,423 B there
against 3,240 B at base. A mix of two trees is the shape that produced round 1's blocker, and L2's 16.4%
is already one.

Nothing in the fold may rewrite `memory/DECISIONS.md:41` (append-only, and AC9 names it a survivor) or
restate `.gitattributes:30`'s dated measurement in the new number. H3's fix must keep
`memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` byte-identical at the edited lines —
`kit-dogfood-parity.test.sh` pairs them — and must not spell gov's declared 61,440 into the template an
adopter receives at the 20,480 default.

M2's fold corrects the engine comment; it must not DELETE the record of the refusal. §3's closing
paragraph and §10 depend on `TOOL-aWidenedGuide-1`'s ground being legible as reopened by a ratified
decision. And no fold may hand any class below `guides/` a line bound back, in the engine or in prose —
F5 and F3 ratified byte-only, and §3's first non-goal is the guard on that.

`READ_PATH_CEILING`, the 300-char entry budget, rotation's carry-forward rule, byte normalisation
(`TOOL-aRootedPrefix-3`), check 10's rotation blindness (`TOOL-cTracedPromise-6`) and the re-shape unit
all stay exactly where round 1 left them.
