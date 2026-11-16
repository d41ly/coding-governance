# TOOL-aPiecewiseGrade-8 — two permanent arms hold the spec-token checker's counter key-set guards

**Status:** CLOSED · rev-1 · 2026-11-16 · node a · Tier-1 · base aebbb4a72 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-build-TOOL-aPiecewiseGrade-8-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-aPiecewiseGrade-8-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-8-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-8-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-8-review-brief.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-8-review-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aPiecewiseGrade-5 added two guards on the per-spec counter key set: a cache miss in
`read_spec_cache` and a `KeyError` in `main`. A scratch probe that the pass then removed was the only
thing that observed them, so deleting either guard leaves the spec-tokens suite green. This unit adds
one permanent suite arm per guard. The source is item 2 (id 2, low) of
`2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2`, built to its class-level fix.

## 2. Scope (IN)

- **S1** — The cached short-set arm. Over the PG1 fixture's warm cache, it takes `ao_bad` out of the
  `counts` of `$pg_a`'s entry. It then expects `$pg_a` in the run's `graded.list`, and the cached run's
  stdout, stderr and exit status to equal the plain run's. Observed by AC1.
- **S2** — The fresh short-set arm. It loads the fixture's checker copy through `importlib`, wraps
  `scan_live_spec` so that the `counts` it returns lack `ao_bad`, and calls `main([])` uncached. It
  expects exit 1, a stderr carrying `KeyError` and `ao_bad`, and no stdout line carrying
  `live spec(s) ·`. Observed by AC2.
- **S3** — `FLOOR_ASSERTIONS` rises from 282 to 284, with a RAISED comment line above it. Observed
  by AC3.

## 3. Non-goals (OUT)

- No change to `tools/check-spec-tokens.py` or any other product file. This unit adds arms only.
- No arm for the other shapes S4 of TOOL-aPiecewiseGrade-5 turns away, which are a renamed key and
  an added key. Also no arm for S3's added-key case. Both brief items name one dropped key per guard.
- No edit to `tools/unattended/` or its suite, which TOOL-aPiecewiseGrade-7 writes.
- No edit to any CLOSED spec, including TOOL-aPiecewiseGrade-5's AC3 and AC4, which stay as written.
- No `The suite arm labels` bullet. The arm-labels join grades one at every status but WONTDO
  (`tools/check-spec-tokens.py#scan_arm_labels`), so this spec would red until it is built.
- No new fixture, helper or checker copy. Both arms run over the PG1 fixture as it stands.

## 4. Design

### What the code does today

Read at `3300b594c`. The header's base `aebbb4a72` is the build's base on the default branch, and it
predates both guards, which TOOL-aPiecewiseGrade-5 built on this branch. The checker's blob is
`7ecdf1aa` and the suite's `ef969642`.

- **S4, the cache miss.** `read_spec_cache` returns None when an entry's `counts` key set is not
  `SPEC_COUNTERS`. This is a two-line guard, `tools/check-spec-tokens.py@7ecdf1aa:2066` and
  `tools/check-spec-tokens.py@7ecdf1aa:2067`, and it runs before the entry is copied into the next
  generation. The entry's `key` hashes the context and the `.inputs` replay and never covers `counts`
  (`tools/check-spec-tokens.py@7ecdf1aa:2062`). An edited `counts` under a valid key therefore reaches
  the guard.
- **S3, the raise.** `main` seeds `totals = dict.fromkeys(SPEC_COUNTERS, 0)`
  (`tools/check-spec-tokens.py@7ecdf1aa:2433`). For every spec, fresh or cached, it raises `KeyError`
  naming the symmetric difference when `got[2].keys() != totals.keys()`
  (`tools/check-spec-tokens.py@7ecdf1aa:2448` and `tools/check-spec-tokens.py@7ecdf1aa:2449`). On the
  plain path `got` comes from `scan_live_spec`, which `main` looks up as a module global
  (`tools/check-spec-tokens.py@7ecdf1aa:2444`).
- The first stdout line carrying `live spec(s) ·` is the summary at
  `tools/check-spec-tokens.py@7ecdf1aa:2559`, printed after the loop. The entry point has no
  exception handler (`tools/check-spec-tokens.py@7ecdf1aa:2675` to
  `tools/check-spec-tokens.py@7ecdf1aa:2678`), so the raise exits 1 with a traceback and no summary.
- The PG1 fixture is `$pd`, with its checker copy at `$pd/${PFX}check-spec-tokens.py`. Its cache is
  `$pc`, and its output directory `$po` (`tools/check-spec-tokens.test.sh@ef969642:2384`). The suite
  already has `run_grade_checker`, `check_grade_same` and `check_input_arm`
  (`tools/check-spec-tokens.test.sh@ef969642:2416`, `tools/check-spec-tokens.test.sh@ef969642:2420`,
  `tools/check-spec-tokens.test.sh@ef969642:2352`). `$pg_ida` is `$pg_a`'s entry id
  (`tools/check-spec-tokens.test.sh@ef969642:2455`).
- At the PG4 block's end, `$pc` holds the generation from PG1 AC7's warm run, with one entry pair per
  live spec. PG4 AC1 asserts that every entry is copied as a hit
  (`tools/check-spec-tokens.test.sh@ef969642:2514`), so `$pg_a`'s entry is a hit there.
- PG1 AC5 already loads the fixture's checker copy through `importlib` and calls `cst.main([])` with
  a patched module global (`tools/check-spec-tokens.test.sh@ef969642:2458`). S2 uses the same shape.
- No suite arm edits a cached entry's `counts` or patches `scan_live_spec`. A grep at `3300b594c`
  for `scan_live_spec`, `SPEC_COUNTERS` and a `["counts"]` subscript over the suite finds no line.

### Where the arms sit

Both arms go after the PG4 block and above the `TOOL-dGroundRules-32 S9` comment
(`tools/check-spec-tokens.test.sh@ef969642:2528`). That comment requires the overlap arm to stay last
before `total=`. Each arm is one `check_input_arm` call at top level. Paths use `${PFX}`, so the
foreign-prefix leg's three prefixes run them unchanged.

### S1 — the cached short-set arm

```bash
cp -r "$pc" "$base/pgcache/drop"
"$PY" -c 'import json, sys
p = sys.argv[1]; e = json.load(open(p, encoding="utf-8")); del e["counts"]["ao_bad"]
json.dump(e, open(p, "w", encoding="utf-8"))' "$base/pgcache/drop/$pg_ida.json"
pg_nx=$(mktemp -d "$pc.XXXXXXXX")
run_grade_checker kdplain
run_grade_checker kdrop SPEC_TOKENS_CACHE="$base/pgcache/drop" SPEC_TOKENS_CACHE_NEXT="$pg_nx"
pg_list=$(tr -d '\r' < "$pg_nx/graded.list")
[[ $'\n'$pg_list$'\n' == *$'\n'$pg_a$'\n'* ]] && check_grade_same kdplain kdrop
check_input_arm "PG8 AC1 a cached entry whose counts lack ao_bad is a miss, and the run prints the plain run's bytes" $?
```

With S4 deleted, the 23-key set reaches S3, which raises. The cached run then exits 1 with no
summary line, and `$pg_a` never reaches `graded.list`. With S3 also deleted, `$pg_a` still never
reaches `graded.list`, so the membership test reds the arm even where the short sum prints the same
bytes.

### S2 — the fresh short-set arm

```bash
(cd "$pd" && env -u SPEC_TOKENS_CACHE -u SPEC_TOKENS_CACHE_NEXT -u SPEC_TOKENS_INPUTS "$PY" -c 'import importlib.util, sys
sys.stdout.reconfigure(encoding="utf-8")
s = importlib.util.spec_from_file_location("cst", sys.argv[1])
cst = importlib.util.module_from_spec(s); s.loader.exec_module(cst)
real = cst.scan_live_spec
def drop(*a):
    hits, near, counts = real(*a)
    return hits, near, {k: v for k, v in counts.items() if k != "ao_bad"}
cst.scan_live_spec = drop
sys.exit(cst.main([]))' "${PFX}check-spec-tokens.py") >"$po/fresh.out" 2>"$po/fresh.err"
[ $? = 1 ] && grep -q KeyError "$po/fresh.err" && grep -q ao_bad "$po/fresh.err" && ! grep -q 'live spec(s) ·' "$po/fresh.out"
check_input_arm "PG8 AC2 a fresh counts set lacking ao_bad raises KeyError naming it, with no summary line" $?
```

The `reconfigure` call mirrors the entry point's, so the summary's `·` prints when the guard is gone,
rather than failing to encode on a non-UTF-8 console. The cache variables are unset so that the plain
path, where the wrapper sits, grades every spec. With S3 deleted, `totals` still holds `ao_bad` at 0
from its seed, so the run sums short, prints its summary and exits normally. That reds the arm.

### The staged breaks, and a correction to the review's fix

At the close the main loop deletes each guard WHOLE: both lines 2066 and 2067 for S4, and both lines
2448 and 2449 for S3. The review stages S4's RED by deleting line 2066 alone. That leaves
`return None` at the same indent as the line above it, so every cached read misses, S1 stays green,
and PG1's rerun step reds instead. A deleted `if` alone at 2448 likewise makes the raise run
unconditionally.

### The floor

The comment above `FLOOR_ASSERTIONS` gains `# RAISED 282 -> 284 by TOOL-aPiecewiseGrade-8: its two
counter key-set arms after the PG4 block, each top-level. Counted by reading; OWED: observed at the
close.`, and the value becomes 284.

### What the arms do not check

- **A renamed or an added key.** S1 drops one key from a cached set, and S2 drops one from a fresh
  set. Both guards compare whole key sets, so one dropped key reaches the same comparison. A guard
  rewritten to test only for missing keys would still pass both arms.
- **The message's whole text.** S2 reads `KeyError` and the counter's name, not the spec path or the
  sentence around them.
- **Any other spec of the fixture.** S1 edits `$pg_a`'s entry alone.

### Rollout

The suite gains three checker runs over the two-spec PG1 fixture. A one-spec fixture ran in 0.26 s,
and the AC probe's four-variant run took 3.4 s (PINNED `3300b594c`, this node, 2026-11-16).

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

## 5. Acceptance criteria

One run of `bash "$SCRATCH/pg8.sh"` serves the first two criteria, and the pass removes it after. It builds
the `scratch` fixture's one-spec repo with the checker and `tools/memory-tree` copied into the
fixture's tool root. Beside the checker copy it writes two mutants: `nos4`, with S4's two lines
deleted, and `nos3`, with S3's two lines deleted. It runs S1's steps with the copy and with `nos4`,
each against its own cold-then-promoted cache, and S2's driver with the copy and with `nos3`. The
probe writes each guard's observation with the guard present and with it gone, independent of the
suite. The main loop observes the arms themselves RED and then GREEN, under §6's `New arm:` lines.

- **AC1** — When `bash "$SCRATCH/pg8.sh"` runs, it prints `drop guard miss 1 same 1` and
  `drop noguard miss 0 same 0`.
  Red when: S1's edit leaves the entry missing for another reason, such as a key or a parse failure.
  The `nos4` line then reads `miss 1 same 1`, and the arm could never red.
  figure: PINNED, observed by this writer at `3300b594c` on 2026-11-16 over the one-spec fixture.
- **AC2** — When `bash "$SCRATCH/pg8.sh"` runs, it prints `fresh guard rc 1 loud 1 summary 0` and
  `fresh noguard rc 0 loud 0 summary 1`.
  Red when: the wrapper misses `main`'s lookup of `scan_live_spec`. Both lines then read
  `rc 0 loud 0 summary 1`.
  figure: PINNED, as AC1.
- **AC3** — When `grep -c 'PG8 AC[12] ' tools/check-spec-tokens.test.sh` runs it prints 2, and
  `grep -c '^FLOOR_ASSERTIONS=284$' tools/check-spec-tokens.test.sh` prints 1.
  Red when: an arm is missing, or the floor is not moved by the two arms added.

## 6. Gates

`spec-tokens self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

The only path touched trips nothing but the broad `tools/` guard. This was measured with
`python tools/check-spec-tokens.py --legs-for` over it at `3300b594c`. The legs above are the ones
that read this change.

New arm: tools/check-spec-tokens.test.sh · covers AC1 · the cached short-set arm after the PG4 block; staged RED by deleting S4's two lines in the checker · FLOOR_ASSERTIONS 282 to 284, with the arm below
New arm: tools/check-spec-tokens.test.sh · covers AC2 · the fresh short-set arm after it; staged RED by deleting S3's two lines in the checker · the same move as the arm above

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate except
the spec-token checker's `--spec` over this file.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-16 · initial draft from the brief `2026-11-16-prompt-TOOL-aPiecewiseGrade-8-1-spec-writer`,
  the owner's "Promote, build now" for item 2 of `2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2`,
  grounded at `3300b594c`.

## 9. Reuse audit

The seams this unit extends are the suite's own: the PG1 fixture and its warm cache, `run_grade_checker`,
`check_grade_same` and `check_input_arm`, plus PG1 AC5's `importlib` driver shape for S2.
`python tools/codebase-map/reuse_lookup.py` ranked the generic `arm` helper first, a SEAM shared by
eleven suites. It ranked `miss` second, and those `miss` hits are other suites' helpers. Nothing closer
than the PG1 block fits, and no new helper is minted.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "a suite arm that tampers a cached entry or wraps a function through importlib and observes a miss or a loud failure"`
