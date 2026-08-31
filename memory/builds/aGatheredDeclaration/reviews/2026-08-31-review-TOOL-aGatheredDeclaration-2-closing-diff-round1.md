**Serves:** diff-review TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8

# Closing diff review — aGatheredDeclaration, round 1

Tier-2 closing review of the build's cumulative diff. Adversarial fan of finder lenses → skeptics
prompted to refute → this synthesis. Severity below is what THIS report adjudicated, not what a
finder proposed; several findings were merged and a few were moved in both directions, and every
move is stated in its own row. Nothing confirmed was dropped.

Range `44734f152c0f6a2d7ea5c6438dc969de8a7e9f33...HEAD` (HEAD = `d43710c5`, tree clean). ROUND 1.

## Verdict: BLOCKED

Four blockers. Three of them are this repo's own merge bar, red right now at HEAD, re-run by hand
while writing this report — `govkit selfcheck` exits 1, `codebase-map coverage + freshness` exits 1,
`lexicon naming predicates` exits 1. All three legs are `opt_in = false` with no guard that spares
them, so the bar cannot go green as this branch stands and the push boundary will refuse it. All
three are one-commit repairs. The fourth ships a leg to adopters that dies with a traceback instead
of grading anything, which is a red bar in every tree that installs this kit.

The eight highs are not repairs of the same kind. They are the class this build's HUNT named: a
declared table nothing reads, a parity claim nobody makes, a parity ARM proven unable to fail, a
filter the new delegation walks past, a durable failure record that names no leg. None of them reds
anything today, which is the point.

## Review shape

| | |
|---|---|
| raw findings | 47 |
| confirmed | 44 |
| refuted | 3 |
| unverified | 0 |
| precision | 0.94 |
| distinct defects after de-duplication | 26 |
| blockers / highs / mediums / lows | 4 / 8 / 11 / 3 |

The 44 confirmed findings collapse to 26 distinct defects. The heaviest duplication is the
pre-push/runner declaration split (four independent finders) and the dead `[[profile]]` table
(three) — convergence from separate lenses, not one finder repeating itself.

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| 1 | BLOCKER | `tools/govkit/registry.toml:173` | `tools/gate-legs.toml` claimed by no entry or exemption — `govkit selfcheck` RED |
| 2 | BLOCKER | `memory/map/generated/symbols.json:247` | generated map not regenerated for `upgrade_manifest.py` — freshness leg RED |
| 3 | BLOCKER | `tools/run-gates/upgrade_manifest.py:41` | four new defs push verb offenders 463 → 467 past the pin — lexicon leg RED |
| 4 | BLOCKER | `tools/run-gates/run-gates.test.sh:57` | both canaries resolve `gate-legs.toml` unconditionally; the runner falls back — the leg dies where the bar still runs |
| 5 | HIGH | `.githooks/pre-push:240` | the gate invocation still hardcodes `tools/run-gates/run-gates.sh` in the commit that made its siblings prefix-aware |
| 6 | HIGH | `tools/run-gates/run-gates.sh:1244` | the tool probe runs before the shard filter — a leg the operator did not name reds the run |
| 7 | HIGH | `tools/gate-legs.toml:92` | the `[[profile]]` rows are a dead declaration; the runner still reads `gate-profiles.txt` |
| 8 | HIGH | `tools/run-gates/run-gates.sh:151` | nothing asserts the two permanently-live declarations agree |
| 9 | HIGH | `tools/unattended/run-unattended-gates.sh:181` | the delegated block sits outside the `$ONLY` filter and makes the liveness assertion unreachable |
| 10 | HIGH | `tools/run-gates/run-gates.sh:1561` | the `notool` verdict never reaches `FAILED_LEGS` — the durable record names no leg |
| 11 | HIGH | `tools/run-gates/run-gates.gov.test.sh:151` | G2's source-parity arm greps a dead assignment; proven unable to fail |
| 12 | HIGH | `tools/run-gates/upgrade_manifest.py:183` | `cwd` is emitted and whitelisted and honoured nowhere — a leg silently grades the wrong subject |
| 13 | MEDIUM | `.githooks/pre-push:213` | predicate 7 picks the declaration by existence, the runner by `tomllib` — force-full-forever below 3.11 |
| 14 | MEDIUM | `.githooks/pre-push:226` | predicate 8 reads only `GATE_SELFTESTS`; the new primary spelling `GATE_OPTIN` bypasses it |
| 15 | MEDIUM | `tools/run-gates/run-gates.sh:1322` | `--manifest` renders `notool` as `held` — a will-fail leg reported as a withheld one |
| 16 | MEDIUM | `tools/run-gates/run-gates.sh:995` | `--manifest`, a declared read-only verb, creates a run dir and repoints `gate-run/current` |
| 17 | MEDIUM | `tools/run-gates/run-gates.sh:1334` | `[ "${prof_c:-live}" = live ]` can never be true — every `--manifest` row prints `declared-only` |
| 18 | MEDIUM | `tools/run-gates/run-gates.sh:201` | `[bar].turnstile_ttl` and `[bar].default_ceiling` are parsed, validated, and never read in the shell |
| 19 | MEDIUM | `tools/run-gates/run-gates.test.sh:300` | both "shipped default" arms drive JSON fixtures — `[bar]` has no coverage at all |
| 20 | MEDIUM | `tools/gate-legs.toml:785` | the gov canary's guard names only `gate-legs.json`, so a declaration-only edit skips its own grader |
| 21 | MEDIUM | `tools/unattended/run-unattended-gates.sh:45` | three `BUDGET_*` ceilings still declared, still summed by `--help`, now enforced by nothing |
| 22 | MEDIUM | `tools/run-gates/upgrade_manifest.py:230` | a failed `git ls-files` reads as an empty repo and prints "nothing to repoint" |
| 23 | MEDIUM | `tools/run-gates/run-gates.sh:1657` | `chunk_close` was never amended for `shardout` — a chunk of only not-named legs reports green |
| 24 | LOW | `tools/run-gates/run-gates.sh:1844` | the `selftests` stamp lost its 0/1 normalization and now writes the raw env value |
| 25 | LOW | `tools/run-gates/run-gates.sh:69` | `--leg` silently overrides `--list` and `--manifest`, turning a query into an execution |
| 26 | LOW | `tools/run-gates/upgrade_manifest.py:90` | the converter's profile parser is stricter than the runner's on indented comments |

---

## BLOCKERS

### 1 — `tools/gate-legs.toml` is outside the declared-population census

**`tools/govkit/registry.toml:173`**

Reproduced at HEAD: `python tools/govkit/govkit.py selfcheck` exits 1 with `surface 59 tracked
path(s) · 25 entr(y|ies) · 17 exemption(s) · 1 unclaimed` and `tracked path 'tools/gate-legs.toml'
is in the declared surface but is neither an entry member nor an exemption`. At base `44734f1` the
same leg reports `surface 58 … 0 unclaimed`, exit 0.

The leg carries `opt_in = false` and no guard, so it runs on every bar including the authoritative
push-boundary run. The irony is load-bearing rather than decorative: the file the bar now reads to
decide what to check is itself outside the census that exists to red on exactly this.

**Fix.** Add `[[exempt]] path = "tools/gate-legs.toml"` beside the `gate-legs.json` row at
`registry.toml:172-174` with the same reasoning, and decide the twin question at line 322-324: the
JSON's `[[gov_only_pin]]` says the file does not travel, while this diff put a `{prefix}/gate-legs.toml`
lf_pin in `tools/run-gates/kit.toml`, which says it does. Two stories, one file — pick one.

**Left-shift.** None needed: the gate that catches this class already exists and already fires. The
gap is that it was not run before the commit landed. If anything is owed it is a pre-commit fast leg
carrying `govkit selfcheck`, which is seconds and would have refused the commit that introduced the
file.

### 2 — the generated codebase map was not regenerated with its claim

**`memory/map/generated/symbols.json:247`**

Reproduced at HEAD: `python tools/codebase-map/test_codebase_map.py` exits 1 with
`FAIL test_generated_artifacts_are_fresh` / `STALE symbols.json`. Green at base. Regenerating
produces exactly +20 lines — the `arr`, `die`, `s` and `wrap` entries for
`tools/run-gates/upgrade_manifest.py` — and nothing else. The leg is `opt_in = false` with no guard.

This is the charter's own DoD item, verbatim: claim edits regen the generated artifacts in the same
commit.

**Fix.** `python tools/codebase-map/gen_map.py --write`, committed with `upgrade_manifest.py`.

**Left-shift.** Same shape as #1 — the gate exists and fires. What is missing is proximity: this and
#1 and #3 are all three "a leg that is `opt_in = false`, runs on every bar, and was not run before
the commit". One cheap pre-commit bundle of the three sub-second repository-subject legs closes all
of them at once, and is a smaller change than three separate reminders.

### 3 — four new function names blow the lexicon verb pin

**`tools/run-gates/upgrade_manifest.py:41`**

Reproduced at HEAD: `python tools/lexicon/lexicon.py` exits 1, `P1 verb graded=1011 offenders=467`
against `VERB_OFFENDER_PIN="463"` (`.lexicon.conf:158`). `--list` names exactly the four new defs:
`die` (:36), `s` (:41), `arr` (:47), `wrap` (:51). `.sh` coverage is dark, so only the Python file
counts and the delta is exactly four. The leg's guard `["tools/", …]` matches this diff.

**Fix.** Rename against the declared table — `python tools/lexicon/lexicon.py --suggest <name>` per
identifier — or move the pin with the four names written into its history block, which is that
file's stated convention for every move. Renaming is the cheaper of the two here: four call sites in
one file.

**Left-shift.** As #1 and #2. Note additionally that the four names are exactly the shape the table's
own rationale predicts — `s`, `arr` and `wrap` are string/array/format helpers, i.e. a naming
question the `--suggest` path answers in one call and which nobody asked.

### 4 — the canaries resolve a manifest the runner may not be reading

**`tools/run-gates/run-gates.test.sh:57`** (identical block at `run-gates.gov.test.sh:82`)

Both harnesses default `LEGS_FILE` to `gate-legs.toml` unconditionally and then decode it with
`tomllib`. The runner does not: `run-gates.sh:151` requires the file to exist AND `HAVE_TOMLLIB=yes`,
and otherwise reads `gate-legs.json` and says why.

Reproduced in a scratch adopter tree holding only `tools/gate-legs.json`:
`run-gates.sh --list` prints the leg name correctly, then `run-gates.test.sh` prints
`FileNotFoundError: 'tools/gate-legs.toml'` / `canary: cannot decode tools/gate-legs.toml` and exits
2. The same happens on any CPython below 3.11 holding both files, where `import tomllib` raises.

That is precisely the dual-format floor S3/S4 exist to hold: the bar keeps working and the leg that
proves the bar can move dies. And the population is not hypothetical — `kit.toml`'s
`[gate_runner_seed]` seeds `{prefix}/gate-legs.json`, `run-gates canary` is a shipped `[[gate_leg]]`
with `subject = repo`, and the descriptor migration is unbuilt. Every govkit-installed adopter is in
this state today.

**Fix.** Mirror the runner's resolution instead of its dead first line: prefer the TOML only when the
file exists AND `$PYBIN -c 'import tomllib'` succeeds, else fall back to the JSON. Better, per
S13/AC19: have `run-gates.sh` export the path it resolved and have both harnesses read that export
rather than re-deriving it — one resolution, no second copy to drift.

**Left-shift.** A canary arm that runs the harness against a fixture tree holding only
`gate-legs.json` and asserts exit 0. Stage it before the fix and confirm it reds. That arm also
covers finding #11, which is the reason this one survived: the parity check that should have caught
the divergence grades a line the runner discards.

---

## HIGH

### 5 — the push hook's gate invocation kept the `tools/` prefix

**`.githooks/pre-push:240`**

`GOV_KITROOT` is resolved at :143-147 and used for `kitfp` (:149), predicate 6 (:204) and predicate 7
(:212-213). The line that actually runs the bar is still
`gate=${GOV_GATE_CMD:-bash tools/run-gates/run-gates.sh}`. The hook ships VERBATIM —
`tools/govkit/entries/push-main.kit.toml` declares it `root_relative = true`, `to = "{relpath}"`, no
substitution — and `GOV_GATE_CMD` is testing-only by the hook's own header and by every use of it.

So the adopter this change was written for — the one installed at `scripts/`, named in the comment at
:138 — now resolves every staleness predicate correctly and then runs a path that does not exist:
exit 127, `gate RED`, every default-branch push blocked having run zero legs. `tools/install-prefix-carried.txt`
records `.githooks/pre-push 2` as carried debt, which tracks the spelling without fixing it.

**Fix.** `gate=${GOV_GATE_CMD:-bash $GOV_KITROOT/run-gates/run-gates.sh}` — the variable is already
in scope — and drop the `tools/` spelling from the header comment at line 3 the same way.

**Left-shift.** Extend `.githooks/pre-push.test.sh` with a fixture that installs the kit under
`scripts/` and asserts the hook reaches a green bar. That arm is the general form: every
prefix-carried path in `install-prefix-carried.txt` is a candidate for it, and it is the only check
that would have distinguished "made three siblings prefix-aware" from "made the hook prefix-aware".

### 6 — the tool probe runs before the shard filter

**`tools/run-gates/run-gates.sh:1244`**

Reproduced in a two-leg scratch repo: with `beta` declaring an absent binary,
`run-gates.sh --leg alpha` printed `GATE ok alpha`, then
`GATE FAIL beta (declares tool …, which is not executable here)`, then `gates RED — 1/2 legs
failed`, exit 1. The usage text promises `--leg <name>   run exactly this leg`, and the shard pass's
own contract two lines below says "Everything not named is dropped".

The in-code rationale — an operator sharding ONTO a toolless leg deserves the real answer — is sound
and covers the NAMED leg only. The denominator confirms the second half: `n=2`, `shardouts=0`, so
`ran` (:1798) counts a leg that never executed.

This is now load-bearing rather than latent. `tools/unattended/run-unattended-gates.sh:185` dispatches
its three checks through `--leg … || st=1`, so one adopter leg declaring a tool absent on that host
turns the unattended check run red for a leg none of the three touch — and
`run-unattended-gates.sh` renders that as a bare `unattended gates RED` naming nothing.

**Fix.** Move the probe below the shard filter and below the empty-name sentinel, keeping it above the
guard and opt-in passes. A named leg still gets the FAIL; an excluded leg is `shardout` and is never
probed.

**Left-shift.** A canary arm: two legs, one declaring an absent tool, `--leg` naming the other,
assert exit 0. Then the mirror — `--leg` naming the toolless one, assert exit 1 with the FAIL text —
so the fix cannot be over-applied into silence.

### 7 — the `[[profile]]` rows are a dead declaration

**`tools/gate-legs.toml:92`**

`PROFILES="${GATE_PROFILES:-$KITREL/gate-profiles.txt}"` at `run-gates.sh:339` is unconditional and
the selection loop at :424-468 parses that file; nothing branches on `LEGS_FMT`. The only
`[[profile]]` reference in the runner is the presence refusal at :1063-1064. `min_cores` and
`min_ram_mb` appear nowhere else in the tree except `upgrade_manifest.py:131`, which WRITES them.

Verified live: with the TOML declaring `name = "capable"`,
`GATE_PROFILE=capable GATE_PROFILES=definitely/absent.txt … --manifest` prints
`GATE_PROFILE='capable' is set but no profile table exists … the request is IGNORED` and falls to the
built-in formula — the runner confirming it looked only at `gate-profiles.txt`.

Three consequences, in ascending order of damage. Editing a width in the file this build presents as
the single declaration changes nothing and reds nothing. `gate-legs.toml`'s header claim that it
"replaces both" is false, and `upgrade_manifest.py:100` refuses conversion with a message about a
reader that does not exist. And an adopter who believes the header and deletes `gate-profiles.txt`
after converting drops silently to `PROF_NAME=built-in`, width `min(cores,8)` — the 16-core thrash
the declared table exists to prevent. Spec 6 S7 deletes exactly that file and lists four follow-on
edits, none of which is "teach the runner to read `[[profile]]`".

**Fix.** Either read the rows when `LEGS_FMT=toml`, falling back to `gate-profiles.txt` otherwise, or
delete the rows, the `doc.get("profile")` refusal and the converter's profile `die()`, and say in the
header that the profile table still lives in `gate-profiles.txt`. Half of either is what shipped.

**Left-shift.** If the rows are implemented: a canary arm that plants a distinctive `width` in the
TOML only and asserts the runner announces that row. If they are deleted: the existing "declared but
unread key" question generalises — a leg that loads `gate-legs.toml`, collects its top-level keys, and
asserts each is named somewhere in `run-gates.sh` would have caught this, #18 and half of #12 in one
predicate. That is the cheapest single gate this report can suggest.

### 8 — nothing asserts the two declarations agree

**`tools/run-gates/run-gates.sh:151`**

Spec 2 S3 declares the dual format permanent, not transitional. `gate-legs.json` therefore remains
live forever: it is what `run-gates.sh:154` reads on any pre-3.11 interpreter, and it is what
`tools/check-testsuite-counts.sh:27`, `tools/codebase-map/map_extractors.py:72-93`,
`tools/drift-audit/drift_signals.py:122` and its template twin, and `tools/govkit/govkit.py`
(:1098/:1235/:1325/:1402) all still read.

No arm anywhere compares the two files. So a leg added to, removed from, or re-guarded in
`gate-legs.toml` alone leaves every one of those readers reporting a clean result over the stale
file, and a leg can stop being checked on any pre-3.11 target with nothing reddening anywhere. The
build's own evidence for parity is a one-time hand comparison of the wire rows. A one-time manual
comparison is not a gate; it is a fact about a moment.

The two files agree today — 86 legs, identical name sets. That is exactly the state in which a silent
divergence begins.

**Fix.** Add a merge-bar leg that loads both declarations through the runner's own loader and diffs
the emitted wire rows outside `subject`, guarded on both files. It is the comparison already performed
by hand, made repeatable.

**Left-shift.** That leg IS the left-shift. Stage a divergence — add one leg to the TOML only — and
confirm it reds before landing it, per the charter's rule that a gate whose failing case has not been
observed is an assertion about nothing.

### 9 — the unattended delegation walks past the `$ONLY` filter

**`tools/unattended/run-unattended-gates.sh:181`**

`run_one`'s first line is `case "$ONLY" in ''|"$kind") ;; *) return 0 ;; esac`. The new delegated
block is guarded only by `[ -x "$_RG" ] || [ -f "$_RG" ]`. `ONLY` defaults to `selftests` (:54), so
the default invocation — the DoD command this file's own header prescribes — now also runs the three
bar checks it was explicitly filtered out of, and reports `8 ran` for a five-suite request.

The `ran=$((ran + 3))` at :189 is equally unconditional, which is the worse half: `ran` is now at
least 3 on every invocation, so the liveness assertion at :209 can never fire again. Its comment says
the class it guards is one "this kit has spent six review rounds on". The fallback else-branch routes
the same three through `run_one` and therefore filters correctly, so the two branches disagree
exactly where `run-gates` is installed.

One correction to the finder's rationale, kept because it narrows the claim: an unknown filter is
already refused up front at :93 with exit 2, confirmed by running it. The specific scenario that
comment names was covered elsewhere. The dead assertion and the ignored filter are real regardless.

**Fix.** Wrap the block in `case "$ONLY" in ''|checks) … esac` and move the `ran` increment inside it.

**Left-shift.** An arm asserting `--selftests` runs five suites and `--checks` runs three, by count,
and an arm asserting `ran -eq 0` still reachable — i.e. that the liveness check can still fail. The
second matters more than the first: a liveness assertion nobody has watched fail is the same defect
one level up.

### 10 — the `notool` failure never reaches the durable record

**`tools/run-gates/run-gates.sh:1561`**

Reproduced: a two-leg scratch manifest with one absent tool printed `GATE FAIL  beta …` on stdout,
while `<git-dir>/gate-last-failure.txt` held only the profile line, the queue line, the chunk row and
`gates RED — 1/2 legs failed`. Zero `GATE FAIL` rows.

`AGENTS.md` tells operators never to read the terminal tail and to read that durable file instead. The
one record designed to survive says a leg failed and refuses to name it. Every other failing branch
— `(no result)`, the generic `else` — appends to `FAILED_LEGS`. This new verb is the half of the
amendment left standing.

**Fix.** In the `notool` branch add the `FAILED_LEGS` append mirroring the generic-failure branch at
~:1605, and `c_ran=$((c_ran+1))` — the chunk roll-up currently reports `1 ran, 1 failed` for a run
whose failing leg was never counted as run.

**Left-shift.** An evidence-suite arm that asserts, for EVERY failure verb the runner can emit, that
the verb's name appears in `gate-last-failure.txt`. Enumerate the verbs from the source rather than
listing them, so verb seven cannot arrive uncovered the way verb six did.

### 11 — G2's source-parity arm grades a line the runner discards

**`tools/run-gates/run-gates.gov.test.sh:151`**

`read_derivation()` greps `^LEGS_FILE=`, which in `run-gates.sh` matches only line 143. Every branch of
the if/elif/else at :148-155 reassigns `LEGS_FILE` before any read, so :143 is a dead store whose only
consumer is this parity check.

Proven by staging the break: the live branch at :152 was edited to resolve `gate-legs.json` while
keeping `LEGS_FMT=toml` — a runner that would try to parse JSON as TOML — and the gov canary returned
PASS, 16 assertions, exit 0. Edit reverted, tree clean.

So G2 certifies that three files agree on a line the runner ignores, which is verbatim the divergence
its own message describes: "it would grade a different file than the bar runs". And the divergence is
live today, not theoretical — it is finding #4. A guard that reads a variable the code under it
discards is not a guard.

**Fix.** Either widen `read_derivation` to capture the whole resolution block, or delete :143 and have
the harnesses read the runner's exported resolved path (the S13/AC19 route, which also fixes #4 with
one mechanism instead of two).

**Left-shift.** The staging above is the gate: land the fix only after editing :154 to name another
file and watching G2 red. This report's single most transferable observation is that the arm was
written, reviewed and landed without anyone ever seeing it fail.

### 12 — `cwd` is emitted, whitelisted, and honoured nowhere

**`tools/run-gates/upgrade_manifest.py:183`**

Stronger than first reported: this is a spec item, not a converter artifact. Spec 2 S6 requires a
per-leg `cwd` resolved against the repo root; AC8 requires exit 2 on a `cwd` escaping the root and a
`pwd` leg asserting the in-root case. None of it exists.

The TOML loader whitelists `cwd` at `run-gates.sh:1069` and never emits it — the wire rows at
:1144-1171 carry ten fields and none is `cwd` — and `runleg()` (:1467-1497) execs `"${argv[@]}"` with
no `cd` and no escape check. The converter faithfully emits `cwd = …` into a key nothing honours,
with none of the inert-note `full_only` gets at `gate-legs.toml:140-142`.

An adopter leg converted with `cwd = "frontend"` runs from the repo root. Usually that is a loud
failure. For a root-runnable command — a test runner, a linter — it silently grades a different
subject and passes, which is the one outcome a merge bar must never produce.

**Fix.** Implement it (`(cd "$cwd" && exec …)` in `runleg`, `cwd` as a trailing wire field, the AC8
escape refusal) or refuse it in the converter the way `scope` is refused, report it as DROPPED with
its reason, and remove it from the loader's known-key set so a declaration carrying it reds.

**Left-shift.** The generalised key-liveness leg proposed under #7 covers this: assert every key the
loader accepts is consumed somewhere. Plus AC8's own `pwd` leg once the feature exists.

---

## MEDIUM

### 13 — predicate 7 and the runner disagree about which declaration is live

**`.githooks/pre-push:213`**

The hook sets `_decl` to the TOML on file existence alone. `run-gates.sh:148-155` prefers it only when
`HAVE_TOMLLIB=yes`, and :1839 stamps `manifest_blob` from `$LEGS_FILE`. On a pre-3.11 host holding both
files — the configuration the dual-format loader exists for, which the runner announces on stderr at
:157 — the stamp hashes the JSON and the predicate hashes the TOML. They can never agree, so `force`
fires on every push forever with `the leg manifest differs from the one the recorded green was earned
on`. Safe in direction, permanent in effect, and reading as caution rather than as the defect it is —
the exact failure predicate 4's own comment (:180-183) was written to reject.

The population is real: `adopt-run-gates.sh:27` states `--upgrade` never deletes the legacy manifest,
so every upgraded target keeps both files, and gov ships both. The mirror risk is smaller but present:
on a 3.11+ host an uncommitted `gate-legs.json` edit is now invisible to predicate 7, leaving
predicate 6's committed-diff check as the only watcher.

**Fix.** Probe the interpreter the way the runner does before choosing `_decl`, or stamp the resolved
manifest PATH beside `manifest_blob` and hash the file the record names. The second is better: one
resolution, recorded, read back.

**Left-shift.** `.githooks/pre-push.test.sh` writes only `tools/gate-legs.json` (:132, :184), so both
new TOML arms pass by the file being absent from the fixture — they cannot currently fail. Plant a
`gate-legs.toml` in the fixture and assert predicates 6 and 7 both fire on it.

### 14 — predicate 8 never learned the new spelling

**`.githooks/pre-push:226`**

The runner resolves the hold as `${GATE_OPTIN:-${GATE_SELFTESTS:-}}` (:1281) and stamps `selftests`
from the same expression (:1844). Grep over `.githooks/pre-push` finds one occurrence of either name,
and it is `GATE_SELFTESTS`. So `GATE_OPTIN=1 git push` leaves predicate 8 unfired, `force` stays
empty, `GATE_BASE=$rec_sha` is exported, and the 46 opt-in legs the operator asked for are guard-scoped
away against a base that has not moved — a green earned with them HELD accepted for a push that meant
to run them. That is the weaker-record-for-a-stronger-push direction the predicate's own comment says
is the only one that bites. Spec 2 AC11 requires both spellings; only the runner half of the rename
landed.

The comment at `run-gates.sh:1278` asserts both spellings reach the record identically "because
.githooks/pre-push gates a predicate on that byte". It does not.

**Fix.** `[ -n "${GATE_OPTIN:-${GATE_SELFTESTS:-}}" ]`, matching the runner byte for byte.

**Left-shift.** `.githooks/pre-push.test.sh:123/138` exercise only the old spelling. Duplicate those
two arms for `GATE_OPTIN` — and, since this class has now recurred, add a source-level check that any
env name the runner reads for the hold appears in the hook.

### 15 — `--manifest` renders `notool` as `held`

**`tools/run-gates/run-gates.sh:1322`**

The probe writes `notool` at :1245; the `--manifest` case handles `ondemand`, `skip` and `shardout`
and falls through `*) _disp=held`. `_would` (:1303) excludes any leg carrying an `.rc` file, so the
would-run count is wrong too. `report_one` (:1557) does the opposite and correctly prints
`GATE FAIL … declares tool X, which is not executable here`, with a comment saying a bar reporting that
as anything but red is broken. Two views of one leg, opposite verdicts, and the manifest view picks
the quietest possible label for the one disposition the probe exists to make loud.

**Fix.** `notool) _disp=missing-tool ;;`, and keep `*)` as a loud unknown rather than an alias for
`held`.

**Left-shift.** A canary arm asserting that for every disposition the runner can write, `--manifest`
prints a distinct token — enumerated from the source, not listed.

### 16 — `--manifest` is not read-only

**`tools/run-gates/run-gates.sh:995`**

Reproduced: after `run-gates.sh --manifest`, `.git/gate-run/current` named a freshly created, empty
directory — no header, no verdict. The run-record block has no `[ "$QUERY" = no ]` guard, unlike the
turnstile (:616) and the queue-state block (:922); `--manifest` then exits at :1336, before the header
write (:1393) and before the retention sweep (:1855).

So the structural claim at :70-72 — "a QUERY VERB is read-only and says so structurally … writes only
its payload to stdout" — is false; a concurrent reader resolving `current` mid-run sees the runner's
own documented crash signature with nothing crashed (`run-gates.evidence.test.sh:218-230` asserts that
exact path); and the empty dirs accumulate past `GATE_RUN_KEEP` because the sweep never runs here.

**Fix.** Guard the run-record block with `[ "$QUERY" = no ]`. Every later `[ -n "$RUNDIR" ]` already
tolerates an empty `RUNDIR`.

**Left-shift.** An evidence-suite arm: run each query verb, assert `.git/gate-run` gained no entry.
It is one `find | wc -l` before and after and it covers all three verbs at once.

### 17 — the enforcement column of `--manifest` cannot say `enforced`

**`tools/run-gates/run-gates.sh:1334`**

Reproduced: `GATE_CEILINGS=1 … --manifest` printed the header `… ceilings live from env` and then
`declared-only` on every LEG row. `prof_c` is assigned at :585-590 as `live from <src>` /
`OFF from <src>` / `INERT (no runnable timeout)` — never the bare word `live` — and is always set
before the manifest block, so `[ "${prof_c:-live}" = live ]` is a dead arm.

One command's header and its own per-leg column contradict each other on the fact an operator uses to
decide whether a ceiling is safe to turn on. Given #19, that decision surface is the only coverage
`[bar].enforce_ceilings` has.

**Fix.** Test the state variable: `[ "$CEILINGS_LIVE" = 1 ] && echo enforced || echo declared-only`.

**Left-shift.** An arm asserting `GATE_CEILINGS=1 --manifest` prints `enforced` on at least one row,
and the unset run prints none. A column with one reachable value is the "arm that cannot fail" class
in report form rather than in test form.

### 18 — two `[bar]` keys are parsed, validated, and discarded

**`tools/run-gates/run-gates.sh:201`**

`BAR_TTL` occurs twice in the file — the initialiser at :176 and the read at :201 — and is consumed
nowhere. `TS_TTL` is still `PROF_TIMEOUT*3` or `${GATE_TURNSTILE_TTL:-1800}` (:630-631), and
`TS_MAXWAIT` inherits the disconnection at :636. In TOML mode `PROF_TIMEOUT` is unreachable-nonzero,
since it is only set from a profile row's `timeout=` knob and the TOML carries none by design.

`gate-legs.toml:30-34` says the opposite in as many words: the key exists so "the value survives as a
key rather than disappearing with the knob". It did not survive. A malformed value still exits 3, so
the key refuses input it cannot act on — a declared knob with a validator and no consumer. It is
invisible only because the shipped 1800 equals the hardcoded fallback, and `run-gates.sh:628` still
prescribes setting a knob the TOML no longer has. `BAR_DEFAULT_CEILING` is dead in the shell the same
way (the Python loader reads `default_ceiling` itself at :1066), which is why nothing noticed.

**Fix.** Seed the fallback from the declaration — `GATE_TURNSTILE_TTL` still outranking — or delete
the key, its validator and the paragraph that promises it. Delete `BAR_DEFAULT_CEILING` or route the
loader's `dflt` through it.

**Left-shift.** The key-liveness leg from #7, which is now earning its third finding.

### 19 — `[bar]` has no test coverage, and both "shipped default" arms prove it

**`tools/run-gates/run-gates.test.sh:300`**

The `1e-shipped` arm drives `GATE_LEGS="$_cd/bounded.json"`, so `LEGS_FMT=json` and `CEIL_WANT` takes
the hardcoded `else CEIL_WANT=0` at :217 — not `BAR_CEILINGS`. Its own failure text says
"[bar].enforce_ceilings=false is not reaching the runner", a claim it cannot make. The turnstile suite
has the identical shape: its header (:23) says the shipped-default arm "reads the declaration
instead", while that arm (~:694) calls `legs "$RD" '[…]'`, and `legs()` (:91) writes
`tools/gate-legs.json` into a scratch repo whose `mk_repo` copies no TOML.

Grepping both suites for `enforce_ceilings`, `turnstile_ttl`, `default_ceiling` or `[bar]` returns
only that one message string. The block at :176-201 warns in its own comment that a TOML `false`
passed through verbatim would ship the mechanism ENABLED — and no arm would notice.

**Fix.** Give each arm a scratch repo carrying a `gate-legs.toml` with the `[bar]` key it names, and
add the negative control that flips it to `true` and asserts the mechanism turns on.

**Left-shift.** The negative control IS the left-shift; without it the fix reproduces the defect with
better prose. Both knobs default OFF, so an arm that only ever asserts "off" is satisfied by the
mechanism being absent entirely.

### 20 — the gov canary's guard cannot see the file it grades

**`tools/gate-legs.toml:785`**

`guard = ["tools/run-gates/", "tools/gate-legs.json"]`, and `changed()` (:312) is
`git diff --quiet $BASE -- <pathspecs>`, so the literal `tools/gate-legs.json` cannot match
`tools/gate-legs.toml`. A declaration-only edit therefore guard-skips the suite that grades that
declaration — the suite holding the untracked-guard-path arm, the double-space arm and the
unguarded-ledger-leg arm. The sibling `run-gates canary` escapes only because its guard list happens
to start with `tools/`.

Scoped honestly: both are `opt_in = true`, so this bites on a `GATE_OPTIN` run — which is the DoD run
for kit work, i.e. exactly when a declaration is being edited.

**Fix.** Add `"tools/gate-legs.toml"` to that guard array — the same amendment `.githooks/pre-push`
already took at :204.

**Left-shift.** A canary arm asserting that every path the runner can resolve as a manifest appears in
the guard of every leg whose subject is the manifest. Cheaper alternative if that reads as too clever:
the run-gates canary already refuses a guard naming an untracked path; extend it to refuse a guard
that names one member of a known pair without the other.

### 21 — three declared budgets now bound nothing

**`tools/unattended/run-unattended-gates.sh:45`**

The budget verdict lives entirely inside `run_one` (:158-168), including the "A MISSING BUDGET IS
ITSELF A FAILURE" arm. The delegated path never calls it, so `BUDGET_kit_gate`,
`BUDGET_playbook_validity_gate` and `BUDGET_skill_wiring` are declared and enforced by nothing, while
`--help`'s sed-derived sum (:76-84) still reads them out of the file's own text and quotes them as
part of the declared budget. Three suites can go from 28 s to 500 s with no `OVER BUDGET` line.

The file's own rule is that a suite arriving without a budget would be "exempt from the rule by the
act of arriving". These three are exempt by the act of being delegated. The manifest's ceilings are no
backstop: `gate-legs.toml:21` ships `enforce_ceilings = false`, and the ceiling declared for
`unattended kit gate` is 16040 s against the 120 s declared here.

Distinct from #9 — that is the filter, this is the enforcement — and it needs its own fix.

**Fix.** Time the delegated invocation and grade it against the sum of the three, or pass
`GATE_CEILINGS=1` on that call and say so, or delete the three declarations and name the manifest as
their new owner. Any of the three; none of them is what shipped.

**Left-shift.** An arm asserting the `--help` budget sum equals the sum of the budgets actually
enforced by a run. A declared ceiling with no enforcer should red the same way a missing one does —
that is the file's own rule applied to itself.

### 22 — a failed scan reports as a clean one

**`tools/run-gates/upgrade_manifest.py:230`**

`subprocess.run([… ls-files -z], capture_output=True, timeout=60)` with no `check=True`, and the
surrounding `try` catches only the launch failure. A non-zero git exit — TARGET not a repo, an index
lock — yields empty stdout, no exception, `tracked = ['']`, no hits, and line 267 prints `NO tracked
file outside the manifest names 'gate-legs.json' — nothing to repoint`. The git-absent path funnels to
`tracked = []` and the same line.

The comment directly above it asserts "An empty report and a report nobody generated must be
distinguishable". They are not. An adopter converting their manifest is told no live reader needs
repointing, while every tool still reading the old JSON keeps reading it.

**Fix.** Capture the returncode and emit `SCAN DID NOT RUN — git ls-files exited N in <target>;
repoint check NOT performed`, suppressing the reassuring line on that path. Same in the `except`
branch instead of falling through to `tracked = []`.

**Left-shift.** An arm running `--upgrade` against a non-repo directory and asserting the output
contains the DID NOT RUN token. This is the charter's liveness rule in miniature: a probe that cannot
move must say so.

### 23 — `chunk_close` was never amended for the sixth verb

**`tools/run-gates/run-gates.sh:1657`**

Reproduced: three legs across chunks `one` and `two`, `--leg aa` printed
`---- chunk two: green  (0 ran, 0 failed, 0 skipped, 0 reused, 0 held)`. `report_one`'s `shardout` arm
(:1563-1572) increments only the run-wide `shardouts` and none of the `c_*` tallies, so the predicate
sees an all-zero chunk and falls through to `verdict="green"`.

The comment two lines above records the same amendment being made once already, for the `held` verb
(TOOL-dUnstalledConvoy-32), for precisely this reason, and states the rule the code no longer
implements for verb six. Held at medium rather than high because the run-wide verdict is still correct
— only the chunk row lies — but this is the same "half of an amendment" shape as #10 and #14, in the
one place that already knew about it.

**Fix.** Add a `c_shardout` tally, include it in the skipped predicate, and emit it in the chunk line
and `CHUNK_ROLLUP` beside the other four.

**Left-shift.** A canary arm asserting that every verb `report_one` can write increments some `c_*`
tally, derived from the source rather than listed. That is the general form of an amendment whose
halves keep separating.

---

## LOW

### 24 — the `selftests` stamp lost its normalization

**`tools/run-gates/run-gates.sh:1844`**

`bc39566e` wrote `"${GATE_SELFTESTS:+1}"`, which mapped every non-empty value to `1`. `476a4166`
replaced it with `"${GATE_OPTIN:-${GATE_SELFTESTS:-}}"`, writing the raw value, while its only reader
(`.githooks/pre-push:226`) tests `[ "$rec_st" != "1" ]`. The runner's hold predicate is an emptiness
test, so `GATE_OPTIN=yes`, `true` and even `0` all genuinely run the opt-in legs and all three stamp a
byte the reader classifies as HELD. It fails safe — a needless full bar against a 26-minute floor —
but the field no longer means what its reader tests, and an operator value carrying a tab lands
unescaped in a TSV the hook parses with `awk -F'\t'`. That last part is a regression against this
file's own "marshal every value to the byte 0 or 1" discipline at :168.

**Fix.** `printf 'selftests\t%s\n' "$([ -n "${GATE_OPTIN:-${GATE_SELFTESTS:-}}" ] && echo 1)"`.

**Left-shift.** An arm running with `GATE_OPTIN=yes` and asserting the stamped byte is `1`. Cheap, and
it is the same arm #14 needs.

### 25 — `--leg` silently swallows the query verbs

**`tools/run-gates/run-gates.sh:69`**

`MODE=shard` is assigned unconditionally after the parse loop, so `--list --leg X` and
`--manifest --leg X` discard the query verb. Reproduced: `--list --leg alpha` printed the ceilings
banner, the profile line and the queue line, then RAN the legs and exited 1, where plain `--list`
prints the names and exits 0. The usage text documents both verbs as "print … and exit" and documents
no precedence, so an operator who meant to inspect gets a bar that starts running.

**Fix.** Refuse the combination in the parse loop rather than resolving it silently.

**Left-shift.** An arm asserting `--list --leg X` exits 2 and runs nothing. Argument-surface
precedence is exactly the kind of thing that is decided once, in the parser, and then never
re-derived.

### 26 — the converter is stricter than the runner it converts for

**`tools/run-gates/upgrade_manifest.py:90`**

`raw.startswith("#")` without an `lstrip`, so an indented comment is neither skipped nor blank, splits
to one field and dies with "carries a malformed row". `run-gates.sh:438` strips leading blanks before
the same test, carrying a comment recording that not doing so once "refused the whole bar with a
message about field counts" and that two readers disagreeing about which lines are even rows "is the
drift this joins shut". The converter is the second reader and takes the losing side. Two secondary
defects in the same function: `int(knobs.get("width", 1))` (:132) emits `width = 1` for a row the
runner refuses with "declares no width knob", and `int(c)`/`int(r)` raise an uncaught `ValueError`
instead of routing through `die()`.

gov's own `gate-profiles.txt` has no indented comment, so this bites an adopter rather than this tree.

**Fix.** `raw.lstrip().startswith("#")`; `die()` on an absent `width` rather than defaulting it; wrap
the `int()` conversions.

**Left-shift.** One fixture `gate-profiles.txt` carrying an indented comment, a row with no `width`
and a non-numeric threshold, asserted to produce the same accept/refuse verdict from both readers.
Same principle as #8: two readers of one file need a check that they agree, not two careful authors.

---

## What did NOT turn up

Stated because a review that only lists findings hides its own coverage. No security finding: the
diff opens no write path, no egress, no auth surface. The dual-format loader's byte-identical wire
rows outside `subject` reproduce as claimed — the defect there is that nothing keeps it true, not
that it is false. The turnstile-off and ceilings-off defaults are correctly plumbed at the runner;
their defect is that no arm grades the declared path (#19) and one declared knob is inert (#18),
not that the defaults are wrong. `upgrade_manifest.py`'s refusal set is otherwise sound: `scope` is
refused loudly, `full_only` is documented inert. And the `--leg` name refusal, the `--list` output and
the `--help` text all behave as documented in the cases not named above.

## The pattern worth carrying forward

Sixteen of the twenty-six defects are one of two shapes, and both were in the HUNT.

**Half an amendment.** A verb, a spelling or a prefix was added in one place and not in its siblings:
`notool` reaches stdout but not `FAILED_LEGS` (#10) and not `--manifest` (#15) and not `chunk_close`
(#23); `GATE_OPTIN` reaches the runner but not the hook (#14); `GOV_KITROOT` reaches three predicates
but not the gate invocation (#5); `gate-legs.toml` reaches the loader but not the registry (#1), not
the guard (#20) and not the parity claim (#8). The repair that generalises is not care — it is
deriving the sibling set from the source in a check, so verb seven and spelling three cannot arrive
uncovered.

**A criterion that cannot fail.** G2's parity arm grades a dead assignment and was proven green over a
staged break (#11). The `1e-shipped` and turnstile shipped-default arms grade a format that cannot
carry the key they name (#19). `--manifest`'s enforcement column has one reachable value (#17). The
repoint scan reports clean when it did not run (#22). Each was written in good faith and each
certifies nothing. The charter already has the rule: a gate is not landed until its failing case has
been observed. Four arms in this diff were landed without that, and the fix for each is to stage the
break before landing the repair.
