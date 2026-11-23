# KICK-dKeptSession-8 — acceptance ledger

**Serves:** journal KICK-dKeptSession-8

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `21745a994`.
AC1 to AC7 ran through the unit's own fixture CLI, `bash actions-free.fixture.sh --plant <case>` in the
hooks kit, one plant at a time, each building its own scratch repository under a short temp
directory; neither hooks suite was run. The new `check_free_line` rows of the scratch-guard suite,
29 (PINNED, the count of the criteria's calls), and the agent-cap suite's two rows for rule nine
were probed alone over that fixture output, copied into a scratch script, never by running the suite:
all held, and a doctored output line reds its row. AC8 to AC11 ran as the spec's own commands. Every
new function was graded OK by `python tools/lexicon/lexicon.py --suggest <name> --as js.function`, and
`python tools/lexicon/lexicon.py --offenders` names none of the unit's new definitions; the full
check exits 1 on verb offenders already over its pin at the base, none of them this unit's.

The spec predates KICK-dKeptSession-27, -24, -10, -25, -21, -6, -7, -35 and -42; none of them moved
what it cites. `tools/hooks/scratch-guard.js#checkItemBoundary`, the red-fix lane's read in
`tools/hooks/scratch-guard.js#checkRouted`, `tools/hooks/scratch-guard.js#COMMIT_SHAPED`,
`tools/hooks/agent-cap.js#main`, `tools/hooks/agent-cap.js#resolvePolicyHelper`, the catalogue row, the
presets, the mirror and the suite's `FLOOR_ASSERTIONS` pin of 401 (PINNED at base `21745a994`) all
read as section 4 and section 10 state them.

Owed to the close: every leg the spec's section 7 names, the scratch-guard and agent-cap suites whole,
the `policy fixtures` leg, and the two `New arm:` lines' RED-first observations: the scratch-guard
suite's `check_free_line` rows staged against the base hook, which admits a Bash write with no item in
flight, and the agent-cap suite's rows for rule nine staged against the base hook, which has none.

**Evidences:** KICK-dKeptSession-8
- AC1 — `probes-none` under the stub's `read-only-probes` with `item — none · at <HEAD sha8>`: `git status` exited 0 with an empty stderr; `echo x > f`, `git commit -m x`, `git push` and an `Edit` of `src/a.js` each exited 2, printing `actions.free (read-only-probes) refuses this Bash write`, `Bash commit`, `Bash push` and `Edit write`, each `— the card of tFix reads item — none.` and the remedy line (DERIVED, that run). Section 4's refusal spells the pointer `item — none`, so the line names `item — none` where AC1 writes `item none`; the log line alone spells `item none`.
- AC2 — `probes-item` wrote `item — item.build.base@TOOL-tFix-1#aaaa0001 · at <HEAD sha8>`: the four acts each exited 0 with an empty stderr under each of the three values, 12 calls (DERIVED, that run).
- AC3 — `reads-none` under `item-reads-only`: `git status` exited 2 printing `actions.free (item-reads-only) refuses this Bash read`; `python position.py tFix --boundary none` and `bash manifest-check.sh --card --boundary --build tFix --session tFixSession-1` each exited 0 with an empty stderr (DERIVED, that run).
- AC4 — `anything-none` under `recorded-anything`: `echo x > f` and `git status` each exited 0 with an empty stderr, and the fixture's `gov-free-actions.log` held exactly one line, `<iso> · tFixSession-1 · write · Bash · item none` (DERIVED, that run).
- AC5 — `spawn-none` piped an `Agent` payload to `agent-cap.js`: it exited 2 printing `BLOCKED by agent-cap: rule 9 (KICK-dKeptSession-8) refused this Agent call — actions.free (read-only-probes) refuses this Agent spawn — the card of tFix reads item — none.`; `spawn-item` exited 0 with an empty stderr (DERIVED, that run). Rule 6 found no role index and rule 7 read the stub's limit against the scratch settings, so both admitted before rule 9.
- AC6 — `no-pointers` exited 0 with an empty stderr; `no-route` and `other-owner` each exited 0 printing `scratch-guard: actions.free unarmed —`, naming `routes no build` and `card-owner tFixOther-2`; `throw`, a directory at the card file's path, exited 2 printing `the actions.free arm threw (EISDIR: …) and fails closed on a Bash.` (DERIVED, that run).
- AC7 — `no-helper` and `refusal` each exited 2 as `read-only-probes` does, each printing one NOTE: `NOTE — no policy kit resolves beside this hook, so actions.free reads read-only-probes`, and `NOTE — actions.free could not be read (policy refused: the fixture plants a refusal of actions.free), so it reads read-only-probes` (DERIVED, that run). `grep -c '\.readPolicy(' scratch-guard.js` in the hooks kit printed 1, the call inside `readPolicyValue` (DERIVED, that probe).
- AC8 — the catalogue probe in the policy kit printed `dKeptSession read-only-probes` and `node tools/policy/policy-mirror.js get actions.free` printed `read-only-probes`; `python tools/govkit/docs_leg.py --fingerprints` printed `policy:actions.free c5786fdc help/orientation-card.md`, the fingerprint the page's anchor carries (DERIVED, that probe, the same as the spec's PINNED reading); `grep -c 'policy:actions.free' memory/project/docs-undocumented.txt` printed 0 (DERIVED, that probe).
- AC9 — the spec's `node -e` over `buildGitShaped` printed `true:false false:true true:false` (DERIVED, that probe); a probe requiring a copy of the base hook found its `COMMIT_SHAPED` source equal to `buildGitShaped('commit')`'s (DERIVED, that probe).
- AC10 — the spec's `node -e` over `readItemPointer` printed `{"key":"item.build.base@TOOL-tFix-1#aaaa0001","at":"1a2b3c4d"} {"none":true,"at":"unborn"} {"malformed":"item — x y","at":null}`, and `grep -c 'unborn)' scratch-guard.js` printed 1 (DERIVED, that probe).
- AC11 — in the hooks kit `grep -c 'rules 6, 8 and 7'` printed 0 for `agent-cap.js`, `agent-cap.test.sh` and `README.md`, `grep -c 'rules 6, 8, 7 and 9' agent-cap.js` printed 3, and `The role-gate arm is the other` and `After rule 7 only` each counted 0; in the workflows kit `README.md` counted 0 for `rules 6, 8 and 7` (DERIVED, that probe).
- S11 — the ten scratch-guard plants ran one after another in 9.0 s and the two spawn plants in 0.9 s by direct CLI (DERIVED, that run); `scratch-guard self-test` reads 296, over its 282, and `agent-cap self-test` stays 590, each row's note naming the re-read; neither reading reaches its leg's ceiling of 490 or 1800 (PINNED, the leg manifest at base `21745a994`).
