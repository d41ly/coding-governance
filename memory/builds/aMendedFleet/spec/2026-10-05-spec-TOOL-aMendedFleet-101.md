# TOOL-aMendedFleet-101 — the G0 grant fixture writes the `may:` path its own assertions read

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 102

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`unattended gate selftest shard 8/8` is red on every scheduled run of the remote CI workflow in the
census (cause C5 of the held-red census journal). Its G0 fixture builds four records for the
second-opinioned grant arms of check 19. Merge `5cb052dab` drained kit path literals out of the
suites and rewrote the fixture's grant from `tools/lander-granted.sh` to `bin/lander-granted.sh` in
the README writers, the pristine assertion and every expected message. It missed the three `sed`
lines that write the same path into the run-state files, because they spell it with an escaped
slash. The README and the run-state record now disagree inside the fixture, so the pristine
assertion fails and every arm below it grades a contradiction. This unit makes the three lines
write the path the rest of the block already reads.

## 2. Scope (IN)

- **S1** — The three `sed` lines of the G0 block in `tools/unattended/check-unattended.test.sh`
  (lines 5323, 5346 and 5355 at base) write `bin\/lander-granted.sh` where they wrote
  `tools\/lander-granted.sh`. No other byte of the suite moves. Observed by AC1 and AC2; the suite
  verdict is AC3's.
  **Readers:** by name: the G0 block's pristine assertion (line 5333 at base) and its four arms
  below it, which grep the run-state line and the expected `[bin/lander-granted.sh]` messages.
  by value: check 19 of `tools/unattended/check-unattended.sh` compares each run-state record's
  `may:` fact against its build README at the recorded BASE, so the replaced value is what that
  comparison reads; nothing outside the fixture's scratch repositories reads it.

## 3. Non-goals (OUT)

- Whether `tools/check-install-prefix.sh` sees an escaped-slash spelling of a kit path. The escaped
  form is why the drain missed these lines, but the fixture path names a loose file and not a kit
  directory, which the ban does not grade by design (the class `TOOL-aScouredKit-20` records).
  The tree-wide predicate in §4 finds no other escaped `tools\/` spelling, so there is no second
  instance to fix here.
- Any change to check 19 itself, or to the other G-blocks of the grant section.
- Moving the unattended kit version. A `*.test.sh` is withheld from adopter installs, and the build
  moves every kit version it owes once, after its last pass.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; the four line numbers are unchanged at the branch head `34a99ad17`.

- `git grep -nF 'tools\/' -- '*.sh' '*.py'` over the whole tree prints exactly the three `sed`
  lines. The unescaped spelling is gone from the block, and `git blame` shows lines 5318, 5319,
  5333, 5334, 5349, 5351 and 5353 last written by `5cb052dab`, while 5323, 5346 and 5355 still
  carry `3bd4e18b7`'s bytes.
- The failed-job log of scheduled run `37196051126`, read with `gh run view --log-failed`, carries
  five `FAIL` lines for shard 8/8 and all five are this block: the pristine assertion, the control
  arm's unexpected pin message, the two AC4 arms missing `[bin/lander-granted.sh] against [none]`,
  and the AC5 arm missing the `prompt`-mode message. The shard executed 506 assertions against a
  floor of 389. No other arm of the shard failed, so this is the shard's only cause on that run.
- Node d's `dUnstuckLanding` branch and `aGraftedHelix`'s branch both still carry the three
  `tools\/` lines, so no bytes elsewhere fix this and rule 7 of the spec brief has nothing to reuse.

### Mechanism

Three in-place substitutions inside single-quoted `sed` programs. The `sed` delimiter stays `/`,
so the slash stays escaped. The result is byte-identical to the unescaped spelling the README
writer at line 5318 and the assertion at line 5333 already use.

### Files touched (estimate)

- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Switch the three lines to a `|` delimiter so the path is unescaped.** It would make the next
  literal sweep find them, but it changes three program shapes to fix three values, and the drain
  that missed them is finished.
- **Revert the block to `tools/lander-granted.sh` everywhere.** It reintroduces the literal the
  merge drained on purpose.

## 5. Production-readiness checklist

- security — N/A: a test fixture's scratch repositories only.
- perf / scale — N/A: no new arm and no new process.
- error / empty / loading states — the block's existing pristine assertion is the empty-state
  guard, and it is what reported this defect.
- observability — N/A: no new output.
- risks — none beyond the suite; the shard's other arms passed on the census run.
- testing — AC1 and AC2 are direct and take seconds; AC3 is the held shard's own verdict.
- migration — N/A.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `git grep -cF 'tools\/lander-granted' -- tools/unattended/check-unattended.test.sh`
  runs, it prints nothing and exits 1, and the same probe for `bin\/lander-granted` counts 3.
  Red when: any of the three lines keeps the `tools` spelling; at base the first probe counted 3.
  Staged break: restore one line's old spelling and the first probe counts 1.
  figure: the count 3 is PINNED, measured at base and at `34a99ad17`.
- **AC2** — When each `sed` program the G0 block applies to a `may: none` line is extracted from
  the suite with `grep -o` and applied with `sed` to a scratch file holding `may: none`, every
  result matches the pristine assertion's own pattern from line 5333 of the suite, so the record
  writer and the assertion agree byte for byte.
  Red when: a program writes any other path; at base all three results carried the `tools` path
  and none matched. Staged break: as AC1's, which leaves one of three unmatched.
  cost: seconds; the scratch file goes under the session scratchpad.
- **AC3** — When the held shard runs after landing, its five G0 `FAIL` lines are gone; the remote
  observation is the first scheduled run of `.github/workflows/remote-ci.yml` after the landing,
  read with `gh run view --log-failed`, where the shard 8/8 job passes or fails on a line outside
  the G0 block.
  Red when: the pristine assertion's `FAIL` line still prints.
  permission: the shard is a held self-test, which no unit pass runs; the daily held job runs it on
  the hosted runner, and the main loop may run it on demand.

## 7. Gates

`unattended kit gate` · `spec tokens (a spec's own names resolve)`

New arm: none · the existing G0 pristine assertion is the arm, and AC1's staged break is what reds it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the census journal's C5 row, the shard's failed-job log
  of run `37196051126`, and a tree-wide fixed-string scan for the escaped spelling.

## 10. Reuse audit

No existing seam fits, because the change is three values inside one fixture and adds no code.
`python tools/codebase-map/reuse_lookup.py "fixture writes a grant path its own assertions grep for"`
returned only general writers (`write` in `tools/memory-tree/gotchas.py`, `write_text` in
`tools/memory-tree/gen_build_index.py`), and its header reports `.sh` as an unscanned layer, so it
cannot see this suite at all. The fixture's own builders (`ma_readme`, `ma_run`, `ma_grant` in the
same block) are the seam the substitution stays inside. Recall returned the grant ruling
`TOOL-dDerivedDocket-19` the block tests, the census row, and `TOOL-aScouredKit-20` on the prefix
ban's blindness to loose files.

Where the report and the tree disagree: the census names the lines as 5323, 5346 and 5355, and they
are still at those lines at `34a99ad17`. Nothing has fixed them on main or on either live branch.

Recall terms used: `python tools/memory-recall/query.py "why does the may grant fixture in check-unattended spell bin rather than tools, and what drained kit path literals" --terms "may: grant fixture lander-granted bin/ tools/ kit path literal drained install-prefix ban sed G0 check 19 second-opinioned"`
