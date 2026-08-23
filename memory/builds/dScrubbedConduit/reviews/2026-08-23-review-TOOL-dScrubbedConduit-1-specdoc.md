# Review — TOOL-dScrubbedConduit-1 (spec rev-1)

**Serves:** spec-audit TOOL-dScrubbedConduit-1

## Verdict: CLEAN WITH FIXES

Lens 3 of 3 — the spec as a document. Three ACs unrunnable as written, a claimed backlog row that did not exist, and a class already filed twice in this backlog. Folded at rev-2.

---

# Spec review — TOOL-dScrubbedConduit-1, document lens

Subject: `memory/builds/dScrubbedConduit/spec/2026-08-23-spec-dScrubbedConduit-1.md`
Repo: `C:/projects/coding-governance/.claude/worktrees/upstream-asks-dScrubbedConduit`, base `abd0f026`
(verified an ancestor of both `main` and `origin/main`). Branch `branch/upstream-asks-dScrubbedConduit`.
Environment: git 2.54.0.windows.1, Git-Bash.

## Gate result — the spec CONFORMS

`bash tools/memory-tree/check-memory-hygiene.sh` → exit 0, zero output (the script's own documented
"clean" signal). The spec IS in check 12's population: it is tracked (`git ls-files | grep
dScrubbedConduit`) and its path matches the check-12 selector at `check-memory-hygiene.sh:757`.
Header parses, ten canonical `##` sections in order, no extra `##`, `streams tooling` is inside
`DISCIPLINES`, filename date 2026-08-23 is at/after all four cutoffs, every acceptance bullet carries
a backticked token, `rev-1` is logged in §9. Status is `OPEN`, so the §8 resolution rule does not bind.

So: no CONFORMANCE finding. Everything below is about whether the document is TRUE and BUILDABLE.

---

## F1 · HIGH · S1 fixes one call site of a three-site class, and AC1 fails on the scoped fix

`gen_build_index.py:493` is the site the spec names, and it is real — reproduced:

    plan RAISED UnicodeDecodeError 'utf-8' codec can't decode byte 0x89 in position 0
      File ...gen_build_index.py, line 128, in read_text

(fixture: the module's own `_fixture()` tree plus a PNG at
`memory/builds/tOne/reviews/obs-spec/shot.png`, i.e. nc's exact shape.)

But `read_text()` is called over arbitrary tracked files at THREE places, and the other two catch
`OSError`, which also does not catch `UnicodeDecodeError`:

| site | function | except | population |
|---|---|---|---|
| `gen_build_index.py:492` | `rosters` | `Problem` | every tracked file under the memory root |
| `gen_build_index.py:351` | `read_bindings` | `OSError` | `record_paths()` — build/, prompts/, reviews/, **any extension** |
| `gen_build_index.py:302` | `spec_ids` | `OSError` | `memory/builds/*/spec/`, **any extension** |

Measured with ONLY line 493 widened (patched copy in the scratchpad, one-line change):

- `read_bindings` still raises on the same PNG.
- The render path swallows it — `gen_build_index.py:1023` is `except Exception: binds_all = {}` — so
  the run completes and **every build's records table silently disappears**:

      --- DIFFERS: memory/builds/tOne/README.md
           Records live under `spec/` and `reviews/`.
          -| Record | Kind | Serves |
          -|---|---|---|
          -| [2026-08-02-review-ARCH-tOne-1-1.md](reviews/...) | spec-audit | ARCH-tOne-1 |

That directly refutes AC1 ("completes and reports **the same artifacts** as without that file") and
S1's justification ("skipping it changes no output"). It is true of `rosters`; it is false of the tool.

Worse, the same class disables a bar leg by absence. Hygiene check 21 shells out at
`check-memory-hygiene.sh:663`:

    b21=$("$_PY" "$HERE/gen_build_index.py" --print-bindings 2>/dev/null || true)

`do_print_bindings` calls `spec_ids` (line 413), which raises on a binary under `spec/` — reproduced:
`do_print_bindings RAISED UnicodeDecodeError`. With stderr discarded and `|| true`, `b21` is empty, so
branches 1, 2 and 4 of check 21 find nothing and branch 3 reads `${n21:-0}`=0 against
`RECORD_UNBOUND_PIN="10"` (`.memory-tree.conf:292`) — the whole check passes while measuring nothing.

Document fix: S1 must name the class rather than the line, and AC1 must be an artifact-EQUALITY
observation. As written, AC1 would be signed off by a run whose records regions had all vanished.

## F2 · HIGH · S2's stated mechanism is wrong, and its "invisible here" row is refuted in this repo

Two separate defects in one item.

**(a) "Git EXPORTS `GIT_DIR` (and friends) into hooks" — not true as stated.** Fixture: plain
top-level clone, `core.hooksPath` set, pre-push hook dumps `env | grep ^GIT_`:

    GIT_EDITOR=true
    GIT_EXEC_PATH=C:/Program Files/Git/mingw64/libexec/git-core
    GIT_PREFIX=
    GIT_SSH=...

No `GIT_DIR`. (pre-commit in the same repo gets `GIT_INDEX_FILE=.git/index` and still no `GIT_DIR`.)

**(b) The real precondition is "the gitdir is not a plain `./.git`", which a LINKED WORKTREE satisfies
— no submodule required.** Same repo, `git worktree add`, push from the worktree:

    GIT_DIR=.../gitenv/work/.git/worktrees/wt

And the damage lands on the SHARED config, not a submodule one:

    before shared: bare=false
    $ cd scratch2 && GIT_DIR=<...>/worktrees/wt git init -q .    # rc 0, creates NOTHING at cwd
    after  shared: bare=true
    $ cd ../work && git status
    fatal: this operation must be run in a work tree

`git rev-parse --show-toplevel`, `git diff` and `git add` all fatal the same way. That is nc's reported
symptom, produced in a top-level clone.

The submodule arm reproduces too (super + `vendor/nc`): pre-push gets
`GIT_DIR=<super>/.git/modules/vendor/nc`, `git init` flips `core.bare` false→true beside the existing
`core.worktree`, and git then says `warning: core.bare and core.worktree do not make sense / fatal:
unable to set up work tree using invalid config`.

Consequences for the document:

- §4's table row `S2 | ... a SUBMODULE | no — gov is a top-level clone` is **false**. gov's charter
  mandates worktree-per-stream, this review is running inside `.claude/worktrees/`, and bar legs run
  `git init` in temp dirs — `gen_build_index.py:1129`, `corpus_ids.py:517`, `govkit/selftest.py`
  (many sites), `lexicon/selftest.py`, `drift-audit/selftest.py:253`.
- §4's "The mechanism behind S2, stated once" would be recorded wrong, and §1's "Four of the five are
  structurally invisible in this repo" over-counts by at least one.
- "(and friends)" is unspecified and dangerous: the exported set here includes `GIT_EXEC_PATH`, which
  must NOT be scrubbed. Name the variables.

## F3 · MED · AC2 mandates the most expensive fixture and under-covers the repo it ships from

AC2: "Observed RED first, in a SUBMODULE fixture". A submodule fixture is constructible — I built one
— but per F2 the cheaper linked-worktree fixture reproduces the identical corruption of the shared
config, and it is the shape gov itself is exposed through. An AC pinned to submodules gates the
adopter's layout and leaves the maintainer's own ungated: "gate the CLASS, not the instance" pointed
the wrong way.

## F4 · MED · the GIT_DIR class is already filed TWICE in this repo's backlog; the spec cites neither

`memory/backlog/TOOL.md`:

- line 72 — `TOOL-aSealedCaravan-5 · OPEN · the row-keyed merge driver is INERT in a linked worktree:
  an absolute GIT_DIR makes ... Hit live`.
- line 142 — `TOOL-aPacedTurnstile-10 · OPEN · ... Git exports GIT_DIR to a merge driver ...
  reproduced with one variable — GIT_DIR=$(git rev-parse --absolute-git-dir) alone flips repo_root()`.

Both OPEN, both hit live IN THIS REPO, and one states in its own words the export behaviour §4 says
gov cannot see. Nothing in the spec references them. §10's "The seam for S2 is `.githooks/pre-push`"
is therefore too narrow twice over: a merge driver is invoked by `git merge`, not by a hook, so
neither Q1 option ("hook, runner, or both") reaches it. Either fold the rows in, or state explicitly
that S2 is scoped to the hook path and the merge-driver injector stays open.

## F5 · MED · S5 is unbuildable as scoped, and Q2(c) has no host for S3

The charter's bar is "a gate OR a documented check"; S5 defers the shape to Q2 and recommends (c),
"fold S1/S3 into their kits' suites". S1 has a host — `python3 tools/memory-tree/gen_build_index.py
--selftest` is the bar leg `build-index selftest`. **S3 has none.**
`tools/memory-tree/kit-dogfood-parity.test.sh` is itself a PRODUCT leg (`gate-legs.json`:
`kit/dogfood doc parity`), not a self-test; nothing tests it —
`grep -rln kit-dogfood-parity tools/ skills/ .githooks/` returns only callers and prose — and
`check-arms.py` excludes `*.test.sh` from its population outright (`check-arms.py:127`), so it is not
even arm-audited. Option (c) therefore costs the same "fifth harness" (b) was rejected for, for one of
its two members. Q2 cannot be resolved without that fact.

## F6 · MED · AC4 can pass while a third of the defect survives, and names the wrong subject

`tools/unattended/.unattended.conf.example` ships three angle-bracket values:

    35:KEEPALIVE_CREATE="<your-schedule-create-tool>"
    36:KEEPALIVE_DELETE="<your-schedule-delete-tool>"
    41:KEEPALIVE_INTERVAL="<e.g. every 10 minutes (cron 3-59/10 * * * *)>"

Measured against the current probe pattern `<[a-z-]+>`: CREATE matches, DELETE matches, **INTERVAL
does not** (spaces, dots, parens). AC4 demands one fixture "carrying an unsubstituted conf value";
picking CREATE satisfies it while INTERVAL stays undetectable under any narrowing that keeps that
character class.

Second half: AC4 says the probe "runs against a correctly-filled SKILL.md". A rendered `SKILL.md`
cannot distinguish a conf-injected `<your-schedule-create-tool>` from the template's own documented
`<slug>` — the substitution is `{{KEEPALIVE_CREATE}}`→value (`adopt-unattended.sh:174-176`) and both
land as identical prose. A narrowed probe must read `.unattended.conf` (or the resolved values), so
AC4's stated subject is stale relative to its own fix.

S4's underlying claim is otherwise CONFIRMED and reproduced here: probe rc 1 in gov with all four
keepalive values correctly filled (`.unattended.conf:33,34,40`), and
`tools/unattended/SKILL.template.md` carries exactly the counts the spec cites — 25 `<slug>`,
6 `<name>`, 3 `<unit-id>`. One number to correct: the spec says "32 matches remaining"; 32 is the LINE
count, the MATCH count is 60 (`grep -oE '<[a-z-]+>' ... | wc -l`).

## F7 · MED · S4's blast radius is unmodelled — the broken probe currently grants a standing exemption

`govkit.exempt_leg` (`govkit.py:1721`, called once at `govkit.py:2513` inside `cmd_apply`) returns
True — leg EXEMPT — when any `blocks_gate` hole's discharge probe exits non-zero:

    if subprocess.run(...).returncode != 0:
        return True          # the hole is genuinely undischarged, right now

`keepalive-tool-names` has `blocks_gate = true` (`tools/unattended/kit.toml:108`) and its probe always
exits non-zero. So today, an apply that installs the unattended kit exempts that kit's three gate legs
(`unattended kit gate`, `playbook validity gate`, `unattended skill wiring`) from the red-after-install
criterion. Narrowing the probe REMOVES that exemption and can turn those legs red in an acceptance
run. §5's `risks` line covers only S1's widened `except` and S3's `--render` semantics; this is not
mentioned anywhere in the document.

(Not on gov's own bar — `matrix.py` only applies the `check-wiring` kit — so §4's "nothing on the
merge bar runs it" stands as written for gov. It is not true of the deployer's apply path.)

## F8 · LOW · AC3's exit-code arm cannot fail, and S3 omits that the failure is exit-0 silent

Reproduced with a temp repo holding the kit, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md` present
and `memory/guides/BUILD-METHOD.md` absent:

    $ bash tools/memory-tree/kit-dogfood-parity.test.sh --render
    kit-parity: rendered memory/HYGIENE.md from ...
    kit-parity: rendered memory/TEMPLATE-SPEC.md from ...
    kit-parity: missing live copy memory/guides/BUILD-METHOD.md
    RC=0                       # already 0, and the file was NOT created
    $ bash tools/memory-tree/kit-dogfood-parity.test.sh --check
    kit-parity: missing live copy memory/guides/BUILD-METHOD.md
    RC=1

S3's mechanism is confirmed (`kit-dogfood-parity.test.sh:77`, `continue` in every mode). Two document
defects: AC3's "WRITES that copy **and exits 0**" — the exit-0 half is already true on the unfixed
code (`:107`, `[ "$MODE" = --render ] && exit 0`), so only the WRITE is an observation that can fail;
and §2's S3 never says the current failure is invisible to any caller that checks rc, which is the
part that makes it survivable inside an adopter's install script.

## F9 · LOW · §3 claims a backlog row that does not exist

"That is a redesign of the fixture's addressing... **Filed as its own backlog row.**" No such row is on
disk: `grep -rn "playbook.fixture" memory/backlog/` returns nothing (hits exist only under
`memory/builds/dScriptedRepeat/reviews/`). The premise of the non-goal IS confirmed —
`tools/unattended/playbook.fixture.md:11-16` hardcodes `tools/unattended/` in `outputs`, `grain`,
`records` and `legs` — but a cut-line whose follow-up is unfiled is a dropped item.

## F10 · LOW · AC5 is the acceptance shape TEMPLATE-SPEC forbids

`memory/TEMPLATE-SPEC.md` §6: "an observation that proves THIS change works ... **Never an unrelated
green gate.**" AC5 is "when `bash tools/run-gates/run-gates.sh` runs, it is green". Its second clause
("every leg this unit touched ran rather than skipped") is a real observation and worth keeping; the
green-bar clause proves nothing about S1-S4, and no AC in the set observes the four fixes together.

## F11 · LOW · S5 says "five", and only four items sit above it

§2's S5 opens "the five defects above get gates" — S1-S4 is four; the fifth defect lives in §3 as a
non-goal. Its own body then says "S1-S4 are each a one-line fix". Whether S5 owes a gate for the
scoped-OUT `playbook.fixture.md` item is left ambiguous at the exact place the charter's
gate-or-documented-check rule binds.

## F12 · LOW · §5 merges two required checklist items

`memory/TEMPLATE-SPEC.md` §5 lists `a11y` and `i18n` as separate bullets, "one line each"; the spec
writes a single `a11y / i18n` line. Check 12 grades `##` sections only, so nothing catches it — a
documented-rule deviation, not a gate failure.

---

## The "structurally invisible" table, verified row by row

| # | spec says | verdict |
|---|---|---|
| S1 | no non-UTF-8 tracked file under the memory root | **TRUE** — decoded every one of `git ls-files -- memory/`; zero failures |
| S2 | no — gov is a top-level clone | **FALSE** — F2; reproduced in a linked worktree of a plain clone, and filed twice already (F4) |
| S3 | gov has always had all three live copies | **TRUE** — `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` all present |
| S4 | yes — gov is exposed too | **TRUE** — probe rc 1 here with all four keepalive values correctly filled |

## Duplicate / already-decided check

- `memory/DECISIONS.md` (91 lines, all families): nothing contradicts or pre-decides S1-S5. No id
  collision — `dScrubbedConduit` appears only in this build's two files.
- `memory/backlog/TOOL.md`: no row for S1, S3, S4 or the OUT item. Two OPEN rows for S2's class (F4).
  Adjacent but distinct: `TOOL-aSealedCaravan-4` (renders are install-prefix-correct but not
  MEMORY_ROOT-correct) sits beside the OUT item's addressing problem without covering it.

## Reproduction assets

In this scratchpad: `repro_s1.py`, `repro_s1b.py`, `repro_s1c.py`, `repro_s1d.py`, `repro_s1e.py`,
`patched/gen_build_index.py` (the one-line S1 fix), `gitenv/` (clone + linked-worktree GIT_DIR
fixtures), `sub/` (submodule fixture), `s3/` (kit-parity first-render fixture).
