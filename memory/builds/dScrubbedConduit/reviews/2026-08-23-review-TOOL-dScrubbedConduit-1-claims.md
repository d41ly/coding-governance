# Review — TOOL-dScrubbedConduit-1 (spec rev-1)

**Serves:** spec-audit TOOL-dScrubbedConduit-1

## Verdict: CLEAN WITH FIXES

Lens 1 of 3 — do the five reported defects reproduce as described? All five DO reproduce; two are described wrongly. Folded at spec rev-2.

---

# Spec review — TOOL-dScrubbedConduit-1, lens: are the five defects real, as described?

Base `abd0f026`; spec at `memory/builds/dScrubbedConduit/spec/2026-08-23-spec-dScrubbedConduit-1.md`.
Every claim below was reproduced with a command, on git 2.54.0.windows.1 under Git-Bash.

## Verdict per item

| # | defect real? | mechanism as described? |
|---|---|---|
| S1 | YES | PARTLY — the crash site named is one of three, and the fix as scoped leaves two |
| S2 | YES | NO — the exposure condition and the "normal clone is safe" reasoning are both wrong |
| S3 | YES | PARTLY — `--render` exits 0, not non-zero; and the fix needs a `mkdir` nobody names |
| S4 | YES | YES — token counts exact; two small imprecisions |
| OUT | symptom YES | NO — the reason given ("the filenames encode the address") is refuted by the code |

---

## F1 — HIGH — S1 fixes one of three call sites; the other two are the ones the adopter's file actually hits

`tools/memory-tree/gen_build_index.py:124-128` `read_text` decodes UTF-8 strictly, so it raises
`UnicodeDecodeError` (a `ValueError`), which `except Problem` at `:493` cannot catch. That much is
exactly as specced — reproduced with a fixture memory tree carrying a real PNG:

    $ python gen_build_index.py --check
    File ".../gen_build_index.py", line 492, in rosters
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte

But `read_text` is called from two more places that are unguarded for this exception, and both are
reached by the very file the report is about:

- `:351` in `read_bindings`, guarded `except OSError`. Its population is `record_paths()` — "any
  depth, ANY extension" under `memory/builds/*/{build,reviews,prompts}/`. The adopter's file is
  `memory/builds/eVerbatimVista/reviews/w5-acceptance/obs-spec/footer-live-e.png`, squarely in it.
- `:302` in `spec_ids`, same `except OSError`, population `memory/builds/*/spec/`.

Applied the spec's own one-line widening to a copy (`except (Problem, OSError, UnicodeDecodeError)`
at `:493`) and re-ran the same fixture:

- `--check` / `--write` now complete. Good.
- `--print-bindings` still tracebacks at `:351`. Live confirmation in the adopter's tree, where
  carve-out 7/15 already applies exactly the specced fix: `python scripts/gen_build_index.py
  --print-bindings` → `UnicodeDecodeError` at `scripts/gen_build_index.py:146`, rc 1.
- `plan()` wraps `read_bindings` in a blanket `except Exception` at `:1022`, so the crash is
  SWALLOWED and `binds_all` becomes `{}`. Two fixtures identical but for the PNG, both rendered
  with the patched generator, diffed:

        23,28d22
        < | Record | Kind | Serves |
        < |---|---|---|
        < | [2026-08-02-review-tOne-1.md](reviews/...) | diff-review | ARCH-tOne-1 |
        < Ids no `spec-audit` record has ever named: ARCH-tOne-1.

  The whole records table and both coverage joins vanish from every build README, identically in
  `--check` and `--write`, so no gate reds.

Two consequences the spec should carry:

1. **AC1 is false as written under the specced fix.** "completes and reports the same artifacts as
   without that file" — it does not. The arm that catches this needs the binary under a *record*
   folder AND at least one `**Serves:**`-bearing record present; a binary anywhere under `memory/`
   is not enough.
2. **check 21 goes green by absence.** `check-memory-hygiene.sh:663` (adopter copy: `:707`) is
   `b21=$(... --print-bindings 2>/dev/null || true)`. On the traceback `b21` is empty, so the A arm,
   the B arm, the N arm (`${n21:-0}` = 0 ≤ pin) and the projection arm all pass on nothing.

Also: `read_bindings`'s docstring at `:340` says "Never raises." It does.

The spec's justification sentence — "a file that is not text cannot contribute one and skipping it
changes no output" — is true of `rosters()` and false of the generator.

## F2 — HIGH — S2's exposure condition is wrong: the damage is not submodule-specific, and gov is exposed

The defect is REAL and reproduced end to end with a real leg from this repo:

    $ git config --file <super>/.git/modules/sub/config --get core.bare   # false
    $ GIT_DIR=<super>/.git/modules/sub bash tools/check-line-length.test.sh   # rc 1
    $ git config --file <super>/.git/modules/sub/config --get core.bare   # true
    $ cd <super>/sub && git status --short
    warning: core.bare and core.worktree do not make sense
    fatal: unable to set up work tree using invalid config

Roughly 30 tracked `*.test.sh` files run `git init`, 39 leg strings in `tools/gate-legs.json` name a
`.test.sh`, and nothing in `.githooks/pre-push` or `tools/run-gates/run-gates.sh` unsets `GIT_DIR`.

Three of the spec's stated mechanics do not hold:

- **"Git EXPORTS `GIT_DIR` (and friends) into hooks."** Not unconditionally. Measured with an
  env-dumping pre-push hook: pushing from a plain top-level clone (from the top level and from a
  subdirectory) the hook sees `GIT_DIR=<unset>` — only `GIT_PREFIX` and `GIT_EXEC_PATH` are set.
  It IS exported when the gitdir is not the default: from a linked worktree the hook sees
  `GIT_DIR=.../work/.git/worktrees/wt`. Submodules are one member of that class, not the class.
- **"For a normal clone ... nothing changes."** False. Pointing `GIT_DIR` at a linked worktree's
  gitdir and running `git init` in a scratch dir flipped `core.bare` `false → true` in the plain
  clone's SHARED config, and its PRIMARY tree then answered
  `fatal: this operation must be run in a work tree`. What protects a normal top-level push is that
  `GIT_DIR` is never exported there — not that `core.bare` re-derives correctly.
- **Design table row "S2 | gov has it? no — gov is a top-level clone."** Gov's charter mandates
  worktree work and this review ran inside `C:/projects/coding-governance/.claude/worktrees/…`,
  whose `git rev-parse --git-dir` is `C:/projects/coding-governance/.git/worktrees/…`. That is the
  exporting shape.

This matters for the fix's test: **AC2 says "Observed RED first, in a SUBMODULE fixture."** A
linked-worktree fixture reproduces it and is cheaper; scoping the arm to submodules leaves the wider
class unexercised. Also measured: `git init <dir>` with an argument does the same damage, and
exporting `GIT_WORK_TREE` alongside `GIT_DIR` is what keeps `core.bare` false.

## F3 — MED — "The value reverts later" could not be reproduced

The spec explains nc's twice-misdiagnosed race with "The value reverts later." Nothing I ran
reverts it. After the flip, `core.bare` stayed `true` through all of:

- `git init` again with `GIT_DIR` set and cwd = the submodule worktree,
- `git init` again with cwd = the gitdir's parent (`.git/modules`),
- `git submodule sync`, `git submodule absorbgitdirs`, `git submodule update --init` in the super.

Only setting `GIT_WORK_TREE` alongside `GIT_DIR` produced `bare=false`. The spec asserts the revert
as observed behaviour; on this git it is not.

Minor, same item: the quoted symptom `fatal: this operation must be run in a work tree` is
command-dependent in a submodule — `git rev-parse --show-toplevel` gives exactly that, while
`git status` gives `warning: core.bare and core.worktree do not make sense` +
`fatal: unable to set up work tree using invalid config`.

## F4 — MED — S3 is real, but `--render` exits 0, and the fix needs a `mkdir` the spec and AC3 omit

`tools/memory-tree/kit-dogfood-parity.test.sh:77` sits above the `case "$MODE"`, so it `continue`s
in `--render` too. Reproduced in a fixture repo holding the kit and only two of the three live copies:

    $ bash tools/memory-tree/kit-dogfood-parity.test.sh --render
    kit-parity: rendered memory/HYGIENE.md from ...
    kit-parity: rendered memory/TEMPLATE-SPEC.md from ...
    kit-parity: missing live copy memory/guides/BUILD-METHOD.md
    rc=0            <-- st=1 is discarded by line 108: [ "$MODE" = --render ] && exit 0
    $ ls memory/guides/     -> still empty
    $ bash ... --check      -> kit-parity: missing live copy ...   rc=1

So "gets `kit-parity: missing live copy` from the command documented as the fix for it, forever" is
right about the message and wrong about the exit status — `--render` reports success.

Second gap, unmentioned: the write is `render "$ship" > "$live"` with no `mkdir -p`. Removed the
directory and reproduced the real first-time-adopter state:

    $ rmdir memory/guides && printf 'x' > memory/guides/BUILD-METHOD.md
    bash: memory/guides/BUILD-METHOD.md: No such file or directory

**AC3 as written ("`--render` … WRITES that copy and exits 0") passes on a fixture that pre-creates
`memory/guides/` while a real adopter still fails.** The AC needs the parent directory absent.

## F5 — LOW — S4 confirmed; two imprecisions, and the "never passed" claim was never actually run

The probe fails in this repo right now:

    $ bash -c "! grep -qE '<[a-z-]+>' .claude/skills/unattended/SKILL.md" ; echo $?
    1

Token tally against the live `.claude/skills/unattended/SKILL.md` and against
`tools/unattended/SKILL.template.md` — identical, and exactly the spec's numbers: 25 `<slug>`,
6 `<name>`, 3 `<unit-id>`, then `<piece>` 3, `<why>` 2, `<text>` 2, `<root>` 2, `<path>` 2, `<n>` 2,
`<label>` 2, `<item>` 2, `<id>` 2, `<handle>` 2, and six singletons.

- **"32 matches remaining" is 32 LINES, 60 matches.** `grep -oE … | wc -l` = 60. Cosmetic, but the
  spec presents it as a measurement.
- **"its own probe has never passed" — it has never been RUN here.** No bar leg runs a discharge
  probe: the only `govkit` legs in `tools/gate-legs.json` are `selfcheck`, `selftest`,
  `refusal_join` and `matrix`. `govkit check --target .` refuses in this repo — "NOT LANDED (no
  .governance/install.json)" — so it never reaches the hole. That strengthens Q3 rather than
  weakening S4, but the sentence claims an observation nobody made.

The proposed narrowing is feasible, checked rather than assumed: the five angle-bracket example
values in `tools/unattended/.unattended.conf.example` (`<MEMORY_ROOT>`, `<dod>`, `<phases>`,
`<your-schedule-create-tool>`, `<your-schedule-delete-tool>`) each occur ZERO times in
`SKILL.template.md`, so a probe on those exact tokens has no collision with the documented syntax.

## F6 — MED — the OUT item's stated reason is refuted by the code it describes

The symptom is real. Copied the kit to `scripts/unattended/` in a fresh repo:

    $ bash scripts/unattended/check-playbook.sh
    PLAYBOOK check 6 FAILED — ... names a leg target that does not resolve in this tree:
      tools/unattended/check-playbook.sh for fixture-shape in scripts/unattended/playbook.fixture.md
    playbook: DEAD PROBE — the grain resolves no piece ...
    rc=1

The reason for scoping it OUT does not hold. The spec says the records "literally encode
`tools~unattended~…` in their FILENAMES" and calls that "a redesign of the fixture's addressing":

- `tools/unattended/check-playbook.sh:125-131` `record_for()` finds a record by reading its own
  `piece:` FIELD, with a comment explicitly refusing to re-derive the writer's naming. **Nothing
  reads those filenames.** They are cosmetic.
- `playbook-sha:` appears in the two piece records and `grep -n playbook-sha check-playbook.sh`
  returns ZERO hits — nothing joins on the fixture's bytes either.

The actual surface is 4 lines — `playbook.fixture.md:11,12,13,16` — plus 2 `piece:` values in
`fixture-records/`. The real obstacle, which the spec does not name, is that the fixture ships under
`kit.toml:9` `[[files]] include = "**" role = "engine"`, i.e. copied verbatim with no placeholder
pass, so the fix means promoting it to `role = "rendered"` with a `KIT_DIR` placeholder (as
`SKILL.template.md` already is) or teaching `check-playbook.sh` to resolve declared paths relative
to the kit dir. Deferring is defensible; the sentence on the page is not the reason.

## Not findings

- S1's crash site `:492-494` is cited correctly, and `Problem` is not a `ValueError` subclass.
- S2's core defect, S3's `continue`, S4's counts and the OUT item's symptom all reproduce.
- Q2's option (c) and Q3 are consistent with what I measured about which legs run.
