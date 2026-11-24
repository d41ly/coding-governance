**Serves:** research KICK-dKeptSession-79

# Brief — dKeptSession: the closing diff review's promoted findings, closed in one unit

## The prompt

> /unattended dKeptSession

## The brief

### Goal

The closing diff review of this build, round 1 over `c2a407b0..bcecefcfc`, read CLEAN WITH FIXES:
- 0 blockers, 0 highs, 5 mediums and 3 lows;
- every finding confirmed, none refuted (run `wf_72f622df-161`);
- the report is
  `memory/builds/dKeptSession/reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md`.

The round is CONVERGED, and the driver recorded its exit with `--disposition promote`. The build
method promotes every confirmed finding at that exit: the mediums and lows batch into ONE unit, two
only across disjoint write sets. These eight do not split. The loop-kit and the driver fixes both
re-price rows of `tools/run-gates/selftest-budgets.txt`, so their write sets meet.

Write the spec of that one unit, `KICK-dKeptSession-79`, as a new Tier-2 spec in this build's
`spec/` folder. It closes M1 to M5 and L1 to L3, each by the fix the report states.

### Items

1. M1, `agent-output-interpolated-into-an-instruction`:
   - Validate a fetched mail record in ONE place, the driver's `read_mailbox` `flush()`
     (`tools/unattended/unattended.sh#read_mailbox`).
   - Drop a record whose id is not 12 lower-case hex digits, whose kind is outside the loop kit's
     closed mail set, whose build fails the slug shape, or whose build differs from its ref's slug
     segment.
   - Arm: a fixture remote carrying a planted record, with `position.py <slug> --mail-interrupts --local`
     printing no line with its text. Observed RED first against the current reader.
2. M2, `destructive-step-before-its-precondition`: in `tools/loop/loop_transition.py#write_transition`,
   compute the whole move before the ack write.
   - The move covers `derive_move`, the patch hold, the witness checks, the field loop, the tree
     verdict, the composition, `derive_move_scenarios` and the VALUE check.
   - Only then run `write_consumed_acks` and the MailHeld raise.
   - Add one plant per refusal class (a bad witness, a derived `--field`, a scenario conflict). Each
     asserts no ack commit lands and the row still reads open.
3. M3, `concurrency-is-not-a-budget`: the skeptic's corrected fix.
   - On a fetch that does not rewrite the stamp, `print_mail_notice` leaves `<stamp>.fetching` with
     its mtime at the attempt.
   - `tools/unattended/mail-notice.js` spawns nothing while that marker is younger than
     `mailbox.fetch-seconds`.
   - The 2*seconds stale-marker removal is kept only past that age.
   - Arm: two hook calls inside fetch-seconds after a failed fetch, and the second spawns nothing.
4. M4, `a-new-local-collides-in-a-long-function`:
   - Rename the notify.owner pair in `write_transition`, so the composition's `unread` cannot shadow
     it.
   - Add a plant: a pinned composition whose compose fails, with notify.owner selecting
     `transition`. Its `progress —` line prints, and no `progress · unread` line names the
     composition's cause.
5. M5 and L2, `observed-by-claim-no-arm-discharges`. Two suite arms in
   `tools/unattended/unattended.test.sh`, each with its floors raised from the figure read at the
   build base:
   - the card binding of `mail-notice.js` (`readCardBuild`): a card file names the build, no RUN.md
     session fact exists, and logging `git` and `bash` stubs stay empty;
   - the detached spawn's argv and `windowsHide: true`, through a recorder in place of
     `child_process.spawn`.
6. L1: correct the `measure_context_fill` docstring and the runlog README to `(share, window, source)`.
   That is the shape the code returns and both callers read.
7. L3: rewrite the `mail-notice.js` header so it agrees with its registration.
   - The registration's matcher is `*` and the hook is the only carrier of the unread-mail line.
   - KICK-dKeptSession-44 is CLOSED and frozen, so its S6 wording is not amended. Say so in §3 and
     cite this unit's text as the current statement.
8. The left-shift owed by each finding:
   - Two classes are NEW: `docstring-misnames-a-returned-value` and
     `header-rationale-contradicts-the-registration`. Each becomes a bug-class record under
     `memory/gotchas/`, with its map claim and `gotchas.py --write`, as this repository's left-shift
     practice requires.
   - The other classes already exist. Their new arms are the gate.
9. Budgets: the `loop transition record` leg's 120 s ceiling (PINNED 2026-11-23, tools/gate-legs.json)
   is the owner's parked decision. This unit re-prices its rows from measured readings, never stops
   on that ceiling, and never edits `tools/gate-legs.json`.
10. Write `Files touched` as the complete write set, each path tied to its clause. Include
    `tools/run-gates/selftest-budgets.txt`, and every help page and verbs-guide copy a changed
    behaviour reaches. Leave out `memory/DECISIONS.md` and `.memory-tree.conf`, which check 49
    refuses to a pass.
11. Header: Tier-2, `order 37` (one past KICK-dKeptSession-65's 36), streams kickoff, advancing
    KICK-dKeptSession-29 as its siblings do.
    - Carry no clause: a promotion derives from the review, not the packet.
    - Each `New arm:` line names its RED-first staging.
    - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED on its own line.
    - Keep within the live-spec size cap, and leave no fork open.

### Acceptance

These all report nothing for the new spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-79`

### Gates

Only these: the memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker,
the pinned-facts check and the driver's `--check-specs`.

### Non-goals

- No product code, no commit and no index render.
- No spec other than KICK-dKeptSession-79's. Read the others freely; edit only the new spec, in the
  run worktree.
