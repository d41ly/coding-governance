# The report-switch step at dTrueNorth's landing, and the re-pin guard it needed

**Serves:** research PLAY-dClosedLoop-1

The two `memory/DECISIONS.md` rows `PLAY-dClosedLoop-27` and `PLAY-dClosedLoop-28`, minted under dClosedLoop's slug
in the owner-asked landing that carries the report-switch step of
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` (`[phase-1]`, the retirement table's first two rows;
`[owner]`, the row for dTrueNorth's landing). A row is capped at 300 characters (`memory/HYGIENE.md`, check 7), so
this record carries each in full, with the observations that proved it.

## [row-1]

**PLAY-dClosedLoop-27 — packet.py's re-pin guard derives an in-place landing's LANDED.**
- Source: the owner, 2026-10-22, relayed verbatim by the dTrueNorth session: "option 2, fix the guard first". The
  option read: "an owner-asked dClosedLoop landing so packet.py reads LANDED the way --landed does, then the re-pin."
- Cause, filed as `PLAY-dClosedLoop-26`: dTrueNorth landed in place, where `unattended.sh --landed` only observes,
  printing "phase LANDED (derived: 622a4a9a on refs/heads/main at dbb735b2) · observed, not written". Its `RUN.md`
  stays at LANDING on the default branch by design, and `packet.py --repin` refused it as a live chain run.
- The guard now reads a LANDING record as terminal when it is committed as it stands and the commit that last wrote
  it is an ancestor of the default branch the first remote advertises: `read_derived_phase` (`unattended.sh:1440`)
  over `read_landing_commit` (`lib-unattended.sh:1688`). It is stricter in one place: any working-tree change refuses,
  where the driver admits a lease-only diff.
- Seen: before the fix, `--repin deviations.py` refused with "memory/builds/dTrueNorth/RUN.md (phase LANDING)";
  after it, the guard derives "derived LANDED: 622a4a9a on refs/heads/main at dbb735b2", and the re-pin ran. Plants
  over a scratch clone of a scratch remote: `run-pushed` not refused; `run-unpushed` refused, its landing commit not
  on the tip; `run-dirty` refused, the record not committed as it stands; `run-live` still refused at BUILDING.

## [row-2]

**PLAY-dClosedLoop-28 — the departures report reads the product, and every chain packet is re-pinned.**
- Source: the owner's ask for this landing (row 1's quote), which the plan's report-switch step requires, recorded
  as a decision row. It disposes `PLAY-dClosedLoop-25`, the ask dTrueNorth's landing owed, and `PLAY-dClosedLoop-24`.
- `deviations.py --report` runs `tools/memory-tree/asbuilt_view.py --check` (`cl-dClosedLoop-0006`) where it ran
  `asbuilt.py --check`, and embeds the build README's `build-coverage` region (`cl-dClosedLoop-0003`) where it ran
  `carries.py --report <slug>`. Its population, join, entries, validating arm and byte compare are unchanged, and
  its head still names all four instrument blobs.
- `packet.py --repin deviations.py` and `--repin packet.py` moved those two pins in all 22 chain packets, every other
  pin kept (P0.3). The packets keep `asbuilt.py`'s and `carries.py`'s pins; field 11 still runs `carries.py --report`,
  which stays in service until dIndexedDesign.
- Seen: every report plant and control of `deviations.py --report --fixture`, 53 runs, gives the verdict it gave
  with the previous instrument at `3e236a8ee`. `deviations.py --report dTrueNorth` reads 355 entries and a
  validating arm with 0 findings. dTrueNorth's written report is not re-rendered: it is that run's landed record,
  and its byte compare already differed at `dbb735b29`, where the landing had moved the §8 marks it cites one line.
