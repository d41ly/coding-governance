# Design pass 1 — the enforcement layer, mis-aimed and kept

**Serves:** none — a design pass the build README grades REJECTED for scope; it warranted no spec and none was minted

**What this pass was aimed at:** proving that an unattended run did not tamper with its own
instructions. It produced a provenance-and-evidence system.

**What had been asked for:** the build method — how to spec, how to review, how to build.

Those are different questions. This pass answered the first and the deliverable was labelled as an
answer to the second. The record is kept because the method was sound, three findings are
independently real, and the failure mode is worth having on paper: a well-run pass converges hard on
whatever its briefing names as the central tension, so a mis-aimed briefing produces a confident
wrong answer rather than a visibly confused one.

## 1. How the target was set wrong

The briefing was written by the session, not by the owner. It named as "the central design tension to
resolve, not dodge" this proposition:

> A run that writes its own SPEC is the instruction-layer analogue of a run that writes its own
> MANDATE. The kit already refuses the latter absolutely.

It then scored candidate designs on `checkability` and `self_authorization_safety`, among other axes.

The proposition is defensible on its own terms and it is not what the owner asked about. Every one of
the three candidate designs and both judges optimized it faithfully, which is the point: the pass did
not drift. It went exactly where it was aimed.

The tell was in the output and was missed until the owner named it. The pass mapped the owner's
sixteen rules to enforcement labels and reported the split as its headline accounting:

| Label | Count |
|---|---|
| machine-checked | 6 |
| witnessed | 6 |
| agent-attested | 3 |
| unenforceable | 3 |

That is a grading rubric. A procedure had been asked for.

## 2. The pass itself

Five phases, fourteen agents, 2.11M tokens, 47 minutes, zero agent errors. Fan-out routed through the
bounded helper after `tools/hooks/agent-cap.js` blocked the first launch for raw `parallel()` — the
repo's own cap working as designed on the session that wrote it.

| Phase | Agents | Shape |
|---|---|---|
| Ground | 4 | driver mechanics, gate leg, reuse seams, record structures |
| Design | 3 | declaration-first, phase-machine, rendered-brief |
| Judge | 2 | a mechanist scoring falsifiability, an operator scoring survivability |
| Synthesize | 1 | winner plus grafts |
| Verify | 4 | self-authorization, vacuity, operational, adoption |

The judges split. The mechanist picked declaration-first on enforcement strength, the operator picked
rendered-brief on architecture. The synthesis took rendered-brief's architecture with
declaration-first's enforcement, and rejected phase-machine's ordering ladder on the grounds that
every commit a run makes is an ancestor of its own HEAD, so a run may write all the code first and
then climb the ladder in order with valid witnesses at every rung.

## 3. What it designed

Two artifacts under a build's own `build/` folder, chosen because that path is outside the hygiene
index caps:

- **A pinned brief**, written once at preflight and immutable after, carrying the rules, a
  regrounding procedure, every unit's governing spec, and a provenance ledger holding each governing
  artifact's blob at BASE and at pin time.
- **A discharge ledger**, appended one line per obligation, each naming a tracked evidence artifact
  interrogated by five questions.

Around them: ten new `.unattended.conf` declarations, three new mandate clauses granting
spec-authoring and declaration-repinning budgets, nine new gate checks, six new DoD obligations under
a `witnessed` label, and terminal-phase flags on `--close`.

Its one genuinely useful structural idea was the spec gradient, which survives into pass 2 as a
procedure rather than as an authorization gate:

| State | Test | Rule |
|---|---|---|
| INHERITED | the spec exists at BASE | the owner's text as it stands |
| UNDERSPECCED | the unit is declared at BASE, the spec text is absent or thin | the run may write it, within a budget |
| MISSING | the unit is not declared at BASE | refused |

## 4. What the adversarial stage found

Three of four lenses returned BROKEN across 52 defects, of which 15 were blockers. The blockers were
not incidental. The largest invalidated the design's own foundation, and most of the rest were
defects in machinery that should not exist at all.

| Blocker class | Substance |
|---|---|
| foundation | the pinned BASE is chosen by the run, so every provenance claim reduces to a forgeable value |
| terminal phases | `--close --landed` cannot succeed from either branch; `--aborted` inherits the DoD loop, so ABORTED is unreachable exactly when a run cannot meet its DoD |
| override arity | `verb_close` takes one override scalar, so any two unmet items make a run permanently unclosable regardless of the designed budget |
| reset primitive | `--preflight` has no phase guard and is re-runnable mid-run |
| unfloored obligations | the six new obligations sat in `DOD_EXTRA`, which has no floor, repeating the `CORE_FLOOR` lesson one level out |
| unenforced declarations | the four keys the design called mandatory had no enforcement, because `render()` substitutes an empty value silently |

## 5. The three findings that survive

Verified against source in this worktree, not inherited from the pass.

**The pinned BASE is forgeable.** `default_branch()` in `tools/unattended/unattended.sh` returns
`$GOV_DEFAULT_BRANCH` verbatim when set. `resolve_base` then merge-bases HEAD against
`refs/remotes/origin/$d`. A remote-tracking ref is writable locally:

```bash
git update-ref refs/remotes/origin/zzz <run-authored-commit>
```

Reproduced end to end in a scratch repo. The command exits 0 with no push and no network, BASE
resolves to a commit the run authored, and it stays unequal to HEAD so the degenerate guard does not
fire. `check_mandate` then compares run-authored bytes against run-authored bytes and prints OK. The
driver's own comment block asserts the defense that fails here, claiming a remote-tracking ref cannot
be moved without a push. This was already filed as D3/BLOCKER in
`../../aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md` with fixes specified, and no
backlog row tracked it. It is now `TOOL-aWrittenMethod-2` and is out of this build's scope.

**Four declarations are delivery rather than enforcement** and carry forward: the recall entrypoint,
the reuse entrypoint, the review harness, and the keepalive interval. The last one closes a real gap.
`CronCreate` takes a five-field cron expression and a prompt, and `.unattended.conf` declares
neither, so the owner's cadence and CONTINUE payload live only in chat prose. Three properties of the
real scheduler bear on any design: jobs fire only while the session is idle rather than mid-turn, the
store is in-memory and session-scoped which independently confirms the kit's split-by-actor
reasoning, and recurring jobs auto-expire after seven days.

**Measured corpus facts.** `## Verdict` appears in 8 of this repo's 32 review records and no verdict
field exists anywhere, so no content anchor for "this spec was reviewed" can be keyed on it without
reddening most of honest history. The build README `ids:` key is written as ranges and unions across
all 25 builds, so it is not a machine-readable unit roster. The unattended gate leg self-describes as
thirteen checks where `AGENTS.md` says eleven.

## 6. Disposition

Superseded by pass 2. The full 60 KB design document and its 52-defect table were session artifacts
and are not retained: their substance is above, and preserving a rejected enforcement design in the
tree would add a carrier for rules the tree does not hold.

The scope error is recorded as a gotcha candidate rather than a decision, because the lesson is about
how a pass is briefed and not about this kit: a multi-agent pass inherits its briefing's framing
completely, so the briefing's statement of the central tension is the highest-leverage line in it and
deserves the same scrutiny as a spec's §1.
