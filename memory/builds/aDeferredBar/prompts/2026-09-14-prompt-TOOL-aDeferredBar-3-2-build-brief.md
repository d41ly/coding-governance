# Build brief — TOOL-aDeferredBar-3

**Serves:** journal TOOL-aDeferredBar-3

The pass this brief is handed to builds unit 3 of `aDeferredBar` at rev-3. The spec is
`memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-3.md` and it is authoritative;
this brief adds only what the spec cannot carry — what two audit rounds settled, what units 1 and 2
left in the tree, and the rules the pass itself is bound by.

## What the pass builds

`tools/unattended/gate-guard.js`, a `PreToolUse` hook on `Bash|PowerShell` that denies a full bar
or a self-test suite while the current branch's run is in a phase before `VERIFYING`; the
`run-branch:` fact `--preflight` writes on both anchors, as fact 13 of the protocol; the fragment
and the settings wiring, LAST; the withheld suite with its descriptor and budget rows; the
adopter's `--check` arm; the corpus measurement; the prose carriers and the kit version step. The
spec's §4 files table is the write set; declare it with `--dispatch` BEFORE the first edit.

## What the audits and the two landed units already decided, so the pass does not reopen it

- **Every criterion is one payload fed to the hook** — `printf '%s' "$P" | node "$HOOK"; echo
  "rc=$?"` — exit code and stderr asserted, the row's command in prose. The suite is named in prose
  and on `New arm:` lines only. Its `PASS (<n> assertions)` and the `PHASES_CORE` parity arm are
  returned in `summary` for the main loop at `VERIFYING`.
- **S4 is the LAST step.** Wire `.claude/settings.json` with `python tools/settings-merge.py
  --fragment tools/unattended/gate-guard.fragment.json` only after every hook-fed observation has
  been made; settings are re-read mid-session, so the hook is live from that moment, and this
  run's record is at `BUILDING` on this branch — the hook will then deny the shapes it exists to
  deny for the rest of your pass. The observations that follow S4 (AC7, AC8, AC12, AC13, AC15) are
  greps and checkers that carry no deny shape.
- **The key**: `run-branch:` first, `branch-ref:` fallback; the per-worktree `HEAD` read from the
  `.git` file-or-directory without spawning git; `MEMORY_ROOT` from `.unattended.conf`. Two stale
  `BUILDING` records on `main` (`aUnblockedFleet`, `aClosedDocket`) are on other branches and must
  key nothing — an arm asserts it.
- **`run-branch:` is written beside the `anchor-kind` pin** (`unattended.sh` near line 2724) on
  both anchors, with the value of `git symbolic-ref HEAD`; the driver-suite arm asserts against
  the fixture's own `$(git symbolic-ref HEAD)`, never a literal. The protocol is 57815 bytes of a
  61440-byte cap and 666 of 750 lines; fact 13 fits. Check 10 of `check-unattended.sh` is the
  protocol pair gate.
- **The allow set is the tail of `PHASES_CORE` from `VERIFYING`**, spelled in the hook with the
  comment saying so; `check-unattended.sh` refuses a restated SET (its lines 374–390), not a
  literal — the spec's FACT-QUESTION is decided by running that checker once the file exists.
- **The empty assignment `GATE_FULL=` is the plain bar** (row D1) and unit 2's join agrees; a
  `*.test.sh` basename as a `grep` argument is allowed (AC5); the deny shapes after `&&` and
  `then` are denied (AC2).
- **Kit versions in the tree now**: unattended `1.20` (unit 1), memory-tree `2.76` (unit 2). Your
  step is unattended `1.20` → `1.21` in every carrier that spells it — four `.sh` constants and the
  renders included, fifteen carriers at unit 1's count; AC8's count is DERIVED by its grep.
- **The manifest is 155 bytes under its 25600-byte cap** and C7 says trim, never raise. Your S8
  trap line must fit; if it does not, trim a duplicated trap rather than the cap, and record it.
  Both stamps move: `last-audit` (merge-base sha) and `last-body-change` (the commit's parent).
- **`memory/map/generated/symbols.json`** is re-rendered by `python tools/codebase-map/gen_map.py
  --write` after the hook lands, because the `kit-js` layer enumerates the new file's definitions;
  `python tools/codebase-map/test_codebase_map.py` is the observation.
- **AC10's precondition**: seed, run the adopter install with no verb inside `FIX`, THEN remove
  `.claude/settings.json`, THEN `--check` — the first `--check` arm exits 1 on a seed-only tree for
  a reason that is not the hook.
- **The corpus** is `~/.claude/projects/C--projects-coding-governance*/**/*.jsonl`; each `Bash` /
  `PowerShell` `tool_use` carries `input.command` and the record's `isSidechain` flag. The research
  record's section 2 holds the first-cut probe and its counts; measure the SHIPPED predicate with
  its string-blanked view and record hits AND near-misses in the unit's build record (S7, AC11).

## The rules this pass is bound by

- **No merge bar, no self-test suite, no `GATE_*=` prefix, no `run-selftests.sh`, no
  `run-unattended-gates.sh` in this pass** — the hook you are writing will refuse them once wired,
  and the build README's fifth rule refuses them before that. The hook's own failing case is
  observed RED by the fixture: a record at `BUILDING` on the fixture's branch and the command
  `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` → exit 2 and the deny text.
- Function names from the declared verb table — `check…`, `read…`, `build…`, `resolve…`,
  `render…` as `scratch-guard.js` uses them; run `python tools/lexicon/lexicon.py --suggest <name>
  --as js.function` before naming anything else. No `tools/` literal in the hook: the conf key and
  the record basename are the only spellings.
- Author with Write/Edit, never a heredoc into a file: a backslash escape dies one layer in and the
  symptom never looks like quoting.
- Commit ONCE at the end of the pass with the unit id in the subject; flip the spec's status header
  to CLOSED in that same commit; write the acceptance ledger under `build/` per `memory/HYGIENE.md`
  "Acceptance ledger", one line per AC, `**Serves:** journal TOOL-aDeferredBar-3`. The `--brief`
  row for this brief and the `--dispatch` declaration are recorded before the commit.
- Then run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names
  before returning.

## What the pass must not do

- No edit to `tools/check-spec-tokens.py`, `.memory-tree.conf`, `tools/memory-tree/*` — units 1
  and 2 own them and both are CLOSED.
- No edit to `tools/hooks/*` — the hook lives in the unattended kit for the literal-ban reason the
  spec records.
- No edit to `memory/DECISIONS.md` or `memory/backlog/*.md` — shared records, main-loop only.
- No change to the phase vocabulary, no new leg on the bar, no ceiling re-declared.
- No widening of scope: a beneficial discovery goes in `summary` for the main loop to `--rescope`.
