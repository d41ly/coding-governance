# TOOL-dQuietDisk-12 — `pre-push.test.sh` builds each repeated pushed-main fixture once and copies it per arm

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-push.test.sh` rebuilds a bare remote, a work repository, a commit and a push for every
fixture it asks for, and 24 of those calls ask for a fixture an earlier call already built with the
same arguments. This unit builds each such fixture once per runner invocation through
TOOL-dQuietDisk-7's template cache and copies it per call, so the suite spends fewer git processes
and fewer real pushes for the same arms with the same RED and GREEN results.

## 2. Scope (IN)

- **S1** — Four builders become template-backed: `build_ir_fixture`, `build_sel_fixture`,
  `build_docs_fixture` and `build_bg_fixture` (`.githooks/pre-push.test.sh@609cd40b1:1410`, `:1685`,
  `:2145` and `:2417`). Each splits into a template half and a call half. The template half is
  today's body up to and including its push, run once per key by unit 7's bash face into the
  template's directory. Observed by AC1 and AC2.
- **S2** — The call half copies the template's directory to the call's `$d` with `cp -a`, then
  points the copy at itself: `git config core.hooksPath "$d/hooks"` and
  `git remote set-url origin "$d/remote.git"` in the work repository, and today's tail (`cd`, the
  `IR_R`, `SEL_R`, `BG_D`, `bg_gd` and `BG_MARK` assignments, and `: > "$BG_MARK"`). Observed by AC1
  and AC2.
- **S3** — The key is unit 7's kit tree hash plus a discriminator naming this suite, the builder, the
  digest of the builder's text, and every argument but the tag. The tag only names `$d`, so two calls
  differing only in their tag share a template. Observed by AC3.
- **S4** — A builder whose copy the probe in AC2 cannot prove equivalent to a per-call build stays
  per-call, and the spec's §9 names it with the read that differed. Observed by AC2.
- **S5** — At an install where the factory's bash face is not on disk, the suite still runs: it
  carries that face as unit 7 ships it to a copy-installed suite, and sources no file under gov's lib
  directory. Observed by AC4.
- **S6** — Under unit 7's switch at its other value, every call runs its builder whole, as today.
  That branch is the factory's. Observed by AC2.
- **S7** — The arm set, every arm's verdict and the saving are observed. Observed by AC5.

## 3. Non-goals (OUT)

- Builders whose every call carries distinct arguments: `build_pfx_fixture` (4 calls, 4 argument
  sets, one of them a hook file the arm rewrites), `build_vr_fixture` (1) and `build_sg_fixture` (2).
  A template used once costs what the build costs.
- The single-use inline fixtures at lines 285, 923, 974, 1035, 1120, 1261, 1348, 1652, 1935, 2060
  and 2105 at `609cd40b1`.
- The 75 real pushes the arms themselves make: each is the subject under test.
- `.githooks/pre-push` itself, and the push boundary's verdict and reuse rules (dWitnessedBar).
- The factory, its switch and how its bash face ships: TOOL-dQuietDisk-7.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the bash face that builds a template once per runner invocation and hands back its path, a key composition admitting a caller's discriminator, its switch, and a form a copy-installed suite can carry inline. This suite ships with the push-main kit and is a leg at adopters (`tools/govkit/entries/push-main.kit.toml@609cd40b1:98`), so without the inline form a shipped copy reds on arrival.
- **hands-off** `TOOL-dQuietDisk-19` — the suite's before and after readings, if unit 19 takes them.

## 4. Design

### Inventory of the repeated calls at `609cd40b1`

| Builder | Calls | Distinct argument sets | Repeats a built key |
|---|---|---|---|
| `build_ir_fixture` | 13 | 8 (`kit:own-mixed-contended` with `INHERITED_RED_MAX_AGE=10` six times) | 5 |
| `build_sel_fixture` | 3 | 2 (`on-demand` twice) | 1 |
| `build_docs_fixture` | 7 | 5 (`GATE_DOC_PATHS="notes/"` three times) | 2 |
| `build_bg_fixture` | 20 | 4 (no second argument fourteen times, `$PM_DECL` four times) | 16 |

Counted from the call sites, with a call inside a loop counted once. 24 calls repeat a key.

### What a call costs

Today a `build_bg_fixture` call spends 12 git processes: two `init`, four `config`, `add`, `commit`,
`branch -M`, `remote add`, one `push --no-verify` and one `rev-parse`. `build_ir_fixture`,
`build_sel_fixture` and `build_docs_fixture` spend 10 or 11 and push through the real hook with the
green stub (`GOV_GATE_CMD="bash $green"`), which spends more git processes of its own. A repeated call
after the change spends 3: the two `config` calls of S2 and the `rev-parse`. The bound: at least
24 × 7 = 168 fewer git processes per run, and 8 fewer hooked pushes. DERIVED from the call sites;
unit 19 or the close measures the real count.

### Why a copy and not a clone

A clone of the work repository would carry an `origin/HEAD` and a `branch.main` upstream that today's
`git init` plus `remote add` never makes. The hook's default-branch resolution reads `origin/HEAD`:
the suite pins `GOV_DEFAULT_BRANCH` because it is unset
(`.githooks/pre-push.test.sh@609cd40b1:263-265`). Removing both would cost two more processes. The
measured entry counts are TOOL-dQuietDisk-10 §4's: a copy and a shared clone create about the same.

### The equivalence the probe reads

For each of the four builders and each distinct argument set, the probe builds one fixture with the
switch at today's value and one copied from a template, each at its own `$d`, and compares, with
`$d` replaced by a fixed token:

- `git for-each-ref` and `git config --local --list` in the work repository and in `remote.git`;
- `git ls-files -s` and `git rev-parse HEAD^{tree}` in the work repository;
- the name and bytes of every file under each `.git` outside `objects/`, which holds what the
  hook's push wrote there, such as `push-main-active` and any stamp.

### Files touched (estimate)

`.githooks/pre-push.test.sh`

### Alternatives rejected

- Templating every builder: three of them never repeat a key, so a template would cost what the
  build costs.
- A clone per call: rejected above.

## 5. Production-readiness checklist

- security: N/A — no new write path; copies land in the suite's own scratch.
- perf / scale: at least 168 fewer git processes and 8 fewer hooked pushes per run (§4).
- error / empty / loading states: a failed template build returns 1 from the builder, which every
  caller already reports as `could not build its fixture`.
- observability: none added.
- risks: a hook record written during the template's push that names the template's path; S4 keeps
  that builder per-call.
- testing: AC1 to AC4 are probes of this unit's code; AC5 runs the suite and is the main loop's.
- migration: N/A — templates live for one runner invocation.
- user docs: N/A — test fixtures; no `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — When a probe sources the four builders out of the edited suite into a scratch script
  and calls each twice with one argument set and two tags under `GIT_TRACE2_EVENT=<dir>`, the second
  call adds at most 3 trace files.
  Red when: a repeated key rebuilds, or the call half spawns more than its two `config` calls and one
  `rev-parse`.
- **AC2** — When the same probe runs the equivalence of §4 over every distinct argument set of the
  four builders, every read is byte-identical after the `$d` substitution.
  Red when: a copied fixture differs in a ref, a config value, the index, the tree or a git-dir file.
- **AC3** — When the probe calls `build_bg_fixture` with tags `a` and `b` and no second argument,
  then with `$PM_DECL`, the first two share one template and the third builds another.
  Red when: the tag enters the key, or an argument is left out of it.
- **AC4** — When `grep -nE '(^|[;&|] *)(\.|source) .*/lib/' .githooks/pre-push.test.sh` runs, it
  prints nothing, and the factory's bash face appears in the suite as the inline form unit 7 ships.
  Red when: the suite sources a file under gov's lib directory, which no adopter holds.
- **AC5** — When the main loop runs the suite at the build base and at this unit's commit, each in a
  scratch `git clone --shared` with `GIT_TRACE2_EVENT`, `TEMP`, `TMP` and `TMPDIR` pointed at scratch
  dirs, both runs print the same `ok` and `FAIL` lines, the git process count falls by at least 168,
  and residual temp entries are 0 both times.
  Red when: a line changes, the count does not fall by the bound, or an entry remains.
  permission: a role pass may not run a `.test.sh` suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  figure: 168 is DERIVED from §4's call-site count at `609cd40b1`.
  fixture: the adopter half is a scratch target that `python tools/govkit/govkit.py apply` installs
  the push-main kit into, where the main loop runs the shipped suite; `tools/govkit/fixtures/` holds
  no adopter tree with this kit today. `python tools/govkit/govkit.py check --target
  C:/projects/incms/main` and `--target C:/projects/nicocares/main`, run read-only from gov, read
  the same before and after.

## 7. Gates

`pre-push self-test`

New arm: .githooks/pre-push.test.sh · covers AC2 · an arm copies a bg fixture whose call half skips the `core.hooksPath` rewrite, and the hook no longer fires on its push · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.

## 10. Reuse audit

The seam is TOOL-dQuietDisk-7's template factory, generalising `tools/lib/lib-selftest.sh`
`build_fixture`, which builds once and copies per arm; this suite's builders already share one
shape, bare remote plus work plus push, so the factory serves them unchanged.
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once and clone it per test case"`
ranked `build_fixture`, `build_target` and `build_scratch_gov` as seams, and no pre-push builder.
Chain owner: dWitnessedBar (Test). Its branch changes 811 lines of this suite between `9e21ac760` and
`609cd40b1`: it re-signed `build_ir_fixture` and `build_docs_fixture`, added `build_sel_fixture`,
and added `build_bg_fixture` calls. This unit builds on its landed tip and re-counts §4's table
there.

Recall terms used: `python tools/memory-recall/query.py "how does the pre-push self-test build its pushed fixture repositories" --terms "pre-push.test.sh build_bg_fixture build_ir_fixture fixture remote.git push template copy hooksPath GOV_GATE_CMD"`
