# TOOL-dBoundRoles-61 — unit 59's read check fails on its slice's exit status, so a slice that crashes can no longer pass for a read it never checked

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 24 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-61-deviation-611.md](../build/2026-10-26-build-TOOL-dBoundRoles-61-deviation-611.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-61-deviation-612.md](../build/2026-10-26-build-TOOL-dBoundRoles-61-deviation-612.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md) | research | TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 |
| [2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md) | research | TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 |
| [2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 59 and 60
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md`) confirmed
finding **id 19 at HIGH**, report item **H1**. No other id shares the item. Id 9 reports the same defect
at MEDIUM, item M2, and is `TOOL-dBoundRoles-63`'s.

`TOOL-dBoundRoles-59` §4 "The slice" gives `assert_role_reads` one verdict: an empty printed line means
every key is read. The slice's exit status is never read, and `tools/roles/adopt-roles.test.sh:51` runs
under `set -u` alone, so a `$(...)` capture of a slice that crashes comes back empty and the case
passes. A role slot with no file raises `KeyError`, and malformed front matter raises `RolesError`. In
each case the check certifies a read it never made.

This unit makes the helper fail on any non-zero exit of its slice and restates unit 59's spec for it.
It repairs `TOOL-dBoundRoles-59` and builds one step after it (order 24).

## 2. Scope (IN)

- **S1** — The exit check. `assert_role_reads <role> <key>...` in `tools/roles/adopt-roles.test.sh`
  captures its slice's stdout, its stderr and its exit status apart. A non-zero exit fails the case
  through `check_arm`, naming the role, the exit status and the last line of the slice's stderr. Exit 0
  with an empty stdout passes. Exit 0 with a printed key fails, naming the role and that key, as 59 S1
  states. Observed by AC1 and AC2.
- **S2** — A role slot the installed kit holds no file for fails the call by S1's non-zero branch,
  naming that slot. Observed by AC1.
- **S3** — A role file whose front matter `roles_lib.parse_front_matter` refuses fails the call by the
  same branch, naming the role and the refusal. Observed by AC2.
- **S4** — Unit 59's spec follows the helper. The pass bumps `TOOL-dBoundRoles-59`'s spec before it edits
  the helper (BUILD-METHOD M2, READY). Its S1 and its §4 "The slice" state S1's three verdicts. Its §5
  error states gain the missing-slot and refused-front-matter inputs. Its §6 gains AC5, the missing-slot
  call of AC1 below. Its §9 line names this unit, S1, §4, §5 and AC5. Unit 59's ledger answers AC5 in the
  OBSERVED form from this pass's observation. Where unit 59's pass already read the exit status and
  recorded the deviation, this pass records that, edits no code, and still makes the bump. Observed by
  AC3.
- **S5** — The floor moves with the arm. The floored assertions S1 to S3 add raise `FLOOR_ASSERTIONS` in
  `tools/roles/adopt-roles.test.sh`, with a `+<n> for <case> (TOOL-dBoundRoles-61)` term in the comment
  above it. Observed by AC4.

## 3. Non-goals (OUT)

- Id 9, the medium face of this defect: `TOOL-dBoundRoles-63` records this unit's closure of it.
- The report's left-shift checklist entry, "a check whose pass verdict is empty output must also assert
  exit status 0". No clause of this build names it; AC1 is this suite's regression.
- The suite's other `$(...)` captures. `MR` and `CH` at `tools/roles/adopt-roles.test.sh:67-68` are
  tested non-empty at `:69`, so a crash there already stops the suite.
- A `parse_read_key` refusal case. Unit 14 S4 states what the function returns, not what it refuses, so
  no input can be named here that it is known to refuse; S1's non-zero branch covers it either way.

### Edges

- **consumes-from** `TOOL-dBoundRoles-59` — the folded `assert_role_reads`, its slice, S1, §4, §5 and §6, which S1 extends and S4 restates (id 19)
- **hands-off** `TOOL-dBoundRoles-62` — S5's `+<n>` term naming this unit on the adopter suite's floor, which unit 62's restated AC15 of spec 60 requires (ids 19 and 21)
- **hands-off** `TOOL-dBoundRoles-63` — the exit check and spec 59's bump, which unit 63's item for id 9 records rather than rebuilds (ids 9 and 19)
- **hands-off** `TOOL-dBoundRoles-64` — S1, S4, S5, §4 "The capture", §7, AC1 and AC4, which unit 64 restates: the in-suite negative case inverted with its +2 term, the cases on every branch and the driver's `$TMP_ROOT` (ids 4, 8, 20, 22, 23 and 30 of the round-1 audit of units 61 to 63)
- **hands-off** `TOOL-dBoundRoles-66` — AC2, S1 and §7, which unit 66 has unit 64's AC5 read for `gov-orienter`, `R2` and the outer `check_arm` (id 5 of the round-1 audit of unit 64)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/adopt-roles.test.sh:51` is `set -u`, and the file holds no `set -e`. `:60` resolves `$PY`
  by running each candidate. `:81` holds `FLOOR_ASSERTIONS=50` under the `10, then +<n>` comment of
  `:73-80`. `:83` defines `check_arm`.
- `tools/roles/roles_lib.py:306-327` `parse_front_matter` raises `RolesError` on a missing block, an
  indented key, a line with no `:`, an unknown key and a repeated key.
- `tools/roles/roles_lib.py:330-336` `load_roles` returns a dict keyed by slot, so indexing it with a slot
  that has no file raises `KeyError`.
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-59.md` §4 "The slice" ends with "An
  empty line means every key is read"; neither its S1 nor its §5 names an exit status.
- `parse_read_key` is minted by unit 14 S4 and absent at base.

### The capture

```bash
out=$("$PY" -B -c "$slice" "$FX/$FXK" "$role" "$@" 2>"$TMP_ROOT/reads.err"); rc=$?
out=${out%$'\r'}
if [ "$rc" != 0 ]; then
  check_arm "$label: $role — reads slice exit $rc: $(tail -n 1 "$TMP_ROOT/reads.err")" 0
elif [ -n "$out" ]; then
  check_arm "$label: $role does not read $out" 0
else
  check_arm "$label: $role reads $*" 1
fi
```

An assignment from a command substitution takes that command's exit status, so `rc` is the slice's.
The CR strip follows `:67`. The block is the design's shape; the pass fits it to the helper's labels and
argument handling.

### Inventory

Minted: none. `assert_role_reads` keeps its name and its call sites.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 24, after unit 59 at order 23. `TOOL-dBoundRoles-19` holds order 24 and its
Files touched names the same suite (spec 19, §4), so the two declared write sets intersect and
`--dispatch` refuses the second pass while the first is open (M6 condition 1).

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`
- the spec of TOOL-dBoundRoles-59, a rev bump (S4), named here for the dispatch write set
- unit 59's acceptance ledger, the OBSERVED answer of S4, named here for the dispatch write set

### Alternatives rejected

- **`set -e` in the suite.** The suite counts failures and runs on, so one red arm would stop every arm
  after it.
- **An OK token printed by the slice on success.** It makes empty output fail, but it names no error, and
  the reader has to re-run the slice to learn why it crashed.

## 5. Production-readiness checklist

- security — no new write path; the stderr file lives under the suite's own `$TMP_ROOT`.
- perf / scale — one `"$PY" -B -c` per call, as 59 S1 already makes.
- error / empty / loading states — a missing slot, refused front matter or any other crash fails the case
  naming the role and the exit; an empty `reads` value still fails naming the first key.
- observability — each failure names the role, the exit status and the slice's last stderr line.
- risks — a slice that writes a warning to stderr and exits 0 still passes, which is correct.
- testing — AC1 to AC4 by a scratch driver over the helper, scratch role files and grep; the arm of §7 at
  the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a scratch driver defines `check_arm`, `$PY`, `$FX` and `$FXK` over the roles adopter
  fixture, sources the `assert_role_reads` definition from the roles adopter suite, and calls
  `assert_role_reads gov-nosuch input:question`, the call prints a `FAIL` line naming `gov-nosuch` and
  `KeyError`. With the helper staged back to reading stdout alone, the same call prints `ok`.
  Red when: the helper reads only stdout, so a crashed slice passes.
  fixture: a scratch repository with the roles kit installed by `build_fixture`'s steps, under `%TEMP%`,
  short-pathed.
- **AC2** — When the same driver indents the `reads:` key of the fixture's `gov-orienter.agent.md` and
  calls `assert_role_reads gov-orienter input:question`, the call prints a `FAIL` line naming
  `gov-orienter` and `R2`; restored, the call prints `ok`.
  Red when: refused front matter yields an empty line the helper reads as every key read.
- **AC3** — When a `python -c` probe extracts spec 59's S1 bullet and its `### The slice` subsection, each
  names the exit status, and spec 59's §6 holds an AC5 naming `gov-nosuch`, and its §9 holds a line
  naming `TOOL-dBoundRoles-61`.
  Red when: spec 59 still reads an empty line as the only verdict.
- **AC4** — When `grep -n 'TOOL-dBoundRoles-61' tools/roles/adopt-roles.test.sh` runs, it prints a `+<n>`
  term of the comment above `FLOOR_ASSERTIONS` and the call of AC1.
  Red when: the arm lands in the floored suite and the floor stays put.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · the missing-slot call and the refused front matter, staged by a helper that reads stdout alone · `FLOOR_ASSERTIONS` raised by the floored assertions the cases add, with a `+n` comment naming this unit

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 59 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 59 and 60, id 19
  (HIGH, item H1), on the report's fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-66, the minors batch of the round-1 audit of unit 64; nothing else moved.

## 10. Reuse audit

The seam is unit 59's `assert_role_reads` and the suite's `check_arm`
(`tools/roles/adopt-roles.test.sh:83`), extended by one exit branch rather than a second helper.
`python tools/codebase-map/reuse_lookup.py "fail a test case when a python slice it captures exits non-zero with empty output"`
ranked `fail`, `slice`, `resolve_python` and `read_git_output`, none a capture of a slice's exit status,
so no existing seam fits beyond the helper and `check_arm`. The recall query's hits include
`TOOL-aPromptedMandate-6`, whose arm asserts exit 0 AND empty output for the same wrong-reason pass, and
`TOOL-dDeclaredLoop-58`, the counted non-empty output form; both confirm the shape.

Recall terms used: `python tools/memory-recall/query.py "how does a test helper treat a crashed python slice whose output is empty" --terms "exit status empty output slice crash check_arm assert_role_reads set -u capture wrong-reason pass"`
