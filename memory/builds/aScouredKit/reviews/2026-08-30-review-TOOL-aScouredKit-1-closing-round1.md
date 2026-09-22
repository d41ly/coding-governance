**Serves:** diff-review TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15

# aScouredKit — closing Tier-2 review, ROUND 1

*Adversarial diff review of the build's own fixes. Node `a`, 2026-08-30. Every finding below was
re-derived against the tree in this worktree before it was written down; the severities in the table
are this report's adjudication, not the finders' self-grading.*

**Range:** `093730e40355d6a04300966f791f2634379e8b45...HEAD` (8 commits, 14 units).

**ROUND:** 1.

## Verdict: BLOCKED

One blocker. `tools/govkit/govkit.py:4446` blanks the receipt's gate-leg ownership on the withheld
path, which permanently wedges the next `apply` at every existing adopter — and TOOL-aScouredKit-12,
in this same diff, changes two leg argvs and so pulls the trigger on the first re-`apply` everywhere.
It is the same defect this build fixed one function away at `govkit.py:6530`, reintroduced on the
other side of the file. Three high findings follow it: a shipped gate that can no longer fail on a
path with a space, a half-applied fix inside one descriptor that permanently exempts a
default-selection leg from its own red criterion, and a `subject = repo` leg that has no green state
in a govkit-deployed adopter.

**Review shape.** Raw 21, confirmed 15, refuted 6, unverified 0, precision 0.71. The 15 confirmed
findings collapse to 10 distinct defects: three lenses independently reported the
`check-install-prefix.sh` `xargs` regression (F2), two reported the `kickoff-manifest` hole probe
(F3), two the `DRIFT_WORKFLOWS_REL` override (F4), and two the unlanded S3 hoist (F7). Convergence
across independent lenses is corroboration, so each merged finding carries the strongest reachability
argument of its contributors.

## Findings

| # | Sev | Site | One line |
|---|-----|------|----------|
| F1 | BLOCKER | `tools/govkit/govkit.py:4446` | Withheld path blanks the receipt's leg ownership and wedges the next `apply` |
| F2 | HIGH | `tools/check-install-prefix.sh:74,202` | Bare `xargs` word-splits paths, so a shipped gate reads fewer files than it claims and prints clean |
| F3 | HIGH | `tools/govkit/entries/kickoff-manifest.kit.toml:54` | Hole probe left un-pathed, so it exempts the leg the same unit just fixed |
| F4 | HIGH | `tools/drift-audit/adopt-drift-audit.sh:122` | Env-only override nothing can supply makes `drift-audit wiring` unsatisfiable in a deployed adopter |
| F5 | MEDIUM | `tools/govkit/govkit.py:4393` | `chunk` decides a hold but travels in no descriptor, no agreement check and no emitted row |
| F6 | MEDIUM | `tools/check-install-prefix.sh:74,202` | Both batched greps assume a `<file>:` prefix that a one-file invocation does not emit |
| F7 | MEDIUM | `memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-6.md:23` | Closed unit's spec claims a hoist that is not in the diff |
| F8 | LOW | `tools/drift-audit/selftest.py:111` | Enlarged conf fixture still dark on the one spelling that still diverges |
| F9 | LOW | `tools/govkit/govkit.py:446` | A non-string element in the target's `kits` crashes the refusal written to reject it |
| F10 | LOW | `tools/govkit/selftest.py:2017` | New arm's predicate is a substring test that its target population satisfies trivially |

---

### F1 — BLOCKER · `tools/govkit/govkit.py:4446`

TOOL-aScouredKit-11 added `emitted = []` on the WITHHELD branch of `_cmd_apply`'s gate-runner step.
The manifest is correctly not rewritten there, but the receipt at `govkit.py:4546` is written
UNCONDITIONALLY — there is no early return and no `if not r.problems:` guard between the two. So a
withheld run leaves the target's runner file holding the legs a prior apply wrote, and the receipt
claiming none of them.

`owned` at `govkit.py:4324` is derived solely from `receipt.gate_runner.emitted`. The next `apply`
therefore computes `owned = set()`, reaches `nm in by_name and nm not in owned` at `govkit.py:4378`,
and raises a hard `Refusal`: *the target's runner already has a leg named 'X' and this target's
receipt does not claim it*. That accuses the adopter of authoring gov's own leg. There is no local
repair short of hand-editing `.governance/install.json` or the runner, and `adopt --re-adopt` cannot
help — it carries `gate_runner` forward from the blanked receipt.

The trigger is live in this diff rather than hypothetical. TOOL-aScouredKit-12 changed the argv of
`kickoff-manifest ratchet` (now carrying `{manifest_path}`) and of the agent-cap restatement leg, so
`prev.get("argv") != argv` at `govkit.py:4404` fires on every existing adopter's next `apply`,
withholds, and blanks. `kickoff-manifest` is in the registry DEFAULT selection.

The comment at `govkit.py:6528-6535` describes this exact chain, verbatim, as the D2 defect this same
build had just fixed in `cmd_adopt`. The class existed pre-11 for the single drifted leg, whose
`continue` skipped its own `emitted.append`; -11 widens it from one leg to all of them and moves the
abort to the first leg met.

**Fix.** Keep what the receipt already legitimately owns instead of clearing the list:

```python
emitted = [e for e in ((receipt or {}).get("gate_runner") or {}).get("emitted", [])
           if e.get("name") in by_name]
```

The receipt then claims exactly what is in the target's runner and no more, which is the property the
withheld branch's own comment says it wants.

**Left-shift.** A `selftest.py` arm that applies, forces an in-loop leg failure on a second apply, and
asserts the THIRD apply exits without the "already has a leg named" `Refusal`. Stage the break first
and confirm it RED against the current code — the arm is worthless if it has only ever passed.

---

### F2 — HIGH · `tools/check-install-prefix.sh:74` and `:202`

TOOL-aScouredKit-6 replaced two quoted per-file loops with bare `xargs` — no `-0`, no `-d`. `xargs`
word-splits on whitespace and parses quotes, so a tracked path with a space is split into
non-existent arguments and skipped, and a path with an apostrophe aborts the whole invocation.

Both halves reproduce on this node. `printf '%s\n' "don't.md" other.md | xargs -r grep -c x --`
prints `xargs: unmatched single quote`, runs grep zero times, and exits 1. In the script that stderr
goes to `2>/dev/null` and the status is swallowed by `|| true`, so `hits` is empty and the arm prints
`install-prefix: clean … no undeclared root-install spelling` having read nothing. The space case
drops the file with no trace at all. `git ls-files` emits both spellings unquoted; `core.quotePath`
only touches non-ASCII, control, backslash and double-quote.

The replaced code was a `while IFS= read -r f` loop running `grep -nE "$RE" -- "$f"` on one quoted
path, which handled both. The new comment's claim that "the list is newline-delimited exactly as the
`$files` variable already was, so no path handling changes" is false.

This is a shipped kit (`tools/govkit/entries/check-install-prefix.kit.toml:14`) whose leg is
`subject = repo`, `guard = []` — it runs on every adopter's bar, over the adopter's own `tools/*`,
`skills/*` and `.githooks/*`, where such names are ordinary. In gov's tree the apostrophe case would
red on the stale-waiver arm's twelve rows, so gov gets a wrong remedy rather than a false green; the
adopter's waiver registry ships seeded EMPTY, so there the stale loop never iterates and the arm
prints clean over a population it never read. The space case prints clean in both trees. gov itself
has zero whitespace paths today, which is exactly why it is green and lying.

The inconsistency is internal to the unit: the two sibling sites batched in the SAME commit,
`tools/memory-tree/check-method-carriers.sh:71` and `tools/unattended/check-playbook.sh:180`, both use
`git ls-files -z` + `xargs -0`, and one of them names this reason in its own comment.

**Fix.** Feed both pipelines NUL-delimited. Arm 1: build `files` with `git ls-files -z`, keep the
exclusion filters NUL-aware, and pipe to `xargs -0 -r`. Arm 2: `printf '%s\0' "$f"` in the filter loop
and `xargs -0 -r`. Drop the `2>/dev/null` from the `xargs` pipeline or route its stderr somewhere a
human sees it, so an aborted run can never look like a clean one.

**Left-shift.** The gate's own self-test creates a scratch repo containing `tools/a b.md` and
`tools/don't.md`, each carrying a live root-prefix literal, and asserts both appear in `--list`. That
is a class gate, not an instance fix, and it would also have caught F6.

---

### F3 — HIGH · `tools/govkit/entries/kickoff-manifest.kit.toml:54`

TOOL-aScouredKit-12 passed `{manifest_path}` into the gate leg's argv at line 43 and left the sibling
`[[hole]] manifest-section-b` discharge probe on the un-pathed
`command = ["bash", "{prefix}/manifest-check.sh"]` eleven lines below — under a comment describing the
defect as fixed. Given no path argument, `skills/session-kickoff/manifest-check.sh:33` falls back to
the hardcoded `MANIFEST_LOCATIONS="memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md"` and
exits 2 with `no kickoff manifest at …` for any other location.

Two consumers run that probe, and neither is gated behind `--run-discharge`:

- `cmd_check`'s hole loop (`govkit.py:2739-2765`) reports `manifest-section-b` UNDISCHARGED forever at
  any `manifest_path` outside those two, however completely the adopter authored their manifest.
- `exempt_leg` (`govkit.py:3104-3117`, reached from `govkit.py:4540`) returns `True` on any non-zero
  probe exit, granting the `kickoff-manifest ratchet` leg a standing red-after-install exemption. The
  unit made that leg able to fail; the un-fixed probe guarantees nobody hears it.

Not hypothetical: govkit's own fixtures declare `docs/SESSION-KICKOFF.md` (`selftest.py:175`) and
`docs/KICK.md` (`:829`). gov is unaffected because its manifest sits at the first hardcoded location —
the adopter-asymmetry class this whole build is about.

**Fix.** `discharge = { command = ["bash", "{prefix}/manifest-check.sh", "{manifest_path}"] }`. That
alone is not enough: `exempt_leg` builds its own ctx at `govkit.py:3108` as the hardcoded
`{"kit", "prefix", "kit_id", "memory_root"}` and discards `resolve_tokens`' miss list, so
`{manifest_path}` would be passed through as a literal token string. Give `exempt_leg` the target's
`target_context(...)` and make an unresolved token in a discharge command a refusal there, matching
what `cmd_check` already does at `govkit.py:2752`.

**Left-shift.** A `selfcheck` arm asserting that every token appearing in any `gate_leg.argv` is also
resolvable in every `hole.discharge.command` of the same entry — the "gate the class, not the
instance" rule applied to the descriptor's two argv-bearing fields. Cheap, static, and it fails today.

---

### F4 — HIGH · `tools/drift-audit/adopt-drift-audit.sh:122`

`WORKFLOWS_REL="${DRIFT_WORKFLOWS_REL:-$WORKFLOWS_REL}"` makes the rendered Skill's bytes depend on an
environment variable persisted nowhere, while `--check` re-renders and byte-diffs against the
committed Skill with no environment at all. The shipped workaround is self-defeating on the check
path.

`tools/workflows/kit.toml` declares `id = "review-harness"`, so govkit lands the harnesses at
`{prefix}/review-harness` — resolving the entry live prints `tools/review-harness/drift-audit-code.js`
— while line 118 derives `${KIT_REL%/*}/workflows`. In a DEFAULT deployment selecting both kits the
harnesses exist and TOOL-aScouredKit-15's new `_wf_missing` assertion reports them absent, reddening
the `drift-audit wiring` leg (`tools/drift-audit/kit.toml:85`, `subject = repo`, `guard = []`)
permanently.

Following the refusal makes the other guard fail. Render with
`DRIFT_WORKFLOWS_REL=tools/review-harness` and the committed Skill carries that path, but `--check`
re-renders env-less to `tools/workflows` and the diff arm at lines 163-170 reds FIRST, before
`_wf_missing` is ever reached, with the misleading "out of sync with SKILL.template.md" message and
the remedy `re-render with: $0` — which, run env-less, overwrites the correct Skill with the dead
pointer the unit exists to prevent. Nothing can supply the variable: `[adopt]` (`kit.toml:34`),
`[check]` (`:38`) and the leg (`:85`) are all bare `bash {kit}/adopt-drift-audit.sh`, and govkit has
no env mechanism anywhere.

Before this unit the leg was green and lying; it is now unsatisfiable for the govkit-deployed adopter
who selected the harness kit. Two caveats that do not overturn it: an adopter could set
`[kit.review-harness] kit = "tools/workflows"` in `deploy.toml` and rename to match the guess, and the
underlying missing cross-entry token is tracked OPEN as TOOL-aScouredKit-26. That backlog row records
the durable fix while asserting the override "worked around its absence" — it does not record that the
new assertion makes a `subject = repo` leg unsatisfiable in the default deployment, and spec-15 §5
only anticipates the adopter who did NOT select the harness kit.

**Fix.** Persist the answer where both the render and the check read it, which is the shape
TOOL-aScouredKit-12 used twice in this same diff. Either take it as `$1` and put
`{prefix}/review-harness` into `argv` for adopt, check and the leg in `tools/drift-audit/kit.toml`, or
read a declared key from `.memory-tree.conf` (which this script already opens at line 49 for
`MEMORY_ROOT`), document it in `.memory-tree.conf.example`, and make `_wf_complain` name the conf key
rather than an env var the gate will never see.

**Left-shift.** A kit self-test that runs `adopt` then `--check` in a scratch tree where the harnesses
sit at a NON-sibling path, asserting `--check` exits 0. gov's own layout cannot distinguish the two
answers, which is precisely what spec-15's AC1 measured and missed.

---

### F5 — MEDIUM · `tools/govkit/govkit.py:4393`

TOOL-aScouredKit-3 makes `chunk` co-equal with `subject` in deciding whether a leg runs — the runner
holds on `subject == kit OR chunk == selftests` (`run-gates.sh:947`) — and pins it. Only half the
deciding pair can travel.

`chunk` appears in no kit descriptor: grep over `tools/govkit/entries/*.toml` and `tools/*/kit.toml`
finds one prose mention and no field. The emitted row is `{"name", "argv"}` plus a conditional
`subject`/`guard`, so `chunk` never reaches a target, where `run-gates.sh:909` defaults it to
`default`. And selfcheck's descriptor-vs-manifest agreement block (`govkit.py:1288`) compares
`subject` only; `manifest_chunk` is read at `:1267` solely to build the pin file, which grades gov's
manifest against itself.

The defect that block's own rationale describes — *"deploys a leg that is held in the target and run
here, or the reverse"* — is live on the untravelled half. Six legs in `tools/gate-legs.json` carry
`subject = repo` with `chunk = selftests`; three of them are shipped by descriptors that declare
`subject = "repo"` and no chunk: `push-main self-test` and `pre-push self-test`
(`tools/govkit/entries/push-main.kit.toml:49,62`) and `run-gates canary`
(`tools/run-gates/kit.toml:74`). Their engines ship, so no `_silenced` withholding applies. gov holds
these three off its own bar and ships every adopter a runner that executes them on every push, and
nothing reds.

**Fix.** Extend the agreement block at `govkit.py:1288` to compare `leg.get("chunk")` against
`manifest_chunk[nm]` the way it already compares subject; declare `chunk` on the three descriptors;
emit it beside `subject` at `govkit.py:4393` under the same `check_target_reads_subject` floor.

**Left-shift.** The agreement extension IS the gate — it fails on all three legs today. Add a
`run-gates canary` pin arm asserting the emitted row carries `chunk` whenever the descriptor declares
one, so the emitter and the checker cannot drift apart again.

---

### F6 — MEDIUM · `tools/check-install-prefix.sh:74` and `:202`

Distinct from F2 and fixed by a different flag. Both batched greps depend on grep prefixing each
result with `<file>:`, which grep only does when the invocation receives more than one file. Verified
here: `grep -nE 'a' -- one.txt` prints `1:aaa` and `grep -cE 'a' -- one.txt` prints `1`, both
unprefixed; two files yield the prefix. `xargs --show-limits` reports ~20.8 KB usable, so `xargs`
produces one-file invocations whenever the list overflows with a single path remaining — and a small
adopter reaches a one-file population outright.

At line 74 the `cut -d: -f1,2` then yields `<lineno>:<match-fragment>`, which matches no waiver row, so
the gate reds with a garbage hit and `sed -n "${h##*:}p" "${h%:*}"` tries to read a file named after a
line number. At line 202 the `awk -F: 'NF>=2'` silently drops the unprefixed count, so a genuinely
carrying file vanishes from the ratchet and the shrink-only pin falls without cause. gov's two lists
measure 6067 and 6707 bytes today, so this is latent here and live per-tree elsewhere.

**Fix.** Add `-H` to both: `xargs -0 -r grep -HnE "$RE" --` and `xargs -0 -r grep -HcE "$re_ship" --`.
`-H` forces the prefix regardless of the invocation's file count, which is the property both pipelines
already assume.

**Left-shift.** Same scratch-repo self-test as F2, with one arm whose population is exactly ONE file
carrying one literal. It fails today and it pins the assumption rather than the symptom.

---

### F7 — MEDIUM · `memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-6.md:23`

Scope item S3 declares "both per-file loops batched, AND the double `carried_population()` call on the
`--check` path hoisted to one". `git show 3eaf38d0 -- tools/check-install-prefix.sh` contains only the
two batching hunks. No hoist landed, and the tree still calls it twice on BOTH branches:
`carried_live` (`tools/check-install-prefix.sh:173`) and `carried_rows` (`:198`), invoked at `:241`
and `:244` on `--check`, `:225` and `:229` on `--write-ratchet`. Each call spawns the resolved python
and imports govkit to resolve every descriptor.

rev-2's revision log declares the unit built and records only AC1's byte comparisons; §6 has no AC
covering S3, so nothing on the bar can catch the gap and no revision note descopes it. The build
roster marks unit 6 CLOSED. A closed unit whose spec names work that is not in the diff is exactly the
record-vs-reality drift this repo's own drift-audit exists to red — inside the build whose subject is
discovery cost.

One correction to the finders, both of whom measured under contention. The 15.97 s figure did not
reproduce: `bash tools/check-install-prefix.sh` runs in ~4 s on node `a` right now and one
`carried_population` costs ~1 s over 183 sources, so the duplicate is worth roughly a second, not half
of sixteen. The claim's direction holds; its magnitude was inflated by load.

**Fix.** Either land the hoist — capture `pop=$(carried_population | tr -d '\r')` once at the top of
each branch and feed both readers — or rev-bump the spec and strike the clause with a §9 note, the way
specs -1 and -2 were amended in this same build.

**Left-shift.** Not a gate; this is what the drift-audit tier already exists for. Add the closed-unit
scope-vs-diff question to the build's own wrap-up derivation in `BUILD-METHOD.md`, so a unit cannot be
marked CLOSED with a scope item no AC covers and no revision note drops.

---

### F8 — LOW · `tools/drift-audit/selftest.py:111`

The `conf parser vs bash` fixture enlarged by TOOL-aScouredKit-5 adds the two spellings the unit found
and leaves the third dark: a QUOTED value with a trailing inline comment. Reproduced here — with
`DISCIPLINES="tooling playbook"   # the enum`, bash yields `tooling playbook` and
`drift_report.load_conf` yields `"tooling`. The quoted branch at `drift_report.py:114` tests
`v[0] == v[-1]`, which a trailing comment defeats, so the value falls to the new `v.split()[0]` and
keeps a leading quote.

`MEMORY_ROOT` is read through this parser (`drift_report.py:1379`), so the same spelling silently
mis-resolves every path the report walks rather than refusing. The unit's whole premise was that this
fixture had never observed a divergence; it is enlarged by two arms and the gate still passes over the
gap. `tools/codebase-map/map_lib.py:197` carries the identical logic, so the copy is faithful — but
this gate's stated operand is BASH, not `map_lib`, so faithfulness is not the question it asks, and no
conf or README declares a grammar forbidding the spelling.

**Fix.** Add `QUOTED_COMMENT="a b"   # a trailing comment` to the fixture body and to the key list at
`:124`, observe it RED, then strip a trailing `\s+#.*` before the quote test in BOTH `load_conf`
copies.

**Left-shift.** The fixture arm is the gate. Add the same key to the `map_lib` side so the two copies
are graded against bash independently rather than against each other.

---

### F9 — LOW · `tools/govkit/govkit.py:446`

TOOL-aScouredKit-13's new `declared = list((deploy or {}).get("kits") or [])` branch assumes every
element of the target-authored `kits` array is a string. `load_deploy` (`govkit.py:814-822`) does no
shape validation, so a target writing `kits = [1, 2]` produces `unknown = [1, 2]` and
`', '.join(unknown)` raises `TypeError: sequence item 0: expected str instance, int found` — inside
the very `Refusal` written to reject the value. `main` at `govkit.py:6888` catches only `Refusal`, so
the operator gets a raw traceback from `plan`/`apply`. A nested-list element crashes one line earlier
at the unhashable membership test; same outcome.

On the trust boundary this is the only new path where a target-authored value reaches anything, and it
does still reach only a membership test — the STRICT grading contract is intact. It fails on
diagnostics, not on safety, which is why it is low.

**Fix.** Grade the shape first: `bad = [k for k in declared if not isinstance(k, str)]`, raising a
`Refusal` naming `repr(k)`, before the `k not in descs` pass. One line, and it keeps every
target-descriptor defect on the `Refusal` path the rest of the file uses.

**Left-shift.** A selftest arm running `plan` against a fixture with `kits = [1]` and asserting the
output is the named refusal, not a traceback. It generalizes: one arm per malformed-`deploy.toml`
shape, which the M3 receipt-shape refusal already established as a pattern here.

---

### F10 — LOW · `tools/govkit/selftest.py:2017`

The new arm's predicate `"memory-tree" in w or "memory" in w or w.endswith(".conf")` cannot
discriminate. Running `plan` against the exact `DEPLOY_FULL` fixture confirms all 26 write rows are
`tools/memory-tree/*`: `"memory-tree" in w` alone decides every element, `"memory" in w` is strictly
weaker and adds only false acceptance, and `w.endswith(".conf")` matches ZERO paths (the only
conf-ish one ends `.example`) — a dead clause.

The gap is concrete. `registry.toml:36`'s default includes `memory-recall`, whose home is
`tools/memory-recall` with a rendered target under `.claude/skills/memory-recall/`; every one of its
paths contains `memory`, so a leak of memory-recall — the requires-neighbour of memory-tree, and thus
the likeliest leak — passes this arm unchanged. The adjacent strict-subset arm cannot catch it either,
since memory-tree + memory-recall is still a strict subset of the six-kit default, and grep finds no
arm pinning the printed selection line at all. Test-arm weakness rather than product behaviour, but
it is the §7 "predicate that never matched its target population" class this repo left-shifts.

**Fix.** Assert against the kit's own resolved destinations rather than a substring: derive the
memory-tree entry's write set with the `resolve_entry`/`planned_writes` pair the harness already uses
and check equality. At minimum drop the two dead clauses and anchor on the `tools/memory-tree/` path
prefix.

**Left-shift.** Pin the printed `selection:` line as its own arm, so a leaked kit is caught by name
rather than by a path-shape heuristic.

---

## Notes on scope

Nothing here reports the by-design set: kit self-tests off the merge bar, `GATE_SELFTESTS=1` as the
on-demand route, the 48 KiB charter ceiling and its advisory WARN, or the twelve backlog rows this
build added on purpose.

Both AGENTS.md prose cuts were checked against the hunt list. Each names a surviving carrier in the
same file, both carriers exist, and both carry the property claimed — no finding filed.

The `resolve_selection` trust-boundary question was answered directly: target-supplied `kits` values
reach a membership test against the descriptor set and the refusal message, and nothing else. F9 is
the only defect on that path and it is a diagnostics failure, not an argv escape.
