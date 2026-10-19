**Serves:** diff-review TOOL-dRenderedAnchor-1

# Closing diff review, round 1: dRenderedAnchor unit 1, the resolver's rendered-row join and the misplaced-harness red

2026-10-19 · Tier-2 · on `branch/frosty-feistel-42acd4` · adversarial fan through `tier2-review.js`: 5 finder lenses, then 4 skeptic batches, then this synthesis. Unit TOOL-dRenderedAnchor-1, spec rev-1. The diff widens the receipt join in `tools/lib/resolve_kit_dir.py` and its 70 inline copies, adds `scan_misplaced_harnesses` and `MISPLACED_LINE` to `tools/roles/render_agents.py`, adds selftest arms 16 and 17, and updates the docs.

**Reviewed range:** `a60b0c7dcce48d090d7b5b8278e58e1bc2f4bdad...033b15f240f740fdd3df219d94f8fc42bcaf7420`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. The widened join gives the right answer on every caller the reviewers traced, and the new red catches the misplaced index it was built for. Three defects still need fixing before the close.

- The misplaced scan matches on file name alone. Under the owner-ruled accepted absence, an adopter's own `tier2-review.js`, `unattended-build.js` or `unattended-unit.js` turns the note into a red on the merge bar.
- No gate can fail on either guard term of the widened join.
- The join also changes the answer of the `{{TOOL_ROOT}}` citation resolvers. The spec says no such caller exists, and nothing observes the change.

The rest is wording and orientation text.

## Review shape

Intensity **full** · raw **12** · confirmed **10** · refuted **2** · unverified **0** (0 uncertain) · precision **0.83**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| seams | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

The 10 confirmed findings collapse to **8 items**. I made the merges when writing this report, and each one joins findings of a single binding grade:

- ids 5 and 8 are one defect: the join's guard terms are ungated.
- ids 4 and 9 are one defect: the citation resolvers' changed answer is unrecorded and unobserved.

Two findings describe the same defect as a MEDIUM item but carry a LOW binding grade, so each is an item of its own that points back:

- Id 7 is the namesake false red of M1, seen from the root-install side.
- Id 10 is the spec-table omission of M3.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 3 MEDIUM · 5 LOW** (8 items).

Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 5 LOW** (10 findings).

Every id keeps its bracketed binding grade. I would grade id 7 MEDIUM alongside id 1, because it is the same false red on the merge bar and only its trigger is narrower. The grade binds, so it stays LOW.

The two refuted findings (2, 3) are listed with their reasons in the appendix and are not re-adjudicated here.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **4/4** returned, **0 DIED**.
- The pipeline demoted **0** contradictory verdicts to unverified, discarded **0** spurious verdicts and removed **0** duplicates.
- Fixes on confirmed findings: **9** judged sound, **1** judged UNSOUND (id 1), **0** none proposed, **0** NOT JUDGED.
- Severity on confirmed findings: **0** ungraded by the skeptic, **0** re-graded by the skeptic.
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders ran as gov-diff-reviewer, the skeptic batches as gov-skeptic, and this synthesis as gov-synthesizer.
- Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 16 items, each assigned to exactly one of 5 lenses (security 4, correctness 3, seams 3, verification 3, intent 3).
- By design: the caller's byDesign.

Every stage returned and every counter above that could mark a hole is zero, so this run is complete. A zero in this report is evidence of absence, not a gap.

This synthesis re-executed none of the findings. Each item rests on the finder's probe and the skeptic's verification, as cited.

## MEDIUM

### M1. The misplaced scan reds the merge bar on any namesake file, including when review-harness is not installed (id 1)

- **Where:** `tools/roles/render_agents.py:166-177` (`scan_misplaced_harnesses`). `run_mode` prints the red and returns `1 if misplaced` under `--check` (`:264-280`).
- **Defect:** the scan treats a harness as misplaced whenever a file with the same basename sits directly inside any directory under the tool root. It never checks that review-harness wrote that file. The skeptic's repro used a scratch tree with `.git/`, `tools/roles/` and an adopter-owned `tools/ci/tier2-review.js`. It returned `{'tools/workflows/tier2-review.js': ['tools/ci/tier2-review.js']}`.
- **Impact:** owner ruling 2026-10-19 makes "review-harness not installed" an accepted absence: a note and exit 0. Under that absence, an adopter file named `tier2-review.js`, `unattended-build.js` or `unattended-unit.js` turns the note into `misplaced … is installed; the kit resolver did not find it`. The `roles render wiring` leg then reds the adopter's merge bar and blames a kit the adopter may legitimately leave out. Re-rendering cannot clear the red. The adopter can only rename its own file or install the optional kit. Adopters who keep hand forks of the harnesses, which the review-harness `kit.toml` records, are the likely population.
- **Fix:** the skeptic judged the finder's fix UNSOUND. This is the skeptic's corrected fix:
  - Narrow the scan to files that review-harness could have installed, and keep reading the disk, not the receipt.
  - Count a hit only when the same directory also holds the harness's template `<stem>.template.js`. govkit ships the templates beside their renders under the `**` engine rule, as the repro's install shows.
  - For an engine harness with no template (`unattended-unit.js`), count a hit only when that directory's `kit.toml` declares `id = "review-harness"`.
  - In the same change, plant `a.template.js` (or that `kit.toml`) beside `a.js` in arm 17's renamed directory, so the arm keeps reading `misplaced`.
  - Add arm 18: an unrelated namesake in a directory with neither marker and no receipt must print the note and exit 0. Observe arm 18 RED against the current scan first.
- **Left-shift:** arm 18 is the gate for this item. Add a bug-class checklist entry, "a guard that names a defect by file name alone must show the file is the kit's own before it reds", under the `name-search-resolves-a-namesake` class.

### M2. Neither guard term of the widened join has a gate that can fail (ids 5, 8)

- **Where:** the canonical block in `tools/lib/resolve_kit_dir.py` and its 70 inline copies. The only exercising fixture is arm 16 at `tools/roles/render_agents.py:542-568` (cited at `:546` and `:551`).
- **Defect:** the join is `made = role=='rendered' and basename(path)==anchor`, and it skips a row `if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home])`. Arm 16's receipt holds one row, a `rendered` row whose source sits under the correct home. Every weakened predicate also joins that row. Arm 17 writes no receipt. Section 1 of `tools/lib/resolve-python.test.sh` tests `resolve_python` only, and its parity table compares the 71 copies only with each other. The S5 parity arm in `check-wiring.test.sh` (`:1710-1724`) passes only non-rendered anchors. Spec §4's six-row table and AC2 (spec `:326-331`) were a one-time scratch probe.
- **Impact:** both finders' probes ran the shipped block and two mutants on arm 16's fixture, and all three returned `toolroot/renamed`.
  - With `row.get("role") == "rendered"` dropped, a `merged` row (`.claude/s.json` from `hooks/s.fragment.json`) resolves `('hooks', 's.json')` to `.claude`.
  - With `src[-2:-1] == [home]` dropped, a rendered row from another kit's template resolves to `.claude`.
  - Either regression would land in all 71 copies with the `roles render selftest`, the parity table and the `python resolver` leg green. The shipped code is correct today, so the exposure is to future regressions.
- **Fix:** both skeptics judged the fixes SOUND. They are merged here.
  - Add decoy rows to arm 16's `install.json`, each backed by a real file on disk:
    - a `merged` row whose path basename is `a.js` (for example `.claude/a.js`, source `{prefix}/workflows/a.fragment.json`);
    - a `rendered` row with path `.claude/a.js` and source `{prefix}/other/a.template.js`.
  - Put both decoys before the real row so receipt order cannot hide them. Assert that `harnesses` is still the `renamed` path.
  - Better still, add a `resolve_kit_dir` behaviour arm to `tools/lib/resolve-python.test.sh` that replays spec §4's six rows.
  - Observe the new arm RED with the role term dropped, and separately with the home term dropped.
- **Left-shift:** the behaviour arm in `resolve-python.test.sh` is the gate, and the `python resolver` leg already runs that file. Add a checklist entry, "every term of a join predicate needs a fixture row that only that term rejects", under `fixture-passes-by-finding-nothing` and `staged-break-substitutes-a-synthetic-value`.

### M3. The widened join changes what the `{{TOOL_ROOT}}` citation resolvers return, and the spec's callers table leaves them out (ids 4, 9)

- **Where:**
  - Spec `memory/builds/dRenderedAnchor/spec/2026-10-19-spec-TOOL-dRenderedAnchor-1.md:136-152` ("Which callers move", line 139).
  - The repro record's line 79 ("the role render is the only one today").
  - The dynamic callers: `tools/lib/render-doc.sh:160-171` (`derive_kit_paths`, cited at `:166`), `tools/memory-tree/adopt-memory-tree.sh:270-282`, `tools/memory-tree/kit-dogfood-parity.test.sh:198-210`.
  - The literal call `WF_DIR=$(resolve_carrier_kit workflows tier2-review.js)` at `tools/check-kit-versions.sh:125`, which `govkit.py:2186-2190` scrapes and re-resolves.
- **Defect:** the spec says the table is enumerated "over every literal resolve_kit_dir call" and that "Only these pass a rendered anchor". It lists five callers.
  - It misses `check-kit-versions.sh:125`.
  - It misses the three citation loops. Each loop calls `resolve_kit_dir(home, anchor, kit)` for every `{{TOOL_ROOT}}<home>/<file>` in the templates, and falls through to the bare prefix substitution on `LookupError`.
  - These templates cite `{{TOOL_ROOT}}workflows/tier2-review.js` and `unattended-build.js`: `BUILD-METHOD.template.md:134/223/225/262`, `workflows/REVIEW-PROTOCOL.template.md:34/202`, `roles/SKILL.template.md:45/76` and `unattended/SKILL.template.md:125`.
  - `tools/workflows/kit.toml:76-78` renders those harnesses from templates under `workflows/`.
- **Impact:** in an adopter with a receipt, those citations now resolve to `<prefix>/review-harness/…`. Before, they fell through to the dead `<prefix>/workflows/…`. One probe ran both blocks on the real rendered row: the base gave `LookupError -> tools/workflows/tier2-review.js` and the tip gave `tools/review-harness/tier2-review.js`. Every adopter's rendered BUILD-METHOD.md, REVIEW-PROTOCOL.md and SKILL pages change bytes on the next memory-tree render. The output also depends on whether the review-harness row is already in the receipt when memory-tree renders. The change is a correction, but no AC, arm or ledger entry observes it. The next change to the join will trust a callers table that is missing rows.
- **Fix:** both skeptics judged the fixes SOUND. They are merged here.
  - Correct the spec's callers table, or add a rev-2 note. Add rows for the citation resolvers in `render-doc.sh`, `adopt-memory-tree.sh` and `kit-dogfood-parity.test.sh`, for the doc templates whose citations now resolve differently, and for `check-kit-versions.sh`'s `WF_DIR`. Fix the repro record's line 79 the same way.
  - Add an arm to the memory-tree render suite, or a `derive_kit_paths` arm in `tools/lib/resolve-python.test.sh`. Its fixture receipt carries a rendered review-harness row at `<prefix>/review-harness/tier2-review.js`. It asserts that `derive_kit_paths` emits `{{TOOL_ROOT}}workflows/tier2-review.js<TAB><prefix>/review-harness/tier2-review.js`. Observe it RED with the a60b0c7d block.
  - Observe whether `govkit update` reports the re-rendered guides as drift in an existing adopter, and record the answer in the ledger.
- **Left-shift:** the `derive_kit_paths` arm is the gate. Add a checklist entry: "a resolver change's callers table enumerates dynamic callers (loops over template citations), not only literal calls". Record it under `decision-re-derived-by-a-second-process`.

## LOW

### L1. At a root install, the misplaced scan covers every top-level directory of the adopter's repo (id 7)

- **Where:** `tools/roles/render_agents.py:166-177`, and spec §4 "One level, and why".
- **Defect:** this is M1's defect seen from another side. The scan never checks that a directory is a kit dir. At a root install (`KIT_REL` `roles`, an empty prefix, which govkit supports), the tool root is the repo root, so every top-level adopter directory is scanned. `git ls-files` shows that no gov kit other than `tools/workflows/` carries a file with any of the three harness names. With review-harness absent, any hit is therefore the adopter's own file. The spec assumes every directory under the tool root is a kit dir and never covers namesakes or root installs.
- **Impact:** a false `--check` exit 1 on the `roles render wiring` leg, in a case the owner ruled should be a note. The printed remedy (`--scaffold`) cannot clear it. The trigger is narrow, because the adopter needs a file with exactly that name directly in such a directory.
- **Fix:** judged SOUND. Count a hit only when the directory is a govkit-installed kit dir, for example when a `kit.toml` sits beside the file or the directory is named after a registry id. Keep the read on disk so it shares no state with the resolver. Add a selftest arm with a namesake in a non-kit directory, and assert `NOTE_LINE` and exit 0. M1's corrected fix (template sibling, or a `kit.toml` declaring `id = "review-harness"`) meets this requirement, so land both in one change and reuse arm 18. Also add a root-install variant of arm 18.
- **Left-shift:** arm 18, run once with a prefix and once at the root. Amend spec §4 to state the root-install case.
- **Grade note:** I would grade this MEDIUM with id 1, since it is the same false red. The binding grade is LOW.

### L2. The spec's callers table says no rendered-anchor caller exists beyond its five literal calls (id 10)

- **Where:** spec `memory/builds/dRenderedAnchor/spec/2026-10-19-spec-TOOL-dRenderedAnchor-1.md:136-150` (line 138), and §5's claim that "the callers table shows each one wants it".
- **Defect:** this is the record half of M3. The table leaves out the three citation loops (`tools/lib/render-doc.sh:168`, `tools/memory-tree/adopt-memory-tree.sh:280`, `tools/memory-tree/kit-dogfood-parity.test.sh:208`). `git grep -n 'TOOL_ROOT}}workflows/\(tier2-review\|unattended-build\)'` prints `BUILD-METHOD.template.md:134`, `:223` and `:262`, and those citations now resolve to `tools/review-harness/`.
- **Impact:** the blast-radius record is incomplete. Behaviour is correct.
- **Fix:** judged SOUND. Add rows, or a rev-2 note, for the three dynamic citation callers. Name BUILD-METHOD.template.md's harness citations as rendered anchors they now resolve. Add a probe that runs `derive_kit_paths` over BUILD-METHOD.template.md on the AC4 scratch install, and record that both citations print `tools/review-harness/` paths. M3's arm makes this probe a standing gate, so one change satisfies both items.
- **Left-shift:** the same as M3.

### L3. Only `render_agents --check` says `misplaced`, while help/roles.md implies every tool does and check-wiring calls the same install ok (id 6)

- **Where:** the roles arm in `tools/check-wiring.sh:1735-1748` (cited at `:1743`), and `help/roles.md:131-133`.
- **Defect:** check-wiring's SessionStart roles arm reads the same `roles.json`. For a listed harness that is not a file, it prints `note … absent here; /build cannot drive it until the review harness is installed` and then `ok roles`, with no namesake scan. The diff leaves that arm unchanged. The new help text follows "each tool prints a note naming the missing harness" with "reads `misplaced` instead", which implies every tool does. Only `render_agents.py`, and the leg and `adopt-roles --check` that run it, print `misplaced`.
- **Impact:** take a receipt-less or hand-copied review-harness under a renamed kit dir. The merge-bar leg reds it as misplaced. The session-start report says ok and asks the user to install a kit that is already installed. The diagnoses conflict, but no gate gives a wrong verdict.
- **Fix:** judged SOUND. Have check-wiring's roles arm apply the same one-level namesake test, with the marker narrowing from M1, and print UNWIRED/misplaced instead of the note. Otherwise, reword `help/roles.md:131-133` to say that only `render_agents.py`, and the leg that runs it, reports `misplaced`.
- **Left-shift:** if the arm gains the test, add a check-wiring.test.sh fixture that pins both readers to the same verdict on one misplaced tree. Otherwise add a checklist entry, "a new verdict names every reader of the same index that does not share it", under `invariant-held-on-one-admission-path`.

### L4. The roles feature map still says an absent harness is never a defect (id 11)

- **Where:** `memory/map/features/roles.md:100-102` (line 101), its decisions list (line 8) and its receipt-contract bullet (line 139).
- **Defect:** the map claims `tools/roles/**` and still says "A well-formed harness the tree does not hold is a note, not a defect". The decisions list has no TOOL-dRenderedAnchor-1. The receipt contract describes only `source` and `path` and does not mention the new `role == 'rendered'` join. The diff's only map change is `generated/symbols.json`.
- **Impact:** the orientation page gives the opposite answer to the render's docstring, `tools/roles/README.md` and `help/roles.md`. An agent that reads the map first will treat a misplaced red as a regression of the "note, not a defect" decision.
- **Fix:** judged SOUND. Amend the paragraph: a harness found nowhere stays a note, and one found in another directory directly under the tool root is `misplaced` and reds `--check`. Add TOOL-dRenderedAnchor-1 to the decisions list. Extend the receipt-contract bullet to say the join also matches a `rendered` row on its `role`, its template's home and its path's file name. Write the paragraph after M1's narrowing lands, so it states the final rule.
- **Left-shift:** add a checklist entry: "a unit that changes a dossier-claimed path's documented rule edits that feature map in the same diff". Record it under `two-answers-to-one-question`.

### L5. help/roles.md and the MISPLACED_LINE comment say "kit directory" and "is installed", but the scan checks neither (id 12)

- **Where:** `help/roles.md:131-133` ("sits in another kit directory"), the comment above `MISPLACED_LINE` at `tools/roles/render_agents.py:80` ("sits in a kit directory"), the line's own text (`%s is installed`), and the docstring at `render_agents.py:37` ("installed elsewhere").
- **Defect:** `scan_misplaced_harnesses` keeps any directory under the tool root that passes `d.is_dir()` and `(d / name).is_file()`. `tools/roles/README.md` correctly says "directly inside a directory under the tool root", so the pages answer one question two ways.
- **Impact:** a reader who hits the red from an adopter-owned `tools/<dir>/tier2-review.js` is told it can only come from a kit directory, and cannot find the cause from the docs.
- **Fix:** judged SOUND. Use the README's and the docstring's wording in help/roles.md and the comment: "a file of its name directly inside any directory under the tool root". Change "is installed" to "is present" in `MISPLACED_LINE`, and change "installed elsewhere" in the docstring to match. No selftest string-matches "is installed". Otherwise, restrict the scan to kit directories as M1 and L1 do, and state that rule in all four places. Once M1's narrowing lands, the restricted wording is the accurate one, so write the wording to match whichever scan ships.
- **Left-shift:** add a checklist entry: "a printed verdict line and its help text name the scan's actual predicate". Record it under `two-answers-to-one-question`.

review-shape kind=diff-review round=1 intensity=full at=synth raw=12 confirmed=10 refuted=2 unverified=0 blocker=0 high=0 medium=5 low=5 agents=10 out-tokens=157007

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/roles/render_agents.py:166 | medium | medium | confirmed | Confirmed against the code and by a repro. scan_misplaced_harnesses (tools/roles/render_agents.py, the function this diff adds) matches on basename only. It keeps any directory d directly under tool_root for which d/<name> is a file, and it never checks that the file is review-harness's. I built a scratch tree with .git/, tools/roles/ and an adopter's own tools/ci/tier2-review.js, and the call returned {'tools/workflows/tier2-review.js': ['tools/ci/tier2-review.js']}. run_mode then prints MISPLACED_LINE in place of NOTE_LINE, and under --check returns `1 if misplaced`. So in the case the owner ruled an accepted absence (review-harness not installed), a namesake the adopter owns turns the note into a red on the `roles render wiring` leg. The red blames the resolver, and re-rendering cannot clear it. The adopter-tool-root shape is real: the tool root is govkit's <prefix>, and an adopter can keep its own directories there. The red is visible and stops nothing silently, so this is medium. | unsound | name-search-resolves-a-namesake |
| 2 | correctness | tools/lib/resolve_kit_dir.py:39 | medium | - | refuted | The predicate does accept rendered rows whose `to` sits outside {kit} (memory/guides/*, .claude/skills/*/SKILL.md). But no caller in the tree reaches that, and the finder itself says so. I checked the data-driven callers the finding names. No template carries a {{TOOL_ROOT}}<home>/<anchor> citation naming SKILL.md, REVIEW-PROTOCOL.md or any guide basename (grep across tools/, skills/ and the root .md files returned nothing). No kit.toml uses must_not_resolve. workflows.toml lists only .js harnesses. check-kit-versions' resolve_carrier_kit lines name in-kit anchors, and WF_DIR (workflows, tier2-review.js) now joins correctly. The finding also overstates the consequence. In the one data-driven scanner, derive_kit_paths in render-doc.sh, a hypothetical citation like {{TOOL_ROOT}}workflows/REVIEW-PROTOCOL.md would now render memory/guides/REVIEW-PROTOCOL.md, where the file actually is, instead of the absent tools/workflows/ path. That is not a wrong answer. With no reachable path, and a medium grade, the finding is refuted. | unsound | join-key-widened-by-a-shared-location |
| 3 | seams | tools/roles/SKILL.template.md:76 | high | - | refuted | This defect is pre-existing and the diff leaves it unchanged. git diff over the range does not touch tools/roles/SKILL.template.md, tools/roles/adopt-roles.sh or tools/unattended/SKILL.template.md. adopt-unattended.sh changes only inside its inline resolve_kit_dir copy. At base, adopt-roles.sh already rendered the /build Skill's harness citations by plain `${out//{{TOOL_ROOT}}/"$TOOL_ROOT"}` substitution, so the Skill already named tools/workflows/tier2-review.js and tools/workflows/unattended-build.js, which do not exist in an adopter that installs review-harness at tools/review-harness/. At base, agent-cap admitted that scriptPath (the index listed tools/workflows/*) and the Workflow call then failed on the absent file. After the diff, agent-cap denies it first. The /build call failed before and fails now; only the failing step moved. The spec's goal (§1, AC4) is the role index and the resolver, and it never claims the Skill. This is a real follow-up, but the diff did not introduce it. | sound | decision-re-derived-by-a-second-process |
| 4 | seams | memory/builds/dRenderedAnchor/spec/2026-10-19-spec-TOOL-dRenderedAnchor-1.md:139 | medium | medium | confirmed | Spec line 139 says 'Enumerated over every literal resolve_kit_dir call ... Only these pass a rendered anchor' and lists five callers. That is wrong in two ways. First, tools/check-kit-versions.sh:125 has a literal `WF_DIR=$(resolve_carrier_kit workflows tier2-review.js)`, which goes through its inline resolve_kit_dir. govkit.py:2186-2190 scrapes and re-resolves that line. Second, the citation resolvers in tools/lib/render-doc.sh:160-171, adopt-memory-tree.sh:270-282 and kit-dogfood-parity.test.sh:198-210 call resolve_kit_dir(home, anchor, kit) for every `{{TOOL_ROOT}}<home>/<file>` in the templates. On LookupError they `continue`, falling through to the prefix line. I grepped the templates. BUILD-METHOD.template.md:134/223/225/262, roles/SKILL.template.md:45/76, unattended/SKILL.template.md:125 and workflows/REVIEW-PROTOCOL.template.md:34/202 cite {{TOOL_ROOT}}workflows/tier2-review.js and unattended-build.js. tools/workflows/kit.toml:76-78 renders tier2-review.template.js to {kit}/tier2-review.js, so its receipt row's source sits under workflows/ and its path's basename is the anchor. The widened join therefore now resolves these citations to <prefix>/review-harness/... in an adopter that has a receipt. Before, they fell through to the prefix spelling <prefix>/workflows/... The rendered docs change bytes. A grep of the spec, brief and build records for citation/BUILD-METHOD/derive/WF_DIR finds nothing, so no AC or record covers it. The behaviour change is itself a correction, so the consequence is contained to an inaccurate blast-radius record. That makes it medium. | sound | decision-re-derived-by-a-second-process |
| 5 | seams | tools/roles/render_agents.py:546 | medium | medium | confirmed | render_agents.py:542-568 (arm 16) writes a receipt with exactly one row: role 'rendered', with its source FIXTURE_HARNESS.template.js under the correct home and its path the held file. The canonical block in resolve_kit_dir.py is `made = role=='rendered' and basename(path)==anchor; skip if src[-2:]!=[home,anchor] and not (made and src[-2:-1]==[home])`. Delete the role term and arm 16 still returns the renamed directory. Delete the home term and it does too, so neither mutant reds the arm. I searched the tests and selftests for a receipt fixture with a 'merged' row, or a 'rendered' row under another home, that is fed to the resolver. Only govkit.py itself has 'merged' rows. The parity table in resolve-python.test.sh checks byte identity only. The acceptance ledger records AC2, the six-row table, as a one-time %TEMP% probe and not as a gated arm. Both guard terms are therefore ungated across all 71 copies. Nothing ships a wrong result today, so the effect is contained. | sound | fixture-passes-by-finding-nothing |
| 6 | seams | tools/check-wiring.sh:1743 | low | low | confirmed | At check-wiring.sh:1735-1748 the roles arm reads roles.json's harnesses. For any listed harness that is not a file, it prints 'note ... absent here; /build cannot drive it until the review harness is installed' and then 'ok roles'. That arm is unchanged by the diff and has no namesake scan. The help/roles.md text that this diff added (lines 131-133) follows 'each tool prints a note naming the missing harness' with 'reads `misplaced` instead'. That implies every tool does, but only render_agents.py, and the leg and adopt-roles --check that run it, prints misplaced. In a misplaced state (receipt-less or hand-copied, renamed kit dir), the merge-bar leg reds while the SessionStart report says ok and asks for an install that is already there. This is a doc overstatement plus a diagnostic inconsistency on a narrow path, with no wrong gate verdict, so low. | sound | invariant-held-on-one-admission-path |
| 7 | seams | tools/roles/render_agents.py:166 | low | low | confirmed | tools/roles/render_agents.py:166-177 lists every `d` in `tool_root.iterdir()` that is a directory and holds a file named like the harness. It never checks that `d` is a kit dir. At a root install (KIT_REL 'roles', which govkit supports: the census.test.sh, selftest.py and matrix.py PFX logic reads an empty prefix as a root install), the tool root is the repo root, so every top-level adopter directory is scanned. run_mode (lines 264-280) prints MISPLACED_LINE and `--check` returns 1 for any hit. No gov kit other than tools/workflows/ carries a file named tier2-review.js, unattended-build.js or unattended-unit.js (git ls-files shows each once), so a hit with review-harness not installed can only be the adopter's own file of that name. That is a false red on a case the owner's ruling makes a note. Spec §4 'One level, and why' assumes every directory under the tool root is a kit dir and never covers namesakes or root installs. The path needs an adopter file with exactly that name directly in such a directory, so the case is narrow. The consequence is a false red, contained, and a re-render cannot clear it. | sound | - |
| 8 | verification | tools/roles/render_agents.py:551 | medium | medium | confirmed | Arm 16 (render_agents.py:546-566) writes exactly one receipt row, with role 'rendered' and source '{prefix}/workflows/a.template.js'. Under the shipped predicate (resolve_kit_dir.py), dropping `row.get("role") == "rendered"` still joins that row, and so does dropping `src[-2:-1] == [home]`. Either way the arm passes. Arm 17 writes no receipt. The resolver suite's section 1 (tools/lib/resolve-python.test.sh) exercises resolve_python only, and its parity section compares the copies with each other. The check-wiring.test.sh S5 parity arm (1710-1724) passes only non-rendered anchors (merge-rows.py, scratch-guard.fragment.json, recall-opened.fragment.json) over a receipt whose merged rows have other basenames, so it cannot catch either regression. Spec §4's six-row table and AC2 (spec:326-331) are a one-time in-process probe, not a gate. So no gate can fail on the role term or the home term. The shipped code is correct today, so the effect is contained to future regressions going unseen. | sound | staged-break-substitutes-a-synthetic-value |
| 9 | verification | tools/lib/render-doc.sh:166 | medium | medium | confirmed | tools/lib/render-doc.sh:162-170 (derive_kit_paths, also copied in adopt-memory-tree.sh:274-283) runs resolve_kit_dir(home, anchor, kit) for every `{{TOOL_ROOT}}<home>/<file>` cite in the templates. A LookupError means the cite is not emitted, so it falls through to the bare `{{TOOL_ROOT}}` prefix substitution (render-doc.sh:52 and 265). The shipped templates cite these harnesses: BUILD-METHOD.template.md:134, 223, 225 and 262, REVIEW-PROTOCOL.template.md:34 and 202, roles/SKILL.template.md:45 and 76, and unattended/SKILL.template.md:125. In an adopter with a rendered review-harness row, the widened join now emits tools/review-harness/... where the base fell through to tools/workflows/.... That changes the rendered bytes of adopter docs. The change goes the right way, since the old path was dead, but it is unobserved. Spec §4 'Which callers move' (lines 136-152) lists only literal-anchor calls and says the guides 'render to {memory_root}/ ... and no call names them', which misses this caller. The repro record's line 79 says 'role render is the only one today'. No arm, AC or ledger entry exercises derive_kit_paths with a rendered row. This is a real verification and documentation gap on a shipped behaviour change. Its effect is contained, because the new output is the correct one. | sound | - |
| 10 | intent | memory/builds/dRenderedAnchor/spec/2026-10-19-spec-TOOL-dRenderedAnchor-1.md:138 | low | low | confirmed | Confirmed. In the spec, the 'Which callers move' section (lines 136-150) is enumerated 'over every literal resolve_kit_dir call' and says 'Only these pass a rendered anchor'. Its five rows leave out the dynamic citation loops at tools/lib/render-doc.sh:166-170, tools/memory-tree/adopt-memory-tree.sh (same loop, line ~280) and tools/memory-tree/kit-dogfood-parity.test.sh:206-210. Each of these splits every `{{TOOL_ROOT}}<home>/<file>` match into (home, anchor) and calls resolve_kit_dir. The probe git grep prints tools/memory-tree/BUILD-METHOD.template.md:134 and :223 (and :262), all citing workflows/tier2-review.js or workflows/unattended-build.js. tools/workflows/kit.toml declares home=workflows and renders the build harness from its template. So in an adopter the new `made and src[-2:-1]==[home]` arm in resolve_kit_dir now matches the rendered row and emits tools/review-harness/... for those citations. Before, it hit LookupError, the citation was skipped, and the generic prefix substitution applied. No other place in the spec names these callers or BUILD-METHOD's citations. The behaviour change is a correction, so the consequence is limited to an incomplete blast-radius record. That makes it low. | sound | - |
| 11 | intent | memory/map/features/roles.md:101 | low | low | confirmed | Confirmed. memory/map/features/roles.md claims tools/roles/** in its [paths] block. Line 101 still says 'A well-formed harness the tree does not hold is a note, not a defect'. The diff now makes run_mode in tools/roles/render_agents.py print MISPLACED_LINE and return 1 under --check when an absent harness has a namesake under the tool root, so the map answers one way and the render's docstring, README and help/roles.md answer the other. The decisions list (line 8) has no TOOL-dRenderedAnchor-1. The receipt-contract bullet says only 'rows naming a kit's source and installed path' and does not mention the new role=='rendered' join. The diff's only memory/map change is generated/symbols.json, so the dossier was not touched. Behaviour is unaffected; the effect is orientation text, which makes it low. | sound | two-answers-to-one-question |
| 12 | intent | help/roles.md:132 | low | low | confirmed | Confirmed. help/roles.md:131-133 says a namesake 'sits in another kit directory'. The comment above MISPLACED_LINE (render_agents.py:80) says 'sits in a kit directory', and the line itself says '%s is installed'. scan_misplaced_harnesses (render_agents.py:166-177) keeps any d under tool_root with d.is_dir() and (d / name).is_file(). It never checks that d is a kit (no kit.toml or receipt test), which the spec's own wording at lines 162-167 matches. tools/roles/README.md says 'directly inside a directory under the tool root', so the pages give two answers to one question. The red on an adopter's own tools/<dir>/tier2-review.js follows from the design the spec chose. The finding's defect is that the docs mislead about the cause, so it is low. On the fix: changing the wording in help and the comment, plus 'is installed' -> 'is present', cures it, and no selftest string-matches 'is installed' (grep finds only the constant and the docstring). The docstring at render_agents.py:37 also says 'installed elsewhere' and should get the same word. The kit.toml-restriction alternative is also viable, since kit.toml rows land in receipts. | sound | two-answers-to-one-question |
