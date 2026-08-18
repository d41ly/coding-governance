# TOOL-aDeclaredBound-2 — SPEC10_CUTOFF joins its three sibling cutoffs in the conf

**Status:** CLOSED · rev-3 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

The hygiene engine has four date cutoffs. Three are `.memory-tree.conf` keys declared together above
the conf source; the fourth is a shell default with an environment override, in the middle of check
12. Move it to the block its siblings live in, so an adopter sets four cutoffs one way instead of
three one way and one another.

## 2. Scope (IN)

- **S1** — TWO statements, because one cannot do both jobs and the first draft asked for one. An
  UNCONDITIONAL assignment above the conf source, beside its three siblings, which is what makes
  the value env-immune — the siblings are env-immune precisely because they are assigned before the
  source and never re-read. Then, AFTER the source, a fallback that restores the shipped value when
  the conf declared the key BLANK. The literal `2026-08-04` appears once and the fallback refers to
  it rather than retyping it.
- **S1b** — the framing correction the audit forced, recorded because the README repeated it: a
  conf declaration ALREADY wins today. The conf is sourced at line 41 and the read is at line 664,
  so `.memory-tree.conf` can set this key right now. What is wrong is not that the key is
  unsettable — it is that the key is settable through TWO channels, is declared in neither the
  shipped example nor the sibling block, and reads to any maintainer as an env knob.
- **S2** — the ENV override is retired. The three siblings have never had one, the repo-wide search
  finds no caller setting it, and two channels for one value is the drift this unit exists to
  remove. Retiring it is a CONTRACT CHANGE for adopters and is called one here rather than slipped
  in as a refactor.
- **S3** — `memory/TEMPLATE-SPEC.md` and its shipped template stop describing the key as
  env-overridable and describe it as a conf declaration. That document's `SPEC10_CUTOFF` section is
  the place an author is sent to learn how §10 is phased in, and it currently teaches the retired
  channel.
- **S4** — the shipped `.memory-tree.conf.example` gains the key. Its comment already REFERS to
  `SPEC10_CUTOFF` beside `SPEC_FORMAT_CUTOFF` without declaring it, which is how an adopter learns
  the name exists and then cannot find where to set it.
- **S5** — an arm proving the conf value is read AND that the env no longer reaches it: a scratch tree declaring a cutoff that makes a
  dated fixture spec fall on the other side of the ten-section canon, observed through check 12.
- **S6** — an arm proving a blank declaration keeps a usable value rather than an empty string. The
  three siblings all treat blank as "check off"; this one cannot, because §10 is part of a canon
  selection rather than a check of its own, and an empty cutoff makes every date compare as
  after it.
- **S7** — the kit-version ordering is stated HERE, not only in the build README.
  `check-verdict-epoch.sh` is TOPOLOGICAL: the newest behaviour-bearing commit across the engine
  and its delegates must be an ancestor of, or equal to, the commit that changes
  `KIT_MEMORY_TREE_VERSION`. Units 1 and 2 both move that engine. **Unit 1 lands FIRST and carries
  no bump; unit 2 lands second and its commit carries the single bump.** Naming which is later is
  the half rev-2 left out, and the earlier unit's own commit reds that leg until the later lands.
- **S8** — one acceptance criterion observes the shipped conf example, shared in purpose with unit
  1's S10 and separately owed here because this unit adds a key to the same file.

## 3. Non-goals (OUT)

- The VALUE does not move. `2026-08-04` grandfathers exactly the specs it grandfathers today.
- Check 12's other three cutoffs are untouched.
- The nine-section and ten-section canons themselves are untouched; this unit changes where the
  selector's date comes from, not what either canon contains.


## 4. Design

### Data model

| key | shipped default | blank |
|---|---|---|
| `SPEC10_CUTOFF` | `2026-08-04` | falls back to the shipped default, NOT to "off" |

### Why blank differs from its siblings

`SPEC_FORMAT_CUTOFF` blank turns check 12 off; `STREAMS_CUTOFF` blank means never required;
`SPEC_WITNESS_CUTOFF` blank means the same. Each of those is a rule that can be absent. `SPEC10` is
not a rule — it is the boundary between two canons, and check 12 must pick one for every spec it
grades. An empty string compares as earlier than every date, so a blank declaration would silently
demand the TEN-section canon of every grandfathered spec in the tree. S6 is the arm for that, and it
is the one place this unit's behaviour is not simply "same value, new home".

### Migration

An adopter who set the env var gets a behaviour change and no warning, because the retired channel
cannot report its own retirement. This repo has no such caller. The mitigation is S3: the document
that taught the channel stops teaching it in the same release that removes it.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh` — the declaration moves to the cutoff block.
- `tools/memory-tree/check-memory-hygiene.test.sh` — S5 and S6, and its floor.
- `tools/memory-tree/.memory-tree.conf.example` — the key and its comment.
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, rendered to `memory/TEMPLATE-SPEC.md`.
- The kit-version carriers, shared with unit 1.

### Alternatives rejected

- **Keep the env override on top of the conf key.** Rejected: it is the two-answers-to-one-question
  shape with the answers in different files, and the survey that produced this build found the key
  precisely because it was the odd one out among four siblings. Adding a conf key while keeping the
  env read makes it odd in a new way.
- **Make blank mean "every spec takes the ten-section canon".** Rejected: it is the strict reading,
  but it retroactively reds landed specs in any tree that blanks the key, which is the one thing the
  cutoff mechanism exists to prevent.

## 5. Production-readiness checklist

- security — N/A. A date string reaching a string comparison in awk.
- perf / scale — N/A.
- a11y · i18n — N/A.
- error / empty / loading states — the blank case is S6 and is the unit's only behavioural subtlety.
- observability — N/A; check 12's message already names the spec and the canon it wanted.
- risks — a silent behaviour change for an adopter using the retired env channel. Named in Design,
  mitigated by S3, and not fully preventable from inside this repo.
- testing + left-shift gates — S5 and S6.
- migration / rollback — restore the env read; the conf key can stay either way.
- user docs — S3 and S4.

## 6. Acceptance criteria

- **AC1** — When a scratch tree declares `SPEC10_CUTOFF` after a fixture spec's filename date,
  `bash tools/memory-tree/check-memory-hygiene.test.sh` observes check 12 grading that spec against
  the nine-section canon; when it declares one before that date, the ten-section canon.
- **AC2** — When `SPEC10_CUTOFF=1999-01-01 bash tools/memory-tree/check-memory-hygiene.sh` runs on a
  fixture, the environment has NO effect — the retirement is observable rather than assumed.
- **AC3** — When a scratch tree declares the key blank, `bash
  tools/memory-tree/check-memory-hygiene.test.sh` observes check 12 grading a grandfathered fixture
  spec exactly as it does with the key absent.
- **AC4** — When `grep -n 'env-overridable' memory/TEMPLATE-SPEC.md` runs, it returns nothing.
- **AC5** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, the spec template and its
  render agree.
- **AC6** — When `grep -c '^SPEC10_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` runs, it
  returns 1.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash
tools/memory-tree/check-memory-hygiene.test.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
· `bash tools/memory-tree/check-verdict-epoch.sh` · `bash tools/check-kit-versions.sh` · `bash
tools/check-testsuite-counts.sh` · and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — S2 retires the env channel, and the alternative of keeping both is rejected in section 4
rather than left open, because the survey's whole finding was that two channels is the defect.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1.
- rev-3 · 2026-08-18 · folded spec-audit round 2.
- rev-3 · 2026-08-18 · BUILT and status CLOSED. The kit-version item was filed under Non-goals,
  where a builder reading section 3 as authoritative would drop it — it is now S7 inside section 2,
  and it NAMES the order rather than saying "the later of the two" and leaving the pair
  unresolved. S8 adds the example-conf observation neither unit had. S1 asked for one statement that had to be in two
  places at once: env-immunity requires an assignment ABOVE the conf source, and blank-resolves-
  forward requires a fallback BELOW it. Split. S1b records that a conf declaration already wins
  today, so the defect is two channels rather than none. Section 10's no-new-mechanism claim was
  false. S7 states the kit-version ordering.

## 10. Reuse audit

Satisfied for the set by `TOOL-aDeclaredBound-4` §10. The seam this unit extends is the cutoff
block above the conf source in `check-memory-hygiene.sh`, and S1's second statement is a SHAPE the
file does not currently contain anywhere: a post-source fallback for a blank declaration. The first
draft said the unit extends no seam and introduces no mechanism, which was wrong on the second
count — the blank-resolves-forward behaviour has to be written, and none of the three siblings has
it because for them blank legitimately means off. The reuse question worth
recording is the one it answers NO to — there is no shared cutoff-parsing helper to extract, because
each of the four cutoffs is consumed by a different awk binding and none of them parses anything.
