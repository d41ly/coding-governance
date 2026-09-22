**Serves:** diff-review TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-15

# aScouredKit — closing Tier-2 review, ROUND 3

*Adversarial review of the SECOND FOLD, not of the build. Node `a`, 2026-08-30. The base is round 2's
recorded tip, so the diff under review is the eight fixes round 2 bought and nothing else. Every
finding below was re-derived against the tree in this worktree, and where the report says
"reproduced" or "measured", executed. Two of them were proved by staging the break and observing the
suite. The severities in the table are this report's adjudication, not the finders' self-grading.*

**ROUND:** 3.

**Range:** `13e2cfc2...HEAD` (1 commit, `14cac4aa`, 14 files, 5 of them product).

## Verdict: BLOCKED

Two blockers, both fold-INTRODUCED, and both on the same file. The drift-audit unit
(TOOL-aScouredKit-15) exists to remove a silence: a rendered Skill that instructs an agent to run two
files that are not there, over a gate leg reporting "in sync". This fold replaced the round-2 defect
with two new mechanisms that restore that silence — a persisted answer that does not survive a clone,
and a branch that reads "the directory I derived is absent" as "the sibling kit is not installed".
Together they close the loop the wrong way: on a fresh checkout the leg reds with a misdiagnosis, and
following the remedy it prints overwrites the correct committed Skill with a dead pointer, after
which the leg exits 0. Reproduced end to end in a fixture repo, twice, at a clean path.

The rest of the fold is better than round 2's but not clean. The `kits` shape guard was hoisted above
the branch split exactly as round 2 asked and is then defeated one frame up, at the only caller that
feeds it a target-authored value — so round 2's finding 3 survives verbatim on the `adopt` path, and
the new comment asserting the opposite is now a false claim about the code beneath it. The
`exempt_leg` fix is correct in direction and over-reaches: its `return False` short-circuits the
whole function, so an unresolvable probe on one hole now vetoes an exemption that a *different*
mechanism had already earned. And the wedge class that produced round 2's blocker now has one honest
arm out of three: the "end to end" arm hand-restores the exact field the production fix supplies, and
the second carry-forward this fold added has no arm at all.

**The finding behind the findings, again.** Round 2 said every fix was scoped to the instance rather
than the class. This fold fixed that for the shape guard (hoisted above the split) and then reproduced
the same error one level higher; fixed it for the ownership carry-forward (both branches) and graded
only one of them; fixed the `check-install-prefix` consumers and left the producer that feeds them
word-splitting. Three of eight fixes are correct and complete.

**Review shape:** raw 22 · confirmed 18 · refuted 4 · unverified 0 · precision 0.82. The 18 confirmed
raws consolidate to the 6 distinct defects the finders found (four raws named the `kits` call site,
four named the `.workflows-rel` precedence, three named the store's durability, four named the vacuous
selftest arm, two named the absent-kit branch, one named the waiver producer). Consolidation is not
refutation — the duplicates agreed on file, line and mechanism. Four rows below (F, G, I, K) are this
report's own and were not in the finder set.

**Banked, not findings.** `TOOL-aScouredKit-27`, `-28` and `-29` are tracked and were deliberately not
fixed in this fold. The open rows in `memory/backlog/TOOL.md` are tracked. Kit self-test suites are
off the merge bar by owner ruling 2026-08-23. None are re-reported here.

---

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| A | **BLOCKER** | `tools/drift-audit/adopt-drift-audit.sh:251` | the persisted answer is untracked and nothing stages it, so the bar leg reds on any fresh checkout — and the remedy it prints overwrites the committed Skill with the dead derived path |
| B | **BLOCKER** | `tools/drift-audit/adopt-drift-audit.sh:166` | `_wf_absent_kit` cannot tell "the sibling kit is absent" from "the sibling kit is elsewhere", so a wrong answer now exits 0 with a false note instead of redding |
| C | HIGH | `tools/govkit/govkit.py:6365` | `cmd_adopt` pre-coerces the target-authored `kits` with `list(...)`, so the hoisted `_graded` container guard never sees it — round 2's finding 3, verbatim, on the one path the new comment claims it closed |
| D | HIGH | `tools/drift-audit/adopt-drift-audit.sh:148` | a stale store outranks a NEW `DRIFT_WORKFLOWS_REL`, and the persist block then rewrites the stale value under a message saying the operator's answer was recorded |
| E | MEDIUM | `tools/govkit/selftest.py:1099` | the "a later apply RECOVERS" arm hand-restores the receipt field the production fix supplies, so it passes with the wedge fully present — measured |
| F | MEDIUM | `tools/govkit/govkit.py:4590` | the fold's SECOND ownership carry-forward has no arm anywhere: reverting it to the wedge leaves the whole suite green — measured |
| G | MEDIUM | `tools/govkit/govkit.py:3164` | the new fail-closed `return False` exits the whole function, vetoing the independent `red_after_land` exemption and the remaining hole probes |
| H | MEDIUM | `tools/drift-audit/kit.toml:10` | the store lives inside the kit's `include = "**"` engine surface with no `project-owned` carve-out, the exact shape that once destroyed `drift_signals.py` |
| I | LOW | `tools/check-install-prefix.sh:86` | the consumers were hardened for spaced paths; the waiver PRODUCER still word-splits with `awk '{print $1}'`, so a spaced hit is unwaivable |
| J | LOW | `tools/govkit/govkit.py:3155` | `exempt_leg`'s `deploy=None` fallback is unreachable and preserves the hardcoded `tools/`+`memory` context the fix above it condemns |

---

### A — BLOCKER · the persisted answer does not survive a clone, and the remedy destroys the Skill

**Site:** `tools/drift-audit/adopt-drift-audit.sh:245-252`, against
`tools/drift-audit/kit.toml:89-93`.

The fold's premise is sound: the gate leg cannot carry the sibling's path in its argv, so the answer
must be persisted. The location chosen is `{kit}/.workflows-rel`, and nothing in the kit, the
descriptor, govkit or the README makes that file reach the repository.

- No `[[files]]` rule claims it, so it is not a receipt row and not an `install.sums` line.
- `[adopt].mutates_index = false` is DERIVED and asserted (`govkit.py:1173-1195`), and govkit stages
  only its own plan destinations (`govkit.py:4106`), `.gitattributes` (`:3954`) and `gr['file']`
  (`:4494`).
- `git check-ignore` returns 1 and `grep -rn workflows-rel` over the whole tree returns exactly two
  hits: the script itself and a kit.toml comment. No doc, no printed line, nothing tells the operator
  to commit it.

Reproduced in a fixture repo at a clean path, using the descriptor's own `[adopt]` argv and then the
leg's own `[[gate_leg]]` argv:

```
$ bash tools/drift-audit/adopt-drift-audit.sh tools/review-harness
drift-audit: recorded the review-harness home as tools/review-harness in .workflows-rel
$ git status -s
?? tools/drift-audit/.workflows-rel          # the Skill is tracked; the answer is not

# commit as govkit stages it, then model a fresh clone / CI checkout / a second node:
$ rm -f tools/drift-audit/.workflows-rel
$ bash tools/drift-audit/adopt-drift-audit.sh --check
drift-audit: .../SKILL.md is out of sync with SKILL.template.md + .memory-tree.conf
  re-render with: tools/drift-audit/adopt-drift-audit.sh
< tools/review-harness/drift-audit-code.js
> tools/workflows/drift-audit-code.js
exit=1

$ bash tools/drift-audit/adopt-drift-audit.sh          # following the printed remedy
$ git diff --stat
 .claude/skills/drift-audit/SKILL.md | 4 ++--
$ bash tools/drift-audit/adopt-drift-audit.sh --check
drift-audit: in sync ... NOTE: no tools/workflows/ in this tree, so the review-harness kit is not
drift-audit: installed ... Not graded: this kit does not require it.
exit=0
```

The leg is `subject = "repo"`, `guard = []` — it runs on every adopter bar — and its failure message
blames template drift, which is not the cause. Following the only remedy it prints rewrites the
correct committed Skill to a path that does not exist and then reports green over it. A red converted
into a green with a broken artifact is worse than the round-2 defect it replaced, because round 2's
version stayed loud.

An operator's habitual `git add -A` sweeps the dotfile in by luck. That is not a channel, and it
breaks on the realistic upgrade path, where `git add -u` carries the Skill's new spelling and leaves
the new untracked store behind.

**Fix.** Make the answer travel in the repository. Cheapest correct form: declare it in
`tools/drift-audit/kit.toml` as a `[[files]]` rule with `role = "project-owned"` and
`to = "{kit}/.workflows-rel"`, so govkit claims, stages and receipts it the way it does
`drift_signals.py` — which also closes H. Failing that, `git add -- "$WORKFLOWS_STORE"` immediately
after the write, with the confirmation line saying `COMMIT THIS FILE — the --check leg reads it`.

**Left-shift gate.** Add a `--check` arm that distinguishes the two causes: when `SKILL.md` exists,
the store does not, and the Skill's rendered `{{WORKFLOWS_DIR}}` differs from the derivation, red with
"the recorded answer is missing from this checkout — do not re-render" rather than with the generic
out-of-sync message whose remedy destroys the answer. Then wire a govkit selftest arm that adopts with
the positional, drops the untracked store, and asserts the leg does NOT tell the operator to
re-render.

---

### B — BLOCKER · "not installed" and "installed somewhere else" are the same answer

**Site:** `tools/drift-audit/adopt-drift-audit.sh:166` (`_wf_absent_kit`), consumed at `:165` and
`:224`.

`_wf_absent_kit() { [ -d "$ROOT/$WORKFLOWS_REL" ] && return 1 || return 0; }` tests the DERIVED path,
not the sibling. When the derivation is wrong — which is the entire population TOOL-aScouredKit-15
exists for — an absent directory means "my guess was wrong", and this branch reads it as "that kit is
not installed". The in-code justification ("only honest because the descriptor now passes the
sibling's real home") holds for a govkit install and is false for the hand-install population, which
is the population `DRIFT_WORKFLOWS_REL` was added to serve. It is also false for A's fresh-checkout
case, where the descriptor's answer is gone.

Reproduced in a fixture repo where the harnesses really are at `tools/review-harness/`, with no
positional, no env and no store:

```
$ bash tools/drift-audit/adopt-drift-audit.sh
drift-audit: rendered .../SKILL.md            # and NOT ONE WORD of warning
$ grep -o 'tools/[a-z-]*/drift-audit-code.js' .claude/skills/drift-audit/SKILL.md
tools/workflows/drift-audit-code.js           # does not exist
$ ls tools
drift-audit  review-harness                   # it is right there
$ bash tools/drift-audit/adopt-drift-audit.sh --check
drift-audit: in sync ... NOTE: no tools/workflows/ in this tree, so the review-harness kit is not
drift-audit: installed ... Not graded: this kit does not require it.
exit=0
```

Two regressions in one branch. The `--check` leg now exits 0 over a Skill naming two commands that do
not run, and the early `return` inside `_wf_missing` (`:165`) also silences the ADOPT-time
`_wf_complain` at `:262-263`, so the operator is not told at render time either. Pre-fold this state
redded with a remedy naming the entry id; the fold converted it into a silent green. That is the
green-by-absence class the charter names, and it defeats this unit's own acceptance criterion.

**Fix.** Gate the branch on PROVENANCE, not on the path. Set `WF_EXPLICIT=1` where the value is
resolved — when `WORKFLOWS_ARG`, `WORKFLOWS_SAVED` or `DRIFT_WORKFLOWS_REL` supplied it, empty when it
came from the `case "$KIT_REL"` derivation — and let `_wf_absent_kit` return true only when
`WF_EXPLICIT` is set. An explicitly-answered path that is absent is the sibling kit's absence and
earns the note at exit 0. A DERIVED path that is absent is a guess that may be wrong and stays a
complaint. Optionally strengthen it: before concluding absence, probe `${KIT_REL%/*}/review-harness`
and red if the two `.js` files are found there instead.

**Left-shift gate.** A drift-audit selftest arm that plants the harnesses at `tools/review-harness/`,
adopts with NO answer, and asserts `--check` exits 1. Stage the break once and confirm RED before
landing it — this is a branch that has only ever been seen pass.

---

### C — HIGH · `adopt` still splats the target-authored `kits` before the guard can grade it

**Site:** `tools/govkit/govkit.py:6364-6365`, against the new guard at `:439-455`.

```python
selection = resolve_selection(reg, descs, "kits" if deploy.get("kits") else "default",
                              list(deploy.get("kits") or []))
```

The `list(...)` runs one frame above `_graded`. Reproduced against the live registry by executing the
real call-site expression:

| `kits =` in the target's `deploy.toml` | result |
|---|---|
| `5` | `TypeError: 'int' object is not iterable`, raised at `:6365` |
| `true` | `TypeError: 'bool' object is not iterable` |
| `"memory-tree"` | `Refusal: --kits names m, e, m, o, r, y, -, t, r, e, e, which are not a registry entry` |
| `{a=1}` | `Refusal: --kits names a, which is not a registry entry` |

`main` (`:6975`) catches only `Refusal`, so the first two are raw tracebacks out of `govkit adopt`.
The third is verbatim the character explosion the comment at `:435-439` says it removed ("Both now say
what is actually wrong"), and it names a `--kits` flag that `adopt` does not accept. `load_deploy`
(`:842`) is a bare `load_toml` with no shape validation, so nothing upstream filters it, and `adopt`
is the FIRST verb run against a target descriptor.

Sharper than round 2 could state it: the `_graded` call inside the `mode == "kits"` branch is now
**dead code**. The other three callers of that mode (`:2399`, `:3809`, `:6706`) all receive
`[k.strip() for k in argv[i+1].split(",")]` from the CLI, which is always `list[str]`. The only caller
that could ever hand it a non-list is the one that pre-coerces. The guard was hoisted to cover the
adopt path and covers nothing.

**Fix.** Stop duplicating the deploy read at the call site and let the default branch do it — it
already reads `deploy['kits']` itself at `:474`, grades it with the right label, and then runs
`derive_install_order(sorted(declared), descs)`, which is behaviour-identical to today's `"kits"`-mode
call for every well-formed descriptor:

```python
selection = resolve_selection(reg, descs, "default", [], deploy)
```

That removes the bypass and the second computation of one thing. While there, give the
`mode == "kits"` `unknown` refusal the same `where` label `_graded` takes, so no path says `--kits`
about a value that came from a descriptor.

**Left-shift gate.** `_graded` has NO selftest arm anywhere — `grep` for its refusal strings in
`selftest.py` returns nothing, which is why an untested half shipped. Add one table-driven arm over
`5`, `true`, `"memory-tree"`, `{a=1}`, `[1]`, `[["a"]]`, `[None]` driving `adopt` (not just `apply`),
asserting a `Refusal` and never a `TypeError`.

---

### D — HIGH · a stale store outranks a new explicit answer, and the confirmation line reports the wrong one

**Site:** `tools/drift-audit/adopt-drift-audit.sh:148` and `:250-252`.

`WORKFLOWS_REL="${WORKFLOWS_ARG:-${WORKFLOWS_SAVED:-${DRIFT_WORKFLOWS_REL:-$WORKFLOWS_REL}}}"` orders
`ARG > SAVED > ENV > derived`, while the persist block fires on `[ -n "$WORKFLOWS_ARG" ] || [ -n
"${DRIFT_WORKFLOWS_REL:-}" ]` and then writes `$WORKFLOWS_REL` — the RESOLVED value, which may be the
stale saved one. The condition asks about the answer's presence; the write is about something else.

Reproduced in a fixture repo:

```
$ DRIFT_WORKFLOWS_REL=tools/review-harness bash .../adopt-drift-audit.sh
drift-audit: recorded the review-harness home as tools/review-harness in .workflows-rel

$ DRIFT_WORKFLOWS_REL=tools/OTHER bash .../adopt-drift-audit.sh      # the operator corrects it
drift-audit: recorded the review-harness home as tools/review-harness in .workflows-rel
$ cat tools/drift-audit/.workflows-rel
tools/review-harness                          # correction discarded, stale value re-persisted
```

The precedence itself is stated in the code comment at `:143-144`, so that half is a decision. What is
not defensible is the rest, and it stands on its own. The confirmation line tells the operator their
answer was recorded when a different one was. And the script's own user-facing remedy at `:182` —
`Set DRIFT_WORKFLOWS_REL to the real path and re-run this script` — is inert in every govkit-deployed
tree, because `[adopt]`'s positional guarantees a store exists there. That is a gate teaching a repair
that does nothing. The only escape is deleting a dotfile the README never mentions.

The write is also unchecked. Only `set -u` is in effect, so on a read-only kit dir the redirect fails
and the same false confirmation prints.

**Fix.** The store is a CACHE of a previous explicit answer, so any fresh explicit answer must
outrank it:

```sh
WORKFLOWS_REL="${WORKFLOWS_ARG:-${DRIFT_WORKFLOWS_REL:-${WORKFLOWS_SAVED:-$WORKFLOWS_REL}}}"
```

That also makes `:250-252` correct as written, since `$WORKFLOWS_REL` is then the explicit answer
whenever the write fires. Guard the confirmation on the write itself:
`if printf '%s\n' "$WORKFLOWS_REL" > "$WORKFLOWS_STORE"; then echo ...; else echo "drift-audit: could
not write $WORKFLOWS_STORE" >&2; fi`.

**Left-shift gate.** A drift-audit selftest arm: adopt with answer X, re-adopt with answer Y, assert
the store holds Y and the confirmation line names Y. One arm covers both the precedence and the
message.

---

### E — MEDIUM · the "RECOVERS" arm is satisfied by its own fixture

**Site:** `tools/govkit/selftest.py:1097-1105`.

```python
_tamper["argv"] = [a for a in _tamper["argv"] if a != "--recorded-differently"]
_rcpt_now = json.loads(_rcpt_path.read_text(encoding="utf-8"))
_rcpt_now["gate_runner"]["emitted"] = (_pre_rcpt.get("gate_runner") or {}).get("emitted", [])
```

`_tamper` is a live reference into `_pre_rcpt`'s emitted rows, so by line 1099 that snapshot is the
original untampered list. The assignment then replaces, wholesale, whatever the withheld run left on
disk — which is precisely the work the production carry-forward at `govkit.py:4518` is supposed to do.
`owned` (`govkit.py:4384`) derives solely from that field, so `_wr2` sees a byte-identical receipt
whether or not the fix exists.

**Measured, by staging the break.** Patched `govkit.py:4518` to `emitted = []` and ran the suite:

```
FAIL AC-withheld: and the receipt KEEPS the previous ownership rather than blanking them
                  — pre=['check-wiring self-test'] post=[]
ok   AC-withheld: and a later apply RECOVERS — it is not wedged by the withheld run
govkit-selftest: 1 FAILED
```

Exactly one arm fails, and it is the FIELD arm at `:1089`. The arm billed by its own comment as "THE
WEDGE ITSELF, end to end ... this one is about the CONSEQUENCE" prints `ok` on a build with the wedge
fully present. The suite carries a claim it does not test. `govkit.py` was restored; the tree is
clean.

**Fix.** Repair only the tamper, never the ownership — un-tamper in place on whatever the withheld run
actually left:

```python
_rcpt_now = json.loads(_rcpt_path.read_text(encoding="utf-8"))
for e in (_rcpt_now.get("gate_runner") or {}).get("emitted", []):
    e["argv"] = [a for a in e.get("argv", []) if a != "--recorded-differently"]
```

With the fix the rows are there and the apply recovers; with the blanking there is nothing to
un-tamper, `owned` is empty, and `_wr2` hits `already has a leg named` — the arm failing for the right
reason. Drop the `_tamper["argv"]` mutation at `:1097`, which only touches the in-memory snapshot.

**Left-shift gate.** The gate IS the arm; what is missing is the observation. Stage `emitted = []`
once, confirm the corrected arm goes RED, unstage — the charter's own rule, and the one this arm was
landed without.

---

### F — MEDIUM · the fold's second carry-forward has no arm at all

**Site:** `tools/govkit/govkit.py:4590` (the `[gate_runner].kind = "none"` / ordered branch).

This fold fixed round 2's finding 5 by adding the same ownership carry-forward to the branch that
orders legs rather than emitting them. The fix reads correctly. Nothing grades it.

**Measured.** Restored `:4518` and patched `:4590` to `emitted = []` — the exact wedge the comment at
`:4584-4589` says it prevents — and ran the full suite:

```
exit=0 · 999 ok · 0 FAIL
govkit-selftest: all arms held
```

A fix that reverting leaves the suite entirely green is, by the charter's own words, an assertion
about nothing. Taken with E, the wedge class that produced round 2's blocker now has exactly ONE
honest arm across two branches and three arms.

**Fix.** None to the product — the carry-forward at `:4590` is right. Add the arm.

**Left-shift gate.** A `runner_target` fixture whose `deploy.toml` declares `[gate_runner] kind =
"none"` after a manifest-kind apply has already written rows: assert the post-run receipt's
`gate_runner.emitted` equals the pre-run one, and that a subsequent manifest-kind apply does not print
`already has a leg named`. Stage `emitted = []` and confirm RED before landing it.

---

### G — MEDIUM · the fail-closed return vetoes an exemption a different mechanism had earned

**Site:** `tools/govkit/govkit.py:3164-3168`.

The direction of the fix is right: an unresolvable probe must not grant an exemption, and a red leg is
visible where a silent exemption is not. The over-reach is the scope of the `return`. `exempt_leg`'s
own docstring says "Two ways, and nothing else", and the two ways are independent: an undischarged
hole probe, and the `red_after_land` window at `:3172`. The new `return False` exits the whole
function, so way #1 failing to RESOLVE now vetoes way #2 — and also skips the remaining holes, one of
which may be genuinely undischarged.

Measured with a synthetic descriptor against the real function:

```
hole h1 probe exits 0 (discharged) · hole h2 holds {manifest_path} · red_after_land window OPEN
-> govkit: leg 'L' — the hole probe for 'demo' holds unresolved token(s) manifest_path ...
-> exempt_leg(...) == False        # the open red_after_land window was never consulted
```

Reachable through the shipped descriptors: `kickoff-manifest.kit.toml` has both a `red_after_land`
leg (`:46`) and a `blocks_gate` hole whose probe carries `{manifest_path}` (`:58`), and `apply` does
not demand answers up front (`needed_answers` is `intake`-only). The consequence is a criterion FAIL,
so the trade is in the safe direction and this is not a blocker — but it reds a leg that a stated,
independent rule says is exempt, on a descriptor defect that has nothing to do with that leg.

**Fix.** Scope the failure to the hole it belongs to. Record the unresolvable probe, keep scanning:

```python
if missing:
    print(...)          # unchanged
    _unresolved = True
    continue            # not `return False`
...
if leg.get("red_after_land") and eid in configure_skipped:
    return True
return False            # falls through here when only unresolvable probes were seen
```

**Left-shift gate.** A selftest arm over a fixture descriptor carrying a `red_after_land` leg, a
skipped configure phase, and a hole probe with an unresolvable token: assert `exempt_leg` returns
True and that the unresolved-token line is still printed. A second arm with two holes — the first
unresolvable, the second failing — asserting True.

---

### H — MEDIUM · the store sits inside the `**` engine surface with no `project-owned` carve-out

**Site:** `tools/drift-audit/kit.toml:9-11`, against `tools/drift-audit/adopt-drift-audit.sh:145`.

`[[files]] include = "**" role = "engine"` expands to every TRACKED file under the entry's home not
claimed by another rule (`govkit.py:3285-3289`). `.workflows-rel` is claimed by no rule and is not in
`.gitignore` (`git check-ignore` exits 1). Today it is untracked in gov, so nothing ships — but the
moment any node runs the adopter with an explicit answer and commits with `git add -A`, gov's own
answer becomes an ENGINE row written into every adopter's kit dir, overwriting the answer their
`[adopt]` just recorded, on every `apply` and `update`.

That is not hypothetical reasoning: it is the measured incident recorded in `scan_claimed_paths`'
docstring, verbatim, about `drift_signals.py` — which is exactly why that file carries its own
`role = "project-owned"` rule three lines below the wildcard. `.workflows-rel` is the same kind of
file and has no such rule. A's fix and this one are the same edit.

On the target side there is no problem: nothing reverse-checks a kit dir for files the receipt does
not claim, and `install.sums` parity (`govkit.py:2678-2690`) compares the sidecar against the receipt
only. Gov's per-file-claim arm (selfcheck 7i) quantifies over `tracked(root)`, so the untracked file
is invisible to it — and if it becomes tracked, the wildcard claims it and 7i stays green while the
clobber ships.

**Fix.** Declare it: `[[files]] include = ["\.workflows-rel"] role = "project-owned"` (or whatever
spelling the include grammar takes for a dotfile), which both prevents the ship and makes A's staging
fall out for free.

**Left-shift gate.** Extend govkit's selfcheck: for every entry with a `**` include, any path the
entry's own adopter WRITES into `{kit}` must be claimed by a non-wildcard rule. Derive the written
paths from a grep of the adopter for redirects into `$KIT_DIR`, or — cheaper and honest about its
limit — assert that no file an adopter creates under its own home is left to the wildcard, and say in
the leg's header that it is a textual probe.

---

### I — LOW · a spaced hit can be reported and cannot be waived

**Site:** `tools/check-install-prefix.sh:86`.

The fold replaced both `--check` loops with `while IFS= read -r`, so a hit whose path contains a space
now survives intact. The waiver producer one line above still builds `waived_rows` with
`awk '{print $1}'`, and the documented waiver format is `<path>:<line>` followed by whitespace and a
reason. Reproduced against the real consumer predicate:

```
waiver row: tools/my kit/x.sh:5   reason
waived_rows == 'tools/my'
grep -qxF 'tools/my kit/x.sh:5' <<< 'tools/my'   ->  no match
```

So the gate reds forever on such a hit with no declared escape, and the stale-waiver loop at `:120-129`
then additionally reports `tools/my` as STALE. Latent in gov (170 shipped files, zero spaced paths,
gate green) and live in an adopter: `check-install-prefix.kit.toml` ships this script with a
`subject = "repo"`, `guard = []` leg and an EMPTY target-authored waiver registry.

**Fix.** Split the waiver row on the reason rather than the path — `sed -E 's/[[:space:]]{2,}.*$//'`
against a two-space-delimited format, or make the registry tab-delimited and read it with
`IFS=$'\t'`. If neither is wanted, say in the file's header that a path containing whitespace cannot
be waived, and have the `--check` loop say so when it reports one.

**Left-shift gate.** A `check-install-prefix` self-test arm over a temp tree holding one spaced path
and one waiver row naming it, asserting exit 0. It reds today.

---

### J — LOW · the `deploy=None` fallback is unreachable and preserves what the fix condemns

**Site:** `tools/govkit/govkit.py:3155-3157`.

```python
ctx = (target_context(target, deploy, eid, d) if deploy is not None
       else {"kit": f"tools/{eid}", "prefix": "tools", "kit_id": eid, "memory_root": "memory"})
```

`exempt_leg` has exactly one caller (`:4627`) and it passes `deploy`, which comes from `load_deploy`
and is always a dict (`load_deploy` refuses rather than returning None). The `else` branch is dead,
and what it preserves is the hardcoded four-key literal the comment eight lines above calls the defect:
"This dict spelled `tools/` and `memory` literally, so at any other prefix or memory root the probe
ran against paths the target does not have."

**Fix.** Delete the parameter's default and the branch; make `deploy: dict` required. Deletion over
disable.

**Left-shift gate.** None warranted — this is a two-line deletion, and gov's dead-code lens already
owns the class.

---

## Round 2's eight findings — status

| R2 | What it was | Verdict on the fix |
|----|-------------|--------------------|
| 1 | BLOCKER · `exempt_leg`'s hardcoded context | **Fixed**, and the fail-closed addition is the right direction — but over-scoped (**G**) |
| 2 | BLOCKER · leg and Skill disagree on the sibling path | **Not fixed.** Replaced by a non-durable side channel (**A**) and a conflating branch (**B**). The disagreement is now silent instead of loud |
| 3 | HIGH · shape guard in the `declared` branch only | **Not fixed.** Guard hoisted correctly, defeated one frame up at the only caller that matters (**C**) |
| 4 | MEDIUM · container vs elements | **Fixed** in `resolve_selection`, **defeated** at the `adopt` call site — same root as **C** |
| 5 | MEDIUM · blanking still standing on the `kind != "manifest"` branch | **Fixed** at `:4590`, and graded by nothing (**F**) |
| 6 | MEDIUM · falsified comment, un-suppressed self-test advisory | **Fixed.** Comment corrected, message reworded to "leg(s) in your runner", literal re-pinned in the arm. The advisory still fires after a withheld run, deliberately and with a stated reason — accepted |
| 7 | LOW · consumer loops word-split | **Half fixed.** Both consumers hardened, the producer that feeds them left word-splitting (**I**) |
| 8 | LOW · no arm for the withheld ownership path | **Half fixed.** Three arms added; one is genuine, one is vacuous (**E**), and the sibling branch still has none (**F**). `legs_withheld` now has a reader |

Three of eight correct and complete. Two moved their defect one caller over — the same sentence round
2 wrote, about a different pair of callers.

## Verification notes

- Findings A, B and D were reproduced in throwaway git repos at a clean filesystem path, using the
  descriptor's own `[adopt]` and `[[gate_leg]]` argv rather than hand-written invocations. All fixture
  trees were removed; `git status` is clean.
- Findings E and F were proved by staging the production break and running the full govkit selftest
  suite. `tools/govkit/govkit.py` was restored to HEAD in both cases and `git diff` is empty.
- Finding C was reproduced by executing the real call-site expression from `:6364-6365` against the
  live registry and descriptors.
- Finding G was measured against the real `exempt_leg` with a synthetic descriptor; the reachability
  claim rests on reading `kickoff-manifest.kit.toml` and `needed_answers`' single caller, not on an
  end-to-end run.
- `bash tools/check-install-prefix.sh --check` is green on this tree (170 shipped files, 12 waivers),
  and the full govkit selftest is green at HEAD (999 arms, all held). Neither green contradicts a
  finding above; both are stated so no reader mistakes them for coverage.
