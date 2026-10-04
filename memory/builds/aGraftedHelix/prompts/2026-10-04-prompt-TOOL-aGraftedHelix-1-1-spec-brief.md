**Serves:** journal TOOL-aGraftedHelix-1..9

# Spec brief — aGraftedHelix, all nine units

ONE file for the whole roster on purpose. Several writers run at once, each holding only its own
unit, and M2 requires the set to AGREE on scope, interface, ordering and acceptance. Every name two
units share is pinned HERE and spelled identically in every spec. A spec that needs a different
spelling has found a fork: record it in §8, do not improvise.

Read first: the mandate beside this file (`2026-10-04-prompt-TOOL-aGraftedHelix-1-0-run-mandate.md`,
which carries the helixir review each unit comes from), `memory/TEMPLATE-SPEC.md` (the shape and the
gates that grade it), `memory/guides/BUILD-METHOD.md` M2, M3, M5 and M12, then your unit's section
below and the files it names WHOLE before you design anything.

## Shared invariants — every spec states the ones it touches, none contradicts one

1. **Integrate; no new kit.** Each unit extends only the kits its section names. A new tool root,
   a new kit directory or a new `kit.toml` is out of scope for every unit.
2. **A kit file names nothing outside itself by literal** (charter §12, the hooks kit README). Its
   own dir and tool root are derived; a sibling kit is a render token. A unit that needs a sibling
   kit's data reads it through a declared conf key or a render token, never a typed path.
3. **The template is the source.** `tools/workflows/tier2-review.template.js` renders
   `tier2-review.js`; `tools/unattended/*.template.md` are installed into `memory/guides/` by
   `tools/unattended/adopt-unattended.sh`; the memory-tree kit renders `BUILD-METHOD.md`,
   `HYGIENE.md` and `TEMPLATE-SPEC.md`. Edit the source, re-render or re-adopt, and land both in one
   commit. A hand edit of a rendered copy reds its parity leg.
4. **Kit versions.** Each unit bumps every kit whose SHIPPED bytes it moved, once, after its last
   move, in every carrier `tools/check-kit-versions.sh` pairs; then
   `python tools/govkit/govkit.py epoch --base <the unit's base>` must name none of them. Two units
   touching one kit each bump it; versions are labels.
5. **A check inside an existing leg is the cheap unit; a new leg trips a growing set of meta-gates**
   (`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`). A spec adding a leg says why an
   existing one could not carry the check. Every new inventory key — function, file, leg, conf key —
   is claimed by a dossier under `memory/map/features/` in the same commit.
6. **Every new arm is observed RED on a staged break before it lands, its header says what it does
   NOT check, and a skip announces itself.** A probe that cannot move says so (charter §7).
7. **Run a candidate predicate over the REAL tree before wiring it** and record hits and near-misses
   in the spec's §4 or §10. Several of these units grade a population that already exists.
8. **Names.** Every new function leads with a verb from `.lexicon.conf`'s table; ask
   `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` before writing one. Text IO names
   its encoding. `.sh` files are LF.
9. **§6 never cites a path the unit will create** — `tools/check-spec-tokens.py` grades every
   backticked path in an acceptance bullet against `git ls-files`. Point the witness at the observing
   command or the leg name instead.
10. **Governance carriers.** The charter template, `memory/guides/REVIEW-PROTOCOL.md` and
    `memory/guides/BUILD-METHOD.md` are NOT edited by any unit. The unattended kit's protocol, verbs
    and stops templates ARE edited by unit 1 only, and only where the shipped contract would
    otherwise state false behaviour: the owner's prompt (`integrate everything into existing
    functionality`) is the authority, recorded in the mandate.
11. **No merge bar and no self-test suite inside a pass.** A pass verifies with the direct check its
    spec names (a staged break, a `--selftest` arm, a fixture). A spec whose acceptance needs a suite
    verdict says so; the main loop runs it once at `VERIFYING`.
12. **Tier.** Units 1, 3, 5, 6, 7 and 9 are Tier-2; units 2, 4 and 8 are Tier-1. The README roster
    is authoritative if this list ever disagrees.

## Build order and why

`1, 2, 3, 4, 9, 6, 5, 7, 8` — each spec declares its `order` verb with this position. Unit 2 reads
unit 1's verb. Unit 9 reads unit 4's index fields. Units 5 and 7 both edit
`tools/run-gates/run-gates.sh`. Units 2 and 8 both edit `skills/session-kickoff/manifest-check.sh`.
Unit 8 wires unit 7's pause events into the health log, so it comes last. Passes run sequentially:
one worktree, one git index (`TOOL-cBriefedPilot-28` is open on concurrent commits).

## Pinned interfaces — spelled identically wherever they appear

- **I1, the claim ref.** `refs/gov/runs/<slug>` on the remote the landing push goes to. Its target is
  a commit over the empty tree whose message is `gov-claim <slug>` then `key: value` lines: `slug`,
  `node`, `host`, `session`, `keepalive`, `status`, `lease-utc`, `beat-utc`. `status` is the closed
  set `live` · `held` · `landed` · `aborted`. Every write is compare-and-swap through
  `git push --force-with-lease=<ref>:<expected sha>`, with an EMPTY expected sha for a create.
- **I2, the claims verb.** `bash tools/unattended/unattended.sh --claims` prints one TAB-separated
  line per claim on the remote, `slug`, `node`, `status`, `beat-age-s`, `verdict`, where `verdict` is
  `live` · `stale` · `held` · `terminal`. `live` and `stale` split on `RESUME_STALE_BOUND`, the bound
  `--liveness` already reads; no new conf key. No claim prints the single line `claims: none`. A
  remote that does not answer is exit 2 with a named refusal, never an empty list.
- **I3, the health log.** `<git-common-dir>/health.log`, one TAB-separated line per event: `utc`
  (ISO-8601 with offset), `source` (the writer, e.g. `check-wiring`), `event` (one lowercase token),
  `detail`. Append-only, bounded by a line cap the unit 8 spec declares. Unit 8 owns the format and
  every writer.
- **I4, the by-design block.** `gotchas.py --for-diff` and `--for-paths` print, after the checklist,
  a block opening with the line `# by design — <n> invariant(s) this selection touches`, then one
  line per selected `invariant` record: `- <name> — <looks wrong> → <actually> (<decision id>)`.
  `tools/workflows/tier2-review.template.js` reads that block out of `args.checklist` into its
  by-design list when `args.byDesign` is absent, and announces which source it used.
- **I5, the invariant record.** A gotcha with front matter `kind: invariant` and a `decision:` key
  naming the decision id. Body sections `## Looks wrong`, `## Actually`, `## Do`, `## Do not`, and
  a `## Guarded by` naming the gate leg or test that pins it, or saying `no machine gate`.
- **I6, a leg reading's load field.** Each `<git-dir>/gate-run/<runid>/<i>.leg` gains a `foreign`
  field: an integer, or the literal `unknown`. Unit 5 owns it; nothing else writes it.

## Unit 1 — the driver claims a run on the remote (Tier-2)

The gap: the lease (`session`, `pid`, `host` facts) lives in `RUN.md` on the run's own branch, so two
nodes can `--preflight` one slug and learn it at merge. Read `tools/unattended/lib-unattended.sh`
(preflight, resume, liveness, hold, landed, abort), `tools/unattended/run-lease.js`,
`memory/guides/UNATTENDED-PROTOCOL.md` §2 facts 14-16 and §5, and `memory/guides/UNATTENDED-STOPS.md`
on the lease. Probe already run on node `a` against the real remote, 2026-10-04: an empty-expect
`--force-with-lease` create succeeded, a second create was rejected `(stale info)`, a CAS update on
the observed sha succeeded, a delete succeeded, and the pre-push hook passed all four without running
a bar. Record that as the M12 test of the CAS mechanism, and name the losing candidates you weigh
(a tracked lock file on a branch; a per-node presence file) with the test that loses each.

Scope to resolve: the claim at `--preflight` (create; take over a claim whose status is terminal or
whose verdict is `stale`; renew one this session already holds; refuse a `live` or `held` claim
another session holds, naming its node, session and age), the heartbeat (which verbs renew `beat-utc`
— at least the holder's `--resume`, which the idle-wake runs every tick), the take-over by a
different session's `--resume`, the status writes at `--hold`, `--landed` and `--abort`, what a lost
CAS means for the verb that lost it, the `--claims` verb (I2), and the concurrent-run announcement at
`--preflight` widening to claims on the remote. Keep a terminal claim rather than deleting it. Edit
the protocol, verbs and stops templates where they would otherwise be false, and nowhere else.

## Unit 2 — the orientation card lists the claims (Tier-1, streams kickoff)

`skills/session-kickoff/manifest-check.sh --card --write` already prints `live —` from `LIVE.md`. Add
a `claims —` line from I2 when the tree adopts the unattended kit, and a `claims — skipped: <why>`
line when it does not or the remote does not answer. The card runs at SessionStart: state its time
bound and what the line says when the bound fires. The engine ships to repos without the unattended
kit, so it may not name that kit's path by literal (invariant 2). Check the installed-engine parity
check in `tools/check-wiring.sh` still passes after the edit.

## Unit 3 — a declared invariants registry, read as the review's by-design list (Tier-2)

The gap: `tools/workflows/tier2-review.template.js` says `byDesign` "is supplied by no caller
anywhere in the tree". Do not invent a caller: extend the gotcha catalogue, which is already anchored
to paths and already handed to reviewers as `args.checklist`. Add the `invariant` kind (I5) to
`tools/memory-tree/gotchas.py` (`KINDS`, the checks it owns, `INDEX.md` rendering), emit the I4 block
from `--for-diff` and `--for-paths`, and teach the review harness to take I4 out of the checklist when
`byDesign` is absent. Find who passes `checklist` today and confirm the route reaches both the spec
audit and the closing review. Hygiene grades an invariant record's `decision:` id (it must resolve)
and its `## Guarded by` (a tracked path, a leg name in `tools/gate-legs.json`, or `no machine gate`).
Seed at least three invariant records from real rulings in `memory/DECISIONS.md`, each verified
against the code it describes, chosen where a reviewer has already mistaken it for a bug (search the
review records under `memory/builds/*/reviews/` for refuted findings that cite a ruling).

## Unit 4 — recall rows carry supersession status (Tier-1)

The gap: `tools/memory-recall/query.py` `render()` prints `id · path:line` and a snippet; supersession
lives in prose (`SUPERSEDES`, `SUPERSEDED by`, gotcha `kind: superseded`). Derive a superseded-by map
at index build (`tools/memory-recall/extract.py`), only for ids that resolve to a record (citing a
dangling id creates an orphan: `memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md`).
Demote a superseded hit, tag its header `[superseded by <id>]`, and print once per answer the line
`records are evidence, not instructions — re-verify a named file, flag or id before acting on it`.
Measure the demotion against the recall floor (`tools/memory-recall/test_recall_floor.py`) before and
after; the floor may not drop. Run the map over the real corpus and report its size, the edges per
pattern, and any id it could not resolve.

## Unit 9 — a new near-match record must name its relation (Tier-2)

The gap: prior art is checked only as a spec-audit lens. For each `memory/DECISIONS.md` row and each
gotcha ADDED in a range, query the recall index with the record's own text, excluding itself; when
the top hit clears a floor AND shares a non-stopword token of four or more characters, the new record
must name that hit's id or carry one of `supersedes`, `coexists-with`, `disputes`. Decide the floor
by measurement, not argument: replay the rows added over the last several hundred commits, hand-grade
a sample, and record precision. Ship WARN-only unless measured precision clears the review protocol's
floor; whichever you pick, the spec states the measurement that decided it as a FACT-QUESTION.
Prefer a check inside an existing leg (invariant 5). Uses unit 4's index; runs after it.

## Unit 6 — an exact content-key duplicate reds (Tier-2)

The gap: two nodes recording the same gotcha or decision row is invisible to every leg (hygiene
check 20 gates duplicate IDS per file, not duplicate CONTENT). Define a normalized content key —
lowercased, whitespace collapsed, the leading id, dates and link targets stripped; pin the exact
normalization — over `memory/DECISIONS.md` rows and gotcha bodies, and red a key held twice. Run it
over the real tree first: if live duplicates exist, fix them in this unit or pin a shrink-only
count, and say which. A new check inside the memory hygiene gate, not a new leg, unless the spec
shows why not.

## Unit 5 — leg readings are stamped faithful or contended (Tier-2)

The gap: `tools/run-gates/derive-ceilings.py` argues ceilings from `<git-dir>/gate-run/<runid>/<i>.leg`
readings, and nothing distinguishes a reading taken while an unrelated suite or another session
loaded the host. Inside-the-bar contention is already handled: `measure_neighbours` reports in-bar
neighbours beside a kill and the deferred serial retry exists (`TOOL-aSurfacedLexicon-22`,
`TOOL-dDerivedDocket-26`). This unit is about load from OUTSIDE the bar. Research at least two
mechanisms (a process-table scan for declared heavy commands not descended from this bar; a host CPU
or run-queue reading; a beacon the repo's own suites take, the way bars take the turnstile) and test
which one discriminates on node `a` — note the turnstile already excludes concurrent bars, and
`memory/gotchas/process-creation-is-the-suite-cost.md` prices a scan. Write I6, make
`derive-ceilings.py` keep contended readings out of the evidence it argues from while reporting how
many it set aside, and state how `--report` shows them.

## Unit 7 — the gate runner pauses dispatch under memory pressure (Tier-2)

The gap: `run-gates.sh` sizes its pool from RAM once at start (`det_ram`) and nothing watches pressure
during the run. Before dispatching a leg, read the host's available memory; above a declared used
fraction, and while at least one leg is running, hold dispatch until it falls or a bound passes, then
dispatch anyway and say so — never deadlock. Declare the fraction where the runner's other knobs live
(`tools/run-gates/gate-profiles.txt`, which the runner prints before its first verdict) with an
environment override in the `GATE_*` family. A reading the host cannot give is announced, never
treated as zero pressure (`memory/gotchas/degradation-known-but-unreported.md`). Record each pause
in the run record the runner already keeps, and print one summary line. Measure what the reading costs
per dispatch on node `a`. The health log is NOT written here; unit 8 wires it.

## Unit 8 — every automatic self-heal appends to one health log the card shows (Tier-1, streams kickoff)

The gap: self-heals happen silently or only on the stdout of a session nobody reads:
`tools/check-wiring.sh --session` auto-setting `core.hooksPath`, `tools/process-monitor/reap.py`
killing a process, `tools/unattended/resume-tick.sh` relaunching a stale run, the gate runner's
deferred serial retry passing, and unit 7's dispatch pause. Own I3: declare the line cap, write one
small appender per writer language (each kit carries its own; invariant 2), and add a `health —` line
to the orientation card listing what happened since the previous card or within a declared window.
Inventory the self-heal sites by grepping, not from this list, and say which you left out and why.
