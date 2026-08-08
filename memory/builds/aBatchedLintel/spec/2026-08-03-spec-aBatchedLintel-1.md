# TOOL-aBatchedLintel-1 — memory-tree kit: collapse checks 12 and 7 to one awk each

**Status:** INPROGRESS · rev-3 · 2026-08-03 · node a · Tier-2 · base e8d046cc

## 1. Goal

`tools/memory-tree/check-memory-hygiene.sh` spends roughly thirteen forks per spec file in check 12
and two per index file in check 7, the two cost centres the previous collapse round
(`TOOL-bThriftyBellows-*`) did not reach. Measured on this repo they are 42.88s and 7.86s of a run
whose other ten checks total 31.03s. Upstream took the same code from 257.8s to 1.66s at 356 specs;
this port brings the fix, and the verification method that makes a gate rewrite safe, into the kit
every adopter installs.

## 2. Scope (IN)

- S1 Rewrite check 12's per-spec loop as ONE `awk` over a tagged driver stream of paths, reproducing
  every per-file fork it spends today: the `_unfenced` fence machine, the five-line status-header
  extraction, the header-shape assertion, the skeleton placeholder scan, the `WONTDO` header-tail
  assertion, the `^## ` section-canon comparison, the empty-section scan, the §9 revision-log
  maximum, and the §8 `sed` range extraction for a terminal status.
- S2 Rewrite check 7's per-file `_unfenced "$f" | awk` pair as ONE `awk` over the selected index
  files, preserving three things: the unfenced-stream line numbering the current `FNR` produces, the
  dynamic `$ex7` exemption that depends on `$MAP_SUB`, and — stated explicitly because the file
  contains a counter-example — **no `LC_ALL=` prefix and no `xargs` wrapper that sets one.**
  Locale-dependent `length()` is the current, deliberate behaviour. Check 8's `LC_ALL=C xargs -r awk`
  at `:259`, seventeen lines below, is not the pattern to copy here.
- S3 Carry the trailing-blank strip. `body=$(_unfenced "$f")` is the ORACLE, and command substitution
  drops trailing newlines, so the batched form must re-apply that or it changes the §8 verdict.
- S4 Port the differential parity harness as `tools/memory-tree/hygiene-parity.test.sh`, carrying the
  upstream review's corrections: it refuses a run whose two sides are the same bytes, its
  finding-count floor is anchored on the message texts checks 12 and 7 emit, and it runs **both full
  and `--staged` mode** with a guard that the staged run actually produced a finding, so the
  comparison cannot pass vacuously on empty output.
- S5 Extend `tools/memory-tree/check-memory-hygiene.test.sh`. It has **14 assertions today, all of
  them check-12 fixture classes** — the ratchet is the file's entire subject. The gaps this unit must
  close are check 7 (zero coverage), the source-level trailing-CR assertion, a `--staged` arm, an
  interval-expression source assertion, and the byte-versus-character row of S2.
- S6 Bump the kit version `1.3` to `1.4` at **all four** sites carrying it, not the two the version
  gate enforces. See §4.
- S7 Add per-check timing instrumentation to the build record, so the before-and-after observation
  AC6 demands can actually be made.
- S8 Record the unit: `memory/tooling/DECISIONS.md`, `memory/tooling/BACKLOG.md`, the node `a` ledger
  row, and this build folder.

## 3. Non-goals (OUT)

- Changing any verdict. This is a pure performance port; an output difference is a bug in this unit.
- The other ten checks. The axis is **growth, not magnitude** — check 3 costs 11.35s here, which is
  more than check 7's 7.86s, so magnitude alone would pull it in. Only checks 7 and 12 are
  O(files); check 3 forks per top-level entry and per discipline at `:125`, which is O(disciplines)
  and flat as an adopter tree grows, and check 10 forks three times per rotated archive at
  `:291-293`. Those two line ranges are named here so a later sweep does not re-find them as
  oversights.
- Check 9. `TOOL-bThriftyBellows-2` records a measured negative result for the cache-and-grep shape;
  only a single-pass generator would help, and that is its own unit.
- The `SPEC10_CUTOFF` transition-window logic from upstream. The kit's canon is NINE sections with no
  window, so that branch does not exist here and must not be imported.
- Adding the `/^## /{f=0}` reset to the §9 rev scan. It is a verdict change, not a tidy-up — see §8.
- Any result cache, and any widening of what the checks assert.

## 4. Design

The kit's script is already partly collapsed. `check-memory-hygiene.sh:94` carries the driver-stream
`while ((getline line < f) > 0)` idiom in check 2, ported from inCMS `ARCH-aFencedNamespace-3`, and
checks 4, 6 and 8 were collapsed by `TOOL-bThriftyBellows-*`. This unit wires through that existing
idiom rather than inventing a second shape; after it, the script holds three such loops.

### Inventory

Every row measured on this repo at base `e8d046cc`, except where marked as upstream's.

| what | value |
|---|---|
| spec files entering check 12's per-spec body | 12 |
| spec files matching the check-12 glob at `:325` | 13, one of which is pre-cutoff |
| files under `builds/*/spec/` in total | 16, the other 3 legacy-named and never matching |
| tracked files under `memory/` | 75 |
| forks per spec in check 12 | about 13, upstream's count of upstream's larger check 12 |

Per-check wall time, timers injected around each `# N —` block, measured **while several review
agents were running on the same box**:

| check | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s | 0.46 | 2.45 | 11.35 | 5.34 | 2.58 | 4.50 | **7.86** | 1.84 | 0.87 | 1.38 | 0.26 | **42.88** |

Checks 12 and 7 are 50.74s of 81.77s, a hair over 62% of the run. That ratio is the stable quantity.
The absolutes are not: the same two checks measure 7.03s and 1.06s on a quiet box, so this table runs
roughly 6× hot. It is kept as measured, with its conditions stated, because the ratio is what the
scope argument rests on — and because a table presented without its load conditions is exactly the
kind of number a later reader would trust wrongly.
The wall total is not: the unmodified script measured 27.4s, 102.8s and 2m3.5s across three sessions
on this machine with no code change, because it is `sys`-bound and every other agent on the box moves
it. Two independent instrumented runs agreed on the RANKING of all twelve checks while their absolute
seconds differed by roughly 2×. §6 pins acceptance on deterministic quantities for this reason.

### Data model

Check 12's `awk` reads a driver stream of tagged paths on stdin, built in the shell:

| tag | payload | meaning |
|---|---|---|
| `M` | a path | tracked and in scope, absent from the worktree |
| `P` | a path | analyse |

**The canon is passed with `awk -v canon="$SPEC_CANON"`, not as driver records.** Upstream needed
`C<TAB><heading>` records because it derived a nine- and a ten-heading variant from one generated
FILE. The kit has one inline nine-line string and one equality comparison, so the records buy
nothing — and they were the sole source of a TAB-truncation hazard and of the runtime guard against
it. Dropping them removes the hazard, the guard, and a tag. If a TAB invariant is still wanted it
belongs beside S5's CR assertion as a source-level check, which is the mechanism this unit already
chose for the sibling hazard.

Tagging in bash rather than switching on `ARGIND` stays: `ARGIND` is gawk-only, and upstream recorded
a byte cap that silently did not exist under mawk because of it.

**Every interval expression is spelled out character by character in the batched awk.** The regexes
this port moves out of `grep -E` and into awk carry them — `:332` has `[0-9]{4}-[0-9]{2}-[0-9]{2}`
and `[0-9a-f]{8}`, `:338` has `[0-9a-f]{8,}`. Interval support is not universal in awk, and on a
build that treats `{8}` literally the header regex demands the literal bytes `{8}` and never matches,
so every post-cutoff spec reds with "missing/invalid **Status:** header". The failure is loud rather
than silent, and mawk 1.3.4 and busybox awk both honour intervals, so the exposed population is
narrow — but the kit ships to arbitrary adopters and the prophylaxis is one line of care.

### The divergence this port must carry

`body=$(_unfenced "$f")` is the oracle, and command substitution DROPS trailing newlines, so the old
body ends at its last non-empty line. The §8 extraction reproduces
`sed -n '/^## 8\. Open questions/,/^## 9\. /p' | sed '1d;$d'`, and the two deletes act on the
**concatenated range output**. A body array that keeps its trailing blanks moves which line `$d`
removes: for a terminal spec whose §8 is the last section, the old code deletes the unresolved entry
and stays silent, while the array version surfaces it and emits a finding the gate never emitted.

The fix is `while (n > 0 && body[n] == "") n--` immediately after the read loop.

The range has three further properties that decide the same verdict, and each must be reproduced:

- It **restarts** on every later `/^## 8\. Open questions/` match.
- It runs to **EOF** when `/^## 9\. /` never matches after the opener.
- A range shorter than three lines yields nothing, because both deletes land inside it.

Two shapes distinguish a correct implementation from a plausible one, and both are required members
of AC2's corpus:

- **Shape A** — the §8 heading twice, first body empty. The real pipeline yields
  `## 8. Open questions`, matching none of `none*`, `N/A*` or empty, so it FINDS. A per-range
  implementation that drops both headings yields `none` and stays silent.
- **Shape B** — `## 8. Open questions`, then `- unresolved`, then `## 10. Appendix`, with no §9. The
  range runs to EOF and `$d` removes the `## 10.` line, so `- unresolved` survives and it FINDS. An
  implementation that stops at the next `^## ` heading drops it as the range's last line and stays
  silent.

### Rollout

One commit on a feature branch, no flag. A gate cannot be half-enabled; the parity harness and the
extended self-test are what make the landing safe, and both run before the merge ask.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | checks 12 and 7 rewritten; version constant and its inline marker |
| `tools/memory-tree/check-memory-hygiene.test.sh` | check-7, CR, interval, `--staged` and byte-vs-char arms |
| `tools/memory-tree/hygiene-parity.test.sh` | new |
| `tools/memory-tree/HYGIENE.template.md` | the `gov:kit memory-tree@` marker |
| `memory/HYGIENE.md` | this repo's own installed marker, which the version gate does NOT read |
| `memory/tooling/DECISIONS.md` and `BACKLOG.md` | the records |
| `memory/project/in-flight/a.md` | the ledger row |

The version lives in four live sites and `tools/check-kit-versions.sh` reads only two of them — the
constant at `:21` and the template marker at `:31`. The two it cannot see are the inline
`gov:kit memory-tree@` comment on the engine's own constant line, and this repo's installed
`memory/HYGIENE.md` marker. That gap has bitten before: `git show d510bc7` records the previous bump
as "constant + both markers agree; also fixed HYGIENE.md's stale @1.1", meaning the installed marker
had silently missed a whole version.

### Alternatives rejected

**Copying the upstream awk verbatim.** It carries the `win` flag, the `c9` nine-heading variant, a
`CANON_FILE` read and the `C` canon records, none of which exist or are needed here.

**Reproducing `diff`'s output inside awk** for the section-canon excerpt. That needs a
longest-common-subsequence implementation, and the mismatch path fires zero times on a clean tree.

**Leaving check 7 alone because it is only two forks.** Two forks times the index-set size is the
same growth shape as check 12, and the collapse is a few lines once the driver idiom is present.

## 5. Production-readiness checklist

- security: N/A — the script reads tracked documentation and writes nothing; no new input reaches a
  shell.
- perf / scale: the point of the unit, pinned by AC6 on deterministic quantities rather than wall
  clock.
- a11y: N/A — no user interface.
- i18n: the check-7 locale constraint of S2 is the live concern, and it is adopter-side: this node
  has `LANG` empty and `LC_ALL` unset, so gawk is already in byte mode and `LC_ALL=C` is a no-op
  here. A UTF-8-locale adopter is where the flip shows. The literal middot bytes inside the awk
  patterns must also stay literal, because awk has no `\u` escape.
- error / empty / loading states: an empty selected set must not hand awk an untagged blank record.
  Both checks need the explicit `[ -n ... ]` guard, since neither driver is self-priming once the
  canon moves to `-v`.
- observability: unchanged. Findings keep their exact current text, which is what the self-test and
  every adopter's hook grep for.
- risks (concurrency, data-loss, rollback hazards): the risk is a silently weakened gate, covered by
  AC1 through AC5. No data-loss surface. Rollback is one revert.
- testing + left-shift gates: S4 and S5. `check-memory-hygiene.test.sh` already rides the gate suite,
  so the new arms run on every bar.
- migration / rollback: N/A — no stored state. Adopters pick the new engine up when they re-copy the
  kit; the version bump is what tells them it moved.
- user docs: `HYGIENE.template.md` carries the version marker and needs no behavioural edit, since no
  rule changes. `WIRE-INTO-PROJECT.md` needs no change — the new harness is a kit-internal tool.

## 6. Acceptance criteria

- AC1 When the pre-change and post-change scripts are run over a mutated copy of this repo's real
  memory tree carrying a violation of every check-12 assertion class, stdout and exit code are
  byte-identical **in both full and `--staged` mode**, and the run is asserted non-empty first.
- AC2 When the same comparison runs over a corpus of pathological spec shapes, stdout and exit code
  are byte-identical. The corpus must include a terminal spec whose §8 is last followed by trailing
  blank lines, Shape A and Shape B of §4, and one index row that is at most 300 characters but more
  than 300 bytes.
- AC3 When the parity harness is given two identical scripts, it refuses and exits non-zero instead
  of reporting a pass.
- AC4 When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, **all 14 existing assertions
  still pass unmodified** and the new arms are strictly additive. A raw count cannot distinguish new
  coverage from deleted coverage, so the floor is on the surviving set, not on a number.
- AC5 When each assertion of the two new awk programs is mutated one at a time, the self-test reds
  for that mutation, and the mutating step asserts the mutation actually applied to the source.
- AC6 When check 12 and check 7 are measured before and after **in the same session on the same
  machine**, their combined `user`+`sys` falls by at least 10×, and the fork count attributable to
  the two checks falls from O(files) to O(1). Wall-clock is explicitly NOT the criterion: the
  unmodified script measured 27.4s, 102.8s and 2m3.5s on this machine with no code change.
- AC7 When `bash tools/check-kit-versions.sh` runs after the bump it passes, **and**
  `grep -rn 'memory-tree@1\.3'` over the worktree returns nothing. The gate reads two of the four
  sites, so it alone cannot prove the bump landed.
- AC8 When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

- `memory/` hygiene — `tools/memory-tree/check-memory-hygiene.sh`, must stay green and get faster.
- kit self-test — `tools/memory-tree/check-memory-hygiene.test.sh`, extended by S5.
- kit version markers — `tools/check-kit-versions.sh`, which S6 must keep green.
- the full suite — `bash tools/run-gates.sh`.
- The new `tools/memory-tree/hygiene-parity.test.sh` is run by hand for this unit; §8 asks whether it
  should be wired.

## 8. Open questions

- **Q1 — should `hygiene-parity.test.sh` become a gate leg?** It needs a before-revision to compare
  against, and that reference rots as soon as anything else edits the engine. Recommendation: ship it
  as a kit tool, documented, but do NOT add it to `tools/gate-legs.json`. The standing protection is
  the self-test, which needs no baseline.
- **Q2 — how far should the self-test grow?** Against the true baseline of 14 check-12 assertions,
  the menu is the gaps rather than a target count: check 7's unfenced line numbering with its three
  exemptions, the 300-versus-301 threshold from both sides, the byte-versus-character row, the
  source-level CR assertion, the source-level interval assertion, and a `--staged` arm.
  Recommendation: all six, since each pins a distinct way this port can be wrong.
- **Q3 — the missing `/^## /{f=0}` reset in the `lrev` awk.** rev-1 called adding it
  behaviour-neutral. That was wrong, and the review reproduced the counter-example: check 12 runs the
  rev scan on NON-conforming specs too, because the canon-differ branch at `:344-347` emits its
  finding and does not `continue`. Against a file carrying `## 10. Appendix` and the text `rev-99`
  after §9, the current no-reset awk yields a high-water of 99 and the reset yields 1 — and since the
  reset can only shrink the scanned range, it can only produce MORE findings. That is a verdict
  change, which §3 forbids and AC1 and AC2 would fail. Two branches, and this is the OWNER's call:
  (a) a `BACKLOG` row for a separate unit that owns the verdict change and its fixture, or (b)
  explicitly carve the rev scan out of AC1 and AC2 in this unit and add a fixture pinning the new
  verdict. Recommendation: (a), because it keeps this unit's "no verdict changes" invariant intact.
  Tempering fact: both awk variants were run over every spec in this corpus with zero divergence, so
  no committed file has a heading after §9 today.

## 9. Revision log

- rev-1 · 2026-08-03 · initial draft, written against `check-memory-hygiene.sh` at base `e8d046cc`.
- rev-2 · 2026-08-03 · folded all eleven findings of review `wf_1b771a5c-a41`. Corrected the
  self-test baseline from 4 to 14 and re-pointed S5 at the real gaps; added the check-7 locale
  constraint; replaced AC6's wall-clock threshold with `user`+`sys` and fork count and added the
  measured per-check table; corrected every §4 count; rewrote Q3 after its premise was refuted;
  enumerated all four version sites; added the interval-expression rule, the full `sed`-range
  semantics with Shapes A and B, and `--staged` coverage; replaced the `C` canon records and their
  TAB guard with `awk -v canon=`. The review's one unconfirmed precondition, that this file was
  absent from disk, was checked and is false — the finder agents resolved relative paths against a
  different repository.
- rev-3 · 2026-08-03 · built. Marked the §4 per-check table as measured under load, since the same
  two checks are 7.03s and 1.06s on a quiet box and an unlabelled table would be trusted wrongly.
  Status to INPROGRESS: built and verified on a branch, not yet merged.
