# decisions — index

> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.
> Grouped by family for reading; the file is never re-sorted and a landed row is never edited.

## PLAY — playbook

- PLAY-cDerivedGlossary-1 — Ported 2 lessons from inCMS DES-bMirroredLexicon-1 to domain-rules §12+§10: runtime-derive-vs-artifact fork; a gate's hardcoded export-mirror drifts, so derive it + a non-vacuity sentinel. — _Accepted 2026-07-22 (node c)_

## KICK — kickoff

*(none yet)*

## TOOL — tooling

- TOOL-aRuledParchment-1 · spec-format discipline in the kit: SPEC-TEMPLATE.template.md + conf-gated check 12 (SPEC_FORMAT_CUTOFF) + hardened _unfenced + self-test; dogfood armed 2026-07-15 -> builds/2026-07-15-TOOL-aRuledParchment/ (upstream inCMS ARCH-aRuledParchment-1/-2)
- TOOL-aWardenGraft-1 · adopted inCMS branch-guard inline in .githooks/pre-commit (§3 enforcement + red/green self-test); DECLINED node-doctor (inCMS-specific check registry, no cg env-health need) + standalone new-stream (thin git, stays adopter-supplied per WIRE §5)
- TOOL-aWireWarden-1 · built check-wiring.sh (--check/--fix/--session) + SessionStart hook auto-wiring unset core.hooksPath (never clobbers) + agent-cap detection via settings-merge.py --check; adopted agent-cap on cg; Tier-2 review wf_f0164aef -> builds/2026-07-15-TOOL-aWireWarden/
- TOOL-bThriftyBellows-1 · kit 1.2 fork-collapse of check-memory-hygiene.sh: set membership, one-awk checks 2/4/8, memoized index_set, batched wc + stale-guard — 2647s → 34s on a 1487-file tree, byte-identical ×3 targets (upstream PERF-eThriftyBellows-1) -> journal/2026-07-16-bThriftyBellows
- TOOL-bTamedTempest-1 · pytest-parallel-guardrails kit 1.0: xdist four-knob recipe + crashprobe death-attribution + aiosqlite seam patch + forced-race gate + domain-rules additions; 11-finding review folded (upstream inCMS ARCH-eVigilantCanary-2) -> builds/2026-07-16-TOOL-bTamedTempest/
- TOOL-aQuarriedLantern-1 · memory-recall kit 1.0 ported from inCMS ARCH-aTemperedLoom-1..-4: conf-driven retrieval, conf_digest in the cache key, loud zero-record diagnosis, rendered Skill + opt-in hook, 2 gate legs + WIRE §3c gate-wiring step -> builds/2026-08-03-TOOL-aQuarriedLantern/
- TOOL-aBatchedLintel-1 · kit 1.4 fork-collapse 2: checks 12 and 7 to one awk each (42.88s + 7.86s of an 81.77s run; 257.8s→1.66s upstream at 356 specs) + hygiene-parity.test.sh + 16 self-test arms; byte-identical over the real corpus and 28 shapes -> builds/2026-08-03-TOOL-aBatchedLintel/
- TOOL-aFoldedQuarry-1 · fold inCMS ARCH-dQuarriedLedger-1 + ARCH-dWinnowedTrove-2 into the memory-tree kit as a PARAMETERISED port (mechanism, never inCMS's corpus numbers), then re-dogfood on this repo's memory/ -> builds/2026-08-08-TOOL-aFoldedQuarry/
- TOOL-aFoldedQuarry-2 · U6 tier2-review.js joins findings to verdicts on an orchestrator-assigned INTEGER (Map), not an echoed file:line; agreeing repeat idempotent, disagreeing repeat -> UNVERIFIED; kept the kit's unverified/PARTIAL reporting; 2 new gates + 16-arm self-test
- TOOL-aFoldedQuarry-3 · U1 flatten: builds/<slug>/ (no date/FAMILY), one append-only DECISIONS.md, backlog/<FAMILY>.md; discipline becomes the spec header's `streams` enum gated by STREAMS_CUTOFF; every retargeted selector asserts a NON-EMPTY population; kit 1.4->1.5
- TOOL-aFoldedQuarry-4 · U2 retires gen-memory-tree.sh/TREE.md for gen_build_index.py: build status DERIVED from spec headers, rendered into each build README, LIVE.md and ledger/<month>.md; one source of truth per build (a `status:` key is legal ONLY when nothing is derivable)
- TOOL-aFoldedQuarry-5 · U3 corpus_ids.py adds checks 13-16 (id collision, orphan waiver, 4-rule dead-path registry, read-path accounting); declares no grammar or set it does not own — grammar from memory-recall, the two sets asked of the shell; pins measured

## DEPL — deployer

*(none yet)*
