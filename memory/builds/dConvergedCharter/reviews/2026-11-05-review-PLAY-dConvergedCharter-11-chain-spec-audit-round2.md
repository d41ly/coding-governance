**Serves:** spec-audit PLAY-dConvergedCharter-11@rev-7 PLAY-dConvergedCharter-17@rev-4 PLAY-dConvergedCharter-38@rev-3 PLAY-dConvergedCharter-41@rev-3 PLAY-dConvergedCharter-20@rev-6 PLAY-dConvergedCharter-21@rev-4 PLAY-dConvergedCharter-13@rev-5 PLAY-dConvergedCharter-40@rev-2 PLAY-dConvergedCharter-7@rev-5 PLAY-dConvergedCharter-9@rev-5

# Tier-2 spec audit: dConvergedCharter, ten chain units (11, 17, 38, 41, 20, 21, 13, 40, 7, 9), round 2

*This is an adversarial pre-code pass over the round-4 fold of ten spec units of the Convergence build. The build has no run-mandate prompt, so the README is the mandate: close the owned gaps, one roster unit per clause. Synthesised by gov-synthesizer on 2026-11-05. Every item below survived a skeptic who was prompted to refute it.*

Reviewed: memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md@850c591bdd1c12adde0b9a84a8c0db3cd7b2e154, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md@bd22cdb6557c9f4424b1bcc7b7eb74b091a95df6, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-38.md@1e4a990f4926ef9842a85cb4f25f2e22864b7636, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md@8d8fd6c248d6ae80822bf520213fadd69061aaf3, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md@2661e677870734a58d811dbe82f9e944a05e911e, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md@802ae9c5a59b10787928c83fe49599a9cdaaf73f, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md@b60f52304db231355e53dab9b64c6c9fe6aa32ee, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-40.md@2db0c2b879e36faf93f38efea8d0a25f24fc1118, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md@360a68c5ce73d5baf0aeaac66007fcd86fb0b474, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md@8f6cf2ddb6a1841bbf8999b57160deebc9dd33f3

ROUND: 2

## Verdict: CLEAN WITH FIXES

No item is a blocker.

Seven HIGH items cover nine findings, and each must be fixed before the build pass:

- Unit 11 gives `adopt-codebase-map.sh`'s walk a stop condition that a first adoption can never meet (H1).
- Unit 11's and unit 41's typed list of legs guarding the policy kit leaves out legs whose suites now run it (H2).
- Seven legs still select themselves by a folded home's path, not by `.governance/policy.toml` (H3).
- Unit 11's AC32 cannot see the multi-line and `${conf}` carriers S4 re-words (H4).
- Unit 11's AC33 misses the house `.get(key, default)` spelling and is green at base (H5).
- Kits with `requires = []` get readers that need the policy kit, with no absent-kit behaviour (H6).
- Unit 9's DOWN restores the old render whatever the UP did, overwriting a kept edited Skill (H7).

Four defects carry findings at two binding grades. Each has a HIGH item and a MEDIUM item that cross-refer: H2 and M1, H3 and M2, H4 and M3, H5 and M4. Fix each pair as one defect.

Units 13, 21 and 38 have no confirmed finding.

## Review shape

Intensity full: raw 37, confirmed 37, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 BLOCKER, 7 HIGH, 19 MEDIUM, 2 LOW (28 items).

Adjudicated tally by raw confirmed finding: 0 BLOCKER, 9 HIGH, 25 MEDIUM, 3 LOW (37 findings).

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdicts: 0 contradictory demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 33 judged sound, 4 judged UNSOUND (findings 13, 14, 25 and 33, whose items give the skeptic's corrected fix), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 6 RE-GRADED by the skeptic (findings 2, 3, 18, 22, 23 and 32, each from high to medium).
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 18 spec documents were supplied as `specs`, as sibling context.
- Checklist: 109 items, each assigned to one lens (coherence 22, grounding 22, reuse 22, blast-radius 22, failure-envelope 21).
- By design: 2 invariants from the checklist's by-design block.
- Move check: no checked subject moved.
- Fold diff: 10 of 10 subjects carried prevBlob.

Every count is zero where it should be, so this run is complete as a run.

## BLOCKER

None.

## HIGH

### H1. Unit 11 gives `adopt-codebase-map.sh`'s walk a stop condition a first adoption can never meet (findings 1, 11)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md`, §2 S4, the walk-up resolver paragraph naming `tools/codebase-map/adopt-codebase-map.sh:28-35`; §6 AC29.
- **What is wrong:**
  - S4 gives every walk-up resolver one stop: the home exists at this level, or the level holds `.git` and `legacy <home> --root <level>` prints a folded key.
  - The adopter's walk stops at a bare `.git` on purpose (`[ -f "$_parent/.codebase-map.conf" ] || [ -e "$_parent/.git" ]`), because the adopter is what creates the marker.
  - A repository that has never adopted holds no conf and no folded key, so under S4's condition the walk never stops at its own root.
  - AC29 runs only `row_grammar.resolve_root` and `map_lib.resolve_root`, so no criterion covers the adopter.
- **Consequence:** built as written, every first-time `adopt-codebase-map.sh` walks to the filesystem root and exits 2 with 'no repo root above'.
- **Fix (skeptic: sound, both findings):**
  - Take the adopter off S4's walk-up list, or state that the `.git` stop stays unconditional in every walk and the folded-key test only decides whether that level counts as adopted. Apply the per-level presence shape only to the two resolver walks that fall back or raise at `.git`.
  - Add an AC29 clause: on a scratch repository with no `.codebase-map.conf` and no policy file, `bash tools/codebase-map/adopt-codebase-map.sh` resolves ROOT to `git rev-parse --show-toplevel`.
- **Left-shift gate:** checklist entry "a shape rule applied to a list of walks is checked against each walk's purpose; a walk that creates its own marker keeps its bare `.git` stop", plus a codebase-map adopter e2e arm on a never-adopted scratch repo.

### H2. The typed list of legs that guard the policy kit leaves out legs whose suites now run it (findings 10, 28)

**Specs:** PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-41

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4, the paragraph 'Each leg whose suite now reads through the policy kit names it in its guard', and §6 AC30. `2026-11-04-spec-PLAY-dConvergedCharter-41.md` §2 S1 (the three legs) and §6 AC12. The same defect at medium grade is M1.
- **What is wrong:**
  - S4 names seven legs and unit 41 names three. The fold's own re-points make more suites policy-kit readers, and their guards name no `{prefix}/policy/` file.
  - The omitted legs: `row-grammar selftest` (row_grammar.resolve_root's `legacy` walk), `codebase-map kit selftest` and `codebase-map adopter e2e` (map_lib.resolve_root and the adopter walk), `codebase-map gate coverage` (imports map_lib), `corpus-ids selftest` (check 16's READ_PATH_WAIVER re-point), `gotchas selftest` (`rev="HEAD"`), `memory-hygiene self-test` (`budgets.py resolve --rev HEAD`), and the run-gates legs running the legs-parse python (`run-gates turnstile`, `run-gates adopter e2e`, `profile-bar selftest`, `run-gates gov canary`). Under unit 41, `backlog migration selftest` (migrate_backlog.py calls read_modes).
  - AC30 and AC12 check only 'each leg S4 names', so they are green by construction.
- **Consequence:** a change to `policy.py` (`render_folded_lines`, `derive_home_folds`, `legacy --root`) or to `budgets.py --rev` skips these suites on a guarded bar. A breaking change to the policy kit lands green on the guarded bar and reds only the full bar.
- **Fix (skeptic: sound, both findings):**
  - Derive the leg set, never type it. For each file S1, S4 and unit 41 S1 re-point, take every leg whose argv suite imports or executes that file. Add `{prefix}/policy/policy.py` to each such guard, and `budgets.py` where the read goes through it.
  - Rewrite AC30 and AC12 to iterate the derived set and to red on any leg running a re-pointed reader whose guard omits the kit.
  - Probe for the build: stage a one-line break in `render_folded_lines`, run the bar with `GATE_FULL=0`, and observe it select `row-grammar selftest`, `corpus-ids selftest` and the codebase-map legs.
- **Left-shift gate:** a run-gates or manifest-check arm that reds a leg whose suite imports or spawns a `tools/policy/` file while its guard names no policy-kit path. This class (C21) has now recurred in its own fix, so a gate, not a checklist entry, is owed.

### H3. Seven legs still select themselves by a folded home's path, not by the policy file (finding 19)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (the leg-guard paragraph) and §6 AC30; the legs' guards in `tools/gate-legs.json`. The same defect at medium grade is M2.
- **What is wrong:**
  - `kit/dogfood doc parity`, `recall floor`, `transition-audit arms`, `straggler-guard arms`, `codebase-map gate coverage`, `lexicon naming predicates` and `govkit acceptance matrix` guard on `.memory-tree.conf`, `.lexicon.conf` or `.codebase-map.conf`.
  - S2 moves those homes' owner-policy values into `.governance/policy.toml`. No guard names that file, and the fold's guard paragraph covers only policy-kit code files.
  - A leg's guard files are its reuse-key inputs (`input_key`/`build_key_text`, `run-gates.sh:3300-3346`).
- **Consequence:** an owner's edit of `lexicon.langs`, a `codebase-map.*` key or `memory-tree.recall-floor` in the policy file leaves those legs' keys unchanged, so the bar reuses a green earned under the old values. `lexicon naming predicates` declares a `history` read, so a committed edit moves its key there, but an uncommitted edit does not.
- **Fix (skeptic: sound):**
  - In S4, state the class rule: every leg whose guard names a folded home also names `.governance/policy.toml`, and the home stays in the guard only while it holds keys. Derive the set from `tools/gate-legs.json` at the pass, and apply it to each descriptor's `[[gate_leg]]` guard too (`tools/lexicon/kit.toml:167`).
  - Widen AC30 to iterate every leg whose guard intersects the folded homes and require `.governance/policy.toml` in each.
  - Probe for the build: on a scratch clone after S2, edit `lexicon.langs` in the policy file and run the bar with reuse on; a stale reuse of `lexicon naming predicates` is the red case.
- **Left-shift gate:** a manifest-check arm that reds a guard naming any home `legacy --keys` covers without `.governance/policy.toml` beside it, staged red by a planted removal.

### H4. Unit 11's AC32 cannot see the carriers S4 re-words (finding 13)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §6 AC32, against §2 S4's agent-cap re-word list (`agent-cap.js:1478`, `:1590-1595`) and `tools/hooks/README.md:159`. The same defect at medium grade is M3.
- **What is wrong:**
  - AC32 greps for `.unattended.conf` and `SPEC_AUDIT_DEFAULT` on one line. At base it matches only `help/spec-audit.md:19`, `agent-cap.js:44` and `:1426`.
  - `agent-cap.js:1477-1478` and `tools/hooks/README.md:159-160` split the two tokens across lines.
  - `agent-cap.js:1590` and `:1595` spell the path as `${conf}`, built at `:1587` from `path.join(root, '.unattended.conf')`.
- **Consequence:** a build that re-words only the three lines the grep sees leaves the deny strings and the hooks README telling the owner to set `SPEC_AUDIT_DEFAULT` in `.unattended.conf`, and AC32 passes. Its Red-when is certified without being checked.
- **Fix (skeptic: UNSOUND as proposed; the skeptic's corrected fix):**
  - Replace the one-line grep with a scan of each named file joined across lines that flags `.unattended.conf`, or the `conf` variable built from it at `agent-cap.js:1587`, within a few lines of `SPEC_AUDIT_DEFAULT`.
  - Drive agent-cap's deny path in a scratch repo, with the README carrying no key and a non-date `unattended.spec-audit-default` in `.governance/policy.toml`, and assert the rendered deny names `unattended.spec-audit-default` and `.governance/policy.toml`.
  - Assert nothing about the conf no longer being read, because an adopter's legacy home is still read through `readFoldedKey`.
- **Left-shift gate:** checklist entry "a criterion over user-facing text runs the producer, or scans joined lines; a single-line grep is not a check of a multi-line or interpolated string".

### H5. Unit 11's AC33 misses the house `.get(key, default)` spelling and is green at base (finding 33)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §6 AC33, with §2 S1 'ONE READER OF THE FIELD'. The same defect at medium grade is M4.
- **What is wrong:**
  - AC33's regex `\[.legacy.\]|get\(.legacy.\)` needs `)` straight after the quoted key, so `row.get("legacy", "")`, the house form, does not match.
  - It searches only four named files, and it prints nothing at base, so it is green before the unit is built.
- **Consequence:** a second derivation of the home-to-keys map, written as `r.get("legacy", "")` in `conf_to_policy.py` or placed in any file outside the four, passes AC33. That is the second derivation S1's one-reader rule exists to prevent.
- **Fix (skeptic: UNSOUND as proposed; the skeptic's corrected fix):**
  - Grep every tracked code file with a regex that admits a default argument (`get\(\s*['"]legacy['"]`, `\[['"]legacy['"]\]`). Exclude `policy.py`'s `derive_home_folds`.
  - Name `tools/playbook/render_playbook.py` as an allowed reader of the playbook block's own, unrelated `legacy` field. Better, limit the check to files that load `catalogue.toml`.
  - Stage `row.get("legacy", "")` in a scratch copy of `check-kit-placeholders.py` and confirm the criterion goes red.
- **Left-shift gate:** a `check_policy.py` arm over the catalogue's loaders that reds any read of the `legacy` field outside `derive_home_folds`, with its planted red recorded.

### H6. Kits with `requires = []` get readers that need the policy kit, and no absent-kit behaviour is stated (finding 29)

**Specs:** PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-41

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (the legs-parse python's procmon branch; the walk-up resolvers). `2026-11-04-spec-PLAY-dConvergedCharter-41.md` §2 S1 (the `read_modes` and `held_halves.py` bullets).
- **What is wrong:**
  - `tools/run-gates/kit.toml:15` and `tools/memory-tree/kit.toml:7` declare `requires = []`. The registry's default selection (`tools/govkit/registry.toml:38-53`) carries run-gates, memory-tree and codebase-map but not policy.
  - Yet run-gates' legs-parse python now answers presence through `render_folded_lines`, `held_halves.py` reads through `policy.py legacy` with no resolver named, `read_modes` reaches the kit by the inlined `resolve_kit_dir`, and row_grammar's walk calls `legacy`.
  - S4's general rule says a missing kit refuses naming the reader. Only drift_report's re-point states what an unresolved kit does. The legs-parse branch's existing rule that 'a refusal never ends this program' (`run-gates.sh:2836-2842`) is not carried over.
- **Consequence:** at a default adopter with no policy kit, the bar refuses on every run where `[ -f .process-monitor.conf ]` could never fail. `held_halves` refuses its parity count permanently. Check 26 and migrate_backlog break on memory-tree-only adopters.
- **Fix (skeptic: sound):**
  - State the absent-kit and refused-read behaviour for each such reader.
  - The legs-parse branch catches both, never exits, falls back to the home's own presence (`[ -f <home> ]`) and prints one named line.
  - `held_halves` names its resolver (`resolve_kit_dir("policy", "policy.py", ...)`) and reads the gate file's text when no kit resolves.
  - `read_modes` falls back to the conf blob alone when no kit resolves, as today.
  - Add a fixture per reader with the policy kit removed.
- **Left-shift gate:** a govkit check that reds a kit whose code resolves another kit not listed in its `requires`, unless the call site carries a named absent-kit fallback.

### H7. Unit 9's DOWN restores the old render whatever the UP did (finding 34)

**Specs:** PLAY-dConvergedCharter-9

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-9.md` §2 S4 ('The DOWN clears the forwarder, then restores the old render byte-identical'), the Migration (:207), and §6 AC4.
- **What is wrong:**
  - The UP has three outcomes: it withdrew a kit render; it kept the target's hand-edited Skill and wrote no forwarder (`edited`); or the path was empty and gains the forwarder alone (`absent`).
  - The DOWN is given only the first: it restores the old render unconditionally.
  - AC4 runs the DOWN only on the `rename` plant.
- **Consequence:** rolling back an adopter whose edited Skill the UP kept overwrites that edit with the kit's old render, which is data loss. Rolling back an `absent` adopter creates a Skill it never had. For `older-render` and `crlf` adopters, 'byte-identical' restores the current template's render, not the adopter's bytes.
- **Fix (skeptic: sound):**
  - Key the DOWN on the UP's outcome. Clear only a file carrying this rename's `gov:shim <id>` marker.
  - Restore only where the UP withdrew, and restore the adopter's own pre-UP bytes rather than a fresh render, through `STEPS.write_from_before_image` (`upgrade_steps.py:1121`, `:1192`) as `fanout_cap.py:201-203` already does, or the receipt's recorded render.
  - Leave a kept file untouched and an absent path absent.
  - Extend AC4: run the DOWN over `edited`, `absent`, `crlf` and `older-render`, red when any byte differs from the pre-UP tree.
- **Left-shift gate:** an upgrade-steps fixture rule that every step's DOWN runs over every plant its UP runs and compares the tree byte-for-byte with the pre-UP tree.

## MEDIUM

### M1. The typed guard list misses policy-kit readers, at medium grade (findings 2, 20, 21)

- **Where:** unit 11 §2 S4 (leg-guard paragraph), §6 AC30 and §7; unit 41 §2 S1 (the three-leg sentence) and §6 AC12.
- **What is wrong:** this is the H2 defect, raised by three findings the skeptic graded medium. They add these omitted legs: `run-gates run-log line` (the procmon branch via `render_folded_lines`), `pre-push run-log line` (drives the hook whose gate-key reads at `pre-push:1453-1454` unit 41 re-points), and `backlog migration selftest`. Finding 20 adds that §7 also omits `row-grammar selftest` and `corpus-ids selftest`.
- **Consequence:** a change to `policy.py` or `budgets.py` alone reuses these legs' greens on a scoped push. The effect is contained: the unguarded `memory hygiene` leg still runs, and the pre-push full-run lag still applies.
- **Grade note:** the binding grade is medium per finding; the defect as a whole stands at HIGH through H2, and both are folded by H2's fix.
- **Fix (skeptic: sound, all three):** H2's derived-set fix; it covers these legs. Name `pre-push run-log line` and `backlog migration selftest` in unit 41 S1's guard sentence. Add `row-grammar selftest` and `corpus-ids selftest` to unit 11 §7. Restate AC30 and AC12 over the derived set, for example the legs whose suite greps for a re-pointed reader, so a forgotten leg reds it.
- **Left-shift gate:** as H2.

### M2. Folded-home guards lose selection on a policy-file edit, at medium grade (finding 3)

- **Where:** unit 11 §2 S2/S4 against the legs' guards, §7; unit 41 S1; `tools/lexicon/kit.toml:167`.
- **What is wrong:** the H3 defect, seen as C16 (a spelling change strands its readers) applied to leg selection. The lexicon kit's shipped descriptor guard also names `.lexicon.conf`, which unit 20 deletes at adopters.
- **Consequence:** changing a folded key in `.governance/policy.toml` no longer selects the leg that grades it, so a scoped push stays green over an unchecked value. `lexicon wiring` is partly mitigated (empty guard; `apply` drops an untracked conf entry). The memory-tree and codebase-map legs are not.
- **Grade note:** binding medium; the defect stands at HIGH through H3.
- **Fix (skeptic: sound):** add an S4 item: every guard entry naming a folded home also names `.governance/policy.toml`, in `tools/gate-legs.json` and each descriptor's `[[gate_leg]]`. Add a criterion iterating the homes `legacy --keys` covers. Plant a removal to see it red.
- **Left-shift gate:** as H3.

### M3. AC32's one-line grep misses split and interpolated carriers, at medium grade (findings 5, 32)

- **Where:** unit 11 §6 AC32, against §2 S4 (`agent-cap.js:44`, `:1426`, `:1477-1478`, `:1584-1595`; `tools/hooks/README.md:159-160`).
- **What is wrong:** the H4 defect. In addition, AC32's second grep checks `unattended.spec-audit-default` only in the help page and README, never in `agent-cap.js`.
- **Consequence:** with every deny string unchanged, AC32 passes. S4 names those lines explicitly, so shipping stale text also needs the builder to miss them.
- **Grade note:** binding medium; the defect stands at HIGH through H4.
- **Fix (skeptic: sound, both):** run the hook on the deny path with a non-date `unattended.spec-audit-default` in a scratch policy file and require the deny text to name `.governance/policy.toml` and `unattended.spec-audit-default`. Add `agent-cap.js` to the second grep's files. Name AC32's population by line (`agent-cap.js:44`, `:1426`, `:1477-1478`, `:1584-1595` and the `conf` binding, `help/spec-audit.md:19`, `tools/hooks/README.md:159-160`), or grep each file for `\.unattended\.conf` alone. Stage a probe that keeps `:1477` unchanged and observe AC32 red. Per H4's correction, do not assert the conf is no longer read.
- **Left-shift gate:** as H4.

### M4. AC33 cannot red a second reader of `legacy`, at medium grade (findings 6, 14, 25)

- **Where:** unit 11 §6 AC33, against §2 S1 'ONE READER OF THE FIELD' and S3.
- **What is wrong:** the H5 defect. In addition, AC33's second half compares `legacy <home> --keys` with the keys `legacy <home>` folds, and S3 derives both from `derive_home_folds`, so it compares one function with itself.
- **Consequence:** a defaulted `.get` re-derivation in `check_policy.py`, `settings_census.py`, `check-kit-placeholders.py` or `conf_to_policy.py` passes, and the one-reader rule ships with no check that can fail.
- **Grade note:** binding medium; the defect stands at HIGH through H5.
- **Fix:** finding 6's fix is sound; findings 14's and 25's were judged UNSOUND, and the skeptic's corrections are written here.
  - Widen the pattern to admit a default argument: `\[\s*["']legacy["']\s*\]|get\(\s*["']legacy["']\s*[,)]`.
  - Scope it to the code that loads the policy catalogue (the files that import policy.py's catalogue loader or open `catalogue.toml`, which include `check_policy.py`, `settings_census.py`, `check-kit-placeholders.py` and `conf_to_policy.py`), with `derive_home_folds` the only admitted site. Do not run it over every tracked `.py`.
  - Replace the tautological half with an independent oracle: compare `--keys` against the `legacy = "<home> <KEY>"` lines a grep finds in `catalogue.toml`, or a fixture's literal expected map.
  - Stage the red with `row.get("legacy", "")` planted in `settings_census.py` (or `check_policy.py`).
- **Left-shift gate:** as H5.

### M5. Unit 11's §7 omits legs its new Files-touched paths select (finding 4)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §4 Files touched against §7 Gates.
- **What is wrong:** the round-4 fold adds `gotchas.py`, `budgets.py`, `map_lib.py`, `adopt-codebase-map.sh`, `drift_report.py` and the `row_grammar.py` re-point. §7 still omits `memory-hygiene self-test`, `gotchas selftest`, `row-grammar selftest`, `run-gates turnstile`, `run-gates adopter e2e` and `run-gates gov canary`, whose guards select those paths.
- **Consequence:** the close does not run the self-tests of the files the unit changes, so §7 understates what the unit puts at risk.
- **Fix (skeptic: sound):** re-derive §7 by joining every Files-touched path against each leg's guard in `tools/gate-legs.json`, and add at least the six legs above.
- **Left-shift gate:** a spec-token check that reds a §7 missing any leg whose guard selects a §4 Files-touched path.

### M6. Unit 11's HEAD cap read breaks the hygiene and gotchas suites' premise (finding 18)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S1 ('Their two enforcers read them at HEAD'), §7.
- **What is wrong:** both suites assume no fixture has a landed revision, so the policy reader refuses and every cap breach refuses (`check-memory-hygiene.test.sh:264-268`, `:1632`; `gotchas.py:846-849`). A read at HEAD succeeds, and with no policy file `budgets.enforce` falls to its catalogue default `warn` (`catalogue.toml:1315-1317`).
- **Consequence:** check 6/7/19 breaches become `BUDGET WARN` lines, and `memory-hygiene self-test` and `gotchas selftest` go red. The spec does not foresee this, and §7 omits both legs. Their guards still select the change, so the red surfaces at the bar rather than shipping.
- **Fix (skeptic: sound):** name both suites in S1 and say how their fixtures keep a refusing reader under a HEAD read: plant an invalid policy file, or pin `budgets.enforce = "refuse"` in the fixture, and re-word the 'no fixture has a landed revision' comments. Add both legs to §7. Probe: run `bash tools/memory-tree/check-memory-hygiene.test.sh` and `python3 tools/memory-tree/gotchas.py --selftest` with the `--rev HEAD` change applied and fixtures untouched, and observe them red.
- **Left-shift gate:** checklist entry "a change to a reader's revision names every suite whose fixture relies on the old revision's absence".

### M7. Unit 11's walk-up list misses three `.memory-tree.conf` walks (finding 22)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (the WALK-UP resolver sentence), §4, §6 AC29.
- **What is wrong:** S4 names `row_grammar.resolve_root`, `map_lib.resolve_root` and the adopter. It misses `merge-rows.py`'s `_anchor_root` (`:218-235`, the row-keyed merge driver), `transition_audit.resolve_root` (run in commit-msg) and `backlog._resolve_anchor_at`.
- **Consequence:** S4's class rule plus S5's presence red do force the builder to re-point all three. But the named list, Files touched and AC29 miss them, so a wrong per-level re-point there (stopping at the kit directory) goes unobserved. Built wrong, the merge driver raises on every row-keyed merge at an adopter whose home unit 20 deleted.
- **Fix (skeptic: sound):** add the three to S4's walk-up list with the per-level shape, read in-process through `render_folded_lines`. Name them in §4's readers and Files touched. Extend AC29 to call each on the clone with `.memory-tree.conf` deleted. Derive the class at the pass by grepping for `parents` loops testing a folded home.
- **Left-shift gate:** S5's presence arm already reds an unconverted walk; add an AC29 rule that it calls every walk S5's arm finds.

### M8. Unit 11's AC29 compares backslash paths against git's forward-slash path (finding 12)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §6 AC29.
- **What is wrong:** on gov's Windows nodes `row_grammar.resolve_root` (`os.path.abspath`, `row_grammar.py:131`) and `map_lib.resolve_root` (a `Path`) print backslashes, while `git rev-parse --show-toplevel` prints forward slashes.
- **Consequence:** AC29 reads red on a correct build, so a builder either "fixes" working code or loosens the comparison by hand with no rule.
- **Fix (skeptic: sound):** compare normalised paths, `pathlib.Path(...).as_posix()` or `os.path.normcase(os.path.realpath(...))` on both sides, or `os.path.samefile`. State the normalisation in AC29.
- **Left-shift gate:** checklist entry "an AC comparing printed paths states its normalisation".

### M9. The `SPEC_AUDIT_DEFAULT` move leaves the driver's readers on `.unattended.conf` (finding 26)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (the agent-cap bullet and the re-words of `help/spec-audit.md:19`, `tools/hooks/README.md:159` and the deny strings), §6 AC32.
- **What is wrong:** S2 moves `SPEC_AUDIT_DEFAULT` (gov's value is blank, so the held rule does not hold it), and S4 sends the owner to `unattended.spec-audit-default` in the policy file. The driver's authorization at BASE (`unattended.sh:4175-4205`) and check 19's run-commit refusal (`check-unattended.sh:2133-2150`, `:3028`) still read `.unattended.conf` and are not re-pointed.
- **Consequence:** until unit 12 retires the driver, agent-cap admits an opt-in set in the policy file while the driver says 'not owed'. Check 19 does not see a run commit that sets the key in the policy file.
- **Fix (skeptic: sound):** either keep `SPEC_AUDIT_DEFAULT` in `.unattended.conf` under the held rule until unit 12 re-points the driver, leaving the page and deny strings as they are, or name and re-point `unattended.sh`'s check_authorization read and check 19's population in this unit. Add an AC in which an opt-in set in the policy file only is read the same way by agent-cap and the driver.
- **Left-shift gate:** checklist entry "a moved key's readers are found by grepping its old spelling across every kit, not only the kit that documents it".

### M10. Unit 11 does not say what `render_folded_lines` does with an invalid policy blob in history (finding 30)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S3 (`render_folded_lines`, `legacy --rev`) and §5 error states; with drift_report (S4) and unit 41's `read_modes`.
- **What is wrong:** the specs never mention invalid TOML or a failed `validate`. The owner's TTY commit is not schema-checked, so invalid text can land, and the fold adds readers that walk history. The kit already has a rule: `read_revision` sets `table = None` and `resolve_read` takes `read_last_valid_value` (`policy.py:724-750`).
- **Consequence:** under S4's refuse rule, one historic typo makes check 26, the straggler parity and the drift signal refuse forever. A silent fallback instead misreads the mode.
- **Fix (skeptic: sound):** add a sentence to S3: at a revision whose text `validate` rejects, `render_folded_lines` takes `resolve_read`'s last-valid-value path (or names its rule), and a history reader never refuses on a past commit. Add an AC fixture with an invalid policy blob mid-history, observed through `read_modes` and the drift signal.
- **Left-shift gate:** checklist entry "every history reader states its behaviour on an unparseable past blob".

### M11. Unit 11's drift signal finds a `langs` change by a line regex (finding 31)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (drift_report.py bullet, `signal_lexicon_ratified_stale` via `git log -G` on `langs =`) and AC28.
- **What is wrong:** `-G 'langs ='` matches only the line holding the key. The folded value is an 18-member list; an owner who spells it as a multi-line array, or writes `langs=`, makes an edit that is never returned.
- **Consequence:** `lexicon_ratified_older_than_language_surface` stays 0, and a gateable signal certifies a ratified table over a moved language surface. AC28's fixture uses one spelling, so it cannot red.
- **Fix (skeptic: sound):** list commits touching `.governance/policy.toml` (`git log --format=%H -- .governance/policy.toml`) and compare `render_folded_lines`' LANGS at each against its parent, or use `-G` over the whole `[lexicon]` table. Add an AC28 case with a multi-line `langs` and the narrowing on a continuation line.
- **Left-shift gate:** checklist entry "a history lookup of a structured value compares parsed values, not a line regex".

### M12. Unit 11 gives procmon-hook a policy-file-exists walk and leaves its env branch (finding 36)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S4 (`procmon-hook.js`'s `resolveRoot`, `:48-59`, 'walks by the policy file').
- **What is wrong:** the same sentence that gives other walks the per-level presence shape gives procmon-hook the predicate "the policy file exists". The `CLAUDE_PROJECT_DIR`/`PROCMON_ROOT` branch at `:50` still tests `.process-monitor.conf` and is not addressed.
- **Consequence:** null from `resolveRoot` is the hook's only 'not adopted' test (`:102-103`), so every policy-kit repo reads as monitor-adopted and the hook reaps where the monitor was never adopted. The env root is ignored once gov's conf is deleted. Contained to repos where the hook's settings fragment is installed.
- **Fix (skeptic: sound):** give procmon-hook the per-level shape: the home exists here, or this level holds `.git` and `readFoldedKey` (the mirror at HEAD) holds a `process-monitor.*` row sourced `file`. Apply it to the env branch too. Add a fixture with a policy file holding no process-monitor key, in which the hook stays silent.
- **Left-shift gate:** checklist entry "an adoption test keys on the kit's own keys, never on a shared file's existence".

### M13. Unit 7's AC14 observes the guard's existing behaviour, not the commit route (findings 7, 24)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-7.md` §6 AC14 against §2 S8 (THE COMMIT ROUTE).
- **What is wrong:** AC14 stages a `.governance/deploy.toml` edit from a non-TTY shell and expects `policy-guard: refused`. The guard already does that at base (`guarded-paths.txt:8`, `guard.py:5-12`). Its red case, 'the pass plans an agent commit of deploy.toml', is not observable by that command.
- **Consequence:** AC14 is green before the unit is built, and stays green if the pass lands the `:54` and `:68` edits with `--no-verify` or inside an agent commit. S8's owner-commit route is asserted, not checked.
- **Fix (skeptic: sound, both):** have AC14 grade the landed range: `git log --format='%H %s' <base>..<tip> -- .governance/deploy.toml` prints exactly one commit; it is the owner's terminal commit the pass handed over (no agent `Co-Authored-By` trailer, or the TTY-proof record, compared against the build record's handed-over sha); it holds the manifest's `git mv` and no other path; and it precedes every agent commit of S8. Keep the guard-refusal half as a precondition, not the observation.
- **Left-shift gate:** checklist entry "an AC is run at base first; one green at base observes nothing the unit adds" (C99).

### M14. Unit 7 moves the kickoff manifest into `memory/project/`, which check 3 and the charter forbid (finding 23)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-7.md` §2 S8, §4 Files touched, §8 F5.
- **What is wrong:** hygiene check 3 (`check-memory-hygiene.sh:903-965`) admits under `memory/project/` only named registries plus `PROJECT_REGISTRY_EXTRA`, which does not list `SESSION-KICKOFF.md`. `.governance/deploy.toml:65`, rendered at `AGENTS.md:91`, says `memory/project/` holds only the gates' row registries. Spec 7 names neither.
- **Consequence:** the move reds `memory hygiene` and the pre-commit staged hygiene leg, so it does not ship silently, but the exits are unplanned. After unit 11, `PROJECT_REGISTRY_EXTRA` is an owner-guarded folded key, needing another owner terminal commit. The rendered charter line becomes false.
- **Fix (skeptic: sound):** choose a home check 3 already admits, or add to S8: the check-3 widening (a named `F:SESSION-KICKOFF.md` case with its reason, or the owner's `PROJECT_REGISTRY_EXTRA` entry folded into the owner's terminal commit beside `deploy.toml`); the re-word of `deploy.toml:65` in that commit with AGENTS.md re-rendered; and unit 6's `check_record_homes` kind for the file. Add an AC running `bash tools/memory-tree/check-memory-hygiene.sh --only 3` on the moved tree, expecting no `memory/project/SESSION-KICKOFF.md` finding.
- **Left-shift gate:** checklist entry "a file move names the hygiene checks and charter rules that govern its destination".

### M15. Unit 17's re-points of two guides have no criterion (finding 8)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-17.md` §2 S4 (re-points of `memory/guides/SESSION-KICKOFF.md:54` and `memory/guides/UNATTENDED-VERBS.md:821`) against §6 AC4 and AC5.
- **What is wrong:** both lines sit outside the inventory's walk, so AC4's `--readers` run never reads them, and AC5 greps only AGENTS.md, the charter template and the kickoff card.
- **Consequence:** a build without these edits passes every criterion while the kickoff manifest every session reads still says 'An attended code build runs through `/build`'.
- **Fix (skeptic: sound):** extend AC5: `grep -nE '/build([^/A-Za-z0-9_-]|$)' memory/guides/SESSION-KICKOFF.md memory/guides/UNATTENDED-VERBS.md` prints nothing after S4 (it prints `:54` and `:821` at base), and `grep -c 'run.py' memory/guides/SESSION-KICKOFF.md` prints at least 1. Unit 17 runs before unit 7 moves the manifest, so the guides path is correct.
- **Left-shift gate:** checklist entry "every by-name re-point outside a derived walk has its own criterion".

### M16. Unit 9 names `render_shim` for a Skill's `.md` forwarder (finding 15)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-9.md` §2 S4 (the UP's forwarder write, 'with `render_shim` (`tools/govkit/shims.py:232`)').
- **What is wrong:** `render_shim` and `read_shim_rows` handle only `.sh`/`.js`/`.py` (LANGS, `shims.py:49`), and `read_shim_rows` refuses any other extension (`:97`). The `.md` renderer is `render_skill_shim`, minted by unit 17 §4.
- **Consequence:** a builder following S4 hits the read refusal or emits a code-language template at a `SKILL.md` path; either way the forwarder AC10 requires is not the one unit 17 specifies.
- **Fix (skeptic: sound):** name `render_skill_shim`, or the `.md` dispatch unit 17 S2 gives `write_shims`, as the UP's renderer, and cite unit 17's LANGS/validation change as what lets `read_shim_rows` admit the row. See M17, which replaces the call with a shared per-row writer.
- **Left-shift gate:** checklist entry "a cited function is checked to accept the cited input's kind".

### M17. Unit 9 re-implements the `skill` kind's write rule instead of reusing the shims kit (finding 17)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-9.md` §2 S4 (the UP's forwarder write, rev-5 fold) against `2026-11-03-spec-PLAY-dConvergedCharter-17.md` §2 S2.
- **What is wrong:** unit 17 puts the absent-or-own-marker rule inside `write_shims`' row loop. Unit 9 rebuilds the same rule in `skill_rename.py` from `read_shim_rows` plus a renderer. S4 also never names `read_shim_rows`' `troot` parameter (`shims.py:60-67`). At base `write_shims` (`:267-279`) overwrites any differing dest and has no per-row writer.
- **Consequence:** the rule that keeps an adopter's hand-edited Skill lives in two places, so a later change (unit 17's `held:` reporting, a new marker spelling) reaches one copy. A builder copying base `write_shims`' shape overwrites the kept Skill. Contained to the five rename forwarders; the `troot` sub-claim is weak because the forwarder template spells no policy path.
- **Fix (skeptic: sound):** in unit 17 S2, factor the per-row write out of `write_shims` as one function, e.g. `write_shim(root, row) -> str | None`, applying the kind's write rule and returning the path written; `write_shims` loops over it. In unit 9 S4, call it for the rename's row at the target, reading the row with `read_shim_rows(GOV, troot=govkit.derive_tool_root(target))`. List the function in unit 17's §4 mint and unit 9's §10 Reuse audit. Name in unit 9 AC4 the `edited-then-write` plant, staged red with the UP's write swapped for an unconditional `write_bytes`.
- **Left-shift gate:** checklist entry "a rule another unit mints is called, never restated" (reuse audit).

### M18. Unit 20's adopter route leaves scratch-guard UNARMED with no bound (finding 35)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-20.md` §2 S1 (THE ADOPTER'S COMMIT ROUTE, :89-97).
- **What is wrong:** `update` stages the home lines' removal with the policy file, and until the agent's commit N+1 scratch-guard reads UNARMED. The spec does not say what happens when commit N, the owner's terminal commit, never comes: an agent or unattended `update`, an owner who declines, or other sessions sharing the checkout.
- **Consequence:** UNARMED denies every write except to the conf (`scratch-guard.js:1157-1160`), so the agent and every concurrent session are locked out of Write and Edit, and no rollback is stated. Contained: Bash `git restore` recovers it and nothing is lost.
- **Fix (skeptic: sound):** state the window's bounds. Either `update` removes the home lines only after commit N lands (stage `policy.toml` alone, remove the home lines in N+1 with the mirror), closing the window, or the up's last line prints the rollback (`git restore --staged --worktree <home>`) next to the route. Add an AC with `update` staged and no commit N, showing writes are not locked out, or are restored by the printed rollback.
- **Left-shift gate:** checklist entry "a route that opens a guard window states how it closes when the human step never comes".

### M19. Unit 40's record-first amend leaves an orphan record (finding 37)

- **Where:** `2026-11-04-spec-PLAY-dConvergedCharter-40.md` §2 S2 ('Each amend's record is written BEFORE the manifest is rewritten') and AC3 `amend-interrupted`.
- **What is wrong:** an interrupted amend leaves an `edit` record whose `After` hash names a row never on disk. The spec covers only a re-run with an unchanged plan.
- **Consequence:** with no re-run, or a corrected `help` before the re-run (a different `After`), the first record is an orphan and a second `edit` record is written from the same `Before`. The trail reports two edits of one row, one fictitious. Contained to the record trail.
- **Fix (skeptic: sound):** name the orphan case. Either a re-run whose entry's `After` differs removes or supersedes a record of this section whose `After` is not on disk, or a check reds an `edit` record whose `After` matches no manifest revision. Add an `amend-interrupted-then-edited` plant.
- **Left-shift gate:** checklist entry "a write-ahead record states its recovery when the plan changes between attempts".

## LOW

### L1. Unit 11's new `budgets.py resolve --rev` has no usage declaration (findings 9, 27)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S1 (`budgets.py resolve` gains `--rev`), §2 S10, §4 Files touched and Minted; `tools/govkit/usage.toml:159-164`.
- **What is wrong:** S10 declares new flags only for `policy.py#legacy` and `check_policy.py`; the `budgets.py#resolve` row keeps `flags = ["--explain"]`. Declaring the flag moves its fingerprint under `help/size-caps.md:40`'s anchor `cfbc2b02`. `check_policy.scan_cap_requests` (`:584-587`) would read `HEAD` as a cap name in a shell enforcer spelling `--rev HEAD`.
- **Consequence:** a help page documenting `--rev` reds as an undeclared flag under `help.enforce = refuse`, and the declaration drifts from the verb. The spec's own enforcers do not reach the census path, so the phantom cap is hypothetical.
- **Fix (skeptic: sound, both):** add `--rev` to the usage row and re-stamp `help/size-caps.md:40` in the same commit; document it on `help/size-caps.md`. In `scan_cap_requests`, skip the argument after `--rev`, or state that enforcers pass `--rev` only in-process. Name all three in §4. Have AC25 also check `grep -A5 'budgets.py#resolve' tools/govkit/usage.toml` for `--rev`.
- **Left-shift gate:** checklist entry "a minted flag lands with its usage row, its help anchor and its census parse".

### L2. Unit 11 adds a GATE_DOC_PATHS arm that already exists (finding 16)

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md` §2 S2 Readers (govkit selftest M5) and §7 New arm.
- **What is wrong:** `tools/govkit/selftest.py:9241-9243` already grades three planted multi-path GATE_DOC_PATHS lines unconditionally, above the gov-line arm (`:9244-9249`) that skips. The new arm duplicates them, and the real loss, live-tree grading of gov's own spelling, is not stated.
- **Consequence:** only the spec's account of coverage is wrong; behaviour is unaffected.
- **Fix (skeptic: sound):** drop the planted-line arm, or delete the dead gov-line arm and state in §4 that M5's plants at `selftest.py:9241-9243` already cover the predicate once gov's line leaves.
- **Left-shift gate:** none owed beyond the reuse audit's existing "grep for the arm before adding it".

review-shape kind=spec-audit round=2 intensity=full at=synth raw=37 confirmed=37 refuted=0 unverified=0 blocker=0 high=9 medium=25 low=3 agents=11 out-tokens=259889

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the walk-up resolver paragraph naming `tools/codebase-map/adopt-codebase-map.sh`'s walk, :28-35); section 6 AC29 | high | high | confirmed | Spec 11 at blob 850c591 (lines 281-288) gives every walk-up resolver one stop condition: 'the home exists here, or this level holds `.git` and `legacy <home> --root <this level>` prints a folded key'. It names `tools/codebase-map/adopt-codebase-map.sh`'s walk (`:28-35`) among them. tools/codebase-map/adopt-codebase-map.sh:26-37 stops at `[ -f "$_parent/.codebase-map.conf" ] \|\| [ -e "$_parent/.git" ]`. Its comment says the adopter must reach the .git root because it CREATES the marker, and otherwise it exits 2 'no repo root above'. A repository that has never adopted has no conf and no folded key, so under S4's condition the walk passes its own root. AC29 (lines 751-757) runs only row_grammar.resolve_root and map_lib.resolve_root, so no criterion checks the adopter. | sound | - |
| 2 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the leg-guard paragraph 'Each leg whose suite now reads through the policy kit names it in its guard'); section 6 AC30; also PLAY-dConvergedCharter-41 section 2 S1 and AC12 | high | medium | confirmed | In tools/gate-legs.json, these legs' guards name nothing under policy/: 'memory-hygiene self-test' ['{prefix}/lib/','{prefix}/memory-tree/','{prefix}/check-spec-tokens.py'], 'gotchas selftest' and 'row-grammar selftest' ['{prefix}/lib/','{prefix}/memory-tree/'], 'codebase-map kit selftest', 'codebase-map adopter e2e', and 'run-gates run-log line' ['{prefix}/run-gates/','{prefix}/runlog/']. Spec 11 S4 (lines 297-301) adds policy-kit files to the guards of seven named legs only. Yet S1 and S4 re-point code those other legs' suites run: check-memory-hygiene.sh:305 and :651, gotchas.py rev=HEAD, the resolve_root walks, and the run-gates procmon branch. Unit 41's AC12 adds three more legs. AC30 checks only the legs S4 names, so a leg S4 forgot cannot red it. An edit to policy.py or budgets.py therefore skips these legs on a scoped push. The effect is contained: the unguarded 'memory hygiene' leg still runs, and the pre-push full-run lag still applies. | sound | held-suite-guard-misses-a-sibling-kit |
| 3 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S2/S4 (the moved values) against the legs' guards; section 7; also PLAY-dConvergedCharter-41 S1 | high | medium | confirmed | Re-probed tools/gate-legs.json. Guard entries naming a home: 'kit/dogfood doc parity', 'recall floor' and 'transition-audit arms' name .memory-tree.conf; 'straggler-guard arms' names .memory-tree.conf and .lexicon.conf; 'codebase-map gate coverage' names .codebase-map.conf; 'lexicon naming predicates' and 'govkit acceptance matrix' name .lexicon.conf. `grep -n policy.toml tools/gate-legs.json` printed nothing. tools/lexicon/kit.toml:167 also guards on .lexicon.conf. No subject spec adds .governance/policy.toml to these guards: spec 16's mention of kit.toml:167 is a path re-point, not this. One check is partly mitigated: kit.toml:149-162 says 'lexicon wiring' carries an empty guard and `apply` drops a conf entry the target does not track. The memory-tree and codebase-map legs still lose selection on a policy-file edit. | sound | a-spelling-change-strands-its-readers |
| 4 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 4 Files touched against section 7 Gates | medium | medium | confirmed | Spec 11 section 4 Files touched (lines 496-510) names tools/memory-tree/gotchas.py, row_grammar.py, tools/policy/budgets.py, the codebase-map files, and run-gates.sh among the readers. Section 7 (line 782) lists 'memory hygiene' and 'run-gates canary'. It does not list 'memory-hygiene self-test', 'gotchas selftest', 'row-grammar selftest', 'run-gates turnstile', 'run-gates gov canary' or 'run-gates adopter e2e'. In gate-legs.json those legs' guards ({prefix}/memory-tree/, {prefix}/run-gates/) select the touched paths. This is not a duplicate of the prior manifest-check finding: it concerns paths the round-4 fold added. | sound | - |
| 5 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC32 against section 2 S4 (agent-cap.js comments and deny strings `:44`, `:1426`, `:1478`, `:1590-1595`; `tools/hooks/README.md:159`) | medium | medium | confirmed | Running AC32's git grep at HEAD printed only help/spec-audit.md:19, agent-cap.js:44 and agent-cap.js:1426. tools/hooks/README.md:159-160 splits `SPEC_AUDIT_DEFAULT` and `.unattended.conf` across two lines, and so does agent-cap.js:1477-1478. agent-cap.js:1587 builds `conf` from '.unattended.conf', and :1590 and :1595 interpolate `${conf}`. S4 (line 234) re-words :1478 and :1590-1595, yet AC32 passes with them left as they are. The second grep covers only help/spec-audit.md and the README. | sound | line-claim-matched-over-the-whole-output |
| 6 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC33 against section 2 S1 ('ONE READER OF THE FIELD') | medium | medium | confirmed | AC33's pattern `get\(.legacy.\)` allows one character on each side of `legacy` and then requires `)`, so `row.get("legacy", "")` does not match. S3 (lines 172-186) has `render_folded_lines` take its folded keys from the names `derive_home_folds` gives, and `--keys` prints `derive_home_folds`' map. AC33's second half therefore compares one function's output with itself and cannot red a second derivation. | sound | fixture-passes-by-finding-nothing |
| 7 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 6 AC14 against section 2 S8 (THE COMMIT ROUTE) | medium | medium | confirmed | Spec 7 AC14 (line 412) stages a deploy.toml edit from a non-TTY shell and expects `policy-guard: refused`. At base, tools/policy/guarded-paths.txt:8 already lists .governance/deploy.toml, and guard.py:5-12 already refuses any agent change to a guarded path except a budgets cap raise. So AC14 is green before unit 7 is built. Nothing in it reads the pass's commits, so the route S8 requires (lines 113-118) is never observed: the owner's terminal commit, holding :54, :68 and the `git mv`, landing before the agent's commits. | sound | - |
| 8 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md:section 2 S4 (re-points of `memory/guides/SESSION-KICKOFF.md:54` and `memory/guides/UNATTENDED-VERBS.md:821`) against section 6 AC4 and AC5 | medium | medium | confirmed | Spec 17 at blob bd22cdb, S4 lines 82-85, re-points memory/guides/UNATTENDED-VERBS.md:821 and memory/guides/SESSION-KICKOFF.md:54 'by name', and says both lie outside the inventory's walk. So AC4's --readers run (lines 240-247) never reads them. AC5 greps only AGENTS.md, the charter template and the kickoff card SKILL.md. Re-running the grep at HEAD printed SESSION-KICKOFF.md:54 ('An attended code build runs through `/build`') and UNATTENDED-VERBS.md:821. Unit 7, which moves the manifest, is order 17 and unit 17 is order 4, so the fix's guides path is still correct when unit 17 runs. | sound | - |
| 9 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (`budgets.py resolve` gains `--rev`) against section 2 S10 and section 4 Files touched (`tools/govkit/usage.toml`) | low | low | confirmed | Spec 11 S1 (lines 82-83) and the Inventory (line 468) mint `budgets.py resolve --rev`. S10 (lines 368-371) declares usage-table flags only for `policy.py#legacy` and `check_policy.py`. tools/govkit/usage.toml:159-163 still holds `script:{prefix}/policy/budgets.py#resolve` with `flags = ["--explain"]`, so the declared-flag row drifts from the verb. The effect is limited to the help and usage declaration. | sound | - |
| 10 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the leg-guard paragraph, 'Each leg whose suite now reads through the policy kit names it in its guard') and section 6 AC30; likewise PLAY-dConvergedCharter-41 section 2 S1 (the three legs) and AC12 | high | high | confirmed | I loaded tools/gate-legs.json. The guards for row-grammar selftest, corpus-ids selftest, gotchas selftest, backlog migration selftest (all ['{prefix}/lib/','{prefix}/memory-tree/']), memory-hygiene self-test, codebase-map kit selftest and codebase-map adopter e2e do not name `{prefix}/policy/`. Spec 11 S4 (lines 282-288) re-points row_grammar.resolve_root, map_lib.resolve_root and the adopt-codebase-map.sh walk to `legacy --root`. S1 sends the hygiene engine through `budgets.py resolve --rev HEAD` and gotchas.py through budgets with rev=HEAD. migrate_backlog.py:1325 calls audit.read_modes. Yet the guard paragraph (lines 297-301), which AC30 checks, names only seven legs. A policy-kit change therefore skips these suites on a guarded bar. This is a gap in the fix's own enumeration, not a re-raise of the earlier C21 finding. | sound | held-suite-guard-misses-a-sibling-kit |
| 11 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the walk-up resolver sentence naming `tools/codebase-map/adopt-codebase-map.sh`'s walk `:28-35`) | high | high | confirmed | At tools/codebase-map/adopt-codebase-map.sh:28-35 the walk stops at `-f $_parent/.codebase-map.conf \|\| -e $_parent/.git`, so the `.git` stop is unconditional. The comment above it says the adopter must reach the .git root because it is creating the marker. Spec 11 S4 (lines 282-288) gives one per-level condition for all three walks: 'the home exists here, or this level holds `.git` and `legacy <home> --root <this level>` prints a folded key'. On a fresh adoption there is no conf and no folded key, so built literally the walk passes the toplevel and ends with 'no repo root above' (exit 2). The adopter's walk already stops at `.git` from the kit's own directory, so it never needed this re-point. | sound | - |
| 12 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC29 | medium | medium | confirmed | I ran AC29's two commands at base. row_grammar.resolve_root() and map_lib.resolve_root(Path('.')) each printed 'C:\projects\coding-governance\.claude\worktrees\unattended-dconvergedcharter-51d347' with backslashes, while `git rev-parse --show-toplevel` printed the same path with forward slashes. row_grammar.py:131 uses os.path.abspath and map_lib returns Path(os.path.abspath(...)), so AC29's literal comparison of the printed paths fails on gov's Windows nodes even when the walk is correct. | sound | - |
| 13 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC32 (against section 2 S4's agent-cap re-word list `:1478`, `:1590-1595`, and `tools/hooks/README.md:159`) | high | high | confirmed | I ran AC32's grep at base. It printed only help/spec-audit.md:19, tools/hooks/agent-cap.js:44 and :1426. The carriers S4 lists for re-wording (spec 11 lines 234-236) are outside its reach. agent-cap.js:1477-1478 splits `.unattended.conf` and `SPEC_AUDIT_DEFAULT` across two source lines. :1590 and :1595 spell the conf as `${conf}`, built at :1587 from path.join(root, '.unattended.conf'). tools/hooks/README.md:159-160 also splits the two across lines. AC32 would therefore pass a build that leaves those carriers pointing at `.unattended.conf`. | unsound | - |
| 14 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC33 (first half, the grep for a second reader of the `legacy` field) | medium | medium | confirmed | I piped four spellings through AC33's regex. It matched `row.get("legacy")` and `row["legacy"]` but not `row.get("legacy", "")` or `row.get('legacy', None)`. Run at base over the four named files, the grep exits 1 and prints nothing, so this half is already green before the build. The key-equality half still catches a disagreeing derivation, which limits the effect. | unsound | - |
| 15 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 (the UP's forwarder write, 'with `render_shim` (`tools/govkit/shims.py:232`)') | medium | medium | confirmed | Spec 9 S4 (lines 96-97) names `render_shim` (`tools/govkit/shims.py:232`) as the renderer of the skill forwarder. In shims.py, LANGS (:49) is only .sh/.js/.py, read_shim_rows refuses any other extension at :97 ('from and to must be two .sh, .js or .py paths of one language'), and render_shim keys on row['lang']. Unit 17's Inventory (line 170) mints `render_skill_shim` for a skill's `.md` forwarder, and its S2 has write_shims render it when `to` is `.md`. S4 names the wrong function. | sound | - |
| 16 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S2 Readers (govkit selftest M5: 'grades a planted multi-path `GATE_DOC_PATHS` line in its place') and section 7 New arm | low | low | confirmed | tools/govkit/selftest.py:9241-9243 already grades three planted multi-path GATE_DOC_PATHS lines unconditionally, just before the `if _gov_line:` arm at :9244-9249. Spec 11 lines 159-160 (and the Files-touched entry at 517-518) add 'a planted multi-path GATE_DOC_PATHS line in its place', which duplicates those arms, and the gov-line arm still skips silently. This only affects the spec's account of test coverage, not behaviour. | sound | - |
| 17 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 (the UP's forwarder write, rev-5 fold text) against PLAY-dConvergedCharter-17 section 2 S2 | medium | medium | confirmed | Unit 9 S4 (rev-5 diff) has the UP assemble `read_shim_rows` + `render_shim` and apply its own 'absent path or over that marker' rule. Unit 17 S2 (lines 55-60) puts the same rule inside `write_shims`' row loop. At base, `write_shims` (shims.py:267-279) is one inline loop that overwrites any differing dest, and there is no per-row writer to reuse. So the one rule that keeps an edited Skill would have two implementations. read_shim_rows' `troot` parameter (shims.py:60-67) exists and S4 never names it. That sub-claim is weak, though: the skill forwarder template (unit 17 §4) spells only from/to under `.claude/skills/` and no policy path. The two copies agree today and only five forwarders are affected, so the effect is contained. | sound | - |
| 18 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (the new 'Their two enforcers read them at HEAD' sentence); section 7 Gates | high | medium | confirmed | Unit 11 S1 (lines 81-85) makes check-memory-hygiene.sh:651 pass `--rev HEAD` and gotchas.py pass `rev="HEAD"`. Both suites rely on there being no landed revision. check-memory-hygiene.test.sh:264-268 says 'no fixture has a landed revision, every check-6/7 breach refuses', and :1632 asserts the READER_REFUSED text. gotchas.py:846-849 makes the same assumption for its master-only scratch. In budgets.resolve_caps (:218-251), a successful read_revision at HEAD with no policy file leaves `budgets.enforce` at its catalogue default `warn` (catalogue.toml:1315-1317). The READER_REFUSED rule then no longer applies, and those assertions break. §7 (line 781) lists `memory hygiene` but not `memory-hygiene self-test` or `gotchas selftest`. Both legs exist in gate-legs.json with guards on `{prefix}/memory-tree/`. The change edits files under that guard, so the bar would still select them and the red surfaces there rather than shipping, which keeps this at medium. | sound | borrowed-seed-inherits-its-head-state |
| 19 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 ('Each leg whose suite now reads through the policy kit names it in its guard'); section 6 AC30 | high | high | confirmed | gate-legs.json gives seven legs a guard that names a folded home (.memory-tree.conf, .lexicon.conf or .codebase-map.conf), as the finding lists, and none names `.governance/policy.toml`. legacy-homes.txt marks those homes' keys owner-policy (for example .codebase-map.conf rows 5-10 and RECALL_FLOOR at 52), so S2 moves their values into the policy file. input_key/build_key_text (run-gates.sh:3300-3346) hash only the guard's ls-files listing and dirt, plus the declared reads. S4's guard paragraph (lines 297-301) and AC30 cover only policy-kit code files for seven named suites. As a result, a policy.toml edit leaves legs like `recall floor` and `codebase-map gate coverage` with unchanged keys, and the bar reuses their stale greens. `lexicon naming predicates` declares a `history` read, so a committed edit does move its key, but an uncommitted edit still does not. This is a stale certification on the narrow path of an owner policy edit. | sound | - |
| 20 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the leg-guard list) and section 7; section 6 AC30 | medium | medium | confirmed | S4 re-points `row_grammar.resolve_root`, `map_lib.resolve_root` and the adopt-codebase-map walk to `legacy --root` (lines 282-288). S1 (lines 75-77) re-points corpus_ids check 16 through S4. Yet S4's guard list (lines 297-301) names only scratch-guard, format-guard, agent-cap, process-monitor adopter, lexicon, drift-audit and manifest-check. The relevant guards in gate-legs.json are: `row-grammar selftest` and `corpus-ids selftest` ['{prefix}/lib/','{prefix}/memory-tree/'], `codebase-map kit selftest` ['{prefix}/codebase-map/','{prefix}/lib/','{prefix}/lexicon/'] and `codebase-map adopter e2e` ['{prefix}/codebase-map/','{prefix}/lib/']. None names the policy kit. §7 (line 781) omits `row-grammar selftest` and `corpus-ids selftest`. AC30 reads only the legs S4 names. This is not a duplicate: it is a gap in the fix to the prior C21 finding. | sound | held-suite-guard-misses-a-sibling-kit |
| 21 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md:section 2 S1 (the new sentence on the three legs' guards); section 6 AC12 | medium | medium | confirmed | Unit 41 S1 (lines 124-125) and AC12 (lines 406-408) name only `pre-push self-test`, `transition-audit arms` and `straggler-guard arms`. S1 (lines 83-88) re-points `transition_audit.read_modes` to `render_folded_lines` and names its second caller, migrate_backlog.py:1325 (confirmed in code). The `backlog migration selftest` leg runs migrate_backlog.py --selftest with guard ['{prefix}/lib/','{prefix}/memory-tree/']. The `pre-push run-log line` leg runs .githooks/pre-push.runlog.test.sh, which drives the hook whose gate-key reads at pre-push:1453-1454 S1 re-points. Its guard is ['.githooks/','{prefix}/runlog/','{prefix}/run-gates/']. Neither guard names `{prefix}/policy/policy.py`, so a change to policy.py alone reuses both legs' greens. | sound | held-suite-guard-misses-a-sibling-kit |
| 22 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the WALK-UP resolver sentence); section 6 AC29 | high | medium | confirmed | The three walk-ups exist as cited. merge-rows.py:218-235 `_anchor_root` raises RuntimeError. transition_audit.py `resolve_root` raises Problem and runs in commit-msg. backlog.py `_resolve_anchor_at` returns 'no .memory-tree.conf above this file'. Specs 11 and 41 never name them, and AC29 runs only row_grammar and map_lib. The claimed consequence is overstated, however. S4 states the per-level shape as a class rule ('A WALK-UP resolver ... takes the shape PER LEVEL') and says 'The rest DERIVED at the pass by S5's presence red'. S5's arm reds any `.is_file()` naming a folded home on a code line unless the adapter is in the same condition. Its population (`derive_code_files`, CODE_PATHSPECS `*.py`) includes all three files, and FOLDED_HOME_EXEMPT exempts only `read_modes`, not `resolve_root`. So the builder is forced to re-point them. What remains real is that the named list, the Files-touched entry and AC29 miss them, so a wrong per-level re-point there (stopping at the kit directory) would go unobserved. | sound | move-inventory-misses-readers-by-path |
| 23 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 (the manifest moved to memory/project/), section 4 Files touched, section 8 F5 | high | medium | confirmed | Hygiene check 3 (check-memory-hygiene.sh:903-965) admits under memory/project/ only its named .txt registries, plus whatever PROJECT_REGISTRY_EXTRA lists. Gov's PROJECT_REGISTRY_EXTRA (.memory-tree.conf:925) does not list SESSION-KICKOFF.md, so `memory/project/SESSION-KICKOFF.md` would be reported. .governance/deploy.toml:65 and AGENTS.md:91 say '`memory/project/` holds only the gates' row registries'. Spec 7 S8 (line 111) and F5 move the manifest there, and grep finds no mention in spec 7 of check 3, PROJECT_REGISTRY_EXTRA or the :65 rule. PROJECT_REGISTRY_EXTRA is legacy-homes row 46 (owner-policy), so unit 11 folds it into the guarded policy file. The memory hygiene leg would catch this as a red rather than ship it, hence medium. The false charter line remains. | sound | - |
| 24 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 6 AC14 | medium | medium | confirmed | AC14 (spec 7 lines 412-417) only stages the deploy.toml edit in a non-TTY shell and expects `policy-guard: refused`, then expects exit 0 from a terminal. `.governance/deploy.toml` is already in tools/policy/guarded-paths.txt:8, and guard.py:5-12 already refuses any non-cap change by a non-TTY agent. So the AC is green before S8 is built. Its red case ('the pass plans an agent commit') cannot be observed by that command, and a --no-verify commit or a folded agent commit would pass. The owner-commit route that rev-5 added is therefore certified only by the guard's pre-existing behaviour. | sound | rule-stated-with-no-check-that-fails |
| 25 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC33 | medium | medium | confirmed | I ran AC33's own grep at HEAD and it printed nothing (exit=1). The four named files contain no `"legacy"` key read at all: git grep for `["']legacy["']` over tools/policy, settings_census.py and check-kit-placeholders.py hits only budgets.py's unrelated `how == "legacy"`. So the criterion is green before the unit is built. The pattern `get\(.legacy.\)` needs `)` straight after the key, so it cannot match `row.get("legacy", "")`. The second half compares `legacy --keys` with `legacy`, and S1 line 57 makes `derive_home_folds` the source of both, so it cannot diverge. The one-reader rule has no check that can fail. | unsound | a-grep-for-a-word-is-a-presence-probe |
| 26 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (agent-cap bullet, the fold's re-word of help/spec-audit.md:19, tools/hooks/README.md:159 and the deny strings); section 6 AC32 | medium | medium | confirmed | The tree has `SPEC_AUDIT_DEFAULT=""` at .unattended.conf:326 and a row for it at legacy-homes.txt:111. The held rule (S2, spec lines 108-113) holds a key only when its default differs from gov's value, and gov's value is blank, so S2 moves the line. S4 (lines 233-236) re-words the help page, README and deny strings to name `unattended.spec-audit-default` in the policy file. The driver still reads the opt-in from `git show $_cb:.unattended.conf`, evaluated at unattended.sh:4193-4206. Check 19 at check-unattended.sh:2150 and :3028 also reads only `.unattended.conf` commits. Neither spec 11 nor spec 41 names check_authorization or check 19; the only `unattended.sh` re-point is `:746`. Unit 12 removes the kit later, so between units 11 and 12 an owner who follows the re-worded page sets a value that agent-cap admits and the driver never sees. | sound | two-readers-of-one-config-one-re-derived |
| 27 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (`budgets.py resolve` gains `--rev <rev>`); section 4 Files touched and Minted | low | low | confirmed | S1 (line 83) adds `--rev` to `budgets.py resolve`. S10 (lines 368-371) declares new flags only for `policy.py#legacy` and `check_policy.py`. tools/govkit/usage.toml:159-164 keeps `flags = ["--explain"]` for the budgets resolve row. help/size-caps.md:40 anchors that row at fp8 `cfbc2b02`, and docs_leg.py:16-17 computes the fingerprint over the row's shape fields, so adding the flag moves the anchor. In scan_cap_requests (check_policy.py:584-587), any token not led by `-` is read as a cap, so `--rev HEAD` would yield a `HEAD` cap. The spec's own enforcers do not reach that path: the hygiene engine calls `budgets.main([...])`, which REQUEST_SHAPES does not match, and gotchas passes a kwarg. The effect is contained to documentation and a hypothetical shell enforcer. | sound | - |
| 28 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the closing 'Each leg whose suite now reads through the policy kit names it in its guard' paragraph) and section 6 AC30; also PLAY-dConvergedCharter-41 section 2 S1 (the three legs) and AC12 | high | high | confirmed | I read the guards in tools/gate-legs.json. `row-grammar selftest` has ['{prefix}/lib/','{prefix}/memory-tree/']. `codebase-map kit selftest` has codebase-map/lib/lexicon, and `codebase-map adopter e2e` has codebase-map/lib. `run-gates turnstile` has run-gates/lib, `run-gates adopter e2e` and `profile-bar selftest` have run-gates only, and `gotchas selftest` has lib/memory-tree. None of these names a policy-kit file. S4 re-points row_grammar.resolve_root, map_lib.resolve_root (tools/codebase-map/selftest.py:154-186 drives it), adopt-codebase-map.sh's walk, the run-gates legs-parse python and gotchas' `rev="HEAD"` read. S4's guard paragraph lists only seven legs. AC30 checks only 'each leg S4 names', so a guarded bar skips these suites when policy.py or budgets.py changes. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 29 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the legs-parse python's procmon branch; the walk-up resolvers); also PLAY-dConvergedCharter-41 section 2 S1 (`read_modes`, `held_halves.py` bullets) | high | high | confirmed | tools/run-gates/kit.toml:15 and tools/memory-tree/kit.toml:7 both read `requires = []`. The registry's default selection (tools/govkit/registry.toml:38-53) carries run-gates, memory-tree and codebase-map but not policy, so a default adopter has no policy kit. S4's general rule is that 'a missing python, kit or valid policy file refuses naming the reader'. S4 also hands the legs-parse python the presence question on every run. Today that python's procmon branch never ends the program (run-gates.sh:2836-2842). The spec does not say what it does when the policy kit is absent. Spec 41 S1 (lines 83-93) names no resolver and no absent-kit fallback for held_halves.py, and none for read_modes beyond 'the inlined resolve_kit_dir'. Only drift_report's re-point states its unresolved-kit behaviour. | sound | core-depends-on-an-optional-part |
| 30 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S3 (`render_folded_lines` / `legacy --rev`) and section 5 error states; with the history readers the fold adds (S4 drift_report.py; PLAY-dConvergedCharter-41 S1 `read_modes`) | medium | medium | confirmed | Grep over specs 11 and 41 for invalid, on-invalid, TOMLDecode, 'last valid' and validate printed nothing. policy.py:724-750 shows the kit's existing rule: read_revision sets `table = None` when validation finds problems, and resolve_read then takes read_last_valid_value. Invalid text can land, because the owner's TTY commit is not schema-checked. guard.py:141-149 only parses the text to judge an agent's raise shape. So the spec leaves open how the history readers it adds (drift_report, read_modes) treat a past invalid blob. Under S4's refuse rule such a blob refuses forever. | sound | - |
| 31 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (drift_report.py bullet, `signal_lexicon_ratified_stale` via `git log -G` ... `langs =` in `.governance/policy.toml`) and AC28 | medium | medium | confirmed | Spec 11 S4 (line 295) keys the policy-file half of signal_lexicon_ratified_stale on `git log -G` touching `langs =`. The current lookup at drift_report.py:1342 is `-G LANGS= -- .lexicon.conf`, a line regex. The LANGS value at .lexicon.conf:24 is a long single line with many members. An owner who re-spells `langs` as a multi-line array, or writes `langs=` with no spaces, makes an edit that `-G 'langs ='` never returns. The gateable signal then stays at 0. AC28's narrowing commit uses whatever spelling the fixture writes, so it would not catch this. | sound | - |
| 32 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC32 | high | medium | confirmed | I ran AC32's grep at base. It printed only help/spec-audit.md:19, agent-cap.js:44 and :1426. In agent-cap.js the deny string at :1477-1478 splits `.unattended.conf` and `SPEC_AUDIT_DEFAULT` across two lines. The deny strings at :1590 and :1595 spell the path as `${conf}`, bound at :1587 by `path.join(root, '.unattended.conf')`. tools/hooks/README.md has the key on :159 and the path on :160. After the three single-line hits are re-worded, AC32 prints nothing while those strings still name the retired home. S4 names these lines explicitly, so the shipped defect needs the builder to miss them as well; the consequence is stale text. | sound | - |
| 33 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC33 (with section 2 S1 'ONE READER OF THE FIELD') | high | high | confirmed | Spec 11 :773-777 (AC33) greps `\[.legacy.\]\|get\(.legacy.\)` over four named paths only. `printf 'x = row.get("legacy", "")' \| grep -cE` with that regex printed 0, because `get\(.legacy.\)` needs `)` straight after the quote, so a default argument escapes it. Running AC33's git grep at the tip printed nothing (exit=1), so the criterion is already green before the unit is built. S1 :57-60 says 'no other code reads the field', but AC33 does not test that across the tree. A second derivation written with the house `.get(key, default)` form, or placed in any file outside the four, passes it. | unsound | vacuous-selector-empty-population |
| 34 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 ('The DOWN clears the forwarder, then restores the old render byte-identical') and section 6 AC4 | high | high | confirmed | Spec 9 S4 :100-101 says 'The DOWN clears the forwarder, then restores the old render byte-identical' unconditionally. The Migration :207 repeats it. The same paragraph gives the UP three outcomes: withdrawn, `edited` kept and named (:88, :99-100), and absent, which gains the forwarder alone (§5 :253). Nothing keys the DOWN on which outcome the UP had. Rolling back an adopter whose edited Skill was kept would write the kit render over that edit, and rolling back an absent adopter would create a Skill it never had. AC4 :279-280 observes the DOWN only under the `rename` plant. A sibling step already has the primitive this needs: `fanout_cap.py:201-203` restores through `STEPS.write_from_before_image` (`upgrade_steps.py:1121`, `:1192`), and spec 9 never names it. | sound | - |
| 35 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S1 (THE ADOPTER'S COMMIT ROUTE) | medium | medium | confirmed | Spec 20 S1 :89-97 says `update` stages the home lines' removal with the policy file, and that 'until N+1 ... scratch-guard reads UNARMED, a window the route needs no routed write in'. It never says what happens when commit N, which is the owner's from a terminal, never comes. `scratch-guard.js:1157-1160` denies every write except to the conf while UNARMED. An agent or unattended session that ran `update` is therefore locked out of Write and Edit, as is any other session in that checkout, and the spec states no rollback. The effect is contained: Bash `git restore` can still recover it, and nothing is lost. | sound | - |
| 36 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (`procmon-hook.js`'s `resolveRoot` (:48-59) walks by the policy file, as above) | medium | medium | confirmed | Spec 11 :237-238 ('its root walk `:50-53` finding the root by the policy file') and :288 (`resolveRoot` 'walks by the policy file') give procmon-hook a different predicate from the per-level presence shape that the same sentence gives the other walk-up resolvers (:282-285). `procmon-hook.js:48-59` has an env branch at :50 that tests `.process-monitor.conf`, and the spec leaves it unaddressed. Null is the hook's only 'not adopted' test (:102-103). Walking by the policy file's existence treats any policy-kit repo as monitor-adopted. The effect is contained because the hook only runs where its settings fragment was installed. | sound | - |
| 37 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-40.md:section 2 S2 ('Each amend's record is written BEFORE the manifest is rewritten') and AC3 `amend-interrupted` | medium | medium | confirmed | Spec 40 S2 :65-70 writes the record before the manifest. The record part is skipped only when a record whose `After` equals the amended row's hash exists. S3 :75 and AC :196 cover `amend-interrupted` only for a re-run with the same plan. If the plan's `help` is corrected before the re-run, the new `After` differs, so a second `edit` record is written from the same `Before` and the first is left as an orphan claiming a change that never reached disk. The same orphan is left when no re-run follows. Nothing in the spec removes or flags it. The effect is limited to the record trail. | sound | - |
