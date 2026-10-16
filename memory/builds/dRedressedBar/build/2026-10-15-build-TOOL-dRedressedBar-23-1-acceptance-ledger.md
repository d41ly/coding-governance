# TOOL-dRedressedBar-23 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-23

This is the build pass of the round-1 closing diff review's govkit batch, report ids 4, 5, 12 and
13, built from spec 23 rev-1. `<w23>` is `9a894f23a`, the spec-writer pass that corrected specs 12,
14, 15, 16 and 17. `<p23>` is `baca8fe05`, the product commit, and `<p23m>` is `e8430e2cb`, the
kickoff-manifest re-stamp at it. `tools/govkit/` is byte-identical at `bf42c5113` and at `<w23>`,
so every cited line held until the build pass.

The product commit changes the deployer, its selftest and one guard in `tools/gate-legs.json`, and
re-stamps the kickoff manifest at its parent. `memory/map/generated/symbols.json` came from
`gen_map.py --write`, run alone, and the build README's rows and `memory/LIVE.md` from
`gen_build_index.py --write` over spec 23's dispatched INPROGRESS header, committed with them. The
pre-commit hook's staged legs, memory hygiene and the manifest ratchet among them, passed both
commits.

No merge bar, gate leg or self-test suite was run by this pass, and no check of
`tools/govkit/selftest.py` was executed: the new `[dRB-12]` order checks, the three `[dRB-23]`
blocks and the per-member `[-21] AC2` checks were parsed, read and lexicon-checked, never run, so
the close's `govkit selftest` run is their first execution. The naming lexicon answered OK for
`run_target_argv` and for the nested `read_order_halves23`. Every new selftest local was searched
for at `<w23>` and one, `_src23`, was already bound at `:5342`, so the static check reads
`_gsrc23`.

Every criterion was observed by a direct probe written apart from the arms, on node d, Windows,
under Python 3.12.10. A target is a fresh `git init` tree under `%TEMP%/d23*` with
`core.autocrlf false`, committed after each step; a scratch gov is built as `build_gov13` builds it,
from the engine the line names. A red half "over `bf42c5113`" ran the engine of a local
`git clone` of gov under `%TEMP%`, checked out at `bf42c5113`. A red half stated as a scratch copy
of the tip ran a copy with the one named edit, built by a probe script that asserted the edit
matched exactly once. The green probes of AC1, AC2, AC3 and AC6 ran before the last edit to
`<p23>`'s engine, which split `run_target_argv`'s signature over two lines to annotate `argv` and
moves no behaviour; AC4 was re-run after it, and its line numbers are the committed ones. The red
halves the section 7 `New arm:` lines state are owed to the close.

**Evidences:** TOOL-dRedressedBar-23
- AC1 — `manifest-section-b` — over a `DEPLOY_FULL` target, the three-kit apply ran twice, exit 0
  both. Its one hole order, `manifest-section-b`, carried `kit` `kickoff-manifest`. With `kit`
  removed from every hole order and committed, `apply --kits settings-merge` exited 0, and its
  receipt's orders read the `gate-legs` order, then the keyless `manifest-section-b` hole order,
  then one `machine` order of `kickoff-manifest`. The last two equal the stripped receipt's orders
  of the carried kits, as JSON and in order. `check` printed one line opening
  `govkit check — kickoff-manifest: undischargeable`. The order file's instruction half carried
  `- settings-merge selftest: ` and `- kickoff-manifest ratchet: `, and it had no WITHHELD half.
  Red over `bf42c5113`: the fresh three-kit apply's hole order carried no `kit`, the narrower
  receipt held the `gate-legs` order alone, so no order with `kit` `kickoff-manifest` and none with
  id `manifest-section-b`. `check` printed no `undischargeable` line, and the order listed
  `settings-merge selftest` alone. Red over a copy of the tip keying the carry on `kit` alone: the
  narrower receipt kept the `machine` order and lost `manifest-section-b`.
- AC2 — `demo2/absent.sh` — over a scratch gov from the tip's `govkit.py` and a
  `M13_DEPLOY_NONE` target, `apply` then `apply --kits demo` each exited 0, the receipt still
  claimed `demo2`, and the order's instruction half read `- demo leg: ` and
  `- demo2 leg: bash scripts/demo2/engine.sh`. With demo2's leg engine rewritten to
  `demo2/absent.sh` and committed, `apply --kits demo` exited 0. Its instruction half carried no
  `demo2 leg`, its WITHHELD half carried `- demo2 leg: bash scripts/demo2/absent.sh` with the
  `WITHHELD — names scripts/demo2/absent.sh` line, and no output line carried
  `declares gate leg 'demo2 leg'`. Red over a gov from `bf42c5113`'s `govkit.py`: after the first
  narrower apply the order carried no `demo2 leg` anywhere. Red over a copy of the tip whose
  non-manifest loop skips the `_silenced` test for a carried kit: the third apply listed
  `- demo2 leg: bash scripts/demo2/absent.sh` in the instruction half and nothing under WITHHELD.
- AC3 — `It printed nothing to stderr` — the tip's `govkit.run_target_argv` over a program writing
  `4a f6 72 67 0a` to `sys.stderr.buffer` and exiting 2 returned `returncode` 2 and `stderr`
  `J`, U+FFFD, `rg` and a newline. `inspect.getsource` of `_cmd_apply` carries
  `run_target_argv(` once and of `_cmd_update` twice. Over the gained case, `update --write` exited
  1 and printed exactly one line opening
  `govkit: kit 'demo3': its adopter exited 2 on the update that gained it`, ending
  `Its stderr ended: J` with U+FFFD and `rg`, with no `It printed nothing to stderr`, and no output
  line carried `UnicodeDecodeError`. Red over `bf42c5113`, on Windows: the engine has no
  `run_target_argv`, and the gained loop's keywords read `stderr` None while the reader thread
  raised `UnicodeDecodeError`. The gained case printed one problem line ending
  `It printed nothing to stderr`, none carrying `Its stderr ended: J`, and the thread's traceback
  reached the run's output. The POSIX form, a `UnicodeDecodeError` raised out of the run, was not
  observed on this host.
- AC4 — `errors="replace"` — an `ast` walk of the tip's `tools/govkit/govkit.py` selected four
  `subprocess.run` calls with a `resolve_shell_argv(...)` first argument and an `encoding` keyword,
  at `:1226`, `:5228`, `:6318` and `:13570`. Every one passes `errors="replace"`, and `:1226` sits
  inside `run_target_argv`. Exactly three call nodes call `run_target_argv`, at `:8085`, `:11359`
  and `:11493`. Red over `bf42c5113`: the same walk selected six, at `:5194`, `:6284`, `:8038`,
  `:11309`, `:11445` and `:13523`, named exactly one lacking `errors="replace"`, `:11445`, and
  found no `run_target_argv`.
- AC5 — `{prefix}/codebase-map/kit.toml` — the `govkit selftest` leg's `guard` in
  `tools/gate-legs.json` holds `{prefix}/codebase-map/kit.toml`, after its three paths, and one leg
  carries that string, under `BROAD_LEG_FLOOR` 5. `check_guard_trips`, loaded from
  `tools/check-spec-tokens.py` with `importlib`, is true for `tools/codebase-map/kit.toml` against
  that entry with `{prefix}` read as `tools`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names `baca8fe05`, at which `tools/gate-legs.json` holds the
  path, and `<p23m>`'s body carries one `manifest-audit:` line. Red over `bf42c5113`: no entry of
  that guard trips `tools/codebase-map/kit.toml`.
- AC6 — `rcpt_file` — the tip's `read_bar_writes21`, extracted with `ast` and executed in a
  namespace binding `_ast` and `_re` alone, returned routed lines for each member of
  `govkit.ADOPTER_BAR_PATHS` alone over the tip's `govkit.py`: one for `gr["file"]`, seven for
  `receipt_path`, five for `"install.sums"`. Over a copy in which every whole-word `receipt_path`
  reads `rcpt_file`, it returned none for `receipt_path` alone, and the union returned six routed
  lines and no direct write. The selftest loops one check per member, whose label and detail carry
  the member. Red over `bf42c5113`: its `read_bar_writes21`, executed in a namespace whose
  `GOVKIT` names that copy and whose `govkit_module()` returns the constant, left `_dest21` as
  `rf` and `sums_path`, `_routed21` with six lines and `_direct21` empty, so all three `[-21] AC2`
  checks pass while the receipt member grades nothing.
- AC7 — `memory/map/generated/symbols.json` — holds an entry with id `run_target_argv`, kind
  `function` and file `tools/govkit/govkit.py`, and
  `python tools/lexicon/lexicon.py --suggest run_target_argv --as py.function` printed a line
  opening `OK`. Red: `<w23>`'s symbol index holds no such entry.
- AC8 — `hands-off` — over `<w23>`, specs 12, 14, 15, 16 and 17 each took one header rev change,
  rev-8 to rev-9, rev-7 to rev-8, rev-6 to rev-7, rev-4 to rev-5 and rev-5 to rev-6, each CLOSED on
  both sides, and one new revision line naming `TOOL-dRedressedBar-23` and its report id: 4, 4, 5,
  4 and 13. Each one's Edges carries a `hands-off` bullet naming `TOOL-dRedressedBar-23`.
  `git diff --name-only` over `<p23>` under `memory/builds/dRedressedBar/spec/` names this spec
  alone, for its dispatched header, and over `<p23m>` names nothing. This ledger carries
  `**Serves:** journal TOOL-dRedressedBar-23`.

## Owed to the close

The section 7 gates, run once by the main loop as the bar: `govkit selftest`,
`govkit acceptance matrix`, `govkit refusal join`, `govkit selfcheck`, `receipt sync`,
`run-gates canary`, `run-gates gov canary`, `kickoff-manifest ratchet`,
`codebase-map coverage + freshness`, `lexicon naming predicates`, `encoding posture`,
`spec tokens`, `recall floor`, `recall floor arms` and `memory hygiene`. The encoding posture rows
for `tools/govkit/govkit.py` and `tools/govkit/selftest.py` were not measured here; every new text
read, write and process call names `encoding="utf-8"`, so spec 23 §4 expects neither to move. And
the RED-first observation of the five `New arm:` lines: the `[dRB-12]` order checks (AC1), the
`[dRB-23]` no-runner case (AC2), the `[dRB-23]` gained case (AC3), the `[dRB-23]` static checks
(AC4) and the per-member `[-21] AC2` checks (AC6). The selftest gains three scratch govs, one
extra commit and six engine runs, a cost unmeasured until that run.
