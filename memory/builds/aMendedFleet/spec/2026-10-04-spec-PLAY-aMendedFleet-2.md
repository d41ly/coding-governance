# PLAY-aMendedFleet-2 — an experiment's instruments and result rows are committed beside its record, and the vague-brief arm gates §1 as a HIGH ask

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams playbook · advances PLAY-aMendedFleet-5 · ratified 2026-10-04 · order 80

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The aBlindedTrial build ran the one blinded trial this repository has, and its report says every
figure names a file under a scratch root in `%TEMP%`. That root now holds no file: the cells, the
results and every script are gone, and only the briefs survive, because a journal copied them. A
figure whose instrument is gone can be neither re-derived nor re-run. This unit adopts the rule the
review asks for `[B#19]`: an experiment's instruments and result rows are committed beside its
unit's record, never left only under a temp directory. It is one charter bullet, rendered into
`AGENTS.md`. It then files the untested vague-brief arm as a HIGH ask that gates the charter's §1
`[B#22]`, so the design-pass rule changes only on a recorded reading of that arm, which unit 73
produces.

## 2. Scope (IN)

- **S1** — THE RULE. One bullet in `coding-governance-agents.template.md` §8, on the line after the
  bullet that opens "Persist each Tier-2 run as an in-repo artifact folder", reading:
  "Commit an experiment's instruments and result rows beside its unit's record, never only to a temp
  directory: a figure whose instrument is gone can be neither re-derived nor re-run." No placeholder
  and no id, because the template is project-agnostic. Observed by AC1 and AC3.
- **S2** — THE RENDER. `bash tools/playbook/adopt-playbook.sh --target .` re-renders `AGENTS.md`'s
  charter region, so the bullet lands there byte-identical in the same commit. Observed by AC2.
- **S3** — THE SIZE. Both size subjects stay inside their declared ceilings. Where a subject's
  measured figure passes its recorded high-water, the pass re-records it with
  `bash tools/check-template-size.sh --bump <subject>` and names the byte delta in a `Decided:`
  trailer, because growth is priced against that record. Observed by AC3.
- **S4** — THE ASK, filed in this build's own `BACKLOG.md` under the id the orchestrator mints and
  writes into this unit's brief. Three rows:
  - under `## Asks`, one physical line: the ask, its text saying the charter's §1 design pass keeps
    the full Tier-2 spec until a recorded reading of the vague-brief arm decides otherwise, the two
    figures the first trial measured on explicit briefs, an `accept` clause naming an owner ruling on
    §1's design-pass shape that cites unit 73's trial report, and the pointer
    `→ coding-governance-agents.template.md`;
  - under `## Dispositions`, `SEV · <ask> · HIGH · <why>`, the why naming §1 as the rule every
    Tier-2 unit pays;
  - under `## Dispositions`, `KEEP · <ask> · <why>`, the why saying the reading is unit 73's and
    the ruling is the owner's, so this build closes nothing.
  The spec's status header gains `advances <ask>` in a rev bump with its §9 line, so the unattended
  `asks-disposed` item reads the ask as KEEP after a CLOSED unit that advances it. Observed by AC4
  and AC5.
- **S5** — THE MANIFEST STAMP. The template is on the kickoff manifest's `watch:` line, so the
  commit that moves it re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` with a delta
  line in its message; the staged manifest leg of `.githooks/pre-commit` refuses the commit
  otherwise. Observed by AC6.

## 3. Non-goals (OUT)

- A gate or hygiene check that detects an instrument left in a temp directory. No population names
  "an experiment's instruments", so a predicate would grade a guess, and the review's do-not-build
  list forbids a general experiment framework before a second experiment exists. §8 F1 records the
  documented-check disposition.
- Running the vague-brief arm, or any trial. That is `TOOL-aMendedFleet-73`, which obeys S1.
- Changing §1's design-pass rule. The ask gates it; the owner rules on it.
- Recovering the first trial's lost instruments. Its record keeps their figures.
- Bumping the charter template's version marker, owed once at the close for every unit of this
  build that moves the template.

### Edges

- **consumes-from** `TOOL-aMendedFleet-73` — the arm whose trial report the ask's `accept` clause
  names; without it the ask waits on a reading nobody produces.
- **consumes-from** `PLAY-aMendedFleet-1` — the wrapper trim that frees the `AGENTS.md` headroom S2
  spends; at base the charter sits 168 bytes under its 64512-byte row.
- **consumes-from** external — the ask id the orchestrator mints before dispatch, since a writer of
  this build never mints one.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04; every file below is byte-identical at the worktree tip
`8312d315`.

- The aBlindedTrial trial report under that build's `build/` folder opens by naming its scratch root,
  `C:/Users/daily-agent/AppData/Local/Temp/xp/`, as untracked. `find` over that root on node a
  prints 0 files and ten empty directories, PINNED 2026-10-04. Unit 73's §4 records the same.
- The aReplayedCard build's ask about its counterfactual arm already wrote each agent return under
  `memory/builds/aReplayedCard/build/`: the practice exists and no rule states it. `grep -n -i
  "instrument"` over the template, `memory/guides/BUILD-METHOD.md` and `memory/HYGIENE.md` finds
  no rule about where one lives.
- Template §8's "Persist each Tier-2 run as an in-repo artifact folder" bullet is the nearest
  rule: it makes a review's record durable and says nothing of an experiment's.
- `bash tools/check-template-size.sh` reports 48193 of 49152 bytes for the template; the
  high-water record holds 48378. `AGENTS.md` measures 64344 against its 64512 row, with a recorded
  high-water of 60930, so the charter-size leg prints an advisory WARN at base. All PINNED
  2026-10-04. S1's bullet is about 175 bytes.
- `.memory-tree.conf` sets `BACKLOG_MODE` to `builds`, so an ask is filed once in its own build's
  `BACKLOG.md`. The row grammar, `SEV`, `KEEP`, `accept` and verdicts V10, V12 and V14 are the
  memory-tree kit README's "Row kinds" and "Verdicts" sections. This build holds no `BACKLOG.md` at
  base; unit 14, ordered earlier, files its triage ask in the same file, and this pass appends.
- `memory/guides/UNATTENDED-PROTOCOL.md`'s `asks-disposed` item accepts an ask this build filed when
  it reads KEEP after a CLOSED unit that `advances` it. Unit 14 uses the same shape.

### Rollout

`PLAY-aMendedFleet-1` trims the wrapper first, at order 79, and unit 73 is ordered before this one. The pass edits the template,
re-renders `AGENTS.md`, bumps a high-water only where S3 says, appends the three rows and rev-bumps
this spec's header with `advances`, in one commit. The orchestrator regenerates the build index and
the PLAY family view afterwards.

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `AGENTS.md`
- `tools/template-size-highwater.txt`
- `memory/builds/aMendedFleet/BACKLOG.md`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **The rule in `memory/guides/BUILD-METHOD.md` M12.** M12 governs research inside a spec pass, and
  an experiment is not always one; it is also a memory-tree kit file under its own byte cap, while
  the review names the rule a charter rule.
- **Folding the rule into the "Persist each Tier-2 run" bullet.** That bullet points at the reviews
  folder; an instrument belongs under the unit's own record folder, and one bullet carrying two
  directives breaks the template's one-line-per-directive rule.
- **A `BLOCKED` row holding the ask on unit 73.** It releases the ask the moment unit 73 closes,
  before any owner ruling, and a `KEEP` row is what `asks-disposed` reads.

## 5. Production-readiness checklist

- security — N/A — a prose rule and three record rows; no write path.
- perf / scale — every session reads about 175 bytes more of the charter, ESTIMATED.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — the ask shows HIGH in the PLAY family view and in `--asks`, where an owner finds it.
- risks — the rule is ungated; §8 F1 says why. The charter's headroom is thin until
  `PLAY-aMendedFleet-1` lands.
- testing — direct greps, the render check, the two size checks and the asks verb.
- migration — N/A — no stored state.
- user docs — N/A — the charter is the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -c "never only to a temp directory" coding-governance-agents.template.md` runs,
  it prints 1, and `grep -n -A1 "Persist each Tier-2 run" coding-governance-agents.template.md`
  shows that bullet on the line after it.
  Red when: the rule is missing, duplicated, or placed outside §8.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it exits 0, and
  `grep -c "never only to a temp directory" AGENTS.md` prints 1.
  Red when: the template moved and the rendered region did not.
- **AC3** — When `bash tools/check-template-size.sh` and `bash tools/check-template-size.sh AGENTS.md`
  run, each exits 0, and neither prints a WARN this pass introduced without a matching `--bump` row in
  `tools/template-size-highwater.txt`.
  Red when: either subject passes its declared ceiling, or growth past a high-water went unpriced.
  figure: 49152 and 64512 are the declared rows, read at observation time.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --asks <ask>` runs after the pass, it
  prints `sev HIGH`, an `accept` clause naming the §1 ruling, the template as its pointer and
  `PLAY-aMendedFleet-2` among its live specs.
  Red when: the ask carries no severity or acceptance, or this spec's header does not advance it.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --check` runs after the orchestrator
  regenerates the index, its backlog line reports `0 verdict(s)`.
  Red when: a row is malformed, the ask lacks its `SEV` row, or the ask is filed outside this
  build's folder.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs after the unit's commit, it
  exits 0, and `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` shows the `last-audit:`
  line moved.
  Red when: check 5 reports unaudited drift on `coding-governance-agents.template.md`.

No new refusal or gate clause is added, so nothing here is observed RED on a staged break; each
`Red when:` names the break an existing checker or grep reports.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook render wiring` · `playbook parity` · `memory hygiene` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The two recall legs are owed by the `memory/` guard over this build's `BACKLOG.md`. All run once, at
the close.

## 8. Open questions

- **F1** — Where does the rule live, and is it gated?
  Options: a charter bullet in §8; a paragraph in the build method's M12; a hygiene check refusing a
  build record that cites a temp path as an instrument's home. The check has no population to grade:
  nothing marks a file as an experiment's instrument, and a temp-path grep would also fire on the
  records that honestly report a scratch clone, which this build's own specs do. §7 of the charter
  takes an ungateable class as a documented check.
  RESOLVED (agent, 2026-10-04, delegated): a §8 charter bullet beside the review-persistence rule,
  ungated, per S1; this spec is its documented check.
- **F2** — Is the ask a second mechanism that splits?
  Options: one unit; split the ask to a unit the run adds. The ask is three record rows and no code,
  and the review states the rule and the ask as one point.
  RESOLVED (agent, 2026-10-04, delegated): one unit, per S4.
- **F3** — Who mints the ask's id?
  Options: this unit's pass; the orchestrator. The charter forbids a fan-out child from minting, and
  this unit is built by one.
  RESOLVED (agent, 2026-10-04, delegated): the orchestrator mints it and writes it into the brief,
  as unit 14's triage ask does.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the aBlindedTrial trial report and its emptied scratch
  root, the template's §8, the two size records and the memory-tree kit's row grammar at base.
- rev-2 · 2026-10-04 · S5 · AC6 · §4 · §7 · M2 cross-read: the template is a watched path, which
  units 78 and 94 re-stamp the kickoff manifest for and this spec did not; S5 re-stamps it in the
  same commit and AC6 observes it.
- rev-3 · 2026-10-06 · S4 · the main loop minted PLAY-aMendedFleet-5, filed it with its HIGH severity and KEEP
  row, and added `advances` to the status header; the ask notes that unit TOOL-aMendedFleet-73's run
  stopped at its pilot without a reading, so the gate it describes still has nothing behind it.

## 10. Reuse audit

The seams are template §8's existing review-persistence bullet, which S1 sits beside rather than
duplicating; the existing `## Asks` and `## Dispositions` row grammar of the memory-tree kit, written
by hand exactly as unit 14 writes its triage ask; and `tools/playbook/adopt-playbook.sh`, the one
renderer of the charter region. No code is added. `python tools/codebase-map/reuse_lookup.py "keep an
experiment's instruments and result rows in the build folder instead of a temp directory"` returned
only `build_*` and `*_row` helpers by name stem, `render_ask_row` and `render_status_row` among them,
which render rows a writer could also type; no existing seam fits a prose rule, so none is extended.
Recall returned the aBlindedTrial spec and trial report, which name the `%TEMP%` root, unit 73's
spec, which hands this unit the ask, and the aReplayedCard ask showing the practice already followed
once. Where the report and the tree disagree: none; the report's claim that the instruments are gone
holds, re-measured as 0 files.

Recall terms used: `python tools/memory-recall/query.py "where must an experiment or trial keep its
instruments and result rows, and what gates the charter section 1 design pass" --terms "experiment
trial instruments result rows build folder TEMP scratch vague-brief arm spec-first plan Tier-2 design
pass"`
