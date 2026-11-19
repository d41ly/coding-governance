# TOOL-dTrackedAtlas-18 — the schedule instrument re-pinned in every chain packet and in the chain-packet door

**Status:** INPROGRESS · rev-1 · 2026-11-19 · node d · Tier-2 · base 9e21ac76 · streams tooling · order 11 · closes TOOL-dTrackedAtlas-6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-18-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-18-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-18-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-18-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-18-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-18-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dTrackedAtlas-1` and `TOOL-dTrackedAtlas-9` edited the schedule instrument in place, so its
blob no longer matches the pin all 22 chain packets carry nor the door's
`tools/chain-packet.py#INSTRUMENT_BLOBS` entry. This unit re-pins both on the owner's word of
2026-11-19, so each packet's `--check` reads green again and the door takes its shortcuts again,
its answer still the instrument's own.

## 2. Scope (IN)

- **S1** — The packets: `packet.py --repin schedule.py` run once, setting the schedule's pin to its
  blob at HEAD in every chain build's packet and re-rendering each. Observed by AC1, AC2 and AC3.
- **S2** — The door's constant: the `"schedule"` entry of `tools/chain-packet.py#INSTRUMENT_BLOBS`
  set to the same blob, and the three comment lines above it rewritten to the reliance points §4
  "The door's reliance points, re-read" finds. Observed by AC4, AC5 and AC6.
- **S3** — Nothing else under `tools/` moves: the edit stays inside that one entry and its comment,
  the row the owner approved. Observed by AC7.

## 3. Non-goals (OUT)

- The door's parent-spec read itself: `tools/chain-packet.py#set_reads`'s rebound `git`, its
  leak-variable notice and the docstring paragraph describing it stay as they are, though §4 shows
  the read answers nothing at the new blob. Changing them is a `tools/` edit beyond the approved row
  and moves suite arms; the ask in §3 "Edges" carries it.
- `tools/chain-packet.test.sh`: no arm is added, moved or rewritten.
- The flagged bar, `chain-packet self-test` under `GATE_SELFTESTS`: ask `TOOL-dTrackedAtlas-19`
  holds it, and this run leaves the variable unset. Ask `TOOL-dTrackedAtlas-6`'s self-test half
  rides on that ask.
- Any instrument's bytes, the schedule's included, and any pin other than the schedule's.
- A `memory/DECISIONS.md` row: the owner's word sits in this build's README rules and prompt
  record.
- Reconciling the packets of `dWitnessedBar` and `dPlacedRequest` on their own branches: their
  landings do it, as §4 "Rollout" states.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-1` — the schedule edit that moved the blob, and the
  derivation `tree_state` now reads; without it there is nothing to re-pin.
- **consumes-from** `TOOL-dTrackedAtlas-9` — the second schedule edit; the blob pinned is the one
  both units leave at HEAD.
- **hands-off** external — one ask, filed by the main loop at the close in this build's
  `BACKLOG.md`: the door's parent-spec read answers nothing since `tree_state` reads the derivation,
  so a `tools/` unit deletes that read, its notice and its docstring paragraph, deletes arm CP8, which
  calls the rebound read directly and so grades a read no render takes, rewrites CP9's notice
  assertion, and restates CP4's premise, since a parent's build state now comes from its run records,
  not its spec text. Seen as §6 AC6's probe printing `0`.
- **hands-off** external — the flagged bar, ask `TOOL-dTrackedAtlas-19`, the owner's to run or
  waive.

## 4. Design

### The re-pin guard, at this branch

`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#cmd_repin` first runs
`#scan_live_run` over v2's `[chain]`: each chain build's working-tree `RUN.md` whose last `phase:`
is not terminal is a live chain run, and a `LANDING` record is terminal only when
`#read_landed_derivation` finds its close commit on the default branch the first remote advertises,
read with `git ls-remote` bounded at `60 s`. With nothing live, any caller is admitted. With a live
run, `#derive_caller` admits only an owner at a console: no `AI_AGENT` or `CLAUDECODE` in the
environment, a terminal on stdin, and `yes` typed.

Measured on 2026-11-19 at `0b42f0922`, with a read-only probe calling `scan_live_run` over the
`22` chain builds: it returned `[]` in `13.1 s`. `dDeclaredLoop`'s `RUN.md` reads `LANDED`, and
every other chain `RUN.md` here reads `LANDING` with its close commit on origin's main. So at this branch the guard admits the builder, no console
is needed, and the packets carry no `repinned inside a live chain run` line for this re-pin.

`dWitnessedBar` and `dPlacedRequest` hold live claims (`refs/gov/remote/runs/<slug>`, `status: live`,
read 2026-11-19), but on their own branches: `branch/unattended-dwitnessedbar-2ed3b3` reads
`phase: RUNNING` and `branch/unattended-dplacedrequest-42a7be` `phase: BUILDING`. The guard reads
this branch's working tree only, where both records read `LANDING`, landed. A claim is not read.

If the guard refuses, it prints `packet: refused: --repin is the owner's, ...`, exits 1 and has
written nothing, since it refuses before the first packet. The builder then edits nothing, never
sets or unsets an agent marker, never gives the verb a terminal or a piped `yes`, and parks the
unit in the run-state file with that line. The ask stays open for the owner at a console.

### The packets

The verb is the only writer of a packet's pins. Run as the instrument, from the worktree root:

```bash
"$PY" memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --repin schedule.py
```

`#resolve_instrument` matches `schedule.py` to the one instrument path ending `-schedule.py`. For each
of the `22` packets, `scan_packets` finds one file, the six other pins and any repin record are
kept, the schedule's pin moves to `git rev-parse HEAD:<schedule path>`, and the packet is
re-rendered at HEAD by `#render_text`. One stdout line per packet reads
`packet: <slug> · <schedule path> pinned 5aa5421e265b -> <new blob 12> · <packet path>`.

Measured on 2026-11-19 at `0b42f0922` (PINNED): the schedule's blob at HEAD is
`6184e5717b5909ebff84695a6d317548b6ab2ff5`; all `22` packets pin it at
`5aa5421e265b02ba4478f8860ad9a4f5fea94500`; the six other pins match their blobs at HEAD. The
builder pins whatever `git rev-parse` prints at its own HEAD, which is DERIVED, and reports it if
it differs from the measured value.

The re-render also clears what each packet had gone stale on besides the pin. Measured on
`dPlacedRequest` on 2026-11-19: `--check` exits 1 with `byte compare red`, six ask-arm findings for
`PLAY-dClosedLoop-33` to `-38`, and the schedule's pin-arm finding.

A packet that fails partway, such as one carrying no pin, raises after the earlier packets are
written. The builder restores them with `git checkout --` over the `22` packet paths and parks.

Cost: each re-render runs the instrument's own `carries.py --report` child. One `--check` of
`dPlacedRequest` took `365 s` there (PINNED, 2026-11-19), so the verb takes about two hours
(DERIVED, `22` times that), and the builder runs it in the background. The door does not shorten it,
since `tools/chain-packet.py#main` hands `--repin` to the instrument as a child.

### The door's reliance points, re-read

The door's comment beside the constant says a landing that moves an instrument re-reads its points
against the new bytes and then sets the constant. The schedule's points, against blob `6184e5717b59`:

| Point at `5aa5421e265b` | At `6184e5717b59` | Where read |
|---|---|---|
| `git(*args, check=True)` returning stdout decoded `text=True, encoding="utf-8"` | holds, the function is unchanged | `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#git` |
| `tree_state` calls `git("ls-tree", ...)` once per build and `git("show", ...)` once per listed path | no longer holds: `tree_state` calls the derivation's `derive(ref, claims=False, detail=False)` and no `git` | `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#tree_state` |

The derivation reads through its own `run_git` and through `tools/memory-tree/tree_lib.py#read_blobs_at`
(`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#run_git`,
`#read_blobs`), never through the schedule's `git`. Measured on 2026-11-19 (PINNED) with a probe
wrapping the module's `git` and calling `tree_state("HEAD", {"dDeclaredLoop": []})`: the schedule
at `5aa5421e265b` made `104` calls, the one at `6184e5717b59` made `0`, in `11.1 s`.

What that means for the door. `tools/chain-packet.py#set_reads` still rebinds `schedule.git` with
the same signature, so loading and installing raise nothing. The rebound read fills its cache only
on an `ls-tree` call and answers only a cached `show`, and a render makes neither, so every read
of a packet render goes through code the door does not touch. The door's answer is therefore the
instrument's byte for byte, with no change to the door beyond the constant. Measured on 2026-11-19:
the door's `--check dPlacedRequest`, run in-process with the constant set to the new blob in memory
only, took `18.6 s` and printed the same lines as the instrument's own run of `365 s`.

The door does not need to fall back anywhere: the one read that could no longer answer was the
parent-spec read, and it now answers nothing, so nothing reads stale bytes. The ask in §3 deletes
it.

### The edit to the door

In `tools/chain-packet.py#INSTRUMENT_BLOBS`, the `"schedule"` value becomes the blob S1 pinned, and
its three comment lines become, in substance:

```python
    # `git(*args, check=True)` returning stdout decoded `text=True, encoding="utf-8"`, which
    # `set_reads` rebinds. `tree_state` reads the chain build-state derivation and calls no `git`
    # (TOOL-dTrackedAtlas-18), so the rebound read answers no parent spec at this blob.
```

No other line of the file moves. The docstring's "the parent specs" paragraph, `read_git` and the
leak notice stay. That is the owner's approval of 2026-11-19, recorded in the build README's rules
as "unit 18's schedule pin in `tools/chain-packet.py`".

### The order the builder takes

1. Run the re-pin verb, S1, in the background, with no `git fetch` before the checks in step 3.
   The derivation measures landings on `refs/remotes/<remote>/<branch>`, so a fetch can move a
   parent's line between render and check.
2. Edit the door, S2, setting the value to the blob the verb printed.
3. Run §6's observations. Write the acceptance ledger and commit once, with the unit id in the
   subject.

Running the verb first means a guard refusal leaves nothing to undo.

### Rollout

The `22` re-rendered packets and the door land together on this build's branch. For the two live
runs:

- On their branches nothing changes until they merge the default branch. Both branches hold the
  schedule at `5aa5421e265b`, their merge-base `9e21ac760`, and both re-rendered their own packet
  there, moving its `rendered at` and `as-built view` lines and adding asks `PLAY-dClosedLoop-33`
  to `-38` (read 2026-11-19). Their own `--check` keeps reading their own tree.
- Whichever lands second meets a conflict on that build's packet, since both sides moved its
  `rendered at` line. The charter's reconcile practice and ask `PLAY-dClosedLoop-35` resolve
  generated text by taking one side and re-rendering. The pin line to keep is this unit's, since
  the merged tree holds the schedule at `6184e5717b59`, and then `packet.py --write <slug>` keeps
  the pins and re-renders. Keeping the branch's old pin leaves the pin arm red, and clearing that is
  `--repin`, which inside that run's live chain run admits only the owner at a console.
- The same holds if either live run merges the default branch before it lands. While its `RUN.md`
  reads live, the spec-tokens leg's packet join runs `--check` on its packet
  (`tools/check-spec-tokens.py#scan_live_packets`), so an old pin kept there reds that leg.
- The schedule reads both claims as `running`, through the derivation. The re-pin does not touch
  that.

What it does not check: that the merged packets are reconciled correctly at those landings; the
door's behaviour under a leak variable, which is unchanged; and suite arms CP3 to CP9 on fixture T
after `TOOL-dTrackedAtlas-1`, which are UNVERIFIED and are observed only by the flagged bar of ask
`TOOL-dTrackedAtlas-19`. One reading of CP4 depends on the derivation resolving a default branch
in the fixture clone, and CP9 depends on the derivation's `run_git` honouring `GIT_DIR` while
`read_blobs_at` strips it.

### Files touched (estimate)

`tools/chain-packet.py`
`memory/builds/dTrueNorth/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dSafePassage/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dOrderedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dDeclaredLoop/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dPlacedRequest/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dKeptSession/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dBoundRoles/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dFurnishedOrders/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dLinkedLibrary/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dMindYourWords/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dWellOiledMachine/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dRankedPlan/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dIndexedDesign/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dScopedBuild/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dShippedRelease/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dTendedCadence/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dCalibratedLens/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-18-ledger.md`

### Alternatives rejected

- Deleting the parent-spec read in this unit, with arms CP8 and CP9 rewritten and the suite's floor
  moved. Rejected: it is a `tools/` edit beyond the one row the owner approved, which a run may not
  widen, and it moves suite arms whose red-first observation needs the held flagged bar.
- Re-pinning the value and leaving the old comment. Rejected: the comment would state a reliance
  point that no longer holds, against the door's own rule beside the constant.
- Re-pinning the door alone and leaving the packets to the owner, as ask `TOOL-dTrackedAtlas-6`
  first assumed. Rejected: the guard admits any caller at this branch, so the owner's console is not
  needed, and leaving the packets keeps every `--check` red on its pin arm.
- Running `--repin` in-process with the door's reads installed, to cut its two hours to minutes.
  Rejected: `--repin` is not one of the door's shortcut modes, and no arm grades that route.

## 5. Production-readiness checklist

- security — No new write path: the re-pin verb is the existing sole writer of packet pins, and
  its guard stays deny-by-default for an unclassified caller. The builder never sets or unsets an
  agent marker and never feeds the confirmation prompt.
- perf / scale — The verb takes about two hours (DERIVED, §4). After the re-pin each door `--check`
  takes about `19 s` against `365 s` for the instrument (PINNED, 2026-11-19).
- error / empty / loading states — A guard refusal writes nothing and parks the unit. A partial
  loop is restored with `git checkout --` and parks. An unanswered remote reads a `LANDING` record
  as live, so the guard refuses, which is the same park.
- observability — The verb's one stdout line per packet. The door's stderr loses its
  `chain-packet: shortcuts off` line.
- risks — A packet conflict at the second of this build's and a live run's landings (§4 "Rollout").
  A fetch between the re-pin and the checks can move a parent line.
- testing — §6's observations. The suite runs only at the flagged bar, ask `TOOL-dTrackedAtlas-19`.
- migration — N/A — the packets are re-rendered by their own verb and one constant moves; no
  record changes shape.
- user docs — N/A — no page under `help/` names the door or the packet instrument (grep,
  2026-11-19).

## 6. Acceptance criteria

The commands run from the worktree root, with these names set. `$X` is the run's scratch folder,
and `$F` a scratch clone at `%TEMP%/ta18fx` of the build's tip before this unit.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
PACKET=memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py
SCHED=memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
NEW=$(git rev-parse HEAD:$SCHED); OLD=5aa5421e265b02ba4478f8860ad9a4f5fea94500
PACKETS=$(git ls-files -- ':(glob)memory/builds/*/prompts/*-prompt-PLAY-dClosedLoop-1-packet.md')
```

- **AC1** — When `"$PY" "$PACKET" --repin schedule.py` runs at the unit's base, it exits 0 and
  prints `22` lines opening `packet: `, each naming `$SCHED` and `pinned 5aa5421e265b ->` followed
  by the first 12 hex of `$NEW`, one per chain build, and no line opening `packet: owner repin`.
  Red when: in `$F`, a line `phase: BUILDING` appended to `memory/builds/dWitnessedBar/RUN.md` makes
  the same call, run in an agent's shell, print `packet: refused: --repin is the owner's` and exit
  1, with `git -C "$F" status --porcelain` listing that one record and no packet.
  cost: about two hours, the instrument's walk once per packet.
- **AC2** — When `grep -l` for the line `` - instrument: `$SCHED` blob `$NEW` `` runs over
  `$PACKETS`, it lists all `22`, and a `grep -l` for `$OLD` over them lists none; and
  `git diff -U0` of the base against the tip over `$PACKETS`, filtered to removed lines opening
  `- instrument:`, shows only the schedule's.
  Red when: the same two greps on the current tree list `0` and `22`.
  figure: PINNED, 2026-11-19 at `0b42f0922`.
- **AC3** — When `"$PY" tools/chain-packet.py --check <slug>` runs for each slug of `$PACKETS`, every
  run exits 0, prints `byte compare green`, `completeness 0 findings` and
  `pin arm 7 instruments, 0 findings`, and writes no stderr line opening `chain-packet:`.
  Red when: on the current tree, observed 2026-11-19 for `dPlacedRequest`: exit 1,
  `byte compare red`, six ask-arm findings, and
  `pin arm: instrument <$SCHED> moved: pinned 5aa5421e265b, HEAD holds 6184e5717b59`.
  cost: about `19 s` a run, `22` runs.
- **AC4** — When `"$PY" tools/chain-packet.py --check dPlacedRequest > "$X/door.out" 2> "$X/door.err"`
  and `"$PY" "$PACKET" --check dPlacedRequest > "$X/inst.out"` both run, both exit 0,
  `cmp "$X/door.out" "$X/inst.out"` finds them identical, and `"$X/door.err"` holds no line opening
  `chain-packet:`; and `"$PY" tools/chain-packet.py --parity dPlacedRequest` exits 0 printing
  `chain-packet: parity dPlacedRequest · identical ·` and a byte count.
  Red when: on the current tree, observed 2026-11-19, the door's stderr is
  `chain-packet: shortcuts off, running the instrument as it stands — schedule: blob 6184e5717b59, read against 5aa5421e265b`,
  so the compare matches the instrument with itself, and `--parity` exits 2 on that moved role.
  cost: the instrument's walk twice, about `365 s` each.
- **AC5** — When the probe
  `"$PY" -B -c "import importlib.util as u; s = u.spec_from_file_location('door', 'tools/chain-packet.py'); d = u.module_from_spec(s); s.loader.exec_module(d); print(d.scan_moved(d.resolve_instruments()))"`
  runs, it prints `[]`.
  Red when: on the current tree it prints
  `['schedule: blob 6184e5717b59, read against 5aa5421e265b']`, observed 2026-11-19.
- **AC6** — When the probe below runs with `$SCHED`, it prints `0`, and with `git show "$OLD"`
  written to `$X/schedule-old.py` it prints `104`; and `grep -n -B3 "\"schedule\": \"$NEW\"" tools/chain-packet.py`
  shows the comment naming `tree_state` and the derivation.
  Red when: the comment still names the two calls `tree_state` made, `git("ls-tree"` and
  `git("show"`, which the probe at `$SCHED` shows it no longer makes.
  figure: `104` is PINNED, 2026-11-19 at `0b42f0922`, from the number of `dDeclaredLoop` specs
  plus one.

  ```bash
  "$PY" -B -c "import importlib.util as u, sys; s = u.spec_from_file_location('s', sys.argv[1]); m = u.module_from_spec(s); s.loader.exec_module(m); n = []; g = m.git; m.git = lambda *a, **k: (n.append(a), g(*a, **k))[1]; m.tree_state('HEAD', {'dDeclaredLoop': []}); print(len(n))" <schedule file>
  ```

- **AC7** — When `git diff --stat` of the base against the tip runs over `tools/`, it lists
  `tools/chain-packet.py` alone, and `git diff -U0` over that file shows hunks only inside the
  `"schedule"` entry of `INSTRUMENT_BLOBS` and its three comment lines.
  Red when: a hunk touches the docstring's "the parent specs" paragraph or `set_reads`.

## 7. Gates

The close runs the plain bar once. `chain-packet self-test` is a guarded leg of the `selftests`
chunk, so the plain bar does not run it; the flagged bar of ask `TOOL-dTrackedAtlas-19` does. The
two recall-floor legs guard the re-rendered packets as records. The spec-tokens leg's packet join
runs `--check` only for a chain build whose `RUN.md` reads live in the tree, and none does here. No
suite arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

## 10. Reuse audit

The seams extended: `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#cmd_repin`,
the one verb that writes a packet's pins, run as it stands; and
`tools/chain-packet.py#INSTRUMENT_BLOBS`, whose own comment states the re-pin procedure this unit
follows. No new code is written. The precedent is the 22-packet re-pins recorded as
`PLAY-dClosedLoop-28` and `PLAY-dClosedLoop-29` in `memory/DECISIONS.md`.
`python tools/codebase-map/reuse_lookup.py "re-pin an instrument blob in every chain packet and in the packet door"`
ranked only name-stem helpers (`read_blobs_at`, `derive_unit_pin`, `derive_pin_hash`,
`read_chain_clauses`), none a writer of packet pins. The recall probe returned ask
`TOOL-dTrackedAtlas-6`, this unit's brief, `TOOL-aBatchedPacket-1` (the door), and asks
`PLAY-dClosedLoop-24`, `-25` and `-26` (the packet staleness, the re-pin's own acceptance shape, and
the guard reading an in-place landing). No hit disagreed with the source read.

Recall terms used: `python tools/memory-recall/query.py "how is the schedule instrument re-pinned in the chain packets and the chain-packet door after it moves" --terms "INSTRUMENT_BLOBS chain-packet door repin packet pin arm schedule tree_state reliance points shortcuts fallback"`
