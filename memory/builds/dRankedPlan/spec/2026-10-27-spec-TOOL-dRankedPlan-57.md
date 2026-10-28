# TOOL-dRankedPlan-57 — a shell assignment whose value is a command substitution binds the words inside it

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 22 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-57-deviation-571.md](../build/2026-10-27-build-TOOL-dRankedPlan-57-deviation-571.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) | spec-audit | TOOL-dRankedPlan-59 TOOL-dRankedPlan-55 TOOL-dRankedPlan-58 TOOL-dRankedPlan-60 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-56 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 28 at HIGH**, item **H4**. `TOOL-dRankedPlan-49` S1 and S2 compare a literal assignment value
with `ratify.py` and never say what the value of `g=$(…)` is. Under `TOOL-dRankedPlan-52` S7 the outer
word rebuilds as `g=$()`, which does not end in `ratify.py`, and unit 49 §3 excludes only a substitution
"whose text does not end in `ratify.py`", which leaves this form in scope and unread. So `if
g=$(resolve_kit_gate loop ratify.py); then "$py" "$g" "$slug"; fi` passes the deny-by-default ban, and
that is the bound shape the repository's own hooks write. This unit binds a substitution's inner words
to the name. It repairs `TOOL-dRankedPlan-49`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The substitution value. `TOOL-dRankedPlan-49` S1's collector reads an assignment word as
  `TOOL-dRankedPlan-52` S7 rebuilds a `$(`-interrupted word, so `g=$(…)` arrives as one assignment whose
  value holds `$()`. Each `$()` in a value stands for its nested span, and that span's words, at every
  nesting depth, are part of the value. The value names `ratify.py` when one of those words ends in
  `ratify.py` with its quote characters stripped, as well as when the value itself does. Then
  `TOOL-dRankedPlan-49` S2 resolves `$g` as it resolves a literal value. The assignment is read after
  `TOOL-dRankedPlan-39`'s and `TOOL-dRankedPlan-40`'s leading words, so `if g=$(…)` binds `g`. This
  narrows unit 49 §3's first bullet to a substitution none of whose words names `ratify.py`. Observed
  by AC1, AC2 and AC3.
- **S2** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-bound-resolver` plants a `.githooks/pre-commit` holding `if g=$(resolve_kit_gate loop
    ratify.py); then "$py" "$g" "$slug"; fi`. It is refused.
  - `caller-shell-bound-resolver-exit` plants the same with `--exit` after `"$slug"`. It is admitted.
  - `caller-shell-bound-resolver-other` plants the tree's own shape, `if g=$(resolve_kit_gate loop
    guard.py); then "$py" "$g" --staged; fi`. It is admitted.

## 3. Non-goals (OUT)

- A value assembled from a variable the substitution prints, such as `g=$(cat "$listfile")`: run-time
  assembly, unread as `TOOL-dRankedPlan-32` §3 states.
- A literal tail after a substitution, `r="$(dirname "$0")/ratify.py"`: `TOOL-dRankedPlan-62`'s item
  for finding 12, over S1's rebuilt-word reading.
- The resolver call itself as a command: `TOOL-dRankedPlan-41` S3 reads it as a nested command whose
  command word is not an interpreter, so it is not an invocation.

### Edges

- **consumes-from** `TOOL-dRankedPlan-49` — S1's collector and S2's resolution, whose value rule S1 widens; without them no binding exists
- **consumes-from** `TOOL-dRankedPlan-52` — S7's `piece` tokens and the rebuilt outer word, through which S1 finds the `$()` in a value
- **hands-off** `TOOL-dRankedPlan-67` — S1's substitution value, which that unit's item for finding 34 extends to a backtick span; carry S18 of that unit into this unit's pass (spec audit of units 53 to 62)

## 4. Design

### Evidence

- `.githooks/pre-commit:199` reads `if g=$(resolve_kit_gate "$pg_kit" guard.py); then`, and :212 reads
  `elif ! with_hook_index "$py" "$g" --staged; then`. `resolve_kit_gate` is defined at :174.
- `git grep -cE '[A-Za-z_][A-Za-z0-9_]*=\$\((resolve_kit_gate|resolve_kit_dir)' -- '*.sh' '.githooks/*'`,
  run 2026-10-27 at base 0689e7fa, counted 5 in `.githooks/pre-commit`, 4 in `.githooks/pre-push` and 1
  in `skills/session-kickoff/manifest-check.sh`, among others. The counts are PINNED.
- `scan_shell_tokens('if g=$(resolve_kit_gate loop ratify.py); then "$py" "$g" "$slug"; fi\n')`, run
  2026-10-27 at base 0689e7fa from `tools/lexicon/lexicon.py`, printed the words `if`, `g=`,
  `resolve_kit_gate`, `loop`, `ratify.py`, `then`, `"$py"`, `"$g"`, `"$slug"` and `fi`: the default
  mode drops the `$(` boundary, which separators mode keeps (`TOOL-dRankedPlan-41` S1). The output is
  PINNED.

### The reading after this unit

| Hook lines | Value of `g` | Answer |
|---|---|---|
| `if g=$(resolve_kit_gate loop ratify.py); then "$py" "$g" "$slug"; fi` | `$()`, span `resolve_kit_gate loop ratify.py` | caller |
| the same with `--exit` | the same | not a caller |
| `if g=$(resolve_kit_gate loop guard.py); then "$py" "$g" --staged; fi` | span names no `ratify.py` | not a caller |
| `g=$(pick_script)`, then `"$py" "$g"` | span names no `ratify.py` | unread, run-time assembly |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-bound-resolver`, `caller-shell-bound-resolver-exit`, `caller-shell-bound-resolver-other` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 22, after `TOOL-dRankedPlan-52` inside that step, because both write
`tools/loop/ratify.py` and this unit consumes from it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Bind only a substitution whose LAST word ends in `ratify.py`.** `resolve_kit_gate loop ratify.py
  home` would then pass, and the last-word rule needs the resolver's signature to be right.
- **Name the resolver binding as unread.** It is the repository's own hook pattern, so the ban would
  certify an absence over the shape the next hook copies.

## 5. Production-readiness checklist

- security — narrows: the repository's resolver-binding hook pattern is read by the deny-by-default
  ban.
- perf / scale — one pass over each assignment's nested spans.
- error / empty / loading states — a value with no `$()` is read as `TOOL-dRankedPlan-49` S1 reads it.
- observability — the refusal names the file and the invoking command's line.
- risks — a name bound to a substitution that only mentions `ratify.py`, such as `g=$(echo
  ratify.py)`, is refused when invoked through an interpreter, which fails closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-bound-resolver` runs, the check exits
  1 naming `.githooks/pre-commit`.
  Red when: a name bound to a resolver substitution naming `ratify.py` passes.
- **AC2** — When the plant `caller-shell-bound-resolver-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a resolver-bound `--exit` call is refused.
- **AC3** — When the plant `caller-shell-bound-resolver-other` runs, the check exits 0.
  Red when: a resolver binding for another kit script is read as a `ratify.py` caller.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `caller-shell-bound-resolver*` plants, staged by a collector that compares the rebuilt `g=$()` text only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 28 (HIGH,
  item H4), repairing `TOOL-dRankedPlan-49`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-49`'s binding collector and `TOOL-dRankedPlan-52` S7's word
rebuild. `python tools/codebase-map/reuse_lookup.py "resolve a shell variable bound to a script path
where a command invokes it"`, run 2026-10-27, ranked name stems only (`resolve`, `resolve_kit_dir`,
`resolve_caps`), and `resolve_kit_dir` is the resolver the hooks call, not a reader of its binding, so
no existing seam fits beyond the two units. `tools/gate-lint/sh_hygiene.py:160-163` reads an assignment
with a regex over a raw line rather than over tokens, and lives in another kit, so it is cited and not
imported. The recall
query returned units 47 to 52 and dWitnessedBar's resolver scouts, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
