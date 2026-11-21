# TOOL-dPlacedRequest-97 — the lease fence knows an id-less run's own claim by its keepalive

**Status:** CLOSED · rev-2 · 2026-11-20 · node d · Tier-2 · base 2b4cc0bd · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dPlacedRequest-97-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-97-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 TOOL-dPlacedRequest-100 |
| [2026-11-21-build-TOOL-dPlacedRequest-97-deviation-732.md](../build/2026-11-21-build-TOOL-dPlacedRequest-97-deviation-732.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-97-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-97-closing-review-spec-brief.md) | research | — |
| [2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 2
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`),
confirmed item **H1** at HIGH, finding id 7, and its exit promoted it to this unit. Under
`RUN_CLAIMS=on` in a harness that exposes no session id, `--preflight` writes the run's build lease
with `session: absent` and the run's keepalive. At landing the lander asks `--lease fence build
<slug>`, whose lease column compares sessions only and is handed no keepalive, so the run's own lease
reads `foreign` and the fence refuses it `live-holder`: every such landing pushes nothing. The stops
guide and the run-claim exemption say the lease is `mine` through its keepalive. This unit builds that
stated fallback for the fence, and gates the class.

## 2. Scope (IN)

- **S1** — H1, closed by the record's first fix, which the skeptic judged SOUND: build the stated
  mechanism. `write_fence_beat` in `tools/unattended/unattended.sh` hands the lease column the slug's
  run-state file as `check_claim_writable`'s sixth argument, the slot the run columns already read.
  In the `lease` mode, with this harness's session or the record's absent, the record is `mine` when
  its fleet tag is this node's, its `keepalive` is present, is not `absent`, and equals that file's
  `keepalive` fact. The `--lease` verbs hand no run-state file, so a `--lease` write, recording
  `keepalive: absent`, still identifies nobody. The column's header comment says the fence is the one
  caller handing a keepalive. The left-shift the record names lands with it: a permanent arm in the
  unattended kit's suite planting an id-less run claim and fencing it, with its mismatched-keepalive
  twin. Observed by AC1.

## 3. Non-goals (OUT)

- Not the record's second option, amending the stops guide and the run-claim specs to say an id-less
  run cannot land fenced: the stated identity is kept and built.
- No change to the `--lease` verbs' own identity: two id-less sessions of one node still read each
  other's `--lease` write `foreign`, as `TOOL-dPlacedRequest-32` S3 states.
- No change to the run columns' keepalive rows, which already read the run-state file.
- No change to the lander: `push-main.sh` reads the fence line as it does today.

### Edges

- **consumes-from** external — the fence verb and the lease column this build's fenced-push and
  absent-session units built and CLOSED; this unit adds one identity row to the landed code, and those
  specs stay frozen

## 4. Design

### The column's `mine` test in the `lease` mode

```
mode = lease, rel = the run-state file the caller handed, or empty
  c_node = ka  and  c_sess = sid  and  sid present (not empty, not absent)        -> mine   (as today)
  rel given  and  (sid absent  or  c_sess absent)
    and c_node = ka  and  c_ka present, not absent
    and c_ka = fact(rel, keepalive)                                               -> mine   (new)
  me present and c_sess = me                                                      -> same   (as today)
  else                                                                            -> foreign-<verdict>
```

`write_fence_beat` reads the run-state file by `runmd_of "$slug"` and passes it as the sixth
argument; a slug with no run-state file passes the path anyway, and `fact` on a missing file answers
nothing, so the new row cannot match and the fence refuses as today. Handing the file in also lets the
`mine` row compute its write-due fields, which the `lease` mode never reads, so no other row moves.

Cited at the base: the `lease` mode's `mine` and `same` rows are
`tools/unattended/unattended.sh@0e8038fd:2845` and the following line, inside
`tools/unattended/unattended.sh#check_claim_writable`, whose header at
`tools/unattended/unattended.sh@0e8038fd:2781` states the keepalive fallback and that the column is
handed none; the fence's call with `sid=${CLAUDE_CODE_SESSION_ID:-absent}` is
`tools/unattended/unattended.sh#write_fence_beat`, its session line at
`tools/unattended/unattended.sh@0e8038fd:4397`; the run claim recording `session: absent` with the
run's keepalive is `tools/unattended/unattended.sh#write_claim`; the run-state path is
`tools/unattended/unattended.sh#runmd_of` and the reader `tools/unattended/unattended.sh#fact`; the
lander's reading of the refusal is `tools/push-main.sh#read_fence_line`.

### The arm

In the unattended kit's suite, over a scratch clone with a bare origin and `RUN_CLAIMS=on`: a build
lease of this node's fleet tag with `session: absent` and `keepalive: K`, and the slug's run-state
file holding `keepalive: K` under its run facts. With `CLAUDE_CODE_SESSION_ID` unset, `--lease fence
build <slug>` prints a `fence — <ref> <tip> <beat>` line and exits 0. The twin writes `keepalive: K2`
into the run-state file and asserts `lease refused — live-holder`, exit 1. A third row guards the
non-goal that the `--lease` verbs gain no identity, and it must reach the column to do so: an
id-less `--lease acquire` is stopped by `run_lease_verb`'s session gate, which prints `lease not
written — no session` and exits 2 before `check_claim_writable` runs, so it would pass whatever the new
row does. The row therefore runs `CLAUDE_CODE_SESSION_ID=s2 --lease acquire build <slug>`, a present
session that is not the record's, over the same `session: absent`, `keepalive: K` record of this
node's tag, with the run-state file still holding `keepalive: K`. The `--lease` verbs hand no
run-state file, so the new row's `c_sess` absent branch is live and cannot match, and the row asserts
`lease refused — live-holder`, exit 1. The class rule the record states, an identity fallback a spec states owes an arm that
removes the primary identity and asserts the fallback answers, is what this arm is.

The unattended kit's own suites are waived for this build's landing (README rule 8): the arm is written
and its clean reading is owed with PLAY-dClosedLoop-14, and AC1 observes the change by a direct probe.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the `mine` row, the fence's call and the column's header comment
- `tools/unattended/unattended.test.sh`: the arm and its twins
- the unattended kit's version carrier, moved once by the kit-epoch rule

### Alternatives rejected

- **Hand the keepalive as a new positional.** The sixth argument already carries the run-state file to
  the run columns, and a second spelling of where the keepalive lives is one fact in two places.
- **Amend the statements instead.** The record offers it; it leaves every id-less unattended landing
  refused, the outcome the run-claim exemption was written to prevent.

## 5. Production-readiness checklist

- security — the fence now trusts a keepalive equal to the slug's run-state fact on this node, the same
  identity the run columns already trust; a second id-less session on the node landing the same slug
  under the same run-state file is read as the run, as the run columns read it today.
- perf / scale — one `fact` read per fence.
- error / empty / loading states — no run-state file, or a keepalive fact that is empty or `absent`:
  the new row cannot match and the fence refuses as today.
- observability — the fence line or the refusal line, both unchanged in shape.
- risks — a run-state file copied between slugs would carry a foreign keepalive; the fleet tag must
  still match, which bounds it to this node.
- testing — AC1's probe and the arm in §7.
- migration — none.
- user docs — none: `memory/guides/UNATTENDED-STOPS.md` already states the keepalive fallback, and
  `help/loop.md` names no lease column.

## 6. Acceptance criteria

- **AC1** — When a scratch clone with a bare origin and `RUN_CLAIMS=on` holds a build lease for `tKa`
  of this node's fleet tag with `session: absent` and `keepalive: K`, its run-state file holding
  `keepalive: K`, and `env -u CLAUDE_CODE_SESSION_ID bash tools/unattended/unattended.sh --lease fence
  build tKa` runs, it exits 0 printing one `fence — refs/gov/leases/tKa/build` line naming the tip and a
  beat; and with the run-state file's fact changed to `keepalive: K2` the same command exits 1 printing
  `lease refused — live-holder`.
  Red when: the `lease` mode never compares a keepalive; the driver at 2b4cc0bd4 is that break, and
  there the first command exits 1 printing `lease refused — live-holder`, its RED-first reading.
  fixture: the scratch clone, origin and run-state file, built by the probe; the tree holds none.
  permission: the suite that carries the arm is waived for this landing by README rule 8, so this probe
  observes the driver directly.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the id-less run claim fenced, its mismatched-keepalive twin and an acquire by a present session that is not the record's, staged against the lease column at 2b4cc0bd4 that compares no keepalive · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted from the closing diff review round 2, item H1 (HIGH,
  finding id 7), by its exit's disposition.
- rev-2 · 2026-11-20 · §4 · §7 · folded 2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit finding
  id 7 (M6): the arm's third row runs under a present session that is not the record's, so it passes
  `run_lease_verb`'s session gate and reaches the column, and asserts `live-holder`, exit 1.

## 10. Reuse audit

The seam extended is `tools/unattended/unattended.sh#check_claim_writable`'s sixth argument, the
run-state file the run columns already read their keepalive through, now handed by
`tools/unattended/unattended.sh#write_fence_beat` too; no new argument and no new reader.
`python tools/codebase-map/reuse_lookup.py "keepalive identity of a run claim"` ranked `run` and
`run_git`, name stems only, no seam for this row. The recall query below returned the round-2
record's H1 and `TOOL-dPlacedRequest-43`'s ledger rows on the take-over keepalive; none disagrees with
the source read above. The record cites the column's header at lines 2779 to 2783, and the source
agrees at blob 0e8038fd.

Recall terms used: write_fence_beat check_claim_writable lease mode mine keepalive session absent run claim fence live-holder runmd_of
