# KICK-dKeptSession-50 — acceptance ledger

**Serves:** journal KICK-dKeptSession-50

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass. The `policy fixtures` leg, `govkit selfcheck` and the other legs the spec's section 7 names
were not run as commands. The criteria were observed on win32 at the pass's base `3e14697d` by
probes of the unit's own code: a `python -c` call of the new `run_mirror_upgrade("mirror-upgrade")`,
the function the `mirror-upgrade` row of `CASES` runs, its scratch repository and bare remote made
by `build_landed_repo` under `%TEMP%`; a scratch copy of arm 7l's sentence predicate from
`tools/govkit/govkit.py#selfcheck` run over the edited files and over their copies at the base; and
`sed`, `tr`, `grep` and `git diff` over the tree. The unit adds one function, `run_mirror_upgrade`,
which `python tools/lexicon/lexicon.py` graded with exit 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of the new
`mirror-upgrade` case and `govkit selfcheck`'s arm 7l over the README sentence and the case's
docstring among them; and the RED-first observation of the `New arm:` line in
`tools/policy/check_policy.py`, the case on its two staged breaks, a copy of `adopt-policy.sh` that
skips the mirror on a kept policy file and `check_mirror_text` with `legacy_blobs` left out of the
fields it compares, and green once restored.

## S4 — unit 40's wording, superseded

Unit 40 is CLOSED, so neither its spec nor its ledger is written (F1, resolved (b)). These two
passages of `2026-10-26-spec-KICK-dKeptSession-40.md` read as S3 of this unit says:

- Its §4 Migration: "A mirror rendered before this unit carries no `presets.toml` entry, so
  `policy-mirror.js` reads it stale once and the reader answers; the next `policy.py mirror --write`
  records the entry." Superseded by S3: a pre-unit mirror is re-rendered at the next landing by the
  `[[generated]]` row, and in an adopter by the `[[regenerate]]` row on every kit update unless
  `GOVKIT_RERENDER=0` is exported; with it exported the mirror stays as it was, the adopter's
  `--check` refuses it, and the hooks read it stale.
- Its §5 risks line: "every existing mirror reads stale once after landing, by design." Superseded
  by S3 for the same reason: the stale read lasts only where the upgrade is skipped, and there the
  check names it.

Unit 40's criteria are joined by AC1 and AC2 below, for the pre-unit mirror they never see.

**Evidences:** KICK-dKeptSession-50
- AC1 — over the planted pre-unit mirror, `bash adopt-policy.sh --scaffold --target <dir>` exited 0, its first line opening `kept` and its last `policy: mirror written`; the written mirror's `legacy_blobs` held `.agent-cap.conf`, `.governance/instructions.toml` and `tools/policy/presets.toml`, and `policy.py mirror --check` in `<dir>` exited 0 printing `policy: mirror fresh` (DERIVED, that probe).
  The case's probe returned 4 assertions and 0 wrong (DERIVED, that probe). The kit copy holds
  `presets.toml` from `MIRROR_KIT_FILES`, so the render recorded the store's key with a blob id.
- AC2 — over the same plant, before any re-render, `bash adopt-policy.sh --check --target <dir>` exited 1 and printed `policy-check: arm_mirror_parity · 1 finding(s)` and the finding line `legacy_blobs: differs from the render at HEAD` (DERIVED, that probe).
  The same run printed `arm_legacy_homes` with 112 findings of gov's legacy-home list against the
  scratch tree, so the exit alone observes nothing, as the spec says (DERIVED, that probe).
- AC3 — the squeezed mirror section of `tools/policy/README.md` piped into `grep -c "became an input"` printed `1`, and into `grep -c "became an input[^.]*GOVKIT_RERENDER=0"` printed `1` (DERIVED, that probe).
  The same pipes over the README at the base printed `0` and `0` (DERIVED, that probe). Arm 7l's
  predicate, copied, found 2 claims naming `update` and a re-render in the README and 1 in
  `check_policy.py`, each naming `GOVKIT_RERENDER`, against 1 and 0 at the base, with 0 refused in
  each (DERIVED, that probe).
- AC4 — the squeezed ledger piped into `grep -c` of each of the two passages S4 quotes printed `1`, and `git diff --name-only 3e14697d --` over unit 40's spec and its acceptance ledger, the working tree included, printed nothing (DERIVED, that probe).
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `mirror-upgrade`: `check_mirror_text` compares no `legacy_blobs`
