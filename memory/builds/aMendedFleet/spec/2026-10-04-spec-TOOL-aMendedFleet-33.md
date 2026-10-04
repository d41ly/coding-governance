# TOOL-aMendedFleet-33 — the recall README and Skill stop typing corpus figures, and a miss re-queries before grep

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 33

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The recall README sizes this repo's corpus at 66 files, 496,153 bytes, 9 records and 1,033 chunks,
and its Skill tells a caller that on "a small corpus" grep is faster and "returns half the tree", so
a miss should fall straight back to grep. The corpus is now about 2,770 files and 46 MB, the index
holds over 2,000 records and 90,000 chunks, and a miss is most often a vocabulary miss that a second
query in the record's own words recovers. This unit deletes the typed figures, points at the counts
the CLI prints on every query, and makes the miss advice "re-query in the record's vocabulary, then
grep".

## 2. Scope (IN)

- **S1** — The README `Notes` bullet that opens "On a small corpus, retrieval buys precision, not
  speed" loses every typed figure about this repo's corpus and timing. What stays is the claim the
  tree still bears out: a warm query is not faster than a full grep, and what it buys is a ranked
  list. It points at the `index <records> records + <chunks> chunks` line every query prints, and at
  `--stats` given beside a question, for the live counts. Observed by AC1 and AC4.
  **Readers:** by name: `tools/memory-recall/README.md` alone spells these figures. by value:
  NO VALUE READERS — prose figures nothing computes from.
- **S2** — The Skill's "A miss is ordinary" paragraph, edited in
  `tools/memory-recall/SKILL.template.md` and re-rendered into `.claude/skills/memory-recall/SKILL.md`,
  drops "small corpus" and "half the tree" and says: on thin or wrong hits, re-query once with
  terms in the vocabulary the missing record would use, an id family, a flag key, a file name, and
  only then grep the memory root. Observed by AC1, AC2 and AC3.
  **Readers:** by name: `tools/memory-recall/SKILL.template.md` and its render
  `.claude/skills/memory-recall/SKILL.md` spell the paragraph. by value: NO VALUE READERS — the
  Skill is read by agents, and nothing parses the paragraph.
- **S3** — The README's file table cell for `recall-opened.test.sh` stops typing "8 cases" and
  points at the `passed` line the test prints, as the `selftest.py` cell already does for its
  checks. Observed by AC4.
  **Readers:** by name: `tools/memory-recall/README.md` alone spells the count. by value:
  NO VALUE READERS — the test computes its own count and reads nothing from the README.

## 3. Non-goals (OUT)

- Figures attributed to the upstream project: the rewrite's recall@20 0.71 to 0.84, the 115 MiB
  per worktree and 37.9% evictable. They are pinned history of another corpus, labelled as such.
- The recall-floor figures, `h=10`, `R=12` and the pin's derivation. Those belong to the floor's
  own unit of this build, unit 28.
- Typed defaults that are correct, the `--k` default of 20 and the budget. Unit 31 rewrites the
  paragraph that types the budget.
- The README eviction paragraph and the conf comment's cache-size figure, which unit 32 rewrites.
- The memory-recall kit version bump, owed once at this build's close after the last move.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; the three files are byte-identical at `580dc980e`, re-verified 2026-10-04
with `git diff --stat`.

- `tools/memory-recall/README.md` lines 255 to 261 carry the figures S1 removes, and
  `tools/memory-recall/SKILL.template.md` lines 53 to 55 the paragraph S2 rewrites; the rendered
  Skill carries the same two lines.
- Re-measured on 2026-10-04, PINNED: `git ls-files memory` names 2,776 markdown files of 46,466,714
  bytes; this worktree's cache manifest records 2,153 records and 93,399 chunks before a rebuild and
  the next query printed 2,163 and 93,707; `grep -rIl "adopt" memory/` takes 0.55 s wall and lists
  1,719 files; a warm query took 0.69 s wall. The README's qualitative claim, that grep is not
  slower, still holds; every figure beside it is stale.
- The report's "`--stats` does not exist" is half true: `--stats` is a known flag that prints the
  cache manifest, but only beside a question. Alone it exits 2 with "no question given". S1 says
  "beside a question".
- The `recall-opened.test.sh` cell's "8 cases" is correct today, eight scenarios and 16 `ck`
  assertions, and `TOOL-aProbedToolkit-14` checked it correct on 2026-09-03. It goes under the
  repo's rule that no count of a derived population is typed in prose, the same move
  `TOOL-dHashedPrelude-3` made for the selftest cell.

### Files touched (estimate)

- `tools/memory-recall/README.md`
- `tools/memory-recall/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md`

### Rollout

This unit builds after units 31 and 32, which also write `tools/memory-recall/README.md`, and unit
31 writes the Skill paragraph above S2's. The rendered Skill is regenerated with
`adopt-memory-recall.sh --scaffold`, never hand-edited.

### Alternatives rejected

- **Re-measure and re-type the figures.** They would be stale on the next corpus edit, which is how
  these went stale.
- **A `--stats` mode that runs without a question.** It is a new CLI surface for a figure every query
  already prints on its first line.

## 5. Production-readiness checklist

- security — N/A — documentation only.
- perf / scale — N/A — no code path changes.
- error / empty / loading states — N/A — no code path changes.
- observability — the docs point at the `index` line the CLI already prints.
- risks — the new miss advice costs one more query before grep; the Skill bounds it at one.
- testing — the Skill render check and greps over the three files.
- migration — N/A — no stored data.
- user docs — this unit is user docs, S1 to S3.

## 6. Acceptance criteria

- **AC1** — When `grep -n -E "small corpus|half the tree|496,153|1,033 chunks|66 tracked" tools/memory-recall/README.md tools/memory-recall/SKILL.template.md .claude/skills/memory-recall/SKILL.md`
  runs, it prints nothing.
  Red when: any of the stale phrases or figures survives in any of the three files.
- **AC2** — When `grep -n "re-query" .claude/skills/memory-recall/SKILL.md` runs, it hits the miss
  paragraph, and that paragraph names the record's own vocabulary before it names grep.
  Red when: the paragraph still sends a miss straight to grep.
- **AC3** — When `bash tools/memory-recall/adopt-memory-recall.sh --check` runs after the render, it
  exits 0.
  Red when: the rendered Skill was hand-edited or not re-rendered from the template.
- **AC4** — When `grep -n -E "8 cases|--stats" tools/memory-recall/README.md` runs, it prints no
  "8 cases" line, and the `--stats` hit sits in the `Notes` bullet saying it prints the manifest
  beside a question.
  Red when: the typed count survives, or the bullet points at no live count.

## 7. Gates

`memory-recall skill wiring` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`check-wiring self-test` and `lexicon naming predicates` are owed by the rendered Skill under
`.claude/`. `memory-recall kit selftest` runs at the close: its guard, `tools/memory-recall/`, is
excluded as broad, and its Skill-drift arm reads the same render.

## 8. Open questions

- **F1 — Does the correct "8 cases" count go too?**
  Options: keep it, since it is not stale; remove it under the rule against typed derived counts.
  The brief's subject is stale typed figures, and the repo's rule covers correct ones too, which
  `TOOL-dHashedPrelude-3` already applied to the sibling cell.
  RESOLVED (agent, 2026-10-04, delegated): remove it and point at the test's own summary, S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the README, the Skill template and a re-measure of the
  corpus.

## 10. Reuse audit

No code seam applies: the unit edits prose, and the pointer it adds names output the CLI already
prints, the `index` line in `main` of `tools/memory-recall/query.py`. `python
tools/codebase-map/reuse_lookup.py "documentation stating measured figures that go stale, replaced
by a pointer at the derived count"` returned `derive_*` name-stem neighbours only, none of which
renders documentation, so no existing seam fits. Recall named `TOOL-aProbedToolkit-14`, the open ask
on drifted README counts that checked "8 cases" correct, and `TOOL-cBriefedPilot-29`, a row that
stopped restating figures for the same reason. Where the report and the tree disagree: `--stats`
exists, beside a question only, and a warm query is still slower than grep, so only the figures and
the two phrases are stale.

Recall terms used: `python tools/memory-recall/query.py "which recall README and Skill figures are
stale and what should a miss tell the caller to do" --terms "memory-recall README SKILL.template.md
small corpus grep faster half the tree miss stale figures --stats manifest counts"`
