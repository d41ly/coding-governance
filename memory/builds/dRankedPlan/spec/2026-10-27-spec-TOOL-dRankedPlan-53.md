# TOOL-dRankedPlan-53 — an expanded heredoc body fed to a shell is read by the shell reader, with the textual line rule beside it

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-53-deviation-531.md](../build/2026-10-27-build-TOOL-dRankedPlan-53-deviation-531.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-59 TOOL-dRankedPlan-55 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-60 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 3 at HIGH**, item **H1**, which it shares with finding 23. `TOOL-dRankedPlan-52` S13 gives a
reading rule for a `heredoc-expanded` body only when `TOOL-dRankedPlan-47` S1 routes it to Python, and
says nothing of an expanded body whose command word is a shell. An unquoted `bash <<EOF` body running
`"$py" "$d/ratify.py" "$slug"` then has no stated reader, and `TOOL-dRankedPlan-38`'s textual rule,
which matches the predicate's name only, passes it through the deny-by-default ban. This unit states
the shell arm for an expanded body. Finding 23, the router's selection of both kinds, is
`TOOL-dRankedPlan-54`'s. This unit repairs `TOOL-dRankedPlan-52`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The shell arm over an expanded body. A `heredoc-expanded` body whose command word, read as
  `TOOL-dRankedPlan-46` S1 reads one, is in `SHELL_BODY_WORDS` is read by `read_shell_callers` as
  `TOOL-dRankedPlan-46` S1 reads a quoted one, with `TOOL-dRankedPlan-38`'s textual rule beside it.
  `TOOL-dRankedPlan-52` S13's textual line rule also applies to each of its lines, because the outer
  shell expands the body before `bash` reads it, so a line's words are not the words `bash` runs. The
  body is refused when any of the three reads a caller. This supersedes the silence of unit 52 S13 on a
  shell-fed expanded body, and its §4 table row for `heredoc-expanded` reads "a body, by its delimiter's
  quoting, routed by its command word". Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-heredoc-shell-unquoted` plants a `.githooks/pre-commit` feeding `bash <<EOF` a body whose
    one line is `"$py" "$d/ratify.py" "$slug"`. It is refused with exit 1.
  - `caller-heredoc-shell-unquoted-exit` plants the same body with `--exit` after `"$slug"`. It is
    admitted.

## 3. Non-goals (OUT)

- The router's selection of both heredoc kinds (finding 23, the same item): `TOOL-dRankedPlan-54`.
- A `$name` in an expanded body bound in the enclosing file: `TOOL-dRankedPlan-55`.
- `bash -c` and `bash <<<`: `TOOL-dRankedPlan-56`.
- An expanded body fed to Python: `TOOL-dRankedPlan-52` S13, unchanged.

### Edges

- **consumes-from** `TOOL-dRankedPlan-54` — `HEREDOC_KINDS` and the router's membership test, without which an expanded body never reaches S1
- **consumes-from** `TOOL-dRankedPlan-52` — S13's `heredoc-expanded` kind and its textual line rule, which S1 applies to a shell-fed body
- **consumes-from** `TOOL-dRankedPlan-46` — `SHELL_BODY_WORDS` and the shell arm's command-word reading, which S1 extends to the expanded kind
- **hands-off** `TOOL-dRankedPlan-66` — S1's expansion reading and the line rule beside the shell reader, which that unit extends to a command word in neither class (spec audit of units 53 to 62, id 31)
- **hands-off** `TOOL-dRankedPlan-67` — S1's arm, its plants, its `New arm:` line and §4 Evidence, which that unit's items for findings 8 and 20 complete and re-cite; carry S11 and S28 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-52` S13 (its lines 121-129) reads: "A body `TOOL-dRankedPlan-47` S1 routes to
  Python is read, when it is `heredoc-expanded`, by the textual rules only". No sentence of unit 52
  names a shell-fed expanded body.
- `TOOL-dRankedPlan-46` S3's three plants each use `<<'EOF'`, a quoted delimiter.
- `git grep -nE '(^|[ ;(|$])(bash|sh)( -[a-z]+)* <<[^<]' -- '*.sh' '.githooks/*'`, run 2026-10-27 at
  base 0689e7fa, printed nothing. The count is PINNED. The arm guards a form the tree does not write
  yet, in a deny-by-default ban.

### The reading after this unit

| Hook lines | Kind | Readers | Answer |
|---|---|---|---|
| `bash <<EOF`, body `"$py" "$d/ratify.py" "$slug"` | `heredoc-expanded` | shell reader, name rule, line rule | caller |
| the same body with `--exit` | `heredoc-expanded` | the same | not a caller |
| `bash <<'EOF'`, the same body | `heredoc` | shell reader, name rule | caller, by `TOOL-dRankedPlan-46` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-heredoc-shell-unquoted`, `caller-heredoc-shell-unquoted-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 23, after `TOOL-dRankedPlan-54` inside that step, because both write
`tools/loop/ratify.py` and this unit consumes from it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **The textual line rule alone for an expanded shell body.** A shell-fed body is shell source that
  the shell reader already reads, and the line rule sees no mode flag on a continued line, so the
  shell reader is the primary reading and the line rule is the expansion's fail-closed addition.

## 5. Production-readiness checklist

- security — narrows: an unquoted shell-fed body that runs the predicate's CLI is refused.
- perf / scale — one more line pass per expanded shell body. The tree holds none at base.
- error / empty / loading states — a body the shell tokenizer cannot read exits 2, as
  `TOOL-dRankedPlan-41` S4 states for a file.
- observability — the refusal names the hook and the body's line.
- risks — an expanded body whose line names `ratify.py` for a non-executing purpose is refused, which
  fails closed.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-heredoc-shell-unquoted` runs, the check
  exits 1 naming `.githooks/pre-commit`.
  Red when: an expanded shell-fed body gets the textual rules of unit 52 S13's Python arm only, and
  passes.
- **AC2** — When the plant `caller-heredoc-shell-unquoted-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: an expanded body's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · the two `caller-heredoc-shell-unquoted*` plants, staged by a router that sends every `heredoc-expanded` body to unit 52 S13's textual rules whatever its command word · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 3 (HIGH,
  item H1, shared with finding 23), repairing `TOOL-dRankedPlan-52`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-66`, the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-46` S1's shell arm, reached through `TOOL-dRankedPlan-54`'s kind
set, and `TOOL-dRankedPlan-52` S13's line rule, applied beside it. `python
tools/codebase-map/reuse_lookup.py "route a heredoc body to a reader by its token kind and command
word"`, run 2026-10-27, ranked name stems only (`read`, `read_text`, `resolve_prefix_token`), so no
existing seam fits beyond the router and the two readers. The recall query returned units 38, 41, 45
to 47, 49, 51 and 52 and this audit's H1 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check route a heredoc body by its delimiter quoting and command word" --terms "heredoc expanded quoted delimiter kind router shell interpreter body reader textual rule caller ratify"`
