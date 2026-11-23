# KICK-dKeptSession-27 — acceptance ledger

**Serves:** journal KICK-dKeptSession-27

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `64e146d9`
over the working tree before the commit, by a scratch probe script of this pass's own (a bare
remote and two clones A and B under the short temp path, each post made through the driver's
`--mail` verb under its own `CLAUDE_CODE_SESSION_ID`, each check in a subshell that sources the
driver and runs `load_driver_conf`), by the greps and `cmp` AC6 states, and by one direct call of
`tools/loop/loop_transition.py#read_mail_rows` over clone A.

Before the first edit the spec's cited code was probed at the base. `write_mail_post` took eight
arguments and passed `none` as `derive_message_id`'s eighth field; `read_mailbox`'s walk read the
six keys it requires and printed eleven columns, `reply` last (DERIVED, read at `64e146d9`); the
`--mail` dispatch's value flags and its two refusals spelled the set the spec names; the comment
above `MAIL_COLUMNS` named "the columns of one row"; the `help/loop.md` anchor read `f25c9c53`
(PINNED, `docs_leg.py --fingerprints` at `64e146d9`); and no arm of the suite greps either refusal
the dispatch rewords. The floors had moved past the spec's figures: unit 23 raised them first, as
§4 anticipates, to 4100 and 1317 (DERIVED, the last assignment of each at `64e146d9`).

## Criteria

**Evidences:** KICK-dKeptSession-27
- AC1 — `--mail read fy` — on A, after `s0`'s one post and `s1`'s two, printed `s1`'s two rows with column 12 reading `1` and `2`, and every row 14 fields (DERIVED, the probe).
- AC2 — `seen-utc` — with `s0`'s feed line on A rewritten to `2026-01-01T00:00:00Z` (PINNED) and `s2` posting twice, column 13 read `s1`'s second id on `s2`'s first message, `none` on `s2`'s second and `none` on `s0`'s, the build's first; `s1`'s first message named `s0`'s id (DERIVED, the probe, ids from each post's `mail — posted` line). Staged red: with `read_first_seen` redefined in a sourced subshell to answer `-` for every pair, as a pair spelled with the cache prefix reads, a fresh session's first post named `s0`'s id, the lesser ref, where the green reading names the newest tip (DERIVED, the probe).
- AC3 — `--interface` — a `confirmed` post naming an interface file recorded `seq`, `after` and `content-key` after `answers`, its `content-key` equal to `derive_gov_id --file` over that file and its id equal to `derive_message_id` over its fields with that key eighth; a `changed` with no `--interface`, a `question` naming one and a `confirmed` naming an absent file each exited `2` with S3's line, and the remote's ref count stayed `5` across the three (DERIVED, the probe). `--mail read` naming `--interface` printed the read's form refusal, and an unknown flag the `--mail takes` line naming `--interface` (DERIVED, the probe).
- AC4 — `check_interface_notice fy I16 i2.txt` — on B, with B's feed planted the `changed`'s tip at `2026-01-01T00:00:00Z` and the `confirmed`'s at `2026-01-01T00:01:00Z` (PINNED) before its first read, printed `interface — current <the changed's id> · changed · key <i2.txt's key>` and exited `0`; over the same read, an arrival-order pick of the newest `first-seen` named the `confirmed` (DERIVED, the probe).
- AC5 — `interface — unconfirmed` — over an interface file matching neither key the check printed that line with the file's key and exited `1`; over an absent file it printed `interface — not read · the interface file cannot be read: <file>`, exited `2` and printed no `unconfirmed` line; with `RUN_CLAIMS` off it printed `interface — off` and exited `2` (DERIVED, the probe).
- AC6 — `grep -n "content-key" tools/unattended/VERBS.template.md` — found the `--mail` entry naming `seq`, `after`, `content-key` and `--interface`, the act sentence of KICK-dKeptSession-51 kept after the id sentence; `cmp` found `memory/guides/UNATTENDED-VERBS.md` equal; `grep -n -- "--interface" help/loop.md` found the `--mail` paragraph; `grep -n "interface <file>"` over the driver found the usage line; `docs_leg.py --fingerprints` printed `verb:unattended.sh:--mail` at `4a30e33b`, the fingerprint the paragraph's anchor now carries (DERIVED, those probes).
- AC7 — `read_mail_rows` — called directly over clone A's fourteen-column read of `fy`, it returned every row with the 11 keys of `MAIL_COLUMNS` and `reply` intact, unarmed `None` (DERIVED, that call). The guard's `refused — <build> · mail open <id>` line under `loop_transition.py --fixture --plant mail-open` is a plant of the loop kit's self-test and is owed to the close.

Every refusal the pass adds prints a line and `return`s from a function, and the one added line
carrying `exit 1` opens `#`, so the census at the driver's ceiling (PINNED,
`.memory-tree.conf#REFUSAL_CEILINGS`, 347) does not move; it is read at the close. A cache read the
post cannot complete, a `rev-list --count` or the predecessor's `for-each-ref`, refuses with a
`mail — not written` line naming the mail cache, exit 2, where the spec names no outcome, so an
unread order never writes a guessed `seq` or `after`; no arm reaches either line, nor the check's
`interface — not read` line over a refused read. The new arm in
`tools/unattended/unattended.test.sh` counts 8 region-eight `same` (DERIVED, the block's own lines),
raising `FLOOR_ASSERTIONS` to 4108 and `FLOOR_SHARD_8` to 1325 (DERIVED, base plus 8), each with its
`RAISED` line; its RED-first observation is the close's. `python tools/lexicon/lexicon.py` exited 1
on its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that run), the count unit 51's
ledger read at its base, so `check_interface_notice` adds none. `gen_map.py --write` added that
function's one row to `memory/map/generated/symbols.json` and moved nothing else.
