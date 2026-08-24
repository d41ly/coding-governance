# DEPL-dCarriedReceipt-9 — `carry` rungs, recomputed, over a derived needle map

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

After `-7` a receipt row carries two identities, `gov_oid` and `oid`, and `oid != gov_oid` is the
local-delta predicate. On its own that predicate is too blunt to install anything. An adopter at a
non-default `prefix` differs from gov on every file that spells a path, so those rows read as local
deltas forever and never take an automatic write — which is the state both live targets are in.
Measured on inCMS at `2cff5855` against each row's own recorded gov commit: of the 52 rows whose
commit resolves, 21 are byte-identical, 6 differ only in line endings, and 5 differ only by the
prefix relocation. Eleven rows carry no local edit at all and the blunt predicate refuses every one.
This unit explains the difference with a per-row `carry` rung — `verbatim`, `eol` or `relocate` —
recomputed by proof on every run and never read back from the receipt.

## 2. Scope (IN)

- **S1** — `classify_row` (`govkit.py:2874`) computes `carry` before it computes a verdict, over
  three rungs tried in order, cheapest first: `verbatim` (ours == base), `eol` (equal after CRLF to
  LF applied to both sides), `relocate` (ours == relocate(base, alpha)). The first that proves itself
  wins; none proving itself means there is a local delta.
- **S2** — `carry` is RECOMPUTED on every run and never trusted from the receipt. It is written into
  the row for reporting, and the reader is the print loop only. No branch in either verb may read a
  stored `carry`, which is asserted by an arm rather than left to discipline.
- **S3** — `alpha` is DERIVED from the receipt and never authored. Each row contributes one pair,
  `(dirname(source), dirname(path))`; the pairs are deduplicated; any gov directory that yields two
  DIFFERENT target directories is DROPPED and reported by name. There is no override key and no
  descriptor field: an authored map is a second answer to a question the receipt already answers.
- **S4** — needles emit in both the `/` form and the `~` form, because gov flattens paths into
  fixture filenames. Substitution is a single left-to-right pass, longest needle first, and the
  output is never rescanned, so one substitution can never feed another.
- **S5** — WHOLE-FILE equality decides a rung. One residual byte and the rung does not match, the
  row keeps exactly the verdict it has today, and nothing is written.
- **S6** — for a row that DID match a rung and later diverges, the rung is applied to BOTH `base`
  and `theirs` before `three_way` (`:2897`), so the substitution cancels in the base-to-theirs diff
  and `git merge-file` sees only gov's semantic change.
- **S7** — the run prints one line per dropped ambiguous gov directory and one line naming the pair
  count and the needle count, so a map that silently collapsed is visible rather than inferred.
- **S8** — `selftest.py` arms: one per rung, one for the ambiguity drop, one for the `~` form, one
  for the no-rescan property, one asserting the three-way sees only the semantic change, and one
  asserting a stored `carry` in a fixture receipt is ignored.

## 3. Non-goals (OUT)

- **Not** a write-time transform. `alpha` is a PROOF instrument: it is applied to gov's bytes only to
  compare them, never to produce bytes that get landed on the strength of the map alone. That
  alternative was measured and is rejected in §4.
- **Not** an authored, overridable or descriptor-declared map, and **not** a free-form rewrite rule
  or line-level partial application. All three sit on the build-wide cut list.
- **Not** rename detection. A row whose target path moved is `-11`, and this unit must not grow a
  second answer to it: `alpha` explains a difference in BYTES, never a difference in the row's path.
- **Not** composing rungs. `relocate` is proved on raw bytes, not on eol-normalised ones. See §8 F2.
- **Land-alone caveat:** this unit CANNOT land alone. It reads `gov_oid` and `oid`, which `-7`
  introduces, and it would re-open the integrity hole `-8` closes if a merged result could still
  overwrite `gov_oid`. It lands after both, in that order.

## 4. Design

### Data model

One new row field, `carry`, holding `verbatim`, `eol`, `relocate`, or absent. It is output, not
input. No other receipt shape changes, and a receipt written before this unit reads identically
after it — every rung is recomputed from the two identities the row already carries.

### Inventory

The derivation, measured over inCMS at `2cff5855` against gov `9ddcc5c9`, reconstructed from
`.governance/kits.json` plus `.governance/install.index` because neither target has a govkit receipt
yet:

| Quantity | Value |
|---|---|
| rows in the reconstructed population | 92 |
| rows whose gov source resolves | 86 |
| gov directories after the dirname lift | 15 |
| gov directories dropped as ambiguous | 2 — `tools/memory-recall` and `tools/workflows` |
| surviving directory pairs | 13 |
| needles emitted, 13 pairs in 2 forms | 26 |

Rung distribution over the 52 rows carrying a resolvable recorded gov commit:

| Rung | Rows |
|---|---|
| `verbatim` | 21 |
| `eol` | 6 |
| `relocate` | 5 |
| none, a local delta | 20 |

The five `relocate` rows are `scripts/unattended/adopt-unattended.sh`, `check-playbook.test.sh`,
`cross-component.test.sh`, `playbook.fixture.md` and `run-unattended-gates.sh`. All five prove on
RAW bytes, and zero of them need `eol` composed with `relocate`, which is what §8 F2 rests on.

`tools/memory-recall` being dropped is the derivation working, not failing. It maps to
`scripts/recall` for `query.py` and to `.claude/hooks` for `recall-opened.js`, so it names two
different destinations and cannot be a needle. `tools` survives as a single pair here only because
the dirname lift keeps `tools/hooks` to `.claude/hooks` separate from it.

### Alternatives rejected

- *Apply the map at WRITE time, rewriting gov's bytes through `alpha` and landing the result.*
  Measured and rejected. On `tools/unattended/adopt-unattended.test.sh` at `ce5dca99` it corrupts six
  lines: four occurrences of the fixture literal `bash tools/land.sh`, which the `tools` needle
  rewrites although it names no prefix at all, and lines 132-133, where the fixture builds a
  directory literally named `my tools/unattended` and the needle turns it into `my scripts`. Under
  the proof gate this row simply matches no rung and stays a local delta, and none of those six
  lines is ever written. Measured more widely: of the 27 rows that are green by identity today, a
  blanket write-time rewrite changes the bytes of 17.
- *Lift each row to a directory pair by stripping EQUAL trailing segments.* Measured and rejected;
  it is also the form the design brief carries, and it is wrong. Stripping `unattended` as an equal
  segment collapses `tools/unattended` into the bare gov directory `tools`, which then collides with
  the hooks kit's `tools` and is dropped as ambiguous — taking the whole unattended kit's relocation
  with it. Measured on the same population: 5 gov directories, 3 surviving pairs, and zero
  `relocate` rows. The dirname lift yields 13 pairs and 5 rows.
- *Rescan the output, or substitute longest-match-anywhere rather than left-to-right.* Either lets
  one substitution feed another, so rewriting `tools` inside a path already rewritten to `scripts`
  becomes reachable and the transform stops being a function of its input.
- *Store `carry` and trust it.* A stored rung is a claim about bytes that have moved since. The whole
  point of the two identities is that no stored boolean stands between the tool and the blobs.

### Migration

None. `carry` is additive and derived; a schema-2 receipt written before this unit is read
identically after it, and the field is recomputed on the first run regardless of what it holds.

### Files touched (estimate)

`tools/govkit/govkit.py` (~70 lines: the derivation, the substituter, the rung ladder inside
`classify_row`, the two report lines), `tools/govkit/selftest.py` (7 arms), and one fixture receipt
carrying a non-default prefix and a deliberately ambiguous gov directory.

## 5. Production-readiness checklist

- security — the rung ladder WIDENS the automatic-write arm, which is the one direction that needs
  argument. It is contained by S5: a rung opens the arm only after proving whole-file equality
  against bytes gov holds, so a row admitted here is one whose content is provably a mechanical
  restatement of gov's, and the raw-write arm stays closed to every row that is not.
- perf / scale — one extra whole-file comparison per non-identical row, and at most one substitution
  pass per such row. The measured population is 92 rows, and the blob reads that dominate the run
  already happen. No new subprocess.
- a11y — N/A: CLI.
- i18n — N/A. The substituter operates on bytes decoded as UTF-8 and returns its input unchanged on a
  decode failure, so a binary row is never mangled into a false rung; asserted by AC6.
- error / empty / loading states — a receipt whose rows yield NO surviving pair produces an empty
  `alpha`, which makes `relocate` degenerate to `verbatim` rather than raising. A row with no
  `source` contributes no pair and is skipped, not refused.
- observability — S7's two lines. A dropped gov directory is printed by name with both destinations,
  because a silently collapsed map is indistinguishable from a target that genuinely relocated
  nothing, and that is the failure mode that would waste the most time.
- risks — the residual risk is a FALSE rung: two files that happen to be equal after substitution
  while the target genuinely edited one of them. That requires the edit to be exactly the
  substitution, in which case the bytes are gov's answer anyway. The larger risk runs the other way
  and is accepted by design: a row like `adopt-unattended.test.sh` will never take an automatic
  write, and that is the correct outcome rather than a gap.
- testing + left-shift gates — seven `selftest.py` arms (S8). The classes left-shifted are "a
  substitution that chains" and "a map with an ambiguous key", both gated directly rather than
  through the row that exposed them.
- migration / rollback — none; revertible as a pure addition. Dropping the field returns every row to
  the `-7` and `-8` behaviour with no on-disk change.
- user docs — `WIRE-INTO-PROJECT.md` gains one paragraph beside the update step naming the three
  rungs and stating that a row with no rung is never written automatically.

## 6. Acceptance criteria

- **AC1** — Over a fixture receipt built from inCMS's 52 resolvable rows, `classify_row` reports
  `verbatim` on 21, `eol` on 6 and `relocate` on 5. Observe RED first: at `9ddcc5c9` the returned
  dict has no `carry` key at all and all 32 non-identical rows classify with `o_state` as `differs`.
- **AC2** — The derivation over that same receipt yields exactly `13` directory pairs and `26`
  needles, and DROPS `tools/memory-recall` and `tools/workflows` by name in the printed report.
- **AC3** — `scripts/unattended/adopt-unattended.test.sh` matches NO rung, keeps its current verdict,
  and its bytes are unchanged after a `govkit.py update --write` against the fixture, asserted with
  `git diff --exit-code` over that path. This is the `my tools` row; a build that "fixes" it has
  re-introduced the rejected write-time alternative.
- **AC4** — A needle map containing both `tools/unattended` and `tools` rewrites
  `tools/unattended/fixture-records/tools~a~b.md` to
  `scripts/unattended/fixture-records/scripts~a~b.md` in ONE pass, and rewrites a string already
  reading `scripts/unattended` not at all. The `~` arm is load-bearing at gov HEAD:
  `tools/unattended/check-playbook.test.sh` spells `tools~` at lines 365, 479, 523, 570 and 582 while
  inCMS's fixture records are named `scripts~unattended~fixture-pieces~one~piece.md.md`.
- **AC5** — For a row that matched `relocate` and then diverged, `three_way` is called with the rung
  applied to both `base` and `theirs`, and the merged output carries gov's semantic change with the
  target's spelling intact. Asserted on CONTENT and never on the exit code, per `three_way`'s own
  docstring.
- **AC6** — A fixture row whose blob is not valid UTF-8 returns unchanged from `relocate` and
  classifies exactly as it does at `9ddcc5c9`.
- **AC7** — A fixture receipt carrying a hand-written `"carry": "relocate"` on a row that provably
  matches no rung classifies as a local delta anyway, and `python tools/govkit/govkit.py update`
  never reads the stored value.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. Adds seven arms and one fixture; adds no new leg file. It adds NO refusal branch —
the ambiguity drop reports through `r.note` and a print rather than `r.fail` — so
`tools/govkit/refusal_join.py` and its shrink-only `BRANCH_PIN = 161` are unmoved, and that pin
staying untouched in the diff is itself the assertion.

## 8. Open questions

- **F1 — should an ambiguous gov directory drop silently, drop loudly, or refuse the run?** Drop
  loudly. Refusing would make a perfectly installable target unupdatable over a map entry it never
  asked for, and a silent drop is indistinguishable from a target that relocated nothing, which is
  the exact confusion §5's observability line exists to prevent.
  RESOLVED (agent, 2026-08-24, delegated): drop and report by name, under the full-scope approval.
- **F2 — should the rungs compose, so a row may be `relocate` AND `eol` at once?** No: a ladder, not
  a lattice. Measured on the live target, all five `relocate` rows prove on raw bytes and zero need
  the composition, so composing today buys nothing and adds a fourth rung's worth of surface. The
  cost is stated rather than hidden: an adopter whose checkout is CRLF and whose prefix is also
  non-default falls to local delta on those rows and gets the three-way instead of a raw write.
  RESOLVED (agent, 2026-08-24, delegated): a strict three-rung ladder, with composition left as a
  later unit's ask if a target ever needs it.
- **F3 — derive `alpha` from the RECEIPT, or re-resolve it from the descriptors?** From the receipt.
  The descriptor says where gov would put a file today; the receipt says where the target actually
  took it, and `update`'s whole job is to move what was taken. Re-resolving would also make the map
  drift the moment a descriptor's `to` changes, which is the class `-1` closes elsewhere.
  RESOLVED (agent, 2026-08-24, delegated): from the receipt.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every line
  number cited was opened at `9ddcc5c9`, and every count in §4 was re-measured against inCMS at
  `2cff5855` rather than carried from the brief. Four corrections to the brief are folded in.
  First: the lift is a DIRNAME pair per row, not "stripping equal trailing segments" — the latter
  yields 5 gov directories and 3 surviving pairs and kills every unattended relocation, measured both
  ways, and §4 records the rejected form. Second: the needle count derived from the 13 pairs is 26,
  not 178; 178 is 2 times 89, the shape of a per-ROW needle set rather than the per-directory map the
  architecture specifies, so S4 pins the per-directory derivation and §4 pins 26. Third: the
  `my tools/unattended` hazard is real and verified at lines 132-133, and there is a SECOND instance
  in the same file the brief does not name — four `bash tools/land.sh` lines hit by the bare `tools`
  needle. Fourth: the blanket-rewrite blast radius measures at 17 currently-green rows here against
  the brief's 18; the reconstruction excludes 6 rows whose gov source does not resolve and 34 whose
  recorded commit reads `unverified`, either of which accounts for the one. Two line numbers in the
  brief's reuse list are also off by one and are cited correctly above: `three_way` is at `:2897`,
  and `Report` is at `:565` with `Refusal` at `:78`.

## 10. Reuse audit

Wires through `classify_row` (`:2874`) rather than adding a second classifier beside it, and through
`blob_at` (`:2148`) for every byte it compares, which is what keeps a rung a claim about the git
index rather than about a worktree. The three-way arm reuses `three_way` (`:2897`) unchanged; S6
changes only what is handed to it.

One seam is deliberately NOT reused, and that decision is the reuse result. `resolve_dests` (`:2067`)
and `rule_relpath` (`:172`) already know how a source maps to a destination, and calling them here
would look like reuse. They answer for the descriptor as it reads TODAY, while `alpha` must answer
for what the target actually installed, possibly at a different gov commit and a different `prefix`.
Reusing them would make the map drift with the registry — the same two-spellings-of-one-fact class
`-1` exists to close, re-created one layer down. `alpha` therefore reads the receipt, which is the
only record of what was taken, and no new seam is created: the derivation is a private helper with
one caller inside `cmd_update`.
