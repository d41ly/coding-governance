# TOOL-dRankedPlan-39 — a command led by a compound-command reserved word is read past that word

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-39-deviation-391.md](../build/2026-10-27-build-TOOL-dRankedPlan-39-deviation-391.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) | spec-audit | TOOL-dRankedPlan-43 TOOL-dRankedPlan-38 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-44 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 2 at HIGH**, item **H2**, which it shares with finding 34. `TOOL-dRankedPlan-32` S2 reads a
command's first word after skipping only `NAME=value` words. So in `if ! "$py" "$d/ratify.py" "$slug";
then` the first word is `if`, and the guarded call to the predicate's CLI is never an invocation. The
tree already writes that shape at `tools/lexicon/adopt-lexicon.sh:423`. Unit 32 §5 nevertheless says
"every unread form is named in §3", and no plant covers the guarded form. This unit skips the
compound-command reserved words before the command word is read, and replaces §5's claim with a table
of the forms the reader reads. Finding 34, the prefix commands and the case arm of the same item, is
`TOOL-dRankedPlan-40`'s. This unit repairs `TOOL-dRankedPlan-32`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The reserved words. `SHELL_RESERVED_WORDS = ("if", "then", "elif", "else", "while", "until",
  "do", "!", "{")` in `tools/loop/ratify.py`. `read_shell_callers` (`TOOL-dRankedPlan-32` S2) skips
  every leading word of a command that is in this set, before and after the `NAME=value` words unit 32
  already skips, and reads the next word as the command word. Unit 32 S2's two invocation forms and its
  mode-flag rule then apply unchanged. Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-shell-if` plants a `.githooks/pre-commit` holding `if ! "$py" "$d/ratify.py" "$slug"; then
    exit 1; fi`. It is refused.
  - `caller-shell-if-exit` plants the same line with `--exit` after `"$slug"`. It is admitted.
- **S3** — The claim corrected. §4 "The forms read" of this unit is the list of shell forms the reader
  reads. It supersedes unit 32 §5's security line, "every unread form is named in §3", which was false
  for this form. NOT OBSERVED by a criterion: it is a record correction, and the plants observe the
  forms it lists.

## 3. Non-goals (OUT)

- The prefix commands `exec`, `command`, `time`, `env` and `nohup`, and a case-arm pattern (finding
  34): `TOOL-dRankedPlan-40`.
- The textual rule for a line naming the predicate: `TOOL-dRankedPlan-38`.
- The tokenizer and its error rule: `TOOL-dRankedPlan-41`. S1 is stated over the words of a command,
  whichever tokenizer yields them.
- `case`, `for`, `select` and `function` as leading words. Each is followed by a name or a pattern
  list, never by a command, so skipping it would misread the next word.

### Edges

- **consumes-from** `TOOL-dRankedPlan-32` — `read_shell_callers` and S2's command-word rule, which S1 reads past the reserved words; without it there is no command word to find
- **hands-off** `TOOL-dRankedPlan-51` — `SHELL_RESERVED_WORDS`, from which that unit takes the `{` the tokenizer never yields as a word (spec audit of units 38 to 45, id 35)
- **hands-off** `TOOL-dRankedPlan-52` — `SHELL_RESERVED_WORDS`, §4 Evidence and §10, which that unit's items for findings 2, 15 and 20 probe and correct; carry S17 and S21 into this unit's pass (spec audit of units 38 to 45, ids 2, 15, 20)

## 4. Design

### Evidence

- `tools/lexicon/adopt-lexicon.sh:423` reads `if ! "$PY" "$KIT_DIR/lexicon_conf.py" --print-verbs
  "$CONF" >/dev/null; then`.
- A scratch probe over the 175 tracked shell files, every `*.sh` and every `.githooks/` file but its
  one `*.py`, run 2026-10-27 at base 0689e7fa, counted the leading words that sit before an interpreter word running a `*.py` script:
  `if` 2 and `!` 1, both at `tools/lexicon/adopt-lexicon.sh:423`. The counts are PINNED.
- `TOOL-dRankedPlan-32` §3 names only a call assembled at run time as unread.

### The forms read

| Form | Read by |
|---|---|
| `"$py" "$d/ratify.py" …`, `ratify.py …` | `TOOL-dRankedPlan-32` S2 |
| led by `NAME=value` words | `TOOL-dRankedPlan-32` S2 |
| led by `if`, `then`, `elif`, `else`, `while`, `until`, `do`, `!` or `{` | S1 |
| led by `exec`, `command`, `time`, `env` or `nohup`, or by a case-arm pattern | `TOOL-dRankedPlan-40` |
| any line naming `read_plan_ratification` | `TOOL-dRankedPlan-38` |
| a call assembled at run time from pieces | unread, `TOOL-dRankedPlan-32` §3 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SHELL_RESERVED_WORDS` | constant, `tools/loop/ratify.py` | none declared |
| `caller-shell-if`, `caller-shell-if-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. Units 38 to 41 share order 8 and all write `tools/loop/ratify.py`, so by
BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Judge any interpreter word anywhere in the command that is followed by a word ending
  `ratify.py`.** It reads past every prefix at once, but it also reads `echo "$py" "$d/ratify.py"`
  as an invocation, which unit 32 S2 admits by position on purpose.

## 5. Production-readiness checklist

- security — narrows: the guarded call, the likeliest hook spelling, is refused by the
  deny-by-default ban.
- perf / scale — one set test per leading word of a command.
- error / empty / loading states — a command made only of reserved words has no command word, and is
  not an invocation.
- observability — the refusal names the file and the command's first line.
- risks — none beyond unit 32's.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-if` runs, the check exits 1 naming
  `.githooks/pre-commit` and the `if` line.
  Red when: a call to the predicate's CLI guarded by `if !` passes.
- **AC2** — When the plant `caller-shell-if-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a guarded `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · the `caller-shell-if` and `caller-shell-if-exit` plants, staged by a reader that takes `if` as the command word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 2 (HIGH,
  item H2, shared with finding 34), repairing `TOOL-dRankedPlan-32`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-51`, the hands-off edge to `TOOL-dRankedPlan-52`, each the reciprocal of that promoted unit's own edge (spec audit of units 38 to 45, `reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-32`'s `read_shell_callers`, which gains a skip set before its
command word. `python tools/codebase-map/reuse_lookup.py "tokenize shell source into commands and
words with quotes and command substitution"` ranked `parse_shell_defs` and `resolve_shell_argv`, and
neither skips a reserved word, so no seam fits beyond unit 32's reader. The recall query returned this
audit's H2 item, whose fix lists the same words, and they agree with the probe.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader find a script invocation behind if exec or a case arm" --terms "shell tokenizer scan_shell_tokens invocation reserved word exec case pattern heredoc shlex caller predicate"`
