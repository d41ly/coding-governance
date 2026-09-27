# TOOL-dPinnedHandoff-1 — an external precondition says what the builder does when it is false

**Status:** SPECCED · rev-1 · 2026-09-22 · node d · Tier-2 · base 9b7e2de6 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A `**consumes-from** external` edge names a precondition the unit does not build. It says nothing
about what the builder does when that precondition turns out to be false. The NicoCares handoff
briefs always say it: stop, report the blocker, and do not take the named workaround. This unit
makes such an edge carry an `If false:` clause, graded by shape in hygiene check 12 from a new dated
cutoff, so the builder's disposition is decided at authoring time and not improvised mid-build.

## 2. Scope (IN)

- S1. The spec template gains the rule in its `## §3 Edges` section and in the skeleton's Edges
  example. The template source is `tools/memory-tree/SPEC-TEMPLATE.template.md`, rendered to
  `memory/TEMPLATE-SPEC.md`. Every `**consumes-from** external` bullet carries a clause opening with
  `If false:`, on its first line or on any continuation line. The clause names the disposition and
  the substitute the builder must not take. The same section gains one writing rule: the precondition
  is stated by its exact contract, meaning the header, flag, version or sha, never a paraphrase.
  Observed by AC4.
- S2. Check 12's edge arm in `tools/memory-tree/check-memory-hygiene.sh` reads each bullet as its
  opening line plus its continuation lines. A `consumes-from` bullet whose payload is `external`, in a
  Tier-2 spec whose filename date is on or after `SPEC_HALT_CUTOFF`, reds when that span carries no
  `If false:` marker. Observed by AC1, AC2 and AC3.
- S3. `SPEC_HALT_CUTOFF` is declared blank in the checker's own default and in
  `tools/memory-tree/.memory-tree.conf.example`, where blank means the clause is never required. This
  repo's `.memory-tree.conf` sets it to a date strictly after the landing commit, with the reason
  beside the value. Observed by AC5 and AC6.
- S4. The check 12 entry in `memory/HYGIENE.md` names the clause and its key. The source is
  `tools/memory-tree/HYGIENE.template.md`. Observed by AC4.
- S5. The arm prints its graded count on every full run. When the key is set and zero bullets were
  graded, it prints the announce line the edges arm already prints for the same state. Observed by
  AC5.
- S6. The dry run: before the arm is wired, its predicate runs over every spec in the tree with the
  cutoff forced early. The run prints the bullets graded, the bullets lacking the clause, and the
  near-misses. Observed by AC7.
- S7. The arms of AC1, AC2, AC3 and AC6 are added to the hygiene self-test. NOT OBSERVED as a suite,
  because a suite run is not an acceptance observation from `SPEC_DIRECT_CUTOFF` onward; §7 names
  the suite under `New arm:`.

## 3. Non-goals (OUT)

- Sibling edges, `**consumes-from** <unit-id>`. The order and reciprocity joins already grade them,
  and a sibling's false case is the sibling not landing, which M6's sequencing owns.
- `**hands-off** external` bullets. An outbound handoff is a different shape, the other direction of
  the NicoCares comparison, and it is a follow-up.
- Grading what the clause SAYS. Whether the disposition is legal under M3, and whether the named
  substitute is the tempting one, are the author's questions. The arm grades that the clause exists.
- Requiring a backticked contract token on the bullet. Measured at `9b7e2de6`: 63 of the 68 external
  bullets already carry one within three lines, so an arm would buy almost nothing. The writing rule
  in S1 carries it instead.
- Quoting a unit's `If false:` clauses into its unattended pass brief. That is the unattended kit's
  change to make, and it is handed off below.
- A retroactive sweep of the 68 existing bullets. The cutoff grandfathers them by filename date.

### Edges

- **consumes-from** external — check 12's edge arm as landed at `9b7e2de6`, which parses the verb and
  payload of every Edges bullet one line at a time
  (`tools/memory-tree/check-memory-hygiene.sh:1709-1753`). If false: another build has reshaped the
  arm by build time; re-ground on the landed arm per M7 and put the span reader inside it. Do not add
  a second Edges walker beside it, which would give one bullet two readers that can disagree.
- **hands-off** external — the unattended driver quoting a unit's `If false:` clauses into its pass
  brief, and an outbound-handoff shape for `**hands-off** external`. Neither has a row yet; this
  unit's landing files both in `memory/backlog/TOOL.md`.

## 4. Design

### Data model

```text
- **consumes-from** external — `<the contract, exact>` what this unit takes, and what breaks without it.
  If false: <the disposition> — <the substitute the builder must not take, and why>.
```

The marker is the ASCII string `If false:`, matched case-insensitively as a substring over the
accumulated bullet. That is the rule the failure-mode arm applies to `Red when:`
(`tools/memory-tree/check-memory-hygiene.sh:1352-1377`), so the two clauses share one latitude and
one spelling discipline. Three dispositions occur in practice, and the template names them without
closing the set. The first is M3's park. The second is a `BLOCKED` status with the blocker stated.
The third is a named check that makes the precondition true before the unit proceeds.

### The bullet span

Today the arm reads `L = body[i]` and computes the verb and payload from that one line. The change
keeps that computation and adds an accumulator. From a bullet line, the span collects each following
line until a blank line, the next list marker at column 0, or a heading. The clause test runs over
the span once it closes. That happens at the next bullet, at the next heading, or at the end of the
section, the same three closers the failure-mode arm uses. Only a bullet whose verb is
`consumes-from` and whose computed payload is the bare word `external` is tested.

The population is the edges arm's own. It covers Tier-2 specs past `SPEC_EDGES_CUTOFF`, intersected
with `SPEC_HALT_CUTOFF` on the filename date. So the arm needs both keys armed, and AC1's fixture arms
both. The arm is a SHAPE arm that reads one file, so it stays live under `--staged`, as the Edges
shape arm does.

A finding reads `<file> (§3 **consumes-from** external bullets carrying no If false: clause,
required at/after SPEC_HALT_CUTOFF <date>): <n>`. It names the count and not the bullet text, because
the bullet text is prose of any length.

### Inventory

One conf key is minted, `SPEC_HALT_CUTOFF`, in the shape of its dated `*_CUTOFF` siblings. No
function is minted, because the arm is inline awk inside check 12, as every sibling arm is. The awk
locals carry the arm's existing `eg_` prefix. `sh` is a DARK extension in `.lexicon.conf`, so no
naming cell grades them.

### Migration

None. A blank key is off, and this repo's date sits strictly after the landing commit, so no landed
spec can red. The 68 existing bullets are grandfathered by filename date.

### Rollout

An adopter receives the blank key in the example conf and the rule in the rendered template, so
nothing changes in their tree until they set a date. The memory-tree version move for this build
rides `TOOL-dPinnedHandoff-3`, per the build README.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | the span accumulator, the clause test, the finding, the report line, the key's default |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the arms of AC1, AC2, AC3 and AC6, each staged red first |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the rule in `## §3 Edges`, the skeleton example, the contract writing rule |
| `memory/TEMPLATE-SPEC.md` | REGENERATED from the template; never hand-edited |
| `tools/memory-tree/HYGIENE.template.md` | check 12's entry |
| `memory/HYGIENE.md` | REGENERATED from the template |
| `tools/memory-tree/.memory-tree.conf.example` | the blank key and its comment |
| `.memory-tree.conf` | the key set, with its reason beside the value |
| `memory/backlog/TOOL.md` | at landing, the two follow-up rows §3 Edges hands off |

### Alternatives rejected

- **Grade every `consumes-from` bullet, siblings included.** The order join already reds a sibling
  sequenced after the unit that consumes it, and an `If false:` on a sibling edge would restate M6.
- **A closed disposition vocabulary.** The briefs' dispositions are prose: "stop and ask", and
  "describe it in the PR; do not dress it up". A token vocabulary is satisfied by the token alone,
  which is the witness rule's known weakness a second time.
- **Put the arm in `tools/check-spec-tokens.py`.** That checker is exempt from shipping
  (`tools/govkit/registry.toml`), so adopters would get the rule without the check. The Edges shape
  arm ships in check 12, and this clause belongs beside it.

## 5. Production-readiness checklist

- security: N/A — the arm reads tracked spec text inside an existing pass; no write path, no egress.
- perf / scale: one accumulator per bullet inside an awk pass that already runs; no new process.
- error / empty / loading states: key blank means off. Key set with zero bullets graded prints the
  announce line. A span that never closes is closed by the section's end.
- observability: the graded count prints on every full run, so a zero is visible, not assumed.
- risks: a span swallowing the next bullet's text would let a neighbour's clause satisfy it. The
  closers and AC3's adjacency fixture pin that.
- testing: each self-test arm is observed red on a staged break before it is kept.
- migration: none; the cutoff grandfathers the corpus.
- user docs: the rendered template and `memory/HYGIENE.md` are the docs. This repo has no `help/`.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-tree/check-memory-hygiene.sh` runs over a fixture tree holding a
  Tier-2 spec dated on the cutoff, with a `**consumes-from** external` bullet and no `If false:`
  clause, it names that spec and the string `If false:`.
  Red when: the spec is not named.
  fixture: a scratch tree the self-test builds, whose conf arms both `SPEC_EDGES_CUTOFF` and
  `SPEC_HALT_CUTOFF`. The arm sits inside the edges population, so a blank `SPEC_EDGES_CUTOFF` would
  leave it grading nothing while looking armed.
- **AC2** — When the same fixture carries the clause on the bullet's second continuation line, in
  lower case, `tools/memory-tree/check-memory-hygiene.sh` does not name the spec.
  Red when: it names the spec.
- **AC3** — When the fixture carries the clause-less shape on a `**consumes-from** <unit-id>` bullet,
  on a `**hands-off** external` bullet, in a spec dated the day before the cutoff, and in a Tier-1
  spec, `tools/memory-tree/check-memory-hygiene.sh` names none of them. It also names none when a
  clause-less external bullet is followed directly by a bullet whose span carries `If false:`, and it
  names the first.
  Red when: any of the four is named, or the adjacent pair is graded as one span.
- **AC4** — When `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` are re-rendered from their
  templates, the first carries `If false:` in its `## §3 Edges` section and in its skeleton, and the
  second names `SPEC_HALT_CUTOFF` in check 12.
  Red when: either file lacks its token, or a fresh render differs from the committed copy.
- **AC5** — When `.memory-tree.conf` sets `SPEC_HALT_CUTOFF` and the checker runs over this tree,
  the report prints the arm's graded count.
  Red when: no count line is printed, or the count is a literal rather than a count of what the run
  graded.
  figure: DERIVED at observation time.
- **AC6** — When the key is blank in the fixture conf, `tools/memory-tree/check-memory-hygiene.sh`
  names no spec for a missing clause.
  Red when: any spec is named.
- **AC7** — When the arm's predicate runs over a scratch clone of this tree whose
  `.memory-tree.conf` sets `SPEC_HALT_CUTOFF` to `2026-01-01`, it prints the external bullets
  graded, those lacking the clause, and the near-misses. A near-miss is a span that says what happens
  without the precondition in other words. The output is recorded in this build folder before the arm
  is wired.
  Red when: the graded count is zero, which would mean the span reader matched nothing.
  cost: a scratch clone and one checker run, minutes.
  figure: DERIVED at run time. The rev-1 count, 68 external bullets, is PINNED at `9b7e2de6` on
  2026-09-22 and is a sanity bound, not the assertion.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

`kit/dogfood doc parity` is the leg this unit arms: its guard names `memory/TEMPLATE-SPEC.md` and
`memory/HYGIENE.md`, and this unit edits both templates and both rendered copies. `recall floor` and
`recall floor arms` carry the guard `memory/`, which every `memory/` path in Files touched sits
under. `memory-hygiene self-test` is held by default, so the Definition of Done reaches it only
through the post-build run the build method schedules.

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · AC1's clause-less fixture, AC2's
continuation fixture, AC3's four non-graded shapes and adjacency pair, AC6's blank key · the suite's
printed count rises by the arms added, and its pinned floor moves with it where one is pinned

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, from the comparison of the three NicoCares handoff briefs with
  this template; the build README states the source.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "require a clause on a spec Edges bullet that consumes an
external precondition"` returned no seam this unit can extend. Its candidates share a name stem and
nothing else: `require_adopted_root` in `tools/codebase-map/map_lib.py` and `build_edges` in
`tools/process-monitor/scope.py`. Its scan coverage names `.sh` as the unscanned layer, which is where
the seam actually is. The seam this unit extends is check 12's edge arm
(`tools/memory-tree/check-memory-hygiene.sh:1709-1753`), which already computes the verb and payload
of every Edges bullet. The span rule is copied from the failure-mode arm
(`tools/memory-tree/check-memory-hygiene.sh:1352-1377`), not reinvented.

Recall terms used: `python tools/memory-recall/query.py "was a halt rule on external edges, a
do-not-touch path list checked against the diff, or a runnable grep invariant as acceptance
considered before, and what decided the Edges block and the acceptance witness shape" --terms "Edges
consumes-from external precondition witness Red-when Files-touched guard join invariant grep frozen
shape-only"` — 40 hits. The load-bearing one is the unit that introduced Edges,
`memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md:204`. None of the hits
proposes a disposition clause.
