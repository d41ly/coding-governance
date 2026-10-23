# TOOL-dGroundRules-48 — the help page's install-section count observed with its path whole, and paired with the break that empties it

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-48-deviation-36.md](../build/2026-10-23-build-TOOL-dGroundRules-48-deviation-36.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 2 at HIGH**, which shares item **H2** with ids 11
(`TOOL-dGroundRules-49`) and 22 (`TOOL-dGroundRules-50`). Id 2 is H2 seen from coherence:
`TOOL-dGroundRules-41`'s `INSTALL_LINES` runs `awk` over a bare `policy.md`, which does not open from
the repository root, while that unit's S1 to S3 name the page at `help/policy.md`; so AC4, the
restatement of `TOOL-dGroundRules-34` AC36 that S3 promised whole, prints 0 on a correct build. This
unit is id 2's promotion. It changes no code: it is the observation `TOOL-dGroundRules-41` S3 owes,
made at this unit's close with the page path whole, and paired with the staged break that must turn
it to zero, so the count is shown able to fail. It repairs `TOOL-dGroundRules-41`, which sits at
order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The count, whole. `INSTALL_LINES_WHOLE` (§5) counts the lines holding `mirror deferred`
  inside the `## Install` section of `help/policy.md`, and is the command through which
  `TOOL-dGroundRules-41` AC4 and `TOOL-dGroundRules-34` AC36 are observed at this unit's close.
  Observed by AC1.
- **S2** — The break. `HELP_MOVED` of `TOOL-dGroundRules-41` §6, the deferral line moved under
  another `## ` heading in a scratch copy, makes `INSTALL_LINES_WHOLE` print `0` there.
  Observed by AC2.

## 3. Non-goals (OUT)

- The page's wording and the case's parity check: `TOOL-dGroundRules-41` S1 and
  `TOOL-dGroundRules-34` S36. This unit observes them.
- The leg-join observation and the case's witness line: `TOOL-dGroundRules-49` and
  `TOOL-dGroundRules-50`.

### Edges

- **consumes-from** `TOOL-dGroundRules-41` — S3's restated AC36 on the `## Install` section of `help/policy.md`, and the `HELP_MOVED` staging, which S1 and S2 observe with the path whole
- **hands-off** `TOOL-dGroundRules-52` — `INSTALL_LINES_WHOLE`, through which that unit observes `TOOL-dGroundRules-41` AC4 (id 31)

## 4. Design

The page path is spelled whole in a fenced block of §5 and nowhere in a criterion bullet, because
`help/policy.md` is not tracked at this spec's base and the spec-tokens paths join reds an untracked
path in a bullet (`TOOL-dGroundRules-42` S3). The section bounds are the ones
`TOOL-dGroundRules-34` AC36 states: the line after `## Install` up to the next `## ` heading.

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

## 5. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr48`, checked out at the commit under test. The literal is spelled whole here, once, and the
criteria name it:

```text
INSTALL_LINES_WHOLE = awk '/^## Install/{f=1;next} /^## /{f=0} f' help/policy.md | grep -c "mirror deferred"
```

- **AC1** — When `INSTALL_LINES_WHOLE` runs on the built tree, it prints `1` or more.
  Red when: the deferral line sits outside the section an installer reads, or the page is absent.
- **AC2** — When `HELP_MOVED` runs in the scratch copy and `INSTALL_LINES_WHOLE` runs there, it
  prints `0`.
  Red when: the count reads the whole page rather than the install section, so it cannot fail.

## 6. Gates

`memory hygiene`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 2 (HIGH, item H2) of the round-1 spec
  audit of units 35 to 43, from the review's sound fix, with unit 41's literals read on 2026-10-23.

## 9. Reuse audit

No existing seam fits beyond the one observed: the count is `TOOL-dGroundRules-34` AC36's own
command with its path whole, and the break is `TOOL-dGroundRules-41`'s `HELP_MOVED`, so nothing is
built. `python tools/codebase-map/reuse_lookup.py "read test table rows from a suite file to probe two
overlap rules"` and the help-page probe `TOOL-dGroundRules-41` §10 ran ranked no seam that reads a
help page's section. The recall probe returned `TOOL-dGroundRules-42` and `TOOL-dGroundRules-41`;
both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
