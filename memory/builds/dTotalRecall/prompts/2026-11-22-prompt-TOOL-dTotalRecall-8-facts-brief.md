**Serves:** journal TOOL-dTotalRecall-8

# Brief — dTotalRecall: pin three unpinned facts in units 8 and 1, and set unit 8's leg ceiling by the ceiling rule

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 1's pass legs at `0b3c2b3f9` read `writing practice (records and
units)` red on three unpinned facts in two specs, and unit 1's own leg met a ceiling rule its spec did not know.

## The brief

### Goal

Revise both specs in place, each as a rev bump with one revision-log line naming this brief by its file stem, so
`python tools/playbook/writing_practice.py check pinned-facts` reads neither spec red.

### Items

1. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md` (DEFERRED, rev-4): its facts `60 s` and (PINNED 2026-11-22, deviation 15)
   `941 KB` are unpinned. The `941 KB` measurement is a prototype figure: pin it with what measured it, or cut it if
   nothing on disk records it. The `60 s` is the new leg's declared ceiling, and the (PINNED 2026-11-22, deviation 15)
   `leg ceilings clear their evidenced maximum` leg requires a ceiling to clear the leg's evidenced maximum by
   max(120 s, 1.0x) (DERIVED, that leg's failure line for unit 1's `record-kinds` leg, recorded in
   `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-deviation-15.md`), so a 60 s ceiling can never (PINNED 2026-11-22, deviation 15)
   pass. Restate the ceiling as that rule gives it over the spec's own measured time, PINNED with today's date and the
   rule, in every place the spec states it (S-lines, Design, Gates), and say where the builder records the evidence row
   (`tools/run-gates/ceiling-evidence.txt`).
2. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md` (CLOSED, rev-7): its S3 fact
   `120 seconds` is unpinned and the unit was built at 122 by deviation 15. Pin that one line, citing the deviation (PINNED 2026-11-22, deviation 15)
   record by its file stem, as a rev-8 bump whose revision-log line names this brief and says the change is a
   record-only pin to a CLOSED spec, no criterion moved. Change nothing else in that spec.
3. Keep every other claim of both specs as it stands; this is a facts pass, not a re-ground.

Before returning, run `python tools/playbook/writing_practice.py check pinned-facts`,
`python tools/check-spec-tokens.py --spec <path>` over each spec and
`bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-8`, and fix every finding they name
in these two specs. The status headers keep their statuses; the write grant is the two spec files; do not commit.

### Acceptance

The pinned-facts check names neither spec, and both other commands exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve) · writing practice (records and units)

### Non-goals

No spec but these two. No product code. No change to any criterion of either spec.
