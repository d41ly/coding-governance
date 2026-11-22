# KICK-dKeptSession-5 — acceptance ledger

**Serves:** journal KICK-dKeptSession-5

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `c9e89a05`,
each by a probe of this unit's own code: the driver's `--mail` verbs run by direct CLI over a scratch
fixture, a bare remote and two clones under the user temp directory, RUN_CLAIMS on, clone A under
`GOV_NODE=a` and B under `b`, each post under its own `CLAUDE_CODE_SESSION_ID`, the loop kit the
tracked one; the loop kit's and the record factory's own plants, each run alone by direct CLI; the
kickoff engine's card-store plants, each run alone by direct CLI; and `python -c` probes of the
transition writer's `read_mail_rows`.

Before the first edit the spec's cited code was probed at the base: `derive_ref_segment`,
`check_slug_shape`, `write_card_ref`, `write_register`, `resolve_claim_remote`, `add_feed_sightings`,
`CLAIM_KV_AWK`, `check_lease_witness` (columns 2, 4 and 10 by position), `check_mail_recipient`,
`check_mail_addressed`, `derive_message_id`, `check_mail_duplicate`, `refuse_waive_unless_preflight`,
`verbs_all` and the `gov:argv` sentinels in `tools/unattended/unattended.sh`; `build_gov_commit` and
`write_gov_ref` in `tools/lib/gov-ref.sh`; `read_first_seen` in `tools/lib/gov-feed.sh`;
`read_dispositions`, `check_loop` and `SEG` in `tools/loop/loop_lib.py`; `write_transition`,
`read_transitions`, `TRANSITION_FIELDS`, `VALUE`, `write_card_follow` and `resolve_build_anchor` in
`tools/loop/loop_transition.py`; `write_first_transition` and `PatchHeld` in `tools/loop/claim.py`;
`write_placement_fixture` and `write_fixture_gov_ref` in `tools/loop/placement.py`; `KINDS`,
`write_record` and `read_card` in `tools/memory-tree/build_records.py`; `TYPED_RECORD_KINDS` in
`tools/memory-tree/tree_lib.py`; `render_pointers`, `render_budget_line`, `run_driver_bounded`,
`POINTER_LINES` and `CARD_CLAIMS_BOUND` in `skills/session-kickoff/manifest-check.sh`; the `[[door]]` row
reading `pending = "dTotalRecall"` in `tools/playbook/doors.toml`. Each stood where the spec cites it.
One reading differs from the spec's wording and is recorded, not built around: `derive_message_id` at
the base takes six fields (KICK-dKeptSession-22), and KICK-dKeptSession-31, which widens it to eight,
builds after this unit, so S5's eight-argument call is written as the spec states and the function
reads its first six until that unit lands; the verb guide states the call's eight fields in order.

`python tools/lexicon/lexicon.py` exited 1 over the working tree on its verb-offender pin, 1432
offenders over a pin of 1421 (DERIVED, that run), the count KICK-dKeptSession-22's ledger read at its
own base; `--offenders` lists none of this unit's names, and `--suggest` graded each OK: the driver's
`build_gov_message`, `derive_mail_ref`, `write_mail_ref`, `write_mail_post`, `write_mail_ack`,
`print_mailbox` and `read_mailbox`, the engine's `render_mail_line`, the fixture's `write_card_mail`,
the suite's `seed_mail_at`, `run_mail_arm` and `read_mail_refs`, and the Python `read_mail_kinds`,
`read_mail_rows`, `write_mail_records`, `render_fixture_mail` and `read_mailbox_message`. The breach is
not this change's and is owed to the close. `python tools/playbook/writing_practice.py check
pinned-facts` read green.

Owed to the close: every leg the spec's section 7 names; the unattended suite whole, whose effective
`FLOOR_ASSERTIONS` rises from 4077 to 4091 and `FLOOR_SHARD_8` from 1294 to 1308 (PINNED, the block's
fourteen unconditional `same` rows, all in region eight); the kickoff suite, whose `FLOOR_ASSERTIONS`
rises from 438 to 441 (PINNED, the three plants' rows from its `--list` loop); and each `New arm:`
line's RED-first observation.

## Decisions taken in the build

- The post's sequence is one function, `write_mail_post`, the ack's one more, `write_mail_ack`, and the
  read verb's filter a third, `print_mailbox`: the dispatch arm parses the flags between the `gov:argv`
  sentinels, as `--lease` does, and calls them, so the arm stays a parser.
- `build_gov_message` binds GOVMSG and GOVMSG_WHY and prints nothing, so a caller keeps the refusal
  without a subshell; `write_register` keeps its readable-file check ahead of the problem id, and the
  builder holds the size and byte checks it held, so its lines are unchanged.
- The post validates the body and values once with a placeholder header before the remote, as S5
  orders, and builds the record again with the derived id after the duplicate check.
- `read_mailbox` stays dark while RUN_CLAIMS is not `on`, printing nothing; the verb prints `mail —
  off`, so `check_lease_witness` reads no stray line.
- Rows are printed oldest sighting first, an unsighted `-` after every stamp, ties by ref.
- The transition guard's `MailHeld` names every open id; the claim prints `claim held — <MailHeld>`.
- The transition plants keep their bare remote inside the scratch repository's git dir, so the
  fixture's one removal takes it, and reuse `placement.py`'s `write_fixture_gov_ref` to set each
  message; `render_fixture_mail` renders the message once for the transition and claim plants.
- The unattended suite's `seed_mail_at` sits beside `add_claim_sighting`, shared by the re-planted
  lease arms and the mailbox block.

**Evidences:** KICK-dKeptSession-5
- AC1 — the scratch fixture: session `s1` posted twice and `s2` once from `fx`, each printing `mail — posted <id> · <ref>`; the remote held `refs/gov/mail/fx/a/s1` at a first-parent count of 2 with its oldest commit parentless, and `refs/gov/mail/fx/a/s2` at 1, all three subjects `gov-mail fx/<id>`.
  (DERIVED, that probe.) A fourth post from session `s9` repeating `s1`'s first message printed `mail — duplicate` naming `s1`'s cache ref, exit 1.
- AC2 — `--kind chat` exited 2 printing `mail — not written · the kind 'chat' is none of the closed set: confirm-request …`, the remote's ref count unchanged; `python tools/loop/loop_lib.py --mail-kinds` printed the twelve kinds, exit 0; `--fixture --plant mail-kinds-repeated` printed `the mail kind confirm-request is given twice`, exit 1.
  (DERIVED, that probe.)
- AC3 — a sourced driver's `build_gov_message` returned 2 for a 4097-byte body, a body holding a NUL and a value holding a newline, each with its `write_register` words; `--register decision` and `--register problem` over one body through the new driver and through the base driver each wrote records whose `%B` read equal to the bytes the suite pins.
  (DERIVED, that probe; 4097 PINNED, one over the cap.)
- AC4 — B's `fy` question to `build:fx` read one row in A's `--mail read fx`, state `open`, reply `-`; after `--mail ack fx <id>` it read `acked`, its reply the ack's id, and the ack, addressed to `build:fy`, read `reply` in B's `--mail read fy`.
  (DERIVED, that probe.)
- AC5 — one id planted on `fy`'s refs `t8` and `t9`, `t9`'s sighting a day earlier, printed once at `t9`'s first-seen and ref; with the remote renamed away the read printed `mail — local copy: the remote did not answer …` on stderr and the cached row, exit 0.
  (DERIVED, that probe.)
- AC6 — `loop_transition.py --fixture --plant mail-open` printed `refused — tFix · mail open a1b2c3d4e5f6 …`, exit 1, commits unchanged; `--plant mail-disposed` wrote one commit holding the transition record and `…-mailbox-message-1.md`, its trailer and record carrying `disposed=a1b2c3d4e5f6`, the record read by `build_records.py read` with exit 0, `**Serves:** mailbox-message TOOL-tFix-1` and `**State:** acked`; the next move disposed nothing and the check read 0 findings.
  (DERIVED, that probe.)
- AC7 — RUN_CLAIMS off in clone A's conf: the post printed `mail — off`, exit 2, the remote's ref count unchanged; the read printed `mail — off`, exit 0; a `python -c` probe of `read_mail_rows` over that clone returned no row and the unarmed cause `mail — off`, which `write_transition` prints as its one `loop: mail · unarmed` line, and the transition plants whose repository holds no `.unattended.conf` printed that line and recorded.
  (DERIVED, that probe.)
- AC8 — `card-store.fixture.sh --plant mail-open`, `mail-none` and `mail-off` each printed `held`, the session card's pointers section carrying `mail — a1b2c3d4e5f6`, `mail — none` and `mail — skipped: RUN_CLAIMS is off`; `pointers-render`, `pointers-cap` and `pointers-replay` still read no `MISSED`.
  (DERIVED, that probe.)
- AC9 — the post with `CLAUDE_CODE_SESSION_ID` unset printed `mail — not written: no session id`, exit 2; the driver's lines spelling the namespace off comment lines are `derive_mail_ref`'s `MAIL_REF=` line and the two fetch refspecs alone.
  (DERIVED, that probe.)
- AC10 — the verb guide's `--mail` entry names the three verbs, the twelve kinds, the four recipient forms, the call's eight fields, the four states and exits 0, 1 and 2; `help/loop.md` names `mail open`; `docs_leg.py --list` lists `verb:unattended.sh:--mail` anchored by `help/loop.md`, its fingerprint as `--fingerprints` printed it; the Skill template holds one `unattended.sh --mail ` line, its render re-run and the cap raised to the render's CR-stripped size.
  (DERIVED, that probe.)
- AC11 — `build_records.py --fixture --plant typed-kinds` printed `build-records: PASS typed-kinds — 17 typed kinds bound`, `mailbox-message` among them.
  (DERIVED, that probe.)
- AC12 — a `python -c` probe rebinding `loop_witness.resolve_bash` to `None` raised `ValueError: mail unknown: no bash that can see <driver>` from `read_mail_rows` over clone A; `claim.py --fixture --plant mail-held` printed `claim: mail-held · held exit 1 · held`, its run carrying `claim held — dRunAgain · mail open a1b2c3d4e5f6`.
  (DERIVED, that probe.)
