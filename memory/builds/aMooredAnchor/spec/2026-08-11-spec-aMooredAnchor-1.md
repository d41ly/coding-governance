# TOOL-aMooredAnchor-1 — marker grammar, the lifecycle the kit never had, and two silent skips

**Status:** CLOSED · rev-5 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling · review wf_cc04b49a-8d3

## 1. Goal

Close the five reproduced defeats in the unattended kit that do **not** depend on which commit the
anchor names, and state the anchor's real bound in the protocol instead of asserting a guarantee that
does not hold. Today one `git update-ref refs/replace/<base>` makes the mandate comparison read bytes
the run authored, a run can widen its own authorization inside the mandate block while both sides
compare byte-equal, and the first successful unattended landing reds the merge bar permanently.

## 2. Scope (IN)

- **S1** — **Replace-free provenance reads.** Every object read that establishes provenance is
  replace-free, and a repo running an unattended run may not carry replace refs or grafts at all: a
  positive check that `git for-each-ref refs/replace/` is empty and `.git/info/grafts` is absent.
  Neutralising the mechanism and refusing its presence are two different checks and both land.
- **S2** — **The marker grammar.** `region()` rejects a marker line carrying anything beyond the
  marker itself, in both copies, and `splice()` likewise. A marker line is the marker or it is a
  malformed pair.
- **S3** — **The terminal-record lifecycle.** A landed run-state record must not red the bar forever.
  Check 9's question changes from *the recorded base equals the merge-base* to *the recorded base is
  an ancestor of the resolved anchor and is not HEAD*. This is fork-independent and it is what makes
  the kit survive its own first success.
- **S4** — **Every silent path in check 9 becomes a named refusal**, over the three real exits: the
  default branch is unresolvable, no candidate ref resolves, and a candidate resolves but
  `git merge-base` fails.
- **S5** — **The population loop stops word-splitting.** Iterate with `while IFS= read -r`, and make a
  selected-but-unreadable path a named refusal rather than a `continue`.
- **S6** — **The gate stops reading `GOV_DEFAULT_BRANCH`**, and the driver's own read is named in
  scope with it so the two cannot disagree about where the name comes from.
- **S7** — **The fixture rework S5-of-rev-1 did not budget.** Both sibling suites gain
  `git remote set-head origin main`; the gate suite loses `export GOV_DEFAULT_BRANCH=main`. Every new
  red arm gets a control that distinguishes *red because the thing under test is broken* from *red
  because no default branch resolved*.
- **S8** — **The protocol states the bound**, as the checkable sentence in §4, replacing the
  unforgeability claim. The false comment at `tools/unattended/unattended.sh:119-120` is corrected and
  quoted in full so the target survives line drift.
- **S9** — A `memory/gotchas/` record for the class the review's own method demonstrates: *a gate that
  reads the same subject-supplied input as the driver is a second implementation, not a second
  opinion* — extended by what this review found, that the second opinion can also be defeated at the
  **read path** rather than at the input.

## 3. Non-goals (OUT)

- **The trust root itself.** `refs/remotes/origin/HEAD`, `remote.origin.url`, `url.*.insteadOf` and
  the default-branch NAME all remain subject-supplied after this unit. That is fork F1, it is now
  correctly priced in §8, and it is a separate build. This unit **documents** the bound rather than
  closing it, and §8 says so in the protocol's own words.
- Signature verification and any key provisioning. Option C is only true with an out-of-band keyring
  supplied on the git command line; that is its own build with its own spec.
- Any network dependency on the merge bar. Rev-1 proposed one; it is withdrawn with option A.
- The driver's `resolve_base` candidate loop and its `base == HEAD` refusal. Landed in `b94818b`,
  armed, unchanged.
- The five non-authorization `GOV_DEFAULT_BRANCH` readers, and the `--no-verify` git-level bypass.
- `base-ref:` as a sixth authored key. Under any fork answer it carries no discriminating information
  that `base:` does not already carry, so it is deferred with fork F1 rather than landed here.

## 4. Design

### What rev-1 got wrong

Rev-1 recommended fetching the anchor from the remote and argued it was sound because *"to forge it
the run must land a default-branch push, which is the act under authorization."* That sentence is
false and it was the load-bearing justification. `origin` is not an identity; it is a lookup in
`.git/config`, which is untracked, appears in no commit, and therefore has no value at BASE for
anything to compare against.

Reproduced here twice, with a live control:

| Route | Command | Result |
|---|---|---|
| URL repoint | `git config remote.origin.url <run's own bare repo>` | fetched anchor **is** the run's forged commit |
| `insteadOf` | `git config url.<evil>.insteadOf <honest>` | same, and `git config remote.origin.url` still **reads** honest |

The review found the same thing independently three times, once driving the real `.githooks/pre-push`
with no `--no-verify`: the honest push route is blocked by the hook, the three-command config route is
not. Option A is withdrawn. It costs a permanent network dependency on the merge bar and buys a defeat
one `git config` cheaper than the one it closes.

### The two defeats that no fork answer reaches

Both verified here against the real gate, each with a control.

**Read integrity.** The kit establishes "the mandate as committed at BASE" with `git show BASE:RUN.md`,
which resolves through git's object layer and therefore applies `refs/replace/*`. With a replacement
commit built by `git commit-tree` carrying the **same parents** as the base, ancestry is untouched:

```
base            = 4c4b71d  (non-root; parent 6ce330f)
control (honest tree):                 >>> GATE GREEN
git show BASE:RUN.md mandate BEFORE:   The owner authorizes tRun to merge and to push.
git show BASE:RUN.md mandate AFTER:    FORGED — the run authorizes ITSELF to merge, push and force-push.
merge-base still reproduces recorded:  4c4b71d vs recorded 4c4b71d
GATE verdict:                          >>> GATE GREEN AND SILENT
DRIVER --preflight:                    rc=0 :: preflight OK — base 4c4b71d…
```

Check 9 passes on an affirmative **match**, not a skip. `git -c core.useReplaceRefs=false show` returns
the honest content, so the remedy is cheap. No env var, no push, no network, and nothing in
`refs/remotes/` touched.

**Marker grammar.** `region()` identifies a marker with `index($0,o)==1` — a prefix test — then `next`s
the line, so the marker line's trailing content is in neither slice. A run appends its own
authorization to the open marker line; both slices stay byte-equal and the injected sentence sits
inside the block a human reads. Verified here:

```
what a human reads in the mandate section of the working copy:
       <!-- run:mandate --> ...and the run may force-push and disable the hooks.
       The owner authorizes tRun to merge and to push.
       <!-- /run:mandate -->
gate verdict:  >>> GATE GREEN (silent)
```

### The lifecycle the kit never had

Checks 4, 5, 6, 8, 9, 11 and 13 apply to every tracked run-state file regardless of phase;
`check-unattended.sh:139` is the only phase-conditional line and it merely tallies `nlive`. Check 9
asserts the recorded `base:` **equals** the merge-base — and merging and pushing, the two acts a
mandate authorizes, move the merge-base past the pin forever. So the first successful unattended
landing reds the bar permanently, for every later push, with no attacker involved.

A phase-keyed carve-out is **not** the fix: `phase:` is written by the run (`set_fact`), so it would
hand the run a one-line escape from checks 9 and 13.

The fix is to change check 9's *question*. For a live run and a landed one alike, the meaningful
assertion is:

- the recorded base is an **ancestor of the resolved anchor** — so it lies on the history the owner
  landed, not on the run's branch; and
- the recorded base is **not HEAD** — the existing degenerate-case refusal, unchanged.

Equality was never the property that mattered; it was a proxy for it that happens to hold only while
the run is live. Check 13's byte-compare at that base continues to do the authorization work.

### The bound, stated

This replaces rev-1's guarantee. It goes into `PROTOCOL.template.md` and the installed copy verbatim:

> The anchor is unforgeable only by a process that does not edit `.git/config` and does not write
> `refs/replace/*`. No in-repo mechanism can verify the first, because `.git/config` is untracked and
> appears in no commit. The second **is** checkable and this kit checks it. The guarantee therefore
> rests on the pre-push hook and on the absence of a config-level redirect, and a run with full repo
> write access can defeat it — which is the boundary, stated rather than argued.

It is worth more than option A because it is true and the next reviewer can test it.

### Inventory — check 9's exits, before and after

| Exit | Today | After |
|---|---|---|
| `GOV_DEFAULT_BRANCH` set | trusted verbatim | not read by the gate |
| default branch unresolvable (empty `$d`) | whole block skipped, silent | named refusal |
| no candidate ref resolves | loop falls off the end, silent | named refusal |
| candidate resolves, `git merge-base` fails | `continue`, then silent | named refusal |
| recorded base is not an ancestor of the anchor | not asked | named refusal |
| recorded base equals HEAD | refusal | unchanged |
| a selected path is unreadable | `continue`, silent | named refusal |
| a path with a space | word-split into two, both skipped | read intact |

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1 replace-free, S2 grammar in `region`/`splice`, S6 driver read, S8 comment |
| `tools/unattended/check-unattended.sh` | S1 both halves, S2, S3, S4, S5, S6 |
| `tools/unattended/unattended.test.sh` | arms + controls; S7 fixture; the `:145` refusal string changes |
| `tools/unattended/check-unattended.test.sh` | arms + controls; S7 fixture and the dropped export |
| `tools/unattended/PROTOCOL.template.md` | S8's paragraph |
| `memory/guides/UNATTENDED-PROTOCOL.md` | the installed copy, byte-equal after prefix stripping |
| `memory/gotchas/` + `INDEX.md` | S9, re-rendered |
| `memory/map/features/unattended.md` | the dossier claim |
| `.memory-tree.conf` | `ARMS_FLOORS` RAISED to the measured counts for both files |
| `.claude/SESSION-KICKOFF.md` | ratchet re-stamp — `.memory-tree.conf` is a watched pathspec |

### Alternatives rejected

**Skip terminal phases in the gate.** `phase:` is run-written, so it is a one-line escape from the two
checks that matter.

**Keep equality and archive the record at `--close`.** Defensible, and heavier: it needs a new path the
leg does not select, a gate that the move happened, and a migration for adopters. The question change
achieves the same with no new state.

**Fetch the anchor (rev-1's option A).** Withdrawn — see above.

## 5. Production-readiness checklist

- **security** — the unit is the security work; the threat model is an agent process with full repo
  write access and no owner turn. Three of the four blockers were reproduced against the real gate.
- **perf / scale** — no network on the bar (option A withdrawn). One `for-each-ref` and one
  `merge-base --is-ancestor` per run-state file. This repo has zero run-state files, so the loop does
  not run here at all — which is why the new paths are exercised by the self-tests, not by this repo's
  bar. Rev-1 claimed the opposite and was wrong.
- **a11y** — N/A — a shell gate with no interface.
- **i18n** — N/A — refusal strings are the repo's operator English, as every other leg.
- **error / empty / loading states** — the empty states are the substance: no default branch, no
  candidate ref, a failing merge-base, an unreadable path. Each becomes a named refusal.
- **observability** — every refusal names its check number, the offending value and the file.
- **risks** — the fixture rework is the main one: S7 changes inputs both suites have depended on, and
  the shipped suite has been running permanently in the no-`origin/HEAD` state, so its only check-9
  coverage exists because of an export this unit removes. Second: `ARMS_FLOORS` sits exactly at its
  pins for both files, so any refusal that moves between files drops a count below a shrink-only floor.
- **testing + left-shift gates** — every arm pairs with a control, and each new red arm asserts refusal
  text distinct from S4's, or it proves only that some refusal was reached.
- **migration / rollback** — no run-state grammar change (`base-ref:` deferred), so no adopter
  migration. Rollback is a revert. A landed record that reds today becomes green, which is the point.
- **user docs** — the protocol carries the bound; the charter's gate-suite bullet gains the replace-ref
  refusal.

## 6. Acceptance criteria

- **AC1** — When a run replaces the base commit with a same-parent `commit-tree` forgery and the
  working copy carries the forged mandate, the gate reds. It exits 0 silently today, with merge-base
  affirmatively matching. Green control: an honest tree with the replace ref absent.
- **AC2** — When any `refs/replace/*` ref exists, or `.git/info/grafts` exists, the gate reds naming
  it, independently of whether a forgery is present.
- **AC3** — When text is appended to the `<!-- run:mandate -->` open marker line in the working copy
  and not at BASE, the gate and the driver both red. Both exit 0 today. Same for the close marker, and
  for the `run:generated` pair. Green control: clean markers.
- **AC4** — When a run-state record is LANDED and the merge-base has moved past the recorded base, the
  gate is **green**. It reds permanently today, on an honest tree with no attacker.
- **AC5** — When the recorded base is not an ancestor of the resolved anchor, the gate reds.
- **AC6** — When the default branch is unresolvable, when no candidate ref resolves, and when a
  candidate resolves but `merge-base` fails, the gate reds with three **distinct** named refusals.
  The third is reachable with an orphan-history fixture.
- **AC7** — When a tracked run-state path contains a space, every check still runs on it. Today it
  word-splits and is skipped by all seven.
- **AC8** — When `GOV_DEFAULT_BRANCH` is set to any hostile value, the gate's verdict is unchanged
  from the same tree with it unset. Both suites run green with it unset and with it hostile.
- **AC9** — When both sibling suites run, each reports PASS with a higher assertion count than today,
  and no previously-green control has become red. The S7 fixture change lands in the same commit as
  S4 and S6, or six green controls red.
- **AC10** — When `check-arms.py` runs, every new `fail` branch is armed by a positive assertion
  naming its own text, and `ARMS_FLOORS` is RAISED to the measured counts. The gate only reds when a
  count falls, so a forgotten raise is silent and must be checked by hand.
- **AC11** — When `bash tools/run-gates.sh` runs on the finished tree, every leg is green. Noted:
  a green bar here exercises none of the new refusal paths, because this repo has no run-state file.

## 7. Gates

The full bar, `bash tools/run-gates.sh`. Legs this unit moves:

- the three unattended legs, and `check-unattended.sh` check 10 — the protocol-parity comparison,
  which is the leg that actually sees `PROTOCOL.template.md` change. `adopt-unattended.sh --check`
  reads only the Skill render and does not.
- `tools/memory-tree/check-arms.py` with raised `ARMS_FLOORS` for both files.
- `bash tools/memory-tree/check-memory-hygiene.sh` checks 17-19 for the S9 record, plus
  `gotchas.py --write` to re-render `INDEX.md`.
- `python tools/codebase-map/test_codebase_map.py` — the dossier claim and a fresh render.
- `skills/session-kickoff/manifest-check.sh` — `.memory-tree.conf` is a watched pathspec, so the
  ratchet re-stamps.
- `tools/check-kit-versions.sh` — the kit version constant moves as a matched pair.

`tools/gate-legs.json` does **not** move: no new `.sh` is added, because F2 is resolved in §8 as *no
shared resolver file*. Had it been added, the leg count, the dossier's gate-legs row, a fresh map
render and a charter bullet would all move with it.

## 8. Open questions

### F1 — the trust root · RESOLVED (owner, 2026-08-11): option D, restated honestly

The owner picked "the builder's recommendation" while that recommendation was option A. A is now
withdrawn on reproduced evidence (§4), so the recommendation it named has changed to **D**, and the
menu it was picked from was mispriced in three of four entries. Recorded for the record:

| Option | Rev-1 pricing | Corrected |
|---|---|---|
| A · fetch the anchor | sound; costs a network dependency | **false** — the fetch resolves through untracked `.git/config`. Withdrawn |
| B · reflog provenance | corroboration only | unchanged, still correct |
| C · signature verification | "the only purely-local unforgeable root" | **false as stated** — three repo-local config lines make `git verify-commit` exit 0. True only with the keyring supplied on the git command line from outside the repo, which is its own build |
| D · concede the bound | honest but cheapest | **picked**, and it must say that `refs/remotes/origin/HEAD` is subject-supplied too, or D's own paragraph is false |

This unit therefore takes D, writes §4's checkable sentence, and moves the substance off the fork.
**Deferred to a follow-up build**: closing the trust root at all, for which C is the only candidate
that can be made true.

### F2 — one resolver or two · RESOLVED (builder, 2026-08-11): neither, no new file

Rev-1 leaned toward a shared sourceable `tools/unattended/anchor.sh`, on a cost note that was wrong in
both directions: `check-arms.py` discovers a file only when it **defines** `fail() {`, so a
`fail()`-free resolver is invisible to the meta-gate and needs no floor, while a `fail()`-defining one
plus the sibling test the charter requires would move `gate-legs.json`, the dossier's gate-legs row,
a fresh map render and a charter bullet — all of which §7 denied. With option A withdrawn there is no
fetch to share, so the resolver stays where it is and no file is added.

### F3 — `base-ref:` · RESOLVED (builder, 2026-08-11): deferred with F1

Under every fork answer the local ref name carries no information `base:` does not, so its
disagreement branch compares a constant with itself — this corpus's own
`assertion-between-two-derived-values` class. Deferred rather than dropped: if F1's follow-up lands a
real trust root, the discriminating pair to record is the remote plus the upstream branch plus the
anchor sha, not the local ref name.

### F4 — a network dependency on the bar · RESOLVED (builder, 2026-08-11): none

Dissolved by A's withdrawal. Rev-1 could not have answered it anyway: its premise was that terminal
run-state files are "almost never", and they are the steady state of every adopter that has completed
a run.

### F5 — RESOLVED (superseded, 2026-08-11)

`git ls-remote --symref origin HEAD` returned empty against a plain `git init --bare` origin in two
independent fixtures. This does not block this unit, which asks no remote anything. It is recorded
because F1's follow-up will want it and it is not automatic.

RESOLVED elsewhere: `aStandingWrit` S0 hit exactly this while making the anchor an observation of
the remote, and its fixture now sets the bare repo's HEAD symref explicitly before any arm runs.
The answer is in `unattended.test.sh`, not here. Nothing for the owner to decide.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Written after the reproduction harness ran, so §4's table was
  measured rather than argued.
- rev-2 · 2026-08-11 · folded review `wf_cc04b49a-8d3` (38 raw, 32 confirmed, 6 refuted, precision
  0.84; 17 distinct defects, 4 blockers). Verdict was FOLD AND REBUILD and this is the rebuild, not a
  patch. Option A withdrawn after independently reproducing both config routes; the unit re-scoped
  off fork F1 entirely onto the five defeats no fork answer reaches. Added S1 (replace-free reads),
  S2 (marker grammar), S3 (terminal lifecycle), S5 (word-split population); corrected S4's exit
  enumeration from three to the three real ones; added S7, the fixture rework rev-1 did not budget.
  Status moves OPEN to SPECCED.
- rev-3 · 2026-08-11 · BUILT. Status moves SPECCED to INPROGRESS, which in this tree means built and
  reviewed but NOT landed — the merge and the push each need an explicit ask, and this run holds no
  committed standing mandate. Five of six reproduced defeats verified closed against the original
  harnesses; the sixth is `TOOL-aMooredAnchor-2` by design. Two corrections found while building:
  the fixture reset had to restore the REF namespace and not just the work tree, and a per-ref
  cleanup loop cost 2m18s of process spawn until it was batched through `update-ref --stdin`.

- rev-4 · 2026-08-11 · REBASED onto `aStandingWrit` S0, which landed on main while this unit was
  building and solved the overlapping half independently. Their work supersedes this spec's S1 anchor
  material and is better on one measured point: `GIT_NO_REPLACE_OBJECTS=1` does NOT suppress a graft
  file, and only `GIT_GRAFT_FILE` pointing outside the repo does — so their `GIT()` pin replaces the
  export this unit had written. Their protocol §9 states the boundary better than this spec's §4
  paragraph did, so that paragraph is withdrawn rather than duplicated: a rule in two carriers is a
  defect in the second. What rebased forward, each still a live defect on main at `c839f5d` and each
  verified absent there before re-applying: the marker-line grammar, the terminal-record lifecycle,
  the word-split population loop, and the replace-ref/graft PRESENCE refusal. F1 is therefore moot
  for this unit — the anchor is `TOOL-aMooredAnchor-2` and now also `aStandingWrit`'s §9.

- rev-5 · 2026-08-11 · CLOSED. Landed at `7890bec`. `TOOL-aMooredAnchor-4` built in the same
  pass: the two sibling self-tests were costing 77s and 73s for ~1.4s of CPU apiece, and the cause
  was NOT the git calls. `fact`, `fact_of`, `phase_of` and `core_of` were each `sed | head | tr` —
  three processes per call, called per run-state file per check. Converted to pure bash, plus the
  two `--plan` sites to a single awk: **1094 sed/head/tr spawns to 278, a 75% cut**, both suites
  green at 74 and 103 assertions. Measured by process COUNT rather than wall clock, because ten
  worktrees share this box and wall time moved 20% between two runs of identical code. Pinned by a
  source-level arm in each suite; that arm immediately found the two `--plan` sites.

## 10. Reuse audit

Unchanged in conclusion from rev-1, and one correction. `reuse_lookup.py` returns no seam that fits;
the nearest ancestry wrapper, `Git` in `tools/drift-audit/drift_report.py`, resolves its base ref from
`GOV_DEFAULT_BRANCH` first, which is the opposite of what S6 wants — so wiring through it would import
the defect. The review challenged the wording of that claim and refuted the challenge: the decision is
right even though rev-1 stated the ladder loosely.

The correction: rev-1 said "the seam this unit creates is `resolve_base`, extended to a trust root and
shared with the gate per F2." With A withdrawn and F2 resolved to no new file, this unit creates no
seam. It hardens two existing ones in place — `region()`, whose contract `check_mandate`,
`verb_status`, check 8 and check 13 all share, and check 9's question.
