**Serves:** diff-review DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21

# aRepatriatedFork: Tier-2 closing diff review, round 1

*Node `a`, 2026-09-24. This reviews the whole build: 22 units that make gov's kits run verbatim at
two adopters (inCMS, NicoCares) instead of being forked on each pull. The finders were primed with the
build's seven-point security model and the 35-class checklist from
`python tools/memory-tree/gotchas.py --for-diff f8fdd873..HEAD`. Every confirmed finding survived an
adversarial skeptic. The synthesis pass re-opened the two HIGH-and-above clusters in this worktree
(`.githooks/pre-push:432-558`, `tools/push-main.sh:136-150`) before grading them.*

**Range reviewed: `f8fdd873161801c83a5398afaceaaa7c3205ed28...e69bf51418324bf716d4d8a51de65b8caaf4c6a3`**
(branch `branch/arepatriated-fork-build-e42158`).

**Round: 1.**

## Verdict: BLOCKED

The build's first security-model invariant does not hold at HEAD, and it fails in two independent
ways. First, a value set only in the environment, `GOV_GATE_CMD='bash gatepayload <tracked>.sh'`,
passes the pre-push vetting as `bar=tracked` and then runs an unvetted program over a RED bar. That is
the `gatepayload <tracked>` evasion TOOL-aRepatriatedFork-5 claims to have closed, moved one word to
the right. Second, the hook and the lander answer "was the bar a stub?" from different inputs, so a
`.githooks/gate-env.sh` that sets the test escape gets a stub-gated push that still writes the lander
marker. The tally is 1 BLOCKER, 1 HIGH, 5 MEDIUM and 4 LOW items, which cover 2, 3, 8 and 4 raw
confirmed findings.

## Review shape and run integrity

- **Raw findings:** 32. Confirmed 17, refuted 15, unverified 0. **Precision 0.53** (17/32).
- **Adjudicated by item:** 11 items. BLOCKER 1, HIGH 1, MEDIUM 5, LOW 4.
- **Adjudicated by raw confirmed finding:** 17. BLOCKER 2 (ids 1, 26), HIGH 3 (ids 8, 15, 27),
  MEDIUM 8 (ids 3, 9, 5, 17, 30, 4, 10, 16), LOW 4 (ids 6, 28, 12, 22).
- **Run integrity:** lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
  contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there
  were 0 duplicates at the verdict stage. So the finder set is complete for this shape. The
  finder-level duplicates listed below were merged at synthesis.
- **Duplicates merged at synthesis:** four clusters were found independently by more than one lens:
  {1, 26}, {8, 15, 27}, {3, 9} and {5, 17, 30}. When separate lenses reach the same defect, that
  raises confidence. It is also why 17 confirmed findings become 11 items.

## BLOCKER

### B1. An interpreter's bare-word operand is never vetted: `bash gatepayload <tracked>` lands a RED bar (ids 1, 26)

- **Where:** `.githooks/pre-push:491` (the word loop) and `.githooks/pre-push:520` (the first-word
  arm), inside `check_bar_command`. The same function also vets `GOV_BRANCH_GATE_CMD` at `:570`.
- **Defect:** the loop grades only words shaped like `*/*` or `*.sh`, and options (`-*`) only before
  the first path-shaped word. The first-word arm accepts `bash`/`sh`. A bare word such as
  `gatepayload` or `x.pyc` sitting between the interpreter and the tracked script matches none of
  these arms. bash runs its first non-option operand as the script, looking in the cwd and then on
  PATH, and the tracked name becomes `$1`.
- **Reproduced by two lenses:** `check_bar_command K 'bash gatepayload tools/run-gates/run-gates.sh'
  <HEAD>` returns rc 0 with `bar_class=tracked`. With `gatepayload` on PATH it printed `PAYLOAD RAN`
  at rc 0 over a bar stubbed RED, with the tree clean. A root-level `x.pyc` is gitignored
  (`.gitignore:2`), so the working-copy arm never sees it either.
- **Impact:** the push lands with run log `bar=tracked` and push-main writes the lander marker, which
  `unattended.sh --landed` accepts. This is the a7c78ad2 class (`GOV_GATE_CMD=true`) that TOOL-5
  exists to close, and it needs only the environment knob. There is a secondary gap too: vetting runs
  under `set -f`, but execution at `:577` (and at the default-branch run site) does not, so a glob
  word can expand after it was vetted.
- **Fix:** when `_bar_first` is `bash` or `sh`, the SECOND word must be path-shaped, tracked at `$at`
  and clean. Refuse any other word between the interpreter and the script. Stated as one rule: the
  program that executes is a tracked, clean path at word 1, or at word 2 after an interpreter. Run
  `$gate` and `$GOV_BRANCH_GATE_CMD` with globbing off as well.
- **Left-shift:** add `bash gatepayload <tracked>` and `sh x.pyc <tracked>` as evasion rows in
  `.githooks/pre_push_bar_selftest.py`. Each row stages a PATH-resident payload and asserts that the
  push is REFUSED. The selftest already disables arms in a copy and watches evasions land, so this row
  also proves the new arm can go RED (§7: a gate is not landed until its failing case is observed).
  The class is "an arm enumerates dangerous word shapes instead of pinning the executed word's
  position". The durable guard is a positional rule, not another shape pattern.

## HIGH

### H1. Hook and lander decide "stub" from different inputs; gate-env.sh can set the escape (ids 8, 15, 27)

- **Where:** `.githooks/pre-push:432-434` sources `.githooks/gate-env.sh` without vetting it.
  `check_bar_command` then honours `GOV_GATE_CMD_TEST` at `:464`. `tools/push-main.sh:143` withholds
  the lander marker only when `GOV_GATE_CMD_TEST` is set in ITS OWN environment.
- **Defect:** this is two readers of one decision, i.e. two-guards-one-question-two-answers.
  Suppose gate-env.sh sets `GOV_GATE_CMD_TEST=1` and `GOV_GATE_CMD=true`. The file can be committed,
  or it can be untracked and excluded through `.git/info/exclude`, which `git status --porcelain`
  does not report. Then the hook runs `true` as `bar=stub` and exits 0, and push-main never sees the
  variable, so it writes `LANDER_MARKER`.
- **Impact:** this falsifies security-model item (1), "the lander writes no marker under the escape",
  and TOOL-5 S4's claim that a stub-gated push can never become a LANDED. The run log does say
  `bar=stub`, but nothing that decides a landing reads it. The skeptic's caveat stands and widens the
  finding: an unvetted sourced file can also just `exit 0`. So the underlying defect is that
  gate-env.sh is sourced without vetting and is missing from the unattended protocol's list of open
  classes. Moving the variable read above the `.` line alone does not close it.
- **Fix:** give the hook's verdict ONE channel. At the start of each run the hook clears a git-dir
  file next to `pre-push-refusal`, then writes the bar class it actually vetted
  (`default`/`tracked`/`stub`) plus the vetted script path and blob id. push-main writes the marker
  only when that file reads `default` or `tracked`, and stops re-deriving the class from its own
  environment. Separately, either vet gate-env.sh (tracked at the pushed sha and clean, with an
  ignored copy refused), or name it in `memory/guides/UNATTENDED-PROTOCOL.md` as an open class that
  shell access can defeat.
- **Left-shift:** add a `pre-push.test.sh` arm in which gate-env.sh sets the escape and a bar that
  goes RED, driven through push-main, and assert that the marker is ABSENT. Add a second arm with the
  file excluded through `.git/info/exclude`. The general class, "a decision re-derived by a second
  process from a different input", should become a gotcha entry, because `--for-diff` did not flag it
  here.

## MEDIUM

### M1. Any tracked, clean script passes as the merge bar, and nothing records which one ran (ids 3, 9)

- **Where:** `.githooks/pre-push:558` (`bar_class=tracked`, reached after only three checks).
- **Defect:** `GOV_GATE_CMD='bash tools/lib/kit-rel.sh'` and `'bash tools/lib/resolve-python.sh'`
  both pass. Each script only defines a function and exits 0; both lenses measured rc 0. The hook
  header says the tracked-file property "separates a reviewed bar script from `true`", but any cheap
  tracked script is `true` with extra steps, and setting it needs only the environment knob.
- **Impact:** the run log records only the class, and the lander marker records nothing about the
  bar. So the evidence an unattended run is judged on still cannot tell the whole bar from a no-op.
  That is the a7c78ad2 gap, one step removed. It ranks below B1 because the script that runs is at
  least reviewed code.
- **Fix:** accept `GOV_GATE_CMD` only when it equals the default runner or a value DECLARED in a
  tracked file read at the pushed sha (`.unattended.conf` `GATE_CMD`, or
  `git show $at:.githooks/gate-env.sh`). Write the vetted path and blob id into the run-log END line
  and the lander marker, so `--landed` can compare them (this pairs with H1's channel).
- **Left-shift:** a selftest row with `GOV_GATE_CMD='bash tools/lib/kit-rel.sh'` that asserts a
  refusal. Also an `unattended.test.sh` arm in which `--landed` refuses a marker whose recorded bar is
  not the declared one.

### M2. `--accept-role-moves` into `rendered` skips the reconcile and the re-render destroys the edit (ids 5, 17, 30; residual d)

- **Where:** `tools/govkit/govkit.py:7851`, the `write and accept_role_moves` branch.
- **Defect:** for every target role the branch sets `row["role"] = now` and then `continue`s. That
  includes `rendered`, which maps through `UPDATE_ROLE` to `adopter`, the one
  `KIT_WRITING_DISPOSITIONS` member. The DEPL-cMendedVintage-27 fall-through directly above it exists
  to reconcile the operator's copy or refuse, and it never runs for this row. Later in the same run,
  the kit's `[[regenerate]]` argv (the re-render block, around `:9259`-`:9323`) rewrites the
  destination whenever that kit is in `touched_kits`. That is likely, because gov moved the kit's
  descriptor in this pull. Id 30 described the `_rg_set` mechanism imprecisely, since that set is only
  the rollback snapshot. The outcome still holds.
- **Impact:** an operator's local edit is overwritten with no conflict, no refusal and no line naming
  it. The branch comment's "NO BYTE MOVES in this run" is false for this role. Residual (d) is
  CONFIRMED: the only fixture (`selftest.py:1317`, AC10) covers moves into `seed` and `engine`.
- **Fix:** take the accept branch only for `UPDATE_ROLE.get(now) not in KIT_WRITING_DISPOSITIONS`.
  A move into `rendered` then falls through to the existing reconcile/refuse path under the recorded
  role, or is refused with a named remedy.
- **Left-shift:** add a selftest arm for an operator-edited engine row whose descriptor role moves to
  `rendered`, run under `update --write --accept-role-moves`. It asserts that the bytes are unchanged
  or that the run refuses, and it must be observed RED against HEAD first. The class is
  amendment-leaves-its-other-half-standing: a flag branch added above a protective fall-through.

### M3. `[[own]]` path is graded but never canonicalised, so `./x` escapes the owned-file skip (id 4)

- **Where:** `tools/govkit/govkit.py:1047` (`resolve_owned_rows`). The exact-equality matches are at
  `:5941` (`owned_dests`) and at the apply write loop around `:6209`, and adopt's around `:10604`.
- **Defect:** `demand_safe_token` admits `.` and `/`. `demand_contained_dest` normalises only for its
  containment test and returns the raw string, and `(target/path).is_file()` is satisfied by a
  `./x` spelling. So `./tools/memory-tree/x.py`, `tools//memory-tree/x.py` and
  `tools/memory-tree/./x.py` all pass, while `p in o["dests"]` is false.
- **Impact:** apply finds no owned entry and writes gov's bytes over the file the target declared it
  owns, with no conflict check. That is exactly the DEPL-21 property. adopt records the file as an
  ordinary engine row, so later updates overwrite it too. A case variant on Windows has the same
  effect. The trigger is an operator's non-canonical spelling, but the result is a silent overwrite.
- **Fix:** after grading, refuse any `own.path` that is not already equal to
  `posixpath.normpath(path)`. Refusing beats silently re-keying, because it tells the operator their
  spelling was wrong.
- **Left-shift:** an apply selftest arm with a `./`-prefixed `own.path` that asserts a refusal, or
  asserts `SKIPPED [adopter-owned]` with the bytes unchanged. The class is join-key compared raw on
  one side and canonical on the other; the gotcha corpus's containment-tested-one-way is the nearest
  existing entry and should gain this variant.

### M4. `update` ignores `[[own]]` and writes into a declared-owned file until `adopt` re-runs (id 10)

- **Where:** `tools/govkit/govkit.py:7333` onward (`_cmd_update`). It dispatches only on the receipt
  row's role through `UPDATE_ROLE` (around `:7794`-`:7805`). `resolve_owned_rows` has exactly two
  callers, apply and adopt.
- **Defect:** apply reads `deploy.toml` and refuses to write an owned file, while update and check
  read only the receipt. adopt's own remedy text tells an operator to "declare it adopter-owned with
  an [[own]] row". An operator who does exactly that and then runs `update --write` still has an
  `engine` receipt row, and gov's bytes are three-way merged into the program the target declared as
  its own. `check` says nothing.
- **Impact:** two readers of one declaration give two answers
  (two-readers-of-one-config-one-re-derived), and the one that writes is the one that is wrong.
- **Fix:** call `resolve_owned_rows` in `_cmd_update` and `cmd_check` before dispatch. For an
  `engine` receipt row whose path is a declared owned destination, refuse the write and name
  `adopt --re-adopt` as the remedy. Alternatively treat it as `contract`.
- **Left-shift:** a selftest arm that adds an `[[own]]` row after adopt, runs `update --write`, and
  asserts the owned bytes are unchanged and that a named refusal appears. A structural guard is also
  worth having: a static assertion that every command that writes target bytes reaches
  `resolve_owned_rows` (one grep-based arm over govkit's `cmd_*` writers).

### M5. A check-unattended self-test arm asserts a literal that the resolver no longer prints (id 16)

- **Where:** `tools/unattended/check-unattended.test.sh:2298`. The producer is
  `tools/unattended/check-unattended.sh:2615`, which now interpolates `$(derive_index_repair)` from
  `lib-unattended.sh:126`.
- **Defect:** the fixture copies only the unattended kit into `$TMP` (around `:150`-`:165`). It has
  no memory-tree dir and no `.governance/install.json`, so `derive_index_repair` prints its refusal
  text instead of `repair with the --write mode of tools/memory-tree/gen_build_index.py`. Reproduced
  from a scratch repo holding only `tools/unattended/`. `unattended.test.sh:700` passes only because
  it runs the real kit in place.
- **Impact:** that suite is red at HEAD. The unattended `*.test.sh` legs are off the bar (owner
  ruling, 2026-08-23), so no bar leg shows it. But this is kit work, and its DoD owes
  `bash tools/unattended/run-unattended-gates.sh --serial`. A pass that reported the suite green did
  not run it against this commit.
- **Fix:** copy `gen_build_index.py` to `$TMP/$(dirname $KIT_REL)/memory-tree/` in the fixture setup
  and assert against the resolved path, or assert the refusal text the fixture actually produces. In
  both cases keep the whole-literal signature.
- **Left-shift:** this is fixture-removes-the-path-under-test. The existing kit-dogfood parity leg is
  the natural home for the check that every literal an arm expects from a `derive_*` helper is
  produced under that arm's fixture. Short of that, the close's DoD must run the kit suite; the
  owner's "on demand only" ruling makes that a documented check, not a gate.

## LOW

### L1. `--close --override` and `--abort` reasons reach `park()` unguarded, so they can forge a fact line (id 6; residual c)

- **Where:** `tools/unattended/unattended.sh:3733` (the override park) and `:2833` (the abort park),
  both into `park()` around `:4666`. The reader is `fact()` at `:738`.
- **Defect:** `set_fact` refuses LF and CR (TOOL-6), and so do the `--review`, `--park`, `--propose`,
  `--brief`, `--rescope` and waiver paths. These two do not. So `--reason $'why\n<key>: <value>'`
  writes a well-formed fact line under `## Parked`. `fact()` returns the first match across the
  WHOLE file, so a key not yet present in Run facts is read from the forged line, and check 34 never
  looks there. The TOOL-6 comment claims the guard now matches "every sibling writer", which is false
  for these two.
- **Residual (c) CONFIRMED:** `record-piece` and `record-set` write a records file, not RUN.md, so
  the S4 matrix's "phase unchanged" assertion cannot fail for them. They pass by finding nothing.
- **Impact:** low, because the actor is the run itself. It is still a real sibling-guard gap under
  §9's composite-write-guard rule.
- **Fix:** apply the same `wc -l`/CR refusal to `OV_REASONS` in `verb_close`'s validation loop and to
  the abort reason. For the two record verbs, assert against the records file they actually write.
- **Left-shift:** add both verbs to `run_hostile_verb`. Better still, make one arm enumerate every
  verb that takes free text from the driver's usage table, so a new verb cannot be left out of the
  matrix (the class is vacuous-selector-empty-population).

### L2. Check 34 scans `## Run facts`, but the readers it protects scan the whole file (id 28)

- **Where:** `tools/unattended/check-unattended.sh:2852` (the section-scoped awk). The readers are
  `fact()` at `unattended.sh:738` and `fact_of`/`phase_of` at `check-unattended.sh:818`.
- **Defect:** a `phase: LANDED` line above the heading, in the title or the generated region, is read
  by the driver and the leg ahead of the real one, while check 34 reports clean. The header's "a key
  outside the section is not read" is true of the check and false of the readers.
- **Fix:** scope `fact`/`fact_of` to the section. That one change also closes L1's forged-line read,
  which is why this item and L1 should be fixed together.
- **Left-shift:** a check-unattended arm with a duplicate key above the heading that asserts RED, or
  asserts that the reader ignores it.

### L3. manifest-check's resolver is anchored at the script, so the junction copy grades gov's tree (id 12)

- **Where:** `skills/session-kickoff/manifest-check.sh:417` (`resolve_id_reader`), and
  `resolve_kit_dir` at `:362`.
- **Defect:** commit 3e939527 replaced the `$ROOT/tools/memory-tree` and `$ROOT/memory-tree` probes
  with `resolve_kit_dir` anchored at `MC_DIR`. From the per-machine junction copy, which SKILL.md
  uses as the last fallback, `here.resolve()` follows the junction into gov's checkout. The receipt
  rung then reads gov's receipt, and the flat `$ROOT/memory-tree` layout is no longer probed.
- **Impact:** a narrow regression. In a repo with no in-repo copy and a flat or receipt-relocated
  memory-tree, id citations are now silently skipped on the NOTE path. In-repo copies are unaffected.
- **Fix:** try `resolve_kit_dir "$py" memory-tree corpus_ids.py "$ROOT"` after `MC_DIR`, and keep the
  flat `$ROOT/memory-tree` probe as a final fallback.
- **Left-shift:** a manifest-check test arm that runs the script from OUTSIDE the fixture repo, as the
  junction does, against a flat-layout fixture, and asserts that id citations are graded.

### L4. Two copies of the receipt-prefix read, neither honouring per-entry prefixes (id 22; residual a)

- **Where:** `tools/memory-tree/adopt-memory-tree.sh:45` and `kit-dogfood-parity.test.sh:58`.
- **Residual (a) CONFIRMED.** Each file carries a grep/sed read of the first top-level `"prefix"`,
  and nothing checks that the two agree. Both also ignore the `kit.<entry>.prefix`/`kit.<entry>.kit`
  overrides that govkit's `resolve_context` (around `govkit.py:1012`) honours and records only per
  row.
- **Impact:** an adopter who re-homes one sibling kit gets `{{TOOL_ROOT}}` sibling paths rendered at
  the global prefix. The two copies do not diverge today, because the parity test exits 2 unless the
  kit is inside the repo, which is equivalent to `KIT_INSIDE`.
- **Fix:** resolve the sibling through the inline `resolve_kit_dir`, which reads receipt rows in
  Python, in both files.
- **Left-shift:** if the copies stay, add both blocks to the `resolve-python.test.sh` byte-parity
  table.

## Residuals the unit passes reported

- **(a) receipt-prefix copies (TOOL-10):** CONFIRMED, LOW. This is L4.
- **(b) `.agent-cap.conf` re-parsed in shell (TOOL-7):** confirmed on read by the synthesis pass. It
  is not a skeptic-verified finding, so it is ungraded in `items`; my reading puts it at LOW. The
  shell reads do not share the hook's grammar. `check-verifier-fanout.sh:117` uses a sed that matches
  only well-formed lines, so `FANOUT_CAP=4` followed by `FANOUT_CAP=abc` yields `4` (measured), while
  the hook's `loadDeclaredCap` takes the last raw line and denies every call.
  `check-protocol-parity.test.sh:104` does match the hook on that input. The impact is small, because
  the fanout value is display-only and the hook has already redded the scripts. It is still the
  two-answers-to-one-question class. The fix is to have both scripts ask the hook for the effective
  cap (for example a `node agent-cap.js --print-cap` mode) instead of parsing the conf.
- **(c) TOOL-6 S4 matrix vacuous for record-piece/record-set:** CONFIRMED, part of L1.
- **(d) DEPL-17 `--accept-role-moves` into `rendered` has no fixture:** CONFIRMED, and it is worse
  than a missing fixture, because it loses data. This is M2.
- **(e) DEPL-21 fallback receipt row repeats adopt's keys:** confirmed on read by the synthesis pass,
  ungraded in `items`, LOW. The row literal at `govkit.py:6216`-`6219` restates the shape adopt builds
  at around `:10663`. A key added to one is silently missing from the other. The fix is one shared row
  builder that both call.
- **(f) DEPL-13 contract probes time out at inCMS (~4 minutes for `govkit check`):** NOT adjudicated.
  No lens reached it and it cannot be reproduced from this tree, because it needs the inCMS checkout.
  It remains OUTSTANDING. Under §7's rule that cost is a verdict, it needs a declared ceiling on
  `govkit check`, measured at inCMS.

## Checklist classes this range hit

These classes from the selected checklist produced confirmed findings:
two-guards-one-question-two-answers (H1, L2), two-readers-of-one-config-one-re-derived (M4,
residual b), amendment-leaves-its-other-half-standing (M2), fixture-removes-the-path-under-test (M5),
fixture-passes-by-finding-nothing (residual c), allowlist-narrower-than-the-root-it-guards (B1, M1),
join-key-widened-by-a-shared-location (M3) and second-implementation-is-not-a-second-opinion (L4).
H1 in particular is not covered by any existing gotcha entry and should be added as one.
