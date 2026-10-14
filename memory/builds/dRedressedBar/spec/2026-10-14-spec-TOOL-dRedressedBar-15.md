# TOOL-dRedressedBar-15 — agent-cap's adopter runs settings-merge's own adopter at settings-merge's home, declared as `[adopt] via`, and selfcheck refuses any argv naming another entry's file

**Status:** SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-15-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-15-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-15-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-15-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

agent-cap's adopter argv is `["python", "{prefix}/settings-merge.py"]` (`tools/hooks/kit.toml:108`),
a copy of settings-merge's own (`tools/govkit/entries/settings-merge.kit.toml:27`). CONFIGURE
resolves it through agent-cap's own `target_context` (`tools/govkit/govkit.py:7673`, `:7743`), which
reads `[kit.agent-cap]` (`:1452-1455`). So at `[kit.agent-cap] prefix = "scripts"` it runs
`scripts/settings-merge.py`, a file settings-merge never installed there, and python exits 2 with
"can't open file". This unit lets a descriptor say "my adopter is that entry's adopter", as
`[adopt] via = "settings-merge"`. The engine then runs the named entry's argv, resolved in that
entry's context. A selfcheck arm refuses the class: an argv an entry declares that names a file
only another entry ships. With unit 14's early receipt, the brief's reproduction then exits 0.

## 2. Scope (IN)

- **S1** — One module-level function in `tools/govkit/govkit.py`, placed after `target_context`
  (`:1415-1477`):
  `resolve_adopter_argv(target: pathlib.Path, deploy: dict, eid: str, descs: dict[str, tuple[dict, str]]) -> list[str]`.
  It reads `eid`'s `[adopt] via`. When that is a non-empty string it is the source entry, else `eid`
  is. It returns the source entry's `[adopt].argv`, each element passed through `resolve_tokens`
  with `target_context(target, deploy, <source>, descs[<source>][0])`, keeping element `[0]` as both
  spawn sites do today. An entry with no argv returns `[]`. Its docstring states the `via` grammar,
  the four rules S5 enforces, and that the configured entry's own descriptor still classifies the
  exit. It validates nothing: selfcheck (S5) is the one validator of a gov-authored descriptor.
  Observed by AC5 and AC9.
- **S2** — `_cmd_apply`'s CONFIGURE loop replaces the lines binding `argv`, testing it and binding
  `resolved` (`:7740-7743`) with `resolved = resolve_adopter_argv(target, deploy, eid, descs)` and
  `if not resolved: continue`. The spawn, `classify_outcome(target, d, ctx, rc)`, the
  printed line and every branch below it keep the configured entry's own `d` and `ctx`. The inert,
  hole and resume checks above it are unchanged. Observed by AC1, AC2, AC3 and AC4.
- **S3** — `_cmd_update`'s gained loop (`:11104-11126`) takes `_res_g` from
  `tuple(resolve_adopter_argv(target, deploy, _ge, descs))`. The skip test reads `_res_g` where it
  read `_argv_g`, and `_argv_g` is no longer bound. `_ctx_g` stays `target_context(target, deploy,
  _ge, _d_g)` and still feeds `classify_outcome`. The same-argv dedup on `_ran_gained` is unchanged.
  Observed by AC5 and AC9.
- **S4** — `tools/hooks/kit.toml`'s `[adopt]` table becomes exactly one key, `via = "settings-merge"`.
  agent-cap's own `argv`, `mutates_index` and `why_no_regenerate` are deleted, because each now
  belongs to the adopter settings-merge declares with the same values. The comment above the table
  keeps its RESTORED paragraph and gains one saying why: the `Workflow|Agent` wiring is
  settings-merge.py's default action, its file is settings-merge's, and `via` runs it at
  settings-merge's home, where the per-kit-prefix case used to miss it. Observed by AC1, AC6 and AC9.
  **Readers:**
  by name: `tools/govkit/govkit.py` spells an `[adopt]` table's `argv` at `:1868`, `:2606`,
  `:3265`, `:3700`, `:7315`, `:7740`, `:11107` and `:12736`, `mutates_index` at `:2603`, and
  `why_no_regenerate` at `:1874`. `tools/check-kit-placeholders.py:133-139` and
  `tools/playbook/render_playbook.py:801` spell `argv`. S2 and S3 rewrite the two spawn sites, and
  §3 says why the rest keep reading the declared argv.
  by value: the 3b-iii note at `:1882` counts one adopter fewer. The update dedup at `:11112`
  compares resolved argvs, and agent-cap's now equals settings-merge's at every prefix. Intake's
  token walk at `:12736` loses agent-cap's `{prefix}`, which is derived and never asked.
- **S5** — One arm in `selfcheck`, inside the bare-target block, after the reserved-prefix note
  (`:3217-3221`). It reuses `_bare_t`, `_bare_deploy`, `_bare_sel` and `_bare_rows`, and binds only
  names prefixed `_xa_` (`grep -c _xa_` reads 0 today). It has two parts, specified in §4 "The class
  gate": the `via` rules, and the ownership join over four argv kinds. It has three `r.fail` sites
  and one `r.note`. Observed by AC6 and AC7.
- **S6** — `[dRB-15]` checks in `tools/govkit/selftest.py`, in two places. The first reads the
  apply that unit 14's `[dRB-14]` block runs, and asserts AC1's exit and line facts on the lines
  they name. The second sits after the scratch-gov liveness arms that use `build_scratch_gov_kit`
  (`:5508-5604`). It builds AC7's scratch govs and asserts each on the arm's own lines. Every file
  write names `encoding="utf-8"`, and every process call goes through an existing helper. Observed
  by AC1 and AC7, through the two `New arm:` lines in §7.
- **S7** — The hooks kit's version moves by one, minted, never typed. After S1 to S6 and S8 are
  committed, `python tools/govkit/govkit.py mint --base ebce889c7` runs, and its writes are
  committed as a second commit carrying the unit id. If the mint names any entry other than
  agent-cap as minted, the pass stops before committing and returns to the main loop. Observed by AC8.
- **S8** — S1 adds a function, so `python tools/run-gates/regen.py --write` runs before the product
  commit, and that commit carries what it rewrites under `memory/map/generated/`. Observed by AC9.
- **S9** — Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-15`.
  Observed by AC10.

## 3. Non-goals (OUT)

- No change to the token grammar. `TOKEN_RX` (`tools/govkit/govkit.py:1132`) gains no
  `{prefix:<entry>}` form, and `SEEDED_TOKENS` (`:1376`) gains no key (§4, alternatives).
- No change to `tools/settings-merge.py`, to settings-merge's descriptor, or to any copy of
  `resolve_kit_dir`.
- No edit to unit 14's receipt write (brief non-goal), and no change to which kits the registry's
  default set holds (brief non-goal).
- No change to which descriptor classifies agent-cap's exit. Spec 9 §4 "Why the shared argv stays
  safe" rests on agent-cap's refusal being read under agent-cap's descriptor, in both verbs.
- No dedup in `apply`'s CONFIGURE. A default-prefix apply still runs the one script twice and
  prints both lines, as AC2 pins.
- No rewording of any CONFIGURE line. An operator still reads `CONFIGURE agent-cap: adopter exit N`.
- No change to the other readers of `[adopt].argv`. Arms 3b-iii, 7d and 7j, `check_entry_producer`,
  the merged-rule guard at `:7315`, intake's token walk and the two shipped readers each grade the
  script a descriptor declares, and the delegate's script is graded on its own entry. agent-cap
  ships no `rendered`, `generated` or `merged` rule, so `check_entry_producer`'s and `:7315`'s answer
  for it does not move.
- No grading of `[[hole]]` discharge commands or `[[outcome]]` probe paths by the S5 arm (§4).
- No raise of the refusal join's `BRANCH_PIN`. It is a floor, the leg runs enumeration-only
  (`tools/govkit/refusal_join.py:244-256`), and re-baselining it is not this unit's.
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers a descriptor key.

### Edges

- **consumes-from** `TOOL-dRedressedBar-14` — the receipt written ahead of CONFIGURE, after which
  settings-merge's adopter exits 0 at a per-kit agent-cap prefix, so the reproduction's only exit 2
  is agent-cap's. AC1's exit 0 rests on it, and S6's first half reads the apply its `[dRB-14]` block
  runs. Without it settings-merge still exits 2 and AC1 cannot pass.
- **consumes-from** `TOOL-dRedressedBar-11` — S3's stderr tail on a refused CONFIGURE exit, which
  AC1's red half reads for python's "can't open file". Without it the red half shows only an exit code.
- **hands-off** external — `TOOL-aScouredKit-26`, the open ask for a cross-entry destination token,
  stays open. `via` names a whole adopter and passes no sibling's destination into an argv, so
  drift-audit's `DRIFT_WORKFLOWS_REL` workaround is untouched.

## 4. Design

### The defect, measured

The first row is unit 14's, read at `29c72f51`. The rest were read on 2026-10-14 at `95350ba5`.
Both trees' `tools/` equal `ebce889c`'s (`git diff --stat ebce889c7 HEAD -- tools skills` prints
nothing). Targets are fresh `git init` trees under `%TEMP%` holding `DEPLOY_FULL`'s answers
(`tools/govkit/selftest.py:700-710`).

| Reading | Result |
|---|---|
| Unit 14 §4, steps 4 and 5, on `%TEMP%/drb14` with `[kit.agent-cap] prefix = "scripts"` | agent-cap's resolved argv `python scripts/settings-merge.py` exits 2, `can't open file`, with a receipt on disk |
| `%TEMP%/drb15s`, `[kit.settings-merge] prefix = "scripts"`, `apply --kits agent-cap,settings-merge,kickoff-manifest` | exit 1. `CONFIGURE settings-merge: adopter exit 2` and `CONFIGURE agent-cap: adopter exit 2`. settings-merge.py landed at `scripts/` only |
| The same target, receipt on disk, `python scripts/settings-merge.py` | exit 0, `wired agent-cap Workflow\|Agent hook` |
| The same target, `python tools/settings-merge.py`, agent-cap's resolved argv | exit 2, `can't open file '…\\tools\\settings-merge.py'` |
| `%TEMP%/drb15b`: `apply --kits settings-merge`, commit, then `apply --kits agent-cap,kickoff-manifest` | the second apply exits 0 with one CONFIGURE line, `CONFIGURE agent-cap: adopter exit 0`. `.claude/settings.json` gains `node "${CLAUDE_PROJECT_DIR}/tools/hooks/agent-cap.js"`, which the committed tree lacked |

So the class has two faces. A per-kit prefix on the entry that declares the argv moves the path it
names. A per-kit prefix on the entry that ships the file moves the file. The last row is the
behaviour any fix must keep: agent-cap's adopter is the only step that wires the hook when
settings-merge is claimed but not selected. CONFIGURE iterates the selection alone (`:7671`), and
`run_fragment_merges` wires only `.fragment.json` rows (`:5869-5871`). The `Workflow|Agent` entry
is no fragment (`:11100-11103`).

### The delegate key

```toml
[adopt]
via = "settings-merge"
```

`via` names the registry entry whose adopter this entry runs. That entry's `[adopt].argv` is
resolved in that entry's context, so `{prefix}` and `{kit}` take its per-kit table, exactly as its
own CONFIGURE resolves them. The key is read only from gov's descriptors. A target's
`.governance/deploy.toml` cannot set it, because `[kit.<eid>]` values become ctx tokens
(`:1469-1475`), never `[adopt]` keys.

| Site | Argv run | Tokens resolved in | Exit classified by |
|---|---|---|---|
| `_cmd_apply` CONFIGURE (`:7740-7772`) | the `via` entry's `[adopt].argv`, else its own | the `via` entry's `target_context`, else its own | its own `d` and `ctx`, unchanged |
| `_cmd_update` gained loop (`:11104-11126`) | the same | the same | the same; the dedup key stays the resolved tuple |

The inert decline, the `blocks_adopt` skip, `held` and the resume gate stay the configured entry's
own. settings-merge declares no hole, and an inert settings-merge never stopped agent-cap's adopter.

### The class gate

**The `via` rules.** For every entry in `_bare_sel` whose `[adopt]` carries `via`, one `r.fail`
site reports the first rule broken:

```
entry '<eid>' declares [adopt] via = '<v>', which <reason>
```

| Rule | `<reason>` |
|---|---|
| `<v>` is a registry entry | `names no registry entry` |
| `<v>` is in `<eid>`'s `requires` | `is not in its requires, so that entry's script may not be installed` |
| `<v>`'s own `[adopt]` carries a non-empty `argv` | `declares no [adopt] argv of its own` |
| `<eid>`'s `[adopt]` carries no non-empty `argv` | `sits beside an [adopt] argv in the same table` |

The second rule answers the question `TOOL-aScouredKit-26` leaves open for a token.
`derive_unsatisfied_requires` (`:944-967`) admits a run only when every `requires` entry is
selected or claimed, so the named script is installed whenever the configured entry is. The third rule rules out a chain, because a
`via` entry has no argv. An entry that breaks a rule is left out of the join below, so the helper
never meets an invalid `via`.

**The ownership join.** An argv kind is graded when the engine resolves it through the declaring
entry's own `target_context`. Four kinds qualify:

- `[adopt]`, through S1, with the source entry as the owner it is joined to;
- `[check]`, which `run_kit_check` runs with the entry's ctx (`:10015`);
- `[[gate_leg]]`, which `write_gate_legs` resolves per entry (`:4105-4114`);
- `[[regenerate]]`, which `update`'s re-render resolves per entry (`:10932`).

Owners are `{dest: kits}` over `_bare_rows` rows whose `missing` is empty. An element is OFFERED
when its declared text carries `/`. It is GRADED when its resolved text carries no `{` and no space.
It is a HIT when some entry ships the resolved path and the source entry does not. One `r.fail`
site per hit:

```
entry '<eid>': its <kind> argv names '<path>', a file entry '<owner>' ships and '<source>' does not. Each entry's tokens resolve from its own table, so a per-entry prefix on either moves one side and not the other. An adopter that runs another entry's script declares [adopt] via = "<owner>"
```

`<kind>` is `[adopt]`, `[check]`, `gate leg '<name>'` or `[[regenerate]]`. `<owner>` joins several
owners with `, `. The note, printed always:

```
cross-entry argv: <o> slash-bearing element(s) offered by [adopt], [check], [[gate_leg]] and [[regenerate]] across <m> entries, <g> graded, <h> naming a file only another entry ships
```

The third `r.fail` site is the liveness red. It fires when `<o>` is above zero and `<g>` is zero,
reading `cross-entry argv: <o> element(s) offered and none graded — every one carried an
unresolved token or a space, so the predicate read nothing`. With nothing offered it stays silent,
as arm 7j4 stands its zero-population reds down.

**Measured over the real registry first.** A scratch probe ran the join through `read_descriptors`,
`planned_writes` and `target_context` at a bare target, at `95350ba5`. It graded 29 of 29 entries
and 105 offered elements: 15 `[adopt]`, 11 `[check]`, 67 `[[gate_leg]]` and 12 `[[regenerate]]`.
All 105 graded, and exactly one hit: agent-cap's `[adopt]` `{prefix}/settings-merge.py` resolving
to `tools/settings-merge.py`, owned by `settings-merge`. It found no element naming a path no entry
ships. These figures are PINNED to that run. After S4, agent-cap's `[adopt]` element is
settings-merge's argv resolved in settings-merge's context, so the offered count holds and the hit
count falls to 0. AC6 derives both at observation.

**What it does not check.**

- An element with no `/`, such as a repo-root file. This is the same gap `silenced_legs` pins
  (`:3919-3924`).
- A space-bearing element or one with an unresolved token. Each is offered and counted, not graded.
- `[[hole]]` discharge commands. Most are `bash -c` or `python -c` strings, which carry a space.
- `[[outcome]]` probe paths. settings-merge's code-2 block names `{prefix}/hooks/agent-cap.js` by
  design (spec 9 §4), and units 10 and 11 bound that probe through the receipt.
- A path no entry ships, which `silenced_legs` already grades for gate legs.
- Whether the delegate's adopter succeeds.
- A real per-entry prefix. The bare target has one prefix, so the class shows as ownership, not as
  a missing file.

### What an adopter sees change

| Situation | At `<p14>` | After |
|---|---|---|
| `apply --kits agent-cap,settings-merge,kickoff-manifest`, `[kit.agent-cap] prefix = "scripts"` | exit 1. settings-merge `adopter exit 0`, agent-cap `adopter exit 2`, its problem line ending in python's `can't open file '…scripts\\settings-merge.py'` | exit 0, both `adopter exit 0`, no problem line |
| the same, `[kit.settings-merge] prefix = "scripts"` | exit 1, agent-cap `adopter exit 2` opening `tools\\settings-merge.py`. Derived from §4's rows 2 to 4 and unit 14 | exit 0 |
| the same at the default prefix | exit 0, both `adopter exit 0` | unchanged: both resolve to `python tools/settings-merge.py`, as today |
| `apply --kits agent-cap,kickoff-manifest` over a target claiming settings-merge | agent-cap's adopter wires the hook (§4, last row) | unchanged: the delegate runs though settings-merge is not selected |
| `update --write` gaining both, `[kit.agent-cap] prefix = "scripts"` | two different resolved argvs. Both run, and agent-cap's cannot open its file | one resolved argv, run once and classified by agent-cap's descriptor, as at the default prefix. Derived, not run |
| any `update` after this lands | — | the shipped `{prefix}/hooks/kit.toml` and the three version carriers move, one version up. No installed adopter re-runs (`:11100-11103`) |

### Versions and order

The hooks kit is the `agent-cap` entry (`tools/govkit/registry.toml:131-132`). Its shipped bytes
include `{prefix}/hooks/kit.toml` (`tools/hooks/kit.toml:38-41`), so S4 moves its epoch. Unit 7
mints every kit over `ebce889c7..HEAD` before units 10 to 14, which touch only govkit-exempt files.
So `derive_epoch_state` (`tools/govkit/govkit.py:12976-13031`) over the same base reads agent-cap as
`moved`, with the last bump preceding S4's commit, and `cmd_mint` (`:13110-13208`) adds one to the
last component of `KIT_AGENT_CAP_VERSION` (`tools/hooks/agent-cap.js:104`).
`write_version_carriers` then moves the `gov:kit agent-cap@` markers at `tools/hooks/format-guard.js:7`
and `tools/hooks/scratch-guard.js:144`. agent-cap declares no `[[regenerate]]`, so no render runs.
The mint reads committed movers, so it runs after the product commit and lands as its own.

This unit follows unit 14 (order 10), so its order is 11. Units 13 and 14 rewrite the CONFIGURE
call and the lines above it. That is a sequence and not an edge, because no criterion here rests
on unit 13's work. Unit 7 is a sequence too: S7's stop rule covers a mint that finds another kit
owed, and AC8 reads only agent-cap.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `resolve_adopter_argv` | a module-level function | `py.function`. `lexicon.py --suggest resolve_adopter_argv --as py.function` prints `OK — resolve_adopter_argv leads with resolve` |
| `via` | an `[adopt]` descriptor key | none: no cell grades a TOML key, and no descriptor spells `via` today |
| `_xa_` | the prefix of the S5 arm's locals | none |
| `cross-entry argv:` | the S5 note's and liveness line's opener | none |
| `[dRB-15]` | the check-label prefix of S6's checks | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/hooks/kit.toml`
- `tools/hooks/agent-cap.js`
- `tools/hooks/format-guard.js`
- `tools/hooks/scratch-guard.js`
- `memory/map/generated/`
- `memory/builds/dRedressedBar/build/`

### Alternatives rejected

Each candidate was written down with the test that could make it lose before anything ran. The
pick is M3's: the most feature-rich survivor after its vetoes.

| Candidate | The test that could make it lose | Result | Verdict |
|---|---|---|---|
| C1 — a `{prefix:<entry>}` token | a reader of the grammar that does not know the form; a resolver that holds one entry's ctx | `resolve_tokens('{prefix:settings-merge}/settings-merge.py', {'prefix': 'scripts'})` returns the string unchanged with no missing token, because `TOKEN_RX` admits `[a-z_]+` only (`:1132`). The grammar is spelled three times (`:1132`, `tools/playbook/render_playbook.py:129`, `tools/govkit/selftest.py:7433`), and every `target_context` caller holds one entry's ctx | Rejected: it moves the grammar every token reader shares, for one argv |
| C1b — a seeded per-entry key such as `{settings_merge_prefix}` | a target's `[answers]` supplying that key | `[answers]` values reach ctx through the prose class (`:1466-1468`). Only a key in `SEEDED_TOKENS` is refused (`:1441-1451`), so the set must grow with the registry or the injection that constant closes reopens | Rejected on `[security]` |
| C2 — agent-cap carries no adopter and relies on settings-merge's | a run selecting agent-cap but not settings-merge, over a target claiming settings-merge | §4's last measured row: agent-cap's adopter is the only step that wires the hook there | Rejected; AC4 stages it |
| C3 — resolve the script through the receipt at run time | `update` gaining both kits | the gained loop (`:11104-11126`) runs before `update`'s receipt write (`:12017-12062`), so a settings-merge gained in the same run is in no receipt. The argv also becomes a `python -c` string, which S5 cannot grade, carrying another resolver copy | Rejected |
| C4 — `[adopt] via`, resolved in the named entry's context | every test above | no grammar move. No target-supplied key. It runs on agent-cap's own selection and reads no receipt | Chosen |
| C5 — keep agent-cap's argv and add a context key beside it | every test above | equal to C4 on each, but the argv is then stated in two descriptors and can drift | Rejected on `[one-fact]` |
| C6 — ship a second `settings-merge.py` under agent-cap's home | selfcheck's one-claim-per-source rule (`tools/hooks/kit.toml:28-29`) | two entries claiming one source is the conflict selfcheck reports, and duplicated engine bytes are what `TOOL-dRetiredFork-14` removed | Rejected |

M3's vetoes against C4. Veto 1: none of AC1 to AC10 fails, and no non-goal is crossed. Veto 2:
`via` is no public surface. The only `[adopt]` readers outside the deployer are
`tools/check-kit-placeholders.py` (registry-exempt at `tools/govkit/registry.toml:228`) and
`render_playbook.py:801`, which reads only the playbook's own descriptor. No install location or
governance carrier moves. Veto 3: no write surface widens, because the argv run is one gov already
runs for settings-merge.

## 5. Production-readiness checklist

- security — Narrows nothing and widens nothing. `via` is read from gov's descriptors only, and a
  target cannot supply it. The delegate's ctx comes from `target_context`, which grades every
  target value it reads exactly as it does for that entry's own adopter today. C1b is rejected for
  the channel this keeps shut.
- perf / scale — N/A — one more `target_context` call per adopter, and one selfcheck loop over
  about a hundred argv elements.
- error / empty / loading states — An invalid `via` is a selfcheck finding (S5), and the bar's
  `govkit selfcheck` leg refuses it. Run over such a tree without selfcheck, the helper raises a
  `KeyError`, which is stated in its docstring. An entry with no adopter returns `[]`, as today.
- observability — The CONFIGURE line is unchanged. The S5 note prints its offered, graded and hit
  counts on every selfcheck.
- risks — A future cross-entry argv now reds selfcheck, and its message names the remedy. No arm
  pins agent-cap's `[adopt].argv` or the 3b-iii count: `git grep` finds no `CONFIGURE agent-cap`
  and no `descriptor(s) declare one` in `tools/govkit/selftest.py`. The `govkit selftest` leg grades
  the rest at the close.
- testing — AC1 to AC4 are scratch applies under `%TEMP%`, with `<p14>` clones for the red halves.
  AC5 is a python probe, AC6 and AC7 are selfcheck runs over a gov clone and scratch govs, and AC8
  and AC9 are verb and source probes. Two new arms are declared in §7.
- migration — N/A — no receipt field, conf key or deploy shape moves. An adopter's installed
  `{prefix}/hooks/kit.toml` takes the new bytes on their next `update`, and nothing at a target
  reads its `[adopt]` table.
- user docs — N/A — `help/` holds no govkit page. `WIRE-INTO-PROJECT.md:206-210`'s authoring note
  concerns `placeholders`, and the grammar's home is S1's docstring.

## 6. Acceptance criteria

`<p14>` is unit 14's build-pass commit, as its acceptance ledger names it. `<p15a>` is this unit's
product commit and `<p15>` its mint commit. Every command runs from the worktree root. A target is a
fresh `git init` tree under `%TEMP%/<short-name>`, never inside the worktree, with
`core.autocrlf false` and `.governance/deploy.toml` holding `DEPLOY_FULL`'s answers, plus the
per-kit table a criterion names. A red half at `<p14>` runs `python <clone>/tools/govkit/govkit.py`
from a local `git clone` of gov under `%TEMP%`, checked out at `<p14>`.

- **AC1** — When `python tools/govkit/govkit.py apply --target <t> --kits agent-cap,settings-merge,kickoff-manifest`
  runs at `<p15>` over a target with `[kit.agent-cap] prefix = "scripts"`, it exits 0. Exactly one
  line opens `govkit apply — CONFIGURE settings-merge:` and exactly one opens
  `govkit apply — CONFIGURE agent-cap:`, and each ends `adopter exit 0`. No line opens
  `govkit: kit '`. The receipt holds a row with path `scripts/hooks/agent-cap.js` and source
  `tools/hooks/agent-cap.js`. Read as JSON, `.claude/settings.json`'s `PreToolUse` group with
  matcher `Workflow|Agent` holds exactly one command, and it carries `scripts/hooks/agent-cap.js`.
  Red when: over the `<p14>` clone the run exits 1, the agent-cap line ends `adopter exit 2`, and
  exactly one line opens `govkit: kit 'agent-cap'` and carries both `settings-merge.py` and
  `can't open file`.
  fixture: the red half is derived from unit 14 §4 steps 4 and 5 and unit 11's S3, and the pass
  observes it first. A red half without `can't open file` is returned to the main loop.
  cost: two applies and one clone, about a minute.
- **AC2** — The same apply runs with no per-kit table, once at `<p15>` and once from the `<p14>`
  clone, each into its own target. Both exit 0. The lines carrying `CONFIGURE ` are identical
  across the two outputs, two of them ending `adopter exit 0`. The two `.claude/settings.json`
  files are byte-equal.
  Red when: the delegate changes which script a default-prefix apply runs, or what a CONFIGURE line
  prints.
- **AC3** — The same apply runs at `<p15>` over a target with `[kit.settings-merge] prefix = "scripts"`.
  It exits 0, and both CONFIGURE lines end `adopter exit 0`. `.claude/settings.json` holds one
  `tools/hooks/agent-cap.js` command.
  Red when: over the `<p14>` clone the agent-cap line ends `adopter exit 2` and its problem line
  carries `can't open file`, as §4 rows 2 to 4 measured at the base.
  fixture: the base half was observed at spec time on `%TEMP%/drb15s`. The `<p14>` half is derived.
- **AC4** — Over one target at `<p15>`: run `apply --kits settings-merge`, commit the target, then
  run `apply --kits agent-cap,kickoff-manifest`. In the second output, exactly one line opens
  `govkit apply — CONFIGURE agent-cap:` and ends `adopter exit 0`. `.claude/settings.json` holds one
  `tools/hooks/agent-cap.js` command, which the committed tree lacked.
  Red when: a scratch copy of gov at `<p15>` with the `via` line deleted from
  `tools/hooks/kit.toml`, which is candidate C2, prints no `CONFIGURE agent-cap:` line, and
  settings.json holds no `agent-cap.js` command.
  fixture: the passing half was observed at the base on `%TEMP%/drb15b` (§4, last row).
  cost: two gov trees and four applies, about three minutes.
- **AC5** — A python program run from `tools/govkit` imports `govkit` at `<p15>`. It builds a target
  whose deploy carries `[kit.agent-cap] prefix = "scripts"`, reads `read_descriptors`, and calls
  `resolve_adopter_argv` for `agent-cap` and for `settings-merge`. Both calls return
  `['python', 'tools/settings-merge.py']`. With `[kit.settings-merge] prefix = "scripts"` in place
  of that table, both return `['python', 'scripts/settings-merge.py']`.
  Red when: at `<p14>` the name is absent, and agent-cap's inline resolution,
  `[resolve_tokens(a, target_context(t, deploy, "agent-cap", d))[0] for a in argv]`, returns
  `scripts/settings-merge.py` while settings-merge's returns `tools/settings-merge.py`.
- **AC6** — `python tools/govkit/govkit.py selfcheck` at `<p15>` prints exactly one line opening
  `govkit: cross-entry argv:`, and it carries `offered by` and `0 naming`. No line opens
  `govkit: entry 'agent-cap': its`.
  Red when: a `git clone` of gov at `<p15>`, with `tools/hooks/kit.toml` checked out from `<p14>`,
  prints a line opening
  `govkit: entry 'agent-cap': its [adopt] argv names 'tools/settings-merge.py'` that carries
  `'settings-merge'`, its note carries `1 naming`, and it exits 1.
  figure: the offered and graded counts are DERIVED at observation. §4 pins 105 at `95350ba5`.
  cost: two selfcheck runs and one clone; not timed at spec time.
- **AC7** — Scratch govs shaped as `build_scratch_gov_kit` builds them (`tools/govkit/selftest.py:5508-5536`)
  carry a second entry, `other`. It is shaped as settings-merge's descriptor is: flat, `home = "."`,
  one `engine` rule landing `other.py` at `{prefix}/other.py`, and `[adopt] argv = ["python",
  "{prefix}/other.py"]`. `demo` declares `requires = ["other"]`. In each, `<g>/tools/govkit/govkit.py
  selfcheck` prints exactly one line that opens `govkit: cross-entry argv:` and carries `offered by`,
  which proves the arm ran, and:
  - with demo's `[adopt] argv = ["python", "{prefix}/other.py"]`, exactly one line opens
    `govkit: entry 'demo': its [adopt] argv names` and carries `other.py` and `'other'`;
  - with `[adopt] via = "other"`, no line opens `govkit: entry 'demo': its [adopt] argv` or
    `govkit: entry 'demo' declares [adopt] via`;
  - with `via = "nobody"`, one line opens `govkit: entry 'demo' declares [adopt] via` and carries
    `names no registry entry`;
  - with `via = "other"` and `requires = []`, that line carries `is not in its requires`;
  - with `via = "other"` and `other`'s argv emptied, it carries `declares no [adopt] argv of its own`;
  - with `via = "other"` beside demo's own argv, it carries `sits beside an [adopt] argv`;
  - with demo's only argv `["bash", "{nosuch}/x.sh"]` and other's argv emptied, a second line
    opens `govkit: cross-entry argv:` and carries `none graded`.
  Red when: the same govs built around the `<p14>` `govkit.py` print no line opening
  `govkit: cross-entry argv:`.
  cost: seven scratch govs, each one selfcheck, about a minute.
- **AC8** — `python tools/govkit/govkit.py mint --base ebce889c7`, run at `<p15a>`, prints exactly
  one line carrying ` -> `, and it opens `mint: agent-cap ·`. After `<p15>`,
  `python tools/govkit/govkit.py epoch --base ebce889c7` prints a line opening
  `epoch: agent-cap · clean ·`. `git grep -h "gov:kit agent-cap@" -- tools/hooks` prints three lines
  carrying one value, the value of `KIT_AGENT_CAP_VERSION`.
  Red when: at `<p15a>` the same epoch prints `epoch: agent-cap · FAILED · last bump`.
  figure: the version is DERIVED by the minter at observation, one above `<p14>`'s in its last
  component.
- **AC9** — `git diff <p14> <p15> -- tools/govkit/ | grep -E '^[+-](def|class) '` prints exactly
  `+def resolve_adopter_argv(`. `grep -c resolve_adopter_argv tools/govkit/govkit.py` prints at
  least 4. `grep -n '_argv_g' tools/govkit/govkit.py` prints nothing. A python one-liner reading
  `tools/hooks/kit.toml` with `tomllib` prints `{'via': 'settings-merge'}` for its `adopt` table.
  `python tools/codebase-map/gen_map.py --check` exits 0. A python program imports
  `tools/gate-lint/encoding_posture.py`, runs `scan_text_io` over the two `tools/govkit/` files, and
  counts exactly the rows `memory/project/encoding-posture-sites.txt` declares for each.
  Red when: the pass minted a second function, left the update site on its own resolution, left
  the symbol index stale, or added an unencoded text-IO site.
  figure: the posture counts are DERIVED from the registry at observation.
- **AC10** — The ledger S9 names exists under `memory/builds/dRedressedBar/build/` and carries
  `**Serves:** journal TOOL-dRedressedBar-15`, with one line per criterion above.
  Red when: the pass closes with no ledger, as at `95350ba5`.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `hook destinations self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dRB-15]` checks on the `[dRB-14]` apply, over `<p14>`, where the run exits 1 and agent-cap's line ends `adopter exit 2` · none

New arm: tools/govkit/selftest.py · covers AC7 · the `[dRB-15]` scratch govs built around the `<p14>` `govkit.py`, where no `cross-entry argv:` line prints · none

AC6 is also re-read by the `govkit selfcheck` leg over the real tree, which reds if any shipped argv
names another entry's file. The refusal join's floor does not move: S5 adds three `r.fail` sites and
the leg grades the floor alone. The main loop observes both new arms red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from `prompts/2026-10-14-prompt-TOOL-dRedressedBar-15-brief.md`.
  The class predicate ran over the real registry at `95350ba5` and found one hit in 105 elements.
  Two scratch applies measured the mirror case at a settings-merge per-kit prefix and the run that
  C2 would lose. Seven candidates were graded by M12, and the pick was taken by M3's rule.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve an adopter command against the install home of
the kit that ships the script it runs"` ranked name-stem SEAMs (`run`, `resolve`, `adopt`,
`resolve_kit_dir`, `resolve_prefix_token`), and none resolves one entry's argv in another entry's
context. The seams this unit extends are the two it calls rather than restates.
`target_context` (`tools/govkit/govkit.py:1415-1477`) is called with the delegate's id, so the
strict-class validation and the per-kit table apply unchanged. The selfcheck bare-target block
(`:3158-3221`) already holds `planned_writes`' rows over every entry. The ownership join reads those
rows as `silenced_legs` and the reserved-prefix check do, so no second planner exists.
`resolve_kit_dir` was weighed as candidate C3 and rejected, with its test, in §4.

The gotchas checklist for the four product paths selected these classes:
- `two-answers-to-one-question`, which is why `via` replaces a copied argv rather than sitting
  beside it (C5);
- `fixture-passes-by-finding-nothing`, which is why the arm prints its offered and graded counts and
  reds when it grades none, and why AC7's absence checks demand the note line;
- `staged-break-substitutes-a-synthetic-value`, which is why AC6 restores the shipped `<p14>` bytes
  rather than a simpler argv;
- `line-claim-matched-over-the-whole-output`, which is why every criterion asserts on the line it
  names;
- `a-new-local-collides-in-a-long-function`, which is why S2 keeps `resolved`, S3 keeps `_res_g`,
  and S5's locals carry a prefix grepped unbound.

The recall probe returned `TOOL-aScouredKit-26` (`memory/builds/aScouredKit/BACKLOG.md:16`). It
records that no cross-entry token exists, and that adding one means deciding what it does when the
named entry is not selected. C1 would inherit that question. `via` answers it for whole adopters
with the `requires` rule, and leaves the ask open (§3). It also returned spec 9 §4 "Why the shared
argv stays safe" (`spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:153-160`). That section rests on
agent-cap's exit being classified by agent-cap's descriptor, which is why S2 and S3 keep the
configured entry's `d` and `ctx`. And it returned `TOOL-cMendedVintage-4`, which moved
check-wiring's settings-merge remedies to the install prefix. That is the same class at a script's
caller, and this unit's arm grades descriptors only.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap declare the same adopter
argv as settings-merge, and how does a per-kit prefix resolve another kit's script" --terms
"agent-cap settings-merge adopter argv per-kit prefix target_context token CONFIGURE requires
descriptor wiring"`
