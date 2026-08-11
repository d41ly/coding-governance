# review-aStandingWrit-2 — Tier-2 over the cumulative diff landing on main

**Subject:** `a21a150..HEAD` — 18 files, +636/-285. The six commits that build S1+S2+S3 (the build
folder IS the authorization), S7 (every statement of the rule follows the rule), S6 (the phase
vocabulary gets pass names and a producer), S4 (the gap list, mechanised from M2) and the closing
records pass.

**Review shape:** raw 24 · confirmed 17 · refuted 7 · unverified 0 · precision 0.71.
Every raw finding reached a skeptic; none was left unadjudicated. The 17 confirmed findings collapse
to **11 distinct defects** — four of them were found independently by more than one lens, which is
noted per finding and is itself signal about where the diff is thin.

**Verdict: do not land as-is.** One blocker, four highs. The blocker is not in the kit — it is in
`skills/session-kickoff/SKILL.md`, where S1's class-wide authorization grant was consumed by the
*attended* kickoff path and deleted the engine's only human checkpoint by default.

---

## The shape of the failure

S1 moved authorization from a per-build owner-authored mandate block to the build folder itself.
Inside the unattended kit that move is documented and owner-accepted — protocol §1 cost #2 states the
narrowing plainly. What was not re-derived is everything downstream that had been reading the *old*
predicate as a proxy for "an owner did something deliberate about this specific build":

- `session-kickoff` read it as the trigger for skipping the READY stop → **blocker, F1**
- the leg's degenerate-base refusal was left pinned to the pre-S3 rule → **high, F3**
- the phase vocabulary grew a producer the operating doc never names → **high, F5**
- the test that was supposed to arm S6's new guard passes without reaching it → **high, F4**

Three of the eleven defects are the repo's own named classes turned on the kit that enforces them:
*two-answers-to-one-question* (F3, F5, F11), *fixture-passes-by-finding-nothing* (F4, F9), and
*record-vs-reality* (F7). That is the argument for the left-shift gates below rather than point fixes.

---

## BLOCKER

### F1 — Step 5b's unattended hand-back now fires on tree state alone, so the READY stop is skipped by default

`skills/session-kickoff/SKILL.md:172`

The diff replaces the Step 5b trigger *"a committed standing **mandate** for this build is reachable
from the pinned BASE"* with *"the **build folder itself** is reachable from the pinned BASE."* The old
predicate was a per-build, owner-authored artifact. The new one is satisfied by **29 committed build
READMEs on `main`** (`git ls-tree -r main -- memory/builds | grep -c '/README.md$'`).

Step 5b's two conjuncts are now (a) the project adopts an unattended kit — true in this repo — and
(b) a committed build folder exists. So **any `/session-kickoff` scoped to an existing build**
satisfies the literal condition, and the step's own text then says *"continue without halting"*,
deleting the READY stop that is the engine's only human checkpoint. That defeats AGENTS.md's rule
that merge and push each need an explicit ask, on the ordinary attended path.

The step simultaneously disclaims the one narrowing that survives. It says *"never on the strength of
a chat instruction"*, while `memory/guides/UNATTENDED-PROTOCOL.md` §1 cost #2 states the narrowing
**is** *"the slug the owner types, and chat is not machine-checkable."* The two documents contradict
each other, so nothing narrows the trigger at all.

The class-wide grant is documented and owner-accepted — but the accepted cost is about *unattended
authorization*, not about the default stop disappearing for ordinary sessions. That consumption is
new, undocumented and unratified.

`check-unattended.sh` check 12 (lines 279-289) greps only for the literal `Step 5b`, the READY prompt
string, and an exit count `>= KICKOFF_EXITS`. None of those can see that the trigger widened.

**Fix.** Make an in-session owner signal a *necessary* condition. Step 5b fires only when the owner
invoked the unattended skill naming this slug — the protocol's own stated owner act — **AND** the
build folder is reachable from BASE. Reachability becomes a refusal-side check, never the trigger.

**Left-shift gate.** Add a check-12 arm asserting Step 5b's text still names the owner-invocation
precondition (a positive `grep -F` on the phrase, armed by a negative fixture that strips it), so a
future widening reds the bar instead of shipping. Longer term: the reason check 12 could not see this
is that it greps for *structure* (a heading, a string, a count) and never for the *predicate*. Any
check whose subject is a rule should assert the rule's operative clause, not its presence.

---

## HIGH

### F2 — `--phase` reaches the terminal phases directly, so the entire DoD gate is optional

`tools/unattended/unattended.sh:502`

`verb_phase` validates only: slug, run-state file exists, membership in `$(phases)`, and witness
presence. `PHASES_CORE` (line 69) includes `LANDED ABORTED`, so both terminal phases pass vocabulary
membership. `verb_close` (627-671) writes only `LANDING` (line 669) — **`LANDED` is reachable ONLY
through `--phase`, and from ANY phase, with no requirement that `--close` ever ran.**

Reproduced in a fixture repo: `--close tRun` blocks (`check 13 FAILED … keepalive-reaped /
parked-decisions-surfaced`, rc=1), then `--phase tRun LANDED --witness $(git rev-parse HEAD)`
succeeds (rc=0) and the record reads `phase: LANDED`. A run goes `RUNNING → LANDED` in one command,
skipping `gates-green`, `records-current`, `landed-via-lander` and the explicitly non-overridable
`authorization-reachable` — the item `verb_close` refuses to let `--override` touch at line 644.

Nothing notices afterwards: `check_single_live` and leg check 7 both skip terminal phases; check 9,
the region copy, BASE and bypass-grep are all satisfied by a run that never closed.

Four of the six DoD items are redundantly covered elsewhere (gates-green by the pre-push bar,
records-current by leg check 8, landed-via-lander by check 11, authorization by check 13). But
**`keepalive-reaped` and `parked-decisions-surfaced` (`dod_met`, 692-695) are enforced NOWHERE except
`--close`** — and `parked-decisions-surfaced` is the mechanism the protocol calls *"where the owner
gets the turn you did not take."* So an unattended run can reach a terminal phase with the keepalive
orphaned and every parked decision unsurfaced, silently. The verb whose whole purpose is to replace
the owner turn with a machine-checkable checkpoint is bypassed by the sibling verb added in the same
commit.

**Fix.** A precondition, not a blanket rejection — `--phase` is the sole producer of `LANDED`:

```sh
case " $PHASES_TERMINAL " in *" $want "*)
  fail … "a terminal phase is reached by --close, which evaluates the DoD set; --phase moves a run between non-terminal positions: $want"
  return 1 ;;
esac
```

…and have `verb_close` write the terminal phase itself, or expose an internal flag `--phase` cannot
supply. Also refuse moving a run that is already terminal.

**Left-shift gate.** Add a leg check asserting that every DoD item has at least one enforcement site
**other than** `--close`, or that no path reaches a terminal phase without a recorded close. Concretely:
an arm in `check-unattended.sh` that fails a run-state file reading `phase: LANDED` with no
`closed-at`/`close-witness` fact. The generalisable rule: when a verb is the sole gate for an
obligation, the bar must assert that the obligation's *outcome* is present, not that the verb exists.

---

### F3 — leg check 9 still refuses `base == HEAD` unconditionally, which is exactly what `--preflight` now records

`tools/unattended/check-unattended.sh:200` *(found independently by three lenses)*

S3 relaxed the degenerate-base refusal **in the driver only**. `unattended.sh:537` passes
`trusted_base "$rel" allow-degenerate` — and only `--preflight` does — on the stated ground that
`base == HEAD` is *"the normal state of a run that has correctly built nothing yet, which is every run
at preflight"* (comment at 530-536). The merge-bar leg was not revisited: check 9's HEAD-equality arm
is unconditional, and its arm at `check-unattended.test.sh:317` **pins that unconditional behaviour**.

Reproduced end-to-end in a scratch clone from the shipped kit. On a fresh branch off `main` with
nothing committed:

- `unattended.sh --preflight tRun --keepalive-id k1` → rc=0, `preflight OK — base <sha>` with
  `base == HEAD`, and it **stages** `memory/builds/tRun/RUN.md` (see F7), so `git ls-files` makes the
  run visible to the leg immediately
- `bash tools/unattended/check-unattended.sh` on that same tree → rc=1,
  `UNATTENDED check 9 FAILED — the merge-base equals HEAD, so the run authored every byte a mandate
  comparison would read`

`git show 6d7cdd7 -- tools/unattended/check-unattended.sh` confirms the same commit that relaxed the
driver rewrote check 13 and left check 9 untouched. Both verdicts are enshrined in green tests landing
in this diff: `unattended.test.sh:347-352` asserts preflight **accepts** the state;
`check-unattended.test.sh:315-317` asserts the leg **refuses** it. The repo's own
two-answers-to-one-question class, inside one kit, in one commit.

The leg is an unguarded entry in `tools/gate-legs.json` and `GATE_CMD` in `.unattended.conf` is
`bash tools/run-gates.sh`, so the full bar is red for the entire window between preflight and the
run's first commit — the window S3 was written to legalise. An unattended run that gates itself at DoR
gets an unexplainable refusal on its first act, with no owner turn to interpret it: the
stall-or-learn-to-bypass failure protocol §6 names.

**Honest scoping** (why high and not blocker): the window is bounded — it clears the moment the run
commits (`mb != HEAD` → leg exit 0), and by push time a run necessarily has commits. Check 9's body is
also skipped entirely when no default branch resolves; this repo has
`refs/remotes/origin/HEAD -> origin/main`, so it fires here. `check-unattended` is not in the
pre-commit fast leg, so the red surfaces only if the full bar runs inside that window.

**Fix.** Make check 9 verb-aware the way `trusted_base` is: skip (or downgrade to a note) the
`mb == HEAD` refusal when the run-state file's phase is `PREFLIGHT`/`RUNNING` **and** its `witness`
equals HEAD — i.e. the run has committed nothing on top of the anchor — and keep it a hard refusal for
every later phase. Better: re-state the relaxation as a property of the *state* rather than of the
*caller*, so both files derive it from one place. Also fix the message, which still says "mandate
comparison" after the rename to authorization.

**Left-shift gate.** Add a **cross-component** arm to `check-unattended.test.sh` that runs the real
driver's `--preflight` on a degenerate base and then runs the leg on the resulting tree, asserting the
leg stays silent. No arm today crosses the two halves of the kit — every arm builds its own fixture
tree by hand, which is precisely why a driver relaxation could ship without the leg noticing. Make
"driver-produced state must pass the leg" a standing property, not a per-defect arm.

---

### F4 — the arm that was supposed to arm S6's phase-preservation guard passes vacuously

`tools/unattended/unattended.test.sh:450` *(found independently by three lenses)*

The arm `"a re-run preflight leaves a reached phase alone"` never reaches the guard it exists to arm.
Instrumented: at line 449, `git status --porcelain` reads ` M memory/builds/tRun/RUN.md` — the
preceding `--phase` left RUN.md modified — and the second `--preflight`'s entire output is
`UNATTENDED check 2 FAILED — the working tree is dirty … unattended: --preflight refused; the
run-state file is unchanged`. `check_clean` (line 523) fires before any write, so the verb writes
nothing, and the `same` at 450 compares `BUILDING` against a file preflight never touched.

**Mutation-confirmed.** Reverting `unattended.sh:573` from
`[ -n "$(fact "$rel" phase)" ] || set_fact "$rel" phase RUNNING` to the unconditional
`set_fact "$rel" phase RUNNING` leaves the suite at `PASS (92 assertions)` — byte-identical to the
unmutated run. The S6 regression that both the commit message and the source comment at 570-572 call
out — *"a resumed run that had reached BUILDING was silently moved back to RUNNING by the verb it is
told to re-run after a compaction"* — has **no arm that can fail.**

`unattended.test.sh` is bar leg *"unattended driver selftest"*, so the bar certifies coverage that
does not exist. This is this repo's own vacuous-arm class, which `check-arms.py` and the AGENTS.md
harness meta-gate exist to catch.

**Correction to one lens's headline, recorded:** the guard is *not* unreachable in production. Preflight
stages RUN.md deliberately (line 424) so the run's next commit carries it, and the realistic path —
commit RUN.md, `--phase BUILDING`, commit, clean tree, re-run preflight — reaches the guard and
correctly preserves `BUILDING`. The defect is **test coverage**, plus the dirty-tree-after-preflight
consequence in F7. Not dead code.

**Fix.** Commit the run-state file between the two preflights
(`git add -A && git commit -q -m runstate --no-verify`) so the second one reaches its write phase —
verified by hand that the guard then genuinely holds `BUILDING` and the mutant fails. Add
`hit "$out" "preflight OK"` on the second call so the arm fails loudly if preflight refuses for any
reason, instead of passing by refusing.

**Left-shift gate.** `check-arms.py` keys on the call site and asserts each `fail` branch is armed by
a positive assertion naming its own failure text. It cannot see this, because the defect is a
*success* path that was never reached. Extend the meta-gate's remit: any test arm whose subject verb
can refuse must assert the verb **succeeded** before asserting what it wrote. Mechanically — flag any
`same`/`hit` on post-state that is not preceded by a success assertion on the command that produced
it, in the same arm.

---

### F5 — `--phase` and `--plan` appear nowhere in the Skill the agent actually reads

`.claude/skills/unattended/SKILL.md:42` and `tools/unattended/SKILL.template.md:42`
*(found independently by two lenses)*

`grep -n -- '--phase\|--plan'` over both files returns **nothing**. The rendered Skill names only
`--preflight`, `--status`, `--resume` and `--close`. Line 42 says *"Keep the phase honest, and give
every phase claim a WITNESS"* — an obligation with no named mechanism.

The consumer-facing surfaces are worse than that. `unattended.sh`'s usage header (lines 5-8) and the
`usage:` line at the bottom of dispatch both enumerate only the same four verbs, so an agent that runs
the driver bare is told the same four. Repo-wide, `--phase` appears only in `PROTOCOL.template.md:183/186`,
`memory/guides/UNATTENDED-PROTOCOL.md`, the driver dispatch, the driver's own unknown-argument string,
and this build's spec/README — **not in any operating instruction a run is told to invoke.**

So the four new CORE members that raised `CORE_FLOOR` from `6:6` to `10:6` — `SPECCING`, `REVIEWING`,
`FOLDING`, `BUILDING` — stay decorative in practice, and the agent is left doing exactly what the S6
comment at `unattended.sh:429-433` calls the defect: *"hand-editing an artifact this kit calls
generated."* The Skill's step list otherwise enumerates the whole lifecycle (preflight, status, resume,
close, override, land, reap), so the omission reads as completeness.

Two mitigations, recorded: the Skill does point at the protocol as binding, and protocol §7 documents
both verbs — so the phases are reachable via the binding contract, just not via the operating summary
the agent loads. And `scaffold_runmd`'s "never hand-edit it" scopes to the *generated region*, not the
Run-facts block that holds the phase.

`adopt-unattended.sh --check` only renders the template and diffs it against the render, so no leg can
notice a verb that is in neither.

**Fix.** Add both verbs to `tools/unattended/SKILL.template.md` under "While it runs":
`bash {{KIT_DIR}}/unattended.sh --phase <slug> <PHASE> --witness <sha>` and
`bash {{KIT_DIR}}/unattended.sh --plan <slug>`; cite the phase vocabulary by pointing at protocol §3
rather than restating it. Re-render via `bash tools/unattended/adopt-unattended.sh` so the wiring leg
stays green. Extend the driver's usage header and `usage:` line to the same six verbs (see F11).

**Left-shift gate.** Add a **verb-parity** check to `check-unattended.sh`: extract the verb set from
the driver's dispatch `case` and assert every verb appears in the rendered Skill *and* in the protocol.
That is a five-line `grep`-and-compare and it closes the whole class — today `adopt-unattended.sh
--check` asserts template↔render parity but nothing asserts render↔implementation parity, which is the
axis that actually strands the agent.

---

## MEDIUM

### F6 — `plan_state` diverges from the M2 rule it claims to compute, in the unsafe direction

`tools/unattended/unattended.sh:466`

`memory/guides/BUILD-METHOD.md:37-38` defines *"FORKED — §8 Open questions carries an unresolved item"*
and *"READY — none of the above, AND §10 Reuse audit is filled where the format requires it."*

The awk assigns `forkline` **once** (line 460, `if (cur == "forks" && forkline == "") forkline = line`)
and then tests only that first non-empty line for `RESOLVED`/`none`/`n/a`. §10 is not in the section
map at all — only `## 2.`, `## 6.`, `## 7.`, `## 8.` are mapped.

Reproduced: a spec whose §8 reads `**F1 which colour?** RESOLVED (owner) — blue.` then
`**F2 which database?** OPEN. Nobody has decided.` prints **READY**. M2 rule 3 is *any* unresolved
item, and M3's instruction is to *"Mark it in place"* per-fork — exactly the shape that misclassifies.
M2's Act clause routes FORKED → M3, and its hard floor is *"Never build a MISSING or THIN unit"*, so a
false READY is the driver telling an unattended run to build a unit with open forks — the one direction
that cannot be recovered from without an owner turn.

Unarmed: `unattended.test.sh:490-517` only exercises single-line §8 fixtures (`none`, `F1 which way?`),
so no arm can fail on a multi-item §8.

**Correction, recorded — the §10 half is weaker than first stated.** `bash tools/unattended/unattended.sh
--plan aGuardedTally` prints `TOOL-aGuardedTally-1 INPROGRESS READY` for a spec with no §10 section at
all, and 19 tracked specs have an empty or absent §10 — but §10 is date-gated to
`SPEC10_CUTOFF=2026-08-04` (`memory/TEMPLATE-SPEC.md:14`, `check-memory-hygiene.sh:494`) and all 19 are
pre-cutoff or non-conforming, so the measured READY is not itself a §10 violation. The structural gap
is still real: the hygiene canon check asserts only that the §10 **heading** exists, never that its body
is filled, so a post-cutoff spec with an empty §10 still prints READY. **Confirmed on the FORKED axis;
the §10 impact is overstated.**

**Fix.** Scan the whole §8 body: keep an `unresolved` flag set for any non-empty line that is not a
`none`/`n/a` preamble and does not carry `RESOLVED`, and decide FORKED on that. Add `## 10\.` to the
section map and require `seen["reuse"]` non-empty before printing READY. If §10 completeness is judged
too soft to mechanise, say so in the output line rather than silently promoting to READY.

**Left-shift gate.** Add multi-item §8 fixtures to `unattended.test.sh` — resolved-then-open,
open-then-resolved, and all-resolved — so the first-line-only shape has an arm. Generally: any awk that
reduces a *section* to a *line* should carry a fixture whose section has more than one line; that is a
cheap, checkable rule for the harness meta-gate.

---

### F7 — `scaffold_runmd` stages the blank scaffold, then `verb_preflight` invalidates it

`tools/unattended/unattended.sh:424`

`GIT add -- "$rel"` runs on the freshly written **blank** scaffold at line 424, and it is the only
`GIT add` in the file. `verb_preflight` then splices the generated region (559-564) and writes seven
facts via `set_fact` (565-574) directly into the worktree copy, **with no re-add**.

Reproduced end to end: after a successful `--preflight`, `git status --porcelain` reads
`AM memory/builds/tRun/RUN.md`, and `git show :memory/builds/tRun/RUN.md` contains an **empty**
`<!-- run:generated -->` region and no `base:`, `phase:`, `witness:` or `keepalive:` lines — while the
worktree copy has all of them.

Every leg check reads the worktree (`check-unattended.sh:129-130`, `sed -n … "$f"`) while its
*population* comes from `git ls-files`, so the bar is green over a staged blob that is not what it
graded. A plain `git commit -m …` that does not re-add the path lands a run-state record with no BASE,
no phase and no witness. That is precisely the record-vs-reality class the kit exists to close — and
the function's own comment justifies the staging as *"what makes the run visible to every leg check."*
What it makes visible is a blank file.

The self-test's only staging arm (`unattended.test.sh:236`) asserts the **path** appears in
`git ls-files` and never its content.

**Fix.** Move `GIT add -- "$rel"` out of `scaffold_runmd` and into `verb_preflight` after the last
`set_fact` (line 574), so the staged bytes are the bytes the verb just reported. Do the same at the end
of `verb_phase`. One line, and it also removes the dirty-tree consequence behind F4.

**Left-shift gate.** Assert in `unattended.test.sh` that `git show :<rel>` **equals** the worktree file
after every writing verb, not merely that `git ls-files` returns the path. Broader: the leg's population
comes from the index and its assertions come from the worktree — any check with that split should have
one arm proving the two agree, or it is grading a different file than the one that lands.

---

### F8 — `verb_plan` fabricates units from any `.md` under `spec/`

`tools/unattended/unattended.sh:475` and `:481` *(found independently by two lenses)*

`verb_plan` globs `git ls-files "$dir/spec/*.md"` with **no conformance test**, then derives the unit id
from the first word of any `# ` heading:
`sed -n 's/^# \([A-Za-z0-9][A-Za-z0-9-]*\) .*/\1/p'` — which matches any H1 with two or more words.

Measured on this repo's own corpus — **5 of 25 builds report an invented unit and name it as the next
thing to build**:

| build | fabricated id | printed |
|---|---|---|
| `aDeployScout` | `The` | `The ? THIN` → `next: The (THIN)` |
| `aKitHardener` | `govkit` | `govkit ? THIN` |
| `aLeanRework` | `Template` | `Template ? THIN` |
| `aPortableWarden` | `worktree-guards` | `worktree-guards ? THIN` |
| `aRatchetForge` | `Manifest` | `Manifest ? THIN` |

Each is a research report or a legacy non-conforming doc. `BUILD-METHOD.md` M2 defines the fallback
roster as the *conforming* specs under `spec/` (*"A unit's spec is the file under spec/ whose status
header carries the id"*), and M2's hard floor is *"Never build a MISSING or THIN unit"* — so an
unattended run following `--plan` is directed to thicken a research report as if it were a spec.

Two sub-claims, both verified: the documented `basename` fallback at line 483 is **unreachable across
the entire corpus** — I extracted the id for every tracked `memory/builds/*/spec/*.md` and not one file
failed the regex (it is live only for a one-word or absent H1). And no fixture covers the shape:
`mkspec` (`unattended.test.sh:460`) always emits a conforming spec with a `**Status:**` header, so
extraction failure is outside the test population entirely.

Mitigation worth naming: the status column prints `?` for these, which does signal non-conformance — but
the `next:` line, the actionable output, carries the bogus id with no such marker.

**Fix.** Refuse to classify a file that does not parse as a conforming spec — require both a
`**Status:**` header and an id matching the `FAMILY-slug-N` grammar
(`^# ([A-Z]+-[A-Za-z0-9]+-[0-9]+)[ —-]`) — and report the rest on their own line
(*"N tracked file(s) under spec/ are not conforming specs and are excluded"*) rather than as units.
That is also the honest input to the MISSING state the verb says it cannot report.

**Left-shift gate.** Add a test arm writing a non-spec `.md` into `spec/` and assert it is named as
excluded and never appears as `next:`. Standing rule for this kit's fixtures: every roster-building verb
needs at least one **non-conforming** input in its population, because a fixture generator that only
emits valid inputs cannot find an over-collection.

---

### F9 — the check-13 green control runs no machinery

`tools/unattended/check-unattended.test.sh:370`

`anchor_break noop_break` is the control that is supposed to prove the three check-13 arms fire on a
*specific* break rather than on any anchor edit. Instrumenting `anchor_break`'s
`git add -A && git commit -q -m anchor-break --no-verify && git push -q -f origin main` with an
`|| echo` marker: it fires **exactly once, on the noop arm**, and the suite still prints
`PASS (57 assertions)` plus the leaked `On branch main / nothing to commit, working tree clean`.
`git commit` fails with "nothing to commit", the `&&` chain short-circuits, and no commit and no push
happen. State dump at the control: `HEAD == PRISTINE` and `origin/main == ANCHOR0`.

The control's own comment says it proves *"the same machinery with NOTHING broken must stay silent, or
these arms are indistinguishable from a leg that reds on any anchor edit at all"* — but with no anchor
commit and no push it degenerates to running the leg on the pristine tree, which lines 101-103 already
assert. **A leg that redded on every benign anchor advance would still pass this control.**

Minor imprecision in the original finding, recorded: the `git merge main` on the next line *does* run,
but resolves to a no-op since main is already an ancestor. Substance unchanged.

**Fix.** Give `noop_break` a real but harmless anchor edit — e.g.
`printf 'x\n' >> memory/builds/tRun/README.md` below the front matter and outside the
`gen:build-index` region — so the commit/push/merge/re-record path actually executes. Replace the `&&`
chaining in `anchor_break` with an explicit `|| { echo FAIL anchor_break machinery; st=1; }` so a dead
chain can never be silent again.

**Left-shift gate.** Ban silent `&&` chaining in test helpers whose steps *set up* the subject:
a helper that builds state must fail loudly when a step fails, or every arm downstream of it is
vacuous. This is mechanically checkable — flag `git commit`/`git push`/`git merge` inside a `&&` chain
in any `*.test.sh` with no `||` failure branch — and it belongs in `check-arms.py`, which already owns
the vacuous-arm class.

---

## LOW

### F10 — check 13's front-matter branch falls through and emits a second, false failure

`tools/unattended/check-unattended.sh:227`

There is no `continue` or guard after the front-matter `fail 13` (lines 223-231), so control falls into
the `dslug` awk, whose `NR == 1 { next }` presumes line 1 is `---`. Reproduced by instrumenting the
test's `anchor_break break_fm` arm: it prints **both**
`check 13 FAILED — … is not a build README` **and**
`check 13 FAILED — a build README at its run's recorded BASE declares a different slug …: declared ,
folder tRun`.

The second message asserts a rename or a copy that did not happen, and it contradicts the driver, whose
`check_authorization` returns 1 at the same branch (`unattended.sh:390-391`) — so the bar's "second
opinion" leg diverges in *behaviour* from the implementation it is meant to independently confirm.

**Fix.** Replace the `*) fail 13 …;;` arm with one that also skips the slug comparison — set a flag and
guard the `dslug` block, or hoist the per-file body into a function so the branch can `return`, matching
`check_authorization`'s early return.

**Left-shift gate.** Where the leg is documented as a "second opinion" on a driver function, arm the
pair: for each refusal shape, assert the driver and the leg produce the *same number* of failures on the
same fixture. Divergence in count is the cheapest detector of a missing early-exit.

---

### F11 — the driver states its own verb set two ways, and the operator-facing one is the stale one

`tools/unattended/unattended.sh:722` (and the header comment at lines 5-8)

`bash tools/unattended/unattended.sh` with no verb prints a four-verb usage string
(`preflight | status | resume | close`) and exits 2. `--bogus` prints *"the verbs are --preflight,
--plan, --phase, --status, --resume and --close"* (line 719) and exits 1. The header docstring carries
the same stale four.

So the one output an operator sees when they do not know the interface is the one that hides the two
verbs this diff added — the same omission as F5, in the other consumer surface. The six-verb refusal
text is pinned verbatim by `unattended.test.sh:526`; nothing pins the usage line.

**Fix.** Extend the usage string and the header comment block to the same six verbs the refusal names:
`--plan <slug>` and `--phase <slug> <PHASE> --witness <id>`.

**Left-shift gate.** Add a source-level arm asserting the usage string and the fail-14 message list the
same verb set — a one-line `diff <(verbs_from_usage) <(verbs_from_refusal)`. Fold this into the same
verb-parity check proposed under F5 so there is one place that knows the verb set: dispatch, usage,
refusal, Skill, protocol.

---

## What the confirmed set says about the diff

Eleven distinct defects over 636 added lines. The distribution is the finding:

- **Nothing in this diff crosses component boundaries.** F3 and F5 and F11 are all one shape — a change
  landed in one half of a pair and the other half was not re-derived. The kit has driver arms and leg
  arms and Skill-parity arms, and **zero** arms that run the driver and then the leg. That single missing
  fixture would have caught F3 and F7 outright.
- **Two of the four highs are test defects, not code defects** (F4, and F9 at medium). Both are this
  repo's own named vacuous-arm class, and both are inside the very kit that exists to make unattended
  runs machine-checkable. `check-arms.py` cannot see either, because it keys on `fail` branches and both
  defects are unreached *success* paths. That is a concrete, scoped extension to the meta-gate.
- **The blocker is a downstream consumer, not the kit.** S1's authorization redefinition was reasoned
  about carefully inside `tools/unattended/` and applied literally in `skills/session-kickoff/`, where
  the same predicate means something entirely different. Nothing in the bar looks across that boundary;
  check 12 greps for a heading and a string.

The recommended order is F1 first — it is the only finding that changes what happens to a user who has
not opted into anything — then F2, then the F3/F7 pair together since one fix touches both, then F4/F9
as one test-hardening pass, then F5/F11 as one verb-parity pass.
