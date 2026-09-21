**Serves:** journal TOOL-dDerivedDocket-7

# TOOL-dDerivedDocket-7 — acceptance ledger

Every line below was observed in the build pass, by the direct check the criterion names: the
generator's own `--selftest` flag over builds-mode fixture trees, plus the pass's mandated
regeneration run over this repo. No merge bar, no suite file and no gate leg ran in the pass.

**Evidences:** TOOL-dDerivedDocket-7

- AC1 — `*No live ask.*` — the selftest's builds-mode fixture declares four families and files asks
  in three folders across two of them. `plan()` returns exactly
  `memory/backlog/{EXMP,FRTH,OTHR,THRD}.md`; `THRD` and `FRTH` carry the empty case; each of the
  five live asks appears once across the four views, counted rather than eyeballed. The cost line's
  other half is discharged too: each new arm's RED was observed by hand, by staging eight breaks
  into the renderer, the guard, the reporter, the roster skip, the stream discipline and the conf
  reader one at a time and reverting each. All eight went red. One of them found a defect in the
  arms themselves, recorded below.
- AC2 — `extract.anchor_at` — every line of every rendered view is run through the real function
  from the memory-recall kit, bound by `grammar_for` to the FIXTURE's root rather than to this
  repo's, so the fixture's own families are in the grammar and an empty answer cannot come from a
  grammar that recognises nothing. None of the lines anchors an id and none opens with a list
  marker. The arm carries its own control: the same function and the same grammar DO anchor a
  bare-id first cell, which is what the link wrapper exists to prevent. An unavailable kit is a
  named SKIP that also fails the leg, never a silent pass.
- AC3 — `tools/` — the view header is rendered with a synthetic kit prefix and a synthetic header
  line, and every line of `render_relocation_recipe` appears in it quoted, byte for byte, with no
  literal of this install anywhere in the output. The data-loss guard's message is compared against
  the same constant rendered at this install's derived prefix. An empty prefix refuses rather than
  rendering a command that cannot run.
- AC4 — `--check` — the arm loop iterates `backlog.VERDICT_CODES`, the tuple the parser module
  exports, and stages a builds-mode fixture for each of the fourteen. `--check` names each code and
  exits 1; `--write` over the same tree writes every artifact and exits 0, because a render is not a
  verdict.
- AC5 — `--relocate` — an authored dash row appended to a rendered view: `--write` exits 1, that
  view is byte-identical to what was on disk, `memory/backlog/OTHR.md` is still written, and the
  message names the offending line and all three entry points. `--check` names the same line and
  prints no DRIFT header at all, so the `--write` remedy is never offered against it.
- AC6 — `--check` — a shards-mode fixture tracking one `BACKLOG.md` exits 1 naming V18 and the
  file; a second fixture whose only half-migration is a status header carrying `closes` exits 1
  naming V18 and the spec.
- AC7 — `--check` — a builds-mode fixture tracking `memory/archive/EXMP.2026-01.md` exits 1 naming
  V19 and that path, while `memory/archive/DECISIONS.2026-01.md` sits beside it in the same fixture
  and appears nowhere in the output.
- AC8 — `BACKLOG.md` — the fixture's `aHome` folder holds one tracked file of that name and no
  README. Its ask renders in the OTHR view, and the slug appears in neither `memory/LIVE.md` nor
  `memory/ledger/2026-09.md`. The same corpus in shards mode still raises the no-README refusal
  verbatim.
- AC9 — `ids:` — the same corpus rendered in both modes yields identical front-matter id lines for
  every build README. The roster half is observed directly on `rosters()`: over a fixture whose
  `memory/backlog/EXMP.md` names an id nothing else names, the builds-mode scan does not see it and
  the shards-mode scan does, which is the control that keeps the first half from passing vacuously.
- AC10 — `--check` — the builds-mode fixture prints
  `backlog 6 ask(s) · 1 row(s) · 0 link(s) in 3 file(s) · 5 live · 0 verdict(s)`, every figure
  derived at run time and every one matching the fixture by hand. On this repo's shards tree the
  pass's `--write` run printed the shards announcement with zero mode verdicts, which is the second
  half of this criterion observed on the tree it names.
- AC11 — `--status` — `--asks EXMP-aFoo-3` prints the terminal ask's CLOSED status and the evidence
  that closed it; `--asks EXMP --all --json` writes nothing, exits 0 and carries `mode`, `examined`
  and all thirteen pinned fields; `--asks --build aBar` prints one row and only that home's. Over a
  fixture holding one BLOCKED and one OPEN ask of the family, `--asks EXMP --status BLOCKED` prints
  the one row at exit 0, and `--status NOPE` prints nothing on stdout, names the token on stderr and
  exits 2.
- AC12 — `BACKLOG_EXCERPT_CHARS` — `0` and `abc` each refuse by name through `plan()`; absent, the
  view renders the wide ask's summary cut at 72; declared at 40, the same ask's cell re-cuts, so the
  key is observed to be read rather than merely accepted.
- AC13 — `--write` — the dark half is observed on this repo: `python tools/memory-tree/gen_build_index.py --write`
  rewrote 773 artifacts and changed not one tracked byte, and the selftest separately asserts that a
  shards render produces no `memory/backlog/` artifact at all. The criterion's `--check` half is the
  same command a gate leg runs over the real tree, so under the build-wide rule this spec's rev-4
  folded it is owed to the one run the main loop makes at `VERIFYING`, not claimed here.
- AC14 — `--write` — an authored shard with no generator header at a view path: `--write` exits 1,
  the file is byte-unchanged, every other artifact is written, and the message names its id-leading
  line. The guard never consults the view predicate, which is why this file is read at all.
- AC15 — `ASK_CUTOFF` — the code loop's fifteenth and sixteenth iterations assert the key's own name
  appears in the `--check` output beside the code, so the conf verdicts are reported rather than
  returned into silence.
- AC16 — `--write` — a conflict region whose two sides are adjacent view rows: exit 0, the announcement
  `re-rendered over a view conflict`, and the view equal byte for byte to a fresh render. With one
  side replaced by an id-leading list row the same fixture exits 1 and the guard names that line.
- AC17 — `json.loads` — over a fixture carrying a waived corrupt header and a fold verdict,
  `json.loads` succeeds over the whole of stdout at exit 0, and the tolerated-header line is found on
  stderr and not on stdout. Over a fixture whose front matter `collect()` refuses, the exit is 1,
  stdout is empty and the refusal is on stderr.
- AC18 — `BACKLOG_EXCERPT_CHARS` — the EXMP view lists `-2` before `-10`, omits the CLOSED ask, and
  renders the wide ask's cell as
  `| a / pipe, a deep/path/to/a/file.py token and a linked thing followed by… |` — the pipe folded,
  the backticks gone, the link reduced to its text and the cut taken at a space.

## What the staged breaks found

The V-code arm was satisfied by its own failure message. On a miss it returned
`NO ARM FOR V7 rc=1 :: …`, which CONTAINS the string `V7 rc=1` the arm was asserting, so dropping a
code from the reporter left the leg green. Staging that break is what found it, and the arm now
returns a failure text that shares nothing with what it wants. The other seven breaks went red
first time.

## What this ledger does not evidence

AC13's `--check` half, and nothing else. The observation is `gen_build_index.py --check` over this
repository, which is a gate leg's own command over the real tree; the build-wide rule keeps that in
the `VERIFYING` run rather than in a unit pass. The pass's own pre-commit hook exercises the same
path on the commit that carries this record, which is evidence but is not the criterion.
