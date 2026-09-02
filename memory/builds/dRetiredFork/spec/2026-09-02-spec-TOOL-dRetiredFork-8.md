# TOOL-dRetiredFork-8 — check-wiring resolves the settings file instead of spelling one path

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Absorb `settings_json()` and `check_settings_scope` from inCMS's `scripts/check-wiring.sh`. gov
hardcodes `.claude/settings.json`; inCMS's live settings file sits OUTSIDE the worktree on every one
of its nodes by design, so gov's spelling resolves to nothing there and the wiring checks pass by
finding no file. The adopter also carries an arm reporting when the RESOLVED settings file lies
outside the repo root, which is the worktree false-green it recorded at `ARCH-dBriskLanyard-1 S10`.
gov's hardcoded path is the defect; the resolver plus the scope arm is the fix.

## 2. Scope (IN)

- **S1** — `settings_json()` in `tools/check-wiring.sh`, resolving the settings file the way the
  harness itself resolves it rather than spelling one location, and REFUSING when the resolution
  yields nothing. A path that resolves to nothing must be a refusal, not a non-match — the same rule
  `TOOL-aBoundedCeiling-7` records for `.githooks/pre-push`.
- **S2** — `check_settings_scope`, reporting when the resolved file lies outside the repo root.
  REPORT, not RED, because a legitimate per-machine layout is exactly that shape.
- **S3** — Every existing arm in `tools/check-wiring.sh` reads through `settings_json()` rather than
  the literal, so no caller keeps a second answer to the same question.
- **S4** — Arms in `tools/check-wiring.test.sh`: a resolvable in-tree file, a resolvable out-of-tree
  file that reports, and an unresolvable one that REFUSES. The third observed RED first.
- **S5** — Bump `KIT_CHECK_WIRING_VERSION` and its `gov:kit check-wiring@` marker.

## 3. Non-goals (OUT)

- inCMS's remaining `check-wiring` divergence. Its row is `+67/-25` residual lines of which roughly
  90 travel with S1 and S2; what remains is 39 literal prefix sites, and those retire under
  `TOOL-dRetiredFork-13`, not here.
- `.claude/settings.json` as a written default. The resolver may PREFER it; it may not spell it as
  the only answer, which is the defect.

## 4. Design

### Data model

`settings_json()` returns one path or refuses. It never returns an empty string, because an empty
string is what let every downstream arm pass by absence.

### Migration

gov's own tree keeps its settings file in the worktree, so the resolver returns the same path it
spells today and gov's arm count is unchanged. That equivalence is the regression proof and must be
demonstrated rather than assumed.

### Alternatives rejected

A `SETTINGS_PATH` config key. It is a second answer to a question the harness can answer itself, and
an adopter 164 commits behind cannot read a key their installed kit predates.

## 5. Production-readiness checklist

- security — the resolver reads a path from the environment's own harness resolution. It must not
  accept a value that leaves its argument; grade it with the strict path class, as `govkit`'s
  per-entry `kit` key already is.
- perf / scale — one resolution, cached for the run.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an unresolvable settings file REFUSES. This is the whole unit.
- observability — the run prints the resolved path and whether it is inside the repo root, every
  time, so a false green is visible rather than inferred.
- risks — a resolver that finds a DIFFERENT file than the one the harness actually reads would make
  every wiring check confidently wrong. Mitigated by S4's arms and by printing the resolved path.
- testing + left-shift gates — `tools/check-wiring.test.sh`, already a bar leg.
- migration / rollback — reverting restores the literal; no adopter state.
- user docs — `tools/README.md` wiring section names the resolution order.

## 6. Acceptance criteria

- **AC1** — When the settings file sits inside the worktree, `bash tools/check-wiring.sh` resolves
  it, prints the path, and its arm results are byte-identical to the pre-change run.
- **AC2** — When the settings file sits outside the repo root, the command REPORTS that fact and
  still grades the wiring, where the pre-change command found no file and passed silently. Observed via `bash tools/check-wiring.sh`.
- **AC3** — When no settings file resolves, the command exits non-zero naming the failed resolution. Observed via `bash tools/check-wiring.sh`.
- **AC4** — `bash tools/check-wiring.sh --session` still auto-sets an unset `core.hooksPath` and
  never clobbers a set one.
- **AC5** — `bash tools/check-kit-versions.sh` exits `0` after the bump.

## 7. Gates

`wiring` · `wiring self-test` · `kit versions` · `install prefix (shipped surface)`.

## 8. Open questions

- **F1 — does the scope arm REPORT or RED?** inCMS reports, because its layout is deliberate. A
  project whose settings file escaped the repo by accident wants RED. Recommendation: report, and let
  `TOOL-dRetiredFork-16`'s extension point be how a project promotes it to a leg of its own.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the inCMS `KIT_CHECK_WIRING_DELTA` row and the
  `ARCH-dBriskLanyard-1 S10` worktree false-green it records.

## 10. Reuse audit

The seam is the resolver pattern in `tools/lib/resolve-python.sh`, which RUNS a candidate rather than
trusting a name — the same discipline applied to a path instead of an interpreter. `reuse_lookup.py`
reports no shared settings-locator symbol, and `tools/lib/` is gov-internal and never travels, so the
shape is copied inline rather than imported, which is this repo's standing rule for shipped kits.

Recall terms used: `check-wiring`, `settings.json`, `hooksPath`, `worktree`, `false-green`,
`resolver`, `refusal`, `non-match`, `prefix`, `adopter`, `scope`, `session`.
