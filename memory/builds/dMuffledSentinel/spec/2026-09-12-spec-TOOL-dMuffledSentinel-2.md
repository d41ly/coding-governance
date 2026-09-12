# TOOL-dMuffledSentinel-2 — the pass-order and trace waiver registries take a declared path

**Status:** INPROGRESS · rev-1 · 2026-09-12 · node d · Tier-1 · base 24f8c712 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-12-build-TOOL-dMuffledSentinel-2-1-pass-order-probe.sh](../build/2026-09-12-build-TOOL-dMuffledSentinel-2-1-pass-order-probe.sh) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Both waiver registries are hard-coded under `<MEMORY_ROOT>/project/`: `tools/unattended/check-pass-order.sh`
reads `pass-order-waiver.txt` there, and `tools/drift-audit/drift_report.py` reads `trace-waiver.txt`.
inCMS retired that directory and its hygiene gate refuses one, so a true finding on either leg has
no waiver an inCMS unit can write. Let each registry's path be declared, with today's path as the
default.

## 2. Scope (IN)

- **S1** `check-pass-order.sh` imports `PASS_ORDER_WAIVER` from `.unattended.conf` through its
  existing allow-list. Blank keeps `<MEMORY_ROOT>/project/pass-order-waiver.txt`. Observed by AC1
  and AC2.
- **S2** A DECLARED `PASS_ORDER_WAIVER` naming a file not tracked at HEAD refuses with exit 2 and
  names the key, since a mistyped registry would otherwise waive nothing in silence. The default path
  keeps today's rule that an absent file is an empty set. Observed by AC3.
- **S3** `drift_report.py` reads `TRACE_WAIVER` from the project layer by `getattr`, the way
  `TRACE_CUTOFF` and `TRACE_GLOBS` arrive. Blank keeps `<MEMORY_ROOT>/project/trace-waiver.txt`.
  Observed by AC4.
- **S4** A declared `TRACE_WAIVER` that is absent, absolute, or climbs out of the tree becomes a
  finding row in its signal, never an empty waiver set. Observed by AC5.
- **S5** The keys are documented beside their siblings: `tools/unattended/.unattended.conf.example`,
  `tools/drift-audit/drift_signals.template.py` and the drift-audit README's layout table.
  NOT OBSERVED by a criterion here: that is prose, and no criterion grades prose.

## 3. Non-goals (OUT)

- Moving this repo's own registries. Both defaults are unchanged and `memory/project/` stays.
- A general registry-path mechanism for every kit. Two keys for the two registries an adopter hit.
- The inCMS half, which points both keys at `scripts/` after its next pull.
- Running the unattended kit's self-test suites, which carry a standing owner instruction not to be
  run. S1 and S2 are observed by a probe that drives the real leg over a throwaway clone instead.

### Edges

none

## 4. Design

Each key rides the conf surface its engine already has. The pass-order leg imports `.unattended.conf`
through a declared allow-list, so the key joins that list. The drift engine reads the project layer
with `getattr` and a fallback, so the key arrives the way `TRACE_CUTOFF` does. Neither engine gains a
second reader.

The two engines read their registries from different places, and that difference is kept: pass-order
from the graded commit, drift from the working tree. Only the path moves.

An explicit declaration must resolve. The default path may be absent, meaning no waivers, because
that is how an adopter with nothing to waive starts. A declared path may not, because the only
reason to declare one is to use it, and an unresolved one looks exactly like having nothing waived.

## 6. Acceptance criteria

- **AC1** — When `.unattended.conf` sets `PASS_ORDER_WAIVER` to a relocated registry tracked at HEAD,
  every unit it lists is waived, proved by the probe over a throwaway clone of this tree.
  Red when: the key is missing from the allow-list and the relocated rows waive nothing.
- **AC2** — With the key blank, `tools/unattended/check-pass-order.sh` still waives the same units
  from the default registry, in the same probe.
  Red when: the default path moved.
- **AC3** — A declared `PASS_ORDER_WAIVER` naming an untracked file exits 2 with a line naming the key.
  Red when: the leg reads an absent declared registry as an empty waiver set.
- **AC4** — When the project layer sets `TRACE_WAIVER` to a relocated registry, its row waives a
  closed untraceable spec, proved by an arm in `tools/drift-audit/selftest.py`.
  Red when: the engine keeps reading the hard-coded path.
- **AC5** — A declared `TRACE_WAIVER` that is absent reds the signal with a row naming it, proved by
  an arm in the same suite.
  Red when: an absent declared registry reads as an empty waiver set.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `pass-order history` · `memory hygiene`
`kit/dogfood doc parity` · `unattended kit gate`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-12 · §2 S1 S2 S3 S4 S5 · opened, and committed before any code this time.
