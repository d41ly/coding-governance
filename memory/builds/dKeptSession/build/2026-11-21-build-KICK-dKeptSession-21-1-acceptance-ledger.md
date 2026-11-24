# KICK-dKeptSession-21 — acceptance ledger

**Serves:** journal KICK-dKeptSession-21

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands; the role's hook refused `sh_hygiene.py` as the `shell hygiene` leg
when it was tried. The criteria were observed on win32 at the pass's base `e356c0e3` over the working
tree before the commit: by one scratch probe script of this pass's own, which runs the notice block's
own driver and hook calls standalone over a bare origin and two clones B (`c1`, fleet tag `a`) and A
(`c2`, fleet tag `b`) under the short temp path, each conf `RUN_CLAIMS` on, policy values landed as the
block's `write_lease_policy` lands them; by `card-store.fixture.sh --plant mail-notice-boundary` run
alone by direct CLI; by `settings-merge.py --fragment` over a scratch copy of the base settings file;
and by the greps, `cmp`, `policy.py get` and `docs_leg.py --fingerprints` AC8 to AC10 state.

This pass is the unit's second dispatch: the first builder's pass was applied as its saved patch, read
against the spec, and every generator it names re-run. `policy.py lists --write` and
`render_playbook.py --reference` reproduced its `unsummarised-keys.txt` and `help/reference/policy.md`
(the render also rewrote three sibling reference pages' line endings alone, which were restored);
`gen_map.py --write` reproduced its four renders under `memory/map/generated/`. The kickoff manifest's
`last-audit` and the two budget rows the first builder priced over its base `71b22e42` were re-taken
at this base.

Before the first edit the spec's cited code was probed at the base, units 39, 51, 27, 24, 10 and 25
read as landed: `observe_remote`, `read_mailbox` (modes `soft|strict`, sixteen columns, `deadline` and
`default` last), `print_mailbox`, `check_mail_addressed`, `derive_mail_ref`, `derive_ref_segment`,
`check_slug_shape` and `read_lease_policy` (its last arm `flow.wait-ceiling`) in the driver;
`resolve_sidecar_dir` in the kit library; `resolveRepo`, `readMemoryRoot`, `resolveLease`,
`deriveSidecarPath` and `readSidecarLines` in `run-lease.js`; `run_card_boundary`,
`run_context_boundary`, `run_mail_interrupts <slug> [--local]`, `run_driver_bounded`,
`render_mail_line`, `render_pointers` and `CARD_CLAIMS_BOUND` in the kickoff engine;
`scratch-guard.js#checkItemBoundary`'s detached spawn and `factories.py#write_hook`. The floors read
4137 and 1354 in the driver suite and 442 in the kickoff suite (DERIVED, the last assignment of each at
`e356c0e3`), units 27, 24, 25 and 10 having raised the 4100, 1317 and 441 the spec read at `b2303b53`,
as its Files touched anticipates; the `verb:unattended.sh:--mail` anchor read `dd481ead`, unit 25's
stamp (PINNED, `docs_leg.py --fingerprints` at `e356c0e3`); the refusal ceiling read 347 (PINNED,
`.memory-tree.conf#REFUSAL_CEILINGS`). The only suite arm grepping a refusal text the pass rewords is
unit 25's `--mail read --cite` arm, re-armed for the read form's `[--local]`.

## Criteria

**Evidences:** KICK-dKeptSession-21
- AC1 — the boundary notice — B's first `--mail notice tFix` printed `mail — none for tFix · fetched` and wrote the stamp; A's `question` to `build:tFix` posted with `--default no`; a scratch copy whose notice reads with `local` in place of `soft`, one line apart from the driver (DERIVED, `diff`), printed `mail — none`; B's `--mail notice tFix --item <key>` then printed `mail — 1 unread for tFix · <A's id> · fetched · item <key>` (DERIVED, the probe).
- AC2 — the fallback — with B's origin pointed at a missing path, B's notice exited `0` and printed A's id with ` · local copy 14s old (the remote did not answer, git fetch exited 128: <the missing path>)`, the age within two seconds of the stamp's by `stat`, the stamp's mtime unmoved, and one `mail — local copy:` cause line on stderr; `--local` printed ` · local copy 16s old (--local)` and no cause line (DERIVED, the probe).
- AC3 — the boundary verb — `card-store.fixture.sh --plant mail-notice-boundary` printed four `held` rows, exit `0`, in 55.7 s (DERIVED, that run): the crossing printed the fetched `notice — mail — 1 unread for tFix · … · fetched · item <K2>` line at output line 4 before the `interrupt — mailbox` line at line 5 (DERIVED, the plant's own line count), the stub engine's last log line read `tFix --mail-interrupts --local`; no crossing printed no `notice —` line; under `mailbox.notice` planted `off` a crossing printed no `notice —` line and the log read `tFix --mail-interrupts`. `card-store.fixture.sh --list` names the plant once (DERIVED, `grep -c`).
- AC4 — the tool call — with `notice = "every-tool-call"` and `fetch-seconds = 10` (PINNED, the planted interval) landed on the origin and fetched, one notice wrote the stamp's first line `{"notice": "every-tool-call", "fetch-seconds": 10, "bash": "<Git's bash.exe as a native path>"}`; A posted, and B's hook fed one payload every two seconds (PINNED, the cadence) named the new id 14 s after the post, inside the 20 s window (PINNED, twice the interval; 14 DERIVED, the probe), its marker created once over eleven payloads (DERIVED, the probe); a copy of the hook whose one spawn line is a stub, one line apart (DERIVED, `diff`), never named the next message over eleven payloads (DERIVED, the probe).
- AC5 — no network on the call — with B's origin away and the stamp fresh, the hook fed one payload returned in 58 ms, under the 500 ms bound (PINNED, the bound; 58 DERIVED, `EPOCHREALTIME` around the call), its `additionalContext` naming both stamped ids; a payload with `agent_id` set and one for an unbound session printed nothing; `grep -c 'execFileSync\|spawnSync\|readPolicy' mail-notice.js` printed `0` (DERIVED, the probe).
- AC6 — a refused read — over a fresh fixture whose first policy revision does not parse, the notice exited `0` printing `mail — none for tFix · fetched`, and stderr held one `unattended: NOTE - mailbox.notice was not read, so it reads its catalogue default 'every-item'` line and one for `mailbox.fetch-seconds` reading `'60'`, each naming the policy kit's refusal of the file; the stamp's first line read `"notice": "every-item", "fetch-seconds": 60`, and the hook fed a payload printed nothing (DERIVED, the probe).
- AC7 — the ring — `--ring refs/gov/mail/fy/b/p1` with an id of eleven hex digits, and `--ring refs/heads/main` with a twelve-digit id, each exited `2` printing `mail — not read · --ring takes a mail ref and a twelve-hex-digit id` and nothing on stderr with the origin away, so no read ran; a valid pair printed S1's line, `… · fetched`; with `deps.messaging = "live-and-mailbox"` landed and no ring delivered, a new question was named by the next boundary notice (DERIVED, the probe).
- AC8 — the texts — `grep -c -- '--mail notice\|--local\|--ring\|mail-notice'` over `tools/unattended/VERBS.template.md` printed 10, `grep -c 'notice —'` 3 over `help/loop.md` and 1 over `help/orientation-card.md`, `grep -c 'mail-notice' tools/unattended/README.md` 2 (DERIVED, those greps); `cmp` of the template and `memory/guides/UNATTENDED-VERBS.md` was silent; `grep -c 'mailbox.notice\|mailbox.fetch-seconds' memory/project/docs-undocumented.txt` printed 0 (DERIVED); `docs_leg.py --fingerprints`, with the new hook's fragment in the index, printed `hook:mail-notice d1c1243b`, `policy:mailbox.notice 1a6cbc4e`, `policy:mailbox.fetch-seconds 15fe6233` and `verb:unattended.sh:--mail e05e3012`, each at `help/loop.md`, the fingerprints its anchors carry (DERIVED, that run).
- AC9 — the catalogue rows — `policy.py get mailbox.notice` and `get mailbox.fetch-seconds` in this repository, whose policy file sets neither, printed `every-item` and `60`; after `lists --write`, `tools/policy/unsummarised-keys.txt` names neither key (DERIVED, `grep -c` 0); every preset of `tools/policy/presets.toml` keeps both defaults. The mirror's `catalogue_blob` is re-stamped by `mirror --write` in the commit after the catalogue's, as `mirror --write` refuses while the catalogue differs from HEAD; its equality with `git rev-parse` of the committed catalogue is read after that commit and stated in the pass's return.
- AC10 — the wiring — `grep -c 'mail-notice.js' .claude/settings.json`, `grep -c 'PostToolUse {prefix}/unattended/mail-notice.js' tools/loop/loop.toml` and `grep -c 'PostToolUse tools/unattended/mail-notice.js' memory/map/features/unattended.md` each printed 1 (DERIVED, those greps); `settings-merge.py --fragment tools/unattended/mail-notice.fragment.json` over a scratch copy of the base settings file, in a scratch project holding the hook, wrote a file byte-equal to this tree's `.claude/settings.json`, and a second run reported it already wired and left it byte-equal (DERIVED, `cmp`).

Every refusal the pass adds prints a line and `return`s 2 from a function, or sets `_rl_rc=2`, and no
added code line carries `exit 1`, `status=1` or a `fail` call, nor a `$(printf`, `$(cat` or
`$(basename` site (DERIVED, a grep of the diff's added lines), so the census at the driver's ceiling
does not move; it is read at the close. No added line is a `while` loop fed by `<<<` or a process
substitution (DERIVED, a grep of the added lines). The new arms in `tools/unattended/unattended.test.sh`
count 19 region-eight `same` (DERIVED, the block's own lines: AC1 4, AC2 2, AC4 4, AC5 3, AC6 2, AC7 4),
raising `FLOOR_ASSERTIONS` to 4156 and `FLOOR_SHARD_8` to 1373 (DERIVED, base plus 19), each with its
`RAISED` line; the kickoff suite's `FLOOR_ASSERTIONS` rises to 443 (DERIVED, base plus the plant's one
ok row). The probe above ran the same 19 observations green in 94.9 s (DERIVED, `time`), the reading
the shard row is priced from. Their RED-first observations are the close's. `python
tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders over a pin of 1421
(DERIVED, that run), the count units 24 and 25 read at their bases, and its offender list names none of
`write_mail_notice`, `print_mail_notice`, `run_mail_notice`, `run_notice_arm`, `run_notice_hook`,
`readMailNotice`, `checkFetchDue`, `runDetachedFetch` or `renderMailNotice`. `gen_map.py --write`
added those functions' rows and the hook's `main` to `memory/map/generated/symbols.json` and the hook's key to `MAP.md`,
`CARDS.md` and `inventories.json`.
- seen-red — `manifest-check self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `mail-notice-boundary`: the notice step left out of the boundary verb
