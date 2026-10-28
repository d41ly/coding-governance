# TOOL-dIndexedDesign-52 — the standalone `--design-exit` opt-in reader refuses a present undated value and a conf it cannot evaluate, as the driver does

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 20 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-53 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-53 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-52-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-52-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 26 at HIGH**, report item **H4**, the item's only id. Report item M4, ids 6 and 11,
is the same reading at MEDIUM and is batched into `TOOL-dIndexedDesign-53`. `TOOL-dIndexedDesign-46` S11
says `check_spec_audit_declared` applies the driver's dated rule, then says "An undated value reads
absent", and says nothing of a conf it cannot evaluate. The driver does the opposite.
`tools/unattended/unattended.sh:3966-3982` refuses a present README `spec-audit:` value that is not a
date of four, two and two digits, such as `2026-10-01`, a bare one shown as `(empty)`, with `fail 52`. `:4022-4029` refuse a conf blob not
evaluated to its end with `fail 55`, and `:4030-4036` refuse a non-date `SPEC_AUDIT_DEFAULT` with
`fail 54`. Unit 46 AC9 makes `spec-audit: yes` printing no lens line the green result, so a standalone
`--design-exit` certifies "no audit owed" for a build whose owner tried to opt in.

This unit takes the report's sound fix. The reader answers each input class as the driver does, and only
a missing key reads absent. It repairs `TOOL-dIndexedDesign-46` and takes order 20, one above unit 46's 19.

## 2. Scope (IN)

- **S1** — An act ahead of this unit's order, in unit 46's pass commit. `check_spec_audit_declared` in
  `tools/memory-tree/gen_build_index.py` answers by the table in §4 Data model, which supersedes unit 46
  S11's "An undated value reads absent". A refusal makes `--design-exit` exit 2 and print the key, its
  source, `readme` or `project`, and the value. Unit 38 S22 already treats an exit other than 0 or 1 as a
  refusal. Unit 46's Edges block names this, and its builder reads it there. Observed by AC1 and AC2.
- **S2** — The conf read the driver's way. The `.unattended.conf` blob unit 46 S11 reads is evaluated by
  `bash` with the driver's sentinel: the key blanked first, the blob `eval`ed, two newlines, then a
  `printf "OK %s"` of the key on a descriptor the blob does not redirect. No sentinel means the read was
  cut short, which is a refusal and never absent. Observed by AC2.
- **S3** — Unit 46 AC9's second case reads "over a README carrying `spec-audit: yes`, `--design-exit`
  exits 2 naming `spec-audit`". Unit 46's acceptance ledger carries the note `TOOL-dIndexedDesign-52 S3`
  under AC9's answer. Observed by AC3.

## 3. Non-goals (OUT)

- The `review.design` source, the third route unit 3 reads: unchanged, consulted only when both of the
  others are absent.
- Unit 46 §8 F1's claim about AC9, the bare-line case's own record and a parity arm against the driver:
  report ids 6 and 11, MEDIUM, in `TOOL-dIndexedDesign-53`.
- The driver's `check_authorization`: unchanged; it is the reference this reader matches.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-46` — S11's `check_spec_audit_declared` and AC9, which S1 restates in that unit's pass commit and S3 supersedes (id 26)
- **consumes-from** `TOOL-dIndexedDesign-38` — S3's `check_spec_audit_declared` and S22's reading of a `--design-exit` exit 2 as a refusal, on which S1's exit rests (id 26)
- **hands-off** `TOOL-dIndexedDesign-53` — the restated reader, which that unit's parity arm runs beside the driver over one fixture set, and AC9's claim in unit 46 §8 F1 (ids 6 and 11)

## 4. Design

### Evidence

- `tools/unattended/unattended.sh:3966-3969`: a present non-date value is a refusal, because read as absent
  it "would silently opt a build out". `:3970-3976` show a bare `spec-audit:` as `(empty)` so it refuses
  too. `:3980` is `fail 52`.
- `:4022-4023` consult `SPEC_AUDIT_DEFAULT` only when the README has no `spec-audit:` line at all.
  `:4024-4029` evaluate the blob with the sentinel and refuse with `fail 55` when it is absent. `:4034` is
  `fail 54`. Read 2026-10-28.
- The driver's comment (`:3989-3991`) names the bug class a sed-style reader hits: two readers of one
  config, one re-derived, which read `KEY='v'`, a trailing comment and a last-wins pair differently.

### Data model

| Input | Driver | This reader |
|---|---|---|
| README `spec-audit:` a date shaped like `2026-10-01` | declared, readme | declared, readme |
| README `spec-audit:` any other value, empty included | `fail 52` | exit 2, `readme` |
| no README line; conf key a date | declared, project | declared, project |
| no README line; conf key any other non-empty value | `fail 54` | exit 2, `project` |
| no README line; conf blob not evaluated to its end | `fail 55` | exit 2, `project` |
| no README line; no conf, or the key blank | absent | absent, then `review.design` |

### Inventory

Minted: no identifier. The refusal text names the existing keys `spec-audit` and `SPEC_AUDIT_DEFAULT`.

### Migration

None: no build has run the standalone reader.

### Rollout

S1 and S2 land in unit 46's pass, order 19. Unit 46's Edges block names them. S3 and AC1 to AC3 are this
unit's own pass at order 20, alone at that order.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`: S1 and S2, in unit 46's pass, and its selftest arm
- `memory/builds/dIndexedDesign/build/`: S3's ledger note

### Alternatives rejected

- **Parse the conf with a line regex.** Lost to the driver's own comment: such a reader reads quoting,
  trailing comments and a last-wins pair differently from the shell, the two-readers class.
- **Call the driver for its derived value.** `--authorization` needs a run-state file, and the
  standalone `--design-exit` runs outside a run, which is why unit 46 §8 F1 chose the reader.
- **Drop the claim that S11 matches the driver.** Admitted by id 6's skeptic, but it leaves this finding
  open.

## 5. Production-readiness checklist

- security — closes a fail-open: an owner's malformed opt-in now refuses instead of reading absent.
- perf / scale — one `bash` evaluation of one small blob per run.
- error / empty / loading states — every non-date value and a cut-short read refuse, naming the source.
- observability — the refusal prints the key, its source and the value.
- risks — the sentinel idiom has two copies, the driver's and this reader's. The parity arm in
  `TOOL-dIndexedDesign-53` runs both over one fixture set, so they cannot drift silently.
- testing — AC1 and AC2 over scratch fixture repositories, AC3 by a ledger grep.
- migration — none.
- user docs — none under `help/`: the standalone reader has no page of its own.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --design-exit tFix` runs under
  `with-spec-audit` over a fixture README carrying `spec-audit: yes`, and again over one carrying a bare
  `spec-audit:`, it exits 2 each time, printing `spec-audit`, `readme` and the value, `(empty)` for the
  bare line. Over a README carrying `spec-audit: 2026-10-01` it prints a lens line.
  Red when: an undated value reads absent or declared, or a dated one refuses.
  fixture: scratch repositories under `%TEMP%/tfix-52`, which the tree does not hold today.
- **AC2** — When the fixture README carries no `spec-audit:` line and its `.unattended.conf` declares
  `SPEC_AUDIT_DEFAULT="soon"`, `--design-exit` exits 2 naming `SPEC_AUDIT_DEFAULT` and `project`. When the
  conf holds `return 0` before the key, it exits 2 naming the read as cut short. When the conf declares
  `SPEC_AUDIT_DEFAULT="2026-10-01"` followed by a last line `false`, it prints a lens line.
  Red when: a cut-short read reads absent, or a conf ending in `false` refuses.
- **AC3** — When `grep -n "TOOL-dIndexedDesign-52 S3"` runs over unit 46's acceptance ledger, it prints
  the note under AC9's answer, naming `spec-audit: yes`.
  Red when: the note is missing or stands as its own `- AC` line.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `policy fixtures` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 · the undated README values, the undated default and the cut-short conf, staged by reading an undated value as absent · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 26
  (HIGH, item H4), on its sound fix, repairing TOOL-dIndexedDesign-46 S11 and AC9.

## 10. Reuse audit

The seam is the driver's own read in `check_authorization` (`tools/unattended/unattended.sh:3966-4036`):
S1's table is its verdicts and S2 is its sentinel idiom. The probe
`python tools/codebase-map/reuse_lookup.py "evaluate a shell conf blob to its end and refuse when the read is cut short"`
ranked `read`, `read_text`, `load_conf` and `parse_conf`. Each parses a conf as text, the reading the
driver's comment rejects, so no existing python seam fits. `tools/hooks/agent-cap.js` `readConfKey` is a
third reader of the key, in JavaScript, and cannot be called from the generator.

Recall terms used: `python tools/memory-recall/query.py "how does the driver read SPEC_AUDIT_DEFAULT and refuse an undated opt-in" --terms "SPEC_AUDIT_DEFAULT spec-audit dated opt-in fail 52 fail 54 fail 55 sentinel evaluated to the end check_authorization"`
