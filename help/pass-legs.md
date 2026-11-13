# The pass legs

**What it is.** A build runs in passes, and the merge bar runs once, at the close. The pass legs are
the short list of gate legs the main loop runs between those two points: after each unit pass's
commit, over that pass's diff alone. A leg that reds there is known one pass after the change that
broke it, instead of at the close with every later pass on top. The bar still runs once, in full, at
the close, and a pass itself still runs no gate.

Under the unit harness, `tools/workflows/unattended-unit.js`, the return of a pass that committed
carries a `nextAction` when its caller handed it a `passLegs` command. It orders the main loop to
run that command before the next dispatch and before any later commit.

The runner is `<prefix>/run-gates/pass-legs.sh` and the declaration is
`<prefix>/run-gates/pass_legs.py`, which are under `tools/run-gates/` in this repository. The
run-gates kit README's sections "The pass legs" and "The pass-leg runner" are the full reference.

## How to run it

Run `bash tools/run-gates/pass-legs.sh --base <rev>`, where `<rev>` is the commit the pass started <!-- usage: script:tools/run-gates/pass-legs.sh c6221f63 -->
from. The runner filters the leg manifest to the declared rows, writes them to
`<git-dir>/gate-pass-legs.json` and starts `run-gates.sh` once over that list, with `<rev>` as the
base each leg's own guard decides against. Every leg's command runs behind the held tier's leg shim,
`run-held-wsl.sh --leg`, so a leg that reads the manifest as its subject grades the whole manifest
and never the filtered list.

- **Exit code:** the bar runner's own, unchanged. It is 0 too when the switch below is `off` and
  when no row is declared.
- **Exit 2, nothing run:** `--base` is absent or names no commit. The bar runner reads an
  unresolvable base as empty and runs every leg, so the adapter stops first.
- **The record:** `<git-dir>/gate-pass-legs.txt`, one `key TAB value` per line, replaced on every
  run that got as far as reading the manifest.

| Key | Value |
|---|---|
| `run_id` | `pass-<UTC stamp>-<pid>`, the run's directory under `gate-run/`; `-` when no runner started |
| `base`, `head` | the resolved base, and `HEAD` when the run started, as full shas |
| `started` | UTC, to the second |
| `exit` | the runner's exit code, or `-` when no runner started |
| `verdict` | the runner's verdict; `EMPTY` when no row is declared; `NO-VERDICT` when it wrote none |
| `declared` | how many rows carried the field |
| `wall_s`, `budget_s`, `limit_s` | whole seconds around the runner call, and the two declared figures |
| `over` | `none`, `tolerance` or `limit` |
| `held` | the runner's count of held legs |
| `leg` | one line per declared leg: its name, its status and its seconds |

A leg's status is `ok`, `fail` or `timeout`. A declared leg the run did not start reads `not-run`:
its guard skipped it for this diff, or the runner held it.

## What it prints

The bar runner's output passes through uncaptured. The adapter adds at most these lines, and none
of them moves the exit code:

```text
pass-legs: FINDING overrun: the run took <wall>s, over the <limit>s limit (budget <budget>s)
pass-legs: FINDING held: <n> declared leg(s) did not run, held as a self-test or a kit-subject leg
pass-legs: NOTE the run took <wall>s, inside the tolerance above the <budget>s budget
pass-legs: 0 legs declared, nothing ran
```

The first two are findings to act on. The `NOTE` line is a run over the budget and inside the
limit, which is no finding. The last line is a manifest in which no row carries the field.

## How the list is declared

A row of the leg manifest, `tools/gate-legs.json` here, is a pass leg when it carries
`"pass_leg": true`. Nobody types the field: `pass_legs.py` derives it by one rule. Rank every <!-- usage: script:tools/run-gates/pass_legs.py 76be594d -->
eligible leg by its recorded reds per evidenced second of cost, then fill the budget in that order.
A self-test leg, a leg whose subject is the kit, an end-to-end leg, the unattended kit gate, a leg
that has never been red, a leg with no cost row and a leg over the cap are not eligible.

| Verb | What it does |
|---|---|
| `python tools/run-gates/pass_legs.py --report` | one line per leg: its verdict, reds, cost, score and name |
| `GOV_NODE=<tag> python tools/run-gates/pass_legs.py --write` | rewrites the evidence from this node's run log and ledgers, then applies |
| `python tools/run-gates/pass_legs.py --apply` | writes the field onto each selected row and removes it from every other |
| `python tools/run-gates/pass_legs.py --check` | exit 0 when the manifest is what `--apply` would write, 1 naming each leg that differs |

The evidence is `tools/run-gates/pass-leg-evidence.txt`, tracked and generated: one row per leg
that has been red, with its count of reds and its last seconds. With no evidence file the rule
selects nothing, which is an adopter's state until it runs `--write` on a node that has run a bar.
The field is re-applied at every landing, and each bar's preflight proves it fresh.

## The budget

The declared list is held to three figures, which are constants of `pass_legs.py`.
`python tools/run-gates/pass_legs.py --figures` prints them as budget, limit and cap, in seconds:

```text
600	690	120
```

A list is filled up to the budget. A run over the budget and at or under the limit is the `NOTE`
line above, and a run over the limit is the `overrun` finding. No single leg may cost more than the
cap. In this repository `--check` printed `pass-legs: 29 declared, 486.5s of 600s` on 2026-11-12.

`python tools/run-gates/pass_legs.py --budget` is the gate over the list the rule leaves. It exits
1 with a `PASS-BUDGET FAILED` line per finding, and 2 when it cannot grade:

| Finding | The declared leg, or the list |
|---|---|
| excluded class | is a self-test leg, an end-to-end leg or the unattended kit gate |
| held | has the kit as its subject, so the runner would hold it and run nothing |
| no cost row | has no row in `ceiling-evidence.txt` |
| over the cap | costs more than the cap, by its cost row or its last seconds |
| over the limit | the declared legs' cost rows sum above the limit |

A sum over the budget and at or under the limit prints `pass-budget: WARN` and is no finding. The
bar leg `leg ceilings clear their evidenced maximum` carries the gate, so every bar grades it.

## The scoped legs

A full leg too slow for a pass can have a cheap form: a second manifest row carrying `scope_of`,
the name of the leg it is a form of. A scoped row is credited that leg's reds, so it can earn its
place in the list. The manifest holds three, and each is declared a pass leg:

| Scoped leg | A form of | What it runs |
|---|---|---|
| `memory hygiene (the pass checks)` | `memory hygiene` | `check-memory-hygiene.sh --only 9,21,23` |
| `spec tokens (the pass's own spec)` | `spec tokens (a spec's own names resolve)` | `check-spec-tokens.py --pass-spec` |
| `positional (the citation check alone)` | `tags (the resolver's checks)` | `positional.py check` |

The full leg still runs at the bar. A scoped leg's green says nothing about the checks it left out.

## Who runs it

The main loop, and nobody else. A role agent's pass stays gate-free: the hooks kit's role gate
refuses a role agent's call of `pass-legs.sh` under its row `G2 runner`, which matches the bar
runner, the self-test runner, the unattended gates runner and the pass-leg runner by basename, and
admits none of them for any role. The refusal tells the agent to return the need to the main loop.

## The switch

`pass.fast-legs` in `.governance/policy.toml` turns the mechanism on or off. <!-- usage: policy:pass.fast-legs 3272585d -->

| Value | What the runner does |
|---|---|
| `on` | the default: it runs the declared legs |
| `off` | it exits 0 having started no runner and written no file, and prints nothing |

```toml
[pass]
fast-legs = "off"
```

`python tools/policy/policy.py get pass.fast-legs` prints the value in force. The runner asks the
key once, before it starts anything, at the landed revision: a branch's own edit of the policy file
has no effect until it lands. A read the policy reader refuses, or a value that is neither `on` nor
`off`, ends the run with exit 0 and no leg run, under one line saying so. A repository with no
policy kit has no switch and keeps the mechanism: the runner prints one `NOTE` line on stderr and
runs. [The policy file](policy.md) says how a key is set and read. A red leg a pass-leg run
records may be fixed through [the red-fix lane](red-fix-lane.md).

## What a run costs the bar's records

A pass-leg run goes through the bar runner, so it writes what a bar writes:

- A red run replaces `gate-last-failure.txt`, as the next red bar would.
- A green run with no skipped leg and a clean tree replaces the `gate-full-green` stamp with one
  naming the filtered manifest. The push hook trusts a stamp only when its manifest is the kit's
  own, so the next push runs its bar in full, and the next full bar re-earns the stamp.
- The run adds its legs' rows to the gate ledger, `gate-ledger.tsv`, and leaves every other row
  standing. A row it writes is keyed on the command behind the shim.

## Example

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
bash tools/run-gates/pass-legs.sh --base HEAD~1
cat "$(git rev-parse --absolute-git-dir)/gate-pass-legs.txt"
```

## What it does not check

- Whether the declared list is the rule's own output or inside its budget. Those are
  `pass_legs.py --check` and `pass_legs.py --budget`.
- Whether a leg its guard skipped should have run: a guard too narrow for the diff is not seen.
- Any runner knob beyond `GATE_FULL` and `GATE_SELFTESTS`, which it empties. An inherited
  `GATE_DOCS_BASE` or `GATE_REUSE` reaches the runner as the caller set it.
- The budget gate reads cost rows, and a cost row is the worst reading on record on one node: a leg
  never re-measured can sit under its true cost. Its sum is the legs run one after another, and a
  leg its guard skips counts in full.
- Anything the bar checks and the list leaves out. A green pass-leg run is not a green bar.
