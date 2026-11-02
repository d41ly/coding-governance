**Serves:** journal TOOL-dSafePassage-46

# TOOL-dSafePassage-46 — acceptance ledger

The unit as built, at spec rev-3. S1 needed no code: TOOL-dSafePassage-34's pass already raised
`cutoff_keys_armed` 36 -> 37 in the commit that arms `SPEC_AC_ORDER_CUTOFF`. S2: arm 37 of
`tools/push-main.test.sh` loads `check-arms.py` from `"$HERE/$_mt_rc/"`, the memory-tree kit arm 26's
scan finds beside the lander, and prints a `skip — 37` line naming the absent kit where there is none.
S3: `tools/memory-tree/SPEC-TEMPLATE.template.md` gains the `SPEC_AC_ORDER_CUTOFF` paragraph after
the `SPEC_FAILURE_MODE_CUTOFF` paragraph and its example, spelling the checker `{{SPEC_TOKEN_CHECKER}}`;
`memory/TEMPLATE-SPEC.md` carries the same paragraph with that placeholder rendered as
`tools/check-spec-tokens.py`; `tools/memory-tree/.memory-tree.conf.example` gains a blank
`SPEC_AC_ORDER_CUTOFF=""` row with its comment, after `SPEC_GUARD_LEGS_CUTOFF`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) over this worktree or a scratch dir under the session scratchpad.

Owed at the close: the `memory/DECISIONS.md` row S1 leaves to the main loop in a `Pass: none` commit
(AC1's second half); the RED-first observation of the `New arm:` line (arm 37 of
`tools/push-main.test.sh`); `push-main self-test`, `foreign-prefix parity (every self-test at three
prefixes)`, `kit/dogfood doc parity`, `recall floor`, `recall floor arms`, `memory-hygiene self-test`,
`drift-audit records` and `spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dSafePassage-46
- AC1 — `git log --reverse --format=%H -S '"cutoff_keys_armed": 37' -- tools/drift-audit/drift_signals.py` printed first `56aef62aac5a2fea23ecda473ac00660cccb797f`, subject `build(dSafePassage): TOOL-dSafePassage-34 — ... cutoff_keys_armed 36 -> 37`, trailer `Pass: TOOL-dSafePassage-34`; its `git show --stat` lists `.memory-tree.conf` and `tools/drift-audit/drift_signals.py` and not `memory/DECISIONS.md`; `python tools/drift-audit/drift_report.py --json` read `cutoff_keys_armed` value 37 of 37, tolerance 37. The decision-row half printed nothing yet: it is the main loop's, at the close.
- AC2 — `git grep -n -e "check-arms.py" -e "tools/memory-tree" -- tools/push-main.test.sh` printed `:1402` (`' "$HERE/$_mt_rc/check-arms.py" "$1" ...`), `:1404` (the comment), `:1406` (the guard on `"$HERE/$_mt_rc/check-arms.py"`) and `:1428` (`skip — 37 no memory-tree kit (check-arms.py) beside this lander ...`); no line spells `tools/memory-tree/`. A scratch probe running the arm's lines printed two `ok` lines from gov's tree, two `ok` lines from a lander copy with the memory-tree kit copied beside it as `mt-x/`, the `skip — 37` line from a lander copy with no kit, and two `FAIL` lines from an arm copy loading `tools/memory-tree/check-arms.py` by a typed path at the foreign prefix.
- AC3 — `git grep -n -e "SPEC_AC_ORDER_CUTOFF" -e "ac-order" -- tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md tools/memory-tree/.memory-tree.conf.example` printed `SPEC-TEMPLATE.template.md:507` and `:509`, `TEMPLATE-SPEC.md:514` and `:516`, and `.memory-tree.conf.example:163` and `:169:SPEC_AC_ORDER_CUTOFF=""`. The two docs' changed lines are equal once `{{SPEC_TOKEN_CHECKER}}` reads `` `tools/check-spec-tokens.py` ``.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, `tools/push-main.test.sh` AC2, run at a foreign prefix inside the clone. **GREEN cases:** with the memory-tree kit copied beside the lander as `mt-x/` (`fp/`), both arm-37 `ok` lines; with no kit beside it (`fp2/`), `skip — 37 no memory-tree kit (check-arms.py) beside this lander, so the derived-count arm did not run`. **Break:** an arm copy loading `"$HERE/memory-tree/check-arms.py"` by a typed path, which is the spelling before unit 46 (`8c69f3e47`). Result: `FAIL — 37 cmd_prepare refuses 0 way(s) …, PREPARE_REFUSALS carries 6 row(s)` and `FAIL — 37 the derived count moved …: 0, not 0`.
