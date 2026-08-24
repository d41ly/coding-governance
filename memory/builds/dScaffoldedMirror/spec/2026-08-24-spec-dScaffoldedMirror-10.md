# TOOL-dScaffoldedMirror-10 — supply the vocabulary to the author

**Status:** INPROGRESS · rev-2 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams tooling

## 1. Goal

The declaration is the only half of this kit with a measured record: 136 definitions and zero
offenders since `.lexicon.conf` landed on 2026-08-16, over a window in which the gate refused
nothing. That half works by delivering context, and today it is delivered by a session happening to
open the declaration. Build the machinery that hands the table to the author instead — `--suggest`
for one name, `--brief` for one file, a rendered Skill so the whole 1,787-byte table travels and
stays bound to its source, and a charter bullet that points at that machinery instead of carrying
four copies of its rows. The failure mode this unit attacks is ABSENCE, not randomness, and the fix
for absence is supply.

## 2. Scope (IN)

- **S1** — `--suggest <name>`: one deterministic line, no corpus pass. `OK` when the identifier's
  leading token is in the declared table, otherwise a refusal naming the token. The line that names
  the REPLACEMENT and quotes the negative definition is supplied by `TOOL-dScaffoldedMirror-8`'s
  structured NOT-clause grammar, which this unit consumes and does not define. That is a NEW
  dependency edge and it is stated as new in §4.
- **S2** — `--brief <path>`: for the OBJECTS this file already names, which leading tokens are live
  across the corpus. Not a directory histogram. Bounded by the count of distinct objects in the one
  file, never by the directory's vocabulary.
- **S3** — `--brief` declares its coverage mode for the path it was handed and REFUSES on a `dark`
  extension rather than printing an empty section.
- **S4** — a rendered lexicon Skill on the `memory-recall` pattern: `tools/lexicon/SKILL.template.md`
  with `role = "rendered"`, a `to` of `.claude/skills/lexicon/SKILL.md`, a closed placeholder set, an
  `adopt-lexicon.sh --check` that re-renders and byte-diffs, one `[[lf_pin]]`, and a gate leg with NO
  guard.
- **S5** — the `§12` charter block POINTS and shrinks. The edit is net-negative in bytes in both
  `AGENTS.md` and `coding-governance-agents.template.md`, and the arithmetic is in §4.
- **S6** — the guards that keep `--brief` from becoming the mirror it resembles, built as structure
  rather than stated as intent: no exit code 1 on either verb, no pin figure in either output, no
  import edge from the brief into `scaffold_lexicon.py`, and a header on the brief saying it prints
  what the corpus does and never what it should do.
- **S7** — `tools/lexicon/LEXICON.md` gains the section on how the table reaches an author;
  `tools/lexicon/README.md` gains the two verbs, the rendered Skill and the new leg.

## 3. Non-goals (OUT)

- **No vocabulary change, no new predicate, no pin move.** This unit adds no way for the gate to
  refuse anything it does not already refuse. `--suggest` and `--brief` are authoring aids and the
  Skill is a delivery mechanism; the merge bar's verdict is byte-identical before and after, except
  for the one new wiring leg in S4.
- **No `PreToolUse` deny hook.** Killed in the research pass at 57.8% of 2,987 agent-written
  definitions denied and ~82.6% of those denials wrong, and this repo has already rejected a hook at
  59.3% wrong once. Re-opening it is a fork, not a design choice.
- **No verb table in the charter.** The declared `VERBS` block is 1,787 bytes including its
  terminating newline and `AGENTS.md` has 118 bytes of headroom. Arithmetic, not preference.
- **No directory frequency histogram.** The prototype's shape dies at adopter scale and §4 gives the
  measurement.
- **No rule change to `§12`.** This unit removes a COPY from the charter and adds a POINTER; the
  rules in that block survive verbatim. A conclusion that `§12` must state a new rule is a `PLAY-`
  unit, and it is F3.
- **No uptake instrument beyond the observer named in F5.** Whether an agent handed the brief uses
  it is unmeasured and this unit does not pretend otherwise.
- **No corpus scoping, no waiver keying, no coverage floor.** `-3`, `-4` and `-6` own those.
- **`.ts`/`.tsx` stay dark.** `-13`.

## 4. Design

### `--suggest`, and the edge it hangs on

`--suggest <name>` splits the identifier with `subtokens.leading_verb` — the same splitter P1 grades
with, so the answer cannot disagree with the gate — and looks the leading token up in the declared
table. No corpus pass, no `git ls-files`, no parse: the whole cost is reading `.lexicon.conf`, which
is why the prototype measured 0.042 to 0.047 s.

The verdict is available today. The MESSAGE is not. `TOOL-dScaffoldedMirror-8` turns a `VERBS` row
into `<verb> <gloss> — NOT <other>[, NOT <other>]` as parsed data and backfills the 11 rows of 22
that carry no negative definition at all; inverting that index is what lets `--suggest fetch_remote`
answer "use `load`; the declaration says `load`, NOT `fetch`" instead of the contentless "not in the
declared VERBS table". **This is a new dependency edge and it points the wrong way for the phase
order**: `-10` is Phase 1 and `-8` is Phase 2. It is resolved in F1 by landing the surface here with
the degraded message named out loud, and letting `-8` fill it in the commit that lands the index.
`-8` should carry the matching sentence in its own §2 or §4.

### `--brief`, and the histogram it replaces

The prototype printed the declared table plus a frequency histogram of the directory's off-table
leading tokens — 378 bytes and 0.18 s on this repo. It dies at adopter scale. One `incms` test
directory carries **750 distinct off-table leading tokens** and a 7,996-byte full list, so the
top-nine line priced at 92 bytes shows **1.2%** of the live vocabulary. The truncation that bounds
the cost is what voids the signal, and there is no truncation that does not.

The replacement is keyed on what the author is about to name rather than on where they are standing.
For each definition in the handed file, take its OBJECT — the subtokens after the leading one — and
report, for each object, the set of leading tokens that spell it anywhere in the corpus. The row
count is bounded by the distinct objects in ONE file, which is a small number by construction, and
the report surfaces the only drift class this repo has actually measured: `do_`-prefixed subcommand
entrypoints in `memory-tree` against `cmd_`-prefixed ones in `govkit`, and one file carrying 29
`t_`-led definitions beside 5 `test_`-led ones while `test` is a declared row and `t` is not.

### The coverage-mode refusal

82 of this repo's tracked files are `.sh` and shell is declared `dark`; 54 of the 126
definition-carrying files, 42.9%, are covered by an armed mode. Handed a `.sh` path, a brief with an
empty "established here" section is byte-indistinguishable from a brief over a language with nothing
established, and the first reading an author takes from it is "invent freely". So the brief prints
its coverage mode for the path's extension on every run, and on `dark` it prints
`COVERAGE: dark — nothing extracted for .sh` and produces no brief at all.

### The exit-code grammar, which is narrower than "exit 0 only"

The guard handed to this unit is "exit code 0 only", and read literally it collides with S3: a
refusal that exits 0 is a refusal an author's wrapper cannot see. The rule that satisfies both is
that neither verb may ever emit **1**, which is this engine's gate verdict. `2` is already this
module's refusal code — `lexicon.py:559` returns 2 on an unknown mode and `:564` on a non-repo — so
`--brief` exits 0 on a brief and 2 on a dark or untracked path, and `--suggest` exits 0 always. The
property that matters is that no invocation of either verb can contribute a RED, and that property
is preserved. F2 records the deviation.

### The rendered Skill

`memory-recall` already ships this exact machinery and it is the seam this unit wires through:
`role = "rendered"` with a `to` and a closed `placeholders` list in `kit.toml`, a render function in
the adopt script, `--check` re-rendering to a temp file and `diff`-ing it against a CR-normalised
read of the committed artifact, a `[ -s ]` refusal so an empty render compared to an equally empty
Skill cannot pass green, a leftover-`{{...}}` scan, and a `[[lf_pin]]` so a Windows checkout cannot
smudge the artifact its own gate byte-compares.

The placeholder set is `VERBS`, `BANNED_SUFFIXES`, `SUGGEST_CLI` and `BRIEF_CLI`, filled from
`.lexicon.conf` and from the kit's install path. The two CLI placeholders take the literal `python3`
spelling for the reason `adopt-memory-recall.sh:144` already records: the render is a COMMITTED
artifact shared across a fleet, so baking one node's resolved launcher reds `--check` on every node
that resolves differently.

**The leg must be unguarded, and the reason is verified rather than stylistic.** The existing
`lexicon wiring` leg carries `guard = ["tools/lexicon/"]`, and `.lexicon.conf` is deliberately not a
guard pathspec — `kit.toml` records that govkit partitions guards into declared classes and a
root-level conf falls into none of them, so declaring one reds `selfcheck` rather than scoping
anything. A declaration edit therefore runs no lexicon leg at all on a guarded bar. An unguarded leg
is the only shape that reds when someone edits the table and does not re-render the Skill, which is
the whole property being bought. Confirmed against `tools/gate-legs.json`: `memory-recall skill
wiring` carries no `guard` key and `lexicon wiring` carries one.

### The charter pointer, with the arithmetic

Measured on this worktree, 2026-08-24:

| subject | bytes | ceiling | free |
|---|---|---|---|
| `AGENTS.md` | 64,394 | 64,512 | 118 |
| `coding-governance-agents.template.md` | 48,827 | 49,152 | 325 |
| the `§12` lexicon block in `AGENTS.md` | 1,726 over five bullets | — | — |
| the `VERBS` block in `.lexicon.conf` | 1,787 with its newline | — | — |
| the bare 22-word verb list | 125 | — | — |

The five bullets measure 391, 344, 237, 396 and 358 bytes. The template's copy of the same block is
1,751 bytes because it carries a 25-byte kit-conditional note the renderer drops, and the five
bullets themselves are byte-identical in both files — so one edit produces one delta in two places.

The third bullet carries four verbatim rows of the file it also names: `build` not `create`, `load`
not `fetch`, `remove` not `delete`, `set` not `update` are the negative definitions of the `build`,
`load`, `remove` and `set` rows of `.lexicon.conf`. That is a value stated in prose beside the source
that owns it, which is the `§6` rule that same document states, and which that document says is "the
one most often broken by the document that states it."

The edit replaces the copy with the pointer and keeps the rule:

```
- Write the NEGATIVE definitions or do not bother, and let a rendered Skill HAND them to the author.
  A row with only a positive gloss cannot tell two verbs apart, and the boundary is the whole product.
```

201 bytes against 236, a delta of **-35**. `AGENTS.md` lands at 64,359 of 64,512 with 153 free and
the template at 48,792 of 49,152 with 360 free. Both improve, which is what net-negative means here.

Two things this does NOT do, said because a reader will expect them. It does not clear the standing
`TEMPLATE-SIZE WARN`: the recorded high-waters are 60,930 for `AGENTS.md` and 48,378 for the
template, both already passed, and a 35-byte shrink does not reach either. And it does not change a
rule — the negative-definitions rule survives word for word, and only the four copies leave.

### The guards, built as structure

1. **No verdict.** Neither verb can emit 1. Asserted by a selftest arm that runs both over every
   fixture and fails on any exit of 1.
2. **No pin figure.** Neither verb prints a `*_OFFENDER_PIN` line or an offender count. Asserted by
   grepping both outputs for `_OFFENDER_PIN` and for `over pin` and requiring no match.
3. **No code path into the seed writer.** A second `LAYERS` row,
   `tools/lexicon/lexicon.py -> tools/lexicon/scaffold_lexicon.py`, makes P3 refuse the import if
   anyone ever adds it. Both globs select a tracked file, so the row is selective and
   `scan_unselective_rules` does not red it; it has no live candidate edge today, which is what an
   obeyed rule looks like and is the reading `memory/gotchas/armed-but-unreachable-rule.md` already
   records. The existing dependency runs the other way — `scaffold_lexicon.py:72` calls
   `lex.extract` — and is untouched.
4. **A header.** The brief's first line states that it prints what the corpus does and never what it
   should do.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~200 lines for the two verbs and the coverage-mode refusal), a new
`tools/lexicon/SKILL.template.md`, `tools/lexicon/kit.toml` (a `[[files]]` rendered row, a
`[[lf_pin]]`, a fourth `[[gate_leg]]`), `tools/lexicon/adopt-lexicon.sh` (render, `--check`
byte-diff, leftover-placeholder scan), the committed `.claude/skills/lexicon/SKILL.md`,
`tools/gate-legs.json` and `.gitattributes` (both regenerated by govkit from the descriptor),
`.lexicon.conf` (one `LAYERS` row), `AGENTS.md` and `coding-governance-agents.template.md` (the
pointer, identical delta), `tools/lexicon/LEXICON.md` and `tools/lexicon/README.md`, and
`tools/lexicon/selftest.py`.

### Alternatives rejected

- **The directory histogram.** 750 distinct off-table leading tokens in one adopter directory, and a
  top-nine line showing 1.2% of them.
- **Embedding the table in the charter.** 1,787 bytes against 118 of headroom.
- **A guarded Skill leg.** It would never fire on the edit it exists to catch, because the guard
  cannot name the declaration.
- **A sixth `§12` bullet.** Any bullet long enough to say something exceeds the 118 bytes of
  headroom, and funding it then requires deleting a rule, which is a `PLAY-` unit rather than this
  one.
- **A hand-written `SKILL.md` with no template.** That is the one genuinely unverifiable state, and
  `adopt-memory-recall.sh:117` already reds on it.

## 5. Production-readiness checklist

- **security** — `--suggest` reads argv and the declaration; `--brief` additionally reads tracked
  files it already has read access to. No write path, no network, no execution of any adopter-supplied
  value. The rendered Skill is a new committed artifact an agent harness loads, so its content is
  governed by the byte-diff and by the declaration that owns it, and the renderer refuses a leftover
  placeholder rather than shipping one.
- **perf / scale** — `--suggest` 0.042 to 0.047 s measured, no corpus pass. `--brief` 0.18 s here and
  ~1.6 s on a 6,168-file adopter. The Skill `--check` leg ~0.8 s. The three lexicon legs are 13.0 s
  of a 2,587 s leg-sum, 0.503%; a fourth makes it four legs and cost is not a constraint on this kit.
- **a11y** — N/A. A CLI and a markdown Skill; there is no rendered surface to make accessible.
- **i18n** — N/A, and deliberately. The table is a closed English word class and translating a row
  would change which verb it excludes, which is the whole content of a negative definition.
- **error / empty / loading states** — the empty state is the subject. An empty "established here"
  section on a `dark` extension is byte-indistinguishable from an unextracted language, which S3
  refuses; a tracked path with zero definitions and an untracked path are separate outputs.
- **observability** — the two verbs ARE the observability change for the declaration half. What
  stays unobserved is uptake, and F5 is the instrument for it.
- **risks** — three. The new leg is UNGUARDED and therefore runs on every bar including a
  records-only commit, so a CRLF smudge on the rendered artifact reds it on Windows; the `[[lf_pin]]`
  is what prevents that and `memory-recall` has already paid for learning it. The charter edit
  touches two files that must move together, since `AGENTS.md` is rendered from the template, and
  `playbook render wiring` is the leg that catches a half-edit. And `--suggest`'s message is degraded
  until `-8` lands, which is a known gap rather than a defect.
- **testing + left-shift gates** — arms for the Skill drift red, the empty-render refusal, the
  leftover-placeholder refusal, the `dark` refusal, the no-pin-in-output assertion, the no-exit-1
  assertion and `--suggest`'s determinism. The two Skill arms are modelled directly on
  `t_skill_drift_reds` and `t_skill_description_invariants` in `tools/memory-recall/selftest.py`.
- **migration / rollback** — the rendered Skill is a new file and the `LAYERS` row is additive.
  Rollback is deleting the Skill, its leg and its LF pin, and reverting one bullet in two files. No
  persisted artifact changes shape and no declaration key changes meaning.
- **user docs** — S7. `LEXICON.md` gains the delivery section, `README.md` gains the verbs and the
  leg, and the charter bullet is the pointer.

Unresolved here, and therefore the owner scope menu: **observability** — whether the uptake observer
of F5 ships in this unit; and **risks** — whether the unguarded leg is acceptable on every bar or
must wait for a records-only exemption this repo does not currently have.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --suggest build_index` runs, it prints a single
  line beginning `OK` and exits 0, having read only `.lexicon.conf`; a selftest arm asserts no
  `git ls-files` subprocess was spawned.
- **AC2** — When `python tools/lexicon/lexicon.py --suggest fetch_remote` runs, it names the
  off-table leading token `fetch` on one line and exits 0. After `-8` lands, the same invocation
  quotes the negative definition and names `load`; until then the arm asserts only the token.
- **AC3** — When `python tools/lexicon/lexicon.py --brief tools/memory-tree/gen_build_index.py` runs,
  its output carries one row per distinct object in that file and each row lists every leading token
  live for that object across the corpus, flagging any object spelled more than one way. rev-1 named
  `do_check_format` showing both `do` and `cmd`; `TOOL-dScaffoldedMirror-14` renamed every `do_` away
  before this unit was built, so that example is GONE and its absence is the earlier unit having
  worked. The live example the arm uses instead is `conf`, spelled `load` x9, `read` x1 and `budget`
  x1 — the `load_conf`/`read_conf` conflict the research pass measured, surfaced by this verb.
- **AC4** — When `--brief` is handed a path whose extension is declared `dark`, it prints
  `COVERAGE: dark` naming the extension, produces no established-here section, and exits `2`.
- **AC5** — When either verb runs over any selftest fixture, its stdout contains neither
  `_OFFENDER_PIN` nor `over pin`, and its exit code is never `1`. Asserted by
  `python tools/lexicon/selftest.py`, not by reading the output.
- **AC6** — When `.lexicon.conf`'s `VERBS` block is edited and `.claude/skills/lexicon/SKILL.md` is
  not re-rendered, `bash tools/lexicon/adopt-lexicon.sh --check` exits non-zero and prints `DRIFTED`.
- **AC7** — When the render is forced to produce an empty file, `--check` refuses rather than
  comparing it to an equally empty Skill and passing.
- **AC8** — When `tools/gate-legs.json` is regenerated from `tools/lexicon/kit.toml`, the row named
  `lexicon skill wiring` carries no `guard` key, matching `memory-recall skill wiring`.
- **AC9** — When `bash tools/check-template-size.sh AGENTS.md` runs after the charter edit, it
  reports 64,359 of 64,512 bytes and exits 0, and `bash tools/check-template-size.sh` reports 48,792
  of 49,152 and exits 0.
- **AC10** — When `python tools/lexicon/lexicon.py` runs after the new `LAYERS` row lands, P3 reports
  no `UNSELECTIVE LAYERS RULE` for it and no offender, so the row is armed and obeyed rather than
  inert.
- **AC11** — When `--suggest` is timed over 20 consecutive invocations, every one completes in under
  100 ms on node `d`.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`,
`charter size`, `template size <=48KiB`, `playbook parity`, `playbook render wiring`, `govkit
selfcheck`, `kit version markers` and `marker contracts`.

Adds exactly one leg: **`lexicon skill wiring`**, `subject = "repo"`, argv
`bash tools/lexicon/adopt-lexicon.sh --check`, and **no guard**. Everything else this unit builds is
a new refusal or a new verb inside an existing leg, which is deliberate — the leg count is not the
coverage, and the one addition exists because no existing leg can be made to fire on a declaration
edit.

## 8. Open questions

- **F1 — `--suggest`'s message before `-8` lands, and the new edge it creates.** The replacement
  clause needs `-8`'s structured NOT-clause index, and `-8` is a phase later. Options: land the
  surface now with the degraded message; block `-10` on `-8` and re-order the phases; or parse the
  gloss column here, which would put a second reader on a grammar `-8` owns. RECOMMENDATION: land the
  surface now. The verdict is the useful half and it is available today, the phase order was chosen
  because supply beats pressure, and a second parser for `-8`'s grammar is the one option that
  creates a defect rather than a gap. RESOLVED (agent, 2026-08-24, delegated): land the surface in
  Phase 1 with the degraded message named in the README, and `-8` upgrades it in the commit that
  lands the index. The edge is NEW and `-8` should state it as "unblocks `-10`'s message".
- **F2 — `--brief`'s exit code on a `dark` path.** The stated guard is "exit code 0 only" and a
  refusal that exits 0 cannot be seen by a caller. RECOMMENDATION: read the guard as "never 1", which
  is what it is protecting — the gate verdict — and use the module's existing refusal code 2.
  RESOLVED (agent, 2026-08-24, delegated): `--brief` exits 0 or 2 and never 1, `--suggest` always
  exits 0, and the no-exit-1 property is asserted in AC5 rather than left as prose.
- **F3 — does the charter need a rule change rather than a pointer?** `§12` currently says nothing
  about the table being DELIVERED, and one reading is that the missing rule is exactly this unit's
  subject. RECOMMENDATION: no. The pointer sentence carries the delivery fact inside an existing
  rule, the byte budget does not fund a sixth bullet, and a rule change to the operating ruleset is a
  `PLAY-` unit with a different reviewer. RESOLVED (agent, 2026-08-24, delegated): pointer only; if a
  later pass concludes a rule is owed, it opens a `PLAY-` unit and does not grow this one.
- **F4 — UNRESOLVED, owner. The Skill's trigger rate is unmeasured and there is no in-repo
  precedent.** `memory-recall`'s description is question-shaped, which is a much stronger trigger
  signal than a "before you name something" description can be, and no measurement exists of how
  often a harness loads a Skill on that shape. This unit ships the Skill anyway because the byte-diff
  property is worth having regardless of trigger rate, but the claim "an author will be handed the
  table" is UNVERIFIED at landing and must not be written as though it were measured. It stays open
  until F5's observer reports.
- **F5 — should the uptake observer ship with the brief or after it?** Nothing measures whether an
  agent handed the brief actually uses it, and the same `PostToolUse` observer instrument that
  `tools/memory-recall/recall-opened.js` already provides would answer it. RECOMMENDATION: with. An
  instrument that ships later measures a different population than the one the change was made for,
  and this build's whole diagnosis rests on a measurement nobody had planned to take. RESOLVED
  (agent, 2026-08-24, delegated): the observer ships in this unit, opt-in on the `recall-opened`
  pattern, and F4 stays open until it has reported.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, recommendation
  R9 and its Phase 1 exit criteria) and on the read-only probe of `incms/main` taken the same day,
  from which the 750-token directory and the 7,996-byte list are drawn. Charter and block byte
  figures re-measured on this worktree while writing.
- rev-1 status 2026-08-24 · KEPT whole and RE-ORDERED to land first or second. Three defects owed at rev-2: it reds three gate legs its own section 7 lists as green, AC9's byte literals are wrong by two (the measured delta is -33, landing at 64,361 and 48,794), and two map inventory keys go unclaimed.

- rev-2 · 2026-08-25 · S1, S2, S3 and S6 BUILT; S4, S5 and S7 remain. AC3's stated example is GONE
  and the spec now says why: `-14` renamed every `do_` away first, so `check_format` shows only
  `cmd`. A criterion naming a live instance ages with the tree, and the honest repair is to name
  what is live NOW rather than to weaken the criterion. AC1, AC2, AC4, AC5 and AC11 are met and
  observed — AC11 at 84 ms worst of 20 against a 100 ms bar. AC2's FULL form works because
  `TOOL-dScaffoldedMirror-8` S6/S7 landed first: `--suggest fetch_remote` names `load_remote` and
  quotes the negative, which is the whole reason that split was taken.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py skill render brief suggest vocabulary author` returns
`render` (`tools/playbook/render_playbook.py`, fan-in 5, SEAM) and three `render_*` seams in
`tools/codebase-map/map_lib.py`, plus the `memory-recall skill wiring` gate-legs key,
`t_skill_description_invariants` and `t_skill_drift_reds` in `tools/memory-recall/selftest.py`, and
the `memory-recall` dossier.

The seam this unit wires THROUGH is the `memory-recall` rendered-Skill machinery, and it is a real
one rather than a near-miss: the `role = "rendered"` plus `to` plus `placeholders` contract in
`kit.toml`, the render-and-byte-diff shape of `adopt-memory-recall.sh` including its `[ -s ]` empty
refusal and its leftover-placeholder scan, the unguarded `[[gate_leg]]`, and the `[[lf_pin]]` on the
committed artifact. Its two selftest arms are the model for AC6 and AC7. Nothing is copied by hand
that govkit can emit from a descriptor.

`render_playbook.py`'s `render` is NOT the seam despite ranking first. It fills placeholders in the
charter template against a target's `deploy.toml`, and the lexicon Skill renders from
`.lexicon.conf` against a kit-owned template with a different placeholder set and a different owner;
wiring one through the other would couple the naming kit's delivery to the playbook deployer's
contract for no shared behaviour. The charter edit in S5 does touch that renderer's INPUT, which is
why `playbook render wiring` is named in §7, but it is an edit to the template rather than a reuse of
the renderer. No new shared helper is introduced.
