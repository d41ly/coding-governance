# TOOL-dUnstuckLanding-20 — `LANDING_NODES`: landing capability declared, resolved from machine and user, and a planned hand-off

**Status:** INPROGRESS · rev-1 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 8 · closes TOOL-dUnstuckLanding-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 |

<!-- /gen:spec-records -->

## 1. Goal

Five nc node-`b` runs each built real work, overrode Definition-of-Done items they knew before they
started were unmeetable on that node, and then aborted (design section 7). Let a project declare
which nodes may land, as `LANDING_NODES` pairs of `<tag>=<machine>/<user>`, resolved from the host
name and the user and never from a path. A run on any other node starts normally, says
`landing: handoff` from its first record, and ends at `--handoff --code owner-landing` by design,
with no override.

## 2. Scope (IN)

- **S1 — the user reader.** `read_user_name` in `tools/unattended/lib-unattended.sh`, beside
  `read_host_name` and in its shape: `USERNAME` where Windows sets it, else `id -un`, else `USER`,
  lowercased; it returns 1 when none answers. Observed by AC1, AC3.
- **S2 — the grammar, once.** Two library functions the driver and the gate leg both call, so the
  pair grammar has one spelling:
  - `match_landing_node <nodes> <machine> <user>` prints the tag of the one well-formed pair whose
    machine and user equal the given ones, compared lowercased, and returns 0. It returns 1 on no
    match, on an empty machine or user, and when two pairs with different tags match.
  - `landing_nodes_malformed <nodes>` prints each token that is not `<tag>=<machine>/<user>`, with
    `<tag>` one lowercase letter and neither half empty or carrying `/`, plus each tag or
    machine/user pair declared twice. It prints nothing for a well-formed or blank value.

  The library header's "WHAT IT HOLDS" sentence names the three. Observed by AC1, AC2, AC3, AC4.
- **S3 — the read at BASE.** `resolve_landing_node` in `tools/unattended/unattended.sh` reads
  `LANDING_NODES` from `.unattended.conf` at the pinned BASE, by the evaluate-to-a-sentinel read
  `check_authorization` already uses for `SPEC_AUDIT_DEFAULT`, never from the working copy. It sets
  `LN_STATE` to `undeclared`, `lander` or `handoff`, with `LN_TAG` and `LN_WHY`. It never calls
  `fail`. Undeclared or blank at BASE is `undeclared`, today's behaviour. A blob that does not
  evaluate to the end, an unreadable machine or user, or no matching pair, is `handoff`, the safe
  direction. The init block defaults `LANDING_NODES=""` beside its neighbours, and the value the
  startup source binds decides nothing. Observed by AC5, AC6, AC9.
- **S4 — `--preflight`.** After the lease is written, it resolves and prints one line:
  `unattended: landing — lander · node <tag>`, or `landing — handoff · <why> · this run ends at
  --handoff --code owner-landing`, or `landing — undeclared · every node may land`. It writes the
  fact `landing: lander` or `landing: handoff`, afresh at every preflight like the lease, because it
  describes the node holding the run. Undeclared writes no fact. Observed by AC5, AC6.
- **S5 — `--close` on a hand-off node.** `--close` resolves again, for its own node, and that
  answer decides; a disagreement with the recorded fact is printed. On `handoff`:
  - an `--override` is refused as a free refusal, before the anchor observation, by a new numbered
    `fail` naming `--park` and `--handoff`;
  - otherwise the Definition of Done is evaluated as today, and an unmet item refuses as today;
  - on a met DoD, the bar's facts are written and staged exactly as the met path writes them, and a
    second new numbered `fail` refuses the landing. It names
    `--handoff <slug> --code owner-landing --reason <text> --reaped <id>`. Nothing else is written:
    no carry check, no `units-at-landing`, no phase write, no close commit.

  A `lander` or `undeclared` close is unchanged. Observed by AC7, AC8, AC10.
- **S6 — the gate leg.** `tools/unattended/check-unattended.sh` initialises `LANDING_NODES=""`,
  admits it in the import allow-list, and adds one numbered check that reds when
  `landing_nodes_malformed` prints anything for the project conf's value, naming each token.
  Observed by AC4, AC11.
- **S7 — the carriers.**
  - `tools/unattended/.unattended.conf.example` declares `LANDING_NODES=""` with its grammar.
  - PROTOCOL §8 gains its key row, §2 gains the `landing` fact as the next numbered authored fact,
    and §6 gains one sentence on the hand-off node.
  - VERBS gains one sentence each on `--preflight` and `--close`.
  - Both renders under `memory/guides/` are re-copied in the same pass.

  Observed by AC11, AC12.
- **S8 — the close-decision row.** The close-decision table `TOOL-dUnstuckLanding-18` adds to the
  protocol gains one row, in that table's own grammar: a node not declared able to land maps to
  HAND OFF under `owner-landing`. Observed by AC12.

## 3. Non-goals (OUT)

- Declaring gov's own `LANDING_NODES`. Which of gov's nodes may land is the owner's policy, and the
  registry rows for nodes `a` and `d` carry no machine name today. A follow-up the owner scaffolds.
- The inCMS half of design section 7, the `primary` lander publishing other sessions' commits from a
  shared local main. That is `TOOL-dUnstuckLanding-11`'s carriage.
- Deriving the tag from the charter's §2 registry table. See §4's alternatives.
- Any change to `--resume`, `--landed`, `--hold`, the Skill, or the resume tick. A resumed run that
  moved node is caught at `--close`, which re-resolves.
- A refusal at `--preflight`. Candidate (a) of design section 7 was rejected there: it throws away
  work the owner wanted.
- The kit version bump. The orchestrator makes it once, at VERIFYING.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-13` — the `--handoff` verb and its `owner-landing` code,
  which S5's refusal names as the run's exit. Without it the refusal names a verb that does not
  exist, and AC8 cannot complete the hand-off it describes.
- **consumes-from** `TOOL-dUnstuckLanding-18` — the close-decision table S8 adds one row to. Without
  it S8 has no table to extend.

## 4. Design

### Data model

```
.unattended.conf     LANDING_NODES="a=<machine>/<user> d=<machine>/<user>"   # read at BASE only
RUN.md run facts     landing: lander | handoff                               # absent when undeclared
```

A pair's three fields are compared lowercased. Machine names disagree on case across sources on one
machine: measured on node `d`, 2026-10-04, `COMPUTERNAME` is `COMPEETO` and `hostname` is
`Compeeto`, which `read_host_name` already folds. `USERNAME` and `id -un` both read `d41ly` there,
and `USER` is unset.

### Resolution order

1. No `base` fact, or no `.unattended.conf` blob at BASE → `undeclared`.
2. The blob does not evaluate to its sentinel → `handoff`, "unknown is not absent".
3. The key is blank → `undeclared`.
4. `read_host_name` or `read_user_name` answers nothing → `handoff`.
5. `match_landing_node` returns a tag → `lander`. Otherwise → `handoff`, naming the machine/user it
   resolved and any malformed tokens.

Step 1 keeps a record with no BASE on today's path; such a record cannot pass
`authorization-reachable` anyway, so it never reaches a landing.

### Why BASE and not the working copy

The driver sources the working copy at startup. A run that adds its own node to that copy would
grant itself a landing the project did not declare, which widens a write surface. Reading the key
at the pinned BASE, as `SPEC_AUDIT_DEFAULT` is read, closes that route by the same mechanism and for
the same reason.

### Why `--close` runs the bar before refusing

`TOOL-dUnstuckLanding-13`'s `owner-landing` guard reads the `gates-run` fact through
`check_inherited_override`, and refuses with no such fact. A close refusing before the bar would
leave a hand-off node with no bar verdict, so the guard could never admit the exit this unit
designs. Running the DoD first gives the owner a verdict and the guard a record. A refusing close
that writes the bar's facts is not new: the unmet `gates-green` arm already writes `gates-run`
before it returns (`tools/unattended/unattended.sh:7645-7659`).

### Inventory

- Library functions `read_user_name`, `match_landing_node` and `landing_nodes_malformed`; driver
  function `resolve_landing_node`; globals `LN_STATE`, `LN_TAG` and `LN_WHY`. Each name is graded by
  the lexicon gate's shell cell, so ask `--suggest` for each before writing it.
- Conf key `LANDING_NODES`. Fact key `landing`.
- Two new driver `fail` branches in `--close`, and one new leg check. Each takes an arm in its
  sibling test asserting a literal slice of the branch's own text. No unarmed-branches row is
  planned. The numbers are the next free ones when this unit builds, after units 13 to 19.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Resolving the tag from the charter's node registry.** `tools/drift-audit/drift_report.py:2443`
  does this, matching the user as a SUBSTRING of a table cell. A kickoff design measured that shape
  wrong: a row-wide match on `d41ly` hit four rows through the Remote column, and rows `a` and `d`
  carry no machine name (`KICK-aReplayedCard-1`'s orientation design, claim 41). It would also make
  a kit file read the charter by literal, which the kit literal ban refuses.
- **A path.** The charter's §2 forbids it: roots can be identical across machines.
- **Pinning the preflight fact and trusting it at close.** A run resumed on another node would land
  from a node nobody declared. The close's own resolution decides.

## 5. Production-readiness checklist

- security — narrows nothing a project relied on: blank keeps today's behaviour. Declared, every
  doubt resolves to `handoff`, and the key is read at BASE so a run cannot grant itself a landing.
  Environment variables can spoof a machine or user name; that is the limit protocol §9 states for
  any check running under the run's own uid, and it buys only the landing the run could already do
  before this unit existed.
- perf / scale — one `git show` of one blob and one subshell evaluation, at preflight and at close.
  No network.
- error / empty / loading states — every resolution step above prints its reason. A malformed pair
  never matches, is named in `LN_WHY`, and reds the leg.
- observability — the preflight line, the `landing` fact, the close's disagreement line, and the
  refusal naming the exact `--handoff` invocation.
- risks — a typo in a pair makes that node hand off rather than land. The leg names the token, so
  the bar catches it; the run itself loses nothing.
- testing — arms in the driver suite and the leg suite, named in §7.
- migration — none. An undeclared key is today's path, and a record without `landing` reads as
  undeclared.
- user docs — the example conf, PROTOCOL §2, §6 and §8, and VERBS, rendered into `memory/guides/`.

## 6. Acceptance criteria

- **AC1** — When `bash -c '. tools/unattended/lib-unattended.sh && match_landing_node "a=desk-a/daily-agent d=compeeto/d41ly" COMPEETO D41LY'`
  runs, it prints `d` and exits 0.
  Red when: case differs between the inputs and the pair and the match fails, or it prints `a`.
- **AC2** — When the same `match_landing_node` call is given `desktop-3j1o6cd agent5`, an empty
  machine, or a value carrying both `d=compeeto/d41ly` and `b=compeeto/d41ly`, it prints nothing and
  exits 1 each time.
  Red when: an unlisted node, an unreadable one, or an ambiguous match resolves to a tag.
- **AC3** — When `bash -c '. tools/unattended/lib-unattended.sh && USERNAME=Agent5 read_user_name'`
  runs it prints `agent5`, and with `USERNAME` unset it prints what `id -un` prints, lowercased.
  Red when: the reader keeps the case, or returns nothing while `id -un` answers.
- **AC4** — When `landing_nodes_malformed "d=compeeto a=/x bb=m/u c=m/u/v d=m2/u2"` runs after
  sourcing the library, it prints `d=compeeto`, `a=/x`, `bb=m/u`, `c=m/u/v` and the doubled tag `d`,
  and over `"a=m/u d=compeeto/d41ly"` or `""` it prints nothing.
  Red when: a malformed token or a doubled tag goes unprinted, or a well-formed value prints.
- **AC5** — When `COMPUTERNAME=desktop-3j1o6cd USERNAME=agent5 bash tools/unattended/unattended.sh --preflight fx --keepalive-id k1`
  runs in fixture G, stdout carries `landing — handoff` naming `desktop-3j1o6cd/agent5`, and
  `RUN.md` reads `landing: handoff`. With the environment naming `compeeto/d41ly`, the line reads
  `landing — lander · node d` and the fact reads `landing: lander`.
  Red when: an unlisted node records `lander`, or a listed node records `handoff`.
  `fixture:` G is a bare origin and a clone carrying this tree's kit, a build `fx` authorized at the
  anchor, and an `.unattended.conf` at BASE declaring `LANDING_NODES="a=desk-a/daily-agent d=compeeto/d41ly"`.
  The tree holds none today; build it under `%TEMP%/ln20` from the recipe the driver suite's
  preflight fixture uses. `cost:` a full preflight, seconds to a minute.
- **AC6** — When G's BASE conf declares no `LANDING_NODES` and the working copy declares
  `LANDING_NODES="b=desktop-3j1o6cd/agent5"`, the node-`b` preflight of AC5 prints
  `landing — undeclared` and writes no `landing` fact. When BASE declares the AC5 value and the
  working copy adds node `b`, the node-`b` preflight still prints `handoff`.
  Red when: the working copy's value decides anything.
- **AC7** — When a node-`b` `--close fx --override build-complete --reason r` runs in G after
  preflight, it is refused by an `UNATTENDED check <n> FAILED` line naming `--park` and
  `--handoff`, stdout carries no `observing the anchor` line, and `git status --porcelain` shows
  the record unchanged.
  Red when: the override is parked, or the anchor is observed first.
- **AC8** — When a node-`b` `--close fx` runs in a copy of G whose Definition of Done is met, it
  exits non-zero with a numbered refusal naming `--handoff fx --code owner-landing`, `RUN.md` carries
  the `gates-run` fact, and `grep -c '^phase: LANDING' RUN.md` prints `0`. The `--handoff` that
  refusal names then completes and writes `phase: HELD`.
  Red when: the close writes LANDING, writes no bar fact, or the named hand-off is refused for a
  missing bar.
  `cost:` a DoD-met fixture, built by hand from the driver suite's met-close recipe; minutes.
  `fixture:` needs `TOOL-dUnstuckLanding-13` built first.
- **AC9** — When G's preflight ran as node `d` and the close runs as node `b`, the close prints the
  disagreement and refuses as AC8 does.
  Red when: the recorded `landing: lander` lets node `b` land.
- **AC10** — When the AC8 close runs as node `d`, it writes `phase: LANDING` as it does at BASE.
  Red when: a listed node's close is refused or changed.
- **AC11** — When `grep -n 'LANDING_NODES' tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/check-unattended.sh`
  runs, it shows the example declaration, a §8 table row, the leg's initialiser, an allow-list
  entry between the `gov:conf-allow-begin` and `gov:conf-allow-end` sentinels, and the new check
  calling `landing_nodes_malformed`.
  Red when: any of the five is missing, which check 22's join would also report.
  `cost:` observing the leg end to end costs a full leg run; the bar at the close is where that is
  paid, and this criterion does not run it.
- **AC12** — When `grep -n 'landing' tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md`
  runs, PROTOCOL §2 lists the `landing` fact, §6 carries the hand-off-node sentence, the
  close-decision table carries the hand-off row, VERBS' `--preflight` and `--close` entries mention
  it, and `cmp` of each template against its `memory/guides/UNATTENDED-*.md` render reports no
  difference.
  Red when: a carrier is missing, or a render is not re-copied.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `memory hygiene` · `recall floor` · `recall floor arms`

The suite arms are held self-tests and run only on demand; they are declarations, not part of this
unit's verification, which is the direct checks in §6.

New arm: tools/unattended/unattended.test.sh · a preflight and a met close as an unlisted node, a listed node, and with the key blank at BASE but set in the working copy · none
New arm: tools/unattended/unattended.test.sh · an override close on an unlisted node, asserting the refusal's literal text and an unchanged record · none
New arm: tools/unattended/check-unattended.test.sh · a fixture conf declaring a malformed pair and a doubled tag, asserting the new check's literal text · none

## 8. Open questions

- **F1 — where `LANDING_NODES` is read.** (a) The working copy the driver sources. (b) The conf blob
  at BASE. RESOLVED (agent, 2026-10-04, delegated): (b). Option (a) lets a run declare itself able
  to land, which widens the landing surface (veto 3); (b) reuses the `SPEC_AUDIT_DEFAULT` read.
- **F2 — what `--close` does on a hand-off node.** (a) Refuse before the bar. (b) Run the DoD, write
  the bar's facts, then refuse naming `--handoff`. (c) Write HELD itself. RESOLVED (agent,
  2026-10-04, delegated): (b). Option (a) leaves no `gates-run` fact, so unit 13's guard refuses the
  very exit this unit designs, and AC8 fails. Option (c) is a second writer of the terminal unit 13
  owns.
- **F3 — what a blank key means.** (a) Every node may land, announced. (b) No node may land.
  RESOLVED (agent, 2026-10-04, delegated): (a). Option (b) changes every adopter's landing on
  upgrade and fails the ask's "a resolved listed node is unchanged" for any project not yet
  declaring the key.
- **F4 — whether the leg grades the value.** (a) The driver only. (b) The leg too, through the same
  library function. RESOLVED (agent, 2026-10-04, delegated): (b). A typo otherwise makes a node hand
  off forever with nothing red; one spelling in the library keeps the two readers from disagreeing.
- **F5 — overrides on a hand-off node.** (a) Park them as on any close. (b) Refuse them up front.
  RESOLVED (agent, 2026-10-04, delegated): (b). The design says the hand-off needs no override;
  parking one for a close that lands nothing records a waiver of an obligation the run never meets,
  and a later close on a listed node would park it twice.
- **F6 — exact or substring match.** RESOLVED (agent, 2026-10-04, delegated): exact, lowercased.
  The substring form is the one measured wrong, cited in §4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from design section 7 at rev-2, review item M9, and ask
  `TOOL-dUnstuckLanding-10`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve which registered node this machine and user is,
to decide whether it may land"` returned only Python name-stem neighbours, and its coverage line
reports `.sh` as an unscanned layer, so the map cannot see the driver. Read against source, the
seams this unit extends are:

- `read_host_name` in `tools/unattended/lib-unattended.sh:341`, the one node-name reader the lease
  writer uses. The design record and review item M9 both say the driver has "no node reader"; that
  is stale, since the lease already records `host:` through this function. What was missing is the
  USER half, which S1 adds beside it.
- The BASE-blob read in `check_authorization`, `tools/unattended/unattended.sh:2360-2372`, reused
  for `LANDING_NODES`.
- The unmet `gates-green` arm's early `gates-run` write, `tools/unattended/unattended.sh:7645-7659`,
  the precedent for S5's refusing close that records the bar.
- `tools/drift-audit/drift_report.py:2443`, a node-tag resolver, deliberately NOT reused, for the
  reason §4 records.

Recall terms used: `python tools/memory-recall/query.py "which node may land an unattended run, and
how is the node identified by machine and user rather than path" --terms "node registry machine
user hostname COMPUTERNAME read_host_name lease landing capability handoff preflight LANDING_NODES"`
