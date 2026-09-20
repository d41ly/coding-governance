# TOOL-aWokenSentinel-10 — `STOP_GUARD_BLOCKS` declared in every carrier check 22 and spec 6 AC6 read

**Status:** CLOSED · rev-3 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-10-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-10-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-10-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-10-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H2 (round 1, raw ids 19 and 31): `TOOL-aWokenSentinel-3` adds
`STOP_GUARD_BLOCKS="12"` to the shipped conf example and assigns every protocol edit to unit 6,
while `TOOL-aWokenSentinel-6` §4 says each knob's section 8 row lands with the unit that reads the
key — so no unit adds the row, and check 22 of `tools/unattended/check-unattended.sh`, which joins
the example's `^[A-Z_]+=` keys against the rendered protocol's section 8 key column in both
directions, reds `undocumented in the protocol` from the hook's commit to the close. The same gap
left the root `.unattended.conf` line with no writer (audit M7, raw 24, folded into specs 3 and 6
to point here). This unit is the knob's DECLARATION SET, one commit: the example line, the kit
descriptor's `optional_keys` entry, the protocol's section 8 row with its render, and the root conf
line with its rationale and the kickoff-manifest re-stamp that edit owes.

## 2. Scope (IN)

- **S1** — `tools/unattended/.unattended.conf.example` gains `STOP_GUARD_BLOCKS="6"` with one
  comment line above it, beside `UNIT_STALL_BOUND`, on `GATE_BOUND`'s terms. The value is the
  hook's `BLOCKS_DEFAULT` as spec 3 pins it at rev-2. Observed by AC1.
- **S2** — `tools/unattended/kit.toml` `optional_keys` gains `STOP_GUARD_BLOCKS`. Observed by
  AC1.
- **S3** — `tools/unattended/PROTOCOL.template.md` section 8's key table gains one row for
  `STOP_GUARD_BLOCKS` on `UNIT_STALL_BOUND`'s terms — what it bounds, its default, that absent is
  announced and that a malformed value ALLOWS the stop with `knob-malformed` rather than refusing,
  the one divergence from the driver's rule — and `memory/guides/UNATTENDED-PROTOCOL.md` is
  re-rendered in the same commit. Observed by AC2.
- **S4** — The root `.unattended.conf` gains `STOP_GUARD_BLOCKS="6"` with a one-line rationale
  above it, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is re-stamped in the same
  commit with a delta line in the subject, because the conf is on the manifest's `watch:` line.
  Observed by AC3.
- **S5** — Check 22's three-way join is observed directly in the pass by the awk-cut section 8
  grep spec 5 AC6 already uses, over both the example's keys and the root conf's keys, so the
  pass sees now what the kit gate reds at the close. Observed by AC2.

## 3. Non-goals (OUT)

- **No hook change.** The hook's read, its default `BLOCKS_DEFAULT`, its NOTE and its
  `knob-malformed` allow are unit 3's; this unit declares the key the hook already reads.
- **No prose rationale beyond one line per file.** Unit 6 adds a rationale only where a unit left
  none; this unit leaves none absent for its key, so unit 6 does not touch it.
- **No other knob.** `RESUME_STALE_BOUND` is unit 2's declaration set, `RESUME_ATTEMPTS` and
  `RESUME_TURNS` are unit 5's; each declares its own key across the same four carriers.
- **No section 5 edit.** Unit 6's.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-3` — the hook that reads `STOP_GUARD_BLOCKS`, its
  default and its NOTE text. Without a reader a declared key is `documented and dead`, which is the
  other direction of the same check 22.
- **hands-off** `TOOL-aWokenSentinel-6` — nothing for this key; unit 6's AC6 finds the rationale
  line present and the key located in both conf files.
- **hands-off** external — nothing.

## 4. Design

### The four carriers

| carrier | line | reads it |
|---|---|---|
| `tools/unattended/.unattended.conf.example` | `# the stop-guard blocks a bound session's turn end at most this many times per run and session, then allows and says so; the harness itself ends a turn after 8 consecutive blocks, so a value above 8 is unreachable inside one turn` then `STOP_GUARD_BLOCKS="6"` | check 22's `undocumented`/`phantom` directions; adopters |
| `tools/unattended/kit.toml` `optional_keys` | the key appended to the list | `govkit` `requires_if` reads |
| `tools/unattended/PROTOCOL.template.md` section 8 | `\| \`STOP_GUARD_BLOCKS\` \| the cap on stop-guard blocks per run and session, kit default 6. OPTIONAL, on \`GATE_BOUND\`'s terms for absence: the hook says so on stderr; a malformed value ALLOWS the stop with \`knob-malformed\` on the sidecar line, because for a Stop hook a refusal is a block \|` | check 22's key column; readers |
| `.unattended.conf` | the same comment line, closed with this unit's id as every sibling knob's rationale line cites its own, and `STOP_GUARD_BLOCKS="6"` after `UNIT_STALL_BOUND` | check 22's `proj_extra` direction; the hook on this repo |

The render is `bash tools/unattended/adopt-unattended.sh`; check 10 byte-compares the pair at the
close and `--check` compares it now.

### The manifest re-stamp

`.unattended.conf` is on the `watch:` line of `memory/guides/SESSION-KICKOFF.md`. The commit
re-stamps `last-audit` with a delta line in its message, the shape units 2 and 5 already use for
their own conf keys. The stamp's sha is the ratchet's own rule, `HEAD` on the default branch and
`git merge-base origin/main HEAD` on a run branch — so on this branch it names the merge-base, not
this commit's parent, which is unreachable from `origin/main` — and it is the DATETIME that moves:
the ratchet's C5 reads a re-stamp as any commit whose block-scoped `last-audit` VALUE differs from
its parent's, at or after the newest watch-touching commit.

### The guide cap

The render sat at 61345 B against `GUIDE_CAP_BYTES=61440` at the pass's parent, so the one row this
unit owes lands it over hygiene check 6 and the pre-commit refused the commit. The pass lands the
row and a `memory/project/curation-debt.txt` entry for the render, the escape check 6 declares
(`memory/HYGIENE.md` check 6, "grandfather"): check-6-only on a guide, measured in the row, and
reported stale by the registry's own guard the run the cap moves past the render or the protocol is
split. The cap itself is a watched governance carrier and the template is the kit's binding
contract, so the owner call between raising the cap and splitting the protocol is PARKED on the
run-state record as `guide-cap TOOL-aWokenSentinel-10`, not taken.

### Inventory

No identifier is minted. `STOP_GUARD_BLOCKS` is unit 3's key; this unit declares it.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/.unattended.conf.example` | one comment line, one key line |
| `tools/unattended/kit.toml` | `optional_keys` +1 |
| `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md` | one section 8 row, re-rendered |
| `.unattended.conf` | one comment line, one key line |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |
| `memory/project/curation-debt.txt` | one row for the render, added at the build pass (rev-3) |

### Alternatives rejected

- **Leave the row to unit 6 as spec 3 §3 wrote.** Spec 6 §4 refuses it by rule and the audit
  measured the gap; the row belongs with the key.
- **Declare the key only in the example and the protocol, not the root conf.** Spec 6 AC6 requires
  the key located in `.unattended.conf`, and this repo dogfoods the hook, so the announced default
  would print on every bound stop here forever.

## 5. Production-readiness checklist

- security — N/A; declarations in tracked text.
- perf / scale — N/A.
- error / empty / loading states — an adopter that never copies the example keeps the announced
  default; the row documents both the absence and the malformed case.
- observability — check 22's failure line names any direction that disagrees; the awk-cut grep of
  AC2 is the same join read by hand.
- risks — a value typed differently in the example and the root conf is not a defect check 22 can
  see; AC3's grep pins both at `6`.
- testing — §6; greps and `--check`, seconds.
- migration — N/A; an optional key with a default.
- user docs — the protocol row and the example comment are the docs.

## 6. Acceptance criteria

Each criterion is a grep or `--check` over a tracked file, seconds. Figures at base are read by
`git show <base>:<path>` at this unit's own order base.

- **AC1** — When `grep -c '^STOP_GUARD_BLOCKS="6"$' tools/unattended/.unattended.conf.example`
  runs it prints 1 and 0 at base; `grep -c 'STOP_GUARD_BLOCKS' tools/unattended/kit.toml` prints
  1 — the `optional_keys` line — and 0 at base; the line above the key in the example starts with
  `#`.
  Red when: the key is absent from the descriptor, which `govkit` cannot see and check 22 does not
  read; or the value differs from the hook's `BLOCKS_DEFAULT`, which is two defaults.
- **AC2** — When the section 8 region of `memory/guides/UNATTENDED-PROTOCOL.md`, cut by
  `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'`, is grepped for `STOP_GUARD_BLOCKS` it prints 1 and
  0 at base; the same over `tools/unattended/PROTOCOL.template.md` prints 1; and every key matched
  by `grep -oE '^[A-Z_]+=' tools/unattended/.unattended.conf.example` and by the same over
  `.unattended.conf` is found in that region, which is check 22's join read by hand.
  Red when: a key is declared in either conf and absent from the table, which check 22 reds at the
  close as `undocumented in the protocol` or `set by this project and undocumented`.
- **AC3** — When `grep -c '^STOP_GUARD_BLOCKS="6"$' .unattended.conf` runs it prints 1 and 0 at
  base, the line above it starts with `#`, and `git show --name-only --format= HEAD` on the pass
  commit lists `.unattended.conf` together with `memory/guides/SESSION-KICKOFF.md`, whose
  `last-audit` value differs from its parent's and names the sha of `git merge-base origin/main
  HEAD` at the commit, and whose message carries the `manifest-audit:` delta line.
  Red when: the conf moved without the stamp, which `kickoff-manifest ratchet` reds at the close;
  or the rationale line is absent, which reds spec 6 AC6 at its order.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the render, it
  prints `in sync` and exits 0.
  Red when: the template moved and the render did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These run once at `--close`. The pass runs none of them: it verifies with the greps of AC1 to AC3
and the adopter's `--check`. Under `unattended kit gate`, check 22 is the join this unit moves and
check 10 the parity it keeps.

New arm: none — check 22 is the arm, existing; this unit is the row it was reading for.

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-09-20 · §4, AC3 · at the build pass: the stamp rule read "this commit's parent or a
  later sha", which the ratchet's own rule (`HEAD` on the default branch, else the merge-base) and
  the charter's §1 both contradict on a run branch — the merge-base is an ANCESTOR of the parent,
  and the parent can never be the stamp because the ratchet's `STAMP_SHA_RULE` names the
  merge-base; AC3 now reads the moved VALUE at the merge-base, which is what C5 grades. §4's root
  conf row gains the unit-id suffix every sibling rationale line in `.unattended.conf` carries.
  AMEND (add): the render crossed `GUIDE_CAP_BYTES` by 193 B on this row alone, which speccing did
  not measure; §4 "The guide cap" and the files-touched table take the `curation-debt.txt` row and
  the parked owner call. Status CLOSED.
- rev-2 · 2026-09-20 · §1 · folded at the M4 disposal of spec-audit round 2: no finding of that
  round names this unit; L2 (raw 30) was spec 3's residue and is folded there, so spec 3 AC2 now
  carries the one literal `block 1/6` this unit's S1 declares. Order 7 → 9 for the insertions of
  units 20 and 16.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H2 (raw ids 19, 31); takes the example line and the `optional_keys` entry from spec
  3 S5 and the root-conf line from spec 6 S5, both folded at their rev-2 to point here.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a conf knob in the protocol key table, the
example, the kit descriptor and the root conf"` returned no seam and `unscanned layers: .sh`. The
seam is the declaration set the sibling knobs already use, read at source: `UNIT_STALL_BOUND` at
`tools/unattended/.unattended.conf.example:41` and `.unattended.conf:40` with their comment lines,
the `optional_keys` list at `tools/unattended/kit.toml:92`, and the section 8 row for
`UNIT_STALL_BOUND` in `tools/unattended/PROTOCOL.template.md`, whose terms this row copies. The
recall probe's top hit is `TOOL-aHoistedPass-40`: the kit gate's import allow-list is a fourth
hand-typed spelling of the conf key set that check 22 does not join — a hook reads its key by its
own reader and never passes the driver's `case`, so that row does not bind this key, and it is
cited so the next reader knows why.

Recall terms used: `check 22 section 8 key table example optional_keys undocumented phantom proj_extra conf knob manifest watch re-stamp`
