# run-gates kit

`gov:kit run-gates@1.0` — the marker a deployer greps; paired with `KIT_RUN_GATES_VERSION` in
`run-gates.sh` and asserted EQUAL by `tools/check-kit-versions.sh`. Presence of a marker is not
agreement between a marker and a constant, and this repo has twice had a half-bumped pair pass a
presence-only check.

## What this is

The merge-bar runner, its two harnesses, and the adopter that keeps a target's verdict-reading
declaration honest. The runner is a thin iterator over a leg manifest: it holds no leg command of
its own, and the canary asserts that.

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
| `gate-fingerprint.sh` | "what tree is this, exactly", in two forms. With no argument it digests the tree object at `HEAD` plus the sorted porcelain lines plus the blob hashes of every dirty-or-untracked file; with a `<rev>` argument it digests that rev's tree and supplies the other two components EMPTY. On a CLEAN tree the two forms agree, which is what lets a hook ask whether a recorded green still describes the commit it names. Empty output on any failure — a caller that cannot measure must see nothing rather than a partial digest |
| `profile_bar.py` | the profiling verb: runs the bar, records it as a RUN, and names the regime — floor-bound or packing-bound — so the next fix is chosen from a measurement |
| `profile_bar.test.sh` | the profiler's own arms |
| `run-gates.test.sh` | the SHIPPED canary — every assertion here is true in any tree |
| `run-gates.gov.test.sh` | the GOV-ONLY arms, withheld from the payload; see below |
| `run-gates.evidence.test.sh` | the durability arm: a red leg's output survives on disk |
| `run-gates.turnstile.test.sh` | the turnstile arms: peak occupancy, reaping, FIFO order, release on every signal |
| `adopt-run-gates.sh` | `--check` asserts a target's `[gate_runner]` declaration still matches this runner's output strings |
| `adopt-run-gates.test.sh` | the adopter e2e, gated on EFFECTS rather than exit codes |
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
one line, always, zero when uncontended, so a wrapper can tell waiting from working.

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

## The run record

Every run writes a durable, machine-readable record under `<git-dir>/gate-run/<run-id>/`, and
`<git-dir>/gate-run/current` names the in-flight one so a concurrent reader — including a leg of the
run itself — can find it. The `header` is written before the first leg dispatches; one `<i>.leg` TSV
row and one redacted `<i>.out` copy land per leg; the `verdict` is written last, and ITS ABSENCE is
the crash signal. `GATE_RUN_KEEP` run directories are kept, swept after the verdict and never before
dispatch, so a crashed run's record survives the next few ordinary runs.

`<git-dir>/gate-ledger.tsv` is the cross-run store: one row per leg, with the duration in field 2 —
which is what lets the runner read it as a dispatch hint and `profile_bar.py` read it as a
measurement, with no second copy of the same fact.

`<git-dir>/gate-full-green` is stamped only when the run failed nothing, skipped nothing, reused
nothing, the tree did not move, AND the tree was CLEAN when the run started. CLEAN means
`git status --porcelain` empty, untracked files included. All five preconditions are what make the
file's name true, and an implementation that forgets one passes every arm written for the others.

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

## The report tail contract

Every tailed line is `<verb>  <leg name>  <tail>` — TWO spaces before the parenthesised tail, on
every verb. A reader splits the remainder on a double space and gets the bare leg name back; a
single space made that split return a truncated name for any leg whose name contains a space, which
is most of them, and the deployer reads a target's verdicts exactly that way. The gov-only canary
forbids a double space INSIDE a leg name, which is what keeps the split unambiguous rather than
merely usually right.
