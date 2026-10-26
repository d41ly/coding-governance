**Serves:** research TOOL-dGroundRules-66

# Spec brief — TOOL-dGroundRules-66, `--dispatch` skips a terminal unit's keys

## The prompt

> The build run adopted a blocker discovery (`--rescope --act add`, RUN.md): `--dispatch`'s sibling loop in `tools/unattended/unattended.sh` (`verb_dispatch`, the `sibrows` derivation around line 13863) asks `check_pass_open` about EVERY key of EVERY unit, terminal or not. TOOL-dGroundRules-19 is CLOSED, yet its keys `729e5128` (`tools/policy/guard.py help/policy.md`) and `d88f7ddd` (`.governance/policy.json`) can never close: `pass_commit` takes the FIRST `Pass: TOOL-dGroundRules-19` commit after each anchor, that commit is `31aa43f9b`, and it wrote only the unit's ledger. So check 49 refused TOOL-dGroundRules-7 twice (the mirror paired with its generator `tools/policy/policy.py`) and refuses every later unit declaring `policy.py`, `guard.py`, `help/policy.md` or the mirror. `--audit` (around line 8490) already skips a unit whose spec is `CLOSED` or `WONTDO`, resolving status through `load_spec_facts`.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-24-spec-TOOL-dGroundRules-66.md`: `--dispatch`'s sibling set leaves out every key of a unit whose spec is terminal (`CLOSED` or `WONTDO`), resolved the way `--audit` resolves it, so one predicate answers both verbs. Add its row to the build README's authored roster table. Author only: no product code, no commit, no gate.

### Items
1. One mechanism: the sibling-set derivation in `verb_dispatch` skips terminal units' keys, reusing `--audit`'s status read (`load_spec_facts`, `SPEC_PATH`, `SPEC_ST`), ideally hoisted so both verbs call one function (the two-answers class). `--check-commit`'s open-pass rows (around line 13505) and the gate leg's openness reader (around line 13869) are read and either share the rule or are named as deliberately unchanged, with the reason.
2. The code comment beside `--audit`'s skip that calls the conservative answer "right for `--dispatch`" is revised, since a terminal unit cannot write (the scratch guard refuses a closed unit's product writes) and so reserves nothing a live pass could collide with.
3. Acceptance: a fixture run where a CLOSED unit holds a never-closing key on a generated file and a live unit declares that file's generator, refused before and admitted after; the same with the unit's spec flipped back to `INPROGRESS`, still refused; and this build's own state, `--dispatch dGroundRules --pass TOOL-dGroundRules-7` with unit 7's write set, admitted. Each criterion names a probe or fixture, never the bar or a suite; the suite arm goes on a `New arm:` line.
4. Status header: `DEFERRED` is wrong for a unit this run builds; use the status the spec format gives a unit specced in the build run, Tier-2, `order 3` (it precedes TOOL-dGroundRules-7 at order 4), `streams tooling`. Carry the binding line the chain's other run-added units carry (`**Derived:** PLAY-dClosedLoop-2`), and run `python tools/check-spec-tokens.py --list` for the §7 leg line.
5. If `memory/HYGIENE.md` "Deviation records" requires one for a unit added to a chain build, author it in this build's `build/` folder.

### Acceptance
The spec holds every section the format requires; the README roster row exists; every §6 code span sits on one line; `python tools/check-spec-tokens.py` is the main loop's to run.

### Gates
No gate runs in this pass beyond the role's own.

### Non-goals
Changing `pass_commit`'s first-commit rule or check 23's grading; editing RUN.md rows; any other spec.

### Limitations
The fix touches the unattended kit's driver, which is a grader: the close owns every red the kit's legs print at the tip.

### Reuse
`--audit`'s terminal skip in the same file is the seam; `check_pass_open` stays the one openness predicate.
