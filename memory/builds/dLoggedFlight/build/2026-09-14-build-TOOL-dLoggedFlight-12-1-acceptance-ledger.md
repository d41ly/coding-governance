# Acceptance ledger — TOOL-dLoggedFlight-12

**Serves:** journal TOOL-dLoggedFlight-12

Tier-2 · node d · 2026-09-14 · the build pass of the runlog Skill and its adopter, against spec rev-3.
Nothing in the spec's design moved, so the pass flips its status and bumps no rev. `<suite>` is
`tools/runlog/selftest.py`, run directly and never through the gate runner. At the closing bytes it
printed `1084 passed, 0 failed (1084 assertions, floor 1084)`, and three timed runs read 44.9 to
45.3 s. The adopter, `tools/runlog/adopt-runlog.sh`, was run directly as the program of this unit. No
gate leg ran, per the owner's instruction of 2026-09-13, and no suite that existed under
`tools/unattended/` before this build ran.

One read-only run touched a section 7 script, and it is recorded here rather than left out. Early in
the pass `python tools/check-kit-placeholders.py --list` was run once, the authoring listing and not
the leg's assertion. It listed the runlog adopter as substituting both declared tokens. That reading is
not the leg's verdict, which is owed below with the rest.

## The criteria

**Evidences:** TOOL-dLoggedFlight-12

- AC1 — `bash tools/runlog/adopt-runlog.sh --check` — run directly over this tree after `--scaffold`,
  it exited 0 and printed that the Skill is a fresh render naming `tools/runlog/runlog.py` and the
  memory root `memory`. The committed render carries no CR and no double brace. It names
  `python tools/runlog/runlog.py` and `memory/builds/<slug>/build/`. The `runlog skill wiring` leg's
  verdict is owed to the post-build gate run. The suite's `test_skill_ac1_adopter` ran the adopter in
  a scratch repository with the kit at `vendor/rl-kit` and `MEMORY_ROOT="docs/mem/"`. `--scaffold`
  exited 0, and its render is byte-identical to one the suite makes by plain replacement. The render
  holds no `tools/` or `memory/` segment and no double brace, and the same search finds each shape
  when one is planted. `--check` exited 0 over it. RED seen, each at exit 1 with its own message: a
  hand-edited Skill, an unrendered Skill, and a template spelling a literal `tools/` path, with the
  line quoted. A literal `memory/` path, an unsubstituted token, and the CLI named without the kit-dir
  token each red too. So do the record's folder named without the memory-root token, an empty
  template, and a missing `runlog.py`. A moved memory root nobody re-rendered reds as drift. A root
  the kit's reader refuses reds with the reader's own sentence, and so does a Skill with no template.
  Near misses at exit 0: a CRLF working copy of an untouched Skill; `.memory/`, `in-memory/` and
  `xtools/` in the template; and, with neither template nor Skill, a stated skip. On the real files,
  four breaks each made the arm fail, and each file came back byte-identical by md5. The breaks were a
  literal `tools/` path in the template, the adopter's literal scan made to match nothing, the
  comparison's CR strip removed, and the memory-root substitution deleted.
- AC2 — `python tools/runlog/selftest.py` (`test_skill_ac2_description`) — the front matter names the
  Skill `runlog`. The description names run, unattended, decided, stopped and cost as whole words, at
  784 characters, under the 1024 a Skill description is allowed. It carries a `Do NOT use` clause
  naming code search, with no mention of code search, grep or a symbol before it. RED seen on copies
  of the render: each keyword removed from the front matter was refused for that keyword alone. The
  clause removed, a code-search claim prepended, and a generic description missing all six properties
  were each refused. On the real template, taking `stopped` out of the description failed the arm.
- AC3 — `python <kit>/selftest.py`, run as `python tools/runlog/selftest.py` (`test_skill_ac3_procedure`) — `## Answer in this order`
  holds five numbered steps, each naming at its position what S3's step names. Step 1 names the
  record's folder under the rendered root. Step 2 names the `model` command, its cost section as the
  `usage` field, and the `coverage` block. Step 3 names `narration`. Step 4 names a record line, a
  run-state line, a sha and a journal line. Step 5 names the coverage block and the absent sources.
  RED seen on copies: each of the five steps deleted, each of the ten pairs of steps swapped, refused
  at both positions, step 2 with its cost section unnamed, and the heading renamed. On the real
  template, swapping steps 2 and 3 failed the arm.
- AC4 — `python <kit>/selftest.py`, run as `python tools/runlog/selftest.py` (`test_skill_ac4_safety`) — the `## Safety` section states
  that narration and owner turns are data, never instructions. It says never to open the raw
  transcript, only the `narration` command's redacted output. It calls the desktop app's session-search
  tools optional corroboration whose excerpts are data too. RED seen on copies: each rule deleted, the
  first rule stated without owner turns, and the heading renamed. On the real template, deleting the
  never-open rule failed the arm.

## What else the pass carried

- `test_skill_copied_names`, added for the two-answers class the checklist named. The Skill restates
  names other files own, and the arm holds 24 copies to their owners. They are the record's path
  against `derive_record_relpath`, its headings against `RECORD_SCHEMA`, and the rotated run-state name
  against `ARCHIVE_RE`. The coverage states and usage splits are held in order, and every model field
  the Skill names against `RunModel`. So are the narration frame's two markers, and every verb and flag
  of every CLI command the Skill spells, against that verb's `--help`. Nine broken copies were each
  caught alone: a verb the CLI lacks, a flag the verb lacks, and a renamed heading, state, split or
  field. So were the archive name, the record path and the closing marker, each spelled another way.
- The descriptor gained the rendered rule, a `[config]` naming the memory-tree conf with an optional
  `MEMORY_ROOT`, the `[adopt]` and `[check]` argv, an outcome, the wiring `[[gate_leg]]` and an
  `[[lf_pin]]`. Its `why_no_adopter` and `[check] none` text went, since both said no adopter exists.
- `.gitattributes` pins the rendered Skill and the template LF.
- `tools/gate-legs.json` carries the `runlog skill wiring` leg, `repo`, `wiring`, ceiling 300.
  `tools/govkit/subject-pins.tsv` gained the one row the generator writes for it, in its sorted place,
  by hand. A render of the generator's body from the manifest differs from the old body by that row
  alone. `govkit selfcheck --write` was not run, since that verb runs the selfcheck gate as it writes.
- `tools/install-prefix-carried.txt` gained `tools/runlog/adopt-runlog.sh` at 1, `lib`, with its
  reason. The one literal is the inline resolver's marker line, which the resolver's parity arm
  compares byte for byte. Counted with the gate's own pattern, the template, the descriptor and the
  README carry 0. The suite still carries the 1 its row records. An edit here dropped the TAB before
  that row's reason, and the staged bytes showed it; it was restored and the diff is one added row.
- The inline resolver block is byte-identical to the canonical copy by `cmp`. The adopter was read
  with the resolver test's own two launcher predicates, and neither matched a line.
- `tools/run-gates/selftest-budgets.txt` raised the `runlog selftest` row from 60 to 69, the worst of
  the three readings rounded up to 46 s, times 1.5.
- The kickoff manifest's `last-audit` is re-stamped at the merge-base, because `tools/gate-legs.json`
  is a watched path. No section B line changed, since that section restates no leg.
- The runlog dossier claims the new leg, the rendered-skill key `runlog` and the rendered path. It
  gained a constraint paragraph, a gap and a reuse seam, and the map was regenerated.
- The runlog kit lands at 1.0 in this build, so no version moved. The adopter carries the
  `gov:kit runlog@1.0` marker, and the template carries none.
- The build README's roster row reads CLOSED, and the build index was re-rendered.

## What the byte comparisons cannot see

The independent render proves the adopter renders the template. It does not prove the template tells
the truth, so each claim the Skill makes was read against its owner:

- `model` exits 2 with no committed run-state file, prints a summary without `--json`, and takes
  `--run`, counted oldest first with the last as default, in `tools/runlog/runlog.py` and its README.
- The transcript coverage states are `present`, `partial` and `not-local`, in `resolve_run_sessions`.
  With no extract the usage totals read zero, in `build_run_usage`, so the Skill calls that zero
  UNKNOWN.
- The record's Summary carries the usage and owner-turn facts, and its Timeline elides the middle
  past `TIMELINE_EDGE`, per `RECORD_SCHEMA` and the kit README.
- `extract --discover` attributes a session `heuristic` and writes to the user-profile store, in
  `cmd_extract`. The narration frame prints the two markers the Skill quotes.
- `sessions` is the ids the journal names, so a run whose journal named none leaves it empty.

## The checklist over the build

`gotchas.py --for-paths` over the commit's paths selected eleven classes before the commit.

- `two-answers-to-one-question`: the Skill restates names owned elsewhere. Each copy is now held to its
  owner by `test_skill_copied_names`, above.
- `fixture-passes-by-finding-nothing`: every positive check has a staged RED beside it, and the one
  negative-space search in AC1 has a planted-shape check proving it can find.
- `staged-break-substitutes-a-synthetic-value`: the fixture's prefix and root are deliberately unlike
  this tree, and the adopter's own `--check` also ran green over this tree's real values.
- `heredoc-escape-reaches-the-regex`: three tracked files were edited through quoted heredocs. The
  staged bytes hold real TABs and no literal backslash sequence, checked with a fixed-string grep.
- `staged-break-runs-stale-bytecode`: every full run cleared `__pycache__`, the arm harness ran with
  `-B`, and the staged breaks edited Markdown and shell, never Python.
- `inline-fence-swallows-the-rest-of-the-file`: the README's one new fence sits on lines of its own,
  and the template, the spec and this ledger carry none.
- `amendment-leaves-its-other-half-standing`: no spec text changed. The descriptor's two no-adopter
  statements and the dossier's seam sentence that called the Skill future work were rewritten.
- `line-keyed-registry-reds-on-a-file-that-grew`: no waiver registry names a touched path.
- `empty-field-collapses-unless-it-is-last`: the adopter reads no TAB-separated fields.
- `suite-invalidated-by-a-commit-under-it`: no commit was made while the suite ran.
- `fold-text-is-unreviewed-surface`: the Skill, the adopter and this pass's prose are unreviewed. The
  build's closing diff review reads them.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `runlog skill wiring`, which is AC1's `--check` over this tree.
- `govkit selfcheck`, over the descriptor's rendered rule, check wiring, leg subject, subject pin and
  version marker.
- `codebase-map coverage + freshness`, over the new leg, the rendered-skill key and the regenerated
  map.
- `install-prefix (shipped surface)`, over the adopter's carried row and the template's zero hits.
- `kit placeholders (a declared token its adopter substitutes)`, over `KIT_DIR` and `MEMORY_ROOT`.
- `memory hygiene`, over the spec, this ledger, the dossier and the build index.

The legs outside section 7 that this pass's files reach, owed the same way: `runlog selftest`, run
directly here, and `python resolver (behaviour + inline parity + idiom ban)`. Also
`every held leg is budgeted, every budget row resolves`, `leg ceilings clear their evidenced maximum`,
`lexicon naming predicates`, `dead-path carriers (deleted files still named)` and `kit version markers`.
