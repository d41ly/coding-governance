# TOOL-dRankedPlan-50 — a command run through `timeout` or a same-file `$@` wrapper function is read through its arguments

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 9 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-50-deviation-501.md](../build/2026-10-27-build-TOOL-dRankedPlan-50-deviation-501.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-51 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 34 at HIGH**, item **H4**. `TOOL-dRankedPlan-40` S1 makes the prefix commands a closed set,
`exec command time env nohup`, and its §3 leaves every other wrapper out because "No tracked shell file
runs a kit script behind one". The tree contradicts that: `tools/check-wiring.sh:1941` runs `timeout
60 "$py" "$path"`, and `.githooks/pre-commit:11` defines `with_hook_index() { … "$@"; }` and runs a kit
guard through it at :212. Unit 40's probe missed both because it counted only literal `*.py` script
words. So `timeout 60 "$py" "$d/ratify.py" "$slug"` or `with_hook_index "$py" "$d/ratify.py" "$slug"`
reads `timeout` or `with_hook_index` as the command word and passes the ban. This unit reads both
wrapper kinds through their arguments, corrects unit 40's premise, and re-runs the probe over the
interpreter-plus-variable form. It repairs `TOOL-dRankedPlan-40`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The wrapper call. `SHELL_WRAPPER_COMMANDS = ("timeout",)` in `tools/loop/ratify.py`. A
  command whose command word, read as `TOOL-dRankedPlan-32` S2, `TOOL-dRankedPlan-39` and
  `TOOL-dRankedPlan-40` read it, is in that set or names a wrapper function of S2 is a wrapper call.
  A wrapper call invokes `ratify.py` when one of its argument words ends in `ratify.py` and either
  follows an interpreter word of unit 32 S2's class directly, or is the first argument word that
  neither begins `-` nor is a `timeout` duration. A duration is digits with an optional fraction and
  an optional `s`, `m`, `h` or `d`. Unit 32 S2's mode-flag rule then applies to the call's words.
  Observed by AC1 and AC2.
- **S2** — The wrapper functions. A function the file defines, found by `parse_shell_defs(text)` from
  the loop kit's `extract_code.py`, is a wrapper function when its body holds a word containing `$@`,
  `$*`, `${@` or `${*`. The body is the tokens from the `{` or `(` op that opens it to the op that
  closes it at the same depth. Observed by AC2 and AC3.
- **S3** — The premise corrected. Unit 40 §3's sentence "No tracked shell file runs a kit script
  behind one" is superseded by this unit's §4 "The probe over the tree": `timeout` and same-file `$@`
  functions are read here, and `sudo`, `xargs` and `nice` stay outside, the probe finding none of them
  before an interpreter word. NOT OBSERVED by a criterion: it is a record correction, and the plants
  observe the forms it reads.
- **S4** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-timeout` plants a `.githooks/pre-commit` holding `timeout -k 5s 60 "$py"
    "$d/ratify.py" "$slug"`. It is refused.
  - `caller-shell-func-wrapper` plants `with_hook_index() { if [ -n "$h" ]; then GIT_INDEX_FILE=$h
    "$@"; else "$@"; fi; }` and then `with_hook_index "$py" "$d/ratify.py" "$slug"`. It is refused.
  - `caller-shell-func-wrapper-exit` plants the same with `--exit` after `"$slug"`. It is admitted.

## 3. Non-goals (OUT)

- `sudo`, `xargs`, `nice` and a function defined in another file the hook sources. The probe found none
  before an interpreter word, and §4 records them as the ceiling.
- The argument-taking options of unit 40's prefix commands, such as `exec -a NAME` (finding 12):
  `TOOL-dRankedPlan-52`'s item.
- The citation of `tools/runlog/extract.py`'s wrapper set in unit 40 §10 (finding 19):
  `TOOL-dRankedPlan-52`'s item, which agrees with S1.
- Braces, parentheses and function bodies as command boundaries (finding 35): `TOOL-dRankedPlan-51`.
  S2 finds a body by its ops whichever rule ends commands.

### Edges

- **consumes-from** `TOOL-dRankedPlan-40` — S1's prefix skip and §3's wrapper non-goal, which S1 reads after and S3 corrects; without them there is no command word to test
- **hands-off** `TOOL-dRankedPlan-52` — S1's wrapper call and `SHELL_WRAPPER_COMMANDS`, beside which that unit's items for findings 12 and 19 add the prefix commands' option table and record why the prefix set stays narrow
- **hands-off** `TOOL-dRankedPlan-58` — S1's wrapper-call test, which that unit routes through `resolve_ratify_word` (spec audit of units 46 to 52, id 29)
- **hands-off** `TOOL-dRankedPlan-59` — S1's first arm, which that unit restates past the interpreter's options (spec audit of units 46 to 52, id 30)
- **hands-off** `TOOL-dRankedPlan-62` — S1's direct arm, S2, §4, §7 and §10, which that unit's items for findings 9, 17, 20 and 24 plant or correct; carry S6, S11 and S12's `spans` keyword with its copies, Files touched and leg line, of that unit into this unit's pass (spec audit of units 46 to 52)
- **hands-off** `TOOL-dRankedPlan-67` — the `spans` keyword this unit builds, whose close rule that unit's item for finding 37 corrects; carry S20 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `tools/check-wiring.sh:1941` reads `out=$(timeout 60 "$py" "$path" --stragglers --local --tsv
  2>/dev/null); rc=$?`, and `tools/run-gates/run-gates.sh:2315` reads `… timeout -k 5s 60 "$PYBIN"
  "$PROCMON_REAP" \`.
- `.githooks/pre-commit:11` defines `with_hook_index() { if [ -n "$hook_index" ]; then
  GIT_INDEX_FILE=$hook_index "$@"; else "$@"; fi; }`, and :212 runs `elif ! with_hook_index "$py" "$g"
  --staged; then`.
- `tools/unattended/unattended.sh:262` defines `run_bounded() { # argv...`, whose body passes `"$@"` on,
  and :10571 runs `run_bounded "$_py" "$_kd/map_diff.py" …`.
- `tools/runlog/extract.py:479` `_derive_program` skips `timeout N` only when the next word starts with
  a digit, so `timeout -k 5s 60` defeats it, which is why S1 reads adjacency and not position.

### The probe over the tree

A scratch probe over the 175 tracked shell files, every `*.sh` and every `.githooks/` file but its one
`*.py`, run 2026-10-27 at base 0689e7fa, counted the first word before an interpreter word that is
followed by a `*.py` or `$` script word, after unit 39's and unit 40's words and assignment words. The
counts are PINNED.

| Interpreter words counted | Leading words found |
|---|---|
| `python`, `python3`, `py`, and `$py`, `$PY`, `$PYBIN`, `$PYTHON` in any quoting | `timeout` 2; same-file `$@` functions `with_hook_index` 1, `run_bounded` 1 and `run_in` 1; `sudo`, `xargs`, `nice` 0; the rest are prose, `echo` text and test helpers that take a command as one string, such as `run_role_bash` 5 |
| every `$` variable, as unit 32 S2's class reads one | `cp` 99, `rm` 42, `mv` 15, `cmp` 11, and the rows above |

The second row is why S1 reads adjacency only inside a wrapper call: in any other command, a `$`
variable followed by a `ratify.py` path is a file utility's argument list.

### The reading after this unit

| Command | Answer |
|---|---|
| `timeout 60 "$py" "$d/ratify.py" "$slug"` | caller |
| `timeout -k 5s 60 "$d/ratify.py" "$slug"` | caller, the first argument past the options and durations |
| `with_hook_index "$py" "$d/ratify.py" "$slug"` | caller |
| `with_hook_index "$py" "$d/ratify.py" "$slug" --exit` | not a caller |
| `with_hook_index cp "$s" "$d/ratify.py"` | not a caller |
| `sudo "$py" "$d/ratify.py" "$slug"` | unread, the ceiling |

The upgrade is a word added to `SHELL_WRAPPER_COMMANDS` with its plant, once the tree uses one.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SHELL_WRAPPER_COMMANDS` | constant, `tools/loop/ratify.py` | none declared |
| `caller-shell-timeout`, `caller-shell-func-wrapper`, `caller-shell-func-wrapper-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 9. `TOOL-dRankedPlan-51` shares order 9 and also writes
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 the two are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2, S4

### Alternatives rejected

- **Invert the rule to fail closed: any command in which an interpreter word is followed by a word
  ending `ratify.py` is an invocation unless its command word is a named non-executing command.** The
  probe's second row shows that every `cp`, `rm`, `mv` or `cmp` with a variable source and a
  `ratify.py` path would be refused, so an adopter copying the kit's own script reds the always-run
  leg, and the named list grows with every utility. That is the exemption list `TOOL-dRankedPlan-32`
  §4 rejected.
- **Add `timeout` to `SHELL_PREFIX_COMMANDS` with one duration word.** `timeout -k 5s 60` then reads
  `60` as the command word, as runlog's `_derive_program` does.
- **Import runlog's `WRAPPERS`.** It is another kit's reader, and a copy-installed kit carries no
  import from a sibling kit.

## 5. Production-readiness checklist

- security — narrows: the two wrapper shapes the tree already writes are read by the deny-by-default
  ban.
- perf / scale — one `parse_shell_defs` pass and one body walk per shell file the check reads.
- error / empty / loading states — a wrapper call with no argument word ending `ratify.py` is not an
  invocation.
- observability — the refusal names the file and the wrapper call's line.
- risks — a wrapper function whose arguments place a `$` variable directly before a `ratify.py` path
  for a non-executing purpose is refused, which fails closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-timeout` runs, the check exits 1
  naming `.githooks/pre-commit` and the `timeout` line.
  Red when: a call to the predicate's CLI behind `timeout -k 5s 60` passes.
- **AC2** — When the plant `caller-shell-func-wrapper` runs, the check exits 1 naming the
  `with_hook_index "$py"` line.
  Red when: a call through a same-file `$@` function passes.
- **AC3** — When the plant `caller-shell-func-wrapper-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a wrapped `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the `caller-shell-timeout` and two `caller-shell-func-wrapper*` plants, staged by a reader that takes `timeout` or the function's name as the command word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 34 (HIGH,
  item H4), repairing `TOOL-dRankedPlan-40`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-58`, the hands-off edge to `TOOL-dRankedPlan-59`, the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-40`'s command-word reading, which gains a wrapper reading
after it, and `parse_shell_defs`, the shared block's function-definition reader, which finds the
wrapper functions. `tools/runlog/extract.py:89` `WRAPPERS` and `_derive_program` (:479) are the
sibling reader, cited and not imported, for the reasons under Alternatives rejected. `python
tools/codebase-map/reuse_lookup.py "find which command a shell heredoc or wrapper function runs and
read its script argument"` ranked name stems only (`read`, `run`, `run_git`), so no seam fits beyond
those two. The recall query returned units 38, 40 and 41 and this audit's H5 item, and they agree with
the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
