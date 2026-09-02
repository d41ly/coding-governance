# TOOL-dRetiredFork-17 — the authoring rule, and the gate that turns the ratchet into a ban

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 9 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Every other unit drains the fork class. This one makes it impossible to refill. gov's carried-prefix
ratchet is shrink-only, which slows the class without closing it: a new literal can still enter, it
just has to be paid for elsewhere. After the sweeps land, the remaining population is small enough
to convert the ratchet into a BAN with a declared, shrink-only exception list, and to state the
authoring rule that the ban enforces.

## 2. Scope (IN)

- **S1** — The authoring rule, written once: a kit file names nothing outside itself by literal. Its
  own kit dir and tool root are DERIVED at run time and an empty derivation is a REFUSAL. A sibling
  kit, or anything a non-program document must SAY, is a token the render channel fills, and an
  unresolved token is a refusal rather than an emitted brace. A replicated policy value is extracted
  or rendered from the one file that owns it, never retyped.
- **S2** — The rule lands in `tools/hooks/README.md` and `AGENTS.md`, NOT the charter template.
  Measured 2026-09-02: `coding-governance-agents.template.md` is 48867 of 49152 bytes with 285 free
  and already WARN past its recorded high-water, so there is no room and adding one would price the
  rule against the ceiling rather than against its value.
- **S3** — Convert the CARRIED-PREFIX arm of `tools/check-install-prefix.sh` — the shrink-only
  ratchet keyed on `tools/install-prefix-carried.txt` and written by `--write-ratchet` — into a ban
  over the drained population, with exceptions in a tracked, shrink-only list carrying a reason per
  row. **Not arm 1**, which rev-1 named: arm 1 is ALREADY a ban, declared in the script's own
  header at `:4-6` as "assert; exit 1 on an unwaived hit" against `tools/install-prefix-waivers.txt`,
  so converting it is a no-op that would leave the 656 recorded occurrences untouched.
  `TOOL-dRetiredFork-13` §3 already spells this correctly; the two specs disagreed and this was the
  side that was wrong. Arm 1's existing waiver registry is kept as-is.
- **S4** — Fix the two OPEN defects the ban would otherwise inherit. `TOOL-aScouredKit-20`: both
  arms bind a kit-DIRECTORY segment and an extension from a fixed set, so a literal naming a LOOSE
  file directly under `tools/` is invisible — which is why five wave-2 hardcoded-prefix findings were
  green on this leg. `TOOL-dTieredTribunal-27`: `--write-ratchet` does not reach a fixed point in one
  pass, because the ratchet counts `tools/<kit>/` literals per file and the ratchet file is itself a
  list of such paths, so writing it moves its own row and the next `--check` reds.
- **S5** — The candidate predicate is run over the real tree BEFORE wiring, printing hits AND
  near-misses, per the build-level rule and `AGENTS.md` §7.
- **S6** — The failing case is observed: stage a new literal, confirm RED, unstage. A gate never seen
  to fail is an assertion about nothing.
- **S7** — The leg carries a declared wall-clock ceiling and a row in
  `memory/project/testsuite-count-waivers.txt` if its suite does not print an executed assertion
  count, because `tools/check-testsuite-counts.sh` derives its population from `tools/gate-legs.json`
  and a new named suite without one reds the bar.

## 3. Non-goals (OUT)

- **A foreign-prefix install leg on the bar.** It collides head-on with the owner ruling at
  `AGENTS.md:510` that a kit's self-tests are not on the bar, and 40 of 87 legs already carry
  `subject = "kit"` and are held unless `GATE_SELFTESTS=1`, which is on-demand only. The
  foreign-prefix run is valuable and belongs on demand, not on the merge bar.
- Widening the ratchet's population to include tests. Measured and unnecessary: arm 2 has no test
  exclusion — its own source says so — and 259 of its 656 occurrences are already test rows. Only
  arm 1 excludes them.
- Banning the `.claude/hooks/` probe rung `TOOL-dRetiredFork-10` keeps. That is a fork in that unit's
  §8 and this gate must not pre-empt it.

## 4. Design

### Migration

The ban lands LAST, at order 9, because a ban over an undrained population is either permanently red
or immediately full of exceptions — and an exception list seeded at the size of the problem is a
ratchet with a worse name. Its population is whatever survives units 10 through 13.

### Alternatives rejected

Keeping the ratchet and lowering it aggressively. It cannot close the class: shrink-only permits a
new literal as long as an old one leaves, so the population converges without the class ever
becoming impossible. That distinction is the whole unit.

## 5. Production-readiness checklist

- security — N/A. A text predicate over tracked files.
- perf / scale — one pass over the shipped surface; the ceiling in S7 is what makes the cost a
  verdict rather than an annoyance.
- a11y — N/A.
- i18n — the predicate reads bytes, and a text-mode read rewrites lone CRs, so read with
  `newline=""` on both sides where the implementation is Python.
- error / empty / loading states — an EMPTY population REFUSES. A ban whose population collapsed
  reports the same zero as a clean tree, which is the vacuous-selector class this repo has recorded
  and which `DEPL-dCarriedReceipt-13`'s review already caught in this exact file.
- observability — the run prints the population size, the ban hits and the live exception count, so
  a growing exception list is visible without reading it.
- risks — a ban is a hard stop for every contributor, and a false positive blocks work repo-wide.
  Mitigated by S5's pre-wiring run over the real tree and by the exception list existing from day one
  rather than being added under pressure.
- testing + left-shift gates — S6's observed RED, plus the existing `check-install-prefix.test.sh`.
- migration / rollback — reverting to ratchet mode is a flag in the same script.
- user docs — S2's two carriers, plus the script's own header, which must state what it does NOT
  check.

## 6. Acceptance criteria

- **AC0** — The authoring rule is WRITTEN, which rev-1 scoped in S1 and S2 and observed nowhere:
  `tools/hooks/README.md` carries the four clauses in full, `AGENTS.md` carries a pointer and not a
  copy — F1's ratified pick — and `bash tools/check-template-size.sh` exits `0` with
  `coding-governance-agents.template.md` byte-unchanged. Without this the ban can land green while
  enforcing a rule no document states.

- **AC1** — When a new root-prefix literal is staged in a shipped file, `bash
  tools/check-install-prefix.sh` exits non-zero naming the file and line; the RED is observed before
  the ban is wired.
- **AC2** — When that literal carries a row in the exception list with a reason, the command exits
  `0` and prints the live exception count.
- **AC3** — When an exception row names a path the tree no longer tracks, the command exits non-zero. Observed via `bash tools/check-install-prefix.sh`.
- **AC4** — When the population is empty, the command REFUSES rather than passing. Observed via `bash tools/check-install-prefix.sh`.
- **AC5** — When a literal names a LOOSE file directly under `tools/`, the command catches it;
  `TOOL-aScouredKit-20` records that today it does not.
- **AC6** — When `--write-ratchet` runs twice in succession, the second run is a no-op and the
  following `--check` exits `0`; `TOOL-dTieredTribunal-27` records that today it reds.
- **AC7** — The candidate predicate's hits and near-misses over gov's tree are recorded before
  wiring, and every near-miss is dispositioned. Printed by `bash tools/check-install-prefix.sh --list`.
- **AC8** — `bash tools/check-testsuite-counts.sh` exits `0` and the leg declares a wall-clock
  ceiling in `tools/gate-legs.json`.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `testsuite counts (every bar self-test prints one)` · `template size <=48KiB`.

## 8. Open questions

- **F1 — does the rule land in `AGENTS.md` at all, or only in the kit README?** `AGENTS.md` is this
  repo's own charter and is not size-gated the way the template is, but a rule stated in two places
  is one fact twice — the failure mode `TOOL-dUnstalledConvoy-16` records, where a correction landed
  in one carrier of three and the refuted sentence shipped to every adopter. Recommendation: the
  kit README owns the rule; `AGENTS.md` carries a pointer, not a copy.
- **F2 — is the exception list seeded from the post-sweep population, or from zero?** Seeding from
  the population makes the ban green on day one and hides whatever the sweeps missed. Seeding from
  zero makes it red until every survivor is dispositioned. Recommendation: zero, and let the red be
  the work — but this is an owner turn, because it blocks the branch until it is finished.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. The 285-byte template headroom was measured by running
  `bash tools/check-template-size.sh`, and the two inherited defects were found by a recall query
  rather than assumed absent.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H6. rev-1's central mechanism named arm 1, which is already a
  ban, so the conversion was a no-op over the arm carrying none of the occurrences units 10-13
  drain — and it contradicted `TOOL-dRetiredFork-13` §3, which spelled it correctly.
- rev-3 · 2026-09-02 · folded spec-audit round 2, finding 10. Half the unit's title — the authoring rule — was
  scoped in S1 and S2 and observed by no criterion, so the ban could land with the rule unwritten;
  AC0 observes both carriers. F1 is ratified with the rest of this build's forks, and S2 now agrees
  with it: the kit README owns the rule and the charter points.

## 10. Reuse audit

The seam is `tools/check-install-prefix.sh` itself, which already owns this predicate, its waiver
registry and its ratchet file — `reuse_lookup.py` reports the `testsuite-counts` affordance seam
covering `install` and `prefix`, and the shrink-only registry shape is the corpus's standing pattern
across six files under `memory/project/` and `tools/`. Nothing new is built; one arm changes mode and
two recorded defects in it are repaired first.

Recall terms used: `install-prefix`, `carried`, `ratchet`, `shrink-only`, `waiver`, `ban`,
`vacuous-selector`, `population`, `near-miss`, `staged RED`, `ceiling`, `testsuite-counts`, `charter`.
