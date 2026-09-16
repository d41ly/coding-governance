# TOOL-dDerivedDocket-37 — a hands-off's payload tokens are named by the sibling it names

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 39

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-16-review-TOOL-dDerivedDocket-37-spec-audit-g6-round1.md](../reviews/2026-09-16-review-TOOL-dDerivedDocket-37-spec-audit-g6-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

A `**hands-off**` bullet in a spec's `### Edges` block promises a named sibling something, and the
promise is usually a backticked token: a flag, a key, a file, a placeholder. Nothing checks that the
sibling names it. This build's round-1 spec audits found that class by hand in two topic groups: the
placeholder the migration planner handed the switch-over unit, which the switch-over unit never named.
The fold fixed that instance. A probe run after the fold over this build's 37 live specs graded 131
hands-off payload tokens and found three more. Unit 7 handed unit 11 a verb whose comparison is unit
34's. Unit 13 handed unit 35 a helper by a filename unit 35 never used. Unit 10 handed the adopter
runbook a leg its own §8 F4 said an adopter adds, and the runbook never said so. The orchestrator
fixed all three before this spec was written.

Each of those is a join over two tracked files, the shape `tools/check-spec-tokens.py` already
exists to run. This unit adds it there as a fourth population, so a later spec set gets the answer
from the bar rather than from a review round. It was adopted under the unattended protocol's section
11: it makes a leg this repo already runs red where it should, measured by the three hits above;
nothing measured gets worse; and it trips no veto, because the checker is gov-internal and exempt from
shipping in `tools/govkit/registry.toml`.

## 2. Scope (IN)

- **S1** — the hands-off population. `tools/check-spec-tokens.py` reads the `### Edges` sub-head
  inside §3 of every LIVE spec whose filename date is on or after `SPEC_HANDOFF_CUTOFF`, whatever its
  tier. For each bullet opening `- **hands-off** ` followed by a backticked unit id, with its
  two-space continuation lines, it grades every further backticked token in the bullet. A graded
  token must occur verbatim in the text of the named sibling's spec. Unit ids, and tokens matching
  the checker's existing `NOT_A_TOKEN` shape, are not graded. A miss is a hit of kind `handoff`
  naming the source file, the target id and the token. Observed by AC1 and AC2.
- **S2** — silence, counted. A bullet whose target id names no LIVE spec in the source's own build
  folder is not graded: either the target is terminal and frozen, or the id has no spec there. A
  bullet naming `external` carries no backticked id and is not read. Each silent bullet is counted,
  and the report prints the count. Observed by AC3.
- **S3** — the dated demand. `SPEC_HANDOFF_CUTOFF="2026-09-14"` in `.memory-tree.conf`, with a header
  comment in the idiom of `SPEC_LEGLINE_CUTOFF`: what the arm grades, why it exists as measured here,
  why this date, and that blank means off. Blank or absent turns the arm off, and the report says
  `SPEC_HANDOFF_CUTOFF blank (arm off)`. Observed by AC4 and AC6.
- **S4** — the report line. Every run prints
  `spec-tokens: <b> hands-off bullet(s) graded · <t> payload token(s) · <s> silent (target not a live spec in the build) · SPEC_HANDOFF_CUTOFF <date>`,
  so a green run over zero bullets cannot pass for a graded one. Observed by AC1, AC3 and AC6.
- **S5** — the waiver key. A `handoff` hit is waived only by a row whose token cell is
  `<source id>><target id>:<token>`. The existing stale-waiver and missing-reason refusals apply
  unchanged. Observed by AC5.
- **S6** — the real-tree pass. At this unit's pass, `python tools/check-spec-tokens.py --list` runs
  once over the tree as an authoring aid. It is not a gate leg run. A hit in a live spec of this build
  is fixed in that spec, with a rev line, in this unit's commit. A hit in another build's live spec
  is that build's writer's to fix, so it takes a waiver row naming the build, and the stale-waiver
  refusal retires the row when the spec is fixed. Observed by AC6.
- **S7** — the carriers. The checker's header docstring gains the fourth population and its limits,
  and the `memory/map/features/spec-tokens.md` dossier refreshes its title and prose on touch. The
  kickoff manifest's `last-audit` is re-stamped in this unit's commit with a delta line in the
  commit message, because `.memory-tree.conf` is in its `watch:` list. Observed by AC8.
- **S8** — the self-test arms and their floor. `tools/check-spec-tokens.test.sh` gains the arms §7
  lists, and `FLOOR_ASSERTIONS` rises by the number of arms added. Observed by AC7.
- **S9** — the version. NOT OBSERVED by a criterion here: `KIT_SPEC_TOKENS_VERSION` does not move.
  The file ships to no adopter, and the leg-line arm TOOL-aJoinedCanon-7 added was added at the same
  version, so no reader of the constant sees a change.

## 3. Non-goals (OUT)

- **Consumes-from bullets.** Measured over this build, grading them exactly produced twelve misses
  and no true one. Eight were an argument or placeholder variant of a command the producer does
  name, and four were a consumer naming its own file (`.retry`, `AGENTS.md`) or a third unit's key as
  context. Reciprocity (check 12) already forces every consumes-from edge to have a hands-off at
  the producer, and this arm grades that one. See §8 F2.
- **Scope agreement.** The join proves the sibling NAMES the token. It does not prove the sibling
  does the work the bullet describes. A sibling that mentions the token only in passing passes.
- **The other left-shift candidates the fold plans listed**, among them a join per kit constant, a
  §1-closes-to-AC join, an S-item citation on each edge bullet, and a first-commit dating lint. The
  S-item citation proxy was measured at 101 unmatched bullets of 214, mostly correct prose, and the
  others have no decidable shape in the current spec text. They stay review classes.
- **The hygiene engine.** Check 12's edge arms are untouched; see §4 Alternatives rejected.

### Edges

none

## 4. Design

### The selection

```
for each tracked memory/builds/<b>/spec/<date>-spec-<id>.md that is LIVE:
    skip unless <date> >= SPEC_HANDOFF_CUTOFF (blank: arm off, nothing graded)
    edges = the text under "### Edges" inside §3, up to the next "### " or "## "
    for each bullet matching ^- \*\*hands-off\*\* `<target>` with its "  " continuation lines:
        target spec = memory/builds/<b>/spec/*-spec-<target>.md, LIVE, else silent += 1
        for each backticked token after the first:
            skip an id-shaped token, or one NOT_A_TOKEN matches
            tokens += 1
            if the token is not a substring of the target spec's text: hit(handoff)
```

The bullet shape is the one check 12's SHAPE arm accepts: the verb, then a backticked id. The
continuation rule is the one this file already uses for section 6 bullets
(`tools/check-spec-tokens.py:237`). The target is read whole, because a sibling may name the token in
its scope, its design or its edges, and any of those counts as naming it.

### The hit and its waiver

A `handoff` hit's key is `<source id>><target id>:<token>`, and that is the string a waiver row
matches (`tools/check-spec-tokens.py:254` keys on the hit's third field). A token waived for one
edge is therefore not waived for another. A bare token key would waive the token in every bullet of
every build, which is the stale-exception problem the registry refuses elsewhere.

### The report

The existing two report lines (`tools/check-spec-tokens.py:270` and `:279`) are unchanged. S4's line
is printed third, whether or not the arm is on.

### Inventory

One function, `grade_handoffs`, in the `py.function` cell, leading with a declared verb, and one
constant, `HANDOFF_KEY`. No new leg and no new file.

### Files touched (estimate)

`tools/check-spec-tokens.py`, `tools/check-spec-tokens.test.sh`, `.memory-tree.conf`,
`memory/guides/SESSION-KICKOFF.md`, `memory/map/features/spec-tokens.md`, and
`memory/project/spec-token-waivers.txt` only if S6 finds a foreign hit.

### Alternatives rejected

- **An arm in check 12.** The hygiene engine already parses the Edges bullets with their prose, so
  the edge parser would be reused rather than copied. But the engine is a copy-installed kit, so the
  arm would reach every memory-tree adopter's bar on upgrade. That is a shipped surface this unit
  did not price (M3 veto 3), for a population gov has only measured in its own tree.
- **A parts rule** that passes a token when each whitespace-separated part of it occurs, placeholders
  dropped. It was built for `--attribute <BASE>` against `--attribute <R>`. Measured, all such cases
  sit in consumes-from bullets, and over hands-off bullets it matched nothing, so it is taste and is
  left out.

## 5. Production-readiness checklist

- **security** — read-only over tracked files. No write, no subprocess beyond the `git ls-files`
  call the checker already makes.
- **perf / scale** — one extra read per graded target, over at most the live specs. The leg's
  declared ceiling is 60 s, and the whole checker runs in seconds at this corpus size.
- **error / empty / loading states** — an Edges block with no hands-off bullet grades nothing and
  counts nothing. A blank key prints the arm-off line. A target file that fails to decode is read
  with replacement, as every spec read in this file already is.
- **observability** — S4's line on every run, and `--list` printing each hit with its key.
- **risks** — a straggler branch from another node could merge a spec dated on or after the cutoff
  whose hands-off disagrees with its sibling. That reds the bar at the merge, which is the join
  working. The merging session fixes the bullet or waives the edge.
- **testing** — the arms §7 lists, in `tools/check-spec-tokens.test.sh`, each break staged and
  observed red at the build's post-build bar. The suite's selftest budget row (130 s) is re-declared
  with its reading if the new arms push the leg past it.
- **migration** — none. A spec dated before the cutoff is never graded.
- **user docs** — the checker's docstring and the dossier; the key's own header comment.

## 6. Acceptance criteria

- **AC1** — When a scratch build holds two live specs dated at the cutoff, and the first's
  hands-off bullet to the second names `` `--frob` `` which the second never names,
  `python tools/check-spec-tokens.py` exits 1 and prints `[handoff]` with the source file and the key
  `EXMP-tOne-1>EXMP-tOne-2:--frob`. With `--frob` added to the second spec, it exits 0 and S4's line
  counts one bullet and one token. The arms are in `tools/check-spec-tokens.test.sh`.
  Red when: the join grades the target id itself, or searches the source instead of the target, and
  the missing token passes.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC2** — When the missing token sits on the bullet's two-space continuation line,
  `python tools/check-spec-tokens.py` exits 1 with the same `[handoff]` key.
  Red when: only the bullet's first line is read, so a payload wrapped past column 100 is never
  graded.
- **AC3** — When the hands-off target is a CLOSED sibling, or an id with no spec in the build, the
  checker exits 0 over a token that sibling does not name, and S4's line reports `1 silent`, in
  `tools/check-spec-tokens.test.sh`.
  Red when: absence reds as disagreement, so a hand-off to a finished unit fails a spec nobody may
  edit; or the skip is uncounted, so a silent run reads as a graded one.
- **AC4** — When `SPEC_HANDOFF_CUTOFF` is blank in the scratch repo's `.memory-tree.conf`, a missing
  token exits 0 and the report prints `SPEC_HANDOFF_CUTOFF blank (arm off)`. When the source spec's
  date is before a set cutoff, the same bullet is not graded and the bullet count is 0.
  Red when: the key is ignored, so every dated spec in the corpus is graded on landing day; or a
  blank key grades anyway, so the arm cannot be turned off.
- **AC5** — When `memory/project/spec-token-waivers.txt` in the scratch repo holds
  `EXMP-tOne-1>EXMP-tOne-2:--frob` with a reason, the AC1 fixture exits 0. When the second spec then
  names `--frob`, the checker exits 1 printing `STALE WAIVER`. A third spec's bullet to the second,
  naming `--frob` unnamed, still exits 1.
  Red when: the waiver matches on the token alone, so one row silences the token in every edge.
- **AC6** — When `python tools/check-spec-tokens.py` runs on this unit's commit, it exits 0, and its
  third report line names `SPEC_HANDOFF_CUTOFF 2026-09-14`. The ledger records the `--list` output
  S6 took, with its bullet and token counts.
  Red when: the key is misspelled or blank, so the arm is off over the corpus that motivated it; or a
  live hit remains unfixed and unwaived.
  figure: the counts are DERIVED at observation time, since specs close as the build proceeds.
- **AC7** — When `bash tools/check-testsuite-counts.sh` runs over the post-build tree, it reports the
  spec-tokens suite's printed count at or above its `FLOOR_ASSERTIONS` pin in
  `tools/check-spec-tokens.test.sh`, and that pin equals the arm count before this unit plus the arms
  it adds.
  Red when: arms land without raising the pin, so a later deletion of this unit's arms passes.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs on this unit's commit, check 5
  passes with the re-stamped `last-audit`, and `memory/map/features/spec-tokens.md` names four joins.
  Red when: `.memory-tree.conf` moves with no re-stamp, or the dossier still describes three joins,
  which the map's freshness leg would not catch because it grades claims rather than prose.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `testsuite counts (every bar self-test prints one)` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · a hands-off token its target never names · none
New arm: tools/check-spec-tokens.test.sh · the token on a continuation line · none
New arm: tools/check-spec-tokens.test.sh · a hands-off to a CLOSED sibling and to an unspecced id · none
New arm: tools/check-spec-tokens.test.sh · a blank key, and a source dated before the cutoff · none
New arm: tools/check-spec-tokens.test.sh · a waiver keyed on one edge, then stale, then not reaching another edge · none

## 8. Open questions

- **F1** — Which targets are graded? Options: (a) Tier-2 targets only, as check 12's joins do;
  (b) any live sibling, whatever its tier. Check 12 is silent on a Tier-1 target because a Tier-1
  spec owes no Edges block, so it cannot owe a reciprocal bullet. This join demands only that the
  target's text names the token, which a Tier-1 spec can do. Measured, one of the three hits had a
  Tier-1 target: the adopter runbook. RESOLVED (agent, 2026-09-14, delegated): (b), the most
  feature-rich survivor, with no veto tripped.
- **F2** — Which verbs are graded? Options: (a) hands-off only; (b) both verbs. Measured over this
  build before the orchestrator's fixes: 15 misses across both verbs. The twelve false ones were all
  consumes-from tokens, and the three true ones were all hands-off. RESOLVED
  (agent, 2026-09-14, delegated): (a). With both verbs, the leg reds correct specs, and check 12's
  reciprocity already routes every consumes-from edge to a graded hands-off.
- **F3** — Which cutoff? Options: (a) 2026-09-14, this spec set's date; (b) 2026-09-08,
  `SPEC_EDGES_CUTOFF`'s date. Measured, both select the same 107 bullets today, because no other
  live spec carries a hands-off bullet. (b) would also reach a straggler spec dated 2026-09-08 to
  2026-09-13 on another node's branch, which this build never measured. RESOLVED (agent, 2026-09-14,
  delegated): (a). The coverage is equal on every spec this repo holds, and its reach into branches
  nobody measured is smaller.

## 9. Revision log

- rev-1 · 2026-09-14 · adopted after the round-1 fold under protocol section 11, from fold plans
  c1 A1 to A6, c2's three, c3's optional, c4 A2 to A4 and c5 A3. Only the hands-off payload join was
  measured decidable. The rest are named in §3. Recorded with `--rescope --act add`.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "join a spec's hands-off edge payload
  tokens against the sibling spec that receives them"` returned symbol-name neighbours only
  (`build_edges` in `tools/process-monitor/scope.py`, `join_aliases`, `parse_tokens`) and no seam in
  the spec-tokens feature. The seam was found by reading source instead: this unit extends
  `tools/check-spec-tokens.py`, reusing its LIVE selection, `TICK`, `NOT_A_TOKEN`, the section-6
  bullet shape, the conf-key reader `read_conf_key` and the waiver registry.
- **Against BASE.** `tools/check-spec-tokens.py` and its test are unchanged from BASE to this spec's
  commit. The cited lines hold at BASE: `:237` is the section-6 bullet regex, `:254` keys a waiver on
  the hit's third field, and `:270` and `:279` are the two report lines.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: `python tools/memory-recall/query.py "how are spec edges between sibling units
  checked for agreement" --terms "hands-off consumes-from Edges reciprocity sibling spec join payload
  token check-spec-tokens SPEC_EDGES_CUTOFF edge"`. Top hits: `.memory-tree.conf:268`
  (`SPEC_EDGES_CUTOFF`'s header, whose payload arm is check 12's `external` test and not this join),
  TOOL-aKeyedAnnotation-9 (the paths arm's open defect, untouched here), `memory/HYGIENE.md:135`,
  the aLeakedHandle round-2 review's edge-bullet checklist item, and this build's G4 round-1 record.
