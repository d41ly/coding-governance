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
so the limit reads the same before and after. Its down puts both files back byte-for-byte. Until the
deployer runs steps itself, run it by hand, from this checkout, against a repository whose
`.agent-cap.conf` and policy file are committed:

```sh
python tools/govkit/steps/fanout_cap.py up <repo>       # exit 1, writing nothing, on a bad value
python tools/govkit/steps/fanout_cap.py witness <repo>  # exit 0 once the file is gone
python tools/govkit/steps/fanout_cap.py down <repo>     # exit 1 if a file changed since the up
```

Then commit the result, `.governance/steps/agent-cap/` included: the before-image there is what the
down restores from.
