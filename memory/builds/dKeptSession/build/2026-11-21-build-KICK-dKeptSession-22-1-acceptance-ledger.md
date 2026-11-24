# KICK-dKeptSession-22 — acceptance ledger

**Serves:** journal KICK-dKeptSession-22

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `38d0012e`,
each by a probe that sources `tools/unattended/unattended.sh` in a fresh bash and calls the three new
functions, `derive_gov_id`, `derive_message_id` and `check_mail_duplicate`, over a body file in the
session scratchpad and scratch repositories under the user temp directory whose cache refs
`refs/gov/remote/mail/fx/a/<session>` hold planted parentless commits subjected `gov-mail fx/<id>`.
A second probe, a scratch script holding the new suite block verbatim (its `mktemp -d` swapped for a
short temp path), printed the five lines its five `same` rows compare, each equal to the row's
expected text.

Before the first edit the spec's cited code was probed at the base: `derive_problem_id`
(`tools/unattended/unattended.sh#derive_problem_id`) pipes the three fields, each NUL-ended, then the
body's bytes and one NUL into `GIT hash-object --stdin` and cuts 12 hex; its one caller is
`write_register` (`tools/unattended/unattended.sh#write_register`), which tests the body file's
readability first; `read_claims`, `build_gov_commit`, `write_feed_success`, `derive_section_sha`,
`derive_request_content_key` and the suite's `run_register_arm` all stand where the spec cites them;
and `git grep` for the three new names under `tools` and `skills` found nothing. The landed body,
re-run over a missing file, printed the fields-only hash with rc 0, as section 4 says.

`python tools/lexicon/lexicon.py` exited 1 over the working tree on its verb-offender pin, 1432
offenders over a pin of 1421 (DERIVED, that run), the count KICK-dKeptSession-28's ledger read at its
own base, so this change adds none; `--suggest --as sh.function` graded `derive_gov_id`,
`derive_message_id`, `check_mail_duplicate` and the suite's nested `build_mail_commit` OK. The breach
is not this change's and is owed to the close.

Owed to the close: every leg the spec's section 7 names, the unattended suite whole, whose effective
`FLOOR_ASSERTIONS` rises from 4072 to 4077 and `FLOOR_SHARD_8` from 1289 to 1294 (PINNED, the block's
five unconditional `same` rows, all in region eight), and the `New arm:` line's RED-first observation
on the base driver, which has no message id.

## Decisions taken in the build

- `derive_gov_id` sits directly above `derive_problem_id`, its first caller, and `derive_message_id`
  and `check_mail_duplicate` directly below `check_mail_addressed`, the mailbox predicates the post
  calls beside them.
- `derive_gov_id --file` with no path, or a path that is no readable file, returns 1 before the pipe;
  zero fields and no `--file` hash the empty input, since a `printf` with no argument would still
  print one NUL and is guarded.
- `derive_message_id` writes `none` for an empty field as for an absent one, so an empty `answers`
  and the literal `none` are one id.
- `check_mail_duplicate` prints its one line on stdout and returns 1, no `fail` call and no `exit 1`
  or `status=1`, so the driver's refusal census does not move; the subject is matched whole through
  awk's ENVIRON, never as a pattern.
- The suite block plants a ref under build `fxy` too, so a prefix that matched `fx` without its
  trailing slash would red AC4's row.

**Evidences:** KICK-dKeptSession-22
- AC1 — the sourced probe: `derive_problem_id s1 entry.claim push-main.sh body.txt` and the hand pipe both printed `7de4931227cd`; `derive_gov_id --file` over a missing file returned 1, and `derive_problem_id` over it 1.
  (DERIVED, that probe.) The planted `derive_gov_id` that drops the file's trailing NUL printed
  `fa225da7e65f` for the same call (DERIVED, that probe), and the landed body over the missing file
  printed the fields-only `050f12d52656` with rc 0 (DERIVED, that probe): the two reds the criterion names.
- AC2 — the sourced probe: `derive_message_id fx 'item.design.exit@1#0a1b2c3d' 1 question I16 none` printed `280a6766c48a` under `CLAUDE_CODE_SESSION_ID=s1` and under `s2`, and a changed value in each of the six fields printed six other ids.
  Six fields, six ids each unequal to the first (DERIVED, that probe).
- AC3 — the sourced probe: with that id planted on `refs/gov/remote/mail/fx/a/s1`, `check_mail_duplicate fx 280a6766c48a` returned 1 printing `mail — duplicate 280a6766c48a · refs/gov/remote/mail/fx/a/s1`.
  (DERIVED, that probe.)
- AC4 — the sourced probe: with session `s2`'s ref holding only another message, the check for the retry returned 1 naming `s1`'s ref; a planted check reading only `s2`'s ref returned 0, the red the criterion names.
  (DERIVED, that probe.) In the suite-block probe an id planted only under build `fxy` returned 0
  for `fx`, and in the sourced probe build `fxy`'s own check returned 1 naming its own ref.
- AC5 — the sourced probe, in a fresh repository with no commit and no mail ref: two `ack`s from one item and pass answering `q1` and `q2` printed `c3bf806764ff` and `995bbf5d9455`, each check returned 0, and once the first was planted the second returned 0 and the first 1.
  (DERIVED, that probe.) A `git log --source --first-parent` over no revision there exited 128 (DERIVED,
  that probe), the red a check running the log over no ref would show; a directory outside any
  repository returned 2.
