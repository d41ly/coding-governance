**Serves:** spec TOOL-dPromptedSeam-3

# TOOL-dPromptedSeam-3 — `--brief` calls nine unrelated concepts one concept, out loud

**Status:** OPEN · rev-2 · 2026-08-25 · node d · Tier-1 · base ee6554c3 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`--brief` exists to surface "one concept spelled two ways in two kits". For a third of the files
where it says anything at all, at least one thing it says is false: every identifier ending in a
stopword — `_of`, `_at`, `_in`, `_for`, `_with` — collapses into one object, and the report flags the
collection as a concept spelled many ways. Stop emitting the false rows, and stop silently dropping
the group it cannot describe. Supersedes `TOOL-dPromptedSeam-2`, whose premise was false.

## 2. Scope (IN)

- **S1 — a liveness predicate, stated as TWO rules with the set ENUMERATED.** A token is dead when it
  is in the set below OR is shorter than two characters. The set is 21 words, restated from
  `map_lib._STOPWORDS` because the layer ban forbids importing it, and written out here because the
  membership IS the contract:

  ```
  a an the to of in on for and or is be as at by from into with it this that
  ```

  An object is dead when every one of its tokens is dead. The length rule applies to the RAW
  subtoken, before any stemming, matching `map_lib.py:626-628`.
- **S2 — `run_brief` stops emitting a dead object as a multi-spelling row.** The `SPELLED MORE THAN
  ONE WAY` marker is withheld when the shared object is dead; the row itself may still print, but it
  may not claim the spellings are one concept.
- **S3 — the silently dropped group is REPORTED.** `lexicon.py:916` filters on the truthiness of
  `read_object`, so every single-token definition vanishes from the report with no line saying so.
  It gets a count and a name.
- **S4 — arms, and one of them is honestly synthetic.** A dead-by-membership case, a dead-by-length
  case, a live control, and a no-object control. The length arm is SYNTHETIC and must say so: the
  only identifier in this repo that exercises it is `boundedK` in `tools/hooks/agent-cap.js`, which
  is JavaScript and outside the Python corpus these arms walk.

## 3. Non-goals (OUT)

- **`read_object`'s return contract does not change.** It returns the joined tail or `""`, exactly as
  today. The liveness verdict is a SEPARATE named helper taking the identifier, because the returned
  string cannot distinguish "no object" from "dead object" — both would have to be falsy.
- **No stemming.** The predicate asks whether a token survives, never what it reduces to.
- **No cross-kit call and no import of `map_lib`.** `.lexicon.conf` declares that direction
  forbidden.
- **No full-identifier fallback.** `TOOL-dPromptedSeam-2` proposed one; nothing in this kit performs
  a lookup that could consume it.
- **No change to P1, P2 or P3.** `leading_verb` is untouched and no pin moves.

## 4. Design

**D1 — the before-state, pasted rather than described.** `python tools/lexicon/lexicon.py --brief
tools/lexicon/lexicon.py` prints today:

```
  of: openers x2 (off-table), cache x1 (off-table), ext x1 (off-table), index x1 (off-table),
      message x1 (off-table), owners x1 (off-table), parent x1 (off-table), pin x1 (off-table),
      token x1 (off-table)  <-- SPELLED MORE THAN ONE WAY
```

Nine unrelated functions, asserted to be one concept, because each ends in `_of`.

**D2 — the measurement, and the model it uses.** `run_brief` joins the TARGET's objects against
CORPUS-wide spellings (`lexicon.py:916` for the target, `:936` for the corpus), so neither
"rows inside one file" nor "identifiers repo-wide" is the population. Measured under the model the
code computes, over every tracked `.py` file as a target in turn: **31** targets emit any
multi-spelling row, and **11 of those 31 (35%)** emit at least one FALSE row. `map_lib.py` emits two
(`of`, `in`); `govkit.py` two (`for`, `at`); `lexicon.py` one (`of`).

Two earlier revisions of the superseded unit measured this over the wrong population twice — 231
off-table symbols, then 644 distinct function names — and both figures were reported as the design's
premise. The number above is the third attempt and the first one taken under the model
`run_brief` actually uses. That history is why D1 pastes output instead of quoting a percentage.

**D3 — the verdict is a helper on the IDENTIFIER, not a property of the return.** Signature:
`read_object_state(name) -> "live" | "dead" | "none"`. `run_brief` branches on it. Putting it on the
return value cannot work: `""` and a dead object would both be falsy, which is the collapse this unit
exists to undo.

**D4 — withheld marker, not a withheld row.** A dead object still tells the reader something — that
several names share a stopword tail — so the row may print. What it may not do is claim they are one
concept. Deleting the row would hide a real observation to fix a wrong label.

## 5. Production-readiness checklist

- **security** — N/A. Pure string predicate over an identifier.
- **perf / scale** — N/A. One set membership and one length test per token, on a path that already
  walks the corpus.
- **a11y** / **i18n** — the ASCII limit in `subtokens` is untouched and stays
  `TOOL-dScaffoldedMirror`'s carried finding.
- **error / empty / loading states** — the three states of D3 ARE this line.
- **observability** — `--brief` prints the change; there is no state.
- **risks** — low, and bounded to one report. The one real risk is the stopword set drifting from
  `map_lib`'s; §8 Q1 owns it.
- **testing + left-shift gates** — S4, on `lexicon selftest`. That leg is `subject = "kit"` and is
  HELD unless `GATE_SELFTESTS=1`, so these are on-demand arms rather than every-bar coverage, and
  this line says so rather than letting §7 read as more.
- **migration / rollback** — none.
- **user docs** — `LEXICON.md`'s `--brief` paragraph gains one sentence.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --brief tools/lexicon/lexicon.py` runs, the `of:`
  row no longer carries `SPELLED MORE THAN ONE WAY`, and the four live rows in that same output
  still do. A build that suppresses the marker everywhere fails the second half.
- **AC2** — When `read_object_state` is asked for `pin_of` it answers `dead`, for `build_index`
  `live`, and for `main` `none`. Three distinct answers; a two-valued helper cannot pass all three.
- **AC3** — When `python tools/lexicon/lexicon.py --brief tools/lexicon/lexicon.py` runs, its output
  names the count of definitions with no object at all, and that count is non-zero for this file —
  `_main`, `run`, `extract` and others are single-token.
- **AC4** — When the length half of S1 is reverted in a scratch copy, `python tools/lexicon/selftest.py`
  reds naming the SYNTHETIC length arm; when the membership half is reverted it reds naming the
  membership arm. Two reverts, two distinct arms, so one rule cannot stand in for the other.
- **AC5** — When `python tools/lexicon/lexicon.py --check` runs, the three OFFENDER counts are
  unchanged from base `ee6554c3` (381 / 0 / 0), and `P1 verb graded` has risen by exactly the number
  of definitions this unit adds — 866 to 868. rev-1 of this spec pinned `graded=866` as "unchanged",
  which a unit that adds two functions can never satisfy: the criterion was false on the commit that
  satisfied the unit. Offenders are what "no predicate moved" actually means; graded is a count of
  the corpus and this unit grows it on purpose.

## 7. Gates

Adds no leg. Rides `lexicon selftest` (S4's arms, HELD by default as §5 records) and `lexicon naming
predicates` (AC5). `--brief` has no gate of its own and this unit does not add one: its output is a
report a human reads, and gating a report's prose is how a report stops being changeable.

## 8. Open questions

- **Q1 — must the inline set EQUAL `map_lib._STOPWORDS`, or may it be a subset?** RESOLVED (agent,
  2026-08-25, delegated): EQUAL, and the docstring says so, because a subset would make the two kits
  disagree about the same word silently. Nothing gates the pair — the layer ban forbids the import
  that would let a parity check read both — so the docstring is the only carrier and it names that
  limitation rather than implying coverage.
- **Q2 — should a dead-object row print at all?** RESOLVED (agent, 2026-08-25, delegated): yes,
  without the marker, per D4. Deleting it would hide a true observation to fix a false label.

## 9. Revision log

- rev-2 · 2026-08-25 · node d · OPEN. AC5 corrected DURING the build that satisfied it: it pinned
  `graded=866` as unchanged, and this unit adds two definitions, so the criterion was false on the
  very commit meant to pass it. Offenders unchanged is what "no predicate moved" means; graded is
  a corpus count this unit grows deliberately. Caught by running the check rather than reading it.

- rev-1 · 2026-08-25 · node d · OPEN. Supersedes `TOOL-dPromptedSeam-2`, which was retired WONTDO
  after spec-audit round 2 proved its premise false: it claimed `read_object` returns empty for two
  reasons and that both vanish from `--brief`. It returns empty for one reason, and the other case is
  loudly reported and wrong. This unit is written from the pasted before-state rather than from a
  description of it, which is the one discipline that would have caught all three premise errors this
  build has now made.

## 10. Reuse audit

- `read_object()` (`tools/lexicon/lexicon.py:856`) — READ, not changed. Its contract is a §3 non-goal.
- `subtokens()` (`tools/lexicon/subtokens.py`) — REUSED unchanged; the predicate reads its output.
- `map_lib._STOPWORDS` + the `len(t) >= 2` rule (`tools/codebase-map/map_lib.py:583-628`) — RESTATED,
  not imported, because `.lexicon.conf` forbids that direction. Q1 records that nothing can gate the
  restatement and why.
- `run_brief` (`lexicon.py:910-945`) — EXTENDED at its two existing join points rather than rewritten.

**Recall terms used**, shared with the build's other units per M5: `lexicon subtokens port
self-contained layers import ban codebase-map map_lib kit independence adopter reuse seam`. The map
probe's behaviour phrase was *"reduce an identifier to the concept it names, dropping the leading
verb"*; it returned `leading_verb` as the only seam in this area, confirming no third implementation
exists to extend instead.
