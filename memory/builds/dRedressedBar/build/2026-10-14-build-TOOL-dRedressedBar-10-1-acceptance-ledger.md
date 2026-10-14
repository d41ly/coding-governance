# TOOL-dRedressedBar-10 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-10

The build pass of the round-1 spec audit's minors batch. It moved two product files: the second
`must_not_exist` term in `tools/govkit/entries/settings-merge.kit.toml`, and the parent-home row of
settings-merge's `check_outcome_states` call in `tools/govkit/matrix.py`. It also wrote this ledger
and spec 10's status cell. The sibling corrections are the spec-writer pass `<s10>`, `67a23b14d`.
The pass commits named below come from each commit's `Pass:` trailer, because no sibling unit wrote
an acceptance ledger: `<p2>` `c7a9213d1`, `<p8>` `a50d04eb7` and `<p9>` `59f11096a`.

No merge bar, no self-test suite and no gate leg ran in this pass. Each criterion was observed
through a direct probe. The greps and `git` readings ran over the tip. Three python programs
imported the code under test: `govkit.classify_outcome` for AC16, `matrix.check_outcome_probes`
with a recorder for AC7 and the new row, and `sh_hygiene.scan_spawn_file` for AC5 and AC12. AC17
drove both verbs over fresh `git init` targets under `%TEMP%`, from a scratch gov clone at
`%TEMP%/u10g`. The clone's HEAD carried unit 9's single-term block for the red half. The same clone,
with this pass's product diff committed, gave the green half. These probes stand in for
`govkit acceptance matrix` (the row), `govkit selftest` (the `[dRB-9]` arm's descriptor) and
`memory hygiene` (the specs and this ledger). The §7 gates themselves are owed to the close, along
with the `New arm:` line's RED-first observation: the matrix leg with unit 9's single-term block
staged, where the parent-home row must read ACCEPTED.

**Evidences:** TOOL-dRedressedBar-10
- AC1 — `wc -l` — over the tip, the glued pattern through `grep -o` printed 0 and the spaced
  pattern printed 14.
- AC2 — `.githooks/pre-push.test.sh` — the first executed push printed line 139 and
  `^unset GATE_SELFTESTS` printed exactly one line, 122, so the unset sits above the push. In a
  scratch copy with that line moved to the file's end, the push read 138 and the unset 2601, after
  it.
- AC3 — `FOREIGN_PREFIX_PROBE:-0` — `tools/roles/adopt-roles.test.sh` printed two lines, 88 (the
  attribution comment) and 89 (the `if` line), between `# ---- arm 1` at 82 and `# ---- arm 2` at
  91. The `:-0` grep printed line 89 alone, which reads `${fail:-0}` and `${n:-1}`, and a lowercase
  `pass` grep over it counted 0.
- AC4 — `MP_BOUND` — `git diff --stat a50d04eb7~1 a50d04eb7 -- tools/` listed one file,
  `tools/run-gates/run-gates.test.sh`. In that file's diff, `MP_BOUND` appears only inside
  `run_mp_bar` (lines 3411 and 3414 at `<p8>`) and on the one `ac14` call (3645). No
  `FLOOR_ASSERTIONS` line is in the diff, and the file reads `FLOOR_ASSERTIONS=401` at `<p8>`.
- AC5 — `scan_spawn_file` — for `tools/run-gates/run-gates.test.sh` at `<p8>~1` and `<p8>`, the
  site counts read cat-file 25 and 25, date-fmt 1 and 1, path-subst 12 and 12, printf-subst 2 and 2,
  and var-pipe 141 and 141. Each equals its row in `memory/project/spawn-idiom-sites.txt`, read at
  observation. `grep -n 'reads none of this file'` over spec 8 printed nothing, and its Gates cut
  printed `scan_spawn_tree` in the corrected sentence, at its line 12.
- AC6 — `kickoff-manifest` — the aQuenchedHarness-3 cut is 41 lines. Its grep printed the
  `kits = ["agent-cap", "settings-merge", "kickoff-manifest"]` line, the
  `"--kits", "agent-cap,settings-merge,kickoff-manifest"` line, and one comment line.
  `manifest_path` and `user_skills` each printed one line.
- AC7 — `check_outcome_probes` — `[dRB-9]` hit lines 3345 to 3351, one block after the `u2a`
  re-stamp arms (`stale_target("u2a")` at 3303). The block reads `means` from the settings-merge
  descriptor at 3342 and 3343. `def check_outcome_states` hit once and `check_outcome_states(` three
  times. With `check` replaced by a recorder, `check_outcome_probes` recorded exactly two `lexicon `
  labels, equal to §4's pins: `lexicon exit 1 after a failed first scaffold is REFUSED` and
  `lexicon exit 1 after a declaration removed after one is ACCEPTED`. All 16 recorded checks passed.
  These include the new `settings-merge exit 2 after an install with the hook at its prefix's
  parent home only is REFUSED`.
- AC8 — `project-owned` — `grep -n 'roles kit'` over spec 4 printed nothing. `project-owned`
  printed the corrected non-goal at line 46 and the hands-off at line 60, both citing
  `tools/roles/kit.toml:47-48`. The hands-off to `TOOL-dRedressedBar-7` at line 54 names the
  `agent-cap` kit alone. The base sentence `from the roles kit (tools/roles/kit.toml:47)` is absent.
- AC9 — `consumes-from` — `grep -nE 'units 1 to 6|six units'` over spec 7 printed nothing. Its
  Edges hold the `TOOL-dRedressedBar-8` line, citing `tools/run-gates/kit.toml:40-41`, and the
  `TOOL-dRedressedBar-9` line, citing `tools/govkit/registry.toml:295-297`. Spec 8 at line 66 and
  spec 9 at line 92 each open ``- **hands-off** `TOOL-dRedressedBar-7` ``.
- AC10 — `--kits` — over the tip, the guard printed nine lines (3304 to 3327, 6927, 6941, 7105,
  7115 and 7129), and none carries `--kits`. A scratch copy had `"--kits", "check-wiring", `
  inserted in the `str(up)` writing call at 3315. There, the guard printed that line carrying
  `--kits`, and unit 3's AC5 regex dropped from 6 hits to 5, printing nothing for it.
- AC11 — `by content` — spec 5's Design cut printed its line 37, naming unit 1's probe stop and
  unit 4's `WORKFLOW_RUNS_DIR` lines as the two insertions. Spec 6's printed its §4 sentence at its
  line 6.
- AC12 — `scan_spawn_file` — at the tip, var-pipe, path-subst and date-fmt read 0 for
  `tools/branch-reconcile/adopt-branch-reconcile.sh`, `tools/roles/adopt-roles.sh`,
  `tools/roles/adopt-roles.test.sh` and `tools/hooks/format-guard.test.sh`. For
  `tools/workflows/unattended-build.test.sh`, var-pipe read 62 and printf-subst 66, equal to its
  rows.
- AC13 — `always arrive together` — the grep over spec 3 printed nothing.
  `The defect, and where it sits` printed the pointer to unit 9 at line 158.
- AC14 — `symbols.json` — spec 2's Scope cut printed S4's by-name Readers line and S5's line. Spec
  9's cut printed S7's line. Both specs' §7 leg lines name `codebase-map coverage + freshness`.
  Over the tip, `memory/map/generated/symbols.json` lists `renderAskQuote` and
  `check_outcome_states`, and holds no `clean` entry at all. `git show --name-only --format=` over
  `c7a9213d1` and over `59f11096a` each list `memory/map/generated/symbols.json`.
- AC15 — `must_not_exist` — `grep -n -A5 '^\[\[outcome\]\]'` over the descriptor printed one block:
  `code = 2`, `must_exist = "{prefix}/settings-merge.py"`, the two-term `must_not_exist` §4 gives,
  `means = "no-agent-cap-to-wire"` and `ok = true`.
- AC16 — `classify_outcome` — through `read_descriptors`, `outcome_accepted` and
  `declares_outcome_for`, settings-merge's exit 2 over four scratch directories, each holding
  `tools/settings-merge.py`, read as follows. No hook: ACCEPTED. Hook at `tools/hooks/agent-cap.js`:
  REFUSED. Hook at the parent home `hooks/agent-cap.js` only: REFUSED. Hook at a third path
  `vendor/hooks/agent-cap.js` only: ACCEPTED. With unit 9's single-term block substituted in the
  descriptor, the parent-home row read ACCEPTED. That is the red case, and the other three rows
  were unchanged.
- AC17 — `adopter exit 2` — with the two-term block, the second
  `apply --target <t> --kits settings-merge` over the plant exited 1. It printed
  `CONFIGURE settings-merge: adopter exit 2` and `1 problem(s)`, and no `no-agent-cap-to-wire`.
  `update --write --to <HEAD>` over unit 9's AC2 program with the same plant exited 1. It printed
  `no declared outcome accepts that`, and `gov_commit` stayed `24f39915`. The red half ran first,
  over unit 9's single-term block. Apply exited 0 with
  `adopter exit 2 — no-agent-cap-to-wire [accepted stop]`. Update exited 0, re-stamped
  `gov_commit` to the `--to` commit, and printed the fragment's
  `REFUSED by settings-merge (exit 2)` parse-failure line first, as §4 states.
- AC18 — `reachable only by` — the grep over spec 9 printed nothing. Its §4 "What it does not
  check" table names the three routes, and its §5 security line names the receipt-homed residual
  as open and `TOOL-dRedressedBar-11` as its closer.
- AC19 — `TOOL-dRedressedBar-10` — `git diff 67a23b14d~1 67a23b14d` over the spec folder shows
  one header change and one new revision line each in specs 1 and 3 to 9. The revs match §4's
  table: rev-3, rev-4, rev-3, rev-6, rev-3, rev-5, rev-3 and rev-5. Each line names
  `TOOL-dRedressedBar-10` and every report id §4 assigns its spec, and spec 2 shows no change. This
  pass's staged spec-folder set, the diff its commit records, names spec 10 alone. This ledger
  carries `**Serves:** journal TOOL-dRedressedBar-10`.

## Finding for the close

Spec 10 §5 "observability" says a refused stop prints `no declared outcome accepts that` and
`adopter exit 2`. That holds for `update`. On `apply`, the refusal line reads `its adopter exited 2
— unclassified, because no [[outcome]] evaluator exists yet to say WHICH declared outcome that code
means`, a message `tools/govkit/govkit.py` still prints though the evaluator exists. No criterion
reads that line, and govkit.py is outside this unit's write set. Unit 13, which corrects spec 10
§5, is the place for the sentence. The stale message itself is not owned by any unit yet.
