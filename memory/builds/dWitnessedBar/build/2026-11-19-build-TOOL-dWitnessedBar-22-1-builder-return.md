**Serves:** journal TOOL-dWitnessedBar-22

# TOOL-dWitnessedBar-22 — builder return 1 (run `wf_cf539ade-dc7`), a divergence, nothing committed

## Why

DIVERGENCE: §2 S4 and §4 "The edge read" (and §7, which lists the `edges (every declared edge parses, is registered and resolves)` leg) say that every `enforces` edge `read_leg_edges` yields is typed and resolved through `check_edges` and `run_resolve`, and that only an unregistered `feature.*` `tests` target is withheld. The tree disagrees. 13 of the manifest's `enforces` targets, on 8 legs (DERIVED), use the rule-member form `practice.<p>.<rule>`. That form is admitted by `tools/playbook/practices.toml` line 5 (`rules`, each read as `<tag>.<rule>`) and by `core.py`'s meta-check. The tag index does not resolve it.
- The 13 targets: `practice.portable.{paths,temp-files,encoding,launch,interpreter-floor}` and `practice.writing.{address,retirement,typed-relations,one-subject,pinned-facts,one-door,rationale-apart,one-owner}`.
- The 8 legs (DERIVED): leg.gate-lint.shell-hygiene-a-location-probe-asked-from-a-moved, leg.gate-lint.shell-hygiene-a-fixed-name-temp-renamed-into-place, leg.gov.encoding-posture-text-io-names-its-encoding, leg.gov.python-resolver-behaviour-inline-parity-idiom-ban, leg.gov.tags-the-resolver-s-checks, leg.gov.edges-every-declared-edge-parses-is-registered-and, leg.gov.writing-practice-records-and-units, leg.gov.one-owner.
- Probe: `edge_grammar.resolve_edge` over `build_resolve_context(repo)` for every distinct `enforces` value. All 19 `principle.*` targets returned `resolved`, and so did the bare `practice.portable`, `practice.writing` and `practice.land`. Each of the 13 rule-member targets returned `red · resolves to no row of the tag index`.

`practice` is a registered namespace, so neither `check_edges` nor the spec's `feature.*` withholding stops these. Wiring `read_leg_edges` into `read_tree_edges` as written would turn the `edges` leg red on 13 targets the moment the pass lands, and the spec's §7 has the close run that leg. The spec has to choose one of these, and it is a design choice, not a build detail:
- (a) the resolver learns the `<practice>.<rule>` member form from `practices.toml` `rules` (a tag_index or resolver change outside Files touched);
- (b) the leg-row adapter counts and prints rule-member targets as unarmed, the same way it handles `feature.*`, with an AC and a plant for it;
- (c) the values are respelled, which is units 11 and 24's job, not this unit's (§3).

A second point, so the revision covers both: §4 pins the signature `read_leg_edges(manifest_rows) -> [(type, from_tag, to_tag)]`, yet the adapter is what withholds a target whose namespace is not registered (S4, §4), and AC4 grades that against a FIXTURE registry. A function that takes only `manifest_rows` cannot see the fixture registry. The spec should name the adapter's registry input, or move the withholding to the caller that holds the namespaces (`run_check` / `run_parse`). It should also name the edge-dict shape (`path`, `line`, `site`) that the tuples become for `check_edges`.

Every other probed claim held at base 99fea7ac:
- 198 rows (DERIVED), every one tagged; 51 carry `enforces`, none carries `tests`.
- 33 dossiers: 180 legs (DERIVED) claimed once, none twice, 18 unclaimed, `run-gates evidence` among them; every claim names a manifest leg.
- 27 descriptors, the same 4 with no claimed leg.
- The 6 `enforces` copies exactly as §4 names them; no descriptor row carries `enforces`.
- `LEG_KEYS` is the one line at `tools/run-gates/run-gates.test.sh@07550393:352` and holds `enforces`, not `tests`.
- The `enforces` row of `edges.toml` has `to = [unit, practice, principle]`; `feature` is not registered.
- The 7h block (tools/govkit/govkit.py@146416ff:2743) has the `doc_reads`, `impure`, `stage` and `tag` presence-included arms.
- `run_plant_rows edges` exists in `adopt-playbook.sh`.

## Summary

I committed nothing: TOOL-dWitnessedBar-22 goes back as a divergence, because building it as the spec says would turn the `edges` leg red on 13 targets.

**Base:** 99fea7aca079f143a7ef3ed6ae43050456657127. The worktree is clean; no product path was edited, so nothing needed restoring.

**Brief:** I did not run `--brief` again. RUN.md line 125 already records it (`brief · item TOOL-dWitnessedBar-22`, committed in 0e023dcde), and a second record would have changed a path I then had to restore.

**What I checked** (read-only probes in place of the gates that need them, the closest being `edges (every declared edge parses, is registered and resolves)`; no gate, suite or bar ran):
- `python -c` over `tools/gate-legs.json` for row and key counts, and over the dossiers' TOML fences under `memory/map/features/` for the claim counts. Both re-derived 180 claimed, 18 unclaimed, none claimed twice, so AC1's pinned figures hold.
- `python -c` over the `tools/**/*.toml` descriptors: 27 carry `[[gate_leg]]` rows, the same 4 have no claimed leg, and the 6 `enforces` copies match §4.
- `edge_grammar.resolve_edge` over the real repo for all 32 distinct `enforces` values. This is where it fails: the 19 `principle.*` targets resolve, but the 13 `practice.<p>.<rule>` targets come back `red · resolves to no row of the tag index`. That is the failure the `edges` leg's `--check` would report after this unit lands.
- I also read `govkit.py`'s 7h block, the `LEG_KEYS` line and its control pairs in `run-gates.test.sh`, `owed_rows.py`'s key arm, `adopt-playbook.sh`'s edge plant rows, and the `edges.toml` and `namespaces.toml` registries.

**For the spec revision:**
- **The red edges:** §2 S4 and §4 "The edge read" need to say what happens to rule-member `enforces` targets. The three options are in `why`.
- **The signature:** `read_leg_edges(manifest_rows)` cannot see the fixture registry that AC4 grades the withholding against. The spec should give the adapter a registry input or move the withholding to the caller.

**Still owed for the rebuild, by the close:** the three `New arm:` lines in §7 (the gov canary's compare, the two `adopt-playbook.sh` edge plants, and govkit selftest's 7h join), each to be seen RED first. AC1 to AC6 are not observed yet.

I did not run the M6 gotchas checklist, because there is no commit range to run it over.

Paths:
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-22.md
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/gate-legs.json
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/playbook/practices.toml
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/playbook/edge_grammar.py
