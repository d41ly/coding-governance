# 2026-07-16 — `bThriftyBellows` (node b): memory-tree kit 1.2 — hygiene-gate fork-collapse port

Port of BOTH upstream inCMS optimization rounds (ARCH-aFencedNamespace-3 + PERF-eThriftyBellows-1)
into `tools/memory-tree/check-memory-hygiene.sh`. The 1.1 kit still had every slow pattern; the gate
is process-creation-bound on Windows/MSYS, so fork COUNT is the cost, not compute.

## What changed (all byte-identical to 1.1 output)

- Membership (legacy/debt/staged): grep-per-call here-strings → associative-array lookups.
- Check 2 link integrity: 3 forks PER FILE → one awk pass (fence semantics + the sed fall-through
  for anchor-only links preserved exactly).
- Check 4 build-folder shape: `O(build-folders × files)` per-folder rescan + per-entry grep → one
  grep+awk per discipline; conf-aware (`FAM_ALT` injected, folder field index derived from
  `MEMORY_ROOT`'s segment count — the old hardcoded `NF==5` mis-parsed a multi-segment root; that
  latent-bug fix is the ONE deliberate semantic divergence, unreachable with a single-segment root).
- Check 5: basename+awk+grep per recording file → bash builtins + `[[ =~ ]]`.
- Checks 6/7: `index_set` memoized (was recomputed per check) + `wc` batched (2 forks total, not 2/file).
- Check 8: 3-fork-per-row token count → one awk; `nmatch()` replicates `grep -oE '…\b' | wc -l`
  exactly (caret branch anchors once; trailing `\b` checked zero-width so it never consumes the next
  delimiter) — validated 0 mismatches over the upstream tree's 589 real backlog/STATUS rows.
- Check 12: rev-log max chain (5 forks) → one awk. Stale-line guards: `git ls-files --error-unmatch`
  per grandfathered line → one `git ls-files` + set lookup, skipped entirely when both lists are empty.
- Kit version 1.1 → 1.2 (engine constant + the `HYGIENE.template.md` marker pair, per check-kit-versions).
- `gen-memory-tree.sh` NOT touched: a cache-and-grep rewrite measured SLOWER than per-call
  `git ls-files` upstream (9.0s vs 12–14s, controlled 3-run min — git's mmap index reads win);
  only a single-pass generator would help → TOOL-bThriftyBellows-2.

## Verification

OLD (HEAD) vs NEW golden diff IDENTICAL across three targets, full + `--staged`:
(a) a scratch fixture repo firing checks 1–12 incl. membership/stale-guard/tombstone paths across
two disciplines (44 / 19 / 27 finding lines); (b) this repo's dogfood tree (clean, 0 lines);
(c) the inCMS 1,487-file tree under the kit defaults — 292 finding lines byte-identical.
Timing on (c): **OLD 2647.5s → NEW 33.9s (~78×)**. Kit self-test 14/14 assertions.

## Gotcha banked

Do NOT "optimize" the per-subdir `git ls-files` calls (gen-memory-tree) by caching the list and
grepping per call — measured slower. The fast path for many-small-listings IS git; the fast path for
per-item validation is one awk. They are opposite lessons from the same investigation.
