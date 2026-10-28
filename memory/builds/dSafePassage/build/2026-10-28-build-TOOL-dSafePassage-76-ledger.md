**Serves:** journal TOOL-dSafePassage-76

# TOOL-dSafePassage-76 — acceptance ledger

The unit as built, at spec rev-5. Product writes: `tools/govkit/upgrade_steps.py` (S1 `check_contained`'s
two git-directory refusals and `read_git_dir`; S2 move 1's staging; S3 `read_image_paths(..., index=True)`
and the reverse walk's fallback to it; S4 `derive_reverse_steps`' retired ids; S7 the five-parameter
`run_step_walk`; S8 the walk refusal's own prefix; the plants `kill-before-stage`, `kill-after-down-stage`,
`kill-after-down-stage-garbled`, `retired-step` and the `<slug>.down-block-after` switch),
`tools/govkit/govkit.py` (S6 and S7's two callers), `tools/lib/python_floor.py` and
`tools/lib/python-floor.sh` (S5, `derive_gov_root`), `tools/govkit/fixtures/retired_edits.py` (the
`render-filter-broken` plant), `tools/govkit/refusal_join.py` (`BRANCH_PIN` 327 -> 334 by the measured
delta, 466 -> 473), `tools/govkit/selftest.py` and `tools/lib/resolve-python.test.sh` (the `New arm:`
lines), the three help pages (S9), and `memory/map/generated/symbols.json` regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11, Python 3.15) over this worktree, by the unit's own fixture CLI or a probe, run from the
repository root.

Where the build met what the spec does not say: `read_image_paths` grades both sources through one
parse, so a working-tree image that does not parse or lists no paths is a refusal naming it too, never
a `KeyError` (move 1 now reads an image it finds); the `kill-after-up` plant's planted image is
therefore written whole; `FIXTURE_REVERSE_CHILD` prints a refusal as `rollback: refused · Refusal:
<reason>` and exits 1, so AC3's garbled variant reads no traceback and `[dSP-51]` AC5's needle still
matches.

Owed at the close: every `New arm:` line's RED-first observation — the `[dSP-76]` containment rows in
`tools/govkit/selftest.py` (AC1), the `check_step_walk` / `check_step_rollback` rows for
`kill-before-stage`, `kill-after-down-stage`, `kill-after-down-stage-garbled` and `retired-step` (AC2 to
AC4), arm 1e's two lines in `tools/lib/resolve-python.test.sh` (AC5), the `_rte_cases` row for
`render-filter-broken` (AC6), and the isolation fixture's unkeyed-kind prefix assertion (AC8) — and the
§7 legs at the bar.

**Evidences:** TOOL-dSafePassage-76
- AC1 — a scratchpad `python` probe calling `check_contained` over a `git init` target and a `--separate-git-dir` one — printed `refused` naming the path for `.git/hooks/post-checkout`, `.GIT/config`, `.git./x` and `.git /x`, `ok docs/a.md`, `refused gd/config` naming `<target>/gd`; `GIT~1` resolved to `.git` on this volume and `GIT~1/hooks/x` printed `refused` naming `<target>/.git`; a non-repository target's `read_git_dir` is `None` and `docs/a.md` passed there.
- AC2 — `python tools/govkit/upgrade_steps.py fixture walk --plant kill-before-stage` — exit 0, no `walk: FAILED`, printed `walk: after the kill · staged nothing · s1.txt and its image present` then `walk: the re-run · git diff --cached --name-only lists s1.txt yes · .governance/steps/fx/s1.before.json yes · fx/s1 applied`.
- AC3 — `fixture rollback --plant kill-after-down-stage` — exit 0, no `rollback: FAILED`, printed `rollback: the re-run · git diff --cached --name-status lists D s1.txt yes · D .governance/steps/fx/s1.before.json yes · fx/s1 rolled-back`; `--plant kill-after-down-stage-garbled` — exit 1, no `rollback: FAILED`, no `Traceback`, printed the refusal naming `.governance/steps/fx/s1.before.json` and `stage the restored paths and the image's removal by hand`, then `... to stage by hand: yes`.
- AC4 — `fixture rollback-update --plant retired-step` — exit 1, no `rollback-update: FAILED`, printed `updated to C · exits 0 · fx/s2 applied` and `update --rollback --to B --write exits 0 · update --rollback --to A --write exits 2, naming fx/s2, its [[retired]] row and that its down is owed: yes`.
- AC5 — `python tools/lib/python_floor.py down 3.12 <scratch git init>` — exit 2, `python-floor down: <to> is required outside gov's own tree: ...`; the same verb with no `<to>` from a copy in a scratch gov over that gov — exit 0, `the floor 3.12 restored in 1 file(s)`.
- AC6 — `python tools/govkit/fixtures/retired_edits.py --plant render-filter-broken` — exit 0, `6 of 6 observation(s) matched`: verdict `render-edited`, the `HELD BACK` line, one render-edited order, the edited bytes kept; with `--stub today` the verdict read `re-rendered` and the orders `0`, two `MISS` lines.
- AC7 — the spec's `inspect.signature` probe printed `['gov_root', 'target', 'receipt_path', 'receipt', 'rows']`; `git grep -n "run_step_walk(" -- tools/` showed no call passing a sixth argument; an `ast` probe over `govkit.py`, `selftest.py` and `FIXTURE_WALK_CHILD` found four calls, each of arity 5 (`govkit.py` 9454 and 11725 among them).
- AC8 — `fixture isolation --plant submodule-config-malformed` — exit 1, no `isolation: FAILED`, its refused line `fixture/status up: the repositories a step could enter from the target could not be cleared: ... .git/modules/sub/config or a file it includes does not read ..., so nothing was spawned`, no `declares what git runs as a program`; `submodule-filter` still leads with the executor prefix.
- AC9 — the spec's seven `git grep -F` phrases over `help/upgrade-steps.md` printed one line each, the two over `help/python-floor.md` one each, `cannot be proven unedited` one line in `help/update-edits.md`; the three negative greps printed nothing.
