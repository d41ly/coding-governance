# DEPL-dShippedRelease-27 — `carries` on the landing record, the `landing` class, publications, `commits.squash` and Codex targets

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0437@bb284003 whole
**Carries:** node:policy-key.commits.squash

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md](../build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md) | research | DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-30 |
| [2026-10-30-build-DEPL-dShippedRelease-27-deviation-271.md](../build/2026-10-30-build-DEPL-dShippedRelease-27-deviation-271.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-27-deviation-272.md](../build/2026-10-30-build-DEPL-dShippedRelease-27-deviation-272.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

The landing record says what a landing moved, a commit's trailers survive a squash or the loss is recorded,
and what was published names the tree it showed. An install that names Codex gets Codex's targets, with its
hook trust surfaced at install and again whenever a Codex-installed hook's bytes move. One clause holds five
behaviours, so this one spec holds them as S-items and is not split into parts. The range is `<landing_prior_tip>..<landed sha>`, because `<current default>..HEAD` is empty once the landing has pushed.

## 2. Scope (IN)

**Build-run preconditions**, each specced and unbuilt at this base: `read_landing`, `set_landing_field` and
`deploy_fixture.py` (DEPL-dShippedRelease-1); `landing_prior_tip` (DEPL-dShippedRelease-12);
`record-kind.release` (DEPL-dShippedRelease-15); `read_commits` and the `[[trailer]]` table
(TOOL-dDeclaredLoop-23, PLAY-dOrderedCharter-28); `tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19,
-28); `.githooks/prepare-commit-msg` (TOOL-dWellOiledMachine-33 S4); and
`tools/runtime/harnesses/codex.toml`, `resolve_install_target` and `runtime.harnesses`
(TOOL-dWellOiledMachine-14 S1, S5, S6). `item.deploy.record` and `record-kind.landing` are unit 1's, and
`record-kind.release` unit 15's: this unit extends both and owns neither.

- **S1** — `carries`. `derive_landing_carries(sha, root)` in `tools/loop/deploy_items.py` reads
  `read_landing_outcome(sha)`'s `landing_prior_tip`, then
  `read_commits(repo, ["--no-merges", "<prior>..<sha>"], ("Pass",))`, and returns the value
  `<prior>..<sha> · <n> commit(s)`. This is the range the clause writes `<current default>..HEAD`, with
  `--no-merges`: once pushed, the default branch equals `<sha>` and that spelling is empty, so the prior tip
  stands in for `<current default>` (§8 F1, the deviation). `unattended.sh --deploy carries <sha>` writes it
  through `set_landing_field` after `--deploy record`. `read_landing_carries(sha, root)` is the one reader:
  it re-runs `git rev-list --no-merges` over the recorded range and returns the commits, so the list is
  derived and never stored beside the count. On a second node `read_landing_outcome` derives the prior tip
  as the SHA's first parent (DEPL-dShippedRelease-12 S8), which under an in-place close names too short a
  range, so that value carries the clause `prior-derived`. `check_carry_set` (`tools/push-main.sh:962`) is
  not this set, and neither reader calls it. Observed by AC1, AC2.
- **S2** — The `landing` native-id class. One `[[native]]` row in `tools/playbook/namespaces.toml`:
  `class = "landing"`, `owner = "dShippedRelease"`, `pattern = "deploy_items:LANDING_RE"` and
  `resolver = "deploy_items:print_landing_ids"`, the id `landing-<first 12 hex of the landed sha>` from
  `derive_landing_id(sha)`, `LANDING_RE` `landing-[0-9a-f]{12}`. The resolver lists `refs/gov/landing/*`
  after one bounded fetch. Observed by AC3.
- **S3** — A publication. `python deploy_items.py publish <sha> <url>` writes one `record-kind.release`
  record per (SHA, artifact environment), the environment spelled `artifact:<url>`, by
  `python release.py record <sha> artifact:<url> --outcome verified`, `write_release`'s verb
  (DEPL-dShippedRelease-15 S11), the integrations kit found through `resolve_kit_dir`, an absent kit exiting
  2 naming it. A second publish of one pair prints `publish — already recorded` and writes nothing. It
  refuses a URL that is not `https` or that carries a userinfo part, and a `<sha>` the default branch does
  not contain. An `artifact:` environment is never a member of `release.environments`, so no `release.*`
  pass picks it. The atlas is the first subject: the page `help/deploy.md` names the verb and the publisher
  runs it, and no instrument changes. Observed by AC4.
- **S4** — The squash, read at the landing. `derive_squash_commits(rng)` finds each commit of the
  `--no-merges` range whose message holds git's `Squashed commit of the following:` line, and
  `check_squash_landing(prior, sha)` acts by `commits.squash`, read by a literal
  `policy.py get commits.squash`, per the table in §4. The prepared landing in `tools/push-main.sh` calls it
  after `check_carry_set` (`:962`), before the marker at `:967`, and under `refuse` it exits 1 with nothing
  pushed. The attended path calls it at the same place relative to `:1128`. A lossy result writes
  `squash: lossy · <n> commit(s)` as a second clause of the `carries` value. Observed by AC5, AC6, AC7.
- **S5** — The union, re-emitted at the commit. `.githooks/prepare-commit-msg` gains a `squash` source arm:
  under `re-emit-union`, `derive_squash_union(<SQUASH_MSG>)` reads every indented `    <Key>: <value>` line
  whose key the `[[trailer]]` table registers, de-duplicates, and appends them with
  `git interpret-trailers --in-place --if-exists addIfDifferent`, then `Gov-Squash: union`, a `[[trailer]]`
  row this unit adds. Under the other two values the arm does nothing. Observed by AC5.
- **S6** — A hosted squash. A hosted squash button never runs the lander, so `refuse` cannot stop it
  (`.githooks/pre-rebase:14` states that blindness). `derive_outside_commits(prior)` walks the first-parent
  line back from `<prior>` to the newest commit holding a landing record, at most 200 commits, and each
  single-parent commit on it that no landing record names is recorded `outside: <n> commit(s)` in the
  `carries` value of the next landing, under every value of the key. It records and refuses nothing (§8 F3,
  the deviation). Observed by AC8.
- **S7** — The key. `commits.squash`'s row (`tools/policy/catalogue.toml:1560`) gains `summary` and `usage`,
  its name drained from `tools/policy/unsummarised-keys.txt` with `policy.py lists --write`, and gains no
  second row. Its allowed values and default stay `re-emit-union`, `refuse`, `accept-loss` and
  `re-emit-union`. Observed by AC9.
- **S8** — Codex targets. `tools/runtime/harnesses/codex.toml`'s `[install]` declares
  `settings = ".codex/hooks.json"` and a fourth kind, `config = ".codex/config.toml"`, because a kind names
  one path and Codex has two; `resolve_install_target` stays as it is. `run_fragment_merges`
  (`tools/govkit/govkit.py:6109`) resolves the settings path per harness of `runtime.harnesses`, calling
  `resolve_install_target("settings", [harness])` once for each, in place of the literal at `:6133`, so a
  Codex-only install writes no `.claude/` file; `GOV_SETTINGS_JSON` keeps its meaning for `claude-code`. A
  missing `.codex/hooks.json` is seeded `{"hooks": {}}`. No kit row lands a `config` target today, so that
  file is declared and written by nothing yet. Observed by AC10.
- **S9** — The trust step, surfaced. `tools/govkit/codex_targets.py` holds `derive_codex_hooks(target)`, the
  hook files `.codex/hooks.json` wires, and `derive_retrust(before, after)`, those whose receipt `sha256`
  moved or which are new. `apply` (`cmd_apply`, `:7503`) prints
  `codex — trust step · <n> hook(s) · <command>` for every wired hook, since none is trusted yet. `update`
  (`cmd_update`, `:9144`) prints the same line for the moved hooks and appends one `codex-retrust` row to
  the receipt's `orders`, the attended step DEPL-dShippedRelease-17 walks and a `kits.offer` run carries as
  its outbox order; no moved hook writes no row. The check reads bytes and runs nothing, so it is legal in
  the offer's mode. Observed by AC11, AC12.

## 3. Non-goals (OUT)

- No landing record and no `read_landing`: unit 1's.
- No squash in the lander: `tools/push-main.sh` makes `--no-ff` merges only (`:881`, `:1070`), and this unit
  adds no squash path.
- No rewrite of a landed commit, and no second commit for a lost trailer: a loss is recorded.
- No publication automation: the publisher runs the verb, and the atlas instrument is not edited.
- No `release.*` program: an `artifact:` environment is a record only.
- No Codex hook adapter for the runtime's own spawns: TOOL-dWellOiledMachine-14, -36 and -37 own those, and
  the preflight's `untrusted-hook` rule reads the store this step asks the owner to update.
- No owner item for a re-trust. The attended step serves both verbs, because an offer's grant reaches only
  `gov/update-*` on the adopter's remote and could post no mail there.
- No gov content for `.codex/config.toml`: no row lands one, and a key written for its own sake is
  scaffolding.

### Edges

- **consumes-from** `DEPL-dShippedRelease-12` — `landing_prior_tip`, the tip before the push, without which the range is empty
- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing`, with `set_landing_field`, the record `carries` lands on
- **consumes-from** `DEPL-dShippedRelease-15` — `record-kind.release`, the kind, and `write_release`, the writer a publication uses
- **hands-off** `DEPL-dShippedRelease-17` — `codex-retrust`, the `orders` row its attended walk runs
- **consumes-from** external — TOOL-dDeclaredLoop-23's `read_commits`, PLAY-dOrderedCharter-28's `[[native]]` and `[[trailer]]` tables, TOOL-dWellOiledMachine-33's `prepare-commit-msg` and -14's harness table, each specced and unbuilt at base `f4597719`
- **hands-off** external — a Maintain reading of a hosted squash past what S6 records, which dTendedCadence may take

## 4. Design

### Evidence

- `cmd_land` reads the tip `R` at `tools/push-main.sh:956`, and the attended path `was` at `:1127`; neither
  is recorded today, and `write_lander_marker` holds no prior tip. Unit 12 records it as
  `landing_prior_tip`.
- `derive_carry_set` (`tools/push-main.sh:548`) is the intersection with the LOCAL default branch, a
  different question from the range, which is why TOOL-dWellOiledMachine-39 §8 F3's reading is not followed.
- The research measured git's default squash message as 0 parsed trailers and two indented raw lines
  (research-git-pockets:50), which is the input S5 reads.
- `run_fragment_merges` writes `.claude/settings.json` by literal (`tools/govkit/govkit.py:6133`), and
  `settings-merge.py` takes the settings path as its first argument, so S8 changes the argument and not the
  merge.
- Measured 2026-10-30, `codex-cli 0.139.0` on this node (PINNED): `codex --help` documents
  `--dangerously-bypass-hook-trust`, "without requiring persisted hook trust", so the trust the gap names is
  real at that version. The shape of `.codex/hooks.json` is UNVERIFIED here: research-harness-cli:52 and
  :133 name the file and its twelve events and show no body, so S8 seeds the `{"hooks": {}}` form
  `settings-merge.py` reads, and TOOL-dWellOiledMachine-36's `hook-events` row is what confirms it.

### `commits.squash` at the landing

| Value | A squash commit carrying `Gov-Squash: union` | A squash commit carrying none |
|---|---|---|
| `re-emit-union` | passes | recorded `squash: lossy`, the push goes on |
| `refuse` | refused, exit 1 before the push | refused, exit 1 before the push |
| `accept-loss` | recorded `squash: lossy` | recorded `squash: lossy` |

Under `refuse` a commit carrying the union still refuses, because the value says a squash does not land. A
lossy record names no key that was lost, since the hook did not run and nothing read them.

### The `carries` value

```
<prior sha>..<landed sha> · <n> commit(s)[ · squash: lossy · <m> commit(s)][ · outside: <k> commit(s)]
<first parent>..<landed sha> · <n> commit(s) · prior-derived
```

`S1`'s value holds no newline, as `render_landing_body` requires, and no commit list.

### Inventory

| Minted | Cell or kind |
|---|---|
| `derive_landing_carries`, `read_landing_carries`, `derive_landing_id`, `print_landing_ids`, `derive_squash_commits`, `check_squash_landing`, `derive_squash_union`, `derive_outside_commits` | `py.function`, `deploy_items.py`, each put to `lexicon.py --suggest` in the build pass |
| `derive_codex_hooks`, `derive_retrust` | `py.function`, `codex_targets.py` |
| `LANDING_RE` | `py.constant` |
| `landing` | `[[native]]` class |
| `Gov-Squash` | `[[trailer]]` key |
| `codex-retrust` | an `orders` row kind |
| `config` | an `[install]` kind |
| `--deploy carries`, `publish` | verbs |

### Rollout

Live at landing: the default `re-emit-union` never refuses, and gov never squashes. Codex's path runs only
where `runtime.harnesses` names `codex`.

### Files touched (estimate)

- `tools/loop/deploy_items.py`, `tools/loop/deploy_fixture.py`
- `tools/unattended/unattended.sh`: `--deploy carries`
- `tools/push-main.sh`: the `check_squash_landing` call at both landing paths
- `.githooks/prepare-commit-msg`: the `squash` arm
- `tools/playbook/namespaces.toml`: the `[[native]]` and `[[trailer]]` rows
- `tools/runtime/harnesses/codex.toml`: `[install]`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`
- `tools/govkit/codex_targets.py` (new)
- `tools/settings-merge.py`: a missing `.codex/hooks.json` seeded
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`
- `help/deploy.md`: `carries`, `publish` and `commits.squash`

### Alternatives rejected

- **`carries` as a stored commit list.** A landing of several hundred commits would make one commit message
  that long, and the list is derivable from an immutable range, so `[derive]` rejects it.
- **`derive_carry_set`.** It answers what rode in through the local default branch, and a clean landing
  answers empty. The test is any ordinary landing.
- **The lander writing the union into its own merge message.** `read_commits` over `--no-merges` never reads
  a merge commit, so the union would sit where the one reader cannot see it.
- **An `OWNER_ITEM_KINDS` row `codex-retrust`.** Scout B proposed it. An item posts to the adopter's mailbox
  refs, which an offer's grant cannot reach, so it fails on the offer, the case that needs it.

## 5. Production-readiness checklist

- security: `publish` refuses a non-`https` URL and any userinfo part, so no credential reaches a record. S9
  reads bytes and runs no target code.
- perf / scale: one `rev-list` and one trailer read at a landing; S6 is bounded at 200 commits.
- error / empty / loading states: a landing with an empty range writes `0 commit(s)`; `prior-derived` says
  the range was derived and not recorded.
- observability: `carries` on the record, and each S4 result printed by the lander.
- risks: a squash with a custom message evades S4, since it carries no marker. S6 then names it only if it
  sits outside a landing, and a squash on a branch with a rewritten message reads as an ordinary commit.
- testing: planted ranges and a planted `SQUASH_MSG`, each key value on its own planted squash.
- migration: N/A — a new field value; old records keep `-`.
- user docs: `help/deploy.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case carries-merges` lands a planted branch of 3 commits and
  one merge, `read_landing` prints `carries` as `<prior>..<sha> · 3 commit(s)` and `read_landing_carries`
  returns those three.
  Red when: the merge is counted, or the range reads `<current default>..HEAD` after the push and is empty.
  figure: 3 is PINNED by the fixture.
- **AC2** — When `--case carries-carry-set` lands a clean branch whose `check_carry_set` answer is empty,
  the value still names its commits; and `--case carries-second-node`, with no local outcome record, writes
  a value ending `prior-derived`.
  Red when: the field follows `check_carry_set`, or a derived range reads as a recorded one.
- **AC3** — When `python deploy_items.py print-landing-ids` runs after a planted landing it prints
  `landing-<12 hex>`, and `--case landing-class` resolves that id and refuses `landing-zz`.
  Red when: an id for no record resolves.
- **AC4** — When `python deploy_items.py publish <sha> https://example.invalid/atlas` runs twice in
  `--case publication`, one `release` record for (`<sha>`, `artifact:https://example.invalid/atlas`) exists
  and the second prints `already recorded`; a plain `http://` URL and one holding a userinfo part `u:p@`
  each exit 2.
  Red when: two records exist, or a credential URL is written.
- **AC5** — When `--case squash-reemit` plants a local `git merge --squash` of two commits with `Pass:`
  trailers under a planted `.governance/policy.toml` reading `commits.squash = "re-emit-union"`, the commit
  carries both `Pass:` values and `Gov-Squash: union`, and the landing passes with no lossy clause.
  Red when: the union drops a key, or the hook changes a message under another value.
- **AC6** — When `--case squash-refuse` plants the same squash under `commits.squash = "refuse"`, `--land`
  exits 1 before the push and the remote's tip does not move.
  Red when: the planted squash lands.
- **AC7** — When `--case squash-accept` plants it under `commits.squash = "accept-loss"`, the landing passes
  and `carries` holds `squash: lossy · 1 commit(s)`; `--case squash-unmarked` under `re-emit-union`, the
  hook skipped, records the same clause.
  Red when: a lost trailer lands with no record of it.
- **AC8** — When `--case squash-hosted` plants one single-parent commit on the remote's default branch
  between two landings, the second landing's `carries` holds `outside: 1 commit(s)` under each value of the
  key.
  Red when: the commit is unnamed, or the landing refuses on it.
- **AC9** — When `python policy.py get commits.squash` runs with no file value it prints `re-emit-union`,
  and `grep -c commits.squash tools/policy/unsummarised-keys.txt` prints 0, with the reader-coverage arm
  counting the literal call in `tools/push-main.sh`.
  Red when: the row has no `summary`, or no literal reader.
- **AC10** — When `python codex_targets.py --fixture --case install` applies a planted hook fragment with
  `runtime.harnesses = ["codex"]`, the scratch tree's `hooks.json` under `.codex/` wires it and it holds no
  `.claude/` file; with `["claude-code", "codex"]` both files wire it.
  Red when: a Codex-only install writes `.claude/`, or two harnesses refuse.
- **AC11** — When `--case trust-install` runs, `apply` prints one `codex — trust step` line per wired hook;
  `--case trust-unchanged` runs `update` with no hook bytes moved, and prints none and adds no `orders` row.
  Red when: the step is silent at install, or fires on an unchanged hook.
- **AC12** — When `--case trust-changed` moves one Codex-installed hook's bytes through `update`, the line
  names that hook and the receipt's `orders` gains one `codex-retrust` row, and `--case trust-offer` runs
  the same under an offer's mode with no target process spawned.
  Red when: a changed hook leaves no attended step, or the check spawns target code.

## 7. Gates

`policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `playbook render selftest` · `settings-merge selftest` · `push-main self-test`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each `--case` above, the failing case `squash-refuse` with the refusal removed · none
New arm: tools/govkit/selftest.py · covers AC10 AC11 AC12 · a scratch target with `runtime.harnesses = ["codex"]`, its failing case a moved hook with no `orders` row · none

## 8. Open questions

- **F1 — Which range is `carries`, given `<current default>..HEAD` is empty once pushed?** Options: (a) read
  the prior tip the lander records; (b) write `carries` before the push; (c) `check_carry_set`, as
  TOOL-dWellOiledMachine-39 §8 F3 assumes. (b) needs a record before a landing exists, and (c) is another
  set. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, the clause's intent held and its literal range
  recorded in deviation 271. widens: none · relaxes: none
- **F2 — What is a "planted squash", when the lander never squashes?** Options: (a) a local
  `git merge --squash`, seen by the hook and at the landing; (b) a hosted squash only; (c) both. (b) cannot
  be refused, and (c) needs S6 as well. RESOLVED (agent, 2026-10-30, delegated): (c), rung 3, the most
  stated cases met. widens: none · relaxes: none
- **F3 — `refuse` over a hosted squash.** The clause says "refused at the landing", and a hosted squash
  never reaches one. Options: (a) record it at the next landing under every value; (b) drop hosted squashes
  from scope; (c) a server-side rule, which is a new surface on a host gov does not own, veto 2. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3; the departure is deviation 272. widens: none · relaxes: none
- **F4 — Two Codex paths and one `settings` kind.** Options: (a) a new kind `config`; (b) a list value on
  `settings`; (c) changing `resolve_install_target`. (b) and (c) amend TOOL-dWellOiledMachine-14 S5.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, S5's table takes a row and its function does not
  change. widens: none · relaxes: none
- **F5 — Attended step or owner item for a re-trust?** The clause admits either. Options: (a) the attended
  step on both verbs; (b) an owner item. (b) cannot reach an adopter from an offer. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 1, the clause's first option. widens: none · relaxes: none
- **F6 — An ask for dWellOiledMachine.** TOOL-dWellOiledMachine-33 S4 says the filler "never runs for a
  merge or squash source". This unit's `squash` arm is a second arm of the same hook. Ask, target
  dWellOiledMachine: accept TOOL-dWellOiledMachine-33 S4's sentence and any fixture over it read "the
  `Gov-*` filler", so a later `squash` arm of the hook meets no contradiction, seen as that unit's criteria
  green with the arm present. RESOLVED (agent, 2026-10-30, delegated): the ask stands, filed by the main
  loop; the arm is built meanwhile, since the sentence is about the filler. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, the spec run.

## 10. Reuse audit

The seams extended: `read_commits` (TOOL-dDeclaredLoop-23 S3) with `landing_prior_tip`; the `[[native]]`
table, `intake-key` (TOOL-dWellOiledMachine-27 S5) the precedent; `record-kind.release`;
`run_fragment_merges` (`tools/govkit/govkit.py:6109`) and `resolve_install_target`.
`python tools/codebase-map/reuse_lookup.py "the commits a landing carried read over the prior tip with no merges"`
ranked name-stem hits only (`read`, `merge`, `build_commit`), so the seams come from scout B's row, verified
at source: `:956`, `:962`, `:1127` and `:548` of `tools/push-main.sh`, and `:6109`, `:6133`, `:7503` and
`:9144` of govkit. Two recall hits disagree with source: research-git-pockets:153 says the lander re-emits
the union, and the lander never squashes; and TOOL-dWellOiledMachine-39 §8 F3 takes `carries` for
`check_carry_set`. Scout B's `OWNER_ITEM_KINDS` row `codex-retrust` is dropped, §4 records why.

Recall terms used: commits.squash re-emit-union trailers carries landing no-merges codex hook trust retrust
publication
