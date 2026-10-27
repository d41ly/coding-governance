# TOOL-dRankedPlan-75 — a command substitution span of an expanded heredoc body does not count a `case` statement's parentheses

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-75-deviation-751.md](../build/2026-10-27-build-TOOL-dRankedPlan-75-deviation-751.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 13 at HIGH**, item **H5**. Finding 17, item M7, reports the same bypass beside a hidden
minted function, and its item in `TOOL-dRankedPlan-77` names that function in unit 66's Inventory.
`TOOL-dRankedPlan-66` S1 closes a `$(` span "at the `)` that balances it, counting parentheses outside
quotes". A `case` arm's pattern `)` has no opening `(`, and bash accepts it inside a substitution, so
the body line `$(case $x in a) "$py" "$d/ratify.py" "$slug";; esac)` closes the span at `a)`. The
span reads `case $x in a`, the call after it is read as data, and it passes the deny-by-default ban
though bash runs it during expansion. This unit carries the `case` … `esac` skip into the span's
close rule. It repairs `TOOL-dRankedPlan-66`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The skip. In `TOOL-dRankedPlan-66` S1's `$(` span, between a `case` word and its matching
  `esac` word at the span's own depth, a bare `(` or `)` outside quotes is not counted. A `$(` there
  still opens a nested span, whose own parentheses are counted as anywhere. A `case` or `esac` word is
  that run of letters outside quotes, bounded on each side by the span's start or end, whitespace, `;`,
  `&`, `|`, `(` or `)`. Each `case` opens one level and each `esac` closes the latest, so nested
  statements balance. This is the rule `TOOL-dRankedPlan-67` S20 gives unit 62 S12's `close` index,
  stated for the character scan, which reads text the shell tokenizer cannot. It supersedes unit 66
  S1's "counting parentheses outside quotes inside the span" for a span that holds a `case` word.
  Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.githooks/pre-commit` feeding `cat
  <<EOF`. Observed by AC1 and AC2.
  - `caller-heredoc-cat-case` feeds the body line `$(case $x in a) "$py" "$d/ratify.py" "$slug";;
    esac)`. It is refused with exit 1. It is the plant finding 17's fix names
    `caller-heredoc-cat-subst-case`; one is built, under this name.
  - `caller-heredoc-cat-case-paren` feeds `$(case $x in (a) "$py" "$d/ratify.py" "$slug";; esac)`,
    whose pattern takes the optional opening `(`. It is refused with exit 1.

## 3. Non-goals (OUT)

- The token-based `close` index of `parse_shell_defs`: `TOOL-dRankedPlan-67` S20, unchanged.
- An `esac` written as an ordinary argument inside an arm, such as `echo esac`. It closes the level
  early, the ceiling §5 names.
- Unit 66's Inventory row for the span scanner: `TOOL-dRankedPlan-77`'s item for finding 17.

### Edges

- **consumes-from** `TOOL-dRankedPlan-66` — S1's span scan and close rule, which S1 amends; without it there is no span to close
- **hands-off** `TOOL-dRankedPlan-77` — S1's amended scanner and S2's `caller-heredoc-cat-case`, which that unit's item for finding 17 names in unit 66's Inventory

## 4. Design

### Evidence

- Git Bash ran `x=a; cat <<EOF` with the body `$(case $x in a) echo RAN-CASE;; esac)` on 2026-10-27
  and printed `RAN-CASE`, so the arm runs during the expansion of a body fed to `cat`. The output is
  PINNED.
- `TOOL-dRankedPlan-67` S20 states the skip for `parse_shell_defs(src, spans=True)`'s `close` index
  only, and unit 66 S1 counts every parenthesis outside quotes.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-cat-case`, `caller-heredoc-cat-case-paren` | `ratify.py` fixture plants | none |

No item mints a function. S1 amends the close rule of unit 66's span scanner.

### Rollout

Live at landing, at order 25. Units 67, 73, 74 and 76 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Call `TOOL-dRankedPlan-67` S20's `close` index.** It indexes `scan_shell_tokens` output, and a
  `cat` body is prose the tokenizer raises on, which is why unit 66 scans characters.
- **Skip `)` alone and count `(`.** The optional opening `(` of a pattern then never closes, and the
  span runs to the body's end and exits 2.

## 5. Production-readiness checklist

- security — narrows: a `case` statement inside a substitution of an expanded heredoc body is read.
- perf / scale — none: a level counter in the same scan.
- error / empty / loading states — a `case` with no `esac` leaves the span open, and unit 66 S3 exits 2.
- observability — the refusal names the hook and the body's line.
- risks — an argument word `esac` inside an arm closes the level early, so a later pattern `)` can close
  the span early: the ceiling, a reading narrower than bash's.
- testing — the two plants.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-cat-case` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: the span counts the pattern's `)` and closes at `a)`.
- **AC2** — When the plant `caller-heredoc-cat-case-paren` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the skip ignores `)` alone, so the pattern's `(` never closes and the check exits 2.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `caller-heredoc-cat-case` reddened by a bare parenthesis count, and `caller-heredoc-cat-case-paren` reddened by a skip of `)` alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 13
  (HIGH, item H5; finding 17 shares the defect at medium), repairing `TOOL-dRankedPlan-66`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-66` S1's span scanner, whose close rule gains the skip
`TOOL-dRankedPlan-67` S20 states for the token-based `close` index. `python
tools/codebase-map/reuse_lookup.py "find command substitution spans in heredoc text with case esac"`,
run 2026-10-27, ranked name stems only (`read_text`, `write_text`, `load_text`), none of which scans
shell, so no existing seam fits beyond unit 66's scanner. The recall query returned units 46, 53 and
65 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read command substitutions inside an expanded heredoc body and ansi-c carriers" --terms "heredoc expanded command substitution span case esac arithmetic ansi-c carrier shlex caller ratify"`
