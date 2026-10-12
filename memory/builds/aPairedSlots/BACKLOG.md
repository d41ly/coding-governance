# aPairedSlots — asks

## Asks
- TOOL-aPairedSlots-10 · filed 2026-10-11 · the health log's trim is a tail-and-`mv` copy-and-replace in the `health_log_sh` block, inlined byte-identical in `tools/lib/health-log.sh`, `tools/run-gates/run-gates.sh`, `skills/session-kickoff/manifest-check.sh` and `tools/check-wiring.sh`, with a Python twin in `tools/lib/health_log.py`; with two bars admitted at once, a line a sibling appends between one bar's `tail` and its `mv` is lost, and two bars trimming at once can trim twice. Short appends were measured whole (4500 concurrent 100-byte lines on node a), so only the trim needs a guard: a `noclobber` lock beside the log and a re-read before the `mv`, in all four copies and the twin, under their parity gate. · accept two fixture writers appending to one `health.log` while a third trims it at its cap lose no line the cap keeps and leave no lock behind, observed against all four inlined copies and the Python twin
- TOOL-aPairedSlots-16 · filed 2026-10-12 · held red: suite push-main self-test red at 9b743831 on the daily held job, run 38133597959 · seen `{prefix}/push-main.test.sh`@9b743831 run `bash {prefix}/push-main.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPairedSlots-17 · filed 2026-10-12 · held red: suite pre-push self-test red at 9b743831 on the daily held job, run 38133597959 · seen `.githooks/pre-push.test.sh`@9b743831 run `bash .githooks/pre-push.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPairedSlots-18 · filed 2026-10-12 · held red: suite memory-hygiene self-test red at 9b743831 on the daily held job, run 38133597959 · seen `{prefix}/memory-tree/check-memory-hygiene.test.sh`@9b743831 run `bash {prefix}/memory-tree/check-memory-hygiene.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPairedSlots-19 · filed 2026-10-12 · held red: suite unattended driver selftest shard 5/8 red at 9b743831 on the daily held job, run 38133597959 · seen `.github/workflows/remote-ci.yml`@9b743831 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPairedSlots-20 · filed 2026-10-12 · held red: suite unattended driver selftest shard 7/8 red at 9b743831 on the daily held job, run 38133597959 · seen `.github/workflows/remote-ci.yml`@9b743831 · accept the suite is green on the daily held job at the default branch's tip

## Dispositions
- SEV · TOOL-aPairedSlots-10 · LOW · a trim runs once per 250 health events, its window is one `tail` and one `mv`, and a lost line is a diagnostic event, never a verdict
- KEEP · TOOL-aPairedSlots-10 · the block is a shared contract across four kits and a Python twin; changing it is its own cross-kit unit, out of the turnstile change this build lands
- SEV · TOOL-aPairedSlots-16 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPairedSlots-16 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPairedSlots-17 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPairedSlots-17 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPairedSlots-18 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPairedSlots-18 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPairedSlots-19 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPairedSlots-19 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPairedSlots-20 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPairedSlots-20 · filed by an unattended run for the owning build; outside this build's goal
