# TOOL-dFramedEntrypoint-11 — the build method's declared budget rises to 350 lines

**Status:** SPECCED · rev-1 · 2026-08-25 · node d · Tier-1 · base 60ba1d60 · order 1 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` declares its own budget as ≤24 KB and ≤310 lines and has been over
the line half since before `dFramedEntrypoint` touched it. The owner ruled the budget rises to 350.
This unit moves the declared figure and records what the ruling does not do.

## 2. Scope (IN)

- **S1** — the budget sentence in `tools/memory-tree/BUILD-METHOD.template.md` declares ≤350 lines,
  edited in the TEMPLATE first with `memory/guides/BUILD-METHOD.md` re-rendered from it, because the
  parity harness renders live from template and editing the pair together inverts that direction.
- **S2** — the raise carries its reason inline, in the same sentence that carries the two previous
  movements: it is an owner call, dated, and it is a raise rather than a trim.
- **S3** — the sentence states plainly that NO GATE enforces the pair, which is why the file sat two
  lines over unnoticed, and that whether one is added is a separate unruled question.
- **S4** — the byte half of the budget is UNCHANGED at ≤24 KB. Only the line figure moved, and the
  file measures well inside the byte cap.

## 3. Non-goals (OUT)

- No gate for the pair. The owner ruled the raise and was told explicitly that it fixes the breach
  and not the blindness; adding a leg is a different decision nobody has taken.
- No trimming of method prose. The raise is the ruling; trimming would spend another build's content
  to make room the owner already granted.
- No change to the byte cap, and no change to M1's argument for having a budget at all.

## 4. Design

### Data model

None. One declared figure in one sentence.

### Migration

The template is edited and the live copy re-rendered by
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Adopters take the new figure on their
next kit update; nothing in an adopter's tree reds in the meantime, because no gate reads the pair.

### Alternatives rejected

**Trimming to 310.** Offered to the owner and declined. It would have spent prose belonging to other
builds to stay under a figure the owner was willing to move.

**Adding the gate in the same unit.** Offered as the recommendation and declined. Bundling a check
the owner did not ask for into a unit they did ask for is how a ruling grows a tail.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` (re-rendered) ·
`tools/memory-tree/check-memory-hygiene.sh` and the three template markers for the kit version.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No mechanism ships.
- observability — none, and that is the point of S3: the pair remains unobserved, said out loud.
- risks — the read-path budget. `memory/guides/BUILD-METHOD.md` is a capped member and this unit
  changes one sentence; the delta is small but must be measured, not assumed.
- testing + left-shift gates — none new. The parity harness already asserts template and live agree.
- migration / rollback — one figure, revertible.
- user docs — the sentence is the doc.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/BUILD-METHOD.md` is read at HEAD, its M1 budget sentence declares
  ≤350 lines and ≤24 KB, and names the raise as an owner call dated 2026-08-25.
- **AC2** — When `wc -l memory/guides/BUILD-METHOD.md` runs, the count is at or under 350 and the
  file is under 24576 bytes.
- **AC3** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, template and live agree.
- **AC4** — `memory/guides/BUILD-METHOD.md` M1 — its budget sentence states that no gate enforces
  the pair and that adding one is unruled.
- **AC5** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both
  margins are recorded and `bash tools/memory-tree/check-memory-hygiene.sh` is green including
  check 16.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `check-kit-versions.sh` · `check-verdict-epoch.sh` ·
`method carriers`.

## 8. Open questions

- **F1 — does the pair get a gate?** The owner was asked and ruled only the raise, so this unit does
  not add one. RESOLVED (owner, 2026-08-25): raise only; the gate is a separate question and stays
  unruled rather than being decided by omission here.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s second park.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `build method budget lines bytes owner call raise trim
governance carrier veto gate enforcement declared pair`. The seam is
`tools/memory-tree/BUILD-METHOD.template.md`'s own M1 sentence, which already carries two prior
movements with their reasons and is the only place the figure is stated — `check-method-carriers.sh`
asserts which files point AT the method, never what its budget is. No existing gate reads the pair,
which is the finding rather than a gap to fill here.
