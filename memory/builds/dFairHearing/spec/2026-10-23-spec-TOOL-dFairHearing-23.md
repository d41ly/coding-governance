# TOOL-dFairHearing-23 — the round-1 spec audit's 49 minors: one contract per shared name, criteria a correct build can pass, and the fixtures and records the moved code needs

**Status:** CLOSED · rev-6 · 2026-11-03 · node d · Tier-2 · base 3708a705 · streams tooling · order 19 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-23-deviation-231.md](../build/2026-10-23-build-TOOL-dFairHearing-23-deviation-231.md) | deviation | — |
| [2026-10-23-build-TOOL-dFairHearing-23-deviation-238.md](../build/2026-10-23-build-TOOL-dFairHearing-23-deviation-238.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 |
| [2026-10-23-prompt-TOOL-dFairHearing-23-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-3-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-3-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-23-readers-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-23-readers-fix-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFairHearing-23-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-23-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief.md) | research | TOOL-dFairHearing-10 TOOL-dFairHearing-22 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-1 TOOL-dFairHearing-21 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-25 TOOL-dFairHearing-26 |
| [2026-11-03-prompt-TOOL-dFairHearing-23-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-23-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dFairHearing-23-2-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-23-2-fix-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-23-3-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-23-3-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dFairHearing-23-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-23-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md) | spec-audit | TOOL-dFairHearing-22 TOOL-dFairHearing-21 TOOL-dFairHearing-20 |

<!-- /gen:spec-records -->

## 1. Goal

Every MEDIUM and LOW finding the round-1 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`) is closed by one
batch unit: 49 report ids, 37 MEDIUM (items M1 to M28) and 12 LOW (L1 to L12), each a §2 item. Each
lands on code or a record an earlier unit writes, so this unit builds after the units it corrects: one
contract per shared name, a working replay recipe, the fixtures and meta-gate rows the moved code
needs, and an observation for every criterion the audit found unable to fail or to pass. Seventeen
items landed with the units they correct; each says so, with its commit, and its criterion observes the
landing (§6).

## 2. Scope (IN)

Each item names its report id, its report item and the criterion observing it. Where a report item
merges ids, each id is its own item and the later ones point at the first one's mechanism. An item
opening **Landed** names the commit that built it; this unit builds nothing for it. Cites are at
`576f89da` unless they say otherwise.

- **S1** — id 1 (M1, AC1). **Landed** at `af3831a6c` (`TOOL-dFairHearing-12`). `extract_tag_ref` in
  `tools/workflows/replay_scorer.py` (:224-234) has one contract, as §4's table states, its section key
  the integer `extract_section_ref` (:211-221) returns. `TOOL-dFairHearing-18` consumed it at
  `b21501741` and minted no second definition: its builder's return names AC7's `'§3'` tag-shape half
  as this item's hand-off, met by the integer.
- **S2** — id 19 (M1, AC1). S1's defect from the reuse lens; S1 closes it.
- **S3** — id 34 (M1, AC1). S1's defect from the blast-radius lens; S1 closes it, `measure_recall`'s
  window subtraction keeping integer sections.
- **S4** — id 2 (M2, AC2). `check_experiment`'s `review-replay` manifest (§4) is defined whole: a case
  is one review run of one subject record; `dispatched` counts an arm's dispatched runs, `parsed` as
  §4 reads; each `candidates` entry is `{case, report, matched}`,
  `matched` the adjudicated list `TOOL-dFairHearing-1` S3 reads, or `null`. An agent death is read from
  the report's `RUN INTEGRITY` lens and skeptic counts, never the manifest or `parsed`.
  `TOOL-dFairHearing-1`'s void rule and `TOOL-dFairHearing-15`'s `dispatched 4` and `paired 4 of 4`
  use these terms, stated in the factory paragraph of `tools/workflows/README.md`. At `576f89da`
  `measure_replay_experiment` still reads `candidates` as `{<arm>: <src>}`.
- **S5** — id 3 (M3, AC3). `tools/workflows/review_pin.py` gains §4's `--design-audit-runs` and
  `--design-audit-seed`, checked for shape only, and `--design-record-preset` admits `whole-design`.
  When every subject is a design record under `whole-design`, it prints one JSON line per run, as §4
  shows; the caller adds the design's items, scenarios and key hash. It still runs nothing.
- **S6** — id 21 (M3, AC3). S5's defect from the reuse lens; S5 is the route
  `review.design-audit.runs` and `review.design-audit.seed` lacked.
- **S7** — id 4 (M4, AC4). A render-freshness observation compares, in a template and its render,
  the count of a string the edit adds, never a single-token `sed`; the parity suite stays a §7 leg,
  never an acceptance command. This unit's own is AC4, over two strings its §4 edits add to
  `tools/workflows/tier2-review.template.js`. The render-diff clauses `TOOL-dFairHearing-17` AC9 and
  `TOOL-dFairHearing-18` AC10 hand here were met by those units' builds: `roundState` counts 1 in
  `tools/workflows/unattended-build.template.js` and 1 in its render after `3745b407a`, and unit 18's
  builder recorded its template and render as differing by the one filled `{{LENS_SLOTS}}` line, with
  `WALK_RULES` counting 7 in each, after `b21501741`.
- **S8** — id 15 (M4, AC4). S7's defect on `unattended-build.template.js`, whose `{{TOOL_ROOT}}`,
  `{{MEMORY_TREE_DIR}}` and `{{KIT_DIR}}` a single-token `sed` cannot fill; S7 closes it. This unit
  edits neither file of that pair.
- **S9** — id 16 (M4, AC4). S7's defect on `TOOL-dFairHearing-18` AC10 over `tier2-review.template.js`,
  whose `{{LENS_SLOTS}}` and `{{TOOL_ROOT}}` a single-token `sed` cannot fill either; S7 closes it, and
  unit 18's AC10 render-diff half is closed there.
- **S10** — id 32 (M4, AC4). S7's defect, measured at HEAD by the blast-radius lens; S7 closes it.
- **S11** — id 5 (M5, AC5). **Landed** at `ef757de0c` (`TOOL-dFairHearing-11`, `--twin`) and
  `4a0e73da6` (`TOOL-dFairHearing-8`, `--unclassed`). `review_pin.py` prints `unclassed` and `twin`
  only when `--unclassed` or `--twin` is given, so `TOOL-dFairHearing-3` AC7's exact outputs stand, and
  both keys' observations pass a `--subject`, which unit 8's builder did for its AC4.
- **S12** — id 6 (M6, AC6). One rule for kit versions in this build: no unit moves one on the branch;
  `govkit.py mint` at `push-main.sh --prepare` does (`tools/push-main.sh:26-33`). No commit of this
  build moved a version carrier: AC6's build-wide probe prints nothing over the 24 `tool(dFairHearing)`
  commits at `576f89da`, so there is nothing to restore, and this unit's own diff moves none. The rule
  supersedes the version halves of `TOOL-dFairHearing-8` AC11, `TOOL-dFairHearing-10` AC9,
  `TOOL-dFairHearing-11` AC12 and `TOOL-dFairHearing-16` AC11.
- **S13** — id 31 (M6, AC6). S12's defect from the blast-radius lens, naming the carriers a hand bump
  skipped (the `gov:kit roles@` markers in `tools/roles/README.md:1`,
  `.claude/skills/build/SKILL.md:5` and `tools/roles/SKILL.template.md:5`, and the `agent-cap@` markers
  in `tools/hooks/format-guard.js:7` and `tools/hooks/scratch-guard.js:144`). No unit of this build
  moved one, so S12 closes it with no edit to any of them.
- **S14** — id 7 (M7, AC7). **Landed** at `9ce7710ab` (`TOOL-dFairHearing-3`).
  `tools/workflows/render_lenses.py`'s marker grammar admits a second marker, a line ending
  `= [ // gov:lens-optins` (:28), whose `{{LENS_SLOTS}}` token renders the `optin = true` rows as
  `{ key, presets, brief }`; rule 11 still refuses a token with neither marker above it (:135-136).
- **S15** — id 8 (M8, AC8). **Landed** at `b21501741` (`TOOL-dFairHearing-18`), ahead of this unit:
  its builder landed the literal because `render_lenses.py`'s rule 8 refused the walker rows without
  it. `tools/workflows/tier2-review.template.js` carries a `WHOLE_DESIGN_LENSES` literal on a line
  ending `= [ // gov:lens-slots whole-design` (:1221), the preset receiver selects it in a fourth
  branch (:1232), and the fan-out leg counts four marked literals. `TOOL-dFairHearing-2` AC1's arm
  asserts `preset: 'no-such-preset'` throws (`tools/workflows/tier2-review.test.sh:194`).
- **S16** — id 10 (M9, AC9). **Landed** at `886c11fea` (`TOOL-dFairHearing-16`). The hook's rule 0, 2
  and 5 arms moved to the three suites receiving them; the move is observed by counting the arms
  themselves, base against tip, superseding `TOOL-dFairHearing-16` AC8's grep half for names the hook
  suite never held. AC9's label half is `TOOL-dFairHearing-26`'s, by §3.
- **S17** — id 13 (M10, AC10). `tools/workflows/README.md` gains a "Replaying a review blind" section
  carrying §4's recipe: a bundle from a `refs/replay/<name>` ref that lives only until the bundle is
  written, fetched into a fresh `git init` clone as `refs/heads/<name>` and checked out, the ref name
  and clone directory per replay; never `git clone --branch` against a `refs/replay/` ref.
- **S18** — id 41 (M10, AC10). S17's defect from the failure-envelope lens; S17's recipe, with
  `git rev-list --count <name>` above 0 in the clone as its liveness check, closes it for
  `TOOL-dFairHearing-15`'s replays too.
- **S19** — id 14 (M11, AC11). **Landed** at `3745b407a` (`TOOL-dFairHearing-17`), whose builder took
  this change in place of its own AC6's five-token assertion. Its parity arm asserts the four tokens
  reachable inside its domain, `CONVERGED`, `NON-CONVERGENT`, `BOUNDED` and `CONVERGING`
  (`tools/workflows/tier2-review.test.sh:515-518`), its header stating `CEILING` lies outside it on
  both sides (:491-499); the direct case `deriveRoundState([4, 3, 2], 1, 3)` holds `CEILING` (:463).
- **S20** — id 38 (M11, AC11). S19's defect from the failure-envelope lens; S19 closes it.
- **S21** — id 23 (M12, AC12). `tools/memory-tree/gotchas.py` gains `check_gate_token(t, tracked, legs)`,
  `check_invariant`'s resolution today (a tracked path, a directory over tracked paths, or a leg name),
  and `check_ungated(text, tracked, legs)`: a class is ungated when its body says `no machine gate`, or
  no backticked token on its `gated by`, `gated in` or `gated at` line passes `check_gate_token`.
  `check_invariant` calls `check_gate_token`. `gotchas.py` carries neither an `ungated` arm nor an
  `--all-ungated` flag at `576f89da`; whichever unit adds one calls `check_ungated`.
- **S22** — id 25 (M13, AC13). S17's section states how a replayed spec-audit call passes the opt-in
  pack: its `reviewDir` is `memory/builds/dFairHearing/reviews`, and the replay base commit adds
  `memory/builds/dFairHearing/README.md` as at base `3708a705`, the owner-landed key
  `spec-audit: 2026-10-21` with no `authorized-by`. Replays spawning agents directly render each prompt
  as a `gov:handoff` file, all rule 6 of the hook admits (`tools/hooks/agent-cap.js:19-33`); a harness
  replay runs through `tier2-review.js`, a declared harness.
- **S23** — id 26 (M14, AC14). Unit 13's hand-off: `tools/workflows/check-verifier-fanout.test.sh`'s
  `mkfix` harness (:370-386) gains a five-slot literal marked `gov:lens-slots`, so its whole-tree arms
  AC2 and AC3 (:388-401), red under `TOOL-dFairHearing-13` S5's no-marker rule since `864f43d25`, pass
  again. The "non-workflow .js" arm (:315-318) needs no change: it asserts the `verifier-fanout: clean`
  line, which the gate prints before its slot verdict. S27 closes the second cause of the same arms'
  red.
- **S24** — id 27 (M15, AC15). `build_layout` copies `lenses.toml` and `render_lenses.py` beside
  `check-protocol-parity.test.sh` (`tools/workflows/unattended-build.test.sh:2133-2134`), so a
  layout's parity render finds the catalogue.
- **S25** — id 28 (M16, AC16). `scan_pairing_sites(root)` walks the tracked `*.py` at and below the
  factory's own directory, never the tool root's tree, any path under the memory root excluded by rule,
  so at the foreign-prefix leg's repository-root prefix it reaches no record folder. At `576f89da` it
  returns two `aScoutedSeam` bench sites under `memory/` from the repository root.
- **S26** — id 29 (M17, AC17). Unit 16's hand-off: the leg `spec-audit opt-in pack self-test`, which
  `886c11fea` added to `tools/gate-legs.json` with no `guard`, gains its meta-gate rows, none of which
  exists at `576f89da`: an `[[exempt_leg]]` worded as `verifier fan-out self-test`'s
  (`tools/govkit/registry.toml:662-664`), a row in `tools/run-gates/selftest-budgets.txt` beside the
  sibling suites' (:94, :118, :149), and a `WHOLE_RUN` row in `tools/run-gates/foreign-prefix.gov.test.sh`
  (:245-261), the suite carrying no `FOREIGN_PREFIX_PROBE` stop. `TOOL-dFairHearing-27` S4 later
  supersedes the `WHOLE_RUN` half.
- **S27** — id 30 (M18, AC18). Unit 16's hand-off: every fixture of `check-verifier-fanout.test.sh`
  that copies the gate (`:311`, `:354`, `:373`) copies `check-verifier-fanout.js` and `render_lenses.py`
  beside it. Since `886c11fea` the gate exits 2 when its `.js` is absent
  (`tools/workflows/check-verifier-fanout.sh:321-322`), so the empty-population, missing-predicate and
  `mkfix` arms red before reaching their own question. A new arm runs a gate copy with no `.js` beside
  it and expects that exit 2 naming the file.
- **S28** — id 33 (M19, AC19). The `gotchas.py --for-diff` line of `memory/guides/SESSION-KICKOFF.md`
  (:100) says the harness acquires the checklist on the diff kind. This unit's §4 stages no file on the
  kickoff manifest's `watch:` line (`memory/guides/SESSION-KICKOFF.md:6`), so it owes no `last-audit:`
  re-stamp; the re-stamp the `tools/gate-legs.json` edit owed was `TOOL-dFairHearing-16`'s own (its
  rev-7 S9), bundled at `886c11fea`.
- **S29** — id 35 (M20, AC20). **Landed** with the arms themselves, at `e21580aac`
  (`TOOL-dFairHearing-2` AC4), `9ce7710ab` (`TOOL-dFairHearing-3` AC5) and `c70d6a020`
  (`TOOL-dFairHearing-9` AC7). Each key-pinning arm in `tools/workflows/tier2-review.test.sh` compares
  two keys the current render derives under the current `REVIEW_SHAPE`, never base `3708a705`'s harness
  or a literal, so `TOOL-dFairHearing-5`'s bump at `d1db0fc80` moved them together.
- **S30** — id 42 (M21, AC21). Unit 6's hand-off: `TOOL-dFairHearing-6`'s tally
  (`tools/workflows/tier2-review.template.js:2911`) reads an item's grade only when `it.grades` is a
  non-null, non-array object; else each of its ids takes its severity, one WARNING naming the item.
  This is a fallback, never a refusal, and it holds over unit 6's §4 Migration, which that spec's rev-3
  now states as landing here; at `576f89da` the read throws a TypeError.
- **S31** — id 43 (M22, AC22). Unit 8's hand-off: its resume probe returns `legCount`, the manifest's
  element count, beside `legs`; the harness treats `legs` as absent, announced as no leg manifest,
  when it is empty, differs in length from `legCount`, or holds a non-string, an empty string or a
  duplicate. At `576f89da` the harness filters `legs` (`tier2-review.template.js:1597`).
- **S32** — id 44 (M23, AC23). Unit 8's hand-off: the synthesis prompt tells the agent to write each
  `none — <reason>` cell on one line, a pipe written as `\|`; `TOOL-dFairHearing-8` S7's check refuses
  a reason carrying a raw `|` or a line break, setting `dispositions` to `null`, its note naming the
  record's appendix as needing a re-render.
- **S33** — id 45 (M24, AC24). **Landed** at `af3831a6c` (`TOOL-dFairHearing-12`). `read_raw_output`'s
  `<src>` resolves in one order (`tools/workflows/replay_scorer.py:122-150`): an existing working-tree
  path wins; else a 40-hex string is a blob; else `<rev>:<path>` only when the part before the first
  `:` is longer than one character.
- **S34** — id 46 (M25, AC25). The slot count tracks depth over `(`, `[` and `{` together, by S42's
  shared counter. The depth tracking itself landed at `864f43d25` in the gate's `measureSlots`
  (`tools/workflows/check-verifier-fanout.sh:354-378`); the move to the shared counter is S42's.
- **S35** — id 47 (M26, AC26). One predicate finds a marked literal: `render_lenses.py --markers <file>`
  prints the line number of each line matching the renderer's own anchored marker regex, and the
  fan-out leg's slot count walks exactly those lines. A comment that names `gov:lens-slots` is not a
  marker.
- **S36** — id 48 (M27, AC27). `TOOL-dFairHearing-15`'s acquired checklist is refused, announced as a
  `checklistError`, when it carries no `# by design —` head, or when its `- ` items before that head
  differ from `n + u + k`: `n` and `u` from the `# <n> class(es) selected by an anchor + <u> universal`
  line, `k` from the `# invariants are read at <sha>; <k> that ...` line, 0 when absent. At `576f89da`
  the harness admits any return holding one `- ` line (`tier2-review.template.js:1394`).
- **S37** — id 49 (M28, AC28). **Landed** at `7b2153c28` (`TOOL-dFairHearing-15`). The
  `resume:checklist` agent spawns with `probeOpts`, the resume probe's stage and type
  (`tier2-review.template.js:1390`), so `TOOL-dFairHearing-11`'s four-constant arm stays as written.
- **S38** — id 9 (L1, AC29). **Landed** at `4a0e73da6` (`TOOL-dFairHearing-8`). `TOOL-dFairHearing-15`
  reuses the `TOOL_ROOT` token unit 8 declared in `tools/workflows/kit.toml`; the
  `tier2-review.template.js` row lists it once (:84), and the kit.toml half of `TOOL-dFairHearing-15`
  AC6 is superseded, as unit 15's builder recorded.
- **S39** — id 11 (L2, AC30). **Landed** at `c70d6a020` (`TOOL-dFairHearing-9`). Unit 9's three records
  are observed by name: none in the `dead anchors` section of `gotchas.py --report`, each selected by
  its anchors under `--for-paths`.
- **S40** — id 12 (L3, AC31). Replay 1's hit flips `DESIGN_RECORD_PRESET` in `review_pin.py` (:36),
  never a template default; the template's `preset` default stays `unit-spec`
  (`tier2-review.template.js:330`), as S17's section says.
- **S41** — id 18 (L4, AC32). **Landed** at `af3831a6c` (`TOOL-dFairHearing-12`). The drive-letter
  observation of `extract_tag_ref` is written as a raw string, `r'C:\x.md:[a] then [b]'`, which unit 18
  hands here for its AC7.
- **S42** — id 20 (L5, AC33). The slot count lives in `tools/workflows/check-verifier-fanout.js` beside
  rule 2 and counts with `topLevelArgs`, which `TOOL-dFairHearing-16` moved from the hook into that
  file (:737), over its literal-blanked view; no `measureSlots` lexer remains, and `LENS_SLOTS = 5` is
  the one home of the number, read by rule 2's array-literal bound in place of `MAX_LENSES`.
- **S43** — id 22 (L6, AC34). **Landed** at `b21501741` (`TOOL-dFairHearing-18`).
  `measure_design_recall` (`tools/workflows/replay_scorer.py:548-611`) calls
  `measure_recall(plants, candidates, 0)` per run, the plants as items and the confirmed rows as
  candidates, both through `extract_tag_ref`; only the union, the bar and the pin check are new code.
- **S44** — id 24 (L7, AC35). Unit 8's hand-off: `TOOL-dFairHearing-8`'s argument is named
  `gateManifest`, the name `tools/workflows/drift-audit-state.template.js:80` already gives the same
  input.
- **S45** — id 36 (L8, AC36). The by-hand lookup instruction is reworded in
  `tools/memory-tree/HYGIENE.template.md:775-779`, its render `memory/HYGIENE.md`,
  `memory/guides/MERGE-BAR.md:94-97` and `memory/guides/SESSION-KICKOFF.md:100`: each says the harness
  acquires the checklist on the diff kind, the command kept for a reader who wants it.
- **S46** — id 50 (L9, AC37). `review_pin.py` refuses, exit 2 by name, a `--subject` containing `\`, as
  the harness's `specsRule` does (`tools/workflows/tier2-review.template.js:849`).
- **S47** — id 51 (L10, AC38). **Landed** at `c70d6a020` (`TOOL-dFairHearing-9`). Unit 9's per-preset
  note entry is refused, naming `lensNotes`, unless absent or a plain object, before the flat check
  (`tier2-review.template.js:1265-1283`).
- **S48** — id 52 (L11, AC39). `deriveAddressKey` (`tier2-review.template.js:622-634`) strips a leading
  `repo + '/'` after folding both to `/`, and compares a drive letter case-insensitively.
- **S49** — id 53 (L12, AC40). Unit 18's hand-off: the `walk` argument refuses, by name, before the
  first agent: a walker slice above 200 cells, a scenario `name` above 120 characters and a `walks`
  above 600.
- **S50** — units 6 and 8's hand-off on the unattended-build suite, from their builder returns (AC41).
  The synthesis double `build_merged_returns` in `tools/workflows/unattended-build.test.sh` (:968-987)
  returns items with no `grades`, which unit 6's tally reads unguarded (S30), and no `dispositions`,
  which unit 8's synthesis schema requires (`tier2-review.template.js:2833`). The strict runner
  (`unattended-build.test.sh:324-330`) returns such a synthesis as null, so every `MT` arm reads a dead
  synthesis. The double gives each item of an array `grades` mapping each of its ids to the item's own
  severity, and returns `dispositions`, one `{id, disposition}` per id the skeptic double confirms, each
  disposition `new:merged-double`. The counting arms then run the graded path, and S30's fallback stays
  AC21's to observe. The double's `twinFlags: []` landed at `2d992a209` (`TOOL-dFairHearing-1` pass
  (b)) and stays as it is.

## 3. Non-goals (OUT)

- No re-review: each item makes the corrected statement true and reopens no severity.
- No folding into the earlier specs: their criteria stand, each one this unit supersedes named by the
  hands-off bullet in that spec's §3 (§8 F7).
- No HIGH finding: ids 37, 39 and 40 are `TOOL-dFairHearing-20`, `-21` and `-22`.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No retirement of `tools/hooks/agent-cap.js` or of its exports; `topLevelArgs` stays where
  `TOOL-dFairHearing-16` F3 left it.
- No help page: `help/` covers neither the review harness nor the scorer factory.
- No rebuild of a **Landed** item: its criterion observes the landing, and a builder who finds one
  absent from the parent stops and reports it rather than building it here.

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
and writes `tools/workflows/tier2-review.template.js` too; it landed first, at `93531c2e8`, so this
unit's parent carries it.

### One contract per shared name (S1 to S3, S43)

`extract_tag_ref(text) -> (path, key) | None`, defined once, in `tools/workflows/replay_scorer.py`:

| `where` carries | `key` |
|---|---|
| a `[<tag>]` | the first one, as the string `'[<tag>]'` |
| no tag, a `§<n>` or `section <n>` | `n`, the integer `extract_section_ref` returns |
| neither | the ref is unscorable, `None` |

The path folds as `extract_section_ref` folds it: `\` to `/`, a drive prefix `C:/` to `/`, leading
`./` dropped (`derive_ref_parts`, `replay_scorer.py:199-208`). Through S43, a plant and a hit match by
the equality every known-set reader uses. Both landed before this unit (S1, S43).

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
one row `parse_candidates` reads, through the existing `measure_parsed` (`replay_scorer.py:885-896`).

### review.pin's two new flags (S5, S6, S46)

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

At this unit's commit the version carriers differ from its parent by no `KIT_*_VERSION = ` line and
no `gov:kit <kit>@` marker, and no commit of this build moved one (AC6). Other builds' landings since
`3708a705` moved them through their own mints; those are not this build's moves, and S12 restores none
of them. The carriers are those
`tools/check-kit-versions.sh` grades: S13's, `tools/hooks/agent-cap.js`, `tools/roles/roles_lib.py`,
and the `version:` line of `tools/workflows/tier2-review.template.js` with its render. This unit edits
none of the hooks and roles files.

### The slot count, one counter and one predicate (S34, S35, S42)

```
markers = render_lenses.py --markers <harness>          # line numbers, the renderer's own anchored regex
for each marker line: body = the literal from its "[" to the matching "]" in the blanked view
                      slots = topLevelArgs(body).length  # the gate's own, depth over ( [ {
                      red unless slots === LENS_SLOTS     # LENS_SLOTS = 5, its one home
```

The count moves from `check-verifier-fanout.sh` (:349-405, `measureSlots` and the shell `LENS_SLOTS`)
to `check-verifier-fanout.js` (S42); rule 2's bound, which `TOOL-dFairHearing-16` moved into that
file, reads the hook's exported `MAX_LENSES` (`tools/hooks/agent-cap.js:405`, exported at :911) at
`tools/workflows/check-verifier-fanout.js:189` and :419.

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

### The synthesis double (S50)

The double's `node -e` body maps `items` when it is an array, adding to each item
`grades: { <id>: <its severity> }` over its `ids`, after the arm's own `sed` edit of the item list has
run, so a moved id or a changed severity carries its grade with it. `dispositions` lists the ids of
`shape.confirmed` at or below `judged`, each `{ id, disposition: 'new:merged-double' }`: a `new:` slug
matching `CLASS_SLUG` (`tier2-review.template.js:2323`) and no handed slug, which `unclassed: refuse`,
the default, admits. The `absent` case keeps `items` out, so its arm still reads a dead synthesis.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_gate_token`, `check_ungated` | functions, `tools/memory-tree/gotchas.py` | `py.function`, OK |
| `--design-audit-runs`, `--design-audit-seed` | `review_pin.py` flags | none |
| `--markers` | `render_lenses.py` flag | none |
| `LENS_SLOTS` | constant, `tools/workflows/check-verifier-fanout.js` | none |
| `legCount` | probe return field | none |
| `matched` | manifest key | none |

`gateManifest` (S44) is reused from `tools/workflows/drift-audit-state.template.js:80`, not minted.
`WHOLE_DESIGN_LENSES` was minted by `TOOL-dFairHearing-18` at `b21501741` (S15).

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
- `tools/workflows/README.md`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `memory/guides/MERGE-BAR.md`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/govkit/registry.toml`
- `tools/run-gates/selftest-budgets.txt`
- `tools/run-gates/foreign-prefix.gov.test.sh`

`tools/workflows/tier2-review.js` and `memory/HYGIENE.md` are renders.

### Alternatives rejected

- **Two batch units, Python and JS** — §8 F1.
- **Fold each minor into its spec** — the owner's 2026-10-05 ruling (BUILD-METHOD M4) folds none.
- **One bumping unit per kit (S12)** — §8 F5; specs 4, 5, 13, 17 and 18 carry the no-bump non-goal.
- **A parity arm holding a Python and a JS marker regex equal (S35)** — §8 F6.
- **Leaving the double's items without `grades` (S50)** — S30's fallback would carry every counting
  arm, so those arms would grade the fallback and no arm the graded path the live synthesis takes.

## 5. Production-readiness checklist

- security — S46 and S49 refuse at argument boundaries; S22 copies an owner-landed key byte for byte;
  no new write path.
- perf / scale — one more python call per harness in the fan-out leg (S35).
- error / empty / loading states — every new refusal exits 2 or throws by name before any agent; a
  truncated checklist or leg list is announced, never used.
- observability — runs parsed of runs dispatched; one announced line per leg-list or checklist refusal.
- risks — S49's ceilings (§8 F4); a **Landed** item absent from the parent, which §3 stops on.
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none: every surface touched is new in this build or keeps its default.
- user docs — `tools/workflows/README.md` (manifest, replay section, review.pin's flags) and the docs
  S45 rewords (§3: no `help/` page).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory; a clone goes under `%TEMP%/<short name>`, a clone under the
scratchpad exceeding the Windows path limit. A bare script name is the
workflows kit's file under `tools/workflows/`; `$DREC` and `$SPEC` are §4's example subjects. `<unit>`
is this unit's commit and `<unit>~1` its parent, the tree the build pass starts from (`576f89da` when
rev-5 was written).

A criterion opening **Landed at** observes an item an earlier unit built (fix brief item 1). Its
`git merge-base --is-ancestor <sha> <unit>~1` half is read against the parent and is red when the
parent lacks that commit, the item then reopening as work §3 stops on; its probes at the tip are red
when this unit's diff undoes the landing. Every other criterion is red at `<unit>~1`, as its `figure:`
or `Red when:` line says.

- **AC1** — **Landed at** `af3831a6c`. When `git merge-base --is-ancestor af3831a6c <unit>~1` runs, it
  exits 0; and when a scratch python probe imports `replay_scorer.py`, `extract_tag_ref('x.md:§3 S2')`
  returns `('x.md', 3)` and `extract_tag_ref('x.md:[walk-table] plan.input')` returns
  `('x.md', '[walk-table]')`, and an `ast` walk over every tracked `*.py` under `tools/` finds
  `def extract_tag_ref` exactly once.
  Red when: the parent lacks the landing, the section fallback returns the string `'§3'`, or a second
  definition lands.
- **AC2** — When `python replay_scorer.py --experiment "$SCRATCH/rr.json"` runs a review-replay
  manifest of four candidates, each with a report and a `matched` list, arms `dispatched` 4, it prints
  `parsed <arm>: 4 of 4`; with one report's appendix cut, `parsed <arm>: 3 of 4`;
  and a manifest carrying an unknown key still exits 2 naming it.
  Red when: `parsed` counts known items, or a `candidates` list is refused, as at this unit's parent,
  whose `measure_replay_experiment` reads `candidates` as an object of arm to source.
- **AC3** — When `python review_pin.py --subject $DREC --design-record-preset whole-design --design-audit-runs 3 --design-audit-seed synthetic`
  runs, it prints three JSON lines, each `"preset": "whole-design"` with a `walk` of `runs` 3, `seed`
  `synthetic` and `run` 1, 2 and 3 in turn; `--design-audit-runs 4` exits 2 naming the flag; and
  without `whole-design` no line carries `walk`.
  Red when: one line prints for three runs, a run index repeats, or the flag is unknown, as at the
  parent.
- **AC4** — When `grep -c` counts `legCount`, and then `a pipe written as`, over
  `tier2-review.template.js` and `tier2-review.js`, each pair prints equal counts of at least 1.
  Red when: the template is edited and its render is not, so a pair differs, or neither file carries
  the string.
  figure: DERIVED at observation; at `576f89da` all four counts are 0.
- **AC5** — **Landed at** `ef757de0c` and `4a0e73da6`. When `git merge-base --is-ancestor` runs for
  each against `<unit>~1`, both exit 0; and when `review_pin.py --subject $SPEC --unclassed reason` and
  the same `--subject` with `--twin always` run, each prints one JSON line carrying its key, and with
  the `--subject` alone the line is exactly `{"preset": "unit-spec"}`.
  Red when: the parent lacks a landing, or a key prints with its flag absent.
- **AC6** — When `git diff -U0 <unit>~1 <unit> -- tools/hooks tools/roles .claude/skills/build tools/workflows/tier2-review.template.js | grep -E '^[-+].*(KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@)'`
  runs, it prints nothing; and the same `grep` over
  `git log -p --no-merges --grep='^tool(dFairHearing)' 3708a705..<unit> -- <the same paths>` prints
  nothing.
  Red when: this unit's diff, or any commit of this build, hand-bumps a carrier; staged as a scratch
  commit on `<unit>~1` moving one carrier's version line, which the first command then prints.
  figure: the second half's population is DERIVED by `git log`; at `576f89da` it prints nothing over
  the 24 `tool(dFairHearing)` commits landed so far, while other builds' landings moved review-harness
  `1.53` to `1.56`, roles `1.8` to `1.12` and agent-cap `1.40` to `1.42`, which red base `3708a705`'s
  whole-tree diff.
- **AC7** — **Landed at** `9ce7710ab`. When `git merge-base --is-ancestor 9ce7710ab <unit>~1` runs, it
  exits 0; and when `python render_lenses.py` renders a scratch template holding a
  `= [ // gov:lens-optins` marker above a `{{LENS_SLOTS}}` token beside the shipped markers, it exits 0;
  a token with neither marker above it exits 2 naming rule 11.
  Red when: the parent lacks the landing, the opt-in marker is refused, or the orphan passes.
- **AC8** — **Landed at** `b21501741`. When `git merge-base --is-ancestor b21501741 <unit>~1` runs, it
  exits 0; when `grep -n "gov:lens-slots whole-design" tier2-review.js` runs, it prints the
  `WHOLE_DESIGN_LENSES` marker line; a scratch prelude probe with `preset: 'whole-design'` and a valid
  `walk` selects that literal, and `preset: 'no-such-preset'` throws naming `preset`; and
  `bash check-verifier-fanout.sh tier2-review.js` exits 0 at the tip, counting 4 marked literals over
  S35's and S42's counter.
  Red when: the parent lacks the landing, or the whole-design rows name a literal no marker declares,
  so the render refuses, or the moved counter miscounts the shipped literals.
- **AC9** — **Landed at** `886c11fea`. When `git merge-base --is-ancestor 886c11fea <unit>~1` runs, it
  exits 0; and when a scratch probe collects the labels
  `git grep -hoE '^check(_spec_audit)? "rule[05]:[^"]*"' 3708a705 -- tools/hooks/agent-cap.test.sh`
  prints, 24 for rule 0 and 4 for rule 5, then at tip `grep -cF "<label>" spec-audit-optin.test.sh`
  prints at least 1 per rule 0 label, `grep -cF "<label>" check-review-join.test.sh`
  at least 1 per rule 5 label, and `grep -cF "<label>" tools/hooks/agent-cap.test.sh` 0 for all 28; and
  `grep -c "gov:fixed-verifiers\|gov:sequential-agents" tools/hooks/agent-cap.test.sh check-verifier-fanout.test.sh`
  prints, for the hook's suite, less than base's 42, a drop no larger than the fan-out suite's rise from
  base's 1. On a staged break, one rule 0 arm deleted from a scratch copy of its receiving suite, the
  probe names that label.
  Red when: the parent lacks the landing, a moved arm stays in the hook's suite, or one is deleted
  rather than moved.
  figure: the base counts are PINNED, measured at `3708a705` on 2026-10-23; at `576f89da` the hook's
  suite counts 1 and the fan-out suite 45.
- **AC10** — When the recipe in `tools/workflows/README.md`'s replay section runs with `<name>` `fhr`
  and `<commit>` `3708a705`, `git -C "$TEMP/fhr" rev-list --count fhr` prints a number above 0, and
  `git show-ref refs/replay/fhr` in this repository prints nothing afterwards; and
  `grep -c "clone --branch" tools/workflows/README.md` prints 0.
  Red when: the README carries no replay section, as at the parent, or its recipe clones a
  `refs/replay/` ref with `--branch`, which exits 128.
- **AC11** — **Landed at** `3745b407a`. When `git merge-base --is-ancestor 3745b407a <unit>~1` runs, it
  exits 0; when a scratch prelude probe calls `deriveRoundState([4, 3, 2], 1, 3)`, it returns
  `CEILING`; and `grep -n "CEILING lies outside" tier2-review.test.sh` prints a line of the parity arm's
  header comment, the arm's token assertion naming the four in-domain tokens and no `CEILING`.
  Red when: the parent lacks the landing, or the arm demands all five tokens over a domain where
  `CEILING` cannot occur.
- **AC12** — When a scratch python probe imports `tools/memory-tree/gotchas.py`, `check_ungated` reads
  a body "Gated by `tools/check-wiring.sh`." as gated, "There is no machine gate." as ungated, and
  "Gated by `no-such-gate.sh`." as ungated; and an `ast` probe finds `check_invariant`'s body calling
  `check_gate_token`.
  Red when: a class gated by a tracked path joins the ungated population, or the function is absent,
  as at the parent.
- **AC13** — When `node spec-audit-optin.js < "$SCRATCH/replay1.json"` runs over a spec-audit payload
  whose `repo` is a clone the recipe made with S22's README added and whose `reviewDir` is S22's, it
  exits 0; with `reviewDir` `memory/builds/dClosedLoop/reviews` it exits 2 naming `authorized-by: prompt`;
  and `grep -c "memory/builds/dFairHearing/reviews" tools/workflows/README.md` prints at least 1, the
  replay section's placement.
  Red when: the replay's placement is still dClosedLoop's prompt-authorized README, or the README
  states none.
  fixture: the clone under `%TEMP%/fhq`, made by the probe.
  figure: at `576f89da` the grep prints 0.
- **AC14** — When `sed -n '/^mkfix() {/,/^}/p' check-verifier-fanout.test.sh | grep -c "gov:lens-slots"`
  runs, it prints 1, the `mkfix` harness's marked literal; and a scratch fixture as `mkfix` writes it,
  run whole-tree by its gate copy, exits 0, and exits 1 naming the missing marker with that literal cut.
  Red when: the whole-tree fixtures carry no marked literal, so the no-marker red fires on unit 13's
  AC2 and AC3 arms.
  figure: at `576f89da` the first command prints 0.
- **AC15** — When `grep -n "render_lenses.py" unattended-build.test.sh` runs, it prints
  `build_layout`'s copy line beside `lenses.toml`; and a scratch directory holding that copy set renders
  `tier2-review.template.js`, exit 0, and exits 2 without `lenses.toml`.
  Red when: a layout lacks the catalogue, so its parity render fails.
  figure: at `576f89da` the grep prints nothing.
- **AC16** — When a scratch probe calls `replay_scorer.scan_pairing_sites` with the root at this
  repository's root, and at `tools/workflows`, neither returns a site under `memory/`.
  Red when: the population is the tool root's tree, so aScoutedSeam's bench sites are named.
  figure: at `576f89da` the root call returns two, both in
  `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py`.
- **AC17** — When `grep -n "spec-audit opt-in pack self-test" tools/govkit/registry.toml tools/run-gates/selftest-budgets.txt tools/run-gates/foreign-prefix.gov.test.sh`
  runs, it prints the `[[exempt_leg]]` name line, the budget row and the `WHOLE_RUN` row.
  Red when: a meta-gate file lacks the leg, so govkit's descriptor check or the budget check reds.
  figure: at `576f89da` it prints nothing.
- **AC18** — When `grep -cE 'cp [^#]*check-verifier-fanout\.js' check-verifier-fanout.test.sh` and
  `grep -cE 'cp [^#]*render_lenses\.py' check-verifier-fanout.test.sh` run, each prints at least 3, one
  per gate-copying fixture; `grep -c "no check-verifier-fanout.js beside this gate" check-verifier-fanout.test.sh`
  prints at least 1, the new arm's expected line; and a scratch copy of `check-verifier-fanout.sh` with
  no `.js` beside it, run over a harness, exits 2 naming `check-verifier-fanout.js`.
  Red when: a fixture copies the gate alone, so the gate exits 2 before the arm's own question, or the
  missing `.js` prints clean.
  figure: at `576f89da` the three greps print 0; the gate's exit 2 landed at `886c11fea`, so the last
  half is green at the parent and the arm observing it is what this unit adds.
- **AC19** — When `grep -n "gotchas.py --for-diff" memory/guides/SESSION-KICKOFF.md` runs, the line
  it prints no longer says "run before a review".
  Red when: that line still tells a reader to run the checklist before a review, as at the parent.
- **AC20** — **Landed at** `e21580aac`, `9ce7710ab` and `c70d6a020`. When
  `git merge-base --is-ancestor` runs for each against `<unit>~1`, each exits 0; and
  `grep -c "3708a705" tier2-review.test.sh` prints 0, while the arms labelled
  `preset: unit-spec, absent or named, derives one key`,
  `optIn: AC5 a swap moves the review key, and a run without one keeps the key` and
  `lens notes: AC7 the flat and the per-preset form of one note derive one review key` each compare two
  keys the current render derives in the suite's own run.
  Red when: the parent lacks a landing, or an arm compares with base's harness or a literal key, so
  `TOOL-dFairHearing-5`'s bump reds it.
- **AC21** — When a scratch stub run of `tier2-review.js` hands its tally one item with no `grades`
  and one with `grades: null`, each places its ids at the item's severity, a WARNING naming the item.
  Red when: `String(it.grades[String(id)])` throws a TypeError on either, as at the parent.
- **AC22** — When a scratch stub run's resume probe returns `legs: []`, a list one short of `legCount`,
  a list with a duplicate, or one with a non-string, each run announces no leg manifest and admits no
  `gate:` disposition on it; a full list matching `legCount` admits the valid gate.
  Red when: a truncated list refuses a valid gate or admits an invented one, as at the parent, whose
  filter keeps a truncated list as the manifest.
- **AC23** — When `grep -n "a pipe written as" tier2-review.js` runs, it prints the reason-cell
  instruction; and a scratch stub synthesis returning a reason with a raw `|` gets `dispositions: null`,
  its note naming the appendix as needing a re-render.
  Red when: a piped reason reaches the appendix unrefused.
  figure: at `576f89da` the grep prints nothing.
- **AC24** — **Landed at** `af3831a6c`. When `git merge-base --is-ancestor af3831a6c <unit>~1` runs, it
  exits 0; and when a scratch probe calls `read_raw_output` with an existing drive-lettered path under
  `$SCRATCH`, it reads the file; with `HEAD:README.md` or a 40-hex blob id, the blob.
  Red when: the parent lacks the landing, or the drive-lettered path is read as `<rev>:<path>` and
  refused.
- **AC25** — When the fan-out gate runs over a scratch literal of five
  `deriveSlotLens('unit-spec', { key: 'a', brief: 'b, c' })` elements under a marker, it reads 5; and in
  a scratch layout `$SCRATCH/k/workflows/` holding copies of `check-verifier-fanout.sh`,
  `check-verifier-fanout.js` and `render_lenses.py` beside `$SCRATCH/k/hooks/agent-cap.js`, with the
  copied `topLevelArgs` edited to split on every comma, the copied gate over the same file names the
  literal as holding more than 5 slots.
  Red when: a comma inside parentheses or braces counts as a slot, or the count runs on a lexer other
  than `topLevelArgs`, so the staged edit leaves it at 5, as at the parent, where `measureSlots` in
  `check-verifier-fanout.sh` counts.
  fixture: the scratch layout, made by the probe; the tree holds none.
- **AC26** — When `python render_lenses.py --markers "$SCRATCH/h.js"` runs over a file whose comment
  names `gov:lens-slots` above a valid marked literal, it prints only the literal's line; and the
  fan-out leg over that file exits 0.
  Red when: the comment line is walked from a bracket it does not open, or the flag is unknown, as at
  the parent.
- **AC27** — When a scratch stub run's acquiring agent returns the real `gotchas.py --for-diff` stdout
  cut inside its item list, or before the `# by design —` head, the run logs a `checklistError`
  WARNING and passes no checklist; whole, it is accepted.
  Red when: a tail-truncated return passes as complete, as at the parent, which admits any return
  holding one `- ` line.
- **AC28** — **Landed at** `7b2153c28`. When `git merge-base --is-ancestor 7b2153c28 <unit>~1` runs, it
  exits 0; `grep -n "resume:checklist" tier2-review.js` prints the label of an agent call that passes
  `probeOpts`; and `grep -n "const STAGE_OPTS = " tier2-review.test.sh` prints
  `TOOL-dFairHearing-11`'s arm still listing exactly the four constants `probeOpts`, `findOpts`,
  `verifyOpts` and `synthOpts`.
  Red when: the parent lacks the landing, a fifth options constant appears, or the agent spawns untyped.
- **AC29** — **Landed at** `4a0e73da6`. When `git merge-base --is-ancestor 4a0e73da6 <unit>~1` runs, it
  exits 0; and when a scratch python probe loads `tools/workflows/kit.toml` with `tomllib`, the
  `tier2-review.template.js` row's placeholder list holds `TOOL_ROOT` exactly once.
  Red when: the parent lacks the landing, the token is declared twice, or the row lacks it.
- **AC30** — **Landed at** `c70d6a020`. When `git merge-base --is-ancestor c70d6a020 <unit>~1` runs, it
  exits 0; when `python tools/memory-tree/gotchas.py --report` runs, its `dead anchors` section names
  none of `portability-sweep.md`, `topology-sweep.md` and `adopter-migration-sweep.md` under
  `memory/gotchas/`; and `gotchas.py --for-paths` over one anchor of each selects it.
  Red when: the parent lacks the landing, or a record's anchor selects no tracked path.
- **AC31** — When `grep -n "DESIGN_RECORD_PRESET" review_pin.py tools/workflows/README.md` runs, it
  prints the constant and a line of the replay section naming it as replay 1's flip, which
  `grep -n "DESIGN_RECORD_PRESET" tools/workflows/README.md | grep -c "replay 1"` counts at least 1;
  and the template's `preset` default literal reads `unit-spec`.
  Red when: replay 1's verdict flips a template default, or the README names no flip site for it.
  figure: at `576f89da` the counting command prints 0; the README's one line naming the constant
  (:522) names no replay.
- **AC32** — **Landed at** `af3831a6c`. When `git merge-base --is-ancestor af3831a6c <unit>~1` runs, it
  exits 0; and
  `python -c "import sys; sys.path.insert(0, 'tools/workflows'); import replay_scorer as r; print(r.extract_tag_ref(r'C:\x.md:[a] then [b]'))"`
  prints the path `'/x.md'` and the key `'[a]'` as one tuple.
  Red when: the parent lacks the landing, the ref reads the second tag, or the probe raises before
  reaching the reader.
- **AC33** — When `grep -c "measureSlots\|MAX_LENSES" check-verifier-fanout.sh check-verifier-fanout.js`
  runs, each file prints 0, and `grep -c "LENS_SLOTS = " check-verifier-fanout.js` prints 1.
  Red when: a second counter or a second home for 5 remains.
  figure: at `576f89da` the first command prints a count above 0 for each file and the second 0.
- **AC34** — **Landed at** `b21501741`. When `git merge-base --is-ancestor b21501741 <unit>~1` runs, it
  exits 0; when an `ast` probe reads `measure_design_recall` in `replay_scorer.py`, its body calls
  `measure_recall`; and the fixture of `TOOL-dFairHearing-18` AC8 still prints 2 of 3 per run and
  exits 1.
  Red when: the parent lacks the landing, or the grade matches plants with its own loop.
- **AC35** — When `grep -c "legManifest" tier2-review.js` runs, it prints 0, and the
  args header carries `gateManifest:` as a key line.
  Red when: the harness keeps a second spelling of the input.
  figure: at `576f89da` the grep prints 14.
- **AC36** — When `git grep -n "run before a review\|Before a review, run\|Hand a reviewer the classes" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md`
  runs, it prints nothing, and each file names the harness acquiring the checklist.
  Red when: a doc still sends a reviewer to run the lookup by hand, as all four do at the parent.
- **AC37** — When `python review_pin.py --subject 'memory\builds\dX\spec\2026-01-01-spec-TOOL-dX-1.md'`
  runs, it exits 2 and its stderr names the backslash.
  Red when: the backslashed spec path is classified as a design record, as at the parent, which exits
  0.
- **AC38** — **Landed at** `c70d6a020`. When `git merge-base --is-ancestor c70d6a020 <unit>~1` runs, it
  exits 0; and when a scratch prelude probe passes `lensNotes: { 'unit-spec': null }` and then
  `lensNotes: { 'unit-spec': 'x' }`, each throws naming `lensNotes` before the first agent.
  Red when: the parent lacks the landing, or `|| {}` turns either into an empty note set.
- **AC39** — When a scratch probe of `deriveAddressKey` keys `{ file: '<repo>/src/a.js' }` and
  `{ file: 'src/a.js' }` under `repo` `C:/R`, and `{ file: 'c:/R/src/a.js' }` the same way, all three
  keys are equal.
  Red when: a repo-absolute path or a lower-case drive letter keys apart, as at the parent.
- **AC40** — When a scratch prelude probe passes a `walk` whose run-1 slice for one walker holds 201
  cells, a scenario `name` of 121 characters, or a `walks` of 601, each throws naming the field and its
  ceiling before the first agent; 200, 120 and 600 proceed.
  Red when: an oversized grid reaches the walkers, as at the parent.
  figure: the ceilings are PINNED by §8 F4, against the 812-cell walk measured by the audit.
- **AC41** — When a scratch shell sources `build_merged_returns`, sliced from
  `tools/workflows/unattended-build.test.sh:968-986` by `sed -n '/^build_merged_returns() {/,/^}$/p'`,
  and a node probe reads its output for the suite's `MT_MERGED`, the `synth` value carries
  `dispositions`, one `{id, disposition}` for each of the 13 ids
  the skeptic double confirms, each `new:merged-double`, and every item carries `grades` mapping each of
  its ids to its severity; for `build_merged_returns '[]' 0` the `dispositions` list is empty; and for
  `build_merged_returns absent` the `synth` value carries no `items`.
  Red when: the double returns no `dispositions`, so the strict runner hands the harness a null
  synthesis and the `MT` liveness arm reads `the synthesis agent died`, or an item lacks `grades`.
  figure: at `576f89da` the `synth` value carries neither `dispositions` nor any `grades`.

## 7. Gates

`kit/dogfood doc parity` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `verifier fan-out` · `spec-audit opt-in pack self-test` · `review-replay selftest` · `gotchas selftest` · `review-protocol parity (kit vs dogfood)` · `kickoff-manifest ratchet` · `foreign-prefix parity (every self-test at three prefixes)` · `govkit selfcheck` · `every held leg is budgeted, every budget row resolves` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC21 AC22 AC23 AC27 AC39 AC40 · each covered AC's red case, staged against the harness at this unit's parent · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC2 AC16 · each covered AC's red case, staged against the factory at this unit's parent · that runner's declared arm count, raised by the arms added
New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC14 AC18 AC25 AC26 · the marked mkfix literal, a gate copy with no `.js`, a five-call literal, and a comment naming the marker, staged against the gate at this unit's parent · none
New arm: tools/workflows/unattended-build.test.sh · covers AC15 AC41 · a layout without `lenses.toml`, and the synthesis double without `dispositions`, which the existing `MT` liveness arm reads as dead, staged against the suite at this unit's parent · none
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC12 · a class gated by a tracked path and one gated by an untracked token, staged against base's gotchas.py, which has no `check_ungated` · none

The leg line is the set the §4 files' guards trip, derived from `tools/gate-legs.json` at `576f89da`
with its broad guards excluded, plus the legs grading this unit's own changes. `review-replay selftest`
and `spec-audit opt-in pack self-test` carry no guard and are named for the arms and rows S25 and S26
add. No leg of the hooks kit is named: §4 edits no file under `tools/hooks/`.

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
  for a spec-audit minor. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the round-1 spec audit's 37 MEDIUM and 12 LOW findings
  as one batch.
- rev-2 · 2026-10-23 · §3 · the audit of units 20 to 23 disposed: hands-off edges to TOOL-dFairHearing-25, -26 and -27.
- rev-3 · 2026-11-03 · S28 · AC19 · the `last-audit:` re-stamp after `tools/gate-legs.json` moves to
  TOOL-dFairHearing-16 S9, because the pre-commit leg refuses a commit that stages a watched file
  without a re-stamp, so no later unit can carry it. S28 keeps line 99 and schedules no re-stamp.
  AC19 drops its stamp half, which could never pass: a bundled stamp names the bundling commit's
  parent, so `git log <sha>..HEAD` over the watched files always lists that commit (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-16-2-fix-brief, item 3).
- rev-4 · 2026-11-03 · §7 · the leg line adds `policy fixtures`, whose guard §4's
  `tools/workflows/kit.toml`, `tools/memory-tree/gotchas.py`, `tools/govkit/registry.toml`, the hooks
  and `tools/roles/roles_lib.py` trip (2026-11-03-prompt-TOOL-dFairHearing-10-sweep-fix-brief,
  item 1).
- rev-4 · 2026-11-03 · S22 S24 S26 S27 S28 S42 S44 S45 S46 · §4 · §10 · every line re-cited at
  `9c1a2857`: rule 6's header and `MAX_LENSES` at the hook's new lines, and `topLevelArgs` and rule
  2's bound in `check-verifier-fanout.js`, where `TOOL-dFairHearing-16` moved them, in place of the
  hook's `:1362-1380`, past its end today; the kickoff guide's checklist line by its command
  (same brief, items 2 and 4).
- rev-4 · 2026-11-03 · AC19 · the line is found by its command, `gotchas.py --for-diff`, not by
  number: it sits at :100 at `9c1a2857`, so `sed -n 99p` read another line and passed unread (same
  brief, item 2).
- rev-4 · 2026-11-03 · AC6 · §4 · the diff is pinned to this unit's parent, and the build-wide half
  reads only this build's own commits: base `3708a705`'s whole-tree diff is red today through other
  builds' version mints, which no unit of this build made (same brief, item 3).
- rev-5 · 2026-11-03 · §6 · §3 · the **Landed** form: a criterion observing an earlier unit's landing
  reads `git merge-base --is-ancestor` against `<unit>~1`, and §3 stops a builder who finds one absent.
  Each landed item keeps its scope item and criterion, so the ids later specs cite stay put (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-23-fix-brief, items 1 and 4).
- rev-5 · 2026-11-03 · S1 S2 S3 · AC1 · landed at `af3831a6c` and consumed at `b21501741`; unit 18's
  AC7 tag-shape hand-off is named in S1 (same brief, items 3 and 4).
- rev-5 · 2026-11-03 · S11 · AC5 · landed at `ef757de0c` and `4a0e73da6`; AC5 already printed its
  keys only with their flags at `576f89da` (same brief, item 4).
- rev-5 · 2026-11-03 · S14 · AC7 · landed at `9ce7710ab`, `render_lenses.py:28` admitting the opt-in
  marker; AC7's orphan names rule 11, as the renderer's refusal does (same brief, item 4).
- rev-5 · 2026-11-03 · S15 · AC8 · landed at `b21501741`: the literal, its receiver branch and the
  suite's `no-such-preset` arm. AC8 keeps the gate run at the tip, which S35 and S42 move (same brief,
  item 1).
- rev-5 · 2026-11-03 · S16 · AC9 · §7 · landed at `886c11fea`; the `New arm:` lines on
  `spec-audit-optin.test.sh` and `check-review-join.test.sh`, and AC9 on the fan-out line, leave §7, as
  no arm moves here (same brief, item 4).
- rev-5 · 2026-11-03 · S19 S20 · AC11 · landed at `3745b407a`, whose builder took the four-token arm;
  unit 17's AC6 hand-off is named in S19, and AC11 passes at `576f89da`: the header comment (:497)
  carries `CEILING lies outside` and row :463 holds `CEILING` (same brief, item 2).
- rev-5 · 2026-11-03 · S29 · AC20 · landed with the three arms at `e21580aac`, `9ce7710ab` and
  `c70d6a020`, each comparing two keys of the current render; AC20's `REVIEW_SHAPE` grep is gone, as no
  arm reads the literal, and the arms are named by label (same brief, item 4).
- rev-5 · 2026-11-03 · S33 · AC24 · landed at `af3831a6c`, `read_raw_output` already resolving in S33's
  order (same brief, item 4).
- rev-5 · 2026-11-03 · S37 · AC28 · landed at `7b2153c28`; AC28's second grep reads the `STAGE_OPTS`
  line, which the old pattern matched only through `synthOpts` (same brief, items 4 and 5).
- rev-5 · 2026-11-03 · S38 · AC29 · landed at `4a0e73da6`, `TOOL_ROOT` once in kit.toml's row (:84);
  `tools/workflows/kit.toml` leaves §4 (same brief, item 1).
- rev-5 · 2026-11-03 · S39 · AC30 · landed at `c70d6a020`; AC30 reads the report's `dead anchors`
  section, the one it prints, in place of an inert-anchor list it does not (same brief, items 4 and 5).
- rev-5 · 2026-11-03 · S41 · AC32 · landed at `af3831a6c`, the raw-string probe printing
  `('/x.md', '[a]')` at `576f89da` (same brief, item 4).
- rev-5 · 2026-11-03 · S43 · AC34 · landed at `b21501741` (same brief, item 4).
- rev-5 · 2026-11-03 · S47 · AC38 · landed at `c70d6a020`, `tier2-review.template.js:1265-1283`
  already refusing a null or string entry (same brief, item 4).
- rev-5 · 2026-11-03 · S7 S8 S9 S10 · AC4 · AC4 counts `legCount` and `a pipe written as`, strings
  this unit adds, so it is red at the parent; `WALK_RULES` and `roundState` already counted equal.
  Unit 17's AC9 and unit 18's AC10 render-diff halves are named in S7 and S9 as met by their builds
  (same brief, items 3 and 4).
- rev-5 · 2026-11-03 · S12 S13 · AC6 · §4 · no commit of this build moved a carrier, so nothing is
  restored; the hooks and roles files and `.claude/skills/build/SKILL.md` leave §4, and AC6 names how
  its red is staged (same brief, items 4 and 5).
- rev-5 · 2026-11-03 · S23 · AC14 · unit 13's hand-off named; the explicit-files clause for the
  non-workflow arm is gone, as that arm asserts a line the gate prints before its slot verdict; AC14
  counts the marker inside `mkfix` itself, where a whole-file grep already printed two other arms'
  markers (same brief, item 3).
- rev-5 · 2026-11-03 · S27 · AC18 · unit 16's hand-off named; AC18 counts the fixtures' `cp` lines of
  the `.js` and `render_lenses.py` and the new arm's expected line, all 0 at the parent, in place of a
  grep that already printed 5 through comments (same brief, items 3 and 4).
- rev-5 · 2026-11-03 · S26 · AC17 · unit 16's hand-off named and re-grounded: none of the three rows
  exists at `576f89da`, the leg is unguarded, and `TOOL-dFairHearing-27` S4 later supersedes the
  `WHOLE_RUN` half (same brief, item 3).
- rev-5 · 2026-11-03 · S28 · the re-stamp clause leaves S28: unit 16 bundled its own at `886c11fea`
  (its rev-7 S9), and this unit's §4 stages no watched file (same brief, item 1).
- rev-5 · 2026-11-03 · S30 · AC21 · unit 6's hand-off named; S30's fallback holds, and it is a
  fallback rather than a refusal. Unit 6's §4 Migration, which called the fallback unit 6's own, is
  corrected at that spec's rev-3 (same brief, item 2).
- rev-5 · 2026-11-03 · S50 · AC41 · §4 · §7 · units 6 and 8's hand-off on the synthesis double, which
  returns no `grades` and no `dispositions`, so the unattended-build self-test reads a dead synthesis;
  its `twinFlags: []` landed at `2d992a209` (same brief, items 1 and 2).
- rev-5 · 2026-11-03 · S34 · AC25 · the depth tracking landed at `864f43d25`; AC25 adds a staged edit
  of the copied `topLevelArgs`, which the parent's `measureSlots` ignores (same brief, item 4).
- rev-5 · 2026-11-03 · S22 · AC13 · AC13 adds the README's placement grep, 0 at the parent, as the
  pack's own exits already held there (same brief, item 4).
- rev-5 · 2026-11-03 · S40 · AC31 · AC31 counts a README line naming the constant as replay 1's flip,
  0 at the parent, whose line :522 names no replay (same brief, item 4).
- rev-5 · 2026-11-03 · AC2 AC3 AC10 AC12 AC15 AC16 AC17 AC19 AC21 AC22 AC23 AC26 AC27 AC33 AC35 AC36
  AC37 AC39 AC40 · each states its red at the parent, measured at `576f89da` (same brief, item 4).
- rev-5 · 2026-11-03 · S1 S13 S19 S22 S24 S27 S33 S42 S46 · §4 · §10 · every cite re-grounded at
  `576f89da`: `MAX_LENSES` at `agent-cap.js:405`, `specsRule` at template :849, `build_layout`'s copy
  at :2133-2134, and `extract_section_ref` at `replay_scorer.py:211-221`, where `TOOL-dFairHearing-12`
  moved it from `review_replay.py:100-115` (same brief, item 5).
- rev-5 · 2026-11-03 · §7 · §4 · the leg line re-derived from the guards §4's files trip at
  `576f89da`, the hooks-kit legs leaving with the hooks files and `spec-audit opt-in pack self-test`
  joining for S26; the `New arm:` lines name only criteria red at the parent. §4's "Why one unit" notes
  `TOOL-dFairHearing-20` landed at `93531c2e8`, and the Inventory leaves `WHOLE_DESIGN_LENSES` to unit
  18 (same brief, item 5).
- rev-6 · 2026-11-03 · AC41 · the sliced file is cited as `tools/workflows/unattended-build.test.sh:968-986`,
  the function's span at `576f89da`, in place of the bare filename the spec-tokens BAR pattern read as a
  suite run; the `sed` slice and what it observes are unchanged, and no other §6 token matches the
  pattern (fix brief 2026-11-03-prompt-TOOL-dFairHearing-23-2-fix-brief, items 1 to 3).

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries, and none adds a module: the
factory `tools/workflows/replay_scorer.py` and its `measure_recall`, `read_raw_output` and
`extract_section_ref` (`tools/workflows/replay_scorer.py:211-221`, moved there from
`review_replay.py` by `TOOL-dFairHearing-12`); agent-cap's exported
`topLevelArgs`, moved from the hook by `TOOL-dFairHearing-16`
(`tools/workflows/check-verifier-fanout.js:737`), already tracking `(`, `[` and `{`;
`check_invariant`'s token resolution (`tools/memory-tree/gotchas.py:432-440`); the harness's
`specsRule` (`tools/workflows/tier2-review.template.js:849`); drift-audit-state's `gateManifest`
(`tools/workflows/drift-audit-state.template.js:80`); the suite's own synthesis double
`build_merged_returns` (`tools/workflows/unattended-build.test.sh:968-987`), extended in place; and the
sibling rows of `tools/govkit/registry.toml` and `tools/run-gates/selftest-budgets.txt`.
`tools/codebase-map/reuse_lookup.py` over "count the top level elements of an array literal string
aware" and "decide whether a bug class record names a gate" ranked generic stems and
`check_gate_wall`, missing `topLevelArgs` and S21's inline resolution, which the source read found.
Recall returned specs 3, 12 and 16, missing `TOOL-aBatchedTribunal-1d`
(`memory/archive/DECISIONS.2026-08-10.md:50`), the one-counter-per-gate ruling S42 follows.

Recall terms used: `python tools/memory-recall/query.py "spec audit minors on the review harness scorer factory and lens catalogue" --terms "extract_tag_ref review_pin lens-slots topLevelArgs gotchas ungated replay bundle clone opt-in pack kit version mint"`
