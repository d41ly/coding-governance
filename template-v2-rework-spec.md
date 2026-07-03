# Template v2.0 rework — wiring spec

*2026-07-03. Drives the v1.4 → v2.0 rework of `parallel-coding-governance.template.md`. Two changes land
together: (1) **wire in the functionality the template lacked** (found by an 88-agent gap analysis against the
inCMS `CLAUDE.md` — 6 section-chunked finders → merge → one default-refute skeptic per candidate → completeness
critic; 80 findings upheld, 0 refuted), and (2) **rework the whole template to a minimal one-line-per-directive
format**. This file is the durable record of what moved where and what was deliberately dropped.*

---

## 1 · Style contract (binding on all future template edits)

- **One line per directive.** Each bullet is exactly one imperative rule. A bullet may wrap in the source (~110
  cols) but carries ONE rule. No narrative paragraphs; a section preamble is at most one line.
- **The line = rule + trigger + one-phrase why (only when non-obvious).** A directive that loses its trigger,
  exception, or load-bearing why in compression is a broken directive — *kill the frame, keep the fact.* When a
  rule genuinely can't fit one line, it becomes two directives, not a paragraph.
- **Tables/code blocks survive only where they ARE the directive** — the node registry, the ledger schema, the
  micro-format catalog. Everything else is bullets.
- **Placeholders**: every `{{X}}` used in the body appears in the Customize block, and vice versa. Grep `{{`
  after instantiation stays the completeness check.
- **Provenance stays**: a rule motivated by a measured audit or incident keeps its one-phrase citation.

## 2 · Section map (v1.4 → v2.0)

| v1.4 | v2.0 | Notes |
|---|---|---|
| header + §0 TL;DR | header + §0 | TL;DR gains output-discipline + runtime-isolation lines |
| §0.5 lifecycle | **§1** | unchanged function, compressed |
| §1 nodes & IDs | **§2** | + registry variance columns, node self-ID by machine/user, onboarding checklist, legacy-era freeze, shorthand policy |
| §2 parallel hygiene | **§3** | + worktrees-only feature work, hook enforcement, doc-only-on-main guard, scripted bootstrap, worktree lifecycle, `--no-ff` landings, commit trailer |
| — | **§4 Runtime isolation & verification harness (NEW)** | port offsets, one-at-a-time, port hygiene, build-time bakes, workspace-scope anchoring, per-node harness registry, maintained verify recipe, false-signal modes, capability-myth rule |
| §3 memory | **§5** | + no-secrets-in-memory/docs, fresh-machine seeding, help-docs index + removal |
| §4 decisions/backlog | **§6 Decisions, backlogs & the governing doc** | + ordered session-start reading, two-tier index→detail, doc-routing table, product preamble, repo-layout map, command catalog, product-context home, in-doc path convention, provenance annotations, per-surface security models |
| §5 gates | **§7** | + CI required-checks wiring, concurrent gate runner, local↔CI leg equivalences, green-by-absence gate, structural test classification, parallel-suite invariants, documented exemptions, migration-fork protocol, coupled-artifact deploys |
| §6 review | **§8** | + in-repo review corpus & ROI re-tuning, orchestration-runtime constraints; verify-harness content moved to §4 |
| §7 security | **§9** | + composite write-guard on all sibling paths, capability-gated content, draft-only automation default, non-login narrow principal, https-only egress, test-env divergence documentation |
| §8 bug classes | **§10** | + 9 generalizable classes (see §4 below) + documented-check graduation path |
| §9 cross-OS | **§11** | + native-shell installs; per-node credential quirks live in §2's registry |
| §10 token efficiency | merged into **§14** | it was a pointer section; pointers don't earn a section in a one-line doc |
| §11 arch consistency | **§12** | + two-tier widget-promotion ladder |
| §12 visual consistency | **§13** | + living-reference-route authority rule |
| §13 session hygiene | **§14** | absorbs §10's strategy line |
| §14 voice | **§15** | + voice/volume decoupling, always-permitted wrap-up line |
| — | **§16 Output discipline (NEW)** | the whole missing category — see §3 below |
| §15 file references | **§17** | unchanged function |
| Customize block | Customize block | + ~14 new placeholders |

Instantiated v1.x copies **re-adopt v2.0 section-by-section** (the one-line rework defeats §-body diffing);
the template header says so.

## 3 · Gap wiring (the 80 upheld findings → destinations)

Full finding list: gap-analysis run `wu6yl5nbr`, 2026-07-03 (condensed keys below).

- **Output discipline → new §16** (~15 findings): work-report scope + user-ask override · facts-outrank-format
  (rule 0) · mid-turn silence · destructive-action heads-up interrupt window · routine-outcome one-liners ·
  exhaustive gate enumeration with `skipped:` legs · payload-first final message + single state block ·
  size-to-what-changed with mandatory lifts · no-duplicate delivery · kickoff compression · facts-on-disk-first ·
  chat credential hygiene · micro-format catalog · pre-send self-check · measured audit + drift thresholds
  (`{{PROSE_AUDIT}}`). §15 (voice) gains the volume/voice decoupling + wrap-up-line allowance.
- **Machine enforcement → §3, §7**: pre-commit branch guard + installer + session-start nudge (§3); CI
  required checks (`{{CI_FILE}}`), one-command concurrent gate runner (`{{GATE_RUNNER}}`), local↔CI leg
  equivalences (§7).
- **Runtime isolation → §4**: port offsets (`{{PORT_OFFSET}}`), one-server-per-canonical-port, free-port-first,
  build-time bakes (`{{BUILD_TIME_BAKES}}`), workspace-scope anchoring.
- **Verification harness → §4**: maintained verify recipe (`{{VERIFY_RECIPE}}`), per-node launch registry,
  false-signal modes, capability-myth correction.
- **Node/environment registry depth → §2**: variance columns (remote name, launch config, credential quirks —
  covers elevated-scope push credentials), self-ID by machine/user not path, onboarding checklist,
  in-doc path convention (§6).
- **Branch/worktree mechanics → §3**: feature-work-in-worktrees-only, doc-only-on-main guard,
  `{{WORKTREE_SCRIPT}}` bootstrap, lifecycle (enumerate/recreate/move+repair), `--no-ff` descriptive landings,
  `{{COMMIT_TRAILER}}`.
- **Context routing → §6**: ordered reading (master index first), two-tier logs, `{{DOC_ROUTING_TABLE}}`,
  `{{PRODUCT_PREAMBLE}}`, `{{REPO_LAYOUT_MAP}}`, `{{COMMAND_CATALOG}}`, `{{PRODUCT_CONTEXT_HOME}}`,
  provenance annotations, per-surface security models (read-before-extend).
- **ID eras → §2**: legacy-era freeze, shorthand citation policy.
- **Security posture → §9**: composite guard on all sibling write paths, capability gate, draft-only automation,
  non-login principal, https-only, test-env divergence docs; no-secrets-in-memory/docs → §5.
- **Test-harness discipline → §7**: green-by-absence collection gate, structural auto-marking, parallel
  file-isolation invariants, documented exemptions, pure-core/thin-glue split (→ §10's documented-check line).
- **Migrations/deploys → §7**: merge-revision reconciliation (never rebase), local-harness-blind-to-forks note,
  coupled-artifact deployment atomicity.
- **Design refinements → §12/§13**: promotion ladder (§12), reference-route authority (§13).
- **New §10 bug classes** (9): check-then-insert vs bulk-UPDATE race · degraded-response-cached-as-empty ·
  stale-async-response race · blocking hot path (generalized from §9's DNS case) · verify-computed-not-declared ·
  scale-to-fit synchronous measurement · inline-nested-component remount · scrollbar-toggle layout shift ·
  focus-out dismissal per a11y authoring practices. Plus the documented-check graduation mechanism.
- **Review protocol adds → §8**: `{{REVIEW_DIR}}` corpus + periodic ROI re-tuning, orchestration-script runtime
  constraints (restricted language, no imports, no hook/doc inheritance).

## 4 · Deliberately dropped or merged from v1.4

- All multi-sentence *rationale prose* (e.g. §12's closing "why this saves tokens" blockquote, §6's audit
  narrative) — compressed to one-phrase riders on the directives they justified. No rule was dropped.
- v1.4 §10 (token efficiency) as a *section* — it only cross-referenced other sections; its one substantive
  line ("spend tokens on new judgment; stop once verified") opens v2.0 §14.
- The v1.4 "example" sub-clauses that were pure illustration (not triggers/exceptions) where the rule stands
  alone; illustrative micro-examples kept only where the concrete form IS the rule (micro-formats, evasion
  strings like `/\evil`, `git -C` mangling).
- Nothing else. Every v1.4 directive must be traceable to a v2.0 line; the rework's acceptance check is a
  directive-coverage audit of v1.4→v2.0 plus a gap-coverage audit of the 80 findings.

## 5 · Versioning mechanics

- v1.4 snapshotted as `parallel-coding-governance.template-v-1-4.md` (done in the same change).
- Header bumped to v2.0 with the format-rework + re-adoption note; `<!-- governance-template: v2.0 -->` marker
  updated.
- Adopters: diff-by-§-body does not survive a format rework — re-adopt per section using the §-map above.
  From v2.0 on, §-body diffing works again (the header says so).
- Post-audit: a 12-agent verification (6 v1.4-directive-coverage auditors, 4 gap-coverage auditors, one
  style auditor, one refs/placeholders auditor) returned 30 findings — lost triggers/exceptions from
  compression, fused bullets violating the §1 style contract, an unused `{{PROJECT_NAME}}`, and a literal
  placeholder in the header that would trip the post-instantiation `grep '{{'` forever. All 30 applied
  before landing; placeholder parity re-verified 34/34.
