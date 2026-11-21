# KICK-dKeptSession-19 — acceptance ledger

**Serves:** journal KICK-dKeptSession-19

No merge bar, no self-test suite and no gate leg ran in this pass. The `policy check`, `policy
fixtures`, `lexicon naming predicates`, `memory hygiene`, `spec tokens` and the other legs the
spec's section 7 names were not run as commands. The criteria were observed on win32 at the pass's
base `2bf35aa1` by probes of the unit's own code: `policy.py lists --write` and `lists --check` run as
commands in the policy kit; the two new case functions, `run_reader_join("reader-join")` and
`run_reader_join("reader-join-blank")`, and `run_arm` called in process from `check_policy`; a
differential probe running the base's `policy.py` and this pass's over the same planted
`build_legacy_repo` and `build_repo` copies; and the `grep` commands the criteria spell. Each new
name was passed by `lexicon.py --suggest --as py.function`, the three helpers the spec's inventory
does not list, `load_design_lib`, `check_design_blank` and `render_join_design`, included.

Owed to the close: every leg the spec's section 7 names; the `policy fixtures` run of `reader-join`,
`reader-join-blank`, `list-grew`, `summary-new-key`, `legacy-homes`, `legacy-homes-main-dropped`,
`legacy-homes-present`, `arms-empty-declared`, `arms-empty-target` and `adopter-fresh-target`, whose
"Each arm in an adopter" join now holds an `arm_reader_join` row; the fixture's guard trace over the
new case's reads of the memory-tree kit's `design_lib.py` and `tree_lib.py`, both under the leg's
guard; and the RED-first observation of the `New arm:` line, the `reader-join` case's planted row,
naming clause and grown list and `reader-join-blank`'s blank conf, in `tools/policy/check_policy.py`.

**Evidences:** KICK-dKeptSession-19
- AC1 — `python policy.py lists --write` then `python policy.py lists --check` — in the policy kit
  of gov's tree, the write printed `wrote unnamed-keys.txt · drained 0: none`; the check exited 0,
  `policy lists: green · 0 finding(s)`, printing `policy lists: unnamed-keys.txt · no comparison:
  tools/policy/unnamed-keys.txt is absent at c2a407b0390f (merge-base of HEAD and origin/main), and
  absent is never an empty list`. `grep -vc "^#" unnamed-keys.txt` printed 48, the count
  `derive_unnamed_keys` gave in process: 48 of 273 catalogue keys over the view's 509 rows (DERIVED at 2bf35aa1).
- AC2 — `reader-join` — over `build_repo`'s copy, a design naming the catalogue's first row on its
  owner's row and the list seeded by `write_shrink_list` and committed as the base: unplanted, no
  finding, `base 589d06e41706 (upstream/main tip) carried 272, the list carries 272`; the planted
  `dKeptSession` row, `zz.planted: unnamed and not listed`; a clause naming the listed
  `charter.override` on its owner's row, `charter.override: stale: drain it with `lists --write``;
  put back, no finding. 5 checks, 0 wrong.
- AC3 — `reader-join` — the planted row with its name added to the list copy, `zz.planted: added to
  a shrink-only list above the base 589d06e41706`.
- AC4 — `grep -n "read_shrink_base(\|write_shrink_file(" policy.py` — six lines: the two
  definitions, and the calls in `check_shrink_list`, `write_shrink_list`, `read_base_pairs` and
  `write_legacy_homes`. `grep -c '"show", f"{base}' policy.py` printed 1, `grep -c "_HEADER + "
  policy.py` printed 0.
- AC5 — the differential probe — the base's and this pass's `policy.py` over the same planted
  copies, 20 comparisons, 0 different: `lists --check` and `lists --write` of `build_legacy_repo`'s
  copy for each of the eight `legacy-homes` cases and the `legacy-homes-main-dropped` branch, exit
  code, every output line but the new `unnamed-keys.txt` line, and the bytes of every list after
  the verb equal; `check_list` and `write_list` over `build_repo`'s copy unplanted, under
  `seed_summary_new_key` and under `seed_list_grew`, findings, note, drained names and list bytes
  equal. That copy holds no memory-tree kit, and its `lists --check` printed `policy lists:
  unnamed-keys.txt · not graded · no memory-tree kit holding design_lib.py in this install: …`, exit
  0. `derive_withheld_names` over this kit read `legacy-homes.txt`, `unscanned-readers.txt` and
  `unnamed-keys.txt`.
- AC6 — `reader-join-blank` — `check_policy.py --repo` over a scratch repository whose conf leaves
  the four keys blank printed `policy-check: arm_reader_join · not graded · every DESIGN_* key is
  blank (DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW, DESIGN_NODES), so nothing was read`, no
  finding under it. In process, `run_arm` over a conf setting `DESIGN_RECORD` alone answered `1
  finding(s) · the design was not read`, the finding naming the three blank keys; over gov's tree
  `0 finding(s) · 225 of 273 catalogue key(s) named on their owner's row · 48 listed · no comparison:
  …`.
- AC7 — `grep -n "unnamed-keys" policy.md` — in `help/`, lines 112, 114 and 118 of the bullet
  "See which keys no build has picked up", line 114 saying a key leaves `unnamed-keys.txt` by its
  owner build's deviation moving a naming clause onto its row, drained by `lists --write`.
