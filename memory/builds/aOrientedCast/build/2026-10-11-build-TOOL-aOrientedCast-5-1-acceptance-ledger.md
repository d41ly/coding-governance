# TOOL-aOrientedCast-5 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-5

Direct checks only; no gate, suite or bar ran in the pass. AC1, AC3 to AC6, AC8 to AC10 and AC13 ran
from one scratch driver, `t2roles.js`, which slices the suite's `run.js` prologue (through
`const buildLensFile`) and the new `roles:` block out of `tools/workflows/tier2-review.test.sh` and runs
them with `node`. Over the worktree's render it printed 78 `ok` and no FAIL, 28 of them `roles:` arms.
Over the base render, `git show 646d4a73:tools/workflows/tier2-review.js` saved to the scratchpad, 22 of
the 28 went red; the six that held are controls asserting a classic path does not move, and each went red
over a second staged render that applied the posture omission to any role, joined every key into the
print, priced the synthesis into `durable`, always wrote the Roles clause and refused an empty object.
Restored, all 28 passed again. AC7 ran the same driver in `--compare` mode, AC2 and AC11 ran the
protocol-parity script in `--render` and `--check` mode and the greps the criteria name. The close owes
the `tier2-review self-test` suite, whose executed count is checked against the raised floor of 301 only
by a whole-suite run, and the rest of the spec's section 7 list, which this pass ran only as the direct
checks below.

**Evidences:** TOOL-aOrientedCast-5
- AC1 — `{ skeptic: 'none' }` — `null`, `[]`, `'gov-skeptic'`, `{ finder: 'x' }`, `{ skeptic: '' }`, `{ skeptic: '1bad' }`, `{ skeptic: 'none' }`, `{ skeptic: 7 }` and `{ synthesis: 'a b' }` each threw a message opening with the harness name and then `roles` that named the key or the value, with an empty trace; `{}` and the full-role set ran to `complete`. A render with the two refusals disabled failed all nine refusal arms.
- AC2 — `workerType` — `grep -c "AGENT_TYPE_SHAPE.test("` printed 2 and `grep -c "{0,63}\$/"` printed 1 over the template; the protocol-parity `--check` exited 0 printing `agent-type shape — 4 literal(s) in 4 file(s) agree with the owner`, so the owner yields one literal from its `const AGENT_TYPE_SHAPE =` line now that the `workerType` refusal tests the constant.
- AC3 — `gov-diff-reviewer` — under the full-role set with no `workerType`, every `find:` spawn carried `gov-diff-reviewer`, every `verify:` spawn `gov-skeptic`, `synth` `gov-synthesizer` and `resume:probe` no type; over spec args the finders carried `gov-spec-reviewer`; `{ skeptic: 'gov-skeptic' }` alone left finders on `Plan` and `synth` untyped; `{ synthesis: 'gov-synthesizer' }` under `workerType: 'none'` typed the synthesis alone.
- AC4 — `Write no file` — under `{ diffFinder: 'gov-diff-reviewer' }` and `workerType: 'none'` all ten judge prompts carried `Write no file` and none `DURABILITY`, and with every `find:` dead the return read `durable: false` with a note that dispatches every finder and skeptic again; under `{ synthesis: 'gov-synthesizer' }` all ten carried `DURABILITY` and the dead-lens run returned `durable: true`.
- AC5 — `No speculation, no style nits` — under the full-role set no diff or spec `find:` prompt carried `You are the ` or `No speculation, no style nits`, no `verify:` prompt `You are an adversarial skeptic` or `try hard to REFUTE`; every diff finder kept `Review ONLY the diff named under SUBJECT above` and `Nothing outside the diff.`, every spec finder `For EACH subject listed under SUBJECT above` and `PROBE POLICY`, every skeptic `SEVERITY RUBRIC` and `WHEN YOU CANNOT ESTABLISH A FINDING`; with `{ skeptic: 'gov-skeptic' }` alone every finder kept `You are the `.
- AC6 — `result.key` — `roles` absent, `{}`, `{ synthesis: 'gov-synthesizer' }` and `{ specFinder: 'gov-spec-reviewer' }` returned one key; `{ skeptic: 'gov-skeptic' }` returned another, and two full-role runs differing only in `diffFinder` returned two.
- AC7 — `priorFindings` — `t2roles.js --compare` over diff round 1 with `checklist` and `specs`, diff round 2 with `priorFindings` and spec round 1, each under `workerType` absent, `'none'` and `'Plan'` and each with every agent returning, every lens dead and the synthesis dead, printed 27 `ok`: every label, prompt, `agentType` and the whole result, `result.key` included, equalled the base render's, and the logs matched once the three `role ` lines were set aside. A render whose unroled diff finder sentence was reworded failed 18 of the 27, every diff row.
- AC8 — `role find: Plan — workerType` — under `{ skeptic: 'gov-skeptic', specFinder: 'x' }` with no `workerType` the log held `role find: Plan — workerType`, `role verify: gov-skeptic — roles.skeptic`, a `role synthesis:` line naming `no roles.synthesis`, `role find: roles.specFinder is not read on a diff-review` and the `judges under a named type` line, and no line opening `worker type`; a classic run logged the three stage lines as well.
- AC9 — `Roles: finders` — under `{ synthesis: 'gov-synthesizer' }` the `synth` prompt held `Roles: finders` once, after `lens notes`; with `roles` absent it held no `Roles:`.
- AC10 — `roles:` — the suite's own header predicate, run by the slice over the render, printed `ok` for the args header documenting all 17 fields read off the alias as name keys, `roles` among them.
- AC11 — `{{FANOUT_CAP}}` — the template with `{{FANOUT_CAP}}` replaced by the 5 that `check-verifier-fanout.sh --print-cap` printed equalled `tools/workflows/tier2-review.js` byte for byte with carriage returns stripped, and `bash tools/check-install-prefix.sh --offenders` printed no key naming a file this unit touched.
- AC12 — `diffFinder` — `grep -c "harness-args tier2-review" tools/workflows/README.md` printed 1 where HEAD printed 0, the `roles` section's new bullet names `diffFinder`, `specFinder`, `skeptic` and `synthesis`, and `grep -c "under a role" memory/map/features/review-harnesses.md` printed 1 where HEAD printed 0.
- AC13 — `FLOOR_ASSERTIONS` — the slice passed over the new render and failed nine `roles:` arms over a render with the refusal disabled; `grep -c "roles:"` over the suite printed 33 where HEAD printed 0, and `FLOOR_ASSERTIONS` reads 301, 273 plus the 28 assertions the block adds, under a `RAISED 273 -> 301` comment counting them.
