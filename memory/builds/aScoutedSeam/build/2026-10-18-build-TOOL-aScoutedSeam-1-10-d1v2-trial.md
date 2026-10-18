**Serves:** research TOOL-aScoutedSeam-3 TOOL-aScoutedSeam-1

# The T1 trial — an enumerated, per-unit diff check at `medium` solves 14 of 23

Run 2026-10-18 on node `a`. It answers the owner's ruling on TOOL-aScoutedSeam-3 fork F2: measure, and
say why `medium` lost cases. The hypothesis put forward was that the loss came from the prompt's
composition, not from effort. D1 asked one open question, so the reviewer returned one verdict. It
stopped at its first duplicate, or called the diff clean. Medium lost 3 of extra's 7 solved cases that
way.

```bash
B=memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1
python $B-4-bench.py compare $B-3-cases.json $B-5-results.json d1 d1@medium d1v2@medium
```

## What changed from D1

- **A deterministic lister.** `-1-10-d1v2.py units <diff>` lists every unit the diff adds in product
  files: defs, consts, shell functions, constants, CSS custom properties and rules (CSS patterns only in
  style files), schema fields and JSON tree keys. It drops nothing under memory, docs or tests. A hunk
  that adds four or more lines and names no unit is listed as a `hunk` unit, so logic added inside an
  existing function is still listed. The list is capped at 60, with a count of the rest.
- **One verdict per unit.** For each listed unit the reviewer returns the nearest existing
  implementation and one of `duplicate`, `should-extend`, `new` or `not-a-unit`. It then adds rows,
  marked `added`, for duplicates the lister cannot see: a repeated literal, a hardcoded design value, a
  renamed copy of a body, a rebuilt JSON node.
- **No early stop.** The prompt says a review that leaves a listed unit without a row is incomplete.
- **The return contract.** It is M1c's seam shape, with MUST for a duplicate and SHOULD for
  should-extend.

The 23 questions were built by `-1-10-d1v2.py questions` from the same frozen pre-diff trees and diffs
as D1. Each ran as a typed `gov-reuse-scout` at `medium`, from a handoff rendered against an empty card.
The handoffs are under `prompts/` as `2026-10-18-prompt-DEPL-aScoutedSeam-1-13` to `-35-reuse-scout.md`.
The replies were collected as `d1v2@medium` by `-1-9-m1d-trial.py collect`, and all 23 parsed.

## Results, by the path matcher, same 23 cases

| arm | solved | items hit | seams | MUST |
|---|---|---|---|---|
| D1, `extra` | 7 of 23 | 13 of 57 | 52 | 12 |
| D1, `medium` | 4 of 23 | 9 of 57 | 34 | 3 |
| T1, `medium` | 14 of 23 | 19 of 57 | 130 | 30 |

**T1 kept every case either D1 arm solved.** It added seven cases that neither arm solved: product
card image, email image, medical intake gilded, lexicon subtokens, warded terminal, batched launcher and
medical intake restage. Warded terminal's `PHASES_TERMINAL` had not been bound by any arm, pre-spec or
diff-time.

**Four of the nine misses are the matcher's, not the reviewer's.** Read case by case:
- **Marker index:** T1 bound `apply_region._is` at MUST, and the ground truth names `apply_region`.
- **Row grammar:** T1 bound the five `load_conf` copies through `corpus_ids.py`, a sibling the ground
  truth does not list.
- **Deferred settings:** T1 bound `check-wiring.sh` (`json_str`, `wired`), and the ground truth names
  other symbols in the same file.
- **API carousel:** T1 bound `product-carousel-live`, the ground truth's second item, and missed the
  primary, `gen_product_card.py`.

**Five misses are real.**
- **inCMS design data and hero accents:** neither reached `imageField`. The design-data case has been
  missed by every arm.
- **NicoCares account area:** T1 found the rail, steps and token copies, not the eyebrow recipe or the
  section width.
- **Reaped census:** T1 named `scan_descendants` and judged it unreachable from a copy-installed kit.
- **Declared git common dir:** the diff is a spec set with no product unit, so a diff-time check cannot
  see it.

## What this decides

1. The hypothesis holds on this corpus. At the same effort, enumerating the units and demanding a row
   for each took `medium` from 4 to 14, past `extra`'s 7. The loss was the prompt's single-answer shape,
   not effort. TOOL-aScoutedSeam-3 F2 can rule `medium` with the enumerated prompt, instead of `high`
   with D1's.
2. The cost is volume. Seams went from 34 to 130, and MUSTs from 3 to 30. No control case exists in the
   diff corpus, so this trial measures no precision. A blind judge or a cap is owed before the volume is
   shipped to a builder.
3. The lister is part of the treatment. The trial changed the enumeration, the per-unit verdict, the
   no-stop line and the return contract together, so it does not say which of them carried the gain.

## Confounds and limits

- **Runner.** T1 ran as typed role agents carrying the role body, its rule and gov's Facts block. D1
  ran as plain Workflow agents. The model was `claude-opus-5-5` for both, read from the session
  transcript.
- **Contamination.** Gov's Facts block names `resolve-python.sh`, which is batched launcher's ground
  truth. T1 solved that case, and M1d, run under the same block, did not.
- **Matcher.** The figures are the path matcher's, so the four matcher misses above are not counted as
  solved.
- **One run.** T1 ran once, on 23 cases. Wall time ran from 19 s to 4 min 57 s, and output tokens from 1.7k
  to 24.1k per case, as the roles kit's `agents` verb reads them.
