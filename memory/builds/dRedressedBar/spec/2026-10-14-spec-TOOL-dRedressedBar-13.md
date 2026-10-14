# TOOL-dRedressedBar-13 — the units-10-11 spec audit's 5 mediums and 18 lows, batched: each criterion half observed in a form that can fail, each false sentence corrected, and the code sites they describe made to say what the specs claim

**Status:** SPECCED · rev-4 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-13-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-13-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-13-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-13-3-spec-writer.md) | journal | — |
| [2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 10 and 11
(`reviews/2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md`) exited CONVERGED with
24 confirmed findings: no blocker, one high, 5 mediums and 18 lows. BUILD-METHOD M4 promotes the
high alone, as `TOOL-dRedressedBar-12`, and batches every medium and low into ONE unit. This is that
unit. The minors land on specs 10 and 11, so it repairs no unit in particular, and it is ordered
after every unit of this build. It closes these findings, by report id, each with the report item it
shares:

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 1 | MEDIUM | M1 | unit 10 AC5 | the false-sentence half greps line by line, and spec 8 wraps the sentence | S1 |
| 2 | MEDIUM | M2 | unit 10 S9, AC9 against §3, §4, §5 | edits spec 7's AC4 while saying no criterion text moves | S2 |
| 3 | LOW | L1 | unit 10 S17 | its spec-9 half is observed by no criterion | S3 |
| 4 | LOW | L2 | unit 10 AC8 | the `project-owned` half already passes on the hands-off line | S4 |
| 5 | LOW | L3 | unit 10 §1 | says eight specs where the table holds nine | S5 |
| 6 | LOW | L4 | unit 11 §4, S4 | adds a fourth row element and leaves the three-element contract stated | S6 |
| 7 | LOW | L5 | unit 11 S4, AC6 | the key rule's labels have no prefix, so AC6's `lexicon ` count is ambiguous | S7 |
| 8 | MEDIUM | M1 | unit 10 AC5 | as id 1, from the grounding lens | S8 |
| 9 | LOW | L6 | unit 10 AC3 | the `n` half matches any shell line | S9 |
| 10 | LOW | L7 | unit 11 S4, AC6 | the agreement rule's union by `want` is observed by no arm | S10 |
| 11 | LOW | L8 | unit 11 §4 | describes a README edit as pending that has been made | S11 |
| 12 | LOW | L9 | unit 10 §4, unit 11 §5 | "exactly as wide as unit 9's" fails when the target's parent holds the hook | S12 |
| 13 | LOW | L10 | unit 11 §4 | the new stderr tail decodes with the host codepage | S13 |
| 14 | LOW | L11 | unit 10 S5, AC5 | claims six registry classes observed; AC5 compares five | S14 |
| 15 | LOW | L12 | unit 10 §4 | says the probe keys have two readers; a third exists | S15 |
| 16 | LOW | L13 | unit 10 AC5, AC12, §10 | re-types the leg's count and comparison instead of reusing its seams | S16 |
| 17 | MEDIUM | M3 | unit 11 AC4, §4 | fixture B rebuilds the vintage rewind by hand | S17 |
| 18 | MEDIUM | M4 | unit 10 §4, §7 | invites a hand `{prefix}` replace the idiom ban fires on, and omits that leg | S18 |
| 19 | LOW | L14 | unit 10 §7 | omits `spec tokens` and `encoding posture` | S19 |
| 20 | LOW | L15 | unit 11 §4, §7 | omits its acceptance ledger from Files touched, so §7 misses two legs | S20 |
| 21 | LOW | L8 | unit 11 §4 | as id 11, from the blast-radius lens | S21 |
| 22 | LOW | L16 | unit 11 S2, unit 10 S22 | no unit updates the code-2 block's comment after its probe changes | S22 |
| 24 | LOW | L17 | unit 11 §5 | the security line prices one adopter's stderr; the tail reaches every adopter | S24 |

Id 16 was graded medium by its finder and low by the skeptic, and the skeptic's grade binds. Units
10, 11 and 12 build first, as written. This unit then observes, over the tree they leave, the
corrected form of each criterion half the audit found could not pass or could not fail. It records
each reading in its own acceptance ledger and corrects the false prose in specs 9, 10 and 11. It also
changes the code sites §4 lists, so they say what those specs claim.

## 2. Scope (IN)

Item S<n> closes report id n. Id 23 is HIGH and belongs to `TOOL-dRedressedBar-12`, so no S23
exists. S25 is the record. Items that share a report item share its observation, and each still
names its own id.

- **S1** — id 1, M1. Unit 10 AC5's false-sentence half is observed over spec 8's Gates section
  joined into one line, so a sentence wrapped across two lines is seen. Spec 10's revision line
  states that AC5's line-wise grep printed nothing at the pinned spec 8, and names this unit's AC1.
  Observed by AC1.
- **S2** — id 2, M2. Spec 10's §3 first non-goal, §4 Alternatives row 2 and §5 risks are corrected
  in place. They name spec 7's AC4 wording as the single criterion text S9 edits, and say why unit 7's
  ledger is not contradicted. The range gains units 8 and 9, and neither moves a kit version:
  unit 8's one `tools/` file is `project-owned` (`tools/run-gates/kit.toml:40-41`), and unit 9's
  files sit under `{prefix}/govkit`, which the registry exempts (`tools/govkit/registry.toml:295-297`).
  So the kit set AC4 derives from its own `epoch` run is the same set before and after. Observed by
  AC2.
- **S3** — id 3, L1. Unit 10 S17's spec-9 half is observed in spec 9's Gates section: its leg line
  names `codebase-map coverage + freshness`, the leg that reads the `symbols.json` unit 9's own pass
  regenerates and commits (spec 9's S7). Spec 10's revision line names this unit's AC3. Observed by
  AC3.
- **S4** — id 4, L2. Unit 10 AC8's `project-owned` half is observed over spec 4's non-goal list
  alone, cut before its Edges, so the hands-off line cannot satisfy it. Spec 10's revision line
  names this unit's AC4. Observed by AC4.
- **S5** — id 5, L3. Spec 10 §1 says "nine specs". Observed by AC5.
- **S6** — id 6, L4. The docstring of `check_outcome_states` in `tools/govkit/matrix.py` states the
  optional fourth row element unit 11 adds: a mapping from a target-relative path to text, written
  before classifying and deleted after. Spec 9's §4 sentence on the `(label, present paths, expected
  verdict)` rows is corrected in place to name it. Observed by AC6.
  - **Readers:** S6 retires a stated contract: the three-element row shape above, as spec 9 and the
    helper's docstring spell it. The word "deleted" above describes the fourth element's scratch
    file, which is not a retirement. The inventory was read at `29c72f51` with
    `git grep -n -i 'present paths\|expected verdict\|three-element'` and
    `git grep -n -w 'check_outcome_states'` over the tracked tree. Outside the two readers below,
    the contract is only quoted, by the audit report (lines 121 and 242) and by this spec, which
    are records, so nothing in them moves.
    by name: `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:200`, the §4
    sentence that spells the three elements; and `tools/govkit/matrix.py`, whose helper docstring
    unit 9 writes with the same three. That docstring is not in the tree at commit 29c72f51,
    because unit 9 is unbuilt there and the second grep finds no hit under tools/. It is in the
    tree when this unit builds, because unit 9 builds first. Both files are already in §4's Files
    touched, so no file is added.
    by value: NO VALUE READERS, because S6 changes prose only and no code compares, counts or
    derives from a docstring or a spec sentence. The row shape itself is read by the helper's
    unpacking and its calls in `tools/govkit/matrix.py`. Unit 11 widened that reading, not this
    unit, and a three-element row still reads because the fourth element is optional, so no
    caller moves.
- **S7** — id 7, L5. Every label unit 11's key rule records in `check_outcome_probes` opens
  `outcome probe keys: `, its liveness label included. So exactly two labels open `lexicon `.
  Observed by AC7.
- **S8** — id 8, M1. The grounding lens's reading of S1's defect, citing the wrap at spec 8 lines
  352-353. Closed by S1's joined reading. Observed by AC1.
- **S9** — id 9, L6. Unit 10 AC3's counter half is observed as the expansions `${n:-` and `${fail:-`
  on the `FOREIGN_PREFIX_PROBE:-0` line of `tools/roles/adopt-roles.test.sh`, never as the letters.
  Spec 10's revision line names this unit's AC8. Observed by AC8.
- **S10** — id 10, L7. The agreement rule's union by `want` is observed on a staged descriptor whose
  two `ok = true` blocks name one path, one under `must_exist` and one under `must_not_resolve`.
  Where the reading shows the rule still reading the typed pair, this pass makes `derive_probe_paths`
  union every key `govkit.OUTCOME_PROBE_KEYS` maps to `want`, as spec 11 S4 states. Spec 11's
  revision line names this unit's AC9. Observed by AC9.
- **S11** — id 11, L8. Spec 11 §4 "Order, and unit 7" stops describing the README edit as pending.
  Its second paragraph points at `README.md`'s Build-level rules, which already say that units 10
  and 11 follow 7, and at the derived build-order region, which already holds step 7. Observed by
  AC10.
- **S12** — id 12, L9. Spec 10 §4's prefix-`.` sentence states its condition. The parent-home term
  reads absent unless that directory holds `hooks/agent-cap.js`, and there the stop is refused where
  unit 9 accepted it, which fails closed. Spec 11 §5 security states that the resolver's containment
  covers receipt rows only (`tools/govkit/govkit.py:222`). Its static second probe and unit 10's
  parent-home term may both leave the tree. Observed by AC11.
- **S13** — id 13, L10. CONFIGURE's `subprocess.run` in `_cmd_apply`, the one unit 11 binds as
  `_cfg_run`, gains `encoding="utf-8", errors="replace"`. The row `tools/govkit/govkit.py subprocess 36`
  in `memory/project/encoding-posture-sites.txt` falls to 35 in the same commit. Spec 11 §4's sentence
  that the count stays 36 is corrected. Observed by AC12.
- **S14** — id 14, L11. Unit 10 S5's claim over all six registry classes of
  `tools/run-gates/run-gates.test.sh` is observed through the spawn leg's own scan, counter and
  comparator, `pure-fn-subst` included. Spec 10's revision line names this unit's AC13. Observed by
  AC13.
- **S15** — id 15, L12. Spec 10 §4's reader inventory names the accepted-stops class rule in
  `check_outcome_probes` as a third reader, which reads `must_exist` alone and which unit 10 leaves
  untouched. It cites the `git grep` that produced the inventory. Observed by AC14.
- **S16** — id 16, L13. Unit 10 AC12's unit-5 half is observed through the same leg seams as S14.
  Spec 10 §10 names `build_spawn_measured`, `read_registry` and `check_registry` beside
  `scan_spawn_file`. Observed by AC13 and AC14.
- **S17** — id 17, M3. Fixture B of the `[dRB-11]` block gets its old-vintage agent-cap row through
  `write_vintage_receipt` (`tools/govkit/selftest.py:617-673`), and never derives an identity itself.
  Spec 11 §4 "The witnessing arms" names the helper. Spec 11's revision line states that AC4's
  "Before the commit" was inexact, because `stale_target` has already settled, and names this unit's
  AC15. Observed by AC15.
- **S18** — id 18, M4. The parent-home row of settings-merge's `check_outcome_states` call takes its
  path from `govkit.resolve_prefix_token` (`tools/govkit/govkit.py:179-190`), never from a hand
  `.replace` of the token. Spec 10 §4's matrix-row paragraph says so, and spec 10's §7 leg line names
  `python resolver (behaviour + inline parity + idiom ban)`. Observed by AC16 and AC17.
- **S19** — id 19, L14. Spec 10's §7 leg line names `spec tokens (a spec's own names resolve)` and
  `encoding posture (text IO names its encoding)`. Observed by AC17.
- **S20** — id 20, L15. Spec 11's §4 Files touched lists `memory/builds/dRedressedBar/build/`, and its
  §7 leg line names `recall floor` and `memory hygiene`. Observed by AC18.
- **S21** — id 21, L8. The blast-radius lens's reading of S11's defect. Closed by S11's pointer.
  Observed by AC10.
- **S22** — id 22, L16. The comment directly above settings-merge's `[[outcome]]` block in
  `tools/govkit/entries/settings-merge.kit.toml` states the probe as it stands after units 10 and 11.
  It names the two static `must_not_exist` homes, and the `must_not_resolve` term with its receipt
  reading. Observed by AC19.
- **S24** — id 24, L17. Spec 11 §5 security is restated over the class. The tail S3 prints is the
  verbatim stderr of whichever adopter CONFIGURE or the gained loop refuses, so its producers are
  every shipped descriptor's `[adopt].argv`. It names the grep that read those adopters' `>&2` lines,
  and what they print. Observed by AC20.
- **S25** — The record. Specs 9, 10 and 11 each take ONE rev bump in this pass, and each revision
  line names every report id §4's table assigns that spec. Every reading above goes to this unit's
  acceptance ledger under `memory/builds/dRedressedBar/build/`, carrying
  `**Serves:** journal TOOL-dRedressedBar-13`. Observed by AC21.

## 3. Non-goals (OUT)

- Rewriting a faulted criterion of spec 10 or 11. Each was built against its §6 as written. Its
  revision line states which half did not hold and names the criterion here that observes the
  corrected form. Prose stating a false fact is corrected in place, as unit 10 did for specs 1 to 9.
- Re-running unit 10's, 11's or 12's build, or re-observing a criterion the audit did not fault.
- The report's left-shift proposals: the spec-lint checks and the new checklist entries. Each is its
  own mechanism, and none is needed to close these 23 findings. The classes the report names that
  already exist under `memory/gotchas/` stay as they are.
- No change to the regenerate site's or the gained loop's decoding. Both already pass
  `encoding="utf-8"` (`tools/govkit/govkit.py:10986-10987`, `:11119-11120`).
- No module-level function or class minted, and no kit version moved. Every product file sits under
  `{prefix}/govkit`, which the registry exempts, so `memory/map/generated/symbols.json` stays as unit
  7 regenerates it and unit 7 need not follow.
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-10` — its built pass and its spec. S18 reads its parent-home
  row in `check_outcome_probes`, and S22 reads its two-term code-2 block. AC1 to AC4 and AC13 read its
  pass commit `<p10>`. S2, S5, S12, S15, S16, S18 and S19 correct its §1, §3, §4, §5, §7 and §10.
  Units 1, 4, 5, 8 and 9 are reached through this edge, because unit 10 consumes each and this unit
  lands after it. AC1, AC3, AC4, AC8 and AC13 read their built files or specs, and S6 corrects spec
  9's row-shape sentence.
- **consumes-from** `TOOL-dRedressedBar-11` — its built pass and its spec. S6 reads its fourth row
  element of `check_outcome_states`, and S7 reads its key rule. S10 reads its `derive_probe_paths`,
  S13 its `_cfg_run` call, and S17 its `[dRB-11]` fixture B. S22 reads its `must_not_resolve` term.
  S11, S12, S13, S17, S20 and S24 correct its §4, §5 and §7. Without it there is no key rule to
  label, no fourth element to document and no fixture B to rebuild.
- **consumes-from** `TOOL-dRedressedBar-12` — the tree it leaves. Spec 11 is at unit 12's rev bump,
  which this unit's bump of spec 11 follows. The `[dRB-11]` block holds fixture A's third run, beside
  which S17 rebuilds fixture B. `_cmd_apply` holds unit 12's receipt carry, in which S13 changes the
  CONFIGURE call. Both units write `tools/govkit/govkit.py`, `tools/govkit/selftest.py` and spec 11, so this
  unit follows it.
- **hands-off** `TOOL-dRedressedBar-17` — fixture B of the `[dRB-11]` block as S17 rebuilds it. AC15's
  spelling ban spans fixture A too (report id 3), so that unit brackets fixture B with markers and
  observes its identities by behaviour. Also this spec's §1 ordering sentence (report id 6), its §5,
  §3 and §10 decode-site prose (report id 8), and the mirror of the edge spec 14 gains to this unit
  (report id 5), each corrected in place by that unit.

## 4. Design

### Evidence, read at `29c72f51` on 2026-10-14

`29c72f51`'s `tools/` equals `ebce889c`'s (`git diff --stat ebce889c7 HEAD -- tools skills` prints
nothing). Specs 10 and 11 were read at the blobs the report pins, `5b0dba25` and `1b4ea08c`.

- `sed -n '/^## 6. Gates/,/^## 7/p'` over spec 8 then `grep -c 'reads none of this file'` prints 0.
  The same cut joined with `tr '\n' ' ' | tr -s ' '` prints 1.
- Spec 9's Gates section, cut with `sed -n '/^## 7. Gates/,/^## 8/p'`, holds no
  `codebase-map coverage + freshness`.
- Spec 4's non-goal list, cut with `sed -n '/^## 3. Non-goals/,/^### Edges/p'`, holds no
  `project-owned`. The one hit in spec 4 is line 56, its hands-off to unit 7.
- `tools/agent-instructions/adopt-agent-instructions.test.sh:19`, the line unit 1 copies, reads
  `${fail:-0}` and `${pass:-1}`. Spec 1 S5 renames the counters to `fail` and `n`.
- The spawn leg runs `sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  (`tools/gate-legs.json:187-195`). Its body is `scan_spawn_tree`, `build_spawn_measured`,
  `read_registry` with `SPAWN_KEY_SHAPE`, and `check_registry` (`tools/gate-lint/sh_hygiene.py:894-935`).
  Run read-only and restricted to named files, that chain measures `run-gates.test.sh` at cat-file
  25, date-fmt 1, path-subst 12, printf-subst 2, pure-fn-subst 11 and var-pipe 141, with 0 problems
  against the registry. Over the five unit-5 files it reports 10 problems: eight undeclared rows in
  the four files unit 5 converts, and `unattended-build.test.sh` at printf-subst 71 against 66 and
  var-pipe 70 against 62.
- `classify_outcome` tests `(target / resolved).exists()` with no containment
  (`tools/govkit/govkit.py:6313-6324`). `resolve_kit_dir` applies containment to receipt rows only
  (`:222`), and probes `here / home` and `here.parent / home` with none.
- `git grep -n 'must_exist\|must_not_exist' -- 'tools/*.py'` finds, outside `classify_outcome` and
  `derive_probe_paths`, the accepted-stops class rule at `tools/govkit/matrix.py:181-185`.
- CONFIGURE runs `subprocess.run(..., capture_output=True, text=True)` with no encoding
  (`tools/govkit/govkit.py:7744`). The regenerate site and the gained loop pass `encoding="utf-8"`.
  The registry row for `govkit.py`'s subprocess arm is 36.
- `README.md:56-60` already says that units 10 and 11 follow 7 and touch only govkit-exempt files.
  The build-order region already lists step 7.
- The adopters' stderr lines, read with
  `git ls-files 'tools/*adopt-*.sh' 'tools/playbook/adopt-playbook.sh' | grep -v test | xargs grep -h '>&2'`,
  expand paths, exit codes and kit names (`$KIT_REL`, `$TARGET`, `$rc`, `$FIXTURE_REL` and the like).
  None expands a credential.

### Two choices, derived

**Id 2 takes the report's second fix.** When this unit builds, unit 10 is CLOSED. M6 does not let a
pass follow a red check, so unit 10 closed with its AC9 green. AC9 reads all of spec 7 for
`units 1 to 6`, so spec 7's AC4 is already edited on disk. The first fix would revert that edit, and
then unit 10's AC9 reading would answer text that no longer exists. That is the contradiction both
fixes exist to remove. So the second fix is the one consistent with the tree, and S2 states why
unit 7's ledger still holds.

**Id 13 decodes as UTF-8, and replaces what it cannot decode.** The two sibling sites that refuse or
print an adopter's exit already decode UTF-8, so CONFIGURE is the outlier, and the fix is the one
answer. `errors="replace"` follows the F4 comment (`tools/govkit/govkit.py:7634-7637`). CONFIGURE
runs after the bytes are landed and before the receipt is written, so a decode error raised there is
the half-install state that comment says the verb avoids. The report's other two options keep the
outlier. One states it, and the other only observes it under `PYTHONUTF8=0`.

### What this unit corrects in each spec

| Spec | Ids | What moves |
|---|---|---|
| 9 | 6 | §4, the `check_outcome_states` row-shape sentence |
| 10 | 1, 2, 3, 4, 5, 8, 9, 12, 14, 15, 16, 18, 19 | §1 count; §3 first non-goal; §4 prefix-`.` sentence, reader inventory, matrix-row paragraph and Alternatives row 2; §5 risks; §7 leg line; §10 seams. Its revision line names AC1, AC3, AC4, AC8 and AC13 |
| 11 | 6, 7, 10, 11, 12, 13, 17, 20, 21, 22, 24 | §4 "The refused exit names its reason", "Order, and unit 7", "The witnessing arms" and Files touched; §5 security; §7 leg line. Its revision line names AC6, AC7, AC9 and AC15 |

### The code sites

| Id | File | Change |
|---|---|---|
| 6 | `tools/govkit/matrix.py` | `check_outcome_states`'s docstring states the fourth element |
| 7 | `tools/govkit/matrix.py` | the key rule's labels open `outcome probe keys: ` |
| 10 | `tools/govkit/matrix.py` | only where AC9 reads the typed pair: `derive_probe_paths` reads keys by `want` |
| 13 | `tools/govkit/govkit.py`, `memory/project/encoding-posture-sites.txt` | the `_cfg_run` call decodes UTF-8 with replacement; the row falls to 35 |
| 17 | `tools/govkit/selftest.py` | fixture B appends the agent-cap row and calls `write_vintage_receipt(govroot, t, OLD)` before `settle` |
| 18 | `tools/govkit/matrix.py` | the parent-home row's path through `govkit.resolve_prefix_token` |
| 22 | `tools/govkit/entries/settings-merge.kit.toml` | the block comment states the three terms |

Fixture B, in order: `stale_target` with `[kit.agent-cap] prefix = "scripts"` in its deploy. Then
`scripts/hooks/` is created, and one row is appended to the receipt's `files`. That row has path
`scripts/hooks/agent-cap.js`, kit `agent-cap`, role `engine`, and the source `resolve_entry` gives,
and `agent-cap` joins the receipt's `kits`. Then `write_vintage_receipt(govroot, t, OLD)` runs. It
writes the hook's bytes at `OLD` and sets the row's `commit`, `sha256` and `gov_oid`, and it re-sets
the rows already at `OLD` to the same values, so it is idempotent over them. Then `{` goes to
`.claude/settings.json`, and `settle` runs. `git cat-file -e 24f39915:tools/hooks/agent-cap.js`
succeeds, so the helper keeps the row rather than dropping it. Its `git` calls are inside the helper,
so the block adds no counted site.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/matrix.py`
- `tools/govkit/selftest.py`
- `tools/govkit/entries/settings-merge.kit.toml`
- `memory/project/encoding-posture-sites.txt`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md`
- `memory/builds/dRedressedBar/build/`

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Fold each fix into specs 10 and 11 now, before they build | M4 forbids folding at a CONVERGED exit (owner, SPEC 2026-10-05) | Refused by the method |
| Two batch units, one per spec | S7 and S10 write `tools/govkit/matrix.py` for spec 11, and S18 writes it for spec 10, so the two write sets intersect (M6 clause 1) | Rejected |
| Rewrite each faulted criterion in place after its unit closes | That unit's ledger answered the criterion as written, and a rewrite leaves the ledger answering text that no longer exists | Rejected; the revision line points here |
| Id 2 by the report's first fix | It reverts an edit unit 10's AC9 reading depends on (§4, "Two choices") | Rejected |
| Id 13 by a stated host dependency, or a `PYTHONUTF8=0` run | Each keeps CONFIGURE the one adopter site that decodes by host codepage | Rejected |

## 5. Production-readiness checklist

- security — S13 narrows a failure mode: CONFIGURE's decode can no longer raise on an adopter's
  bytes. S24 states the class the tail already reaches. The adopters' stderr is their own output,
  printed to the operator who ran the verb, and the measured lines carry paths, codes and kit names.
- perf / scale — N/A — two docstrings, one keyword pair, one label prefix, one comment and one
  fixture reshaped.
- error / empty / loading states — A non-UTF-8 byte in an adopter's stderr now prints as U+FFFD in
  the tail instead of raising mid-install.
- observability — The key rule's labels read as their own rule in the matrix output.
- risks — `errors="replace"` diverges from the two sibling sites, which decode strictly; those sites
  are not this unit's (§3). A label prefix change moves no check count, so no floor moves.
- testing — AC1 to AC21 are greps over specs and source, in-process python probes, and fixture B
  through the selftest helper. The two moved arms are declared in §7.
- migration — N/A — no receipt, conf or deploy field moves.
- user docs — N/A — `help/` holds no govkit page.

## 6. Acceptance criteria

`<pN>` is the commit of unit N's build pass, as unit N's acceptance ledger names it. Every command runs
from the worktree root. "Joined" means piped through `tr '\n' ' ' | tr -s ' '`. `<sN>` is
`memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-N.md`.

- **AC1** — When `sed -n '/^## 6. Gates/,/^## 7/p' <s8>`, joined, is searched with
  `grep -c 'reads none of this file'` at the tip, it prints 0. The same joined cut carries
  `scan_spawn_tree`. The same command over `git show 29c72f51:<s8>` prints 1.
  Red when: the false sentence stands at the tip, or the reading over `29c72f51` prints 0 and so
  cannot fail.
  figure: 1 at `29c72f51`, PINNED 2026-10-14.
- **AC2** — When spec 10's §5 is cut with `sed -n '/^## 5. Production/,/^## 6/p'`, joined, and searched
  with `grep -c 'no criterion text moves'`, it prints 0. Its §3, cut with
  `sed -n '/^## 3. Non-goals/,/^### Edges/p'` and joined, carries `single criterion` and `AC4`.
  `grep -n 'units 1 to 6' <s7>` prints nothing at the tip.
  Red when: §5 still says no criterion text moves, as at the audited blob `5b0dba25`, where the
  count reads 1.
- **AC3** — When `sed -n '/^## 7. Gates/,/^## 8/p' <s9> | grep -c 'codebase-map coverage + freshness'`
  runs at the tip, it prints at least 1.
  Red when: it prints 0, as over `git show 29c72f51:<s9>`.
- **AC4** — When `sed -n '/^## 3. Non-goals/,/^### Edges/p' <s4> | grep -n 'project-owned'` runs at the
  tip, it prints the corrected non-goal citing `tools/roles/kit.toml:47-48`.
  Red when: it prints nothing, as over `git show 29c72f51:<s4>`.
- **AC5** — When spec 10's §1 is cut with `sed -n '/^## 1. Goal/,/^## 2/p'`, `grep -c 'eight specs'`
  prints 0 and `grep -c 'nine specs'` prints 1.
  Red when: the miscount stands, as at `5b0dba25`.
- **AC6** — When a python program reads `tools/govkit/matrix.py` with `ast.parse` and prints
  `ast.get_docstring` of the `check_outcome_states` function, the text carries `fourth`. Spec 9's §4,
  cut with `sed -n '/^## 4. Design/,/^## 5/p'` and joined, carries `optional fourth`.
  Red when: either still states three elements alone. Spec 9's half prints 0 at `29c72f51`.
- **AC7** — When a python program imports `tools/govkit/matrix.py`, replaces its module-level
  `check` with a recorder, and calls `check_outcome_probes` on a scratch directory, every label
  unit 11's key rule records opens `outcome probe keys: `. Their count is the `[[outcome]]` block
  count `read_descriptors` gives, plus one liveness label. Exactly two labels open `lexicon `:
  `lexicon exit 1 after a failed first scaffold is REFUSED` and
  `lexicon exit 1 after a declaration removed after one is ACCEPTED`.
  Red when: a key-rule label opens `lexicon ` or carries no prefix. In a scratch copy of
  `matrix.py` with one key-rule label respelled to open `lexicon `, three labels open it.
  figure: the block count is DERIVED at observation; the two lexicon labels are PINNED from
  `tools/govkit/matrix.py:240` at `ebce889c`.
- **AC8** — When `grep -F 'FOREIGN_PREFIX_PROBE:-0' tools/roles/adopt-roles.test.sh` runs at the tip,
  it prints one line. Piped on, `grep -cF '${n:-'` prints 1, `grep -cF '${fail:-'` prints 1, and
  `grep -cF '${pass'` prints 0. In a scratch copy with `${n:-` respelled `${count:-`, the first of
  the three prints 0.
  Red when: the stop reads a counter the suite does not keep.
- **AC9** — When AC7's program runs with `govkit.read_descriptors` wrapped, settings-merge's
  `outcome` is replaced by two `ok = true` blocks. One is code 2, means `staged-a`, with
  `must_exist = "{prefix}/settings-merge.py"` and `must_not_resolve = "{prefix}/hooks/agent-cap.js"`.
  The other is code 3, means `staged-b`, with `must_exist = "{prefix}/hooks/agent-cap.js"`. The label
  `accepted stops: 'settings-merge' 'staged-a' and 'staged-b' agree about every path they both name`
  then records false. The program reads the recorded labels whether `check_outcome_probes` returns
  or raises after that rule.
  Red when: that label records true, because the rule still reads the typed `must_exist` and
  `must_not_exist` pair.
- **AC10** — When `grep -c 'The dispatcher owns that README edit' <s11>` and
  `grep -c 'has been inexact since' <s11>` run at the tip, each prints 0. Spec 11's
  "Order, and unit 7" sub-section, cut with `sed -n '/^### Order, and unit 7/,/^### The witnessing/p'`,
  carries `README.md`.
  Red when: the pending edit is still described, as at `1b4ea08c`, where each count reads 1 and the
  cut carries no `README.md`.
- **AC11** — When spec 10's §4 is cut with `sed -n '/^## 4. Design/,/^## 5/p'` and joined, it carries
  `unless that directory holds`. Spec 11's §5, cut with `sed -n '/^## 5. Production/,/^## 6/p'` and
  joined, carries `receipt rows only`.
  Red when: either prints nothing, as at `5b0dba25` and `1b4ea08c`.
- **AC12** — When a python program parses `tools/govkit/govkit.py` with `ast` and finds the
  assignment to `_cfg_run` in `_cmd_apply`, its `subprocess.run` call carries `encoding="utf-8"` and
  `errors="replace"`. A program that runs `scan_text_io` from `tools/gate-lint/encoding_posture.py`
  over `tools/govkit/govkit.py` counts 35 subprocess sites. `memory/project/encoding-posture-sites.txt`
  declares 35 for that row. Spec 11's §4, cut and joined, carries no `stays 36`.
  Red when: the call keeps `text=True` with no encoding and the scan counts 36, as at `<p12>`.
  figure: 36 at `29c72f51`, PINNED 2026-10-14; 35 is that minus the one site this pass encodes.
- **AC13** — A python program imports `tools/gate-lint/sh_hygiene.py` and calls
  `scan_spawn_tree(pathlib.Path("."), [":!*.test.sh", ":!memory/"])`. It passes the result through
  `build_spawn_measured`, reads `memory/project/spawn-idiom-sites.txt` through `read_registry` with
  `SPAWN_KEY_SHAPE`, and restricts both to a file set. When it calls `check_registry` at the tip, it
  returns no problem for `tools/run-gates/run-gates.test.sh`, over all six classes. It returns no
  problem for `tools/branch-reconcile/adopt-branch-reconcile.sh`, `tools/roles/adopt-roles.sh`,
  `tools/roles/adopt-roles.test.sh`, `tools/hooks/format-guard.test.sh` and
  `tools/workflows/unattended-build.test.sh`. `git diff <p8>~1 <p8> -- memory/project/spawn-idiom-sites.txt`
  prints nothing.
  Red when: unit 8's pass added a counted site, or a unit-5 file keeps one, and `check_registry`
  names it.
  figure: over the five unit-5 files at `29c72f51` the program returns 10 problems, PINNED
  2026-10-14 as the red case. The rows are DERIVED from the registry at observation.
- **AC14** — When `grep -c 'outside those two' <s10>` runs at the tip, it prints 0. Spec 10's §4, cut
  and joined, carries `accepted-stops class rule`. Its §10, cut with `sed -n '/^## 10. Reuse/,$p'`,
  carries `build_spawn_measured`, `read_registry` and `check_registry`.
  Red when: the two-reader sentence stands, or §10 names `scan_spawn_file` alone, as at `5b0dba25`.
- **AC15** — When a python program reads `tools/govkit/selftest.py` from the first to the last line
  carrying `[dRB-11]`, the span calls `write_vintage_receipt(` at least once. It carries no `_sha(`, no
  `blob_oid(` and no `"git", "show"`. `scan_text_io` over the file counts, per arm, the registry's
  rows for it.
  Red when: the block derives an identity itself.
  figure: 24 subprocess and 1 file-io, PINNED 2026-10-14 at `29c72f51`; DERIVED from the registry at
  observation.
- **AC16** — When `git grep -nE "\.replace\([\"'][{]prefix[}]" -- tools/govkit/matrix.py` runs at the
  tip, it prints nothing. `inspect.getsource` of `check_outcome_probes` carries
  `resolve_prefix_token(`, and AC7's recorder reads the parent-home row's label true.
  Red when: the row's path is a hand replacement of the token. In a scratch copy so respelled, the
  same `grep -nE` prints that line.
- **AC17** — When spec 10's Gates section is cut with `sed -n '/^## 7. Gates/,/^## 8/p'`, its leg line
  names `python resolver (behaviour + inline parity + idiom ban)`,
  `spec tokens (a spec's own names resolve)` and `encoding posture (text IO names its encoding)`.
  Red when: any of the three is absent, as at `5b0dba25`, where none is named.
- **AC18** — When spec 11's Files touched is cut with `sed -n '/^### Files touched/,/^### Alternatives/p'`,
  it lists `memory/builds/dRedressedBar/build/`. Its Gates section's leg line carries
  `` `recall floor` `` and `` `memory hygiene` ``, read with `grep -cF`.
  Red when: either is absent, as at `1b4ea08c`, where the build path and `` `recall floor` `` read 0.
- **AC19** — When a python program reads `tools/govkit/entries/settings-merge.kit.toml` and takes the
  contiguous `#` lines directly above its `[[outcome]]` line, they carry `must_not_resolve` and
  `receipt`.
  Red when: the comment still describes the single term unit 9 shipped.
- **AC20** — When spec 11's §5 is cut and joined, it carries `[adopt].argv` and the grep §4 names for
  the adopters' `>&2` lines.
  Red when: §5 reasons over settings-merge's stderr alone, as at `1b4ea08c`.
- **AC21** — When `git diff <p13>~1 <p13> -- memory/builds/dRedressedBar/spec/` runs, specs 9, 10 and
  11 each show one header rev change and one new revision line. Each line names every report id §4's
  table assigns that spec. The ledger S25 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-13`.
  Red when: a spec takes no bump, two bumps, or a revision line missing one of its ids.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `python resolver (behaviour + inline parity + idiom ban)` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/matrix.py · covers AC7 AC9 · a key-rule label respelled to open `lexicon `, and settings-merge patched to two ok blocks naming one path under `must_exist` and `must_not_resolve` · none
New arm: tools/govkit/selftest.py · covers AC15 · fixture B with the `write_vintage_receipt` call removed after the row is appended, so the row's identities and bytes disagree and `update` refuses before the adopter runs · none

The refusal join's floor does not move, because no refusal branch is added or removed. The main loop
observes both moved arms red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the units-10-11 spec audit.
  All 23 confirmed medium and low findings, by report id, are batched into this unit by M4. Each
  claim was re-read at `29c72f51` and at the blobs the report pins.
- rev-2 · 2026-10-14 · S6 gains a `**Readers:**` clause, because the pre-commit gate's hygiene check
  25 refused rev-1 for it. By name it lists spec 9's line 200 and `tools/govkit/matrix.py`, both
  found by `git grep` over the tracked tree and both already in §4's Files touched. By value it
  answers NO VALUE READERS, because S6 changes prose only. No other section moves.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-17`, the batch the
  units-12-15 spec audit's minors were promoted into, for report ids 3, 5, 6 and 8. No scope, design
  or criterion moves.
- rev-4 · 2026-10-14 · S3 · the correction unit 2's builder divergence carried here
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md`). S3 no longer describes spec 9's
  leg as deferring the map to unit 7's regen: spec 9's rev-4 has its own pass regenerate and commit
  `symbols.json`. AC3 and every other item stand as written.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count spawn idiom sites per class and compare them with
the registry rows"` ranked name-stem matches (`rows`, `counts`, `load_registry`) and none of the
spawn leg's functions. That is a miss, recorded as one. The seams extended were found by reading
`tools/gate-lint/sh_hygiene.py` at the report's citation. They are the leg's own chain:
`scan_spawn_tree`, `build_spawn_measured`, `read_registry` and `check_registry`
(`tools/gate-lint/sh_hygiene.py:384`, `:444`, `:843-879`). AC13 calls them read-only and never as the
gate. The selftest's `write_vintage_receipt` (`tools/govkit/selftest.py:617-673`) is reused for
fixture B. The marked canonical `resolve_prefix_token` (`tools/govkit/govkit.py:179-190`) is reused
for the matrix row. The two sibling decode sites (`:10986-10987`, `:11119-11120`) give CONFIGURE its
encoding. No code is minted. The gotchas checklist for the five product paths selected
`fixture-passes-by-finding-nothing`, which is why each criterion names the pinned blob where its red
half reads. It selected `a-folded-field-leaves-its-row-shape-docs-behind`, the class of id 6, and
`fixture-inherits-ambient-machine-state`, the class of id 13. It also selected
`verdict-printed-before-the-step-that-reverts-it`, which is unit 12's.

The recall probe returned `TOOL-aEvidencedLens-20` and `TOOL-dRedressedBar-10`, the precedent minors
batches. Each observed a built unit's criteria in a corrected form and corrected prose with one rev
bump per spec, and this unit takes their shape. The report and the code agree on every citation
re-read, with one exception: the containment line the report cites as `govkit.py:219` is `:222`.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit's batch of minor
findings observed after the faulted units are built" --terms "spec-audit minors batch promoted unit
criterion cannot red joined grep observation rev bump ledger"`
