# TOOL-dRankedPlan-51 — the op tokens `(`, `)`, `{` and `}` end a command, so a brace group, a subshell or a function body is read

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 9 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-51-deviation-511.md](../build/2026-10-27-build-TOOL-dRankedPlan-51-deviation-511.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-50 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 35 at HIGH**, item **H5**. `TOOL-dRankedPlan-41` S3 defines a command as "the run of `word`
tokens between two separator `op` tokens", and never says what the tokenizer's other ops, `(`, `)`,
`{` and `}`, do. If a builder drops them from the run, `run() { "$py" "$d/ratify.py" "$slug"; }` reads
`run` as the command word and passes the ban. `TOOL-dRankedPlan-39` puts `{` in
`SHELL_RESERVED_WORDS` as a word, but the tokenizer emits it as an op, so that member can never match.
`TOOL-dRankedPlan-40` S2 relies on a `)` inside a command. Finding 2 is the same ambiguity at MEDIUM,
item M1, and `TOOL-dRankedPlan-52` adds its observation. This unit states that each of the four ops
ends the current command and starts a new one, and restates units 39 and 40 over that model. It
repairs `TOOL-dRankedPlan-41`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The four ops. In `read_shell_callers`' command model (`TOOL-dRankedPlan-41` S3), each of the
  op tokens `(`, `)`, `{` and `}` ends the current command and starts a new one, as the separator ops
  do. A command is the run of `word` tokens between two `op` tokens of any kind, with unit 41 S3's
  `$(` and `$)` nesting unchanged. This supersedes unit 41 S3's "between two separator `op` tokens".
  Observed by AC1, AC2 and AC3.
- **S2** — The brace in the reserved words. `{` leaves `SHELL_RESERVED_WORDS` (`TOOL-dRankedPlan-39`
  S1), because the tokenizer never yields it as a word and S1 already ends a command at it. The set is
  `("if", "then", "elif", "else", "while", "until", "do", "!")`. Observed by AC5.
  **Readers:** by name: `SHELL_RESERVED_WORDS` — READER NOT IN TREE: its one reader is
  `read_shell_callers` in `tools/loop/ratify.py`, which does not exist at base 0689e7fa
  (`TOOL-dRankedPlan-39` S1) · by value: NO VALUE READERS — the members are compared with a command's
  leading words inside `read_shell_callers` only, and no record, fixture or count reads the set.
- **S3** — The case arm. `TOOL-dRankedPlan-40` S2 reads: the words before a `)` op are the arm's
  pattern, which S1 ends as a command of its own, so the command word is read after the `)`. Its
  clause "a word ending in an unquoted `)`" matches no token, because the tokenizer emits every
  unquoted `)` as an op. Unit 40's `caller-shell-case` plant observes the restated rule. Observed by
  AC4.
- **S4** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Each is refused. Observed by AC1, AC2 and
  AC3.
  - `caller-shell-brace` plants a `.githooks/pre-commit` holding `{ "$py" "$d/ratify.py" "$slug"; }`.
  - `caller-shell-subshell` plants `( "$py" "$d/ratify.py" "$slug" )`.
  - `caller-shell-func` plants `run() { "$py" "$d/ratify.py" "$slug"; }` and a later `run`.

## 3. Non-goals (OUT)

- A function used as a wrapper of another command: `TOOL-dRankedPlan-50`. S1 reads the body of
  `run()` above as its own commands, whichever function calls it.
- The class probe that every literal of a matching set is producible as the token kind it is matched
  against (finding 2): `TOOL-dRankedPlan-52`'s item.
- The tokenizer. It already emits the four ops in both modes (§4), and this unit reads them.

### Edges

- **consumes-from** `TOOL-dRankedPlan-41` — S3's command model over the separators-mode tokens, whose command boundary S1 widens to the four ops; without it there is no command to bound
- **consumes-from** `TOOL-dRankedPlan-39` — `SHELL_RESERVED_WORDS`, from which S2 takes the unreachable `{`
- **consumes-from** `TOOL-dRankedPlan-40` — S2's case-arm rule and the `caller-shell-case` plant, which S3 restates over the `)` op
- **hands-off** `TOOL-dRankedPlan-52` — S1's command model and S2's set, over which that unit's item for finding 2 observes that every member of each matching set is producible as a `word` token
- **hands-off** `TOOL-dRankedPlan-62` — S1's command model, §4, §7 and §10, which that unit's items for findings 20, 24 and 34 read or correct; carry S6, S12's §10 sentence and S16's two §4 rows of that unit into this unit's pass (spec audit of units 46 to 52)
- **hands-off** `TOOL-dRankedPlan-67` — §4 and §10, whose corrections from unit 62's S12 and S16 that unit's AC23 observes carried (spec audit of units 53 to 62)

## 4. Design

### Evidence

- A probe run 2026-10-27 at base 0689e7fa, `scan_shell_tokens('run() { "$py" r.py; }\n')`, printed
  `('word','run',1) ('op','(',1) ('op',')',1) ('op','{',1) ('word','"$py"',1) ('word','r.py',1)
  ('op','}',1)`. The output is PINNED.
- The audit's skeptic reproduced the case arm `--ask) exec …` as `('word','--ask',2) ('op',')',2)
  ('word','exec',2)` (its appendix row for id 2).
- The tokenizer's docstring (`tools/lexicon/lexicon.py:472`) reads "`op` is one of `( ) { }`".

### The reading after this unit

| Shell | Commands | Answer |
|---|---|---|
| `{ "$py" "$d/ratify.py" "$slug"; }` | `"$py" "$d/ratify.py" "$slug"` | caller |
| `( "$py" "$d/ratify.py" "$slug" )` | the same | caller |
| `run() { "$py" "$d/ratify.py" "$slug"; }` | `run`, then the call | caller |
| `--ask) exec "$py" "$d/ratify.py" "$slug" ;;` | `--ask`, then `exec …` | caller, read past `exec` by unit 40 S1 |
| `"$py" "$d/ratify.py" "$(printf x)"` | one command, the `$(` span nested | caller, as unit 41 S3 states |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-brace`, `caller-shell-subshell`, `caller-shell-func` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 9. `TOOL-dRankedPlan-50` shares order 9 and also writes
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 the two are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S4

### Alternatives rejected

- **Keep the four ops in the command's token list for unit 40 S2 to test.** Every leading-word rule
  would then have to skip ops as well as words, and a function body would still begin with the
  function's name.
- **Keep `{` in the set and state that it is matched as an op.** The set is matched against words, so
  the member would document a rule the code cannot run, which is the class finding 2 names.

## 5. Production-readiness checklist

- security — narrows: a call inside a brace group, a subshell or a function body is read by the
  deny-by-default ban.
- perf / scale — unchanged: the ops are already in the stream.
- error / empty / loading states — a command with no word, such as the one between `)` and `{` of a
  definition, has no command word and is not an invocation.
- observability — the refusal names the file and the call's line.
- risks — none beyond unit 41's.
- testing — the three plants, red, and unit 40's case plant re-read.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-brace` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a call inside a brace group passes.
- **AC2** — When the plant `caller-shell-subshell` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a call inside a subshell passes.
- **AC3** — When the plant `caller-shell-func` runs, the check exits 1 naming the line of `run() {`.
  Red when: a function body's call is read with the function's name as its command word.
- **AC4** — When the plant `caller-shell-case` (`TOOL-dRankedPlan-40` S3) runs at this unit's tip, the
  check exits 1 naming the arm's line.
  Red when: the `)` op no longer ends the pattern.
- **AC5** — When a probe imports the loop kit's `ratify.py` and prints `"{" in SHELL_RESERVED_WORDS`,
  it prints `False`.
  Red when: the set keeps a member the tokenizer never yields as a word.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 AC4 · `caller-shell-brace`, `caller-shell-subshell`, `caller-shell-func` and unit 40's `caller-shell-case`, staged by a reader that drops the four ops from a command's tokens · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 35 (HIGH,
  item H5; finding 2 is its medium face), repairing `TOOL-dRankedPlan-41`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-67`, each the reciprocal of that promoted unit's own edge (spec audit of units 53 to 62, `reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-41` S3's command model over `scan_shell_tokens`, which already
emits the four ops, so no tokenizer change is needed. `parse_shell_defs` reads the same ops to find a
function's body, which is the reading S1 matches. `python tools/codebase-map/reuse_lookup.py "find
which command a shell heredoc or wrapper function runs and read its script argument"` ranked name stems
only (`read`, `run`, `run_git`), so no seam fits beyond unit 41's model. The recall query returned
units 38, 40 and 41 and this audit's H5 item, and they agree with the probe.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
