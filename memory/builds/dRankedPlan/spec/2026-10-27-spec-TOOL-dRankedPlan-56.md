# TOOL-dRankedPlan-56 — a `-c` word and a here-string fed to a shell are read by the shell reader

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-56-deviation-561.md](../build/2026-10-27-build-TOOL-dRankedPlan-56-deviation-561.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 27 at HIGH**, item **H3**. `TOOL-dRankedPlan-46` §3 sends `-c` and here-strings to
`TOOL-dRankedPlan-52`, but unit 52 S14 reads them only for a command word in `TOOL-dRankedPlan-47`'s
Python class. `TOOL-dRankedPlan-32` S2 reads `bash` as a non-interpreter word, and the quoted `-c` word
does not end in `ratify.py`, so `bash -c '"$py" "$d/ratify.py" "$slug"'` and `bash <<<
'"$py" "$d/ratify.py" "$slug"'` reach no reader that compares against `ratify.py` and pass the
deny-by-default ban. The tree writes `bash -c` and `sh -c` often, so a new hook is likely to copy the
shape. This unit extends unit 52 S14's inline carriers to the shell class. It repairs
`TOOL-dRankedPlan-52`, whose S14 is the reading this unit widens, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The shell carriers. For a command whose command word, read as `TOOL-dRankedPlan-46` S1 reads
  one, is in `SHELL_BODY_WORDS`, two carriers are read as shell source. The word after a `-c` option
  word is one. A `herestring` token (`TOOL-dRankedPlan-52` S14) is the other. A single-quoted carrier
  is read by `read_shell_callers` as a file of its own, its outer quotes stripped, with
  `TOOL-dRankedPlan-38`'s textual rule beside it and `TOOL-dRankedPlan-55`'s inherited bindings. Any
  other quoting is read by `TOOL-dRankedPlan-52` S13's textual line rule over the carrier's text. This
  supersedes unit 52 S14's limit to the Python class, which stays as stated for Python, and unit 46 §3's
  sending of the shell carriers to unit 52. Observed by AC1, AC2 and AC3.
- **S2** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-c` plants a `.githooks/pre-commit` holding `bash -c '"$py" "$d/ratify.py"
    "$slug"'`. It is refused with exit 1.
  - `caller-shell-herestring` plants `bash <<< '"$py" "$d/ratify.py" "$slug"'`. It is refused with
    exit 1.
  - `caller-shell-c-exit` plants `caller-shell-c` with `--exit` after `"$slug"` inside the quotes. It is
    admitted.

## 3. Non-goals (OUT)

- `python -c` and a here-string fed to Python: `TOOL-dRankedPlan-52` S14, unchanged.
- A `-c` word built at run time, such as `bash -c "$cmd"`: run-time assembly, unread as
  `TOOL-dRankedPlan-32` §3 states. S1's line rule reads the word's text, which names no `ratify.py`.
- Shells outside `SHELL_BODY_WORDS`: the ceiling `TOOL-dRankedPlan-46` §4 records.

### Edges

- **consumes-from** `TOOL-dRankedPlan-52` — S14's `herestring` token and its `-c` reading, and S13's textual line rule, which S1 extends to the shell class
- **consumes-from** `TOOL-dRankedPlan-46` — `SHELL_BODY_WORDS` and the shell arm's command-word reading, which select S1's commands
- **consumes-from** `TOOL-dRankedPlan-55` — the enclosing file's bindings a body inherits, which S1 gives a carrier too

## 4. Design

### Evidence

- `TOOL-dRankedPlan-52` S14 (its lines 130-137) reads a `-c` word or here-string "For a command whose
  command word is in `TOOL-dRankedPlan-47` S1's Python class". `TOOL-dRankedPlan-46` §3 (its lines
  55-56) sends "`python -c` and here-strings" to unit 52.
- `scan_shell_tokens`, run 2026-10-27 at base 0689e7fa from `tools/lexicon/lexicon.py`, reads `bash -c
  '"$py" "$d/ratify.py" "$slug"'` as three words, the last one the whole single-quoted span, and reads
  the here-string form as `bash` and that same span. The output is PINNED.
- `git grep -nE '(^|[^A-Za-z0-9_./-])(bash|sh) -c ' -- '*.sh' '.githooks/*'`, run 2026-10-27 at base
  0689e7fa, printed 162 lines, and the same pattern ending `-c '` printed 112, a single-quoted word
  after `-c`. None names `ratify.py`. The counts are PINNED.

### The reading after this unit

| Command | Carrier | Reader | Answer |
|---|---|---|---|
| `bash -c '"$py" "$d/ratify.py" "$slug"'` | single-quoted `-c` word | shell reader | caller |
| `bash <<< '"$py" "$d/ratify.py" "$slug"'` | single-quoted here-string | shell reader | caller |
| `bash -c "\"$py\" \"$d/ratify.py\""` | double-quoted `-c` word | line rule | caller |
| `bash -c "$cmd"` | double-quoted `-c` word | line rule | unread, run-time assembly |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-c`, `caller-shell-herestring`, `caller-shell-c-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 23. Units 53, 54 and 56 write `tools/loop/ratify.py`, so by BUILD-METHOD M6
clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Add `bash` and `sh` to unit 32 S2's interpreter class.** `TOOL-dRankedPlan-46` §4 rejected it: a
  `.py` script run through `bash` is then read as an invocation, and every shell command's reading
  moves.
- **Name the shell carriers as unread.** The tree writes `bash -c` with a single-quoted word 112 times,
  so the ban would certify an absence over a shape hooks copy.

## 5. Production-readiness checklist

- security — narrows: a shell `-c` word or here-string running the predicate's CLI is refused.
- perf / scale — one tokenizer pass per carrier of a shell command. None names `ratify.py` at base.
- error / empty / loading states — a single-quoted carrier the shell tokenizer cannot read exits 2, as
  `TOOL-dRankedPlan-41` S4 states for a file.
- observability — the refusal names the file and the command's line.
- risks — a double-quoted carrier naming `ratify.py` for a non-executing purpose is refused by the line
  rule, which fails closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-c` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a shell `-c` word is read only for the Python class and passes.
- **AC2** — When the plant `caller-shell-herestring` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a here-string fed to `bash` passes.
- **AC3** — When the plant `caller-shell-c-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a shell `-c` word's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · `caller-shell-c`, `caller-shell-herestring` and `caller-shell-c-exit`, staged by a carrier reader limited to the Python class · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 27 (HIGH,
  item H3), repairing `TOOL-dRankedPlan-52`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-52` S14's carrier reading, which gains the shell class beside
the Python one, with `read_shell_callers` reading the carrier. `python
tools/codebase-map/reuse_lookup.py "resolve a shell variable bound to a script path where a command
invokes it"`, run 2026-10-27, ranked name stems only (`resolve`, `resolve_kit_dir`, `resolve_caps`),
none of which reads a `-c` word, so no existing seam fits beyond unit 52's carriers and unit 32's
reader. The recall query returned units 47 to 52 and dWitnessedBar's resolver scouts, and they agree
with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
