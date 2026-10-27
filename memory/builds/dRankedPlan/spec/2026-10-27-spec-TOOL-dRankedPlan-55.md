# TOOL-dRankedPlan-55 — a shell-fed heredoc body resolves a bound name against the enclosing file's bindings

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 22 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-55-deviation-551.md](../build/2026-10-27-build-TOOL-dRankedPlan-55-deviation-551.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-59 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-60 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 32 at HIGH**, item **H2**. `TOOL-dRankedPlan-46` S1 reads a shell-fed body "as a file of its
own", and `TOOL-dRankedPlan-49` S1 collects bindings "in the file", so an assignment written before the
heredoc never reaches the body. With an unquoted delimiter the outer shell expands `$r` before `bash`
runs the body, and an exported `r` is visible to the child under a quoted one. So `r="$d/ratify.py"`
followed by `bash <<EOF` holding `"$py" "$r" "$slug"` passes the deny-by-default ban, and so does
`export r=…` with `<<'EOF'`. This unit resolves a body's `$name` words against the enclosing file's
bindings as well as the body's own. It repairs `TOOL-dRankedPlan-46`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The inherited bindings. When `read_shell_callers` reads a heredoc body that
  `TOOL-dRankedPlan-46` S1 hands it, the bindings `TOOL-dRankedPlan-49` S1 collects over the enclosing
  file join the body's own before `TOOL-dRankedPlan-49` S2 resolves a `$name` or `${name}` word in the
  body. Both delimiter kinds inherit, and an unexported binding counts under a quoted delimiter too,
  because the file-wide reading fails closed. The body's commands stay its own: only bindings cross the
  boundary. This supersedes unit 46 S1's "as a file of its own" for bindings, and nothing else in it.
  Observed by AC1, AC2 and AC3.
- **S2** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-heredoc-shell-bound` plants a `.githooks/pre-commit` holding `r="$d/ratify.py"` and then
    `bash <<EOF` with the body `"$py" "$r" "$slug"`. It is refused.
  - `caller-heredoc-shell-export` plants `export r="$d/ratify.py"` and then `bash <<'EOF'` with the
    same body. It is refused.
  - `caller-heredoc-shell-bound-exit` plants `caller-heredoc-shell-bound` with `--exit` after
    `"$slug"`. It is admitted.

## 3. Non-goals (OUT)

- A body fed to Python. Its `$name` words are expanded shell text, not Python names, and
  `TOOL-dRankedPlan-52` S13 reads an expanded Python-fed body textually.
- A binding in another file the hook sources: run-time assembly, unread as `TOOL-dRankedPlan-49` §3
  states.
- The `-c` and here-string carriers: `TOOL-dRankedPlan-56`, which reads them with S1's bindings.

### Edges

- **consumes-from** `TOOL-dRankedPlan-46` — S1's shell arm, whose body reading S1 gives the enclosing bindings; without it no body reaches the shell reader
- **consumes-from** `TOOL-dRankedPlan-49` — S1's file-wide bindings and S2's resolution, which S1 carries into a body
- **hands-off** `TOOL-dRankedPlan-56` — the inherited bindings, with which that unit reads a `bash -c` word and a here-string
- **hands-off** `TOOL-dRankedPlan-66` — the inherited bindings, which that unit gives each command substitution of an expanded body (spec audit of units 53 to 62, id 31)
- **hands-off** `TOOL-dRankedPlan-67` — §3 and §4 Evidence, which that unit's items for findings 35 and 20 amend and re-cite; carry S14 and S28 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-46` S1 (its lines 30-36) reads the body "by `read_shell_callers` as a file of its
  own", and `TOOL-dRankedPlan-49` S1 (its lines 31-34) collects "every assignment word `NAME=value` in
  the file".
- `scan_shell_tokens('bash <<EOF\n"$py" "$r" "$slug"\nEOF\n')`, run 2026-10-27 at base 0689e7fa from
  `tools/lexicon/lexicon.py`, printed `[('word', 'bash', 1)]`: the body is consumed apart from the
  file's words, so its reader starts with no bindings unless they are passed. The output is PINNED.

### The reading after this unit

| Enclosing file | Body | Answer |
|---|---|---|
| `r="$d/ratify.py"`, `bash <<EOF` | `"$py" "$r" "$slug"` | caller |
| `export r="$d/ratify.py"`, `bash <<'EOF'` | the same | caller |
| `r="$d/ratify.py"`, `bash <<'EOF'` | the same | caller, failing closed: the child sees no `r` |
| `r="$d/ratify.py"`, `bash <<EOF` | the same with `--exit` | not a caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-shell-bound`, `caller-heredoc-shell-export`, `caller-heredoc-shell-bound-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 22. Units 52, 55, 57, 58 and 60 share order 22 and all write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside that step. The
unquoted plant's body becomes a `heredoc-expanded` token when `TOOL-dRankedPlan-52` lands, and
`TOOL-dRankedPlan-54` routes it at order 23, so this unit builds before unit 52 inside step 22 and the
close re-observes it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Inherit only exported bindings under a quoted delimiter.** It needs a reading of `export`, `set
  -a` and `declare -x` to be right, and a wrong answer fails open. The file-wide rule fails closed on
  the same input, as `TOOL-dRankedPlan-49` §4 chose for the file itself.

## 5. Production-readiness checklist

- security — narrows: a body invoking the predicate's CLI through an outer binding is refused.
- perf / scale — the enclosing file's bindings are collected once and shared by its bodies.
- error / empty / loading states — a body `$name` bound nowhere resolves to nothing, as
  `TOOL-dRankedPlan-49` §5 states.
- observability — the refusal names the hook and the body's line.
- risks — an unexported outer name reused inside a quoted body for another path is refused, which
  fails closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-shell-bound` runs, the check exits
  1 naming `.githooks/pre-commit`.
  Red when: a body resolves `$r` against its own bindings only and passes.
- **AC2** — When the plant `caller-heredoc-shell-export` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: an exported outer binding is not seen under a quoted delimiter.
- **AC3** — When the plant `caller-heredoc-shell-bound-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: an inherited binding's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `caller-heredoc-shell-*` binding plants, staged by a body reader that starts from an empty binding set · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 32 (HIGH,
  item H2), repairing `TOOL-dRankedPlan-46`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-66`, the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-49`'s binding collector and resolution, and
`TOOL-dRankedPlan-46` S1's body reading, which now takes the collector's result as an argument instead
of starting empty. `python tools/codebase-map/reuse_lookup.py "resolve a shell variable bound to a
script path where a command invokes it"`, run 2026-10-27, ranked name stems only (`resolve`,
`resolve_kit_dir`, `resolve_caps`), none of which reads a shell assignment, so no existing seam fits
beyond the two units. `tools/gate-lint/sh_hygiene.py:160-163` holds a sibling assignment pattern,
cited and not imported, because a copy-installed kit imports from no sibling kit. The recall query
returned units 47 to 52 and dWitnessedBar's resolver scouts, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
