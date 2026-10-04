# TOOL-aWardedAudit-3 — the carriers state that only the owner opts a build into the spec audit

**Status:** OPEN · rev-1 · 2026-10-05 · node a · Tier-1 · base 35438ba0 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every carrier that describes the spec-audit opt-in says who may declare it, and none tells a run to
declare one. Today the build method calls the audit "recommended" for two or more specs, the Skill
quotes the driver's recommendation line, and nothing says the key is the owner's. A decision row
records the ruling so later sessions recall it rather than re-deriving it.

## 2. Scope (IN)

- **S1** — The build method's M4, in its kit template and its rendered copy: the opt-in is the
  owner's alone, from a `slug` README on the default branch or a `SPEC_AUDIT_DEFAULT` there; a run
  never declares the key and never passes `specAudit` on its own reading. The "recommended" sentence
  goes. Observed by AC1.
- **S2** — The unattended Skill and protocol, in their kit templates and rendered copies: step 3's
  posture paragraph and the harness bullet state the owner-only rule and the refusal; the protocol
  names `spec-audit:` beside `asks:` and `may:` as a key refused under a second-anchor mode.
  Observed by AC2.
- **S3** — The conf comment in `.unattended.conf` and its kit example, and the hooks README's rule 0
  entry, say where the default is read and what the hook admits on. Observed by AC2.
- **S4** — A `memory/DECISIONS.md` row, `TOOL-aWardedAudit-4`, records the owner's ruling. Observed
  by AC3.

## 3. Non-goals (OUT)

- Any behaviour change; this unit documents `TOOL-aWardedAudit-1` and `TOOL-aWardedAudit-2`.

### Edges

none

## 6. Acceptance criteria

- **AC1** — When `grep -n 'Recommended, never' memory/guides/BUILD-METHOD.md` runs, it prints
  nothing, and the `build-method size` leg stays green.
  Red when: the method still calls the audit recommended.
- **AC2** — When the `kit/dogfood doc parity` and `unattended skill wiring` legs run, they are green,
  and `grep -rn 'recommend spec-audit' tools/unattended/SKILL.template.md` prints nothing.
  Red when: a rendered copy disagrees with its template, or the Skill still quotes the recommendation.
- **AC3** — When `python tools/memory-recall/query.py` is asked who may opt a build into the spec
  audit, `TOOL-aWardedAudit-4` is among its hits.
  Red when: the ruling exists only in this build's prose.

## 7. Gates

`build-method size` · `kit/dogfood doc parity` · `unattended skill wiring` · `method carriers (every pointer declared)` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft.

## 10. Reuse audit

No new carrier: the five above already describe the opt-in, and each is edited where it states it.
`python tools/memory-recall/query.py` returned `TOOL-aBlindedTrial-6` and `TOOL-aBlindedTrial-7`,
the rows this one narrows.

Recall terms used: spec-audit SPEC_AUDIT_DEFAULT opt-in owner self-grant second anchor published prompt mode README front matter may grant D12-j
