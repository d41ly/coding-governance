# TOOL-cMendedVintage-1 — `adopt-memory-tree.sh --render`, the one adopter with no render path

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/adopt-memory-tree.sh` accepts only `--scaffold`, and on an adopted tree that mode
prints `already scaffolded — nothing to do` and exits 0 without touching a single rendered file. The
kit ships four `rendered` rows, so it is the one kit whose artifacts no verb can refresh: re-adoption
is a no-op on the happy path and a refusal off it. Give it a narrow mode that skips the adoption
guard, re-renders those four files and nothing else, and declare that mode as the kit's
`[[regenerate]]` argv.

## 2. Scope (IN)

- **S1** `adopt-memory-tree.sh` accepts `--render` beside `--scaffold`. The usage line and the file's
  own header comment name both. Observed by AC1.
- **S2** The four `render_doc` calls that write `HYGIENE.md`, `TEMPLATE-SPEC.md`,
  `guides/BUILD-METHOD.md` and `guides/ANNOTATION-STYLE.md` move into one function called by both
  modes, so the render set is written once and cannot diverge between them. Observed by AC2.
- **S3** `--render` runs after the existing `.memory-tree.conf` and `READINESS_ROWS` refusals and
  after the placeholder derivations, requires the adoption marker — a `gov:kit memory-tree@` line in
  the tree's `HYGIENE.md` — and exits 1 naming `--scaffold` when the marker is absent. It creates no
  directory, writes no registry, seeds no conf and re-renders nothing else. Observed by AC3.
- **S4** `--render` leaves the four files byte-identical when the templates and the conf have not
  moved, and prints one line per file it actually rewrote. Observed by AC2.
- **S5** `tools/memory-tree/kit.toml` gains `[[regenerate]]` with
  `argv = ["bash", "{kit}/adopt-memory-tree.sh", "--render"]`, and a comment naming the four rows it
  refreshes and the flag that gates the step. Observed by AC4.
- **S6** The kit's version constant is bumped, because this changes shipped bytes an adopter runs.
  Observed by AC5.

## 3. Non-goals (OUT)

- No change to `--scaffold`: its guard, its refusals, its registry writes and its index render are
  untouched. A tree that has never been scaffolded still gets exactly one verb.
- `--render` does not re-seed `.memory-tree.conf`, `build-readme-slot-limits.txt` or
  `build-readme-slot-highwater.txt`. Those are `seed` rows the target owns after one copy, and a mode
  that rewrote them would destroy the adopter's own declarations.
- No new outcome block in the descriptor. `--render` exits 1 only where the tree already carries
  `HYGIENE.md` — the case the existing `refused-foreign-tree` outcome classifies — or where the conf
  is missing, which is the `[adopt]` argv's own pre-existing refusal and is not re-adjudicated here.
- No change to `check-memory-hygiene.sh`, to the templates themselves, or to what any of the four
  rendered files says.

### Edges

- **hands-off** `DEPL-cMendedVintage-8` — that unit refuses a descriptor shipping `rendered` rows and
  declaring no `[[regenerate]]`. `memory-tree` is one of its four hits at BASE and is the only one no
  descriptor edit alone can close, so this unit is what lets that gate pass in this repo.
- **hands-off** `DEPL-cMendedVintage-7` — this unit leaves the flag flip to that one. Until it lands,
  the declared argv runs only when an operator sets the variable, and `--render` is reachable by hand.
- **hands-off** external — an adopter takes the new mode on their next routine pull; nothing in this
  repo installs it for them.

## 4. Design

### Data model

The script derives `MEMORY_ROOT`, `KIT_DIR`, `TOOL_ROOT` and `READINESS_ROWS` before it reaches the
adoption guard, and `render_doc` consumes exactly those. So the render set is separable from the
scaffold with no new derivation: the mode branch sits between the conf refusals and the guard.

```
MODE=${1:---scaffold}                # --scaffold | --render, anything else is the usage refusal
… conf + READINESS_ROWS refusals (unchanged) …
if [ "$MODE" = "--render" ]; then
  <marker present?> || exit 1        # names --scaffold in the message
  render_all                          # the four render_doc calls, once
  exit 0
fi
… the guard, then the scaffold, which calls render_all at the point the four calls sit today …
```

`render_all` is the S2 extraction. It exists so the two modes cannot render different sets, which is
the defect class this repo keeps paying for when one artifact list is written twice.

### Inventory

Minted here: the shell function `render_all` and the `--render` mode word. The repo declares naming
cells, and shell function names in a kit adopter are graded by the lexicon kit's shell coverage mode;
`render` is a table verb already used by this file's `render_doc`, so the name extends the existing
spelling rather than introducing a synonym.

### Migration

None on disk. An adopter who runs `--render` against a tree already holding current renders gets four
byte-identical comparisons and no write. An adopter whose renders are stale gets them rewritten in
place, which is a content change to tracked files they then commit.

### Rollout

Reachable by hand on landing, and by `update --write` only once `GOVKIT_RERENDER` defaults on. The
descriptor block is inert until then, exactly as the three blocks `DEPL-cMendedVintage-5` declares.

### Alternatives rejected

A bounded re-adoption — teaching `--scaffold` to fall through its guard when the marker is present —
was refused: the guard is what makes `--scaffold` safe to re-run at all, and a mode that sometimes
writes registries and sometimes does not is two verbs wearing one name. `TOOL-dRetiredFork-29`
already names the `--render` shape as the cheapest one, from the same measurement.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/adopt-memory-tree.sh` | mode parse, the `render_all` extraction, the render branch |
| `tools/memory-tree/kit.toml` | one regenerate block, version bump |

## 5. Production-readiness checklist

- security — the mode writes only inside the declared memory root and runs no target-supplied
  command. It adds no new path class to what `--scaffold` already writes.
- perf / scale — four template reads and four comparisons. N/A.
- error / empty / loading states — three refusals: an unknown mode, a missing conf or row
  declaration, and a tree with no adoption marker. Each names the verb to run instead.
- observability — one line per file rewritten, silence for a file already current, which is the shape
  `--scaffold` already prints.
- risks — the real risk is a `--render` that quietly renders a SUBSET of the rows the descriptor
  declares, leaving one artifact permanently stale while every verb reports success. S2's single
  render set is the structural answer, and AC2 observes the four files together.
- testing — AC1 through AC3 run the script directly against a scratch tree; AC4 reads the descriptor
  through `selfcheck`.
- migration — none.
- user docs — the kit README's adoption section gains the new mode in one line.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/adopt-memory-tree.sh --render` is run in a scratch clone of
  an adopted tree, it exits 0 and reports the render, and the same script run with an unknown mode
  word still exits 2 with its usage line.
  Red when: the mode word is accepted anywhere but the parse, so `--render` falls through into the
  scaffold path and writes registries.
  fixture: a scratch copy of this repo's own `memory/` tree under the run's scratch root. This repo
  IS an adopted memory tree, so the fixture is a copy rather than a construction.
- **AC2** — When one of the four rendered files is truncated in that scratch tree and `--render` is
  re-run, all four files compare equal to a fresh render afterwards, and the run named the file it
  rewrote.
  Red when: the render set is spelled twice and one mode writes three files, which is the stale-row
  failure this unit exists to close.
  figure: DERIVED — the four paths come from the `rendered` rows in `tools/memory-tree/kit.toml`, not
  from a list typed into this spec.
- **AC3** — When `--render` is run against a directory tree whose memory root carries no
  `gov:kit memory-tree@` marker, it exits 1, names `--scaffold` in the message and writes nothing.
  Red when: the marker check is missing, in which case the mode renders gov's documents into a
  foreign tree the adopter never scaffolded.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and its re-render-claims
  note counts `memory-tree` among the kits declaring `[[regenerate]]`.
  Red when: the descriptor block is absent or its argv names a mode the script refuses, which
  `DEPL-cMendedVintage-8`'s refusal then reports against this repo.
- **AC5** — When `bash tools/check-kit-versions.sh` runs, `KIT_MEMORY_TREE_VERSION` is present,
  well-formed and agrees with the marker in the document this kit ships.
  Red when: the engine constant moves and the doc marker does not, which that gate calls a drift.

## 7. Gates

`memory hygiene` · `kit version markers` · `kit/dogfood doc parity` · `govkit selfcheck` · `kit placeholders (a declared token its adopter substitutes)`

No new arm, and the reason is the 2026-08-23 owner ruling rather than an omission: this kit's
self-tests are withheld from the bar, so a new suite for a mode branch would be a file nobody runs.
What guards the class instead is `DEPL-cMendedVintage-8`'s refusal, which reds the moment a
descriptor ships a `rendered` row with no regenerate — including a future row this mode forgets. The
three refusals are observed once, by AC1 through AC3, on the fixture those criteria name.

## 8. Open questions

- **Q1 — does `--render` belong in the same file as `--scaffold`, or in a sibling script?** A sibling
  keeps the scaffold's refusals out of the render path, and costs a second copy of the four
  placeholder derivations plus a second file for the descriptor to name.
  RESOLVED (agent, 2026-09-16, delegated): one file. The derivations already run before the guard,
  so the branch reuses them unchanged, and a second script would be a second place the render set is
  written — the exact defect S2 exists to prevent.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "adopter script re-renders its templates without the
adoption guard"` found no seam and reported `.sh` as an unscanned layer, so this kit's adopter is
outside the map's corpus entirely; the ranked names it returned are `render_*` symbols in the
codebase-map and lexicon kits and none of them is reachable from shell. The seam this unit extends
was read from source instead: `render_doc` in `tools/memory-tree/adopt-memory-tree.sh`, whose header
names `tools/lib/render-doc.sh` as its canonical copy under a parity gate, so the extraction in S2
must not edit the function body. The precedent for a narrow render mode beside a guarded adopter is
`tools/lexicon/adopt-lexicon.sh`, whose `--render` exists because `--scaffold` refuses on an existing
declaration — the same sentence, one kit over. The recall probe returned `TOOL-dRetiredFork-29`,
which measured six kits with twelve rendered rows and zero declarations and names this exact mode as
the cheapest shape.

Recall terms used: `--terms "govkit update regenerate rerender descriptor kit.toml rendered role
adopter dark flag rollback receipt outcome"`, with the question "why does govkit update decline a
kit's re-render unless GOVKIT_RERENDER is set, and what did the dark landing buy".
