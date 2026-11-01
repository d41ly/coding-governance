# TOOL-dRankedPlan-76 — an arithmetic expansion of an expanded heredoc body is scanned, and its text is read by the line rule

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-76-deviation-761.md](../build/2026-10-27-build-TOOL-dRankedPlan-76-deviation-761.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 23 at HIGH**, item **H6**. `TOOL-dRankedPlan-66` S1 skips `$((` arithmetic whole, and its §3
justifies that with "It runs no command word". The premise is false: bash runs every command
substitution nested in an arithmetic expansion, so the `cat` body `$(( $("$py" "$d/ratify.py"
"$slug") + 1 ))` runs `ratify.py`, and the skipped text is never read. Bash also re-reads a `$((`
whose text is not arithmetic as a command substitution of a subshell, so `$(("$py" "$d/ratify.py"
"$slug") )` runs it too. This unit scans an arithmetic expansion for nested spans and reads its own
text by the line rule. It repairs `TOOL-dRankedPlan-66`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The arithmetic span. In the scan of `TOOL-dRankedPlan-66` S1, a `$((` that no unescaped `\`
  precedes opens an arithmetic span and no command span. It closes at the `)` that brings its two
  opening parentheses back to zero, counting parentheses outside quotes and outside nested spans.
  Inside it, a `$(` or a backtick opens a nested span by unit 66 S1's rule, read by unit 66 S2. This
  supersedes unit 66 S1's "and `$((` opens arithmetic and is skipped", and unit 66 §3's bullet
  "Arithmetic `$((…))`. It runs no command word." Observed by AC1 and AC3.
- **S2** — The arithmetic text. The text of an arithmetic span outside its nested spans is read by the
  line rule unit 66 S2 applies over a span, with `(` and `)` read as word breaks, because bash runs it
  as a command when it does not parse as arithmetic. Valid arithmetic names no file, so the rule never
  refuses it. An arithmetic span that never closes exits 2 by unit 66 S3. Observed by AC2 and AC3.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.githooks/pre-commit` feeding `cat
  <<EOF`. Observed by AC1 to AC3.
  - `caller-heredoc-cat-arith` feeds the body line `$(( $("$py" "$d/ratify.py" "$slug") + 1 ))`. It
    is refused with exit 1.
  - `caller-heredoc-cat-arith-reparse` feeds `$(("$py" "$d/ratify.py" "$slug") )`. It is refused with
    exit 1.
  - `caller-heredoc-cat-arith-plain` feeds `$(( n + 1 )) is what ratify.py prints`. It is admitted,
    because the arithmetic text names no file and the `ratify.py` word sits outside every span.

## 3. Non-goals (OUT)

- The escape rule of a `$(` or backtick opener: `TOOL-dRankedPlan-77`'s item for finding 12, carried
  into unit 66 S1.
- A `((…))` arithmetic command at a command word's place: data in a `cat` body, and unit 51's reading
  where a shell reads it.

### Edges

- **consumes-from** `TOOL-dRankedPlan-66` — S1's scan, S2's span reading and line rule, S3's exit 2 and §3's arithmetic bullet, which S1 and S2 restate; without them no span is read
- **hands-off** `TOOL-dRankedPlan-81` — §3 and §10, which that unit's item for finding 12 corrects; carry S9 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- Git Bash on 2026-10-27 ran `cat <<EOF` with the body `$(( $(echo 1; echo RAN-ARITH >&2) + 1 ))`
  and printed `RAN-ARITH` and `2`, and with `$((echo RAN-REPARSE) )` printed `RAN-REPARSE`. With
  `py=echo d=/k slug=s` it ran `$(("$py" "$d/ratify.py" "$slug") )` and printed `/k/ratify.py s`.
  The outputs are PINNED.
- `TOOL-dRankedPlan-66` S1 reads "`$((` opens arithmetic and is skipped", and its §3 reads "Arithmetic
  `$((…))`. It runs no command word."

### The reading after this unit

| Body line fed to `cat <<EOF` | Read | Answer |
|---|---|---|
| `$(( $("$py" "$d/ratify.py" "$slug") + 1 ))` | the nested span, by the shell reader and the line rule | caller |
| `$(("$py" "$d/ratify.py" "$slug") )` | the arithmetic text, by the line rule | caller |
| `$(( n + 1 )) is what ratify.py prints` | the arithmetic text; the rest is data | not a caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-cat-arith`, `caller-heredoc-cat-arith-reparse`, `caller-heredoc-cat-arith-plain` | `ratify.py` fixture plants | none |

No item mints a function. S1 and S2 are a branch of unit 66's span scanner.

### Rollout

Live at landing, at order 25. Units 67, 73, 74 and 75 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Scan nested spans only, and keep the arithmetic text as data.** The audit's fix. The re-read form
  then runs `ratify.py` unread, because its text is the command and holds no nested span.
- **Read the arithmetic text with the shell reader.** Arithmetic holds `<<`, `*` and `(`, which the
  shell tokenizer reads as redirections, globs and subshells, so valid arithmetic would exit 2.

## 5. Production-readiness checklist

- security — narrows: a command substitution nested in arithmetic, and arithmetic bash re-reads as a
  command, are read by the ban.
- perf / scale — none: the same scan, one more opener.
- error / empty / loading states — an arithmetic span that never closes exits 2 by unit 66 S3.
- observability — the refusal names the hook and the body's line.
- risks — arithmetic text naming `ratify.py` is refused even where bash would fail to run it, which
  fails closed.
- testing — the three plants.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-cat-arith` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: `$((` is skipped whole, as unit 66 S1 is written.
- **AC2** — When the plant `caller-heredoc-cat-arith-reparse` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the arithmetic text outside nested spans is data, so the re-read command passes.
- **AC3** — When the plant `caller-heredoc-cat-arith-plain` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: the line rule reads text outside the arithmetic span.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three plants: a scan that skips `$((` whole reddens AC1 and AC2, one that keeps the arithmetic text as data reddens AC2, and a line rule over the whole body line reddens AC3 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 23
  (HIGH, item H6), repairing `TOOL-dRankedPlan-66`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-81`, the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-66` S1's span scanner and S2's readers, which a new opener
feeds; the line rule is the one unit 66 S2 already applies. `python
tools/codebase-map/reuse_lookup.py "find command substitution spans in heredoc text with case esac"`,
run 2026-10-27, ranked name stems only (`read_text`, `write_text`, `load_text`), none of which scans
shell, so no existing seam fits beyond unit 66's scanner. The recall query returned units 46, 53 and
65 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read command substitutions inside an expanded heredoc body and ansi-c carriers" --terms "heredoc expanded command substitution span case esac arithmetic ansi-c carrier shlex caller ratify"`
