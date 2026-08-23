# Review — TOOL-dScrubbedConduit-1 (spec rev-1)

**Serves:** spec-audit TOOL-dScrubbedConduit-1

## Verdict: BLOCKED

Batched skeptic over all three lenses: 31 raw findings, 9 REFUTED, 12 confirmed, 5 high. rev-1 was not buildable. Folded at rev-2.

---

# Batched skeptic — per-finding verdicts

Base `abd0f026` (+ spec commit `4784788a`). Git `2.54.0.windows.1`. All fixtures live under the
scratchpad; the real gov worktree was read-only throughout (`git status --porcelain` = 0 lines,
shared `core.bare` still `false` at exit).

Fixtures built:

- `s1/base` — a standalone top-level clone of the gov tree (850 tracked files), `git init` + commit.
- `s2/{remote.git,plain,wt}` — bare remote + plain clone + linked worktree, env-dumping `pre-push`.
- `s2/{gov,govwt}` — the gov tree as primary + a linked worktree, for a real bar leg.
- `s3` — `s1/base` with `memory/guides/BUILD-METHOD.md`, then the whole `memory/guides/`, removed.
- `q1` — `s1/base` with Q1's scrub applied to `run-gates.sh`.

| id | verdict | evidence |
|---|---|---|
| claims-1 / fixes-1 / fixes-3 / specdoc-1 — S1 names one of three sites; the fix is not output-neutral | **CONFIRMED** → F1 | Unfixed: `UnicodeDecodeError` at `gen_build_index.py:128` via `:492`. With ONLY `:493` widened: `--check` reports **52** stale READMEs; `--write` gives `53 files changed, 2 insertions(+), 398 deletions(-)`, and the Record/Kind/Serves table is gone from every build README. `read_text` (`:124-128`) raises only `OSError` / `UnicodeDecodeError`, so `except Problem` is dead code and `(Problem, UnicodeDecodeError)` still dies with `FileNotFoundError` on a tracked-but-missing file (reproduced by deleting `memory/DECISIONS.md`). AC1's "the same artifacts" is false as written. |
| fixes-2 — a complete fix still reds check 21; today it is vacuously green | **CONFIRMED** → F2 | All three sites widened: `--print-bindings` emits `A<TAB>...shot.png<TAB>unreadable: 'utf-8' codec...`; after `--write` + commit, `check-memory-hygiene.sh` prints `HYGIENE check 21 FAILED`, RC=1. Unfixed, `--print-bindings` emits **0** lines and check 21 passes on nothing, because `:663` runs it under `2>/dev/null || true`. |
| claims-2 / fixes-4 / specdoc-2 / specdoc-3 — S2's mechanism and the §4 table are wrong | **CONFIRMED** → F3 | Env-dumping `pre-push`: a plain clone exports **no** `GIT_DIR`; a linked worktree exports `GIT_DIR=.../.git/worktrees/wt`. `GIT_DIR=<wt gitdir> git init` in a temp dir flipped the **shared** `.git/config` `core.bare` from `false` to `true`, and the primary tree then answered `fatal: this operation must be run in a work tree`. Repeated with a REAL gov leg: `GIT_DIR=... bash tools/check-wiring.test.sh` run from `s2/govwt` flipped `s2/gov`'s shared `core.bare` to `true`. No submodule anywhere. The reviewed tree is itself a linked worktree (`.git` contains `gitdir: .../worktrees/upstream-asks-dScrubbedConduit`). |
| fixes-5 — the S2 corruption makes the merge bar fail OPEN | **CONFIRMED** → F4 | Under `core.bare=true`, `git rev-parse --show-toplevel` exits **128**, so `.githooks/pre-push:11`'s `|| exit 0` fires. Live: with a gov-shaped hook installed, a push from the bricked primary tree printed `[new branch] main -> main2` at **rc=0**, never printed `GATE RAN`, and the branch landed on the remote. |
| fixes-6 — Q1's "both" recommendation breaks the evidence harness | **CONFIRMED** → F5 | One variable. Baseline `run-gates.sh`: `GIT_DIR=$SP/q1/nope.git ... bash run-gates.sh` gives rc=**2**, `not a git repo`, 0 files in the real `.git/gate-logs` — the case at `run-gates.evidence.test.sh:113-117`. With `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE` at the top: rc=**0**, not refused, **1** file written into the real `.git/gate-logs`, and a real `.git/gate-last-summary.txt` created — exactly what the harness header at `:12-14` says the scratch `GIT_DIR` exists to prevent. |
| claims-4 / fixes-8 / specdoc-8 — S3's fix leaves the symptom; AC3 has an arm that cannot fail | **CONFIRMED** → F6 | Unfixed `--render` with the live copy missing prints `missing live copy`, writes nothing, and exits **0**; `--check` exits 1. With the spec's fix applied and `memory/guides/` absent: `line 80: memory/guides/BUILD-METHOD.md: No such file or directory`, the loop still prints `kit-parity: rendered ...`, RC=**0**, file absent. Line numbers: the `continue` is `:77`, the render redirect `:80`, the `exit 0` `:107` (the lenses said 108). |
| specdoc-6 — AC4 is satisfiable while a shipped placeholder stays undetectable | **CONFIRMED** → F7 | `.unattended.conf.example:41` `KEEPALIVE_INTERVAL="<e.g. every 10 minutes (cron 3-59/10 * * * *)>"` does **not** match `<[a-z-]+>` (piped through `grep -qE`: no match). It renders into `SKILL.md:134` via `{{KEEPALIVE_INTERVAL}}`. |
| fixes-10 / specdoc-7 — fixing S4 removes a standing govkit exemption | **CONFIRMED** → F8 | `govkit.py:1741-1750`: any `blocks_gate` hole whose discharge exits non-zero returns `True`; the caller at `:2513` uses that to suppress the red-after-install criterion. `kit.toml` declares three gate legs (`:84`, `:93`, `:99`). The probe measures rc=**1** against gov's live, correctly-filled `SKILL.md`. §5's risks line names only S1 and S3. |
| fixes-11 / specdoc-5 — Q2(c)'s premise is wrong in both directions | **CONFIRMED** → F9 | `tools/gate-legs.json` carries `pre-push self-test` running `bash .githooks/pre-push.test.sh`, already on the bar; that suite builds `git init -q --bare` / `git init -q "$tmp/work"` (`:23-24`), the one layout that exports no `GIT_DIR`. `kit-dogfood-parity.test.sh` IS a bar leg but has no self-test: `grep -rln kit-dogfood-parity tools/ .githooks/` returns only `gate-legs.json` and `check-playbook-parity.sh`. |
| claims-6 — the OUT item's stated reason is refuted by the code | **CONFIRMED** → F10 | `check-playbook.sh:125-131` `record_for()` joins via `sed -n 's/^piece: //p'`, the record's own field, never the filename. `grep -c playbook-sha tools/unattended/check-playbook.sh` = **0**. The real surface is `playbook.fixture.md:11,12,13,16` plus two `piece:` values. The obstacle the spec never names is `kit.toml:9-11` `include = "**"` / `role = "engine"` (verbatim copy, no placeholder pass), against `SKILL.template.md`'s `role = "rendered"`. |
| specdoc-4 — the class is already filed twice in gov's own backlog, cited nowhere | **CONFIRMED** → F11 | `memory/backlog/TOOL.md:72` — `TOOL-aSealedCaravan-5 · OPEN · ... INERT in a linked worktree: an absolute GIT_DIR ...`; `:142` — `TOOL-aPacedTurnstile-10 · OPEN · Git exports GIT_DIR to a merge driver ... reproduced with one variable`. The spec cites neither. A merge driver is invoked by `git merge`, not by a hook, so §10's "the seam for S2 is `.githooks/pre-push`" does not reach `-10`. |
| specdoc-9 — §3's "Filed as its own backlog row" is false on disk | **CONFIRMED** → F12 | `grep -rn 'playbook.fixture\|playbook-fixture' memory/backlog/` exits 1 with no hits. |
| claims-3 / fixes-4 (part) — "the value reverts later" could not be reproduced | **REFUTED** | It reproduces, in one attempt. After the flip, `core.bare` survived `worktree list`, `fetch`, `status` and `gc`; then `(cd wt && git init -q .)` returned it to `false`. A later `git init` whose cwd IS a worktree of that gitdir is a sufficient reverter, so the spec's sentence stands. |
| fixes-9 — S4 is "unbuildable" because placeholders are shape-identical to documented syntax | **REFUTED** | The spec proposes narrowing to "the ANGLE-BRACKET VALUES the conf actually substitutes" — literals, not a character class. `grep -cF` for `<your-schedule-create-tool>`, `<your-schedule-delete-tool>` and `<e.g. every 10 minutes` against `SKILL.template.md` returns **0, 0, 0**. A literal-token probe is buildable exactly as specced. |
| claims-5 — "32 matches" is a mislabel; "its own probe has never passed" | **REFUTED** | The measurement reproduces: gov's `SKILL.md` is 32 lines / 60 matches, nc's 32 lines / 59. The number is right and only the unit word is loose — a nit, folded as one clause into F8. "Nothing on the merge bar runs a hole probe" is what §4:68-69 and Q3 already say; restating it is not a finding. |
| fixes-7 — AC2 needs a new fixture; marker lookups unaffected | **REFUTED as its own row** | The useful half, that `pre-push.test.sh` builds the non-exporting layout, is real and folded into F3 and F9. The remainder is fix guidance, not a defect in the spec. |
| fixes-12 — version-bump markers omitted from §4 | **REFUTED** | §4's list is labelled "Files touched (**estimate**)", and §3 already scopes "no version bumps beyond what the changed kits require". Conditional on a bump the spec has not committed to. |
| fixes-13 — `exempt_leg` hardcodes the `tools/` prefix | **REFUTED** | A real code fact (`govkit.py:1744`, `ctx = {"kit": f"tools/{eid}", "prefix": "tools", ...}`), but another instance of the prefix class §3 explicitly scopes OUT, and latent: all three shipped unattended probes use root-relative literals, and S4's narrowing needs no `{kit}` token. |
| specdoc-10 — AC5's green-bar clause | **REFUTED** | AC1-AC4 already carry the change-exercising observations; a bar-green regression clause alongside them is normal practice, not the "unrelated green gate" substitution the charter bans. Style. |
| specdoc-11 — S5 says "five defects above" when only four are | **REFUTED** | A wording slip. S5's own body says "S1-S4" and §3 records the OUT item's reason. No decision turns on it. |
| specdoc-12 — a11y / i18n as one bullet rather than two | **REFUTED** | Pure formatting; `check-memory-hygiene.sh` passes on the spec (exit 0, no output). A style complaint dressed as a defect. |

## Not a finding, recorded for completeness

The spec PASSES the hygiene gate — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with no
output on the tree containing it. No conformance defect was found in the document's shape.
