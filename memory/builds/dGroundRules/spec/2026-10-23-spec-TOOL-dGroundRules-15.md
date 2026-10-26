# TOOL-dGroundRules-15 — the `.agent-cap.conf` lowering in one home: inside `resolve_read`, so every reader of the limit sees it

**Status:** CLOSED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-15-deviation-3.md](../build/2026-10-23-build-TOOL-dGroundRules-15-deviation-3.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-15-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-15-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 TOOL-dGroundRules-87 TOOL-dGroundRules-88 |
| [2026-10-23-prompt-TOOL-dGroundRules-15-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-15-build-brief.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-9-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-9-close-arms-brief.md) | research | TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 2 at HIGH**, item **H1**, which no other id shares. This unit is its
promotion. It repairs `TOOL-dGroundRules-10` and builds at order 6, one step after that unit.

Three specs place the one lowering in three homes. `TOOL-dGroundRules-10` S1 puts it in
`resolve("runtime.agents-in-flight")`; `TOOL-dGroundRules-5` renders the mirror through
`resolve_read`, which a lowering in the `resolve` wrapper never reaches; `TOOL-dGroundRules-3` says a
legacy home adds a step to `RESOLUTION_ORDER`. Built as written, `policy.py get` prints the lowered
limit while the mirror holds the unlowered one, and rule 7 of `tools/hooks/agent-cap.js`, which reads
the limit through `readPolicy`, admits a hand-raised `env` above the conf's lowering. This unit moves
the lowering to one place every reader passes through: the end of `resolve_read`.

## 2. Scope (IN)

- **S1** — One home. `resolve_read(path, row, read)` in `tools/policy/policy.py` applies
  `read_legacy_fanout` to the `Resolution` it is about to return when `path` is
  `("runtime", "agents-in-flight")`, after `RESOLUTION_ORDER` and after the invalid-file branch, so
  a `last-valid` value is lowered too. The conf is read once per revision read, at the revision the
  read holds, and kept on the read. `resolve` holds no lowering of its own. Observed by AC1, AC4.
- **S2** — Every reader through it. `get`, the mirror render, the `last-valid` branch and the
  settings render of `TOOL-dGroundRules-10` S2 each reach the limit through `resolve_read`, and
  each answers the lowered value. Observed by AC1, AC2, AC3.
- **S3** — The cases `limit-conf-mirror` and `limit-conf-last-valid` in `CASES` of
  `tools/policy/check_policy.py`, which fail as planted on a build where the lowering sits in the
  `resolve` wrapper. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- The mirror's freshness against the conf: a landing that changes only `.agent-cap.conf` and skips
  regeneration. That is finding id 49, item M23, a MEDIUM promoted in `TOOL-dGroundRules-21`, which
  records the conf's blob in the mirror and compares it.
- Changing the conf's grammar, the refusal of a malformed `FANOUT_CAP`, or the reason text
  `TOOL-dGroundRules-10` S1 spells.
- A `RESOLUTION_ORDER` step. The order returns the first `Resolution` a step answers, and a lowering
  needs the answer the order gave (§8 F1).

### Edges

- **consumes-from** `TOOL-dGroundRules-10` — `read_legacy_fanout`, its reason text and refusal, the settings render and the `limit-` case fixture, which this unit re-homes and extends
- **consumes-from** `TOOL-dGroundRules-5` — `resolve_read` and its per-revision read, the one composition the mirror renders through
- **hands-off** `TOOL-dGroundRules-21` — the conf as a resolution input whose blob the mirror records and the helper compares (finding id 49)
- **hands-off** `TOOL-dGroundRules-25` — `derive_lowered_limit`, which that unit's map regeneration records (finding 34)

## 4. Design

### Evidence

- `TOOL-dGroundRules-10` S1: "`resolve("runtime.agents-in-flight")` returns the smaller of the
  value its resolution order gives and that line's integer", read "at the same revision `resolve`
  reads the policy file".
- `TOOL-dGroundRules-5` §4 "The render": `render_mirror` "runs the reader's per-key resolution for
  each listed key over that one read" through `resolve_read`, and `resolve(key, repo, rev)` "keeps
  its signature ... by calling the two in turn".
- `TOOL-dGroundRules-3` §4: `resolve` returns "the first `Resolution` a step returns" from
  `RESOLUTION_ORDER`.
- `TOOL-dGroundRules-10` S5: rule 7 reads the limit with `readPolicy("runtime.agents-in-flight",
  { repo })`, which takes a fresh mirror's value.

### The order after this unit

```python
def resolve_read(path, row, read):
    hit = <RESOLUTION_ORDER over read's table, or the invalid branch>   # units 3 and 4, unchanged
    if path == ("runtime", "agents-in-flight"):
        hit = derive_lowered_limit(hit, read)                          # this unit
    return hit
```

`derive_lowered_limit` calls `read_legacy_fanout(repo, read.sha)` once per read, caches the
answer on the read, and returns `hit` with the smaller value and the reason
`TOOL-dGroundRules-10` S1 states. A malformed conf raises that unit's `Refusal`, so the render
refuses as `get` does.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_lowered_limit` | py.function | `tools/policy/policy.py` |
| `limit-conf-mirror`, `limit-conf-last-valid` | `CASES` entries | `tools/policy/check_policy.py` |

`derive_lowered_limit` leads with `derive`, a verb `.lexicon.conf` declares: `lexicon.py --suggest`
answered OK for it under `py.function` on 2026-10-23.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `.governance/policy.json`

### Alternatives rejected

- **A step in `RESOLUTION_ORDER`.** Steps answer first-wins from the file, a preset or the default;
  a lowering must see the answer, so a step would duplicate the order inside itself (§8 F1).
- **Lowering in `render_mirror` too.** A second home for one rule, the defect this unit removes.

## 5. Production-readiness checklist

- security — the limit every reader sees is the lowered one, so rule 7 refuses settings above the
  conf's lowering, which the clause's lowering-only home requires.
- perf / scale — one conf read per revision read, cached; the render's 270 resolutions read it once.
- error / empty / loading states — an absent conf lowers nothing; a malformed one refuses every
  reader, the render included.
- observability — `--explain` from either reader names the conf line that lowered the limit.
- risks — a later reader that bypasses `resolve_read` would miss the lowering; S1 states the one
  home and `limit-conf-mirror` reds a mirror that misses it.
- testing — the two cases under `--fixture`, with AC1 to AC4.
- migration — `.governance/policy.json` is re-rendered in this unit's commit; gov's conf sets no
  `FANOUT_CAP` below the key, so no value moves.
- user docs — N/A: `help/agent-limit.md` already states what a conf lowering does
  (`TOOL-dGroundRules-10` §5).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`policy.py`, `policy-mirror.js` and `check_policy.py`, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `grep -n "read_legacy_fanout(" policy.py` runs on the built tree, it prints the
  definition and exactly one call, inside `derive_lowered_limit`, and
  `grep -n "derive_lowered_limit(" policy.py` prints the definition and one call, inside
  `resolve_read`.
  Red when: the lowering is also applied in `resolve`, or only there.
- **AC2** — When `python check_policy.py --fixture limit-conf-mirror` runs, which commits
  `FANOUT_CAP=2` in `.agent-cap.conf` with no policy value and renders the mirror, both
  `python policy.py get runtime.agents-in-flight` and
  `node policy-mirror.js get runtime.agents-in-flight` print `2`.
  Red when: the mirror holds the catalogue default while `get` prints `2`.
- **AC3** — When `python check_policy.py --fixture limit-conf-last-valid` runs, which commits a
  valid policy file setting the limit to 6, then `FANOUT_CAP=3`, then a malformed policy file,
  `policy.py get runtime.agents-in-flight --explain` prints `3` with source `last-valid` and a
  reason naming `.agent-cap.conf`.
  Red when: the `last-valid` branch returns the unlowered 6.
- **AC4** — When `python policy.py settings --check` runs over a scratch copy whose conf sets
  `FANOUT_CAP=2`, after `settings --write`, both `env` keys hold `"2"`.
  Red when: the settings render reads a limit the lowering never reached.
  fixture: the scratch copy is made under the run's temp directory; the tree holds none today.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture limit-conf-mirror limit-conf-last-valid`) · covers AC2 AC3 · the lowering staged back into the `resolve` wrapper, so the mirror and the `last-valid` branch read 6 · none

## 8. Open questions

- **F1 — Where does the lowering live?** (a) At the end of `resolve_read`, after the order and the
  invalid branch. (b) A post-step tuple beside `RESOLUTION_ORDER`, of which the lowering is the one
  member. (c) A step inside `RESOLUTION_ORDER`. (c) cannot see the order's answer, so it fails AC2
  as a first-wins step (veto 1). (a) and (b) meet every criterion; (b) is a tuple for one member,
  which the charter's `[yagni]` rule refuses until a second lowering exists. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 2 (HIGH, item H1) of the round-1 spec
  audit, from the review's sound fix and specs 3, 5 and 10 read at their audited revisions.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-25`, the reciprocal of each
  promotion of the round-1 spec audit of units 13 to 21 that repairs this unit; no scope moved.
- rev-3 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.

## 10. Reuse audit

The seam extended is `resolve_read`, `TOOL-dGroundRules-5`'s one composition of the resolution order
and the invalid branch, which already serves `get`, the render and the settings render.
`python tools/codebase-map/reuse_lookup.py "apply a legacy conf lowering after the resolution order
to every reader"` ranked name stems only (`read`, `read_text`, `load_conf`, `parse_conf`), none of
which composes a resolution, so no further seam fits; `read_legacy_fanout` itself is
`TOOL-dGroundRules-10`'s and is reused, not copied. The recall probe returned the spec brief's unit 10
row and this build's review, which agree with the specs read; `TOOL-aDeclaredBound-4` concerns a
declared bound elsewhere and does not bear on the home.

Recall terms used: `python tools/memory-recall/query.py "how does a legacy conf lowering reach every
reader of a policy key" --terms "agent-cap conf FANOUT_CAP lowering legacy home resolution order
mirror resolve_read"`
