# TOOL-dGroundRules-48 — the help page's install-section count observed with its path whole, and paired with the break that empties it

**Status:** CLOSED · rev-2 · 2026-10-24 · node d · Tier-1 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-48-deviation-36.md](../build/2026-10-23-build-TOOL-dGroundRules-48-deviation-36.md) | deviation | — |
| [2026-10-24-build-TOOL-dGroundRules-48-ledger.md](../build/2026-10-24-build-TOOL-dGroundRules-48-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-48-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-48-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-47-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-47-staleness-probe-brief.md) | research | TOOL-dGroundRules-47 TOOL-dGroundRules-49 TOOL-dGroundRules-50 |
| [2026-10-24-prompt-TOOL-dGroundRules-48-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-48-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-48-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-48-probe-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 2 at HIGH**, which shares item **H2** with ids 11
(`TOOL-dGroundRules-49`) and 22 (`TOOL-dGroundRules-50`). Id 2 is H2 seen from coherence: when the
audit ran, `TOOL-dGroundRules-41`'s `INSTALL_LINES` ran `awk` over a bare `policy.md`, which does not
open from the repository root, so the restated `TOOL-dGroundRules-34` AC36 printed 0 on a correct
build. `TOOL-dGroundRules-41` rev-4 now spells the page whole in `INSTALL_LINES`, so the count needs
no second spelling. What id 2 still owes is the count shown able to fail: this unit observes
`INSTALL_LINES` at its close, where it is already green, and pairs it with `HELP_MOVED`, the staged
break that must turn it to zero. It writes no product code. It follows `TOOL-dGroundRules-41`, at
order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The count, through unit 41's literal. `INSTALL_LINES` of `TOOL-dGroundRules-41` §6
  already counts the lines holding `mirror deferred` inside the `## Install` section of
  `help/policy.md`, with the page path whole. This unit adds no second command: it observes
  `TOOL-dGroundRules-41` AC4 and `TOOL-dGroundRules-34` AC36 through that literal at its close.
  Observed by AC1.
- **S2** — The break. `HELP_MOVED` of `TOOL-dGroundRules-41` §6, staged in a scratch clone, makes
  `INSTALL_LINES` print `0` there. The staging lives in the clone and is never committed, so S2
  needs no product code, and this unit writes none.
  Observed by AC2.

## 3. Non-goals (OUT)

- The page's wording, the count's command and the case's parity check: `TOOL-dGroundRules-41` S1,
  S3 and §6, and `TOOL-dGroundRules-34` S36. This unit observes them.
- The leg-join observation and the case's witness line: `TOOL-dGroundRules-49` and
  `TOOL-dGroundRules-50`.
- Respelling `TOOL-dGroundRules-52` S13 and AC11, which still name this spec's rev-1 literal: that
  spec's own revision.

### Edges

- **consumes-from** `TOOL-dGroundRules-41` — `INSTALL_LINES` and the `HELP_MOVED` staging of its §6, which S1 and S2 observe; without them this unit has no count and no break
- **hands-off** `TOOL-dGroundRules-52` — `INSTALL_LINES`, through which that unit observes `TOOL-dGroundRules-41` AC4 (id 31); its S13 and AC11 still spell `INSTALL_LINES_WHOLE` of this spec's rev-1, which this revision no longer defines

## 4. Design

`help/policy.md` is tracked at HEAD: `git ls-files --error-unmatch help/policy.md` named it at
`9bcca6523` on 2026-10-24. So the page path sits whole in a criterion bullet; rev-1 held it in a
fenced block only because the page was untracked at this spec's base. The `## Install` section is
`TOOL-dGroundRules-34` S36's, landed in `75b1ffe59`. At `9bcca6523` the page's deferral line,
`adopt-policy: mirror deferred · <file> has uncommitted changes · commit, then re-run --scaffold`,
sits under `## Install`, ahead of the next heading, `## Every key whose build has landed has a reader`,
and `INSTALL_LINES` printed `1` over it.

That is why the first criterion is green before this unit, and why the second is the one that can
red: a count of `1` cannot tell a section-bounded read from a whole-page grep, and `HELP_MOVED`
can, because it leaves the line on the page and only moves it out of the section. The section bounds
are the ones `TOOL-dGroundRules-34` AC36 states: the line after `## Install` up to the next `## `
heading.

### Files touched (estimate)

none — the unit writes no file of the product; S2's staging lives in a scratch clone, and the unit's
evidence is its acceptance ledger.

## 5. Acceptance criteria

Every command runs from a repository root: the first criterion from this repository's, the second
from the scratch clone's, which `SCRATCH` makes from this repository's root. The count is
`INSTALL_LINES` of `TOOL-dGroundRules-41` §6, named here and not respelled; the one literal this
unit adds is the clone:

```text
SCRATCH = git clone --quiet . "$TEMP/gr48" && git -C "$TEMP/gr48" checkout --quiet <commit under test>
```

- **AC1** — When `INSTALL_LINES` of `TOOL-dGroundRules-41` §6 runs on the built tree, it prints `1` or more. It is green before this unit, which writes neither side of it: at `9bcca6523` it printed `1`.
  Red when: the deferral line sits outside the `## Install` section of `help/policy.md`, or the page is absent.
- **AC2** — When `SCRATCH` runs, `HELP_MOVED` of `TOOL-dGroundRules-41` §6 is staged in the clone, and `INSTALL_LINES` runs from the clone's root, it prints `0`.
  Red when: the count reads the whole page rather than the install section, so the first criterion could not fail.

## 6. Gates

`memory hygiene`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 2 (HIGH, item H2) of the round-1 spec
  audit of units 35 to 43, from the review's sound fix, with unit 41's literals read on 2026-10-23.
- rev-2 · 2026-10-24 · §1 §2 §3 §4 §5 §9 · S1 S2 · AC1 AC2 · a read-only probe of step 14 at `0860b8c1e` found this spec stale against the built branch, and this revision re-read every cited line at `9bcca6523`. Disagreements: S1 minted `INSTALL_LINES_WHOLE` while `TOOL-dGroundRules-41` rev-4's `INSTALL_LINES` already spells `help/policy.md` whole; §4 called the page untracked, and it is tracked at HEAD; AC1 read as able to red, though it is green before this unit. Rulings: S1 observes through `INSTALL_LINES` and adds no second command; the unit writes no product code beyond what S2 needs, which is none, and says so; §4 states the page tracked at HEAD; AC1 is stated green before this unit, with AC2's `HELP_MOVED` break the observation that can red; every moved line is cited by symbol. One disagreement kept visible: `TOOL-dGroundRules-52` S13, AC11 and its consumes-from edge still name `INSTALL_LINES_WHOLE`, which this revision no longer defines; respelling them is that spec's revision, outside this pass.

## 9. Reuse audit

No existing seam fits beyond the one observed, so nothing is built: the count is `INSTALL_LINES`
and the break is `HELP_MOVED`, both of `TOOL-dGroundRules-41` §6.
`python tools/codebase-map/reuse_lookup.py "count lines of a help page section between two markdown headings"`
ranked `counts`, `check_line` and `unfenced_lines`, and no seam that reads a help page's section. The
recall probe returned this spec, `TOOL-dGroundRules-41` §6 and `TOOL-dGroundRules-50`; they agree
with source.

Recall terms used: `python tools/memory-recall/query.py "help page install section count observed with path whole and its break" --terms "INSTALL_LINES HELP_MOVED help/policy.md install section mirror deferred awk count scratch copy"`
