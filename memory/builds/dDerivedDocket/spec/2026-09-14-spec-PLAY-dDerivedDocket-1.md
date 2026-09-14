# PLAY-dDerivedDocket-1 — charter backlog wording and unattended landing exception

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams playbook · order 37

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g5-round1.md) | spec-audit | TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Make the charter template stop contradicting the per-build backlog without breaking the adopters
that keep the authored one, and record owner ruling D12-i3: attended landings keep "land on local
main first", and an unattended run lands by its protocol's landing rule. The edit is net-negative in
bytes, paid for inside §1 by deleting reader-facing drop instructions the renderer now executes,
and gov's own `AGENTS.md` is re-rendered and its authored lines describe the switched tree.

## 2. Scope (IN)

- **S1** A new bullet inside the existing `kit:unattended` fence of §1 Landing, directly under the
  explicit-ask substitute, saying an unattended run lands by its protocol's landing rule rather than
  by the local-first bullet above. It is a pointer: it names no lander verb and no lander mode.
  Observed by AC2, AC9 and AC10.
- **S2** The "Unattended runs" block at the end of §1 gets its own `kit:unattended` fence. Its
  "(kit-conditional — drop this block…)" note and the italic "Two independent blocks…" paragraph
  above the kickoff-manifest exception are deleted, because both ask a reader to do what the renderer
  now does. The fence opens directly under the kickoff-manifest bullet, so a dropped block leaves
  one blank line before §2. Observed by AC1 and AC2.
- **S3** §6's record-types bullet reads true in both backlog modes: the backlog keeps stable ids with
  gaps allowed, and where an ask's status lives is the memory tree's rule, reached through §5. The
  words "status updated in place" leave the template. §1's reconcile bullet keeps its wording (§8
  F5). Observed by AC5.
- **S4** Gov's `AGENTS.md`: the `gov:playbook` region is re-rendered with
  `bash tools/playbook/adopt-playbook.sh --target .` in the same commit, and two authored passages
  outside the region describe builds mode. The layout line lists `backlog/<FAMILY>.md` with the
  other GENERATED members, and the node-registry paragraph says asks are filed per build in
  `memory/builds/<slug>/BACKLOG.md` with `memory/backlog/<FAMILY>.md` as their generated view.
  Observed by AC3, AC4 and AC6.
- **S5** One `memory/DECISIONS.md` row under `## PLAY — playbook`, keyed by this unit's id,
  recording D12-i3 as the owner ruled it and the §6 wording change. Observed by AC7.
- **S6** The kickoff manifest's `last-audit` is re-stamped in the same commit with a delta line in
  the commit message, because the template is in the manifest's `watch:` list and the staged leg
  refuses a watched change without one. The §B claims the template feeds are re-read; none is
  expected to change, since the switch-over unit already rewrote the backlog claims. Observed by
  AC8.
- **S7** The net byte budget: the template's CR-stripped size falls at this unit's commit, and
  `AGENTS.md` stays within its declared ceiling. Observed by AC1 and AC4.

## 3. Non-goals (OUT)

- The attended rule is not reworded. "Land on local `{{DEFAULT_BRANCH}}` first, verify, then push"
  stays verbatim, as owner ruling D12-i3 keeps it.
- No landing mechanism in the charter. The in-place sequence, both lander modes and the fallback
  are the unattended protocol's, written by the run's-landing-path unit; D12-i3 says the rule lives
  there.
- No edit to charter §9's default-off rule. The owner overrode it for auto-resume alone, and the
  auto-resume unit records that as a DECISIONS row.
- No memory-tree kit prose, no HYGIENE or TEMPLATE-SPEC text, and no kickoff-manifest claim. The
  memory-tree docs unit and the switch-over own those; this unit only re-stamps the manifest.
- No runbook edit. The runbook's §2 sentence about the unattended blocks is handed off.
- No template version bump and no high-water bump (§8 F6).
- No `when:` block and no new `drop_blocks` name. The fence reuses the `kit:` namespace as it is.
- The root `README.md` is untouched: its memory-tree line stays true, because shards is the kit's
  default mode.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-34` — the switched tree. Gov's authored `AGENTS.md` lines
  describe builds mode only once that commit has made it true, and the manifest claims this unit
  re-verifies are the ones that commit rewrote.
- **hands-off** `DEPL-dDerivedDocket-1` — the runbook's §2 sentence on what selecting the unattended
  kit keeps in §1, which after this unit is two fenced blocks carrying the landing pointer and the
  protocol contract as well as the ask substitute. Added by this spec, not in the brief's table.
- **hands-off** external — offering the in-place landing merge's carry-set check to attended
  landings as an opt-in, which D12-i3's consequences name as possible and nothing in this build owes.

## 4. Design

### The edits, by location

| Where, at BASE | Now | After |
|---|---|---|
| `coding-governance-agents.template.md:55`-`:57`, the `kit:unattended` fence | one bullet: the explicit-ask substitute | that bullet, then the S1 landing bullet |
| `coding-governance-agents.template.md:63`-`:64` | the italic "Two independent blocks…" paragraph | deleted, with its blank line |
| `coding-governance-agents.template.md:70`-`:77` | "**Unattended runs** *(kit-conditional — drop this block…)*" and its bullet, unfenced | "**Unattended runs.**" and the same bullet, inside a `kit:unattended` fence |
| `coding-governance-agents.template.md:148` | "the backlog is mutable (stable ids, status updated in place; gaps fine)" | the S3 wording |
| `AGENTS.md:78`-`:472`, the `gov:playbook` region | the BASE render | a fresh render |
| `AGENTS.md:52`-`:53`, the layout line | `backlog/<FAMILY>.md` listed after the GENERATED pair | listed as the third GENERATED member |
| `AGENTS.md:70`-`:71`, the node-registry paragraph | "backlogs shard per family at `memory/backlog/<FAMILY>.md`" | asks filed per build, and the family file their generated view |
| `memory/DECISIONS.md`, `## PLAY — playbook` | one row | a second row, this unit's |
| `memory/guides/SESSION-KICKOFF.md` audit block | the switch-over's stamp | re-stamped |

### Proposed text

The build may reword inside the constraints S1, S3 and AC10 state. The template passages:

```markdown
<!-- kit:unattended -->
- That explicit ask has ONE substitute: … (unchanged)
- An unattended run lands by its protocol's landing rule, not the local-first one above.
<!-- /kit:unattended -->
…
- The manifest reconciles additively EXCEPT its `last-audit` line — … (unchanged)
<!-- kit:unattended -->

**Unattended runs.**

- The contract is `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`, … (unchanged)
  paraphrase is the copy that rots.
<!-- /kit:unattended -->
(blank line, then the §2 heading, unchanged)
…
- Two record types per stream: the decision log is append-only (never rewrite a ratified record — supersede with a new id + note); the backlog keeps stable ids (gaps fine), and how an ask's status is kept is the memory tree's rule (§5).
```

The decision row, one line of at most 300 characters:

```markdown
- **PLAY-dDerivedDocket-1** — **attended landings keep local-main-first; an unattended run lands by its protocol's rule** (owner, D12-i3). §6's backlog bullet points at the memory tree's status rule, true in both modes. builds/dDerivedDocket/. — _2026-09-14, `d`_
```

### Byte accounting

PINNED: measured 2026-09-14 by applying the proposed text to BASE's template in a scratch copy and
rendering it with `render_playbook.py` for a target that selects the unattended kit.

| Edit | Template bytes | Rendered region bytes |
|---|---|---|
| S1 landing bullet | +89 | +89 |
| S2 italic paragraph deleted | −186 | −186 |
| S2 heading note deleted | −93 | −93 |
| S2 fence markers | +49 | 0, because a surviving block loses its markers |
| S3 §6 bullet | +34 | +34 |
| total | −107, so 48,778 of 49,152 | −156 |

The authored `AGENTS.md` passages in S4 add about 63 bytes, so the charter moves from 64,347 to
about 64,254 of its 64,512 ceiling. The switch-over and the remote-CI unit may change `AGENTS.md`
before this unit runs; AC4 grades the file at this unit's commit rather than trusting this sum.

### Why the fence is safe to add

The renderer's `remove_fenced` drops a fenced block's body and markers for a target that did not
select the kit, and strips only the markers for one that did. `unattended` is already a registry
entry, because the explicit-ask bullet is fenced with it, so no new refusal can fire. Measured at
BASE: a scratch target whose `kits` omit `unattended` receives the unfenced block and its pointer
to `UNATTENDED-PROTOCOL.md`, a protocol that target does not have. With the proposed text it
receives neither.

### Rollout

1. Reground, and confirm the switch-over unit reads CLOSED.
2. Edit the template, then run `bash tools/playbook/adopt-playbook.sh --target .`.
3. Edit the two authored `AGENTS.md` passages and add the DECISIONS row.
4. Re-read the manifest's §B claims the template feeds, then re-stamp `last-audit` by the stamp rule
   the manifest states.
5. Make the §6 observations, then commit with a delta line for the re-stamp in the message.

### Files touched (estimate)

`coding-governance-agents.template.md` · `AGENTS.md` · `memory/DECISIONS.md` ·
`memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **The design's builds-mode sentence in the template.** It tells a shards-mode adopter to write a
  file its own check 4 refuses (§8 F1).
- **The landing clause on the unconditional local-first bullet.** It ships a pointer to a protocol
  into every charter, including those whose repo has none (§8 F2).
- **Trimming rule prose to pay for the clause.** It rewrites rules no ruling touched, while the drop
  instructions are text the renderer has made redundant (§8 F4).

## 5. Production-readiness checklist

- security — no new authority and no new write path. The explicit-ask substitute is unchanged, the
  landing bullet grants nothing, and the fence narrows what a target without the kit receives.
- perf / scale — N/A: prose. Gov's charter, read every session, gets about 90 bytes shorter.
- error / empty / loading states — a target that did not select the unattended kit now receives
  neither unattended block. The renderer refuses an unknown fence name, and `unattended` is known.
- observability — the size gate's `template-size OK` line for both subjects, the render check's
  `region matches a fresh render` line, and the manifest check's check 5.
- risks — the template's high-water record reads 48,378 at BASE against 48,885, so the size gate
  already prints an advisory WARN; this unit shrinks the file by less than that gap and leaves the
  WARN standing. `AGENTS.md` had 165 bytes free at BASE and another unit may spend some first; AC4
  reads the commit. An adopter re-rendering gets the fence and the new §6 wording with no answer
  change in its `deploy.toml`.
- testing — the scratch render with and without the unattended kit, red at BASE and green after;
  the size, render, line-length and manifest observations. No gate arm is added.
- migration — N/A for data. Adopters receive the change when they next re-render their region.
- user docs — the runbook sentence is handed off; the charter is itself the user-facing document.

## 6. Acceptance criteria

- **AC1** — When `tr -d '\r' < coding-governance-agents.template.md | wc -c` runs at this unit's
  commit and at its parent, the first count is lower, and `bash tools/check-template-size.sh` prints
  `template-size OK`.
  Red when: the landing bullet lands without the §1 deletions, which grows the file while it stays
  under its ceiling, so the size gate stays green and only the parent comparison catches it.
  figure: DERIVED at the commit. BASE's 48,885 and the −107 projection are PINNED, measured
  2026-09-14; design §11's 49,032 was measured at `09a22d2b`.
- **AC2** — When `python tools/playbook/render_playbook.py --target <scratch>` renders the template
  for a scratch target whose `kits` omit `unattended`, `grep -c 'UNATTENDED-PROTOCOL'` over the
  rendered `AGENTS.md` prints 0 and the landing bullet is absent; with `unattended` restored, the
  same render carries both.
  Red when: the "Unattended runs" block stays unfenced, which is BASE's state and printed 1 in this
  fixture on 2026-09-14, or the landing bullet sits on the unconditional local-first bullet.
  fixture: a scratch git repository on `main` holding this repo's `.memory-tree.conf`, a copy of
  `.governance/deploy.toml` with `unattended` removed from `kits` and a `playbook_path` answer naming
  a copy of the template, and a stub answer for every placeholder
  `tools/govkit/entries/playbook.kit.toml` declares that the copy leaves unanswered. Built in the
  scratchpad and discarded; the tree holds none.
- **AC3** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs at this unit's
  commit, it prints `render-playbook OK — region matches a fresh render`.
  Red when: the template is committed without re-rendering `AGENTS.md`, so the region still carries
  the deleted drop instructions.
- **AC4** — When `bash tools/check-template-size.sh AGENTS.md` runs at this unit's commit, it prints
  `template-size OK` against the declared 64512-byte ceiling.
  Red when: the authored passages grow and the region is not re-rendered, so their bytes are spent
  against BASE's 165 free bytes with no saving from the region to offset them.
  figure: 64,347 at BASE is PINNED, measured 2026-09-14; the verdict is DERIVED.
- **AC5** — When `grep -n 'status updated in place' coding-governance-agents.template.md AGENTS.md`
  runs it prints nothing, and §6's record-types bullet names stable ids and points at `§5` for where
  an ask's status lives.
  Red when: the design's builds-mode sentence is written into the template, which
  `grep -c 'BACKLOG.md' coding-governance-agents.template.md` reports as non-zero, and a shards-mode
  adopter's re-render then instructs a file its check 4 refuses at
  `tools/memory-tree/check-memory-hygiene.sh:611`.
- **AC6** — When `grep -n 'backlogs shard per family' AGENTS.md` runs it prints nothing, and the
  node-registry paragraph names `memory/builds/*/BACKLOG.md` as where asks are filed and
  `memory/backlog/*.md` as their generated view.
  Red when: only the region is re-rendered and the authored paragraph keeps its BASE wording, which
  contradicts the switched tree the same file's layout line describes.
- **AC7** — When `grep -c '^- \*\*PLAY-dDerivedDocket-1\*\*' memory/DECISIONS.md` runs it prints 1,
  and that row sits between `## PLAY — playbook` and `## KICK — kickoff`, names D12-i3, and is at
  most 300 characters.
  Red when: the row runs past 300 characters, which hygiene check 7's `ENTRY_CAP_CHARS` reds, or it
  is appended at the end of the file under the TOOL group, which no gate catches and the
  between-headings read does.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs at this unit's commit, check 5
  passes and the `last-audit` line in `memory/guides/SESSION-KICKOFF.md` differs from its parent's.
  Red when: the template is committed without the re-stamp, which the staged leg's check 5 refuses
  at pre-commit because the template is in `watch:`.
- **AC9** — When `bash tools/check-line-length.sh` runs, both declared subjects pass at 450
  characters.
  Red when: the landing sentence is appended to the explicit-ask bullet, a 391-character line at
  `coding-governance-agents.template.md:56`, which makes it about 480.
- **AC10** — When the lines of the first `kit:unattended` fence in
  `coding-governance-agents.template.md` are searched with `grep -cE 'in-place|--prepare|--land|LANDER_MODE'`,
  the count is 0, and the landing bullet names the protocol's landing rule.
  Red when: the bullet quotes the consequence text's "in-place landing", which is false for an
  adopter whose lander mode is the kit default and restates the protocol's rule in the charter.

## 7. Gates

`template size <=48KiB` · `charter size` · `playbook render wiring` · `playbook parity` · `playbook placeholder catalogue` · `line length` · `micro-format definitions` · `kickoff-manifest ratchet` · `memory hygiene` · `govkit acceptance matrix`

No new gate arm. The fence is graded by the render and size legs above, and AC2's scratch render is
an observation made once in the unit pass. The bar runs once, on the landing merge.

## 8. Open questions

- **F1** — What does §6 say about backlog status? (a) Design §11's "asks are filed per build; status
  is derived (§5)". (b) A sentence spelling both modes. (c) A mode-neutral pointer to the memory
  tree's rule through §5, with gov's builds-mode facts in gov's authored `AGENTS.md` lines. (a)
  instructs every shards-mode adopter to write a `BACKLOG.md` its own check 4 refuses, and design §6
  keeps that refusal in shards mode, the adopters' default. (b) restates the kit's modes in the
  charter, a second answer that rots when a mode changes. RESOLVED (agent, 2026-09-14, delegated):
  (c). It satisfies every criterion here, leaves no adopter follow-up and costs the fewest bytes.
- **F2** — Where does the landing clause sit? (a) Inside the existing `kit:unattended` fence under
  the local-first bullet. (b) On the local-first bullet itself. (c) Inside the "Unattended runs"
  block. (b) ships a pointer to a protocol into charters whose repo has none. (c) puts the exception
  a screen away from the rule it excepts. RESOLVED (agent, 2026-09-14, delegated): (a).
- **F3** — What does the clause say? (a) D12-i3's consequence text, "per the unattended protocol's
  in-place landing". (b) A pointer to the protocol's landing rule that names no mode. The
  run's-landing-path unit makes the lander mode a declaration whose blank reads `primary`, so (a) is
  false for an adopter on the kit default. RESOLVED (agent, 2026-09-14, delegated): (b). The ruling
  itself, attended local-first kept with a written unattended exception, is RESOLVED (owner,
  2026-09-13) as D12-i3 and is carried out unchanged.
- **F4** — Which bytes pay for the clause? (a) The reader-facing drop instructions around the
  "Unattended runs" block, with the block fenced. (b) Rule prose elsewhere in §1. (c) Prose outside
  §1. (b) rewrites rules no ruling touched, and (c) departs from D12-i3's consequence that bytes in
  §1 pay. RESOLVED (agent, 2026-09-14, delegated): (a). It also removes a measured BASE defect: a
  target without the kit receives the unfenced block.
- **F5** — Does §1's "Reconcile shared mutable files (backlogs, indexes) additively" change, as
  design §11 names it? (a) Change it. (b) Keep it. It is true in both modes: a build's `BACKLOG.md`
  is merged by the row driver, and the family view is the GENERATED index the same bullet already
  says to re-render. RESOLVED (agent, 2026-09-14, delegated): (b), at zero bytes.
- **F6** — Version and high-water. (a) Bump the template to v3.1 and re-record its high-water. (b)
  Neither. `git log -S'Template **v3.0**'` shows the string set once, at the convergence commit, and
  every later rule change kept it; a high-water bump records growth, and this unit shrinks the file.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- The rulings this unit carries out and does not revisit: D1, adopt per-build asks with a derived
  view, and D12-i3, keep local-first for attended landings with an unattended exception, both
  RESOLVED (owner, 2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds one edge the brief's table does not list, the hands-off
  to the runbook unit, `DEPL-dDerivedDocket-1`, for its sentence on the unattended blocks. Departs
  from design §11's wording on two lines (§8 F1, F5) and from D12-i3's consequence text on the
  clause's words (§8 F3), each for a source fact at BASE the design did not have.

## 10. Reuse audit

The seams are the renderer's `kit:` fence namespace, `OPEN_RE`, `CLOSE_RE` and `remove_fenced` in
`tools/playbook/render_playbook.py`, which already drops the explicit-ask bullet for a target
without the unattended kit, and `tools/check-template-size.sh` with its declared ceilings. The probe
`python tools/codebase-map/reuse_lookup.py "keep an opt-in kit's charter rules in a conditional
block the renderer drops"` ranked `check-template-size.sh` under the playbook dossier and returned
the `charter size` leg, and otherwise name-stem neighbours; its coverage line reads `unscanned
layers: .sh`. It did not surface the fence parser, which was found by reading the renderer and is
named in a prior spec audit the recall probe returned. Recall also returned TOOL-aUnmannedHelm-4,
the precedent that made the unattended rules kit-conditional so the byte-gated template gains no
section, and PLAY-dUnstalledConvoy-1, the precedent for editing the template and re-rendering the
region rather than hand-editing the charter. No new seam is built.

Where the design and the source disagree at BASE, re-verified here:

- Design §11 measured the template at 49,032 of 49,152 bytes. At BASE it is 48,885, and its
  high-water record reads 48,378.
- Design §11's replacement sentence for §6 is true only in builds mode. At BASE check 4 admits only
  `README.md`, `RUN.md` and four subdirectories at a build root, and design §6 keeps `BACKLOG.md`
  refused in shards mode (§8 F1).
- Design §11 names the reconcile bullet's "(backlogs, indexes)" for change; it reads true in both
  modes (§8 F5).
- D12-i3's consequence quotes "in-place landing", while the run's-landing-path unit's spec, on disk
  at this writing, makes the lander mode a declaration whose blank reads `primary` (§8 F3).
- The "Unattended runs" block is unfenced at BASE though it tells a reader to drop it. It arrived in
  that shape at the charter's convergence into one file.

M12 was not reached: the owner's ruling and the design chose the mechanism, and each fork above is
wording or placement decided by a measurement or a veto.

Recall terms used: `charter template kit:unattended fence net-negative byte ceiling land local main first exception playbook render`
