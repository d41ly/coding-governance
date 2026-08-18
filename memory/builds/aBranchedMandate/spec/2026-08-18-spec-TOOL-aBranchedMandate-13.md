# TOOL-aBranchedMandate-13 — build-complete says which region it could not find

**Status:** CLOSED · rev-2 · 2026-08-18 · node a · Tier-1 · base 401416fa · streams tooling · ratified 2026-08-18

## 1. Goal

`build-complete`'s first term requires a `<!-- roster:units -->` pair in the build README. A build
whose README predates the item fails it with a bare "unmet" and no indication that a marker pair is
what is missing. Name the missing region.

## 2. Scope (IN)

- **S1** — when `build-complete` is unmet BECAUSE the roster region is absent or malformed, the
  refusal names the README path and the marker pair, distinctly from the other four terms.

## 3. Non-goals (OUT)

- Relaxing the requirement. The roster region is what the item is FOR; this changes only the
  refusal's legibility.
- Scaffolding the markers into existing READMEs. That is a records migration, not a driver change,
  and doing it silently under a run is the shape protocol section 1 refuses.

## 4. Design

The five terms are ANDed in one expression, so any failure yields one undifferentiated verdict.
Split the roster-region term out and report it by name. The remaining four keep their combined form:
they are all about unit rows, and a build with rows but no region is the case that reads as a
mystery.

Measured on this build: `--close` blocked, and the marker pair was the cause, but nothing in the
output said so. Every build folder in this tree predating the item is in the same state.

## 5. Production-readiness checklist

- security — none; a refusal gains detail.
- error states — a README that is absent entirely already fails an earlier check; this term assumes
  the file and reports on its CONTENT.
- testing — S1's arm, below.
- rollback — revert; nothing persists.

## 6. Acceptance criteria

- **AC1** — When `--close` runs against a build whose README carries no roster marker pair, the
  output names that README and the marker pair.
- **AC2** — When the region is present and a unit is non-terminal, the refusal is the ordinary
  `build-complete` one and does NOT name the region.

## 7. Gates

- `bash tools/unattended/unattended.test.sh` · `python tools/memory-tree/check-arms.py`
- `bash tools/run-gates.sh`

## 8. Open questions

none.

## 9. Revision log

- rev-2 · 2026-08-18 · BUILT and CLOSED. The arm went where an arm already was: the driver
  self-test's term-1 case already deletes the roster pair from a fixture that HAS one, so it was
  extended to assert the named region rather than duplicated. My first attempt wrote a new arm
  against `readme()`, whose fixture never writes the markers — the `sed` was a no-op and the arm
  would have passed by finding nothing, in a unit about roster markers.

- rev-1 · 2026-08-18 · from this run's own blocked close, recorded in the build folder.

## 10. Reuse audit

No new mechanism: `dod_met` already returns per-item verdicts and `verb_close` already prints one
`fail 13` per unmet item. This adds a distinguishing message on one term.
