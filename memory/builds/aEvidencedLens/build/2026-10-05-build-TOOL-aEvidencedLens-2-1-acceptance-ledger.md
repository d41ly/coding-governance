# TOOL-aEvidencedLens-2 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-2

Spec lenses probe read-only, and every spec finding carries evidence. The sources: the pass commit
`bcd020ac2`, whose body records a scratch stub run of the render, 28 assertions over AC1 to AC8 with 12
of them RED against the pass-start render, and the AC11 figures; the main loop's VERIFYING run of the
tier2-review self-test in a frozen clone at `0c8dd1761`, which printed `---- 239 passed, 1 failed ----`,
the one FAIL being the rubric arm, an extractor defect fixed in `5a1643c8d`, whose re-run printed
`---- 240 passed, 0 failed ----`; the unattended-build self-test of the same clone, rc 0 and
`PASS (610 assertions)`; and greps and direct checks re-run on the tree at `5a1643c8d`. The direct
comparison is `ledger-cmp.js`, the scratch `runReview` driver described in this build's
`TOOL-aEvidencedLens-1` ledger, over `git show bcd020ac2~1:` of `tools/workflows/tier2-review.js`,
blob `5d674842`, and `git show bcd020ac2:` of it, blob `9d8733a9`.

**Evidences:** TOOL-aEvidencedLens-2
- AC1 — `PROBE POLICY` — the VERIFYING run printed `ok` for `the probe policy sits once under LENS: in every spec find: prompt, naming the scratch, the bound, the DURABILITY exception and --selftest, and not in synth`. The `verify:` placement is `TOOL-aEvidencedLens-3`'s and is read in its ledger.
- AC2 — `result.key` — `ledger-cmp.js` unmasked over the pass-start and pass renders: `resume:probe` 1/1, `find:` 5/5, `verify:` 5/5 and `synth` 1/1 byte-identical in both arg sets, round 1 with `checklist` and `specs` and round 2 with `priorFindings`, and the keys EQUAL, `…-6380ce0a` and `…-62ba7747`. `grep -c "PROBE POLICY"` over the pass-start render printed 0, so a prompt identical to it carries none.
- AC3 — `scratch` — the VERIFYING run printed `ok` for every `spec scratch:` prelude arm the criterion names: absent, relative, multi-line, equal to repo, repo with a trailing slash, under repo, and under repo by case and backslash each refused with a message opening `tier2-review:`; an absolute path outside repo, the sibling `/tmp/rs`, and a Windows path proceed, the last resolved to `C:/t/s`; and a diff review never reads it. The prelude arms evaluate the extracted prelude, so no agent can be traced. That the `PROBE POLICY` line carries `C:/t/s` is the separate arm `a Windows scratch reaches the PROBE POLICY line folded to C:/t/s`, also `ok`.
- AC4 — `evidence` — the VERIFYING run printed `ok` for `the spec finding schema requires evidence and its return line names it; the diff schema and prompts carry neither`.
- AC5 — `nothing outside the diff` — at `5a1643c8d`, over `tools/workflows/tier2-review.template.js`: `grep -c "nothing outside the spec set"` printed 0, `nothing outside the diff` 1, and `its evidence may come from anywhere` 1.
- AC6 — `PROBE_RULES` — the VERIFYING run printed `ok` for `the review key moves with a PROBE_RULES edit and not with scratch`.
- AC7 — `name:` — the VERIFYING run printed `ok` for the header arm, which reads all 15 fields read off the a alias as `name:` keys, `scratch` among them.
- AC8 — `MT_ARGS` — at `5a1643c8d`, `grep -c '"scratch":'` over `tools/workflows/unattended-build.test.sh` printed 30 and `grep -c "scratch: '/tmp/s'"` over `tools/workflows/tier2-review.test.sh` printed 2. The VERIFYING unattended-build run printed `ok` for `MT the callee ran over the measured shape — 48 raw, 13 confirmed`, which a THROW from the callee would have redded.
- AC9 — `hands its lenses` — at `5a1643c8d`, over `memory/map/features/review-harnesses.md`: `grep -c "hands its lenses"` printed 1 and `and the drift-audit siblings still tell their agents nothing` printed 0.
- AC10 — `--print-cap` — at `5a1643c8d`, `--print-cap` printed 5, the template with `{{FANOUT_CAP}}` replaced by 5 compared byte-identical to `tools/workflows/tier2-review.js` by `cmp`, and `bash tools/check-install-prefix.sh --offenders` exited 0 and printed nothing.
- AC11 — `spec scratch:` — the pass commit records `grep -c "spec scratch:"` at 0 before and 12 after, 11 arms plus the floor comment, and `FLOOR_ASSERTIONS` 182 to 197, 11 prelude arms and 4 whole-script assertions. The VERIFYING run printed `ok` for all 17 `spec scratch:` lines, the six `TOOL-aEvidencedLens-21` added included; at `5a1643c8d` the grep prints 18.
