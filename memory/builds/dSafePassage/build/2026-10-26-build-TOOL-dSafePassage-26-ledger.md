**Serves:** journal TOOL-dSafePassage-26

# TOOL-dSafePassage-26 — acceptance ledger

The unit as built, at spec rev-11: the round-1 audit's minors, one item each. In
`tools/govkit/upgrade_steps.py`: the remote ladder inline, `resolve_landing_base`, `blob_at` (with
the batch `derive_introduced` reads through) and `write_atomic` moved in from govkit, which binds the
three back; `cmd_frozen` and `resolve_landed_ref` call them; `{to}` in a down's argv only, answered
by `update --rollback`'s `--to`; `build_step_env` carries the parent's `core.autocrlf` and
`core.eol`; the before-image written atomically, a cut-short image read absent only over unchanged
paths; the lock's `platform` and `boot_id`; a needs-target row's witness run on gov's own tree;
`read_steps` refusing a shallow clone and reading each commit's declaring files from that commit's
registry; the fixtures through `fixture_target.py`'s two factories; the plants `autocrlf`,
`truncated-image`, `lock-foreign-namespace`, `needs-target-source`. Elsewhere: `shims.py` (the
`--expect` window plant, the landing through `derive_introduced`, the js exit map, the module
forwarder's `sys.path`, four plants), `step_gate.py` (the reader contract, two plants),
`docs_leg.py` (console prompts, continuations, comments, unsplittable lines, four plants),
`govkit.py`'s one row-order writer, `steps/fanout_cap.py` and `steps/receipt_schema_4.py`,
`lib/python_floor.py` and `lib/python-floor.sh` (`{to}`'s population, the `floor` verb),
`lib/resolve-python.sh` and its 75 copies (the `tried:` line last, the alias gap), `lib/render-doc.sh`
and its four copies (a source receipt read as absent, S27), `push-main.sh`'s `resolve_lander_kit`,
the CI workflow's floor step, the lexicon comment, the help pages and the deploy skill.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC below was observed
on node d (Windows, git-bash) by the unit's own code: a CLI, a `python -c` probe, or a scratch
fixture under `%TEMP%` or the session scratchpad. Where a criterion names a gate leg, the hook
refused it to this role, and the line says OWED: the main loop observes it at the close.

**Evidences:** TOOL-dSafePassage-26
- AC1 — `git grep -n -e "def resolve_landing_base" -e "def derive_push_base" -- tools/govkit` printed one line, `tools/govkit/upgrade_steps.py`.
- AC2 — `git grep -n "resolve_landing_base(" -- tools/govkit` printed the calls in `cmd_epoch`, `cmd_frozen` and `step_gate.py` (two); `python tools/govkit/step_gate.py --print-base` printed `60d90cb7…`, equal to `git merge-base origin/main HEAD`.
- AC3 — an `ast` probe found no `Import`/`ImportFrom` naming govkit in `upgrade_steps.py`; the marker grep printed 1 (deviation 180).
- AC4 — both `check-receipt.py` greps printed one line each (`:212`, `:471`).
- AC5 — four of the five files name `step-rows-frozen`; `tools/run-gates/ceiling-evidence.txt` does not. OWED: its row is `derive-ceilings.py --write` over a measured run of the leg, which this role may not run.
- AC6 — `python tools/codebase-map/gen_map.py --write` regenerated the map; OWED: `--check`, the coverage and freshness leg.
- AC8 — `shims.py --fixture --plant window --window 2 --releases 1 --expect held` printed `the closed row: held · expects held · ok`, exit 0; `--expect allowed`, exit 1.
- AC9 — arm 1e of `resolve-python.test.sh`, run outside the suite in a stand-in: a PEP 701 file at the tip and absent at `<to>` passed (exit 0) and restored 3.11; present at `<to>`, exit 1 naming `planted.py:2`; `check_argv` refused `{to}` in an up naming the token, and `resolve_step_argv` refused it outside a rollback.
- AC10 — the same stand-in: an adopter's own PEP 701 `own.py` no receipt row names, exit 0; a TOML 1.1 table in `.governance/policy.toml`, exit 1 naming it.
- AC11 — `python tools/lib/python_floor.py check` printed nothing, exit 0; the literal grep printed nothing.
- AC12 — `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant autocrlf` exited 0, the step's oid equal to the parent's; with `read_line_ending_config` stubbed to nothing the same plant printed `DIFFERENT` and exited 1.
- AC13 — one `def blob_at`, in `upgrade_steps.py`.
- AC14 — one `def write_atomic`, in `upgrade_steps.py`; `receipt_schema_4.py` calls it.
- AC15 — the grep printed the `derive_introduced(` call in `resolve_shim_landing` and no `-S`.
- AC16 — `--plant window-prefix-id` (2 of 2) and `--plant window-comment-id` (1 of 1) each exited 0, each id at its own row's commit.
- AC17 — every row-keyed `outbox / f"update-` hit sits in `write_row_order`; the other three are keyed on a kit id.
- AC18 — `git grep -n -F '"init", "-q", "-b", "main"' -- tools/govkit/upgrade_steps.py "tools/govkit/fixtures/retired_edits.py" "tools/govkit/upgrade_walk.py" "tools/govkit/fixture_target.py"` printed `tools/govkit/fixture_target.py:31` only, at this unit's pass. Re-run at TOOL-dSafePassage-83's pass head it prints nothing: since TOOL-dSafePassage-67 (`f64d1302d`) the factory's line, now `tools/govkit/fixture_target.py:53`, reads `"init", "-q", "--template=", "-b", "main"`, and `git grep -n -F '"-b", "main"'` over the same four paths prints that line only.
- AC19 — 9009 stubs, `GOV_PYTHON` unset: the first stderr line opened `resolve_python: no usable python launcher`, the last read `resolve_python: tried: python3 python py`.
- AC23 — re-observed at TOOL-dSafePassage-83's pass head, `201eb127c`, in unit 8's AC5 fixture (a bare clone of that HEAD pushed as `main`, a `feat` branch with one unit commit, under `%TEMP%/sp83`): `bash tools/push-main.sh --prepare --slug fx` exited 0 with `prepared c159a29a`, a merge of two parents, and an empty `git status --porcelain`; then `python "tools/govkit/step_gate.py" --base HEAD` exited 0 printing `9 classes · 917 members at the tip · 0 vanished · 0 witnessed · 0 joining`, and `--list` there printed `file · 231 members`.
- AC24 — the `-A4` grep shows `pop("steps"` in the `_sch` block, and the `s1` block carries it.
- AC25 — `fixture rollback-update --plant refused|descendant|scoped|no-base` each printed `update exits 2`; the skill's usage line carries `[--rollback]`.
- AC26 — OWED: the two adopters' `--check` are legs. Probed instead `derive_kit_paths`, the reader those checks render through, in a scratch clone with and without a source-mode receipt: identical lines; HEAD's version differed on `{{REVIEW_PROTOCOL}}`, `{{UNATTENDED_PROTOCOL}}` and a bare `{{TOOL_ROOT}}` line, the fix in `lib/render-doc.sh`.
- AC27 — `retired_edits.py --plant seed-retired-edited` exited 0, 5 of 5.
- AC28 — the grep printed the `PROJECT_REGISTRY_EXTRA` member.
- AC29 — over `OTHER=1` and `FANOUT_CAP=2`: exit 0, `OTHER=1` left, the key 2, the witness 0, the down restoring both; over `FANOUT_CAP=abc`: exit 1, nothing written.
- AC30 — `fixture walk --plant truncated-image`: over unchanged paths the image rewritten and s3 applied; over a changed `kept.txt`, s3 failed `exit 1: upgrade_steps.Refusal: .governance/steps/fx/s3.before.json: …`.
- AC31 — `fixture update --plant needs-target-source`: source mode, witness absent, exit 1 with s2 failed attended; witness present, exit 0 with s2 applied.
- AC32 — `fixture lock --plant lock-foreign-namespace`: refused `unknown, it was taken under platform 'gk-elsewhere'`, exit 1, the lock unchanged.
- AC33 — `--plant missing-target --lang js`: the forwarder exit 127 and the error printed, the plant 0 (deviation 179).
- AC34 — `--plant py` and `--plant module`, each target importing `sib`, exited 0.
- AC35 — `docs_leg.py --fixture --plant console-prompt|continued-flag|unbalanced-quote` each exit 1 naming `help/guide.md:<n>`; `comment-apostrophe` exit 0; every `help/*.md` page reads the same commands as before.
- AC36 — a scratch gov whose descriptor moved: `list` gave the row the first commit at the old path; a `--depth 1` clone: exit 2 naming `git fetch --unshallow`.
- AC37 — the fixture with this tree's files staged in its clone: `reader-raises` exit 2 `class sg-fixture's reader raised on the tip side: RuntimeError: …`; `base-without-source` exit 0, `1 joining (sg-fixture)`.
- AC39 — `read_consumes_from` over units 3, 8, 12, 11 and 19 printed unit 1, units 3 and 11, unit 11, unit 15, and unit 18 among their producers.
- AC40 — OWED: a scratch adopter walked with fakes printing 3.14 first on `PATH`, the upgrade-walk leg's ground.
- AC41 — each file prints its `runtime.agents-in-flight` line.
- AC42 — `git grep -l -F '.agent-cap.conf' -- tools skills` printed 13 files, disposed: `tools/policy/policy.py`, `tools/policy/policy-mirror.js`, `tools/policy/check_policy.py`, `tools/policy/README.md` and `tools/hooks/README.md` kept as the legacy-home reader and its record under `cl-dClosedLoop-0016`; `tools/govkit/steps/fanout_cap.py` and `tools/hooks/kit.toml` kept, the step and its row that retire the home; `tools/govkit/fixtures/release-0/plants.toml`, `tools/govkit/selftest.py` and `tools/hooks/agent-cap.test.sh` kept, fixtures planting the legacy file; `tools/workflows/README.md`, `tools/workflows/REVIEW-PROTOCOL.template.md` and `tools/workflows/check-protocol-parity.test.sh` already re-pointed at `runtime.agents-in-flight`, naming the file only as the lowering it reads.
- AC43 — not built here: handed off to TOOL-dSafePassage-41 (§3 Edges), with its arm. That ledger's AC1 records the `ac-order` join over a scratch live spec listing `AC2` before `AC1`, exit 1 naming `ac-order <- AC2`, and its AC2 the predicate probe over this build's live specs, `out of order 0`; the close's arm observation below reds that arm.
- AC44 — `receipt_schema_4.py up` then `down` over a schema-3 receipt: the bytes equal, no `\r`.
- AC45 — the grep printed the alias gap and the 25 ms figure naming `python3`.
- AC46 — a fake `python3` exiting 1 under `-I`, the other names 9009 stubs: the refusal printed `python3: did not run`.
- AC47 — the query at `3708a705` printed seven statements, `tools/lexicon/selftest.py:109` among them (deviation 178).
- AC48 — `git ls-tree -r --name-only 3708a705 | wc -l` printed 5832 and `git ls-tree -r --name-only 3708a705 -- memory | wc -l` printed 5382, re-observed at TOOL-dSafePassage-83's pass head.
- AC49 — `git show "3708a705:tools/govkit/selftest.py" | grep -c "make_target("` printed 80, the definition at line 679; the count re-observed at TOOL-dSafePassage-83's pass head.
- AC50 — one `resolve_kit_dir "$py"`, in `resolve_lander_kit`, which every stage calls; arm 38 run outside the suite: green over this lander, red over HEAD's.
- AC51 — `python-floor.sh floor` over `3.15`, `3.15\nx=1`, `3.\n15` and `3.15\r\n`: `3.15` exit 0, exit 1, exit 1, `3.15` exit 0; the workflow's four floor steps run it.
- AC52 — the grep printed the schema-4 receipt paragraph and its `upgrade-steps.md` pointer.

NEW ARMS, their RED-first observation OWED to the main loop at the close (§7): `tools/govkit/selftest.py`
(AC9 AC12 AC14 AC30 AC31 AC32 AC37 and the one-writer arms, `refusal_join.py`'s `BRANCH_PIN` 324 -> 327 by
the measured 447 -> 450), `tools/lib/resolve-python.test.sh` (AC19 AC46), `tools/push-main.test.sh` (AC50).
`tools/check-spec-tokens.test.sh` (AC43) is TOOL-dSafePassage-41's.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: Three `New arm:` lines in scope, each break staged alone. **`resolve-python.test.sh`:** AC46, probe run without `-I`: `FAIL a launcher failing only under -I was not passed over as did not run: rc=0 …`. AC19, an extra line echoed after `tried:`: `FAIL a line prints after the tried: line: resolve_python: end`. Restored: PASS (6). **`check-spec-tokens.test.sh` AC43.** The suite has no arm of its own for AC43: spec 26 hands it to TOOL-dSafePassage-41's arm at `:937`. Break `bad = None` gave `arm FAIL  TOOL-dSafePassage-41 a spec dated at SPEC_AC_ORDER_CUTOFF listing AC2 before AC1 REDS naming both — expected rc 1, got 0`. Restored: 4/4. **`push-main.test.sh` AC50 (arm 38).** Break: `run_regen` given its own `resolve_kit_dir` call back. Result: `FAIL — 38 resolve_kit_dir "$py" runs 2 time(s), stages without resolve_lander_kit: [run_regen], …`. Restored: `push-main.test: all cases ok`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_upgrade_steps`, whole function. Break: the `check_argv` refusal of `{to}` outside a down disabled (AC9). RED: `FAIL [dSP-1 AC2] a {to} in an up argv exits 2 naming its file, row and key — rc=0 upgrade-steps: 1 step row(s) · 0 retired row(s) · landed ref main`. The source comments this arm as TOOL-dSafePassage-26 AC9 although its label says dSP-1. GREEN restored: FAILURES=0, 57 ok.
