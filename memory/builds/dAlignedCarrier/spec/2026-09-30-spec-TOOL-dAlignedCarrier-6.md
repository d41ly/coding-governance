# TOOL-dAlignedCarrier-6 — the owed self-test bar is announced at VERIFYING, and the main loop exports its flag

**Status:** CLOSED · rev-3 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · closes TOOL-dDerivedDocket-70 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-build-TOOL-dAlignedCarrier-6-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-dAlignedCarrier-6-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-6-fold-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-6-fold-brief.md) | journal | — |
| [2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md) | diff-review | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 |

<!-- /gen:spec-records -->

## 1. Goal

`print_selftests_owed` tells a run that its kit Definition of Done owes the flagged bar, and tells it
to run that bar by hand at VERIFYING. It prints inside the `--close` that runs the bar and commits
LANDING, so the instruction arrives after VERIFYING is over, and the build that landed it did so with
its held legs unrun over its last kit commits. The owner ruled that the notice moves to VERIFYING
entry, that the main loop exports the flag into its one `--close` when the range owes it, and that
the driver still sets the flag nowhere. This unit moves the notice, points it at the run's own range,
and has the Skill and the declarations describe the new order.

## 2. Scope (IN)

- **S1** — `print_selftests_owed` in `tools/unattended/unattended.sh` takes the run-state file and
  reads its range as `git diff --name-only <base> HEAD`, where `<base>` is the run's pinned `base`
  fact, instead of `HEAD^1..HEAD` of a prepared merge. Four outcomes: a range touching a declared
  prefix prints the owed line, §4 "The notice"; a range touching none prints nothing, as today; a blank
  `SELFTESTS_OWED_PATHS` prints the blank announcement, as today; a record pinning no `base` prints
  that the range is unanswerable, and so does a pinned `base` this clone cannot resolve, whose
  `git diff` would print nothing and read as an untouching range. No line is prefixed `close`.
  Observed by AC1, AC2.
- **S2** — `verb_phase` calls it after its `phase VERIFYING · witness` line when the target phase is
  `VERIFYING`, whatever `LANDER_MODE` declares, and for no other target. Observed by AC1, AC3.
- **S3** — `print_resume_orientation` calls it when its phase argument is `VERIFYING`, so a session
  that resumes or takes over a run at VERIFYING, after a compaction or a process death, reads the
  notice again. Observed by AC3.
- **S4** — The `gates-green` branch of `--close` makes no call to it, and `GATE_SELFTESTS` stays
  neither set nor unset in the bar's environment, so an exported flag reaches the bar by inheritance
  and the driver adds nothing. Observed by AC4.
- **S5** — The header comment above `print_selftests_owed` is rewritten to cite the owner's ruling on
  this ask: the notice is read at VERIFYING, the main loop pays the flagged bar by exporting the flag
  into its one close, an unattended main loop counts as on demand, and no line of the driver sets it.
  Observed by AC4.
- **S6** — The Skill template's "While it runs" bullet has its sentence on the flagged form rewritten:
  kit work owes that form too, paid by exporting `GATE_SELFTESTS=1` into the one `--close` when the
  VERIFYING notice names a surface. The bullet's gate-guard sentence is kept, and its closing sentence
  ("Under `LANDER_MODE` set to `in-place` the close ANNOUNCES ...") is rewritten: the move into
  VERIFYING announces under every mode, and the main loop exports the flag into its one `--close`.
  Its Close section gives the sequence per `LANDER_MODE`. Under `in-place`: the move
  `--phase <slug> VERIFYING --witness <sha>`, a commit of the record it staged, then `--prepare`, then
  the close, with `GATE_SELFTESTS=1` exported when the notice named a surface, and NO second move after
  the prepare: a move stages the record, and the in-place close refuses a non-empty porcelain
  (check 62). The range the prepared merge adds is the over-announce §8 F2 accepts. Under `primary`:
  the move, its commit, then the close. The paragraph opening "It also ANNOUNCES, on an in-place
  close" is rewritten to match. The render follows. Observed by AC5.
- **S7** — The `SELFTESTS_OWED_PATHS` row of the protocol's §8 table
  (`tools/unattended/PROTOCOL.template.md:457` at BASE) is rewritten to §4's cell. The render follows.
  The pass grows the protocol by at most 120 bytes. Observed by AC6.
- **S8** — The comment above `SELFTESTS_OWED_PATHS` in `tools/unattended/.unattended.conf.example`,
  and the one in this repo's `.unattended.conf`, are rewritten to say the move into VERIFYING
  announces and the main loop exports the flag. Neither value changes. `.unattended.conf` is on the
  kickoff manifest's watch list, so the same commit carries the manifest re-stamp the staged check
  demands. Observed by AC7.
- **S9** — The suite arms are rewritten, not run. In `tools/unattended/unattended.test.sh` the in-place
  close arm that asserted the announcement asserts its absence; new arms assert the notice on
  `--phase ... VERIFYING` over a range touching the fixture's declared prefix, its absence over an
  untouching range and on a move into `BUILDING`; the arms asserting the bar's environment, the flag
  unset by default and an exported flag passing through unchanged, keep every byte. Observed by AC8.

## 3. Non-goals (OUT)

- A Definition-of-Done item that refuses `--close` when the range owes the flagged bar and the close's
  environment lacks the flag. The ruling kept the driver out of the decision; such an item is a
  follow-up for the owner, and it would bring back by another route the boundary the charter reserves.
- `--status` printing the notice. That verb is unit 4's in this build, and the ask names the phase
  entry.
- `AGENTS.md`'s merge-bar fence and `.githooks/gate-env.sh`, which restate the on-demand rule. No
  accept clause of this build names either, so M3 veto 2 leaves them to the owner.
- Check 45 of the kit gate. Its message names an in-place landing that would never be told, which
  stays true.
- The kit version. The orchestrator moves it once, at VERIFYING.

### Edges

Files shared with a sibling, which are not edges. `tools/unattended/unattended.sh` is also written by
units 1, 3 and 4; this unit touches `verb_phase`, `print_resume_orientation`, `print_selftests_owed`
with its header, and the one call line in the `gates-green` branch. The Skill template and its render
are also written by unit 3, which owns the directive table and the scope paragraphs; this unit owns the
"While it runs" bullet's flag sentence and the Close section's opening block and its ANNOUNCES
paragraph. The protocol template and its render are also written by unit 2 (§4) and unit 3 (§10); this
unit owns the §8 table's `SELFTESTS_OWED_PATHS` row and takes at most 120 of the 582 bytes free.
`tools/unattended/unattended.test.sh` is also written by units 3 and 4; this unit edits the in-place
close arms and appends the VERIFYING arms. The kickoff manifest's re-stamp is also owed by unit 5 for
its own watched file; the two re-stamps are sequential and neither reads the other.

none

## 4. Design

### Evidence

Read at `87c245b3` on 2026-09-30. `print_selftests_owed` (`tools/unattended/unattended.sh:7035`) has
one call site, inside the in-place arm of `gates-green` (`:7422`), on the bar's first try, after the
preconditions and before the bar runs. It diffs `HEAD^1 HEAD`, the prepared merge's first parent
against the merge. `grep -nE '^[^#]*GATE_SELFTESTS' tools/unattended/unattended.sh` prints nothing:
no code line of the driver names the flag. `verb_phase` refuses HELD, LANDING and the terminal
phases and accepts `VERIFYING`; it does not refuse a move into the phase the record already reads.
The `base` fact is pinned by `--preflight` and read back unchanged. The gate-guard hook
`tools/unattended/gate-guard.js` denies a `GATE_SELFTESTS=` prefix until the record reaches
`VERIFYING`, so the exported close is admitted exactly where the Skill will put it.

### The notice

```
unattended: the run's range <base8>..HEAD touches a declared self-test surface (<prefixes>), so the kit Definition of Done owes the flagged bar: export GATE_SELFTESTS=1 into this run's one --close, whose bar inherits it; this driver sets it nowhere
unattended: SELFTESTS_OWED_PATHS is blank, so no range here can ever owe the flagged bar and no phase move will announce one
unattended: the record pins no base, so the range that decides whether the flagged bar is owed cannot be read, and no notice is printed; whether it is owed is unanswerable here, not no
unattended: the record's base <base8> does not resolve in this clone, so the range that decides whether the flagged bar is owed cannot be read, and no notice is printed; whether it is owed is unanswerable here, not no
```

The builder may reword for accuracy, and must keep the leading `unattended:`, the phrase
`touches a declared self-test surface` the suite already matches, the range and the prefixes.

### The protocol row

```
| `SELFTESTS_OWED_PATHS` | path prefixes whose touch in the run's range from its pinned BASE makes the move into `VERIFYING` ANNOUNCE the flagged bar is owed, which the main loop pays by exporting the flag into its one `--close`. Blank means never, announced |
```

### Rollout

The render is `bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template
edit; it re-renders the Skill and re-copies the protocol and the stop contract. `bash tools/unattended/adopt-unattended.sh --check`
is the parity observation.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/SKILL.template.md` ·
`.claude/skills/unattended/SKILL.md` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/.unattended.conf.example` ·
`.unattended.conf` · `memory/guides/SESSION-KICKOFF.md` · `tools/unattended/unattended.test.sh`

### Alternatives rejected

- Keeping a second notice inside `--close`. The ruling moves it, and a notice inside the verb that
  runs the bar is the defect the ask files.
- Having the driver export the flag when the range owes it. The ruling keeps the flag the main
  loop's.
- Computing the range from the advertised remote tip at VERIFYING. It needs the network at a phase
  move, which fails on every outage, and F2 records why the pinned BASE wins.

## 5. Production-readiness checklist

- security — N/A: an announcement and documentation; the bar's environment is unchanged.
- perf / scale — one `git diff --name-only` per move into VERIFYING, over the run's own range.
- error / empty / loading states — blank prefixes and a record with no `base` each announce
  themselves rather than passing silently; an untouching range prints nothing, as today.
- observability — the notice names the range and the surfaces it matched.
- risks — after `--prepare` makes the landing merge, a resume at VERIFYING reads a range that also
  holds what the merge brought in from the default branch, so it can announce a surface another
  landing touched; the cost is one flagged bar more than strictly owed, never one fewer. And a main
  loop that closes without ever moving into VERIFYING is not told; the Skill's Close section puts the
  move first for that reason.
- testing — the fixture observations and greps below; the suite arms, written and not run.
- migration — none: a record already at VERIFYING reads the notice at its next resume.
- user docs — the Skill's Close section, the protocol row and the two conf comments.

## 6. Acceptance criteria

- **AC1** — When `--phase <slug> VERIFYING --witness <sha>` runs over a fixture whose record pins
  `base` at its first commit, whose `.unattended.conf` declares `SELFTESTS_OWED_PATHS="kitsurface/"`,
  and whose later commit touches a file under `kitsurface/`, it prints the owed line naming
  `kitsurface/` and the range, and exits 0. The BASE driver, extracted by `git archive 87c245b3 tools/unattended`,
  prints no such line over the same fixture.
  Red when: the move is silent over a touched surface, or the BASE driver already prints the line.
  fixture: none in the tree. The pass builds a scratch repository under `%TEMP%`, with the driver run
  from this tree against it.
- **AC2** — When the same move runs over the fixture with the later commit touching nothing declared,
  it prints no owed line; with `SELFTESTS_OWED_PATHS=""` it prints the blank announcement; and with the
  `base` line deleted from the record it prints the unanswerable announcement.
  Red when: an untouching range announces, or either skip is silent.
- **AC3** — When `--phase <slug> BUILDING --witness <sha>` runs over the touching fixture, it prints no
  owed line; and when the holder's `--resume <slug> --keepalive-id k1` runs over the record at
  `VERIFYING`, with the session and pid environment the record names, it prints the owed line after
  its orientation lines.
  Red when: a move to another phase announces, or the resume at VERIFYING does not.
- **AC4** — When `grep -nE '^[^#]*print_selftests_owed' tools/unattended/unattended.sh` runs, it prints
  the definition and exactly two call sites, one in `verb_phase` and one in `print_resume_orientation`,
  where BASE prints the definition and one call in the `gates-green` branch; and
  `grep -nE '^[^#"]*GATE_SELFTESTS=' tools/unattended/unattended.sh` prints nothing, as at BASE.
  Red when: the close still calls the notice, or any code line assigns or exports the flag.
- **AC5** — When `grep -c -E 'nowhere earlier|by hand at' tools/unattended/SKILL.template.md` runs, it
  prints 0, where BASE prints 2; `awk '/^## Close/,0' tools/unattended/SKILL.template.md | grep -c -- '--phase <slug> VERIFYING'`
  prints at least 1, where BASE prints 0; inside `## Close` the `--phase <slug> VERIFYING` line comes
  before the `--prepare` line; the Close section spells the exported close once;
  `awk '/^## While it runs/,/^## While the work runs/' tools/unattended/SKILL.template.md | grep -c 'close ANNOUNCES'`
  prints 0, where BASE prints 1; and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: the Skill still sends the flagged bar to a by-hand run, still says the close announces,
  orders a phase move after the prepare, or the render differs.
- **AC6** — When `grep -n '^| .SELFTESTS_OWED_PATHS. |' memory/guides/UNATTENDED-PROTOCOL.md` runs, it
  prints one row naming `VERIFYING` and `--close`, and not the in-place close as the announcer;
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` exits 0;
  `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 0; and
  `wc -c < tools/unattended/PROTOCOL.template.md`, read before and after the pass, differs by at most
  120.
  Red when: the row still names the close as the announcer, the render differs, or the pass takes
  more than its share.
  figure: the 120-byte share is PINNED, allocated on 2026-09-30 from the 582 bytes free at BASE.
- **AC7** — When `sed -n '/^# THE KIT SURFACE OF THIS REPO/,/^SELFTESTS_OWED_PATHS=/p' .unattended.conf`
  and `sed -n '/^# THE SELF-TEST SURFACE/,/^SELFTESTS_OWED_PATHS=/p' tools/unattended/.unattended.conf.example`
  run, neither block says the close announces, both name the move into VERIFYING, and each ends on the
  value line it ended on at BASE; and `bash skills/session-kickoff/manifest-check.sh --staged` exits 0
  over the staged pass.
  Red when: a comment still describes the close as the announcer, a value line moved, or the watched
  conf is committed without its re-stamp.
- **AC8** — When `grep -c -E -- '--phase [A-Za-z]+ VERIFYING' tools/unattended/unattended.test.sh` runs, it
  prints at least 1, where BASE prints 0; and `git diff -U0 -- tools/unattended/unattended.test.sh`
  over the pass shows no line of the two arms that read the bar's environment for the flag, the one
  asserting it unset and the one asserting an exported value passes through.
  Red when: the arms still expect the close to announce, or the pass-through arm moved.
  permission: running the suite is waived for this landing by the build README's rule; the arms are
  written and their run is not observed here.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `kickoff-manifest ratchet` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: `tools/unattended/unattended.test.sh` · a move into VERIFYING over a range touching the fixture's declared prefix, an untouching range and a move into BUILDING · none

## 8. Open questions

- **F1 — Who pays the owed flagged bar, and when is it announced?** The owner ruled on this ask's
  parked decision: when a landing touches a declared self-test surface the main loop exports
  `GATE_SELFTESTS=1` into its one `--close`, the driver never sets it, the owed notice moves to
  VERIFYING entry, and an unattended main loop counts as on demand. RESOLVED (owner, 2026-09-30): as
  ruled; S1 to S6 build it.
- **F2 — Which range does the notice read at VERIFYING entry, where no prepared merge exists yet?**
  (a) The pinned `base` fact to HEAD, a recorded value read offline. (b) The merge-base with the local
  default branch, which may be stale. (c) The remote's advertised tip, which needs the network at a
  phase move. (a) over-announces only after a merge brings in another landing's kit commits, which
  costs a bar and never skips one; (c) fails on every outage. Recommendation (a). RESOLVED (agent,
  2026-09-30, delegated): (a), the only option readable offline from a fact the run already pinned.
- **F3 — Does the notice fire under every `LANDER_MODE`, or under `in-place` alone as today?** (a)
  Every mode: the kit Definition of Done owes the flagged bar whatever shape the landing takes, and the
  close's bar inherits an exported flag under `primary` as well. (b) `in-place` alone, the old gate.
  Recommendation (a). RESOLVED (agent, 2026-09-30, delegated): (a), the ruling names no mode.
- **F4 — Are the two conf comments rewritten?** (a) Both, with the manifest re-stamp the watched gov
  conf owes. (b) The kit example alone, leaving gov's comment describing a close that no longer
  announces. (b) leaves prose in the conf every run here reads that states the retired behaviour.
  Neither is a governance carrier. Recommendation (a). RESOLVED (agent, 2026-09-30, delegated): (a).

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, from the ask's accept clause, the owner's ruling and the
  build's spec brief.
- rev-2 · 2026-09-30 · §2 §6 · S6 AC5 · the M2 cross-read found S6's "repeat the move before the
  close" refused under in-place landing, where a move stages the record and the close demands a clean
  porcelain (check 62), and found the bullet's closing "the close ANNOUNCES" sentence left standing.
  S6 now gives the sequence per `LANDER_MODE` with no move after `--prepare`, and rewrites that
  sentence; AC5 observes both.
- rev-3 · 2026-09-30 · §2 §4 · S1 · the build pass. A pinned `base` this clone cannot resolve now reads
  as the unanswerable outcome too, with its own line in §4 "The notice": `git diff` over it printed
  nothing and read as an untouching range, the silent skip §5 rules out. Both unanswerable lines end
  "unanswerable here, not no". The suite arms sit inside the in-place block after its untouching
  close arm, reusing `ipreset`, and add the resume, blank and no-base readings beside S9's three. No
  acceptance criterion moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "announce when a range touches a declared self-test
surface"` ranked name-stem neighbours outside this kit (`build_self_chain`, `drop_touched_exemptions`)
and reported `.sh` as an unscanned layer. The seam is `print_selftests_owed` itself, kept and re-aimed
rather than copied: its prefix match and its blank announcement stay, its range source moves to the
pinned `base` fact every verb already reads through `fact`, and its call site moves to the two
functions every entry into VERIFYING passes through.

Recall terms used: `print_selftests_owed SELFTESTS_OWED_PATHS GATE_SELFTESTS flagged bar VERIFYING
close on-demand main loop kit Definition of Done`.
