# Spec briefs — aProbedUnit, all seven units

**Serves:** journal TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

What the SPEC stage's writers are handed, per unit. The orientation below was done by the run
before the roster was written, at base `1b000d1a`; a writer verifies a line number against source
before citing it, because the driver is 5000 lines and moves.

## Rules every spec obeys

- Shape: `memory/TEMPLATE-SPEC.md`, ten sections, status header `**Status:** SPECCED · rev-1 ·
  2026-09-14 · node a · Tier-<n> · base 1b000d1a · streams tooling · order <n>`. The `order` value
  is the unit number. Filename `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-<n>.md`.
- §6 acceptance names OBSERVATIONS — a command and what it prints, a gate leg by its manifest name,
  a staged red observed — never a path the unit will create. `tools/check-spec-tokens.py` grades every
  backticked path-shaped token in §6 against `git ls-files`, and the waiver file is shrink-only.
- §7 gates are what `--close` runs, NOT what the pass runs. State that in §7 for every unit: the
  pass verifies with the ONE check that exercises its change, and nothing else.
- §10 carries the recall terms used and the seam cited. The seam for every unit is named below; the
  recall probe already run is `python tools/memory-recall/query.py` with the terms in each brief.
- Every kit file names nothing outside itself by literal (charter §12); a shipped `.js` under
  `tools/workflows/` spells no install path — paths travel in `args` or in the `.template.js`.
- A unit that edits a `*.template.*` file re-renders its output in the SAME commit:
  `bash tools/unattended/adopt-unattended.sh` for the unattended templates, the review-harness
  gate's `--render` mode for `unattended-build.template.js`, `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`
  for `BUILD-METHOD.template.md`. The parity legs byte-compare template and render.
- A unit that edits a file the kickoff manifest WATCHES (`.unattended.conf`,
  `memory/guides/BUILD-METHOD.md`) re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` in
  the same commit with a delta line in the commit message. Units 1, 3, 6, 7 do.
- Kit VERSION bumps are the closing pass's, once: unattended 1.21 → 1.22 across every carrier
  `bash tools/check-kit-versions.sh` names, memory-tree 2.75 → 2.76 across five carriers, agent-cap
  1.14 → 1.15. A unit does NOT bump a version.
- Every new `fail <n> "…"` branch in `tools/unattended/unattended.sh` needs an ARM in
  `tools/unattended/unattended.test.sh` asserting its literal text — `check-arms selftest` is on the
  bar. A unit observes its arm RED by running that arm's fixture alone, never the suite whole.

## Unit 1 — `TOOL-aProbedUnit-1` — no gate, suite or bar inside a unit pass (Tier 2)

**Defect.** A unit agent reads its spec's §7 Gates and template §1's "gates green" and runs the merge
bar, self-test suites included, inside its pass; one pass ran 5 h stacking suites
(`memory/builds/aRatifiedRulings/README.md`, build-level rules, owner 2026-09-13), another 12 h on
node d. The owner's rule now: in one session gates run ONCE, PRE-MERGE, when every finding is fixed.

**Mechanism.** The child prompt in `tools/workflows/unattended-unit.js` (`PROMPT`, after
`DRIVER_STEPS`) gains a binding paragraph: never run `tools/run-gates/run-gates.sh`, any leg of
`tools/gate-legs.json`, any `*.test.sh` suite, or the spec's §7 gate list inside this pass — those are
`--close`'s, once; verify with the single smallest check that exercises the change (one test file,
one script arm, one command), and say in `summary` which check ran and which gate it stands in for.
A spec's §7 or a brief that says otherwise is overridden by this sentence. The parent's `GROUND` in
`tools/workflows/unattended-build.template.js` (and its render) carries the same one-sentence rule so
the SPEC writers write §7 as the close's list.

**The method carrier.** `tools/memory-tree/BUILD-METHOD.template.md` M6, the sentence "Then the
diff-scoped gates for what the pass touched; the full bar runs ONCE, at the push boundary. A pass
whose gate is red…" becomes: no gate and no suite runs inside a pass; the bar runs ONCE at the close;
a pass verifies with the one check that exercises its change; a pass whose check is red is not
followed by another. The file is at 26743 of a 27648-byte cap and 340 of 350 lines: the edit trades
bytes or it does not land. Re-render `memory/guides/BUILD-METHOD.md`.

**The Skill.** `tools/unattended/SKILL.template.md`, the "Drive the build as ONE program" bullet:
one sentence that the child is ordered not to run gates and the bar is `--close`'s. Re-render
`.claude/skills/unattended/SKILL.md`.

**Acceptance shape.** `grep -c` of the new sentence in the child, the template AND the render of the
build harness, the method template AND its render; `bash tools/workflows/check-protocol-parity.test.sh`
(or the parity leg's manifest name) green; `node tools/workflows/check-workflow-syntax.js` green;
`bash tools/unattended/adopt-unattended.sh --check` green.

**Seam.** The child's `PROMPT` string and the parent's `GROUND`; both already exist and are the only
carriers a sidechain agent reads. Recall terms used: `unit pass gates merge bar full bar push
boundary diff-scoped run-gates unattended-unit stall suite self-test close`.

## Unit 2 — `TOOL-aProbedUnit-2` — every command a unit runs is bounded (Tier 1)

**Defect.** A unit sat 6 h 14 min on one `rm` and a whole workflow waited on it. Nothing in the
child prompt bounds a command or says what to do when one does not return.

**Mechanism.** The same `PROMPT` in `tools/workflows/unattended-unit.js` gains a second paragraph:
PRIMARY OBJECTIVE is code written and committed. Every shell call carries the tool's `timeout`
parameter — 120 s default, at most 600 s for a build or test command the change itself needs — and a
check, cleanup, probe or any command unrelated to writing code that exceeds it is SKIPPED, named in
`summary` with what it was for, and never re-run or waited on. Never wait on a command with no
bound. A backgrounded command is polled by the harness's notification, not by a loop. The Skill bullet
from unit 1 gains one clause naming this.

**Acceptance shape.** `grep -c` of the timeout sentence in the child; `check-workflow-syntax.js`
green; the child still has exactly ONE top-level definition (`check`) — the codebase-map JS liveness
floor counts it. Tier 1: prompt text only, no new write path.

**Seam.** The child `PROMPT`. Recall terms: `bounded command timeout stalled unit skip cleanup probe
rm approval prompt session blocked hours`.

## Unit 3 — `TOOL-aProbedUnit-3` — `--audit <slug>`, the dispatched-unit stall probe (Tier 2)

**Defect.** Nothing observes a live unit from outside. The keepalive fires every 10 minutes while a
`Workflow` runs in the background and does nothing with the turn.

**Mechanism, the verb.** `tools/unattended/unattended.sh` gains `--audit <slug>` in `VERBS_SLUG`, the
header's invocation lines (the usage text is DERIVED from them), and the dispatch `case`. For each
unit whose LATEST `dispatch · item <grp> <id> · reason …` row in the run-state file has no later
build commit carrying that id in its subject (the same join `check-brief-recorded.sh` and
`check-pass-order.sh` make — read theirs, do not invent a third), print one line:
`unattended-audit: <id> · dispatched <ISO> · elapsed <s>s · last-write <s>s ago · last-commit <s>s ago · <PROGRESSING|STALLED>`.
`last-write` is the newest mtime among `git status --porcelain` paths (modified + untracked) relative
to now; `last-commit` is `git log -1 --format=%ct`. STALLED when BOTH exceed `UNIT_STALL_BOUND`
seconds, a conf key read where `GATE_BOUND` is read (validated positive integer; absent → the kit
default 1800, ANNOUNCED on stderr the way `GATE_BOUND` is). A STALLED line is followed by the remedy
line: stop the unit's task, re-dispatch it with a brief naming what stalled and that it is skipped.
No dispatched-and-open unit → print `unattended-audit: no unit is dispatched and open` and exit 0.
A dispatched unit whose declared write set includes a path the tree never wrote is NOT a separate
verdict — say in the header what the verb does not check: what the unit is doing, whether a process
is stuck. Where `tools/process-monitor/census.py` is tracked, print one pointer line naming it as
the process-side probe; where it is not, print nothing about it.

Refusals, each a `fail <n>` with an ARM: no run-state file; a terminal record (`refuse_if_terminal`).
Take the next free check number after the driver's current high-water (`fail 50` is in use).

**Mechanism, the keepalive.** `tools/unattended/SKILL.template.md`, the "schedule the keepalive NOW"
section: the keepalive PROMPT the agent schedules is `bash tools/unattended/unattended.sh --audit
<slug>` (spelled through the `{{TOOL_ROOT}}` token the template already uses for the driver) — on
`STALLED` the main session stops the unit's task, records `--park` or a brief note, and re-dispatches
that unit with a brief naming the stalled command as skipped; on `PROGRESSING` it does nothing. Before
`--preflight` exists no slug is known, so the prompt says "once the run has a slug, run …". Also
`tools/unattended/VERBS.template.md` gains the `--audit` bullet, and `PROTOCOL.template.md` §8 (what a
project declares) names `UNIT_STALL_BOUND`. `kit.toml` `optional_keys` gains `UNIT_STALL_BOUND`;
`.unattended.conf` and `tools/unattended/.unattended.conf.example` (if tracked — check) declare it
with the reason beside it.

**Acceptance shape.** On a fixture run-state file with a dispatch row dated an hour ago and a clean
tree whose last commit is older than the bound, `--audit` prints `STALLED`; with a file touched now,
`PROGRESSING`; with no dispatch row, the no-unit line. The two refusal arms observed RED by running
each arm alone. `bash tools/unattended/adopt-unattended.sh --check` green after re-render.
`check-arms selftest` green.

**Seam.** `verb_status` (reads the run-state file the same way), `review_counts`'s awk row parser,
`run_bounded` and the `GATE_BOUND` conf read for the bound. Recall terms: `dispatch row unit stall
elapsed idle keepalive cron audit probe process-monitor census bound conf`.

## Unit 4 — `TOOL-aProbedUnit-4` — every harness agent is handed the session scratchpad (Tier 2)

**Defect.** Agents write temporary files to `$TMPDIR/x` with `TMPDIR` empty (measured empty on node
`a` this session; the incident on node `d`), to `/tmp`, and to drive roots. The session scratchpad
path is in the caller's system prompt and nowhere a workflow script can read.

**Mechanism.** `tools/workflows/unattended-build.template.js` (and its render) REQUIRES a new arg
`scratch` — an absolute path — refusing without it in the style of `repo`/`slug` (a defaulted
scratch root is the floating temp dir this unit exists to end). It is carried in `dispatch.args`
and into `GROUND` as one sentence: every temporary file, backup, probe, log or throwaway clone goes
under that path, spelled absolute; never `$TMPDIR`, `$TMP`, `$TEMP`, `/tmp`, a bare `mktemp`, or any
path outside the repository. `tools/workflows/unattended-unit.js` adds `check('scratch', …)` and the
same sentence in `PROMPT`. `tools/unattended/SKILL.template.md`'s dispatch instructions tell the
caller to pass its own scratchpad path — the one its system prompt names — as `scratch`.

**Acceptance shape.** The build harness's test double (`tools/workflows/unattended-build.test.sh`)
gains an arm observing the refusal without `scratch` RED and the passing case with it; the child
refuses without `scratch`; `grep -c` of the sentence in both files and both renders;
`check-workflow-syntax.js` and the parity leg green.

**Seam.** The `check()` predicate in the child and the `cfg.repo`/`cfg.slug` refusals in the parent.
Recall terms: `scratchpad session temp dir TMPDIR empty backup fixer prompt args harness child
absolute path`.

## Unit 5 — `TOOL-aProbedUnit-5` — scratch-guard denies an empty temp variable, `/tmp`, and root litter (Tier 2)

**Defect and measurement.** `tools/hooks/scratch-guard.js` reads a write target textually; `cp x
$TMPDIR/y` with `TMPDIR` empty is allowed and lands at `/y`. Over 55,231 real Bash calls on node `a`
its own `scanWriteTargets` found 72 `$TMPDIR`-rooted, 143 `$TEMP`-rooted, 3,803 `/tmp`-rooted and 4
POSIX-root (`/mir`, `/xj`) write targets. The owner ruled 2026-09-14: deny `/tmp` too.

**Mechanism, three predicates in `checkCommand`, each with its own `kind` and sentence in
`renderDeny`.**
1. `empty-var`: a target beginning `$TMPDIR`, `${TMPDIR}`, `$TMP`, `$TEMP` (braced or bare) whose
   variable is EMPTY or unset in `process.env` is denied — the message says the variable is empty in
   this session so the write lands at the filesystem root. A NON-empty variable is expanded into the
   target and grading continues. `${VAR:-default}` expands to the default when the variable is empty.
2. `tmp`: a target whose comparable form is `/tmp` or under it is denied, naming the scratchpad.
3. `posix-root`: a target `/<top>/…` (no drive letter after `buildComparablePath`) whose `<top>` is
   not in a POSIX-root conventional set (`dev proc sys usr etc var opt home root mnt media srv bin
   sbin lib lib64 run boot private volumes cygdrive workspace workspaces` — hand-listed like
   `DRIVE_ROOT_CONVENTIONAL`, for the same stated reason) is litter and denied. `/tmp` and `/temp`
   are NOT in that set, so rule 2 and this one agree.
**The allowed roots grow by one**: `<os.tmpdir()>/claude` — the CLI's scratchpad base
(`<tmpdir>/claude/<project-slug>/<session-id>/scratchpad`, verified against the CLI binary this
session) — so on a POSIX host where the scratchpad sits under `/tmp`, rule 2 does not deny the one
place the owner wants writes to go. Fails open exactly as today on unparseable input.

**Acceptance shape.** `bash tools/hooks/scratch-guard.test.sh` gains arms: each of the three denials
observed RED on a fixture command with the variable unset/empty in the arm's env, and the ALLOW cases
— a non-empty `TMPDIR` target under it, `<tmpdir>/claude/x`, `/dev/null`, `/c/projects/x` — observed
green. `tools/hooks/README.md` states the three rules and what they do not catch (variable
indirection, heredoc'd Python, `cd`). The hook's version constant stays; the closing pass bumps
agent-cap.

**Seam.** `buildResolvedTarget` (already expands `~`/`$HOME`), `checkDriveRootLitter`,
`resolveAllowedRoots`. Recall terms: `scratch-guard write target home directory drive-root litter
allowlist derived TMPDIR TEMP corpus measured deny`. The gotcha
`allowlist-narrower-than-the-root-it-guards` is the class rule 2 must not re-commit: the scratch base
under `/tmp` is the sanctioned destination INSIDE the denied prefix.

## Unit 6 — `TOOL-aProbedUnit-6` — `REVIEW_ROUNDS` bounds a spec-audit subject; the `BOUNDED` exit (Tier 2)

**Defect.** `review_state` in `tools/unattended/unattended.sh` re-arms the loop at round 1 whenever
blockers > 0, so every spec audit with one blocker costs a second lens fan. Owner rule: one round by
default, SPEC subjects only; the closing DIFF review keeps its convergence loop.

**Mechanism, the driver.** A conf key `REVIEW_ROUNDS`, optional, read where `GATE_BOUND` is,
validated as a positive integer not above `RUNAWAY_CEILING`, defaulting to 1 with the default
ANNOUNCED on stderr. `review_state` takes the bound: `blockers == 0 → CONVERGED`; `n>0 and count ≥
prev → NON-CONVERGENT`; `n+1 ≥ RUNAWAY_CEILING → CEILING`; NEW: `n+1 ≥ bound → BOUNDED`; else
`CONVERGING`. The bound applies ONLY when the subject is not the build slug — `verb_review` already
has `subj` and `slug`; the diff review's subject IS the slug per the Skill and the `diff-reviewed`
DoD term (`review_last_reason "$rel" "$slug"`), so a diff-review round passes the ceiling as its
bound. `BOUNDED` is TERMINAL: it joins the terminal grep in `verb_review`, the `note` case, the echo
case (its own sentence: the declared round bound is reached, the loop STOPS, every standing
blocker is disposed by severity — unit 7's rule), and `--close`'s `diff-reviewed` term's
`*CONVERGED*|*NON-CONVERGENT*|*CEILING*` case. **`--disposition` at a terminal exit becomes
OPTIONAL and DEFAULTS to `promote`** — the severity rule makes `promote` the demanded value whenever
blockers > 0, which is the only way a non-CONVERGED exit is reached, and the gotcha
`one-value-field-records-a-mixed-outcome` already rules that a mixed exit records `promote`. The
`fail 37 "--review exits $state and requires --disposition …"` branch is DELETED and its arm rewritten
to assert the default is written; an EXPLICIT `--disposition` on a non-terminal round stays refused.

**Mechanism, the readers.** `tools/unattended/check-unattended.sh` check 2: `BOUNDED` joins both
regexes (`term` and `needs`). `tools/workflows/unattended-build.template.js` and render:
`REVIEW_TOKENS` gains `BOUNDED`, the recorder prompt names five tokens, and the `verdict ===
'CONVERGED'` disposal skip is unit 7's to change. `VERBS.template.md` `--review` bullet,
`SKILL.template.md` "Record each review round" list (a fifth state), `PROTOCOL.template.md` §8
(declares `REVIEW_ROUNDS`), `kit.toml` `optional_keys`, `.unattended.conf` (declare `REVIEW_ROUNDS=1`
with the reason), `BUILD-METHOD.template.md` M4's convergence paragraph (one round by default for a
spec subject; the diff review converges) — byte-neutral or better, and unit 7 edits the same
paragraph's disposal sentence, so unit 6 leaves that sentence alone.

**Acceptance shape.** `review_state` sliced arms: with bound 1, `review_state '' 3` → `BOUNDED`;
with bound 8 the existing sequence arms hold unchanged; a diff-review subject (equal to the slug) at
round 1 with 3 blockers → `CONVERGING`. A fixture round recorded at `BOUNDED` with no
`--disposition` writes `· BOUNDED · disposition promote`. `bash tools/unattended/check-unattended.sh`
green over a fixture record carrying a `BOUNDED` exit. `check-arms selftest` green.

**Seam.** `review_state`, `verb_review`'s state gate, check 2's awk, the `GATE_BOUND` conf read.
Recall terms: `review round convergence CONVERGING NON-CONVERGENT disposition fold promote blockers
ceiling spec-audit tier2 bound one round`. Prior: `TOOL-aProvenReuse-3` (OPEN), `TOOL-dFoldedVerdict-1`,
`TOOL-aLeakedHandle-6`.

## Unit 7 — `TOOL-aProbedUnit-7` — disposal by severity, on any confirmed finding (Tier 2)

**Defect.** The DISPOSAL stage in `tools/workflows/unattended-build.template.js` runs only when the
verdict is not `CONVERGED` and disposes by NATURE (fold a document defect, promote a missing
mechanism). A `CONVERGED` round with three highs and five mediums disposes nothing. Owner rule:
blockers and highs are PROMOTED (a unit, per M4), mediums and lows are FOLDED into their specs.

**Mechanism.** The stage runs whenever `auRaw.confirmed > 0` (an integer the review harness returns;
`blockers` and `highs` beside it) — on `CONVERGED` too, announced as such — and its prompt reads:
open the report; PROMOTE every confirmed BLOCKER and HIGH through `--rescope --act add --item <id>`
and a spec at its tier whose mechanism CLOSES the finding (the change to the design and the artifact
that proves it), so it is audited once and built; FOLD every confirmed MEDIUM and LOW into the spec it
belongs to as a rev-N bump with its §9 line; never parked, waived, retired or re-reviewed; name in
`standing` every finding not disposed. The `DISPOSAL_SCHEMA` gains `promoted` and `folded` integer
counts so the hand-out reports the split. The `verdict === 'CONVERGED'` skip becomes a
`confirmed === 0` skip. M4 in `BUILD-METHOD.template.md`: the disposal sentence becomes the severity
rule (with unit 6's round-bound sentence beside it); `TOOL-aProvenReuse-3` is answered — mark the
backlog row CLOSED by this ruling with its residual (a promoted spec defect's unit is the mechanism
that closes it). The Skill's `NON-CONVERGENT` bullet and `VERBS` describe the severity rule once.

**Acceptance shape.** `tools/workflows/unattended-build.test.sh` arms: with a test double returning
`confirmed: 4, blockers: 0, highs: 1` the disposal agent is spawned (observed via the log line) and
the return carries `promoted`/`folded`; with `confirmed: 0` the skip line prints. The M4 edit fits the
byte cap; `kit-dogfood-parity.test.sh` green after render; `check-workflow-syntax.js` green.

**Seam.** The existing DISPOSAL stage and `DISPOSAL_SCHEMA`; `tier2-review.js`'s return already
carries `confirmed`, `blockers`, `highs`. Recall terms: `disposal fold promote severity blocker high
medium low rescope add unit spec-audit converged skip`.
