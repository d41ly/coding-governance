**Serves:** spec-audit TOOL-dDeclaredLoop-93@rev-1 TOOL-dDeclaredLoop-94@rev-1

# Tier-2 spec audit — dDeclaredLoop TOOL-dDeclaredLoop-93 and TOOL-dDeclaredLoop-94 (round-11 audit, run 1)

Provenance: an adversarial Workflow review. Finders were gov-spec-reviewer, skeptic batches were gov-skeptic, and synthesis was gov-synthesizer. The 92 sibling spec documents were supplied as context.

Reviewed: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md@21fcd5a599d9ee4fc29216552e7da6024ea6a0ac, memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md@a1fb6cd2077de0c99582e19f2b4cc0f283fad926

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. One high item has to be fixed before 94 is built: as written, 94 AC1 goes red on a correct build. The tally is 12 items: 1 high, 6 medium and 5 low. Counted as raw confirmed findings, that is 14: 1 high, 7 medium and 6 low.

Review shape: intensity full, raw 17, confirmed 14, refuted 3, unverified 0 (0 uncertain), precision 0.82.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| reuse | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| blast-radius | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| failure-envelope | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |

Run integrity is complete. All 5 lenses returned and none died. All 5 skeptic batches returned and none died. No verdict was demoted as contradictory. No duplicate refutation was demoted as orphaned. No spurious verdict was discarded, and no duplicate was found.

On the 14 confirmed findings, the skeptics judged 11 fixes sound and 3 unsound. None lacked a proposed fix, and none went unjudged. On severity, the skeptics left 0 confirmed findings ungraded and re-graded 3. There were no unverified findings, so none was answered uncertain and none lacked a usable verdict.

No lens notes were supplied, so every lens ran on the kit's generic brief. The checklist held 15 items, 3 for each of the 5 lenses. No by-design block was supplied. No checked subject moved.

Item merges:
- Ids 4 and 12 describe one defect, 93 AC3's self-counting floor, and are one item.
- Ids 5 and 15 describe one defect, the skew row's in-process module cache, and are one item.
- Id 7 (low) overlaps id 9 (medium) on 90's sketch and 88 S33. The findings carry different binding grades, so they stay as separate items. Applying id 9's fix discharges id 7.

## HIGH

### H1 — 94 AC1's tree_lib route probe goes red on the tree the earlier units leave (id 1)

- **Where:** 94 §4 "The tree_lib route, after this unit" and "The tree_lib route probe"; §2 S7 and S22; §6 AC1.
- **What is wrong:** `resolve_memory_root` in `tools/loop/loop_lib.py` reads the memory-tree kit's `parse_conf` through `resolve_kit_dir("memory-tree", "tree_lib.py", here)`. Three earlier units require that route: 41 S1 (order 6), 72 S1 (order 36) and 79 S25/AC25 (order 40). All of them build before 94 (order 48). 94's probe counts any `resolve_kit_dir("memory-tree", ...)` outside `load_tree_lib` as a HIT. If the call is routed through the loader instead, `parse_conf` becomes a member outside the three-name `TREE_LIB_SYMBOLS`, which is also a HIT.
- **Consequence:** AC1 is red on a correct build of the whole set. The builder is left with two moves the spec never authorises: grow `TREE_LIB_SYMBOLS` past §5's "at most three", or re-route `resolve_memory_root`. A builder who narrows the probe to get green leaves this class of hit unguarded.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**
  - Keep `resolve_memory_root`'s own route to `parse_conf`, and add a non-goal saying so in 94 §3.
  - In §4's probe and in AC1, add one stated exception: inside `loop_lib.resolve_memory_root`, one `resolve_kit_dir("memory-tree", "tree_lib.py", here)` whose result is read only for `parse_conf`. AC1 also checks that this exception site exists, so the exception never covers anything else.
  - Alternatively, route the call through `load_tree_lib(need=("parse_conf",))`, add `parse_conf` to `TREE_LIB_SYMBOLS` and update the §5 count. Then catch the loader's no-kit refusal inside `resolve_memory_root` as "no memory-tree conf", so 41 S2's no-kit path still prints the foreign-build line. Add consumes-from edges to 41, 72 and 79.
  - Either way, the build runs the probe over the tree as built through order 47 and observes it green.
- **Left-shift gate:** before a spec is promoted, run each new AST/grep probe in its ACs over the tree its predecessors leave at its build order, and require it to be green.

## MEDIUM

### M1 — 94 orders restatements in 92's text that no criterion observes (id 2)

- **Where:** 94 §2 S4, S5, S6, S7, S8, S9 (AC16 half), S10 (92 half), S20, S22 and S23, against §6.
- **What is wrong:** These items order sentences in 92 (AC8, AC16, S3, S8, §5 and S17). AC1 to AC18 grep only a few of them: AC1 for `spec_from_file_location` and AC5 for `S35`. Nothing greps 92 AC16 for S9's range greps, 92 AC8 for the staged breaks or the getattr population, 92 S8 or §5 for `need` or first use, 92 S3/S8 for the sketch sites, or 92 S17 for the first-non-blank rule or the 85 S3 sites. Each of these counts is 0 at HEAD.
- **Consequence:** A pass that writes only the code halves meets every criterion and leaves 92 still wrong. That includes id 4's defect, since 92 AC16 would still lack its range greps.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Add one range grep per restated sentence, each pinned at 0 at HEAD:
  - over the 92 AC8 range: `derive_X`, `import_module`, `getattr` and `non-empty` (`non-empty` replaces `GIT_ENV_LEAKS`);
  - over the 92 AC16 range: `S24` and `S21`;
  - over the 92 S8 range: `need` and `first use`;
  - over both the 92 S3 and the 92 S8 ranges: `conf-constant class` (this replaces `89` over the S8 range);
  - over the 92 S17 range: `first non-blank` and `85 S3`.
- **Left-shift gate:** a spec-lint check that every scope item ordering a "92 Sx states/says" restatement has at least one AC grep over that range.

### M2 — 93 AC3's exit-claim floor is met by 93's own sentences, and its matcher accepts one phrasing only (ids 4, 12)

- **Where:** 93 §6 AC3 and §4 "The exit-claim probe".
- **What is wrong:** The probe runs over the whole spec folder. At HEAD it finds 9 claims, and 4 of them are in 93 itself. So the "at least five claims" floor is met by 93 plus one sibling claim. The floor proves nothing about the 81, 83 and 88 claims the unit says agree. The matcher also accepts only `\bexits (\d+)` within 60 characters of the backticked command. 93's own §1 phrases the defect as "an exit code of 0", which the matcher would miss.
- **Consequence:** Suppose 81, 83 or 88 is reworded out of the regex, or 94 S19/S20 rewrites 92 AC16 as "exit code 0", "exits with 0" or "returns 0". AC3 and 94 AC10 still print `{1}` and pass. 94 AC10 does not re-run 93 AC1. So the conflict 93 exists to remove can come back while every check stays green.
- **Fix:** The skeptic judged id 4's proposal UNSOUND and id 12's SOUND. The combined fix:
  - Exclude 93's own file from the population.
  - Require at least one claim from each of the 81, 83, 88 and 92 files. Pin no exact per-file count: 94 S14 rewrites 92 S17, so an exact `92:1` pin could go red on a correct build.
  - Widen the matcher to `exit(s| code)?( of| with)? <n>` and to `non-zero`. No current sibling hits the widened forms, so this would not go falsely red today.
  - Have 94 AC10 also re-run 93 AC1's AC16-range grep.
  - Stage a break that rewords 92 AC16 to "exit code of 0" in a scratch copy and show AC3 going red. Restoring "exits 0" is not enough on its own.
- **Left-shift gate:** add "a guard whose population includes its own spec" to the project's bug-class checklist, next to fixture-passes-by-finding-nothing. A probe's floor must be met by files other than the spec that states the probe.

### M3 — 94 leaves 90's loader sketch and the 90/86/88 refusal sentences on the old loader (id 9)

- **Where:** 94 §2 S10, S21 and S22; §6 AC6.
- **What is wrong:** S21 makes the loader catch any Exception and refuse once, naming every missing name. S22 gives each caller its own `need`. But S10 rewrites only the tuple line of 90's sketch, so the rest of that sketch keeps the old loader:
  - `load_tree_lib():` with no `need`;
  - the per-name `for name in TREE_LIB_SYMBOLS: refuse` loop;
  - a catch of only `ImportError | SyntaxError`;
  - the comment "every tree_lib name loop_lib calls", which is false once `GIT_ENV_LEAKS` joins the tuple.

  The same stale wording stands in three sentences. 90 S4 says the loader refuses when any name in `TREE_LIB_SYMBOLS` is absent. 90 S6 has 86 S21 and 88 S33 state the refusal over `TREE_LIB_SYMBOLS`. 88 S33 names only ImportError or SyntaxError.
- **Consequence:** The sibling text and S22 give opposite answers to one question: does `need=("GIT_ENV_LEAKS",)` refuse when a derive_* name is missing? AC4's second half requires that it does not. The next change may read the wrong answer. AC6 stays green, because it greps only `GIT_ENV_LEAKS` in 90's sketch.
- **Fix (the skeptic judged it SOUND):**
  - Widen S10 to rewrite 90's whole loader block to 94's form: the `need` parameter, one refusal naming every missing name, and any Exception caught. Drop the "every tree_lib name loop_lib calls" comment.
  - Add 90 S4, 86 S21 and 88 S33 as restatement sites that state the refusal over the caller's `need`. For 88 S33, that covers both its refusal-as-a-class sentence and its "ImportError or SyntaxError" clause.
  - Extend AC6 with greps over 90's sketch range: `need` at least 1, and `for name in TREE_LIB_SYMBOLS` and `ImportError | SyntaxError` at 0 each.
- **Left-shift gate:** a checklist entry for amendment-leaves-its-other-half-standing. When a unit changes a contract, grep every sibling sketch and S-item that states the contract, and give each hit a restatement item or a non-goal.

### M4 — 92's sketch keeps the bare, import-time loader calls that 94 S8 and S22 remove (id 10)

- **Where:** 94 §2 S8, S21 and S22; §6 AC2.
- **What is wrong:** 92's sketch "The tree_lib route, after this unit" still shows three loader calls:
  - `derive_conf_reads(...): tl = load_tree_lib()`;
  - `derive_conf_constants(...): tl = load_tree_lib()`;
  - a module-level `GIT_ENV_LEAKS = loop_lib.load_tree_lib().GIT_ENV_LEAKS` in loop_witness.py.

  S8 and S22 rewrite only 92 S8 and §5. S21 rewrites only the loader body. S3 adds only budget.py, and AC2 greps only `budget.py`.
- **Consequence:** One build carries two designs for the same callers. The next change that reads 92's sketch rebuilds the module-level call that S8 removes.
- **Fix (the skeptic judged it SOUND):**
  - Add to S8 and S22 that 92's sketch caller lines read `tl = load_tree_lib(need=<the names it reads>)` for `derive_conf_reads` and `derive_conf_constants`.
  - Have the loop_witness.py line move inside its reading function, with `need=("GIT_ENV_LEAKS",)`.
  - Add to AC2 a grep over `awk '/^### The tree_lib route/,/^### The OSError/'` of the 92 spec: `need=` at least 1, and `GIT_ENV_LEAKS = loop_lib.load_tree_lib()` at 0.
- **Left-shift gate:** the same checklist entry as M3. Sibling sketches are restatement sites too.

### M5 — Loader results can escape 94's probe by routes other than a call argument (id 13)

- **Where:** 94 §2 S5; §4 "The tree_lib route probe"; §6 AC3.
- **What is wrong:** The probe defines a loader result as a `load_tree_lib(...)` Call, or a Name bound from one in the same body. The only escape it counts as a HIT is a loader result passed as a call argument. Other routes escape unseen:
  - returned from a helper: `def tl(): return loop_lib.load_tree_lib(need=())`, then `tl().derive_X`;
  - stored in an attribute or container: `self.tl = ...` or `CACHE['tl'] = ...`;
  - aliased: `t2 = tl`.
- **Consequence:** A read of a name the loader never checked escapes AC1. On a skewed kit it ends in an AttributeError traceback, contradicting §5's "never a silent pass". AC3 stages only the helper-argument route, so a builder who closes that one route meets every criterion.
- **Fix (the skeptic judged it SOUND):**
  - State the class in S5 and in the probe. A loader result may only be the direct value of an Attribute, of getattr, or of a plain Name bound once in the same body.
  - Count as a HIT any loader result that is returned, yielded, assigned to an attribute, subscript or second Name, or placed in a container.
  - Add to AC3 a staged helper that does `return loop_lib.load_tree_lib(need=())`, read through `.derive_X`, which must report a hit.
- **Left-shift gate:** a checklist entry. An AST escape probe enumerates the value-flow forms (argument, return, yield, attribute or subscript store, alias, container) and stages one break per form.

### M6 — 94's probe ignores a positional or list-literal `need` (id 14)

- **Where:** 94 §2 S22; §4 "The tree_lib route probe", need(call).
- **What is wrong:** The sketch declares `def load_tree_lib(need=TREE_LIB_SYMBOLS)`, so `need` can be passed positionally. The probe defines need(call) only from a keyword `need` literal tuple, falling back to `TREE_LIB_SYMBOLS`. It says nothing of a positional tuple or a list literal.
- **Consequence:** `load_tree_lib(("GIT_ENV_LEAKS",)).derive_docstring_ids` passes the probe, because the read is in the full union. At runtime the loader checks only `GIT_ENV_LEAKS`, so on a kit lacking `derive_docstring_ids` the read ends in a traceback instead of the named refusal. That is the hole S22 says AC1 closes.
- **Fix (the skeptic judged it SOUND):**
  - Make `need` keyword-only (`def load_tree_lib(*, need=TREE_LIB_SYMBOLS)`), or treat any positional argument as `need`.
  - State that a non-tuple literal is a HIT.
  - Add to AC3 a staged positional-need read of an unchecked name.
- **Left-shift gate:** when a probe reads a call's argument, the spec states every way the argument can be passed (keyword, positional, non-literal, other literal type), and a staged break covers each.

## LOW

### L1 — The 93/94 edge cites different id sets on its two sides (id 3)

- **Where:** 94 §3 Edges, the consumes-from TOOL-dDeclaredLoop-93 bullet (94.md:151), against 93's hands-off 94 bullet (93.md:58).
- **What is wrong:** 93's bullet cites the round-10 ids 4, 11, 13, 20 and 29. 94's mirroring bullet cites id 11 alone. This is the two-answers-to-one-question class.
- **Consequence:** A reader or edge-mirror check gets two answers about what crosses the edge. Ids 13 and 29 are exactly what 93 §3 hands to 94. Only the record's text is affected.
- **Fix (the skeptic judged it SOUND):** Make both bullets cite one id set, whichever matches what crosses the edge. Either 94's bullet cites 4, 11, 13, 20 and 29, or 93's bullet cites 11 alone.
- **Left-shift gate:** extend the edge-mirror check so it compares the cited audit-id sets on the two sides of an edge, not only the edge's presence.

### L2 — The skew row's scratch-copy check is unspecified against the loader's module cache (ids 5, 15)

- **Where:** 94 §2 S2, S21 and S24; §4 "The tree_lib route, after this unit" (budget.py skew row).
- **What is wrong:** S21 has the loader follow `row_grammar.load_recall_kit`'s idiom: `sys.path.insert(0, kit)`, then a plain `import`. That caches the module in `sys.modules`. The skew row first calls `loop_lib.load_tree_lib(need=()).__file__` in budget.py's own process, then copies the kit to scratch. The spec never says whether the copy is checked in a subprocess. If it is checked in-process, the real `tree_lib` is already cached and stays first on `sys.path`, so the copy's missing `derive_constant_charges` is never seen.
- **Consequence:** An in-process build makes 92 AC7 and 94 AC18 go red, and the spec does not explain why. The trap shows up as a failing check, never a false pass. That is why the skeptic graded both findings low against the finder's medium. A builder who works around it with a by-path load under a fresh name can make the row observe something different from what the real readers do.
- **Fix (the skeptic judged both findings' fixes SOUND):**
  - In S2, S21 and the S24 sketch, state that the skew row checks the copy in a fresh child `python` process with its cwd at the copy's `loop/`.
  - Alternatively, have `load_tree_lib` load by path through `importlib.util.spec_from_file_location`, either under a key that identifies the resolved path (as `check-spec-tokens.py`'s `load_kit_module` does) or under one fixed name, evicting the cached `tree_lib` and its `sys.path` entry when the kit directory differs.
  - Add an AC18 half: after a prior in-process `load_tree_lib()` of the real kit, the row still prints `tree_lib lacking derive_constant_charges`.
- **Left-shift gate:** a checklist entry. A spec that reuses an import idiom across more than one kit directory in one process states its isolation (subprocess or path-keyed cache).

### L3 — 90's sketch and 88 S33 still state the narrower ImportError | SyntaxError, per-name loader (id 7)

- **Where:** 94 §2 S21 and S10; §4 "The tree_lib route, after this unit".
- **What is wrong:** S21 widens the loader to catch any Exception and refuse once, naming every missing symbol. Two statements keep the old wording: 90's sketch line `# ImportError | SyntaxError -> 88 S33's refusal`, with the per-name refuse loop, and 88 S33.
- **Consequence:** The specs describe one loader three ways. Code is unaffected, because the narrower wording is a subset of the wider one. AC6 and AC16 do not notice. This overlaps M3 (id 9), whose fix discharges it.
- **Fix (the skeptic judged it SOUND):**
  - Extend S10, or add an item, to restate 90's sketch catch line and per-name loop to S21's idiom: any Exception refused by class name, one refusal naming every missing symbol, need-scoped.
  - Have 88 S33 name "any exception the import raises".
  - Add to AC6/AC16 a grep over 90's sketch range: `grep -c 'ImportError | SyntaxError'` prints 0.
- **Left-shift gate:** the same checklist entry as M3.

### L4 — The skew row's sketch copies "dirname(...) and its siblings", and §5 omits loop/ from the price (id 16)

- **Where:** 94 §4 sketch (the skew row's "copy dirname(...) and its siblings"); §5 perf / scale.
- **What is wrong:** Read literally, the sketch copies all of `tools/`, about 20 MB. §5 prices about 3.3 MB, which covers memory-tree and lib only and omits `loop/`. 90 S5 names the authoritative set, which S24 does not carry.
- **Consequence:** Close to cosmetic, which is why the skeptic graded it low against the finder's medium. A literal reader copies about 6x the price. A reader who copies only memory-tree leaves the copy unable to resolve `here/../memory-tree`.
- **Fix (the skeptic judged it SOUND):**
  - In S24 and the sketch, name the copied set exactly as 90 S5 does: `tools/loop/`, `tools/lib/` and `tools/memory-tree/` as siblings, with `__pycache__` excluded.
  - Re-price §5 from `du -sk` of those three directories.
- **Left-shift gate:** a spec's perf price cites the `du` command and the directory list it was taken from, and the sketch names the same list.

### L5 — The scratch copy's "outside the repository" and "always cleaned up" claims are broader than the design (id 17)

- **Where:** 94 §2 S24; §5 security; §6 AC18.
- **What is wrong:** A bare `tempfile.TemporaryDirectory()` honours TMPDIR/TEMP, which can point inside the tree. Cleanup does not run on SIGTERM or SIGKILL. On Windows, a cleanup PermissionError turns a passing row into a traceback. AC18 checks only that a `with` item exists.
- **Consequence:** On those paths, scratch copies are left behind or a passing row ends in a traceback. Nothing is falsely certified or lost.
- **Fix (the skeptic judged it SOUND):**
  - Pass a `dir=` resolved outside the repository root, or assert that the temp path is not under the repository.
  - Use `ignore_cleanup_errors=True` and print a warning when cleanup fails.
  - Narrow §5 to "removed on normal exit and on an exception".
  - Have AC18 assert that the created path is outside `git rev-parse --show-toplevel`.
- **Left-shift gate:** a checklist entry. A spec claiming "outside the repository" for a temp path carries an AC asserting the path against `git rev-parse --show-toplevel`.

## Refuted (not items)

The skeptics refuted three findings, which are not items:
- Id 6: the `<strerror>` sites are owned by 92 S17, which 94 consumes.
- Id 8: a preference, with no observable defect.
- Id 11: a duplicate of id 12.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=17 confirmed=14 refuted=3 unverified=0 blocker=0 high=1 medium=7 low=6 agents=11 out-tokens=125586

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 4 "The tree_lib route, after this unit" and "The tree_lib route probe"; section 2 S7, S22; section 6 AC1 | high | high | confirmed | Re-read the specs. 41.md:33 (S1) reaches the memory-tree kit's parse_conf through `resolve_kit_dir("memory-tree", "tree_lib.py", here)`. 60.md:38 and 64.md:35 call that 'the route 41 S1 specifies'. 72.md:36-39 puts `resolve_memory_root` in tools/loop/loop_lib.py, reading `.memory-tree.conf` through parse_conf, and 72's sketch (line 84) calls parse_conf directly. 79.md:148 S25 and AC25 (`grep -n "parse_conf(" loop_lib.py`) require that call. All of these come at order 6, 36 and 40, before 94's 48. 94.md:174 TREE_LIB_SYMBOLS holds only the three derive_/GIT_ENV_LEAKS names. 94.md:199 makes any `resolve_kit_dir("memory-tree", ...)` outside load_tree_lib a HIT, and 94.md:205 requires every member to be inside need and every need to be a subset of TREE_LIB_SYMBOLS. grep over spec/*.md finds parse_conf nowhere in 86-94 except an unrelated 88:551. Nothing in 92 or 94 moves resolve_memory_root onto the loader. So on the tree the earlier units leave, AC1's probe goes red whichever way parse_conf is reached, and no scope item, edge or non-goal says what to do about it. | unsound | - |
| 2 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S4, S5, S6, S7, S8, S9 (AC16 half), S10 (92 half), S20, S22, S23 against section 6 | medium | medium | confirmed | Read 94 section 6 (AC1 to AC18) against S3 to S23. The only greps of 92 are these: AC1 (AC8 range, spec_from_file_location), AC2 (S8 range and sketch, budget.py), AC5 (AC8 range, S35), AC10 (S17 range, 88 S18), AC11 to AC13, AC14 (AC16 range, (no output)), AC16 (section 10, load_recall_kit) and AC18 (section 5, 3.3 MB). No criterion greps 92 AC16 for the S24/S21/class-name range greps that S9 orders. None greps 92 AC8 for the staged derive_X or import_module breaks (S6, S7) or the getattr population (S4). None greps 92 S8 or section 5 for need or first use (S8, S22), 92 S3/S8 for the sketch sites (S10), or 92 S17 for first non-blank (S20) or the 85 S3 sites (S23). AC4, AC14 and AC15 observe only code. I re-ran the counts at HEAD: AC8 range derive_X 0, import_module 0, getattr 0; AC16 range S24 0, S21 0, class name 0; S8 range need 0, first use 0; S17 range first non-blank 0, 85 S3 0. A pass can go green and still leave those 92 sentences unwritten. | unsound | - |
| 3 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 3 Edges, consumes-from TOOL-dDeclaredLoop-93 | low | low | confirmed | 93.md:58, the hands-off 94 bullet, cites '(the round-10 spec audit's ids 4, 11, 13, 20, 29)'. 94.md:151, the consumes-from 93 bullet, cites '(the round-10 spec audit's id 11)'. The two sides of one edge give different id sets. 93 section 3 itself hands ids 13 and 29 to 94, and 94 S9, S19, S20 and S23 (ids 4, 13, 29, 20) work on 92 AC16 and S17 as 93 leaves them. Only the record's text is affected. | sound | two-answers-to-one-question |
| 4 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md:section 6 AC3 | medium | medium | confirmed | I re-ran the section 4 exit-claim regex over spec/*.md with whitespace squeezed. It found op-81 ['1'], op-83 ['1'], op-88 ['1','1'], op-92 ['0'], op-93 ['1','1','1','1']: 9 claims, set {'1','0'}. Four of the claims are 93's own. After S1 rewrites 92 AC16, 93 plus 92 makes five and meets AC3's floor of 'at least five'. So if 81, 83 or 88 were reworded out of the regex, AC3 would still print {1} and pass, and the agreement it certifies would rest only on the unit's own sentences. | unsound | fixture-passes-by-finding-nothing |
| 5 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S21 and S24; section 4 "The tree_lib route, after this unit" (budget.py skew row) | medium | low | confirmed | 94 S21 tells the loader to follow row_grammar.load_recall_kit's idiom. I read tools/memory-tree/row_grammar.py around lines 1020-1032: it does `sys.path.insert(0, kit)` and then a plain `import bench`, so the module is cached in sys.modules. The 94 sketch's skew row first calls `loop_lib.load_tree_lib(need=()).__file__` in budget.py's own process, so the real tree_lib is already cached there. Then it copies the kit into scratch. Neither 94 S24, 92 S7 nor 90 S5 says whether the copy is checked in a subprocess. tools/check-spec-tokens.py load_kit_module (around lines 851-875) avoids the same collision by caching on the resolved path. The finding is true. The consequence is limited, though. The refusal exits non-zero, which in practice pushes a builder toward a subprocess. And if a builder does check in-process, AC18 and 92 AC7 go red. So the trap shows up as a failing check, never as a false pass, and the defect is confined to a builder's misstep that the gates catch. | sound | - |
| 6 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S23; section 6 AC17; section 4 Evidence (the `start failed: <strerror>` baseline) | medium | - | refuted | The premise does not hold on re-probe. The four hit locations reproduce: 85:43 (S3), 86:139 (S22), 88:159 (S24) and 90:129 (S21). But 88 S24 and 90 S21 are not left without an owner. 92 S17 (92.md:102-106) rewrites the OSError spelling to `start failed: <detail>` and states '90 S21 and AC21 and 88 S24 say so, in the rev bumps of 90 and 88'. 94 consumes-from 92 S17 (94 section 3, line 150). So the two sites the finding calls unowned belong to the unit 94 builds on, and once they are restated to `<detail>` the literal `<strerror>` is gone. 94 AC17's whole-file grep is the check that this happened. The claim that the baseline misplaces 88's hit is also false. 94 Evidence line 236 says only '`start failed: <strerror>` 1 each over 85, 86, 88 and 90', with no section given. The AC24 range is cited separately, for the different token `and the strerror`, which the awk over 88 AC24 confirms is there. The finder graded it medium and the core consequence (AC17 left red) does not follow, so it is refuted. | unsound | - |
| 7 | reuse | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S21 and S10; section 4 "The tree_lib route, after this unit" | low | low | confirmed | Confirmed by reading the specs. 94 S21 has the loader catch any Exception, refuse by class name and refuse once naming every missing symbol. Older wording survives in two places. 90.md:182 keeps `# ImportError \| SyntaxError -> 88 S33's refusal`, and 90.md:183-185 keep the per-name refuse loop. 88.md:183-188 (S33) names only `ImportError` or `SyntaxError`. 94 S10 restates only 90's TREE_LIB_SYMBOLS tuple line. 94 S21 names 92's §10 and 92's sketch (92.md:147, the same line), but not 90's sketch or 88 S33. 94 AC6 greps 90's sketch only for GIT_ENV_LEAKS and load_tree_lib, and AC16 checks only 92 §10. So after 94 lands the specs still describe the loader in more than one way. There is no behavioural effect, because the narrower statement is a subset of the wider one, so the defect is in documentation only. | sound | - |
| 8 | reuse | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S20 | low | - | refuted | This is a preference, not a defect the rubric grades. 94 S20 (94.md:115) and 88 S24 (88.md:157-163) use the same wording, 'first non-blank line', and both apply to `build_failure_detail` in tools/loop/guard.py. 88 S25 already makes that builder the one spelling. The danger the finding describes, two splitlines rules disagreeing on whitespace-only lines or a stray \r, is how a builder might write the code. The spec does not ask for it. Under 92 S17's rule, the detail is the first non-empty of the stripped strerror and str(exc). So for OSError("  \nb"), str(exc).strip() already yields 'b', and the example the finder proposes would not diverge either way. No observable defect follows from the spec as written. | sound | - |
| 9 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S10, S21, S22; section 6 AC6 | medium | medium | confirmed | Re-read the specs. 90's sketch 'The tree_lib route, after this unit' (90 spec lines ~176-185) still has the two-name tuple with the comment 'every tree_lib name loop_lib calls', `load_tree_lib():` with no `need`, the comment `ImportError \| SyntaxError -> 88 S33's refusal`, and the per-name `for name in TREE_LIB_SYMBOLS: refuse "tree_lib lacks <name>"` loop. 90 S4 says the loader 'refuses where any name in the module-level tuple TREE_LIB_SYMBOLS is absent'. 90 S6 has 86 S21 and 88 S33 state the refusal 'as a class over TREE_LIB_SYMBOLS'. 88 S33 (line 183) still names only `ImportError` or `SyntaxError`. In 94, S10 restates only the tuple line of 90's sketch, and AC6 greps only `GIT_ENV_LEAKS` over that range. S21 and S22 (any Exception, one refusal naming every missing name, a per-caller `need`) rewrite 92's text only. 94's own sketch has the new loader, so after 94's pass the sibling text contradicts it, for example on whether `need=("GIT_ENV_LEAKS",)` refuses over a missing derive_* name. No non-goal withholds this: the 'already wrote' non-goal covers only passages that already read as stated. The effect is contained to spec text that misleads the next reader, so medium. | sound | amendment-leaves-its-other-half-standing |
| 10 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S8, S21, S22; section 6 AC2 | medium | medium | confirmed | Re-read 92's sketch 'The tree_lib route, after this unit'. It prints `derive_conf_reads(...): tl = load_tree_lib()`, `derive_conf_constants(...): tl = load_tree_lib()` and the module-level `loop_witness.py: GIT_ENV_LEAKS = loop_lib.load_tree_lib().GIT_ENV_LEAKS`. In 94: S8 restates only '92 S8 and 92 §5'. S22 restates only '92 S8 and 92 §5 risks'. S21 puts only 'the idiom' (the loader body) into 92's sketch. S3 adds only budget.py to that sketch, and AC2's grep over that range checks only `budget.py`. 94's own §4 sketch shows the `need=` calls and the in-function loop_witness read, so after the pass 92's sketch would still show the import-time route that S8 removes. No criterion reds on it. The defect is contained to spec text, so medium. | sound | amendment-leaves-its-other-half-standing |
| 11 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md:section 6 AC3; section 4 'The exit-claim probe' | low | - | refuted | duplicate of id=12. I re-ran 93 §4's regex over memory/builds/dDeclaredLoop/spec/*.md with whitespace squeezed. It printed 81:1, 83:1, 88:1 twice, 92:0, 93:1 four times, then `9 {'0', '1'}`. So four of the nine claims come from 93 itself, as claimed. Id 12 states this same self-counting floor defect and adds more, and I confirm id 12. | sound | - |
| 12 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md:section 6 AC3, section 4 "The exit-claim probe" | medium | medium | confirmed | Reproduced. 93 §4's regex over the spec folder (whitespace squeezed) printed nine claims: 81, 83 and 92 one each (92's is the 0), 88 two, and 93 four, all four stating 1. It ended with `9 {'0', '1'}`. With 92's claim gone, 8 remain and 5 of them come from 81 and 93, so AC3's 'at least five claims' floor is met mostly by 93's own sentences. The matcher accepts only `\bexits (\d+)` within 60 characters of the backticked command. 93's own goal line (§1) phrases the defect as 'an exit code of 0', which the pattern does not match. A later rewrite of 92 AC16 (94 S19/S20 rewrite it again) worded 'exit code 0' or 'exits with 0' would leave AC3 and 94 AC10 printing {1}, and 94 AC10 does not re-run 93 AC1. The effect is a guard that misses one reworded relapse, so medium. On the fix: a grep for 'non-zero', 'exit code' and 'exit(s) of/with' near the plant name found no current sibling hit, so the widened matcher would not falsely red today. | sound | - |
| 13 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S5, section 4 "The tree_lib route probe", section 6 AC3 | medium | medium | confirmed | I read 94.md:201-205. A LOADER RESULT is defined only as 'a load_tree_lib(...) Call, or a Name bound from one in the same body', and the only escape HIT is 'a loader result as an argument of any call but getattr' (S5 at :63-65 says the same). Take `def tl(): return loop_lib.load_tree_lib(need=())` followed by `tl().derive_X`: the attribute's value is a Call to tl, not to load_tree_lib, so it is not in the population. The call inside the helper has need=() and has no members, so nothing goes red. `self.tl = load_tree_lib(...)` then `self.tl.derive_X` escapes the same way, because the value is an Attribute and not a Call or Name. AC3 at :294-299 stages only the helper-argument route. The read goes unchecked, and on a skewed kit it ends in an AttributeError, which contradicts §5 risks ('never a silent pass'). The effect is limited to loop-kit code, so medium. | sound | - |
| 14 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S22, section 4 "The tree_lib route probe" need(call) | medium | medium | confirmed | The sketch at 94.md:176 declares `def load_tree_lib(need=TREE_LIB_SYMBOLS)`, so need can be passed positionally. The probe at :203 defines need(call) as 'its literal `need` tuple of str, else TREE_LIB_SYMBOLS' and never mentions a positional argument. A builder who reads `need` as the keyword will treat `load_tree_lib(("GIT_ENV_LEAKS",)).derive_docstring_ids` as checking the full union, so it passes. At runtime the loader checks only GIT_ENV_LEAKS, so a kit lacking that derive_* name gives a traceback. A list literal is also unclassified: it is not a 'literal tuple', yet it is arguably not 'non-literal' either. This is a real hole in the probe's completeness, and the path is narrow. | sound | - |
| 15 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S2 and S21, section 4 "The tree_lib route, after this unit" (budget.py skew row) | medium | low | confirmed | tools/memory-tree/row_grammar.py:1010-1039 does `sys.path.insert(0, kit)` and then `import bench`, so the module lands in the sys.modules cache. S21 (94.md:119-123) tells load_tree_lib to follow that idiom. The skew row (94.md:187-189) calls `loop_lib.load_tree_lib(need=())` inside the budget.py process before it copies. I grepped 90, 92, 93, 94 and 88 for subprocess, child process and sys.modules: the only hits are 88's unrelated subprocess.run for git. Neither 90 S5, 92 S7 nor 94 S24 says how the row runs the copy. So the gap is real. If the copy were loaded in-process, the cached real tree_lib (and loop_lib) would be reused and the refusal would never fire. AC18 requires the label, so that build would go red, not ship. The consequence is a spec that leaves a trap for the builder, not a wrong result that ships, so low. | sound | - |
| 16 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 4 sketch (skew row 'copy dirname(...) and its siblings'), section 5 perf / scale | medium | low | confirmed | 94.md:189 reads 'copy dirname(loop_lib.load_tree_lib(need=()).__file__) and its siblings into scratch'. That dirname is tools/memory-tree, and read literally its siblings are all of tools/. `du -sk tools` printed 20766. 94 §5 (:267) prices about 3.3 MB, which matches the memory-tree and lib figures in §4 Evidence (3104 and 160) and leaves out loop/. S24 does not name the copied set. However, 92 S7 says the row is '90 S5's version-skew row', and 90 S5 (90.md:70-73) names `tools/loop/`, `tools/lib/` and `tools/memory-tree/` exactly. 94's own Evidence at :220-222 names the same three. So the authoritative population exists, and the defect is loose sketch wording plus a price that omits the not-yet-built loop/. The effect is close to cosmetic. | sound | - |
| 17 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md:section 2 S24, section 5 security, section 6 AC18 | low | low | confirmed | git hash-object on 94.md printed a1fb6cd2…, which matches the pinned blob. I re-read the cited lines. S24 (lines 133-136) promises a fresh TemporaryDirectory 'outside the repository … cleaned up when the row ends whether it passes or fails'. The §4 sketch spells it `with tempfile.TemporaryDirectory() as scratch:` with no dir= and no ignore_cleanup_errors. §5 security says 'removed on exit'. AC18 checks only three things: a `with` item that parses, an unchanged `git status --porcelain` after two concurrent runs, and the 3.3 MB grep. Nothing in the spec pins the temp root outside the tree. A TMPDIR or TEMP that points inside the repository would pass AC18 on any machine where it is not set that way. The spec says nothing about SIGKILL or SIGTERM, where no `with` cleanup runs, or about a cleanup PermissionError on Windows. So the claim is true. The effect is contained: leftover scratch copies, or a traceback on a narrow path. A git-status check on an inside-tree TMPDIR would show the copy as untracked, and nothing would be certified falsely or lost. Graded low because §5's guarantee is overstated and the paths are rare. | sound | - |
