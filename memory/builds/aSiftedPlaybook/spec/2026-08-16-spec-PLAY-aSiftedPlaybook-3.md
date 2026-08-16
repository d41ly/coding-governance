# PLAY-aSiftedPlaybook-3 — the playbook learns which kits it ships

**Status:** SPECCED · rev-7 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams playbook · ratified 2026-08-16

## 1. Goal

Several kits under `tools/` are named nowhere in the three shipped playbook files, so an
adopter's instantiated ruleset never mentions capabilities the deploy runbook installs for them, and
the customize companion's deletion checklist cannot tell them what to remove if they decline one.
Give each a template placement and a conditional-section row.

## 2. Scope (IN)

- **S1 — `drift-audit`.** A §5 bullet in the shape of the existing kit bullets (~645 bytes).
  `WIRE-INTO-PROJECT.md §3d` installs it as "optional, recommended"; the ruleset it installs into
  never mentions records-vs-reality auditing at all.
- **S2 — `pytest-parallel-guardrails`.** A §7 bullet (~527 bytes) plus a two-clause append at
  `parallel-coding-governance.domain-rules.md:87-88` naming the kit (~130 bytes). Those two §10
  bullets already encode, in full, the exact bug classes this kit exists to fix — the xdist
  worker-death attribution class and the aiosqlite closed-loop seam — while telling the reader
  nothing about the shipped fix. §7 rather than §5 because it is a gate-discipline concern, not a
  memory one.
- **S3 — `agent-instructions`.** A §6 bullet (~421 bytes). `customize.md:12-13` currently orders the
  deploying agent to write the filled template into "`AGENTS.md` / `CLAUDE.md`" without naming the
  kit that wires that pair. **An adopter who writes only `AGENTS.md` ships a repo Claude Code cannot
  read**, because Claude Code does not read `AGENTS.md` natively — which is the entire reason the
  kit exists. This is the highest-consequence omission of the four.
- **S4 — `gate-lint`.** A fourth absent kit the audit did not catch. Its README describes it as
  "project-agnostic", "drop-in", with "a two-line adoption step" and no gate legs of its own — an
  adopter-facing product by its own description. It is absent from the trio **and from `AGENTS.md`
  and `README.md` entirely**, so the charter does not know it ships. In scope: the template
  placement, the customize row, the charter's kit list in `AGENTS.md`, **and the shipped-contents
  list in root `README.md`** — that last one was named as part of the defect and then silently
  dropped from scope, which is how a defect becomes lost rather than deferred.
- **S5 — the customize conditional rows.** One per kit (~685 bytes total), in that file's existing
  voice, stating what to delete when the kit is declined.
- **S7 — the exemption registry.** `tools/playbook-kit-waivers.txt`, seeded with the kits that are
  legitimately not adopter-facing and a reason each, modelled on `tools/install-prefix-waivers.txt`.
  **This unit creates it; `TOOL-aSiftedPlaybook-3` consumes it and never adds a row.** Without it
  AC1 quantifies over a "declared exempt set" that exists only as prose inside this spec, which no
  builder can observe and no later gate can read.

  **Seed with `lib/` and `hooks/` ONLY — not `workflows/`.** Measured against the trio under
  `TOOL-aSiftedPlaybook-3` S1's own anchored path-segment rule: `lib` scores 0 (all seven apparent
  hits are the substring inside "deliberate"), `hooks` scores 0 (its one mention is the English
  word), but **`workflows` scores 1** — `parallel-coding-governance.template.md:150` spells
  `tools/workflows/tier2-review.js`. A waiver for a kit that already passes excuses nothing, and
  the stale-row arm only reds a row whose kit is GONE, so a redundant one would sit there until
  `TOOL-aSiftedPlaybook-3` AC6's second arm reds it as excusing nothing.

  **The registry is a declared exemption list, not a shrink-only count.** It must be able to gain a
  row for a genuinely experimental kit — that is the escape hatch `TOOL-aSiftedPlaybook-3` §8 F2
  depends on now that a missing kit REDS. It drains through that unit's two AC6 arms instead: a row
  whose kit is gone, and a row whose kit is named in the playbook, both red. This is the one place
  it diverges from `tools/install-prefix-waivers.txt`, which is shrink-only and can only lose rows.
- **S9 — `govkit`, the twelfth kit.** It arrived from main after this unit was drafted and is the
  deployer — arguably the most adopter-facing kit in the tree. It gets the same treatment as S1-S4:
  a template placement in the section that owns its concern, plus a customize conditional row.
  Without a disposition, AC1 is false at this unit's own DoD and `TOOL-aSiftedPlaybook-3` AC1 reds
  the merge bar the day unit 7 lands.
- **S10 — the closing `--bump`** (`TOOL-aSiftedPlaybook-1` B3). This is the last template-touching
  unit, so it owns returning the size ratchet to quiet: run the gate's `--bump` after S1-S4 and S8
  have landed, so `tools/template-size-highwater.txt` records the template's final size. Units 5 and
  6 are expected to fire the warn before this; that is the ratchet working, not a defect.
- **S8 — the version marker and the archive snapshot.** Both deploy files carry
  `<!-- governance-template: vN.N -->` and are re-pulled in lockstep:
  `parallel-coding-governance.template.md:12` and `parallel-coding-governance.domain-rules.md:3`
  move v2.7 → **v2.8**, and the pre-bump template is copied to
  `memory/archive/parallel-coding-governance.template-v-2-7.md` (the archive holds `-v-2-0` through
  `-v-2-6` and no v-2-7 today). The template's own header paragraph gains the v2.8 line describing
  what changed.

  **This unit owns it because it is the last template-touching unit in the build order**, per the
  README's ordering. The obligation was previously stated only as a build-level rule in the README
  and appeared in no spec — so a builder working these acceptance criteria would have shipped a
  v2.7 marker over v2.8 content and passed every check.
- **S6 — two broken cross-references found alongside.** `WIRE-INTO-PROJECT.md:81` cites a §2a
  section for the agent-instructions install **that does not exist**, and
  `tools/gate-lint/README.md:35` cites `parallel-coding-governance.domain-rules.md §14` for the
  observed-failing-case rule — the companion has no §14 and the rule is §7:44-45. Both are
  adopter-facing dead pointers into the files this unit is already editing.

## 3. Non-goals (OUT)

- **Making the kit list machine-checked.** `TOOL-aSiftedPlaybook-3`. This unit fixes the population
  once; that one keeps it fixed.
- **Adding a gate leg for `gate-lint`.** Its README says the consuming project owns the legs, and
  whether gov itself has PowerShell worth scanning is a separate question. Follow-up row.
- **Rewriting `WIRE-INTO-PROJECT.md`'s section numbering.** S6 corrects one dead reference; the
  runbook's structure is not in scope.

## 4. Design

### The invariant is not the one the audit assumed

The audit's framing was that every optional kit gets both a §5 bullet and a customize row.
**That is false**: the `unattended` kit has no §5 bullet at all — it is reached through §1's Landing
clause and companion §1. The true invariant is weaker and more useful:

> Every kit an adopter can install has (a) a placement in the template section that owns its
> concern, and (b) a row in the customize conditional-sections list.

Stated because an acceptance criterion written against the false invariant would demand a §5 bullet
for kits whose concern is not memory, and would have been wrong for two of the four.

### The population is machine-enumerable, so the acceptance criterion quantifies over it

The kit population is DERIVED, never spelled: at HEAD
`git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u` returns **twelve**, one more than
when this unit was drafted — `govkit` arrived with the merge at `8712ac0`. A hardcoded count inside
the unit that exists to close hardcoded counts is the same defect, so no count is stated here. The same derivation is already used twice —
`tools/codebase-map/map_extractors.py` (feeding the `kits` inventory in `inventories.json`) and
`check-install-prefix.sh:38`'s kit-name alternation — so AC1 quantifies over that enumeration rather
than over a list of four, which would go stale the moment a twelfth kit lands. **Two** kits are legitimately not adopter-facing and belong on the exemption side: `lib/`
(gov-internal, ships nothing, per `AGENTS.md`) and `hooks/` (reached through §8's `agent-cap.js`).
`workflows/` is NOT among them — measured, it already scores a path-segment hit at
`parallel-coding-governance.template.md:150` (`tools/workflows/tier2-review.js`), so a waiver for it
would excuse nothing and `TOOL-aSiftedPlaybook-3` AC6's second arm would red it as redundant.

### Cost, and why this unit alone needs the ceiling raise

| Item | Bytes | Gated? |
|---|---|---|
| S1 drift-audit §5 bullet | ~645 | yes — template |
| S2 pytest-guardrails §7 bullet | ~527 | yes — template |
| S3 agent-instructions §6 bullet | ~421 | yes — template |
| S4 gate-lint bullet | ~450 | yes — template |
| S2 domain-rules §10 append | ~130 | no |
| S5 customize rows | ~685 | no |
| S8 the v2.8 header entry | ~230, measured against the v2.7 entry | yes — template |
| S9 govkit bullet | measure at build time | yes — template |

The gated subtotal is roughly **2043 bytes against 86 free at BASE**. Unlike
`PLAY-aSiftedPlaybook-2`, there is no cheaper naming that makes this fit: the content IS the cost.
**This unit is the one that genuinely requires `TOOL-aSiftedPlaybook-1` to land first**, and it is
the clearest single justification for the owner's raise.

### A prior review refuted this, and the ground it was refuted on is being removed

`memory/builds/aCandidStub/reviews/2026-08-10-review-aCandidStub-1.md:222-224` raised this exact
omission as finding id 19 and **refuted it on THREE grounds**: no line claims the kit menu is
exhaustive; each bullet is individually true; and the template is at its ceiling. Its dispositive
framing — "an omission, not a contradicted claim" — rests on the first two, which the raise does not
touch. **Only the third ground is removed.**

The case for landing now is therefore not "the objection is gone". It is that the ceiling was the
practical blocker, and that S1-S4 change the thing the other two grounds were about: they stop
treating §5 as a menu that happens to be non-exhaustive and give each kit a placement in the section
that owns its concern. A reader is then entitled to infer coverage, which is exactly what id 19 said
they could not. The build's decision row cites id 19 in those terms — overstating it as "the only
blocking objection" would write a mischaracterization into a record the repo declares append-only.

### Files touched (estimate)

| File | Items |
|---|---|
| `parallel-coding-governance.template.md` | S1 §5, S2 §7, S3 §6, S4 |
| `parallel-coding-governance.customize.md` | S5, and S3's fill instruction at `:12-13` |
| `parallel-coding-governance.domain-rules.md` | S2's §10 append |
| `AGENTS.md` | S4's charter kit list |
| `README.md` | S4's adopter-facing shipped-contents list |
| `WIRE-INTO-PROJECT.md` | S6's dead §2a reference |
| `tools/gate-lint/README.md` | S6's dead §14 reference |
| `tools/playbook-kit-waivers.txt` | S7, new — seeded with `lib` and `hooks` only |
| `tools/govkit/registry.toml` | + row — S7's new depth-1 path must be declared or `govkit selfcheck` reds |
| `tools/template-size-highwater.txt` | S10's closing `--bump` rewrites it |
| `parallel-coding-governance.template.md` `:12` · `.domain-rules.md` `:3` | S8, the v2.8 marker in lockstep |
| `memory/archive/parallel-coding-governance.template-v-2-7.md` | S8, new — the pre-bump snapshot |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp — the template is a watched pathspec |

### Alternatives rejected

- **A single "other kits" bullet listing all four.** Rejected: it puts a memory kit, a gate kit, a
  wiring kit and a lint kit under one heading, so no reader loading §7 for gate work learns about
  the gate kit. The template's routing is by concern, and the whole defect is that these kits are
  unroutable.
- **Deferring `gate-lint` because the charter does not list it.** Rejected: that is the defect, not
  a reason to preserve it. A kit tracked, README'd and described as project-agnostic is shipping
  whether or not the charter has noticed.

## 5. Production-readiness checklist

- security — N/A directly. S3 has an indirect angle: an adopter whose `CLAUDE.md` is unwired runs
  with no governing doc loaded at all, which silently disables every rule in it.
- perf / scale — the template grows ~2 KB, read every session. Real but small, and F1 addresses
  whether it should be smaller.
- a11y / i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — **drafted bullets are prose about kits the author did not build.** Each must be checked
  against its kit README by someone reading the README, not the draft; a confidently wrong bullet is
  worse than an absent one because it will be believed and will not be re-derived.
- testing + left-shift gates — `TOOL-aSiftedPlaybook-3`, which is the whole reason it exists.
- migration / rollback — an adopter re-pulling gains four bullets and four deletion rows.
- user docs — these files ARE the docs.

## 6. Acceptance criteria

- **AC1** — When the tracked kit dirs under `tools/` are enumerated, every one is either named in at
  least one of the three playbook files (matched as a path segment, never a bare substring), or
  listed in `tools/playbook-kit-waivers.txt` with a reason. The enumeration is the machine one, not
  a hand-list, and the waiver file is the artifact S7 creates — an AC that quantified over a set
  declared only in this spec's prose would be unobservable.
- **AC2** — When `parallel-coding-governance.customize.md`'s conditional-sections list is read,
  every kit named in the template has a row saying what to delete when it is declined.
- **AC3** — When each new bullet is read against its kit's own README — `tools/drift-audit/README.md`,
  `tools/pytest-parallel-guardrails/README.md`, `tools/agent-instructions/README.md`,
  `tools/gate-lint/README.md` — every claim it makes is present there. Checked per kit, by reading
  the README rather than the draft.
- **AC4** — When `grep -n '§2a' WIRE-INTO-PROJECT.md` runs it returns nothing, and when
  `tools/gate-lint/README.md:35` is read it cites §7 rather than §14.
- **AC5** — When `bash tools/check-template-size.sh` runs, it exits 0 against the raised ceiling and
  reports the measured size read FROM the gate.
- **AC6** — When `bash tools/run-gates.sh` runs, every leg is green.
- **AC9** — When the kit population is re-derived with
  `git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u`, every member is either named
  in a playbook file or present in `tools/playbook-kit-waivers.txt`. Quantified over the derivation,
  never over a count — a twelfth kit arrived mid-build and a spelled number would not have noticed.
- **AC10** — When `python tools/govkit/govkit.py selfcheck` runs, it is green with
  `tools/playbook-kit-waivers.txt` declared in `tools/govkit/registry.toml`.
- **AC11** — When `bash tools/check-template-size.sh` runs after S10's `--bump`, it prints no warn
  line. This is the observation `TOOL-aSiftedPlaybook-1` AC9 could not make from unit 1.
- **AC8** — When `grep -n 'gate-lint' AGENTS.md README.md` runs, both carry a `gate-lint` entry in
  their shipped-kit lists. Without this AC a builder can skip the charter half of S4 entirely and
  pass: AC1 quantifies over the three playbook files and the waiver registry, AC2 over
  `customize.md`, AC3 over kit READMEs, AC4 over cross-references, and the drift signal §7 leans on
  matches gate-leg argv paths, not kit bullets in "What ships here".
- **AC7** — When `grep -n 'governance-template:' parallel-coding-governance.template.md
  parallel-coding-governance.domain-rules.md` runs, both read `v2.8`, and
  `memory/archive/parallel-coding-governance.template-v-2-7.md` exists and is byte-identical to the
  template as it stood before this build's first template edit. Checking only one of the two markers
  is the drift the lockstep re-pull rule exists to prevent.

## 7. Gates

- `bash tools/check-template-size.sh` — this unit spends ~2 KB of the new headroom.
- `bash skills/session-kickoff/manifest-check.sh` — the template is watched; re-stamp.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `python tools/drift-audit/drift_report.py --check` — `AGENTS.md` gains a kit; confirm no hand-kept
  inventory signal moves.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — the fork below is RESOLVED (owner, 2026-08-16).

- **F1 — do the four bullets go in the template, or behind §-stubs in the companion?**
  **RESOLVED (owner, 2026-08-16): option (a) — all four INLINE in the template.** S1-S4, §4's cost
  table, §4's ordering conclusion and AC5 are already written for inline, so no scope changes; the
  agent recommendation had been (b) and is not taken. Discoverability wins over per-session read
  cost: a session loading §7 for gate work meets the gate kit there. The ~2 KB is spent knowingly,
  and `TOOL-aSiftedPlaybook-1` S8's high-water ratchet is what will price the next such spend.

  The original framing:

  **The template
  is read every session; a kit roster is reference material consulted at adoption time and rarely
  after. Putting ~2 KB of kit descriptions into the per-session read is the cost the old ceiling
  existed to prevent, and the raise makes it possible without making it wise.
  Options: (a) all four inline, as specced; (b) one-line pointers in the owning sections plus a
  companion §5a holding the descriptions; (c) inline for the three that change how work is done
  (drift-audit, pytest-guardrails, agent-instructions) and companion-only for `gate-lint`, which
  applies only to projects with PowerShell.
  **Recommendation: (b).** It is the v2.3 pattern the template already uses nine times, it keeps the
  per-session read flat, and it survives a twelfth kit. This is a real fork and it is the owner's,
  because it trades discoverability against per-session cost and the raise has just moved the price
  of that trade.

## 9. Revision log

- rev-7 · 2026-08-16 · folded round-3 L4 and L5. The cost table priced S1-S5 only while
  `TOOL-aSiftedPlaybook-1` §3 defers to it as the owning figure for the whole gated draw, so S8 and
  S9 now have rows. S7's `lib` evidence disagreed with `TOOL-3` S1's on the same measurement — two
  answers to one question, inside the build that exists to close it — and now points at the owner.
- rev-6 · 2026-08-16 · folded round-3 blockers B1/B2/B3 and highs H4/H7. **B1**: `govkit` arrived
  from main as a TWELFTH kit and was in no scope item, waiver or non-goal; both spelled counts are
  deleted and the population is derived (AC9), with `govkit` given a disposition as S9. **B2**:
  `govkit selfcheck` reds on any undeclared depth-1 `tools/` path and S7 creates one. **B3**: this
  unit takes the closing `--bump` as S10, which unit 1 could not perform. **H4**: S8 and AC7 named
  two archive blobs ~2.3 KB apart; AC7 now matches S8 and the v-2-6 precedent. **H7**: §4 still
  listed `workflows/` as exempt against S7's two-row seed.
- rev-5 · 2026-08-16 · corrected S7's waiver-registry contract, exposed by resolving
  `TOOL-aSiftedPlaybook-3` F2 to RED. The registry cannot be both shrink-only and the escape hatch a
  red requires — a shrink-only file cannot gain the row an experimental kit needs. It is a declared
  exemption list that drains through that unit's two AC6 arms, and the divergence from
  `tools/install-prefix-waivers.txt` is now stated rather than implied by the word "modelled on".
- rev-4 · 2026-08-16 · folded round-2 medium M11. S4 named `README.md` as part of the gate-lint
  defect and then scoped only `AGENTS.md`, dropping the adopter-facing half without a non-goal —
  lost rather than deferred. Both are now in scope and Files touched, and AC8 observes them; without
  it every existing AC could pass with the charter half skipped entirely. Fork F1's per-option cost
  analysis is moot: the owner resolved it to inline.
- rev-3 · 2026-08-16 · cleared blocker B1 and two findings from the round-2 audit
  `wf_98677a7a-009`, and the owner resolved F1 to inline. **S8 added**: the v2.8 marker bump and the
  v2.7 archive snapshot were assigned to this unit by the build README and appeared in no spec, so
  the ACs would have passed while shipping a v2.7 marker over v2.8 content — round 1's fix went to
  the README and never reached the receiving unit, which is worse than the original state. S7's seed
  drops `workflows/`: measured, it already scores a path-segment hit at template `:150`, so the
  waiver would excuse nothing and never drain. §4's id-19 account corrected — the refutation rested
  on three grounds, not one, and only the ceiling is removed; the previous wording would have
  written that overstatement into an append-only record.
- rev-2 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`. AC1 quantified over a
  "declared not-adopter-facing set" that existed only as prose in §4, so nothing a builder could
  read; S7 now creates `tools/playbook-kit-waivers.txt` as that artifact and
  `TOOL-aSiftedPlaybook-3` consumes it. Dropped the `inventories.json:62` line anchor — the file is
  regenerated, `:62` is the string `"gate-lint"`, and the `kits` key is at `:58`. Added the manifest
  re-stamp to Files touched and corrected the `drift_report.py` spelling to `--check`.
- rev-1 · 2026-08-16 · initial draft. The fourth kit (`gate-lint`), the false "every other kit gets
  a §5 bullet" premise, the byte costs, and both dead cross-references in S6 came from the
  `unwired-kits` lens of `wf_4e13d9e7-550`; the aCandidStub id-19 refutation was surfaced by the same
  lens and changed the unit's framing from "add missing bullets" to "land a finding whose blocking
  objection was removed".

## 10. Reuse audit

The seam is the template's own kit-bullet shape at `:107-109` — three existing bullets whose voice,
ordering (`**Required —**` / `**Optional —**`), and closing "Adopt … per the kit README" clause the
four new ones copy rather than reinvent. AC3 makes conformance to the kit's README the test, so the
bullets stay derived from the kits rather than authored about them.

For AC1 the reused seam is the kit enumeration already implemented twice —
`tools/codebase-map/map_extractors.py` (the `kits` inventory, the `kits` inventory in `inventories.json`) and
`tools/check-install-prefix.sh:38`'s derived alternation. **No third enumeration is written**; the
acceptance criterion reads one of the existing two, which is also what makes
`TOOL-aSiftedPlaybook-3` cheap to build later.

Recall terms used, recorded per M5: `playbook template companion customize domain-rules agnostic
adopter stale externalize byte gate section stub kit wiring`. The binding prior record is the
`aCandidStub` review's refuted finding id 19, cited in §4; the binding backlog row is
`PLAY-aCandidStub-2`, whose "the template is effectively FULL" premise this build's ceiling raise
retires.
