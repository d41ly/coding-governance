# TOOL-dAlignedCarrier-5 — BUILD-METHOD M7 regrounds with `--status`

**Status:** CLOSED · rev-2 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 2 · closes TOOL-dDerivedDocket-72 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-build-TOOL-dAlignedCarrier-5-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-dAlignedCarrier-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-6 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-6 |
| [2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md) | diff-review | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-6 |

<!-- /gen:spec-records -->

## 1. Goal

BUILD-METHOD M7 step 1 tells a mandated run to reground with `unattended.sh --resume <slug>` and no
keepalive id. On a live run the resume matrix answers that with the `--status` block and then a
check 59 refusal, so the run's journal carries one refused resume per pass boundary
(`TOOL-dDerivedDocket-72`). This unit makes step 1 name `--status <slug>` instead: the read-only verb
that already prints the phase and witness M7's self-probe asks for, and that `TOOL-dAlignedCarrier-4`
extends with the holder-worktree and pinned-asks verdicts, so regrounding orients without a refusal
and without losing either check.

## 2. Scope (IN)

- **S1** — In `tools/memory-tree/BUILD-METHOD.template.md`, M7's numbered step 1 (line 228 at BASE)
  names `bash {{TOOL_ROOT}}unattended/unattended.sh --status <slug>` as the mandated regrounding
  command, where it named the same command with `--resume <slug>`. The change is the verb token
  alone, 8 bytes for 8, on that one line; no other line of the file moves. Observed by AC1 and AC4.
- **S2** — `memory/guides/BUILD-METHOD.md` is re-rendered from the template in the same pass by the
  memory-tree kit's own render and is never hand-edited, so the dogfood copy carries the same step 1
  with `{{TOOL_ROOT}}` resolved to `tools/`, and the render moves no other live copy. Observed by AC2
  and AC4.
- **S3** — M7's body keeps naming `playbook-followed` in backticks outside every HTML comment. The
  directive registry `DIRECTIVES_CORE` in `tools/unattended/unattended.sh` routes that handle to M7,
  and check 16's body term in `tools/unattended/check-unattended.sh` reds a cited section that stops
  naming it. Observed by AC3.
- **S4** — As the unit that closes `TOOL-dDerivedDocket-72`, this unit re-observes the two halves of
  that ask's accept clause that `TOOL-dAlignedCarrier-4` builds, and builds neither: `--status <slug>`
  reporting the holder-worktree and pinned-asks verdicts while writing nothing, and section 8 of
  `memory/guides/UNATTENDED-STOPS.md` following the new step 1. Observed by AC5 and AC6.
- **S5** — The build commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, because
  `memory/guides/BUILD-METHOD.md` is on that manifest's `watch:` list and the pre-commit ratchet
  refuses a commit that stages a watched file without moving the stamp. The commit message carries
  the `manifest-audit:` delta line. Observed by AC7.

## 3. Non-goals (OUT)

- No change to `--status`, `--resume`, the resume matrix, `tools/unattended/STOPS.template.md` or
  its render. All of it is `TOOL-dAlignedCarrier-4`'s; this unit only reads it as acceptance input.
- No clause in M7 saying what `--status` reports or what a failing verdict means. M1's one rule makes
  a rule stated both in M7 and in an M11 carrier a defect in M7, and the verdict contract lives in the
  unattended kit's own guides.
- No other M7 step and no other section of the method moves. Steps 2 to 5, the `playbook-followed`
  sentence and M1's budget line stay byte-identical.
- No kit version bump. The memory-tree kit's version moves in the build's one sweep at VERIFYING, per
  the build brief, and that sweep is what discharges the accept clause's "both kit versions move"
  half. No criterion here names a version.
- No change to the unattended Skill's Resume section, which already runs `--status <slug>` first and
  `--resume <slug> --keepalive-id <id>` after it. A resume after compaction or process death is a
  change of who drives, not a pass-boundary reground.
- No dossier edit: `memory/map/features/build-method.md` does not spell M7's regrounding command at
  BASE (`grep -n -- '--resume' memory/map/features/build-method.md` prints nothing), so there is no
  prose to refresh.

One line is shared with a sibling: the `last-audit` stamp in `memory/guides/SESSION-KICKOFF.md`,
which `TOOL-dAlignedCarrier-6` also re-stamps. This unit is ordered later, so it owns that line and
its stamp supersedes unit 6's. Beside that, it READS three files `TOOL-dAlignedCarrier-4` writes, as
acceptance inputs: `tools/unattended/unattended.sh`, `tools/unattended/STOPS.template.md` and
`memory/guides/UNATTENDED-STOPS.md`. That read is why it is ordered after that unit rather than
beside it.

### Edges

- **consumes-from** `TOOL-dAlignedCarrier-4` — the `--status <slug>` verb extended to report, read
  only, the holder-worktree verdict (check 58's question, `check_holder_worktree`) and the
  pinned-asks verdict (check 73's question, `check_asks_pinned`), and section 8 of
  `memory/guides/UNATTENDED-STOPS.md` rewritten to match the new step 1. Without it step 1 would
  reground through a verb that skips the two checks a no-id `--resume` ran before refusing, and AC5
  and AC6 stay red.
- **hands-off** external — the build's one kit-version sweep at VERIFYING, which moves the
  memory-tree kit's version for the template this unit edits. The accept clause of the ask this unit
  closes requires it, and the build brief takes every version out of every unit.

## 4. Design

### The change

M7 step 1 of the template, at BASE and after this unit:

```text
1. `git log --oneline -5` — under a mandate, `bash {{TOOL_ROOT}}unattended/unattended.sh --resume <slug>`.
1. `git log --oneline -5` — under a mandate, `bash {{TOOL_ROOT}}unattended/unattended.sh --status <slug>`.
```

The render writes the second line into `memory/guides/BUILD-METHOD.md` with `{{TOOL_ROOT}}` as
`tools/`. Nothing else in M7 is touched, so the self-probe, steps 2 to 5 and the
`playbook-followed` sentence that check 16 grades read exactly as they do at BASE.

### Why `--status` is enough for step 1

M7's self-probe asks two questions, and the second is "the phase and its witness". `verb_status`
(`tools/unattended/unattended.sh:5545`) prints one line carrying the phase, the witness, the next
unit, the parked and noted counts and the keepalive's presence, and exits 0 on a live record.
Measured at BASE `87c245b3` on node d, 2026-09-30 (PINNED, that date and node):
`bash tools/unattended/unattended.sh --status dAlignedCarrier` printed that line and the lander-mode
line, exited 0 in 4.2 s wall, and left `git status --porcelain` byte-identical.

What the no-id `--resume` ran beyond that, before refusing, is `check_asks_pinned` (called at
`tools/unattended/unattended.sh:6290`) and, on a leased record, `check_holder_worktree` (called at
`tools/unattended/unattended.sh:6394`). `TOOL-dAlignedCarrier-4` makes `--status` report both
verdicts without refusing and without writing. That is the half of the owner's ruling this unit does
not build, and it is why this unit is `order 2`.

### Render

```bash
bash tools/memory-tree/kit-dogfood-parity.test.sh --render
```

`--render` writes every live copy from its template (TEMPLATE -> LIVE, per the script's own header),
so the builder confirms afterwards that only `memory/guides/BUILD-METHOD.md` moved among the four
live copies; AC2 is that confirmation. The parity check itself is the close's `kit/dogfood doc
parity` leg, never a run inside this pass. The `--render` form answers in seconds and is on the
read-only list of `tools/unattended/gate-guard.js`, so the deferred-bar hook does not refuse it
during a unit pass.

### Inventory

This unit mints nothing: no function, flag, file, conf key or vocabulary member. No naming cell
grades it.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md` — M7 step 1, one line.
- `memory/guides/BUILD-METHOD.md` — the same line, written by the render.
- `memory/guides/SESSION-KICKOFF.md` — the `last-audit` line only (S5).

### Rollout

Adopters take the new step 1 with the memory-tree kit's next version, through the kit's ordinary
render. Nothing is flagged, because nothing new runs: the step names a verb every adopter's driver
already carries (§5, migration).

### Alternatives rejected

- **`--resume <slug> --keepalive-id <id>` in step 1.** Option (a) of the 2026-09-14 parked decision in
  `memory/builds/dDerivedDocket/RUN.md`. The holder row of the resume matrix may record and stage the
  lease and reaps orphans (STOPS section 8 and section 14), so every pass boundary would take actions
  where it should only read; a session that is not the holder would enter a take-over. The owner
  ruled `--status` instead (`TOOL-dDerivedDocket-72`).
- **Leave M7 and let the no-id `--resume` print the status block before refusing.** Option (b) of the
  same parked decision, folded then as "fully functional". It is the defect the ask names: one refused
  resume logged per pass boundary.
- **Swap the verb and add a clause on what `--status` reports.** Refused by M1's one rule, and it
  grows a file M7 re-reads whole at every boundary to say something the unattended kit's guides
  already own. The byte-neutral swap keeps `build-method size` exactly where BASE left it.

## 5. Production-readiness checklist

- security — N/A: one line of a shipped guide; no write path, input, credential or surface moves.
- perf / scale — the step runs one read-only driver call per pass boundary where the old one ran the
  same status block plus a refusal. 4.2 s wall at BASE on node d (PINNED, 2026-09-30); the cost of
  the two verdicts `TOOL-dAlignedCarrier-4` adds is that unit's to state.
- error / empty / loading states — a slug with no run-state file makes `--status` refuse with check
  10, naming the path (`verb_status`); a build with no mandate never reaches step 1's mandate clause.
- observability — the gain: a mandated run's journal stops carrying one refused resume per pass
  boundary, which is the whole ask.
- risks — step 1 naming `--status` before `TOOL-dAlignedCarrier-4` lands would drop checks 58 and 73
  from regrounding. The `order 2` header verb and the consumes-from edge sequence it, and AC5
  observes the result.
- testing — no suite moves and no arm is added. AC1 to AC6 are direct reads and one fixture run; the
  close's `kit/dogfood doc parity` leg grades the render byte for byte.
- migration — `verb_status` has shipped in the driver since its first commit, `20f80825`
  (2026-08-10), a day before M7's `--resume <slug>` first rendered at `a3833757` (2026-08-11). No
  adopter's driver therefore lacks the verb the new step names; an older driver only lacks the two
  verdicts, and prints the phase and witness step 1 needs.
- user docs — N/A: no `help/` page covers the build method. The guide is the doc, and it is the edit.

## 6. Acceptance criteria

The accept clause of `TOOL-dDerivedDocket-72` has four halves. AC1 to AC4 observe the first, which
this unit builds. AC5 and AC6 re-observe the second and third, which `TOOL-dAlignedCarrier-4` builds
and this unit consumes. The fourth, both kit versions moving, is the build's VERIFYING sweep (§3), so
the union of these criteria, that unit's own and the sweep implies the clause. Every criterion is
observed at the end of this unit's pass, before the sweep.

- **AC1** — When `grep -n -- '--status <slug>' tools/memory-tree/BUILD-METHOD.template.md` runs after
  the pass, it prints exactly one line, that line begins `1. ` and its number lies between the two
  numbers `grep -n '^## M[78] ' tools/memory-tree/BUILD-METHOD.template.md` prints; and
  `grep -c -- '--resume' tools/memory-tree/BUILD-METHOD.template.md` prints `0`.
  Red when: step 1 still spells the no-id `--resume <slug>`, or the new verb landed outside M7's step
  1.
- **AC2** — When `diff <(sed -n '/^## M7 /,/^## M8 /p' tools/memory-tree/BUILD-METHOD.template.md | sed -e 's#{{TOOL_ROOT}}#tools/#g' -e 's#{{MEMORY_ROOT}}#memory#g') <(sed -n '/^## M7 /,/^## M8 /p' memory/guides/BUILD-METHOD.md )`
  runs after the render, it prints nothing and exits 0; and
  `git status --porcelain -- memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/ANNOTATION-STYLE.md`
  prints nothing.
  Red when: `memory/guides/BUILD-METHOD.md` was not re-rendered, or was hand-edited to a different
  line, so M7 of the two files differs; or the render rewrote a sibling live copy this unit had no
  reason to move.
- **AC3** — When
  `awk '/^## M7 /{f=1;next} /^## M8 /{f=0} f && index($0, "\140playbook-followed\140")' memory/guides/BUILD-METHOD.md | wc -l`
  runs after the render, it prints `1`, the figure it prints at BASE.
  Red when: the edit or the render dropped the backticked handle from M7, so check 16's body term
  reds `playbook-followed:M7` and a run resolving that directive reads a section stating no rule
  about it.
- **AC4** — When `wc -c < memory/guides/BUILD-METHOD.md` and
  `git cat-file -s "87c245b3:memory/guides/BUILD-METHOD.md"` run after the render, they print the same
  number; `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exits 0; and
  `git diff --numstat 87c245b3 -- tools/memory-tree/BUILD-METHOD.template.md memory/guides/BUILD-METHOD.md`
  prints `1` inserted and `1` deleted for each of the two paths.
  Red when: step 1 grew a clause, or a second line of either file moved, so the file M7 re-reads
  whole at every boundary pays for text this unit had no mandate to add.
  figure: DERIVED — both byte counts are read at observation time. The reading on node d at BASE on
  2026-09-30 was 27422, recorded only as the value the check is expected to reproduce.
- **AC5** — When `bash tools/unattended/unattended.sh --status dAlignedCarrier` runs in this run's
  worktree after `TOOL-dAlignedCarrier-4` is built, it exits 0, its output carries the holder-worktree
  and pinned-asks verdicts in the spelling that unit's acceptance criteria name, and
  `git status --porcelain` prints the same bytes before and after it.
  Red when: `--status` still prints only its phase line, so step 1 would reground without the two
  checks the no-id `--resume` ran before refusing; or the verb wrote a tracked file.
  fixture: this run's own record, `memory/builds/dAlignedCarrier/RUN.md`, present in the run's
  worktree while the run is live. Before unit 4 the same command printed two lines (§4).
- **AC6** — When
  `grep -n "no-id spelling" memory/guides/UNATTENDED-STOPS.md tools/unattended/STOPS.template.md`
  runs after `TOOL-dAlignedCarrier-4` is built, it prints nothing, where at BASE it prints line 189
  of the render and its template twin.
  Red when: section 8 still says a session regrounding by the build method's no-id spelling reads the
  status block before its refusal, which after step 1 moves describes a caller that does not exist.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the staged build
  commit, it exits 0, and `git diff --cached -- memory/guides/SESSION-KICKOFF.md` shows the
  `last-audit` line and no other line moving.
  Red when: the pass staged the watched `memory/guides/BUILD-METHOD.md` without re-stamping the
  manifest, which the ratchet's check 5 refuses at the commit.

## 7. Gates

`kit/dogfood doc parity` · `kickoff-manifest ratchet` · `build-method size` · `method carriers (every pointer declared)` · `unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness`

New arm: none. This unit adds and moves no gate arm; its failing cases are the direct reads of §6.

The line names every leg whose manifest guard a §4 path trips, except those tripped only through
`tools/memory-tree/` or `tools/`, which the guards join excludes as broad guards. The
version-bound legs are the VERIFYING sweep's to green, not this unit's. All of these run once, at the
close; none runs inside this unit's pass.

## 8. Open questions

- **F1 — which command does M7 step 1 reground with under a mandate?** The no-id
  `--resume <slug>`, `--resume <slug> --keepalive-id <id>`, or `--status <slug>` extended with the two
  read-only verdicts (§4, Alternatives rejected). RESOLVED (owner, 2026-09-30): `--status <slug>`,
  extended to report the holder-worktree and pinned-asks checks read-only — the ruling recorded as
  `TOOL-dDerivedDocket-72` in `memory/DECISIONS.md`. Not re-decided here.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, authored by the build harness's spec stage from the shared
  brief `memory/builds/dAlignedCarrier/prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md`.
- rev-2 · 2026-09-30 · §2 §3 §4 §6 §7 · S5 AC7 · the M2 cross-read found the watched
  `memory/guides/BUILD-METHOD.md` owes a kickoff-manifest re-stamp this spec never named, while unit 6
  said it did. S5 and AC7 add it, the Edges name the shared `last-audit` line as this unit's, and §7
  names the ratchet leg.

## 10. Reuse audit

The seams are the driver's existing `--status` verb, `verb_status` in `tools/unattended/unattended.sh`,
which `TOOL-dAlignedCarrier-4` extends and this unit only names, and the memory-tree kit's own render
of its method template. `python tools/codebase-map/reuse_lookup.py "regrounding at a pass boundary
reads the run state without a keepalive id"` returned generic `read_*` and `run*` symbols and the
`.unattended.conf` affordance seam, and reported `.sh` unscanned, so it cannot see `verb_status` at
all; the source was read instead. The map's `build-method` dossier lists the two files this unit
edits among its path globs and says nothing about M7's command, so it needs no refresh.

The decision-record probe returned the ask and the owner's ruling (`TOOL-dDerivedDocket-72` in
`memory/builds/dDerivedDocket/BACKLOG.md` and `memory/DECISIONS.md`), section 8's no-id sentence in
`memory/guides/UNATTENDED-STOPS.md`, and the 2026-09-14 parked decision in
`memory/builds/dDerivedDocket/RUN.md`, whose options (a) and (b) are §4's first two rejected
alternatives. Where a hit and the source disagreed: the map dossier says `{{MEMORY_ROOT}}` is not a
substitution key of the render, but at BASE M7 of the template carries it and the render resolves it
to `memory`, measured by AC2's command, which prints nothing. The solution is given by the owner's
ruling, so M12's research and test obligations do not apply to this unit.

Recall terms used: `BUILD-METHOD M7 regrounding reground --resume --status keepalive check-59 lease
resume-matrix playbook-followed pass-boundary`, with the question "why does the build method's
regrounding step run the unattended driver's resume verb without a keepalive id, and what should it
run instead".
