# TOOL-dPlacedRequest-1 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-1

The unit was built from its spec at rev-9 on base `a250e173d`. Each criterion below was observed by a
probe of this unit's own code: the driver `tools/unattended/unattended.sh` run as a process in scratch
fixtures under the node's short temp path, each a bare origin with its HEAD set and clones holding the
suite's conf keys under `RUN_CLAIMS="on"` and `USERNAME=daily-agent`, policy values planted as the
landed revision (committed, pushed, fetched); the driver sourced and `load_driver_conf` run for the
driver's own claim write and the direct witness probe; and the named readers over the tree. No gate,
suite or bar ran in this pass; the arms the spec's §7 declares and their RED-first observations are
owed at the close.

**Evidences:** TOOL-dPlacedRequest-1
- AC1 — `--lease acquire build tFix`, `--lease acquire unit tFix TOOL-tFix-2` and
  `--lease acquire run maintain 2026-10` each exited 0, and the origin held `refs/gov/leases/tFix/build`,
  `refs/gov/leases/tFix/unit/TOOL-tFix-2` and `refs/gov/leases/run/maintain/2026-10`, each message
  opening `gov-claim <tail>` with epoch 1, its kind and `fleet-tag: a` (DERIVED).
  `--lease acquire build 'a b'` printed `lease not written — 'a b' is not a legal one-segment ref name`
  and exited 2 (DERIVED);
  every ref is built by `tools/unattended/unattended.sh#derive_lease_ref`.
- AC2 — over a planted stale lease of tag `b`, `--lease take-over build tSt` by session s2 exited 0 at
  epoch 2, its parent the planted tip (DERIVED); `--lease acquire build tSt` by s3 under `agent5`
  printed `lease refused — live-holder · tSt/build · node a · session s2 …` and exited 1 (DERIVED).
- AC3 — with only a legacy `refs/gov/runs/tMig`, `--claims` printed one row of 5 fields (DERIVED);
  after the next write the lease read epoch 1 parented on the legacy tip, the legacy ref unchanged, and
  `--claims` printed 1 `tMig` row (DERIVED). The driver's own write, sourced
  (`tools/unattended/unattended.sh#write_claim` after `check_claim_writable` read the legacy row
  `mine`), created `refs/gov/leases/tDrv/build` at epoch 1 on the legacy tip, and its next write kept
  epoch 1 parented on that lease (DERIVED).
- AC4 — under the default `progress` a renewal with no witness wrote `renews: no`; a witness whose
  `Gov-Transition` trailer names `build=tFix` wrote `renews: yes` and that witness; the same witness
  again `renews: no`; its 7-character prefix `renews: no` with the full sha stored (DERIVED); a commit
  with no transition exited 2 (DERIVED). Under `transitions.record = ["log"]` a witness adding
  `tFix`'s `-transition-1.md` record wrote `renews: yes` (DERIVED). Under `leases.renewal` planted
  `activity`, `fixed` and `none` a renewal with no witness wrote `yes`, `no` and `-`.
- AC5 — under `leases.granularity = "build"` a unit acquisition exited 2 naming `leases.granularity`;
  under `"unit"` a build acquisition exited 2 naming it; under the default a unit lease was written
  (DERIVED).
- AC6 — with branch `other` declaring `tools/zkit/a.sh` and this build's spec `tools/zkit/b.sh`, the
  acquisition printed `origin/other … 1 shared: tools/zkit/a.sh (declared)` under the default
  `kit-dirs` and `no shared path` under `files` (DERIVED); under `leases = "refuse"` it printed
  `lease refused — overlap` and exited 1 (DERIVED); with the path made equal under `builds` it printed one
  finding, `origin/other … shares a path with this run`, and branch `two`, touching only
  `memory/builds/tTwo/`, drew no finding (DERIVED). The reduction is
  `tools/unattended/unattended.sh#check_cross_run_overlap`.
- AC7 — with the origin renamed away an acquisition printed `lease — tOff/build · queued · epoch 1`,
  exited 0, `gov-queue.log` held 1 line and `git for-each-ref refs/gov/leases` listed 0 refs
  (DERIVED); restored, `--lease flush` printed `flushed`, the origin held the ref and the queue held 0
  lines (DERIVED). A queued renewal beaten by a conflicting write printed `yield … (stale info)` and
  left the conflicting tip. Under `refuse` an offline acquisition and renewal each exited 1 printing
  `offline`; under `follow-leases` the acquisition exited 1 and the held lease's renewal printed
  `lease — tFix/build · follow-leases · epoch 1` (DERIVED).
- AC8 — `USERNAME=nobody-here` exited 2 printing that no row of `fleet.toml` names the user, and the
  origin was unchanged (DERIVED); under `daily-agent` `--claims` printed `a` in field 2.
  `tools/playbook/render_playbook.py#read_fleet_tag` answers `a` for `daily-agent` and refuses
  `nobody`, exit 1, naming `fleet.toml` (DERIVED).
- AC9 — `--lease acquire build tNew` in a second clone, whose fetch of the lease namespace a shim
  answered with nothing, after the first clone created it, printed
  `lease refused — epoch-fence · tNew/build · lost the race on the lease: [rejected] (stale info)`,
  exit 1 (DERIVED). The verb's ten argument refusals each exit 2 printing their own line, observed over
  the same clone and armed in the suite's lease block (DERIVED).
- AC10 — `grep -n` over `tools/unattended/STOPS.template.md` found `refs/gov/leases/<slug>/build`,
  `--lease`, `leases.renewal` and `epoch-fence` inside section 7, and AC1's `--claims` rows held 5
  TAB fields (DERIVED).
- AC11 — with exported stubs of `read_mailbox`, printing one `question` row to `tFix` in state `open`
  at commit `Q`, and `check_mail_deadline`, two renewals with `--witness Q` each wrote `renews: yes`
  and `witness: Q`; with the row `expired` the renewal exited 0 with `renews: no` and the prior
  witness; a 40-hex sha the clone lacks exited 2; with no stub the renewal exited 2 (DERIVED).
- AC12 — with the stub printing `open` on its first call and `expired` after,
  `tools/unattended/unattended.sh#check_lease_witness` in the sourced driver printed `question` and
  returned 0, and the renewal after it exited 0 with `renews: no` (DERIVED).
- AC13 — the four `grep -c` reads printed 1, 1, 2 and 1, and the skill render measures 11094 bytes (DERIVED)
  CR-stripped against its row 11094 (DERIVED).
- AC14 — with `refs/remotes/origin/HEAD` deleted under `leases = "refuse"` the acquisition printed
  `lease refused — overlap · tF4/build · overlap probe UNAVAILABLE — …` and exited 1, writing no lease;
  under `warn` it printed the UNAVAILABLE line and exited 0 (DERIVED).
- AC15 — a legacy `tOld` of node `n1` and the lease `tFix` of tag `a` printed field 2 `n1` and `a`,
  5 fields each (DERIVED).
- AC16 — `check_policy.scan_reader_keys` printed `leases`, `leases.granularity`, `leases.offline`,
  `leases.overlap` and `leases.renewal`, and the `read_lease_policy` cut holds 5 literal `get leases`
  lines, one per arm (DERIVED).
- AC17 — over a `.governance/policy.toml` whose first revision does not parse, the acquisition printed
  `lease not written — leases refused: policy: refused …` and exited 2, the origin unchanged; with the policy kit
  absent beside a copy of the driver in a checkout of its own, it printed one NOTE naming the five
  keys and wrote at the default (DERIVED).
- AC18 — `--claims --with-key` printed 6 fields per row; `tFix`'s key equalled `claims.py key` over
  `refs/gov/leases/tFix/build@<sha>` and differed from the one over `refs/gov/runs/tFix@<sha>`, and
  `tOld`'s equalled the one over `refs/gov/runs/tOld@<sha>` (DERIVED).
- AC19 — `comm -3` of `CLAIM_READS` by `CLAIM_MODES` against the cells `GC_CELLS` types printed
  nothing, `CLAIM_MODES` names `lease` and 8 `lease` cells are typed (DERIVED); the static join of the
  kit gate's check 52, its awk run over the driver alone, printed no hit.

## Owed at the close

- The three `New arm:` lines of the spec's §7, each RED-first: `tools/unattended/unattended.test.sh`
  (the lease block in region eight, the 8 `lease` cells of `GC_CELLS`, the `--lease` parity row;
  floors raised by their count, waived by README rule 8), `tools/playbook/render_playbook.py` (the
  `--fleet-tag` selftest arm) and `skills/session-kickoff/manifest-check.test.sh` (the `DPR1 AC15`
  and `DPR1 AC18` arms). (DERIVED)
- The legs §7 names, run once by the main loop; `govkit selfcheck --write` rewrote no subject pin in
  this pass.
