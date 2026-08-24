# TOOL-dFramedEntrypoint-2 — per-slot budgets: a hard declared ceiling and an advisory high-water

**Status:** CLOSED · rev-6 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · order 4 · streams tooling · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dFramedEntrypoint-2-acceptance.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-2-acceptance.md) | journal | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md](../reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md) | diff-review | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round2.md](../reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round2.md) | diff-review | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |

<!-- /gen:spec-records -->

## 1. Goal

A closed slot set bounds what a build README may say but not how much of it, and the corpus shows the
second is where the entrypoint actually fails: the authored half runs to 347,503 bytes against 200,270
generated, with a single file carrying 32,946. This unit gives each authored slot a DECLARED byte
ceiling that fails the bar, plus an advisory high-water that never touches the exit code, copying both
halves of the shape `tools/check-template-size.sh` already ships.

## 2. Scope (IN)

- **S1** — TWO declared files, not one: `tools/memory-tree/build-readme-slot-limits.txt` carrying the
  hard ceiling per canonical slot, and `tools/memory-tree/build-readme-slot-highwater.txt` carrying the
  recorded high-water. They are split because S6's `--bump` verb WRITES the high-water, and a ceiling
  living inside the write path of the thing that must never move it is guarded only by a reviewer
  reading a diff. Both are declared data, never computed from the corpus they grade.
- **S2** — the budget check rides `slot_violations`' caller in `gen_build_index.py --check-format`,
  measured over the AUTHORED slice only: from a slot's heading line to the line before the next
  canonical heading or the first generated marker, whichever comes first.
- **S3** — a slot over its hard ceiling exits 1 and names the slot, the file, the measured bytes and
  the declared ceiling.
- **S4** — a slot over its recorded HIGH-WATER but under its ceiling prints an advisory naming the
  same four values and does NOT change the exit code.
- **S5** — the advisory must REACH a human. `run-gates.sh` prints only an ok line for a passing leg and
  echoes leg stdout only on failure, so an advisory inside a green leg reaches nobody. The advisory is
  therefore also written to the leg's persisted per-leg log and surfaced by a `--report` verb that
  prints every slot's measured bytes against both numbers.
- **S6** — a `--bump` verb that rewrites the high-water file from the measured tree, so raising one is
  a reviewable diff rather than a hand edit. It never writes the ceiling file.
- **S6b** — the ADOPTER does not inherit this repo's measured ceilings. The mechanism is named rather
  than assumed: `tools/memory-tree/adopt-memory-tree.sh` scaffolds a limits file carrying the canonical
  slot rows with NO ceiling values, the same way unit 3's S6c scaffolds the registry, and
  `tools/memory-tree/kit.toml` gains a declared hole with its discharge probe. A row present with no
  ceiling is the ANNOUNCED UNARMED state and is legal — distinct from a missing row, which stays a
  refusal — and the leg names how many slots are unarmed on every run, so an adopter's unmeasured
  tree says so rather than reporting a clean bar. Ceilings measured against this corpus and shipped
  into a tree that never measured them are either vacuous or permanently red, which is the class this
  kit already declares holes against.
- **S7** — this unit ships DECLARED PROVISIONAL ceilings, written into the limits file at this unit's
  landing with their provenance stated in the file header, taken from the researched distribution and states
  the RULE — seed from the declared population, never from the whole corpus. It does NOT perform the
  seeding: unit 3 lands with zero bound rows by its own design, so at this unit's landing the seeding
  source is empty. Unit 7 owns the one real seeding event, and this unit's green is VACUOUS until it
  lands, which AC8 states rather than implies. One fact, one owner.
- **S8** — selftest arms for every branch: over-ceiling, over-high-water-under-ceiling, under both, a
  missing limits file, a limits row naming a slot the canon does not declare, and a limits file MISSING
  a row for a canonical slot. That last refusal is declared in this spec's own readiness checklist and
  had neither an arm nor a criterion, which is the unarmed-refusal class the charter names.
- **S-EPOCH** — this unit moves `tools/memory-tree/gen_build_index.py`, which is inside the
  verdict-epoch gate's scan set, so its landing carries a `KIT_MEMORY_TREE_VERSION` bump. The carrier
  set is DERIVED, never read off the epoch gate's remedy text: bump the constant and its inline marker
  in the engine, then every carrier `git grep -l 'gov:kit memory-tree@'` returns over tracked paths
  outside `memory/builds/` and `memory/archive/`, then re-render the live copies with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The remedy string names three paths and
  the parity harness three pairs; their union is five, and there are SEVEN carriers — the two it cannot
  reach are kit SOURCES rather than dogfood copies. Following the remedy exactly reds the unguarded
  `kit version markers` leg, which is `TOOL-dSettledRoster-4` in the backlog, recorded as having cost a
  full-bar cycle twice. The rule binds per PUSH RANGE, not per commit: units landing in one push need
  one correctly-placed bump, on the LAST engine-moving commit in that range. It is stated in every
  engine-moving unit rather than once, because a rule written in one spec is a rule the other seven do
  not carry.

## 3. Non-goals (OUT)

- No PER-BULLET cap. Measured and rejected: a 400-byte per-bullet rule reds 27 of 130 bullets across
  11 READMEs, and it is dominated by the section ceiling it was proposed to backstop — the outlier it
  was written for is caught 4.6 times over by the section ceiling alone.
- No budget over GENERATED bytes. Every backfire of a character cap in this tree has been a generated
  row blowing an authored-prose cap, and the only remedy available silenced three checks on the whole
  file. The measurement is authored-slice-only by construction, not by convention.
- No change to the existing whole-file byte cap or per-line character cap in the hygiene gate. Those
  grade a different question and stay exactly as they are.
- No RATCHET-DOWN schedule. Whether ceilings tighten over time is an owner decision this unit does not
  take; it ships the mechanism that makes tightening a one-row diff.

## 4. Design

### Data model

One row per slot: the slot's canonical heading key, the hard ceiling in bytes, the recorded high-water
in bytes. A row naming a slot the canon does not declare is a refusal, not a warning — that is the
declared-population rule applied in the second direction, and it is what stops a ceiling surviving the
slot it was written for.

### Inventory

The measured slice for a slot begins at its heading line and ends at the line before the next
canonical heading; for the LAST slot it ends before the authored `roster:units` opening marker where
one is present, and before the first generated marker otherwise. Terminating unconditionally at the
generated marker would bill the roster pair's table to the parked-decisions slot, which unit 1
forbids touching. Bytes, not characters. The reason is NOT that the hygiene entry cap is a byte measure — it is declared
in CHARACTERS. What its own comment refuses to pin is the awk `length()` primitive, which counts bytes
or characters depending on the awk build and the ambient locale, so the DECLARED unit and the MEASURED
unit can differ per node. This check is written in Python, where the choice is explicit, and it picks
bytes so the verdict is node-independent by construction rather than by luck.

### Migration

The ceilings are seeded from the unit-3 population so the leg lands green over the tree it was written
against, which is how every existing cap in this repo was seeded. Seeding from the whole corpus is
what makes a budget decorative: 32 of 61 READMEs exceed the sum of the researched ceilings today.

### Alternatives rejected

**A pure advisory with no hard ceiling.** Rejected because a warning inside a green leg is invisible
here — the runner echoes leg stdout only on failure. An advisory alone would be a check nobody reads,
which this repo already treats as a check nobody runs.

**Ceilings at the measured p90 over the whole corpus.** That lands green with no registry, and it was
one of the four options the owner ruled between. It lost: p90 authored is 13,656 bytes, loose enough
to permit almost everything the owner objected to.

### Files touched (estimate)

`tools/memory-tree/build-readme-slot-limits.txt` and `tools/memory-tree/build-readme-slot-highwater.txt`
(both new, tracked, LF-pinned) · `tools/memory-tree/kit.toml` for the declared hole ·
`tools/memory-tree/gen_build_index.py` for the measurement, the two verdict tiers, `--report`,
`--bump` and the selftest arms · `tools/gate-legs.json` if `--report` earns its own invocation ·
`.gitattributes` for the new data files' LF pin, AND `tools/memory-tree/kit.toml`'s own `[[lf_pin]]`
block, which is what carries the pin to an adopter — a pin in gov's `.gitattributes` alone protects
this repo and no other · the `build-readme-surface` dossier.

## 5. Production-readiness checklist

- security — N/A. Reads tracked text, writes only the limits file under `--bump`.
- perf / scale — one additional slice measurement per graded file; negligible against the leg's
  current sub-second cost.
- a11y — N/A.
- i18n — N/A, and deliberately so: the measure is bytes precisely to avoid a locale-dependent verdict.
- error / empty / loading states — a missing limits file is a refusal naming the expected path, never
  a skip. A slot with no row is a refusal for the same reason.
- observability — `--report` prints every slot's measured bytes against both numbers, so the margin is
  readable before a breach rather than after.
- risks — the recorded hazard is a budget that reds a third of the corpus on landing. S7 removes it by
  seeding from the declared population; the residual risk is that the population grows faster than the
  ceilings, which `--report` makes visible.
- testing + left-shift gates — six selftest arms, one per branch, including the three data-shape
  refusals. The selftest leg is HELD on a bare bar, so this unit's Definition of Done names the
  `GATE_SELFTESTS=1` invocation rather than the bare one.
- migration / rollback — rollback is deleting the limits file, which by S-design is a refusal rather
  than a silent pass, so the rollback is deliberate rather than accidental.
- user docs — the limits file's own header states what it declares and what the two tiers mean.

## 6. Acceptance criteria

- **AC1** — When a slot body exceeds its declared ceiling,
  `python tools/memory-tree/gen_build_index.py --check-format` exits 1 and its message names the slot,
  the file, the measured bytes and the ceiling.
- **AC2** — When a slot body exceeds its recorded high-water but not its ceiling, `--check-format`
  exits 0 and prints an advisory naming the same four values.
- **AC3** — When the advisory fires inside a green bar, the text is present in that leg's persisted log
  under the gate-log directory, demonstrated by grepping that file after a `bash tools/run-gates/run-gates.sh` run.
- **AC4** — When `--report` runs, it prints one line per slot per graded file with measured bytes,
  high-water and ceiling.
- **AC5** — When `--bump` runs on a tree whose high-waters are stale, `git diff` shows only rows in the
  high-water file changed.
- **AC6** — When `tools/memory-tree/build-readme-slot-limits.txt` is absent, `--check-format` exits 1
  naming the expected path, rather than skipping.
- **AC7** — When the limits file carries a row for a slot the canon does not declare, `--check-format`
  exits 1 naming that row.
- **AC8** — When `bash tools/run-gates/run-gates.sh` runs at this unit's landing, the bar is green AND
  the leg states that the declared population is empty, so the green is recorded as VACUOUS. The real
  seeding observation belongs to unit 7 AC5, not here.
- **AC9** — When the limits file omits a row for a canonical slot, `--check-format` exits 1 naming the
  slot, observed RED against a staged deletion before the arm is written.
- **AC12** — When a row is present with no ceiling value, `--check-format` exits 0 and the leg's output
  names that slot as UNARMED, so the announced-unarmed state is distinguishable from a graded one.
- **AC13** — When the high-water file is absent, `--check-format` exits 0 and treats every slot as
  having no recorded high-water, because an absent ADVISORY baseline is not a refusal — only the
  absent CEILING file is. The two files are declared separately and fail differently, which is the
  whole reason rev-2 split them.
- **AC10** — When `--bump` runs, `git diff --stat` shows `build-readme-slot-limits.txt` unchanged and
  only `build-readme-slot-highwater.txt` modified.
- **AC11** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, every new arm passes;
  the bare `bash tools/run-gates/run-gates.sh` does NOT exercise them, because the selftest leg is held
  unless `GATE_SELFTESTS=1` is set, so the Definition of Done for this unit names
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 7. Gates

`build README slot contract` · `build-index selftest` · `memory hygiene` · the LF discipline check over
the new data files · `check-kit-versions.sh` (leg `kit version markers`, unguarded) ·
`check-verdict-epoch.sh` · `kit/dogfood doc parity`.

## 8. Open questions

- **F1 — do the ceilings ratchet down on a schedule, or only when an owner edits a row?** A schedule
  makes the budget shrink without anyone deciding to; a manual edit means it never shrinks. The
  measured precedent in this tree is that every cap moved manually and every movement is recorded with
  its reason. RESOLVED (agent, 2026-08-24, delegated): manual. The scheduled option satisfies no
  additional acceptance criterion in this spec and would move a declared ceiling with nobody deciding
  to, which is the shape the charter's own gate rules refuse.
- **F2 — is the advisory's persisted-log home sufficient, or should a breached high-water surface on
  the runner's own summary line?** Surfacing it on the summary needs a runner change, which widens
  this unit past one mechanism. RESOLVED (agent, 2026-08-24, delegated): persisted log plus `--report`.
  A runner advisory channel is a SECOND mechanism, and M2's one-mechanism-per-spec rule puts it in its
  own unit rather than in this one.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the owner's fork-4 ruling and the verification finding that
  a pure warning inside a green leg reaches nobody.
- rev-2 · 2026-08-24 · folded spec-audit round 1. The limits file splits in two, because `--bump`
  wrote the file the ceilings live in. The seeding event moves wholly to unit 7 and this unit ships
  declared provisional ceilings plus the rule, since unit 3 lands with an empty population and three
  specs previously gave three answers to one question. The declared missing-row refusal gains its
  arm and its criterion. The adopter copy ships unarmed with a declared hole. The last slot's
  measured slice stops at the roster pair.
- rev-3 · 2026-08-24 · folded the factual corrections from round 1's LOW tier. The
  bytes-over-characters reason is corrected: the hygiene entry cap is declared in characters, and
  what its comment refuses to pin is awk's `length()`. The kit's own LF pin block joins the files
  touched, since a pin in this repo's `.gitattributes` reaches no adopter. The provisional ceilings
  are stated as written-at-landing rather than left implicit.
- rev-4 · 2026-08-24 · folded spec-audit round 2. The kit-version carrier set becomes a derivation,
  and `kit version markers` joins the gate list.
- rev-3 · 2026-08-24 · folded spec-audit round 2. The adopter's unarmed state gains a mechanism — a
  scaffolded row with no ceiling value, legal and announced — rather than a promised outcome with no
  way to reach it. The high-water file gains its own absent-state semantics, which the rev-2 split
  created and did not define.
- rev-5 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-6 · 2026-08-24 · BUILT and CLOSED. Two declared files, the two verdict tiers, `--report`, `--bump`, the adopter strip and the kit hole. Seven arms, 95 to 102. One defect shipped and was caught by running the verb: the comment predicate ate every data row because a slot heading starts with a hash, and with an empty population nothing validated the declaration at all — so the table assertion now runs on every check rather than only while grading a bound file. Ledger: `build/2026-08-24-build-TOOL-dFramedEntrypoint-2-acceptance.md`.

## 10. Reuse audit

`tools/check-template-size.sh` is the existing seam and is copied in both halves rather than
generalised: it declares per-subject ceilings in `tools/template-size-limits.txt`, fails hard on
breach, and carries a separate high-water ratchet that never touches the exit code. A shared helper
was considered and rejected — the two subjects are graded by different gates in different languages,
and extracting a common library to serve two call sites would create a seam with a fan-in of two,
below this repo's own threshold for calling something a seam.
