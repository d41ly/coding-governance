# TOOL-dGroundRules-73 — a missing default-branch ref refuses with its own remedy, never rule 7's settings remedy

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-73-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-73-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-73-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-73-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md](../reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md) | diff-review | TOOL-dGroundRules-72 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 |

<!-- /gen:spec-records -->

## 1. Goal

A repository whose default branch is not `main` and that has no `refs/remotes/<remote>/HEAD` names
no landed revision. That is what `git init` and a first push leave behind. Every policy read then
refuses with `<ref> names no commit in this repository`, which does not say why `main` was read or
how to name the real branch. Agent-cap rule 7 wraps that refusal in its settings denial, so every
`Agent` and `Workflow` call is denied and told to run `policy.py settings --write`, which changes
nothing. This unit keeps the refusal, since guessing a branch would be worse. The reader and the
shim name the missing ref and the remedy, and rule 7 prints a refused read under its own text. The
two help pages document `origin/HEAD` and `GOV_DEFAULT_BRANCH`, and a policy fixture case covers the
whole path.

## 2. Scope (IN)

- **S1** — The reader's refusal. In `tools/policy/policy.py`, `derive_landed_revision` gives its
  Refusal the matching line of §4 "The two refusal lines" when the ladder named no branch and the
  `main` it falls back to names no commit. Every other outcome of the function is unchanged, the `how` string
  included. Its docstring says so in one sentence. Observed by AC1.
- **S2** — The shim's refusal. In `tools/policy/policy-shim.sh`, the `landed` verb prints the same
  line as S1, byte for byte, under the same condition. Its header comment says so in one sentence.
  Observed by AC2.
- **S3** — Rule 7's denial for a refused read. In `tools/hooks/agent-cap.js`, `checkSettingsInForce`
  answers a `PolicyRefusal` from `readPolicy` with the denial §4 "Rule 7's refused-read denial"
  gives. That denial does not name `settings --write`. Every settings denial keeps its present text.
  The comment block above `SETTINGS_VARS` gains one sentence. Observed by AC4.
- **S4** — The help pages. `help/policy.md` and `help/agent-limit.md` document `origin/HEAD`,
  `git remote set-head <remote> -a` and `GOV_DEFAULT_BRANCH`, and the refused-read denial, as §4
  "The help pages" gives. Observed by AC5.
- **S5** — The fixture case. In `tools/policy/check_policy.py`, the `limit-` outcome cases gain
  `limit-hook-landed-unread`, as §4 "The fixture case" gives. It is added to `LIMIT_CASES`, to the
  module docstring and to the case paragraph of `tools/policy/README.md`. Observed by AC6.
- **S6** — The parity arm. In `tools/policy/check_policy.py`, `run_mirror_landed_parity` adds a
  fifth state, `no remote, on master`, and compares a refused state's whole line, as §4 "The parity
  arm" gives. Its docstring, the module docstring's case line and the parity sentence of
  `tools/policy/README.md` say five states. Observed by AC3.

## 3. Non-goals (OUT)

- Guessing the default branch from `init.defaultBranch`, from the current branch or from a fetch.
  The skeptic judged the finder's fix UNSOUND for that reason.
- The text of any other refusal. That covers a ladder refusal, a `GOV_DEFAULT_BRANCH` that names
  no ref, an observed branch that was never fetched, and a `--rev` that names no commit.
- Rule 7's settings denials and their `settings --write` remedy, which name the right fix. So
  `tools/hooks/agent-cap.test.sh:1203` and the `limit-hook-settings-over` case keep passing as they
  are.
- The non-integer limit denial at `tools/hooks/agent-cap.js:1802`, and the header comment of
  `agent-cap.js`, which `TOOL-dGroundRules-78` amends (L1).
- `tools/hooks/README.md` and the revision bullet of `tools/policy/README.md`. Both stay true: the
  hooks README says a refused policy read refuses with its line, and the policy README names the
  ladder and its `main` fallback.
- The `## Install` section of `help/policy.md`, which a policy fixture parity reads
  (`tools/policy/check_policy.py:1353-1371`).
- `KIT_AGENT_CAP_VERSION`. Units 10, 18, 21 and 61 changed rule 7 without a bump.
- The policy fixtures leg's budget and ceiling, which `TOOL-dGroundRules-78` re-measures (M4). The
  case S5 adds is a few seconds of that run.
- The rule that every hook denial path has a fixture asserting its remedy for each cause (§7).
- The other findings of the report, and the inherited reds the close recorded: unattended shards 1,
  3, 5 and 7, and the hygiene partition arm.

### Edges

none

This unit repairs what `TOOL-dGroundRules-5` (the shim and the mirror helper) and
`TOOL-dGroundRules-10` (rule 7) built, and changes nothing else either unit built.

## 4. Design

### Evidence

Measured at `fce5603f8`. `derive_landed_revision` (`tools/policy/policy.py:471-482`) takes the
ladder's branch, then sets `branch = branch or "main"` at `:480`. It reads
`refs/remotes/<remote>/<branch>`, or `refs/heads/<branch>` when the ladder names no remote, through
`resolve_commit` (`:462-468`). That function raises `Refusal(POLICY_REL, 0, "<rev> names no commit
in this repository")`. The ladder's branch is `GOV_DEFAULT_BRANCH`, else what `<remote>/HEAD`
names (`:415`). The shim does the same at `tools/policy/policy-shim.sh:104-106`, its branch
`RR_BRANCH` from `:64`. `runShim` in `tools/policy/policy-mirror.js:83` passes an exit-2
`policy: refused · ` line through as a `PolicyRefusal`. `checkSettingsInForce`
(`tools/hooks/agent-cap.js:1779`) catches that refusal at `:1799` and hands it to
`renderSettingsDeny` (`:1788-1792`), whose remedy is `policy.py settings --write` (`:1787`).

The probe copied the hooks kit and the policy kit into scratch repositories with a limit of 2 and
settings at 2 (§5, `f73.sh`). Its results:

- A repository on `master` with no remote: `policy.py get runtime.agents-in-flight` and
  `policy-shim.sh landed` each exit 2 with
  `policy: refused · .governance/policy.toml:0 · refs/heads/main names no commit in this repository`.
  The hook denies, exit 2, with the settings header, that line, and
  `Render them from the policy: python kits/policy/policy.py settings --write, ...`.
- The same repository under `GOV_DEFAULT_BRANCH=master`: the hook exits 0.
- A repository on `master` pushed to one bare remote, which leaves no `refs/remotes/origin/HEAD`:
  the same denial, naming `refs/remotes/origin/main`. After `git remote set-head origin -a` the hook
  exits 0.
- A control on `main` with no remote: the hook exits 0.

So the premise holds at HEAD, in both the remote and the no-remote case.

### The two refusal lines

The remedy applies only on the fallback path: the ladder named no branch, because
`GOV_DEFAULT_BRANCH` is unset or empty and `<remote>/HEAD` names none, and the `main` ref names no
commit. A ladder refusal, or a branch the ladder did name, keeps its present text. Each line is the
Refusal's `why`, after `policy: refused · .governance/policy.toml:0 · `. `<R>` is the resolved
remote, joined at run time:

```
refs/remotes/<R>/main names no commit in this repository, and main is only the fallback: refs/remotes/<R>/HEAD names no branch and GOV_DEFAULT_BRANCH is unset. Name the default branch: git remote set-head <R> -a, or export GOV_DEFAULT_BRANCH=<branch>.
refs/heads/main names no commit in this repository, and main is only the fallback: this clone has no remote and GOV_DEFAULT_BRANCH is unset. Name the local default branch: export GOV_DEFAULT_BRANCH=<branch>.
```

`<branch>` is literal text. The reader does not guess the branch, so the remedy does not either.

In `derive_landed_revision`, the `not branch` test is taken before the fallback. A `resolve_commit`
Refusal on that path is raised again with the why above. The shim builds the same why in a
variable when `RR_BRANCH` is empty, and prints it in its existing `printf` at `:106`. Neither line
spells a remote by name. The code joins `remote`, or `$RR_REMOTE`, so
`tools/check-remote-literals.sh` (shape 5, `set-head` then the name) has nothing to match. Neither
line carries `Name it: export GOV_REMOTE=<remote>.`, the phrase the `budgets-reader-refused` case
counts (`tools/policy/check_policy.py:3690`).

### Rule 7's refused-read denial

At `tools/hooks/agent-cap.js:1799`, a `PolicyRefusal` returns this denial and not
`renderSettingsDeny`. It is two lines, and `<tool>` is `data.tool_name`:

```
BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this <tool> call — the landed agent limit cannot be read, so the settings in force were not compared, and a rule that cannot read does not admit. Clear the policy reader's refusal, which names its cause:
  <the PolicyRefusal's message>
```

It is a sibling arrow beside `renderSettingsDeny`, built from the same `data.tool_name`. A throw
that is not a `PolicyRefusal` still reaches `main`'s threw denial (`:1890-1892`). The writer split's
limit read at `:469` already prints `e.message`, so it carries S1's and S2's remedy unchanged.

### The help pages

- `help/policy.md`, the **Read a key** bullet (`:29-34`). The landed revision is the tip of the
  branch `refs/remotes/<remote>/HEAD` names. A clone sets that ref, and
  `git remote set-head <remote> -a` sets it after a first push. `export GOV_DEFAULT_BRANCH=<branch>`
  names the branch outright. With no remote it is the local branch `GOV_DEFAULT_BRANCH` names. When
  neither names one, `main` is the fallback. A repository with no `main` refuses, naming the
  missing ref and these remedies. A sub-bullet after the `GOV_REMOTE` one (`:42`) says the same in
  one line.
- `help/agent-limit.md`, after the paragraph that ends `A set AGENT_CAP changes nothing.`
  (`:67-75`). One paragraph says a refused policy read is not a settings refusal: rule 7 prints the
  reader's refusal under its own header, and `policy.py settings --write` does not clear it. A
  fenced example follows, the remote case of §4's lines under §4's denial, with `Agent` as the tool
  and `origin` as the remote. Then one sentence gives both remedies.

Neither page states an agent count as a digit, so `tools/check-agent-cap-restatement.sh`, which
reads every tracked `*.md` (`:122`), has nothing new to match.

### The fixture case

`limit-hook-landed-unread` is a new `elif` in `run_limit_case` (`tools/policy/check_policy.py:2873`).
It calls `build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))`, then
`write_settings(repo, render_limit_env(2))`, then `git branch -m master`. A Workflow call is
`render_workflow(repo, "const r = await agent('one')\n")`, judged through `check_hook_call`. Four
checks, in order:

| Scenario | Judge |
|---|---|
| `no remote, on master` | exit 2, carrying `rule 7`, `the landed agent limit cannot be read`, `refs/heads/main names no commit` and `export GOV_DEFAULT_BRANCH=<branch>`, and not `settings --write` |
| `no remote, GOV_DEFAULT_BRANCH=master` | `admits`, with `env={**os.environ, "GOV_DEFAULT_BRANCH": "master"}` |
| `one remote, no remote HEAD` | after a bare repository under `t` is added as `FIXTURE_REMOTE` and `master` is pushed to it: exit 2, carrying `refs/remotes/{FIXTURE_REMOTE}/main names no commit` and `git remote set-head {FIXTURE_REMOTE} -a`, and not `settings --write` |
| `after remote set-head -a` | after `git remote set-head <FIXTURE_REMOTE> -a`: `admits` |

The refusing judges are `has(...)` (`:2881`) joined to a `"settings --write" not in err` term. The
remote is named only through `FIXTURE_REMOTE` (`:208`), which keeps `check_policy.py`, product code
for the remote-literals gate, free of a spelled remote. `run_fixture` pops `GOV_DEFAULT_BRANCH`
before any case (`:4418`), so only the second scenario sets it.

### The parity arm

`run_mirror_landed_parity` (`tools/policy/check_policy.py:2264-2301`) runs four states and accepts
any refusal that opens `policy: refused · ` (`:2296`). That would pass S2 left undone. Two changes
follow:

- A fifth state, `no remote, on master`, runs after `no remote` once
  `git branch -m main master` has run in the parity repository. Both sides refuse there, on S1's and
  S2's no-remote line.
- A refused state is judged by the whole line. It needs exit 2, no stdout, and stderr stripped
  equal to `str(exc)` of the reader's Refusal. Measured at `fce5603f8`, the two ladder refusals
  this arm and the ladder can reach are already byte-identical in shim and reader: two remotes with
  none chosen, and a `GOV_REMOTE` naming no remote. So the `two remotes` state stays green under
  the stricter judge.

### Readers of the changed text

The reader's and the shim's lines are read by: rule 7 (S3); the writer split's limit read
(`agent-cap.js:469`), which prints the message; budgets' refused list, which each enforcer prints
once (`tools/policy/budgets.py:219-223`); and `arm_reader_coverage` (`check_policy.py:540-542`),
which announces it. None compares the text. The fixture arms that judge a refusal match a prefix
or a needle, except `run_mirror_landed_parity`, which S6 tightens. The hygiene suite's fixture is on
`master` with no remote. It now gets the longer line, but its check-7 arms read only budgets'
`READER_REFUSED` rule (`budgets.py:69`), never the line (`TOOL-dGroundRules-71` §4). Rule 7's
settings denial is read by `agent-cap.test.sh:1203` and by `limit-hook-settings-over`
(`check_policy.py:2983`), and S3 leaves it as it is.

### Alternatives rejected

- Fall back to the current branch, or to `init.defaultBranch`. That is a guess. On a feature branch
  it would read an unlanded policy file as the landed one, which this kit's reader exists to
  prevent.
- A remedy on every `names no commit`. A `GOV_DEFAULT_BRANCH` naming no ref, or a branch never
  fetched, has a different fix. The remedy for one cause must not show up under another.
- Rule 7 strips the reader's line and prints its own remedy. Rule 7 cannot tell a fallback from a
  malformed policy file, and the line already carries the cause.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
`TOOL-dGroundRules-76` also edits `tools/policy/policy.py`, `tools/policy/check_policy.py`,
`tools/policy/README.md` and `help/policy.md`. `TOOL-dGroundRules-78` edits
`tools/hooks/agent-cap.js`, `tools/policy/README.md` and `help/policy.md`. So this spec cites each site by symbol or heading
as well as by line, and the builder re-finds it at its own base.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/policy-shim.sh`
- `tools/hooks/agent-cap.js`
- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `help/policy.md`
- `help/agent-limit.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. `f73.sh <dir> <branch> [remote]`
builds a repository on `<branch>` at `<dir>` with the worktree's hooks and policy kits copied in, a
limit of 2 and settings at 2. With a remote it also pushes `<branch>` to a bare repository, which
leaves no `<remote>/HEAD`. `p73.sh <dir> reader` runs the copied `policy.py get
runtime.agents-in-flight` in `<dir>`, and `p73.sh <dir> shim` runs the copied shim's `landed` there.
`h73.sh <dir>` sends one Workflow call through the copied hook and prints its stderr, then
`exit <code>`.

```
T=$(cygpath -m "$TEMP" 2>/dev/null || printf %s "$TEMP")
cat > "$TEMP/f73.sh" <<'EOF'
R="$1"; rm -rf "$R" "$R.git"; mkdir -p "$R/.governance" "$R/kits/hooks" "$R/kits/policy" "$R/.claude"
cp tools/hooks/agent-cap.js tools/hooks/scratch-guard.js "$R/kits/hooks/"
for f in policy.py budgets.py caps.toml catalogue.toml policy-mirror.js policy-shim.sh; do cp "tools/policy/$f" "$R/kits/policy/"; done
printf '[runtime]\nagents-in-flight = 2\n' > "$R/.governance/policy.toml"
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R/.claude/settings.json"
( unset GIT_DIR GIT_WORK_TREE GOV_DEFAULT_BRANCH GOV_REMOTE; cd "$R" && git init -q . && git symbolic-ref HEAD "refs/heads/$2" && git config user.email t@t.test && git config user.name t && git add -A && git commit -qm limit --no-verify
  if [ -n "${3:-}" ]; then git init -q --bare "$R.git" && git remote add "$3" "$R.git" && git push -q "$3" "$2"; fi ) 2>/dev/null
EOF
cat > "$TEMP/p73.sh" <<'EOF'
cd "$1" || exit 9
case "$2" in
  reader) python -B kits/policy/policy.py get runtime.agents-in-flight ;;
  shim) bash kits/policy/policy-shim.sh landed ;;
esac
EOF
cat > "$TEMP/h73.sh" <<'EOF'
printf '%s' '{"tool_name":"Workflow","cwd":"'"$1"'","tool_input":{"script":"const r = await agent(1)"}}' | node "$1/kits/hooks/agent-cap.js"; echo "exit $?"
EOF
bash "$TEMP/f73.sh" "$T/r73" master
bash "$TEMP/f73.sh" "$T/o73" master origin
```

`r73` is the no-remote case and `o73` the remote case. The payload's `cwd` must be a
forward-slash path, which is why `T` is derived: a backslash path is not valid JSON there.

- **AC1** — When `bash "$TEMP/p73.sh" "$T/r73" reader` runs, it exits 2 and prints, on stderr, `policy: refused · .governance/policy.toml:0 · ` followed by §4's no-remote line.
  `bash "$TEMP/p73.sh" "$T/o73" reader` prints §4's remote line with `<R>` as `origin`.
  Red when: S1 is staged back to the bare `resolve_commit` refusal. Each repository then prints
  only `refs/heads/main names no commit in this repository`, or the `refs/remotes/origin/main` form,
  as measured at `fce5603f8`.
- **AC2** — When `diff --strip-trailing-cr <(bash "$TEMP/p73.sh" "$T/r73" shim 2>&1) <(bash "$TEMP/p73.sh" "$T/r73" reader 2>&1)` runs, it prints nothing and exits 0, and so does the same command over `"$T/o73"`.
  Together with AC1, the shim prints the line with the remedy.
  Red when: S1 is built and S2 is staged back. The shim then prints the bare line, and `diff` exits
  1, naming both lines.
- **AC3** — When `python tools/policy/check_policy.py --fixture mirror-landed-parity` runs, it prints a `policy-fixture: mirror-landed-parity · no remote, on master · ` line with no `WRONG`, its last line ends `· 0 wrong`, and it exits 0.
  At `fce5603f8` the case printed four states and no `no remote, on master` line.
  Red when: S2 alone is staged back. The fifth state's whole-line judge then prints `WRONG`, which
  the old prefix judge at `:2296` would have passed.
- **AC4** — When `bash "$TEMP/h73.sh" "$T/r73"` runs, it prints §4's two-line denial with `<tool>` as `Workflow` and the message as AC1's line, then `exit 2`, and no line carries `settings --write`.
  When `GOV_DEFAULT_BRANCH=master bash "$TEMP/h73.sh" "$T/r73"` runs, it prints `exit 0`.
  Red when: S3 is staged back, so a `PolicyRefusal` reaches `renderSettingsDeny` again. The denial
  then says the settings `do not hold the landed agent limit`, and its last line opens
  `Render them from the policy:` and names `settings --write`, as measured at `fce5603f8`.
- **AC5** — When `grep -c "GOV_DEFAULT_BRANCH" help/policy.md help/agent-limit.md` runs, each page counts at least 1, and `grep -c "git remote set-head" help/policy.md help/agent-limit.md` counts at least 1 for each too.
  Red when: either page is left as it is. Both greps printed `0` for each page at `fce5603f8`.
- **AC6** — When `python tools/policy/check_policy.py --fixture limit-hook-landed-unread` runs, it prints its four scenario lines with no `WRONG`, its last line ends `· 0 wrong`, and it exits 0.
  At `fce5603f8` it printed `policy-fixture: no case named limit-hook-landed-unread` and exited 2.
  Red when: S3 is staged back, so `no remote, on master` and `one remote, no remote HEAD` each print
  `WRONG`, because `settings --write` appears. Red also when S2 is staged back: the remedy needles
  are missing from the same two lines.

## 6. Gates

`policy fixtures` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy check` · `python resolver (behaviour + inline parity + idiom ban)` · `remote literals (kit code names no remote)` · `agent-cap restatement` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

These were run through `derive_guarded_legs` at `fce5603f8`, with `{prefix}` as `tools`. Every
policy file trips `policy fixtures` through its `{prefix}/policy/` guard, and `help/policy.md` and
`tools/hooks/agent-cap.js` trip it through their own guard rows. `tools/hooks/agent-cap.js` also
trips five legs through `{prefix}/hooks/`: the agent-cap, scratch-guard, verifier fan-out,
review-join and hook-destinations self-tests. `help/agent-limit.md` trips no guarded leg. The
unguarded legs that read these files:

- `policy check` runs `check_policy.py` over the tree.
- The python resolver leg reads the inline ladder blocks of `policy.py` and `policy-shim.sh`. S1 and
  S2 edit outside those blocks, and its broad guard keeps it out of the join.
- The remote-literals leg reads every tracked `*.sh`, `*.py` and `*.js`.
- The restatement leg reads every tracked `*.md`.

New arm: tools/policy/check_policy.py · covers AC6 · the case `limit-hook-landed-unread`; staging S3 back reds its two refusing scenarios on `settings --write`, and staging S2 back reds them on the missing remedy · none
New arm: tools/policy/check_policy.py · covers AC3 · the fifth state of `mirror-landed-parity`, judged by the whole line; staging S2 back alone reds it · none

No floor moves. The fixture asserts only that some assertion ran (`check_policy.py`, `run_fixture`'s
last line), and no count of its cases is pinned. The close's main loop observes both arms red, then
green.

## 7. Open questions

none

A follow-up, not a fork, which the main loop files as an ask: the report's left-shift rule, that
every hook denial path has a fixture asserting its remedy text for each distinct cause, so a
refusal never shares another cause's remedy. That needs an inventory of every denial path in
`agent-cap.js` and `scratch-guard.js` and a predicate over the fixtures. It is a gate of its own,
not an arm of this mechanism. The non-integer limit denial at `agent-cap.js:1802` is a candidate it
would reach.

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's rescope add row for this unit and its spec
  brief, grounded at `fce5603f8`. Re-measured H2 (report id 13) in scratch repositories built from
  the worktree's kits, in both the no-remote and the one-remote case, and confirmed the premise.
  Specs the skeptic's corrected fix, because the finder's fix was judged UNSOUND. The fix keeps the
  refusal, names the missing ref and its remedy in reader and shim alike, gives rule 7 a refused-read
  denial, documents both remedies, and adds the fixture case. The remedy applies only on the
  fallback path, so another cause never shows it. The parity arm's whole-line judge is in scope as
  one small arm of the same mechanism. The left-shift class rule goes to §7. The brief's leg item
  names §6, which in this Tier-1 shape is the Gates section, and its follow-up item names §7, Open
  questions here. The report and the brief, untracked when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-73-spec-brief.md
```

## 9. Reuse audit

This unit extends existing seams and builds no new mechanism. The refusal stays the policy kit's
`Refusal` (`tools/policy/policy.py:201`), raised from `derive_landed_revision`. The shim's refusal
stays its existing `printf`. Rule 7's denial is a sibling of `renderSettingsDeny` inside
`checkSettingsInForce`. The fixture case reuses `build_limit_repo`, `write_settings`,
`render_workflow`, `check_hook_call`, `has` and `admits` from `run_limit_case`, and the parity arm
is the existing `run_mirror_landed_parity`.
`python tools/codebase-map/reuse_lookup.py "refusal remedy when the landed revision default branch ref names no commit"`
ranked `Refusal` (`tools/policy/policy.py` among its homes) as a seam, which is the class S1 raises.
Its other candidates were name stems (`refusal`, `remedy`, `branches`), and none reads a landed
ref. The recall probe returned the report's H2 and this unit's brief. It also returned
`TOOL-aStandingWrit-4`'s ruling that an environment-named branch may only cross-check. That ruling
governs the pre-push classifier. The policy ladder already reads `GOV_DEFAULT_BRANCH` ahead of the
observed branch (`tools/policy/policy.py:415`), and this unit changes no ladder order: it only
names that variable in a refusal's remedy.

Recall terms used: `python tools/memory-recall/query.py "landed revision refusal remedy origin HEAD default branch rule 7 denial" --terms "derive_landed_revision policy-shim landed GOV_DEFAULT_BRANCH set-head origin/HEAD renderSettingsDeny PolicyRefusal checkSettingsInForce"`
