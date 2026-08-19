# TOOL-aDeclaredBound-4 — agent-cap reads a declaration: lowering is free, raising is attributed

**Status:** OPEN · rev-4 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling · ratified 2026-08-18

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
- **S1a** — the conf GRAMMAR is one `KEY=value` per line with `#` comments, which is the only
  shape `drift_report.py`'s scalar reader matches — an anchored `KEY = "?digits"?` on a line of
  its own, comments skipped. A trailing comment on the assignment line makes the ratchet read
  nothing, so the grammar is a constraint on the file this unit ships and not a stylistic note.
- **S1b** — the file is COMMITTED at the shipped values rather than left absent. That is not a
  style choice: S8's ratchet compares the value at the base ref against the value at head, and
  `drift_report.py` SKIPS a file that does not exist at the base. With no committed blob the
  first raise — the one the ratchet exists for — is never compared. A committed file also makes
  the knob discoverable and puts the declared path, not the fallback path, in the corpus.
- **S2** — the hook reuses the resolver it ALREADY HAS. `agent-cap.js` carries a `gitCommonDir`
  walk that goes up bounded by a `.git` entry and handles the worktree case where `.git` is a
  file rather than a directory. This unit does not write a second one. Two things it must state
  that the existing helper leaves open: the declaration is read from the REPO ROOT and not the
  common dir, so every linked worktree can carry its own; and the walk anchors on the same
  payload cwd the existing code anchors on.
- **S2a** — a SECOND walk is written after all, beside `gitCommonDir` rather than replacing it,
  and rev-3's flat "does not write a second one" was wrong. `gitCommonDir` deliberately resolves
  a linked worktree through to the SHARED git dir — its own comment says one budget per repo, not
  per worktree — so a builder obeying rev-3 would read the main checkout's declaration from every
  linked worktree, silently. The new walk returns the directory holding the `.git` ENTRY, which
  is the worktree root. `gitCommonDir` keeps its collapsing behaviour untouched, because the slot
  budget depends on it.
- **S2c** — the Workflow modality has NO fixture isolation today and this unit adds it. The
  payload-cwd anchor rev-3 leaned on is an Agent-modality property: measured, every Workflow arm
  in the harness ships no `cwd` and the suite never changes directory before invoking the hook,
  so those arms resolve against the process cwd — the repo root, where S1b commits the real
  declaration. Since `MAX_LENSES` and `MAX_VERIFIERS` are consumed on exactly that modality,
  every affected arm gains a `cwd` pointing at a scratch tree carrying a `.git` entry, on the
  idiom the Agent arms already use. Without it AC1's premise is unreachable and no fixture
  criterion below can be observed.
- **S2b** — this unit carries the READS-IT half of unit 5's replacement predicate. Unit 5 asserts
  the pointer SHAPE — that each section stating a bound names the file resolving it — and cannot
  assert more, because the conf key and the hook's read of it are minted HERE and land after.
  In the same commit that makes the hook read the declaration, `check-protocol-parity.test.sh`
  gains the second half: the declaration the protocol names is one the hook actually reads.
  Ratified by the owner as a split by landing.
- **S3** — **lowering is free.** A declared value at or below the shipped constant applies with no
  ceremony, because a tighter bound is never the risk this guard exists to manage.
- **S4** — **raising is attributed.** A declared value ABOVE the shipped constant applies only
  when the declaration carries an attribution line NAMING THAT KEY, in the grammar
  `# <KEY> RAISED <old> -> <new> (owner, <date>): <reason>`, within FIVE lines above the
  assignment. Five, and stated rather than left open as rev-3 left it: the file is one key per
  line with a short comment, so five reaches a justification without reaching the previous key's.
  This window is INDEPENDENT of drift-audit's `RATCHET_LOOKBACK`, which unit 3 makes adopter-
  declarable; unit 3's S1c says the same from its side. An adopter who narrows one and not the
  other gets lines the hook accepts and the ratchet reds on, and that is a stated consequence
  rather than a surprise. Three details the first draft left open and each of which is a defect:
  the key must appear, because all three bounds default to 5 and an unkeyed line would attribute
  a raise of one to a raise of another; the window must be stated, or the hook has no rule for
  how far to look; and the HOOK owns the regex, with the ratchet reading the same text through
  its own.
- **S4b** — the two readers disagree about `<old>` after the first raise, and the spec says so
  rather than leaving a builder to find it. The ratchet's old value is the BASE BLOB's value;
  the hook can only know the shipped constant. From a declared 8 to a declared 10, the ratchet
  wants `8 -> 10` and a naive hook would want `5 -> 10`. The rule: `<old>` is the PREVIOUS
  DECLARED value, which is what the ratchet already computes, and the hook accepts any `<old>`
  in a correctly keyed and shaped line rather than checking its value. The hook enforces SHAPE
  and the ratchet enforces ARITHMETIC — one sentence, two readers, neither duplicating the
  other's job. The hook DOES require the stated `<new>` to equal the value it is applying;
  without that, an attribution line left behind by a previous raise authorises any further move
  for the whole session, and only the bar would catch it.
- **S4c** — the RATCHET is made key-aware, and this is a code change to drift-audit rather than a
  statement about it. Its justification matcher is built from the two NUMBERS alone; executed
  over a fixture with all three keys raised to 8 and a single `LENS_CAP RAISED 5 -> 8` comment,
  all three raises read as justified. That is precisely the confusion S4 requires the key to
  prevent, sitting in the reader S4b assigns the arithmetic to, so S4b is false until this lands.
- **S5** — every failure direction falls back to the SHIPPED constant, never higher: no file, an
  unreadable file, a malformed value, a raise without attribution. A guard that fails open is worse
  than no guard, and the fallback is the shipped number rather than the declared one precisely so a
  malformed raise cannot be a working raise.
- **S6** — an ignored declaration is REPORTED ON RESOLUTION, not on verdict. The first draft put
  the message on the denial path, which is the wrong half: a malformed or unattributed raise
  usually leaves the fan-out UNDER the shipped 5, so the call is ALLOWED and the hook exits
  silently — the operator declared 8, got 5, and nothing said so. The hook emits on stderr
  whenever a declaration is present and not applied, on the allow path as well as the deny path,
  naming the key and the value it used instead.
- **S7** — the environment REFUSAL is unchanged, but its MESSAGE is not, and the first draft
  scoped only the comment. The refusal text currently tells the reader that the cap is the file
  constant and that changing it means editing `agent-cap.js` and the review protocol where the
  rule is stated. After this unit the first is untrue whenever a declaration applies, and after
  unit 5 the protocol no longer states it. The refusal keeps its prefix — an existing arm keys on
  it — and its remedy redirects at the declaration.
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
- **S12** — `MAX_LENSES` keeps a LINE-ANCHORED BARE LITERAL for its shipped default.
  `tools/check-playbook-parity.sh` extracts it with an anchored pattern as one of its declared
  pairs, and its anti-vacuity arm reds when an extraction matches nothing. Restructuring the
  assignment into a call would red that gate with a message about an unresolvable pair rather
  than about this unit. The declaration is READ separately; the constant stays where the pair
  can find it.
- **S13** — THREE new files are declared to the deployer, and the mechanism rev-3 named does not
  cover the one that matters. Measured: the govkit surface globs reach `tools/*`, `.githooks/**`,
  `skills/session-kickoff/**` and two playbook root patterns, so a repo-root dotfile is OUTSIDE
  the declared surface and `selfcheck` is green with or without it. The example therefore ships
  from `tools/hooks/.agent-cap.conf.example` with an unprefixed destination, which the per-file
  claim arm does cover; the kit's README is a third new file needing its own rule; and the
  instance `.agent-cap.conf` is per-repo data rather than kit payload, which the spec now says
  outright. `memory/guides/SESSION-KICKOFF.md` records that a new tool at the repo root silently
  leaves the enforced surface — that is the objection §4's prefix-independence argument has to
  beat, and it beats it only for the INSTANCE, never for the payload.

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

The hook runs on the `Workflow|Agent` matcher rather than on every tool call.

**What it does not buy is prevention.** An agent with shell access can edit `.agent-cap.conf`, write
its own attribution line, edit `drift_signals.py` to drop the ratchet, and edit the hook itself. No
arrangement of files in this repository changes that, and a spec that implied otherwise would be
selling the same false comfort as the override this design keeps refusing. The protocol §9 already
makes this argument for unattended runs and this unit points at it rather than restating it.

So the honest claim is: **an agent cannot raise this quietly.** Raising it requires an edit to a
file whose only purpose is this number, in a shaped sentence naming the key and both values, or
the bar reds.

Rev-3 named the binding control as "review of the diff, by a human, on the remote" and attributed
that to the protocol's §9. It says no such thing. What §9 names is the same leg re-run in a clone
the run never touched, by a party the run cannot execute code as — and it forbids any document
here from implying otherwise, which rev-3 did. Corrected: with S4c landed, the control is the
drift-audit ratchet leg re-run where this run cannot reach. Without S4c there is none, because a
key-blind matcher justifies every raise from any one line.

### Why a file at the repo root rather than beside the kit

The first draft justified this by saying the root is where every other per-repo declaration in
this tree lives. That is FALSE and the audit measured it: four declarations sit at the root and
eight are kit-homed, including `tools/template-size-limits.txt`, which `TOOL-aDeclaredCeiling-1`
deliberately placed beside its gate rather than at the root — the same precedent unit 3 of this
build invokes to keep its own value out of a conf.

The reason that survives is PREFIX INDEPENDENCE, and it is specific to this kit. Every kit-homed
declaration is read by an engine that knows its own location, so it can find a sibling. This one
is read by a hook that has been DEPLOYED away from its kit: it runs from `.claude/hooks/` while
its kit dir is `tools/hooks/` here and may be `hooks/` in a root-install adopter. A sibling read
would require the deployed hook to reconstruct an install prefix it does not know, which is the
class this repo records as breaking silently — a kit that resolved its root by counting
directories up answered from an empty corpus at every other prefix. From the repo root the hook
needs no prefix at all.

The cost is S13: a root file that the kit ships is still kit payload as far as the deployer is
concerned, so it needs its rows.

### Rollout

The file is absent in every existing ADOPTER tree, and absent means shipped constants, so nothing
changes for them on the day this lands. This repo COMMITS it at the shipped values, per S1b: the
ratchet needs a base blob to compare against, and a declaration that only appears on the day
somebody raises it is a declaration the ratchet skips exactly once, on the one commit that
matters. Committing it at 5/5/5 also means the corpus exercises the DECLARED path rather than
the fallback.

S8's three ratchet rows carry a liveness statement for the same reason. A ratchet whose file is
absent produces no finding and no complaint, which is indistinguishable from a ratchet that is
watching and content.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` and its byte-identical `.claude/hooks/` copy — the resolver, the three
  reads, S6's reporting, S7's comment, the version constant.
- `tools/hooks/agent-cap.test.sh` — S11's branch coverage.
- `.agent-cap.conf` — the instance, committed at 5/5/5 per S1b. Per-repo data, not kit payload.
- `tools/hooks/.agent-cap.conf.example` and a new `tools/hooks/README.md` — both NEW, both needing
  their own `kit.toml` rules per S13.
- `tools/drift-audit/drift_signals.py` — three ratchet declarations and their liveness statement.
- `tools/drift-audit/drift_report.py` — S4c's key-aware matcher. Absent from rev-3's write set,
  which left S4b describing behaviour nothing in the build could produce.
- `tools/drift-audit/selftest.py` — the arms AC7 observes.
- `tools/hooks/kit.toml` and the govkit registry — S13.
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
- **Kit-owned and EXTEND-ONLY, the shape already built for the unattended directives.** A project
  may add to a kit-owned set and never subtract, which needs no attribution grammar, no ratchet
  rows and no second parser. Rejected because it forecloses the RAISE the owner asked for, and
  that is the only reason — it is otherwise cheaper than the chosen design and the reader should
  be able to price that. Two ratified rows argue for it and are named here rather than left
  uncited: `TOOL-cBriefedPilot-2` refuses a conf key for the directive set because a key lets a
  project declare zero and that is a global waiver carrying no name, no reason and no record; and
  `TOOL-aBoundedVerdict-1` keeps a second cap as a driver file constant on the reused agent-cap
  argument. The second is the cap that governs the review of this very spec.

## 5. Production-readiness checklist

- security — this is the security-shaped unit of the build, and section 4 states its limit rather
  than its promise. The fallback direction is the control that matters: every failure yields the
  shipped constant, so no malformed input widens a bound.
- perf / scale — one small file read per `Workflow`/`Agent` tool call, on a path that already
  reads stdin and parses a script. No caching: the hook is a fresh process per call, so there is
  nothing for a cache to outlive.
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
- **AC4** — When the same fixture adds `# LENS_CAP RAISED 5 -> 8 (owner, 2026-08-18): <reason>`
  within five lines above the key, the eight-lens script is allowed; when the line omits the key,
  or names `VERIFIER_CAP` instead, the lens raise stays unapplied at 5. Rev-3's criterion tested
  the exact unkeyed line its own S4 forbids, so a builder could satisfy one only by failing the
  other.
- **AC5** — When a fixture declares a non-numeric or negative value, `bash
  tools/hooks/agent-cap.test.sh` observes the shipped constant applying and the hook's message
  saying the declaration was unusable.
- **AC6** — When `AGENT_CAP=99` is set in the environment alongside a valid declaration, `bash
  tools/hooks/agent-cap.test.sh` observes the refusal still firing AND its remedy naming
  `.agent-cap.conf` rather than the file constant and the review protocol.
- **AC7** — When a raise lands in `.agent-cap.conf` without the shaped justification, `python
  tools/drift-audit/selftest.py` observes a weakened ratchet — over a fixture whose BASE carries
  the file, since a base without it is the case `drift_report.py` skips.
- **AC8** — When a declaration is present, malformed, and the resulting fan-out is ALLOWED,
  `bash tools/hooks/agent-cap.test.sh` observes the stderr report naming the key. This is the
  arm for S6's correction, and it is the case the first draft could not observe at all.
- **AC9** — When `bash tools/check-playbook-parity.sh` runs, the `MAX_LENSES` pair still
  resolves, and when `python tools/govkit/govkit.py selfcheck` runs, the two new files are
  declared rather than an undeclared widening of the shipped surface.
- **AC10** — When `diff tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` runs, it is empty.
- **AC11** — When `bash tools/workflows/check-verifier-fanout.sh` runs, it enforces the declared
  bound, which it inherits by delegating to the hook rather than by reading the file itself.

## 7. Gates

`bash tools/hooks/agent-cap.test.sh` · `bash tools/check-agent-cap-restatement.sh` · `bash
tools/check-agent-cap-restatement.test.sh` · `bash tools/check-playbook-parity.sh` · `python
tools/govkit/govkit.py selfcheck` · `python tools/govkit/selftest.py` · `bash
tools/workflows/check-verifier-fanout.sh` · `bash
tools/workflows/check-verifier-fanout.test.sh` · `bash tools/workflows/check-protocol-parity.test.sh`
· `python tools/drift-audit/drift_report.py --check` · `python tools/drift-audit/selftest.py` ·
`bash tools/check-kit-versions.sh` · `bash tools/check-wiring.sh --check` · `bash
tools/memory-tree/check-memory-hygiene.sh` · and `GATE_FULL=1 bash tools/run-gates.sh` at the push
boundary.

## 8. Open questions

RESOLVED (owner, 2026-08-18): the shaped comment line, and the repo root for the declaration.

- **The attribution line is not a credential.** An agent can type `(owner, <date>)` as easily as a
  person can, so S4 is a speed bump and an audit artifact rather than an authorisation check. The
  design takes that as acceptable because the binding control is diff review, per section 4. The
  owner may prefer a stronger form — a signed commit trailer, or a value that must match something
  outside the repository — and that is a decision about how much ceremony a rare edit deserves.
  RESOLVED (owner, 2026-08-18): the shaped comment. The owner took the stated limit — it proves a
  raise was deliberate, not that the owner authorised it — and accepted it, because the two
  stronger forms tax every adopter's setup for an edit most will never make, and an unattended run
  on a node without signing configured would simply fail.
- **Where the declaration lives.** RESOLVED (owner, 2026-08-18): the repo root, on the
  prefix-independence reasoning in section 4 rather than the false one the first draft gave. The
  alternative was the kit home, which matches the numerically dominant precedent; it loses because
  a hook deployed away from its kit cannot reconstruct an install prefix, and this repo has already
  paid for that mistake once. S13's deployer rows are the accepted cost.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1, which BLOCKED on this unit. The ratchet in S8
  could not fire: `drift_report.py` skips a file absent at the base ref, and the first draft's
  rollout deliberately left it absent, so the one comparison the design rests on would never
  happen. S1b commits it. S2 was writing a resolver the file already contains. S4's grammar named
  no key while all three bounds share a default, and S4b resolves a disagreement about `<old>`
  the two readers would have had after the first raise. S6 reported on the wrong half — the
  common case for an ignored raise is an ALLOWED call. S7 scoped a comment while leaving a
  refusal message this build makes false. S12 and S13 are gates the unit would otherwise have
  redded: the playbook-parity extraction and the deployer's surface declaration. Section 4's
  root-versus-kit justification was false and is replaced with the one that survives measurement.
- rev-4 · 2026-08-18 · folded spec-audit round 2. The ratchet S4b assigns the arithmetic to is
  KEY-BLIND — one attribution line justifies all three raises, reproduced by execution — so S4c
  makes it key-aware and `drift_report.py` joins the write set it was missing from. S4 states the
  five-line window it had only promised to state, and says it is independent of unit 3's lookback.
  S2a admits the second walk this unit does write, because the existing resolver collapses linked
  worktrees on purpose. S2c adds the Workflow fixture isolation that does not exist, without which
  no fixture criterion here is observable. S2b takes the reads-it half of unit 5's predicate under
  the owner's split-by-landing. S13 was wrong about govkit: a root dotfile is outside the declared
  surface, so the example ships from the kit dir instead, and there are three new files not two.
  Section 4's claim that the protocol's section 9 names human diff review as the binding control
  was false and is corrected against what it actually says. AC4 tested the unkeyed line S4 forbids.
- rev-3 · 2026-08-18 · both forks put to the owner and RESOLVED: the shaped comment line, and the
  repo root. No design change — the owner ratified what section 4 already argued for.

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
