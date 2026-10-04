# KICK-aMendedFleet-3 — kickoff Step 4 points at the two context commands the build method spells once

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams kickoff+tooling · ratified 2026-10-04 · order 78

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The kickoff engine's Step 4 spells the bug-class command itself, in a 606-byte paragraph that also
explains how to locate the memory-tree kit, and it never asks for the open asks that target the
same entrypoints. The engine measures 18407 of its 18432-byte ceiling, PINNED 2026-10-04 with
`bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`, so nothing new fits in it.
This unit makes the build method the one place the two context commands for a path set are
spelled, the bug-class checklist and the path-filtered asks, and collapses Step 4's paragraph into
a pointer at them. The engine shrinks, and a kickoff reports the asks on its card beside the
classes.

## 2. Scope (IN)

- **S1** — The build method's M5 gains one short paragraph and one fenced block spelling the two
  context commands for a path set: `gotchas.py --for-paths <paths>` and
  `gen_build_index.py --asks --path <paths>`, both under the memory-tree kit dir. The edit is made in
  `tools/memory-tree/BUILD-METHOD.template.md` with the `{{KIT_DIR}}` token M6 already uses, and
  reaches `memory/guides/BUILD-METHOD.md` through the kit's own render, never by hand. Observed by
  AC1, AC4 and AC5.
- **S2** — Step 4's paragraph headed "The bug classes this area can hit" in
  `skills/session-kickoff/SKILL.md`, its fenced command and its trailing two sentences, is replaced
  by one paragraph that names `<MEMORY_ROOT>/guides/BUILD-METHOD.md` and its M5, says to run those
  two commands over the pointer-map row's entrypoints when the project ships the method, and says
  where each lands on the READY card: the class names on `## classes`, the ask ids on `## records`.
  The pointer spells neither command. Observed by AC2 and AC3.
  **Readers:** by name: `skills/session-kickoff/SKILL.md` alone spells the paragraph and the
  `<MEMORY_TREE_KIT>` placeholder it defines. by value: NO VALUE READERS — agents read the step,
  and no checker parses its text.
- **S3** — The build method's byte high-water in `tools/template-size-highwater.txt` is re-recorded
  with `--bump` after the render, because S1's growth is intended. Observed by AC4.
- **S4** — The `skills/session-kickoff/SKILL.md` row of `memory/project/method-carriers.txt` says
  that Step 4 points at M5's context commands, beside Step 5b's hand-back it names today. The
  registry keys on path alone, so this is accuracy, not a gate fix. Observed by AC6.
- **S5** — The kickoff manifest's `last-audit` line is re-stamped in the landing commit with a delta
  line, because `memory/guides/SESSION-KICKOFF.md` watches both `skills/session-kickoff/SKILL.md` and
  `memory/guides/BUILD-METHOD.md`. Its body does not change, so `last-body-change` stays. Observed by
  AC7.

## 3. Non-goals (OUT)

- Building `--path`, its ranking or its cap. That is `TOOL-aMendedFleet-10`.
- Step 4's map-dossier paragraph and its memory-recall paragraph. Recall stays keyed by a question,
  not by a path set, and the recall kit ships without the memory-tree kit in some adopters, so its
  paragraph keeps its own kit resolution.
- The workflow prompts that also read a path set's asks. Unit 11 repoints the review harness; the
  build harness prompts are not named by the brief.
- Adding the asks command to the kickoff manifest's own gate-command block. The manifest measures
  25564 of the 25600 bytes check C7 allows, PINNED 2026-10-04, and the method is the commands' home.
- Changing Step 5's card grammar. Ask ids ride the existing `## records` section, which the card
  writer does not parse by name.
- The kit version bumps for the kickoff-manifest and memory-tree kits. Several units of this build
  move both kits, so each bump is owed once, at the close, after the last move.

### Edges

- **consumes-from** `TOOL-aMendedFleet-10` — the `--path` option of `gen_build_index.py --asks`;
  without it the second command the method spells exits 2 as an unknown option.
- **hands-off** external — the kickoff-manifest and memory-tree kit version bumps, owed once by
  this build's close.

## 4. Design

### Evidence

Read at base `7af5f564`. The two engine files, the method's template and render, the size limits
and the high-water record are byte-identical at the worktree tip `efc4b0c9`.

- `skills/session-kickoff/SKILL.md` lines 178-188 hold the paragraph S2 replaces, 606 bytes measured
  with `awk` over that range. Line 234 is Step 5b's existing pointer at the method, spelled
  `<MEMORY_ROOT>/guides/BUILD-METHOD.md`, which is the spelling S2 reuses.
- `tools/template-size-limits.txt` declares the engine at 18432 and the method render at 30720.
  `tools/template-size-highwater.txt` records the engine at 18369 and the method at 27946. The
  engine already sits 38 bytes past its high-water, an advisory WARN, so S2's net shrink also
  clears that WARN.
- `memory/guides/BUILD-METHOD.md` measures 27946 bytes and 346 lines against M1's 30720-byte and
  400-line budget. M5 spells the two set-wide probes; M6 spells `gotchas.py --for-diff HEAD~1..HEAD`
  as an act after each commit. Neither section spells `--for-paths` or `--asks`.
- `tools/memory-tree/kit.toml` declares the method `rendered` from its template;
  `bash tools/memory-tree/adopt-memory-tree.sh --render` rewrites the four rendered guides and
  nothing else. The `kit/dogfood doc parity` leg compares template and render.
- `tools/memory-tree/check-method-carriers.sh` greps every tracked file outside `memory/` for the
  method's filename and requires a registry row; the engine already has one. Its arm 5 refuses a
  carrier holding an `## M` heading, which S2 does not add.

### The two edits, as they will read

Method, M5, after the paragraph that ends "and M7 re-runs the query":

```markdown
**The context for a path set** — kickoff's entrypoints, a spec's Files touched — is two more
commands, and the kickoff engine points here rather than spelling them:

    python {{KIT_DIR}}/gotchas.py --for-paths <paths>            # the bug classes those paths can hit
    python {{KIT_DIR}}/gen_build_index.py --asks --path <paths>  # the open asks targeting them, ranked and capped
```

The block is fenced as `bash` in the file; it is indented here only to sit inside this fence.

Engine, Step 4, replacing lines 178-188:

```markdown
**The bug classes and open asks for this area** (when the project ships the build method,
`<MEMORY_ROOT>/guides/BUILD-METHOD.md`): run the two context commands its M5 spells over the
pointer-map row's entrypoints. Report the class names on `## classes` and the ask ids on `## records`.
```

The replacement is about 300 bytes against 606, so the engine lands near 18100. The method grows
by about 380 bytes to about 28330, inside its 30720 row. Both figures are ESTIMATES, re-derived by
AC3 and AC4 at build time.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `skills/session-kickoff/SKILL.md`
- `tools/template-size-highwater.txt`
- `memory/project/method-carriers.txt`
- `memory/guides/SESSION-KICKOFF.md`

### Rollout

Two prose edits, one rendered. An adopter receives the method paragraph on its next memory-tree
kit update and the engine paragraph on its next kickoff-manifest kit update. An adopter on the new
engine and an old method render reads a pointer to an M5 that does not spell the commands yet; the
pointer still names the file, and the `kit/dogfood doc parity` leg keeps gov's own pair in step.

### Alternatives rejected

- **Folding the asks into `gotchas.py` as one carrier.** The source report rejects it: it couples
  the class catalogue to the backlog fold, at about 2.6 s against 0.25 s.
- **Spelling the commands in the engine and pointing the method at it.** The engine is at its
  ceiling and is installed per machine, while the method renders per repo with the right kit path.
- **Placing the paragraph in M6.** M6 is what runs after a commit; the context for a path set is
  read before code, which is M5's moment.

## 5. Production-readiness checklist

- security — N/A — prose in two instruction documents; no new write path.
- perf / scale — two commands of about a quarter second each over a handful of entrypoints.
- error / empty / loading states — an entrypoint no ask targets prints an empty asks list, and a
  project without the method skips the step, as the paragraph's own condition says.
- observability — N/A — the commands' own output is the observation.
- risks — the asks command is dead until unit 10 lands; order 10 before 78 covers it, and AC5
  observes it.
- testing — direct greps over the four edited files, one size check each, the carriers checker and
  one run of each command.
- migration — N/A — no stored state.
- user docs — N/A — the engine and the method are the user docs.

## 6. Acceptance criteria

- **AC1** — When `grep -n -e "--for-paths" -e "--asks --path" tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md`
  runs, each file reports exactly one line per command, and every hit sits between the `## M5` and
  `## M6` headings.
  Red when: either command is missing from M5, or spelled a second time elsewhere in the method.
- **AC2** — When `grep -c -e "gotchas.py" -e "gen_build_index" -e "MEMORY_TREE_KIT" skills/session-kickoff/SKILL.md`
  runs, it prints 0, and `awk '/^## Step 4/,/^## Step 5 /' skills/session-kickoff/SKILL.md` prints a
  Step 4 that names `BUILD-METHOD.md`, `## classes` and `## records`.
  Red when: Step 4 still spells a command or the kit placeholder, or no longer names the method.
- **AC3** — When `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` runs, it exits
  0, prints a byte figure below 18407 and prints no WARN line.
  Red when: the step grew, or shrank too little to clear the 18369 high-water.
  figure: 18407 and 18369 are PINNED, measured at base 2026-10-04.
- **AC4** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs after S3's
  bump, it exits 0 under the 30720 row and prints no WARN line.
  Red when: the render exceeds its row, or its growth went unrecorded.
- **AC5** — When `bash tools/memory-tree/adopt-memory-tree.sh --render` runs and is followed by
  `git diff --exit-code -- memory/guides/BUILD-METHOD.md`, the diff prints nothing; and
  `python tools/memory-tree/gotchas.py --for-paths skills/session-kickoff/SKILL.md` and
  `python tools/memory-tree/gen_build_index.py --asks --path skills/session-kickoff/SKILL.md` each
  exit 0.
  Red when: the render was edited by hand away from its template, or the method spells a flag
  combination `gen_build_index.py` refuses.
  permission: run after unit 10 is built; before it, the second command exits 2 by design.
- **AC6** — When `bash tools/memory-tree/check-method-carriers.sh` runs, it exits 0, and
  `grep -n "Step 4" memory/project/method-carriers.txt` hits the engine's row.
  Red when: the engine gained an `## M` heading, or its row still names Step 5b alone.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh` runs after the landing commit, it
  exits 0 with `last-audit` naming a commit that contains both edited watched files.
  Red when: check 5 reports unaudited drift on a watched path.

No new refusal or gate clause is added, so nothing here is observed RED on a staged break; each
`Red when:` names the break the existing checker already reports.

## 7. Gates

`kickoff engine size <=18KiB` · `build-method size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The three self-test legs are owed by the `skills/session-kickoff/` guard, and the two recall legs by
the method render's guard, which the recall corpus reads. All run once, at the close.

## 8. Open questions

- **F1** — Where in the method do the two commands live?
  Options: M5, beside the two set-wide probes read before code; M6, beside the post-commit
  `--for-diff` run; a new M-section. A new section costs a heading every M11 carrier and
  `check-unattended.sh` arm B resolve against, and M6 is the wrong moment.
  RESOLVED (agent, 2026-10-04, delegated): M5.
- **F2** — Does Step 4's recall paragraph also collapse into the pointer?
  Options: collapse it too, since M5 spells `query.py`; keep it. The recall kit is separately
  adoptable, so an adopter with recall and no memory-tree kit would lose its only instruction.
  RESOLVED (agent, 2026-10-04, delegated): keep it; the brief names the two context commands only.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the engine, the method's template and render, the size
  limits and the high-water record at base.

## 10. Reuse audit

The seam is the method's existing render pair: `tools/memory-tree/BUILD-METHOD.template.md`,
rendered by `adopt-memory-tree.sh --render` and graded by the kit/dogfood parity leg, plus the
engine's existing method pointer at Step 5b, whose spelling S2 reuses. No code is added.
`python tools/codebase-map/reuse_lookup.py "point the kickoff step at the bug-class checklist and
open asks for the entrypoint paths"` returned `SESSION-KICKOFF.md` and `render_ask_row` by name stem
and no existing path-set context pointer, and its header printed `unscanned layers: .sh`, which
does not touch these markdown carriers. Recall named `TOOL-aWeighedCompass-14`, which measured
`--for-paths tools/` selecting the catalogue rather than a checklist; that is why the pointer runs the
commands over the pointer-map row's entrypoints, never a whole tree. Recall also returned the
manifest's own command block, where `--for-paths` is annotated "Step 4". Where the report and the
tree disagree: the report's "18,407 of 18,432" still holds at base, and the report's claim that the
method spells the two commands is a target, not today's tree — neither is in the method yet.

Recall terms used: `python tools/memory-recall/query.py "which record decides what kickoff Step 4
tells a session to run for bug classes and asks before code" --terms "session-kickoff Step 4 gotchas
--for-paths pointer-map entrypoints READY card classes engine byte cap build method carrier"`
