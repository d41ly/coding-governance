# TOOL-dRankedPlan-65 — a shell carrier in any other quoting is unquoted as the shell does, then read as a single-quoted one

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-65-deviation-651.md](../build/2026-10-27-build-TOOL-dRankedPlan-65-deviation-651.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-65-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-65-promoted-fix-return.md) | research | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-65-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-65-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-65-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-65-promoted-fix-brief.md) | research | — |
| [2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) | spec-audit | TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 53 to 62
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`) confirmed
**finding 29 at HIGH**, item **H2**. `TOOL-dRankedPlan-56` S1 sends a `-c` word or here-string that is
not single-quoted to `TOOL-dRankedPlan-52` S13's line rule, a word ending in `ratify.py` with its
quotes stripped. `scan_shell_tokens` hands `bash -c "\"$py\" \"$d/ratify.py\" \"$slug\""` over as one
raw word with its escapes kept, and splitting and stripping quotes leaves `\$d/ratify.py\`, which ends
in a backslash. So the common double-quoted carrier passes the deny-by-default ban, while unit 56's
§4 row 3 answers "caller" for it. This unit removes the carrier's quoting the way the shell does and
then reads the text it leaves exactly as unit 56 S1 reads a single-quoted carrier. Finding 12 is the
medium face of the same defect, unit 56's design-table row, and its item in `TOOL-dRankedPlan-67`
corrects that row. This unit repairs `TOOL-dRankedPlan-56`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The unquoting. A `-c` word or `herestring` token of `TOOL-dRankedPlan-56` S1 that is not
  single-quoted is unquoted by `shlex.split(word, posix=True)`, which strips the double quotes and turns
  `\"` and `\\` inside them into their characters, and the words it returns are joined with one
  space. The text that leaves is read as `TOOL-dRankedPlan-56` S1 reads a single-quoted carrier: by
  `read_shell_callers` as a file of its own, with `TOOL-dRankedPlan-38`'s textual rule and
  `TOOL-dRankedPlan-55`'s inherited bindings, and with `TOOL-dRankedPlan-52` S13's line rule over the
  same unquoted text. The carrier is refused when any of them reads a caller. This supersedes unit 56
  S1's "Any other quoting is read by `TOOL-dRankedPlan-52` S13's textual line rule over the carrier's
  text". Observed by AC1 and AC2.
- **S2** — The refusal. A carrier `shlex.split` cannot split, an unbalanced quote say, exits 2 naming
  the file and the command's line, as `TOOL-dRankedPlan-41` S4 states for a file the shell tokenizer
  cannot read. Observed by AC3.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-c-dq` plants a `.githooks/pre-commit` holding `bash -c "\"$py\" \"$d/ratify.py\"
    \"$slug\""`, unit 56's §4 row 3 form. It is refused with exit 1.
  - `caller-shell-c-dq-exit` plants the same with `--exit` after `\"$slug\"` inside the quotes. It is
    admitted.
  - `caller-shell-c-dq-broken` plants `bash -c "\"$py\" \"$d/ratify.py` with no closing quote on a
    line that also names `ratify.py`. It exits 2.

## 3. Non-goals (OUT)

- `bash -c "$cmd"`: run-time assembly, unread as `TOOL-dRankedPlan-56` §3 states. Its unquoted text
  `$cmd` is a command word that is not an interpreter, so S1 reads no caller there either.
- A `\$` inside double quotes. `shlex` keeps its backslash, so `"\$d/ratify.py"` unquotes to
  `\$d/ratify.py`, which still ends in `ratify.py`, so no answer moves.
- Python carriers: `TOOL-dRankedPlan-52` S14, unchanged.
- Unit 56's §4 table row: `TOOL-dRankedPlan-67`'s item for finding 12 corrects its Reader column.

### Edges

- **consumes-from** `TOOL-dRankedPlan-56` — S1's shell carriers, their single-quoted reading and the `SHELL_BODY_WORDS` command test, which S1 extends to every other quoting; without them no shell carrier is selected
- **hands-off** `TOOL-dRankedPlan-67` — S1's unquoted reading, over which that unit's item for finding 35 plants a double-quoted carrier naming a bound path and its item for finding 12 corrects unit 56's §4 row 3
- **hands-off** `TOOL-dRankedPlan-73` — S1's readers, S2 and S3's third plant, which that unit restates by reader and replaces (spec audit of units 63 to 67, id 11)
- **hands-off** `TOOL-dRankedPlan-74` — S1's `shlex` unquoting, before which that unit renders ANSI-C and locale quoted segments (spec audit of units 63 to 67, id 25)
- **hands-off** `TOOL-dRankedPlan-77` — §4 Evidence and §7, which that unit's item for finding 4 corrects; carry S7 of that unit into this unit's pass (spec audit of units 63 to 67)
- **hands-off** `TOOL-dRankedPlan-81` — S3, its Inventory, AC3 and §5, which that unit's item for finding 13 corrects; carry S12 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- A probe run 2026-10-27 at c22908a6 over `scan_shell_tokens` from `tools/lexicon/lexicon.py` read
  `bash -c "\"$py\" \"$d/ratify.py\" \"$slug\""` as three words, the last `"\"$py\" \"$d/ratify.py\"
  \"$slug\""` with its escapes kept. `shlex.split` over that word returned the one word `"$py"
  "$d/ratify.py" "$slug"`, and `scan_shell_tokens` over that text returned the three words `"$py"`,
  `"$d/ratify.py"` and `"$slug"`. The outputs are PINNED.
- `git grep -nE '(^|[^A-Za-z0-9_./-])(bash|sh) -c "' -- '*.sh' '.githooks/*'`, run 2026-10-27 at
  c22908a6, printed 45 lines, and none of them opens its word with an escaped quote. The counts are
  PINNED. None names `ratify.py`.
- `TOOL-dRankedPlan-41` S3 took `shlex.split` out of the reader's word splitting, because a split
  piece left an open quote. Here `shlex` sees one whole carrier word, which the shell tokenizer
  already closed, and only removes its quoting; `scan_shell_tokens` keeps a word's quotes and so
  cannot do that step.

### The reading after this unit

| Command | Carrier | Readers | Answer |
|---|---|---|---|
| `bash -c "\"$py\" \"$d/ratify.py\" \"$slug\""` | double-quoted `-c` word | shell reader, name rule, line rule, after unquoting | caller |
| the same with `--exit` inside the quotes | the same | the same | not a caller |
| `bash -c "$cmd"` | double-quoted `-c` word | the same | unread, run-time assembly |
| `bash -c '"$py" "$d/ratify.py" "$slug"'` | single-quoted `-c` word | unit 56 S1 | caller, unchanged |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-c-dq`, `caller-shell-c-dq-exit`, `caller-shell-c-dq-broken` | `ratify.py` fixture plants | none |

No item mints a function. S1 is a branch of unit 56's carrier reading.

### Rollout

Live at landing, at order 24. `TOOL-dRankedPlan-62` and `TOOL-dRankedPlan-66` share order 24 and
write `tools/loop/ratify.py` too, so by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Unescape `\"` and `\\` by hand and keep the line rule alone.** That is the audit's first fix. A
  second quote-removal rule beside `shlex` drifts from it, and the unquoted text is shell source the
  shell reader already reads, so reading it as the single-quoted form is read makes the two
  quotings one path.
- **Name the double-quoted carrier as unread.** Unit 56 §4 already promises "caller" for it, and 45
  tracked lines write a double-quoted `-c` word, so a hook copying one would pass.

## 5. Production-readiness checklist

- security — narrows: a double-quoted shell carrier running the predicate's CLI is refused.
- perf / scale — one `shlex.split` and one tokenizer pass per carrier that is not single-quoted.
  None names `ratify.py` at base.
- error / empty / loading states — S2's exit 2 for a carrier that cannot be unquoted.
- observability — the refusal names the file and the command's line.
- risks — a double-quoted carrier naming `ratify.py` for a non-executing purpose is refused, which
  fails closed.
- testing — the three plants, red, green and refused.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-c-dq` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the line rule strips quotes from the raw carrier and leaves the backslashes, so no word
  ends in `ratify.py`.
- **AC2** — When the plant `caller-shell-c-dq-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: an unquoted carrier's `--exit` call is refused.
- **AC3** — When the plant `caller-shell-c-dq-broken` runs, the check exits 2 and prints the
  `.githooks/pre-commit` line.
  Red when: a carrier that cannot be unquoted is read as no caller, or raises a traceback.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC3 · `caller-shell-c-dq` reddened by unit 56 S1's line rule over the raw carrier, and `caller-shell-c-dq-broken` reddened by a `shlex` error read as no caller; AC2 is green-only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 53 to 62, finding 29 (HIGH,
  item H2; finding 12 is its medium face), repairing `TOOL-dRankedPlan-56`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-73`, the hands-off edge to `TOOL-dRankedPlan-74`, the hands-off edge to `TOOL-dRankedPlan-77`, each the reciprocal of that promoted unit's own edge (spec audit of units 63 to 67, `reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-81`, the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams reused are the stdlib `shlex.split`, as a quote remover over one closed word, and
`TOOL-dRankedPlan-56` S1's single-quoted carrier reading, which the unquoted text joins. `python tools/codebase-map/reuse_lookup.py "remove shell quoting from a
double-quoted word the way bash does"`, run 2026-10-27, ranked `resolve_bash`, `parse_shell_defs`
and `resolve_shell_argv` (`tools/govkit/govkit.py:1200`). The last replaces a leading `bash` in an
argv and removes no quoting, so no existing seam fits beyond `shlex` and unit 56's reading. The recall
query returned units 46, 47, 52 to 56 and this audit's H item records, and they agree with the source
read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read a bash -c word or a heredoc whose body the outer shell expands" --terms "bash -c carrier double-quoted unquote shlex heredoc expanded command substitution backtick span line rule caller ratify"`
