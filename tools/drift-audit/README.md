# drift-audit kit

`gov:kit drift-audit@1.1` — the marker a deployer greps; paired with `KIT_DRIFT_AUDIT_VERSION` in
`drift_report.py` and asserted equal by `tools/check-kit-versions.sh`, which also holds each Tier-2
harness's own `meta.version` to the same number.

**Migrating 1.0 → 1.1 (breaking, `args` only).** The two Tier-2 harnesses no longer accept a
caller-supplied concurrency cap or verifier total; both are bare literals matching the review
protocol's ≤5. Delete those two keys from any `args` object you pass — they are ignored, not
honoured. Nothing else in the contract moved. The knobs never worked as documented on any adopter
whose `agent-cap.js` enforced the rule: the guard read the literal on the fallback's right-hand side
and the runtime used the caller's value, so the two disagreed silently. `agent-cap.js` 1.2 now
resolves the bound and denies that binder form, which is what makes the removal load-bearing rather
than cosmetic.

Measures whether a repo's own **records** still describe reality, and — at higher tiers — hunts dead,
unwired and duplicated code. Ported from the inCMS audit that found a repo where 24 of 58 in-flight
ledger rows contradicted git and roughly half of all non-terminal spec headers said "not built" about
shipped work, with every hygiene check green throughout.

Nothing was lost in that repo. The records had simply stopped being readable, and it took a human's
hunch to notice. This kit is the machine that notices instead.

## The premise

A governance repo gates its **code** contracts hard and its **record** contracts not at all. A
memory-hygiene gate checks that a spec Status token is spelled legally; nothing checks whether it is
**true**. That gap is where drift lives, and it is invisible by construction.

The four dispositions, in cost order — most records need the first, which is free:

| | When | Example |
|---|---|---|
| **Delete** | git or a generated file can derive it | a ledger's landed-state prose |
| **Gate** | must stay written, an oracle exists | spec Status headers |
| **Pin** | countable, no clean oracle | the three pins below |
| **Declare** | genuinely non-derivable | "was the human security review done?" |

The fourth row is real. Keep it **small and loud**, not buried in prose.

## Install

```bash
cp -r <governance>/tools/drift-audit <target-repo>/drift-audit
cd <target-repo>
drift-audit/adopt-drift-audit.sh
```

Requires `.memory-tree.conf` (owned by the memory-tree kit). This kit reads `MEMORY_ROOT` from it and
**declares no conf of its own** — there is deliberately no `--memory-root` flag. A second way to state
the same value is the hand-kept-second-copy defect the kit exists to detect.

Then, in order:

1. Fill `drift-audit/drift_signals.py` — `PRODUCT_GLOBS` at minimum.
2. Run `python drift-audit/drift_report.py`.
3. **Seed `PINS` at the values you just measured, not at zero.** A pin above the measured value hides
   a live regression on day one; a pin below it reds the bar on work nobody did.
4. Wire `--check` into your gate manifest.

## Layout

| File | Owner | What |
|---|---|---|
| `drift_report.py` | kit | the engine: five signal implementations, `--json`, `--check` |
| `drift_signals.template.py` | kit | the project layer's starting point |
| `drift_signals.py` | **project** | `PRODUCT_GLOBS`, `SHRINK_ONLY`, `HANDKEPT`, `PINS`, optional `CHARTER` |
| `SKILL.template.md` | kit | rendered to `.claude/skills/drift-audit/SKILL.md` by the adopt script |
| `adopt-drift-audit.sh` | kit | adopt + the `--check` sync arm for the merge bar |
| `selftest.py` | kit | the kit's own falsifiability test |

Tier 2 needs the two workflow scripts from `tools/workflows/drift-audit-{code,state}.js`.

## The signals

| Signal | Asks | Gateable |
|---|---|---|
| `ledger_rows_contradicting_git` | does an in-flight row claim "not merged" about a landed sha? | yes |
| `non_terminal_specs_cited_by_product_source` | does a SPECCED/INPROGRESS spec describe shipped work? | yes |
| `shrink_only_lists_not_shrinking` | are the lists that promise to shrink actually shrinking? | no |
| `handkept_inventories_disagreeing_with_source` | does a hand-kept list still match what generates it? | yes |
| `dangling_pointers_in_own_ledger` | do this node's own rows point at worktrees that exist? | no |

**Every signal carries a `live` field.** A signal whose population is empty prints `DEAD PROBE`
instead of a clean `0`. This is the kit's central rule and it is not decoration: the upstream repo's
convergence tool shipped a `collision_flags` signal structurally incapable of being non-zero, and
every reader took the 0 as "converged" for thirteen days. A metric that cannot move is worse than no
metric, because it is read as good news.

The kit holds itself to that rule — `selftest.py` exercises each gateable signal **twice**, once on a
fixture where it must be silent and once on a minimal violating fixture where it must fire. An arm
that can only pass the first is the dead probe the report refuses.

## Why pins rather than a perfect oracle

The spec-status oracle has one residual false-positive mode it cannot cheaply discriminate: an id
cited as a **forward** reference ("TODO: see FOO-1") reads identically to one citing shipped work. And
`INPROGRESS` is arguably true of a built-but-unmerged unit.

Chasing a perfect oracle is the expensive way to be wrong. A shrink-only pin drains the population
without needing one, and it is the idiom these repos already use for exactly this. Lower a pin as its
population drops; raising one needs the same justification as any other ratchet raise.

## Oracles are tightened against FIELD false positives, never speculatively

Both corrections in this kit's history came from a real misjudged row, and both are recorded at the
code:

- Keying the spec signal on the **slug** over-flagged 107 of 126 — one shipped unit made all 14
  siblings of its multi-spec build look stale. The **seq** is the discriminator.
- Including a `scripts/` tree let an **id catalog** (a recall alias file listing every id in the
  corpus) certify all 110 specs. Product source only; a record certified by an index of records is
  circular.
- The ledger signal flagged a row whose only sha was a **parity comparison baseline**
  ("byte-identical vs `X`"). The reference-sha exclusion now covers `vs|against|compared to|relative
  to` as well as `off|base`.
- This repo's own first `HANDKEPT` probe compared charter **bullets** (12) to **legs** (19) — numbers
  that should never be equal, so it was permanently red. Comparing leg **names** gives a predicate
  that can legitimately reach zero.

Widen an exclusion when a real row is misjudged. Never pre-emptively: every term costs detection power.

## Known portability trap

`selftest.py` compares the Python conf parser against a shell sourcing the same file. On Windows a
bare `bash` resolves to the **WSL** shim ahead of MSYS on PATH, and it cannot source a Windows temp
path the same way — so the comparison fails on an interpreter mismatch rather than on real parser
drift. The selftest therefore **resolves** a working POSIX shell by probing candidates, and if none
works it prints `SKIP` and tallies it. It never prints `ok` for an arm that did not run.

## Tiers

| Tier | Cost | Answers |
|---|---|---|
| 0 | seconds, 0 agents | Are the records still true? Which pins moved? |
| 1 | ~20 min, ≤5 agents | Why did a signal move? Is an instrument blind? |
| 2 | hours, ~22 agents | Dead / unwired / duplicated code, and everything above |

In the founding audit, **Tier 0 alone produced the blocker, the vacuous-metric lead and the entire
work-state answer.** The 22 agents deepened those and added the code findings; they did not originate
the most consequential ones. Run Tier 0 first, always. The rendered Skill carries the eight harness
invariants for the agent tiers — read those before any Tier 1 or 2 run.
