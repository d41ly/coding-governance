# Tier-2 Review — Cumulative Diff Landing on main

- **Date:** 2026-07-12
- **Scope:** `a9e8744..04dc139` — manifest-ratchet spec + Units A–E (manifest-check gate C1–C6/C5s, 38-scenario suite, manifest template v1.1, engine Step 2b read-repair, playbook v2.2, wire docs)
- **Findings:** 0 blockers · 0 high · 0 medium · 3 low
- **Verdict:** Ship. Nothing gates the merge. All three findings are hardening items on the new ratchet surface: one trust-boundary tightening in the kickoff engine, one false-red bound in C5, one silently-vacuous test scenario. Each is small, localized, and has a clear fix.

All findings below survived skeptic review; the C5 cap was empirically reproduced in a throwaway repo (N=9 decoys → green, N=10 → false red).

---

## Blockers

None.

## High

None.

## Low

### L1 — Step 2b auto-executes a repo-chosen script before the user confirmation gate

- **File:** `skills/session-kickoff/SKILL.md:91` (Step 2b, lines 89–93)
- **Category:** security / trust boundary

Step 2b resolves the checker from the manifest's `check-script:` value — falling back to
`scripts/manifest-check.sh`, then the kit-shipped copy — "and RUN it", with no constraint that the
path is git-tracked, inside the repo, or the known-good kit script. Resolution and execution happen
during kickoff, **before** Step 5's "say go" gate. The skill explicitly targets "ANY project",
including fresh clones.

**Impact:** Running `/session-kickoff` on an untrusted repo escalates from "read the manifest" to
"execute whatever the manifest names". A hostile or compromised manifest picks the executable; the
only mitigation is the harness bash permission prompt, which users routinely allowlist for bash in
their own repos. Prompt-injection-shaped: repo-authored data selects an auto-executed binary.

**Fix:** Constrain resolution in Step 2b, and mirror the constraint in `manifest-ratchet-spec.md`
section 4: accept `check-script:` only if it is a git-tracked path inside the repo whose basename is
`manifest-check.sh`; otherwise fall back to the kit-shipped copy beside the skill, and **surface**
(not execute) any non-conforming `check-script:` value in one clause so the operator can vet it.

**Left-shift gate:** Add a skill-lint rule to the kit's self-check (or the fold-review harness) that
flags any SKILL.md instruction pairing an execute directive ("RUN it", "execute", "invoke") with a
path resolved from repo-authored data (manifest fields, config values) unless the same sentence
states a tracked-path/basename/allowlist constraint. Companion: a suite scenario asserting a
manifest with `check-script:` pointing outside the repo (or at a non-`manifest-check.sh` basename)
is reported, not run.

---

### L2 — C5 stamp search caps candidates at `head -10`, enabling a decoy-induced false red

- **File:** `skills/session-kickoff/manifest-check.sh:191`
- **Category:** correctness / spec conformance (fails closed — no laundering path)

C5's stamp-commit search truncates the `git log -G'^last-audit:' "$LA_SHA..HEAD"` candidate pool at
`head -10`. Column-0 `last-audit:`-shaped lines in *other* files (vendored MANIFEST-TEMPLATE.md
copies, doc examples) match `-G'^last-audit:'`; each such decoy commit is correctly validated away
(`cur == prev`) but still consumes a candidate slot. With 10+ decoy commits after the true re-stamp
S, the cap truncates the list before S is reached, S stays empty, and C5 false-reds.

**Impact:** A repo with a legitimate re-stamp at/after the newest watch commit still fails check 5
whenever 10+ newer decoy candidates precede it — a wrong red on the standing gate that the operator
can only clear by re-stamping again, eroding trust in the ratchet. Spec §3 C5 has no cap: green iff
S non-empty and W ancestor of S; its only documented residual is the pre-rename decoy case.
Empirically reproduced: N=9 decoys → exit 0; N=10 → `check 5 FAILED`, exit 1.

**Fix:** Drop the `head -10` (or raise it substantially, e.g. 200). The `while` loop already breaks
at the first validated candidate, so the cap only bounds pathological decoy chains; if cost bounding
is wanted, bound on *validated* hits (loop counter after the `cur != prev` test), not by truncating
the raw candidate pool.

**Left-shift gate:** Boundary-test every truncation: adopt a suite convention (police it in the §10
sweep) that any `head -N` / `--max-count=N` in `manifest-check.sh` must have a scenario exercising
N+1 items on the far side of the cut — here, a scenario 29-style repo with a true re-stamp followed
by 15 decoy commits, asserting exit 0. That scenario written first would have caught this before
Unit A landed.

---

### L3 — Scenario 29 silently degenerates to a duplicate of scenario 10 on python3-only machines

- **File:** `skills/session-kickoff/manifest-check.test.sh:313`
- **Category:** test coverage / green-by-absence (spec §7)

Scenario 29 (block-reorder-after-drift → C5 red) shells out to bare `python` — the suite's only
Python use — to swap the `last-audit:` and `watch:` lines. The suite runs under `set -u` only (no
errexit), so on machines without a `python` shim (python3-only distros, Windows without Python) the
heredoc fails with 127 and execution continues: the reorder never lands, the follow-up `commit_all`
(line 321) no-ops with its exit unchecked, and HEAD stays at the line-312 "unaudited drift" commit —
state-identical to scenario 10. The run assertion (exit 1 + `check 5 FAILED`) passes on that state
regardless, so the scenario prints ok and the suite exits 0.

**Impact:** Green-by-absence, exactly the failure mode spec §7 names and the §10 sweep polices: the
block-reorder regression coverage — one of the structural-C5 guarantees the spec calls out — is
vacuously absent on those machines. A future regression in `blockstamp`'s order-independence ships
undetected there.

**Fix:** Two parts. (1) Resolve the interpreter — `PY=$(command -v python3 || command -v python)` —
or eliminate the dependency with a two-line awk/sed swap. (2) Make the scenario fail hard if the
mutation didn't land: assert `git -C "$R" status --porcelain` is non-empty before `commit_all`,
mirroring scenario 35's commit-count guard, so a silent no-op becomes a loud failure rather than a
duplicate scenario.

**Left-shift gate:** Preamble dependency check: have the suite assert every external command it uses
(`command -v` loop over a declared list) and hard-fail — not skip — when one is missing, so
environment gaps surface as red, never as vacuous green. Companion CI gate: run the suite once in a
python3-only container (or with `python` shimmed to `exit 127`) so interpreter-name drift is caught
on every push. Generalize scenario 35's guard into a `commit_all_strict` helper for any scenario
whose assertion depends on a prior mutation having landed.

---

## Cross-cutting observation

L2 and L3 share a root pattern with the kit's own spec vocabulary: the suite's strongest guarantees
(§7 anti-green-by-absence, §10 sweep) police *scenario presence*, not *scenario potency*. Both fixes
above push toward potency checks — boundary tests at every cap, and hard assertions that each
scenario's setup mutation actually landed. Folding those two conventions into the §10 sweep
definition would close this class rather than these two instances.
