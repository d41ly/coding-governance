# TOOL-dRetiredFork-8 — check-wiring resolves the settings file instead of spelling one path

**Status:** CLOSED · rev-4 · 2026-09-03 · node d · Tier-2 · base b0108f13 · streams tooling · order 1 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRetiredFork-8-1-acceptance-ledger.md](../build/2026-09-03-build-TOOL-dRetiredFork-8-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRetiredFork-8-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-8-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |
| [2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md](../reviews/2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md) | diff-review | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

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
- **S6** — Take this file's own install-prefix literals through the `KIT_REL` idiom in the same
  landing. Its ratchet row is `tools/install-prefix-carried.txt:17` at 6 occurrences, distinct from
  `tools/check-wiring.test.sh` at `:18` with 16.

## 3. Non-goals (OUT)

- inCMS's residual literal prefix sites are NOT deferred: S6 takes them here. rev-1 sent them to
  `TOOL-dRetiredFork-13`, whose
  declared population is "the 32 remaining shipped test and selftest files" and which therefore
  excludes this checker — so the sweep had no owner. S6 takes it here instead. rev-1's arithmetic
  was also unreconciled: "+67/-25 of which roughly 90 travel" leaves about two lines, not 39 sites.
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
- user docs — the resolution order in the script's own header AND in its runtime output, which
  prints the resolved path and its scope on EVERY run. `tools/README.md` does not exist, and
  the only other place check-wiring is documented is `AGENTS.md`, a governance carrier M3
  veto 2 puts outside this mandate. A path printed on every run beats a file nobody opens.

## 6. Acceptance criteria

- **AC1** — When the settings file sits inside the worktree, `bash tools/check-wiring.sh` resolves
  it, prints the path, and its arm results are byte-identical to the pre-change run.
- **AC2** — When the settings file sits outside the repo root, the command REPORTS that fact and
  still grades the wiring, where the pre-change command found no file and passed silently. Observed via `bash tools/check-wiring.sh`.
- **AC3** — When no settings file resolves, the command exits non-zero naming the failed resolution. Observed via `bash tools/check-wiring.sh`.
- **AC4** — `bash tools/check-wiring.sh --session` still auto-sets an unset `core.hooksPath` and
  never clobbers a set one.
- **AC5** — Every arm in `tools/check-wiring.sh` resolves its settings path through `settings_json()`,
  asserted by a grep for the literal `.claude/settings.json` in that file returning only the
  resolver's own preference rung. Byte-identity cannot catch a residual literal here, because §4
  states gov's own settings file sits where the literal already pointed.
- **AC6** — `bash tools/check-install-prefix.sh` reports `tools/check-wiring.sh`'s carried count
  BELOW its recorded 6, and the ratchet is re-baselined in the same commit.
- **AC7** — `bash tools/check-kit-versions.sh` exits `0` after the bump.

## 7. Gates

`check-wiring self-test` · `kit version markers` · `install-prefix (shipped surface)`.


## 8. Open questions

- **F1 — does the scope arm REPORT or RED?** inCMS reports, because its layout is deliberate. A
  project whose settings file escaped the repo by accident wants RED. Recommendation: report, and let
  `TOOL-dRetiredFork-16`'s extension point be how a project promotes it to a leg of its own.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the inCMS `KIT_CHECK_WIRING_DELTA` row and the
  `ARCH-dBriskLanyard-1 S10` worktree false-green it records.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings H4 and H14. H4: rev-1's §3 deferred 39 literal sites to a unit
  whose population excludes non-test files, leaving them undrained before `TOOL-dRetiredFork-17`'s
  ban at order 9; S6 takes the sweep here and AC6 observes the ratchet row falling. H14: S3's
  requirement that every caller read through `settings_json()` had no criterion, and AC1's
  byte-identity is structurally incapable of catching a caller left on the literal; AC5 is it.
- rev-3 · 2026-09-02 · folded spec-audit round 2, findings 25 and 29. 29: a cut-line section opened with
  "Nothing." and then listed an item. 25: the leg rename left a duplicate in §7.


- rev-4 · 2026-09-03 · built, and THREE of my own cuts were measured wrong before they landed.
  (a) The resolver was called EAGERLY at startup and exited 2 whenever nothing resolved, which
  killed 45 of the self-test's 76 arms — not one of them about settings. A repo with no settings
  file is legal; the refusal belongs to the ARMS that need it, so each says UNWIRED with the
  reason instead of passing by absence. AC3 is met by that non-zero, not by a whole-run refusal.
  (b) S6's collapse to ONE derived rung broke five recall arms and the two-layout arm: KIT_REL is
  derived from where the SCRIPT lives, not from the tree it grades, and those differ exactly when
  it matters. The dual-spelling probe is restored with only the PREFIXED rung derived.
  (c) The tolerant wrapper discarded the resolver's stderr, so "you named a path that is not
  there" and "there is no settings file" printed the same sentence. The resolver's own words now
  reach the operator.
  §5's user-docs row named a file that does not exist; the disposition matches
  `TOOL-dRetiredFork-7`'s.

## 10. Reuse audit

The seam is the resolver pattern in `tools/lib/resolve-python.sh`, which RUNS a candidate rather than
trusting a name — the same discipline applied to a path instead of an interpreter. `reuse_lookup.py`
reports no shared settings-locator symbol, and `tools/lib/` is gov-internal and never travels, so the
shape is copied inline rather than imported, which is this repo's standing rule for shipped kits.

Recall terms used: `check-wiring`, `settings.json`, `hooksPath`, `worktree`, `false-green`,
`resolver`, `refusal`, `non-match`, `prefix`, `adopter`, `scope`, `session`.
