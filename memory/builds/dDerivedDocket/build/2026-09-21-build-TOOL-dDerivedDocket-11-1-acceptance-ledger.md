# TOOL-dDerivedDocket-11 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-11

The shards-to-builds migration planner: a new memory-tree module `migrate_backlog.py` carrying
`--plan` and `--selftest`, the census and its copy-choice rule, the same-id and triage worksheets,
the previewed dispositions, the per-id status prediction over the simulated migrated corpus, the
conservation proof, the four records, and the held `backlog migration selftest` leg with its
descriptor claim, its subject pin and its budget row.

NO MERGE BAR, NO GATE LEG AND NO `*.test.sh` SUITE RAN IN THIS PASS. The module's own
`--selftest` is the flag-form direct check the pass makes, which is what §8 F9 bought by holding the
new leg's `ceiling` at the direct-check bound. Every other observation below was made against a
scratch fixture repository with real git history, or by running `--plan` over this tree.

EVERY ARM'S RED WAS OBSERVED, and not by assertion. Nineteen breaks were staged one at a time into a
COPY of the whole kit directory under the run's scratch root — never the tree — and the copy's own
`--selftest` was run against each: copy-choice taking the first copy it meets, the archived-terminal
rule removed, the unreadable-row refusal removed, the two-live-copies blocker removed, the
empty-corpus refusal removed, the whole-token id match reduced to a substring test, F2's two
exclusions removed, the same-id spec admitted as triage evidence, the design-named ids moved into a
module constant, the outside-the-population refusal removed, the unresolvable-hold rule removed,
both of a signed record's missing-cell refusals removed, the conservation refusal removed, a wall
clock in a record name, the repo resolved from the module's own location, the low-overlap flag
pinned false, the evidence class read from equal ids alone, the view size measured over every ask,
and the archive-citation finding dropped. All nineteen went RED, each on the arm named for it. The
assertion FLOOR was observed red too, on the run where the executed count came back one under it.

TWO OF THOSE BREAKS WERE LIVE DEFECTS IN THE FIRST CUT, found by the arms rather than staged into
them: the substring id match (a spec closing `EXMP-aBar-20` read as closing `EXMP-aBar-2`) and a
conservation proof that raised `KeyError` instead of reporting a row that would not parse back. A
third was found by the first real-tree run — `row-names-hold` fired on a bare mention and proposed
BLOCKED for 97 of 334 triage rows — and is folded as rev-6.

**Evidences:** TOOL-dDerivedDocket-11
- AC1 — `migrate_backlog.py --plan` — over the selftest's fixture repository the census counts 31
  row copies across two live shards and two family archives, joins the fixture's wrapped row onto
  one logical row, and chooses the live OPEN copy over an archived TERMINAL one; a second fixture
  adds one row-shaped line that reads as nothing and `--plan` exits 1 naming
  `memory/backlog/OTHR.md:4` with no worksheet written; an id carried only by two archives, one
  CLOSED and one OPEN, resolves to CLOSED under both file orders, the second fixture holding the
  tokens the other way round.
- AC2 — `--plan` — a fixture whose second live shard repeats an id of the first exits 1 with
  `carry TWO live copies` and both `<file>:<line>` pairs on the message.
- AC3 — `specced-in-place` — the fixture's row flipped OPEN to SPECCED in a later commit reads
  `specced-in-place` with a 40-character sha, the row added in its same-id spec's own commit reads
  `born-in-spec-commit` with its sha, and the pair with neither reads `none` with `-`; the pair
  whose row shares no words with its spec's H1 and Goal carries `low_overlap` yes at 0.000 while the
  matching pair carries no.
- AC4 — `row-names-hold` — over the fixture the triage worksheet proposes CLOSED by the sibling spec
  that absorbs the ask, CLOSED by the product commit that names it, `none` with `dead_pointer` set
  for the untracked pointer, and `none` for the ask whose same-id spec reads CLOSED even though that
  spec's own body carries a closing phrase naming it; the ask named only by its filing commit and
  the ask named only by a records-only commit both propose `none`; the ask whose text carries a hold
  phrase naming a live ask proposes that hold; with `--design-named` naming three `EXMP` ids three
  rows read basis `design-named` with evidence `-` and without it none do; an id the option names
  outside the triage population exits 1 naming it; and the CLOSED ask on the finished build is
  absent from the worksheet.
- AC5 — `TRIAGE-ASK` — the fixture's CLOSED, WONTDO, BLOCKED-naming-an-id and DEFERRED-naming-none
  rows predict CLOSED, WONTDO, BLOCKED and DEFERRED, the last with `decided_by` reading the
  placeholder; the BLOCKED row naming only the shorthand `-4` and the one naming a decision id
  nothing files both preview as holds on that placeholder, while `EXMP-aFoo-3` BLOCKED on
  `EXMP-aFoo-2` previews as that hold with `EXMP-aFoo-2` in `decided_by`.
- AC6 — `mirror-closed` — a signed same-id record marking one pair `unit` whose spec reads CLOSED
  makes that id predict CLOSED in class `mirror-closed`; a signed triage record's CLOSED verdict
  predicts CLOSED in class `triaged`; a triage record whose header lacks `Field` is refused by name,
  naming the record and the cell; and a fixture row whose text is exactly `unit` — the one shape the
  renderer and the parser disagree about — exits 1 as a difference no declared normalization
  explains. The five normalizations are counted on every run and printed.
- AC7 — `BACKLOG.md` — under a fixture cap of 400 bytes the census names the over-cap prospective
  ask file with its size; the six README-less slugs of this repo and the fixture's one are listed as
  filing homes; the EXMP view's prospective size grows when the fixture gains one live ask and does
  not move when it gains a terminal one; and the fixture row backticking a family-archive path is
  named with its file and line, with the citation count on the finding's own heading.
- AC8 — `git status --porcelain` — `--plan --record <dir> --record-as EXMP-aFoo-1` run twice over
  one fixture tree writes the same four files, named by the recording grammar with HEAD's commit
  day, each carrying its Serves line, byte-identical between the runs, and porcelain shows nothing
  outside `<dir>`.
- AC9 — `--plan` — run over this repo with no `--record` it exits 0, prints the census summary and
  the liveness line (8 git processes, constant in the census size), and `git status --porcelain`
  taken before and after is byte-identical.
- AC10 — `migrate_backlog.py --selftest` — prints `PASS (70 assertions)` against the module's
  declared floor of 70, in about 6 seconds; `tools/gate-legs.json` carries the new leg with its
  `ceiling` of 300, at the `DIRECT_CHECK_BOUND` the unattended kit's gate-guard suite grades a
  `--selftest` leg against; `tools/memory-tree/kit.toml` declares it as a `[[gate_leg]]`
  beside its four module-selftest siblings; `tools/govkit/subject-pins.tsv` carries its
  `kit`/`selftests` row, regenerated by `python tools/govkit/govkit.py selfcheck --write`, which
  reported 0 problems once the module was staged; and the memory-tree hygiene dossier claims the
  key. The criterion's own `permission:` line defers `bash tools/run-gates/run-selftests.sh --check`
  and `python tools/govkit/govkit.py selfcheck` to the post-build bar, and neither was run here.
- AC11 — `memory/LIVE.md` — one `--plan` run with `--record` naming this build's `build/`
  folder and `--record-as TOOL-dDerivedDocket-11` filed the four records; the triage worksheet's
  334 rows equal the 334
  status-worksheet rows predicting OPEN whose slug has a tracked build README and is absent from
  `memory/LIVE.md`, counted from those two files by a scratch script rather than by the planner's
  own population function. The criterion's `permission:` line defers
  `bash tools/memory-tree/check-memory-hygiene.sh` over the four records to the post-build bar, and
  it was not run here.
- AC12 — `--plan` — the selftest adds a second worktree of the fixture repository detached one
  commit back, where the tip row is absent, and runs `--plan` with the Bash call's own working
  directory inside it: the census reports 30 row copies against the tip's 31, and the distinct-id
  count is exactly one lower.
- AC13 — `MEMORY_ROOT` — a fixture holding the conf and one build README but no shard and no family
  archive exits 1 naming the empty population, with the reason that a proof over nothing proves
  nothing, and files no worksheet.
