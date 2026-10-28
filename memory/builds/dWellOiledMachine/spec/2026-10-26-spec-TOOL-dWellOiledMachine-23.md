# TOOL-dWellOiledMachine-23 — the session-start hook loading the set `memory.default-load` names, ending with `next`'s line, held under the hook channel's measured cap

**Status:** DEFERRED · rev-4 · 2026-10-28 · node a · Tier-2 · base 0689e7fa · streams tooling · order 19 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0301@29109ea6 whole
**Carries:** node:policy-key.memory.default-load

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-23-deviation-231.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-23-deviation-231.md) | deviation | — |
| [2026-10-27-build-TOOL-dWellOiledMachine-23-deviation-232.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-23-deviation-232.md) | deviation | — |
| [2026-10-28-build-TOOL-dWellOiledMachine-23-deviation-233.md](../build/2026-10-28-build-TOOL-dWellOiledMachine-23-deviation-233.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-126 |
| [2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-90 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

The compaction replay carries the card alone: the level-0 map returns only when a session regenerates
and reads it by hand, and the first position a session reads after a reset is a summary's, not a
derived one (gap-orient-18, gap-rt-01). The owner's session loads the set `memory.default-load` names,
the card and the map by default (PM-7), at startup, at resume and at a compaction, and the load ends
with `next`'s line computed at that moment (P22). The hook channel's output cap is measured with a
32 KiB map before the default is armed, and a size check reds a set over the measured cap rather than
letting the harness cut it silently (night pass, point 5).

## 2. Scope (IN)

- **S1** — The key's reader. `manifest-check.sh` reads `memory.default-load` once per hook run through
  `policy-shim.sh get memory.default-load` (I31; `tools/policy/catalogue.toml:1392`, values `card`,
  `card-and-live`, `card-and-map`, default `card-and-map`). A refused read loads `card` and prints
  `load — card only: memory.default-load refused`. Observed by AC1.
- **S2** — The set. `card` is the card the hook already prints. `card-and-map` adds the level-0 map,
  `python tools/memory-tree/gov_map.py`'s output from its cache `<git-common-dir>/gov/map/<tree>.map`
  (TOOL-dTotalRecall-14 S2, S7); `card-and-live` adds the generated `memory/LIVE.md`. The extra is
  printed under one line `load — <value> · <bytes> bytes` after the card. Observed by AC1.
- **S3** — Who loads it. Only a session whose binding (I17, TOOL-dWellOiledMachine-12) reads
  `owner: yes`; an act session loads its work order and gets no extra. Observed by AC2.
- **S4** — When. The same load runs inside `--card --write` at `startup` and `clear`, and inside
  `--card --replay` at `resume`, `compact` and `fork`, so the three moments the clause names, startup,
  resume and compaction, print one shape. Observed by AC1 and AC3.
- **S5** — The last line. Every run of S4 ends with the one `next —` line (I13) that
  TOOL-dWellOiledMachine-2's `next` verb prints for the binding's build at that moment, after the
  `now —` line; with no build named, or a verb that does not answer inside 10 s, it prints I13's
  terminal `next — none · <reason>`. Nothing is printed after it. Observed by AC3.
- **S6** — The cap, measured. `python tools/runtime/measure_hook_cap.py --live` starts one headless
  session through `launch_act` (I2, TOOL-dWellOiledMachine-1) in a scratch repository whose SessionStart
  hook prints a 32768-byte numbered map, reads the session's transcript for that hook's delivered
  output, and writes the `[[capability]]` row `session-start-output-cap` to the harness's table
  `tools/runtime/harnesses/claude-code.toml` (I7, TOOL-dWellOiledMachine-14): `value` the delivered
  byte count, `measured-on` the date, `binary-version` the harness's `--version`, and `cut` = `yes` when
  the delivered count fell short of 32768. `--transcript <file>` runs the same reading over a recorded
  transcript offline. Observed by AC4 and AC5.
- **S7** — Armed only once measured. While the session harness's table holds no
  `session-start-output-cap` row, `card-and-map` and `card-and-live` load `card` only and print
  `load — card only: the hook output cap is unmeasured for <harness>`. Observed by AC6.
- **S8** — The size check. Before printing, the hook sums the bytes of everything this run prints, the
  card, the extra, the `now —` and `next —` lines and the lines TOOL-dPlacedRequest-2 S7 and
  PLAY-dOrderedCharter-4 add to the replay. Over the measured cap it withholds the extra and prints
  `load — over cap · <n> bytes · cap <c> · withheld <map|live>`; when the card and the closing lines
  alone are over, it prints only that line, the `now —` line and the `next —` line. The run exits 0
  either way, since a SessionStart hook's output reaches the session only then, and never prints more
  than the cap. Observed by AC7.
- **S9** — The fixture arms live in `skills/session-kickoff/manifest-check.test.sh` with a planted
  policy file, a planted capability table and a stub `next` verb, and `measure_hook_cap.py --fixture`
  reads three recorded transcripts. The leg `runtime hook-cap fixtures` runs it: one `[[gate_leg]]`
  row of `tools/runtime/kit.toml` holding every manifest key, `enforces` §8 F4's tag, made by `python
  tools/run-gates/leg_factory.py new`, whose `--write` renders it into `tools/gate-legs.json`
  (TOOL-dWitnessedBar-11 S1 to S3; TOOL-dOrderedCharter-7 S3 reds a leg with no `enforces`).
  `leg_factory.py` is not in the tree at this base, so until that unit lands the pass hand-edits the
  manifest row to equal the declaration and records that it did. Observed by AC1 to AC8.

## 3. Non-goals (OUT)

- The `next` verb and its line: TOOL-dWellOiledMachine-2. This unit calls it.
- The level-0 map's renderer, budget and cache: TOOL-dTotalRecall-14.
- The binding and the card's re-attachment cap: TOOL-dWellOiledMachine-12. The card's home:
  TOOL-dWellOiledMachine-38.
- The instruction map in the replay: PLAY-dOrderedCharter-4. Its bytes count toward S8's sum.
- A second harness's cap: each adapter's row is measured on that harness when its adapter lands.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-12` — `session-bindings`: the binding's `owner` and `build` decide who loads the set and which build `next` answers for
- **consumes-from** `TOOL-dWellOiledMachine-14` — the `[[capability]]` table S6 writes `session-start-output-cap` to and S7 and S8 read
- **consumes-from** `TOOL-dWellOiledMachine-2` — the `next —` line the load ends with, and its terminal form
- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch_act`, the one launcher the live measurement starts its headless session through
- **consumes-from** external — `gov_map.py` and its cache (TOOL-dTotalRecall-14 S2, S7)
- **hands-off** `TOOL-dWellOiledMachine-79` — the session-start fallback and `measure_hook_cap.py` (findings 23, 41, 57), which the spec audit's minors batch repairs
- **hands-off** `TOOL-dWellOiledMachine-90` — the map extra keyed on `owner`, which treats `machine` as `yes` (finding 38)

## 4. Design

### Evidence

At this base the startup hook writes the card and the replay prints the stored card and one `now —`
line (`skills/session-kickoff/manifest-check.sh:706-725`); neither prints a map, a `next —` line or
checks a size against any harness figure. The one documented hook channel figure in the tree is
`ROUTE_CONTEXT_CAP=10000` (`tools/hooks/scratch-guard.js:1456`), the harness's documented cap for a
SubagentStart context, not a measured SessionStart one. The map's default budget is `32k`
(TOOL-dTotalRecall-14 S6), which is why the measurement uses a 32 KiB map: the default load is sized to
come back whole only if that much survives the channel.

### One run's output, `card-and-map`, under the cap

```
orientation — … (the card)
…
load — card-and-map · 18211 bytes
<the level-0 map>
now — HEAD 0689e7fa · branch … · clean
next — item.build.unit · actor builder · key item.build.unit@1·2#9b1c
```

### The measurement

The live arm's hook prints lines `map-line-<n>` padded to 64 bytes, 512 lines, so the delivered count
and the last line seen both say where a cut fell. The reading takes the SessionStart hook's attachment
from the transcript the launch names; a transcript with no such attachment is a refusal, exit 2, never
a row of 0. The row is PINNED to its `binary-version`, and a later harness version re-runs `--live`.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `session-start-output-cap` | capability row | `tools/runtime/harnesses/claude-code.toml` |
| `measure_hook_cap.py` `--live`, `--transcript`, `--fixture` | CLI | `tools/runtime/measure_hook_cap.py` |
| `load —` | output line | `manifest-check.sh` |
| `runtime hook-cap fixtures` | gate leg | `[[gate_leg]]` row of `tools/runtime/kit.toml` |

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/runtime/measure_hook_cap.py` (new)
- `tools/runtime/harnesses/claude-code.toml`
- `tools/runtime/kit.toml`

`tools/gate-legs.json` is the factory's render of the leg's declaration (S9).

### Alternatives rejected

- **Arm the map on the documented 10,000-character figure.** It is the SubagentStart figure, and the
  clause asks for a measured SessionStart cap before the default is armed.
- **Truncate the set to the cap.** A cut map reads as a whole one; withholding it and saying so is the
  clause's "rather than letting the harness cut it silently".
- **A separate SessionStart entry for the load.** Hooks of one event run in parallel, so its output
  could not be ordered before the `next —` line or summed with the card's.

## 5. Production-readiness checklist

- security — reads only the tree's own generated map, `memory/LIVE.md` and the policy key; the live
  measurement runs in a scratch repository through the one launcher.
- perf / scale — the map comes from its cache; one `next` call bounded at 10 s; the sum is over bytes
  already rendered.
- error / empty / loading states — a refused key, an unmeasured cap, a missing map and a silent `next`
  verb each print a `load —` or `next — none` line and the card still arrives.
- observability — the `load —` line names the value, the bytes and any withholding.
- risks — a cap measured on one binary version may shrink on another; the row's `binary-version` says
  which, and S7 holds the default off where no row exists.
- testing — the arms in §7 and AC1 to AC7.
- migration — none; the default is held off until the row exists.
- user docs — `skills/session-kickoff/SKILL.md`'s session-start paragraph names the load and its line.

## 6. Acceptance criteria

The fixture is a scratch repository with the kickoff kit, unit 12's binding with `owner: yes` and
`build: fx`, a planted `.governance/policy.toml`, a planted capability table, a stub map cache and a
stub `next` verb printing `next — item.build.unit · actor builder · key k1`.

- **AC1** — When `bash manifest-check.sh --card --write --session t1` runs under each planted value of
  `memory.default-load`, `card` prints no `load —` extra, `card-and-map` prints the stub map after a
  `load — card-and-map` line, and `card-and-live` prints `memory/LIVE.md`'s bytes.
  Red when: a value loads the wrong set.
- **AC2** — When the same command runs with the binding reading `owner: act-0123456789ab` and the value
  `card-and-map`, no map is printed.
  Red when: an act session loads the owner's set.
- **AC3** — When `bash manifest-check.sh --card --replay --session t1` runs with source `compact`, the
  last line of its output is `next — item.build.unit · actor builder · key k1`, after the `now —` line;
  with the stub verb sleeping 15 s it is `next — none · next verb did not answer`.
  Red when: any line follows the `next —` line, or the replay ends without one.
- **AC4** — When `python measure_hook_cap.py --fixture` reads its three recorded transcripts, one whole,
  one cut at 10000 bytes and one with no hook attachment, it writes `value` 32768 with `cut = "no"`,
  `value` 10000 with `cut = "yes"`, and refuses the third with exit 2.
  Red when: a cut transcript reads as whole, or the missing attachment writes a row.
- **AC5** — When `python measure_hook_cap.py --live` runs on a node with the pinned harness binary, the
  table gains a `session-start-output-cap` row naming that `binary-version` and the delivered bytes.
  Red when: the row's value is not what the transcript shows delivered.
  cost: one headless session, about a minute.
  permission: a live harness launch, which a spec pass may not run; the build run's main loop runs it.
  fixture: the pinned binary is the one TOOL-dWellOiledMachine-1's spike records; the tree holds no row.
- **AC6** — When the table holds no `session-start-output-cap` row and the value is `card-and-map`, the
  write prints `load — card only: the hook output cap is unmeasured for claude-code` and no map.
  Red when: the map is loaded with the cap unmeasured.
- **AC7** — When the planted row says 6000 and the stub map is 8000 bytes, the replay prints
  `load — over cap`, withholds the map, ends with the `next —` line, prints at most 6000 bytes and
  exits 0; with the row at 400 it prints only the over-cap, `now —` and `next —` lines.
  Red when: output over the cap is printed, or the run exits non-zero.
- **AC8** — When `grep -n -A16 "runtime hook-cap fixtures"` runs over the runtime kit's `kit.toml`, it
  prints a `[[gate_leg]]` row whose `enforces` holds §8 F4's tag; and `python leg_factory.py --check`
  exits 0 with that row declared.
  Red when: the leg is in the manifest with no declaration, or its declaration carries no `enforces`.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC6 AC7 · each value, an act binding, a silent `next` verb, an unmeasured cap and an over-cap map, staged by the base script, which loads the card alone and prints no `next —` line · none
New arm: tools/runtime/measure_hook_cap.py · covers AC4 · the cut and attachment-less transcripts, staged by a reader that takes the transcript's length as delivered · none

## 8. Open questions

- **F1 — What happens to a set over the cap?** (a) Withhold the extra and print the over-cap line, the
  card and `next —` kept; (b) truncate the map to fit; (c) exit non-zero. (b) is the silent cut the
  clause forbids, and (c) delivers nothing to the session. Rung 1, the clause's "rather than letting the
  harness cut it silently". RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — What loads before the cap is measured?** (a) The card alone, named; (b) the key's value
  unchecked. (b) arms the default before the measurement, against the clause. Rung 1. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — Where does the load run?** (a) Inside the card's own hook command, so its bytes are summed and
  ordered with the card's; (b) a second SessionStart entry. (b) runs in parallel with the card hook, so
  no order or sum holds. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — Which principle does `runtime hook-cap fixtures` enforce?** No v2 `[enforcement]` row names
  `cl-dClosedLoop-0301`, so the tag cannot be read off the clause. Options: (a) `principle.p27`, every
  load point loading its reader's units within a declared budget, which the measured cap and the size
  check are; (b) `principle.p22`, position derived, which only S5's closing `next —` line is. (b)
  covers one case of seven, (a) what the leg checks across them. Recommendation: (a). Open for the
  owner, who owns the `[enforcement]` table.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-79.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.
- rev-4 · 2026-10-28 · §2 S9, §4 Inventory and Files touched, §6 AC8, §8 F4 · the leg is declared
  once with `enforces` (F4, open) and the manifest rendered from it, per the parents' cross-check
  `2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck`, row 59.

## 10. Reuse audit

The seam extended is the kickoff kit's SessionStart pair, `write_card` and `print_replay`
(`skills/session-kickoff/manifest-check.sh:706`, `:721`), which already run at every source this unit
names; the map is TOOL-dTotalRecall-14's renderer and cache, the `next —` line unit 2's verb, the
launch unit 1's `launch_act`, and the row unit 14's table. No existing seam fits the cap measurement:
`python tools/codebase-map/reuse_lookup.py "print the default memory load at session start under a size
cap"` ranked `load`, `load_conf`, `resolve_caps` and `load_map_tree` by name stem; `resolve_caps`
(`tools/policy/budgets.py`) resolves budget keys and measures no harness channel. Scout B's row holds at
this base: the hooks at `settings.json:32-50`, the key at `catalogue.toml:1392`, and
`ROUTE_CONTEXT_CAP=10000` at `scratch-guard.js:1456`, which it rightly calls a documented SubagentStart
value.

Recall terms used: `python tools/memory-recall/query.py "what loads at session start by default and how
big may it be" --terms "memory.default-load card map level-0 replay SessionStart hook output cap 32 KiB
next line"`
