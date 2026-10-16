# TOOL-dRedressedBar-5 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-5

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The builder's return says the probe output "was not
committed: no acceptance ledger exists for any unit of this build, so the main loop records it at
the close"; this is that record. The unit was built against spec 5 rev-5 in the one pass commit
`ecdca277e`. Spec 5's rev-6 names AC1 and AC2 and says "no criterion text moves", so the readings
answer the criteria as they stand. The readings are the builder's, from that commit's body and
from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
`2026-10-14T15:57:14 · gov-builder · wf_295d6b9f-6a5/a5092d46835faecff` at line 4882. Every probe
ran under bash 5.3.9. No merge bar, no self-test suite and no gate leg ran in the build pass, and
the section 7 legs were owed to the close.

**Evidences:** TOOL-dRedressedBar-5
- AC1 — `grep -nE '\$\((basename|dirname|date) '` — over the four files it printed nothing.
- AC2 — `var-pipe` — the count printed 0, 0 and 0 for the branch-reconcile adopter, the roles
  adopter and the roles suite, and 62 for `tools/workflows/unattended-build.test.sh`, equal to that
  file's row. Imported, sh_hygiene's own `scan_spawn_file` read 0 registry-class sites in the four
  row-less files, and printf-subst 66, var-pipe 62, pure-fn-subst 28, path-subst 6 and cat-file 1
  for the suite, each equal to its row.
- AC3 — `printf -v _wfj` — the whole-file `$(printf ` count fell from 288 to 275. The commit's diff
  holds five `-` lines with a pipe-free `$(printf `, and their `+` lines say `printf -v _wfj`.
- AC4 — `${CH%/*}` — the forms probe ran 186 specimen pairs, among them the specimens the
  criterion names and every converted site read at its converted line, and every pair matched.
  Both staged wrong forms differed: `${CH%/*}` alone on `AGENTS.md`, and the CR strip inside
  `$( )`. A second probe ran arm 9's compare over the suite's own A9L1 and A9L2 values: 4 of 4
  matched, and the wrong form failed on the CRLF value.
- AC5 — `TMPDIR` — in a clone under `%TEMP%/u5fx`, with `TMPDIR` set to the scratchpad, the
  `ebce889c` adopters and the converted ones printed the same lines and statuses from the root,
  from each kit directory, by absolute path and as `./`. That clone's fixture passed 25 of 25
  checks across AC5 to AC7.
- AC6 — `.claude/skills/branch-reconcile/SKILL.md` — in the same clone, the recognised render there
  was withdrawn, a foreign file was kept, a near-miss name was kept, a CRLF render was withdrawn,
  and the `tools/` hits printed indented, as the criterion states.
- AC7 — `{{UNKNOWN_TOKEN}}` — in the same clone, the refusal printed the
  `    line <n>:{{UNKNOWN_TOKEN}}` line.
- AC8 — `memory/project/spawn-idiom-sites.txt` — its diff at the pass commit is empty.
- AC9 — `mkdir -p "${SKILL%/*}" || exit 1` — the pin file's diff is one hunk with one `-` line and
  one `+` line, five fields each, agreeing on fields 1, 2, 3 and 5. Row 178 was re-keyed to that
  converted line in field 4 only, and the file holds 181 lines at both commits.
- AC10 — `scan_refusal_sites` — check-arms' own `scan_refusal_sites` and `parse_pin` found all 11
  pins of the branch-reconcile adopter live, with 13 sites in total (11 + 2). The staged red, the
  `<pass>~1` adopter against the pass rows, reported row 178 stale and the old key unpinned. The
  two roles sites carried equal keys before and after.
