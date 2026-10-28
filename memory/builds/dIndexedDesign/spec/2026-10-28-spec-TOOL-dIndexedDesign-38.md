# TOOL-dIndexedDesign-38 — the round-1 spec audit's 42 minors batched: shared budgets priced, one resolver and one path rule, readers that refuse what they cannot read, and every unbuildable criterion restated

**Status:** DEFERRED · rev-3 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 17 · advances TOOL-dIndexedDesign-17 · ratified 2026-10-28

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-31-promoted-fix-return.md) | research | TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-31-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-38-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-38-1-spec-writer.md) | journal | — |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
exited BOUNDED with 49 confirmed findings. BUILD-METHOD M4 promotes every MEDIUM and LOW into one
batch unit, or two only where they split into disjoint write sets by M6. They do not split: most items
write `tools/memory-tree/design_lib.py` or `tools/unattended/unattended.sh`, and S5 to S7 and S15 to S17
share `.memory-tree.conf`. This is that one unit. Each finding is named by report id and is its own
scope item, including where the report merged ids into one item. The minors land on 15 units, so this
unit repairs no one unit and takes order 17, above every unit of the build.

| Item | Sev | Id | Lands on | S |
|---|---|---|---|---|
| M1 | MED | 1 | unit 16 S6, AC6 | S1 |
| M2 | MED | 2 | unit 16 Rollout | S2 |
| M3 | MED | 3 | units 3 S1, 16 S9 | S3 |
| M4 | MED | 4 | units 2, 7, 15 S7, 1 | S4 |
| M5 | MED | 13 | unit 16 S7 | S5 |
| M5 | MED | 14 | unit 1 S2 | S6 |
| M5 | MED | 15 | unit 3 S2 | S7 |
| M6 | MED | 16 | unit 10 S4 | S8 |
| M7 | MED | 18 | unit 16 S9, S12 | S9 |
| M8 | MED | 22 | unit 2 S6, S7 | S10 |
| M9 | MED | 23 | unit 2 S1, F4 | S11 |
| M10 | MED | 24 | units 1, 2, 3, 16 | S12 |
| M11 | MED | 25 | unit 6 S6 | S13 |
| M12 | MED | 29 | unit 16 S8 | S14 |
| M13 | MED | 30 | unit 6 S9 | S15 |
| M13 | MED | 31 | unit 8 S12 | S16 |
| M13 | MED | 32 | unit 4 S5 | S17 |
| M14 | MED | 34 | unit 15 S6, F3 | S18 |
| M15 | MED | 35 | unit 9 S7 | S19 |
| M16 | MED | 36 | unit 9 S10 | S20 |
| M17 | MED | 38 | unit 2 S2 | S21 |
| M18 | MED | 40 | unit 16 S6, S7 | S22 |
| M19 | MED | 41 | unit 14 S4 | S23 |
| M20 | MED | 42 | unit 9 S5, S6, S11 | S24 |
| M21 | MED | 43 | unit 12 S5 | S25 |
| M22 | MED | 44 | unit 1 S3 | S26 |
| M23 | MED | 45 | unit 13 §4 | S27 |
| M24 | MED | 46 | unit 4 S3 | S28 |
| M25 | MED | 47 | unit 8 S8 | S29 |
| M26 | MED | 48 | unit 20 S1 | S30 |
| M27 | MED | 50 | unit 7 M2 | S31 |
| L1 | LOW | 6 | unit 8 §2 | S32 |
| L2 | LOW | 7 | unit 9 §3, F1 | S33 |
| L3 | LOW | 8 | unit 9 AC7 | S34 |
| L4 | LOW | 9 | unit 1 §4 | S35 |
| L5 | LOW | 10 | units 13, 20 order | S36 |
| L6 | LOW | 11 | units 12, 9, 6 | S37 |
| L7 | LOW | 12 | units 16, 9 §3 | S38 |
| L8 | LOW | 17 | unit 7 §4 | S39 |
| L9 | LOW | 26 | unit 9 AC10 | S40 |
| L10 | LOW | 27 | unit 7 M1 | S41 |
| L11 | LOW | 51 | units 2 S6, 15 S5 | S42 |

That is 31 MEDIUM and 11 LOW findings by raw id. Ids 13, 14 and 15 share item M5; ids 30, 31 and 32
share M13. Id 23 is the medium-graded side of id 39, whose predicate `TOOL-dIndexedDesign-37` lands;
ids 18 and 22 are the class of H1, whose kinds `TOOL-dIndexedDesign-32` to `-34` bind; id 29 documents
the stage `TOOL-dIndexedDesign-35` lands.

## 2. Scope (IN)

Every item builds at this unit's pass on the code its unit built, unless it says "at the close". A
"ledger note" is §4's rule.

- **S1** — id 1. Unit 16 AC6's base clause is superseded: the `plan_state` slice is compared across
  unit 16's own pass commit, its first parent against the commit itself, never against `57bc3b91`, because unit 9
  S5 changes the slice's section literals at order 1. `derive_ready_state` adds nothing to the slice.
  Ledger note under unit 16 AC6. Observed by AC1.
- **S2** — id 2. The lens reading this build owes itself. Once unit 35 has landed, and before the next
  `--dispatch`, the main loop runs `tier2-review.js` with `coverage: 'only'` over the build's remaining
  specs and commits the `coverage-lens` record, so every later dispatch meets a reading. Until it exists,
  every dispatch after unit 16's pass meets unit 16's coverage refusal, unit 35's own included, and §8
  F1 holds how the run passes that window. Observed by AC2.
- **S3** — id 3. One predicate for "the build declares a spec audit": `check_spec_audit_declared(root, slug)`
  in `gen_build_index.py`, true when the README carries `spec-audit:` or when
  `policy.py get review.design --rev <base>`, the read unit 3 S1 re-points, prints a value
  TOOL-dDeclaredLoop-19 S8's table derives as owed. `--design-exit`'s `with-spec-audit` test calls it. Ledger note under unit 3's S1 criterion. Observed by AC3.
- **S4** — id 4. The four stand-ins retired. The `[[stand-in]]` rows of `item.design.overlaps`,
  `item.design.unit-spec`, `item.design.streams` and `item.design.ready` leave `tools/loop/loop.toml`,
  and each row's `witness` names `design_lib.py --overlaps`, check 12's spec-token grade,
  `plan_streams.py check` and `derive_ready_state`, the readers units 2, 7, 15 and 16 landed.
  **Readers:** by name: `tools/loop/loop.toml`'s rows; READER NOT IN TREE for the loop kit's stand-in
  reader, TOOL-dDeclaredLoop-13 S8's, unbuilt at base · by value: NO VALUE READERS — a deleted row is
  counted by nothing this build ships. Observed by AC4.
- **S5** — id 13. Unit 16's refusal sites fold into one: `check_design_exit` holds exactly one
  `fail 49 "` call site, and its coverage refusals compose their message and reach it. Observed by AC5.
- **S6** — id 14. Unit 1's `_hov` policy-read refusal and its per-unit hand-off refusal compose their
  messages into that same site instead of calling `fail 49` themselves. Observed by AC5.
- **S7** — id 15. Unit 3's refusal of an unreadable `review.design` joins an existing refusal site of
  `check_authorization`, the one its fail 52, 54 and 55 family uses, its message naming `review.design`
  and `check`'s line, so it mints no new code. The census of `tools/unattended/unattended.sh` stays at
  or under its `REFUSAL_CEILINGS` 323, which no edit moves (§8 F2). Observed by AC5.
- **S8** — id 16. `tools/loop/placement.py` runs `check-playbook.sh --resolve` through an inline
  `resolve_bash` block byte-identical to `tools/lib/resolve_bash.py`'s, registered in
  `tools/lib/resolve-python.test.sh`'s parity table, and refuses naming the resolver when it returns
  None. Observed by AC6.
- **S9** — id 18. `coverage-lens` registered through the factory:
  `python record_kinds.py new coverage-lens --tag record.coverage-lens --writer "tier2-review.js coverage=only" --check "memory hygiene"`.
  It sits in the untyped head of `RECORD_KIND_TOKENS`, never `TYPED_RECORD_KINDS`, because
  tier2-review writes it into `reviews/`. Unit 16 S12's hand-written kind line leaves
  `tools/memory-tree/HYGIENE.template.md`, which takes the kind through the registry's generated region
  (TOOL-dTotalRecall-1 S6). Observed by AC7.
- **S10** — id 22. Unit 2's record is bound `**Serves:** overlap <ids>`; `overlap` joins
  `TYPED_RECORD_KINDS` and `build_records.py`'s per-kind table, with the fields unit 2 §4's grammar
  spells, so its `-overlap-<n>.md` home is policed both ways. Observed by AC7.
- **S11** — id 23. Unit 2's `--overlaps` reads a write-set token through `check_meet_path`, the
  predicate `TOOL-dIndexedDesign-37` lands, so its join, `derive_parallel_step` and
  `plan_streams.py check` hold one rule; a root file joins. Ledger note under unit 2's F4 criterion.
  Observed by AC8.
- **S12** — id 24. `resolve_policy_kit` in `tools/unattended/lib-unattended.sh`, beside
  `resolve_index_generator` (`:188`) and built on `resolve_kit_dir` (`:132`): the policy kit's path, or
  status 1 with nothing printed. Units 1, 2, 3 and 16's reads call it in place of `_hopy`/`_hopol`,
  `_ovpy`/`_ovpol`, `$_pk` and the preflight's own resolution, and keep the literal
  `policy.py" get <key>` text the reader-coverage arm counts. Each caller turns status 1 into its named
  miss. Observed by AC9.
- **S13** — id 25. Unit 6's ref reader takes the tree through
  `tree_lib.read_git_output(root, ("ls-tree", "-r", "--name-only", sha, "--", <spec dir>))` and the
  bodies through one `tree_lib.read_blobs_at` call, and spawns no `git show`. Observed by AC10.
- **S14** — id 29. `tools/workflows/README.md` names, at its spec-audit lens list (`:165`), the five
  lenses, the coverage stage and the `coverage` argument, and at its review-shape grammar (`:293`) the
  field `coverage=<with|only|skip>`; `SHAPE_RE` at `tools/workflows/tier2-review.test.sh:1540` admits
  the field. Observed by AC11.
- **S15** — id 30. `SPEC_AGREEMENT_CUTOFF` ships blank in `.memory-tree.conf`, so armed `_CUTOFF` keys
  stay at the `cutoff_keys_armed` pin of 36 (`tools/drift-audit/drift_signals.py:351`); arming it is an
  owner-attended landing's (§8 F3). Ledger note under unit 6's S9 criterion. Observed by AC12.
- **S16** — id 31. `SPEC_FORK_RECORD_CUTOFF` ships blank, as S15. Ledger note under unit 8's S12
  criterion. Observed by AC12.
- **S17** — id 32. `SPEC10_PROBE_CUTOFF` ships blank, as S15. Ledger note under unit 4's S5 criterion.
  Observed by AC12.
- **S18** — id 34. The `plan` entry of `tools/roles/workflows.toml` becomes `driver = "workflow"`,
  `harness = "{prefix}/workflows/plan-streams.js"` and `stages = { planner = "gov-planner" }`;
  `render_agents.py --write` re-renders `.claude/roles.json`. `plan-streams.js` throws, naming `roles`,
  on a call without it (§8 F4). Observed by AC13.
- **S19** — id 35. review_replay's tag-keyed sections, every reader: under spec-audit `measure_recall`
  compares sections by equality, never by window arithmetic; `render_replay` prints a tag after `:`,
  not `:§`; the section-ref and window-0 selftest expectations, the module docstring and
  `tools/workflows/README.md`'s matching rule (`:502-505`) read tags. Observed by AC14.
- **S20** — id 36. The two tier-dependent prompt sites unit 9 S10 missed name tags: tier2-review's
  `PROBE_RULES` reads "each `[section.acceptance]` criterion", and unattended-build's fold prompt
  reads "their `[section.revision-log]` lines" at both of its sites. Observed by AC15.
- **S21** — id 38. An `**overlaps**` payload holding `/` or `.` is a path, admitted only when
  `check_meet_path` holds, so a root, `.`, a glob or `..` acknowledges nothing; the consumer of
  `read_spec_edges(text, "overlaps")` and check 12's `**overlaps**` arm refuse it by name. Observed by
  AC8.
- **S22** — id 40. A `--design-exit` exit other than 0 or 1 is a refusal: `check_design_exit` refuses at
  `--phase BUILDING` and `--dispatch` through S5's site naming the exit, and `derive_ready_state` prints
  no token and returns non-zero, which every caller refuses. Observed by AC16.
- **S23** — id 41. Unit 14's verdict adds a fourth test: an arm passes only when every dispatched case
  parsed, else `verdict <arm>: unarmed — parsed <n> of <d>`. An answer refused past the cap or for an
  unknown name counts as unparsed for its case and never refuses the run. Observed by AC17.
- **S24** — id 42. Unit 9's twins, the awk at `unattended.sh`'s `plan_state`, `lib-unattended.sh`'s
  reader, `tools/runlog/model.py`, `check-recall.py`'s `S10_RE` and `replay-phrases.py`'s `_SEC10`,
  each skip fenced lines and strip a trailing CR before matching; contract 3 gains a CRLF row, and its
  fenced row expects "not a heading" of every reader. Observed by AC18.
- **S25** — id 43. Unit 12's `gov_tag.py bundle` wrapper treats any non-zero exit as a
  `DesignRefusal` naming the tag, the exit code and the stderr line, and bounds the call at
  `PROBE_TIMEOUT_SECONDS`, 30, a kill being a refusal. Observed by AC19.
- **S26** — id 44. `--audit-pins` gains the verdict `blocked`, when the highest pin at or above the header
  revision belongs to a record whose `## Verdict:` is `BLOCKED`; unit 1's hand-off refuses it under
  `ready-plus-audit` with the remedy "revise and re-audit". Observed by AC20.
- **S27** — id 45. Unit 13's MUST test matches `<symbol>` as a whole token,
  `(?<![\w.-])<symbol>(?![\w-])`, on unfenced lines at the `**Index:**` sha; for a `.py`, `.sh` or `.js`
  path it also requires a definition shape on a non-comment line, and for any other file a key or
  heading. Observed by AC21.
- **S28** — id 46. Unit 4's evidence forms are a tracked path, optionally suffixed `:<line>` or
  `:<a>-<b>` and stripped before `ls-files`, or a backticked command; prose is refused with its own
  finding text naming the form. Observed by AC21.
- **S29** — id 47. Unit 8's fork join reds a `Class`, `Level` or `Resolver` value outside its closed set,
  a `Pick` not among `Options`, and an F-item carrying `FACT-QUESTION` whose record's `Class` is not
  `fact`; its population line adds "a goal class is self-declared". Observed by AC22.
- **S30** — id 48. Unit 20's revision binding reads every `*.md` of the build's `build/` folder at `rev`
  through `read_blobs_at` and selects by the first `**Serves:**` binding, so a misnamed
  `feature-design` record is refused at both bindings. Observed by AC23.
- **S31** — id 50. Unit 7's M2 matches a unit id as a whole token, `(?<![\w-])<id>(?![\w-])`, in the
  `Pass:` trailer first and, falling back to the subject, only in the head position
  `build(<slug>): <id> —`. Observed by AC24.
- **S32** — id 6. Unit 8 owes no `sections` column: its arm (e) reads `### Interfaces` through
  `read_spec_section(text, "section.design")`. Ledger note under unit 8's S5 criterion. Observed by AC25.
- **S33** — id 7. Unit 7 trials the format and files the arming ask (its S7), and `SPEC_TAGS_CUTOFF`
  stays blank past this build until that ask is answered. Ledger note under unit 9's F1 criterion.
  Observed by AC25.
- **S34** — id 8. Unit 9 AC7 is observed by a direct probe, AC26, not by `--selftest`. Ledger note under
  unit 9 AC7. Observed by AC26.
- **S35** — id 9. Unit 1's per-unit call passes the exit lines `check_design_exit` holds:
  `derive_ready_state "$spec" "$FORK_CUTOFF" "$_exit_lines"`, the variable S5's function names, so
  `--design-exit` runs once per call. Observed by AC16.
- **S36** — id 10. In step 9, unit 13 lands before unit 20, which rebases over its `loop.toml` and
  `record-kinds.toml` rows. Observed by AC27.
- **S37** — id 11. The ledger answers of unit 12 AC6, unit 9 AC12 and unit 6 AC3 each quote a
  backticked token that sits whole on its criterion's first line. Observed by AC25.
- **S38** — id 12. The coverage lens's read of sections through unit 9's `design_lib.py --section` is
  named in `COVERAGE_BRIEF` and in this unit's §3, and unit 16's ledger records the edge. Observed by
  AC15.
- **S39** — id 17. Unit 7's "254 past audits" is superseded by its AC4's derived population, whose
  count and command its research record states. Ledger note under unit 7 AC4. Observed by AC25.
- **S40** — id 26. Unit 9 AC10's command is scoped to the lens literal, the coverage brief, `PROBE_RULES`
  and the address line: `sed -n '/^const SPEC_LENSES/,/^]/p'` piped to `grep -nE "section[- ][0-9]"`
  prints nothing, and so does the same grep over the other three. Observed by AC15.
- **S41** — id 27. Unit 7's M1 maps an ordinal to its tag through unit 9 S7's `extract_section_ref`,
  imported by its instrument, never a third reader. Observed by AC24.
- **S42** — id 51. `design_lib.py --overlaps --record <slug>` and `plan_streams.py write <slug>` validate
  the slug by `backlog.SLUG_RE` and the lowercase-initial rule (`gen_build_index.py:4141`), and refuse a
  slug whose README is absent, exit 2 and nothing written. Observed by AC8.

## 3. Non-goals (OUT)

- Any HIGH or BLOCKER of the audit: `TOOL-dIndexedDesign-31` to `-37`.
- Raising `MAX_LENSES`, `REFUSAL_CEILINGS` or `cutoff_keys_armed`: owner turns (§8 F2, F3).
- Rewriting a CLOSED spec's text: each repaired unit is answered in its ledger (§4), never re-specced.
- The report's left-shift gates and checklist entries; no clause of this build names them.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-1` — S4, S6, S12, S26, S35: its hand-off arms, `_hopy`, `--audit-pins`, its per-unit call and `item.design.ready`
- **consumes-from** `TOOL-dIndexedDesign-2` — S4, S10, S11, S12, S21, S42: `--overlaps`, its record, `**overlaps**` payloads, `_ovpy` and `item.design.overlaps`
- **consumes-from** `TOOL-dIndexedDesign-3` — S3, S7, S12: the `review.design` read and its refusal
- **consumes-from** `TOOL-dIndexedDesign-4` — S17, S28: its cutoff key and evidence grammar
- **consumes-from** `TOOL-dIndexedDesign-6` — S13, S15, S37: its ref reader, cutoff key and AC3
- **consumes-from** `TOOL-dIndexedDesign-7` — S4, S31, S39, S41: its instrument and `item.design.unit-spec`
- **consumes-from** `TOOL-dIndexedDesign-8` — S16, S29, S32: its cutoff key, fork join and preconditions
- **consumes-from** `TOOL-dIndexedDesign-9` — S19, S20, S24, S33, S34, S37, S38, S40: `design_lib.py --section`, its twins, review_replay and AC7, AC10, AC12
- **consumes-from** `TOOL-dIndexedDesign-10` — S8: `placement.py`'s subprocess
- **consumes-from** `TOOL-dIndexedDesign-12` — S25, S37: the bundle wrapper and AC6
- **consumes-from** `TOOL-dIndexedDesign-13` — S27, S36: the MUST test and step 9
- **consumes-from** `TOOL-dIndexedDesign-14` — S23: the `bug-class-intent` verdict
- **consumes-from** `TOOL-dIndexedDesign-15` — S4, S18, S42: `plan-streams.js`, `plan_streams.py write` and `item.design.streams`
- **consumes-from** `TOOL-dIndexedDesign-16` — S1, S2, S3, S5, S9, S12, S14, S22, S38: `check_design_exit`, `derive_ready_state`, `--design-exit` and `coverage-lens`
- **consumes-from** `TOOL-dIndexedDesign-20` — S30, S36: the revision binding and step 9
- **consumes-from** `TOOL-dIndexedDesign-35` — S14, S38: the coverage stage and `COVERAGE_BRIEF`
- **consumes-from** `TOOL-dIndexedDesign-37` — S11, S21: `check_meet_path`, which `--overlaps` and its payload rule call
- **consumes-from** external — TOOL-dTotalRecall-1's `record_kinds.py new` and generated kind region, PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS` and `build_records.py`, TOOL-dBoundRoles-1's `gov-planner` role, each DEFERRED at base and an ancestor's
- **consumes-from** `TOOL-dIndexedDesign-39` — §8 F1's premise: from unit 16's pass tip the harness is admitted, so the window is only the lack of a reading (id 1)
- **consumes-from** `TOOL-dIndexedDesign-44` — S2's `coverage: 'only'` reading, which runs after that unit's pass, since before it an `only` run writes no record (id 26)
- **hands-off** `TOOL-dIndexedDesign-40` — S15 to S17, which that unit lands in the passes of units 6, 8 and 4, so this unit's pass writes none of them and AC12 finds them true (id 2)
- **hands-off** `TOOL-dIndexedDesign-41` — S5 to S7, which that unit lands in the passes of units 16, 1 and 3 with no net `fail` site, so AC5 finds them true (id 3)
- **hands-off** `TOOL-dIndexedDesign-46` — the items and criteria the audit's minors land on; that unit's S12 keeps S4's four stand-in rows, so this unit's pass deletes none of them (ids 4, 5, 6, 8, 9, 10, 15, 16, 18, 19, 22, 23, 24, 25, 28, 30 and 38)
- **consumes-from** `TOOL-dIndexedDesign-50` — S2's `coverage: 'only'` reading and AC2's window, reachable from unit 35's pass commit once that unit lands unit 44's counts in unit 16's pass (id 3)
- **hands-off** `TOOL-dIndexedDesign-51` — S22 and S35, which that unit restates at this unit's pass: S22's exit-2 refusal sets `_dx_msg` and refuses through unit 41 S1's composed sites, adding no `fail` site (id 20)
- **hands-off** `TOOL-dIndexedDesign-52` — S3's `check_spec_audit_declared`, which that unit has refuse a present undated value and a cut-short conf, resting on S22's reading of exit 2 as a refusal (id 26)
- **hands-off** `TOOL-dIndexedDesign-53` — S5's one-site sentence and AC5's third clause, which that unit's S1 supersedes at this unit's pass: `check_design_exit` holds no `fail <n> "` (id 2)

## 4. Design

### Evidence

- `.memory-tree.conf:653` sets `REFUSAL_CEILINGS` for `tools/unattended/unattended.sh` at 323, and the
  report's re-run of `check-arms.py --emit-floors` printed 323 sites; `check-arms.py:989-993` reds growth
  and `:985` wants a DECISIONS.md id for a raise.
- `tools/drift-audit/drift_signals.py:337-351` pins `cutoff_keys_armed` at 36; every past raise was an
  owner ruling or a decision.
- `tools/hooks/agent-cap.js:1735` `checkHarnessCall` admits a Workflow call only by a `harnesses` entry
  of `.claude/roles.json`, which lists three scripts on 2026-10-28.
- `tools/lib/resolve_bash.py` is the canonical block, its parity row at `resolve-python.test.sh:186`.
- `tools/workflows/review_replay.py:70` keys sections by integer, `:267` compares by `abs(...)`, and
  `:311` joins with `":§"`.
- `gen_build_index.py:3679` sets `PROBE_TIMEOUT_SECONDS = 30` beside `run_probe`, the bound S25 reuses.
- `backlog.SLUG_RE` (`tools/memory-tree/backlog.py:129`) and the lowercase-initial test at
  `gen_build_index.py:4141` are the slug guard S42 copies by call, not by text.

### Ledger notes

Where an item supersedes a criterion or a sentence of a CLOSED unit, that unit's acceptance ledger
carries, at the close, a continuation line under the named criterion's answer, two spaces in: the label
`TOOL-dIndexedDesign-38 S<n>` and, on that one physical line, a backticked token of the item. A note is
never its own `- AC` line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_spec_audit_declared` | Python function, `gen_build_index.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `resolve_policy_kit` | shell function, `lib-unattended.sh` | `sh.function`, answered OK by `lexicon.py --suggest` |
| `blocked` | `--audit-pins` verdict | none |
| `coverage-lens`, `overlap` | registry rows, tuple members | none |

### Migration

`.memory-tree.conf` loses three values units 4, 6 and 8 set; their fixtures arm the keys themselves.
`tools/loop/loop.toml` loses four stand-in rows. No record is rewritten.

### Rollout

The pass lands every item but S2 at order 17. S2 is one act earlier, after unit 35's pass, because
the stall it ends falls there; §8 F1 is the window before it. The close reads the ledgers.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S11, S13, S21, S25, S28, S29, S30, S42
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/build_records.py`, `tools/memory-tree/record-kinds.toml`: S9, S10, S27
- `tools/memory-tree/gen_build_index.py`: S3, S26, S27
- `tools/memory-tree/plan_streams.py`: S42
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`: S21
- `tools/memory-tree/marker-contract.test.sh`: S24
- `tools/memory-tree/HYGIENE.template.md`, render `memory/HYGIENE.md`: S9
- `tools/unattended/unattended.sh`, `tools/unattended/lib-unattended.sh`, `tools/unattended/unattended.test.sh`: S5 to S7, S12, S22, S24, S26, S35
- `tools/runlog/model.py`, `tools/memory-recall/check-recall.py`, `tools/codebase-map/replay-phrases.py`: S24
- `tools/workflows/review_replay.py`, `tools/workflows/README.md`: S14, S19
- `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`, renders `tools/workflows/tier2-review.js` and `tools/workflows/unattended-build.js`: S20, S38
- `tools/workflows/tier2-review.test.sh`: S14
- `tools/workflows/replay_scorer.py`: S23
- `tools/workflows/plan-streams.template.js`, render `tools/workflows/plan-streams.js`: S18
- `tools/roles/workflows.toml`, render `.claude/roles.json`: S18
- `tools/loop/loop.toml`: S4; `tools/loop/placement.py`, `tools/lib/resolve-python.test.sh`: S8
- `.memory-tree.conf`: S15 to S17
- `memory/builds/dIndexedDesign/build/`: the ledger notes and unit 7's instrument (S31, S41)
- `memory/builds/dIndexedDesign/reviews/`: S2's record

### Alternatives rejected

- **Two batches.** Lost to M6 clause 1: `design_lib.py` and `unattended.sh` sit in every candidate
  split, and S5 to S7 and S15 to S17 share `.memory-tree.conf`.
- **Fold each fix into its unit's spec.** Lost to the owner's 2026-10-05 ruling M4 records: none is
  folded.

## 5. Production-readiness checklist

- security — S42 validates a slug at two write boundaries; S8 refuses a blind shell; S25 bounds a
  subprocess; S18 widens the harness admission list by one named script.
- perf / scale — S35 runs `--design-exit` once per call instead of once per unit.
- error / empty / loading states — S22, S25 and S42 turn silent passes into named refusals.
- observability — every refusal names its cause; S23 prints the parsed count it ruled on.
- risks — S2's act precedes this unit's order, and the window before it needs §8 F1's owner act; AC2
  shows whether the reading came in time.
- testing — AC1 to AC27, by probe, fixture or ledger; the arms §7 declares.
- migration — three conf values and four stand-in rows; nothing else.
- user docs — none under `help/`; `tools/workflows/README.md` is S14's and S19's.

## 6. Acceptance criteria

- **AC1** — When `git show <p>^:tools/unattended/unattended.sh` and `git show <p>:tools/unattended/unattended.sh`
  are each piped to `sed -n '/^plan_state()/,/^}/p'`, `<p>` being unit 16's pass commit, the two
  slices are identical, and unit 16's ledger holds the S1 note. Red when: unit 16 changed the slice.
  permission: at the close.
- **AC2** — When `python gen_build_index.py --design-exit dIndexedDesign` runs at the close, it prints no
  `· none` lens line, and `git log --diff-filter=A` over `memory/builds/dIndexedDesign/reviews/` shows a
  `coverage-lens` record committed after unit 35's pass commit and before the next pass commit.
  Red when: a dispatch after it met no reading. permission: at the close.
- **AC3** — When `--design-exit` runs under `with-spec-audit` over a fixture whose `.governance/policy.toml`
  sets `review.design = "owed"` and whose README has no `spec-audit:`, it prints a lens line. Red when:
  the policy opt-in owes no reading.
- **AC4** — When a `python -c` `tomllib` read of `loop.toml` lists `[[stand-in]]` rows, none names
  `item.design.overlaps`, `item.design.unit-spec`, `item.design.streams` or `item.design.ready`, and each
  item's `witness` names its reader. Red when: a stand-in survives its witness.
- **AC5** — When `python check-arms.py --emit-floors` runs in the memory-tree kit, it prints
  `tools/unattended/unattended.sh` at or under 323, `REFUSAL_CEILINGS` is unchanged, and `check_design_exit`'s
  body holds one `fail 49 "`. Red when: the census grows or a design refusal calls `fail` itself.
- **AC6** — When `grep -c ">>> resolve_bash_py" placement.py` runs in the loop kit it prints 1, and a
  `repeat` fixture whose `--resolve` names the real fixture playbook passes through the resolved bash.
  Red when: a bare `bash` runs the script, or the copy drifts.
- **AC7** — When a `python -c` `tomllib` read of `record-kinds.toml` finds rows `coverage-lens` and
  `overlap`, and `tree_lib.read_bindings` reads a scratch `coverage-lens` record and the record
  `--overlaps --record` writes as `bound`, kinds `coverage-lens` and `overlap`. Red when: either reads
  `malformed` or has no row.
- **AC8** — When `design_lib.py --overlaps` runs over two builds' specs sharing only `.memory-tree.conf`,
  it reports the pair, as `derive_parallel_step` reads `no` and `plan_streams.py check` reds arm (c);
  an `**overlaps**` bullet with payload `tools/` is refused and acknowledges nothing; and `--record ../x`
  and `--record tNope` each exit 2 writing nothing, as does `plan_streams.py write tNope`. Red when: the
  three joins disagree, a root payload acknowledges, or a bad slug writes.
- **AC9** — When `grep -c "resolve_policy_kit" lib-unattended.sh unattended.sh` runs in the unattended kit,
  it counts the definition and the four call sites, no `_hopy`, `_ovpy` or `_pk` assignment resolves
  the kit itself, and an absent policy kit makes the hand-off read refuse naming the miss. Red when: a
  caller resolves on its own.
- **AC10** — When a `python -c` reads one fixture spec holding a multi-byte character at HEAD and at a
  ref through unit 6's reader, the two texts are equal, and `grep -n "git show"` over `design_lib.py`
  prints no line of that reader. Red when: the ref read differs or spawns `git show`.
- **AC11** — When `grep -n "coverage=" README.md` runs in the workflows kit, it prints the grammar line,
  and the suite's `SHAPE_RE` line holds `coverage=`. Red when: either lags the line unit 16 writes.
- **AC12** — When `grep -E '^(SPEC_AGREEMENT|SPEC_FORK_RECORD|SPEC10_PROBE)_CUTOFF=""$' .memory-tree.conf`
  runs, it prints three lines, and a `python -c` count of non-blank `_CUTOFF` keys over the tracked root
  confs prints 36. Red when: a key is armed past the pin. figure: 36 is PINNED by `drift_signals.py:351`.
- **AC13** — When a Workflow payload naming `plan-streams.js` with `roles` is piped to `node agent-cap.js`, it
  is admitted, and a stub run of `plan-streams.js` without `roles` throws naming it. Red when: the hook
  denies the harness or a roleless call spawns.
- **AC14** — When a `python -c` calls review_replay's `measure_recall` on two spec-audit items in one
  tagged section, it matches without a `TypeError`, and `render_replay` prints `x.md:section.scope`.
  Red when: tags meet window arithmetic or print after `:§`.
- **AC15** — When `grep -nE "section[- ][0-9]"` runs over tier2-review's `SPEC_LENSES` literal (by
  `sed -n '/^const SPEC_LENSES/,/^]/p'`), its `COVERAGE_BRIEF`, `PROBE_RULES` and address line, and over
  unattended-build's fold prompts, it prints nothing, and `COVERAGE_BRIEF` holds `design_lib.py --section`.
  Red when: a tier-dependent number remains.
- **AC16** — When `--phase BUILDING` and `--dispatch` run on a fixture whose committed policy file is
  invalid, and again with the policy kit absent, both refuse naming the exit; and a `bash -x` trace of
  `--phase BUILDING` over a three-unit roster shows one `--design-exit` run. Red when: an exit 2 admits,
  or `--design-exit` runs per unit.
- **AC17** — When `python replay_scorer.py --experiment <manifest>` scores a planted run whose arm parsed
  10 of 47 cases with high precision, it prints `unarmed — parsed 10 of 47`. Red when: it prints `armed`.
- **AC18** — When each S24 twin reads a scratch spec holding a tagged heading inside a fence and a
  numbered heading ending in CR, `extract_open_questions`, `S10_RE` and `_SEC10` by `python -c`,
  `plan_state` by the `sed -n` slice from `^plan_state()` to its closing brace of `unattended.sh`, and
  `read_consumes_from` by sourcing `lib-unattended.sh`, none reads the fenced one and each reads the CR
  one. Red when: a twin differs.
- **AC19** — When `design_lib.py --bundle feature.nope-not-a-tag` runs with `gov_tag.py` stubbed to exit 1
  with a traceback, it exits non-zero naming the tag and exit 1. Red when: empty output reads clean.
- **AC20** — When `gen_build_index.py --audit-pins tFix` reads a unit pinned at its revision by a record
  whose `## Verdict:` is `BLOCKED`, it prints `blocked`, and `--dispatch` under `ready-plus-audit`
  refuses it. Red when: it reads `current`.
- **AC21** — When unit 13's grader reads MUSTs whose symbol is only in a comment and only inside a longer
  identifier, each exits 1, a MUST on a TOML key exits 0; and unit 4's grammar admits
  `BUILD-METHOD.md:34-37` and refuses `the table above` naming the form. Red when: presence passes, or
  a line suffix reds.
- **AC22** — When `design_lib.py --decompose` runs over plants of a preference fork recorded `fact`, a
  `FACT-QUESTION` item recorded `preference` and `Class: preferences`, each is a finding. Red when: one
  admits.
- **AC23** — When `design_lib.py --reentry tFix --base <rev>` runs where a feature record is misnamed at
  base, it exits 2 naming it. Red when: it diffs as `interface added`.
- **AC24** — When unit 7's instrument runs `--fixture divergence`, where a `TOOL-tFix-12` commit precedes
  unit 1's, M2 takes unit 1's own commit, and `grep -c "extract_section_ref"` over the instrument prints
  at least 1. Red when: a substring match wins, or M1 maps ordinals itself. permission: at the close.
- **AC25** — When `grep -n "TOOL-dIndexedDesign-38 S"` runs over the acceptance ledgers of units 2, 3, 4,
  6, 7, 8, 9, 12 and 16 at the close, it prints the notes of S1, S3, S11, S15 to S17, S32 to S34 and
  S37 to S39, each under its criterion, and S37's carry a token found whole on that criterion's first
  line. Red when: a note is missing or is a `- AC` line of its own. permission: at the close.
- **AC26** — When a `python -c` resolves `x.md:AC2` and `x.md:section 5` over a scratch Tier-1 subject
  through review_replay, both print `section.acceptance`. Red when: either prints a number.
- **AC27** — When `git log --format=%s` lists the build's pass commits at the close, unit 13's precedes
  unit 20's. Red when: the order is reversed. permission: at the close.

## 7. Gates

`kit/dogfood doc parity` · `routed-commits selftest` · `pre-push run-log line` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `runlog selftest` · `run-gates run-log line` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `drift-audit records` · `marker contracts` · `python resolver (behaviour + inline parity + idiom ban)` · `roles render wiring` · `agent-cap self-test` · `review-replay selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC9 AC16 · an absent policy kit and an invalid policy file under both verbs, staged by `check_design_exit` admitting on exit 2 · none
New arm: tools/memory-tree/marker-contract.test.sh · covers AC18 · contract 3's CRLF row and fenced row over every twin, staged by removing one twin's fence tracking · none
New arm: tools/workflows/tier2-review.test.sh · covers AC11 · `SHAPE_RE` over a shape line carrying `coverage=only`, staged by the pre-field regex · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 · an `**overlaps**` bullet with a root payload, staged by admitting any non-empty payload · none

## 8. Open questions

- **F1 — How does this build run pass the window between unit 16's pass and its first lens reading
  (id 2)?** After unit 16 lands, `--dispatch` refuses every unit with no `coverage-lens` reading under
  this repo's defaults, `design.coverage` `refuse` and `design.coverage.semantic` `every-exit`. No
  reading can be made until unit 35 lands, because unit 16's six-lens harness is denied by the
  agent-cap hook (report id 28), and unit 35's own dispatch is refused in that window. Options: (a) the
  owner commits `design.coverage = "warn"` to `.governance/policy.toml` on the run branch at unit 16's
  pass, and restores `refuse` once S2's record lands; the policy guard keeps that value from an agent.
  (b) A grace in `check_design_exit`: a unit whose newest pinning spec-audit record carries no
  `coverage=` field reads its lens line as `WARN`. Built here at order 17, it lands after the window,
  and it relaxes `design.coverage` for every unit audited before the lens. (c) Unit 16's S8 and S9 moved
  to the build's last order, the skeptic's second fix: a re-scope of unit 16, which no repair unit may
  make. Recommendation: (a), the one option that passes the window without weakening the gate for later
  builds. It needs the owner, so a delegated run parks at unit 16's boundary until it is taken, and the
  M3 sweep before the build run's first unit is where the owner sees it.
- **F2 — Raise `REFUSAL_CEILINGS` or fold the sites (ids 13 to 15)?** Options: (a) raise by a dated
  decision; (b) fold into existing sites. (a) moves a declared ceiling the conf gives no run the terms to
  move (M3). RESOLVED (agent, 2026-10-28, delegated): (b), rung 3, the one survivor. widens: none · relaxes: none
- **F3 — Raise `cutoff_keys_armed` or ship the three keys blank (ids 30 to 32)?** Options: (a) raise 36 to
  39 with a reason; (b) ship blank and arm at an owner-attended landing. Every past raise was an owner
  ruling, so (a) is an owner turn. RESOLVED (agent, 2026-10-28, delegated): (b), rung 3; the arming is
  an ask for this build, accept line "the three keys armed and `cutoff_keys_armed` raised 36 to 39 by
  owner ruling". widens: none · relaxes: none
- **F4 — Change the `plan` entry here, or wait on ask TOOL-dIndexedDesign-27 to dBoundRoles (id 34)?**
  Options: (a) S18 here, as unit 5 changes the `research` entry; (b) make the ask a build-run
  precondition. (b) leaves the harness denied if the parent does not move. RESOLVED (agent, 2026-10-28,
  delegated): (a), rung 3, the most feature-rich survivor; it meets that ask's accept line.
  grants: PLAY-dClosedLoop-3 the `plan` entry's `driver`, `harness` and `stages`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, the minors batch of the round-1 spec audit of this build: 31
  MEDIUM and 11 LOW findings by raw id, each its own scope item.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-40, TOOL-dIndexedDesign-41 and TOOL-dIndexedDesign-46 and the
  consumes-from bullets mirroring the hands-off edges of TOOL-dIndexedDesign-39 and
  TOOL-dIndexedDesign-44, promoted by the round-1 spec audit of units 31 to 38; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-51, TOOL-dIndexedDesign-52 and TOOL-dIndexedDesign-53 and the
  consumes-from bullet mirroring the hands-off edge of TOOL-dIndexedDesign-50, promoted by the round-1
  spec audit of units 39 to 46; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names: `resolve_kit_dir` and `resolve_index_generator` for S12,
`tree_lib.read_blobs_at` and `read_git_output` for S13 and S30, `resolve_bash.py`'s block for S8,
`PROBE_TIMEOUT_SECONDS` for S25, `backlog.SLUG_RE` for S42, `check_meet_path` for S11 and S21, and
`record_kinds.py new` for S9. The probe
`python tools/codebase-map/reuse_lookup.py "resolve a sibling kit directory from the unattended driver"`
ranked `resolve_kit_dir` second, the seam S12 builds on, beside
`resolve`, `kit_rel` and `kit_dir`, none a driver-side resolver of the policy kit; so S12 extends
`resolve_kit_dir` as `resolve_index_generator` (`lib-unattended.sh:188`) already does, and no item
builds a seam that exists.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted finding repair unit order minors batch blocker high disposition rescope"`
