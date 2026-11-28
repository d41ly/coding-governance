# TOOL-aIndexedAnchor-2 — another build's backlog row and README are records, not a build commit

**Status:** INPROGRESS · rev-1 · 2026-11-28 · node a · Tier-2 · base 9dcc07a9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-28-prompt-TOOL-aIndexedAnchor-2-1-spec-writer.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-1-spec-writer.md) | log | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-2-brief.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`build_commit` stops taking a unit's spec commit for its build commit when the only paths that commit
touches outside its own build folder and the declared record surface are another build's `BACKLOG.md`
or `README.md`. That case is why `pass-order history` reds aIndexedAnchor's landing on 1b161ee30, a
conforming spec commit, and this fix is how the branch re-lands without a waiver.

## 2. Scope (IN)

- **S1** — `tools/unattended/lib-unattended.sh#build_commit` excludes every build's `BACKLOG.md` and
  `README.md` directly under the builds root, which it derives from the build folder it is handed.
  The block comment above the function gains one paragraph naming that surface and the ask door
  that writes it. Every caller reads the change through the one predicate. Observed by AC1, AC2
  and AC3.
- **S2** — The exclusion line `tools/unattended/check-pass-order.sh` prints, and its twin in
  `tools/unattended/check-brief-recorded.sh`, name the new surface. Observed by AC4.
- **S3** — An arm in `tools/unattended/check-pass-order.test.sh` with two halves. Its spec half is
  a spec commit that also writes another build's backlog row and README, followed by a product
  commit, and it grades conforming. Its product half is a commit naming the unit that touches
  another build's `BACKLOG.md` and a product file, and that commit is still the build commit.
  Observed by AC2, AC3 and AC4.

## 3. Non-goals (OUT)

- Any `.unattended.conf` key, `SHARED_RECORDS` and `GENERATED_INDEXES` among them.
- `memory/project/pass-order-waiver.txt`, which gains no row.
- The ask door `gov_record.py new build-readme`, whose refusal of an ask filed in the new build's
  own `BACKLOG.md` is why the case arises.
- Any file of TOOL-aIndexedAnchor-1, and history, which is never rewritten.
- A wider exclusion, such as every path under the builds root. The brief names the two files, and
  a sibling build's `spec/` or `build/` write is not the case observed.
- The re-land itself, which is the lander's run after this unit closes.

### Edges

- **hands-off** external — the re-land of aIndexedAnchor's branch through `bash tools/push-main.sh`,
  whose `pass-order history` red this unit clears.

## 4. Design

### The failing case

1b161ee30, `spec(aIndexedAnchor): TOOL-aIndexedAnchor-1 — ...`, touches ten paths. Eight sit in
`memory/builds/aIndexedAnchor/`, in a `GENERATED_INDEXES` index (`memory/LIVE.md`, `memory/backlog`,
`memory/ledger`) or in `SHARED_RECORDS` (`memory/project/readme-contract.txt`). The other two are
`memory/builds/dTotalRecall/BACKLOG.md` and `memory/builds/dTotalRecall/README.md`. Probed
2026-11-28: `resolve_generated_indexes` over this repo's `.unattended.conf` answers the index set
above, and `build_commit 229f1ddef..7a7566928 TOOL-aIndexedAnchor-1 memory/builds/aIndexedAnchor`
with that set answers 1b161ee30. So `check-pass-order.sh` grades 1b161ee30's parent, which holds
no spec.

### The change

The selection is the `grep -qv` in `tools/unattended/lib-unattended.sh#build_commit`. It reads one
commit's paths and answers true when any path falls outside `-e "^$_bc_dir/"` and the `$_bc_ex`
list. The builds root is `${_bc_dir%/*}`, set once as `_bc_root` beside `_bc_ex=""`. Two quoted
patterns join the grep beside the build-folder pattern:

```bash
    if GIT show --pretty=format: --name-only "$_bc_c" 2>/dev/null \
       | grep -v '^$' | grep -qv -e "^$_bc_dir/" -e "^$_bc_root/[^/]*/BACKLOG\.md\$" \
           -e "^$_bc_root/[^/]*/README\.md\$" $_bc_ex; then
```

The patterns are quoted on the grep line and not appended to `$_bc_ex`. That list expands unquoted,
so its words are pathname-expanded, and `[^/]*` is a glob that a `nullglob` caller would delete. The
`[^/]*` segment also matches the graded build's own folder, which `^$_bc_dir/` already excludes. A
nested record such as `<root>/<slug>/sub/README.md` is not matched. `_bc_root` carries the
`MEMORY_ROOT` bytes into a regex exactly as `^$_bc_dir/` already does, so this adds no new instance
of the conf-value-in-a-regex class.

Probed 2026-11-28 on a scratch copy of the library carrying those two patterns, with the real index
set: the same `build_commit` call answers 398ba9252, the unit's product commit.

### The three callers

| Caller | Call site | What changes |
|---|---|---|
| `pass-order history` | `tools/unattended/check-pass-order.sh@fbd503a7:830` and `:849` | the in-range and pre-anchor walks skip such a commit |
| `brief-recorded` | `tools/unattended/check-brief-recorded.sh@1c1e9e4f:760`, `:789` and `:839` | the same three walks skip it |
| the driver's term 4 | `tools/unattended/unattended.sh@c634eb54:16623` | a commit touching only such records is no longer any unit's build commit |

No caller changes its call. The brief names two callers. The driver's term 4 is a third, and it reads
the same predicate whether or not this unit names it.

### The exclusion lines

`tools/unattended/check-pass-order.sh@fbd503a7:1036` and `tools/unattended/check-brief-recorded.sh@1c1e9e4f:1022`
each print `the record surface excluded from build-commit selection was: <build folder> ` and then the
conf paths. The comment above the first says the line is the trace that makes a widened surface
visible, so a line that leaves out part of the surface fails at that job. Both lines gain the same
words after `<build folder>`:

```
<build folder> <every build's BACKLOG.md and README.md> <conf paths...>
```

The phrase is prose, as `<build folder>` already is, and not a second spelling of the regex.

### The arm

The arm sits before the suite's closing `echo "--- $n arms, exit $st"`. It is one inline
`for half in spec product` loop with no new function, as the store arm above it is written. Each
pass builds a `mktemp -d` repository. It copies `lib-unattended.sh`, `unattended.sh`,
`check-pass-order.sh` and `commit_trailers.py` into `${PFX}${KIT_NAME}/` and writes the conf
`MEMORY_ROOT=memory`, `PASS_ORDER_CUTOFF="2026-01-01"` and
`SHARED_RECORDS="memory/DECISIONS.md memory/backlog"`. The base commit carries a sibling build
`memory/builds/tP/` with a `README.md` opened 2025-06-01, so the cutoff skips it, and a `BACKLOG.md`.

| Half | Commits after the base | Expected |
|---|---|---|
| `spec` | `spec ARCH-tS-1 authored` writes the `tS` README carrying one CLOSED `ARCH-tS-1` row, `tS/spec/s1.md`, one row appended to `tP/BACKLOG.md` and one line appended to `tP/README.md`; then `ARCH-tS-1: build the thing` writes a product file | rc 0, `graded 1 closed unit`, no `FAILED`, and the exclusion line's new phrase |
| `product` | `records(tS): open the build` writes the `tS` README; `ARCH-tS-1: build the thing` writes a product file and appends one row to `tP/BACKLOG.md`; `spec ARCH-tS-1 written afterwards` writes the spec | rc 1, naming `ARCH-tS-1 — BUILT at <short sha of the build-the-thing commit>` |

The spec text is the store arm's `q1.md` shape with the id swapped. The spec half also asserts the
exclusion line carries `<build folder> <every build's BACKLOG.md and README.md>`.

Prototyped 2026-11-28 in the scratchpad against both libraries. With the shipped library, the spec
half exited 1 naming its spec commit and the product half exited 1 naming its build commit. With the
two patterns added, the spec half exited 0 and the product half still exited 1 naming its build
commit.

### Alternatives rejected

- A glob in `SHARED_RECORDS`: a non-goal, and a conf value with a backslash turns off the history
  store at `tools/unattended/check-pass-order.sh@fbd503a7:557`.
- Appending the patterns to `$_bc_ex`: its unquoted expansion globs `[^/]*`.
- One shared helper printing the exclusion phrase for both legs: the two lines are already literal
  twins, and a helper for one phrase is a layer no other caller uses.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-pass-order.test.sh`

## 5. Production-readiness checklist

- security — N/A: the patterns are code, not conf, and the grep reads git's own path list.
- perf / scale — the grep gains two patterns per commit already walked, and no new process. The
  suite gains two fixtures and two leg runs. Its row in `tools/run-gates/selftest-budgets.txt`
  allows 170 s against 111 s measured on 2026-09-07 (PINNED, from that row), so the close re-reads
  the suite's wall time against it.
- error / empty / loading states — a `_bc_dir` with no `/` makes `_bc_root` the folder itself, and
  the patterns then match nothing a caller passes. Every caller passes `<memory root>/builds/<slug>`.
- observability — S2: both exclusion lines name the new surface.
- risks — the driver's term 4 now reads a commit that touches only such records as no unit's build
  commit, so an ask recorded CLOSED by such a commit refuses at that term. That is the term's stated
  rule, that a CLOSED ask carries a unit's evidence. A suite fixture whose unit commit touches only
  its own folder and a sibling's README would change verdict, and the close's suites would show it.
- testing — S3's arm, both halves, seen red and then green at the close.
- migration — N/A: no data moves. Both legs key their history store on the library's bytes
  (`tools/unattended/check-pass-order.sh@fbd503a7:549`, `tools/unattended/check-brief-recorded.sh@1c1e9e4f:487`),
  so stored verdicts regrade once.
- user docs — N/A: no `help/` page names the build-commit record surface. A grep of `help/` for
  `pass-order` and `SHARED_RECORDS` finds only the `hooks.bypass` row of `help/reference/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `bash -c '. tools/lib/resolve-python.sh && . tools/unattended/lib-unattended.sh && G=$(resolve_generated_indexes "$PWD" "$(read_conf_value .unattended.conf GENERATED_INDEXES)" memory); S=$(read_conf_value .unattended.conf SHARED_RECORDS); build_commit 229f1ddef..7a7566928 TOOL-aIndexedAnchor-1 memory/builds/aIndexedAnchor "$G" "$S"'`
  runs at the repo root, it prints `398ba9252b2f1317024e200856c72cc7764a435a`.
  Red when: the two patterns are absent, so it prints `1b161ee303d48721bf2ac7df2e224c885972b8a1`,
  the spec commit.
  cost: about 20 s on node a, measured 2026-11-28 (PINNED).
  figure: both shas PINNED; the commits are in pushed history, which is never rewritten.
- **AC2** — When `bash tools/unattended/check-pass-order.sh` runs inside the arm's spec-half fixture,
  it exits 0, prints `graded 1 closed unit` and prints no `FAILED`.
  Red when: the sibling patterns are absent, so the leg exits 1 naming `ARCH-tS-1 — BUILT at` the
  spec commit.
  fixture: the arm builds it under `mktemp -d`; the tree holds none.
- **AC3** — When `bash tools/unattended/check-pass-order.sh` runs inside the arm's product-half
  fixture, it exits 1 and names `ARCH-tS-1 — BUILT at` the short sha of the commit subjected
  `ARCH-tS-1: build the thing`, with the patterns present and with them absent.
  Red when: the exclusion skips a whole commit that touches a sibling record, or matches the product
  path, so the leg exits 0 counting `1 unit(s) unbuilt-in-range`.
  fixture: as AC2.
- **AC4** — When the AC2 run's output is read, its exclusion line carries
  `<build folder> <every build's BACKLOG.md and README.md>`, and
  `grep -c "<build folder> <every build's BACKLOG.md and README.md>" tools/unattended/check-brief-recorded.sh`
  prints 1.
  Red when: either line still prints `<build folder>` followed directly by the conf paths.

## 7. Gates

`pass-order history` · `brief-recorded` · `unattended kit gate` · `routed-commits selftest`

The kit's self-test suites `unattended pass-order selftest` and `unattended brief-recorded selftest`,
named in `tools/run-gates/selftest-budgets.txt`, run at the close. The second reads `build_commit`
through the brief-recorded leg.

New arm: `tools/unattended/check-pass-order.test.sh` · covers AC2 AC3 AC4 · deleting the two sibling patterns from the grep in `build_commit` reds the spec half while the product half stays green · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-28 · initial draft.

## 10. Reuse audit

The seam is `tools/unattended/lib-unattended.sh#build_commit`, the one build-commit predicate that
`reuse_lookup.py` ranks as a SEAM at fan-in 7. Its grep already carries the build-folder pattern
and the `$_bc_ex` list, and the two new patterns join that same grep. No caller gains its own copy.

Recall terms used: `reuse_lookup.py "build commit selection exclusion record surface sibling build BACKLOG README spec commit pass-order SHARED_RECORDS"`
