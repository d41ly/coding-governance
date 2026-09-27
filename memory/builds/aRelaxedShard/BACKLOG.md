# aRelaxedShard — asks

## Asks

- TOOL-aRelaxedShard-2 · filed 2026-08-17 · check 6's build-README class (25,600 B, `cl=0`) has NO byte-axis arm: `tRunOk/README.md` and `tRunBig/README.md` are front-matter stubs and nothing sizes one past the cap, so a class whose only bound is bytes is unarmed. Found regrounding TOOL-aRelaxedShard-1
- TOOL-aRelaxedShard-3 · filed 2026-08-17 · by deletion (TOOL-dSpentCeiling-1) · the complaint was that a byte budget over a file whose length tracks OPEN-BUILD COUNT measures parallelism. It did, and the budget is gone rather than corrected: `memory/LIVE.md` is still generated and still tracks that count, but nothing sums it any more. Measured while closing: over the seven days to 2026-08-25 `LIVE.md` SHRANK 303 B while the read path grew 43460 B, so the parallelism term was real but was never the driver — two kit-rendered guides supplied 64.9% of that growth

## Dispositions

- CLOSED · TOOL-aRelaxedShard-3 · by TOOL-dSpentCeiling-1 · by deletion (TOOL-dSpentCeiling-1) · the complaint was that a byte budget over a file whose length tracks OPEN-BUILD COUNT measures parallelism. It did, and the budget is gone rather than corrected: `memory/LIVE.md` is still generated and still tracks that count, but nothing sums it any more. Measured while closing: over the seven days to 2026-08-25 `LIVE.md` SHRANK 303 B while the read path grew 43460 B, so the parallelism term was real but was never the driver — two kit-rendered guides supplied 64.9% of that growth
