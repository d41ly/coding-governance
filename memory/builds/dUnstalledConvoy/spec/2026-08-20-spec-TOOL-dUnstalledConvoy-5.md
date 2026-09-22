# TOOL-dUnstalledConvoy-5 — the `--rescope` verb records an amendment, and records it as a declaration rather than a summary

**Status:** CLOSED · rev-5 · 2026-08-21 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md](../../aBoundedVerdict/reviews/2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-22 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 TOOL-aShardedFloor-4 |
| [2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md](../build/2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-11 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 |
| [2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md](../reviews/2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md) | spec-audit | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-cumulative.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-cumulative.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-lib-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-lib-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dUnstalledConvoy-4` gives a run the authority to retire, supersede and add units. An authority
with no record is indistinguishable from a run quietly doing whatever it wants. This unit adds the
verb that writes the amendment into the run-state file, in the row grammar the file already uses, so
a gate and a wrap-up can both read it.

## 2. Scope (IN)

- **S1** — `--rescope <slug> --act <act> --unit <id> [--successor <id>] --reason "<why>"` writes one
  row through the existing `park` helper with a new kind token `rescope`. No new region, no new
  parser, no new file.
- **S2** — `--act` takes a value from the closed set `retire supersede add`. A value outside it is a
  refusal naming the value and the set, never a default.
- **S3** — `--unit` must match the id shape the driver's OWN `_ids_of` helper already uses, reused
  rather than re-spelled. The memory-tree kit's `id_pattern` is deliberately NOT the seam here: it is
  a Python function in a DIFFERENT kit, and each kit is copy-installed standalone, so an adopter may
  hold this one and not that one. Verified at source — `unattended.sh` names `id_pattern` nowhere.
- **S4** — arity by act. `supersede` REQUIRES `--successor`; `add` REFUSES it; `retire` accepts it
  optionally, because a retirement may or may not have a replacement.
- **S5** — `retire` and `supersede` REFUSE a `--unit` that the build README's generated units region
  does not carry. A run cannot retire a unit its roster never held.
- **S6** — `add` on a `--unit` the region already carries is a NO-OP when a matching row already
  exists, and a REFUSAL only when none does. The guards are ORDERED and §4 states the order: the
  exact-line idempotence compare runs FIRST and returns the no-op before any region-membership test.
  Review fold: M12. The first draft made membership an unconditional refusal, which cannot coexist
  with S8 — the region is rendered from the specs that exist, so the moment the amendment is performed
  the id IS in it, and a run recording the row after authoring the spec met a permanent refusal while
  `TOOL-dUnstalledConvoy-6` demanded that row permanently. That is the wedge shape this build removes.
- **S7** — every refusal `verb_park` already makes is inherited verbatim: no run-state file, missing
  reason, a newline in any field, the field separator inside a value, the declared bypass flag in any
  field, and a terminal record.
- **S8** — idempotent by the exact-line compare `verb_park` uses, so a resumed run that re-derives the
  same amendment does not duplicate the row.
- **S9** — the verb writes the record and **changes nothing else**. It does not edit the spec, the
  roster or the build README.
- **S10** — the Skill gains a `--rescope` section and the protocol's verb list gains its row, and both
  are SCOPE rather than a Files-touched afterthought. Review fold: M4. The first draft edited two
  documents that appeared in no scope item, no criterion and no gate, so a builder could satisfy every
  criterion and ship a verb that neither document an unattended run reads ever mentions. The installed
  protocol is also one of the six read-path files, so this unit re-measures that budget from its gate
  like every other unit that writes one.

## 3. Non-goals (OUT)

- Performing the amendment. S9 is the design, not an omission — see §4.
- The gate that grades the record. That is `TOOL-dUnstalledConvoy-6`.
- Any change to `--park`. The two verbs share a helper and a grammar; they do not share a code path,
  and folding them would make one verb's refusals reachable from the other's flags.
- A `--rescope` on a build with no run-state file. That is an attended build, where the amendment is
  an ordinary spec edit and the owner is present to read it.

## 4. Design

### Data model

One row per amendment, in the file's existing grammar:

```
<timestamp> rescope · item <act> <unit-id>[ -> <successor-id>] · reason <why>
```

The kind token sits where `decision`, `waiver` and `abort` already sit, so every existing reader that
selects rows by kind keeps working and the two checks that parse the parked region line-wise need no
new shape. This is the reuse that makes the unit small.

### Why the verb records and does not act

A record derived from a change it just made is a summary, and a check comparing the two confirms the
driver rather than checking it — this repo's `second-implementation-is-not-a-second-opinion` class.
Recording separately from acting is what gives `TOOL-dUnstalledConvoy-6` two independent inputs: the
declared amendment, and the roster transition that actually happened in git.

The honest limit, which the verb's header must state: nothing forces the verb to be called BEFORE the
edit, so the record is a declaration in shape rather than in enforced ordering. What the pair buys is
the detection of an amendment made with NO record at all, which is the failure mode that matters — a
run quietly retiring a unit it found inconvenient. It does not buy detection of a truthful-looking
record attached to a different edit, and the check says so where it reports.

### Inventory of refusals

| Condition | Refusal |
|---|---|
| `--act` outside the closed set | names the value and the three members |
| `--unit` not id-shaped | names the pattern source, not a regex spelled here |
| `supersede` with no `--successor` | names the act and the missing flag |
| `add` with a `--successor` | names the act and the surplus flag |
| `retire` or `supersede` naming an id absent from the units region | names the id and the region |
| `add` naming an id already in the units region | names the id and the region |
| every `verb_park` refusal in S7 | verbatim, same messages, same exit path |

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `verb_rescope`, its flag parsing, one dispatch row |
| `tools/unattended/unattended.test.sh` | the cases in §6, plus the `ARMS_FLOORS` bump per new `fail` call site |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |
| `tools/unattended/SKILL.template.md` and its render | one section, in the shape `--park` already has |
| `memory/guides/UNATTENDED-PROTOCOL.md` and its template | one row in section 7's verb list |

### Alternatives rejected

- **A new region in the run-state file.** Rejected: the parked region's grammar already carries a
  kind token, and a second region would need its own parser, its own malformed-marker refusal and its
  own place in every reader. The kit has a recorded scar from a region whose zero-byte write was then
  certified by its own check.
- **Folding the amendment into `--park`.** Rejected: `--park` means "I refused to decide". An
  amendment is the opposite — a decision taken. Overloading one verb with both would make the
  wrap-up's open-and-parked row wrong, since it derives from parked entries.
- **Having the verb perform the status flip.** Rejected in §4. It would also make the verb a writer
  of spec files, which nothing else in this driver is.

## 5. Production-readiness checklist

- security — the verb writes only the run-state file and inherits the bypass-flag refusal in both
  fields, which is a recorded defect class where screening one field left the other free.
- perf / scale — one file append and one region scan per call.
- a11y — N/A — a shell verb with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — the seven refusals in §4's table, each naming itself.
- observability — the row IS the observability, and it reaches the wrap-up through M9's
  open-and-parked derivation.
- risks (concurrency, data-loss, rollback hazards) — append-only to one file, staged by the same
  helper every other verb uses. A resumed run cannot duplicate a row, by S8.
- testing + left-shift gates — the cases in §6. Each new `fail` message must be armed with its entire
  literal signature, and a positional in a `fail` message cannot be armed, so every interpolation is
  bound to a name and placed after the sentence.
- migration / rollback — none. Existing run-state files simply carry no `rescope` rows.
- user docs — the Skill section and the protocol verb row, which S10 puts in scope.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/unattended.sh --rescope <slug> --act retire --unit <id> --reason
  "<why>"` appends one row whose kind token is `rescope`, observed in the fixture's run-state file.
- **AC2** — The same invocation run twice appends ONE row and reports the amendment as already
  recorded, matching `--park`'s idempotence.
- **AC3** — `--act sideways` refuses, naming the value and the three legal members.
- **AC4** — `--act supersede` with no `--successor` refuses; `--act add` WITH `--successor` refuses.
- **AC5** — `--act retire --unit <id>` where the id is absent from the build README's generated units
  region refuses, naming the id and the region.
- **AC6** — `--act add --unit <id>` where the id is already in that region refuses.
- **AC7** — A `--reason` containing the declared bypass flag refuses, and so does an `--item`-side
  spelling of it, matching `verb_park`'s both-fields rule.
- **AC8** — `--rescope` on a record in a terminal phase refuses through `refuse_if_terminal`.
- **AC9** — Each new refusal is observed RED against a fixture before the unit lands, and
  `bash tools/unattended/check-unattended.sh` stays green.
- **AC10** — `--act add` for an id already in the region AND already carrying a matching row reports
  the no-op and appends nothing; the same call with no matching row refuses. Both observed in
  `tools/unattended/unattended.test.sh`. Review fold: M12.
- **AC11** — `grep` finds `--rescope` in the rendered `.claude/skills/unattended/SKILL.md` and in the
  verb list of `memory/guides/UNATTENDED-PROTOCOL.md`. Review fold: M4.
- **AC12** — `bash tools/unattended/adopt-unattended.sh --target . --check` exits 0, which is what
  actually grades the Skill pair. Review fold: M4, H13.
- **AC13** — `python tools/memory-tree/corpus_ids.py --report` shows the read path below
  `READ_PATH_CEILING` after the protocol edit, with the figure in the commit message. Review fold: M4.
- **AC14** — The verb's header STATES what it cannot buy, observed by `grep` over
  `tools/unattended/unattended.sh`. Review fold: L1.

## 7. Gates

`unattended driver selftest` · `unattended kit gate` · `unattended skill wiring` · `harness arms` ·
`memory-tree hygiene` (check 16, the read path) · the full bar at the push boundary. `ARMS_FLOORS`
moves for `tools/unattended/unattended.sh`, and that constant lives in `.memory-tree.conf`, which is
therefore in this unit's write set. Review fold: M4, M7, H13.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): do NOT refuse early. A uniform record across every phase is worth more than a distinction the method itself does not draw, and a phase-gated verb is one more refusal a resumed run can meet and cannot interpret.**

  The question this settles: should `--rescope` refuse before the phase reaches `BUILDING`? An amendment declared during
  `SPECCING` is ordinary spec authoring, which M2 already covers without a verb. Recording it anyway
  costs a row and buys a uniform history. Refusing it draws a line the method does not draw.
  **Recommendation: do not refuse.** A uniform record is worth more than a distinction the method
  itself does not make, and a phase-gated verb is one more way for a resumed run to meet a refusal
  it cannot interpret.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.
- rev-5 · 2026-08-21 · CORRECTION to rev-4's evidence. rev-4 cited a 400-assertion PASS as proof this
  unit's arms held. They had not run: the block was appended past the suite's terminal `exit` and was
  stranded, and the 400 counted the suite WITHOUT it. The refusals were exercised by hand against the
  live record at the time, so the verb was right, but the arms were not evidence of it. They run now —
  the suite executes 447 — and the assertion floor is raised from 338 to that count, because a floor
  sixty arms below the executed total is what let the stranding hide. TOOL-dUnstalledConvoy-19 carries
  the class.
- rev-4 · 2026-08-20 · built. Twelve refusal branches, each armed with its entire literal signature;
  the driver selftest passes 400 assertions and `check-arms` is clean with no floor move needed. The
  S10 carriers landed: a Skill block and a protocol verb row, both templates and both renders.
  RECORDED while building — the protocol's section 7 verb list omits `--park` and `--attest`
  entirely, so this unit appended rather than claiming a position in a sequence it does not own.
  TOOL-dUnstalledConvoy-17 carries that gap.
- rev-3 · 2026-08-20 · folded the spec audit: M12 (the guards are ORDERED, idempotence first, and S6
  becomes a no-op rather than a permanent refusal), M4 (the Skill section and the protocol verb row
  promoted into scope with four criteria and the read-path re-measurement), M7 (`.memory-tree.conf`
  named in Files touched as a build-wide shared write), H13 (the Skill pair is graded by the adopter's
  check mode, not by the kit gate's byte comparison).
- rev-2 · 2026-08-20 · S3 and §10 corrected: `id_pattern` is unreachable from this shell driver
  because it is a Python function in a separately-installed kit. The seam is the driver's own
  `_ids_of`. Caught by verifying the claim against source rather than by the spec audit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an unattended run changes its own build scope and retires
a planned unit"` returns `id_pattern(conf)` in the `row-grammar` dossier as an affordance seam, and
the `unattended` dossier. The first is REJECTED and the rejection is the finding: `id_pattern` is a
Python function in `tools/memory-tree/row_grammar.py`, and `tools/unattended/unattended.sh` is shell
in a kit that ships standalone — check 10's own header records that an adopter may hold one kit and
not the other. S3 therefore reuses the driver's `_ids_of` helper instead. S1 reuses the `park` helper
and its kind token.

Read at source before writing: `verb_park` at `tools/unattended/unattended.sh` carries six refusals
and an exact-line idempotence compare whose header records that a `grep -qF` substring match
previously reported success while writing nothing. S7 and S8 inherit that code path deliberately
rather than re-deriving it, because re-deriving it is how the substring bug would return.

`python tools/memory-recall/query.py "how does the unattended driver record a decision it took, and
why does a gate need an input the driver did not derive" --terms "park verb kind token parked region
row grammar idempotent record declaration second opinion driver gate amendment"` returns the
park-verb records and the second-opinion class. No existing seam covers the amendment itself; the row
is new and everything that carries it already ships.

Recall terms used: park verb kind token parked region row grammar idempotent record declaration
second opinion driver gate amendment.
