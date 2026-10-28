# TOOL-dRankedPlan-41 — the shell caller reader tokenizes through the shared shell tokenizer, and a file it cannot tokenize exits 2

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-38-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-38-promoted-fix-return.md) | research | TOOL-dRankedPlan-38 TOOL-dRankedPlan-45 |
| [2026-10-27-build-TOOL-dRankedPlan-41-deviation-411.md](../build/2026-10-27-build-TOOL-dRankedPlan-41-deviation-411.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-38-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-38-promoted-fix-brief.md) | research | TOOL-dRankedPlan-38 TOOL-dRankedPlan-45 |
| [2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) | spec-audit | TOOL-dRankedPlan-43 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-44 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 33 at HIGH**, item **H3**. `TOOL-dRankedPlan-32` S2 splits a joined line at `;`, `|`, `$(`, a
backtick and `(`, and only then calls `shlex.split`. A split at `$(` inside a quoted argument leaves an
open quote, so the most natural hook shape, `"$py" "$d/ratify.py" "$(…)"`, raises `ValueError`, and
neither S2 nor §5 says what follows. Built as written, `--check-callers` either crashes the always-run
leg on every bar or skips the piece and fails open. Finding 13 is the same gap at MEDIUM, item M7, and
`TOOL-dRankedPlan-45` adds its observation. The root cause is the hand-rolled splitter. The tree already
ships a shell tokenizer that reads `$(…)` inside double quotes as code, `scan_shell_tokens`, and it
tokenizes every tracked shell file with no error. This unit reads shell through that tokenizer, in a
separators mode added behind an opt-in parameter, and states the rule for a file it cannot tokenize:
exit 2 naming the file and line, never a skip. It repairs `TOOL-dRankedPlan-32`, so it sits one order
above it.

## 2. Scope (IN)

- **S1** — The separators mode. `scan_shell_tokens(src, seps=False)` in the canonical block of
  `tools/lib/extract_code.py` (TOOL-dTotalRecall-13 S1) gains the keyword `seps`. With `seps=False` the
  token stream is byte for byte what it is today, so `parse_shell_defs` and every current caller are
  unchanged. With `seps=True` it also emits these `op` tokens, each at its line: `;`, `;;`, `&`, `&&`,
  `|` and `||` where the shell reads them as operators; `\n` at the end of each code line that is not
  continued; `$(` at a command substitution's opening and `$)` at the `)` that closes it; and `` ` `` at
  each end of a backtick span, whose body is tokenized as code between them rather than kept as one
  opaque word. Observed by AC1 and AC4.
- **S2** — The copies. Every copy of the block carries S1 byte for byte, as TOOL-dTotalRecall-13 S3's
  parity row holds them. The loop kit gains its own copy, `tools/loop/extract_code.py`, found by the
  same `# >>> extract_code` marker, so `ratify.py` imports the tokenizer from its own directory and
  reaches across no kit boundary. Observed by AC4.
- **S3** — The reader re-pointed. `read_shell_callers(path, text)` (`TOOL-dRankedPlan-32` S2) takes its
  words from `scan_shell_tokens(text, seps=True)` in place of line joining, splitting and
  `shlex.split`. A command is the run of `word` tokens between two separator `op` tokens. A `$(` opens a
  nested command that ends at its `$)`, and the outer command resumes after it, so `"$py"
  "$d/ratify.py" "$(…)"` stays one command with its script word intact. A word is compared with
  `ratify.py`, an interpreter name or a mode flag with its quote characters stripped. Unit 32 S2's
  two invocation forms, its `NAME=value` skip and its mode-flag rule apply to these commands unchanged.
  This supersedes unit 32 S2's sentences on joining, splitting and `shlex.split`. Observed by AC2.
- **S4** — The error rule. When the tokenizer raises `SyntaxError` on a shell file the check reads, the
  check prints `ratify — <path>:<line> cannot be tokenized: <reason>` and exits 2. The line is the one
  the tokenizer's message names. The file is never skipped and never read in part. This answers unit 32
  §5's error states for shell, which named only a Python file. Observed by AC3.
- **S5** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC2 and AC3.
  - `caller-shell-subst` plants a `.githooks/pre-commit` holding `"$py" "$d/ratify.py" "$(printf '%s'
    "$slug")"`, whose substitution is quoted and carries apostrophes. It is refused with exit 1.
  - `caller-shell-unterminated` plants a `.githooks/pre-commit` whose invocation line `"$py"
    "$d/ratify.py" "$slug` never closes its quote. The check exits 2 naming the file and the line.

## 3. Non-goals (OUT)

- Which leading words the reader skips: `TOOL-dRankedPlan-39` and `TOOL-dRankedPlan-40`, whose rules
  are stated over a command's words and read these commands unchanged.
- The textual rule for a line naming the predicate: `TOOL-dRankedPlan-38`. It reads raw lines and needs
  no tokenizer.
- A textual prefilter, so a shell file naming neither `ratify.py` nor the predicate is never
  tokenized, and its unbalanced-quote plant (finding 13): `TOOL-dRankedPlan-45`'s item.
- The JavaScript reader's tokenizer, `scan_ts_tokens`, and the heredoc body (findings 20 and 14):
  `TOOL-dRankedPlan-45`'s items.
- Moving the tokenizer. Its home is TOOL-dTotalRecall-13's, read here and extended by one keyword.

### Edges

- **consumes-from** `TOOL-dRankedPlan-32` — `read_shell_callers` and S2's invocation forms, whose tokenizing S3 re-points; without them there is no reader to feed
- **consumes-from** external — dTotalRecall's `tools/lib/extract_code.py`, its `scan_shell_tokens` and its parity row (TOOL-dTotalRecall-13 S1, S3), built before this build run
- **hands-off** `TOOL-dRankedPlan-45` — S1's separators mode and S4's error rule, over which that unit's items for findings 13, 14 and 20 add the prefilter, the heredoc reading and the JavaScript tokenizer
- **hands-off** `TOOL-dRankedPlan-49` — S3's commands and words, over which that unit collects the shell assignments a `$name` script word resolves through (spec audit of units 38 to 45, id 33)
- **hands-off** `TOOL-dRankedPlan-51` — S3's command model, whose boundary that unit widens to the op tokens `(`, `)`, `{` and `}` (spec audit of units 38 to 45, id 35)
- **hands-off** `TOOL-dRankedPlan-52` — the separators mode, the copies, Files touched and §7, which that unit's items for findings 5, 9, 11, 23, 24 and 25 extend or correct; carry S6, S9, S10 and S16 into this unit's pass (spec audit of units 38 to 45, ids 5, 9, 11, 23, 24, 25)

## 4. Design

### Evidence

- `scan_shell_tokens` (`tools/lexicon/lexicon.py:469` at base, moved verbatim to
  `tools/lib/extract_code.py` by TOOL-dTotalRecall-13 S1) tracks single and double quotes, `$'…'`,
  continuations, `#` comments, `${…}`, `$((…))`, backticks, heredocs and here-strings. It reads `$(…)`
  as code with its own nesting even inside a double-quoted string (:589-600), and raises `SyntaxError`
  naming the construct and its line rather than return a partial list (:489-492).
- Today it swallows `;`, `&` and `|` as word breaks (:728-732) and emits only `( ) { }` as `op`, which
  is why the reader needs S1's mode.
- TOOL-dTotalRecall-13 S3 holds every copy of the block byte for byte and finds copies by the marker,
  `git grep -l "^# >>> extract_code" -- '*.py'` (its §4).

### The probe over the tree

The audit's probe ran unit 32 S2's split and `shlex.split` over the tracked shell files. This unit's
probe ran the tokenizer S3 reads over the same population, measured 2026-10-27 at base 0689e7fa with a
scratch probe, so the figures are PINNED.

| Reading | Population | Errors |
|---|---|---|
| unit 32 S2's split and `shlex.split`, pieces naming `gen_build_index.py` | 88 pieces | 14 |
| unit 32 S2's split and `shlex.split`, pieces naming `drift_report.py` | 14 pieces | 2 |
| unit 32 S2's split and `shlex.split`, every line | the 176 files git lists | 6189 lines in 147 files |
| `scan_shell_tokens`, whole file | 175 shell files, every `*.sh` and `.githooks/` file but its one `*.py` | 0 |

The first three rows are the audit's, from its appendix rows for findings 33 and 13. The tokenizer
raises on no tracked file, so S4's exit 2 reds the leg on no file at base, and fires only on a file the
shell itself would refuse to parse.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `seps` | keyword parameter of `scan_shell_tokens` | none |
| `$)` | `op` token text in separators mode | none |
| `tools/loop/extract_code.py` | inline copy of the canonical block | none |
| `caller-shell-subst`, `caller-shell-unterminated` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. Units 38 to 41 share order 8 and all write `tools/loop/ratify.py`, so by
BUILD-METHOD M6 clause 1 they are sequenced inside that step. The kits whose shipped bytes move here
take their version bump from `govkit.py mint` at the lander.

### Files touched (estimate)

- `tools/lib/extract_code.py`: S1
- `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`: S2, the re-synced copies
- `tools/loop/extract_code.py`: S2, the new copy
- `tools/loop/ratify.py`: S3 to S5

### Alternatives rejected

- **A quote-aware splitter inside `ratify.py`.** It would be a second, weaker tokenizer beside the one
  the lexicon and the map are tested against, which is finding 20's defect.
- **Count a piece `shlex` cannot split as a caller when it names `ratify.py`.** It fails closed, but
  it refuses a correct `--exit` call that carries a quoted `$(…)`, and it keeps the split that causes
  the error.
- **Skip an untokenizable file.** It fails open on the one file the reader could not see.

## 5. Production-readiness checklist

- security — deny by default holds through parse failures: a file the reader cannot read reds the leg
  by name.
- perf / scale — one tokenizer pass per shell file the check reads. The tokenizer read all 175 files
  in the probe above.
- error / empty / loading states — S4's exit 2 and its line.
- observability — the exit-2 line names the file, the line and the tokenizer's reason.
- risks — the default token stream is a contract of `parse_shell_defs` and the map's shell layer. S1
  leaves it unchanged, and the lexicon and codebase-map selftests read it.
- testing — the two plants, AC1's token probe, and the parity row over the copies.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a probe calls `scan_shell_tokens` from the loop kit's `extract_code.py` with
  `seps=True` on the line `"$py" "$d/ratify.py" "$(printf '%s' "$slug")"; echo done` and its
  newline, the `op` tokens are
  `$(`, `$)`, `;` and `\n` in that order, and with `seps=False` the stream holds no `op` token.
  Red when: a separator is swallowed in separators mode, or the default stream changes.
- **AC2** — When `python ratify.py --fixture --plant caller-shell-subst` runs, the check exits 1 naming
  `.githooks/pre-commit` and the invocation line.
  Red when: an invocation carrying a quoted substitution is skipped or crashes the check.
- **AC3** — When the plant `caller-shell-unterminated` runs, the check exits 2 and prints `cannot be
  tokenized` with `.githooks/pre-commit` and the line.
  Red when: an untokenizable hook is skipped, or the check exits 0.
- **AC4** — When `git grep -l "^# >>> extract_code" -- '*.py'` runs at this unit's tip, it lists the
  loop kit's `extract_code.py` beside the other copies, and `cmp` of each copy's block with the
  canonical block reports no difference.
  Red when: the loop kit imports the tokenizer from another kit, or a copy drifts.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC2 AC3 · the `caller-shell-subst` and `caller-shell-unterminated` plants, staged by a reader that splits at `$(` before tokenizing and skips a piece that raises · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 33 (HIGH,
  item H3; finding 13 is its medium face), repairing `TOOL-dRankedPlan-32`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-49`, the hands-off edge to `TOOL-dRankedPlan-51`, the hands-off edge to `TOOL-dRankedPlan-52`, each the reciprocal of that promoted unit's own edge (spec audit of units 38 to 45, `reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `scan_shell_tokens`, today `tools/lexicon/lexicon.py:469` and, once
TOOL-dTotalRecall-13 lands, the canonical block in `tools/lib/extract_code.py` with one inline copy per
kit. It is extended by one opt-in keyword, so its current callers keep their stream. `python
tools/codebase-map/reuse_lookup.py "tokenize shell source into commands and words with quotes and
command substitution"` ranked `parse_shell_defs`, the tokenizer's own caller, and the recall query
returned TOOL-dTotalRecall-13's move of the tokenizer into `tools/lib`, which is where this unit
extends it. The two agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader find a script invocation behind if exec or a case arm" --terms "shell tokenizer scan_shell_tokens invocation reserved word exec case pattern heredoc shlex caller predicate"`
