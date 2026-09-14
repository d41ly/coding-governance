**Serves:** diff-review TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4

# aRatifiedRulings — Tier-2 diff review of the cumulative landing diff

*Node `a`, 2026-09-14, branch `branch/aRatifiedRulings`. Adversarial pass over the diff that lands
on `main`: four primed lens passes, five skeptic batches prompted to REFUTE, one synthesis. Every
confirmed finding below was re-read at source in this tree before it was written here; where this
report narrows a finding's claim, it says so in the finding.*

**Reviewed range: `16da4c6abdb5d74ad80891f51f254cd5205d0b17...HEAD`** (14 commits, 51 files,
+3511 / -106). HEAD is `fc6ee211db75bf2efd76b8a6ce952286afc196f7`. The subjects that carry every
finding, pinned at the blob they were read at:

- `tools/unattended/check-unattended.sh@740ce329b96c6e49c34c500562730914126552cf`
- `tools/unattended/lib-unattended.sh@19f2cfac02f13d62a0e864f4b90fd41796d05966`
- `tools/unattended/check-brief-recorded.sh@b1feb19f33ead89c0870aefd9d5fab7cb8951a2c`
- `tools/unattended/unattended.sh@0d3262799950fdbc6990d10a352a81267b8b71c8`
- `tools/memory-tree/check-memory-hygiene.test.sh@0bedadb7da0a5e99a8bd831ff90c659a0bc2dc06`

**Round: 1.** This is the first review of the CODE. The two rounds already in this folder audited the
four specs at rev-1 and rev-2; neither read a line of the checkers, so nothing here is a re-report.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. One HIGH: the check-23 brief exclusion (unit 2) turned a loud false red
into a silent green for a commit shape the kit's own header calls ordinary — a bookkeeping commit
carrying the run-state file and the brief is now selected as the pass commit, grades clean, and the
pass's real commit is never graded. Two LOW ids are one defect: the check-23 header and the unit-2
spec both credit `brief-recorded` with a join it does not make. One LOW: a `29-file` fixture count
repeated in a test comment and seven spec lines that no command reproduces. Every fix is small and
lives inside the files the diff already touched.

**Review shape:** raw 10 · confirmed 4 · refuted 6 · unverified 0 · precision 0.40.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every
lens and every skeptic batch came back, so the finding set is complete for the lenses that ran and
the zero counts below (0 BLOCKER, 0 unverified) are positive evidence rather than the artefact of a
dead lens. The precision of 0.40 is below the charter's ~0.5 tightening threshold (§8): six of ten
raw findings were refuted, which says the lens priming was wide for a diff whose product surface is
four checker edits and their fixtures. Noted for the next round's brief, not a defect of this diff.

**Adjudicated severities:** BLOCKER 0 · HIGH 1 · MEDIUM 0 · LOW 3. Id 7 was filed MEDIUM and is HIGH
here; ids 2 and 5 are one defect (cluster B) and keep their LOW; id 4 keeps its LOW.

Severity meaning in this record: BLOCKER — the diff cannot land: a gate on the bar reports green on
a shape it was built to red, with no compensating leg, or a write path the charter's §9 covers is
open. HIGH — a merge-bar leg reports green on an ordinary shape it should red, or reds an ordinary
shape it should pass, and the fix is contained inside the leg and its fixture. MEDIUM — a premise
in a shipped file is false against source so a reader acting on it does the wrong thing, but no
gate verdict changes. LOW — a sentence or a figure does not reproduce; no verdict changes.

Why id 7 is HIGH and not BLOCKER, stated so the line is auditable: the driver is NOT fooled by the
same shape — `unattended.sh:4809-4815` requires an `overlaps` hit between the selected commit's
paths and the row's declared set before condition 1 closes a pass, and a `{RUN.md, brief}` commit
overlaps nothing a pass declares unless it declared the prompts folder. So the pass stays open in
the driver, the stray write lands, and only check 23 fails to see it. The finding's clause "the
driver's condition 1 also reads the pass as already committed" is narrowed here to that declared-
prompts case. Why not MEDIUM: check 23 is on the bar, its header states the shape as the ordinary
one, and a green that means "graded the wrong commit" is the §7 class this repo names first.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 7 | HIGH | 2 | `tools/unattended/lib-unattended.sh:171` · `check-unattended.sh:2373-2381` | A |
| 2 | LOW | 2 | `tools/unattended/check-unattended.sh:2249-2250` | B |
| 5 | LOW | 2 | `tools/unattended/check-unattended.sh:2367-2372` · spec U2 §3 lines 186-189 | B |
| 4 | LOW | 3 | `tools/memory-tree/check-memory-hygiene.test.sh:2222` · spec U3 lines 23, 107, 130, 192, 213, 220, 350 | C |

---

## HIGH

### A — the brief exclusion lives in check 23 while `pass_commit` selects the commit (id 7)

**Where.** `tools/unattended/lib-unattended.sh:171` (the `grep -vxF -- "$_prel"` that is
`pass_commit`'s only exclusion) and `tools/unattended/check-unattended.sh:2373-2381` (the new
`dsbrief` branch that excludes the brief-row path from the subset test).

**What.** `pass_commit` walks `$_pa..$_pto` oldest-first and returns the first commit whose subject
names the unit and whose touch set minus the run-state file is non-empty. It knows nothing about
brief rows. Check 23 then reads that commit's touch set, subtracts the run-state file, and — new on
this diff — skips every path a ` brief · item <unit> · reason ` row in the run-state blob at that
commit names. Put the two together on the commit shape the check's own header (`:2292-2299`) calls
ordinary: `verb_brief` requires the brief to be TRACKED (`unattended.sh:4280`, `ls-files
--error-unmatch`), so the brief is staged before `--brief`; `--brief` stages the run-state file; the
run commits both with a subject naming the unit, exactly as the header says it commits the
`--dispatch` declaration. That commit's touch set minus `RUN.md` is exactly the brief path, so
`pass_commit` selects it. Check 23 excludes the brief path, `dsout` stays empty, and the leg prints
nothing. The pass's real commit — the next one naming the unit, carrying `work/one.txt` and the
stray `work/stray.txt` — is never read by check 23, because the check grades one commit per row.

Before this diff the same commit shape redded loudly on the brief path (a false accusation, but one
that made the run declare the prompts folder or restructure its commits). After it the shape is
silent in every case. The finding reproduced this end to end on the suite's own scratch harness;
this report re-derived it from the two functions and confirms the selection: nothing in
`pass_commit` can skip a commit whose only non-run-state path is the brief.

**Scope narrowed.** The driver's condition 1 (`unattended.sh:4802-4816`) is not defeated: it calls
the same `pass_commit`, gets the same bookkeeping commit, then requires an `overlaps` hit against
the row's declared paths before it treats the pass as closed, and the brief overlaps nothing an
ordinary pass declares. So the driver keeps the pass open and the stray write lands unchecked by
check 23 alone. That is still a bar leg reporting green on the wrong commit.

**Class.** `gotchas/two-guards-one-question-two-answers`: the shared predicate picks the commit and
the consumer decides what the commit is allowed to carry, so a path the consumer forgives is a path
the predicate should never have counted. The same split is what the check's own comment at
`:2296-2299` says the run-state skip was moved into the library to avoid.

**Fix.** One predicate, one answer. In `pass_commit`, after `grep -vxF -- "$_prel"`, also drop every
path a ` brief · item $_pu · reason ` row in `$_prel` AT `$_pc` names — the same two `${x#* ·
reason }` / `${x#* }` expansions check 23 uses, read from `GIT show "$_pc:$_prel"` — and `continue`
when nothing is left. A commit that moved only the run-state file and the brief it staged is
bookkeeping, exactly like the `RUN.md`-only commit the function already skips. Check 23's `dsbrief`
branch then becomes redundant for the pass commit it selects and can stay as the report-channel
announcement, or go. The driver inherits the fix through the library, which is why it belongs there.

**Left-shift.** A fixture in `tools/unattended/check-unattended.test.sh` beside the five brief arms
this diff added, F: `drow` → commit `{brief, brief row}` with a subject naming the unit → commit
`{work/one.txt, work/stray.txt}` with a subject naming the unit → `hit "$(run)" "wrote
work/stray.txt"`. Stage it against HEAD first and confirm RED (§7: a new gate is not landed until
its failing case has been observed); it is red at HEAD by the derivation above. Raise
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` by the arm's assertion count in the same commit, since this
diff already moved both and the canary reds a floor that lags. A sibling arm for `pass_commit`
itself in `unattended.test.sh` — the bookkeeping commit is skipped, the work commit is returned —
pins the library rather than the consumer, which is where the rule now lives.

---

## LOW

### B — the header and the spec credit `brief-recorded` with a join it does not make (ids 2, 5)

**Where.** `tools/unattended/check-unattended.sh:2249-2250`: "a row naming a path no brief was handed
at is a lie the `brief-recorded` leg joins against the build commit". The unit-2 spec repeats it at
§3 lines 186-189. The exclusion set that leans on it is built at `check-unattended.sh:2367-2372`.

**What.** Read against `check-brief-recorded.sh`, the sentence overstates the leg on four counts.
It grades only units whose README row reads ` CLOSED ` (`:234`). It grades the BUILD commit
selected by `build_commit` (`:242`), whose exclusion set skips commits touching only the build
folder, the generated indexes or the shared records — a different commit from check 23's pass
commit, and a pass commit writing only `memory/DECISIONS.md` plus `RUN.md` is never a build commit
at all. It reads the LAST brief row per unit (`tail -1`, `:262`), while check 23's `dsbrief` is the
UNION of every row for the unit at the pass commit (`:2367-2372`), so an earlier row naming a stray
tracked path is excluded by check 23 and read by nothing. And its only assertions are a twelve-hex
shape (`:274-279`), tracked-at-build-commit (`:283-288`), and hash-prefix equals blob (`:289-293`);
nothing asserts the path is a brief or sits under the build folder. `verb_brief` computes the hash
from the working tree itself (`unattended.sh:4284`), so a row naming ANY tracked path is
hash-consistent by construction and the join can only ever catch "the file moved under the row" —
it never tests "was handed".

So the shipped kit file tells an adopter that a stray-path brief row is caught downstream; it is
not, and a two-`--brief` sequence (`--brief U work/stray.txt` then `--brief U <real brief>`, both
accepted because `verb_brief` refuses only untracked, missing, off-roster, terminal and
separator-bearing paths, and its exact-line compare at `:4298` writes a second row for a different
path) leaves the stray path excluded from check 23 and joined by nothing. LOW because the fix is
prose or one containment line, no verdict on the bar changes today, and the same-commit limit the
header already states for dispatch rows covers most of the ground; but a gate header overstating
what it buys is the §7 class this repo names, and this one is in the file adopters read.

**Fix.** Two options; the second is the smaller diff that makes the sentence true rather than
weaker. (1) Prose: rewrite `:2249-2250` and spec lines 186-189 to what the leg proves — "for a
CLOSED unit, `brief-recorded` proves the LAST row's hash still names the blob at the BUILD commit;
nothing proves the path was a brief, and earlier rows are unjoined". (2) Construction: in the
`dsbrief` loop at `:2369`, exclude a row's path only when it sits under the build's own prompts
folder — one `case "$dsbr" in "$(dirname "$f")/prompts/"*) ;; *) continue ;; esac` before the
append — after which the exclusion is bounded to the build folder by construction and the header
can say so instead of citing the sibling leg. If (2), also settle which row is live: mirror the
sibling's last-row rule (reset `dsbrief=$dsnl` before each append) or state in both places that
check 23 takes the union and the sibling the last row, so the two readers are documented as
different rather than assumed the same.

**Left-shift.** For option (2), fixture F2 in the same block as A–E: a brief row naming
`work/stray.txt` with its real hash, the file in the pass commit, `hit "$(run)" "wrote
work/stray.txt"`. RED at HEAD by the code above. For the prose half there is no gate; it joins the
documented §10 check "a gate header that cites another leg as coverage quotes that leg's actual
predicate", which the spec-audit lens for this build already runs on specs and which this report
extends to checker headers.

### C — the `29-file` fixture count reproduces as 9 (id 4)

**Where.** `tools/memory-tree/check-memory-hygiene.test.sh:2222` ("The 29-file tree above"), and
the unit-3 spec at lines 23, 107, 130, 192, 213, 220, 350, the unit's build brief, and commit
`d4509c29`'s subject.

**What.** Rebuilding the check-16 note fixture exactly as `:2181-2200` does — fresh `git init`, the
conf, `AGENTS.md`, `memory/README.md`, `DECISIONS.md`, `stale-header-waiver.txt`, `builds/tOne/
README.md`, one spec, then `gen_build_index.py --write`, which adds `LIVE.md` and
`ledger/2026-08.md` — yields `git ls-files | wc -l` = 9, and the checker's own population at
`check-memory-hygiene.sh:197` (`git ls-files "$M/"`) = 7. No counting of that tree yields 29. The
per-invocation floor (8.0 s), the archive-vs-fixture comparison, and the §4 risk about "a 29-file
corpus" are all attributed to a tree three times the size of the one the arms run. The timings are
real; the population they are ascribed to is not. This is the charter's §7 rule stated outright: no
count of a derived population is written in prose, because the number is wrong on the next commit
and nobody notices — here it was wrong on the commit that wrote it.

**Fix.** Drop the figure from the test comment and say "the check-16 fixture above"; in the spec,
either drop it or replace each occurrence with the derived figure and its derivation in one place
(`git ls-files | wc -l` in the fixture = 9; the checker grades 7 under `memory/`). The build brief
and the commit subject are landed records and stay as written; the spec's §4 measurements table is
the one live reader.

**Left-shift.** Not gateable at reasonable cost — a number in a comment has no source to join
against — so it is a documented check: a measurement row in a spec's §4 that names a population size
quotes the command that produced the size beside it. That sentence belongs in
`memory/TEMPLATE-SPEC.md` §4 if the owner wants it standing; this report only proposes it.

---

## The six refuted findings

The skeptic batches refuted six raw findings; none reached this report, and the synthesis was
handed only the four that survived, so their subjects are not restated here. A refuted claim is not
a finding, and this record does not paraphrase text it did not read. The count is stated so the
shape line above reconciles: 4 confirmed + 6 refuted = 10 raw.

## Not reviewed here, by design

The four specs and the two spec-audit rounds are records, not code, and were read only where a
finding cited them. No confirmed finding names the unit-1 or unit-4 product edits
(`check-memory-hygiene.sh`'s terminal rule; `run-gates.sh`'s seconds-on-kill line), and this report
makes no positive claim about them beyond that: four lenses returning with nothing confirmed there
is evidence for the classes they were primed on, not a proof of absence for the ones they were not.

---

*State for the caller: 0 BLOCKER · 1 HIGH · 0 MEDIUM · 3 LOW, all four ids adjudicated in the
table above. Verdict CLEAN WITH FIXES; the HIGH's fix and its RED-first fixture are owed before the
next round, and this round's record needs no further owner input.*
