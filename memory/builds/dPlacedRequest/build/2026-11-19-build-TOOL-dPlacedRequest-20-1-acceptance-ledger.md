# TOOL-dPlacedRequest-20 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-20

The unit was built from its spec at rev-6 on base `cfc890886`. `--lease offer <kind> <name> [<sub>] (PINNED)
--to <fleet tag>[/<session>]` is a new act of `tools/unattended/unattended.sh#run_lease_verb`: before
any read it holds the session half to `tools/unattended/unattended.sh#check_lease_segment`, refuses an
empty or `absent` one, and asks `tools/unattended/unattended.sh#check_fleet_tag` whether the playbook
kit's one registry reader, `tools/playbook/render_playbook.py#read_fleet`, holds the tag. It reads
`leases.offer-seconds` through `tools/unattended/unattended.sh#read_lease_bound` and writes through
`tools/unattended/unattended.sh#write_lease_offer`, which hands `offer` and `offer-deadline` to
`tools/unattended/unattended.sh#write_claim` as `WL_OFFER` and `WL_ODL` (every other write still writes
`-`), keeping the read epoch over a `released` record and creating at epoch one over an absent lease.
`tools/unattended/unattended.sh#check_claim_writable` gains the `offered` class, tested first in the
`lease` mode through `tools/unattended/unattended.sh#check_deadline_passed`, its `lease:offered` cell,
and the offer act's own decision: none creates, `released` writes, terminal refuses `terminal`, the
rest `live-holder`. `CLAIM_READS` names `offered`. Section seven of `tools/unattended/STOPS.template.md` (PINNED)
gains the `offered` row and the offer paragraph, the `--lease` bullet of
`tools/unattended/VERBS.template.md` the act and its session form, both rendered byte-identical into
`memory/guides/`, and `help/loop.md` the act, its two causes and the refreshed usage fingerprint
`b121c595`, the one `tools/govkit/docs_leg.py#read_fingerprint_rows` printed for the moved usage line. (DERIVED)

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the
run's scratch directory over a fixture under the node's short temp path: a bare origin, clone A
(`USERNAME=daily-agent`, tag `a`) built with the suite's own `mkconf` read out of
`tools/unattended/unattended.test.sh` by `awk`, `RUN_CLAIMS=on`, and clone B of the same origin
(`USERNAME=agent5`, tag `b`); the registry is the kit's own `fleet.toml`, whose rows hold both tags.

**Evidences:** TOOL-dPlacedRequest-20
- AC2 — `--lease offer unit fx u1 --to zz` printed `lease not written — --to zz: 'zz' is no tag of
  fleet.toml`, exit 2; after it and the three AC9 refusals the origin held 0 refs under `refs/gov` (DERIVED)
  and clone A had no `gov-last-fetch`, so no read ran.
- AC1 — the offer of the absent `fx/unit/u1` to `b` printed `lease — fx/unit/u1 · offer b · epoch 1`; (DERIVED)
  the record read `status: released`, `offer: b`, `offer-deadline: 300`, `epoch: 1`, no parent. Over (DERIVED)
  clone B's live lease the same act printed `lease refused — live-holder · fx/unit/u1 · …`, exit 1,
  the tip unmoved; over a `withdrawn` one, `lease refused — terminal`, the tip unmoved. A re-offer of
  the offered lease kept epoch 1, parented on the first offer. (DERIVED)
- AC3 — clone A's `--lease acquire unit fx u1` inside the window printed
  `lease refused — offered · fx/unit/u1 · b`, exit 1, the tip unmoved; `take-over` the same; a build (DERIVED)
  lease offered to `b` refused A's acquire the same way. `CLAIM_READS` names `offered`.
- AC4 — clone B's acquire printed `lease — fx/unit/u1 · take · epoch 2`; the record read `status: (DERIVED)
  live`, `offer: -`, `offer-deadline: -`, `fleet-tag: b`.
- AC5 — with clone A's feed line for the offer tip restamped 301 seconds old, A's acquire of (DERIVED)
  `fx/unit/u3` printed `lease — fx/unit/u3 · take · epoch 2`, `offer: -`. With `GOVFEED_DIR` naming (DERIVED)
  a regular file, so the feed could hold no sighting, A's acquire of `fx/unit/u4` printed
  `lease refused — offered · fx/unit/u4 · b`, the tip unmoved. An `offer-deadline` replanted as
  `30x` read as expired: A took `fx/unit/u5` at epoch 2. (DERIVED)
- AC6 — `fx/unit/u2` offered to `b`, A's sighting restamped past the window, B took it at epoch 2; (DERIVED)
  A's acquire under a `git` shim first on PATH answering every fetch with nothing, so its read stayed
  on the epoch-1 tip, printed `lease refused — epoch-fence · fx/unit/u2 · lost the race on the (DERIVED)
  lease: [rejected] (stale info)`; the origin named `b` at epoch 2, and its log's `epoch:` values, (DERIVED)
  oldest first, read `1 2`. (DERIVED)
- AC7 — `python tools/policy/policy.py get leases.offer-seconds` printed `300` in this tree, and the (DERIVED)
  offer wrote `offer-deadline: 300`, read through `read_lease_bound offer`. (DERIVED)
- AC8 — `grep -n "offered"` over the stops template found the `offered` table row and the paragraph;
  `grep -n "lease offer"` and `grep -nF -- "--to <fleet tag>/<session>"` over the verbs template each
  found the `--lease` bullet.
- AC9 — `--to 'b/s 1'`, `--to b/absent` and `--to b/` each exited 2 before any read. The offer to (DERIVED)
  `b/s1` wrote `offer: b/s1`; clone B under `s2`, under `absent`, and with `CLAUDE_CODE_SESSION_ID`
  unset each printed `lease refused — offered · fx/unit/u6 · b/s1`, the tip unmoved; under `s1` it
  printed `lease — fx/unit/u6 · take · epoch 2` with `offer: -`. (DERIVED)
- `bash -n` read both changed shell files clean. Four names were checked with the naming lexicon
  before they were written: `write_lease_offer` and `check_fleet_tag` in the driver, `run_offer_arm`
  and `read_offer_tip` in the suite.

**Owed at the close.** The new arm in `tools/unattended/unattended.test.sh`, the region-eight offer
block and the `offered` row of the claim cell table, runs and is observed RED-first against the base
driver, which has no offer act, by the main loop after every unit is terminal. The suite is waived
for this build's landing by README rule eight.
