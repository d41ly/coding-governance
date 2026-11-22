# TOOL-dQuietDisk-10 — `check-wiring.test.sh` builds its wired copies from one captured config, with no per-copy git

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base 7b8c737b · streams tooling · order 3 · ratified 2026-11-22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 |
| [2026-11-22-build-TOOL-dQuietDisk-10-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-10-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-10-widen-9.md](../build/2026-11-22-build-TOOL-dQuietDisk-10-widen-9.md) | widen | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-10-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-10-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-10-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-10-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md) | research | TOOL-dQuietDisk-6 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-18 |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-wiring.test.sh` builds its seed repository once per run and copies it per arm. It
still spends one `git config` process on every copy that wants its hooks wired. This unit captures
the wired config once per run and writes it into each wired copy with a builtin, so no copy spawns
git. That saves the git processes the suite spends today on wiring. The arms stay the same, with
the same RED and GREEN results: 255 arms, PINNED by the analysis's measured run at gov `608aa364c`.

This goal is restated by the run's ruling of F2 and F3 on 2026-11-22, not by this spec's writer.
It replaces the earlier goal, which took both base repositories from TOOL-dQuietDisk-7's template
cache.

### The saving, re-grounded at 7b8c737b0

On the cache as built, the earlier goal's move spends more than the suite spends today, so its
saving is none. Sections 2 to 7 follow F2's ruling.

- **Today:** the seed build costs 4 git processes per run, and each of the 33 wired calls one more,
  37 in all.
  figure: DERIVED from `tools/check-wiring.test.sh@8d0af8c91b34`, every guarded block taken, as a
  gov checkout takes them, plus the probe's 4 for the seed.
- **On the cache as built:** the two templates cost 21 git processes per run. That saves 16 but
  adds at least 35 temp entries at peak. The order-3 re-ground task moves a suite onto the cache
  only where both counts fall.
  figure: PINNED, measured 2026-11-22.
- **Under F2's ruling:** the suite keeps its own seed and spends 5 git processes per run.
  That saves 32, and the temp entries stay as they are.
  figure: DERIVED from the same count, and the 5 is PINNED by the same probe.

## 2. Scope (IN)

- **S1** — After today's seed block (`tools/check-wiring.test.sh@8d0af8c91b34:45-49`), the suite
  captures the wired config once. It reads the seed's `.git/config` into a shell variable with
  `IFS= read -r -d ''` and runs `git -C "$NEWREPO_SEED" config core.hooksPath .githooks`. It then
  reads the result into `NEWREPO_WIRED_CONFIG` the same way, and writes the first bytes back to the
  seed with `printf '%s'`. This costs one git process per run. Observed by AC1 and AC2.
- **S2** — `newrepo` takes an optional word `wired`. It copies the seed exactly as today
  (`tools/check-wiring.test.sh@8d0af8c91b34:50-52`). With `wired`, it also writes
  `NEWREPO_WIRED_CONFIG` over the copy's `.git/config` with `printf '%s'`, a builtin, so neither
  form spawns git. Observed by AC1 and AC2.
- **S3** — The ten sites that spell `newrepo; git config core.hooksPath .githooks` call
  `newrepo wired` instead:
  - at blob `8d0af8c91b34`, lines 404, 1343, 1348, 1841, 1935, 1958, 2013, 2220, 2306 and 2366;
  - everything after that pair on each line stays as it is.

  The site at line 398, which spells the hooks directory with a leading dot-slash, keeps its own
  `git config`. So do the two that write an out-of-tree path, at lines 388 and 2290. Observed by AC3.
- **S4** — A capture that fails exits 2 before any arm runs, as a failed seed build does today
  (`tools/check-wiring.test.sh@8d0af8c91b34:49`). The `git config` may exit non-zero, or the
  captured bytes may equal the plain ones. Observed by AC4.
- **S5** — The suite adds no inline block and sources no file under gov's lib directory, so a
  copy-installed suite runs as it does today. Observed by AC5.
- **S6** — The arm set and every arm's verdict are unchanged. Observed by AC6.
- **S7** — The saving is counted: git processes, and peak and residual temp entries, before and
  after. Observed by AC7.

## 3. Non-goals (OUT)

- `tools/check-wiring.sh` itself. Of the 3,786 git processes the analysis measured in one run, 1,679
  are `ls-files` (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
  its representative-runs section). Those come from the checker re-listing the tree on each
  invocation, not from fixtures. TOOL-dQuietDisk-26 carries that one listing per invocation, at
  order 4, after this unit (F1).
  figure: PINNED, the analysis's measurement at gov `608aa364c`.
- The template cache's functions, under F2's ruling. `resolve_template`,
  `derive_template_key` and `build_template_clone` in `tools/lib/template-cache.sh` are not called,
  and the `template_cache_sh` block is not carried inline. Section 4 says why.
- A policy switch for the wired capture, under F3's ruling.
- A read-only checkout shared by reading arms. The suite's header names an auto-fix mode
  (`tools/check-wiring.test.sh@8d0af8c91b34:2`), so which arms write is a per-arm question. Every
  `newrepo` arm keeps its own copy.
- Fewer entries per copy. A copy holds the seed's 28 entries, its reflog and `COMMIT_EDITMSG`
  among them. Pruning those changes state a later `git commit` in an arm writes back, so it is a
  separate question, and this unit leaves the copy as it is.
  figure: PINNED, measured 2026-11-22.
- The single-use fixtures (lines 410, 1448-1478, 1718 and 2267 at blob `8d0af8c91b34`).
- The owned, swept scratch root for `newrepo`'s `mktemp -d`: TOOL-dQuietDisk-9.
- A kit version bump by hand. The lander's `govkit.py mint` writes every owed bump
  (`tools/push-main.sh@3a5bf825e879:27-30`).
- `memory/gotchas/` records and gate-lint rows for the R1 rule: asks TOOL-dQuietDisk-20 and -23.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the template cache's measured build and clone costs, which F2's ruling weighed against the suite's own seed. Without them the ruling had no measured ground, and the suite would have been moved onto a face that costs it more.
- **hands-off** `TOOL-dQuietDisk-19` — the suite's before and after readings, taken in a scratch `git clone --shared`. Under F3's ruling this unit carries no switch, so its saving shows in B0 against A, not between A-off and A-on.
- **hands-off** `TOOL-dQuietDisk-26` — the checker's per-invocation `ls-files`, `ls-tree` and `check-attr` reads, one each per invocation, and the two arms that pin them, added to the suite this unit changes.

## 4. Design

### The capture and the wired copy

```bash
# after the seed block, before `newrepo` (S1, S4)
IFS= read -r -d '' _nr_plain < "$NEWREPO_SEED/.git/config" || :
git -C "$NEWREPO_SEED" config core.hooksPath .githooks || exit 2
IFS= read -r -d '' NEWREPO_WIRED_CONFIG < "$NEWREPO_SEED/.git/config" || :
printf '%s' "$_nr_plain" > "$NEWREPO_SEED/.git/config" || exit 2
[ -n "$NEWREPO_WIRED_CONFIG" ] && [ "$NEWREPO_WIRED_CONFIG" != "$_nr_plain" ] || exit 2
newrepo() {   # [wired] -> cd (in THIS shell) into a fresh copy of the seed
  D=$(mktemp -d); cp -a "$NEWREPO_SEED/." "$D/" || exit 2; cd "$D" || exit 2
  [ "${1:-}" != wired ] || printf '%s' "$NEWREPO_WIRED_CONFIG" > .git/config || exit 2
}
```

The wired bytes are the ones git itself wrote, so the suite never spells git's config format.
`read -r -d ''` stops at NUL, which a config file never holds, so it takes the whole file,
trailing newline included. It returns non-zero at end of file, which the `|| :` absorbs, and the
final guard catches a read that took nothing. `cleanup` and the existing `trap` are unchanged.

A probe on 2026-11-22 confirmed this form against today's in the session scratchpad. The form ran
on a seed built by today's block, with the suite's environment from
`tools/check-wiring.test.sh@8d0af8c91b34:37-38`, under git 2.54.0.windows.1 on node d:
- a wired copy's `.git/config` is byte-identical (`cmp`) to a seed copy after
  `git config core.hooksPath .githooks`;
- the seed's config after the write-back is byte-identical to its config before the capture;
- the two `newrepo` calls added no trace2 file;
- `bash tools/check-wiring.sh --check` prints `ok       hooks     — core.hooksPath -> .githooks`
  and exits 0 in the wired copy;
- in the plain copy it prints `UNWIRED  hooks` and exits 1. That is why the existing arm
  `AC5 all wired -> exit 0` reds when the wired write is lost.

### What the cache as built costs this suite

These are measured with `GIT_TRACE2_EVENT=<dir>` by counting its files. Measured on 2026-11-22 in
the session scratchpad, under git 2.54.0.windows.1 on node d, PINNED. The builder is today's seed
block, run through `tools/lib/template-cache.sh` as it stands at blob `c9e02755f426`.

| Step | git processes | Entries |
|---|---|---|
| Today's seed build: `init`, `add`, `commit` and the `maintenance run --auto` child `commit` starts | 4 | 28 in the copy |
| `derive_template_key` with no input file: one `hash-object --stdin` | 1 | 0 |
| `resolve_template` building `newrepo`: the builder's 4, then `add -A`, `commit`, `rev-parse`, `diff --cached` and `config --local --list` | 9 | — |
| Both templates, keys included; the wired builder adds one `git config` | 21 | 63 under the root, against the seed's 28 |
| `resolve_template` reusing a built template | 0 | 0 |
| One `cp -a` copy of a template's `repo` | 0 | 28 |
| One `build_template_clone` | 3: `clone`, `git-upload-pack`, `remote remove` | 23 |

The template is built once per cache root, and nothing in the tree exports
`SELFTEST_TEMPLATE_ROOT` (`grep -rn SELFTEST_TEMPLATE_ROOT tools` names only the two faces and
`tools/lib/lib-selftest.test.sh`). The root is therefore the bar's owned `$WORK` or the suite's own
scratch, and this suite, its only user, builds both templates on every run. Unit 7's spec says the
same of the class: a suite whose arms copy with `cp -a` and spawn no git spends more on the cache
(`memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-7.md`, "The consumers").

### The saving

The fixture git processes per run are counted at blob `8d0af8c91b34`, with every guarded block
taken. The wired calls a run makes are these:
- 8 single sites, PINNED, counted at that blob on 2026-11-22;
- 3 calls of `seed_mode_fixture`, PINNED, counted at that blob on 2026-11-22;
- 22 calls of `seed_ssh_fixture`, DERIVED: 9 top-level calls plus 13 from passes of its 6 loops;
- 33 calls in all, DERIVED as the sum of the three lines above.

| Form | Per run | Per wired call | Total | Peak temp change |
|---|---|---|---|---|
| Today | 4 | 1, 33 times | 37 | — |
| F2 (a): the cache's templates, `cp -a` per call | 21 | 0 | 21 | at least +35 |
| The cache's templates, `build_template_clone` per call | 21 | 0 | 21, plus 3 per `newrepo` call | at least +35 |
| F2 (b): the suite's seed plus the captured config | 5 | 0 | 5 | 0 |

Under (b) the suite spends at least 32 fewer git processes per run, DERIVED from this table. That
is about 0.85% of the 3,786 the analysis measured (PINNED there). The checker's listing,
TOOL-dQuietDisk-26's, is the larger share.

### Files touched (estimate)

`tools/check-wiring.test.sh`

No other order-3 unit, 6, 12, 13, 18 or 28, names this path.

### Alternatives rejected

- F2 (a), the cache's templates copied with `cp -a`: 16 more git processes and at least 35 more peak entries
  than (b), on the table above.
- The cache's `build_template_clone` per call: 3 git processes per call, where a copy spends none.
- Appending `\thooksPath = .githooks` to the copy's config. Probed byte-identical, but it holds only
  while `[core]` is the seed config's last section, which the capture never assumes.
- A second seed directory copied from the first, then `git config` on it: the same one git process,
  28 more entries and one more `cp -a`.

## 5. Production-readiness checklist

- security: N/A — no new write path, input or surface; every write lands in the suite's own scratch.
- perf / scale: at least 32 fewer git processes per run, DERIVED in section 4; temp entries unchanged.
- error / empty / loading states: a failed capture exits 2 before any arm (S4).
- observability: none added; the suite's per-arm `ok`/`FAIL` lines are unchanged.
- risks: the capture assumes `git config` writes only `.git/config`. The write-back restores the
  seed byte for byte, and AC2 compares both files.
- testing: AC1 to AC5 are probes of this unit's code; AC6 and AC7 run the suite and are the main loop's.
- migration: N/A — the suite carries no state between runs.
- user docs: N/A — a test-internal change; no `help/` page describes the suite's fixtures.

## 6. Acceptance criteria

- **AC1** — When a probe extracts the seed block, the capture and `newrepo` from the edited suite
  with `awk` and runs them under `GIT_TRACE2_EVENT=<dir>`, the capture adds one
  trace file. Then `newrepo wired` and `newrepo` add none.
  `git -C "$D" config --local core.hooksPath` prints `.githooks` for the wired copy and nothing for
  the plain one.
  Red when: the wired copy carries no `core.hooksPath`, the plain one carries it, or a call spawns git.
- **AC2** — When the same probe compares the copies, a `newrepo wired` copy's `.git/config` is
  `cmp`-identical to a plain copy after `git config core.hooksPath .githooks`. Its `git ls-files -s`,
  `git for-each-ref` and `git config --local --list` read identically too, and the seed's own config
  is `cmp`-identical to its bytes before the capture.
  Red when: the write-back leaves `core.hooksPath` in the seed, or the wired bytes differ from git's.
- **AC3** — When `grep -c 'newrepo; git config core.hooksPath .githooks' tools/check-wiring.test.sh`
  runs after the change, it prints 0. `grep -cE '^ *newrepo wired' tools/check-wiring.test.sh` prints
  10, and `grep -cF 'newrepo; git config core.hooksPath .' tools/check-wiring.test.sh` prints 1, the
  dot-slash site at line 398.
  Red when: a wired site survives beside the capture, or the dot-slash site loses its own config.
  figure: DERIVED from blob `8d0af8c91b34`, where the three greps print 10, 0 and 11 before the change.
- **AC4** — When the probe defines a shell function `git` that fails a `config` call and runs the
  extracted block, the block exits 2 before `newrepo` is defined.
  Red when: a failed capture falls through and the wired arms run on plain copies.
- **AC5** — When `grep -nE '(^|[;&|] *)(\.|source) .*/lib/' tools/check-wiring.test.sh` runs, it
  prints nothing, and `grep -c '>>> template_cache_sh' tools/check-wiring.test.sh` prints 0.
  Red when: the suite sources a file under gov's lib directory, which no adopter holds.
- **AC6** — When the main loop runs `bash tools/lib/extract-arms.sh` over the suite at the build
  base and at the unit's commit, both inventories hold the same 255 labels with the same verdicts,
  and the suite's `PASS` total is the same.
  Red when: an arm is lost, added or changes verdict.
  permission: a role pass may not run a self-test suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two suite runs, about 300 s each [PINNED] (the analysis's representative-runs section).
- **AC7** — When the main loop runs the suite in a scratch `git clone --shared`, before and after,
  with `GIT_TRACE2_EVENT`, `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs, the git process count
  falls by at least 32. Peak temp entries do not rise, and the residual temp entries are 0 both times.
  Red when: the count falls by less, the peak rises, or an entry remains after the run.
  permission: as AC6.
  figure: the bound 32 is DERIVED from section 4's count at blob `8d0af8c91b34`; the measured counts are
  TOOL-dQuietDisk-19's record.
  fixture: the adopter half is a scratch target that `python tools/govkit/govkit.py apply` installs
  the check-wiring kit into, where the main loop runs the shipped suite; `tools/govkit/fixtures/`
  holds no adopter tree with this kit today. `python tools/govkit/govkit.py check --target
  C:/projects/incms/main` and `--target C:/projects/nicocares/main`, run read-only from gov, read
  the same before and after.

## 7. Gates

`check-wiring self-test`

No new arm. The existing `AC5 all wired -> exit 0` arm reds when the wired write is lost, as
section 4's probe shows, and AC6 holds the arm set fixed.

## 8. Open questions

- **F1** — Does this build add a unit for `tools/check-wiring.sh`'s per-invocation re-listing?
  The suite's measured cost is the subject: 1,679 `ls-files` and 421 `check-attr` of 3,786 git
  processes (the analysis's representative-runs section), against at least 7 this unit saved at
  rev-3. The prompt names check-wiring as a biggest target (the prompt record's Fix 2).
  - (a) No unit; the main loop files an ask naming the listing. One follow-up stays open.
  - (b) ADD a unit: one `git ls-files -s` per invocation, read in-process by every check that
    re-lists today, with the checker's findings byte-identical on the suite's 255 arms. It closes the
    follow-up and is a separate mechanism, so it is its own unit
    (`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`).
  - Recommendation: (b). It is the most feature-rich option, and no veto applies: it adds no
    dependency, surface or carrier change, and widens no write surface.
  - RESOLVED (agent, 2026-11-20, delegated): (b). TOOL-dQuietDisk-26 now carries
    `check-wiring.sh`'s one listing at order 4, and this unit stays on the suite's fixtures at
    order 3.
- **F2** — Does the suite take its two base repositories from the template cache as built, or keep
  its own seed? The goal says the cache, but the order-3 re-ground task moves a suite onto the cache
  only where git processes and temp entries both fall. Unit 7's consumers section says a `cp -a`
  suite spends more there.
  - (a) The cache, as the goal reads. `newrepo [wired]` asks `resolve_template` for each template
    once per run and copies it with `cp -a`. The suite carries `template_cache_sh` inline, with a
    parity row in `tools/lib/resolve-python.test.sh`. It already carries `resolve_python` and
    `refuse_wrong_shell` inline and calls `refuse_wrong_shell`, which unit 7's rev-6 requires.
    The cost is 21 git processes per run, a saving of 16, with at least 35 more temp entries at peak.
  - (b) The suite's own seed stays its template, and `newrepo wired` writes the config bytes git
    wrote once (section 4). The cost is 5 git processes per run, a saving of 32, with no entry added
    and no inline block. The goal's "from TOOL-dQuietDisk-7's template cache" clause and the title
    are rewritten to name the seed, and the brief item that reads "on the template cache" is met by
    the saving, not by the mechanism.
  - (c) WONTDO with no saving: the seed is already a once-per-run template. The 32 processes stay
    spent.
  - Recommendation: (b). It saves twice what (a) saves with less code. It is the only option that
    meets the re-ground task's rule, and no veto applies: no dependency, surface or carrier
    changes. It changes this unit's goal wording, which is why it is a fork and not a design choice.
    The sibling records that read "as moved onto the template cache" need one line each: unit 26's
    consumes-from edge and unit 19's A-off and A-on limits line.
  - RESOLVED (agent, 2026-11-22, delegated): (b). It is the only option the measurements show
    saving git processes, 37 to 5 per run, without adding temp entries. The cache as built adds both,
    and the unit 7 ruling moves a suite onto the cache only where it then spends less. The run
    restated this unit's goal and title to match.
- **F3** — Under F2 (b), does the wired capture read a policy switch? The spec brief makes every
  new cache, store or skip switchable. `tests.fixture-templates` exists, but its catalogue row
  (`tools/policy/catalogue.toml`, the `tests.fixture-templates` row) scopes it to a self-test that
  opts into the template cache.
  - (a) No switch. The capture is a per-run memo of bytes git writes in the same run from the same
    seed, held in a shell variable and persisted nowhere. `NEWREPO_SEED` is the same class
    (TOOL-aSparedSpawn-9 S3), and no switch governs it. Unit 19's M1 saving then shows in B0
    against A, as units 9 and 26 do.
  - (b) Read `tests.fixture-templates` once per run through the policy kit. `per-case` runs
    `git config` per wired call, as today. This costs one or two python spawns per run and widens the
    catalogue row's summary, which re-renders `help/reference/policy.md`.
  - Recommendation: (a). Nothing stored can go stale across runs, so there is no stale-answer risk
    for a switch to hold back. Option (b) adds two files to the write set for a memo no reader
    persists.
  - RESOLVED (agent, 2026-11-22, delegated): (a). `tests.fixture-templates` covers only suites that
    opt into the cache, and a switch this unit does not need is scaffolding.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-20 · §3 · §4 · §8 · F1 resolved (b) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`: the listing non-goal and the bound point at
  TOOL-dQuietDisk-26, and the external hand-off becomes an edge to it.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  6, section 8 and section 10 AC6's suite cost from the analysis and dWitnessedBar's changed-line
  count are marked PINNED, and the fork's build-method citation names its tag. Design, scope and
  acceptance unchanged.
- rev-4 · 2026-11-22 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · §10 · S1 to S7 · AC1 to AC7 ·
  re-grounded at 7b8c737b0 (orders 1 and 2 built), under `2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task`.
  The suite is byte-identical to its copy at `59e882afd` (blob `8d0af8c91b34`), so its citations
  re-pin to that blob with no line moved. The cache as built costs 21 git processes for the two
  templates and adds at least 35 peak entries, measured. Today's seed costs 4, not 3, since `commit` starts a
  `maintenance` child. The wired sites run 33 times, not 10. Scope and acceptance move to F2's
  recommendation: a captured wired config replaces the cache. Why: the re-ground task's rule, and
  unit 7's consumers section, keep a `cp -a` suite off the cache. The bound moves from 7 to 32,
  the copy-install item becomes "no inline block", the switch item moves to F3, and the
  rev-3 `New arm:` line is dropped for the existing `AC5 all wired -> exit 0` arm. F2 and F3 are
  opened.
- rev-4 · 2026-11-22 · title · §1 · §3 · §8 · the run ruled F2 (b) and F3 (a), and both are marked
  RESOLVED in place. The run, not this spec's writer, restated the title and the goal to name the
  captured config. Under the rulings, the wording that read "recommendation" in section 1, the
  non-goals and the edges now reads "ruling". Design, scope and acceptance are unchanged.

## 10. Reuse audit

The seam is the suite's own `NEWREPO_SEED` (`tools/check-wiring.test.sh@8d0af8c91b34:45-52`,
TOOL-aSparedSpawn-9 S3), which already builds once per run and copies per call. This unit extends it
with one captured config rather than adding a second template. TOOL-dQuietDisk-7's factory,
`tools/lib/template-cache.sh#resolve_template` and `#build_template_clone`, was probed and costs more
here (section 4).
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once per run and copy it per test case"`
ranked `build_fixture` (`tools/lib/lib-selftest.sh`) and `build_target` (`tools/govkit/fixture_target.py`)
as seams. Neither has a face that wires a copy without a git process, so no existing seam fits
the wired copy beyond the suite's own seed.

Chain owner: dWitnessedBar (Test, gate health and budgets). Its landed unit 27 added the inline
`refuse_wrong_shell` block this suite carries at blob `8d0af8c91b34`, and no fixture line, so
nothing overlaps.

Recall terms used: `python tools/memory-recall/query.py "how do the check-wiring self-test fixtures build and wire their scratch repositories" --terms "newrepo NEWREPO_SEED template-cache resolve_template build_template_clone seed copy hooksPath wired fixture check-wiring spawn"`
