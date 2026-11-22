# KICK-dKeptSession-9 — acceptance ledger

**Serves:** journal KICK-dKeptSession-9

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `7f53e589` by probes under the host temp directory: one builds the runlog arm's own
fixture through `selftest.py`'s builders, without running any arm, and runs `python
tools/runlog/runlog.py extract --orient` over it once per committed policy file; one builds the
`orient-calls` census plant under `warn`, `refuse` and `zero` through `check_policy.py`'s own
`run_cap_mode`, the function the case calls, without running the case. `python tools/lexicon/lexicon.py`
exited 1 on its verb-offender pin, 1432 offenders over a pin of 1421 (DERIVED, that run), the count
KICK-dKeptSession-30 read at its base; no line it printed names a file this pass touched, and
`--suggest` graded every new function name OK as `py.function`.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose new case and floor
are below; `check_policy.py --fixture budgets-cap-orient-calls` and `--fixture fixtures-guard-census`
themselves; and both `New arm:` lines' RED-first observations, the runlog case staged against the base
extract, which has no `--orient` mode, and the census case staged against a census with no
`orient-calls` row.

## Decisions taken in the build

- `run_kit_verb(home, anchor, args, repo)` in the extractor is the one place a sibling kit's verb runs,
  found through the inline `resolve_kit_dir` block: the report's policy reads, its budgets reads and
  the steps verb all go through it. With it come three private helpers, the git call, the move read
  and the first timed record, and the constant `ORIENT_ACTIONS`, the three classes S2 names.
- The context window is derived once per model per run, so each row's share is the one
  `derive_context_fill(ev)` takes under the default root, without re-scanning the host's transcripts
  per row; KICK-dKeptSession-46 passes the report's own root.
- A session both attributions name reads `driver`. An agent file's row takes its session's stage.
- `calls`, `tokens` and `context` count what precedes the action event in the extract's order, so the
  usage of the request that emitted the action is not counted.
- The stage lines and the under-floor line print under every `orient.budget` value; only the value's
  own warning differs.
- A `transitions.record` read the policy reader refuses is one NOTE and every stage `none`, never a
  default channel set, as the loop kit reads its own channels.
- The census plant sets `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, so its run reads no host transcript.

**Evidences:** KICK-dKeptSession-9
- AC1 — under `preset = "strict"` the report printed one `orient row` per file of the fixture's sessions, 30 rows over 29 sessions, the agent file's row with `source=agent-orient`; a 3-call session's row read `action=edit calls=3 tokens=180033 context=30%`, and the session with no edit read `action=none calls=5`, its two reads after the third call counted (DERIVED, that probe).
- AC2 — under the default channel set the first design session's row read `stage=step.design` and the first build session's `stage=step.build`; under `transitions.record = ["log"]` both read the same; under `["micro-format"]` every row read `stage=none` under one NOTE naming `transitions.record` (DERIVED, that probe).
- AC3 — the strict file's header read `orient.budget=warn-at-evidence-ceiling`, the design stage line ended `ceiling p90=3` over its 22 rows, and one `orient WARN` printed, the 40-call row's, `calls 40 past the evidence ceiling 3 (p90 of n=22)` (DERIVED, that probe).
- AC4 — under `preset = "standard"` the header read `orient.budget=record-only`, every row printed, no `orient WARN` printed, exit 0 (DERIVED, that probe).
- AC5 — with `orient.budget = "owner-ceiling"` and `budgets.orient-calls = 30` one `orient WARN` printed, `calls 40 past the owner ceiling 30`, followed by the budgets kit's `BUDGET WARN — orient-calls` line, exit 0; with no `budgets.orient-calls` one NOTE named it and no line held `WARN`; under `preset = "strict"` beside the cap the row printed `orient REFUSED` and the kit's `BUDGET REFUSE` line, exit 1 (DERIVED, that probe).
- AC6 — the build stage printed `orient — no ceiling · step.build · n=6 under 20` and none of its rows warned; over an empty projects dir the report printed `runlog: orient DEAD PROBE` and exited 2 (DERIVED, that probe).
- AC7 — `grep -n -- "--orient" tools/runlog/README.md` printed three lines: the mode's row in the command list, and the first and last lines of its paragraph, which follows the `--ready` paragraph and lists the three values, `record-only`, `warn-at-evidence-ceiling` and `owner-ceiling`, one bullet each (DERIVED, that probe).
- AC8 — `python tools/loop/loop_lib.py --steps` printed five tab-separated lines, `step.plan` and `planning` first and `step.deploy` and `deploying` last, exit 0; at the base it printed the usage line and exited 2 (DERIVED, that probe).
- AC9 — the plant built through `run_cap_mode` exited 0 printing `BUDGET WARN — orient-calls` under `warn`, exited 1 printing `budgets.enforce is refuse` under `refuse`, and exited 0 under `zero` with neither mark nor `BUDGET WARN`; `check-spec-tokens.py --legs-for -` over the runlog kit's `runlog.py` and `prose.py` named `policy fixtures` for each (DERIVED, that probe). The two cases themselves are the close's.
- AC10 — `grep -n -- "--steps" help/loop.md` printed the new bullet in "How to use it", and the page's `loop_lib.py` usage anchor carries `d50887a1`, the fingerprint `python tools/govkit/docs_leg.py --fingerprints` printed for that row after `--steps` joined its flags (DERIVED, that probe).
- `ASSERTION_FLOOR` rises from 1595 to 1612: the new case's 14 checks and its 3 decoy checks (PINNED, the count its `RAISED` comment prices).
