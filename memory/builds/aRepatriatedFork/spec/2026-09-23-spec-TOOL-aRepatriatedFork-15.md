# TOOL-aRepatriatedFork-15 — a kit whose shipped bytes move bumps its version

**Status:** CLOSED · rev-2 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-TOOL-aRepatriatedFork-15-1-acceptance-ledger.md](../build/2026-09-24-build-TOOL-aRepatriatedFork-15-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-15-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-15-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

A kit's version constant is the one answer an adopter has to "am I in sync?". Between gov fd240496
and a7c78ad2, eight kits changed bytes an adopter receives while their constants stood still, and
inCMS's `kit-versions` leg — which compares the bytes it carries against the constant between its
`main` and the pull branch — reds on the two it measures. Nothing in gov notices:
`check-kit-versions.sh` grades presence and agreement, never a diff (`TOOL-aHoistedPass-31`). This
unit bumps the kits that moved, and adds the gate that makes a forgotten bump red on the branch that
forgot it.

## 2. Scope (IN)

- **S1** — A `govkit.py epoch` verb applies `tools/memory-tree/check-verdict-epoch.sh`'s topological
  rule to every registry entry: over `<base>..HEAD`, the newest commit that changes any byte of the
  entry's shipped set must be an ancestor of, or equal to, the newest commit that changes the
  entry's version value. The shipped set is `TOOL-aRepatriatedFork-16`'s `govkit.py shipped` rows
  with role `engine`, `seed`, `rendered` or `merged`; the value is read by
  `resolve_entry_version_at` (`tools/govkit/govkit.py:432`). The base defaults to the merge-base
  with the default branch, as `tools/memory-tree/check-verdict-epoch.sh:74-78` does, and an
  unresolvable base is a FAILED exit 1. Two merge rules (rev-2): a move is a NON-merge commit, and a
  bump is any commit, merges included, whose value differs from its FIRST parent's, because a value
  can enter a range only through a merge (check-wiring's 1.4 to 1.5 over `fd240496..a7c78ad2` did);
  and an entry whose value at the base equals its value at HEAD while its bytes moved is FAILED
  outright, so a reconcile merge that carries a mainline bump into a branch cannot excuse the
  branch's own moves. Observed by AC1, AC2 and AC3.
- **S2** — The two kits inCMS measured are bumped: drift-audit 1.11 to 1.12, over five files and
  +664/-13, which `TOOL-aRepatriatedFork-7` (f204b537) already did before this unit's pass; and
  kickoff-manifest 1.4 to 1.5, over four files and +133/-41, under the version split S4 defines.
  Observed by AC4.
- **S3** — The further kits S1's run names are bumped. Over `fd240496..a7c78ad2` it named six:
  lexicon 1.5, memory-recall 1.9, playbook-render 1.0 and review-harness 1.8 were already bumped by
  sibling units before this pass (d50ac91d, b858ce1a, f204b537); process-monitor 0.2 to 0.3; and the
  playbook template's `governance-template: v3.0` marker to v3.1, with the v3.0 text cut as a
  `memory/archive/coding-governance-agents.template-v-3-0.md` snapshot, because 84383ffd moved
  charter TEXT and §8 F2 rules that a snapshot. At this unit's own tip the run names two more,
  moved by sibling units after their own last bumps: memory-tree 2.88 to 2.89 (7308f088 moved its
  `kit.toml` after 643cb92c's bump) and unattended 1.29 to 1.30 (68af7553 after ca2c20a0). And
  playbook-render 1.2 to 1.3, because this unit's own leg exemption moves `tools/govkit/registry.toml`,
  which that kit ships. Every one is in scope because AC4 reads zero FAILED lines. Observed by AC4.
- **S4** — kickoff-manifest carries two numbers where it carried one. `KIT_MANIFEST_VERSION`
  (`skills/session-kickoff/manifest-check.sh:37`) stays the kit's vintage and is what bumps; a new
  `MANIFEST_FORMAT` constant holds the manifest format, and it alone is compared with an adopter's
  `kickoff-manifest: v<N>` marker (`:580-584`) and with the seed's marker
  (`tools/check-kit-versions.sh:47-60`). Observed by AC5.
- **S5** — A kit with `version_from = { none = … }` is not graded; the verb prints one announced
  skip per such kit whose shipped bytes moved, naming the files. Observed by AC6.

## 3. Non-goals (OUT)

- Retiring `tools/memory-tree/check-verdict-epoch.sh`. It asks a narrower question — behaviour lines
  of one engine — and it is shipped to adopters, where `TOOL-aRepatriatedFork-2` fixes its paths.
  The overlap is §8 F3.
- Giving a constant to the kits that declare none (check-install-prefix, check-microformats,
  gate-lint, push-main). Each descriptor records why; the verb announces them instead.
- The receipt's stale `version` labels after a pin. That is `DEPL-aRepatriatedFork-17`'s item (f),
  on the deployer side of the same number.
- An adopter's own comparison. inCMS's `scripts/check_kit_versions.py` is its own program and keeps
  its own rules; this unit makes gov's bytes stop tripping it.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-16` — the `shipped` verb's role column. Without it the
  epoch verb would re-derive the survivors a third time and could disagree with the install-prefix
  gate about what an adopter receives.
- **hands-off** `DEPL-aRepatriatedFork-14` — the bumps S2 makes, which let that unit's
  `kit-versions-need-list` hole discharge at an inCMS update branch.

## 4. Design

### The defect, measured

inCMS, node a, 2026-09-23, on the pull branch at `1bc57da27` against its `main` at `e681f78d6`:
`bash scripts/check-kit-versions.sh` prints `FAILED — kit drift-audit: bytes moved between main and
HEAD while KIT_DRIFT_AUDIT_VERSION stayed at 1.11`, and the same line for `KIT_MANIFEST_VERSION` at
1.4. The comparison is inCMS's check 2 (`scripts/check_kit_versions.py:18-26`). PINNED.

Gov, same day, by `git diff --shortstat fd240496..a7c78ad2` and the constants at both ends:

| Kit | Shipped files moved | Constant at both ends |
|---|---|---|
| drift-audit | `tools/drift-audit/`: 5 files, +664/-13; three of them `engine` | `KIT_DRIFT_AUDIT_VERSION = "1.11"` (`tools/drift-audit/drift_report.py:51`) |
| kickoff-manifest | `skills/session-kickoff/`: 4 files, +133/-41; three shipped | `KIT_MANIFEST_VERSION="1.4"` (`skills/session-kickoff/manifest-check.sh:37`) |

A resolution of every registry entry over the same range, reading each entry's `version_from` at
both commits and comparing the blobs of its `engine`, `seed`, `rendered` and `merged` sources, found
six more (PINNED, node a, 2026-09-23): lexicon at 1.5, memory-recall at 1.9, playbook-render at 1.0,
process-monitor at 0.2, review-harness at 1.8, and the charter template at `v3.0`. Five kits that
moved DID bump over the range — agent-cap, check-wiring, memory-tree, run-gates, unattended — and
runlog gained its first constant. inCMS reds on two and not eight because it carries no constant
for, or no copy of, the other six.

### Why bytes and not behaviour

`check-verdict-epoch.sh` exempts comment lines because a comment changes no verdict. An adopter's
comparison cannot know that: inCMS compares blob ids, so a comment-only change reds it exactly as a
logic change does. Counting every shipped byte over-counts on purpose, and the cost is the one the
verdict-epoch header already accepts for its own rule: one bump per range, correctly placed.

### Why the manifest needs two numbers

`KIT_MANIFEST_VERSION` is also the manifest FORMAT. `manifest-check.sh:580-584` warns "manifest
format v1.4 < kit v1.5 — see the upgrade recipe" when an adopter's manifest is older, and
`tools/check-kit-versions.sh:47-60` requires the seed's marker to equal the constant. So a vintage
bump today tells every adopter, gov included (`memory/guides/SESSION-KICKOFF.md:3` reads `v1.4`), to
upgrade a format that did not change, pointing at a recipe with no step for it. inCMS's standing
`kickoff-manifest` waiver in `.governance/kits.json` records the same number's earlier stall at 1.3.

### Data model

`python tools/govkit/govkit.py epoch [--base <rev>]` prints one line per entry:

```
epoch: <entry> · clean · <version>
epoch: <entry> · FAILED · moved in <sha> (<n> files) · no value change in <base>..HEAD (still <version>)
epoch: <entry> · FAILED · last bump <S> precedes last move <W>
epoch: <entry> · skip · no declared version · moved: <paths|none>
```

It exits 1 on any FAILED line, 0 otherwise, and 2 on an unreadable registry.

### Inventory

- `epoch`, a govkit verb dispatched beside `selfcheck`; its handler is `cmd_epoch`.
- `MANIFEST_FORMAT`, a new constant in `skills/session-kickoff/manifest-check.sh`.
- One gov leg, named in §7's arm line; `memory/map/features/govkit.md` lists it among its legs.

### Migration

- inCMS: the pull after this lands carries a bump for both kits, so its `kit-versions` leg is green
  without the two `version_waivers` rows it would otherwise add to `.governance/kits.json`. Its
  standing `kickoff-manifest` waiver self-expires when `main` moves, and after S4 there is no reason
  to re-issue it.
- nc: nothing. Its `scripts/check-kit-versions.sh` carve-out 31 is an enumeration change, unrelated
  to history.
- Every adopter's manifest keeps `kickoff-manifest: v1.4` and stops being told to upgrade it.

### Rollout

S1 lands first with gov's own range clean. S2 and S3 follow as one bump commit per kit, each moving
the constant and every `gov:kit <id>@` marker `tools/check-kit-versions.sh` pairs with it. S4 lands
before the kickoff bump, so the format warning never fires.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/check-kit-versions.sh`
- `tools/gate-legs.json`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/SKILL.md`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/README.md`
- `tools/drift-audit/adopt-drift-audit.sh`
- `tools/drift-audit/drift_signals.template.py`
- `tools/workflows/drift-audit-code.js`
- `tools/workflows/drift-audit-state.js`
- `tools/workflows/tier2-review.js`
- `tools/lexicon/lexicon.py`
- `tools/memory-recall/recall_conf.py`
- `tools/process-monitor/adopt-process-monitor.sh`
- `tools/playbook/render_playbook.py`
- `coding-governance-agents.template.md`
- `AGENTS.md`
- `memory/archive/coding-governance-agents.template-v-3-0.md`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/unattended/unattended.sh`
- `WIRE-INTO-PROJECT.md`
- `memory/map/features/govkit.md`

### Alternatives rejected

- **Widen `check-verdict-epoch.sh` to every kit.** It is a memory-tree engine shipped to adopters
  and reads files at fixed paths; the registry is gov's, and a registry-driven check belongs where
  the registry is read.
- **Make `check-kit-versions.sh` read history.** It is a `seed`, so an adopter's copy is theirs
  after install and never receives the arm; the check has to live in gov-only code.
- **Bump only the two kits inCMS measured.** The gate's first run names eight, and leaving six means
  the one observation that found them is a red-first run nobody repeats.

## 5. Production-readiness checklist

- security — N/A. Read-only over git history.
- perf / scale — one `git log -- <paths>` per entry over the branch range, which is short at the
  push boundary. `--base fd240496` over a whole pull range is the expensive form and runs by hand
  only.
- error / empty / loading states — no merge-base is a FAILED exit 1, never a zero-status skip, as
  `check-verdict-epoch.sh:79-87` already argues; an entry with an empty shipped set is a named
  refusal.
- observability — every entry prints a line, clean ones included, so a missing entry is visible.
- risks — S4 changes what `manifest-check.sh` compares; a slip there makes every adopter's manifest
  warn, or makes a real format change silent. AC5 brackets both directions.
- testing — S1's selftest arm over a fixture registry; AC2 on real history as the red-first run.
- migration — adopters change nothing; inCMS stops needing two waivers.
- user docs — `WIRE-INTO-PROJECT.md` §4 names `MANIFEST_FORMAT` where it now spells the kit
  version as the format, and the rule "a kit whose shipped bytes move bumps" joins the kit-authoring
  notes beside `check-kit-versions.sh`.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py epoch` runs on a fixture branch that edits one line
  of a shipped engine and leaves its constant, it prints a FAILED line naming the entry and exits 1;
  with the bump in a later commit it exits 0. Red when: the unbumped edit exits 0.
- **AC2** — When `python tools/govkit/govkit.py epoch --base fd240496` runs at a7c78ad2, it exits 1
  and names at least drift-audit and kickoff-manifest. Red when: either is absent, meaning the verb
  cannot see the two moves inCMS measured.
  figure: the two kits are PINNED; the full list is derived by the run and was eight on 2026-09-23.
- **AC3** — When the fixture moves a bump to a commit BEFORE a later edit of the same kit, the verb
  prints the "last bump precedes last move" line and exits 1. Red when: an early bump excuses a
  later change, the endpoint-comparison defect `check-verdict-epoch.sh`'s header records.
- **AC4** — When `python tools/govkit/govkit.py epoch --base fd240496` runs after S2 and S3, it
  exits 0 with no FAILED line. Red when: any of the eight kits still reads at its a7c78ad2 value.
- **AC5** — When `bash skills/session-kickoff/manifest-check.sh` runs over gov's own
  `memory/guides/SESSION-KICKOFF.md` after the kickoff bump, it prints no `manifest format` warning;
  with `MANIFEST_FORMAT` raised in a fixture it does. Red when: the vintage bump alone produces the
  warning, or a raised format produces none.
- **AC6** — When the fixture moves a file of a kit whose descriptor declares no version, the verb
  prints a `skip` line naming that file and exits 0. Red when: the kit is silently absent from the
  output.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` ·
`kit version markers` · `kickoff-manifest ratchet` · `manifest-check self-test` ·
`scratch-guard self-test` · `lexicon naming predicates` · `drift-audit selftest` ·
`lexicon selftest` · `codebase-map kit selftest` · `memory-recall kit selftest` · `recall floor` ·
`recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test` ·
`process-monitor adopter selftest` · `playbook render selftest` · `tier2-review self-test` ·
`review-join self-test` · `verifier fan-out self-test` · `unattended-build self-test` ·
`run-gates canary` · `run-gates gov canary`

New arm: `tools/govkit/selftest.py` · a fixture registry with one versioned and one unversioned
entry on a three-commit branch — edit without bump, bump, edit after bump — observed FAILED, clean,
FAILED; then run once on real history as AC2 · none.

New arm: gov leg `kit epoch (shipped bytes move, the version moves)` in `tools/gate-legs.json`, argv
`python tools/govkit/govkit.py epoch` · its first run on the build's own branch before S2 lands,
observed red on drift-audit · none.

## 8. Open questions

- **F1 — split kickoff-manifest's number, or bump the format too?** Bumping `KIT_MANIFEST_VERSION`
  alone warns every adopter to upgrade a format that did not move. Recommendation: the split in S4,
  because the warning's whole value is that it fires only when the format changes.
  RESOLVED (owner, 2026-09-23): the split in S4, as recommended.
- **F2 — what does bumping the charter template mean?** Its `governance-template: v3.0` marker is
  also the charter's printed version, and the template header says history lives in `…-v-N-N.md`
  snapshots, so a bump implies a snapshot. Recommendation: treat it as a format like the manifest —
  bump the playbook kit's vintage only when rendered output changes, and snapshot on a charter-text
  change — and ask the owner before S3 moves it.
  RESOLVED (owner, 2026-09-23): a format: the playbook kit's vintage bumps only when rendered output
  changes, and a `-v-N-N` snapshot is cut on a charter-text change. This is the owner turn S3 waited
  on; S3 may move the marker under that rule.
- **F3 — does the memory-tree verdict-epoch leg stay on gov's bar?** The new verb subsumes it for
  memory-tree bytes and is stricter. Recommendation: keep it one release, because it is also the
  adopter-side check for memory-tree, then decide with its adopter behaviour fixed by
  `TOOL-aRepatriatedFork-2`.
  RESOLVED (owner, 2026-09-23): keep it one release, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from inCMS's red `kit-versions` leg on the a7c78ad2 pull
  branch and a resolution of every gov registry entry over `fd240496..a7c78ad2`.
- rev-2 · 2026-09-24 · S1 gains the two merge rules, because check-wiring's bump entered the range
  only through merges and read as "no value change" without them; S2 and S3 record the four kits
  sibling units bumped before this pass, and S3 adds memory-tree and unattended, which the verb
  names at the build tip, and playbook-render, whose shipped registry this unit's leg moves; the
  data model's skip line reads `moved: none` for an unmoved kit.

## 10. Reuse audit

The rule is `tools/memory-tree/check-verdict-epoch.sh`'s, lifted from one engine to the registry:
its W-ancestor-of-S walk, its `-G` candidate search validated against the parent, and its no-base
refusal. The version reader is `resolve_entry_version_at` (`tools/govkit/govkit.py:432`), which
already reads a constant at a commit.
`python3 tools/codebase-map/reuse_lookup.py "compare kit version constant against shipped file changes in a commit range"`
ranks own-kit helpers only and scans no `.sh`, so the shell seam was found by reading the
verdict-epoch gate; no existing seam fits the registry-wide case.

Recall terms used: `kit version`, `version_from`, `verdict epoch`, `KIT_MANIFEST_VERSION`,
`kit-versions`, `bump`, `vintage`, `marker`, `gov:kit`, `receipt`, `topological`, `forgotten bump`.
