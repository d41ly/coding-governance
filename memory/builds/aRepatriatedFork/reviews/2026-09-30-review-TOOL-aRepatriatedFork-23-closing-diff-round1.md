**Serves:** diff-review TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47

# aRepatriatedFork: Tier-2 review of the cumulative diff landing on main, round 1

*Node `a`, 2026-09-30. This is the integration-boundary review (§8) of everything the build lands
on `main`: 68 commits on `branch/arepatriated-fork-build-e42158`. Four primed finder lenses fanned
out, and every finding went to an adversarial skeptic prompted to refute it. The unit ids on the
binding line are the ones the range's commit messages carry.*

**Range reviewed: `d6e1749c0542218004260928f1399174daafb789...HEAD`** (HEAD = `a9b11dd2` when the review ran).

**Round: 1.**

## Verdict: BLOCKED

One finding blocks the landing. The default push-boundary bar can now be redirected by an untracked
install receipt to an untracked runner. That reopens the ignored-file class the closing review's H1
closed for `gate-env.sh`, this time for the bar itself. Two HIGH findings leave kit self-tests red:
the fan-out gate breaks when run from another repo, and the run-gates canary reads a manifest whose
spelling changed under it. Nine more findings (MEDIUM and LOW) are regressions or drift from the same
prefix-token migration. Every one is confirmed, and none is fixed in this range.

## Review shape and run integrity

- **Raw 17, confirmed 12, refuted 5, unverified 0. Precision 0.71** (12 / 17).
- **Adjudicated tally, by item:** 11 items. 1 BLOCKER, 2 HIGH, 6 MEDIUM, 2 LOW.
- **Adjudicated tally, by raw confirmed finding:** 12. 1 BLOCKER, 2 HIGH, 7 MEDIUM, 2 LOW. The counts
  differ because findings 4 and 13 are one defect, reported by two lenses and merged into item M1.
- **Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0
  contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run
  is complete: no lens or batch died, so the finding set is not truncated by the harness.
- The five refuted findings are the raw ids missing from the table below. They were dropped on the
  skeptic's refutation and are not carried as open items.
- The cited lines were spot-checked against HEAD while this report was written: `pre-push:482-492`,
  `check-verifier-fanout.sh:136`, `check-review-join.sh:175`, `render_playbook.py:220`,
  `settings-merge.py:685`, and 228 `{prefix}` tokens in `tools/gate-legs.json`.

| Item | Severity | Finding ids | Where | One line |
|------|----------|-------------|-------|----------|
| B1 | BLOCKER | 1 | `.githooks/pre-push:986` | An untracked receipt can point the default bar at an untracked runner that always exits 0 |
| H1 | HIGH | 2 | `tools/workflows/check-verifier-fanout.sh:136` | Hook path joins the caller's root to a kit-relative dir, giving MODULE_NOT_FOUND from another repo |
| H2 | HIGH | 10 | `tools/run-gates/run-gates.test.sh:356` | Canary arm 1b compares raw `{prefix}/` guards to `git ls-files` and gets 114 false reds |
| M1 | MEDIUM | 4, 13 | `tools/playbook/render_playbook.py:220` | `derive_gate_runner` reads `prefix` from `[answers]`, so flat runners are no longer found |
| M2 | MEDIUM | 11 | `tools/run-gates/run-gates.test.sh:378` | Canary arm 2 greps for `{prefix}/x.sh` literals and can no longer fire |
| M3 | MEDIUM | 3 | `tools/govkit/govkit.py:1669` | Selfcheck 5b cannot parse `${XX_DIR}` carriers, so the parity check is 28 notes of noise |
| M4 | MEDIUM | 12 | `tools/settings-merge.py:685` | Selftest crashes on `None.name` in a settings-merge-only install |
| M5 | MEDIUM | 14 | `tools/govkit/govkit.py:5639` | `foreign_kit_present` stopped probing `tools/`, so a legacy copy gets a second install |
| M6 | MEDIUM | 15 | `tools/check-wiring.sh:399` | Without python, the agent-cap arm prints a false "not adopted" skip for a hook that is present |
| L1 | LOW | 9 | `tools/govkit/govkit.py:2931` | Docs and comments still describe the deleted install-prefix sidecars as live |
| L2 | LOW | 16 | `tools/govkit/fixtures/make_adopter_receipt.py:177` | Descriptor read passes a raw `{prefix}/` path, so `homes` comes back empty |

## BLOCKER

### B1. The default merge bar follows an unvetted receipt (finding 1)

**Where:** `.githooks/pre-push:986`. The receipt is read at 482-497, `resolve_kit_dir` is inlined at
555-609, and the default bar runs at 977.

**Defect.** The default bar is now whatever runner `.governance/install.json` names. Neither the
receipt nor that runner has to be tracked or unmodified. `read_receipt_path`'s awk filter rejects
only absolute, drive-letter and `..` paths, so a path like `.git/x/run-gates/run-gates.sh` passes it
and also passes `root in hit.parents`. `check_bar_command` runs its tracked, clean and declared checks
only for `GOV_GATE_CMD` (line 979), and the default bar skips all three. The dirty-tree refusal at 871
cannot see excluded or ignored files. Planting a `gate-legs.json` beside the runner gets past the
manifest-elsewhere refusal at 823. `gate-fingerprint.sh` resolves from the same redirected directory,
so the fingerprint forcing predicate can be steered as well. push-main then writes a `default`-class
lander marker without checking `bar_blob`, which is empty in this case.

**Reproduction (skeptic-confirmed).** The resolution half was reproduced in a scratch repo: a tracked
`tools/run-gates/run-gates.sh` that exits 1, `.governance/` listed in `.git/info/exclude`, and a
receipt row pointing at `.git/x/run-gates/run-gates.sh`, which exits 0. Both resolvers returned
`.git/x/run-gates`, and `git status --porcelain` stayed empty. The full hook was not run end to end.
The remaining steps follow from the code as read.

**Why it blocks.** On `main` the runner was the fixed `$GOV_KITROOT/run-gates/run-gates.sh`, with
`GOV_KITROOT` hard-coded (main:366-374), and the dirty-tree check covered it. This diff regresses the
push boundary, the one place the bar binds, and reopens a class this build already closed once.

**Fix.**
1. Vet the receipt the way `gate-env.sh` is vetted. It must be tracked at `$_env_at`, and its working
   copy must hash to that blob. Otherwise ignore it or refuse with `bar-refused`.
2. After resolving `GATE_RUNNER`, require `git cat-file -e "$main_local:$GATE_RUNNER"` and a
   working-copy hash equal to that blob. Alternatively, send the default bar through
   `check_bar_command` without `declared`.
3. Refuse when `bar_blob` is empty.
4. Reject receipt rows whose path starts with `.git/`, in both the awk rung and `resolve_kit_dir`.
5. In `push-main.sh`, withhold the lander marker when `barblob` is empty.

**Left-shift gate.** Add a pre-push self-test arm that stages this exact setup (ignored receipt,
runner under `.git/`, planted `gate-legs.json`, red tracked bar) and asserts the push is REFUSED with
no lander marker. Add a sibling arm for a tracked receipt whose working copy is modified. Then add a
structural check that every path feeding `GATE_RUNNER` goes through the tracked-and-clean predicate,
so a new resolver rung cannot skip it.

## HIGH

### H1. Hook path mixes two repo roots (finding 2)

**Where:** `tools/workflows/check-verifier-fanout.sh:136`, and the same shape at
`tools/workflows/check-review-join.sh:175`.

**Defect.** `HOOK="$ROOT/$_hk_dir/agent-cap.js"`. `_hk_dir` is relative to the repo containing
`$HERE`, because the resolver walks up from `here`. `ROOT` is `git rev-parse --show-toplevel` of the
caller's cwd (line 26). When the two differ, the path points at nothing.

**Reproduction.** `check-verifier-fanout.sh --print-cap` run from a scratch `git init` repo fails:
node throws MODULE_NOT_FOUND for `<scratch>/tools/hooks/agent-cap.js`, and the gate reports
`verifier-fanout: FAILED` on a clean file. The suite's own arms at `check-verifier-fanout.test.sh:163`
and `:165` use exactly this setup, so the kit self-test is red at HEAD. The base version resolved
`$HERE/../hooks` absolutely.

**Fix.** Anchor to the repo that contains `$HERE`:
`HOOK="$(git -C "$HERE" rev-parse --show-toplevel)/$_hk_dir/agent-cap.js"`. Or have the inline
resolver print an absolute path. Apply the same change in `check-review-join.sh`.

**Left-shift gate.** The existing test arms already cover this, but they are held (`chunk=selftests`).
Add a cheap unguarded leg, or a lint over `tools/`, that flags `"$ROOT/$<var>"` joins where `<var>`
comes from the sibling-kit resolver. That catches the class in any other kit that adopted the
resolver.

### H2. Run-gates canary arm 1b reads raw `{prefix}` guards (finding 10)

**Where:** `tools/run-gates/run-gates.test.sh:356`.

**Defect.** Arm 1b ("every guard matches a tracked path") loads `tools/gate-legs.json` raw and
compares each guard literally against `git ls-files`. The manifest now spells its guards
`{prefix}/...`: 0 tokens on `main`, 228 at HEAD. Replaying the arm's predicate over the real manifest
gives 114 bad guards, for example `{prefix}/check-microformats.sh`.

**Impact.** The canary is red whenever it runs. It is held by default, so the break stays hidden
until `GATE_SELFTESTS=1`, which the DoD requires for kit work. The one liveness assertion that stops
an untracked guard from skipping forever is broken on the run meant to prove the bar can move.
Classes: vacuous-selector-empty-population, and retirement-inventory-misses-readers-by-value.

**Fix.** Resolve each guard before the tracked-path test, the way `run-gates.sh` does. Inline the
gated `resolve_prefix_token` block into the `-c` program and pass `$(dirname "$KITREL")` as the tool
root. Then stage a guard naming an untracked path and confirm the arm goes RED.

**Left-shift gate.** A structural check that every reader of `tools/gate-legs.json` (grep for the
filename across `tools/`) either calls `resolve_prefix_token` or declares that it reads the raw
spelling on purpose. A manifest spelling change should red every unmigrated reader, not just the
ones whose suites happen to run.

## MEDIUM

### M1. `derive_gate_runner` reads `prefix` from the wrong table (findings 4 and 13)

**Where:** `tools/playbook/render_playbook.py:220`.

**Defect.** `_a` is the lowercased `[answers]` table from `read_deploy` (callers at 513 and 549).
`prefix` is a top-level `deploy.toml` key (`.governance/deploy.toml:9`), and `govkit intake` writes it
only there (`govkit.py:11326`). `needed_answers` treats `prefix` as a seeded token, so it never lands
in `[answers]`, and `pfx` is always None. Every root in the remaining glob fallback comes from
`*/run-gates/run-gates.sh`, so the first rung always matches and the `anchor` and `gate.sh` rungs in
the loop at 227 cannot be reached.

**Impact.** `main` found flat runners (`tools/run-gates.sh`, `scripts/run-gates.sh`,
`scripts/gate.sh`). HEAD derives nothing for them. As finding 13's skeptic noted,
`resolve_placeholder_value` then raises a Refusal asking the operator for `GATE_RUNNER`. The operator
sees a loud refusal, not a silent empty render, but it is still a capability regression with dead
code attached. A root install is still found by `resolve_kit_dir`'s probe or the depth-1 glob, so
that part of finding 4 was overstated.

**Fix.** Pass the top-level `prefix` into the probe. Either merge `cfg['prefix']` into the dict the
probe receives, or have the deriver read `.governance/deploy.toml` itself. When roots is empty, keep
probing the root install and the flat `<root>/run-gates.sh` and `<root>/gate.sh` candidates.

**Left-shift gate.** A render selftest arm with a top-level `prefix = "scripts"` and a flat
`scripts/gate.sh`, asserting `bash scripts/gate.sh` is rendered. Add one arm per flat candidate that
`main` used to find.

### M2. Run-gates canary arm 2 can no longer fire (finding 11)

**Where:** `tools/run-gates/run-gates.test.sh:378`.

**Defect.** Arm 2 ("no leg script path is hardcoded in run-gates.sh") collects `argv[1:]` from the raw
manifest, now `{prefix}/check-template-size.sh` and similar, and greps `run-gates.sh` for those
literals. A leg inlined at its real path `tools/x.sh` never contains the string `{prefix}/x.sh`, so
the arm reports `ok` and proves nothing. The one exception is `skills/session-kickoff/manifest-check.sh`,
which carries no token. Class: armed-but-unreachable-rule.

**Fix.** Resolve `{prefix}` against the runner's tool root before the grep, as for H2.

**Left-shift gate.** One staged break that writes a resolved leg path into a scratch copy of
`run-gates.sh` and asserts RED. H2's reader-migration check covers this reader too.

### M3. Selfcheck 5b cannot read the version gate's new carriers (finding 3)

**Where:** `tools/govkit/govkit.py:1669`.

**Defect.** The 5b cross-check parses `need "..." <path>` lines from `tools/check-kit-versions.sh` and
substitutes only `${K}`. Those lines now spell their carriers `${MT_DIR}/`, `${CM_DIR}/`, `${HK_DIR}/`,
`${RG_DIR}/`, `${UN_DIR}/`, `${MR_DIR}/`, `${DA_DIR}/`, `${WF_DIR}/`, `${PG_DIR}/` and `${GK_DIR}/`
(for example, lines 138-140). None of them matches a registry `version_from.file`.

**Impact.** Measured: 28 "reported, not repaired" notes at HEAD against 12 on `main`, one pair per
kit. The parity check between the version gate and the registry is now noise, and because these are
notes nothing reds.

**Fix.** Resolve each `${XX_DIR}` the way the gate does: map the variable to its (home, anchor) and
call `resolve_kit_dir` from the gate's directory. Alternatively, have `check-kit-versions.sh` print
its resolved carrier list and have selfcheck read that instead of scraping the source.

**Left-shift gate.** Assert in selfcheck that every `need` line the parser extracts resolves to a
concrete path. An unresolved `${…}` becomes a FAIL, not a note. That is the liveness assertion this
probe lacked: a parser that matches nothing now says so.

### M4. settings-merge selftest crashes without a hooks kit (finding 12)

**Where:** `tools/settings-merge.py:685`.

**Defect.** `_hk = _resolve_agent_cap_dir().name`, but `_resolve_agent_cap_dir()` returns None on
LookupError. The entry declares `requires = []`, and its descriptor says a target may select it
alone.

**Reproduction.** In a scratch repo holding only `scripts/settings-merge.py`, `--selftest` at HEAD
exits 1 with `AttributeError: 'NoneType' object has no attribute 'name'`. On `main` it PASSes in the
same layout. The shipped `settings-merge selftest` leg is where adopters hit it.

**Fix.** When the resolver returns None, fall back to the old name-independent assertion
(`.endswith('/agent-cap.js')` plus the declared-prefix check), or SKIP the arm with a printed reason.

**Left-shift gate.** A fixture arm that runs the selftest with no hooks kit beside the file. More
generally, add a govkit check that runs each `requires = []` entry's gate legs in an install holding
that entry alone.

### M5. `foreign_kit_present` dropped the `tools/` probe (finding 14)

**Where:** `tools/govkit/govkit.py:5639`.

**Defect.** `main` probed the fixed pair `('tools', '')` (main `govkit.py:5511`). HEAD probes the
target's own declared prefix and the root. The comment claims the root probe "which the old pair also
covered" stays, which is true, but the `tools` probe is gone.

**Impact.** Take a target with a receipt-less, hand-copied kit under `tools/<kit>/`, running intake
with prefix `scripts`. AC8 at `govkit.py:6182` no longer refuses, and `apply` installs a second copy
under `scripts/`. That is the convergence the refusal exists to stop. It needs a non-default prefix
plus a legacy `tools/` copy, which is narrow but reachable. Class: a view fix that trades one
blindness for another.

**Fix.** Probe the union: the target's own ctx, gov's canonical ctx (`canonical_ctx(eid)`), and the
root.

**Left-shift gate.** An arm with a foreign kit at the canonical prefix while intake declares another
prefix, asserting the refusal.

### M6. check-wiring's resolver rung needs python (finding 15)

**Where:** `tools/check-wiring.sh:399`, with the same loss at 631, 692, 935 and 945.

**Defect.** `resolve_kit_file` replaced the bash-only `${KIT_REL:+$KIT_REL/}<home>/<file>` probe
(main `check-wiring.sh:496`) with the python sibling-kit resolver. With no usable python it returns
nothing and prints only a one-time stderr note.

**Impact.** This runs as a SessionStart hook, and its header says the host may have no python. With
no receipt, which gov itself does not keep, the agent-cap arm prints
`skip agent-cap — not adopted (no agent-cap.js at tools/hooks/ ...)` over a hook that is present.
That stdout line names a location that was never probed, and the arm's own comment calls a false skip
here security-shaped. The scratch, recall and merge-driver arms lose their probe rung the same way.

**Fix.** When `resolve_python` fails, fall back to the pure-bash probe of
`$_KIT_ROOT/$KIT_REL/<home>/<file>` and its parent, which is the resolver's own probe rung.
Alternatively, have the skip line say the probe did not run for lack of python.

**Left-shift gate.** A check-wiring test arm that shadows `resolve_python` to fail, with the hook
present at `tools/hooks/`, and asserts the arm does NOT print `not adopted`.

## LOW

### L1. Deleted install-prefix sidecars are still described as live (finding 9)

**Where:** `tools/govkit/govkit.py:2931` (`check_entry_producer` docstring), plus
`memory/map/features/govkit.md:94`, `tools/line-length-limits.txt:12`,
`tools/govkit/entries/check-line-length.kit.toml:10` and `tools/memory-tree/merge-rows.test.sh:1642`.

**Defect.** TOOL-aRepatriatedFork-30 deleted `tools/install-prefix-waivers.txt`,
`tools/install-prefix-carried.txt` and their descriptor rules. The docstring still names
check-install-prefix as a producer-less entry "seeded empty rather than copied". The map dossier
describes two arms and a `--write-ratchet` mode that no longer exist. The three comments cite that
registry as current precedent. This is doc drift only, with no runtime effect.

**Fix.** Remove the check-install-prefix clause from the docstring. Rewrite the `govkit.md` bullet to
describe the single pure ban. Change the three comments to the past tense, or drop the precedent.

**Left-shift gate.** `check-dead-paths` skips `memory/` and matches filenames only. Extend it, or add
a sibling, to scan `memory/map/features/` for backticked repo paths that do not exist in the tree.
A dossier is the inventory sessions read, so it is the worst place for a dead path to live.

### L2. Adopter-fixture regenerator reads raw `{prefix}` descriptors (finding 16)

**Where:** `tools/govkit/fixtures/make_adopter_receipt.py:177`.

**Defect.** `resolve_kit_homes` derives the registry path per revision, but passes
`entry["descriptor"]` raw to `git show rev:path`. From this landing on, descriptors are spelled
`{prefix}/...` (`registry.toml:51`), so every read returns empty, and
`if not txt.strip(): continue` silently empties `homes`. Separately, `home` is now kit-relative, so
`resolve_source` would miss even if the read worked.

**Impact.** Latent. The committed fixture is pinned at `ce5dca99`, and no gate regenerates it.
Regenerating at any post-landing `gov_rev` leaves rows UNRESOLVED, and each is printed by name.

**Fix.** Resolve the token before the read:
`read_gov_text(gov_rev, entry["descriptor"].replace("{prefix}/", derive_rev_prefix(gov_rev)))`.
Make an empty descriptor read a `SystemExit` rather than a `continue`, and join `home` against the
revision's prefix.

**Left-shift gate.** A fixture selftest that regenerates against HEAD in a scratch clone and asserts
`homes` is non-empty and the unresolved count is zero.

## Cross-cutting note

Eight of the twelve findings (2, 3, 4/13, 10, 11, 12, 15, 16) come from one migration: kit paths
moved from literals to `{prefix}` tokens and resolver-derived directories, and a reader of the old
spelling was not migrated. H2's reader-migration check is the class gate for the manifest. The same
check, extended to `registry.toml` descriptors and the `${XX_DIR}` carriers, would have caught M3 and
L2 as well. One structural check earns more here than eight point fixes.

## Next

Fix B1 before anything lands. Fix H1 and H2 in the same pass, then run
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` as kit work's DoD requires, since
both HIGHs live in held legs. Round 2 reviews the fix diff only.
