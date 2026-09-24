# TOOL-aRepatriatedFork-16 — check-install-prefix grades only what a repo ships

**Status:** CLOSED · rev-2 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-TOOL-aRepatriatedFork-16-1-acceptance-ledger.md](../build/2026-09-23-build-TOOL-aRepatriatedFork-16-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-16-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-16-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-install-prefix.sh` claims to grade what a repo SHIPS, but its root-install arm grades
`${SELF_PREFIX}*` in any repo, so at a consumer installed under `scripts/` it grades the consumer's
own tree plus every gov file that consumer received, against gov's own waivers keyed on gov's paths.
It redded nc on gov's own bytes and nc deselected the kit (owner ruling 2026-09-23). This unit makes
"what a repo ships" ONE derivation — a govkit verb over the repo's own registry — and has both arms
grade that set, and skip out loud where no registry exists.

## 2. Scope (IN)

- **S1** — A `shipped` verb on `tools/govkit/govkit.py` prints one `<entry>\t<role>\t<src>` row per
  descriptor survivor that carries a source, over THIS repo's `tools/govkit/registry.toml`. It is
  the one derivation of the shipped set; `derive_received_files` in `tools/check-install-prefix.sh`
  (`:108-150`) calls it rather than carrying its own heredoc over the same govkit API. Observed by
  AC1 and AC2.
- **S2** — The kit-source test (`tools/check-install-prefix.sh:182-183`) is hoisted above arm 1. In
  a repo that is not a kit source, arm 1 does not grade and prints a SKIP line naming why, the same
  way arm 2 already does at `:479-483`. The gate exits 0 there with both SKIP lines printed.
  Observed by AC3, and red-first by AC4.
- **S3** — In a kit source, arm 1's population and predicate are unchanged, so gov's own verdict is
  byte-for-byte the verdict at a7c78ad2. Observed by AC2.
- **S4** — The refusal message at `tools/check-install-prefix.sh:290-291` says "installs kits at
  tools/<kit>/", which is false at every adopter prefix the gate now runs under. It names the
  derived prefix instead. Observed by AC5.
- **S5** — The self-test derives its gate from its own location. `GATE` is spelled
  `$ROOT/tools/check-install-prefix.sh` at `tools/check-install-prefix.test.sh:17`, and at nc's
  `scripts/` install every `mkfix` arm exited 127 on that path (measured below). The `mkfix`
  fixtures of arms 1-8, S4 and AC6 (`:39-50`, `:395-414`, `:475-481`) build repos with NO registry
  and expect arm 1 to grade them; after S2 those repos skip, so they take a registry — through
  `mkfix` itself, per the rev-2 note below, not by moving each arm onto `mkfix_source` (`:120`).
  Observed by AC6.
  rev-2: `mkfix` itself takes the registry, a minimal one naming only the kit's engine file, plus
  an empty ratchet, so arms 1-8 keep their bodies and their meaning. `GATE_REL` becomes the gate's
  FIXTURE-internal path — every fixture lays its kits under `tools/` whatever the host prefix, so the
  gate inside a fixture sits there too — and `run_arm` runs that copy rather than the host's, which
  resolved its prefix from the host tree. The arms that need a NON-source (the carried skip at
  `:157` and AC6 at `:475`) move onto AC3's consumer fixture; arm 7's empty-kit refusal moves its
  gate to a prefix with no kit directory; the S4 arm moves the kit and sidecars and leaves the
  registry at `tools/govkit/`, rewriting the descriptor's home.
- **S6** — `tools/govkit/entries/check-install-prefix.kit.toml`'s `why_conditional` and the gate's
  header state the consumer behaviour: installed at a repo that ships nothing, the kit grades
  nothing and says so. NOT OBSERVED — prose, graded by review only.

## 3. Non-goals (OUT)

- Whether nc re-selects the kit. The deselection is an owner ruling; this unit makes re-selection
  safe and leaves the choice (§8 F2).
- Any change to arm 2's predicate or to `PREDICATE_EPOCH` (`:363`). The predicate does not move;
  only the population a non-source reaches does, so there is no epoch to spend.
- The runtime-literal class in shipped code. That is `TOOL-aRepatriatedFork-2`, which adds a third
  arm to this same file on top of S1 and S2.
- The self-test's remaining `tools/` literals. They are fixture-internal layout, justified on the
  ban list's own row for this file, and the suite-wide derivation is `TOOL-aRepatriatedFork-18`'s.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-2` — the runtime-literal arm, which reads S1's verb and runs
  only inside S2's hoisted kit-source branch.
- **hands-off** `TOOL-aRepatriatedFork-15` — the kit-epoch arm, which reads S1's verb with its role
  column to know which bytes an adopter receives.

## 4. Design

### The defect, measured

Arm 1's population is `git ls-files -- "${SELF_PREFIX}*" 'skills/*' '.githooks/*' '*.template.*'
'*.fragment.json' …` (`tools/check-install-prefix.sh:169-171`), and its kit alternation is every
directory under `${SELF_PREFIX}` (`:101`). Both run unconditionally. Only arm 2 checks whether the
repo is a kit source (`:182-183`, `:479`).

The glob spelled the literal `tools/*` until gov `306ed6de` (2026-09-21), which derived it so the
gate could run at `vendor/gov/`. That derivation is what brought a `scripts/` consumer's installed
gov bytes into the population. A consumer installed at `tools/`, gov's default prefix, was in the
same state before `306ed6de` — derived by reading the code, not by a run.

Measured on node a, 2026-09-23: nc at `052a8b39` (the parent of its deselection commit `239057ca`),
carrying the gate at gov a7c78ad2's bytes (blob `6b3c599a`), gives exit 1 with nine hits. PINNED.

| Hit at nc | Whose bytes | Why gov itself is green |
|---|---|---|
| `scripts/check-wiring.sh:455`, `:505` | gov's, installed | waived as `tools/check-wiring.sh:455`/`:505` in `tools/install-prefix-waivers.txt` |
| `scripts/codebase-map/map_lib.py:1493`, `gen_map.py:47`, `adopt-codebase-map.sh:155` | gov's, installed | waived at their `tools/` paths, same file |
| `scripts/drift-audit/drift_signals.py:5`, `:6`, `:127` | nc's, project-owned | not in gov's tree |
| `scripts/check-memory-hygiene.sh:531` | nc's fork comment | not in gov's tree |

Five of the nine are gov's own deliberate dual-spelling probes and legacy literals. Gov's waiver
rows cannot reach them: the rows key on gov's paths, and the descriptor seeds the registry EMPTY at
the adopter rather than copying it (`tools/govkit/entries/check-install-prefix.kit.toml`, the
`install-prefix-waivers.txt` rule's note). So every consumer that selects this kit reds on gov's
bytes, and the only remedies left are a fork or a deselection.

The same clone ran the self-test from `scripts/`: nine arms exited 127 on
`tools/check-install-prefix.sh` and the AC6 arm reported a missing skip line. PINNED, same run.

### Why "ships" means "a registry declares it"

The descriptor itself says the kit is `selectable = "conditional"` because it only makes sense for
"a target that itself ships kits onward". A repo ships what its registry resolves; `govkit apply`
writes nothing a registry does not name. A repo with no `tools/govkit/registry.toml` ships nothing,
so the honest verdict there is a SKIP, printed. The kit-source test keeps its two literal paths: a
kit source's registry sits at gov's layout by definition, because `tools/govkit/` is a registry
exemption that never travels (`tools/govkit/registry.toml`, the `[[exempt]]` row for
`tools/govkit`).

### Data model

`python tools/govkit/govkit.py shipped` prints, sorted, one tab-separated row per descriptor
survivor with a non-empty `src`:

```
<entry-id>\t<role>\t<src>
```

It resolves exactly what `derive_received_files` resolves today (`read_descriptors`, then
`resolve_entry(..., canonical_ctx(eid))["survivors"]`, `:131-134`), plus the entry id and role that
heredoc drops. It adds `WIRE-INTO-PROJECT.md` as the one named non-descriptor member only in the
gate, where that addition is documented (`:110-112`), never in the verb. It takes no arguments,
writes nothing, and refuses outside a repo carrying a registry.

### Inventory

- `shipped`, a govkit verb, dispatched by `main` beside `selfcheck`
  (`tools/govkit/govkit.py:10589`). Its handler is `cmd_shipped`, the `cmd` verb the lexicon
  reserves for a subcommand entry point.
- No new gate leg. The two existing legs grade the change.

### Migration

- gov: none beyond the code. The ban list and the waiver registry keep their rows, which AC2 proves.
- inCMS: nothing. It never selected the kit; there is no `scripts/check-install-prefix.sh` in its
  tree (checked 2026-09-23).
- nc: nothing is forced. If the owner re-selects the kit (§8 F2), nc reverts the deselection note in
  its own `.governance/deploy.toml` (lines 143-149 at nc `45e84273`), restores the leg its
  `239057ca` took out of `scripts/gate-legs.json`, and re-raises `VERB_OFFENDER_PIN` by the nine
  names `21fe990e` drained.

### Rollout

One commit for S1, one for S2-S5. The first is behaviour-neutral and AC1 proves it; the second is
where arm 1 changes, and AC3 and AC4 bracket it. rev-2: landed as ONE commit instead (§9); AC1 was
observed before either gate edit, so the neutrality it proves still holds.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/check-install-prefix.sh`
- `tools/check-install-prefix.test.sh`
- `tools/govkit/entries/check-install-prefix.kit.toml`

### Alternatives rejected

- **Subtract the receipt's rows from arm 1's glob at a consumer.** That grades what is left, which
  is the consumer's own tree, and a consumer's own prose naming its own `drift-audit/` files is not
  a root-install spelling of anything it ships. It trades gov's false reds for the adopter's.
- **Ship gov's waiver rows.** They key on gov's paths and never match at another prefix, and the
  descriptor already records why the registry is seeded empty.
- **Leave it deselected everywhere.** That is nc's state today. It leaves the trap armed for the
  next consumer that selects a kit its own descriptor calls selectable.

## 5. Production-readiness checklist

- security — N/A. A read-only lint; no write path, no egress.
- perf / scale — S1 replaces a heredoc with one subprocess of the same work; the gate's wall time
  is unchanged within noise. A non-source now does less work, not more.
- error / empty / loading states — a registry that resolves NO rows is a dead probe and refuses, as
  both arms already do (`:192-197`, `:497-500`). A missing registry is the SKIP, printed.
- observability — both SKIP lines name the missing registry, so a consumer's green run cannot be
  misread as a graded one.
- risks — S2 changes what a `mkfix` fixture means, and a re-fixture that forgets one arm turns it
  into a SKIP that reads green. The suite's existing liveness counters (`:484`, `:493`) are the
  guard, and S5 must keep them at or above today's floor.
- testing — S1 gets a govkit selftest arm; S2 gets the consumer fixture and its red-first twin.
- migration — none at gov or inCMS; optional at nc (§4 Migration).
- user docs — the gate header and the descriptor's `why_conditional`; no `help/` page exists for
  gov's gates.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py shipped` runs at gov HEAD, its third column, sorted
  and de-duplicated, equals the set the pre-change `derive_received_files` heredoc prints minus
  `WIRE-INTO-PROJECT.md` and plus the gate's own ratchet `install-prefix-carried.txt`, and it exits
  0. The ratchet is a descriptor survivor the heredoc discarded; the verb prints every survivor and
  the gate keeps discarding its own ratchet after the call, so the gate's set is unchanged (rev-2,
  measured: the heredoc run with an empty `CARRIED_SELF` prints exactly that one extra row).
  Red when: a role or an entry is dropped and the diff of the two sets is non-empty.
  figure: derived at observation time from both outputs; no count is written here.
- **AC2** — When `bash tools/check-install-prefix.sh` runs over gov's own tree after the change,
  both summary lines match those at a7c78ad2: 301 shipped files, 11 declared waivers, 26 marked
  fixture lines, and 141 recorded files of which 45 are hand-justified. Red when: S1 or S2 moved
  gov's population, so any of the five figures differs.
  figure: PINNED, measured on node a 2026-09-23 at a7c78ad2.
- **AC3** — When the gate runs as `cd scripts && bash check-install-prefix.sh` in a consumer fixture
  (kits under `scripts/`, a govkit receipt, no registry) whose files carry the five
  gov-waived spellings from §4, it exits 0 and prints both SKIP lines. Red when: arm 1 grades the
  fixture and exits 1 naming a hit.
  fixture: built by the new suite arm in §7; the tree holds no such repo today. rev-2: the
  fixture COPIES gov's own four files carrying those spellings rather than retyping them — the
  bytes nc received — so the suite gains no marked fixture line and AC2's figure holds.
- **AC4** — When the AC3 fixture is run with the gate's bytes at a7c78ad2 (blob `6b3c599a` of
  `tools/check-install-prefix.sh`), it exits 1 naming the root-install hits. Red when: the old gate
  exits 0, meaning the fixture does not reproduce nc's measurement and AC3 proves nothing.
  rev-2: observed ONCE, by hand, at the build; it is not a standing arm, because an adopter
  running the suite has no gov history to `git show` from.
- **AC5** — When arm 1 refuses in a fixture whose gate sits at `vendor/gov/`, the refusal text names
  `vendor/gov/` and no longer spells a `tools/` home; checked with
  `grep -c 'installs kits at tools/' tools/check-install-prefix.sh` returning 0. Red when: the
  message still states gov's prefix.
- **AC6** — When the suite is copied under `scripts/` in a scratch clone and run from there, every
  arm prints `arm ok` and none exits 127; its `GATE` line carries no `tools/` literal, checked with
  `grep -n '^GATE=' tools/check-install-prefix.test.sh`. Red when: `GATE` still resolves to
  `$ROOT/tools/check-install-prefix.sh` and nine arms exit 127 as measured at nc.
  cost: one suite run, about 20 s on node a.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `govkit selfcheck` ·
`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: `tools/check-install-prefix.test.sh` · a consumer fixture under `scripts/` with a receipt,
no registry, and the five gov-waived spellings; run first against `git show
a7c78ad2:tools/check-install-prefix.sh` to observe exit 1, then against the new gate · the suite's
`BAN_ARMS`/`CARRIED_ARMS` liveness floors do not move.

New arm: `tools/govkit/selftest.py` · a fixture registry with one entry of two roles; `shipped` must
print both rows with their roles, and a copy with the role column deleted must fail the arm · none.

## 8. Open questions

- **F1 — should a consumer's SKIP exit 0 or exit 2?** Exit 0 matches arm 2's skip today and keeps a
  consumer's bar green when it has nothing to police. Exit 2 would force a consumer to deselect,
  which is what nc did by hand. Recommendation: exit 0 with both SKIP lines, because the descriptor
  already calls the kit conditional and a printed skip is the house form for "nothing to grade".
  RESOLVED (owner, 2026-09-23): exit 0 with both SKIP lines, as recommended.
- **F2 — does nc re-select the kit after this lands?** Re-selecting buys nothing nc uses today — it
  ships no kits — and costs nine lexicon offender names. Recommendation: nc stays deselected; this
  unit exists so the next consumer that selects the kit is not red on day one.
  RESOLVED (owner, 2026-09-23): nc stays deselected, as recommended.
- **F3 — should the self-test's `GATE` derivation wait for `TOOL-aRepatriatedFork-18`'s canonical
  block?** Recommendation: no. S5 needs one line, the same `$(dirname "$0")` form the gate already
  uses for `_self_dir` at `:46`; if 18 ships a canonical block later, this line joins its parity
  table.
  RESOLVED (owner, 2026-09-23): no; one `$(dirname "$0")` line now, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from the nc deselection commit `239057ca` and a re-run of gov
  a7c78ad2's gate and suite at nc `052a8b39`.
- rev-2 · 2026-09-23 · built. AC1 gains the ratchet row the heredoc discarded (the verb prints every
  survivor; the gate still discards its own). S5 names how the fixtures take a registry — through
  `mkfix`, not by rewriting each arm onto `mkfix_source` — and that `GATE_REL` is fixture-internal,
  because a derived host path resolves to nothing inside a fixture whose kits sit under `tools/`.
  AC3's fixture copies gov's files rather than retyping the spellings; AC4 is a one-time
  observation, not a standing arm. §4 Rollout landed as ONE commit, not two: S1's call site and
  S2's hoist edit the same function's file, and AC1 was observed before either gate edit.

## 10. Reuse audit

The seam is `derive_received_files` in `tools/check-install-prefix.sh:108-150`, which already asks
govkit for the survivors; S1 lifts that one call into a govkit verb so the two further readers this
build adds (`TOOL-aRepatriatedFork-2`, `TOOL-aRepatriatedFork-15`) do not paste the heredoc a second
and third time. `python3 tools/codebase-map/reuse_lookup.py "derive the set of files a kit registry
ships to adopters with their role"` ranks `kit_rel` and `kit_dir` first; neither enumerates a
registry's survivors, and the tool reports `.sh` as an unscanned layer, which is where the real seam
lives. The skip form reuses arm 2's own announce line (`:479-483`) rather than inventing one.

Recall terms used: `install-prefix`, `shipped surface`, `received set`, `KIT_SOURCE`,
`carried-prefix`, `root-install`, `waiver registry`, `conditional`, `consumer`, `SELF_PREFIX`,
`derive_received_files`, `deselect`.
