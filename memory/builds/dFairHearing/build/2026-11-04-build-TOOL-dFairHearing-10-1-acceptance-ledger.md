# Acceptance ledger — TOOL-dFairHearing-10

**Serves:** journal TOOL-dFairHearing-10

Built against spec rev-3 and committed as pass commit `59c5af433`, at parent `69930b485`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-10-2-builder-return.md` and the pass commit's message; nothing below was observed again for it. The first return, `2026-11-03-build-TOOL-dFairHearing-10-1-builder-return.md`, committed nothing and observed no criterion, and rev-3 changed no criterion's text. No suite, gate or bar ran in the pass: the spec declares no `New arm:` line, and its legs are owed to the close.

**Evidences:** TOOL-dFairHearing-10
- AC1 — `lenses.toml` — the retired-lens grep printed nothing over either protocol copy, and the pointer is present in `memory/guides/REVIEW-PROTOCOL.md`
- AC2 — `memory/guides/REVIEW-PROTOCOL.md` — the lens-count range grep printed nothing, and the default configuration says five lens slots, `LENS_SLOTS` in `check-verifier-fanout.sh`
- AC3 — `default-refute` — the grep printed nothing over either protocol copy, and the protocol states the harness's rule: refuted for a medium or low finding a skeptic cannot establish, uncertain for a blocker or high
- AC4 — `check-verifier-fanout` — the grep found the three rule homes, `check-verifier-fanout.js`, `check-review-join.js` and `spec-audit-optin.js`, and the does-not-reach list says an inline script's verifier total is checked at no tool call
- AC5 — `tier2-review has four` — the grep printed nothing, and the comment beside `MAX_LENSES` in `tools/hooks/agent-cap.js` now says tier2-review runs five lenses on both kinds
- AC6 — `tools/workflows/tier2-review.js` — the render and `tools/workflows/tier2-review.template.js` each hold 2 `agent-cap` lines, and both of the template's name the `MAX_VERIFIERS` bound the hook still holds
- AC7 — `.claude/agents/gov-synthesizer.md` — the input sentence lists confirmed and unverified findings, refuted claims and same-address twins, a twinned run's two runs, and the disposition inputs. The body-size probe printed 1625 against the 3072 ceiling
- AC8 — `tools/check-agent-cap-restatement.sh` — its pattern matched none of the pass's added template lines, and the waiver row `≤5 batched skeptics (required)` still counts 1
- AC9 — `KIT_ROLES_VERSION = ` — each version differs from base: review-harness 1.56 against `1.53` and roles 1.12 against `1.8`. Earlier units moved both, and the spec's hands-off edge to `TOOL-dFairHearing-23` supersedes this version half with the lander's mint
