# TOOL-dDerivedDocket-18 — leg second opinions over the ask mandate

**Status:** SPECCED · rev-5 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |
| [2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 16 makes the driver pin an ask mandate at preflight and unit 17 grades it at close, but both
answers are written into a run-state file by the run being graded. Give the unattended leg its own
reading of each mandate fact, re-derived from inputs the run cannot move, so that a forged,
mistaken or stale fact reds the bar instead of certifying itself. This is the pattern check 19
already applies to `authorized-by:`, `playbook:` and `pieces:`
(`tools/unattended/check-unattended.sh:1424-1455`), extended to the four facts the ask path adds.
`asks-ready:` and the freeze's content are re-derived by re-running the declared producer on frozen
inputs before the record is published, and announced as not re-derived after (S8).

## 2. Scope (IN)

- **S1** The `asks:` fact against the build README. The leg re-parses the `asks:` front-matter line
  from the README blob at the recorded BASE, the blob check 19 already reads, and requires it
  byte-equal to the recorded fact. For a record in a working phase or HELD, it also requires the
  README at HEAD to carry the same bytes, which is property P6 seen from the leg. A record at LANDING
  or at a terminal phase is past its close, and nothing re-reads its README's `asks:` line.
  Observed by AC1 and AC2.
- **S2** P5 re-derived. For every mandated id the leg requires the ask row `- <id> · filed ` in the
  home build's `BACKLOG.md` at the recorded `m-base:`, and it checks `m-base:` itself against the
  pinned `anchor-sha:`, never against `base:` (fix F4). Observed by AC3 and AC4.
- **S3** The folder-wide anchor ban. For a record carrying an `asks:` fact, no tracked file under
  that build's folder may carry a line that anchors an id whose slug is not this build's, judged by
  the memory-recall kit's own `anchor_at`, never by a copy of its shapes. Observed by AC5 and AC6.
- **S4** The freeze is present. Every record whose phase is LANDED and that carries an `asks:` fact
  carries an `asks-at-landing:` fact naming every mandated id. Observed by AC7 and AC13.
- **S5** One authorization path (owner ruling D12-a). A record carrying an `asks:` fact must record
  mode `slug`, and no record may carry one while the conf's `ASKS_CMD` is blank. Its driver twin is
  unit 16 S2's preflight refusal, so a record reaching this arm was written around the driver.
  Observed by AC8.
- **S6** Every arm is vacuous without an `asks:` fact and says so on one line, with the count of
  mandated records it examined. Observed by AC9.
- **S7** Every new `fail` branch gets an arm in `tools/unattended/check-unattended.test.sh`, and
  `ARMS_FLOORS` moves in the same commit. Observed by AC10.
- **S8** The pins re-derived before publication. For every mandated record whose preflight commit
  (the commit that first recorded `m-base:`, as S2 finds it) is not reachable from the default
  branch's advertised tip, the leg re-runs unit 16's call shape 1 at the recorded `m-base:` and
  requires its `<id>=<grade>` pairs to equal `asks-ready:`. For every such record carrying
  `asks-at-landing:`, it re-runs call shape 2 over M ∪ F — F enumerated at that commit by the shared
  P5 line matcher — at the FIRST PARENT of the commit that introduced the `asks-at-landing:` line,
  which is the tree `--landed` (primary) or `--close` (in-place) examined, and requires the
  `<id>=<STATUS>` pairs to equal the fact. Both calls run through the conf's `ASKS_CMD`, bounded; a
  breach is never answered, not a red. A record already reachable from the advertised tip is counted
  and announced as published and not re-derived; with the tip unobserved, every mandated record is
  re-derived and the reason printed. Where the introducing commit cannot be found, S2's announced
  fallback applies and this arm skips by name. Observed by AC11 and AC12.

## 3. Non-goals (OUT)

- Pinning any fact. The driver's preflight pins `asks:`, `asks-ready:` and `m-base:` (unit 16) and
  `--landed` writes `asks-at-landing:` (unit 17). This unit only reads.
- Implementing READY or any ask status. That is the fold's (unit 6), printed by unit 15's
  `--asks --tsv`; the leg re-runs the declared producer on frozen inputs (S8) and compares, and holds
  no second implementation.
- Check 13's claimant rule across the whole corpus is the memory-tree engine's, refined by D12-g in
  unit 8 (`TOOL-dDerivedDocket-8` S6). S3 is narrower: it covers the run's own folder for every foreign id, legacy ones included,
  which is where the 27 hazard ids came from (DR §19.1 K9, measured at `abac6d59`; re-measured at
  `fb07ca25` the set is 28 of 658 distinct legacy ids, its one addition TOOL-aKeyedAnnotation-9,
  anchored at `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md:124` — the
  ratified design record stays at its own figure).
- Moving the freeze to `--close` under in-place (unit 22) changes which records S4 grades. Unit 22
  extends S4's population to a committed LANDING record under `LANDER_MODE=in-place` in the same
  commit that moves the freeze. This unit grades recorded LANDED, which includes a record unit 22's
  rotation retires.
- The real-tree staged RED of S3 on a typed resolution table is unit 35's.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — the pinned `asks:`, `m-base:` and `anchor-sha:`
  facts, `ASKS_CMD`, and the ask-row line matcher the driver's P5 uses, and call shapes 1 and 2 that
  S8 re-runs, over inputs the record pins. Without them S1, S2 and S5 have nothing to compare.
- **consumes-from** `TOOL-dDerivedDocket-17` — the `asks-at-landing:` fact S4 requires on a landed
  record, and the freeze's content S8 re-derives.
- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute <BASE>`, whose
  attributed verdict, `verdict clean` with every inherited suite filed, is the only criterion the
  unattended suites, red at BASE (TOOL-aHoistedPass-36), can meet.
- **consumes-from** `TOOL-dDerivedDocket-48` — the witness capture that keeps the producer's stderr
  off the row stream, which S8's two re-runs route through as the driver does. The G3 round-2
  record's B1 measured that `run_bounded` merges both streams; S8 keeps its current text and takes
  that unit's answer.
- **consumes-from** `TOOL-dDerivedDocket-52` — how the commit that introduced a pinned line is found
  across a rotation rename. The same record's H4 measured that rotation renames inside the folder,
  so §4's announced ancestry fallback never fires where it says it does; §4's S2 paragraph and S8
  keep their current text.
- **consumes-from** `TOOL-dDerivedDocket-53` — which tree supplies the conf under `--at`. The same
  record's H5 measured that `ASK_CUTOFF` and `BACKLOG_MODE` stay evaluation-time values, so §8 F3's
  pure-function premise does not hold; that unit decides it and S8's equality rule takes the answer.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of S3, a typed resolution table
  in a mandated run's folder, after gov sets `ASKS_CMD`.
- **hands-off** `TOOL-dDerivedDocket-20` — the folder-wide anchor ban, whose carrier sentence
  protocol §2 states.
- **hands-off** `TOOL-dDerivedDocket-22` — S4's freeze-presence arm, whose population that unit
  extends in the commit that moves the freeze.

## 4. Design

### Which inputs each arm trusts

| Arm | Reads | Never reads |
|---|---|---|
| S1 | the README blob at the recorded BASE, and at HEAD for a record in a working phase or HELD | the driver's own parse |
| S2 | the pinned `anchor-sha:`; the commit that first recorded `m-base:`; the home `BACKLOG.md` blob at `m-base:` | `base:`, and any working-tree file |
| S3 | tracked files under the run's build folder; the recall kit's `anchor_at` | a local list of anchor shapes |
| S4 | the record's own facts | the witness, which may have moved since landing |
| S5 | the record's `mode:` and the conf's `ASKS_CMD` | anything the Skill printed |
| S8 | the conf's `ASKS_CMD`; the recorded `m-base:`, `asks:` and folder slug; the commit that introduced the freeze; the advertised tip | the witness output the run recorded, and HEAD's tree for the freeze |

S8's two calls run through the conf's `ASKS_CMD` bounded, exactly as the driver's do, and what that
capture hands the parse is not settled in this spec. At `fb07ca25` `run_bounded` redirects both
streams into one file and reads it back (`tools/unattended/unattended.sh:191-196`), so a healthy
producer's stderr notices arrive inside the rows, and the G3 round-2 record's B1 promoted that to
`TOOL-dDerivedDocket-48`. S8 keeps its current text and takes that unit's answer.

### S2, the m-base re-derivation

`m-base:` is merge-base(`anchor-sha:`, HEAD at preflight), both frozen commits, so equality is safe
here in a way it is not for check 9. Check 9 had to move to ancestry because a merge-base computed
NOW moves after landing (`tools/unattended/check-unattended.sh:1239-1245`); a merge-base of two
frozen commits never moves. HEAD at preflight is the first parent of the earliest commit whose copy
of the record carries the `m-base:` line, because preflight refuses a dirty tree and stages the
record, so the next commit carries it.

Where that commit cannot be found, as in a rotated record whose path changed, or a shallow clone,
the arm falls back to two ancestry tests: `m-base:` is an ancestor of `anchor-sha:` and of the
record's HEAD. It announces the weaker reading by name, so a green row is never read as the
equality test.

The ROTATED case above is not settled in this spec, and the sentence stating it is kept only until
the unit that owns it lands. At `fb07ca25` rotation is a rename inside the SAME folder:
`archive_name_of` builds the archived name from the record's own directory
(`tools/unattended/unattended.sh:1692-1698`) and the move is a staged `git mv`
(`tools/unattended/unattended.sh:2748`). The rotated path therefore exists and its blob carries
`m-base:`, so a path-scoped search for the earliest commit whose copy carries that line answers with
the ROTATION commit rather than the preflight one, and the fallback this paragraph announces for it
never fires. The G3 round-2 record's H4 promoted that to `TOOL-dDerivedDocket-52`, which says how the
rename is followed and splits AC4's assumed case into a rotated-record arm graded against the
RECORDED `m-base:` and a genuinely unfindable one. S2, S8 and AC4 keep their current text and take
that answer; S8's freeze half, whose first-parent tree rests on the same search, inherits it.

The ask-row match itself is the SAME line matcher the driver's P5 calls, shared
through the kit library: the second opinion's independence lies in its inputs, never in a second
grammar, which would be a second implementation and not a second opinion.

### S3, the anchor ban

The extractor is reached through the declared `RECALL_CLI`, whose directory holds the recall kit's
extractor. That keeps the kit file from naming a sibling kit by literal, which the install-prefix
gate bans. A blank `RECALL_CLI`, or an extractor that does not import, SKIPS S3 with a line saying
which, never a pass. The arm runs one interpreter per folder, feeding every line of every tracked
file under it, and collects `(file, line, id)` for each anchor whose slug is not the folder's. The
interpreter is resolved by an inline `resolve_python` block, byte-identical to
`tools/lib/resolve-python.sh`, which the driver has carried since aDeferredBar
(`tools/unattended/unattended.sh:209`). The leg can source no shared library in an adopter, and the
python resolver leg's invocation-shape ban reds a bare launcher in any tracked `*.sh`. A resolver
that finds no usable launcher SKIPS S3 by name, as a blank `RECALL_CLI` does.

Why a foreign slug and not "an id whose ask row is filed elsewhere": both a foreign ask id and a
foreign unit id anchored in this folder make this build a second claimant under check 13, and the
narrower predicate would need the witness, which S3 deliberately does not read.

### Fail codes

S1, S2 and S5 are declaration second opinions and report under check 19, beside the arms they
extend. S4 is a terminal-record fact and reports under check 15. S8's `asks-ready:` half reports
under check 19, its freeze half under check 15. S3 is a new class and takes a new
leg code, allocated at build time as the next integer above the leg's highest, because other units
of this build allocate leg codes concurrently.

### Rollout

Dark by construction. No record carries an `asks:` fact until a run is pointed at asks after unit
35 arms gov, so every arm announces vacuity on every bar until then. The fixtures carry the
coverage in the meantime.

### Inventory

No new fact, conf key or verb. One leg code for S3, number allocated at build time. Any new shell
function is named through `python tools/lexicon/lexicon.py --suggest <identifier> --as <cell>`.

### Files touched (estimate)

`tools/unattended/check-unattended.sh`, whose conf import assigns only a key initialised above it
and listed between `gov:conf-allow-begin` and `gov:conf-allow-end`, so `RECALL_CLI` and `ASKS_CMD`
join both or the leg reads them blank whatever the conf declares ·
`tools/unattended/check-unattended.test.sh` ·
`tools/unattended/lib-unattended.sh`, only if unit 16's matcher is not already there ·
`.memory-tree.conf` for `ARMS_FLOORS` · `memory/map/features/unattended.md`.

### Alternatives rejected

- **A subset arm over the prompt record's IDLIST (fix F2 as first adopted).** Owner ruling D12-a
  makes every ask-driven run start from an owner-landed README, and an ids invocation writes nothing,
  so no run-written IDLIST exists to compare. F2's check becomes S1 plus S5; see §8 F1.
- **Reading anchors with a local regex copy.** Two copies of one grammar disagree silently, which is
  derive critique F13's own finding against the view's selftest (DR §5.3).
- **Ancestry-only for `m-base:`.** It passes a pin moved to any older common commit. Kept only as
  the announced fallback.

## 5. Production-readiness checklist

- security — every arm reads committed blobs or the record; the anchor extractor runs over tracked
  text and executes nothing it reads. S8 executes the conf-declared `ASKS_CMD` as the driver does,
  never ask text; `--at` reads committed trees.
- perf / scale — per mandated record, two `git show` calls for S1, one per mandated id for S2, and
  one interpreter per folder for S3. Zero mandated records today, so the leg's cost does not move.
  S8 runs at most two bounded producer calls per UNPUBLISHED mandated record, so its cost follows the
  runs in flight and does not grow with the archive.
- error / empty / loading states — no `asks:` fact is announced vacuity; an unreadable blob or an
  unresolvable `m-base:` is a named refusal; a missing extractor is a named skip.
- observability — one line per arm per mandated record, and one summary count line per run.
- risks — S2's equality depends on preflight staging the record before any other commit, which
  unit 16's preflight inherits from today's; the fallback covers the cases where it cannot be shown.
  A run whose own unit changes READY reds S8 on its own record, because the leg re-runs today's
  producer at `m-base:`; that difference is real, and the run parks it.
- testing — one fixture per arm in `tools/unattended/check-unattended.test.sh`, each observed RED;
  the unattended suites run at the build's one post-build bar, read through unit 1's
  `--attribute <BASE>`.
- migration — none; every existing record is vacuous.
- user docs — none beyond the leg's own header comments, which state what each arm does NOT check;
  the folder-wide ban's carrier sentence is unit 20's (S3).

## 6. Acceptance criteria

- **AC1** — When a fixture record's `asks:` fact differs by one id from the README line at its
  recorded BASE, `bash tools/unattended/check-unattended.sh` reds check 19 naming both values.
  Red when: the arm compares the fact against the driver's parse, or against the README at HEAD
  only, so a README edited after BASE agrees with a forged fact.
- **AC2** — When a live fixture record's README at HEAD carries an `asks:` line that differs from the
  one at BASE, check 19 reds. The same README on a LANDED record, and on a committed LANDING record in
  either lander mode, does not red.
  Red when: the HEAD half grades a record past its close, so the owner's follow-up `asks:` edit reds
  a landed record forever, and under in-place it does so through a record that never rotates.
- **AC3** — When a mandated id has no ask row in its home `BACKLOG.md` at the fixture's `m-base:`,
  check 19 reds naming the id and the blob it read.
  Red when: the arm reads the working tree, so a row filed after the run started satisfies it.
- **AC4** — When a fixture record's `base:` and `m-base:` are both replaced by the same older
  ancestor of `anchor-sha:`, check 19 reds naming `m-base:`; when the introducing commit cannot be
  found, the arm prints that it fell back to ancestry.
  Red when: the arm derives the merge-base from `base:`, so the forged pair agrees with itself, or
  the fallback runs silently.
- **AC5** — When a mandated fixture run's folder carries a table row whose first cell is a
  backticked foreign id, the new S3 check reds naming the file and line; a link-wrapped first cell
  does not red.
  Red when: the arm uses a local shape list that misses the backticked first cell `anchor_at`
  admits.
- **AC6** — When `RECALL_CLI` is blank in the fixture conf, the S3 arm prints a skip line naming the
  key and the leg exits on its other arms' verdicts alone.
  Red when: a blank key reads as zero anchors found.
- **AC7** — When a LANDED fixture record carrying an `asks:` fact has no `asks-at-landing:` fact,
  check 15 reds; with the fact present it passes.
  Red when: the arm grades only records with no `asks:` fact, the population where it cannot fire.
- **AC8** — When a fixture record carries an `asks:` fact with mode `prompt`, when a second carries
  one with mode `recipe`, or when a THIRD in mode `slug` carries one while `ASKS_CMD` is blank,
  check 19 reds. The mode fixtures are the whole of `SECOND_ANCHOR_MODES`
  (`tools/unattended/unattended.sh:580`), and the arm count equals that set's size read from the
  constant rather than typed here; the blank-conf fixture records mode `slug` so that the refusal
  S5 declares for a blank conf is the only rule that can fire on it.
  Red when: any combination passes, so a run-authored mandate carries a pinned ask set; or the
  refusal keys on `prompt` alone, so a `recipe` record — which resolves at the anchor the run can
  write, the same hazard — carries a pinned mandate ungraded; or the blank-conf arm is reached only
  through the mode refusal, so a `slug` record pinning a mandate with no declared producer passes.
- **AC9** — When the leg runs over today's tree, it prints one line stating that no record pins an
  `asks:` fact, with the count 0.
  Red when: the leg prints nothing, so vacuity reads as a pass.
  permission: unit passes run no gate legs (fix F7, and the unit child prompt since
  TOOL-aProbedUnit-1), so this run of the leg over the real tree is observed at the one post-build
  bar the main loop runs at VERIFYING, after the last unit. The pass's direct check is the leg run
  over a scratch fixture repository holding no record with an `asks:` fact, never a run of §7's arm
  file: that file is a self-test suite, which `tools/unattended/gate-guard.js` denies before
  VERIFYING, and the arm itself executes with the suite at that same post-build bar.
- **AC10** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs at the
  build's one post-build bar, its attribution summary reads `verdict clean`, meaning no NEW FAIL, no
  `DEAD PROBE at L` and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or
  `DEAD PROBE at R` is named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows. Every arm this
  unit added passes, each observed RED with its fix unstaged.
  Red when: an arm is wired without its failing case ever being seen; or the attributed run is read
  by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or pushed
  past its budget, reads as clean; or an inherited failure is attributed away with no record filing
  it.
  cost: one run of the unattended suites, the unit's single sanctioned suite run (D12-h).
  permission: the run drives the unattended self-test suites, which `memory/guides/BUILD-METHOD.md`
  M6 keeps out of a unit pass, so it is the run the main loop makes at VERIFYING, after the last
  unit. `tools/unattended/gate-guard.js` denies the same runner before VERIFYING, so the hook and
  the method agree. Which run covers it: `tools/gate-legs.json` carries NO leg for the unattended
  suites, so this is one of the attributed suite runs the main loop makes beside its bar, and no
  bar reaches it — not a plain one and not
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. In the pass each arm's RED is
  observed by hand against a scratch fixture. That folds the conservative reading of the D12-h
  conflict and does not decide it: S7, §5 and §10 keep the ruling's wording, and the run record
  parks it for the owner.
- **AC11** — When a fixture record's `asks-ready:` reads `EXMP-aFoo-3=yes` while the stub producer
  at the recorded `m-base:` grades that id `no`, and the record's preflight commit is not on the
  fixture remote's advertised tip, `bash tools/unattended/check-unattended.sh` reds check 19 naming
  both pairs; with the preflight commit on the advertised tip, the record is not re-run and is
  counted in one `published, not re-derived` line. Three further arms over the same fixture observe
  S8's other declared branches: with a stub `ASKS_CMD` that sleeps past the bound, the record is
  reported as never answered and the leg does not red on it; with a fixture remote advertising no
  tip, every mandated record is re-derived and the reason is printed on its own line; and with a
  record whose introducing commit cannot be found, the arm prints a `skipped` line naming itself and
  the leg exits on its other arms' verdicts.
  Red when: the arm compares `asks-ready:` against the record's own other facts, or re-runs the
  producer at HEAD, so a run that edited `yes` to `no` takes F3's laxer path unseen; or a bound
  breach is reported as a red, so a bar owner hunts a forged pin that does not exist; or an
  unobserved tip re-derives nothing, or re-derives with no reason printed; or the
  unfindable-commit branch passes without announcing its skip, so a green row is read as a verified
  one.
- **AC12** — When an unpublished fixture record's `asks-at-landing:` reads `EXMP-aFoo-3=CLOSED` while
  the stub producer, at the first parent of the commit that introduced that line, reports it OPEN,
  check 15 reds naming both; a REOPEN at HEAD does not red a published record.
  Red when: the freeze is re-derived at HEAD, so a later REOPEN reds a correct record for ever, or
  not re-derived at all, so a forged freeze passes S4.
- **AC13** — When a fixture record in S4's population carries an `asks-at-landing:` that omits one
  id of its `asks:`, check 15 reds naming the id.
  Red when: S4 checks the fact's presence only, so a freeze missing one mandated id passes and that
  ask's frozen answer is lost.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · one fixture record per arm S1 to S5 carrying the break, plus a vacuous fixture, a forged `asks-ready:` pair and a forged freeze, each unpublished, and one published record · the leg suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`

## 8. Open questions

- **F1 — what does fix F2's IDLIST arm check once D12-a drops the ids start?** F2 was adopted
  against E2, where the run wrote a prompt record holding the IDLIST. Under D12-a an ids invocation
  prints the recipe and writes nothing, the owner lands the scaffolded README, and the run starts as
  E1. The only record of the list is then the README's `asks:` line, which S1 already
  second-opinions. A provenance stamp written by the scaffold was considered and rejected: it would
  widen unit 15's output and create a second carrier of one list. RESOLVED (agent, 2026-09-14,
  delegated): F2's arm reduces to S1 plus S5.
- **F2 — may the leg reach the recall kit's extractor at all?** It must not name the kit by literal.
  RESOLVED (agent, 2026-09-14, delegated): through the declared `RECALL_CLI`, with a blank key an
  announced skip, which is the kit's existing adoption idiom for that key.
- **F3 — does the leg second-opinion `asks-ready:` and the freeze's content, and over which
  records?** Options: (i) re-derive both on every bar for every mandated record, re-running unit
  16's call shape 1 at the recorded `m-base:` and call shape 2 at the tree the freeze was computed
  at; (ii) state in the Goal, S4 and the leg header that both go unverified; (iii) (i) bounded to
  UNPUBLISHED records, those whose introducing commit is not yet reachable from the advertised
  default tip, with the published remainder announced by count. (i) costs one generator run per
  mandated record per bar for ever, against the charter's "cost is a verdict", and a later READY-rule
  change would red an archived record whose pin was right when written; (ii) leaves the "second
  signature, not a second opinion" of TOOL-aUnmannedHelm-6 standing. RESOLVED (agent, 2026-09-14,
  delegated): (iii), which catches a forged pin at every bar before it can land and never grades a
  published record against a later producer. It relies on unit 16 rev-2 passing no live-build set,
  which makes the READY call a pure function of pinned inputs.
  That premise does not hold for the CONF, and the resolution stands as written until the unit that
  owns it lands: `load_conf` reads `.memory-tree.conf` from the working-tree root whatever `--at`
  names (`tools/memory-tree/gen_build_index.py:286-291`), so `ASK_CUTOFF` and `BACKLOG_MODE` are
  evaluation-time inputs and a grade can move between the pin and this re-derivation while nothing
  was forged. The G3 round-2 record's H5 promoted that to `TOOL-dDerivedDocket-53`, which decides
  whether the conf is read at the pinned rev or the grade-bearing keys are named so S8 can skip BY
  NAME when they have moved; AC11 takes its arm from that unit and gains none here.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR §19.8 U13, fixes F2 and F4, and ruling D12-a. Adds one
  edge the brief's table does not carry: hands-off unit 35, which DR §19.8 U15 names as staging the
  leg's RED on a typed resolution table. The IDLIST arm of fix F2 is reduced under D12-a (§8 F1).
- rev-2 · 2026-09-14 · §1 §3 §4 §5 §7 §8 · S1 S4 S5 S8 · AC2 AC4 AC10 AC11 AC12 AC13 · spec audit
  round 1 folded. G3 M9: S8 re-derives `asks-ready:` and the freeze before publication (AC11, AC12;
  §8 F3), possible because unit 16 rev-2 passes no live-build set (G3 H4). G3 M22: AC4 forges `base:`
  and `m-base:` together. G3 L3: AC13 reds a freeze omitting a mandated id. G3 H6: S5 names its
  driver twin. G3 H9: `--attribute <BASE>`, consumes-from unit 1. G3 M4: hands-off unit 20. G3 H8 and
  G3's observation on in-place LANDING records: S1's HEAD half grades only records in a working
  phase or HELD, because a committed LANDING record is past its close (AC2); §3's fourth bullet
  states that the derived-terminal unit extends S4's population to a committed in-place LANDING
  record in the commit that moves the freeze, with a hands-off edge to that unit.
- rev-3 · 2026-09-16 · spec-audit round 2 fold. Plan c1 E39, G1 H1 (2, 24), a sibling fold from the
  G1 round-2 record, over §3 Edges and §6 AC10: AC10 reads unit 1's `verdict clean` (unit 1 S10) and
  the inherited-suite filing, its `Red when:` gains the NEW-count-alone reading, and the §3
  consumes-from edge to unit 1 names the attributed verdict in place of the NEW set. Fold
  verification then gave AC10's `Red when:` the rest of plan c1 §12's standard consumer text, the
  over-budget reading and the unfiled inherited failure, so it goes red on every half of unit 1
  S10's criterion, as the other consumers' criteria do.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). No S-item, criterion or fork moves.
  The check 19 and check 9 citations in §1, §4 and §10 are re-pointed, because `check-unattended.sh`
  grew through aDeferredBar (`1afd26c9`), aProbedUnit (`5493495a`) and aRatifiedRulings
  (`b6bbfa7b`); each cited block is byte-identical at its new line. §4's S3 paragraph resolves its
  interpreter through the inline `resolve_python` block the driver has carried since aDeferredBar's
  closing round 2, and §7 names the python resolver leg that grades that copy. AC9 gains a
  `permission:` line, because TOOL-aProbedUnit-1's child prompt now binds F7's no-gate rule in every
  pass. §10 records the suite-run conflict with ruling D12-h in AC10, reported and not decided.
  Verification added to §4 Files touched the leg's conf import allow-list, which predates `abac6d59`
  and assigns neither `RECALL_CLI` nor `ASKS_CMD` today, so S3, S5 and S8 would read both blank.
  Extended 2026-09-20, same base, by the regrounding consolidation pass · AC9 AC10 · §7. AC10 gains
  a `permission:` line deferring the `--attribute <BASE>` suite run to the one post-build bar the
  main loop runs at VERIFYING, which folds the conservative reading of the D12-h conflict without
  deciding it; S7, §5 and §10 keep the ruling's wording and the run record parks it. AC9's
  `permission:` line no longer calls a run of §7's arm FILE the pass's direct check, because
  `tools/unattended/gate-guard.js` denies a `*.test.sh` run before VERIFYING; the pass's check is
  the leg itself over a vacuous scratch fixture. §7's `New arm:` third field names the leg suite's
  executed-assertion floor, which that suite pins, beside the `ARMS_FLOORS` pin. No criterion here
  asserts that a phrase counts zero, and this unit writes to no byte-capped carrier.
  Extended again on the closing consolidation pass · §3 · §5 · §10 · AC10, with the header date
  moved to the last-change date and the rev kept. Two owed cross-edits land. The first: the
  D12-h conflict is FOLDED rather than decided, so AC10's own sentence, §5's testing line and §10
  place the attributed run at the one the main loop makes at VERIFYING instead of at this unit's
  end, while the ruling itself stays parked for the owner and stays reported. The second: §3's hazard-id bullet no longer gives a bare 27. It
  keeps the design record's own figure, says it was measured at `abac6d59`, and adds the
  re-measurement at BASE with its one addition and that addition's anchor, so this spec and unit
  33's §10 stop answering one question two ways. This unit still writes to no byte-capped
  carrier, so Decision 1's net-zero rule reaches nothing here.
  Extended again on the close-out pass, same base and rev · §10 · AC10. AC10's `permission:` line
  takes the owed cross-edit's wording verbatim, keeps the hook clause beside it, and now says which
  run covers the suite run: `tools/gate-legs.json` carries no leg for the unattended suites, so it
  is an attributed suite run beside the bar the main loop makes at VERIFYING and no bar reaches it,
  held flags or not. §10 stops calling the D12-h mechanics decided — the question is parked for the
  owner and the run folds the conservative reading meanwhile. Rule 1 reads narrowly here and
  already did: AC9's leg run over a vacuous scratch fixture is the pass's own direct check, and what
  defers is the same leg over the real tree and any run of §7's arm FILE. The close-out verifier
  restored ruling D12-h's OWN words in that §10 sentence: the ruling says the suites run once at
  the unit's end, and stating it in the folded terms left the paragraph parking a conflict it had
  just defined away. AC10 and the `cost:` line are untouched.

- rev-5 · 2026-09-20 · spec-audit round 3 fold, the G3 round-2 record, which exited BOUNDED.
  §3 Edges · §4 · §8 F3 · AC8 AC11. M1 (3): three of S8's declared branches had no criterion, so
  AC11 gains an arm each for the bound breach reported as never answered, the unobserved tip that
  re-derives every mandated record with its reason printed, and the unfindable introducing commit
  that prints a `skipped` line naming the arm, each with its own `Red when:`. L1 (11): AC8's fixture
  carried `prompt` alone where S5's predicate covers both members of `SECOND_ANCHOR_MODES`, so it
  now carries a `recipe` record too and its arm count is read from that constant rather than typed.
  Three findings are PROMOTED to units of this build and folded nowhere: H4 (24) to
  `TOOL-dDerivedDocket-52`, pointed at from §4's S2 paragraph, where the measured rotation rename is
  now stated beside the fallback sentence it contradicts; B1 (21) to `TOOL-dDerivedDocket-48`,
  pointed at from §4 above that paragraph, because S8's two calls route the same capture; and H5
  (25) to `TOOL-dDerivedDocket-53`, pointed at from §8 F3, whose pure-function premise does not hold
  for the conf. §3 gains a consumes-from edge to each, and S2, S8, AC4 and F3's resolution keep
  their current text. No cap is raised, no S-item moves, and §7 does not move: both folded criteria
  are fixtures inside `tools/unattended/check-unattended.test.sh`, which its `New arm:` line already
  names. The fold verifier corrected AC8's blank-conf arm: the fold bound it to `either` of the two
  mode fixtures, where S5 refuses a blank conf for ANY record, so the arm was reachable through the
  mode refusal alone; it now names a THIRD fixture in mode `slug`, and its `Red when:` names that
  reading. The verifier also restored the S2 paragraph break the promotion note ran into.

## 10. Reuse audit

The seam is check 19 in `tools/unattended/check-unattended.sh`, which already re-parses front
matter from the README blob at the recorded BASE and compares it against recorded facts; S1 and S5
are two more keys through that same blob and `awk`. The anchor judgement reuses
`tools/memory-recall/extract.py`'s `anchor_at` rather than a copy. `reuse_lookup.py "second opinion
leg re-derives a run fact against the build README at BASE"` returns only generic python helpers,
because the lookup reports `.sh` as an unscanned layer and so cannot see the leg; the `unattended`
dossier's shared seams name no second re-derivation mechanism, and none is built. Where DR and the
source disagree: DR places check 19 at `:1395-1418`, and at BASE `fb07ca25` the membership and
agreement arms start at `tools/unattended/check-unattended.sh:1424`. The leg grew between
`abac6d59` and `fb07ca25`, and no landed build adds a second opinion over a mandate fact, a folder
anchor ban or a freeze: check 19 still second-opinions `authorized-by:`, `playbook:` and `pieces:`
only, `anchor_at` is unchanged, and `RECALL_CLI` keeps its blank-means-not-adopted contract in both
confs. The leg itself spawns no interpreter today, so S3's is its first, and the driver's inline
resolver is the precedent it copies.

Ruling D12-h, in its own words, would let this unit read the unattended suites once at its end
(AC10). Since `5493495a` the unit child prompt of `tools/workflows/unattended-unit.js` and M6 of
`memory/guides/BUILD-METHOD.md` forbid any self-test suite inside a pass, and
`tools/unattended/gate-guard.js` denies `run-unattended-gates.sh` before VERIFYING. That question
is PARKED for the owner — no child prompt and no hook amends a ratified ruling — and until an owner
turn takes it the run folds the CONSERVATIVE reading, which is the one both machines already
enforce: the attributed run is the one the main loop makes at VERIFYING, after the last unit, which
is what AC10 and §5 are written to.

Recall terms used: `second-opinion check-19 recorded-BASE authorization-mode playbook anchor-ban
resolution-table foreign-id landed-anchor units-at-landing leg-arm skip-announce`
