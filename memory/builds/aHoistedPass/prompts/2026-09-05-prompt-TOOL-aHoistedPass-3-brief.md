# Brief — TOOL-aHoistedPass-3

**Provenance.** The mandate's roster named
`memory/builds/aHoistedPass/prompts/brief-TOOL-aHoistedPass-3.md` and no file existed at it, for any
of the ten units; that name is also unwritable under hygiene check 5, which derives the record kind
from the `prompts/` subfolder. Derived by the building run from the roster line and the spec.

## What this unit is

`memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-3.md`, **rev-4**, Tier-2, order 2,
parallel with `DEPL-aHoistedPass-1`. Read it whole — twelve scope items and sixteen criteria.

`BUILD-METHOD.template.md` declares its own budget in prose and no checker reads the figure. The unit
raises the byte half to an exact integer, declares it where the existing size gate already looks, and
adds the one term that stops the number drifting between the document and the declaration.

## The shape that matters

**No new program.** The seam is `tools/check-template-size.sh`'s subject resolution, and extending it
is one `gate-legs.json` row naming the subject, one row in `template-size-limits.txt` giving the
ceiling with its reason, and one `--bump` to seed the high-water row. A sibling script would duplicate
subject resolution, ceiling resolution, CR-normalized measurement and the ratchet.

**The subject is the RENDER**, `memory/guides/BUILD-METHOD.md`, because the budget prices the render's
re-read cost and M7 re-reads the render.

**The PAIR TERM is the only new code**, and it needs TWO guards: `[ -n "$declared" ]` keeps an
undeclared subject off the hard default, and `[ -n "$bline" ]` keeps the three existing subjects out.
An unparseable budget line reds through the same branch, which is the whole point — a file must not be
able to move its prose and pass.

## What the run must not do here

Do not gate the LINE axis; do not add a second subject; do not write a new file under `tools/`; do not
make the high-water ratchet binding; do not write the M6 anchors or the route sentence, which are
`TOOL-aHoistedPass-2` at order 3 — this unit only funds them.

## What nothing will catch for you

Section 7 names three: `harness arms` does not force S10, because `ARMS_FLOORS` is one-sided upward;
`kit version markers` grades presence and agreement and reads no diff, so it has no opinion about
S12's bump; and `check-verdict-epoch.sh`'s scan set excludes templates. AC7, AC15 and AC16 are the
observations that replace those absent catchers.

## The acts this pass owes the record

`--dispatch` with the write set, `--brief` with this file, one commit carrying the unit id, then
`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`. The three staged breaks of section 6
are observed in scratch copies before the leg row lands.
