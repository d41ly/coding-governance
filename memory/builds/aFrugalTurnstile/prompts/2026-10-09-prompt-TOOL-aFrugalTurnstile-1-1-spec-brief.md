**Serves:** journal TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1

# Spec brief — aFrugalTurnstile, all twelve units

You author the spec for each unit you are handed, and you write no code. Read, in this order: the
owner's prompt beside this file (`2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md`), then the design
record `memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md`
WHOLE. **The design record's decisions D1 to D12 are resolved forks: implement them, do not reopen
them.** Your job is to turn the decision a unit implements into a buildable spec: exact insertion
points read from the current source, exact message wording, the fixture that stages the failing case,
acceptance criteria a direct check observes, and the edges. If reading the source shows a decision
cannot work as written, say so in §8 as a FACT-QUESTION with the probe that decides it, and name the
design decision; do not silently design around it.

Every spec is **Tier-2**, under the spec template `memory/TEMPLATE-SPEC.md` with all ten sections,
including `§3 ### Edges` and `§10 Reuse audit`. Filename
`memory/builds/aFrugalTurnstile/spec/2026-10-09-spec-<FAMILY>-aFrugalTurnstile-<n>.md`; status `OPEN`,
`rev-1`, `node a`, `base bef97330`, `streams tooling` (`playbook` for PLAY-1, `deployer` for DEPL-1),
and the header `order` given per unit below. Name the specs you author in `authored` by unit id.

**Invariants for all twelve.**
- A pass runs no merge bar, no self-test suite and no `*.test.sh`; gate-guard refuses them on the run
  branch before VERIFYING. Each acceptance criterion is observed by a DIRECT check: a scratch fixture
  repo under the session scratch, a `--selftest` flag, or a stub bar. Say which in §6. Arms ADDED to a
  suite (`.githooks/pre-push.test.sh`, `tools/run-gates/run-gates.turnstile.test.sh`, …) are part of
  the unit's scope, but they are run at VERIFYING, not in the pass.
- Every new refusal or decision has its failing case OBSERVED in the fixture before the fix: stage
  the case, run the file as it is at base, see the old behaviour, then the fixed file.
- §6 criteria never name a file the unit itself creates as a backticked path (check-spec-tokens joins
  those against `git ls-files`): name the observing command or the leg instead.
- Run `python tools/check-spec-tokens.py --list` and put every `NEAR [guards]` leg it prints for your
  §4 `### Files touched (estimate)` on the §7 leg line.
- No kit-version bump inside a unit; one bump per touched kit happens once, after the last unit.
- Do not edit `memory/DECISIONS.md` or any backlog. Note discoveries in §8 or §3 Edges.
- Every message this build adds to `.githooks/pre-push` keeps the hook's existing shape: one
  `pre-push:` line per decision, and every predicate FORCES; nothing added may make a run smaller
  except the two decisions the design names (`covered`, D4, and lineage reuse, D5).
- A gate's own header states what it does NOT check (charter §7): each spec names the sentence it
  adds there.
- `tools/run-gates/run-gates.sh`'s held-count summary line belongs to the concurrent run
  `aBenchedProbe`; no unit touches it.

## TOOL-aFrugalTurnstile-1 — staleness counts first-parent landings, and a runner stamp is trusted only for the runner's own manifest (`order 1`)

Implements D1 and D2. **Where.** `.githooks/pre-push` `check_green_record` predicate 3 (~1194) and
predicate 7 (~1231); the green-candidate loop (~1301) for the "no runner stamp for a non-runner bar"
rule; `read_green_file` (~1140) for the new `manifest` key; `tools/run-gates/run-gates.sh` stamp
block (~3878) for writing `manifest`, and the inherited-green stamp beside it (same key, same reason).
The decision-line wording `is N commit(s) back` (1457, 1466) changes to name first-parent landings.
**Fixture.** A scratch repo with the runner copied in, a stub-legged manifest and a hand-written
`gate-full-green`: (a) a branch of 12 commits landed `--no-ff`, with the green at the branch tip → old
hook FULL on lag 13, new hook scoped at 1 first-parent landing; (b) 11 first-parent commits on main
past the green → FULL in both; (c) a stamp whose `manifest` names a file outside the kit sibling →
refused, naming the path; (d) `GOV_GATE_CMD` naming a tracked non-runner script with a valid runner
stamp present → the runner stamp is not a candidate, and the line says so; (e) a stamp with no
`manifest` key → read as the kit sibling, so today's stamps keep working. Use `GOV_GATE_CMD_TEST=1`
only where the arm is about the decision, never where it is about bar identity. **Non-goals.**
Re-keying the inherited-green record beyond the `manifest` key; changing `GATE_FULL_MAX_LAG`.

## TOOL-aFrugalTurnstile-2 — pre-push records the green of the bar it ran, and a push whose tree carries one runs nothing (`order 2`)

Implements D3 (pre-push's writer) and D4 (the reader and the `covered` decision). **Where.** The
writer sits after the bar's verdict is final and the HEAD-moved check passes (~1600-1615), and only on
the hook's own green (`rc 0` before the inherited-red landing arm changes it). The reader is a new
cover pass ahead of predicates 2 to 8 over the candidates (runner stamps for a runner bar per TOOL-1,
then `gate-bar-green` in the git dir, then `<common-dir>/gate-bar-green.shared`), and a new decision
branch beside the three at ~1455. `covered` still writes `$PUSH_BAR` so push-main's marker logic is
unchanged, sets `RUNLOG_DECISION=covered`, and exits 0 without running `$gate`; read
`tools/runlog/` for any reader of the decision value and extend it if one exists. The `kind scoped`
half of D4 needs the base this push would pick: for this unit, a `scoped` record covers only when its
`base` equals the full green the scoped decision below adopted (the D9 callable arrives in TOOL-7;
here the comparison is inline). State in the hook header what `covered` does not check (D4's history
gap). **Fixture.** (a) a full bar green, then the same tree pushed again as a `--no-ff` merge commit →
old hook runs a bar, new hook `covered`, no bar process started (the stub bar writes a marker file;
assert it is absent); (b) the same with one byte changed → not covered; (c) a STUB bar green writes no
record; (d) a red bar writes none; (e) a record from bar A offered to bar B → not covered; (f) a record
whose `selftests` is held offered to a `GATE_SELFTESTS=1` push → not covered; (g) a tree read failing
on both sides (an unborn or unreadable sha) → never covered. **Non-goals.** The unattended writer
(TOOL-3); lineage reuse (TOOL-4).

## TOOL-aFrugalTurnstile-3 — the unattended close records the green of the bar it ran (`order 2`)

Implements D3's second writer. **Where.** `tools/unattended/unattended.sh` `gates-green` arm
(~10126-10240): after `_grc = 0`, with HEAD equal to the HEAD before the bar and an empty porcelain
listing, write `gate-bar-green` exactly in D3's grammar, `by unattended`, `kind full` when the bar
ran with `GATE_FULL=1` in its environment (the in-place arm always; the primary arm only when the
caller exported it), else no record (a plain bar is not the boundary's scoped decision until TOOL-9).
The git dir comes from the arm's existing `_ggd`; from a linked worktree it also writes the `.shared`
copy into the common dir. The grammar is spelled in two programs (this one and pre-push), the
pattern `read_policy_key` already follows: name a parity arm that reds when the two writers' key sets
differ, and say which suite carries it. **Fixture.** A scratch repo with a stub `GATE_CMD` and the
driver invoked on the arm in isolation if a seam exists (read `unattended.sh` for its arm-level test
seams, e.g. how `tools/unattended/*.test.sh` drive `gates-green`), else a minimal sourcing harness:
green → record written with the bar string; red → none; dirty tree → none. **Non-goals.** The decision
change under a declared post-merge bar (TOOL-9).

## TOOL-aFrugalTurnstile-4 — lineage reuse: after a red, the boundary's full bar re-runs only failed and moved legs, and may stamp (`order 3`)

Implements D5. **Where.** `run-gates.sh` ledger write (~3643-3685): four new trailing fields; every
reader of the ledger must tolerate them (grep `gate-ledger.tsv` and the `LEDGER`/`TIMINGS` readers,
including the Python dispatch-hint parser and `profile_bar.py`, `derive-ceilings.py`). The reuse block
(~2288-2304): a `lineage` branch with the extra terms. The stamp preconditions (~3873): `reuses = 0`
becomes "every reuse was lineage-qualified", with a counter, and the stamp records `reused`. pre-push:
keep scrubbing an inherited `GATE_REUSE` (~1421) and export `GATE_REUSE=lineage` on a FULL decision
for a runner bar only. The README's reuse section is rewritten, not appended to. **Fixture.** A scratch
repo with three stub legs (one guarded on `a/`, one guarded on `b/`, one unguarded): (a) a FULL run
with the `b/` leg red; fix `b/`; FULL again under `lineage` → the `a/` leg reused, `b/` and the
unguarded leg run, the stamp written with `reused 1`; (b) the same with the previous run NOT full
(scoped) → nothing reused; (c) a manifest change between the runs → nothing reused; (d) the previous
run's head not an ancestor of HEAD (a reset to a sibling) → nothing reused; (e) `GATE_REUSE=1` → reuse
as today and no stamp; (f) an impure leg → never reused. State the measured unguarded share (61 of 128
at base) in §4 as the ceiling on the saving.

## TOOL-aFrugalTurnstile-5 — the gate turnstile is host-wide, names its holder, lets nested bars through, and `--hold` admits a foreign bar (`order 2`)

Implements D6. **Where.** `run-gates.sh` 1088-1512: `TS_COMMON` keeps feeding the health log and
`WORK_COMMON`; a new `TS_HOST` feeds `TS_DIR_C` and `TS_Q`. The beacon writer and `ts_try_reap` (read
the beacon fields and the reaping predicates around 1190-1215) gain `repo`, `run`, `ttl`, and staleness
uses the holder's `ttl` when present, the waiter's own otherwise (an old runner's beacon). The queue
message at ~1439 changes its leading clause only; the `queued at position N (waited Ns)` tail and the
`gate queue: waited` / `acquired` lines stay byte-identical. Nested: the holder exports
`GATE_TURNSTILE_HOLDER`; a runner inheriting a value equal to the live beacon's nonce skips acquiring
and prints one `gate queue: nested under …` line, and the run header's `queued_from` records `nested`.
`--hold -- <cmd…>` is a new verb beside `--print-profile` (read the argument parser), acquires, runs
the command with the holder exported, releases through the same traps, and exits with the command's
status. pre-push scrubs `GATE_TURNSTILE_DIR` and `GATE_TURNSTILE_HOLDER` from the bar's environment
(add both to `BAR_SCRUBBED_KNOBS`, ~1421). The README's turnstile section is rewritten. **Fixture.**
Two scratch repos sharing one `GATE_TURNSTILE_DIR`: (a) a long stub bar in repo 1 and a bar in repo 2
→ old runner runs both at once, new runner queues repo 2 and names repo 1's top level and run id;
(b) a nested runner started by a leg of the holder → not queued; (c) a beacon whose pid is dead →
reaped as today; (d) a beacon with `ttl 600` and a heartbeat 400 s old read by a waiter whose own TTL is
60 → NOT reaped; (e) `--hold -- false` exits 1 and leaves no beacon. **Non-goals.** Changing the TTL or
TS_MAXWAIT derivation; the per-common-dir health log.

## TOOL-aFrugalTurnstile-6 — `post-merge.sh` runs the full bar on a landed sha and publishes its verdict as a remote ref (`order 4`)

Implements D7. A NEW file in the run-gates kit, so it owes: the kit's `kit.toml` file rules (read
it), the declared-population legs (install-prefix, hook destinations, dead paths, codebase-map
coverage: a new script's functions must be claimed, see `memory/map/`), the README, and the lexicon
(`python tools/lexicon/lexicon.py --suggest <name> --as sh.function` for every function name, recorded
in §4 Inventory). **Shape.** `post-merge.sh <sha> [--remote <name>]`: resolve the remote by the
lander's ladder (read how `tools/push-main.sh` and the kit probes resolve it, `dLadderedRemote`;
never a literal `origin`); `git worktree add --detach` a scratch tree under the git common dir; read
`GOV_GATE_CMD` from the gate-env file AT the sha with the same parse the hook uses (never source it);
run it with `GATE_FULL=1` through `run-gates.sh --hold --`; write `gate-bar-green` (`by post-merge`)
into the common dir on green; publish per D7 with one `git push` per verdict, bounded; write
`<common-dir>/gate-post-merge` (`sha`, `verdict`, `run_id`, `published`, `stamped`); remove the
worktree. Exit 0 green, 1 red, 2 refused. **Fixture.** A bare repo as the remote and a clone: (a) a
red stub bar → the remote gains `refs/gov/bar-red` at the sha; (b) a later green on a descendant →
the ref is deleted; (c) a green on a sha that does NOT descend from the red → the ref stays; (d) a
remote that refuses the push → exit 1 with the local file still written and the refusal named.
**Non-goals.** Starting it (TOOL-8); reading the ref (TOOL-7); remote-CI wiring, which is the
adopter's declaration (DEPL-1).

## TOOL-aFrugalTurnstile-7 — pre-push binds a post-merge red, and `--decide` prints the boundary's decision (`order 4`)

Implements D8 and D9. **Where.** `GATE_POST_MERGE` is read at R with `read_policy_key` in the same
block as `GATE_DOC_PATHS`; the `ls-remote` is bounded (read how the hook and the kit bound network
calls) and its failure under a declaration forces FULL with its own reason. The force sits after the
green candidate is adopted, because "descends from the red" is a property of the adopted sha. `--decide
<tip> <remote-sha>`: the hook's decision code runs with stdin replaced by one synthesized ref line,
prints exactly one line (`full <why>`, `scoped <base>` or `covered <record>`) on stdout, writes no
refusal, no run log, no vetted-bar file, runs no bar, and exits 0 (2 on a usage error). Read how the
hook guards its writes so `--decide` cannot reach one; name each write site the spec exempts.
**Fixture.** (a) declared, a red ref on an ancestor of the tip, a full green below it → FULL naming the
red sha; (b) the same with the adopted green descending from the red → scoped; (c) undeclared, the ref
present → today's decision, and no `ls-remote` spawned (count it); (d) declared, the remote unreachable
→ FULL; (e) `--decide` on each of covered, scoped and full prints the one line and leaves the git dir
byte-identical (hash the files the hook can write before and after). **Non-goals.** Deleting the ref
from the hook.

## TOOL-aFrugalTurnstile-8 — push-main starts the post-merge bar after a landing where it is declared (`order 5`)

Implements D10. **Where.** `tools/push-main.sh`, after a landing push succeeded and the lander marker is
written (read the flow around `write_lander_marker`). Read the declaration at the LANDED tip with the
hook's parse. `local`: start `post-merge.sh <tip>` detached with its output to a file under the git
dir, register it the way the process-monitor kit expects a long-lived child to be recorded (read
`tools/process-monitor/`), and print one line naming the pid and the log. `ci`: print one line saying
remote CI owns it. Undeclared: nothing. The child must not hold the lander's stdout (memory note "A
backgrounded job holds the caller's stdout"). **Fixture.** A stub `post-merge.sh` that writes a marker:
declared `local` → marker appears and push-main returns before the stub finishes (the stub sleeps);
`ci` and undeclared → no marker. **Non-goals.** Retrying a failed post-merge bar.

## TOOL-aFrugalTurnstile-9 — the unattended close runs the boundary's decision where a post-merge bar is declared (`order 5`)

Implements D11. **Where.** The in-place branch of the `gates-green` arm. With `GATE_POST_MERGE` declared
at the default-branch side (read with the same reader the arm uses for the inherited-red policy), it
runs `.githooks/pre-push --decide <HEAD> <R>` (resolve the hook through `core.hooksPath` as the lander
does), then the bar under that decision, and writes the TOOL-3 record with the matching `kind` and
`base`; `covered` meets the item without a bar and the item's output names the record. A `--decide`
that fails or prints anything else falls back to today's `GATE_FULL=1` and says so. Undeclared: today's
behaviour byte-for-byte. **Fixture.** As TOOL-3's, with a stub hook printing each of the three
decisions. **Non-goals.** The protocol text (TOOL-10).

## TOOL-aFrugalTurnstile-10 — the unattended protocol's landing rule states the scoped-then-full path (`order 1`)

Implements D12 for `memory/guides/UNATTENDED-PROTOCOL.md` (read its landing rule and its §13 exits;
the file has a size leg, `unattended protocol size`, so measure the bytes you add). State: what the
close runs under a declared `GATE_POST_MERGE`; that the landing push is then `covered`; that a
post-merge red is binding through `refs/gov/bar-red` and forces FULL until a full green descends from
it; what an adopter declares; and that relaxing a project's own stricter unattended rule is that
project's change. Gov's own `.githooks/gate-env.sh` declaration is NOT this unit's (it is decided at
the close, after the code exists). **Acceptance** is textual and observed by grep plus the size leg's
checker run directly.

## PLAY-aFrugalTurnstile-1 — the charter's §1 Landing states the scoped-then-full path (`order 1`)

Implements D12 for `coding-governance-agents.template.md` §1 Landing and its render in `AGENTS.md`.
Read how `AGENTS.md` is rendered from the template (the playbook kit's renderer and the
`playbook render wiring` and `charter size` legs) and keep both byte-consistent; the template has a size
gate (`template size <=48KiB`) and a line-length leg. One or two directive lines, in the charter's
voice (one line per directive), replacing or extending the bullet "After each merge run a diff-scoped
gate…; the push boundary DECIDES whether a full bar is owed…". Point at the protocol for the mechanism
rather than restating it (charter §6: a value stated beside its owning source rots).

## DEPL-aFrugalTurnstile-1 — the runbook states what an adopter declares to use each part (`order 1`)

Implements D12 for `WIRE-INTO-PROJECT.md`: the table in the design record's §4, in the runbook's own
voice, beside its existing gate-env paragraph (read it; `GATE_DOC_PATHS` and `INHERITED_RED` are
documented there and are the model). Include remote CI: the job runs `post-merge.sh <sha>` on every
push to the default branch with a token that can push `refs/gov/*`.
