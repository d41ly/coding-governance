# TOOL-dQuietDisk-13 — the run-gates suites build each repeated scratch repository once and copy it per arm

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

Three run-gates suites rebuild the same scratch repository on every call of five builders, about 150
calls between them. This unit builds each of those repositories once per runner invocation through
TOOL-dQuietDisk-7's template cache and copies it per call, so the suites spend fewer git processes for
the same arms with the same RED and GREEN results.

## 2. Scope (IN)

- **S1** — `tools/run-gates/run-gates.turnstile.test.sh`: `mk_repo`
  (`tools/run-gates/run-gates.turnstile.test.sh@609cd40b1:343`) builds its repository from a
  template. The beacon and queue removal at its head stays per call, because it clears host state
  every arm reads. Observed by AC1 and AC2.
- **S2** — `tools/run-gates/run-gates.evidence.test.sh`: `rec_repo`, `ru_repo` and
  `fresh_gitdir` (`tools/run-gates/run-gates.evidence.test.sh@609cd40b1:504`, `:1315` and `:367`)
  build from templates. `ru_repo`'s call half re-points `origin` at the call's own
  `"$RU_T.origin.git"`, which is absolute, and re-derives `RU_E` and `RU_C2` as today's last two
  lines do. `rec_repo`'s `origin` is `../origin.git`, relative, so its copy needs no rewrite.
  `build_lin_repo` calls `ru_repo` and keeps its own tail. Observed by AC1 and AC2.
- **S3** — `tools/run-gates/run-gates.test.sh`: `build_hv_repo`
  (`tools/run-gates/run-gates.test.sh@609cd40b1:3442`) builds from a template. Observed by AC1 and AC2.
- **S4** — Each template's key is unit 7's kit tree hash plus a discriminator naming the suite, the
  builder and the digest of its text. None of the five takes an argument that shapes its content:
  each takes only a destination. Observed by AC3.
- **S5** — A builder whose copy the probe in AC2 cannot prove equivalent to a per-call build stays
  per-call, and this spec's §9 names it with the read that differed. Observed by AC2.
- **S6** — Under unit 7's switch at its other value, every call runs its builder whole, as today.
  That branch is the factory's. Observed by AC2.
- **S7** — The arm sets, their verdicts and the saving are observed. Observed by AC4.

## 3. Non-goals (OUT)

- `tools/run-gates/run-gates.gov.test.sh`. It builds no fixture: it holds no `git init`, `mktemp -d`,
  clone or worktree at `609cd40b1`, and grades gov's own corpus in place.
- `tools/run-gates/run-gates.runlog.test.sh`, which matches the `run-gates*.test.sh` glob and which
  the spec brief does not name. It has one `git init`.
- The builders whose calls never repeat a content: `build_attr_fixture` (1 call),
  `build_replay_fixture` and `build_age_fixture` (3 calls each, 3 argument sets each),
  `build_moved_age_fixture` and `build_owned_fixture` (1 each), and the single-use inline repositories.
- The nested bars the arms run, 134, 70 and 39 of them by the analysis's count (§3, row G1d). Each is
  the subject under test, and the runner's own fixed cost is K9, which the prompt does not ask for.
- An inline form of the factory's face. All three suites are withheld from `govkit apply` with
  `role = "project-owned"` (`tools/run-gates/kit.toml@609cd40b1:44-46`) and are gov-only legs, so they
  may source gov's lib directory as `tools/check-line-length.test.sh` does.
- The factory, its switch and its concurrency: TOOL-dQuietDisk-7.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the bash face that builds a template once per runner invocation and hands back its path, a key composition admitting a caller's discriminator, and its switch. Without it there is nothing to copy from.

## 4. Design

### Inventory at `609cd40b1`

| Builder | Calls | git today, per call | git after, per repeated call | Saved per run |
|---|---|---|---|---|
| `mk_repo` (turnstile) | 46 | 3: `init`, `add`, `commit` | 0 | 135 |
| `rec_repo` (evidence) | 31 | 6: `init`, `add`, `commit`, `remote add`, `update-ref`, `symbolic-ref` | 0 | 180 |
| `ru_repo` (evidence) | 29 | 8: the six above, `hash-object -w`, `commit-tree` | 3: `remote set-url`, `hash-object`, `commit-tree` | 140 |
| `fresh_gitdir` (evidence) | 7 | 1: `init --bare` | 0 | 6 |
| `build_hv_repo` (canary) | 17 | 3: `init`, `add`, `commit` | 0 | 48 |

Calls are counted from the call sites, a call inside a loop or a function counted once, and the
first call of each builder pays the full build. The bound: at least 509 fewer git processes over
the three suites per run. DERIVED from these counts; the measured figure is the close's.

### The call half

```bash
mk_repo() {
  local d=$1
  rm -rf "$GATE_TURNSTILE_DIR"/gate-bar-beacon "$GATE_TURNSTILE_DIR"/gate-bar-beacon.* \
         "$GATE_TURNSTILE_DIR/gate-bar-queue" 2>/dev/null
  mkdir -p "$d" && cp -a "$(template_of mk_repo _build_mk_repo)/." "$d/"   # unit 7's face
}
```

`template_of` stands for unit 7's bash face as its spec spells it. `_build_mk_repo` is today's body
after the beacon removal, moved and not edited. The other four follow the same shape.

### Why a copy and not a clone

Every builder here writes an uncommitted or once-committed repository with no remote, or a remote
it configures by hand. A clone adds `refs/remotes/origin/*` and an upstream that `rec_repo` and
`ru_repo` set themselves to a different value, and the runner's remote ladder reads both
(`tools/run-gates/run-gates.evidence.test.sh@609cd40b1:520-524`). A copy spends 0 git processes. The
entry counts are TOOL-dQuietDisk-10 §4's measurement.

### The equivalence the probe reads

For each of the five builders the probe builds one repository with the switch at today's value and
one copied from a template, and compares, with the destination path replaced by a fixed token:
`git for-each-ref`, `git config --local --list`, `git ls-files -s`, `git status --porcelain`,
`git rev-parse HEAD^{tree}` where a commit exists, and the name and bytes of every work-tree file.

### Files touched (estimate)

`tools/run-gates/run-gates.turnstile.test.sh` · `tools/run-gates/run-gates.evidence.test.sh` ·
`tools/run-gates/run-gates.test.sh`

### Alternatives rejected

- One shared template for all five builders: their trees differ, so one template would need a
  per-call rewrite larger than the build it replaces.
- A clone per call: rejected above.

## 5. Production-readiness checklist

- security: N/A — no new write path; copies land in each suite's own scratch.
- perf / scale: at least 509 fewer git processes per run of the three suites (§4).
- error / empty / loading states: a failed template build returns 1 from the builder, which every
  caller already handles as a failed build (`mk_repo "$R" || { ...; exit 2; }` and its kin).
- observability: none added.
- risks: a template built while a commit moves the runner under it
  (`memory/gotchas/suite-invalidated-by-a-commit-under-it.md`); the key carries the factory's kit tree
  hash, so a moved tree builds a new template.
- testing: AC1 to AC3 are probes of this unit's code; AC4 runs the suites and is the main loop's.
- migration: N/A — templates live for one runner invocation.
- user docs: N/A — test fixtures; no `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — When a probe sources the five builders out of the edited suites into a scratch script
  and calls each twice under `GIT_TRACE2_EVENT=<dir>`, the second `mk_repo`, `rec_repo`,
  `fresh_gitdir` and `build_hv_repo` call adds 0 trace files and the second `ru_repo` call adds
  at most 3.
  Red when: a repeated call rebuilds its repository.
- **AC2** — When the same probe runs the equivalence of §4 over the five builders, every read,
  `git for-each-ref` and `git config --local --list` among them, is byte-identical after the path
  substitution.
  Red when: a copy differs in a ref, a config value, the index, the status, the tree or a file.
- **AC3** — When the probe edits `_build_mk_repo`'s text in a scratch copy of the turnstile suite
  and asks for the template, the factory builds a new one.
  Red when: the key omits the builder digest and the old template is reused.
- **AC4** — When the main loop runs `extract-arms.sh` over the `run-gates canary`,
  `run-gates turnstile` and `run-gates evidence` legs at the build base and at this unit's commit, each in a scratch `git clone --shared` with
  `GIT_TRACE2_EVENT`, `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs, each suite prints the same
  per-arm lines and the same `PASS` total both times, the summed git process count falls by at least
  509, and residual temp entries are 0 both times.
  Red when: an arm line changes, the count does not fall by the bound, or an entry remains.
  permission: a role pass may not run a `.test.sh` suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: three suites whose ceilings run to tens of minutes each.
  figure: 509 is DERIVED from §4's call-site count at `609cd40b1`.

## 7. Gates

`run-gates canary` · `run-gates turnstile` · `run-gates evidence`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC2 · an arm copies a `ru_repo` template whose call half skips the `origin` rewrite, and the scoped-skip arm reds on the template's remote · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.

## 10. Reuse audit

The seam is TOOL-dQuietDisk-7's template factory, generalising `tools/lib/lib-selftest.sh`
`build_fixture`. Each builder here already has one function per base repository, so it becomes the
template's builder unchanged and its callers do not move.
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once and clone it per test case"`
ranked `build_fixture`, `build_target` and `build_scratch_gov` as seams, and none of these five.
Chain owner: dWitnessedBar (Test). Its branch changes 256, 18 and 320 lines of the three suites
between `9e21ac760` and `609cd40b1`, the verdict, held-leg and flake arms among them, so this unit
builds on its landed tip and re-counts §4's table there.

Recall terms used: `python tools/memory-recall/query.py "how do the run-gates canary, turnstile and evidence suites build their scratch repositories" --terms "mk_repo rec_repo ru_repo build_hv_repo fresh_gitdir scratch repository template copy run-gates turnstile evidence canary"`
