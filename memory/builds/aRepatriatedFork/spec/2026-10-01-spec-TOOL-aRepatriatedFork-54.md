# TOOL-aRepatriatedFork-54 — two gov gates grade a repo-root install correctly

**Status:** SPECCED · rev-2 · 2026-10-01 · node a · Tier-1 · base 56c7befa · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aRepatriatedFork-54-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aRepatriatedFork-54-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The VERIFYING repair pass R2 ran gov's suites with the tool root moved to the repository root, the
third prefix the owner ruled every suite must run at, and found two gates whose population rule
assumes a non-empty tool root. `check-playbook-parity.sh` counts every top-level directory as a kit,
so `.claude/` and `skills/` red as undocumented kits. `check-spec-tokens.py` grades a token as a
path only when it carries a `/`, so a root install's bare file names go ungraded and the suite's
red arm for an untracked witness path stays green. This unit makes each gate grade a root install
the way it grades every other prefix.

## 2. Scope (IN)

- **S1** — `check-playbook-parity.sh` derives its kit population from govkit's declared registry
  rather than from a listing of the tool root. A kit is a TRACKED directory segment the registry
  declares under its `{prefix}` token: the head of an `[[entry]]` descriptor path, or an `[[exempt]]`
  path naming a tracked directory, in both cases holding a tracked file. The registry is found through the sibling-kit resolver the gate
  already inlines for the hooks kit, and an unresolvable registry exits 2 naming what it looked for,
  never an empty population. The frozen sentinel and both waiver arms are kept as they are.
  Observed by AC1, AC2 and AC3.
- **S2** — `check-spec-tokens.py`'s path join grades a bare file-name token when the graded tree's
  tool root is the repository root, which `derive_legs_path` already reports as an empty prefix. A
  bare token is graded when it has no `/` and its extension is the extension of some tracked file.
  It resolves when it is a tracked path or the basename of one, because the house style cites a
  kit file by its basename; otherwise it reds as `not tracked by git ls-files`. Every other prefix
  is graded exactly as at base. Observed by AC4, AC5 and AC6.
- **S3** — Each gate's header states the rule, and what it still does not grade. Observed by AC7.

## 3. Non-goals (OUT)

- The other two listing-derived populations the parity gate's comment names,
  `check-install-prefix.sh`'s and the codebase-map extractor's. R2 observed neither red at the root,
  and the comment that calls the three one derivation is rewritten to say they now differ and why.
- Grading bare names at a non-root install. §8 F2 records the measurement that rules it out.
- Govkit's own `selfcheck` at a root install, whose `{prefix}/*` surface glob reads every root
  entry. It was not observed red, and it is govkit's.
- Running any suite at a foreign prefix. That is `TOOL-aRepatriatedFork-52`'s leg.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-52` — both gates' self-tests green at a repo-root install,
  which the redesigned foreign-prefix leg probes at the root and reds without.

## 4. Design

### Evidence

- The VERIFYING repair record's item 3, "Two gates' semantics at a root install", and the RUN.md
  rescope row adding this unit, both 2026-10-01.
- `check-playbook-parity.sh` at `56c7befa` lists `git ls-files -- "${SELF_PRE}*/*"` and keeps every
  first segment; with `SELF_PRE` empty that is every top-level directory holding a file.
- `check_path_shaped` in `check-spec-tokens.py` at `56c7befa` admits a slash with an extension, or
  an exact tracked path. The suite's arm 2 plants `${PFX}nope.sh`, which is `nope.sh` at the root,
  so the arm expects a red the gate cannot give there.
- govkit's registry header says some tool-root directories are not deployable and some entries are
  not directories; its `selfcheck` asserts the declared surface against the tracked one in both
  directions, so the registry is the declared population this gate can read.

### Files touched (estimate)

- `tools/check-playbook-parity.sh`
- `tools/check-playbook-parity.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/playbook-kit-waivers.txt`, only if the derived population differs at `tools/`

### Alternatives rejected

- Subtracting known non-kit directories at the root. That is a hand-kept list of an adopter's own
  layout, which the build-level rule against new conf keys for layout refuses.
- Kit directories as the ones holding a `kit.toml`. govkit's own directory holds none; its
  descriptors sit under its entries folder, so the population would lose a kit.
- The two fixes as two units. They are one owner-adopted unit, the same class of defect, and they
  write disjoint files, so the closing diff attributes each finding by file.

## 5. Production-readiness checklist

- security — none; two read-only gates over tracked text.
- perf / scale — one registry read; one basename set built once per run.
- error / empty / loading states — an unresolvable registry refuses with exit 2 (S1).
- observability — the parity OK line keeps printing its derived kit count.
- risks — the derived set at `tools/` must equal the base set; AC1 observes it.
- testing — AC1 to AC6.
- migration — none.
- user docs — none; both gates are gov-internal.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-playbook-parity.sh` runs on the real tree, it exits 0 and its OK
  line's kit count equals the count the `56c7befa` gate prints.
  Red when: the registry derivation gains or loses a kit at `tools/`.
  figure: DERIVED at observation time, both sides.
- **AC2** — When the parity suite's first §7 new arm runs as a slice, a root-install fixture
  holding `.claude/` and `skills/` beside its declared kits passes the gate with exit 0, and an
  undeclared directory planted beside them is not reported as a kit.
  Red when: the `56c7befa` gate is staged into the arm and reds naming `.claude`, which is the
  red-first control.
- **AC3** — When the fixture's registry is made unresolvable, the gate exits 2 naming the registry,
  and when a declared kit is left unnamed by the playbook it still exits 1 naming that kit, at the
  root and at `tools/`.
  Red when: an unresolvable registry reads as an empty population, or the coverage arm goes silent.
- **AC4** — When the spec-tokens suite's untracked-witness arm runs as a slice with its tool root
  at the repository root, the planted `nope.sh` reds with `not tracked by git ls-files`.
  Red when: the `56c7befa` checker is staged into the arm and it stays green, which is the red-first
  control.
- **AC5** — At a root install, a bare token naming a tracked file by its basename, such as
  `kit.toml`, is graded and resolves, and a dotted word whose extension no tracked file carries,
  such as `json.loads`, is not graded.
  Red when: the basename citation reds, or the dotted word is graded.
- **AC6** — When the `56c7befa` copy of `tools/check-spec-tokens.py` and the built one run over the
  same real tree, both exit 0 and print the same graded-token count.
  Red when: a bare token is graded at `tools/`, which moves the count.
  figure: DERIVED at observation time, both sides.
- **AC7** — When the headers of `tools/check-playbook-parity.sh` and `tools/check-spec-tokens.py`
  are read, each states its root-install rule and what it does not grade.
  Red when: either header still describes the listing derivation, or the slash-only path rule.

## 7. Gates

`playbook parity` · `playbook parity selftest` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: `tools/check-playbook-parity.test.sh` · a root-install fixture with `.claude/` and `skills/` beside its declared kits, and one with an unresolvable registry · the suite's floor rises by the new arms

New arm: `tools/check-spec-tokens.test.sh` · a root-install fixture citing an untracked bare file name, a basename citation, and a dotted non-file word · the suite's floor rises by the new arms

## 8. Open questions

- **F1 — what is the parity gate's kit population?** Option (a): the directory segments govkit's
  registry declares under `{prefix}`. Option (b): the tool-root listing with a root-only exclusion
  of directories that hold no kit descriptor. Option (c): every directory holding a `kit.toml`.
  Recommendation: (a). It is the declared population the owner's ruling names, it is
  prefix-independent because it reads the registry's own `{prefix}` strings, and (c) loses govkit.
  RESOLVED (agent, 2026-10-01, delegated): (a).
- **FACT-QUESTION · F2 — are bare names graded at every prefix, or only at a root install?** The
  probe: run S2's shape and basename rule over every live spec's acceptance bullets in this tree and
  count the tokens it would red. The observation that decides it: a non-zero count rules out every
  prefix, because the path join would red specs nobody changed. Liveness: the same probe resolves
  the corpus's basename citations, so it can and does produce hits. Measured at `56c7befa` on
  2026-10-01: 63 bare tokens with a tracked extension in live specs, of which 10 in three specs
  name no tracked file.
  RESOLVED (agent, 2026-10-01, delegated): a root install only, where a bare name is how a
  root-level file is written; every other prefix keeps the base rule.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft from the owner's 2026-10-01 ruling adopting this unit, with
  R2's root-install findings as its evidence.
- rev-2 · 2026-10-01 · S1: an `[[entry]]` head counts as a kit only while it holds a tracked file,
  as an `[[exempt]]` path already had to. A registry-only population keeps a kit whose directory
  was deleted, so the suite's sentinel and empty-set arms, which untrack the kit, could never red,
  and a waiver for a removed kit could never read stale.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive the kit population at a repo-root install"`
named `resolve_kit_dir` among its seams, which the parity gate already inlines and S1 reuses to find
the registry; the population itself comes from `tools/govkit/registry.toml`, the declared surface
govkit's `selfcheck` already asserts. For S2 the seam is `check_path_shaped` and `derive_legs_path`
in `tools/check-spec-tokens.py`, extended in place. The recall probe's hits were this build's own
repair record and `TOOL-aRepatriatedFork-46`'s root fixture fold; no earlier decision set a root
rule for either gate.

Recall terms used: `kit population registry descriptor root install prefix playbook parity derivation sentinel waiver spec-tokens bare`.
