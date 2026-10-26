# TOOL-dPlacedRequest-29 — the lander's fence survives its own holder's write: a same-holder move re-fences and retries

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 10 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-29-deviation-291.md](../build/2026-10-25-build-TOOL-dPlacedRequest-29-deviation-291.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 51 at HIGH**, its item **H5**. `TOOL-dPlacedRequest-15` S4 classifies any move of
the lease tip after the fence read as `fenced` and tells the run to `--abort <slug> --code
claim-lost`. The resume tick runs `--beat` for a LIVE run (`tools/unattended/resume-tick.sh:305-310`),
due every quarter of `RESUME_STALE_BOUND` (`tools/unattended/unattended.sh:2275`), which this
repository sets to 5400 s (`.unattended.conf:95`), and `TOOL-dPlacedRequest-11` S6 removes the
`push-main-active` hold that kept a claim write off during a landing (`:2415-2416`). The bar runs in the
pre-push hook between the fence read and the atomic push, so a landing whose bar spans a due beat
fails its compare-and-swap and the run's own heartbeat aborts it. This unit repairs
`TOOL-dPlacedRequest-15`: a tip moved by this holder's own write at the same epoch is re-fenced and
retried, and only a risen epoch or a changed holder is `fenced`.

## 2. Scope (IN)

- **S1** — The re-fence read. `TOOL-dPlacedRequest-15` S2's `--lease fence build <slug>` takes
  `--after <tip>`: it reads the lease once, bounded, as S2 does, and prints the fence line on the new
  tip only when this session holds the lease by the `lease` mode, `<tip>` is a first-parent ancestor
  of the current tip, and the current tip's `epoch` equals `<tip>`'s. Any other reading prints
  `lease refused — epoch-fence · <tail> · <holder>` and exits 1; a foreign holder keeps its own cause
  word. Observed by AC3.
- **S2** — The classifier. When a fenced push fails, `derive_push_failure`
  (`tools/push-main.sh:262-292`) reads `unchanged`, and the lease tip has moved from the tip read, the
  lander runs S1 with `--after <tip read>`: a fence line is the new class `refenced`; a refusal is
  `TOOL-dPlacedRequest-15`'s `fenced`, unchanged. Observed by AC1 and AC2.
- **S3** — The retry. `refenced` prints `push-main: the lease moved under this holder's own write;
  re-fencing on <new tip8> (attempt <n>/<max>)`, adds one to the attempt count, and loops without
  re-preparing, since the default branch did not move; the next attempt's fence read, which
  `TOOL-dPlacedRequest-15` S3 runs once per attempt, fences on the new tip. Both landings take it, the
  `--land` loop (`tools/push-main.sh:953-1008`) and the attended loop (`:1064-1153`), and the attempts
  stay bounded by the same `max`. Observed by AC1.
- **S4** — The documentation: the lander's header comment and the verbs guide's `fence` row
  (`tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`) name
  `--after` and the `refenced` class. Observed by AC4.

## 3. Non-goals (OUT)

- No hold of the beat during a landing: the classifier covers every same-holder write, the tick's beat
  and any other, and `TOOL-dPlacedRequest-11` S6's retirement of the hold stands.
- No change to the pre-push hook: whether a retried push of an unchanged sha runs the bar again is the
  hook's green-record predicates (`.githooks/pre-push:1660-1678`), which this unit does not move.
- No change to `race`, `refused`, `unreachable` or `unfenced`: `TOOL-dPlacedRequest-15` S4.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-15` — the fence act, the fenced push and its failure table, which this unit gives a same-holder class; without them there is no fence to retry
- **consumes-from** `TOOL-dPlacedRequest-1` — the lease record's `epoch`, `fleet-tag` and `session` and the `lease` mode, which decide a same-holder move; without them a move cannot be attributed
- **hands-off** `TOOL-dPlacedRequest-43` — the re-fence's unanswered read, which that unit's item for finding 35 keeps `offline` and maps to `unreachable`

## 4. Design

### The failure table, extended

| `derive_push_failure` | Lease tip after | `--lease fence --after <tip read>` | Class |
|---|---|---|---|
| `unchanged` | moved | fence line: mine, same epoch, descends from the tip read | `refenced`: retry, no re-prepare |
| `unchanged` | moved | refused | `fenced`, as `TOOL-dPlacedRequest-15` S4 |
| `unchanged` | the tip read | not run | `unfenced`, as `TOOL-dPlacedRequest-15` S4 |

The decision is the driver's, because the record's format is the driver's; the lander reads one line,
as it reads the fence line today.

### Why the epoch and the ancestry both

A same-session take-over raises the epoch with the holder unchanged, which is a new tenure the fence
must not paper over; and a holder whose lease was taken and re-taken by itself between the reads is
at a higher epoch too. Ancestry rules out a tip rewritten off the chain the fence read.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--after` | option of `--lease fence` | none |
| `refenced` | `derive_push_failure` follow-up class | none |

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **`--beat` declines while `push-main-active` is present.** It covers the tick's beat only, not a
  Workflow child's holder write, and a marker a crash leaves behind would stop the beat for good.
- **Read the moved record in the lander.** The record's grammar is the driver's
  (`TOOL-dPlacedRequest-15` §4 "Alternatives rejected").

## 5. Production-readiness checklist

- security — the fence still refuses every foreign or later-epoch holder; the retry pushes only under
  a fresh compare-and-swap.
- perf / scale — one more fence read per same-holder move; whether the hook re-runs the bar on the
  same sha is its green-record rule, unchanged.
- error / empty / loading states — a re-fence the driver refuses is `fenced`, as today.
- observability — the `refenced` line names the new tip and the attempt.
- risks — a holder that writes faster than the hook runs exhausts `max` and exits 1 with today's
  "moving faster than the gate" line.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`; no `help/` page covers the lander.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-15`'s: `tools/push-main.test.sh`'s bare remote and stub pre-push
hook, a build lease held by the landing session.

- **AC1** — When the stub hook, on its first run only, advances the lease ref by one commit parented
  on the tip, at the same epoch and with this session's fleet tag and session, `push-main.sh --land
  --slug tFix` prints `refenced`, retries once without re-preparing, and lands: the default branch
  moves once and the lease ref holds the landing's beat parented on the hook's commit.
  Red when: the landing is classified `fenced`, the planted case being `TOOL-dPlacedRequest-15`'s
  lander.
- **AC2** — When the stub hook instead advances the lease at the epoch plus one under another
  session, the landing prints `fenced`, exits 1, and the default branch is unmoved.
  Red when: a take-over is retried as the holder's own write.
- **AC3** — When `unattended.sh --lease fence build tFix --after <old tip>` runs over a same-holder
  beat on `<old tip>`, it prints a fence line on the new tip; over an epoch-plus-one commit by the
  same session, and over a tip `<old tip>` does not precede, it exits 1 printing `epoch-fence`.
  Red when: a later tenure or an off-chain tip re-fences.
- **AC4** — When `grep -n -- '--after\|refenced' tools/unattended/VERBS.template.md tools/push-main.sh`
  runs, the verbs guide's `fence` row names `--after` and the lander's header names `refenced`.
  Red when: either is undocumented.

## 7. Gates

`push-main self-test` · `unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC1 AC2 · a holder beat and a take-over each planted inside the stub hook, staged against `TOOL-dPlacedRequest-15`'s lander, which classifies both `fenced` · the suite's assertion count raised by the arms added
New arm: tools/unattended/unattended.test.sh · covers AC3 · the `--after` reads over a same-holder beat, a later epoch and an off-chain tip, staged against the fence act without `--after` · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does the landing survive its own holder's write?** (a) Classify a same-holder,
  same-epoch move `refenced` and retry; (b) `--beat` declines while the lander's marker is present;
  (c) both. (b) covers one writer and depends on a marker a crash can strand; (c) adds (b)'s marker
  dependence for no case (a) misses. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's
  fix judged sound. grants: PLAY-dClosedLoop-3 the `--after` option of the fence act · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 51 (HIGH, item H5).
- rev-2 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seams extended are `derive_push_failure` (`tools/push-main.sh:262-292`) and the two attempt loops
(`:953-1008`, `:1064-1153`), whose `race` arm already loops on an attempt count, and
`TOOL-dPlacedRequest-15`'s fence act, which gains one option. The beat's cadence was read at
`tools/unattended/resume-tick.sh:305-310` and `tools/unattended/unattended.sh:2275`. `python
tools/codebase-map/reuse_lookup.py "classify a failed fenced landing push by the lease tip that
moved"` ranked `fail`, `classify`, `resolveLease` and `check_landed_facts_due`, name stems only; the
classifier above is the seam. `python tools/memory-recall/query.py "what happens when the lander's
fenced push fails because the lease moved"` returned scout A's row 9 and unit 15's §1 and §4; none
disagrees with source.

Recall terms used: fenced push atomic force-with-lease lease tip beat race classifier claim-lost push-main
