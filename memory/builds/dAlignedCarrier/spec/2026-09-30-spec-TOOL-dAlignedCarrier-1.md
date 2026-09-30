# TOOL-dAlignedCarrier-1 — the driver stops saying no verb commits, and the kit gate reads the whole kit for it

**Status:** SPECCED · rev-1 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · closes TOOL-dDerivedDocket-74 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |

<!-- /gen:spec-records -->

## 1. Goal

A comment in `tools/unattended/unattended.sh` still states the premise that no driver verb commits,
though `--close` commits its own record under in-place landing. The premise was taken out of three
carriers once, by fixed-string greps that could not see a new instance, and one came back in a
different case the next day. This unit corrects the comment and makes the kit gate read every
shipped file of the kit for the premise as a class, case-insensitively and across a line wrap.

## 2. Scope (IN)

- **S1** — The last paragraph of the auto-file header above `read_leg_argv`
  (`tools/unattended/unattended.sh:6750` at BASE, the four lines opening `STAGED, NEVER COMMITTED`)
  is rewritten. It says the rows are STAGED by this item, and that `--close` commits them in its own
  records commit under `LANDER_MODE=in-place`, that under `primary` they ride the records commit the
  close names as owed, and that on a path printing a `hold ·` line the Skill's Close sequence commits
  them before `--hold`. The `ASKS_CMD` sentence is kept. No code line moves. Observed by AC1.
- **S2** — `tools/unattended/check-unattended.sh` gains check 47, the class scan. Its header is
  spelled `# ---- check 47 - ` so the `--only 28` announcer derives it, and it sits after check 43,
  inside the region that guard skips. Its population, normalisation, predicate and failure are §4's
  "The scan". Observed by AC2, AC5.
- **S3** — Check 47's header states what it does NOT check, in the words §4 gives. Observed by AC3.
- **S4** — `tools/unattended/check-unattended.test.sh` gains an arm for each new `fail 47` branch: a
  kit file copy carrying the premise, ASSEMBLED FROM FRAGMENTS so the suite's own bytes never spell it,
  asserting the check 47 text; and a near-miss arm asserting silence over the phrase that spells no
  commit. The arms are written; their RUN is not observed, because the owner waived the kit's own
  suites for this landing (the build README's rule). Observed by AC4.
- **S5** — The edit to `tools/unattended/check-unattended.sh` is made in BYTES: that file carries raw
  CR bytes on purpose, so it is read and written binary-safe, never through a text-mode rewrite.
  Observed by AC6.

## 3. Non-goals (OUT)

- The `memory/DECISIONS.md` row stating the premise. It is an append-only record, not a kit file,
  and its supersession row already exists under the id of the unit that overturned the premise.
- The rendered carriers outside the kit directory. Each is a copy of a template inside it, which the
  scan reads, and the parity legs already fail a render that differs from its template.
- A repo-wide scan. The population is this kit's shipped files, which is what the ask names.
- Any spelling of the premise outside the predicate. The predicate is a closed pair of patterns, and
  its header says so.
- Raising the check-unattended pair in `ARMS_FLOORS`. A floor is a minimum, so a new armed branch
  lowers nothing, and `.memory-tree.conf` is a watched file whose edit owes a manifest re-stamp.
- The kit version. The orchestrator moves it once, at VERIFYING, for every kit this build touched.

### Edges

Files shared with a sibling, which are not edges: `tools/unattended/unattended.sh` is also written by
units 3, 4 and 6, and this unit touches only the auto-file header paragraph above `read_leg_argv`.
`tools/unattended/check-unattended.test.sh` is also written by unit 3, which re-aims the scope-join
arm; this unit appends one new arm region after the suite's last arm and edits no existing line.
Check 47 reads every file the siblings write, so a sibling that spelled the premise would red it, and
that is the guard working rather than a dependency.

none

## 4. Design

### Evidence

Measured at `87c245b3` on 2026-09-30, PINNED. A case-insensitive scan of every tracked file under
`tools/unattended/`, lines joined after their comment markers are stripped, finds ONE instance, at
`tools/unattended/unattended.sh:6750`. Its nearest miss is `check-brief-recorded.test.sh:177`, which
reads "which no driver verb does" and spells no commit, so the predicate below must stay silent on
it. `tr -cd '\r' < tools/unattended/check-unattended.sh | wc -c` reads 4. The earlier greps were
case-sensitive and read three named files; the live instance is lowercase and sits in a fourth
place, which is why this is a class check.

`--close` commits `records(<slug>): close — LANDING` through `write_close_commit`, under in-place
landing only, and the superseding decision row says so.

### The scan

- **Population.** Every path `GIT ls-files -- "$KITREL"` lists, where `KITREL` is the kit directory
  this gate already derives, so an adopter's install prefix is honoured and nothing is spelled by
  literal. This checker and `check-unattended.test.sh` are left out BY BASENAME, the precedent check
  33 set: the checker's header must describe the premise to say what it checks, and the suite stages
  it. The suite also assembles its staged line from fragments, so the exclusion is a second guard.
- **Normalisation, per file.** CR bytes stripped; on each line, leading whitespace and ONE leading
  comment marker (`#`, `//`, `*` or `<!--`) stripped; the lines joined by one space, runs of
  whitespace squeezed, the whole folded to lower case with POSIX `tolower`. A wrap inside a comment or
  a paragraph therefore reads as one sentence.
- **Predicate**, two alternatives, word-bounded: `no`, at most two words, `verb`, at most two words,
  then `commits`; or `nothing commits it`. Written in the checker with optional groups, so its own
  source never spells an instance even before the exclusion applies.
- **Failure.** One `fail 47` naming every file that matched and the matched text. The message
  describes the premise without spelling it, so the arm that asserts the message stays clean too.
- **Header, the does-NOT-check paragraph.** A spelling outside the two alternatives passes. A file
  outside the kit directory is not read. The two excluded files are not read. A match inside a
  string literal counts like one in prose, because the premise misleads a reader either way.

### Inventory

No function is minted. The block's variables carry the `_c47_` prefix, the gate's per-check idiom.

### Rollout

`tools/unattended/check-unattended.sh` carries raw CR bytes on purpose, so the new check is inserted
in BYTES: read and written binary-safe, for instance by a Python script opening the file in `rb` and
`wb`, never by a text-mode rewrite or an editor that normalises line endings. AC6 is the observation.
The comment edit in the driver and the suite arm are ordinary text edits. No render is involved.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- Three fixed strings, case-sensitive, over named files. That is the shape that missed the live
  instance.
- Scanning `*.sh` only. The premise once lived in a markdown template.
- Reading the checker and its suite, relying on fragment assembly alone. The checker's header has
  to name what it guards, and a header that could not describe its own predicate is worse.

## 5. Production-readiness checklist

- security — N/A: a read-only scan over tracked files; no write, no network.
- perf / scale — one `ls-files` and one awk pass per file over roughly fifty files; seconds on a leg
  measured at 593 s whole on node d on 2026-09-30.
- error / empty / loading states — an empty population is not reachable, since the driver itself is
  in it; a file `ls-files` lists and the worktree lacks is skipped, as the gate's other scans do.
- observability — the failure names each file and the matched words.
- risks — a future legitimate sentence matching `nothing commits it`; the remedy is rewording, and
  the header names the predicate so the author can see why.
- testing — the staged-break observation below; the suite arm, written and not run.
- migration — none.
- user docs — none: the check's own header is its documentation.

## 6. Acceptance criteria

- **AC1** — When `grep -n -i -E 'no (driver )?verb (here )?commits' tools/unattended/unattended.sh`
  runs after the pass, it prints nothing; at BASE it prints line 6750. And
  `grep -n -B6 '^read_leg_argv()' tools/unattended/unattended.sh` shows a comment naming `--close` and
  in-place landing as what commits the rows.
  Red when: the comment still states the premise in any case, or names no verb that commits.
- **AC2** — When three instances are staged at once in three kit files, each spelled differently —
  one lowercase line appended to `tools/unattended/lib-unattended.sh`, one uppercase phrase wrapped
  across two lines of `tools/unattended/README.md`, and `nothing commits` / `it` wrapped across two
  `#` comment lines of `tools/unattended/kit.toml` — then `bash tools/unattended/check-unattended.sh`,
  the argv of the `unattended kit gate` leg in `tools/gate-legs.json`, exits 1 with
  `UNATTENDED check 47 FAILED`, naming exactly those three files and not the brief-record suite whose
  line 177 is the nearest miss. When the three files are restored from byte-identical backups and it
  runs again, it exits 0 with no `FAILED` line.
  Red when: any of the three spellings passes, the near-miss is named, or the restored tree reds.
  cost: two runs of the kit gate, 593 s each on node d on 2026-09-30 (PINNED).
  fixture: the tree itself; the backups go under the run's scratchpad and are restored before commit.
- **AC3** — When `awk '/^# ---- check 47 /,/^[^#]/' tools/unattended/check-unattended.sh` runs, its
  output holds the header paragraph naming what the check does not read, and a `grep -c 'NOT check'`
  over that output prints 1.
  Red when: the header states the predicate and not its limits.
- **AC4** — When `python tools/memory-tree/check-arms.py --report` runs, every check 47 branch of
  `tools/unattended/check-unattended.sh` reads ARMED by the sibling suite, and
  `grep -c -i -E 'no (driver )?verb (here )?commits|nothing commits it' tools/unattended/check-unattended.test.sh`
  prints 0.
  Red when: a branch reads UNARMED, or the suite spells the premise contiguously.
  permission: running the suite itself is waived for this landing by the build README's rule.
- **AC5** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh --only 28` runs, it
  prints `check 47 skipped under --only 28`.
  Red when: the header is spelled so the announcer cannot derive it, and the skip is silent.
  cost: the 28 region plus the gate's setup, UNVERIFIED on this node.
- **AC6** — When `tr -cd '\r' < tools/unattended/check-unattended.sh | wc -c` runs after the pass, it
  prints the BASE count, 4 (PINNED 2026-09-30), and
  `git diff --numstat -- tools/unattended/check-unattended.sh` reports 0 deleted lines.
  Red when: a text-mode rewrite changed a CR byte or touched a line outside the new check.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)`

New arm: `tools/unattended/check-unattended.test.sh` · a kit file copy carrying the premise assembled from fragments reds check 47, and the no-commit near-miss stays silent · none (the floor is a minimum)

## 8. Open questions

- **F1 — Which spellings does the scan read?** (a) The three fixed phrases the earlier greps named.
  (b) The two-alternative family in §4, which admits up to two words on each side of `verb` and
  covers the three phrases and their near variants. (c) Any sentence carrying `commit` near a
  negation. (c) is a prose classifier and would red honest sentences; (a) is the instance shape the
  ask exists to replace. Recommendation (b). RESOLVED (agent, 2026-09-30, delegated): (b), the most
  spellings covered with no hit on the BASE tree beyond the one live instance and silence on its
  nearest miss.
- **F2 — Does the population include the checker and its suite?** (a) Exclude both by name, as check
  33 does, and assemble the suite's staged line from fragments as well. (b) Include both and rely on
  fragment assembly and optional-group spelling alone. (b) forbids the checker's header from naming
  what it guards. Recommendation (a). RESOLVED (agent, 2026-09-30, delegated): (a), reusing the
  seam check 33 established.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, from the ask's accept clause and the build's spec brief.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scan the kit's shipped files for a retired phrase,
case-insensitive"` ranked name-stem neighbours only (`kit_rel`, `scan_processes`, `corpus_files`) and
reported `.sh` as an unscanned layer, so it cannot see this gate. The seam was found by reading the
gate: check 33 in `tools/unattended/check-unattended.sh` is a class scan over the kit's own files that
excludes the checker and its suite by name and whose arm assembles the banned bytes from fragments.
Check 47 reuses that shape and widens its population from `*.sh` to every tracked file under
`KITREL`, the kit-relative path the gate already derives.

Recall terms used: `check-unattended class scan retired premise no driver verb commits case-insensitive
shipped kit files fragments staged instance`.
