# TOOL-dRankedPlan-73 — a shell carrier the file tokenizer closes but its readers cannot read exits 2, each reader planted

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-73-deviation-731.md](../build/2026-10-27-build-TOOL-dRankedPlan-73-deviation-731.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 11 at HIGH**, item **H3**. Finding 4, item M4, is its medium face, and its item in
`TOOL-dRankedPlan-77` corrects unit 65's evidence and arm line. `TOOL-dRankedPlan-65` S2 exits 2 on a
carrier `shlex.split` cannot split, and its plant `caller-shell-c-dq-broken` leaves the carrier's `"`
unclosed. `scan_shell_tokens` then raises on the whole file, and `TOOL-dRankedPlan-41` S4 exits 2
before any carrier reaches `shlex`. AC3 is green whether S2 is built, built wrong or missing, so the
path where the file tokenizer accepts a carrier that a carrier reader rejects is covered by nothing.
This unit names the two carrier readers that can fail after the file tokenizer succeeds, gives each a
plant that reaches it, and pins that exit 2 wins over a caller answer. It repairs
`TOOL-dRankedPlan-65`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The refusal, by reader. A `-c` word or `herestring` carrier of `TOOL-dRankedPlan-65` S1
  exits 2, printing `ratify — <path>:<line> cannot be tokenized: <reason>` as `TOOL-dRankedPlan-41` S4
  prints it, the line being the command's, in two cases. In the first, `shlex.split(word,
  posix=True)` raises `ValueError`. In the second, `scan_shell_tokens` raises `SyntaxError` on the
  unquoted text. The exit 2 is decided before any reader's caller answer over that carrier, so a line
  rule hit beside it never turns it into exit 1, as unit 41 S4 never reads a file in part. This
  supersedes unit 65 S2's "A carrier `shlex.split` cannot split, an unbalanced quote say, exits 2", and
  unit 65 S3's plant `caller-shell-c-dq-broken` and its AC3, which this unit's plants replace. Observed
  by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.githooks/pre-commit`. Observed by
  AC1 and AC2.
  - `caller-shell-c-dq-unsplit` holds `bash -c "${py#"'"} \"$d/ratify.py\" \"$slug\""`. The file
    tokenizer closes the word, and `shlex` raises. It exits 2.
  - `caller-shell-c-dq-untokenized` holds `bash -c "echo it's \"$d/ratify.py\""`. `shlex` unquotes it
    to `echo it's "$d/ratify.py"`, and the shell tokenizer raises on the apostrophe. It exits 2.

## 3. Non-goals (OUT)

- A carrier the file tokenizer rejects: `TOOL-dRankedPlan-41` S4's exit 2, unchanged.
- Unit 65's §4 Evidence and `New arm:` line: `TOOL-dRankedPlan-77`'s item for finding 4.
- A carrier in ANSI-C or locale quoting: `TOOL-dRankedPlan-74`.

### Edges

- **consumes-from** `TOOL-dRankedPlan-65` — S1's unquoting and its readers, and S2 and S3, which S1 restates and S2 replaces; without them no carrier is unquoted
- **hands-off** `TOOL-dRankedPlan-77` — S1's two readers and S2's plants, which that unit's item for finding 4 names in unit 65's §4 Evidence and `New arm:` line

## 4. Design

### Evidence

- A probe run 2026-10-27 at a76dbde6 over `scan_shell_tokens('bash -c "${x#"\'"} \\"$d/ratify.py\\""\n')`
  from `tools/lexicon/lexicon.py` returned three words, the last the whole carrier, because
  `read_braced` (:530) nests the `${…}` and its quotes. `shlex.split` over that word raised `No closing
  quotation`. Bash with `x="'echo"` ran it and printed `/k/ratify.py`. The outputs are PINNED. The
  word holds no `$(` or backtick span, so the piece rule of `TOOL-dRankedPlan-52` S7 leaves it whole in
  separators mode too.
- The same probe over `bash -c "echo it's \"$d/ratify.py\""` returned three words, `shlex` unquoted the
  last to `echo it's "$d/ratify.py"`, and `scan_shell_tokens` over that text raised `unterminated '
  quote opened at line 1`. The outputs are PINNED.
- The same tokenizer over unit 65's `caller-shell-c-dq-broken` line raised on the whole file, as the
  audit's finding 11 records.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-c-dq-unsplit`, `caller-shell-c-dq-untokenized` | `ratify.py` fixture plants | none |

No item mints a function. S1 is the error arm of unit 65's carrier reading.

### Rollout

Live at landing, at order 25. Units 67, 74, 75 and 76 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Drop unit 65's S2 and AC3, citing unit 41 S4.** The audit offers it. The probes show two readers
  that fail after the file tokenizer succeeds, so unit 41 S4 does not own them, and dropping S2 leaves
  a reachable fail-open path.
- **Let a line rule hit win as exit 1.** A carrier a reader cannot read is read in part then, which
  unit 41 S4 forbids for a file.

## 5. Production-readiness checklist

- security — closes a fail-open path: a carrier a reader cannot read is refused, never admitted.
- perf / scale — none.
- error / empty / loading states — S1's two exits 2.
- observability — each refusal names the file, the command's line and the reader's reason.
- risks — a carrier bash runs but `shlex` cannot split exits 2 on readable input, which fails closed.
- testing — the two plants.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-c-dq-unsplit` runs, the check exits
  2 and prints the `.githooks/pre-commit` line with `No closing quotation`.
  Red when: the `ValueError` handler reads the carrier as no caller, so the check exits 0.
- **AC2** — When the plant `caller-shell-c-dq-untokenized` runs, the check exits 2 and prints the
  `.githooks/pre-commit` line.
  Red when: the inner `SyntaxError` is read as no caller and the line rule's hit exits 1, or the check
  raises a traceback.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `caller-shell-c-dq-unsplit` reddened by a `ValueError` handler returning no caller, and `caller-shell-c-dq-untokenized` reddened by an inner `SyntaxError` handler returning no caller · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 11
  (HIGH, item H3; finding 4 is its medium face), repairing `TOOL-dRankedPlan-65`.

## 10. Reuse audit

The seams reused are unit 65's `shlex.split` and `scan_shell_tokens` (`tools/lexicon/lexicon.py:469`),
whose two errors S1 maps onto `TOOL-dRankedPlan-41` S4's message and exit. `python
tools/codebase-map/reuse_lookup.py "decode ansi-c dollar single quoted shell string escapes"`, run
2026-10-27, ranked `parse_shell_defs`, `resolve_shell_argv`, `ask_shell` and `scan_shell_layer`, none
of which reports a carrier's error, so no seam fits beyond unit 41 S4's error rule. The recall query
returned units 46, 53 and 65 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read command substitutions inside an expanded heredoc body and ansi-c carriers" --terms "heredoc expanded command substitution span case esac arithmetic ansi-c carrier shlex caller ratify"`
