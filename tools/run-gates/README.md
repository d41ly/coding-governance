# run-gates kit

`gov:kit run-gates@1.54` — the marker a deployer greps; paired with `KIT_RUN_GATES_VERSION` in
`run-gates.sh` and asserted EQUAL by `<prefix>/check-kit-versions.sh`. Presence of a marker is not
agreement between a marker and a constant, and this repo has twice had a half-bumped pair pass a
presence-only check.

## What this is

The merge-bar runner, its two harnesses, and the adopter that keeps a target's verdict-reading
declaration honest. The runner is a thin iterator over a leg manifest: it holds no leg command of
its own, and the canary asserts that.

## Exit codes

| exit | the bar | its last stdout line |
|---|---|---|
| 0 | GREEN: every leg that ran passed, over a tree that did not move, with at least one leg line reported and the run record's verdict file written | `gates GREEN — …` |
| 1 | RED: one or more legs failed and at least one of them is not HOST, or the whole-run wall fired | `gates RED — …` |
| 2 | REFUSED: not run from a repository, no usable python, a manifest or profile table it cannot read, a scratch dir or run record it cannot create, a manifest whose every leg is held, a run that reported no leg line (an empty manifest), a green whose verdict file was not written, or a declared generated output that is stale or unproven (see "Generated outputs") | a `run-gates:` line, or `gates REFUSED — …` |
| 3 | TREE MOVED: no leg failed, but the tree changed while the bar ran, so no verdict describes it | `gates TREE MOVED — …` |
| 4 | HOST: every failed leg timed out twice, the second time alone, while one spawn cost more than `GATE_HOST_RATIO` times this clone's recorded floor, so the verdict is about the host and not the subject | `gates HOST — …` |

**The precedence, first match wins: 2 REFUSED, 1 RED, 4 HOST, 3 TREE MOVED, 0 GREEN.** One leg that
failed for a reason of its own makes a bar RED however many others the host explains, and its RED
line names them as `(<n> HOST: <legs>)`. A HOST bar over a moved tree still exits 4, its line ending
`(the tree moved while the bar ran)`. HOST writes no `gate-full-green` stamp, keeps the failure record
a red keeps, and its run record says `verdict HOST`. Exit 0 is never taken on the status of the legs
alone: the pre-push hook reads `verdict GREEN` from the run record of the id it pinned after every
exit 0, and blocks a push whose record says anything else or nothing.

**Exit 3 never outranks a red.** A failed leg is a finding about some tree, so a bar that failed AND
moved exits 1, and its RED line ends `(the tree moved while the bar ran)`. A moved bar never writes
the `gate-full-green` stamp, and its run record says `verdict TREE MOVED`. Every caller that reads
any non-zero exit as "not green" — the pre-push hook is one — reads exit 3 correctly without
learning it. What to do about a moved tree, such as re-running once on a tree that has stopped
moving, is the caller's decision and not the runner's.

## A leg killed by its own ceiling gets one serial retry

A leg whose OWN ceiling fired — `timeout` exited 124, or 137 once the leg ran to its bound and ignored
the TERM — is not failed on the spot, because a bar under its own concurrency kills legs that pass in
a fraction of the time alone. It is printed in its manifest position as

```
GATE retry  <leg>  (timed out after <n>s beside <k> neighbours; retried in the pool's tail, and alone after it drains unless that passes)
```

where `<k>` counts the legs that were running when it timed out. Its chunk closes `pending`, never
`green`. The worker that saw the ceiling fire leaves a `<i>.defer` marker in the work dir, and once
every first attempt is dispatched the pool starts that leg's retry as soon as at most one other job
runs: the pool's TAIL, where the floor leg runs alone and the other slots sit idle. A tail retry that
passes is final. One that does not decides nothing: its files are set aside as `<i>.tail.*` and,
after the pool drains and inside the run's wall, the leg runs once more ALONE under its own ceiling,
as does a deferred leg the tail never reached. Each retried leg prints its final line after the drain,
in the order it was deferred: `GATE ok    <leg>  (retried after timeout)`, which counts green, or
`GATE FAIL  <leg>  (timed out after <n>s, again on its serial retry; …)`, whose note says whether
HOST was read and why not, so a red verdict and a HOST reading always come from an attempt that ran
alone. One `---- retry: <green|RED|HOST|killed>  (<n> retried, <m> failed)` line follows. Any other
137 — a self-kill, an OOM kill, an operator's or a CI cancel, under a bound or with none — is an
ordinary failure and is never retried; nor is an assertion failure.

**HOST is a ratio, never a wall clock.** Each bar with a bounded leg to run times ten spawns of one
external binary and keeps the lowest figure this clone has ever measured in `gate-spawn-floor` under
the git common dir, one `<per-spawn-ms><TAB><iso-utc>` line written tmp-then-rename. A leg that times
out on its retry is HOST when one more measurement then exceeds `GATE_HOST_RATIO` times the floor AS
READ before this bar measured, so a clone's first bar can never read HOST. The ratio is a constant in
the runner's source, not a conf key, and every HOST tail prints the ratio it measured. The timed-out
attempts' processes must be gone first: the worker kills whatever is left in the process group its
`timeout` led, and the retry pass verifies that before it measures, naming any survivor instead of
calling it another tenant. A descendant that left that group on its own is invisible to both.
`GATE_SPAWN_CMD` (what is timed), `GATE_SPAWN_FLOOR` (the floor file's path) and `GATE_VERDICT_FAULT`
(make the verdict write fail) are arm seams for the suites, not conf keys: the runner unsets each
once read, and the pre-push hook clears all three before the bar it runs.

The records keep every attempt: the first attempt's `<i>.leg` row reads `timeout` and a
`<i>.retry.leg` row sits beside it, with a set-aside tail attempt's `<i>.tail.leg` between them when
there was one, the verdict file gains `retried <n>`, and the ledger row takes the
retry's seconds. Its status is `retried` only where the retry exited 0, and otherwise the retry's
own, `fail` or `timeout`, so the ledger holds the leg's final verdict; reuse accepts neither, and a
red row carries no key. The drift report sums `retried` across the run records as
`legs_retried_after_timeout`.

**The same-tree re-run, `GATE_RERUN=1`** (TOOL-dWitnessedBar-8). Every other red is re-run only when
the bar is asked: after the serial retry and the reuse sample, inside the wall, each leg whose
effective result is a numeric red runs once more, alone, on the same tree, into `<i>.rerun.*` beside
its attempts and a `<i>.rerun.leg` row. A leg whose own ceiling fired is not, its quiet-host re-run
being `TOOL-dWitnessedBar-30`'s, and a bar whose wall fired re-runs nothing. The re-run moves no
verdict and no exit code, and writes no `gate-logs` file, so `log:` keeps naming the attempt that
redded the run; a red-then-green leg prints `nondeterministic · <leg>`, as the sample does. The
runner reads the knob once and unsets it, so a nested bar never inherits it; the unattended driver's
`gates-green` bar sets it, and `verdict_flow.py route` and `flakes` read the rows it leaves (see "Which
red blocks").

## The switch every adopter needs to know about

**A leg declaring `subject = "kit"` is HELD.** It does not run on your bar unless you ask:

```bash
GATE_SELFTESTS=1 bash <prefix>/run-gates/run-gates.sh
```

A kit-subject leg is a self-test of a KIT'S OWN SOURCE — it stages a break into a copy of a checker
and asserts the checker still catches it. That job exists when the kit's source changes, and it does
not exist in a repository that copy-installs the kit and never edits it. Run them once when you
install or upgrade a kit, and after that only when you edit one.

**`GATE_FULL=1` does NOT unlock them.** It means *ignore every leg guard*, and a kit's own tests are
not a guard. A green bar without `GATE_SELFTESTS=1` says nothing about the kits — and the runner
says so itself: held legs get their own verb, `GATE held  <name>  (<source>, <note>)`, are
subtracted from the total, and are counted by source in the summary,
`gates GREEN — <n>/<n> legs passed (<n> held: <n> kit, <n> quarantine, <n> level; GATE_SELFTESTS=1 runs the kit ones)`,
a source with none left out. How many legs this repository holds is read from
`python <prefix>/run-gates/leg_factory.py --conform`, whose count line ends `· <h> held · <u> unguarded`,
never typed here.

A leg that declares no `subject` defaults to `repo` and runs, so nothing you already had changes
behaviour by arriving here. A whole manifest of held legs is REFUSED rather than reported green,
because a bar that executed nothing is not a bar that passed.

The state reaches two other readers: the deployer, which reads a held leg as `held` rather than as a
leg that vanished, and the `gate-full-green` stamp, which records whether the run covered them so a
push boundary cannot mistake a partial bar for a whole one.

A held kit leg with a `guard` still skips under `GATE_SELFTESTS=1` when nothing it guards moved; one
with none runs whole. That choice is declared: `leg_factory.py --conform`'s `held guard` arm refuses a
held declaration carrying neither a guard nor a descriptor-only `unguarded_why`, the reason it runs
whole, and refuses one carrying both.

### Held by policy — the hold sources, the selection record and `verdict.held`

Held is a policy over any leg (TOOL-dWitnessedBar-5). One predicate, `derive_hold_source`, names the
SOURCE a leg is held by: `kit`, derived from the row as above; `quarantine` and `level`, read only
from the selection record `GATE_SELECTION=<path>` names. That record is written at a revision R by
`python <prefix>/run-gates/verdict_flow.py select --rev <R> --out <path>`, from inputs read at R and
never from the working tree: a header naming the values it read, then one TAB row per held leg,
`held · <leg> · <source> · <note>`. A `quarantine` row is a leg an OPEN held-flaky-leg ask names
(TOOL-dWitnessedBar-8), its note `<count>/<window>, ask <id>`, printed `GATE held  <leg>  (quarantine,
<note>)`: the asks are those the `ASKS_CMD` generator `.unattended.conf` declares at R prints, run in a
scratch worktree at R, so a branch cannot quarantine a leg it breaks, and none where R declares no
generator. A `level` row is a leg whose `level` is outside
`tests.landing-levels`, none under `every-declared` or while `tests.without-cadence` reads
`run-at-landing`. A selection-held leg is held whatever `GATE_SELFTESTS` says. A row whose source is
outside `quarantine level`, `kit` included, or whose leg the manifest lacks, is printed and ignored,
and its leg runs. The runner copies the record into the run record as `selection`, and the pre-push
hook runs `verdict_flow.py select --check --run <run dir> --rev <R>` before it admits a verdict made
under one: a row R does not derive refuses the push. The run record is the worktree's own and is swept,
so the per-tree verdict carries the same rows as `selection` and `selection.<n>` (TOOL-dWitnessedBar-41,
see "The verdict per tree"), and the hook re-derives them with `select --check --selection <path>`
before it adopts that record from any worktree.

The verdict record carries one `held.<n>` key per held leg beside the `held` count,
`<leg> · <source> · <result>`, the result `unrun` for a leg the bar did not execute.

A row's fifth field is its MODE, `hold` or `run`, a four-field row reading `hold` (TOOL-dWitnessedBar-30).
A `run` leg executes in its ordinary slot, past its guard, the docs mode and the reuse cache, and
writes its `.leg` row, so the flake record of a bar it ran in holds its result; that result is its
`held.<n>`, `ok` or `fail`, printed `GATE held  <leg>  (quarantine, <note>; run outside the verdict:
<result>)`, counted in `held` and never in `failed`, what ran or the verdict. `select` writes a
`quarantine` row `run` when the leg's newest executed row in the flake records at R since its hold, the
committer date of the commit filing its ask, ended more than 24 hours before the selection, or there is
none, whatever `verdict.held` reads, so a quarantined leg runs at least once a day in any Test-step bar
and its greens accrue; every other row is `hold`. `select --check` compares leg, source and note, never
the mode. THE RELEASE: a quarantined leg whose rows since its hold open, newest first, with
`verdict.flakes.release` greens (first rc 0; three by default, a red resetting the count), or whose
manifest row at R differs from its row at that filing commit, is selected as ordinary, and `select`
prints `release  <leg>  <ask id>  <reason>` naming the streak's run ids or the row change. The
unattended driver's `gates-green` runs `select` at R after its bar on every return code, beside its
held-job reader, and writes each such ask's `- CLOSED · <id> · by <HEAD> · <why>` row through its
`write_ask_closing`, staged with the views it moves. No caller hands a bar a selection yet: that is the
loop engine's Test step.

`verdict.held` decides when held legs run: `on-demand`, the default and gov's, holds them at every bar
unless `GATE_SELFTESTS` asks; `push-selected` makes the pre-push hook export `GATE_SELFTESTS=changed`
for its bar when the pusher set nothing; `peer-or-cadence` holds them at the push and needs a runner
declared elsewhere, `HELD_CI_WORKFLOW` in `.unattended.conf` at R, or `select` exits 2 naming it.

### `GATE_SELFTESTS=changed` — only the held legs whose kit moved

A developer tool, and a Definition-of-Done one: no push boundary sets it (TOOL-aSparedSpawn-12, owner
ruling F1) unless `verdict.held` reads `push-selected` at R. A held leg executes when any of these
holds, and is otherwise held with `GATE held  <name>  (kit, unchanged since <sha8>)`:

- it has no last-run record, an unreadable one, one whose sha is not an ancestor of `HEAD`, or one
  earned under a different manifest row;
- the record sits more than `GATE_SELFTESTS_MAX_LAG` first-parent commits behind `HEAD` (default
  10, the value of the push boundary's `GATE_FULL_MAX_LAG`), so no `changed` run holds a suite on a
  record that old;
- a path in its selection set differs between the recorded sha and the working tree.

The selection set is the owning kit's shipped sources in govkit's epoch roles
(`govkit.py shipped --epoch`, the same rows the version-bump rule reads) plus the suite file; the
owner is every govkit entry whose `shipped` rows carry one of the leg's suite files. A leg no kit
owns, and every leg when govkit cannot be reached, selects by its `guard` plus its suite file, and the
bar says so once. Each executing leg gets a `run-gates: selftests changed: <name> runs (<reason>)`
line before dispatch.

The record is one file per held leg under `<git-common-dir>/gate-selftest-last/`, shared by every
worktree of the clone. It is written only by a leg that executed green on a tree that was clean when
the run started and did not move, under any non-empty `GATE_SELFTESTS`, so a `GATE_SELFTESTS=1` run
seeds every record; a red or a retried pass removes it. The `gate-full-green` stamp of such a run
says `selftests changed`, never `1`, and a push that runs the self-tests forces over it.

Manifest order drives five readings, so moving a row is a change to each of them and never a no-op:
the dispatch tie-break (legs dispatch largest-first by recorded seconds, and a tie keeps manifest
order because the sort is stable); the report order, every `GATE` line and every `GATE warn` line, so
the output is byte-stable at any width; the `fail.<n>` indices of the run-log line, numbered in that
order up to their cap; the spec-token checker's `--legs-for`, which names each leg's first tripping
guard in that order; and the held halves, whose `held_halves.py` partition lists each half's held legs
in that order.

## Why it became a kit

It was a registry EXEMPTION, with two stated reasons that were both exact. It sourced `<prefix>/lib/`,
which is gov-internal and never travels; and with that path absent, `bash` sourcing a missing file
under `set -u` continues, `resolve_python` is undefined, and the guard on the next line fires — the
runner exited 2 having run ZERO legs. So `govkit apply` wired legs into a runner the target was
assumed to already own, and a target that owned none received a merge bar that could not start.

the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` cut that dependency by inlining the canonical resolver into every shipped
file that had one, byte-identically, under the markers `<prefix>/lib/resolve-python.test.sh` greps for
— so each copy enrols itself in the parity gate rather than needing a table row.

## The pieces

| file | what it is |
|---|---|
| `run-gates.sh` | the runner. Legs run through a bounded pool, at the width `gate-profiles.txt` declares for the detected hardware; `GATE_JOBS` overrides the width alone |
| `gate-profiles.txt` | the DECLARED knob table: rows of name, minimum cores, minimum RAM MB, knobs, most-capable-first with a zero-threshold catch-all last. `GATE_PROFILE=<row>` selects one by name and skips detection; `GATE_PROFILES=<path>` reads a different table, and an absent path falls back to the built-in formula — which is the rollback. `GATE_CORES` / `GATE_RAM_MB` replace the detected readings and bypass detection, and `GATE_CGROUP_ROOT` relocates the cgroup files the RAM chain reads |
| `lib-attribute.sh` | the attribution's two shared halves, SOURCED and never run: the normaliser (`write_normaliser`) and the detached scratch worktree at a base (`add_scratch_worktree` / `remove_scratch_worktree`). The runner sources it only when `GATE_ATTRIBUTE` is set and a leg is red, and `run-selftests.sh` only under `--attribute`, so a copy of either runner without it still runs every other mode |
| `lib-verdict.sh` | the block table, SOURCED and never run: `derive_red_blocks <value> <class>` prints `block` or `pass` for one attributed red under a `verdict.blocks` value. The runner sources it beside `lib-attribute.sh`, and it is in KF3's list; see "Which red blocks" |
| `verdict_flow.py` | a red bar's reds routed (`route --run <run dir>`, the routing record) and the tester's judgment of an `attribute` route recorded (`judge`), see "Which red blocks"; and the selection record a bar holds legs by, written at R (`select --rev <R> --out <path>`) and re-derived there (`select --check --run <run dir> --rev <R>`, or `--selection <path>` for a per-tree verdict's rebuilt rows), see "Held by policy"; and a red bar's `flake` record with the holds it justifies (`flakes --run <run dir> --build <slug> --unit <id>`, and `flakes --check`), see "Which red blocks" |
| `post-merge.sh` | the post-merge bar: the full bar on a landed sha, run through `--hold` in a scratch worktree, its verdict published as the remote ref `refs/gov/bar-red`; see "The post-merge bar" |
| `gate-fingerprint.sh` | "what tree is this, exactly", in two forms. With no argument it digests the tree object at `HEAD` plus the sorted porcelain lines plus the blob hashes of every dirty-or-untracked file, both walked with `--untracked-files=all` so a file inside a new directory is hashed rather than collapsed into its `?? dir/` line; with a `<rev>` argument it digests that rev's tree and supplies the other two components EMPTY. On a CLEAN tree the two forms agree, which is what lets a hook ask whether a recorded green still describes the commit it names. Empty output on any failure — a caller that cannot measure must see nothing rather than a partial digest |
| `profile_bar.py` | the profiling verb: runs the bar, records it as a RUN, and names the regime — floor-bound or packing-bound — so the next fix is chosen from a measurement |
| `profile_bar.test.sh` | the profiler's own arms |
| `bar-wall-evidence.txt` | gov's whole-bar wall time per node, written by `GOV_NODE=<tag> python profile_bar.py --record`; withheld from the payload |
| `precommit.py` | the derived commit-time list behind `--precommit`: every manifest row's `precommit` argv its `guard` trips; see "The commit-time list is derived" below |
| `keep_tails.py` | the keep verb: a red run's failing-leg tails, which the runner keeps by hash, committed as `leg-tail` records under `trace.leg-output = "tail-by-hash"`; see "The run record" below |
| `product_tests.py` | the product-test contract: the rows carrying `level` graded against `tests.product`, and the runner adapters' rows the leg factory renders; see "The product-test contract" below |
| `measure_legs.py` | the gate profiler: every manifest leg run clean and unbounded, serially or under a load cap, each in its own Windows Job Object and profiled to its processes; see "The gate profiler" below |
| `fixtures/measure-legs/` | the fixture legs and manifests `measure_legs.py --selftest` runs |
| `run-gates.test.sh` | the SHIPPED canary — every assertion here is true in any tree |
| `run-gates.gov.test.sh` | the GOV-ONLY arms, withheld from the payload; see below |
| `run-gates.evidence.test.sh` | the durability arm: a red leg's output survives on disk |
| `run-gates.turnstile.test.sh` | the turnstile arms: peak occupancy, reaping, FIFO order, release on every signal |
| `run-gates.runlog.test.sh` | the run-log arms: one line per bar on every exit path after the trap and on every caught signal, and the `SPAWNS` arm's per-leg spawn ceiling, withheld from the payload |
| `adopt-run-gates.sh` | `--check` asserts a target's `[gate_runner]` declaration still matches this runner's output strings |
| `adopt-run-gates.test.sh` | the adopter e2e, gated on EFFECTS rather than exit codes |
| `check-receipt.py` | the leg `receipt sync (installed files match the receipt)`: every engine row of `.governance/install.json` still on disk and still hashing to its recorded sha256, or, where the raw bytes miss, hashing through the target's own clean filter to the row's `oid` while the raw bytes' blob does not: that row is graded clean and counted `eol-only` on the summary and `ok` lines, the rule `govkit check` applies, in one `git hash-object --stdin-paths` spawn for every such row. A row with no `oid`, a real edit, a CRLF copy no filter normalizes, a tampered `sha256` over bytes that are the blob, a tree with no `.git` and a git refusal all still red, the last two with a `GIT` line naming why. The INTEGRITY half only — it reads no `source`, `commit` or `gov_oid`, because those resolve against a gov checkout an adopter does not have, and it grades no `seed`, `merged`, `attributes` or `forked` row. A tree with no receipt is an announced `SKIP`, and the built-in fixture arms, the eol-only ones over real git repositories, run on every invocation so the leg has a verdict there too; its `fixtures:` line prints their count |
| `run-held-wsl.sh` | the held tier split in two: its Linux-safe legs in WSL2 from an ext4 mirror, the declared Windows-only legs natively, one combined verdict; see below |
| `held_halves.py` | the split's partition, host resolution, combiner and parity record, with a `--selftest` that builds its own synthetic halves |
| `windows-only-legs.txt` | gov's declaration of the held legs that run natively, one `<leg> TAB <reason>` row each; withheld from the payload |
| `regen.py` | the generated-output verb behind `--regen`, `--regen-check` and `--regen-list`: it reads the staged `[[generated]]` and `[[regenerate]]` rows of every tracked kit descriptor and regenerates them in stage order, or proves each fresh without writing; see "Generated outputs" below |
| `pass_legs.py` | the pass-leg declaration: derives which legs a unit pass runs from recorded reds per evidenced second and writes `pass_leg` onto their manifest rows; see "The pass legs" below |
| `pass-legs.sh` | the pass-leg runner: runs the declared pass legs over one pass's diff through `run-gates.sh`, writes a run record and prints an overrun or a held leg as a finding; see "The pass-leg runner" below |
| `pass-leg-evidence.txt` | gov's recorded reds per leg, written by `pass_legs.py --write`; withheld from the payload |
| `kit.toml` | this entry, declared as data |

## Generated outputs — declared by the kit that writes them

A merge bar grades generated outputs for freshness: the build index, the bug-class index, the
codebase map, and the Skills and guides the kits render from templates. Each one is declared in the
descriptor of the kit that generates it, so the set is read from the kits and never kept as a list
here (TOOL-aPrimedIndex-1).

| table | keys that make a row an item | the item's check |
|---|---|---|
| `[[generated]]` | `write` and `check`, argv arrays, and `stage`, an integer; all three or none | the row's `check` |
| `[[regenerate]]` | `stage`, plus an optional `check` argv | the row's `check`, else the kit's `[check]` argv |

The argv tokens are the four the descriptors already spell: `{kit}`, `{prefix}`, `{memory_root}`
and `{map_root}`. An argv beginning `python` or `python3` runs under the reader's own interpreter.
Rows sharing one write and one check are one item.

A `[[generated]]` row may carry a `when`, and is no item where it does not hold. It has two forms,
and neither runs a command; any other spelling is refused (TOOL-dWitnessedBar-45):

| `when` | holds when |
|---|---|
| `"<conf file>:<KEY>=<value>"` | the conf at the repo root reads that value for the key |
| `"exists:<path>"` | the path, its tokens resolved as an argv's are, exists in the tree; resolved to an absolute path (`/…`, `X:…`) or one holding a `..` segment, it is refused (TOOL-dWitnessedBar-62) |

The leg factory's row carries `when = "exists:{prefix}/govkit/govkit.py"`: its render reads govkit,
which never reaches an adopter, so an adopter's `--regen-list` names the row skipped and its bar
does not refuse at stage 1 on a check that cannot run there.

**Stages run in order, the items of one stage concurrently**, because one stage's outputs are
disjoint and a later stage reads an earlier one's:

| stage | what it holds |
|---|---|
| 1 | renders from kit templates: the Skills, the rendered guides and documents, the charter region |
| 2 | indexes over the records: the build index and its views, the bug-class index |
| 3 | the codebase map, which reads the output of both earlier stages |

A row with none of the keys keeps exactly its old meaning: the unattended kit reads `[[generated]]`
for its write-set rules and govkit runs `[[regenerate]]` argvs, and neither reads these keys.

### `--regen`, `--regen-check`, `--regen-list` — one command for every declared output

`regen.py`, beside the runner, reads the declarations above and is reached through the runner's
first argument, so it needs no python launcher of the reader's own (TOOL-aPrimedIndex-2):

```bash
bash <prefix>/run-gates/run-gates.sh --regen         # run every write, stage by stage; prints what each stage moved
bash <prefix>/run-gates/run-gates.sh --regen-check   # run every check; writes nothing
bash <prefix>/run-gates/run-gates.sh --regen-list    # the resolved items, in run order
```

The tree is the current directory's git toplevel; the descriptors are the tracked `kit.toml` files
one directory below the tool root, where this kit sits in its own repository. `--regen` names any
untracked file first, because the build-index generator enumerates tracked files and does not see a
record until it is added. A write that exits non-zero is followed by its own check: a fresh check
makes it `declined`, which a kit's adopter is when it renders nothing in a state its kit declares
legal, and the stage goes on. A write whose check is not fresh FAILS, and a failed write stops
before the next stage. `--list` names every row it skips, each with its reason: a `[[regenerate]]`
row for carrying no stage, a `[[generated]]` row for a `when` that does not hold.

| exit | `--regen` | `--regen-check` |
|---|---|---|
| 0 | every write ran | every item fresh |
| 1 | a write failed, or timed out, and its check is not fresh | an item stale, its check failed, or it timed out |
| 2 | REFUSED: a descriptor that does not parse, a malformed row, an unresolved token, a script an argv names that is not in the tree, no repository | the same |

`GATE_REGEN_JOBS` bounds concurrency (default 4) and `GATE_REGEN_BOUND` bounds each command in
seconds (default 900). A command's output goes to a file and never through a pipe, so the bound
holds whatever its children do; a command outliving it is killed with its process tree (`taskkill
/T` on Windows, its process group on POSIX), and an MSYS fork can still escape Windows parentage. A
`bash` argv runs under the bash `profile_bar.resolve_bash` finds by running each candidate, never by
`PATH` order, which reaches WSL's first on a default Windows `PATH`. **What it does not check:** that
a write writes what its row names, or that a check grades it; a check red for a reason a regeneration cannot fix reads as stale, and its output
tail is printed so a reader can tell.

### Every bar proves them fresh before it queues

After its profile and process-monitor lines and before the host turnstile, the runner runs
`regen.py --check`. A stale, failed or timed-out item, or a declaration the verb refuses, ends the
run with exit 2, REFUSED, before any leg, naming `--regen` and saying to commit what it moves
(TOOL-aPrimedIndex-3); a refused declaration gets its own line, because `--regen` cannot cure it. Before the queue, because a refusal after an hour in another bar's queue is
the cost the check exists to remove. Every bar entry point reaches the runner — a hand-run bar, the
pre-push hook, the lander's push, the unattended close and remote CI — so this binds all of them.
govkit's `apply` reads the runner too, for its baseline and after verdicts, and runs it with the
check skipped, because it compares legs and a stale output reads there as its own leg's red
(DEPL-aPrimedIndex-1).

The runner never regenerates the tree it grades: at the push boundary the hook refuses a dirty tree,
and a green earned over an uncommitted regeneration could never be reused. A tree with no kit
descriptor at the tool root prints one line and spawns nothing. `GATE_REGEN_CHECK=0` skips the
check with a line naming the knob. A stale output then reds only where its own leg runs in that bar,
and a guard can skip that leg, so a skip can turn a refusal into a green. The pre-push hook therefore
scrubs the knob from the bar that lands (TOOL-aPrimedIndex-6), and from the bars whose green they record
the hook, post-merge (`PM_SCRUB`) and the unattended driver (`_gknobs`) all drop `GATE_REGEN_CHECK`
(TOOL-dWitnessedBar-60).

### The lander regenerates over its merged tree

`<prefix>/push-main.sh` is the verb's second caller (TOOL-aPrimedIndex-4). `--prepare` runs
`regen.py --write` over the merged tree after the version mint, and what it moved enters the
prepared merge the way the mint's output does, same parents and same subject. The attended landing
runs it on every attempt after its mint commit and commits what moved as its own commit, subject
`regen: generated outputs onto <remote>/<default> at <sha8>`, with a `Pass: none` trailer. That is
what keeps a reconcile merge, which leaves the `merge=ours` indexes stale, from meeting the push
bar's refusal. A failed write refuses the landing: `--prepare` leaves the branch where it was, and
the attended landing keeps the reconcile merge and the mint commit it already made on the local
default branch, as a refused mint does. Either way the files the regeneration created are cleaned
(TOOL-aPrimedIndex-8). A lander with no `regen.py` beside it says so in one line and lands without
it.

## Reuse, and the baseline a guard diffs against

Reuse skips a leg whose inputs are byte-identical to a recorded green. There are three modes, two
over the CACHE and one over the LEDGER, each asked for by its own knob, and a run takes ONE of them by
the table below (TOOL-aSparedSpawn-32, composing TOOL-aSparedSpawn-13's cache with
TOOL-aFrugalTurnstile-4's lineage). The runner reads the three knobs once, records the mode as the run
header's `reuse` key, `off`, `env`, `push` or `lineage`, and unsets all three before any leg starts,
so a leg's nested runner never inherits a mode. Any missing term of a mode means execute — every
failure mode is "did more work", never "checked less".

| `GATE_FULL` | `GATE_REUSE_LINEAGE` | `GATE_REUSE_PUSH` names HEAD | `GATE_REUSE` | mode | named on stderr as not used |
|---|---|---|---|---|---|
| set | set | any | any | `lineage` | `GATE_REUSE` and `GATE_REUSE_PUSH`, when set |
| set | empty | any | any | `off` | `GATE_REUSE` and `GATE_REUSE_PUSH`, when set |
| empty | any | yes | any | `push` | `GATE_REUSE_LINEAGE`, when set |
| empty | any | no | set | `env` | `GATE_REUSE_LINEAGE`, when set |
| empty | any | no | empty | `off` | `GATE_REUSE_LINEAGE`, when set |

`.githooks/pre-push` never sets two of them for one bar: it clears every inherited one first, then sets
`GATE_REUSE_LINEAGE` only on a FULL decision and `GATE_REUSE_PUSH` only on a SCOPED one, so the table
governs a direct caller. `GATE_FULL` keeps meaning "no cache reuse", and the boundary's lineage run is
the one deliberate exception, because its reused verdicts were earned by full runs.

**What the stamps record.** `gate-full-green` carries `reused`, the legs the run carried forward, and
`reused_cache`, the legs it took from the cache. A run that reused anything from the cache stamps
neither `gate-full-green` nor the inherited green, so `reused_cache` is always `0` there, and a full
green carries `reused` above 0 only from lineage. The push boundary's predicate 9 forces the full bar
over a non-zero `reused_cache`, and over a record with no `reused_cache` and a non-zero `reused`, which
was written before the field existed and cannot say its kind. The inherited green records `reused 0`
and `reused_cache 0`.

### The cache, `env` mode — `GATE_REUSE=1`

`GATE_REUSE=1` skips a leg whose inputs are byte-identical to a recorded green: it carries no legacy
`impure`, a `remote` leg has an observed remote, its row is not quarantined, the cache in the git
common dir holds an `ok` under the key computed this run, it has not been reused on 10 runs in a row,
and the sample did not draw it. It is OPT-IN because an advisory input may cause less work only on a
run that is not authoritative, and a run you ask for by hand is not one.

### The cache, `push` mode — `GATE_REUSE_PUSH`, at the boundary's SCOPED decision

An authoritative run reuses only a `remote` or `history` leg, at the exact pushed sha and observed
tip, and is then scoped: `.githooks/pre-push` sets `GATE_REUSE_PUSH` to `<pushed sha> <tip>
<advertisement digest>` on a SCOPED decision whose `ls-remote` probe agreed with the remote sha git
handed it, and on no other, and it clears `GATE_REUSE`. The terms are the env mode's, narrowed to those
two classes, and the mode holds only while HEAD is the pushed sha.

The push key's environment is the caller's, restored: git starts the hook with `GIT_EXEC_PATH`, its
exec path at PATH's head and, on Git for Windows, `LC_CTYPE=C.UTF-8`, none of which a direct bar from
your shell had. So beside `GATE_REUSE_PUSH` the hook writes the environment as it was before git, with
those additions taken back out, to a file in the git dir, and names it in `GATE_REUSE_DIGEST_ENV`; in
this mode alone the digest reads that file in place of the runner's own environment, and a file that
cannot be read fails the digest. The legs still run under the hook's environment: only the key reads
the caller's. A value the hook cannot tell from git's own is left out, which costs a saving and never
a verdict.

**What a leg reads beyond its inputs** is declared on its manifest row as `reads`, an object mapping
a class to a one-line reason. The classes are closed, and each puts one thing into the key:

| class | the key takes | for a leg that |
|---|---|---|
| `base` | the resolved baseline and `GATE_PUSH_BASE` | diffs against a merge-base or the push base |
| `history` | the `HEAD` sha | reads commits, so a commit moves it with the tree unchanged |
| `clock` | the UTC day (`GATE_REUSE_DAY` pins it) | compares against today |
| `remote` | `HEAD`, the default branch's advertised tip and the digest of the whole `ls-remote --heads` advertisement | observes the remote |

A leg that declares none is keyed on its inputs alone, so a landing that moves the baseline no longer
misses it. A legacy `impure`, a class outside the four, or a `reads` that is no object is read as
`remote` and never reused, so an adopter's `impure` keeps its meaning; govkit writes a descriptor's
`reads` into an adopter's row as that legacy `impure`. A `remote` leg is keyed only when the runner
probes the remote (one bounded `ls-remote --heads`, on a clean tree, when such a leg is still to run)
and caches its verdict only when a second probe after the legs end reads the same advertisement.

**The cache** is one file per key under `<git-common-dir>/gate-cache/<key[0:2]>/<key>`, holding `ok`,
seconds, run id, `HEAD`, an epoch and its reuse count, so every worktree of a clone shares it and nothing pushes it. It
is written only by a leg that EXECUTED `ok` on its first attempt on a tree that was clean when the
run started and did not move, with its count at 0; a reused leg rewrites only its count, so a wrong entry cannot carry itself
forward. Every write and the prune of entries older than 30 days run in one python process at run
end. `gate-ledger.tsv` is the dispatch-duration hint and the lineage mode's store; neither cache
mode reads it.

**The soundness sample.** On a reusing run each reusable leg is drawn for execution at
`GATE_REUSE_SAMPLE` (default `0.25`, uniform per leg, seeded from the run id so a draw replays). A
drawn leg that executes green agrees. One that reds against its cached `ok` has redded the run and
runs once more: red again prints `cache disagreement · <leg> · <key>` and erases the entry, red then
green prints `nondeterministic · <leg>`, and either quarantines the leg (`quarantine.<name key>` in
the cache dir) until its manifest row changes. A leg reused on 10 consecutive runs executes on the
next whatever the draw, so a wrong entry lives at most that long. The count is kept per KEY, in the
entry itself: only an execution under that key resets it, by writing a fresh entry, and an execution
under another key, a dirty tree's for one, leaves it alone. Each fact is on the leg's own line, under
the two-space tail: `GATE ok    <leg>  (sampled against a cached ok)` for a drawn leg, and
`(executed: reused on 10 runs in a row)` for one the bound forced, on its `GATE ok` or `GATE FAIL` line.
An executed red against a cached `ok` erases the entry and quarantines the leg,
whatever drew the execution: the age bound, a plain bar, or a push-mode bar that may not reuse
that leg. Only a drawn leg runs once more to classify; any other takes its effective verdict, its
serial retry's where it had one, and prints `cache disagreement · <leg> · <key>`.

The key takes the leg's argv, its manifest row (classes and row hash), the declared reads above, and
its inputs: for a guarded leg the `git ls-files -s` of its guards plus the walk rows under them, each
`<XY> <blob-or-dash> <path>`, the blob hashed at run start from one `--untracked-files=all` walk; for
an unguarded leg the working-tree fingerprint. Every key also takes `REUSE_SCHEMA`, a runner constant
bumped when what a reusable `ok` means changes, and one digest per run of bash, the MSYS or Cygwin
runtime, python and its UTF-8 mode, `git version` and its `core.autocrlf`/`core.eol`, the resolved
location of every tool a leg names, and the exported `GATE_* GOV_* *_PY GIT_* PYTHON* LC_* LANG TZ
PATH` variables, less every `GATE_REUSE*` knob, `GATE_TURNSTILE_HELD`, `GATE_TURNSTILE_HOLDER`, `GATE_RUN_ID`, and `GATE_BASE`
and `GATE_PUSH_BASE`, which enter only a `base` leg's key. Each `/bin` in PATH is read as `/usr/bin`
where the two are one directory, for the PATH line and the tool locations alike. It does NOT see a tool other than git
upgraded in place at the same path, a variable outside that set, or a read no class names, which is
what the sample exists to catch. A failed walk or digest makes the key a dash, which never matches,
and a run that would have reused or cached says so once on stderr: `run-gates: reuse — the input
keys could not be measured (<step>), so nothing is reused or cached this run`.
The header's `reuse_schema` and `reuse_sample` keys say how a run keyed and drew.

### Lineage — `GATE_REUSE_LINEAGE`, at the boundary's FULL decision

`GATE_REUSE_LINEAGE`, honoured only beside `GATE_FULL`, reuses a leg from `<git-dir>/gate-ledger.tsv`
and never from the cache: the leg is not declared `impure`, a `remote` leg has an observed remote, its
row says `ok`, the row's input key equals the one computed this run, its `full` field reads `1`,
meaning the run that earned it set `GATE_FULL` on a clean tree, its `manifest_blob` is this run's, and
its `head` is an ancestor of `HEAD`. A run whose every reuse meets those terms may still stamp
`gate-full-green`, which records the count as `reused`. `.githooks/pre-push` exports this mode on its
own FULL decision for this runner, and on no other decision or bar. That FULL line ends `— reuse:
lineage`. So after a red push, the fix push re-runs the failed legs and the legs whose key moved, and
nothing else. The key's base term ties one chain of reuses to one remote base, because a landing moves
the base and voids every key.

WHAT LINEAGE REUSE DOES NOT CHECK: that a reused leg's guard names every input the leg reads, or
that its verdict depends on the tree alone. A reused verdict is only as good as its input key, so
a too-narrow guard or an undeclared `impure` leg is carried forward until its key moves, the
remote base moves, or a run without `GATE_REUSE` re-executes it — the post-merge full bar is that
run.

The ledger is per git dir, so a bar run in one worktree feeds lineage only to pushes from that
worktree. A row written before these fields existed has an empty `full` and is never
lineage-reusable.

### The baseline

The baseline a guard diffs against is the MERGE-BASE with the default branch, so a branch is graded
on what it changed rather than on everything that landed while it was open — used only where the
merge-base is a proper ancestor of `HEAD`, with the remote tip standing otherwise. The remote and its
branch are the remote ladder's: `GOV_REMOTE`, else the current branch's remote, else the only one, and
the branch its HEAD names. `GATE_BASE` outranks both, and an unresolvable baseline, a ladder refusal
included, runs every leg.

## The docs mode — `doc_reads` and `GATE_DOCS_BASE`

A leg may declare `doc_reads`: the repo paths of the repository's doc class it reads, each a file or a
directory ending in `/`. `GATE_DOCS_BASE=<rev>` turns the docs mode on. In it, a leg that declares the
key runs only when one of those paths moved since `<rev>`, in the net diff or in any commit of the
range, and a declared `[]` skips. A leg that declares nothing is decided as before, so a missing
declaration costs time and never coverage. Each docs skip prints `GATE skip  <leg>  (docs-only: …)`
and counts as a skip, so a docs run never stamps `gate-full-green`. `GATE_FULL` outranks the mode; an
unresolvable `<rev>` turns it off and says so; the runner withholds the variable from its legs.

`.githooks/pre-push` sets it, to the remote tip R, on a push it classifies doc-only against the
`GATE_DOC_PATHS` declared in the gate-env file at R. The deployer carries a kit leg's `doc_reads` into
an adopter's manifest, all or nothing, only once the adopter's runner reads the key (1.25 and up).

A full green earned in a LINKED worktree is copied to `gate-full-green.shared` in the common git dir,
and the hook reads it after its own git dir's stamp and the primary's, so a green earned in a run's
worktree serves the primary tree's push. It is one slot per clone, last writer wins: a second
worktree's green evicts the first, which costs that push its saving and never its verdict.
TOOL-dThriftyLanding-1, -2, -3.

## The turnstile — `slots` bars per host, one by default

A run claims a beacon in a HOST directory before it dispatches: `GATE_TURNSTILE_DIR`, else
`~/.gov/gate-turnstile`. Every repository on the machine shares it, because bars from different
repositories contend for the same cores and memory (`TOOL-aFrugalTurnstile-5`); the health log and
the scratch sweep stay per git common dir. A host dir that cannot be created falls back to the common
dir for the beacon and the queue, with a NOTE, which is per-repository queueing. A runner older than
this keys on its common dir and does not see the host beacon, so serialization is complete only when
every repository on the host carries this runner.

**The turnstile admits `slots` holders at once** (`TOOL-aPairedSlots-2`), the selected profile row's
`slots` knob, 1 where it declares none, `GATE_TURNSTILE_SLOTS` over it. Each holder owns its own
beacon directory: slot 1 is `gate-bar-beacon`, slot k is `gate-bar-beacon.<k>`. The queue is still
one FIFO: only the ticket that sorts first claims, it takes the first free slot, and it gives up its
ticket at once, so a second free slot goes to the next ticket one tick later. A waiter reaps a dead
or stalled holder slot by slot, each removal guarded by the nonce it judged, and a release frees only
its own slot. Above one slot a queued bar's line reads
`<k> of <n> bar slots on this host are held — <repo> run <id> pid <pid>[; …] — queued at position N (waited Ns)`
and the run record's header gains `slots` and `slot`; at one slot nothing printed or written changes,
except where a bar's own worktree holds it back, as the next paragraph says.
A host whose repositories declare different counts admits the LARGEST, since every runner claims
among its own slots and all share slot 1 and the queue: a runner older than this claims slot 1 alone.
A count above 64 is refused in a row and ignored, with a NOTE, in the override.

**A worktree holds one bar at a time** (`TOOL-aPairedSlots-5`, `TOOL-aPairedSlots-15`). Everything
under a worktree's git dir — its ledger, run records, gate logs and summary — assumes one writer, so
a bar does not claim while any holder present names its own top level: a slot at any count, or a
docs beacon. A head held back that way waits, keeping later tickets behind it, and its line names
that holder: `… this worktree's bar holds <slot k|the docs key> — <repo> run <id> pid <pid> — queued
at position N (waited Ns)`. Two worktrees of one repository have two git dirs and run at once.

**A bar that acquires while another slot is held takes the shared width** (`TOOL-aPairedSlots-3`):
the held count is read once, right after the acquire, and the constant `TS_SHARE_RULE` decides —
`half` divides the width by the held count, `full` leaves it. The rule is the two-bar A/B's
(`TOOL-aPairedSlots-9`), which sets it. `GATE_JOBS` is the operator's width and is never divided. The
bar prints `gate profile: width <w> at dispatch — <k> of <n> bar slots held (<rule>)`, and the
summary file and header record that width; a bar that acquires alone prints nothing and keeps its
profile's width, and is not narrowed later when a neighbour arrives. The memory pause needs no
counterpart: it reads a host-wide source, so two bars already pause on one reading.

**A doc-only bar never queues** (`TOOL-aPairedSlots-4`). A run whose docs mode resolved — a
`GATE_DOCS_BASE` naming a commit, with `GATE_FULL` unset — takes no ticket and claims no slot: it
writes its beacon to `gate-docs-beacon/<run id>` beside the slots, exports its nonce so its legs'
runners nest, runs the ticker, prints `gate queue: docs-only — admitted on the docs key, not queued`,
and records `queued_from` `docs`. Nothing caps how many run at once (owner, 2026-10-11). It waits
only for a bar in its own worktree, printing `gate queue: docs-only — this worktree's bar holds <key>
— … — waiting for it`, and never for another worktree's. The reap and the held count read the slots
only, so a doc-only bar never narrows or is named by a non-doc bar, and delays one only in its own
worktree. A doc-only run first sweeps the docs beacons of dead, stalled or unfinished holders: one
with neither a pid nor a heartbeat is judged by its directory's age. `--hold` is never doc-only.

The beacon holds `heartbeat`, `pid`, `nonce`, and the holder's name: `repo` (its top level), `run`
(its run id) and `ttl`. A second run takes a time-sorted ticket and queues, announcing
`another bar holds this host — <repo> run <id> pid <pid> — queued at position N (waited Ns)`, with
`-` for a field an older beacon lacks; the runner prints `gate queue: waited <n>s` on exactly
one line, always, zero when uncontended, so a wrapper can tell waiting from working. The next line is
`gate queue: acquired <iso-utc> from <state>`, the instant the bar stopped waiting, and the run
record's header carries the same pair as `acquired` and `acquired_from`, so a bar killed later can
still be told apart from one that never acquired.

That line is not durable, and the status file beside it is deleted the moment the wait ends, so the
wait also reaches the RUN RECORD as the paired keys `queued` and `queued_from`, and the summary
file as its own line. `queued_from` reads `held` (queued, then acquired), `nested` (ran inside the
bar that holds the host, below), `expired` (burned the bounded wait and ran unqueued), `unticketed`
(could not write a ticket and ran unqueued at once), `docs` (a doc-only bar on the docs key, above),
`off` (the turnstile was disabled) or
`unresolved` (neither the host dir nor the common dir resolved). `off` and `unresolved` record a
DASH rather than a zero, because a zero for a probe that never ran is a reassuring number about
nothing. `unresolved` is UNARMED and the runner's comment says why.

A holder exports its nonce as `GATE_TURNSTILE_HOLDER` to its legs. A runner that inherits a value
equal to the `nonce` of any live slot beacon is NESTED inside that bar: it takes no ticket, prints
`gate queue: nested under <run> — <repo> pid <pid>`, and runs. Without that, a suite's scratch-repo
bar, or a wrapper bar's inner runner, would queue behind the very bar whose leg started it. Nesting
trusts an inherited value any process on the host can read from the beacon, so it decides contention
and never a verdict; the pre-push hook classes both knobs INERT rather than scrubbing them, as it
does `GATE_TURNSTILE=0`. `run-selftests.sh` gives each pooled row its own `GATE_TURNSTILE_DIR`, so a
pool's suites do not serialize against each other.

`run-gates.sh --hold -- <command…>` is how a bar that is NOT this runner joins the queue: it takes
the turnstile exactly as a bar does (or nests, or runs unqueued when that is what a bar would do),
runs the command from the repository top level right after `gate queue: acquired`, with
`GATE_TURNSTILE_HOLDER` exported when it holds, releases, and exits with the command's status. It
writes no run record, ledger row or stamp. `--hold` with no `--` or no command exits 2.

A waiter also rewrites `gate-queue-heartbeat` under its OWN worktree's git dir, beside `gate-logs/`,
on every tick that does not acquire, holding `waited<TAB><seconds>`. It is for an out-of-process
liveness reader that dates a worktree by its newest write: the ticket, the beacon and the status file
move nothing while a bar waits, and a gate log lands only when a leg finishes, so without it a
healthy queued bar reads as silent and a resumer may kill it. Readers go by its mtime and never
parse it. Unlike the status file it is NEVER removed: a leftover ages out as an old gate log does,
and a removal at the acquire would drop the newest move just before the first leg lands.

A holder is reaped on either of two signals: a dead PID, or a heartbeat older than the HOLDER's TTL,
read from the beacon's `ttl` and falling back to the waiter's own when the beacon has none, since two
repositories may run different TTLs. The TTL is derived from the profile row's per-leg `timeout=`
when it sets one, else `GATE_TURNSTILE_TTL`, and a detached ticker refreshes the heartbeat at a sixth
of it. Release is nonce-guarded and folded into a trap widened to INT, TERM and HUP: a run whose
beacon was reaped can never delete its successor's.

It FAILS OPEN. The wait is bounded at a declared multiple of the TTL; on expiry the run says so
loudly, drops its ticket and proceeds unqueued. `GATE_TURNSTILE=0` disables it entirely. It never
contributes to the exit code — a turnstile that can wedge a bar is worse than two bars.

Every repair the runner makes on its own also appends one line to the health log under the git
common dir, which the orientation card counts (`TOOL-aGraftedHelix-8`): `beacon-reaped`,
`ticket-swept`, `scratch-swept`, `turnstile-expired`, `retry-passed` for a serial retry that passed,
and one `dispatch-paused` per bar the memory pause held; the line format is the header of the
`health_log_sh` block in `run-gates.sh`.

## The post-merge bar

`post-merge.sh <sha> [--remote <name>]` runs the full bar on a sha that has already LANDED, and
publishes the verdict where every node reads it (`TOOL-aFrugalTurnstile-6`, design D7). It is the
after-the-merge half of the scoped-then-full landing path: the push boundary may scope a landing,
and this script pays the one full bar afterwards, in place of the boundary's.

It makes a detached scratch worktree of `<sha>` at `<common-dir>/gate-pm.<pid>`, reads the bar that
`<sha>` declares (`GOV_GATE_CMD` in `.githooks/gate-env.sh` as committed there, never sourced, else
`bash <kit>/run-gates.sh`) and runs it with `GATE_FULL=1` through this kit's own
`run-gates.sh --hold`, so it queues on the host turnstile like any other bar. Only three keys of that
file apply: `GOV_GATE_CMD`, `GATE_SELFTESTS` and `GOV_PYTHON`, and a line naming `GOV_GATE_CMD` in
any other shape, such as `export GOV_GATE_CMD=…`, is a refusal. Every knob `PM_SCRUB` in
`post-merge.sh` lists is dropped and named on one `post-merge: not honoured from the environment:`
line: the caller's `GIT_DIR` family, interpreter knobs, arm seams, the reuse modes, `GATE_RUN_ID`,
`GATE_TURNSTILE_HOLDER`, and every knob the pre-push hook scrubs or clears for a bar, which the gov
suite's scrub parity arm holds it to (TOOL-dWitnessedBar-60). The remote is the lander's
ladder (`GOV_REMOTE`, which `--remote` sets), and the sha must be an ancestor of that remote's
default branch as this clone last fetched it.

| exit | means |
|---|---|
| 0 | GREEN, and its publication completed |
| 1 | RED, or any verdict whose publication failed |
| 2 | REFUSED: a bad argument, an unlanded or unknown sha, no remote or a ladder refusal, a bar the tree at `<sha>` does not track, or a scratch worktree whose HEAD moved under the bar; nothing is published |

**The ref is `refs/gov/bar-red` on the remote.** A RED pushes `<sha>` there when the ref is absent,
or advances it when it names an ancestor of `<sha>`; any other ref is kept, so a red never moves it
backwards. A GREEN deletes it when it names `<sha>` or an ancestor; any other ref is kept, so a green
that does not descend from the red never clears it. Every push is `--force-with-lease` on the sha
the one bounded `ls-remote` observed, by remote name, from the scratch worktree, and the porcelain
line decides: a ref that moved in between is a lost race and a failed publication, never an
overwrite. A ref object missing locally counts as not an ancestor, which keeps the ref.

**Two records, under the git common dir.** `gate-post-merge` holds the last verdict for a reader with
no network: `sha`, `verdict` (`GREEN`, `RED` or `REFUSED`), `run_id`, `published` (`pushed`,
`cleared`, `kept`, `none` or `failed`), `why`, `remote` (the name, never a URL) and `stamped`. The
landed tree's verdict is the runner's own per-tree record, written from the scratch worktree into the
same common dir (see "The verdict per tree"). When the bar was the runner, its run record is copied to `gate-run/<run id>/` before
the worktree goes, so a red's leg output survives, and an exit 0 counts green only when that record
reads `verdict GREEN`.

**Remote CI** can run the same script on the landed sha instead of a local node, with credentials
that may push a `refs/gov/` ref; which one runs it is the adopter's declaration.

## `--print-profile` — the resolved profile, for a second reader

`run-gates.sh --print-profile` prints what this run WOULD use and exits before the turnstile: no
beacon, no leg, no run record. One TAB-separated `key value` line each, and a reader takes the keys
it knows:

| key | value |
|---|---|
| `name` · `width` · `timeout` | the selected row, the effective width and its per-leg timeout |
| `wall` | the whole-run wall in seconds, `GATE_WALL` over the row's own; 0 is no wall |
| `queue` | the turnstile's bounded wait in seconds, the declared multiple of the TTL, derived before the verb exits |
| `slots` | how many bars the host turnstile admits at once: the row's `slots` knob, 1 where it declares none, `GATE_TURNSTILE_SLOTS` over it. The profile line carries `, slots <n>` only above 1 |
| `ceiling_max` | the largest positive leg `ceiling` in the resolved manifest, or `-` when no leg declares one; ABSENT when the manifest does not parse |
| `ceilings` · `line` | whether per-leg ceilings are live here, and the profile line a bar prints |
| `mempause` | the memory pause's effective threshold, `GATE_MEMPAUSE` over the row's own; 0 is off. A host that gives no reading shows as `mempause INERT` on `line` |
| `spawnpause` · `width_from` | the spawn pause's ratio, 0 for off; and where `width` came from: `row`, `calibrated` or `GATE_JOBS` |

The unattended kit's driver reads `wall`, `queue` and `ceiling_max` to size the backstop of its
own bar (`TOOL-dDerivedDocket-27`): the wall is armed only after the queue, so the longest a
healthy bar takes is the two together, and a wall below `ceiling_max` fires on a healthy bar that
dispatches that leg.

## The memory pause — `mempause=<pct>`

The width is chosen once, from RAM, at start; the `mempause` knob watches what the legs then do to
memory. Before every dispatch the runner reads used memory and HOLDS that dispatch while the reading
sits above the threshold and a leg is still running. Every shipped row declares one, and the table
argues its figure; a row that omits it, or `GATE_MEMPAUSE=0`, is off. `GATE_MEMPAUSE=<pct>` overrides
the row alone, any other override prints one `run-gates: NOTE` and leaves the pause off, and a table
value above 100 refuses.

**A hold always ends**, so the knob costs speed and never a leg. Nothing polls: each decision happens
when a leg completes, and a hold is released when the reading falls to the threshold (`fell`), when
no leg is left running (`drained`), when the reading vanishes (`unread`), at the first completion
after the block's `MEMPAUSE_HOLD` seconds, which `GATE_MEMPAUSE_HOLD` overrides (`bound`), or by the
wall (`wall`). Under pressure that never falls the pool drains toward width 1 and keeps moving; the
serial retry is never held.

**The reading** is `/proc/meminfo`'s `MemTotal` against `MemAvailable`, or `MemFree` where the file
has none, which on MSYS is Windows' own available figure; and the cgroup's usage over its limit under
`GATE_CGROUP_ROOT`. The higher wins, read with shell builtins, so a decision spawns nothing.
`GATE_MEMINFO=<path>` replaces the file. A host with neither, macOS among them, reads INERT: one
`run-gates: NOTE` at start, `mempause INERT` on the profile line.

**What it records.** Each episode is one row of the run record's `pauses` file, `<started-s> ·
<ended-s> · <held-s> · <peak-pct> · <threshold> · <ended-by>`, TAB-separated; the verdict file gains
`paused` and `paused_s`, the header `mempause`, and every bar prints one line after its pool drains:
`memory: pause off`, `memory: no reading on this host, …`, `memory: no pause  (peak <p>% used, …)` or
`memory: <k> pause(s), <s>s held  (…; fell <a>, bound <b>, drained <c>, unread <d>, wall <e>)`. Its
peak varies with the host, so a reader comparing two bars' whole output filters it by name. A
seventh field, `<held-by>`, names the reading that held the episode: `memory`, `spawn` or
`memory+spawn` (next section). The `memory:` line and `paused` count what memory held.

## The spawn calibration and the spawn pause — `--calibrate-width`, `spawnpause=<n>`

The cost that binds a bar on a loaded Windows host is process creation, and a width past the point
where more concurrent spawns stop raising the spawn rate only dilates every leg. Two levers, both
TOOL-aSparedSpawn-2:

**`run-gates.sh --calibrate-width`** times K concurrent loops of the spawn `GATE_SPAWN_CMD` names
(`true` by default) for K in 1, 2, 4, 6 and 8, prints `rates`, `theta`, `pick` and `cache` as TAB
key/value lines, and writes `<git-common-dir>/gate-host-calibration`: `<pick> TAB <K=rate,…> TAB
<iso-utc> TAB <boot-epoch>`. The pick is the smallest K whose rate is within the runner's
`CALIBRATE_THETA` percent of the best. It exits before the turnstile and runs no leg; on a loaded host
it takes minutes. `GATE_CALIBRATION_RATES=<r1>,…,<r5>` replaces the timed loops with given rates.

**Every bar reads that cache** and never calibrates. A cache that is well formed, under seven days
old and written in this boot narrows the row's width to the pick, never widens it; `GATE_JOBS`
outranks both. Otherwise the row stands and the profile line says why: `width 8 uncalibrated:
absent`, `malformed`, `stale` or `another boot`. The header records `width_from`.

**`spawnpause=<n>`** holds the next dispatch while one spawn costs over `<n>` times this clone's
`gate-spawn-floor` and a leg runs, on the memory pause's episodes and every one of its release
rules. The census sampler times three spawns a tick for the reading; `GATE_SPAWN_NOW=<path>` replaces
it. With no floor recorded the knob is INERT: one `run-gates: NOTE` and a `spawn: no spawn floor
recorded, …` line. A run with the knob on prints a `spawn:` line after `memory:`; a run with it off
prints nothing new. Every shipped row declares 0 until the width A/B sets each row's value.
`derive-ceilings.py` sets aside, as `paused`, any reading whose leg ran while one of its own run's
episodes was open. `run-selftests.sh --pooled` carries the same block, byte-identical and
parity-graded, holds its next suite the same way, and prints the same line; it keeps no `pauses` row.

## The runner's own spawns — a ceiling per leg, and no clock

A fork costs a large fraction of a second on a loaded Windows host, so the bookkeeping a worker pays
around each leg is held to a count rather than left to a timing (TOOL-aSparedSpawn-4). The worker reads
its clock from `EPOCHREALTIME`, the leg's output with `mapfile`, and its log name with a parameter
expansion; it runs `redact` only on output that holds `://` and then `@`, and sets `umask 077` once,
after the leg exits, in place of two `chmod 600`. Every leg's input key is computed once before
dispatch, the bar asks `git rev-parse` once for its git dir, common dir and HEAD, and the
process-monitor kit dir is resolved inside the legs-parse python, so its
`run-gates: process-monitor:` line now prints after the turnstile lines rather than before them.

**The `SPAWNS` arm of `run-gates.runlog.test.sh`** holds that cost. It traces a one-leg and a two-leg
bar at width 1 with a `PS4` that carries `${BASHPID}`, counts FORKS as the pids that trace a command of
their own and EXECS as the command words that are no builtin, keyword or runner function, and reads
the per-leg figure as the difference. It counts a specimen with known forks first and refuses when
the counter disagrees, so a trace that cannot move reads as a refusal, never as zero. The ceiling is
the `SPAWN_CEILING` constant in that file, pinned with its date and node. The arm reds on growth,
printing the figure, the ceiling and the `file:line` sites the extra events came from, and reds as
STALE when the ceiling sits more than max(3, 5 %) above the figure.

**To move it:** lower the constant in the commit that saves a spawn, to the figure the arm printed.
Raise it only with a reason line beside the constant naming the spawn that is worth its cost.
`RGRL_ARMS=SPAWNS bash run-gates.runlog.test.sh` runs the arm alone.

## The held tier in WSL2 — `run-held-wsl.sh`

A spawn costs about a millisecond in WSL2 and tens to hundreds under MSYS, so the held self-test tier
can run its Linux-safe legs in WSL and only the declared Windows-only legs natively
(TOOL-aSparedSpawn-5). Dark: nothing invokes it but the owner, and no boundary reads its record.

**Setup, once per node.** Declare the node's host in `<git-common-dir>/gate-wsl.conf`, untracked and
never committed: `GATE_WSL_DISTRO=<distro>` and `GATE_WSL_MIRROR=<absolute ext4 path>`, the only two
keys it admits. Without it the run asks WSL's default distro and uses the shared default mirror,
`GATE_WSL_MIRROR_DEFAULT` in `.githooks/gate-env.sh`, and every run prints each value with its source.
Then `bash <prefix>/run-gates/run-held-wsl.sh --setup` clones the mirror from this clone, with remote
`win` as the fetch source and `origin` the hosted URL. The mirror's parent must be writable inside
WSL; the clone is the only write `--setup` makes.

**A run.** `bash <prefix>/run-gates/run-held-wsl.sh` refuses a dirty tree, pins `HEAD` and its
fingerprint, and runs two halves at once: the runner under `GATE_FULL=1 GATE_SELFTESTS=1` over the
Windows-only partition in a scratch `git clone --local`, and over the rest in a detached worktree of
the mirror after `git fetch win`, with `/mnt/*` off `PATH` and `TMPDIR` on ext4. Each partition row
runs its leg through the `--leg` shim, which unsets `GATE_LEGS` so no leg grades the partition as its
subject. `held_halves.py --combine` then refuses, exit 2, on a missing verdict, a fingerprint or
`HEAD` other than the pinned one, a moved tree, two manifest blobs, or a held leg not reported exactly
once on its declared host. Otherwise it exits by the runner's precedence, 1, then 4, then 3, then 0.

**Paired runs and `held-green`.** `--paired` runs every Linux-safe held leg on both hosts and appends
one row per host per leg to `<git-common-dir>/held-parity`; it writes no record. A plain run that
combines GREEN writes `<git-common-dir>/held-green` only while the last `GATE_WSL_PARITY_RUNS` paired
runs at this manifest blob agree on every compared leg, and otherwise prints `parity <n>/<k>` and
the legs that disagreed. `held-green` certifies the held tier at one sha and fingerprint across both
hosts, and nothing more: it is never `gate-full-green`, the push bar never reads it, and a WSL green
covers only the POSIX branch of a mixed suite, whose Windows arms the daily `held` CI job keeps.

## The gate profiler — `measure_legs.py`

`profile_bar.py` times the bar. `measure_legs.py` looks inside each leg (TOOL-dRedressedBar-18). It
runs every row of the manifest beside this kit, or of `--legs <path>`, with no guard, hold, reuse,
ceiling, retry or reap, and profiles each leg down to its processes. Guarded, kit-subject and
`selftests` legs are all included.

```bash
python <prefix>/run-gates/measure_legs.py --serial        # one leg at a time
python <prefix>/run-gates/measure_legs.py --concurrent    # next leg only at or under 80% CPU and 90% memory
python <prefix>/run-gates/measure_legs.py --selftest      # its arms, over fixtures/measure-legs/
```

**What each reading comes from.** Each leg's root starts suspended inside its own Windows Job
Object, so the kernel counts every process the leg starts, with its CPU, peak commit and I/O,
short-lived processes included. The process-monitor census is polled every `--census-every` seconds
(default 5) for per-process rows, and the job's count minus the census rows is recorded as `unseen`.
The runner's own `measure_spawn_cost` is sampled at each census tick. Host CPU and memory are read
every second with calls that spawn nothing. The runner's foreign-census predicate counts gate work
beside a leg, and the host turnstile's queue and slot beacons are read but never written.

**The environment.** Every `GATE_*` name, every `git rev-parse --local-env-vars` name and the push
hook's `unset GIT_…` names are scrubbed, the turnstile's two nesting names included. The scrubbed set
is printed and recorded, and values are stored only as digests. The legs get the runner's own
`TMPDIR` shape, its python and its bash. Python opens the scratch dir and the turnstile key only by
their `cygpath -m` spelling, and the envelope keeps both spellings.

**An alias launcher is substituted.** Every process a Microsoft Store App Execution Alias starts
leaves the job. So a launcher whose file carries the alias reparse tag runs, in every leg, as the
interpreter the alias reports as `sys.executable`, and the legs' `GOV_PYTHON` names that interpreter.
Each substitution prints `measure-legs: SUBSTITUTED <launcher> <alias> -> <resolved>` and is
recorded in the envelope's `substitutions`. A substituted reading lacks the alias's own process per
launch, so it is not exactly the bar's. Before the first leg, the interpreter the legs will run is
launched twice in test jobs, once with one child and once with none. Unless the two totals differ by
exactly 1, the run refuses. An alias that is not PYBIN also refuses.

**The record.** `<git-dir>/gate-profile/<run id>/` holds `envelope.json`, `host.tsv`, `census.tsv`,
`legs.tsv` and, per leg, a `.leg` row in the runner's eight-field grammar, a redacted `.log` and the
full `.json` profile. Nothing prunes it. Each raw capture is deleted once its redacted copy exists,
and one that cannot be deleted is named in `raw_kept`. A capture a leg's processes still hold at
its root's exit is retried at the run end, and an interrupt names every kept capture: a running
leg's, and one an ended leg's processes still hold, retried first, its reason opening
`interrupted; ` (TOOL-dRedressedBar-22). `legs.tsv` gains a row at each leg's end, so a run killed
outright keeps its rows, and is rewritten whole from the final records at the run end and at an
interrupt, so a retried capture's `log_bytes` reaches the table. A `.leg` row's eighth field is the
foreign count plus the foreign turnstile holders plus the leg's own queued bars. So
`derive-ceilings.py`'s `read_runs` sets a contended reading aside, and a serial reading with eighth
field `0` can be carried by `--observed`.

**What it does not check.** It grades no leg, because `ok` and `fail` are the exit status. It cannot
see work done for a leg by another process, or a bar on another turnstile key. A leg that sleeps, or
waits in the host queue, longer than `--stall-window` reads STALLED. No process that has run is ever
signalled: a leg that never ends keeps the run open. The one terminate is a leg's root still
suspended after a failed open, job assign, thread snapshot or resume, which has executed nothing and
records `fail` with its `launch_error`. It runs only on Windows and refuses anywhere else. Exit 0
every leg ended and every record was written · 1 a record write failed · 2 a refusal before the
first leg · 130 an interrupt.

## The scratch directory — owned, redirected and swept

Every heavy leg is hermetic because it builds its own `mktemp -d` scratch repo, so the scratch a bar
produces is proportional to its legs. The runner owns all of it:

- **Owned.** The run's scratch dir is a named `gate-work.*` directory under the AMBIENT `TMPDIR` —
  `/tmp` when that is unset or empty, where `mktemp -d` itself falls back — and it carries an `owner`
  record: the runner's pid, the resolved git common dir and the start epoch, one TAB-separated line.
- **Redirected.** Before the first leg dispatches the runner exports `TMPDIR` as that dir's `tmp/`,
  so every leg's `mktemp -d` and every Python `tempfile` lands inside it and goes when the bar exits.
  The spelling is the one `mktemp -d` returned and never a drive-letter rewrite.
- **Swept.** A bar killed by signal 9 runs no trap and leaves its whole scratch dir. Each later bar
  removes every `gate-work.*` whose owner names THIS repository's common dir and whose pid is dead,
  and says so on stderr: `run-gates: sweeping the scratch of a dead bar (pid <p>)`. A live pid only
  withholds the sweep. A dir with no readable owner — every bar's scratch from before this kit
  version, and another repository's — is never touched.

Once per bar, after the sweep, the runner prints `TMPDIR entries <n>`, the count of top-level entries
in the ambient `TMPDIR`, its own dir included, and writes the same figure to the run record header as
`tmpdir_entries`. Over an unchanged ambient two bars print the same figure, so a leak reads as growth.

**What the ambient cost before the runner owned it.** Measured on node `a`: 30733 entries, 58 legs,
and a full bar >10 min and still running, where the same bar finished on a fresh `TMPDIR`. Growth
there now comes only from bars that predate the owned scratch or run another repository. On a node
that still carries such a backlog, point `TMPDIR` at an empty dir before blaming the diff, and do not
delete the shared one.

The runner also re-executes itself through its own absolute path when it was started relatively, so
its argv, and the argv every leg subshell inherits by fork, names a path the process-monitor fence can
attribute. `exec` keeps the pid, and it happens before any output, lock or scratch exists.

## The run record

Every run writes a durable, machine-readable record under `<git-dir>/gate-run/<run-id>/`, and
`<git-dir>/gate-run/current` names the in-flight one so a concurrent reader — including a leg of the
run itself — can find it. The `header` is written before the first leg dispatches; one `<i>.leg` TSV
row and one redacted `<i>.out` copy land per leg; the `verdict` is written last, and ITS ABSENCE is
the crash signal. `GATE_RUN_KEEP` run directories are kept, swept after the verdict and never before
dispatch, so a crashed run's record survives the next few ordinary runs.

A `<i>.leg` row, and a `<i>.retry.leg` row beside it for a leg retried alone, holds eight TAB-separated
fields: `name · status · rc · seconds · started · ended · key · foreign`. `started` and `ended` are
epoch nanoseconds. `foreign` is the run's census of foreign gate work over that attempt: the largest
count of foreign process trees any sample saw from three census periods before the leg started until
it ended, `0` when every sample saw none, `unknown` when the census could not see. The samples land in
the record's `census` file, one line each: epoch second, count or `unknown`, and each tree's root as
`<pid>:<token>`, never its command line, which can carry a credential. The first sample is taken
before the first leg dispatches, then one every 60 s, which `GATE_CENSUS_EVERY` overrides with a
positive integer; the header records the period as `census_every`. A first sample reading `unknown`
prints one `run-gates: NOTE` line on stderr.

**What the census counts, and what it cannot see.** One `ps -ef` snapshot per sample: a row is gate
work when its whole line names a script some manifest leg runs, this runner or `run-selftests.sh`,
or carries a word ending `.test.sh` or `selftest.py`. This bar's own ancestors and descendants never
count, and a tree counts once, at its topmost matching process. It cannot see load shaped otherwise —
another repository's build, an on-access scanner, an agent's own CPU — nor, on Windows, any process
no MSYS shell spawned, so `0` means no foreign gate work and never a quiet host. Contention from this
bar's own neighbours is the serial retry's to answer. It over-counts in the safe direction: a bar
queued on the turnstile or a short command whose text names a gate script reads as foreign, which
only sets a reading aside. `ps` failing, a header naming no PID or PPID column, or a snapshot holding
no row for this runner reads `unknown`, never `0`. The bar's exit stops the sampler and the turnstile
ticker, so neither outlives it to be counted by the next bar.

A caller may pin the run id with `GATE_RUN_ID`, and the pre-push hook does, so its push line joins
this run's line exactly. The runner reads the pin and then REMOVES it from its environment before any
leg starts: left set, every leg would inherit it, and a leg that drives a nested runner, as this
kit's own suites do in scratch clones, would reuse one run directory for every nested bar. A pin
names ONE run.

**The verdict names its run and its cause** (TOOL-dWitnessedBar-25). The `verdict` file carries
`run_id`, the id its header names, and `cause`, the act that started the bar: `GATE_CAUSE` as its
caller exports it, read once and removed before any leg starts, as `GATE_RUN_ID` is, so a leg's nested
runner never names its caller's cause. The callers that pin a run id export one: the pre-push hook
`push:<pushed sha>`, `post-merge.sh` `post-merge:<landed sha>`, the unattended close `run:<slug>` and
`pass-legs.sh` `pass:<head sha>`. With none exported it reads `attended`, and a value outside
`[A-Za-z0-9._:@-]+` reads `attended` too, with one `run-gates: GATE_CAUSE refused` line on stderr.

**A failing leg's output tail is kept by its hash.** For each failed leg, in manifest order, the
runner cuts the last 60 lines of its redacted `<i>.out` copy (its retry's copy for a leg retried alone),
at most their last 8192 bytes, hashes them as git hashes a blob, writes them to
`<common-dir>/gate-tails/<hash>` where no file holds that hash (where one does, it sets that file's
modification time to now with `touch -c`), and adds `tail.<n>` `<hash> <leg name>` to the verdict, `<n>`
from 1. A failed leg with no copy keeps the empty tail. The directory is the COMMON dir's, so every
worktree of a clone writes one directory and a tail outlives the worktree that produced it. After the
run sweep, the tails directory keeps every hash a retained run of ANY worktree of the clone names, read
from `<common-dir>/gate-run/*/verdict` and `<common-dir>/worktrees/*/gate-run/*/verdict`, and every
tail modified less than `TAIL_GRACE_S` ago, seven days, so a tail a bar still running in another
worktree wrote before its verdict names it survives. A staging temp the writer leaves when a bar dies,
any name opening `tail.` (`tail.<n><n>.tmp`, `tail.XXXXXXXX`, either with `.cut`), is never kept as a
tail: it is removed once older than `TAIL_GRACE_S`, and a fresh one is kept (TOOL-dWitnessedBar-56 S13).
The sweep prints one `run-gates: tails swept` line with the counts it removed and kept. **What the sweep does not check:** a sweep that reads a tail's
time just before another worktree's bar freshens it can still remove it.

**A size warning a passing leg prints is shown, not buried** (TOOL-dWitnessedBar-29). A green leg's
output stays in the work dir, so a `TEMPLATE-SIZE WARN` or `BUDGET WARN` line inside one reached
nobody. Every size-warning emitter prints a MARKER on the line after its human warning, on the same
stream: `gate-warn<TAB><class><TAB><subject><TAB><detail>`, the class `size`, the subject the path the
warning measured (repo-relative inside the repository, else the warning's own subject, such as a
roster slot or a rule's line), the detail free text; the policy kit's `budgets.render_warn_marker`
builds it for the Python emitters. After the pool drains, the serial retry, the reuse sample and the
red legs' re-run, `scan_leg_warnings` runs ONE `grep -F` over the copies of the legs that passed —
`<i>.out` where `<i>.rc` reads `0`, `<i>.retry.out` where `<i>.retry.rc` does, a held leg a selection's
`run` row executed from its first attempt alone — and never over a failed, skipped, unrun held or
reused leg, a sample's second look or a red leg's re-run. Each marker line is one summary line before
the `----` line, in manifest order, on stdout and in `gate-last-summary.txt`:

```text
GATE warn  build-method size  (memory/guides/BUILD-METHOD.md: 28351 -> 29326 (+975) over high-water; grown by TOOL-dX-4)
gates GREEN — 141/141 legs passed (1 warned)
```

`grown by` is `routed_commits.py --newest-unit HEAD <subject>` from the memory-tree kit, reached
through `resolve_kit_dir`: the newest non-merge commit touching the subject whose unit a spec defines,
one python spawn per distinct subject and none on a run with no warning. It names the newest unit that
CHANGED the file, which may have shrunk it, not a proven grower. It reads `-` and names why — no
memory-tree kit, an attribution that failed, or no commit naming a specced unit (every subject that is
not a path). The verdict gains `warned<TAB><n>` and one `warn.<k><TAB><leg name><TAB><class><TAB><subject><TAB><unit>`
per warning, `<k>` from 1, after `tail.<n>`; the value keeps its inner TABs, so a reader splits it
itself. A warning never moves the verdict or the exit code, and `profile_bar.py` reads `GATE warn` as
an annotation. **What it does not check:** a warning printed with no marker, or a marker a leg prints
for any other reason.

**The keep verb commits them.** `python keep_tails.py --run <run id> --build <slug> --unit <unit id>`,
run in the repository, reads `trace.leg-output` through the policy kit's `policy.py get`, the catalogue
default where that reader cannot run. Under `tail-by-hash`, the default, it writes one `leg-tail`
record per `tail.<n>` of the run through the memory-tree record factory's `write_record`: fields `Leg`,
`Hash`, `Run`, `Sha` and `Cause`, then the tail in one fenced block, each span runlog's `scan_secrets`
finds replaced by its placeholder; a hash a tracked `leg-tail` record holds is skipped. Under
`node-local` it writes nothing and says `trace.leg-output is node-local`. Exit 0 when every tail is
written or skipped, 1 when one is not kept (its file gone, its bytes not hashing to its name, or a line
`write_record` refuses), 2 on a refusal before any write. The unattended close runs it on its bar's red
path, under the build's record anchor, and stages what it wrote with the `gates-run` fact.
`keep_tails.py --selftest` plants its own scratch repositories. **What it does not check:** that a tail
decodes or that its cut lands on a character boundary, or secret shapes runlog's table does not know.

**Every bar also leaves one line in the run log.** From its EXIT trap the runner appends one
`ev=once` line to `runlog/gates.log` under the git COMMON dir, in the runlog kit's grammar, so the
primary tree and every linked worktree of a clone write one file, and a run that ran the bar
seventeen times keeps seventeen verdicts rather than the last five records of one worktree. Every
value is read back from this record rather than recomputed: the run id, the header's worktree,
`head`, `started` and `full`, the verdict and its counts, `rc`, and the first twenty failing legs in
manifest order as `fail.1` onward, with `fail_more` counting the rest. A bar killed by INT, TERM or
HUP has no verdict file, so its line reads `verdict=NONE` with 130, 143 or 129, written once although
the signal runs the handler twice. A refusal between the trap and the header reads
`stage=pre-header` with the header's keys empty. An exit above the trap, `--print-profile` or a
refused profile table among them, writes nothing.

The line is evidence and never an input. A failed append prints one `run-gates: run log` line on
stderr and changes neither the exit code nor stdout, `GOV_RUNLOG=0` turns the line off, and writing
it costs no process beyond the one `mkdir` a clone's first bar pays for the journal directory.

`<git-dir>/gate-ledger.tsv` is the cross-run store: one row per leg, with the duration in field 2 —
which is what lets the runner read it as a dispatch hint and `profile_bar.py` read it as a
measurement, with no second copy of the same fact. A row is nine tab-separated fields: name,
seconds, status, input key, ended-at, run, full, manifest_blob, head. The reuse section above says
what reads the last four. A run carries forward every row it did not
measure, so a bar that reused or skipped every leg leaves the store as it found it.

Dispatch is longest-first, and a leg the ledger holds no row for is placed by a PRIOR: the largest
reading `ceiling-evidence.txt` beside the runner records for it, else its declared `ceiling` divided
by the median ceiling-to-reading ratio over the legs carrying both (re-derived every bar), else 0. So
a new worktree, which has no ledger, still starts its heaviest legs first. The order is advisory and
never moves a verdict; the run header's `dispatch` key records the one a bar used.

`<git-dir>/gate-full-green` is stamped only when the run failed nothing, skipped nothing, reused
nothing but lineage-qualified legs, the tree did not move, AND the tree was CLEAN when the run
started. CLEAN means
`git status --porcelain` empty, untracked files included. All five preconditions are what make the
file's name true, and an implementation that forgets one passes every arm written for the others.
The stamp also records `manifest`, the repo-relative path of the leg manifest the run read, and the
pre-push hook trusts it only for a runner bar reading that manifest.

## The verdict per tree — `gate-verdict/<tree hash>`

The record kind `verdict` (TOOL-dWitnessedBar-4) is what the latest bar said about one TREE, written
by this runner alone, GREEN or not. It is two files of one grammar, `<key>TAB<value>` lines read by
key, keys in the runlog grammar (an all-digit suffix is an index), so a key added later is ADDITIVE
and changes no reader:

| File | Written | Keys this runner writes |
|---|---|---|
| `<git-dir>/gate-run/<run id>/verdict` | every run, last | the run record's keys plus `tree`: the tree hash of `HEAD` when the run started clean, `-` otherwise; `run_id`; `cause`; `tail.<n>` per failing leg; and `warned` with one `warn.<k>` per size warning a passing leg printed (see "The run record") |
| `<common-dir>/gate-verdict/<tree hash>` and `<tree hash>.scoped` | every run that started clean and did not move | `tree`, `sha`, `verdict`, `kind` (`full` under `GATE_FULL`, `scoped` otherwise), `base` (the resolved `BASE` a scoped run diffed against, empty on a full one), `manifest`, `manifest_blob`, `fingerprint`, `selftests`, `reused`, `reused_cache` (the full-green stamp's two counts), `run_id`, `selection`, `selection.<n>` and `selection_ignored` (below), `cause`, `tail.<n>` per failing leg, `stamped`, `by` (`runner`) |

The files live in the git COMMON dir, so every worktree of a clone reads one directory, and are
written through a temp name and a rename. A full run writes the bare tree file and a scoped one the
`.scoped` file, so a scoped run never overwrites the full record its base rests on: two slots per
tree, and the last run of a tree in a slot wins, GREEN or RED. A run that started dirty or whose tree
moved writes none, and says so on one line; a written one prints its path.

**The selection it ran under** (TOOL-dWitnessedBar-41, -56). `selection` is the `git hash-object --stdin`
of the CANONICAL TEXT of the file `GATE_SELECTION` named: the rows the runner ACCEPTED and only those, in
file order, one trailing CR cut, each LF-terminated. A row is accepted when it has four or five TAB
fields, the first `held`, a source of `quarantine` or `level`, a fifth if present `hold` or `run`, and a
leg the manifest carries, the field rule `verdict_flow.py`'s `read_selection` applies. Every other row is
printed, left out of the text and the keys, and counted as `selection_ignored <n>`; a blank or `#` line
is no row. It reads `none` when the run read no `GATE_SELECTION` or the knob named no file, and
`selection_ignored` reads 0. One `selection.<n>` per accepted row, `<n>` from 1, holds
`<leg><TAB><source><TAB><note>`, and `<TAB><mode>` where the row has a fifth field: the row with its
`held` field cut and its TABs kept, so a ` · ` inside a note round-trips. The hook rebuilds each row as
`held<TAB>` plus that value, hashes the text the same way, and runs `verdict_flow.py select --check
--selection` over it at R, at most once per hash per push: a record with no `selection` key, rows that do
not hash to it, or a row R does not derive is not adopted. A record written before the TAB form, its
values joined with ` · `, rebuilds to another hash and is refused once, so the first push of such a tree
runs its bar.

**Two more runs write none** (TOOL-dWitnessedBar-40), each saying why on one line. A run in docs mode
(`GATE_DOCS_BASE` resolved) ran fewer legs than a scoped bar from the same base, which the record
cannot say: `run-gates: no gate-verdict written — docs mode`. A scoped run whose base is an inherited
green rests on a base no full record names: `run-gates: no gate-verdict written — scoped on an
inherited green, as the run record header's base_from row reads`; that header row carries a third field,
`inherited`, beside its source (TOOL-dWitnessedBar-56 S10). The runner learns that from `GATE_BASE_FROM`, `inherited` or `full` (any other
value reads `full`), read once and removed before any leg starts, as `GATE_RUN_ID` is; the pre-push
hook exports it beside `GATE_BASE` in its inherited-green branch, and the unattended close on its
scoped bar where `--decide` named `-` as the full base.

**Readers.** `.githooks/pre-push` reads the pushed tree's two files as candidates, for this runner's
own bar only, and adopts one only when it reads `verdict GREEN` and passes the predicates a
`gate-full-green` stamp passes (ancestry, lag, fingerprint, manifest path and blob, self-tests, and a
non-zero `reused_cache` refused), and carries at least one of `reused` and `reused_cache`: a record
with neither cannot say whether its run reused a leg, so it is refused where a keyless runner stamp
is not, and the `not covered` line names the missing pair; and whose `selection` R derives, as above. A full record covers the push and no bar runs, and a scoped one
covers only a push scoping from its base. The loop kit's transition writer reads the full file at
`item.test.exit` and refuses the move into deploying unless it reads GREEN. Nothing writes it but the
runner: the hook, the unattended close and the post-merge verifier each run the runner, so none of
them writes a record of its own. A clone's older `gate-bar-green*` files are left on disk and read by
nothing.

**What it does not check:** which legs a scoped run skipped; `kind`, `base` and the run record under
`run_id` say what ran.

## Verdict backends — `[[verdict_backend]]`

TOOL-dWitnessedBar-6. The policy key `verdict` names the backend a landing's verdict comes from. A
backend is a `[[verdict_backend]]` row in a kit descriptor, `name`, `reader` (`<module>:<function>`
under that kit), `off_node` (a boolean) and `owner`, read across every `<prefix>/*/kit.toml` by
`read_backends` in `verdict_backends.py`. govkit's install does not read the table, as with `[[drive]]` and
`[[command]]`, and a name declared twice is refused naming both descriptors. This kit declares three:

| Row | Reader | `off_node` | Stands when |
|---|---|---|---|
| `local-hook` (the default) | `read_local_verdict` | false | the full `<common-dir>/gate-verdict/<tree hash>` above reads `verdict GREEN` and passes the hook's two record predicates, the reuse pair and the selection re-derived at the landed revision (TOOL-dWitnessedBar-56 S7, S8); the `.scoped` slot never counts |
| `peer-node` | `read_peer_verdict` | true | `refs/gov/verdict/<sha>`, fetched from the remote, is an annotated tag on the SHA whose `tree` is its tree, whose `node` is not this node's `GOV_NODE`, signed by the key `verdict.peer.signers` registers for that `node`, whose `verdict` is `GREEN`, and whose pinned files derive `verdict.remote.pin` under `dispatch-closure` (TOOL-dWitnessedBar-43) |
| `remote-ci` | `read_remote_verdict` in `remote_verdict.py` | true | the witness rule below holds; the row also declares its `workflow`, `job` and bar `step` |

**One read, five states.** `read_verdict(backend, sha, tree)` returns `Verdict(state, witness, why)`;
`python verdict_backends.py read [--backend <name>] --sha <sha>` prints `verdict: <backend> · <state>
· <sha8> · <why>` and exits 0 on `GREEN`, 1 otherwise, 2 on a refusal. `GREEN`, `RED`, `NONE`, `HELD`
and `DEAD PROBE`: only `GREEN` stands. With no `--backend` it reads `verdict` at the landed revision
through the policy kit's `policy.py get`, a reader's refusal passed on and never read as
`local-hook`; `check_backend` refuses a value no row declares, naming it and the declared names. Only
this kit with no policy kit beside it reads the catalogue default, saying so on one line.

**Is the row off-node.** `python verdict_backends.py off-node [--backend <name>]` reads `verdict` as
`read` does where no `--backend` is given, finds its row by `check_backend`, and prints
`verdict-backends: off-node · <name> · <true|false> · off-node backends: <names>`, the names every
declared row with `off_node = true`. It exits 0 when the row is off-node, 1 when it is not, 2 on a
refusal. The lander, passing the value it already read, and the pre-push hook, passing none, ask it
under `hooks.bypass = refused`, which refuses every landing while `verdict` names no off-node backend,
because a hook on the bypassing node cannot refuse its own bypass (TOOL-dWitnessedBar-2).

**The peer.** `python verdict_backends.py verify-peer [--remote <name>]`, run on a second node under
its `GOV_NODE`, lists `refs/gov/candidate/*` and `refs/gov/verdict/*` with one bounded `git ls-remote`,
and for each candidate with no verdict fetches it, runs this kit's `run-gates.sh` on it under
`GATE_FULL=1` in a detached worktree of the node's own clone, and pushes an annotated tag
`refs/gov/verdict/<sha>` whose message is the full slot's `verdict`, `tree` and `run_id` lines and a
`node` line, in the slot's `<key>TAB<value>` grammar. `refs/gov/bar-red` is the precedent. The tag is
SIGNED, `git -c gpg.format=ssh tag -s` under the operator's own `user.signingkey`, its local name
deleted once pushed; `verify-peer` refuses, exit 2, before any `ls-remote` where `user.signingkey`
reads empty (TOOL-dWitnessedBar-43).

**The peer's two checks** (TOOL-dWitnessedBar-43). SIGNER: `read_peer_verdict` reads
`verdict.peer.signers` at the landed revision, never the working tree or the candidate, writes its
members, one allowed-signers line `<node tag> <key type> <base64 key>` each with no options field, to a
temp file under the common git dir, removed after, and runs `git -c gpg.ssh.allowedSignersFile=<file>
verify-tag --raw`; the verdict stands only when that exits 0 and its `Good "git" signature for
<principal>` line, which git writes to standard error, names the tag's `node` line and not this node.
An unsigned tag, an unknown key, a bad signature (git's `Signature verification failed`, a tag whose
message changed after it was signed, TOOL-dWitnessedBar-56 S15) or another principal reads `NONE`; the
key unset reads `NONE`, `no signer table`; a verify that cannot run, `ssh-keygen` absent included, an
`ls-remote` or `fetch` that fails and a refused policy read are `DEAD PROBE`. The key is owner-only: the loop guard refuses
an agent's change to it off a live run's branch, as it does `verdict.remote.pin`. Each node's operator
registers the node's public key with the owner. SOURCE: `check_pin_source` in `remote_verdict.py`, the
one source rule `remote-ci` applies too, over the same three keys, so a candidate that rewrites the
leg manifest reads `HELD`. Under `verdict.remote.pin-scope = workflow` a peer read is `HELD` naming the
key outside `app-only`, because that scope pins only the remote workflow, which no peer runs: a peer
verdict stands only once the owner sets `dispatch-closure` and pins under it.

**The witness rule**, `remote_verdict.py`. KEY: a push run whose `head_sha` is the SHA, the SHA's tree
resolved in this clone. WRITER: the run's check suite app slug `github-actions`, its `path` the row's
`workflow`, its event `push`, and the row's `job`. LIVENESS: that job's `step` concluded `success`,
never `skipped`. SOURCE: the files `verdict.remote.pin-scope` names (`workflow`: the workflow;
`dispatch-closure`: also `run-gates.sh`, the leg manifest and `.githooks/gate-env.sh`) derive, at the
SHA, the id `verdict.remote.pin` holds: `git hash-object --stdin` over their sorted `<path> <blob id>`
lines, through `check_pin_source`. `verdict.remote.trust` = `pinned-workflow` or `owner-reviews-workflow-change` reads differing
files `HELD`; `app-only` skips the source and reads a pass `GREEN` with witness `claimed`. The three
keys are read at the landed revision; no pin reads `HELD`, `no pin`; a failed read is `DEAD PROBE`.
Every GET goes through `read_api`: https to `api.github.com` only, no redirect, no credential, 30 s,
4 MiB. `--responses <dir>` points it at canned files named by `derive_response_name`, an arm seam.
`python remote_verdict.py pin` prints the pinned lines and id at HEAD and writes nothing.

**The held reader** moved here too: `python remote_verdict.py held <anchor URL> <workflow file>`,
`read_held_runs`, prints what the unattended kit's retired `read_held_reds` printed, one TAB row per
`held <suite>` job and one liveness line, or one DEAD PROBE line; `write_held_asks` files the reds.

**Its readers.** `check_landing_verdict` in `push-main.sh` before each landing push: `local-hook` lands as
before; under another value only `GREEN` lands, a `peer-node` SHA not yet green published as
`refs/gov/candidate/<sha>` first. The unattended driver's gates-green term files a `remote-ci` `HELD`
read as one owner item. `verdict_backends.py --fixture --plant <case>` runs each plant in a scratch
directory, and `run-gates.gov.test.sh` runs them.

**What it does not check:** that a peer ran the bar its tag names, beyond the pinned files it ran it
from; that `GOV_NODE` is unique; that a registered key is still held only by its node; that the pinned
files are all the bar job executes.

## Every leg may declare a `ceiling`, and the runner holds it to it

**`"ceiling": <seconds>`, a positive integer, per leg row in the manifest.** A leg that outlives it
is KILLED, deferred and retried once alone, as the serial-retry section above states, and a leg that
outlives it on the retry too is reported `GATE FAIL <leg> (timed out after Ns, again on its serial
retry; …)` — never skipped, and green only when its retry passed. That is the one way a knob here may
change a verdict: it converts an unbounded hang into a RED naming its leg. Before it existed, one leg
that never returned wedged the whole bar and named nothing.

**A KILLED leg names the seconds it RAN and its ceiling separately.** `timeout` exits 124 when its
own TERM fires and 137 when a SIGKILL ends the leg — its `-k` escalation, an operator, an OOM killer
and a CI cancel all arrive as 137 and cannot be told apart. So that tail reads
`GATE FAIL <leg>  (killed after Ns, ceiling Ms)`: N is the elapsed value the runner measured, byte
for byte the same figure `gate-ledger.tsv` carries for that leg, and M is the bound it may never have
reached. Neither is passed off as the other, and the verb does not claim a timeout it cannot observe.
With NO bound in play — no ceiling declared, no profile timeout, or a host with no runnable
`timeout` — the tail is `(killed after Ns)` alone: the absence of the ceiling clause is the
information, and N is still the ledger's own figure.

**A leg that declares no ceiling runs UNBOUNDED, and is COUNTED rather than refused.** The runner
prints `N of M legs declare no ceiling and run unbounded this run` on stderr and carries on. It
cannot tell a leg somebody forgot from a leg you deliberately left alone, so it reports and leaves
the judgement to you. If you want the requirement enforced over YOUR corpus, assert it in a harness
of your own — gov does exactly that in `run-gates.gov.test.sh`, which is withheld from this payload
for the reason that file's header gives.

**A kit leg's ceiling arrives only where its descriptor declares one.** The deployer carries a kit leg's `ceiling` into your manifest at run-gates 1.2 or later,
and only for a leg whose kit descriptor declares one; a value you set by hand on that row is kept
and reported rather than overwritten, while a deleted one comes back on the next deployer run.

**Choosing a number.** `<git-dir>/gate-ledger.tsv` already carries one row per leg with its own
seconds, so the derivation gov used is `max(60, 3 × that leg's measured seconds)`. The factor is
headroom for the box, not for the code: the same workload has been measured at 10.7 s and 26 s
across one session on a machine with an on-access antivirus scanner, and a ceiling that reds on
someone else's scan is a ceiling that gets deleted. The 60 s floor is what gives a leg that
finishes in under five seconds a bound worth having.

**Raising one that fired needs a reading the bar cannot give you.** A leg killed at its ceiling
never completes, so the only thing its run record holds is the bound that stopped it, and
`derive-ceilings.py` builds evidence from completed runs — the mechanism cannot reach exactly the
legs whose bounds fire. Re-run the leg quiet, then hand the number in rather than editing a bound
from something nobody wrote down:

```
GOV_NODE=<tag> python derive-ceilings.py --write \
  --observed '<leg>=<seconds>' --how 'how you took the reading'
```

It refuses a reading with no stated conditions, one for a leg the manifest does not carry, one whose
node would have to be defaulted, and one that raises nothing. The row lands in the evidence file
carrying its source, so a number somebody measured by hand never reads as one the runner watched,
and `--check` names those legs apart from the rest.

**Evidence is keyed by leg AND node** (TOOL-dWitnessedBar-10). A row keeps its six fields, `<leg>`,
`<max seconds>`, `<readings>`, `<node>`, `<date>`, `<source>`, and one leg may carry one row per node.
Every `--write` needs `GOV_NODE`, and refuses naming it when it is unset rather than defaulting to
`a`, because a node-keyed row written under a defaulted tag overwrites that node's evidence. It
raises or holds only the writing node's rows and carries every other node's byte-identical, so two
nodes' writes touch different rows. `--check` grades each ceiling against the largest reading across
nodes and prints `ceiling-evidence: <k> of <n> legs evidenced on one node only`, a report and never a
failure. The runner's dispatch prior and `pass_legs.py`'s cost read take the same per-leg maximum.

**The whole-bar wall time is committed too.** `GOV_NODE=<tag> python profile_bar.py --record [--out
<log>]` distils the last record of `<git-dir>/gate-profile.jsonl` into the tracked
`bar-wall-evidence.txt`, one TAB-separated row per node: `<node>`, `<date>`, `<sha8>`, `<wall
seconds>`, `<legs run>`, `<width>`. It replaces that node's row with the latest reading, not a
maximum, because a wall time measures a bar and bounds nothing. It refuses, writing nothing, a last
record taken with `--scoped` (a guarded run is not the whole bar) and an unset `GOV_NODE`.

**Only a reading the census found free of foreign gate work argues a ceiling.** `derive-ceilings.py`
admits a run-record reading only when its `foreign` field reads `0`, and sets the rest aside under
one reason each, first match: a positive count is `contended`, and anything else, `unknown` or a
seven-field row written before the census existed, is `uncensused`. `--report` prints a
`# set aside:` line with the count per reason and an `aside` column per leg, and names a leg whose
every reading was set aside on its own line rather than as UNBACKED; `--write` names the same counts
on its summary line and, when everything was set aside, holds every evidence row rather than
reporting DEAD PROBE, which stays for a record holding no reading at all. The census never lowers a
ceiling: the evidence file stays monotone, and `--check` reads tracked files only.

**`--observed` is the one uncensused route, and it stays admitted.** A reading taken outside the
runner is admissible and uncensused, as TOOL-cMendedVintage-17 rules: it never passes through a run
record, so no census reaches it and nothing filters it, and its `--how` text is the only record of
the load it was taken under. Say in that text what else was running.

**On a host with no runnable `timeout -k`, every ceiling is INERT** and the runner says so on
stderr. Legs still run. A bound may cost you speed and may turn a hang into a verdict; it may never
turn a leg into a pass or a skip.

## The leg manifest is the kit dir's SIBLING, and it is GENERATED

Each leg is declared ONCE: a `[[gate_leg]]` row of its kit's descriptor when an adopter receives it,
else an `[[exempt_leg]]` row of the deployer's registry carrying its whole row beside its `why`. Where
gov's own run differs from what an adopter receives, gov's value sits under the row's
`[gate_leg.gov]` sub-table, key by key; an empty list there removes the key from gov's row.
`leg_factory.py --write` renders `<prefix>/gate-legs.json` from every declaration, `pass_leg` included
through `pass_legs.py`'s own rule; `--check` names each leg the file holds differently, and
`regen.py` runs it at stage 1; `--conform`, the `gate-leg conformance` leg, adds every field arm over
every declaration. Never hand-edit the manifest. Declare a new leg with
`python <prefix>/run-gates/leg_factory.py new <name> --kit <id> --argv <json> --subject <kit|repo>
--purpose <text> --enforces <tag>`, or `--exempt <why>` in place of `--kit` for a registry row; the
kinds register reaches the same verb as `python <prefix>/playbook/core.py new gate-leg <name> ...`
(TOOL-dWitnessedBar-11).

In a tree with no govkit, which is every adopter's, `leg_factory.py` still loads: `--write`, `--check`,
`--list` and `new` exit 2 naming the places they looked for govkit, and `--conform` grades every field
arm over the `[[gate_leg]]` rows of the tree's `*/kit.toml` descriptors, read through `regen.py`'s
reader. It prints `fresh: not graded here — no govkit` and `enforces: not graded here — no govkit`,
since the render and the registries those arms read are gov's; it does not read the registry's
`[[exempt_leg]]` rows or the flat entries' descriptors the playbook kit lands beside its engine
(TOOL-dWitnessedBar-45).

`<prefix>/gate-legs.json`, DERIVED from this kit's own location rather than spelled, so a one-segment
install resolves it at any prefix. `GATE_LEGS` still outranks the derivation, which is the seam both
harnesses drive so a nested run never re-enters the real bar.

Leg-row keys: `argv`, `ceiling`, `chunk`, `doc_reads`, `enforces`, `guard`, `name`, `pack`, `pass_leg`, `precommit`, `purpose`, `reads`, `scope_of`, `signature`, `stage`, `subject`, `tag`, `tests`.

Each is a key some row of the manifest carries. `tag` is the leg's `leg.<owner>.<name>` tag in the
leg namespace, beside its free-text `name`, which stays the key every file keyed by leg joins on;
the canary's one key set is `LEG_KEYS` in `run-gates.test.sh`. `tests` lists the features a leg
tests (`feature.<f>`) and `enforces` the principles and practices it enforces; both are edges from
the row's `tag`, read by the playbook kit's edge check (`edge_grammar.py --check`), declared once, on the
leg's one declaration, which renders the manifest row, and neither travels into an adopter's
manifest. The gov canary compares `tests` with the map dossiers' `gate-legs` claims in
both directions (TOOL-dWitnessedBar-22). `purpose` says what the leg is for: one line of 1 to 60
characters, no two legs sharing one: its shape and uniqueness are `leg_factory.py --conform`'s
`purpose` arm, and selfcheck 7h grades its presence until TOOL-dWitnessedBar-51 moves it; it travels into an
adopter's manifest from run-gates 1.52, `LEG_KEY_FLOORS["purpose"]` (TOOL-dWitnessedBar-19).
`precommit` is the argv the pre-commit hook runs for the leg, in the manifest's `{prefix}` grammar,
declared beside the row's `argv` in the same tokens and overridden under `[gate_leg.gov]` wherever
`argv` is; it travels into an adopter's manifest from run-gates 1.53, `LEG_KEY_FLOORS["precommit"]`
(TOOL-dWitnessedBar-10).
`level` is in `LEG_KEYS` from run-gates 1.54, `LEG_KEY_FLOORS["level"]`, and no row of gov's manifest
carries it, so it is not on the list above: a row carrying it is a product-test leg, its level one of
`unit`, `integration`, `e2e` or `performance`. See "The product-test contract" below
(TOOL-dWitnessedBar-9).

**The product-test contract — `tests.product`.** `product_tests.py check`, the leg `product-test
contract (tests.product)`, reads `tests.product` through the policy kit's `policy.py get`, or its
catalogue default with the reason where that reader refuses, and grades the manifest's rows carrying
`level` against it. The four levels are the ones the catalogue's `tests.landing-levels` row names.

| `tests.product` | the product-test rows the manifest may hold | `check` is red when |
|---|---|---|
| `none` | none | any row carries `level` |
| `declared` | the repository's own rows carrying `level`; no adapter row is rendered | a level is outside the four, or no row carries one and a runner's `detect` names one |
| `declared-with-runners` (the default) | those, plus one adapter row per level each detected runner declares | a level is outside the four, or a detected runner's row is missing from the manifest |

A runner adapter is a `[[test_runner]]` row of a kit descriptor, holding `runner`, a `detect` argv,
the `levels` it can run and an `argv` spelling `{level}`; the guardrails kit's pytest row is the
first. `leg_factory.py` runs each `detect` in the tree and, where one names a level, reads
`tests.product` and adds one row per detected level after the declarations: name `<runner> <level>
tests`, tag `leg.<runner>.<level>`, `pack` `product-tests` and its `level`. A tree no runner detects
spends no policy read. `check` prints the value and where it was read, each product-test row with its
level, and the count; a tree with no product test and no runner prints `0 product-test legs declared`
and exits 0, the zero printed so it is never read as coverage. Gov holds no product suite, so gov's
row runs `check --fixture`, one planted repository per value, printing `case <name>: red|green` and
exiting 1 where a case reads otherwise than it is planted to. WHAT IT DOES NOT CHECK: that a leg
carrying a level runs tests of that level, or that an adopter whose legs the deployer emitted, rather
than the factory rendered, holds its adapter rows.

**The commit-time list is derived, not typed in the hook.** `run-gates.sh --precommit` hands over to
`precommit.py` before any bar machinery exists, as `--regen` does. It reads the manifest beside this
kit (or `--legs <path>`), lists the staged set once, and for every row carrying `precommit`, in
manifest order, prints `pre-commit: <name> not tripped` when the row's `guard` names no staged path,
or runs the argv and prints `pre-commit: <name> ok` or `pre-commit: <name> FAILED (rc <n>)`. A row
with no `guard` runs at every commit. A row whose argv names a script absent from the tree prints the
hook's announced skip and is not a failure. It exits 1 when any run failed; `--list` prints each row's
name, argv and trigger and runs nothing. The pre-commit hook calls it once, after its memory hygiene
block, which stays hand-named because its commit-time form is a grade, a check-9 render and a regrade
that no one argv states; the hygiene leg declares no `precommit`. WHAT IT DOES NOT CHECK: a trigger
narrower than the bar's `guard` — the commit-time trigger IS the guard, so an unguarded leg costs its
run at every commit.

The manifest does NOT travel. A target's leg list is emitted from the selected kits' `[[gate_leg]]`
blocks; seeding an adopter with gov's leg names is the class
`memory/gotchas/pin-copied-from-another-corpus.md` exists for, and the adopter starts with an empty
list instead.

## The pass legs — `"pass_leg": true`, derived and never typed

**`"pass_leg": true` on a leg's row declares it one of the legs a unit pass runs.** An undeclared
row carries no such key, as an unguarded row carries no `guard`. No hand writes the field:
`pass_legs.py` derives it, and a field typed by hand is a finding of its `--check`. The field is
data. This section says which rows carry it, and nothing here runs a leg.

**The rule** ranks every leg by recorded reds per evidenced second and fills a budget:

1. **Cost.** A leg's cost is its maximum in `ceiling-evidence.txt`.
2. **Excluded.** `check_pass_eligible` gives the first reason that fits, in this order:

   | reason | the leg |
   |---|---|
   | `selftest` | has `chunk` `selftests` |
   | `kit-subject` | has `subject` `kit`, the other half of what the runner holds |
   | `e2e` | has `chunk` `e2e` |
   | `unattended-gate` | has an `argv` word ending `check-unattended.sh`, so a renamed row stays excluded |
   | `no-red` | has no row in the pass-leg evidence |
   | `unevidenced` | has no row in the ceiling evidence, so its cost is unknown |
   | `over-cap` | has a cost, or a last seconds, above `PASS_LEG_CAP_SECONDS` |

3. **Score.** `reds / max(cost, 1.0)`. The one-second floor keeps a sub-second leg from outranking
   every other by division.
4. **Order.** Score descending, then cost ascending, then name.
5. **Fill.** Walk the order with a running sum of cost. A leg is `selected` while the sum with its
   cost stays at or under `PASS_BUDGET_SECONDS`, else it is `over-budget`, and the walk goes on, so
   a cheaper leg further down still enters.

`PASS_BUDGET_SECONDS` and `PASS_LEG_CAP_SECONDS` are constants of `pass_legs.py` and their values
are read there. The last-seconds half of `over-cap` exists because ceiling evidence can be stale
low. Every recorded red counts, an inherited one included: the run log does not say whose a red
was. An `unevidenced` leg enters once a routine `derive-ceilings.py --write` gives it a row.

**The evidence** is `pass-leg-evidence.txt`, tracked, generated and never hand-edited: a
`# window` line naming the bars read, the first and last bar's start, the node and the date, then
one `<leg> TAB <reds> TAB <last seconds, or ->` row per manifest leg with at least one red. Reds are
counted from the bar lines of `<git-common-dir>/runlog/gates.log`, whose `fail.<n>` fields name
each bar's failing legs. A line whose `run` value opens `pass-` is a pass-leg run, which is no bar,
and it is skipped: only a declared leg can red there. The gate ledger keeps one row per leg and no history, so it gives the last
seconds alone, read from `<git-dir>` and `<git-common-dir>` with the later row winning. The file is
gov's own and is withheld from the payload, as the ceiling evidence is.

**`scope_of` names the leg a row is a cheap form of.** A manifest row carrying `"scope_of": "<leg>"`
grades part of what that leg grades, and `--write` credits it the named leg's reds beside its own.
The evidence row of a scoped leg therefore holds its own reds plus its parent's, and every credit
reads the counts as logged, so a form of a form gains one parent's and no more. A `scope_of` naming
no manifest row is a Refusal: exit 2, before the run log is read or a byte is written.

| verb | what it does |
|---|---|
| `GOV_NODE=<tag> python pass_legs.py --write` | distils this node's run log and ledgers into the evidence file, replacing every row, then applies. Exit 2 with `GOV_NODE` unset. A run log that is absent or holds no bar line is a `DEAD PROBE`: exit 1, nothing written |
| `python pass_legs.py --apply` | writes the field onto each selected row and removes it from every other, from tracked files alone. It edits the manifest as text, one line after a row's `"name"` line, and refuses with exit 2 and nothing written unless the result parses to the old rows with only `pass_leg` differing |
| `python pass_legs.py --check` | exit 0 printing `pass-legs: <n> declared, <sum>s of <budget>s` when the manifest's text, line endings apart, is what `--apply` would write; exit 1 naming each leg that carries a field the rule does not give it and each selected leg that lacks one |
| `python pass_legs.py --report` | one line per leg: verdict, reds, cost, score and name, under the window line |
| `python pass_legs.py --budget` | the budget gate below: exit 0 when the declared legs are clean, a warning included; exit 1 on any finding; exit 2 when it cannot grade, on a manifest that does not parse, a limit under the budget or a cap over the budget |
| `python pass_legs.py --figures` | prints `<budget> TAB <limit> TAB <cap>` and nothing else, three integers, so a shell reader holds no copy of them |

**With no evidence file the rule selects nothing.** `--apply` writes nothing over a manifest with no
field, `--check` is green and prints `pass-legs: not derived, no evidence file`, and a field typed
by hand is still a finding. That is an adopter's state on arrival, until it runs `--write` on a
node that has run a bar. A fresh install may hold no manifest beside the kit at all: `--apply` and
`--check` then exit 0 printing `pass-legs: not derived, no leg manifest at <path>`, so the staged
row below reads fresh and the bar's preflight passes. A manifest `GATE_LEGS` names and that is
absent still refuses with exit 2.

**The field is re-applied at every landing.** This kit's descriptor declares `--apply` and
`--check` as a staged `[[regenerate]]` row at stage 2, so `--regen` and the lander write the field
and every bar's preflight proves it fresh, as "Generated outputs" above states for every staged
row. A ceiling-evidence refresh that moves the selection is cured by the landing or by one
`--regen`, and is never a leg's red. A deployer update rebuilds the rows it owns from their
descriptors and drops the field from them, and the same staged row puts it back. Both halves of the
row run behind the leg shim, `bash run-held-wsl.sh --leg python pass_legs.py …`, which unsets
`GATE_LEGS`: the check grades the manifest beside this kit under any runner, a pass-leg run's
included, whose runner is started with `GATE_LEGS` naming its filtered list.

**The budget gate re-reads the list the rule leaves.** `--check` asks whether the field is the
rule's own output. `--budget` asks a different question of the same tracked files: whether the
declared rows, however the field got there, fit the owner's limits. A field typed by hand, a cost
row that rose after the last apply and a fault in the rule all land here. It reads the field and
never `pass.fast-legs`. `check_pass_budget` gives each declared leg the first finding that fits,
then sums the list:

| finding | the declared leg, or the list |
|---|---|
| excluded class | `check_pass_eligible` answers `selftest`, `e2e` or `unattended-gate` for it |
| held | `check_pass_eligible` answers `kit-subject` for it, so the pass-leg runner would hold it and run nothing |
| no cost row | has no row in `ceiling-evidence.txt` |
| over the cap | has a cost row above `PASS_LEG_CAP_SECONDS`, or `check_pass_eligible` answers `over-cap` on its last seconds |
| over the limit | the declared legs' cost rows sum above `PASS_LIMIT_SECONDS` |

The two cost findings ask the cost row directly, because the predicate answers `no-red` ahead of
both. `PASS_LIMIT_SECONDS` is a constant of `pass_legs.py` beside the budget and the cap. A sum
above `PASS_BUDGET_SECONDS` and at or under the limit is a `pass-budget: WARN` line and no finding.
Each finding is a `PASS-BUDGET FAILED` line on stderr naming its leg. A clean run ends on
`pass-budget: <n> leg(s) declared, <sum>s against a <budget>s budget and a <limit>s limit, cap
<cap>s`, or on `pass-budget: 0 leg(s) declared` when no row carries the field.

**The leg `leg ceilings clear their evidenced maximum` carries it.** `derive-ceilings.py --check`
calls `check_pass_budget` after its own arm, whether or not a ceiling failed, and exits with the
higher of the two. Where `pass_legs.py` is not beside it, it prints `pass-budget: not graded` and
its own verdict stands. That leg is gov's own, so an adopter runs `--budget` by hand once it holds
cost rows.

What the gate does not check: a cost row is the worst reading on record on one node, and a leg
never re-measured can sit under its true cost. The sum is the legs run one after another, and a leg
its guard skips counts in full.

## The pass-leg runner — `pass-legs.sh --base <rev>`

`bash <prefix>/run-gates/pass-legs.sh --base <rev>` runs the declared pass legs over one pass's
diff (TOOL-aNimbleMend-5). It holds no leg command and no verdict logic: it filters the manifest to
the rows whose `pass_leg` is true, in manifest order, writes them to `<git-dir>/gate-pass-legs.json`
and starts `run-gates.sh` once with that file as `GATE_LEGS`. Each row is copied with its `argv`
behind the held tier's leg shim, `bash <prefix>/run-gates/run-held-wsl.sh --leg`, and nothing else
of the row moves (TOOL-aNimbleMend-13). `--base` is required and must name a
commit; without one it exits 2 and starts nothing, because the runner reads an unresolvable base as
empty and runs every leg.

| What it sets for the runner | Why |
|---|---|
| `GATE_BASE=<the resolved base>` | each leg's own `guard` decides against the pass's diff |
| `GATE_FULL` and `GATE_SELFTESTS` empty | a flag the calling session exported cannot widen the run |
| `GATE_RUN_ID=pass-<UTC stamp>-<pid>` | the run's directory under `gate-run/` is known, so its record can be read back |
| `GATE_TURNSTILE=0` | the run starts beside a queued bar: one that waits out another worktree's bar cannot be held to a budget |

The exit code is the runner's, unchanged. The runner's output is passed through and never captured.
Before it starts anything the adapter asks the policy key `pass.fast-legs` once, under the policy
kit's ask contract: `off`, a refused read and a value outside the pair each end the run with exit 0,
no runner and no file, and where no policy kit resolves it runs under one NOTE line on stderr. When
no row carries the field it starts no runner, prints `pass-legs: 0 legs declared, nothing ran` and
exits 0.

**The record is `<git-dir>/gate-pass-legs.txt`**, `key TAB value` per line, replaced on every run
that got as far as reading the manifest:

| Key | Value |
|---|---|
| `run_id` | the pinned id, naming the directory under `gate-run/`; `-` when no runner started |
| `base`, `head` | the resolved base and `HEAD` when the run started, full shas |
| `started` | UTC, to the second |
| `exit` | the runner's exit code, or `-` when no runner started |
| `verdict` | the runner's own verdict, `EMPTY` when no row carries the field, `NO-VERDICT` when the runner wrote none |
| `declared` | how many rows carried the field |
| `wall_s`, `budget_s`, `limit_s` | whole seconds around the runner call, and the two declared figures |
| `over` | `none`, `tolerance` or `limit` |
| `held` | the runner's count of held legs |
| `leg` | one line per declared leg: name, status, seconds |

A leg's status is the runner's own, `ok`, `fail` or `timeout`, its retry's where it was retried. A
declared leg with no row reads `not-run` with `-` for seconds: its guard skipped it, or the runner
held it. `head` is what tells a record earned at another commit from one earned at this one.

**Two findings, and neither moves the exit code.** Each is one stdout line and a key of the record.

| Condition | Line |
|---|---|
| `wall_s` above `PASS_LIMIT_SECONDS` | `pass-legs: FINDING overrun: the run took <wall>s, over the <limit>s limit (budget <budget>s)` |
| `wall_s` above `PASS_BUDGET_SECONDS`, at or under the limit | `pass-legs: NOTE the run took <wall>s, inside the tolerance above the <budget>s budget`, which is no finding |
| the runner's `held` above 0 | `pass-legs: FINDING held: <n> declared leg(s) did not run, held as a self-test or a kit-subject leg` |

Both figures are read from `pass_legs.py` at each run. The wall time is the shell's clock around
the runner call, so it includes the runner's own start, which no cost row holds.

**What a pass-leg run costs the bar's records**, each because it runs through the bar runner:

- A red run replaces `gate-last-failure.txt`, exactly as the next red bar would.
- A green run with no skipped leg and a clean tree replaces the `gate-full-green` stamp with one
  naming the filtered manifest. The push hook trusts a stamp only when its manifest is the kit's
  own, so the next push runs its bar in full, and the next full bar re-earns the stamp.
- The run adds its legs' rows to the gate ledger and leaves every other row standing.
- Every leg starts through the shim with `GATE_LEGS` unset, so a declared leg that reads it as its
  subject grades the manifest beside its kit, as under the full bar, whatever the caller exported.
  Each leg costs one more shell start, and a ledger row the run writes is keyed on the wrapped
  command. `GATE_BASE` is inherited as the adapter set it.

What it does not check: whether the declared list is the rule's own output or inside its budget,
which are `pass_legs.py --check` and `--budget`, and whether a skipped leg's guard is too narrow. It
scrubs no runner knob beyond the two flags above.

## The gov-only harness

`run-gates.gov.test.sh` is withheld from the payload by a `project-owned` rule in `kit.toml`, exactly
as the memory-recall kit withholds its recall-floor program and fixture, and for the same stated
reason: arms keyed on THIS repo's corpus are meaningless in another tree. It is a leg on gov's own
bar and carries an `[[exempt_leg]]` row in the registry — deliberately not a `[[gate_leg]]` here,
because a descriptor row naming a leg a target's manifest cannot carry is what reds the deployer's
selfcheck.

It REFUSES with exit 2, rather than passing, when the manifest it is pointed at is not gov's. A
gov-only harness that quietly succeeds against a foreign corpus is the split failing open.

## Whose red is it — `GATE_ATTRIBUTE=<R>`

A red bar names WHICH legs failed and never WHOSE failure each one is. With `GATE_ATTRIBUTE=<R>` set
the runner re-runs each red leg ALONE at `R` — `R`'s own manifest row, from a detached scratch
worktree of `R` under the git common dir, under `R`'s ceiling for that row — and prints one line per
red leg in manifest order, then a summary:

```
GATE attr  <leg>  INHERITED · offenders <n> · at <R8> · passes
GATE attr  <leg>  MIXED · inherited <i> · own <o> · at <R8> · blocks
GATE attr  <leg>  OWN · <reason> · blocks
GATE attr  <leg>  CONTENDED · timed out after <n>s; not re-run at R · blocks
GATE attr  <leg>  DEAD PROBE · <reason> · blocks
attributed <N> of <M> red legs against <R8>[ · DEAD PROBE <k>] · verdict.blocks <value>[, none handed] · <b> blocking
```

The same rows land in the run record as `attribution`, TAB-separated: leg, verdict, inherited, own,
the full `R` sha, age, owner sha8, owner id, blocks, reason — the reason LAST, the three age columns
`-` where no age was asked, and `blocks` the word "Which red blocks" below derives. **It changes no
exit code**: a bar that was red is red. What to DO with a verdict is the landing readers'.

The classifier, first match wins. **OWN, forced** when the diff between `R` and the working tree
touches this runner, `gate-fingerprint.sh`, `lib-attribute.sh`, `lib-verdict.sh` or the pre-push hook `core.hooksPath`
names — a run that edited its grader cannot vouch for any verdict. **CONTENDED** when the leg's own
ceiling fired (124 under a positive bound, or 137 under one whose seconds reached it); it is not
re-run. **OWN** when `R` has no row for the leg, its argv differs from `R`'s, the diff touches its
COMPARATOR — every tracked file under the directory of a tracked file in its argv or in `R`'s
`signature`, plus each tracked root-level file those files' bytes name — or it is green at `R`.
**DEAD PROBE** when `R` cannot answer, including an `R` run the whole-run wall cuts, or when the
leg's own output at L normalises to nothing. Otherwise **INHERITED** or **MIXED**, by the rule below.

`R` is meant to be the LANDING base. `.githooks/pre-push` exports the remote sha it reads for the
default branch; an `R` that is a merge-base or a local ref buys an attribution only as fresh as it.

### The optional `signature` key

A manifest row may declare `"signature": [argv…]`: a command, run in the tree being graded, that
prints ONE stable key per offender and nothing else — no line number, no count, no header, no cut.
Where `R`'s row declares one, both ends are graded with `R`'s: INHERITED when the set of keys at L is
non-empty and inside the set at `R`, else MIXED. Where it declares none, the leg's normalised output
must be byte-identical to read INHERITED. **L's own `signature` is never run**, so a run cannot choose
its own grader. The normaliser strips each root in its three spellings, `mktemp`-shaped names,
durations and trailing whitespace, and nothing else: an unknown variation reads MIXED, the safe way.

WHAT IT DOES NOT CHECK: the comparator reads each grader's own directory and the root files its
bytes name, so a module imported from ANOTHER directory, or a conf named only at run time, is outside
it; an edit there that hides the run's own offender can read INHERITED. An untracked file is
invisible to the diff. A repository at a very deep path on Windows may fail to make the worktree,
which reads every red DEAD PROBE rather than guessing.

### The age of an INHERITED red — `GATE_INHERITED_RED_MAX_AGE=<n>`

With the bound set, each INHERITED leg runs once more at `R~n`, `R`'s n-th first-parent ancestor,
from `R`'s row in the same scratch worktree. Red there carrying every offender L carries appends
`aged at R~<n>`; otherwise a bisection of the window names the landing that introduced the red,
`age <k> · owner <sha8> <id>`. A probe that cannot answer appends `age unproven`. The age decides
no landing (ruling `TOOL-dUnstuckLanding-22`): the inherited-green stamp is written whenever every
red leg's row reads `pass` under a handed `GATE_VERDICT_BLOCKS`, at any age and with or without a
bound, its `max_age` empty when none was handed; the unattended driver escalates an `aged` leg's
ask to BLOCKER. Without a `signature` the offenders are the output's
non-blank lines: red with every line of L's is red there, and red with ANY other output cannot be
answered, because text cannot tell a fixed offender from a moved count line. Such a leg is aged
only while its text holds still or shrinks toward L's; one whose red prints a changing count
declares a `signature` to be aged across it.

### Which red blocks — `GATE_VERDICT_BLOCKS=<value>`

The policy key `verdict.blocks` decides which red of a red bar blocks its landing (TOOL-dWitnessedBar-3).
The pre-push hook and the unattended driver each read it at `R` through the policy kit's `policy.py get
--rev`, and hand it to the bar as `GATE_VERDICT_BLOCKS`; the runner reads it once and removes it, as it
does `GATE_ATTRIBUTE`. Each attributed red's class is joined to `block` or `pass` by `lib-verdict.sh`:

| class | `own-only` | `own-mixed-contended` | `every-red` |
|---|---|---|---|
| OWN | block | block | block |
| MIXED | pass | block | block |
| CONTENDED | pass | block | block |
| INHERITED | pass | pass | block |
| DEAD PROBE | block | block | block |
| no row, or an unknown class | block | block | block |

An absent value reads `every-red`, said on the summary; an unknown one reads `every-red` too. A red bar
lands only when every attribution row reads `pass`: the hook's `check_inherited_verdict` and the
driver's `read_gates_record` read that field and never re-decide it, and `lib-verdict.sh` is in KF3's
list, so a diff that edits the table reads every red OWN.

`python verdict_flow.py route --run <run dir>` joins each red to one route by its class and writes the
routing record `<run dir>/routing` (leg, class, blocks, route, judgment, next): a red whose same-tree
re-run reads `ok` routes `flakes`, ahead of every other row; a passing red routes
`ask`; a blocking OWN or MIXED red `attribute`, the tester's; CONTENDED `quiet-rerun`; DEAD PROBE, or a
red the attribution omits, `probe-repair`; INHERITED `fix-unit`. The unattended driver's `gates-green`
runs it on every red bar it reads. `verdict_flow.py judge --run <run dir> --leg <name> --judgment
<word>` records the tester's `code-miss` or `spec-wrong` on an `attribute` row and fills `next` by
`verdict.red-route`; it reads the judgments through the loop kit's `loop_lib.py items --tag`, the verb
`TOOL-dWitnessedBar-100` asks for, and exits 2 naming it until it lands.

THE QUIET-HOST RE-RUN (TOOL-dWitnessedBar-30). `route` stamps a `quiet-rerun` row `routed <epoch>`, the
stamp of the newest sibling run record naming the leg when its row there still reads `rerun waiting`,
else now, so a contended red's wait spans the bars each pass runs. `python verdict_flow.py quiet-rerun
--run <run dir>` takes each such row not yet re-run: when `profile_bar.py#check_quiet` reads `true`, no
foreign bar visible on the host by PowerShell or, where none exists, `ps -eo pid=,args=`, both under the
liveness assertion that this process's own command line is read, it runs the leg once, alone, through
this runner under a one-row manifest (`GATE_LEGS`), `GATE_FULL=1` and `GATE_SELFTESTS=1`, attributed
against the R its attribution row names (`GATE_ATTRIBUTE`), its run record `<run id>-quiet-<n>` beside
the bar's. Green writes `rerun ok`, the red cleared as contention; red re-attributes the row and routes
it by its new class, `rerun red <class>`. Otherwise it prints `awaiting quiet host  <leg>  since
<routed at>`, and once the wait exceeds `flow.wait-ceiling` hours `owner  <leg>  contended, no quiet host
within <h> h`, writing `rerun owner`. A state other than `waiting` is final and never re-run. The
unattended driver runs it after `route` on every red bar it reads and files each `owner` line as a HIGH
`contended red, no quiet host: leg <leg>` ask through `write_leg_ask`, once per leg while it is OPEN.

`python verdict_flow.py flakes --run <run dir> --build <slug> --unit <id>` is `test.flakes`
(TOOL-dWitnessedBar-8), and acts as `verdict.flakes` reads: under `retry-only` it writes nothing; under
`record` and `quarantine` it writes one `flake` record through the memory-tree factory's
`write_record`, `Run`, `Ended`, `Sha`, `Tree` and `Legs`, then one TAB row per executed leg, `<leg> ·
<first rc> · <re-run rc or ->`. A flake is a row whose first rc is not 0 and whose re-run rc is, as the
factory's `derive_flaked` says, and the rows are read through its `read_flake_body`. It then runs the
drift kit's gate-health measurement in the repository's top, bounded at 60 seconds, `drift_report.py
--gate-health --selection <the run's selection record, or an empty temporary file> --write --build <slug>
--unit <id> --with <the record it wrote>`, and prints every line it prints, so a `drift-report: wrote
<path>` line's gate-health record is staged beside the flake record;
no drift kit, a non-zero exit or the bound firing prints one `flakes  gate-health · <why>` line, and
`flakes` still exits 0. The holds it prints read the threshold in force before that record. Under
`quarantine` it prints `hold  <leg>  <flakes>/<window>  <record ids>` for each leg whose flakes in its
last `<window>` rows, newest `Ended` first across every tracked flake record and after its last
release, reach `verdict.flakes.entry`, and that no OPEN held-flaky-leg ask names: a declared
`<count>/<window>`, or under `measured` the newest gate-health record's `Measured`, 2/10 until the
factory registers that kind and one is tracked. A release is the committer date of the commit adding
the CLOSED row of the leg's held-flaky-leg ask. The unattended driver's `gates-green` runs it beside
`route` on every red bar, under the build's record anchor, stages the record, and files each `hold`
line as a MED `held flaky leg: leg <leg> flaked <n> in its last <window> verdicts` ask through its
`write_leg_ask`; that OPEN ask is the hold the selection's `quarantine` row reads. `flakes --check`
reds an OPEN held-flaky-leg ask whose leg had fewer flakes, in its window at the ask's filing date,
than the threshold in force then.

MIGRATION NOTE: `verdict.blocks` replaces the gate-file key `INHERITED_RED=park|land`, which the hook,
the driver and this runner (as `GATE_INHERITED_RED`) no longer read. The govkit upgrade step
`govkit/inherited-red-to-verdict-blocks` reads both files the key lived in, `.githooks/gate-env.sh`,
the hook's, and the file `GATE_POLICY_FILE` names in `.unattended.conf`, the driver's, each where
present. It writes a declared `park` as `every-red` and `land` as `own-mixed-contended` into the
target's `.governance/policy.toml`, any other non-blank value as `every-red`, as both readers read it,
and takes the assignments out; where the two files differ, the stricter value, `every-red`, wins. Where
the policy file already sets `verdict.blocks` to another value the step refuses, printing `conflict ·
verdict.blocks · policy <value> · gate <value>`, exits 1 and writes nothing. An undeclared key leaves
the catalogue default `own-only`. The age bound `INHERITED_RED_MAX_AGE` stays. The whole step is in
`help/upgrade-steps.md`, "Where `INHERITED_RED`'s value lives".

## The report tail contract

Every tailed line is `<verb>  <leg name>  <tail>` — TWO spaces before the parenthesised tail, on
every verb. A reader splits the remainder on a double space and gets the bare leg name back; a
single space made that split return a truncated name for any leg whose name contains a space, which
is most of them, and the deployer reads a target's verdicts exactly that way. The gov-only canary
forbids a double space INSIDE a leg name, which is what keeps the split unambiguous rather than
merely usually right.
