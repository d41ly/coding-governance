# Spec-audit chains

**What it is.** A declared spec audit disposes each round's confirmed findings by their nature: a
local fix folds into each spec it touches, and only a finding that needs a new mechanism becomes a
unit. Each generation of the audit is a fresh subject, so the rounds form a chain, and the chain
stops on a verdict the driver derives from what was recorded. Three policy keys switch the rules,
and two verbs of the unattended driver, `tools/unattended/unattended.sh`, record a round and
answer the verdict.

The method states the rule in `memory/guides/BUILD-METHOD.md`, section M4, and the verbs' full
reference is `memory/guides/UNATTENDED-VERBS.md`. This page anchors the three keys, the two verbs
and the hook for [the docs leg](docs-leg.md), which reds a landing that changes one and not this page.

## When a chain runs

A spec audit is owed only where the build or its project declares it:

- the front matter of the build's README, as the owner landed it, carries `spec-audit: <date>`; or
- `.unattended.conf` on the default branch declares a dated `SPEC_AUDIT_DEFAULT`, and the README
  declares no key.

Under neither, none is owed, and the tooling says so instead of running one. The opt-in is the
owner's: a run never writes the key, nor passes `specAudit` on its own reading, unless its prompt
record quotes the owner asking. An audit that seems owed goes to the wrap-up.

## The opt-in pack

The pack is a `PreToolUse` hook on `Workflow` calls. It refuses a spec audit in a build that declares none, so the opt-in above holds at the tool call. <!-- usage: hook:spec-audit-optin f61373f5 -->
A default install wires it, and the refusal names the key the build's README would carry.

## How a round disposes

At a spec exit each confirmed finding is disposed by its nature, severity apart, on the
outstanding count and never the verdict word:

- **NEW MECHANISM:** its fix adds a document, gate, adopter, generated artifact, verb or write path
  that no unit's Scope names.
- **LOCAL:** every other finding.

A local finding, a BLOCKER too, folds at the disposal into each spec it touches: a rev bump and a
revision-log line naming the review record and the finding. A new-mechanism finding is promoted: a
BLOCKER or HIGH to its own unit, MEDIUMs and LOWs batched into one unit, or two across disjoint
write sets. A repair unit corrects an unbuilt sibling's spec itself, with a rev bump and a
revision-log line naming the repair and the record. A CLOSED spec stays frozen, and its correction
is a new unit on top. The round records `--folded` and `--promoted`.

`review.spec-audit.disposal` in `.governance/policy.toml` chooses the rule. <!-- usage: policy:review.spec-audit.disposal d6f3b3b9 -->

| Value | What a spec exit does |
|---|---|
| `by-nature` | the default: the nature rule above, for a spec exit past `SPEC_FOLD_CUTOFF` |
| `promote-all` | the rule before: every confirmed finding is promoted |

`SPEC_FOLD_CUTOFF` is a date in `.unattended.conf`. A spec exit before it is disposed the old way,
every confirmed finding promoted.

## Recording a round

`--record-round` appends one spec-audit round to the build's chain record. <!-- usage: verb:unattended.sh:--record-round 60847ce3 -->

```bash
bash tools/unattended/unattended.sh --record-round <slug> --subject <s> --audited "<ids>" --blockers <b> --highs <h> --finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev> --sibling <unit>@rev-<n>
```

- **The record:** one tracked file per build, `<date>-build-<first audited id>-chain-rounds.md` in
  the build's `build/` folder. It is append-only, and the verb stages it. It needs no run-state
  file, so an attended run takes the same route.
- **The rows:** `--finding` and `--sibling` repeat. In a `--finding` row the severity is `BLOCKER`,
  `HIGH`, `MEDIUM` or `LOW`, and the nature is `local` or `new-mechanism`. A `--sibling` row is a
  repair's sibling edit, and it counts as a fold.
- **The round's number** is the record's own, the last plus one, never the harness's `round`.
  `--subject` is the generation, so a replay is refused.
- **Who commits it:** the build harness renders this command as `chainRecord` on every hand-out past
  the disposal and never runs it. The caller commits the disposal's folds and specs, runs the
  command, then commits the record.
- **What it refuses,** before writing a byte: a token outside its grammar; a slug with no build
  folder; two `-chain-rounds.md` files; a tracked record gone from the worktree; rows disposing
  fewer BLOCKER or HIGH ids than `--blockers` or `--highs` count, so a round whose HIGHs reached
  neither a promotion nor a fold is refused; and a `local` or `--sibling` row that never reached
  the tree, meaning a unit no tracked spec carries, a rev below 2 or above the spec's header, or a
  rev with no revision-log entry.

## Asking the verdict

`--chain-verdict` derives whether a chain goes on, and writes nothing. <!-- usage: verb:unattended.sh:--chain-verdict 5fdc7c80 -->
It reads the chain record and the roster alone.

```bash
bash tools/unattended/unattended.sh --chain-verdict <slug>
```

It prints one line, and every word exits 0:

```text
unattended: chain <slug> · round <N> · <word> · reason <reason>[ · audit <ids>][ · override specs-audited <ids>]
```

The word comes from the first of five steps that holds, in M4's order, and the reason names the
step:

| Step | Word | Reason | When it holds |
|---|---|---|---|
| 1 | `CONTINUE` | `unreviewed` | a live roster spec no round audited and this round did not promote, or one of the previous round's promotions and BLOCKER-or-HIGH folds that this round did not audit; it is audited with step 5's set |
| 2 | `STOP` | `clean` | no BLOCKER or HIGH, and nothing promoted |
| 3 | `STOP` | `own-work` | from round 2, every BLOCKER's and HIGH's specs sit inside the previous round's promotions and BLOCKER-or-HIGH folds |
| 4 | `HOLD` | `ceiling` | the chain has reached `review.spec-audit.chain-ceiling` rounds |
| 5 | `CONTINUE` | `open` | anything else: audit what this round promoted or folded for a BLOCKER or HIGH |

What to do on each word:

- **`CONTINUE`:** re-invoke the build harness at the next `round` with `auditIds` the ids after
  `audit`, no `subjectRound` and no `subjects`, and dispatch nothing, because a folded spec is
  audited again.
- **`STOP`:** dispatch the roster. On an `own-work` stop this round's disposal still runs, and a
  unit after `override specs-audited` is built from its spec as written and closes under a
  recorded `--override specs-audited`.
- **`HOLD`:** a second line prints the recipe: `--park <slug> --item spec-audit-chain-ceiling`,
  reap the keepalive, then `--handoff <slug> --code owner-decision --reaped <id>`, because `--hold`
  refuses that code. An attended run asks the owner. A HOLD stays the answer until the owner moves
  the ceiling or rules.

## When a chain stops

`review.spec-audit.chain-stop` in `.governance/policy.toml` chooses which stops the verdict reads. <!-- usage: policy:review.spec-audit.chain-stop b0668fc2 -->

| Value | Which stops the verdict reads |
|---|---|
| `own-work` | the default: the clean stop and, from round 2, the own-work stop |
| `clean-only` | the old rule: the clean stop alone |

Most chains end at round 2. A HIGH naming one older spec keeps the chain alive, because that spec
sits outside the previous round's work. An empty set of HIGHs never reads as the own-work stop. A
HIGH with no address is refused at synthesis: `tier2-review.js` holds it a tally fault, both counts
go null, and the harness refuses the stated absence.

## The ceiling

`review.spec-audit.chain-ceiling` in `.governance/policy.toml` bounds a chain's rounds. <!-- usage: policy:review.spec-audit.chain-ceiling 35f3e681 -->

| Value | What it does |
|---|---|
| `4`, the default; a round count, at least 1 | at that round a chain neither stop ended HOLDs for the owner |

It is a new bound with no old value, and raising it loosens the policy. It is no `CEILING` state:
that runaway backstop counts one subject's rounds, while this bound counts a chain's and is a
`--chain-verdict` word.

## Reading and setting the keys

- **Read one:** `policy.py get <key>` reports each key's value, and the driver reads the three keys
  through it. See [the policy file](policy.md).
- **With no policy kit** resolving beside the unattended kit, each key takes its kit default, and
  the driver prints a note on stderr.
- **A value outside the closed set** the driver branches on refuses, since a value nobody declared
  there takes no behaviour.
- **Setting one:** the keys live in `.governance/policy.toml`, which the pre-commit hook guards. The
  owner commits a change to it from a terminal, and an agent's commit moving one of these keys is
  refused.

The note and the refusal read:

```text
unattended: NOTE - no policy kit resolves beside this kit, so <key> takes the kit default '<default>'.
unattended: <key> answered '<value>', which is outside the closed set this driver branches on, and a value nobody declared here takes no behaviour.
```

## What it does not change

- A closing diff review still disposes by severity: every confirmed finding is promoted, a BLOCKER
  or HIGH to a unit whose mechanism closes it, MEDIUMs and LOWs batched into one unit, two only
  across disjoint write sets. None is parked, waived, retired, re-reviewed or folded.
- The verdict is computed once, in the driver: the build harness renders the two commands and reads
  no set.
