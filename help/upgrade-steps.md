# Upgrade steps and retired kits

**What it is.** An upgrade step is a declared, reversible move of something an installed repository
holds — a conf key, a file — to where gov keeps it now. Each step is one `[[upgrade]]` row: in the
descriptor (`kit.toml`) of the kit that owns the surface, or in `tools/govkit/steps.toml` for a
surface no kit owns. The row names three commands, `up`, `down` and `witness`, the `surfaces` it
moves, and whether it runs the target's own code (`needs-target`). The commit that introduced a row
is never written in it: it is the first commit on the default branch's first-parent line that holds
the row, and a row the default branch has not landed reads `unlanded`. A kit that leaves gov gets a
`[[retired]]` row in `tools/govkit/registry.toml` naming its `successor`, another kit, or `none`.

## How to use it

- **See every step, in the order they run:**

  ```sh
  python tools/govkit/upgrade_steps.py list
  ```

  One line per row: its position, its id, its introducing commit (or `unlanded`) and the file that
  declares it, then one line per `[[retired]]` row. Rows that landed in the same commit run with
  `steps.toml` first, then each kit in registry order. A malformed row exits 2 naming its file, row
  and key.
- **See which old homes a step still has to empty:** `python tools/govkit/upgrade_steps.py list
  --window` prints each home a step's `surfaces` names, `open` until that step lands, then `closed by
  <step id>`.
- **Correct a landed step:** add a new step under a new id. A landed row is frozen: the
  `step-rows-frozen` leg, `python tools/govkit/upgrade_steps.py frozen`, fails when a branch edits a
  landed row's `up`, `down`, `witness`, `resume` or `surfaces`, edits a byte of a program a landed
  row runs, or removes a landed row with no `[[retired]]` row naming it. It does not check what a
  step program imports.

## What a step can reach

A step is gov's code run over your repository, so it runs under one contract, whichever command
starts it:

- **From gov's checkout**, never yours: a relative path in a step names gov's file.
- **A clean environment.** Only the names a process needs to start (`PATH`, `SYSTEMROOT`, `LANG`
  and the like) are copied in; everything else, every token and credential variable included, is
  left out. Home and temp point at a fresh scratch directory that is removed after the step.
- **No git config of yours or the machine's, no hooks, no credentials.** Git reads no system or
  global config and never prompts, and two settings passed through `GIT_CONFIG_COUNT`, which
  outrank your repository's own config, point `core.hooksPath` at an empty directory and set
  `credential.helper` to nothing. A step's `git add` or `git mv` fires none of your hooks.
- **Python runs isolated (`-I`)**: it ignores `PYTHONPATH` and imports nothing from your tree or
  the working directory.

A step that needs your repository's own code or hooks declares `needs-target = true`. The runner
spawns nothing for such a step and reads it `attended`: a person runs it. The `update` walk still
runs its witness, under this same contract, to see whether that person already has. To check a step's declaration,
gov runs it beside planted hooks and modules in a scratch copy and reads one verdict:

- `isolated` — it ran clean and touched none of your code;
- `needs-target` — it failed and touched none of your code, so it needs it: declare
  `needs-target = true`;
- `breach` — it ran your code anyway, named in the line; fix the step;
- `attended` — it already declares `needs-target = true`, and nothing ran.

To see the contract hold on this machine:

```sh
python tools/govkit/upgrade_steps.py fixture isolation                  # exit 0
python tools/govkit/upgrade_steps.py fixture isolation --plant hook     # hook canary: absent
```

The contract is not a sandbox: a step that opens a path into your tree on purpose is not stopped,
which is what `breach` reports.

## What the receipt records about steps

The receipt, `.governance/install.json`, declares its `schema`. Schema 4 adds `steps`, one row per
step that has run on this repository: its `id`, the commit that `introduced` it (`null` for a step
that ran before its row landed), and its `state`, one of `applied`, `failed` (with the `failure`
text) or `rolled-back`. The last `applied` row is the last step completed. `govkit.py check`
reports a malformed `steps` field as a problem naming the row.

A first install, by `apply` or `adopt`, is born at schema 4 with an empty `steps`. An existing
receipt at schema 4 keeps its schema and its `steps` across a re-apply, an `adopt --re-adopt` or an
`update`; one below 4 is never raised past 3 by them, and an existing receipt
reaches 4 only by the step `govkit/receipt-schema-4`, the first row of `steps.toml`. Its up takes
a schema-3 receipt to 4 with an empty `steps` (a receipt below 3 is refused: run `update` first,
which lifts it to 3); its down takes the field out again and refuses while any other step reads
`applied`.

Before schema 4 no step row is written: a step's failure or interruption on such a receipt shows
only in `update`'s output and findings. The `govkit/receipt-schema-4` row itself is written once
that step's re-read of the receipt shows schema 4, like any other row. A row is recorded only on a
receipt whose `schema` is a number of 4 or more and whose `steps` is a list; anything else is
refused. Until the deployer runs steps itself, run the step by hand:

```sh
python tools/govkit/steps/receipt_schema_4.py up <repo>       # schema 3 -> 4
python tools/govkit/steps/receipt_schema_4.py witness <repo>  # exit 0 at schema 4
python tools/govkit/steps/receipt_schema_4.py down <repo>     # schema 4 -> 3
```

## What `update` does with steps

`govkit.py update --target <repo> --write` walks the steps after it lands the files and before it
re-renders, so a step meets the new files and the renders meet the moved ones:

- **The order.** Every step row in `--to`'s tree, in the order `list` prints, minus each step the
  receipt's `steps` records `applied`. A step landed after `--to` is not walked.
- **The skip.** Each step's witness runs first. Where it holds, the step is recorded `applied` and
  its up never runs: `step <id> · skipped (witness holds)`.
- **A step that runs** is recorded `failed`, `interrupted: started <utc>, no exit recorded`, before
  its up starts, and `applied` once the up exits 0 and the witness holds. Its writes and its
  before-image under `.governance/steps/` are staged, never committed.
- **A stopped walk.** An up that exits non-zero (`exit <rc>: <its last stderr line>`), or a witness
  that still fails after it (`witness does not hold after up`), stops the walk. The steps before it
  stay applied, no down runs, the run exits 1, and the receipt's `gov_commit` does not move.
- **An attended step** (`needs-target = true`) stops the walk before its up, recorded `failed` with
  `attended: the step needs the target's code`, and writes
  `.governance/outbox/update-attended-step-<slug>.md`, naming the step and the command to run. Run
  it yourself; the next `update --write` skips the step once its witness holds.
- **Read-only, and `--kits`.** Without `--write`, `update` prints `would walk <id>` for each pending
  step and runs none of them, witnesses included. A `--kits` run walks none and prints `steps: not
  walked` with the pending count; the next run without `--kits` walks them.

Every write run prints one line with every count, zeros included:
`govkit update — steps: <n> pending · <a> applied · <s> skipped · stopped at <id|none>`.

**After a kill.** A killed run leaves its write lock, `.governance/outbox/.update.lock`, which names
the holder's pid and host. The next writing run on that host reclaims it by itself once the pid is
gone from the process table, or names a process started after the lock, and prints `reclaimed`. A
lock from another host, one it cannot read, or one it cannot judge because the process census cannot
run is not reclaimed: the refusal names the holder, and you delete the lock by hand once you know
that run has ended. Before each index write a run appends the path and the blob it stages to
`.governance/outbox/.update.lock.staged`; the run that reclaims the lock reads that journal, so the
paths the killed run staged are not refused as dirty, while a different blob you staged at one of
them still is. The step the kill interrupted reads `failed` with its `interrupted:` text, and the
next walk runs it again, or runs the row's `resume` command where it declares one.

To see it on this machine:

```sh
python tools/govkit/upgrade_steps.py fixture walk                       # s1 to s4 applied, in order
python tools/govkit/upgrade_steps.py fixture walk --plant kill-step     # killed, re-run, converges
python tools/govkit/upgrade_steps.py fixture lock --plant lock-dead     # reclaimed
python tools/govkit/upgrade_steps.py fixture update --plant kill-walk   # update killed mid-step
```

## What `update` does with a retired kit

`govkit.py update --target <repo>` reads the target's receipt. A claimed kit that is still a registry
entry is updated as always. One that is not, and has a `[[retired]]` row:

- **with a successor:** prints `retired <old>: claimed by its successor <new>`, classifies the kit's
  files under the successor's descriptor, and with `--write` the receipt claims `<new>` instead of
  `<old>`;
- **with `none`:** prints `retired <old>: released`, and each of its files reads `withdrawn`: with
  `--write` an order lands under `.governance/outbox/`, and nothing is deleted unless you also pass
  `--write-withdrawals`.

A claimed kit with no `[[retired]]` row still stops the whole run, naming the kit, before anything is
written. `govkit.py check` prints `<old>: retired, successor <new>` for a retired claim and counts no
problem for it.

## Where `.agent-cap.conf`'s value lives

The agent limit is the policy key `runtime.agents-in-flight` in `.governance/policy.toml`
([the agent limit](agent-limit.md)). A `FANOUT_CAP=<n>` line in `.agent-cap.conf` only lowers it.
The step `agent-cap/fanout-cap-to-agents-in-flight` retires the file: its up writes `<n>` into the key
when the line lowers it (and leaves the policy file alone when it does not), then removes the file,
so the limit reads the same before and after. Its down puts both files back byte-for-byte.
`update --write` runs it as one of its steps; to run it by hand, from this checkout, against a
repository whose `.agent-cap.conf` and policy file are committed:

```sh
python tools/govkit/steps/fanout_cap.py up <repo>       # exit 1, writing nothing, on a bad value
python tools/govkit/steps/fanout_cap.py witness <repo>  # exit 0 once the file is gone
python tools/govkit/steps/fanout_cap.py down <repo>     # exit 1 if a file changed since the up
```

Then commit the result, `.governance/steps/agent-cap/` included: the before-image there is what the
down restores from.
