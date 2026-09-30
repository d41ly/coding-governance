# TOOL-dAlignedCarrier-6 — the owed self-test bar is announced at VERIFYING, and the main loop exports its flag

**Status:** CLOSED · rev-4 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · closes TOOL-dDerivedDocket-70 · ratified 2026-09-30

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
  kit work owes that form too, paid by exporting the pair `GATE_FULL=1 GATE_SELFTESTS=1` (rev-4, S11)
  into the one `--close` when the VERIFYING notice names a surface. The bullet's gate-guard sentence
  is kept, and its closing sentence ("Under `LANDER_MODE` set to `in-place` the close ANNOUNCES ...")
  is rewritten: the move into
  VERIFYING announces under every mode, and the main loop exports the pair into its one `--close`.
  Its Close section gives the sequence per `LANDER_MODE`. Under `in-place`: the move
  `--phase <slug> VERIFYING --witness <sha>`, a commit of the record it staged, then `--prepare`, then
  the close, with the pair exported when the notice named a surface, and NO second move after
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
- **S10** — The closing review's M1. `verb_phase` stages the record after its LAST write, the
  witness, not between the phase and the witness, so a move stages the whole record and the Skill's
  "commit the record the move stages" commits all of it. The unit-6 suite arm commits only what the
  move staged and asserts nothing is left unstaged; the TOOL-aBoundedVerdict-15 `--phase` arm makes a
  second move with a changed witness and asserts the same. The class is gated by a new check 48 of the
  kit gate: no function of a shipped shell file writes a run-state fact after its last staging of
  that file. Observed by AC9.
- **S11** — The closing review's M2, resolved by §8 F5. The notice, the Skill's Close paragraph and its
  export line, the "While it runs" bullet, the protocol's `SELFTESTS_OWED_PATHS` row and both conf
  comments name the PAIR, `GATE_FULL=1 GATE_SELFTESTS=1`, as what the main loop exports into its one
  `--close`. The driver still sets neither. A suite arm cuts the export out of the notice, applies it
  to the close exactly as printed under both modes, and reads both flags from the bar stub's own
  environment. Observed by AC10.
- **S12** — The closing review's L1. The range read in `print_selftests_owed` passes `--no-renames`
  and `-c core.quotepath=off`, and a diff that fails announces that the answer is unanswerable, not
  no. A suite arm commits a rename out of the declared prefix and nothing else and expects the notice.
  The class is a `memory/gotchas/` record. Observed by AC11.
- **S13** — The closing review's L2. Check 45's header, its blank-key echo and its fail message name a
  run's range and the move into VERIFYING, not the in-place close, and the two arm literals in
  `tools/unattended/check-unattended.test.sh` change in the same commit. Check 47 becomes a table of
  two retired premises, its second row the close as the announcer, each row with its own fail line and
  its own staged arm and near-miss control. Observed by AC12.

## 3. Non-goals (OUT)

- A Definition-of-Done item that refuses `--close` when the range owes the flagged bar and the close's
  environment lacks the flag. The ruling kept the driver out of the decision; such an item is a
  follow-up for the owner, and it would bring back by another route the boundary the charter reserves.
- `--status` printing the notice. That verb is unit 4's in this build, and the ask names the phase
  entry.
- `AGENTS.md`'s merge-bar fence and `.githooks/gate-env.sh`, which restate the on-demand rule. No
  accept clause of this build names either, so M3 veto 2 leaves them to the owner.
- Check 45's VERDICTS. Which declarations it refuses and which it announces are unchanged; rev-4
  rewords its header, its blank-key echo and its fail message only (S13), because the rev-1 reason
  for leaving it, that its message stayed true, covered the message and never weighed the header.
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
its own watched file; the two re-stamps are sequential and neither reads the other. The rev-4 fold
adds `tools/unattended/check-unattended.sh` and its suite, where unit 1 owns check 47's first row;
this unit adds its second row, rewords check 45 and adds check 48, and leaves the first row's pattern
and fail line byte-for-byte.

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
unattended: the run's range <base8>..HEAD touches a declared self-test surface (<prefixes>), so the kit Definition of Done owes the flagged bar: export GATE_FULL=1 GATE_SELFTESTS=1 into this run's one --close, whose bar inherits both; this driver sets neither
unattended: SELFTESTS_OWED_PATHS is blank, so no range here can ever owe the flagged bar and no phase move will announce one
unattended: the record pins no base, so the range that decides whether the flagged bar is owed cannot be read, and no notice is printed; whether it is owed is unanswerable here, not no
unattended: the record's base <base8> does not resolve in this clone, so the range that decides whether the flagged bar is owed cannot be read, and no notice is printed; whether it is owed is unanswerable here, not no
unattended: the run's range <base8>..HEAD could not be diffed, so whether the flagged bar is owed is unanswerable here, not no
```

The first line names the pair since rev-4 (§8 F5), and the last line is rev-4's (S12). The range is
read with `--no-renames` and `-c core.quotepath=off`, so a rename names both of its paths.

The builder may reword for accuracy, and must keep the leading `unattended:`, the phrase
`touches a declared self-test surface` the suite already matches, the range and the prefixes.

### The protocol row

```
| `SELFTESTS_OWED_PATHS` | path prefixes whose touch in the run's range from its pinned BASE makes the move into `VERIFYING` ANNOUNCE the flagged bar is owed, which the main loop pays by exporting `GATE_FULL=1 GATE_SELFTESTS=1` into its one `--close`. Blank means never, announced |
```

### The fold of the closing review's round 1 (rev-4)

- **M1, S10.** `set_fact ... witness` moves above `stage_or_fail` in `verb_phase`. Check 48 is a
  per-function source-order scan over every tracked `*.sh` under the kit directory: an event is a call
  of the fact writer or the staging refusal on a plain variable, and a write after the function's last
  staging of the same variable is a hit. Run before wiring: one hit at `3c45a567` (`verb_phase`), none
  after the move, over 602 functions of which 18 stage.
- **M2, S11.** Option (a) of the review, §8 F5. Under `primary` the close's bar carries no
  `GATE_FULL`, so the pair is what makes the export the flagged bar under both modes.
- **L1, S12.** The review's own replacement line, with its announcement for a failed diff.
- **L2, S13.** Check 47's awk program is held once in a variable and run per row. Row 2's pattern is
  the hyphenated mode token within two words of a word opening `close`, within three words of a word
  opening `announc`, or the reverse order with the token directly before the close. Run before
  wiring: at BASE it names the protocol row, two Skill sentences and the check-45 header; on the tree
  it named the check-45 header alone, which S13 rewords.

### Rollout

The render is `bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template
edit; it re-renders the Skill and re-copies the protocol and the stop contract. `bash tools/unattended/adopt-unattended.sh --check`
is the parity observation.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/SKILL.template.md` ·
`.claude/skills/unattended/SKILL.md` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/.unattended.conf.example` ·
`.unattended.conf` · `memory/guides/SESSION-KICKOFF.md` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md` · `memory/gotchas/INDEX.md`

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
- **AC9** — When `--phase <slug> BUILDING`, a commit of what it staged, then `--phase <slug> VERIFYING`
  with the moved HEAD as witness run over the scratch fixture, `git diff --name-only` prints nothing
  after the move, committing what it staged leaves `git status --porcelain` empty, and the committed
  record's `witness:` is the move's own; a second move with a changed witness leaves nothing unstaged
  either. The driver at `3c45a567` leaves `memory/builds/tRun/RUN.md` unstaged on the same steps. And
  when `bash tools/unattended/check-unattended.sh --skip 28` runs with `verb_phase`'s staging moved
  back between its two writes, it prints `UNATTENDED check 48 FAILED` naming `verb_phase`; over the
  tree it prints no check 48 line.
  Red when: a move leaves part of the record unstaged, or check 48 is silent on the staged break or
  red over the tree.
  fixture: none in the tree; the pass builds a scratch repository under `%TEMP%`.
- **AC10** — When the move into VERIFYING runs over the touching fixture under `primary` and under
  `in-place`, the export its notice prints, cut from the notice's text and applied to `--close`
  exactly as printed with both flag names unset beforehand, reaches the bar stub's recorded
  environment with both flags at 1 under both modes; the driver at `3c45a567` prints an export whose
  `primary` close leaves `GATE_FULL` unset. And `wc -c < tools/unattended/PROTOCOL.template.md`, read
  before and after the fold, differs by at most 300.
  Red when: under either mode the stub records either flag unset, or the fold takes more than its
  share of the protocol.
  figure: the 300-byte share is PINNED, allocated to this fold by its brief from the 404 bytes free
  after the build pass.
  permission: the suite arm that makes the same observation is written and not run, under the build
  README's rule; the fixture runs its steps.
- **AC11** — When the fixture's only commit after the preflight is
  `git mv kitsurface/thing.txt moved-out.txt`, the move into VERIFYING prints the owed line naming
  `kitsurface/`, where the driver at `3c45a567` prints none; a rename into the prefix announces and a
  rename between undeclared paths does not. And `python tools/memory-tree/gotchas.py --check` exits 0
  with the class record added.
  Red when: a rename out of the declared prefix reads as an untouched range, or the class record fails
  the catalogue's checks.
- **AC12** — When `bash tools/unattended/check-unattended.sh --skip 28` runs with the line
  `# the in-place close announces the owed bar` appended to a shipped kit file, it prints
  `UNATTENDED check 47 FAILED` with the second row's message; over the tree it prints no check 47
  line; and `grep -c 'in-place close derives' tools/unattended/check-unattended.sh` prints 0, where
  `3c45a567` prints 1.
  Red when: the retired premise can come back unflagged, or check 45's header still names the close
  as the announcer.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `kickoff-manifest ratchet` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: `tools/unattended/unattended.test.sh` · a move into VERIFYING over a range touching the fixture's declared prefix, an untouching range and a move into BUILDING · none
New arm: `tools/unattended/unattended.test.sh` · the VERIFYING move's staged set committed alone, and a second `--phase` with a changed witness, each asserting nothing unstaged · none
New arm: `tools/unattended/unattended.test.sh` · the notice's printed export applied to the one close under both modes, read from the bar stub's environment · none
New arm: `tools/unattended/unattended.test.sh` · a rename out of the declared prefix and nothing else, expecting the notice · none
New arm: `tools/unattended/check-unattended.test.sh` · check 47's second row staged in both word orders, with a near-miss control · none
New arm: `tools/unattended/check-unattended.test.sh` · check 48 staged as a write after the last stage, with the reversed order as its near-miss control · none

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
- **F5 — What does the notice tell the main loop to export, now that it announces under `primary`
  too?** The closing review's M2: under `primary` the close's bar carries no `GATE_FULL`, so exporting
  `GATE_SELFTESTS=1` alone lifts the hold and leaves every guarded self-test leg the branch did not
  move reporting skip, while the notice, the Skill and the protocol row say the flagged bar was paid.
  (a) Name the pair, `GATE_FULL=1 GATE_SELFTESTS=1`, in the notice, the Skill's Close paragraph and
  export line, the protocol row and both conf comments; the driver still sets neither, and gate-guard
  already admits both prefixes from VERIFYING. (b) Narrow the claim: under `primary` the notice says
  the export buys a guard-scoped run and names the pair as what the Definition of Done owes.
  Recommendation (a), the review's. RESOLVED (agent, 2026-09-30, delegated): (a). Owner ruling
  TOOL-dDerivedDocket-70 names the flag the main loop exports and forbids the driver setting it, and
  the charter's kit Definition of Done names the pair; adding `GATE_FULL=1` to the export keeps both
  true under `primary`, where the close's bar carries no `GATE_FULL`, and it is redundant and harmless
  under `in-place`. (b) leaves a default adopter's notice prescribing a remedy that does not pay the
  clause it names. Neither option touches a governance carrier or widens a write surface.

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
- rev-4 · 2026-09-30 · §2 §3 §4 §6 §7 §8 · S6 S10 S11 S12 S13 · AC9 AC10 AC11 AC12 · the fold of the
  closing diff review's round 1, CONVERGED with no blocker, every finding disposed by severity. M1
  (S10, AC9): `verb_phase` staged between its two writes; it now stages after the witness, two arms
  assert nothing is left unstaged, and check 48 gates the class. M2 (S11, AC10): under `primary` the
  exported flag alone bought a guard-scoped run; §8 F5 resolves it as the pair, and an arm exercises
  the printed export under both modes, and S6's three mentions of the exported flag name the pair.
  L1 (S12, AC11): the range read was blind to a rename out of a prefix; it passes `--no-renames` and
  a quotepath override, announces a failed diff, and the class is a gotcha record. L2 (S13, AC12):
  check 45's header still named the close as the announcer; it is reworded with its echo and
  message, their arm literals move with them, and check 47 gains a second row. The §3 non-goal on
  check 45 is narrowed to its verdicts, since rev-1's reason covered its message and never its
  header. AC6's 120-byte share measured the build pass (117); the fold's own share is AC10's.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "announce when a range touches a declared self-test
surface"` ranked name-stem neighbours outside this kit (`build_self_chain`, `drop_touched_exemptions`)
and reported `.sh` as an unscanned layer. The seam is `print_selftests_owed` itself, kept and re-aimed
rather than copied: its prefix match and its blank announcement stay, its range source moves to the
pinned `base` fact every verb already reads through `fact`, and its call site moves to the two
functions every entry into VERIFYING passes through. The rev-4 fold reuses check 47's own scanner for
its second row, held once and run per row, rather than writing a second normalisation, and check 48
takes the population the same way check 47 does, from `ls-files` under the derived kit directory.

Recall terms used: `print_selftests_owed SELFTESTS_OWED_PATHS GATE_SELFTESTS flagged bar VERIFYING
close on-demand main loop kit Definition of Done`.
