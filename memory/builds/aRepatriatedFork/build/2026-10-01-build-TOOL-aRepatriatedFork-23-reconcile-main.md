**Serves:** journal TOOL-aRepatriatedFork-23

# aRepatriatedFork: reconcile of origin/main (dDerivedDocket, dAlignedCarrier)

*Node `a`, 2026-10-01. Branch tip `aa660634`, origin/main `1f915870`, merge base `d6e1749c`.
`git merge --no-ff --no-commit origin/main` conflicted in 105 paths: 146 hunks, 71 of them only a
version number. No push, local main and the primary tree untouched, no hook bypassed, no whole bar.*

Every check the reconcile owes ran ALONE, on a candidate commit built from the staged index with
`git commit-tree` and checked out in a scratch worktree, because hygiene check 26, the kit epoch,
pass-order and the manifest gate read history the uncommitted merge does not have yet.

## Per file group

**Version carriers.** Every kit both sides bumped takes a version above both, in every carrier,
found by a tree-wide sweep for both old values rather than by the conflict list: check-wiring 1.22,
codebase-map 1.21, drift-audit 1.21 (and the two drift workflows' `meta.version`, the carrier the
first sweep missed and `check-kit-versions.sh` named), kickoff-manifest 1.15, lexicon 1.17,
memory-recall 1.25, memory-tree 2.113, playbook-render 1.20, review-harness and tier2-review 1.25,
run-gates 1.20, runlog 1.6, unattended 1.50. The charter template both sides moved to v3.2 with
different bodies is v3.3, on its header and on its `governance-template:` marker. Evidence: kit
version markers 0, govkit selfcheck 0, kit epoch against `f8fdd873` 0.

**The pure ban and `--offenders`.** The two deleted registries stay deleted. dDerivedDocket's
`--offenders` signature (TOOL-dDerivedDocket-23) is rebuilt over the ban's one counter: one
`<path> TAB ban TAB <spelling>` key per counted spelling, an ordinal on a repeat, nothing else on
stdout, written in one piece so a refusal or a dead counter leaves no key. Its suite gains the
exact-set, ordinal, unrelated-edit, clean-control and dead-counter arms; floor 35 to 40. Every kit
path node d's code spelled was drained into a derivation: `{prefix}` in the leg manifest and the
budgets, `PFX` and the resolved kit-name variables in the suites, `resolve_kit_dir` in the hooks,
`<prefix>/` in prose, and `bin/` or `src/` for fixture paths that only had to be some path. Evidence:
the ban clean over 330 files; its suite PASS at 40.

**Hooks.** `gate-env.sh` keeps `GOV_KITROOT` and gains the inherited-red pair. In `pre-push` the
straggler block moved below the kit-root ladder, since this branch unsets `GOV_KITROOT` until the
vetted `gate-env.sh` runs and the block read it above that point; it finds the memory-tree kit
through the sibling resolver. The guard-record predicates take node d's function and this branch's
`${KP}` manifest path. The VR fixture declares its kit root the way this branch's hook reads it.

**Red attribution.** The runner reads the manifest at R through the same `{prefix}` resolution as
the manifest at L, or every red leg would read OWN by "its argv differs". `run-selftests.sh` passes
its tool root to the reader node d turned into an argument-taking function.

**Generated artifacts.** Re-rendered by their own renderers, never hand-merged: the charter region
of `AGENTS.md`, the memory-tree guides and `HYGIENE.md` and `TEMPLATE-SPEC.md` by the kit's parity
render, the unattended guides and Skill by its adopter, the lexicon Skill by its adopter, the
codebase map by `gen_map.py --write`, the build index and family views by
`gen_build_index.py --write`, the gotchas index, and the workflow and fixture renders from their
templates with the token values HEAD's own renders carry.

**Backlog.** origin/main moved to builds mode; this branch's shard edits were relocated with
`migrate_backlog.py --relocate --as aRepatriatedFork`. The one row it refused,
TOOL-dSpentCeiling-6, was a prose-only edit and is dropped with that reason recorded. This build's
nine open asks get a KEEP row, since the build derives CLOSED with them open. Five asks in other
builds that cite the two deleted registries by path now name them in words, as this branch had
already done to the same rows in the shard. `ASK_CUTOFF` moves to 2026-10-01 by its own rule, the
relocation having written an ask filed 2026-09-30.

**Shared records.** `.memory-tree.conf` takes main's builds-mode keys and blank row pins, keeps
this branch's third registry member, and re-derives `SPEC_HANDOFF_CUTOFF` to 2026-10-02 by its
relation. `.lexicon.conf`'s pin is re-measured at 1064. The leg manifest, the selftest budgets and
the lexicon kit's guard are unions, the budget rows taking node d's later measurements. The
`ORDER|project-owned` count is 29, both sides having added a row from 27.

**Specs and dossiers.** TOOL-aRepatriatedFork-24 keeps this branch's CLOSED status and takes node
d's leg-line edit as its rev-7. The install-prefix dossier keeps the pure-ban text and gains a
paragraph on `--offenders`. The archived v3.1 snapshot is the one main published, which is
append-only; main's v3.2 is archived beside it.

## Checks, each alone, on the candidate

Exit 0: install-prefix, lexicon, encoding posture, check-arms, full memory hygiene, build index
`--check` and `--check-format`, spec tokens, shell hygiene, codebase-map tests, kit versions, kit
epoch, govkit selfcheck, dead paths, drift report, template size, playbook parity, verdict epoch,
pass-order (320 s). Exit 1: `manifest-check.sh`, checks 5 and 9. The pre-commit gate demands the
re-stamp inside the merge commit, so §B was re-audited against the merged tree there: its
`<prefix>/unattended/` DoD line now names both verdicts dDerivedDocket allows, and both stamps name
the pre-merge HEAD. The follow-up commit re-stamps both at the merge, per the kickoff-manifest merge
exception.

## After the merge: the repo-subject hook suites

Run alone after `5cb052da`, because their legs are on every bar. `transition-audit arms` exit 0.
`pre-push self-test` and `straggler-guard arms` redded, and every red was this reconcile's:

- The red-attribution parser added to `run-gates.sh` carried a comment with apostrophes inside its
  single-quoted program, a runtime syntax error on every red. Rewritten without one.
- dDerivedDocket gave the runner eight new `GATE_` names, and this branch's knob-class arm needs
  each classified once: the three arm seams join the names the hook clears before a non-stub bar,
  the other five the inert set.
- Node d's IR fixture and the straggler fixture declared no kit root, which the old probe had
  guessed; each now declares `GOV_KITROOT` in its tracked `gate-env.sh`. The straggler fixture's
  memory-tree copy drops its hygiene gate, so the pre-commit hygiene leg still announces a skip
  there, as the fixture's header requires. The AC3 (24) stub runner writes the GREEN record an
  exit 0 needs since TOOL-dDerivedDocket-26.

After the repair: `pre-push self-test` exit 0, `straggler-guard arms` PASS at 84.

## Not run

The held kit self-test suites were not run whole: run-gates canary, run-selftests, install-prefix
(run once, PASS at 40, before the repair), check-wiring, merge-rows, govkit selftest and the
unattended suites.
