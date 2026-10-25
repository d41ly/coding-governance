# TOOL-dGroundRules-80 — the policy fixtures pin the new case's bare remote HEAD, and a sixth parity state holds the remote refusal variant byte-equal

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 59f02fde · streams tooling · order 28

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-80-ledger.md](../build/2026-10-25-build-TOOL-dGroundRules-80-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-80-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-80-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-80-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-80-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 2 confirmed two medium findings in `tools/policy/check_policy.py`.
This unit repairs both. M1: the `limit-hook-landed-unread` case creates its bare remote without
pinning its HEAD. On a node whose `init.defaultBranch` is `main`, the case's
`git remote set-head <remote> -a` fails and reds the `policy fixtures` leg, although no product code
is wrong. M2: the `mirror-landed-parity` case never reaches the remote variant of the main-fallback
refusal. So nothing holds the reader's line and the shim's line for that variant byte-equal. This
unit pins the bare's HEAD to the branch the case pushes, and adds a sixth parity state that reaches
the remote variant and judges it by the whole line.

## 2. Scope (IN)

- **S1** — In the `limit-hook-landed-unread` branch of `run_limit_case`
  (`tools/policy/check_policy.py:2973-2996`), one line goes directly after the bare's init at `:2989`:
  `run_fixture_git(bare, "symbolic-ref", "HEAD", "refs/heads/master")`. A one-line comment above it
  says why, in the text §4 "S1, the pin" gives. The bare's HEAD then names the branch the case pushes
  at `:2991`, whatever the node's git config says. Observed by AC1.
- **S2** — `run_mirror_landed_parity` (`tools/policy/check_policy.py:2227-2263`) gains a sixth state,
  `one remote, no remote HEAD, on master`, after `no remote, on master`, in the code §4 "S2, the sixth
  state" gives. It is judged by the same whole-line lambda as the other states. The function's
  docstring and the module docstring's sentence at `:80` say six states, and the README sentence
  under the case list says six states and names the new one. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- `tools/policy/policy.py` and `tools/policy/policy-shim.sh`. Both refusal lines are correct today
  (§4 "Evidence"). This unit adds only the gate that holds them equal.
- M1's left-shift gate: a fixed `-c init.defaultBranch=<value>` on every `run_fixture_git` call, or
  one leg run under an injected `main`. It is a separate mechanism that changes every fixture git
  call across all 150 cases. A one-case probe cannot show its effect, so it is a follow-up (§8).
- M2's left-shift gate: a count check that every refusal variant a spec declares byte-equal has a
  whole-line parity state. It is a new check over spec text and code, so it is a follow-up (§8).
- `help/policy.md`. It names neither case, and no user-facing behaviour changes.
- The report's other findings and the inherited reds the close recorded.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-73` (CLOSED). That unit added both
refusal variants, the `limit-hook-landed-unread` case and the fifth parity state. This unit changes
none of the refusal code that unit wrote.

## 4. Design

### Evidence

Every premise below was re-read at `59f02fde9`, and both premises still hold.

M1. The case runs `run_fixture_git(bare, "init", "-q", "--bare")` at `:2989` with no branch pin. It
pushes only `master` at `:2991`, then runs `remote set-head <remote> -a` at `:2994`.
`run_fixture_git` (`:4413-4417`) passes only `user.name`, `user.email` and `commit.gpgsign` as `-c`,
with `check=True`. So the bare's HEAD follows the node's `init.defaultBranch`. On this node that is
`master`, set in the system gitconfig (`git config --show-scope --get-all init.defaultBranch` printed
`system ... master`). Three probes were run:

- `python tools/policy/check_policy.py --fixture limit-hook-landed-unread` printed `· 0 wrong`.
- The same command under `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=init.defaultBranch GIT_CONFIG_VALUE_0=main`
  printed `policy-fixture: limit-hook-landed-unread · limit-hook-landed-unread · the fixture · WRONG: CalledProcessError: error: Cannot determine remote HEAD`
  and `79 assertion(s) executed · 1 wrong`.
- A scratch replay of the case's git steps under the same injection showed the bare's HEAD as
  `refs/heads/main` and `set-head -a` exiting 1. With `symbolic-ref HEAD refs/heads/master` run on the
  bare after its init, it printed `'up/HEAD' is now created and points to 'master'` and exited 0.

Every other `init` in the file either pins its branch with `symbolic-ref` or never reads a remote
HEAD. The other bare repositories (`:2009`, `:2464`, `:2662`) are only pushed to by explicit refspec,
and nothing runs `set-head` or clones them. `:2994` is the file's only `set-head`.

M2. The case's five states are at `:2245-2247`. In `one remote`, `refs/remotes/upstream/main` was
pushed (`:2242`) and resolves, so the reader's `if remote:` branch in `derive_landed_revision`
(`tools/policy/policy.py:491-494`) is never reached. The shim's matching `WHY` is at
`tools/policy/policy-shim.sh:108-109`. `python tools/policy/check_policy.py --fixture mirror-landed-parity`
printed five state lines and `· 0 wrong`. None of them carries `HEAD names no branch`. A scratch
repository on `master`, with one remote, only `refs/remotes/upstream/master`, and no remote HEAD,
was built from the worktree's `policy.py` and `policy-shim.sh`. There the shim and the reader each
printed this same line:

```
policy: refused · .governance/policy.toml:0 · refs/remotes/upstream/main names no commit in this repository, and main is only the fallback: refs/remotes/upstream/HEAD names no branch and GOV_DEFAULT_BRANCH is unset. Name the default branch: git remote set-head upstream -a, or export GOV_DEFAULT_BRANCH=<branch>.
```

So the code is right today, and the state below reaches it. The report this unit answers, untracked
when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md
```

### S1, the pin

The skeptics judged either of two pins SOUND: `--initial-branch=master` on the init, or a
`symbolic-ref` after it. S1 takes the second. It is the idiom this file already uses for every
branch pin (`:1527`, `:1593`, `:1945`, `:2466`, `:2664`, `:2807`, `:3224`, `:4436`), and it needs no
git version floor. After S1, lines `:2987-2991` read:

```
            bare = t / "o.git"
            bare.mkdir()
            run_fixture_git(bare, "init", "-q", "--bare")
            # the bare's HEAD names the branch pushed below, whatever this node's init.defaultBranch (TOOL-dGroundRules-80)
            run_fixture_git(bare, "symbolic-ref", "HEAD", "refs/heads/master")
            run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, bare.as_posix())
```

### S2, the sixth state

The state tuple at `:2245-2247` gains a sixth entry, `("one remote, no remote HEAD, on master", None, None)`.
After the existing `no remote, on master` branch in the loop body, a second branch builds the state:

```
            if state == "one remote, no remote HEAD, on master":
                run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, bare.as_posix())
                run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_REMOTE}/master", "HEAD")
```

The states run in order, so the repository is already on `master` with no remote when this branch
runs. Re-adding `FIXTURE_REMOTE` makes it the only remote. Its tracking refs were deleted with it in
the `no remote` state, so `update-ref` leaves exactly one, `refs/remotes/<remote>/master`, and no
`refs/remotes/<remote>/HEAD`. `branch.master.remote` is unset, because no push used `-u`. So
`resolve_remote` (`tools/policy/policy.py:366-416`) picks the only remote, observes no branch, and
returns an empty branch. Both sides then take the remote fallback refusal. The existing lambda judges
it by `rc == 2 and not o and e.strip() == line`, the whole line.

`update-ref` and not `push` or `fetch`: it is the idiom `:2244` uses for the second remote, it does
no I/O, and a fetch could create the remote HEAD the state must not have.

The function's docstring becomes:

```
    """The shim's `landed` against the reader's `derive_landed_revision` in six ladder states, each
    remote's main a different commit: two remotes with GOV_REMOTE naming the second; two without;
    one remote; no remote; no remote, on master; one remote with no remote HEAD, on master. The same
    sha in each, or both refusing with the same whole line (TOOL-dGroundRules-73, TOOL-dGroundRules-80).
    The shim runs under the bash `resolve_bash` finds able to see it, whatever PATH puts first, and
    the case names it."""
```

The module docstring's sentence at `:80` becomes
`` `mirror-landed-parity` holds the shim's `landed` to `derive_landed_revision` in six ladder states. ``

In `tools/policy/README.md`, the sentence at `:484-487` that opens `` `mirror-landed-parity` runs the
shim's `` becomes these lines, and the next sentence starts on a new line:

```
other outcome case must leave `arm_mirror_landed` green. `mirror-landed-parity` runs the shim's
`landed` beside `derive_landed_revision` in six states, with two remotes and `GOV_REMOTE`, two
without, one, none, none on `master`, and one on `master` with no remote HEAD: the same sha, or both
refusing with the same whole line, in each (TOOL-dGroundRules-73, TOOL-dGroundRules-80).
`mirror-commit-rewrite` runs `mirror --write` at a
```

### What this does not check

AC1 shows the case is green under one injected default, `main`. It does not show that the other 149
cases are green under it. That is the left-shift gate this unit leaves as a follow-up. AC2 holds
only the remote fallback variant. A third variant added to either side later gets no state from this
unit. The sixth state does not grade `git remote set-head` itself. `limit-hook-landed-unread` does
that through the hook.

### Alternatives rejected

- `--initial-branch=master` on the init. Also SOUND, but it needs git 2.28 or later and departs from
  the file's eight `symbolic-ref` pins.
- Building the sixth state with `push -q <remote> master` to the bare. That gives the same refs, but
  it writes to the bare that the earlier states share, and it does not match `:2244`'s idiom.
- A new standalone case for the remote variant. The parity case already owns the whole-line judge
  and the state ladder, so a separate case would copy both.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
No help page changes, because nothing a user runs behaves differently.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/README.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. Each staged break is made in the
worktree file named, the command is run again, and the file is restored with `git checkout -- <file>`.
`check_policy.py` imports the worktree's `policy.py` as the reader and copies the worktree's
`policy-shim.sh` into each fixture, so a break in either file reaches the case.

- **AC1** — When `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=init.defaultBranch GIT_CONFIG_VALUE_0=main python tools/policy/check_policy.py --fixture limit-hook-landed-unread` runs, it prints its four scenario lines with no `WRONG`, its last line ends `· 0 wrong`, and it exits 0. The same command without the three variables prints the same.
  At `59f02fde9` the injected run printed `the fixture · WRONG: CalledProcessError: error: Cannot determine remote HEAD` and `· 1 wrong`.
  Red when: S1's `symbolic-ref` line is staged out. The injected run then prints that same `WRONG`
  line again.
- **AC2** — When `python tools/policy/check_policy.py --fixture mirror-landed-parity` runs, it prints six state lines, one of them opening `policy-fixture: mirror-landed-parity · one remote, no remote HEAD, on master · ` and carrying `refs/remotes/upstream/HEAD names no branch`, with no `WRONG` anywhere, its last line ending `· 0 wrong`, and it exits 0.
  At `59f02fde9` it printed five state lines and none of them carried `HEAD names no branch`.
  Red when: the remote `WHY=` assignment in `tools/policy/policy-shim.sh` is staged to `WHY=""`. The
  shim then prints the bare `names no commit in this repository` line, and the sixth state prints
  `WRONG`.
  Red also when the `if remote:` raise in `derive_landed_revision` (`tools/policy/policy.py`) is staged out. The reader then raises the no-remote remedy, and the sixth state prints `WRONG`.
- **AC3** — When `grep -c "in six ladder states" tools/policy/check_policy.py` runs, it prints `2`, and `grep -c "in six states" tools/policy/README.md` prints `1`.
  At `59f02fde9` they printed `0` and `0`, and `grep -c "in five ladder states" tools/policy/check_policy.py` printed `2`.
  Red when: either docstring or the README sentence still says five, with the sixth state built.

## 6. Gates

`policy fixtures` · `policy check` · `remote literals (kit code names no remote)` · `agent-cap restatement` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

`python tools/check-spec-tokens.py --legs-for` was run at `59f02fde9` over both touched files. It
names one non-broad guarded leg for each, `policy fixtures`, through `{prefix}/policy/`. Every other
leg it prints trips only on the broad `tools/`. These unguarded legs read what this unit changes:

- `policy check` runs `tools/policy/check_policy.py` in its live mode.
- The remote-literals leg reads every tracked `*.py`. S1 and S2 name the remote only through
  `FIXTURE_REMOTE`.
- The restatement leg reads every tracked `*.md`, so it reads the README sentence.
- `kit epoch` reads the policy kit's shipped bytes. Both files ship, so it prints the version move as
  owed at the lander.

New arm: tools/policy/check_policy.py · covers AC2 · the sixth state of `mirror-landed-parity`, judged by the whole line; staging the shim's remote `WHY=` to empty, or the reader's `if remote:` raise out, reds it · none

S1 adds no arm. It makes an existing case independent of the node's git config, and AC1's staged
break reds it under the injected default. The close's main loop observes the new arm red, then
green.

No floor or pinned count moves. The fixture asserts only that some assertion ran, and no count of its
cases is pinned. The case count stays 150, and the assertion count grows by one. The leg is sized at
budget 970 and ceiling 1290, from a 644s whole run (`tools/run-gates/selftest-budgets.txt`, the
`policy fixtures` row). S2 adds one shim run and one reader call, about 2s, judged against the five
states the case runs in about 12s today. S1 adds one git call. The leg stays inside both figures:
about 646s, and 646 x 1.5 is 969. Neither figure moves.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `59f02fde9`. Both
  premises were re-verified. M1 was reproduced by the case itself under an injected `main` default,
  and by a scratch replay that also showed the `symbolic-ref` pin clears it. M2 was confirmed by the
  case's five state lines and by a scratch repository in which the shim and the reader printed the
  same remote-variant line. S1 takes the `symbolic-ref` form of the two SOUND fixes, to match the
  file's own pins. Follow-ups for the main loop to file as asks. These are not forks, because the
  brief scoped this unit to the SOUND fixes. First, M1's left-shift gate (class
  `memory/gotchas/fixture-inherits-ambient-machine-state.md`). Either `run_fixture_git` passes a
  fixed `-c init.defaultBranch=<value>`, or the `policy fixtures` leg runs once under an injected
  `main`. A `-c` on the command line wins over `GIT_CONFIG_COUNT`, as measured on this node, so the
  first form makes every fixture git call node-independent. Its effect on all 150 cases needs a whole
  leg run, which no case-sized probe gives. Second, M2's left-shift gate (class
  `memory/gotchas/rule-stated-with-no-check-that-fails.md`). It is a check that every refusal
  variant a spec declares byte-equal between the reader and the shim has a whole-line parity state,
  so that adding a refusal branch without a state fails the parity arm's own count. The brief,
  untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-80-spec-brief.md
```

## 9. Reuse audit

This unit builds no mechanism. S1 reuses the file's own branch pin, a `symbolic-ref HEAD` call
through `run_fixture_git` (`tools/policy/check_policy.py:2807` and seven others). S2 extends the existing state ladder and whole-line judge of `run_mirror_landed_parity`
(`tools/policy/check_policy.py:2245-2259`). It builds its refs with the `update-ref` idiom that
function already uses at `:2244`.
`python tools/codebase-map/reuse_lookup.py "pin a fixture repository's default branch so git init does not inherit the machine's init.defaultBranch"`
ranked only name stems (`git`, `fixture`, `run_git`, `build_fixture`), and none of them pins a
fixture's branch. The seam is the file's own `run_fixture_git` pin idiom. The recall probe returned
`TOOL-aLevelledCopy-9`, which pinned other ambient git state in a different kit's fixtures under
the same gotcha class. It also returned this unit's brief and report. No record pins a policy-fixture
bare HEAD.

Recall terms used: `python tools/memory-recall/query.py "fixture inherits init.defaultBranch bare remote HEAD set-head parity state refusal shim reader byte-equal" --terms "init.defaultBranch symbolic-ref set-head mirror-landed-parity run_fixture_git"`
