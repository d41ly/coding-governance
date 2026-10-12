# Re-dispatch brief — TOOL-aBriskPreflight-1, after its first pass was killed

**Serves:** research TOOL-aBriskPreflight-1

The first pass of this unit (workflow `wf_1fb612af-e48`, dispatched 2026-10-11T03:40Z) was killed by
the platform's session limit after 70 tool calls, before it verified or committed anything. Nothing
of it is committed. It is not resumed: a resumed agent replays a cached refusal. Its work is on disk:

- `tools/check-wiring.sh` modified, uncommitted: the eol population through one
  `git check-attr --stdin`, the smoke's per-id `grep -c` replaced by one `awk`, the two audit-line
  `sed | tail` reads replaced by one tagged `sed`, and the family harvest run as one `sed` per chunk
  of paths kept under 8000 characters.
- `tools/check-wiring.test.sh` modified, uncommitted (16 lines added).
- Seven untracked slice scripts under `tools/`: `cw-slice-base.sh`, `cw-slice-ac9.sh`,
  `cw-slice-ac10.sh`, `cw-slice-brk-awk.sh`, `cw-slice-brk-eol.sh`, `cw-slice-brk-harvest.sh`,
  `cw-slice-brk-tags.sh`. What each established is unknown: re-run what you rely on.

**Your pass**: read the build brief (`2026-10-11-prompt-TOOL-aBriskPreflight-1-build-brief.md`) and
the spec whole, then REVIEW those edits against the spec as if a stranger wrote them — keep what is
right, fix what is not, finish what is missing — then verify every acceptance criterion the spec
names, delete every slice script before `gen_map.py --write`, and commit. The build brief's rules all
still bind.

**The "before" spawn count is already measured** and need not be re-taken: `check-wiring.sh --check`
at BASE, traced with this build's instrument, 568 s, **355 forks and 387 execs** (run
`cw-base-traced`, in `build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md` and its runs log).
Trace the "after" once, the same way, from this tree; record the host's spawn cost beside it.
