# TOOL-dSafePassage-51 — the step module's 15 audit minors from units 47 to 50: build order in commit order, the walk's checks in one sequence, the guard's keys, one section probe

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-51-deviation-97.md](../build/2026-10-23-build-TOOL-dSafePassage-51-deviation-97.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-51-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-51-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-51-title-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-51-title-fix.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-51-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-51-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 47 to 50
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md`)
exited CONVERGED with 22 confirmed findings, none at BLOCKER or HIGH. BUILD-METHOD M4 batches its 22
minors, and they split into two disjoint write sets by M6's clauses, so they are two units.

This unit is the half whose writes are the step module, its self-test and its help page: 6 MEDIUM and
9 LOW findings. Each is named by its report id and is its own scope item, including where the report
merged ids into one item. The other half, the lander's suite and the spec template, is
`TOOL-dSafePassage-52`. These minors land on units 47, 48 and 49, so this unit repairs none in
particular and builds after every unit, at order 14.

Where a minor would bite an earlier pass, the faulted unit's own §3 hands-off bullet to this unit
names it, so that pass may build it. Where a finding's defect is the text of a spec built before this
one, the item states the superseding reading. A criterion here observes it where anything can.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-1 | MEDIUM | 1 | S1 |
| D-2 | MEDIUM | 2, 9 | S4, S5 |
| D-3 | MEDIUM | 4 | S8 |
| D-4 | MEDIUM | 14 | S9 |
| D-5 | MEDIUM | 22 | S6 |
| D-6 | LOW | 3 | S10 |
| D-9 | LOW | 8 | S12 |
| D-10 | LOW | 10, 19 | S2, S3 |
| D-12 | LOW | 12 | S13 |
| D-13 | LOW | 13 | S11 |
| D-17 | LOW | 18 | S14 |
| D-18 | LOW | 23 | S7 |
| D-19 | LOW | 24 | S15 |

That is 6 MEDIUM and 9 LOW findings by raw id. The report's other seven confirmed ids, 6, 7, 11, 15,
16, 17 and 20, land on TOOL-dSafePassage-50 alone and are `TOOL-dSafePassage-52`'s. The report
refuted ids 5, 21 and 25 and left none unverified. The skeptic re-graded id 1 from high to medium and
id 3 from medium to low. It REJECTED the finder's fix of id 14, so S9 is built from the skeptic's
corrected fix.

## 2. Scope (IN)

### The build order, observed where it happened (D-1, D-10)

- **S1** — id 1. TOOL-dSafePassage-49 AC2 reads header verbs, so this unit observes the order the
  builds ran in. The commit that first carries `Pass: TOOL-dSafePassage-4` follows the first ones
  carrying `Pass: TOOL-dSafePassage-43` and `Pass: TOOL-dSafePassage-7`. The first commits carrying
  `Pass: TOOL-dSafePassage-18` and `Pass: TOOL-dSafePassage-19` follow it. TOOL-dSafePassage-49 §8
  F1(a) is read with one more step at its end: the sweep runs TOOL-dSafePassage-49 AC2's header probe,
  and the build run hands out no roster while TOOL-dSafePassage-4's order is not greater than both
  TOOL-dSafePassage-43's and TOOL-dSafePassage-7's. TOOL-dSafePassage-49's §3 hands-off bullet to this
  unit names the reading. Observed by AC1.
- **S2** — id 10. TOOL-dSafePassage-49 F1(a)'s sweep is read widened to the §4 Rollouts of
  TOOL-dSafePassage-2 and TOOL-dSafePassage-7, each rev-bumped with a §9 line naming
  TOOL-dSafePassage-49 S4. TOOL-dSafePassage-7's Rollout keeps "this unit builds first, then
  TOOL-dSafePassage-2" within order 2. TOOL-dSafePassage-2's keeps "after TOOL-dSafePassage-7". Each
  then says, in these words and on one line, that `TOOL-dSafePassage-4 builds at order 3`. Observed
  by AC2.
- **S3** — id 19. The same sweep amends TOOL-dSafePassage-43's §4 Rollout. Its sentence that
  TOOL-dSafePassage-4, "also at order 2", is sequenced after this pass by M6 clause 2 is read as void.
  The amended Rollout says `TOOL-dSafePassage-4 builds at order 3`, after it, so no same-order
  sequencing applies between the two. Its clause on the other order-2 units that share
  `tools/govkit/upgrade_steps.py` stays. Observed by AC2.

### The walk's checks in one sequence (D-2, D-18)

- **S4** — id 2. TOOL-dSafePassage-49 S7's `rev-parse --git-dir` refusal has a fixed place in
  TOOL-dSafePassage-47's walk. TOOL-dSafePassage-47 S2's config read runs first. `rev-parse --git-dir`
  runs only on a candidate whose read exited 0. So the rev-parse refusal is reached only by a readable
  config whose repository git still will not open, the `submodule-format-unknown` plant. §4 "The walk,
  in sequence" is the amended `walk(d)`. TOOL-dSafePassage-49 S7, §5 and §7 are read with it, and its
  §3 hands-off bullet to this unit names the reading. Observed by AC3.
- **S5** — id 9. The audit reproduced that a config holding `[core` makes both commands exit 128 with
  one message, on git 2.54.0.windows.1. So the plant on which both checks fail is
  `submodule-config-malformed`, and it shows which check answers. Under S4 its refusal still names
  `.git/modules/<name>/config`, so TOOL-dSafePassage-47 AC2 holds after TOOL-dSafePassage-49's pass.
  The arm of §7 stages a walk copy that runs `rev-parse` first, under which that refusal no longer
  names the config file. Observed by AC3.
- **S7** — id 23. TOOL-dSafePassage-47 S2's refusal names `<c>/config` "or a file it includes", beside
  the exit code. A read run with `--includes` fails on a malformed included file too, and git names
  that file on stderr, which S2 never parses. TOOL-dSafePassage-47 §5's observability line and S6's
  help sentence are read with the same words. TOOL-dSafePassage-47's §3 hands-off bullet to this unit
  names the reading. Observed by AC3.

### No link followed under `modules/` (D-5)

- **S6** — id 22. TOOL-dSafePassage-47's walk never follows a symlink or a junction. Before it tests
  a directory's shape or descends into it, it tests `os.path.islink(c) or os.path.isjunction(c)`. A
  link under `modules/` is a refusal naming that path. An `OSError` while listing a directory is a
  refusal naming that directory. Both use TOOL-dSafePassage-24's one `raise Refusal` site. The
  `isolation` family gains `submodule-modules-link-loop`: a superproject whose `.git/modules/a/loop`
  links back to `.git/modules`. On Windows the plant makes a junction with `cmd /c mklink /J`, and on
  POSIX a directory symlink. TOOL-dSafePassage-47's §3 hands-off bullet to this unit names the rule.
  Observed by AC4.

### TOOL-49's arm and criteria (D-3, D-4, D-6)

- **S8** — id 4. TOOL-dSafePassage-49's `New arm:` line gains a seventh staged case. It is a
  reverse-walk copy whose move 3 keeps a `rolled-back` row whose witness holds `rolled-back` and sets
  the `down interrupted:` failure on it. Under TOOL-dSafePassage-49 S16's row rule that row is
  refused, so `--plant rolled-back-witness-holds` over the copy raises `Refusal` and exits non-zero.
  So TOOL-dSafePassage-49 AC3 is seen red, and the plant is shown to reach move 3.
  TOOL-dSafePassage-49's §3 hands-off bullet to this unit names the case. Observed by AC5.
- **S9** — id 14, the skeptic's corrected fix. The expected unlisted executor keys live only in the
  guard. `tools/govkit/selftest.py` holds them as a literal set, `{"sendemail.sendmailCmd"}`, beside a
  comment citing git-send-email `:394` and `:1787`. `tools/govkit/upgrade_steps.py` defines no
  `UNLISTED_EXECUTOR_KEYS`. TOOL-dSafePassage-49 S8, §4 "The arm's widening", its Inventory, its
  Alternatives line on the option table and §7 "What the check does not cover" are read as naming the
  selftest literal. The arm of §7 stages a module copy whose `STEP_REFUSED_KEYS` lacks the
  `sendemail.sendmailCmd` row and keeps every other line, and the arm goes red on it.
  TOOL-dSafePassage-49's §3 hands-off bullet to this unit names the reading. Observed by AC6.
  **Readers:** by name: READER NOT IN TREE, because `UNLISTED_EXECUTOR_KEYS` was a name in
  TOOL-dSafePassage-49's unbuilt design, and no tracked file spells it at the base · by value: the
  class arm in `tools/govkit/selftest.py`, which reads the selftest literal in its place.
- **S10** — id 3. TOOL-dSafePassage-49 S13's "fixture code compares through the constant too" is read
  as one form. Fixture code that checks a stop text calls `test_step_row` and never calls `startswith`
  over `DOWN_STOP_PREFIXES`. So TOOL-dSafePassage-49 AC5's count of exactly one such call, inside
  `test_step_row`, holds over the module with its fixture in it. TOOL-dSafePassage-49's §3 hands-off
  bullet to this unit names the form. Observed by AC7.
- **S11** — id 13. TOOL-dSafePassage-49 S6's Readers sentence is read with this reason. TOOL-dSafePassage-29 §4
  "The predicate", widened by TOOL-dSafePassage-37's `hook` suffix and TOOL-dSafePassage-42's
  `tunnel`, `httpd` and `smtpserver`, keeps no key whose last segment is `url` or `pushurl`. So the
  class arm never matches a `remote.<x>.url` or `remote.<x>.pushurl` row. The old reason, kept keys
  that "end in `command` or `cmd`", was false: the predicate also keeps `helper`, `path` and others.
  NOT OBSERVED: a reading of a reason. TOOL-dSafePassage-49 AC7 observes the conclusion.

### One section probe (D-9)

- **S12** — id 8. §4 "The section probe" here is the one probe for the "What a step can reach"
  section of `help/upgrade-steps.md`. It ends the section only at a heading of the same or a higher
  level than the one that opened it, and it skips fenced blocks. TOOL-dSafePassage-47 AC4,
  TOOL-dSafePassage-48 AC3 and TOOL-dSafePassage-49 §4 "The section probe", with its S17 and AC12, are
  read as citing it, in place of the awk line each one typed. The §3 hands-off bullets of those three
  units to this unit name the reading. Observed by AC8.

### Readings of a pin and a record (D-12, D-17)

- **S13** — id 12. TOOL-dSafePassage-48 §4 "Data model", the `sendemail.smtpServer` row, is read as
  citing `:1782-1790`. This unit read git 2.54.0.windows.1's `git-send-email` on node d, 2026-10-23:
  line 1782 is the `elsif (defined $sendmail_cmd || file_name_is_absolute($smtp_server))` branch, and
  line 1790 is `exec ($smtp_server, @sendmail_parameters)`. TOOL-dSafePassage-48's §3 hands-off bullet
  to this unit names the reading. NOT OBSERVED: a reading of a citation, which no code carries.
- **S14** — id 18. TOOL-dSafePassage-49 §10 is read with this unit's §10 beside it. That section runs
  one lookup per behaviour TOOL-dSafePassage-49 mints and records what each ranked. Its recall query
  is written in this unit's own terms, not copied from a sibling. NOT OBSERVED: a reuse record, which
  no code carries.

### The `.gitmodules` type test before any open (D-19)

- **S15** — id 24. TOOL-dSafePassage-49 S18's test is a `stat` taken before any open of
  `<worktree>/.gitmodules`, git's own `config -f` read included. `os.lstat` raising
  `FileNotFoundError` means missing. Otherwise `os.stat` must succeed and `stat.S_ISREG` must hold.
  Anything else is the refusal naming the path: a directory, a FIFO, a device or a dangling link. Only
  then does TOOL-dSafePassage-45 S13's read run. The `isolation` family gains `gitmodules-fifo`, made
  by `os.mkfifo`, which prints a `skip —` line and exits 0 where `os.mkfifo` is absent, as on Windows.
  TOOL-dSafePassage-49's §3 hands-off bullet to this unit names the test. Observed by AC9.

## 3. Non-goals (OUT)

- The lander's suite and the spec template: `TOOL-dSafePassage-52`.
- Rewriting a built spec. An item that corrects a spec's text states the reading here. The exceptions
  are the Rollout sentences S2 and S3 name and the header move they ride with, which TOOL-49 F1(a)'s
  sweep writes before hand-out, as its resolution already places it.
- The report's left-shift gates and checklist entries.
- A change to `tools/workflows/unattended-build.js`. S1's hand-out refusal is the build run's sweep,
  as TOOL-dSafePassage-49 F1(c) already refused the driver change.
- Reparse points other than symlinks and junctions under `modules/`, such as an App Execution Alias.
  Git writes none there.

### Edges

- **consumes-from** `TOOL-dSafePassage-47` — the walk, S2's config read and its refusal, AC2 and AC4, which S4, S5, S6, S7 and S12 order, word, bound and cite; without the walk there is nothing to sequence
- **consumes-from** `TOOL-dSafePassage-48` — the `sendemail.sendmailCmd` row, the smtpServer pin and AC3, which S9's staged copy, S13 and S12 read
- **consumes-from** `TOOL-dSafePassage-49` — F1(a)'s sweep and AC2, S6's Readers, S7's rev-parse refusal, S8's arm, S13's form, S18's file test, §4's section probe and §10, which S1 to S5 and S8 to S15 read and amend
- **hands-off** `TOOL-dSafePassage-53` — S6's listing handler split by class, `except FileNotFoundError: return` before `except OSError: refuse d`, so an absent `modules/` is the empty population, with the `submodule-modules-not-a-directory` plant, finding 22 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-54` — the walk's sound baseline, a `submodule-sound-no-nested` plant built by `git submodule add` and the walk over gov's own tree, each exiting 0, finding 7 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-55` — S1's hand-out refusal widened to TOOL-dSafePassage-49 AC2's four relations, run as that unit's one order probe, finding 1 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-56` — S6's link test run by `test_path_linked` at the top of `walk(d)`, so the root and every `c/modules` are tested before they are listed, finding 8 of the spec audit of units 51 and 52
- **hands-off** `TOOL-dSafePassage-59` — AC1 and AC2 recorded as the sweep's checks, the dispatch edge refusal cited, AC1's grep made whole-line by `-x`, S3's one-line phrase, the link test without `os.path.isjunction`, a root-link and a dangling-link plant, S15's `lstat` link refusal, S9's census at the build HEAD and the tilde fence, findings 2, 13, 16, 29, 18, 23, 24, 12, 4, 17, 5 and 19 of the spec audit of units 51 and 52

## 4. Design

### The walk, in sequence

TOOL-dSafePassage-47 §4 "The walk" with TOOL-dSafePassage-49 S7 and S6 here, in the order S4 fixes:

```
walk(d):                                          # d starts at <git_dir>/modules/
  try: entries = subdirectories of d              # never following a link
  except OSError: refuse d                        # S6
  for c in entries:
    if islink(c) or isjunction(c): refuse c       # S6, before any shape test
    if isfile(c/HEAD) and isdir(c/objects) and isdir(c/refs):        # TOOL-47 S1
      rc = git --git-dir=c config --list --show-scope --show-origin --includes -z
      if rc != 0: refuse "<c>/config or a file it includes", rc      # TOOL-47 S2, S7 here
      rc = git --git-dir=c rev-parse --git-dir                       # TOOL-49 S7, S4 here
      if rc != 0: refuse c, rc
      list c; walk(c/modules)                                        # TOOL-47 S3
    else:
      walk(c)                                     # a name segment
```

| Plant | Config read | `rev-parse` | Refusal names |
|---|---|---|---|
| `submodule-config-malformed` | exit 128 | not run | `.git/modules/<name>/config` |
| `submodule-format-unknown` | exit 0, a warning | exit 128 | `.git/modules/<name>` |
| `submodule-modules-link-loop` | not run | not run | `.git/modules/a/loop` |

This unit's probe on node d, Python 3.14.5, 2026-10-23, made a junction `modules/a/loop -> modules`
under the scratchpad with `mklink /J`. `os.path.islink` read False, `os.path.isjunction` read True and
`os.path.isdir` read True. So a test of `islink` alone follows the junction, and S6 tests both.

### The section probe

```
awk '/^```/{c=!c} !c&&/^#+ What a step can reach/{l=index($0," ");f=1;next} !c&&f&&/^#+ /&&index($0," ")<=l{f=0} f' help/upgrade-steps.md
```

`l` is the opening heading's level, the column of its first space. A heading inside a fence never
opens or closes the section. This unit ran it on node d, 2026-10-23, over a scratch page holding the
section, a `###` subheading inside it, a fenced block holding `# a shell comment`, and a following
`##` heading. It printed the section through the subheading and the fence, and stopped at the `##`
heading. The awk line TOOL-dSafePassage-47 AC4 typed printed only the first paragraph of the same page.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the `isolation` plants `submodule-modules-link-loop` and
`gitmodules-fifo`. In `tools/govkit/selftest.py`: the literal set of expected unlisted executor keys.
No function, constant, conf key, gate leg or policy key. The refusals of S6 and S15 are
TOOL-dSafePassage-24's one `raise Refusal` site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN`
does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 14, after every unit of the build. Its write set is
`tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and `help/upgrade-steps.md`. That set does
not meet `TOOL-dSafePassage-52`'s, and the two run at different orders anyway. S1's hand-out step and
S2's and S3's Rollout sentences are not in this write set: TOOL-dSafePassage-49 F1(a)'s sweep writes
them before the roster is handed out.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Printing git's stderr beside the refusal (S7).** The report's second option. The refusal line
  would carry text whose shape gov does not control. TOOL-dSafePassage-38's guarantee that no refusal
  line prints a credential would then rest on TOOL-dSafePassage-45 S9's free-text pattern, which
  TOOL-dSafePassage-49 S19 shows misses a password holding a space.
- **Scoping TOOL-dSafePassage-49 AC5's count to non-fixture functions (S10).** The report's first
  option. The module names no fixture boundary an `ast` walk can read, so the count's scope could not
  be stated exactly. One form keeps AC5's count of exactly one.
- **Testing `os.path.islink` alone (S6).** It reads False on a Windows junction, measured above.
- **Opening `.gitmodules` and catching the error (S15).** An open of a FIFO blocks until a writer
  appears, so the error never comes.
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: S6 stops the walk leaving the target's `.git/modules/` through a link; S9 keeps the
  guard's expected keys out of the module it guards; S15 stops a FIFO `.gitmodules` hanging the step.
- perf / scale: one `lstat` per directory under `modules/` (S6) and one per `.gitmodules` (S15); S4
  runs `rev-parse` only on a candidate whose read exited 0.
- error / empty / loading states: a link, an unlistable directory, a non-regular `.gitmodules` and a
  failed read are each a refusal naming the path, never a traceback or a hang.
- observability: each refusal names its path; S7's names a config "or a file it includes" and the
  exit code.
- risks: S1's hand-out refusal stops a build run whose sweep missed S4's move, before any pass runs.
- testing: the probes and plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, the section S12's probe reads, which names S6's link refusal and
  S7's wording.

## 6. Acceptance criteria

- **AC1** — When `git log --reverse --format='%(trailers:key=Pass,valueonly)' <BASE>..HEAD` runs,
  `<BASE>` being the build run's pinned base in `memory/builds/dSafePassage/RUN.md`, the first line
  reading `TOOL-dSafePassage-4` comes after the first lines reading `TOOL-dSafePassage-43` and
  `TOOL-dSafePassage-7`. The first lines reading `TOOL-dSafePassage-18` and `TOOL-dSafePassage-19`
  come after it.
  Red when: TOOL-dSafePassage-4's pass ran before a unit it consumes from, whatever its header reads
  now.
- **AC2** — When `git grep -n -e 'also at order 2' -e 'then TOOL-dSafePassage-4:' -e 'TOOL-dSafePassage-4, the three sharing'`
  runs over the TOOL-dSafePassage-2, TOOL-dSafePassage-7 and TOOL-dSafePassage-43 specs, it prints
  nothing. `git grep -c 'TOOL-dSafePassage-4 builds at order 3'` prints at least `1` for each of the
  three.
  Red when: a sibling Rollout still places TOOL-dSafePassage-4 at order 2.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-config-malformed`
  runs, the step is refused before any spawn, the refusal names `.git/modules/<name>/config` and holds
  `or a file it includes` and the exit code, and the run exits 1.
  Red when: `rev-parse` runs before the config read, so the refusal names the git directory alone.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-modules-link-loop`
  runs, the step is refused naming `.git/modules/a/loop`, the output holds no `Traceback`, and the run
  exits 1 within 60 seconds.
  Red when: the walk follows the link, so it ends in an uncaught `OSError` or walks the loop.
- **AC5** — When the self-test's staged copy of `tools/govkit/upgrade_steps.py`, whose move 3 keeps a
  `rolled-back` row `rolled-back` with the `down interrupted:` failure, runs
  `fixture rollback --plant rolled-back-witness-holds`, it raises `Refusal` naming the step and exits
  non-zero. The same plant over the module as built exits 0, as TOOL-dSafePassage-49 AC3 states.
  Red when: the plant exits 0 over the copy, so it never reached move 3.
- **AC6** — When `git grep -n UNLISTED_EXECUTOR_KEYS -- tools/govkit/upgrade_steps.py` runs, it prints
  nothing. `git grep -n 'sendemail.sendmailCmd' -- tools/govkit/selftest.py` prints a line within
  three lines of one citing `:394`. A `python -c` probe applying TOOL-dSafePassage-49 §4 "The arm's
  widening", its `kept` taken as TOOL-dSafePassage-29 S3's kept keys plus that literal, names
  `sendemail.sendmailcmd` over a module copy whose `STEP_REFUSED_KEYS` lacks that one row.
  Red when: the key the arm enforces is read from the module it guards, or the row can go and the
  probe stays green.
- **AC7** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, its fixture
  functions included, it finds exactly one call of `startswith` whose argument is
  `DOWN_STOP_PREFIXES`, and that call is inside `test_step_row`.
  Red when: fixture code compares a stop text with its own `startswith`.
- **AC8** — When §4 "The section probe" runs over a scratch page holding a `###` subheading and a
  fenced `# ` line inside the section, its output holds the lines after both and none after the next
  `##` heading. Over `help/upgrade-steps.md` its output holds the lines TOOL-dSafePassage-47 AC4,
  TOOL-dSafePassage-48 AC3 and TOOL-dSafePassage-49 AC12 assert.
  Red when: the probe ends the section at a deeper heading or at a `# ` line inside a fence.
- **AC9** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, the function
  that reads `<worktree>/.gitmodules` calls `os.lstat` and `os.stat` on lines before the one that
  spawns its `config -f` read and before any `open`. When
  `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant gitmodules-fifo` runs on a POSIX
  host, the step is refused naming the `.gitmodules` path and the run exits 1 within 60 seconds. On a
  host without `os.mkfifo` it prints a `skip —` line naming the plant and exits 0.
  Red when: the read opens or spawns on the path before its type test, so a FIFO hangs the run.
  fixture: the FIFO half needs a POSIX host. Node d is Windows, and so is every job of
  `.github/workflows/remote-ci.yml` (`runs-on: windows-latest`), so this repo observes the `ast` half
  and the `skip —` line only.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 AC5 AC6 AC9 · the self-test runs the walk's three plants of §4, `rolled-back-witness-holds` and `gitmodules-fifo`, and the widened class arm against the selftest literal; its failing cases are staged by a walk copy running `rev-parse` before the config read, a walk copy that follows links, a reverse-walk copy whose move 3 keeps `rolled-back` with a failure, a module copy whose `STEP_REFUSED_KEYS` lacks the `sendemail.sendmailCmd` row, and a `.gitmodules` read copy that spawns its `config -f` read before its `stat`, which AC9's `ast` half names and under which, on POSIX only, the FIFO plant runs to its bound · none

What the check does not cover: the commit order of AC1 before this unit's own pass, which only S1's
hand-out step guards; a reparse point that is neither a symlink nor a junction; and the FIFO plant's
refusal on any host this repo runs, all of them Windows, where only its `skip —` line is seen.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 47 to 50's 6 MEDIUM and 9
  LOW findings on the step module, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions `TOOL-dSafePassage-53`, `TOOL-dSafePassage-54`, `TOOL-dSafePassage-55`, `TOOL-dSafePassage-56` and `TOOL-dSafePassage-59` of the spec audit of units 51 and 52, written by the disposal stage; no other section moved.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-47's walk and config read,
TOOL-dSafePassage-49's arm, row rule, `.gitmodules` test and section probe, TOOL-dSafePassage-24's
refusal site, and TOOL-dSafePassage-49 F1(a)'s sweep, all specced and unbuilt at the base. For the
behaviours TOOL-dSafePassage-49 mints, S14's lookups ran on node d, 2026-10-23:
`python tools/codebase-map/reuse_lookup.py "refuse a record field that is not a non-empty string"`
ranked `note`, `records`, `field`, `CensusRefused` and `ScopeRefused`, name-token matches, none a
row-field predicate. `"redact a password from a url userinfo before printing"` ranked
`render_redacted` in `tools/runlog/runlog_lib.py`, which TOOL-dSafePassage-38 §4 already rejects for
config text. `"refuse a path that exists and is not a regular file before opening it"` ranked
`before`, `note`, `opened` and the census refusals, none a file-type test. `"widen a config key to
its subsection identity form"` ranked `key`, `keys` and `read_conf_key`, none reading git config. For
this unit's own S6, `"walk a directory tree without following symlinks or junctions"` ranked `tree`,
`walk` in `tools/memory-tree/corpus_ids.py`, which walks `git ls-files` output and not the
filesystem, and `load_map_tree`. A grep of `tools/` for `isjunction`, `followlinks` and `islink`
found only `check_app_alias` in `tools/run-gates/measure_legs.py`, which tests an App Execution Alias
and not a directory link. So no existing seam fits beyond those specs.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted units' passes" --terms "spec audit minors batched reading hands-off walk link junction refusal order section probe"`
