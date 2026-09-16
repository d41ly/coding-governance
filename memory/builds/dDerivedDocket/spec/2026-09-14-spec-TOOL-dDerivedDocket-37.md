# TOOL-dDerivedDocket-37 — a hands-off's payload tokens are named by the sibling it names

**Status:** SPECCED · rev-2 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 6

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
The fold fixed that instance. A probe run after the fold found three more. Unit 7 handed unit 11 a
verb whose comparison is unit 34's. Unit 13 handed unit 35 a helper by a filename unit 35 never used.
Unit 10 handed the adopter runbook a leg its own §8 F4 said an adopter adds, and the runbook never
said so. The orchestrator fixed all three before this spec was written. The tree that probe read was
never committed, so its token count cannot be re-derived and is not repeated here. With this spec's
rev-2 selection at `282e0a6b`, after the fixes, the build's live specs carry 107 hands-off bullets
and 128 payload tokens, and no token misses.

Each of those is a join over two tracked files, the shape `tools/check-spec-tokens.py` already
exists to run. This unit adds it there as a fourth population. A later spec set then gets the answer
from the bar rather than from a review round, and so does every later pass of this build, through
the run of the checker the orchestrator makes after each unit commit (§4 Rollout). It was adopted
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
- **S3** — the dated demand. `SPEC_HANDOFF_CUTOFF="2026-09-14"` is appended at the end of
  `.memory-tree.conf`, with a header comment in the idiom of `SPEC_LEGLINE_CUTOFF`: what the arm
  grades, why it exists as measured here, why this date, and that blank means off. Blank or absent
  turns the arm off, and the report says `SPEC_HANDOFF_CUTOFF blank (arm off)`. The key goes in
  gov's conf only, never in `tools/memory-tree/.memory-tree.conf.example`, per §8 F5. It is appended
  rather than placed beside its sibling, so this unit moves no conf line a sibling spec cites, such
  as `.memory-tree.conf:387`. Observed by AC4 and AC6.
- **S4** — the report line. Every run prints
  `spec-tokens: <b> hands-off bullet(s) graded · <t> payload token(s) · <s> silent (no live target in the build, or no source uid) · SPEC_HANDOFF_CUTOFF <date>`,
  so a green run over zero bullets cannot pass for a graded one. Observed by AC1, AC3 and AC6.
- **S5** — the waiver key. A `handoff` hit's key is `<source uid>><target uid>:<token>`, where each
  uid is the one its spec's H1 carries, never one read from a filename. A hit is waived only by a row
  whose token cell is that key. The existing stale-waiver and missing-reason refusals apply
  unchanged. Observed by AC5 and AC9.
- **S6** — the real-tree pass. This unit's pass runs no hand-run checker, by the owner rule the
  build brief states. After this unit's commit, at `order 6` once units 1 to 5 have closed, the
  orchestrator runs `python tools/check-spec-tokens.py --list` once over the tree, and its graded
  bullet count must be above zero. It is not a gate leg run. A hit in a live spec of this build is
  fixed in that spec, at the source bullet or in the target's text, with a rev line naming this join,
  in a commit the orchestrator makes before the next unit's pass. A hit in another build's live spec
  is that build's writer's to fix, and none exists today (§8 F3). Neither kind takes a waiver row
  unless the same commit retires another row: `memory/project/spec-token-waivers.txt` is shrink-only
  by its own header, and `TOOL-aKeyedAnnotation-9` records that absorbing a class there is not
  available. A foreign hit with no row to retire is parked, naming the hit, and this unit parks with
  it, because AC6 cannot pass over a live hit. Observed by AC6.
- **S7** — the carriers. The checker's header docstring gains the fourth population and its limits.
  The join proves a sibling names a token, never that it does the work. Consumes-from bullets are not
  graded, so a consumes-from payload is graded only through a hands-off check 12 forces at the
  producer and this join reads. Neither check grades a Tier-1 consumer's edges, an edge from a
  consumer dated before `SPEC_EDGES_CUTOFF`, or an edge naming a Tier-1 producer or one dated before
  `SPEC_HANDOFF_CUTOFF`. An `external` bullet has no sibling to join. The
  `memory/map/features/spec-tokens.md` dossier refreshes its title and prose on touch. The kickoff
  manifest's `last-audit` is re-stamped in this unit's commit with a delta line in the commit
  message, because `.memory-tree.conf` is in its `watch:` list. Observed by AC8.
- **S8** — the self-test arms and their floor. `tools/check-spec-tokens.test.sh` gains the twelve
  `arm` calls §7's `New arm:` rows sum to, and `FLOOR_ASSERTIONS` moves from 20 to 32. Observed by
  AC7 and AC10.
- **S9** — the version. NOT OBSERVED by a criterion here: `KIT_SPEC_TOKENS_VERSION` does not move.
  The file ships to no adopter, and the leg-line arm TOOL-aJoinedCanon-7 added was added at the same
  version, so no reader of the constant sees a change.

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
    skip unless <date> >= SPEC_HANDOFF_CUTOFF (blank: arm off, nothing graded)
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
`tools/check-spec-tokens.py:168`.

One rule is wider than check 12's. Check 12 reads a bullet's first line only, and this join reads
its two-space continuation lines too, the rule this file already uses for section 6 bullets
(`tools/check-spec-tokens.py:237`). The target is read whole, because a sibling may name the token
in its scope, its design or its edges, and any of those counts as naming it. Measured 2026-09-16 at
`7804eb7f`, 624 tracked specs carry an H1 uid each and no two files in a build share one, so the
several-files rule has no instance today.

### The hit and its waiver

A `handoff` hit's key is `<source uid>><target uid>:<token>`, both uids read from H1 lines, and
that is the string a waiver row matches (`tools/check-spec-tokens.py:254` keys on the hit's third
field). A token waived for one edge is therefore not waived for another. A bare token key would
waive the token in every bullet of every build, which is the stale-exception problem the registry
refuses elsewhere. The registry is shrink-only by its header, so S6's offset rule governs when a row
may be added at all.

### The report

The existing two report lines (`tools/check-spec-tokens.py:270` and `:279`) are unchanged. S4's line
is printed third, whether or not the arm is on.

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

So the pair runs in sequence. `tools/workflows/unattended-build.js` dispatches strictly sequentially
and orders a shared step by id, which puts this unit first. Measured 2026-09-16 on the spec text at
`7804eb7f`, S6 then grades 81 bullets, or 72 if unit 6 runs first. This unit declares no sibling
edge, so check 12's order arm has nothing to compare.

**What grades this build after this unit.** A unit pass runs no gate and no hand-run checker, by the
owner rule the build brief states, so the brief cannot make a later pass run this join. The
orchestrator does: from this unit's step onward, it runs `python tools/check-spec-tokens.py` over the
tree after each unit commit, and a hit it reports is fixed in the live spec carrying it before the
next unit's pass, as S6 states for this unit's own commit. The post-build bar runs the checker once
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

- **security** — read-only over tracked files. No write, no subprocess beyond the `git ls-files`
  call the checker already makes.
- **perf / scale** — one uid map over the live specs, and one read per graded target. The spec tokens
  leg's declared ceiling is 60 s, and the whole checker runs in seconds at this corpus size.
- **error / empty / loading states** — an Edges block with no hands-off bullet grades nothing and
  counts nothing. A blank key prints the arm-off line. A spec whose H1 carries no uid makes no map
  entry, and its own bullets count silent. A target file that fails to decode is read with
  replacement, as every spec read in this file already is.
- **observability** — S4's line on every run, and `--list` printing each hit with its key.
- **risks** — a straggler branch from another node could merge a spec dated on or after the cutoff
  whose hands-off disagrees with its sibling. That reds the bar at the merge, which is the join
  working. The merging session fixes the source bullet or names the token in the target spec. It
  adds no waiver row except in a commit that retires another, because
  `memory/project/spec-token-waivers.txt` is shrink-only by its header and `TOOL-aKeyedAnnotation-9`
  records that absorbing a class there is not available.
- **testing** — the arms §7 lists, in `tools/check-spec-tokens.test.sh`, each break staged and
  observed red at the build's post-build bar. The new arms must fit the self-test leg's declared
  figures, and neither figure is re-declared (§8 F7). At BASE the suite's row in
  `tools/run-gates/selftest-budgets.txt` is 130 s, from a worst reading of 80 s over 20 arms, and its
  leg ceiling in `tools/gate-legs.json` is 120 s. Twelve more arms at that per-arm cost land near
  128 s, past the ceiling, so the twelve share the 40 s the ceiling leaves over that reading, about
  3.3 s each against BASE's 4 s. BASE builds a fresh scratch repo for each of its 20 arm calls. The
  new arms build one per criterion, six for twelve calls, and a criterion's later state edits that
  repo's files in place: the checker takes the tracked list from `git ls-files`
  (`tools/check-spec-tokens.py:87`) and reads each tracked file's working-tree bytes (`:203`), so
  only a file the state creates needs `git add`. A breach of either figure at the post-build bar is
  PARKED, naming the reading, and is never re-declared: re-declaring makes a declared budget worse,
  which fails condition 2 of the unattended protocol's section 11, the condition this unit was
  adopted under.
- **migration** — none. A spec dated before the cutoff is never graded.
- **user docs** — the checker's docstring and the dossier; the key's own header comment.

## 6. Acceptance criteria

- **AC1** — When a scratch build holds two live specs dated at the cutoff, with H1 uids
  `EXMP-tOne-1` and `EXMP-tOne-2`, and the first's hands-off bullet to the second names `` `--frob` ``
  which the second never names, `python tools/check-spec-tokens.py` exits 1 and prints `[handoff]`
  with the source file and the key `EXMP-tOne-1>EXMP-tOne-2:--frob`. With `--frob` added to the
  second spec, it exits 0 and S4's line counts one bullet and one token. The arms are in
  `tools/check-spec-tokens.test.sh`.
  Red when: the join grades the target id itself, or searches the source instead of the target, and
  the missing token passes.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC2** — When the missing token sits on the bullet's two-space continuation line,
  `python tools/check-spec-tokens.py` exits 1 with the same `[handoff]` key. When the bullet instead
  opens with a `*` marker and a tab and names its target uid unbackticked, it exits 1 with that key
  too.
  Red when: only the bullet's first line is read, so a payload wrapped past column 100 is never
  graded; or the bullet shape is narrower than the one check 12 accepts at
  `tools/memory-tree/check-memory-hygiene.sh:1557`, so a bullet check 12 registers is neither graded
  nor counted.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC3** — When the hands-off target is a CLOSED sibling, the checker exits 0 over a token that
  sibling does not name, and S4's line reports `1 silent`. When the target is instead a uid no spec in
  the build carries in its H1, and the same scratch repo also holds a live source spec whose H1
  carries no uid, handing a live sibling a token that sibling does not name, it exits 0 and S4's line
  reports `2 silent`. Each state is one arm call in `tools/check-spec-tokens.test.sh`.
  Red when: absence reds as disagreement, so a hand-off to a finished unit fails a spec nobody may
  edit; the skip is uncounted, so a silent run reads as a graded one; or a source whose H1 carries no
  uid is graded, or skipped without being counted, so the second state exits 1 or reports `1 silent`.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC4** — When `SPEC_HANDOFF_CUTOFF` is blank in the scratch repo's `.memory-tree.conf`, a missing
  token exits 0 and the report prints `SPEC_HANDOFF_CUTOFF blank (arm off)`. When the source spec's
  date is before a set cutoff, the same bullet is not graded and the bullet count is 0.
  Red when: the key is ignored, so every dated spec in the corpus is graded on landing day; or a
  blank key grades anyway, so the arm cannot be turned off.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC5** — When `memory/project/spec-token-waivers.txt` in the scratch repo holds
  `EXMP-tOne-1>EXMP-tOne-2:--frob` with a reason, the AC1 fixture exits 0. When the second spec then
  names `--frob`, the checker exits 1 printing `STALE WAIVER`. A third spec's bullet to the second,
  naming `--frob` unnamed, still exits 1.
  Red when: the waiver matches on the token alone, so one row silences the token in every edge.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC6** — When the orchestrator's run of `python tools/check-spec-tokens.py` over the tree follows
  this unit's commit and any fix S6 makes, it exits 0, and its third report line names
  `SPEC_HANDOFF_CUTOFF 2026-09-14` with a graded bullet count above zero. The ledger records the
  `--list` output S6 took, with its bullet, token and silent counts.
  Red when: the key is misspelled or blank, so the arm is off over the corpus that motivated it; the
  graded bullet count is 0, so the arm landed without grading one real bullet; or a live hit remains
  unfixed.
  permission: this unit's pass runs no hand-run checker, by the build brief's owner rule. The
  orchestrator runs it after the commit, before the next unit's pass, and writes this criterion's
  ledger line.
  figure: DERIVED at observation from the specs still live at this unit's step, since every earlier
  pass closes its own spec. §4 Rollout gives the count measured on the text at `7804eb7f`.
- **AC7** — When `grep -c '^arm "' tools/check-spec-tokens.test.sh` runs on this unit's commit, it
  prints 32, and the `FLOOR_ASSERTIONS=` pin in `tools/check-spec-tokens.test.sh` reads 32: the 20
  `arm` calls at BASE plus the 12 §7's `New arm:` rows add.
  Red when: arms land without raising the pin, so a later deletion of this unit's arms passes; or the
  pin and the `arm` call count disagree in either direction, which
  `bash tools/check-testsuite-counts.sh` cannot see, because it runs nothing and reads only the
  suite's shape.
  figure: PINNED. The 20 was counted at BASE `abac6d59` on 2026-09-16, and the 12 is the sum of §7's
  rows.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs on this unit's commit, check 5
  passes with the re-stamped `last-audit`, and `memory/map/features/spec-tokens.md` names four joins.
  Red when: `.memory-tree.conf` moves with no re-stamp, or the dossier still describes three joins,
  which the map's freshness leg would not catch because it grades claims rather than prose.
  permission: this unit's pass runs no hand-run checker, by the build brief's owner rule. The
  pre-commit hook runs the checker's staged leg, check 5's staged form included, on this unit's
  commit, and the post-build bar's `kickoff-manifest ratchet` leg runs the whole checker; the
  orchestrator writes this criterion's ledger line after that bar.
- **AC9** — When the scratch build's source spec is named `2026-09-14-spec-tOne-1.md` with H1 uid
  `EXMP-tOne-1`, and its hands-off target is named `2026-09-14-spec-tOne-2-u1-part.md` inside a
  `units` sub-folder of `spec` with H1 uid `EXMP-tOne-2`, `python tools/check-spec-tokens.py` exits 1
  over a token the target never names and prints the key `EXMP-tOne-1>EXMP-tOne-2:--frob`, in
  `tools/check-spec-tokens.test.sh`.
  Red when: the target is found by filename or one directory deep, so a legal family-less, tailed or
  sub-folder spec is counted silent and never graded; or the key's source half is read from the
  filename rather than the H1.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.
- **AC10** — When the post-build bar runs `tools/check-spec-tokens.test.sh` with `GATE_SELFTESTS=1`,
  the suite prints `PASS (32 assertions)` inside the self-test leg's declared ceiling in
  `tools/gate-legs.json`.
  Red when: an arm is stranded past an exit or never reaches the checker, so fewer than 32 execute
  while AC7's static count still reads 32; or the new arms run the suite past that ceiling, which
  reds the leg however many assertions pass.
  permission: the suite is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`,
  never in this unit's pass.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`

The testsuite-counts leg witnesses the suite's shape only: it runs nothing and compares no count, so
AC7 and AC10 observe the floor. The lexicon leg grades the two function names §4 Inventory mints.

New arm: tools/check-spec-tokens.test.sh · a hands-off token its target never names, then named · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 2 arm calls
New arm: tools/check-spec-tokens.test.sh · the token on a continuation line, and a star marker with a tab before an unbackticked target uid · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 2 arm calls
New arm: tools/check-spec-tokens.test.sh · a hands-off to a CLOSED sibling, then to an unspecced uid beside a source whose H1 carries no uid · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 2 arm calls
New arm: tools/check-spec-tokens.test.sh · a blank key, and a source dated before the cutoff · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 2 arm calls
New arm: tools/check-spec-tokens.test.sh · a waiver keyed on one edge, then stale, then not reaching another edge · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 3 arm calls
New arm: tools/check-spec-tokens.test.sh · a family-less, tailed target filename in a units sub-folder · FLOOR_ASSERTIONS in tools/check-spec-tokens.test.sh, 1 arm call

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
- **F3** — Which cutoff? Options: (a) 2026-09-14, this spec set's date; (b) 2026-09-08,
  `SPEC_EDGES_CUTOFF`'s date. Measured at rev-1, both select the same 107 bullets, because no other
  live spec carries a hands-off bullet. (b) would also reach a straggler spec dated 2026-09-08 to
  2026-09-13 on another node's branch, which this build never measured. RESOLVED (agent, 2026-09-14,
  delegated): (a). The coverage is equal on every spec this repo holds, and its reach into branches
  nobody measured is smaller.
- **F4** — Where does this unit sit in the build order, and what binds the later passes to its join?
  Options for the order: (a) keep order 39, and run S6 and AC6 in a scratch worktree at a sha where
  the build's specs are live; (b) order 6, sharing the step with unit 6, the pair run in sequence as
  §4 Rollout proves it must be; (c) an order ahead of units 1 to 5. (c) contradicts owner ruling
  D12-i11, which builds units 1 to 5 first, so it is not a run's to take. (a) grades a tree the unit
  does not land on, and leaves every later pass of this build without the join.
  RESOLVED (agent, 2026-09-16, delegated): (b). It grades on the unit's own commit a population
  measured at 81 bullets, and lets AC6's zero-count clause fire. No veto trips: the order verb is this
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
- **F7** — Do the twelve new arms fit the self-test leg's declared figures, or do the figures move?
  Options: (a) keep the 120 s ceiling in `tools/gate-legs.json` and the 130 s budget in
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

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "join a spec's hands-off edge payload
  tokens against the sibling spec that receives them"` returned symbol-name neighbours only
  (`build_edges` in `tools/process-monitor/scope.py`, `join_aliases`, `parse_tokens`) and no seam in
  the spec-tokens feature. The seam was found by reading source instead: this unit extends
  `tools/check-spec-tokens.py`, reusing its LIVE selection, `TICK`, `NOT_A_TOKEN`, the section-6
  bullet shape, the conf-key reader `read_conf_key` and the waiver registry.
- **Against BASE.** `tools/check-spec-tokens.py` and its test are unchanged from BASE to `7804eb7f`.
  The cited lines hold at BASE: `:168` is the any-depth spec population, `:237` is the section-6
  bullet regex, `:254` keys a waiver on the hit's third field, and `:270` and `:279` are the two
  report lines.
- **Against check 12.** The grammar S1 takes is check 12's edge arm in
  `tools/memory-tree/check-memory-hygiene.sh`, unchanged from BASE to `7804eb7f`; §4 The selection
  cites each line. It is reused by copying its regexes into the checker, not by calling the engine,
  for the reason §4 Alternatives rejected gives.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: `python tools/memory-recall/query.py "how are spec edges between sibling units
  checked for agreement" --terms "hands-off consumes-from Edges reciprocity sibling spec join payload
  token check-spec-tokens SPEC_EDGES_CUTOFF edge"`. Top hits: `.memory-tree.conf:268`
  (`SPEC_EDGES_CUTOFF`'s header, whose payload arm is check 12's `external` test and not this join),
  TOOL-aKeyedAnnotation-9 (the paths arm's open defect, untouched here), `memory/HYGIENE.md:135`,
  the aLeakedHandle round-2 review's edge-bullet checklist item, and this build's G4 round-1 record.
