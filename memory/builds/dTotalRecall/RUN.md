# dTotalRecall - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 581a761f8
phase: REVIEWING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dtotalrecall-4bf827
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-25T21:37:34Z
pid-image: claude.exe
host: compeeto
pid: 1700
session: 23826028-3fee-42de-ac69-b4090f699257
keepalive: 2ec9a796
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 462d20f3510072a1dddb5b948370937cfd3bbe0e
anchor-ref: refs/heads/main
base: 462d20f3510072a1dddb5b948370937cfd3bbe0e

## Parked

2026-10-25T23:39:11Z rescope · item add TOOL-dTotalRecall-36 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 1 HIGH, item H1: unit 19's causes check reds every record a current writer adds after the seed, because no writer but the door emits a Caused-by line; repairs TOOL-dTotalRecall-19

2026-10-25T23:39:22Z rescope · item add TOOL-dTotalRecall-37 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 16 HIGH, item H2: unit 8 registers tools/workflows/*.js as linguist-generated, which drops the four template sources and three hand-written workflow scripts from the code record; repairs TOOL-dTotalRecall-8

2026-10-25T23:39:23Z rescope · item add TOOL-dTotalRecall-38 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 17 HIGH, item H3: unit 5's reader census finds regex readers only, so the split-on-hyphen id readers stay unpointed and its flip probe still prints ok under the hyphenated in-slug date; repairs TOOL-dTotalRecall-5

2026-10-25T23:39:24Z rescope · item add TOOL-dTotalRecall-39 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 23 HIGH, item H4: unit 19 mints read_header_edges in tree_lib.py beside PLAY-dOrderedCharter-28's edge_grammar adapter of that name, and the two read the bulleted Caused-by form differently; repairs TOOL-dTotalRecall-19

2026-10-25T23:39:24Z rescope · item add TOOL-dTotalRecall-40 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 36 HIGH, item H5: unit 4's routing region compares the retired journal kind raw, so every log record written after unit 18 drops out of it; repairs TOOL-dTotalRecall-4

2026-10-25T23:39:25Z rescope · item add TOOL-dTotalRecall-41 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 49 HIGH, item H6: unit 7's new ask door grades its argument mapping and not the row it writes, so a newline or separator in --text injects ungraded BACKLOG rows past the refuse default; repairs TOOL-dTotalRecall-7

2026-10-25T23:39:26Z rescope · item add TOOL-dTotalRecall-42 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) id 51 HIGH, item H7: unit 11's shape-run home is the whole build folder, so the record-kinds check misgrades every build record or reds the empty home at its landing; repairs TOOL-dTotalRecall-11

2026-10-25T23:39:26Z rescope · item add TOOL-dTotalRecall-43 · reason spec-audit round 1 (reviews/2026-10-26-review-dTotalRecall-spec-audit-round1.md) the 59 confirmed minors batched into one unit: 46 MEDIUM, ids 2 3 4 5 6 7 8 9 10 11 12 13 18 19 24 25 26 27 28 29 30 31 32 33 37 38 39 40 41 42 43 44 45 46 48 50 52 53 56 57 58 60 62 63 64 65 (items M1 to M44), and 13 LOW, ids 15 20 21 22 34 35 47 54 55 59 66 67 68 (items L1 to L13); lands on several units, so repairs no unit in particular

2026-10-26T00:02:54Z review · item dTotalRecall-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 7 · minors 59 · disposition promote

2026-10-26T00:57:52Z rescope · item add TOOL-dTotalRecall-44 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 1 HIGH, item H1 shared with id 35: unit 38's split census keys on the value's name, so it cannot list check-recall.py:511 or gen_build_index.py:4073 and its AC2 is red by construction; repairs TOOL-dTotalRecall-38

2026-10-26T00:57:52Z rescope · item add TOOL-dTotalRecall-45 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 35 HIGH, item H1 shared with id 1: unit 38's census and AC3 grep miss single-quoted and tree-wide id splits, so branch_reconcile.py:520, row_grammar.py:1116 and gen_build_index.py:8576 still split under the hyphenated slug; repairs TOOL-dTotalRecall-38

2026-10-26T00:57:53Z rescope · item add TOOL-dTotalRecall-46 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 22 HIGH, item H3: unit 38's parse_id_parts reads named groups ID_RE does not have and int() a seq the grammar admits with a suffix; repairs TOOL-dTotalRecall-38

2026-10-26T00:57:54Z rescope · item add TOOL-dTotalRecall-47 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 3 HIGH, item H2: unit 36 is ordered after unit 19's causes leg and backfills only at its own pass base, so the records of 19, 21 and 39 written after the seed stay causeless; repairs TOOL-dTotalRecall-36

2026-10-26T00:57:54Z rescope · item add TOOL-dTotalRecall-48 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 30 HIGH, item H4: unit 36 puts the run record's cause line where runlog's fixed six-line head requires a blank line; repairs TOOL-dTotalRecall-36

2026-10-26T00:57:55Z rescope · item add TOOL-dTotalRecall-49 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 31 HIGH, item H5: unit 36's VIEW_HEAD cause line breaks byte parity with the pinned asbuilt.py instrument and rewrites a legacy view; repairs TOOL-dTotalRecall-36

2026-10-26T00:57:56Z rescope · item add TOOL-dTotalRecall-50 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 32 HIGH, item H6: unit 36 misses the pinned deviations.py departures writer the close runs, so the close's departures record reds the causes leg; repairs TOOL-dTotalRecall-36

2026-10-26T00:57:57Z rescope · item add TOOL-dTotalRecall-51 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 40 HIGH, item H7: unit 36 gives a non-markdown record no cause form and its backfill writes a bare markdown line into a script record; repairs TOOL-dTotalRecall-36

2026-10-26T00:57:57Z rescope · item add TOOL-dTotalRecall-52 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) id 37 HIGH, item H8: unit 43 S19 merges two legacy ledgers on a key that collides, through a shrink-only rule that refuses it, and leaves the retired name's carriers; repairs TOOL-dTotalRecall-43

2026-10-26T00:58:02Z rescope · item add TOOL-dTotalRecall-53 · reason spec-audit round 1 of units 36 to 43 (reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) the 41 confirmed minors batched into one unit: 24 MEDIUM, ids 2 5 6 7 8 9 13 14 15 17 18 19 23 25 27 28 36 38 41 42 45 49 50 51 (items M1 to M17), and 17 LOW, ids 4 10 11 12 16 20 21 24 26 29 33 34 39 43 46 47 52 (items L1 to L16); lands on several units, so repairs no unit in particular

2026-10-26T01:17:29Z review · item dTotalRecall-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 9 · minors 41 · disposition promote

2026-10-26T02:12:38Z rescope · item add TOOL-dTotalRecall-54 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 1 HIGH, item H2: unit 46 repairs unit 38's parse_id_parts after unit 38's own order-8 pass needs it, so every call there raises IndexError; repairs TOOL-dTotalRecall-5, landing the working parser in step 8 ahead of unit 38's re-points

2026-10-26T02:12:49Z rescope · item add TOOL-dTotalRecall-55 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 37 HIGH, item H1 shared with ids 4, 15 and 24: unit 53 S34 retires CAUSE_WRITER_KEPT with no keep path for unit 50's eight build-folder scripts, which no pass of this build may edit; repairs TOOL-dTotalRecall-53

2026-10-26T02:12:50Z rescope · item add TOOL-dTotalRecall-56 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 15 HIGH, item H1 shared with ids 4, 24 and 37: unit 53 S22 keeps the pinned deviations.py compare by an in-file marker, which would move a pinned blob outside the build's write set; repairs TOOL-dTotalRecall-53

2026-10-26T02:12:50Z rescope · item add TOOL-dTotalRecall-57 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 4 HIGH, item H1 shared with ids 15, 24 and 37: unit 53 AC34 reds every file-keyed exemption and S34 exempts no pinned file, so a file that cannot carry the marker has no lawful keep; repairs TOOL-dTotalRecall-53

2026-10-26T02:12:51Z rescope · item add TOOL-dTotalRecall-58 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 24 HIGH, item H1 shared with ids 4, 15 and 37: built as written, unit 53's pass writes markers into pinned instruments and stops at packet.py --check, or cannot keep them; repairs TOOL-dTotalRecall-53

2026-10-26T02:12:51Z rescope · item add TOOL-dTotalRecall-59 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) id 13 HIGH, item H3: unit 52's gained refusal and absorbs read cannot arise at this run's compare base, where neither legacy home exists; repairs TOOL-dTotalRecall-52

2026-10-26T02:12:52Z rescope · item add TOOL-dTotalRecall-60 · reason spec-audit round 1 of units 44 to 53 (reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) the 35 confirmed minors batched into one unit: 26 MEDIUM, ids 2 3 5 6 7 8 12 14 16 17 18 19 20 21 25 26 27 29 30 32 33 38 39 40 42 44 (items M1 to M21), and 9 LOW, ids 9 10 11 22 23 31 34 35 36 (items L1 to L8); lands on several units, so repairs no unit in particular

2026-10-26T02:27:23Z review · item dTotalRecall-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 35 · disposition promote

2026-10-26T03:24:15Z rescope · item add TOOL-dTotalRecall-61 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) id 1 HIGH, item H1: units 55 to 58 repair unit 53 but are ordered after its pass, so unit 53 retires the file-keyed keeps before their path-keyed home exists and its AC22, AC28, AC34 and AC35 are red at its own tip; repairs TOOL-dTotalRecall-50, the hand-off from its eight build-folder rows to unit 53's retirement, landing at step 19 ahead of unit 53's pass

2026-10-26T03:24:25Z rescope · item add TOOL-dTotalRecall-62 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) id 2 HIGH, item H2: unit 59 repairs unit 52 after unit 52's own pass, so unit 52's AC2 reads a first seed and its AC3 finds the absorbs line it wrote, both red at step 28; repairs TOOL-dTotalRecall-43, amending unit 52, the unit that carries 43's merge, in step 28 ahead of its pass

2026-10-26T03:24:26Z rescope · item add TOOL-dTotalRecall-63 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) id 3 HIGH, item H3 shared with id 22: unit 54 says unit 46 builds nothing it built while unit 46's spec still rebuilds parse_id_parts, and nothing observes unit 54's body at unit 46's pass; repairs TOOL-dTotalRecall-54

2026-10-26T03:24:27Z rescope · item add TOOL-dTotalRecall-64 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) id 22 HIGH, item H3 shared with id 3: unit 46's spec still rebuilds parse_id_parts on tree_lib._id_alternation with a read_root_conf that does not exist, the read unit 54 rejects; repairs TOOL-dTotalRecall-54

2026-10-26T03:24:27Z rescope · item add TOOL-dTotalRecall-65 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) id 27 HIGH, item H4: CENSUS_KEPT_PATHS ships gov-only build-script paths in tree_lib.py, engine bytes every adopter installs; repairs TOOL-dTotalRecall-55

2026-10-26T03:24:28Z rescope · item add TOOL-dTotalRecall-66 · reason spec-audit round 1 of units 54 to 60 (reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) the 40 confirmed minors batched into one unit: 27 MEDIUM, ids 4 5 6 7 8 12 13 14 15 16 24 25 28 31 32 33 34 37 39 40 41 42 43 44 45 46 47 (items M1 to M21), and 13 LOW, ids 9 10 11 18 19 20 21 23 29 35 38 48 50 (items L1 to L11); lands on several units, so repairs no unit in particular

2026-10-26T03:42:08Z review · item dTotalRecall-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 5 · minors 40 · disposition promote

2026-10-26T04:24:48Z rescope · item add TOOL-dTotalRecall-67 · reason spec-audit round 1 of units 61 to 66 (reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) id 1 HIGH, item H1 alone: unit 61's AC1 is green before its pass because the hands-off fold already wrote a section-9 line naming unit 61 into units 55, 56 and 57, so their amendments go unobserved; repairs TOOL-dTotalRecall-61, landing at step 20 ahead of the order-30 passes

2026-10-26T04:24:49Z rescope · item add TOOL-dTotalRecall-68 · reason spec-audit round 1 of units 61 to 66 (reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) id 16 HIGH, item H2 alone: unit 65's keep registry is a memory/project txt file with no [[ledger]] registration and its own hand parser, so no shrink-only ratchet grades a keep added later; repairs TOOL-dTotalRecall-65

2026-10-26T04:24:49Z rescope · item add TOOL-dTotalRecall-69 · reason spec-audit round 1 of units 61 to 66 (reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) id 21 HIGH, item H3 alone: unit 65 edits .memory-tree.conf, a watched file, after unit 60's last-audit re-stamp, so the kickoff-manifest ratchet leg is red from step 31 to the close; repairs TOOL-dTotalRecall-65

2026-10-26T04:24:50Z rescope · item add TOOL-dTotalRecall-70 · reason spec-audit round 1 of units 61 to 66 (reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) the 25 confirmed minors batched into one unit: 23 MEDIUM, ids 2 3 4 5 6 9 10 11 12 13 14 17 18 22 24 25 26 27 28 29 30 31 32 (items M1 to M17), and 2 LOW, ids 8 33 (items L1 and L2); lands on several units, so repairs no unit in particular

2026-10-26T04:39:22Z review · item dTotalRecall-spec-set-r5 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 3 · minors 25 · disposition promote

2026-10-26T05:15:12Z review · item dTotalRecall-spec-set-r6 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 4 · minors 23 · disposition promote

2026-10-26T05:22:41Z rescope · item add TOOL-dTotalRecall-71 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) id 23 BLOCKER, item B1: unit 67's probe double-quotes the backticked edge string, so AC1's edge row is green whether or not unit 57's edge to unit 56 exists; repairs TOOL-dTotalRecall-67, landing at step 21 ahead of unit 57's order-30 pass

2026-10-26T05:22:42Z rescope · item add TOOL-dTotalRecall-72 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) id 10 HIGH, item H2: the same double-quote probe defect, by which unit 67's S1 reads unit 57's edge as present and its S2 never writes it; repairs TOOL-dTotalRecall-67, landing at step 21 ahead of unit 57's order-30 pass

2026-10-26T05:22:42Z rescope · item add TOOL-dTotalRecall-73 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) id 5 HIGH, item H1: unit 68's literal registration home and unit 65's conf-derived path give the census and its base compare two answers to where the registry lives; repairs TOOL-dTotalRecall-68

2026-10-26T05:22:43Z rescope · item add TOOL-dTotalRecall-74 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) id 11 HIGH, item H3: unit 70 reuses the double-quote probe on its backticked strings, so its absorbs row is green before unit 62's amendment exists; repairs TOOL-dTotalRecall-70

2026-10-26T05:22:44Z rescope · item add TOOL-dTotalRecall-75 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) id 17 HIGH, item H4: unit 69 re-stamps last-audit for manifest-check C5 and never advances last-body-change, so C9 keeps the ratchet leg red and its AC2 cannot pass; repairs TOOL-dTotalRecall-69

2026-10-26T05:22:45Z rescope · item add TOOL-dTotalRecall-76 · reason spec-audit round 1 of units 67 to 70 (reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) the 23 confirmed minors batched into one unit: 16 MEDIUM, ids 1 2 3 4 6 12 13 18 19 20 21 26 27 29 30 31 (items M1 to M15), and 7 LOW, ids 7 8 9 15 16 25 28 (items L1 to L7); lands on several units, so repairs no unit in particular
