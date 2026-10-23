# TOOL-dGroundRules-64 — the respelled literals no other repair covers, restored whole and observed: units 5, 21, 33 and 34

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-64-deviation-52.md](../build/2026-10-23-build-TOOL-dGroundRules-64-deviation-52.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md) | research | TOOL-dGroundRules-21 TOOL-dGroundRules-25 TOOL-dGroundRules-34 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 |
| [2026-10-23-prompt-TOOL-dGroundRules-58-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-58-task.md) | research | TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build's spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
traced its items H1 and H2 to one defect: the main loop cleared spec-tokens path hits by respelling
each flagged word in a spec's §6 to its basename, and some of those words were fixture literals a
criterion runs verbatim. This unit is the adopted discovery. Of the brief's respelling inventory it
takes every line that H1, H2, M1 and the earlier repairs do not already cover, verifies it against
the spec and its history, and restores each literal's meaning whole in §4, which the paths join does
not read, so the criterion that runs it can pass. It changes no code. It repairs units 5, 21, 33 and
34, at orders 3 to 12, and consumes `TOOL-dGroundRules-51` at order 15, so it builds at order 17.

## 2. Scope (IN)

- **S1** — `TOOL-dGroundRules-5` AC1 (line 333). Its blob compare runs as `POLICY_BLOB_WHOLE` (§4),
  the policy file's path whole in the revision argument, against the mirror's `policy_blob` read by
  `MIRROR_POLICY_BLOB`. Observed by AC1.
- **S2** — `TOOL-dGroundRules-21` §6 line 424, the bare-name convention: `policy.toml` and
  `policy.json` are read under `.governance/`. The two criteria of that unit that read those files
  at a revision or by attribute, AC1's blob at HEAD and AC19's line-ending pin, run as
  `POLICY_SHOW_WHOLE` and `MIRROR_ATTR_WHOLE` (§4). Observed by AC2.
- **S3** — `TOOL-dGroundRules-33` AC4 (lines 171, 172 and 176). Its staging takes out the guard
  entry `TOOL-dGroundRules-33` S1 adds, and plants a read of the deployer's selftest, each by its
  whole spelling, `GUARD_OUT_SELFTEST` and `READ_SELFTEST` (§4). Observed by AC3.
- **S4** — `TOOL-dGroundRules-34` AC20 (line 522), AC23 (line 538) and AC32 (line 571). AC20 plants
  the install-day policy file at its path whole, `POLICY_BEFORE_SCAFFOLD`; AC23 stages the rename in
  the deployer's selftest by its path whole, `DEPLOY_FULL_OUT`; AC32 is observed through
  `EVIDENCE_WHOLE` of `TOOL-dGroundRules-51` §5, which names the build README whole.
  Observed by AC4, AC5, AC6.

## 3. Non-goals (OUT)

- The inventory lines H1, H2 and M1 cover: units 44 and 45 (`TOOL-dGroundRules-53` to
  `TOOL-dGroundRules-60`) and unit 46's population (the minors unit of the closing review).
- The inventory lines an earlier repair already observes whole, and the ones judged false positives,
  each listed with its reason in §4 (`The inventory, line by line`).
- Unit 21's other repairs and the hands-off line on unit 21, which the writer of
  `TOOL-dGroundRules-61` and `TOOL-dGroundRules-62` adds.
- Rewriting any repaired spec's §6. A repaired spec names this unit in its §3 (BUILD-METHOD M4).

### Edges

- **consumes-from** `TOOL-dGroundRules-5` — AC1's blob compare, which S1 runs with the policy file's path whole
- **consumes-from** `TOOL-dGroundRules-21` — the bare-name convention at §6 line 424 and the criteria AC1 and AC19, which S2 runs with the paths whole
- **consumes-from** `TOOL-dGroundRules-33` — the guard entry of S1 and the staging of AC4, which S3 spells whole
- **consumes-from** `TOOL-dGroundRules-51` — `EVIDENCE_WHOLE`, through which S4 observes `TOOL-dGroundRules-34` AC32

`TOOL-dGroundRules-34`, whose AC20, AC23 and AC32 S4 restores, takes no edge here: its spec sits 23
bytes under the 49152-byte live-spec ceiling of `tools/template-size-limits.txt`, so a reciprocal
line cannot be added to it, the reason `TOOL-dGroundRules-52` §3 gives for the same choice.

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `git rev-parse HEAD:policy.toml` exits 128 with `path 'policy.toml' does not exist in 'HEAD'`; a
  revision argument resolves from the repository's top level, so the cut form can never name the
  policy file. `git rev-parse HEAD:tools/gate-legs.json` prints a blob id. At base neither
  `.governance/policy.toml` nor `.governance/policy.json` is tracked; `TOOL-dGroundRules-1` and
  `TOOL-dGroundRules-5` create them.
- `TOOL-dGroundRules-5` §4 spells the field `policy_blob` as the blob id of `.governance/policy.toml`
  at the rendered revision, and step 3 of its helper's evaluation order spells the revision argument
  whole as `L:.governance/policy.toml`. Every committed revision of its §6 (`429689679`,
  `4174257e6`, `f4d31452a`) holds the cut `HEAD:policy.toml`.
- `git check-attr eol` answers `unspecified` for a path no attribute pattern matches, so AC19 read at
  the repository root would grade no pin.
- `git ls-files` lists nine files named `selftest.py`, one of them `tools/govkit/selftest.py`, so a
  staging that names the file by basename picks none of them.
- `tools/gate-legs.json` spells every guard entry from `{prefix}`, and `TOOL-dGroundRules-33` S1
  adds `{prefix}/govkit/selftest.py` to the `policy fixtures` row in that spelling.
- `git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order` printed lines
  `165` and `179`, the evidence `TOOL-dGroundRules-34` S32 cites.
- No committed revision of units 29, 33, 34 or 39 holds an inventory original: each spec's §6 was
  respelled before its first commit, so each restoration below is resolved from the spec's own scope
  and design.
- `tools/template-size-limits.txt` line 167 holds `memory/builds/*/spec/` at 49152 bytes;
  `TOOL-dGroundRules-34`'s spec is 49129 bytes.

### The inventory, line by line

| Inventory line | Disposition | Where it is answered |
|---|---|---|
| 5 :333, two words | restored | S1 |
| 21 :424 | restored, the convention's two readers | S2 |
| 25 :424 | false positive: the same convention line as 21 :424, naming the directory; no criterion of unit 25 reads either file by revision or by attribute | none owed |
| 29 :147, :148 | covered: unit 34 S11 spells AC4's tree whole, and `TOOL-dGroundRules-39` `TREE_AMBIG` runs it | units 39 and 43 S2 |
| 29 :151 | false positive: AC5 greps the kit README for the file name, which matches as written | none owed |
| 32 :355, three words | covered: unit 34 S15 spells AC9's probe whole, unit 40 S3 restates it, and unit 45 routes it through the probe | H2, `TOOL-dGroundRules-59` |
| 33 :171, :172, :176 | restored | S3 |
| 34 :486, :490 | covered: AC11 and AC12 are observed whole through unit 39 | units 39 and 43 S2 |
| 34 :499 | false positive: a quoted glob that lists every untracked registry file as written | none owed |
| 34 :504, :505, :509 | covered: AC15 and AC16 are restated by unit 40 S3 and routed through the probe | H2, `TOOL-dGroundRules-59` |
| 34 :522 | restored | S4 |
| 34 :538 | restored | S4 |
| 34 :571 | restored by reference to unit 51's whole evidence | S4 |
| 39 :129, :140, :142 | false positive: the staging counts any file of that name, the criterion's red case is a top-level file, and AC4 names `TREE_AMBIG`'s two paths, each spelled whole in that unit's fence | none owed |
| 40 :129, :130 | covered: unit 45 S3 routes those criteria through the probe | H2, `TOOL-dGroundRules-59` |
| 43 :231 | covered: `TOOL-dGroundRules-51` `EVIDENCE_WHOLE` observes AC3 | unit 51 |
| 44 :129 | H1 | units 53 to 57 |
| 45 :124 | H2 | `TOOL-dGroundRules-58` |

### The literals

Spelled whole here, once, and named by the criteria. Each runs from the root of the tree it
observes; a staging runs in a scratch copy.

```text
MIRROR_WRITE         = python tools/policy/policy.py mirror --write
POLICY_BLOB_WHOLE    = git rev-parse HEAD:.governance/policy.toml
MIRROR_POLICY_BLOB   = python -c "import json; print(json.load(open('.governance/policy.json', encoding='utf-8'))['policy_blob'])"
POLICY_SHOW_WHOLE    = git show HEAD:.governance/policy.toml
SCAFFOLD_BYTES       = python tools/policy/policy.py scaffold
MIRROR_ATTR_WHOLE    = git check-attr eol -- .governance/policy.json
GUARD_OUT_SELFTEST   = in the scratch copy, the entry {prefix}/govkit/selftest.py taken out of the guard
                       list of the "policy fixtures" row of tools/gate-legs.json
READ_SELFTEST        = in the scratch copy, one read-mode open() of tools/govkit/selftest.py staged into
                       the first line of build_fresh_target, until TOOL-dGroundRules-34 S23's in-process
                       read is built
FRESH_TARGET         = python tools/policy/check_policy.py --fixture adopter-fresh-target
POLICY_BEFORE_SCAFFOLD = in the install-day target <t> TOOL-dGroundRules-34 AC20 builds, the file
                       <t>/.governance/policy.toml written before --scaffold, setting budgets.enforce
                       outside its allowed set and policy-file.on-invalid to refuse
SCAFFOLD_TARGET      = bash tools/policy/adopt-policy.sh --scaffold --target <t>
DEPLOY_FULL_OUT      = in the scratch copy, the assignment DEPLOY_FULL renamed in
                       {prefix}/govkit/selftest.py, which in a copy of this repository is
                       tools/govkit/selftest.py
ANSWERS_PROBE        = python -c probe, tools/policy on sys.path, that imports check_policy and prints
                       read_deploy_answers("<the copy's root>")
```

### Files touched (estimate)

none — the unit writes no file of the product; its evidence is its acceptance ledger.

### Alternatives rejected

- **Each literal respelled in place in its spec's §6.** It rewrites reviewed criteria, which
  BUILD-METHOD M4 keeps to a promoted unit, and it puts an untracked path back in a criterion bullet,
  where the paths join reds it until the build creates it.
- **One unit per repaired spec.** Each restoration is a literal and its observation, with no code;
  four units would add four specs, four deviation records and four ledgers for one mechanism.

## 5. Production-readiness checklist

- security — N/A: probes and scratch copies; no write path.
- perf / scale — one mirror write, two git reads, three fixture runs.
- error / empty / loading states — a revision argument naming no tracked path exits 128, which AC1
  and AC2 red.
- observability — each criterion names the field or line it compares.
- risks — the observations need units 1, 5, 21, 33 and 34 built; S3's planted read stands in for
  unit 34's in-process read until that unit is built.
- testing — AC1 to AC6.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch copy is a git clone of this repository under
`%TEMP%/gr64`, checked out at the commit under test. The literals are spelled in §4 and named here.

- **AC1** — When `MIRROR_WRITE` runs on the built tree, `MIRROR_POLICY_BLOB` and `POLICY_BLOB_WHOLE`
  print the same blob id, and `POLICY_BLOB_WHOLE` exits 0.
  Red when: the mirror's `policy_blob` names another blob, or the revision argument names a path the
  revision does not hold and exits 128.
- **AC2** — When `POLICY_SHOW_WHOLE` runs on the built tree, it exits 0 and its bytes equal what
  `SCAFFOLD_BYTES` prints; and `MIRROR_ATTR_WHOLE` prints a line ending `eol: lf`.
  Red when: either file is read at the repository's top level, where `git show` exits 128 and
  `check-attr` answers `unspecified`.
- **AC3** — When `GUARD_OUT_SELFTEST` and `READ_SELFTEST` run in a scratch copy and `FRESH_TARGET`
  runs from that copy's root, it prints `guard-trace · WRONG tools/govkit/selftest.py`.
  Red when: the staging takes out another entry than the deployer's selftest, or plants a read of
  another of the tracked selftest.py files, so the trace stays silent.
- **AC4** — When `POLICY_BEFORE_SCAFFOLD` is planted and `SCAFFOLD_TARGET` runs, it exits non-zero,
  prints the `arm_schema` finding naming `budgets.enforce`, and prints no `mirror deferred`.
  Red when: the invalid file sits at the target's top level, which the reader never reads, so
  `--scaffold` writes its own valid file and defers.
- **AC5** — When `DEPLOY_FULL_OUT` runs in a scratch copy and `ANSWERS_PROBE` runs from that copy's
  root, it prints `WRONG` naming selftest.py.
  Red when: the rename lands in another selftest.py, so the answers still parse.
- **AC6** — When `EVIDENCE_WHOLE` of `TOOL-dGroundRules-51` §5 runs, it prints two lines, numbered
  `165` and `179`.
  Red when: the evidence `TOOL-dGroundRules-34` S32 cites is read from a file its revision does not
  hold at those lines.
  figure: PINNED, the revision being fixed; this is a check on evidence, not on the build.

## 7. Gates

`memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the adopted discovery of the closing diff review of the spec
  run: each line of the brief's respelling inventory verified against its spec and history, the
  uncovered ones restored whole in §4, with the rev:path, attribute and selftest probes run on
  2026-10-23.

## 10. Reuse audit

No existing seam fits beyond the ones observed: each literal is its repaired criterion's own command
or staging with the path whole, and AC6 reuses `EVIDENCE_WHOLE` of `TOOL-dGroundRules-51` rather than
spell the evidence a third time; nothing is built. `python tools/codebase-map/reuse_lookup.py "source
a shell library by its tracked path and probe two overlap rules per table row"` ranked name-stem
hits (`rows`, `probe`, `tracked`) that read no criterion literal. The recall probe returned
`TOOL-dGroundRules-42`, whose bug class this is, `TOOL-dGroundRules-46` and `TOOL-dGroundRules-47`,
and the open ask `TOOL-aKeyedAnnotation-9` on the paths join that drove the respelling; all agree with
source.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal restored
when a respelling cut it to its basename" --terms "acceptance criterion literal stripped respelled
basename fenced block library source whole path paths join PAIRS_TABLE"`
