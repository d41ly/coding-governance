# TOOL-aReplayedCard-1 — `scratch-guard.js` denies a `git commit` on an un-oriented card

**Status:** CLOSED · rev-5 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams tooling · order 3 · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md](../build/2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 |
| [2026-09-14-build-TOOL-aReplayedCard-1-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aReplayedCard-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-TOOL-aReplayedCard-1-brief.md](../prompts/2026-09-14-prompt-TOOL-aReplayedCard-1-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make orientation a precondition of the session's first durable act rather than a request. A `git
commit` issued by the main loop is refused, with the remedy in the reason, while the session's card
was written at that session's own start and still holds the writer's sentinel, or names a different
tree. A card that is ABSENT, or that a replay wrote fresh because the session started before the
writer was wired, is allowed: the deny binds sessions that started under the wiring, and no other
session — the landing run included — can be refused by a hook whose remedy it cannot yet run. The
check rides the PreToolUse process that already spawns on every shell call, and compares paths
through the normaliser that process already ships.

## 2. Scope (IN)

- **S1** One check inside `tools/hooks/scratch-guard.js`, after the existing scratch verdict, that
  fires only when the command's string-blanked view holds the argv token `git`, then any number of
  dash-prefixed tokens and, for each of `-C`, `-c`, `--git-dir`, `--work-tree`, `--namespace`,
  `--exec-path` and `--config-env`, the one value token that follows it unless written in the `=`
  form — where a quoted run in the view, `"…"` or `'…'`, whose quote characters survive blanking,
  counts as ONE value token — and then the whole argv token `commit` followed by whitespace or the
  end of the command; so `git -C /c/x commit -m y`, `git -C "C:/p q" commit -m y`,
  `git -c "a=b" commit` and `git -c a=b commit` match, and `git merge-base`,
  `git merge --ff-only origin/main`, `git log --grep commit`, `git commit-tree` and a quoted
  `commit` never do; and the payload carries no `agent_id`. `merge` and `push` are NOT in the set;
  §8 records why. Observed by AC1, AC6 and AC9.
- **S2** The check resolves the commit's toplevel from the `-C` target when the command carries one,
  read from the ORIGINAL command at the offset the view located it — the file's own two-views rule
  and its `readTokenAt` — relative to the payload's `cwd`, else from `cwd` itself. Both the target
  and `cwd` pass through the drive fold `buildComparablePath` already performs, `/x/…` to `x:/…`,
  BEFORE the walk up to the directory holding `.git`, because every registered node writes `git -C`
  paths in the `/c/` spelling node cannot walk; the common dir comes from that `.git` file's
  `gitdir` and `commondir` lines or from the directory itself. A walk that finds no `.git` allows
  with one witness line naming the start directory, because git itself will refuse a commit there.
  The check reads `<git-common-dir>/orientation/<session_id>.md`, tests its header line for
  `--card --replay` (S5) and nothing else — a header naming neither writer is S6's hand-written
  card and proceeds to the READY test rather than earning a third branch — and requires a line
  starting `READY —` whose tail is not the writer's sentinel `none yet`, and a `tree —` cell whose
  toplevel, passed through `buildComparablePath`, equals the resolved toplevel passed through the
  same function. Observed by AC2, AC3, AC9 and AC10.
- **S3** The deny is exit 2 with stderr naming the card path, the condition that failed, and the
  remedy: `/session-kickoff` for the sentinel; `cd <target-tree> && /session-kickoff` for a tree
  mismatch, because `KICK-aReplayedCard-2`'s append rewrites the `tree —` cell to the append's
  PROCESS cwd, and a second real-READY append from the target tree replaces the previous READY line
  and its body rather than adding to it, so the cap is never consumed twice; `KICK-aReplayedCard-2`
  S5 and S10 own both facts and the `consumes-from` edge names them. No waiver clause exists.
  Observed by AC2 and AC3.
- **S4** The prompt-path exemption: when a `README.md` whose path matches
  `/(^|\/)builds\/[^/]+\/README\.md$/` — the one rule — is NEW, either staged as added or untracked
  in the working tree and absent from HEAD and the index, and its bytes carry `authorized-by:`
  followed by a member of the driver's `SECOND_ANCHOR_MODES` set, `prompt` or `recipe` at
  `tools/unattended/unattended.sh:497`, the commit passes without a READY line and stderr carries
  one witness line. The playbook path commits its `recipe` folder before its kickoff exactly as the
  prompt path does, so keying on `prompt` alone deadlocks it. Git runs at the resolved toplevel with
  the pathspec `*builds/*/README.md` as a coarse filter and the rule above selects from what it
  lists, so `rebuilds/z/README.md`, `builds/a/b/README.md` and `docs/README.md` never exempt. The
  condition is the commit that CREATES the authorization, never the presence of such a folder in
  the tree, so the single-call `git add … && git commit` form, whose index is empty at PreToolUse,
  is covered by the untracked arm. The staged blob is read for a staged file and the worktree
  bytes for an untracked one. Observed by AC4, AC5 and AC8.
- **S5** Fail open, silently, when `session_id` or `cwd` is absent from the payload — the two fields
  the predicate reads; `tool_use_id` is not read and is not a condition. Fail open with one witness
  line when no card exists under the resolved common dir for this `session_id`, or when the card's
  header names `--card --replay` as its writer — a card the replay wrote fresh for a session that
  started before the writer was wired, the landing run included. That line is a self-test and
  debug-log witness ONLY: the harness discards stderr on exit 0, so nothing reaches the session, and
  no sentence in this spec claims otherwise. Observed by AC1, AC7 and AC11.
- **S6** The file header states the ceiling: a commit made by a script, a heredoc, a non-git tool,
  a deleted card, a hand-written card, a card the writer refused to write, an unwalkable `-C`
  target, or a session that started before the wiring and never restarted escapes; the guard stops
  forgetting, not evasion; a READY line's presence is asserted, never its correctness; `--git-dir`
  or `--work-tree` pointing outside the resolved tree is compared as the resolved tree; and the
  witness lines on exit 0 depart from the file's "Allow = print nothing" protocol line, which the
  header records as the one difference from `agent-cap.js`. NOT OBSERVED by a criterion: header
  prose.
- **S7** Every arm below is in `tools/hooks/scratch-guard.test.sh`, each observed RED before it
  lands, and `FLOOR_ASSERTIONS` there moves by the number added. The fixture is a scratch
  repository under the suite's existing `mktemp -d`, made by `git init` plus one commit, with
  `git worktree add` of it where an arm needs a linked worktree, so the arms exercise the `.git`
  FILE branch every real session takes; every payload `cwd` is the fixture's path as node spells
  it, read by `node -p process.cwd()` inside the fixture. The arm rule: an ALLOW with a present
  `--write` card asserts stderr byte-EMPTY; an ALLOW on absence, replay origin, an unwalkable
  target or the exemption asserts its one witness line by text; a DENY asserts the card path and
  the remedy by text; the suite gains a `run` variant that greps the captured stderr. Two arms are
  CLASS arms. One extracts every inline code span in `skills/session-kickoff/SKILL.md` Steps 0
  through 4 that begins `git ` — eight at base — plus the Step 1 batch spelled as literals
  (`git fetch`, `git merge --ff-only origin/main`, `git rev-parse HEAD`, `git status --short`,
  `git worktree list`), feeds each as a sentinel-card payload expecting ALLOW with empty stderr,
  asserts the extracted count is at or above a floor stated beside its base figure, and REFUSES on
  zero. The other runs the writer's `--card --write` from the step's base blob —
  `git show <step-3 base sha>:skills/session-kickoff/manifest-check.sh` extracted into the
  fixture, because `KICK-aReplayedCard-2` edits the live file in the same step — from the linked
  worktree, feeds that file with the sentinel in place expecting the sentinel DENY, then with the
  sentinel replaced by a real READY line through the test's own `sed` expecting ALLOW with empty
  stderr, then with the card removed expecting ALLOW with the absence line, so the discriminator is
  observed to move and a spelling fold between the two kits reds here. A parity arm reads
  `SECOND_ANCHOR_MODES` from the driver's source and asserts the hook's accepted bytes equal it.
  Observed by AC9, AC10 and AC12.

## 3. Non-goals (OUT)

- No gating of `Edit`, `Write` or any tool that pays no hook today; the design record's section 6
  prices that at a node spawn per edit.
- No second hook file on the `Bash|PowerShell` matcher; the design record's verdict 13 measured a
  node spawn at 0.8–1.1 s on this node, so a second file doubles every shell call's cost.
- No `merge` and no `push` in the commit-shaped set; §8.
- No deny on an ABSENT or replay-written card; §8.
- No JSON `additionalContext` on an allow. The only model-visible channel on exit 0 is a protocol
  extension nothing in this repository has probed; the witness line is honest about reaching nobody.
- No signature, hash or TTL on the card.
- No `--waive`; owner decision 2.
- No exemption keyed on a folder existing in the tree; §8 records why.
- No second path normaliser; the drive fold is `buildComparablePath`'s own step at
  `scratch-guard.js:63`, applied before the walk as well as before the compare.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card path, the header line naming the writing
  verb, the `tree —` cell's declared spelling, the `READY — none yet` sentinel bytes and the
  `--card --write` verb the cross-kit arm runs from the step's base blob.
- **consumes-from** `KICK-aReplayedCard-2` — the single real `READY —` line the append writes, the
  `tree —` cell it rewrites to its process cwd, and the real-over-real append that replaces the
  previous body; the shipped behaviour, not the self-test, which stands in the sentinel line by
  hand and freezes the writer at the base blob.
- **hands-off** `TOOL-aReplayedCard-3` — the deny a resumed run meets, which its kickoff step
  answers.
- **hands-off** external — the unattended driver's own refusals; this deny never reads a run-state
  file and never exempts on a phase.

## 4. Design

### Data model

The predicate, in order, each step returning ALLOW on its own condition, and this list is the ONE
evaluation order:

1. Not a `git commit` command by S1's token rule → allow.
2. `agent_id` present → allow (a subagent's shell calls are never gated).
3. `session_id` or `cwd` missing → allow, silently.
4. The `-C` target or `cwd`, drive-folded, walks to no `.git` → allow, one witness line.
5. No card for this `session_id` under the resolved common dir, or a card whose header names
   `--card --replay` as its writer → allow, one witness line.
6. The card's only READY line is the sentinel, or the two normalised toplevels differ → evaluate
   step 7; else allow, nothing printed.
7. A NEW README by S4's rule carrying an accepted `authorized-by:` value → allow, one witness line;
   else DENY.

Step 7 alone spawns git — `git diff --cached --name-only --diff-filter=A -- '*builds/*/README.md'`
and `git ls-files --others --exclude-standard -- '*builds/*/README.md'` at the resolved toplevel,
then `git show :<path>` for a staged hit or the worktree bytes for an untracked one — so the common
path pays no spawn, and an adopter with no card never spawns at all.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `checkOriented` | function | `scratch-guard.js` | leads with `check`, a verdict; JS camel per the js cell |
| `readCard` | function | `scratch-guard.js` | leads with `read`, bytes from a named source |
| `resolveToplevel` | function | `scratch-guard.js` | leads with `resolve`, a drive-folded start dir to the directory holding `.git`, or null |
| `resolveCommonDir` | function | `scratch-guard.js` | leads with `resolve`, the `.git` file's `gitdir` and `commondir` |
| `extractCommitTarget` | function | `scratch-guard.js` | leads with `extract`, the `-C` value read from the original via `readTokenAt` |
| `checkAuthorizedReadme` | function | `scratch-guard.js` | leads with `check`, the S4 rule over the listed paths |
| `COMMIT_SHAPED` | regex constant | `scratch-guard.js` | screaming snake like `TOOLS` |
| `GIT_VALUE_FLAGS` | array constant | `scratch-guard.js` | screaming snake; the seven flags that take a value token |
| `ANCHOR_MODES` | array constant | `scratch-guard.js` | screaming snake; `prompt`, `recipe`, pinned to the driver's set by the parity arm |

### Migration

None in this repository: the hook is already wired on `Bash|PowerShell`, and a session with no
card, or a replay-written one, is allowed, so no running session and no landing run is denied by
the file landing or by the wiring that follows it. An adopter of the hooks kit without the kickoff
kit never has a card and is never denied; one with both is denied only on a session that started
under the wiring and never kicked off, which is the designed state.

### Rollout

Lands at order 3. Until `TOOL-aReplayedCard-2` wires the writer at order 4 no session has a card and
every main-loop commit passes with the witness line; after it, a session that started before the
wiring gets a replay-written card at its next compaction and keeps passing, the landing run
included, until it restarts; the sentinel deny binds every session started under the wiring. The
`scratch-guard self-test` leg's guard in `tools/gate-legs.json` gains `skills/session-kickoff/`, so
a move of the sentinel bytes, the `tree —` spelling or the engine's inline spans runs the suite
that reds on it; the manifest moving forces the push boundary's total run.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/hooks/scratch-guard.js` | the check, six functions, three constants, the header paragraph and its protocol note |
| `tools/hooks/scratch-guard.test.sh` | the fixture repository and worktree; the arms in §7, two of them class arms; the stderr-asserting `run` variant; `FLOOR_ASSERTIONS` |
| `tools/hooks/README.md` | one section naming the deny, its grammar, its exemption, its absence and replay rules and its ceiling |
| `tools/gate-legs.json` | `skills/session-kickoff/` in the self-test leg's guard |
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

**Denying on an absent or replay-written card.** The card directory is under the common dir every
worktree on the node shares. A deny on absence refused this build's own landing run from order 3;
a deny on a replay-written sentinel refused it from its first compaction after order 4, with a
remedy that is the primary tree's old engine through the junction until the merge. Both windows
had no exit but the evasions the header names. Resolved in §8.

**Applying the wiring in the landing pass to dodge the window.** It moves the window to the
commits after `--landed`, and a later build hits it again; the replay-origin rule closes it for
every session that started before any wiring, which is the class.

**Comparing the two toplevels as bytes, or walking an unfolded `/c/` path.** Measured at the
synthesis: the writer prints `C:/…`, the shell's `pwd` prints `/c/…`, node prints `C:\…`, and
`path.resolve` turns `/c/x` into `C:\c\x`; every registered node is Windows plus Git-Bash, so a
byte compare denies the fleet and an unfolded walk finds nothing. `buildComparablePath` exists in
this file for exactly that fold.

**Reading the card from context rather than disk.** A hook sees the payload, not the transcript;
the file is the only thing it can read.

## 5. Production-readiness checklist

- security — the hook reads one file under the common dir and spawns git with fixed argv at a
  resolved directory; `cwd` and the `-C` value are used only to locate `.git`, never interpolated
  into a shell.
- perf / scale — zero spawns on the common path; two on the exemption path, which is one commit
  per prompt-path or playbook-path run.
- error / empty / loading states — missing fields fail open silently; a missing, replay-written or
  unlocatable card fails open with a witness line; a sentinel card denies with the card path and the
  remedy; a tree mismatch denies naming both trees and the `cd` form of the remedy.
- observability — every deny prints the card path and the failed condition; the exit-0 witness
  lines reach the debug log and the self-test only, which S5 states.
- risks — deny-forever if the sentinel predicate or the path compare is wrong; the cross-kit arm
  feeds the writer's real bytes from a linked worktree and observes the discriminator move. A
  session that moves trees is denied until it kicks off there, which the append's cell rewrite and
  real-over-real replacement make possible.
- testing — the arms in §7, RED first, on a git fixture with a linked worktree, two of them class
  arms with a refused empty population, one a parity arm on the driver's constant.
- migration — none.
- user docs — `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `git commit -m x` payload with a `session_id` whose card is
  absent, with and without an `orientation/` directory in the fixture's common dir, and again with
  a card whose header names `--card --replay` and whose only READY line is the sentinel, the hook
  exits 0 and stderr carries exactly one witness line naming the absent or replay-written card.
  Red when: an absent or replay-written card denies, so the landing run and every session open
  before the wiring are refused with a remedy they cannot run.
- **AC2** — When a `--write` card exists and holds `READY — none yet` only, the hook exits 2 and
  stderr carries the resolved card path, the word `sentinel` and `/session-kickoff`; when it holds
  a `READY — t · node a` line and a matching `tree —` cell, the hook exits 0 and stderr is empty.
  Red when: the sentinel satisfies the predicate, the deny omits the path or the remedy, or an
  allow prints.
- **AC3** — When B is `git worktree add` of the fixture and the card, written in A, names A in its
  `tree —` cell, a payload from B exits 2 naming both trees and `cd <B> && /session-kickoff`, the
  card having been found from B through B's `.git` FILE; when the cell is then rewritten to B the
  way the append does, the same payload exits 0 with empty stderr.
  Red when: a card written in worktree A opens commits in worktree B, the `.git` file branch fails
  to find the common dir, or a moved session is denied for life with a remedy that cannot change
  the cell.
- **AC4** — When the fixture stages a new `README.md` at `builds/x/` carrying
  `authorized-by: prompt` and the card holds the sentinel, the hook exits 0 with the exemption
  line; the same at `memory/builds/y/`; the same with `authorized-by: recipe`; when the staged blob
  carries the key and the worktree copy is overwritten without it, exit 0; when the staged blob
  lacks the key and the worktree copy carries it, exit 2; when a new `README.md` under `docs/` or
  under `rebuilds/z/` carries the key, exit 2.
  Red when: the worktree bytes are read for a staged file, either depth is missed, `recipe` is
  refused, or a README outside a `builds/<one>/` segment exempts.
- **AC5** — When that same fixture has the folder COMMITTED in HEAD and stages an unrelated file,
  the `git commit -m y` payload exits 2.
  Red when: the exemption keys on the folder's existence and fires on every later commit.
- **AC6** — When the payload carries an `agent_id`, the hook exits 0 with empty stderr on a
  sentinel card.
  Red when: a subagent's commit is gated.
- **AC7** — When the payload lacks `session_id`, or lacks `cwd`, the hook exits 0 and prints
  nothing; when it lacks only `tool_use_id` and the card holds the sentinel, the hook exits 2.
  Red when: a fail-open is assumed rather than asserted, or a field the predicate never reads
  opens the deny.
- **AC8** — When the fixture holds an UNTRACKED `README.md` at `memory/builds/y/` carrying
  `authorized-by: prompt`, nothing staged, the card holds the sentinel, and the payload is
  `git add memory && git commit -m z` issued from a subdirectory `cwd` of the fixture, the hook
  exits 0 with the exemption line.
  Red when: the single-call add-and-commit form is denied because the index is empty at
  PreToolUse, or the spawn runs at the payload `cwd` and lists nothing.
- **AC9** — When every inline code span beginning `git ` in `skills/session-kickoff/SKILL.md` Steps
  0 through 4, plus the five Step 1 literals, plus `git merge-base origin/main HEAD`,
  `git merge --ff-only origin/main`, `git log --grep commit`, `git commit-tree` and
  `git push origin main`, is fed as a sentinel-card payload, every one exits 0 with empty stderr,
  the arm prints the count it extracted, that count is at or above the floor `8` stated beside it,
  and a run over a fixture engine file with no such span exits 1 naming the empty population; and
  `git -C <fixture toplevel in /c/ spelling> commit -m y` from a payload `cwd` OUTSIDE the fixture,
  `git -C "<fixture toplevel>" commit -m y`, `git -c a=b commit` and `git -c "a=b" commit` fed the
  same way exit 2, while the first of them fed with a real READY card whose cell is the fixture
  exits 0 with empty stderr, and `git -C /nowhere/x commit` exits 0 with the unwalkable line.
  Red when: the remedy the deny names is itself denied, `merge-base` or `commit-tree` matches at a
  word boundary, a quoted value swallows the `commit` token, the `/c/` spelling walks to nothing
  and falls back to the payload's tree, or an empty extraction passes.
  figure: DERIVED — the arm extracts the spans from the engine file at run time; the floor is
  PINNED at the base measurement of 8.
- **AC10** — When the self-test extracts `skills/session-kickoff/manifest-check.sh` at the step's
  base blob into the fixture and runs its `--card --write` from the fixture's linked worktree, the
  hook fed that file unchanged, with the worktree's `node -p process.cwd()` as the payload `cwd`,
  exits 2 naming the sentinel and the card path; fed the same file with the sentinel line replaced
  by a real READY line through `sed`, exits 0 with empty stderr; fed with the card removed, exits 0
  with the absence line; and with the card holding `/c/…` and the payload `C:\…` for one tree,
  exits 0 with empty stderr.
  Red when: the two kits spell the toplevel differently and the compare is on bytes, the card at
  the writer's path is never read, or the arm is green by absence.
- **AC11** — When this repository's `git rev-parse --git-common-dir` is listed from the test's cwd
  after the whole self-test, no `orientation/sgtest-*` entry is present, `sgtest-` being the
  session-id prefix every arm uses; and the parity arm reports the hook's accepted
  `authorized-by:` values equal `SECOND_ANCHOR_MODES` read from `tools/unattended/unattended.sh`.
  Red when: a fixture card is left in the shared common dir, or a third mode reaches one reader and
  not the other.
- **AC12** — When `bash tools/hooks/scratch-guard.test.sh` runs, it prints `PASS` with an
  assertion count at or above the moved `FLOOR_ASSERTIONS`, and a non-commit `ls` payload with a
  sentinel card exits 0 with empty stderr.
  Red when: an arm is unreachable and the floor did not move.

## 7. Gates

`scratch-guard self-test` · `hook destinations (every declared hook path ships)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene` · `run-gates canary`

New arm: `tools/hooks/scratch-guard.test.sh` · an absent card with and without the directory, and a replay-written sentinel card · `FLOOR_ASSERTIONS`
New arm: `tools/hooks/scratch-guard.test.sh` · a `--write` card with only the sentinel, asserting the path and the remedy · same
New arm: `tools/hooks/scratch-guard.test.sh` · a linked worktree B whose card names A, then the cell rewritten to B · same
New arm: `tools/hooks/scratch-guard.test.sh` · a staged-added authorized README at two depths and both modes, the staged-versus-worktree pair, and two out-of-rule READMEs · same
New arm: `tools/hooks/scratch-guard.test.sh` · the same folder already in HEAD · same
New arm: `tools/hooks/scratch-guard.test.sh` · an `agent_id` payload · same
New arm: `tools/hooks/scratch-guard.test.sh` · payloads lacking `session_id`, lacking `cwd`, and lacking only `tool_use_id` · same
New arm: `tools/hooks/scratch-guard.test.sh` · an untracked authorized README and a single-call add-and-commit from a subdirectory · same
New arm: `tools/hooks/scratch-guard.test.sh` · every inline git span of the engine's Steps 0–4, the batch literals, five near-miss literals, four value-flag hits, one `/c/` fold, one unwalkable target, and an empty fixture engine · same
New arm: `tools/hooks/scratch-guard.test.sh` · the writer's own card from the base blob in a linked worktree: sentinel deny, `sed` allow, removed-card allow, two path spellings · same
New arm: `tools/hooks/scratch-guard.test.sh` · the shared common dir after the run, and the `SECOND_ANCHOR_MODES` parity · same
New arm: `tools/hooks/scratch-guard.test.sh` · a non-commit payload with a sentinel card · same

The full bar is owed with `GATE_SELFTESTS=1`. The `tools/gate-legs.json` edit moves the manifest,
which the push boundary treats as forcing a total run.

## 8. Open questions

- **The exemption's key.** The owner's answer reads "the hook checks the cwd for a build folder
  with `authorized-by: prompt`". Read literally, every commit in this repository is exempt, because
  landed prompt-path builds leave such folders in the tree, and the prompt's own acceptance line
  "a commit without READY denied with the remedy in the reason" cannot then be met. The only
  reading under which both the owner's decision and the acceptance survive is the commit that
  CREATES the authorization: a NEW `builds/*/README.md`, staged-added or untracked, whose bytes
  carry the key. RESOLVED (agent, 2026-09-13, delegated): the new-README reading, S4, with AC5 as
  the arm that proves the literal reading is not what shipped and AC8 as the arm for the
  single-call form. The accepted bytes are the driver's own set, `prompt` and `recipe`, because the
  playbook path commits before its kickoff exactly as the prompt path does and the owner's question
  named only the path that was asked about.
- **The commit-shaped set.** The prompt names "commit-shaped" and the design record spelled
  `commit|merge|push`. The round-1 audit showed the engine's own Step 1 fast-forward is a
  `git merge --ff-only` made before any READY line, so the deny would refuse its own remedy, and
  the unattended prompt path pushes its build folder before the preflight that permits a kickoff,
  so owner decision 3 would be defeated at the push. The acceptance line names a COMMIT. RESOLVED
  (agent, 2026-09-13, delegated): the set is `commit` alone, S1; a push carries commits already
  gated at commit time and the lander runs the bar at the push boundary; AC9 is the arm that keeps
  the engine's fast-forward and the near-miss spellings allowed.
- **An absent or replay-written card.** The prompt's acceptance line reads "a commit without READY
  denied". The round-2 audit showed a deny on ABSENCE refuses this build's own landing run from
  order 3; the round-3 audit showed a deny on a REPLAY-WRITTEN sentinel refuses it from its first
  compaction after the wiring lands at order 4, with a remedy that is the primary's old engine
  through the junction until the merge. Both windows had no bootstrap but the evasions the header
  names. The line is satisfied by the sentinel deny on a session that started under the wiring: a
  session whose writer ran at its start and who never kicked off is refused; a session whose writer
  never ran, or ran only as a replay, is allowed, and the witness line reaches the debug log and
  the self-test, not the session. RESOLVED (agent, 2026-09-14, delegated): S5's absence and replay
  rules, AC1, and the honest statement of the witness channel.

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
- rev-4 · 2026-09-14 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · S1 · S2 · S3 · S4 · S5 · S6 · S7 ·
  AC1 · AC2 · AC3 · AC4 · AC7 · AC8 · AC9 · AC10 · AC11 · AC12 · folded the round-3 spec audit,
  the loop's NON-CONVERGENT exit with disposition FOLD. A replay-written sentinel card allows like an
  absent one, so the landing run's first compaction after the wiring cannot deny it, and the
  sentinel deny binds sessions started under the wiring (B1, third §8 mark reworded); the `-C`
  target and `cwd` are drive-folded before the walk, an unwalkable target allows with a witness
  line, and AC9 observes the fold on the fixture's own `/c/` spelling (H1); a quoted value is one
  token and the target is read from the original via `readTokenAt`, with two quoted DENY literals
  (H2); every present-card allow asserts empty stderr, AC10 gains its sentinel twin and its
  removed-card control, and the suite gains a stderr-asserting `run` variant (H3); the witness line
  is stated to reach the debug log only and the header records the departure from the print-nothing
  protocol (H4); the accepted bytes are the driver's `SECOND_ANCHOR_MODES`, `prompt` and `recipe`,
  with a parity arm (H5); the fixture is a scratch repository with a linked worktree, payload `cwd`
  as node spells it, and AC11 names the `sgtest-` prefix (M1, M9); the README rule is one regex
  over the pathspec's listing, with two out-of-rule arms (M2); AC4 gains the staged-versus-worktree
  pair (M3); the cross-kit arm runs the writer from the step's base blob (M4); the second
  real-READY append replaces the body and the edge names it (M5); the tree-mismatch remedy is the
  `cd` form and the cell follows the append's process cwd (M6); the self-test leg's guard gains
  `skills/session-kickoff/` (M7); one evaluation order, absence before the exemption (M8); the
  card path is asserted in AC2, a no-`cwd` payload in AC7, and `git log --grep commit` plus
  `git commit-tree` in AC9 (L1, L2, L3).
- rev-5 · 2026-09-14 · S2 · the build pass. The header is tested for `--card --replay` only: a
  card whose header names neither writer proceeds to the READY test, because a third branch for a
  hand-written card would decide nothing S6 does not already concede, and `--card --write` as a
  REQUIRED spelling buys nothing a hand-written card cannot forge in one line. Every `-C` value in
  the matched span is resolved in order, the superset of "the `-C` target". The deny and the
  witness lines print the card path in `buildComparablePath`'s form, the one spelling the self-test
  can compute from the hook's own export. Status CLOSED.

## 10. Reuse audit

The seam is `tools/hooks/scratch-guard.js` itself — the process, the stdin parse, the string-blanked
command view and its two-views rule with `readTokenAt` at lines 190–210, `buildComparablePath` at
line 63 whose drive fold serves the walk as well as the compare, and the deny protocol at lines
370–390 — and `agent-cap.js`'s `.git` walk at line 1512 for the common dir, which returns the
common dir and not the toplevel, so the toplevel resolver here is the directory the walk stopped in.
The accepted `authorized-by:` set is the driver's `SECOND_ANCHOR_MODES` at
`tools/unattended/unattended.sh:497`, pinned by a parity arm rather than restated. `python
tools/codebase-map/reuse_lookup.py "session orientation card written at session start, replayed
after compaction, commit denied until READY"` returned `agent-cap.topLevelArgs` and the
`pre-commit` hook as seams; the pre-commit hook was read and rejected as the home because it sees no
session id, and the PreToolUse payload is the only surface that does. The empty-population refusal
reuses `tools/check-hook-destinations.sh`'s shape at its lines 27–35.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
