# Research: the distribution expansion, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 55's return, verbatim, except that its title line is demoted to keep one H1 per
record. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-21-researcher.md`, which dispatch 56 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

**Distribution layer: candidates, losing tests and a recommendation (dClosedLoop, PLAY-dClosedLoop-1, question 21)**

## 1. Verdict

Distribution delivers kits. It owns:
- govkit;
- the install half of each adopt script (first placement, seeding, receipts, withdrawal);
- releases and their notes, which are generated;
- the fleet register and the currency probe;
- installing the render targets that each harness adapter maps.

The core owns everything the core already reads: the descriptor schema (`regen.py` reads `kit.toml`), rendering in place (the adopt scripts' `--render`/`--check` modes run in the bar), and each kit's version constant.

I recommend **A, a descriptor-driven copy-install at a tagged release**. The pinned-reference candidate (B) and the per-machine candidate (C) each lose a measured test.

Without distribution, the core lands builds unchanged. The lander skips minting and says so, the bar falls back from govkit, and each version slot reads "not installed".

## 2. Today

| Part | What it does | Measured | file:line |
|---|---|---|---|
| `kit.toml` descriptors | files with their roles, adopter, check, gate legs, regenerate, holes, lf pins | 17 under `tools/*/` plus 12 in `govkit/entries/` = 29 registry entries. 0 declare `layers`, extension points or record kinds. 92 `[[files]]` rules, 49 `[[gate_leg]]` | `tools/*/kit.toml`; `registry.toml:57-181` |
| Unknown-key validation | none | grep for a known-key set or "unknown key": 0 hits. A mistyped field is silently ignored | `govkit.py:12862` reads descriptors |
| govkit verbs | selfcheck, shipped, epoch, mint, contribute, plan, check, apply, intake, update, adopt | 11 verbs. USAGE omits `contribute` | `govkit.py:13677-13743`, USAGE `:13212` |
| Version minting | `mint` raises a moved kit's last version digit at the landing. `epoch` grades that moved bytes date a bump | 19 of 29 entries carry a version. 10 print `skip · no declared version`, push-main among them | `govkit.py:12976-13207`; `push-main.sh:792-810` |
| Releases | none | `git tag` gives 3 tags, all `archive/*`. Changelog or release-notes files: 0 | — |
| Landing rate | — | 29 first-parent merges on origin/main in 7 days, 74 in 30 | `git log` |
| Install receipt | `.governance/install.json` at schema 3, rows with sha256 and commit | `gov_source` is `str(root)`, a local path on the deployer machine. Gov's own tree has no receipt (`.governance/` holds only `deploy.toml`) | `govkit.py:49, :8020, :12652` |
| Receipt integrity | `check-receipt.py` checks engine hashes in an adopter's bar | integrity only, no currency | `run-gates/check-receipt.py:3-20` |
| Adopter list | `adopters.toml` | 3 rows of names, used as a brand ban. No remote and no version | `adopters.toml:16-27` |
| Adopt scripts | the configure step, plus render and check modes | 13 scripts. 11 `--check` legs are in the bar. 12 `[[regenerate]]` argvs, 11 of them adopt scripts, are run by the core's `regen.py` | `gate-legs.json`; `regen.py:13-18` |
| Charter overlay | `[charter] adopter_rules` in `deploy.toml` renders as section 2 | It sits inside the one `gov:playbook` region (AGENTS.md:1-177, section 2 at :84). It is not a separate block | `deploy.toml:59-70`; `render_playbook.py:118,668` |
| Other overlays | role house overlays seeded in the kit home; seed files in kit homes; merged blocks; `[config]` files | 11 house files; 6 seed and 7 rendered rows land under `{kit}/`; 3 merged rows; 9 `[config]` | `roles/kit.toml:31-40` |
| Render targets | descriptor `to =` paths and per-kit renderers | 8 rows hard-code `.claude/`. `render_agents.py` writes `.claude/agents`. agent-instructions maps aliases itself and measures `CODEX_MAX=32768` | `adopt-agent-instructions.sh:31,50-55` |
| Copy path without govkit | runbook `cp -r` | 162,896 bytes, 40 headings | `WIRE-INTO-PROJECT.md:229,435,456,518` |
| Inline `resolve_python` | hand-kept copies | 73 files define it, 88 carry the marker | `check-kit-versions.sh:31` and others |

Measuring commands (outputs abridged):

```
$ python3 tools/govkit/govkit.py epoch | grep -c 'skip · no declared'     -> 10
$ git tag                                                                  -> archive/aGatheredDeclaration archive/aMendedWarden archive/aPairedLexer
$ git grep -lE '^\s*resolve_python\(\) *\{' | wc -l                        -> 73
$ grep -hE 'to = "\.claude/' tools/*/kit.toml tools/govkit/entries/*.toml | wc -l -> 8
```

## 3. Attach points

| Attach point | Declared by | What distribution does there | Core without distribution |
|---|---|---|---|
| Deploy's "versions and release notes" slot | flow-steps `[deploy]` :358-359 | mints at the lander's prepare; the release cut reads the landing records | Lander prints "kit versions were NOT minted — no govkit deployer" and lands (`push-main.sh:806-808`). The slot renders as not installed, with the fallback "kit versions frozen at the installed release" |
| Command adapters | runtime `[extend]` :739 | registers `mint`, `release`, `currency-probe`, `update`, `install` | not registered. The bar's govkit query falls back (`run-gates.sh:2992-3005`) |
| Harness adapters' render-target table | runtime `[harness]` :712-725, `[extend]` :743; instruction R-K :594-604 | installs each target kind for each harness in `runtime.harnesses` | The core renders in place for whatever targets already exist (regen stage 1). Nothing is first-placed |
| Notification adapters | runtime `[extend]` :745 | currency-drift owner items | the terminal |
| Memory contract record kinds | P30 | declares release, receipt, fleet row and currency observation | absent kinds are not registered |
| Instruction manifest overlay | instruction R-I :549-551 | seeds the adopter's overlay on first install | The overlay is hand-authored. The core renders whatever exists |
| **Missing: cadence items** | Runtime `[schedule]` :690 says it "runs the cadence items that their layers declare", but `[extend]` :736-746 lists no such point | the release cut under daily or weekly cadence, and the fleet probe | — |

The handed fact says Maintain cuts the release. Maintain is observability's, so that would make one expansion depend on another, which P28 forbids. A tenth point, "cadence items", removes the dependency.

## 4. Candidates

**A. Descriptor-driven copy-install at a tagged release (recommended).**
- **Mechanism:** extend govkit. Engine bytes are copied from a release tag, and the receipt records the release and gov's remote URL. Overlays live outside kit homes, and render targets are named by kind and mapped by the harness adapter.
- **Seam:** `govkit apply/update`, the receipt, `mint` and `epoch`.
- **Losing test 1:** the core in an adopter needs govkit at runtime. **Result: PASS.** Govkit is never installed (`registry.toml:296-297`). The lander skips minting with a named line (`push-main.sh:806-808`), and the bar falls back (`run-gates.sh:2992-3005`).
- **Losing test 2:** a kit's version cannot be read from its own bytes. **Result: PARTIAL FAIL.** 10 of 29 entries carry no version (the epoch output above). The conformance gate must require a version.
- **Losing test 3:** an adopter cannot name its source off the deployer machine. **Result: FAILS as built.** The receipt stores `gov_source` as a local path (`govkit.py:8020`). This is cured inside A by recording the release and remote.

None of these failures is structural; each is a field to add.

**B. Pinned reference (a submodule or subtree at a tag, or a harness plugin); the engine is read-only.**
- **Mechanism:** the adopter holds a reference plus its overlay, and nothing is copied.
- **Losing test:** any adopter-written byte lands inside a kit home.
- **Result: LOSES.**
```
$ python3 - (walk files rules: role in seed/rendered/merged, to under {kit} or absent)
Counter({('rendered','outside'):17, ('rendered','in-kit'):7, ('seed','in-kit'):6, ('seed','outside'):4, ('merged','outside'):3})
```
13 of 37 adopter-written rows land inside the engine directory. Examples are `codebase-map/map_extractors.py`, `roles/house/*` and `workflows/tier2-review.js`.

**C. Per-machine install (a user-level junction like session-kickoff, or a harness plugin).**
- **Mechanism:** kits live on each machine, and the repo holds only overlays.
- **Losing test:** remote CI or a fresh clone must run the bar from the checkout alone.
- **Result: LOSES.**
```
$ python3 -c "...gate-legs.json..."  -> legs 140 naming {prefix}: 133
$ grep -n run-gates .github/workflows/remote-ci.yml -> 106: ... bash tools/run-gates/run-gates.sh
```

A push model is not a fourth candidate. Push-versus-pull is a currency mode under A (`deploy.currency`), not a different install mechanism.

## 5. The contract, filled (pick A)

| Field | Value |
|---|---|
| Tag and definition | `distribution`: puts a release of kits into a repository, keeps it there, and measures how far behind it is |
| Instruction units | the install runbook, generated from descriptors (it replaces the parity-checked narrative); the deploy-governance Skill, slimmed to an operator order; the currency line in the landing view |
| Engine kits | `govkit`, the deployer (gov-side only); a shipped `kitcheck`, the one wiring and version verdict, which the core bar may run when present; the install half of each adopt script (`--install`, `--seed`, `--withdraw`) |
| Record kinds | `release` (an annotated tag `release/<YYYY.MM.DD>` whose message is generated from per-kit version deltas and landing records, with no changelog file); `install-receipt` (`.governance/install.json`, schema 4 adds `release` and `source_remote`); `fleet-row` (gov's register, grown from `adopters.toml`: key, remote, default branch, channel); `currency-observation` (adopter, observed SHA, receipt release, releases behind, period) |
| Extension points declared | `install modes` (copy today, reference later); `kit sources` (a git remote, a local path); `render-target kinds` (skill, agent, rule, hook, instructions, settings), which harness adapters fill |
| Extension points used | Deploy's version slot; command adapters; harness adapters; notification adapters; cadence items (owed, see section 3) |
| Policies | `release.cadence`, `deploy.currency`, and the new keys in section 6 |
| Gates | `kit conformance` (descriptor schema, required version, `requires` closure, render targets named by kind, P28 fields joined to registries); `kit wiring` (one verdict); `kit version` (one check); `receipt integrity` (exists); `currency` (adopter leg); generated-runbook freshness |

The P28 fields to add to each descriptor:
- `layers = [...]`;
- `[contract] units`, `declares`, `uses`, `record_kinds`, `policies`;
- `version_from` as required, with `none` refused;
- `to = {target = "<kind>", name = "<n>"}` alongside paths.

`resolve_python` becomes an `[[inline]]` row: the copy-install and regen generate each block from `tools/lib/resolve-python.sh`, and the byte-identity gate becomes regen's `--check`.

## 6. Items and policies

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `deploy.version` (fills the Deploy slot, run in the lander's prepare) | command: `govkit mint` | mints each kit whose shipped bytes moved | the version-line change in the prepared merge, graded by `kit version` at the push boundary | minted or clean → continue; refused → Test; absent → "not installed, versions frozen" |
| `deploy.release` | command: `govkit release` | under `every-landing`, cuts the tag after `deploy.record`. Notes are derived from per-kit value deltas between tags plus landing records | the annotated tag at the landed SHA | cut → `deploy.notify`; already tagged → no-op |
| `cadence.release` | command, registered as a cadence item | the same cut under daily or weekly, keyed by period; `owner-cut` makes it an owner item | the tag, keyed by period | due → cut; nothing landed since the last tag → skip, announced |
| `cadence.currency` | command: the probe | for each fleet row, reads the adopter's receipt at its remote tip and counts release tags between | `currency-observation`: the adopter's committed receipt at a named SHA (P2) | at or under `currency.max-behind` → record; over → `currency.on-behind`; unreachable → owner item |
| `cadence.offer` | command | under `push-branches`, runs `update --write` in a worktree and pushes `gov/update-<release>` | the pushed ref on the adopter's remote | pushed → adopter lands with its own lander; refused → outbox order |
| `test.currency` (an adopter bar leg) | command | compares the receipt's release with `git ls-remote --tags <source_remote>` | the leg's verdict | as `currency.on-behind` |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `release.cadence` | every-landing, daily, weekly, owner-cut | weekly | handed. At 29 landings a week, every-landing would mean 29 releases a week |
| `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch | handed. pull-only is today's behaviour, push-branches needs adopter write access |
| `runtime.harnesses` | registered harness adapters | claude-code | handed. Distribution installs targets for each one |
| `currency.max-behind` (new) | an integer of releases, 0 or more | 2 | under weekly releases this is two weeks; adopters today sit about 990 commits behind |
| `currency.on-behind` (new) | note, owner-item, red | owner-item | red would block an adopter's own landings for gov's cadence |
| `distribution.install` (new; structural, so possibly a decision rather than a key) | copy, reference | copy | B loses today (13 in-kit rows) |

## 7. Gaps

Closed by the pick:

| Gap | How |
|---|---|
| `gap-deploy-04` | the fleet register, `cadence.currency`, and the push-branches mode |
| `gap-deploy-06` | partly. Release notes are derived and the release cut is an item. A release review stays a breakpoint the owner may declare |
| `gap-deploy-07` | partly. Conformance requires push-main's version and its `requires = ["run-gates"]`. The Windows kill and hooks-path drift stay Runtime's. This worktree's `core.hooksPath` is `C:\projects\coding-governance\.githooks`, the main checkout's, which is a live instance |
| `gap-deploy-08` | the runbook is generated from descriptors, and its freshness is a regen check |
| `gap-tool-02` | one `kit wiring` verdict replaces three judges, and one `kit version` replaces the lockstep checks (below) |
| `gap-tool-04` | the `[[inline]]` rows generate the 73 copies |

The consolidation behind `gap-tool-02`:
- **Wiring is judged three ways today:**
  - `check-wiring.sh`, at SessionStart (`settings.json:56`);
  - 11 `adopt-*.sh --check` legs in the bar;
  - `govkit check`, which runs the same `[check]` argvs (`govkit.py:5139`).

  The new `kit wiring` iterates descriptors, so the bar carries one leg instead of 11 typed ones. Its git-config checks (hooksPath, merge driver, ssh) move to Runtime's hook pack.
- **Version lockstep is checked five ways today:**
  - `check-kit-versions.sh`;
  - `check-placeholders.sh`'s marker half;
  - `govkit epoch`;
  - `check-verdict-epoch.sh`;
  - selfcheck arm 5c (`govkit.py:2162`).

  `kit version` is one function: `derive_epoch_state` plus marker agreement plus well-formedness.

New gaps this exposes:

| New gap | Evidence |
|---|---|
| 10 of 29 entries are unversioned | epoch output, section 2 |
| The receipt's source is a local path, so no adopter's CI can resolve gov | `govkit.py:8020`, `:12652` |
| No release has ever been cut | `git tag` |
| Descriptor keys are unvalidated | grep for a known-key set: 0 hits |
| Render destinations are Claude-Code-only | 8 `.claude/` rows; `render_agents.py` |
| 13 adopter-written rows sit inside kit homes | the walk in section 4 B |
| The charter overlay is not a separate block (P8) | `AGENTS.md:84` is inside `:1-177` |
| The cadence-item attach point is undeclared | runtime `[extend]` :736-746 against `[schedule]` :690 |

Where a record and the code disagree:
- **Version lockstep count.** `gap-tool-02` says four ways; the code has five (selfcheck 5c).
- **govkit verbs.** The Deploy research (:22) omits `shipped`; the code has 11 verbs.
- **A stale header.** `check-kit-versions.sh:7-9` says "no consumer reads these constants until the Phase-1 govkit deployer"; `mint` and `epoch` read them.
- **Adopt scripts.** The handed definition puts them wholly in distribution, but the core's bar runs their render and check modes (`regen.py`; 11 legs). Only their install half is distribution.

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| Install mechanism | copy at a release; pinned reference | **copy**. Moving overlays out of kit homes keeps reference possible later |
| Who owns the descriptor schema | core (the layer-contract fields and target kinds); distribution | **core**: `regen.py` and the bar already read `kit.toml`. Distribution adds install fields as a pack |
| One conformance gate or two | dOrderedCharter's layer gate plus dShippedRelease's kit gate; one gate | **one**, owned by dOrderedCharter, with distribution's install checks registered into it |
| Where the release cut attaches | Maintain (observability); a Runtime cadence item | **cadence item**: add it as Runtime's tenth extension point, with Maintain as one consumer. The handed "Maintain cuts" otherwise breaks P28 |
| Gov's own receipt (P8) | exempt, as today; a `source`-mode receipt | **source-mode**: the same checks run, and currency reads "source, 0 behind" as an announced line, never a silent one |
| `currency.on-behind` default | note, owner-item, red | **owner-item** |

Relevant paths:
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\govkit.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\registry.toml
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\adopters.toml
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\push-main.sh
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\run-gates\run-gates.sh
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\run-gates\regen.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\gate-legs.json
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.governance\deploy.toml
