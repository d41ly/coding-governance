# Closing review — the cumulative diff, faaea5f5..HEAD

**Serves:** diff-review TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8

Node `a`, 2026-09-07. The M8 closing pass over everything this build lands, scoped to the cumulative
diff at the pinned BASE `faaea5f5` and reviewed once at the integration boundary. Bound to this run
by commit `a94b64a0`, which carries the fixes below.

## Verdict: CLEAN WITH FIXES

Seven findings were shipped behaviour and are FIXED in this pass, each with its failing case observed
where one could be staged. Twenty-seven are promoted: none changes what the code does today, and the
largest group is arms that cannot fail — a green light over something ungraded, which is this repo's
own most-filed class and the right first target for a follow-up. Nothing found here blocks the
landing; the bar is 47/47 green with the fixes in.

## Shape and cost

Five primed finder lenses over the diff — gate-efficacy, shell-correctness, measurement-integrity,
claim-vs-code, declaration-completeness — then skeptics batched five ways and prompted to REFUTE.
Ten agents, 1.84M subagent tokens, 23 minutes wall. The repo's own recurring-bug-class checklist for
this diff (`python tools/memory-tree/gotchas.py --for-diff`) selected 28 classes and was handed to
every lens as its checklist.

**34 findings, 34 CONFIRMED, 0 REFUTED.** A precision of 1.0 is a number to distrust rather than to
celebrate — the charter's own guidance treats the skeptic stage as the thing that should be killing
findings, and a stage that kills none has either met unusually good finders or done its job badly.
Two things argue for the first reading here and they are recorded so a later reader can weigh them:
every finding traced to a file and a line, and several quote the diff contradicting ITSELF — two
comments thirty lines apart disagreeing about whether a branch exits early, a header claiming a
report the code cannot emit. The counter-argument is left standing rather than explained away: no
sampling was done to check the skeptics, and the next Tier-2 run in this repo should seed one known
-false finding to measure them.

## What was FIXED in this pass

Seven, all shipped behaviour, all in `a94b64a0` and `60719fbe`.

- **`run-gates.sh` — a wall breach left NO verdict.** The breach block `exit 1`s above the run
  record's verdict writer, so the most deliberate outcome the runner has recorded itself as a header
  with no verdict, which this runner documents as its CRASH signal. The wall made the one condition
  it exists to make legible the one nobody could read. Observed after the fix:
  `verdict RED` + `wall_breach 5`; three older run dirs in this repo still carry the crash signal.
- **`run-gates.sh` — the wall's only liveness assertion could never fire.** `remove_descendants`
  deleted its `ps` snapshot one line before re-scanning it for survivors, so the walk returned its
  seed and the report could never name a descendant. Byte-for-byte the failure of the startup probe
  this same build deleted, described a few lines lower in the same file. Observed: three pids with
  the snapshot, one without.
- **The ported suite broke every adopter selecting `check-line-length`.** It shipped as
  `role = "engine"` while sourcing `tools/lib/lib-selftest.sh`, gov-internal and shipped to nobody,
  so an adopter got a wired merge-bar leg redding with `build_fixture: command not found`.
  `silenced_legs` cannot catch it — it drops a leg whose argv names a MISSING path, and the argv
  named the suite, which WAS being shipped.
- **`tools/install-prefix-carried.txt` went stale against 22 files** and `--write-ratchet` refuses to
  absorb any of them by design. Each is hand-justified with a reason and its kits column derived from
  the gate's own report.
- **`tools/hooks/kit.toml` lost `[adopt]` and `[check]`** as collateral of the gate-leg removal, so
  `govkit check` red for every adopter selecting `agent-cap`.
- **`run-selftests.sh` printed a GREEN line for a suite it never ran.** An empty budget column
  collapses under `IFS=$'\t'`, the argv read back empty, `eval ""` returned 0. The run loop also
  ignored `$state` entirely. BADBUDGET is a named state now and both readers refuse a non-`ok` row.
- **"ELEVEN AND A HALF HOURS" typed into two shipped files** was 30% stale within a day of being
  written. Deleted; `--list` derives it.

## What is PROMOTED, and why each was not taken here

Twenty-seven, none of them shipped behaviour, and the honest reason for most is that this pass had
already spent its budget on the seven above.

**Arms that cannot fail** — the highest-value group and the one a follow-up should take first, because
each is a green light over something ungraded. `extract-arms.test.sh`'s `prefixed` arm pipes through
`head -1`, so the rc it grades is `head`'s and its want-substring is a substring of the fixture's own
filename, which every refusal message interpolates: delete the leading-word alternation from the
extractor and the arm still reports ok. Its timing-strip arm passes with the timing strip deleted.
`run-gates.test.sh`'s wall fixture advertises a grandchild and creates a direct child, because bash
exec-replaces a subshell whose only command is `sleep` — the same bash behaviour this build documents
elsewhere as the reason a deleted probe graded nothing. Turnstile arms 4c and 4f grade something
other than what they name.

**Unit 1 AC6 has no observer at all.** No arm captures a pid, so the wall's descendant walk is
ungraded — which is precisely how the `rm` in the wrong place shipped inside it. Recorded in that
unit's acceptance ledger as NOT DONE rather than unrun.

**Record accuracy** — the 773 ms and 319 ms per-spawn constants this build reasons from are refuted
by its own in-situ readings; the unit 7 record omitted its second quiet reading (fixed); the x3.34
growth is attributed wholly to population when the checker also gained checks; `registry.toml` says
the budgets file has 55 rows and it has 58; two files still claim the six unattended suites appear in
neither manifest after unit 3 changed that.

**Robustness** — `lib-selftest.sh` runs arms unbounded when `timeout` is absent while its failure
message still names a bound; `EPOCHSECONDS` is a bash 5.0 builtin used under `set -u`;
`run-selftests.sh` fabricates width 2 when `--print-profile` fails, and `--kit` with its value omitted
spins the argument loop forever; `run-unattended-gates.sh` types `ran=$((ran + 6))`, a count of a
population declared in another file, into its liveness counter.

**Documentation** — `WIRE-INTO-PROJECT.md` asserts "that runbook removes them separately" and the
runbook was never touched.

## One finding the review did not make, added by measuring it

`tools/check-install-prefix.sh` is not concurrency-safe. Run while another instance is live it
reported **170 shipped files and 1 drifted row** where three consecutive quiet runs agree on **192 and
22** — it graded a subset and called it clean. Found by accident while fixing its blocker, and worse
than the blocker: a gate that shrinks its own population under load is green for the wrong reason.

## What this review did NOT cover

- It read the diff, not the running system. Nothing here was executed except small scratch
  reproductions; the finders were explicitly barred from running suites because a timing-sensitive
  verification was live on the box.
- It did not re-derive the build's measurements, only checked them for internal consistency.
- The skeptic stage refuted nothing and was not itself audited. See above.
