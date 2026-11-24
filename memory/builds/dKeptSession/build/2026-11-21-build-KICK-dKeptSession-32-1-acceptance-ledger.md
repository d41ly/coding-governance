# KICK-dKeptSession-32 — acceptance ledger

**Serves:** journal KICK-dKeptSession-32

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass. The criteria were observed on win32 at the pass's base `7df6a1da` by probes of the unit's own
code: `run_scaffold_preset`, `run_arms_empty_target`, `run_mirror_absent_adopter`, `run_mirror_landed`
and `run_fresh_target` called from a `python -c` script in `tools/policy/`, with `GOV_REMOTE`,
`GOV_DEFAULT_BRANCH` and the `GIT_*` location variables unset; `policy.py scaffold` run as a CLI, in
the kit and over a scratch kit copy under the session scratchpad; and `grep`. The two new names,
`run_scaffold_preset` and its nested `check_preset_scaffold`, are `run_` and `check_` verbs:
`lexicon.py --suggest` answered OK for each as `py.function`, and `lexicon.py` exited 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` runs of the
`scaffold-preset`, `arms-empty-target`, `adopter-fresh-target` and `mirror-landed-merge` cases among
them; AC6's `git diff --name-only` over the pass's range; and the RED-first observation of the
`New arm:` line, the `scaffold-preset` case of `tools/policy/check_policy.py`, on its staged break,
the checkout's `render_scaffold` writing every literal row under a preset, and green once restored.

## Unit 4's superseded wording (S4)

Unit 4 is CLOSED, so its spec and its ledger are not written; its two passages are answered here.

- Unit 4 S2 said `render_scaffold` writes `preset = "<name>"` as the first key, "the line after
  `SCAFFOLD_HEADER` and above dGroundRules' tables". Superseded by name: the tables below that line
  hold only the rows S1 writes, a row the named preset assigns standing in its table as the comment
  `# <key> = <value> (preset <name>)`.
- Unit 4 AC3 said that once the install is committed "the line after the target's header comment is
  `preset = "strict"`". Answered with AC1's output below: under strict that line is still
  `preset = "strict"`, and the `[budgets]` table under it opens with the comment
  `# enforce = "refuse" (preset strict)`.

**Evidences:** KICK-dKeptSession-32
- AC1 — `policy.py scaffold --preset strict` printed the header, `preset = "strict"`, then `[budgets]` holding `# enforce = "refuse" (preset strict)` and `pinned = []`, `[policy-file]` and `[runtime]`, the file section 4 of the spec shows, byte for byte.
  Committed as the policy file of a `build_reader_repo` repository on `main`, `policy.py get
  budgets.enforce --explain` exited 0 printing `refuse` on stdout and `policy: budgets.enforce ·
  preset · preset strict at <sha8>, local main: this clone has no remote` on stderr.
- AC2 — `run_scaffold_preset("scaffold-preset")` returned 12 assertions, 0 wrong, in 63.6 seconds (DERIVED, that probe): per preset `velocity`, `standard`, `strict` and `guarded`, the scaffold exited 0 with nothing on stderr, `get <key> --explain` read each of the preset's 246 assigned keys from the preset (DERIVED, that probe's lines), and `preset --diff` printed `- preset — <name>` and `- no key differs`.
  Under `velocity`, `standard` and `guarded` the scaffold writes `# enforce = "warn" (preset
  <name>)`, since each assigns `budgets.enforce`; no preset assigns `budgets.pinned`,
  `policy-file.on-invalid` or `runtime.agents-in-flight`, each a `never` key, so all three stay
  literal rows.
- AC3 — a `python -c` probe calling `render_scaffold(rows)` raised `TypeError: render_scaffold() missing 1 required positional argument: 'preset'`.
  `render_scaffold(rows, None)` equalled the base's `render_scaffold(rows)` byte for byte, the base
  module read from `git show HEAD` and run in process. Over a scratch kit copy holding no
  `presets.py`, `policy.py scaffold --preset strict` exited 2 with nothing on stdout and the line
  `policy: refused · … · presets.py, the named presets' module, does not import beside …` on stderr;
  with `presets.py` copied and a store that does not parse, it exited 2 with nothing on stdout and
  the store's `does not parse` refusal on stderr.
- AC4 — `run_arms_empty_target` returned 4 assertions, 0 wrong (DERIVED, that probe), its scaffolded target graded at 4 keys; `run_fresh_target("adopter-fresh-target")` returned 168 assertions, 0 wrong, in 29.8 seconds (DERIVED, that probe); `run_mirror_landed("mirror-landed-merge")` returned 5 assertions, 0 wrong (DERIVED, that probe), its helper reading `refuse` from the file at L.
  `git grep -n "render_scaffold(" -- tools/policy/check_policy.py` at the repository root printed 5
  lines, one per call (DERIVED, that grep): the four S5 calls each pass `None` on their own line,
  and `run_fresh_target`'s line ends in the comma after its first argument, its `preset=preset` on
  the next. `run_mirror_absent_adopter` returned 4 assertions, 0 wrong (DERIVED, that probe). The
  scaffold's key count is 4 with no preset, under `standard` and under `strict` (DERIVED, a
  `python -c` count of `scan_keys` over each render).
- AC5 — `grep -n "as a comment" README.md` in the policy kit printed one line, the `policy.py scaffold` entry's, saying a row the named preset assigns is written as a comment naming the preset's value.
- AC6 — this ledger holds each of unit 4's two passages once, quoted under S4 above; the pass's staged paths name neither unit 4's spec nor its acceptance ledger, and the `git diff --name-only` over the pass's range is owed to the close.
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `scaffold-preset`: `render_scaffold` writes every literal row under a preset
