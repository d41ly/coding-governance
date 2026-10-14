# TOOL-dRedressedBar-9 — settings-merge's adopter exit with no agent-cap hook declared an accepted stop, so a gaining update completes

**Status:** CLOSED · rev-7 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 |
| [2026-10-14-prompt-TOOL-dRedressedBar-13-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-13-4-revision.md) | research | TOOL-dRedressedBar-13 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md) | research | TOOL-dRedressedBar-17 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 |
| [2026-10-14-prompt-TOOL-dRedressedBar-9-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-9-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-brief.md) | research | — |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 |

<!-- /gen:spec-records -->

## 1. Goal

Every writing `govkit update` over a receipt that does not claim `kickoff-manifest` gains
`settings-merge` and leaves `agent-cap` out. It then fails on settings-merge's adopter, which refuses
to wire an `agent-cap.js` that is not installed, and it never re-stamps. This unit declares that
refusal, in that state only, an accepted outcome of settings-merge's own descriptor. The update then
completes, and so does `apply --kits settings-merge`, which fails the same way today.

## 2. Scope (IN)

- **S1** — `tools/govkit/entries/settings-merge.kit.toml` gains one `[[outcome]]` block: `code = 2`,
  a probe whose `must_exist` is `{prefix}/settings-merge.py` and whose `must_not_exist` is
  `{prefix}/hooks/agent-cap.js`, `means = "no-agent-cap-to-wire"` and `ok = true`, with a comment
  stating why. Nothing else in the descriptor moves. Observed by AC1 and AC4.
- **S2** — A writing `update` over a narrow receipt that gains `settings-merge` and leaves `agent-cap`
  out completes. The gained adopter still runs and still exits 2. govkit reads that exit as the
  declared stop, so the run exits 0, re-stamps the receipt and keeps `settings-merge` claimed.
  Observed by AC2 and AC5.
- **S3** — `apply --kits settings-merge` over a target with no hooks kit completes the same way, and
  prints the stop as an accepted one. Observed by AC3.
- **S4** — Where `agent-cap.js` is installed, nothing moves. The shared adopter still exits 0 and
  wires the built-in entry, and an exit 2 there stays a failure. Observed by AC4 and AC6.
- **S5** — One new witnessing arm in `tools/govkit/selftest.py`, inserted after the `u2a` re-stamp
  arms, on a fixture of its own. It asserts the narrow update exits 0, re-stamps at the pin, claims
  `settings-merge`, and printed the stop's `means`, read from the descriptor at run time. Observed by
  AC2, through the `New arm:` line in §7.
- **S6** — `tools/govkit/matrix.py`'s `check_outcome_probes` grades settings-merge's block through
  the engine, beside lexicon's. Its engine-agrees half becomes a helper, `check_outcome_states`,
  called once for lexicon's two existing states and once for settings-merge's three. The
  settings-merge paths are derived from the agent-cap and settings-merge descriptors, never typed.
  Observed by AC4, through the `New arm:` line in §7.
- **S7** — The symbol index moves with S6's mint. After S1 to S6, the pass runs
  `python tools/codebase-map/gen_map.py --write` alone, before the product commit. That commit
  carries `memory/map/generated/symbols.json`, and the map then lists `check_outcome_states` for
  `tools/govkit/matrix.py`. If `--write` moves any other path, the pass commits nothing and returns
  to the main loop (§4, "The symbol index"). Observed by AC7.

## 3. Non-goals (OUT)

- No edit to `tools/govkit/govkit.py`. The gaining rule, its requirement filter and the gained-adopter
  loop stay as they are; §4's alternatives say why the rule is not where the defect sits.
- No edit to `tools/settings-merge.py` and no new flag on it. Its bare form keeps refusing to wire a
  missing hook, which is the guard agent-cap's own adopter relies on.
- No edit to `tools/hooks/kit.toml`. agent-cap keeps its adopter and declares no outcome, so its
  refusal stays a failure wherever agent-cap is selected.
- No change to settings-merge's `[adopt]` argv, its `merged` json-pointer rule or its `requires`.
- No change to which kits the registry's default set holds (brief non-goal).
- No edit to `tools/govkit/selftest.py` beyond the one new arm block. No existing line in it moves,
  and `TOOL-dRedressedBar-3` owns that file's re-arming and lands after this unit (brief non-goal).
- No fix for the `[-8]` arms' gained `run-gates` at an older `--to` vintage. That is a separate
  limitation, and unit 3 scopes those two arms.
- No kit version bump. All three files sit under `{prefix}/govkit`, which the registry exempts as
  "the deployer itself", installed into no target (`tools/govkit/registry.toml:295-297`). So none is a
  `[[files]]` source whose role the version epoch reads (`EPOCH_ROLES`,
  `tools/govkit/govkit.py:12935`). `TOOL-dRedressedBar-7`'s mint over the finished tree measures that
  rather than this spec asserting it.
- No `python tools/run-gates/regen.py --write`, and no generated output other than the map S7
  regenerates. Every other declared output is `TOOL-dRedressedBar-7`'s.

### Edges

- **hands-off** `TOOL-dRedressedBar-3` — the three arms that unit leaves unscoped,
  `and re-stamps the receipt at the new commit`, `[-12] AC4 NEGATIVE` and `[-12] AC9 NEGATIVE`, read
  green only over this unit's descriptor block. That unit lands after this one and owns every other
  edit to `tools/govkit/selftest.py`.
- **hands-off** `TOOL-dRedressedBar-10` — what the round-1 spec audit found (report ids 7, 17 and
  22). S5 and S6 name criteria that never read `tools/govkit/selftest.py` or `tools/govkit/matrix.py`.
  §4's false-accept envelope names one route where three reach it: a single-kit `apply` over a target
  already holding agent-cap, an `update` gaining settings-merge with agent-cap already claimed, and a
  hook the receipt alone locates. Report id 17's half on this spec, the map that lists
  `check_outcome_states`, is closed here by rev-4: S7 regenerates and commits
  `memory/map/generated/symbols.json` in this unit's own pass, and §7 names
  `codebase-map coverage + freshness`. That unit observes S5 and S6 directly, reads the committed
  map, corrects §4 and §5, and, by its F1, narrows this unit's code-2 block with a second
  `must_not_exist` term and adds one row to settings-merge's `check_outcome_states` call. It also
  writes the hands-off to `TOOL-dRedressedBar-7` these Edges lack.
- **hands-off** `TOOL-dRedressedBar-7` — the tree this unit leaves, which that unit measures. The
  three product files sit under `{prefix}/govkit`, which the registry exempts
  (`tools/govkit/registry.toml:295-297`), so they leave that unit no version to bump. The
  `memory/map/generated/symbols.json` this pass commits leaves that unit's `regen.py --write` a
  fresh map.
- **hands-off** `TOOL-dRedressedBar-17` — the `[dRB-9]` update-gaining block, which that unit
  extends with a case gaining both agent-cap and settings-merge at a per-kit agent-cap prefix, so
  `update`'s gained loop is observed resolving agent-cap's `[adopt] via` (report id 13). Also §4's
  two sentences on agent-cap's argv, which `TOOL-dRedressedBar-15` takes away and that unit corrects
  in place (report id 20).

## 4. Design

### The defect, and where it sits

TOOL-aRoutedQuill-5 S4 made a writing `update` install every entry the registry's default set gained
since the receipt's `gov_commit` (`tools/govkit/govkit.py:8863-8879`, `derive_default_gained` at
`:970`). The requirement filter drops `agent-cap`, which requires `kickoff-manifest`
(`tools/hooks/kit.toml:9`). It keeps `settings-merge`, which requires nothing
(`tools/govkit/entries/settings-merge.kit.toml:8`). The gained-adopter loop then runs settings-merge's
adopter (`tools/govkit/govkit.py:11100-11126`).

That adopter is the bare `python {prefix}/settings-merge.py` (`settings-merge.kit.toml:27`). With no
`--fragment`, its only work is wiring agent-cap's built-in `Workflow|Agent` entry
(`tools/settings-merge.py:1020`). It refuses with exit 2 when that hook file is absent
(`tools/settings-merge.py:1046-1052`). No outcome is declared for the exit, so `update` records
`kit 'settings-merge': its adopter exited 2 on the update that gained it` and does not re-stamp.

Measured at spec time with a scratch program that builds the target as `stale_target` does
(`tools/govkit/selftest.py:3237-3249`): `apply --kits check-wiring`, the receipt rewound to the
`24f39915` vintage, committed. Run on `ea25a64a`, whose `tools/` and `skills/` trees are byte-equal to
`ebce889c`'s (`git diff --stat ebce889c7 HEAD -- tools skills` is empty), `update --write` exits 1.
It prints `default-gained settings-merge: adopter exit 2` and `1 problem(s)`, and `gov_commit` stays
`24f39915`. The same program with a dirty `README.md`, and again with a committed deletion of
`tools/check-wiring.sh`, reports the same single problem. Those are the shapes of `[-12] AC4 NEGATIVE`
and `[-12] AC9 NEGATIVE`.

The gaining is not the only route in. settings-merge's `requires = []` is deliberate: its in-file
selftest arm 18 grades a settings-merge install with no hooks kit beside it
(`tools/settings-merge.py:982-996`). Measured at spec time, `apply --kits settings-merge` over a fresh
target exits 1 with `CONFIGURE settings-merge: adopter exit 2` and `unclassified`. So the defect is
settings-merge's own contract: an entry that may stand alone declares an adopter that cannot. The
fix belongs on that contract, and it closes both routes.

### The mechanism: a declared, accepted outcome

govkit already decides what an adopter's exit code means by a filesystem probe. `classify_outcome`
(`tools/govkit/govkit.py:6295`) returns the `[[outcome]]` block whose probe holds, and
`outcome_accepted` (`:6263`) accepts a non-zero exit only through a satisfied block carrying
`ok = true`. `apply`'s CONFIGURE step (`:7745-7764`) and `update`'s gained-adopter loop
(`:11121-11126`) both read it. memory-tree's `seed-and-stop` and lexicon's `no-project-layer` are
the accepted stops that already ship, and TOOL-aWalkedCorpus-9 is the ruling that a declared outcome
may be an accepted stop, per outcome (`memory/DECISIONS.md:90`).

The block, placed between `[adopt]` and `[check]`:

```toml
[[outcome]]
code = 2
probe = { must_exist = "{prefix}/settings-merge.py", must_not_exist = "{prefix}/hooks/agent-cap.js" }
means = "no-agent-cap-to-wire"
ok = true
```

Each probe term has one job.

| Term | Path | Why this path |
|---|---|---|
| `must_not_exist` | `{prefix}/hooks/agent-cap.js` | Where agent-cap's descriptor lands the hook under one prefix (`tools/hooks/kit.toml:21-24`), and the first place settings-merge.py's resolver probes after the receipt, `<here>/hooks/agent-cap.js` (`tools/settings-merge.py:84`, `:105-108`). |
| `must_exist` | `{prefix}/settings-merge.py` | Pins `{prefix}` to the adopter's own directory, so the absence is read where the adopter looked. It also satisfies the matrix's class rule that an accepted stop declared by an absence names a presence (`tools/govkit/matrix.py:149-185`). |

Probed at spec time through the base engine's own functions, on a scratch target with the block
added to an in-memory copy of the shipped descriptor. Nothing in the tree was written.

| State | rc 0 | rc 1 | rc 2 |
|---|---|---|---|
| settings-merge.py present, agent-cap.js absent | accepted | refused | accepted |
| both present | accepted | refused | refused |
| neither present | not probed | not probed | refused |

### Why the shared argv stays safe

At this unit's base, `agent-cap` spelled settings-merge's argv as its own (`tools/hooks/kit.toml:108`
at `ebce889c`). Since `TOOL-dRedressedBar-15` its `[adopt]` table holds `via = "settings-merge"`
alone (`tools/hooks/kit.toml:116` at `7da62c241`), and `resolve_adopter_argv`
(`tools/govkit/govkit.py:1483` at `7da62c241`) runs settings-merge's argv resolved in
settings-merge's context, so the two entries' resolved argvs are equal at every prefix. In
`update`, one resolved argv runs once per run (`tools/govkit/govkit.py:11112-11118`; the dedup on
resolved argvs sits at `:11331-11347` at `7da62c241`). The registry default lists `agent-cap` before
`settings-merge` (`tools/govkit/registry.toml:48-49`), so when both are gained the one run is
classified by agent-cap's descriptor, which declares no outcome. In `apply`, each kit's adopter runs
under its own descriptor (`:7740-7764`), and `via` changes only the argv, never the descriptor that
classifies the exit, so an agent-cap refusal still fails there. Only settings-merge's exit is ever
read through the new block. The argument holds through `via` and the dedup on resolved argvs.

### What it does not check

The probe reads static paths and cannot see the receipt. settings-merge.py's resolver finds the hook
through the receipt first, then at `<here>/hooks`, then at `<here>/../hooks`
(`tools/settings-merge.py:78-108`). Where it finds the hook, `run` still exits 2 on a
`.claude/settings.json` that fails to parse or is not an object (`_load`, `:491-500`) and on a write
`OSError` (`:507-539`). This block refuses that exit only where `{prefix}/hooks/agent-cap.js`
exists. Three routes reach a found hook with that path absent, and in each no agent-cap adopter runs
to report the failure, so the probe reads the stop as accepted:

| Route | Why agent-cap's adopter does not run | Cited at `671f25c7` |
|---|---|---|
| `apply --kits settings-merge` over a target already holding agent-cap | CONFIGURE runs only the selected kits | `tools/govkit/govkit.py:7743-7767` |
| `update` gaining settings-merge where agent-cap is already claimed | the gained loop runs adopters only for gained entries | `tools/govkit/govkit.py:11107-11129` |
| either verb, agent-cap homed elsewhere by `[kit.agent-cap] prefix` or a renamed directory | the receipt row finds it, and the probe cannot read the receipt | `tools/govkit/govkit.py:1453-1459`, `tools/settings-merge.py:146-160` |

`TOOL-dRedressedBar-10` narrows this block with a second `must_not_exist` term,
`{prefix}/../hooks/agent-cap.js`, the resolver's other static home. What still reads as an accepted
stop after it is a hook the receipt alone locates, under either verb. That is an open false accept,
not an accepted one, and `TOOL-dRedressedBar-11`'s receipt-reading probe term closes it.

### What an adopter sees change

| Situation | Before | After |
|---|---|---|
| `update --write` over a receipt that claims neither `kickoff-manifest` nor `settings-merge`, from before the default widened | exit 1; `default-gained settings-merge: adopter exit 2`; `no declared outcome accepts that`; not re-stamped | exit 0; `default-gained settings-merge: adopter exit 2 — no-agent-cap-to-wire`; re-stamped; `settings-merge` claimed and appended to `deploy.toml`'s `kits`; every claimed fragment wired |
| `apply --kits settings-merge` with no hooks kit | exit 1; `CONFIGURE settings-merge: adopter exit 2`; `unclassified` | exit 0; `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]` |
| any install or update where `agent-cap.js` is installed | adopter exit 0 | unchanged |
| `govkit check` | settings-merge declares `[check] none` | unchanged |

`.claude/settings.json` never gains an agent-cap entry in the first two rows, before or after. The
fan-out guard is not installed there, and nothing wires a command naming a file that does not exist.

### The witnessing arms

`tools/govkit/selftest.py` gains one block after line 3313, inside the scope that defines
`stale_target`. It builds `stale_target("rq9")` with `DEPLOY_FULL`, so it shares no fixture with the
three arms it witnesses. It runs `update --target <t> --write` with no `--kits`, and checks four
facts under one `[dRB-9]` label prefix. The run exits 0. The receipt's `gov_commit` is the
`rev-parse` of `GOV_PIN`. The receipt's `kits` holds `settings-merge`, which an arm that only read the
exit code would let a dropped gain pass. The output carries
`default-gained settings-merge: adopter exit 2 — <means>`, with `<means>` read from the descriptor's
code-2 block at run time. That last fact proves the adopter ran and the declared stop was what
accepted it. Its process calls go through `run`, and its file reads name `encoding="utf-8"` as the
`u2a` arm's do, so the file's rows in `memory/project/encoding-posture-sites.txt`, which count only
sites predating that leg, do not move.

`tools/govkit/matrix.py:222-241` grades lexicon's code-1 stop through the engine over two states.
This is that kind's second instance, so the loop becomes `check_outcome_states`, a module-level
helper taking the descriptors, the scratch directory, an entry id, an exit code and a list of
`(label, present paths, expected verdict)` rows. A row may carry an optional fourth element, which
`TOOL-dRedressedBar-11` added: a mapping from a target-relative path to text, which the helper
writes before it classifies and deletes after (`tools/govkit/matrix.py:165`). Lexicon's call keeps
its two rows and its two check labels byte for byte. settings-merge's call grades rc 2 over the
three states in the table above. Its two paths come from the engine's own resolver, `resolve_entry`
(`tools/govkit/govkit.py:449`), over
the agent-cap and settings-merge descriptors in the probe directory's context. So a probe naming a
path agent-cap does not land at reds the "agent-cap.js absent" row rather than passing on a typed
copy of itself.

### The symbol index

The map's python layer lists every public module-level function under `tools/`
(`python_symbols`, `tools/codebase-map/map_lib.py:318-360`), and `tools/govkit/matrix.py` is in
that population: `memory/map/generated/symbols.json:4375-4379` lists its `check_outcome_probes`. So
the new `check_outcome_states` moves the map. `.githooks/pre-commit:233-246` runs the codebase-map
gate on any commit that stages a `.py` file and refuses a stale `symbols.json`, and lines 253-257
refuse regenerated artifacts left unstaged. So the pass regenerates the map with its one declared
generator, `gen_map.py --write` (the `[[generated]]` row at `tools/codebase-map/kit.toml:148-156`),
and commits it with the product files. This build's specs 17 (S10) and 19 (§4, "Order, and unit 7")
take the same step for their own mints.

`gen_map.py --write` renders `inventories.json`, `MAP.md`, `CARDS.md` and `symbols.json`
(`tools/codebase-map/gen_map.py:137-152`). The first three are built from the kit, hook, gate-leg
and dossier inventories, not from function names, so this unit moves only `symbols.json`. At
`3d1adca9`, `python tools/codebase-map/gen_map.py --check` exited 0 (PINNED, 2026-10-14), so a
second moved path would be a sibling's staleness, which S7 returns rather than commits.

`TOOL-dRedressedBar-2` renames `clean` in `tools/unattended/gate-guard.js`, and its pass also
commits a regenerated `symbols.json`. Both units sit at order 1. Their write sets meet on that file,
so by M6 clause 1 they are not disjoint and are built one after the other. `--dispatch` refuses a
path a still-open sibling pass in the same group already declared
(`tools/unattended/unattended.sh:13718-13729`). Whichever unit runs second regenerates over a tree
holding the first one's commit, so its map carries both names. Unit 7's `regen.py --write` then finds
the map fresh.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `no-agent-cap-to-wire` | an `[[outcome]] means` value in a kit descriptor | none; kebab-case, the shape of `no-project-layer` |
| `check_outcome_states` | a module-level function in `tools/govkit/matrix.py` | `py.function`, snake, P1 verb `check` |
| `[dRB-9]` | the check-label prefix of the new selftest arm | none |

`python tools/lexicon/lexicon.py --suggest check_outcome_states --as py.function` answered at spec
time `OK — check_outcome_states leads with \`check\``.

### Rollout

Tier-2: the descriptor is the contract govkit reads for this kit, and the block changes what both
verbs accept as success. No engine bytes move, no receipt or conf shape moves, and no target needs
an upgrade step. The next `update` an adopter runs reads the new descriptor and completes.

### Files touched (estimate)

- `tools/govkit/entries/settings-merge.kit.toml`
- `tools/govkit/selftest.py`
- `tools/govkit/matrix.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

Each candidate was written down with the test that could make it lose before it was graded. The
pick is M3's: the most feature-rich survivor after the vetoes.

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — a requirement-closure rule in the gaining: leave `settings-merge` out whenever `agent-cap` is left out for an unmet requirement | `apply --kits settings-merge` exits 1 at base on the same adopter (measured), and C1 leaves it so. The narrow update's gain of `settings-merge` is what wires `tools/check-wiring.fragment.json` (measured: `hooks: tools/check-wiring.fragment.json wired`; the trigger is `if "settings-merge" in gained`, `tools/govkit/govkit.py:11076-11078`), and C1 drops that gain for every receipt without `kickoff-manifest`. | Survives the vetoes; satisfies fewer criteria than C3 |
| C1b — keep the gain, and skip a gained adopter whose resolved argv equals a left-out entry's | The same `apply --kits settings-merge` probe: apply has no left-out entry to compare against, so it still exits 1. It also turns argv string equality into ownership, which two prefixes break. | Survives the vetoes; satisfies fewer criteria than C3 |
| C2 — settings-merge declares no adopter of its own | `apply` refuses a json-pointer merged rule with no adopter to delegate to (`tools/govkit/govkit.py:7314-7317`), so the rule must move to agent-cap or go. Either way the arm at `tools/govkit/selftest.py:6566-6585`, keyed on `("settings-merge", ".claude/settings.json")` previewing as `BLOCK`, reds, and fixing it edits an existing selftest line. | Vetoed by M3 veto 1: the brief's non-goal on `selftest.py` |
| C4 — an adopter that does not presume `agent-cap.js`: a new tolerant flag on `settings-merge.py` in settings-merge's argv | A new CLI flag is a new public surface on a shipped engine, and it moves settings-merge's engine bytes and version. | Vetoed by M3 veto 2 |
| C3 — the declared accepted outcome | Its losing test was the probe table above: a probe that accepted rc 2 with `agent-cap.js` present would lose. It refuses there. | Chosen |

## 5. Production-readiness checklist

- security — No write surface widens. The accepted stop writes nothing: the adopter refused before
  touching `.claude/settings.json`, and no command naming a missing file is wired. agent-cap's own
  adopter keeps the bare refusal, so a target that selects the fan-out guard and lacks its file still
  fails. §4 "What it does not check" names three routes into a false accept: settings-merge exits 2
  on a `.claude/settings.json` it cannot parse or write, the hook sits where this probe does not
  look, and no agent-cap adopter runs in that run to report it. `TOOL-dRedressedBar-10` refuses the
  resolver's second static home. The receipt-homed residual stays an open false accept, closed by
  `TOOL-dRedressedBar-11`'s receipt-reading probe term.
- perf / scale — N/A — one descriptor block; the probe is two `exists` calls on a path the run
  already resolved.
- error / empty / loading states — An exit 2 is accepted only with the hook absent and the adopter
  present. Every other exit 2, and every exit 1, stays a failure. AC4 reads all three rc-2 states.
- observability — Both verbs already print an accepted outcome's `means` beside the exit code, so the
  stop names itself: `adopter exit 2 — no-agent-cap-to-wire`.
- risks — The suite arms that build `stale_target` and run an unscoped `update --write` now read over a
  run that completes, where before it reported one problem. Those that were green, such as
  `[dGV-8] update --write does NOT re-stamp while a row is unattributed`, assert on a guard that
  prints regardless of the problem count. The main loop's selftest run at the close is the verdict on
  them.
- testing — AC1 to AC6 are direct probes: greps of the descriptor and scratch targets under `%TEMP%`
  driven through `tools/govkit/govkit.py`, each seconds long. AC7 reads the committed map. The two
  new arms are declared in §7.
- migration — N/A — no receipt, conf or deploy field moves, and existing receipts need nothing.
- user docs — N/A — `help/` holds one page, `help/roles.md`, and no page covers govkit. The runbook's
  sentence that `apply` and `update --write` wire every hook a default install lands
  (`WIRE-INTO-PROJECT.md:933-935`) stays true, and no runbook sentence states the failure this
  removes.

## 6. Acceptance criteria

- **AC1** — When `grep -n -A5 '^\[\[outcome\]\]' tools/govkit/entries/settings-merge.kit.toml` runs,
  it prints exactly one block with `code = 2`, `must_exist = "{prefix}/settings-merge.py"`,
  `must_not_exist = "{prefix}/hooks/agent-cap.js"`, `means = "no-agent-cap-to-wire"` and `ok = true`.
  `git diff --stat ebce889c -- tools/govkit/govkit.py tools/settings-merge.py tools/hooks/kit.toml tools/govkit/registry.toml`
  prints nothing.
  Red when: the block is absent, carries no `ok`, or declares only the absence.
- **AC2** — When a scratch program builds a target the way `stale_target` does, and then
  `python tools/govkit/govkit.py update --target <t> --write --to <HEAD sha>` runs over it, the run
  exits 0. It prints `default-gained settings-merge: adopter exit 2 — no-agent-cap-to-wire` and
  `hooks: tools/check-wiring.fragment.json wired`. The receipt's `gov_commit` is the `--to` commit, and
  its `kits` holds `check-wiring`, `run-gates` and `settings-merge`. Over the base descriptor the same
  program exits 1, prints `no declared outcome accepts that`, and leaves `gov_commit` at `24f39915`.
  Red when: the descriptor carries no code-2 block, and the update fails on the gained adopter and
  never re-stamps.
  fixture: a fresh `git init` target under `%TEMP%`, never inside the worktree; the base half was
  observed at spec time on `ea25a64a`, whose `tools/` tree equals `ebce889c`'s.
- **AC3** — When `python tools/govkit/govkit.py apply --target <t> --kits settings-merge` runs over a
  fresh target whose `deploy.toml` carries `DEPLOY_FULL`'s answers, it exits 0. It prints
  `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]`. The target
  holds no `.claude/settings.json`, as at base, so no command naming `agent-cap.js` was wired.
  Red when: the stop is unclassified, and the apply exits 1 as it does at base.
  fixture: a fresh `git init` target under `%TEMP%`.
- **AC4** — When a python program imports `tools/govkit/govkit.py`, reads the shipped descriptors with
  `read_descriptors`, and evaluates `outcome_accepted(2, classify_outcome(...), declares_outcome_for(d, 2))`
  for settings-merge over a scratch directory, it prints ACCEPTED with `{prefix}/settings-merge.py`
  present and `{prefix}/hooks/agent-cap.js` absent. It prints REFUSED with both present, and REFUSED
  with neither. The two paths are the destinations `resolve_entry` gives the two descriptors in that
  directory's context.
  Red when: the probe drops `must_not_exist`, and the both-present state reads ACCEPTED, so an
  agent-cap refusal would be swallowed.
- **AC5** — When the AC2 program instead leaves `README.md` dirty before the update, the run exits 0.
  When it commits a deletion of `tools/check-wiring.sh` before the update, the run exits 0 and prints
  `missing`. Over the base descriptor both exit 1 with the single problem AC2 names.
  Red when: the gained adopter's exit still fails the run, which is how `[-12] AC4 NEGATIVE` and
  `[-12] AC9 NEGATIVE` red at base.
  fixture: the AC2 target, one per shape.
- **AC6** — When `python tools/govkit/govkit.py apply --target <t> --kits agent-cap,settings-merge,kickoff-manifest`
  runs over a fresh target with `DEPLOY_FULL`'s answers, it exits 0. It prints
  `CONFIGURE settings-merge: adopter exit 0` and `CONFIGURE agent-cap: adopter exit 0`, and no line
  carrying `no-agent-cap-to-wire`. The target's `.claude/settings.json` holds a command naming
  `agent-cap.js`.
  Red when: the block is keyed on a code the full install reaches, or its probe stops the wiring.
  fixture: a fresh `git init` target under `%TEMP%`; at base the exit, both CONFIGURE lines and the
  wired `agent-cap.js` command read the same, observed at spec time.
- **AC7** — When a `python` one-liner loads `memory/map/generated/symbols.json` at the unit's tip, it
  finds one entry with id `check_outcome_states` and file `tools/govkit/matrix.py`. Over
  `git show 3d1adca9:memory/map/generated/symbols.json` it finds none.
  `python tools/codebase-map/gen_map.py --check` exits 0 at the tip.
  `git show --name-only --format= <p9>`, over the pass's product commit, lists
  `tools/govkit/matrix.py` and `memory/map/generated/symbols.json`, and no other path under
  `memory/map/`.
  Red when: the mint is committed without the map, so the map lacks `check_outcome_states` and
  `--check` names `symbols.json` stale.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `recall floor arms` · `codebase-map coverage + freshness` · `recall floor`

`codebase-map coverage + freshness` reads the map S7 regenerates. `recall floor` is owed by the
guard join: `memory/map/generated/symbols.json` sits under the `memory/` guard it carries
(`tools/gate-legs.json:868-875`).

New arm: tools/govkit/selftest.py · covers AC2 · the `[dRB-9]` block over the base descriptor, where the update exits 1 on `no declared outcome accepts that` and `gov_commit` stays at the old vintage · none
New arm: tools/govkit/matrix.py · covers AC4 · settings-merge's rows of `check_outcome_states` over the base descriptor, where the absent-hook row reads REFUSED; and over a block staged without `must_not_exist`, where the both-present row reads ACCEPTED · none

The three existing arms this unit witnesses, `and re-stamps the receipt at the new commit`,
`[-12] AC4 NEGATIVE` and `[-12] AC9 NEGATIVE`, move no line. The main loop reads them green in the
same selftest run that observes the new arm. The refusal join's floor does not move, because no
refusal branch is added to or removed from the engine.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the unit-9 brief. The defect was reproduced at the base on
  three narrow-update shapes and on `apply --kits settings-merge`. Four candidates were graded by M12,
  and the pick was taken by M3's rule.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to TOOL-dRedressedBar-10, the batch the round-1
  spec audit's minors were promoted into, for report ids 7, 17 and 22. No scope, design or criterion
  moves.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-17`, the batch the
  units-12-15 spec audit's minors were promoted into, for report ids 13 and 20. No scope, design or
  criterion moves.
- rev-4 · 2026-10-14 · S7 · §3 · §4 · §5 · AC7 · §7 · the correction unit 2's builder divergence
  carried here (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md`): a commit staging a
  mapped file with a stale `symbols.json` is refused by the pre-commit hook. S7 regenerates the map
  with `gen_map.py --write` alone and commits it with the product files. §4 Files touched names the
  map, and §4 gains "The symbol index", with the M6 sequencing against unit 2. AC7 observes the
  committed map. §7 names `codebase-map coverage + freshness` and `recall floor`. The Edges line to
  `TOOL-dRedressedBar-10` no longer defers the map to unit 7's regen: report id 17's half on
  this spec is closed here.
- rev-5 · 2026-10-14 · §3 · §4 · §5 · S5 · S6 · a records fix for TOOL-dRedressedBar-10, closing
  round-1 report ids 7 and 22, written by that unit's spec-writer pass. The status stays CLOSED, and
  no criterion text moves. Id 22: §4 "What it does not check" claimed one route into the false
  accept, reached only by `apply`. It now names the three routes, the narrowing
  `TOOL-dRedressedBar-10` adds and the receipt-homed residual as open, closed by
  `TOOL-dRedressedBar-11`, and §5 security follows. Id 7: S5 and S6 name AC2 and AC4 as their
  observations, and neither criterion reads `tools/govkit/selftest.py` or `tools/govkit/matrix.py`.
  TOOL-dRedressedBar-10's AC7 reads both files directly. Edges gain the hands-off to
  `TOOL-dRedressedBar-7`, the mirror of that spec's new `consumes-from`.
- rev-6 · 2026-10-14 · §4 · a records fix for TOOL-dRedressedBar-13, closing the units-10-11 spec
  audit's report id 6, written by that unit's spec-writer pass `<w13>`. The status stays CLOSED, and
  no criterion text moves. §4 "The witnessing arms" stated `check_outcome_states`'s rows as three
  elements, and `TOOL-dRedressedBar-11` gave them an optional fourth. The sentence now names it,
  cited at `tools/govkit/matrix.py:165` at `fda78c56`. TOOL-dRedressedBar-13's AC6 reads it beside
  the helper's docstring.
- rev-7 · 2026-10-14 · §4 · a records fix for TOOL-dRedressedBar-17, closing the units-12-15 spec
  audit's report id 20, written by that unit's spec-writer pass `<w17>`. The status stays CLOSED,
  and no criterion text moves. `TOOL-dRedressedBar-15` replaced agent-cap's copied `[adopt]` argv
  with `via = "settings-merge"`. §4 "Why the shared argv stays safe" opened on agent-cap's copy of
  the argv; it now says the copy was the base's, cites the `via` line and `resolve_adopter_argv` at
  `7da62c241`, and states that the argument holds through `via` and the dedup on resolved argvs,
  which TOOL-dRedressedBar-17's AC20 reads. The row's second target, the "What it does not check"
  sentence saying agent-cap's own adopter ran the same argv, no longer exists: rev-5's rewrite for
  report id 22 took it out, and the routes table that stands there names no argv. Nothing moves for
  it.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "an adopter exit code declared as an accepted outcome when the kit
it wires is not installed"` ranked `classify_outcome`, `outcome_accepted` and `declares_outcome_for`
in `tools/govkit/govkit.py`. That is the seam this unit extends: the declared-outcome evaluator both
verbs already call. It needs no code, only a descriptor block. Its other hits were name-stem
neighbours, among them `resolve_kit_dir`, which is settings-merge.py's resolver and is read here, not
changed. The matrix's engine-agrees loop over lexicon (`tools/govkit/matrix.py:222-241`) is the second
seam, and this unit extracts it into `check_outcome_states` at its second instance. The gotchas
checklist for the three files selected `staged-break-substitutes-a-synthetic-value` and
`two-answers-to-one-question`. Both are why the matrix rows derive their paths from the descriptors
and the selftest arm reads `means` from the descriptor. S7 builds nothing: its seam is the map's
declared generator, `gen_map.py --write`, the remedy the pre-commit hook names.

The brief and the code disagree in one place. The brief's reuse line says `apply`'s
requirement-complete selection never meets this defect. It does: settings-merge alone is a
requirement-complete selection, and `apply --kits settings-merge` exits 1 at base on the same adopter.
That measurement is what moved the fix from the gaining rule to settings-merge's descriptor. The
recall probe returned TOOL-aWalkedCorpus-9 (`memory/DECISIONS.md:90`), the ruling this block rests on,
and TOOL-aRoutedQuill-5's S1, which made settings-merge a default entry in its own right.

Recall terms used: `python tools/memory-recall/query.py "why does settings-merge's adopter refuse when
agent-cap is absent, and how are adopter exit codes declared as accepted outcomes" --terms
"settings-merge agent-cap adopter outcome accepted stop classify_outcome default-gained requires
kickoff-manifest must_exist probe"`
