# PLAY-aRoutedQuill-1 — the charter's Definition of Ready: every product-code unit carries a spec before code

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams playbook · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The charter's §1 Definition of Ready asks for a written spec only for a large Tier-2 feature, and it
names no gate that refuses an unspecced write. Owner decision D3 makes every product-code write need
a specced unit. This unit states that rule in the DoR: every product-code unit commits a spec before
code, a Tier-1 unit's being the micro-spec `TOOL-aRoutedQuill-1` defines, and a write gate refuses
the rest where the target ships one. It stays inside the template's byte ceiling and keeps the Tier-2
design pass as the owner ruled it.

## 2. Scope (IN)

- **S1** — Lines 37 and 38 of `coding-governance-agents.template.md` become the four bullets in
  §4 "The new text": a spec-before-code bullet carrying the Tier-1 micro-spec, a `Tier-2:` bullet
  carrying the design pass and its production-readiness menu word for word, the scope-approval
  bullet unchanged, and a write-gate bullet inside a `kit:agent-cap` fence. The bullet opener
  `Large new feature (a Tier-2 change)` and the parenthetical `a written spec (goal · scope ·
  non-goals · acceptance)` are retired; the spec-shape pointer moves into the first bullet.
  **Readers:** by name: `coding-governance-agents.template.md`, the source, and `AGENTS.md`, its
  render; a git grep over the tools, skills, hooks and harness-settings trees on 2026-10-09 found
  no script, test or hook spelling either phrase. by value: NO VALUE READERS, because no checker
  extracts this bullet's text: the value pairs of the playbook parity gate read other lines, and the
  size and line-length legs measure lengths only.
  Observed by AC1, AC4 and AC5.
- **S2** — `AGENTS.md` is re-rendered from the template. The write-gate bullet survives in gov's
  render because gov selects `agent-cap`, and the fence marker lines do not reach the render.
  Observed by AC2 and AC3.
- **S3** — Both size subjects re-record their high-water in `tools/template-size-highwater.txt`
  with `--bump`, so the growth is priced rather than warned about. Observed by AC4.
- **S4** — The kickoff manifest's Tier rule (`memory/guides/SESSION-KICKOFF.md:205-207`) gains
  the micro-spec, reading `Tier 1 (a micro-spec before building, then gates + one focused
  self-review)`. That is a body change, so `last-body-change` advances to the commit making it, in
  the follow-up commit that also re-stamps `last-audit`. Observed by AC6.
- **S5** — The template's version marker moves once for this build, by the route §8 F2 settles,
  and the landed `AGENTS.md` region equals a fresh render after it moves. Observed by AC7.

## 3. Non-goals (OUT)

- What a micro-spec holds and how check 12 grades it: `TOOL-aRoutedQuill-1`.
- How the write gate decides, and the statuses it admits: `TOOL-aRoutedQuill-2`. The charter states
  the rule, not D6's status table, which would be a second copy of the gate's contract.
- Shipping or wiring the gate at adopters: the build's adopter-default unit.
- The Tier-2 menu's words. `PLAY-aMendedFleet-6` ruled that the design pass keeps the full Tier-2
  spec, and this unit moves the menu between bullets without editing it.
- §0's TL;DR. §4 "Alternatives rejected" says why it stays as it is.
- §8's review tiers at template line 230. A review tier is a different question from whether a
  spec exists, and that line stays true.
- An archive snapshot of v3.4 or v3.5. Neither was archived when it was superseded, and git holds
  both.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-1` — the micro-spec's name and its required sections, which
  the first bullet points at through `TEMPLATE-SPEC.md`; without it the DoR names a profile nothing
  grades.
- **consumes-from** `TOOL-aRoutedQuill-2` — the write gate in `scratch-guard.js` that the fenced
  bullet names; without it the bullet states a refusal nothing makes.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- The DoR is `coding-governance-agents.template.md:32-41`. Line 37, the Tier-2 bullet, is 462
  bytes and 449 characters against a 450-character limit (`tools/line-length-limits.txt`), so it
  cannot grow and the new rule has to be a bullet of its own.
- `bash tools/check-template-size.sh` reports the template at 48597 of 49152 bytes, 555 under, with
  a high-water of 48597. `AGENTS.md` is 54472 of 64512 and already 95 bytes past its 54377
  high-water before this unit, which the advisory warning reports today.
- The header banner reads `v3.4` (`coding-governance-agents.template.md:3`) and the marker reads
  `governance-template: v3.5` (`:9`). The marker is the `playbook` entry's version
  (`tools/govkit/entries/playbook.kit.toml:6`). The landing merge `26a803ea6` moved the marker from
  v3.4 to v3.5 and left the banner.
- The lander mints a moved entry and runs only that entry's `[[regenerate]]` argvs
  (`tools/govkit/govkit.py:12504-12517`, `:12360-12373`). The `playbook` entry declares none; the
  `AGENTS.md` region is written by the separate `playbook-render` entry's regenerate
  (`tools/playbook/kit.toml:53-55`). At `26a803ea6` the `playbook-render` entry was minted as well,
  1.22 to 1.23 (`tools/playbook/render_playbook.py:1106`), so its regenerate ran. Whether anything
  re-renders `AGENTS.md` after a mint of the marker alone is UNVERIFIED.
- `tools/check-playbook-parity.sh:256` extracts every template line spelling `matcher` and then a
  backticked word, and compares it with `.claude/settings.json`. A new line spelling one would make
  that pair disagree, so the new text spells none.
- `.governance/deploy.toml:21` selects `agent-cap`. The renderer refuses a `kit:` fence that names no
  registry entry; `agent-cap` is `tools/hooks/kit.toml:3` and ships `scratch-guard.js` (`:56`).
  `grep -c "<!-- kit:" AGENTS.md` returns 0, so fence markers never reach the render.
- `memory/guides/SESSION-KICKOFF.md:6` watches the template. Three watched non-merge commits sit
  after `last-body-change` today, and manifest check 9 reds at ten; this build adds several, so S4's
  body change also resets that count.

### The new text

Template lines 37 and 38 become these six lines, in this order:

```markdown
- Spec before code: every product-code unit commits a spec in the memory-kit `TEMPLATE-SPEC.md` shape (check 12) first; a Tier-1 unit's is a micro-spec — what and how, when it is done, out of scope, how to verify.
- Tier-2: the DoR *is* a design pass — the full spec + a bounded production-readiness menu (best-practice implementation, the extra tools it needs, and the cross-cutting concerns: security · perf/scale · a11y · i18n · error/empty/loading states · observability · testing/gates · migration/rollback · `{{HELP_DIR}}` docs).
- Surface that menu and **get scope approval BEFORE building** (a menu to select from, not scope-creep licence); record the agreed spec per §6.
<!-- kit:agent-cap -->
- A write gate refuses a product-code write that no specced unit owns.
<!-- /kit:agent-cap -->
```

The longest line is 321 characters. The `<!-- kit:codebase-map -->` fence that follows at today's
line 39 is untouched.

### Bytes, measured

Measured on 2026-10-09 by splicing the six lines into a copy of each file at base and running
`check-template-size.sh` on the copy. PINNED: a sibling landing first moves both, so the builder
re-measures.

| Subject | Before | After | Delta | Ceiling | Headroom after |
|---|---|---|---|---|---|
| `coding-governance-agents.template.md` | 48597 | 48800 | +203 | 49152 | 352 |
| `AGENTS.md` | 54472 | 54628 | +156 | 64512 | 9884 |

The template's two DoR lines were 608 bytes and the six are 811. The fence markers are 47 of the
203, and they do not reach `AGENTS.md`. Near-zero growth was not reachable without editing the
Tier-2 menu; the cheapest cut found, pointing the menu at the spec template's §5, is in
"Alternatives rejected".

### Inventory

None minted. The fence reuses the renderer's existing `kit:` namespace, and "micro-spec" is the
profile name `TOOL-aRoutedQuill-1` mints.

### Files touched (estimate)

`coding-governance-agents.template.md` · `AGENTS.md` · `tools/template-size-highwater.txt` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Edit the template, then re-render with `bash tools/playbook/adopt-playbook.sh --target .`.
- Re-record both high-water rows with `bash tools/check-template-size.sh --bump` and
  `bash tools/check-template-size.sh --bump AGENTS.md`. The second also absorbs the 95 bytes the
  charter grew before this unit, and the commit message says so.
- Edit the manifest's Tier rule and re-stamp `last-audit` in the same commit, as the pre-commit
  manifest ratchet demands for a staged watched file. A follow-up commit advances
  `last-body-change` to that commit's sha, since a commit cannot name its own.
- The version moves once for the playbook kit. This unit is the build's only one touching the
  template, so whichever route §8 F2 picks is also the last. Under F2 (b) the bump rides the last
  commit that edits the template, and `AGENTS.md` is re-rendered in that same commit.
- It lands at order 4, after the profile and the gate it names exist; D4 puts it in force on
  landing.

### Alternatives rejected

- **Appending the rule to the Tier-2 bullet.** That line has one character of headroom.
- **A §0 TL;DR bullet.** Measured at 106 bytes, it restates §1, and the write gate enforces the
  rule mechanically; one fact in one place.
- **Pointing the Tier-2 menu at the spec template's §5 rows.** It saves about 230 bytes and removes
  a list that already differs from gov's own `READINESS_ROWS`, but it rewrites the menu
  `PLAY-aMendedFleet-6` kept. A candidate for its own unit, not for this one.
- **Stating D6's admission statuses in the charter.** They are the gate's contract, and prose
  beside the source that owns a value rots.
- **An unfenced gate clause.** §8 F1.

## 5. Production-readiness checklist

- security — no code. The bullet describes a refusal the gate makes and grants nothing.
- perf / scale — 203 bytes of the template's 555 of headroom; the line-length limit holds.
- error / empty / loading states — a target that did not select the gate's kit renders no gate
  bullet, rather than a rule that is false for it.
- observability — N/A — prose; the gate's refusal message is `TOOL-aRoutedQuill-2`'s.
- risks — the minted marker may not reach `AGENTS.md`; §4 "Evidence" and §8 F2.
- testing — the existing size, line-length, parity, render and manifest legs; no new arm.
- migration — adopters receive the new text when their charter is re-rendered, and the fence keeps
  the gate bullet out of a charter whose target lacks the gate.
- user docs — the charter is the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -n "Spec before code" coding-governance-agents.template.md AGENTS.md` runs,
  each file shows the bullet once inside §1's Definition of Ready, followed by the `Tier-2:` bullet
  whose concern list is byte-identical to base's.
  Red when: either file lacks the bullet, or the Tier-2 menu's words changed.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, the region
  matches a fresh render; `grep -c "A write gate refuses" AGENTS.md` returns 1 and
  `grep -c "<!-- kit:agent-cap" AGENTS.md` returns 0.
  Red when: the region drifts, the bullet is missing, or a fence marker reaches the render.
- **AC3** — When `adopt-playbook.sh --target` renders a fixture whose `.governance/deploy.toml`
  kits omit `agent-cap`, the write-gate bullet is absent and the other three bullets are present.
  Red when: the bullet survives for a target without the gate.
  cost: a scratch fixture repo holding a `deploy.toml` and the template.
- **AC4** — When `bash tools/check-template-size.sh` and `bash tools/check-template-size.sh
  AGENTS.md` run after the bump, each prints OK with no high-water warning, at the sizes §4 "Bytes,
  measured" gives or their re-measured values.
  Red when: either subject is over its ceiling, or warns past its high-water.
  figure: PINNED on 2026-10-09 at base; the builder re-measures after any sibling lands.
- **AC5** — When `bash tools/check-line-length.sh` and `bash tools/check-playbook-parity.sh` run,
  both report clean.
  Red when: a new line passes 450 characters, or spells `matcher` and a backticked word.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs after the follow-up commit, it
  passes, and `grep -n "micro-spec" memory/guides/SESSION-KICKOFF.md` shows the Tier rule.
  Red when: the stamp or stall check reds, or the Tier rule still gives Tier 1 no spec.
- **AC7** — When `python tools/govkit/govkit.py epoch` runs on the unit's last commit, the
  `playbook` row reads `clean` under F2 (b) or `owed at the lander` under F2 (a); and after the
  landing, `adopt-playbook.sh --target . --check` still passes on the default branch.
  Red when: the row reads `broken`, or the landed region disagrees with a fresh render.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook parity` · `playbook render wiring` · `playbook placeholder catalogue` · `agent-instructions wiring` · `agent-cap restatement` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm.

## 8. Open questions

- **F1 — Is the write-gate bullet fenced by the kit that ships the gate?** (a) A bullet inside a
  `kit:agent-cap` fence, 118 bytes measured, dropped for a target without that kit. (b) One clause
  appended to the spec-before-code bullet, about 60 bytes estimated, rendered everywhere and false
  wherever the gate is absent. Recommendation: (a). The template already fences kit-conditional
  rules this way, and a rule claiming a refusal that the target's tooling never makes is false in
  that target. The fence id is whichever registry entry ships `scratch-guard.js` when this unit
  builds; it is `agent-cap` today, and if the adopter-default unit moves the gate, this fence
  follows it.
- **F2 — How does the version move, and does the banner move with it?** (a) Leave it to the
  lander's mint: the marker goes to v3.6, the banner stays at v3.4, and `AGENTS.md` keeps v3.5
  unless something re-renders, which §4 "Evidence" could not confirm. (b) Bump in this unit's last
  commit: the marker to v3.6, the banner to v3.6 with that commit's date for zero net bytes, and
  `AGENTS.md` re-rendered in the same commit, so the mint reads `clean`. (c) As (b), but take the
  number out of the banner so only the marker carries it, about 6 bytes saved. Recommendation: (b).
  It is the only route that keeps the template, its render and the banner in agreement with no
  unverified step. (c) is the cleaner end state, and it is a separate charter edit.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "state in the charter template that every unit carries a
spec before code, behind a kit fence the renderer drops"` ranked name-token neighbours (`before`,
`units`, `kit_rel`, `resolve_kit_dir`) and no seam for charter prose. The seam reused is the
renderer's `kit:` fence in `tools/playbook/render_playbook.py`, which the template already uses for
the codebase-map and unattended rules. No code is written.

Recall terms used: `Definition of Ready design pass Tier-2 spec scope approval charter template size
ceiling high-water governance-template marker render AGENTS.md` — which surfaced
`PLAY-aMendedFleet-5` and its ruling `PLAY-aMendedFleet-6`, `TOOL-aScouredKit-23` and
`TOOL-dSpentCeiling-4`.
