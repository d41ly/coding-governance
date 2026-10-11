# aFrugalTurnstile — asks

## Asks
- TOOL-aFrugalTurnstile-18 · filed 2026-10-11 · a post-merge full bar enters the host turnstile through `run-gates.sh --hold` like any other bar, so on a busy host it holds the queue for a full bar's duration while every session's diff-scoped bar waits behind it; the queue has one class, first come first served · seen `tools/run-gates/post-merge.sh`@b5309d4a:12 · accept the turnstile serves a waiting interactive or landing bar before a queued post-merge bar, or a post-merge bar yields between legs, observed with two queued bars in a fixture

## Dispositions
- SEV · TOOL-aFrugalTurnstile-18 · LOW · only a host declaring `GATE_POST_MERGE=local` pays it, and gov declares none
- KEEP · TOOL-aFrugalTurnstile-18 · a scheduling class is a new turnstile contract and out of this run's scope
