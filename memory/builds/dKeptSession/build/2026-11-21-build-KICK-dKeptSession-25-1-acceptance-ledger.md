# KICK-dKeptSession-25 — acceptance ledger

**Serves:** journal KICK-dKeptSession-25

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands; the role's hook refused `loop_lib.py --check` as the `loop definition`
leg when it was tried. The criteria were observed on win32 at the pass's base `edb4a01e` over the
working tree before the commit: by three scratch probe scripts of this pass's own (a bare remote and two
clones A and B under the short temp path, each conf `RUN_CLAIMS` on, each post, read, ack and answer
made through the driver's `--mail` verb under `GOV_NODE` a or b, each outcome and each claim write in a
subshell that sources the driver and runs `load_driver_conf`), by `python -c` probes importing the loop
kit's `termination.py` and `loop_lib.py` over the parsed `tools/loop/loop.toml`, and by the greps,
`cmp` and `docs_leg.py --fingerprints` AC6 states.

Before the first edit the spec's cited code was probed at the base, units 39, 51, 27, 24 and 10 read as
landed. `write_mail_ack` read columns 1, 6 and 7 and posted with eight arguments; `write_mail_post` took
ten, the default tenth, so the answer's eight-argument call records `default: ack`, as S2 says unit 24
writes; `read_mailbox` printed sixteen columns, `deadline` and `default` last, and its comment named
`check_lease_witness`'s columns 2, 4 and 10 alone; `check_lease_witness` held no `declare -F` probe;
`read_lease_renewal` held the one transition step; the `--beat` line was `renewed <utc>` alone;
`item.entry.claim` was the entry program's last row, its header comment "orient, place by the policy key
`placement`, claim"; `check_wait` read `on-deadline` as an outcome outside `waits`
(`tools/loop/termination.py#check_wait`); the floors read 4120 and 1337 (DERIVED, the last assignment
of each at `edb4a01e`), units 27 and 24 having raised the 4100 and 1317 the spec read at `d06e2a65`
first, as its Files touched anticipates; the `verb:unattended.sh:--mail` anchor read `9ed486eb`, unit
24's re-stamp of the `f25c9c53` the spec read (PINNED, `docs_leg.py --fingerprints` at `edb4a01e`); and
the refusal ceiling read 347 (PINNED, `.memory-tree.conf#REFUSAL_CEILINGS`). No arm of any suite greps
the `--mail` unknown-flag, unknown-verb or form refusal texts the pass rewords.

## Criteria

**Evidences:** KICK-dKeptSession-25
- AC1 — the row — `check_program` over the parsed definition, its inputs unchecked, returned the entry program `item.entry.mailbox-answer`, `.orient`, `.place`, `.place-check`, `.place-owner`, `.claim`, the new row first as it needs nothing; both input layers, `layer.flow` and `layer.memory`, are rows of the playbook kit's layers list; `check_wait` over the row returned no problem, and over a copy with its `deadline` deleted returned one `wait` problem naming `item.entry.mailbox-answer`, "it waits on another party and declares no deadline"; the actor matched `ACTOR_FORM` (DERIVED, those probes). The three loop legs over the tree, and the scratch clone's `termination.py check` exit 1, are the close's.
- AC2 — the answer — B's question to `build:fx` posted with `--default no`; A's `--mail answer fx <id> <body> --cite cited.txt@<base sha>` printed `mail — posted <id> · refs/gov/mail/fx/a/s1`, exit `0`, the record `kind: answer`, `to: build:fy`, `answers: <the question's id>`, `default: ack`, its body the file then `cites cited.txt@<the full sha>`; `derive_mail_answer_outcome fx <id>` printed `awaiting` before it and `answered` after, exit `0`; a second answer printed `answer — <id> · answered`, exit `1`; a cite of `-x`, a cite with no path and a cite of a path the sha does not hold each exited `2` with their S2 lines, the remote's ref count unmoved at `1` (DERIVED, the probe); an id naming no question exited `2` printing `is no question addressed to fx`, and the outcome over it `mail — not read · … is no question addressed to fx`, exit `2`; an unreadable body file, `--cite` with no value, two positional words and `--to` on an answer each exited `2` with their lines; `--mail read fx --cite a@b`, `--mail ack … --cite a@b` and `--mail post … --cite a@b` each exited `2` printing their own form; an unknown verb printed `--mail takes post, read, ack or answer`, an unknown flag the list naming `--cite`; an acknowledged question's outcome read `defaulted` and its answer printed `answer — <id> · acked`, exit `1`; with `RUN_CLAIMS` off an answer printed `mail — off`, exit `2`, before its bad cite was read (DERIVED, the probe).
- AC3 — the default — a question to `build:fx` whose line A's feed planted 73 hours back (PINNED, the probe's literal) under the default deadline read `defaulted`; one planted 30 hours back (PINNED, the probe's literal) read `awaiting` and was the one `--mail read fx --open --ids` id (DERIVED, the probe). The suite's arm stages AC3's own literals, `wait-ceiling = 30` and sightings an hour and 31 hours back; its run is the close's.
- AC4 — the wait renews — through `write_claim` over A's build lease of fx, keepalive k1 and session s1: with no question a renew within the tenure wrote `renews: no`; with an open question it wrote `renews: yes`, the verdict `question`, `LR_WAIT` the question's id and the witness kept, twice; with the record's `witness` the newest transition and the question open it wrote `renews: yes` and kept that transition (DERIVED, the probe). A scratch copy, outside the repository with the kit library beside it, whose `read_lease_renewal` returns before the question step wrote `renews: no` over the same open question (DERIVED, the probe). The `--beat` line's ` · wait question <id>` suffix, a due beat in the run-claim fixture, is the suite arm's, observed at the close.
- AC5 — the wait ends — the question answered, the next write was `renews: no`, its witness unchanged; a question sighted 73 hours back read `defaulted` and the write was `renews: no`, its witness unchanged and `LR_WAIT` empty; a transition differing from the record's `witness`, committed beside the open question, was the write's `new` verdict and its stored witness, `LR_WAIT` empty; a scratch copy storing the question's commit as the witness stored it, and its next write, the question still open, read the older transition as `new` and renewed (DERIVED, the probe).
- AC6 — the texts — `grep -n -- '--mail answer\|--cite\|wait question' tools/unattended/VERBS.template.md` found the `--mail` and `--beat` entries, `grep -n 'oldest open' tools/unattended/STOPS.template.md` the `leases.renewal` row, `grep -n 'item.entry.mailbox-answer\|six items\|--mail answer' help/loop.md` the guard paragraph, the `--mail` paragraph and the entry section; `cmp` found both installed guides equal to their templates; `grep -c 'five items' help/loop.md` printed `0`; `docs_leg.py --fingerprints` printed `verb:unattended.sh:--mail` at `dd481ead`, the fingerprint the paragraph's anchor now carries (DERIVED, those probes).

Every refusal the pass adds prints a line and `return`s 2 or 1 from a function, or sets `_rl_rc=2`, and
no added code line carries `exit 1`, `status=1` or a `fail` call, so the census at the driver's ceiling
does not move; it is read at the close. The new arms in `tools/unattended/unattended.test.sh` count 17
region-eight `same` (DERIVED, the blocks' own lines), raising `FLOOR_ASSERTIONS` to 4137 and
`FLOOR_SHARD_8` to 1354 (DERIVED, base plus 17), each with its `RAISED` line; their two scratch
drivers were staged here by the arms' own `awk` lines and differ from the driver by one line each
(DERIVED, `diff`). Their RED-first observations are the close's. `python tools/lexicon/lexicon.py`
exited 1 on its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that run), the count
unit 24's ledger read at its base, and names neither `write_mail_answer` nor
`derive_mail_answer_outcome`, each OK by `--suggest`. `gen_map.py --write` added those two rows to
`memory/map/generated/symbols.json` and moved nothing else.
