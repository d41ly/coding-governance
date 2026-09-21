# TOOL-aWokenSentinel-23 — a kit-gate check banning the line count that reads an empty capture as one line: `printf '%s\n'`, `echo` or a here-string into `wc -l` over a captured variable, with the class in `memory/gotchas/`

**Status:** CLOSED · rev-3 · 2026-09-21 · node a · Tier-2 · base 830c46e8 · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-23-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-23-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-23-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-23-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-24 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H3 (round 3, raw id 28): `TOOL-aWokenSentinel-17`'s `check_status_one_line`
counted the verb's stdout with `printf '%s\n' "$_o" | wc -l`, and `printf '%s\n'` on an empty
capture prints one newline, so `wc -l` reads `1` for a verb that wrote NOTHING and the `same`
against `1` passes — the empty case spec 17 §5 said "reds as loudly as `2`" could not fail, which is
the green-by-absence class that unit exists to close, one helper down. The helper is folded at spec
17's rev-2 to `printf '%s' "$_o" | grep -c ''`, which prints `0` on empty and `1` on one line, with a
third reading against a driver copy whose status `printf` is deleted. This unit closes the CLASS
rather than the instance (charter §7, "gate the class"): a check in
`tools/unattended/check-unattended.sh` reds any code line in the kit's shell files that pipes a
captured variable into `wc -l` through `printf '%s\n'`, `echo` or a here-string, and the class is
recorded under `memory/gotchas/` so `gotchas.py --for-diff` names it over any diff that touches a
suite helper. The predicate was run over the real tree before wiring: zero hits, and eight
near-misses in the driver — `printf '%s' "$var" | wc -l`, no newline added — which count embedded
newlines correctly and are the shape the header says it does not red.

## 2. Scope (IN)

- **S1** — A new check in `tools/unattended/check-unattended.sh`, the next free number above the
  gate's high-water at the pass (31 at this unit's base and 32 after unit 11, DERIVED by
  `grep -oE 'fail [0-9]+'`), that greps its OWN population — every `*.sh` beside the checker,
  `*.test.sh` INCLUDED, minus two files excluded by name: the checker itself and
  `check-unattended.test.sh` — for a CODE line matching `(printf '%s\n'|echo) "$<name>" | wc -l`
  or `wc -l <<< "$<name>"`, with any whitespace around the pipe, and `fail <n>`s naming the file,
  the line and the remedy `printf '%s' "$x" | grep -c ''`. The population departs from the
  checker's `KIT_SH` at `check-unattended.sh:2728`, which skips every `*.test.sh`, because the
  instance this class gate exists for lived in a suite helper and a population that skips suites
  cannot see the next one. Zero hits is the pass; the check does not require a positive
  population, because a kit with no such line is the state it exists to keep. Observed by AC1 and
  AC5.
- **S2** — The check's header states what it does NOT check: `printf '%s'` with no newline piped to
  `wc -l` counts embedded newlines and reads an empty capture as `0`, which is the driver's own
  idiom at `unattended.sh:1296` and seven sibling lines and is correct; a count through an
  intermediate command (`grep -o … | wc -l`) is not read; a `wc -l` over a file or a command
  substitution is not read; the checker's own file is outside the population because its grep
  carries the pattern, and `check-unattended.test.sh` is outside it because its arm stages the
  banned bytes and a self-hit would red the close on the suite that proves the check; a comment
  line is not counted; and the population is this check's own and wider than `KIT_SH`, with the
  reason. Observed by AC2.
- **S3** — The check is observed RED on a staged break before it is wired — a copy of
  `unattended.test.sh` in a scratch kit dir with one line `printf '%s\n' "$_o" | wc -l` added,
  graded by a copy of the checker seeded beside it together with a copy of
  `check-unattended.test.sh`, so the scratch run reads the population the close reads — and GREEN
  with the line removed, and GREEN with the near-miss `printf '%s' "$_o" | wc -l` added instead.
  The `echo` and here-string spellings are staged and read RED by `TOOL-aWokenSentinel-28` over the
  same copy. Observed by AC1.
- **S4** — The check joins the kit's own gate suite: one arm in `check-unattended.test.sh` stages
  the `printf` break and reads the refusal, so the `harness arms` leg counts the new `fail` branch
  as armed. The staged line is ASSEMBLED in the arm from fragments — the command word split, the
  variable and the pipe joined at run time — so this suite's own bytes never match the predicate
  and the by-name exclusion of S1 is a second guard, not the only one. Observed by AC3 and AC5.
- **S5** — A new class in `memory/gotchas/`, `line-count-reads-empty-capture-as-one.md`, in that
  folder's grammar — front matter `name`, `description`, `kind: class`, and a body whose backticked
  paths are its DERIVED anchors — naming the suite the helper lives in and the checker that gates
  it, so `gotchas.py --for-diff` selects it for any diff touching either; the body carries the
  `gated by` sentence check 18 reads, and `memory/gotchas/INDEX.md` is regenerated by
  `gotchas.py --write` in the same commit, which check 17 compares. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to `check_status_one_line`.** The `grep -c ''` count and the empty-copy reading are
  spec 17's rev-2; this unit is why the next helper cannot repeat the shape.
- **No scan outside the kit.** The population is every `*.sh` beside the checker, suites
  included, which is THIS check's own population and not `KIT_SH`'s: no existing check in the
  gate reads a suite (`check-unattended.sh:2729` skips `*.test.sh`, `TOOL-aDeferredBar-4` records
  why), and unit 11's check reads three named files. `tools/lib/resolve-python.test.sh:186` pipes
  a function's output into `wc -l`, which is not a captured variable and is outside both the
  predicate and the population. The repo-wide home — a CLASSES row in
  `tools/gate-lint/sh_hygiene.py`, whose population is every tracked `*.sh` — was weighed at
  rev-2 and not taken; §4 says why, and the gotcha record anchors that scanner's population
  statement so the class is named over a diff there too.
- **No ban on `wc -l`.** Eight lines in the driver use it correctly over `printf '%s'`; the defect
  is the newline `printf '%s\n'`, `echo` and `<<<` add before the count, and the predicate is those
  three spellings and nothing wider.
- **No generalisation to other idioms.** A gate over every empty-input-reads-as-one shape is a
  lexicon-shaped project; this check binds the one shape this build's spec set produced.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-17` — the helper that carried the instance and the
  `grep -c ''` spelling the remedy sentence names; without the fold the check would red the tree
  it lands on.
- **consumes-from** external — `tools/unattended/check-unattended.sh`'s `fail()` at `:93`, its
  `$HERE` and `$_LIB_DIR` derivations, its check-numbering high-water as it stands at the pass
  (unit 11's check lands one number above 31 at order 4, and this one takes the next free), and
  its suite's scratch-kit seeding at
  `check-unattended.test.sh:65`; `tools/memory-tree/gotchas.py`'s checks 17 to 19 and the
  `destructive-step-before-its-precondition` record unit 12 writes, whose shape this one copies.
- **hands-off** `TOOL-aWokenSentinel-28` — the `echo` and here-string staged lines and their RED
  readings in this unit's suite arm, over the same suite copy, so every top-level branch of the
  predicate has been seen to fail; this unit stages the `printf` line only.
- **hands-off** external — nothing.

## 4. Design

### The check

In `tools/unattended/check-unattended.sh`, after the highest check at the pass, in the checker's
own idiom (`# ---- check <n>`, a `fail <n>` with a sentence that names the remedy):

```
# POPULATION: this check's OWN, not KIT_SH — every *.sh here INCLUDING the suites, because the
# instance lived in a suite helper. Two files out by name: this checker (its grep carries the
# pattern) and check-unattended.test.sh (its arm stages the banned bytes).
_lc_hits=""
for _lc_f in "$HERE"/*.sh; do
  case "$(basename "$_lc_f")" in "$(basename "$0")"|check-unattended.test.sh) continue ;; esac
  _lc_h=$(grep -nE "^[^#]*((printf '%s\\\\n'|echo) \"\\\$[A-Za-z_][A-Za-z0-9_]*\"[[:space:]]*\|[[:space:]]*wc -l|wc -l[[:space:]]*<<<[[:space:]]*\"\\\$[A-Za-z_][A-Za-z0-9_]*\")" "$_lc_f" || true)
  [ -n "$_lc_h" ] && _lc_hits="$_lc_hits$(basename "$_lc_f"):$_lc_h"$'\n'
done
[ -z "$_lc_hits" ] || fail <n> "a shell file in this kit counts a captured variable's lines by adding a newline first — printf '%s\n', echo or a here-string into wc -l — which reads an EMPTY capture as one line, so an assertion on the count passes on a command that wrote nothing; count with printf '%s' \"\$x\" | grep -c '' instead, which reads empty as 0. hits: $_lc_hits"
```

The exact escaping of the pattern is the pass's to get right against the fixture of S3 for the
`printf` group, and against unit 28's two staged lines for the `echo` spelling and the here-string
alternation — three fixtures for three spellings, one per top-level case the regex can take, so no
branch lands unseen; the four facts the block must hold are the population (every `*.sh` beside
the checker, suites included, the checker and its suite excluded by name), the three spellings,
the code-line anchor `^[^#]*`, and the remedy in the sentence. `grep -c ''` counts lines the way `wc -l` does on non-empty input — a final line with
no trailing newline still counts, which `wc -l` misses — and reads `0` on empty input, which is the
one property the helper needs.

### What it cannot see, in its header

- `printf '%s' "$x" | wc -l`, no newline: correct, counts embedded newlines, reads empty as `0`.
  The driver's idiom at `unattended.sh:1296` and seven siblings; not a hit.
- A count through an intermediate command, `printf '%s\n' "$x" | grep -o … | wc -l`, at
  `unattended.test.sh:1512`: the newline reaches `grep`, not `wc`; not read.
- A `wc -l` over a file or a `$(…)`: outside the predicate.
- The checker's own source, which carries the pattern inside its grep: excluded by name.
- `check-unattended.test.sh`, whose arm stages the banned line into a suite copy: excluded by
  name, and its staged line is assembled from fragments besides, so the exclusion is a second
  guard and not the only one.
- A comment line: not counted, by the anchor; the edit that uncomments it is the one this reds.
- Any `*.sh` outside `tools/unattended/`: the population is the kit's, wider than `KIT_SH` by the
  suites and no wider; the repo-wide scanner is `tools/gate-lint/sh_hygiene.py` and this class is
  not a row there (see Alternatives rejected).
- A capture counted through a variable that holds the count already: not a line count.

### The staged break, and the near-miss beside it

A scratch kit dir under a short `%TEMP%` path seeded the way `check-unattended.test.sh` seeds its
fixture — the checker, the driver, the library and the two templates copied beside each other —
plus a copy of `check-unattended.test.sh`, which the suite's own fixture at `:65` does not copy
and this one must, because that file is in the population the close reads and a scratch run that
omits it cannot see a self-hit; plus a copy of `unattended.test.sh` with one line appended inside
a function body: `_x=$(printf '%s\n' "$_o" | wc -l)`. The copied checker prints the new `fail`
sentence naming `unattended.test.sh` and that line, and exits 1. The same copy with the line
removed prints no failure for this check; the same copy with `_x=$(printf '%s' "$_o" | wc -l)`
appended instead — the near-miss — prints no failure either, which the pass prints beside the hit
before wiring, per charter §7. The checker runs whole, so each observation costs one kit-gate run,
199 s on node `a` by the gate ledger on 2026-09-20 as spec 11 read it. The `echo` line and the
here-string line are unit 28's, over this same copy.

In the suite arm the staged line is not a literal: `_lc_cmd="pri""ntf"` and the pipe joined at run
time, so `check-unattended.test.sh` never carries `printf '%s\n' "$_o" | wc -l` contiguously on a
code line; the quoted-heredoc idiom the suite uses elsewhere (`:188`) would put those exact bytes
on a non-comment line the `^[^#]*` predicate matches.

### The class, in `memory/gotchas/`

One file in the folder's grammar: front matter `name: line-count-reads-empty-capture-as-one`, a
one-line `description`, `kind: class`; the body states the class — a line count over a captured
variable that adds a newline before counting reads an empty capture as one line, so a one-line
assertion cannot fail on a command that wrote nothing — the instance, spec 17's helper at its
rev-1, the measurement (`_o=""; printf '%s\n' "$_o" | wc -l` prints `1`;
`printf '%s' "$_o" | grep -c ''` prints `0`), the remedy in one sentence, and the gate sentence
check 18 requires of a `kind: class` record — `gated by` this unit's check in
`tools/unattended/check-unattended.sh` — because a class that names no gate and does not say it has
none reds `tools/memory-tree/gotchas.py --check` at the close. Anchors are DERIVED by `gotchas.py`
from the backticked path-like tokens in the body, so the body cites
`tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.sh` and — as the
repo-wide scanner where the class would be a CLASSES row if it ever leaves this kit —
`tools/gate-lint/sh_hygiene.py`, and `--for-diff` prints the class over any diff that touches any
of the three. `memory/gotchas/INDEX.md` is regenerated by `gotchas.py --write` in the same commit,
or check 17 reds.

### Inventory

| identifier | kind | cell |
|---|---|---|
| one `fail <n>` number | a check in the kit gate | derived at build time, next free above the high-water at the pass |
| `memory/gotchas/line-count-reads-empty-capture-as-one.md` | gotcha class | no cell; the folder's grammar |

No function, key, verb or file under `tools/` is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.sh` | one check with its header |
| `tools/unattended/check-unattended.test.sh` | one arm: the staged line reads the refusal; the near-miss line reads none; restored, the check passes |
| `memory/gotchas/line-count-reads-empty-capture-as-one.md` | new, naming its gate |
| `memory/gotchas/INDEX.md` | regenerated by `gotchas.py --write` |
| `memory/map/features/unattended.md` | the new class claimed under `gotcha-classes` — a gotcha record is an inventory key, and the map coverage leg reds an unclaimed one (unit 12's follow-up commit is the precedent) |
| `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json` | re-rendered by `gen_map.py --write` in the same commit |

### Alternatives rejected

- **A gotcha record alone.** The report's minimum. A class that one grep can gate is a class the
  charter says to gate; a documented check is for what cannot be.
- **A lens brief for the spec audit.** The audit reads specs, not suites, and the next helper is
  written in a pass the audit never sees.
- **Widen to every `| wc -l`.** Reds the driver's eight correct lines and the suite's `grep -o`
  count; the defect is the added newline, so the predicate is the three spellings that add one.
- **Home the check in `check-arms.py`.** That tool discovers gates by a `fail() {` helper and
  reads suites only as arm carriers; a shell-idiom scan belongs in a gate that reads shell files,
  and this check derives its own population for that (rev-1 said unit 11's check "already reads
  the same files", which is false — it reads three named files).
- **Home the class in `tools/gate-lint/sh_hygiene.py` as a CLASSES row.** The repo-wide scanner:
  population every tracked `*.sh` (`:205`), a CLASSES table at `:78`, comment stripping, a
  shrink-only registry and a `--selftest` in both directions, on a `subject = repo` leg; the
  retired-launcher ban at `tools/lib/resolve-python.test.sh:113` is the same shape. It is the
  wider gate and would be the smaller diff over an empty tree. Not taken at rev-2, and the reason
  is one of authority rather than taste: this unit was promoted at round 3 as "a kit-gate check",
  its mechanism is recorded in the run-state row and the roster, and moving the home is a change
  of mechanism, which BUILD-METHOD M2 routes through AMEND — RETIRE or SUPERSEDE — and not
  through a fold, which is the only disposition a MEDIUM admits. What a kit home costs is stated
  in §3: the class is gated over this kit's directory, and a suite helper under `tools/workflows/`
  or `tools/lib/` is not read. The gotcha record anchors `tools/gate-lint/sh_hygiene.py` so a
  diff there is shown the class, and the row is the follow-up if a second kit ever produces the
  instance.

## 5. Production-readiness checklist

- security — N/A; a grep over the kit's tracked scripts.
- perf / scale — one grep per shell file beside the checker, milliseconds, inside a leg that
  already reads them.
- error / empty / loading states — a kit with no `*.sh` beside the checker is check 1's refusal
  before this one runs; zero hits is the pass and says nothing, which is the honest reading of a
  ban.
- observability — the refusal prints every hit as `file:line:text` and the remedy.
- risks — a fourth spelling of the same defect (`printf '%s\n' "${x}"` with braces, or a variable
  not immediately quoted) passes; the header says so and the gotcha record names the class rather
  than the spellings.
- testing — the staged break and the near-miss of S3 in the pass; the suite's arm at the close.
- migration — additive; a new check number and a new record.
- user docs — none; the check's header and the gotcha record.

## 6. Acceptance criteria

- **AC1** — When a scratch kit dir seeded as §4 states — the suite's five files plus the kit gate's
  own suite, copied by `cp tools/unattended/check-unattended.test.sh <kit>/` — holds a copy of the driver suite made by
  `cp tools/unattended/unattended.test.sh <kit>/` with `_x=$(printf '%s\n' "$_o" | wc -l)` appended
  inside a function, the copied checker beside it prints `UNATTENDED check <n> FAILED` naming the
  copy's basename and the line and no other file, and exits 1; with the line removed the same run
  prints no failure for that check; with `_x=$(printf '%s' "$_o" | wc -l)` appended instead it
  prints no failure for that check either.
  Red when: the added-newline count passes, which is the check reading the wrong spelling or the
  wrong population; or the near-miss reds, which bans the driver's own correct idiom; or the
  unmodified population fails, which is spec 17's rev-2 not having landed the `grep -c ''` form;
  or the refusal names the kit gate's own suite file, which is the arm's own staged bytes read as
  a hit — the self-hit the close would red on.
  fixture: a scratch kit dir under a short `%TEMP%` path, never this worktree, holding the suite
  copy the fixture at `check-unattended.test.sh:65` omits.
  cost: one whole kit-gate run per observation, 199 s each on node `a` by the gate ledger on
  2026-09-20 as spec 11 read it; the pass runs it three times, on the break, the restored copy and
  the near-miss.
  figure: 199 is PINNED as read by spec 11 from `<git-dir>/gate-ledger.tsv` on 2026-09-20.
- **AC2** — When `grep -c 'does NOT check' tools/unattended/check-unattended.sh` is compared
  between this unit's base and tip, the tip is one higher, and the new check's header names the
  no-newline `printf '%s'` idiom, the intermediate-command count and the checker's own exclusion
  as outside its reach.
  Red when: the header claims a semantic it does not have, which is the false-confidence class
  charter §7 names.
- **AC3** — When `python3 tools/memory-tree/check-arms.py --report` runs at the tip, filtered to
  `check-unattended.sh`, it lists the new `fail` branch as armed, and
  `grep -c 'reads an EMPTY capture as one line' tools/unattended/check-unattended.test.sh` prints
  at least 1 and 0 at this unit's base.
  Red when: the branch is unarmed, which the `harness arms (fail branches armed or pinned)` leg
  reds at the close; or the arm exists but never reads the refusal's text.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-diff <base>..<tip>` runs over a range
  whose `git diff --name-only` lists the driver suite, its stdout names
  `line-count-reads-empty-capture-as-one`; the same tool's report mode does not list the record as
  unanchored; `python tools/memory-tree/gotchas.py --check` exits 0 at the tip, which is check
  17's index freshness and check 18's gate sentence together; and the file's front matter parses
  under the folder's grammar so `memory hygiene` reads it.
  Red when: the class is written but reaches no path, which the tool reports as unanchored and is
  a gotcha nobody is shown; or `--check` reds on a stale `INDEX.md` or a class naming no gate,
  which the memory hygiene leg reds at the close.
- **AC5** — When the check's own predicate — the pattern of §4, `^[^#]*`-anchored — is grepped
  with `grep -cE` over the kit gate's own suite file, the one §7's `New arm:` line names, at the
  tip, it prints 0, and
  `grep -c 'check-unattended.test.sh) continue' tools/unattended/check-unattended.sh` prints at
  least 1 on the new check's population loop.
  Red when: the suite carries the banned bytes contiguously on a code line, which the by-name
  exclusion hides at the close and this criterion does not; or the exclusion is absent, which is
  the population claim of rev-1 landing as written.
  figure: both counts are DERIVED by the greps at observation.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the checker over the
three suite copies of AC1 in a scratch kit dir, the greps of AC2 and AC3, and the `gotchas.py`
reads of AC4. Under `unattended kit gate`, the new check is the arm this unit adds; under
`harness arms`, its `fail` branch is the count it moves; under `memory hygiene`, checks 17 to 19
read the new record.

New arm: `tools/unattended/check-unattended.test.sh` · the staged added-newline `printf` count in a suite copy, assembled from fragments, the same line without the newline (the near-miss, green), and the restored copy; the `echo` and here-string lines are unit 28's · `FLOOR_ASSERTIONS` at `check-unattended.test.sh:3252` and the floor of the shard the arm joins rise by its executed count

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-09-21 · §4 · at the build pass: the Files-touched estimate gains the unattended
  dossier's `gotcha-classes` claim and the two generated map files it re-renders, because a new
  gotcha record is an inventory key the map coverage leg reds unclaimed (unit 12 paid this as a
  follow-up commit); the check's header names the repo-wide scanner by kit and basename rather
  than by its path, because the checker's row in the carried-prefix ratchet is shrink-only and a
  new kit literal in it reds the install-prefix leg; the AC1 fixture was the suite's own preamble
  sourced under `bash -c` with `$0` set to the suite (so `HERE` derives to the kit) and `TMPDIR`
  pointed at a short `%TEMP%` path, which reads the population the close reads and cost 14 s per
  checker run on node `a` rather than the 199 s the ledger prices a contended bar leg at; the
  new check landed as 33, one above the high-water of 32 at the pass. No mechanism changed.
- rev-2 · 2026-09-20 · S1 · S2 · S3 · S4 · §3 · §4 · AC1 · AC5 · §7 · §10 · folded spec-audit
  round 4: sibling agreement for the promoted `TOOL-aWokenSentinel-28` (H6, raw 2) — S3 and AC1
  stage the `printf` line only and say so, the `echo` and here-string readings are handed off by
  edge, and §4 names three fixtures for three spellings; M6 (raw 16) — the population INCLUDES
  `*.test.sh` and excludes the checker and `check-unattended.test.sh` by name with the header
  saying why, the suite arm assembles its staged line from fragments, AC1's fixture copies the
  suite so the scratch run reads what the close reads, and AC5 greps the suite for the bytes; M7
  (raw 35) — §3 and §4 no longer claim `KIT_SH`'s population or that unit 11 reads the same
  files, the `sh_hygiene.py` home is weighed in Alternatives rejected with the reason it was not
  taken, and the gotcha anchors that scanner.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 3 as the
  promotion of H3 (raw id 28): the helper's count is spec 17's rev-2 fold, and the class gate and
  its record are this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count the lines of a captured shell variable without
reading an empty capture as one line"` ranked `read_text` in `tools/memory-tree/gen_build_index.py`
and the `read` seam across six memory-tree modules, Python readers with no bearing on a shell
count, and reported `unscanned layers: .sh`; no existing seam fits. The seam, read at source, is
the kit gate's own idiom — `tools/unattended/check-unattended.sh`'s `fail()` at `:93`, its `$HERE`
at `:68`, and the check-shape unit 11 adds over the same population — and the gotcha folder's
grammar as `tools/memory-tree/gotchas.py` reads it (checks 17 to 19 at `:279` to `:292`), with
unit 12's `destructive-step-before-its-precondition` record as the copied shape. The candidate
predicate was run over `tools/` before this spec was written: zero hits under `--include='*.sh'`,
eight near-misses in `tools/unattended/unattended.sh` (`printf '%s'`, no newline) and one at
`unattended.test.sh:1512` (a `grep -o` between the `printf` and the `wc`). `reuse_lookup.py`
reports `unscanned layers: .sh`, so its miss says nothing about shell seams, and the two that
exist were read at source at rev-2: `tools/gate-lint/sh_hygiene.py`'s CLASSES table over every
tracked `*.sh`, and the retired-launcher ban at `tools/lib/resolve-python.test.sh:113`; both are a
repo-wide home for a shell-idiom ban, weighed in §4 and not taken for the reason given there. The recall probe
returned `TOOL-aBranchedMandate-5` (an empty render against an empty Skill is a PASS — the same
class one kit over), this build's round-3 audit at the H3 paragraph, and
`TOOL-aSurfacedLexicon-21` (a checker reading GREEN over a population it never scanned); no prior
record names the added-newline line count.

Recall terms used: `wc -l printf newline empty capture one line grep -c kit gate idiom ban class scan test.sh helper green-by-absence`
