# TOOL-aFrugalTurnstile-7 — pre-push binds a post-merge red, and `--decide` prints the boundary's decision

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D8 and D9 in `.githooks/pre-push`. Where the gate-env file at R declares
`GATE_POST_MERGE`, the hook reads the remote's `refs/gov/bar-red` with one bounded call. A red on an
ancestor of the tip forces a FULL bar until the green the decision adopted descends from it, so a
post-merge red blocks the next landing through recorded state rather than a log line. A new mode,
`pre-push --decide <tip> <remote-sha>`, runs the same decision code, prints the decision as one
line, and writes nothing. The unattended close then runs the bar the landing push would ask for
(TOOL-aFrugalTurnstile-9).

## 2. Scope (IN)

- **S1 — the declaration, read at R.** In `classify_docs`, around line 1262, the blob of the
  gate-env file at R is already read with `git show`. Right after that read, and before the
  `GATE_DOC_PATHS` early return, `PM_DECL` is set to `read_policy_key "$blob" GATE_POST_MERGE`. That
  is the brief's "same block as `GATE_DOC_PATHS`", and it costs no spawn. `GATE_POST_MERGE` joins
  the names the policy block unsets around line 1093, so neither the environment nor a sourced
  pushed-tree copy can declare it.
  - Empty, or R absent or all zeros, is undeclared: nothing is read, and every decision is today's.
  - `local` or `ci` is declared.
  - Any other value is read as declared, the direction in which a typo cannot land a red. One line
    names it: `pre-push: GATE_POST_MERGE at <R8> is '<v>', outside 'local ci', and is read as declared`.

  Observed by AC3 and AC5.
- **S2 — the read, bounded.** `read_post_merge_red` runs one
  `git ls-remote --exit-code <url> refs/gov/bar-red`. It runs only under a declaration, and only
  when the push is about to be scoped or covered. A push that is FULL with no covering record prints
  one line saying the red was not read because the push is already FULL, so the skip announces
  itself.
  - The bound is the kit's `observe_remote` shape, with source constants copied from
    `tools/unattended/unattended.sh` lines 144-149 at base (PINNED): `timeout -k 5s 60`,
    `GIT_TERMINAL_PROMPT=0`, `ssh -o ConnectTimeout=20 -o BatchMode=yes`,
    `-c credential.interactive=never` and `-c http.lowSpeedLimit=1000 -c http.lowSpeedTime=60`.
  - Output is captured to a `mktemp` file outside the git dir, cleaned up afterwards, and never read
    through a command substitution: the class `bounded-through-a-pipe-is-unbounded`.
  - A host with no working `timeout -k`, probed once and only under a declaration, prints one line
    saying the wall-clock bound is inert while the transport bounds still apply.
  - rc 0 with a hex sha on the `refs/gov/bar-red` line is present. rc 2 is absent. Anything else is
    unreadable: rc 124 reads "the 60 s bound fired", and any other rc reads "git ls-remote exited <rc>".
  - The URL is `$2` on a push, the URL git is pushing to. Under `--decide` it is
    `git remote get-url --push <remote>`. The URL is never printed: a message names the remote by
    NAME, or says "the push URL".

  Observed by AC1, AC3 and AC4.
- **S3 — the force, after adoption.** `check_post_merge_red` runs once the adopted record is known.
  That is between TOOL-aFrugalTurnstile-2's cover pass and its covered exit, which that unit places
  after the dirty-tree refusal (around line 1448) and before the decision line. A push that any
  refusal stops therefore never pays the network read. The adopted sha `X` is the covering record's
  sha when the cover pass found one, else `inh_sha`, else `rec_sha`.
  - Unreadable: force FULL.
  - Present as `P`, and `P` is not an ancestor of the tip: no force, and one line says it does not
    bind this push. A `P` absent from this clone's object store is no ancestor of the tip, because
    every ancestor of a local commit is local.
  - Present, an ancestor of the tip, `P` is an ancestor of `X`, and `X` is not `P`: no force, and one
    line says the red is cleared, naming `X`.
  - Present and an ancestor of the tip otherwise: force FULL.

  A force empties `inh_sha` and the covering record and sets `force`. The covered exit is then not
  taken, and the decision block takes its FULL branch and names the reason on the decision line.
  That is the half of TOOL-aFrugalTurnstile-2's hand-off which says a red must refuse a covered
  decision unless the covering record's sha descends from it. Nothing here can make a run smaller
  than today's decision, so the hook's every-predicate-forces rule holds. Observed by AC1, AC2, AC4
  and AC11.
- **S4 — `--decide`, its arguments and exits.** It is parsed in a new block after `cd "$top"`
  and above THE RUN LOG, in the form `pre-push --decide <tip> <remote-sha> [<remote>]`.
  - `<tip>` must resolve to a commit, and `<remote-sha>` must be 40 or 64 hex digits, all zeros
    allowed.
  - `<remote>`, when absent, comes from the lander's ladder: the `remote_ladder_sh` block from
    `tools/lib/resolve-remote.sh`, carried inline and byte-identical. Given, it is passed to the
    block as `GOV_REMOTE`.
  - A wrong count, a bad value or a ladder refusal prints a usage line or `RR_WHY` on stderr and
    exits 2. Every such site sits above the journal root, so it is unloggable by construction.
  - The ref loop then reads one synthesized line,
    `refs/heads/<default> <tip> refs/heads/<default> <remote-sha>`, in place of stdin.
  - `push_remote` is the ladder's name, so the default branch is observed exactly as on a push.

  Observed by AC7 and AC9.
- **S5 — `--decide` writes nothing.** Observed by AC6 and AC7. The mode empties `PUSH_REFUSAL`
  and `PUSH_BAR`, forces the run-log switch off, and installs no EXIT trap. Each write site the hook
  has is exempted as §4 "The write sites under --decide" lists. It skips three layers that refuse a
  push and decide nothing: the straggler guard (around line 666), the merge-loss check (around 736)
  and the raw-push marker refusal (around 1019). Every other refusal still applies and exits 1 with
  nothing on stdout: the default-branch refusals, the receipt and runner vetting, the manifest
  refusal, the head mismatch, bar vetting and the dirty tree.
- **S6 — `--decide` prints exactly one line.** On entry the mode runs `exec 3>&1 1>&2`, so every
  existing `echo`, the decision line included, goes to stderr. `print_decision` writes the one line
  to fd 3 and the mode exits 0. The shapes:
  - `full <why>`, where `<why>` is the FULL decision line's reason, `$force` with `; $inh_why` when set;
  - `scoped <base>`, where `<base>` is the full sha the push would export as `GATE_BASE`;
  - `covered <record>`, where `<record>` is the path of the record that covered the tip.

  A doc-only decision prints plain `scoped <base>`, and the docs narrowing is not carried: the
  caller runs a wider bar, never a narrower one. The covered line is printed from
  TOOL-aFrugalTurnstile-2's covered branch, before that branch writes anything, and the other two
  from the decision block.
  - **The scoped base, resolved once.** `resolve_scoped_base` returns `inh_sha` when an inherited
    green was adopted, else `rec_sha`. It is called by the scoped `GATE_BASE` export, by
    `print_decision`'s scoped line and by TOOL-aFrugalTurnstile-2's scoped-record comparison, which
    that unit writes inline. That moves the comparison onto the callable decision, the other half of
    its hand-off, so the cover check and the decide line cannot name two bases.

  Observed by AC6 and AC11.
- **S7 — the text.** The header gains the two sentences in §4 "The header sentences". The
  `.githooks/pre-push.runlog.test.sh` exit table gains one row per new exit site, each `exempt:`
  with its reason: the mode's exit-2 sites, and its `RUNLOG_CLEAN=1; exit 0` decision site. That
  site carries the clean-exit mark because it sits below the trap line. Observed by AC10. The
  table rows are NOT OBSERVED in the pass: the run-log suite's EXITS arm grades them at VERIFYING.
- **S8 — the arms.** The arms in §7 join `.githooks/pre-push.test.sh`. NOT OBSERVED in the pass,
  which runs no suite: AC1 to AC9 observe the same behaviour directly on a scratch fixture.

## 3. Non-goals (OUT)

- Deleting or writing the ref from the hook. Only `post-merge.sh` publishes it
  (TOOL-aFrugalTurnstile-6).
- Calling `--decide` from the unattended close (TOOL-aFrugalTurnstile-9).
- Any change to which decisions exist, to `GATE_FULL_MAX_LAG`, or to the docs class.
- Gov's own `GATE_POST_MERGE` declaration, which is decided at the close, after the code exists.
- A kit-version bump. One bump per touched kit happens after the last unit.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-6` — the red ref and its rules. Without a publisher, the
  read in S2 always answers absent, and AC1 stages the ref by hand.
- **consumes-from** `TOOL-aFrugalTurnstile-2` — the cover pass and the covered decision. S3 reads the
  covering record's sha, and S6 prints `covered` from that pass's state.
- **hands-off** `TOOL-aFrugalTurnstile-9` — calling the decide mode from the close's in-place arm and
  running the bar under the decision it prints.

The decision code `--decide` prints includes the first-parent staleness count and the runner-only
candidate rule from the order-1 unit on this hook. No criterion here rests on them, so no edge is
declared. The protocol text and the runbook text that describe this binding are order-1 units,
before this one, so a hands-off to either would run against the declared build order.

## 4. Design

Read at base `bef97330`, whose `.githooks/` and `tools/` are byte-identical to `5a836bf0f`.

- `read_policy_key`, around line 1095, parses one key out of the gate-env file at R without
  executing it. `classify_docs` already holds that blob.
- The decision block, around lines 1455-1470, checks `inh_sha` first, then `force`, then the
  scoped full green. A force therefore has to empty `inh_sha`, or a FULL reason would be printed
  beside a scoped run.
- The hook resolves the default branch from `$1`, the remote name git passes, around line 403. Under
  `--decide`, `$1` is the flag, so the remote has to come from somewhere else, and the ladder is
  the one every landing probe uses (TOOL-dLadderedRemote-1).
- `.githooks/pre_push_bar_selftest.py` anchors on the `set +f` line, which is spelled exactly once.
  Nothing this unit adds spells a second one.
- The run-log suite enumerates every exit site by its code text and count. A new exit that is not in
  its table reds that suite, which is why S7 adds the rows.

### The write sites under --decide

Every site at base that writes a file, with what the mode does to it. Line numbers are approximate.

| Site | Around line | Under `--decide` |
|---|---|---|
| `rm -f "$PUSH_REFUSAL" "$PUSH_BAR"` | 334 | guarded on a non-empty name, so skipped |
| `write_push_line`, through the once, start and end writers and the EXIT trap | 193, 455 | switch off and no trap |
| `write_refusal`, from every refusal and from `check_reviewed_file` | 337, 476 | returns at once; the caller still exits 1 |
| `rm -rf "$gd/gate-run/$RUNLOG_GATE_RUN"` | 1534 | unreachable: the mode exits at the decision |
| `printf … > "$PUSH_BAR"` | 1563 | unreachable, and guarded |
| the bar and everything after it | 1565 | unreachable |
| TOOL-aFrugalTurnstile-2's covered branch writing the vetted-bar file | — | guarded on a non-empty name |
| the sourced `gate-env.sh` | 492 | NOT guardable; named in the header |

### Messages

Every line starts `pre-push: `. Each is one line per decision.

- `pre-push: post-merge bar: no red on <name|the push URL> (GATE_POST_MERGE=<v> at <R8>)`
- `pre-push: post-merge bar: red <P8> on <name> is not an ancestor of the pushed tip, so it does not bind this push`
- `pre-push: post-merge bar: red <P8> on <name> is cleared for this push — the adopted green <X8> descends from it`
- `pre-push: post-merge bar: not read — this push is already FULL`
- The force reason, inside the FULL line:
  `a post-merge full bar is RED at <P8> (refs/gov/bar-red on <name>) and the adopted green <X8> does not descend from it`.
  With no adopted record, the reason reads `… and no adopted green descends from it`.
- The unreadable reason, inside the FULL line:
  `GATE_POST_MERGE is declared at <R8> and refs/gov/bar-red on <name> could not be read (<why>), so a post-merge red cannot be ruled out`.

### The header sentences

> WHAT --decide DOES NOT CHECK: the raw-push marker, the straggler layer and the merge-loss layer,
> which refuse a push and decide nothing, so a push it reports as scoped can still be refused by
> them; the docs-only narrowing, which it reports as plain scoped, so its caller runs a wider bar and
> never a narrower one; and anything a sourced gate-env.sh writes, which runs inside this hook in
> either mode.

> WHAT THE POST-MERGE READ DOES NOT CHECK: it reads the remote's red ref once, at this push, so a red
> published after the read binds the next push; it takes a red sha absent from this clone as no
> ancestor of the tip, which is wrong only in a shallow clone; and a red on exactly the adopted
> green's sha is not cleared here, since the order of two verdicts on one sha is unknown to this
> hook. `post-merge.sh` clears that case by deleting the ref on its next green.

### Inventory

Each name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` at writing
time, cell `sh.function`, and each answered OK: `read_post_merge_red`, `check_post_merge_red`,
`print_decision` and `resolve_scoped_base`. The inline `resolve_remote_sh` is carried, not minted. The variables minted are
`PM_DECL`, `PM_RED`, `PM_STATE` and `PM_WHY`, and the mode's flag and arguments.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`

### Alternatives rejected

- **A second `git show` of the gate-env file for the new key.** A git spawn costs about 751 ms on
  node a (memory note, PINNED there), and `classify_docs` already holds the blob.
- **Reading the ref whatever the decision.** A FULL decision gains nothing from it, and the network
  call is the slowest step the hook would add.
- **`--decide` printing a refusal as `full <why>`.** A refusal is not a FULL decision. Exit 1 with an
  empty stdout is "anything else", which TOOL-aFrugalTurnstile-9's caller already treats by falling
  back to a full bar.
- **Carrying the docs narrowing in the decide line.** A fourth shape, or a second field, is a shape
  TOOL-aFrugalTurnstile-9's caller rejects, so it would fall back to a full bar. A plain scoped line
  keeps most of the saving and is never narrower than the push.

## 5. Production-readiness checklist

- security — Only R decides whether the ref is read, never the pushed tree or the environment. The
  read can only force. The URL never reaches output. `--decide` cannot reach a write the table names,
  except what a sourced gate-env file does in either mode.
- perf / scale — Undeclared: zero extra spawns. Declared: one bounded `ls-remote`, plus the
  `timeout` probe, and only on a push that would otherwise be scoped or covered.
- error / empty / loading states — An unreadable ref forces FULL with its reason. A `--decide`
  refusal exits 1, with its message on stderr and nothing on stdout.
- observability — One `pre-push: post-merge bar:` line on every declared push. The FULL line names
  the red sha. `--decide` keeps every message, on stderr.
- risks — The gotcha class `decision-re-derived-by-a-second-process` is avoided by construction:
  `--decide` is the hook's own code. Its inputs can still move between the decide call and the
  push, such as the remote's sha or a new red, and the push then decides again on its own inputs.
- testing — The arms in §7, on scratch fixtures with a git shim on `PATH` that logs every argv.
- migration — None. Undeclared repositories behave byte-for-byte as before.
- user docs — The hook header. The adopter's declaration is DEPL-aFrugalTurnstile-1's.

## 6. Acceptance criteria

Every criterion runs on a scratch clone with a bare remote under a short root in `%TEMP%`. The clone
holds this hook copied into its `.githooks/`, the shape `.githooks/pre-push.test.sh` already builds.
It also holds a stub bar that writes a marker file and its `GATE_FULL` value, the lander marker for
the real-push arms, and a hand-written `gate-full-green`. A git shim directory sits first on `PATH`;
it appends each argv to a log and execs the real git. The red ref is staged with
`git push <bare> <sha>:refs/gov/bar-red`. Each red-before-fix case runs the hook as it is at base,
taken with `git show bef97330:.githooks/pre-push`, and then the changed hook.

- **AC1** — When `GATE_POST_MERGE=local` is committed at R, the ref names an ancestor of the tip,
  and the recorded full green is an ancestor of that red within the lag bound, a push prints
  `pre-push: FULL gate` naming the red's short sha. The stub bar records `GATE_FULL` as 1, and the
  shim log holds exactly one `ls-remote` line. Red when: the push is scoped, which is the base
  hook's decision.
- **AC2** — When the same fixture's recorded green is a strict descendant of the red, the push
  prints `pre-push: scoped gate` and the `post-merge bar:` line naming the red as cleared. Red when:
  the push is FULL.
- **AC3** — When no `GATE_POST_MERGE` is committed at R and the ref is present, the decision line
  matches the base hook's, and `grep -c ls-remote <shim log>` prints 0. Red when: an `ls-remote` is
  spawned undeclared, or the decision moves.
- **AC4** — When the key is declared and the remote's push URL is set by
  `git remote set-url --push <remote> <a path that does not exist>`, `pre-push --decide <tip> <R>`
  prints one line opening `full ` that names refs/gov/bar-red as unreadable. Red when: it prints
  `scoped `, which reads an unreadable ref as absent.
- **AC5** — When the committed value is `GATE_POST_MERGE=yes`, the push prints the
  `outside 'local ci'` line, and AC1's red still forces FULL. Red when: the value reads as
  undeclared.
- **AC6** — When `pre-push --decide <tip> <R>` runs in three fixture states, each with no lander
  marker, stdout is exactly one line each time, and the exit is 0.
  - With no record, the line opens `full `.
  - With the full green in range, the line is `scoped <sha>`, where `<sha>` is the record's full
    40-hex sha.
  - With a `gate-bar-green` record whose tree equals the tip's, for a tracked bar declared in both
    `gate-env.sh` and `.unattended.conf`, the line opens `covered `.

  Each time, a `sha1sum` of every file under the git dir is unchanged after one warm-up
  `git status`. There is no `pre-push-refusal` or `pre-push-bar` file, the journal line count is
  unchanged, and the fixture bar's marker is absent. Red when: a second stdout line, any changed or
  added file, or a marker appears. The base hook, given the flag, reads it as a remote name, exits 0
  on an empty stdin and writes a journal pair.
  fixture: the warm-up absorbs git's own racy-index refresh, which a read-only hook does not cause.
- **AC7** — When `--decide` runs on a dirty tree, or with `<tip>` not equal to HEAD, it exits 1
  with an empty stdout and no `pre-push-refusal` file. With one argument, or a `<tip>` naming no
  commit, it exits 2 and prints a usage line on stderr. Red when: either case exits 0, or writes a
  refusal file.
- **AC8** — When `diff` compares the `remote_ladder_sh` block extracted from the hook with the one
  in `tools/lib/resolve-remote.sh`, both by `awk` over the `# >>> remote_ladder_sh` and
  `# <<< remote_ladder_sh` markers, it prints nothing. Red when: the copy drifts by a byte.
- **AC9** — When `--decide` runs with no `<remote>` in a clone with two remotes, a detached HEAD
  and no `GOV_REMOTE`, it exits 2 naming `GOV_REMOTE`. With `<remote>` given, it decides. Red when:
  it picks a remote nobody named.
- **AC10** — When `grep -n 'WHAT --decide DOES NOT CHECK'` and
  `grep -n 'WHAT THE POST-MERGE READ DOES NOT CHECK'` run over `.githooks/pre-push`, each prints one
  line. Red when: either sentence is absent.
- **AC11** — When AC6's covering `gate-bar-green` record is present and a declared red is an
  ancestor of the tip that the record's sha does not descend from, a push prints `pre-push: FULL gate`
  naming the red, and the fixture bar's marker gains a line. When the record's sha strictly descends
  from the red, the push prints `pre-push: covered` and the marker is unchanged. In the scoped state,
  the base `--decide` prints equals the `GATE_BASE` the stub bar records on a push of the same tip.
  Red when: a red the record does not descend from leaves the push covered, or the two bases differ.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `branch-guard self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `remote literals (kit code names no remote)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close runs these. A pass runs none of them. The python resolver leg's parity table already reads
`.githooks/*`, so the inline ladder copy joins its `remote_ladder_sh` row with no table edit.

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC9 AC11 · a bare remote with a hand-staged red ref, a declaration committed at R, a git shim counting ls-remote, an unreachable push URL and three decide states · none
New arm: .githooks/pre-push.runlog.test.sh · covers none · the new decide-mode exit sites, each an exempt row in the exit table · none

## 8. Open questions

- **F1 — what does `--decide` do where a push would be refused?** Print `full <why>`, or exit 1
  with an empty stdout. A refusal is not a decision, and the brief names exit 0 only for the three
  decisions. Recommendation: exit 1 with an empty stdout. Its caller already treats any output
  other than the three shapes as a fall-back to the full bar.
  RESOLVED (agent, 2026-10-09, delegated): exit 1, nothing on stdout, the message on stderr, and no
  refusal file. This refines the brief's exit-0 line without contradicting it, and §4 records the
  rejected option.
- **F2 — does a red on exactly the adopted green's sha clear?** Design D8 says "descends from".
  `post-merge.sh` deletes the ref on a green at the same sha, but the hook cannot order two verdicts
  on one sha. Recommendation: strict descent only, the forcing direction.
  RESOLVED (agent, 2026-10-09, delegated): strict descent. The case is stated in the header, and the
  next post-merge green clears it.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from design D8 and D9 and the spec brief.

## 10. Reuse audit

The seams are reused and none is re-implemented. `read_policy_key` and the blob `classify_docs`
already reads in `.githooks/pre-push` carry the declaration. The `remote_ladder_sh` block from
`tools/lib/resolve-remote.sh` resolves the remote under `--decide`, and
`tools/lib/resolve-python.test.sh` parity-gates its copies. The bounded-read shape is
`observe_remote`'s in `tools/unattended/unattended.sh`. `reuse_lookup.py` was asked "bounded remote
observation of a ref with a wall-clock timeout and no credential prompt". It returned `run_bounded`
and `resolve_remote`, among weaker name-stem hits. It did not return `observe_remote`, because it
ranks by name, so that seam was found by reading. The recall corpus confirms it through
`TOOL-aGraftedHelix-1`'s evidence section, which calls it "the one bounded network call". The hook
ships verbatim and sources no kit, so the shape is copied rather than called. No existing seam
fits "print a decision without acting on it": the hook has no dry-run mode today. The binding records
are the design record D8 and D9, `TOOL-dThriftyLanding-3`, which established the gate-env-at-R read
for the docs class, and `TOOL-aSurfacedLexicon-25`, the reason the decision line must never be
silent about a push it lets through.

Recall terms used: `python tools/memory-recall/query.py "how does the push boundary read a policy at the remote sha and bound a network call" --terms "pre-push read_policy_key GATE_DOC_PATHS INHERITED_RED remote sha ls-remote bounded observe_remote timeout decision forcing predicate"`
