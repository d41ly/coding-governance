# TOOL-dRetiredFork-9 — `_`-prefixed spec subfolders, and C21's batched greps

**Status:** CLOSED · rev-3 · 2026-09-03 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-prompt-TOOL-dRetiredFork-9-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-9-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Take two independent unattended-kit fixes both adopters are holding. NicoCares carries `nc carve-out
20/20` because the kit enumerates every file under `spec/` as a spec, so a `_`-prefixed working
subfolder produces `NOT A UNIT` rows beside "every tracked spec is terminal"; its own comment files
this as an upstream ask. inCMS carries a C21 rewrite that batches two greps instead of `2N`,
measured at 132.2 s to 2.795 s with the verdict asserted identical.

## 2. Scope (IN)

- **S1** — Honour a `_`-prefixed directory at both enumeration sites in
  `tools/unattended/unattended.sh` (`spec_ids` and the `--plan` sibling). No config key: `_` is
  already this tree's marker for "not part of the set", so the rule is structural.
- **S2** — Absorb inCMS's C21B batching into `tools/unattended/check-unattended.sh`, keeping gov's
  message shapes, and record the before and after wall clock in the acceptance ledger.
- **S3** — One arm per change: a `_`-prefixed subfolder producing no `NOT A UNIT` row, and a
  verdict-equality arm proving the batched grep and the per-file loop agree on a fixture.
- **S4** — Bump `KIT_UNATTENDED_VERSION` in both files that carry it plus every shipped
  `*.template.md` marker, which `tools/check-kit-versions.sh` pairs.

## 3. Non-goals (OUT)

- Running the unattended kit's self-test suite. Its seven `*.test.sh` legs left the bar at the owner
  ruling recorded in `AGENTS.md:510`, and `GATE_SELFTESTS=1` is on-demand only. A stricter standing
  instruction — that `--selftests` is not to be run on this node at all — is carried in session
  memory and has NO in-repo carrier; treat it as UNVERIFIED and confirm with the owner before
  relying on it.
- Any other C21 arm. Only the batching is absorbed; the depth narrowing inCMS also carries is a
  corpus fact about that tree and stays with it.

## 6. Acceptance criteria

- **AC1** — When a build carries `spec/_working/notes.md`, `bash tools/unattended/unattended.sh
  --plan` prints no `NOT A UNIT` row for it, and the pre-change command printed one.
- **AC2** — When C21 runs over the gov corpus, `bash tools/unattended/check-unattended.sh` produces
  a verdict byte-identical to the pre-change run, and its measured wall clock is recorded.
- **AC3** — After the bump, `bash tools/check-kit-versions.sh` exits `0`.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers`.


## 8. Open questions

none - it takes two INDEPENDENT absorptions, each with its mechanism fixed by the
adopter tree that already runs it. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 2, finding 25. The leg rename collapsed two distinct
  names onto one in §7.
- rev-3 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.
