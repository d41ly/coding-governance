**Serves:** journal TOOL-dDerivedDocket-34

# TOOL-dDerivedDocket-34 — acceptance ledger

The switch-over, built as one commit, `c4568fe0`: `migrate_backlog.py --write` over the whole
legacy corpus, the four family views rendered into the paths it emptied, builds mode armed, and every
carrier the deletions and the mode switch reach edited in the same commit. The spec moved to rev-11
first, for five divergences its §9 line names; none moves a criterion.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the writer
itself over this tree, `gen_build_index.py --check` and `--asks` on the switched tree, the memory-tree
module's own `--selftest` flag, the recall and drift readings named below, and scratch repositories
built in the pass. Where a criterion's `permission:` line defers its verdict to the one post-build
bar, it has NO line below: the orchestrator writes it after that run.

**The pass journal.** The triage ask is TOOL-dDerivedDocket-66, minted by the orchestrator at this
pass and grep-checked free at `411fac91` before `--write` ran (S17). Rollout step 5's probe loop had
nothing to drop: the triage worksheet header unit 11 recorded reads `design-named none`, so the
re-plan passed no `--design-named` and dropped no id. The re-plan recorded the census and three
worksheets as this unit at `411fac91`, 730 ids and 372 triage asks, and the signer's `--tail switch`
signed them (KEEP 366, CLOSED 5, one T1 exclusion), its `--check` re-deriving both records
byte-identical. The first `--write` REFUSED, writing nothing, on two ids no merge-skipping walk could
date — both rows were born in merge resolutions — which is rev-11's third divergence; the second run
wrote 1368 records into 104 files and removed the four authored shards.

**The straggler inventory (S14), before the write.** `--stragglers --tsv` examined 11 refs against
`main` at `869209ed` and listed four stragglers: this run branch and its remote-tracking copy, a
leftover `worktree-wf_` workflow branch, and `origin/main` itself; `--local` examined 7 and listed the
two local ones. Five remote-tracking refs exist. Report-only, as the owner ruled.

**Readings the post-build bar owns, taken here because only the pass could take them.** The recall
floor BEFORE the switch read `records:fts5:r@5` 0.8333 normalised against 0.81, per-id 12/12, and
AFTER it the same 0.8333 and 12/12 (AC9). `.unattended.conf` now carries `memory/backlog` under
`GENERATED_INDEXES` twice, once per renderer file, and not under `SHARED_RECORDS`;
`scan_shared_index_overlaps` in `tools/unattended/lib-unattended.sh`, sourced and called directly,
prints no pair over the new values and two pairs when `memory/backlog` is staged back into the shared
key (AC8). `bash tools/unattended/check-unattended.sh` ran past its 300-second bound and was stopped
unread. The ask projection read directly shows 454 live asks over 104 files, 731 examined for
`backlog_asks_contested` with 0 counted, 67 closing shas examined for `backlog_evidence_sha` with 0
unresolved, and 454 live asks examined for `backlog_asks_unlabelled`, all 454 unlabelled (AC10). AC21's
three fixture shapes were built with the drift kit's own fixture builder and graded by running
`drift_report.py` over each scratch repository, 14 checks green, not the suite file. The manifest
carries neither BASE string, the two gotchas each open with a shards-mode-only qualification, and the
manifest reads 25591 bytes against 25595 at the parent and 306 lines (AC12); its own check 7 caps it
at 25600, which the rev-11 line records. `git diff HEAD^ HEAD` over the three memory-recall carriers
and `drift_report.py` shows `CACHE_VERSION` 3 to 4, 1.17 to 1.18 on all three carriers, 1.17 being
what `origin/main` advertised after a fetch at this pass and 1.8 the base's, and
`KIT_DRIFT_AUDIT_VERSION` unmoved (AC27).

**Not observed in this pass, and owed.** AC20 cannot be observed now: `origin/main` is still
`869209ed`, an ancestor of HEAD since the second merge, so the landing form of `--ingest` refuses by
its own admission rule (exit 2, naming `--repair`), which a dry run in a scratch worktree of the run
branch confirmed with the run tree's porcelain unchanged. AC15, AC24, AC25 and AC29, the scratch
rehearsal of the landing reconcile with a bare remote, were not built in this pass. The reconcile is
a procedure over verbs other units shipped, and it runs at the landing; those four criteria have no
line below.

**One observation for the record.** The first V13 break was staged on an ask row carrying a pointer
tail and `--check` stayed green: a clause appended after ` → <pointer>` reads as pointer text and is
never graded. The renderer puts clauses before the pointer, so no written row has that shape, but a
hand-edited one could. The break was restaged on a row with no pointer and went red.

**Evidences:** TOOL-dDerivedDocket-34
- AC1 — `python tools/memory-tree/gen_build_index.py --check` — on the switch-over tree exits 0 and
  prints `backlog 731 ask(s) · 638 row(s) · 66 link(s) in 104 file(s) · 454 live · 0 verdict(s)`
  and `clean (954 artifact(s))`, with `DEPL.md`, `KICK.md`, `PLAY.md` and `TOOL.md` rendered as views.
- AC2 — `migrate_backlog.py --write` — prints 730 census ids and 731 ask rows planned, 730 plus the
  triage ask; its own re-read of the written files found one ask row per id and each text equal to its
  normalized legacy text; the counts are status-slot-removed 730, filed-inserted 730, unit-inserted 66,
  wrapped-row-joined 1, relative-link-rebased 0 and archive-citation-unbackticked 5.
- AC3 — `python tools/memory-tree/gen_build_index.py --asks --all --json` — compared with the status
  worksheet `--plan --signed` recorded at `411fac91` over the two switch records: 730 ids compared,
  0 differing, and the two exceptions each on its own line, the WONTDO of S11 and the triage ask
  deriving OPEN; every predicted hold target is in the derived `holds`.
- AC4 — `BACKLOG_MODE="builds"` — is declared beside `ASK_CUTOFF="2026-09-29"`, the day after the
  newest `filed` over every written ask row, 2026-09-28, grepped from the files; `--check` names no
  verdict at all; `python tools/memory-tree/row_grammar.py --emit-pin` prints both pins blank and both
  are declared blank.
- AC5 — `git check-attr merge memory/backlog/TOOL.md` — reads `rows`, and so does
  `memory/builds/dDerivedDocket/BACKLOG.md` through the added line.
- AC11 — `python tools/memory-tree/gen_build_index.py --asks TOOL-aWeighedCompass-3` — prints WONTDO,
  decided by and declined by `dDerivedDocket`, the disposition sitting in this build's own file.
- AC13 — `gen_build_index.py --check` — over the committed switch-over: the moved ask row red V1
  naming the id's slug and the folder it sat in; the authored row appended to the TOOL view made
  `--write` exit 1 leaving the view byte-identical and naming the line and the `--ingest` remedy; the
  removed signed KEEP red V10 naming the ask and its CLOSED build; the malformed `seen` clause red V13
  naming the row. Each removal by checkout was followed by `--check` exiting 0 on a clean tree.
- AC14 — `migrate_backlog.py --stragglers --tsv` — examined 11 refs where `--stragglers --local --tsv`
  examined 7, with five remote-tracking refs listed by `git for-each-ref refs/remotes`.
- AC16 — `grep -c TRIAGE-ASK memory/builds/*/BACKLOG.md` — prints 0 for all 104 files; `--asks` prints
  the triage ask OPEN in this build's file beside its KEEP, and `--asks --all --json` shows five asks
  held on it, the five legacy holds that named no id.
- AC17 — `migrate_backlog.py --selftest` — PASS at 250 assertions, 44 of them the `--write` fixtures:
  eight refusals each graded on exit, message and an unmoved porcelain, the named holds, the zero-hold
  filing, the dry run and the write. Twelve breaks staged one at a time into a copy of the kit each
  went RED on its own arm, and the unbroken copy stayed green.
- AC18 — `python tools/memory-tree/gen_build_index.py --asks --all --json` — 371 signed triage rows
  outside the one exclusion each carry their verdict in this build's `BACKLOG.md`, and no other
  per-build file carries a disposition naming a triage-record id.
- AC19 — `git ls-files memory/backlog` — listed nothing between the write and the render, and the
  render's `gen_build_index.py --write` exited 0 writing all four views.
- AC22 — `memory/DECISIONS.md` — carries one TOOL row keyed by this unit, naming the stance of
  DEPL-dGaugedVintage-13 as superseded and citing design §4.4, in 258 characters.
- AC23 — `(durable home: <n>)` — read 915 before and 917 after; the spine holds 731 documents under
  `memory/builds/*/BACKLOG.md`, and the ten fixture ids that were backlog rows each anchor there.
- AC26 — `git log --format=%ad --date=short -G '^- <id> · ' -- memory/backlog memory/archive` — at the
  switch-over's parent, over 91 ids, every id whose only copy was archived, the one wrapped row and
  twelve others, gives each written `filed`; 0 differing. The two rows born in merge resolutions are
  dated by their merges, which a `-G` log with no `-m` does not list.
- AC28 — `migrate_backlog.py --plan` — in a scratch repository: the step-5 probe with the three
  recorded ids exited 1 naming the first flipped id with the porcelain unchanged, the probe with the
  other two and the recorded run exited 0, whose header and design-named rows name those two, and the
  journal file gained one line naming the dropped id, not leading with it; step 2 in a worktree of the
  second flip exited 1 naming the second id, its recorded run with the third exited 0 naming only that
  id, and the journal gained no line.
