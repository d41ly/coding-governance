# TOOL-dRankedPlan-46 — a heredoc body fed to a shell is read by the shell reader, through its own command-word test

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 21 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-46-deviation-461.md](../build/2026-10-27-build-TOOL-dRankedPlan-46-deviation-461.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 1 at HIGH**, item **H1**, which it shares with finding 30. `TOOL-dRankedPlan-45` S10 sends a
heredoc body to `read_shell_callers` when "that command's word is an interpreter" and the word is
`bash` or `sh`. Unit 32 S2's interpreter class is `python`, `python3`, `py` or a `$` variable, so it
holds neither word, and the shell arm is unreachable as worded. A heredoc'd hook body that runs the
predicate's CLI under `bash` is then read only by `TOOL-dRankedPlan-38`'s textual rule, which matches
the predicate's name and not `ratify.py`. This unit states the shell arm as its own command-word test,
checked before any interpreter test. Finding 30, the Python arm of the same item, is
`TOOL-dRankedPlan-47`'s. This unit repairs `TOOL-dRankedPlan-45`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The shell words. `SHELL_BODY_WORDS = ("bash", "sh", "$BASH")` in `tools/loop/ratify.py`.
  A heredoc body's command is the command its `<<` belongs to, and its command word is read as
  `TOOL-dRankedPlan-32` S2, `TOOL-dRankedPlan-39`, `TOOL-dRankedPlan-40` and `TOOL-dRankedPlan-50`
  read one. That word is compared with its quote characters stripped and `${name}` respelled `$name`,
  and the last path segment of a literal path is compared, so `/bin/bash` matches `bash`. When it is
  in `SHELL_BODY_WORDS`, the body is read by `read_shell_callers` as a file of its own, with
  `TOOL-dRankedPlan-38`'s textual rule beside it. Observed by AC1, AC2 and AC3.
- **S2** — The order of the tests. S1's test runs before `TOOL-dRankedPlan-47`'s interpreter test, so
  `"$BASH"`, a `$` variable, reaches the shell reader and never the Python one. This supersedes the
  clause of unit 45 S10 that reads "by `read_shell_callers` for `bash` or `sh`", and the §4 row "a
  heredoc body fed to `bash` or `sh`" of unit 45's table "File kinds and readers". Observed by AC2.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-heredoc-shell` plants a `.githooks/pre-commit` feeding `bash <<'EOF'` a body whose one
    line is `"$py" "$d/ratify.py" "$slug"`. It is refused.
  - `caller-heredoc-shell-var` plants the same body fed to `"$BASH" -s <<'EOF'`, a line that names
    `ratify.py`, so unit 32 S1's prefilter would parse it as Python. It is refused by the shell reader
    with exit 1.
  - `caller-heredoc-shell-exit` plants the `caller-heredoc-shell` body with `--exit` after
    `"$slug"`. It is admitted.

## 3. Non-goals (OUT)

- A body fed to a Python interpreter, `$py` and the bare `python3` included: `TOOL-dRankedPlan-47`
  (finding 30, the same item).
- A body that does not parse, `python -c` and here-strings (findings 31 and 32), and the mapping of a
  body line to a file line (finding 36): `TOOL-dRankedPlan-52`'s items.
- `zsh`, `dash` and other shells. No tracked shell file feeds a heredoc to any shell (§4), and a
  shell outside the set reaches the textual rule only, which §4 records as the ceiling.

### Edges

- **consumes-from** `TOOL-dRankedPlan-45` — S10's `heredoc` token and its routing table, whose shell arm S1 and S2 restate; without them no body reaches a reader
- **hands-off** `TOOL-dRankedPlan-52` — `SHELL_BODY_WORDS`, whose members that unit's item for finding 2 probes as `word` tokens
- **hands-off** `TOOL-dRankedPlan-53` — `SHELL_BODY_WORDS` and S1's shell arm, which that unit extends to a `heredoc-expanded` body (spec audit of units 46 to 52, id 3)
- **hands-off** `TOOL-dRankedPlan-55` — S1's body reading, which that unit gives the enclosing file's bindings (spec audit of units 46 to 52, id 32)
- **hands-off** `TOOL-dRankedPlan-56` — `SHELL_BODY_WORDS` and the shell arm, over which that unit reads a `bash -c` word and a here-string (spec audit of units 46 to 52, id 27)
- **hands-off** `TOOL-dRankedPlan-62` — S1's normalizations, S2, AC2, §4 Evidence, §7 and the `New arm:` line, which that unit's items for findings 10, 15, 16, 19, 24 and 33 plant or correct; carry S6, S14, S15's AC2 Red-when, S19 and S22 of that unit into this unit's pass (spec audit of units 46 to 52)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-45` S10 (its lines 107-114) and its §4 table "File kinds and readers" (lines
  256-263) route by "that command's word is an interpreter", then name `bash` or `sh`.
- `TOOL-dRankedPlan-32` S2 defines an interpreter as `python`, `python3`, `py` or a `$` variable.
- `git grep -nE '(^|[ ;(|$])(bash|sh)( -[a-z]+)*( [^ ]+)* <<'` over `*.sh` and `.githooks/*`, run
  2026-10-27 at base 0689e7fa, printed two lines, `.githooks/pre-push.test.sh:2124` and one record
  script, each a `<<<` here-string and neither a heredoc. A `$BASH`-fed heredoc printed none. The
  counts are PINNED. The arm guards a form the tree does not write yet, in a deny-by-default ban.

### The routing after this unit

| The body's command word | Reader |
|---|---|
| `bash`, `sh`, `$BASH`, `${BASH}`, `/bin/bash` | `read_shell_callers`, with `TOOL-dRankedPlan-38`'s textual rule |
| `python`, `python3`, `py`, any other `$` variable | `read_python_callers`, by `TOOL-dRankedPlan-47` |
| any other word | `TOOL-dRankedPlan-38`'s textual rule only |

The ceiling is the closed set: a body fed to a shell outside it is read by the textual rule only. The
upgrade is a word added to `SHELL_BODY_WORDS` with its plant.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SHELL_BODY_WORDS` | constant, `tools/loop/ratify.py` | none declared |
| `caller-heredoc-shell`, `caller-heredoc-shell-var`, `caller-heredoc-shell-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 21. Units 46 to 49 share order 21 and all write `tools/loop/ratify.py`, so
by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Add `bash` and `sh` to unit 32 S2's interpreter class.** Unit 32 S2 then reads `bash
  "$d/ratify.py"` as running a script through bash, which is wrong for a Python script and changes
  the reading of every shell command, not only of heredoc bodies.

## 5. Production-readiness checklist

- security — narrows: a shell body that runs the predicate's CLI is refused by the deny-by-default ban.
- perf / scale — one set test per heredoc body. The tree holds no shell-fed heredoc at base.
- error / empty / loading states — a body the shell tokenizer cannot read exits 2 as
  `TOOL-dRankedPlan-41` S4 states for a file.
- observability — the refusal names the hook and the body's line.
- risks — none beyond the ceiling in §4.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-shell` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: a `bash`-fed body that runs the predicate's CLI passes.
- **AC2** — When the plant `caller-heredoc-shell-var` runs, the check exits 1, never 2, naming
  `.githooks/pre-commit`.
  Red when: a `"$BASH"`-fed body reaches the Python reader, which exits 2 on shell source
  (`TOOL-dRankedPlan-32` S1), or passes.
- **AC3** — When the plant `caller-heredoc-shell-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a shell body's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `caller-heredoc-shell*` plants, staged by a router that tests the interpreter class before the shell words · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 1 (HIGH,
  item H1, shared with finding 30), repairing `TOOL-dRankedPlan-45`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-53`, the hands-off edge to `TOOL-dRankedPlan-55`, the hands-off edge to `TOOL-dRankedPlan-56`, the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-45` S10's heredoc routing, over `TOOL-dRankedPlan-32`'s
`read_shell_callers`, which reads the body. `tools/runlog/extract.py:90` already holds an
`INTERPRETERS` set naming `bash` and `sh`, but it serves the run log's program reader in another kit,
and a copy-installed kit carries no import from a sibling kit, so it is cited and not imported.
`python tools/codebase-map/reuse_lookup.py "find which command a shell heredoc or wrapper function
runs and read its script argument"` ranked name stems only (`read`, `run`, `run_git`), so no seam fits
beyond unit 45's router. The recall query returned units 38, 40 and 41 and this audit's H5 item, and
they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
