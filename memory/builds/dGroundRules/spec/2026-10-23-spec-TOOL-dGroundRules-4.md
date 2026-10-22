# TOOL-dGroundRules-4 — an invalid policy file read as `policy-file.on-invalid` says, never as defaults

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2

**Carries:** cl-dClosedLoop-0010@cd629be7 whole
**Carries:** node:policy-key.policy-file.on-invalid

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |

<!-- /gen:spec-records -->

## 1. Goal

A policy file that does not parse, or sets a value outside its key's allowed set, must never read
the catalogue defaults, because a default is looser than an owner's stricter choice (the design
audit's H6). This unit adds `validate(text)` to `tools/policy/policy.py` and the branch `resolve`
takes when the file at the revision it reads is invalid: by default the last valid landed revision,
with the reason recorded, and with none, a refusal naming the line, which the push and landing gates
carry. `policy-file.on-invalid` chooses between `last-valid` and `refuse`, and is itself read from
the last valid revision whenever the current file is invalid.

## 2. Scope (IN)

- **S1** — `validate(text) -> list[Problem]`, `Problem` a named tuple `(line, key, why)`. An empty list
  is a valid file. Text that is not TOML is one problem: the decoder's line, key `""`, its message.
  Text that parses yields one problem per leaf whose value its catalogue row does not admit, at the
  line that assigns it, and one per leaf no catalogue row names (§8 F6). Observed by AC1, AC11.
- **S2** — `validate` judges each leaf with `check_value(row, value)`, `TOOL-dGroundRules-1`'s, which
  owns the `allowed` grammar, the empty-set rule and every typed range, and finds each leaf's row with
  `read_catalogue_row`. This unit adds no value judgement of its own, and re-points unit 1's
  `arm_schema` through `validate`, so one function judges a policy file (§8 F3).
  Observed by AC1, AC6, AC11.
- **S3** — `derive_key_line(text, path)` returns the 1-based line assigning a key path, reading each
  table header and each assignment's key with `parse_key`; `0` where the key sits in an inline table.
  Observed by AC1, AC6.
- **S4** — `read_last_valid(repo, sha)` returns the newest revision on `sha`'s first-parent history
  whose policy file is present and valid, with its parsed table, or `None`. It walks
  `git rev-list --first-parent <sha> -- .governance/policy.toml` and reads each commit's text through
  `read_policy_text`. A revision where the file is absent is not a valid one (§8 F5).
  Observed by AC3, AC4, AC7.
- **S5** — The invalid branch, `read_last_valid_value`, taken by `resolve` whenever `validate` returns
  a problem for the text at the revision it reads; `resolve` calls `parse_policy` on valid text only.
  It reads `policy-file.on-invalid` from the last valid revision by `RESOLUTION_ORDER`, so a value
  that revision does not set is the default `last-valid`. With no valid revision, or with `refuse`,
  it raises a `Refusal` at the first problem's line. With `last-valid`, it runs `RESOLUTION_ORDER`
  over that revision's table for the requested key and returns its value with source `last-valid`
  and a reason naming the invalid sha, the line, the problem and the valid sha. The whole file falls
  back, never one key (§8 F4). Observed by AC2, AC3, AC4, AC5, AC6, AC7, AC8.
- **S6** — The parse refusal `TOOL-dGroundRules-2` left in `resolve` is removed; S5 answers it.
  An absent file is not invalid and keeps `TOOL-dGroundRules-3`'s default with its reason.
  Observed by AC2, AC3.
- **S7** — The verb `python tools/policy/policy.py check [--rev <rev>]`, `cmd_check`, the revision
  defaulting to `HEAD`, the candidate a push lands. It exits 0 printing one line when the file is
  valid, absent, or invalid with a last valid revision under `last-valid`, the line naming which and
  why; and exits 2 printing the `Refusal` otherwise. Observed by AC3, AC4, AC7.
- **S8** — The push and landing gates. `arm_on_invalid`, added to `ARMS` in `check_policy.py`, runs
  the `check` verb's logic over the repository's `HEAD` and reports its refusal as a finding, so the
  `policy check` leg `TOOL-dGroundRules-1` declares refuses an invalid file with no fallback on the
  pre-push bar, which a default-branch push and every `tools/push-main.sh` landing run. This unit
  sets that leg's row in `tools/gate-legs.json` so its `guard` is absent or covers the policy file,
  and the `policy fixtures` row's argv so it carries `--strict-from` (S10). Observed by AC4, AC10.
- **S9** — Cases in `CASES` of `tools/policy/check_policy.py`, grouped as `on-invalid-classes`,
  planting each failure class the clause lists in its own temporary repository and asserting its
  stated outcome; the class with no valid revision is also red as planted under `arm_on_invalid`.
  Observed by AC2, AC3, AC4, AC5, AC6, AC7, AC8, AC11.
- **S10** — The case `on-invalid-strict`, reading v2 from the path `check_policy.py`'s new flag
  `--strict-from <path>` names; without the flag it prints `NOT RUN` with the reason, never a pass,
  and the leg always passes it. Its population is derived (§4): every key whose `strict` cell in
  v2's `[presets]` table parses, against its catalogue row, to an admitted value that differs from
  the row's default. It plants a valid revision setting each such key at that value and a malformed
  revision after it, and reads every key at the malformed one. Observed by AC9.
- **S11** — `.lexicon.conf`'s `VERB_OFFENDER_PIN` moves by the one definition this unit adds outside
  the verb table, `validate` (§8 F2), read off `python tools/lexicon/lexicon.py` and argued beside the
  key. NOT OBSERVED by a criterion here: the `lexicon naming predicates` leg reads the pin at the
  close, and this pass runs no gate.
- **S12** — A paragraph on `help/policy.md`: what an invalid file reads, the two values of
  `policy-file.on-invalid`, and the `check` verb. Observed by AC12.

## 3. Non-goals (OUT)

- The mirror's stale or absent case: unit 5 reads it as `policy-file.on-invalid` says, through this
  unit's branch.
- Presets. The strict plant sets each key explicitly; a file naming `strict` is dKeptSession's case
  (FM9 of the audit fold's closing review).
- Editing `.githooks/pre-push` or `tools/push-main.sh`. Both gates already run the bar, and the leg
  is how the refusal reaches them (§8 F8).
- Validating anything but `.governance/policy.toml`; the instruction and deploy manifests are unit
  6's to guard and other builds' to read.
- The catalogue's rows, its `empty` field and its shape audit: `TOOL-dGroundRules-1`'s.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — `check_value` and the catalogue rows it reads, `arm_schema`, `check_policy.py`'s `ARMS`, `CASES` and `--fixture` mode, and the `policy check` and `policy fixtures` legs
- **consumes-from** `TOOL-dGroundRules-2` — `resolve`, `read_policy_text`, `parse_policy`, `parse_key`, `Refusal`, and the parse refusal this unit replaces
- **consumes-from** `TOOL-dGroundRules-3` — `RESOLUTION_ORDER`, run over the last valid revision's table

## 4. Design

### Evidence

- The owner's AF-2: "Read the last valid landed revision and record why; with none, the push and
  landing gates refuse and name the line. A stale or absent mirror falls back to the TOML reader. An
  absent file still reads defaults (RC-1)."
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:14`).
- The catalogue row: `policy-file.on-invalid`, values `last-valid` and `refuse`, default
  `last-valid`, "the key is read from the last valid landed revision whenever the current file is
  invalid, and an out-of-set value of it counts as malformed"
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1153`).
- H6 named the failure classes and the guard-bearing arm
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md:100-110`);
  FM2 added the refuse-then-malformed plant and FM9 restated the arm over explicitly set keys
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-audit-fold-closing.md:90-100`,
  `:174-185`).
- The pre-push hook runs the full bar on a default-branch push and blocks it on a red
  (`.githooks/pre-push:1-3`), and the bar may scope a leg out by its `guard` on any run
  (`tools/run-gates/run-gates.sh:408-419`). A leg whose guard misses the policy file would skip a
  policy-only push.
- Python 3.14's `tomllib.TOMLDecodeError` carries `lineno`; on 3.11 to 3.13 the line is in the
  message as `at line <n>`. `derive_key_line`'s fallback and the decoder's line both answer `0` when
  neither yields one.

### Data model

```python
Problem = namedtuple("Problem", "line key why")      # key "" for a file that is not TOML

validate("[budgets]\nenforce = \"refuze\"\n")
# [Problem(line=2, key='budgets.enforce', why=<check_value's reason>)]
```

The reason a `last-valid` read records, as `--explain` prints it:

```text
policy: budgets.enforce · last-valid · .governance/policy.toml at 9f2c41aa is invalid, line 2:
'refuze' is not one of warn, refuse; read from the last valid revision 51b0e7d3: set in
.governance/policy.toml at 51b0e7d3
```

The two refusals:

```text
policy: refused · .governance/policy.toml:2 · 'refuze' is not one of warn, refuse; no valid revision of the file precedes 9f2c41aa
policy: refused · .governance/policy.toml:1 · Invalid statement (at line 1, column 7); policy-file.on-invalid is refuse at 51b0e7d3
```

### The branch, in order

1. `resolve` reads the text at the revision. `None` goes to `RESOLUTION_ORDER` as before.
2. `validate(text)`. An empty list: `parse_policy`, then `RESOLUTION_ORDER`.
3. Otherwise `read_last_valid(repo, sha)`. `None`: refuse at the first problem's line.
4. `RESOLUTION_ORDER` for `policy-file.on-invalid` over the valid table. `refuse`: refuse, naming the
   valid sha. The current file's own value of the key is never read, so an out-of-set value of it is
   one more problem and the valid revision's value governs.
5. `RESOLUTION_ORDER` for the requested key over the valid table, wrapped with source `last-valid`.

### The strict plant's population

`--strict-from` names v2, which is frozen at its packet pin. The arm reads the table under its
`## [presets]` heading whose header row opens `| Key | velocity |`, takes each row's key cell and
`strict` cell, and keeps a key when the cell, read as the key's catalogue row expects, is a value
`check_value` admits and differs from the row's `default`. Read as the row expects means: one of the
row's strings; a `, `-separated list for a set-valued row, compared as a set; a number for a typed
range. Every other row is excluded and named on every run, with why: no catalogue row, a placeholder
key such as `roles.effort.<role>`, a cell that is no value (`each cap's evidence-derived value`), a
value equal to the default, which cannot tell a fallback from a read, or a key that is a dotted
prefix of another kept key, such as `leases` beside `leases.overlap`, which no TOML file can hold
together (`TOOL-dGroundRules-1` §8 F5); of such a pair the longer key is kept. An empty population is
a red, never a pass. Measured 2026-10-23 by a parse of v2: 246 rows carry a strict cell and 119 differ
from their key's default as text, before any cell is read as a value. Both are PINNED at that date;
the arm re-derives the parsed count on every run and prints it.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `validate` | function | `tools/policy/policy.py` |
| `derive_key_line`, `read_last_valid`, `read_last_valid_value`, `cmd_check` | function | `tools/policy/policy.py` |
| `Problem` | type | `tools/policy/policy.py` |
| `check`, `--rev` | CLI verb and flag | `tools/policy/policy.py` |
| `arm_on_invalid` | arm function in `ARMS` | `tools/policy/check_policy.py` |
| `on-invalid-classes`, `on-invalid-strict` | fixture case groups in `CASES` | `tools/policy/check_policy.py` |
| `--strict-from` | CLI flag | `tools/policy/check_policy.py` |

Every function but `validate` leads with a verb `.lexicon.conf`'s `VERBS` declares (§8 F2).
`KIT_POLICY_VERSION` in `policy.py` moves with this unit.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/gate-legs.json`
- `.lexicon.conf`
- `help/policy.md`

### Alternatives rejected

- **Per-key fallback**, the current file's valid keys read and only the bad one taken from the last
  valid revision. One commit's values would then be read half from two revisions, and the clause
  says the current file is invalid, not a key (§8 F4).
- **A refusal written into `.githooks/pre-push`.** The hook ships verbatim to every push-main adopter
  and would gain a Python call and a policy kit it may not carry; the leg reaches the same push.
- **A strict table typed into the fixture.** It would be one more copy of v2's column, the
  `[derive]` rule's typed-beside-the-source shape (§8 F7).

## 5. Production-readiness checklist

- security — the change closes a fail-open: an invalid file never reads a default, and an owner's
  `refuse` survives the very malformation it exists for. The history walk reads commits only, never
  the working tree. A key no row names is a problem, so a typo cannot pass as unset.
- perf / scale — a valid file costs one more parse; an invalid one costs one `rev-list` and one
  `show` per revision walked back to the last valid one, a handful in practice.
- error / empty / loading states — absent reads defaults; invalid reads the last valid revision or
  refuses at a line; a catalogue type with no judge refuses naming the row.
- observability — the `last-valid` reason names both shas, the line and the problem; `check` prints
  one line on every push.
- risks — a long-invalid file keeps reading an old revision silently to a consumer that ignores
  `source`; `check` names it on every push, and unit 5's mirror carries the source.
- testing — AC1 to AC12; the arms under §7.
- migration — none: the file is new in this build.
- user docs — the invalid-file paragraph and the `check` verb on `help/policy.md`.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the module and the arm CLI by bare
name, `policy.py` and `check_policy.py`, and the help page as `policy.md` under `help/`, because this
run creates them and the spec-token checker grades a path-shaped token in a criterion against the
tracked set. Each fixture repository sits under `%TEMP%`, short-named. Every `get` and `check` below
reads with `--rev HEAD` at the case's newest commit, so no case rests on the landed-ref rule
`TOOL-dGroundRules-2` observes. "V" is a valid revision and "C" a later one.

- **AC1** — When a probe imports `policy.py` and calls `validate` on three texts, a `[budgets]` table
  with `enforce = "refuze"` returns one `Problem` at line 2 with key `budgets.enforce`, the same with
  `"warn"` returns `[]`, and `enforce = ` with no value returns one problem at line 2 with key `""`.
  Red when: an out-of-set value passes, or a problem names line `0` where the line is known.
- **AC2** — When `check_policy.py --fixture` reaches the `on-invalid-classes` cases and one plants
  a repository with no policy
  file, `policy.py get budgets.enforce --explain` prints `warn` with source `default`.
  Red when: an absent file refuses or reads as invalid.
- **AC3** — When a case plants V setting `budgets.enforce = "refuse"` and a malformed C,
  `policy.py get budgets.enforce --explain` prints `refuse` with source `last-valid` and a reason
  naming C's line and V's sha8, and `policy.py check` exits 0 naming the fallback.
  Red when: the malformed file reads the catalogue default `warn`.
- **AC4** — When a case plants one malformed revision and nothing before it, `policy.py get
  budgets.enforce` and `policy.py check` each exit 2 printing a line that opens `policy: refused ·`
  and names the malformed line, and `arm_on_invalid` over that repository reports one finding; over
  the same repository with the file made valid it reports none.
  Red when: either verb reads a default or exits 0, or the arm stays silent.
- **AC5** — When a case plants a valid C that does not set `runtime.agents-in-flight`,
  `policy.py get runtime.agents-in-flight --explain` prints `6` with source `default`.
  Red when: a missing key refuses or is read as invalid.
- **AC6** — When a case plants V setting `budgets.enforce = "refuse"` and C setting
  `budgets.enforce = "refuze"` and `runtime.agents-in-flight = 3`, `get budgets.enforce` prints
  `refuse` and `get runtime.agents-in-flight` prints V's reading, the default `6`, both with source
  `last-valid`.
  Red when: C's `refuze`, C's `3` or a catalogue default is read while C is invalid.
- **AC7** — When a case plants V setting `policy-file.on-invalid = "refuse"` and a malformed C,
  `policy.py get budgets.enforce` and `policy.py check` each exit 2 naming C's line and `refuse`.
  Red when: the read falls back to V or to the default, the FM2 case.
- **AC8** — When a case plants V setting `policy-file.on-invalid = "refuse"` and C setting it to
  `"never"`, every read exits 2; with V setting no value of the key and C the same, `get
  budgets.enforce` reads V's value with source `last-valid`.
  Red when: C's own value of `policy-file.on-invalid` is consulted, or C is read as valid.
- **AC9** — When `check_policy.py --fixture --strict-from
  memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` reaches the
  `on-invalid-strict` case, it prints its population count and every excluded key with its reason,
  then reads each kept key at the malformed revision and finds strict's value with source
  `last-valid`. Red when: any kept key reads its catalogue default or another value, or the
  population is empty.
  figure: the count is DERIVED from v2's table and the catalogue at observation.
  fixture: run without `--strict-from`, the case prints `NOT RUN` naming the flag, never a pass.
- **AC10** — When `python -c` loads `tools/gate-legs.json` and prints the rows named `policy check`
  and `policy fixtures`, the first's `guard` is absent or holds a pathspec covering the policy file,
  and the second's argv carries `--strict-from` and v2's path. Red when: a push changing only the
  policy file would skip the live arm under the scoped bar, or the strict case runs with no source.
- **AC11** — When a case plants a valid-looking C whose `[budgets]` table sets `enforse = "warn"`
  and a V before it, `policy.py get budgets.enforce --explain` reads V with source `last-valid` and a
  reason naming `enforse` as no catalogue key. Red when: the unknown key is ignored and C read.
- **AC12** — When `grep -n 'on-invalid'` runs over `policy.md` under `help/`, it prints the paragraph,
  and `grep -n 'policy.py check'` there prints the verb. Red when: the branch ships undocumented.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `govkit acceptance matrix` · `straggler-guard arms` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)`

The `policy check` and `policy fixtures` legs `TOOL-dGroundRules-1` declares run these arms; they
are named here rather than on the line above, because they do not exist at this spec's base.

New arm: tools/policy/check_policy.py --fixture (the `on-invalid-classes` cases) · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC11 · a fixture repository per failure class: absent, malformed after a valid revision and with none, a missing key, an out-of-set value, an unknown key, `refuse` then malformed, and an out-of-set `policy-file.on-invalid` with and without a valid value before it · none

New arm: tools/policy/check_policy.py --fixture --strict-from (the `on-invalid-strict` case) · covers AC9 · a valid revision setting each derived guard-bearing key at strict's value, then a malformed revision · none

New arm: tools/policy/check_policy.py (`arm_on_invalid` in `ARMS`) · covers AC4 · the `check` logic over `HEAD` of the repository it is given, red on a planted malformed policy file with no valid revision before it · none

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens a spec header reuses
  (`memory/HYGIENE.md:105`). Liveness: the line would print `DRAFT` if the vocabulary declared it.
  Observed 2026-10-23: it does not. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, which
  `memory/TEMPLATE-SPEC.md:62` gives as "drafting".
- **F2 — S5 of the brief spells the function `validate`, and `.lexicon.conf` declares `check` with
  "NOT `validate`".** (a) Keep `validate`, so every spec spelling S5 agrees, and move
  `VERB_OFFENDER_PIN` by one with its argument beside the key. (b) Spell it `check_policy_text` here
  and leave units 1, 5 and 6, written concurrently against S5, calling a name that does not exist
  until the spec audit reconciles them. Both build; (b) leaves an interface disagreement open across
  four specs, (a) one pinned name. Recommendation (a), fewer open questions. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F3 — The brief has `TOOL-dGroundRules-1`, order 1, call `validate`, which this unit, order 2,
  owns.** Unit 1 must see its planted empty value red before `validate` exists. (a) Unit 1's
  `check_value` is the seed: `validate` calls it per leaf, and this unit re-points unit 1's
  `arm_schema` through `validate`, as unit 1's own §8 F2 resolves. (b) Re-implement the value rules
  here. (b) is a second copy of one rule, the charter's `[reuse]` refusal. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F4 — Does an invalid file fall back whole, or per key?** v2's row reads "the key is read from the
  last valid landed revision whenever the current file is invalid". (a) Whole: any problem makes the
  revision invalid and every key reads the last valid one. (b) Per key. Rung 1: v2 answers it.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F5 — Is a revision where the file is absent a valid revision for the walk?** (a) No: the walk
  wants a present, valid file. (b) Yes, reading defaults. Under (b) a malformed first version of the
  file reads every default, the fail-open H6 closes; v2's row says a malformed file "never reads
  defaults". Rung 1: v2 answers it. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F6 — Is a key no catalogue row names a problem?** (a) Yes, an out-of-set value, since no allowed
  set admits a value for it. (b) Ignore it. Under (b) a misspelt `enforse = "refuse"` leaves
  `budgets.enforce` at its default `warn` silently. Recommendation (a), the more capable. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F7 — Where do strict's values for the plant come from?** (a) v2's `[presets]` table, read by the
  arm from the path `--strict-from` names. (b) A table typed into the fixture. (c) A `strict` field on
  each catalogue row. (b) types a copy beside its source, against `[derive]`. (c) builds presets, a
  later build's surface and a non-goal, veto 1. (a) keeps the kit free of a gov-only path, since the
  leg row names it. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F8 — How do the push and landing gates refuse?** (a) The live half of the arm in the policy leg,
  which the pre-push bar and every landing run, its guard covering the policy file. (b) A call added
  to `.githooks/pre-push` and `tools/push-main.sh`. (b) changes a hook every push-main adopter
  receives verbatim, a public-surface change no clause of this build names, veto 2. Recommendation
  (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "find the last valid revision of a file in history
when the current one does not parse"` ranked general `parse` names and `parse_conf` in
`tools/memory-tree/tree_lib.py`; none walks history for a valid revision. No existing seam fits the
walk or the branch; this unit extends `TOOL-dGroundRules-2`'s `resolve` and reads through its
`read_policy_text`, and runs `TOOL-dGroundRules-3`'s `RESOLUTION_ORDER` over the valid table rather
than a second order. `check_value` is `TOOL-dGroundRules-1`'s and is called (§8 F3).
`load_policy` in `tools/roles/roles_lib.py:373` refuses on any defect of its file with no fallback,
which the owner's AF-2 rules out here. The recall hits on FM2 and H6 agreed with their records;
FM9's text names dDeclaredLoop as the preset build where the clause names dKeptSession, and this spec
follows the clause.

Recall terms used: `python tools/memory-recall/query.py "what does a malformed policy file or an
out-of-set value read, and when does the gate refuse" --terms "on-invalid last-valid refuse malformed
out-of-set absent missing key AF-2 FM2 FM9 guard-bearing strict"`
