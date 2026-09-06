**Serves:** journal TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-12

# Build pass, steps 6 and 7 — the canon overlay, surface-aware suggest, and the arming commit

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. The last three units, sequenced.
Unit 12 is the one that ARMS the build: it writes the full cell matrix into the declaration and flips
the undeclared-cell constant in the SAME change, which is what turns a report-only arm into a refusal.

**Evidences:** TOOL-aSurfacedLexicon-11
- AC1 — amended rev-7 — re-keyed off the exit code. All three of AC1, AC2 and AC3 graded the wiring check by its EXIT STATUS, and that check reds in any sandbox with no rendered Skill, so every scratch-tree run is non-zero whatever the stamp says. AC1 asked for an exit-0 its own fixture could never produce, and the other two asked for a non-zero that was true on every run and evidence about none. All three now read the MESSAGES.
- AC2 — `tools/lexicon/selftest.py` — an overlay block with a stamp carrying a date and node but no REASON — refused under its own wording, and the distinctness from the empty-stamp refusal is asserted in BOTH directions.
- AC3 — amended rev-7, with AC1 and AC2, for the same cause.
- AC4 — `tools/lexicon/selftest.py` — the posture line — printed ABOVE the counts on both a passing and a failing run, so an unfreeze cannot be read past.
- AC5 — `tools/lexicon/selftest.py` — the merge with no overlay declared — byte-identical to the shipped canon, asserted in-process against `canon.CLUSTERS` rather than against a reading of it.
- AC6 — `tools/lexicon/selftest.py` — replace, add and delete — six arms, each asserted through all three canon accessors. All six red when the merge is suppressed.
- AC7 — `tools/lexicon/selftest.py` — the refusals — four, not the three the spec named, and a fourth arm asserts they are pairwise distinct so no refusal wears another's message.
- AC8 — `tools/lexicon/selftest.py` — a canon block staged into the scaffolder's output — refused, naming the file and line, and an ABSENT scaffold ANNOUNCES the skip rather than letting a green row read as verified.
- AC9 — `tools/lexicon/selftest.py` — the guard's own population — the narrowed predicate matches nothing in the shipped scaffold while the loose form matches exactly one line, so the single near-miss is pinned and a later reader knows the count is what it is by design.
- AC10 — `bash tools/lexicon/adopt-lexicon.sh --check` — the wiring check on the tracked tree — rc 0, `Skill in sync, declaration grades clean`, so the refusal branch does not fire on the frozen state every adopter who is not the author sits in.
- AC11 — `tools/lexicon/adopt-lexicon.sh` — a self-exercising arm inside the wiring check — it stands up its own stamped scratch conf and asserts the posture line; suppressing the merge makes it say the overlay did not reach the answer, and an unavailable temp dir makes it ANNOUNCE the skip rather than pass.
- AC12 — `grep -c "considered overlay from a mirror" .lexicon.conf tools/lexicon/README.md` — one hit in each, so the written statement that no machine check can tell a considered overlay from a mirror is present in both carriers, and deliberately ungated, because gating a sentence is how prose becomes a checkbox.
- AC13 — `tools/lexicon/selftest.py` — a stamped overlay that moves a pin — the run names the OVERLAY as the cause, observed in BOTH directions: present with the overlay, absent from a fixture that moves the same two rows without one.

**Evidences:** TOOL-aSurfacedLexicon-8
RE-KEYED onto the spec's own numbering, for the reason unit 9's block above states. The first cut
described the bare-surface menu under AC6 and the `dark` refusal nowhere, and stopped at AC8 while
the spec numbers twelve. The arms are all in one file, green at 509 arms:
`python tools/lexicon/selftest.py`.

- AC1 — `tools/lexicon/selftest.py` — `--suggest FooManager --as py.type` answers about the banned suffix `Manager`, and does NOT answer about the leading token instead, which is the branch it exited on before this unit.
- AC2 — `tools/lexicon/selftest.py` — `--suggest fetchUserData --as py.function` comes back `load_user_data`, re-cased and verb-swapped: the same name on a different cell gets a different answer, which is the whole point of the surface being an argument.
- AC3 — amended rev-6 — the criterion PASSED ON A RUN WITH THE GUARD DELETED. It asked that the message name the required flag, and the malformed-cell refusal names the same flag, so deleting the required-flag guard left it green. Re-keyed onto the wording only that guard prints, plus a second arm asserting the two neighbouring refusals are absent.
- AC4 — `tools/lexicon/selftest.py` — the re-caser over four names — including the acronym span that must survive re-casing, which is the case the original headline input never reached because the classifier already accepted it, and the `$` name refused rather than re-spelled.
- AC5 — `tools/lexicon/selftest.py` — a `file` cell re-cases the STEM of the basename, stemming at the FIRST dot so a compound extension answers unchanged, and runs no verb check at all on a cell arming neither flag.
- AC6 — `tools/lexicon/selftest.py` — a `dark` cell refuses rather than answering and exits non-zero, and the refusal is NARROW: AC9 compares it against the undeclared one.
- AC7 — `tools/lexicon/selftest.py` — `leading_verb`'s contract preserved: the underscore-only and non-ASCII names are UNGRADEABLE and nothing is re-spelled for them, while a digit-leading name is graded rather than refused.
- AC8 — `bash tools/lexicon/adopt-lexicon.sh --check` — rc 0; the rendered Skill byte-compares after the placeholder change.
- AC9 — `tools/lexicon/selftest.py` — the UNDECLARED refusal exits non-zero, names the cell and says UNDECLARED, a declaration carrying no CELLS block refuses every cell the same way, and the message is asserted TEXTUALLY DISTINCT from the `dark` one.
- AC10 — `tools/lexicon/selftest.py` — four malformed `--as` shapes, including the selector'd key that is the S9 boundary, each refuse as MALFORMED and each differs from the undeclared refusal.
- AC11 — `tools/lexicon/selftest.py` — a bare surface refuses and LISTS the declared cells carrying it and no cell on another surface, so the refusal is a menu rather than a wall, and its message differs from the malformed one.
- AC12 — `tools/lexicon/selftest.py` — the convention-only path: `buildUserIndex --as py.function` answers `build_user_index` and names the convention the input currently satisfies, which is the quiet everyday case no earlier criterion exercised.

**Evidences:** TOOL-aSurfacedLexicon-12
- AC1 — `grep -cE '^# *(RAISED |LOWERED )?[0-9]+ -> [0-9]+' .lexicon.conf` — returns 0 against the 10 the region carried, the recorded-move narration is gone, and the declaration still declares the same table: `python tools/lexicon/lexicon_conf.py --print-verbs .lexicon.conf | wc -l` prints 23.
- AC1a — amended rev-6 — AC1's line-count ceiling was STRUCK and replaced by the landing-time delta above, because deleting the pin region alone already spent the whole 77-line budget before one byte of the `PINS:` block, the `CELLS` matrix or the surviving decision comments was added. The ceiling could not be satisfied without dropping scope this unit owes. Logged in the rev-6 line of section 9.
- AC2 — amended rev-8 — the criterion claimed `--measure` emits a block of per-cell rows; it emits two scalar pin lines and no block, so nothing it claimed to compare was ever comparable. Re-keyed onto the two lines it can actually compare. Logged in the rev-8 line of section 9.
- AC3 — `grep -c "TOOL-aSurfacedLexicon" memory/DECISIONS.md` — 3, the three owed decision records, each carrying its supersession.
- AC4 — amended rev-8 — the criterion banned a superseded figure from the supersession notes, and the notes carry it deliberately, because this repo quotes a superseded claim beside its supersession and a note saying the figure did not reproduce cannot say so without naming it. Re-keyed onto the figure a note ASSERTS. Logged in the rev-8 line of section 9.
- AC5 — `grep -n "reading one of two" memory/builds/dScaffoldedMirror/README.md` — one hit, followed by its correction, and the correction records what the signal actually reports: ABOVE the threshold the kill rule watches, so the reading BREAKS the downward chain rather than continuing it.
- AC6 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — rc 0, `shipped and installed docs agree (3 pairs, rendered for 'tools/memory-tree')`. Staging the line into `memory/TEMPLATE-SPEC.md` alone made it exit non-zero first, which is the observed RED for the two-file rule.
- AC7 — `grep -c "the cell that grades it" memory/TEMPLATE-SPEC.md tools/memory-tree/SPEC-TEMPLATE.template.md` — one hit in each, so the spec-template line landed in both halves of the rendered pair.
- AC8 — `grep -n "TOOL-dClosedLexicon-2" memory/map/features/lexicon.md memory/backlog/TOOL.md` — the dossier's only BLOCKED mention is past tense (`said BLOCKED ... until`), the backlog row reads CLOSED, and the spec header still reads CLOSED. All three carriers agree.
- AC9 — `python tools/drift-audit/drift_report.py --json` — the signal is `lexicon_ratified_older_than_language_surface` and it reports `0 of 1` with `live` true and `langs_commit 672ae990` at HEAD, so the re-stamped half is observed. STATED PLAINLY: the STALE half is not observed here. That signal compares the stamp against the COMMIT DATE of the last commit touching the language line, so an uncommitted edit moves it not at all — the same limit `TOOL-aSurfacedLexicon-14`'s AC7 records for itself.
- AC10 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 over the tree with all of the above in place.
- AC11 — `grep -c 'forbidden import' coding-governance-agents.template.md AGENTS.md` — 0 on BOTH halves of the rendered pair, and the `kit:lexicon` block names the cell matrix, the convention predicate, the selector and the unfreeze stamp on both. `bash tools/playbook/adopt-playbook.sh --target . --check` exits 0 with `region matches a fresh render, no placeholder survived`, which is what proves the rendered half was regenerated rather than hand-edited, and `bash tools/check-placeholders.sh` stays green.
- AC12 — `bash tools/check-template-size.sh` — 49032 / 49152 bytes, 120 under the ceiling, against the 49038 the same file carried immediately BEFORE the S11 edit (`git show 2d487019:coding-governance-agents.template.md | wc -c`). Below, not merely at, and the `OK` line still reports a non-negative margin.
- AC12a — `bash tools/check-template-size.sh AGENTS.md` — 64394 / 64512 bytes, 118 under, against 64400 before the S11 edit (`git show 2d487019:AGENTS.md | wc -c`). This is the BINDING reading of the pair, and it is net-negative by the same six bytes.
- AC12b — `bash tools/check-template-size.sh` — both WARN lines recorded as context and NEITHER graded: `TEMPLATE-SIZE WARN — coding-governance-agents.template.md grew past its recorded high-water: 48378 -> 49032 (+654)` and `TEMPLATE-SIZE WARN — AGENTS.md grew past its recorded high-water: 60930 -> 64394 (+3464)`. The tree warns on a clean checkout, so a criterion forbidding the WARN would have required this unit to shrink the charter by 654 bytes that nothing in its scope proposes.
- AC13 — `.lexicon.conf` — the committed `PINS:` block carries `py.file.conv` and `sh.function.conv` separated by exactly one blank line, and `python tools/lexicon/lexicon_conf.py --print-verbs .lexicon.conf` still parses the file at 23 rows.
- AC14 — `git show 672ae990 -- tools/lexicon/lexicon.py | grep -c '^+UNDECLARED_CELL_ARMED = True'` — 1, so the arming constant landed in that commit, and the same commit adds the five `CELLS` matrix rows and the paragraph declaring the matrix full. STATED PLAINLY: the criterion's OTHER command, `git show 672ae990 -- .lexicon.conf | grep -q '^+CELLS:'`, returns 0 and does NOT reproduce — the `CELLS:` header itself predates that commit, having landed at `2d487019` with `sh.function`, so what the arming commit adds is the matrix ROWS under an existing header. The two-landing-separately failure the criterion exists to catch did not occur; the command written to detect it is keyed on a line that was never going to be added.

## What the revert matrix found in this pass

**Seventeen mechanisms across this build were UNGATED when first written** — reverting each left a
fully green suite. This pass alone found ten, and the most serious was the canon door's entire
RECORDED half: replacing one row-count guard with a constant false deleted BOTH stamp refusals, and
nothing noticed. The build's own rule is that an unfreeze must be visible and recorded, so the
mechanism enforcing the record was the one mechanism that must not be silently removable.

**Two arms passed for the wrong reason**, which is worse than absent. One asserted a refusal by
grepping for a flag name that a NEIGHBOURING refusal also prints, so it stayed green on a run with
the guard deleted. Another asserted only that the word "line" appeared, which meant five sibling
refusals looked covered while a sixth had no fixture at all — any one firing satisfied any row.

**And removing a refusal does not always make a reader permissive; sometimes it makes the next line
crash.** Two staged breaks produced an unpacking error and an index error rather than a silent pass.
An arm catching only the domain error would have let those propagate and redded the suite with a
traceback naming the reader instead of the arm that knows which check went missing.

## The structural finding, filed rather than fixed

Every one of those seventeen was a PYTHON branch, and the kit's shell files are armed and clean
throughout. That is not a difference in discipline: `check-arms.py`, the meta-gate for unarmed refusal
branches, discovers its population as tracked shell files, so a Python refusal is outside it **by
construction** — not waived, not exempted, invisible. A reader who trusts that gate reads green over a
population it never scanned, which is the green-by-absence class inside the checker written to prevent
it. Filed as `TOOL-aSurfacedLexicon-21` with the shape of a fix and the reason it is not a one-liner.
