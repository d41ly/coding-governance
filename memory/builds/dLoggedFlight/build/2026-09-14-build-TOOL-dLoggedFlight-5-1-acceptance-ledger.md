# Acceptance ledger — TOOL-dLoggedFlight-5

**Serves:** journal TOOL-dLoggedFlight-5

Tier-2 · node d · 2026-09-14 · the build pass of the redaction table, against spec rev-3, which this
pass wrote before its code. Every criterion line is OBSERVED. The gate legs are written as owed.
`<suite>` is `tools/runlog/selftest.py`, run directly and never through the gate runner. Its three
timed runs over the staged kit printed `368 passed, 0 failed (368 assertions, floor 368)` in 3.4 to
3.6 s. No gate leg was run, per the owner's instruction of 2026-09-13, and no suite that existed under
`tools/unattended/` before this build ran.

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
  `task-` id matched, and `env-assign` widened to a spaced `=` so `PIN_KEY =` matched.
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
  text (33 arms), and the `aws-key` pattern broken, which missed every planted AWS string.
- AC5 — `CLASS_IDS` (`test_redact_ac5_class_ids`) — the declared ids are distinct, every one has a
  row, every row's id is declared, and each row carries a positive and a negative. The same comparison
  run over a scratch table missing its last row named that id as missing, and over one with an
  undeclared `rogue-class` row named it as extra. RED seen on mirrors two ways: the `named-token` row
  deleted (4 arms, and the count fell to 360 under the floor of 368), and an undeclared row added (7
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
The floor rose from 183 to 368, and a mirror with it at 369 exited 1, "under its floor".

## Staged RED

14 breaks, each applied to a MIRROR of the kit: a copy in a scratch dir, made a git repository so that
`git ls-files` resolves in it, and never the working tree. All 14 went RED on FAIL lines naming the
arm their break aimed at, and an unmodified mirror printed `368 passed` before each batch. One break
first went RED for the wrong reason: the undeclared-row mirror crashed the suite with a traceback,
because the in-suite comparison loaded a table carrying that row twice. The comparison now returns
the loader's refusal as its value, and the same break reds seven named arms.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `runlog selftest`, at or above its floor of 368 inside its 60 s budget row;
- `lexicon naming predicates`, `install-prefix (shipped surface)` and `govkit selfcheck`;
- `codebase-map coverage + freshness` and `memory hygiene`;
- `every held leg is budgeted, every budget row resolves`, since the budget row's evidence changed;
- `testsuite counts (every bar self-test prints one)`.

## Residue

- The first AC4 draft spliced each positive over filler characters, and six planted strings then
  carried a foreign claim. A near miss cut in two had become a real secret: the cut left a bare
  lowercase assignment in one string and a secret flag in front of the positive in another. The
  positive now goes in at a word boundary and only the far end is trimmed.
- Four negatives first held none of their own rule's hints, so the prefilter, not the pattern, left
  them alone and a widening could not red them. Those were `pem-block`, `env-assign`, `cookie` and
  `azure-key`. Each gained a near miss that reaches its regex, and an arm now asserts it per row.
- `tools/install-prefix-carried.txt` did not move: no shipped file of the kit gained a kit-path
  literal. `tools/govkit/subject-pins.tsv` did not move, since no leg was added.
- The runlog kit stays at 1.0, as the brief sets it, and no kit version moved in this unit.
- The budget row's evidence now reads the post-unit worst of three direct readings, 3.6 s against 2.4
  s before the redaction arms. Its figure stays at the file's 60 s floor, and the leg's ceiling of
  180 s did not move.
