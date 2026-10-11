# aPairedSlots — asks

## Asks
- TOOL-aPairedSlots-10 · filed 2026-10-11 · the health log's trim is a tail-and-`mv` copy-and-replace in the `health_log_sh` block, inlined byte-identical in `tools/lib/health-log.sh`, `tools/run-gates/run-gates.sh`, `skills/session-kickoff/manifest-check.sh` and `tools/check-wiring.sh`, with a Python twin in `tools/lib/health_log.py`; with two bars admitted at once, a line a sibling appends between one bar's `tail` and its `mv` is lost, and two bars trimming at once can trim twice. Short appends were measured whole (4500 concurrent 100-byte lines on node a), so only the trim needs a guard: a `noclobber` lock beside the log and a re-read before the `mv`, in all four copies and the twin, under their parity gate. · accept two fixture writers appending to one `health.log` while a third trims it at its cap lose no line the cap keeps and leave no lock behind, observed against all four inlined copies and the Python twin

## Dispositions
- SEV · TOOL-aPairedSlots-10 · LOW · a trim runs once per 250 health events, its window is one `tail` and one `mv`, and a lost line is a diagnostic event, never a verdict
- KEEP · TOOL-aPairedSlots-10 · the block is a shared contract across four kits and a Python twin; changing it is its own cross-kit unit, out of the turnstile change this build lands
