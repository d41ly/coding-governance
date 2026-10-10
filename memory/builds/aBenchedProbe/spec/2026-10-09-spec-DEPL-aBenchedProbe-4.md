# DEPL-aBenchedProbe-4 — regression arms for the keep rule, 7j4 and the 7h ceiling clause

**Status:** CLOSED · rev-1 · 2026-10-10 · node a · Tier-2 · base 2b26f187 · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-10-build-DEPL-aBenchedProbe-4-1-acceptance-ledger.md](../build/2026-10-10-build-DEPL-aBenchedProbe-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-DEPL-aBenchedProbe-3-1-spec-brief.md](../prompts/2026-10-09-prompt-DEPL-aBenchedProbe-3-1-spec-brief.md) | journal | DEPL-aBenchedProbe-3 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, confirmed four minor items that leave correct code
unguarded: H-M1 (ids 1, 4 and 6), H-M2 (ids 7 and 8), H-L1 (id 3) and H-L2 (id 9). This unit is
their one batched promotion under M4. It commits arms that red when the keep rule's receipt write,
7j4's red and exempt branches, or the 7h ceiling clause regress, it removes a dead binding whose
comment is false, and it records the one class the review named that the catalogue lacks.

## 2. Scope (IN)

- **S1** — H-M1. In `check_ceiling_emission` in `tools/govkit/selftest.py`, after CE4's checks and
  before CE5's leading settle: assert the receipt's emitted `ceiling` for `pre-push self-test` is
  still gov's 1780, call `settle(t, "the keep")`, run a second `apply --kits push-main` with no edit
  to the row, and assert it exits 0, the row still reads 3600 and the keep line prints again. CE5
  is left as it is; its leading settle commits this apply. Observed by AC1 and AC2.
- **S2** — H-L2. CE4's "names the leg" check and S1's second keep check each match the leg INSIDE
  the keep line, as one `any(...)` over `out.splitlines()`, never as two substring tests over the
  whole output. No helper is added, so no new name reaches the lexicon. Observed by AC1 and AC3.
- **S3** — H-M2(a). A module-level `check_benched_probe_arms(gcopy, run_selfcheck)` in
  `tools/govkit/selftest.py`, holding persistent staged-break arms for 7j4: (a1) the copy's
  `pre-push self-test` set to `subject = "repo"` in the push-main descriptor AND the manifest reds
  with a 7j4 line naming entry `push-main` and the leg; (a2) the manifest's `marker contracts` row,
  staged with no chunk key in the copy only, reds with a 7j4 line naming that leg and the
  `marker-contract.test.sh` argv element. Every break is written back from its kept bytes.
  Observed by AC4 and AC5.
- **S4** — H-M2(b). In the same function, the copy's push-main `pre-push self-test` ceiling set to
  1781, then to `true`, each reds with a 7h line naming `push-main`, the leg and the staged value.
  Observed by AC4 and AC5.
- **S5** — H-L1. The pre-initialisation `manifest_chunk: dict = {}` at `tools/govkit/govkit.py:2673`
  (at `54ba9c0e`) and its comment are deleted, under the condition §4 states. The same function
  gains arm (c): the copy's manifest removed, selfcheck prints a line carrying both `7j4` and
  `gate-legs.json`, and no `Traceback`. Observed by AC4, AC5 and AC6.
  **Readers:**
  by name: arm 7h of `selfcheck` in `tools/govkit/govkit.py` binds `manifest_chunk` from the
  manifest (~2683) and reads it (~2832); arm 7j4 reads it (~3271) inside its own `is_file()` guard.
  The name stays; only the dead pre-initialisation goes.
  by value: NO VALUE READERS, because the empty map is rebound from the manifest before every read,
  which is the finding.
- **S6** — The H-L2 class has no catalogue record, so this unit adds one class record under
  `memory/gotchas/`, named `line-claim-matched-over-the-whole-output`, in the front-matter format the
  others use and anchored on `tools/govkit/selftest.py`, then re-renders `memory/gotchas/INDEX.md`
  with `python tools/memory-tree/gotchas.py --write`. Observed by AC7.
- **S7** — `main()` in `tools/govkit/selftest.py` calls `check_benched_probe_arms(gcopy,
  _run_selfcheck)` directly after `check_halved_install_arms(gcopy, _run_selfcheck)`, sharing that
  gov copy. NOT OBSERVED by any pass: `main()` cannot be sliced, so only the close's `govkit
  selftest` run executes the call; the pass's grep for it is a locator, not an observation.

## 3. Non-goals (OUT)

- **N1** — No change to 7j4's predicate, its liveness reds or its absent-manifest handling. That is
  `DEPL-aBenchedProbe-3`, and this unit's arms assert against whatever text it lands.
- **N2** — No change to CE1, CE2, CE3 or CE5, and no new fixture target: S1 extends CE4's target.
- **N3** — Not the review's left-shift for H-M2, a hygiene-style check refusing "manual staged break"
  as the only evidence for a new selfcheck arm, nor its §10 checklist entries for H-M1 and H-L1.
  The catalogue already holds `containment-tested-one-way` (H-M1's class) and
  `guard-above-a-fold-makes-its-fallback-dead` (H-L1's class).
- **N4** — No edit to `check_halved_install_arms` or its nested `check_staged`. Its one-break-per-run
  shape and single-substring assertion are correct for its arms; S3 to S5 group breaks by run (§4).
- **N5** — No kit-version bump inside this unit, and no edit to `memory/DECISIONS.md`, any backlog,
  `WIRE-INTO-PROJECT.md`, `.githooks/` or `tools/run-gates/run-gates.sh`.

### Edges

- **consumes-from** `DEPL-aBenchedProbe-3` — 7j4 as that unit lands it: the per-leg red text the a1
  and a2 arms match, the absent-manifest line arm (c) matches, and the guard S5's condition reads.
  Built before it, S5's condition is judged against code about to change.
- **hands-off** external — the review's H-M2 left-shift gate in N3 stays unbuilt, for an ask the
  main loop may file.

## 4. Design

### H-M1 and H-L2, inside `check_ceiling_emission`

After CE4's four checks (`tools/govkit/selftest.py` ~2398-2412 at `54ba9c0e`), in this order:

```python
check("CE4: the receipt still records gov's ceiling, never the kept one",
      read_emitted().get(leg, {}).get("ceiling") == 1780, str(read_emitted().get(leg)))
settle(t, "the keep")
p = run("apply", "--target", str(t), "--kits", "push-main")
out = p.stdout + p.stderr
check("CE4b: a second apply with no edit exits 0", p.returncode == 0, out[-900:])
check("CE4b: the kept ceiling survives it", read_rows().get(leg, {}).get("ceiling") == 3600, ...)
check("CE4b: and the keep line names the leg again",
      any("kept the target's ceiling" in ln and f"'{leg}'" in ln for ln in out.splitlines()), out[-900:])
```

CE4's existing naming check takes the same one-line `any(...)` form. Under the review's mutation
(govkit.py ~4179 `"ceiling": _ce` written as `row.get("ceiling")`), the first new check reds because
the receipt holds 3600, and the second apply reds twice because target and receipt then agree, so no
keep fires and 1780 lands. That is the persistence the review asked to prove.

### H-M2 and arm (c), in `check_benched_probe_arms`

Five staged breaks in the gov copy `main()` already builds for 7d, 7e and the halved-install arms.
Every break is a text replace asserted to have MATCHED (a `LIVENESS` check, the precedent's form),
and every red is asserted on the ONE line that names it, because the subject-pin ratchet and the
stale-exemption check also red on several of these breaks. Breaks that red disjoint lines share a
selfcheck run:

| run | breaks staged together | asserted |
|---|---|---|
| 1 | a1 (descriptor and manifest subject `repo`), a2 (`marker contracts` chunk deleted), b at 1781 | a 7j4 line with `entry 'push-main' gate leg 'pre-push self-test'`; a 7j4 line with `'marker contracts'` and `marker-contract.test.sh`; a line with `gate leg 'pre-push self-test' with ceiling 1781` and `push-main` |
| 2 | b at `true` | a line with `gate leg 'pre-push self-test' with ceiling True` and `push-main` |
| 3 | (c) the copy's `gate-legs.json` removed | a line carrying both `7j4` and `gate-legs.json`; no `Traceback` anywhere |
| 4 | every file written back from its kept bytes | exit 0 |

Run 3 cannot join run 1 or 2: with no manifest, 7h's block is skipped, so the ceiling clause and
the subject parity are never reached. Each replace is anchored on its own leg's row, because
`subject = "kit"` appears on all three push-main rows. Run 4 is asserted here rather than left to the
arms after it in `main()`, so a bad restore is attributed to this function.

### Cost, measured

On node a, 2026-10-09, under a contended host: `python tools/govkit/govkit.py selfcheck` over the
real tree took 142 s, and over a fresh gov copy with the manifest removed 140 s; the copy and its one
commit took 47 s. All three are PINNED as measured that day. Four runs therefore add about 9.5
minutes to the `govkit selftest` leg, against its declared ceiling of 11750 s in
`tools/gate-legs.json`. One break per run, the precedent's shape, would be five breaks and five
restores, ten runs and about 23 minutes. A copy of its own would add the 47 s copy and a
base-green run. So the arms share `main()`'s copy (§8 F2).

### H-L1, and its condition

The probe on a manifest-less gov copy at `54ba9c0e` printed the 7j4 absent-manifest line and no
`Traceback`, so the deletion is safe there. Deleting rather than rewording leaves no fallback: a later
reader that loses 7j4's `is_file()` guard raises `NameError` on a tree with no manifest, which arm
(c) catches, where the empty map would have let it grade nothing. **The condition:** the pass first
reads every use of `manifest_chunk` in `selfcheck` as `DEPL-aBenchedProbe-3` left it. If every read
still sits under an `is_file()` guard, it deletes. If one does not, it does not build S5 as written:
it amends this spec first, with a rev bump and a §9 line, per M2.

### The record S6 adds

`kind: class`, `universal: false`, with Symptom, Where it bit, The fix and Gate sections like
`memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md`. Where it bit: CE4's check, and the 7h
and 7j4 arms here, whose breaks also fire the pin ratchet and the stale-exemption line on the same
output. The fix: match inside the line. The gate states the residual: no predicate catches a new
two-substring assertion, and the arms above are where the fix lives.

### Inventory

| identifier | where | cell |
|---|---|---|
| `check_benched_probe_arms` | `tools/govkit/selftest.py` | `py.function`, verb `check`, confirmed by `lexicon.py --suggest` |
| `line-claim-matched-over-the-whole-output` | gotcha class name | not lexicon-graded |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/gotchas/`
- `memory/gotchas/INDEX.md`

### Rollout

Order 5, after `DEPL-aBenchedProbe-3`: both write `tools/govkit/govkit.py` and
`tools/govkit/selftest.py`, and S3 and S5 assert against its 7j4. The pass runs
`python tools/codebase-map/gen_map.py --write` after adding the function, because a new function
stales the map's symbol set, and deletes any slice script it wrote under the tree first. Fixture
roots go under the default `%TEMP%`, never the session scratchpad, whose path length false-reds
govkit fixtures.

### Alternatives rejected

- **The review's minimum for 7j4: count the legs that reach the subject comparison and red at
  zero.** The test that rejected it is the mutation set in AC5: it catches the exempt-everything
  mutation, and stays green when the filename globs are emptied, when the subject comparison is
  weakened, or when the 7h clause is disabled. It is also a product change where a test is owed.
- **Inline arms in `main()`'s gov-copy block.** They cannot be sliced, so no pass could observe them
  red without the whole suite (memory note "govkit slices and the guards that bite them").
- **One break per selfcheck run, through a module-level copy of `check_staged`.** It is about 23
  minutes against 9.5 (§4 Cost), and the precedent's whole-output substring is the H-L2 shape once a
  second substring is needed.

## 5. Production-readiness checklist

- security — N/A — test arms and a deleted dead binding; no write path, no trust boundary. H-M1
  guards the security model's stated invariant, that a kept adopter bound is never clobbered.
- perf / scale — about 9.5 minutes added to `govkit selftest` (§4 Cost); the second apply in S1 adds
  one apply to a slice measured in minutes.
- error / empty / loading states — every staged replace asserts it matched, so a stale anchor reds
  as `LIVENESS` and never as a missing red.
- observability — each arm prints an `ok` or `FAIL` line with its own label; FAIL details carry the
  output tail.
- risks — arm (c) and a1 match 7j4 text that `DEPL-aBenchedProbe-3` may reword; the order 5 header
  sequences this unit after it, and the builder anchors on the landed text.
- testing — AC1 to AC3 slice `check_ceiling_emission`; AC4 and AC5 slice the new function over a
  fresh copy; AC6 is a real-tree selfcheck; AC7 runs the catalogue checker. No suite and no bar runs
  in the pass.
- migration — N/A — no data shape changes.
- user docs — N/A — no user-facing surface; the gotcha record is the reviewer-facing note.

## 6. Acceptance criteria

Two slices, each run from the repo root, each running one function and nothing else. Slice `S` is
`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_ceiling_emission(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`.
Slice `A` is
`python -c "import sys,pathlib,tempfile,shutil,subprocess as sp; sys.path.insert(0,'tools/govkit'); import selftest as s; g=pathlib.Path(tempfile.mkdtemp())/'g'; shutil.copytree(s.GOV_ROOT,g,ignore=shutil.ignore_patterns('.git')); [s.git(g,*a) for a in (('init','-q','-b','main'),('config','user.email','t@e'),('config','user.name','t'),('add','-A'),('commit','-qm','arms'))]; s.check_benched_probe_arms(g,lambda r: sp.run([sys.executable,str(r/s.PFX/s.KIT_NAMES['govkit']/'govkit.py'),'selfcheck'],capture_output=True,text=True,encoding='utf-8',errors='replace')); print(s.FAILURES)"`.
A mutation below is made by saving the file's bytes, editing, running, and writing the bytes back;
`git diff --stat` afterwards shows only the pass's own edits.

- **AC1** — When slice `S` runs on the built tree, it prints `[]`, and its output carries `ok` lines
  for the receipt check, the second apply's exit, the kept 3600 and the second keep line.
  Red when: any FAIL prints, or one of those labels is absent from the output.
  cost: about a minute on a contended host.
- **AC2** — When the receipt write in `tools/govkit/govkit.py` is changed to
  `"ceiling": row.get("ceiling"),` and slice `S` runs, it prints FAIL for the receipt check and for
  the second apply's kept 3600; restored, slice `S` prints `[]`.
  Red when: the mutated run prints `[]`, which is the review's surviving mutation.
- **AC3** — When the keep print in `tools/govkit/govkit.py` is split into two `print` calls, the leg
  on the first and `kept the target's ceiling` on the second, slice `S` prints FAIL for CE4's naming
  check. Run before the S2 edit, the same split leaves that check `ok`, which is the gap observed.
  Red when: the split leaves the S2 check `ok`, or the pre-edit run already reds it.
- **AC4** — When slice `A` runs on the built tree, it prints `[]`, and its output carries an `ok`
  line for each staged replace's `LIVENESS` check, for a1, a2, both ceiling values and arm (c), and
  for the restored copy's exit 0.
  Red when: any FAIL prints, or any of those labels is absent.
  cost: about 10.5 minutes, the 47 s copy plus four selfcheck runs at about 140 s each, PINNED as
  measured on node a on 2026-10-09.
  fixture: the copy is built under the default `%TEMP%`; slice `A` passes no `dir=`.
- **AC5** — When slice `A` runs after its copy's `tools/govkit/govkit.py` takes four mutations at
  once — 7j4's exempt test widened to `if chunk:`, its filename glob tuple emptied, the 7h clause's
  `if "ceiling" in leg:` made `if False:`, and 7j4's absent-manifest branch made unreachable — it
  prints FAIL for a1, a2, both ceiling arms and arm (c), and none for the restored copy's exit 0.
  Each mutation fails a different arm's label, so one run observes all four.
  Red when: any of those arms stays `ok` under its mutation.
  cost: as AC4.
  fixture: the mutations are made in the copy after `copytree` and before the call, so the worktree
  is never edited; a scratch script holding slice `A` plus four replaces, each asserted to match
  once, is the form, written outside the tree.
- **AC6** — When `grep -n "manifest_chunk: dict" tools/govkit/govkit.py` runs after the pass it
  prints nothing, and `python tools/govkit/govkit.py selfcheck` on the real tree exits 0 with its
  `held self-test legs:` note line naming nonzero graded and shaped counts.
  Red when: the binding remains, selfcheck exits non-zero, or a `NameError` prints.
  figure: the counts are DERIVED at observation; 59 graded and 22 shaped were measured at `54ba9c0e`.
  cost: about 140 s.
- **AC7** — When `python tools/memory-tree/gotchas.py --check` runs it exits 0, and
  `python tools/memory-tree/gotchas.py --for-paths tools/govkit/selftest.py` lists
  `line-claim-matched-over-the-whole-output`.
  Red when: the check reds on the new record or an unrendered index, or the class is not selected
  for that path.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py check_ceiling_emission CE4 receipt and second apply · covers AC1 AC2 AC3 · the receipt write changed to row.get("ceiling"), and the keep print split across two lines · none
New arm: tools/govkit/selftest.py check_benched_probe_arms · covers AC4 AC5 · 7j4's exempt test widened, its globs emptied, the 7h ceiling clause disabled and the absent-manifest branch unreachable, in the copy's govkit.py · none

The four govkit legs are the ones the estimate's `tools/govkit/` paths trip; `memory/gotchas/` trips
the two recall legs through their `memory/` guard; `memory hygiene` grades the catalogue index; the
last two grade the new function's name and the map's symbol set. `tools/` is a broad guard the
checker excludes. The close runs them; no pass does.

## 8. Open questions

- **F1 — H-L1: delete the pre-initialisation, or keep it and reword its comment?**
  Both close the false comment. Keeping it leaves a fallback that turns a lost `is_file()` guard into
  a silent grade over an empty map; deleting it turns the same loss into a `NameError` that arm (c)
  reds. The probe on a manifest-less copy at `54ba9c0e` found no traceback, so deletion is safe on
  today's code. Neither option trips an M3 veto. Recommendation: delete, under §4's condition.
  RESOLVED (agent, 2026-10-09, delegated): delete, and amend this spec instead if
  `DEPL-aBenchedProbe-3` leaves a read of `manifest_chunk` outside an `is_file()` guard.
- **FACT-QUESTION · F2 — Can the H-M2 arms share one gov copy and group breaks per run?**
  Probe: time a gov copy and a selfcheck on it, and check which breaks red disjoint lines. Liveness:
  the timing could have shown a copy cheap against a run, which would favour isolation. Observed:
  47 s per copy, about 140 s per run, and only arm (c) needs a run of its own. Four shared runs cost
  about 9.5 minutes against about 23 for one break per run.
  RESOLVED (agent, 2026-10-09, delegated): share `main()`'s copy, in the four runs §4 tabulates.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seam is `check_halved_install_arms` in `tools/govkit/selftest.py` (~1587 at `54ba9c0e`), a
module-level function taking `main()`'s gov copy and its `_run_selfcheck`, whose arms stage a break,
assert it matched, assert the red and restore; this unit adds its sibling with the same signature
and call site. `tools/codebase-map/reuse_lookup.py`, asked "stage a break in a copy of gov and assert
selfcheck names it, then restore", returned only name-stem neighbours (`stage_or_fail`,
`run_in_gov`, `build_gov_index`) and no fixture seam, so the seam was confirmed by reading
`tools/govkit/selftest.py` at 1587-1622, 2328-2427 and 3387-3546. For H-M1 the seam is
`check_ceiling_emission` itself, with its `settle`, `run`, `read_rows` and `read_emitted`; nothing
new is added there. The recall probe returned the DEPL-aBenchedProbe-2 brief's staged-break
precedent, the aGradedDialect round-3 review asking that a staged break live in a `selftest.py`
mutation fixture applied to a copy, and this build's own review record. Candidates tested and
rejected are in §4 Alternatives rejected.

Recall terms used: `python tools/memory-recall/query.py "how are selfcheck arms kept observable red after a manual staged break, and how is a keep rule tested across re-applies" --terms "staged break gov copy selfcheck arm observed red restore halved install keep rule receipt ceiling regression"`
