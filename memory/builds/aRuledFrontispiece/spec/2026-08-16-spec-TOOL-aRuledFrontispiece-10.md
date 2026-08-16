# TOOL-aRuledFrontispiece-10 — the corpus retrofit and the kit version bump

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Make the slot contract true of the corpus rather than only of builds opened after it. Every tracked
build README is retrofitted, with no filename-date cutoff grandfathering any of them, because the
owner declined one. `KIT_MEMORY_TREE_VERSION` moves once here, in the last commit of the build that
touches the verdict-epoch scan set, and its seven mirrors move with it.

## 2. Scope (IN)

- **S1** — sequencing, as a deliverable rather than as an intention. The generator changes, their
  arms and the format leg land in their own units' commits BEFORE any README is re-rendered. The
  re-render is then a commit whose entire diff is machine-derivable, and a reviewer reads
  `python tools/memory-tree/gen_build_index.py --check` output against it rather than reading a
  corpus-wide diff.
- **S2** — the authored retrofit, which is two operations on authored bytes and therefore one
  commit landing BEFORE the re-render. First, the 12 build READMEs that carry a roster table and no
  marker pair get `<!-- roster:units -->` and its close around that table. Second, the six READMEs
  that violate unit 1's slot order get their prose blocks MOVED so that all authored prose sits
  between the title and the plan slot. Both sets are measured 2026-08-16 and named in §4, and both
  are reviewed file by file — without this commit the re-render is not the pure one S1 promises.
- **S3** — the re-render. `python tools/memory-tree/gen_build_index.py --write` over the whole tree,
  in one commit, changing no byte a human wrote.
- **S4** — the bounded prose block gets the refusal discipline `strip_records_sentence` at
  `tools/memory-tree/gen_build_index.py:396` already carries: more than one candidate is a refusal
  naming every line, and an anchor the bounding pattern does not fully match is a refusal too. A
  mis-bounded README stops the render; it is never rewritten on a guess.
- **S5** — `KIT_MEMORY_TREE_VERSION` moves 2.16 to 2.17 at the constant plus its seven mirrors, in
  one commit. Three mirrors are re-rendered by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` rather than hand-edited.
- **S6** — the generator's `--selftest` gains an arm that drives a fixture carrying the RETROFITTED
  shape — the plan pair present, the generated regions present — through `--write` and then
  `--check`, asserting the second run is clean. The existing fixed-point arm covers the pre-retrofit
  shape only.
- **S7** — no cutoff, and the absence is recorded rather than assumed. `SPEC_FORMAT_CUTOFF`,
  `SPEC10_CUTOFF` and `STREAMS_CUTOFF` all grandfather by filename date; this retrofit adds no
  fourth knob of that kind, so a build README's age never exempts it.
- **S8** — the landing rule. Build READMEs carry no merge driver, so the retrofit is landed as a
  reconcile-then-push in one sitting, and a conflict inside a generated region is resolved by
  re-running `--write`, never by choosing a side.
- **S9** — no artifact count, README count or arm count is written into any record this unit lands.
  Each is read from the gate that derives it. `--check` reported `clean (42 artifact(s))` at
  `base 96141aed`, and that number is a measurement with a date on it, not a constant.

## 3. Non-goals (OUT)

- Making the `<!-- roster:units -->` pair mandatory. Forks 1 and 5 both point at opt-in, and
  requiring it is `TOOL-cBriefedPilot-7`'s territory on another node.
- Authoring a unit plan for a build that has none. The retrofit WRAPS a roster table that already
  exists; 26 of the 39 build READMEs have no roster heading at all, and each of those keeps unit 1
  S5's no-pair branch rather than gaining an invented or empty plan.
- Rewriting prose. S2 relocates whole blocks; it does not edit sentences, retitle headings or
  summarise.
- Changing what renders inside `<!-- gen:build-index -->`. Check 8 of
  `tools/unattended/check-unattended.sh` byte-compares that slice against the
  `<!-- run:generated -->` slice of every sibling `RUN.md`, and two of those exist.
- Retrofitting anything outside `memory/builds/*/README.md`. Guides, specs, `memory/README.md` and
  the map are untouched.
- Bumping any other kit version. `KIT_UNATTENDED_VERSION` moves only if unit 8 changes that kit's
  engine, and that is unit 8's to declare.

## 4. Design

### Inventory

The version value has eight spellings. Seven are mirrors of the constant, and they are not equally
defended — the gate column is the load-bearing one, because a mirror nothing compares is a mirror
that goes stale silently.

| Spelling | Gated by |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh:13`, the constant | `tools/check-kit-versions.sh` presence check; `check-verdict-epoch.sh` parses it |
| the same line's `gov:kit memory-tree@` marker | NOTHING — verified against source, see below |
| `tools/memory-tree/HYGIENE.template.md:1` | `check-kit-versions.sh`, derived template loop |
| `tools/memory-tree/BUILD-METHOD.template.md:1` | the same loop |
| `tools/memory-tree/SPEC-TEMPLATE.template.md:1` | the same loop |
| `memory/HYGIENE.md:1` | `kit-dogfood-parity.test.sh`, transitively |
| `memory/TEMPLATE-SPEC.md:1` | the same |
| `memory/guides/BUILD-METHOD.md:1` | the same |

`check-kit-versions.sh` compares the constant against every tracked
`tools/memory-tree/*.template.md` marker and against nothing else in this kit. The marker sharing
the constant's own line is therefore unchecked, even though the same file asserts exactly that
pairing for `agent-cap.js` and `settings-merge.py`. Closing it is a one-line addition to that gate
and is NOT in this unit's scope; what this unit owes is that the miss cannot happen silently here,
which AC5 buys with a grep over the live carriers.

The three live copies are gated only through the render: `kit-dogfood-parity.test.sh` substitutes
`{{KIT_DIR}}` and `{{TOOL_ROOT}}` into each template and byte-compares the result against the
installed copy. So a template bumped without a `--render` reds, and a live copy hand-edited to the
new number without its template also reds. Neither can be bumped alone.

### Migration

The corpus is 39 tracked `memory/builds/*/README.md` files, measured 2026-08-16 with
`git ls-files`. Thirteen carry a roster or units heading and 26 do not, so the plan pair is added to
13 files and one of those, `aStandingWrit`, already has it. Separately, 33 of the 39 already satisfy
the slot order unit 1 declares. Six do not:

| README | What violates the order |
|---|---|
| `memory/builds/aRuledFrontispiece/README.md` | 65 non-blank lines of prose after the closing generated marker |
| `memory/builds/aSiftedPlaybook/README.md` | 120 non-blank lines of prose after the closing generated marker |
| `memory/builds/aTimedTurnstile/README.md` | 10 non-blank lines of prose after the closing generated marker |
| `memory/builds/cKeyedLaunchpad/README.md` | 11 non-blank lines of prose after the closing generated marker |
| `memory/builds/cTracedPromise/README.md` | 23 non-blank lines of prose after the closing generated marker |
| `memory/builds/aStandingWrit/README.md` | 74 non-blank lines of prose between the plan pair's close and the generated open |

This falsifies unit 1 §4 Migration, which states that every build README today has its slots in the
required order and that none carries a `roster:units` pair. `aStandingWrit/README.md:90-104` carries
one, added by `TOOL-aStandingWrit-1` S8, and it is the file whose slots are out of order. Unit 1
asked this unit to verify that sentence over the corpus rather than trust it; the verification is
negative, and the consequence is an ordering one rather than a design one — a refusal reachable from
`plan()` reds hygiene check 9 on six live files the moment unit 1 lands. Either those six are
restructured inside unit 1's own commit, or unit 1 keeps the slot refusal off the corpus path until
this unit's S2 commit lands. This spec does not pick between those; it states that one of them must
be true and that AC1 is the observation.

Prose relocation costs the render nothing: for a build README the rendered artifact IS the file with
one region replaced, so moving authored bytes is a fixed point of `--check` on the same run.

The retrofit removes no bytes. That constraint is why S4 copies the shape at
`gen_build_index.py:396` rather than writing a new bounding rule: that function already refuses on
more-than-one-match and on an anchor whose sentence does not close, having learned both the
expensive way, and both refusals are exactly what a prose block bounded by position rather than by
markers needs. A bounding predicate that guesses is a data-loss path over 39 files at once.

The recurring class here is `gate-green-by-accident-on-generated-bytes`. Its fix has two halves and
both are already present: `.gitattributes` pins `memory/**/*.md text eol=lf` so the committed bytes
are LF, and `read_text` in the generator decodes and replaces CRLF before any comparison, so a
Windows checkout cannot red a correct tree. Neither half is added here — both are asserted, because
a retrofit is exactly the moment a half-present fix looks green. The generator's selftest already
carries a write-then-check fixed-point arm; S6 adds a second one over the retrofitted shape, since
the existing arm's fixture has neither a plan pair nor the new regions.

### Rollout

Three commits, in this order, all after units 1 through 6 have landed.

1. **A — the authored retrofit.** The 12 marker insertions and the six files in the table above.
   Reviewed as prose, by eye. Touches nothing in the verdict-epoch scan set.
2. **B — the version bump.** The constant and its same-line marker at
   `tools/memory-tree/check-memory-hygiene.sh:13`, the three templates, then
   `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` for the three live copies. Reviewed
   as an eight-line diff.
3. **C — the re-render.** `--write`, then `--check`. Reviewed as `--check` output.

Commit B must be the NEWEST commit in the range that touches
`tools/memory-tree/check-memory-hygiene.sh` or any of the six delegates
`check-verdict-epoch.sh` scans. The gate's rule is topological: the newest behaviour-bearing engine
change must be an ancestor of, or equal to, the newest commit that changes the constant's value. B
satisfies it by being both. Commit C touches no scanned file, so it cannot displace B. A generator
fix landing AFTER B — the plausible case, because C is where the corpus first meets the new
renderer — moves the newest engine change past the bump and reds the leg; the remedy is to fold that
fix into B before it lands, or to bump again, and the second is the one this build's rule against a
mid-build bump exists to avoid.

Landing is positional. `git check-attr merge -- memory/builds/aStandingWrit/README.md` reports
`unspecified`, so the row-keyed driver that protects `memory/DECISIONS.md` and the backlog shards
does not cover build READMEs — git's built-in three-way text merge does, across 39 files at once.
Every spec status header on any node is an input to its own build's rendered region, so a concurrent
node landing one spec makes commit C's rendered bytes stale for that build and produces a textual
conflict inside a generated region. The rule in S8 follows: fetch, rebase, re-run `--write`, push,
in one sitting; and resolve any conflict inside a generated region by re-rendering rather than by
picking a side, because both sides are outputs and neither is evidence.

### Files touched (estimate)

Commit A: at most 17 build READMEs, the 12 wrapped and the six restructured overlapping in
`aStandingWrit`. Commit B: `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/HYGIENE.template.md` · `tools/memory-tree/BUILD-METHOD.template.md` ·
`tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/HYGIENE.md` · `memory/TEMPLATE-SPEC.md` ·
`memory/guides/BUILD-METHOD.md`. Commit C: every `memory/builds/*/README.md`, plus
`memory/LIVE.md` and the ledger shards if any build's derived status moved. Ahead of all three:
`tools/memory-tree/gen_build_index.py` for S4 and S6, and one row in `memory/DECISIONS.md`.

### Alternatives rejected

A filename-date cutoff, the mechanism `SPEC_FORMAT_CUTOFF` and `SPEC10_CUTOFF` already provide for
specs. It is the cheapest option and the owner declined it. Recorded because it will be proposed
again: a cutoff would leave the corpus permanently two-shaped, and the format gate in unit 6 would
then have to carry the cutoff too, which is a second knob for a corpus of 39 files.

Landing the bump and the re-render in one commit. Rejected because it destroys the reviewability
property S1 exists for: the eight version lines would be indistinguishable, in a diff, from the
mechanical output of the renderer.

Restructuring the six non-conformant READMEs mechanically, by relocating everything after the
closing marker to just above it. Rejected because the correct destination differs per file — the
method section in `cKeyedLaunchpad` and the owner decision menu in `cTracedPromise` are not the same
kind of block — and a mechanical move produces a document whose reading order no author chose.

## 5. Production-readiness checklist

- security — N/A. No new input crosses a trust boundary; every file read is tracked and read today.
- perf / scale — one `--write` over the corpus, the same pass the gate already runs on every push.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Markers and version strings are ASCII literals.
- error / empty / loading states — a build with no roster table, an empty prose block, and a build
  folder whose only record is its README each render unchanged; each is an arm.
- observability — every refusal names the file and the line, and the version bump is observable as a
  single grep over the live carriers.
- risks — the bounded prose rewrite is the single highest-risk item in this build. It writes 39
  authored files in one commit, and a mis-bounded block is deleted authored text that `--check` then
  agrees with forever, because the file is its own render's input. S4's two refusals are the whole
  mitigation, and they must stop the render rather than repair it.
- testing + left-shift gates — the new fixed-point arm over the retrofitted shape, plus the format
  leg from unit 6 running over the real corpus for the first time at commit C.
- migration / rollback — commit C reverts as one revert and restores the previous rendered bytes;
  commit B reverts as an eight-line revert plus a `--render`; commit A reverts as a prose revert.
  Reverting C alone leaves the version claiming an epoch the corpus no longer matches, so C and B
  revert together or not at all.
- user docs — the slot contract lands in `memory/HYGIENE.md` and its kit template in unit 1; this
  unit only carries their version markers.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at commit A's tip, it
  reports clean, and every one of the six READMEs named in §4 satisfies the slot order unit 1
  declares, with `git grep -c '<!-- roster:units -->' -- 'memory/builds/*/README.md'` returning a
  hit in each of the 13 files that carry a roster and in none of the other 26.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --write` runs at commit C and
  `git diff --stat` is read, no line outside a generated region and outside the `ids:` front-matter
  line differs from commit B's tree.
- **AC3** — When a fixture README puts a second candidate prose block outside the bounded slot,
  `--check` fails naming both line numbers, in the shape `strip_records_sentence` already uses for
  a multi-match refusal.
- **AC4** — When a fixture README's bounded prose block is opened and not closed, `--check` refuses
  and writes nothing, proved by asserting the fixture's bytes are unchanged after the failed run.
- **AC5** — When the bump lands, `git grep -l 'gov:kit memory-tree@2.16'` over the five live
  carriers — `tools/memory-tree/check-memory-hygiene.sh`, the three
  `tools/memory-tree/*.template.md` files, and the three installed copies under `memory/` — prints
  nothing, and `bash tools/check-kit-versions.sh` exits 0.
- **AC6** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the bump, it exits 0
  without needing `--render`, proving the three live copies were re-rendered rather than hand-typed.
- **AC7** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs at commit C's tip, it prints
  `clean` and names commit B as the commit in which the version moved.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the new arm over the
  retrofitted fixture passes and the total arm count is strictly greater than at `base 96141aed`.
- **AC9** — When `git check-attr eol -- memory/builds/aStandingWrit/README.md` runs after the
  retrofit, it reports `lf`, and a second consecutive `--check` on an unmodified tree is clean.
- **AC10** — When `bash tools/unattended/check-unattended.sh` runs at commit C's tip, check 8 passes
  for both tracked `RUN.md` files, proving the retrofit changed no byte inside
  `<!-- gen:build-index -->`.

## 7. Gates

`bash tools/run-gates.sh` in full, because this unit is the build's landing commit. The legs that
can only be judged here: `verdict epoch (kit version dates the engine)` · `kit version markers` ·
`kit/dogfood doc parity` · `memory hygiene (20 checks)` for check 9 over the re-rendered corpus ·
`build-index selftest` · `marker contract (4 readers)` · `unattended kit gate` for check 8 ·
`codebase-map coverage + freshness`. Before the review,
`python tools/memory-tree/gotchas.py --for-diff 96141aed..HEAD` names the classes this diff can hit;
`gate-green-by-accident-on-generated-bytes` is the one already known.

## 8. Open questions

none — forks 3, 5 and 7 at the build README resolved the three this unit would otherwise have asked,
and the owner's refusal of a grandfather cutoff resolved the fourth. The one live cross-unit
conflict is a FALSIFICATION of unit 1's migration claim rather than a fork, and §4 carries it with
the measurement and the two ways out.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `retrofit corpus generated
region marker kit version bump verdict epoch byte compare eol pin fixed point render parity`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| refuse an anchored rewrite that is ambiguous | `strip_records_sentence` at `gen_build_index.py:396` | REUSE THE SHAPE — both refusals, applied to the bounded prose slot |
| splice into a named marker pair | `apply_region` at `gen_build_index.py:493`, parameterised by unit 1 | REUSE as unit 1 leaves it; this unit adds no marker machinery |
| re-render a shipped template into its live copy | `kit-dogfood-parity.test.sh --render` and its `PAIRS` list | REUSE unchanged — it already covers all three doc pairs |
| prove a render is its own fixed point | the `write then check is a fixed point` arm in `--selftest` | EXTEND — a second fixture carrying the retrofitted shape |
| force the version to move with the engine | `check-verdict-epoch.sh` | REUSE unchanged; this unit satisfies it rather than changing it |

`python tools/codebase-map/reuse_lookup.py "retrofit a generated marker region across every file
in a corpus"` returned `apply_region` and `render_region` in `gen_build_index.py` as the only
marker-region seams, `kit-dogfood-parity.PAIRS` as the only template-to-live render seam, and
`gate-green-by-accident-on-generated-bytes.md` as the governing gotcha class. No seam exists for a
corpus-wide authored restructure, which is why S2 is hand work rather than a tool.

Every claim about existing code in this spec was verified against source at writing time, including
the eight version spellings, the six non-conformant READMEs, the absent merge attribute on a build
README, and the absence of any gate pairing the constant with the marker on its own line.
