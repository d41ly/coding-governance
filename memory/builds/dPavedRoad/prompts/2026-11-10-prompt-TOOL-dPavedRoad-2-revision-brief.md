**Serves:** research TOOL-dPavedRoad-2

# Brief: TOOL-dPavedRoad-2's revision after the builder's divergence

## The brief

### Goal
DIVERGENCE: spec section 4, "Rollout", says `tools/gate-legs.json` is watched by the kickoff manifest and that "its re-audit falls to the main loop at the close. This pass does not do it." But S6 makes this pass edit `tools/gate-legs.json`, and the pre-commit hook refuses that commit. The refusal is `skills/session-kickoff/manifest-check.sh` check 5, staged leg, around lines 1776-1790. It reads: "staged changes touch watched files: tools/gate-legs.json but the staged manifest's audit block does not update last-audit … bundle the re-stamp into THIS commit". The code's own comment calls the bundle "the only green path here". So a pass that ships S6 cannot also leave the re-audit to the close. The only ways through are a re-stamp of `memory/guides/SESSION-KICKOFF.md`'s manifest-audit block, which the spec forbids and which is outside this unit's Files touched, or `--no-verify`, which would route around the refusal.

To fix it, the spec must say one of two things:
(a) The pass re-verifies the section-B claims fed by `tools/gate-legs.json` and bundles the `last-audit` re-stamp into its build commit. Then `memory/guides/SESSION-KICKOFF.md` joins Files touched and the Rollout sentence is removed.
(b) S6 leaves this unit for one that the close or a follow-up commits together with the re-stamp.

The same commit also needs `memory/builds/dPavedRoad/README.md` re-rendered with `python tools/memory-tree/gen_build_index.py --write`. The hook reported it as DRIFT once the CLOSED flip was staged. That file is generated, and Files touched should list it.

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
