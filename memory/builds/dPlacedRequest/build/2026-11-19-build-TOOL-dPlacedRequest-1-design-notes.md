**Serves:** research TOOL-dPlacedRequest-1

# TOOL-dPlacedRequest-1 — the design record its §4 points at

Moved whole out of `TOOL-dPlacedRequest-1`'s §4 at rev-8, on 2026-11-19, by the disposal of
`2026-11-19-review-dPlacedRequest-spec-audit-round-1` (finding 24, L10), so the spec measures under the
49152-byte ceiling of `memory/builds/*/spec/` (`tools/template-size-limits.txt`). Nothing here was
re-decided by the move; the spec's S6 and S8 point here. "The rows" did not move: the spec's S2 and
S11 now carry it, with the legacy row's field 2 that finding 22 asked for.

## The record

```
gov-claim dExample/unit/TOOL-dExample-3

slug: dExample
node: daily-agent
host: COMPEETO-AGENT
session: 5f0c…
keepalive: absent
status: live
lease-utc: 2026-10-25T09:00:00Z
beat-utc: 2026-10-25T09:40:12Z
epoch: 3
kind: unit
fleet-tag: a
renews: yes
witness: 3f9c2a71…
offer: -
offer-deadline: -
last-fetch: -
```

A lease taken by a step checklist outside a run has no keepalive and writes `absent`. A run claim
keeps its keepalive, session and host rules from the run-state file, unchanged
(`tools/unattended/unattended.sh@875eaadf:2405-2410` at the pinned base).

## The table, extended

| claim read | `lease` acquire | `lease` take-over | `lease` renew | `lease` release |
|---|---|---|---|---|
| none | create, epoch 1 | create, epoch 1 | not written, exit 2 | not written, exit 2 |
| mine | renew | renew | renew | write the status |
| same session | rewrite | take, epoch +1 | rewrite | write the status |
| foreign `live` or `held` | refused `live-holder` | refused `live-holder` | refused `live-holder` | refused `live-holder` |
| foreign `stale` | refused `live-holder`, naming `take-over` | take, announced, epoch +1 | refused `live-holder` | refused `live-holder` |
| foreign `terminal` | refused `tombstone` | refused `tombstone` | refused `tombstone` | refused `tombstone` |
| `unknown` | refused `live-holder` | refused `live-holder` | refused `live-holder` | refused `live-holder` |

The run columns of the stops guide's section 7 keep every cell; their takes now bump the epoch.
`CLAIM_READS` gains no class here. `check_claim_writable` reads the eighteen fields.

## The witness under `progress`

`--witness <sha>` must name a commit the clone holds that records a transition of this build, on the
channel TOOL-dDeclaredLoop-3 S7's `read_transitions(build, repo)` reads (its §4 "The source, by
selection"). `transitions.record` is read once per process through the same `policy.py get` S12 makes,
its catalogue default all three channels until dGroundRules' reader lands (TOOL-dDeclaredLoop-3 S4).
With `trailer` selected, the commit's `Gov-Transition` trailer names the build, read with one
`git log -1 --format='%(trailers:key=Gov-Transition,valueonly)'`. With `log` and no `trailer`, the
commit adds a `-transition-<n>.md` record under the build's `build/` folder whose `**Build:**` names
it, read with `git diff-tree --no-commit-id --name-only -r <sha>` and `git show <sha>:<path>` (§8 F8).
With `micro-format` alone nothing is stored, so no commit witnesses and `progress` renews nothing. A
sha that does not resolve, or that records no transition of the build and is no question witness
(below), exits 2. A beat (`--beat`, `write_claim_beat`, `:2469`) and every holder write the driver
makes without a new witness write `renews: no`; they still move `beat-utc`, which the liveness verdict
reads until `TOOL-dPlacedRequest-17` replaces it. The driver passes the newest commit on the run's
branch that records a transition of the build, read as above, as its witness when one exists. Until
dWellOiledMachine's executor writes transitions at item boundaries, a run lease therefore renews only
when a transition is recorded by hand, and this is the interim v2:1159 journals.

## The question witness

`check_lease_witness <slug> <sha>` is the one witness check `--lease renew` runs, and the no-write
probe KICK-dKeptSession-25 §8 F7 (b) calls: it prints `transition`, `question`, `question-closed` or
why it admits none, exiting 0, 0, 1 or 2. It applies its tests in one order. First, where `declare -F`
finds both functions, it runs `read_mailbox <slug> soft`, whose fetch is the only remote read the check
makes. Second, it resolves `<sha>` with `git rev-parse --verify --quiet <sha>^{commit}`, after that
fetch, and a sha that does not resolve exits 2 whatever the mailbox printed. From here on `<sha>` is
that resolved full 40-hex sha, never the argument as typed: the record's `witness` field is written
with it, the differs-from-the-record test compares it, and the mailbox row's `commit` is matched
against it, so a short sha, a full one and a ref name naming one commit are one witness (the
disposal of `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`, finding 22). Third, it classifies the
resolved commit: a transition of the build, read as the section above states, answers `transition`.
Otherwise it answers `question` when `declare -F` finds both `read_mailbox` and
`check_mail_deadline`, and `read_mailbox <slug> soft`, which prints only messages addressed to the
build, prints a row of kind `question`, commit `<sha>` and state `open`. That reader prints
`expired` for a row whose `check_mail_deadline` returned 0 (KICK-dKeptSession-24 S5), so an `open`
row is inside its declared deadline on this node's clock. A `question` witness renews whatever the
record's `witness` holds, so a wait renews at every beat; a `transition` witness keeps the
differs-from-the-record rule. With either function absent, a question commit exits 2 as above.

The beat's probe and `--lease renew` each run this check, in two processes, on two mailbox reads and
two clocks, so a question can expire or be answered between them. The renew's own reading is the one
that counts, and a closed question is no error. A commit that `read_mailbox` prints as a row of kind
`question` to the build in any state but `open` answers `question-closed`, exit 1. On exit 1 the renew
writes the record as a beat does: `renews` as `TOOL-dPlacedRequest-25`'s `derive_lease_renews` gives it
for no witness, `no` under `progress`, and `witness` left at the record's value. The beat loses no
record, and a closed question still renews nothing.

## The policy reads

| Key | Values | Default | Read where |
|---|---|---|---|
| `leases` | warn, refuse | warn | the overlap's verdict (S9) |
| `leases.granularity` | build-and-unit, build, unit | build-and-unit | `--lease acquire` (S7) |
| `leases.renewal` | progress, activity, fixed, none | progress | every lease write (S8) |
| `leases.overlap` | kit-dirs, files, builds | kit-dirs | the overlap's reduction (S9) |
| `leases.offline` | warn, refuse, follow-leases | warn | an unanswered read (S10) |

Defaults from v2:1157-1162. A policy file cannot hold `leases` and a `leases.*` key together
(TOOL-dGroundRules-1 §8 F5); a project setting one reads the other at its default.

Moved here from the spec's §4 on 2026-11-19 by the disposal of
`2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`, with nothing re-decided; the spec's S7 to S10
and S12 state each key's values and default.

## The overlap reduction

The probe drops `SHARED_RECORDS` and the index half of `GENERATED_INDEXES` first
(`tools/unattended/unattended.sh@875eaadf:3803-3805`), then reduces the rest. `kit-dirs` reduces a
`tools/<kit>/…` or `skills/<skill>/…` path to that directory and joins every other path as `files`
does, so two builds editing one kit overlap and two touching only their own `memory/builds/<slug>/`
do not. `files` is today's join, a path or a directory the other sits under. `builds` keeps that join
and prints one finding per other branch. The population stays every unmerged remote branch within
`OVERLAP_AGE_DAYS`.

`--lease acquire` sets `ASHA` from the claim remote's local `refs/remotes/<remote>/HEAD`, as
`print_overlaps` does (`tools/unattended/unattended.sh#print_overlaps`), and passes a build lease's
slug, a unit lease's build slug, or for a cadence run lease the empty slug, the attended semantics. The probe's four UNAVAILABLE exits, an unset or unresolvable anchor,
no scratch directory, an unlistable own diff and unlistable tracking refs, each return 0 at base; under
`refuse` each returns 1 and its line is the refusal's cause, and the summary line that reads `this run
is NOT blocked` at base (`tools/unattended/unattended.sh@875eaadf:3884`) reads `refused` instead.

Moved here from the spec's §4 on 2026-11-19 by the disposal of
`2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`, with nothing re-decided, to keep the spec under
its ceiling as that audit's findings folded in.

## Migration

Lazy and additive (the spec's §8 F3): the reader reads both namespaces and the first write moves a slug
onto its lease, parented on the legacy tip. No ref is deleted. The suite's `refs/gov/runs` fixtures
move to the lease ref with the tests that assert a write's position.

## Rollout

Dark behind `RUN_CLAIMS`, as today. This repository's conf has it `on` (`.unattended.conf:162`), so
its runs move onto build leases at their next claim write; an adopter's stay untouched until it opts in.

## Alternatives rejected

- **A `[[upgrade]]` step that copies every run claim at once** (dSafePassage-1 S1). A step's `down`
  would have to delete leases, which `TOOL-dPlacedRequest-16` forbids, and the lazy read needs none.
- **The fleet tag parsed from `fleet.toml` in shell.** `read_fleet` is the file's one reader and
  grades every row; a second parser is a second grammar.
- **A `writes` key in the record for the overlap.** I6 fixes the keys, and the probe already derives
  each branch's write set from its specs' Files touched (`:3458`).
- **A `READER_SHAPES` row for `read_lease_policy <key>`.** It re-derives `read_spec_audit_switch`'s
  resolution beside it and widens the policy kit for one wrapper; literal `get` lines need no row
  (finding 16 of the same audit).
- **Reducing every non-kit path to its first segment under `kit-dirs`.** Every build branch commits
  under `memory/builds/<slug>/`, so every pair would join on `memory` (finding 26 of the same audit).

## The forks, as written before the move (§8)

The spec's §8 keeps each fork's question, pick and mark; the options and why each lost are these, as
rev-7 wrote them. Each fork id below is the spec's, and the marks here are copies, not a second
resolution.

- FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py@772ccec8:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- F2 — Does the migration retire `RUN_CLAIMS`? I24 keeps it "until unit 1's migration retires it";
  `leases` has no off value (v2:1157). (a) Keep it as the switch every lease read and write sits
  behind; (b) retire it, leases always on. (b) lands a Tier-2 write surface live in every adopter,
  against the charter's `[small]` rule. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; retiring
  the switch is an owner's default change after the chain lands. widens: none · relaxes: none
- F3 — How do run claims migrate? (a) Lazily, the reader reading both namespaces and the first
  write parenting the lease on the legacy tip; (b) an `[[upgrade]]` step copying every claim. (b)'s
  `down` must delete leases, which clause 0134 forbids, so veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- F4 — Which lease does a run hold under `leases.granularity: unit`? (a) The build lease always,
  the key governing the checklists' acquisitions; (b) no build lease, so a run holds no claim. (b)
  removes the one exclusive claim section 7 exists for, and v2 names no run without a claim.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- F5 — What witnesses progress for a run lease before any caller records a transition? (a) Only a
  recorded transition of the build, as clause 0120 and v2:1159 state, read on the channel
  `transitions.record` makes the source; (b) also the driver's `Pass:` commits and phase moves. (b)
  renews on a witness the clause does not name, which veto 1 discards. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1, TOOL-dDeclaredLoop-3 S4 and S7 at `783f1ad3a`, whose channel set is any
  non-empty subset, so a trailer-only read, this fork's first pick on 2026-10-25, never renews under
  `["log"]`; the consequence, a long run reading stale once `TOOL-dPlacedRequest-17` lands, is listed
  in §5 and is the interim v2:1159 journals. widens: none · relaxes: none
- F6 — What do `fixed` and `none` mean, which v2 names without defining? RESOLVED (agent,
  2026-10-25, delegated): `fixed` renews only at acquisition, so the lease expires `leases.expiry-hours`
  after it is taken; `none` tracks no renewal and the lease never expires, ending only by release or a
  take-over the holder's own session makes; rung 3, the reading of walk C2's value names.
  widens: none · relaxes: none
- F7 — How do the three `leases.overlap` values reduce a path? RESOLVED (agent, 2026-10-25,
  delegated): as §4 "The overlap reduction" states, `kit-dirs` coarsest by directory and `builds`
  coarsest in its report; rung 3, from the value names and coordination item 3's "against every live
  lease at `leases.overlap`'s granularity". widens: none · relaxes: none
- F8 — How does the bash driver read a log-only transition, when `read_transitions` is a Python
  function with no verb? Options: (a) the driver reads the selected channel itself with two `git`
  calls, on the source TOOL-dDeclaredLoop-3 §4 "The source, by selection" names; (b) an ask for a
  `loop_transition.py read --build <slug>` verb printing `read_transitions`, run as a subprocess
  through `resolve_kit_dir`; (c) `python -c` importing `loop_transition`, a kit importing a sibling,
  which TOOL-dDeclaredLoop-12 S4 bars after TOOL-dGroundRules-1 §4 Evidence. (a) restates which channel is the source, held to that table by
  AC4's `["log"]` plant; (b) waits on a parent change for a read two `git` calls make. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- F9 — The question witness (S8) rests on dKeptSession, a child build landing after this unit; how
  is it built here? `read_mailbox` (KICK-dKeptSession-5 S6), `check_mail_deadline`
  (KICK-dKeptSession-24 S3) and the `question` kind are neither in the tree nor minted by this build
  or a parent. Options: (a) the branch built here, armed only when `declare -F` finds both functions,
  observed on exported stubs (AC11), inert until dKeptSession lands; (b) S8 left at the transition
  rule and the ask returned, KICK-dKeptSession-25 extending `check_lease_witness` in its own pass, as
  KICK-dKeptSession-12 §8 F3 builds its switch in this build's code; (c) a mail reader minted here, a
  second reader of KICK-dKeptSession-5's records. (c) writes one grammar twice; (b) leaves the
  adopted ask unbuilt; KICK-dKeptSession-25 §8 F7 (b)'s probe expects the check here. RESOLVED
  (agent, 2026-11-19, delegated): (a), rung 3; it calls the child's mints by name only and is inert
  until dKeptSession lands, so no veto trips. widens: none · relaxes: none
