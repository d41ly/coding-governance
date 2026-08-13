# KICK-cKeyedLaunchpad-4 — the sealed task region, and the duplication it must remove rather than ratify

**Status:** OPEN · rev-1 · 2026-08-13 · node c · Tier-2 · base f006691f · streams kickoff+tooling

## 1. Goal

Make the manifest's task contract binding. Today §A says the agent derives it and the user does not
fill it, and that sentence is prose: deleting §A entirely leaves every check green. This unit gives
the field set one home, seals the manifest's copy against it, and removes the second spelling instead
of blessing it.

## 2. Scope (IN)

- S1. The canonical task field set becomes a quoted heredoc constant in `manifest-check.sh`, the only
  kickoff-kit file guaranteed present and byte-fixed in every adopting repo.
- S2. A `--task-skeleton` verb prints that constant, following the read-only print-and-exit-0 shape
  U2 establishes for `--locations`.
- S3. A new check byte-compares the manifest's marked region against the constant. Markers are
  `<!-- kickoff:task -->` and `<!-- /kickoff:task -->`, matching the repo's dominant convention.
- S4. `SKILL.md` Step 3 stops enumerating the seven fields and invokes the verb.
- S5. `MANIFEST-TEMPLATE.md`'s §A blockquote is replaced by the sealed region, and the gov-only
  self-test byte-compares the shipped seed against the same constant.
- S6. This repo's own §A is rewritten to carry the canonical region, replacing its hand-collapsed
  one-bullet variant.
- S7. `region()` is lifted from `check-unattended.sh` with `# >>>` / `# <<<` delimiters and added to
  the inline-copy parity population, so the second spelling is gated rather than apologised for.
- S8. The manifest format goes to v1.3, and `write_manifest` in the self-test emits the sealed region.

## 3. Non-goals (OUT)

- **The §A heading, its prose paragraph and the per-field parentheticals are NOT sealed.** Those are
  the parts this repo already reworded for itself, and an adopter should be free to reword them. Only
  the field set is a contract.
- **No placeholder inside the sealed region.** The tier value is dropped from it entirely; §4 gives
  the reason.
- **No new conf.** A `.session-kickoff.conf` existing only to render one optional line would be a new
  file, a new gate leg and a new adopter step for a single string.
- **Absence of the region is not a skip.** §4 explains why that would make the seal dormant in exactly
  the population it exists for.
- No change to C1-C9.

## 4. Design

### The objection this unit had to answer first

Sealing §A as written would make the manifest a second binding spelling of the engine's own contract.
The seven field names and their qualifiers already live in `SKILL.md` Step 3, the manifest outranks
the skill on conflict, and two spellings with a precedence rule between them is the drift class this
whole build exists to close. Sealing the copy would have frozen the duplication rather than removed
it — F2's defect, reproduced one section over by the unit meant to fix F4.

So the field set gets ONE home and three readers. `manifest-check.sh` holds it as a constant, because
it is the only kickoff-kit file that is present, byte-identical and overwritten wholesale in every
adopting repo. `MANIFEST-TEMPLATE.md` cannot hold it: it is a SEED that BECOMES the manifest and is
never installed as a reference, so an adopting repo has no in-tree source to compare against. The
engine reads the constant through the verb, the manifest is byte-compared against it, and the shipped
seed is compared against it by the gov-only self-test. One carrier, and the two documents that used
to restate it now derive from it.

### Why the tier value leaves the sealed region

The template's §A field list ends with a tier line carrying a placeholder, and that placeholder is
OPTIONAL — the template's own customize note says to delete the line when the project is single-tier.
A region whose content is conditional cannot be byte-compared, and a sealed region containing a
placeholder shape would be simultaneously required by this check and banned by C1.

It also does not need to be there. The tier enumeration already has a home in §B's tier-rule section,
which is where this repo's own manifest put it. Dropping it from the sealed region is therefore a
deduplication that happens to be what makes the seal implementable — the constraint and the
improvement are the same edit.

### Absence must fail, not skip

The prior art skips silently when its source file is absent. Copying that here would make the seal
permanently dormant in precisely the population it exists for: every adopter manifest written before
this lands has no region at all. A missing or malformed marker pair is therefore a NAMED failure
carrying the remedy text, with three distinct messages — markers absent, markers malformed, region
differs — following the prior art's one-message-per-failure-mode discipline.

This reds every un-upgraded adopter manifest on the version bump. That is the same consequence the
owner accepted for the size ceiling, and it is applied here for consistency rather than re-decided;
§8 records it as such so it can be overridden rather than discovered.

### The marker discipline, and the two bugs it already paid for

`region()` in `check-unattended.sh` carries two fixes that were reproduced before they were written:
a marker line is IDENTIFIED by prefix and JUDGED by equality, because the older form let a run append
its own text to a marker line and still compare byte-equal; and the pair must be exactly one open and
one close with the close AFTER the open, because a transposed pair satisfies a count-only check and
once truncated a file.

Re-typing that awk would create a second spelling of a hard-won predicate with no parity gate, which
is the class `resolve-python.test.sh` exists to police. `tools/lib/` is gov-internal and ships
nothing, so sourcing it is not available to a copy-installed kit. The resolution is the pattern this
repo already uses for exactly this situation: carry the function inline between `# >>>` and `# <<<`
delimiters, and add it to the discovered inline-copy parity population so the copies are gated
byte-for-byte.

One weakness of the prior art is NOT inherited. Its region captures go through command substitution,
which strips trailing newlines and hides a trailing-blank-line difference. This check appends the
sentinel that `kit-dogfood-parity` already uses against that exact strip.

### Both halves of the byte-compare

Neither file is `eol=lf` pinned today. U2's move fixes the manifest half by landing it under a pinned
prefix; the template half stays unpinned, so this unit adds the pin AND normalises CR in the
comparison. The repo's own rule is that either alone leaves the file green only right after a render.

### Files touched (estimate)

| File | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | the constant, the verb, the check, the lifted `region()`, the version |
| `skills/session-kickoff/manifest-check.test.sh` | `write_manifest` emits the region, arms for three failure modes, the seed comparison |
| `skills/session-kickoff/MANIFEST-TEMPLATE.md` | §A becomes the sealed region |
| `skills/session-kickoff/SKILL.md` | Step 3 points at the verb |
| the manifest (at U2's path) | the canonical region, and the re-stamp the edit obliges |
| `.gitattributes` · `.memory-tree.conf` | the template pin; the raised arms floor |

### Alternatives rejected

- **Sealing the template's §A byte-for-byte.** Reds this repo on day one, since its §A is a five-line
  rewrite of the template's seventeen, and it ratifies the duplication above.
- **Shipping `MANIFEST-TEMPLATE.md` as an installed reference.** A second shipped copy per adopter to
  avoid one constant, and a new govkit file rule.
- **Making a missing region a skip.** Dormant exactly where it is needed.
- **Re-typing `region()`.** An ungated second spelling of a predicate that already cost two bugs.

## 5. Production-readiness checklist

- security — one file read and a string comparison.
- perf / scale — one read; cheap enough for the staged leg, like C1.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — three named failure modes, none of them a skip.
- observability — each message names the remedy, with the file path last so the literal run stays
  assertable.
- risks — the seal reds every pre-v1.3 adopter manifest; see §4 and §8.
- testing + left-shift gates — S7's parity population, plus arms per failure mode, plus S5's
  seed-versus-constant comparison, which is what stops the shipped seed drifting from the gate.
- migration / rollback — the version WARN channel tells an adopter their manifest predates the
  format; the retrofit is adding the region, which the verb prints for copy-paste.
- user docs — the `WIRE` §4 retrofit recipe gains the region step.

## 6. Acceptance criteria

- AC1. When `bash skills/session-kickoff/manifest-check.sh --task-skeleton` runs, it prints the
  canonical region including both marker lines and exits 0.
- AC2. When a manifest's sealed region matches the constant, the check passes.
- AC3. When a single character inside the sealed region is edited, the check fails naming the region
  and exits 1.
- AC4. When the sealed region is absent, the check fails with a message distinct from AC3's, and does
  NOT skip.
- AC5. When the marker pair is transposed or duplicated, the check fails with a third distinct
  message.
- AC6. When the sealed region differs from the constant only by a trailing blank line, the check still
  fails — the sentinel defeats the command-substitution strip.
- AC7. When the manifest is CRLF, a region otherwise identical to the constant passes.
- AC8. `MANIFEST-TEMPLATE.md`'s §A region is byte-identical to the constant, asserted by the
  self-test rather than by inspection.
- AC9. `grep -c` for the seven field names in `SKILL.md` returns zero — Step 3 points at the verb.
- AC10. The lifted `region()` is byte-identical to `check-unattended.sh`'s, asserted by the inline
  parity arm, and that arm refuses an empty population.
- AC11. `python tools/memory-tree/check-arms.py` reports every new branch armed with the floor raised.
- AC12. `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

- `bash skills/session-kickoff/manifest-check.sh` and `manifest-check.test.sh`.
- `bash tools/lib/resolve-python.test.sh`'s sibling inline-parity arm, extended by S7.
- `python tools/memory-tree/check-arms.py` · `bash tools/check-kit-versions.sh`.
- `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none — one fork resolved by the owner, one by consistency and flagged.

- That a binding, non-hand-authorable region should exist. RESOLVED (owner, 2026-08-13), as the
  kickoff request's fourth observation.
- Whether a missing region reds every un-upgraded adopter manifest. RESOLVED (agent, 2026-08-13) by
  consistency with the owner's hard-red decision for the size ceiling, since the alternative makes
  the seal dormant in the population it exists for. It is a NEW adopter-breaking consequence that the
  owner has not been asked about directly, so it is recorded here to be overridden rather than
  discovered.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.

## 10. Reuse audit

The mechanism is lifted, not invented. `check-unattended.sh`'s check 8 is the closest prior art — a
marker-delimited region byte-compared against the slice it copies — and its `region()` extractor
carries two reproduced-bug fixes this unit must not lose. `kit-dogfood-parity.test.sh` supplies the
trailing-newline sentinel that the prior art lacks. `resolve-python.test.sh` supplies the pattern for
gating an inline copy of a shared predicate across files that cannot source a common library, plus
the non-empty-population assertion that keeps such a parity arm from judging nothing.

A marker census over the tracked tree decided the naming: the `<!-- ns:name -->` and `<!-- /ns:name -->`
form has 47 and 42 instances against 2 for the `BEGIN GENERATED` outlier, so the sealed region follows
the dominant convention rather than minting a third.

`reuse_lookup.py "compare a copied region against the source it was copied from"` returns the
unattended kit's seam and the `gen:build-index` renderer. The latter is deliberately NOT extended: it
re-derives its region from data and splices it, whereas this region is a fixed constant with no data
to derive from, and bending a renderer into a comparator would give the constant two homes again.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
