# TOOL-aQuarriedLantern — build ledger

One entry per build unit. Every number below came from a command run in-session, not from the spec.

## U1 — `tools/memory-recall/` — the kit itself

**Landed** 2026-08-03 · node `a` · base `f564109e`

### Shipped — 9 files, `tools/memory-recall/`

| File | Category | Bytes |
|---|---|---|
| `recall_conf.py` | new — the project layer | 7 492 |
| `extract.py` | forked from inCMS `5318064` | 21 542 |
| `query.py` | forked from inCMS `5318064` | 45 572 |
| `bench.py` | verbatim upstream | 20 253 |
| `union.py` | verbatim upstream | 5 827 |
| `selftest.py` | new — 14 checks | 24 934 |
| `adopt-memory-recall.sh` | new | 5 701 |
| `README.md` | new | 7 786 |
| `verbatim.json` | new — digest pin for the two verbatim files | 69 |

`bench.py` and `union.py` were verified byte-identical to `/c/projects/incms/main/scripts/recall/`
with `cmp -s`, not assumed. `verbatim.json` pins their LF-normalised sha256 prefixes
(`bench.py 5a46060ffb2008fc`, `union.py a345199f5d901aae`) so a later silent edit reds the selftest.

### Measured

| Fact | Value |
|---|---|
| this repo's corpus | 66 tracked `.md` files, 496 153 B |
| first live query | `index 9 records + 1033 chunks (rebuilt 0.09s)`, 29 hits, 7 shown in 2 917 B |
| index build (`built_s`) | 0.18 s |
| warm query, wall | 1.584 / 2.230 / 2.274 s — interpreter start-up and `git`, not the index |
| full-corpus grep baseline | `grep -rIl "adopt" memory/` 0.077 / 0.092 / 0.447 s, 31 of 66 files |
| selftest | 14/14 checks, 24.2 s wall |
| conf digest, this repo | `9bcce30ca38b` |

At this corpus size retrieval is **slower** than the grep it replaces. What it buys is a ranked
handful instead of half the tree, and the README says so rather than implying a speed win.

### The three things that had to be right

1. **The silent zero (S7).** Upstream returns `index 0 records + N chunks` and exits 0 when the id
   families do not match the corpus. Reproduced in a throwaway repo with `FAMILIES="tooling:ZZZZ"`:
   the header still reads `index 0 records + 1 chunks`, and the CLI now also prints a `ZERO RECORDS`
   block on stderr naming the resolved families, the conf path and
   `` `python memory-recall/query.py --rebuild` ``. The same diagnosis fires on `extract.py`'s own
   path. Gated by the selftest arm *mis-declared FAMILIES is LOUD*, which asserts both paths.
2. **The cache freshness key (blocker F1).** `Conf.digest()` hashes the RESOLVED `MEMORY_ROOT`, the
   sorted families tuple and the node-tag class — not the conf file's bytes, so a comment edit costs
   no rebuild. It lands in the manifest and joins `ensure_cache`'s `fresh` predicate. Measured in
   both directions: `2 records (rebuilt) -> cached -> 0 (rebuilt) -> 2 (rebuilt)`.
3. **Writes nothing in the adopter's worktree (F5).** `sys.dont_write_bytecode = True` sits ABOVE
   the `sys.path` insert in `query.py`, `selftest.py` and `recall_conf.py`. Asserted by PATH: the
   arm walks the whole worktree — kit directory included — before and after a query, in a fixture
   repo with **no** `.gitignore` at all, and asserts the set is unchanged and that the 4 files
   created all sit under `<gitdir>/recall/`.

### Also folded

- **R1** — no `--memory-root`, no `--families`. The conf-absent refusal prints a two-key stub; the
  selftest pastes that stub verbatim into a fixture repo, asserts the next query returns 2 records,
  and asserts both flags are rejected as unknown.
- **F7** — every printed invocation derives from `__file__` through one `CLI` expression, reused by
  the module docstring, `REFUSAL`, the `--export` header and the qid hand-back. The selftest runs in
  a repo whose kit dir is `memory-recall/` (not this repo's `tools/memory-recall/`), harvests every
  `python <path>.py` the CLI prints across `--help`, the no-terms refusal and a successful query,
  and asserts each one resolves.
- **R5 / F14** — `evict_dead_siblings` deletes a sibling cache only when its manifest is readable
  AND records a `worktree` that no longer exists. No readable manifest = NEVER evicted (that is the
  shape of a sibling mid-first-build). All three cases are one selftest arm.
- **F9** — `adopt-memory-recall.sh` resolves `python3` first with a `python` fallback and a
  `RECALL_PY` override (the `tools/check-wiring.sh:69` form). The selftest runs it on a PATH cut
  down to a `python3` shim plus the bash/git directories, and asserts exit 0.
- `--export` writes beside the query log under the common git dir and requires `--tag`; upstream's
  `CLAUDE.md` node-registry lookup is deleted. `BUILD_QID_CUTOFF` ships empty — the mechanism, none
  of the inCMS data. No alias data ships; the alias mechanism does, and the empty-alias path is a
  gated arm.

### Bugs found and fixed while building, each by a run rather than a read

- `HERE` was resolved after `cd "$ROOT"`, so a relative `$0` made the adopt script look for
  `recall_conf.py` under `C:/Program Files/Git/`. Now resolved before the `cd`.
- `git rev-parse --show-toplevel` spells the root `C:/x` under MSYS while `pwd` spells it `/c/x`, so
  the prefix-strip that computes the kit's repo-relative path silently no-opped and printed an
  absolute path. Root is re-read through `pwd`.
- The `python`-off-PATH arm tested `"HAVE_PYTHON" in probe`, and `"HAVE_PYTHON3"` contains
  `"HAVE_PYTHON"` — so a correctly isolated PATH reported "python is still here" and the arm skipped
  for the wrong reason. It now matches exact tokens. Without this the AC14 arm would have shipped
  never running.

### Mutation verification — 8/8 killed

Green baseline asserted first (14/14). Each mutation was asserted APPLIED on disk (present-before /
absent-after) and each revert asserted byte-identical; a crash scores as a kill. Post-revert 14/14.

| Mutation | File | Arm that reddened |
|---|---|---|
| M1 drop `sys.dont_write_bytecode` | query.py | writes NOTHING in the worktree |
| M2 drop `conf_digest` from the `fresh` predicate | query.py | conf_digest joins freshness |
| M3 drop the zero-record diagnosis from the query path | query.py | mis-declared FAMILIES is LOUD |
| M4 `zero_record_diagnosis` always returns None | extract.py | mis-declared FAMILIES is LOUD |
| M5 evict cache dirs with no readable manifest | query.py | cache eviction |
| M6 hardcode the printed invocation to the upstream path | query.py | printed invocations resolve |
| M7 stop trimming unquoted conf values at whitespace | recall_conf.py | conf parser == bash |
| M8 edit a verbatim file | bench.py | byte-identical to upstream |

### One follow-up commit, and why the next unit will hit it too

Registering the two legs changed `tools/gate-legs.json`, which the kickoff-manifest ratchet watches.
The ratchet only sees COMMITTED state, so it was green before the commit and red after: check 5 wants
a `last-audit` re-stamp at or after the watched change. It also surfaced pre-existing debt —
`tools/run-gates.sh` had changed since the 2026-07-20 stamp with no re-stamp. §B was re-verified
(the leg list is still single-sourced from `gate-legs.json`; the gate-command line gained the
skill-wiring category it lacked) and `last-audit` was re-stamped at the kit commit. **Any later unit
that touches `tools/gate-legs.json` will red the same leg** — re-verify §B and re-stamp, do not
skip past it.

### Deviations from the rev-2 spec

- **`union.py` ships.** Spec §3 lists it under Non-goals; the orchestrator's ratified shipping set
  names it. Shipped byte-identical, with the README stating that its `main()` is inert without a
  `fixture.json` this kit does not ship — the same caveat `bench.py` carries.
- **`SKILL.template.md`, `recall-opened.js` and `recall-opened.fragment.json` are not in this
  unit.** `adopt-memory-recall.sh` ships their full contract and reports a three-state result:
  template absent → `skip` and exit 0 on `--check` (nothing rendered can drift), exit 1 on
  `--scaffold` (you asked to install it); a rendered `SKILL.md` with no template → exit 1, because
  that is the one genuinely unverifiable state. Placeholder contract for whoever writes the
  template: `{{FAMILIES}}`, `{{MEMORY_ROOT}}`, `{{QUERY_CLI}}` — an unsubstituted `{{...}}` reds.
- **Both gate legs and the `check-kit-versions.sh` pair assertion were registered here** rather than
  deferred: a kit that ships unwired is the defect the source feature spent a session repairing.
  `memory-recall skill wiring` is green-with-a-skip-line until the Skill template lands.
- The R1 selftest arm asserts the two flags are REJECTED, which is a stronger reading than the
  spec's "the refusal must not print them".
- The adopt script does **not** carry codebase-map's `-ef` fixed-kit-name check: this repo keeps its
  kits under `tools/`, and `--check` is a gate leg here, so a fixed `<root>/memory-recall` assertion
  would red the leg in the reference adopter.

## U2 — the invocation surfaces: the rendered Skill, the outcome hook, settings-merge

**Landed** 2026-08-03 · node `a` · base `3e427de`

### Shipped — 4 new files in `tools/memory-recall/`, 3 files extended

| File | Category | Bytes |
|---|---|---|
| `SKILL.template.md` | new — the trigger surface, rendered from the conf | 4 853 |
| `recall-opened.js` | forked from inCMS `fd6274d` | 9 234 |
| `recall-opened.test.sh` | new — 8 cases | 7 874 |
| `recall-opened.fragment.json` | new — event, matcher, marker, hook path | 158 |
| `tools/settings-merge.py` | `--fragment FILE` + 4 selftest cases | +154 / -31 |
| `tools/check-wiring.sh` | the three-state `recall` arm | +36 |
| `tools/memory-recall/selftest.py` | 4 new arms (14 -> 18 checks) | +141 |
| `.claude/skills/memory-recall/SKILL.md` | this repo's dogfood render | 4 903 |

### Measured

| Fact | Value |
|---|---|
| kit selftest | **18/18 checks**, 2 m 06 s wall (was 14/14 at 24 s — the 4 new arms spawn bash+git+node) |
| hook test | **8/8 cases**, 21.6 s wall (5 `git init` = 4.9 s, 9 `node` spawns = 3.4 s, measured) |
| settings-merge selftest | PASS, 10 cases (6 pre-existing + 4 `--fragment`) |
| hook fork divergence | 26 code lines, all in ONE construct (comments stripped before diffing) |
| rendered description | 1 322 B, 1 `/session-kickoff` clause, 0 flags `query.py` cannot parse |
| mutations | **9 killed / 10**, each asserted applied on disk and reverted byte-identically |

### AC10's first half, measured rather than argued

`settings-merge.py` with no `--fragment` was run head-to-head against `git show HEAD:` of itself,
on a settings file already carrying a foreign `PreToolUse` group: the written file is
**byte-identical** (`cmp`) and so is stdout, on the create path, the already-wired re-run, and the
`--check`-on-absent-file path. The fragment is the ONLY behaviour change.

### The three things that had to be right

1. **The hook works on any corpus root (F13).** Upstream tests a literal `memory/` prefix and then
   scans for a literal `/memory/` boundary; on any other `MEMORY_ROOT` both return null and `main()`
   bails, indistinguishable from "no read matched". The root now comes from the log's `shown_paths`,
   which is corpus-relative by construction — **not** from parsing `.memory-tree.conf`, which would
   be a third copy of that grammar in a third language, gated by nothing. Two cases pin it: a
   `docs/`-rooted corpus, and a `docs/`-rooted read from a SIBLING WORKTREE.
2. **No hook without `--with-hook` (R4/F10).** Absence is a true signal, so `check-wiring.sh` reports
   three states instead of a permanent false UNWIRED in the repo that runs it as its own SessionStart
   hook. All four states verified end to end: kit absent -> `skip` exit 0 · opt-in not taken ->
   `skip` exit 0 · present-but-unmerged -> `UNWIRED` exit 1 · merged -> `ok` exit 0, with `--session`
   exit 0 throughout.
3. **The description claims nothing this engine lacks (R2/F4).** Upstream's clause — "that skill's
   Step 3 issues this query itself" — is true in inCMS and false here, and ported verbatim it
   suppresses the tool at the exact moment the Goal targets. The template defers to whatever probes
   the kickoff skill asks for and names no step number; the selftest rejects any `/session-kickoff`
   sentence carrying `Step` or a digit.

### Three things found by running, not reading

- **A sentence split on `;` let upstream's own clause through.** The first cut of the AC18 check
  split on `[.;]`, which cuts "…is running; that skill's Step 3 issues this query itself." in half:
  the half naming `/session-kickoff` has no digit and the half with the digit has no
  `/session-kickoff`. Split on the sentence terminator only. Caught by mutation M5, which is exactly
  the upstream text.
- **The hook's own-tree fast path is not independently observable.** Restoring only its `memory/`
  literal leaves every case green, because the boundary scan is a strict superset for a read inside
  the hook's own checkout. Kept anyway (upstream parity, one fewer `statSync` on the hottest tool in
  the session) and scored honestly: M1 SURVIVED, M1b (the scan's literal, killed by the sibling
  case) and M1c (both literals — the real upstream state) both KILLED.
- **`cygpath -m` hands back the 8.3 name.** `C:/Users/DAILY-~1/...` while git writes the long form
  into a linked worktree's `gitdir:` pointer, and `path.resolve` does not unify them — so the
  sibling-worktree case recorded nothing, for a FIXTURE reason that looks exactly like the hook
  defect it exists to catch. `cygpath -ml`. The hook itself is upstream-identical here: it does not
  canonicalise 8.3 names, and neither does upstream.
- Bonus, from the harness: a bare `bash` under Python's `subprocess` is the **WSL** shim — exit 127,
  script never read, `chdir(/mnt/c/...) failed 5`. Scoring on exit status alone would have called
  every bash mutation a kill. The harness probes `uname -o` for `Msys` and demands a named token in
  the red output.

### Deviations from the rev-2 spec

- **The `skills/session-kickoff/SKILL.md` Step 4 probe paragraph is NOT in this unit.** F4's fix has
  two halves; this unit closed the template half (the clause claims nothing the engine lacks) and
  left the positive-wiring half to the unit that owns registrations — it is the kickoff engine's own
  doc, and touching it re-opens the manifest ratchet. **If no later unit takes it, F4 is half-folded.**
- **`tools/check-wiring.test.sh` gains no cases here** — per the build plan U3 pins both hook states.
  The expectations they must pin are the four verified above, and the mutation that must red them is
  `if [ ! -f .claude/hooks/recall-opened.js ]; then` -> `if false; then` (M4, killed against a
  scratch oracle). Until then the arm is verified but ungated.
- **No new gate leg for `recall-opened.test.sh`.** Spec §7 names two legs and both already exist;
  the hook test runs as a kit-selftest arm instead, so `tools/gate-legs.json` is untouched and the
  kickoff-manifest ratchet is not re-opened.
- **No `gov:kit` marker in `SKILL.template.md`.** The spec's wiring table pairs the constant with a
  marker there; U1 paired it with `README.md` and that pair is gated. A second hand-kept marker with
  no second gate line would be a marker that can drift silently, which is worse than none.
- **`--stats` and `--export`** — no sentence anywhere in the kit claims `--stats` reads the query
  log. The rendered Skill states it prints the cache manifest, and that `--export` writes beside the
  log under the common git dir with `--tag` required.
