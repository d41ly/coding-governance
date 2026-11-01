**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16

# Fix brief — dMindYourWords, the spec stage's mechanical reds

The six writers authored all 17 specs under `memory/builds/dMindYourWords/spec/`, staged and NOT committed. The main
loop ran the checks the spec brief names over them, and every red below is a finding in exactly one spec. Fix each in
place, in the spec it names, and nothing else: no design change, no new scope, no edit to a spec this list does not
name. The specs have never been committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit.

## Hygiene check 25 — a retirement with no `**Readers:**` clause

Each §2 item below retires a named thing and carries no `**Readers:**` clause. Write one per item: `by name:` and every
reader that spells the name, then `by value:` and every reader of its value, or `NO VALUE READERS` and a reason; find
each reader with `git grep` over the tree, never from a record.

- TOOL-dMindYourWords-1: S2, S4, S9.
- TOOL-dMindYourWords-14: S5.
- TOOL-dMindYourWords-8: S4.

## Hygiene check 13 — a foreign id read as defined here

- TOOL-dMindYourWords-5, §3 Non-goals: a bullet opens with `TOOL-dScaffoldedMirror-4's S4`, and an id leading an item
  is read as defining it, so check 13 reports the id claimed by two build folders. Reword the bullet so the id is
  cited inside prose and does not lead.

## `tools/check-spec-tokens.py` — 23 hits on these specs

Paths a check reads as citations of tracked files:

- TOOL-dMindYourWords-9, -10, -16: `help/lexicon.md` is not tracked. The page this build creates or updates under
  `help/` is a file the build run writes: keep its full path in §2, §4 and Files touched, and cite it by basename in
  any section the check reads as a citation, as the spec brief's paths rule says. Use one spelling of the page across
  the three specs.
- TOOL-dMindYourWords-15: `memory/builds/x/build/2026-01-01-build-T-1-probe.py`, `tools/demo/fixtures/case/plant.py`,
  `memory/builds/x/a.weird`, `Memory/Builds/a/b.py`, `memory/project/lexicon-debt.txt`; TOOL-dMindYourWords-16:
  `memory/builds/r/x.py`; TOOL-dMindYourWords-8: `packs/delta.toml`, `../delta.toml`. Planted fixture paths and a
  file a sibling unit creates are not tracked. Spell a planted path so the check does not read it as a repository
  citation (name it as the fixture's relative path inside the planted tree, or describe it), and cite the ledger file
  unit 1 creates by its basename.
- TOOL-dMindYourWords-14: `README.md:650` reads as the root README, which has 119 lines; the line meant is
  `tools/lexicon/README.md:650`. Spell it whole.

A bar or suite as an acceptance observation:

- TOOL-dMindYourWords-11: an acceptance criterion names `tools/drift-audit/selftest.py`. Observe the checker on its
  staged break or a fixture of the unit's own code instead, and put the suite arm on a `New arm:` line in §7.

Legs a §4 files-touched path trips and the §7 leg line omits (`python tools/check-spec-tokens.py --list` prints them):

- TOOL-dMindYourWords-11: `kit/dogfood doc parity` (from `memory/HYGIENE.md`), `govkit selftest` and
  `govkit refusal join` (from `tools/govkit/govkit.py`). Add them to §7's leg line, or drop the path from
  files-touched if the unit does not write it; a rendered file is never the edit, so say which source the unit edits.
- TOOL-dMindYourWords-14: `policy fixtures` (from `tools/lexicon/kit.toml`).

Hand-off tokens a sibling never names (the producer's bullet hands a token the consumer's spec does not spell):

- TOOL-dMindYourWords-11 → TOOL-dMindYourWords-10: `RECORD_TAGS`, `--check-record`.
- TOOL-dMindYourWords-12 → TOOL-dMindYourWords-4: `context=True`.
- TOOL-dMindYourWords-2 → TOOL-dMindYourWords-4: `resolve_forced_source`, `build_class_index`.
- TOOL-dMindYourWords-7 → TOOL-dMindYourWords-6: `--suggest --base`.

For each, name the token in the consumer's spec where it reads it, when it does read it; otherwise correct the
producer's bullet. Keep every edge reciprocal (hygiene check 12).

## How to verify

Stage your edits under `memory/builds/dMindYourWords/` (`git add`, never commit), then run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25`, the one gate your role admits, and repeat until
it prints no finding on a dMindYourWords spec. The main loop re-runs `check-spec-tokens.py` after you return; its
hits above are stated whole, so fix them by reading. The packet's byte-compare red is the main loop's, not yours. Return each finding above with what you changed, and any you could not fix with the reason.
