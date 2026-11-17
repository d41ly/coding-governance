# Revision — aPiecewiseGrade: TOOL-aPiecewiseGrade-2 diverged at its builder

**Serves:** research TOOL-aPiecewiseGrade-2

## The brief

### Goal
DIVERGENCE: section 4 S2 says to promote with `{ rm -rf "$_stspecs" && mv "$_stspecs.next" "$_stspecs"; } 2>/dev/null || :`. That `mv` is a rename into place from a fixed temp name. Section 7 lists the gate `shell hygiene (a fixed-name temp renamed into place)`, and that gate would go red on it. In tools/gate-lint/sh_hygiene.py, scan_temp_file counts an `mv` as `fixed` when its source is not a single expansion and contains no `$(mktemp`. The source `"$_stspecs.next"` has that shape: it is the same as the leg's own registry fixture, `mv -f "$f.tmp" "$f"`. Spelling it through a bound local such as `_stnext="$_stspecs.next"` still counts as `fixed`, because the leg follows the binding one hop. The leg needs memory/project/temp-name-sites.txt to declare exactly the measured count for each file. Its row `tools/unattended/unattended.sh fixed-temp 2` would then be wrong, since the file would hold 3 such sites. That file is not in section 4's Files touched, and its header and the lint's docstring say the registry only shrinks. Its existing rows are sites that predate the lint and are waiting to be removed, not new ones. The lint's fix is an unpredictable temp name, and that is not available here. The name `<dir>.next` is fixed by TOOL-aPiecewiseGrade-1's closed contract (tools/check-spec-tokens.py lines 296-300: 'the caller promotes <dir>.next ... by removing <dir> and renaming <dir>.next to it'). Writing S2 as specified therefore turns a section 7 gate red. Getting around the leg by wording the code differently would ignore the tool's refusal, which the [tools] rule forbids. To be buildable, section 4 S2 and Files touched need to choose one of three options. (a) Add `memory/project/temp-name-sites.txt` to Files touched and raise the `tools/unattended/unattended.sh` row from 2 to 3, with a reason. This is an owner ruling against the registry's shrink-only rule. The reason would be that the source is a directory the checker creates with `os.makedirs` after removing it, inside the worktree's git dir. (b) Promote without a rename, for example by copying, and state what that costs. (c) Revise unit 1's contract in a new unit, because a CLOSED spec stays frozen. Two smaller notes for the same revision. First, S4 calls the text ending 'recorded under the sidecar root only when the tree and HEAD held still while it ran' a sentence. At HEAD, and at the cited blob d92b6991, that is only a clause: the sentence goes on '; with no fingerprint it announces that the cache is off and runs the checker.' S4 should say the new sentence goes after 'runs the checker.' Second, S1 puts `_stspecs` beside the record path, but the read half `run_spec_token_check` has no `_stdir`. It receives the start half's state only through the seven ST_ globals. S1 or the Inventory should say whether the read half works it out from `_strec` (`${_strec%.key}.specs`) or carries an eighth ST_ global. The Inventory names neither.

### Acceptance
- The differential arm's every step prints byte-identical stdout and the same exit status from the plain and the incremental checker, and each plant is one the arm can be seen red on.
- After a commit that moves one spec, the incremental run re-grades exactly one spec.
- A timed `--dispatch` on node a after a sequential pass commit, base against built, on one frozen clone.

### Gates
The spec-tokens self-test and the driver suite's dispatch arms, run directly. `check-arms` over the driver suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### Non-goals
- Scoping the check to the dispatching build.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`.
- The bar's spec-tokens leg, which keeps the plain whole-tree run.
- aLightenedLoop's whole-key cache, except what runs on its miss.
- The unattended Skill.
- A kit version bump by hand.

### Limitations
- aLightenedLoop is not landed. No unit builds before it lands, and the specs' citations of its code are blob-pinned so they resolve before and after.
- A spec's acceptance criteria cite no path its unit has not built yet.
- Every spec line stating a measured figure carries the word PINNED or a commit sha on that line.
