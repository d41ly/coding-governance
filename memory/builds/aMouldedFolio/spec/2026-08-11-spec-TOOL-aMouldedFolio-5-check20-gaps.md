# TOOL-aMouldedFolio-5 — check 20 reuses the kit's fence reader, and refuses a fence it cannot close

**Status:** CLOSED · rev-2 · 2026-08-11 · node a · Tier-2 · base 7890becf · streams tooling

## 1. Goal

Replace check 20's private fence toggle with the fence reader this kit already has, and add the one
behaviour neither implementation has: refusing a document whose fence is never closed.

## 2. Scope (IN)

- **S1** — `row_grammar.scan` reads lines through `gen_build_index.unfenced`, which already strips one
  trailing CR, recognises `~~~`, and closes a fence only with the marker that opened it. The private
  boolean toggle is deleted.
- **S2** — an UNTERMINATED fence is a named failure naming the file and the line the fence opened on.
  Neither existing implementation does this; it is the only new behaviour in the unit.
- **S3** — the `unkeyed` branch reports path and line per offender, in the shape the duplicate branch
  already prints, instead of a bare count.
- **S4** — an arm per new or changed branch, each asserting that branch's own text, each proven by a
  negative control against the pre-change predicate.

## 3. Non-goals (OUT)

- **The five shell replicas keep this defect and that is deliberate.** `_unfenced` in the hygiene
  engine and its replicas leave the fence open at EOF and silently drop every later line, at exit 0 —
  the same hole S2 closes for check 20. Fixing them is a shell-side change across a gate this unit
  does not otherwise touch, and it belongs to its own unit. Named here so the asymmetry is a decision
  rather than an oversight.
- No change to what check 20 ASSERTS. Uniqueness per file and the keyability precondition are
  unchanged.
- No waiver registry for `unkeyed`: the measured count is 0, and a registry over an empty population
  is the vacuous-selector class.

## 4. Design

### Data model

`gen_build_index.unfenced` is a generator over a document's unfenced lines. Measured against S1's
three requirements it already satisfies all three:

| Requirement | `unfenced` | check 20's current toggle |
|---|---|---|
| strip one trailing CR | yes | yes |
| recognise `~~~` | yes | **no** |
| close only with the opening marker | yes | **no** (any fence line toggles) |
| refuse an unterminated fence | **no** | **no** |

So the unit is a REUSE plus one addition, not a build. rev-1 said "none in this kit — the hygiene
engine's own scanners do not fence-skip" and decided BUILD; both halves were false, and the seam sits
in the module this kit's own check 9 already calls.

`unfenced` yields lines and discards fence state, so S2 cannot be expressed by the existing generator
alone. The unit adds a sibling that yields `(lineno, text)` and reports the open fence at EOF, and
`unfenced` is re-expressed in terms of it so there is still ONE fence machine in the module rather
than two.

Why refuse rather than best-effort: a fence opened near the top of a row document hides every
duplicate below it, and hiding duplicates is what check 20 exists to prevent. Any reading that keeps
scanning has to guess whether the author meant a fence, and the guess that keeps rows visible is the
one that lets a typo change the check's population.

### Inventory

| Function | Change |
|---|---|
| `gen_build_index` | `unfenced` gains a line-numbered, fence-state-reporting sibling; `unfenced` delegates to it |
| `row_grammar.scan` | reads through the sibling; the private toggle is deleted; refuses an open fence at EOF |
| `row_grammar.do_check` | new branch for the unterminated fence; `unkeyed` prints path and line |
| `row_grammar.scan`'s return | `unkeyed` becomes a list of `(path, line)`, not a count |
| `row_grammar.do_report`, `do_emit_pin` | updated for the new return shape — both unpack `scan` and rev-1's Inventory named neither |
| both selftests | S4's arms |

### Migration

None to the corpus. Measured: no row document contains a `~~~` fence, an unterminated fence, or a
fence of any kind — so every arm is a fixture, stated here so a green run is not mistaken for
coverage.

### Rollout

One commit, and it MUST be one: the change spans two modules in the same kit, and the epoch gate
requires the version bump at or after the last engine change in the pushed range.

### Files touched (estimate)

| File | Why |
|---|---|
| `tools/memory-tree/gen_build_index.py` | the fence sibling |
| `tools/memory-tree/row_grammar.py` | S1, S2, S3 |
| both modules' selftests | S4 |
| `tools/memory-tree/check-memory-hygiene.sh` + both rule-set halves | the version pair — see §8 for the value |
| `memory/map/generated/*` | new functions enter the symbol corpus, so the freshness leg reds without a regen |
| `memory/map/features/row-grammar.md` | the Gaps section this unit closes, and the docstring correction below |
| `.claude/SESSION-KICKOFF.md` | the audit stamp; the hygiene engine is watch item 1 |

### Alternatives rejected

- **Build a private fence reader** (rev-1's plan). Rejected: a second fence machine in the same kit is
  the two-answers class, and the existing one already meets three of four requirements.
- **Import the shell `_unfenced`.** It is awk inside the gate this module is delegated FROM; calling
  back into it would invert the dependency and add a subprocess to a path check 9 runs every time.
- **Treat an unterminated fence as "no fence".** It guesses, and the guess hides duplicates.

## 5. Production-readiness checklist

| Concern | Position |
|---|---|
| Empty population | Every fence arm is a fixture; the corpus has none. Stated so a green run is not read as coverage. |
| Cross-module coupling | Both modules are in one kit directory, imported directly, no subprocess and no cross-kit edge. |
| Return-shape change | `scan` has three callers inside the module; all three are named in the Inventory, which rev-1 did not do. |
| Failure visibility | The unterminated-fence failure names file and opening line; `unkeyed` gains path and line. |
| Ordering | Offenders sort by path then line. |
| Cost | One generator instead of a per-line boolean; no new pass. |
| Reversibility | Both changes are module-local. |

## 6. Acceptance criteria

- **AC1** — a `~~~` fenced block's rows are excluded from the row count and the duplicate census.
- **AC2** — a ``` marker inside a `~~~` block is content, and the reverse, in BOTH modules.
- **AC3** — a document whose fence never closes REDS, naming the file and the opening line number.
  The fixture used carries a duplicate id AFTER the unterminated fence, so the arm fails if the
  implementation silently skips instead of refusing — a fixture whose fence hides nothing cannot tell
  the two behaviours apart.
- **AC4** — the `unkeyed` branch prints one line per offender with path and line, matching the
  duplicate branch's shape.
- **AC5** — `--report` and `--emit-pin` still work after the return-shape change, asserted by an arm
  each, not by inspection.
- **AC6** — check 20's verdict on the REAL corpus is unchanged: row count, unkeyed count and duplicate
  set are identical before and after, measured and recorded in the build report.
- **AC7** — every new branch has a positive arm naming its own text, and each arm FAILS against the
  pre-change code; the negative control is run per branch and its output recorded in the build report at
  `build/2026-08-16-build-TOOL-aMouldedFolio-3-3-followups-controls.md` §3.
- **AC8** — the false claim in `row_grammar.py`'s module docstring and in the dossier — that an
  undeclared pin is "its own refusal" — is corrected, since `pin_of` returns 0. Both copies move.

## 7. Gates

`bash tools/run-gates.sh` green on a QUIESCENT tree at the push boundary. Affected legs: memory
hygiene, the row-grammar selftest, the build-index selftest, codebase-map coverage + freshness, the
kit-version and verdict-epoch pair, kit-dogfood parity, and the kickoff ratchet. The
recurring-bug-class checklist runs over the diff before review.

## 8. Open questions

- **RESOLVED (agent, 2026-08-11, delegated): the version value and landing order.** The three
  follow-up units bump one constant, and an identical bump on two branches merges clean while
  the epoch gate stays satisfied, so they land SEQUENTIALLY on one branch.
  **CORRECTED at the landing:** the value stated here (2.9) was wrong — the base already carried
  a higher one, and main's own lineage reached 2.13 in parallel while this branch went to 3.0.
  A 'next value' rule cannot be fixed in a spec at all: the next value is only knowable at the
  merge, against whatever the other nodes landed. The landing took 2.14, then 2.15 when the
  merge's own resolution read as a DECREASE from the branch side and the epoch gate refused it.
  The standing rule is therefore: pick the value at the merge, above every lineage present, and
  expect the post-merge audit to need one more.

## 9. Revision log

- rev-1 · 2026-08-11 · first draft from the dossier's Gaps section.
- rev-2 · 2026-08-11 · Tier-2 review fold. The Reuse audit was FALSE and its verdict inverted: the
  kit already carries a fence reader meeting three of the four requirements, so the unit becomes a
  reuse plus one addition. `--report` and `--emit-pin` were unnamed consumers of the changed return
  shape. The "three gaps" framing did not map onto the scope items and is replaced by the requirement
  table. AC3 gained the hides-a-duplicate fixture, without which it cannot distinguish refusing from
  skipping. The five shell replicas keeping the same defect are now an explicit non-goal. The version
  value and landing order are fixed in §8.

## 10. Reuse audit

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| Recognise a fenced block, `~~~` included, marker-matched, CR-stripped | `gen_build_index.unfenced` | **REUSE** — same kit dir, plain import; rev-1 said no seam existed and was wrong |
| Report an offender with path and line | the duplicate branch in this module | REUSE its shape for `unkeyed` |
| Refuse at EOF with fence state | nothing has it — `unfenced` discards state and `_unfenced` exits 0 | BUILD, as the sibling generator, bounded to this kit |
| Arm a new failure branch | each module's `--selftest` | REUSE |
| Prove an arm is not vacuous | the negative-control practice | REUSE as AC7 |
