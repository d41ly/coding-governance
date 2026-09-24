# TOOL-aRepatriatedFork-19 — check-wiring judges every arm at a relocated layout

**Status:** CLOSED · rev-3 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-DEPL-aRepatriatedFork-1-runlog-0e284ca8.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-1-runlog-0e284ca8.md) | journal | DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-21 |
| [2026-09-24-build-TOOL-aRepatriatedFork-19-1-acceptance-ledger.md](../build/2026-09-24-build-TOOL-aRepatriatedFork-19-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-19-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-19-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-wiring.sh` finds each kit file it judges by probing `${KIT_REL}/<kit>/<file>`, which
assumes gov's own `<prefix>/<kit>/` layout. At inCMS three arms therefore print `skip … not adopted`
over kits that are installed and wired, and at nc the merge arm does the same. Both adopters' receipts
already record where every gov file landed. This unit makes the checker ask the receipt first, adds the
harness scripts to the eol arm's population, and makes the checker's own suite runnable at a foreign
prefix, so inCMS can drop its check-wiring fork and nc can drop carve-out 27.

## 2. Scope (IN)

- **S1** — A `resolve_receipt_path <kit-home> <file>` function in `tools/check-wiring.sh`, taking the same
  pair as the Python `resolve_kit_dir`. It prints the `path` of the `.governance/install.json` row
  whose `source` ENDS in `<kit-home>/<file>` as whole path segments (a tool-root file such as
  `settings-merge.py` passes an empty home), skips a row whose `path` is
  absolute or climbs with `..`, and prints nothing when the receipt is absent (gov's own tree) or
  holds no such row. The argument is the source's trailing segments rather than the whole gov source
  because a whole source spells gov's tool root, a literal the install-prefix ban refuses in a
  shipped file, and because the last two segments are the Python resolver's own join key. It is the FIRST candidate in the
  `first_of` lists of the merge arm (`tools/check-wiring.sh:721`), the recall arm (`:505`), the
  scratch arm (`:455`), the card arm (`:560`), the agent-cap arm (`:391`) and the settings-merge
  default (`:365-366`). Every existing rung stays after it, so gov's tree and a copy-installed
  adopter with no receipt resolve exactly as today. Observed by AC1, AC2 and AC3.
- **S2** — A skip that the receipt contradicts says so. When `resolve_receipt_path` names a row and the
  file at that path is absent, the arm's `skip` line names the receipt row and the missing path
  instead of "not adopted". It stays a `skip`, because the subject of a missing installed file is
  the receipt leg, not wiring. Observed by AC4.
- **S3** — The eol arm's population (`tools/check-wiring.sh:633-636`) gains tracked
  `.claude/workflows/*.js` carrying an `eol=lf` pin, as a second NAMED glob beside
  `.claude/skills/**.md`. The arm's own comment (`:620-627`) forbids widening to "every eol=lf path
  under .claude/" and this does not. It is inCMS delta D9 (`scripts/check-wiring.sh:377-389`), taken
  as written: `tools/workflows/kit.toml:125-127` already pins these files because "350 CR bytes made
  the shipped harness unlaunchable", and until now nothing on the wiring side looked at them.
  Observed by AC5.
- **S4** — `tools/check-wiring.test.sh` runs at an adopter's prefix. Its default
  `KIT_REL="${KIT_REL:-tools}"` (`:4`) becomes the derived value from the canonical block
  `TOOL-aRepatriatedFork-18` ships. The three `cp "$SMERGE" tools/settings-merge.py` fixture lines
  (`:110`, `:187`, `:267`) spell `$KIT_REL/`. The three sites sourcing
  `$REPO/tools/lib/resolve-python.sh` (`:242`, `:263`, `:328`) use the inline `resolve_python` block
  that `skills/session-kickoff/manifest-check.test.sh:353-356` already carries, which
  `tools/lib/resolve-python.test.sh` gates byte-for-byte. `src_of` (`:30`) gains the derived
  `$REPO/$KIT_REL/` rung between its two literal rungs, which is nc carve-out 27's rung with the
  derivation swapped for the boundary walk. Observed by AC6.
  As found at build time (rev-3): `TOOL-aRepatriatedFork-8` S6 already rewrote `src_of` to
  `"$HERE/$1" "$REPO/$1"`, and `$HERE` IS `$REPO/$KIT_REL` in the S4 sense, so that rung is absorbed
  with no change here; the same unit folded the three resolver sources into one guarded source,
  which this unit replaces with the one inline block.
- **S5** — New arms in `tools/check-wiring.test.sh` for S1, S2 and S3, each observed red against the
  a7c78ad2 checker before it lands, plus one arm asserting that `resolve_receipt_path` and the Python
  resolver `TOOL-aRepatriatedFork-2` ships give the same answer over one fixture receipt, so a change
  to govkit's receipt format reds instead of silently missing. Observed by AC1 through AC5.
- **S6** — `KIT_CHECK_WIRING_VERSION` moves one step, from `1.7` to `1.8` (`tools/check-wiring.sh:23`).
  `TOOL-dPolishedVitrine-2` in `memory/backlog/TOOL.md` closes with the measurement that already
  answers it: `SMERGE_DEFAULT` has been derived from `KIT_REL` since `TOOL-dRetiredFork-8`
  (`:365-366`), and gov's checker printed `Fix: python3 scripts/settings-merge.py` at inCMS on
  2026-09-23. Observed by AC7.
  The backlog row is flipped by the main loop's records commit, not by the unit pass: `--dispatch`
  refuses a unit write set naming `memory/backlog/TOOL.md` (unattended check 49, a shared mutable
  record), so AC7's backlog half is observed at the close (rev-3).

## 3. Non-goals (OUT)

- The card arm's verdict. At inCMS it reports `UNWIRED card` twice because
  `scripts/orientation-card.fragment.json` and `scripts/orientation-replay.fragment.json` are
  installed beside `scripts/manifest-check.sh` and are not in `.claude/settings.json`. That is TRUE:
  the kickoff-manifest entry (`tools/govkit/entries/kickoff-manifest.kit.toml`) installs both
  fragments and declares no step that wires them. The checker is right; the missing step is the
  deployer's, and `TOOL-aRepatriatedFork-11` S3 builds it for every landed fragment.
- The settings.json walk-up (inCMS patch 2, `scripts/check-wiring.sh:103-112`) and D10. inCMS has
  tracked `.claude/settings.json` in-repo since ba4999965, so gov's `$ROOT/.claude/settings.json`
  rung resolves it (audit-B §4), and gov's `check_settings_scope` (`tools/check-wiring.sh:108`)
  already reports scope. Nothing is upstreamed; the adopter drops both.
- The remedy interpreter (inCMS patch 6). gov prints `python3` when `lib/resolve-python.sh` is not
  beside the checker (`tools/check-wiring.sh:240-245`). It is a printed remedy and runs nothing.
- The recall fragment's `{kit}/memory-recall/` hook token. With S1 the recall arm FINDS
  `scripts/recall/recall-opened.fragment.json` at inCMS; what the fragment's `hook_path` expands to is
  inCMS's `KIT_MEMORY_RECALL_DELTA` and the brief's `TOOL-aRepatriatedFork-2`. inCMS keeps that one
  divergence row until then, and nothing here rests on it.
- `tools/push-main.test.sh`, which has the same `tools/lib/resolve-python.sh` defect (audit-B §3).
  It is the lander's suite; see §8 F3.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-2` — the rung order of that unit's `resolve_kit_dir`:
  receipt, then probes, then a named miss. `resolve_receipt_path` is its rung 1 spelled for shell, so both
  answer "where did this gov file land" from the same row by the same join key.
- **consumes-from** `TOOL-aRepatriatedFork-18` — the canonical derived-`KIT_REL` block S4 inlines.
  Without it this suite would carry a fourth hand-copied boundary walk.
- **hands-off** `TOOL-aRepatriatedFork-12` — inCMS's recall pull needs gov's `check-wiring.sh` in the
  same landing, because inCMS patch 5 seds `FAMILIES` out of the `extract.py` that unit replaces.
- **hands-off** `TOOL-aRepatriatedFork-11` — a hook fragment `govkit apply` or `update` lands arrives
  wired, which that unit's S3 builds. The two card fragments are the measured instance.

## 4. Design

### Data model

The receipt is written by `govkit` with `json.dumps(receipt, indent=2)` (`tools/govkit/govkit.py:9431`,
`:9469`, `:9476`), so each row is one flat object whose keys sit one per line, `path` first:

```
      "path": "scripts/merge-rows.py",
      ...
      "source": "tools/memory-tree/merge-rows.py",
```

`resolve_receipt_path` is one awk pass that collects each row's `"path"` and `"source"` between its
`{` and `}` lines, so key order does not matter, and prints the path of the first row whose source
ends in `<kit-home>/<file>` (rev-3). The checker's comment at `:240-245` records that it executes no
python, and that stays true. The join key is the source's last two segments, the part of the GOV
source path that is identical at every adopter and the part `resolve_kit_dir` joins on; the head is
gov's tool root, which a shipped file may not spell.

What each adopter's receipt answers, read on 2026-09-23 (PINNED):

| Gov source | inCMS installed at | nc installed at | gov rung finds it at inCMS | at nc |
|---|---|---|---|---|
| `tools/memory-tree/merge-rows.py` | `scripts/merge-rows.py` | `scripts/merge-rows.py` | no | no |
| `tools/memory-recall/recall-opened.fragment.json` | `scripts/recall/recall-opened.fragment.json` | `scripts/memory-recall/…` | no | yes |
| `tools/hooks/scratch-guard.fragment.json` | `.claude/hooks/scratch-guard.fragment.json` | `scripts/hooks/…` | no | yes |
| `skills/session-kickoff/orientation-card.fragment.json` | `scripts/orientation-card.fragment.json` | `scripts/…` | yes | yes |

The measured consequence, gov a7c78ad2's checker in an inCMS clone (audit-B §4, `cw-gov.out`): `skip`
for scratch, recall and merge where inCMS's fork prints `ok`. Run read-only at nc's worktree for this
spec: `skip merge — memory-tree merge driver not adopted (no merge-rows.py)` over a repo whose receipt
installs `scripts/merge-rows.py`. nc declares no `merge=rows` path, so the honest line there is
`skip merge — no tracked path declares merge=rows`, which S1 produces.

### Adopter deletions

inCMS, once it takes gov's `check-wiring.sh` and `check-wiring.test.sh` byte-for-byte:

| Artefact | Where | Action |
|---|---|---|
| `KIT_CHECK_WIRING_DELTA` | `.governance/kits.json` divergence `scripts/check-wiring.sh`, header `scripts/check-wiring.sh:2-40` | deleted; its settings-outside-the-repo justification went stale at ba4999965 |
| `KIT_CHECK_WIRING_TEST_DELTA` | kits.json divergence `scripts/check-wiring.test.sh` | deleted |
| `version_waivers.check-wiring` | kits.json | deleted; the checker moves to 1.8 with a gov release behind it |
| `kits.check-wiring.files` | kits.json | both rows `diverged` to `engine` |
| patches 2, 3, 4, 5, 6, 8, 9, 10, D8, D9, D10, D12 | `scripts/check-wiring.sh` | gone with the fork: 3, 4, 8, 9 and 10 by S1; D9 by S3; 2 and D10 by ba4999965; 5 by gov's conf read at `tools/check-wiring.sh:784`; D8 by gov's `--only` arm; D12's remedy names a script inCMS now tracks |
| two card fragments unwired | `.claude/settings.json` | adopter wires both with `settings-merge.py --fragment` until `TOOL-aRepatriatedFork-11` does it |

nc deletes carve-out 27 (`scripts/check-wiring.test.sh:30-35`), which S4 absorbs.

### Files touched (estimate)

- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `memory/backlog/TOOL.md`

### Alternatives rejected

- **Flat-layout rungs** (`${KIT_REL}/merge-rows.py`, `${KIT_REL}/recall/…`, `.claude/hooks/…`), which
  is what inCMS patches 3, 8 and 9 are. Each rung is a guess about one adopter's layout and the
  next adopter needs another; the receipt is already the declared answer for every adopter.
- **Resolving through `govkit` or a python helper.** `tools/lib` is gov-internal and ships nothing
  (`tools/govkit/registry.toml`, its `[[exempt]]` row), and the checker runs as a SessionStart hook
  where one awk pass is the whole cost.
- **Declining the card arm at inCMS.** The fragments are installed and the hook script is present;
  declining them would make the checker agree with a state it correctly calls dormant.

## 5. Production-readiness checklist

- security — `resolve_receipt_path` reads a tracked file and prints a repo-relative path that `first_of` then
  tests with `-f`; nothing from the receipt is executed or evaluated.
- perf / scale — one awk pass over the receipt per arm that probes, six at most, inside a SessionStart
  hook that already forks more than that.
- error / empty / loading states — an absent receipt, an absent row and a row naming a missing file
  are three distinct outcomes; S2 makes the third one visible.
- observability — each `ok` line already names the resolved path, so the receipt's answer is printed.
- risks — a hand-edited receipt could steer an arm to the wrong file. The `receipt sync` leg asserts
  the receipt matches the tree, so that state is red elsewhere first.
- testing — S5's arms, each observed red against a7c78ad2's checker.
- migration — none in gov. Adopters per §4 `### Adopter deletions`.
- user docs — N/A: no user-facing surface; the checker's header comment names the new rung.

## 6. Acceptance criteria

- **AC1** — When a scratch repo holds the merge driver and its launcher at a flat `scripts/`
  prefix, a `merge=rows` path, and a receipt row mapping `tools/memory-tree/merge-rows.py` to that
  flat path, `bash tools/check-wiring.sh --check` run there prints a `merge` line that is not
  `skip … not adopted`.
  Red when: the a7c78ad2 checker runs over the same fixture and prints `skip     merge     — memory-tree merge driver not adopted`.
- **AC2** — When the fixture's receipt maps `tools/hooks/scratch-guard.fragment.json` into
  `.claude/hooks/` and settings.json wires it, the `scratch` line reads `ok`; the same fixture with
  a receipt row mapping `tools/memory-recall/recall-opened.fragment.json` under `scripts/recall/`
  gives a `recall` line that is not `not adopted`.
  Red when: either arm prints `skip` over a receipted, wired kit.
- **AC3** — When gov's own tree runs `bash tools/check-wiring.sh --check`, its output lines are
  identical to a7c78ad2's apart from any line the eol arm adds for S3.
  Red when: the receipt rung changes a verdict in a tree that has no receipt.
- **AC4** — When the fixture's receipt names the flat driver path and that file is deleted, the
  `merge` line is a `skip` naming the receipt and the missing path, from `resolve_receipt_path`'s answer.
  Red when: it prints the generic "not adopted".
- **AC5** — When a fixture tracks one script under `.claude/workflows/` with an `eol=lf` pin and the
  worktree copy holds CR bytes, `bash tools/check-wiring.sh --check` prints an `eol` line naming
  that script.
  Red when: the a7c78ad2 checker prints `ok       eol` over the same fixture.
- **AC6** — When `git grep -nE 'KIT_REL:-tools|tools/settings-merge.py|tools/lib/resolve-python.sh' -- tools/check-wiring.test.sh`
  runs, it prints only lines the suite marks as deliberately foreign-prefix fixtures, and
  `grep -c '^# >>> resolve_python' tools/check-wiring.test.sh` prints `1`, which
  puts the suite in the inline-parity leg's scanned population.
  Red when: a gov-prefix default or a `tools/lib/` source survives.
- **AC7** — When `bash tools/check-kit-versions.sh` runs it exits 0 with
  `KIT_CHECK_WIRING_VERSION=1.8`, and `grep -n 'TOOL-dPolishedVitrine-2 · CLOSED' memory/backlog/TOOL.md`
  prints one line.
  Red when: the checker's bytes moved and its version did not.
- **AC8** — When gov's `check-wiring.sh` replaces inCMS's in a shared clone of inCMS whose
  `.claude/settings.json` has both card fragments merged, the clone's `check-wiring.sh --check`
  prints `ok` for scratch, recall, card and merge and exits 0.
  Red when: any of the four is `skip` or `UNWIRED`, which is audit-B §4's measured state.
  permission: inCMS is another repository; observed in a `git clone --shared` scratch clone, editing
  nothing in inCMS.
  fixture: the clone needs `merge.rows.driver` configured, which is per-node git config inCMS's
  charter already requires.

## 7. Gates

`check-wiring self-test` · `kit version markers` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: `tools/check-wiring.test.sh` · fixtures with a receipt row per arm, a receipted-but-missing
driver, a CR-carrying pinned workflow script, and a receipt the awk and Python readers must agree
on, each run against the a7c78ad2 checker first · none

## 8. Open questions

- **F1 — should an arm whose receipted file is missing report `UNWIRED` rather than `skip`?**
  Option (a): `skip` naming the receipt row, as S2 specifies. Option (b): `UNWIRED`, which gates
  `WIRING_CHECK` in `.unattended.conf`. Recommendation: (a). A missing installed file is the receipt
  leg's red; making the wiring checker gate on it would red one defect in two places, and the
  unattended preflight would stop on something `receipt sync` already stops.
  RESOLVED (owner, 2026-09-23): (a), `skip` naming the receipt row, as recommended.
- **F2 — does a shell consumer read the receipt at all?** `TOOL-aRepatriatedFork-2` §8 F1
  recommends that shell consumers use the probe rungs only and print a named miss, because parsing
  the pretty-printed receipt in bash is brittle. check-wiring is the shell consumer where the probe
  rungs cannot answer: at inCMS the three kits it misses sit in renamed or foreign directories that
  no probe spells, and a named miss is today's false `skip` with better wording. Option (a): the awk
  rung, as S1 specifies, with an arm comparing its answer against the Python resolver over the same
  fixture receipt, so a format change in govkit's writer reds rather than silently misses. Option
  (b): shell out to the adopter's resolved Python for rung 1 only. Recommendation: (a). The writer's
  format is fixed by `json.dumps(indent=2)` at three sites, the parity arm makes brittleness a red,
  and the checker runs as a SessionStart hook with no resolved interpreter of its own
  (`tools/check-wiring.sh:240-245`). The two recommendations need one answer before either unit
  builds.
  RESOLVED (owner, 2026-09-23): (a) for this checker: the awk rung plus the parity arm. Shell
  consumers that already resolve a Python import the canonical reader instead, per
  `TOOL-aRepatriatedFork-2` §8 F1, so the two answers are one.
- **F3 — who owns `tools/push-main.test.sh`'s identical `tools/lib/resolve-python.sh` defect?** The
  brief lists it under the lander contracts unit. Recommendation: that unit, applying S4's recipe;
  this unit touches only the check-wiring suite.
  RESOLVED (owner, 2026-09-23): `TOOL-aRepatriatedFork-8`, applying S4's recipe, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from the brief's unit 19, audit-B §4 and §5 and audit-C's nc
  `check-wiring.test.sh` row, with nc's checker run read-only for this spec.
- rev-2 · 2026-09-24 · S6 and its acceptance line move to `1.7` -> `1.8`: `TOOL-aRepatriatedFork-2` and
  `TOOL-aRepatriatedFork-8` each bumped check-wiring in this build before this unit reached it.
- rev-3 · 2026-09-24 · S1 takes the kit home and file as two arguments and matches their join as a
  suffix, not the whole gov source, and is named `resolve_receipt_path` (S2's helper
  `derive_receipt_miss`) because the lexicon's VERBS table holds no `receipt`, so the shipped checker spells no tool root and joins as the Python resolver does; S4's
  `src_of` rung is recorded as already absorbed by `TOOL-aRepatriatedFork-8`; S6 and AC7's backlog
  half move to the main loop's records commit, because check 49 refuses the backlog in a unit write set.

## 10. Reuse audit

The seam is `first_of` in `tools/check-wiring.sh:185`: every arm already resolves its kit file
through it, so S1 adds one candidate at the head of existing lists rather than a new resolution
path. `reuse_lookup.py` surfaced `kit_rel` (fan-in 6) and `resolve` as neighbours; neither reads the
receipt, and no existing shell function in gov does, which is the evidence that no seam for "where did
this gov file land" exists yet. The recall probe surfaced `TOOL-dPolishedVitrine-2`, which S6 closes,
and `TOOL-dRetiredFork-39`, whose `KIT_REL`-set-by-nothing finding S4 inherits through
`TOOL-aRepatriatedFork-18`.

Recall terms used: `check-wiring`, `KIT_REL`, `first_of`, `skip`, `adopted`, `merge-rows`,
`recall-opened`, `scratch-guard`, `fragment`, `receipt`, `install.json`, `prefix`.
