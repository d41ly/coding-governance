# TOOL-dDeclaredLoop-37 — the trailer re-points observed at their call sites, red at base

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-37-deviation-371.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-37-deviation-371.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 8 at HIGH**, its item **H8**, alone in that item; the skeptic judged the
finder's fix unsound and wrote the corrected one this unit takes. `TOOL-dDeclaredLoop-23` S5 says its
re-points are observed by AC2 to AC4, but each of those compares a consumer's output at base
`ed497191` with the working tree, which are identical before the build, so all three are green on a
build that ships the reader and leaves every consumer on its own parser. The same gap sits in
`TOOL-dDeclaredLoop-12` AC4 for `order_by_needs` and `find_cycles`. This unit adds the criteria that
are red at base and green only once each consumer reads through the one reader, and makes any
consumer `TOOL-dDeclaredLoop-23` left on its own parser read through it. It repairs
`TOOL-dDeclaredLoop-23`.

## 2. Scope (IN)

- **S1** — The product-wide probe: `git grep -n -e 'trailers:key=Pass,' -e 'interpret-trailers --parse'
  -- tools ':!*.test.sh'` lists only `tools/lib/commit_trailers.py` and
  the files carrying its `commit_trailers_py` block. At base it lists `tools/memory-tree/routed_commits.py`
  (:231, :371), `tools/unattended/check-unattended.sh` (:4219), `tools/unattended/lib-unattended.sh`
  (:1064, :1150) and `tools/unattended/unattended.sh` (:13491). The patterns carry the format's comma
  so a comment naming `%(trailers:key=Pass)` (`tools/unattended/unattended.sh:13488`) is not read.
  Observed by AC1.
- **S2** — The per-consumer call sites, one grep each over the consumer's code lines, every one red at
  base: `read_routed_commits` and `read_newest_unit` in `tools/memory-tree/routed_commits.py` call
  `read_commits` and `attribute`; `read_first_passes` in `tools/memory-tree/deviation_join.py` calls
  `attribute` with the `replace` view; `read_attribution_tokens` and the `pass_commit` walk in
  `tools/unattended/lib-unattended.sh` and the subset test in `tools/unattended/check-unattended.sh`
  run `commit_trailers.py tokens`; `check_commit_message` in `tools/unattended/unattended.sh` runs
  `commit_trailers.py message`. Observed by AC2.
- **S3** — A consumer either probe still finds on its own parser after `TOOL-dDeclaredLoop-23` is
  re-pointed here, through the view `TOOL-dDeclaredLoop-23` §4 "The consumers" names for it. Observed
  by AC1, AC2.
- **S4** — The second half of the finding, handed to its owner: `TOOL-dDeclaredLoop-12`'s pass runs
  the call-site greps that `derive_install_order` in `tools/govkit/govkit.py` calls `order_by_needs`
  and that `tools/memory-tree/backlog.py`'s one cycle scan calls `find_cycles`, each red at base,
  through the hands-off below. NOT OBSERVED here: that unit builds at order 6, after this one.

## 3. Non-goals (OUT)

- The reader itself, its views and its copies: `TOOL-dDeclaredLoop-23`'s.
- The suites that read `Pass:` to assert a fixture (`tools/push-main.test.sh`,
  `tools/workflows/unattended-build.test.sh`): `TOOL-dDeclaredLoop-23` §3 says a suite reading a
  fixture's trailer is not a reader of record, so S1 excludes `*.test.sh`.
- A spec lint over re-point items, the finding's left-shift: S1 is the class gate for trailer readers,
  and a general lint over every spec's criteria is not named by any clause of this build.
- The runlog consumer, `read_git_range`, whose `Decided` read `read_commits` cannot serve as specced:
  the audit's id 20, batched into `TOOL-dDeclaredLoop-56`, which owns that re-point and its probe.
- The line-ending, pin and missing-table defects of the same reader: ids 18, 19 and 47, units
  `TOOL-dDeclaredLoop-38`, `-39` and `-40`.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py`, `read_commits` and `attribute`, the reader every probe here asks each consumer to call
- **hands-off** `TOOL-dDeclaredLoop-12` — the call-site greps for `order_by_needs` in `derive_install_order` and for `find_cycles` in the backlog cycle scan, which that unit's pass runs as the observation of its re-point

## 4. Design

### Why grep, and why red at base

A re-point's observable is that the old parser is gone and the new call is present. Both are
properties of the source, so a grep over code lines is the direct observation, and its liveness is
that it lists five files at base. A behavioural equality cannot be that observation: it is satisfied
by the consumer that never changed.

### The probes

```bash
# S1, the class: no product file spells its own trailer parse
git grep -n -e 'trailers:key=Pass,' -e 'interpret-trailers --parse' \
  -- tools ':!*.test.sh' | grep -v -e 'commit_trailers' -e '>>> commit_trailers_py'
# S2, one per consumer, each printing at least one line
git grep -n -e 'read_commits(' -e 'attribute(' -- tools/memory-tree/routed_commits.py
git grep -n 'attribute(.*replace' -- tools/memory-tree/deviation_join.py
git grep -n 'commit_trailers.py.* tokens' -- tools/unattended/lib-unattended.sh tools/unattended/check-unattended.sh
git grep -n 'commit_trailers.py.* message' -- tools/unattended/unattended.sh
```

A file that carries the `commit_trailers_py` block is excluded from S1 by the marker, which is the
population the `commit_trailers_py` parity row already reads.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.sh`

Each is touched only where S3 finds a consumer still on its own parser; on a correct build of
`TOOL-dDeclaredLoop-23` the pass changes none of them and records the probes.

### Alternatives rejected

- **The finder's fix, a grep over the whole of `tools/`.** The skeptic judged it unsound: the suites
  plant `Pass:` trailers to assert fixtures and would red it forever.
- **A behavioural before-and-after compare with a staged consumer.** It still passes on an untouched
  consumer, which is the defect.

## 5. Production-readiness checklist

- security — no new surface; read-only greps.
- perf / scale — six greps, under a second.
- error / empty / loading states — each S2 probe printing nothing is the red, and S1 printing a
  product line is the red.
- observability — each probe names the file and line it found.
- risks — a consumer renamed during the build moves its call site; S2 names functions, and a renamed
  function is a miss the builder sees as an empty probe, never a silent pass.
- testing — AC1 and AC2 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none: no page under `help/` describes trailer readers.

## 6. Acceptance criteria

- **AC1** — When the S1 probe runs on the built tree, it prints no line; at base `ed497191` it prints
  six lines across `tools/memory-tree/routed_commits.py`, `tools/unattended/check-unattended.sh`,
  `tools/unattended/lib-unattended.sh` and `tools/unattended/unattended.sh`.
  Red when: a consumer keeps its own `%(trailers:key=Pass,…)` format, so its line is printed.
  figure: the six lines and four files are PINNED, measured 2026-10-24 at base.
- **AC2** — When each S2 probe runs on the built tree, each prints at least one line naming its
  function's call into `commit_trailers`; at base each prints none.
  Red when: `read_first_passes` keeps its `re.sub` over `c["trailer"]`, so its probe is empty.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `runlog selftest` · `unattended kit gate` · `pass-order history` · `brief-recorded` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 · the S1 probe as a selftest arm over the tree, staged by planting a `%(trailers:key=Pass,valueonly)` format in a scratch copy of a consumer · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Does this unit own `TOOL-dDeclaredLoop-12`'s half of the finding?** Options: (a) observe it
  here; (b) hand it to that unit's pass. (a) cannot run: this unit builds at order 4 and the re-point
  lands at order 6, so the probe would be red at this pass for a reason outside it. RESOLVED (agent,
  2026-10-24, delegated): (b), rung 3, through the hands-off in §3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 8 (HIGH, item H8).

## 10. Reuse audit

The seam is the `commit_trailers_py` parity row's marker, which already names the population of
copies S1 excludes; the probes extend no code and add one selftest arm to `routed_commits.py`, the
consumer whose selftest already re-runs `TOOL-dDeclaredLoop-23` AC2. No existing seam fits a call-site
observation of a re-point: `python tools/codebase-map/reuse_lookup.py "a re-point observed by a
call-site grep of each consumer"` ranked regex builders (`build_spec_path_re`, `build_unit_id_re`,
`build_id_token_re`), none of which observes a call site.

Recall terms used: re-point call site trailer Pass interpret-trailers commit_trailers read_commits attribute base equality
