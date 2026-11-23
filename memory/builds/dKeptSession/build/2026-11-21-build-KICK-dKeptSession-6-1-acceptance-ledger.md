# KICK-dKeptSession-6 — acceptance ledger

**Serves:** journal KICK-dKeptSession-6

No merge bar, no self-test suite and no gate leg ran in this pass; the role's hook refused
`render_playbook.py --reference --check` as the `help reference pages` leg when it was tried, so that
check and `policy.py lists --check` and `mirror --check` are the close's. The criteria were observed
on win32 at the pass's base `c18b223b` over the working tree before the commit: by two scratch probe
scripts of this pass's own, each building a bare origin and a clone `c1` under the short temp path,
its conf `RUN_CLAIMS` on, the tracked driver run over it with `USERNAME` daily-agent, so the fleet tag
is `a`, and a policy value landed as the suite's `write_lease_policy` lands one, committed, pushed to
the origin's `main` and fetched; the second probe runs the new block's own expressions and `same`
calls standalone; and by the greps, `cmp` and `policy.py get` AC5 to AC7 state.

Before the first edit the spec's cited code was probed at the base, units 39, 51, 27, 24, 10, 25 and
21 read as landed: `write_mail_post` takes ten arguments and ends in one `case` over `write_mail_ref`'s
return whose `0)` arm prints `mail — posted <id> · <ref>` and returns 0; `write_mail_ack` and unit 25's
`write_mail_answer` each post through it; `read_lease_policy`'s last arms are `flow.wait-ceiling`,
`mailbox.notice` and `mailbox.fetch-seconds`, with no `deps.messaging` arm; the catalogue's
`deps.messaging` row carried no `summary` and stood in `unsummarised-keys.txt` and
`docs-undocumented.txt`; `git grep -n 'SendMessage\|doorbell' -- tools skills` printed only the row's
`registry` cell (F1). The floors read 4156 and 1373 (DERIVED, the last assignment of each at
`c18b223b`), unit 21 having raised the 4100 and 1317 the spec read at `b2303b53`, as its Files touched
anticipates. `docs_leg.py --fingerprints` printed `policy:deps.messaging 21013b0f` with no anchoring
page (DERIVED, that run at `c18b223b`), the fingerprint S5's anchor carries. No suite arm greps the
reader's refusal or NOTE texts the pass widens (DERIVED, a grep of the suite and every kit).

## Criteria

**Evidences:** KICK-dKeptSession-6
- AC1 — the post rings — with no `deps.messaging` set, a `landed` post printed `mail — posted <id> · refs/gov/mail/tFix/a/r1` then `ring — none · no live channel in this harness (stand-in dWellOiledMachine)` as its last two lines, exit `0`, nothing on stderr; with `[deps]` `messaging = "mailbox-only"` landed, the next post's last line was `ring — off (deps.messaging: mailbox-only)`, exit `0` (DERIVED, the probes).
- AC2 — after the write, ref and id only — a sourced driver whose `run_mail_ring` records its arguments and `git ls-remote origin <ref>` held one call of `2` arguments, the mail ref and the id the message's record names, the ls-remote sha equal to the origin's ref after the post; with `write_gov_ref` replaced by one returning 1, the post printed one `mail — lost <id> · <ref> · ` line and returned `1`, and the recorder file was never created (DERIVED, the probes).
- AC3 — `live-only` keeps the mailbox — with `messaging = "live-only"` landed, the post moved the session's mail ref on the origin (one ref where none was) and printed `ring — none · no live channel in this harness (stand-in dWellOiledMachine)`, exit `0` (DERIVED, the probes).
- AC4 — a refused read — a sourced driver whose `read_lease_policy` returns 1 for `deps.messaging` alone with `a planted refusal` in `LP_VALUE`, every other key through the driver's own copy, printed for `run_mail_ring refs/gov/mail/fx/a/s1 0123456789ab 2>&1` one line `unattended: NOTE - deps.messaging did not read, so the ring takes live-and-mailbox: a planted refusal`, then the `ring — none …` line, rc `0` (DERIVED, the probes).
- AC5 — the texts — `grep -c 'ring —'` and `grep -c 'deps.messaging'` each printed 3 over `tools/unattended/VERBS.template.md`, every hit inside the `--mail` entry, and 1 over `help/loop.md`, in the paragraph directly after the `--mail` one (DERIVED, those greps); `cmp` of the template and `memory/guides/UNATTENDED-VERBS.md` printed nothing; `grep -c 'usage: policy:deps.messaging' help/loop.md` printed 1 and `grep -c 'It prints ONE line: .mail — posted'` over the template printed 0 (DERIVED). The grep `post's line\|ONE line` found unit 25's "so the post's line and exits are the answer's" in the template, rewritten to "lines", and `write_mail_answer`'s header comment said the same and is rewritten alike.
- AC6 — the row — after `lists --write`, `grep -c '^deps.messaging$' tools/policy/unsummarised-keys.txt` printed 0, and `grep -c '^policy:deps.messaging' memory/project/docs-undocumented.txt` printed 0 after the row's hand deletion (DERIVED, those greps); `render_playbook.py --reference` re-rendered `help/reference/policy.md`, which now sends the key to `help/loop.md` and counts it out of the unsummarised list, its three sibling pages' line-ending-only rewrites restored; `policy.py get deps.messaging` in this repository printed `live-and-mailbox`. The `lists --check`, `mirror --check` and `--reference --check` readings are the close's; the mirror's `catalogue_blob` is re-stamped by `mirror --write` in the commit after the catalogue's.
- AC7 — the driver's comments and lists — `grep -c 'deps.messaging' tools/unattended/unattended.sh` printed 12 (DERIVED, that grep at observation time): the default, the `get` line, the closed-set line, the signature comment, the no-kit NOTE, the unknown-key refusal, `read_lease_policy`'s two header-comment lines, and `run_mail_ring`'s comment and NOTE lines; `grep -n 'run_mail_ring'` found its definition, its call in `write_mail_post`'s `0)` arm, a line of `write_mail_post`'s header comment and one of `read_lease_policy`'s, and that header now says a posted outcome is followed by the ring point's one `ring —` line.

No added driver line carries `exit 1`, `status=1` or a `fail` call (DERIVED, a grep of the diff's
added lines), so the census at the driver's ceiling does not move; it is read at the close. No added
line is a `while` loop fed by `<<<` or a process substitution. The new arms in
`tools/unattended/unattended.test.sh` count 6 region-eight `same` (DERIVED, the block's own lines:
AC1 2, AC2 2, AC3 1, AC4 1), raising `FLOOR_ASSERTIONS` to 4162 and `FLOOR_SHARD_8` to 1379 (DERIVED,
base plus 6), each with its `RAISED` line. The second probe ran the same 6 observations green in 32.2 s
(DERIVED, `time`); over the base driver it read 5 of them red and the lost-write arm green, since the
base rings nothing, so that arm's RED-first observation needs a staged break ringing in the `1)` arm.
The RED-first observations are the close's. The shard 8/8 budget row is not re-priced, as the spec's
Files touched says. `python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders
over a pin of 1421 (DERIVED, that run), the count unit 21 read at its base, and its offender list names
none of `run_mail_ring`, `run_ring_arm` or `read_lease_policy_once`. `gen_map.py --write` added
`run_mail_ring` and the suite's `run_ring_arm` and two in-arm redefinitions to
`memory/map/generated/symbols.json`, and rewrote no other map file.
