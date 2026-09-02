# DEPL-dRetiredFork-6 — `govkit contribute`, the route by which an adopter's fix becomes gov's

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 8 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

This build absorbs nine defects the adopters found and held privately, one at a time, by hand,
because there is no route. Without one the class returns immediately: the next adopter fix is held
the same way, re-merged on every release, and gov keeps shipping the defect to everyone else. Twelve
of the 44 classified rows are an adopter holding a fix gov needs. `contribute` is the mechanism that
makes the other units STAY true rather than being a one-time cleanup.

## 2. Scope (IN)

- **S1** — `govkit contribute --target <path>` — read-only, like every other measuring verb —
  emitting for each row whose bytes gov does not have a PATCH against gov's own vintage, plus the
  row's declared reason and its receipt evidence.
- **S2** — The four-class rule that decides what qualifies, applied by the verb and stated in its
  output rather than left to a reader:
  1. **gov defect** — the adopter's bytes fix a bug in gov's own behaviour. Qualifies outright.
  2. **gov gap** — the adopter added a capability gov lacks and that gov's own corpus could use.
     Qualifies as a proposal, never as an automatic take.
  3. **project fact** — the change encodes something true only of that tree. Does not qualify;
     belongs in a declaration or an extension point.
  4. **layout carriage** — a repath. Does not qualify as a contribution; it is a gov literal and
     `TOOL-dRetiredFork-17` bans the class.
- **S3** — Classification is PROPOSED by the verb and CONFIRMED by a person. A verb that decides
  class 1 versus class 3 on its own is deciding whether a project fact belongs in gov's product, and
  nothing in the receipt carries that.
- **S4** — Output is a patch set in ONE format, replacing the two incompatible hand-written
  registers this build had to read: NicoCares' numbered comments and inCMS's `kits.json` divergence
  rows.
- **S5** — A liveness assertion: a target whose census maps zero rows REFUSES, rather than reporting
  that the adopter has nothing to contribute.
- **S6** — The verb never writes to gov and never writes to the target. It emits; a person lands.

## 3. Non-goals (OUT)

- Automatic upstreaming. gov's merge bar, review protocol and id discipline all apply to an absorbed
  fix exactly as to any other change, and a verb that lands code into gov from a foreign tree is a
  write surface `AGENTS.md` §9 would have to price. It emits patches; that is the whole product.
- Deciding class 2 admissions. Whether gov WANTS a capability an adopter built is an owner turn.
- Replacing the adopters' own registers. They keep whatever they keep; `contribute` gives them one
  shared output format so the next census does not have to read two.

## 4. Design

### Data model

One record per candidate: the target path, the gov source, the gov vintage the patch is against, the
proposed class, the reason from the target's own register where one exists, and the patch. Forward
slashes throughout, and the body written to a file with a `{path, summary}` return rather than
serialized inline — the structured-output discipline `AGENTS.md` §8 states, applied to a verb whose
output is large by construction.

### Rollout

Run it against both adopters as its own acceptance evidence. The nine absorptions in this build's
order-1 units were found by hand; `contribute` must independently propose at least those nine, or it
does not work. That is a genuine falsification test rather than a demonstration.

### Alternatives rejected

A `[[contribution]]` block in the target's `deploy.toml`. It asks the adopter to declare what they
are contributing, which is the same act as filing an issue and has the same failure mode: it did not
happen for any of the nine. The verb must DERIVE candidates from bytes, because that is the only
input that exists without anyone remembering to write one.

## 5. Production-readiness checklist

- security — read-only against a foreign tree; emits patches into gov's scratch, never applies them.
  A patch is untrusted content until a person reads it, and the output says so.
- perf / scale — one diff per candidate row against one gov blob; bounded by the receipt's size.
- a11y — N/A.
- i18n — patches are bytes; emit them without transcoding, and read with `newline=""` so a lone CR
  survives the round trip.
- error / empty / loading states — S5. Zero mapped rows REFUSES.
- observability — every candidate is printed with its proposed class and the evidence for it, so a
  misclassification is visible before anyone acts on it.
- risks — a class-3 project fact proposed as a class-1 gov defect, absorbed, and shipped to every
  adopter as gov's behaviour. This is the failure that matters and S3 is the whole mitigation:
  proposal, never decision.
- testing + left-shift gates — the nine-absorption falsification run, plus arms for each class.
- migration / rollback — a new read-only verb; nothing to roll back.
- user docs — `WIRE-INTO-PROJECT.md` gains the contribution route, verified by `python
  tools/govkit/check_runbook_parity.py` exiting `0` rather than by a leg, since no leg runs it;
  and the four-class rule lands in
  the deployer's own contract rather than in prose here.

## 6. Acceptance criteria

- **AC1** — When run against `C:/projects/nicocares/main`, `python tools/govkit/govkit.py contribute
  --target <path>` independently proposes the FOUR NicoCares absorptions — `TOOL-dRetiredFork-1`
  (`nc carve-out 5/20`), `-2` (`nc 16/20` and `17/20`), `-3` (`nc 9/20`) and the `nc 20/20` half of
  `-9` — each classed 1 or 2. rev-1 said six, which was the inCMS count.
- **AC2** — When run against `C:/projects/incms/main`, it proposes the SIX inCMS-sourced units —
  `TOOL-dRetiredFork-4`, `-5`, `-6`, `-7`, `-8` and the C21 half of `-9` — and classes that
  adopter's repath rows as class 4 rather than as contributions. rev-1 said three, and named
  "seventeen" against the README's "fourteen": those count different populations — seventeen is
  inCMS's repath ROWS, fourteen is path forks across BOTH adopters — so this criterion names
  neither figure and the report derives them.
- **AC3** — When a row encodes a project fact, the verb proposes class 3 and emits no patch. Observed via `python tools/govkit/govkit.py contribute --target <path>`.
- **AC4** — When the census maps zero rows, the verb REFUSES. Observed via `python tools/govkit/govkit.py contribute --target <path>`.
- **AC5** — The verb writes nothing to gov and nothing to the target, verified by comparing both
  trees' `git status` before and after.
- **AC6** — Emitted patches apply cleanly against the gov vintage each names. Checked with `git apply --check` against the named vintage.
- **AC7** — `python tools/govkit/selftest.py` and `selfcheck` exit `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join`.

## 8. Open questions

- **F1 — does `contribute` need `DEPL-dRetiredFork-7`'s census, or its own?** They compute the same
  join. Recommendation: the census is the shared implementation and `contribute` consumes it, which
  is why this unit is sequenced after it rather than beside it.
- **F2 — what does it do with a row gov has ALREADY absorbed?** NicoCares' `nc carve-out 15/20` is
  exactly that: gov took the hook-side env scrub and the row is now stale. Recommendation: report it
  as ALREADY ABSORBED with the gov commit that took it, because that is the row the adopter can
  delete today, and it is the cheapest output the verb produces.
- **F3 — is the four-class rule the deployer's, or the playbook's?** It decides what belongs in a
  product, which sounds like governance. But it is applied by a verb and must be machine-readable.
  Recommendation: the deployer owns it, and the playbook points.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. The twelve-of-44 figure and the nine hand-found absorptions
  come from this build's classification pass and are the falsification set in AC1 and AC2.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings H2 and M4. H2: the per-adopter falsification counts were
  swapped — four NicoCares and six inCMS, not six and three — so a CORRECT verb would have redded
  AC1; both criteria now name unit ids rather than counts. M4: two derived figures counting
  different populations were compared as if they were one.
- rev-3 · 2026-09-02 · folded spec-audit round 2, finding 23. The runbook claim had no leg behind it once
  `runbook parity` proved not to be a row in `tools/gate-legs.json`; §5 names the direct
  invocation now, matching `TOOL-dRetiredFork-16` AC4.

## 10. Reuse audit

The seam is `DEPL-dRetiredFork-7`'s census plus govkit's existing `derive_carried` family, which
already computes the carried transform needed to tell a repath from a real change — `reuse_lookup.py`
reports `derive_carried`, `derive_carry_rung` and `derive_carried_by_rung` as that family, and class
4 is exactly the set they already identify. No diffing machinery is written; `git diff` against a
named blob is the whole implementation.

Recall terms used: `contribute`, `absorb`, `upstream`, `adopter`, `divergence`, `patch`, `class`,
`gov defect`, `project fact`, `carriage`, `census`, `derive_carried`, `receipt`, `vintage`.
