# Acceptance ledger — TOOL-dRetiredFork-12

**Serves:** journal TOOL-dRetiredFork-12

Tier-2 · node d · 2026-09-03

`playbook.fixture.md` shipped as `engine` with this kit's own directory spelled five times, so
`check-playbook.sh` exited 1 at any other prefix. It is now rendered from
`playbook.fixture.template.md` through the kit's existing render channel, carrying one token.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-12

- AC1 — MET, with one stated difference — `diff` against the `b0108f13` bytes reports exactly one
  added line, the `gov:kit unattended@1.17` marker that `check-kit-versions.sh` REQUIRES of every
  shipped file and that did not exist on this file at that sha. Discounting that line the render is
  byte-identical, which is the regression proof S3 asked for
- AC2 — MET — in a fixture installed at `scripts/unattended`, `bash check-playbook.sh` exits 0 and
  reports `pieces 2 · verified 2 · unrecorded 0` with zero orphan records. Before this unit the same
  tree exited 1 with `unrecorded 2`
- AC3 — MET — a `{{BOGUS_TOKEN}}` staged into the template makes the adopter refuse with
  `refusing to write`, and the previously rendered file is left untouched: the bad render never
  lands. Observed, then reverted
- AC4 — MET — `bash tools/check-install-prefix.sh` reports the fixture at 0 and asked for its
  ratchet row to be deleted. The reason is structural rather than lucky: the carried arm grades the
  SOURCE paths the descriptors resolve, and the source is now the tokenised template
- AC5 — MET — `bash tools/check-kit-versions.sh` exits 0 after the 1.16 to 1.17 bump across eleven
  carriers. It first RED-ed on the new template carrying no marker, which is how the marker in AC1
  came to exist
- AC6 — the parity assertion lives in `adopt-unattended.sh --check`, which is a bar leg, so a
  drifted fixture reds on every push rather than in a kit self-test no boundary runs. The
  no-re-pull-before-`DEPL-dRetiredFork-3` observation is recorded in that unit's AC4 per rev-4

## What the spec could not have known

**The fixture RECORDS carry the prefix in their filenames AND their bodies.** Each is named for the
piece it describes with `/` written as `~`. Rendering the fixture alone left both records describing
pieces that do not exist, which `check-playbook.sh` reports as orphan records — coverage nobody has.
The adopter now repaths both halves, recovering the old prefix from each record's own name rather
than assuming it. This is what inCMS's two `engine`-declared fixture-record forks actually were.

**A template is not a playbook, and the gate only knew that about one filename.** It excluded
`PLAYBOOK-TEMPLATE.*` by name, with a comment explaining that a template's values are a specimen.
The moment a second template existed the gate scanned it, found `{{KIT_DIR}}` in a leg target, and
redded check 6 — **in gov's own tree**, not only at a foreign prefix. The exclusion is widened to any
`*.template.md`, which is the general form of the reason the narrow one already gave.

## An instrument error, corrected mid-unit

`bash gate.sh | tail -2; echo "rc=$?"` reports `tail`'s status, not the gate's. It read `rc=0` over
`check-playbook.sh` while that gate was exiting 1, and the wrong reading survived one full step
before a direct run contradicted it. Redirect to a file and test `$?` on the command itself.

This is the fourth instrument error of this build and the second of this kind. The pattern is
consistent: every one of them read in the reassuring direction.

## What the parity arm does NOT catch, stated rather than assumed

`--check` re-renders the fixture with the same `render()` the writer used and diffs the result
against the installed file. That detects a hand-edited or stale artifact, which is its job. It does
**not** detect a wrong renderer: both sides of the comparison come from the same implementation, so
a defect in `render()` produces two identical wrong answers and a green row.

Render correctness is established elsewhere and deliberately: AC1 compares the output against bytes
committed before this unit existed, and the unresolved-token refusal fires on the class of render
defect that would otherwise ship silently. Saying which check covers which failure is cheaper than
discovering later that neither did.

The same limitation already applied to the Skill's parity check, which this one is modelled on. It
is inherited, not introduced — and now written down.
