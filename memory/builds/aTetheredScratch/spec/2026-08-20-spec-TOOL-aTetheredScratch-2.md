# TOOL-aTetheredScratch-2 — one external scratch root per machine, and the sweep of what is already there

**Status:** SPECCED · rev-1 · 2026-08-20 · node a · Tier-2 · base 56b945cb · streams tooling

Tier-2 despite being three small edits: it changes the temp root every hermetic gate leg writes into,
which is a cross-cutting change to the merge bar's runtime, and the grounding pass found a recorded
refusal of a neighbouring move.

## 1. Goal

Give this machine one scratch root that is external to the working tree, sweepable in a single
command, and not the shared `%TEMP%`; point `TMPDIR` at it for the agent's own shell; and remove the
litter already sitting in the operator's home directory.

The secondary prize is the documented bar timeout: `memory/guides/SESSION-KICKOFF.md:223-226` records
30733 stale scratch dirs, 58 legs, over ten minutes and still running, against the same bar finishing
on a fresh `TMPDIR`. A root that can be swept without touching the shared one makes that trap
maintainable rather than merely documented.

## 2. Scope (IN)

- `.claude/settings.local.json` — untracked, per-machine, carrying `env.TMPDIR` pointed at an external
  scratch root. On node `a` that is a dedicated subdirectory of `%TEMP%`, not `%TEMP%` itself.
- `.gitignore` — the line that keeps `settings.local.json` untracked, so the machine-specific path
  cannot be committed by accident. Today the file is two lines, `__pycache__/` and `*.pyc`.
- The sweep: the eighteen loose files in the operator's home and the `~/.gov-push/` tree, removed
  after their inventory is preserved outside the home directory.
- `memory/guides/SESSION-KICKOFF.md` — one line in the environment-traps section recording that the
  retarget exists as a per-machine opt-in and where it is configured, plus the `last-audit` re-stamp
  the ratchet requires when a watched file moves.

## 3. Non-goals (OUT)

- **A scratch root inside the working tree.** Refused on evidence, not taste — see §4. Two of the four
  breaks are not repairable with an ignore rule.
- **Writing `TMPDIR` into the tracked `.claude/settings.json`.** It is shared by nodes `a`, `b`, `c`
  and `d`, whose home directories differ; a machine path there is wrong on three of them.
- **Changing `run-gates.sh` to set `TMPDIR` for its legs.** A leg cannot set an environment variable —
  `tools/run-gates/run-gates.sh` execs its argv vector with no shell, recorded at
  `tools/check-template-size.sh:78-80` — so the value must come from the parent process, and the
  parent process is the shell this unit already configures. A second carrier would be a second answer.
- **Making any gate leg green by moving `TMPDIR`.** That is the refused shape named in
  `memory/builds/aBranchedMandate/spec/2026-08-17-spec-TOOL-aBranchedMandate-4.md:76-79`. This unit
  moves `TMPDIR` for hygiene, and §6 makes it prove it did not buy a green leg as a side effect.
- **Fixing `TOOL-aBranchedMandate-6`.** Relocating the accumulation is not repairing the cleanup.
  The row stays OPEN and this unit does not touch it.
- **Sweeping the shared `%TEMP%` root.** `memory/guides/SESSION-KICKOFF.md:226` says not to, in as many
  words: "do not delete the shared one".

## 4. Design

**Why the root must be external, with the evidence.** Pointing `TMPDIR` under the working tree breaks
four legs. Two survive an ignore rule and two do not, which is what settles it:

- `tools/check-template-size.sh:60-68` strips the repo-root prefix to derive its high-water key, so a
  scratch subject inside the tree changes key and the arms that prove the keying —
  `tools/check-template-size.test.sh:165`, `:178`, `:181`, `:205`, of which `:173` is commented as
  "THE arm that proves the KEYING" — stop measuring. A path-membership test, immune to `.gitignore`.
- `tools/check-wiring.test.sh:87` proves the non-git branch by `cd`-ing into a `mktemp -d` and
  expecting `git rev-parse --show-toplevel` to fail. Inside the tree it succeeds and the arm silently
  re-measures the ambient repo. Also immune to `.gitignore`.
- The codebase-map filesystem extractors (`tools/codebase-map/map_extractors.py:47-52` and the
  `no_subdirs` guards in `map_lib.py:215-225`) enumerate directories rather than tracked files, so a
  scratch dir under `tools/`, `.githooks/`, `memory/gotchas/`, `memory/guides/`, `memory/backlog/` or
  `tools/workflows/` is a hard `MapError`.
- The three JS gates that enumerate untracked files —
  `tools/workflows/check-review-join.sh:43-44`, `check-verifier-fanout.sh:39-40`,
  `check-workflow-syntax.js:36-40` — would judge scratch fixtures written to spell banned shapes on
  purpose. Repairable with an ignore line, and moot once the root is external.

The repo's own precedent points the same way: run-gates and memory-recall both put durable scratch
inside `.git` (`<git-dir>/gate-logs/`, `<git-dir>/recall/cache/`), where no working-tree enumerator
sees it.

**Why the carrier is `settings.local.json`.** `TMPDIR` is an absolute machine path and
`.claude/settings.json` is tracked and shared. The untracked per-machine file keeps the value where it
is true, and makes the retarget an opt-in each node takes for itself. `tools/settings-merge.py` reads
and writes only `.claude/settings.json` and only its `hooks` key, so nothing in the kit chain is
disturbed by a sibling file it never opens.

**The abandonment condition, and why it is in the design rather than the risks.**
`tools/unattended/adopt-unattended.test.sh:130-153` deliberately constructs a two-spelling divergence
and asserts the spellings really differ before asserting the adoption, precisely so the arm cannot
pass by finding nothing. A different temp root can collapse that divergence, in which case the arm
degrades to a loud skip — safe, but it costs a live arm. `TOOL-aBranchedMandate-4` pinned its AC1 to
the ambient `TMPDIR` on node `a` for that reason. So: if the retarget turns that arm into a skip, the
retarget is reverted and unit 1 ships alone. This is a design constraint, not a contingency, because
it determines whether the unit exists.

**The sweep.** The inventory is written outside the home directory first, the removal is announced
before it happens because it is irreversible, and only then do the eighteen files and `~/.gov-push/`
go. `~/.gov-push/` holds `mrecall-*` repos with read-only git objects, so removal needs a force that
`shutil.rmtree(ignore_errors=True)` does not have — the same platform fact `TOOL-aBranchedMandate-6`
is about.

## 5. Production-readiness checklist

- **Security** — no new surface. An untracked settings file holding one path; no credential, no
  network, no execution. The path is machine-local and named in no tracked file.
- **Blast radius** — every hermetic gate leg. That is the whole risk, and §6 discharges it with a full
  bar run under the new value rather than by reasoning about it. The complete inventory of `mktemp`
  and `TMPDIR` sites, grouped by kit, is in the build record from the grounding pass.
- **The one fixed-name temp file** — `tools/check-playbook-parity.sh:125` is
  `PPTMP="${TMPDIR:-/tmp}/pp.$$"`, keyed on PID with no randomisation and no EXIT trap. A long-lived
  dedicated root makes PID reuse a narrower but real collision surface than a churning `%TEMP%`. The
  leg already refuses to report agreement when it cannot write the file (`:126-131`), so the failure
  mode is a loud red, not a false green. Recorded, not fixed here.
- **Rollback** — delete `.claude/settings.local.json`. `TMPDIR` reverts to the ambient value on the
  next session and every leg behaves as it does today. Nothing else is touched.
- **Migration** — none. No state moves; the old root keeps whatever is in it until swept.
- **Observability** — a wrong `TMPDIR` is loud: `mktemp -d` fails and `tools/check-wiring.sh:389`
  already reports "cannot verify" rather than `ok`, an arm added for exactly this failure.
- **Testing** — no new test file. The proof is the existing suite run under the new value, which is
  the only thing that exercises the change.
- **a11y / i18n** — N/A.

## 6. Acceptance criteria

- **AC1** — The abandonment gate, run FIRST: `bash tools/unattended/adopt-unattended.test.sh` under the
  new `TMPDIR` still PASSES and does not emit its skip line. A skip means the two-spelling divergence
  collapsed, and the unit is reverted rather than landed.
- **AC2** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is GREEN under the new `TMPDIR`, with the
  same leg count reported as under the ambient value and no leg newly skipped.
- **AC3** — The retarget bought no green: the set of failing legs under the ambient `TMPDIR` and under
  the new one is compared and is identical. A leg that reds before and passes after is the refused
  bypass shape and blocks the unit.
- **AC4** — `mktemp -d` from a fresh agent shell resolves under the configured root, observed by
  printing the path, and the root is outside `git rev-parse --show-toplevel`.
- **AC5** — After the sweep, `ls -a ~` shows none of the eighteen inventoried names and no `.gov-push`,
  and the inventory file survives outside the home directory as the record of what was removed.
- **AC6** — `git status --short` is clean of `settings.local.json`, proving the `.gitignore` line
  works rather than assuming it.
- **AC7** — `bash skills/session-kickoff/manifest-check.sh` exits 0 after the manifest edit and the
  `last-audit` re-stamp, with the delta line recorded in the commit message.

## 7. Gates

`GATE_FULL=1 bash tools/run-gates/run-gates.sh`, run twice — once under the ambient `TMPDIR` to
establish the comparison AC3 needs, once under the new one. Plus
`bash skills/session-kickoff/manifest-check.sh` for the manifest edit.

The legs most exposed to this change are every hermetic self-test, which is most of the manifest; the
ones the grounding pass identified as location-sensitive are `template size gate selftest`,
`check-wiring self-test`, `unattended adopter e2e`, `codebase-map coverage + freshness`,
`review-join ban`, `verifier fan-out` and `workflow script syntax`.

## 8. Open questions

- **RESOLVED — internal versus external scratch root.** Considered a gitignored `.tmp/` at the repo
  root, which is what the owner's phrasing suggested. Refused on the four breaks in §4, two of which
  no ignore rule reaches. Ratified: external, a dedicated subdirectory of `%TEMP%`. Resolver: this
  design pass, on the blast-radius reading.
- **RESOLVED — tracked versus per-machine carrier.** Considered `env` in the tracked
  `.claude/settings.json`. Refused: four registered nodes with different home directories.
  Ratified: `.claude/settings.local.json` plus a `.gitignore` line. Resolver: this design pass.
- **OPEN — whether the other three nodes should adopt this at all.** This unit configures node `a`
  only, and deliberately leaves no tracked artifact that would configure `b`, `c` or `d`. Whether the
  retarget becomes a documented per-node step is an owner decision, and the manifest line in §2 is
  written to describe the opt-in rather than to prescribe it. Proceeding node-local because the
  measurement that motivates it — 30733 stale dirs — was taken on node `a` and on no other.

## 9. Revision log

- **rev-1** — 2026-08-20 — authored. Grounded on the `TMPDIR` blast-radius recon, which supplied the
  four breaks in §4, the recorded refusal in `TOOL-aBranchedMandate-4`, and the finding that no gate
  leg can set an environment variable. Two forks resolved from that reading; one owner question left
  open.

## 10. Reuse audit

No existing seam fits, and the probe is recorded rather than asserted. `python tools/memory-recall/query.py`
with the terms
`scratchpad TMPDIR mktemp hermetic scratch repo gate-logs HOME litter temp residue selftest cleanup redirect`
returned forty hits and no record proposing a permanent `TMPDIR` retarget; the only decision touching
the idea is the `TOOL-aBranchedMandate-4` refusal cited in §3, which is a refusal rather than a seam.
`grep` over the tracked tree finds exactly one `TMPDIR` assignment, `tools/check-wiring.test.sh:400`,
and it is a single-command env prefix inside one test arm — not a mechanism to extend.

What is reused is the knowledge rather than the code: the environment trap at
`memory/guides/SESSION-KICKOFF.md:223-226` already states the problem and the workaround, and this unit
makes that workaround durable on one machine instead of re-derived per session. The extension point is
therefore the manifest line, not a new tool — which is the reason this unit ships no new file under
`tools/`.
