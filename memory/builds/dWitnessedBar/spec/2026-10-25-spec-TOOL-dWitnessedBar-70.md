# TOOL-dWitnessedBar-70 — the CRLF record arm proves its planted CR reaches `read_green_file` before any CR-strip assertion counts, and each staged red is recorded with its failing line from a Windows node

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 39 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 10 at BLOCKER**, report item **B1**, the round's one blocker. No other id
shares that item.

`TOOL-dWitnessedBar-66` §4 Evidence says the hook's per-key awk read "keeps a CR". On Git for Windows,
and on the `windows-latest` CI the bar runs on, it does not: gawk reads in text mode and bash `$(...)`
drops a trailing CR-LF. With the CR strip removed, `rec_sha` is still forty bytes, so unit 66's staged
red "CR strip removed" stays green, and the arm certifies a strip it never exercises. That is the
defect unit 66 was promoted to fix.

`TOOL-dWitnessedBar-69` changes the read so the CR can reach the strip. This unit makes the arm PROVE
that it does, on every run and on whatever platform runs it, before the strip assertion counts. It
also makes each staged red a record of the failing line rather than a claim. It repairs
`TOOL-dWitnessedBar-66` and builds at order 39, after unit 69 within that order.

## 2. Scope (IN)

- **S1** — The CR-reach canary. Before the AC12 arm counts unit 66 S2's `rec_sha` assertion, it builds
  a mutant of the cut `read_green_file` that lacks its CR strip, made by `sed 's/%[$].[\]r.}/}/'`. It
  checks that the mutant differs from the cut in exactly one line, counting `diff` output lines that
  open `>`, as `tools/run-gates/run-gates.evidence.test.sh:2169-2177` counts its own variants. It
  sources the mutant in a subshell, calls it on the AC12 record, and asserts that `rec_sha` is
  forty-one bytes whose last byte is CR. Observed by AC1.
- **S2** — The canary's failure is loud and stops the count. When the mutant changed no line, or its
  `rec_sha` is not forty-one bytes ending in CR, the arm prints one line,
  `gov-canary: the planted CR never reached read_green_file on <uname -s>; the CR-strip assertion is not counted`,
  sets `fail=1`, and does not increment the executed count for unit 66 S2's assertion. Observed by
  AC2.
- **S3** — The staged reds are records with their failing line. At the close, the main loop stages
  unit 66 §7's two breaks against a scratch copy of `.githooks/pre-push`, on a Windows node:
  - a `read_green_file` that lacks its CR strip;
  - a `read_green_file` whose `sha` case keeps the first of a repeated key.

  Unit 66's acceptance ledger records each beside AC2, with the arm's failing line as printed and the
  `uname -s` it ran under. A break with no captured failing line is not recorded as red. Observed by
  AC3.
- **S4** — The record is corrected. Unit 66's acceptance ledger, beside AC2, states the platform fact
  in place of its §4 Evidence's "keeps a CR", citing this spec's §4 Evidence. Observed by AC4.

## 3. Non-goals (OUT)

- The read form itself, which is `TOOL-dWitnessedBar-69`'s S1. This unit tests it and changes nothing
  in `.githooks/pre-push`.
- The `fingerprint` line's share of the canary, which is `TOOL-dWitnessedBar-72`'s.
- The report's left-shift text: a bug-class checklist entry for a CR plant read through awk or `$(...)`
  on Git for Windows. No clause of this build names it. S1's canary is the regression this unit
  builds, and it is a check that runs on every bar rather than a reminder.
- Re-wording unit 66's spec text. S4 answers its §4 Evidence in its ledger by name.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-66` — the AC12 arm's hook half, its record and its two staged breaks, which S1 to S4 make observable on the bar's platform (id 10)
- **consumes-from** `TOOL-dWitnessedBar-69` — the whole-line read that keeps the CR, without which S1's mutant reads forty bytes and the canary fails on every run (id 10)
- **hands-off** `TOOL-dWitnessedBar-72` — the canary's `rec_fp` assertion over unit 67's `fingerprint` line (id 20)
- **hands-off** `TOOL-dWitnessedBar-74` — the canary's `rec_sha` comparison as one function, seen red on every run by a one-line `sha` variant, in place of AC2's `$(awk ...)` plant, which stops at the count (id 10 of the round-1 spec audit of units 68 to 73, item H1)
- **hands-off** `TOOL-dWitnessedBar-75` — S2's failure line given a slot naming the check that failed, and AC2's two breaks recorded with the line each printed (id 24, item H1)
- **hands-off** `TOOL-dWitnessedBar-78` — the compares still run after a failed canary, the strip-less break's two lines recorded for AC3, and each byte-arm break's `diff` count recorded beside AC2 (ids 1 and 2, items M2 and M1)

## 4. Design

### Evidence

- On this node (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`, git 2.54.0.windows.1), the base read
  `x=$(awk -F'\t' '$1=="sha"{print $2}' rec)` over a record whose second `sha` line ends in CR-LF gave
  81 bytes with no CR. `awk -F'\t' '$1=="sha"{print length($2)}'` printed 40 for that line. So unit 66
  §4 Evidence's second bullet is false here: the base read prints every match but keeps no CR.
- A prototype of unit 69 S1's loop, mutated by `sed 's/%[$].[\]r.}/}/'` with one line changed, gave
  `rec_sha` 41 bytes ending in `\r`. The same `sed` over a reader written in unit 65 S15's awk form,
  `rec_sha=$(awk -F'\t' '$1=="sha"{v=$2} END{print v}' "$1"); rec_sha=${rec_sha%$'\r'}`, changed one
  line and still gave 40 bytes. So the canary separates a read that keeps the CR from one that does
  not.
- Over the whole of `.githooks/pre-push` the same `sed` changes three lines, so S1 applies it to the
  cut function only, where the count it checks is one.
- `grep -n runs-on .github/workflows/remote-ci.yml` prints four `windows-latest` lines.
- The suite counts executed assertions in `a` and compares them with `FLOOR_ASSERTIONS`
  (`tools/run-gates/run-gates.gov.test.sh:91`, `:94`, `:459`).

### Inventory

Minted: the failure line of S2. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 39, after `TOOL-dWitnessedBar-66` (38) and after `TOOL-dWitnessedBar-69`,
which sorts first in the tie and which the dispatch edge refusal requires CLOSED before this unit is
dispatched. The tie is recorded as `TOOL-dWitnessedBar-68` §4 Rollout records it.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **State the CR half as observable only on a host whose awk and bash keep CR, the report's option
  (b).** The bar runs on `windows-latest` alone, so the arm would certify the strip on no leg that
  runs.
- **Stage the strip-removed break once at the close and trust it thereafter.** A later change to the
  read that eats the CR again would leave the arm green with nobody staging the break; S1 runs that
  break on every bar.

## 5. Production-readiness checklist

- security — no new write path. The mutant is written in the suite's scratch directory.
- perf / scale — one `sed`, one `diff` and one sourced call in a subshell per run.
- error / empty / loading states — S2 names the two ways the canary fails: no line changed, and a CR
  that never arrived.
- observability — S2's line names the platform, so a red on one runner and green on another reads as
  a platform fact.
- risks — a reader rewritten so the strip is spelled differently fails S1's one-line count loudly,
  which is the intended prompt to update the canary with the reader.
- testing — AC1 and AC2 by probe and scratch copy, AC3 and AC4 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the AC12 arm's canary runs over the built tree on this Windows node, the `diff` of the
  cut function and its mutant counts one changed line, and the mutant's
  `printf %s "$rec_sha" | wc -c` prints 41 with `tail -c1 | od -c` showing `\r`. The arm prints no
  `gov-canary: the planted CR` line.
  Red when: the mutant reads forty bytes, so the canary cannot tell a strip from a read that eats the
  CR.
- **AC2** — When the arm runs against a scratch copy of `.githooks/pre-push` whose `read_green_file`
  reads `sha` as `rec_sha=$(awk -F'\t' '$1=="sha"{v=$2} END{print v}' "$1"); rec_sha=${rec_sha%$'\r'}`,
  it prints `gov-canary: the planted CR never reached read_green_file on ` followed by the
  `uname -s` value, and exits non-zero. Against a copy whose function holds no `%$'\r'`, it prints the
  same line.
  Red when: the canary passes over a read whose I/O path drops the CR.
  fixture: scratch copies of `.githooks/pre-push` under `%TEMP%/<short-name>`.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-66*acceptance-ledger*`
  runs at the close, it prints two red records, one per break of S3, each quoting a failing line that
  names `rec_sha` and a `uname -s` value beginning `MINGW` or `MSYS`.
  Red when: a staged red is recorded with no captured failing line, or from no Windows node.
  permission: the arm's run is the main loop's, at the close.
- **AC4** — When the same ledger line is read, it states that gawk's text-mode input and `$(...)` drop
  the CR on Git for Windows and names `TOOL-dWitnessedBar-70`.
  Red when: unit 66's ledger still carries "keeps a CR" as the reason the arm is red at the base.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 · the CR-reach canary over the AC12 record, staged red by a scratch hook whose `sha` read goes through `$(awk ...)` with the strip kept (reaches the canary's 41-byte assertion) and by one with no strip to delete (reaches its one-line count) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 66 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is the CR half made observable on the bar's platform (id 10)?** Options: (a) a
  mid-field CR read by awk into a scratch file checked with `od -c`, the report's option (a); (b) the
  half declared observable only off Windows, its option (b); (c) unit 69's read that keeps the CR, with
  a canary that runs the strip-deleted mutant on every run. (a) reaches the strip only if unit 65 S15
  strips the stored value rather than `$0` (the report's caveat), and `$(...)` still eats a trailing
  CR-LF, so its red depends on how the strip is spelled. (b) certifies the strip on no leg the bar
  runs, which fails AC1; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (c), rung 3. It
  meets AC1 to AC4 on every platform and leaves no open question about where the strip sits.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 10
  (BLOCKER, item B1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-74, TOOL-dWitnessedBar-75 and TOOL-dWitnessedBar-78,
  promoted by the round-1 spec audit of units 68 to 73; nothing else moved.

## 10. Reuse audit

The seam is unit 66's AC12 arm in `tools/run-gates/run-gates.gov.test.sh`, extended in place, and the
broken-copy idiom of `tools/run-gates/run-gates.evidence.test.sh:2169-2177`: a `sed` mutant whose
changed-line count is asserted before the copy is graded.
`python tools/codebase-map/reuse_lookup.py "assert a planted fixture byte survives the read before counting a mutation red"`
ranked `read`, `read_text`, `before` and `counts`, none a mutation check, so no existing seam fits
beyond the two named above.

Recall terms used: `python tools/memory-recall/query.py "how does the green record reader keep a CR so the strip is exercised on Git for Windows" --terms "read_green_file rec_sha CR strip CRLF gawk text mode command substitution read -r canary staged red"`
