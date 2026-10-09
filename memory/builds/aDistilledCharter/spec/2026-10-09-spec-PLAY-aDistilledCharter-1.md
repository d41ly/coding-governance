# PLAY-aDistilledCharter-1 — the charter template v4.0, with a disposition for every v3.5 rule

**Status:** SPECCED · rev-4 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams playbook · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

Rewrite `coding-governance-agents.template.md` as three sections: governing practices that bind
every adopter, one line each; the adopter's own one-line rules; and a generated block holding the
node registry, the tools and protocols of the selected kits, the deploy answers and the micro-formats.
Every one of the 205 rules of v3.5 gets a recorded destination, so nothing leaves the charter
silently.

## 2. Scope (IN)

- **S1** — Section 1, `## 1. Governing practices`: one `<!-- one-line -->` region of practice
  lines, each opening with a bracketed handle, §4 "Section 1". Observed by AC1 and AC2.
- **S2** — Section 2, `## 2. This repository`: a one-line region holding `{{ADOPTER_RULES}}`
  (TOOL-aDistilledCharter-1). Observed by AC1.
- **S3** — Section 3: `## Node registry` holding `{{NODE_TABLE}}` and its one-line claim note
  (TOOL-aDistilledCharter-2); `## Tools to rely on` and `## Protocols`, one bullet per selected
  kit, each inside that kit's `kit:` fence; `## Facts`, the deploy answers; `## Micro-formats`,
  the `<!-- microformats -->` definitions kept byte-identical and a one-line region of the rules for
  emitting them. The `when:node-table` and `when:security-outbound` fences do not survive into
  v4.0. Observed by AC1, AC3 and AC4.
- **S4** — The disposition ledger of §4 maps every v3.5 rule to its destination, and each
  destination resolves. Observed by AC5.
- **S5** — v3.5 is archived as `memory/archive/coding-governance-agents.template-v-3-5.md`, the
  marker reads `v4.0`, and `tools/template-size-highwater.txt` re-records the template at its new
  size, so any growth warns. The ceiling row in `tools/template-size-limits.txt` stays 49152: the
  leg's own name, `template size <=48KiB`, states it, and some thirty records cite that name, so
  lowering it is a rename and an owner decision, not a fold. Observed by AC6.
- **S6** — v4.0 has no line `PROSE_AUDIT` fills: it named an audit script no tree has. Its row
  stays in `tools/govkit/entries/playbook.kit.toml` as a legacy row, because a seeded v3.x template
  still names it (`TOOL-aDistilledCharter-2` rev-2). Observed by AC1.

## 3. Non-goals (OUT)

- Gov's own charter. PLAY-aDistilledCharter-4 re-renders it; this unit's render observations run
  over fixtures and a scratch target.
- Relocating content into shipped guides. PLAY-aDistilledCharter-2 and -3 do it, and land first.
- Re-pointing citations of v3.5 section numbers elsewhere. TOOL-aDistilledCharter-4.
- New gates for rules the ledger keeps as practices. Each is a candidate for a later ask, not this
  build.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-1` — the one-line grade and `ADOPTER_RULES`.
- **consumes-from** `TOOL-aDistilledCharter-2` — `NODE_TABLE` and the retired node placeholders.
- **consumes-from** `PLAY-aDistilledCharter-2` — the review protocol's security and tier sections.
- **consumes-from** `PLAY-aDistilledCharter-3` — the hygiene guide's id protocol.
- **hands-off** `PLAY-aDistilledCharter-4` — gov's re-render.

## 4. Design

### Section 1

Thirty-three practices, in this order, by handle: `yagni` · `reuse` · `consistency` · `core` ·
`contract` · `derive` · `one-fact` · `verify` · `gate` · `class` · `left-shift` · `bar` · `cost` ·
`small` · `isolate` · `land` · `reconcile` · `migrations` · `ids` · `memory` · `records` · `docs` ·
`security` · `risk` · `bound` · `bytes` · `cross-os` · `tokens` · `tools` · `voice` · `signal` ·
`formats` · `default`. The `cross-os` line sits inside the `when:cross-os` fence. The `bound` line
keeps the literal `at most 5 verify agents TOTAL`, which the parity gate compares with the hook and
the restatement waiver names. A line states a practice, never a procedure: where a procedure exists,
the line points at the tool or guide section 3 lists.

### Micro-format rules

Six handles under the definitions: `r1` (a bare list item), `grammar` (head, joiner, fields, the
optional-field notation), `pair` (`BUILD` and `SPEC`), `gates-line`, `state` (payload first, one
state block) and `links`.

### Section 3 kit lines

| Kit fence | Tools line | Protocol line |
|---|---|---|
| `kickoff-manifest` | `/session-kickoff` opens every unit | — |
| `memory-tree` | `gotchas.py --for-diff` before a review | BUILD-METHOD, TEMPLATE-SPEC, HYGIENE |
| `codebase-map` | the dossier first, `reuse_lookup.py` before building | — |
| `memory-recall` | `/memory-recall` for a why-question | — |
| `drift-audit` | `/drift-audit` when records may have drifted | — |
| `lexicon` | `/lexicon` before naming | — |
| `review-harness` | `tier2-review.js` for a Tier-2 review | REVIEW-PROTOCOL |
| `agent-cap` | the cap hook's refusal is read, never routed around | — |
| `unattended` | `/unattended` | UNATTENDED-PROTOCOL |
| `runlog` | `/runlog` | — |
| `push-main` | the lander, never bypassed | — |
| `process-monitor` | `reap.py --sweep` | — |
| `pytest-parallel-guardrails` | the guarded runner | — |
| `gate-lint` | the shell-hygiene scans | — |

No line spells `<prefix>/run-gates/` or `<prefix>/runlog/`: `tools/playbook-kit-waivers.txt` waives
those kits, and a waived kit the playbook names reds the parity gate's arm 6.

### Disposition ledger

Lines are v3.5's at BASE. A destination is one of: `practice [h]` and `format [h]` (a handle above);
`fact KEY`, `nodes`, `tools <kit>` and `protocol <kit>` (section 3); `kept` (byte-identical);
`moved <path> § <heading>`; `gated <leg>`; `owned <path>`; or `deleted —` and the reason.

| Lines | Rule | Destination |
|---|---|---|
| §0 17 | session-scope every new id | practice [ids] |
| §0 18 | own streams, isolate runtimes | practice [small] [isolate] |
| §0 19 | memory non-derivable, status derived | practice [memory] [derive] |
| §0 20 | gates are the merge bar | practice [bar] [left-shift] |
| §0 21-22 | the declared bound and total | practice [bound] |
| §0 23 | verify before claiming done | practice [verify] |
| §0 24 | consistency by construction | practice [consistency] |
| §0 25 | chat carries signal | practice [signal] |
| §0 26 | when no rule covers it | practice [default] |
| §1 30 | keep units small | practice [small] |
| §1 33-36 | DoR sync, locate, scope, reserve | owned `skills/session-kickoff/SKILL.md` Steps 1-4; tools kickoff-manifest; practice [ids] |
| §1 37 | Tier-2 DoR is a design pass | gated `memory hygiene` check 12; protocol memory-tree |
| §1 38 | scope approval before building | practice [risk]; owned SKILL.md Step 3 |
| §1 40 | design pass refreshes a dossier | tools codebase-map |
| §1 44 | DoD gates green, verified | practice [verify] [bar] |
| §1 45 | DoD finding left-shifted | practice [left-shift] |
| §1 46 | DoD help page | practice [docs] |
| §1 48 | DoD inventory keys claimed | gated `codebase-map coverage + freshness` |
| §1 50 | DoD records committed first | practice [records] |
| §1 51 | DoD kickoff manifest updated | gated `kickoff-manifest ratchet` |
| §1 54 | land local first, explicit ask | practice [land] |
| §1 56-57 | the ask's one substitute; unattended landing | protocol unattended |
| §1 59 | diff-scoped gate after each merge | practice [land] |
| §1 60 | reconcile additively | practice [reconcile] |
| §1 61 | land risky behaviour dark | practice [small] |
| §1 62 | reversible migrations | practice [migrations] |
| §1 67 | manifest merge exception | gated `kickoff-manifest ratchet` — its refusal names the re-stamp |
| §1 73-78 | the unattended contract | protocol unattended |
| §2 83, 86-88 | register every node; the table | nodes |
| §2 91-93 | identify by machine/user; claim; onboard | nodes — the claim note |
| §2 94-95 | id shape and slug | practice [ids]; moved `memory/HYGIENE.md` § Ids |
| §2 96-103 | seq, collision grep, no counter, session, children, tie-break, legacy, shorthand | moved `memory/HYGIENE.md` § Ids |
| §3 107 | own streams | fact STREAM_OWNERSHIP |
| §3 108 | trunk-based, merge often | practice [small] |
| §3 109, 113 | main in one tree; worktree lifecycle | practice [isolate] |
| §3 110 | machine-enforce the branch rule | deleted — an instance of [default]'s "gate over remember"; the hook is each repository's own |
| §3 111 | doc-only commits on idle main | deleted — a special case of [isolate] that a branch guard decides |
| §3 112 | one worktree bootstrap script | fact WORKTREE_SCRIPT |
| §3 114 | commit the governing doc | deleted — the render writes a tracked file; an uncommitted charter is not a charter |
| §3 115 | contract-first | practice [contract] |
| §3 116 | --no-ff landings | practice [land] |
| §3 117 | the attribution trailer | fact COMMIT_TRAILER |
| §5 121, 122, 125 | non-derivable memory; mirror; recalled memory | practice [memory] |
| §5 123 | one append-only or generated index | gated `memory hygiene` |
| §5 124 | status derived | practice [derive]; gated `memory hygiene` |
| §5 126 | secrets never in memory | practice [security] |
| §5 127 | user docs in the help dir | practice [docs] |
| §5 128-132 | an inventory whose keys cannot rot | tools codebase-map; gated `codebase-map coverage + freshness` |
| §5 133-135 | ask whether the record matches the tree | tools drift-audit |
| §5 136-137 | retrieval over the decision corpus | tools memory-recall |
| §5 138-144 | the structured memory tree | protocol memory-tree; gated `memory hygiene` |
| §6 148-152 | wire the governing doc for every tool | gated `agent-instructions wiring` |
| §6 153, 157 | log and backlog record types; two-tier logs | protocol memory-tree |
| §6 154 | id families | fact ID_FAMILIES |
| §6 155 | record decisions as you make them | practice [records] |
| §6 156 | session-start reading order | fact DOC_ROUTING_TABLE |
| §6 158-161 | preamble, layout, commands, context home | fact PRODUCT_PREAMBLE, REPO_LAYOUT_MAP, COMMAND_CATALOG, PRODUCT_CONTEXT_HOME |
| §6 162-164 | a value beside its owner rots | practice [one-fact] |
| §6 165 | in-doc paths repo-root-relative | deleted — `dead-path carriers (deleted files still named)` grades citations; [links] covers user-facing ones |
| §6 166 | provenance inline | deleted — a style preference no reader acts on before a gate fires |
| §6 167 | a security-model section per surface | moved `memory/TEMPLATE-SPEC.md` § Security boundaries |
| §7 171-174, 202-203 | parallel test runner guardrails; structural classes; per-file isolation | tools pytest-parallel-guardrails |
| §7 175-179 | silent-failure shell scans | tools gate-lint |
| §7 180-183 | tooling as a declared population | practice [derive]; gated `govkit selfcheck` |
| §7 184 | green at the push boundary | practice [bar]; fact GATE_COMMANDS |
| §7 185 | wire remote CI | fact CI_FILE |
| §7 186-187 | one command; faster variant documented | practice [bar]; fact GATE_RUNNER |
| §7 188-189, 210 | single source and parity; lockstep guards; coupled releases | practice [contract] |
| §7 190-194, 198, 208 | header states the gap; liveness; green-by-absence; exemptions | practice [gate] |
| §7 195-196 | no typed count | practice [derive] |
| §7 197 | left-shift every finding | practice [left-shift] |
| §7 200 | map legs are bar legs | gated `codebase-map coverage + freshness` |
| §7 204-207 | cost is a verdict | practice [cost] |
| §7 209 | migration forks via a merge revision | practice [migrations] |
| §7 212-214 | provenance paragraph | deleted — a history note; the history is git's |
| §7 216-217, 223-224 | failing case observed; a skip announces itself | practice [gate] |
| §7 218-222, 225-226 | shared-variable guard; predicate over the real tree; gate the class | practice [class] |
| §8 230-232 | Tier 1, Tier 2, once at the boundary | practice [risk]; moved `memory/TEMPLATE-SPEC.md` § Tiers |
| §8 233, 246-249, 252, 256-260 | lens shape, concrete findings, precision, priming, richness, sidechains, schemas | owned `memory/guides/REVIEW-PROTOCOL.md`; protocol review-harness |
| §8 234-245 | concurrency and total capped | practice [bound]; gated `verifier fan-out` and the `agent-cap` hook |
| §8 250 | persist each Tier-2 run | fact REVIEW_DIR |
| §8 251 | commit an experiment's instruments | practice [records] |
| §8 253 | verify before done | practice [verify] |
| §8 254 | commit freely; landing is §1's | practice [land] |
| §9 264-266, 271-276 | write-boundary sanitize, composite guard, capability gate, authz core, automation principal, draft-only, PII, concurrency, test-env protections | practice [security] [core]; moved `memory/TEMPLATE-SPEC.md` § Security boundaries |
| §9 268-269 | URL normalizer; SSRF guard | moved `memory/TEMPLATE-SPEC.md` § Security boundaries |
| §10 279-283 | the project's own bug-class checklist | practice [left-shift]; tools memory-tree |
| §11 288-289 | LF; verify staged bytes | practice [bytes] |
| §11 290 | toolchain pins | fact TOOLCHAIN_NOTES |
| §11 291-294 | deterministic run modes; MSYS paths; native installs; crash evidence | practice [cross-os] |
| §12 300-301, 311, 313 | extension pattern; factories; promote primitives; reuse audit | practice [reuse]; fact KIND_FACTORY_MAP, SHARED_PRIMITIVES_LOCATION |
| §12 302, 312 | shared core; forward-compatible data | practice [core] |
| §12 303-310 | single source, runtime derivation | practice [contract] |
| §12 314 | gate the layout conventions | practice [consistency] |
| §12 315 | a kit file names nothing outside itself | gated `install-prefix (shipped surface)` |
| §12 317, 319-324 | the lexicon block | tools lexicon; gated `lexicon naming predicates`, `lexicon wiring` |
| §14 329-334, 336 | token discipline | practice [tokens] |
| §14 335 | pin the diff base to a sha | practice [tokens]; owned SKILL.md Step 1 |
| §15 340-345 | voice | practice [voice] |
| §16 349-352, 356-357, 361 | scope, facts outrank format, silent mid-turn, no repeats, readable | practice [signal] |
| §16 353 | a routine outcome is one line | format [r1] |
| §16 354 | the gates line | format [gates-line] |
| §16 355 | payload first, one state block | format [state] |
| §16 358 | kickoff reporting | owned SKILL.md Step 5 |
| §16 359 | facts on disk before the wrap-up | practice [records] |
| §16 360 | no credential in chat | practice [security] |
| §16 362 | micro-formats are mandatory | practice [formats] |
| §16 363-373, 403 | the grammar; optional fields | format [grammar]; gated `micro-format definitions` |
| §16 374-380 | R1 | format [r1] |
| §16 383-393 | the eleven shapes | kept |
| §16 396-402 | BUILD and SPEC binding pair | format [pair] |
| §16 404 | pre-send self-check | deleted — a list restating the rules above it |
| §16 405 | the prose audit script | deleted — it named no script in any tree, and a threshold nothing measures binds nothing |
| §16 406-407 | link format; session-relative hrefs | format [links] |
| 1-13 | title, banner, marker, what/use note | replaced by the v4.0 header; the marker kept at `v4.0` |

### Files touched (estimate)

`coding-governance-agents.template.md` · `memory/archive/coding-governance-agents.template-v-3-5.md` · `tools/govkit/entries/playbook.kit.toml` · `tools/template-size-limits.txt` · `tools/template-size-highwater.txt`

### Alternatives rejected

- **One shipped companion holding every rule the charter drops.** It moves the disease rather than
  curing it; v3.0 converged a companion into the charter for exactly that reason.
- **Per-kit rows in each kit's descriptor, composed by the renderer.** The template's `kit:` fences
  already compose per-kit lines at zero new mechanism; a self-describing kit is a later ask.
- **Deleting what a gate enforces with no line left.** Kept as a practice where the agent must act
  before the gate can see anything, such as verifying before claiming done.

## 5. Production-readiness checklist

- security — no write path; the security practices keep their substance in section 1 and the
  review protocol.
- perf / scale — the charter shrinks well under the 32 KiB a Codex agent reads
  (`tools/agent-instructions/adopt-agent-instructions.sh` `CODEX_MAX`).
- error / empty / loading states — an adopter with no `adopter_rules` renders the default line.
- observability — the ledger is the record of where every rule went.
- risks — an adopter's wrapper or records citing v3.5 section numbers keep naming sections that no
  longer exist; DEPL-aDistilledCharter-1's runbook says so, and frozen records stay frozen.
- testing — the render selftest and gov's render wiring (PLAY-aDistilledCharter-4).
- migration — `govkit update` re-renders every adopter's region; nothing in an adopter's
  `deploy.toml` must change, because every surviving placeholder keeps its key.
- user docs — the template's own header, and the runbook (DEPL-aDistilledCharter-1).

## 6. Acceptance criteria

- **AC1** — When `render_playbook.py --target` renders a scratch target with every kit selected,
  the render succeeds, no `{{` survives, and every line of both one-line regions passes the grade.
  Red when: the render refuses or a placeholder survives.
- **AC2** — When `grep -c '^- \[' coding-governance-agents.template.md` runs over section 1's region,
  it counts 33, and each handle of §4 appears exactly once. Red when: a handle is missing or doubled.
- **AC3** — When `bash tools/check-microformats.sh` runs, it is green, and the definition lines are
  byte-identical to BASE's. Red when: a definition moved by a byte.
- **AC4** — When the scratch render selects only `memory-tree`, no tools or protocol line of another
  kit appears. Red when: an unselected kit's line survives.
- **AC5** — When every destination in §4's ledger is resolved (`practice`/`format` handles grepped
  in the template, `moved` paths and headings grepped in the guides, `gated` names looked up in
  `tools/gate-legs.json`, `fact` keys grepped as placeholders), none is missing. Red when: one is.
  cost: a scripted pass, minutes.
- **AC6** — When `bash tools/check-template-size.sh` runs, the template is green and its high-water
  in `tools/template-size-highwater.txt` equals its new size, and `memory/archive/` holds the v3.5
  bytes of BASE. Red when: the high-water still reads 48597, or the archive differs from BASE.

## 7. Gates

`template size <=48KiB` · `micro-format definitions` · `playbook parity` · `playbook placeholder catalogue` · `line length` · `agent-cap restatement` · `playbook render wiring` · `memory hygiene` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-4 · 2026-10-09 · §4 · the security and tier rows move to `memory/TEMPLATE-SPEC.md`
  (`PLAY-aDistilledCharter-5`, closing review round 2, B1).
- rev-3 · 2026-10-09 · S6 · `PROSE_AUDIT` stays declared as legacy, agreeing with
  TOOL-aDistilledCharter-2 rev-2, which keeps every name a v3.x template uses.
- rev-2 · 2026-10-09 · S5 · AC6 · the ceiling row stays 49152 and only the high-water moves: the
  leg is named for the ceiling and about thirty records cite the name.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` found no seam composing per-kit
charter lines; the extended seam is the renderer's existing `kit:` fence pass (`remove_fenced` in
`tools/playbook/render_playbook.py`), which already drops an unselected kit's block. The rule map
behind the ledger was taken by a read-only agent over BASE on 2026-10-09.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag` — surfaced `TOOL-aSiftedPlaybook-1` and `aFusedCharter`, the prior reconvergences.
