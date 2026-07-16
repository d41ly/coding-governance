# tooling decisions — index

> One line per decision, append-only. Detail in decisions/.
- TOOL-aRuledParchment-1 · spec-format discipline in the kit: SPEC-TEMPLATE.template.md + conf-gated check 12 (SPEC_FORMAT_CUTOFF) + hardened _unfenced + self-test; dogfood armed 2026-07-15 -> builds/2026-07-15-TOOL-aRuledParchment/ (upstream inCMS ARCH-aRuledParchment-1/-2)
- TOOL-aWardenGraft-1 · adopted inCMS branch-guard inline in .githooks/pre-commit (§3 enforcement + red/green self-test); DECLINED node-doctor (inCMS-specific check registry, no cg env-health need) + standalone new-stream (thin git, stays adopter-supplied per WIRE §5)
- TOOL-aWireWarden-1 · built check-wiring.sh (--check/--fix/--session) + SessionStart hook auto-wiring unset core.hooksPath (never clobbers) + agent-cap detection via settings-merge.py --check; adopted agent-cap on cg; Tier-2 review wf_f0164aef -> builds/2026-07-15-TOOL-aWireWarden/
- TOOL-bThriftyBellows-1 · kit 1.2 fork-collapse of check-memory-hygiene.sh: set membership, one-awk checks 2/4/8, memoized index_set, batched wc + stale-guard — 2647s → 34s on a 1487-file tree, byte-identical ×3 targets (upstream PERF-eThriftyBellows-1) -> journal/2026-07-16-bThriftyBellows
- TOOL-bTamedTempest-1 · pytest-parallel-guardrails kit 1.0: xdist four-knob recipe + crashprobe death-attribution + aiosqlite seam patch + forced-race gate + domain-rules additions; 11-finding review folded (upstream inCMS ARCH-eVigilantCanary-2) -> builds/2026-07-16-TOOL-bTamedTempest/
