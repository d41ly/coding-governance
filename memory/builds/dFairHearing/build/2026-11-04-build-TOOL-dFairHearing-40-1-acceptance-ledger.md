# Acceptance ledger — TOOL-dFairHearing-40

**Serves:** journal TOOL-dFairHearing-40

Built against spec rev-5 at `ed2865025`, and committed against rev-6 at the pass's parent `a565f8339`,
whose acceptance criteria are rev-5's unchanged; between the two, only records under `memory/` moved.
At that parent the pass re-ran `base.py`, `constants.py` and `markers.py`, which printed the AC1 line's
values again, and over this commit's harness the AC19 stub probe, which passed all 4 arms again. `constants.py`, `markers.py`, `base.py`,
`attempts.py` and `void.py` are the spec's scratch probes, written under the run's scratch directory
with the corrections the spec states, and every clone or fixture repository went under `%TEMP%` and
was removed after its probe. The kept attempt clones and the Workflow result files were read and
left in place. No suite, gate or bar ran in the pass. The `New arm:` line, the AC19 arm in
`tools/workflows/tier2-review.test.sh` with its floor raised from 627 to 629, and the spec's legs are
owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-40
- AC1 — `base.py` — with `GATE_BASE` unset it printed `base 8bec4cefd957d194660a8d7c2916f420b7299074 from merge-base of HEAD and origin/main`. Over that sha, `constants.py` printed `constants 20` and no `->` line and exited 0, and `markers.py` printed `files 98` and no `->` line and exited 0. This commit adds no modified path to that range and moves no `version:` line
- AC2 — `base.py` — its sha equals `git merge-base HEAD origin/main`. Over a `git clone --depth 1 file://` of a two-commit repository, `%TEMP%/fsa` cloned to `%TEMP%/fsb`, it exited 2 printing `HEAD is not ahead of origin/main, or shares no merge-base with it (shallow or unrelated history)`. `git grep -n GATE_BASE` printed one line over each builder return of units 33 and 34, and each line says `GATE_BASE` was unset
- AC3 — `attempts.py` — over unit 30's record it exited 0 and printed the eight `scored` lines that unit 35's `## Scoring` section quotes, f1s1, f1u1, f2s2, f2u1, f3s1, f3u1, f4s1 and f4u1, and no `void after cap` line. The staged tables are unit 35 AC2's and were not re-run here
- AC4 — `void.py` — over unit 30's record it printed nine `agrees` lines and exited 0. It reads each clone's report through `parse_candidates`, its Workflow result file's `lensesDead` and `skepticsDead` (0 and 0 in all nine), and f2s1's parse error, which equals the text its void cell quotes. Over scratch copies it exited 1 three times: once naming line 58, record 1 `selected` attempt 1, whose cell cites `agent-a24141d7921658b99.jsonl:1` for `C:/Windows/win.ini`, a path that line does not hold; once naming the report on disk for the same row relabelled `refused`; and once naming line 60, f2s1, whose cell quotes a stated count of 2. As a control, a copy citing that line for the worktree's own path, which the line does hold, exited 0
- AC5 — `attempts.py` — the clones unit 37's ledger grades on its AC11 line are exactly the eight `scored` clones, and f2s1 is only listed there with its void reason. The checker printed no `void after cap` line, so that branch has an empty population here and is not counted as coverage
- AC8 — `renderLexedView` — a scratch node probe sliced `LITERAL_OPENERS`, `checkLiteralOpen`, `resolveLiteralEnd` and `renderLexedView` from `tools/hooks/agent-cap.js` and ran them in a `vm` context. It read `MAX_LENSES` as absent from `tools/hooks/agent-cap.js` and from `check-verifier-fanout.js`. Copies of the hook with each of the three interpolation lines appended exited 1, and copies with `// see ${MAX_LENSES}` and `// MAX_LENSES was 6` exited 0
- AC9 — `grep -n "^\*\*The decision:"` — it printed line 374 of unit 30's record, which names `selected`. This commit does not write `memory/guides/MERGE-BAR.md`, `memory/guides/SESSION-KICKOFF.md`, `memory/HYGIENE.md` or `tools/memory-tree/HYGIENE.template.md`, so their diff against the parent is empty. The `ungated` branch has an empty population and is not counted as coverage
- AC10 — `resolveKitDir` — a scratch probe built unit 37's rows 8 and 9 under `%TEMP%/fkr`. The canonical `tools/lib/resolve_kit_dir.py` printed `h` on both rows, and so did the port sliced between its markers in `tools/hooks/agent-cap.js`. This commit does not write `tools/hooks/agent-cap.js`
- AC11 — `constants.py` — every case exited 2 naming its cause and printed no traceback. `%TEMP%/fce`, holding the govkit kit's Python modules and no registry, named `registry.toml`, and `%TEMP%/fcf` named `No module named 'govkit'`. In a clone at `%TEMP%/fcd`, deleting `tools/roles/roles_lib.py` named `roles`, a `git mv` of `branch_reconcile.py` with its version raised named `branch-reconcile`, and removing that kit's registry entry printed `registry entries at HEAD~1 and not at HEAD: branch-reconcile`. Over the root commit `cbb8c17ba` at both ends it printed `no declared constant resolved at both ends`. As a staged break, a copy without `RuntimeError` in its `except` tuple printed `upgrade_steps.Refusal` as a traceback over `%TEMP%/fce`
- AC12 — `constants.py` — over `7d98741e3~1 7d98741e3` it printed `absent branch-reconcile`, `absent policy` and `absent roles` beside `check-wiring 1.32 -> 1.33` and `unattended 1.100 -> 1.101`. Over `0baf2e47a~1 0baf2e47a` it printed `new branch-reconcile 1.0` and `absent policy`
- AC13 — `grep -cE "ls-files.{0,8}--literal-pathspecs" replay_scorer.py` — it printed 0
- AC14 — `git log --grep='^Pass: TOOL-dFairHearing-36$'` — it printed `e69ecfcf0`. At its parent, `git ls-tree` lists `tools/lib/extract-arms.sh` alone, and `grep -c "PASS (N assertions)"` over that blob printed 2. So unit 36's AC6 held before unit 36 was built, and its AC6 is `precondition` evidence for `TOOL-dFairHearing-36`, never an observation of its S8 and S9
- AC15 — `grep -n -B12 "function deriveAddressKey"` — it printed the `function deriveAddressKey` line, and the comment above it holds no `:1664`. The comment cites no instrument line, so the `:1665-1666` half has an empty population and is not counted as coverage
- AC16 — `grep -c "^\*\*Serves:\*\*.*TOOL-dFairHearing-35"` — it printed 1 over unit 30's record
- AC17 — the `ungated` instrument — run with this checkout as the orchestrating repository over `%TEMP%/f1u1` to `%TEMP%/f4u1`, each range spelled in full shas, it printed 38, 20, 53 and 75 ungated, with checksums `668cc4180bb4`, `bffdbeb67415`, `6f166104d7ff` and `0f260b686f44`. Each equals its row in unit 35's `## Scoring` table: unchanged. Over a scratch copy of `tools/memory-tree/` whose `check_ungated` returns False, every row printed 0 ungated, every checksum differed, and the comparison named all four rows
- AC18 — `git show --name-only` — each path of unit 36's pass commit `e69ecfcf0` (4) and unit 37's `6d768c563` (11) is named on that unit's `dispatch` row in `memory/builds/dFairHearing/RUN.md`. Unit 37's row names `2026-11-04-build-TOOL-dFairHearing-37-1-acceptance-ledger.md`
- AC19 — the suite's own stub runner — a scratch probe ran the suite's runner and fixtures with only the `FH37` arm, the new `FH40` arms and the skeptic-prompt arm, over this commit's `tools/workflows/tier2-review.js`. With a `repo` of `C:/x y/z`, all 45 `git -C` commands read `git -C "C:/x y/z"`. A `repo` holding `$`, `"` or a backtick threw naming that character before any agent spawned. All four arms passed. Over the harness at `6d768c563` all four failed. `grep -c 'git -C \${repo}'` over the template printed 0

## Supersessions

Each one is named by the hands-off bullet to `TOOL-dFairHearing-40` in that unit's spec, and recorded here because that unit has no acceptance ledger at this commit (`TOOL-dFairHearing-23`'s F7 form).

- `TOOL-dFairHearing-33` AC1 — the "a constant moved on the branch" half of its Red when clause is answered by this unit's AC1 over `base.py`'s sha. AC1's reading at unit 33's own commit stands
- `TOOL-dFairHearing-33` S2 and AC3 — `new` is refused unless the descriptor is absent at the base, the registry is read at both ends, `RuntimeError` is caught, and the two refusals AC3 never staged are staged, by this unit's AC11 and AC12
- `TOOL-dFairHearing-33` Design — the sentence naming `(none declared)` as a value the `(` test reads is corrected: the guard above it skips undeclared entries, so only `(unresolvable)` reaches the test. It changes no behaviour, and no criterion observes it
- `TOOL-dFairHearing-34` AC1 — the build-wide half of its Red when clause is answered by this unit's AC1. AC1's reading at unit 34's own commit stands
- `TOOL-dFairHearing-34` Non-goals — a marker in an added or renamed file, or present only at the head of a modified file, is graded by `govkit selfcheck` within its basis of claimed paths and `marker_carriers`, never by `kit version markers`. It changes no behaviour, and no criterion observes it
- `TOOL-dFairHearing-36` Design — the sentence "It prints the line unit 31's probe prints, so units 33 and 34 read its sha the same way" is superseded: the two bases agree only with `GATE_BASE` unset and `HEAD` ahead of the remote tip, and each probe's label is read only by its own criterion
- `TOOL-dFairHearing-36` S12 — `base.py`'s tip refusal names both causes, observed by this unit's AC2
- `TOOL-dFairHearing-36` AC6 — labelled `precondition` evidence on this ledger's AC14 line
- `TOOL-dFairHearing-37` AC9 — the absence is re-read through `renderLexedView`, which decides the nested and comment copies that S9's reader left open (this unit's AC8). Its residual is that block comments are not blanked, so a `/* MAX_LENSES */` copy fails the probe closed
- `TOOL-dFairHearing-37` AC11 — the graded clones are the checker's scored ones, by this unit's AC5. The `void after cap` branch is empty
- `TOOL-dFairHearing-37` AC15 — the grep must print its anchor line, by this unit's AC15
- `TOOL-dFairHearing-37` S6 — every `git -C ${repo}` interpolation is quoted, and a `repo` holding `"`, `$` or a backtick is refused, by this unit's AC19
