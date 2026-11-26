**Serves:** journal TOOL-dTotalRecall-64

# Build brief — TOOL-dTotalRecall-64, a spec-amendment unit built by the spec writer

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 64's whole deliverable is an amendment to
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-46.md`; the write gate admits a spec
write from the spec writer alone, so this unit's pass is the writer's edit and the main loop's pass commit.

## The brief

### Goal

Apply `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md` (rev-4, INPROGRESS) to unit 46's
spec exactly as its §4 "The amendments to unit 46" states, so its AC1 and AC2 hold at this pass's tip.

### Items

1. Make every amendment §4 lists in unit 46's spec: S1's quoted text, S2's and S3's wording, §4 "The parser",
   §4 Inventory, Files touched and the first alternative, §5's perf and testing lines, the §7 New arm line
   struck, §10's seam sentence and the §3 consumes-from line to unit 38. Unit 63's AC1 amendment, landed in
   `818591fc2` as unit 46's rev-5, stays exactly as it stands.
2. Bump spec 46's rev by one and add one §9 line of the form §4 gives, naming this unit.
3. Spec 46's status header keeps `DEFERRED`. Unit 38's spec takes no write (unit 64's §4 "Unit 38's spec");
   unit 64's own spec is not yours to edit: the main loop flips it.

Before returning, run unit 64's §6 commands over spec 46, `bash tools/unattended/unattended.sh --check-specs
dTotalRecall TOOL-dTotalRecall-46`, `python tools/check-spec-tokens.py --spec <spec 46>` and
`python tools/playbook/writing_practice.py check pinned-facts`, and fix every finding they name in spec 46. The
write grant is spec 46 alone; do not commit.

### Acceptance

Unit 64's §6 criteria read green over spec 46; the three checks exit 0 or read green.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No change to spec 46 beyond unit 64's §4; unit 46's own re-check follows this pass. No product code.
