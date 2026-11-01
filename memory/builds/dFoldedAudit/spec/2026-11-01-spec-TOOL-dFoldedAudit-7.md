# TOOL-dFoldedAudit-7 — policy keys switch the disposal, the stop and the ceiling

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base 74274869 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-7-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-7-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-7-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-7-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-7-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-7-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Three catalogue keys carry the new spec-audit rules as their defaults and the old rule as an allowed
value, and one dated conf key keeps a run preflighted before this build lands under the old rule. Every
later unit of this build reads one switch instead of coding one rule.

## 2. Scope (IN)

- **S1** — Three `[[key]]` rows in `tools/policy/catalogue.toml`, `review.spec-audit.disposal`,
  `review.spec-audit.chain-stop` and `review.spec-audit.chain-ceiling`, each with `summary` and
  `usage`, the ceiling row with `direction`. Observed by AC1 and AC6.
- **S2** — `read_spec_audit_switch` in `tools/unattended/unattended.sh`, the driver's one reader of
  the three keys, called on demand and never by `load_driver_conf`. Observed by AC2, AC3 and AC8.
- **S3** — Three kit-default constants beside `SPEC_COUNTS_CUTOFF`, which the reader answers with
  when no policy kit resolves, held to the catalogue's defaults. Observed by AC4 and AC5.
- **S4** — The conf key `SPEC_FOLD_CUTOFF`, declared blank in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`, initialised in the driver's conf block and refused at
  load when it is not an ISO date. Observed by AC6 and AC7.
- **S5** — `.governance/policy.json` re-rendered in a commit of its own after the catalogue commit.
  Observed by AC9.

## 3. Non-goals (OUT)

- The branch that uses the switch. `--review`'s fold refusal, the row and check 2 are
  `TOOL-dFoldedAudit-2`'s, so the refusal half of the brief's acceptance line 7 is observed there.
- Reading the cutoff against a record. Which runs are past it is `TOOL-dFoldedAudit-2`'s.
- The chain verdict, which is `TOOL-dFoldedAudit-5`'s. It reads the stop and the ceiling.
- A conf key for any switch. An adopter without the policy kit takes the kit defaults, and a blank
  `SPEC_FOLD_CUTOFF` is how that adopter keeps the old rule.
- Check 2's import of the new key: `tools/unattended/check-unattended.sh` is
  `TOOL-dFoldedAudit-2`'s file.
- Prose. `UNATTENDED-PROTOCOL`'s key table and the method text are `TOOL-dFoldedAudit-1`'s.
- No kit version moves by hand. A branch owes no bump, because the lander mints each version at the
  landing (`tools/push-main.sh:26-31`).

### Edges

- **hands-off** `TOOL-dFoldedAudit-2` — reads `read_spec_audit_switch disposal` and `SPEC_FOLD_CUTOFF` at a spec exit, and imports the key into check 2
- **hands-off** `TOOL-dFoldedAudit-3` — the DISPOSAL stage takes the disposal switch's two values and their meaning from this unit's rows
- **hands-off** `TOOL-dFoldedAudit-5` — reads `read_spec_audit_switch chain-stop` and `read_spec_audit_switch chain-ceiling` in the chain verdict
- **hands-off** `TOOL-dFoldedAudit-1` — the three key names, their defaults, and the protocol key-table row check 22 owes for `SPEC_FOLD_CUTOFF`
- **hands-off** external — the close writes the landing date into `.unattended.conf`'s `SPEC_FOLD_CUTOFF`, after §5 risks' read of every ref shows no run but this build's began on or after that date; a hit parks the close, because that record would read as past the cutoff

## 4. Design

### The three keys

| Key | `allowed` | Default | The old rule | Read by |
|---|---|---|---|---|
| `review.spec-audit.disposal` | `["by-nature", "promote-all"]` | `by-nature` | `promote-all`, the refusal of `fold` included | `TOOL-dFoldedAudit-2`, and the caller that hands `TOOL-dFoldedAudit-3` its `disposal` arg |
| `review.spec-audit.chain-stop` | `["own-work", "clean-only"]` | `own-work` | `clean-only`, R1 alone | `TOOL-dFoldedAudit-5` |
| `review.spec-audit.chain-ceiling` | `{ type = "round-count", min = 1 }` | `4` | none: a bound, and the old rule had no chain bound | `TOOL-dFoldedAudit-5` |

**Names.** The `review.` family holds every review key (`tools/policy/catalogue.toml:710-748`). The
`spec-audit` segment is M4's word for the act, and `review.design.rounds` is deliberately not reused:
it counts one subject's rounds, where these bind a chain of subjects. No placeholder row matches a
name: `review.<stage>` (`:1206`) has two segments and `review.<stage>.effort` (`:1212`) ends in
`effort`, so each new row is an exact name. At BASE,
`python tools/policy/policy.py get review.spec-audit.disposal` exits 2 with `is not a catalogue key`.

**Homes.** The switches live in `.governance/policy.toml`, and `REVIEW_ROUNDS`'s registration cannot
be copied. That key is a line in `.unattended.conf` with a row at
`tools/policy/legacy-homes.txt:106`, and that list is shrink-only: `tools/policy/policy.py:1285`
refuses a new `.unattended.conf` key as `is a new legacy home and the list is shrink-only`, and tells
the author to carry it as a catalogue key. `RETROFIT_KEY` (`:1125`) exempts a key ending `_CUTOFF`, so the
cutoff alone stays a conf key. The policy home also gives the ceiling the owner-only property that
check 19 gives `REVIEW_ROUNDS` by hand (`tools/unattended/check-unattended.sh:2737`): the file is on
`tools/policy/guarded-paths.txt` and the reader takes the landed revision, so a run cannot raise its
own ceiling.

```toml
[[key]]
name = "review.spec-audit.disposal"
allowed = ["by-nature", "promote-all"]
default = "by-nature"
summary = "How a spec audit disposes a confirmed finding: fold local fixes and promote new mechanisms, or promote every finding."
usage = 'review.spec-audit.disposal = "promote-all"'
owner = "dFoldedAudit"

[[key]]
name = "review.spec-audit.chain-stop"
allowed = ["own-work", "clean-only"]
default = "own-work"
summary = "When a spec-audit chain stops: on a clean round or a round whose highs all sit in the prior round's own work, or on a clean round alone."
usage = 'review.spec-audit.chain-stop = "clean-only"'
owner = "dFoldedAudit"

[[key]]
name = "review.spec-audit.chain-ceiling"
allowed = { type = "round-count", min = 1 }
default = 4
summary = "The chain round at which a spec-audit chain neither stop has ended holds for the owner."
usage = 'review.spec-audit.chain-ceiling = 6'
owner = "dFoldedAudit"
direction = "raise-loosens"
```

The rows sit after `review.max-rounds` (`:723`). `direction` is required: `round-count` is in
`LOOP_BOUND_TYPES`, so `check_direction` selects the row (`tools/policy/README.md:83`). Because each
row carries both `summary` and `usage`, `tools/policy/unsummarised-keys.txt` does not grow. The
catalogue's header says each row is a row of the design's `[policies]` table; these three are not, so
a comment above them names this unit. No check joins the two (`[policies]` appears in no `.py`, `.sh`
or `.js` under `tools/`).

### The reader

```bash
read_spec_audit_switch() { # disposal|chain-stop|chain-ceiling -> the value on stdout; 1 and the refusal on stdout
```

It carries no `fail`: each caller turns status 1 into its own refusal under its own check number,
because `check-arms` finds a branch by its literal number (`tools/unattended/unattended.sh:12742-12744`).

| Case | Stdout | Stderr | Status |
|---|---|---|---|
| the policy kit resolves and `get` answers a value in the key's closed set | the value | nothing | 0 |
| `resolve_python` or `resolve_kit_dir "$py" policy policy.py "$KIT_DIR"` finds nothing | the kit default | `unattended: NOTE - no policy kit resolves beside this kit, so <key> takes the kit default '<value>'.` | 0 |
| `get` refuses, an invalid file with no valid revision before it, say | the reader's `policy: refused` line | nothing | 1 |
| `get` answers a value outside the closed set | a line naming the key and the value | nothing | 1 |
| an argument that is not one of the three | a line naming the three | nothing | 1 |

The third row is a refusal because an invalid file never reads defaults (`tools/policy/README.md:237`).
The fourth is `LANDER_MODE`'s reason (`tools/unattended/unattended.sh:627-628`): a value from a newer
catalogue must not fall through to a behaviour nobody declared. A policy kit older than these rows
lands in the third row, its refusal naming the catalogue, and the remedy is the deployer's update.

The reader spells each key on a line of its own, `"$py" "$d/policy.py" get review.spec-audit.disposal`
and its two siblings, inside a `case`. `arm_reader_coverage` greps a literal key on the `policy.py get`
shape (`tools/policy/check_policy.py:434`), so a key passed in a variable reads as unread once this
build lands. `$d` is repo-relative (`tools/unattended/lib-unattended.sh:131`), which is sound because
`load_driver_conf` has `cd`'d to the root (`tools/unattended/unattended.sh:547`). The pattern is
`print_drift_delta`'s (`:1259-1274`), and the policy read itself is the read
`tools/check-line-length.sh:157-158` makes of the same kit.

**Called on demand.** `load_driver_conf` runs on every verb, and three reads there would add at least
three Python spawns to each one. A spec exit and the chain verdict are the only readers.

### The kit defaults

```bash
SPEC_AUDIT_DISPOSAL_DEFAULT="by-nature"
SPEC_AUDIT_CHAIN_STOP_DEFAULT="own-work"
SPEC_AUDIT_CHAIN_CEILING_DEFAULT="4"
```

They sit after `SPEC_COUNTS_CUTOFF` (`tools/unattended/unattended.sh:1023`), file constants assigned
after the conf is sourced, so a conf cannot preset them. They repeat the catalogue's defaults because
a copy-installed kit cannot read a kit that is not there; AC5 is the gate that compares the two.

### The cutoff key

`SPEC_FOLD_CUTOFF` names the rule it dates, on the `SPEC_COUNTS_CUTOFF` and `FOLD_CUTOFF` pattern. It
is a conf key, as design tag `[cutoff]` rules, and unlike those two driver constants, because a kit
update must not move an adopter onto a new disposal: the example ships it blank with the reason its
siblings give (`tools/unattended/.unattended.conf.example:484-488`).

| Value | Meaning |
|---|---|
| blank or absent | every run keeps the old rule, and check 2 says so on stdout (`TOOL-dFoldedAudit-2`) |
| an ISO date | a run whose record began on or after it takes the new rule |
| anything else | `load_driver_conf` refuses, exit 2 |

Blank is the design's old rule, on `DISPOSITION_CUTOFF`'s terms (`.unattended.conf:478-480`), and it is
what lets an adopter without the policy kit choose: blank for the old rule, a date for the defaults.

The driver adds `SPEC_FOLD_CUTOFF=""` to the init block's last line
(`tools/unattended/unattended.sh:566`) and a reason bullet to the comment under it: a comment inside
the block ends the suite's contiguous read (`:576-579`). The refusal follows the `RUN_CLAIMS` case
(`:672-677`) and spawns nothing:

```bash
case "$SPEC_FOLD_CUTOFF" in
  ""|[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
  *) echo "unattended: REFUSING - SPEC_FOLD_CUTOFF is declared as '$SPEC_FOLD_CUTOFF', which is not an ISO date, and a cutoff nothing can compare grades every run or none." >&2
     RUNLOG_CLEAN=1; exit 2 ;;
esac
```

It exits 2, so it is no refusal site for `check-arms`, whose signature reads `exit 1` and `status=1`
(`.memory-tree.conf:639-643`). This unit adds no `fail` branch.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `read_spec_audit_switch` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-01 |
| `SPEC_AUDIT_DISPOSAL_DEFAULT`, `SPEC_AUDIT_CHAIN_STOP_DEFAULT`, `SPEC_AUDIT_CHAIN_CEILING_DEFAULT` | no `sh.constant` cell is declared | the `<NAME>_DEFAULT` spelling of `REVIEW_ROUNDS_DEFAULT` |
| `SPEC_FOLD_CUTOFF` | no `sh.constant` cell is declared | the `<NAME>_CUTOFF` spelling of its siblings |
| `review.spec-audit.disposal`, `.chain-stop`, `.chain-ceiling` | a catalogue `name` | `arm_shape` |

### Rollout

Dark by construction: nothing calls the reader until `TOOL-dFoldedAudit-2`, and the cutoff stays blank
until the close. The pass makes two commits. `tools/policy/guard.py` refuses a mirror staged beside
an input it records, so the catalogue commits first and `policy.py mirror --write` commits second
(`tools/policy/README.md:352-353`).

### Files touched (estimate)

`tools/policy/catalogue.toml`
`.governance/policy.json`
`.unattended.conf`
`tools/unattended/.unattended.conf.example`
`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Conf keys beside `REVIEW_ROUNDS`.** Refused by `policy.py lists --check`, the `growth` case at
  `tools/policy/README.md:523-524`.
- **Conf keys read only where the policy kit is absent.** A second home for each value, for an
  adopter a blank cutoff already serves, and it would owe `optional_keys` rows and a two-homes rule.
- **The read inside `load_driver_conf`.** Three spawns on every verb, against the spawn budget leg.
- **A driver constant for the cutoff, as `SPEC_COUNTS_CUTOFF` is.** The design rules a conf key, and a
  constant would move every adopter on a kit update.

## 5. Production-readiness checklist

- **security** — The reader writes nothing and reads the landed revision, so a run cannot flip its own
  switch. `SPEC_FOLD_CUTOFF` is a working-copy read like `DISPOSITION_CUTOFF`: not an authorization, and
  a run's edit of it shows in the diff the closing review reads.
- **perf / scale** — No spawn on the verb path. One read costs one Python start and one `git show`.
- **error / empty / loading states** — The reader's table above. A blank cutoff is the default state.
- **observability** — The kit-default answer prints a NOTE. `policy.py get --explain` names source and
  revision.
- **risks** — The value is the landing date by design tag `[cutoff]`, and the idiom at
  `tools/unattended/unattended.sh:1009-1012` records the failure that invites: a record begun on the
  landing day under the old driver reds at the merge, because it reads as on or after the cutoff.
  The landing date meets that idiom's "strictly past" only when every old-contract record began
  before it, and `check_landed_facts_due` keys on the day a record began, so one begun earlier is
  safe at any later value. Edges therefore gives the close a read before it writes the date, over
  every ref because such a record sits on a run branch and not on `main`:
  `git log --all --diff-filter=A --format='%cs %h' --name-only -- 'memory/builds/*/RUN.md' 'memory/builds/*/RUN.*.md'`,
  each line dated on or after the value being a hit, and this build's own record excepted, because
  it carries no spec-audit row. PINNED, measured 2026-11-01: `dTendedCadence` and `dScopedBuild` both
  began that day and hold old-shape spec exit rows on their run branches, so a value of `2026-11-01`
  reds them and any later value does not.
- **testing** — One fixture repository per criterion, no gate. The arms are `New arm:` lines in §7.
- **migration** — Additive. An unset key reads its default, a blank cutoff changes nothing, and the
  shrink-only lists stay as they are.
- **user docs** — `help/policy.md` enumerates no key (`grep -n 'review\.' help/policy.md` prints
  nothing), so no page changes here. The switches' prose is `TOOL-dFoldedAudit-1`'s.

## 6. Acceptance criteria

Each fixture is a scratch git repository under `%TEMP%` with a short name, on branch `main`, with no
remote, so `policy.py get` reads the local `main` (`tools/policy/README.md:220-223`). Fixture K holds
copies of `tools/unattended/unattended.sh`, `tools/unattended/lib-unattended.sh`,
`tools/policy/policy.py` and `tools/policy/catalogue.toml` at those paths, and a `.unattended.conf`
holding `MEMORY_ROOT=memory`, all committed. Fixture N is K without `tools/policy/`. The probe, run with
the fixture as its working directory and `$F` its absolute path:

```bash
bash -c '. "$1"; load_driver_conf; read_spec_audit_switch "$2"' _ "$F/tools/unattended/unattended.sh" <key>
```

The `_` keeps `$0` apart from the sourced path: the source guard at
`tools/unattended/unattended.sh:787` would otherwise run the driver's body.

- **AC1** — When `python tools/policy/policy.py get review.spec-audit.disposal` runs in this repository,
  and again for `review.spec-audit.chain-stop` and `review.spec-audit.chain-ceiling`, they print
  `by-nature`, `own-work` and `4`, each exit 0.
  Red when: a row is absent, which exits 2 naming `is not a catalogue key`, or a default differs.
- **AC2** — When K commits `.governance/policy.toml` setting `disposal = "promote-all"`,
  `chain-stop = "clean-only"` and `chain-ceiling = 2` under `[review.spec-audit]`, the probe prints
  `promote-all`, `clean-only` and `2` for `disposal`, `chain-stop` and `chain-ceiling`.
  Red when: the reader answers a constant, so a staged read of `$SPEC_AUDIT_DISPOSAL_DEFAULT` prints
  `by-nature`.
- **AC3** — When K's first commit sets `disposal = "fold-all"`, the probe for `disposal` exits 1 and
  prints a `policy: refused` line naming `.governance/policy.toml`, and no value line.
  Red when: an invalid file reads a default, or the reader's status is lost in its `$(...)`.
- **AC4** — When the probe runs in N for each of the three, it prints `by-nature`, `own-work` and `4`,
  exit 0, and stderr carries `no policy kit resolves beside this kit`.
  Red when: a missing kit refuses, or takes the default with no NOTE.
- **AC5** — When K holds no policy file, the probe's three answers equal N's three answers.
  Red when: `SPEC_AUDIT_DISPOSAL_DEFAULT` is staged to `promote-all` with the catalogue unchanged, or the
  catalogue default is staged to `promote-all` with the constant unchanged.
- **AC6** — When `python tools/policy/policy.py lists --check` runs in this repository, it reports no
  `is a new legacy home` and no row for `review.spec-audit.`, and
  `grep -c '^SPEC_FOLD_CUTOFF=' .unattended.conf tools/unattended/.unattended.conf.example` prints 1 for
  each file.
  Red when: a switch is homed in `.unattended.conf`, or a new row lacks `summary` or `usage`.
- **AC7** — When K's `.unattended.conf` gains `SPEC_FOLD_CUTOFF="soon"`,
  `bash "$F/tools/unattended/unattended.sh" --version` exits 2 and its output carries
  `SPEC_FOLD_CUTOFF is declared as 'soon', which is not an ISO date`; with the key blank, absent, or
  `"2026-11-02"`, it exits 0 and that text is absent.
  Red when: the shape check is absent, which exits 0 and prints the version with no refusal text, or
  a blank value refuses. The text and the status are the observation: process and in-process
  agreeing proves neither, because a deleted check changes both sides alike.
- **AC8** — When `sed -n '/^load_driver_conf()/,/^}/p' tools/unattended/unattended.sh | grep -c read_spec_audit_switch`
  runs, it prints 0, and `grep -c 'policy.py" get review.spec-audit\.' tools/unattended/unattended.sh`
  prints 3.
  Red when: the read moves into the loader, or a key reaches `get` through a variable.
- **AC9** — When `python tools/policy/policy.py mirror --check` runs after the second commit, it prints
  `policy: mirror fresh`, and `grep -c '"review.spec-audit\.' .governance/policy.json` prints 3.
  Red when: the mirror is not re-rendered, which prints `mirror stale`.

## 7. Gates

`policy check` · `policy fixtures` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The unattended kit gate reds on check 22 until `TOOL-dFoldedAudit-1` writes the key-table row. That is
owed at the close, where it runs, and not at this unit's pass.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · a fixture policy file setting the old values, staged with the reader answering the kit constant · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · a first commit setting an out-of-set value, staged with the reader's refusal branch falling through to the default · none
New arm: tools/unattended/unattended.test.sh · covers AC4 · a fixture with no policy kit, staged with the absent-kit branch refusing · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · `SPEC_AUDIT_DISPOSAL_DEFAULT` staged to `promote-all` · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · a `PARITY_ROWS` conf-refusal row with `SPEC_FOLD_CUTOFF="soon"`, and beside it, after the table's loop in the same shard, `run --version` over that conf held by `hit` on `SPEC_FOLD_CUTOFF is declared as 'soon', which is not an ISO date` and `same` on exit 2, and over a blank and a dated key by `miss` on that text and `same` on exit 0; staged with the shape case deleted, which reds the `hit` and the `same` and leaves the row green · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · the source read of `load_driver_conf`'s body, staged with the reader called from it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.
- rev-2 · 2026-11-01 · §3 §4 §5 · M2's cross-read found two disagreements. The close's check said no
  run was preflighted that day, which names no ref, where the idiom at
  `tools/unattended/unattended.sh:1009-1012` reads any branch and `TOOL-dFoldedAudit-2`'s rule keys on
  the day a record began; the check is now that read, with today's measure. The key table named
  `TOOL-dFoldedAudit-3` a reader of the disposal key, where that unit's §3 reads no key.
- rev-3 · 2026-11-01 · §6 §7 · AC7 · the fix brief's item 4. The first builder showed AC7's arm could
  not go RED: a `PARITY_ROWS` row compares only the process and in-process output, status and tree
  (`tools/unattended/unattended.test.sh:2361-2366`), so deleting the shape case changes both sides
  alike. The row stays, a positive assertion of the refusal text and exit status now sits beside
  it, and AC7 names that text. The driver's design does not move.

## 10. Reuse audit

The seam is `resolve_kit_dir`, the `reuse_lookup.py` candidate for this behaviour, at
`tools/unattended/lib-unattended.sh:132`, called as `print_drift_delta` calls it
(`tools/unattended/unattended.sh:1259-1274`), and `policy.py get`
(`tools/policy/policy.py`), which `tools/roles/roles_lib.py`'s `read_policy_setting` already runs from
Python. `reuse_lookup.py` found no shell reader of a catalogue key, and recall hit
TOOL-dBoundRoles-21 for the Python one. That function is out of reach here because the unattended kit
does not require the roles kit (`tools/unattended/kit.toml:12`). The loader seam is `load_driver_conf`'s
init block and its `case` refusals.

Where the records and the source disagreed: the scout places the new cutoff beside `FOLD_CUTOFF` and
`SPEC_COUNTS_CUTOFF` as if all three were conf keys, and the source holds those two as driver constants
(`tools/unattended/unattended.sh:1013`, `:1023`), with `DISPOSITION_CUTOFF` the conf key. The design's
conf key is built here, read as `DISPOSITION_CUTOFF` is.

Recall terms used: `python tools/memory-recall/query.py "how is a policy switch read by a kit with a default when the policy kit is absent" --terms "policy.py get catalogue row legacy-homes read_bound_key review rounds cutoff adopter"`.
Reuse probe used: `python tools/codebase-map/reuse_lookup.py "read a policy switch with a kit default when the policy kit is absent"`.
