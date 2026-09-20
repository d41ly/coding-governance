**Serves:** spec-audit TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8

# aQuenchedHarness — spec audit of the eight-unit set, round 2

*Node `a`, 2026-09-06, unattended (authorized-by: prompt). A Tier-2 adversarial pass over the eight
specs as DESIGNS, graded against `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` M2/M3/M12
and `AGENTS.md`: a primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis.
Two surfaces are new since round 1 and both were audited as first-time subjects — unit 8, added
mid-build by `--rescope --act add` and never reviewed, and the rev-2 fold prose across units 1-7,
whose §9 revision-log lines were read as CLAIMS TO VERIFY rather than as history to trust
(`memory/gotchas/fold-text-is-unreviewed-surface.md`). Every claim a finding makes about the existing
tree was re-run at source before it was written here; where a sub-claim did not survive that re-check
it is named inside the finding that carried it.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-1.md@c421f0a98d4b8b6ace9dc849d4ef85ff3dc1006a`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-2.md@97a49fef0fd4a3004f8f4295b3197eda5367487a`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-3.md@7bd81d11439b34cdb046664743ae5b5e07bea5c7`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-4.md@2d5f89da5e4e01e78e8ba2d977cc4bb2e53dd014`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-5.md@ae252d979eff14bef5738cdb2aed4262b2765c2a`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-6.md@81e0832e0231fc5666b1426a959dad10f47cced2`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-7.md@7800886b387774aed8a9cebaecf1363a408a53f2`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-8.md@4e96c4c222f96acdaec778d5d388ae5b320a92dd`

Each blob was recomputed with `git hash-object` against the working tree at read time and matched, so
the eight addresses above are the bytes this report grades and nothing else.

## Verdict: BLOCKED

Eight blockers stand. Three of them are in unit 8 — the order-1 unit added mid-build, never folded,
never reviewed, and the unit the whole build now leans on. Its background ticker is a job of the same
shell that runs the dispatch pool, so as specced it makes `GATE_JOBS=1` — the documented serial
rollback — hang before dispatching a single leg, and it wedges the terminal `wait` at every width:
the unit that exists to stop the bar wedging wedges every bar. Its stated mitigation for a leaked
ticker is a trap, which cannot run on `SIGKILL`, and the orphan's captured `TS_DIR` is a constant path
every later bar recreates, so a killed holder disables the stale-heartbeat signal repo-wide — the
"strictly worse: converts a recoverable wedge into a permanent one" outcome its own §5 claims is
mitigated. And the ticker itself is a previously RECORDED rejected alternative in
`spec-TOOL-aPacedTurnstile-4`, reversed with no supersession by a spec whose §10 asserts that record
was read. Unit 1's wall kills "the process GROUP of every outstanding leg" in a runner that never
enables job control, so there is one group and the runner is in it — and `setsid`, the primitive the
corrected mechanism needs, is not on this node. Unit 3's rev-2 rewrite rests on two claims that are
false at source: the emit does add a manifest reader, and the "drop the file claim" operation the
deployer does not offer. Unit 4 ships gov's own corpus to adopters through a `**` rule neither unit
states a disposition for. Nothing here is a matter of taste; each blocker is a statement about the
tree that was measured, and the measurements are reproduced inline.

## Review shape

Raw 54, confirmed 21, refuted 33, unverified 0, precision 0.39.

Precision fell from round 1's 0.57 to 0.39, which is the expected reading over a corpus that has just
been folded: 33 of 54 raw findings were refuted because rev-2 had already fixed the thing the lens
found, and a hardened surface manufactures refuted noise (`AGENTS.md` §8). It is below the ~0.5 line
that section names as the tighten-scope threshold, and the right response at round 3 — if there is
one — is a narrower subject set, not more lenses.

Unlike round 1, this report performs no editorial merging: 21 confirmed findings map one-to-one onto
21 entries below. Two of them (B2 and H2) share a root premise — unit 8 §5's trap claim — and are
kept separate because their consequences differ and each needs its own fix; the overlap is stated on
both.

## Severity adjudication

The severities in the table are the ones adjudicated in this report. One differs from the grade the
pipeline carried: **B7 (unit 4's adopter ship disposition) was raised from HIGH to BLOCKER**, because
its failure mode and blast radius are identical to B6's — an adopter's bar reds on first invocation —
and grading two instances of one consequence differently would make the table unreadable. The
promotion is recorded here rather than left silent so the count can be reconciled against the
pipeline's.

## Run integrity

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates
  discarded by the pipeline.

Every integrity counter is zero, so the finding set is complete for the lens set that ran, and a zero
count in any dimension below is evidence rather than an artefact of a dead agent. There are no
outstanding unverified findings: every raw finding reached a skeptic and got a verdict.

## What is new since round 1

Two corrections to the framing this round was commissioned under, both verified at source:

- **Units 1-7 are at rev-2; unit 8 is at rev-1.** Its §9 carries one line, "initial draft. Added
  mid-build by an `--rescope --act add` amendment". So unit 8 has neither been folded nor reviewed,
  and it takes order 1. Nine of the 21 confirmed findings below are against it.
- **The rev-2 fold prose is where the propagation defects are.** Three findings (H3, M3, and unit 8's
  exclusion from both) are the same shape: a round-1 correction that reached the unit the finding
  named and stopped there, leaving the identical sentence standing in its siblings. That is
  `memory/gotchas/amendment-leaves-its-other-half-standing.md`, and this round found it three times.

Unit 8's core claim was re-checked and HOLDS. `ts_hb` has exactly one call site at leg completion,
every shipped `gate-profiles.txt` row sets `timeout=0`, the `TS_TTL` fallback is 1800 s, and the
longest recorded leg is 3837 s. A bar does reap its own live holder, and the reproduction in
`memory/builds/aQuenchedHarness/build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md`
§7 is sound. The findings below are against the FIX, not against the diagnosis.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| B1 | BLOCKER | 8 | §2 S1, §4 Inventory, §5 | The ticker is a job of the dispatch shell, so `GATE_JOBS=1` never dispatches and every width hangs at the terminal `wait` |
| B2 | BLOCKER | 8 | §5 risks, §6 AC2 | A SIGKILLed holder's orphan ticker refreshes its SUCCESSOR's beacon forever — the permanent wedge §5 claims is mitigated |
| B3 | BLOCKER | 1 | §2 S4, §4 "The wall" | The wall kills "the process GROUP" in a runner with no job control, so the group it kills is its own |
| B4 | BLOCKER | 3 | §2 S2, §5 error-states | `manifest_subject`/`manifest_chunk` are locals of `selfcheck`; the emit is `_cmd_apply` and never opens the manifest |
| B5 | BLOCKER | 3 | §2 S3, §8 F2 | "Drop the file claim" is an operation govkit does not offer, and F2 states the existing contract backwards |
| B6 | BLOCKER | 3 | §2 S1 vs S3, §1 | Three shipping `subject = repo` legs keep their argv while the emit stops shipping the files it names |
| B7 | BLOCKER | 4 | §2 S1/S2, §4 Files touched | `include = "**"` ships gov's own corpus declaration and a leg whose rows name paths no adopter has |
| B8 | BLOCKER | 8 | §4 Alternatives rejected, §10 | The ticker is a RECORDED rejected alternative, reversed with no supersession by a §10 that claims the record was read |
| H1 | HIGH | 1 | §2 S2 vs §6 AC1-AC6, §2 S7 | Arming the wall at process start — the dangerous first draft — passes every criterion while killing a bar for queueing |
| H2 | HIGH | 8 | §2 S5, §5 risks, §6 AC2 | The ticker's own termination is observed by no arm and no AC, in either exit case |
| H3 | HIGH | 8 (also 1, 2, 4, 7) | §4 Inventory / Files touched, §7 | Two new `ts_*` definitions move `VERB_OFFENDER_PIN`, and `.lexicon.conf` is in no Files-touched list |
| H4 | HIGH | 8 | §2 S4 with §5 | S4 removes the comment that turnstile arm 4c's only `nope` greps for — a declarable red left for the build to discover |
| H5 | HIGH | 8 | §2 S5, §8 | Open row `TOOL-aBoundedCeiling-8` names the exact arm this unit rewrites and the exact prerequisite it satisfies; it is cited nowhere |
| H6 | HIGH | 4 | §2 S8, §10 | "This runner resolves the profile row's width W" — profile resolution is inline in `run-gates.sh` and unreachable |
| H7 | HIGH | 7 | §2 S4 with §6 AC2/AC5 | An absolute spawn pin over a population the same spec says only grows, in the build that exists because of pin-raising |
| H8 | HIGH | 2 | §2 S3, §5 risks | `--write` is not monotone, so a pruned or reused window silently lowers an evidenced maximum |
| M1 | MEDIUM | 8 | §7 Gates | "The three held suites that grade this file" is a described population and it is wrong by at least three |
| M2 | MEDIUM | 8 | §10 recall terms | The recall line is byte-identical across all eight specs and names no turnstile term — the mechanism behind B8 and H5 |
| M3 | MEDIUM | 5, 6 | 5 §4, 6 §10 | "The one prior instance" is false; the larger and closer prior art is this build's own base |
| M4 | MEDIUM | 5 | §8 F1 candidate C2 | C2 is decided on single-shot wall clock, on the machine class whose recorded gotcha forbids exactly that |
| M5 | MEDIUM | 6 | §2 S3 with S2 | The port ranking sorts readings taken under two different conditions with no comparability rule |

---

### B1 — BLOCKER · unit 8 · §2 S1, §4 Inventory, §5

*(confirmed finding id 31)*

A background ticker started at beacon-win is a job of the SAME shell that runs the dispatch pool, and
nothing in the spec says it must be hidden from that pool's job accounting. The mechanism is exact and
was re-run at source:

- The turnstile block and the dispatch pool are both top-level in ONE shell. The runner's own comment
  at `tools/run-gates/run-gates.sh:1203` says so — dispatch and report run from one shell "so this
  shell owns every worker and can BLOCK on `wait -n`" — and there is no subshell boundary between the
  beacon claim and the pool.
- `live() { jobs -rp | wc -l; }` at `:1266`. Dispatch gates on `[ "$(live)" -lt "$JOBS" ]` at `:1275`.
  The reader blocks on `wait -n` at `:1279` when `[ "$(live)" -gt 0 ]`, and there are bare `wait`s at
  `:1300` and `:1304`.

A never-terminating ticker permanently counts as one live job. At `GATE_JOBS=1` the dispatch predicate
is false forever, `[ "$(live)" -gt 0 ]` is true with nothing running, and `wait -n` blocks on a job
that never exits: the documented serial rollback hangs before dispatching a single leg. At any width
the terminal `wait` at `:1304` waits for all children including the ticker, and `ts_tick_stop` is
specced to fire in the EXIT trap — which runs after that wait. §2 S1, §4 Inventory and §5 say nothing
about `disown`, a detached process group or a coproc.

**Fix.** Add to S1 that the ticker is started detached from job control — `disown` immediately after
the `&`, or a detached process group — and state the requirement in §4 explicitly: `live()`, the
`wait -n` at `:1279` and the bare `wait`s at `:1300`/`:1304` must not see it. Add an AC: with the
ticker running at `GATE_JOBS=1`, a fixture bar dispatches and completes, asserted against ELAPSED TIME
rather than against a message.

**Left-shift gate.** A turnstile-suite arm that runs a two-leg fixture bar at `GATE_JOBS=1` under a
hard outer timeout and reds on timeout. It fails today against a naive `&` ticker and passes with the
detach, which satisfies §7's "a new gate is not landed until its failing case has been observed" for
the exact direction that matters.

---

### B2 — BLOCKER · unit 8 · §5 risks, with §6 AC2

*(confirmed finding id 32 — shares §5's trap premise with H2, different consequence)*

§5 binds the ticker to the holder "by the same trap that releases the beacon" — the EXIT/INT/TERM/HUP
set — and no trap runs on `SIGKILL`, which is the case AC2 itself names. A holder killed outright
therefore orphans a still-looping ticker, and that ticker's captured `TS_DIR` is `TS_DIR_C`, verified
at source as the CONSTANT path `"$TS_COMMON/gate-bar-beacon"` that every later bar recreates.
`ts_hb` writes `$TS_DIR/heartbeat` unconditionally.

The sequence: `ts_try_reap`'s dead-PID arm reaps the corpse, so AC2 passes and HIDES this. The next
bar then claims the same directory, and the orphan refreshes ITS heartbeat forever. The
stale-heartbeat signal — which the reap block's own comment says exists for "the holder whose PID was
recycled or which is alive but wedged" — is disabled repo-wide until someone finds the process by
hand. That is precisely the "strictly worse: converts a recoverable wedge into a permanent one"
outcome §5 claims is mitigated, and AC3 then cannot fail for the right reason.

**Fix.** Add to S2/S3 that every ticker write is NONCE-GUARDED the way `ts_release` already is: the
ticker re-reads `$TS_DIR/nonce` and exits when it is missing or is not `$TS_NONCE`. The precedent is
in the file being edited and carries its own rationale comment, so this is reuse, not new mechanism.
Belt and braces in the same line: the ticker also exits when `kill -0 $holder_pid` fails. Add an AC —
after SIGKILLing a holder, the successor bar's beacon goes stale on schedule with the previous
ticker still on the process table, asserted by pid.

**Left-shift gate.** A turnstile arm that SIGKILLs a holder, starts a successor, and asserts the
successor's beacon goes stale within `TS_TTL` — with the orphan's pid printed in the failure message
so the arm names the process it caught rather than reporting an anonymous timeout.

---

### B3 — BLOCKER · unit 1 · §2 S4 and §4 "The wall"

*(confirmed finding id 35)*

S4 says the watcher "kills the process GROUP of every outstanding leg", which assumes each leg has its
own process group. It does not. Verified: `run-gates.sh` carries only `set -u` at `:18`, there is no
`set -m` anywhere, no `setsid`, and legs are dispatched as plain `runleg "$k" &` at `:1276` from the
single dispatch/report shell. Without job control a background job stays in the shell's own process
group.

So there is exactly one group to kill and the runner is in it. A group kill takes down the reader
loop, the watcher and the shell that is supposed to render the verdict — the run dies signalled and
silent instead of exiting non-zero with the RED summary S3 and AC1 require. The only separately
grouped legs today are the ones GNU `timeout` wraps at `:1109`, which is the path S4 correctly says
the wall does not use.

Aggravating, and checked on this host: `command -v setsid` returns rc=1. The primitive the corrected
mechanism would reach for first is not available where this build runs.

**Fix.** State in S4 the mechanism the runner must FIRST create, and name it in §4: either `runleg`
launches its command in its own process group (and, given `setsid`'s absence here, say which portable
means — `perl -e 'setpgrp'`, a `bash -m` wrapper, or recorded per-leg pids plus descendant walk), or
the watcher kills recorded per-leg pids and their descendants without touching the runner's group. Add
an AC asserting the runner SURVIVES the breach long enough to print the summary, asserted by exit
status rather than by output presence.

**Left-shift gate.** A wall arm whose fixture leg exceeds the wall and whose assertion is the runner's
EXIT STATUS plus the presence of the RED summary line. An arm that only greps for the breach message
passes on a runner that was itself killed, which is the shape this finding is about.

---

### B4 — BLOCKER · unit 3 · §2 S2, with §5 error-states

*(confirmed finding id 34)*

S2 claims S1 "reads those two maps; it does not add a reader". Verified at source, that is false in
both halves:

- `manifest_subject` and `manifest_chunk` are built at `tools/govkit/govkit.py:1500-1508`, INSIDE
  `selfcheck()` (def at `:976`, next def at `:1996`) — they are locals.
- The emit is `_cmd_apply` (def at `:4258`), which reads `subject` off the DESCRIPTOR at `:4966` and
  never opens `tools/gate-legs.json` at all. The manifest is opened only at `:1360` and `:1497`, both
  inside `selfcheck`, and `cmd_apply` never calls `selfcheck` — its only caller is the CLI dispatch.

So S1 does add a reader: the emit must load and join the gov manifest itself, and `chunk` is simply
unreachable from the emit path today. Worse, the refusal S2 leans on — "already REFUSES a descriptor
leg that is in no row" — is a selfcheck-time property that does not bind an apply run. At emit time a
descriptor leg with no manifest twin has no `subject` and no `chunk` to test, falls through the filter
and SHIPS. §5's "a descriptor leg with no manifest twin already refuses" is asserting a guarantee from
a different command.

**Fix.** Rewrite S2 to state that `_cmd_apply` gains its own read of `tools/gate-legs.json` and builds
the same two name-keyed maps, factored as ONE helper both `selfcheck` and `_cmd_apply` call so the
predicate has one spelling (§12's single-source rule — two spellings of one predicate is the class
this build cites elsewhere by name). Add to S2 that a descriptor leg absent from the gov manifest is a
REFUSAL at emit time, not a shipped row, and add an AC exercising an emit whose descriptor names a leg
the manifest does not carry.

**Left-shift gate.** A govkit test that runs `apply` against a fixture descriptor carrying one leg the
manifest does not, and asserts the emit REFUSES. It reds today, because the fall-through is the
current behaviour.

---

### B5 — BLOCKER · unit 3 · §2 S3 and §8 F2

*(confirmed finding id 33)*

S3 says each descriptor's file claims "drop" the self-test files, and F2 defends it: "a file a
descriptor does not claim is a file the emit does not copy — which is the existing contract". The
existing contract is the opposite, and the contradicting evidence is in the file the spec cites.
`tools/run-gates/kit.toml` states it outright in its own header: govkit has no `exclude` key, a `**`
rule's pool drops only what another rule owns, and `project-owned` is absent from the landable roles
so `apply` never writes it. Withholding is done by CLAIMING the destination — the descriptor withholds
`run-gates.gov.test.sh` exactly that way, and `tools/memory-recall/kit.toml` does the same for three
files. Under `[[files]] include = "**"` there is no claim to remove, so S3 names an operation the
descriptor schema does not offer, and the rev-2 fold that introduced S3 picked a mechanism the
deployer does not have.

The tree confirms the convention from the other side too: `skills/session-kickoff/manifest-check.test.sh`
and `.githooks/pre-commit.test.sh` are carried by explicit `[[exempt]]` rows, not by being unclaimed.

**One correction to the finding as it arrived.** For `tools/*` kits the surface glob is depth-1
(`surface_paths`, `govkit.py:133-149`), so the kit DIRECTORY is the surface path, and dropping a file
claim would not by itself red the unowned-path check at `:1923-1926`. The overreach does not rescue
the spec: the fold's stated rationale and its operation are both still wrong, and the correct answer
(`role = "project-owned"`) is an existing marker F2 argues it does not need.

**Fix.** Replace S3's "drop the claim" with the mechanism the tree already uses and records: a second
`[[files]]` rule claiming the self-test paths with `role = "project-owned"`. Rewrite F2 to say the
marker exists and is `role`. Add an AC that `govkit selfcheck` is green after the descriptors change —
§7 names it as carrying no guard and running on every bar, so this unit's first commit is where it
would be discovered otherwise.

**Left-shift gate.** A govkit test asserting that an emitted target tree contains no `*.test.sh` from
any kit, run over a real emit rather than over the descriptor text — the descriptor-text version is
the check that would have passed while this defect stood.

---

### B6 — BLOCKER · unit 3 · §2 S1 against §2 S3, with §1

*(confirmed finding id 21)*

S1's emit filter drops only descriptor rows whose gov twin is `subject == kit OR chunk == selftests`,
while S3 drops every kit's `*.test.sh` file claims. The two halves do not describe the same set, and
the gap was enumerated over `tools/gate-legs.json`:

- `kit/dogfood doc parity` → `{kit}/kit-dogfood-parity.test.sh` (`tools/memory-tree/kit.toml`)
- `marker contracts` → `{kit}/marker-contract.test.sh` (`tools/memory-tree/kit.toml`)
- `review-protocol parity (kit vs dogfood)` → `{kit}/check-protocol-parity.test.sh`
  (`tools/workflows/kit.toml`)

All three are `subject = repo`, all three ship, and all three invoke a `.test.sh` that S3 stops
shipping. (A fourth, `codebase-map coverage + freshness` → `test_codebase_map.py`, is caught by S3's
`test_*.py` clause and is the same shape.) So an adopter receives three gate legs whose argv names
files the emit no longer copies: a bar that reds on arrival. That is the exact
broken-on-first-invocation failure §4's "Shipping the files while dropping the legs" rejects, arrived
at from the other direction, and AC1, AC3 and AC5 are all green while it happens.

§1's "Thirty `[[gate_leg]]` rows" is likewise stale fold text: 30 is the count of descriptor rows
matching the rev-1 FILENAME predicate, against the 26/27 the rev-2 subject/chunk predicate actually
holds. The population sentence survived the fold that replaced the population.

**Fix.** Add a scope line joining the two halves: no emitted leg's argv may name a file the emit does
not ship. Add an AC asserting it over a freshly emitted fixture target. Then decide the three named
rows explicitly — either their files keep shipping, or the legs are withheld too — and correct §1's
population to the one S1 actually selects.

**Left-shift gate.** A govkit leg that, over an emitted target, resolves every manifest row's first
file argument and reds naming any row whose file is absent. This is the join the spec currently states
in two places and enforces in neither, and it is cheap: it is a set difference over an emit that the
adopter e2e suite already produces.

---

### B7 — BLOCKER (raised from HIGH) · unit 4 · §2 S1/S2 and §4 Files touched, against unit 3 §1

*(confirmed finding id 26 — see "Severity adjudication" above)*

`tools/run-gates/kit.toml:17-19` is `include = "**"`, role `engine`. Unit 4's Files touched adds
`tools/run-gates/run-selftests.sh` and `tools/run-gates/selftest-budgets.txt` under that rule, and
edits the descriptor for the new "every held leg is budgeted, every budget row resolves" leg. Neither
unit 4 nor unit 3 states a ship disposition for any of the three.

Both files therefore ship by default, and the new leg survives unit 3's filter: every sibling
declaration leg in `tools/gate-legs.json` is `subject = repo, chunk = declarations` (`marker
contracts`, `kit version markers`, `kit/dogfood doc parity`), and unit 3's S3 pattern list
(`*.test.sh`, `test_*.py`, `selftest.py`) reaches neither new filename. So an adopter receives a
declaration whose rows enumerate GOV's held leg names and GOV's six unattended suite paths, plus a bar
leg asserting them — and S2's reverse direction requires each row's argv to name a TRACKED file, none
of which exists in an adopter tree. The leg reds on arrival.

This is the pin-copied-from-another-corpus class that this same descriptor names by name at its
`run-gates.gov.test.sh` withholding rule, and it defeats unit 3's goal on exactly the half unit 3's
predicate cannot see.

**Fix.** Add a scope line to unit 4 withholding both new files by claiming their destination with
`role = "project-owned"`, exactly as this descriptor already withholds `run-gates.gov.test.sh`, and
declare the new leg gov-only via an `[[exempt_leg]]` row rather than a `[[gate_leg]]` one. Add an AC
asserting a fixture emit contains neither file nor the leg.

**Left-shift gate.** The same emitted-tree leg B6 asks for closes this one too, from the other
direction: a row whose argv names a file absent from the emitted tree reds regardless of which unit
put it there. One gate, both defects — which is the argument for building it once here rather than
per-unit.

---

### B8 — BLOCKER · unit 8 · §4 "Alternatives rejected", with §10

*(confirmed finding id 43)*

The chosen design — a background ticker refreshing the beacon heartbeat on its own clock — is a
previously RECORDED rejected alternative. `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md`
rejects "a background ticker process refreshing the heartbeat on its own clock ... one more process
per run on a machine measured as spawn-bound, to maintain a number a leg-sized TTL makes unnecessary",
with the supporting analysis ("Why the reader loop is not a refresh site") a hundred lines above. That
record deliberately DROPPED the second refresh site so the TTL would be "sized against a LEG rather
than against a gap" — the exact cliff unit 8 exists to remove.

Unit 8's §4 Alternatives-rejected records only the TTL raise and `timeout=`. It records neither the
ticker's prior rejection nor which of its premises it overturns, while §10 asserts that
`TOOL-aPacedTurnstile-1` through `-16` "were read before writing" — the assertion this omission
contradicts. `AGENTS.md` §6 requires a ratified record to be superseded with a new note, never
silently reversed.

The engineering case for the reversal is sound and stated: the 1800 s fallback sits BELOW the
3837 s longest leg, so the TTL is not in fact leg-sized and the prior record's premise is refuted by
measurement. That is what makes this cheap to fix and keeps it out of the "wrong design" bucket. It
stays a blocker because an order-1 unit landing UNATTENDED reverses the load-bearing decision of the
file it edits, with no owner turn anywhere downstream to catch the missing supersession.

**Fix.** Add the ticker to §4 as prior art now OVERTURNED, citing `spec-TOOL-aPacedTurnstile-4`'s
rejection bullet and its analysis section. State that the "a leg-sized TTL makes it unnecessary"
premise is refuted by this unit's own 3837 s reading against the 1800 s TTL, and price the SURVIVING
spawn-bound premise as a number — ticks over the longest leg at the derived cadence, times the 319 ms
spawn cost on this host — rather than leaving it unaddressed.

**Left-shift gate.** Not gateable as a predicate; it joins the §10 checklist as a documented check:
*a scope item that changes behaviour a prior spec explicitly rejected cites that rejection and states
which premise it overturns.* M2's fix (a real recall query per unit) is the mechanism that makes the
check answerable rather than a matter of memory.

---

### H1 — HIGH · unit 1 · §2 S2, against §6 AC1-AC6 and §2 S7

*(confirmed finding id 5)*

S2 makes arming the wall at first leg DISPATCH — not at process start — a scope requirement,
precisely so that a bar queued behind the turnstile is not killed for waiting its turn. Nothing
observes it. S7's five arms are a long leg, an untimed control, `wall=0`, an INERT wall and a
grandchild; AC1-AC6 all run against a fixture that acquires the beacon immediately.

So arming at process start — the simpler first draft, and the natural one given that the turnstile
acquire precedes leg dispatch in the runner — passes every criterion in §6 while killing a healthy bar
that waited up to `TS_MAXWAIT` (`TS_TTL * 4`, so 7200 s at the shipped 1800 fallback). This is the
wall's single most dangerous mis-implementation, it lands green, and it is precisely the unit-8
interaction that made this unit order 2. Unit 8's own ACs cannot cover it either: unit 8 lands first,
before the wall exists.

**Fix.** Add an AC and an S7 arm: a fixture bar that waits behind a held beacon for longer than the
declared wall, then runs a short leg, completes GREEN, and the arm asserts the wall's own elapsed
measurement starts at first dispatch and not at process start.

**Left-shift gate.** That arm IS the gate, and §7's "a new gate is not landed until its failing case
has been observed" applies directly: stage the arming point at process start, confirm the arm reds,
unstage.

---

### H2 — HIGH · unit 8 · §2 S5 and §5 risks, against §6 AC2

*(confirmed finding id 8 — shares §5's trap premise with B2; this is the leak, B2 is the corruption)*

§5 names a ticker leak as "strictly worse than today", then binds it off "by the same trap that
releases the beacon". Verified: the beacon release runs from traps on EXIT/INT/TERM/HUP, and no trap
runs on `SIGKILL`. The mitigation does not cover the case the reap exists for.

Nothing observes the TICKER's own termination — not in S5's three arms, not in AC1-AC5, in either the
normal-exit or the SIGKILLed-holder case. AC2 passes regardless, because `ts_try_reap`'s dead-PID
signal reaps on the pid independently of the heartbeat: AC2 is green whether the ticker leaked or not,
so the leak is unobservable by construction and accumulates one sleeping process per killed bar.

This repo has recorded this exact class twice — orphaned background loops surviving their parent and
contaminating timings — in a build whose other units depend on clean second-readings. The unit whose
entire subject is process liveness states a mitigation that provably misses the case.

**Fix.** Add an S5 arm and an AC: after a normal run, and after a run whose holder is SIGKILLed, no
ticker process descended from that bar survives, asserted by pid. Correct §5 to say the release trap
covers the signal-catchable exits only, with the pid check as the backstop for the rest.

**Left-shift gate.** A turnstile arm that records the ticker's pid and asserts `kill -0` fails after
the bar exits, in both exit modes. It is the same fixture B2's gate needs, so the two arms share
setup.

---

### H3 — HIGH · unit 8 (and units 1, 2, 4, 7) · §4 Inventory / Files touched, with §7

*(confirmed finding id 46)*

`ts_tick_start` and `ts_tick_stop` are new shell function definitions whose leading token `ts` is not
in the declared verb table. Verified at source, all three legs of it:

- `.lexicon.conf:88` pins `VERB_OFFENDER_PIN="978"`, and the file's own header records the owner ruling
  that made every pin an equality in BOTH directions.
- `python tools/lexicon/lexicon.py --suggest ts_tick_start --as sh.function` returns "`ts` is not in
  the declared table ... a SCOPING question", and `--list` already carries `run-gates.sh` `ts_now` and
  `ts_hb` as live P1 verb offenders — so the shell cell is armed and `ts_*` definitions already count.
- Two more definitions take the population to 980 against a two-sided pin. `lexicon naming predicates`
  has a `tools/` guard, `subject = repo`, `chunk = declarations`: it is NOT held and it fires on this
  edit.

`.lexicon.conf` appears in neither unit 8's Files touched nor its §7. Units 5 and 6 both name the
lexicon leg explicitly, because unit 5's rev-2 M1 fold ran this check for its verbs and noted "§7 now
names the lexicon leg, which no spec in the set did". The fix reached units 5 and 6 and stopped —
the amendment-leaves-its-other-half-standing class — and units 1, 2, 4 and 7 each mint identifiers
while naming neither the conf nor the leg. The recorded gotcha adds the sting: a branch bar can skip
that leg as unchanged-vs-main, so it fails at the LANDER, on an unattended run.

**Fix.** Record the lexicon result for both verbs in §4 beside the `sh.function` cell that grades them;
add `.lexicon.conf`'s `VERB_OFFENDER_PIN` move plus its justification line to Files touched; name
`lexicon naming predicates` in §7. Apply the same to units 1, 2, 4 and 7.

**Left-shift gate.** Already gated — the leg exists and is correct. What is missing is a DoR habit, so
this is a §10 checklist entry: *a unit that mints a function definition records its `--suggest` result
and its pin delta before the build starts.* The gate catches it; the checklist is what stops it
catching it at the lander.

---

### H4 — HIGH · unit 8 · §2 S4, with §5 and §4 Files touched

*(confirmed finding id 44)*

Verified byte-for-byte at `tools/run-gates/run-gates.turnstile.test.sh:228-230`: the arm greps for the
literal `ponytail: a single leg longer than TS_TTL` in `run-gates.sh` and calls `nope` when it is
absent. That is the ONLY `nope` in arm 4c, and it matches the comment S4 removes. So `run-gates
turnstile` — which §7 names among the suites this unit must keep green — reds the moment S4 lands. §5
declares three NEW arms and says nothing about retiring the existing pin, so the build spends a cycle
discovering a red it could have declared. This is the byte-pin-in-a-held-suite class
`TOOL-aBoundedCeiling-10` already records.

**One correction to the finding as it arrived.** 4c's behavioural half calls `ok` on BOTH branches, so
it does not red; it merely goes on printing "the ceiling is not reachable on this host at this timing"
as a permanent state. Only the byte-pin half is a genuine red — which is enough, and is a declarable
one.

**Fix.** Add a scope item: arm 4c is rewritten in the SAME commit — the comment grep retired with the
comment, its behavioural half inverted to S5's first arm — and name
`tools/run-gates/run-gates.turnstile.test.sh` arm 4c explicitly in §4 Files touched.

**Left-shift gate.** A `run-gates` self-test arm that greps the suite corpus for `grep -q '<literal>'
"$HERE/run-gates.sh"` byte-pins and reds naming each one, so a source-comment pin is discovered at
authoring time rather than when someone edits the comment. It has live instances today, which is the
argument for it.

---

### H5 — HIGH · unit 8 · §2 S5 and §8

*(confirmed finding id 45)*

Open backlog row `TOOL-aBoundedCeiling-8` (`memory/backlog/TOOL.md:37`) records that turnstile arm 4c
CANNOT FAIL — both branches `ok`, the only `nope` grading a comment rather than a mechanism — and
states the prerequisite: touching it "needs its failing case observed first, which is a unit". Unit 8
is that unit. It rewrites the arm's subject in S5 and removes the comment 4c's only `nope` grades in
S4, so it touches the arm twice, and it cites the row nowhere.

The row will either be closed silently by a unit that never claimed it, or left open beside a
rewritten arm nobody re-checked. M2 is the mechanism: the recall probe was never run over this domain,
so an OPEN row naming the exact arm, the exact defect class and the exact prerequisite this unit
satisfies never reached the spec.

**Partial mitigation, stated so the severity is honest.** §5's "S5's arms, each observed RED before
landing" does answer the could-not-fail class for the NEW arms, so the finding's implication that §6
inherits the shape overreaches. The uncited open row and the S4/4c collision stand.

**Fix.** Name `TOOL-aBoundedCeiling-8` in §3 or §8, state whether S5's three arms close it, and if
they do, say so in the wrap-up so the row is retired by the unit that fixed it.

**Left-shift gate.** A DoR check rather than a bar leg: *before a unit edits a named file, grep
`memory/backlog/<FAMILY>.md` for that path and cite or dismiss every OPEN row naming it.* It is one
grep and it would have returned this row.

---

### H6 — HIGH · unit 4 · §2 S8, with §10

*(confirmed finding id 40)*

S8 says "This runner resolves the profile row's width W", assuming profile resolution is reachable
from a new script. It is not. Verified: core and RAM detection and row selection are INLINE in
`run-gates.sh` — `KNOWN_KNOBS` at `:177`, `PROFILES` at `:178`, the probes at `:193-235`, selection and
`PROF_WIDTH`/`PROF_NAME` at `:262-333`, `PROF_LINE` at `:404`. The script accepts no CLI verbs at all,
there is no sourceable resolver, and `run-gates.sh` is absent from unit 4's Files touched. §10 names
`run-unattended-gates.sh` and the declared-value FILE SHAPE as the seams, never the resolver.

So `run-selftests.sh` has no stated way to obtain W. It either re-implements detection and row
selection — a second implementation of one predicate, the class unit 2 §10 cites by name — or
hardcodes a width, at which point S8's composite bound and unit 5's `SELFTEST_INNER_WIDTH` are
computed from a number that can silently disagree with the bar's. AC7 would still pass against the
wrong W. The composite bound rev-2 added to fix the squared-width defect rests on this.

**Fix.** Add to S8 how W is obtained: extract profile resolution into a sourceable
`tools/run-gates/lib-profile.sh` that `run-gates.sh` sources too, or add a `--print-profile` verb to
`run-gates.sh` that emits the selected row. Name it in §4 Inventory and §10, and add
`tools/run-gates/run-gates.sh` to Files touched. Add an AC asserting the width `run-selftests.sh`
resolves is byte-equal to the one `run-gates.sh` prints on its profile line, on the same host.

**Left-shift gate.** That byte-equality assertion, as a `profile-bar selftest` arm: two resolvers, one
answer, compared on every bar. It is the §12 single-source rule with a parity gate, which is what this
repo does everywhere else a value has two readers.

---

### H7 — HIGH · unit 7 · §2 S4, with §6 AC2 and AC5

*(confirmed finding id 37)*

S4 pins an ABSOLUTE post-change spawn count and AC2 demands "an absolute number written before the
work", over a population §5 itself says "grows with every landed build". Verified against the unit's
own cited base: `274aa39b` DELETED a hardcoded 35000-spawn figure with the reason "spawn count is
walked depth times graded population, and both only grow", and the surviving header at
`check-pass-order.sh:224-226` states the count as a product rather than a number. AC5 pins
`check-pass-order.sh` — the exact checker whose count that commit recorded as monotonically growing.

A pin over a growing population reds on the next landed build with no regression whatsoever, so the
left-shift gate S4 calls this unit's real product becomes a gate that fails for a reason nobody
caused. The predictable response is the one this build exists because of: somebody raises the pin. The
unit re-files the class it is closing.

**Fix.** Make the pin NORMALISED rather than absolute in S4 and AC2 — spawns per graded unit (per
`RUN*.md` walked, per commit walked) — with the population size DERIVED at run time and printed beside
it. Keep S3's absolute seconds target if you like, but say in §4 that the seconds figure is a reading
and the SPAWN figure is the gate, and that the gate's denominator is derived, never typed.

**Left-shift gate.** The normalised pin IS the gate, and it satisfies §7's "NO count of a derived
population is written in prose" in the only way that survives the next commit. Stage an extra `RUN.md`
into the fixture corpus and confirm the normalised pin does NOT move — that is the failing case worth
observing, inverted.

---

### H8 — HIGH · unit 2 · §2 S3, with §5 risks

*(confirmed finding id 38)*

S3 says `--write` "refreshes" the tracked evidence file with the maximum recorded seconds, and never
says the refresh may not LOWER an existing row. The reading population is a sliding window that
shrinks, on two independent mechanisms both verified at source: `GATE_RUN_KEEP` defaults to 5 and the
sweep at `run-gates.sh:1447` prunes older run directories, and a REUSED leg writes `reuse` to its rc
at `:1077` before `runleg`, so it never reaches the `.leg` write and contributes no reading at all.

So once the run that held a leg's worst reading is pruned — or once the leg is reused for a few bars —
the next `--write` silently overwrites a high evidenced maximum with a lower one, and S5's relation
then permits a ceiling BELOW a value this repo has actually observed. §5's risk paragraph already
ASSUMES the monotonicity S3 does not state ("a stale row still bounds the ceiling from below, which is
the direction that matters"). S6 covers the empty-population case with a refusal, but not the smaller-
population case. The tracked artifact quietly widens the bound it was written to hold, which is the
exact failure AC5 guards against in the other direction.

**Fix.** Add to S3 that `--write` is MONOTONE per leg: the new row's maximum is
`max(existing row, observed)`, and a row is lowered only by an explicit `--reset <leg>` that records
why and by whom. Add an AC: after a `--write` over a population whose maximum is lower than the
committed row, the row is unchanged and the report says the observed population was below the record.

**Left-shift gate.** An evidence-suite arm that writes a row, then re-runs `--write` over a fixture
population with strictly smaller readings, and asserts the tracked row did not move. It reds today
against the specced behaviour, which is the point.

---

### M1 — MEDIUM · unit 8 · §7 Gates

*(confirmed finding id 48)*

"`run-gates turnstile`, `run-gates canary` and `run-gates evidence`, the three held suites that grade
this file" is a population DESCRIBED rather than enumerated, and it is wrong. Legs with a
`tools/run-gates/` guard that an edit to `run-gates.sh` fires: `run-gates turnstile`, `run-gates gov
canary` (subject repo, chunk selftests — held, and it grades the runner BY NAME), `run-gates adopter
e2e` (subject kit — held), `profile-bar selftest` (subject kit — held), plus `run-gates canary` and
`run-gates evidence` via their `tools/` guard. Wrong by at least three, and the omitted one is the
suite whose subject IS this runner.

A reader taking §7 at its word reads a green three-leg run as coverage of the change — the
green-by-absence reading round 1 raised for units 2 and 3 as M2 and U1, which unit 8 inherited
unreviewed. §7's DoD line (`GATE_SELFTESTS=1`) does run the full held set, so the practical coverage
exists; the sentence a reader would take as the coverage claim is still false, which is why this is a
medium and not a high.

**Fix.** Derive the list from `tools/gate-legs.json` — the held legs whose guard matches
`tools/run-gates/` — or name the DERIVATION instead of a list, and add `run-gates gov canary` and
`profile-bar selftest` at minimum.

**Left-shift gate.** A hygiene check that a spec's §7 leg names all exist in `tools/gate-legs.json` is
cheap and would not have caught this one (every named leg exists; the list is incomplete, not wrong).
The real left-shift is the §10 checklist entry round 1 already earned: *a spec states a leg population
by derivation, never by enumeration in prose.*

---

### M2 — MEDIUM · unit 8 · §10, "Recall terms used"

*(confirmed finding id 49)*

The terms line is byte-identical across all eight specs and names no turnstile, beacon, heartbeat,
reap or holder term. Unit 8 was added mid-build by an `--rescope` amendment ABOUT the turnstile, and
its own §10 says the defect was found by probing unit 2 §8 F1 — a different route entirely. So the
retrieval `memory/TEMPLATE-SPEC.md` requires ("the retrieval arguments you actually passed, verbatim")
was not run for this unit's subject.

This is the mechanism behind B8 and H5. Re-run at source for this domain, the query returns the
`aPacedTurnstile-4` ticker rejection as hit 4 and the `TOOL-aBoundedCeiling-8` arm-4c row as hit 5, in
a 3.01 s index rebuild. Both blockers-and-highs above were three seconds away.

It matters beyond this build: BUILD-METHOD M7's regrounding step 5 RE-RUNS the recorded line, so every
later session regrounding unit 8 will query this corpus about selftest ceilings and adopters rather
than about the turnstile. Whether the line was copied or the generic terms were genuinely passed is an
inference either way; the consequence is identical.

**Fix.** Replace the copied line with the terms actually passed for this unit's domain, read what they
return BEFORE the build starts, and fold the two records above into §4 and §8.

**Left-shift gate.** A hygiene check that the `Recall terms used` line is not byte-identical to
another spec's in the same build folder. It is a one-line set comparison over a build's spec set, and
it reds on this build today.

---

### M3 — MEDIUM · units 5 and 6 · 5 §4 "The cost model", 6 §10

*(confirmed finding id 50)*

Unit 5 §4 says `tools/unattended/run-unattended-gates.sh` "records the one prior instance of lowering
it", and unit 6 §10 says "the one prior instance of this exact work in this tree". Both are false:
`check-pass-order.sh`'s spawn rebuild landed in this build's own base at `4042505a` and `274aa39b`,
10184 s to 510 s, and `check-pass-order.sh:220` records the figure. Unit 7 §10 names it explicitly as
"the second instance of that technique".

Three specs in one set, two saying one instance and one saying two — and the uncited instance is by
far the larger measurement (10184 s → 510 s against 469 → 220 spawns) and the closest method prior art
for unit 5's F1 and unit 6's ports. Unit 7's rev-2 fold (H8) is what established the second instance;
it did not propagate to units 5 and 6, whose §10 sentences were EDITED at rev-2 and kept the singular.
The amendment-leaves-its-other-half-standing shape again, this time across units.

**Fix.** Cite the pass-order rebuild (`4042505a`, `274aa39b`) in unit 5 §4 and unit 6 §10 as the second
and larger instance, and read its recorded method — one pass over history into a subject cache,
byte-identical summary, spawn count as the claim — into F1's C1 and C3 before the probe is run.

**Left-shift gate.** Not gateable; §10 checklist entry: *when a fold corrects a factual claim, grep the
build's other specs for the same sentence before closing the fold.* Three of this round's findings are
that one omission.

---

### M4 — MEDIUM · unit 5 · §8 F1, candidate C2

*(confirmed finding id 51)*

C2's losing test is wall clock at width N against width 1, on the machine class whose own recorded
gotcha states that wall clock there is not measurable to better than a factor of two.
`memory/gotchas/process-creation-is-the-suite-cost.md` measured the same workload at 10.7 s to 26 s in
one session, and mandates interleaving old and new, taking the minimum, and preferring the
deterministic spawn-count proxy "for the claim you actually write down". C1 uses the spawn count; C2
does not.

F1's "run in the same conditions" is a control, not a noise protocol. Unit 2 §3 of this same build puts
the same-leg spread at 5.5x median and 47.1x worst on this node — wider than the gain a bounded-width
parallel run would show — and the primary tree's ledger corroborates it (the unattended kit gate at
3837 s there against 819 s in this worktree). So C2 can be adopted or rejected on ambient load.

The finding's implied remedy of a spawn-count proxy is impossible for a PARALLELISM candidate, which
bounds the severity; it does not rescue the criterion.

**Fix.** State C2's protocol in F1: interleave the width-1 and width-N runs, take the MINIMUM of each,
and report the spawn count from S6 beside the seconds so the verdict does not rest on a single loaded
reading.

**Left-shift gate.** Not a bar leg — a §10 checklist entry: *a spec that decides a fork on wall clock
states its interleave-and-minimum protocol, or the fork is decided on a deterministic proxy.* The
gotcha exists; what is missing is the point at which someone is made to read it.

---

### M5 — MEDIUM · unit 6 · §2 S3, with S2

*(confirmed finding id 52)*

S3 selects "in descending recorded seconds" over a population whose readings come from two different
conditions — unit 4 F2 resolves that readings come from bar `.leg` rows for held legs and "from a
direct timed invocation where it is not" — with no requirement that the readings being ranked be
COMPARABLE. S2 refuses on MISSING evidence, not on incomparable evidence, and S6's same-conditions
rule governs the port floor, not the selection.

A leg measured inside an 8-wide bar and a suite measured standalone are not on one scale, and unit 2
§3 puts the same-leg spread at 5.5x median and 47.1x worst on this node — wider than most of the gaps
this ranking has to resolve. The set is visibly already mixed: the primary tree's ledger carries
`unattended gate selftest` at 812.358 s while `run-unattended-gates.sh:66` carries
`BUDGET_gate_selftest` with "MEASURED 3565 s end to end", the figure unit 6 F3 ranks it FIRST on. A
4.4x split on one suite, against a majority-share cut the ranking must resolve. The majority-share set
is then chosen by which readings happened under contention, and the ports may miss the suites that
actually hold the cost.

Bounded by S9 naming the remainder, which is why this is a medium rather than a high.

**Fix.** Add to S2 or S3 that the reading used for the RANKING must be taken in one stated condition
for every row — or rank on the spawn count, which unit 5 S6 already produces and which the recorded
gotcha names as the claim to write down.

**Left-shift gate.** Have the ranking print, per row, the condition its reading came from, and red when
the set spans more than one. It is three lines, and it makes the defect visible instead of silent.

---

## Closing observation

Round 1's closing observation was that five of six blockers came from describing a population rather
than enumerating it. Applied to the rev-2 text, the pattern has MUTATED rather than cleared, and it
mutated in a specific direction worth recording:

**The folds fixed the population where a lens had pointed, and nowhere else.** Unit 3's rev-2 replaced
the filename predicate with a subject/chunk one and left §1's "Thirty rows" describing the population
it deleted (B6). Unit 7's fold established the pass-order rebuild as a second prior instance and left
units 5 and 6 saying "the one prior instance" (M3). Unit 5's fold added the lexicon leg to §7 and
units 1, 2, 4, 7 and 8 still name neither the leg nor `.lexicon.conf` (H3). Three separate instances
of `memory/gotchas/amendment-leaves-its-other-half-standing.md` in one fold cycle — which is the
finding this round most wants left-shifted, and the cheapest: grep the sibling specs for the corrected
sentence before closing a fold.

**Two of unit 3's blockers are a new class, not the old one.** B4 and B5 are not descriptions of a
population; they are claims about the DEPLOYER's existing behaviour that are false at source — "it
does not add a reader" when the emit never opens the manifest, and "the existing contract" stated
backwards when the tree's own descriptor header records the opposite two files away. Rev-2 traded an
unenumerated population for an unverified mechanism claim. The lens that catches this one is not
"enumerate it" but "open the function you are claiming about", and both claims were the load-bearing
sentence of the fold that introduced them.

**And the unreviewed unit is where the damage concentrated.** Nine of 21 confirmed findings and three
of eight blockers are against unit 8 — the unit added mid-build, never folded, never audited, and now
holding order 1 with the rest of the build leaning on it. Its diagnosis is correct and reproduced. Its
fix, as specced, hangs the serial bar (B1), permanently disables the stale-holder signal after a
kill -9 (B2), and silently reverses a ratified decision of the file it edits (B8). A mid-build
`--rescope --act add` that skips the audit round its siblings got is not a cheaper path; it is the
same cost, deferred to the build.
