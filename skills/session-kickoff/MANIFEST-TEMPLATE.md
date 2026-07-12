# Session kickoff manifest — {{PROJECT_NAME}}

<!-- kickoff-manifest: v1.1 · instantiated from coding-governance skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: {{AUDIT_DATETIME}} @ {{AUDIT_SHA}}
watch: {{WATCH_PATHSPECS}}
verify-paths: {{VERIFY_PATHS}}
check-script: scripts/manifest-check.sh
-->

The project layer read by the generic `/session-kickoff` skill (the engine). Precedence on
conflicts: **`CLAUDE.md` > this file > the skill** — flag any conflict so it gets fixed. Keep
this file SHORT: it holds only what the engine can't derive from git or `CLAUDE.md`; the full
multi-node ruleset (if adopted) lives in the governance doc, referenced — not duplicated — here.

## The ratchet — how this file stays true

- Every kickoff audits this file (engine Step 2b runs `manifest-check.sh`) and repairs drift on the
  spot — fix or delete stale rows; a deep restructure becomes a flagged task instead.
- Every work-unit that changed what this file front-loads writes the delta back before wrap-up — a
  gate command, entrypoint, governing doc, layout/branch convention, a trap hit, a doc/memory claim
  found stale, or **a fact the session had to re-derive that this file should have front-loaded**
  (the accretion trigger); no delta → no touch.
- `last-audit` is an assertion of verification, re-stamped ONLY after actually re-verifying §B, with
  a delta line (`manifest-audit: delta <none|summary incl. deletions> · watch-commits-since-stamp:
  <n>`, n counted from the OLD stamp before re-stamping) in the commit message; the gate goes red
  whenever `watch` files move past the stamp.
- Stamp rule: sha = `HEAD` on the default branch, else `git merge-base <remote>/<default> HEAD`;
  no remote → `git merge-base <local-default> HEAD` (a branch sha would be orphaned by a
  squash-merge); the datetime always advances.
- Dated entries (corrections, traps) carry a prune-when condition and are DELETED once it holds.
- A claim whose truth lives in another repo is tagged `(cross-repo — verify at use)` and sits
  outside the `last-audit` assertion — watch pathspecs are single-repo.

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
> - **Risk tier:** {{TIER_VALUES}}

## §B — Orientation (derived at instantiation; re-audited every kickoff per the ratchet above; accretes)

The agent derives every §B field it can from the repo (git state, the tree, `CLAUDE.md`,
`package.json` / `Makefile` / CI config) and the adjacent memory, and uses **`AskUserQuestion`** ONLY
for what the repo genuinely can't reveal (node registry, stream ownership, tier policy). After
instantiation, each kickoff re-audits it (Step 2b) and each closing unit writes its deltas back.

- **Repo layout:** {{LAYOUT}}
- **Remote · default branch:** `{{REMOTE}}` · `{{DEFAULT_BRANCH}}`
- **Branch conventions:** {{BRANCH_CONVENTIONS}}
- **Governing docs:** {{GOVERNING_DOCS}}
- **Governance playbook:** {{PLAYBOOK_PATH}}

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing doc(s) | First code entrypoints |
|---|---|---|
| {{AREA_1}} | {{DOC_1}} | {{ENTRYPOINTS_1}} |
| {{AREA_2}} | {{DOC_2}} | {{ENTRYPOINTS_2}} |

### Gate commands (the merge bar)

```bash
{{GATE_COMMANDS}}
bash scripts/manifest-check.sh        # manifest ratchet — standing line; path = check-script: above
```

### Tier rule

{{TIER_RULE}}

### ID + ledger protocol

{{ID_PROTOCOL}}

### Codebase map

{{CODEBASE_MAP}}

### Current posture — dated corrections

*A correction OVERRIDES a stale doc/memory claim until the underlying staleness is fixed. Entry
shape: `<date> · <what is stale where> · <the correction> · prune when <condition>`. This section
starts empty and is prunable per-ENTRY — never delete the section itself.*

- *(none yet)*

### Environment traps worth front-loading

*This list ACCRETES — append the trap that cost this session time, prune the one that stopped being
true. Keep each to one line; link out for detail.*

{{TRAPS}}

---

**Customize before use** *(the agent does this during scaffolding, then deletes this block; finish
with `grep -nE '\{\{[A-Z]'` — no placeholder may survive):*

- `{{PROJECT_NAME}}` — the project's name.
- `{{AUDIT_DATETIME}}` / `{{AUDIT_SHA}}` — the stamp at the moment §B was derived and verified:
  ISO-8601 datetime with offset (e.g. `date -Iseconds`) · full sha per the stamp rule (`HEAD` on
  the default branch, else `git merge-base <remote>/<default> HEAD`; no remote →
  `git merge-base <local-default> HEAD`). If the repo has no commits yet, make the initial
  commit first — an unborn branch has no stampable sha.
- `{{WATCH_PATHSPECS}}` — `;`-separated git pathspecs for the files §B's gate commands and layout
  claims are derived FROM (CI workflow files, `Makefile`, script dirs first; never lockfiles;
  `package.json`-class files only if gates genuinely derive from them — they churn on every dep
  bump). ≤~8, prefer directory prefixes, each must match ≥1 tracked file.
- `{{VERIFY_PATHS}}` — `;`-separated, the 2–3 highest-value tracked anchors (the playbook + top
  governing doc/dir). NOT a mirror of the pointer map.
- `{{TIER_VALUES}}` — e.g. `1 | 2`; delete the line if single-tier.
- `{{LAYOUT}}` — e.g. "single checkout at repo root" | "worktrees as siblings under `<root>/`,
  primary tree (default branch) at `<root>/main`".
- `{{REMOTE}}` / `{{DEFAULT_BRANCH}}` — from `git remote` / `git symbolic-ref`.
- `{{BRANCH_CONVENTIONS}}` — e.g. "`feature/<name>` branches off `<default>`; primary tree stays on
  `<default>`" — or "none".
- `{{GOVERNING_DOCS}}` — decision logs / backlogs / plans and their precedence; "none" if the
  project has none yet.
- `{{PLAYBOOK_PATH}}` — path to the instantiated parallel-coding-governance doc — or "not adopted".
- `{{AREA_1}}` `{{DOC_1}}` `{{ENTRYPOINTS_1}}` · `{{AREA_2}}` `{{DOC_2}}` `{{ENTRYPOINTS_2}}` —
  pointer-map rows; add/remove rows as needed.
- `{{GATE_COMMANDS}}` — the exact typecheck / lint / test / freshness commands, one per line. Keep
  the standing `manifest-check.sh` line beneath them (adjust its path when `check-script:` is
  non-default).
- `{{TIER_RULE}}` — one sentence: what forces the higher tier (new write path · migration ·
  auth/sanitization/egress surface · shared-contract change · cross-stream merge) and what it
  requires (spec approval before building / adversarial review). Delete the section if single-tier.
- `{{ID_PROTOCOL}}` — either "none — no tracked id scheme" or, per governance §1–§2: the id format
  (e.g. `FAMILY-<slug>-<seq>`), the slug rules + collision grep target, and the ledger file path.
- `{{CODEBASE_MAP}}` — either "not adopted" or: MAP_ROOT, the digest command verbatim, and the two
  standing rules (ratchet gate rides the test suite; a high-risk unit touching an undossiered
  feature creates its dossier at design time). Delete the section if the kit is not adopted.
- `{{TRAPS}}` — the 3–8 machine/toolchain gotchas every session otherwise re-derives; start with
  what instantiation itself surfaced. One line each.

Derive what the repo reveals; ask the user (via `AskUserQuestion`) only for the rest (nodes,
streams, tier policy). Delete sections marked deletable when they don't apply.
