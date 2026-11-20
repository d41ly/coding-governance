# TOOL-dWitnessedBar-6 — the verdict backends registered under `verdict`: the local hook, the peer-node verifier and the `remote-ci` slot with its witness rule and pin

**Status:** CLOSED · rev-7 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 28 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0344@5cea08b4 whole
**Carries:** node:policy-key.verdict
**Carries:** node:policy-key.verdict.remote.trust
**Carries:** node:policy-key.verdict.remote.pin-scope
**Carries:** node:policy-key.verdict.remote.pin

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-6-deviation-61.md](../build/2026-10-25-build-TOOL-dWitnessedBar-6-deviation-61.md) | deviation | — |
| [2026-10-26-build-TOOL-dWitnessedBar-6-deviation-62.md](../build/2026-10-26-build-TOOL-dWitnessedBar-6-deviation-62.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-6-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-6-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-6-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-6-1-builder-return.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-6-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-6-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-6-reground3-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-6-reground3-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-6-reground3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-6-reground3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-6-reground4-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-6-reground4-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-6-reground4-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-6-reground4-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

The binding verdict is one node's bypassable hook, and remote CI blocks nothing
(`.github/workflows/remote-ci.yml@174f9d9e5:15-16`, gap-test-02). A remote verdict also certifies
itself: its workflow sits in the tree it judges, and nothing grades the workflow's text beyond its
`python-version` lines (`.github/workflows/remote-ci.yml@174f9d9e5:19-23`, gap-test-11). The one live
outside reader, `read_held_reds`, sits inside the unattended kit with no registration
(`tools/unattended/unattended.sh#read_held_reds`, gap-test-13). This unit declares the verdict
backends as a registry under the policy key `verdict`: `local-hook` and `peer-node`, both core, and
`remote-ci`, the slot the integrations expansion fills (R5.2, "Local + peer node", remote CI a slot).
A remote verdict stands as a witness only under the rule the clause states, and the held-CI reader
moves into the slot as its reader.

## 2. Scope (IN)

- **S1** — The registry: `[[verdict_backend]]` rows in a kit descriptor, read across every
  `tools/*/kit.toml` by `read_backends(tool_root)` in `tools/run-gates/verdict_backends.py`, each row
  `name`, `reader` (`<module>:<function>` under its kit), `off_node` (boolean) and `owner`. The
  run-gates kit declares three rows in `tools/run-gates/kit.toml`: `local-hook` (off_node false),
  `peer-node` (true) and `remote-ci` (true). A name declared twice is refused naming both
  descriptors. Observed by AC1.
- **S2** — The key `verdict`, read at the landed revision through dGroundRules' reader, `python
  tools/policy/policy.py get verdict` (TOOL-dGroundRules-2 S7), whose catalogue row admits exactly the
  three names S1 declares and defaults to `local-hook` (`tools/policy/catalogue.toml@174f9d9e5:895`).
  A value outside those names is the reader's own refusal, or its whole-file fallback where
  `policy-file.on-invalid` is `last-valid` and a valid revision precedes, never this unit's (§8 F8).
  `check_backend(name, backends)` refuses a value the reader answers that no declared row names,
  naming the value and the declared names; the lander and `verdict_backends.py read` call it before
  any read. A reader that refuses is passed on, exit 2 naming its line, and never read as
  `local-hook`; only a run-gates kit with no policy kit beside it reads the catalogue default, said on
  one line. Observed by AC2.
- **S3** — One read for every backend, `read_verdict(backend, sha, tree)` returning
  `Verdict(state, witness, why)`, `state` one of `GREEN`, `RED`, `NONE`, `HELD` and `DEAD PROBE`, and
  the CLI `python verdict_backends.py read --backend <name> --sha <sha>`, printing one line
  `verdict: <backend> · <state> · <sha8> · <why>`. Only `GREEN` stands; `NONE`, `HELD` and
  `DEAD PROBE` are no verdict and never green. Observed by AC2 and AC5.
- **S4** — `local-hook`'s reader reads the runner-written per-tree verdict
  `<common-dir>/gate-verdict/<tree hash>` (shared interface I8, unit 4's, written in `<key>TAB<value>`
  lines at `tools/run-gates/run-gates.sh@51fb8d207:6224-6244`) for the SHA's tree, the full slot only
  and never the `.scoped` slot the same writer keeps beside it, and stands when its `verdict` line
  reads `GREEN`. Observed by AC3.
- **S5** — `peer-node`: the verb `python verdict_backends.py verify-peer [--remote <name>]`, run on
  a second fleet node, lists `refs/gov/candidate/*` on the remote with one bounded `git ls-remote`,
  fetches each candidate, runs the bar on it under `GATE_FULL=1` in a detached worktree of the node's
  own clone, so the runner writes the full slot S4 reads, and pushes an annotated tag
  `refs/gov/verdict/<sha>` whose message carries that slot's `verdict`, `tree` and `run_id` lines and a
  `node` line in I8's `<key>TAB<value>` grammar. The reader fetches that ref and stands only when the
  tag points at the SHA, `tree` equals the SHA's tree, `verdict` reads `GREEN`, and `node` is not the
  reading node's tag. Observed by AC4.
- **S6** — `remote-ci`'s reader, `read_remote_verdict` in `tools/run-gates/remote_verdict.py`, by
  integrations' witness rule (layer-expansions.md:334-341): **key**, the run's `head_sha` is the SHA
  judged and that SHA's `^{tree}` is the verdict's tree; **writer**, the run's check suite app slug
  `github-actions`, its `path` the row's declared workflow `.github/workflows/remote-ci.yml`, its
  `event` `push`, and the declared job `bar`; **liveness**, the job's declared bar step concluded
  `success` and not `skipped`; **source**, the files `verdict.remote.pin-scope` names derive, at
  `head_sha`, the id `verdict.remote.pin` holds, by S9's rule, as `verdict.remote.trust` says (S8);
  **a failed read**, `DEAD PROBE`. The three keys are read at the landed revision, never at
  `head_sha`. Observed by AC5 and AC6.
- **S7** — The held-CI reader moved: `read_held_reds`' program, unchanged in behaviour, becomes
  `read_held_runs(anchor_url, workflow)` in `tools/run-gates/remote_verdict.py`, beside S6's reader and
  sharing its one bounded GET (`read_api`: no redirect, no credential, 30 s, 4 MiB); its CLI
  `python remote_verdict.py held <anchor URL> <workflow file>` prints the rows and liveness line the
  bash function printed. `tools/unattended/unattended.sh#write_held_asks` reaches it through
  `resolve_kit_dir "$py" run-gates remote_verdict.py "$KIT_DIR"`, as
  `tools/unattended/unattended.sh#write_flake_releases` reaches `verdict_flow.py`, and a python or a
  kit that does not resolve prints one `held reader: DEAD PROBE` line and files nothing. It keeps
  filing each red through `write_leg_ask` (unit 8's, shared interface I13), as it does at HEAD. The bash
  function leaves `unattended.sh`. Its name is spelled at the definition, at its one call inside
  `write_held_asks` (`tools/unattended/unattended.sh@51fb8d207:11114`), at the suite's stub
  (`tools/unattended/unattended.test.sh@51fb8d207:16800`) and at its `unset -f`
  (`tools/unattended/unattended.test.sh@51fb8d207:16832`), and nowhere else outside `memory/`
  (DERIVED by `git grep -n read_held_reds`). Observed by AC7.
  **Readers:**
  by name: `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`.
  by value: `write_held_asks`, which reads its `held` rows and its liveness line; the stub's
  `h9-calls` file, which the suite counts.
- **S8** — The trust values: under `pinned-workflow` (default, v2:1280) pinned files that differ
  read `HELD` and an owner item asks to re-pin or to refuse; under `owner-reviews-workflow-change`
  the owner item opens at the first differing read and the read stays `HELD` until the owner re-pins;
  under `app-only` the source check is skipped and a passing read is `GREEN` with witness `claimed`,
  never `witnessed`. The owner item: the unattended driver's gates-green term, the site in
  `tools/unattended/unattended.sh#dod_met` that calls `write_held_asks` and then
  `write_flake_releases` (`tools/unattended/unattended.sh@51fb8d207:12251-12254`), reads the slot
  under `verdict = remote-ci` after them, inside the same capture put back, and files a pin `HELD`
  through `write_leg_ask <slug> remote-ci 'pin held: backend' ...` (unit 8's), reused while open;
  outside a run the lander's refusal line names it. Observed by AC6.
- **S9** — The pin: `verdict.remote.pin` holds one object id, as its catalogue row's pattern admits
  (`tools/policy/catalogue.toml@174f9d9e5:986-990`, §8 F6): `git hash-object --stdin`, which writes
  nothing, over one `<path> <blob id>` line per file `verdict.remote.pin-scope` names, sorted by path,
  each line ending LF. `workflow` names `.github/workflows/remote-ci.yml`, and `dispatch-closure` adds
  `tools/run-gates/run-gates.sh`, `tools/gate-legs.json` and `.githooks/gate-env.sh`. It is written
  through `python tools/loop/policy_edit.py set verdict.remote.pin <value>` (TOOL-dDeclaredLoop-2 S4),
  whose proof is the owner's terminal or a live run's branch. `tools/loop/guard.py --staged` runs at
  pre-commit only for an agent's commit, where no commit message exists yet (TOOL-dDeclaredLoop-2 §4
  "The verdict"), so it reads no trailer: its `check_staged` refuses an agent-staged change to a key
  of one constant `OWNER_ONLY_KEYS`, holding `verdict.remote.pin`, under every value of
  `policy-file.guard` and of `floor.guard-self`, naming the key, before the value's rule, unless the
  minimal guard's `check_run_mandate` admits the branch as a live run's (§8 F7). The `Gov-Policy:`
  trailer the commit carries is checked by the push arm, `--push-range` (its S6).
  `python remote_verdict.py pin` prints, and never writes, the lines and the id the owner would set
  at HEAD. With no pin set, `policy.py get verdict.remote.pin` refuses on the row's derived default
  (`tools/policy/policy.py#DerivedDefault`), and `remote-ci` reads that refusal alone as `HELD` with
  `why` `no pin`; any other refusal is `DEAD PROBE`. Observed by AC8.
- **S10** — The lander: `tools/push-main.sh` reads `verdict` before each landing push, the push in
  `tools/push-main.sh#cmd_land` and the push of the default path's attempt loop, two sites (DERIVED
  by `grep -c 'git push "$remote"' tools/push-main.sh`). The read is `read_verdict_tree`'s: the kit
  found by `tools/push-main.sh#resolve_lander_kit`, then `policy.py get verdict`. Under `local-hook` it
  lands as today. Under `peer-node` it publishes `<sha>:refs/gov/candidate/<sha>` and lands only when
  `read_verdict` is `GREEN` for the SHA it is about to push, otherwise exits 1 naming the state; under
  `remote-ci` it reads the slot the same way. A reader that refuses, or a value no row declares,
  refuses before any push. Observed by AC2 and AC9.
- **S11** — `tools/run-gates/README.md` states the registry, the three rows, the five states and the
  witness rule; `help/` gains the page `help/verdict-backends.md`, linked from `help/README.md`. The
  keys `verdict`, `verdict.remote.trust`, `verdict.remote.pin-scope` and `verdict.remote.pin` each
  gain a `summary` and a `usage` in `tools/policy/catalogue.toml`, their rows drained from
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`, and `help/reference/policy.md`
  renders their sections (§8 F9). Observed by AC10.

## 3. Non-goals (OUT)

- The integrations expansion: its kit, its header factory, the `remote-verdict` record kind and the
  candidate publication remote CI would need to run before a landing (GitHub runs a push workflow
  for branches and tags, never `refs/gov/*`). This unit fills the slot's reader and leaves its re-home
  to that expansion.
- `GATE_POST_MERGE=ci` and `deploy.core` reading the remote verdict after the landing: dShippedRelease.
- Making a remote job a required check: a repository setting, the owner's
  (`.github/workflows/remote-ci.yml@174f9d9e5:16`).
- Repairing the hosted bar, red since 2026-10-13 (gap-test-12): the reader reports it `RED`.
- Recording a bypass under `hooks.bypass`: TOOL-dWitnessedBar-2, which reads this registry.
- A scheduler for `verify-peer`: the peer's operator runs it, by hand or from its own cadence.
- The selection's `peer-or-cadence` refusal in `tools/run-gates/verdict_flow.py`, which checks only
  `HELD_CI_WORKFLOW` though its words name "a registered peer backend": reading this registry there is
  a later unit's.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-4` — `gate-verdict`, the runner-written per-tree verdict `<common-dir>/gate-verdict/<tree hash>` that `local-hook`'s reader reads and `verify-peer` publishes
- **consumes-from** `TOOL-dWitnessedBar-8` — `write_leg_ask`, through which the moved held reader's reds and the pin's owner item are filed, keyed by name and reused while open
- **hands-off** `TOOL-dWitnessedBar-2` — `verdict`, the registry's `off_node` field and `read_verdict`, which `hooks.bypass = refused` needs as its off-node witness
- **hands-off** `TOOL-dWitnessedBar-43` — `read_peer_verdict` and `verify-peer`, which unit 43 binds to the source pin and to a tag signed by a registered node key (id 63)
- **hands-off** `TOOL-dWitnessedBar-56` — `read_local_verdict`, to which the verdict-boundary minors batch adds the hook's reuse-pair and selection refusals (ids 15, 33)

## 4. Design

### The registry

```toml
# tools/run-gates/kit.toml
[[verdict_backend]]
name = "local-hook"
reader = "verdict_backends:read_local_verdict"
off_node = false
owner = "dWitnessedBar"

[[verdict_backend]]
name = "peer-node"
reader = "verdict_backends:read_peer_verdict"
off_node = true
owner = "dWitnessedBar"

[[verdict_backend]]
name = "remote-ci"
reader = "remote_verdict:read_remote_verdict"
off_node = true
owner = "dWitnessedBar"
workflow = ".github/workflows/remote-ci.yml"
job = "bar"
step = "the merge bar, every leg guard ignored, walled inside the job limit"
```

The descriptor table is the precedent PLAY-dOrderedCharter-6 S1 set with `[[drive]]`, read by
`tools/playbook/render_playbook.py#read_drive_rows`, and TOOL-dDeclaredLoop-6 S3 with `[[command]]`,
read by `tools/loop/factories.py#check_commands`: a row govkit's install does not read, read across
descriptors by its own reader. An expansion registers a backend by declaring a row in its own kit.

### The remote read

```
GET /repos/<o>/<r>/actions/workflows/remote-ci.yml/runs?head_sha=<sha>&event=push&per_page=10
GET /repos/<o>/<r>/actions/runs/<id>/jobs?per_page=100
GET /repos/<o>/<r>/check-suites/<check_suite_id>
```

The owner and repository come from the anchor URL, as `read_held_reds` parses them today
(`tools/unattended/unattended.sh@51fb8d207:10919`). Every request goes through `read_api`, the same
bounded GET the held reader uses; a non-200, an oversize body or a non-JSON body is `DEAD PROBE`. The
pinned blobs at `head_sha` are read from the local object database (`git rev-parse <sha>:<path>`); a
SHA the clone lacks is `DEAD PROBE`, never fetched implicitly.

| Plant | Fixture response | State |
|---|---|---|
| `remote-green` | push run of the declared workflow, `bar` job's step `success`, pinned files deriving the pin | `GREEN` |
| `swapped-workflow` | the same, with `remote-ci.yml` at `head_sha` differing from the pinned one | `HELD` |
| `other-path` | a run whose `path` is another workflow file | `NONE` |
| `step-skipped` | the bar step concluded `skipped` | `NONE` |
| `api-404` | the runs listing answers 404 | `DEAD PROBE` |
| `unregistered` | `verdict = "ci-cloud"` in the fixture policy's only revision | refused by the reader, exit 2 |
| `undeclared` | `verdict = "remote-ci"` over fixture descriptors declaring no `remote-ci` row | refused by `check_backend`, exit 2 |

`--responses <dir>` points `read_api` at canned JSON files named by request path, an arm seam and
not a conf key, as `GATE_VERDICT_FAULT` is one for the runner
(`tools/run-gates/run-gates.sh@51fb8d207:4052`, `tools/run-gates/run-gates.sh@51fb8d207:6078`).

### Inventory

Minted: the descriptor table `[[verdict_backend]]` and its keys; `tools/run-gates/verdict_backends.py`
with `read_backends`, `check_backend`, `read_verdict`, `read_local_verdict`, `read_peer_verdict`
and the verbs `read`, `verify-peer`, `--fixture`, `--plant`; `tools/run-gates/remote_verdict.py` with
`read_remote_verdict`, `read_held_runs`, `read_api`
and the verbs `read`, `held` and `pin` with the flag `--responses`; the
refs `refs/gov/candidate/<sha>` and `refs/gov/verdict/<sha>`; `OWNER_ONLY_KEYS` in
`tools/loop/guard.py`; the pin's derivation rule (S9); the states `HELD` and `NONE`; the witness word
`claimed`. Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name>
--as py.function` at the pass; every function name above answered OK on 2026-11-20, `read_api`
included, which replaces `fetch_api`, refused (§8 F10).

### Migration

Under the default `local-hook` the landing path is unchanged. `HELD_CI_WORKFLOW`
(`.unattended.conf@174f9d9e5:216`) keeps its meaning and its two readers, `write_held_asks` and
`tools/run-gates/verdict_flow.py#read_held_runner`; neither's read of it changes.

### Rollout

Live at landing, dark by default: `verdict` defaults to `local-hook`, and `remote-ci` reads `HELD`
until the owner pins. Every kit whose shipped bytes move carries a version above its landing base's,
which the `kit epoch` leg grades from that base: the set is DERIVED by that leg at the pass, and the
pass moves each version it names at the kit's own version home.

### Files touched (estimate)

- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/remote_verdict.py`
- `tools/run-gates/kit.toml`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.sh` (the version line only)
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/loop/guard.py`
- `tools/loop/loop_lib.py` and `tools/policy/policy.py`, the version line only, where `kit epoch`
  names the kit
- `tools/policy/catalogue.toml`: the `summary` and `usage` of the four keys S11 names
- `tools/policy/unsummarised-keys.txt` (re-rendered by `policy.py lists --write`)
- `help/reference/policy.md` (re-rendered by `render_playbook.py --reference`)
- `help/verdict-backends.md`
- `help/README.md`
- `memory/map/generated/symbols.json` (re-rendered by the codebase-map kit's `gen_map.py --write`,
  which the unguarded `codebase-map coverage + freshness` leg reads)
- `memory/guides/SESSION-KICKOFF.md`: its `watch:` line holds `tools/run-gates/run-gates.sh`, so its
  `last-audit` is re-stamped

Shared with landed sibling units, settled at `51fb8d207`; this unit builds alone at order 28.
`TOOL-dWitnessedBar-29` (`b0ad98958`) moved `tools/run-gates/run-gates.sh` (`scan_leg_warnings`,
whose `warn.<k>` rows go to the run record, never to S4's per-tree writer),
`tools/run-gates/README.md` and `memory/guides/SESSION-KICKOFF.md`'s `last-audit`;
`tools/policy/policy.py` moved under none of them (`git diff 174f9d9e5 HEAD` prints nothing for it).
`memory/map/generated/symbols.json` moved under `TOOL-dWitnessedBar-29`, `TOOL-dWitnessedBar-7`
(`28edeaa0b`) and `TOOL-dWitnessedBar-21` (`cd03e4e75`), whose driver and suite hunks sit in
`--dispatch`, `--check-commit` and their arms, away from S7's and S8's sites. The driver gains no
refusal site: S7's and S8's lines print and return 0, never `exit 1` or `status=1`, and
`read_held_reds` holds none, so `check-arms.py --emit-floors` keeps the driver at
343 sites, 339 armed, its `REFUSAL_CEILINGS` row 343 (TOOL-dDeclaredLoop-52) unmoved (DERIVED
2026-11-20 at `51fb8d207`). Earlier, `tools/run-gates/README.md` was moved by `TOOL-dWitnessedBar-1`
and `TOOL-dWitnessedBar-30`, and `tools/unattended/unattended.sh`, `tools/policy/catalogue.toml`,
`tools/policy/unsummarised-keys.txt` and `help/reference/policy.md` by `TOOL-dWitnessedBar-30`, whose
`write_flake_releases` now sits beside `write_held_asks` at S8's call site.

### Alternatives rejected

- **A registry file of its own.** A backend's reader lives in its kit, so its row lives in that kit's
  descriptor, and an expansion registers without editing a core file.
- **Peer verdicts in a shared branch file.** A ref per SHA is written once by the peer, and
  `refs/gov/bar-red` is the precedent (`tools/run-gates/post-merge.sh@174f9d9e5:252`), pushed by
  `tools/run-gates/post-merge.sh#write_red_ref`.

## 5. Production-readiness checklist

- security — a new outbound read: https to `api.github.com` only, no redirect, no credential sent or
  read, 30 s and 4 MiB bounds, all kept from `read_held_reds`; the pin is guarded by the policy
  writer's proof and a guard constant, and the trust keys are read at the landed revision, never from
  the tree judged; a peer verdict counts only from another node's tag and for the SHA's own tree. The
  peer pushes refs under `refs/gov/` only, with the node's own push grant.
- what the pin does not check — a live run's branch may move the pin, by the owner's 2026-11-12
  ruling (§8 F7), in a commit whose change record and `Gov-Policy:` trailer name it; and
  `dispatch-closure` pins what decides the bar's dispatch, never the code the bar job executes: the
  floor preflight `tools/lib/python-floor.sh`, a step of the `bar` job since TOOL-dSafePassage-12
  (`.github/workflows/remote-ci.yml@174f9d9e5:131-133`), and every leg's own script sit outside it.
- perf / scale — at most three GETs per remote read; one `ls-remote` and one fetch per peer read; a
  `verify-peer` pass runs one bar per candidate.
- error / empty / loading states — every failed read is `DEAD PROBE` and names why; an empty pin
  reads `HELD` with `no pin`; an unregistered value refuses before any push.
- observability — one `verdict:` line per read, and the lander's line naming the state it refused on.
- risks — under `peer-node` a landing waits on a peer that may never run; the lander exits 1 and
  says so rather than polling, and `flow.wait-ceiling` governs the owner item the loop raises.
- testing — AC1 to AC10 by fixture and probe; the arms in §7.
- migration — none under the default value, per §4.
- user docs — `help/verdict-backends.md` and the four keys' sections of `help/reference/policy.md`
  (S11).

## 6. Acceptance criteria

- **AC1** — When `python verdict_backends.py --fixture --plant registry` runs in `tools/run-gates/`, it
  prints the three declared names with their `off_node` values, and with a second descriptor declaring
  `local-hook` again it exits 2 naming both descriptors.
  Red when: a duplicate row overrides the first silently.
- **AC2** — When `python verdict_backends.py --fixture --plant unregistered` runs, `read` and the
  fixture lander each exit non-zero naming `ci-cloud` and the three declared names, and no push is
  made; under `--plant undeclared` each exits non-zero naming `remote-ci` and the two names the
  fixture descriptors declare, and no push is made.
  Red when: an unregistered or undeclared value falls back to `local-hook`.
- **AC3** — When `python verdict_backends.py --fixture --plant local-green` runs over a fixture common
  dir holding a `gate-verdict/<tree hash>` file whose `verdict` line reads `GREEN`, `read --backend
  local-hook` prints `GREEN`; with that line reading `RED` it prints `RED`, with no file `NONE`, and
  with only a `gate-verdict/<tree hash>.scoped` file reading `GREEN`, `NONE`.
  Red when: a missing or scoped-only per-tree verdict reads as green.
- **AC4** — When `python verdict_backends.py --fixture --plant peer` runs, a fixture remote holding
  `refs/gov/verdict/<sha>` from node `b` reads `GREEN` on node `a`, the same tag from node `a` reads
  `NONE`, and a tag whose `tree` line differs reads `NONE`.
  Red when: a node's own verdict, or one for another tree, stands as off-node.
- **AC5** — When `python remote_verdict.py read --responses <dir> --sha <sha>` runs over the
  `remote-green` fixture, it prints `GREEN`; over `other-path` and `step-skipped`, `NONE`; over
  `api-404`, `DEAD PROBE`.
  Red when: any of the writer, liveness or failed-read fields is not checked.
- **AC6** — When the same command runs over the `swapped-workflow` fixture, it prints `HELD` naming
  `.github/workflows/remote-ci.yml` under `pinned-workflow`, and `GREEN` with witness `claimed` under
  `app-only`: the clause's swapped workflow seen red.
  Red when: a workflow that differs from the pin stands as witnessed.
- **AC7** — When `python remote_verdict.py held --responses <dir> https://github.com/o/r remote-ci.yml`
  runs over a fixture of two held jobs, one `failure`, it prints two `held` rows and the liveness line
  `held reader: run <id> at <sha8> · 2 held job(s) read · 1 red`; and
  `git grep -n 'read_held_reds()' tools/unattended` prints nothing; and
  `python tools/memory-tree/check-arms.py --emit-floors` names `tools/unattended/unattended.sh` at
  no more sites than its ceiling (TOOL-dDeclaredLoop-52).
  Red when: the moved reader's rows differ from the bash function's, or the function stays.
- **AC8** — When `python remote_verdict.py pin` runs at HEAD with `verdict.remote.pin-scope` at
  `dispatch-closure`, it prints four `<path> <blob>` lines whose blobs equal `git rev-parse
  HEAD:<path>`, and one `verdict.remote.pin = "<id>"` line whose id equals `git hash-object --stdin`
  over those lines; and `python guard.py --staged`, run in the loop kit's directory over a fixture on
  a branch no live run names, whose policy sets `policy-file.guard = "agents-with-reason"` and which
  stages a change to `verdict.remote.pin` with its change record and `memory/DECISIONS.md` row, so
  that only `OWNER_ONLY_KEYS` can refuse, exits 1 naming the key.
  Red when: the pin helper writes the policy file, or the guard admits an agent's pin off a live run's
  branch.
- **AC9** — When the fixture lander `push-main.sh` runs in the fixture repository of
  `verdict_backends.py --fixture --plant lander-peer` under `verdict = "peer-node"` with no peer
  verdict, it publishes `refs/gov/candidate/<sha>` and exits 1 naming `NONE`.
  Red when: the lander lands on its own hook's verdict under an off-node backend.
  fixture: the fixture repository and its bare remote are built by the plant in the system temp dir.
- **AC10** — When `grep -n 'verdict-backends' help/README.md` runs, it names the page;
  `grep -c 'verdict_backend' tools/run-gates/README.md` prints at least 1;
  `grep -c '^verdict' tools/policy/unsummarised-keys.txt` prints 0; and
  `grep -n '^## .verdict.remote.pin.$' help/reference/policy.md` names that key's section.
  Red when: the registry or its keys ship with no user page.

## 7. Gates

`govkit selfcheck` · `run-gates wiring` · `push-main self-test` · `unattended kit gate` · `remote literals (kit code names no remote)` · `scratch-guard self-test` · `tier2-review self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `loop guard fixtures` · `policy fixtures` · `policy check` · `help reference pages` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant of §4 run through `verdict_backends.py --fixture` and `remote_verdict.py --responses`, staged red by removing the source check from `read_remote_verdict` and the off-node test from `read_peer_verdict` · none
New arm: tools/push-main.test.sh · covers AC9 · the `lander-peer` fixture under `peer-node`, staged red by skipping `read_verdict` before the push · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · the h9 arm re-pointed at the moved reader's `held` verb, staged red by restoring the bash stub's rows · none

## 8. Open questions

- **F1 — Where is the registry declared?** Options: (a) `[[verdict_backend]]` rows in each kit's
  descriptor, read across descriptors; (b) one core file listing every backend; (c) a `case` in the
  lander. (b) makes an expansion edit a core file to register, which P28 as EX-1 amended forbids;
  (c) is a hand-typed list. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by reuse
  of the descriptor-table seam `[[command]]` and `[[drive]]` set. widens: none · relaxes: none
- **F2 — Is the peer-node verifier built here or only registered?** Options: (a) registered and built:
  the reader and `verify-peer`; (b) a registered row whose reader reads `NONE` until a later build.
  layer-expansions' `[core-points]` row says `local-hook` and `peer-node` are "both core and built by
  dWitnessedBar", and R5.2's answer is "Local + peer node". RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 1. The two pushes it adds, `refs/gov/verdict/<sha>` and `refs/gov/candidate/<sha>`, sit
  under `refs/gov/` as `post-merge.sh` already pushes `refs/gov/bar-red`, and this Tier-2 unit prices
  them in §5. widens: none · relaxes: none
- **F3 — What does a remote-ci landing read before CI can run on a candidate?** GitHub runs a push
  workflow for branches and tags only, so no workflow runs on `refs/gov/candidate/<sha>`. Options:
  (a) the slot reads by SHA and the integrations expansion supplies the candidate publication; (b)
  this unit publishes candidates as branches and edits `remote-ci.yml` to run on them. (b) builds the
  expansion's surface and changes the pinned workflow this unit's pin protects. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 1, the clause's "a `remote-ci` slot the integrations expansion
  fills". widens: none · relaxes: none
- **F4 — How is "the platform's own app" read?** Options: (a) the run's check suite `app.slug` is
  `github-actions`; (b) the run's `actor`. (b) names the pusher, not the writer. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 2 by research-integrations-b's witness table, "Writer:
  `app.slug=github-actions`". widens: none · relaxes: none
- **F5 — Is a new user-facing surface and a guard constant within this build's authority?** RESOLVED
  (agent, 2026-10-25, delegated): yes, rung 3 with veto 2 lifted by the README's `may:` grant, because
  the carried clause names the backends, the pin and its keys. grants: PLAY-dClosedLoop-3 the
  `[[verdict_backend]]` descriptor table, the `verify-peer` verb, the `refs/gov/candidate/<sha>` and
  `refs/gov/verdict/<sha>` refs and the guard's `OWNER_ONLY_KEYS`. widens: none · relaxes: none
- **F6 — What value does `verdict.remote.pin` hold, now that its catalogue row is landed as one
  pattern-typed id?** The row admits one string matching `[0-9a-f]{40}|[0-9a-f]{64}`
  (`tools/policy/catalogue.toml@174f9d9e5:986-990`), and `tools/policy/policy.py#scan_keys` descends a
  table under a row that is not map-typed, so rev-5's `<path> = "<blob id>"` table reads as leaves no
  row matches and the whole file as invalid. Options: (a) keep the table and give the policy kit a
  pattern-valued map type; (b) one id, `git hash-object --stdin` over the sorted `<path> <blob id>`
  lines of the scope's files; (c) the id of a commit whose copies of those files are the pinned ones.
  (a) changes the policy kit's catalogue schema, veto 2. (c) makes every reading clone hold that
  commit, else `DEAD PROBE`, and pins by history rather than by the files. RESOLVED (agent, 2026-11-20,
  delegated): (b), rung 3, tie-broken by reuse of git's own blob id, which keeps the row's own words,
  "the pinned files' blob ids". widens: none · relaxes: none
- **F7 — Does a live run's branch admit an agent's change to `OWNER_ONLY_KEYS`?** The guard's
  guard-self step and the minimal guard both admit a live run's branch at HEAD
  (`tools/loop/guard.py#check_staged`), by the owner's 2026-11-12 ruling, "No file is owner-only to a
  run working under its build's mandate"
  (`2026-11-12-build-PLAY-dOrderedCharter-1-owner-guard-ruling`). Options: (a) refused on every branch;
  (b) refused off a live run's branch under every value of `policy-file.guard` and `floor.guard-self`,
  admitted on one through `check_run_mandate`; (c) the pin joins `SELF_KEYS`, switched with them by
  `floor.guard-self`. (a) contradicts the owner's ruling, which no delegation reaches; (c) changes the
  stated meaning of the floor member `guard-self`, the guard protecting its own switch
  (`tools/loop/floor.py`). RESOLVED (agent, 2026-11-20, delegated): (b), rung 1, the owner's ruling,
  and §5 states what it leaves unchecked. widens: none · relaxes: none
- **F8 — What does `check_backend` refuse, now that the catalogue row admits exactly the three
  names?** The landed row `verdict` is an enum of `local-hook`, `peer-node` and `remote-ci`
  (`tools/policy/catalogue.toml@174f9d9e5:895`), so `tools/policy/policy.py#check_value` refuses any
  other value before this unit reads it. Options: (a) `check_backend` stays the registry's lookup,
  refusing a value the reader admits that no declared row names, and a reader's refusal is passed on
  as exit 2; (b) drop `check_backend` and trust the catalogue's enum. (b) leaves a value with no
  declared row, and so no reader, to fail at dispatch with no named refusal. RESOLVED (agent,
  2026-11-20, delegated): (a), rung 3, the more feature-rich, observed by AC2's two plants. widens:
  none · relaxes: none
- **F9 — Does this unit write the summary and usage of the four keys it carries?** The rows sit on
  the shrink-only `tools/policy/unsummarised-keys.txt` at HEAD, and `help/reference/policy.md` renders
  only a row carrying both. Options: (a) yes, the rows drained and the page rendered, as
  TOOL-dWitnessedBar-30 S8 did for `verdict.flakes.release`; (b) no, the keys go live with no page.
  (b) fails the charter's `docs` rule. RESOLVED (agent, 2026-11-20, delegated): (a), rung 1. widens:
  none · relaxes: none
- **F10 — What is the bounded GET named?** `python tools/lexicon/lexicon.py --suggest fetch_api --as
  py.function` refuses `fetch` and offers `load_api`, whose verb reads a store into memory; it
  answers OK for `read_api` (both run 2026-11-20). Options: (a) `read_api`; (b) keep `fetch_api` under
  a verb-waiver row. (b) adds a waiver for a name no code holds yet, against the `lexicon naming
  predicates` leg. RESOLVED (agent, 2026-11-20, delegated): (a), rung 1 by veto 1 on (b); the
  dShippedRelease spec that names `fetch_api` is outside this unit's edit. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 6, the brief's shared interfaces I8 and
  I13 and owned-node table, scout A's row for cl-0344, layer-expansions' witness rule and the
  design rounds' R5.2, at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-43, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-4 · 2026-10-26 · S9 · AC8 · re-grounded on the cross-check record
  `2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`, row 13: `--staged` reads no trailer at
  pre-commit, so it refuses every agent-staged `OWNER_ONLY_KEYS` change under every value, naming the
  key, and the trailer stays with `--push-range`; AC8's fixture sets `agents-with-reason`.
- rev-5 · 2026-11-19 · §7 · the leg line gains the legs `scratch-guard self-test` and
  `tier2-review self-test`, whose guards §4's `tools/unattended/unattended.sh` trips, as the
  spec-token checker's guards join named them at `c6df3e901`, by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief`; §4 is unchanged, as the unit writes
  that path; nothing else moved.
- rev-6 · 2026-11-20 · §1 · S2 S4 S5 S6 S7 S8 S9 S10 S11 · §3 · §4 · §5 · AC2 AC3 AC8 AC10 · §7 ·
  §8 F6 F7 F8 F9 F10 · §10 · re-grounded over HEAD `174f9d9e5` by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-6-reground3-brief`: code citations by symbol or blob-pinned;
  S2 reads the landed catalogue row, its enum and default, and a reader's refusal is never
  `local-hook` (F8, AC2's `undeclared` plant); S4 and AC3 read the full slot only; S5 runs the bar
  under `GATE_FULL=1`; S7 resolves the kit as `write_flake_releases` does and keeps unit 8's
  `write_leg_ask`; S8 names the call site beside `write_flake_releases`; S9 takes the pin as one id
  (F6), the policy writer's live-run proof and the live-run admission (F7), and the derived-default
  refusal as `no pin`; S10 names the lander's two push sites; S11 adds the four keys' pages (F9);
  `fetch_api` is `read_api` (F10); Migration names `HELD_CI_WORKFLOW`'s second reader; Rollout
  derives the kit versions; Files touched gains the catalogue, list, reference page, symbol map,
  kickoff manifest, the gov arm suite and the policy and loop kits' version lines; the leg line gains
  the legs those paths' guards name (PINNED, measured 2026-11-20 by the spec-token checker's guards
  join).
- rev-7 · 2026-11-20 · S4 S7 S8 · §4 · AC7 · §10 · re-grounded over HEAD `51fb8d207` past the
  landed TOOL-dWitnessedBar-29, TOOL-dWitnessedBar-7 and TOOL-dWitnessedBar-21 by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-6-reground4-brief`: the moved runner, driver and suite
  citations re-pinned there; Files touched's shared paragraph names what each landed unit moved,
  `tools/policy/policy.py` moved by none, and the driver's refusal-site census unmoved at its
  ceiling (DERIVED), observed by AC7; the registry's absence re-pinned; nothing else moved.

## 10. Reuse audit

The seams extended: the anonymous bounded GitHub read inside
`tools/unattended/unattended.sh#read_held_reds`, moved whole and given a second caller; its caller
`tools/unattended/unattended.sh#write_held_asks`, which reaches the moved reader as
`tools/unattended/unattended.sh#write_flake_releases` reaches its kit; the
lander's policy read `tools/push-main.sh#read_verdict_tree` and its kit resolver
`tools/push-main.sh#resolve_lander_kit`;
the run-gates kit's own policy read `tools/run-gates/verdict_flow.py#read_policy_at` and its inline
resolver `tools/run-gates/leg_factory.py#resolve_kit_dir`, imported within the kit; the `refs/gov/`
publication precedent of `tools/run-gates/post-merge.sh#write_red_ref` and its reader
`.githooks/pre-push#read_post_merge_red`; the descriptor-table readers
`tools/playbook/render_playbook.py#read_drive_rows` and `tools/loop/factories.py#check_commands`; the
guarded policy writer `policy_edit.py set` and the loop guard's `tools/loop/guard.py#check_staged`
(TOOL-dDeclaredLoop-2 S1, S4), both built by the chain before this build. `python
tools/codebase-map/reuse_lookup.py "read a remote CI verdict for a commit sha from the GitHub API"`
ranked generic stems (`read_text`, `read`, `git`, `run_git`) and missed `read_held_reds`, whose body
is a Python program inside a bash function, outside the symbol tier (re-run 2026-11-20); scout A found
it by reading. No registry of verdict backends exists at HEAD: `git grep -n verdict_backend --
':!memory'` prints nothing (PINNED 2026-11-20 at `51fb8d207`).

Recall terms used: `python tools/memory-recall/query.py "when does a remote CI verdict stand as a witness for a landing and what backends exist" --terms "verdict backend remote-ci peer-node local-hook head_sha workflow pin trust held reader registry"`
