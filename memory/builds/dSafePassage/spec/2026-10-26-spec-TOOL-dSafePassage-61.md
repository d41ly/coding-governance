# TOOL-dSafePassage-61 — the size-limits step and gov's own migration, held until the guard admits a value-preserving write

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0018@d4cade33 part 2/2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-17 TOOL-dSafePassage-21 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 |
| [2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md) | research | TOOL-dSafePassage-1 |
| [2026-10-26-prompt-TOOL-dSafePassage-61-2-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-61-2-spec-writer.md) | journal | — |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

Ship the second upgrade step of `cl-dClosedLoop-0018`, `template-size-limits.txt`'s rows into
`budgets.*`, and migrate gov's own tree by it. The design is TOOL-dSafePassage-1 rev-10's S7, S8 and
the size-limits half of its S5, moved here unchanged on 2026-10-26 when that unit's §8 F8 stop fired,
with the sibling items that observe only this step (§2 S2, S3 and S6 to S9).

DEFERRED until `TOOL-dGroundRules-13` lands. The landed minimal guard (TOOL-dGroundRules-6,
`tools/policy/guard.py`) admits one agent shape, a single measured-file cap raised, and refuses S4's
seven-key value-preserving write of `.governance/policy.toml`: `check_raise_shape` returns
"7 keys changed; one cap raised is the one agent shape" (`tools/policy/guard.py:150-151`), and
`.githooks/pre-commit:199-213` runs it on every commit made without a terminal that stages the
policy file. `TOOL-dGroundRules-13` (`memory/builds/dGroundRules/BACKLOG.md:6`) is the ask that would
admit a step's write whose every `budgets.*` value reads the same after it as before.

## 2. Scope (IN)

- **S1** — The step `govkit/template-size-limits-to-budgets`, a row of `tools/govkit/steps.toml` whose
  program is `tools/govkit/steps/template_size_limits.py`, appended after every row that file holds at
  the pass, so TOOL-dSafePassage-3's and TOOL-dSafePassage-11's rows keep the first and second places.
  Its up moves every row of `<prefix>/template-size-limits.txt` into `budgets.*` in
  `.governance/policy.toml`, each row's comment block carried above its key and the file's header (the
  four raise conditions) carried above the table, and retires the file; its down restores both files
  byte-identical. Observed by AC1 and AC2. The file's by-name readers at the base are those
  `git grep -l -F 'template-size-limits' -- ':!memory/builds' ':!memory/ledger'` prints, the backlog
  index row aside, and S4 disposes each.
  **Readers:** by name: `.gitattributes`, `.memory-tree.conf`, `help/size-caps.md`,
  `memory/guides/SESSION-KICKOFF.md`, `memory/map/features/build-method.md`,
  `memory/map/features/playbook.md`, `memory/map/generated/CARDS.md`,
  `memory/project/method-carriers.txt`, `tools/check-spec-tokens.test.sh`,
  `tools/check-template-size.sh`, `tools/check-template-size.test.sh`, `tools/gate-legs.json`,
  `tools/govkit/registry.toml`, `tools/line-length-limits.txt`, `tools/memory-recall/extract.py`,
  `tools/policy/budgets.py`, `tools/policy/caps.toml`, `tools/policy/catalogue.toml` and
  `tools/run-gates/gate-profiles.txt`, as at base 60d90cb7 · by value: `budgets.py resolve`, which
  reads the file as its `limits:` home until the step (`cl-dClosedLoop-0015`), and through it the
  template-size gate and `tools/check-spec-tokens.py`'s size join (dGroundRules unit 9, S5).
- **S2** — The witness. It holds when `<prefix>/template-size-limits.txt` is absent and either no
  before-image exists or every cap reads its image's value (TOOL-dSafePassage-26 S8, id 9, moved
  here). Observed by AC6.
- **S3** — The no-image down. `template_size_limits.py down <t> <prefix>` on a target with no limits
  file and no image under `.governance/steps/govkit/` exits 0 and writes nothing; code in the program
  that refuses before the shared restore helper is fixed in this pass (TOOL-dSafePassage-35 S17,
  id 41, moved here). Observed by AC7.
- **S4** — Gov migrated first. This unit's pass runs S1's up on gov's tree first, so
  `tools/template-size-limits.txt` leaves gov in the unit's commit. Every by-name reader S1's
  `git grep` prints at the build run's base is disposed in that commit: the `[[exempt]]` row and its
  three `why` mentions in `tools/govkit/registry.toml`, the `.gitattributes` eol row and the
  `RECALL_EXTRA_SOURCES` member in `.memory-tree.conf` are removed or re-pointed to
  `.governance/policy.toml`. `budgets.py`'s `limits:` branch retires and this unit adds the `policy`
  form, `HOME_FORMS` swapping `limits` for it to read `("policy", "file", "conf", "constant")`;
  `tools/policy/caps.toml`'s seven `limits:` rows read `home = "policy:"`, no locator, the value held
  only under `budgets.<name>`, which `resolve_caps` reads as a file value, refusing a `legacy:` handed
  in for it as for `limits:`. `arm_cap_census` exempts a `policy:` row from naming its cap as it did a
  `limits:` one, its limits-file half goes (`check_budgets` already finds a `budgets.<cap>` no row
  names), and the seven `budgets-cap-` plants set `budgets.<name>` where they copied the file.
  `arm_limits_readers`' row of `arm_single_reader` and the cases planting the file go, and
  `budgets-two-homes` is re-planted on a `conf:` home, since gov's is the only tree that ever held the
  file (an `[[exempt]]` path, shipped to no adopter). Each prose mention names `budgets.*`, the
  dossiers' cards re-rendered by `python tools/codebase-map/gen_map.py --write`. The mirror,
  `policy.py mirror --write`, is a second commit: it refuses while the policy file differs from HEAD,
  and the guard admits a mirror only when that file and the catalogue equal HEAD (dGroundRules units
  5 S2, 19 S1). Observed by AC1, AC3 and AC4.
  **Readers:** by name: the readers S1 lists · by value: `budgets.py resolve`, whose `limits:`
  branch this item retires; no reader compares or counts the file's path itself.
- **S5** — The window member. `template-size-limits.txt` joins TOOL-dSafePassage-1's translation
  window through S1's `surfaces`, and closes when this unit lands. Observed by AC5.
- **S6** — Dead paths. `tools/check-dead-paths.sh` excludes the step's declarations from its haystack
  by three commented `:(exclude)` pathspecs beside its own two files (`tools/check-dead-paths.sh:193-196`),
  no waiver row; the help page names a step's dead path by its id (TOOL-dSafePassage-26 S21, id 38,
  moved here, its reading of AC3's exclusions folded into AC3). Observed by AC8.
- **S7** — The gate's arms. `tools/check-template-size.test.sh`'s limits-file arms (A19 and the pair
  arms, `:112-172`) feed scratch `.governance/policy.toml` fixtures, a non-numeric limit redding
  through the policy reader (TOOL-dSafePassage-26 S22, id 39, moved here). Observed by AC9.
- **S8** — Gov's before-image. Gov's image of this step is removed once its witness holds, gov's down
  being its history: no `.governance/steps/` path is tracked or untracked in gov's tree, and
  `memory/map/generated/CARDS.md` is regenerated without the retired file (TOOL-dSafePassage-26 S23,
  id 40, moved here).
  **Readers:** by name: READER NOT IN TREE — `write_before_image` and `write_from_before_image` are
  unbuilt TOOL-dSafePassage-1's; the one tracked reader, `memory/map/generated/CARDS.md`, is
  regenerated · by value: NO VALUE READERS — nothing on gov's tree reads its image's caps.
  Observed by AC10.
- **S9** — The release-0 condition. `tools/govkit/fixtures/release-0/plants.toml` gains the
  `[[condition]]` row `size-limits`: step `govkit/template-size-limits-to-budgets`, plant
  `tools/template-size-limits.txt` created with one row, moved here from TOOL-dSafePassage-5's §4
  plants table so the row lands with the step it names. Observed by AC11.

## 3. Non-goals (OUT)

- Widening the guard. That is `TOOL-dGroundRules-13`'s, an owner-risk surface; this unit builds
  only once it lands, and never commits around the guard (`--no-verify`, a pty wrapper).
- The step row grammar, its reader, the before-image helpers, `render_policy_text` and the frozen
  check: TOOL-dSafePassage-1's.
- The fan-out step `agent-cap/fanout-cap-to-agents-in-flight`, which stays in TOOL-dSafePassage-1.
- Any other legacy home; dConvergedCharter folds the kit conf keys.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the `[[upgrade]]` grammar, `read_steps`, `tools/govkit/steps.toml`, `write_before_image`, `write_from_before_image`, `render_policy_text` and the window's `--window` listing; without them S1's row has no reader and its program no helpers
- **consumes-from** `TOOL-dSafePassage-5` — `tools/govkit/fixtures/release-0/plants.toml` and its `[[condition]]` grammar, and `upgrade_walk.py`; without them S9's row has no home and AC11 no reader
- **consumes-from** `TOOL-dSafePassage-17` — the no-image rule of `write_from_before_image`, without which S3's down refuses for want of an image
- **consumes-from** `TOOL-dSafePassage-26` — the moved minors S2, S6, S7 and S8 carry (ids 9, 38, 39, 40), and `write_atomic`, through which the before-image is written
- **consumes-from** `TOOL-dSafePassage-35` — the moved minor S3 carries (id 41)
- **consumes-from** external — dGroundRules: `TOOL-dGroundRules-13`, the guard admitting a step's value-preserving write of gov's policy file, without which S4's commit is refused at `.githooks/pre-commit`; and `budgets.*` with `budgets.py resolve` and `caps.toml` (`cl-dClosedLoop-0015`), the mirror and the guard, without which S1 has no key to write

## 4. Design

### Data model

The row, in TOOL-dSafePassage-1's grammar (its §4 "### Data model"):

```toml
# tools/govkit/steps.toml, after every row the file holds
[[upgrade]]
id = "govkit/template-size-limits-to-budgets"
up = ["python", "{gov}/govkit/steps/template_size_limits.py", "up", "{target}", "{prefix}"]
down = ["python", "{gov}/govkit/steps/template_size_limits.py", "down", "{target}", "{prefix}"]
witness = ["python", "{gov}/govkit/steps/template_size_limits.py", "witness", "{target}", "{prefix}"]
surfaces = ["file:{prefix}/template-size-limits.txt"]
needs-target = false
```

**S1's up.** No `<prefix>/template-size-limits.txt`: exit 0. Otherwise it splits the file into its
header comment block and its rows, each with the comment block above it; runs `budgets.py resolve`
for each row's cap at the landed revision, its CLI's only one (unit 9, S2), exiting 1 where that
exits 2 or prints source `file` with another value; renders the `[budgets]` table into
`.governance/policy.toml`, the header above the table and each comment block above its key,
verbatim; and removes the file. It writes its before-image first and reads before the commit as
TOOL-dSafePassage-1 §4 states for every step. Witness: S2.

**Writing the policy file.** Through `render_policy_text` in `tools/govkit/upgrade_steps.py`, as the
fan-out step does.

**The guard at each commit.** The pass commit stages `.governance/policy.toml` with every
`budgets.*` value unchanged, which the guard refuses at the base and `TOOL-dGroundRules-13` asks it to
admit. The row and gov's migration land in one commit, so the landing that first declares the row
finds its witness holding on gov, and TOOL-dSafePassage-8's gov-first walk writes no guarded path.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `cmd_up`, `cmd_down`, `cmd_witness`, `main` | `tools/govkit/steps/template_size_limits.py` | `py.function` snake |
| the step id `govkit/template-size-limits-to-budgets` | the row above | — |
| the `policy` home form | `tools/policy/budgets.py` `HOME_FORMS` | — |
| the condition row `size-limits` | `tools/govkit/fixtures/release-0/plants.toml` | — |

Each new `raise Refusal` and `r.fail` site is a `tools/govkit/refusal_join.py` anchor armed by a
`tools/govkit/selftest.py` arm, its `BRANCH_PIN` floor moving by the count measured at both ends.

### Migration

Gov's tree is migrated by S4 in this unit's pass, after `TOOL-dGroundRules-13` lands and the build
run re-grounds this spec against it (§8 F1). No adopter tree holds the file.

### Rollout

Live at the landing after its pass. The window member closes there (S5). The build run's pass reads
whether the landed guard admits S4's write before writing code, and stops if it does not.

### Files touched (estimate)

- `tools/govkit/steps.toml`
- `tools/govkit/steps/template_size_limits.py`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `tools/govkit/registry.toml`
- `tools/govkit/fixtures/release-0/plants.toml`
- `tools/template-size-limits.txt` (removed)
- `.governance/policy.toml`, `.governance/policy.json`
- `tools/policy/budgets.py`, `tools/policy/caps.toml`, `tools/policy/catalogue.toml`,
  `tools/policy/check_policy.py`, `help/size-caps.md`
- `.gitattributes`
- `.memory-tree.conf`
- `memory/project/method-carriers.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/check-template-size.sh`
- `tools/check-template-size.test.sh`
- `tools/check-dead-paths.sh`
- `tools/check-spec-tokens.test.sh`
- `tools/gate-legs.json`
- `tools/line-length-limits.txt`
- `tools/memory-recall/extract.py`
- `tools/run-gates/gate-profiles.txt`
- `memory/map/features/build-method.md`
- `memory/map/features/playbook.md`
- `memory/map/generated/` (CARDS)
- `help/upgrade-steps.md`

### Alternatives rejected

- Keeping the row in TOOL-dSafePassage-1 and moving only S4 (§8 F1).
- Running the step on gov in the lander's prepared merge, where no hook fires (§8 F1).

## 5. Production-readiness checklist

- security — the program runs no target code and a down never overwrites a later edit; the guard
  judges the pass commit, and nothing commits around it.
- perf / scale — one `budgets.py resolve` per row, seven rows on gov.
- error / empty / loading states — no limits file is exit 0 for the up and the down; a resolve that
  exits 2 or disagrees is exit 1 writing nothing.
- observability — the up names each cap it moves; the witness names the cap that differs.
- risks — the guard `TOOL-dGroundRules-13` lands may admit a narrower shape than S4 writes; the
  build run re-grounds first (§8 F1).
- testing — `tools/govkit/selftest.py` arms over scratch gov trees and targets, and the two suite arms
  of §7.
- migration — §4 Migration.
- user docs — `help/size-caps.md` names `budgets.*` as the one home, and `help/upgrade-steps.md`
  names the step by its id.

## 6. Acceptance criteria

Where each criterion came from: AC1 to AC4 are TOOL-dSafePassage-1 rev-10's AC13, AC14, AC15
and AC19, and AC5 the size-limits half of its AC16; AC6 is TOOL-dSafePassage-26's AC7, AC7 is
TOOL-dSafePassage-35's AC15, and AC8 to AC10 are TOOL-dSafePassage-26's AC20 to AC22.

- **AC1** — When S1's `up` argv runs on a remote-less scratch clone of gov's tree at the build run's
  base and commits on `main`, the clone's `python budgets.py resolve` prints each row's cap of
  `tools/template-size-limits.txt` with its base value, the file is gone, each comment block stands
  above its key (`grep -n -F 'RAISED from 32768' .governance/policy.toml`), and the header's four
  raise conditions stand above the table.
  Red when: a planted row whose comment block contains a tab-separated line reads a different cap
  after the step.
  fixture: needs the landed `budgets.*` and `budgets.py`.
- **AC2** — When S1's `down` argv runs after its up on that copy, `tools/template-size-limits.txt`
  and `.governance/policy.toml` are byte-identical to the base.
  Red when: a byte differs.
- **AC3** — When the unit is committed, `git ls-files tools/template-size-limits.txt` prints nothing,
  S1's `witness` argv exits 0 on gov's tree, and `git grep -c -F 'template-size-limits' --
  ':!memory/builds' ':!memory/ledger' ':!memory/backlog' ':!tools/govkit/steps.toml'
  ':!tools/govkit/steps/' ':!help/upgrade-steps.md' ':!tools/govkit/fixtures/release-0/'` prints
  only `.governance/policy.toml:1`. The exclusions are the step's declarations; that line is the
  header its up carries, and any other path a reader S4 left.
  Red when: the grep prints another line or a higher count.
- **AC4** — When `python tools/policy/budgets.py resolve AGENTS.md` runs on gov's tree after S4, it
  prints `AGENTS.md` with the value `budgets."AGENTS.md"` holds in `.governance/policy.toml` and
  source `file`, its census row reading `home = "policy:"`; and `python tools/policy/check_policy.py`
  prints `policy-check: arm_cap_census ·` with no finding line under it.
  Red when: the census refuses the home as opening with none of `HOME_FORMS`, or `arm_cap_census`
  reds a `policy:` row's enforcer for never naming its cap.
- **AC5** — When `python tools/govkit/upgrade_steps.py list --window` runs on gov's tree after the
  unit lands on `main`, it prints `template-size-limits.txt` closed by
  `govkit/template-size-limits-to-budgets`; on the unit's branch before the landing it prints it
  `open`.
  Red when: the unlanded step's home prints `closed`.
- **AC6** — When `python "tools/govkit/steps/template_size_limits.py" witness <t> tools` runs on a
  scratch target that never held the file, and on gov's tree, each exits 0.
  Red when: the witness requires a before-image never written.
- **AC7** — When `python "tools/govkit/steps/template_size_limits.py" down <t> tools` runs on a
  scratch target with no limits file and no image under `.governance/steps/govkit/`, it exits 0 and
  `git -C <t> status --porcelain` prints nothing.
  Red when: the program refuses before the shared helper for want of an image.
- **AC8** — When `bash tools/check-dead-paths.sh` runs, it names no hit in `tools/govkit/steps.toml`,
  `tools/govkit/steps/` or the release-0 fixture; a planted basename of the retired file in a
  tracked `.md` outside `memory/` makes it exit 1 naming it.
  Red when: the exemption is a waiver row, or it hides a prose carrier.
- **AC9** — When `bash tools/check-template-size.sh` runs over a scratch `.governance/policy.toml`
  declaring a non-numeric `budgets` limit, it exits non-zero naming the key, and
  `git grep -n "limits-bad" -- tools/check-template-size.test.sh` prints nothing.
  Red when: an arm still feeds the retired limits file.
- **AC10** — When `git ls-files -- .governance/steps`, `git status --porcelain -- .governance/steps`
  and `git grep -n -F "template-size-limits.txt" -- memory/map/generated/CARDS.md` run on gov's tree,
  each prints nothing.
  Red when: gov's image is committed or left untracked.
- **AC11** — When `python "tools/govkit/upgrade_walk.py" --list` runs, it prints the `size-limits`
  condition row naming `govkit/template-size-limits-to-budgets`, and
  `python "tools/govkit/upgrade_walk.py" --case skip --step govkit/template-size-limits-to-budgets`
  exits 0.
  Red when: the row is absent, so the skip case reads the step as not load-bearing.
  cost: minutes, since the skip case builds the release-0 tree.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `recall floor` · `kit/dogfood doc parity` · `kit epoch (shipped bytes move, the version moves)` · `dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `method carriers (every pointer declared)` · `template size <=48KiB` · `template size gate selftest` · `every held leg is budgeted, every budget row resolves` · `codebase-map coverage + freshness` · `spec-tokens self-test` · `memory hygiene` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `transition-audit arms` · `straggler-guard arms` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC6 AC7 · each case staged by its own scratch gov tree or target, one planted row or file per arm · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count
New arm: tools/check-template-size.test.sh · covers AC9 · a scratch policy file declaring a non-numeric limit · none
New arm: tools/check-dead-paths.test.sh · covers AC8 · a retiring step's declaration beside a planted prose carrier · none

What these arms do not check: that the landed guard admits S4's write, which the pass commit meets;
and a step program's imports, as TOOL-dSafePassage-1 §7 states for every frozen row.

## 8. Open questions

- **F1 — Who moves gov's own caps, given the minimal guard?** Carried from TOOL-dSafePassage-1 §8 F8.
  `cl-dClosedLoop-0012`'s guard refuses every agent write to the policy file but one cap raise, and
  S4 writes every `budgets.*` row at once. (a) This unit's pass runs S1 on gov, every cap reading
  unchanged. (b) TOOL-dSafePassage-8's lander runs it in the prepared merge. (c) Gov keeps the file
  until an attended run moves it. (c) fails unit 8's red on a witness that does not hold on gov and
  leaves an `[[exempt]]` row naming a removed file; (b) commits the refused shape through
  `commit-tree` with no hook (`tools/push-main.sh:921`), routing around the guard; (a) fails only
  veto 3, if the landed guard refuses a value-preserving write. Recommendation (a), rung 5, "Standing
  ruling takes it (Recommended)" (ER:388), that write shape asked of dGroundRules as
  `TOOL-dGroundRules-13`. RESOLVED (agent, 2026-10-23, delegated): (a) · widens: none · relaxes: none
  The stop fired at TOOL-dSafePassage-1's first pass, 2026-10-26, so the row moved here with S4: a
  row declared without gov's migration would have the landing's walk write the refused shape. The
  build run re-grounds this spec against the guard `TOOL-dGroundRules-13` lands, reads whether it
  admits S4's write, and stops this unit again if not.
- **F2 — What does S4 leave of the policy kit's limits-file machinery?** Carried from
  TOOL-dSafePassage-1 §8 F12. `budgets.py`'s `limits:` branch retires with the file. (a) The seven
  census rows take a `policy` `home` form, a value held only under `budgets.<cap>`, which this unit
  adds to `HOME_FORMS` and the census join (S4); `arm_limits_readers`' row and the cases planting the
  file go, and `budgets-two-homes` is re-planted on a `conf:` home. (b) The rows keep `limits:` naming
  an absent file, the arm's reader directory moving to `tools/govkit/steps/`: a home and an arm over a
  file no tree holds. Recommendation (a), charter `[yagni]`. Rung 3. RESOLVED (owner, 2026-10-24): (a).

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft: TOOL-dSafePassage-1 rev-10's S7, S8, AC13, AC14, AC15, AC19,
  the size-limits half of S5 and AC16, and §8 F8 and F12; TOOL-dSafePassage-26's S8, S21, S22, S23
  with AC7, AC20, AC21, AC22; TOOL-dSafePassage-35's S17 with AC15; and TOOL-dSafePassage-5's
  `size-limits` condition row, moved by `2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md`.
  AC3 folds TOOL-dSafePassage-26 S21's exclusions; S1's readers are re-derived at base 60d90cb7.
- rev-2 · 2026-10-26 · AC6 · AC7 · §7 · the leg line names `run-gates canary`, `run-gates gov canary`
  and `measure-legs selftest`, whose guard `tools/gate-legs.json` trips, `transition-audit arms`
  and `straggler-guard arms`, whose guard `.memory-tree.conf` trips, and `policy fixtures`, whose
  guard `tools/govkit/selftest.py` trips, each from §4 Files touched; AC6 and AC7 quote the step
  program this unit creates, as sibling criteria quote a created file, so the path join does not
  read it as tracked, by `2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md`; no
  other section moved.

## 10. Reuse audit

Seams extended: TOOL-dSafePassage-1's reader, before-image helpers and `render_policy_text` in
`tools/govkit/upgrade_steps.py`; `budgets.py`'s `HOME_FORMS` and `resolve_caps`
(`tools/policy/budgets.py:57`, `:275-279`); the dead-path haystack's exclusions
(`tools/check-dead-paths.sh:193-196`); and TOOL-dSafePassage-5's `[[condition]]` rows.
`python tools/codebase-map/reuse_lookup.py "move a legacy limits file's rows into the policy file's budgets table as an upgrade step"`
ranked name-token neighbours (`rows`, `row`, `step`, `load_policy`, `read_catalogue_row`), none a
writer of a policy key, so no existing seam fits beyond those named. Recall found the ask
`TOOL-dGroundRules-13` and `PLAY-dOrderedCharter-6`'s re-ground, which reads the rows as moved by
this step.

Recall terms used: `python tools/memory-recall/query.py "how does gov move its size-limits file into the policy file under the minimal guard" --terms "template-size-limits budgets policy guard upgrade step value-preserving raise shape census limits home gov migrated first"`
