# TOOL-dRankedPlan-42 — the `~` refusal of `--asks --path` is observed on the literal value, past the shell's tilde expansion

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 19 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-42-deviation-421.md](../build/2026-10-27-build-TOOL-dRankedPlan-42-deviation-421.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 10 at HIGH**, item **H4**. `TOOL-dRankedPlan-37` AC19 runs `gen_build_index.py --asks --path
~/x` unquoted. Bash expands the tilde, MSYS rewrites it to `C:/Users/<user>/x`, and the program refuses
it by the drive-letter rule it already has. So that half of AC19 is green before unit 37 S23 is built,
and it would stay green if `read_asks_args` were never routed through `check_repo_relative_path`. This
unit observes the refusal on the literal value: a selftest case hands `read_asks_args` the string
`~/x` with no shell in between, and AC19's command line is respelled quoted, with its red case
recorded at base. It repairs `TOOL-dRankedPlan-37`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The selftest case. `gen_build_index.py --selftest` gains a case that calls
  `_read_asks_run` (`tools/memory-tree/gen_build_index.py:4382`) with `["--path", "~/x"]` and with
  `["--path", "~"]`, and asserts each returns 2 with a stderr line naming the value and `~`. The argv
  list reaches `read_asks_args` as written, so no shell can expand it. Observed by AC1.
- **S2** — AC19's CLI half respelled. `TOOL-dRankedPlan-37` AC19's command becomes
  `gen_build_index.py --asks --path '~/x'`, quoted, which exits 2 naming `~`. Its red case is the base
  reading: at 0689e7fa the quoted value exits 0 and prints the backlog summary. This supersedes the
  unquoted spelling in unit 37 AC19. Observed by AC2.

## 3. Non-goals (OUT)

- The helper itself, `check_repo_relative_path`, and its other two callers: `TOOL-dRankedPlan-37` S23.
- The backslash forms of the same helper (finding 40): `TOOL-dRankedPlan-45`'s item.
- A tilde in `ROUTED_PATHS`. `routed_commits.py` already refuses a leading `~` at base
  (`tools/memory-tree/routed_commits.py:159`), and the conf value reaches it with no shell.

### Edges

- **consumes-from** `TOOL-dRankedPlan-37` — S23's routing of `read_asks_args` through `check_repo_relative_path` and AC19, whose CLI half S2 respells; without S23 the literal `~/x` is admitted and S1's case reds

## 4. Design

### Evidence

- Measured 2026-10-27 at base 0689e7fa in this worktree's Git Bash: `python
  tools/memory-tree/gen_build_index.py --asks --path ~/x` exits 2 with "`C:/Users/daily-agent/x` is
  absolute or climbs out with `..`", and the same command with `'~/x'` quoted exits 0. Both are PINNED.
- `read_asks_args` (`tools/memory-tree/gen_build_index.py:3282`) folds `\` to `/` and refuses `/`, a
  drive letter and `..` (:3339-3342), but not `~`.
- `_read_asks_run(root, conf, argv)` (:4382) is the selftest's own route into `read_asks_args`, already
  used for `--path` cases at :7262-7272.

### Why both halves

S1 is the arm: it reds on any build that leaves `~` admitted, on every shell and on Linux CI, because no
shell sits between the case and the reader. S2 keeps AC19's command honest for a builder who runs it by
hand, and its recorded red case proves the quoted form moves.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| the `--path '~'` selftest case | `gen_build_index.py --selftest` case | none |

### Rollout

Live at landing, at order 19, after unit 37 S23 has routed the reader through the helper.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`: S1

### Alternatives rejected

- **Respell AC19 quoted and add nothing else.** The criterion would then rest on a builder's shell
  quoting, and a later edit that unquotes it would turn it vacuous again with nothing red.

## 5. Production-readiness checklist

- security — no new surface; the case pins a refusal the shared helper adds.
- perf / scale — two in-process calls in the selftest.
- error / empty / loading states — bare `~` is covered beside `~/x`.
- observability — the selftest names the case and the value it refused.
- risks — none.
- testing — S1's case, red at base and green after unit 37 S23.
- migration — none.
- user docs — N/A — no user-facing surface moves.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --selftest` runs at this unit's tip, the
  `--path '~'` case passes, and with `check_repo_relative_path` made to admit `~` the case fails
  naming `~/x`.
  Red when: the reader admits a literal `~/x`.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --asks --path '~/x'` runs at this unit's
  tip, it exits 2 and its message names `~`.
  Red when: the quoted value exits 0, as it does at base.
  figure: the base exit 0 is PINNED, measured 2026-10-27 at 0689e7fa.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 · the `--path '~'` selftest case, staged by a `check_repo_relative_path` that admits a leading `~` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 10 (HIGH,
  item H4), repairing `TOOL-dRankedPlan-37`.

## 10. Reuse audit

The seam extended is the selftest's own `_read_asks_run` (`tools/memory-tree/gen_build_index.py:4382`),
which already drives `--path` cases without a shell. `python tools/codebase-map/reuse_lookup.py "refuse a
path that is absolute, has a drive letter, a tilde or climbs with dot dot"` was run by
`TOOL-dRankedPlan-37` and ranked name stems only, and no seam beyond that helper is needed here. The
recall query returned this audit's H4 item, which agrees with the measurement, beside this spec itself
and an unrelated dDeclaredLoop ask.

Recall terms used: `python tools/memory-recall/query.py "how is a tilde path refusal observed past shell expansion" --terms "tilde expansion quoted argument asks path refusal check_repo_relative_path selftest literal value MSYS drive letter"`
