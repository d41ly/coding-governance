# TOOL-dScrubbedConduit-1 — five kit defects an adopter found by hitting them

**Status:** CLOSED · rev-3 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Fix five defects reported from `d41ly/nc`, which re-adopted the whole kit set on 2026-08-23. Each was
found by an adopter paying for it. rev-1 claimed four of the five were invisible here; **a review
refuted that for the most severe one — gov is exposed to it too, through linked worktrees, and the
class is already filed twice in gov's own backlog.**

## 2. Scope (IN)

- **S1 — the decode CLASS in `gen_build_index.py`, not one site.** rev-1 proposed widening
  `except Problem` at `:493`. Measured by review: there are THREE sites reading arbitrary tracked
  files — `rosters` (`:492`), `read_bindings` (`:352`) and `spec_ids` (`:307`) — and the latter two
  catch `OSError`, which does not catch `UnicodeDecodeError`. Widening only `:493` makes `--check`
  call 52 READMEs stale and `--write` produce `53 files changed, 2 insertions(+), 398 deletions(-)`,
  **deleting the Record/Kind/Serves table from every build README.** Also measured: `read_text`
  (`:124-128`) raises only `OSError` and `UnicodeDecodeError` and never `Problem`, so the existing
  `except Problem` is DEAD CODE, and the natural `(Problem, UnicodeDecodeError)` reading still dies
  with `FileNotFoundError` on a tracked-but-missing file — which both sibling sites already survive.
  S1 is therefore ONE `read_text_or_none` helper used by all three scanners, catching at least
  `(OSError, UnicodeDecodeError)`; `read_bindings`' "Never raises." docstring at `:340` corrected; and
  the blanket `except Exception` at `:1023` narrowed or made loud.
- **S2 — scrub the injected git environment at the hook boundary.** Corrected mechanism, measured on
  git 2.54.0.windows.1: **a plain top-level clone exports NO `GIT_DIR` into `pre-push`; a repo reached
  through a `.git` FILE does** — a linked worktree exports `GIT_DIR=…/.git/worktrees/<wt>`, and a
  submodule likewise. A leg that then runs `git init` re-initialises THAT gitdir and rewrites its
  shared config. Review flipped gov's own fixture clone's `core.bare` to `true` by running a real bar
  leg under a worktree `GIT_DIR`, with no submodule anywhere. Scrub in `.githooks/pre-push` ONLY (see
  Q1), naming the variables explicitly — **`GIT_EXEC_PATH` must survive.**
- **S3 — `--render` must be able to create a first render, and must not lie when it cannot.** Three
  measured facts, two of which rev-1 missed. The `continue` at `:77` skips a missing live copy in every
  mode. `:107`'s `[ "$MODE" = --render ] && exit 0` DISCARDS `st`, so `--render` already exits 0 today
  while printing `missing live copy` and writing nothing. And the write at `:80` is a bare
  `render > "$live"` with no `mkdir -p`, so a first-time adopter — who has no `memory/guides/` at all —
  gets `No such file or directory`, the line `kit-parity: rendered …`, exit 0, and no file. S3 fixes
  all three: render on `--render`, `mkdir -p` the parent, a write-failure arm, and stop `:107`
  swallowing `st`.
- **S4 — narrow the `keepalive-tool-names` discharge probe, and subject it to the CONF.** The probe
  greps `<[a-z-]+>` over the rendered `SKILL.md`, whose template ships 25 `<slug>` and more as
  documented syntax, so it fails for every adopter forever. Review confirmed the narrowing is
  buildable: the three conf placeholder literals occur ZERO times in `SKILL.template.md`. It also
  found the probe's subject is wrong — a rendered `SKILL.md` cannot distinguish a conf-injected
  placeholder from the template's own syntax without matching literals — and that
  `KEEPALIVE_INTERVAL`'s shipped value `<e.g. every 10 minutes (cron 3-59/10 * * * *)>` does NOT match
  `<[a-z-]+>` at all, so it is undetectable today. Probe `.unattended.conf`'s resolved values, all
  three keys.
- **S5 — the hook must not FAIL OPEN.** New at rev-2, and the most severe item in the unit. Once
  `core.bare` is flipped, `git rev-parse --show-toplevel` exits 128, so `.githooks/pre-push:11`'s
  `|| exit 0` fires and **the hook returns success with the merge bar never having run.** Reproduced
  end to end by review: a push from a bricked primary tree printed `[new branch] main -> main2`,
  exited 0, never printed the gate's marker, and LANDED ON THE REMOTE. `.githooks/pre-commit:5`
  carries the same shape. A hook that cannot resolve its repo has not established that the push is
  safe; it must refuse.
- **S6 — left-shift, with the hosts named rather than deferred.** rev-1 left the gate shape to an open
  question, which the charter does not allow a finding to end in. Per-item hosts, costed by review:
  S1 → the existing `gen_build_index.py --selftest`. S3 → a genuinely new harness or an accepted
  documented check, because `kit-dogfood-parity.test.sh` is itself a bar leg with no self-test. S2/S5
  → a LINKED-WORKTREE fixture inside the existing `pre-push self-test` leg, which today builds
  `git init -q --bare` and `git init -q "$tmp/work"` — the one layout that exports no `GIT_DIR`, so the
  fixture must change for the RED to be observable. S4 → the only item with no host at all.

## 3. Non-goals (OUT)

- **`playbook.fixture.md`'s hardcoded `tools/unattended/` stays OUT, with rev-1's reason RETRACTED.**
  rev-1 said the fixture's records "encode the path in their FILENAMES" and called it a redesign of an
  addressing scheme. Refuted: `check-playbook.sh:125-131` `record_for()` joins on the record's own
  `piece:` FIELD and explicitly refuses to re-derive the writer's naming, so the filenames are
  cosmetic to the join. The REAL obstacle, which rev-1 never named, is `kit.toml:9-11` shipping the
  fixture under `include = "**"` / `role = "engine"` — copied verbatim with no placeholder pass,
  unlike `SKILL.template.md`'s `role = "rendered"`. Fixing it means making the fixture `rendered` with
  a `KIT_DIR` placeholder, or making `check-playbook.sh` resolve declared paths relative to the kit
  dir. Still out — that is a kit-descriptor change with its own blast radius — but out for the true
  reason. **The backlog row is filed by this unit** (rev-1 claimed it already existed; it did not).
- **The merge-driver injector stays OPEN after this unit.** `TOOL-aSealedCaravan-5` and
  `TOOL-aPacedTurnstile-10` record the same `GIT_DIR`-export class reaching a MERGE DRIVER, which
  `git merge` invokes rather than a hook. S2 scrubs at the hook and does not reach them.
- **No adopter-side change.** nc carries local carve-outs for all of these; they stay until nc
  re-adopts.
- **`govkit`'s `seed` role is NOT touched** — nc filed it and WITHDREW it, the premise was false.

## 4. Design

### The mechanism, corrected

Git exports `GIT_DIR` into a hook whenever the repository is reached through a `.git` **FILE** rather
than a `.git` directory. That covers a linked worktree and a submodule alike. `git init` with
`GIT_DIR` set does not create a repo at the cwd — it re-initialises the repo `GIT_DIR` names and
re-derives `core.bare` from whether that path has a worktree of its own. For a plain clone the answer
is yes and nothing changes; for a worktree gitdir or a submodule gitdir the answer is no, `core.bare`
flips to `true`, and every later git call in the owning tree fails.

### Which of these can this repo reproduce — CORRECTED

| # | needs | gov has it? |
|---|---|---|
| S1 | a non-UTF-8 tracked file under the memory root | no — gov's memory tree is all text |
| S2 | a gitdir reached through a `.git` FILE | **YES — every linked worktree; measured here** |
| S3 | a first-time render | no — gov has always had all three live copies |
| S4 | any adopter | **YES — gov's own probe has never passed** |
| S5 | a tree whose repo resolution fails | **YES — reachable from S2** |

rev-1's table claimed four of five were invisible here. Three of the five are in fact reproducible in
gov, and two of those are the severe ones. The reason nobody noticed is not exotic: S4's probe is a
`[[hole]]`, which no bar leg runs, and S2/S5 need a worktree fixture where every existing fixture is a
plain `git init`.

### Prior art in this repo's own backlog

`TOOL-aSealedCaravan-5` records the merge driver going inert in a linked worktree under an absolute
`GIT_DIR`, and notes its e2e fixture is a normal repo and cannot see it — the same fixture-blindness
S6 has to fix. `TOOL-aPacedTurnstile-10` records that git exports `GIT_DIR` to a merge driver,
reproduced with one variable. Both are OPEN. They are the strongest evidence against rev-1's premise
and they bound S2's reach.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · `.githooks/pre-push` · `.githooks/pre-commit` ·
`tools/memory-tree/kit-dogfood-parity.test.sh` · `tools/unattended/kit.toml` ·
`.githooks/pre-push.test.sh` · `tools/memory-tree/gen_build_index.py`'s selftest · `memory/backlog/TOOL.md`.

### Alternatives rejected

- **Scrubbing in `run-gates.sh` too** (rev-1's Q1 recommendation). REFUTED by a live failure in gov's
  own harness — see Q1.
- **Deleting S4's probe.** It exists because the hole is genuinely half-silent. Narrow, don't delete.

## 5. Production-readiness checklist

- **security** — S5 is the real security row, and rev-1 understated it badly. The failure is not "a
  leg writes to the wrong repo"; it is **the authoritative merge bar silently not running while the
  push succeeds.** Measured end to end. S2 removes the cause, S5 removes the fail-open.
- **perf / scale** — N/A.
- **a11y / i18n** — N/A.
- **error / empty / loading states** — S3 IS an empty-state defect, and its current behaviour is
  invisible to any caller checking `rc`.
- **observability** — S2's failure presents as a concurrent-session race; the adopter reported it as
  one twice. Whatever S6 lands must name the mechanism.
- **risks** — (a) widening a decode catch can mask a real failure: mitigated by one shared helper with
  a named exception tuple, not a blanket. (b) **A COMPLETE S1 turns hygiene check 21 RED**, measured:
  `record_paths` admits any extension, so the binary becomes an `A` row and
  `check-memory-hygiene.sh:659-666` fails — and today's crash makes that check VACUOUSLY GREEN because
  `:663` runs under `2>/dev/null || true`. Budgeted here, not discovered later. (c) **S4 removes a
  standing exemption**: `govkit.py:1741` `exempt_leg` suppresses the "red after install" criterion
  whenever any `blocks_gate` hole's probe exits non-zero, and this probe always does — so all three
  unattended gate legs are permanently exempt in every adopter today. Narrowing may surface genuinely
  red legs. (d) changing `--render` semantics could mask a missing TEMPLATE; keep that arm failing.
- **testing + left-shift gates** — S6 names a host per item. Every new arm observed RED before landing.
- **migration / rollback** — none. No stored data, no artifact shape change.
- **user docs** — N/A, kit-internal.

## 6. Acceptance criteria

- **AC1** — When a non-UTF-8 tracked file is added under a build's `reviews/`, `gen_build_index.py
  --write` completes, `memory/LIVE.md` and the ledger are **BYTE-IDENTICAL** to the same tree without
  it, and the build README gains ONLY a folder-inventory link — no record row, and no deletion.
  Measured at build time: byte-identity of the README alone was one notch too strong, because listing
  a file that is genuinely in the folder is honest. rev-1's "the same artifacts" was too weak: the
  398-line deletion satisfied it. Observed RED first.
- **AC2** — When `pre-push` runs a leg that executes `git init` in a temp dir, in a **LINKED WORKTREE**
  (primary arm — the shape gov is exposed through), the shared config's `core.bare` is unchanged. A
  SUBMODULE arm follows, for the `core.worktree` collision. Both observed RED first.
- **AC3** — When `kit-dogfood-parity.test.sh --render` runs against a tree where a live copy AND ITS
  PARENT DIRECTORY are absent, the file exists afterwards with correct content. And `--check` against
  the same absent copy exits non-zero. The exit-0 clause rev-1 attached to the first arm is dropped:
  `--render` already exits 0 today, so it could not fail.
- **AC4** — Three arms, one per conf key, `KEEPALIVE_CREATE`, `KEEPALIVE_DELETE` and
  `KEEPALIVE_INTERVAL`: with the key unsubstituted the probe FAILS; with all three filled it passes.
  `KEEPALIVE_INTERVAL` is the arm that matters, being undetectable under today's predicate.
- **AC5** — When `pre-push` cannot resolve its repository, it exits NON-ZERO and the push is refused.
  Observed against the bricked-tree fixture that currently lands a branch at rc=0.
- **AC6** — After S4 lands, `bash tools/unattended/check-unattended.sh`,
  `bash tools/unattended/check-playbook.sh` and `bash tools/unattended/adopt-unattended.sh --check`
  each exit 0 in an adopter-shaped target, rather than passing via the `exempt_leg` blanket that S4
  removes.
- **AC7** — `bash tools/run-gates/run-gates.sh` is green and every leg this unit touched RAN.

## 7. Gates

The full bar, `bash tools/run-gates/run-gates.sh`. Legs this unit can move: the memory-tree self-tests,
`pre-push self-test`, `kit-dogfood-parity` (itself a leg), `check-kit-versions.sh` if a version
constant moves, `govkit selfcheck` for the `kit.toml` change, and the unattended suites — which are
owner-demand only, so they are run BY HAND and their verdict reported rather than assumed.

## 8. Open questions

- **Q1 — RESOLVED by measurement: hook ONLY.** rev-1 recommended scrubbing in `run-gates.sh` as well.
  Refuted: `run-gates.sh:92` resolves `LOGDIR` from `git rev-parse --git-dir`, and
  `run-gates.evidence.test.sh` deliberately drives the runner with an explicit per-case `GIT_DIR` so
  cases cannot clobber the live summary. With the scrub added, the harness's absent-`GIT_DIR` case
  flips from `rc=2 / refused / 0 files` to `rc=0`, writing into the REAL `.git`. If an ambient
  `GIT_DIR` outside a hook is still a worry, add a REFUSAL rather than a scrub.
- **Q2 — RESOLVED into S6.** rev-1 deferred the gate shape, which the charter does not permit. The
  hosts are named in S6 with review's costing: option (c) was wrong in both directions — S2 needs a
  fixture inside an EXISTING leg rather than a new one, and S3's "fold into its kit's suite" is not
  available because that kit has no suite.
- **Q3 — should `[[hole]]` discharge probes run on the bar?** RESOLVED (agent, 2026-08-23, delegated): NO, not in this unit — filed as `TOOL-dScrubbedConduit-3` instead. S4's
  probe has never passed here and nobody noticed precisely because nothing runs it. Fixing S4 without
  this leaves the next broken probe equally unobserved. Filed rather than built.

## 9. Revision log

- rev-1 · 2026-08-23 · initial draft. Five asks in, one moved to non-goals.
- rev-2 · 2026-08-23 · folded a three-lens adversarial review with a batched skeptic: 31 raw findings,
  9 refuted, 12 confirmed, 5 of them high. The mechanism was wrong (linked worktrees, not just
  submodules — and gov IS exposed), the blast radius was understated (the hook FAILS OPEN and a push
  landed with no bar), S1 was scoped to one of three sites and would have deleted 398 lines of record
  inventory, Q1's recommendation was refuted by gov's own harness, S3 had two more defects than filed,
  the OUT item's reason was wrong, the class was already filed twice in this backlog, and a claimed
  backlog row did not exist. S5 and S6 are new.

- rev-3 · 2026-08-23 · BUILT and CLOSED. S1 became one `read_text_or_none` used by all three
  scanners, plus a decision the review forced into the open: a non-text file is NOT a record, so it is
  excluded where the bytes are read rather than guessed at by extension — which keeps hygiene check 21
  green instead of demanding a Serves line from a PNG. AC1's byte-identity was relaxed one notch at
  build time, and the reason is recorded in the AC: a build README gaining a folder-inventory link for
  a file that is genuinely in the folder is honest, so LIVE.md and the ledger carry the identity claim
  and the README carries "no record row, no deletion". S2/S5 landed in BOTH hooks. S3 needed all three
  fixes the review found. S4's predicate is general — a value wrapped in angle brackets is still a
  placeholder — rather than a literal match, and it catches KEEPALIVE_INTERVAL, which the old probe
  could not see. S6 added arms 16, 16b, 17 and 18 to the pre-push self-test, on a LINKED-WORKTREE
  fixture the harness previously had no shape for. Every arm observed RED before landing, twice over:
  the first attempt at breaking arm 16 was a no-op regex and proved nothing, which is exactly the
  failure mode the rule exists to catch. Bar GREEN 59/59.

## 10. Reuse audit

Still no new machinery for S1/S3/S4 — edits to existing kit files. S1 CONSOLIDATES three ad-hoc
decode sites into one helper, which is the reuse move the charter asks for and which rev-1 missed by
scoping to a single line. S2/S5 edit an existing hook. The only genuinely new surface is S6's fixture
work, and review costed it: S2/S5 extend the EXISTING `pre-push self-test` leg rather than adding one,
and S3 is the single item that needs a new harness or an accepted documented check. The adopter's
local carve-out in nc's `.githooks/pre-push` is the prototype S2 upstreams.
