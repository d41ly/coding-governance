# TOOL-aReplayedCard-1 — `scratch-guard.js` denies a `git commit` on an un-oriented card

**Status:** SPECCED · rev-3 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make orientation a precondition of the session's first durable act rather than a request. A `git
commit` issued by the main loop is refused, with the remedy in the reason, while the session's card
still holds the writer's sentinel or names a different tree. A card that is ABSENT is allowed with
one line saying so: once wired, the writer runs at every session start and the replay rewrites a
missing card, so absence means the harness never ran the hook for this session, and a deny there
would refuse the landing run's own commits and every session already open on the node. The check
rides the PreToolUse process that already spawns on every shell call, and compares paths through
the normaliser that process already ships.

## 2. Scope (IN)

- **S1** One check inside `tools/hooks/scratch-guard.js`, after the existing scratch verdict, that
  fires only when the command's string-blanked view holds the argv token `git`, then any number of
  dash-prefixed tokens and, for each of `-C`, `-c`, `--git-dir`, `--work-tree`, `--namespace`,
  `--exec-path` and `--config-env`, the one value token that follows it unless written in the `=`
  form, and then the whole argv token `commit` followed by whitespace or the end of the command —
  so `git -C /c/x commit -m y` and `git -c a=b commit` match, and `git merge-base`,
  `git merge --ff-only origin/main`, `git log --grep commit` and a quoted `commit` never do — and
  the payload carries no `agent_id`. `merge` and `push` are NOT in the set; §8 records why.
  Observed by AC1, AC6 and AC9.
- **S2** The check resolves the commit's toplevel from the `-C` target when the command carries one,
  relative to the payload's `cwd`, else from `cwd` itself, by walking up to the directory holding
  `.git`; the common dir comes from that `.git` file or directory. It reads
  `<git-common-dir>/orientation/<session_id>.md` and requires a line starting `READY —` whose tail
  is not the writer's sentinel `none yet`, and a `tree —` cell whose toplevel, passed through the
  file's own `buildComparablePath`, equals the resolved toplevel passed through the same function.
  Observed by AC2, AC3 and AC10.
- **S3** The deny is exit 2 with stderr naming the card path, the condition that failed, and the
  one remedy, `/session-kickoff`, which for a tree mismatch means a kickoff run IN the tree the
  commit targets, because `KICK-aReplayedCard-2`'s append rewrites the `tree —` cell to the tree it
  ran in. No waiver clause exists. Observed by AC2 and AC3.
- **S4** The prompt-path exemption: when a `README.md` under a `builds/` path segment is NEW —
  either staged as added, or untracked in the working tree and absent from HEAD and the index — and
  its bytes carry `authorized-by: prompt`, the commit passes without a READY line and stderr says so
  in one line. The rule is spelled once and the spawn derives from it: git runs at the resolved
  toplevel with the pathspec `*builds/*/README.md`, which lists a top-level `builds/x/README.md`
  and a nested `memory/builds/y/README.md` alike. The condition is the commit that CREATES the
  authorization, never the presence of such a folder in the tree, so the single-call
  `git add … && git commit` form, whose index is empty at PreToolUse, is covered by the untracked
  arm. Observed by AC4, AC5 and AC8.
- **S5** Fail open, silently, when `session_id` or `cwd` is absent from the payload — the two fields
  the predicate reads; `tool_use_id` is not read and is not a condition. Fail open with ONE stderr
  line naming the writer that did not run for this session when no card exists under the resolved
  common dir for this `session_id`, whether or not an `orientation/` directory exists: that is the
  state of a tree where the writer is not wired, of a session that opened before the wiring landed,
  and of the landing run itself between orders 3 and 5. Observed by AC1, AC7 and AC11.
- **S6** The file header states the ceiling: a commit made by a script, a heredoc, a non-git tool,
  a deleted card or a hand-written card escapes; the guard stops forgetting, not evasion; a READY
  line's presence is asserted, never its correctness; and `--git-dir` or `--work-tree` pointing
  outside the resolved tree is compared as the resolved tree, not the target. NOT OBSERVED by a
  criterion: header prose.
- **S7** Every arm below is in `tools/hooks/scratch-guard.test.sh`, each observed RED before it
  lands, and `FLOOR_ASSERTIONS` there moves by the number added. Two arms are CLASS arms. One
  extracts every inline code span in `skills/session-kickoff/SKILL.md` Steps 0 through 4 that
  begins `git ` — eight at base — plus the Step 1 batch spelled as literals (`git fetch`,
  `git merge --ff-only origin/main`, `git rev-parse HEAD`, `git status --short`,
  `git worktree list`), feeds each as a sentinel-card payload expecting ALLOW, asserts the extracted
  count is at or above a floor stated beside its base figure, and REFUSES on zero, so the remedy the
  deny names is proven reachable and the arm cannot pass on an empty population. The other runs the
  writer's own `--card --write` in the fixture repository, replaces the sentinel line with a real
  READY line through the test's own `sed`, and feeds that file with `process.cwd()` as the payload
  `cwd`, so a spelling fold between the two kits reds here without depending on a verb built in the
  same step. Observed by AC9, AC10 and AC12.

## 3. Non-goals (OUT)

- No gating of `Edit`, `Write` or any tool that pays no hook today; the design record's section 6
  prices that at a node spawn per edit.
- No second hook file on the `Bash|PowerShell` matcher; the design record's verdict 13 measured a
  node spawn at 0.8–1.1 s on this node, so a second file doubles every shell call's cost.
- No `merge` and no `push` in the commit-shaped set; §8.
- No deny on an ABSENT card; §8.
- No signature, hash or TTL on the card.
- No `--waive`; owner decision 2.
- No exemption keyed on a folder existing in the tree; §8 records why.
- No second path normaliser; `buildComparablePath` at `scratch-guard.js:63` is the one this file
  already ships and its header records why the drive fold is load-bearing.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card path, the `tree —` cell's declared spelling,
  the `READY — none yet` sentinel bytes and the `--card --write` verb the cross-kit arm runs.
- **consumes-from** `KICK-aReplayedCard-2` — the single real `READY —` line the append writes, and
  the `tree —` cell it rewrites to the tree the kickoff ran in; the shipped behaviour, not the
  self-test, which stands in the sentinel line by hand.
- **hands-off** `TOOL-aReplayedCard-3` — the deny a resumed run meets, which its kickoff step
  answers.
- **hands-off** external — the unattended driver's own refusals; this deny never reads a run-state
  file and never exempts on a phase.

## 4. Design

### Data model

The predicate, in order, each step returning ALLOW on its own condition:

1. Not a `git commit` command by S1's token rule → allow.
2. `agent_id` present → allow (a subagent's shell calls are never gated).
3. `session_id` or `cwd` missing → allow, silently.
4. A NEW `builds/*/README.md` — staged-added, or untracked and absent from HEAD and index — whose
   bytes carry `authorized-by: prompt` → allow, one stderr line naming the exemption.
5. No card for this `session_id` under the resolved common dir → allow, one stderr line naming the
   writer that did not run.
6. The card's only READY line is the sentinel, or the two normalised toplevels differ → DENY.

Step 4 spawns `git diff --cached --name-only --diff-filter=A -- '*builds/*/README.md'` and
`git ls-files --others --exclude-standard -- '*builds/*/README.md'` at the resolved toplevel, and
on a hit reads the staged blob with `git show :<path>` or the worktree file, only after steps 1–3
passed and only when step 6 would otherwise deny. The common case pays no spawn.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `checkOriented` | function | `scratch-guard.js` | leads with `check`, a verdict; JS camel per the js cell |
| `readCard` | function | `scratch-guard.js` | leads with `read`, bytes from a named source |
| `resolveToplevel` | function | `scratch-guard.js` | leads with `resolve`, a start dir to the directory holding `.git` |
| `resolveCommonDir` | function | `scratch-guard.js` | leads with `resolve`, the `.git` file's `gitdir` and `commondir` |
| `extractCommitTarget` | function | `scratch-guard.js` | leads with `extract`, the `-C` value out of the blanked view |
| `COMMIT_SHAPED` | regex constant | `scratch-guard.js` | screaming snake like `TOOLS` |
| `GIT_VALUE_FLAGS` | array constant | `scratch-guard.js` | screaming snake; the seven flags that take a value token |

### Migration

None in this repository: the hook is already wired on `Bash|PowerShell`, and a session with no card
is allowed with one line, so no running session and no landing run is denied by the file landing.
An adopter of the hooks kit without the kickoff kit never has a card and is never denied; one with
both is denied only on a sentinel card, which is the designed state before a kickoff.

### Rollout

Lands at order 3. From that commit until `TOOL-aReplayedCard-2` wires the writer at order 4, no
session on the node has a card, so every main-loop commit passes with the one line; from the first
session start after the wiring, the sentinel deny is live. Sessions already open when the wiring
lands keep passing until their next compaction writes a card, and are then denied until they kick
off — which is the designed state, and the line they see names it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/hooks/scratch-guard.js` | the check, five functions, two constants, the header paragraph |
| `tools/hooks/scratch-guard.test.sh` | the arms in §7, two of them class arms; `FLOOR_ASSERTIONS` |
| `tools/hooks/README.md` | one section naming the deny, its grammar, its exemption, its absence rule and its ceiling |
| `memory/map/features/agent-cap.md` | dossier refresh on touch |

### Alternatives rejected

**A new `orientation-guard.js`.** Doubles the per-call spawn cost; verdict 13.

**Keying the exemption on the payload `cwd` holding any prompt-authorized build folder.** Every
landed prompt-path build in this repository leaves such a folder, so the exemption would fire on
every commit forever and the deny would never fire; the acceptance line "a commit without READY
denied" could not be met. Resolved in §8.

**Keeping `merge` and `push` in the set.** The kickoff engine's own Step 1 fast-forward is a
`git merge --ff-only` made before any READY line exists, so the deny would refuse its own remedy;
and the unattended prompt path pushes its build folder before preflight, where no kickoff may yet
run. A push carries commits already gated at commit time and the lander runs the bar at the push
boundary regardless. Resolved in §8.

**Denying on an absent card.** The card directory is under the common dir every worktree on the
node shares, and this build's own criteria create it at order 2; a deny on absence then refuses
the landing run's own commits from order 3, with a remedy whose append clause lands at order 5, and
refuses every session already open on the node the moment a new session's writer creates the
directory. The only exits were the evasions the header names. Resolved in §8.

**Comparing the two toplevels as bytes.** Measured at the synthesis: the writer prints
`C:/…`, the shell's `pwd` prints `/c/…`, node prints `C:\…`; every registered node is Windows plus
Git-Bash, so a byte compare denies the fleet with a green suite. `buildComparablePath` exists in
this file for exactly that fold.

**Reading the card from context rather than disk.** A hook sees the payload, not the transcript;
the file is the only thing it can read.

## 5. Production-readiness checklist

- security — the hook reads one file under the common dir and spawns git with fixed argv at a
  resolved directory; `cwd` and the `-C` value are used only to locate `.git`, never interpolated
  into a shell.
- perf / scale — zero spawns on the common path; two on the exemption path, which is one commit
  per prompt-path run.
- error / empty / loading states — missing fields fail open silently; a missing card fails open
  with a line; a sentinel card denies with the remedy; a tree mismatch denies naming both trees and
  the tree to kick off in.
- observability — every deny prints the card path and the failed condition; every fail-open on
  step 4 or 5 prints its one line.
- risks — deny-forever if the sentinel predicate or the path compare is wrong; the cross-kit arm
  feeds the writer's real bytes, and the reason names which condition failed. A session that moves
  trees is denied until it kicks off there, which the append's cell rewrite makes possible.
- testing — the arms in §7, RED first, two of them class arms with a refused empty population.
- migration — none.
- user docs — `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `git commit -m x` payload with a `session_id` whose card is
  absent, with and without an `orientation/` directory in the fixture's common dir, the hook exits
  0 and stderr carries exactly one line naming the writer that did not run for that session.
  Red when: an absent card denies, so the landing run and every open session are refused with a
  remedy that cannot yet append.
- **AC2** — When the card exists and holds `READY — none yet` only, the hook exits 2 naming the
  sentinel and `/session-kickoff`; when it holds a `READY — t · node a` line and a matching `tree —`
  cell, the hook exits 0.
  Red when: the sentinel satisfies the predicate, or the deny prints no remedy.
- **AC3** — When the card's `tree —` toplevel names a sibling worktree, the hook exits 2 naming
  both trees and a kickoff in the commit's tree as the remedy; when the card was written in tree A
  and its `tree —` cell then rewritten to B the way the append does, a payload from B exits 0.
  Red when: a card written in worktree A opens commits in worktree B, or a moved session is denied
  for life with a remedy that cannot change the cell.
- **AC4** — When the fixture repository stages a new `README.md` at `builds/x/` of the fixture,
  carrying `authorized-by: prompt`, and the card holds the sentinel, the hook exits 0 and stderr
  carries one line naming the exemption; the same with the file at `memory/builds/y/` of the
  fixture.
  Red when: the staged-added check reads the worktree file instead of the staged blob, or the
  pathspec misses one of the two depths.
- **AC5** — When that same fixture has the folder COMMITTED in HEAD and stages an unrelated file,
  the `git commit -m y` payload exits 2.
  Red when: the exemption keys on the folder's existence and fires on every later commit.
- **AC6** — When the payload carries an `agent_id`, the hook exits 0 with a sentinel card.
  Red when: a subagent's commit is gated.
- **AC7** — When the payload lacks `session_id`, the hook exits 0 and prints nothing; when it lacks
  only `tool_use_id` and the card holds the sentinel, the hook exits 2.
  Red when: the fail-open is assumed rather than asserted, or a field the predicate never reads
  opens the deny.
- **AC8** — When the fixture holds an UNTRACKED `README.md` at `memory/builds/y/` carrying
  `authorized-by: prompt`, nothing staged, and the payload is `git add memory && git commit -m z`
  issued from a subdirectory `cwd` of the fixture, the hook exits 0 with the exemption line.
  Red when: the single-call add-and-commit form is denied because the index is empty at
  PreToolUse, or the spawn runs at the payload `cwd` and lists nothing.
- **AC9** — When every inline code span beginning `git ` in `skills/session-kickoff/SKILL.md` Steps
  0 through 4, plus the five Step 1 literals, plus `git merge-base origin/main HEAD`,
  `git merge --ff-only origin/main`, `git log --grep push` and `git push origin main`, is fed as a
  sentinel-card payload, every one exits 0, the arm prints the count it extracted, that count is at
  or above the floor `8` stated beside it, and a run over a fixture engine file with no such span
  exits 1 naming the empty population; and `git -C /c/x commit -m y` and `git -c a=b commit` fed
  the same way exit 2.
  Red when: the remedy the deny names is itself denied, `merge-base` matches at a word boundary,
  the value-flag forms slip past the grammar, or an empty extraction passes.
  figure: DERIVED — the arm extracts the spans from the engine file at run time; the floor is
  PINNED at the base measurement of 8.
- **AC10** — When the self-test runs `bash skills/session-kickoff/manifest-check.sh --card --write`
  in its fixture repository, replaces the sentinel line with a real READY line by `sed`, and feeds
  the resulting file unedited otherwise with `process.cwd()` as the payload `cwd`, the hook exits
  0; with the card holding `/c/…` and the payload `C:\…` for one tree, the hook exits 0.
  Red when: the two kits spell the toplevel differently and the compare is on bytes.
- **AC11** — When the fixture's real common dir is listed after the whole self-test, no
  `orientation/` entry the suite wrote remains.
  Red when: a fixture card is left behind for a sibling session or a sibling suite to trip on.
- **AC12** — When `bash tools/hooks/scratch-guard.test.sh` runs, it prints `PASS` with an
  assertion count at or above the moved `FLOOR_ASSERTIONS`, and a non-commit `ls` payload with a
  sentinel card exits 0.
  Red when: an arm is unreachable and the floor did not move.

## 7. Gates

`scratch-guard self-test` · `hook destinations (every declared hook path ships)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/hooks/scratch-guard.test.sh` · an absent card, with and without the directory · `FLOOR_ASSERTIONS`
New arm: `tools/hooks/scratch-guard.test.sh` · a card with only the sentinel · same
New arm: `tools/hooks/scratch-guard.test.sh` · a `tree —` cell naming another worktree, and one rewritten to the payload's tree · same
New arm: `tools/hooks/scratch-guard.test.sh` · a staged-added prompt-authorized README at two depths · same
New arm: `tools/hooks/scratch-guard.test.sh` · the same folder already in HEAD · same
New arm: `tools/hooks/scratch-guard.test.sh` · an `agent_id` payload · same
New arm: `tools/hooks/scratch-guard.test.sh` · a payload with no `session_id`, and one with no `tool_use_id` · same
New arm: `tools/hooks/scratch-guard.test.sh` · an untracked prompt-authorized README and a single-call add-and-commit from a subdirectory · same
New arm: `tools/hooks/scratch-guard.test.sh` · every inline git span of the engine's Steps 0–4, the batch literals, four near-miss literals, two value-flag hits, and an empty fixture engine · same
New arm: `tools/hooks/scratch-guard.test.sh` · the writer's own card with the sentinel replaced by `sed`, and the two path spellings · same
New arm: `tools/hooks/scratch-guard.test.sh` · the common dir holds no suite-written card after the run · same
New arm: `tools/hooks/scratch-guard.test.sh` · a non-commit payload with a sentinel card · same

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

- **The exemption's key.** The owner's answer reads "the hook checks the cwd for a build folder
  with `authorized-by: prompt`". Read literally, every commit in this repository is exempt, because
  landed prompt-path builds leave such folders in the tree, and the prompt's own acceptance line
  "a commit without READY denied with the remedy in the reason" cannot then be met. The only
  reading under which both the owner's decision and the acceptance survive is the commit that
  CREATES the authorization: a NEW `builds/*/README.md`, staged-added or untracked, whose bytes
  carry the key. RESOLVED (agent, 2026-09-13, delegated): the new-README reading, S4, with AC5 as
  the arm that proves the literal reading is not what shipped and AC8 as the arm for the
  single-call form.
- **The commit-shaped set.** The prompt names "commit-shaped" and the design record spelled
  `commit|merge|push`. The round-1 audit showed the engine's own Step 1 fast-forward is a
  `git merge --ff-only` made before any READY line, so the deny would refuse its own remedy, and
  the unattended prompt path pushes its build folder before the preflight that permits a kickoff,
  so owner decision 3 would be defeated at the push. The acceptance line names a COMMIT. RESOLVED
  (agent, 2026-09-13, delegated): the set is `commit` alone, S1; a push carries commits already
  gated at commit time and the lander runs the bar at the push boundary; AC9 is the arm that keeps
  the engine's fast-forward and the near-miss spellings allowed.
- **An absent card.** The prompt's acceptance line reads "a commit without READY denied". The
  round-2 audit showed a deny on ABSENCE refuses this build's own landing run from order 3 and
  every session open on the node when a new session's writer creates the shared directory, with no
  bootstrap but the evasions the header names. The line is satisfied by the sentinel deny: a
  session whose writer ran and who never kicked off is refused; a session whose writer never ran is
  told so and allowed, because the writer runs at every session start once wired and absence then
  means the harness skipped the hook, which no deny can repair. RESOLVED (agent, 2026-09-14,
  delegated): S5's absence rule and AC1.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §1 · §2 · §3 · §4 · §6 · §7 · §8 · S1 · S2 · S4 · S5 · S7 · AC1 · AC8 ·
  AC9 · AC10 · AC11 · AC12 · folded the round-1 spec audit. The set is `commit` alone as a whole
  argv token, so the engine's fast-forward and the prompt path's push are never denied and
  `merge-base` never matches (B1, B2); both toplevels pass through `buildComparablePath` and the
  toplevel resolver returns the directory holding `.git` (B4); the sentinel is excluded by its
  tail (H1); an untracked new README covers the single-call add-and-commit (H8); no `orientation/`
  directory fails open with one line, citing `TOOL-aUnmannedHelm-4` (M11); two class arms — the
  engine's own fenced commands, and the writer's own card fed unedited (B1, B4 left-shifts).
- rev-3 · 2026-09-14 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · S1 · S2 · S3 · S4 · S5 · S6 · S7 ·
  AC1 · AC3 · AC4 · AC7 · AC8 · AC9 · AC10 · AC11 · folded the round-2 spec audit. An ABSENT card
  allows with one line and the directory probe is gone, so the landing run and every open session
  can commit while the writer is unwired; the sentinel and the tree mismatch are the two denies
  (B1, third §8 mark); the grammar skips the value token of `-C`, `-c` and the five path flags and
  the toplevel resolves from the `-C` target (H3); the class arm extracts inline `git ` spans,
  states its floor of 8 and refuses an empty population (H2); the tree-mismatch remedy is a kickoff
  in the target tree, which the append's cell rewrite makes possible, with the rewritten-cell arm
  (H4); the cross-kit arm replaces the sentinel by `sed` rather than through a same-step verb
  (M1); the pathspec is `*builds/*/README.md` at the resolved toplevel with both depths pinned
  (M12); `tool_use_id` leaves the fail-open set (L4); the arm count leaves the prose (L3); a
  cleanup arm on the real common dir (B1 left-shift).

## 10. Reuse audit

The seam is `tools/hooks/scratch-guard.js` itself — the process, the stdin parse, the string-blanked
command view, `buildComparablePath` at its line 63, and the deny protocol at its lines 370–390 —
and `agent-cap.js`'s `.git` walk at its line 1512 for the common dir, which returns the common dir
and not the toplevel, so the toplevel resolver here is the directory the walk stopped in. `python
tools/codebase-map/reuse_lookup.py "session orientation card written at session start, replayed
after compaction, commit denied until READY"` returned `agent-cap.topLevelArgs` and the
`pre-commit` hook as seams; the pre-commit hook was read and rejected as the home because it sees no
session id, and the PreToolUse payload is the only surface that does. The empty-population refusal
reuses `tools/check-hook-destinations.sh`'s shape at its lines 27–35.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
