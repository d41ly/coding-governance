# Review — TOOL-dScrubbedConduit-1 (spec rev-1)

**Serves:** spec-audit TOOL-dScrubbedConduit-1

## Verdict: BLOCKED

Lens 2 of 3 — would the proposed fixes work? S1 as scoped would DELETE 398 lines of record inventory; Q1 refuted by a live harness failure. The spec could not be built as rev-1 wrote it. Folded at rev-2.

---

# Spec review — TOOL-dScrubbedConduit-1, lens: would the proposed fixes work, and what do they break?

Base `abd0f026` (worktree HEAD `4784788a`). Every claim below was reproduced in a throwaway fixture;
the commands are named inline. Git is `git version 2.54.0.windows.1`, Git-Bash on Windows.

**Verdict: three of the four in-scope fixes do not work as specified.** S1 as written turns a loud
crash into silent repo-wide data loss and still does not make the reported corpus pass. S3's
one-liner leaves the exact adopter case broken while printing success. S4 as specified
("narrow the probe to the angle-bracket values") is not distinguishable at all on the SKILL.md side
and has to move to the conf. S2's fix is correct and safe at the hook, but the spec's premise
("gov is not exposed") is wrong, its severity is understated, and Q1's recommendation is refuted by
a file in this repo.

---

## F1 — S1 is NOT output-neutral. It converts a crash into silent, repo-wide corruption. HIGH

The spec: *"A roster is built from ids in PROSE, so a file that is not text cannot contribute one and
skipping it changes no output. Widen the except."*

`rosters()` is one of **three** unguarded `read_text` loops over tracked files, and they disagree
about which exception they catch:

| site | line | catches | reached by a `.png` under `builds/*/reviews/` |
|---|---|---|---|
| `rosters()` | `gen_build_index.py:493` | `Problem` | YES — crashes today |
| `read_bindings()` | `gen_build_index.py:351-353` | `OSError` | YES — `UnicodeDecodeError` is a `ValueError` |
| `spec_ids()` | `gen_build_index.py:302-306` | `OSError` | only for a binary under `spec/` |

`read_bindings` is called on the render path at `gen_build_index.py:1021-1023` inside a blanket
`except Exception: binds_all = {}`. So with **only** S1 applied, the decode error moves one function
over, is swallowed there, and **every build's bindings map is dropped**.

Measured, on a fixture that is this repo's own `memory/` tree plus one `.png` under
`memory/builds/aBatchedLintel/reviews/obs-spec/`:

```
# unfixed:      UnicodeDecodeError at gen_build_index.py:492, exit 1
# S1 as spec'd: `--check` reports 52 build READMEs "stale — differs from a fresh render"
# S1 as spec'd: `--write` then commits the repair an adopter is told to run:
  53 files changed, 2 insertions(+), 398 deletions(-)
```

The deleted 398 lines are the `| Record | Kind | Serves |` inventory table out of every build README,
plus each README's "Ids no `spec-audit` record has ever named:" line. A crash is recoverable; this is
a green `--write` that erases the derived record inventory tree-wide.

**Fix:** the decode decision belongs in ONE place. Either `read_text` gains a
`read_text_or_none`-style sibling used by all three scanners, or the file-selection functions
(`record_paths`, and the `tracked` filter in `rosters`) exclude non-text members before any read.
Widening one `except` leaves the other two disagreeing and leaves `plan()`'s blanket
`except Exception` free to swallow the next one silently. The blanket catch at `:1021` should also be
narrowed or made loud — a render that silently drops every binding is worse than one that stops.

## F2 — S1 does not achieve its own goal: the reported corpus still reds, at check 21. HIGH

The spec's premise is that nc's screenshot "is a legitimate record". With all three decode sites
widened and the index regenerated, the fixture's hygiene gate says:

```
HYGIENE check 21 FAILED — records under build/, prompts/ or reviews/ whose head carries no conformant Serves line:
  memory/builds/aBatchedLintel/reviews/obs-spec/shot.png — unreadable: 'utf-8' codec can't decode byte 0x89 in position 0
```

`record_paths()` (`gen_build_index.py:310-315`) is documented as "any depth, **ANY extension**", and
`check-memory-hygiene.sh:659-666` fails on every `A` row. A binary can never carry a `**Serves:**`
line, so the design says a binary under a record folder is a defect — which is a *decision the spec
has to make*, not an except to widen.

Two consequences the spec does not budget for:

- Today, the crash makes **check 21 vacuously green**. `check-memory-hygiene.sh:663` runs
  `--print-bindings 2>/dev/null || true`; the crash happens before the first row is printed, `b21` is
  empty, no branch fires, and `${n21:-0}` is 0. So an adopter with a binary record has a check 21
  that reports green while measuring nothing — the green-by-absence class this repo names in its own
  charter. Fixing S1 correctly *turns that check red*, which is right but is a landing consequence.
- `--print-bindings` (`gen_build_index.py:405`, the `do_print_bindings` mode) has **no** guard of any
  kind and dies with a raw traceback; that mode is also what `adopt-memory-tree.sh` calls.

The predicate the lens asked about — skip by path/extension rather than by exception — is the right
one, and it has to be applied at `record_paths`/`tracked` so check 21 stops classifying a screenshot
as an unbound record. Decide it once and both symptoms go away.

## F3 — the proposed except tuple is still wrong at its own call site. MEDIUM

`read_text` (`gen_build_index.py:124-128`) raises exactly two things: `OSError` and
`UnicodeDecodeError`. It never raises `Problem`. So `except Problem` at `:493` is **dead code that
has never caught anything**, and `(Problem, UnicodeDecodeError)` still crashes on the other arm.
Measured — delete a tracked file from the worktree and run `--check`:

```
FileNotFoundError: [Errno 2] No such file or directory: '.../memory/DECISIONS.md'   (gen_build_index.py:127)
```

The two sibling call sites already catch `OSError`. Whatever the fix is, `rosters()` should end up
catching at least what its siblings do.

## F4 — S2's premise is over-broad, and the "gov is not exposed" table row is wrong. HIGH

The spec states flatly: *"Git EXPORTS `GIT_DIR` (and friends) into hooks."* Measured, three layouts,
same git binary:

| layout | `GIT_*` in the pre-push hook env |
|---|---|
| top-level clone | `GIT_EDITOR GIT_EXEC_PATH GIT_PREFIX GIT_SSH` — **no `GIT_DIR`** |
| submodule checkout | `GIT_DIR=<super>/.git/modules/vendor/sub` **is exported** |
| linked worktree | `GIT_DIR=<repo>/.git/worktrees/wt1` **is exported** |

(pre-commit additionally exports `GIT_INDEX_FILE`; pre-push does not.)

The rule is not "hooks get GIT_DIR" but "hooks get GIT_DIR wherever the repo is reached through a
`.git` **file**". That makes §4's table row — *"S2 | needs … a SUBMODULE | gov has it? no — gov is a
top-level clone"* — **false**. gov's own documented layout puts every feature branch in a linked
worktree under `.claude/worktrees/` (AGENTS.md §2 registry, and this review is running in one). A
push from there exports `GIT_DIR`, and `git init` in a temp dir with that value set writes
`core.bare = true` into the **shared common config**:

```
temp dir has .git?  no
after:  git worktree list  ->  .../sub (bare)
        (from the PRIMARY tree) git rev-parse --show-toplevel
        fatal: this operation must be run in a work tree
```

So in gov the same bug bricks the *primary* tree rather than the pushing one. gov is an affected
adopter, not a bystander, and S2's fix should be justified on that ground rather than on nc's.

Sub-note: the spec says *"The value reverts later, which makes it present as a race."* Not
reproduced — `core.bare = true` persisted in the config after the push completed, in both the
submodule and the linked-worktree fixture. If nc saw it revert, something else reverted it, and the
race explanation is unsupported as written.

## F5 — S2's blast radius is understated: the corruption makes the merge bar fail OPEN. HIGH

The spec's checklist says S2's blast radius is *"a leaked GIT_DIR lets a leg write to a repo it was
never pointed at."* It is worse. `.githooks/pre-push:11` is

```bash
top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
```

and after the corruption that command exits 128 (measured, both with and without `GIT_DIR` set). The
hook therefore **exits 0 silently and the entire gate never runs**. `.githooks/pre-commit:5` is the
same shape. So the failure mode is not "a red gate" — it is a landing that skips the authoritative
merge bar and says nothing. That belongs in the spec's security row and in whatever gate S5 lands,
and it is an independent defect worth its own row: a `|| exit 0` on the repo-resolution line means
any repo-resolution failure disables the bar.

## F6 — Q1's "do both" recommendation is refuted by this repo. HIGH

Q1 recommends scrubbing in `run-gates.sh` as well. `run-gates.sh:92` resolves its log directory with
`git rev-parse --git-dir`, which honours `GIT_DIR` — and `run-gates.evidence.test.sh:42` **relies on
that**:

```bash
run() { GIT_DIR="$1" GIT_WORK_TREE="$ROOT" GATE_LEGS="$2" bash "$RUNNER" 2>&1; }
```

Its header (`run-gates.evidence.test.sh:12-14`) says why: *"Executing the real runner in place would
re-run the whole bar recursively and clobber the live gate-last-summary.txt mid-run, so every case
here drives it through GATE_LEGS with its own scratch GIT_DIR."* Measured, one probe leg:

```
GIT_DIR honoured (today)   -> log written to <scratch>/gate-logs/probe.log ; real .git untouched
GIT_DIR scrubbed (Q1)      -> log written to <repo>/.git/gate-logs/probe.log
```

A scrub inside the runner destroys that isolation, sends every evidence case's output into the real
repo, and overwrites the live `gate-last-summary.txt` — the exact outcome the harness exists to
prevent. **Answer to Q1: hook only.** If the concern is a session that runs the bar with an ambient
`GIT_DIR`, the honest instrument is a refusal (a leg that reds when `GIT_DIR` is set and not
`GATE_LEGS`-driven), not a scrub — and note `tools/unattended/unattended.sh:555-561` already treats
an ambient `GIT_DIR` as a **fail**, not something to silently clear.

## F7 — S2's testing plan is optimistic; the hook itself is safe under the unset. MEDIUM

The spec's §5 says *"each kit already ships a self-test; S1-S4 extend those rather than adding new
harnesses."* For S2 that is not available: `.githooks/pre-push.test.sh:20-30` builds its scratch
repo with `git init` + `remote add`, i.e. a **top-level clone** — the one layout that does not export
`GIT_DIR`, so AC2's RED cannot be observed there. AC2 needs a submodule or linked-worktree fixture,
which is a new harness with a real cost, not an extension.

The good news, measured: unsetting is safe for the hook's own git calls. In both the submodule and
the linked-worktree layout, `git rev-parse --git-dir` returns the **identical absolute path** with
`GIT_DIR` set and unset, so the marker lookups at `.githooks/pre-push:62` and `:99`
(`push-main-active`, `gate-full-green`) and the `$(git rev-parse --git-dir)` in `push-main.sh` still
join. `--show-toplevel` at `:11` likewise resolves identically. Nothing in the hook reads `GIT_DIR`
directly. Scrub `GIT_DIR GIT_WORK_TREE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES
GIT_INDEX_FILE GIT_COMMON_DIR GIT_NAMESPACE` at the top of `pre-push`, before line 11.

Do **not** copy the same scrub into `pre-commit` without thought: that hook DOES receive
`GIT_INDEX_FILE`, and a partial commit (`git commit -- <paths>`) runs against a temporary index, so
scrubbing it would make the staged legs at `.githooks/pre-commit:39-52` inspect the wrong index.

## F8 — S3's one-liner leaves the exact adopter case broken, and reports success. MEDIUM

S3 is real: `kit-dogfood-parity.test.sh:77` `continue`s in every mode. Measured on a tree with no
live copies:

```
$ bash tools/memory-tree/kit-dogfood-parity.test.sh --render ; echo $?
kit-parity: missing live copy memory/HYGIENE.md
kit-parity: missing live copy memory/TEMPLATE-SPEC.md
kit-parity: missing live copy memory/guides/BUILD-METHOD.md
0
```

Note the exit code. Line 107 (`[ "$MODE" = --render ] && exit 0`) discards `st` in render mode, so
today's failure is **a skip that looks like a pass** — worth stating in the spec, since this repo's
own §7 names that class.

Now the proposed fix ("render when the mode is `--render`"), implemented as the minimal condition
change and measured:

```
kit-parity: rendered memory/HYGIENE.md from tools/memory-tree/HYGIENE.template.md
kit-parity: rendered memory/TEMPLATE-SPEC.md from tools/memory-tree/SPEC-TEMPLATE.template.md
kit-dogfood-parity.test.sh: line 80: memory/guides/BUILD-METHOD.md: No such file or directory
kit-parity: rendered memory/guides/BUILD-METHOD.md from tools/memory-tree/BUILD-METHOD.template.md
exit 0
```

The redirection at line 80 fails because `memory/guides/` does not exist, the loop prints "rendered"
anyway, and the command still exits 0. **`BUILD-METHOD.md` — the file the spec names as the adopter's
symptom — is exactly the pair that stays broken.** The fix needs `mkdir -p "$(dirname "$live")"` and
a write-failure arm (`render "$ship" > "$live" || { echo …; st=1; continue; }`), and line 107 should
stop swallowing `st`.

`--check` is not weakened by the change: measured exit 1 with the guard moved into the check branch,
and the missing-*shipped*-copy arm at line 78 is untouched, which is what the spec's risk note asks
for.

## F9 — S4 as specified is unbuildable; the workable predicate reads the conf, not the SKILL. HIGH

The spec says to *"Narrow the probe to the ANGLE-BRACKET VALUES the conf actually substitutes."* On
the rendered SKILL.md side those values are **shape-identical** to the template's own documented
syntax:

```
unsubstituted value : KEEPALIVE_CREATE="<your-schedule-create-tool>"    -> matches <[a-z-]+>
documented syntax   : <slug> <name> <unit-id> <halt-code> <check-script> -> matches <[a-z-]+>
```

There is no shape that separates them, so a narrowed *pattern* cannot work; only a narrowed *scope*
(anchored to the template's surrounding prose) could, and that couples the probe to sentence text.

Worse, the current pattern would miss the third value even with perfect scoping:
`KEEPALIVE_INTERVAL="<e.g. every 10 minutes (cron 3-59/10 * * * *)>"` contains spaces, digits and
parens and does **not** match `<[a-z-]+>`.

Proposed predicate, and it reads the conf — which is where the authoring the hole is about actually
happens, and which is what the two sibling holes (`directives-floor`, `core-floor`,
`tools/unattended/kit.toml:112-127`) already do:

```bash
! grep -qE '^(KEEPALIVE_CREATE|KEEPALIVE_DELETE|KEEPALIVE_INTERVAL)="?<' .unattended.conf
```

Both arms observed:

```
gov's live .unattended.conf                  -> DISCHARGED (pass)
tools/unattended/.unattended.conf.example    -> HOLE OPEN (fail)
```

Near-miss scan over the real tree: no other `^[A-Z_]+="?<` line exists in gov's live conf, so the
predicate reds nothing innocent. The spec's own numbers are also slightly mixed — 58 angle-bracket
*occurrences* on 32 *lines* in `SKILL.template.md`; "32 matches" is the line count.

And the spec's §4 row is right that gov is exposed: the current probe fails here today, 32 matching
lines, with all four conf values correctly filled.

## F10 — S4 is not cosmetic: the never-passing probe is a standing gate EXEMPTION. HIGH

The spec frames S4 as *"a hole nobody can close, which is worse than the half-silence"*. The actual
mechanism is stronger. `exempt_leg` (`govkit.py:1721-1752`) grants a leg exemption by **running** the
hole's discharge probe:

```python
if subprocess.run(...).returncode != 0:
    return True          # the hole is genuinely undischarged, right now
```

and its only caller, `govkit.py:2513`, uses that to suppress
`leg '<nm>' did not exist before this install and is red after`. Because the keepalive probe can
never exit 0, and the loop hits it before the kit's other holes, **all three unattended gate legs**
(`unattended kit gate`, `playbook validity gate`, `unattended skill wiring`) are permanently exempt
from the after-install red check in every adopter tree. That is a check that cannot fail, in the
engine whose job is to notice checks that cannot fail.

The landing consequence: fixing the probe **removes** that exemption, so adopters may start seeing
genuinely red unattended legs that govkit has been hiding. Budget it as an expected outcome of S4,
not as a regression introduced by it.

## F11 — Q2's option (c) rests on a wrong premise about S2. MEDIUM

Q2(c) is *"fold S1/S3 into their kits' suites and give S2/S4 a bar leg, since those two are the ones
no suite on the bar covers."* Read from `tools/gate-legs.json`:

- `pre-push self-test` — `bash .githooks/pre-push.test.sh`, guard `[".githooks/", "tools/lib/"]`. **On
  the bar**, and it fires on exactly the diff S2 makes. S2 does not need a new leg; it needs a
  fixture the existing leg can drive (F7).
- `kit/dogfood doc parity` and `build-index selftest` are both on the bar too, so S1 and S3's homes
  are bar-visible already.
- S4 is the only genuinely uncovered one: no bar leg runs a `[[hole]]` discharge probe.
  `govkit selfcheck` is on the bar but only asserts that a hole *has* a probe (`govkit.py:697-705`),
  never that it can pass. Q3's instinct is right and the general gap is real.

Separately, **AC5 is unsatisfiable as written** for the unattended half: AGENTS.md (the merge-bar
section, owner ruling 2026-08-23) removed that kit's seven `*.test.sh` legs from
`tools/gate-legs.json` and from its own `kit.toml`. §7 of the spec acknowledges this; AC5's "every
leg this unit touched ran rather than skipped" contradicts it. Reword AC5 or name the hand-run legs
in it.

## F12 — version discipline: nothing is mechanically obliged, and the spec's file list is short. LOW

`check-kit-versions.sh` asserts internal *agreement*, never that a change bumps anything. So:

- **S2** — `.githooks/pre-push` belongs to the `push-main` govkit entry, whose descriptor declares
  `version_from = { none = "no version constant exists…" }`
  (`tools/govkit/entries/push-main.kit.toml:7`). No version, no bump, no marker.
- **S1, S3** — memory-tree kit. Constant `KIT_MEMORY_TREE_VERSION=2.29`
  (`check-memory-hygiene.sh:13`).
- **S4** — unattended kit. `KIT_UNATTENDED_VERSION=1.8`, in **two** files
  (`unattended.sh:41`, `check-unattended.sh:29`).

None is forced. But S1/S3/S4 are behaviour changes an adopter has to be able to detect, so a bump is
the defensible call — and if it is taken, the SAME commit must move every `gov:kit <kit>@<v>` marker
in that kit's shipped templates or `check-kit-versions.sh:101-151` reds:

- memory-tree: 3 templates (`BUILD-METHOD`, `HYGIENE`, `SPEC-TEMPLATE`).
- unattended: 3 templates (`PLAYBOOK-TEMPLATE`, `PROTOCOL`, `SKILL`) **plus** the same-line markers
  beside both constants.

Add those to §4's "Files touched", where they are currently missing.

## F13 — latent prefix bug in the exemption path, same class as the OUT-scoped item. LOW

`govkit.py:1744` hardcodes the token context used to resolve a discharge command:

```python
ctx = {"kit": f"tools/{eid}", "prefix": "tools", "kit_id": eid, "memory_root": "memory"}
```

An adopter installing kits under `scripts/` — which is exactly the reporter — would get any
`{kit}`-bearing discharge command resolved against `tools/`. All three shipped unattended discharge
commands happen to use root-relative literals, so it is latent today. Worth a backlog row beside the
`playbook.fixture.md` one the spec already files, since it is the same "kit assumes `tools/`" class
and the whole batch exists because that assumption broke for one adopter.

---

## Reproduction index

- fixture A — this repo's `memory/` + `.memory-tree.conf` + `gen_build_index.py` in a fresh
  `git init`, plus one binary at `memory/builds/aBatchedLintel/reviews/obs-spec/shot.png`.
  `--check` before: `build-index: clean (64 artifact(s))`.
- fixture B — fixture A plus the whole `tools/` tree and the root `.conf` files, for
  `check-memory-hygiene.sh` (baseline exit 0).
- fixture C — `git init` super + `git submodule add` sub + a linked worktree off a plain clone,
  with an env-dumping `pre-push` in each gitdir's `hooks/`.
- fixture D — templates + `kit-dogfood-parity.test.sh` + `.memory-tree.conf` only, `memory/` empty.
- fixture E — `good.conf` = this repo's `.unattended.conf`; `bad.conf` =
  `tools/unattended/.unattended.conf.example`.
