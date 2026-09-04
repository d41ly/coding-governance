# TOOL-aStagedLane-4 — the carriers name the classifier and the attended route

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The method's detect step tells a run to read the build README's units table and classify by hand,
while a working classifier sits in the driver and answers the same question in one command. Name it
where the method already discusses detection, and declare the attended harness route in the same
pass, so what the preceding units build is reachable without reading their source.

## 2. Scope (IN)

- **S1** — the detect paragraph of the build method names the plan verb as the way to obtain a
  unit's state, without the mandate qualifier the guide's only current mention carries. The
  classifier runs with no run-state file, measured on this node against a build that never had one.
- **S2** — the passes paragraph of the same guide names the harness as the route for spec and build
  passes, and names its two modes, so a session that is not under a mandate knows the route exists.
- **S3** — both halves of the byte-compared pair move in one commit:
  `tools/memory-tree/BUILD-METHOD.template.md` and the rendered `memory/guides/BUILD-METHOD.md`. The
  `kit/dogfood doc parity` leg compares them, so editing one alone reds the bar.
- **S4** — `memory/project/method-carriers.txt` keeps its existing row for the harness. That row
  classifies the file as a pointer that states no rule the method does not, and the attended mode
  must not change that classification. If unit 2's header additions make it state a rule, the row is
  re-classified in this unit rather than left disagreeing.
- **S5** — the charter's merge-bar section gains one sentence naming the pass-order leg's widened
  population, because the current text describes a leg that grades unattended builds only.

## 3. Non-goals (OUT)

- Not restating the classifier's grades in the method. The four states and their precedence are the
  driver's, and a second spelling is a second answer.
- Not restating the harness's mode semantics. Unit 2's file header owns them; this unit points.
- Not editing the rendered protocol guide. It documents the mandate contract, which none of these
  units changes.
- Not adding a new carrier file. Every claim here lands in a document that already exists.
- Not spending charter headroom on prose. The charter edit is one sentence, and the size gate prices
  every growth against a recorded high-water.

## 4. Design

### Why the carriers are a separate unit

The preceding three units each change behaviour, and each would otherwise carry a fragment of the
same document edit. Splitting the documents into one unit keeps the byte-compared pair moving in a
single commit, which is what the parity leg requires, and leaves each behaviour unit with one
mechanism as the decompose rule demands.

### Why this unit lands last

A carrier declares what exists. Landing the declaration before the behaviour would put a document in
the tree describing a route the tree does not have, which is the drift class this repository audits
for.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md`, `AGENTS.md`, and
`memory/project/method-carriers.txt` only if S4's re-classification proves necessary. Three files,
possibly four.

### Alternatives rejected

Folding these edits into the units that motivate them was rejected: the byte-compared pair would then
be edited by two units in two commits, and the parity leg reds between them.

Leaving the method silent and relying on the harness's own header was rejected because a session
that does not already know the harness exists never reads that header.

## 5. Production-readiness checklist

- security — N/A. Document edits only.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No runtime surface.
- observability — N/A.
- risks — the live one is the charter size gate. The edit is one sentence and is priced against the
  recorded high-water before it is written.
- testing + left-shift gates — the parity leg and the method-carriers leg both already exist and
  both grade these files; no new gate is needed and none is added.
- migration / rollback — reverting restores the current text exactly.
- user docs — this unit IS the docs change.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-method-carriers.sh` runs after the edits, it exits 0
  and reports no undeclared pointer.
- **AC2** — When the `kit/dogfood doc parity` leg runs, the template and the rendered guide compare
  equal, proving both halves moved in this commit.
- **AC3** — When `bash tools/check-template-size.sh` runs, it exits 0 and the charter stays inside
  its ceiling with the growth priced against the recorded high-water.
- **AC4** — When the detect paragraph of `memory/guides/BUILD-METHOD.md` is read, it names the plan
  verb without a mandate qualifier, and the guide contains no second spelling of the four unit
  states.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tree, it exits 0.

## 7. Gates

`bash tools/memory-tree/check-method-carriers.sh`, the `kit/dogfood doc parity` leg named in
`tools/gate-legs.json`, `bash tools/check-template-size.sh`, and
`bash tools/memory-tree/check-memory-hygiene.sh`. The full bar is
`bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does unit 2's mode documentation turn the harness from a pointer into a rule-stater?** The
  carriers file currently classifies it as a pointer that states no rule the method does not. A
  header describing which refusals attended mode omits may cross that line.
  Options: keep the header short enough to stay a pointer and put the mode semantics in the method;
  re-classify the row and accept the harness as a rule carrier; split the description across both.
  Recommendation: keep it a pointer and let the method carry the semantics. A rule with two carriers
  is the drift shape this repository already pays to detect.

- **F2 — should the charter sentence in S5 be spent at all?** The charter has a hard ceiling and the
  pass-order leg is already described there in terms that will be wrong after unit 1.
  Options: correct the sentence in place, which costs nothing net; add a new sentence; delete the
  charter's description and point at the manifest.
  Recommendation: correct it in place. The existing sentence becomes false when unit 1 lands, so
  leaving it is not an option, and correcting it spends no headroom.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "classify units MISSING THIN FORKED READY for an attended
build"` returned `build_reference_index` in `tools/codebase-map/map_lib.py` and `classify` in
`tools/memory-tree/check-arms.py` among its candidates, both matched on name stem and neither related
to unit classification in a build. The corpus is Python symbols and the classifier this unit points
at is a shell function, so the tool could not have found it. The seam found by reading is the plan
verb in `tools/unattended/unattended.sh`, which already computes the classification and already runs
without a run-state file, and the method-carriers registry, which already holds a row for the
harness; this unit adds no mechanism and reuses both.

Recall terms used: `M2 detect roster units region plan_state classifier BUILD-METHOD carrier
attended mandate restate`. The query was what the method's detect step tells an attended run to use;
it returned 40 hits, and the binding one is the parent build's spec-audit finding that the method
states its grading in terms the classifier had abandoned, which is the same carrier-drift class this
unit exists to keep closed.
