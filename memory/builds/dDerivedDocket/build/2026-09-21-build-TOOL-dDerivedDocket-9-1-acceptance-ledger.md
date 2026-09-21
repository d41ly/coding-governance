# TOOL-dDerivedDocket-9 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-9

Hygiene check 25, its module, its commit-time carrier and its arms suite. AC1, AC10, AC16 and AC17
each carry a `permission:` line deferring an observation to a run the main loop makes after the last
unit is terminal; those get no line here and the orchestrator writes them after that run. Everything
below was observed in this pass, against a scratch fixture repository or a staged break. No merge
bar, no gate leg and no `*.test.sh` suite was run: the arms were exercised by hand, as the fixture
runs their criteria describe.

**Evidences:** TOOL-dDerivedDocket-9
- AC2 — `transition_audit.py` — over the F1 fixture, two `RELOCATED` rows for one entry exit 1 and
  the verdict names both `aFlip/BACKLOG.md` and `aSecond/BACKLOG.md`; a row whose sha is `0000000`
  exits 1 as unaccounted, and reverting it restores the accounting at exit 0. Staged RED: with the
  sha half of the match deleted so accounting keys on the id alone, the mis-keyed row certifies the
  change and the arm reds.
- AC3 — `git merge --squash` — four fixtures of the same two branches. Merging the straggler into
  the switched default and merging the default into the straggler each report
  `transitions examined 1`; the squash fixture and the rebase-then-fast-forward fixture each report
  `transitions examined 0`, and the arms assert exactly that rather than only the positive half.
- AC4 — `RELOCATED` — three shapes. A criss-cross whose row version at `ours` equals one of two
  merge bases yields no entry from `delta`. A row deleted from the shard with no archive holding it
  is reported with the `removed` kind. And a straggler that rotates its decision log and a
  family-named backlog archive in ONE commit contributes entries for the family archive's id and
  none for any id anchored in the rotated log. Staged RED, and taken first: with the archive half of
  the watched set widened to the whole of `<MEMORY_ROOT>/archive/`, the rotation arm reds naming the
  decision id — which is the reason the arm is written against a fixture that actually holds a
  rotated log.
- AC5 — `transitions examined` — the hygiene engine, run inside two scratch fixtures. On the
  shards-mode fixture it prints check 25's dormant line and prints no other check 25 line at all; on
  the builds-mode fixture it prints the liveness line with `transitions examined 1`. The engine's own
  overall verdict is deliberately not asserted: a scratch tree is not a conforming memory tree, and
  check 25's line prefix is exactly the delegation being graded.
- AC6 — `transitions examined 0` — all four branches. A conf reader staged to call every blob
  `shards` exits 2 as a DEAD PROBE; a `git clone --depth 1` of the builds-mode fixture exits 2 as a
  DEAD PROBE naming SHALLOW; a boundary detector staged to answer nothing exits 2 as a DEAD PROBE;
  and a linear-flip fixture with no merge at all exits 0 printing `transitions examined 0`, which is
  the case design A3's rule would have redded.
- AC7 — `transition-audit.txt` — `transition_audit.py --pin` prints `<merge> accounted` for the
  unpinned transition and the registry file does not exist afterwards. A registry listing a sha this
  history does not hold exits 1 naming STALE PIN; the same registry naming the live transition exits
  0.
- AC8 — `commit-msg` — the tracked hook, wired into a fixture through `core.hooksPath`. An ordinary
  non-merge commit produces no output at all. A clean `git merge --no-ff` is refused, which is the
  half `pre-commit` cannot reach. A conflicted merge resolved and concluded by `git commit` is
  refused too.
- AC9 — `CACHE_EPOCH` — two `--report` runs over an unchanged fixture: the second reads
  `cache hits 1` against `transitions examined 1`. Rewriting the cache file's epoch to a foreign
  value makes the next run print `check 25 cache recomputed 1 (foreign epoch)` and drop to
  `cache hits 0`.
- AC11 — `accounted(entries, tip)` — called as functions, from the arms, with no merge between the
  two tips. `delta(strag, flip)` returns the id, kind and change commit that `--report` lists for the
  merge of the same two commits once that merge is made, compared as text. `accounted` returns every
  entry accounted over a tip carrying one `RELOCATED` row per entry while HEAD lacks them, and none
  accounted the other way round. Staged RED: binding `accounted` to HEAD instead of its `tip`
  argument reds both directions.
- AC12 — `--expect-builds` — the fixture's HEAD and the named tip differ in exactly their
  `RELOCATED` rows. `--at` over the accounted tip exits 0 while HEAD is unaccounted; checked out at
  the accounted commit, `--at` over the unaccounted tip exits 1; the same fixture with no `--at`
  exits 1; and without the flag the liveness line ends `reader cross-check not run`.
- AC13 — `--no-replace-objects` — a `git replace --graft` ref re-parenting the merge as a non-merge
  commit, and an inherited `GIT_GRAFT_FILE` doing the same, each leave the audit still naming the
  merge. Both halves carry their own liveness assertion, because the first cut of both was vacuous:
  the arm now asserts the replace ref exists and that the graft file re-parents the merge for git
  itself. Staged RED: with the two pins removed from the module, both halves red.
- AC14 — amended rev-7 — `transition_audit.py --report` lists the straggler's own row change and no
  entry for the row it took across from the default side. The criterion's fixture is amended from a
  MERGE to a CHERRY-PICK and rev-7's §9 entry records why: a merged commit is a common ancestor, so
  `merge-base --all` returns it and S4's every-base comparison already excludes the row — measured,
  the merge-shaped fixture stayed green with the A6 clause deleted, and the cherry-picked one reds.
- AC15 — `install the memory-recall kit` — a builds-mode fixture with the recall kit deleted exits 1
  naming `memory-recall`, both paths it looked in, that there is no degraded mode, and the remedy
  line. A shards-mode fixture with the same kit deleted prints the dormant line and exits 0. This
  arm found the defect rev-7 records: with the delta cache warm, a lazy import never fired and the
  refusal never happened, so the resolution is now eager.
