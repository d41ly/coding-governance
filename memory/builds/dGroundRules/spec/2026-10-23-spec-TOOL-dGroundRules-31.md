# TOOL-dGroundRules-31 — the install-day scaffold defers the mirror over uncommitted inputs, so the first `--scaffold` in a repository with history exits 0

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-31-deviation-19.md](../build/2026-10-23-build-TOOL-dGroundRules-31-deviation-19.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-27 TOOL-dGroundRules-30 TOOL-dGroundRules-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 24 at HIGH**, item **H4**, which no other id shares. This unit is
id 24's promotion, built from the skeptic's corrected fix, because the finder's was judged unsound.
It repairs `TOOL-dGroundRules-25`, which sits at order 8, so it builds at order 9.

`TOOL-dGroundRules-25` S7 has `adopt-policy.sh --scaffold` run `policy.py mirror --write` whenever
HEAD resolves, and never says what happens when that call refuses. `mirror --write` exits 2 with
`uncommitted changes` whenever a recorded input differs from HEAD, and on install day every input
does: the target is committed, the install is staged and not yet committed, and the scaffold has
just written the policy file. So the first `--scaffold` in any repository with history exits 2. This
unit turns exactly that refusal into a named deferral and leaves every other refusal standing.

## 2. Scope (IN)

- **S1** — The deferral. When the `mirror --write` call of `--scaffold` exits 2 and its refusal
  line carries `uncommitted changes`, over any input the mirror records (`TOOL-dGroundRules-25` S20,
  the `legacy_blobs` keys and `.agent-cap.conf` included), `adopt-policy.sh` prints one line,
  `adopt-policy: mirror deferred · <the input the refusal names> has uncommitted changes · commit, then re-run --scaffold`,
  and goes on; `--scaffold` then exits 0 when nothing else failed. The scaffold compares no input
  itself. Observed by AC1, AC3.
- **S2** — Every other refusal stands. Any other non-zero exit of that call makes `--scaffold` exit
  non-zero, printing the call's output. Observed by AC4.
- **S3** — The re-run writes. Over a target whose install and policy file are committed, `--scaffold`
  writes `.governance/policy.json`, which is `TOOL-dGroundRules-25` AC7's second clause observed on
  the re-run after the first commit. Observed by AC2.
- **S4** — The case. `adopter-fresh-target` asserts the deferral line on its first `--scaffold`, run
  over the state `TOOL-dGroundRules-24` §4 step 4 leaves, and the written mirror on the re-run after
  its first commit, which `TOOL-dGroundRules-25` S7 adds. Observed by AC1, AC2.
- **S5** — The armed branch. `tools/policy/adopt-policy.test.sh` arms S2's exit, and its
  `ARMS_FLOORS` row in `.memory-tree.conf` moves to what `check-arms.py --emit-floors` prints.
  Observed by AC4.
- **S6** — The help page. `help/policy.md`'s install section quotes the deferral line and the order:
  commit the install and the policy file, then re-run `--scaffold`. Observed by AC5.

## 3. Non-goals (OUT)

- The refusal itself and the set of inputs it compares: `TOOL-dGroundRules-5` and
  `TOOL-dGroundRules-25` S20, unchanged.
- The settings render `--scaffold` also runs (`TOOL-dGroundRules-21` S37), whose refusal set this
  finding does not name.
- Committing on the adopter's behalf. The scaffold never commits.

### Edges

- **consumes-from** `TOOL-dGroundRules-25` — `--scaffold`'s `mirror --write` call (S7), the widened refusal over every recorded input (S20) and AC7, whose second clause this unit observes on the re-run
- **consumes-from** `TOOL-dGroundRules-5` — `mirror --write`'s exit 2 and its `uncommitted changes` refusal line, the one shape this unit defers
- **hands-off** `TOOL-dGroundRules-34` — `--scaffold`'s deferral, which that unit makes wait for `arm_schema`, AC4, which that unit observes through the real verb, and the install text of `help/policy.md`, which that unit puts under `## Install` (ids 32 and 30 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read on 2026-10-23.

- `TOOL-dGroundRules-5` §4 "The verbs": `mirror --write` compares each input with HEAD and exits 2
  with `policy: refused · <path>:0 · uncommitted changes; the mirror renders a revision, commit
  first`, an input absent at HEAD included.
- `TOOL-dGroundRules-25` S20 widens that comparison to every input the mirror records, and S7 runs
  the call from `--scaffold` "whenever HEAD resolves".
- `TOOL-dGroundRules-24` §4 steps 1 to 4: a committed target, `apply` staging the install without a
  commit, then the first `--scaffold`, "exit 0 expected".
- `TOOL-dGroundRules-21` S37 already prints one line naming the re-run when HEAD does not resolve,
  the house shape this deferral follows; `.memory-tree.conf:639` sets `ARMS_REFUSALS="graded"`.

### The scaffold's mirror step after this unit

```text
if HEAD resolves:
    out, rc = run(policy.py mirror --write)
    if rc == 0:                                   pass
    elif rc == 2 and "uncommitted changes" in out: print deferral line naming the input; continue
    else:                                         print out; exit rc
```

### Rollout

Order 9 holds `TOOL-dGroundRules-27`, which also writes `tools/policy/check_policy.py`; the inline
author builds that unit first and this one after it, as its Rollout states.

### Inventory

No identifier is minted; the deferral line is a new output string.

### Files touched (estimate)

- `tools/policy/adopt-policy.sh`
- `tools/policy/adopt-policy.test.sh`
- `tools/policy/check_policy.py`
- `.memory-tree.conf`
- `help/policy.md`

### Alternatives rejected

- **The scaffold compares the inputs with HEAD itself and skips the call.** A second copy of the
  refusal's input set, which drifts the day `TOOL-dGroundRules-25` S20's set grows.
- **Defer on any exit 2.** An invalid policy file under `refuse` also exits 2, and deferring it hides
  the one refusal install day must show.

## 5. Production-readiness checklist

- security — N/A: no write is added; the deferral writes less than before.
- perf / scale — unchanged: the one `mirror --write` call S7 already makes.
- error / empty / loading states — the uncommitted refusal is a named deferral with its remedy; every
  other refusal still exits non-zero with its own line.
- observability — the deferral line names the input and the next command.
- risks — an adopter who never re-runs `--scaffold` lands without a mirror; the policy kit's
  `[[generated]]` check reds that at the adopter's bar and names `mirror --write`.
- testing — `adopter-fresh-target` and `adopt-policy.test.sh`, AC1 to AC5.
- migration — none.
- user docs — `help/policy.md`, S6.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py`, `adopt-policy.sh` and `policy.py` under the kit, and `policy.json` under
`.governance/`, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python check_policy.py --fixture adopter-fresh-target` runs on the built tree, its
  first `--scaffold` exits 0 and prints `mirror deferred`, and the target holds no `policy.json`
  after it.
  Red when: the install-day scaffold exits 2, or writes a mirror of a revision the commit will not
  carry.
- **AC2** — When the same case re-runs `--scaffold` after its first commit, `policy.json` is written
  and `python policy.py mirror --check` in the target exits 0.
  Red when: the deferred mirror is never written.
- **AC3** — When `bash adopt-policy.sh --scaffold --target <t>` runs over a committed target whose
  policy file is committed and whose `.agent-cap.conf` carries an uncommitted edit, it exits 0 and
  the deferral line names `.agent-cap.conf`.
  Red when: a refusal over an input other than the policy file escapes the deferral.
- **AC4** — When `policy.py` in a scratch copy of the kit is staged to exit 2 printing a refusal line
  that carries no `uncommitted changes`, `bash adopt-policy.sh --scaffold --target <t>` exits
  non-zero and prints that line.
  Red when: every exit 2 is read as a deferral.
- **AC5** — When `grep -n "mirror deferred" policy.md` runs, it prints a line of the install
  section.
  Red when: the install-day line is undocumented.

## 7. Gates

`kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case and the suite; they are named by the arm
lines, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture adopter-fresh-target`) · covers AC1 AC2 · the deferral branch staged out of `adopt-policy.sh` in a scratch copy · none
New arm: tools/policy/adopt-policy.test.sh · covers AC4 · `policy.py` staged to exit 2 with a refusal that is not `uncommitted changes` · `ARMS_FLOORS`, as `check-arms.py --emit-floors` prints it

## 8. Open questions

- **F1 — How does `--scaffold` treat the mirror's refusal on install day?** (a) Defer exactly the
  `uncommitted changes` refusal, over any recorded input, with one line naming the input and the
  re-run. (b) Compare the policy file and the catalogue with HEAD in the scaffold and skip the call
  when either differs. (c) Leave the refusal to exit 2. (c) fails `TOOL-dGroundRules-24` §4 step 4's
  exit 0 and AC1 (veto 1). (b) misses an uncommitted `.agent-cap.conf` or `legacy_blobs` input, which
  still exits 2, and fails AC3 (veto 1). (a) meets every criterion. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 24 (HIGH, item H4) of the round-1 spec
  audit of units 22 to 25, from the skeptic's corrected fix, with the refusal of `TOOL-dGroundRules-5`
  §4 and the install flow of `TOOL-dGroundRules-24` §4 read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-25` S7's `mirror --write` call inside `--scaffold`, which
keeps its place, and `TOOL-dGroundRules-21` S37's one-line re-run notice, whose shape the deferral
copies. `python tools/codebase-map/reuse_lookup.py "an adopter step that defers a render until the install is committed"`
ranked `adopt`, `render` and `step`; no adopter in the tree defers a render on an uncommitted input,
so no existing seam fits the branch itself. The recall probe returned `TOOL-dGroundRules-16`'s
install-day case, this audit's H4 and the round-2 item that first asked `--scaffold` to run the
mirror; all three agree with this design and with the refusal `TOOL-dGroundRules-5` specifies.

Recall terms used: `python tools/memory-recall/query.py "how does an adopter scaffold handle a render
that refuses uncommitted changes on install day" --terms "adopt-policy scaffold mirror write
uncommitted changes refusal deferred commit first install day exit 2"`
