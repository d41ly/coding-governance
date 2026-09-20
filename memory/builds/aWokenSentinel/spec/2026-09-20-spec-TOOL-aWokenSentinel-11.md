# TOOL-aWokenSentinel-11 — a kit-gate check that the driver holds ONE derivation of the sidecar root

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H3 (round 1, raw ids 4, 20 and 34): `TOOL-aWokenSentinel-2` introduces
`resolve_sidecar_dir` as the driver's ONE derivation of `<git-dir>/unattended`, "never respelled";
`TOOL-aWokenSentinel-5` S8 spelled `$(GIT rev-parse --git-dir)/unattended/resume.<slug>.log` inline
in `verb_status`; and `TOOL-aWokenSentinel-7` AC12 pinned `grep -c 'rev-parse --git-dir'` over the
driver at exactly 1 with a scope that extracts unit 2's copy only — so unit 7 either rewrote unit
5's line unscoped or redded its own criterion, a red with no owner. The audit's left-shift is the
disposition: the count-is-one assertion belongs to the kit gate, where it binds every unit rather
than one unit's pass. This unit adds that check to `tools/unattended/check-unattended.sh`, spec 5
S8 is folded at rev-2 to read through the function, and spec 7's AC12 is folded to cite this check.

## 2. Scope (IN)

- **S1** — A new check in `tools/unattended/check-unattended.sh`, the next free number above the
  gate's high-water (31 at base, DERIVED by `grep -oE 'fail [0-9]+'`), asserting that the literal
  `rev-parse --git-dir` occurs EXACTLY once in `$DRIVER` — the definition of `resolve_sidecar_dir` —
  and that `resolve_sidecar_dir` is called at least once outside its definition. Zero is the
  refusal too: a driver with no derivation and a sidecar reader is spelling the root some other
  way. Observed by AC1 and AC2.
- **S2** — The check's header states what it does NOT check: a second derivation spelled
  differently — `--git-common-dir`, a `$GIT_DIR` read, a path composed from `.git` — is invisible
  to it, and the sibling scripts (`resume-tick.sh`, the hooks) are outside its population by
  design, because each of those carries its own derivation in its own file. Observed by AC3.
- **S3** — The check is observed RED on a staged break — a driver copy with a second
  `$(GIT rev-parse --git-dir)` spelled inline, graded by a copy of the checker seeded beside it in
  a scratch kit dir, since `DRIVER` is derived from the checker's own location — and GREEN with the
  line removed, before it is wired. Observed by AC1.
- **S4** — The check joins the kit's own gate suite at the close: one arm in
  `check-unattended.test.sh` stages the second spelling and reads the refusal, and the harness-arms
  leg counts the new `fail` branch as armed. Observed by AC4.

## 3. Non-goals (OUT)

- **No driver change.** `resolve_sidecar_dir` is unit 2's, landed one order earlier; this unit
  reads it and adds nothing to the driver. At this order the count is 1 by unit 2's AC7.
- **No scan of `resume-tick.sh` or the hooks.** Each derives the git dir in its own file because a
  kit file names nothing outside itself and cannot source the driver's function without spawning
  it; the tick's own spelling is spec 5's, stated there.
- **No generalisation to other literals.** A "one spelling per derivation" gate over the whole
  driver is a lexicon-shaped project; this check binds the one literal two units in this build
  were about to spell twice.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-2` — `resolve_sidecar_dir`, the one derivation, and its
  AC7 count of `1` at unit 2's tip. Without it the check refuses on zero, which is the correct
  refusal on a driver that reads a sidecar with no derivation.
- **hands-off** `TOOL-aWokenSentinel-5` — reading `resume.<slug>.log` through
  `$(resolve_sidecar_dir)`, folded into spec 5 S8 at its rev-2; a second spelling there reds this
  check at the close.
- **hands-off** `TOOL-aWokenSentinel-7` — reading `stop.<slug>.log` through the same function,
  which spec 7 S9 already states; its AC12 is folded at rev-2 to cite this check rather than pin
  the count in one unit's pass.
- **hands-off** external — nothing.

## 4. Design

### The check

In `tools/unattended/check-unattended.sh`, after check 31, in the checker's own idiom (`# ---- check
<n>`, a `fail <n>` with a sentence that names the remedy):

```
n=$(grep -c 'rev-parse --git-dir' "$DRIVER" || true)
calls=$(grep -cE '^[^#]*\$\(resolve_sidecar_dir\)' "$DRIVER" || true)
[ "$n" -eq 1 ] && [ "$calls" -ge 1 ] || fail <n> "the driver must hold ONE derivation of the sidecar root — resolve_sidecar_dir — and read every sidecar through it; a second 'rev-parse --git-dir' is a second spelling that drifts from the first, and zero is a reader with no derivation. count: $n, callers: $calls"
```

`$DRIVER` is the checker's existing variable for the driver path, derived at
`tools/unattended/check-unattended.sh:69` as `$HERE/unattended.sh` — the driver BESIDE the checker,
never an argument — so the check reads whatever driver sits beside the copy of the checker that
runs, which is how its own suite grades a fixture: it copies the checker and a driver into a
scratch kit dir (`check-unattended.test.sh:65`) and runs the copy. The grep is over the file's
bytes, comments included, which is deliberate: a commented-out second spelling is the shape a
future edit uncomments.

### What it cannot see, in its header

- A derivation spelled without the literal: `git rev-parse --git-common-dir`, `${GIT_DIR}`, or a
  path built from `.git` by hand. The check binds the one literal this build's specs spelled.
- Sibling kit scripts. `resume-tick.sh` and the two hooks derive the git dir in their own files
  and are outside `$DRIVER`; a check over them is a different population with a different reason.
- Whether the one derivation is CORRECT — the worktree's git dir and never the common dir is unit
  2's AC7 and the audit arms' fixture, not this count.

### The staged break

A scratch kit dir under a short `%TEMP%` path seeded the way `check-unattended.test.sh` seeds
its fixture — the checker, the driver, the library and the two templates copied beside each other —
with one line appended inside the driver copy's `verb_status`,
`_x=$(GIT rev-parse --git-dir)/unattended`. The copied checker prints the new `fail` sentence with
`count: 2` and exits 1. The same copy with the line removed prints no failure for this check. The
suite's arm is that break, so the harness-arms leg counts the branch as armed. The checker runs
whole — `--only` selects check 28 and nothing else, because checks 1 to 27 share state — so each
observation costs one kit-gate run, 199 s on node `a` by the gate ledger on 2026-09-20.

### Inventory

| identifier | kind | cell |
|---|---|---|
| one `fail <n>` number | a check in the kit gate | derived at build time, next free above 31 |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.sh` | one check with its header |
| `tools/unattended/check-unattended.test.sh` | one arm: the staged second spelling reads the refusal; restored, the check passes |

### Alternatives rejected

- **Keep unit 7's AC12 as the gate.** It binds one pass of one unit and cannot see whose line
  made the count 2; the audit called it the right gate in the wrong place.
- **Assert `at most 1`.** Zero would then pass a driver that reads sidecars with no derivation,
  which is the vacuous-selector class charter §7 names.
- **Scan every `.sh` in the kit dir for the literal.** The tick and the hooks legitimately carry
  their own; a population-wide count of 3 or 4 is a number nobody can read a defect out of.

## 5. Production-readiness checklist

- security — N/A; a grep over a tracked script.
- perf / scale — two greps, milliseconds, inside a leg that already reads the driver.
- error / empty / loading states — an unreadable driver is check 1's refusal, before this one runs.
- observability — the refusal prints the count and the caller count, so a reader knows which
  direction failed.
- risks — a future derivation spelled differently passes; the header says so. The check reds the
  bar for any unit in this build that respells the root, which is its job and the reason it lands
  at order 3, ahead of the units that read sidecars.
- testing — the staged break of S3 in the pass; the suite's arm at the close.
- migration — additive; a new check number.
- user docs — none; the check's header.

## 6. Acceptance criteria

- **AC1** — When a scratch kit dir seeded as §4 states holds a copy of
  `tools/unattended/unattended.sh` at this unit's tip with one inline
  `$(GIT rev-parse --git-dir)/unattended` line added, the copied checker beside it prints
  `UNATTENDED check <n> FAILED` with `count: 2` and exits 1; with the line removed the same run
  prints no failure for that check.
  Red when: the second spelling passes, which is the check reading the wrong file or the wrong
  literal; or the unmodified driver fails, which is unit 2's count not being 1 at this order.
  fixture: a scratch kit dir under a short `%TEMP%` path, never this worktree.
  cost: one whole kit-gate run per observation, 199 s each on node `a` by the gate ledger on
  2026-09-20; the pass runs it twice, on the break and on the restored copy.
  figure: 199 is PINNED as read from `<git-dir>/gate-ledger.tsv` on 2026-09-20.
- **AC2** — When the copy instead has `resolve_sidecar_dir`'s one call site deleted so the count
  of callers is 0, the check fails naming `callers: 0`.
  Red when: a derivation nothing calls passes, which is a function that exists for the grep.
- **AC3** — When `grep -c 'does NOT check' tools/unattended/check-unattended.sh` is compared
  between this unit's base and tip, the tip is one higher, and the new check's header names
  `--git-common-dir` and `resume-tick.sh` as outside its reach.
  Red when: the header claims a semantic it does not have, which is the false-confidence class
  charter §7 names.
- **AC4** — When `python3 tools/memory-tree/check-arms.py --report` runs at the tip, filtered to
  `check-unattended.sh`, it lists the new `fail` branch as armed, and `grep -c 'count: 2'
  tools/unattended/check-unattended.test.sh` prints at least 1 and 0 at base.
  Red when: the branch is unarmed, which the `harness arms (fail branches armed or pinned)` leg
  reds at the close; or the arm exists but never reads the refusal's count.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the checker over the two
driver copies of AC1 and AC2 in a scratch clone and the greps of AC3 and AC4. Under
`unattended kit gate`, the new check is the arm this unit adds; under `harness arms`, its `fail`
branch is the count it moves.

New arm: `tools/unattended/check-unattended.test.sh` · the staged second spelling of the sidecar root in a driver copy, and the deleted call site · no floor exists in this suite

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H3 (raw ids 4, 20, 34).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "assert a shell driver holds one derivation of the
sidecar root and refuse a second spelling"` ranked `repo_root` in `tools/codebase-map/map_lib.py`
and `read_roots` in `tools/process-monitor/scope.py`, both Python root resolvers for other kits and
not a check over a shell driver, and reported `unscanned layers: .sh`; no existing seam fits. The
seam, read at source, is the kit gate itself: `tools/unattended/check-unattended.sh`'s `fail()` at
`:93`, its `$DRIVER` variable that check 1 refuses on, and check 22 at `:1685` to `:1726` as the
shape of a join whose failure sentence names both directions; and `resolve_sidecar_dir` as spec 2
§4 item 9 defines it. The recall probe returned `TOOL-aCandidStub-4` and `TOOL-aCollapsedScan-8`:
one root-resolution defect filed twice and a near-verbatim copy of a pre-fix resolver knowingly
left in a sibling kit — the two-spellings class this check binds for one literal.

Recall terms used: `rev-parse git-dir gate-logs sidecar worktree common dir second spelling drift one derivation check kit gate`
