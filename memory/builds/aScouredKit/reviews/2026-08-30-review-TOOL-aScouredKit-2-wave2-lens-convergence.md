# Wave 2 — LENS B, govkit convergence: deploy · update · wire · check

## Verdict: CLEAN WITH FIXES

**Serves:** research TOOL-aScouredKit-2
**Subject:** the whole product surface at `093730e40355d6a04300966f791f2634379e8b45`
**Question, verbatim:** "can every tool in the kit be deployed, updated, wired to another project?"

Everything below was measured by driving `tools/govkit/govkit.py` into throwaway repositories on this
host. No claim here rests on reading alone. Commands are in §5.

---

## 1. Verdict, one paragraph

**DEPLOY: mostly, and nothing on the bar proves it.** 11 of the 25 registry entries are never passed
to `apply` by any gate, because the leg that was supposed to do that per entry —
`tools/govkit/deployability.test.sh`, AC7/AC8 of a spec marked CLOSED — was never written, and
`matrix.py` narrows its own scope on the written premise that it exists (F3).

**UPDATE: no.** `govkit update` still cannot land a source gov started shipping, re-measured today
(§4, confirming `TOOL-aFlaggedScaffold-3`).

**WIRE: broken by a one-line guard.** `apply` writes the target's gate-leg manifest only when the
whole run has zero problems, and the problems that stop it are by-design outcomes of a normal first
install. One kit whose adopter legitimately cannot complete deletes the gate coverage of every other
kit in the same run, while the receipt records all of them as emitted (F1, blocker).

**CHECK: the arm exists and gov does not run it on itself.** The rule that a `[check]` must declare
either an argv or a reason is enforced only inside `cmd_check`, against a target. `selfcheck` has the
identical arm for `version_from` and not for `[check]`, so a descriptor gov ships violates gov's own
rule with gov's bar green (F5).

And a whole-run defect that sits above all four verbs: **`plan` and `apply` ignore the target's own
committed `deploy.toml` `kits` list** and silently substitute gov's registry default (F2).

---

## 2. THE TABLE — every registry entry and every `tools/*/kit.toml`

`tools/govkit/registry.toml` declares 25 `[[entry]]` rows. Thirteen `tools/*/kit.toml` files exist and
every one is a descriptor for one of those rows; the other twelve descriptors live under
`tools/govkit/entries/`. There is no `kit.toml` that the registry does not claim and no entry whose
descriptor is missing — `selfcheck` asserts both and it is silent on that arm.

Columns:

- **DEPLOY** — does `apply` land bytes for it, and is that ever exercised by a gate?
  `apply@gate` = the entry is passed to `apply` somewhere in `selftest.py` or `matrix.py`.
- **UPDATE** — every entry shares one classification loop (`govkit.py:5124`, `for row in rows_all`
  over the RECEIPT), so no entry can receive a file gov newly ships. Per-entry variation is only in
  the roles, so the column records the role hazard.
- **WIRE** — what actually invokes it in the target after `apply`.
- **CHECK** — `[check].argv` (runs a probe) · `none` + reason (declared absence) · **ABSENT**.

| # | entry | descriptor | DEPLOY | UPDATE | WIRE | CHECK |
|---|---|---|---|---|---|---|
| 1 | `playbook` | `entries/playbook.kit.toml` | 1 `seed` rule → `{playbook_path}`. apply@gate ✔ (default set + matrix shape 5) | receipt-bound | nothing runs the charter; it IS `AGENTS.md`. 0 legs, 1 authoring hole | `none` + reason |
| 2 | `playbook-render` | `tools/playbook/kit.toml` | 3 `engine` rules incl. two `root_relative` pulls of `tools/govkit/{entries/playbook.kit.toml,registry.toml}`. apply@gate ✔ (matrix) | receipt-bound | 2 legs (`playbook render wiring`, `… selftest`) | `argv` ✔ |
| 3 | `kickoff-manifest` | `entries/kickoff-manifest.kit.toml` | 3 rules; the engine dir is an ORDER (a junction the operator makes). apply@gate ✔ | receipt-bound | 1 leg (ratchet) | `none` + reason |
| 4 | `memory-tree` | `tools/memory-tree/kit.toml` | 3/6 landable; 3 `rendered` produced by its own adopter. apply@gate ✔ | receipt-bound | 16 legs | `none` + reason |
| 5 | `codebase-map` | `tools/codebase-map/kit.toml` | 3/4 landable. apply@gate ✔ | receipt-bound | 3 legs; one is SILENCED against a fresh target (argv names `{gate_file}`) | `none` + reason |
| 6 | `memory-recall` | `tools/memory-recall/kit.toml` | 1/4 landable; 3 `forked`, 3 `project-owned` withheld. apply@gate ✔ | receipt-bound; `forked` rows never written by design | 2 legs + rendered Skill | `argv` ✔ |
| 7 | `run-gates` | `tools/run-gates/kit.toml` | 1/2 landable; `run-gates.gov.test.sh` withheld. apply@gate ✔ | receipt-bound | 6 legs, and it OWNS the manifest the others land in — **see F1** | `argv` ✔ |
| 8 | `drift-audit` | `tools/drift-audit/kit.toml` | 2/4 landable. apply@gate ✔ | receipt-bound | 3 legs + rendered Skill — **the Skill names a directory govkit never creates, F4** | `argv` ✔ |
| 9 | `agent-instructions` | `tools/agent-instructions/kit.toml` | 1 `engine` rule. **apply@gate ✘ — never named in either harness** | receipt-bound | 2 legs | `argv` ✔ |
| 10 | `unattended` | `tools/unattended/kit.toml` | 1/4 landable; 3 `rendered`. **apply@gate ✘** | receipt-bound | 3 legs; adopter exits 1 `no-project-layer` on a fresh target and all 3 rendered docs stay absent (`DEPL-aTetheredConvoy-9`) | `argv` ✔ |
| 11 | `pytest-parallel-guardrails` | `tools/pytest-parallel-guardrails/kit.toml` | 1/2 landable; 1 `merged` → BLOCK. apply@gate ✔ | receipt-bound | 1 leg | `none` + reason |
| 12 | `gate-lint` | `tools/gate-lint/kit.toml` | 1 `engine` rule. **apply@gate ✘ — `intake` only** | receipt-bound | **0 legs.** Declared: hole `gate-lint-leg-wiring`, undischargeable by construction | `none` + reason |
| 13 | `lexicon` | `tools/lexicon/kit.toml` | 2/3 landable. **apply@gate ✘** | receipt-bound | 3 legs + rendered Skill; `landed-but-inert` on a fresh target (3 authoring holes) | `argv` ✔ |
| 14 | `agent-cap` | `tools/hooks/kit.toml` | 7 `engine` rules, one source → two destinations. **apply@gate ✘** | receipt-bound | 2 legs; the `.claude/settings.json` entry that WIRES the hook is a `merged` rule with no writer | `none` + reason |
| 15 | `review-harness` | `tools/workflows/kit.toml` | 1/2 landable; lands at `{prefix}/review-harness/`, NOT `workflows/`. **apply@gate ✘ (`plan` only)** | receipt-bound | 7 legs; `memory/guides/REVIEW-PROTOCOL.md` is `rendered` with `adopt.argv = []`, so nothing renders it and `check-protocol-parity.test.sh` exits 1 in the target | `none` + reason |
| 16 | `settings-merge` | `entries/settings-merge.kit.toml` | 1/2 landable; the `merged` rule BLOCKs. apply@gate ✔ (merged-refusal arm) | receipt-bound | 1 leg | `none` + reason |
| 17 | `push-main` | `entries/push-main.kit.toml` | 2/3 landable; 1 `merged` → BLOCK. apply@gate ✔ | receipt-bound | 2 legs + `.githooks/` | `none` + reason |
| 18 | `check-wiring` | `entries/check-wiring.kit.toml` | 1 `engine` rule. apply@gate ✔ (the harness workhorse, 27 uses) | receipt-bound | 1 leg (self-test) + SessionStart | `none` + reason |
| 19 | `check-kit-versions` | `entries/check-kit-versions.kit.toml` | 1 `seed` rule. **apply@gate ✘** | receipt-bound | 1 leg; hole `kit-versions-need-list` UNDISCHARGED on arrival by design | `none` + reason |
| 20 | `check-testsuite-counts` | `entries/check-testsuite-counts.kit.toml` | 1 `engine` rule. **apply@gate ✘** | receipt-bound | 2 legs; the repo-subject leg guards on the literal `tools/gate-legs.json` (dropped at emit, so the leg runs unguarded) | **ABSENT — F5** |
| 21 | `check-agent-cap-restatement` | `entries/check-agent-cap-restatement.kit.toml` | conditional; 1/2 landable. **apply@gate ✘** | receipt-bound | 2 legs | `none` + reason |
| 22 | `check-install-prefix` | `entries/check-install-prefix.kit.toml` | conditional; 1/3 landable. **apply@gate ✘ (`plan` only)** | receipt-bound | 2 legs | `none` + reason |
| 23 | `check-placeholders` | `entries/check-placeholders.kit.toml` | conditional; 1 `engine` rule. **apply@gate ✘** | receipt-bound | 2 legs | `none` + reason |
| 24 | `check-line-length` | `entries/check-line-length.kit.toml` | conditional; 1 `engine` rule. apply@gate ✔ (matrix shape 5) | receipt-bound | 2 legs | `none` + reason |
| 25 | `check-microformats` | `entries/check-microformats.kit.toml` | conditional; 1 `engine` rule. apply@gate ✔ (matrix shape 5) | receipt-bound | 2 legs | `none` + reason |

**apply@gate ✘ count: 11 of 25** — `agent-instructions`, `unattended`, `gate-lint`, `lexicon`,
`agent-cap`, `review-harness`, `check-kit-versions`, `check-testsuite-counts`,
`check-agent-cap-restatement`, `check-install-prefix`, `check-placeholders`. Eight of those eleven are
not named at all anywhere in `selftest.py` or `matrix.py`.

Live install evidence for the whole table: a `--all` install into a fresh repo lands 165 files across
20 kits (5 entries are `selectable = "conditional"` and `--all` excludes them), leaves 19 orders in
`.governance/outbox/`, and finishes with 7 problems.

---

## 3. FINDINGS

### F1 — `apply` silently withholds the target's whole gate-leg manifest whenever the run has any problem, and the receipt records the withheld legs as emitted · **BLOCKER**

`tools/govkit/govkit.py:4401`

```python
        if not r.problems:
            rf.parent.mkdir(parents=True, exist_ok=True)
            rf.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n", ...)
            print(f"govkit apply — gate legs: emitted {len(emitted)} into {gr['file']}")
```

`r.problems` is the report's GLOBAL list (`govkit.py:804-823`), accumulated from every step of the
run. The LEGS step is step 9 of 11; CONFIGURE (step 6) and OBSERVE (step 7) both call `r.fail`. So a
single kit whose adopter legitimately cannot complete suppresses the manifest write for every OTHER
kit in the same install — and `emitted` is still written into the receipt unconditionally at
`govkit.py:4507`.

The comment directly above the loop, at `govkit.py:4305-4308`, describes exactly this failure and
believes it was fixed:

> THE FINDINGS ARE HELD AND RAISED AFTER THE WRITE-BACK, which is guarded by `if not r.problems:`
> below. Calling `r.fail` inside the loop suppressed the manifest write for EVERY leg, so one
> defective leg silently took the healthy ones with it — the install "stood" while the target's
> runner stayed empty.

Deferring the *leg* findings past the write-back does not help, because the guard still reads every
finding raised *before* the step.

**Controlled A/B, run today.** Two identical fixtures, each a fresh repo with a trivial
`kind = "manifest"` gate runner and a seeded empty `tools/gate-legs.json`:

| fixture | `--kits` | exit | printed | manifest on disk | receipt `gate_runner.emitted` |
|---|---|---|---|---|---|
| `C:/fx-clean` | `check-wiring` | 0 | `gate legs: emitted 1 into tools/gate-legs.json` | **1 leg** | 1 |
| `C:/fx-dirty` | `check-wiring,unattended` | 1 | `[9/LEGS] manifest` and nothing more | **0 legs** | **4** |

The four problems in the dirty run are, verbatim:

```
govkit: kit 'unattended': its adopter exited 1 — no-project-layer
govkit: '.claude/skills/unattended/SKILL.md' is declared `rendered` by kit 'unattended' and is absent after its adopter ran …
govkit: 'memory/guides/UNATTENDED-PROTOCOL.md' is declared `rendered` by kit 'unattended' and is absent after its adopter ran …
govkit: 'memory/guides/PLAYBOOK-TEMPLATE.md' is declared `rendered` by kit 'unattended' and is absent after its adopter ran …
```

None of them is about a leg. All four are the *designed* outcome of installing `unattended` into a
repo that has no project layer yet. `check-wiring self-test` — proved emittable one row above — is
recorded in the dirty receipt as emitted and is not in the target's manifest.

The same thing happens on the realistic full install: the `--all` run into a fresh repo printed
`[9/LEGS] manifest`, wrote **no** `tools/gate-legs.json` anywhere in the target (`find` returns
nothing), and recorded **57** emitted legs in `.governance/install.json`. Zero legs installed, 57
claimed.

This is the class the same function refuses one branch up — *"emitting it would record coverage in
the receipt for a leg that cannot run"* (`govkit.py:4302`). Here the receipt records coverage for 57
legs that were not even written.

**Fix.** Snapshot `len(r.problems)` at the top of the LEGS step and guard on problems raised *since*
that point; print an explicit withheld line when the guard fires; and do not put `emitted` into the
receipt for a manifest that was not written.

---

### F2 — `plan` and `apply` ignore the target's committed `deploy.toml` `kits` list and silently substitute gov's registry default · **HIGH**

`tools/govkit/govkit.py:434-440` (`resolve_selection`, the default branch)

```python
    dk = default_kits(reg)            # registry.toml [selection] default
    ...
    return derive_install_order(sorted(dk), descs)
```

`deploy.get("kits")` is read in exactly one verb — `cmd_adopt`, at `govkit.py:6232`:

```python
    selection = resolve_selection(reg, descs, "kits" if deploy.get("kits") else "default",
                                  list(deploy.get("kits") or []))
```

`cmd_plan` (`:2349`) and `_cmd_apply` (`:3731`) both pass the mode straight from argv, so with no
`--kits` they take the registry default and never look at the target's own declaration. Three verbs,
two answers to "which kits does this target want".

**Reproduced on a fresh target:**

```
$ python tools/govkit/govkit.py intake --target C:/gkt-sel --kits check-wiring
govkit intake — wrote C:/gkt-sel/.governance/deploy.toml for 1 kit(s) …
$ grep '^kits' C:/gkt-sel/.governance/deploy.toml
kits = ["check-wiring"]
$ python tools/govkit/govkit.py plan --target C:/gkt-sel
govkit plan — target C:/gkt-sel · selection: kickoff-manifest, memory-tree, playbook, run-gates, codebase-map, memory-recall
```

Six kits the operator did not choose; the one they did choose is not among them. `plan` previews the
wrong set too, so the preview cannot reveal it — the Skill's own instruction to read `plan` before
applying ("the last cheap moment to notice a destination you did not expect") is defeated.

**It is on the documented path.** `skills/deploy-governance/SKILL.md:39` and `:54` prescribe exactly
`plan --target <path>` and `apply --target <path>` with no `--kits`, and `:36` says of the descriptor
"Commit that file. It is the thing that makes the next `apply` reproducible."

**And it is not merely wrong, it is fatal for a non-default selection.** On the same fixture, `apply`
with no `--kits` refuses at exit 2:

```
govkit: entry 'kickoff-manifest' declares an lf_pin whose pattern needs answer 'user_skills' —
a literal brace written into somebody's .gitattributes matches nothing, forever
```

`intake` never asked for `user_skills`, because `kickoff-manifest` was never selected. The documented
three-command sequence therefore dies for any target whose selection is not gov's default six.

The receipt compounds it: `govkit.py:4503` writes `"kits": selection`, so the receipt records the
substituted default and `update`'s `claimed` set (`:5081`) inherits it.

**Fix.** In the default branch of `resolve_selection`, prefer `deploy["kits"]` when the target
declares one, exactly as `cmd_adopt` already does; fall back to the registry default only when it
does not.

---

### F3 — the per-entry deployability leg was never built, the spec that required it is CLOSED, and `matrix.py` scopes itself on the premise that it exists · **HIGH**

`tools/govkit/matrix.py:5-7`

```
deployability leg grades every registry ENTRY. This grades the repo shapes the contract names,
and it CITES those two rather than re-asserting what they already assert: plan-equals-apply and
apply-twice stay with the deployability leg, and the per-mechanism arms stay in the selftest.
```

`memory/builds/aTetheredConvoy/spec/2026-08-16-spec-DEPL-aTetheredConvoy-3.md` is **Status: CLOSED ·
rev-4**, and its AC7 (`:281`) requires `bash tools/govkit/deployability.test.sh` to drive `intake` →
`plan` → `apply` → `apply` for **every registry entry**, with AC8 asserting plan-equals-apply and
idempotency over the same population. F1 of that spec (`:319`) explicitly resolved that the leg does
NOT fold into the matrix.

Measured:

- `git ls-files | grep -i deployab` → **no output**. The file has never existed (`git log --all
  --diff-filter=A -- '*deployability*'` is empty).
- No leg in `tools/gate-legs.json` runs it.
- `lands_nothing`, the declared key AC7 rests on, appears in **no descriptor** in the tree.
- `matrix.py:48` therefore narrows itself to four entries — `SCRATCH_KITS = ["playbook",
  "playbook-render", "check-microformats", "check-line-length"]` — on the written ground that a
  different leg covers the rest.

Union of entries any gate ever passes to `apply`: 14. **Eleven entries are never driven through
`apply` by anything on the bar** (list in §2). Eight of the eleven are not mentioned anywhere in
either harness. Every one of them therefore ships on the strength of `selfcheck`'s *declaration*
arms, which grade the descriptor and never the install.

The section's own cost paragraph (`:157`) argued the leg was affordable because it is guarded and
concurrent. That argument is still true; the leg is still absent.

**Fix.** Either build the leg, or amend `matrix.py`'s docstring and widen `SCRATCH_KITS` — the
current state is a citation to a gate that does not exist, which is strictly worse than an
acknowledged gap.

---

### F4 — the drift-audit Skill an adopter receives names `tools/workflows/…`, a directory govkit never creates · **HIGH**

`tools/drift-audit/adopt-drift-audit.sh:108`

```bash
  */*) WORKFLOWS_REL="${KIT_REL%/*}/workflows" ;;   # prefixed install: sibling of this kit
```

The two deep-tier workflow scripts are landed by the `review-harness` entry
(`tools/workflows/kit.toml`, `include = "**"`, no `to`), and govkit's default destination is
`{kit}/…` where `kit = f"{prefix}/{eid}"` (`govkit.py:790`) — the **entry id**, not the source
directory's basename. So they land at `{prefix}/review-harness/`.

Measured in a `--all` install into a fresh repo:

```
$ find <target> -name 'drift-audit-*.js'
<target>/tools/review-harness/drift-audit-code.js
<target>/tools/review-harness/drift-audit-state.js
$ sed -n '73,74p' <target>/.claude/skills/drift-audit/SKILL.md
tools/workflows/drift-audit-code.js     # dead · unwired · duplication · inefficiency · instruments
tools/workflows/drift-audit-state.js    # records · charter · work-state · record-gate integrity
```

The rendered Skill instructs an agent to run two files that do not exist, in an install where the
files WERE landed under a different directory. This is correct by coincidence in gov only, because
gov's own source dir happens to be `tools/workflows/`.

The comment immediately above the defect, `adopt-drift-audit.sh:101-106`, records that this exact
class was already measured once and "fixed":

> Measured: the template hardcoded `workflows/`, so at this repo's own `tools/` prefix the rendered
> Skill instructed an agent to run two files that do not exist — and `--check` reported "in sync",
> because it diffs the render against the template and BOTH carried the same wrong spelling.

The fix parameterised the *prefix* and left the *directory name* hardcoded, so the same defect
survives one level down — and the same `--check` blindness survives with it, for the same reason.

Supporting: `tools/workflows/kit.toml:8` states `why_two_ids = "… The drift-audit workflow scripts
travel with the drift-audit entry."` That is false. `tools/drift-audit/kit.toml` has `home =
"tools/drift-audit"` and no rule naming either file; they travel with `review-harness`. The same
split is why `govkit selfcheck` reports `tools/check-kit-versions.sh` asserting constants in
`tools/workflows/drift-audit-{code,state}.js` "that no registry entry claims" — those two version
constants sit outside the registry's version model entirely.

**Fix.** Derive the sibling directory from the `review-harness` entry's own resolved destination (or
make it an `[answers]` key), and make `adopt-drift-audit.sh --check` assert the rendered paths EXIST
rather than only that the render matches the template.

---

### F5 — `check-testsuite-counts.kit.toml` declares no `[check]` at all; the rule that forbids that is enforced only against a target, never by `selfcheck` · **MEDIUM**

`tools/govkit/entries/check-testsuite-counts.kit.toml` — the file has `[adopt]`, two `[[gate_leg]]`
blocks and a `version_from = { none = … }`, and **no `[check]` table**.

The rule exists, at `govkit.py:2455-2458`:

```python
    if r is not None:
        r.fail(f"kit '{eid}' declares neither `[check].argv` nor `[check] = {{ none = \"…\" }}`, "
               f"so nothing measured it and nothing said why — declare the absence with a "
               f"reason; silence is not a third option")
```

That call site is `run_kit_check`, reached from `cmd_check` — i.e. only when someone points govkit at
an installed target. `selfcheck` carries the *identical* rule for the sibling key, at
`govkit.py:1000-1002` ("`version_from = { none = "<reason>" }`; silence is not a third option"), and
carries no equivalent arm for `[check]`.

Measured:

```
$ python tools/govkit/govkit.py selfcheck ; echo $?
… 0                     # green, no mention
$ python tools/govkit/govkit.py check --target <installed target> ; echo $?
govkit check — check-testsuite-counts: landed-unmeasured
govkit: kit 'check-testsuite-counts' declares neither `[check].argv` nor `[check] = { none = "…" }`,
  so nothing measured it and nothing said why — declare the absence with a reason; silence is not
  a third option
… 1
```

So a descriptor gov authored and ships is defective by gov's own written rule, gov's bar is green, and
the first person to be told is an adopter — whose `govkit check` exits 1 over a problem they cannot
fix in their own tree.

**Fix.** Add the reason (or an argv) to the descriptor, and lift the assertion into `selfcheck` so gov
grades its own descriptors on the same terms as an adopter's.

---

### F6 — `TOOL-dClosedLexicon-15` is OPEN and its recorded description is now false · **LOW**

`memory/backlog/TOOL.md:113` reads:

> the `playbook` entry declares both files `project-owned`, which is not landable, while its own
> `why_no_adopter` says "installation is a copy to an owner-chosen path" — so the DEFAULT selection
> installs no playbook.

Every measurable claim in that sentence is now wrong. `tools/govkit/entries/playbook.kit.toml:22-26`
declares ONE file (v3.0 converged the charter) at `role = "seed"`, which is landable
(`LANDABLE_ROLES = ("engine", "seed")`, `govkit.py:230`). The descriptor's own comment at `:17-21`
records the repair by name. Measured: a default-selection `apply` into a fresh repo writes the
charter, and `head -3 <target>/AGENTS.md` returns the rendered template.

The row should be CLOSED. Left OPEN it points a future session at a defect that no longer exists,
which in a governance repo is the same cost as a stale gate.

---

## 4. UPDATE, re-measured — `TOOL-aFlaggedScaffold-3` is still live at 093730e4

Not a new finding; the row is tracked and OPEN. It is re-stated here because it is half the owner's
question and because it was re-measured today rather than read.

Reproduction, end to end:

1. Cloned gov to `C:/gk2`, reset to `093730e4`.
2. `intake` + `apply --kits drift-audit` into a fresh `C:/gkt`. Receipt: 11 rows.
3. In `C:/gk2`, added `tools/drift-audit/newthing.py` and committed → `78eb14d7`. The file is inside
   `home = "tools/drift-audit"` and is matched by that entry's `include = "**"` engine rule, so it is
   unambiguously a file gov now ships for a kit the target claims.
4. `python tools/govkit/govkit.py update --target C:/gkt --to 78eb14d7`

Output: eight `current` rows, the "available (not installed)" list, and the tally
`current 9 · missing 1 · project-owned:skipped 1`. **`newthing.py` does not appear anywhere** — not as
a write, not as a report, not as a withheld row.

Cause is unchanged: `_cmd_update`'s classification loop is `for row in rows_all` at `govkit.py:5124`,
over `receipt.get("files", [])` (`:5094`). A descriptor source with no receipt row is not in the
iteration space, and there is no second pass that quantifies over the descriptors. Every mechanism
the verb has — rename detection, three-way carry, withdrawal orders — operates on rows that already
exist.

Practical shape of it: an adopter's kit can be missing a module gov added, `update --write` will
report the install clean, and the failure surfaces as an ImportError the next time the kit runs.

---

## 5. Commands run

```bash
python tools/govkit/govkit.py selfcheck
python tools/govkit/govkit.py                                   # USAGE / verb set
python tools/govkit/govkit.py intake --target <t> --all --answer gate_file=… --answer manifest_path=… \
                                     --answer playbook_path=AGENTS.md --answer user_skills=.claude/skills
python tools/govkit/govkit.py plan   --target <t> --all
python tools/govkit/govkit.py apply  --target <t> --all
python tools/govkit/govkit.py check  --target <t>
python tools/govkit/govkit.py intake --target C:/gkt-sel --kits check-wiring
python tools/govkit/govkit.py plan   --target C:/gkt-sel        # F2
python tools/govkit/govkit.py apply  --target C:/fx-clean --kits check-wiring          # F1 arm A
python tools/govkit/govkit.py apply  --target C:/fx-dirty --kits check-wiring,unattended  # F1 arm B
python tools/govkit/govkit.py apply  --target C:/gkt --kits drift-audit                # §4
python tools/govkit/govkit.py update --target C:/gkt --to 78eb14d7                     # §4
python tools/govkit/check_runbook_parity.py
bash <target>/tools/review-harness/check-protocol-parity.test.sh
git ls-files | grep -i deployab
grep -rn "lands_nothing" .
```

Fixtures: `C:/gk2` (gov clone at `093730e4` + one synthetic commit), `C:/gkt`, `C:/gkt-sel`,
`C:/fx-clean`, `C:/fx-dirty`, and a `--all` target under the session scratchpad. Short paths were
required — cloning this repo into the scratchpad fails with `Filename too long` on
`memory/builds/*/reviews/*`, which is worth knowing before anyone else tries.

## 6. Looked at and NOT reported

- **Guards in `[[gate_leg]]` that name literal `tools/…` paths** (`tools/lexicon/kit.toml:70`,
  `entries/check-testsuite-counts.kit.toml:31`). `govkit.py:4307-4313` DROPS a guard matching no
  tracked path in the target, with a stated rationale, so the emitted leg runs unguarded rather than
  skipping forever. The class is already `TOOL-aPacedTurnstile-12`.
- **`check_runbook_parity.py` exists, is wired into no leg, and exits 1 naming 18 entries with no
  anchored runbook section.** Already `TOOL-dScaffoldedMirror-15` (DEFERRED), with the same figure.
- **`requires_config_first` / `[[files]].placeholders` / `[config].defaults` declared-and-unread.**
  Already wave-1 F5 and F6.
- **`merged` and `rendered` roles not landing; the two adopters that exit 1 on a fresh target.**
  Declared in `memory/map/features/govkit.md` §Gaps and tracked as `DEPL-aTetheredConvoy-9`.
- **`run_all_env` is a required `[gate_runner]` key that nothing consumes** — `GR_REQUIRED` at
  `govkit.py:2900` checks presence only, and `read_gate_verdicts` (`:3004`) documents running
  *without* the escape deliberately. Presence-only-by-design; not worth a row.
- **`intake` writing a literal `prefix = "tools"`** — `DEPL-dCarriedReceipt-3`.
- **The silenced `codebase-map coverage + freshness` leg on a fresh target** —
  `DEPL-dCarriedReceipt-6`.
