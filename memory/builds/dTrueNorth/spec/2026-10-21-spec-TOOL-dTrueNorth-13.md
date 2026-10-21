# TOOL-dTrueNorth-13 — a design-document subject of a spec audit: its id served bare, and no pin owed for it

**Status:** CLOSED · rev-3 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 3

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-13-deviation-12.md](../build/2026-10-21-build-TOOL-dTrueNorth-13-deviation-12.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-13-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-13-ledger.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-13-1-spec-writer.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-13-1-spec-writer.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-13-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-13-build-brief.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-13-divergence-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-13-divergence-brief.md) | research | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 39 at HIGH**, its item **H6**: spec-audit pins cannot represent a
design-document audit. `TOOL-dTrueNorth-5` S1 refuses, at every round, a spec-kind subject with no
integer `rev` or whose id repeats another subject's, and its S3 prints a `P` row for every unpinned id
of a graded record. The corpus already holds the other input class: dClosedLoop's design audit serves
`PLAY-dClosedLoop-1` over two subjects, v2 and the gap register, neither of which has a `rev` header.
Built as written, such an audit cannot run, or runs on a fake pin that `TOOL-dTrueNorth-4`'s
revision-after-audit arm then reads as a real audit. This unit names the class end to end: the
harness tells a spec subject from a design-document subject by its path, serves a design id bare,
writes the reviewed subjects on a literal line, and the grading owes a pin only for an id whose spec
the record reviewed. It repairs `TOOL-dTrueNorth-5`.

## 2. Scope (IN)

- **S1** — Subject classes in `tools/workflows/tier2-review.template.js` and its render
  `tools/workflows/tier2-review.js`. A spec subject is one whose `path` holds a `builds/<slug>/spec/`
  segment; it carries `id` and `rev` as `TOOL-dTrueNorth-5` S1 requires. Any other subject is a
  design-document subject: it carries `id` in the same grammar, a `rev` on it is refused naming the
  field, and it is exempt from the duplicate-id refusal, which runs over spec subjects only. This
  supersedes `TOOL-dTrueNorth-5` S1's refusal of every subject without a `rev`. Observed by AC1.
- **S2** — `renderAuditBinding(subjects)` renders a spec subject as `<id>@rev-<rev>` and a
  design-document subject as `<id>`, each id once, in first-seen order, and never repeats bare an id
  a spec subject already pins. Observed by AC2.
- **S3** — `renderReviewedLine(subjects)` returns the literal `Reviewed: <path>@<blob>, …` in subject
  order. The spec kind's synthesis prompt instructs it as the record's subjects line where it now
  asks the agent to compose one (`tools/workflows/tier2-review.js:1799-1800`), and the build harness's
  clean-round instruction writes the same literal where it now asks for "a line naming the reviewed
  subjects" (`tools/workflows/unattended-build.js:2550`, `:2566-2567`), in both templates and
  renders. Observed by AC2 and AC3.
- **S4** — The grading in `cmd_print_bindings` (`TOOL-dTrueNorth-5` S3). A record with no
  `Reviewed:` line grades every id, as `TOOL-dTrueNorth-5` S3 states, and `read_reviewed_paths(text)`
  is the one reader of the line. Observed by AC4. For a graded `spec-audit` record whose first twelve
  unfenced lines hold a line opening `Reviewed: `, the paths that line names decide which of the
  record's ids owe a pin, each read at HEAD:
  - when any path the line names has no blob at HEAD, EVERY id of the record owes a pin, exactly as
    a record with no `Reviewed:` line does: a path the grading cannot read cannot show that the
    record reviewed no spec, so the missing path grades toward the pin, never away from it;
  - otherwise an id owes a pin only when a path the line names is a spec file whose H1 defines that
    id, read through `tree_lib.parse_spec_h1` (`tools/memory-tree/tree_lib.py:203`) over that file.
- **S5** — The suites' spec-audit fixtures take spec-shaped paths, because S1 classes a subject by
  its path. Observed by AC5. In `tools/workflows/tier2-review.test.sh` about 30 spec-audit subjects
  carry `rev` on a path with no `builds/<slug>/spec/` segment, spelled `a.md`, `b.md`, `s.md`,
  `m.md`, `u.md`, `v.md`, `one.md`, `two.md` and `three.md`; under S1 each becomes a design subject
  and is refused for its `rev`. The `TOOL-dTrueNorth-5` pin arms from its line 225 give subjects on
  the same paths no `rev` and expect a refusal naming it, which a design subject never meets, so
  those arms would stop refusing. Every spec-audit subject on such a path moves to a path holding a
  `builds/<slug>/spec/` segment, and the resume-probe stubs that name a subject's path follow it.
  The `renderAuditBinding` arm (`tools/workflows/tier2-review.test.sh:233-243`) passes subjects with
  no `path`, which S2 renders bare, so each gains a spec-shaped `path`. In
  `tools/workflows/unattended-build.test.sh` the `MT_ARGS` fixture (line 816), the one fixture there
  that runs the real review harness, carries subject path `s1` plus a `rev`, and moves to a
  spec-shaped path the same way.

## 3. Non-goals (OUT)

- A pin form for a design document, such as its blob. The record already names each blob on its
  `Reviewed:` line, and a new suffix on a Serves token strands every reader that admits only
  `@rev-N`, the class `TOOL-dTrueNorth-9` repairs.
- The cutoff and the in-flight records: `TOOL-dTrueNorth-14`.
- The design-audit preset and its lenses, which dFairHearing's `cl-dClosedLoop-0069` owns.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).
- The build harness's own caller-subject check (`tools/workflows/unattended-build.js:1556-1569`),
  which requires `id` and `rev` on every subject, and its resolver's `rev` refusal (`:1498-1505`):
  both are unchanged, so the build harness keeps auditing spec subjects only, and a design audit runs
  through the review harness directly.

### Edges

- **consumes-from** `TOOL-dTrueNorth-5` — the `id` and `rev` subject fields, `renderAuditBinding`, the clean-round binding line and `cmd_print_bindings`' `P` rows; without them there is no pin to exempt a design subject from
- **hands-off** `TOOL-dTrueNorth-20` — `read_reviewed_paths` reading `Reviewed:` up to the record's first `## ` heading, past S4's twelve-line window (the round-2 spec audit's id 37)

## 4. Design

### Evidence

- `memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md` opens
  `**Serves:** spec-audit PLAY-dClosedLoop-1` and its `Reviewed:` line names
  `…-architecture-v2.md@535c0e05…` and `…-gap-register.md@9a05621f…`, two files under `build/`.
- The harness has two kinds only (`tools/workflows/tier2-review.js:187`), so a design audit runs as
  the spec kind.
- The subjects line is composed by the synthesis agent today: the prompt asks for "a line naming each
  reviewed subject and the blob it was pinned at" (`tools/workflows/tier2-review.js:1799-1800`), and
  the corpus spells it three ways, `Reviewed:`, `Reviewed subjects, each pinned at …` and none, so a
  reader cannot rely on it until the harness renders it.
- `tree_lib.parse_spec_h1(rel, text, memory_root, families)` returns the id a spec file's H1 defines.

### Data model

```
Reviewed: memory/builds/dX/build/a.md@abc1234, memory/builds/dX/spec/2026-10-21-spec-TOOL-dX-1.md@def5678
**Serves:** spec-audit TOOL-dX-1@rev-2 PLAY-dX-1
```

The first line above is the record's subjects line and the second its binding line; in a record the
binding line is line 1, as the harness's ordered opening states.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `renderReviewedLine` | function, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `read_reviewed_paths` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/memory-tree/gen_build_index.py`

### Alternatives rejected

- **Grading a pin only when every subject path is a spec file.** A mixed audit, a spec and the design
  it carries, would then owe no pin for its spec, which is the false pass the pin exists to remove.
- **Telling the classes apart by id.** `PLAY-dClosedLoop-1` is both the design audit's id and a spec
  id in that build, so the id says nothing about the subject.

## 5. Production-readiness checklist

- security — the design subject's `id` is held to the anchored id grammar `TOOL-dTrueNorth-5` S1
  applies, so no newline reaches a prompt line; paths are rendered, not executed.
- perf / scale — one file read per path a graded record's `Reviewed:` line names.
- error / empty / loading states — a record with no `Reviewed:` line grades every id; a `Reviewed:`
  line naming any path with no blob at HEAD grades every id of the record the same way (S4).
- observability — the `P` row names the id and the record as before.
- risks — a hand-written `Reviewed:` line naming a spec it did not review would owe a pin, the safe
  direction.
- testing — AC1 to AC4 as probes, AC5 as greps; the arms under §7.
- migration — none: records before the cutoff are not graded.
- user docs — none; `help/` does not cover record bindings (`TOOL-dTrueNorth-5` §3).

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  as `tools/workflows/tier2-review.test.sh:67-81` cuts it, with `kind: 'spec-audit'`, round 1 and two
  subjects `{path: 'memory/builds/dX/build/a.md', blob: 'abc1234', id: 'PLAY-dX-1'}` and
  `{path: 'memory/builds/dX/build/b.md', blob: 'def5678', id: 'PLAY-dX-1'}`, it proceeds; with
  `rev: 2` added to the first it throws naming `rev`; a subject under `builds/dX/spec/` without `rev`
  still throws naming `rev`.
  Red when: the two design subjects are refused for a missing `rev` or a shared id.
- **AC2** — When the probe calls `renderAuditBinding` on a spec subject `TOOL-x-1` at rev 3 and the two
  design subjects of AC1, it returns exactly `**Serves:** spec-audit TOOL-x-1@rev-3 PLAY-dX-1`, and
  `renderReviewedLine` on the same three returns `Reviewed: ` followed by the three `<path>@<blob>`
  pairs joined by `, `; `grep -c 'renderReviewedLine(subjects)'` finds the call in the synthesis prompt
  of `tools/workflows/tier2-review.js` and `tools/workflows/tier2-review.template.js`.
  Red when: a design id repeats or carries a pin, or the prompt still asks the agent to compose the
  subjects line.
- **AC3** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js`, the shape
  `tools/workflows/unattended-build.test.sh:164-237` uses, ends in a clean round, its `nextAction`
  carries `Reviewed: ` followed by the callee's subjects.
  Red when: the clean-round instruction still asks for an unprefixed subjects line.
  cost: a scratch harness of about 80 lines, modelled on that suite's stub agents.
- **AC4** — When `cmd_print_bindings` runs in-process over a fixture git repository under `%TEMP%`
  whose conf sets `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"` and whose HEAD commits `PLAY-tDoc-1`'s spec
  file and two files under `build/`, a 2026-02-01 record `**Serves:** spec-audit PLAY-tDoc-1` whose
  `Reviewed:` line names those two committed `build/` files prints no `P` row; the same record with
  its `Reviewed:` line naming `PLAY-tDoc-1`'s spec file prints one; the record with no `Reviewed:`
  line prints one; and a missing-path record `**Serves:** spec-audit PLAY-tDoc-1 PLAY-tDoc-2` whose
  `Reviewed:` line names one committed `build/` file and one path absent at HEAD prints two, a `P`
  row for every id the record serves, as the record with no `Reviewed:` line would.
  Red when: the design-only record prints a `P` row, the spec-reviewing record prints none, or the
  missing-path record prints fewer `P` rows than the ids it serves.
  fixture: a fixture repository built as the generator's self-test builds its own.
- **AC5** — When four greps read the two suites' fixture text, each prints 0:
  `grep -cE "path: '[a-z]+\.md'[^}]*rev:" tools/workflows/tier2-review.test.sh`, which prints 24
  today (30 subjects on 24 lines);
  `grep -cE "kind: 'spec-audit'.*path: '[a-z]+\.md'" tools/workflows/tier2-review.test.sh`, which
  prints 21 today and counts the pin arms' subjects with no `rev`;
  `grep -c 'rab(\[{ id:' tools/workflows/tier2-review.test.sh`, which prints 1 today; and
  `grep -c '^MT_ARGS=.*"path":"s1"' tools/workflows/unattended-build.test.sh`, which prints 1 today.
  Red when: any of the four prints a count above 0.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `build-index selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 · two design subjects sharing an id and a mixed binding, staged against the harness TOOL-dTrueNorth-5 left · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · covers AC3 · a clean round whose instruction carries no literal subjects line · that suite's assertion floor, raised by the arms added
New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC4 · a design-only spec-audit record graded against the base predicate that owes every id a pin · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Exempt a design subject by its path, or give it a pin form of its own?** (a) By path, a bare
  id and a literal subjects line the grading reads. (b) A pin form such as `@blob-<sha>`. (b) is a
  token every Serves reader refuses today (`_expand_ids`, `expand_id_runs`), so it strands them, and it
  repeats the blob the subjects line already carries. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the harness and generator edits?** All are governance
  carriers by `PLAY-dClosedLoop-10`'s list, and `cl-dClosedLoop-0005` names every audit of a spec
  record pinning the revision it read, whose subject contract and grading these are. RESOLVED (agent,
  2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the
  spec-audit subject classes, the literal subjects line and the pin grading cl-dClosedLoop-0005 names
  · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 39 (HIGH, item H6).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §2 §3 §4 §5 §6 §10 · the builder's divergence: S4 said an id owes a pin only
  when a named path is a spec file defining it, so a `Reviewed:` path with no blob at HEAD owed none,
  while §5 said that path's id owes one, and AC4 was silent. The run's ruling (a): a named path with
  no blob at HEAD makes every id of the record owe a pin, exactly as a record with no `Reviewed:`
  line. S4 and §5 now state it, and AC4 commits its design-only record's two `build/` files and
  gains the missing-path case. S5 and AC5 move the suites' spec-audit fixtures to spec-shaped paths,
  which S1 otherwise turns into refused design subjects; §3 keeps the build harness's caller-subject
  check unchanged; line citations refreshed against the tree.

## 10. Reuse audit

No existing seam fits the subject classes, and the evidence is the harness itself: its validator
(`tools/workflows/tier2-review.js:349-418`) knows one subject shape, and its kinds are two
(`:187`). The seams extended are `TOOL-dTrueNorth-5`'s: `renderAuditBinding` and its validator,
the clean-round writer of the build harness, and `cmd_print_bindings`; the H1 reader is
`tree_lib.parse_spec_h1`, already the kit's one reader of which spec defines an id.
`python tools/codebase-map/reuse_lookup.py "classify each record binding line and its ids"`, the
phrase `TOOL-dTrueNorth-5` ran, ranked generic name stems and no subject classifier. The recall hit
that disagreed with source was the corpus's subjects line, which three record shapes spell three ways.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
