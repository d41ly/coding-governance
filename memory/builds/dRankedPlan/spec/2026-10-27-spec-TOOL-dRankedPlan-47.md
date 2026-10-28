# TOOL-dRankedPlan-47 — a heredoc body fed to a Python interpreter is read by the Python reader, over unit 32's interpreter class

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 21 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-47-deviation-471.md](../build/2026-10-27-build-TOOL-dRankedPlan-47-deviation-471.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-47-deviation-472.md](../build/2026-10-27-build-TOOL-dRankedPlan-47-deviation-472.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-46 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 30 at HIGH**, item **H1**, which it shares with finding 1. `TOOL-dRankedPlan-45` S10 hands a
heredoc body to `read_python_callers` only when the command word is a literal `python`, `python3` or
`py`, and every other body goes to `TOOL-dRankedPlan-38`'s textual rule alone. That rule matches the
predicate's name, not `ratify.py`. The tree's usual shape is a `$` variable, `"$PY" - <<'PYEOF'`, and
S10's own plant `caller-heredoc-argv` feeds `"$py" - <<'EOF'`. So a heredoc'd
`subprocess.run([sys.executable, "ratify.py", slug])` passes the deny-by-default ban, and unit 45 AC8
cannot go red. This unit routes a body by unit 32 S2's interpreter class, `$` variables included.
Finding 1, the shell arm of the same item, is `TOOL-dRankedPlan-46`'s. This unit repairs
`TOOL-dRankedPlan-45`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The Python arm. A heredoc body whose command word, read as `TOOL-dRankedPlan-46` S1 reads it,
  is in `TOOL-dRankedPlan-32` S2's interpreter class, meaning `python`, `python3`, `py` or a `$`
  variable, and is not in `TOOL-dRankedPlan-46`'s `SHELL_BODY_WORDS`, is read by
  `read_python_callers` as a file of its own. Unit 32 S1's textual prefilter applies to the body, so a
  body naming neither `ratify.py` nor `read_plan_ratification` is never parsed. This supersedes unit
  45 S10's "for `python`, `python3` or `py`" and the §4 row "a heredoc body fed to `python`, `python3`
  or `py`" of unit 45's table. Observed by AC1, AC2 and AC3.
- **S2** — The plants. `caller-heredoc-argv` (unit 45 S10, `"$py" - <<'EOF'`) is refused by S1. Two
  cases join `ratify.py --fixture --plant <case>`, each in its own scratch repository laid out from
  `TOOL-dRankedPlan-30`'s anchors, so both arms of the class are observed. Observed by AC1, AC2 and
  AC3.
  - `caller-heredoc-argv-bare` plants a `.githooks/pre-commit` feeding `python3 - "$slug" <<'EOF'`
    the body of `caller-heredoc-argv`. It is refused.
  - `caller-heredoc-argv-exit` plants the `caller-heredoc-argv` body with `"--exit"` as the list's
    last element. It is admitted.

## 3. Non-goals (OUT)

- A body fed to `bash`, `sh` or `$BASH`: `TOOL-dRankedPlan-46` (finding 1, the same item).
- A body that does not parse, which an unquoted delimiter makes likely, and `python -c` and
  here-string sources (findings 31 and 32): `TOOL-dRankedPlan-52`'s items, over S1.
- The file line a refusal inside a body names (finding 36): `TOOL-dRankedPlan-52`'s item.

### Edges

- **consumes-from** `TOOL-dRankedPlan-45` — S10's `heredoc` token, its routing table and the `caller-heredoc-argv` plant, whose Python arm S1 restates; without them no body reaches a reader
- **hands-off** `TOOL-dRankedPlan-52` — S1's Python arm, over which that unit's items for findings 31, 32 and 36 add the unparsable-body rule, the `-c` and `<<<` sources and the body's file line
- **hands-off** `TOOL-dRankedPlan-62` — S1's exclusion, §4, §5 and §7, which that unit's items for findings 15, 16, 18, 19 and 24 rely on or correct; carry S6, S15's §4 and §5 sentences, S21 and S22 of that unit into this unit's pass (spec audit of units 46 to 52)
- **hands-off** `TOOL-dRankedPlan-67` — §4, whose superseded sentence and citation that unit's AC8 and AC23 observe carried; nothing new to carry here beyond unit 62's S15 and S22 (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-45` S10 (its lines 107-114) and the §4 table (lines 256-263) name only the
  literal `python`, `python3` and `py`, and S10's plant feeds `"$py" - <<'EOF'`.
- `TOOL-dRankedPlan-32` S2 counts `python`, `python3`, `py` or a `$` variable such as `"$py"` as an
  interpreter.
- `git grep -nE '"\$\{?(py|PY|PYBIN|PYTHON)\}?" -( |$).*<<'` over `*.sh` and `.githooks/*`, run
  2026-10-27 at base 0689e7fa, printed 30 lines, such as `tools/check-hook-destinations.sh:105`
  `DESTS=$("$PY" - "${SELF_PRE}govkit" <<'PYEOF'`. The same search for a bare `python`, `python3` or
  `py` printed 3, all in `tools/unattended/gate-guard.test.sh` at :417, :427 and :430. The counts are
  PINNED. The `$` form is ten times the literal one.

### The routing after this unit

| The body's command word | Reader |
|---|---|
| `bash`, `sh`, `$BASH` | `read_shell_callers`, by `TOOL-dRankedPlan-46` |
| `python`, `python3`, `py`, any other `$` variable | `read_python_callers`, behind unit 32 S1's prefilter |
| any other word | `TOOL-dRankedPlan-38`'s textual rule only |

A `$` variable that names neither Python nor a shell, such as `"$tool" <<EOF`, is read as Python. That
fails closed on the rare body naming `ratify.py`, and the prefilter keeps every other body unparsed.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-argv-bare`, `caller-heredoc-argv-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 21. Units 46 to 49 share order 21 and all write `tools/loop/ratify.py`, so
by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Name the `$`-fed heredoc as unread.** It is thirty of the thirty-three Python heredocs the two
  searches in §4 found, so the ban would certify an absence over the shape hooks actually write.
- **Route by the variable's name, such as `$py` or `$PYBIN`.** A name list grows with every spelling,
  which is the exemption list unit 32 §4 rejected, and unit 32 S2 already decided the class.

## 5. Production-readiness checklist

- security — narrows: the tree's usual heredoc shape is read by the deny-by-default ban.
- perf / scale — the prefilter parses only bodies naming `ratify.py` or the predicate. None does at
  base.
- error / empty / loading states — a body that fails to parse is `TOOL-dRankedPlan-52`'s item for
  finding 31, and until it lands unit 32 S1's exit 2 applies to the body.
- observability — the refusal names the hook.
- risks — a body fed to a non-Python `$` tool that names `ratify.py` is read as Python, which fails
  closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-argv` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: a `"$py"`-fed body that runs `ratify.py` through an argv list passes.
- **AC2** — When the plant `caller-heredoc-argv-bare` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the literal arm of the class is lost while the `$` arm is added.
- **AC3** — When the plant `caller-heredoc-argv-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a heredoc'd `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · `caller-heredoc-argv`, `caller-heredoc-argv-bare` and `caller-heredoc-argv-exit`, staged by a router that sends only a literal `python`, `python3` or `py` body to the Python reader · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 30 (HIGH,
  item H1, shared with finding 1), repairing `TOOL-dRankedPlan-45`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-45` S10's heredoc routing, which now reads
`TOOL-dRankedPlan-32` S2's interpreter class instead of a second word list, and `read_python_callers`,
which reads the body unchanged. `python tools/codebase-map/reuse_lookup.py "find which command a shell
heredoc or wrapper function runs and read its script argument"` ranked name stems only (`read`, `run`,
`run_git`), so no seam fits beyond unit 45's router and unit 32's reader. The recall query returned
units 38, 40 and 41 and this audit's items, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
