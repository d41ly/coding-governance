# TOOL-dUnstalledConvoy-28 — this repo sets the self-test switch somewhere govkit does not ship to every adopter

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base b164a296 · streams tooling

## 1. Goal

`TOOL-dUnstalledConvoy-26` rev-2 resolved "where does this repo set `GATE_SELFTESTS`?" with "in
`.githooks/pre-push`". govkit ships that hook VERBATIM as engine payload to every push-main adopter,
so the answer turns the switch ON for exactly the repositories the parent unit exists to spare — at
exactly the boundary it was measured for.

## 2. Scope (IN)

- **S1 — the switch is set in a file that is NOT part of any kit's shipped payload**, so an adopter
  installing the push-main kit does not inherit this repo's choice.
- **S2 — the non-membership is ASSERTED, not assumed.** A check derives every path any kit ships, the
  way govkit derives it, and refuses if the file carrying this repo's switch is among them. A file
  that becomes shipped later must red rather than silently start travelling.
- **S3 — the adopter's own way to set it is documented** where an adopter reads, distinct from this
  repo's.
- **S4 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- The switch's semantics, its name, or what reads it — `TOOL-dUnstalledConvoy-26` and `-27`.
- Changing what govkit ships. The payload is right; the mistake was putting a local choice inside it.
- A per-kit switch.

## 4. Design

The defect is a category error rather than a bug: a repo-local POLICY was written into a file whose
whole purpose is to be copied elsewhere. So the fix is a location, and the durable part is S2 — the
assertion that keeps the location honest after everyone has forgotten why it was chosen.

S2 derives the shipped set through govkit's own descriptor reading rather than by listing paths,
because a list of what a kit ships is exactly the kind of second spelling this build has been bitten
by twice.

## 5. Production-readiness checklist

- **security** — an adopter no longer inherits a policy it did not choose.
- **perf/scale** — one derivation over descriptors already loaded.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a repo with no such file simply runs with the switch off, which is
  the documented default.
- **observability** — the refusal in S2 names the file and the kit that would ship it.
- **testing/gates** — govkit's selftest, plus the full bar.
- **migration/rollback** — no state; rollback is a revert.
- **help/ docs** — S3.

## 6. Acceptance criteria

- **AC1** — this repo's bar runs self-tests without any kit-shipped file carrying the switch, observed
  by `bash tools/run-gates/run-gates.sh`.
- **AC2** — a check derives every shipped path through govkit's descriptor loader and refuses if the
  switch-carrying file is among them, observed in `tools/govkit/selftest.py`.
- **AC3** — that refusal was observed RED by moving the switch into a shipped file, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-28-1-red-first.md`.
- **AC4** — `.githooks/pre-push` carries no `GATE_SELFTESTS` assignment, observed by `grep`.
- **AC5** — the adopter-facing text says how an adopter sets it, observed in
  `tools/govkit/selftest.py`.
- **AC6** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — which file?** RESOLVED (agent, 2026-08-24): one this repo owns and no kit ships, with S2
  asserting that property rather than trusting it. Naming the file here would put the choice in two
  places; S2's derivation is the single source.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit, which found rev-2's F4
  resolution shipping this repo's policy to every push-main adopter.

## 10. Reuse audit

govkit already derives every shipped path to decide what to install; S2 asks the same derivation a
second question rather than adding a second walk.
