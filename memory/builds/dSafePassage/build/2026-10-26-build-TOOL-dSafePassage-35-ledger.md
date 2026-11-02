**Serves:** journal TOOL-dSafePassage-35

# TOOL-dSafePassage-35 — acceptance ledger

The unit as built, at spec rev-7. `read_plan_destinations` keeps `kind == "write"` rows with no
`missing` (S1), which TOOL-dSafePassage-8's source receipt already calls (S2). The step gate's
`file` class reads the plan alone; its plant stages `git rm` of the first `.md` destination whose
source is that path, and the fixture gains the `stale-receipt` case (S3). The lock plants: a 6 s
census delay (S4), `lock-reused` writing `started_boot` 600 s back (S5), and the boot rows split out
of the namespace loop with `lock-other-boot`, `lock-no-namespace` and the child's `bootid` stand-in
(S26). The selftest leg's guard holds the census (S6). `REUSE_MARGIN_S`'s comment states each
backend's bound (S7). `STEP_REFUSED_KEYS` gains the credential-bearing values, plant
`local-url-userinfo` (S8). The lander's `write_untracked_snapshot` serves all three snapshot sites,
each refusing before its stage (S10, S11), with arms 39 and 40 (S11, S12). The floor down's `<to>` is
optional (S22). Argv resolution's closure moves into the step module, and govkit binds back eight
names (S24). Plant `autocrlf-local` (S27). `render_row_order_key` holds the one order-key spelling
(S39). The help pages are updated: `help/step-gate.md` (S3), `help/upgrade-steps.md` (S8, S14, S26)
and `help/python-floor.md` (S22).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) over this worktree, its scratchpad, or `%TEMP%/sp35`: a clone of this worktree's
HEAD with the unit's working changes committed onto it. The lander and the step gate run the code
committed in their fixture clones, so their probes needed that clone. Arms 39 and 40 of
`tools/push-main.test.sh` were run once by hand, as one script over `sp35`.

Owed at the close: every §7 leg, and the RED-first observation of each new arm on its §7
`New arm:` line. The `tools/govkit/selftest.py` arms are the `[dSP-35]` checks for AC1, AC3
(`stale-receipt`, and the member each `file` plant names), AC4 (the judge copy), AC8, AC23 and AC24.
The `tools/push-main.test.sh` arms are arm 39 (AC10) and arm 40 (AC11).

**Evidences:** TOOL-dSafePassage-35
- AC1 — `read_plan_destinations` on gov's root returned 231 destinations, equal to the `kind == "write"` rows with empty `missing`, and none starts with `.gitattributes:`; over a scratch gov whose kit plants an `lf_pin` and a `project-owned` rule, the plan held `('order', 'tools/demo/own.md')` and `('order', '.gitattributes:tools/demo/*.sh')`, both with nothing missing (the red a `missing`-only filter admits), and `read_file_members` returned only `{prefix}/demo/eng.txt`.
- AC2 — `update --target . --write` in the scratch clone `sp35` exited 0, and its receipt's 231 `files` paths equal the 231 `read_plan_destinations` returns on that tree, with no `.gitattributes:` pseudo-destination.
- AC3 — in `sp35`, `step_gate.py --fixture --plant stale-receipt` exited 1 printing `RED file:{prefix}/agent-instructions/README.md vanished`; `--plant file` exited 1 naming the same `file:` member its `git rm` took out (its `installable:` twin vanishes too, as §5 says); both `--with-row` runs exited 0; `git grep -n "install.json" -- tools/govkit/surface-classes.toml help/step-gate.md` printed nothing. The red: the same `stale-receipt` run against HEAD's committed class read the receipt at the tip.
- AC4 — `upgrade_steps.py fixture lock --plant lock-live-slow-census`, the plant `lock-live-slow-census`, exited 1, refusing `live, pid … is still running`, with `lock: the planted lock unchanged`; the same plant run from a judge copy whose `check_holder_dead` reads the clock after the census printed `lock: taken`, `lock: the planted lock CHANGED` and `lock: FAILED`.
- AC5 — `fixture lock --plant lock-reused` ran five times on node d, each exit 0 with `a reused pid` and no `lock: FAILED`; under `wsl.exe` (Python 3.14.4, `read_boot_clock` 440944.1) the same plant reclaimed naming `a reused pid` and exited 0, where at HEAD it printed `lock: FAILED` (§8 F4).
- AC6 — a `python -c` probe loading `tools/gate-legs.json` found `{prefix}/process-monitor/census.py` in the `govkit selftest` leg's guard.
- AC7 — `git grep -n -B6 "^REUSE_MARGIN_S =" -- tools/govkit/upgrade_steps.py` printed the comment naming `windows-join` at most 0.5 s and `posix-ps` at most 1 s.
- AC8 — `fixture isolation --plant local-url-userinfo` exited 1: the step was refused naming `remote.origin.url in .git/config`, the output held neither `gk-planted-user` nor `gk-planted-secret`, and with an scp-form `git@example.invalid:x.git` remote it printed `scp-form remote · not refused · git add exits 0`.
- AC9 — `git grep -n "write_untracked_snapshot" -- tools/push-main.sh` printed the definition and three calls (4 lines), and `git grep -c "ls-files --others --exclude-standard -z"` printed `tools/push-main.sh:2`.
- AC10 — arm 39's body over `sp35`: `--prepare --slug fx` with `TMPDIR` naming a file printed `gov first could not snapshot the untracked files before its walk`, exited 1 with `feat` unmoved, and left no receipt and no before-image. The red: the same body over HEAD's lander ran the walk and left `?? .governance/install.json`. The helper alone returned 1 for an empty path, a failed `mktemp` and a `git ls-files` outside a repository.
- AC11 — arm 40's body over `sp35`: the attended landing with the planted failing witness exited 1 with `did not hold on gov first` and `git status --porcelain` empty; the retry exited 0 and landed, and its `steps: gov first` and `regen:` commits named no `.governance/steps` or `.governance/outbox` path and recorded no `planted-witness-fails` row. No kit version was owed, so no `mint:` commit was made.
- AC12 — a `bash -c` probe extracting every `resolve_python` block between its markers, CR bytes stripped, found 75 copies and none differing from `tools/lib/resolve-python.sh`; with `tools/check-template-size.sh`'s copy put back on the pre-unit echo rule in `sp35`, the probe printed `DIFFERS tools/check-template-size.sh`, and `python tools/lib/python_floor.py check` printed nothing and exited 0. The same probe found 102 `resolve_kit_dir` copies, the step module's new one included, none differing.
- AC13 — `git grep -n -i -F "below schema 4 no step row is persisted" -- help/upgrade-steps.md` printed `help/upgrade-steps.md:135`, the receipt section's sentence.
- AC14 — a `python -c` `ast` probe of `tools/govkit/upgrade_steps.py` found one `def test_steps_recordable`, one call of it inside `set_step_state`, and no `Compare` node reading `schema` there.
- AC16 — `git grep -n -F "schema-step-early"` printed `ROLLBACK_SCHEMA_PLANTS` holding it, and its branch in the `rollback` family.
- AC18 — `git grep -c -F "<phrase>"` printed `:1` for each of the eight rows of §4 "The cites, by phrase", against TOOL-dSafePassage-1, -2, -3, -4 and -10.
- AC19 — in a scratch clone with the three pre-unit 3.12-only files taken out by one commit, as TOOL-dSafePassage-11's ledger observed its AC6, and the plant `v = f"{"X" if c else "y"}"` committed at `HEAD`, `bash tools/lib/python-floor.sh down 3.11 <clone>` printed `mode static` and `fx_floor_plant.py:2`, and exited 1; with `<to>` before the plant it exited 0, `the floor 3.11 restored in 77 file(s)`. A plant left only in the working tree was not named by the call without `<to>`, so the default grades a commit. `git grep -n -F "down 3.12 <target> [<to>]" -- help/python-floor.md` prints the upgrade-step line.
- AC20 — `python tools/lib/python_floor.py check --rev 3708a705` printed seven statements, `tools/lexicon/selftest.py:109` among them.
- AC21 — an `ast` probe found the five functions, the eight constants and `resolve_kit_dir` defined in `tools/govkit/upgrade_steps.py`, no import naming `govkit`, and exactly the nine borrowed attributes off `load_govkit()`, where HEAD's thirteen added `resolve_shell_argv`, `resolve_tokens`, `target_context` and `resolve_kit_dir`; govkit binds back the eight names once each and none of `_BASH`, `ANSWER_VALUE_RE`, `DRIVE_PREFIX_RE`, `PER_KIT_PATH_TOKENS` and `TOKEN_VALUE_RE`; `git grep -c "^# >>> resolve_kit_dir"` printed `tools/govkit/upgrade_steps.py:1`, and `git grep -n "govkit\._BASH" -- tools/govkit/selftest.py` printed nothing.
- AC23 — `fixture lock --plant lock-other-boot` reclaimed a live pid's lock, naming `this host has booted since, as 'gk-boot-after'`, and exited 0; `--plant lock-no-namespace` refused `unknown, it was taken with no pid_ns recorded` under the `pidns` stand-in and exited 1, and with no pid_ns on either side the census reclaimed it.
- AC24 — `fixture isolation --plant autocrlf-local` printed `the step's oid 4e349b59… · the parent's 4e349b59… · equal` and exited 0, the liveness check holding that the parent's global `true` moves the oid.
- AC26 — `bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh` with `GOV_PYTHON` unset and fakes for `python3` (exit 1 under `-I`), `python` and `py` (9009) first on `PATH` exited 1, printing `python3: did not run`.
- AC27 — `git grep -n "resolve_landing_base" -- tools/govkit` printed one definition in `tools/govkit/upgrade_steps.py`, govkit's binding of it, and the calls in `cmd_epoch`, `cmd_frozen` and the step gate.
- AC28 — `git grep -n -e 'update-conflict-' -e 'outbox / f"update-'` printed three `outbox / f"update-…-{eid}.md"` lines keyed on an entry id, one comment and one glob, and no row- or slug-keyed spelling outside `render_row_order_key`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: Two `New arm:` lines in `tools/push-main.test.sh`, each break staged alone. **AC10 (arm 39).** Break `brk-35a10` (`d857caef4`) puts the pre-unit inline snapshot line back at cmd_prepare's site. It gave `FAIL — 39 an unwritable snapshot fell through to the walk, or the refusal did not name gov first's snapshot: …`, reading `receipt=present`. GREEN at `83817478f`: `ok — 39 …`, 139 s. **AC11 (arm 40).** Break `brk-35a11` (`ff65f58e0`): the attended gov-first refusal without `remove_new_untracked`. It gave `FAIL — 40 the attended landing with a failing witness did not refuse at gov first on a clean tree, …`, reading `plant-rc=1 stage=gov-first plant-left=[?? .governance/install.json] retry-rc=2`. GREEN: `ok — 40 …`, 402 s.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_walk`, cut to `lock-other-boot` and `lock-no-namespace`. Break: the reboot branch (two differing boot ids, so the holder is dead) disabled. RED: `FAIL [dSP-35] fixture lock lock-other-boot exits 0 and names this host has booted since, as 'gk-boot-after', which ended its holder, lock: taken` with `lock: FAILED · the reclaim does not name the reboot`. `lock-no-namespace` stayed ok. GREEN restored: both ok. This unit's staged judge copy, `[dSP-35] AC4`, was also seen going red under unit 22's break and ok once restored.
