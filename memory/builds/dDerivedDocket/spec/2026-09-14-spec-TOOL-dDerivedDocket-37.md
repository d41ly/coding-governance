# TOOL-dDerivedDocket-37 — a hands-off's payload tokens are named by the sibling it names

**Status:** CLOSED · rev-5 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dDerivedDocket-37-1-acceptance-ledger.md](../build/2026-09-21-build-TOOL-dDerivedDocket-37-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-16-review-TOOL-dDerivedDocket-37-spec-audit-g6-round1.md](../reviews/2026-09-16-review-TOOL-dDerivedDocket-37-spec-audit-g6-round1.md) | spec-audit | — |
| [2026-09-20-review-TOOL-dDerivedDocket-37-spec-audit-g6-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-37-spec-audit-g6-round2.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

A `**hands-off**` bullet in a spec's `### Edges` block promises a named sibling something, and the
promise is usually a backticked token: a flag, a key, a file, a placeholder. Nothing checks that the
sibling names it. This build's round-1 spec audits found that class by hand in two topic groups: the
placeholder the migration planner handed the switch-over unit, which the switch-over unit never named.
The fold fixed that instance. A probe run after the fold found three more. Unit 7 handed unit 11 a
verb whose comparison is unit 34's. Unit 13 handed unit 35 a helper by a filename unit 35 never used.
Unit 10 handed the adopter runbook a leg its own §8 F4 said an adopter adds, and the runbook never
said so. The orchestrator fixed all three before this spec was written. The tree that probe read was
never committed, so its token count cannot be re-derived and is not repeated here. With this spec's
rev-2 selection at `282e0a6b`, after the fixes, the build's live specs carry 107 hands-off bullets
and 128 payload tokens, and no token misses.

Each of those is a join over two tracked files, the shape `tools/check-spec-tokens.py` already
exists to run. This unit adds it there as a fifth join over a fourth population, since the `bar`
join TOOL-aDeferredBar-2 added reads two existing populations rather than minting one. A later spec
set then gets the answer from the bar rather than from a review round, and so does every later pass
of this build, through the run of the checker the orchestrator makes after each unit commit and the
run `--dispatch` makes before each pass (§4 Rollout). It was adopted
under the unattended protocol's section 11. It makes a leg
this repo already runs red where it should, measured by the three hits above. Nothing measured gets
worse, which holds only while its function names lead with a declared verb (§4 Inventory) and its
new arms stay inside the self-test leg's declared ceiling and budget (§5 testing). It
trips no veto: the checker is gov-internal and exempt from shipping in `tools/govkit/registry.toml`,
and its conf key stays out of the shipped example (§8 F5).

## 2. Scope (IN)

- **S1** — the hands-off population, in check 12's own grammar. `tools/check-spec-tokens.py` maps
  every LIVE tracked spec under `memory/builds/<b>/spec/`, at any depth, from the uid its H1 line
  carries to its file, per build. It reads the `### Edges` sub-head inside the Non-goals section,
  found by heading text, of every LIVE spec whose filename date is on or after
  `SPEC_HANDOFF_CUTOFF`, whatever its tier. A bullet is any line check 12 accepts as a hands-off
  edge: a `-` or `*` marker, spaces or tabs, `**hands-off**`, then a backticked or bare target uid.
  Its two-space continuation lines belong to it. Every backticked token in the bullet other than a
  backticked target is graded, and must occur verbatim in the text of the target uid's live spec.
  Unit ids, and tokens matching the checker's existing `NOT_A_TOKEN` shape, are not graded. A miss
  is a hit of kind `handoff` naming the source file and S5's key. Observed by AC1, AC2 and AC9.
- **S2** — silence, counted. A bullet is not graded when its target uid names no LIVE spec in the
  source's own build folder, because the target is terminal and frozen, or no spec there carries
  that uid in its H1. A source spec whose H1 carries no uid has no key to report a hit under, so its
  bullets are not graded either. Each such bullet is counted, and the report prints the count. A
  bullet naming `external` has no sibling to join and is not read. Observed by AC3.
- **S3** — the dated demand. `SPEC_HANDOFF_CUTOFF="2026-09-22"` is appended at the end of
  `.memory-tree.conf`, with a header comment in the idiom of `SPEC_LEGLINE_CUTOFF`: what the arm
  grades, why it exists as measured here, why this date, and that blank means off.
  THE DATE IS DERIVED, NEVER CHOSEN, and the why-this-date slot of that idiom is the derivation.
  The owner ratified one relation over every cutoff key this register introduces at
  `TOOL-aJoinedCanon-1` section 8 F1, recorded on the `REV_SCOPE_CUTOFF` row at
  `.memory-tree.conf:131` and spelled out with both clauses and its three reading commands on the
  `SPEC_DIRECT_CUTOFF` row at `.memory-tree.conf:252`: the value is the day AFTER the later of
  (a) the newest spec filename date on ANY ref or live worktree and (b) the setting commit's own
  date. The reading taken AT THE BUILD COMMIT, 2026-09-21 on node `d`, over every local and remote
  ref and every worktree `git worktree list` names: (a) 2026-09-20, (b) 2026-09-21, the later is
  2026-09-21, and the relation returns 2026-09-22. It superseded the rev-4 reading of the day
  before, which returned 2026-09-21 and would have EQUALLED the setting commit's own day rather
  than sitting past it — the second clause, and the reason this key is re-derived rather than
  carried. It is RE-DERIVED at the build commit and again at landing, never
  carried, because the relation is to the fleet working day and a value carried across a day
  boundary is stale by construction — `tools/check-spec-tokens.py:47` states that as this file's
  own rule for every cutoff key it reads, and `REV_SCOPE_CUTOFF` moved twice for it.
  THREE PLACES CARRY THE LITERAL and must move together, so the re-derivation has a checklist rather
  than a memory: this paragraph, both where the key is spelled above and where its reading is
  recorded; AC6's report line; and §8 F3's resolution. No gate joins them — nothing reds if one
  moves and the others do not — so re-running the relation means editing all three in one commit or
  none. A grep for the value also hits section 9, which spells it inside dated records of readings
  already taken; those are append-only history and do NOT move with a re-derivation, so the
  checklist is three and not every occurrence. The fixtures deliberately carry no literal: AC1's
  and AC9's specs are dated AT the scratch repo's own key, whatever it holds.
  THE COST, stated rather than discovered: the arm grades ZERO bullets on landing day, since every
  spec of this build is dated 2026-09-14, so the self-test fixtures are its whole coverage until a
  spec is written on or after the key's date. That is the state `SPEC_LEGLINE_CUTOFF`,
  `SPEC_DIRECT_CUTOFF` and `REV_SCOPE_CUTOFF` each shipped in, each of those rows states it, and
  S4's report line makes it visible rather than silent. Section 8 F3 records the relation, the
  register rows and the one counter-precedent weighed against them. Blank or absent
  turns the arm off, and the report says `SPEC_HANDOFF_CUTOFF blank (arm off)`. The key is read
  through `read_cutoff_key`, so a set value that is not an ISO date refuses before grading, the rule
  the checker's header states for every cutoff key it reads. The key goes in
  gov's conf only, never in `tools/memory-tree/.memory-tree.conf.example`, per §8 F5. It is appended
  rather than placed beside its sibling, so this unit moves no conf line a sibling spec cites, such
  as `ROTATION_MODE` at `.memory-tree.conf:429`, which unit 12 cites three times. Observed by AC4
  and AC6.
- **S4** — the report line. Every run prints
  `spec-tokens: hands-off join · <b> bullet(s) graded in live spec(s) · <t> payload token(s) · <s> silent (no live target in the build, or no source uid) · SPEC_HANDOFF_CUTOFF <date>`,
  so a green run over zero bullets cannot pass for a graded one. Its `live spec(s) ·` is the text
  by which `--dispatch`'s refusal drops a report line from its diagnosis (§8 F9). Observed by AC1,
  AC3 and AC6.
- **S5** — the waiver key. A `handoff` hit's key is `<source uid>><target uid>:<token>`, where each
  uid is the one its spec's H1 carries, never one read from a filename. A hit is waived only by a row
  whose token cell is that key. The existing stale-waiver and missing-reason refusals apply
  unchanged. Observed by AC5 and AC9.
- **S6** — the real-tree pass. This unit's pass runs no hand-run checker, by the owner rule the
  build brief states. After this unit's commit, at `order 6` once units 1 to 5 have closed, the
  orchestrator runs `python tools/check-spec-tokens.py --list` once over the tree, and its report
  line must name the key and its date rather than the arm-off line. The graded bullet count is
  whatever the corpus holds and is ZERO on landing day, because the relation-derived key (S3)
  postdates every spec of this build; an above-zero count was the retroactive date's property and
  went with it (section 8 F3). It is not a gate leg run. A hit in a live spec of this build is
  fixed in that spec, at the source bullet or in the target's text, with a rev line naming this join,
  in a commit the orchestrator makes before the next unit's pass. A hit in another build's live spec
  is that build's writer's to fix, and none exists today (§8 F3). Neither kind takes a waiver row
  unless the same commit retires another row: `memory/project/spec-token-waivers.txt` is shrink-only
  by its own header, and `TOOL-aKeyedAnnotation-9` records that absorbing a class there is not
  available. A foreign hit with no row to retire is parked, naming the hit, and this unit parks with
  it, because AC6 cannot pass over a live hit. Observed by AC6.
- **S7** — the carriers. The checker's header docstring gains the fifth join, its population and
  its limits.
  The join proves a sibling names a token, never that it does the work. Consumes-from bullets are not
  graded, so a consumes-from payload is graded only through a hands-off check 12 forces at the
  producer and this join reads. Neither check grades a Tier-1 consumer's edges, an edge from a
  consumer dated before `SPEC_EDGES_CUTOFF`, or an edge naming a Tier-1 producer or one dated before
  `SPEC_HANDOFF_CUTOFF`. An `external` bullet has no sibling to join. The
  `memory/map/features/spec-tokens.md` dossier refreshes its title and prose on touch. The kickoff
  manifest's `last-audit` is re-stamped in this unit's commit with a delta line in the commit
  message, because `.memory-tree.conf` is in its `watch:` list. That re-stamp is NOT a trim and
  claims nothing from the manifest's headroom: rewriting the `last-audit:` line at
  `memory/guides/SESSION-KICKOFF.md:5` is the bookkeeping every unit touching a watched file
  owes, a timestamp and a sha replaced in place by a timestamp and a sha. Another unit of this
  build rewrites the same line for the same reason, and that is NOT a collision. This unit
  writes no other byte of that file, so it displaces nothing and funds nothing, and AC11 reads
  the carrier only to catch a stamp written as an added line. Observed by AC8 and AC11.
- **S8** — the self-test arms and their floor. `tools/check-spec-tokens.test.sh` gains thirteen
  `arm` calls spread over §7's six `New arm:` rows in the distribution AC7 states, and
  `FLOOR_ASSERTIONS` moves from 42 to 55. Observed by AC7 and AC10.
- **S9** — the version. NOT OBSERVED by a criterion here: `KIT_SPEC_TOKENS_VERSION` does not move.
  The file ships to no adopter, `tools/check-kit-versions.sh` names no carrier for it, and the
  leg-line arm TOOL-aJoinedCanon-7 added and the `bar` join TOOL-aDeferredBar-2 added were each
  added at the same version, so no reader of the constant sees a change.

## 3. Non-goals (OUT)

- **Consumes-from bullets.** Measured over this build, grading them exactly produced twelve misses
  and no true one. Eight were an argument or placeholder variant of a command the producer does
  name, and four were a consumer naming its own file (`.retry`, `AGENTS.md`) or a third unit's key as
  context. Between two Tier-2 specs dated on or after `SPEC_EDGES_CUTOFF`, check 12's reciprocity
  forces every consumes-from edge to have a hands-off at the producer, and this arm grades that one
  when the producer is dated on or after `SPEC_HANDOFF_CUTOFF`. Outside that population it forces
  nothing: a Tier-1 spec is skipped before the edge arm
  (`tools/memory-tree/check-memory-hygiene.sh:1517`), and a target outside the registered population
  is skipped by the join (`tools/memory-tree/check-memory-hygiene.sh:1790`). S7 names that
  remainder. See §8 F2.
- **Scope agreement.** The join proves the sibling NAMES the token. It does not prove the sibling
  does the work the bullet describes. A sibling that mentions the token only in passing passes.
- **The other left-shift candidates the fold plans listed**, among them a join per kit constant, a
  §1-closes-to-AC join, an S-item citation on each edge bullet, and a first-commit dating lint. The
  S-item citation proxy was measured at 101 unmatched bullets of 214, mostly correct prose, and the
  others have no decidable shape in the current spec text. They stay review classes.
- **A high-water gate on the waiver registry.** The registry's shrink-only rule is a header comment
  nothing enforces. Comparing its row count with a pinned high-water would grade every population
  the checker reads, a second mechanism in one spec, so it stays a candidate for its own unit.
- **The shipped example conf.** `SPEC_HANDOFF_CUTOFF` is not declared in the memory-tree kit's
  example conf. See §8 F5 and the external edge below.
- **The hygiene engine.** Check 12's edge arms are untouched; see §4 Alternatives rejected.

### Edges

- **hands-off** external — `TOOL-aJoinedCanon-13` widens the example-parity derivation to every tool
  that reads `.memory-tree.conf`, so it meets `SPEC_HANDOFF_CUTOFF`, which §8 F5 keeps out of the
  shipped example. When that row lands, it either exempts a key whose only reader the shipping
  registry exempts, or declares this key blank in the example.

## 4. Design

### The selection

```
uids: for each tracked memory/builds/<b>/spec/.../*.md that is LIVE, at any depth:
    (b, the uid of its first "# <UID> " line) -> that file; one uid may map to several files
for each tracked memory/builds/<b>/spec/.../<date>-spec-*.md that is LIVE:
    skip unless <date> >= SPEC_HANDOFF_CUTOFF (blank: arm off, nothing graded;
                                               not an ISO date: refused before grading)
    edges = the text under "### Edges" inside the "## <n>. Non-goals" section, found by heading
            text, up to the next "### " or "## "
    for each line matching ^(-|\*)[ \t]+\*\*hands-off\*\*[ \t], with its "  " continuation lines:
        target = the first backticked token when the payload opens with one,
                 else the leading [A-Za-z0-9_-] run
        skip the bullet when target is "external"
        source = the uid of this spec's first "# <UID> " line
        if source is empty, or (b, target) is not in uids: silent += 1, next bullet
        bullets += 1
        text = every file uids maps (b, target) to, joined
        for each backticked token in the bullet other than the target:
            skip an id-shaped token, or one NOT_A_TOKEN matches
            tokens += 1
            if the token is not a substring of text: hit(handoff, key source>target:token)
```

Every shape above is check 12's, cited so a reader can compare them line for line. The uid is read
at `tools/memory-tree/check-memory-hygiene.sh:1533-1534`. Non-goals and Edges are found by heading
text at `:1547` and `:1549`. The marker is `:1553`, the verb `:1557`, and the backticked-or-bare
target `:1564-1565`. Check 12 selects specs at any depth (`:1153`) and registers each one it grades
(`:1588`). This map reads any depth too, through the checker's own population regex at
`tools/check-spec-tokens.py:258`.

One rule is wider than check 12's. Check 12 reads a bullet's first line only, and this join reads
its two-space continuation lines too, the rule this file already uses for acceptance-criteria
bullets (`tools/check-spec-tokens.py:370`). The target is read whole, because a sibling may name the
token in its scope, its design or its edges, and any of those counts as naming it. Measured
2026-09-16 at `7804eb7f`, 624 tracked specs carry an H1 uid each and no two files in a build share
one, and again at `94fd2f54`, 649 of 649 with no shared uid, so the several-files rule has no
instance today.

### The hit and its waiver

A `handoff` hit's key is `<source uid>><target uid>:<token>`, both uids read from H1 lines, and
that is the string a waiver row matches (`tools/check-spec-tokens.py:405` keys on the hit's third
field). A token waived for one edge is therefore not waived for another. A bare token key would
waive the token in every bullet of every build, which is the stale-exception problem the registry
refuses elsewhere. The registry is shrink-only by its header, so S6's offset rule governs when a row
may be added at all.

### The report

The existing three report lines (`tools/check-spec-tokens.py:423`, the `bar` join's at `:430` or
`:434`, and `:442`) are unchanged. S4's line is printed fourth, whether or not the arm is on. The
hands-off tokens join neither population the `bar` join reads (`pop_toks`, `:329`), so its examined
count and its `NEAR` lines do not move.

### Inventory

Two functions in the `py.function` cell, each leading with a verb `.lexicon.conf` declares. On
2026-09-16, `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for both.

| Identifier | Cell | Verb, and why |
|---|---|---|
| `scan_handoffs` | `py.function` | `scan`: it walks the live population looking for misses |
| `read_spec_uids` | `py.function` | `read`: it pulls each spec's H1 uid from the tracked files |
| `HANDOFF_KEY`, `HANDOFF_BULLET`, `NONGOALS_HEAD`, `SPEC_UID`, `UNIT_ID` | `py.constant` | no cell row declares it, so no naming arm grades these |

`grade`, the rev-1 verb, is not in the declared table. A definition leading with it adds one P1 verb
offender, and `VERB_OFFENDER_PIN` is a two-sided equality, so `lexicon naming predicates` would red.
A fixture helper the suite gains leads with a declared verb in `sh.function`, as `write_handoff_spec`
would. No new leg and no new file.

### Rollout

**Order 6, sharing the step with unit 6** (§8 F4). Units 1 to 5 are built first by owner ruling
D12-i11, so step 6 is the earliest that ruling leaves, and every order from 6 to 38 is taken. A
shared value declares a parallel group, and M6 in `memory/guides/BUILD-METHOD.md` requires parallel
passes only where disjointness is proven. It is not proven for this pair, on two clauses:

- Unit 6's pass closes its own spec, which this unit's S6 reads as an acceptance input (clause 2).
- Both passes run `python tools/memory-tree/gen_build_index.py --write` (clause 3).

So the pair runs in sequence. `tools/workflows/unattended-build.js` hands the caller a roster ordered
by step and then by id (`tools/workflows/unattended-build.js:314`), dispatched strictly sequentially
(`:70`), which puts this unit first. Measured 2026-09-16 on the spec text at
`7804eb7f`, a 2026-09-14 key would have graded 81 bullets here, or 72 if unit 6 runs first.
Section 8 F3 took the relation-derived key instead, so S6's own run grades ZERO on landing day and
those two figures describe the option that was not taken; what binds every later pass of this build
from this step on is the checker's other four joins, none of which is dated. This unit declares no
sibling edge, so check 12's order arm has nothing to compare.

**What grades this build after this unit.** A unit pass runs no gate and no hand-run checker, by the
owner rule the build brief states, so the brief cannot make a later pass run this join. The
orchestrator does: from this unit's step onward, it runs `python tools/check-spec-tokens.py` over the
tree after each unit commit, and a hit it reports is fixed in the live spec carrying it before the
next unit's pass, as S6 states for this unit's own commit. The harness backs that run
mechanically: since TOOL-aDeferredBar-2, `--dispatch` runs the checker `.unattended.conf` declares
as `SPEC_TOKENS_CLI` over the live tree before admitting a pass, and refuses the dispatch while it
reds (`tools/unattended/unattended.sh:4964-4979`), so from this unit's commit a hit left in a live
spec stops the next pass rather than reaching it. The post-build bar runs the checker once
more, and grades none of this build's bullets there, because every spec is CLOSED by then. From this
unit's commit on, that run replaces the join the orchestrator has made by hand after each fold. A
later build is graded at every bar while its specs are live (§8 F4).

### Files touched (estimate)

`tools/check-spec-tokens.py`, `tools/check-spec-tokens.test.sh`, `.memory-tree.conf`,
`memory/guides/SESSION-KICKOFF.md` and `memory/map/features/spec-tokens.md`. A live spec of this build
in which S6 finds a hit is edited in the orchestrator's fix commit, not in this unit's.
`memory/project/spec-token-waivers.txt` is touched only under S6's offset rule, in a commit that
retires another row. The shipped example conf is not touched (§8 F5).

### Alternatives rejected

- **An arm in check 12.** The hygiene engine already parses the Edges bullets with their prose, so
  the edge parser would be reused rather than copied. But the engine is a copy-installed kit, so the
  arm would reach every memory-tree adopter's bar on upgrade. That is a shipped surface this unit
  did not price (M3 veto 2), for a population gov has only measured in its own tree.
- **A parts rule** that passes a token when each whitespace-separated part of it occurs, placeholders
  dropped. It was built for `--attribute <BASE>` against `--attribute <R>`. Measured, all such cases
  sit in consumes-from bullets, and over hands-off bullets it matched nothing, so it is taste and is
  left out.
- **Keeping order 39 and grading a snapshot.** Built last, the unit's pass finds no live hands-off
  bullet, because every earlier pass closes its own spec. Pinning S6 to a sha where the build's specs
  are live grades a tree the unit does not land on, and leaves every later pass of this build without
  the join. See §8 F4.
- **Counting the bullets check 12 accepts and S1 skips.** A narrower shape with a skip count announces
  the gap instead of closing it. Taking check 12's shape leaves no such bullet. See §8 F6.

## 5. Production-readiness checklist

- **security** — read-only over tracked files. No write, and no subprocess beyond the git calls the
  checker already makes (`git rev-parse` at `tools/check-spec-tokens.py:251`, `git ls-files` at
  `:140`, and the `bar` join's history query at `:305`).
- **perf / scale** — one uid map over the live specs, and one read per graded target. The spec tokens
  leg's declared ceiling is 60 s, and the whole checker runs in seconds at this corpus size.
- **error / empty / loading states** — an Edges block with no hands-off bullet grades nothing and
  counts nothing. A blank key prints the arm-off line, and a set key that is not an ISO date refuses
  through `read_cutoff_key`. A spec whose H1 carries no uid makes no map
  entry, and its own bullets count silent. A target file that fails to decode is read with
  replacement, as every spec read in this file already is.
- **observability** — S4's line on every run, and `--list` printing each hit with its key. A
  dispatch the checker refuses names up to three non-report `spec-tokens:` lines, and S4's wording
  keeps its line out of those three (§8 F9).
- **risks** — the relation S3 derives the key by exists to make the straggler case impossible at
  the merge: the value sits past the newest spec filename date on ANY ref and past the setting
  commit's own day, so a spec already in flight on another node's branch is dated before the key and
  is not graded when it lands. What the relation costs instead is the day-one zero population S3
  states — the arm lands grading nothing, its coverage is the self-test fixtures until a spec is
  written on or after the key's date, and S4's report line is what keeps that visible rather than
  silent. Clause (a) has no tree-side form, because a bar grades one tree and not the fleet
  (`.memory-tree.conf:252`), so it stays a documented check re-taken at the build commit and again
  at landing. Once a spec IS dated on or after the key, a hands-off disagreeing with its sibling
  reds the bar at that spec's merge, which is the join working.
  The merging session fixes the source bullet or names the token in the target spec. It
  adds no waiver row except in a commit that retires another, because
  `memory/project/spec-token-waivers.txt` is shrink-only by its header and `TOOL-aKeyedAnnotation-9`
  records that absorbing a class there is not available.
- **testing** — the arms §7 lists, in `tools/check-spec-tokens.test.sh`, each break staged and
  observed red at the build's post-build bar. The new arms must fit the self-test leg's declared
  figures, and neither figure is re-declared (§8 F7). At `fb07ca25` the leg's ceiling in
  `tools/gate-legs.json` is 300 s, re-declared from 120 s at `577cffbb` over two kills at 120 s and
  quiet readings of 43 s and 76 s, and the suite's row in `tools/run-gates/selftest-budgets.txt` is
  still 130 s, from a worst reading of 80 s taken when the suite held 20 arms. It now executes 42
  assertions: 38 `arm` calls over 22 scratch repos, two of them shared and reset in place by the bar
  arms TOOL-aDeferredBar-2 added, plus four direct assertions. No reading at 42 is tracked; that
  build projected 103 s idle for its first 32 assertions
  (`memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md:509`). The new arms build
  one scratch repo per criterion, six for thirteen calls, and a criterion's later state edits that
  repo's files in place: the checker takes the tracked list from `git ls-files`
  (`tools/check-spec-tokens.py:140`) and reads each tracked file's working-tree bytes (`:326`), so
  only a file the state creates needs `git add`. At that build's measured split, 2.4 s per scratch
  repo, 0.8 to 1.2 s per checker run and 0.4 s per in-place edit, the thirteen calls add about 30 to
  35 s. That sits inside the 300 s ceiling AC10 grades. Added to the 103 s projection it is 133 to
  138 s, past the 130 s budget row, which `tools/run-gates/run-selftests.sh` reads on demand and the
  post-build bar does not. A breach of either figure is PARKED, naming the reading, and is never
  re-declared: re-declaring makes a declared budget worse, which fails condition 2 of the unattended
  protocol's section 11, the condition this unit was adopted under.
- **migration** — none. A spec dated before the cutoff is never graded.
- **user docs** — the checker's docstring and the dossier; the key's own header comment.

## 6. Acceptance criteria

- **AC1** — When a scratch build holds two live specs dated at the cutoff, with H1 uids
  `EXMP-tOne-1` and `EXMP-tOne-2`, and the first's hands-off bullet to the second names `` `--frob` ``
  which the second never names, `python tools/check-spec-tokens.py` exits 1 and prints `[handoff]`
  with the source file and the key `EXMP-tOne-1>EXMP-tOne-2:--frob`. With `--frob` added to the
  second spec, it exits 0 and S4's line carries
  `1 bullet(s) graded in live spec(s) · 1 payload token(s)`. The arms are in
  `tools/check-spec-tokens.test.sh`.
  Red when: the join grades the target id itself, or searches the source instead of the target, and
  the missing token passes.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC2** — When the missing token sits on the bullet's two-space continuation line,
  `python tools/check-spec-tokens.py` exits 1 with the same `[handoff]` key. When the bullet instead
  opens with a `*` marker and a tab and names its target uid unbackticked, it exits 1 with that key
  too.
  Red when: only the bullet's first line is read, so a payload wrapped past column 100 is never
  graded; or the bullet shape is narrower than the one check 12 accepts at
  `tools/memory-tree/check-memory-hygiene.sh:1557`, so a bullet check 12 registers is neither graded
  nor counted.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC3** — When the hands-off target is a CLOSED sibling, the checker exits 0 over a token that
  sibling does not name, and S4's line reports `1 silent`. When the target is instead a uid no spec in
  the build carries in its H1, and the same scratch repo also holds a live source spec whose H1
  carries no uid, handing a live sibling a token that sibling does not name, it exits 0 and S4's line
  reports `2 silent`. Each state is one arm call in `tools/check-spec-tokens.test.sh`.
  Red when: absence reds as disagreement, so a hand-off to a finished unit fails a spec nobody may
  edit; the skip is uncounted, so a silent run reads as a graded one; or a source whose H1 carries no
  uid is graded, or skipped without being counted, so the second state exits 1 or reports `1 silent`.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC4** — When `SPEC_HANDOFF_CUTOFF` is blank in the scratch repo's `.memory-tree.conf`, a missing
  token exits 0 and the report prints `SPEC_HANDOFF_CUTOFF blank (arm off)`. When the source spec's
  date is before a set cutoff, the same bullet is not graded and the bullet count is 0. When the key
  reads `2026-9-14`, the checker exits 1 printing `is not an ISO date` before grading.
  Red when: the key is ignored, so every dated spec in the corpus is graded on landing day; a
  blank key grades anyway, so the arm cannot be turned off; or a malformed key is read through
  `read_conf_key` rather than `read_cutoff_key`, so a string comparison arms a join that grades
  nothing, the class the checker's header refuses for every other cutoff key.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC5** — When `memory/project/spec-token-waivers.txt` in the scratch repo holds
  `EXMP-tOne-1>EXMP-tOne-2:--frob` with a reason, the AC1 fixture exits 0. When the second spec then
  names `--frob`, the checker exits 1 printing `STALE WAIVER`. When that naming is then REVERTED,
  restoring the waiver to live, and a third live spec with H1 uid `EXMP-tOne-3` carries a hands-off
  bullet to `EXMP-tOne-2` naming `--frob`, which that target never names, the checker exits 1
  printing the key `EXMP-tOne-3>EXMP-tOne-2:--frob`, with no `STALE WAIVER` anywhere in its output
  and the AC1 edge still waived. Three checker runs, as AC7's distribution states.
  Red when: the waiver matches on the token alone, so one row silences the token in every edge —
  which the third state can see only once it stops riding the second state's stale hit, so it
  asserts the PRINTED KEY and the absence of `STALE WAIVER` rather than an exit code alone.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC6** — When the orchestrator's run of `python tools/check-spec-tokens.py` over the tree follows
  this unit's commit and any fix S6 makes, it exits 0, and S4's report line names
  `SPEC_HANDOFF_CUTOFF 2026-09-22` with its bullet, token and silent counts. That bullet count is
  ZERO on landing day and this criterion does not require otherwise: every spec of this build is
  dated before the relation-derived key (S3), so what the live run observes is that the arm is ARMED
  and REPORTING, and the arm's coverage on landing day is the self-test fixtures AC1 to AC5, AC9 and
  AC10 exercise. The ledger records the `--list` output S6 took, with all three counts.
  Red when: the key is misspelled or blank, so the report prints the arm-off line instead of the
  date and nothing would ever be graded; the report line is absent, so a run that never reached the
  join is indistinguishable from one that graded zero; or a live hit remains unfixed.
  permission: this unit's pass runs no hand-run checker, by the build brief's owner rule. The
  orchestrator runs it after the commit, before the next unit's pass, and writes this criterion's
  ledger line.
  figure: DERIVED at observation from the specs still live at this unit's step, since every earlier
  pass closes its own spec. §4 Rollout gives the count a 2026-09-14 key would have graded on the
  text at `7804eb7f`, which is the option section 8 F3 did not take.
- **AC7** — When `grep -c '^arm "' tools/check-spec-tokens.test.sh` runs on this unit's commit, it
  prints 51, and the `FLOOR_ASSERTIONS=` pin in `tools/check-spec-tokens.test.sh` reads 55: the 38
  `arm` calls at `fb07ca25` plus the 13 this unit adds across §7's six `New arm:` rows, two for
  each of the first three rows, three for each of the next two and one for the last, and on top of
  them the four direct assertions the suite already makes outside `arm`
  (`tools/check-spec-tokens.test.sh:265`, `:443`, `:445` and `:447`).
  Red when: arms land without raising the pin, so a later deletion of this unit's arms passes; or the
  pin and the `arm` call count plus those four disagree in either direction, which
  `bash tools/check-testsuite-counts.sh` cannot see, because it runs nothing and reads only the
  suite's shape.
  figure: PINNED. The 38 calls and the 42 pin were counted at `fb07ca25` on 2026-09-16, and the 13
  is the per-row distribution this criterion states, since §7's third fields name the floor in
  words and carry no count.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs on this unit's commit, check 5
  passes with the re-stamped `last-audit`, `memory/map/features/spec-tokens.md` names five joins,
  and the module docstring of `tools/check-spec-tokens.py` carries a fifth join row keyed `handoff`
  beside `legs`, `paths`, `cites` and `bar`, naming its population — a hands-off bullet's backticked
  payload in a LIVE spec dated at or after `SPEC_HANDOFF_CUTOFF` — and its stated limits, that
  consumes-from is ungraded and that naming a token is not doing the work.
  Red when: `.memory-tree.conf` moves with no re-stamp, or the dossier still describes four joins,
  which the map's freshness leg would not catch because it grades claims rather than prose; or the
  docstring still describes four joins, so the file's own header understates what the file grades —
  the false-confidence case charter section 7's own-header rule exists for, arriving through the gate
  written to prevent it.
  permission: this unit's pass runs no hand-run checker, by the build brief's owner rule. The
  pre-commit hook runs the checker's staged leg, check 5's staged form included, on this unit's
  commit, and the post-build bar's `kickoff-manifest ratchet` leg runs the whole checker; the
  orchestrator writes this criterion's ledger line after that bar.
- **AC9** — When the scratch build's source spec is named for the scratch repo's own
  `SPEC_HANDOFF_CUTOFF` followed by `-spec-tOne-1.md`, with H1 uid `EXMP-tOne-1`, and its hands-off
  target by that same date followed by `-spec-tOne-2-u1-part.md`, inside a `units` sub-folder of
  `spec` with H1 uid `EXMP-tOne-2` — both dated AT that key, as AC1's fixture is, so the fixture's
  dates move with the key instead of pinning a value the relation re-derives —
  `python tools/check-spec-tokens.py` exits 1
  over a token the target never names and prints the key `EXMP-tOne-1>EXMP-tOne-2:--frob`, in
  `tools/check-spec-tokens.test.sh`.
  Red when: the target is found by filename or one directory deep, so a legal family-less, tailed or
  sub-folder spec is counted silent and never graded; or the key's source half is read from the
  filename rather than the H1.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC10** — When the post-build bar runs `tools/check-spec-tokens.test.sh` with `GATE_SELFTESTS=1`,
  the suite prints `PASS (55 assertions)` inside the self-test leg's declared ceiling in
  `tools/gate-legs.json`.
  Red when: an arm is stranded past an exit or never reaches the checker, so fewer than 55 execute
  while AC7's static count still reads 51; or the new arms run the suite past that ceiling, which
  reds the leg however many assertions pass.
  permission: the suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar and never in this
  unit's pass.
- **AC11** — When `wc -c < memory/guides/SESSION-KICKOFF.md` is read at this unit's commit and at
  its parent, the reading at this unit's commit is NO LARGER than the reading at the parent, and
  `git diff --numstat` over `memory/guides/SESSION-KICKOFF.md` between those same two commits,
  resolved by sha rather than by `HEAD^ HEAD`, reports one line added and one removed; where a
  pass lands more than one commit the pair is the stamp commit and its parent, so a fix-up
  landing after the stamp does not red a stamp that landed correctly.
  Red when: the re-stamp is written as an extra line rather than in place, or a §B claim is edited
  here as well, so a carrier other units of this build write too grows on a unit whose whole edit
  to it is a stamp. The cap half is red by the `memory hygiene` leg's index-cap check; the NET delta
  against the parent is the half no leg reads, which is why this criterion reads it.
  permission: both readings are `wc -c` and `git diff` over tracked files in the pass. NO CAP IS
  RAISED by this unit: moving the 61440 is an owner turn.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`

The testsuite-counts leg witnesses the suite's shape only: it runs nothing and compares no count, so
AC7 and AC10 observe the floor. The lexicon leg grades the two function names §4 Inventory mints.

New arm: tools/check-spec-tokens.test.sh · a hands-off token its target never names, then named · the suite's executed-assertion floor, raised by the arms this row adds
New arm: tools/check-spec-tokens.test.sh · the token on a continuation line, and a star marker with a tab before an unbackticked target uid · the suite's executed-assertion floor, raised by the arms this row adds
New arm: tools/check-spec-tokens.test.sh · a hands-off to a CLOSED sibling, then to an unspecced uid beside a source whose H1 carries no uid · the suite's executed-assertion floor, raised by the arms this row adds
New arm: tools/check-spec-tokens.test.sh · a blank key, a source dated before the cutoff, and a key that is not an ISO date · the suite's executed-assertion floor, raised by the arms this row adds
New arm: tools/check-spec-tokens.test.sh · a waiver keyed on one edge, then stale, then not reaching another edge · the suite's executed-assertion floor, raised by the arms this row adds
New arm: tools/check-spec-tokens.test.sh · a family-less, tailed target filename in a units sub-folder · the suite's executed-assertion floor, raised by the arms this row adds

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
  (agent, 2026-09-14, delegated): (a). With both verbs, the leg reds correct specs. Between Tier-2
  specs dated on or after `SPEC_EDGES_CUTOFF`, check 12's reciprocity routes every consumes-from edge
  to a hands-off at the producer, which this join grades when the producer is dated on or after
  `SPEC_HANDOFF_CUTOFF`; outside that population nothing grades the payload, and S7 names the
  remainder.
- **F3** — Which cutoff? Options: (a) 2026-09-14, this spec set's date, which grades this build's
  own bullets retroactively; (b) 2026-09-08, `SPEC_EDGES_CUTOFF`'s date; (c) the value the owner's
  cutoff relation returns, re-derived at the build commit and again at landing. Measured at rev-1,
  (a) and (b) select the same 107 bullets, because no other
  live spec carries a hands-off bullet. (b) would also reach a straggler spec dated 2026-09-08 to
  2026-09-13 on another node's branch, which this build never measured. (a) was resolved on that
  reading at 2026-09-14 and is wrong for a reason neither option weighed: the owner ratified a
  RELATION over every cutoff key this register introduces at `TOOL-aJoinedCanon-1` section 8 F1,
  recorded at `.memory-tree.conf:131` and spelled out with both clauses at `.memory-tree.conf:252`,
  and 2026-09-14 breaks both — it EQUALS this build's own newest spec filename date instead of
  sitting past it, and it precedes the setting commit's own date.
  `tools/check-spec-tokens.py:47` states the same rule as the CHECKER's own posture for every cutoff
  key it reads. The counter-precedent was weighed and rejected at that same F1:
  `ACCEPTANCE_LEDGER_CUTOFF` was taken so a check would ship exercised on real units, which is this
  unit's exact rationale, and the owner did not take it here.
  RESOLVED (agent, 2026-09-20, delegated): (c), superseding the 2026-09-14 resolution of (a) narrated above. The
  value is RE-DERIVED by the relation rather than recorded as a departure, which is the route
  entirely inside a run's authority — a fork contradicting an owner ruling is not a run's to settle,
  which is the ground F4 refuses its own option (c) on. The reading re-taken at the build commit,
  2026-09-21, returns 2026-09-22 (S3), superseding the 2026-09-21 this fork first recorded from the
  day before. The day-one zero population is accepted as the relation's stated cost: S6 and AC6
  no longer require a graded count above zero, section 5 risks now reads the straggler case as the
  relation preventing it rather than as the join working, and F4's order resolution is re-read below
  in that light.
- **F4** — Where does this unit sit in the build order, and what binds the later passes to its join?
  Options for the order: (a) keep order 39, and run S6 and AC6 in a scratch worktree at a sha where
  the build's specs are live; (b) order 6, sharing the step with unit 6, the pair run in sequence as
  §4 Rollout proves it must be; (c) an order ahead of units 1 to 5. (c) contradicts owner ruling
  D12-i11, which builds units 1 to 5 first, so it is not a run's to take. (a) grades a tree the unit
  does not land on, and leaves every later pass of this build without the join.
  RESOLVED (agent, 2026-09-16, delegated): (b). RE-READ at the round-3 fold, after F3 took the
  relation-derived cutoff: the 81-bullet population and AC6's above-zero clause were properties of
  option (a)'s date and went with it, so neither argues for (b) any more. What still does is
  unchanged — (a) grades a tree the unit does not land on and leaves every later pass of this build
  without the join, (c) contradicts D12-i11, and (b) lands the arm in the tree at the earliest step
  the owner ruling leaves. No veto trips: the order verb is this
  spec's own field, and §4 Rollout shows the shared step owes no parallel pass. Options for the
  binding: (i) a build brief step making each later pass run the checker before its commit;
  (ii) nothing between this unit's commit and the post-build bar, which grades none of this build's
  bullets; (iii) the orchestrator's own run. (i) contradicts the owner rule the brief states, that a
  unit pass runs no gate and no hand-run checker, and (ii) leaves the join binding no pass of the
  build that motivated it.
  RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (iii). From this unit's step
  onward the orchestrator runs `python tools/check-spec-tokens.py` over the tree after each unit
  commit, and the post-build bar runs it once more (§4 Rollout, S6, AC6).
- **F5** — Which carriers hold `SPEC_HANDOFF_CUTOFF`? Options: (a) gov's conf and the shipped
  example, blank there with an adopter comment, as the aJoinedCanon closing review's F2 did for
  `SPEC_LEGLINE_CUTOFF`; (b) gov's conf only. F2's premise was an adopter holding a conf without the
  key while their kit's own text describes the arm, and for `SPEC_LEGLINE_CUTOFF` that text is
  `tools/memory-tree/SPEC-TEMPLATE.template.md:184`. This unit writes no shipped text, and the
  checker ships to no adopter. (a) would put an adopter-visible key that no shipped tool reads into a
  copy-installed kit file, a public surface this unit never priced, so M3 veto 2 discards it, as §4
  Alternatives rejected does for an arm in check 12. RESOLVED (agent, 2026-09-16, delegated): (b),
  with the §3 external edge to `TOOL-aJoinedCanon-13`, which would otherwise red on this key.
- **F6** — Which bullet shape is graded? Options: (a) rev-1's `- **hands-off** ` with a backticked id,
  counting on S4's line the bullets check 12 accepts and this shape skips; (b) check 12's accepted
  shape, cited line for line in §4. RESOLVED (agent, 2026-09-16, delegated): (b). It grades every
  hands-off edge check 12 registers, so no skipped bullet is left to count.
- **F7** — Do the new arms fit the self-test leg's declared figures, or do the figures move?
  Options: (a) keep the leg's ceiling in `tools/gate-legs.json`, 120 s when this fork was resolved
  and 300 s at `fb07ca25`, and the 130 s budget in
  `tools/run-gates/selftest-budgets.txt`, require the arms to fit, and park a breach; (b) stage fewer
  cases per arm call, lowering the arm count and the coverage S8, AC7 and AC10 pin; (c) re-declare
  either figure from the post-build reading. (c) makes a declared budget worse, which fails condition
  2 of the unattended protocol's section 11, so the unit would become a backlog row rather than an
  adoption. (b) gives up cases §6 stages.
  RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (a), by the route §5 testing
  gives, one scratch repo per criterion edited in place, observed by AC10.
- **F8** — How is S2's source with no H1 uid observed? Options: (a) a third AC3 state with its own
  arm call, moving the pin to 33 and adding to F7's cost; (b) S2 names that branch NOT OBSERVED, with
  its reason; (c) one more source spec with no H1 uid inside AC3's existing fixture, asserting the
  silent count it adds, with no arm call added. (b) leaves a reachable branch ungraded.
  RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (c). The arm count, the floor
  pin and §5's cost figures do not move, and S2 stays observed by AC3.
- **F9** — How does S4's line sit beside the refusal `--dispatch` prints? That verb runs the checker
  before every pass and, on a red run, names the first three `spec-tokens:` lines that are not
  report lines, dropping the three existing report lines by their text
  (`tools/unattended/unattended.sh:4973`).
  Options: (a) word S4's line so that filter drops it too, through the `live spec(s) ·` it already
  matches; (b) keep rev-2's wording, so a refused dispatch spends one of its three diagnosis lines on
  the count and can crowd out a hit; (c) widen the filter, which changes the unattended kit's shipped
  bytes and version, a surface this unit never priced. (b) degrades a landed diagnosis, and (c)
  reaches a second kit for a wording choice this unit owns.
  RESOLVED (agent, 2026-09-16, delegated): (a). AC1's graded state observes the wording.

## 9. Revision log

- rev-1 · 2026-09-14 · adopted after the round-1 fold under protocol section 11, from fold plans
  c1 A1 to A6, c2's three, c3's optional, c4 A2 to A4 and c5 A3. Only the hands-off payload join was
  measured decidable. The rest are named in §3. Recorded with `--rescope --act add`.
- rev-2 · 2026-09-16 · G6 round-1 fold. H1 and L1: AC7 re-witnessed by the static `arm` count
  against the pin, new AC10 by the suite's printed count at the post-build bar, S8 moves the pin
  from 20 to 32, and §7's `New arm:` rows carry their floor and arm counts. H2: header order 39 to 6,
  new §4 Rollout, and S6 and AC6 require a graded count above zero (§8 F4). H3: S1, S2, S5 and §4
  The selection key both ends by H1 uid at any depth, with new AC9. M1: §4 Inventory renames the
  function `scan_handoffs`, adds `read_spec_uids`, and §7 gains `lexicon naming predicates`. M2: S6,
  §5 risks and §4 Files touched drop the waiver route except under an offset rule, and §3 names the
  registry high-water gate out. M3: S3 and §3 keep the key out of the shipped example (§8 F5), with
  a §3 external edge. L2: §3 and §8 F2 narrow the reciprocity claim, and S7 names the remainder. L3:
  S1, §4 and AC2 take check 12's bullet shape (§8 F6). From the record's unconfirmed notes: §1's
  unreproducible token figure is replaced by a count at `282e0a6b`, and §4's veto citation reads
  veto 2. AC2 to AC5 and AC9 carry the held suite's `permission:` line, and §5 testing states the
  suite's budget and ceiling against the new arm count. Fold verification: S5 now names AC9, whose
  Red-when observes the H1 key; §3, S7 and §8 F2 add that this join grades a forced hands-off only
  when the producer is dated on or after `SPEC_HANDOFF_CUTOFF`; §4 The selection cites check 12's
  any-depth selection line rather than its registration line alone; §4 Rollout narrows the brief's
  permission to run the checker to a unit whose criterion names it; §1 names the self-test leg's
  ceiling and budget as a condition of nothing getting worse; S6 parks the unit with a foreign hit,
  which AC6's exit 0 already required. Round-2 fold, third pass, from the orchestrator's decisions
  on the second-pass verifier problems: §5 testing keeps the self-test leg's ceiling and budget,
  requires the new arms to fit by one scratch repo per criterion edited in place, and parks a breach
  rather than re-declaring either figure (new §8 F7), and AC10 reds past that ceiling. AC3's second
  state stages a source with no H1 uid inside its existing fixture with no arm call added, reporting
  `2 silent`, and §7's AC3 row names it (new §8 F8); S2 stays observed by AC3, and S8, AC7 and the
  pin stay at 32. §4 Rollout and §8 F4 bind the later passes through the orchestrator's run of the
  checker after each unit commit, because the build brief's owner rule lets a unit pass run no gate
  and no hand-run checker. S6, AC6, §1 and §4 Files touched move this unit's own real-tree pass and
  its fixes to that run, and AC6 and AC8 gain `permission:` lines.
- rev-3 · 2026-09-16 · regrounded on fb07ca25 (origin/main). TOOL-aDeferredBar-2 (`d7caa426`,
  `50c4418a`, `15148b2a`) gave `tools/check-spec-tokens.py` a fourth join, `bar`, a third report
  line, `AC_HEAD` and `read_cutoff_key`, and grew its suite to 38 `arm` calls and a 42 pin: §1 and S7
  make this unit's join the fifth; S3, §4 The selection, §5 and new AC4 state three read the key
  through `read_cutoff_key` and observe its ISO refusal, so S8, AC7, AC10 and §7's AC4 row move to 13
  new calls, 51 `arm` calls and a 55 pin; §4 The report prints S4's line fourth and keeps it out of
  the `bar` join's populations; AC6 names S4's line rather than an ordinal; AC8 counts five joins,
  because the dossier already names four; §4 The selection, The hit, §5 and §10 re-cite the moved
  lines. `577cffbb` re-declared the self-test leg's ceiling 120 s to 300 s: §5 testing and §8 F7's
  option (a) carry it, and §5 prices the new arms against the 130 s budget row. `--dispatch` now runs
  the declared checker before every pass (`tools/unattended/unattended.sh:4964-4979`): §1 and §4
  Rollout name it, and new §8 F9 words S4's line so its refusal filter drops it, observed by AC1. S3
  re-cites the conf line a sibling spec cites, S9 names the `bar` join's precedent, §4 Rollout cites
  the roster order, and §10 re-cites the recall hit at `.memory-tree.conf:278`. Extended 2026-09-20,
  same base, on a second regrounding pass. Every citation above was re-read at HEAD and holds:
  `tools/check-spec-tokens.py` at `:140`, `:251`, `:258`, `:305`, `:326`, `:329`, `:370`, `:405`,
  `:423`, `:430`, `:434` and `:442`; check 12's grammar at
  `tools/memory-tree/check-memory-hygiene.sh:1153`, `:1517`, `:1533-1534`, `:1547`, `:1549`, `:1553`,
  `:1557`, `:1564-1565`, `:1588` and `:1790`; `--dispatch` at `tools/unattended/unattended.sh`
  `:4964-4979` and `:4973`; the roster at `tools/workflows/unattended-build.js:70` and `:314`; and
  `tools/memory-tree/.memory-tree.conf.example:140`. Re-measured: the suite makes 38 `arm` calls with
  `FLOOR_ASSERTIONS=42`, its four direct assertions sit at `tools/check-spec-tokens.test.sh:265`,
  `:443`, `:445` and `:447`, the `spec-tokens self-test` ceiling is 300 s and its
  `tools/run-gates/selftest-budgets.txt` row is 130 s, so S8, AC7, AC10 and §5 testing are unchanged.
  S3's example conf line is corrected from `:422`, which no sibling cites, to `:429`, which unit 12
  does. §4 Rollout's roster citation now reads a file main renders from
  `tools/workflows/unattended-build.template.js`, which changes neither line.
  Extended again 2026-09-20, same base, by the build-wide consolidation pass, which changed no
  rule of this spec and is recorded so the check is on the record. The `permission:` lines on AC1
  to AC5, AC9 and AC10 were re-read against the gate-guard hook's measured denied population and
  KEPT: each observation is a `tools/check-spec-tokens.test.sh` file invocation carrying no
  read-only verb, which is exactly what that hook denies before VERIFYING, and each already places
  its run at the build's one post-build bar. AC6 and AC8 keep the no-hand-run-checker line the
  build brief's owner rule gives them, and AC7's `grep -c` reads a tracked file in the pass and is
  neither a suite nor a leg. §7's six `New arm:` third fields name `FLOOR_ASSERTIONS` and an arm
  count rather than `none`, and `tools/check-spec-tokens.test.sh` is not one of the two suites the
  build-wide arm-line rule names, so none of them moves. No criterion of this spec asserts that a
  phrase counts zero, so the phrase sweep found nothing to repair. The capped carriers this unit
  writes are `.memory-tree.conf`, which carries no byte cap, and
  `memory/guides/SESSION-KICKOFF.md`, 20057 bytes against the 61440 its class declares.
  Extended once more 2026-09-20, same base, by the closing consolidation pass, which applied the
  build's NET-ZERO rule to every capped carrier rather than only to the contested ones, so the
  forty-kilobytes-free argument is no longer load-bearing. §2 S7 now NAMES its passage, the
  `last-audit:` line at `memory/guides/SESSION-KICKOFF.md:5`, records that a stamp displaces no
  text, and new §6 AC11 reads the carrier at this unit's commit against its PARENT with a
  `git diff --numstat` half that reds a stamp written as an added line. Inside this closing set the passages taken
  are the §B `TMPDIR` trap, the ceiling line, the §B M6 claim and this stamp, so no two of them
  collide; a stamp is not a contested passage at all, because every unit touching a watched path
  rewrites it, the passes are ordered, and each leaves the file the same size. §8 F4's second resolution is RE-RATIFIED unchanged: the orchestrator's run
  of the checker BETWEEN passes is the orchestrator's and not a pass's, so the build-wide rule
  sending a gate-leg observation to the run at VERIFYING does not reach AC6 or AC8, and §4
  Rollout keeps its wording. The header date moves to the last-change date; the rev does not,
  because no criterion changed its subject.
  Closed 2026-09-20, same base, by the last consolidation pass before the spec audits re-run.
  §2 S7 STOPS CALLING THE MANIFEST RE-STAMP A TRIM, on the orchestrator's ruling: rewriting the
  `last-audit:` line at `memory/guides/SESSION-KICKOFF.md:5` is the bookkeeping every unit
  touching a watched file owes, it claims nothing from that carrier's headroom, and the sibling
  unit that rewrites the same line is NOT a collision with this one. §7's six `New arm:` third
  fields are rewritten in WORDS: each now reads the suite's executed-assertion floor, raised by
  the arms its row adds, and none carries an identifier or a count, which is what the build's
  field rule asks for. The arithmetic those counts carried is not stranded, it is MOVED to where
  a criterion can own it: §6 AC7 now states the per-row distribution that sums to thirteen, its
  `figure:` line says the thirteen is that distribution rather than a sum read out of §7, and
  §2 S8 points at AC7 instead of at the rows. One verifier finding is repaired rather than
  carried: AC11's second half read `git diff --numstat HEAD^ HEAD`, which reds a correctly landed
  stamp whenever a pass lands more than one commit; it now resolves the stamp commit and its
  parent by sha and says so. Every `permission:` line naming the HELD `spec-tokens self-test` leg
  spells the VERIFYING run `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` rather than
  "with `GATE_SELFTESTS=1`", so a held leg is not read as covered by a plain bar. The header date
  stays at the last-change date; the rev does not move.
  Extended 2026-09-20 by the spec-audit round 3 fold, the G6 round-2 record, which exited CONVERGED
  with no blocker, so its one HIGH folds here rather than promoting; H1 was folded first, because a
  re-cut AC6 changes which criteria the other two hang from. G6 H1 (8, 15): the key was
  `SPEC_HANDOFF_CUTOFF="2026-09-14"`, which breaks BOTH clauses of the cutoff relation the owner
  ratified at `TOOL-aJoinedCanon-1` section 8 F1 — it equals this build's own newest spec filename
  date instead of sitting past it, and it precedes the setting commit's day — and no section named
  the ruling or recorded a departure, while S3 ordered a header comment "in the idiom of
  `SPEC_LEGLINE_CUTOFF`" whose why-this-date slot IS that relation. The route taken is
  RE-DERIVATION, the one wholly inside a run's authority, not a recorded exception: the reading of
  2026-09-20 over every ref and worktree returns 2026-09-21, and S3 now carries the relation, its
  two register rows at `.memory-tree.conf:131` and `.memory-tree.conf:252`, the reading, the
  re-derive-at-landing rule and the day-one zero cost. Everything that hung on the retroactive date
  moved with it: S6 and AC6 drop the above-zero clause and observe instead that the arm is ARMED and
  REPORTING, AC6's `figure:` and §4 Rollout attribute the 81 and 72 bullet counts to the option not
  taken, section 5 risks stops affirming the straggler merge as the join working and states the
  relation prevents it, section 8 F3 gains option (c) with the ruling, the register and the
  `ACCEPTANCE_LEDGER_CUTOFF` counter-precedent cited and is re-resolved to it, F4's order
  resolution is re-read so it no longer leans on the 81-bullet population or the zero-count clause,
  AC9's fixture dates move with the key rather than being pinned, and §10's 109-bullet probe is
  attributed to the key that was not taken. G6 M1 (3): S7 said the checker's header docstring is
  "Observed by AC8 and AC11" while neither read a byte of it, so AC8 now reads the fifth join row
  keyed `handoff` beside the four, with its population and its two stated limits, and its Red when
  names the four-join header in front of a five-join program. G6 M2 (4): AC5's third state rode the
  second state's stale hit, so an implementation matching on the bare token — the exact defect its
  own Red when names — passed all three states; state 3 now REVERTS the second spec's naming, adds
  a third live spec with H1 uid `EXMP-tOne-3`, and asserts the PRINTED KEY
  `EXMP-tOne-3>EXMP-tOne-2:--frob` with no `STALE WAIVER` in the output rather than an exit code
  alone. The arm count does not move, so S8, AC7, AC10 and section 5's cost figures are untouched.
  Base and header date unchanged; the rev is kept under the fold's edit rule, which extends this
  spec's existing 2026-09-20 line rather than opening a new one.
- rev-4 · 2026-09-20 · §2 · S3 · AC9 · the round-3 fold's verifier. Two repairs about one literal.
  The relation was RE-RUN at HEAD on node `d` before anything was edited, all three readings of the
  `SPEC_DIRECT_CUTOFF` row at `.memory-tree.conf:258-260`: (a) the newest spec filename date over
  every ref and every `git worktree list` worktree is 2026-09-20, (b) `git log -1 --format=%cs` is
  2026-09-20, so the relation still returns 2026-09-21 and the value stands. What did not stand is
  the maintenance story. Four places carried the date literally with nothing joining them, so a
  re-derivation at the build commit or at landing could move one and leave three, and no leg would
  red. AC9 leaves that set entirely: it spelled two literal fixture filenames and then claimed, in
  the same sentence, that its fixture dates move with the key rather than being pinned — a
  contradiction inside one clause, since AC1 genuinely is unpinned and AC9 was not. Its fixture
  names are now derived from the scratch repo's own key, which keeps the family-less, tailed and
  sub-folder shape the criterion exists to grade and removes one carrier. S3 names the three that
  remain — its own paragraph, AC6's report line and §8 F3's resolution — and says plainly that no
  gate joins them, so the re-derivation has a checklist instead of a memory. Recorded as its own
  entry with a single bump: this build settled that form for a spec already touched the same day.
  Verified in the same round and corrected in place, at no further rev bump: S3's checklist now says
  that section 9's own mentions of the value are frozen records of readings taken and are not
  carriers, so a grep returning more than three hits does not read as a fourth carrier.
- rev-5 · 2026-09-21 · §2 S3 · §6 AC6 · §8 F3 · the build pass. THE KEY MOVED, by the relation
  rather than by a choice, which is what S3 ordered and not a departure from it. The three readings
  were re-taken at the build commit on node `d`, before any file was written: (a) the newest spec
  filename date is 2026-09-20 over every local and remote ref and, at any depth, over every
  `git worktree list` worktree; (b) `git log -1 --format=%cs` is 2026-09-21. The later is
  2026-09-21, so the relation returns 2026-09-22, and rev-4's 2026-09-21 no longer satisfies the
  second clause it was derived against — it would have EQUALLED the setting commit's own day, which
  is precisely the shape §8 F3 rejected 2026-09-14 for. S3's three carriers moved together in this
  one commit, as its checklist says they must: S3's own paragraph, where the key is spelled and
  where its reading is recorded; AC6's expected report line; and F3's resolution. Section 9's
  earlier mentions of 2026-09-21 are frozen records of the readings then taken and did NOT move,
  which S3's checklist already states. Nothing else in this spec changed: no criterion changed its
  subject, the day-one zero population is unaffected because the key still postdates every spec of
  this build, and §5 risks reads the same. The relation is re-derived once more AT LANDING.
  Recorded as its own entry with a single bump, the form rev-4 settled.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "join a spec's hands-off edge payload
  tokens against the sibling spec that receives them"` returned symbol-name neighbours only
  (`build_edges` in `tools/process-monitor/scope.py`, `join_aliases`, `parse_tokens`) and no seam in
  the spec-tokens feature. The seam was found by reading source instead: this unit extends
  `tools/check-spec-tokens.py`, reusing its LIVE selection, `TICK`, `NOT_A_TOKEN`, the
  acceptance-criteria bullet shape, the cutoff reader `read_cutoff_key` and the waiver registry.
- **Against BASE.** BASE is `fb07ca25`, origin/main, which HEAD `94fd2f54` merges without changing
  code. From `abac6d59` to `fb07ca25`, TOOL-aDeferredBar-2 changed `tools/check-spec-tokens.py` and its
  test: the `bar` join over the legs and paths populations, armed by `SPEC_DIRECT_CUTOFF`; the
  acceptance section found by heading text; `read_cutoff_key`, one ISO-date refusal for every cutoff
  key; a third report line; and 18 more `arm` calls with four direct assertions, the pin 20 to 42.
  The cited lines hold at `fb07ca25`: `:258` is the any-depth spec population, `:370` is the
  acceptance bullet regex, `:405` keys a waiver on the hit's third field, and `:423`, `:430` or
  `:434`, and `:442` are the three report lines. `577cffbb` moved the self-test leg's ceiling to
  300 s. The unattended kit's `--dispatch` gained its run of the declared checker, whose report-line
  filter §8 F9 answers. The shipped example conf now declares `SPEC_DIRECT_CUTOFF` blank by hand
  (`tools/memory-tree/.memory-tree.conf.example:140`); §8 F5 stays as resolved, so this unit's key
  stays out of it. Probed read-only at `94fd2f54` under a 2026-09-14 key, S1's join grades 109
  bullets and 160 tokens with no miss, every one in this build; under the relation-derived key
  §8 F3 takes it grades none of them, and no other build's live spec is dated on or after that key
  at all.
- **Against check 12.** The grammar S1 takes is check 12's edge arm in
  `tools/memory-tree/check-memory-hygiene.sh`, unchanged from `abac6d59` to `fb07ca25` but for its
  version line, memory-tree 2.74 to 2.78; §4 The selection cites each line, and each holds at
  `fb07ca25`. It is reused by copying its regexes into the checker, not by calling the engine,
  for the reason §4 Alternatives rejected gives.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: `python tools/memory-recall/query.py "how are spec edges between sibling units
  checked for agreement" --terms "hands-off consumes-from Edges reciprocity sibling spec join payload
  token check-spec-tokens SPEC_EDGES_CUTOFF edge"`. Top hits: `.memory-tree.conf:278`, at `:268` when
  queried (`SPEC_EDGES_CUTOFF`'s header, whose payload arm is check 12's `external` test and not this join),
  TOOL-aKeyedAnnotation-9 (the paths arm's open defect, untouched here), `memory/HYGIENE.md:135`,
  the aLeakedHandle round-2 review's edge-bullet checklist item, and this build's G4 round-1 record.
