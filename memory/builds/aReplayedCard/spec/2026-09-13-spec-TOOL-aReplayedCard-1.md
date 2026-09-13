# TOOL-aReplayedCard-1 — `scratch-guard.js` denies a commit-shaped command with no READY line

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make orientation a precondition of the session's first durable act rather than a request. A `git
commit`, `git merge` or `git push` issued by the main loop is refused, with the remedy in the
reason, until the session's card carries a `READY —` line written in this tree. The check rides
the PreToolUse process that already spawns on every shell call, so it costs no second node spawn.

## 2. Scope (IN)

- **S1** One check inside `tools/hooks/scratch-guard.js`, after the existing scratch verdict, that
  fires only when the command's string-blanked view matches a commit-shaped git invocation —
  `git` followed by `commit`, `merge` or `push` as a word — and the payload carries no `agent_id`.
  Observed by AC1 and AC6.
- **S2** The check reads `<git-common-dir>/orientation/<session_id>.md`, resolving the common dir
  from the payload's `cwd` by the same `.git` walk `agent-cap.js` already implements, and requires
  a line starting `READY —` and a `tree —` cell whose toplevel equals the toplevel derived from
  `cwd`. Observed by AC1, AC2 and AC3.
- **S3** The deny is exit 2 with stderr naming the card path, the condition that failed, and the
  one remedy, `/session-kickoff`. No waiver clause exists. Observed by AC1 and AC2.
- **S4** The prompt-path exemption: when the staged set adds a `README.md` under a `builds/`
  segment whose staged blob carries `authorized-by: prompt`, the commit passes without a READY
  line and stderr says so in one line. The condition is the commit that CREATES the authorization,
  never the presence of such a folder in the tree. Observed by AC4 and AC5.
- **S5** Fail open, silently, when `session_id`, `tool_use_id` or `cwd` is absent from the payload,
  mirroring the hook's existing posture. Observed by AC7.
- **S6** The file header states the ceiling: a commit made by a script, a heredoc, a non-git tool
  or a hand-written card escapes; the guard stops forgetting, not evasion; and a READY line's
  presence is asserted, never its correctness. NOT OBSERVED by a criterion: header prose.
- **S7** Every arm below is in `tools/hooks/scratch-guard.test.sh`, each observed RED before it
  lands, and `FLOOR_ASSERTIONS` there moves by the number added. Observed by AC8.

## 3. Non-goals (OUT)

- No gating of `Edit`, `Write` or any tool that pays no hook today; the design record's section 6
  prices that at a node spawn per edit.
- No second hook file on the `Bash|PowerShell` matcher; the design record's verdict 13 measured a
  node spawn at 0.8–1.1 s on this node, so a second file doubles every shell call's cost.
- No signature, hash or TTL on the card.
- No `--waive`; owner decision 2.
- No exemption keyed on a folder existing in the tree; §8 records why.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card path, the `tree —` cell and the
  `READY — none yet` sentinel; without the card every main-loop commit is denied, which is the
  intended state before a kickoff and the reason `TOOL-aReplayedCard-2` wires the writer first.
- **consumes-from** `KICK-aReplayedCard-2` — the single real `READY —` line the append writes.
- **hands-off** `TOOL-aReplayedCard-3` — the deny a resumed run meets, which its kickoff step
  answers.
- **hands-off** external — the unattended driver's own refusals; this deny never reads a run-state
  file and never exempts on a phase.

## 4. Design

### Data model

The predicate, in order, each step returning ALLOW on its own condition:

1. Not a commit-shaped command → allow.
2. `agent_id` present → allow (a subagent's shell calls are never gated).
3. `session_id`, `tool_use_id` or `cwd` missing → allow, silently.
4. Staged set adds a `builds/*/README.md` whose staged blob carries `authorized-by: prompt` →
   allow, one stderr line naming the exemption.
5. Card absent, or no `READY —` line, or `tree —` toplevel differs from `cwd`'s → DENY.

Step 4 spawns `git diff --cached --name-only --diff-filter=A` and, on a hit, `git show :<path>`,
only after steps 1–3 passed and only when the card would otherwise deny. The common case pays no
spawn.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `checkOriented` | function | `scratch-guard.js` | leads with `check`, a verdict; JS camel per the js cell |
| `readCard` | function | `scratch-guard.js` | leads with `read`, bytes from a named source |
| `resolveCommonDir` | function | `scratch-guard.js` | leads with `resolve`, a name to the thing it denotes |
| `COMMIT_SHAPED` | regex constant | `scratch-guard.js` | screaming snake like `TOOLS` |

### Migration

None. The hook is already wired on `Bash|PowerShell`; the check is inert until a card directory
exists, and a repository with no card at all is denied on its first main-loop commit, which is the
designed state — `TOOL-aReplayedCard-2` orders the writer's wiring before this file lands in an
adopter.

### Rollout

Lands in this repository at order 3, before the SessionStart writer is wired at order 4. Between
the two commits, a main-loop commit in a fresh session of this repository would be denied; the run
writes its own card by hand-invoking `--card` and running a kickoff, which is the same act the wiring
automates. The build record notes the window.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/hooks/scratch-guard.js` | the check, three functions, the regex, the header paragraph |
| `tools/hooks/scratch-guard.test.sh` | eight arms; `FLOOR_ASSERTIONS` |
| `tools/hooks/README.md` | one section naming the deny, its predicate and its ceiling |
| `memory/map/features/agent-cap.md` | dossier refresh on touch |

### Alternatives rejected

**A new `orientation-guard.js`.** Doubles the per-call spawn cost; verdict 13.

**Keying the exemption on the payload `cwd` holding any prompt-authorized build folder.** Every
landed prompt-path build in this repository leaves such a folder, so the exemption would fire on
every commit forever and the deny would never fire; the acceptance line "a commit without READY
denied" could not be met. Resolved in §8.

**Reading the card from context rather than disk.** A hook sees the payload, not the transcript;
the file is the only thing it can read.

## 5. Production-readiness checklist

- security — the hook reads one file under the common dir and spawns git with fixed argv; the
  `cwd` is used only to locate `.git`, never interpolated into a shell.
- perf / scale — zero spawns on the common path; two on the exemption path, which is one commit
  per prompt-path run.
- error / empty / loading states — missing fields fail open; a missing card denies with the remedy.
- observability — every deny prints the card path and the failed condition.
- risks — deny-forever if the READY predicate is wrong; the self-test arms exercise every branch
  and the reason names which failed.
- testing — eight arms, RED first.
- migration — none.
- user docs — `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `git commit -m x` payload with a `session_id` whose card is
  absent, the hook exits 2 and stderr names the card path and `/session-kickoff`.
  Red when: the check reads the command's prose view and a quoted `commit` word fires it, or the
  deny prints no remedy.
- **AC2** — When the card exists and holds `READY — none yet` only, the hook exits 2 naming the
  missing READY line; when it holds a `READY — t · node a` line and a matching `tree —` cell, the
  hook exits 0.
  Red when: the sentinel satisfies the predicate.
- **AC3** — When the card's `tree —` toplevel names a sibling worktree, the hook exits 2 naming
  both trees.
  Red when: a card written in worktree A opens commits in worktree B.
- **AC4** — When the fixture repository stages a new `README.md` under a `builds/` folder of the fixture, carrying
  `authorized-by: prompt`, and the card has no READY line, the hook exits 0 and stderr carries one
  line naming the exemption.
  Red when: the staged-added check reads the worktree file instead of the staged blob.
- **AC5** — When that same fixture has the folder COMMITTED in HEAD and stages an unrelated file,
  the `git commit -m y` payload exits 2.
  Red when: the exemption keys on the folder's existence and fires on every later commit.
- **AC6** — When the payload carries an `agent_id`, the hook exits 0 with no card at all.
  Red when: a subagent's commit is gated.
- **AC7** — When the payload lacks `session_id`, the hook exits 0 and prints nothing.
  Red when: the fail-open is assumed rather than asserted and a missing field throws to exit 1.
- **AC8** — When `bash tools/hooks/scratch-guard.test.sh` runs, it prints `PASS` with an
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

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

- **The exemption's key.** The owner's answer reads "the hook checks the cwd for a build folder
  with `authorized-by: prompt`". Read literally, every commit in this repository is exempt, because
  landed prompt-path builds leave such folders in the tree, and the prompt's own acceptance line
  "a commit without READY denied with the remedy in the reason" cannot then be met. The only
  reading under which both the owner's decision and the acceptance survive is the commit that
  CREATES the authorization: a staged-added `builds/*/README.md` whose staged blob carries the key.
  RESOLVED (agent, 2026-09-13, delegated): the staged-added reading, S4, with AC5 as the arm that
  proves the literal reading is not what shipped.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is `tools/hooks/scratch-guard.js` itself — the process, the stdin parse, the string-blanked
command view and the deny protocol at its lines 370–390 — and `agent-cap.js`'s `.git` walk for the
toplevel. `python tools/codebase-map/reuse_lookup.py "session orientation card written at session
start, replayed after compaction, commit denied until READY"` returned `agent-cap.topLevelArgs` and
the `pre-commit` hook as seams; the pre-commit hook was read and rejected as the home because it
sees no session id, and the PreToolUse payload is the only surface that does.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
