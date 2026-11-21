# TOOL-dWitnessedBar-81 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-81

No merge bar, no self-test suite and no gate leg ran in this pass, and no code changed. The criteria
were probed on node d, 2026-11-21, `uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9
`x86_64-pc-cygwin`, through one scratch probe that sources the suite's own lines,
`tools/run-gates/run-gates.gov.test.sh#check_cr_reached` through `check_key_variant`, and the arm's
liveness loop from its `rgf_seen=` line to its `done`, over a `rgf_fn` cut of
`.githooks/pre-push#read_green_file` and a hand-built record laid out as the AC12 arm's:
`verdict<TAB>GREEN<CR>`, two `sha` lines the second CR-ended, `reused_cache` 1 then 0`<CR>`, a CR-ended
`fingerprint`. The record `run_local_plant` builds, the scratch clones and the arm's exit are the main
loop's at the close, and so are the records S3 and S4 write, as the spec's Rollout and each criterion's
permission line place them. This probe is not the clone run (DERIVED from the builder's probe).

**Evidences:** TOOL-dWitnessedBar-81
- AC1 — `check_cr_reached` — over the suite's functions as built the loop printed no line, `fail` 0, `rgf_seen` ` rec_sha rec_fp`. Over a copy whose `check_cr_reached` count reads `-ge 0`, one `diff` line from the suite, its tail test kept, it printed `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the length variant passed a value one byte short)` and the same line for `rec_fp`, no line holding `tail variant`, `fail` 1, `rgf_seen` empty. Over a copy whose `check_cr_reached` keeps `-eq 41` and holds no last-byte test, one `diff` line, it printed `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the tail variant passed a value whose last byte is not CR)` and the same line for `rec_fp`, no line holding `length variant`, `fail` 1, `rgf_seen` empty. The two runs in scratch clones under `%TEMP%/<short-name>` are OWED to the main loop at the close (DERIVED from the builder's probe).
- AC2 — `TOOL-dWitnessedBar-81` — OWED to the main loop at the close: S3's two records beside AC2 in `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-74-1-acceptance-ledger.md`, each one physical line carrying its clone run's printed `rec_sha` line, the line it did not print, its `uname -s` and this unit's id, with S3's statement of the rev-2 `-ge 0` break and the unrestaged `true` break. This pass wrote neither, so the probe above is not that record.
- AC3 — `rec_fp` — OWED to the main loop at the close: S4's same two records beside AC2 in `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-76-1-acceptance-ledger.md`, each with its clone run's printed `rec_fp` line, its `uname -s` and this unit's id.
