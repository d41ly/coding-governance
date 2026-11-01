# TOOL-dRankedPlan-66 — the command substitutions of an expanded heredoc body fed to any other command are read as commands

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-66-deviation-661.md](../build/2026-10-27-build-TOOL-dRankedPlan-66-deviation-661.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) | spec-audit | TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-67 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 53 to 62
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`) confirmed
**finding 31 at HIGH**, item **H3**. `TOOL-dRankedPlan-53` S1 justifies its line rule by the outer
shell expanding a body before `bash` reads it. That expansion runs every `$(…)` and backtick span of
an unquoted body whatever the command word is. Units 53 and 54 route an expanded body only for shell
and Python command words, and `TOOL-dRankedPlan-46` §4 and `TOOL-dRankedPlan-47` §4 map "any other
word" to `TOOL-dRankedPlan-38`'s textual rule, which matches only `read_plan_ratification`. So `cat
<<EOF` with the body `$("$py" "$d/ratify.py" "$slug")` runs `ratify.py` during expansion and passes
the deny-by-default ban. This unit reads those spans as the commands they are. It repairs
`TOOL-dRankedPlan-53`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The spans. In the text of a `heredoc-expanded` body whose command word is in neither
  `SHELL_BODY_WORDS` nor `TOOL-dRankedPlan-47` S1's Python class, a span opens at `$(` or at a
  backtick that no unescaped `\` precedes, and `$((` opens arithmetic and is skipped. A `$(` span
  closes at the `)` that balances it, counting parentheses outside quotes inside the span, and a
  backtick span closes at the next unescaped backtick. Text outside every span is data and is not
  tokenized. Observed by AC1, AC3 and AC4.
- **S2** — The reading. Each span's text is read by `read_shell_callers` as a file of its own, with
  `TOOL-dRankedPlan-55`'s inherited bindings, because the outer shell runs it with the enclosing
  file's variables. `TOOL-dRankedPlan-52` S13's line rule applies over each line of the span's text,
  as `TOOL-dRankedPlan-53` S1 applies it beside the shell reader. The body is refused when either
  reads a caller, and `TOOL-dRankedPlan-38`'s textual rule still reads the whole body. This adds the
  router row "any other command word, `heredoc-expanded`" to the routing of `TOOL-dRankedPlan-46` §4,
  `TOOL-dRankedPlan-47` §4 and `TOOL-dRankedPlan-54` §4, whose "any other word" row stays for the
  `heredoc` kind. Observed by AC1 to AC3.
- **S3** — The refusal. A span that never closes, or whose text the shell tokenizer cannot read,
  exits 2 naming the file and the body's line, as `TOOL-dRankedPlan-41` S4 states for a file.
  Observed by AC5.
- **S4** — The plants. Five cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.githooks/pre-commit` feeding
  `cat`. Observed by AC1 to AC5.
  - `caller-heredoc-cat-subst` feeds `cat <<EOF` the body line `$("$py" "$d/ratify.py" "$slug")`. It
    is refused with exit 1.
  - `caller-heredoc-cat-subst-quoted` feeds `cat <<'EOF'` the same line. It is admitted, because a
    quoted body is data.
  - `caller-heredoc-cat-backtick` feeds `cat <<EOF` the body line `` `"$py" "$d/ratify.py" "$slug"`
    ``. It is refused with exit 1.
  - `caller-heredoc-cat-prose` feeds `cat <<EOF` the body line `it's run by ratify.py at $(date)`.
    It is admitted, with exit 0: the apostrophe and the `ratify.py` word sit outside the one span.
  - `caller-heredoc-cat-unclosed` feeds `cat <<EOF` the body line `$("$py" "$d/ratify.py"` with no
    closing `)`. It exits 2.

## 3. Non-goals (OUT)

- A body fed to a shell or a Python word: `TOOL-dRankedPlan-53` and `TOOL-dRankedPlan-52` S13. A
  shell-fed body is already read whole by the shell reader, which reads its spans.
- `${…}` parameter expansion with no command inside. It runs no command, so it is data here.
- Arithmetic `$((…))`. It runs no command word.
- A `heredoc` body, quoted, fed to any other word: data, `TOOL-dRankedPlan-38`'s textual rule only,
  unchanged.

### Edges

- **consumes-from** `TOOL-dRankedPlan-53` — S1's expansion reading and its line rule beside the shell reader, which S2 extends past the shell class
- **consumes-from** `TOOL-dRankedPlan-54` — `HEREDOC_KINDS` and the router's membership test, to which S2 adds the row for any other command word; without them no expanded body reaches a reader
- **consumes-from** `TOOL-dRankedPlan-55` — the enclosing file's bindings a body inherits, which S2 gives each span
- **hands-off** `TOOL-dRankedPlan-75` — S1's span close rule, to which that unit adds the `case` … `esac` skip (spec audit of units 63 to 67, id 13)
- **hands-off** `TOOL-dRankedPlan-76` — S1's arithmetic skip, S2, S3 and §3's arithmetic bullet, which that unit restates (spec audit of units 63 to 67, id 23)
- **hands-off** `TOOL-dRankedPlan-77` — S1, S3, S4, §4 and §7, which that unit's items for findings 12, 24, 17 and 21 amend; carry S9 to S12 of that unit into this unit's pass (spec audit of units 63 to 67)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-46` §4 "The routing after this unit" and `TOOL-dRankedPlan-47` §4 of the same
  heading each map "any other word" to `TOOL-dRankedPlan-38`'s textual rule only.
  `TOOL-dRankedPlan-54` §4 "The router after this unit" has the columns `bash` and `"$py"` only.
- A probe run 2026-10-27 at c22908a6 over `scan_shell_tokens("run ratify.py's check: $(date)\n")`
  from `tools/lexicon/lexicon.py` raised `SyntaxError: unterminated ' quote opened at line 1`. A
  reading that tokenizes a whole `cat` body would exit 2 on ordinary prose, which is why S1 tokenizes
  the spans only. The output is PINNED.
- `git grep -nE '\bcat <<[^<]' -- '*.sh' '.githooks/*'`, run 2026-10-27 at c22908a6, printed 10
  lines, 5 of them with an unquoted delimiter. None names `ratify.py`. The counts are PINNED.

### The router after this unit, for a command word in neither class

| Body token kind | Readers | `$("$py" "$d/ratify.py" "$slug")` in the body |
|---|---|---|
| `heredoc` | `TOOL-dRankedPlan-38`'s textual rule | not a caller, data |
| `heredoc-expanded` | the textual rule, and each span by the shell reader and the line rule | caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-cat-subst`, `caller-heredoc-cat-subst-quoted`, `caller-heredoc-cat-backtick`, `caller-heredoc-cat-prose`, `caller-heredoc-cat-unclosed` | `ratify.py` fixture plants | none |

No item mints a function. S1 and S2 are the router arm for the new row.

### Rollout

Live at landing, at order 24. `TOOL-dRankedPlan-62` and `TOOL-dRankedPlan-65` share order 24 and
write `tools/loop/ratify.py` too, so by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S4

### Alternatives rejected

- **Hand the whole expanded body to the shell reader.** The body of `cat` is prose, and the probe
  above shows one apostrophe makes the tokenizer raise, so every help heredoc would exit 2.
- **Apply the line rule to the whole body.** A help text naming `ratify.py` is printed, not run, so
  that refuses data. The spans are what the expansion runs, so the line rule reads them.
- **Name the form as unread.** The ban is deny-by-default, and 5 tracked `cat` heredocs already
  expand their bodies.

## 5. Production-readiness checklist

- security — narrows: a command substitution the outer shell runs inside any expanded heredoc is
  read by the ban.
- perf / scale — one character scan per expanded body fed to another word, and one tokenizer pass per
  span. None names `ratify.py` at base.
- error / empty / loading states — S3's exit 2 for a span that never closes.
- observability — the refusal names the hook and the body's line.
- risks — a span that only echoes `ratify.py`, such as `$(echo ratify.py)`, is refused by the line
  rule, which fails closed.
- testing — the five plants: refused, admitted and exit 2.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-cat-subst` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: an expanded body fed to `cat` reaches the textual rule only and passes.
- **AC2** — When the plant `caller-heredoc-cat-subst-quoted` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a quoted body's spans are read as commands.
- **AC3** — When the plant `caller-heredoc-cat-backtick` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a backtick span is not opened, so only `$(` spans are read.
- **AC4** — When the plant `caller-heredoc-cat-prose` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: the whole body is tokenized, so the apostrophe exits 2, or the line rule reads text outside
  the spans and refuses the line naming `ratify.py`.
- **AC5** — When the plant `caller-heredoc-cat-unclosed` runs, the check exits 2 and prints the
  `.githooks/pre-commit` line.
  Red when: an unclosed span is read as data, or raises a traceback.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC3 AC4 AC5 · the five `caller-heredoc-cat-*` plants: a router whose any-other-word arm reads every body by the textual rule only reddens AC1, AC3 and AC5; a span reader that tokenizes the whole body reddens AC4; AC2 is green-only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 53 to 62, finding 31 (HIGH,
  item H3), repairing `TOOL-dRankedPlan-53`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-75`, the hands-off edge to `TOOL-dRankedPlan-76`, the hands-off edge to `TOOL-dRankedPlan-77`, each the reciprocal of that promoted unit's own edge (spec audit of units 63 to 67, `reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are the body router of `TOOL-dRankedPlan-54` over `HEREDOC_KINDS`, which gains a
row, and `read_shell_callers` with `TOOL-dRankedPlan-55`'s bindings and `TOOL-dRankedPlan-52` S13's
line rule, which read each span. `python tools/codebase-map/reuse_lookup.py "find command
substitutions inside an unquoted heredoc body"`, run 2026-10-27, ranked name stems only
(`build_baseline_findings`, `find_block`, `ratchet_findings`), none of which reads shell, so no
existing seam finds a span in prose. S1's scan is new for that reason: the shell tokenizer finds
spans only in text it can tokenize whole. The recall query returned units 46, 47 and 52 to 56 and this
audit's H3 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read a bash -c word or a heredoc whose body the outer shell expands" --terms "bash -c carrier double-quoted unquote shlex heredoc expanded command substitution backtick span line rule caller ratify"`
