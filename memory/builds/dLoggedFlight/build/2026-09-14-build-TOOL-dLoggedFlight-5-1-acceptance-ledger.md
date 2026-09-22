# Acceptance ledger — TOOL-dLoggedFlight-5

**Serves:** journal TOOL-dLoggedFlight-5

Tier-2 · node d · 2026-09-14 · the build pass of the redaction table, against spec rev-3, which this
pass wrote before its code, and the fold of its bug-class checklist. Every criterion line is OBSERVED.
The gate legs are written as owed. `<suite>` is `tools/runlog/selftest.py`, run directly and never
through the gate runner. Its three timed runs at the build commit printed
`368 passed, 0 failed (368 assertions, floor 368)` in 3.4 to 3.6 s, and its runs after the fold
printed `370 passed, 0 failed (370 assertions, floor 370)`. No gate leg was run, per the owner's
instruction of 2026-09-13, and no suite that existed under `tools/unattended/` before this build ran.
The closing diff review's round-1 fold of observation O1 bumped the spec to rev-4 and added two rows,
`bearer-token` and `aws-sts-key`; the AC lines below say what that fold observed of them.

## The criteria

**Evidences:** TOOL-dLoggedFlight-5

- AC1 — `python <kit>/selftest.py` (`test_redact_ac1_rows`) — every row's expanded positive was
  changed by `render_redacted` with none of its random values left in the output. The first rule to
  claim each positive was its own, and the rendered text scanned clean and rendered unchanged. Every
  expanded negative came back unchanged under the whole table, and each negative holds one of its own
  rule's hints, so the pattern and not the prefilter is what leaves it alone. Every run also breaks and
  widens each rule in memory (`test_redact_ac1_staged_red`): a never-matching pattern lost its
  positive's own claim, and an everything pattern changed its negative, for every row. RED seen on
  mirrors three ways: the `aws-key` pattern broken (5 arms), the `sk-key` lookbehind dropped so a
  `task-` id matched, and `env-assign` widened to a spaced `=` so `PIN_KEY =` matched. The fold of O1
  saw both new rows pass every per-row check, and the `auth-header` positive and the two-rule overlap
  arm stayed that row's, since it runs before `bearer-token`. RED seen in place, restored by checksum: the
  `bearer-token` value's 20-character floor dropped, which redacted its `Bearer realm=` near miss,
  and the `aws-sts-key` pattern keyed on `AKIA`, which lost its own positive.
- AC2 — `render_redacted` (`test_redact_ac2_prefix_kept`) — a generated value after
  `Authorization: Bearer ` rendered as exactly `Authorization: Bearer <redacted:auth-header>`. A
  generated 40-character token in `https://<value>@host/x` rendered as
  `https://<redacted:url-userinfo>@host/x`, and so did a `user:pass` userinfo. No value remained, and
  the near miss `ssh://git@host/x` came back unchanged. RED seen with the span taken from the whole
  match instead of group `v`: all three renders lost their prefix, and both overlap arms redded too.
- AC3 — `scan_secrets` (`test_redact_ac3_kit_scans_clean`) — over the bytes of every file
  `git ls-files` lists under the kit, with the table's positive column blanked, it found nothing. The
  listed population held the table, the reader and the suite. A control shows the unblanked table DOES
  hit, and only in the positive column, so the exclusion is load-bearing and no wider than one column.
  An expanded positive written into a negative cell was a hit on exactly its own line. The arm redded
  during the build on four spellings in the suite itself: a comment quoting a template, a bytes
  literal, and the two inputs of the overlap arm, which are now assembled from pieces. RED seen on
  mirrors two ways: a literal key appended to the README, and a new tracked fixture holding a planted
  token, which also redded the kit's fixture-declaration arm.
- AC4 — `scan_secrets` (`test_redact_ac4_prefilter_count`) — 50,000 generated 200-character strings,
  every hundredth carrying one row's expanded positive and every row planted. The wrapped patterns'
  `finditer` calls numbered 341,274, equal to the (string, rule) pairs whose hint matched, of 850,000.
  Every planted secret was found by its own rule, nothing else in a planted string was claimed, no
  planted value survived the render, and no unplanted string yielded a span, near misses included. The
  scan's wall time, 1.3 to 1.9 s across runs, is printed report-only. RED seen three ways: the
  prefilter removed (850,000 searches), hints matched against the raw text instead of the lowercased
  text (33 arms), and the `aws-key` pattern broken, which missed every planted AWS string. With the
  fold of O1's two rows the searches numbered 341,644 of 950,000 pairs, every row still planted.
- AC5 — `CLASS_IDS` (`test_redact_ac5_class_ids`) — the declared ids are distinct, every one has a
  row, every row's id is declared, and each row carries a positive and a negative. The same comparison
  run over a scratch table missing its last row named that id as missing, and over one with an
  undeclared `rogue-class` row named it as extra. RED seen on mirrors two ways: the `named-token` row
  deleted (4 arms, and the count fell to 362 under the floor of 370), and an undeclared row added (7
  arms, the class comparison among them).

## The edges the criteria do not name

`test_redact_edges` observed the §5 named results. An empty string has no span and renders as itself.
Bytes and `None` raise `TypeError` naming `str`. An unknown template token is refused by name. A CRLF
copy of the table loads the same rules. Eleven malformed tables, a table that is not UTF-8 and an
absent one are each refused by a message naming why, and the smallest valid table loads one rule.
A value two rules match goes once to the earlier row: an assignment of a `ghp_` token to a
`*_TOKEN` name renders as `github-token`, and a bearer header holding one renders as `auth-header`.
RED seen with the CRLF tolerance removed (1 arm), the overlap rule removed (2 arms, each value
rendered twice over) and the placeholder skip removed (6 arms, each a rendered positive matched again).
The floor rose from 183 to 370, and a mirror with it at 371 exited 1, "under its floor".

## Staged RED

17 breaks, each applied to a MIRROR of the kit: a copy in a scratch dir, made a git repository so that
`git ls-files` resolves in it, and never the working tree. All 17 went RED on FAIL lines naming the
arm their break aimed at, re-run in one batch against the folded kit, where an unmodified mirror
printed `370 passed` first. One break first went RED for the wrong reason: the undeclared-row mirror
crashed the suite with a traceback, because the in-suite comparison loaded a table carrying that row
twice. The comparison now returns the loader's refusal as its value, and the same break reds seven
named arms.

## The checklist over the build commit

`gotchas.py --for-diff HEAD~1..HEAD` selected eleven classes, and one was violated.
`two-answers-to-one-question`: the table's header states the 196-character bound and the template
classes for the author of a new row, while the suite enforces its own copies of both, and nothing
held the two together. The fold added `test_redact_table_header`, which reads the header and
compares both. RED seen three ways on mirrors: the suite's bound moved to 190, a template class the
header does not name, and a class dropped from the header. The dossier's typed string count went
with it, since the suite owns that number. The others were checked and hold. Each negative reaches
its own regex, so no arm passes by finding nothing. The in-memory breaks replace the pattern, which
is the subject, and never the shipped positives and negatives it is graded against. Every nested
helper leads with a declared verb. The table was written by a script file, never through a heredoc.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `runlog selftest`, at or above its floor of 370 inside its 60 s budget row;
- `lexicon naming predicates`, `install-prefix (shipped surface)` and `govkit selfcheck`;
- `codebase-map coverage + freshness` and `memory hygiene`;
- `every held leg is budgeted, every budget row resolves`, since the budget row's evidence changed;
- `testsuite counts (every bar self-test prints one)`.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. Every leg listed above is GREEN. `runlog selftest` printed
`1543 passed, 0 failed (1543 assertions, floor 1543)`, this unit's floor of 370 having risen with
the units after it. The suite cost 80 s run directly, under the 93 s its budget row declares, so
`tools/run-gates/selftest-budgets.txt` does not move; inside the bar's 8-wide pool the same leg
recorded 93.9 s, a contention reading that file's own header says to re-read on a quiet box. The
row now declares 93 s rather than the 60 s written above. The run's one RED, `govkit selftest`, is
on none of these legs: its 30 failing assertions are the IDENTICAL set `origin/main` carries,
pre-existing, untouched by this build and being fixed in a separate session. It is not called
green here.

## Residue

- The first AC4 draft spliced each positive over filler characters, and six planted strings then
  carried a foreign claim. A near miss cut in two had become a real secret: the cut left a bare
  lowercase assignment in one string and a secret flag in front of the positive in another. The
  positive now goes in at a word boundary and only the far end is trimmed.
- Four negatives first held none of their own rule's hints, so the prefilter, not the pattern, left
  them alone and a widening could not red them. Those were `pem-block`, `env-assign`, `cookie` and
  `azure-key`. Each gained a near miss that reaches its regex, and an arm now asserts it per row.
- Two negatives landed in the build commit carrying a filesystem path, an absolute Windows one in the
  `env-table` row and a home-relative key file in the `pem-block` row. This repository is public, so a
  second fold replaced both with path-free near misses before the unit returned, and the suite still
  printed `370 passed`.
- `tools/install-prefix-carried.txt` did not move: no shipped file of the kit gained a kit-path
  literal. `tools/govkit/subject-pins.tsv` did not move, since no leg was added.
- The runlog kit stays at 1.0, as the brief sets it, and no kit version moved in this unit.
- The budget row's evidence now reads the post-unit worst of three direct readings, 3.6 s against 2.4
  s before the redaction arms. Its figure stays at the file's 60 s floor, and the leg's ceiling of
  180 s did not move.
- The fold of O1 took the two misses of the review's probe that sit beside a row the table has. The
  SendGrid, DigitalOcean, Shopify, Stripe restricted and Twilio shapes it also found stay in the
  documented residue of a class with no row. A `Bearer` value under 20 characters is not redacted
  outside the `Authorization` header, the price of leaving prose such as `Bearer realm=` alone.
