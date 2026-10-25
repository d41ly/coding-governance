# TOOL-dWitnessedBar-54 — the `exists:` spelling of a generated row's `when` reaches its other two readers, and the three readers are held to agree

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 10 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
confirmed finding **id 42 at HIGH**, its item **H2**, alone in that item. `TOOL-dWitnessedBar-45` S1
gives a `[[generated]]` row's `when` the form `exists:<path>` and migrates only `regen.py`. Two other
readers exist. govkit's selfcheck requires `when` to fullmatch `<conf>:<KEY>=<value>`
(`tools/govkit/govkit.py:2470`), so it fails gov's own tree, closed. `resolve_generated_indexes`
(`tools/unattended/lib-unattended.sh:883-886`) splits the value into conf `exists` and key
`{prefix}/govkit/govkit.py`, compares an empty answer and `continue`s, so the factory's generated
manifest drops out of `GENERATED_INDEXES` with no message, open. This unit takes the report's fix: both
readers learn the form, and a parity arm holds all three to one answer. It repairs
`TOOL-dWitnessedBar-45`.

## 2. Scope (IN)

- **S1** — The shell reader. `resolve_generated_indexes` reads a `when` beginning `exists:` as a path:
  it resolves `{prefix}`, `{kit}`, `{memory_root}` and `{map_root}` as `regen.resolve_argv` does,
  `{prefix}` being the reader's own `_rg_tool` or `.` (`lib-unattended.sh:849`), and keeps the row only
  when that path exists under the repository root. A path left with a token it cannot resolve skips the
  row with the line `:891` prints for a path token, naming the `when`. The `<conf>:<KEY>=<value>` form
  reads as today. Observed by AC1.
- **S2** — The descriptor check. govkit selfcheck's `_gwbad` (`govkit.py:2470`) admits, beside
  `<conf>:<KEY>=<value>`, `exists:<path>` whose path is non-empty and carries no token outside
  `regen.TOKENS` (`tools/run-gates/regen.py:48`); its refusal message names both forms, and the
  `when with no conf part` case of `tools/govkit/selftest.py:4340-4341` expects the new message.
  Observed by AC2.
- **S3** — The three readers agree. `tools/govkit/selftest.py` gains an arm over a scratch tree holding
  one `[[generated]]` row per `when` form, a conf form that holds, one that does not, an `exists:` path
  present, one absent and one with an unknown token: `regen.build_items` and `resolve_generated_indexes`
  keep the same rows, and selfcheck refuses exactly the forms `regen.check_when` refuses.
  Observed by AC3.

## 3. Non-goals (OUT)

- The `exists:` form, the factory row's `when` and `regen.py`'s reading: `TOOL-dWitnessedBar-45`'s.
- govkit's own shell-reader parity of `[[generated]]` rows (`govkit.py:2436-2464`), which compares the
  raw `when` string both ways and is unchanged by a new value shape.
- A bug-class entry "a spelling change strands its readers", the report's left-shift text: S3 gates the
  class for this key.
- The selfcheck observation on the built tree that unit 45's §7 never names: the minors batch's id 30
  item (`TOOL-dWitnessedBar-57`).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-45` — the `exists:` form and the factory row carrying it, whose two unmigrated readers this unit migrates
- **hands-off** `TOOL-dWitnessedBar-57` — the widened `_gwbad`, which the minors batch's id 30 item observes on the built tree with a malformed `when` staged
- **hands-off** `TOOL-dWitnessedBar-62` — S3's parity arm, the `exists:` reader, `_gwbad` and AC1 and AC2, which the minors batch splits by form, contains to the tree and documents (ids 1, 7, 10, 14, 19, 33, 37, 38, 39)

## 4. Design

### Evidence

- The readers, found by `git grep -n '"when"\|get("when")\|^when'` over `tools/`: `regen.check_when`
  (`tools/run-gates/regen.py:140-146`, called at `:186`), govkit selfcheck 6c (`govkit.py:2469-2477`),
  and the awk-and-shell reader of `resolve_generated_indexes` (`lib-unattended.sh:876`, `:883-886`).
- `_gen_tokens = {"memory_root", "map_root", "kit"}` (`govkit.py:2455`) bounds a row's `path`, not its
  `when`; `regen.TOKENS` adds `prefix` (`regen.py:48`), and regen resolves `{prefix}` to the tool
  directory (`:176`).
- The driver and its two checkers resolve `GENERATED_INDEXES` through this reader
  (`tools/unattended/unattended.sh:750`, `check-unattended.sh:361`, `check-pass-order.sh:130`,
  `check-brief-recorded.sh:188`).

### The forms, read three ways

| `when` | regen | lib-unattended | govkit selfcheck |
|---|---|---|---|
| `<conf>:<KEY>=<value>` | conf key equals value | same | admitted |
| `exists:<path>`, tokens known | path exists | same, S1 | admitted, S2 |
| `exists:<path>`, unknown token | Refusal | skipped with its line | refused |
| `exists:` with no path, or any other shape | Refusal | skipped with its line | refused |

### Inventory

Minted: nothing by name; one selftest arm and a widened refusal message.

### Migration

None: the only `exists:` row is unit 45's, and it lands one step earlier.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-45`.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Move the factory's row out of `GENERATED_INDEXES`' reach.** The unattended driver's index handling
  would stop covering a generated file, the silent half of the finding.
- **Have lib-unattended call `regen.py --list`.** The library forks no Python on this path today, and an
  adopter of the unattended kit without run-gates has no regen.

## 5. Production-readiness checklist

- security — `exists:` stats a path and runs nothing in all three readers.
- perf / scale — one `[ -e ]` per row carrying the form.
- error / empty / loading states — an unresolvable `when` is skipped with a line, never dropped silently.
- observability — the skip line names the descriptor and the `when`.
- risks — a fourth reader added later is not covered unless it joins S3's arm.
- testing — AC1 to AC3 by probe and fixture; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `bash -c '. tools/unattended/lib-unattended.sh && resolve_generated_indexes "$PWD" "" memory'`
  runs at gov's root on the built tree, its output names the leg factory's generated path paired with
  its generator; in a scratch copy with `tools/govkit/` removed, it does not, and no line is lost
  silently.
  Red when: the reader keeps the conf-only parse, so the pair drops out with no message.
  fixture: a scratch copy under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it reports no
  `[[generated]]` row failure; with the factory row's `when` set to `exists:` in a scratch copy, it
  fails naming both admitted forms.
  Red when: `_gwbad` still requires `<conf>:<KEY>=<value>`, so gov's tree fails selfcheck.
- **AC3** — When the S3 arm's scratch tree is read by
  `python -c "import sys; sys.path.insert(0, 'tools/run-gates'); import regen; ..."` through
  `regen.build_items` and by the AC1 shell call, both keep the conf-true and present-path rows only, and
  `govkit.py selfcheck` over that tree refuses the unknown-token and empty-path rows only.
  Red when: any two readers disagree on one form.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `routed-commits selftest` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so S1 is observed by
AC1 and S3's arm, not by that kit's suites.

New arm: tools/govkit/selftest.py · covers AC2 AC3 · five `when` forms read by regen, lib-unattended and selfcheck, staged red by restoring lib-unattended's conf-only parse · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-45`'s clause. Unit 45 carries
  none, being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51, id 42
  (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

The seams extended are the two readers themselves, `resolve_generated_indexes` and selfcheck 6c, and
`regen.TOKENS` with `resolve_argv`'s token rule, which both now follow rather than a third token list.
`python tools/codebase-map/reuse_lookup.py "evaluate a generated row when condition in the shell reader"`
ranked `rows`, `row`, `read` and `read_text`, generic stems of no condition reader, so no existing seam
fits beyond the readers named.

Recall terms used: `python tools/memory-recall/query.py "how do the readers of a generated row condition agree" --terms "generated when regen check_when govkit selfcheck _gwbad resolve_generated_indexes GENERATED_INDEXES shell reader parity"`
