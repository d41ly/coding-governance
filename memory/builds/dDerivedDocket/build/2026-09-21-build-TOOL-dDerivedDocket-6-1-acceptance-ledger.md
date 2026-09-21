**Serves:** journal TOOL-dDerivedDocket-6

# TOOL-dDerivedDocket-6 — acceptance ledger

Every observation below was made in the build pass, by a DIRECT check: the new module's own
`--selftest` over in-memory fixtures, the generator's `--selftest` over a scratch fixture spec, and
a read of the tree. No gate leg, no merge bar and no self-test suite ran in this pass. No criterion
of this unit carries a `permission:` line, so nothing here is owed to the post-build bar — AC3's
extra line is a COST note, and rev-4 records that its flag run stays in the pass.

Every criterion's Red-when was STAGED and observed RED before this ledger was written; the breaks
are named per line. Two of them found arms that could not fail and three arms were added; the
rev-5 revision entry records which.

**Evidences:** TOOL-dDerivedDocket-6

- AC1 — `backlog.py --selftest` — a fixture holding one of every row shape returns 7 asks and 8 rows
  with no verdict, and the same walk over a clean file reports none at all (the control). A
  continuation line, a row above `## Asks`, an ask row under `## Dispositions` and a file holding
  only its H1 each yield V2 naming the file and the line. RED observed by making the walk skip an
  unrecognised row instead of reporting it: four arms failed, including both V5 arms.
- AC2 — `extract.anchor_at` — resolved from the memory-recall kit at this tree's real install
  prefix, NOT a local copy, and the arm did not skip. The ask row anchors its id; the CLOSED, SEV,
  REOPEN and RELOCATED rows each anchor nothing. Every renderer's output parses back to the class it
  was rendered from, and the ask round trip keeps the `unit` marker and the pointer. RED observed by
  making the ask renderer stop leading with the id: 54 arms failed, that one among them.
- AC3 — `python3 tools/memory-tree/gen_build_index.py --selftest` — fixture headers carrying
  `closes EXMP-aFoo-2..4` and `advances EXMP-cBaz-3` produce the expanded lists on the unit record;
  `closes 2x`, a second `closes`, one id under both verbs, and a `closes` with no value each refuse
  naming the fixture file. The DARK arm sits first: a header carrying neither verb returns two empty
  lists. RED observed by dropping the bad-token refusal: the malformed-value arm failed. Measured
  cost of the whole flag run on node d: 7.1 s.
- AC4 — `backlog.py --selftest` — one fixture per rule R1 to R7, each deriving that rule's token
  with its Decided-by naming the evidence. A CLOSED row beats a live closing spec; CLOSED beats
  WONTDO; a BLOCKED hold on a CLOSED target and a DEFERRED hold whose `until` target folds CLOSED
  both release to OPEN; a hold on a target that is neither a filed ask nor a spec H1 renders
  `UNRESOLVED` beside V6; two live asks each BLOCKED on the other both derive BLOCKED while V6 names
  the cycle. RED observed twice: dropping `has a live target` failed both release arms, and
  evaluating stratum 1 live-first failed three including the CLOSED-beats-live one.
- AC5 — `unit` — a non-`unit` ask whose only closing spec reads WONTDO stays OPEN; a `unit` ask
  whose same-id spec reads WONTDO derives WONTDO, and one whose same-id spec reads CLOSED derives
  CLOSED. RED observed by letting a WONTDO spec in C(A) decline its ask: the non-`unit` arm failed.
- AC6 — `of` — a REOPEN naming the closing spec leaves the ask live; a second CLOSED row citing the
  same evidence stays cancelled; a CLOSED row by a new sha re-closes it; a REOPEN naming a folder
  slug cancels that folder's WONTDO from another file; a REOPEN whose `of` names nothing closing its
  target yields V11. RED observed by making a REOPEN cancel every closing record rather than the one
  it names: the re-close arm failed.
- AC7 — `backlog.py --selftest` — 432 permutations of two files' order and of the row order inside
  each fold to exactly 1 distinct result, over statuses, Decided-by and severities together. A
  second arm names the closing evidence for an ask carrying TWO closing records in two files. RED
  observed by naming `closers[-1]` instead of the sorted minimum, which the permutation arm alone
  could not see — the corpus then closed one ask with one record, a population of one.
- AC8 — `HIGH` — an ask with a `HIGH` row in one file and a `LOW` row in another reads `HIGH`, and
  one with no SEV row reads `unlabelled`. RED observed by making the last-read row win. The fixture
  was REORDERED first: with `LOW` read before `HIGH` the same break passed this arm by coincidence
  of file order, and only the permutation arm caught it.
- AC9 — `WITHDRAWN` — the legacy reader returns id and status for an id-first row, a status-first
  row, a ` - ` separated row and a `CLOSED by deletion (…)` slot, keeping that slot's evidence prose
  in the body; `WITHDRAWN` folds to WONTDO with the `withdrawn` flag. A prose line, an unkeyable
  list row and a row whose token is not a legacy status each return nothing WITH their reason. RED
  observed by returning an unreadable row as OPEN.
- AC10 — `backlog.py --selftest` — V1 to V12, V15 and V16 each staged into an otherwise clean
  fixture and each reported ALONE, with the clean fixture reporting none. V1 names the folder and
  the id's slug; V3 names both files and both builds; V9 names the ask's file and the spec's. A
  CLOSED row `by` a sha is shape-checked only and is not V8, and a REOPEN counts as an ask's KEEP so
  V10 does not fire. RED observed at V4 by folding provenance rows back into the per-class rule, and
  at V16 by dropping the zero-padding refusal.
- AC11 — `BACKLOG_MODE` — absent, blank, `shards`, `builds` and `shard` return shards, shards,
  shards, builds and a refusal naming the legal set; `builds` with a blank `ASK_CUTOFF` returns V15,
  with `2026-9-30` returns V16 naming the key, and with `2026-09-30` returns neither. A further arm
  shows the disarming is real: an October ask under the unpadded cutoff reports V16 and NOT V12. RED
  observed by defaulting an unrecognised mode to shards.
- AC12 — `python tools/memory-tree/gen_build_index.py --check` — exits 0 over this tree with the new
  module imported and no header carrying either verb, reporting `clean (773 artifact(s))`. A
  `--write` over a scratch clone carrying this unit's four files rewrote all 773 and left
  `git status --short` empty. RED for this class is `parse_spec` refusing or re-rendering a
  verb-less header, which the AC3 dark arm covers from the other side.

## Caveats a reader should not have to find

- **No kit version moved, deliberately.** `tools/memory-tree/gen_build_index.py` is in
  `check-verdict-epoch.sh`'s delegate set, so this build owes one `KIT_MEMORY_TREE_VERSION` bump —
  and that bump is unit 34's, which the specs already say. A bump here would sit BEHIND later units'
  engine changes and would red that gate on the post-build bar rather than satisfy it.
- **`memory/HYGIENE.md` is untouched**, as section 4 says. The grammar and the fold reach HYGIENE
  and the kit README through the engine and docs units; this unit's module docstring carries them
  meanwhile, together with what the module does NOT check.
- **The AC3 flag run is the pass's most expensive direct check**, measured at 7.1 s on node d. That
  is well inside the per-command bound a pass holds, so rev-4's cost line stands as written and
  nothing was deferred for it.
