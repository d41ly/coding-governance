# TOOL-dGroundRules-1 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-1

No merge bar, no gate leg and no self-test suite ran in this pass, the lexicon naming predicates
excepted, which the builder role is allowed and which read green at its pin. The two legs this unit
adds, `policy check` and `policy fixtures`, were observed by calling the same functions in process
with `python -c`, so the textual leg argv never ran; both legs, and each `New arm:` line's red-first
observation, are owed to the close. Scratch targets were made under the user temp directory and
removed.

**Evidences:** TOOL-dGroundRules-1
- AC1 — `arm_schema` — `check_policy.main(['--repo', '.'])` exited 0 and printed one line per arm:
  `arm_schema · 0 finding(s) · 4 key(s) of .governance/policy.toml against 267 row(s)`,
  `arm_shape · 0 finding(s) · 267 row(s), 19 set-valued, 10 never-empty` and `arm_summaries ·
  0 finding(s) · 263 of 267 row(s) unsummarised`, its base note reading the list absent at
  3c2b69be4652, which is no comparison. The leg's own run is the close's.
- AC2 — `git show 9bf3b4c91952d54f01be759082f7ae3e52cde160` — a probe parsed the design's table
  between `## [policies]` and `## [presets]` into 267 rows and the catalogue into 267, and printed
  `names equal in order: True` and `owners equal: True`, with the four S1 defaults `last-valid`,
  `warn`, `[]` and `6`.
- AC3 — `schema-empty-<name>` — the in-process `--fixture` run printed ten `schema-empty-<name>`
  cases, each `RED as planted` and `green unplanted`, against ten rows carrying `empty = "never"`.
- AC4 — `shape-no-empty` — `shape-no-empty` and `shape-unknown-field` each printed `RED as planted`,
  naming `charter.practices`, then `green unplanted`.
- AC5 — `summary-new-key` — `summary-new-key` and `usage-new-key` each printed `RED as planted`,
  naming `zz.planted` as not listed, then `green unplanted`.
- AC6 — `list-grew` — `list-grew` printed `RED as planted` naming `zz.planted` as added above the
  base, then `green unplanted`; on the `summary-new-key` copy the run printed `lists --write left the
  planted row out · lists --check still red`. The run ended `34 assertion(s) executed · 0 wrong`.
- AC7 — `lists --write` — a copy of the kit under the run's scratch gave `autonomy` a `summary` and a
  `usage`: `policy.py lists --check` exited 1 naming `autonomy` stale, `lists --write` printed
  `drained 1: autonomy` and the list went from 263 rows to 262 with that row the only difference,
  and `lists --check` then exited 0.
- AC8 — `python "tools/policy/policy.py" scaffold` — `tomllib` read the policy file's leaves as
  exactly `budgets.enforce`, `budgets.pinned`, `policy-file.on-invalid` and
  `runtime.agents-in-flight` at their catalogue defaults, and the file's bytes equalled the
  scaffold's output, both captured and redirected.
- AC9 — `--check --target <t>` — on a fresh `git init` under the user temp directory, `--scaffold`
  wrote the scaffold's bytes; run again over an edited file it printed `kept` and the file's sha1 was
  unchanged; `--check` exited 0, and after `runtime.agents-in-flight = 0` exited 1 naming
  `runtime.agents-in-flight: 0 is below the minimum 1`.
- AC10 — `usage-out-of-set` — `usage-out-of-set` printed `RED as planted`, naming `budgets.enforce`'s
  usage refused by its own row, then `green unplanted`.
- AC11 — `lists --check` — `grep -n "policy.md" help/README.md` found the link at line 7, and the
  page counts two lines for `governance/policy.toml`, two for `check_policy.py` and one for
  `lists --check`.
