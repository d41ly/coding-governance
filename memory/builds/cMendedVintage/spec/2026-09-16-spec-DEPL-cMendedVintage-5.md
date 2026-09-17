# DEPL-cMendedVintage-5 — `[[regenerate]]` for the three kits whose adopter already renders

**Status:** CLOSED · rev-3 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-DEPL-cMendedVintage-5-acceptance-ledger.md](../build/2026-09-16-build-DEPL-cMendedVintage-5-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-DEPL-cMendedVintage-5-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-5-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

`lexicon`, `drift-audit` and `memory-recall` each ship exactly one `rendered` row and declare no
`[[regenerate]]` block, so `govkit update` cannot refresh their Skills and each one goes a vintage
stale on every pull. All three adopters already carry a re-render entrypoint that does not trip an
adoption guard, so the whole missing piece is a declaration per descriptor. Ship lexicon's
accepted-stop `[[outcome]]` in the same edit, because the entrypoint this unit declares is the one
that can refuse.

## 2. Scope (IN)

- **S1** `tools/lexicon/kit.toml` gains `[[regenerate]]` with
  `argv = ["bash", "{kit}/adopt-lexicon.sh", "--render"]`. That mode exists at BASE, skips the
  `--scaffold` refusal on an existing declaration, and re-runs `write_skill`. Observed by AC1.
- **S2** `tools/drift-audit/kit.toml` gains `[[regenerate]]` with
  `argv = ["bash", "{kit}/adopt-drift-audit.sh"]`. The bare invocation renders the Skill and reads no
  project layer of its own, so the regenerate argv and the `[adopt]` argv are the same words.
  Observed by AC1.
- **S3** `tools/memory-recall/kit.toml` gains `[[regenerate]]` with
  `argv = ["bash", "{kit}/adopt-memory-recall.sh", "--scaffold"]`. That mode renders unconditionally
  and refuses only when the shared `.memory-tree.conf` is unreadable. Observed by AC1.
- **S4** `tools/lexicon/kit.toml` gains one `[[outcome]]` block for exit code 1, probing
  `must_not_exist = ".lexicon.conf"`, `means = "no-project-layer"`, and carrying `ok = true`. The new
  `--render` argv exits 1 with that message on a claimed-but-unconfigured target, and without the
  block `outcome_accepted` refuses the exit and `update` raises an unaccepted failure on a kit that
  correctly declined. Observed by AC2.
- **S5** Each of the three descriptors carries a comment on its new block naming what the argv
  renders and why re-running the adopter is safe. Any sentence in those three files that says
  `update` re-renders names `GOVKIT_RERENDER` in the same sentence, because declaring the block puts
  each file into selfcheck arm 7l's population for the first time. Observed by AC3.
- **S6** The three kits' version constants are bumped, so an adopter's receipt can tell the vintage
  that carries a regenerate from the one that does not. Observed by AC4.

## 3. Non-goals (OUT)

- `tools/memory-tree/kit.toml` gets no block here. Its adopter accepts only `--scaffold` and has no
  render entrypoint to name, which is `TOOL-cMendedVintage-1`'s whole unit.
- No `[[outcome]]` for `memory-recall`, although `--scaffold` exits 1 on a tree with no
  `.memory-tree.conf`. That exit is pre-existing and is shared with the `[adopt]` argv, so declaring
  it `ok = true` would also change what `govkit apply` accepts for a state no unit in this build has
  re-adjudicated. The regenerate on an unconfigured `memory-recall` therefore fails loudly and names
  the kit, which is BASE behaviour for the same exit.
- No `[[outcome]]` for `drift-audit`. Its render reads no project layer, so it has no unconfigured
  state to classify; its non-zero exits are environment failures.
- No change to the `GOVKIT_RERENDER` default, and no change to the re-render loop in
  `tools/govkit/govkit.py`. This unit is inert until that flag flips.
- No change to any adopter script. All three entrypoints exist at BASE and are used as they stand.

### Edges

- **hands-off** `DEPL-cMendedVintage-7` — this unit leaves the flag flip to that one. Until it lands
  these three blocks are read by `selfcheck` and executed by nothing, which is why this unit ships
  first and alone changes no run's behaviour.
- **hands-off** `DEPL-cMendedVintage-8` — that unit's new refusal grades exactly the population this
  unit drains. Three of its four hits at BASE are closed here.
- **hands-off** external — the two live adopters take these blocks on their next routine pull; no
  runbook step in this repo installs them.

- **hands-off** `DEPL-cMendedVintage-16` — that unit narrows the lexicon `[[outcome]]` probe this unit ships, which as written also accepts a failed first scaffold.
## 4. Design

### Data model

A `[[regenerate]]` block is one key, `argv`, resolved through `target_context` and run in the
target's tree by `_cmd_update`'s re-render stage. The exit code goes through `classify_outcome` and
`outcome_accepted`, exactly as `apply`'s CONFIGURE step does, so a kit may declare a non-zero exit as
an accepted stop rather than a failure.

| kit | regenerate argv | measured refusal it can produce |
|---|---|---|
| `lexicon` | `bash {kit}/adopt-lexicon.sh --render` | exit 1, `no .lexicon.conf; nothing to render from` |
| `drift-audit` | `bash {kit}/adopt-drift-audit.sh` | none tied to the project layer |
| `memory-recall` | `bash {kit}/adopt-memory-recall.sh --scaffold` | exit 1 from the shared conf refusal |

### Inventory

Minted by this unit: one `[[regenerate]]` table per descriptor, and one `[[outcome]]` table in
`tools/lexicon/kit.toml`. No new file, no new flag, no new token. This repo declares naming cells for
identifiers, and a TOML table key is not one of them.

### Alternatives rejected

Re-running each kit's `[adopt]` argv instead of declaring a narrow block was refused upstream and the
measurement is recorded: an adopter run against an adopted tree either no-ops or refuses the tree as
foreign, so re-adoption cannot refresh a rendered row. `TOOL-dRetiredFork-29` names the shape this
unit builds and counts the kits it applies to.

Declaring `ok = true` on the lexicon block rather than leaving the outcome merely classified: a
classified-but-failing outcome still stops the update and withholds the receipt re-stamp, which is
the rollback-by-decline class this build exists to close. An unconfigured lexicon is a posture, not a
fault.

### Rollout

Inert on landing. With `GOVKIT_RERENDER` unset the re-render stage declines every kit before it reads
these blocks, so the observable change in this repo is confined to what `govkit selfcheck` and
`govkit plan` report. The first behavioural run is the one `DEPL-cMendedVintage-7` enables.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/lexicon/kit.toml` | one regenerate block, one outcome block |
| `tools/drift-audit/kit.toml` | one regenerate block |
| `tools/memory-recall/kit.toml` | one regenerate block |
| each kit's version constant and every `gov:kit` marker its entry claims | S6's bump |

S6 is more than three lines: selfcheck arm 5c holds every `gov:kit` marker inside an entry's derived
set equal to that entry's constant, so the bump moves each marker carrier too — including the
workflow harnesses `drift-audit` declares as `marker_carriers`, and the rendered lexicon Skill, whose
marker the adopter writes from the constant. Read the set from the entries rather than from a list
here; it is `entry_members` plus `marker_carriers`, which is what arm 5c itself reads.

## 5. Production-readiness checklist

- security — the argv is gov's, read from a gov-authored descriptor and never from the target's
  `deploy.toml`, so this adds no target-supplied command. The trust boundary is unchanged.
- perf / scale — three more subprocess runs per `update --write`, each a shell adopter that renders
  one file. N/A as a scale concern.
- error / empty / loading states — the refusal paths are the table in section 4; the lexicon one is
  declared, the memory-recall one stays a loud failure by the section 3 non-goal.
- observability — each run and each decline is printed by the re-render stage under the flag.
- risks — a regenerate argv that renders the wrong file would be invisible until the flag flips. The
  argv is byte-identical to the documented entrypoint in each kit's own usage header.
- testing — AC1 and AC2 are fixture observations against a scratch target; AC3 and AC4 are greps.
- migration — none. A descriptor gaining a table changes no receipt row and no path.
- user docs — each kit's README already documents its render entrypoint; no page changes.

## 6. Acceptance criteria

- **AC1** — When a scratch target holding the three kits is taken through
  `python tools/govkit/govkit.py update --target <dir> --write` with `GOVKIT_RERENDER=1` exported,
  the run prints one `ran` line per kit naming that kit's regenerate argv, and each kit's rendered
  Skill is rewritten in that run.
  Red when: a descriptor's block is absent or its argv names a mode the adopter does not accept, in
  which case the kit appears on a `DECLINED` line instead of a `ran` line.
  fixture: a scratch install under the run's scratch root; this repo keeps no `.governance/`
  receipt of its own, so the observation cannot be made against the tree itself.
  cost: one apply plus one update against a small target, tens of seconds.
- **AC2** — When the same update runs against a target whose `.lexicon.conf` has been removed, the
  lexicon row is reported with the declared meaning `no-project-layer` and the run does not raise an
  unaccepted-exit failure for that kit.
  Red when: the `[[outcome]]` block is missing its `ok = true`, which leaves the exit classified and
  still failing.
- **AC3** — When `git grep -n "GOVKIT_RERENDER" -- tools/lexicon/kit.toml tools/drift-audit/kit.toml
  tools/memory-recall/kit.toml` is read beside `python tools/govkit/govkit.py selfcheck`, the
  selfcheck exits 0 and its re-render-claims note counts these three kits in its population.
  Red when: a comment added by S5 says an `update` re-renders without naming the flag in the same
  sentence, which arm 7l refuses the moment the block puts the file in its population.
  figure: DERIVED — the population count comes from the selfcheck's own note line.
- **AC4** — When `bash tools/check-kit-versions.sh` runs, every constant it names is present and
  well-formed, and the three kits' constants read higher than they do at BASE.
  Red when: a descriptor changes with its kit's version constant left where it was, so an adopter's
  receipt cannot distinguish the vintage that carries a regenerate.

## 7. Gates

`govkit selfcheck` · `kit version markers` · `lexicon wiring` · `drift-audit wiring` · `memory-recall skill wiring` · `kit placeholders (a declared token its adopter substitutes)`

No new arm. The behaviour this unit declares is exercised by the fixture in AC1 and by
`DEPL-cMendedVintage-7`'s arms once the flag flips; adding a second end-to-end suite here would grade
the same three argv twice.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · built. Three changes, none to the design. (a) The S4 block ships with a
  comment stating what its probe does NOT tell apart — a failed first scaffold leaves the same
  absent conf — and naming `DEPL-cMendedVintage-16` as the unit that narrows it. The probe itself is
  unchanged, per that unit's ownership of the repair. (b) Section 4's file table listed three
  descriptors and has been corrected: S6's bump moves every `gov:kit` marker inside each entry's
  derived set, which selfcheck arm 5c holds equal to that entry's constant, so the real write set is
  `entry_members` plus `marker_carriers` and is read from the entries rather than listed twice.
  (c) AC1 was observed per-argv rather than through `update`'s re-render loop: each declared argv was
  run in this tree and each rewrote its own `rendered` row, and the AC2 fixture ran the lexicon argv
  against a staged target with no conf. The loop itself is unchanged code already exercised by the
  `unattended` block, and standing up a scratch target for the three kits costs a memory-tree
  seed-and-stop plus a lexicon ratification — the end-to-end `DEPL-cMendedVintage-7` owns.
- rev-3 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. The spec-audit disposal authored DEPL-cMendedVintage-16 naming this unit, and the edge was never written back — hygiene check 12 reds on a handoff one author declared and the other never saw. The edge is a fact about this build that became true when the promotion was created, so recording it completes the record rather than changing the design.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "re-render a kit's rendered artifacts during an update"`
returned no seam for this unit and reported `.sh` as an unscanned layer, so every adopter entrypoint
this unit names is invisible to the map by construction; the ranking it did return is name-token
noise over `render_*` symbols in unrelated kits. The seam this unit extends was found by reading the
descriptors instead, and it is `tools/unattended/kit.toml`'s `[[regenerate]]` block with its
`[[outcome]]` pair, which `tools/govkit/govkit.py` already executes through `classify_outcome`. The
recall probe returned the prior art that settles the shape: `TOOL-dRetiredFork-29` in
`memory/backlog/TOOL.md` names the six kits, the twelve rendered rows and the zero declarations, and
records that re-adoption cannot be the mechanism.

Recall terms used: `--terms "govkit update regenerate rerender descriptor kit.toml rendered role
adopter dark flag rollback receipt outcome"`, with the question "why does govkit update decline a
kit's re-render unless GOVKIT_RERENDER is set, and what did the dark landing buy".
