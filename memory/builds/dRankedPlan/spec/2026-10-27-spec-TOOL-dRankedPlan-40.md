# TOOL-dRankedPlan-40 — a command led by a prefix command or a case-arm pattern is read past it

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-40-deviation-401.md](../build/2026-10-27-build-TOOL-dRankedPlan-40-deviation-401.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) | spec-audit | TOOL-dRankedPlan-43 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-41 TOOL-dRankedPlan-44 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 30 to 37
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`) confirmed
**finding 34 at HIGH**, item **H2**, which it shares with finding 2. `TOOL-dRankedPlan-32` S2 takes a
command's first word, after `NAME=value` words, as its command word. In `exec "$py" "$d/ratify.py"
"$@"` that word is `exec`, and in the case arm `--x) exec "$py" …` it is `--x)`, because `(` is a split
character and `)` is not. The tree writes both shapes, at `tools/memory-tree/merge-rows.sh:60` and
`tools/run-gates/run-gates.sh:224`. So a hook wrapping the predicate's CLI behind `exec`, or in a case
arm, passes the tree-wide ban. This unit skips the prefix commands and a leading case-arm pattern
before the command word is read. Finding 2, the compound-command reserved words of the same item, is
`TOOL-dRankedPlan-39`'s. This unit repairs `TOOL-dRankedPlan-32`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The prefix commands. `SHELL_PREFIX_COMMANDS = ("exec", "command", "time", "env", "nohup")`
  in `tools/loop/ratify.py`. `read_shell_callers` (`TOOL-dRankedPlan-32` S2) skips a leading word in
  this set together with the words that belong to it: every following word that begins `-`, and, after
  `env`, every following `NAME=value` word. It then reads the next word as the command word, and unit
  32 S2's invocation forms and mode-flag rule apply unchanged. Observed by AC1 and AC3.
- **S2** — The case-arm pattern. When a command's leading words run up to a word ending in an
  unquoted `)`, or up to a `)` token, before any word that is an interpreter or ends in `.py`, those
  words are the arm's pattern and are skipped. The command word is read after them. Observed by AC2.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-exec` plants a `.githooks/pre-commit` ending `exec "$py" "$d/ratify.py" "$@"`. It is
    refused.
  - `caller-shell-case` plants a `case "$1" in` block whose arm reads `--ask) exec "$py"
    "$d/ratify.py" "$slug" ;;`. It is refused.
  - `caller-shell-exec-exit` plants `exec "$py" "$d/ratify.py" "$slug" --exit`. It is admitted.

## 3. Non-goals (OUT)

- The reserved words `if`, `!`, `then` and the rest: `TOOL-dRankedPlan-39`.
- The textual rule for a line naming the predicate: `TOOL-dRankedPlan-38`.
- The tokenizer and its error rule: `TOOL-dRankedPlan-41`. S1 and S2 are stated over the words of a
  command, whichever tokenizer yields them.
- `sudo`, `xargs`, `nice` and other wrappers. No tracked shell file runs a kit script behind one, and a
  wrapper outside the set leaves its command unread, which §4 records as the reader's ceiling.

### Edges

- **consumes-from** `TOOL-dRankedPlan-32` — `read_shell_callers` and S2's command-word rule, which S1 and S2 read past the prefix and the pattern; without it there is no command word to find
- **hands-off** `TOOL-dRankedPlan-50` — S1's prefix skip and §3's wrapper non-goal, after which that unit reads `timeout` and same-file `$@` wrapper functions, and whose premise it corrects (spec audit of units 38 to 45, id 34)
- **hands-off** `TOOL-dRankedPlan-51` — S2's case-arm rule and the `caller-shell-case` plant, which that unit restates over the `)` op (spec audit of units 38 to 45, id 35)
- **hands-off** `TOOL-dRankedPlan-52` — `SHELL_PREFIX_COMMANDS`, S1's skip and §10, which that unit's items for findings 2, 12 and 19 probe, give an option table and correct; carry S20 into this unit's pass (spec audit of units 38 to 45, ids 2, 12, 19)

## 4. Design

### Evidence

- `tools/memory-tree/merge-rows.sh:60` reads `exec "$PY" "$HERE/merge-rows.py" "$@"`.
- `tools/run-gates/run-gates.sh:224` reads `--regen)       exec "$PYBIN" "$KITDIR/regen.py" --write
  ;;`.
- A scratch probe over the 175 tracked shell files, every `*.sh` and every `.githooks/` file but its one
  `*.py`, run 2026-10-27 at base 0689e7fa, counted the leading words before an interpreter word running
  a `*.py` script: `exec` 5 and a case-arm pattern 3. It found none of `command`, `time`, `env` or
  `nohup` there. The counts are PINNED. The three unused words stay in the set because each runs its
  next word as the command, so leaving one out would be a known hole in a deny-by-default ban.

### The reading after this unit

| Command | Command word |
|---|---|
| `exec "$py" "$d/ratify.py" "$@"` | `"$py"`, an interpreter, so an invocation |
| `env PYTHONPATH=x "$py" "$d/ratify.py" "$slug"` | `"$py"` |
| `command -v python3` | `python3`, with no later word ending `ratify.py`, so not an invocation |
| `--ask) exec "$py" "$d/ratify.py" "$slug" ;;` | `"$py"` |
| `sudo "$py" "$d/ratify.py" "$slug"` | `sudo`, so unread, the ceiling below |

The ceiling is a closed set: a wrapper outside it leaves its command unread. The upgrade is a word added
to `SHELL_PREFIX_COMMANDS` with its plant, once the tree uses one.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SHELL_PREFIX_COMMANDS` | constant, `tools/loop/ratify.py` | none declared |
| `caller-shell-exec`, `caller-shell-case`, `caller-shell-exec-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. Units 38 to 41 share order 8 and all write `tools/loop/ratify.py`, so by
BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Split commands at `)` as well as `(`.** A `)` also closes a subshell and a `$(` substitution, so a
  split there would cut `"$(…)"` arguments apart, which is finding 33's class.

## 5. Production-readiness checklist

- security — narrows: a wrapped or case-arm call to the predicate's CLI is refused.
- perf / scale — one set test per leading word.
- error / empty / loading states — a command made only of a prefix and its flags, such as `exec
  >log`, has no command word and is not an invocation.
- observability — the refusal names the file and the command's first line.
- risks — the wrapper ceiling in §4, named rather than left implicit.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-exec` runs, the check exits 1 naming
  `.githooks/pre-commit` and the `exec` line.
  Red when: an `exec`-wrapped call to the predicate's CLI passes.
- **AC2** — When the plant `caller-shell-case` runs, the check exits 1 naming the arm's line.
  Red when: a case-arm pattern is read as the command word.
- **AC3** — When the plant `caller-shell-exec-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: an `exec`-wrapped `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the `caller-shell-exec`, `caller-shell-case` and `caller-shell-exec-exit` plants, staged by a reader that takes `exec` or `--ask)` as the command word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 30 to 37, finding 34 (HIGH,
  item H2, shared with finding 2), repairing `TOOL-dRankedPlan-32`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-50`, the hands-off edge to `TOOL-dRankedPlan-51`, the hands-off edge to `TOOL-dRankedPlan-52`, each the reciprocal of that promoted unit's own edge (spec audit of units 38 to 45, `reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-32`'s `read_shell_callers`, which gains a second skip set beside
`TOOL-dRankedPlan-39`'s. `python tools/codebase-map/reuse_lookup.py "tokenize shell source into
commands and words with quotes and command substitution"` ranked `resolve_shell_argv`
(`tools/govkit/govkit.py:1200`), which rewrites a leading `bash` and reads no prefix command, so no
seam fits beyond unit 32's reader. The recall query returned this audit's H2 item, whose fix lists the
same words, and they agree with the probe.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader find a script invocation behind if exec or a case arm" --terms "shell tokenizer scan_shell_tokens invocation reserved word exec case pattern heredoc shlex caller predicate"`
