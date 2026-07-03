# Session kickoff manifest — {{PROJECT_NAME}}

<!-- kickoff-manifest: v1.0 · instantiated from coding-governance skills/session-kickoff/MANIFEST-TEMPLATE.md -->

The project layer read by the generic `/session-kickoff` skill (the engine). Precedence on
conflicts: **`CLAUDE.md` > this file > the skill** — flag any conflict so it gets fixed. Keep
this file SHORT: it holds only what the engine can't derive from git or `CLAUDE.md`; the full
multi-node ruleset (if adopted) lives in the governance doc, referenced — not duplicated — here.

## §A — Task (the agent DERIVES this per kickoff — the user does NOT fill it)

The agent fills §A from the `/session-kickoff` message plus the adjacent memory (the project's decision
logs, backlog, journals, ledger) and the code — to the fullest extent possible. It uses
**`AskUserQuestion`** ONLY for a field it genuinely cannot derive to any extent (a real fork between
approaches, or a non-code prereq only the user knows — the most common one). The template below is the
*shape the agent fills*, not a form the user completes.

> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
> - **Risk tier:** {{TIER_VALUES e.g. "1 | 2" — or delete if single-tier}}

## §B — Orientation (the agent DERIVES these — the user does NOT fill them)

The agent fills §B by deriving every field it can from the repo (git state, the tree, `CLAUDE.md`,
`package.json` / `Makefile` / CI config) and the adjacent memory. It uses **`AskUserQuestion`** ONLY for
what the repo genuinely can't reveal (node registry, stream ownership, tier policy). §B is written once
when this manifest is instantiated; thereafter each session READS it, and re-derives a field only if the
code contradicts it.

- **Repo layout:** {{LAYOUT — e.g. "single checkout at repo root" | "worktrees as siblings
  under <root>/, primary tree (default branch) at <root>/main"}}
- **Remote · default branch:** `{{REMOTE}}` · `{{DEFAULT_BRANCH}}`
- **Branch conventions:** {{e.g. "feature/<name> branches off <default>; primary tree stays on
  <default>" — or "none"}}
- **Governing docs:** {{DOCS — decision logs / backlogs / plans and their precedence; "none" if
  the project has none yet}}
- **Governance playbook:** {{PATH to the instantiated parallel-coding-governance doc — or "not
  adopted"}}

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing doc(s) | First code entrypoints |
|---|---|---|
| {{AREA_1}} | {{DOC_1}} | {{ENTRYPOINTS_1}} |
| {{AREA_2}} | {{DOC_2}} | {{ENTRYPOINTS_2}} |

### Gate commands (the merge bar)

```bash
{{GATE_COMMANDS — the exact typecheck / lint / test / freshness commands, one per line}}
```

### Tier rule

{{TIER_RULE — one sentence: what forces the higher tier (new write path · migration ·
auth/sanitization/egress surface · shared-contract change · cross-stream merge), and what the
higher tier requires (spec approval before building / adversarial review). Delete this section
if single-tier.}}

### ID + ledger protocol

{{ID_PROTOCOL — either "none — no tracked id scheme" or, per governance §1–§2: the id format
(e.g. FAMILY-<slug>-<seq>), the slug rules + collision grep target, and the ledger file path.}}

### Environment traps worth front-loading

{{TRAPS — the 3–8 machine/toolchain gotchas every session otherwise re-derives (stale-port
watchers, EOL rules, shell path quirks, test-harness flags). Keep each to one line; link out
for detail.}}

---

**Customize before use** *(the agent does this during scaffolding, then deletes this block):*
fill every `{{PLACEHOLDER}}` — derive what the repo reveals (gates from `package.json` /
`Makefile` / CI config; layout from the tree), ask the user (via `AskUserQuestion`) only for the
rest (nodes, streams, tier policy). Delete sections marked deletable when they don't apply. Finish with `grep '{{'`
— no placeholder may survive.
