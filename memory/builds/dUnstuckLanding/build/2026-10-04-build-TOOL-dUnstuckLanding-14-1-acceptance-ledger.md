# TOOL-dUnstuckLanding-14 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-14

No merge bar and no self-test suite ran in this pass. The criteria were observed through two
hermetic probes assembled from the suites' own setup: the driver suite's prologue, unit 13's bar
seeding helper and this unit's new arms, which build their own repository and bare origin under the
user temp directory; and the leg suite's prologue, its record writers and this unit's new leg arms.
They reported 95 and 12 assertions passing. Two staged breaks made the probes red where they should:
disabling the attended derivation redded fifteen driver assertions, AC1's among them, and disabling
the revert clause of the content predicate redded the AC4 and AC7 arms; the leg probe redded on a
disabled upheld arm and a disabled HELD admission in check 7. The suites themselves are owed to the
close.

**Evidences:** TOOL-dUnstuckLanding-14
- AC1 — `LANDED (attended)` — a hand-off pushed to the fixture origin's default branch read `phase
  LANDED (attended)` to `--status` and `state: terminal`, `verdict: TERMINAL` to `--liveness`;
  `--settle` wrote `phase: LANDED`, `landed-by: attended`, `landed-derived` naming the hand-off
  commit twice and that commit as the witness, staged only the record and left HEAD where it was.
  The leg run with `--skip 28` printed `attended LANDED 1` and no check 15 failure naming the record.
- AC2 — `inherited-red` — a record held under `inherited-red` and pushed the same way read `phase
  HELD` and not `LANDED (attended)`, and `--settle` printed fail 96 ending in the hold code
  `inherited-red`, with the record's blob unchanged.
- AC3 — `RUN.LANDED.` — `--preflight tRun --keepalive-id KA-2` over the landed hand-off, unsettled
  and then settled and committed, printed `preflight OK` with neither check 81 nor 82, and in both
  cases left an index archive under `RUN.LANDED.` carrying `landed-by: attended`, `units-at-landing:
  ARCH-tRun-1` and `landed-derived` naming the hand-off commit.
- AC4 — `work-landed-at:` — over the fixture population the records whose witness is their base,
  whose witness is another build's commit and whose work was reverted on the first-parent line were
  each refused with fail 102 and its own reason, blob unchanged; the kept record gained
  `work-landed-at:` naming its witness and the tip and stayed ABORTED; with its base removed and
  committed it was refused with fail 103 naming the missing base.
- AC5 — `HANDOFF_CUTOFF` — with `HANDOFF_CUTOFF` at 2000-01-01 the kept record was refused with fail
  98 saying it meant discard; blank, fail 97 named the key; the record's blob was unchanged.
- AC6 — `UNBOUND` — the BUILDING record with no lease read `verdict: UNBOUND`; `--settle` wrote
  `work-landed-at` and `abandoned` and kept `phase: BUILDING`; a `--preflight` of tRun then printed
  it EXCLUDED as abandoned and not as a counted run. With a fresh lease the settle printed fail 101
  saying LIVE and wrote nothing.
- AC7 — `abandoned:` — the leg redded check 15 naming `work-landed-at`, the revert and
  `memory/builds/tArevert/RUN.md` for a hand-written fact on reverted work, redded none on the kept
  record's settled bytes, and redded a record carrying `abandoned:` with no `work-landed-at`.
- AC8 — `tip was not observed` — with the fixture origin's URL pointed at a missing path, `--settle`
  printed fail 99 saying the tip was not observed, and the record's blob was unchanged.
- AC9 — `KA-3` — `--resume tRun --keepalive-id KA-3` over the unsettled landed hand-off printed
  nothing to resume naming `--settle tRun`, left the record's blob unchanged and the tree clean.
- AC10 — `--settle tRun` — the `handoff` row's reason ended `&& bash tools/unattended/unattended.sh
  --settle tRun`, the path before it being the suite's own derived kit path and relative, and
  `--handoff` printed the same command as its hint.
- AC11 — `SKILL.template.md` — the Skill template carries one `unattended.sh --settle ` invocation,
  the verb carrier one `--settle` entry, the protocol template one `work-landed-at` and the
  stops template three; STOPS §1 no longer reads the old two-verb terminal sentence.
- AC12 — `adopt-unattended.sh --check` — after the re-copy, `cmp` found each of the three templates
  identical to its render under `memory/guides/`, and `adopt-unattended.sh --check` exited 0.
- AC13 — `check-arms.py --report` — every new branch, fails 94 to 103, the settle's fail 10 and the
  leg's four new check 15 branches, read ARMED; fail 52's moved branch stayed ARMED; the unarmed
  registry is unchanged.
