# TOOL-aReplayedCard-1 — `scratch-guard.js` denies a `git commit` with no READY line

**Status:** SPECCED · rev-2 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make orientation a precondition of the session's first durable act rather than a request. A `git
commit` issued by the main loop is refused, with the remedy in the reason, until the session's card
carries a real `READY —` line written in this tree. The check rides the PreToolUse process that
already spawns on every shell call, so it costs no second node spawn, and it compares paths through
the normaliser that process already ships.

## 2. Scope (IN)

- **S1** One check inside `tools/hooks/scratch-guard.js`, after the existing scratch verdict, that
  fires only when the command's string-blanked view holds the argv token `git`, optional
  dash-prefixed flags, and then the whole argv token `commit` followed by whitespace or the end of
  the command — so `git merge-base`, `git merge --ff-only origin/main`, `git log --grep commit`
  and a quoted `commit` never match — and the payload carries no `agent_id`. `merge` and `push` are
  NOT in the set; §8 records why. Observed by AC1, AC6 and AC9.
- **S2** The check reads `<git-common-dir>/orientation/<session_id>.md`, resolving the toplevel
  from the payload's `cwd` by walking up to the directory holding `.git`, and the common dir from
  that `.git` file or directory. It requires a line starting `READY —` whose tail is not the
  writer's sentinel `none yet`, and a `tree —` cell whose toplevel, passed through the file's own
  `buildComparablePath`, equals the payload-derived toplevel passed through the same function.
  Observed by AC1, AC2, AC3 and AC10.
- **S3** The deny is exit 2 with stderr naming the card path, the condition that failed, and the
  one remedy, `/session-kickoff`. No waiver clause exists. Observed by AC1 and AC2.
- **S4** The prompt-path exemption: when a `README.md` under a `builds/` segment is NEW — either
  staged as added, or untracked in the working tree and absent from HEAD and the index — and its
  bytes carry `authorized-by: prompt`, the commit passes without a READY line and stderr says so in
  one line. The condition is the commit that CREATES the authorization, never the presence of such
  a folder in the tree, so the single-call `git add … && git commit` form, whose index is empty at
  PreToolUse, is covered by the untracked arm. Observed by AC4, AC5 and AC8.
- **S5** Fail open, silently, when `session_id`, `tool_use_id` or `cwd` is absent from the payload,
  mirroring the hook's existing posture. Fail open with ONE stderr line when the resolved common
  dir holds no `orientation/` directory at all: the writer is not wired in that tree, the hooks kit
  does not require the kickoff kit, and a kit-dependent rule is kit-conditional
  (`TOOL-aUnmannedHelm-4`). Observed by AC7 and AC11.
- **S6** The file header states the ceiling: a commit made by a script, a heredoc, a non-git tool,
  a removed `orientation/` directory or a hand-written card escapes; the guard stops forgetting, not
  evasion; and a READY line's presence is asserted, never its correctness. NOT OBSERVED by a
  criterion: header prose.
- **S7** Every arm below is in `tools/hooks/scratch-guard.test.sh`, each observed RED before it
  lands, and `FLOOR_ASSERTIONS` there moves by the number added. Two arms are CLASS arms: one feeds
  every fenced `git …` command from `skills/session-kickoff/SKILL.md` Steps 0 through 4 as a
  no-card payload expecting ALLOW, so the remedy the deny names is proven reachable; one runs the
  writer's own `--card --write` in the fixture repository and feeds that file unedited with
  `process.cwd()` as the payload `cwd`, so a spelling fold between the two kits reds here.
  Observed by AC9, AC10 and AC12.

## 3. Non-goals (OUT)

- No gating of `Edit`, `Write` or any tool that pays no hook today; the design record's section 6
  prices that at a node spawn per edit.
- No second hook file on the `Bash|PowerShell` matcher; the design record's verdict 13 measured a
  node spawn at 0.8–1.1 s on this node, so a second file doubles every shell call's cost.
- No `merge` and no `push` in the commit-shaped set; §8.
- No signature, hash or TTL on the card.
- No `--waive`; owner decision 2.
- No exemption keyed on a folder existing in the tree; §8 records why.
- No second path normaliser; `buildComparablePath` at `scratch-guard.js:63` is the one this file
  already ships and its header records why the drive fold is load-bearing.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card path, the `tree —` cell's declared spelling,
  the `READY — none yet` sentinel bytes and the `--card --write` verb the cross-kit arm runs;
  without the card every main-loop commit in a wired tree is denied, which is the intended state
  before a kickoff.
- **consumes-from** `KICK-aReplayedCard-2` — the single real `READY —` line the append writes.
- **hands-off** `TOOL-aReplayedCard-3` — the deny a resumed run meets, which its kickoff step
  answers.
- **hands-off** external — the unattended driver's own refusals; this deny never reads a run-state
  file and never exempts on a phase.

## 4. Design

### Data model

The predicate, in order, each step returning ALLOW on its own condition:

1. Not a `git commit` command by S1's token rule → allow.
2. `agent_id` present → allow (a subagent's shell calls are never gated).
3. `session_id`, `tool_use_id` or `cwd` missing → allow, silently.
4. No `orientation/` directory under the resolved common dir → allow, one stderr line.
5. A NEW `builds/*/README.md` — staged-added, or untracked and absent from HEAD and index — whose
   bytes carry `authorized-by: prompt` → allow, one stderr line naming the exemption.
6. Card absent, or no `READY —` line beyond the sentinel, or the two normalised toplevels differ →
   DENY.

Step 5 spawns `git diff --cached --name-only --diff-filter=A` and
`git ls-files --others --exclude-standard -- '*/builds/*/README.md'`, and on a hit reads the staged
blob with `git show :<path>` or the worktree file, only after steps 1–4 passed and only when the
card would otherwise deny. The common case pays no spawn.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `checkOriented` | function | `scratch-guard.js` | leads with `check`, a verdict; JS camel per the js cell |
| `readCard` | function | `scratch-guard.js` | leads with `read`, bytes from a named source |
| `resolveToplevel` | function | `scratch-guard.js` | leads with `resolve`, a name to the directory holding `.git` |
| `resolveCommonDir` | function | `scratch-guard.js` | leads with `resolve`, the `.git` file's `gitdir` and `commondir` |
| `COMMIT_SHAPED` | regex constant | `scratch-guard.js` | screaming snake like `TOOLS` |

### Migration

None in this repository: the hook is already wired on `Bash|PowerShell`, and the check is inert
until an `orientation/` directory exists, which the wired writer creates at the next session
start. An adopter of the hooks kit without the kickoff kit never gains the directory and is never
denied; one with both is denied on its first main-loop commit before a kickoff, which is the
designed state.

### Rollout

Lands in this repository at order 3, before the SessionStart writer is wired at order 4. Between
the two commits no `orientation/` directory exists here, so step 4 allows every commit with one
stderr line; the deny arms itself the moment `TOOL-aReplayedCard-2` writes the first card.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/hooks/scratch-guard.js` | the check, four functions, the regex, the header paragraph |
| `tools/hooks/scratch-guard.test.sh` | twelve arms, two of them class arms; `FLOOR_ASSERTIONS` |
| `tools/hooks/README.md` | one section naming the deny, its predicate, its exemption and its ceiling |
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

**Comparing the two toplevels as bytes.** Measured at the synthesis: the writer prints
`C:/…`, the shell's `pwd` prints `/c/…`, node prints `C:\…`; every registered node is Windows plus
Git-Bash, so a byte compare denies the fleet with a green suite. `buildComparablePath` exists in
this file for exactly that fold.

**Reading the card from context rather than disk.** A hook sees the payload, not the transcript;
the file is the only thing it can read.

## 5. Production-readiness checklist

- security — the hook reads one file under the common dir and spawns git with fixed argv; the
  `cwd` is used only to locate `.git`, never interpolated into a shell.
- perf / scale — zero spawns on the common path; two on the exemption path, which is one commit
  per prompt-path run.
- error / empty / loading states — missing fields fail open; a missing writer fails open with a
  line; a missing card denies with the remedy.
- observability — every deny prints the card path and the failed condition; every fail-open on
  step 4 or 5 prints its one line.
- risks — deny-forever if the READY predicate or the path compare is wrong; the cross-kit arm
  feeds the writer's real bytes, and the reason names which condition failed.
- testing — twelve arms, RED first, two of them class arms.
- migration — none.
- user docs — `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `git commit -m x` payload with a `session_id` whose card is
  absent, in a fixture whose common dir holds an `orientation/` directory, the hook exits 2 and
  stderr names the card path and `/session-kickoff`.
  Red when: the check reads the command's prose view and a quoted `commit` word fires it, or the
  deny prints no remedy.
- **AC2** — When the card exists and holds `READY — none yet` only, the hook exits 2 naming the
  missing READY line; when it holds a `READY — t · node a` line and a matching `tree —` cell, the
  hook exits 0.
  Red when: the sentinel satisfies the predicate.
- **AC3** — When the card's `tree —` toplevel names a sibling worktree, the hook exits 2 naming
  both trees.
  Red when: a card written in worktree A opens commits in worktree B.
- **AC4** — When the fixture repository stages a new `README.md` under a `builds/` folder of the
  fixture, carrying `authorized-by: prompt`, and the card has no READY line, the hook exits 0 and
  stderr carries one line naming the exemption.
  Red when: the staged-added check reads the worktree file instead of the staged blob.
- **AC5** — When that same fixture has the folder COMMITTED in HEAD and stages an unrelated file,
  the `git commit -m y` payload exits 2.
  Red when: the exemption keys on the folder's existence and fires on every later commit.
- **AC6** — When the payload carries an `agent_id`, the hook exits 0 with no card at all.
  Red when: a subagent's commit is gated.
- **AC7** — When the payload lacks `session_id`, the hook exits 0 and prints nothing.
  Red when: the fail-open is assumed rather than asserted and a missing field throws to exit 1.
- **AC8** — When the fixture holds an UNTRACKED `README.md` under a `builds/` folder carrying
  `authorized-by: prompt`, nothing staged, and the payload is `git add memory && git commit -m z`,
  the hook exits 0 with the exemption line.
  Red when: the single-call add-and-commit form is denied because the index is empty at PreToolUse.
- **AC9** — When every fenced `git …` command in `skills/session-kickoff/SKILL.md` Steps 0 through
  4, plus the literals `git merge-base origin/main HEAD`, `git merge --ff-only origin/main`,
  `git log --grep push` and `git push origin main`, is fed as a no-card payload, every one exits 0.
  Red when: the remedy the deny names is itself denied, or `merge-base` matches at a word boundary.
  figure: DERIVED — the arm extracts the commands from the engine file at run time.
- **AC10** — When the self-test runs `bash skills/session-kickoff/manifest-check.sh --card --write`
  in its fixture repository, appends a real READY line through `--card --append`, and feeds the
  resulting file unedited with `process.cwd()` as the payload `cwd`, the hook exits 0; with the card
  holding `/c/…` and the payload `C:\…` for one tree, the hook exits 0.
  Red when: the two kits spell the toplevel differently and the compare is on bytes.
- **AC11** — When the fixture's common dir holds no `orientation/` directory, a `git commit`
  payload exits 0 and stderr carries exactly one line naming the unwired writer.
  Red when: a tree without the kickoff kit is denied every commit with a remedy it cannot run.
- **AC12** — When `bash tools/hooks/scratch-guard.test.sh` runs, it prints `PASS` with an
  assertion count at or above the moved `FLOOR_ASSERTIONS`, and a non-commit `ls` payload with no
  card exits 0.
  Red when: an arm is unreachable and the floor did not move.

## 7. Gates

`scratch-guard self-test` · `hook destinations (every declared hook path ships)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/hooks/scratch-guard.test.sh` · a commit payload with no card · `FLOOR_ASSERTIONS`
New arm: `tools/hooks/scratch-guard.test.sh` · a card with only the sentinel · same
New arm: `tools/hooks/scratch-guard.test.sh` · a `tree —` cell naming another worktree · same
New arm: `tools/hooks/scratch-guard.test.sh` · a staged-added prompt-authorized README · same
New arm: `tools/hooks/scratch-guard.test.sh` · the same folder already in HEAD · same
New arm: `tools/hooks/scratch-guard.test.sh` · an `agent_id` payload · same
New arm: `tools/hooks/scratch-guard.test.sh` · a payload with no `session_id` · same
New arm: `tools/hooks/scratch-guard.test.sh` · an untracked prompt-authorized README and a single-call add-and-commit · same
New arm: `tools/hooks/scratch-guard.test.sh` · every fenced git command of the engine's Steps 0–4 and four near-miss literals · same
New arm: `tools/hooks/scratch-guard.test.sh` · the writer's own card, unedited, and the two path spellings · same
New arm: `tools/hooks/scratch-guard.test.sh` · no `orientation/` directory in the common dir · same

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

## 10. Reuse audit

The seam is `tools/hooks/scratch-guard.js` itself — the process, the stdin parse, the string-blanked
command view, `buildComparablePath` at its line 63, and the deny protocol at its lines 370–390 —
and `agent-cap.js`'s `.git` walk at its line 1512 for the common dir, which returns the common dir
and not the toplevel, so the toplevel resolver here is the directory the walk stopped in. `python
tools/codebase-map/reuse_lookup.py "session orientation card written at session start, replayed
after compaction, commit denied until READY"` returned `agent-cap.topLevelArgs` and the
`pre-commit` hook as seams; the pre-commit hook was read and rejected as the home because it sees no
session id, and the PreToolUse payload is the only surface that does.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
