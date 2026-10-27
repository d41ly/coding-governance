# TOOL-dWellOiledMachine-68 — the runlog and unattended Skills read their destination through `{skill_home}`, completing the install-target re-pointing

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-68-deviation-681.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-68-deviation-681.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 28, item H5, at HIGH. TOOL-dWellOiledMachine-14 S7 re-points five rendered Skill rows to the
token `{skill_home}`, but the tree holds seven: the runlog and unattended kits' rows, their probes and
LF pins, and their adopters' hard-coded paths are left at `.claude/skills`. Those two Skills still land
there under any harness, and 14 S8's `--check-targets`, which refuses any `.claude/skills` value in a
descriptor, cannot pass on the tree as built. This unit re-points the remaining rows and adopters, so
the check's population comes from the tree and reads clean.

## 2. Scope (IN)

- **S1** — The runlog descriptor. In `tools/runlog/kit.toml`, the rendered row's `to` (`:50`), the
  `adopted` outcome's `must_exist` probe (`:85`) and the `lf_pin` `pattern` (`:116`) spell
  `{skill_home}/runlog/SKILL.md`. Observed by AC1.
- **S2** — The unattended descriptor. In `tools/unattended/kit.toml`, the rendered row's `to`
  (`:65`), the `render-failed-half-stamped` outcome's `must_not_exist` probe (`:209`) and the
  `lf_pin` `pattern` (`:403`) spell `{skill_home}/unattended/SKILL.md`. Observed by AC1.
- **S3** — The two adopters. `tools/runlog/adopt-runlog.sh` sets `SKILL_REL` (`:66`) and
  `tools/unattended/adopt-unattended.sh` sets `SKILL_DIR` (`:635`) from `GOV_SKILL_HOME`, defaulting to
  `.claude/skills` when run by hand, as 14 S7 makes the five other adopters do; the `.gitattributes`
  instruction `adopt-unattended.sh` prints (`:1050`) names the resolved path. Observed by AC2.
- **S4** — The count corrected where it is stated. TOOL-dWellOiledMachine-14's §4 Evidence counts six
  `.claude/` `to` rows and its S7 five Skill rows; the tree holds eight `to` rows, seven Skill rows
  and one settings row. Spec 14 takes a rev bump at this unit's pass, its §9 line naming this unit and
  finding 28, so the spec and the tree agree. Observed by AC3.

## 3. Non-goals (OUT)

- No change to the five rows 14 S7 already re-points, to `target_context` or to the settings row.
- No Codex install target: TOOL-dWellOiledMachine-14 §3 leaves those to dShippedRelease.
- No change to which file each kit renders.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-14` — the `{skill_home}` token seeded by `target_context`, `GOV_SKILL_HOME` and `harness.py --check-targets`, which this unit's rows and adopters use and which grades them
- **hands-off** `TOOL-dWellOiledMachine-90` — the Skills' `{skill_home}` destination, whose hard-coded readers and check 31 resolve through it (findings 27, 57)

## 4. Design

### Evidence

- `git grep -n 'to = ".claude/' -- '*kit.toml'` prints eight rows at this base: seven Skill rows,
  among them `tools/runlog/kit.toml:50` and `tools/unattended/kit.toml:65`, and
  `tools/govkit/entries/settings-merge.kit.toml:19`.
- The same two kits spell the path again in a probe and a pin: `tools/runlog/kit.toml:85`, `:116`;
  `tools/unattended/kit.toml:209` (`must_not_exist`), `:403`.
- The adopters hard-code it: `tools/runlog/adopt-runlog.sh:66` `SKILL_REL=".claude/skills/runlog/SKILL.md"`,
  `tools/unattended/adopt-unattended.sh:635` `SKILL_DIR="$ROOT/.claude/skills/unattended"`.
- 14 S7 lists five rows and five adopters (`spec-14.md:73-83`); 14 S8 refuses any `to`, `probe` or
  `pattern` beginning `.claude/skills` (`spec-14.md:84-89`).

### Files touched (estimate)

- `tools/runlog/kit.toml`, `tools/runlog/adopt-runlog.sh`
- `tools/unattended/kit.toml`, `tools/unattended/adopt-unattended.sh`
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-14.md` (S4's rev bump)

### Alternatives rejected

- **Exempting the two kits from `--check-targets`.** An exemption reads as coverage and leaves two
  Skills at a Claude-only path under every other harness.

## 5. Production-readiness checklist

- security — none changes: a token govkit seeds and a target cannot supply (14 S7).
- perf / scale — none.
- error / empty / loading states — an unresolved token is a govkit refusal, never a path
  (`tools/govkit/govkit.py:6617-6641`).
- observability — `--check-targets` names any remaining literal by file and line.
- risks — an adopter run by hand with no `GOV_SKILL_HOME` keeps `.claude/skills`, today's path.
- testing — AC1 to AC3 and the arm in §7.
- migration — none for claude-code targets: `{skill_home}` resolves to `.claude/skills` there.
- user docs — none beyond `help/runtime.md`'s install-target section, which 14 S9 writes.

## 6. Acceptance criteria

- **AC1** — When `git grep -n '"\.claude/skills' -- '*kit.toml'` runs after the unit, it prints
  nothing, and `python harness.py --check-targets` exits 0 over the tree.
  Red when: a descriptor still spells `.claude/skills`, as the runlog and unattended rows do at this
  base.
- **AC2** — When `GOV_SKILL_HOME=.agents/skills bash tools/runlog/adopt-runlog.sh --scaffold` runs in a
  scratch target, the Skill lands at the runlog skill's SKILL.md, and with the variable unset at
  `.claude/skills/runlog/SKILL.md`; `adopt-unattended.sh` likewise for its Skill.
  Red when: an adopter writes `.claude/skills` with `GOV_SKILL_HOME` set.
- **AC3** — When `grep -n "TOOL-dWellOiledMachine-68" 2026-10-26-spec-TOOL-dWellOiledMachine-14.md`
  runs over spec 14, its §9 carries the rev line, and its §4 counts eight `to` rows.
  Red when: spec 14 still counts six.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `unattended kit gate` · `govkit selftest` · `policy fixtures` · `kit placeholders (a declared token its adopter substitutes)` · `memory hygiene` · `recall floor` · `recall floor arms`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/selftest.py · covers AC1 · the check-targets case staged with one runlog row restored to `.claude/skills` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 28 (H5).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-14's `{skill_home}` token and `GOV_SKILL_HOME`, applied to
the two kits its S7 left out; govkit's `resolve_tokens` (`tools/govkit/govkit.py:1233`) already
resolves every `to`, probe and pin value. The probe
`python tools/codebase-map/reuse_lookup.py "resolve a kit's Skill install destination through a token"`
ranked `resolve`, `resolve_kit_dir`, `kit_rel` and `kit_dir`, none a Skill destination; the token is
unit 14's, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "where does each kit render its Skill under a
harness" --terms "skill_home Skill destination kit descriptor adopter GOV_SKILL_HOME install target
harness adapter"`
