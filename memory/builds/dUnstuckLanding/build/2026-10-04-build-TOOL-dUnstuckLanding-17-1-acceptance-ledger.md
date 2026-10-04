# TOOL-dUnstuckLanding-17 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-17

No merge bar and no self-test suite ran in this pass. Each new arm was run ALONE behind a copy of its
suite's own prologue, on fixture repositories under the user temp directory: the pass-order block
read 13 of 13, the brief-recorded block 11 of 11, and the kit-gate block 28 of 28. Each was then run
again against a staged break of the line it grades. The drift arm ran alone through its selftest
function, 9 of 9. The whole suites and the gate legs are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-17
- AC1 — `read_advertised_head` — a fixture clone at `%TEMP%/ul17a` with a bare origin: the first call
  returned 0 with `ADVH_SHA` equal to the sha `git ls-remote origin HEAD` printed. After a second
  clone pushed and the first fetched the object, a fresh shell returned the new sha. With the remote
  removed it returned 1 with `this clone declares no remote to observe`.
- AC2 — `check-pass-order.sh` — the range arm exited 0 with `range <tip8>..` on the summary line and
  did not name the pushed unit. A second unpushed build-first unit exited 1 naming `ARCH-tRange-3`
  and not `ARCH-tRange-1`. With `^<tip>` staged out of the in-range `build_commit` call, the first
  run exited 1 naming the pushed unit.
- AC3 — `check-brief-recorded.sh` — the range arm exited 0 with `range ` on the summary line. An
  unpushed CLOSED unit with no row exited 1 naming `ARCH-tBR-3` only. With `^<tip>` staged out of
  the in-range call, the first run exited 1 naming the pushed unit.
- AC4 — amended rev-2 — the arm grades two passes of one live record rather than two records. The
  pushed pass with an undeclared write beside a clean unpushed pass printed `check 23 fleet — 1
  undeclared write(s)` and no FAILED. A stray write in the unpushed pass printed FAILED naming
  `ARCH-tRun-2` and not `ARCH-tRun-1`. With the `check_adv_reaches` test staged out, the first run
  printed `check 23 FAILED`.
- AC5 — `range whole` — origin HEAD pointed at `refs/heads/nothing-here` printed `range whole (the
  tip did not resolve: ` and exit 1 naming the pushed unit. With HEAD reset to the tip it printed
  `range whole (HEAD carries nothing the tip <tip8> lacks)`.
- AC6 — `UNDECLARED_WRITE_BUDGET` — the allow-list region, the kit example conf and the protocol
  template each match it. `.unattended.conf` carries it at `"0"`. The retired key's git grep over
  `tools`, `.unattended.conf` and `memory/guides` prints the leg's refusal line and its arm, nothing
  else.
- AC7 — `UNDECLARED_WRITE_CEILING="0"` — appended to the fixture conf, the leg printed the refusal
  naming `UNDECLARED_WRITE_BUDGET`. With the name scan staged out, the arm went red.
- AC8 — `--emit-ceiling` — in this tree it exited 2 in 0.11 s, printing the retirement message that
  names the `check 23 fleet` line.
- AC9 — `fleet_over_budget` — over a clone at `%TEMP%/ul17d` it read `live` false with no run
  record. With `gate-run/fx/0.out` carrying `over aFixture=2` it read value 1, `gateable` false and
  detail `aFixture 2`. With the file deleted it read `live` false again.
- AC9 — amended rev-3 — a fleet line reading `over unjudged` reads `live` false and names it, where
  it read a live 0; section 9's rev-3 line logs it.
- AC10 — `tools/drift-audit/drift_report.py` — `grep -c 'check 23 fleet — '` printed 1 for the leg
  and 2 for the engine.
- AC11 — `impure` — the staged `tools/gate-legs.json` diff adds an `impure` key to `pass-order
  history` and to `brief-recorded` and moves no other entry.
- AC12 — `wc -c memory/guides/UNATTENDED-PROTOCOL.md` — 65426 bytes at the commit against 65640 at
  its parent, and `cmp` against the template exits 0.
- AC13 — `last-audit:` — the manifest's stamp moved in the commit, beside `.unattended.conf` and
  `tools/gate-legs.json`.
