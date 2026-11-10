# Brief — dPavedRoad: four mechanical refusals that cost dSafePassage its rework

**Serves:** research TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4

## The prompt

> Can we analyze this build for any refusals/problems that have been costing it time and agent runs/reruns and build quick fixes? There are many more build runs in this set and so far they've been progressing painfully slow due to various mechanical obstacles.

## The brief

### Goal
Remove the four mechanical refusals that cost dSafePassage the most agent round trips, measured from its own transcript, so later build runs stop paying for them.

### Items
1. **TOOL-dPavedRoad-1 — writers self-check spec tokens.** `tools/check-spec-tokens.py --spec <path>` grades that one spec as if it were live, whatever its status, and `tools/roles/house/policy.toml` adds the spec-tokens leg to `gov-spec-writer`'s gates. About 17 of dSafePassage's 37 corrections to agents were "fix spec-token hits" that a writer could not see, because the role may not run the checker and the checker grades no DEFERRED spec.
2. **TOOL-dPavedRoad-2 — format-guard prints the lines it wants.** `tools/hooks/format-guard.js`'s block message includes, verbatim, the `agent`/`returned` lines `handoff.py agents` derives for each agent it names, and the `committed` line for each new commit it names. About 33 turn ends were refused for those lines, each costing a re-send.
3. **TOOL-dPavedRoad-3 — the handoff carries the brief's prompt.** `tools/roles/handoff.py` renders the brief's `## The prompt` into the Task section as a `brief:prompt` field. Three writers needed the finding, its log path or the owner's ruling sent separately by SendMessage, because the Task section dropped it.
4. **TOOL-dPavedRoad-4 — `--staged` grades the staged joins.** `tools/memory-tree/check-memory-hygiene.sh --staged` grades check 12's edge reciprocity and check 23's ledger joins for the staged specs and ledgers only. Both are held under `--staged` today, so 6 one-way edges and 10 unjoined ledger lines surfaced only at the close and cost two adopted units.

### Acceptance
Each unit's own probe: (1) a spec holding a known false-positive token reds under `--spec` while DEFERRED, and the role allowlist admits the leg; (2) a Stop payload missing an agent line yields a block message containing that agent's exact derived line; (3) a rendered handoff's Task section holds the brief's prompt; (4) a staged spec with a one-way edge and a staged ledger with an unjoined line each red under `--staged`, and an unstaged one does not.

### Gates
`bash tools/run-gates/run-gates.sh`, legs from `tools/gate-legs.json`.

### Non-goals
No change to what any check grades on the full run; no change to the spec-audit policy, the dispatch order gate, the packet regen or the manifest ratchet; no new role.

### Limitations
`--staged` must stay cheap: the corpus-wide check 23 cost 16 minutes, which is why it is held. Writers' token runs must stay inside the spec-writer role's write boundary.

### Reuse
Each unit extends its own file's existing seam: check-spec-tokens' live-spec walk, format-guard's defect list, handoff's `extract_task_fields`, and the hygiene script's `--staged` selection. Recall returned no record ruling against any of the four.

## Drawn from the session

> Which mechanical fixes should the fix build carry? … Writers self-check tokens, Format-guard prints lines, Brief prompt in handoff, Hygiene --staged joins
— owner, 2026-11-10

> Declare `spec-audit:` for dPavedRoad? … No audit
— owner, 2026-11-10

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: Go
