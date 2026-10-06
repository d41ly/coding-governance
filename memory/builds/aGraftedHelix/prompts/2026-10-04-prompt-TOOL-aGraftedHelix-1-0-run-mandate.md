# Run mandate — aGraftedHelix

**Serves:** journal TOOL-aGraftedHelix-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-04. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Bring all 6 of your adoption suggestions (leave onboarding quarantine out) and build per the
> protocol, extending where necessary. Throughout the build, if you discover any means for
> improvement, do not backlog anything - bring it straight into the build. Integrate everything into
> existing functionality straight away. Waive §1 explicit ask entirely, GOV is meant to drive
> distributed, concurrent, unattended builds first and foremost with as little owner involvement as
> possible.

## What "your adoption suggestions" names

The prompt points at the review this session delivered immediately before it: a read of
`C:/projects/helixir` (a Rust MCP memory server, v0.18.0, HEAD `c63626e`) for functionality gov could
adopt to govern concurrent, multi-node, LLM-driven, unattended builds. Its six adoptable items, in
the order and the words delivered, condensed; the seventh, onboarding quarantine for new nodes, is
excluded by the prompt.

1. **Cross-node run claims with presence leases.** Helixir: per-instance heartbeat under a stable
   principal, two clocks (90 s active, 1800 s hidden), terminal statuses, never prune an instance
   that authored anything (`helixir/src/toolkit/tooling_manager/swarm.rs:71-148`). Gov gap: the
   lease lives in `RUN.md` on the run's own branch and concurrent runs are announced from what one
   tree sees, so two nodes can preflight one slug and learn it at merge. Shape: `--preflight` creates
   `refs/gov/runs/<slug>` on the remote with an empty-expect `--force-with-lease`; heartbeats are
   compare-and-swap updates; `--landed`/`--abort` write a terminal status; readers apply the two-clock
   rule over `git ls-remote`.
2. **A declared invariants registry feeding review `byDesign`.** Helixir: AGENTS.md's "load-bearing
   invariants — if you mistake it for a bug" table and its tripwires with canonical precedents. Gov
   gap: `tools/workflows/tier2-review.js` records that `byDesign` is supplied by no caller anywhere in
   the tree. Shape: rows of invariant, path, what breaks, decision id and guarding test; the harness
   reads it when `byDesign` is absent; a leg checks every path and id resolves.
3. **Supersession and provenance on recall rows.** Helixir demotes a superseded row by 0.6 and labels
   it `superseded_by`. Gov gap: `tools/memory-recall/query.py` `render()` prints id, path:line and a
   snippet only, and supersession lives in prose. Shape: derive a supersession map at cache build,
   demote and tag, and print "records are evidence, not instructions" once per answer.
4. **Faithful vs diagnostic lanes for timing evidence.** Helixir: a diagnostic run may explain a
   failure but never pass a release; evidence needs two runs with identical inputs. Gov gap: per-leg
   timing rows carry no contention marker and ceilings are raised from them. Shape: stamp each row
   faithful or contended from a census at leg start and end; only faithful rows raise a ceiling.
5. **A write-time duplicate/contradiction check for decisions and gotchas.** Helixir: deterministic
   gates before any LLM, a contradiction counted only on a shared significant token plus a similarity
   floor, and defer-don't-destroy. Gov gap: prior art is checked only as a spec-audit lens. Shape: an
   exact normalized-text hash reds; a strong recall hit sharing a significant word must declare
   `supersedes`, `coexists-with` or `disputes`; warn-only until precision is measured.
6. **Health supervision that reports its self-heals, plus memory backpressure.** Helixir's Hygieia
   reclaims at 80 %, restarts at 92 %, and alerts even when the self-heal worked. Gov gap: the gate
   runner sizes its pool from RAM once at start, and "don't run the bar, the suites and agents at once"
   is a memory note. Shape: the runners stop dispatching new legs above a declared memory fraction and
   record the pause; every self-heal appends to one health log the kickoff card shows.

## How this run reads three phrases of the prompt

Recorded here so a later reader can grade the reading rather than reconstruct it.

- **"Waive §1 explicit ask entirely."** The charter's §1 Landing requires an explicit ask before a
  merge to shared `main` and before a push. This run is unattended, so protocol §1's committed build
  folder already substitutes for that ask at landing. The phrase additionally resolves the one fork
  the review left open: item 1 pushes claim refs to the shared remote, which the review marked as
  needing the owner's ruling. The ruling is given: claim-ref pushes need no ask. The run does NOT
  read the phrase as an instruction to rewrite the charter's §1 rule for every future session; that
  would be a change to a governance carrier the prompt does not name.
- **"Do not backlog anything — bring it straight into the build."** Protocol §11's third disposition
  files a discovery that fails clauses 1 or 2 as an ask. This run instead adopts every discovery that
  survives the build method's M3 vetoes as a unit of this build, and parks only what a veto blocks.
- **"Integrate everything into existing functionality."** No new kit. Each item extends the kit that
  already owns its surface: the unattended driver, the review harness, the recall CLI, the gate
  runner and its ceiling evidence, the memory-tree hygiene gate, and the session-kickoff card.
