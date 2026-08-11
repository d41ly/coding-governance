# PLAY-aSiftedPlaybook-3 — the playbook learns which kits it ships

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base 91ef1b05 · streams playbook

## 1. Goal

Four of the eleven kits under `tools/` are named nowhere in the three shipped playbook files, so an
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
  placement, the customize row, and the charter's kit list.
- **S5 — the customize conditional rows.** One per kit (~685 bytes total), in that file's existing
  voice, stating what to delete when the kit is declined.
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

`tools/` holds eleven tracked kit dirs. The same derivation is already used twice —
`tools/codebase-map/map_extractors.py` (feeding `inventories.json:62`) and
`check-install-prefix.sh:38`'s kit-name alternation — so AC1 quantifies over that enumeration rather
than over a list of four, which would go stale the moment a twelfth kit lands. Three kits are
legitimately not adopter-facing and belong on the exemption side: `lib/` (gov-internal, ships
nothing, per `AGENTS.md`), `hooks/` (reached through §8's `agent-cap.js`) and `workflows/` (reached
through §8's `tier2-review.js`).

### Cost, and why this unit alone needs the ceiling raise

| Item | Bytes | Gated? |
|---|---|---|
| S1 drift-audit §5 bullet | ~645 | yes — template |
| S2 pytest-guardrails §7 bullet | ~527 | yes — template |
| S3 agent-instructions §6 bullet | ~421 | yes — template |
| S4 gate-lint bullet | ~450 | yes — template |
| S2 domain-rules §10 append | ~130 | no |
| S5 customize rows | ~685 | no |

The gated subtotal is roughly **2043 bytes against 86 free at BASE**. Unlike
`PLAY-aSiftedPlaybook-2`, there is no cheaper naming that makes this fit: the content IS the cost.
**This unit is the one that genuinely requires `TOOL-aSiftedPlaybook-1` to land first**, and it is
the clearest single justification for the owner's raise.

### A prior review refuted this, and the ground it was refuted on is being removed

`memory/builds/aCandidStub/reviews/2026-08-10-review-aCandidStub-1.md:222-224` raised this exact
omission as finding id 19 and **refuted it**, partly on the ground that "the template is at its
ceiling". That refutation was correct on 2026-08-10. This unit is not re-litigating a settled
verdict; it is landing a finding whose only blocking objection the owner has now removed. The spec
must say so in those terms, and the build's decision row must cite id 19, or a future session
reading the review record will conclude the playbook re-added something a skeptic had killed.

### Files touched (estimate)

| File | Items |
|---|---|
| `parallel-coding-governance.template.md` | S1 §5, S2 §7, S3 §6, S4 |
| `parallel-coding-governance.customize.md` | S5, and S3's fill instruction at `:12-13` |
| `parallel-coding-governance.domain-rules.md` | S2's §10 append |
| `AGENTS.md` | S4's charter kit list |
| `WIRE-INTO-PROJECT.md` | S6's dead §2a reference |
| `tools/gate-lint/README.md` | S6's dead §14 reference |

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
  least one of the three playbook files, or listed in the declared not-adopter-facing set with a
  reason. The enumeration is the machine one, not a hand-list.
- **AC2** — When `parallel-coding-governance.customize.md`'s conditional-sections list is read,
  every kit named in the template has a row saying what to delete when it is declined.
- **AC3** — When each new bullet is read against its kit's own README, every claim it makes is
  present there. Checked per kit, by reading the README.
- **AC4** — When `grep -n '§2a' WIRE-INTO-PROJECT.md` runs it returns nothing, and when
  `tools/gate-lint/README.md:35` is read it cites §7 rather than §14.
- **AC5** — When `bash tools/check-template-size.sh` runs, it exits 0 against the raised ceiling and
  reports the measured size read FROM the gate.
- **AC6** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

- `bash tools/check-template-size.sh` — this unit spends ~2 KB of the new headroom.
- `bash skills/session-kickoff/manifest-check.sh` — the template is watched; re-stamp.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `python tools/drift-audit/drift_report.py` — `AGENTS.md` gains a kit; confirm no hand-kept
  inventory signal moves.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

- **F1 — do the four bullets go in the template, or behind §-stubs in the companion?** The template
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

- rev-1 · 2026-08-11 · initial draft. The fourth kit (`gate-lint`), the false "every other kit gets
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
`tools/codebase-map/map_extractors.py` (the `kits` inventory, `inventories.json:62`) and
`tools/check-install-prefix.sh:38`'s derived alternation. **No third enumeration is written**; the
acceptance criterion reads one of the existing two, which is also what makes
`TOOL-aSiftedPlaybook-3` cheap to build later.

Recall terms used, recorded per M5: `playbook template companion customize domain-rules agnostic
adopter stale externalize byte gate section stub kit wiring`. The binding prior record is the
`aCandidStub` review's refuted finding id 19, cited in §4; the binding backlog row is
`PLAY-aCandidStub-2`, whose "the template is effectively FULL" premise this build's ceiling raise
retires.
