# TOOL-aMendedFleet-6 — `lexicon wiring` passes on the hosted runner: the conf reader writes UTF-8

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`lexicon wiring` has been red on every push run of the remote CI workflow, always with `lexicon:
DRIFTED` against the rendered Skill. The report put it down to `tools/lexicon/*.template.md` landing
CRLF and asked for an `eol=lf` pin. That is not the cause. The template is LF in the index, the CI
checkout keeps index bytes, and the render strips every CR anyway. The cause is the verb table's
glosses: `adopt-lexicon.sh` reads them from `lexicon_conf.py --print-rows` through a pipe, and on a
Windows host outside Python's UTF-8 mode that stdout is the ANSI code page, so every em dash arrives
as the byte 0x97 and the render no longer matches the UTF-8 Skill. Node a never sees it because its
user environment exports `PYTHONUTF8=1`. This unit makes the conf reader write UTF-8 on every host,
and adds a selftest arm that runs it under the hosted runner's codec.

## 2. Scope (IN)

- **S1** — `tools/lexicon/lexicon_conf.py` reconfigures its stdout to UTF-8 when it runs as a
  script, in its `__main__` block and nowhere else, so `lexicon.py`, `selftest.py` and every other
  importer keep their own stdout. Observed by AC1 and AC2.
- **S2** — `tools/lexicon/selftest.py` gains one arm that runs `lexicon_conf.py --print-rows` over a
  conf whose gloss carries an em dash, with `PYTHONUTF8=0` and `PYTHONIOENCODING` removed from the
  child's environment, and asserts the em dash arrives as its three UTF-8 bytes. Observed by AC3.
  **Readers:** by name: `tools/lexicon/selftest.py` alone spells the child environment the arm builds.
  by value: NO VALUE READERS — the variables are dropped from one child process the arm spawns, and
  nothing outside that child reads them.
- **S3** — Where a redirected stdout under that environment reports a UTF-8 codec anyway, the arm
  prints one `lexicon selftest SKIP` line naming the ungraded dependency, and never passes silently.
  Observed by AC3.

## 3. Non-goals (OUT)

- An `eol=lf` pin on `tools/lexicon/*.template.md`, which the report proposed. `git ls-files --eol`
  shows the template as `i/lf`, the workflow sets `core.autocrlf false` so a CI checkout is LF, and
  `render_skill` in `tools/lexicon/adopt-lexicon.sh` strips CR from the template and again after
  substitution. A pin would change no byte the leg compares.
- A repo-wide gate for the stdout-codec class, which is this build's census question; the matching
  fixes in other kits, which are unit 4's and unit 5's.
- Moving the lexicon kit version. The kit's carriers and the Skill's rendered marker move together,
  and the build moves every kit version it owes once, after the last pass that touches that kit. The
  close's `kit epoch` leg grades that move.

### Edges

- **hands-off** `TOOL-aMendedFleet-7` — whether other held suites red on the same stdout codec, and
  whether a bar-level class gate is owed, is that census's question.

## 4. Design

### Evidence

Read at base `7af5f564`, which carries the same bytes for every file below as `origin/main` at
`35438ba0`.

- The remote CI workflow `.github/workflows/remote-ci.yml` runs its `bar` job on `windows-latest`
  under Git-Bash, sets `core.autocrlf false` globally, and does not export `PYTHONUTF8`.
- Push runs 36938524056, 37003260109, 37194768619, 37200259184 and 37220352485 each red this leg with
  `lexicon: DRIFTED` naming `.claude/skills/lexicon/SKILL.md` against a fresh render of
  `tools/lexicon/SKILL.template.md`.
- `git ls-files --eol` reads `i/lf` for the template and for the Skill; the Skill's attributes pin
  `eol=lf` already, and the template is `text=auto`.
- On node a, `bash tools/lexicon/adopt-lexicon.sh --check` prints `lexicon-adopt OK` with
  `Skill in sync`. Under `env -u PYTHONUTF8` it prints the CI's `lexicon: DRIFTED` lines, and does
  the same with `PYTHONIOENCODING=cp1252`.
- `lexicon_conf.py --print-rows .lexicon.conf` prints 23 rows carrying a non-ASCII byte. Under
  `env -u PYTHONUTF8` the first gloss's em dash arrives as the single byte 0x97.

### Mechanism

S1 is one line placed before `raise SystemExit(_main(sys.argv))`, and it is the first line of the
pair `tools/memory-tree/adopt-memory-tree.sh` already carries: `sys.stdout.reconfigure(encoding="utf-8")`.
Newline translation is untouched; `render_skill` strips the CR it adds. `_main` writes its refusals
to stderr, and their text is ASCII apart from what a conf error quotes back, so stderr needs nothing
for this leg.

S2 builds its fixture conf the way the suite's existing arms do, runs the child through
`subprocess.run` with an explicit `env` and `capture_output=True`, and reads the BYTES, never text,
so the assertion cannot be satisfied by a decode that hides the codec. Its liveness probe is the same
child environment running `import sys; print(sys.stdout.encoding)`; a UTF-8 answer selects S3's skip.
The arm sits beside the suite's existing `lexicon selftest SKIP` announcer and uses its wording.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`
- `tools/lexicon/selftest.py`

### Alternatives rejected

- **Set `PYTHONIOENCODING=utf-8` on the call in `adopt-lexicon.sh`.** It fixes one caller of the
  reader and leaves the next one to rediscover the class; the reader is the one place every caller
  routes through.
- **Decode the reader's output in the shell.** Bash has no codec to decode with, and the render would
  have to know which code page the host used.
- **The report's `eol=lf` pin.** Refuted by the evidence above; see §3.

## 5. Production-readiness checklist

- security — N/A: no new input, write path or surface.
- perf / scale — one child process per run of the new arm, plus its probe.
- error / empty / loading states — S3's skip line is the ungraded state, and it is never silent.
- observability — the skip line names the dependency it could not grade.
- risks — an adopter with a UTF-8 code page sees no change; one without it sees its rendered Skill
  stop drifting.
- testing — AC1 and AC2 are direct and take seconds; AC3 is the held suite's.
- migration — N/A: the rendered Skill's bytes do not change, because node a already rendered it
  under UTF-8.
- user docs — N/A: no user-facing surface; the class is already a section of
  `memory/gotchas/fixture-inherits-ambient-machine-state.md`.

## 6. Acceptance criteria

- **AC1** — When `env -u PYTHONUTF8 bash tools/lexicon/adopt-lexicon.sh --check` runs on node a, it
  prints `lexicon-adopt OK` with `Skill in sync`.
  Red when: S1's line is absent, which at base printed `lexicon: DRIFTED`.
  cost: about 8 s.
- **AC2** — When `PYTHONUTF8=0 PYTHONIOENCODING= python tools/lexicon/lexicon_conf.py --print-rows .lexicon.conf`
  runs on node a, piped into `LC_ALL=C grep -c $'\xe2\x80\x94'`, the count is at least 1, and no
  output byte is 0x97, which the UTF-8 em dash never contains.
  Red when: S1's line is absent, which at base printed the em dash as the single byte 0x97.
  figure: the count is DERIVED at observation time from the repo's own `.lexicon.conf`.
- **AC3** — When the arm S2 adds runs, it passes; with S1's line removed as a staged break it reds
  naming the 0x97 byte; on a host whose redirected stdout is UTF-8 it prints a `lexicon selftest SKIP`
  line and does not fail. The arm's own child invocation is AC2's command, so AC2 observes its
  predicate directly on node a.
  Red when: the arm decodes the child's output as text, so the codec is hidden before it is graded.
  permission: the arm lives in the lexicon kit's held self-test, which no unit pass runs; the daily
  held CI job runs it on `windows-latest`, and the main loop may run it on demand.

## 7. Gates

`lexicon wiring` · `lexicon selftest` · `codebase-map kit selftest` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · S2's codec arm, staged red by removing S1's reconfigure line from lexicon_conf.py · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the remote CI logs and the lexicon kit at base, with the
  leg's own check run on node a with and without Python's UTF-8 mode.

## 10. Reuse audit

The seam is a line this repo already ships twice, and no symbol-level seam fits.
`python tools/codebase-map/reuse_lookup.py "python stdout encoding utf-8 on a windows locale codec"`
returned no function that reconfigures a stream; its nearest hit was `check_encoding` in
`tools/gate-lint/encoding_posture.py`, whose header puts stdout out of scope. The line S1 copies is
`tools/memory-tree/adopt-memory-tree.sh` line 204, also at `tools/lib/render-doc.sh` line 135. The
codec-forcing arm S2 follows `tools/govkit/selftest.py`, which runs its blocks with `PYTHONUTF8=0`
and `PYTHONIOENCODING` unset and announces a skip where the code page is UTF-8. Recall returned the
class as a section of `memory/gotchas/fixture-inherits-ambient-machine-state.md`, which records the
same em dash arriving as 0x97 from govkit.

Where the report and the tree disagree: the report places the CI reds on Linux, and the workflow runs
on `windows-latest`. It names a CRLF template as the cause; the template is LF in the index and in a
CI checkout, the render strips CR twice, and the leg reds on node a only once `PYTHONUTF8` is unset.

Recall terms used: `python tools/memory-recall/query.py "why does a python tool print wrong bytes on a Windows host without PYTHONUTF8, and how was it fixed before" --terms "PYTHONUTF8 cp1252 cp1251 stdout reconfigure encoding utf-8 locale codec Windows CI remote-ci host-dependent red"`
