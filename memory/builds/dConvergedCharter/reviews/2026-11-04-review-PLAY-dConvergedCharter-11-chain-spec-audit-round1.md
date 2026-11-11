**Serves:** spec-audit PLAY-dConvergedCharter-11@rev-6 PLAY-dConvergedCharter-17@rev-3 PLAY-dConvergedCharter-38@rev-2 PLAY-dConvergedCharter-41@rev-2 PLAY-dConvergedCharter-20@rev-5 PLAY-dConvergedCharter-21@rev-4 PLAY-dConvergedCharter-13@rev-4 PLAY-dConvergedCharter-40@rev-1 PLAY-dConvergedCharter-7@rev-4 PLAY-dConvergedCharter-9@rev-4

# Tier-2 spec audit: dConvergedCharter, ten chain units (11, 17, 38, 41, 20, 21, 13, 40, 7, 9), round 1

*This was an adversarial pre-code pass over ten spec units of the Convergence build of the dClosedLoop chain. The build has no run-mandate prompt, so the README is the mandate: close the 15 owned gaps, with one roster unit per clause. Synthesised by gov-synthesizer on 2026-11-04. Every item below survived a skeptic who was prompted to refute it.*

Reviewed: memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md@12e9bc55b4ac959959ea567e4eab9858ebc0d8cf, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md@06019f2e2e704552c2a049b3ba61d704bee50d52, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-38.md@3f7133e92235a3d645ceab2734de6cf95f63e778, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md@e6b7f6f1f746d9c3aaaf90aef58296f6c01039a0, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md@0e69ef8134c893ea7d2fbc6e17d27f282e570678, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md@4659ee194f586c79207e6afe3c9cfa8ef578b65d, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md@c2a026768735c882d95ab17e32f0889117c89ba1, memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-40.md@8a176b21255fe5dcde362351a2349ca4c2c8c197, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md@745ca217161f3f9d5405be4390725fdd12b30615, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md@d18670b98185d0f8bd424019bcbf72540ab4cc98

ROUND: 1

## Verdict: BLOCKED

One item is a blocker. Unit 11 moves `READ_PATH_WAIVER`, a path list, into a count-typed `budgets.*` key, and that invalidates the policy file (B1).

Four HIGH items cover five findings, and each must be fixed before the build pass:

- Unit 11's moved caps are read at the landed revision, so the branch grades with the engine defaults (H1).
- Unit 11 drops `LANGS=` from `.lexicon.conf` and leaves drift-audit's raw readers blind (H2).
- Unit 11's presence shape stops walk-up root resolvers one or more levels too deep (H3).
- Unit 20's adopter fold leaves the mirror stale and has no commit route past the policy guard (H4).

Unit 21 has no confirmed finding.

## Review shape

Intensity full: raw 38, confirmed 35, refuted 3, unverified 0 (0 uncertain), precision 0.92.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 8 | 5 | 3 | 0 | 0 | 0.63 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 1 BLOCKER, 4 HIGH, 21 MEDIUM, 6 LOW (32 items).

Adjudicated tally by raw confirmed finding: blocker 1, high 5, medium 21, low 8 (35 findings).

Merges: H1 holds findings 2 and 12. L1 holds findings 7, 17 and 33.

Findings 1 (medium) and 11 (blocker) describe one defect, but their binding grades differ, so they sit in separate items. M1 points to B1's fix. I would grade finding 1 at blocker with finding 11. Under `on-invalid = "last-valid"`, the count-type refusal silently drops the whole fold's values rather than being caught. The binding medium grade stands.

Findings 12 (high, H1) and 36 (medium, M19) share a root cause: a landed-revision read. They concern different readers, so they stay separate items.

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdicts: 0 contradictory demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 32 judged sound, 3 judged UNSOUND (findings 26, 34 and 37, whose items give the skeptic's corrected fix), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (findings 1, 3 and 7).
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 18 spec documents were supplied as `specs`, as sibling context.
- Checklist: 102 items, each assigned to one lens (coherence 21, grounding 21, reuse 20, blast-radius 20, failure-envelope 20).
- By design: 2 invariants from the checklist's by-design block.
- Move check: no checked subject moved.

Every count is zero where it should be, so this run is complete as a run.

Refuted and not carried: finding 20 (unit 7 F2, whose ask is filed as PLAY-dConvergedCharter-33), finding 25 (unit 9 withdrawal, already reasoned in §4) and finding 27 (unit 21 F4, an open owner fork).

## BLOCKER

### B1. Unit 11 moves `READ_PATH_WAIVER`, a path list, into a count-typed `budgets.<cap>` key (finding 11)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md`, §2 S1 (the `conf:` cap paragraph) and S2, and §4 Evidence and Inventory ("six conf: caps keeping budgets.<cap>").
- **What is wrong:**
  - S1/S2 take the "six at base" cap set from legacy-homes rows 35, 36, 38, 39, 48 and 58, and move gov's value of each into `budgets.<cap>`.
  - Row 48 is `READ_PATH_WAIVER`. In `caps.toml:333-341` it is `cited-file-cap`, class `correctness`, and its value is a path list (`.memory-tree.conf:535`).
  - The catalogue types `budgets.*` as `{ type = "count", min = 0 }`.
  - `budgets.resolve_caps` refuses a cap outside the switch class.
  - `corpus_ids.py:773` reads `conf["READ_PATH_WAIVER"].split()` straight from the conf.
- **Consequence:**
  - S2 writes a string into a count key, which makes the policy file invalid. With `policy-file.on-invalid = "last-valid"`, every reader silently falls back to the last valid revision, so the whole fold's values are ignored.
  - Dropping the conf line also empties the waiver. Hygiene check 16 rule 3 then reds `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
  - AC24 and §5's claim that caps are read through budgets is false for this row.
- **Fix (skeptic: sound):**
  - Narrow S1/S2's cap set to `[[cap]]` rows of class `switch`: INDEX/DOSSIER × BYTES/LINES and UNIVERSAL_BUDGET.
  - Restate "six at base" as derived from the census rows with `class = switch`.
  - Treat `READ_PATH_WAIVER` as an ordinary folded key. Either give it a catalogue row with a list `allowed` and a `legacy` field and re-point `corpus_ids.py` through S3, or hold it in the conf. Say which in S1.
  - Add an AC: after S2, `python policy.py check` exits 0 and check 16 still reads the waiver.
- **Left-shift gate:** have `policy.py check` (or the catalogue shape audit) red any `budgets.<cap>` whose `caps.toml` row is not class `switch`. Add a checklist entry: "a move set derived from a row list is re-derived from the row's class, not typed".

## HIGH

### H1. Unit 11's moved caps are read at the landed revision, so the unlanded branch grades with the engine defaults (findings 2, 12)

**Specs:** PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-41

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md`, §2 S1 (conf: caps) and S3, §5 risks, and §6 AC24. The same landed-revision read hits unit 41's `held_halves.py` re-point; see M19.
- **What is wrong:**
  - S3 reads folded keys at HEAD so that an unlanded fold sees its own values. The caps S1 moves into `budgets.<cap>` get no such rule.
  - `budgets.resolve_caps` reads the policy file through `policy.read_revision`. With no rev, that read uses `derive_landed_revision` (`policy.py:732`).
  - The callers pass no revision: `check-memory-hygiene.sh:645-651` calls `budgets.main(["resolve","--explain",…])`, and `gotchas.py:510` calls `resolve_caps` the same way.
  - `budgets.py` has no `--rev` flag.
- **Consequence:**
  - From S2 until the landing, origin/main sets no `budgets.<cap>` and the conf line is gone. Each cap falls back to the engine constant: INDEX_CAP_BYTES 20480 instead of gov's 61440, INDEX_CAP_LINES 250 instead of gov's 0, and the dossier and universal caps at their constants.
  - The hygiene leg grades gov's tree with caps gov never declared.
  - AC24 prints the default, so it cannot pass before landing.
- **Fix (skeptic: sound):**
  - Give the caps the HEAD rule S3 gives folded keys. Either the hygiene engine and `gotchas.py` pass `--rev HEAD` to `budgets resolve` (a new flag), or `resolve_caps` gains the HEAD read. The alternative is to hold the cap lines in gov's conf until landing, as the HELD rule does. Say which in S1.
  - State plainly which readers (`budgets`, `get`) read the landed revision.
  - Rewrite AC24 to run on a clone whose remote default branch is the fold's parent, as AC16 does, with `--rev HEAD`. Add a red case where the landed ref lacks the value.
- **Left-shift gate:** add a fixture arm that runs every reader of a folded value on a scratch clone whose origin predates the fold, and expects gov's value. Add a checklist entry: "every reader of a moved value names its revision (HEAD or landed)".

### H2. Unit 11 drops `LANGS=` from `.lexicon.conf` and breaks drift-audit's raw readers of it (finding 28)

**Specs:** PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-41

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md`, §2 S2 and S3 (the `.lexicon.conf` fold), §4 "The readers", and §7.
- **What is wrong:**
  - S2 removes `LANGS=` from `.lexicon.conf`. It is not held, because `tools/lexicon/kit.toml` has no `required_keys`.
  - `tools/drift-audit/drift_report.py` reads that line raw. `build_lang_mode_findings` (:367-392) compares HEAD's text against the base blob through `git show`. `signal_lexicon_ratified_stale` (:1318-1351) runs `git log -1 -G LANGS= -- .lexicon.conf`.
  - Neither reader goes through `lexicon_conf.load_conf`, so S3's overlay never reaches them.
  - No spec names `drift_report.py`. §7 omits the unguarded `drift-audit records` leg and `drift-audit selftest`.
- **Consequence:**
  - The fold commit reds `drift-audit records` on every bar. Every armed extension reads as "moved parser -> absent, WEAKENS coverage", and the fold commit itself reads as a LANGS edit newer than the ratified stamp.
  - After the fold, a `lexicon.langs` edit in the policy file never touches `LANGS=`, so the staleness signal stays at zero for good. That is a check reporting fresh over a moved language surface.
- **Fix (skeptic: sound):**
  - Name `drift_report.py` as an S4 reader. Re-point the ratchet by revision: `policy.py legacy .lexicon.conf --rev <base>` and `--rev HEAD --key LANGS`.
  - For staleness, take the newest commit touching either `LANGS=` in `.lexicon.conf` or the `lexicon.langs` row of `.governance/policy.toml`.
  - Add `drift-audit records` and `drift-audit selftest` to §7.
  - Add an AC: `drift_report.py --check` on a scratch clone after S2 prints no LANGS ratchet line. Its staged break is a policy-file `lexicon.langs` edit with no restamp, which must red.
- **Left-shift gate:** have the fold's census (S9) also grep `git log -G <KEY>=` and `git show …:<home>` call sites for each folded home, and red any not listed as a reader. Add a checklist entry: "history readers (`git log -G`, `git show rev:home`) are readers too".

### H3. Unit 11's presence shape stops walk-up root resolvers one or more levels too deep (finding 34)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-11.md`, §2 S4 (the fifth shape, the presence readers) with S3 (`--root`).
- **What is wrong:**
  - S4's presence shape reads "adopted when `policy.py legacy <home>` prints a folded key, or the home exists".
  - S3 reads `--root <dir>` as `git -C <dir>`, which resolves the toplevel from any subdirectory.
  - Walk-up resolvers test presence at each ancestor: `row_grammar.py:133` `resolve_root` (named by S4), `map_lib.py:84` `resolve_root`, `adopt-codebase-map.sh:16` and `procmon-hook.js:47-58`.
  - Applied per iteration, the shape is true at the first directory (the kit's own), because `legacy` reads the toplevel's policy file.
- **Consequence:** each re-pointed walk returns `tools/memory-tree`, `tools/codebase-map` or a cwd subdirectory as the repository root. Every path derived from it (MAP_ROOT, the memory root, the procmon root) is silently wrong by the kit's prefix, in gov and at every adopter. S5's presence red checks the shape of a test, not where it is applied, so it does not catch this.
- **Fix (skeptic: UNSOUND; this is the skeptic's corrected fix):**
  - Name the walk-up class in S4. Such a reader keeps the per-directory `home exists` test. Only at the directory where the walk stops for `.git` does it run `legacy <home> --root <that dir>`, and a printed folded key there counts as presence.
  - `procmon-hook.js` keeps S4's walk by the policy file.
  - List `map_lib.resolve_root`, `adopt-codebase-map.sh` and `row_grammar.resolve_root` by name.
  - Add an AC: over a folded scratch clone with the conf deleted, each resolver run from its kit dir returns the clone's toplevel.
  - Do NOT make `--root` refuse, or read nothing, at a non-toplevel dir.
- **Left-shift gate:** add a fixture arm that runs every `resolve_root`/`resolveRoot` from its kit dir on a folded, conf-less scratch clone and compares the result with `git rev-parse --show-toplevel`. Add a checklist entry: "a presence test inside an ancestor walk is evaluated per level".

### H4. Unit 20's adopter fold leaves the mirror stale and has no commit route past the policy guard (finding 35)

**Specs:** PLAY-dConvergedCharter-20

- **Where:** `2026-11-03-spec-PLAY-dConvergedCharter-20.md`, §2 S1 and S2 (the home mode's write, at an adopter).
- **What is wrong:**
  - S1 writes `.governance/policy.toml` and removes the home lines in one staged change.
  - Nothing regenerates `.governance/policy.json`, and nothing names the commit route past `guard.py`, which refuses an agent's commit of the policy file.
  - Unit 11 prices both for gov: S2's commit route, and the §4 Migration rule that a hook key leaves its home only once the mirror at HEAD is fresh.
  - Adopters carry a mirror (`upgrade_walk.py:264`).
- **Consequence:**
  - Once the adopter commits, the mirror at HEAD is stale against `policy_blob`, so `readFoldedKey` falls back to home lines that are gone. Scratch-guard then reads blank `MEMORY_ROOT`/`ROUTED_PATHS` and denies every write as UNARMED.
  - Where pre-commit runs `guard.py --staged`, an agent running `govkit update` cannot commit the step's output at all.
- **Fix (skeptic: sound):**
  - In S1, state the adopter's commit route. Either the policy-file write is the owner's terminal commit, followed by a mirror commit before the home lines leave (unit 11 S2's two commits, carried to the adopter), or the step keeps each node-hook key's home line until the mirror is re-rendered at HEAD.
  - Add an AC: on a scratch adopter clone after `update` and its commit, scratch-guard admits a routed write and prints no UNARMED.
  - Add an AC: a non-TTY commit of the staged output is refused by `policy-guard`, and the documented route commits.
- **Left-shift gate:** extend the upgrade-walk fixture to commit `update`'s output on a scratch adopter and then exercise scratch-guard. Add a checklist entry: "any write to a guarded path names its commit route".

## MEDIUM

### M1. Unit 11 moves `READ_PATH_WAIVER` into a count-typed `budgets.<cap>` key, seen from AC1 (finding 1)

- **Where:** unit 11, §2 S1 (the conf: caps paragraph) and S2, and §6 AC1.
- **What is wrong:** this is the same defect as B1. Row 48 (`READ_PATH_WAIVER`, a path list) is in the cap move, `budgets.cited-file-cap` accepts only a count, and `corpus_ids.py` check 16 reads the conf directly.
- **Consequence:** either `policy.py check` refuses the value, so AC1 cannot pass, or check 16 rule 3 loses gov's waiver.
- **Grade:** the skeptic graded this medium (the finder graded it high), on the grounds that gates catch it. I disagree, as the review shape explains: under `last-valid` the count-type refusal drops the fold's values silently. The binding grade is kept.
- **Fix (skeptic: sound):** take `READ_PATH_WAIVER` out of the cap move. Fold it as an ordinary key (list type, `legacy = ".memory-tree.conf READ_PATH_WAIVER"`, `corpus_ids.py` re-pointed through `policy.py legacy`) or hold it, and say which in S1. Add an AC that runs check 16 over gov's tree after S2 and expects no rule-3 finding for the two waived files. This is the same fix as B1.
- **Left-shift gate:** as B1.

### M2. The legs of unit 11's and unit 41's re-pointed suites do not guard the policy-kit files they now read (finding 3)

- **Where:** unit 11, §7 Gates and §4 Files touched. Also unit 41, §7.
- **What is wrong:**
  - `scratch-guard.js`, `format-guard.js` and `agent-cap.js` now call `policy-mirror.js`'s `readFoldedKey`.
  - `adopt-process-monitor.sh`, `lexicon_conf.py`, `pre-push` and the straggler guard's suite now call `policy.py legacy`.
  - None of their legs' guards in `tools/gate-legs.json` names `tools/policy/policy-mirror.js` or `policy.py`.
- **Consequence:**
  - A change that edits only `policy-mirror.js` or the `legacy` verb skips those suites, or reuses their old green.
  - AC12's staged red sits in a file the scratch-guard leg's guard never trips.
  - The post-merge full bar contains the effect.
- **Grade:** the skeptic re-graded this from high to medium.
- **Fix (skeptic: sound):**
  - In units 11 and 41, add `{prefix}/policy/policy-mirror.js` and `{prefix}/policy/policy.py` to each affected leg's `guard`, in its descriptor and in `tools/gate-legs.json`. Add `.governance/policy.toml`/`.json` where the suite reads them.
  - List those legs in §4.
  - Add an AC: `--legs-for` over a one-line change to each of the two files prints every re-pointed suite's leg.
- **Left-shift gate:** have the spec-tokens guards join red a re-point whose new import or call target is not in the reader leg's guard (bug class held-suite-guard-misses-a-sibling-kit).

### M3. Unit 17's AC4 reds a correct build on `/build` hits that S4 never re-points (finding 4)

- **Where:** unit 17, §6 AC4 against §2 S4.
- **What is wrong:**
  - AC4 expects `--readers /build --kind value` to exit 0 with only `registry.toml`, `shims.toml` and `usage.toml` excepted.
  - The value-token boundary also matches lines outside S4's list and held set: `WIRE-INTO-PROJECT.md:328` (a records path followed by a space), `tools/govkit/selftest.py:2818` and `:9547`, `.gitattributes:141`, and `tools/unattended/VERBS.template.md:821`.
  - S4's claim that the right boundary excludes records-directory hits holds only when `/` follows.
- **Consequence:** a build done exactly as S4 says exits 1. To pass, the builder must reword a correct runbook line or add excepts AC4 forbids.
- **Fix (skeptic: sound):**
  - Add these lines to S4's reader list, or reword the runbook line.
  - Better, state AC4's except set as derived: run the readers command at the pass and sort each hit into re-pointed or excepted, with its reason.
  - Correct S4's boundary sentence: a records hit followed by a space or quote is a value hit.
- **Left-shift gate:** add a checklist entry: "an AC's except set is the output of its own command at base, not a typed list".

### M4. Unit 11's AC25 docs half loops over an empty population (finding 5)

- **Where:** unit 11, §6 AC25 (second half).
- **What is wrong:**
  - The loop runs "for each folded name `python policy.py lists` prints".
  - Bare `lists` is a usage error (exit 2).
  - `lists --check` and `--write` print legacy-home rows, which S2 drains of folded keys.
- **Consequence:** the docs-anchor check runs over nothing and always passes. A folded key with no `help/policy.md` anchor passes AC25 (bug class fixture-passes-by-finding-nothing).
- **Fix (skeptic: sound):**
  - Take the population from the catalogue: each `[[key]]` row with a `legacy` field, read through tomllib over `tools/policy/catalogue.toml` or a new `policy.py` listing.
  - Print the count, and red where it is 0 or differs from the 95 rows S1 mints.
- **Left-shift gate:** add a checklist entry: "every loop-shaped AC prints and floors its population count".

### M5. Unit 41's S1 deletion list misses lines AC2's no-except grep still finds (finding 6)

- **Where:** unit 41, §2 S1 (the copies' deletion list) against §6 AC2.
- **What is wrong:** `read_policy_key` still appears at `tools/unattended/unattended.sh:10259` and `:11220` (comments), `unattended.test.sh:5373` (a comment) and `:15467` (`unset -f … read_policy_key …`). None of these is in S1's list. AC2 runs with no `--except`, and unit 12 removes the kit only later.
- **Consequence:** a build that follows S1 fails AC2 at unit 41's tip.
- **Fix (skeptic: sound):** add those four lines to S1's delete-or-reword list. Better, define S1's list as the AC2 command's output at the pass's base.
- **Left-shift gate:** the same checklist entry as M3, on derived lists.

### M6. Unit 11 cites the wrong seam in `run-gates.sh` for procmon presence and keeps a gate that is now always false (finding 13)

- **Where:** unit 11, §2 S4 (the fifth shape, `.process-monitor.conf`) and §10 (`run-gates.sh:1532-1541`).
- **What is wrong:**
  - Lines 1532-1541 are a comment block and shell defaults. The legs-parse python is at :2831.
  - At :2830 the python is handed the procmon args only when `[ "$PROCMON_CONF" = 1 ]`.
  - S4 says the prelude "keeps only the default PROCMON_CONF=0" and never says :2830's condition changes.
- **Consequence:** read literally, the python never gets the procmon question, and gov's bar silently loses tree-kill delegation. AC18 catches it, so the effect is contained.
- **Fix (skeptic: sound):** cite `run-gates.sh:2829-2843` (the argv[5..7] branch). State that the python is always handed the presence question and answers PROCMON_CONF in its leading line, and that :2830's condition is replaced.
- **Left-shift gate:** have spec-tokens resolve `file:line` citations and red a cited range that is comment-only (checklist entry: "a cited seam is code").

### M7. Unit 38's AC2 "no bash sees the script" case cannot be staged on a Git-for-Windows node (finding 14)

- **Where:** unit 38, §2 S2 (the announce line when no bash sees the script) and §6 AC2 (second half).
- **What is wrong:** `check_policy.resolve_bash` (:896-915) always tries the fixed Git for Windows paths after `GOV_BASH` and PATH, and both paths exist on gov's nodes. Setting `GOV_BASH` to a 127 stub cannot remove every candidate.
- **Consequence:** the red half of AC2 goes unrun or passes vacuously, so the announce branch ships as a gate never seen red.
- **Fix (skeptic: sound):**
  - Stage the case by injection: give `read_live_carriers` or `resolve_bash` a candidate-list parameter, or have the fixture monkeypatch `resolve_bash` to return None.
  - Assert the "live carriers: not read — … no bash sees …" line and exit 0.
  - State in AC2 why the environment cannot produce the case.
- **Left-shift gate:** add a checklist entry: "a staged-absence case is injected, not produced by environment".

### M8. Unit 7's S8 re-points the guarded `.governance/deploy.toml` with no owner commit route (finding 15)

- **Where:** unit 7, §2 S8 (`manifest_path` at `.governance/deploy.toml:54`, the `:68` reader) and §4 Files touched.
- **What is wrong:** `.governance/deploy.toml` is in `tools/policy/guarded-paths.txt`. `guard.py` refuses any agent commit to it other than a single budgets cap raise. Unlike unit 11 S2, unit 7 names no owner-terminal route.
- **Consequence:** the agent commit that moves `SESSION-KICKOFF.md` is refused at pre-commit. The pass stalls, cannot land unattended, or is tempted toward `--no-verify`.
- **Fix (skeptic: sound):**
  - Add the commit route to S8 and §4 Migration. The deploy.toml edit is the owner's terminal commit, staged and handed over as unit 11 S2 does, and it lands before the agent commit that removes the guides.
  - Add an AC that observes the guard refusing an agent-staged deploy.toml edit on a scratch clone.
- **Left-shift gate:** spec-tokens reds a §4 Files touched entry that matches `guarded-paths.txt` when the spec names no owner commit route.

### M9. Unit 40's amend change record carries `Successor` and leaves `Proof` unset, against the parent edit grammar (finding 16)

- **Where:** unit 40, §2 S2 (the amend's change record) and §4 Evidence.
- **What is wrong:** S2 writes `Action edit` with `Successor none`. PLAY-dOrderedCharter-15 S7 carries `Successor` on every action but `add` and `edit`, and requires `Proof`. S2 sets no `Proof`, though unit 40's own line 101 lists it.
- **Consequence:** `build_records.py new change` either refuses every amend or accepts a shape that unit 20's status derivation reads differently from an ordinary edit.
- **Fix (skeptic: sound):** drop `Successor`. Name `Proof` (`none — <reason>` for an agent pass). Have AC1 assert that the field set equals the parent's edit shape.
- **Left-shift gate:** add a parity arm in `build_records.py`'s suite that renders each action's field set from one grammar table.

### M10. Unit 41 gives the straggler guard its own shell parser of the policy file, named like an existing govkit function (finding 21)

- **Where:** unit 41, §2 S1 (straggler-guard bullet), §4 Inventory and §5 security.
- **What is wrong:**
  - A new shell `read_policy_value` reads `[memory-tree]` `backlog-mode`. That is a second policy-file reader, against the policy kit's one-reader decision.
  - It contradicts unit 11 §4, which says the straggler guard reads `legacy <home> --rev <sha>`.
  - It contradicts unit 41's own §5: "no reader parses a policy home in shell any more".
  - The name duplicates `govkit.read_policy_value` (`govkit.py:274`), which has a different contract.
- **Consequence:**
  - Another valid TOML shape reads as unset, so the guard reads `shards` while `policy.py` reads `builds`.
  - §5 misleads the next change.
  - A reuse lookup finds two contracts under one name.
- **Fix (skeptic: sound):**
  - Read through a reader the policy kit owns, or pay one `legacy --rev` python spawn per distinct blob pair.
  - If a shell parse is kept, record it as a ruled exception to TOOL-dGroundRules-2, with a parity arm against `policy.parse_policy`, and correct §5.
  - Rename the function, for example `read_policy_backlog_mode`.
  - Make unit 11 §4 agree.
- **Left-shift gate:** a namesake check over all languages (not only `sh.function`) at mint time, and a grep gate for shell parses of `.governance/policy.toml`.

### M11. Unit 41's `transition_audit.read_modes` reads the policy blob with no named parser (finding 22)

- **Where:** unit 41, §2 S1 (the `transition_audit.read_modes` bullet).
- **What is wrong:** `read_modes` reads each commit's policy blob with `memory-tree.backlog-mode` winning, but S1 names no parser. Unit 11 §4 says this by-revision reader uses `legacy .memory-tree.conf --rev <sha>`. The policy kit already offers `parse_policy`, `read_policy_text` and `render_folded_lines`.
- **Consequence:** the builder writes a third parse. `read_modes`, and `migrate_backlog.py:1325` that consumes it, can drift from `policy.py legacy --rev`, and no AC holds them equal.
- **Fix (skeptic: sound):**
  - S1 says `read_modes` reads distinct policy blobs through `parse_policy` (reached by the inlined `resolve_kit_dir`), or through `render_folded_lines(repo, sha, '.memory-tree.conf')` per distinct blob pair.
  - AC3 asserts equality with `policy.py legacy .memory-tree.conf --rev <sha> --key BACKLOG_MODE` at each commit.
- **Left-shift gate:** the same grep gate as M10, for new policy-blob parsers outside `tools/policy/`.

### M12. Unit 11 S1 and unit 20 S1 name catalogue types (`int`, `bool`, `string`) that do not exist (finding 23)

- **Where:** unit 11, §2 S1 (the `allowed` type rule) and S3 (the rendering rule). Also unit 20, S1 and AC1.
- **What is wrong:**
  - The catalogue grammar knows COUNT_TYPES, SET_TYPES (`set`, `list`), `enum`, `pattern`/`name`, durations and literal lists (`policy.py:105-107`). `check_value` refuses any other type (:196).
  - S3 mints a fresh renderer and never names `render_toml_value`.
- **Consequence:** a literal build writes rows the shape audit refuses. An ad hoc mapping leaves S3's render and unit 20's inverse parse free to disagree on a row shape neither names.
- **Fix (skeptic: sound):**
  - Restate S1 in the catalogue's vocabulary: `{ type = "count", min = … }`, `{ type = "list" | "set" }`, a flag as a literal `allowed` list, a free string as `{ type = "pattern" }`.
  - Key S3's render and unit 20's inverse on those shapes, and reuse `render_toml_value`'s bool and number spellings.
  - Rename unit 20 AC1's "int row" and "list row" to match.
- **Left-shift gate:** spec-tokens checks catalogue type names cited in specs against `policy.py`'s type tuples.

### M13. The home-to-folded-keys map is derived independently in five places (finding 24)

- **Where:** unit 20, §2 S1 (`derive_home_folds`). Also unit 41, S1 (the kit-placeholders bullet), and unit 11, S3, S5 and S9.
- **What is wrong:** the map from a home to its folded KEYs, read from the catalogue's `legacy = "<home> <KEY>"` field, is parsed separately in five places:
  - unit 20's `derive_home_folds` in `conf_to_policy.py`;
  - unit 41's `extract_conf_keys` addition;
  - unit 11's `render_folded_lines`;
  - unit 11's `scan_reader_keys` expansion;
  - unit 11's census.

  Unit 20's claim that it "reads one map (I5)" is false by its own Inventory.
- **Consequence:** the copies can disagree on home spelling or normalisation. The upgrade step can then strip a key the verb treats as unfolded, or the placeholder arm can miss one.
- **Fix (skeptic: sound):**
  - Unit 11 mints one `derive_home_folds(kit, home)` in `policy.py`, used by `render_folded_lines`, `scan_reader_keys` and the census.
  - Expose it through `policy.py legacy <home> --keys`. Unit 20 S1 and unit 41's placeholder bullet call that.
  - Add a parity assertion to unit 11's arm.
- **Left-shift gate:** add a checklist entry: "an interface shared across units names one owner function, not a shared field".

### M14. Unit 9's UP deletes the old Skill, and nothing renders the forwarder at an adopter (finding 26)

- **Where:** unit 9, §2 S4 and S5, and §4 Migration.
- **What is wrong:** the Migration says `shims.py --write` renders the forwarder at the old path after the UP clears it. `govkit update` never calls `write_shims`, and no `[[files]]` row ships `.claude/skills/<old>/SKILL.md`.
- **Consequence:**
  - At every adopter, `/memory-recall`, `/runlog`, `/lexicon`, `/drift-audit` and `/cleanup` vanish at the update, with no forwarder for the promised deprecation window.
  - The open shim rows read green only in gov's tree.
- **Fix (skeptic: UNSOUND; this is the skeptic's corrected fix):**
  - Have `skill_rename.py`'s UP render the forwarder for its `[[shim]]` row at the target's old path, right after clearing it. It calls `shims.py`'s render for that row, rooted at the target, under the `skill` kind's write rule: write only at an absent path or over this row's own `gov:shim <id>` marker, and name and keep a target's edited Skill.
  - The DOWN removes the forwarder before restoring the old render. The WITNESS checks for the forwarder.
  - Drop the Migration's per-adopter `shims.py --write` sentence.
  - Add an AC: `govkit update --write` over a scratch adopter finds the forwarder at `.claude/skills/<old>/SKILL.md`. Its staged break is the UP skipping the render, which must red.
- **Left-shift gate:** have the upgrade walk assert every open `[[shim]]` row's `from` path exists at the scratch adopter after `update`.

### M15. Unit 11's S2 moves the gate-file keys and leaves govkit check 7h3 and selftest M5 with nothing to check (finding 29)

- **Where:** unit 11, §2 S2 (the gate-file keys moved) and §4 Files touched.
- **What is wrong:**
  - S2 moves `INHERITED_RED`, `INHERITED_RED_MAX_AGE` and `GATE_DOC_PATHS` out of `.githooks/gate-env.sh`.
  - govkit check 7h3 (`POLICY_KEYS` at `govkit.py:58`, :2823-2867) then has an empty population on gov's tree.
  - Selftest M5's gov-line arm (`selftest.py:9244-9249`) skips silently under `if _gov_line:`.
  - Neither spec names them.
- **Consequence:**
  - 7h3 reports `gate policy: 0 file(s)` and stays green, and it cannot see a TOML-held `gate.*` value in a shipped file.
  - One selftest arm goes dead with no red (empty population read as coverage).
- **Fix (skeptic: sound):**
  - Add `govkit.py` (`POLICY_KEYS`, `build_policy_re`, 7h3) and `selftest.py` M5 to S2's readers.
  - Either widen 7h3 to grade shipped TOML assignments of folded `gate.*` rows, or state the narrowed population and turn M5 into a fixture plant.
  - Add an AC: after S2, 7h3 reds a planted kit-shipped file assigning the folded key.
- **Left-shift gate:** add a checklist entry: "a selftest arm reading a live file reds when the read is empty".

### M16. Unit 11's §7 omits the `manifest-check self-test` leg for a file it re-points (finding 30)

- **Where:** unit 11, §7 leg line, against §4 Files touched.
- **What is wrong:** §4 names `skills/session-kickoff/manifest-check.sh`. Its guard, `skills/session-kickoff/`, is carried by 3 legs, which is under BROAD_LEG_FLOOR=5. §7 lists two of those legs but not `manifest-check self-test`.
- **Consequence:**
  - The re-pointed presence read ships with no named suite run.
  - Once the spec is promoted out of DEFERRED, the `spec tokens` guards join reds it.
- **Fix (skeptic: sound):** add `manifest-check self-test` to §7.
- **Left-shift gate:** the guards join already exists. Run it over DEFERRED specs in an audit too, so the miss surfaces before promotion.

### M17. Unit 11's Migration and F5 miss the `unattended-status` fork-ceiling row (finding 31)

- **Where:** unit 11, §4 Migration (fork-ceiling entrypoints) and §8 F5.
- **What is wrong:**
  - S4 re-points `unattended.sh:746`'s top-level `. "$CONF"` to a captured `policy.py legacy` call.
  - That makes `unattended-status` (ceiling 47) dearer, and its setup copies no `.governance/policy.toml`.
  - Migration and F5 name only `memory-hygiene` and `manifest-check`.
- **Consequence:**
  - The unguarded spawn-budget leg reds, and no F5 ruling covers the row.
  - Without the policy file in setup, the row measures a different code path from the one gov runs.
- **Fix (skeptic: sound):**
  - Add `unattended-status` (and `check-unattended` if it sources the conf) to Migration's measured set and to F5, and have its setup copy and commit `.governance/policy.toml`.
  - Or derive the set by running `fork-count.sh` on a scratch clone before and after the re-points.
- **Left-shift gate:** add a checklist entry: "fork-ceiling rows affected by a re-point are derived by measurement, not named".

### M18. Unit 11 leaves help, README and deny-string carriers telling users `SPEC_AUDIT_DEFAULT` lives in `.unattended.conf` (finding 32)

- **Where:** unit 11, §2 S2/S4 readers (SPEC_AUDIT_DEFAULT) and §4 Files touched.
- **What is wrong:** the key moves and is not held. Four carriers still place it in `.unattended.conf`:
  - `help/spec-audit.md:19`;
  - `tools/hooks/README.md:159`;
  - `agent-cap.js`'s deny strings (:44, :1426, :1478, :1590-1595);
  - `agent-cap.js:1466`, which is the only one the spec names (as a read to re-point).
- **Consequence:** the help page and the refusal text direct the owner to a line `readFoldedKey` ignores once the mirror sources the row. Behaviour is correct, but the guidance is wrong, against the charter's [docs] rule.
- **Fix (skeptic: sound):**
  - Add these carriers to S4's readers, re-worded to name `unattended.spec-audit-default` in `.governance/policy.toml`.
  - Add a grep AC: after S2, `git grep -n 'unattended.conf' -- help/spec-audit.md tools/hooks/README.md` places no `SPEC_AUDIT_DEFAULT` there.
- **Left-shift gate:** have the census (S9) also grep `<home>.*<KEY>` co-mentions in prose and string literals, and red unlisted ones.

### M19. Unit 41's `held_halves.py` reads `gate.wsl-parity-runs` at the landed revision with no default (finding 36)

- **Where:** unit 41, §2 S1 (the `held_halves.py` bullet).
- **What is wrong:**
  - `policy.py get` with no `--rev` reads the landed revision. Unit 11 S3 rejects that for every other folded reader.
  - `resolve_wsl_host` refuses a blank count, so the catalogue default ("its reader's default") is undefined.
  - `derive_landed_revision` refuses on a clone with no resolvable landed ref.
  - The spec does not map a non-zero `get` exit.
- **Consequence:** on the run branch after S2, the parity count reads an undefined default, and on unusual clones `get` refuses unhandled.
- **Fix (skeptic: sound):**
  - Read through `policy.py legacy .githooks/gate-env.sh --key GATE_WSL_PARITY_RUNS` (HEAD), as the mechanic key beside it is read. If `get` is kept, pass `--rev HEAD` and state the row's default.
  - A non-zero exit refuses through `print_refusal`, naming the key.
  - Add an AC on a scratch clone whose remote default branch predates the move.
- **Left-shift gate:** as H1.

### M20. Units 13 and 40 skip a move that wrote its row but not its change record (finding 37)

- **Where:** unit 13, §2 S1 (`write_moves`' idempotence) and S4 (row, then change record). Likewise unit 40, S2.
- **What is wrong:** `written(move)` reads only the row. A run that dies between the row append and the `build_records.py new change` write re-runs as "skipped … already at", and the record is never written. S6's `feature-interrupted` plant only interrupts between moves.
- **Consequence:** a kit row promoted from a guide has no change record, and the re-run reports success. Unit 13's migration AC (records = feature rows) catches it at gov's pass.
- **Fix (skeptic: UNSOUND; this is the skeptic's corrected fix):**
  - Split the destination test per part. Skip the row append where an active row with that help exists.
  - Separately skip the record write where a change record with `Promoted-from` = the section tag and `After` = `<tag>@<hash8>` already exists. For unit 40, that is `Action edit` with the same Before/After.
  - A re-run then writes only the missing part.
  - Add `feature-record-interrupted`: the record write raises after the row is appended, and the re-run writes the record and no second row. Add the same plant for unit 40's amend.
- **Left-shift gate:** add a checklist entry: "a multi-part write's idempotence test checks each part".

### M21. Unit 40 does not say how two plan entries that target one tag interact (finding 38)

- **Where:** unit 40, §2 S1 (the two refusals) and §6.
- **What is wrong:** the conflict refusal reads "the manifest", but S1 never says whether that is the manifest on disk or the would-be tree after the plan's earlier amends. No plant has two entries with one `target`. Unit 7 S7 makes that case reachable: two sections of one guide can map to one tag.
- **Consequence:** read against disk, both entries pass. The second overwrites the first's `help` within one pass and writes two edit records, which is what the refusal exists to prevent.
- **Fix (skeptic: sound):**
  - State that the conflict test reads the would-be row after earlier entries.
  - Or refuse a plan with two entries on one `target` (exit 2, naming both sections and the tag), or define the merge.
  - Add plant `amend-two-sections` and its AC.
- **Left-shift gate:** add a checklist entry: "a per-entry refusal names whether it reads base or would-be state".

## LOW

### L1. Unit 7's S8 move of `SESSION-KICKOFF.md` misses the fork-ceiling row and the codebase-map card (findings 7, 17, 33)

- **Where:** unit 7, §2 S8 Readers (the moved manifest's readers), §4 Files touched, §6 AC10 and §7 Gates.
- **What is wrong:**
  - S8 moves `memory/guides/SESSION-KICKOFF.md` to `memory/project/`.
  - `memory/project/fork-ceilings.txt:20`, the `manifest-check` row, copies the old path in its setup and passes it as argv.
  - `memory/map/features/session-kickoff.md:19,24,36` globs the old path.
  - None of these is in S8's readers or §4, and §7 omits `spawn budget (forks per hot entrypoint)` and `codebase-map coverage + freshness`.
  - AC10's pathspec excludes only `memory/builds`, so it also hits `memory/DECISIONS.md:123`.
- **Consequence:**
  - The spawn-budget row's setup `cp` fails after the move.
  - The builder's write set, ceiling re-measure and map regeneration are unbudgeted.
  - AC10 reads red on a correct build because of DECISIONS.md.
  - S8 line 140's re-derivation and the unguarded leg contain this.
- **Grade:** the skeptic re-graded finding 7 from medium to low.
- **Fix (skeptic: sound, all three):**
  - Add `memory/project/fork-ceilings.txt` (setup and argv re-pointed to `memory/project/SESSION-KICKOFF.md`, count re-measured; re-pointing a setup path is not a ceiling raise) and `memory/map/features/session-kickoff.md` with its renders to S8 and §4.
  - Add both legs to §7.
  - Exclude frozen records outside `memory/builds` (`:!memory/DECISIONS.md`, `:!memory/archive`) from AC10, or name them as admitted hits.
- **Left-shift gate:** add a checklist entry: "a file move's readers are the output of `git grep <old path>` at base, including `memory/project` and `memory/map`".

### L2. Unit 38 writes the fixture verb with the wrong grammar and the wrong owner (finding 8)

- **Where:** unit 38, §6 preamble.
- **What is wrong:** the preamble writes `python check_policy.py --fixture <case> <dir>`, which it calls unit 11's verb. The real grammar is `--fixture [--strict-from <dir>] [<case>]` (`check_policy.py:4577`), and the verb already exists at base.
- **Consequence:** running the cited form is a usage error (exit 2), and the builder corrects it.
- **Fix (skeptic: sound):** rewrite the preamble to the code's grammar, as units 11 and 41 have it, and drop the claim that unit 11 owns the verb.
- **Left-shift gate:** spec-tokens checks cited CLI forms against each tool's `USAGE`.

### L3. Unit 11's §4 and S6 give two different populations for `derive_readers` (finding 9)

- **Where:** unit 11, §4 "The readers" against §2 S6.
- **What is wrong:** §4 calls `derive_readers(repo, <home>, "path")` "over `CODE_PATHSPECS`". S6's signature has no pathspec parameter and walks every tracked text file, prose included.
- **Consequence:** the builder has two answers to one question (bug class two-answers-to-one-question). §4's last sentence makes the intent recoverable.
- **Fix (skeptic: sound):** pick one. Either add a `pathspecs` parameter that §4 passes, or have §4 filter S6's output to `CODE_PATHSPECS` and say prose hits are re-worded.
- **Left-shift gate:** add a checklist entry: "a call named in §4 matches its §2 signature".

### L4. Unit 13's hands-off edge to unit 1 names the wrong mover (finding 10)

- **Where:** unit 13, §3 Edges (hands-off PLAY-dConvergedCharter-1).
- **What is wrong:** the edge names only `dossier_move.py`'s plan and apply. Unit 1 uses `guide_move.py` and its write route, to which unit 1 adds `--residue`.
- **Consequence:** the edge graph is misleading. Unit 1's own text is correct.
- **Fix (skeptic: sound):** reword the edge to "`guide_move.py`, the guide caller of the factory `prose_move.py`, with S4's write route, to which unit 1 adds `--residue`".
- **Left-shift gate:** an edge-pair check that a hands-off edge's interface matches the consumer's consumes-from edge.

### L5. Unit 11 S3 cites `policy.py:1362` for a toplevel lookup it does not do (finding 18)

- **Where:** unit 11, §2 S3 ("with no --root, the cwd's toplevel (policy.py:1362)").
- **What is wrong:** `:1362` passes `"."`, the cwd, not its toplevel. The explicit toplevel lookups are at :944, :1409 and :1449.
- **Consequence:** a builder copying the precedent reads the home from a subdirectory, misses the root conf, and lets each reader's default stand.
- **Fix (skeptic: sound):** cite `run_git(".", "rev-parse", "--show-toplevel")` at `policy.py:1409`, and state that the working-tree home is read under that toplevel.
- **Left-shift gate:** as M6, citation resolution.

### L6. Unit 13 cites an unbuilt envelope precedent as live (finding 19)

- **Where:** unit 13, §4 Evidence (the envelope precedent).
- **What is wrong:** `render_envelope` in `tools/lib/envelope.py` under a PARITY_ROWS row does not exist at HEAD. It is PLAY-dOrderedCharter-3's unbuilt row.
- **Consequence:** a builder looking for the precedent finds nothing. The pattern itself stands in live rows.
- **Fix (skeptic: sound):** cite a live PARITY_ROWS row, for example `resolve_bash_py` (`tools/lib/resolve-python.test.sh:369`), or mark the envelope as unbuilt.
- **Left-shift gate:** spec-tokens reds a present-tense path citation that is absent at HEAD.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=38 confirmed=35 refuted=3 unverified=0 blocker=1 high=5 medium=21 low=8 agents=11 out-tokens=272775

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (the conf: caps paragraph) and S2; section 6 AC1 | high | medium | confirmed | Spec 11 lines 59-64 tell S2 to write gov's value of every `conf:` cap key to `budgets.<cap>`, and they name legacy-homes rows 35, 36, 38, 39, 48 and 58. Row 48 prints as `.memory-tree.conf READ_PATH_WAIVER owner-policy`. caps.toml:334-338 maps `cited-file-cap` to `home = "conf:.memory-tree.conf:READ_PATH_WAIVER"`. catalogue.toml:1309-1310 types `budgets.*` as `{ type = "count", min = 0 }`. .memory-tree.conf:535 holds a path list, `"memory/HYGIENE.md memory/TEMPLATE-SPEC.md"`, and corpus_ids.py:773 reads `conf["READ_PATH_WAIVER"].split()` straight from the conf. Spec 11 never names READ_PATH_WAIVER, so it gives no special rule for it. Built as written, either the count type refuses the value or check 16 rule 3 loses gov's waiver. Both outcomes are caught by gates (`policy check` or memory hygiene), so the effect is contained: medium. | sound | - |
| 2 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (conf: caps) and S3; section 6 AC24 | high | high | confirmed | budgets.py:207-221 `resolve_caps` calls `policy.read_revision(repo, rev, rows)`. policy.py:732 resolves a `rev` of None through `derive_landed_revision`. budgets.py has no `--rev` CLI flag (grep found none). check-memory-hygiene.sh:645-650 calls `budgets.main(["resolve", "--explain", ...])` with no revision, and gotchas.py:510 calls `resolve_caps([request], root)` with none either. Spec 11 gives HEAD reads only to folded keys (lines 156-157, 197, 794); caps get no such rule. Once the conf lines leave on the unlanded branch, the landed policy file sets no `budgets.<cap>`, so each cap falls back to the engine constant. That is INDEX_CAP_BYTES=20480 against gov's 61440 (check-memory-hygiene.sh:138 vs .memory-tree.conf:483), and INDEX_CAP_LINES 250 against gov's 0. So AC24 cannot print gov's value before landing, and the hygiene leg grades with the wrong caps on the branch. | sound | - |
| 3 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 7 Gates (and section 4 Files touched); also PLAY-dConvergedCharter-41 section 7 | high | medium | confirmed | I read the guards out of tools/gate-legs.json. scratch-guard self-test has ['{prefix}/hooks/','{prefix}/lib/','skills/session-kickoff/']. agent-cap self-test has ['{prefix}/hooks/','{prefix}/lib/']. process-monitor adopter selftest has only its adopter and its test. lexicon selftest has ['{prefix}/lexicon/']. pre-push self-test has ['.githooks/','{prefix}/lib/']. straggler-guard arms names no policy file. None of these names tools/policy/policy-mirror.js or policy.py. Spec 11 lines 191-196 re-point the node hooks through a new `readFoldedKey` export of policy-mirror.js. Its §7 deals only with the census leg's narrow guard (line 673). The run-gates README (:122-125, :394-397) confirms a guard-selected leg is skipped, or its old verdict reused, when its guard does not name an input it reads. The post-merge full bar re-runs it, so the effect is contained. | sound | held-suite-guard-misses-a-sibling-kit |
| 4 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md:section 6 AC4 (against section 2 S4) | medium | medium | confirmed | I ran `git grep -nP '(?<![A-Za-z0-9_])/build(?![A-Za-z0-9_/-])' -- ':!memory'`, which matches S6's value-token boundary in spec 11 line 295. Its hits include WIRE-INTO-PROJECT.md:328 (`.../<your-slug>/build --record-as`, a records path followed by a space), selftest.py:2818 and :9547 (comments), .gitattributes:141 (a comment), and also tools/unattended/VERBS.template.md:821. None of these is in spec 17 S4's re-point list or its held set, which names only selftest.py:2872,2889 and .gitattributes:143. AC4 admits only `registry.toml`, `shims.toml` and `usage.toml` as excepts, so a build done exactly as S4 says exits 1. S4's claim that the right boundary excludes records-directory hits holds only when `/` follows. | sound | - |
| 5 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC25 (second half) | medium | medium | confirmed | `timeout 60 python tools/policy/policy.py lists` printed the usage line and exit=2. policy.py:1509 dispatches `lists` only for `--check` or `--write`, and `cmd_lists` (:1443-1492) prints legacy-home rows and counts, never folded key names. Spec 11 never redefines bare `lists` (its only `lists` mentions are --write and --check, at lines 108, 126, 515, 617, 756). So AC25's docs half has no valid population: as written it either errors or loops over nothing. | sound | fixture-passes-by-finding-nothing |
| 6 | coherence | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md:section 2 S1 (the copies' deletion list) against section 6 AC2 | medium | medium | confirmed | `git grep -n read_policy_key -- ':!memory/builds'` prints unattended.sh:10259 and :11220 (comments), unattended.test.sh:5373 (a comment) and :15467 (`unset -f ... read_policy_key ...`). None of these is in spec 41 S1's deletion list (lines 44-47: pre-push:1416-1421, post-merge.sh:170, push-main.sh:401-402, and test lines 1007-1011, 1560, 15431, 15551). AC2 (lines 317-323) runs with no `--except` and is red while any comment naming the function survives. Unit 12 removes the unattended kit only after this unit (the hands-off at line 192), so a build that follows S1's list fails AC2. | sound | - |
| 7 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 (the readers of the moved manifest); section 7 Gates; section 6 AC10 | medium | low | confirmed | memory/project/fork-ceilings.txt:20, the manifest-check row, does `cp "$ROOT/memory/guides/SESSION-KICKOFF.md"` and passes that path as argv. Spec 7 S8's reader lists (lines 114-140) do not name fork-ceilings.txt, and §7 (line 390) omits `spawn budget (forks per hot entrypoint)`, which has no guard in gate-legs.json. AC10's pathspec excludes only memory/builds, so it hits memory/DECISIONS.md and other memory files. The consequence is mitigated two ways, though. S8 line 140 says the build re-derives both reader halves by `git grep` at its first pass, which would surface fork-ceilings.txt. And because the spawn-budget leg has no guard, it runs on every bar, so a break is caught anyway. AC10's own wording, 'no reader outside the frozen records', partly admits DECISIONS.md. That leaves the omissions and AC10's inexact pathspec as a contained documentation gap. | sound | - |
| 8 | coherence | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-38.md:section 6 preamble (the fixture verb) | low | low | confirmed | Spec 38 line 160 reads 'The fixture is `python check_policy.py --fixture <case> <dir>`, PLAY-dConvergedCharter-11's verb'. In check_policy.py:4575-4588, USAGE is `--fixture [--strict-from <dir>] [<case>]`, and `main` returns 2 with usage when more than one positional follows. Spec 41 line 303 gives the code's grammar. A builder running spec 38's form gets an immediate usage error and corrects it, so nothing ships wrong. | sound | - |
| 9 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 4 'The readers' against section 2 S6 | low | low | confirmed | Unit 11 is at blob 12e9bc55. §4 'The readers' (lines 391-392) says the population is `derive_readers(repo, <home>, "path")` 'per folded home over `CODE_PATHSPECS`'. S6 (line 292) gives the signature `derive_readers(repo, needle, kind)`, which has no pathspec parameter, and its walk is 'every tracked text file outside the memory root, tests, help pages and comment lines included'. The two do not agree on the population. §4's last sentence says prose-only files are re-worded and S5 grades only code, so the builder can work out what is meant, and the effect is contained. | sound | two-answers-to-one-question |
| 10 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md:section 3 Edges, hands-off PLAY-dConvergedCharter-1 | low | low | confirmed | Unit 13 is at blob c2a02676. The hands-off edge to unit 1 (line 112) names only `dossier_move.py`'s plan and apply as the factory, 'which unit 1 calls for the residue'. Line 74 of the same spec says unit 1 adds `--residue` to the guide route. Unit 1 names guide_move 14 times and dossier_move 2 times. Its consumes-from edge (line 104) names both the factory and `guide_move.py` with its write route. So unit 13's edge leaves out the interface unit 1 actually uses. The effect is limited to the edge graph. | sound | - |
| 11 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (the conf: cap paragraph) and S2; section 4 Evidence and Inventory ('six conf: caps keeping budgets.<cap>') | blocker | blocker | confirmed | Re-probed. legacy-homes.txt rows 35, 36, 38, 39, 48 and 58 are DOSSIER_CAP_BYTES, DOSSIER_CAP_LINES, INDEX_CAP_BYTES, INDEX_CAP_LINES, READ_PATH_WAIVER and UNIVERSAL_BUDGET. Row 48 is in S1's 'six at base' set, which S2 writes to `budgets.<cap>`. In caps.toml:333-341, READ_PATH_WAIVER's row is cited-file-cap with class "correctness". The budgets.py docstring and resolve_caps (`if cap.cls in OUTSIDE: raise Refusal`) refuse a cap outside the switch. The catalogue row `budgets.*` has `allowed = { type = "count", min = 0 }`, and check_budgets makes a non-integer value a Problem. .memory-tree.conf:535 holds a path list. corpus_ids.py:773 reads `conf["READ_PATH_WAIVER"].split()` straight from the conf. policy.toml has on-invalid = "last-valid". Built as written, the fold writes a string into a count key, which invalidates the policy file. Removing the line from the conf also breaks check 16's waiver. | sound | - |
| 12 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (conf: caps), section 5 risks, section 6 AC24 | high | high | confirmed | Re-probed. budgets.resolve_caps calls policy.read_revision(repo, rev, rows), which reads derive_landed_revision when rev is None (policy.py:732). check-memory-hygiene.sh:651 calls `budgets.main(["resolve", "--explain", *sys.argv[2:]])` with no --rev. The engine hands in `legacy:` only when the conf sets the key and otherwise hands in `default:` with its constants. :138 shows INDEX_CAP_BYTES=20480 and INDEX_CAP_LINES=250, while gov's conf has 61440 and 0. Unit 11 handles HEAD versus landed only for `legacy` (S3, lines 153-157, AC20). It says nothing for the budgets caps. Unit 41 line 82 re-points held_halves through `policy.py get`, which also reads the landed revision. Between the commit that removes the conf lines and the landing, the caps fall to the engine defaults, and AC24 run on the branch would print the default. This happens only in the unlanded window and in warn mode, so high, not blocker. | sound | - |
| 13 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (fifth shape, .process-monitor.conf) and section 10 ('the legs-parse python (run-gates.sh:1532-1541)') | medium | medium | confirmed | Re-probed run-gates.sh. Lines 1532-1541 are a comment block, and the defaults are at 1539-1543, with PROCMON_CONF=1 set by the `-f` test at 1543. The legs-parse python is at :2831. :2830 hands it the procmon args only when `[ "$PROCMON_CONF" = 1 ]`, and it resolves the kit only when `len(sys.argv) > 7`. S4 does list :2830 among the sites PROCMON_CONF gates. It never says that :2830's condition must change, and it says the prelude 'keeps only the default PROCMON_CONF=0'. Read literally, the python never gets the question and tree-kill delegation is lost. AC18 would catch it, so the effect is contained. | sound | - |
| 14 | grounding | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-38.md:section 2 S2 (the announce line when no bash sees the script) and section 6 AC2 (second half) | medium | medium | confirmed | Re-probed. check_policy.py:896-915 `resolve_bash` tries GOV_BASH, then which(bash), then the fixed paths C:/Program Files/Git/bin/bash.exe and C:/Program Files/Git/usr/bin/bash.exe, then bare bash. `ls` shows both fixed paths exist on this node. Unit 38 AC2 (lines 175-176) stages 'no bash sees' only by setting GOV_BASH to a 127 stub 'and no other candidate seeing the script'. On a node with Git for Windows the fixed paths see the script, so the environment cannot produce that case. The fixture would then exit 1 instead of printing the announce line, which is either a red on a correct build or a case that is never run. On a node without those paths the case can still be staged through PATH, so the effect is contained. | sound | - |
| 15 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 (manifest_path `.governance/deploy.toml:54` and the `:68` reader) and section 4 Files touched | medium | medium | confirmed | Re-probed. tools/policy/guarded-paths.txt lists .governance/deploy.toml. guard.py:5-12 refuses any staged change to a listed path other than a single budgets cap raise, and its REMEDY says such a change is 'the owner's, committed from a terminal'. Line 54 of .governance/deploy.toml is manifest_path = "memory/guides/SESSION-KICKOFF.md", and line 68 names MERGE-BAR.md. Unit 7 (blob 745ca217) S8 re-points :54 and lists :68 among its readers. A grep for terminal, guarded and policy-guard in unit 7 finds no owner commit route, unlike unit 11 S2's THE COMMIT ROUTE. As written, the agent's commit is refused at pre-commit. | sound | - |
| 16 | grounding | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-40.md:section 2 S2 (the amend's change record) and section 4 Evidence | medium | medium | confirmed | Re-probed. In PLAY-dOrderedCharter-15 S7 (lines 97-104), `Successor` is 'on every action but `add` and `edit`', and `Proof` (`tty-cli` or `none — <value>`) is in the field list. Unit 40 (blob 8a176b21) S2 (lines 57-60) writes `Action edit` with `Successor none` and never names a Proof value. Unit 40's own line 101 lists Proof among the record's fields, yet S2 leaves it unset. The record does not match the parent's edit grammar, so the factory will either refuse it or accept a shape that differs from an ordinary edit. build_records.py does not exist yet, so which of the two happens is not observable today. | sound | - |
| 17 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 Readers (the manifest's readers) and section 4 Files touched | low | low | confirmed | Re-probed: `git grep -n 'guides/SESSION-KICKOFF' -- memory/project` prints memory/project/fork-ceilings.txt:20, the manifest-check row, whose setup cps "$ROOT/memory/guides/SESSION-KICKOFF.md" and whose argv names memory/guides/SESSION-KICKOFF.md. Spec 7's Files touched (lines 276-278) names the moved manifest's readers as only .governance/install.json, tools/kickoff-manifest/manifest-check.sh and tools/govkit/fixtures/release-0/deploy.toml. `grep fork-ceilings` on spec 7 finds nothing. AC10's grep would catch the stale path at the close, so the effect is contained to the builder's write set. | sound | - |
| 18 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S3 ('with no --root, the cwd's toplevel (policy.py:1362)') | low | low | confirmed | policy.py:1362 reads `hit = resolve(args.key, ".", args.rev)`, so it passes the cwd as the repo and never computes a toplevel. The explicit `rev-parse --show-toplevel` calls are at :944, :1409 and :1449. Spec 11 S3 (line 166) cites :1362 for 'the cwd's toplevel'. S3 also reads unfolded keys from the working tree's home (line 156), so a builder who copied the cited precedent would resolve that path from the cwd. The prose does say 'toplevel', so this is a wrong citation and its effect is cosmetic or narrow. | sound | - |
| 19 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md:section 4 Evidence (the envelope precedent) | low | low | confirmed | `ls tools/lib` shows no envelope.py. `git grep render_envelope -- tools` prints nothing, and PARITY_ROWS in tools/lib/resolve-python.test.sh:351 holds resolve_prefix_token and resolve_bash_py rows but no envelope row. Spec 13 line 126 describes render_envelope as 'canonical in tools/lib/envelope.py' in the present tense. Line 280 cites PLAY-dOrderedCharter-3 S3, which is unbuilt. Only the precedent citation is wrong, because the pattern exists in live rows. | sound | - |
| 20 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S6 and S8, section 8 F2 | high | - | refuted | The premise is false on re-probe. The finder grepped only memory/builds/dOrderedCharter/BACKLOG.md. The ask IS filed, in memory/builds/dConvergedCharter/BACKLOG.md:14 as PLAY-dConvergedCharter-33, target dOrderedCharter, with the same accept criterion F2 states ('a fixture unit whose edge targets a section of a retired guide passes `gov_tag.py check` while the same address with no edge reds the retirement rule'). BACKLOG.md:45 adds 'DEFERRED · PLAY-dConvergedCharter-33 · until PLAY-dConvergedCharter-7', so unit 7 is gated on it. Spec 7 line 191 also lists PLAY-dOrderedCharter-29 as an external consumes-from that must be built before this unit's pass. The retirement rule's conflict is therefore the declared, filed dependency, not an unrouted one. gov_tag.py does not exist at HEAD, so nothing reds today. check_rationale_kept asks whether the rationale was kept, which is not the alias-or-red question, so 'second check of the same thing' is a reuse preference. | unsound | two-guards-one-question-two-answers |
| 21 | reuse | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md:section 2 S1 (straggler-guard bullet), section 4 Inventory, section 5 security | medium | medium | confirmed | Spec 41 lines 91-100 have the straggler guard read the policy blob's `[memory-tree]` `backlog-mode` line through a new shell `read_policy_value`. The spec accepts that another TOML shape reads as unset. That contradicts spec 11 lines 395-398, which say the by-revision readers, the straggler guard named, read `legacy <home> --rev <sha>`. It also contradicts spec 41's own §5 security line (line 281): 'no reader parses a policy home in shell any more'. `git grep read_policy_value` confirms govkit.py:274 `def read_policy_value(key, root, rev=None)`, a different contract under the same name. Spec 41 line 235 checked the name only as sh.function. The divergence is bounded by the spec's own fail-direction argument and the suite's parity to legacy, so the effect is contained. | sound | - |
| 22 | reuse | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md:section 2 S1 (`transition_audit.read_modes` bullet) | medium | medium | confirmed | Spec 41 lines 78-81 have read_modes make the policy blob's `memory-tree.backlog-mode` win, but name no parser for that blob. transition_audit.py has no policy or tomllib reader today: grep finds only an unrelated 'git pin policy' comment at :52. Spec 11 lines 395-398 say read_modes, as a by-revision reader, reads `legacy <home> --rev <sha>`, so the two specs disagree. Spec 41's AC3 (line 325) checks a fixture's shards-then-builds outcome only and never holds read_modes equal to `policy.py legacy`, unlike the guard's suite parity. Drift between the two by-revision readers is therefore unguarded, though its effect is contained. | sound | - |
| 23 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1 (the `allowed` type rule) and S3 (the rendering rule); also spec 20 S1 and AC1 | medium | medium | confirmed | policy.py:105-107 defines SET_TYPES=(set,list) and COUNT_TYPES=(count,retry-count,...). check_value's fallthrough at :196 returns "the row's `allowed` type ... is not one this kit knows". There is no int, bool or string type. Spec 11 lines 54-57 state the row's `allowed` type as `int`, `bool` or 'a string row'. Spec 20 lines 65-67 key the inverse parse on 'list/int/bool/string', with no mapping to the catalogue's allowed shapes. Neither spec cites render_toml_value, which `grep render_toml_value` over the specs confirms. A literal reading writes rows the shape audit refuses, which the gate would catch. The ad hoc mapping risks a render and an inverse that disagree. | sound | - |
| 24 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S1 (`derive_home_folds`); also spec 41 S1 (kit-placeholders bullet) and spec 11 S3, S5, S9 | medium | medium | confirmed | Spec 20 line 44 and its Inventory at line 237 mint derive_home_folds in tools/govkit/steps/conf_to_policy.py, which reads catalogue `legacy` rows itself. Spec 41 lines 106-109 add a separate `legacy`-row read to extract_conf_keys. Spec 11 S3 (render_folded_lines), S5 (scan_reader_keys expansion, lines 288-289) and S9 (the census, lines 306-307) each read the same field. `grep derive_home_folds` over the specs hits spec 20 only. Spec 11 line 387 defines I5 as 'readers join on the `legacy` field', which is an agreement on a field and not one owner function. So spec 20's 'read one map' is several independent parses. The drift risk is real, but no concrete divergence is shown, so it is contained. | sound | - |
| 25 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 (the UP's withdrawal) | medium | - | refuted | The cited section already says this. spec-9 §4 Alternatives rejected (:228-232) quotes spec 20's rejection itself: 'Spec 20 §4 rejects a step deciding withdrawal for files `update` owns; this case differs because the path does not stay empty: S5's forwarder must be written there, so the UP clears it, deciding through `update`'s own classification.' So the two specs are not left contradictory, and the reason the rejection does not apply is stated. The UP only deletes on the grid's `withdrawn` cell or the precedent's kit-render recognition test, keeps an edited file (§5 security, :239-241), and the DOWN restores the file byte-identical. I checked govkit.py:8283-8292 (`("equal","absent"): "withdrawn"`) and :14000 (`--write-withdrawals` is the only way `update` itself deletes). That flag governs `update`'s withdrawal arm. Spec 9 deliberately puts this path under a step and gives the reason. | unsound | - |
| 26 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 and S5, section 4 Migration | medium | medium | confirmed | The first option, a `[[files]]` row shipping the forwarder at the old path, keeps the old path in the descriptor. The old row then never reads `withdrawn`: it reads stale, or diverged for an edit, so the UP's own classification goes dead. Ordering the UP after that install also makes the UP's recognition test (front matter `name: <old>`) find and withdraw the forwarder it just installed. The second option, adding a write_shims verb to `update`, is workable but names no write rule or ordering. | unsound | - |
| 27 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md:section 8 F4, section 2 S1 step (2) | medium | - | refuted | A parked fork withholds what this asks. spec-21 F4 (:288-298) is an open fork: it lists options (a), (b) and (c), recommends (a) and ends 'Open for the owner: this run holds no mandate.' What happens on a decline is exactly the owner's choice among those options, so the fork does not leave step (2) without a route: the owner ruling picks one. Filing the ask is also outside the spec writer's remit. F4 itself and README.md:50 confine writes outside the build to an ask row 'written by whoever dispatched this stage, never by a spec writer'. My grep of memory/builds/dShippedRelease/BACKLOG.md for 'unruled' or 'dConvergedCharter' printed nothing, which is consistent with the fork still being open, not with a defect in the spec. | unsound | owner-item-without-its-reject-outcome |
| 28 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S2 and S3 (the .lexicon.conf fold), section 4 "The readers", section 7 | high | high | confirmed | I confirmed it. legacy-homes.txt:23 holds `.lexicon.conf LANGS owner-policy`, and spec-11 S3 names LANGS as one of `.lexicon.conf`'s two folded keys. `grep required_keys tools/lexicon/kit.toml` printed nothing, so S2's held rule does not keep the line, and .lexicon.conf:24 is the `LANGS=` line S2 removes. drift_report.py:367-392 `build_lang_mode_findings` reads HEAD's raw text and the base blob through `git show`. drift_report.py:1343 `signal_lexicon_ratified_stale` runs `git log -1 -G LANGS= -- .lexicon.conf`. Neither goes through lexicon_conf, so S3's overlay never reaches them. After the fold, an edit to `lexicon.langs` in the policy file never touches `LANGS=`, so the gateable staleness signal goes blind for good. A grep of specs 11, 41 and 20 for drift_report finds nothing. gate-legs.json shows `drift-audit records` with no guard, and §7 omits both drift-audit legs. S4's generic rule ('every other reader derive_readers returns by path ... replaces its read with S3's output') might catch the ratchet's text read. It cannot express the git-history lookup, and the by-revision readers are said to be unit 41's named ones only. The result is a staleness check that reports fresh over a moved language surface. | sound | - |
| 29 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S2 (gate-file keys moved), section 4 Files touched | medium | medium | confirmed | I confirmed it. govkit.py:58 has `POLICY_KEYS = ("GATE_SELFTESTS","INHERITED_RED","INHERITED_RED_MAX_AGE","GATE_DOC_PATHS")`, and check 7h3 (:2823-2867) scans tracked non-.md files outside memory/ with `build_policy_re`. I ran that predicate read-only over the tracked tree and it printed exactly one file, `.githooks/gate-env.sh INHERITED_RED=land`. gate-env.sh:103, :104 and :108 assign the three owner-policy keys that S2 moves (legacy-homes.txt:11, :20, :21 owner-policy; GATE_SELFTESTS is mechanic and is not assigned). After S2 the population is 0. selftest.py:9245-9249 reads gov's `GATE_DOC_PATHS=` line, and under `if _gov_line:` that check silently skips. Specs 11 and 41 name neither POLICY_KEYS nor 7h3 nor M5. The effect is contained: 7h3's predicate stays armed for shell assignments in shipped files, but one selftest arm becomes dead with no red, and 7h3 does not see a TOML-held policy. | sound | - |
| 30 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 7 leg line (joined against section 4 Files touched) | medium | medium | confirmed | I confirmed it. spec-11 §4 Files touched names `skills/session-kickoff/manifest-check.sh`. In gate-legs.json the guard `skills/session-kickoff/` is carried by 3 legs (manifest-check self-test, scratch-guard self-test, lexicon naming predicates), which is not broad under BROAD_LEG_FLOOR=5 (check-spec-tokens.py:387). `grep -c 'manifest-check self-test'` on spec-11 printed 0, while §7 lists the other two legs. spec-token-waivers.txt holds no dConvergedCharter line. One part is overstated today: spec 11's status is DEFERRED, and check-spec-tokens.py:356 counts only OPEN/SPECCED/INPROGRESS/BLOCKED as LIVE, so the guards join does not red it yet. It will red once the spec is promoted for its build, and the declared gate set misses the leg that exercises the re-pointed file. | sound | - |
| 31 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 4 Migration (fork-ceiling entrypoints) and section 8 F5 | medium | medium | confirmed | I confirmed it. fork-ceilings.txt holds `unattended-status \| 47`, whose setup copies only `.unattended.conf` and `.memory-tree.conf` and then runs `unattended.sh --status tFork`. unattended.sh:746 is a top-level `. "$CONF"`, which S4's readers list names as re-pointed to a captured `policy.py legacy` call (a python start plus `$(…)` forks). The Migration's enumeration (spec-11 :423-426) reads '`memory-hygiene` and `manifest-check` at base', and F5 (:703-713) names only those two rows. The Migration's generic wording ('each fork-ceiling entrypoint a re-point changes') would reach the row in principle. The stated reading at base is wrong, though, and F5's owner ruling as framed does not cover it. Unit 12 removes the unattended kit only at order 4, after unit 11 at order 2, so the row stays measured. check-unattended.sh sources only lib-unattended.sh (:85), so that row is likely unaffected. The effect is contained: the spawn-budget leg reds and the owner is asked. | sound | - |
| 32 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S2/S4 readers (SPEC_AUDIT_DEFAULT), section 4 Files touched | medium | medium | confirmed | I confirmed it. legacy-homes.txt:111 has `.unattended.conf SPEC_AUDIT_DEFAULT owner-policy`. unattended/kit.toml:172-173's required lists do not name it, so it is not held and S2 moves it. help/spec-audit.md:19 says '`.unattended.conf` on the default branch declares a dated `SPEC_AUDIT_DEFAULT`'. tools/hooks/README.md:159 and agent-cap.js :44, :1426, :1478 (the renderDeny text 'the project's .unattended.conf declares `SPEC_AUDIT_DEFAULT=...`') and :1590/:1595 keep placing the key in the conf. Spec 11 names only agent-cap.js:1466's read. Its generic sentence ('A file naming a home only in prose is re-worded') derives no list, has no AC, and does not reach the deny strings in code. After the fold, users are told to declare the opt-in in a file whose line `readFoldedKey` ignores once the mirror sources the row from the policy file. Behaviour is right and the guidance is wrong, so the effect is contained. | sound | - |
| 33 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 Readers, section 4 Files touched, section 7 | low | low | confirmed | Re-probed: `git grep -n SESSION-KICKOFF -- memory/project/fork-ceilings.txt memory/map/features/session-kickoff.md` prints fork-ceilings.txt:20, whose manifest-check setup is `cp "$ROOT/memory/guides/SESSION-KICKOFF.md" memory/guides/`, and session-kickoff.md:19, :24 and :36 naming the old path. Spec-7's S8 reader list (lines 114-135) and its section 4 manifest readers (`.governance/install.json`, `manifest-check.sh`, `release-0/deploy.toml`) name neither file. The only 'fork' or 'codebase-map' hit in spec-7 is unrelated (:466). Section 7 (:390) lists neither `spawn budget (forks per hot entrypoint)` nor `codebase-map coverage + freshness`, and both legs exist in tools/gate-legs.json. The consequence is contained: AC10's grep `guides/(BUILD-METHOD\|SESSION-KICKOFF)\.md` over `.` minus memory/builds surfaces both stale paths, so the omission is in planning and budget, not a shipped wrong result. | sound | - |
| 34 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 (the fifth shape, the presence readers) with S3 (--root) | high | high | confirmed | Unit 11 S3 (:164-166) reads `--root <dir>` as `git -C <dir>`, which resolves the toplevel from any subdirectory. S4 (:240-248) prescribes the presence shape 'adopted when legacy <home> prints a folded key, or the home exists' and names `tools/memory-tree/row_grammar.py:133` as a reader to re-point. It gives no rule for a reader that walks ancestors. Re-read row_grammar.py:129-138: `resolve_root` starts at the kit dir and tests `.memory-tree.conf` at each level before the `.git` stop. map_lib.py:84 `resolve_root` walks the same way and deliberately avoids `--show-toplevel`. procmon-hook.js:47-58 walks up from the cwd. If the shape is applied per iteration with `--root here`, it is true at the first directory (the kit dir), because legacy reads the toplevel's policy file, so the walk returns a root one or more levels too deep. map_lib and adopt-codebase-map are left to 'DERIVED by S5's presence red', which only checks that a presence test has the shape, not where it is applied. procmon-hook is partly covered, since S4 says its walk finds the root 'by the policy file'. The finding holds for the walk-up readers the spec names or derives. | unsound | - |
| 35 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S1 and S2 (the home mode's write, at an adopter) | high | high | confirmed | `grep -n -i 'mirror\|guard\|terminal\|policy.json'` over unit 20 (blob 0e69ef81) finds only `render_mirror` reads (:51, :53-54, :90) and the conf/HEAD difference guard (:73-76). S1 writes the policy file and removes the home lines in one staged change, and `update` never commits (:76). Nothing regenerates `.governance/policy.json` or names the policy guard's commit route. Unit 11's Migration (:413-420) and S2 (:88-91) require for gov that a node-hook key leave its home only together with `mirror --write`, because scratch-guard reads blank MEMORY_ROOT/ROUTED_PATHS as UNARMED. Adopters do carry a mirror: upgrade_walk.py:264 reports the release-0 adopter re-run committing `.governance/policy.json`. guard.py:5-12 refuses an agent's commit of the policy file. Once the adopter commits update's output, the mirror at HEAD is stale against policy_blob. readFoldedKey then falls back to the home line, which is gone, and the routed-write gate reads blank keys. Unit 20 prices neither path. | sound | - |
| 36 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-41.md:section 2 S1 (the held_halves.py bullet) | medium | medium | confirmed | Unit 41 S1 (:82-84) re-points held_halves to `policy.py get` with no `--rev`. policy.py:732 shows `read_revision` takes `derive_landed_revision` when rev is None. :472-499 shows it reading refs/remotes/<remote>/<branch> and raising Refusal when the ladder names no branch and main names no commit. Unit 11 S3 (:156-158) rules out the landed revision so that an unlanded fold reads its own values. So on the run branch after S2's N+1, `get` reads origin/main's policy file, which does not set the key yet, and returns the catalogue default. Unit 11 S1 (:46-48) makes that default 'its reader's default'. held_halves.py:234-236 has none: it refuses a blank count. So the row's default is unspecified. The spec also does not say how a non-zero `get` exit maps in held_halves. The effect is contained to the parity count on unlanded or unusual clones. | sound | - |
| 37 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md:section 2 S1 (write_moves' idempotence) and S4 (row then change record); likewise unit 40 S2 | medium | medium | confirmed | Unit 13 S1 (:45-53) skips `write(move)` whenever `written(move)` holds, and `written` is S5's predicate: an active unit whose help equals the text. It reads only the row. S4 (:75-77) appends the row, then writes the change record through a separate `build_records.py new change` process. A run that dies between the two re-runs as 'skipped … already at', and no record is written. S6's `feature-interrupted` (:92-93) raises only after 'the first row and record are written', so this case is not planted. Unit 40 S2 has the same hole: an amend is skipped when the row carries the help and edge. The effect is contained: unit 13's migration AC requires as many change records as feature rows at the tip (:236, :291), which catches it at gov's pass. | unsound | - |
| 38 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-04-spec-PLAY-dConvergedCharter-40.md:section 2 S1 (the two refusals) and section 6 | medium | medium | confirmed | Unit 40 S1 says apply 'reads the manifest of the entry's kit through read_units' and refuses 'a row whose help is already non-empty and differs from the entry's'. It never says whether that is the on-disk manifest or the would-be tree after earlier entries. No sentence in the spec addresses two entries sharing a target (grep for 'same target\|two entries\|one target\|duplicate' finds nothing). S3's four plants each hold one entry per target. Unit 7 S7 (:88-93) produces one move per `##` section and amends the existing unit when a section's directive is already a unit, so two sections of one guide mapping to one tag is reachable. Read against the on-disk row, both entries pass and the second overwrites the first's help within one pass, with two edit records. The effect is limited to rationale text in one kit row. | sound | - |
