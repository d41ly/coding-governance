# TOOL-dFairHearing-22 — agent-cap fails closed on a spec-audit call when the opt-in pack is not beside it

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-22-deviation-221.md](../build/2026-10-23-build-TOOL-dFairHearing-22-deviation-221.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-22-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-22-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md) | spec-audit | TOOL-dFairHearing-21 TOOL-dFairHearing-20 TOOL-dFairHearing-23 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit's finding id 40 (item H3, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`) is closed: once
`TOOL-dFairHearing-16` moves rule 0 out of `tools/hooks/agent-cap.js`, the hook still denies, by name, a
`Workflow` call of the spec-audit kind whenever the review kit's opt-in pack `spec-audit-optin.js` is
not installed beside it. Today a supported partial update, `govkit update --kits agent-cap`, lands the
hook without rule 0 and without the pack, because the update narrows to the kits named and the hooks
kit does not require the review kit (`tools/govkit/govkit.py:9286-9316`, `tools/hooks/kit.toml:9`), so
the spec-audit opt-in fails open.

## 2. Scope (IN)

- **S1** — `checkOptinPackPresent(data)` in `tools/hooks/agent-cap.js`, called at the site rule 0's
  `checkSpecAuditDeclared` occupied in `main()`. For a `Workflow` call whose structured args, read by
  `extractWorkflowArgs`, carry `kind: 'spec-audit'` or a `specAudit` key, the trigger rule 0 used
  (`tools/hooks/agent-cap.js:1914-1915`), it denies, exit 2, unless the file
  `<hook dir>/../workflows/spec-audit-optin.js` exists. Every other call, and every spec-audit call with
  the pack present, is admitted by this check; the pack decides the opt-in. Observed by AC1, AC2 and
  AC3.
- **S2** — The deny message names the pack's expected path, that the spec-audit opt-in moved to the
  review kit, and the two remedies: `govkit update --kits review-harness`, or wiring a hand copy with
  `tools/settings-merge.py --fragment`. Observed by AC1.
- **S3** — `tools/hooks/README.md` states that the hook carries no opt-in rule, only this presence
  check, and why: a hook landed without its pack must not admit an audit nobody judged. Observed by
  AC4.
- **S4** — The suite arm the `New arm:` line in §7 declares, in `tools/hooks/agent-cap.test.sh`.
  Observed by AC1, AC2 and AC3 through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No opt-in rule in the hook: whether a build declared `spec-audit:` stays the pack's alone, as
  `TOOL-dFairHearing-16` S4 puts it, so the rule never lives in two homes.
- No read of `.claude/settings.json` from the hook. A pack present and unwired is a hand-copy state
  that `tools/check-wiring.sh` reports UNWIRED (`TOOL-dFairHearing-16` S6); govkit wires every fragment
  it lands (`tools/govkit/govkit.py:6109-6125`), so on govkit's paths presence implies wiring.
- No change to govkit, to either kit's `requires`, or to `update`'s scope narrowing.
- No change to rules 1, 3, 4 and 6, or to any non-`Workflow` call.

### Edges

- **consumes-from** `TOOL-dFairHearing-16` — rule 0's removal from the hook, `extractWorkflowArgs` exported, and the pack file `tools/workflows/spec-audit-optin.js` whose presence S1 tests; without them there is no moved rule to guard
- **hands-off** `TOOL-dFairHearing-27` — finding ids 17, 18, 33 and 34 of the spec audit of units 20 to 23: the pack coupled to agent-cap's marker (its S12, AC7), the remedy by receipt state, superseding S2's fixed remedy and AC1's string (its S13, AC8), the pack resolved through the receipt first (its S20, AC15), and the self-test guard covering the pack (its S21, AC16)

## 4. Design

### Evidence

- `tools/hooks/kit.toml:9` makes the hooks kit require `settings-merge` and `kickoff-manifest` only;
  `tools/workflows/kit.toml:9` makes the review kit require `agent-cap`, the reverse direction.
- `govkit update --kits <k>` narrows the rows to the kits named, widening only through shared version
  markers (`tools/govkit/govkit.py:9286-9316`).
- The hook already probes the review kit beside its own directory, at
  `path.join(path.dirname(__dirname), 'workflows', ...)`, for the harness a deny message names
  (`resolveHarnessName`, `tools/hooks/agent-cap.js:111-116`). S1 reuses that resolution.
- A `requires` edge from the hooks kit to the review kit closes a cycle with the review kit's own edge,
  and govkit's install order refuses a cycle (`tools/govkit/govkit.py`, `derive_install_order`'s
  docstring).

### The check

```
checkOptinPackPresent(data):
  a = extractWorkflowArgs(data)
  if not a, or (String(a.kind) !== 'spec-audit' and a.specAudit === undefined): admit
  p = path.join(path.dirname(__dirname), 'workflows', 'spec-audit-optin.js')
  fs.existsSync(p) ? admit : deny(p)
```

It runs only when no `--only=` selector is given, as rule 0 did. A throw inside it denies, the hook's
fail-closed rule for a rule that cannot finish (`tools/hooks/agent-cap.js:2269-2272`).

### What it does not check

It proves the pack's file is present, never that the pack is wired or that it judges correctly. The
unwired hand copy is `tools/check-wiring.sh`'s to report, and the pack's verdicts are its own suite's.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `checkOptinPackPresent` | function, `tools/hooks/agent-cap.js` | `js.function`, OK |

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`

### Alternatives rejected

- **The hooks kit requires the review kit.** The report offers it. It closes a requires cycle govkit
  refuses, and it forces the review kit onto every adopter of the hooks kit.
- **govkit refuses a partial update that lands agent-cap without the review kit.** It guards govkit's
  path alone, never a hand copy, and it changes the deployer, a carrier no clause of this build names.
- **The hook keeps rule 0 until the pack's fragment is wired.** The rule then lives in two homes at
  once, against `TOOL-dFairHearing-16` §4 "The order inside the pass", and the hook must parse settings.

## 5. Production-readiness checklist

- security — deny by default: a spec-audit call with no pack beside the hook is refused, so no
  landing order or partial update leaves the opt-in unenforced.
- perf / scale — one `existsSync` per spec-audit `Workflow` call.
- error / empty / loading states — an absent pack denies by name with its remedy; a throw denies.
- observability — the deny names the expected path and both remedies.
- risks — an adopter of the hooks kit alone who runs a spec-audit call through some other harness is
  now denied where rule 0 might have admitted a dated README; the message names the kit to install.
- testing — a scratch copy of the hook with and without the pack beside it; the arm in §7 is observed
  RED then GREEN by the main loop at the close.
- migration — none in this tree, where the pack lands with `TOOL-dFairHearing-16`.
- user docs — `tools/hooks/README.md`; `help/roles.md` lists hook refusals and names none of the
  review rules.

## 6. Acceptance criteria

Fixtures live under the pass's scratch directory; a payload's `cwd` is that directory, outside any
checkout, so rule 6 of the hook is unarmed, and `CLAUDE_PROJECT_DIR` is unset for the run.

- **AC1** — When `node "$SCRATCH/p/hooks/agent-cap.js" < "$SCRATCH/sa-dated.json"` runs, the hook and
  `scratch-guard.js` copied into `$SCRATCH/p/hooks/` with no `$SCRATCH/p/workflows/`, over a
  `kind: "spec-audit"` call whose fixture build README carries `spec-audit: 2026-10-23`, it exits 2
  and its stderr names `spec-audit-optin.js` and `govkit update --kits review-harness`.
  Red when: the hook admits a spec-audit call with no pack beside it.
- **AC2** — When the review kit's pack `spec-audit-optin.js`, as `TOOL-dFairHearing-16` lands it, is
  copied to `$SCRATCH/p/workflows/` and the
  same payload runs, the hook exits 0; and a `kind: "diff-review"` payload exits 0 with no pack beside
  the hook.
  Red when: the check denies with the pack present, or denies a call that is not a spec audit.
- **AC3** — When a payload carrying `specAudit: "2026-10-23"` and no `kind` runs against the copy with
  no pack, the hook exits 2 naming `spec-audit-optin.js`.
  Red when: the build harness's `specAudit` call slips past the trigger.
- **AC4** — When `grep -n "spec-audit-optin.js" tools/hooks/README.md` runs, it prints the paragraph
  naming the presence check and the pack as the opt-in's home.
  Red when: the README still describes an opt-in rule in the hook, or none at all.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `agent-cap restatement` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 AC3 · a copy of the hook staged in a layout with no review kit beside it, red against the hook at `TOOL-dFairHearing-16`'s commit, which admits the spec-audit call · none

## 8. Open questions

- **F1 — Where does the guard against a pack-less landing live?** Options: (a) a presence check in the
  hook, failing closed; (b) the hooks kit requiring the review kit; (c) a govkit refusal of a partial
  update; (d) the hook keeping rule 0 until the pack is wired. (b) closes a requires cycle govkit
  refuses, (c) misses a hand copy and changes the deployer, a carrier outside this build's grant, and
  (d) puts one rule in two homes against `TOOL-dFairHearing-16`'s order. (a) covers every landing path
  inside files `TOOL-dFairHearing-16` already touches. RESOLVED (agent, 2026-10-23, delegated): (a),
  rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 40 (item H3) of the round-1 spec audit.
- rev-2 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-27, naming the four findings it closes on this spec and what it supersedes.

## 10. Reuse audit

The seam is the hook's own sibling-kit probe, `resolveHarnessName`
(`tools/hooks/agent-cap.js:111-116`), which already resolves the review kit beside the hook's
directory; S1 resolves the pack the same way, and the trigger is rule 0's own two-condition test
(`tools/hooks/agent-cap.js:1914-1915`). `python tools/codebase-map/reuse_lookup.py "hook resolves a
sibling kit file beside its own directory and denies when absent"` ranked `resolve_kit_dir` and
`kit_rel`, the Python and shell resolvers; neither runs inside the Node hook, so the JS probe the hook
already carries is the seam. The recall query returned the audit's H3 item, `DEPL-aLevelledCopy-2`
(an `apply` landing an engine without its mode) and `TOOL-aRoutedQuill-5`'s rule that a default
fragment lands wired, which §3 relies on.

Recall terms used: `python tools/memory-recall/query.py "what happens when govkit update lands one kit without the kit it depends on" --terms "govkit update kits partial requires agent-cap review-harness fragment wired fail open hook rule"`
