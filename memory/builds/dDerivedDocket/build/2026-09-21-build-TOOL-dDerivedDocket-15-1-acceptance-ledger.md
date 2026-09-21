# TOOL-dDerivedDocket-15 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-15

The ask envelope: a clause tail and `SCOPE` rows on the backlog grammar, verdicts V13 and V14, the
READY predicate and its two projections, the `--probe` runner, and the `--new-build` scaffold. The
whole of it lands DARK — this repository is in `shards` mode, so every branch below is reachable
only under `BACKLOG_MODE=builds`, and `--write` over this tree rewrote 773 artifacts while changing
not one tracked byte.

The direct check for every line below is the FLAG form
`python3 tools/memory-tree/gen_build_index.py --selftest`, which AC12's `permission:` line names as
the check this pass may make; what that line defers to the VERIFYING bar is the identical argv's run
as a HELD `chunk = selftests` LEG, not the criterion. The suite went from 342 arms to 417, all
green, and `backlog.py --selftest` is green beside it. No merge bar, no gate leg and no `*.test.sh`
suite ran in this pass.

Fifteen breaks were staged one at a time, each into the source rather than into a fixture, and every
one went red naming the arm written for it. One of them found a defect in the ARMS: the `may none`
absorption arm matched a substring, so a field reading `<grant>,none` contained the value it
asserted and the arm stayed green over its own break. Three arms were bracketed to assert a whole
field after that.

**Evidences:** TOOL-dDerivedDocket-15

- AC1 — `backlog.py` — three arms. The §4 example ask yields its three clauses and its pointer; a
  row whose TEXT ends ` · out ` ahead of the real clauses still yields the real `seen` and `accept`,
  read right to left, and `--check` reports V13 on the empty value the collision left; a clause-free
  legacy row yields the fields unit 6 yielded and no clause. Break B1 (the tail read left to right)
  redded sixteen arms including all four.
- AC2 — `gen_build_index.py --asks --tsv` — a SCOPE row's `accept` cures an ask the ask row left
  unaccepted and the fold still reads OPEN; `--asks <id>` prints both merged `accept` values; a
  SCOPE row's `may none` is absorbed and leaves the grant unchanged. Break B8 (absorption removed)
  redded the third.
- AC3 — `gen_build_index.py --check` — one tree carrying a bare line number, a doubled label, a
  SCOPE row targeting an unfiled id and a second SCOPE row for one target names V13 four times and
  exits 1, each finding naming its file and row. Breaks B2 and B3 redded the first two findings, and
  B7 redded the arm holding V7 off the unfiled target.
- AC4 — `ASK_CUTOFF` — five asks filed ON the cutoff and one the day before: V14 names the two
  carrying neither `accept` nor a `seen … run`, and the SCOPE-cured one, the accepted one, the
  runnable one and the day-before control all pass. Moving the cutoff past every ask disarms it.
  Break B4 (V14 reading the ask row's own clauses) redded the first.
- AC5 — `gen_build_index.py --asks --tsv --ready` — eleven ids over one mandate, every row's grade
  and failing rules pinned by name. The `-N` continuation carried the mandate. Break B5 (`legacy`
  granted with both R4 and R5 failing) redded it. AMENDED rev-8 entry 2: the UNFILED id's `missing`
  is `R1,R2,R4,R5` and not `R1` alone, because all six rules are graded; the id with TWO rows fails
  `R1` and nothing else, and that is the half asserted exactly.
- AC6 — `--live-builds` — a live closing spec in another build refuses R2; omitting that build from
  `--live-builds` admits it and names it `stale:`; `--target` naming it admits it unprefixed; a
  terminal ask fails R2 and nothing else; a `unit` ask of the `--target` folder is admitted while
  its non-`unit` neighbour under the same option stays refused. Break B6 redded two of them.
- AC7 — `examined` — the whole of stdout over the three-ask fixture is three eleven-field rows and
  the closing line, every cell pinned position by position, with the waiver notice on stderr; an
  all-`no` fixture and an empty `--ready` both exit 0. Break B9 (one field emitted empty) redded
  eight arms.
- AC8 — `git status --porcelain` — a row filed after the pin is not filed at the pin, the same id is
  ready in the working tree, the conf is pinned too, and the porcelain is unchanged across both the
  `--at` run and a `--tsv --ready --target --live-builds` one. Break B10 (`--at` reading the working
  tree) redded two.
- AC9 — `PROBE_ALLOW` — blank refuses and names the key; a declared entry that does not match
  refuses and prints what IS declared; token equality refuses `python3x` under `python3` and
  `tools/../x` under `tools/`; a two-token entry admits its own command and refuses the other
  script; a single-token interpreter entry admits arbitrary code, which is stated; a metacharacter
  or a newline refuses before the split; the bound kills a command that outlives it and reports it
  NEVER ANSWERED; two merged `run` values refuse as ambiguous naming both rows. Break B11 (matching
  by string prefix) redded two. AMENDED rev-8 entry 4: the EXECUTING arm names `git --version` and
  the bound arm passes an argv tuple, because an interpreter path resolved on a Windows node carries
  a byte the metachar ban refuses; every matching arm still names `python3`, `python3x`, `p.py` and
  `q.py`.
- AC10 — `gen_build_index.py --new-build <slug> --asks` — the mandate `EXMP-aFoo-3 -4` scaffolds a
  README whose `asks:` reads `EXMP-aFoo-3..4`, carrying `authorized-by: slug`, `status: OPEN` and a
  bound contract row, and `--check` and `--check-format` both exit 0 over the tree it left. A
  twenty-five-ask mandate wraps: every measured line stays at or under
  `BUILD_README_ENTRY_CAP_CHARS`, read out of the hygiene engine rather than typed. Breaks B12 and
  B14 redded them. AMENDED rev-8 entry 1: `ids:` is asserted as the RENDER's line, present and
  empty, because no id carries a slug minted one command ago.
- AC11 — `EXMP-aFoo-3...5` — the elision, an unfiled id, a slug the probes find and an all-`no`
  mandate each exit non-zero with no build folder written, and the readiness table prints before the
  refusal; a mandate over a granted ask still scaffolds a README with no `may:` line. Break B15
  (matching the elision only as a whole token) redded it.
- AC12 — `python3 tools/memory-tree/gen_build_index.py --selftest` — 417 arms, all green, with the
  fifteen staged REDs above. Its run as a HELD gate leg is the VERIFYING bar's and is not this
  pass's.
- AC13 — `corpus_ids.resolve_anchor(root)` — no line the scaffold wrote anchors an id, over a tree
  that HAS those ids, through this kit's own route bound to the scratch root; the same predicate
  over the same root answers the `- EXMP-aFoo-3 — the ask` break line. Break B13, which leads a
  generated slot bullet with an id, redded the negative arm. AMENDED rev-8 entry 14: the fixture is
  the scaffold's own, whose scratch conf declares the example family outright, rather than
  `_fixture(tmp, example_family=True)`.
