# The merged row, reproduced — B1's refusal shape observed rather than derived

**Serves:** research DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-13

Round 5's blocker B1, and round 4's B2 and H2, were all established by READING `govkit.py` and two
kit descriptors. None had been run. The fork B1 raises was ratified to Direction A on that reading,
and a ruling resting on an unreproduced claim is the shape this repo keeps a gate against, so the
claim was reproduced. Every number below is observed output, not a source citation.

## Method

A scratch git repository with two committed files, then the two verbs, against gov at `1d19b58b`:

```
python tools/govkit/govkit.py intake --target <scratch> --kits push-main
python tools/govkit/govkit.py apply  --target <scratch> --kits push-main
```

`push-main` was chosen because it is one of the two entries in this tree declaring
`role = "merged"` with `marker_style = "hash-comment"`, which is the branch that reaches the row
writer. The run reported `6 row(s), 1 kit(s), schema 2`, and printed the merged write by name.

## What the receipt actually holds

Six rows. The `has` columns are key PRESENCE in the emitted JSON, nothing else:

| role | path | `commit` | `gov_oid` | `oid` | `sha256` | `block_sha256` |
|---|---|---|---|---|---|---|
| attributes | `.gitattributes` | no | no | no | no | yes |
| merged | `.githooks/pre-commit` | **yes** | **no** | no | no | yes |
| engine | `pre-push` | yes | no | no | yes | no |
| engine | `pre-push.test.sh` | yes | no | no | yes | no |
| engine | `tools/push-main.sh` | yes | no | no | yes | no |
| engine | `tools/push-main.test.sh` | yes | no | no | yes | no |

The merged row's key set, verbatim: `block_id`, `block_sha256`, `commit`, `kit`, `marker_style`,
`mode`, `normalized`, `path`, `role`, `source`, `version`, `written`.

## The three claims, and what the run says about each

**B1 — CONFIRMED, and this is the one that mattered.** The merged row carries `commit` and does not
carry `gov_oid`. That is exactly one of the two, which is `-7` S9's third arm — a whole-run refusal
in the preamble, before any row is classified. The refusal itself is still unobserved, because `-7`
is not built; what is now observed is the STATE that triggers it, on a receipt this tree's own kit
produces on a first `apply`. `-7` AC11 still owns the refusal arm.

**B2 — CONFIRMED.** The receipt carries one `attributes` row and one `merged` row. Neither comes
from `resolve_entry`, whose two channels `-13` S2 originally took as the whole destination set. A
bootstrapped receipt built from that set alone would have had four rows here, not six, and the two
missing ones are precisely the classes `-2`'s `pins` disposition and `cmd_check`'s merged loop
dispatch on.

**H2 — CONFIRMED, with a correction to how it was argued.** Four of the six rows carry `sha256`;
the attributes and merged rows do not, by construction. `install.sums` is 333 bytes and covers those
four. So the field is real and the sidecar is non-empty for a normal `apply` — H2's failure mode is
specific to `adopt` omitting the field entirely, which would take the sidecar to zero bytes while
`cmd_check` compared zero against zero. The round-5 fold already moved `-13` AC10's predicate from
"carries a `commit`" to "carries a `sha256`", and this run says why that matters: the two counts
differ by two on the very first receipt.

## What this does NOT establish

The refusal was not run — no arm, gate or `refusal_join.py` branch has been observed red or green,
because `-7` S9 does not exist yet. Direction A's exemption is therefore still an unexercised design
decision, and the first thing `-7`'s build owes is AC11.

Nothing was measured against a live adopter. The scratch target is two files and one kit; the
inCMS and NicoCares populations that `-9` and `-4` reason about are untouched here and remain
unverified where those specs say they are.

The `attributes` row here reads `written: true`, because `apply` wrote the block. `-13` S11 specifies
`written: false` for the row `adopt` synthesizes, since that verb writes no block. This run does not
exercise `adopt`, which does not exist yet, so that half of S11 is still design.
