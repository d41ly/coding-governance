# TOOL-dScrubbedConduit-1 — five kit defects an adopter found by hitting them

**Status:** OPEN · rev-1 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Fix five defects reported from `d41ly/nc`, which re-adopted the whole kit set on 2026-08-23. Each was
found by an adopter paying for it, not by a gate here. Four of the five are structurally invisible in
this repo, because gov's own layout is the one layout that does not trigger them.

## 2. Scope (IN)

- **S1 — `rosters()` cannot read a corpus containing a binary.** `tools/memory-tree/gen_build_index.py:492-494`
  guards `read_text` with `except Problem`, but `read_text` raises `UnicodeDecodeError`, which is not
  a `Problem`. Any non-UTF-8 tracked file under the memory root crashes the generator with a
  traceback. nc carries a UI review screenshot at `memory/builds/*/reviews/*/obs-spec/*.png`; that is
  a legitimate record, and it took the generator down. A roster is built from ids in PROSE, so a file
  that is not text cannot contribute one and skipping it changes no output. Widen the except.
- **S2 — the pre-push hook leaks `GIT_DIR` into every leg.** Git EXPORTS `GIT_DIR` (and friends) into
  hooks. A leg that creates a scratch repo with `git init` inherits it and initialises the SHARED
  gitdir instead of its temp dir. Where that gitdir has no worktree of its own — a SUBMODULE — `git
  init` sets `core.bare=true` on a config that also carries a per-worktree `core.worktree`, and every
  subsequent git call answers `fatal: this operation must be run in a work tree`. Scrub the
  environment at the boundary that injects it.
- **S3 — `kit-dogfood-parity.test.sh --render` cannot create a first render.** Line 77 `continue`s
  past a missing live copy in EVERY mode, including `--render`, whose entire job is to write that
  file. An adopter installing `BUILD-METHOD.template.md` for the first time gets
  `kit-parity: missing live copy` from the command documented as the fix for it, forever. Render when
  the mode is `--render`; keep the failure for `--check`.
- **S4 — the `keepalive-tool-names` discharge probe can never pass.** `tools/unattended/kit.toml:110`
  discharges on `! grep -qE '<[a-z-]+>' .claude/skills/unattended/SKILL.md`, and
  `SKILL.template.md` itself contains 25 `<slug>`, 6 `<name>`, 3 `<unit-id>` and more as DOCUMENTED
  SYNTAX. The probe therefore fails for every adopter no matter how correctly the conf is filled —
  measured on nc with all four keepalive values correct and 32 matches remaining. A hole that can
  never be discharged is a hole nobody can close, which is worse than the half-silence it was added
  to fix. Narrow the probe to the ANGLE-BRACKET VALUES the conf actually substitutes.
- **S5 — the five defects above get gates, or a recorded reason they cannot.** Per the charter, a
  finding is not done until it is a gate OR a documented check. S1-S4 are each a one-line fix; the
  standing risk is that nothing stops them recurring.

## 3. Non-goals (OUT)

- **`playbook.fixture.md`'s hardcoded `tools/unattended/` is NOT fixed here.** It was the fifth
  reported ask. Its `outputs`, `grain`, `records` and `legs` all name that literal path under
  `coverage = "resolvable"`, so the playbook leg exits 1 for any adopter installing the kit at another
  prefix — nc measured exactly that and moved the kit rather than patch a receipted file. The fix is a
  path-token substitution across a fixture whose whole purpose is to be byte-stable, and the records
  under `fixture-records/` literally encode `tools~unattended~…` in their FILENAMES. That is a
  redesign of the fixture's addressing, not a line change, and it does not belong in a unit whose
  other four items are one-liners. Filed as its own backlog row.
- **No adopter-side change.** nc already carries local carve-outs for all five. Those stay until the
  kit ships fixes and nc re-adopts; this unit does not reach into nc.
- **No version bumps beyond what the changed kits require**, and no kit re-release process.
- **`govkit`'s `seed` role is NOT touched.** nc filed it as an ask and then WITHDREW it — the premise
  was false, `seed` is write-if-absent. Recorded here so the withdrawal travels with the batch.

## 4. Design

### Why four of five are invisible here

| # | needs, to reproduce | gov has it? |
|---|---|---|
| S1 | a non-UTF-8 tracked file under the memory root | no — gov's memory tree is all text |
| S2 | a repo whose `GIT_DIR` has no worktree — i.e. a SUBMODULE | no — gov is a top-level clone |
| S3 | a first-time render, i.e. an adopter without the live copy yet | no — gov has always had all three |
| S4 | any adopter at all | **yes** — gov is exposed too, and its own probe has never passed |

S4 is the interesting row. It is not adopter-specific; it fails here as well, and the reason nobody
noticed is that a `[[hole]]` probe is not a gate leg — nothing on the merge bar runs it.

### The mechanism behind S2, stated once

`git init` with `GIT_DIR` set does not create a repo at the cwd. It re-initialises the repo `GIT_DIR`
names, and re-derives `core.bare` from whether that path has a worktree. For a normal clone the
answer is "yes, it does" and nothing changes — which is why gov, and every non-submodule adopter,
sees nothing. For a submodule gitdir the answer is "no", so `core.bare` flips to `true` and collides
with the `core.worktree` the submodule needs. The value reverts later, which makes it present as a
race with another session; nc reported it as one twice before bisecting it.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · `.githooks/pre-push` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/unattended/kit.toml` · the test files for each · `tools/gate-legs.json` if S5 adds a leg.

### Alternatives rejected

- **S2 in `run-gates.sh` instead of the hook.** The runner is not the only thing a hook invokes, and
  the pollution is injected by the hook boundary. Fixing it at the runner leaves every other
  hook-invoked path exposed. REJECTED in favour of the hook — but see Q1: doing BOTH may be right.
- **S4 by dropping the probe.** It exists because the hole is genuinely half-silent: a verbatim
  example conf renders placeholder prose and passes every check. Deleting the probe restores that
  silence. REJECTED; narrow it instead.

## 5. Production-readiness checklist

- **security** — S2 is the only item with a blast radius beyond a red gate: a leaked `GIT_DIR` lets a
  leg write to a repo it was never pointed at. The fix removes an ambient capability rather than
  adding one.
- **perf / scale** — N/A. Four one-line changes.
- **a11y / i18n** — N/A.
- **error / empty / loading states** — S3 IS an empty-state defect: the tool's behaviour when its
  output does not exist yet.
- **observability** — S2's failure mode is actively misleading, not merely silent: it presents as a
  concurrent-session race. Whatever gate S5 adds should name the mechanism, so the next person does
  not spend three blocked pushes on it.
- **risks** — widening an `except` (S1) can mask a real decode failure elsewhere; the mitigation is
  that this catch is scoped to one read whose result is optional. Changing `--render` semantics (S3)
  could mask a genuinely missing TEMPLATE; keep that arm failing.
- **testing + left-shift gates** — each kit already ships a self-test; S1-S4 extend those rather than
  adding new harnesses. Every new arm must be observed RED before it is called landed.
- **migration / rollback** — none needed. No stored data, no generated artifact changes shape.
- **user docs** — N/A. Kit-internal.

## 6. Acceptance criteria

- **AC1** — When a non-UTF-8 tracked file is placed under a fixture memory root and `gen_build_index.py`
  runs, it completes and reports the same artifacts as without that file. Observed RED first: the
  same fixture on the unfixed code raises `UnicodeDecodeError`.
- **AC2** — When `.githooks/pre-push` runs a leg that executes `git init` in a temp dir with `GIT_DIR`
  exported, the shared config's `core.bare` is unchanged. Observed RED first, in a SUBMODULE fixture,
  where the unfixed hook flips it to `true`.
- **AC3** — When `kit-dogfood-parity.test.sh --render` runs against a tree missing one live copy, it
  WRITES that copy and exits 0; and `--check` against the same missing copy still exits non-zero.
  Both arms observed.
- **AC4** — When the `keepalive-tool-names` discharge probe runs against a correctly-filled SKILL.md
  it passes, and against one carrying an unsubstituted conf value it fails. The second arm is what
  the hole exists for and is the one to observe.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, it is green, and every leg this unit
  touched ran rather than skipped.

## 7. Gates

The full bar, `bash tools/run-gates/run-gates.sh`. The legs this unit can move: the memory-tree kit
self-tests, the unattended kit self-tests (owner-demand, not on the bar — so they must be run by hand
and their verdict reported), `check-kit-versions.sh` if any version constant moves, and
`govkit selfcheck` if `kit.toml` changes shape.

New gates: S5's, whose form is Q2.

## 8. Open questions

- **Q1 — does S2 belong in the hook, the runner, or both?** RECOMMENDATION: both. The hook is where
  git injects the variables, so it is the correct single point; but `run-gates.sh` is invoked directly
  by sessions too, and a leg that `git init`s is a hazard whenever any ambient `GIT_DIR` is set,
  hook or not. Scrubbing twice costs one line and closes the path the hook does not cover.
- **Q2 — what shape should S5's gate take?** Options: (a) a self-test arm per fix, in each kit's own
  suite — cheap, but the unattended suites are owner-demand only, so S2 and S4 would land behind a
  gate nothing runs; (b) one new bar leg that asserts the four behaviours from a fixture — visible,
  but a fifth harness to maintain; (c) fold S1/S3 into their kits' suites and give S2/S4 a bar leg,
  since those two are the ones no suite on the bar covers. RECOMMENDATION: (c).
- **Q3 — should the `[[hole]]` discharge probes run on the bar at all?** S4 has never passed here and
  nobody noticed, because a hole probe is not a leg. That is a general gap, not specific to this
  hole. RECOMMENDATION: out of scope for this unit; file it, because fixing S4's probe without this
  leaves the next broken probe equally unobserved.

## 9. Revision log

- rev-1 · 2026-08-23 · initial draft. Five asks in, one moved to non-goals as a redesign rather than
  a fix.

## 10. Reuse audit

No new machinery. S1, S3 and S4 are edits to existing kit files and their existing self-tests. S2
adds one `unset` line at a boundary that already exists. The only candidate for new surface is S5's
gate, and Q2 recommends folding two of the four into suites that already run rather than building a
fifth harness. The seam for S2 is `.githooks/pre-push`, which nc has already carved locally — the
adopter's carve-out is the prototype this unit upstreams.
