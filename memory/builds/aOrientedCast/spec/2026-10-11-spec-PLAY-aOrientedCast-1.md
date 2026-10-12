# PLAY-aOrientedCast-1 — the charter: every agent is handed a rendered role, and the main loop delegates

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams playbook · order 8 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-PLAY-aOrientedCast-1-1-acceptance-ledger.md](../build/2026-10-11-build-PLAY-aOrientedCast-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md) | research | TOOL-aOrientedCast-1 |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-5-resume-handoff.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-5-resume-handoff.md) | journal | TOOL-aOrientedCast-1 |
| [2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md) | diff-review | KICK-aOrientedCast-1 KICK-aOrientedCast-2 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 |

<!-- /gen:spec-records -->

## 1. Goal

The charter says every product-code unit carries a spec and that a write gate refuses an unowned
write, but nothing in it says who writes that spec, who builds from it, or what any agent is told.
This unit states the rule the build exists for, in one bullet a target without the roles kit never
renders: every agent is handed a rendered role, spec writing and review, building and the closing
review run only in role agents, and the main loop orients, hands off and keeps the books. It points
at the roles kit's README for the catalogue, and it corrects the one charter sentence the build makes
false.

## 2. Scope (IN)

- **S1** — `coding-governance-agents.template.md` gains the three lines in §4 "The new text" directly
  after the `<!-- /kit:agent-cap -->` line that closes aRoutedQuill's write-gate bullet in §1's
  Definition of Ready: a `kit:roles` fence holding one bullet that states the rule and points at
  `<prefix>/roles/README.md`. Observed by AC1 and AC3.
- **S2** — In §8, the sidechain bullet's clause `It DOES inherit the governing doc and hooks DO fire
  in it, both measured;` becomes `Hooks DO fire in it, measured;`, because a role agent rendered with
  `omitClaudeMd` holds no charter (§4 "Evidence"). The rest of that bullet is byte-identical.
  **Readers:** by name: `coding-governance-agents.template.md` and its render `AGENTS.md`; a git grep
  over the tracked tree outside the memory tree on 2026-10-11 found no script, test or hook spelling
  the clause. by value: NO VALUE READERS, because no checker extracts this sentence: the playbook
  parity pairs read the fan-out values two bullets above it, and the size and line-length legs
  measure lengths only. Observed by AC1.
- **S3** — `.governance/deploy.toml`'s `kits` array gains `roles`, so gov's own render keeps the new
  bullet; the array's comment already says it lists every kit this repository carries. Observed by
  AC2.
- **S4** — `AGENTS.md` is re-rendered from the template with
  `bash tools/playbook/adopt-playbook.sh --target .`, and the fence markers do not reach it.
  Observed by AC2.
- **S5** — Both size subjects re-record their high-water in `tools/template-size-highwater.txt`
  with `--bump`, so the growth is priced rather than warned about. Observed by AC4.
- **S6** — The unit's commit stages a watched file, so it re-stamps `last-audit` in
  `memory/guides/SESSION-KICKOFF.md` in the same commit, naming that commit's parent. The §B claims
  the template feeds are re-read; none states the rule this unit adds, so `last-body-change` does
  not move unless check 9's count says it is owed when the unit builds. Observed by AC6.
- **S7** — The playbook kit's version moves once for this build, by the route `PLAY-aRoutedQuill-1`
  §8 F2 took: the marker `governance-template: v3.6` and the banner's `v3.6` both move to `v3.7`
  in the run's one mint commit after the last unit, with `AGENTS.md` re-rendered in that commit.
  This unit's own commit leaves both at `v3.6`, because no unit pass moves a kit version. Observed
  by AC7.

## 3. Non-goals (OUT)

- The workflow table, the role table and the enforcement points. They are the roles kit's README,
  which the bullet points at; restating them here is a second copy that rots.
- The write gate's and the spawn guard's contracts, and which role may write which path class. Those
  are the gates' own, and the charter states the rule, not the admission table.
- A §0 TL;DR bullet. §4 "Alternatives rejected" says why.
- The kickoff manifest's §B and the kickoff engine's Step 5. The kickoff units of this build own
  them; this unit only re-stamps `last-audit`.
- Raising the template's 48 KiB ceiling, which is an owner decision. This unit spends headroom.
- An archive snapshot of v3.6. The archive's last snapshot is v3.3, and git holds the rest.

### Edges

- **consumes-from** `TOOL-aOrientedCast-8` — the `roles` registry entry the `kit:roles` fence and
  the `kits` array both name. Without it the renderer refuses the fence and the array. It lands at
  order 7, before this unit, as §8 F1 resolved. The README the bullet points at is the catalogue
  unit's at order 1, which that unit consumes in turn; no criterion here reads the README itself.

## 4. Design

### Evidence

Read at `744e55db` on 2026-10-11, which is BASE `646d4a73` plus this build's three record commits;
no template, renderer or registry byte moved between them.

- The Definition of Ready is `coding-governance-agents.template.md:32-46`. aRoutedQuill's
  write-gate bullet sits in a `kit:agent-cap` fence at `:40-42`, and a `kit:codebase-map` fence
  follows at `:43-45`. The rendered bullet is `AGENTS.md:98`.
- The §8 sidechain bullet is `coding-governance-agents.template.md:256` and `AGENTS.md:294`. Its
  clause says a sidechain agent inherits the governing doc. The agent-type probe recorded under this
  build's `build/` folder measured, on CLI 2.1.292, a `Workflow` agent spawned with an `agentType`
  rendered with `omitClaudeMd: true` writing `NONE` where its untyped control wrote the charter's
  codeword. Every arm, typed or not, logged its `PreToolUse` and `SubagentStart` hooks. Once the
  harnesses spawn role types, the clause is true only of an untyped agent.
- `bash tools/check-template-size.sh` reports the template at 48800 of 49152 bytes, 352 under, and
  its high-water row is 48800. `AGENTS.md` is 54628 of 64512 with a high-water of 54628.
- `tools/line-length-limits.txt:23-24` caps both files at 450 characters a line.
- The renderer refuses a `kit:` fence naming anything that is not a registry entry id
  (`tools/playbook/render_playbook.py:363-366`), and refuses a `kits` member that is not one
  (`:654`). Gov's `kits` array is `.governance/deploy.toml:18-23` and does not hold `roles`. No
  registry entry is `roles` at BASE.
- `tools/check-playbook-parity.sh:215-223` reds a registry kit that neither the template nor
  `WIRE-INTO-PROJECT.md` names as `<prefix>/<kit>/`, `tools/<kit>/` or a backticked `<kit>/`, unless
  a waiver row excuses it. The new bullet names `<prefix>/roles/`.
- The template spells a kit path with the literal `<prefix>/` convention (`:4`, `:247`, `:249`), and
  the render keeps it: `AGENTS.md` carries `<prefix>/hooks/README.md`.
- `memory/guides/SESSION-KICKOFF.md:6` watches the template. The staged leg reds a commit that
  stages a watched file without moving `last-audit` (`skills/session-kickoff/manifest-check.sh:1410-1425`).
  Check 9 counts zero watched non-merge commits since `last-body-change` at `744e55db`.

### The new text

After `coding-governance-agents.template.md:42`, these three lines, in this order:

```markdown
<!-- kit:roles -->
- Every agent is handed a rendered role; spec writing and review, building and the closing review run only in role agents, and the main loop orients, hands off and keeps the books (`<prefix>/roles/README.md`).
<!-- /kit:roles -->
```

The bullet is 209 characters. In §8's sidechain bullet, this clause:

```text
It DOES inherit the governing doc and hooks DO fire in it, both measured;
```

becomes:

```text
Hooks DO fire in it, measured;
```

Which charter sections a role agent does hold is the role file's `charter` list, documented in the
roles kit's README, so the charter does not restate it.

### Bytes, measured

Measured on 2026-10-11 by splicing both edits into a CR-stripped copy of each file at `744e55db`
and running `check-template-size.sh` on the copy. PINNED: a sibling landing first moves both, so the
builder re-measures.

| Subject | Before | After | Delta | Ceiling | Headroom after |
|---|---|---|---|---|---|
| `coding-governance-agents.template.md` | 48800 | 49006 | +206 | 49152 | 146 |
| `AGENTS.md` | 54628 | 54795 | +167 | 64512 | 9717 |

The bullet costs 210 bytes and its fence 39, which do not reach `AGENTS.md`; the §8 clause gives
back 43 in both. The longest line in the edited template stays the existing 448-byte one.

### Inventory

None minted. The fence reuses the renderer's existing `kit:` namespace, and `roles` is the kit id
`TOOL-aOrientedCast-1` mints.

### Files touched (estimate)

`coding-governance-agents.template.md` · `AGENTS.md` · `.governance/deploy.toml` · `tools/template-size-highwater.txt` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Edit the template and gov's `kits` array, then re-render with
  `bash tools/playbook/adopt-playbook.sh --target .`.
- Re-record both high-water rows with `bash tools/check-template-size.sh --bump` and
  `bash tools/check-template-size.sh --bump AGENTS.md`.
- Re-stamp `last-audit` in the same commit, naming its parent, as the staged manifest leg demands.
- The playbook kit's marker and banner move to v3.7 once, in the run's mint commit after the last
  unit, with `AGENTS.md` re-rendered there; this unit's commit leaves both at v3.6.
- Adopters receive the bullet at their next re-render. The fence keeps it out of a charter whose
  target did not select the roles kit, and the roles kit's default membership is what selects it.

### Alternatives rejected

- **An unfenced bullet.** It saves 39 bytes and is false in every target without the roles kit,
  where it also names a README that is absent. `PLAY-aRoutedQuill-1` §8 F1 was resolved by the owner
  the other way for the same reason: a kit-conditional rule is fenced by the entry that ships it.
- **Fencing by `agent-cap`.** The hooks kit carries the role arms, but they arm only where the role
  index exists, so an `agent-cap` target without the roles kit would render a rule nothing there
  makes true.
- **A §0 TL;DR bullet.** About 110 bytes the template does not have to spare, and it restates §1.
- **Keeping the §8 clause and qualifying it** ("unless its role omits it"), which is true and costs
  22 bytes more than it does today. The qualification is the roles README's to state, beside the
  role files that set it.
- **Stating the workflow catalogue or the admission rules in the charter.** Prose beside the source
  that owns a value rots.
- **Funding the bullet by trimming another passage.** No passage was found that this rule makes
  redundant; the only one it falsifies is the §8 clause, which S2 already takes.

## 5. Production-readiness checklist

- security — no code. The bullet states a delegation rule; the gates that enforce it are other units.
- perf / scale — the template spends 206 of its 352 free bytes and is left 146 under the ceiling;
  every session reads 167 more bytes of `AGENTS.md`.
- error / empty / loading states — a target that did not select the roles kit renders no bullet,
  rather than a rule that is false for it.
- observability — N/A — prose; the refusals that enforce it are the role-aware write gate's and the
  spawn guard's.
- risks — the next charter edit has 146 bytes, so it will need a trim or an owner raise. The fence
  binds this unit to the `roles` registry entry's order (§8 F1).
- testing — the size, line-length, parity, render, placeholder and manifest legs; no new arm.
- migration — adopters receive the bullet when their charter is re-rendered, which `govkit update`
  runs by default; the fence keeps it out of a charter whose target lacks the kit.
- user docs — the charter is the user doc, and the roles kit's README is what it points at.

## 6. Acceptance criteria

- **AC1** — When `grep -n "Every agent is handed a rendered role" coding-governance-agents.template.md AGENTS.md`
  runs, each file shows the bullet once, directly after the write-gate bullet in §1's Definition of
  Ready; and `grep -c "It DOES inherit the governing doc" coding-governance-agents.template.md AGENTS.md`
  returns 0 for each file while `grep -c "Hooks DO fire in it, measured;"` returns 1 for each.
  Red when: either file lacks the bullet or still carries the inheritance clause.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, the region matches a
  fresh render and `grep -c "kit:roles" AGENTS.md` returns 0.
  Red when: the region drifts, a fence marker reaches the render, or the render refuses the fence
  because `roles` is not a registry entry.
  fixture: the `roles` registry entry, which `TOOL-aOrientedCast-8` registers at order 7, before this
  unit (§8 F1).
- **AC3** — When `adopt-playbook.sh --target` renders two scratch fixtures under a short `%TEMP%`
  root, one whose `deploy.toml` `kits` omits `roles` and one that keeps it, the first renders the
  bullet 0 times and the second once, and both render the write-gate bullet exactly as their
  `agent-cap` selection says.
  Red when: the bullet survives for a target without the roles kit, or is dropped for one with it.
  cost: two scratch fixture repositories holding a `deploy.toml` and the template.
- **AC4** — When `bash tools/check-template-size.sh` and `bash tools/check-template-size.sh AGENTS.md`
  run after the bump, each prints OK with no high-water warning, at 49006 and 54795 bytes or their
  re-measured values.
  Red when: either subject is over its ceiling or warns past its high-water.
  figure: PINNED on 2026-10-11 at `744e55db`; the builder re-measures after any sibling lands.
- **AC5** — When `bash tools/check-line-length.sh` and `bash tools/check-playbook-parity.sh` run,
  both report clean.
  Red when: a new line passes 450 characters, or the parity gate reds the `roles` kit as named
  nowhere.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs after the unit's commit, it
  passes, and that commit's `last-audit` line differs from its parent's.
  Red when: check 5 reds a watched change with no re-stamp, or check 9 reds on a stalled body.
- **AC7** — When `python tools/govkit/govkit.py epoch --base 646d4a73` runs on the unit's commit, the
  `playbook` row reads owed and not `broken`; after the run's mint commit it reads `clean`, and
  `adopt-playbook.sh --target . --check` passes there.
  Red when: the row reads `broken`, or the minted region disagrees with a fresh render.
  permission: the second half is observable only after the run's mint commit, which the main loop
  owns.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook parity` · `playbook render wiring` · `playbook placeholder catalogue` · `agent-instructions wiring` · `agent-cap restatement` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `dead-path carriers (deleted files still named)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm.

## 8. Open questions

- **F1 — The `roles` registry entry the fence names is ordered after this unit. Which order holds?**
  The brief gives the registry entry to `TOOL-aOrientedCast-8` at order 8 and this unit order 7, and
  the renderer refuses a `kit:` fence or a `kits` member naming a non-entry, so AC2 cannot pass at
  this unit's pass.
  (a) Swap the two orders: `TOOL-aOrientedCast-8` to `order 7` and this unit to `order 8`, both
  headers edited at the cross-read, and the Edges above unchanged. Neither unit depends on anything
  at the other's old step, and the two enforcement units stay last at 9 and 10.
  (b) Keep both orders and have `TOOL-aOrientedCast-1` register the `roles` entry at order 1 with the
  kit. Its spec, as written beside this one, hands the entry to `TOOL-aOrientedCast-8` and accepts
  an unclaimed directory until then, so (b) needs that spec amended as well as both Edges lines here
  and in `TOOL-aOrientedCast-8`.
  (c) Keep both orders and land the fenced template text here without re-rendering, leaving gov's
  `kits` array, the render and the `AGENTS.md` high-water to `TOOL-aOrientedCast-8`. That splits one
  mechanism across two units and leaves the render leg red between them.
  Recommendation: (a). It moves two headers and no content, every other unit's order and edges stay
  as written, and neither unit depends on anything at the other's old step. The header verbs here
  still read the roster's orders, because the roster is the build plan's and the cross-read of the
  whole set is where a plan moves; the two order joins of check 12 red until it does.
  RESOLVED (agent, 2026-10-11, delegated): (a). The M2 cross-read decided it as the option with the
  fewest open questions: it moves two headers and no content. This unit builds at order 8 and
  `TOOL-aOrientedCast-8` at 7.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §3 · AC2 · the M2 cross-read's finding 11: the header reads `order 8` and §8 F1
  is resolved to option (a). The Edges sentence and AC2's fixture line, which said the registry entry
  is ordered after this unit, now say it lands at order 7, before it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "state in the charter template a kit-fenced rule that
agents are handed rendered roles and the main loop delegates spec writing, review and building"`
ranked name-token neighbours (`write`, `build`, `kit_rel`, `resolve_kit_dir`) and no seam for
charter prose. The seam reused is the renderer's `kit:` fence in `tools/playbook/render_playbook.py`,
which the template already uses for the agent-cap, codebase-map and unattended rules, and the
`<prefix>/<kit>/` pointer convention the parity gate already reads. No code is written.

Recall terms used: `charter template kit fence render AGENTS.md high-water ceiling
governance-template marker Definition of Ready delegate role` — which surfaced
`PLAY-aRoutedQuill-1` and its fenced write-gate bullet, `PLAY-dDerivedDocket-1`'s net-negative
charter edit, `TOOL-dSpentCeiling-4` and `TOOL-dFoldedVerdict-7` on pricing growth against a
recorded high-water.
