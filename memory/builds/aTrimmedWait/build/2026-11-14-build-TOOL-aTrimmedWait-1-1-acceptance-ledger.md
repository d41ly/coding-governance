# TOOL-aTrimmedWait-1 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-1

No merge bar and no self-test suite ran in this pass. Every observation below was made on node a,
one command at a time with nothing else running, from the worktree root at the pass's tree. The pass
probe is the spec's fenced `u1.sh` block, copied verbatim into the run's scratch directory; its
fixture repository was `$TEMP/u1`. The verdict-unchanged fixture for `--dispatch` itself was a second
scratch repository, `$TEMP/u1d`, holding the same eight specs COMMITTED with a units region per
build: it sourced the parent's driver bytes (`git show HEAD:tools/unattended/unattended.sh`) and
this pass's, stubbed `check_run_state` and `check_chain_dispatch` to reach the spec-file refusals,
and called `verb_dispatch` for tA, tB, tC, tD, tE, tF and both tG units. The two outputs compared
byte-identical under `cmp`: the same six refusal lines and the same tA green past every spec-file
refusal, into the spec-token check the fixture's conf could not satisfy, which is the next gate in
both. The driver suite's new block and the harness suite's new block each ran alone under a stub
carrying the suite's own `same`, `hit` and `miss` (18 and 8 assertions, all passing); the suites
themselves, their floors and each new arm's RED-first observation are owed to the close.

**Evidences:** TOOL-aTrimmedWait-1
- AC1 — `bash "$SCRATCH/u1.sh"` — printed `clean rc 0 hit 1 fails 0`, `thin rc 1 hit 1 fails 1`,
  `order rc 1 hit 1 fails 1`, `edge rc 1 hit 1 fails 1`, `cycle rc 1 hit 1 fails 1` and
  `missing rc 1 hit 1 fails 1`; the probe's whole run took 1m47.128s real.
- AC2 — `bash "$SCRATCH/u1.sh"` — the same run printed `every rc 1 hit 2 fails 2`,
  `nounit rc 1 hit 1 fails 1`, `badslug rc 1 hit 1 fails 1` and `untracked 8`.
- AC3 — `grep -c 'for a unit whose spec grades THIN' tools/unattended/unattended.sh` — printed 1, and
  1 each over `for a unit no tracked spec under this build defines`,
  `a reader taking its numeric prefix`, `Edges block from which no unit id is read` and
  `edges form a cycle, so no unit on it can be dispatched`;
  `grep -cE '(^|[^_[:alnum:]])check_unit_spec "' tools/unattended/unattended.sh` printed 2 and the
  same count over `check_edge_shape "` printed 2. The `--dispatch` fixture above read identical
  refusals at the parent and at this pass; the driver suite's existing arms are the close's.
- AC4 — `time bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7`
  — at the parent `b9ad1f6ba` it printed `UNATTENDED check 14 FAILED — unknown argument` naming
  `--check-specs`, exit 1, `real` 0m6.049s; at this pass it printed the clean line naming the seven
  units, exit 0, `real` 0m9.885s, under the 60 s budget. <!-- PINNED 2026-11-14 -->
- AC5 — `grep -c "' --check-specs ' + slug" tools/workflows/unattended-build.js` — printed 2, and 2
  over `tools/workflows/unattended-build.template.js`;
  `sed -n '/const commitBlock = \[/,/\]\.join/p' tools/workflows/unattended-build.js | git hash-object --stdin`
  printed `c6ca14b74b2441e87eac15e4094dbbccb49cfa6b` before and after the edit. The writer sentence
  sits outside every `roles.specWriter` conditional: the harness block's stub run found it in both
  the untyped and the typed writer's prompt, and a commit double returning `committed: false` threw
  naming its `why`.
- AC6 — `python tools/roles/render_agents.py --check` — exited 0 after `--write`;
  `grep -c -- '--check-specs' .claude/agents/gov-spec-writer.md` printed 1;
  `grep -cE '[a-z-]+/(unattended|check-memory-hygiene)[.]sh' tools/roles/agents/gov-spec-writer.agent.md`
  printed 0.
- AC7 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — printed nothing;
  ``grep -c -- '^- `--check-specs`' memory/guides/UNATTENDED-VERBS.md`` printed 1;
  `bash tools/unattended/unattended.sh --help | grep -c -- '--check-specs'` printed 2;
  `python tools/govkit/docs_leg.py --fingerprints | grep -F 'verb:unattended.sh:--check-specs'`
  printed `verb:unattended.sh:--check-specs 131e24bd help/roles.md`.

## The fix pass, from `2026-11-14-prompt-TOOL-aTrimmedWait-1-fix`, at spec rev-2

Observed on node a, one command at a time with nothing else running, from the worktree root over the
fix pass's tree. No merge bar, no self-test suite and no gate leg ran; what only a gate observes is
named below as the close's.

**Evidences:** TOOL-aTrimmedWait-1
- AC8 — `grep -c 'unattended.sh --check-specs ' tools/unattended/SKILL.template.md` — printed 1, and
  1 over `.claude/skills/unattended/SKILL.md` after `bash tools/unattended/adopt-unattended.sh`
  re-rendered it, the render's diff being that one line; a second render left its blob unchanged,
  `004dc13f8208b72151ce96b1898845934903e10c` both times, which is the comparison
  `bash tools/unattended/adopt-unattended.sh --check` makes, and that leg itself is the close's;
  `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` printed 10628, the figure now on the <!-- PINNED 2026-11-14 -->
  `.claude/skills/unattended/SKILL.md` row of `tools/template-size-limits.txt`, raised from 10580 <!-- PINNED 2026-11-14 -->
  with its `memory/DECISIONS.md` row.
- AC4, re-timed — the same `--check-specs aTrimmedWait` command over the seven units, each driver run
  once from one scratch copy of the kit: the parent's driver `real` 0m5.982s, this pass's 0m6.507s, <!-- PINNED 2026-11-14 -->
  both exit 0 with the clean line; from the worktree path this pass's printed the clean line, exit 0,
  `real` 0m4.448s, under the 60 s budget. <!-- PINNED 2026-11-14 -->
- AC1, AC2 — `bash "$SCRATCH/u1.sh"` — printed the ten lines both criteria name, unchanged:
  `clean rc 0 hit 1 fails 0` through `untracked 8`.
- No verdict moves — `refuse_waive_unless_preflight` now exits itself, so the five
  `|| { RUNLOG_CLEAN=1; exit 1; }` sites at its callers are gone and the four pre-existing pins of
  them are deleted from `memory/project/unarmed-branches.txt`. A fixture ran nine cases through the
  parent's driver and this pass's: `--waive` beside `--plan` (both orders), `--check-specs`,
  `--phase`, `--claims` and `--status`, `--check-specs` with no unit, the seven-unit clean run and an
  unknown flag. Both printed the same check-37, check-14 and clean lines with the same exit codes,
  byte-identical under `cmp` once the scratch copy's own no-`.git` notice on stderr is set aside.
- The pass legs' reds — the three `TW1 AC5` lines spell the driver through `${PFX}${UNATTENDED}`,
  and the TW1 block under a stub of the suite's `same`, `has` and `hasnt_` passed its 8 assertions
  with the suite's own prefix and failed with a wrong one; `cs_mk` is `write_cs_spec`, which
  `python tools/lexicon/lexicon.py --suggest write_cs_spec --as sh.function` grades OK, and the
  driver block under its stub passed its 18 assertions; the sibling malformed-order pin in
  `tools/unattended/unarmed-branches.txt` is re-keyed 21 -> 23, the refusal having moved below the
  two edge refusals `check_edge_shape` now holds; `python tools/memory-tree/check-arms.py --report`
  read `ceiling tools/unattended/unattended.sh 321/324` and check 49 branch 23 PINNED. The leg <!-- PINNED 2026-11-14 -->
  `check-arms.py --check`, the install-prefix leg, the lexicon leg, the kit gate's check 26 and the
  Skill size leg are the close's.
