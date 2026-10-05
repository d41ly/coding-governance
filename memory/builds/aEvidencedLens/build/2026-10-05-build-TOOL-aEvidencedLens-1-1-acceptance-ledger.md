# TOOL-aEvidencedLens-1 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-1

Five spec-audit lenses, with the harness as the catalogue's one source. The sources: the pass commit
`c49655e6a`, whose body states the AC10 figures and that the pass verified by a scratch stub run of the
render rather than the suite; the main loop's VERIFYING run of the tier2-review self-test in a frozen
clone at `0c8dd1761`, which printed `---- 239 passed, 1 failed ----`, the one FAIL being the rubric arm,
an extractor defect fixed in `5a1643c8d`, whose re-run printed `---- 240 passed, 0 failed ----`; the
unattended-build self-test of the same clone, rc 0 and `PASS (610 assertions)`; and greps and direct
checks re-run on the tree at `5a1643c8d`. The direct comparison is `ledger-cmp.js`, a scratch driver
outside the tree in the `runReview` AsyncFunction shape of `tools/workflows/tier2-review.test.sh` with
all-returning stubs, run over two diff-kind arg sets (round 1 with `checklist` and `specs`, round 2 with
`priorFindings`). Its renders are `git show c49655e6a~1:` of `tools/workflows/tier2-review.js`, blob
`54cf03a3`, and `git show c49655e6a:` of it, blob `5d674842`.

**Evidences:** TOOL-aEvidencedLens-1
- AC1 — `find:coherence` — the VERIFYING run printed `ok` for `spec catalogue: the spec lens set is coherence grounding reuse blast-radius failure-envelope`, reading `find:coherence find:grounding find:reuse find:blast-radius find:failure-envelope` in that order, and `ok` for the shared-brief arm's `spec run, 10 prompts`, five `find:` and five `verify:` with one finding per lens.
- AC2 — `reuse_lookup.py` — no suite arm reads the brief text lens by lens. `grep -cF` over the render at `5a1643c8d` counted each marker the criterion names at least once: cannot FAIL 1, cannot PASS 1, MSYS 2, CRLF 2, reuse_lookup.py 1, query.py 1, --asks --json --all 1, THE BAR 1, gate-legs.json 1, version carriers 1, INSTANCE 1, section 4.3 1. That is a file-level count; the placement on each prompt's `LENS:` line was observed only inside the pass's stub run.
- AC3 — `lensNotes` — the VERIFYING run printed `ok` for `a malformed lensNotes refuses before any agent spawns: spec catalogue: the retired spec key on a spec audit` and for its control, `a spec-kind key on a spec audit, proceeds`. The arm label does not show the message text; its naming of the five keys was observed only inside the pass.
- AC4 — `lenses5-r2` — `grep -c "const REVIEW_SHAPE = 'lenses5-r2'"` over the template printed 1 at `5a1643c8d`. `ledger-cmp.js` over the pass-start and pass renders returned different keys, `…-aada6477` against `…-6380ce0a` at round 1 and `…-30f26c60` against `…-62ba7747` at round 2, on diff-kind args; the shape constant is shared by both kinds, and the spec-arg key pair was observed only inside the pass. The VERIFYING arm `a lens file written under another review shape is dispatched: the rewrite took and the keys differ` printed `ok`.
- AC5 — `priorFindings` — `ledger-cmp.js --mask` over the same two renders: `find:` 5/5, `verify:` 5/5 and `synth` 1/1 byte-identical in both arg sets with each run's key masked. Unmasked, `find:` and `verify:` differ and `synth` stays identical, so every difference is the key. The `resume:probe` prompt, which the criterion does not name, differed under the mask too. `TOOL-aEvidencedLens-13`'s ledger AC1 reads the same `find:` and `verify:` identity cumulatively from BASE `028b5cac` to the render after `TOOL-aEvidencedLens-12`.
- AC6 — `COPIED from` — at `5a1643c8d`: `grep -c "COPIED from"` over the template printed 0, `keeps its four lenses` over `tools/workflows/README.md` 0, `failure-envelope` over it 1, and the template's meta `Find` detail reads `5 finder lenses on either kind`.
- AC7 — `--offenders` — `bash tools/check-install-prefix.sh --offenders` at `5a1643c8d` exited 0 and printed nothing, so no key names a file this unit touched. No source here holds the criterion's staged break.
- AC8 — `MT20_SHAPE` — the grep the criterion names printed 0 for `tools/workflows/tier2-review.test.sh` and 0 for `tools/workflows/unattended-build.test.sh` at `5a1643c8d`. The VERIFYING unattended-build run printed `ok` for `MT the callee ran over the measured shape — 48 raw, 13 confirmed` and `MT20 the callee ran over the measured shape — 46 raw, 16 confirmed, 30 refuted`.
- AC9 — `--print-cap` — `bash tools/workflows/check-verifier-fanout.sh --print-cap` printed 5, and the template with `{{FANOUT_CAP}}` replaced by 5 through `sed`, piped into `cmp` against `tools/workflows/tier2-review.js`, printed nothing, at `5a1643c8d`.
- AC10 — `spec catalogue:` — the pass commit records `grep -c "spec catalogue:"` at 0 before and 2 after, and `FLOOR_ASSERTIONS` 180 to 182, one assertion per new arm. The VERIFYING run printed `ok` for both `spec catalogue:` arms. At `5a1643c8d` the grep still prints 2 and the floor reads 240, every later unit's raise included.
