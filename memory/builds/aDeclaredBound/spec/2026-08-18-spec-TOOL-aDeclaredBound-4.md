# TOOL-aDeclaredBound-4 — agent-cap reads a declaration: lowering is free, raising is attributed

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

`agent-cap.js` holds three fan-out bounds as file constants and refuses an environment override on
the record. Give the owner a channel to change them that keeps every property the refusal was
protecting, and make an agent's use of that channel loud rather than impossible — because impossible
is not on offer and this spec will not pretend otherwise.

## 2. Scope (IN)

- **S1** — three declarations in a repo-root `.agent-cap.conf`: `CONCURRENCY_CAP`, `VERIFIER_CAP`
  and `LENS_CAP`, mapping to the hook's `CAP`, `MAX_VERIFIERS` and `MAX_LENSES`. Named so none of
  them collides with `AGENT_CAP`, which stays a refused environment variable and must not read as
  the same knob under a new spelling.
- **S2** — the hook resolves the file by walking UP from its own location, bounded by a `.git`
  entry. Not by counting directories: this repo records a kit that broke silently at any other
  install prefix by doing exactly that, and the hook is installed at `.claude/hooks/` in a target
  while its source sits at `tools/hooks/`.
- **S3** — **lowering is free.** A declared value at or below the shipped constant applies with no
  ceremony, because a tighter bound is never the risk this guard exists to manage.
- **S4** — **raising is attributed.** A declared value ABOVE the shipped constant applies only when
  the declaration carries an attribution line for that key, in the grammar
  `# RAISED <old> -> <new> (owner, <date>): <reason>`. That is deliberately the same
  `<old> -> <new>` form `drift_report.py`'s `_justified` already reads, so one written sentence
  satisfies both the hook and the ratchet.
- **S5** — every failure direction falls back to the SHIPPED constant, never higher: no file, an
  unreadable file, a malformed value, a raise without attribution. A guard that fails open is worse
  than no guard, and the fallback is the shipped number rather than the declared one precisely so a
  malformed raise cannot be a working raise.
- **S6** — an ignored raise is REPORTED, not silent. When the hook denies a call it already prints a
  message; when it has ignored an unattributed or unusable declaration it says so in that message,
  naming the key and what it used instead. A knob that silently does nothing is the class the
  refused env override was deleted for.
- **S7** — the environment refusal is UNCHANGED, and its comment gains one clause explaining why a
  file is admissible where an env var was not: a committed declaration leaves a diff, a blame line
  and a reviewable justification, and an env read leaves none of those.
- **S8** — the three keys are declared as drift-audit ratchets with `weakens: "up"`, so a raise that
  lands without its justification reds the bar rather than merely being unenforced.
- **S9** — a BINDING rule in `memory/guides/REVIEW-PROTOCOL.md`: an agent does not raise a declared
  cap without an explicit owner request in the conversation that asked for it. Lowering, and any
  change made because the owner asked, are ordinary work.
- **S10** — the same section states plainly what the mechanism does NOT do — see section 4 — on the
  model of `memory/guides/UNATTENDED-PROTOCOL.md` §9, which already says what a check running under
  a run's own uid can and cannot buy.
- **S11** — `KIT_AGENT_CAP_VERSION` moves, both copies of the hook stay byte-identical, and the
  self-test covers every resolution branch in S3 through S6.

## 3. Non-goals (OUT)

- No value changes. Every bound stays 5 until an owner declares otherwise.
- `AGENT_CAP` stays refused. This unit adds a channel; it does not reopen the one that was closed.
- The two rules stay two rules. `CONCURRENCY_CAP` and `VERIFIER_CAP` are separate keys with separate
  defaults even though both are 5, because `memory/gotchas/concurrency-is-not-a-budget.md` exists
  from conflating them once.
- No per-workflow or per-invocation override. The declaration is per repository. A per-call knob is
  the env override wearing a different hat.
- The hook does not validate that a declared lower bound is workable. An adopter who declares two
  lenses will have `tools/workflows/tier2-review.js` denied, because it has four. That is their
  choice and it fails CLOSED, which is the safe direction.

## 4. Design

### Data model

| key | maps to | shipped default | ≤ default | > default |
|---|---|---|---|---|
| `CONCURRENCY_CAP` | `CAP` | 5 | applies | needs attribution |
| `VERIFIER_CAP` | `MAX_VERIFIERS` | 5 | applies | needs attribution |
| `LENS_CAP` | `MAX_LENSES` | 5 | applies | needs attribution |

### What this buys, and what it does not

The recorded objection to a knob here is precise, and worth quoting rather than paraphrasing: an
env-settable ceiling *"is the defeatable class this guard exists to remove, and it leaves no diff
behind when someone raises it."* Every clause of that is about the CHANNEL. A committed file is the
opposite on each: it leaves a diff, the diff has an author and a date, the justification is in the
same commit, and the drift ratchet reds if the justification is missing.

**What it does not buy is prevention.** An agent with shell access can edit `.agent-cap.conf`, write
its own attribution line, edit `drift_signals.py` to drop the ratchet, and edit the hook itself. No
arrangement of files in this repository changes that, and a spec that implied otherwise would be
selling the same false comfort as the override this design keeps refusing. The protocol §9 already
makes this argument for unattended runs and this unit points at it rather than restating it.

So the honest claim is: **an agent cannot raise this quietly.** Raising it requires an edit to a file
whose only purpose is this number, in a shaped sentence naming the owner and both values, or the bar
reds. The control that actually binds is the same one §9 names — review of the diff, by a human, on
the remote.

### Why a file at the repo root rather than beside the hook

The hook is deployed verbatim to `.claude/hooks/` and its source lives at `tools/hooks/`; the two
copies are byte-identical today and S11 keeps them so. A declaration beside the installed copy would
either have to exist beside BOTH or make them differ. The root is also where every other per-repo
declaration in this tree lives, and the walk-up-bounded-by-`.git` idiom is already the recorded
correct way to find one.

### Rollout

The file is absent in every existing tree, and absent means shipped constants, so nothing changes on
the day this lands. This repo declares nothing: gov's own caps stay at their constants, which makes
the shipped path the one the corpus exercises. An adopter who wants a different bound writes three
lines.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` and its byte-identical `.claude/hooks/` copy — the resolver, the three
  reads, S6's reporting, S7's comment, the version constant.
- `tools/hooks/agent-cap.test.sh` — S11's branch coverage.
- `tools/drift-audit/drift_signals.py` — three ratchet declarations.
- `memory/guides/REVIEW-PROTOCOL.md` — S9 and S10. A read-path member; unit 5 shrinks it first.
- A shipped `.agent-cap.conf.example`, and the kit's README.

### Alternatives rejected

- **A key in `.memory-tree.conf`.** Rejected on the reasoning `TOOL-aDeclaredCeiling-1` ratified:
  an unrelated kit's conf must not become the home of another kit's constant.
- **Keep the constants and let the owner edit the hook.** Rejected: it is what happens today, it
  makes every adopter's hook differ from the shipped one, and it gives the byte-identical-copies
  property away for a value that changes rarely.
- **Let the declaration raise freely, with only the drift ratchet behind it.** Rejected: the ratchet
  runs on the bar, and the hook runs on every tool call. A raise would be in force for the whole
  session before anything reported it.
- **Require attribution for LOWERING too.** Rejected: it prices the safe direction the same as the
  unsafe one, and the predictable result is that nobody lowers.

## 5. Production-readiness checklist

- security — this is the security-shaped unit of the build, and section 4 states its limit rather
  than its promise. The fallback direction is the control that matters: every failure yields the
  shipped constant, so no malformed input widens a bound.
- perf / scale — one small file read per `Workflow`/`Agent` tool call, on a path that already reads
  stdin and parses a script. Measured before landing, and cached within a single hook invocation.
- a11y · i18n — N/A.
- error / empty / loading states — S5 enumerates all four failure directions; S6 makes each visible.
- observability — S6. An operator who declared a raise and did not get one is told which key was
  ignored and what was used instead.
- risks — the honest one is a false sense of enforcement, addressed by S10 in the binding document
  an agent actually reads. The mechanical risk is a resolver that finds the wrong file at an unusual
  install prefix, which S2 addresses with the idiom this repo already had to learn once.
- testing + left-shift gates — S11's branch coverage plus S8's ratchet, which is the left-shift for
  the raise-without-justification case.
- migration / rollback — delete the file.
- user docs — the example conf, the kit README, and S9's protocol section.

## 6. Acceptance criteria

- **AC1** — When no `.agent-cap.conf` exists, `bash tools/hooks/agent-cap.test.sh` observes all
  three bounds at their shipped constants, and a script fanning to 6 is denied.
- **AC2** — When a fixture declares `LENS_CAP=3`, a five-lens script that passes today is DENIED,
  and the denial names the declared bound rather than the shipped one.
- **AC3** — When a fixture declares `LENS_CAP=8` with NO attribution line, an eight-lens script is
  denied at 5 and the hook's message names the ignored key.
- **AC4** — When the same fixture adds `# RAISED 5 -> 8 (owner, <a date>): <a reason>` above the
  key, the eight-lens script is allowed.
- **AC5** — When a fixture declares a non-numeric or negative value, `bash
  tools/hooks/agent-cap.test.sh` observes the shipped constant applying and the hook's message
  saying the declaration was unusable.
- **AC6** — When `AGENT_CAP=99` is set in the environment alongside a valid declaration, the
  refusal fires exactly as it does today — the file channel does not resurrect the env one.
- **AC7** — When a raise lands in `.agent-cap.conf` without the `<old> -> <new>` form in its
  justification window, `python tools/drift-audit/drift_report.py --check` reports a weakened
  ratchet.
- **AC8** — When `diff tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` runs, it is empty.
- **AC9** — When `bash tools/workflows/check-verifier-fanout.sh` runs, it enforces the declared
  bound, which it inherits by delegating to the hook rather than by reading the file itself.

## 7. Gates

`bash tools/hooks/agent-cap.test.sh` · `bash tools/workflows/check-verifier-fanout.sh` · `bash
tools/workflows/check-verifier-fanout.test.sh` · `bash tools/workflows/check-protocol-parity.test.sh`
· `python tools/drift-audit/drift_report.py --check` · `python tools/drift-audit/selftest.py` ·
`bash tools/check-kit-versions.sh` · `bash tools/check-wiring.sh --check` · `bash
tools/memory-tree/check-memory-hygiene.sh` · and `GATE_FULL=1 bash tools/run-gates.sh` at the push
boundary.

## 8. Open questions

- **The attribution line is not a credential.** An agent can type `(owner, <date>)` as easily as a
  person can, so S4 is a speed bump and an audit artifact rather than an authorisation check. The
  design takes that as acceptable because the binding control is diff review, per section 4. The
  owner may prefer a stronger form — a signed commit trailer, or a value that must match something
  outside the repository — and that is a decision about how much ceremony a rare edit deserves.
  RECOMMENDATION: ship the shaped comment. It is the only form that costs nothing when unused, and
  the two stronger options both put a per-node setup burden on every adopter to raise a bound most
  of them will never touch.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a per-adopter numeric limit from a declaration
instead of a source constant"` returns file readers at the top and no seam for this shape, which is
the honest answer: no kit in this tree currently reads a per-repo declaration from a JavaScript
hook. What it does return, and what this unit reuses, is the SHAPE rather than the code —
`tools/lexicon/lexicon_conf.py` and `tools/memory-tree/row_grammar.py`'s `pin_of` both implement
"absent means the shipped default, malformed is a named refusal", and S5 is that contract with the
fallback direction made explicit for a security-shaped knob.

`python tools/memory-recall/query.py "why is the agent fan-out cap a file constant rather than a
configurable value" --terms "agent-cap CAP MAX_LENSES verify stage fan-out cap constant override
AGENT_CAP refused review protocol concurrency rate limiter"` is the set's recall probe. It returns
the decision this unit is in tension with and must therefore honour: the env override was deleted
because it was defeatable and left no diff. Section 4 answers that record on its own terms rather
than around it. `TOOL-aDeclaredCeiling-1` supplies the second binding rule — a declared value with
its movement history beside it, in a file that belongs to the kit that owns the value — which is
why the declaration is `.agent-cap.conf` and not a memory-tree key.
