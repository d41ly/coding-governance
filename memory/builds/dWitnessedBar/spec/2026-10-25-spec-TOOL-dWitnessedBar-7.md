# TOOL-dWitnessedBar-7 — `test.seen-red` reading one seen-red record per gate a build adds or changes, the acceptance-ledger line standing in for `build.acceptance`

**Status:** CLOSED · rev-6 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 26 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0345@72933671 whole
**Carries:** node:item.test.seen-red
**Carries:** node:record-kind.seen-red

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md](../build/2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-7-deviation-72.md](../build/2026-10-25-build-TOOL-dWitnessedBar-7-deviation-72.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-7-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-7-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-7-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-7-1-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-7-red-fix-114.md](../build/2026-11-20-build-TOOL-dWitnessedBar-7-red-fix-114.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-7-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-7-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-7-reground3-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-7-reground3-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-7-reground3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-7-reground3-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

"A gate never seen red is not a gate" has no recorder (gap-test-06): the build method tells the main
loop to observe each new arm red and green and to record both in the acceptance ledger
(`memory/guides/BUILD-METHOD.md`, M8's "Observe the owed arms before the bar" paragraph), and nothing
keys that observation by leg or reads it back. This unit fixes the seen-red record's grammar, one
record per gate a build adds or changes, keyed by leg and red SHA, and builds `test.seen-red`, which
reads those records and turns red on a gate with none. Until dScopedBuild lands `build.acceptance` as
the record's writer, the main loop's acceptance-ledger line is the record (the owner's FK-4-12 and
FK-5-2). The same reader admits the empty armed population `ratchet (populated)` reds today, the
admission TOOL-dWitnessedBar-14 left to it (§8 F7).

## 2. Scope (IN)

- **S1** — The seen-red line, the record's one grammar (shared interface I16), a line of an
  `**Evidences:** <unit id>` block of a `journal` record:
  ``- seen-red — `<leg name>` — red `<sha>` — green `<sha>` — <the staged break>``, the leg its
  free-text manifest `name` (I2's join key), each SHA 8 to 40 lowercase hex, the break one line of
  prose. Stated once in `memory/HYGIENE.md`'s "Acceptance ledger" section, rendered from
  `tools/memory-tree/HYGIENE.template.md`; that section's "TWO forms and no third" rule grades an
  answer to a criterion, and the section says the seen-red line is no answer. Observed by AC1 and AC6.
- **S2** — `read_evidence_lines(text)` in `tools/memory-tree/tree_lib.py`: the `**Evidences:**`-block
  walk the ledger arm of `tools/memory-tree/deviation_join.py#read_population` does inline, extracted
  at this, its second Python instance, returning `(line number, unit, line)` for every line under an
  `**Evidences:** <unit>` block, its unit regex and its reset at a heading carried unchanged. The
  journal test stays with each caller, as `read_population` reads it from
  `tools/memory-tree/tree_lib.py#read_bindings`. The verb is `read`, which
  `python tools/lexicon/lexicon.py --suggest` admits, where it declares no `iter`.
  `deviation_join.py` calls it, its verdicts unchanged. Observed by AC5.
- **S3** — `tools/memory-tree/seen_red.py`, the reader. `read_seen_red_records(root)` returns every
  tracked journal record's seen-red lines, the records `tools/memory-tree/tree_lib.py#record_paths`
  lists and `read_bindings` binds `journal`, each walked by `read_evidence_lines`, as
  `{leg name: [(red sha, green sha, record path, line)]}`; a line opening `- seen-red` that breaks
  S1's grammar raises `ValueError` naming the record and the line. No journal record holds a seen-red
  line today: `git grep -n -- '^- seen-red' -- memory` finds two lines outside the population, a
  research record's prose bullet in
  `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` and §4's
  example in this spec. Observed by AC1 and AC6.
- **S4** — The gates a build adds or changes, `derive_owed_gates(root, slug, base)`: (a) every leg
  whose leg-manifest row at HEAD is absent at `base` or carries a different `argv`, the manifest the
  one `tools/memory-tree/routed_commits.py#resolve_leg_manifest` locates (`tools/gate-legs.json`
  here), its `base` bytes read through `tools/memory-tree/tree_lib.py#read_blobs_at`; and (b) every
  `New arm:` line of a spec under `memory/builds/<slug>/spec/`, resolved to the manifest legs whose
  `argv` holds the line's suite path, each `{prefix}` resolved through
  `tools/memory-tree/coverage_join.py#resolve_prefix_token` against the tool root
  `tools/memory-tree/legacy_ledger.py#derive_seed_prefix` derives; a line resolving to no leg is
  named and owes nothing. Observed by AC2 and AC3.
- **S5** — The join, `test.seen-red`'s check: `python tools/memory-tree/seen_red.py --build <slug>
  [--base <sha>]`, `base` defaulting to the `base:` fact of the build's `RUN.md`, its first line
  opening `base:` under the `## Run facts` heading (§8 F5). Each owed gate is joined to a seen-red
  line naming it, under any `**Evidences:**` block of a journal record of that build; an `(b)` gate is
  satisfied by a line naming any leg it resolved to. It prints one line per gate,
  `seen-red: <leg> · <red sha8> · <record>` or `seen-red: <leg> · NO RECORD`, and exits 1 on any
  `NO RECORD`, 0 when every gate has one, and 2 when it cannot answer (no base, a manifest the
  resolver does not locate or that does not read). An empty owed set prints
  `seen-red: <slug> adds or changes no gate · nothing joined` and exits 0, never silently. Observed by
  AC2, AC3 and AC4.
- **S6** — `python seen_red.py --fixture --plant <case>` builds a throwaway repository in the system
  temp directory and runs S5 over it, for the cases `seen`, `unseen-gate`, `unseen-arm`, `bad-line`
  and `empty` of §4. Observed by AC2, AC3, AC4 and AC6.
- **S7** — The item: `item.test.seen-red`'s actor is the command row `seen-red` of the memory-tree
  kit, written through TOOL-dDeclaredLoop-6 S3's factory, `python tools/playbook/core.py new command
  seen-red --kit memory-tree --run seen_red.py`. That factory writes through
  `tools/loop/factories.py#write_command` and runs the kind's gate, `loop command conformance`
  (`tools/loop/factories.py#check_commands`), which refuses a `run` git does not hold, so
  `seen_red.py` is staged first. TOOL-dDeclaredLoop-12's landed `[[item]]` row in
  `tools/loop/loop.toml` names `command:test.seen-red`, so the pass re-points it to
  `command:memory-tree.seen-red`. No kit descriptor holds a `[[command]]` row yet
  (`git grep -n '^\[\[command\]\]' -- 'tools/*/kit.toml'` finds none at `174f9d9e5`), so this row
  turns that leg from `unarmed` to green. The item's `[[stand-in]]` row stays: `loop.toml`'s header
  holds a stand-in until its owning build lands, and no landed unit of this build has edited the file
  (`git log cdfbd1cf..HEAD -- tools/loop/loop.toml` lists dDeclaredLoop commits only). Observed by
  AC7.
- **S8** — Check 23 stays blind to the line: its ledger awk, the `alledger` flattening
  (`tools/memory-tree/check-memory-hygiene.sh@2c5ed1a3a960:3618-3656`), closes the open answer at a
  line opening `- seen-red`, where today it adds every non-blank line under an open answer to that
  answer's tokens, so the line's tokens never join an `AC<n>` answer's token list. Observed by AC5.
- **S9** — The method points at the grammar: `BUILD-METHOD.md` M8's "Observe the owed arms" sentence
  records both observations as a seen-red line, naming HYGIENE as its grammar's home, and ends naming
  `seen_red.py --build <slug>` as the read-back, rendered from
  `tools/memory-tree/BUILD-METHOD.template.md`. The paragraph pays for its words in its own: the
  render measures 30717 bytes (PINNED 2026-11-20, `wc -c memory/guides/BUILD-METHOD.md` at
  `174f9d9e5`) against the 30720 its row in `tools/template-size-limits.txt` holds, so the paragraph
  grows by at most 3 bytes (DERIVED, the difference) and no other text of the method moves (§8 F6).
  Observed by AC7.
- **S10** — `ratchet (populated)` admits an empty armed population a seen-red record vouches for,
  the admission TOOL-dWitnessedBar-14 S8 left to this reader. `tools/memory-tree/ratchet.py#run_populated`
  calls `read_seen_red_records` once, at the first armed home holding no row; a registration whose
  `leg` the records name prints `<leg> · <population> · admitted · seen red at <red sha8> in <record>`,
  the first record the reader lists for it, and does not red. One they do not name keeps the `empty`
  line and exit 1, `EMPTY_TEXT` re-worded to `reads unarmed, no seen-red line names its leg`; a line
  the reader refuses exits 2, as `main` exits on a `ValueError`. The module docstring's "WHAT IT DOES
  NOT CHECK" sentence, the `run_populated` docstring and the `ratchet (populated)` row of
  `tools/memory-tree/README.md` say the same. The plant `populated-seen-red` joins
  `ratchet.py --fixture`. Observed by AC8.

## 3. Non-goals (OUT)

- `build.acceptance`, the executor that re-runs a planted red and writes the record: dScopedBuild's
  (packet Non-goals, Later builds named). This unit ships the stand-in and names the hand-over. The
  memory-tree kit's `acceptance` record kind, which `tools/loop/loop_witness.py` writes as that item's
  stand-in, is not this record: it holds re-run commands, never a leg's red and green.
- A typed record file for the kind in `tools/memory-tree/build_records.py` (§8 F2).
- Observing any arm: the main loop observes, as M8 says. This unit reads what it recorded.
- Routing a missing record to `build.fix-pass`: the item's route is TOOL-dDeclaredLoop-12's row.
- Deleting `item.test.seen-red`'s `[[stand-in]]` row: the build's landing does (S7).
- Grading the leg's guard, ceiling or other fields as a change to the gate (§8 F3).
- A new gate leg: the reader runs as the item's command and at the close, and its arms join the
  memory-hygiene self-test and the ratchet selftest.

### Edges

- **hands-off** `TOOL-dWitnessedBar-28` — `record-kind.seen-red`, read through `read_seen_red_records`, so a repository's leg is counted in its pack once a seen-red line names it
- **hands-off** external — dScopedBuild's `build.acceptance` takes over the write: it emits S1's fields, `Leg`, `Red`, `Green` and `Break`, and `read_seen_red_records` is the one reader it joins
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 11, 17, 20 and 29: `seen_red.py`'s suite-path rule and Gates-bounded arm reader, and the grant for its carrier edits, each a scope item of that unit
- **hands-off** `TOOL-dWitnessedBar-57` — its `memory/HYGIENE.md` and BUILD-METHOD carrier edits, whose commits' grant trailers the resolver and ledger minors batch observes (id 10)

## 4. Design

### The line

```markdown
**Serves:** journal TOOL-dX-4

**Evidences:** TOOL-dX-4
- AC1 — `python gov_tag.py --fixture --plant policy-ns-word` — exits 1 naming the plant
- seen-red — `playbook render selftest` — red `3f2b31b5` — green `3f2b31b5` — the `policy-ns-word` plant with its namespace row deleted
```

`red` is the commit over which the break was staged and observed red; `green` the commit at which the
arm read green once restored, usually the same. The key is `(leg, red)`: a second line for one leg at
another red SHA is a second observation, and both are kept.

### The owed set

```
(a) legs(HEAD) where name not in legs(base) or argv(HEAD, name) != argv(base, name)
(b) for each "New arm: <suite path> · ..." line in builds/<slug>/spec/*.md:
        legs(HEAD) whose argv, {prefix} resolved, contains <suite path>
```

The manifest at `base` is the one `resolve_leg_manifest` names, read in one `read_blobs_at` call. A
`New arm:` line's suite path is its first field, split on ` · `. Two legs sharing a script
(`playbook render wiring` and `playbook render selftest` both run `adopt-playbook.sh`) make one owed
gate satisfied by either name.

### The plants

| Case | Fixture | Exit |
|---|---|---|
| `seen` | a leg added past base, a journal line naming it | 0 |
| `unseen-gate` | a leg added past base, no line | 1, `<leg> · NO RECORD` |
| `unseen-arm` | a spec's `New arm:` line on an existing leg's suite, no line | 1, naming that leg |
| `bad-line` | a `- seen-red` line with no red SHA | 2, naming the record and line |
| `empty` | no leg added, no `New arm:` line | 0, the announced empty line |

### The admission

```
ratchet (populated), per registration whose home reads armed and holds no row:
    records = read_seen_red_records(root)        # read once, at the first such home
    reg.leg in records -> "<leg> · <population> · admitted · seen red at <red sha8> in <record>"
    otherwise          -> "<leg> · <population> · empty · " + EMPTY_TEXT, and the leg exits 1
```

`ratchet.py --fixture --plant populated-seen-red` runs one fixture three ways: a journal record's
seen-red line naming the registration's leg (exit 0, `admitted`), that line removed (exit 1, `empty`),
and the line's red SHA dropped (exit 2, the record named). The `populated-empty-armed` plant keeps its
fixture, which holds no seen-red line, and its exit 1.

### Inventory

Minted: the seen-red line grammar; `read_evidence_lines`; `tools/memory-tree/seen_red.py` with
`read_seen_red_records`, `derive_owed_gates` and the verbs `--build`, `--base`, `--fixture`,
`--plant`; the command row `seen-red` of the memory-tree kit; the ratchet plant
`populated-seen-red`. Naming cells: `read_evidence_lines`, `read_seen_red_records` and
`derive_owed_gates` each read OK from `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at `174f9d9e5`; the pass asks it of any other name it mints.

### Migration

Additive. Landed ledgers carry no seen-red line, so `seen_red.py --build` over a closed build names
its unrecorded gates; it is run on a build from this unit on, and is no gate over landed builds. A
population drained to no row reads `empty` until a seen-red line names its leg.

### Rollout

Live at landing as a command. The memory-tree kit's version moves, `KIT_MEMORY_TREE_VERSION` in
`tools/memory-tree/check-memory-hygiene.sh`, minted by the lander and never on the branch, as the
header of `tools/memory-tree/check-verdict-epoch.sh` states.

### Files touched (estimate)

- `tools/memory-tree/seen_red.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/ratchet.py` (S10, its plant and its two docstrings)
- `tools/memory-tree/README.md` (the `ratchet (populated)` row)
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `tools/memory-tree/BUILD-METHOD.template.md`, rendered to `memory/guides/BUILD-METHOD.md`
- `memory/HYGIENE.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/loop/loop.toml` (the `item.test.seen-red` row's actor, S7)
- `memory/map/generated/symbols.json` (re-rendered by the codebase-map kit's `gen_map.py --write`,
  which the unguarded `codebase-map coverage + freshness` leg reads)

Shared with sibling units: `tools/memory-tree/tree_lib.py`, `tools/memory-tree/HYGIENE.template.md`,
`memory/HYGIENE.md` and `memory/map/generated/symbols.json` with `TOOL-dWitnessedBar-1` (order 23,
landed at `ad3949b5f`, its edits the `gate-health` entry of `TYPED_RECORD_KINDS` and of the record-kind
list, neither the `**Evidences:**` walk nor the "Acceptance ledger" section);
`memory/map/generated/symbols.json` with `TOOL-dWitnessedBar-30` (order 24, landed at `7b918f7e0`);
and `tools/memory-tree/check-memory-hygiene.sh` with `TOOL-dWitnessedBar-29` (order 25, its
`check_cap_findings` and not check 23's awk), each of which lands before this unit; nothing with
`TOOL-dWitnessedBar-59`, `TOOL-dWitnessedBar-21` or `TOOL-dWitnessedBar-6`.

### Alternatives rejected

- **A new hygiene check beside check 23.** Check 23 is corpus-wide and runs on every push; the owed
  set is one build's range from its base, which a corpus-wide check has no base for.
- **Keying a record by the suite path.** I2 keys every record by leg `name`, and two legs share a
  suite.

## 5. Production-readiness checklist

- security — no write path: the reader reads tracked records and blobs through `read_blobs_at`; the
  fixtures write only under the system temp directory; the factory's one write is its guarded edit of
  `tools/memory-tree/kit.toml`.
- perf / scale — one `git ls-files`, one read per journal record of the build, one `git cat-file
  --batch` for the base manifest; `ratchet (populated)` reads the records only once an armed home
  holds no row. The arms join two suites under their manifest ceilings (PINNED 2026-11-20):
  300 s for `ratchet selftest` and 4800 s for `memory-hygiene self-test`, PINNED in `tools/gate-legs.json`.
- error / empty / loading states — an empty owed set is announced and exits 0; no base or a manifest
  that does not resolve or read exits 2 naming why; a malformed line exits 2 naming it, in
  `seen_red.py` and in `ratchet (populated)` alike.
- observability — one line per owed gate, with its record path; one `admitted` line per admitted
  population, with its record.
- risks — a gate whose script changed but whose argv did not is owed only through a `New arm:` line,
  so a pass that rewrites a gate script and declares no arm is not caught (§8 F3). An admission trusts
  any seen-red line naming the leg, in any build and at any red SHA: it shows the leg has been seen
  red, never that this population's emptiness is right.
- testing — AC1 to AC8 by fixture and probe; the arms in §7.
- migration — none, per §4.
- user docs — none owed: no page under `help/` names the ledger, the seen-red line or
  `ratchet (populated)` (`git grep -n -i 'acceptance ledger\|seen-red\|ratchet (populated)' -- help`
  finds none at `174f9d9e5`); `memory/HYGIENE.md` is the ledger's page.

## 6. Acceptance criteria

- **AC1** — When `python seen_red.py --fixture --plant seen` runs in `tools/memory-tree/`, it exits 0
  and prints `seen-red: <leg> · <red sha8> · <record path>` for the planted leg.
  Red when: the reader does not parse S1's line, so the planted record reads `NO RECORD`.
- **AC2** — When `python seen_red.py --fixture --plant unseen-gate` runs, it exits 1 and prints the
  planted leg with `NO RECORD`, the clause's planted gate with no recorded red.
  Red when: the owed set misses an added manifest row, so the plant exits 0.
- **AC3** — When `python seen_red.py --fixture --plant unseen-arm` runs, it exits 1 naming the leg
  whose `argv` carries the `New arm:` line's suite path.
  Red when: `New arm:` lines are not read, so a moved arm owes nothing.
- **AC4** — When `python seen_red.py --fixture --plant empty` runs, it exits 0 and prints the
  `adds or changes no gate` line.
  Red when: an empty owed set prints nothing, which reads as a green join.
- **AC5** — When `python deviation_join.py --fixture --plant amended` runs in `tools/memory-tree/`,
  its output is byte-identical before and after S2, and the hygiene engine's check 23 over a fixture
  ledger whose `AC1` answer is followed by a seen-red line reports the answer's tokens without the
  seen-red line's.
  Red when: the extraction drops a ledger line, or check 23 joins the seen-red line's tokens to `AC1`.
- **AC6** — When `python seen_red.py --fixture --plant bad-line` runs, it exits 2 naming the record and
  the line.
  Red when: a malformed line is skipped, so a typo reads as a missing record or, worse, as none owed.
- **AC7** — When `grep -n 'seen-red' memory/guides/BUILD-METHOD.md memory/HYGIENE.md`,
  `grep -n 'seen-red' tools/memory-tree/kit.toml` and
  `grep -n 'command:memory-tree.seen-red' tools/loop/loop.toml` run, M8 names the line and
  `seen_red.py`, the "Acceptance ledger" section states S1's grammar, the kit descriptor holds the
  `seen-red` command row and the item names it as its actor; `wc -c memory/guides/BUILD-METHOD.md`
  prints at most 30720, the row `tools/template-size-limits.txt` holds for it.
  Red when: the grammar is stated in two places, M8 outgrows its budget, or the item still names
  `command:test.seen-red`.
- **AC8** — When `python ratchet.py --fixture --plant populated-seen-red` runs in
  `tools/memory-tree/`, it exits 0, its PASS lines showing the fixture's empty armed population read
  `admitted` with exit 0 while a journal record's seen-red line names the registration's leg, `empty`
  with exit 1 once that line is removed, and exit 2 naming the record once the line loses its red SHA.
  Red when: the leg admits no population a seen-red line names, or admits one no line names.

## 7. Gates

`memory-hygiene self-test` · `branch-guard self-test` · `policy fixtures` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `build-method size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `ratchet selftest` · `ratchet (populated)` · `loop definition` · `loop command conformance` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant of §4 run through `seen_red.py --fixture`, staged red by deleting the owed-set half (a) and by dropping the seen-red flush from check 23's awk · none
New arm: tools/memory-tree/ratchet.py · covers AC8 · the plant `populated-seen-red`, staged red by `run_populated` skipping its seen-red read · none

## 8. Open questions

- **F1 — Where does `test.seen-red` run?** Options: (a) a command, `seen_red.py --build <slug>`, the
  item's actor and the close's read-back; (b) a hygiene check beside check 23; (c) a bar leg. (b) and
  (c) run over the whole corpus on every push with no build base, so either reds every landed build
  whose ledger predates the grammar. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the item's
  own shape in flow-steps' `test.seen-red` row ("command", reads and writes none). widens: none ·
  relaxes: none
- **F2 — Is the record kind a typed record file now?** Options: (a) the ledger line is the record, its
  grammar and reader in one module, and dScopedBuild's writer emits the same fields; (b) a `seen-red`
  kind in `tools/memory-tree/build_records.py` beside the ledger line, the reader reading both; (c) a
  typed file only. (c) departs from the clause's "recording both in the unit's acceptance ledger"; (b)
  writes one record's grammar twice before a second writer exists. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, the clause names the ledger as the record until dScopedBuild lands its
  writer. widens: none · relaxes: none
- **F3 — What makes a gate "changed"?** Options: (a) a manifest row whose `argv` moved, or a `New arm:`
  line on it; (b) any row field moved, the ceiling included; (c) (a) plus any file the leg's argv names
  changed in the range. (b) owes a red for a ceiling re-derivation that changes no verdict; (c) owes one
  for every edit to a shared script such as `run-gates.sh`, which most units touch. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the set the build method already owes arms for (M8 reads the
  `New arm:` lines); the departure from the clause's "one per gate a build adds or changes" is
  `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md`. widens: none · relaxes: none
- **F4 — Which hash does the `**Carries:**` line pin?** Deviation `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71` amends
  cl-dClosedLoop-0345's text, so the as-built view hashes it `72933671` where the baseline hashed `3265ae12`.
  RESOLVED (agent, 2026-10-25, delegated): rung 1, the line pins `cl-dClosedLoop-0345@72933671`, the view's hash,
  moved by deviation 71. widens: none · relaxes: none
- **F5 — How does `seen_red.py` read the `base:` fact S5 defaults to?** The fact grammar is the
  unattended driver's, and two kits re-read it: `tools/branch-reconcile/branch_reconcile.py#read_run_fact`
  and, landed past this spec's base, `tools/policy/guard.py#read_run_fact`, whose docstring calls it
  "re-read rather than imported". The memory-tree kit requires neither kit (its `kit.toml` holds
  `requires = []`). Options: (a) `seen_red.py` re-reads the one line inline, the first opening `base:`
  under `## Run facts`; (b) one shared block under `tools/lib/`, carried inline by all three kits under
  a parity row; (c) no default, `--base` required. (b) is a second mechanism moving two other kits'
  shipped files, its own unit by M2; (c) drops the default S5 states. RESOLVED (agent, 2026-11-20,
  delegated): (a), the most feature-rich survivor, every criterion met and no other kit moved; per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief. widens: none · relaxes: none
- **F6 — How does M8's sentence grow when its budget has 3 bytes left (S9, DERIVED)?** Options: (a)
  the paragraph's own words re-written so it grows by at most that; (b) other method prose trimmed to
  pay; (c) a budget raise. (c) is the owner's, since the build method's M3 keeps M1's own budget out of
  the delegation; (b) edits carrier text the `may:` grant, PLAY-dClosedLoop-3 for what cl-0345 names,
  does not reach; (a) meets AC7, a draft measured 4 bytes under today's paragraph (PINNED
  2026-11-20). RESOLVED (agent, 2026-11-20, delegated): (a), the one survivor; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief. widens: none · relaxes: none
- **F7 — Does this unit admit the empty armed population `ratchet (populated)` reds?**
  TOOL-dWitnessedBar-14, CLOSED, left the admission to this reader: its §3 names "the admission of an
  empty population it names" this unit's, `run_populated`'s docstring says no seen-red reader is
  landed, and the kit README's pack table says no seen-red record admits one yet. rev-4 scoped no
  admission, so a population drained to no row would red that leg with no way out. Options: (a) S10,
  the leg admitting a population whose registration's `leg` a seen-red line names; (b) the ratchet
  text re-worded, nothing admitted; (c) nothing, the text going false at this landing. (c) leaves
  sentences this landing falsifies; (b) leaves every drained population red; (a) meets every
  criterion with AC8 added and changes no interface I16 states. RESOLVED (agent, 2026-11-20,
  delegated): (a), the most feature-rich survivor, an M2 AMEND act on this build's own scope; per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 7, the brief's shared interfaces I2 and
  I16 and owned-node table, scout A's row for cl-0345 and flow-steps' `test.seen-red` row, at base
  `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; the `**Carries:**` line re-pinned to `72933671`, deviation 71's amended text, with §8 F4; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains the legs `branch-guard self-test`, whose guard §4's
  `tools/memory-tree/check-memory-hygiene.sh` trips; and `policy fixtures`, whose guard §4's
  `tools/memory-tree/deviation_join.py` trips, as the spec-token checker's guards join named them at
  `c6df3e901`, by the brief `2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief`; §4 is
  unchanged, as the unit writes each path; nothing else moved.
- rev-5 · 2026-11-20 · §1 · S1 S2 S3 S4 S5 S7 S8 S9 S10 · §3 · §4 · §5 · AC7 AC8 · §7 · §8 F5 F6 F7 ·
  §10 · re-grounded on the tree at `a4fd535ed`, every unit through order 22 landed, by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-7-reground-brief`: line citations become `path#symbol` or
  blob-pinned; `iter_evidence_lines` becomes `read_evidence_lines`, the lexicon declaring no `iter`;
  the owed set reads the manifest through the kit's `resolve_leg_manifest`, `read_blobs_at` and
  `resolve_prefix_token`; the `base:` fact re-read inline (F5); S7's re-point made definite over the
  landed row and factory, AC7 gaining its `loop.toml` grep; S9 held to the bytes its budget leaves
  (F6); S10 and AC8 admit the empty armed population TOOL-dWitnessedBar-14 left to this reader (F7),
  with its arm; Files touched gains `ratchet.py`, the kit README and `symbols.json`, and the leg line
  `verdict epoch (kit version dates the engine)`, `ratchet selftest`, `ratchet (populated)`,
  `loop definition`, `loop command conformance` and `codebase-map coverage + freshness`; the version
  bump is the lander's.
- rev-6 · 2026-11-20 · S7 S9 · §4 · §5 · §10 · re-grounded on the tree at `174f9d9e5`, every unit
  through order 24 landed, by the brief `2026-11-19-prompt-TOOL-dWitnessedBar-7-reground3-brief`:
  every cited path, symbol, section and blob re-read and unchanged, every PINNED fact re-derived at
  the same value and its stamp moved to HEAD; Files touched's shared-paths sentence names
  `symbols.json` with TOOL-dWitnessedBar-30 and the landed shape of TOOL-dWitnessedBar-1's edits;
  §10 names `read_flake_body` found and not taken and bounds the `Evidences` grep to the kit tree;
  nothing else moved.

## 10. Reuse audit

The seams extended: the `**Evidences:**` block walk inline in
`tools/memory-tree/deviation_join.py#read_population`, extracted into `tree_lib.py` at its second
Python instance; check 23's `alledger` awk
(`tools/memory-tree/check-memory-hygiene.sh@2c5ed1a3a960:3618-3656`); M8's arm-observation paragraph
of `memory/guides/BUILD-METHOD.md`; `tools/memory-tree/ratchet.py#run_populated`; and the command
kind's factory, `core.py new command`. The seams called, each in the memory-tree kit:
`tools/memory-tree/routed_commits.py#resolve_leg_manifest`, `tools/memory-tree/tree_lib.py#read_blobs_at`
("THE one `<rev>:<path>` bytes reader"), `tools/memory-tree/coverage_join.py#resolve_prefix_token`,
`tools/memory-tree/legacy_ledger.py#derive_seed_prefix`, `tools/memory-tree/tree_lib.py#record_paths`
and `tools/memory-tree/tree_lib.py#read_bindings`. Found and not taken:
`tools/check-spec-tokens.py#read_arm_lines`, a `New arm:` walk gov alone runs, `[[exempt]]` from
shipping in `tools/govkit/registry.toml`, its inline carry TOOL-dWitnessedBar-51 S20's; the two
`read_run_fact` copies of §8 F5, in kits this one does not require; the `acceptance` record kind,
`tools/memory-tree/build_records.py#read_acceptance`, whose record holds `run ·` lines of re-run
commands; and `tools/memory-tree/build_records.py#read_flake_body`, landed by TOOL-dWitnessedBar-1,
which reads a flake record's TAB rows and no ledger line. `python tools/codebase-map/reuse_lookup.py
"read the acceptance ledger lines that record a gate seen red"`, re-run at `174f9d9e5`, ranks generic
`read` stems, `read_blobs_at` among them, and no reader of a seen-red observation; the walk in
`deviation_join.py` was found by `git grep -n Evidences -- '*.py'`, which finds no other walk under
`tools/`, its other hits being build records' one-off scripts under `memory/builds/dClosedLoop/`
and `memory/builds/dTracedLedger/`, no kit's code.

Recall terms used: `python tools/memory-recall/query.py "how is a gate's staged red observation recorded in the acceptance ledger and read back" --terms "seen-red record acceptance ledger staged break arm red green New arm observe Evidences journal"`
