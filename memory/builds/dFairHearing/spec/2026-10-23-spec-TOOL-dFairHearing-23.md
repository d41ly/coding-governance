# TOOL-dFairHearing-23 — the round-1 spec audit's 49 minors: one contract per shared name, criteria a correct build can pass, and the fixtures and records the moved code needs

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 19 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-23-deviation-231.md](../build/2026-10-23-build-TOOL-dFairHearing-23-deviation-231.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 |
| [2026-10-23-prompt-TOOL-dFairHearing-23-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-3-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-3-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-readers-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-readers-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md) | spec-audit | TOOL-dFairHearing-22 TOOL-dFairHearing-21 TOOL-dFairHearing-20 |

<!-- /gen:spec-records -->

## 1. Goal

Every MEDIUM and LOW finding the round-1 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`) is closed by one
batch unit: 49 report ids, 37 MEDIUM (items M1 to M28) and 12 LOW (L1 to L12), each a §2 item. Each
lands on code or a record an earlier unit writes, so this unit builds last: one contract per shared
name, a working replay recipe, the fixtures and meta-gate rows the moved code needs, and an
observation for every criterion the audit found unable to fail or to pass.

## 2. Scope (IN)

Each item names its report id, its report item and the criterion observing it. Where a report item
merges ids, each id is its own item and the later ones point at the first one's mechanism.

- **S1** — id 1 (M1, AC1). `extract_tag_ref` in `tools/workflows/replay_scorer.py` has one contract,
  `TOOL-dFairHearing-12`'s, as §4's table states, its section key the integer
  `tools/workflows/review_replay.py:100-115` returns. `TOOL-dFairHearing-18` consumes it and mints no
  second definition.
- **S2** — id 19 (M1, AC1). S1's defect from the reuse lens; S1 closes it.
- **S3** — id 34 (M1, AC1). S1's defect from the blast-radius lens; S1 closes it, `measure_recall`'s
  window subtraction keeping integer sections.
- **S4** — id 2 (M2, AC2). `check_experiment`'s `review-replay` manifest (§4) is defined whole: a case
  is one review run of one subject record; `dispatched` counts an arm's dispatched runs, `parsed` as
  §4 reads; each `candidates` entry is `{case, report, matched}`,
  `matched` the adjudicated list `TOOL-dFairHearing-1` S3 reads, or `null`. An agent death is read from
  the report's `RUN INTEGRITY` lens and skeptic counts, never the manifest or `parsed`.
  `TOOL-dFairHearing-1`'s void rule and `TOOL-dFairHearing-15`'s `dispatched 4` and `paired 4 of 4`
  use these terms, stated in the factory paragraph of `tools/workflows/README.md`.
- **S5** — id 3 (M3, AC3). `tools/workflows/review_pin.py` gains §4's `--design-audit-runs` and
  `--design-audit-seed`, checked for shape only, and `--design-record-preset` admits `whole-design`.
  When every subject is a design record under `whole-design`, it prints one JSON line per run, as §4
  shows; the caller adds the design's items, scenarios and key hash. It still runs nothing.
- **S6** — id 21 (M3, AC3). S5's defect from the reuse lens; S5 is the route
  `review.design-audit.runs` and `review.design-audit.seed` lacked.
- **S7** — id 4 (M4, AC4). The render-freshness observation `TOOL-dFairHearing-17` AC9 meant compares,
  in a template and its render, the count of a string the unit edited, never a single-token `sed`; the
  parity suite stays a `§7` leg, never an acceptance command.
- **S8** — id 15 (M4, AC4). S7's defect on `unattended-build.template.js`, whose `{{TOOL_ROOT}}`,
  `{{MEMORY_TREE_DIR}}` and `{{KIT_DIR}}` a single-token `sed` cannot fill; S7 closes it.
- **S9** — id 16 (M4, AC4). S7's defect on `TOOL-dFairHearing-18` AC10 over `tier2-review.template.js`,
  whose `{{LENS_SLOTS}}` and `{{TOOL_ROOT}}` arrive before that unit; S7 closes it.
- **S10** — id 32 (M4, AC4). S7's defect, measured at HEAD by the blast-radius lens; S7 closes it.
- **S11** — id 5 (M5, AC5). `review_pin.py` prints `unclassed` and `twin` only when `--unclassed` or
  `--twin` is given, so `TOOL-dFairHearing-3` AC7's exact outputs stand, and both keys' observations
  pass a `--subject`.
- **S12** — id 6 (M6, AC6). One rule for kit versions in this build: no unit moves one on the branch;
  `govkit.py mint` at `push-main.sh --prepare` does (`tools/push-main.sh:26-33`). Every kit version
  constant and `gov:kit` marker line this build's units moved is restored to base `3708a705`'s value,
  superseding the version halves of `TOOL-dFairHearing-8` AC11, `TOOL-dFairHearing-10` AC9,
  `TOOL-dFairHearing-11` AC12 and `TOOL-dFairHearing-16` AC11.
- **S13** — id 31 (M6, AC6). S12's defect from the blast-radius lens, naming the carriers a hand bump
  skipped (the `gov:kit roles@` markers in `tools/roles/README.md:1`,
  `.claude/skills/build/SKILL.md:5` and `tools/roles/SKILL.template.md:5`, and the `agent-cap@` markers
  in `tools/hooks/format-guard.js` and `tools/hooks/scratch-guard.js`); S12 restores every one.
- **S14** — id 7 (M7, AC7). `tools/workflows/render_lenses.py`'s marker grammar admits a second
  marker, a line ending `= [ // gov:lens-optins`, whose `{{LENS_SLOTS}}` token renders the
  `optin = true` rows as `{ key, presets, brief }`; rule 11 still refuses a token with neither marker
  above it.
- **S15** — id 8 (M8, AC8). `tools/workflows/tier2-review.template.js` carries a `WHOLE_DESIGN_LENSES`
  literal on a line ending `= [ // gov:lens-slots whole-design`, the preset receiver gains a fourth
  branch selecting it, and the fan-out leg counts four marked literals. `TOOL-dFairHearing-2` AC1's arm
  asserting `preset: 'whole-design'` throws is rewritten to assert `preset: 'no-such-preset'` throws.
- **S16** — id 10 (M9, AC9). The move of the hook's rule 0, 2 and 5 arms is observed by counting the
  arms themselves, base against tip, in the hook's suite and the three suites receiving them,
  superseding `TOOL-dFairHearing-16` AC8's grep half for names the hook suite never held.
- **S17** — id 13 (M10, AC10). `tools/workflows/README.md` gains a "Replaying a review blind" section
  carrying §4's recipe: a bundle from a `refs/replay/<name>` ref that lives only until the bundle is
  written, fetched into a fresh `git init` clone as `refs/heads/<name>` and checked out, the ref name
  and clone directory per replay; never `git clone --branch` against a `refs/replay/` ref.
- **S18** — id 41 (M10, AC10). S17's defect from the failure-envelope lens; S17's recipe, with
  `git rev-list --count <name>` above 0 in the clone as its liveness check, closes it for
  `TOOL-dFairHearing-15`'s replays too.
- **S19** — id 14 (M11, AC11). `TOOL-dFairHearing-17`'s parity arm asserts the four tokens reachable
  inside its domain, `CONVERGED`, `NON-CONVERGENT`, `BOUNDED` and `CONVERGING`, its header stating
  `CEILING` lies outside it on both sides; the direct case `deriveRoundState([4, 3, 2], 1, 3)` holds
  `CEILING`.
- **S20** — id 38 (M11, AC11). S19's defect from the failure-envelope lens; S19 closes it.
- **S21** — id 23 (M12, AC12). `tools/memory-tree/gotchas.py` gains `check_gate_token(t, tracked, legs)`,
  `check_invariant`'s resolution today (a tracked path, a directory over tracked paths, or a leg name),
  and `check_ungated(text, tracked, legs)`: a class is ungated when its body says `no machine gate`, or
  no backticked token on its `gated by`, `gated in` or `gated at` line passes `check_gate_token`.
  `check_invariant` calls `check_gate_token`; `TOOL-dFairHearing-15`'s `ungated` arm and
  `--all-ungated` flag, where shipped, call `check_ungated`.
- **S22** — id 25 (M13, AC13). S17's section states how a replayed spec-audit call passes the opt-in
  pack: its `reviewDir` is `memory/builds/dFairHearing/reviews`, and the replay base commit adds
  `memory/builds/dFairHearing/README.md` as at base `3708a705`, the owner-landed key
  `spec-audit: 2026-10-21` with no `authorized-by`. Replays spawning agents directly render each prompt
  as a `gov:handoff` file, all rule 6 of the hook admits (`tools/hooks/agent-cap.js:39-48`); a harness
  replay runs through `tier2-review.js`, a declared harness.
- **S23** — id 26 (M14, AC14). `tools/workflows/check-verifier-fanout.test.sh`'s `mkfix` harness gains a
  five-slot literal marked `gov:lens-slots`, and the "non-workflow .js" arm passes explicit files, so
  the whole-tree arms stay green under `TOOL-dFairHearing-13` S5's no-marker red.
- **S24** — id 27 (M15, AC15). `build_layout` copies `lenses.toml` and `render_lenses.py` beside
  `check-protocol-parity.test.sh` (`tools/workflows/unattended-build.test.sh:1995-1996`), so a
  layout's parity render finds the catalogue.
- **S25** — id 28 (M16, AC16). `scan_pairing_sites(root)` walks the tracked `*.py` at and below the
  factory's own directory, never the tool root's tree, any path under the memory root excluded by rule,
  so at the foreign-prefix leg's repository-root prefix it reaches no record folder.
- **S26** — id 29 (M17, AC17). The leg `spec-audit opt-in pack self-test` gains its meta-gate rows: an
  `[[exempt_leg]]` worded as `verifier fan-out self-test`'s (`tools/govkit/registry.toml:642-644`), a
  row in `tools/run-gates/selftest-budgets.txt`, and a
  `WHOLE_RUN` row in `tools/run-gates/foreign-prefix.gov.test.sh`.
- **S27** — id 30 (M18, AC18). Every fixture of `check-verifier-fanout.test.sh` that copies the gate
  (`:199`, `:212`, `:231`) copies `check-verifier-fanout.js` and `render_lenses.py` beside it, and a new
  arm runs a gate copy with no `.js` beside it and expects exit 2 naming the file.
- **S28** — id 33 (M19, AC19). `memory/guides/SESSION-KICKOFF.md` is re-stamped after this build's
  changes to its watched `tools/gate-legs.json` and `coding-governance-agents.template.md`, its derived
  claims re-checked, and its line 99 says the harness acquires the checklist on the diff kind.
- **S29** — id 35 (M20, AC20). The key-pinning arms of `TOOL-dFairHearing-2` AC4,
  `TOOL-dFairHearing-3` AC5 and `TOOL-dFairHearing-9` AC7 in `tools/workflows/tier2-review.test.sh`
  compare the no-argument key with the one the current harness derives under the current template's
  `REVIEW_SHAPE`, never base `3708a705`'s harness or a literal, so `TOOL-dFairHearing-5`'s bump moves
  them together.
- **S30** — id 42 (M21, AC21). `TOOL-dFairHearing-6`'s tally reads an item's grade only when
  `it.grades` is a non-null, non-array object; else each of its ids takes its severity, one WARNING
  naming the item.
- **S31** — id 43 (M22, AC22). `TOOL-dFairHearing-8`'s resume probe returns `legCount`, the manifest's
  element count, beside `legs`; the harness treats `legs` as absent, announced as no leg manifest,
  when it is empty, differs in length from `legCount`, or holds a non-string, an empty string or a
  duplicate.
- **S32** — id 44 (M23, AC23). The synthesis prompt tells the agent to write each `none — <reason>` cell
  on one line, a pipe written as `\|`; `TOOL-dFairHearing-8` S7's check refuses a reason carrying a
  raw `|` or a line break, setting `dispositions` to `null`, its note naming the record's appendix as
  needing a re-render.
- **S33** — id 45 (M24, AC24). `read_raw_output`'s `<src>` resolves in one order: an existing
  working-tree path wins; else a 40-hex string is a blob; else `<rev>:<path>` only when the part before
  the first `:` is longer than one character.
- **S34** — id 46 (M25, AC25). The slot count tracks depth over `(`, `[` and `{` together, by S42's
  shared counter.
- **S35** — id 47 (M26, AC26). One predicate finds a marked literal: `render_lenses.py --markers <file>`
  prints the line number of each line matching the renderer's own anchored marker regex, and the
  fan-out leg's slot count walks exactly those lines. A comment that names `gov:lens-slots` is not a
  marker.
- **S36** — id 48 (M27, AC27). `TOOL-dFairHearing-15`'s acquired checklist is refused, announced as a
  `checklistError`, when it carries no `# by design —` head, or when its `- ` items before that head
  differ from `n + u + k`: `n` and `u` from the `# <n> class(es) selected by an anchor + <u> universal`
  line, `k` from the `# invariants are read at <sha>; <k> that ...` line, 0 when absent.
- **S37** — id 49 (M28, AC28). The `resume:checklist` agent spawns with `probeOpts`, the resume probe's
  stage and type, so `TOOL-dFairHearing-11`'s four-constant arm stays as written.
- **S38** — id 9 (L1, AC29). `TOOL-dFairHearing-15` reuses the `TOOL_ROOT` token
  `TOOL-dFairHearing-8` declares in `tools/workflows/kit.toml`; the row lists it once, and the kit.toml
  half of `TOOL-dFairHearing-15` AC6 is superseded.
- **S39** — id 11 (L2, AC30). `TOOL-dFairHearing-9`'s three records are observed by name: none among
  `gotchas.py --report`'s inert anchors, each selected by its anchors under `--for-paths`.
- **S40** — id 12 (L3, AC31). Replay 1's hit flips `DESIGN_RECORD_PRESET` in `review_pin.py`, never a
  template default; the template's `preset` default stays `unit-spec`, as S17's section says.
- **S41** — id 18 (L4, AC32). The drive-letter observation of `extract_tag_ref` is written as a raw
  string, `r'C:\x.md:[a] then [b]'`.
- **S42** — id 20 (L5, AC33). The slot count lives in `tools/workflows/check-verifier-fanout.js` beside
  rule 2 and counts with agent-cap's exported `topLevelArgs` over its literal-blanked view; no
  `measureSlots` lexer remains, and `LENS_SLOTS = 5` is the one home of the number, read by rule 2's
  array-literal bound in place of `MAX_LENSES`.
- **S43** — id 22 (L6, AC34). `measure_design_recall` calls `measure_recall(items, candidates, 0)` per
  run, the plants as items and the confirmed rows as candidates, both through `extract_tag_ref`; only
  the union, the bar and the pin check stay new code.
- **S44** — id 24 (L7, AC35). `TOOL-dFairHearing-8`'s argument is named `gateManifest`, the name
  `tools/workflows/drift-audit-state.template.js:78` already gives the same input.
- **S45** — id 36 (L8, AC36). The by-hand lookup instruction is reworded in
  `tools/memory-tree/HYGIENE.template.md:775-779`, its render `memory/HYGIENE.md`,
  `memory/guides/MERGE-BAR.md:94-97` and `memory/guides/SESSION-KICKOFF.md:99`: each says the harness
  acquires the checklist on the diff kind, the command kept for a reader who wants it.
- **S46** — id 50 (L9, AC37). `review_pin.py` refuses, exit 2 by name, a `--subject` containing `\`, as
  the harness's `specsRule` does (`tools/workflows/tier2-review.template.js:506`).
- **S47** — id 51 (L10, AC38). `TOOL-dFairHearing-9`'s per-preset note entry is refused, naming
  `lensNotes`, unless absent or a plain object, before the flat check.
- **S48** — id 52 (L11, AC39). `deriveAddressKey` strips a leading `repo + '/'` after folding both to
  `/`, and compares a drive letter case-insensitively.
- **S49** — id 53 (L12, AC40). The `walk` argument refuses, by name, before the first agent: a walker
  slice above 200 cells, a scenario `name` above 120 characters and a `walks` above 600.

## 3. Non-goals (OUT)

- No re-review: each item makes the corrected statement true and reopens no severity.
- No folding into the earlier specs: their criteria stand, each one this unit supersedes named by the
  hands-off bullet in that spec's §3 (§8 F7).
- No HIGH finding: ids 37, 39 and 40 are `TOOL-dFairHearing-20`, `-21` and `-22`.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No retirement of `tools/hooks/agent-cap.js` or of its exports; `topLevelArgs` stays where
  `TOOL-dFairHearing-16` F3 left it.
- No help page: `help/` covers neither the review harness nor the scorer factory.

### Edges

- **consumes-from** `TOOL-dFairHearing-1` — the known-set reader, the replay and the void rule
- **consumes-from** `TOOL-dFairHearing-2` — `preset` and its refusal arm
- **consumes-from** `TOOL-dFairHearing-3` — `tools/workflows/review_pin.py` and the opt-in swap
- **consumes-from** `TOOL-dFairHearing-4` — `deriveAddressKey`
- **consumes-from** `TOOL-dFairHearing-5` — `REVIEW_SHAPE`'s bump
- **consumes-from** `TOOL-dFairHearing-6` — the per-id grade tally
- **consumes-from** `TOOL-dFairHearing-8` — the leg probe, the disposition check, `gateManifest`
- **consumes-from** `TOOL-dFairHearing-9` — the three class records and the per-preset notes
- **consumes-from** `TOOL-dFairHearing-10` — the harness version move
- **consumes-from** `TOOL-dFairHearing-11` — the typed spawns, the twin key, the version move
- **consumes-from** `TOOL-dFairHearing-12` — `replay_scorer.py` and its readers
- **consumes-from** `TOOL-dFairHearing-13` — `lenses.toml`, `render_lenses.py` and the slot count
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment` and its manifest
- **consumes-from** `TOOL-dFairHearing-15` — the acquiring agent, the replay, `ungated`
- **consumes-from** `TOOL-dFairHearing-16` — the moved rules and suites, the new leg, the version move
- **consumes-from** `TOOL-dFairHearing-17` — the parity arm, the leg-manifest edit
- **consumes-from** `TOOL-dFairHearing-18` — the preset, `walk`, the design grade
- **hands-off** `TOOL-dFairHearing-25` — finding id 1 (H1) of the audit of units 20 to 23: the replays of units 1 and 15 run on this unit's corrected contract
- **hands-off** `TOOL-dFairHearing-26` — finding id 10 (H2): AC9's label half superseded by its census of every rule 0 and rule 5 label
- **hands-off** `TOOL-dFairHearing-27` — the same audit's 22 minors on this spec: its S1 to S6, S9 to S11, S14 to S18, S22 to S24 and S27 to S31, each naming what it supersedes

## 4. Design

### Why one unit and not two

BUILD-METHOD M6's clause 2 refuses a split where one half writes a file the other reads as a contract.
The Python set (`replay_scorer.py`, `review_pin.py`, `gotchas.py`, `render_lenses.py`) and the JS one
(the harness template, its suite, the fan-out gate) share two: `review_pin.py` reads
`SPEC_SUBJECT_PATH` from the rendered harness (`TOOL-dFairHearing-3` S8), and the fan-out leg reads its
marker lines from `render_lenses.py --markers` (S35). `TOOL-dFairHearing-20` shares this unit's order
and writes `tools/workflows/tier2-review.template.js` too, so the dispatcher sequences the two.

### One contract per shared name (S1 to S3, S43)

`extract_tag_ref(text) -> (path, key) | None`, defined once, in `tools/workflows/replay_scorer.py`:

| `where` carries | `key` |
|---|---|
| a `[<tag>]` | the first one, as the string `'[<tag>]'` |
| no tag, a `§<n>` or `section <n>` | `n`, the integer `extract_section_ref` returns |
| neither | the ref is unscorable, `None` |

The path folds as `extract_section_ref` folds it: `\` to `/`, a drive prefix `C:/` to `/`, leading
`./` dropped. Through S43, a plant and a hit match by the equality every known-set reader uses.

### The review-replay manifest (S4)

```json
{
  "instance": "review-replay",
  "known": "<src>",
  "candidates": [{"case": "<record>", "report": "<src>", "matched": "<src> or null"}],
  "arms": [{"name": "<arm>", "base": null, "settings": {}, "dispatched": 4}]
}
```

`parsed <arm>: <n> of <dispatched>` counts the arm's runs whose report holds an appendix with at least
one row `parse_candidates` reads.

### review.pin's two new flags (S5, S6, S11, S46)

```
python <kit>/review_pin.py --subject <path> [...] [--design-record-preset unit-spec|design-audit|whole-design]
                           [--design-audit-runs 1|2|3] [--design-audit-seed reverted-escapes|synthetic|none]
                           [--unclassed <v>] [--twin <v>] [--opt-in ...]
# defaults: runs 2, seed reverted-escapes
# whole-design: one line per run   {"preset": "whole-design", "walk": {"runs": 3, "run": 1, "seed": "synthetic"}}
# otherwise: one line, a key only for each flag given
```

A `--subject` carrying `\` exits 2 first (S46). The criteria's example subjects, which need not
exist: `$DREC` is the design record `memory/builds/dX/build/d.md`, and `$SPEC` the unit spec
`memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md`.

### Kit versions (S12, S13)

At this unit's commit the version carriers differ from `3708a705` by no `KIT_*_VERSION = ` line and
no `gov:kit <kit>@` marker (AC6). The carriers are those
`tools/check-kit-versions.sh` grades: S13's, `tools/hooks/agent-cap.js`, `tools/roles/roles_lib.py`,
and the `version:` line of `tools/workflows/tier2-review.template.js` with its render.

### The slot count, one counter and one predicate (S34, S35, S42)

```
markers = render_lenses.py --markers <harness>          # line numbers, the renderer's own anchored regex
for each marker line: body = the literal from its "[" to the matching "]" in the blanked view
                      slots = topLevelArgs(body).length  # agent-cap's export, depth over ( [ {
                      red unless slots === LENS_SLOTS     # LENS_SLOTS = 5, its one home
```

The count moves from `check-verifier-fanout.sh` to `check-verifier-fanout.js` (S42); rule 2's bound
read `MAX_LENSES` at `tools/hooks/agent-cap.js:497` and `:635`.

### The ungated predicate (S21)

`check_gate_token` is the inner loop of `check_invariant` (`tools/memory-tree/gotchas.py:432-440`),
lifted unchanged; `check_ungated` reads the class body through the same `FM_RE` cut `declares()` uses
(`:261-268`), so the front matter never decides.

### The replay recipe (S17, S18, S22, S40)

```bash
mkdir -p "$TEMP/<name>b"
git update-ref refs/replay/<name> <commit>
git bundle create "$TEMP/<name>b/h.bundle" refs/replay/<name>
git update-ref -d refs/replay/<name>
git init "$TEMP/<name>"
git -C "$TEMP/<name>" fetch "$TEMP/<name>b/h.bundle" refs/replay/<name>:refs/heads/<name>
git -C "$TEMP/<name>" checkout <name>
git -C "$TEMP/<name>" rev-list --count <name>            # above 0, or the clone is empty
```

For a spec-audit replay, `<commit>` is a scratch commit on the original adding S22's README, and the
call names S22's `reviewDir` (§8 F3).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_gate_token`, `check_ungated` | functions, `tools/memory-tree/gotchas.py` | `py.function`, OK |
| `--design-audit-runs`, `--design-audit-seed` | `review_pin.py` flags | none |
| `--markers` | `render_lenses.py` flag | none |
| `WHOLE_DESIGN_LENSES` | constant, `tools/workflows/tier2-review.js` | none: no JS constant cell in `.lexicon.conf` |
| `LENS_SLOTS` | constant, `tools/workflows/check-verifier-fanout.js` | none |
| `legCount` | probe return field | none |
| `matched` | manifest key | none |

`gateManifest` (S44) is reused from `tools/workflows/drift-audit-state.template.js:78`, not minted.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/review_pin.py`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/render_lenses.py`
- `tools/workflows/check-verifier-fanout.js`
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `memory/guides/MERGE-BAR.md`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/govkit/registry.toml`
- `tools/run-gates/selftest-budgets.txt`
- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/hooks/agent-cap.js`
- `tools/hooks/format-guard.js`
- `tools/hooks/scratch-guard.js`
- `tools/roles/roles_lib.py`
- `tools/roles/README.md`
- `tools/roles/SKILL.template.md`
- `.claude/skills/build/SKILL.md`

The hooks and roles files: version lines only, where an earlier unit moved them (S12, S13).
`tools/workflows/tier2-review.js` and `memory/HYGIENE.md` are renders.

### Alternatives rejected

- **Two batch units, Python and JS** — §8 F1.
- **Fold each minor into its spec** — the owner's 2026-10-05 ruling (BUILD-METHOD M4) folds none.
- **One bumping unit per kit (S12)** — §8 F5; specs 4, 5, 13, 17 and 18 carry the no-bump non-goal.
- **A parity arm holding a Python and a JS marker regex equal (S35)** — §8 F6.

## 5. Production-readiness checklist

- security — S46 and S49 refuse at argument boundaries; S22 copies an owner-landed key byte for byte;
  no new write path.
- perf / scale — one more python call per harness in the fan-out leg (S35).
- error / empty / loading states — every new refusal exits 2 or throws by name before any agent; a
  truncated checklist or leg list is announced, never used.
- observability — runs parsed of runs dispatched; one announced line per leg-list or checklist refusal.
- risks — S12 reverts version lines, re-derived by the mint at `--prepare`; S49's ceilings (§8 F4).
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none: every surface touched is new in this build or keeps its default.
- user docs — `tools/workflows/README.md` (manifest, replay section, review.pin's flags) and the docs
  S45 rewords (§3: no `help/` page).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory; a clone goes under `%TEMP%/<short name>`, a clone under the
scratchpad exceeding the Windows path limit. A bare script name is the
workflows kit's file under `tools/workflows/`; `$DREC` and `$SPEC` are §4's example subjects.

- **AC1** — When a scratch python probe imports `replay_scorer.py`, `extract_tag_ref('x.md:§3 S2')`
  returns `('x.md', 3)` and `extract_tag_ref('x.md:[walk-table] plan.input')` returns
  `('x.md', '[walk-table]')`; and an `ast` walk over every tracked `*.py` under `tools/` finds
  `def extract_tag_ref` exactly once.
  Red when: the section fallback returns the string `'§3'`, or a second definition lands.
- **AC2** — When `python replay_scorer.py --experiment "$SCRATCH/rr.json"` runs a review-replay
  manifest of four candidates, each with a report and a `matched` list, arms `dispatched` 4, it prints `parsed <arm>: 4 of 4`; with one report's appendix cut, `parsed <arm>: 3 of 4`;
  and a manifest carrying an unknown key still exits 2 naming it.
  Red when: `parsed` counts known items, or `matched` is refused as an unknown key.
- **AC3** — When `python review_pin.py --subject $DREC --design-record-preset whole-design --design-audit-runs 3 --design-audit-seed synthetic`
  runs, it prints three JSON lines, each `"preset": "whole-design"` with a `walk` of `runs` 3, `seed`
  `synthetic` and `run` 1, 2 and 3 in turn; `--design-audit-runs 4` exits 2 naming the flag; and
  without `whole-design` no line carries `walk`.
  Red when: one line prints for three runs, or a run index repeats.
- **AC4** — When `grep -c` counts `WALK_RULES` over `tier2-review.template.js` and
  `tier2-review.js`, and `roundState` over `unattended-build.template.js`
  and `unattended-build.js`, each pair prints equal counts of at least 1.
  Red when: a template is edited and its render is not, so a pair differs.
- **AC5** — When `review_pin.py --subject $SPEC --unclassed reason` and the same `--subject` with
  `--twin always` run, each prints one JSON line carrying its key; with the `--subject` alone the line
  is exactly `{"preset": "unit-spec"}`.
  Red when: a key prints with its flag absent.
- **AC6** — When `git diff -U0 3708a705 -- tools/hooks tools/roles .claude/skills/build tools/workflows/tier2-review.template.js | grep -E '^[-+].*(KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@)'`
  runs at this unit's commit, it prints nothing.
  Red when: a hand bump of any carrier survives on the branch.
- **AC7** — When `python render_lenses.py` renders a scratch template holding a
  `= [ // gov:lens-optins` marker above a `{{LENS_SLOTS}}` token beside the shipped markers, it exits 0
  and fills the opt-in rows; a token with neither marker above it exits 2 naming the orphan.
  Red when: the opt-in marker is refused, or the orphan passes.
- **AC8** — When `grep -n "gov:lens-slots whole-design" tier2-review.js` runs, it prints
  the `WHOLE_DESIGN_LENSES` marker line; a scratch prelude probe with `preset: 'whole-design'` and a
  valid `walk` selects that literal, and `preset: 'no-such-preset'` throws naming `preset`; and
  `bash check-verifier-fanout.sh tier2-review.js` exits 0.
  Red when: the whole-design rows name a literal no marker declares, so the render refuses.
- **AC9** — When a scratch probe collects the labels
  `git grep -hoE '^check(_spec_audit)? "rule[05]:[^"]*"' 3708a705 -- tools/hooks/agent-cap.test.sh`
  prints, 24 for rule 0 and 4 for rule 5, then at tip `grep -cF "<label>" spec-audit-optin.test.sh`
  prints at least 1 per rule 0 label, `grep -cF "<label>" check-review-join.test.sh`
  at least 1 per rule 5 label, and `grep -cF "<label>" tools/hooks/agent-cap.test.sh` 0 for all 28; and
  `grep -c "gov:fixed-verifiers\|gov:sequential-agents" tools/hooks/agent-cap.test.sh check-verifier-fanout.test.sh`
  prints, for the hook's suite, less than base's 42, a drop no larger than the fan-out suite's rise from
  base's 1. On a staged break, one rule 0 arm deleted from a scratch copy of its receiving suite, the
  probe names that label.
  Red when: a moved arm stays in the hook's suite, or is deleted rather than moved.
  figure: the base counts are PINNED, measured at `3708a705` on 2026-10-23.
- **AC10** — When the recipe in `tools/workflows/README.md`'s replay section runs with `<name>` `fhr`
  and `<commit>` `3708a705`, `git -C "$TEMP/fhr" rev-list --count fhr` prints a number above 0, and
  `git show-ref refs/replay/fhr` in this repository prints nothing afterwards; and
  `grep -c "clone --branch" tools/workflows/README.md` prints 0.
  Red when: the recipe clones a `refs/replay/` ref with `--branch`, which exits 128.
- **AC11** — When a scratch prelude probe calls `deriveRoundState([4, 3, 2], 1, 3)`, it returns
  `CEILING`; and `grep -n "CEILING lies outside" tier2-review.test.sh` prints the parity
  arm's header line, the arm's token assertion naming the four in-domain tokens.
  Red when: the arm demands all five tokens over a domain where `CEILING` cannot occur.
- **AC12** — When a scratch python probe imports `tools/memory-tree/gotchas.py`, `check_ungated` reads
  a body "Gated by `tools/check-wiring.sh`." as gated, "There is no machine gate." as ungated, and
  "Gated by `no-such-gate.sh`." as ungated; and an `ast` probe finds `check_invariant`'s body calling
  `check_gate_token`.
  Red when: a class gated by a tracked path joins the ungated population.
- **AC13** — When `node spec-audit-optin.js < "$SCRATCH/replay1.json"` runs over a spec-audit payload
  whose `repo` is a clone the recipe made with S22's README added and whose `reviewDir` is S22's, it
  exits 0; with `reviewDir` `memory/builds/dClosedLoop/reviews` it exits 2 naming `authorized-by: prompt`.
  Red when: the replay's placement is still dClosedLoop's prompt-authorized README.
  fixture: the clone under `%TEMP%/fhq`, made by the probe.
- **AC14** — When `grep -n "gov:lens-slots" check-verifier-fanout.test.sh` runs, it
  prints the `mkfix` harness's marked literal; and a scratch fixture as `mkfix` writes it, run
  whole-tree by `check-verifier-fanout.sh`, exits 0, and exits 1 naming the missing marker without it.
  Red when: the whole-tree fixtures carry no marked literal, so the no-marker red fires on them.
- **AC15** — When `grep -n "render_lenses.py" unattended-build.test.sh` runs, it prints
  `build_layout`'s copy line beside `lenses.toml`; and a scratch directory holding that copy set renders
  `tier2-review.template.js`, exit 0, and exits 2 without `lenses.toml`.
  Red when: a layout lacks the catalogue, so its parity render fails.
- **AC16** — When a scratch probe calls `replay_scorer.scan_pairing_sites` with the root at this
  repository's root, and at `tools/workflows`, neither returns a site under `memory/`.
  Red when: the population is the tool root's tree, so aScoutedSeam's bench sites are named.
- **AC17** — When `grep -n "spec-audit opt-in pack self-test" tools/govkit/registry.toml tools/run-gates/selftest-budgets.txt tools/run-gates/foreign-prefix.gov.test.sh`
  runs, it prints the `[[exempt_leg]]` name line, the budget row and the `WHOLE_RUN` row.
  Red when: a meta-gate file lacks the leg, so govkit's descriptor check or the budget check reds.
- **AC18** — When `grep -c "check-verifier-fanout.js" check-verifier-fanout.test.sh`
  prints at least 4, one per gate-copying fixture plus the new arm; and a scratch copy of
  `check-verifier-fanout.sh` with no `.js` beside it, run over a harness, exits 2 naming
  `check-verifier-fanout.js`.
  Red when: the missing `.js` prints clean.
- **AC19** — When `sed -n 99p memory/guides/SESSION-KICKOFF.md` runs, it no longer says "run before a
  review"; and the `last-audit:` line names a sha at which `git merge-base --is-ancestor <sha> HEAD`
  succeeds and after which `git log <sha>..HEAD -- tools/gate-legs.json coding-governance-agents.template.md`
  lists no commit.
  Red when: a watched file moved after the stamp.
- **AC20** — When `grep -n "REVIEW_SHAPE" tier2-review.test.sh` runs, it prints the read the three
  key arms derive their expected key from; and `grep -c "3708a705" tier2-review.test.sh`
  prints no line inside those arms.
  Red when: an arm compares with base's harness, so `TOOL-dFairHearing-5`'s bump reds it.
- **AC21** — When a scratch stub run of `tier2-review.js` hands its tally one item with no `grades`
  and one with `grades: null`, each places its ids at the item's severity, a WARNING naming the item.
  Red when: `String(it.grades[String(id)])` throws a TypeError on either.
- **AC22** — When a scratch stub run's resume probe returns `legs: []`, a list one short of `legCount`,
  a list with a duplicate, or one with a non-string, each run announces no leg manifest and admits no
  `gate:` disposition on it; a full list matching `legCount` admits the valid gate.
  Red when: a truncated list refuses a valid gate or admits an invented one.
- **AC23** — When `grep -n "a pipe written as" tier2-review.js` runs, it prints the reason-cell
  instruction; and a scratch stub synthesis returning a reason with a raw `|` gets `dispositions: null`,
  its note naming the appendix as needing a re-render.
  Red when: a piped reason reaches the appendix unrefused.
- **AC24** — When a scratch probe calls `read_raw_output` with an existing drive-lettered path under
  `$SCRATCH`, it reads the file; with `HEAD:README.md` or a 40-hex blob id, the blob.
  Red when: the drive-lettered path is read as `<rev>:<path>` and refused.
- **AC25** — When the fan-out leg's slot count runs over a scratch literal of five
  `deriveSlotLens('unit-spec', { key: 'a', brief: 'b, c' })` elements under a marker, it reads 5.
  Red when: a comma inside parentheses or braces counts as a slot.
- **AC26** — When `python render_lenses.py --markers "$SCRATCH/h.js"` runs over a file whose comment
  names `gov:lens-slots` above a valid marked literal, it prints only the literal's line; and the
  fan-out leg over that file exits 0.
  Red when: the comment line is walked from a bracket it does not open.
- **AC27** — When a scratch stub run's acquiring agent returns the real `gotchas.py --for-diff` stdout
  cut inside its item list, or before the `# by design —` head, the run logs a `checklistError`
  WARNING and passes no checklist; whole, it is accepted.
  Red when: a tail-truncated return passes as complete.
- **AC28** — When `grep -n "resume:checklist" tier2-review.js` runs, the agent call it
  prints passes `probeOpts`, and `grep -n "probeOpts, findOpts, verifyOpts\|synthOpts" tier2-review.test.sh`
  prints `TOOL-dFairHearing-11`'s arm still listing exactly four options constants.
  Red when: a fifth options constant appears, or the agent spawns untyped.
- **AC29** — When a scratch python probe loads `tools/workflows/kit.toml` with `tomllib`, the
  `tier2-review.template.js` row's placeholder list holds `TOOL_ROOT` exactly once.
  Red when: the token is declared twice, or the row lacks it.
- **AC30** — When `python tools/memory-tree/gotchas.py --report` runs, none of the records
  `portability-sweep.md`, `topology-sweep.md` and `adopter-migration-sweep.md` under `memory/gotchas/`
  appears among its inert anchors, and `gotchas.py --for-paths` over one anchor of each selects it.
  Red when: a new record's anchor selects no tracked path.
- **AC31** — When `grep -n "DESIGN_RECORD_PRESET" review_pin.py tools/workflows/README.md` runs, it
  prints the constant and the replay section's sentence naming it as replay 1's flip; and the
  template's `preset` default literal reads `unit-spec`.
  Red when: replay 1's verdict flips a template default.
- **AC32** — When `python -c "import sys; sys.path.insert(0, 'tools/workflows'); import replay_scorer as r; print(r.extract_tag_ref(r'C:\x.md:[a] then [b]'))"`
  runs, it prints the path `'/x.md'` and the key `'[a]'` as one tuple.
  Red when: the ref reads the second tag, or the probe raises before reaching the reader.
- **AC33** — When `grep -c "measureSlots\|MAX_LENSES" check-verifier-fanout.sh check-verifier-fanout.js`
  runs, each file prints 0, and `grep -c "LENS_SLOTS = " check-verifier-fanout.js` prints 1.
  Red when: a second counter or a second home for 5 remains.
- **AC34** — When an `ast` probe reads `measure_design_recall` in `replay_scorer.py`, its body calls
  `measure_recall`; and the fixture of `TOOL-dFairHearing-18` AC8 still prints 2 of 3 per run and
  exits 1.
  Red when: the grade matches plants with its own loop.
- **AC35** — When `grep -c "legManifest" tier2-review.js` runs, it prints 0, and the
  args header carries `gateManifest:` as a key line.
  Red when: the harness keeps a second spelling of the input.
- **AC36** — When `git grep -n "run before a review\|Before a review, run\|Hand a reviewer the classes" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md`
  runs, it prints nothing, and each file names the harness acquiring the checklist.
  Red when: a doc still sends a reviewer to run the lookup by hand.
- **AC37** — When `python review_pin.py --subject 'memory\builds\dX\spec\2026-01-01-spec-TOOL-dX-1.md'`
  runs, it exits 2 and its stderr names the backslash.
  Red when: the backslashed spec path is classified as a design record.
- **AC38** — When a scratch prelude probe passes `lensNotes: { 'unit-spec': null }` and then
  `lensNotes: { 'unit-spec': 'x' }`, each throws naming `lensNotes` before the first agent.
  Red when: `|| {}` turns either into an empty note set.
- **AC39** — When a scratch probe of `deriveAddressKey` keys `{ file: '<repo>/src/a.js' }` and
  `{ file: 'src/a.js' }` under `repo` `C:/R`, and `{ file: 'c:/R/src/a.js' }` the same way, all three
  keys are equal.
  Red when: a repo-absolute path or a lower-case drive letter keys apart.
- **AC40** — When a scratch prelude probe passes a `walk` whose run-1 slice for one walker holds 201
  cells, a scenario `name` of 121 characters, or a `walks` of 601, each throws naming the field and its
  ceiling before the first agent; 200, 120 and 600 proceed.
  Red when: an oversized grid reaches the walkers.
  figure: the ceilings are PINNED by §8 F4, against the 812-cell walk measured by the audit.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `kit/dogfood doc parity` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `hook destinations self-test` · `govkit selftest` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix` · `verifier fan-out` · `review-replay selftest` · `gotchas selftest` · `review-protocol parity (kit vs dogfood)` · `kickoff-manifest ratchet` · `foreign-prefix parity (every self-test at three prefixes)` · `govkit selfcheck` · `every held leg is budgeted, every budget row resolves` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC8 AC11 AC20 AC21 AC22 AC23 AC27 AC28 AC38 AC39 AC40 · each covered AC's red case, staged against the harness at `TOOL-dFairHearing-18`'s commit · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC1 AC2 AC16 AC24 AC32 AC34 · each covered AC's red case, staged against the factory at `TOOL-dFairHearing-18`'s commit · that runner's declared arm count, raised by the arms added
New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC9 AC14 AC18 AC25 AC26 · the marked mkfix literal, a gate copy with no `.js`, a five-call literal, a comment naming the marker, and rule 2's moved marker arms with the rule cut from the gate, staged against the gate at `TOOL-dFairHearing-16`'s commit · none
New arm: tools/workflows/spec-audit-optin.test.sh · covers AC9 · rule 0's moved arms, staged with the rule cut from the pack · none
New arm: tools/workflows/check-review-join.test.sh · covers AC9 · rule 5's moved arms, staged with the ref-keyed ban cut from the check · none
New arm: tools/workflows/unattended-build.test.sh · covers AC15 · a layout without `lenses.toml`, staged against the suite at `TOOL-dFairHearing-13`'s commit · none
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC12 · a class gated by a tracked path and one gated by an untracked token, staged against base's gotchas.py, which has no `check_ungated` · none

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, Python and JS. (b)
  fails M6's clause 2 on the contract reads §4 "Why one unit" names. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Which contract does `extract_tag_ref` keep for a `§<n>` ref?** Options: (a) the integer of
  `TOOL-dFairHearing-12` AC4; (b) the string `'§<n>'` of `TOOL-dFairHearing-18` AC7. (b) breaks
  `measure_recall`'s window subtraction and the replay scores unit 12's AC3 pins, and unit 12 builds
  first. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — How does a replayed spec-audit call pass the opt-in pack?** Options: (a) S22's `reviewDir`,
  the replay base carrying this build's README byte for byte from base `3708a705`; (b) a recorded
  departure, the call refused; (c) a `RUN.md` planted in the clone. (b) leaves `TOOL-dFairHearing-1`
  AC4 and AC5 nothing to score; (c) is a run writing its own opt-in, which TOOL-aWardedAudit-4
  refuses; (a) copies an owner's date the pack already honours. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — What ceilings bound the walk grid (S49)?** Options: (a) 200 cells per walker slice, 120
  characters per `name`, 600 per `walks`; (b) a ceiling the caller passes; (c) a stated ceiling, no
  refusal. The audit's 812-cell walk dealt about 162 cells per walker and returned whole; (b) is a knob
  no key backs; (c) leaves the failure the finding names. RESOLVED (agent, 2026-10-23, delegated):
  (a), rung 3. widens: none · relaxes: none
- **F5 — One rule for kit versions (S12)?** Options: (a) no branch bump, the lander mints; (b) one
  bumping unit per kit. (b) contradicts `tools/push-main.sh:26-33` and five sibling specs' non-goal.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F6 — How is the marker predicate held once across Python and JS (S35)?** Options: (a) the renderer
  prints marker lines through `--markers`, the leg reads them; (b) a regex per language and an arm
  holding them equal, two predicates, the defect itself. RESOLVED (agent, 2026-10-23, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F7 — How does an earlier unit's builder treat a criterion this unit supersedes?** Options: (a) the
  hands-off bullet in that unit's §3 names it, its acceptance ledger recording it superseded by this
  unit's named criterion; (b) fold the correction into the earlier spec, which BUILD-METHOD M4 refuses
  for a spec-audit minor. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the round-1 spec audit's 37 MEDIUM and 12 LOW findings
  as one batch.
- rev-2 · 2026-10-23 · §3 · the audit of units 20 to 23 disposed: hands-off edges to TOOL-dFairHearing-25, -26 and -27.

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries, and none adds a module: the
factory `tools/workflows/replay_scorer.py` and its `measure_recall`, `read_raw_output` and
`extract_section_ref` (`tools/workflows/review_replay.py:100-115`); agent-cap's exported
`topLevelArgs` (`tools/hooks/agent-cap.js:1362-1380`), already tracking `(`, `[` and `{`;
`check_invariant`'s token resolution (`tools/memory-tree/gotchas.py:432-440`); the harness's
`specsRule` (`tools/workflows/tier2-review.template.js:506`); drift-audit-state's `gateManifest`
(`tools/workflows/drift-audit-state.template.js:78`); and the sibling rows of
`tools/govkit/registry.toml` and `tools/run-gates/selftest-budgets.txt`.
`tools/codebase-map/reuse_lookup.py` over "count the top level elements of an array literal string
aware" and "decide whether a bug class record names a gate" ranked generic stems and
`check_gate_wall`, missing `topLevelArgs` and S21's inline resolution, which the source read found.
Recall returned specs 3, 12 and 16, missing `TOOL-aBatchedTribunal-1d`
(`memory/archive/DECISIONS.2026-08-10.md:50`), the one-counter-per-gate ruling S42 follows.

Recall terms used: `python tools/memory-recall/query.py "spec audit minors on the review harness scorer factory and lens catalogue" --terms "extract_tag_ref review_pin lens-slots topLevelArgs gotchas ungated replay bundle clone opt-in pack kit version mint"`
