# DEPL-dShippedRelease-7 — the adopter register read and the currency watch: `kits.currency` in each adopter, `kits.adopters` in gov

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 19 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0417@3e86117a whole
**Carries:** node:item.kits.currency
**Carries:** node:item.kits.adopters
**Carries:** node:record-kind.currency
**Carries:** node:policy-key.deploy.currency
**Carries:** node:policy-key.currency.max-behind
**Carries:** node:policy-key.currency.on-behind
**Carries:** node:policy-key.kits.host
**Carries:** node:policy-key.kits.watch-cadence

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

`gap-deploy-04`: adopter currency is unwatched, receipts sat 990 commits behind after six days,
`update` is pull-only and nothing reads an adopter from gov. This unit gives each adopter a cadence
program, `kits.currency`, that counts the releases its receipt is behind gov's remote tag list and
acts on it as `currency.on-behind` says, and gives gov a cadence program, `kits.adopters`, that reads
each register row's committed receipt and reports it, offers an update or records it as
`deploy.currency` says. Both run on `kits.host` per `kits.watch-cadence`, and a read that fails is
`unverified`, never green.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`f4597719`: `tools/runtime/points.toml`, `point.cadence-items`, `cadence.py` and `hosts.py`
(TOOL-dWellOiledMachine-13 S1 to S6, -59 S1 to S3); `raise_owner_item` and `OWNER_ITEM_KINDS`
(TOOL-dWellOiledMachine-48 S1); `read_secret_ref` (TOOL-dWellOiledMachine-17 S4); the item schema and
`check_program` in `tools/loop/` (TOOL-dDeclaredLoop-12 S1, S3); the `[[command]]` row and `new command`
(TOOL-dDeclaredLoop-6 S3); the record-kind registry and `record_kinds.py new` (TOOL-dTotalRecall-1 S9,
-18 S1); `build_step_env` and `derive_pending_steps` (TOOL-dSafePassage-7 S1, -2 S1); the journal
`govkit/shim-calls.jsonl` (TOOL-dSafePassage-6 §4); `resolve_kit_dir`'s inline block, already gated.

- **S1** — The probe block. `tools/lib/remote_probe.py` is the canonical home of
  `read_remote_refs(remote, *patterns, symref=False, cwd=None, timeout=20)`, which runs `git ls-remote`
  bounded and with `GIT_TERMINAL_PROMPT=0`, and returns `(rows, why)`: `rows` a list of `(sha, ref)`
  with `why` empty, or `rows` `None` with `why` naming the cause, beside `derive_release_rows(rows)`,
  which keeps the annotated tags matching `RELEASE_TAG_RE`, unit 3's `TAG_RE` moved here so one grammar
  reaches a tree with no govkit, ordered by (date, `<n>`). It is the second instance of the read
  inside `resolve_measurer_currency` (`tools/govkit/govkit.py:612`, its spawn at `:661` and parse at `:668`),
  so `[reuse]` extracts it. It is carried inline between `# >>> remote_probe_py -- canonical copy:
  remote_probe.py in the gov lib dir (byte-identical; gated)` and `# <<< remote_probe_py`, the shape of
  `remote_ladder_py` (`:555-558`), in `tools/govkit/govkit.py`, `tools/govkit/kit_release.py` and
  `tools/run-gates/check_currency.py`, under one new `PARITY_ROWS` row of
  `tools/lib/resolve-python.test.sh`. `resolve_measurer_currency`
  and `read_remote_tip` (DEPL-dShippedRelease-31 S3, factored from the same read) go through it, the
  first keeping every verdict word and its memo. Observed by AC12.
- **S2** — `kits.currency`, the verb `python check_currency.py measure [--now <utc>]` in the new
  `tools/run-gates/check_currency.py`, which needs no gov checkout, the rule `tools/run-gates/check-receipt.py`
  states for itself. `measure_currency(root, now)` reads the receipt through `read_receipt_release`
  (DEPL-dShippedRelease-25 S7, `tools/run-gates/receipt_fields.py` beside it), reads gov's tags from the receipt's `source_remote` with
  `read_remote_refs(source_remote, "refs/tags/gov/v*")`, orders them with `derive_release_rows`, the
  adopter's form of `read_release_tags` (DEPL-dShippedRelease-3 S1), which needs a gov checkout, and
  derives one verdict of §4 "The verdicts". Under
  `release-tag` the figure is the tags newer than `release`; under `any-commit`, the tags dated after
  the installed commit, by §8 F5. Observed by AC1, AC2, AC4, AC5 and AC6.
- **S3** — The currency record (`record-kind.currency`), `write_currency_record(root, rec)`: one JSON
  file `<git-common-dir>/govkit/currency/<HEAD sha>.json`, keyed by HEAD SHA, shape in §4 "Data
  model", written atomically, never in the working tree and never committed (§8 F1). A row in
  `tools/memory-tree/record-kinds.toml` through `record_kinds.py new currency --tag record.currency
  --writer check_currency.py --check <the S5 leg> --purpose "<line>"`, `home`
  `<git-common-dir>/govkit/currency/*.json`, a form TOOL-dTotalRecall-18 S1 admits. Observed by AC1
  and AC13.
- **S4** — The action past the bound, `derive_on_behind_route(verdict, behind, root)`: within
  `currency.max-behind`, read with `read_policy_value("currency.max-behind", root)`, it does nothing
  further; over it, as `read_policy_value("currency.on-behind", root)` says: `note` prints
  one line; `owner-item` raises one owner item of the new kind `currency-behind` through `python
  owner_items.py raise currency-behind kits-currency --option update --option wait --recommend update
  --key <newest tag>`, found through `resolve_kit_dir("runtime", "owner_items.py", here)`, so a second
  run at the same newest tag is the mailbox's duplicate; `red` raises nothing and leaves the record
  for S5's leg. An absent runtime kit prints `currency — owner item not raised: no runtime kit` and
  exits 0. Observed by AC2 and AC3.
- **S5** — The leg. `check_currency_leg(root)`, `python check_currency.py --leg`, reads the record for
  HEAD, else the nearest ancestor's, offline. It runs only under `currency.on-behind = "red"`, printing
  `currency — not armed: currency.on-behind is <value>` and exiting 0 otherwise. Armed, it reds on a
  record over `currency.max-behind`, passes a `source` record as "source, 0 behind", and reds on no
  record or an `unverified` one as a dead probe. A receipt-free tree prints `not installed: no receipt,
  currency unmeasured` and exits 0. A `[[gate_leg]]` row `currency (releases behind gov)` in
  `tools/run-gates/kit.toml`, through `leg_factory.py new`, rendered into `tools/gate-legs.json`,
  `subject = "repo"`, `guard = []`. Observed by AC3 and AC7.
- **S6** — What only the adopter can read. `measure` counts `<git-common-dir>/govkit/shim-calls.jsonl`
  through `read_shim_calls(root)` into the record's `shim_calls`, and the receipt's `steps` rows not
  `applied` into `steps_unapplied`. The journal is under the git directory (TOOL-dSafePassage-6 §8 F3),
  which no remote read reaches, so gov's `adopters` record states `shim_calls: unread`, deviation 252
  of DEPL-dShippedRelease-25; gov alone holds the declared steps, so `steps-pending` is its figure and
  `steps_unapplied` the adopter's. Observed by AC11.
- **S7** — `kits.adopters`, `python adopter_reading.py read [--key <key>]` in the new
  `tools/govkit/adopter_reading.py`. For each row of `read_adopter_rows(root)` (DEPL-dShippedRelease-31
  S2, I6's `adopter_rows`), `read_adopter_reading(row, tags, scratch)` reads the committed receipt at
  the row's `remote` and `branch` through `load_committed_receipt` (§4 "The remote read"), and fills
  the record's fields, §4 "Data model": `behind` per kit through `resolve_entry_version_at`
  (`tools/govkit/govkit.py:696`) over the span of `read_release_tags()`, `steps-pending` through
  `derive_pending_steps`, and `reading`. A row whose `registered` is false reads `unregistered` and
  fetches nothing; a remote or a receipt it cannot read reads `unverified`. Observed by AC8 and AC10.
- **S8** — The route, `derive_adopter_route(reading, value, row)`, as `deploy.currency` says, §4 "The
  route": `pull-and-watch` reports, `push-branches` runs `kits.offer` for the row, `pull-only` records
  only. The value is one gov policy value read with `read_policy_value("deploy.currency", root)`, and
  `push-branches` offers only a row whose `grant` reads `branch-push`, so an adopter consents by its row
  (§8 F2). `write_adopter_record(key, rec)` writes each reading on the ref `refs/gov/adopters/<key>`
  (DEPL-dShippedRelease-31 S4) through `write_gov_ref` and `build_gov_commit` (TOOL-dPlacedRequest-11 S1,
  S2), parented on the tip, one commit per (key, release), so a second node reads it. A report raises
  one owner item of the new kind `adopter-behind` over `currency.max-behind`, keyed `<key> <newest
  tag>`. Observed by AC10.
- **S9** — The cadence. Two `[[adapter]]` rows at `point.cadence-items` in `tools/runtime/points.toml`:
  `kits-currency`, `run` `check_currency.py tick`, and `kits-adopters`, `run` `check_currency.py
  adopters`, a dispatcher that resolves `adopter_reading.py` through `resolve_kit_dir("govkit",
  "adopter_reading.py", here)` and prints `kits.adopters — not installed: no adopter register here` where
  it is absent, because the row ships to every adopter and govkit does not. Each carries `host-key =
  "kits.host"`, `period = "daily"`, the finest period TOOL-dWellOiledMachine-59 S1 admits, and `events =
  []`. The program applies `kits.watch-cadence` itself, §4 "The cadence", read with
  `read_policy_value("kits.watch-cadence", root)`, and states the `kits.host` value it ran under, read
  with `read_policy_value("kits.host", root)`, on the record. `every-session` runs through §8 F4's line
  in `tools/runtime/session-tick.sh`. Observed by AC8 and AC9.
- **S10** — The rows. `[[item]]` rows `item.kits.currency` and `item.kits.adopters` in
  `tools/loop/loop.toml`, §4 "The items"; `[[command]]` rows `kits.currency` in
  `tools/run-gates/kit.toml` and `kits.adopters` in the govkit descriptor (DEPL-dShippedRelease-21) by
  `new command`; `currency-behind` and `adopter-behind` in `OWNER_ITEM_KINDS`. Observed by AC13.
- **S11** — The five catalogue rows (`tools/policy/catalogue.toml:1034`, `:1040`, `:1046`, `:1089`,
  `:1095`) gain `summary` and `usage`; their `allowed` and `default` stay as written, and `python
  tools/policy/policy.py lists --write` drains the five names from
  `tools/policy/unsummarised-keys.txt`. Observed by AC14.
- **S12** — The page `help/currency.md`, linked from `help/README.md`: what the two programs read, each
  value of the five keys, what `unverified` means, and how to run `measure` before the leg in a CI job.
  Observed by AC15.

## 3. Non-goals (OUT)

- The register's rows, the `adopters` kind's row, the registration verb and `read_adopter_rows`:
  DEPL-dShippedRelease-31.
- `release`, `source_remote` and `read_receipt_release`: DEPL-dShippedRelease-25.
- The cut, the tag and `read_release_tags`: DEPL-dShippedRelease-3.
- `kits.offer`'s run: DEPL-dShippedRelease-16. This unit calls it and writes the route.
- The `session-start` host row and its hook: DEPL-dShippedRelease-3 S7 registers them (the brief's C10);
  this unit reads the row and adds one line to the hook's script.
- A per-kit distance in the adopter's own record: §8 F3.
- A fetch of gov's objects into an adopter. `measure` reads an advertisement and nothing else.

### Edges

- **consumes-from** `DEPL-dShippedRelease-31` — `read_adopter_rows`, I6's `adopter_rows`, the one register reader S7 walks, with `registered`, the rows' `remote`, `branch` and `grant`, and the `adopters` record's home
- **consumes-from** `DEPL-dShippedRelease-3` — `read_release_tags`, the tag list and order S2 and S7 count over, and `session-start`, the default host S9 reads
- **consumes-from** `DEPL-dShippedRelease-25` — `read_receipt_release`, the receipt's `release`, `source_remote` and `install_from`, without which "releases behind" is undefined
- **hands-off** `DEPL-dShippedRelease-16` — `adopter_reading.py`, whose route runs `kits.offer` for one row and whose `load_committed_receipt` credential path S4 of that unit reuses
- **consumes-from** external — TOOL-dWellOiledMachine-13, -17, -48 and -59, TOOL-dDeclaredLoop-6 and -12, TOOL-dTotalRecall-1 and -18, TOOL-dSafePassage-2, -6 and -7, each specced and unbuilt at base `f4597719`

## 4. Design

### Evidence

Read at `5d1c82ac0`; no product file differs from base `f4597719`.

- `resolve_measurer_currency` (`tools/govkit/govkit.py:612`) is the one `ls-remote` read of a remote's
  state, with the rule that a dead probe is `unverified`. `tools/govkit/census.py:122` needs an adopter
  checkout, so it is shape reference only.
- `tools/run-gates/check-receipt.py` reads the receipt with no gov checkout; its leg is
  `tools/run-gates/kit.toml:155-159`. `run-gates` is engine `**` (`kit.toml:17-19`), so a new file ships.
- `tools/govkit/adopters.toml:17-25` holds three rows with `key` and `names` only, and arm 10 reads it
  at `tools/govkit/govkit.py:3742`. It sits under the govkit exemption, so nothing there ships.
- The five keys: `tools/policy/catalogue.toml:1034`, `:1040`, `:1046`, `:1089`, `:1095`, each on
  `tools/policy/unsummarised-keys.txt` (`:40`, `:41`, `:43`, `:92`, `:93`).
- A record home may be `<git-common-dir>/<glob>` (TOOL-dTotalRecall-18 §4), and the reader-coverage
  arm counts a call whose first argument is the key literal (`tools/policy/check_policy.py:423-428`).
- A `kit.toml` may not import a sibling kit, and `tools/run-gates/` holds no policy read, so
  `read_policy_value(key, root)` here is the same subprocess TOOL-dMindYourWords-1 S5 runs: `policy.py
  get <key>` found through `resolve_kit_dir`, an absent kit giving the catalogue default with a notice.

### Data model

```json
{"schema": 1, "head": "<HEAD sha>", "at": "<utc>", "host": "<kits.host value>",
 "verdict": "level|within|over|source|unverified", "behind": 3,
 "release": "<receipt release or null>", "newest": "<newest tag or null>",
 "install_from": "release-tag|any-commit|source", "kits": ["<id>"], "shim_calls": 0,
 "steps_unapplied": 0, "reason": "<why, on unverified>"}
```

`behind` is `null` on `unverified` and `source`. `kits` lists the receipt's kits (§8 F3).

The `adopters` record holds DEPL-dShippedRelease-31 §4's six fields, `key`, `release`, `receipt-sha`,
`behind`, `steps-pending` and `reading`, with `behind` a map of kit to the releases in the span that
moved its version, and adds `releases` (the span's length, which the route and `currency.max-behind`
read), `route` and `shim_calls`, always `unread`. DEPL-dShippedRelease-16 and -20 add `offer`, `order`
and `orders_open`.

### The verdicts

| Verdict | When | Green at the leg |
|---|---|---|
| `source` | `read_receipt_release` answers `install_from` `source` (DI-1), read with no remote call | yes, "source, 0 behind" |
| `level` | `behind` is 0 | yes |
| `within` | `behind` is at or under `currency.max-behind` | yes |
| `over` | `behind` is above it | no |
| `unverified` | no receipt field to count from, the remote did not answer, it lists no release tag, or the receipt's `release` is not in its list | no, a dead probe |

An empty tag list is `unverified`, never `level`: zero tags and zero behind cannot be told apart
(`[gate]`). While no tag exists, every adopter reads `unverified` with that reason, which is the truth.

### The remote read

`load_committed_receipt(row, scratch)` makes a bare repository under `scratch`, runs `git fetch --depth=1
--no-tags <remote> refs/heads/<branch>` there under `build_step_env(scratch)`, and returns the parsed
`FETCH_HEAD:.governance/install.json` with the fetched SHA. A shallow fetch is the one read every host
serves; `git archive --remote` is not (§4 "Alternatives rejected"). `build_step_env` empties the
environment and the credential helper. A register row holds a scope and never a value
(DEPL-dShippedRelease-31 S1), so the secret's reference is derived, `adopter-<key>`. Where
`read_secret_ref` resolves it, the row gets one helper back, `credential.helper=!<python> <this file>
credential adopter-<key>`, set through `GIT_CONFIG_COUNT`, so the value crosses to git over the helper's
stdout and never by argv, environment or file: `read_secret_ref` runs inside that helper process. An
unresolved reference reads anonymously, which a public remote serves and a private one refuses as
`unverified`.

### The route

| `deploy.currency` | `level`, `within` | `over` | `unverified` |
|---|---|---|---|
| `pull-and-watch` (default) | reported | reported, one `adopter-behind` item | reported, one item |
| `push-branches`, `grant` is `branch-push` | reported | `kits.offer`, once per (key, newest tag) | reported, one item, never offered |
| `push-branches`, `grant` is `read` | reported | reported, one item, reason `read grant` | reported, one item |
| `pull-only` | recorded | recorded | recorded |

An `unregistered` row is recorded under every value and raises nothing. "Reported" is one line on the tick's output and `route = reported` on the record. An already-recorded
(key, newest tag) with `route = offered` on the ref's tip is not offered again, so a daily tick does
not re-push.

### The cadence

`tick` reads `kits.watch-cadence`: `daily` measures; `weekly` measures when the newest record's `at`
falls in an earlier ISO week than now, by `date.isocalendar()`, the form `derive_period` uses; and
`every-session` measures. A cadence row's period witness caps the tick at one run a day (TOOL-dWellOiledMachine-13 S6),
so a second session that day reaches `measure` by §8 F4's entry alone.

### The items

```toml
[[item]]
tag = "item.kits.currency"
program = "kits"
actor = "command:kits.currency"
needs = []
inputs = ["layer.distribution:the receipt and gov's remote tag list"]
allowance = "the git common directory's currency record"
returns = "record-kind.currency"
outcomes = ["within", "over", "unverified"]
witness = { class = "history", by = "the currency record, keyed by HEAD SHA" }
owner = "dShippedRelease"
[item.routes]
within = "end"
over = "end"
unverified = "end"
```

`item.kits.adopters` has the same shape: actor `command:kits.adopters`, `returns =
"record-kind.adopters"`, `outcomes = ["reported", "offered", "recorded", "unverified"]`, `offered =
"item.kits.offer"` and the rest `end`, witness "the adopter record, per release". `program = "kits"`
and the target `end` are §8 F6's ask, the one TOOL-dLinkedLibrary-8 §8 F2 and F5 file for `adopt`.

### Inventory

Minted: `tools/lib/remote_probe.py` with `read_remote_refs`, `derive_release_rows` and `RELEASE_TAG_RE`;
the parity marker `remote_probe_py`;
`tools/run-gates/check_currency.py` with `measure_currency`, `write_currency_record`,
`read_currency_record`, `derive_on_behind_route`, `check_currency_leg`, `read_shim_calls` and
`read_policy_value`, its verbs `measure`, `tick`, `adopters`, `session`, `--leg`, `--fixture`, `--plant`;
`tools/govkit/adopter_reading.py` with `read_adopter_reading`, `load_committed_receipt`,
`derive_adopter_route`, `write_adopter_record`, its verbs `read`, `credential`, `--fixture`, `--plant`;
the owner-item kinds `currency-behind`, `adopter-behind`; the leg `currency (releases behind gov)`.
Naming cell `py.function`: each OK by `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at `5d1c82ac`; `route_*` and `fetch_*` were asked first and refused, so the names above
are the ones the lexicon admits.

### Migration

Additive. A receipt below schema 5 has no `source_remote`, so `measure` reads `unverified` with that
reason until DEPL-dShippedRelease-25's step runs. No conf or receipt field changes here.

### Rollout

Landing arms nothing until a `session-start` host row exists and a release tag does. Gov's own receipt
is source mode, so gov's tick reads `source`.

### Files touched (estimate)

- `tools/lib/remote_probe.py` (new), `tools/lib/resolve-python.test.sh`: S1
- `tools/govkit/govkit.py`: S1, the inline block and the re-point
- `tools/run-gates/check_currency.py` (new), `tools/run-gates/kit.toml`: S2 to S6, S9, S10
- `tools/gate-legs.json`: rendered by `tools/run-gates/leg_factory.py` from the declaration
- `tools/run-gates/ceiling-evidence.txt`: the new leg's first clean reading
- `tools/runtime/session-tick.sh`, `tools/govkit/kit_release.py`: §8 F4, S1
- `tools/govkit/adopter_reading.py` (new), `tools/govkit/selftest.py`: S7, S8
- `tools/runtime/points.toml`, `tools/runtime/owner_items.py`: S9, S10
- `tools/loop/loop.toml`: S10
- `tools/memory-tree/record-kinds.toml`: S3
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S11
- `tools/run-gates/README.md`, `help/currency.md` (new), `help/README.md`: S12

### Alternatives rejected

- **`git archive --remote` for the receipt.** Rejected by a read of research-distribution-b `:125`, which
  proposes the shallow fetch, and because GitHub's smart HTTP refuses `upload-archive`. UNVERIFIED by a
  live call in this pass; the shallow fetch does not depend on it.
- **A live read inside the leg.** It would make a bar leg depend on the network on every landing, and
  layer-expansions:465 reads the record offline.
- **Reading through `census.py`.** `tools/govkit/census.py:122` needs the adopter's working tree.
- **A per-row `channel` field for `deploy.currency`.** research-distribution-a's shape, rejected by
  §8 F2: `grant` is already the row's consent, and a second field is a second answer.
- **A `secret` field on a register row.** Rejected by DEPL-dShippedRelease-31 S1, whose `grant` is a
  scope; a derived reference needs no field.

## 5. Production-readiness checklist

- security — `measure` makes one anonymous read of a public advertisement and writes only under the
  git directory. `adopter_reading.py` reads under an emptied environment, a secret crossing only through
  the helper's pipe. `source_remote` is a value from a committed receipt, passed as one argv element, so
  a shell never sees it; a value starting `-` or naming a local path is `unverified`.
- perf / scale — one `ls-remote` per tick per adopter tree; one shallow fetch per register row per tick.
- error / empty / loading states — no receipt is an announced skip; no tag, a dead remote and an unknown
  `release` are `unverified`; an absent policy or runtime kit prints its line and runs on the default.
- observability — `measure` prints one line on every path; every path writes the record.
- risks — under `red` a fresh CI clone holds no record, so the leg reds until the job runs `measure`
  first, which `help/currency.md` states. A record is per clone, so two nodes measure separately, and
  nothing compares them.
- testing — the arms of §7, each a scratch repository with a bare remote and planted tags.
- migration — §4 "Migration".
- user docs — `help/currency.md`.

## 6. Acceptance criteria

- **AC1** — When `python check_currency.py --fixture --plant behind-3` runs over a scratch adopter whose
  receipt names the oldest of four release tags on a bare remote, it prints `behind 3` and the
  git directory holds the record named for HEAD with `verdict` `over`, and `git status --porcelain` in
  the scratch prints nothing.
  Red when: the count is off by one, the record lands in the tree, or no record is written.
- **AC2** — When `python check_currency.py --fixture --plant max-behind-<v>` runs for each of `0`, `1`,
  `2` and `4` over a committed `.governance/policy.toml` naming that `currency.max-behind`, an adopter
  one tag behind reads `over` under `0` and `within` under the rest, and one five behind reads `over`
  under all four; with no policy file the bound reads `2`.
  Red when: a value is ignored, or the default is not the catalogue's.
- **AC3** — When `--plant on-behind-note`, `on-behind-owner-item` and `on-behind-red` each run over an
  `over` record, the first prints one line and raises nothing, the second posts one stubbed
  `owner_items.py raise currency-behind` and a second run at the same newest tag posts none, and under
  the third `python check_currency.py --leg` exits 1 naming the count; under `note` the leg prints
  `currency — not armed` and exits 0.
  Red when: `red` reds with no record over the bound, or `owner-item` raises twice for one tag.
- **AC4** — When `python check_currency.py --fixture --plant dead-remote`, `no-tags` and `unknown-release`
  run, each record reads `unverified` with a named `reason`, `behind` `null`.
  Red when: any reads `level` or `within`, which is a dead probe or an empty population read as green.
- **AC5** — When `--plant source-mode` runs over a receipt with `install_from` `source`, it prints `source,
  0 behind`, makes no remote call (the plant's remote is unreachable) and `--leg` under `red` exits 0.
  Red when: a source receipt spawns `ls-remote`, or reads `unverified`.
- **AC6** — When `--plant any-commit` runs over a receipt with `install_from` `any-commit` and tags dated
  before and after the commit that last wrote the receipt, `behind` counts only the later tags.
  Red when: every tag counts, or the plant reads `unverified`.
- **AC7** — When `python check_currency.py --leg` runs under `red` with no record on the tree, it exits 1
  naming the dead probe; with the record on HEAD's parent only, it grades that record.
  Red when: an absent record passes, or the leg spawns `git ls-remote` (the plant's `PATH` shim for `git`
  logs each spawn, and a spawn reds).
- **AC8** — When `python check_currency.py --fixture --plant watch-daily`, `watch-weekly` and
  `watch-every-session` run, `tick` measures twice over two days under `daily`, once over two days of
  one ISO week under `weekly`, and `session` measures twice in a day under `every-session` and does
  nothing under the other two.
  Red when: `weekly` runs daily, or `every-session` reads as `daily`.
  fixture: `tick` runs directly with `--now`; the cadence row's witness is TOOL-dWellOiledMachine-13's.
- **AC9** — When `--plant host-session-start`, `host-os-scheduler`, `host-cloud-routine` and
  `host-registered` each commit that `kits.host` value and run `tick`, the record's `host` carries it;
  and when `python cadence.py tick --dry-run` runs under `host-cloud-routine` with no such host row, it
  prints `not ready` for `kits-currency` and runs nothing.
  Red when: a record carries another value, or an unregistered host runs the row.
  fixture: `cadence.py` and `hosts.py` as TOOL-dWellOiledMachine-59 builds them.
- **AC10** — When `python adopter_reading.py --fixture --plant currency-<v>` runs for `pull-and-watch`,
  `push-branches` and `pull-only` over a register of four rows (one `over` with `branch-push`, one `over`
  with `read`, one whose remote is gone, one unregistered), the `pull-and-watch` run reports three and
  raises three `adopter-behind` items, the `push-branches` run offers only the first through a stub and
  never the dead one, and the `pull-only` run prints nothing and leaves four commits, one per row, under
  `refs/gov/adopters`, each with `route` `recorded`.
  Red when: a dead remote is offered, a `read` row is offered, or `pull-only` reports.
- **AC11** — When `python check_currency.py --fixture --plant shim-calls` runs with two lines in the git
  directory's `shim-calls.jsonl` and one `failed` row in the receipt's `steps`, the record's `shim_calls`
  is `2` and `steps_unapplied` is `1`; and when `python adopter_reading.py --fixture --plant reading` reads
  that adopter's remote, its record reads `shim_calls: unread` and a `steps-pending` figure.
  Red when: gov's record states a number it cannot have read.
- **AC12** — When `python tools/govkit/govkit.py update --target <a fixture> --to HEAD` runs against a
  scratch gov with a dead remote, it prints the `unverified` line it prints today, naming the remote;
  and `grep -c "remote_probe_py" tools/lib/resolve-python.test.sh` prints `1`.
  Red when: the re-point changes a verdict word, or the copy has no parity row.
- **AC13** — When `python loop_lib.py --check` and `python cadence.py --check` run, both pass with
  `item.kits.currency`, `item.kits.adopters`, `kits-currency` and `kits-adopters` in their output, and
  `python record_kinds.py --check` names `record-kind.currency`.
  Red when: a route names no item, or the row's `host-key` has no catalogue row.
- **AC14** — When `python tools/policy/policy.py get deploy.currency` and the same for
  `currency.max-behind`, `currency.on-behind`, `kits.host` and `kits.watch-cadence` run, each prints its
  catalogue default, `grep -cE "^(deploy\.currency|currency\.|kits\.host|kits\.watch)"
  tools/policy/unsummarised-keys.txt` prints `0`, and `grep -c read_policy_value check_currency.py
  adopter_reading.py` counts a literal call of each of the five keys.
  Red when: a name stays listed, a key has no literal reader, or a row's `allowed` moved.
- **AC15** — When `grep -c kits.watch-cadence currency.md` runs from the `help` directory it prints at
  least `1`, and `help/README.md` links the page.
  Red when: the page is absent or a value is unstated.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `run-gates adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `policy check` · `policy fixtures` · `memory hygiene`

New arm: tools/run-gates/check_currency.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC11 · `--selftest` over every plant, its failing case the `no-tags` plant read `level` · none
New arm: tools/govkit/selftest.py · covers AC10 · `adopter_reading.py --fixture` under each `deploy.currency` value, its failing case a dead remote offered · none
New arm: tools/lib/resolve-python.test.sh · covers AC12 · the `remote_probe_py` row, its failing case a one-byte edit in `check_currency.py`'s copy · none

## 8. Open questions

- **F1 — Is the currency record committed?** layer-expansions:465 reads "the newest committed currency
  record", and a `session-start` run cannot land a commit in an adopter. Options: (a) a tracked
  `.governance/currency.json`, landed by whoever commits next; (b) a file under the git common
  directory; (c) a ref `refs/gov/currency/<sha>` through `write_gov_ref`. (a) dirties the tree on every
  probe, and `update`'s claimed-path checks and a lander's clean-tree rule then meet it. (c) needs the
  gov-ref block and a push from every adopter's session, which the run-gates kit does not carry. (b) is
  where this deployer already keeps state that must not dirty a tree (TOOL-dSafePassage-6 §8 F3) and
  costs a CI job one `measure` step. v2's clause names no home, so it is not a departure. RESOLVED
  (agent, 2026-10-30, delegated): (b), rung 3, the only option that runs on the default host. widens: none · relaxes: none
- **F2 — Is `deploy.currency` one value or per row?** Options: (a) one gov value; (b) a per-row
  `channel`; (c) one value, `push-branches` reaching only a row whose `grant` reads `branch-push`. Under
  (a) a preset setting `push-branches` would push to every adopter. (b) adds a field I6 does not spell.
  (c) makes the row's `grant` the adopter's consent, and DEPL-dShippedRelease-16 needs that scope anyway.
  RESOLVED (agent, 2026-10-30, delegated): (c), rung 3, most feature-rich with no new field. widens: none · relaxes: none
- **F3 — "Releases behind, per kit" (layer-expansions:458).** A product tag is one release, and which
  kit a release moved is in gov's history, which `ls-remote` does not return. Options in the adopter:
  (a) one figure with the receipt's `kits` listed; (b) fetch each tag into the adopter. (b) writes gov's
  objects into an adopter's repository on every probe, and `currency.max-behind` counts releases, not
  kits. RESOLVED (agent, 2026-10-30, delegated): (a) in `kits.currency`, rung 3, v2's clause not saying
  per kit; gov's `kits.adopters`, which holds the history, fills `behind` per kit, as
  DEPL-dShippedRelease-31 §4's field states. widens: none · relaxes: none
- **F4 — How `every-session` runs.** TOOL-dWellOiledMachine-59 S1 admits `daily` and `weekly`, and a
  cadence row's witness stops a second run that day (scout D fork 14, the brief's C10). Options: (a) ask
  for a `session` period kind and hold the value until it lands; (b) this build's own entry, the shape
  DEPL-dShippedRelease-3 S7 and S8 give `kits_cut.py session`: `tools/runtime/session-tick.sh` gains one
  line, `python check_currency.py session`, found through `resolve_kit_dir`, which reads `kits.host` and
  `kits.watch-cadence` and measures only when they read `session-start` and `every-session`; (c) a
  fragment of this unit's own, which wires a second hook for one line. (a) leaves a declared value dead
  at landing, against the clause's "each value seen". RESOLVED (agent, 2026-10-30, delegated): (b), rung
  3, with the extension offered back by the ask below. widens: none · relaxes: none
- **F5 — What `any-commit` counts from.** layer-expansions:458 says tags dated after the installed
  commit, and an adopter holds no gov object to date it. Options: (a) fetch `gov_commit` to date it; (b)
  the date of the adopter commit that last changed `.governance/install.json`, `git log -1 --format=%cs`;
  (c) a new receipt date field. (a) writes gov's objects here and (c) is DEPL-dShippedRelease-25's list,
  which holds none. (b) is at or after the installed commit, so it can undercount by the landing's lag
  and never overcounts. RESOLVED (agent, 2026-10-30, delegated): (b), rung 3. widens: none · relaxes: none
- **F6 — The ask this unit's rows need.** `item.kits.*` names no step, and `check_program` admits a
  route only to a declared item, `transition` or `stand-in`. RESOLVED (agent, 2026-10-30, delegated):
  `program = "kits"` and route target `end`, as TOOL-dLinkedLibrary-8 §8 F2 and F5 ask for `adopt`, rung
  3. Ask for dDeclaredLoop, its `BACKLOG.md`: "a `kits` program's item rows name a program and route a
  terminal outcome to `end`" · accept `check_program` passes `item.kits.currency`, seen red on a row
  naming neither a step nor a program. A second ask for dWellOiledMachine, its `BACKLOG.md`, joined with
  DEPL-dShippedRelease-3 §8 F3's: "a `session` period kind for cadence rows" · accept `derive_period`
  admits it and the `session` verbs can go, seen on a row with `period = "session"`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 7, layer-expansions:458-467, :470-477,
  scout D's unit 7 row, its disagreements 4, 10, 11 and 14, its forks 2, 3, 11 and 14, and the brief's
  C10 and I6, I15, I16.

## 10. Reuse audit

The seams extended are `resolve_measurer_currency` (`tools/govkit/govkit.py:612`) for the probe, whose
read moves into `tools/lib/` as the second instance, on the `remote_ladder_py` pattern (`:555-558`);
`tools/run-gates/check-receipt.py` as the sibling that needs no gov checkout, with its leg at
`tools/run-gates/kit.toml:155`; `tools/govkit/adopters.toml` through `read_adopter_rows`; and
`point.cadence-items` for the schedule. `python tools/codebase-map/reuse_lookup.py "read an adopter's
committed receipt from its remote and report releases behind"` ranked name-stem helpers (`read`,
`read_text`, `report`, `read_descriptors`) and no currency code, which agrees with scout D that none
exists; the seams above come from reading source. Scout D's rows held at `5d1c82ac0`, with
`resolve_measurer_currency`'s spawn at `:661` rather than the cited `:612`, which is its definition.
Its disagreement 4 is S6; disagreement 10 and 11 are §8 F4 and the consumes-from on
DEPL-dShippedRelease-3. Recall surfaced `gap-deploy-04`'s own records and the skeptic's C5-F1, which
DEPL-dShippedRelease-25 closes.

Recall terms used: `python tools/memory-recall/query.py "how is adopter currency measured, which adopter is behind and who reports it" --terms "adopter currency receipt releases behind ls-remote kits.currency adopters.toml register pull-and-watch unverified"`
