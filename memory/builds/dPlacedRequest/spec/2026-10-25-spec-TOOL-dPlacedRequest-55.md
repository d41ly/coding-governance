# TOOL-dPlacedRequest-55 — the version oracle's verdict reads its walk's own exit status

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 28 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-56 |
| [2026-10-25-build-TOOL-dPlacedRequest-55-deviation-551.md](../build/2026-10-25-build-TOOL-dPlacedRequest-55-deviation-551.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-56 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
confirmed **finding 22 at HIGH**, its item **H3**, which holds no other finding.
`TOOL-dPlacedRequest-52` S11 ends the oracle `if git log … -p "$r" -- … | grep -E …; then exit 1;
fi; exit 0`. Nothing reads `git log`'s own status and no `pipefail` is set, and the commit count
before it comes from `rev-list --count`, which reads no blobs and succeeds where the walk will not.
When the walk dies (a partial clone missing blobs offline, a bad object, a signal), `grep` matches
nothing and the oracle exits 0: it certifies "no version bump" over a walk it never read. This unit
repairs `TOOL-dPlacedRequest-52`, at order 27, so it sits at order 28: the walk's status is part of
the verdict, and a dead walk exits 2.

## 2. Scope (IN)

- **S1** — The walk answers for itself. The oracle captures the walk, `w=$(git log --no-merges
  --invert-grep --grep='^mint:' -p "$r" -- <the two paths>)`, and when git exits non-zero it prints
  `version oracle: the walk failed` and exits 2. Only then does it grep the capture: a `KIT_` line
  exits 1, none exits 0. The capture is a command substitution, so the status is git's own and no
  `PIPESTATUS` or scratch file is needed. Written into 44 §4, where unit 52 leaves the oracle, and
  into 52's §4 sketch; 52 S11 names the status check. Observed by AC1 and AC2.
- **S2** — The failure staged. 52 gains AC29: with a PATH-stub `git` that passes every call through
  to the real git except a `log` carrying `-p`, which exits 128, the oracle prints `the walk failed`
  and exits 2, never 0. 52 S11 names AC29, and 52 takes one rev bump with its §9 line naming this
  unit. Observed by AC2.

## 3. Non-goals (OUT)

- No change to how the merge is found or refused: `TOOL-dPlacedRequest-54`.
- No change to the `rev-list --count` call's guards: finding 8's item of `TOOL-dPlacedRequest-56`.
- No `set -o pipefail` across the oracle: one captured status covers the one producer the verdict
  reads, and the earlier lines already branch on their own results.
- No new bug-class record: `memory/gotchas/swallowed-delegate-reads-as-clean.md` names the class, a
  check that discards its delegate's status and reads a dead delegate as a clean population.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — S11's verdict line and §4's oracle sketch, which this unit makes read the walk's status, and §6, which gains AC29; without them there is no verdict to correct
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's oracle as unit 52 leaves it, whose verdict this unit rewrites in place
- **hands-off** `TOOL-dPlacedRequest-56` — the oracle's captured walk, before which that unit's item for finding 8 guards the count line
- **hands-off** `TOOL-dPlacedRequest-59` — AC1 and AC2, which that unit's item for finding 9 gives the fixture's base

## 4. Design

### The oracle's tail, as this unit leaves it

```bash
w=$(git log --no-merges --invert-grep --grep='^mint:' -p "$r" \
      -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh) \
  || { echo "version oracle: the walk failed"; exit 2; }
if printf '%s\n' "$w" | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='; then exit 1; fi
exit 0
```

The lines before it are unchanged by this unit. The capture holds the diff of two files over the
build's commits, megabytes at most, read once at the close.

### Evidence

- Measured 2026-10-25 on node a in a fixture under `%TEMP%` with a short name (a base, a branch commit
  `b2`, a branch commit bumping `KIT_UNATTENDED_VERSION` from 1.110 to 1.111, one default-branch
  commit, a `--no-ff` merge with the lander's subject), with a stub `git` first on `PATH` that exits
  128 on a `log` carrying `-p` and runs the real git otherwise. The §4 tail printed the header, `the
  walk failed` and exited 2; the S11 form `if git log --no-merges -p "$r" -- … | grep …` printed the
  stub's `fatal:` line and exited 0. With the real git the §4 tail printed both version lines and
  exited 1. PINNED at that date.
- The stub's directory entered `PATH` as `/c/…`: a `C:/…` entry splits at its colon under Git Bash
  and the stub is never found, which reads as a walk that did not fail.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md`: S11, §4, AC29 and its
  §9 line. `TOOL-dPlacedRequest-53` and `TOOL-dPlacedRequest-54` write this file at the same order,
  so the three passes run in sequence.
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md`: §4 and its §9 line.
  `TOOL-dPlacedRequest-54` writes this file at the same order, in the same sequence.

### Alternatives rejected

- **`set -o pipefail` and `PIPESTATUS[0]`.** It works, and it makes a reader track which stage of
  which pipe the status came from; the capture states it in one line.
- **Capture to a scratch file.** The oracle then owns a path and its cleanup for no gain over a
  variable.

## 5. Production-readiness checklist

- security — none: a read of local history.
- perf / scale — the walk's output is held in memory once; megabytes at most.
- error / empty / loading states — a dead walk exits 2, named (S1).
- observability — git's own error line reaches stderr beside the oracle's.
- risks — none beyond the oracle's own.
- testing — the probes of §6.
- migration — none: a criterion's command.
- user docs — none: criterion text.

## 6. Acceptance criteria

- **AC1** — When the oracle as 44 §4 states it runs on the §4 Evidence fixture with the real `git`,
  it prints both `KIT_UNATTENDED_VERSION` lines and exits 1.
  Red when: capturing the walk loses the bump lines.
  fixture: built by the probe under `%TEMP%`, not held in the tree.
- **AC2** — When the same oracle runs there with the stub `git` first on `PATH`, it prints `version
  oracle: the walk failed` and exits 2; the S11 pipe form under the same stub exits 0.
  Red when: a walk that died reads as a clean build.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the oracle is a criterion's command, observed once at the close.

## 8. Open questions

- **F1 — How does the verdict read the walk's status (S1)?** (a) Capture by command substitution and
  branch on it; (b) `set -o pipefail` and `PIPESTATUS[0]`; (c) capture to a scratch file. All three
  meet AC2. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the fewest moving parts, measured
  under the stub. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  22 (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edge to `TOOL-dPlacedRequest-59`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is the oracle `TOOL-dPlacedRequest-52` S11 leaves in `TOOL-dPlacedRequest-44` §4;
the stub follows the suite's PATH-stub shape (`tools/unattended/unattended.test.sh:6098`, `PATH="$stubdir:$PATH"`).
`python tools/codebase-map/reuse_lookup.py "a check whose verdict pipes a producer into grep reads
the producer's exit status"` ranked `read`, `read_text` and `check`, name stems only, none a
status-reading helper for a shell pipe: no existing seam fits, since the oracle is criterion text.
`python tools/memory-recall/query.py "a check that exits clean when the command feeding its grep
died"` returned this audit's H3, TOOL-dTieredTribunal-3, TOOL-dHonouredPark-9 and round 4's record,
none on this oracle's status; a listing of `memory/gotchas/` found
`swallowed-delegate-reads-as-clean.md`, the class this unit closes an instance of. None disagrees with
source.

Recall terms used: oracle walk exit status pipe grep producer died clean verdict swallowed delegate stub git
