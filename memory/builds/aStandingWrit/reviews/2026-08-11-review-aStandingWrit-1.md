# review-aStandingWrit-1 — Tier-2 over the rev-1 spec

**Serves:** spec-audit TOOL-aStandingWrit-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

**Verdict: do not build.** Five lenses, five cold-start agents, at the review protocol's cap of five
total. Every lens returned findings; none was dead. The most severe finding is not about this spec.

## The finding that outranks the spec

**The shipped unattended kit's authorization can be bypassed with one offline command, today, on
`main`.** It was reproduced end-to-end to a landed push, with a live control.

`resolve_base()` anchors the pinned BASE on `refs/remotes/origin/<default>`, on the stated ground
that "Moving it requires a push, which is the act being authorized" — `tools/unattended/unattended.sh:119-120`.
That is false. `git update-ref refs/remotes/origin/main <sha>` succeeds locally, offline, leaves the
real remote untouched, and is not a push.

Reproduced sequence, in a scratch repo with a bare `origin` whose `main` contained no mandate and no
build folder:

1. the run branches, authors its own mandate block in a run-state file, commits it as `C1`
2. one empty commit, so the merge-base is not HEAD
3. `git update-ref refs/remotes/origin/main $C1`
4. `--preflight` prints `preflight OK` and accepts text the run wrote
5. `check-unattended.sh` — the independent second opinion — exits 0 and silent
6. `--close` reports the machine-checked `mandate-reachable` item MET
7. the advisory lander marker is an ordinary file, so `git push origin HEAD:main` runs the bar green
   and the run-authored mandate lands on the remote default branch

Control with an honest anchor: `check 6 FAILED — no run-state file at the pinned BASE`.

A second variant needs no ref forgery: `GOV_DEFAULT_BRANCH` is read by both the driver
(`unattended.sh:107`) and the leg (`check-unattended.sh:177`), so a manufactured tracking ref plus
the env var makes both compute the same wrong value. That ref survives an ordinary single-branch
fetch.

This is prior blocker (b) from the second Tier-2 on the previous build. `git branch -f` was closed;
`git update-ref` was not, and the comment asserting otherwise is still in the source. It is recorded
as its own backlog row because it is a defect in landed code, independent of whether this spec is
ever built.

## Blockers against the spec

**B1 — S3 widens the live bypass.** S3 makes the merge-base-equals-HEAD refusal legal at
`--preflight`. That refusal is worded as the exact property being protected. With the anchor
forgeable, S3 reduces the attack from two commits to one: the run creates its build folder, commits,
forges the ref, and preflight pins BASE to the run's own commit. Reproduced with the S3 relaxation
patched in: `base == witness == HEAD == the run's own commit`. The lens also confirmed the honest
half — with a genuine anchor, S3's reasoning is sound and today's refusal really does block every
normal run. S3 is correct and must not land before the anchor is closed.

**B2 — S3 leaves BASE undefined for the state it legalises.** `resolve_base` returns 2 before it
prints, so rc 2 carries no value. `check_mandate` documents that it deliberately has no empty-BASE
guard *because* `trusted_base` refuses first — the invariant S3 deletes. The literal implementation
restores the `git show ":<path>"` index read that was blocker (a). Exploitation on a clean tree is
HYPOTHESIS; restoration of the shape is confirmed.

**B3 — `--plan`'s sequence-number join is wrong on 7 of 7 multi-unit builds, and right on none.**
The spec's sequence number is a per-build record counter; a review's is "which review is this". They
coincide only at one unit and one review. Measured: `aFoldedQuarry` 6 of 7 attachments wrong;
`aMendedLedger` 4 false positives and 4 false negatives out of 8, with the review named for U9
credited to U3; `aPrunedCeremony`'s key is not even unique across families; `aSealedCaravan` — the
live build — reports a unit reviewed yesterday as `REVIEW NEEDED`. The two counters are not the same
quantity and no build in this corpus has ever treated them as one, so this is not repairable by
fixing the join.

**B4 — S4's reuse mechanism is banned by a shipped, armed assertion the spec did not read.**
`tools/unattended/unattended.test.sh:384-388` refuses any python launcher in the driver. The driver
is bash; `gen_build_index.py` exposes no machine-readable mode. §10's claim that `--plan` "calls
those rather than re-parsing" is aspirational — there is no seam.

**B5 — `memory/TEMPLATE-README.md` reds hygiene check 3.** The memory-root allowlist is closed and
hardcoded at `tools/memory-tree/check-memory-hygiene.sh:211`. Admitting the file edits that engine,
which trips the verdict-epoch gate, the kit-version pair, the kit/dogfood parity leg and the
hygiene-parity floor. None of the four is in the spec's file list, and §7 claims no leg moves.

**B6 — the `mandate-reachable` DoD item is orphaned.** It lives in protocol §4, which S7 does not
amend. Deleting it shrinks a floor the protocol forbids shrinking. Renaming it makes `dod_met` fall
through to a default arm satisfied by a line the run writes into its own file, and makes the
non-overridable guard at `unattended.sh:391-395` stop matching. Two of the three unstated answers
reinstate self-authorization.

**B7 — the plan-title match is unsatisfiable, and assertion 4 turns it into a livelock.** The owner
authors the planned title before the spec exists; the agent authors the spec's title. Measured
against the prior build: zero of seven match. A run then sees `SPEC NEEDED` forever, and assertion 4
forbids the obvious repair — editing the plan region reds preflight as "the run rewrote its own
scope". The run cannot converge and cannot fix it.

## Highs

**H1 — the class grant is self-propagating, and §4 does not name it.** A legitimately authorized run
whose diff creates a new build README authorizes the *next* run by bytes a run wrote and landed.
Under the mandate this required authoring a file whose only purpose was authorization — conspicuous.
Under README-existence it is indistinguishable from ordinary work.

**H2 — the grant no longer names the actions, and is irrevocable.** Both charter statements hinge on
"naming the build and both actions". A README names no action, so merge-only is unexpressible. A
mandate could be withdrawn by deleting it; a build README cannot be deleted, so after this lands
there is no act meaning "not this build", and every build ever created stays eligible.

**H3 — assertion 4 is vacuous for all 26 builds that exist.** No build README carries a plan region.
Under the class grant the run picks the slug, so it picks a region-less build and the conditional
skips. F1's mitigation is day-N over a class whose day-1 membership is permanently region-less.

**H4 — F1 and §5 contradict each other.** §5 makes an empty plan region a refusal; F1 recommends the
template ship the region. A scaffolded build then carries an empty region and preflight refuses
until the owner hand-fills it — the per-build authoring F0a removed, reintroduced by S5.

**H5 — the ARMS floor is a per-gate NET count, so this build's additions mask its deletions.** S1
deletes six named guards and adds four; if the net lands at or above 31, `check-arms.py` is silent.
The per-gate design prevents cross-gate masking and cannot prevent within-gate masking, which is
exactly this build's shape.

**H6 — AC6 states the gate's comparison backwards.** `check-unattended.sh:85-88` fires when the
driver's core set shrinks below the declared floor, never when the declared floor sits below the
driver. With core at nine and a stale `6:6`, every leg is green and the three new members are freely
deletable forever. AC6 is unimplementable as written.

**H7 — S6's arithmetic forces `RUNNING` to survive with no assigned meaning**, and the three new
phases have no producer: only `--preflight` and `--close` write a phase, and `--preflight`
unconditionally rewrites it to `RUNNING`, clobbering a resumed run's position.

**H8 — the cut-line is not real, and it is wrong for Tier-1.** The four-state table defines what
"built" means, mandates a review record for every unit, and fixes the order — three questions §3
assigns to the parallel session. Tier-1 units produce no review record, so they read `REVIEW NEEDED`
forever.

**H9 — the four-state machine cannot express `INPROGRESS`**, which this tree uses for
built-but-not-landed. Eight specs sit there today; five would be told to build what is already
built. `BLOCKED` and `DEFERRED` become `next:` targets. Five specs have no parseable status header
and are invisible, so `--plan` would report `SPEC NEEDED` for a spec on disk.

**H10 — S7's amendment set omits five files that spell the retired mandate**, including the playbook
template itself (three sites), `.customize.md`, `WIRE-INTO-PROJECT.md`, `HYGIENE.template.md`, and
`check-memory-hygiene.sh:333`, whose check-7 exemption is justified by a rationale S2 deletes. §4's
Migration claim that the playbook is amended "by way of the domain-rules companion" is wrong: the
template spells the clause directly.

**H11 — drift-audit's `non_terminal_specs_cited_by_product_source` is at its pin with zero
headroom**, and six of S7's seven targets are inside its globs. One comment citing this spec's id
while it is non-terminal reds the bar.

**H12 — the leg's "independent second opinion" is not independent.** Check 13 takes its base from
the run-written file and validates it with check 9, which recomputes from the same subject-supplied
inputs. In the reproduction it exited 0 over a forged anchor. AC7's second half cannot be met in
scope.

**H13 — S2 removes the structural reason the run-state file is ever committed.** Every leg check is
keyed on `git ls-files`; an untracked run-state file makes checks 4, 5, 6, 8, 9, 11 and 13 vanish
silently. It also breaks the single-live-run rule: two concurrent preflights each see zero live runs.

## Factual errors, verified against source

| Claim | Actual |
|---|---|
| "the playbook template has 190 bytes free, measured 2026-08-11" | **148**. The number was copied from a stale manifest note, not measured — and that note says to read it from the gate |
| `parked:` is a fact the driver reads and writes | It is not. `park()` appends an unkeyed line; the reader greps a different key; `fact()` is `head -1`, so the "one entry per line" shape is unparseable |
| minting ids ahead of specs creates orphans, "which is what `ORPHAN_ID_PIN` counts" | A backlog row **defines** an id. The protocol *requires* minting one. The pin caps waiver rows, not orphans. The conclusion survives only because the waiver is at 5 of 5 |
| "`--plan` would read seven units as unreviewed" | Six. And all seven are CLOSED, so the terminal row short-circuits and the cited build cannot demonstrate the defect at all |
| `push-main.sh` brings the run's branch onto a newer default | It refuses to run off the default branch. The merge-base hazard may exist by another route, not this one |
| §5: "both inputs come from a commit the run cannot have made" | Assertion 4's second input is the working copy, which the run authors by definition |
| the backlog row's evidence | It cites "no documented rule and two live readings", not "one id for a build that has seven" |
| two §7 legs | quoted without the `--check` flag `gate-legs.json` runs; bare `drift_report.py` always exits 0 |

## What the review did not find

No live branch or worktree collides with this spec's file list; all ten other branches are ancestors
of `main`. The spec is machine-clean against the format contract — the hygiene gate exits 0 and a
hand-check of all ten sections, the header, the sub-head names and the writing rules found only 26
lines over 100 columns, the longest at 106. The parallel session owning the instruction layer could
not be located anywhere in the repo, which is its own finding: the cut-line's other half is
unlocatable by anyone but this session's author.

## Method

Five agents, one per lens, cold-started, told to refute by default and to reproduce before claiming.
Lenses: the authorization threat model; every factual claim against source; gate and harness
consequences; governance coherence and scope integrity; the derived gap list against the real corpus.
Three findings were independently confirmed by two lenses each — the hygiene check-3 blocker, the
backwards AC6, and the stale byte budget — which is why they are stated without hedging. Items the
lenses could not reproduce are marked HYPOTHESIS in the text above and nowhere else.
