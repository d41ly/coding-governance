# KICK-dKeptSession-24 — acceptance ledger

**Serves:** journal KICK-dKeptSession-24

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `88070c29`
over the working tree before the commit: by a scratch probe script of this pass's own (a bare remote
and two clones c1 and c2 under the short temp path, c1's conf this tree's with `RUN_CLAIMS` on, each
post and read made through the driver's `--mail` verb under `USERNAME` daily-agent, so fleet tag `a`,
each judgment in a subshell that sources the driver and runs `load_driver_conf`), by direct CLI runs
of `tools/loop/loop_transition.py --fixture --plant <case>`, and by the greps and `cmp` AC6 and AC8
state.

Before the first edit the spec's cited code was probed at the base. `write_mail_post` took nine
arguments, the interface file ninth; `read_mailbox` printed fourteen columns, `content-key` last
(DERIVED, read at `88070c29`); `read_lease_policy` held eight keys and no `flow.wait-ceiling` arm;
`read_lease_bound` held the fraction arithmetic inline; `check_lease_witness` probed `declare -F
read_mailbox` and `declare -F check_mail_deadline`; `MAIL_DISPOSED_STATES` in
`tools/loop/loop_transition.py#MAIL_DISPOSED_STATES` already held `expired`; `python
tools/policy/policy.py get flow.wait-ceiling` printed `72` (DERIVED, that run); the floors read 4108
and 1325 (DERIVED, the last assignment of each at `88070c29`), units 23 and 27 having raised them
first as the spec's Files touched anticipates; `len(PLANTS)` read 18 (DERIVED, imported at
`88070c29`); and the `help/loop.md` `--mail` anchor read `4a30e33b` (PINNED, `docs_leg.py
--fingerprints` at `88070c29`). No arm of any suite greps a refusal or NOTE text the pass rewords.

One claim of §4's Evidence does not hold, and the design does not depend on it: the sightings walk
(`tools/lib/gov-feed.sh#derive_feed_events`) records the first commit NOT authored `gov-claim` and
then stops, so a fixture's message committed by `fx` is sighted at the driver's read too, not only by
a planted line. The `mail-expired` plant holds regardless, since its planted line is written before
the read and `read_first_seen` ages the first line of a ref and commit; the plant's comment says so.
The suite's AC4 unsighted row is staged where no walk runs, a plain fetch into c1's cache and a read
with the remote renamed away.

## Criteria

**Evidences:** KICK-dKeptSession-24
- AC1 — `deadline: 30` — under `[flow]` `wait-ceiling = 30` (PINNED, the fixture's literal) landed by commit, push and fetch, c1's `question` posted with `--default no` recorded `deadline: 30` and `default: no` after `content-key`; the same post with no `--default` exited `2` printing `mail — not written · a question declares its default with --default`, the remote's ref count unmoved; a `confirm-request` with none printed the same line naming it; a `--default` holding a tab printed `mail — not written · the default carries a control byte`, exit `2`; a `landed` post and a `--mail ack` of a planted question each recorded `default: ack`; with the file landed as `preset = "strict"` alone `get` printed `168` in c1 and the next post recorded `deadline: 168` (DERIVED, the probe and that `get`).
- AC2 — `expired` — c2's question to `build:tFix`, `deadline: 30`, its line planted in c1's feed 31 hours back (PINNED, the fixture's literal), read in c1's `--mail read tFix` as `expired` with column 15 `30` and column 16 `no`, sixteen columns, and `--open --ids` printed `none`; a second question planted an hour back read `open` and `--ids` printed its id alone (DERIVED, the probe). `loop_transition.py --fixture --plant mail-expired` printed `recorded · planning -> designing`, the fixture's `record` exit `0`, `commits 1 · 2 file(s) · 1 mailbox-message record(s)`, the trailer carrying `disposed=a1b2c3d4e5f6` and the record read with exit `0`, `Serves mailbox-message TOOL-tFix-1 · State expired`; `--plant mail-open` over the same question with no deadline exited `1` with commits unchanged (DERIVED, those runs).
- AC3 — the sender's stamp — c2's question committed under a committer date 25 hours back (PINNED, the fixture's literal), `deadline: 24`, its line planted in c1's feed a minute back, read `open 24` in c1; a scratch copy of the driver whose `check_mail_deadline` ages `now - %ct` read the same row `expired` (DERIVED, the probe).
- AC4 — `check_mail_deadline` — sourced in c1 over one ref's planted lines at 7200, 60 and 5000 seconds back (PINNED, the fixture's literals), it returned `0 1 2 2 0 1 0 1` for 7200 s, 60 s, an unsighted sha and `x` over 1 hour, then 7200 s and 5000 s over 1.5 hours, then the `refs/gov/remote/` spelling over 7200 s and 60 s; `derive_bound_seconds` printed `5400` for `1.5` and `4444` for `1.2345678` over 3600 and returned 1 for `x` and for an empty number (DERIVED, the probe). A message under `deadline: 0` cached by a plain fetch and read with the remote away read `open`, its first-seen `-` (DERIVED, the probe). `check_lease_witness` over the expired question printed `question-closed`, exit `1` (DERIVED, the probe).
- AC5 — no policy kit — a scratch copy of the driver in a repository of its own, the loop and playbook kits copied beside it and no policy kit, posted a `landed` message recording `deadline: 72` and printed one `unattended: NOTE - no policy kit resolves beside this kit` line naming `flow.wait-ceiling` among its keys and reading `'72'` (DERIVED, the probe); over a fresh fixture whose one policy revision ends in an unparsable line, the post exited `2` printing `mail — not written · policy: refused`, the policy kit's refusal naming the file's third line and that no valid revision precedes it, and the remote gained no ref (DERIVED, the probe).
- AC6 — the texts — `grep -n -- '--default\|deadline\|expired\|first saw'` over `tools/unattended/VERBS.template.md` found each in the `--mail` entry, and `cmp` found `memory/guides/UNATTENDED-VERBS.md` equal; `grep -n -- '--default' help/loop.md` found the `--mail` paragraph, `grep -n 'deadline' help/loop.md` the guard paragraph, `grep -n 'mail-expired'` each plant list of `help/loop.md` and `tools/loop/README.md`; `docs_leg.py --fingerprints` printed `verb:unattended.sh:--mail` at `9ed486eb`, the fingerprint the paragraph's anchor now carries, and no other fingerprint moved (DERIVED, those probes).
- AC7 — the probe deleted — `grep -c 'declare -F check_mail_deadline' tools/unattended/unattended.sh` printed `0` and `grep -c "functions absent" tools/unattended/unattended.test.sh` printed `0` (DERIVED, those greps).
- AC8 — the guard's words — `--plant mail-open`'s `refused —` line ended "until it is answered, acknowledged or past its deadline"; folded by `tr -s ' \n' '  '`, `grep -c 'answered, acknowledged or past its deadline'` printed `1` over each of `help/orientation-card.md` and `tools/loop/claim.py`, and `grep -c -E 'answered (or|nor) acknowledged'` printed `0` over the six files folded together (DERIVED, those runs).

Every refusal the pass adds prints a line and `return`s 2 from a function, and no added line carries
`exit 1`, `status=1` or a `fail` call, so the census at the driver's ceiling (PINNED,
`.memory-tree.conf#REFUSAL_CEILINGS`, 347) does not move; it is read at the close. The new arm in
`tools/unattended/unattended.test.sh` counts 13 region-eight `same` (DERIVED, the block's own lines)
less DPR1 AC11's retired one, raising `FLOOR_ASSERTIONS` to 4120 and `FLOOR_SHARD_8` to 1337
(DERIVED, base plus 12), each with its `RAISED` line; it reuses `read_mail_refs`, given the bare
remote as an optional argument. The `loop transition record` row's `plants=` token reads 19
(DERIVED, `len(PLANTS)`), its reading re-priced by `mail-expired` run alone by direct CLI, 2.8 s
(PINNED, that run on node d). Both arms' RED-first observations are the close's. `python
tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders over a pin of 1421
(DERIVED, that run), the count unit 27's ledger read at its base, and `--offenders` names none of
`check_mail_deadline`, `derive_bound_seconds`, `run_deadline_arm` or `read_deadline_keys`.
`gen_map.py --write` added those four rows to `memory/map/generated/symbols.json` and moved nothing
else.
