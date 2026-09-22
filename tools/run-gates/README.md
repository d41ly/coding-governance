# run-gates kit

`gov:kit run-gates@1.9` — the marker a deployer greps; paired with `KIT_RUN_GATES_VERSION` in
`run-gates.sh` and asserted EQUAL by `tools/check-kit-versions.sh`. Presence of a marker is not
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
| 2 | REFUSED: not run from a repository, no usable python, a manifest or profile table it cannot read, a scratch dir or run record it cannot create, a manifest whose every leg is held, a run that reported no leg line (an empty manifest), or a green whose verdict file was not written | a `run-gates:` line, or `gates REFUSED — …` |
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
GATE retry  <leg>  (timed out after <n>s beside <k> neighbours; one serial retry after the pool drains)
```

where `<k>` counts the legs that were running when it timed out. Its chunk closes `pending`, never
`green`. After the pool drains, and inside the run's wall, each such leg runs once more ALONE under its
own ceiling and prints its final line: `GATE ok    <leg>  (retried after timeout)`, which counts green,
or `GATE FAIL  <leg>  (timed out after <n>s, again on its serial retry; …)`, whose note says whether
HOST was read and why not. One `---- retry: <green|RED|HOST|killed>  (<n> retried, <m> failed)` line
follows. Any other 137 — a self-kill, an OOM kill, an operator's or a CI cancel, under a bound or with
none — is an ordinary failure and is never retried; nor is an assertion failure.

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

The records keep both attempts: the first attempt's `<i>.leg` row reads `timeout` and a
`<i>.retry.leg` row sits beside it, the verdict file gains `retried <n>`, and the ledger row takes the
retry's seconds with the status `retried`, which reuse never accepts. The drift report sums `retried`
across the run records as `legs_retried_after_timeout`.

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
says so itself: held legs get their own verb, are subtracted from the total, and are named in the
summary, `gates GREEN — 43/43 legs passed (42 held: kit self-tests, GATE_SELFTESTS=1 runs them)`.

A leg that declares no `subject` defaults to `repo` and runs, so nothing you already had changes
behaviour by arriving here. A whole manifest of held legs is REFUSED rather than reported green,
because a bar that executed nothing is not a bar that passed.

The state reaches two other readers: the deployer, which reads a held leg as `held` rather than as a
leg that vanished, and the `gate-full-green` stamp, which records whether the run covered them so a
push boundary cannot mistake a partial bar for a whole one.

## Why it became a kit

It was a registry EXEMPTION, with two stated reasons that were both exact. It sourced `tools/lib/`,
which is gov-internal and never travels; and with that path absent, `bash` sourcing a missing file
under `set -u` continues, `resolve_python` is undefined, and the guard on the next line fires — the
runner exited 2 having run ZERO legs. So `govkit apply` wired legs into a runner the target was
assumed to already own, and a target that owned none received a merge bar that could not start.

the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` cut that dependency by inlining the canonical resolver into every shipped
file that had one, byte-identically, under the markers `tools/lib/resolve-python.test.sh` greps for
— so each copy enrols itself in the parity gate rather than needing a table row.

## The pieces

| file | what it is |
|---|---|
| `run-gates.sh` | the runner. Legs run through a bounded pool, at the width `gate-profiles.txt` declares for the detected hardware; `GATE_JOBS` overrides the width alone |
| `gate-profiles.txt` | the DECLARED knob table: rows of name, minimum cores, minimum RAM MB, knobs, most-capable-first with a zero-threshold catch-all last. `GATE_PROFILE=<row>` selects one by name and skips detection; `GATE_PROFILES=<path>` reads a different table, and an absent path falls back to the built-in formula — which is the rollback. `GATE_CORES` / `GATE_RAM_MB` replace the detected readings and bypass detection, and `GATE_CGROUP_ROOT` relocates the cgroup files the RAM chain reads |
| `lib-attribute.sh` | the attribution's two shared halves, SOURCED and never run: the normaliser (`write_normaliser`) and the detached scratch worktree at a base (`add_scratch_worktree` / `remove_scratch_worktree`). The runner sources it only when `GATE_ATTRIBUTE` is set and a leg is red, and `run-selftests.sh` only under `--attribute`, so a copy of either runner without it still runs every other mode |
| `gate-fingerprint.sh` | "what tree is this, exactly", in two forms. With no argument it digests the tree object at `HEAD` plus the sorted porcelain lines plus the blob hashes of every dirty-or-untracked file; with a `<rev>` argument it digests that rev's tree and supplies the other two components EMPTY. On a CLEAN tree the two forms agree, which is what lets a hook ask whether a recorded green still describes the commit it names. Empty output on any failure — a caller that cannot measure must see nothing rather than a partial digest |
| `profile_bar.py` | the profiling verb: runs the bar, records it as a RUN, and names the regime — floor-bound or packing-bound — so the next fix is chosen from a measurement |
| `profile_bar.test.sh` | the profiler's own arms |
| `run-gates.test.sh` | the SHIPPED canary — every assertion here is true in any tree |
| `run-gates.gov.test.sh` | the GOV-ONLY arms, withheld from the payload; see below |
| `run-gates.evidence.test.sh` | the durability arm: a red leg's output survives on disk |
| `run-gates.turnstile.test.sh` | the turnstile arms: peak occupancy, reaping, FIFO order, release on every signal |
| `run-gates.runlog.test.sh` | the run-log arms: one line per bar on every exit path after the trap and on every caught signal, withheld from the payload |
| `adopt-run-gates.sh` | `--check` asserts a target's `[gate_runner]` declaration still matches this runner's output strings |
| `adopt-run-gates.test.sh` | the adopter e2e, gated on EFFECTS rather than exit codes |
| `check-receipt.py` | the leg `receipt sync (installed files match the receipt)`: every engine row of `.governance/install.json` still on disk and still hashing to its recorded sha256. The INTEGRITY half only — it reads no `source`, `commit` or `gov_oid`, because those resolve against a gov checkout an adopter does not have, and it grades no `seed`, `merged`, `attributes` or `forked` row. A tree with no receipt is an announced `SKIP`, and four built-in fixture arms run on every invocation so the leg has a verdict there too |
| `kit.toml` | this entry, declared as data |

## Reuse, and the baseline a guard diffs against

`GATE_REUSE=1` skips a leg whose inputs are byte-identical to a recorded green: not declared
`impure`, its ledger row says `ok`, and the row's input key equals the one computed this run. Any
missing term means execute — every failure mode is "did more work", never "checked less". It is
OPT-IN because an advisory input may cause less work only on a run that is not authoritative, and
`.githooks/pre-push` never sets it. A run that reused anything cannot stamp `gate-full-green`.

The baseline a guard diffs against is the MERGE-BASE with the default branch, so a branch is graded
on what it changed rather than on everything that landed while it was open — used only where the
merge-base is a proper ancestor of `HEAD`, with the origin tip standing otherwise. `GATE_BASE`
outranks both, and an unresolvable baseline runs every leg.

## The turnstile — one bar per repository

A run claims a beacon under the git COMMON dir before it dispatches, so every worktree of one
repository shares one beacon and two repositories never contend. A second run takes a time-sorted
ticket and queues, announcing its position; the runner prints `gate queue: waited <n>s` on exactly
one line, always, zero when uncontended, so a wrapper can tell waiting from working. The next line is
`gate queue: acquired <iso-utc> from <state>`, the instant the bar stopped waiting, and the run
record's header carries the same pair as `acquired` and `acquired_from`, so a bar killed later can
still be told apart from one that never acquired.

That line is not durable, and the status file beside it is deleted the moment the wait ends, so the
wait also reaches the RUN RECORD as the paired keys `queued` and `queued_from`, and the summary
file as its own line. `queued_from` is a closed four-word vocabulary: `held` (queued, then
acquired), `expired` (burned the bounded wait and ran unqueued), `off` (the turnstile was disabled)
and `unresolved` (the common dir did not resolve). The last two record a DASH rather than a zero,
because a zero for a probe that never ran is a reassuring number about nothing. `unresolved` is
UNARMED and the suite header says why.

A holder is reaped on either of two signals: a dead PID, or a heartbeat older than the TTL. The TTL
is DERIVED from the profile row's per-leg `timeout=` when it sets one, because the heartbeat
refreshes when a leg COMPLETES — so "can the holder still be holding" and "has a leg finished
lately" are the same question. Release is nonce-guarded and folded into a trap widened to INT, TERM
and HUP: a run whose beacon was reaped can never delete its successor's.

It FAILS OPEN. The wait is bounded at a declared multiple of the TTL; on expiry the run says so
loudly, drops its ticket and proceeds unqueued. `GATE_TURNSTILE=0` disables it entirely. It never
contributes to the exit code — a turnstile that can wedge a bar is worse than two bars.

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

A caller may pin the run id with `GATE_RUN_ID`, and the pre-push hook does, so its push line joins
this run's line exactly. The runner reads the pin and then REMOVES it from its environment before any
leg starts: left set, every leg would inherit it, and a leg that drives a nested runner, as this
kit's own suites do in scratch clones, would reuse one run directory for every nested bar. A pin
names ONE run.

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
measurement, with no second copy of the same fact.

`<git-dir>/gate-full-green` is stamped only when the run failed nothing, skipped nothing, reused
nothing, the tree did not move, AND the tree was CLEAN when the run started. CLEAN means
`git status --porcelain` empty, untracked files included. All five preconditions are what make the
file's name true, and an implementation that forgets one passes every arm written for the others.

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

**On a host with no runnable `timeout -k`, every ceiling is INERT** and the runner says so on
stderr. Legs still run. A bound may cost you speed and may turn a hang into a verdict; it may never
turn a leg into a pass or a skip.

## The leg manifest is the kit dir's SIBLING

`<prefix>/gate-legs.json`, DERIVED from this kit's own location rather than spelled, so a one-segment
install resolves it at any prefix. `GATE_LEGS` still outranks the derivation, which is the seam both
harnesses drive so a nested run never re-enters the real bar.

The manifest does NOT travel. A target's leg list is emitted from the selected kits' `[[gate_leg]]`
blocks; seeding an adopter with gov's leg names is the class
`memory/gotchas/pin-copied-from-another-corpus.md` exists for, and the adopter starts with an empty
list instead.

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
GATE attr  <leg>  INHERITED · offenders <n> · at <R8>
GATE attr  <leg>  MIXED · inherited <i> · own <o> · at <R8>
GATE attr  <leg>  OWN · <reason>
GATE attr  <leg>  CONTENDED · timed out after <n>s; not re-run at R
GATE attr  <leg>  DEAD PROBE · <reason>
attributed <N> of <M> red legs against <R8>[ · DEAD PROBE <k>]
```

The same rows land in the run record as `attribution`, TAB-separated: leg, verdict, inherited, own,
the full `R` sha, reason — the reason LAST. **It changes no exit code**: a bar that was red is red.
What to DO with a verdict is a policy, and the policy is not this runner's.

The classifier, first match wins. **OWN, forced** when the diff between `R` and the working tree
touches this runner, `gate-fingerprint.sh`, `lib-attribute.sh` or the pre-push hook `core.hooksPath`
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

## The report tail contract

Every tailed line is `<verb>  <leg name>  <tail>` — TWO spaces before the parenthesised tail, on
every verb. A reader splits the remainder on a double space and gets the bare leg name back; a
single space made that split return a truncated name for any leg whose name contains a space, which
is most of them, and the deployer reads a target's verdicts exactly that way. The gov-only canary
forbids a double space INSIDE a leg name, which is what keeps the split unambiguous rather than
merely usually right.
