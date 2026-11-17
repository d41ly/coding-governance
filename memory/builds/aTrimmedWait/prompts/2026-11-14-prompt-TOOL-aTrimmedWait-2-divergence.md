# Revision — TOOL-aTrimmedWait-2: the §4 probe's planted sibling contradicts S2

**Serves:** research TOOL-aTrimmedWait-2

## The prompt

The unit harness's builder (run `wf_142cf922-be4`) returned `diverged: true` before committing any code, with this `why`, quoted whole below as the Goal; `<P>` stands for the `TOOL-aCarriedStop` prefix, so the record cites no id that does not exist.

## The brief

### Goal
DIVERGENCE: §6 AC1 and AC2 (and the §4 probe they quote) contradict §2 S2. I built S2 as written: untracked specs are in the selection, and an edge finding is reported when either end is graded. Run over that build, the probe prints `spec-c rc 1 A 0 B 0 C 1 N 1 same yes live 1`, `spec-n rc 1 A 0 B 0 C 0 N 2 same yes live 1` and `build rc 1 A 1 B 0 C 1 N 2 same yes live 1`. AC1 and AC2 expect `N 0`, `N 1` and `N 1`. The extra `N` finding is a real edge finding: the probe makes N with `sed "s/$P-3 /$P-98 /; ..." "$K"`, so N keeps K's `**consumes-from** \`TOOL-aCarriedStop-2\`` edge. Spec -2 declares `hands-off` only to -3, never to -98, so check 12 reports `2026-11-14-spec-<P>-98.md (§3 declares **consumes-from** \`TOOL-aCarriedStop-2\` and that unit declares no matching **hands-off** \`<P>-98\` back)`. That finding appears whenever N or C is graded, which is exactly what S2 says. The full run at the parent never reads N because N is untracked, so the spec's own probe could not have shown it. The spec has to change in one of two ways. (a) The §4 probe plants an N that adds no unmatched edge, for example by also deleting K's `consumes-from` bullet from N or by writing `- none` under N's `### Edges`, so the AC lines stand as written. (b) AC1 and AC2 quote `spec-c ... N 1`, `spec-n ... N 2` and `build ... N 2`, and S2 names the cross-edge from an untracked sibling as an expected finding. Every other probe line matched the spec exactly: full, spec-a, spec-k and all seven refusal lines. I restored every path I changed (`git status` is clean), committed nothing, and removed the fixture at %TEMP%/u2.

### Items
1. Revise TOOL-aTrimmedWait-2 so its §4 probe, §2 S2 and §6 AC1/AC2 agree. The main loop recommends
   option (a): the probe plants an N that adds no unmatched edge (drop K's `consumes-from` bullet
   from N, or write `- none` under N's `### Edges`), so S2 and every AC line stand as written. Take
   (b) only if (a) cannot keep the probe's other lines identical.
2. Bump the rev and add the §9 line naming this record, with the sections it changed.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md` exits 0.
- The §4 probe text and the AC1/AC2 expected lines agree with S2 as revised, by reading them together.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
Copied from the build's brief: check 12's loop and the `--only` parse in `tools/memory-tree/check-memory-hygiene.sh`.
