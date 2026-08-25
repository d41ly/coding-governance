# TOOL-dSpentCeiling-1 — retire check 16's byte budget, and make rules 3 and 4 structural

**Status:** INPROGRESS · rev-2 · 2026-08-25 · node d · Tier-2 · base 70df24ea · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-TOOL-dSpentCeiling-1-ceiling-history.md](../build/2026-08-25-build-TOOL-dSpentCeiling-1-ceiling-history.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Delete hygiene check 16's byte-budget arm and both `READ_PATH_*` pins kit-wide, and lift rules 3 and
4 out of the armed unit so the charter-citation check no longer depends on a pin anyone can blank.
Nothing replaces the budget: check 6 already caps every read-path member, so rule 1 was a second
bound over an already-bounded population.

## 2. Scope (IN)

- **S1** — New top-level `check_read_path(root, conf)` in `corpus_ids.py` holding rule 3 and rule 4.
  It calls neither `walk()` nor `grammar()`; `read_set` needs only root, conf and tracked, so a
  minimal dict suffices and memory-recall stays a CONDITIONAL kit dependency.
- **S2** — `main()` becomes `bad = check_read_path(root, conf)` then `if armed(conf): bad +=
  checks(walk(root, conf))`.
- **S3** — `armed()` becomes `any(conf.get(k) for k in ("DEAD_PATH_PIN", "ORPHAN_ID_PIN"))`. Two
  changes, both load-bearing: the tuple loses the ceiling, and the subscript becomes `.get` so a key
  absent from `load_conf`'s defaults is not a raw `KeyError`. Docstring corrected to checks 13-15.
- **S4** — Delete the budget arm, `DEFAULT_READ_PATH_HEADROOM`, the `--measure` ceiling line, both
  keys from `load_conf` defaults, and `_parse_conf_int`'s `minimum=` parameter, whose last caller was
  the ceiling read.
- **S5** — The untracked-CHARTER raise becomes a finding plus an early return inside
  `check_read_path`, so a mis-set charter reds check 16 alone instead of replacing every 13/14/15
  finding with one line. `read_set` keeps its raise for `cmd_report`'s existing try/except.
- **S6** — The tracked-but-absent line is renumbered rule 4, retexted without the word NOTE, and its
  `check 12 owns that finding` comment DELETED as false.
- **S7** — The grace. A kit constant names the version at which rule 3 begins to red. At memory-tree
  2.42 rules 3 and 4 print their findings on a non-redding channel; at the declared successor version
  they red. It is a kit constant, never a conf key.
- **S8** — The stale-key announcement, non-redding, keyed on PRESENCE in the conf dict (blank
  included) — which is an exact test only because S4 removes both keys from the defaults.
- **S9** — Carriers, all forced by gates: `.memory-tree.conf`, `.memory-tree.conf.example`,
  `kit.toml` (requires_if, conditional_keys, discharge), `HYGIENE.template.md` and its rendered
  `memory/HYGIENE.md`, `check-memory-hygiene.sh`'s check-6 comment and version marker,
  `check-memory-hygiene.test.sh`'s engine-key list, `drift_signals.py`'s RATCHETS row and its prose
  citation, `install-prefix-waivers.txt`, `method-carriers.txt`, `memory-recall/extract.py`'s worked
  example, `template-size-limits.txt`, `memory/map/features/memory-tree-hygiene.md`, and
  `tools/memory-tree/README.md`.
- **S10** — The movement-history block moves from `.memory-tree.conf` into this build folder as the
  retirement exhibit, with a short surviving comment at `READ_PATH_WAIVER` pointing at it. The
  pointer is what keeps `memory/project/method-carriers.txt` honest.
- **S11** — Selftest arms in `corpus_ids.py`'s own suite for every behaviour above, replacing the
  arms that exercised the deleted budget.
- **S12** — Records: append-only supersessions for `TOOL-aFoldedQuarry-5`'s blank-means-off contract
  and `TOOL-aWidenedGuide-1`'s premise that the byte ceiling is the real budget, plus the retirement
  record carrying the composition finding. Backlog: this row closes, `TOOL-aRelaxedShard-3` closes,
  `TOOL-dSettledRoster-1` is re-worded, and a new row opens against kit-rendered doc size.

## 3. Non-goals (OUT)

- **No replacement instrument.** No drift signal, no `--report` class column, no new dossier, no
  parity arm. The composition finding is recorded prose, not a standing measurement. If read-path
  growth becomes a live question again it is a fresh build with fresh evidence.
- `read_set` does not move. Which files count is unchanged, including its three token arms.
- `READ_PATH_WAIVER` is KEPT and becomes the only conf key check 16 reads.
- No new gate leg — a leg name is a codebase-map key, a `subject-pins.tsv` row and a drift-audit
  leg-probe entry at once, and this unit adds no subject.
- Check 16 is NOT split into two numbered checks. The hygiene check COUNT is hand-typed in at least
  three places and already disagrees with itself; renumbering adds a fourth wrong count. That
  inconsistency gets its own backlog row, not a fix here.
- The stale `gov:kit drift-audit@` markers are left alone — already behind, and fixing them grows the
  diff a second topic.

## 4. Design

### Mechanism

Check 16 today is one `if conf["READ_PATH_CEILING"]:` wrapping three things: the byte budget, rule 3,
and the tracked-but-absent finding. Blanking one line silences all three, and `armed()` is a
MODULE-WIDE switch, so a repo whose only set pin was the ceiling also loses checks 13, 14 and 15.
That is two arming layers over a check whose population comes from `CHARTER`, which already ships
with a value. The fix is to stop arming rule 3 at all: it runs whenever the conf is loadable.

### Migration — what an adopter experiences

An adopter who never armed the pins sees one new non-redding announcement if their conf declares
either key, and rule 3 / rule 4 findings printed but not gating. An adopter who armed the ceiling
sees the budget stop reporting and the same two rules keep reporting. Nobody reds for doing nothing,
which is what makes 2.42 a legitimately MINOR bump next to a gate that is arming.

### Rollout — the grace, and its cost stated

Rule 3 has never run in any tree but this one, because the kit ships every pin blank. Arming it as a
straight gate would red an adopter for a pre-existing condition on their first upgraded bar. So 2.42
announces and the declared successor version gates. The cost here is one version in which a NEW
uncapped charter citation would print rather than block — measured, not assumed: all six members are
byte-capped today and `READ_PATH_WAIVER` is empty, so the grace costs this repo nothing observable,
and the announcement still prints on every bar.

### Alternatives rejected

- **A replacement rate signal** (`measure_read_path_authored_growth`, epoch-windowed, report-only).
  Fully designed and dropped on the owner's ruling of 2026-08-25. It would have added a second copy
  of the token grammar pinned only at HEAD, a new drift-audit dossier the map's convergence rule then
  requires, and its own selftest arms — to replace an instrument this build's own evidence shows was
  redundant rather than mis-calibrated.
- **A new arming key for rule 3** (`READ_PATH_ARM` or similar). Recreates the defect being closed,
  renamed.
- **Striking the ceiling from `armed()`'s tuple without restructuring.** Silently disarms checks 13,
  14 and 15 for an adopter whose only set pin was the ceiling — a legal state today.
- **Refusing on a stale key rather than announcing.** The shipped example declares the key blank, so
  refusal reds every adopter for doing nothing.

## 5. Production-readiness checklist

- security — N/A: no new input, no new write path, no egress.
- perf / scale — N/A: strictly fewer reads. The budget's `getsize` sum over members is deleted.
- a11y — N/A: no user surface.
- i18n — N/A.
- error / empty / loading states — the untracked-CHARTER case moves from a raise that eats sibling
  findings to a finding plus early return (S5). No charter citation under `MEMORY_ROOT` is a
  legitimate empty population and must announce itself rather than pass silently.
- observability — the announcement is the observability: a retired key and a graced rule both print.
- risks — the one real hazard is S3. Removing a key from `armed()` without S1's restructure silently
  disarms three checks; AC5 exists to catch exactly that, and it is the arm to write first.
- testing + left-shift gates — S11. Every deleted arm is replaced by an arm over the new behaviour;
  the arms count is floored by `ARMS_FLOORS`.
- migration / rollback — reverts cleanly: the change is a deletion plus a restructure in one file,
  and no data shape moves. An adopter mid-upgrade holds a conf key nothing reads, which is inert.
- user docs — `HYGIENE.template.md` and the rendered `memory/HYGIENE.md` (S9), plus the kit README's
  check description.

## 6. Acceptance criteria

- **AC1** — When the pre-change engine runs against a scratch conf that sets NO pin and a charter
  backtick-citing a tracked, present `memory/project/notes.md` outside `--print-index-set`, it exits
  `0` with no output. This green IS the defect and is recorded BEFORE the change.
- **AC2** — When the post-change engine runs the same fixture at the graced version, `check 16 rule
  3` is PRINTED and the exit code is `0`; at the declared successor version the same fixture exits
  `1`. Both observed, because the grace and the gate are one mechanism read twice.
- **AC3** — When that path is added to `READ_PATH_WAIVER`, the rule-3 finding disappears. Observed
  AFTER AC2's finding, never before, or the valve is unproved.
- **AC4** — When the same fixture runs with `tools/memory-recall/extract.py` deleted, the rule-3
  finding still prints AND stderr carries no `the id grammar lives in the memory-recall kit` refusal
  — proving `check_read_path` left `walk()`.
- **AC5** — When a fixture sets `DEAD_PATH_PIN` and seeds a check-15 break, the check-15 finding
  reports; when that pin is then blanked, check 15 goes silent while rule 3 still reports. This is
  the arm that catches disarming 13-15 for an adopter whose only pin was the ceiling.
- **AC6** — When a fixture sets `CHARTER="NOPE.md"` and stages a check-14 break, BOTH the check-16
  charter finding and the check-14 finding print in ONE run. Today `Problem` escapes `checks()` and
  `main()` prints one line, so the observation is that TWO lines appear.
- **AC7** — When the charter cites a guide that is tracked but absent from the worktree, rule 4
  fires, its message contains neither `check 12` nor `NOTE`, and `check-memory-hygiene.sh` check 12
  and check 6 both stay silent about that file.
- **AC8** — When a fixture conf carries `READ_PATH_CEILING="161120"` — a value that redded instantly
  under the old rule 1 — it exits with the SAME code as the same fixture without the key, plus the
  announcement line. Blank gives the same announcement; the line deleted gives none.
- **AC9** — When `READ_PATH_CEILING` is removed from `kit.toml`'s `conditional_keys` but LEFT in
  `requires_if.when_any_key_set`, `python tools/govkit/govkit.py selfcheck` reds. Observed red, then
  both moved, then green.
- **AC10** — When the conf block is rewritten with `memory/project/method-carriers.txt` untouched,
  `bash tools/memory-tree/check-method-carriers.sh` reds on the declared carrier that no longer
  mentions `BUILD-METHOD.md`. Observed red, then the pointer added, then green.
- **AC11** — When the kit version bump is placed EARLIER in the range than the last behaviour-bearing
  commit, `bash tools/memory-tree/check-verdict-epoch.sh` reds. Observed red, then re-placed, then
  green, with `bash tools/check-kit-versions.sh` green.
- **AC12** — When `memory/HYGIENE.md` is hand-edited instead of re-rendered, `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` reds. Observed red, then re-rendered, then green.
- **AC13** — OBSERVED SILENCE, recorded as such: with both keys gone from the conf and
  `drift_signals.py`'s RATCHETS row still present, `python tools/drift-audit/drift_report.py --check`
  says NOTHING about the dead row. The row's deletion is therefore a manual obligation, not a gated
  one, and this criterion is what stops a reviewer assuming a gate covers it.
- **AC14** — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` green on the merged
  tree. The `corpus-ids selftest` and `memory-hygiene self-test` legs are subject-kit and held by
  default, so a plain bar over this change proves close to nothing.

## 7. Gates

`memory hygiene` · `corpus-ids selftest` · `memory-hygiene self-test` · `kit versions` · `verdict
epoch` · `install prefix` · `method carriers` · `govkit selfcheck` · `kit/dogfood doc parity` ·
`drift-audit records` · `build README slot contract` · the manifest gate fence. The DoD run is
`GATE_FULL=1 GATE_SELFTESTS=1`; no new leg is added.

## 8. Open questions

- **F1 — does the grace constant expire by a follow-up unit, or ship with its flip version baked
  in?** Baking the successor version in means no second unit and no chance of the flip being
  forgotten; a follow-up unit means the flip is a decision someone makes with adopter evidence in
  hand. Recommendation: bake it in, because a grace whose end depends on somebody remembering is a
  grace with no end. RESOLVED (agent, 2026-08-25, delegated): bake it in.
- **F2 — does the retirement record supersede `TOOL-aWidenedGuide-1`?** That decision widened the
  guide cap to 61440/750 partly on the stated ground that check 16's byte-measured
  `READ_PATH_CEILING` is the real budget and is NOT relaxed. This build removes that backstop, so the
  ground is gone even though the widened cap stays correct. Recommendation: supersede it with a new
  id rather than leave the premise standing, per §6's never-rewrite rule.
- **F3 — the manifest has 22 B of margin** (25578 B against `MAX_MANIFEST_BYTES` 25600). S12's
  manifest edits must net at most that, and the manifest's own check-7 text says the file is trimmed
  rather than the limit raised. Recommendation: trim the read-path bullet to a single line once the
  key is gone, which frees more than the edit spends.

## 9. Revision log

- rev-2 · 2026-08-25 · built. AC6's stated mechanism was too narrow and is corrected here: it said the pre-change engine printed ONE line because the `Problem` escaped `checks()`. Observed both paths — with a ceiling declared it printed one line and check 14 vanished, and with no ceiling declared the mis-set charter was INVISIBLE because check 16 never ran. The post-change engine prints both findings in either case.
- rev-1 · 2026-08-25 · initial draft. Scope cut from a six-unit decomposition to one unit on the
  owner's ruling that six specs to remove one variable is the tail wagging the dog; the designed
  replacement signal is recorded in §4 as rejected rather than dropped from the record.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` over "conf key arming a hygiene check that must not be
disableable by blanking" returns `armed` (`corpus_ids.py`, fan-in 6, SEAM) as the seam this unit
rewires, and `load_conf` (fan-in 16, SEAM) as the accessor it must not fork. The reuse for S7's
non-blankable resolution is the CAPTURE-BEFORE-SOURCE idiom already shipped twice in
`check-memory-hygiene.sh` — `_SPEC10_SHIPPED` captured before the conf is sourced and restored
after — and NOT the `_resolve_cap` helper the dossier advertised, which exists in no file under
`tools/` and was corrected at `8e9a04e1`. `ask_shell --print-index-set` is reused unchanged: check 6
owns the capped population and this unit keeps asking rather than transcribing.
