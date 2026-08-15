# TOOL-cBriefedPilot-5 — the BASE is pinned once, which is what the contract already claims

**Status:** BLOCKED · rev-1 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Guard the `base:` write so a re-preflight preserves the pin instead of moving it.
`memory/guides/UNATTENDED-PROTOCOL.md` §2 fact 4 says the BASE is "pinned once at run start"; the
driver rewrites it on every preflight, and a re-preflight is not an edge case but the documented
recovery command and a precondition of every `--close`.

## 2. Scope (IN)

- **S1** — `set_fact "$rel" base "$base"` at `tools/unattended/unattended.sh:852` becomes conditional
  on the record carrying no base, guarded in the same shape as the phase write eight lines below it
  at `:860`.
- **S2** — after the guard, `base` is re-read from the record, so the preflight echo at `:863`
  reports the value that is ON the file rather than the one just derived.
- **S3** — one arm: advance the anchor, reconcile it into the run's branch, commit, re-preflight, and
  assert the `base:` line is byte-identical to the first preflight's and that the echo names it.
- **S4** — the first preflight still writes the base, and the four existing arms that seed or delete
  `base:` to exercise `trusted_base` stay green unchanged.

## 3. Non-goals (OUT)

- **Changing what the authorization comparison reads.** `trusted_base` deliberately returns the
  FRESHLY DERIVED base in `TB` and treats the recorded one as evidence; `check_authorization` is
  called with the derived value at `:826` and stays that way. This unit touches the write, not the
  read.
- **Freezing the anchor triple written at `:853-855`.** §8.
- **Any leg-side change.** Leg check 9 already refuses an absent base and already tests ancestry
  rather than equality, so a pin that stops moving is a value it keeps accepting.
- **A new refusal.** This is a guard on a write. No `fail` branch, so `ARMS_FLOORS` does not move.

## 4. Design

### What a moving pin costs

The mandated lander reconciles origin BEFORE the gate, and a second `--preflight` is mandatory before
every `--close`: `--preflight` is the only writer of the run-state file's generated region — `splice`
has exactly one call site, at `:846` — and the `records-current` DoD item diffs that region against
the build README slice, which re-renders as units close. So reconcile-then-re-preflight is the normal
path of a long run, and today it moves the pin forward onto commits that were not on the anchor when
the run was authorized.

The authorization comparison survives that by construction, because it reads the derived base. What
does not survive is everything that reads the RECORD. `closing-review-recorded` (unit 8) joins a
tracked review record to the pinned BASE, and a pin that advances turns "a review that names the
value this run pinned" into "a review that names whatever the last preflight saw". Protocol §2 also
says facts 5 through 7 exist so a party outside this process can re-derive the pin without trusting a
byte the run wrote; a value that moves between preflights cannot be re-derived from anything.

### The guard

`[ -n "$(fact "$rel" base)" ] || set_fact "$rel" base "$base" || return 1`, then `base=$(fact "$rel"
base)` before the echo. The scaffold at `:519` writes no `base:` line, so the first preflight of a
fresh record always takes the write; a terminal record never reaches here, because
`refuse_if_terminal` runs at `:804`.

The echo naming the recorded value is not cosmetic: after a reconcile the derived base and the pin
are different commits, and the pin is the only one any later reader — the leg, the wrap-up, unit 8's
join — will ever see. `trusted_base` has already refused unless the recorded value is an ancestor of
the derived one, so the reported value is one the derived base dominates.

### Files touched (estimate)

`tools/unattended/unattended.sh` (`:852` and `:863`) · `tools/unattended/unattended.test.sh` (one
arm).

### Rollout

The arm has to COMMIT its fixture before the second preflight, because preflight refuses a dirty tree
and an uncommitted fixture would be reported as dirtiness instead of as the thing under test. The
suite already carries that exact scar in the arm that proves preflight does not move a phase
backwards, at `unattended.test.sh:534-537`, and this arm copies its shape. Advancing the anchor
requires a commit on `main` pushed to the fixture's bare origin and then merged into the `unit`
branch; a bare push alone does not move the merge-base, which is why the reconcile is part of the
fixture rather than a detail of it.

### Alternatives rejected

- **Refusing a second preflight whose derived base differs from the recorded one.** The derived base
  legitimately moves whenever the remote advances and the run reconciles, which is the mandated
  lander's own first act. A refusal there wedges the run on the one path it is required to take —
  the failure this kit already reproduced live on 2026-08-11 with equality, and moved off. The case
  that matters, a recorded base off the anchor's history, is already `trusted_base`'s refusal at
  `:350`.
- **Recording a pinned base and a current base as two facts.** Breaks protocol §2's seven-fact count
  for a value nothing reads.

## 5. Production-readiness checklist

- security — the recorded base is written by the run, and the protocol says so in the same breath as
  it accepts the value. Pinning it stops it moving; it does not make it trustworthy, and §9 of the
  protocol is unchanged by this unit.
- perf / scale — one extra `fact` read per preflight, which is pure bash and forks nothing.
- a11y · i18n — N/A.
- error / empty / loading states — an absent base is still written on the next preflight, and an
  absent base at `--close` is still leg check 9's refusal.
- observability — the preflight echo starts reporting the record instead of a derivation, which is
  the value every later reader uses.
- risks — a run whose anchor moved out from under it has no verb that re-pins. That is the intent;
  the exit is `--abort`, which already refuses to be silent about its reason.
- testing + left-shift gates — S3's arm, plus the four existing `trusted_base` arms as the
  no-regression control.
- migration / rollback — a live run whose record already carries a base keeps it; a fresh run is
  unchanged.
- user docs — none needed. The protocol already states the property; this makes the driver agree
  with it, which is why unit 18 owes no sentence for this unit.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs a second time after the anchor advanced and was reconciled into
  the run's branch, the `base:` line is byte-identical to the one the first preflight wrote.
- **AC2** — When the guard is removed, AC1's arm is observed RED, with the second preflight naming
  the new merge-base.
- **AC3** — When the first `--preflight` runs on a fresh record, `base:` is written exactly as today.
- **AC4** — The preflight echo names the value on the record.
- **AC5** — The four existing arms that seed `base:` with an unresolvable sha, with HEAD, with an
  ancestor, and with the line deleted are green unchanged.

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`, whose check 9 reads the pinned value) · `harness arms`.

## 8. Open questions

**Do facts 5 through 7 pin with fact 4?** The anchor ref, the anchor tip sha and the endpoint URL are
written unguarded at `:853-855`, immediately after the base. Protocol §2 describes all three as
observed "at pin time" and existing so an outside party can re-derive the pin. If the base freezes
and the triple keeps moving, the record's own evidence stops reproducing its own pin.

Measured: `anchor-ref`, `anchor-sha` and `anchor-url` appear in `tools/` at those three lines and
nowhere else, so nothing in the kit reads them back and freezing them is behaviour-neutral here.
Options: guard all four together, which is three more identical conditions and no new branch; or
leave the triple as a fresh observation each preflight and accept that the evidence dates a different
moment from the value it is evidence for. Recommendation: guard all four — evidence for a pinned
value that moves is evidence for nothing. It is left as a fork rather than taken because it widens
this unit past the one line the design pass scoped, and because protocol §2's wording is unit 18's to
touch. Resolver: owner.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the nine-agent design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds FG-7. §8's anchor-triple fork is new
  at authoring, found by reading the three lines below the one FG-7 named.

## 10. Reuse audit

- **The guarded phase write at `tools/unattended/unattended.sh:860`** — the seam this unit copies,
  byte-for-byte in shape. It exists for the same failure: preflight used to rewrite the phase
  unconditionally, so the verb a compacted run is told to re-run silently moved it backwards. This is
  that fix applied to the field beside it.
- **`fact()` and `set_fact()`** — the readers and the writer, unchanged. `fact` returns the empty
  string for an absent key, which is exactly the discriminator the guard needs.
- **`trusted_base`'s recorded-versus-derived cross-check at `:343-360`** — already the thing that
  makes preserving a recorded value safe, because a preserved base that is not an ancestor of the
  derived one is refused. This unit adds no second opinion about that.
- **The commit-before-re-preflight arm at `unattended.test.sh:534-537`** — the fixture shape S3
  copies.

`python tools/codebase-map/reuse_lookup.py "pinned base recorded once run state fact guard
idempotent"` returned no bash candidate and printed its standing caveat that the bash layer has no
symbol extractor. The seams above were found by hand in the driver.

Recall terms used: unattended pinned base preflight idempotent re-pin run state fact anchor
merge-base reconcile lander evidence.
