# TOOL-aBatchedLintel-1 — build record

**Serves:** journal TOOL-aBatchedLintel-1

Node `a`, 2026-08-03, base `e8d046cc`. Ports inCMS `PERF-aSlothfulCapstan-1` into the memory-tree
kit. Spec: `../spec/2026-08-03-spec-aBatchedLintel-1.md`. Review: `../reviews/2026-08-03-review-TOOL-aBatchedLintel-1-1.md`.

## Result

Checks 12 and 7 each collapse from a per-file fork storm to ONE `awk` over a driver stream.
Measured before and after in the SAME session on a quiet box, per-check timers around each
`# N —` block:

| check | before | after | factor |
|---|---|---|---|
| 12 spec ratchet | 7.03s | **0.57s** | 12.3× |
| 7 entry budget | 1.06s | **0.14s** | 7.6× |
| combined | 8.09s | **0.71s** | **11.4×** |

Whole-script CPU (`user`+`sys`) fell 14.78s to 10.76s in the same pair of runs. Wall-clock is not
reported as a result: the unmodified engine measured 16.0s, 27.4s, 102.8s and 2m3.5s on this machine
across sessions with no code change, and the AFTER run's wall was HIGHER than the BEFORE run's in the
very pair that produced the CPU numbers above. The engine is `sys`-bound, so every other agent on the
box moves it. AC6 was written against `user`+`sys` for exactly this reason.

## What differs from upstream, and why

The kit is not a copy of inCMS's script and the port is not a copy of its diff.

- **Nine sections, no window.** The kit compares against one nine-heading canon, so upstream's `win`
  flag, its `c9` variant and its `SPEC10_CUTOFF` branch have no meaning here and were not imported.
- **The canon rides on `awk -v canon=`, not on `C` driver records.** Upstream needed records because
  it derived two variants from one generated FILE. The kit has one inline string and one equality, so
  the records bought nothing — and they were the sole source of a TAB-truncation hazard and of the
  runtime guard against it. Dropping them removed the hazard, the guard and a tag. This was the
  review's F11 and it is the one place the port is SIMPLER than its source.
- **The `lrev` awk keeps its missing `/^## /{f=0}` reset.** Upstream has the reset; the kit does not.
  Adding it is a VERDICT change rather than a tidy-up — check 12 runs the rev scan on non-conforming
  specs, because the canon-differ branch emits and does not `continue`, so a `## 10.` heading carrying
  `rev-99` after §9 yields a high-water of 99 without the reset and 1 with it. The reset can only
  shrink the scanned range and therefore only produce MORE findings. Deferred as
  `TOOL-aBatchedLintel-2`.
- **Interval expressions are spelled out** character by character. On a build that does not honour
  `{8}` the header regex would demand those literal bytes and never match, redding every post-cutoff
  spec — a loud break of a check that works today under `grep -E` everywhere.
- **Check 7 takes no locale prefix**, stated in the code because check 8's `LC_ALL=C xargs -r awk`
  sits seventeen lines below and is the obvious thing to copy. It sorts; it does not measure.

## The divergence carried over

`body=$(_unfenced "$f")` is the oracle and command substitution DROPS trailing newlines. The §8
extraction reproduces `sed '1d;$d'`, whose deletes act on the CONCATENATED range output, so a body
array that keeps its trailing blanks moves which line the last delete removes — inventing a finding
on a terminal spec whose §8 is the last section. Carried as `while (n > 0 && body[n] == "") n--`,
pinned by self-test fixture 16 and harness shape 08.

The review additionally required the two range behaviours upstream states but no fixture had covered:
the range RESTARTS on a later opener (Shape A) and runs to EOF when §9 never follows (Shape B). Both
are in the harness corpus; both distinguish a correct implementation from a plausible one.

## Verification

**Parity** — `tools/memory-tree/hygiene-parity.test.sh e8d046cc`: byte-identical stdout and exit code
between the pre-change and post-change engines, over the real tracked tree with violations injected
(12 specs, 4 findings) AND over 28 pathological shapes (27 check-12 findings, 4 check-7 findings), in
FULL and in `--staged` mode. It refuses a run whose two sides are the same bytes, anchors its
finding-count floor on the eight message texts checks 12 and 7 emit rather than on a path shape, and
carries a planted-difference arm proving it can fail.

**Self-test** — `check-memory-hygiene.test.sh`: 14 assertions to **37**. All 14 originals pass
UNMODIFIED; the new arms are additive, which is the form AC4 takes after the review showed a raw
count cannot distinguish new coverage from deleted coverage.

**Mutation battery** — 24 single-assertion breaks, literal string replacement, each asserted to have
APPLIED before the self-test runs. Final: **24 killed, 0 survived, 0 not-applied.** Three survived
the first pass and each was a real gap rather than a false alarm: two because nothing asserted the
diff EXCERPT, one because the `--staged` arm exercised only check 12's `in_scope` and not check 7's.
All three closed and re-checked.

**Version** — `1.3` to `1.4` at all four live sites, not the two `check-kit-versions.sh` reads.
`grep -rn 'memory-tree@1\.3'` returns nothing outside build records.

## Gotchas banked

**Two of the new source-level assertions were wrong on their first run, and both were the catalogued
class.** The interval ban matched the `) {` that opens each if-block, flagging lines that contain no
interval at all; the `LC_ALL` ban fired on the comment explaining the ban. Both were fixed by running
the predicate over the real tree and then proving it still catches a deliberately reintroduced `{8}`
and a deliberately added `LC_ALL=C`. Running a new gate predicate over the real tree BEFORE trusting
it is the whole lesson.

**The upstream survivor is dead here.** On inCMS, deleting check 12's CR strip survived the entire
fixture suite, because Cygwin's runtime strips CR before awk sees a byte and no fixture on that
platform can tell. Porting the LESSON — a source-level assertion that every `getline` loop carries
the strip — rather than the fixture is what killed it in the kit.

**The review's one blocker was false.** It reported the spec file absent from disk. The file was
present the whole time; the finder agents ran `git status` and relative `find` without entering this
repository, so they saw the orchestrator's working directory instead. Every claim they made by
ABSOLUTE path was correct, and eleven of them were real defects.
