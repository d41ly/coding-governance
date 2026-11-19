**Serves:** research TOOL-dTrackedAtlas-1

# dTrackedAtlas — the run branch's history rewrite, old sha to new

On the owner's word of 2026-11-19 ("Rewrite the branch to drop the four Red-fix trailers"), `git filter-branch
--msg-filter` over `6547d032..ba99b007de81` removed the `Red-fix:` lines of `f24d90e25`, `97da019cf`, `68794ff8d` and
`2e5147a2e`, whose spec edits the inline lane's limit L3 refuses. No tree changed: `git diff` between the old tip
`ba99b007de81` and the new `459463ad46f2` is empty. Every commit from the first of the four onward took a new sha.

The run record, the red-fix records, the review records and the ledgers now name the new shas. The specs, which are
CLOSED and frozen, and the hash-sealed handoff prompts keep the old ones; this table resolves them. The red-fix records
of the four commits are deleted with their trailers, since each joined a trailer that no longer exists.

| Old | New | Subject |
|---|---|---|
| `f24d90e25823` | `8d69e97b77e1` | fix(dTrackedAtlas): unit 1's pass-leg reds — the specs pin their figures, `predecessors` t |
| `d9bbd1d4c058` | `a47c438bb1f7` | records(dTrackedAtlas): unit 1's three red-fix records, and unit 2's build brief and dispa |
| `a587c887a29c` | `5651f783b3b8` | build(dTrackedAtlas): TOOL-dTrackedAtlas-2 — the Atlas renders the actual state of each ch |
| `397a7528860f` | `4de3be6429f3` | fix(dTrackedAtlas): TOOL-dTrackedAtlas-2 — the ledger's code spans stay on one line each |
| `97da019cf0cf` | `7f98e9d33f4a` | fix(dTrackedAtlas): unit 2's brief stops exposing a figure through a wrapped code span, an |
| `2f929deaf223` | `87f222053486` | records(dTrackedAtlas): unit 2's red-fix record, and unit 3's build brief and dispatch |
| `8529cce8b70c` | `c6801669e305` | spec(dTrackedAtlas): TOOL-dTrackedAtlas-3 and -4 rev-3 — every new function name leads wit |
| `f1b02b3eb093` | `d0743a938cb6` | records(dTrackedAtlas): unit 3's redispatch at rev-3 |
| `3a7e9ef2cdd7` | `cffbd91e0999` | build(dTrackedAtlas): TOOL-dTrackedAtlas-3 — the page carries the commit and input digest  |
| `68794ff8d66e` | `870be1b18449` | fix(dTrackedAtlas): unit 3's pass-leg reds — the nested refusal helper takes a declared ve |
| `40e06fdbec9b` | `0dc483dea811` | records(dTrackedAtlas): unit 3's red-fix records, and unit 4's build brief and dispatch |
| `eabe8f9ff727` | `dff9e0193a1c` | spec(dTrackedAtlas): TOOL-dTrackedAtlas-4 rev-4 — AC6 plants a break that runs |
| `03a1f8f71f38` | `4d83d5b6e773` | records(dTrackedAtlas): unit 4's redispatch at rev-4 |
| `d8aaf6bffd09` | `99848a5db7d4` | records(dTrackedAtlas): unit 4 carried forward against TOOL-dTrackedAtlas-7, and the build |
| `2e5147a2ef43` | `b1de0d961f58` | fix(dTrackedAtlas): TOOL-dTrackedAtlas-4 rev-6 pins the two figures rev-5 added |
| `18af33dafb40` | `5f2d3da6f8f4` | records(dTrackedAtlas): unit 4's red-fix record, and phase REVIEWING |
| `2b57a776e689` | `81cfc29dcd26` | records(dTrackedAtlas): closing review round 1 — CLEAN WITH FIXES, its three HIGH items an |
| `1b5c0a628997` | `c8bfb3502b2e` | spec(dTrackedAtlas): TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL- |
| `5c2d5b5af190` | `8a79a8297fc2` | fix(dTrackedAtlas): the round-1 review record's line citations pinned at the reviewed tip, |
| `03dd18cec85c` | `801ace581b22` | records(dTrackedAtlas): the round-1 red-fix records, the promoted units' build briefs, and |
| `0a11f912f9a4` | `8237debbc6ba` | build(dTrackedAtlas): TOOL-dTrackedAtlas-8 — the fork scan quotes every value it writes in |
| `a899e9657605` | `cb9f7431cac5` | records(dTrackedAtlas): unit 9's dispatch |
| `d036dcb92679` | `e1c8b2ddfcf4` | build(dTrackedAtlas): TOOL-dTrackedAtlas-9 — a landing counts only on the default branch's |
| `bc4fb14f092e` | `ffcceea599b4` | records(dTrackedAtlas): unit 9 closes, and unit 10's dispatch |
| `4391b1451678` | `c8b3322f6e12` | build(dTrackedAtlas): TOOL-dTrackedAtlas-10 — the page's staleness digest covers the merge |
| `6b38e374d7ef` | `2a9ddae08594` | records(dTrackedAtlas): unit 10 closes, and unit 11's dispatch |
| `72a958aada71` | `c8c089b07746` | build(dTrackedAtlas): TOOL-dTrackedAtlas-11 — one reader for the Atlas's valued options, a |
| `e818d4faf8f3` | `0faa800880c5` | records(dTrackedAtlas): the browser-pane observations M1 owed — unit 2's AC12 and unit 3's |
| `812bd05192c4` | `62fcd9a10d8b` | records(dTrackedAtlas): phase REVIEWING for closing-review round 2 |
| `d23a030c993e` | `da435e9a63df` | records(dTrackedAtlas): closing review round 2 CONVERGED — its minors promoted to unit 12 |
| `ea7c36fc9e94` | `f1af61f09153` | spec(dTrackedAtlas): TOOL-dTrackedAtlas-12 |
| `3b741f6ad35d` | `bbde190491cc` | fix(dTrackedAtlas): the round-2 review record's line citations pinned at the reviewed tip, |
| `b3f60b96355e` | `c6c533e643cf` | records(dTrackedAtlas): unit 12's red-fix records, brief and dispatch |
| `2118c04ac4c9` | `2d8acb04e93b` | build(dTrackedAtlas): TOOL-dTrackedAtlas-12 — one stamp-rules table for writer and reader, |
| `3f298cfaba83` | `46fc33374d67` | records(dTrackedAtlas): unit 12's S5 — the pane observations re-recorded beneath their owe |
| `87ca8e38bafb` | `9e663d410258` | records(dTrackedAtlas): phase VERIFYING |
| `18a8aedf1e84` | `04f5885cfe83` | records(dTrackedAtlas): the keepalive reaped and both attestations written |
| `04f5491e179a` | `23c8a147dfc6` | merge: dTrackedAtlas — land onto origin/main at 9e21ac76 |
| `8f583a198b98` | `d32987e8d016` | records(dTrackedAtlas): the close's asks kept, and the eight CLOSED units declared records |
| `15c462a7dd7a` | `934f4d5937f0` | records(dTrackedAtlas): the routed-commits lane red parked for the owner |
| `c942b173d3b6` | `561e43f1e171` | records(dTrackedAtlas): handed off HELD under owner-decision — the routed-commits lane red |
| `ba99b007de81` | `459463ad46f2` | records(dTrackedAtlas): resumed on the owner's word — rewrite, re-pin, unit 4's row, land |
