# TOOL-dHonouredPark-4 — build record

**Serves:** journal TOOL-dHonouredPark-4

Node `d`, 2026-08-25, base `bd0348f3`. `--plan` takes its unit SET and ORDER from the generated units
region. Spec: `../spec/2026-08-25-spec-dHonouredPark-4.md`.

## The verification, and why it is not the arms

**The arms in `tools/unattended/unattended.test.sh` were WRITTEN AND NOT RUN.** A standing owner
instruction of 2026-08-23 forbids running this kit's self-test suites, and no leg on the bar invokes
that file either — the two facts the spec's §7 declares as a skip. They are syntax-checked with
`bash -n` and nothing more. That is a real gap and it is stated here rather than left for a reader to
discover.

**And the gap bit immediately.** The first draft of those arms was written against an `arm` helper
this file does not have — it has `hit`, `miss`, `same` — inside a function nothing ever called. Dead
twice over, and `bash -n` passed it happily. What caught it was `check-arms.py` on the merge bar,
refusing the new `fail 42` branch as unarmed, which forced a read of how the harness actually asserts.
An unrunnable suite is not merely unverified: arms written for it can be wrong in ways only a
different gate notices.

The same read found a STRANDED assertion. S1 replaced the roster summary sentence, and an existing
arm asserted the old text — the `arm-literal-strands-on-message-edit` class the closing checklist
selected for this diff. It is fixed here.

What stands in its place is stronger about BEHAVIOUR and says nothing about the arms.
`bash tools/unattended/unattended.sh --plan <slug>` was captured over **all 63 tracked builds** before
the change and again after, and the two captures diffed:

- The unit **SET is identical on every one of the 63**.
- The **ORDER changed on 11**, which are the builds whose region is not already in id order.
- The roster summary line changed on **5** — the builds whose authored pair names no id of their own.
- Nothing else moved.

That is exactly what the spec predicted its diff would be, measured against the real corpus rather
than a fixture.

## One defect the corpus check caught that a fixture would not have

The first implementation ran `grep -oE` over the whole region to collect ids. A rendered row spells
its id **twice** — once as the link's text and once inside the link's target — so every unit appeared
twice and the listing doubled. A two-unit fixture would have shown four rows and might have been read
as a fixture problem; 63 real builds showed it immediately.

## Acceptance ledger

**Evidences:** TOOL-dHonouredPark-4

- **AC1** — OBSERVED, `--plan dHonouredPark` names `TOOL-dHonouredPark-4` as next, which is the
  region's first non-terminal row and therefore the same unit `--status` reads. At BASE this verb
  named `TOOL-dHonouredPark-1`, by path order.
- **AC2** — OBSERVED, `--plan` captured over 63 builds. On builds carrying no order values the
  region is already in id order, and before and after agree line for line on all 47 unchanged builds.
- **AC3** — OBSERVED, `fail 42`: a README with no units marker at all now refuses with `no units
  marker at all`, naming the file and the repair. At BASE the outer `grep -qF` guard made this case
  fall through silently to the spec-derived listing.
- **AC4** — GREEN AT BASE, `fail 42` on a malformed pair. Already shipped and already armed; kept as
  a regression guard, not offered as coverage this unit adds.
- **AC5** — OBSERVED. `missing_units` still reads the AUTHORED pair, and the MISSING join is
  untouched — the corpus diff shows no MISSING row appearing or disappearing anywhere.
- **AC6** — amended rev-6. NOT OBSERVED and not observable in this build: the state needs a fixture
  in the suite a standing owner instruction forbids running, and it does not occur in the corpus. The
  divergence it pins is documented in S4 and in the protocol, and the arm is written and unexecuted.
  Recorded as amended rather than dressed as met.
- **AC7** — OBSERVED, `--plan` over the five builds carrying such a file still prints `NOT A UNIT (no
  status header)` for each. The corpus diff confirms all five survived the move.
- **AC8** — OBSERVED, `--plan dHonouredPark` rows appear in region order.
- **AC9** — OBSERVED, `corpus_ids.py --report`: 134954 before, 135719 after. The protocol paragraph
  and one decision row; `.memory-tree.conf` carries the movement, 135107 to 135872.
- **AC10** — amended rev-6. NOT OBSERVED, same reason as AC6: zero tracked specs produce a heading
  whose id does not parse, so the condition has no live instance and its fixture is in the unrunnable
  suite.
- **AC11** — OBSERVED, `--plan` over 63 builds. No region row lacks a tracked spec anywhere, which is
  expected while the region is rendered FROM those specs; the branch exists because S1 makes the state
  representable, and it is exercised only by the written arm.
- **AC12** — OBSERVED, `bash tools/unattended/adopt-unattended.sh --check`: `in sync`. Both templates
  were edited and re-rendered; editing either rendered copy directly reds this check.

## Three copies of one sentence, and only one of them editable

`--plan`'s behaviour is described in `tools/unattended/PROTOCOL.template.md`, rendered byte-identical
to `memory/guides/UNATTENDED-PROTOCOL.md`; and in `tools/unattended/SKILL.template.md`, rendered to
`.claude/skills/unattended/SKILL.md`. The adopter refuses on drift in either pair. Both SOURCES were
edited and both renders regenerated — the round-2 review found rev-2 of this spec named only the
rendered guide, which would have redded the very leg §7 lists as green.
