# aPromptedMandate — can a prose-started run authorize itself? Measured.

**Serves:** research TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2

Node `a`, 2026-08-18. Kit `unattended@1.6` as shipped, unmodified. Fixture: a bare origin advertising
`refs/heads/main`, a clone, a unit branch. The question the ask forces: does prose-plus-a-flag need a
new authorization primitive, or does one already exist?

## The candidates

| | Candidate | Verdict |
|---|---|---|
| A | reuse `ANCHOR_SCOPE="published"` — the run authors the build folder, commits, pushes the branch, preflights against the branch tip | **chosen** — measured working, opens nothing new |
| B | a new `ANCHOR_SCOPE` value or a new authorization kind for prompt mode | rejected — spends a NEW property, and widens leg check 13 for every adopter |
| C | the owner commits the build folder first | rejected — this is the status quo the ask names as insufficient |

B was rejected on cost, not on difficulty. Protocol §1 enumerates three things the second anchor
already spends and §9 states what the kit does and does not close; a third anchor would extend both
lists, and A needs neither extension because the run-branch anchor already admits exactly this act.

## The measurements

Each ran against a live control — the same tree, one condition changed.

**A1 · self-authored build folder, branch NOT pushed.** Refused:

```
UNATTENDED check 32 FAILED — the remote advertises no tip for the branch this run is on,
so nothing published authorizes it; push the branch first: refs/heads/unit
```

**A2 · same tree, branch pushed.** Accepted, and the record names the anchor it used:

```
unattended: preflight OK — base 82d6161 · anchor refs/heads/main at 561fa6b · keepalive k1
anchor-kind: run-branch
branch-ref: refs/heads/unit
```

**A3 · the gate leg over that same tree**, with the full fixture (both protocol halves, the shipped
Skill template, the real build method): **exit 0**. Checks 9 and 13 — the two that ask whether the
recorded BASE is published and whether a build README resolves there — are silent. This is the
measurement that matters, because check 13 is unconditional over every tracked run-state file and
cannot be gated on the conf: had it refused, a prose-started run would red the bar permanently, for
every future bar run in the repo, not just its own.

**A4 · the roster grows after preflight** — which is what a research pass DOES, since the unit set is
its output. No roster refusal; only the ordinary unmet-DoD blocks. Protocol §1 predicts this in
words ("roster integrity becomes satisfiable by construction" on the branch anchor) and the
measurement agrees. Recorded here because the prediction and the code could have disagreed:
`check_authorization` compares the roster whenever the BASE blob carries the markers, with no
anchor-kind condition, and it is the run's own push that re-satisfies it.

## What the measurement does NOT establish

A3 was run in a clone this run controlled, which is the exact reduction §9 makes: a leg run under the
run's own uid asserts internal consistency, not authorization. Nothing here weakens or strengthens
that. What A1–A4 establish is narrower and sufficient: the prompt path needs no new authorization
code, and the two-command self-authorization it relies on is one the record already prices and the
owner already accepted.

## What this leaves for the build

Authorization: nothing. Everything else: a mode bit that survives to the record, phases for the
research and test work, a method section the directives can point at, the directives, the Skill
path, and the cross-component arm that would have produced A1–A4 automatically.
