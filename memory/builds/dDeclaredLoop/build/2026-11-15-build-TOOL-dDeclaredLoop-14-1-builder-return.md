**Serves:** journal TOOL-dDeclaredLoop-14

# Builder return — TOOL-dDeclaredLoop-14, dispatch 1: the verb_refused name would raise the lexicon offender pin

## Why

DIVERGENCE: the spec names a function whose name would add a new naming-lexicon offender, and that offender count may not rise. Section 2 S3 and section 4 Inventory call the new driver function `verb_refused` in tools/unattended/unattended.sh. The suggest command, `python tools/lexicon/lexicon.py --suggest verb_refused --as sh.function`, says the leading token `verb` is not in the declared verb table: "Declared verbs: add arm build check cmd derive extract init load main measure parse print read remove render resolve run scan seed set test write". `--list` shows that the existing `verb_*` driver functions (`verb_propose`, `verb_brief` and 17 more) are already counted as UNRULED P1 verb offenders. So `verb_refused` would take the count from the pin `VERB_OFFENDER_PIN="1209"` in .lexicon.conf to 1210, and the section 7 lexicon gate would turn red at the close. Section 5 lists no such risk. To fix it, sections 2 S3 and 4 Inventory have to name the function with a declared verb, for example `write_refusal`, which `--suggest` accepts for sh.function. The verb flag stays `--refused`. Two other gaps the spec writer may want to fix in the same revision (neither is a red on its own): (1) Section 4's `derive_frontier(items, witnessed, step)` cannot produce entries carrying a unit and an instance key as its data model says. The key needs the unit id and HEAD (`derive_instance_key(tag, unit_id, inputs or [head])` in position.py as built), so the signature should also take the unit and the head. `witnessed` should be stated as the held tags mapped to their inputs. (2) The `frontier-none` case ("every item of the step witnessed") cannot come out of a position the engine derives from the shipped definition. The build's step is, by construction, the step whose unit-forward item the least-advanced unit has not passed (for step.build that is `item.build.acceptance`, a unit-forward item whose witness is the unit at `built` or later), so that item is always unwitnessed. Section 4's fixture table should say the plant narrows that step's items in its in-memory definition, as unit 7's `deadlock` plant edits needs.

## Summary

I stopped before writing anything, so there is no commit. While checking what the change could newly turn red, I found the spec's `verb_refused` name would add a naming-lexicon offender over its pin of 1209. Details are in `why`. Nothing in the tree changed and no patch file was needed. `--dispatch` and `--brief` were not run, because both write to the run-state file. The four untracked prompt files under memory/builds/dDeclaredLoop/prompts/ (units 47 and 84) belong to other units and were left alone.

Checks that ran, all read-only, none a gate:
- The lexicon's suggest verb over `verb_refused` and over the planned Python and shell names (`derive_frontier`, `check_refusal`, `write_refusal` and others). Every name passed except `verb_refused`. The lexicon's `--list` confirmed the existing `verb_*` functions are counted offenders. Together these stand in for the `lexicon naming predicates` leg.
- Python probes of the shipped loop definition's step.build and step.test items and of the unit transition rows. These grounded the A/B/C/D plant tags as `item.build.base`, `item.build.unit-lease`, `item.build.unit-pass` and `item.test.merge`, and showed the `frontier-none` gap.
- Reads of the code the spec relies on, all of which hold as built: `derive_next_item`, `PLANTS` and `main` in tools/loop/position.py; `park`, `verb_propose`, `verb_plan`, `resolve_position_engine`, `VERB_REQUIRES`, `VERBS_SLUG` and the argument loop in unattended.sh; check 26 and check 27 in check-unattended.sh; `read_run_state` and `PARK_KINDS` in tools/runlog/model.py; `_RUN_PARK_KINDS` in tools/drift-audit/drift_report.py.
- Counts at base: `grep -c '"refusal"'` over drift_report.py prints 0, and `grep -c 'unattended.sh --refused '` over the Skill render prints 0. The Skill render measures 10524 bytes CR-stripped, equal to its row.

For the rebuild after the spec is revised, the suite needs three things the spec does not list:
- A parity-table row for `--refused`, because every verb needs one.
- `refused` added to the hostile-value matrix, because its header placeholder `<text>` puts it in that population.
- The newline and bypass-flag guards written as `case` patterns rather than `printf | wc -l` or `printf | grep`, so the change adds no new var-pipe spawn site.

Owed at the close, unchanged from section 7: both `New arm:` RED-first observations (position.py frontier plants; unattended.test.sh `--refused` arms), the core meta-check for AC8, and the bar.
