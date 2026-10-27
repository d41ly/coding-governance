# TOOL-dFurnishedOrders-43 — a receipt target's kit homes are the directories `apply` lands each kit's home at, derived through the entry's own destination rules, never a formula beside them

**Status:** DEFERRED · rev-3 · 2026-10-27 · node d · Tier-2 · base 47d3a464 · streams tooling · order 8 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. Id 14 shares that item and takes
`TOOL-dFurnishedOrders-44`.

`TOOL-dFurnishedOrders-40` S1 builds a receipt kit's home as `resolve_prefix_token("{prefix}/" +
desc["home"], pfx)`. `apply` never lands a kit there. A rule with no `to` lands at `ctx['kit']/<rel>`
(`tools/govkit/govkit.py:6617-6644`), and `ctx['kit']` is the target's `[kit.<eid>].kit` when set,
else `{prefix}/{eid}` (`:1479-1481`). A rule with a `to` lands where its template says. So
review-harness, whose descriptor id is `review-harness` and whose home is `workflows`
(`tools/workflows/kit.toml:3-4`), lands at `tools/review-harness/`, and a target that sets
`kit.memory-recall.kit` moves memory-recall wherever it says. Unit 40's home names neither directory,
so unit 36 subtracts no kit suite there and `witness` and `up` stop on a kit's deliberate key spelling,
while an adopter directory at gov's layout path is hidden. Unit 40 AC1 plants review-harness's rows
under `tools/workflows/`, gov's layout, so its criterion certifies the error.

The skeptic's fix, `target_context(...)["kit"]` alone, is not the whole of where `apply` lands a kit.
A probe of every non-flat registry entry at `47d3a464` (§4 "What the probe measured") shows agent-cap's
eight engine rules land under `{prefix}/hooks/` by their own `to` (`tools/hooks/kit.toml:24`), and
playbook-render's rules land under `{prefix}/playbook/` (`tools/playbook/kit.toml:9` declares the
`dir` kind), while `{kit}` names `tools/agent-cap` and `tools/playbook-render`. This unit takes the
home from the rules `apply` itself evaluates. It repairs `TOOL-dFurnishedOrders-40` and builds one
step after it (order 8).

## 2. Scope (IN)

- **S1** — The homes are where `apply` lands the kit's home. `derive_receipt_homes(gov_root, target,
  receipt, deploy)` in `tools/govkit/steps/retired_dispatch_args.py` answers `{eid: [home, ...]}` for
  each distinct `kit` value of the receipt's `files` rows. For an entry with a gov descriptor, read as
  `desc, _src = read_shipped_descriptors(gov_root)[eid]` (`tools/govkit/govkit.py:13283`), it takes
  `ctx = target_context(target, deploy, eid, desc)` (`:1436`), with `deploy` chosen as unit 40 S1
  chooses it, and walks the `survivors` of `resolve_entry(gov_root, desc, ctx)` (`:452`), whose
  destinations `expand_rules` resolves through `resolve_dests` (`:444`). A survivor row whose `src`
  lies under gov's home `H = desc["home"]`, whose `miss` list is empty, and whose `dest` ends in
  `/<rel>`, `rel` being `src` after `H/`, adds the directory `dest` minus `/<rel>`, with a leading
  `./` stripped. `derive_call_sites` takes unit 36 S1's receipt kit homes from this function alone.
  Observed by AC1 and AC2.
- **S2** — What is never a home. An entry whose descriptor declares `kind = "flat"` answers no home.
  A candidate that is the target root, that equals the entry's own `ctx["prefix"]`, or that names no
  directory on the target adds nothing. A receipt kit with no gov descriptor answers no home, which
  unit 41 S10 names on the scan line. Observed by AC2.
- **S3** — Unit 40's fixture placed where `apply` lands it. Unit 40 S1's `{prefix}/<home>` formula is
  not built, and this function stands in its place; unit 40's ledger answers its AC1 in the AMENDED
  form, its review-harness rows and its build-harness suite copy under `tools/review-harness/`,
  naming this unit's AC1. Unit 40 §4's sentence that reading from gov "keeps the step agreeing with
  `apply`" is true of this derivation, which reads the rules `apply` reads. Observed by AC1.

## 3. Non-goals (OUT)

- The parity gate that holds this derivation to the receipt `apply` writes, for every shipped kit:
  `TOOL-dFurnishedOrders-44`, for id 14.
- Unit 41 S6's compare of a copied `kit.toml`'s `home`, and a malformed `deploy.toml`: the minors
  batch `TOOL-dFurnishedOrders-45`, for ids 25 and 27.
- Mapping `project-owned` rows onto the target: unit 41 S8, which reads the homes S1 answers.
- The report's left-shift gate, a bug-class checklist entry for a target path derived beside
  `apply`'s seam: no clause of this build names it; unit 44's parity arm is its instance here.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-40` — S1's receipt-home branch of `derive_call_sites` and AC1's fixture, which S1 to S3 derive from `apply`'s own rules (id 1)
- **hands-off** `TOOL-dFurnishedOrders-41` — the homes `derive_receipt_homes` answers, which unit 41 S7's prefix guard, S8's `project-owned` mapping and S10's no-descriptor branch read (id 1)
- **hands-off** `TOOL-dFurnishedOrders-44` — `derive_receipt_homes`, which unit 44's arm holds to the receipt `apply` writes for every shipped kit (ids 1, 14)
- **hands-off** `TOOL-dFurnishedOrders-45` — the deploy read and the descriptor unpack S1 performs, which unit 45 S1, S6 and S8 settle (ids 25, 13, 27)
- **hands-off** `TOOL-dFurnishedOrders-46` — the files this unit's arm reads outside the `govkit selftest` guard, which unit 46 S8 adds to it (id 22)
- **hands-off** `TOOL-dFurnishedOrders-48` — `derive_receipt_homes`, its S1 walk and its S2 guards, which unit 48 S21, S22 and S24 settle (ids 14, 17, 33 of the fifth audit)
- **hands-off** `TOOL-dFurnishedOrders-52` — AC1's and AC2's fixtures and the arm over them, which unit 52 S17 gives `source` fields (id 18 of the sixth audit)

## 4. Design

### The home set on a receipt target, after this unit

```
deploy := .governance/deploy.toml if present, else {"prefix": receipt["prefix"]} if set, else {}
descs  := read_shipped_descriptors(gov_root)                  # {eid: (descriptor, descriptor path)}
for eid in sorted({row["kit"] for row in receipt["files"]}):
    eid not in descs                -> no home (unit 41 S10 names it)
    desc, _src := descs[eid];  desc["kind"] == "flat"  -> no home
    ctx := target_context(target, deploy, eid, desc);  H := desc["home"]
    for row in resolve_entry(gov_root, desc, ctx)["survivors"]:
        src, dest := row["src"], row["dest"]
        src empty, row["miss"] non-empty, src not under H/   -> skip
        rel := src after "H/";  dest not ending "/" + rel     -> skip
        cand := dest minus "/" + rel, leading "./" stripped
        cand is "." or ctx["prefix"], or no directory on target -> skip
        homes[eid] += cand
```

### Why the rules and not the token

`resolve_dests` is the one place `apply` decides where a source lands, and its docstring names
`plan`, the write loop and the wildcard exclusion as its readers. A kit's home on a target is the
image of its gov home under that decision. `{kit}` is one input to it, and it is the whole answer only
for an entry whose every rule lands under `{kit}`.

### What the probe measured

A scratch probe imported `govkit.py`, ran `target_context` and `resolve_entry` on every registry entry
at `47d3a464` with a deploy of prefix `tools`, and computed S1's image (PINNED, measured 2026-10-27;
re-derived by unit 44's arm on every run):

| entry | `{kit}` | S1's homes |
|---|---|---|
| agent-cap | `tools/agent-cap` | `tools/hooks` (8 engine rows) and `tools/agent-cap` (3 project-owned rows) |
| playbook-render | `tools/playbook-render` | `tools/playbook` (5 engine rows) |
| review-harness | `tools/review-harness` | `tools/review-harness` |
| memory-recall, `kit.memory-recall.kit = "scripts/recall"` | `scripts/recall` | `scripts/recall` |
| each other non-flat entry | `tools/<eid>` | `tools/<eid>`, the same |
| each `kind = "flat"` entry | `tools/<eid>` | the prefix `tools`, which S2 refuses |

At prefix `.` every candidate carries a leading `./`, which S1 strips. No candidate fell under the
memory root or `.claude/`: the skill and guide rules render from a source whose name differs from
their destination's, so their `dest` never ends in the source's `rel`.

### What it does not check

- A directory an adopter created at a kit's `{kit}` path that `apply` lands only `project-owned`
  sources at, agent-cap's `tools/agent-cap` say, is a home when it exists; its `*.test.sh` leave the
  scan. That is the directory the kit's descriptor names for those suites.
- A target that applied a kit under one `deploy.toml` and has since changed it reads the current one,
  as unit 40 §5 records for a moved descriptor.

### Inventory

Minted: the function `derive_receipt_homes` in the step; `derive` is a VERBS member of
`.lexicon.conf`, so `VERB_OFFENDER_PIN` does not move.

### Migration

None: the steps have never run.

### Rollout

Live at landing, at order 8, after unit 40.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **`target_context(...)["kit"]` alone, the skeptic's fix.** It answers `tools/agent-cap` where
  agent-cap's engine files land under `tools/hooks`, and `tools/playbook-render` where nothing lands,
  measured by §4's probe.
- **Unit 40's `{prefix}/<home>` formula.** `desc["home"]` is already joined to gov's tool root by
  `resolve_descriptor_paths` (`tools/govkit/govkit.py:13256-13280`), so it answers `tools/tools/...`,
  and even unjoined it names gov's layout, not the target's.
- **The directory of each receipt row.** Unit 40 §4 rejects it: merged and seed rows land at the root.

## 5. Production-readiness checklist

- security — the step reads gov's descriptors, the target's deploy descriptor and its receipt and
  writes nothing; every target value passes `target_context`'s strict token class first.
- perf / scale — one `resolve_entry` per receipt kit, each a glob over that kit's gov sources.
- error / empty / loading states — a refused per-entry value exits 1 as unit 40 S4 states; a receipt
  kit with no descriptor, or a flat one, answers no home.
- observability — unit 36 S2's `kit suite(s)` count on the scan line.
- risks — a kit whose rules land its home in two directories, agent-cap, yields two homes (§4).
- testing — AC1 and AC2 by fixtures and a probe; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed line is what the walk shows.

## 6. Acceptance criteria

- **AC1** — When `python retired_dispatch_args.py witness <target> checklist` runs over a scratch
  target whose `install.json` under `.governance` carries `prefix` `tools`, an `engine` row of kit
  `review-harness` whose `path` is unattended-unit.js under `<target>/tools/review-harness/`, an `engine` row
  `tools/hooks/agent-cap.js` of kit `agent-cap`, a `merged` row `pyproject.toml` and a `seed` row
  `.process-monitor.conf`, and which tracks a copy of the build-harness suite under
  `<target>/tools/review-harness/` spelling `"checklist":`, and an adopter suite, run.test.sh under
  `<target>/tools/workflows/`, naming `unattended-unit.js` and passing `checklist: 'x'`, it exits 1
  naming that adopter suite alone, and its scan line counts `1 kit suite(s)`.
  Red when: the review-harness home is taken as `tools/workflows` or `tools/tools/workflows`, so the
  kit's suite is scanned and the adopter's is hidden or both are named.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
- **AC2** — When `python -c` imports the step and prints `derive_receipt_homes` for a scratch target
  whose `deploy.toml` under `.governance` sets `prefix = "tools"` and `[kit.memory-recall]` `kit =
  "scripts/recall"`, whose receipt names kits `memory-recall`, `agent-cap`, `playbook-render`,
  `review-harness`, `check-wiring` and `no-such-kit`, and which holds each directory S1 derives, it
  prints `scripts/recall` for memory-recall, a list holding `tools/hooks` for agent-cap,
  `tools/playbook` for playbook-render, `tools/review-harness` for review-harness, and an empty list
  for `check-wiring` and `no-such-kit`; no answer is `.`, `tools` or under `tools/tools/`.
  Red when: a per-kit `kit` override is ignored, a `to` rule's directory is missed, or a flat entry
  or the prefix becomes a home.
  fixture: a scratch target under `%TEMP%`, built by the pass.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a receipt target with review-harness and agent-cap rows where `apply` lands them and an adopter suite at gov's layout path, and a per-kit `kit` override, staged by restoring unit 40's `{prefix}/<home>` formula · none

## 8. Open questions

- **FACT-QUESTION · F1 — Which seam answers a receipt kit's home?** Options: (a) S1's image of gov's
  home under `resolve_entry`'s survivors; (b) `target_context(...)["kit"]`, the skeptic's fix; (c)
  unit 40's `{prefix}/<home>`. Probe: §4's scratch import of `govkit.py`, computing (a) and (b) for
  every registry entry. Observation: an entry where (b) names a directory no rule lands its home at
  loses (b). Liveness: the probe can print (a) equal to (b) for every entry, and printed it for
  sixteen of the eighteen non-flat entries. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the probe's agent-cap and playbook-render rows. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-40`, with units 25, 35 and 36
  under it, is specced and unbuilt at `47d3a464`. RESOLVED (agent, 2026-10-27, delegated): the build
  run re-grounds on each at the pass and stops this unit if unit 40's receipt branch is still absent
  then, rung 1, the brief's rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-3 promotions, id 1
  (HIGH, item H1, shared with id 14).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-48, promoted from the spec audit of the round-4 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-52, promoted from the spec audit of the round-5 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `resolve_entry` (`tools/govkit/govkit.py:452`) and `expand_rules` (`:424`), which
reach `resolve_dests` (`:6617`), the one spelling of where `apply` lands a source; `target_context`
(`:1436`); `read_shipped_descriptors` (`:13283`). `python tools/codebase-map/reuse_lookup.py "the
directory apply lands a kit's files at on a target"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`
first and `target_context` lower; `resolve_kit_dir` finds one anchor file through a receipt row or a probe and
answers no home set, and `kit_rel` and `kit_dir` resolve gov's own directories, so no seam beyond the
four named derives a home on a target. The recall probe returned TOOL-aScouredKit-26, which records
that govkit lands every kit at `{prefix}/{entry-id}`, and the audit's H1 text; source agrees with the
first for rules with no `to` and refines both for rules with one (§4).

Recall terms used: `python tools/memory-recall/query.py "where does apply land a kit's home on an
adopter that sets a per-kit install directory" --terms "kit home resolve_dests target_context kit
token receipt apply landing directory eid override"`
