**Serves:** diff-review TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-15

# aScouredKit — closing Tier-2 review, ROUND 2

*Adversarial review of the FOLD, not of the build. Node `a`, 2026-08-30. The base is round 1's
recorded tip, so the diff under review is the four fixes round 1 bought and nothing else. Every
finding below was re-derived — and where the report says "reproduced", executed — against the tree
in this worktree before it was written down. The severities in the table are this report's
adjudication, not the finders' self-grading.*

**ROUND:** 2.

**Range:** `926da8482b5b1b8ba8e0d0f5f1bfc4b1a7f5f3d0...HEAD` (1 commit, `13e2cfc2`, 25 files, 5 of
them product).

## Verdict: BLOCKED

Two blockers, both fold-INTRODUCED rather than fold-missed, and both are the same shape: a token was
added to one carrier of a pair and not the other, so the two channels that must agree now render
different answers. The kickoff-manifest one is the sharper of the two, because it inverted its own
goal — the fix written to remove a standing red-after-install exemption created a permanent
unconditional one. Neither is more than a two-line change.

The fold's stated deliverable was four fixes. **One is correct and complete** (the drift-audit
argument parser, executed across ten invocation shapes). **One is correct on the path it was written
for and leaves the identical defect standing on its sibling branch** (the withheld-legs ownership
set). **Two moved their defect one caller over** (the `kits` shape guard, the `{manifest_path}`
token). That ratio is the finding behind the findings: every fix in this fold was scoped to the
instance the round-1 report named, and §7's "gate the CLASS, not the instance" was not applied to
any of them.

**Review shape:** raw 23 · confirmed 20 · refuted 3 · unverified 0 · precision 0.87. The 20 confirmed
raws consolidate to the 8 distinct defects below (four raws named the drift-audit leg, four named the
`n_kit` comment, four named the `kits` container, two each named the unguarded `kits` branch and the
`check-install-prefix` loops). Consolidation is not refutation — the duplicates agreed on file, line
and mechanism.

**Banked, not findings.** `TOOL-aScouredKit-27` (`chunk` does not travel to adopters), `-28` (a quoted
conf value with a trailing comment diverges from bash in both python parsers) and `-29` (a substring
predicate in govkit's selftest) were deliberately not fixed in this fold and carry their
measurements as backlog rows. The ~215 open rows in `memory/backlog/TOOL.md` are tracked. None are
re-reported here.

---

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| 1 | **BLOCKER** | `tools/govkit/govkit.py:3123` | `exempt_leg` cannot resolve the `{manifest_path}` the fold just added, so the kickoff-manifest leg is now unconditionally exempt at every target |
| 2 | **BLOCKER** | `tools/drift-audit/kit.toml:90` | the `{prefix}/review-harness` positional reached `[adopt]` and `[check]` but not the gate leg, so an adopter's bar and their rendered Skill disagree permanently |
| 3 | HIGH | `tools/govkit/govkit.py:433` | the new `kits` shape guard is in the `declared` branch only; `adopt` routes the same target-authored list through the unguarded `mode == "kits"` branch |
| 4 | MEDIUM | `tools/govkit/govkit.py:446` | the guard grades the ELEMENTS; the `list()` one line above it is what raises on a non-list container, and explodes a bare string into characters |
| 5 | MEDIUM | `tools/govkit/govkit.py:4501` | the ownership-blanking the fold removed from the withheld path still stands on the `kind != "manifest"` branch |
| 6 | MEDIUM | `tools/govkit/govkit.py:4487` | the carry-forward falsified the comment at `:4485` and un-suppressed the self-test advisory, which now fires after a run that wrote nothing |
| 7 | LOW | `tools/check-install-prefix.sh:100` | the `-0` hardening is on the producer only; both `--check` consumers are unquoted `for` loops that word-split the rows it just made readable |
| 8 | LOW | `tools/govkit/selftest.py` | the rewritten withheld-ownership path has no arm, and `legs_withheld` has three writers and zero readers |

---

### 1 — BLOCKER · `exempt_leg` grants the kickoff-manifest leg a standing exemption

**Site:** `tools/govkit/govkit.py:3123-3125`, against
`tools/govkit/entries/kickoff-manifest.kit.toml:58`.

The fold gave the `manifest-section-b` hole's discharge probe the `{manifest_path}` token, so the
probe and the leg would ask one question. `exempt_leg` is the only consumer of that probe, and it
builds its own context as a hardcoded four-key literal:

```python
ctx = {"kit": f"tools/{eid}", "prefix": "tools", "kit_id": eid,
       "memory_root": "memory"}
resolved = [resolve_tokens(a, ctx)[0] for a in cmd]
```

`manifest_path` is a target ANSWER — `needed_answers` at `:6602` scans hole discharge commands
precisely so intake asks for it — and it is not in that dict. `resolve_tokens` returns an unresolved
token verbatim by design (`:563-579`), and the `[0]` discards the missing list, so the probe runs
with a literal brace as its argument.

**Reproduced.** `bash skills/session-kickoff/manifest-check.sh '{manifest_path}'` exits **2**
(`MANIFEST env ERROR — '{manifest_path}' not found`). Non-zero is read as "the hole is genuinely
undischarged, right now", so `exempt_leg` returns `True` — unconditionally, at every target,
including one whose `manifest_path` is gov's own default, where the probe used to run for real.

The consequence is the exact inversion of the fix's intent. `apply`'s after-check at `:4570` is
`elif b is None and a2 == "red" and not exempt_leg(...)`, so the leg named `kickoff-manifest ratchet`
— `red_after_land = true`, in the registry's DEFAULT selection, `guard = []` — can never again
report "did not exist before this install and is red after". The fold's own comment on the changed
line says the un-tokenised probe would "grant the newly-fixed leg a standing red-after-install
exemption". Adding the token without teaching this caller to resolve it created that exemption
rather than preventing it.

The same defect, with the same token, is documented as already-fixed one function over. From
`resolve_dests`' docstring at `:3209-3212`:

> THE `missing` LIST IS RETURNED, not dropped. An earlier cut called `resolve_tokens(...)[0]` and
> discarded it, so `apply --kits kickoff-manifest` with no `manifest_path` answer wrote a file named
> literally `{manifest_path}` and exited 0.

**Fix.** Give `exempt_leg` the real context and fail CLOSED on an unresolved token. It already
receives `target`, and its only caller at `:4570` holds `deploy`:

```python
ctx = target_context(target, deploy, eid, d)
resolved, miss = [], []
for a in cmd:
    s, m = resolve_tokens(a, ctx); resolved.append(s); miss += m
if miss:
    return False          # never grant an exemption over a probe that could not be rendered
```

Note the hardcoded dict also pins `prefix = "tools"` and `memory_root = "memory"`, so the probe is
wrong at any other prefix even for tokens it does resolve — `target_context` fixes that in the same
edit.

**Left-shift.** Ban the pattern, not the instance: a `selfcheck` arm (or a one-line grep leg) that
refuses `resolve_tokens(...)[0]` at any call site whose result becomes an argv, with a per-line
allowlist carrying a reason. That predicate finds this call and would have found the `resolve_dests`
one. Second, cheaper leg: assert that every `[[hole]].discharge.command` token is resolvable under
the same builder `apply` uses, so a descriptor cannot declare a token its own consumer cannot see.

---

### 2 — BLOCKER · the drift-audit wiring leg keeps the old argv

**Site:** `tools/drift-audit/kit.toml:90`, three lines below the comment that justifies the change by
that leg's own behaviour.

`[adopt]` (`:34`) and `[check]` (`:38`) both gained `{prefix}/review-harness`. The
`[[gate_leg]]` named `drift-audit wiring` did not:

```toml
# TOOL-aScouredKit-15. THE SIBLING'S HOME IS PASSED, because this kit cannot derive it and an
# environment variable is not durable — the leg re-invokes the script with a fresh environment on
# every bar, so an env-only answer is lost between the render and the check that grades it.
[[gate_leg]]
name = "drift-audit wiring"
subject = "repo"
argv = ["bash", "{kit}/adopt-drift-audit.sh", "--check"]
guard = []
```

The sibling entry's id really is `review-harness` (`tools/workflows/kit.toml:3`, `registry.toml:102`)
with an `include = "**"` engine rule and no per-file `to`, and govkit lands an entry at
`{prefix}/{eid}` (`govkit.py:810-811`), so a deployed target holds the harnesses at
`{prefix}/review-harness/drift-audit-{code,state}.js`. `apply` runs `[adopt]` WITH the positional and
writes `.claude/skills/drift-audit/SKILL.md` naming that path. The emitted leg runs WITHOUT it, falls
through the unset `DRIFT_WORKFLOWS_REL` (`adopt-drift-audit.sh:140`) to the
`${KIT_REL%/*}/workflows` derivation (`:133`), renders a different string, and reds.

**Reproduced on gov's own tree**, where the polarity is inverted because gov's sibling genuinely is
`tools/workflows`:

```
$ bash tools/drift-audit/adopt-drift-audit.sh --check                        # the LEG's argv
drift-audit: in sync (... deep-tier harnesses present at tools/workflows/)   # exit 0

$ bash tools/drift-audit/adopt-drift-audit.sh --check tools/review-harness   # the [check] argv
drift-audit: ... is out of sync with SKILL.template.md + .memory-tree.conf
  re-render with: tools/drift-audit/adopt-drift-audit.sh
73,74c73,74
< tools/workflows/drift-audit-code.js     ...
---
> tools/review-harness/drift-audit-code.js     ...
```

At an adopter the two swap sides and neither can be green at the same time. Worse, the byte-diff arm
at `:184-187` fires BEFORE the `_wf_missing` filesystem assertion at `:197`, so the operator sees
`out of sync with SKILL.template.md + .memory-tree.conf` — which is not what is wrong — and the
remedy `re-render with: $0`, which is the positional-less form. Following it overwrites the correct
Skill with the dead `tools/workflows` pointer, after which `govkit check` reds the other way. A
destructive remedy on a `subject = "repo"`, `guard = []` leg that runs on every adopter bar.

Invisible here twice over: gov's own `tools/gate-legs.json:678-688` carries the same positional-less
argv and is correct for gov, and `selfcheck`'s descriptor-vs-manifest arm (`govkit.py:1283-1340`)
compares NAME, SUBJECT and CHUNK and never ARGV — the one field that diverged.

**Fix.**

```toml
argv = ["bash", "{kit}/adopt-drift-audit.sh", "--check", "{prefix}/review-harness"]
```

Gov's own manifest row stays bare and `selfcheck` will not object, since 7h does not compare argv.
Say the asymmetry out loud in the leg's comment.

**The fix is necessary but not sufficient, and this is the part to decide before landing it.**
`drift-audit` declares `requires = ["memory-tree"]` and neither it nor `review-harness` is in the
registry's default selection (`registry.toml:36`). An adopter who installs drift-audit alone gets a
Skill pointing at `{prefix}/review-harness/*.js` that is not there, `_wf_missing` fires, and the leg
reds anyway — and `_wf_complain` then tells them to `Set DRIFT_WORKFLOWS_REL`, which is precisely the
channel the fold's own comment says the leg cannot carry. Either add `review-harness` to
drift-audit's `requires`, or resolve the sibling's home from the registry rather than spelling it
(`TOOL-aScouredKit-26` already tracks the missing cross-entry token). Spelling `{prefix}/review-harness`
is also still wrong for a target that sets `kit.review-harness.prefix`.

**Left-shift.** A `selfcheck` arm asserting that an entry's `[check].argv` and any `[[gate_leg]]`
argv invoking the SAME script agree on their arguments, or carry an explicit `why_argv_differs`.
This is the second time in one build that one token was added to one carrier and not its twin (see
finding 1), so the class is measured, not hypothetical. Then extend the `:1283-1340` parity arm to
compare argv between descriptor and `tools/gate-legs.json` with a declared exemption list — gov's own
row legitimately differs here, and an exemption that has to be written is an exemption somebody read.

---

### 3 — HIGH · the `kits` shape guard is missing from the branch `adopt` uses

**Site:** `tools/govkit/govkit.py:433-440` (the `mode == "kits"` branch), reached from
`_cmd_adopt` at `:6307-6308`.

The fold added `badshape` at `:454-460`, inside `if declared:`. `cmd_adopt` passes the target's own
list through the OTHER branch:

```python
selection = resolve_selection(reg, descs, "kits" if deploy.get("kits") else "default",
                              list(deploy.get("kits") or []), ...)
```

**Reproduced against the live registry (25 entries):**

| input | mode `"kits"` (adopt) | mode `"default"` (guarded) |
|---|---|---|
| `[1]` | `TypeError: sequence item 0: expected str instance, int found` | Refusal, names the value |
| `[["a"]]` | `TypeError: cannot use 'list' as a dict key` | Refusal, names the value |

The first raises from inside `", ".join(unknown)` — the Refusal written to reject the bad shape is
itself what crashes. `main` catches only `Refusal` (`:6918`), so both surface as raw tracebacks.
`load_deploy` (`:827`) does no schema validation, and `adopt` is the first verb an operator runs
against a target descriptor, so the unguarded path is the one a malformed `kits` hits first. That is
verbatim the outcome the new comment at `:448-453` claims to have closed.

**Fix.** Hoist ONE guard above the `mode` split — both lists are target-authored and both are
consumed the same way — and delete the copy in the `declared` branch. One guard where both callers
route through, not one guard per branch.

**Left-shift.** A table-driven selftest arm running every malformed shape (`5`, `true`, `"str"`,
`[1]`, `[["a"]]`, `[None]`, `["memory-tree", 2]`) through BOTH modes and asserting `Refusal`, never
`TypeError`. Generalisable leg, since `main` catches only `Refusal`: assert that every `deploy.toml`
key govkit reads has a declared type check before its first use.

---

### 4 — MEDIUM · the guard grades the elements, not the container

**Site:** `tools/govkit/govkit.py:446`, one line above the new guard.

```python
declared = list((deploy or {}).get("kits") or [])
```

An explicit `list()` over whatever the target wrote. **Reproduced:**

- `kits = 5` → `TypeError: 'int' object is not iterable`
- `kits = true` → `TypeError: 'bool' object is not iterable`
- `kits = "memory-tree"` → the string is exploded into 11 single-character strings, every one of
  which passes `isinstance(k, str)`, so `badshape` is empty and control reaches the unknown-entry
  Refusal: `the target's deploy.toml names m, e, m, o, r, y, -, t, r, e, e in \`kits\`, which are not
  a registry entry`.

The first two are tracebacks, not refusals. The third is worse than a traceback because it looks
authoritative: it names eleven keys that do not exist and suggests no fix, and a bare TOML string
where an array was meant is the likeliest authoring slip in the set. The same `list()` sits on the
adopt path at `:6308`. Distinct from finding 3 rather than a duplicate — fixing the branch coverage
does not close this, and fixing this does not close that.

**Fix.** Grade the container before expanding it, in the same hoisted guard:

```python
_raw = (deploy or {}).get("kits")
if _raw is not None and not isinstance(_raw, list):
    raise Refusal(f"`kits` in the target's deploy.toml is a {type(_raw).__name__}, not an array of "
                  f"registry entry ids — a bare string included; wrap it in brackets")
declared = list(_raw or [])
```

**Left-shift.** The same arm as finding 3, with the container shapes in its table.

---

### 5 — MEDIUM · the ownership-blanking still stands on the non-manifest branch

**Site:** `tools/govkit/govkit.py:4501` (the `else:` of the `kind == "manifest"` split), against the
receipt write at `:4581-4582`.

`emitted` is initialised `[]` at `:4299`. Only the manifest branch appends to it (`:4433`) or, since
the fold, restores it (`:4475`). The `else:` — taken whenever `[gate_runner].kind` is `none` or
absent — never assigns it, and the receipt writes `"emitted": emitted` unconditionally. So that
branch persists `[]`.

`owned` derives from exactly that field (`:4341`), and `:4394-4397` raises when a leg name is in the
target's runner but not in `owned`:

> the target's runner already has a leg named 'X' and this target's receipt does not claim it

Sequence: manifest install (gov owns N legs, receipt claims them) → target sets `kind = "none"` or
drops the stanza and re-applies (ownership blanked) → target restores `kind = "manifest"` → every
subsequent `apply` refuses on the first gov-written name still in their runner, permanently, with
`--re-adopt` carrying the blanked receipt forward. That is the identical wedge the fold's own comment
at `:4462-4475` and `_cmd_adopt`'s D2 at `:6554-6562` both describe, one branch over. The fix moved
the defect rather than closing the class.

Reachability needs a deliberate kind downgrade-and-restore, which is narrower than the withheld path
— hence MEDIUM rather than BLOCKER — but it is mechanically real and unrecoverable without
hand-editing the receipt.

**Fix.** Hoist the carry-forward to the declaration at `:4299` and let the manifest write-back be the
only path that overwrites it:

```python
emitted: list[dict] = list(((receipt or {}).get("gate_runner") or {}).get("emitted", []))
```

That makes `emitted` mean "the ownership set" everywhere, which is what the fold's own comment says
it means, and removes both the withheld special case and this branch's silent one.

**Left-shift.** A selftest arm over the transition: manifest install → demote `kind` → re-apply →
restore `kind` → apply must complete rather than raise. Same arm as finding 8, one fixture apart.

---

### 6 — MEDIUM · the carry-forward falsified the comment beside it and un-suppressed the advisory

**Site:** `tools/govkit/govkit.py:4485-4489`.

The comment at `:4482-4486` is the stated justification for the summary block's indentation, and its
last sentence is now false:

> `emitted` is empty on the withheld path, so the `if n_kit:` below is false there and the block is
> correct at this indent for both.

`:4475` reassigns `emitted` to the previous receipt's rows, and those rows carry `subject` (written
at `:4432-4440`). `n_kit` at `:4487` sits at the `if`'s indent with no withheld guard, and
`_legs_withheld` — set at `:4476` — is read only at `:4582`, never as a guard here.

Behaviourally, on any re-apply whose LEGS step raises a problem over a receipt that owns kit-subject
legs, the operator gets, consecutively:

```
govkit apply — gate legs: WITHHELD from ... the N leg(s) this step built are NOT written.
govkit apply — M of those are kit SELF-TESTS and are HELD by default ...
govkit apply —   GATE_SELFTESTS=1 <cmd>          ... Run them once now to verify this install
```

`N` was formatted before the reassignment and `M` after, so the two counts can differ; "those" refers
to rows this run wrote nowhere; and "this install" did not complete. Reachable through either in-loop
`r.fail` — the unresolved-token fail at `:4367` or the receipt-drift fail at `:4419-4423`, both of
which increment `r.problems` before the `:4447` snapshot comparison.

Low blast radius. It is on the table because it is a load-bearing comment contradicted by the same
commit that wrote it, four lines above — the class this build has now booked three times (S6's "ONE
index reader", the withheld branch's own indentation bug, this).

**Fix.** `if not _legs_withheld and n_kit:` at `:4488`, and rewrite `:4482-4486` to describe what the
withheld path now carries. If finding 5's hoist is taken, the guard becomes the only correct form,
since `emitted` will be non-empty on the write path's first run too.

**Left-shift.** Prose cannot be gated, so gate the behaviour: the selftest arm from finding 8 asserts
that a withheld run prints the WITHHELD line and does NOT print the `GATE_SELFTESTS=1` advisory.

---

### 7 — LOW · the `-0` hardening stops one screen short of its own consumers

**Site:** `tools/check-install-prefix.sh:100` and `:115`.

The producer is now space-safe (`:82`):

```sh
hits=$(printf '%s\n' "$files" | tr -d '\r' | grep -v '^$' | tr '\n' '\0' \
  | xargs -0 -r grep -HnE "$RE" -- 2>/dev/null | cut -d: -f1,2 || true)
```

`git ls-files` does not C-quote a plain space, so a tracked path holding one now survives the
producer and is emitted as `dir/a b.md:12`. Both `--check` consumers are unquoted `for` loops:

```sh
for h in $hits; do ...           # :100 — splits into `dir/a` and `b.md:12`
for w in $waived_rows; do ...    # :115 — same shape
```

`${h##*:}` and `${h%:*}` then hand `sed -n` a line number and a filename that do not correspond,
`grep -qxF "$h"` can never match a legitimate waiver, and the stale-waiver arm reds on the same path
from the other side. The waiver producer's own `awk '{print $1}'` (`:86`) truncates such a row at the
space anyway, so both sides of the comparison break on the same input class. The `--list` arm nine
lines above at `:91` already does this correctly with `while IFS= read -r h` — the same data parsed
two ways in one file, one of them wrong.

The finding's own concession stands: `git ls-files | grep -c ' '` is **0** over the shipped globs
today, so this is latent. But the script is a govkit entry and travels to adopters, and the `-0`
change was justified precisely by space-bearing paths.

**Fix.** Both loops become `printf '%s\n' "$hits" | while IFS= read -r h`, matching `:91`. Move the
`bad`/`stale` counters out of the resulting subshell — the comment at `:278` already documents why a
`| while` verdict variable never reaches the exit.

**Also checked, and clean.** `cut -d: -f1,2` on a colon-bearing path: the population is `git ls-files`
output, repo-relative and POSIX, so a Windows drive letter cannot appear — git never emits an
absolute path into this pipeline. Measured: `git ls-files | grep -c ':'` is **0**. The `-H` addition
is what makes the two-field cut correct for a one-file population, which previously produced
`<lineno>:<text>` and had the cut take the line number as the path. Arm 2's awk is correct as
written: `grep -cHE` emits `<path>:<count>`, and `sub(/:[^:]*$/, "", $0)` strips only the LAST
colon-field, so a colon-bearing path survives intact; `NF>=2` is exactly what `-H` now guarantees,
and without it a single-file population produced `NF==1` and every row was dropped — green by
absence, on a ratchet (`:211`). A colon in a repo-relative path would still truncate arm 1's rows, which is the
same latent class as the space and is closed by the same discipline.

**Left-shift.** A fixture repo in the kit's own selftest holding a tracked path with a space and one
with a quote, asserting the gate reds and names them verbatim. Cheaper and broader: a shellcheck leg
over `tools/*.sh` — SC2013 and SC2086 catch this class mechanically, and it is the second `for`-over-
unquoted-`$(...)` in this file's history.

---

### 8 — LOW · the rewritten path has no arm, and `legs_withheld` has no reader

**Site:** `tools/govkit/selftest.py` (absence), `tools/govkit/govkit.py:4582`.

The withheld-legs ownership path was round 1's blocker and is materially rewritten here. No arm
exercises it. The `-6` block's AC5 fixture at `:7221-7238` looks like it should, but the silenced-leg
path appends to `_silenced_found` and calls `r.fail` only AFTER the write-back
(`govkit.py:4378`, drained at `:4543`), so `len(r.problems) == _legs_problems_before` still
holds at `:4447` and that fixture takes the WRITTEN path — which is exactly why AC5 can assert the
sibling leg is present. Grepping `selftest.py` for `gate legs: WITHHELD`, `are NOT written`,
`unresolved token` and `differs from what the receipt recorded` reaches nothing on this branch; the
`## WITHHELD` hits at `:7286-7293` are the outbox section of the OTHER branch. The `-13` D2 arm at
`:6905-6924` covers `adopt --re-adopt`, a different verb.

`grep -rn legs_withheld tools/` returns `govkit.py:4303`, `:4476` and `:4582` — three writers, zero
readers — so the recorded fact cannot be asserted either.

Per §7 a new gate is not landed until its failing case has been observed, and the regression this
guards is the permanent wedge described in finding 5.

**Fix.** One arm beside the existing `[-6]` leg fixtures: apply into a manifest fixture, force a
LEGS-step problem on the second run, assert the receipt's `gate_runner.emitted` still names the first
run's legs and `legs_withheld` is true, then assert a THIRD apply completes rather than raising the
ownership Refusal. Give `legs_withheld` a reader in the same edit — `govkit check` saying "the last
apply withheld its legs" is the smallest one that makes the field assertable.

**Left-shift.** The arm is the left-shift. Add the finding-5 and finding-6 assertions to it and one
fixture covers three of this report's rows.

---

## What was checked and came back clean

Stated because a skip that looks like a pass is indistinguishable from coverage.

**The withheld-path ownership set, on the paths that are not finding 5.**

- *First install, no prior receipt.* `receipt` is `None`, so `:4475` yields `[]`. Correct — nothing
  was ever written and the ownership set is genuinely empty.
- *`--re-adopt`.* `_cmd_adopt:6567-6585` carries `gate_runner` forward verbatim from the receipt being
  replaced, flag included. The D2 fix holds; the withheld carry-forward composes with it correctly.
- *`legs_withheld` reaching the receipt on every path.* Initialised `False` at `:4303` and written
  unconditionally at `:4582`, so it lands on the success path, the withheld path and the
  non-manifest path alike. A fresh (non-`--re-adopt`) `adopt` omits `gate_runner` entirely, so no
  stale flag is carried. The field is correct; it just has nobody reading it (finding 8).

**The drift-audit argument parser.** Executed across every shape, and it behaves as documented:

| invocation | result |
|---|---|
| *(no args)* | adopt mode, no positional |
| `--check` | check mode, no positional |
| `<dir>` | adopt mode, positional set |
| `--check <dir>` / `<dir> --check` | check mode, positional set — order-independent |
| `--check a b` / `a b` | `usage:` + exit 2 |
| `--bogus`, `--check=x` | `usage:` + exit 2 |
| `""` (explicit empty) | skipped, neither set |
| `--check "my dir/wf"` | positional preserved intact |

`"${@:-}"` is correct under `set -u` with zero positionals, and the `""` case absorbs the single
empty string it expands to. Two looseness notes, neither a finding: a repeated `--check` is accepted
silently, and a mistyped bare `check` is now taken as a workflows directory rather than refused (it
exited 2 before), so a typo renders rather than aborts — the render then reds against `[check]`, and
this is the unavoidable cost of an optional positional. The precedence at `:140`
(positional → env → derivation) is the right order and its comment is accurate.

**Fold-introduced regressions specifically hunted and not found.** The new `legs_withheld` key does
not owe a `RECEIPT_SCHEMA` bump — `:45` scopes that to per-role ROW fields and this is an envelope
sibling. No reader rejects unknown keys under `gate_runner`. The `-H` flag changes only the
single-file case in both `check-install-prefix` arms and is a strict improvement in both. The
`emitted` carry-forward does not double-count on a subsequent successful run, because the manifest
branch reads `owned` from the receipt and rebuilds `existing` by name.

---

## The pattern worth landing before the next fold

Four fixes, three of which stopped at the instance the report named:

- the `{manifest_path}` token reached the leg and the hole, but not the hole's only CONSUMER;
- the `{prefix}/review-harness` positional reached two of its three carriers;
- the `kits` shape guard reached one of two branches, and one of two nesting levels;
- the withheld-legs carry-forward reached one of two branches.

The one fix that is complete — the argument parser — is complete because it was a rewrite of a whole
unit rather than a patch to a named line. §7's rule is already written for this ("Gate the CLASS, not
the instance. Fixing one file and scanning only that file certifies coverage you do not have"), and
the two gates it recommends here are small: a grep leg banning `resolve_tokens(...)[0]` at argv sites,
and a `selfcheck` arm requiring an entry's `[check]` argv and its same-script `[[gate_leg]]` argv to
agree. Between them they close findings 1 and 2 as a class rather than as two lines.
