**Serves:** research TOOL-aScoutedSeam-3

# The enumerated-coverage prompt — how T1's prompt was written, and why it beat effort

T1 (`2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2-trial.md`) took the diff-time reuse check at `medium`
from 4 of 23 to 14 of 23, past D1 at `extra` (7 of 23), with no change of model, tree or diff. This
record states the method as a recipe, so a later prompt can be written to it. The instrument that applies
it is `-1-10-d1v2.py`, and the T1 handoffs under `prompts/` are worked examples.

## The failure it fixes

D1 asked one open question: does this diff re-implement something the tree already has? An open
question invites one answer. The reviewer stopped at its first duplicate, or concluded "clean" once it
had looked at the parts it found interesting. Effort only changed how long it searched before it
stopped. That is why `medium` lost three of `extra`'s seven cases. It found less, and it did not reason
worse about what it found.

## The recipe

1. **Enumerate the population outside the model.** A deterministic lister produces every item the
   question is about, here every unit the diff adds. The model is handed the list, not asked to find
   it. Coverage then becomes checkable: a row per item, or the review is incomplete.
2. **Give every item an escape.** The verdict vocabulary is closed and includes an artefact verdict
   (`not-a-unit`). A noisy list then costs a row, not a false finding.
3. **Demand one row per item, in order.** Each row carries a fixed set of fields. The verdict comes from
   a closed set: `duplicate`, `should-extend`, `new` or `not-a-unit`.
4. **Make each row prove its search.** A row's `nearest` field is either an existing `path::symbol`, or
   `none` plus what was searched. A negative must show its work, and the model must search the concept
   with synonyms across all file types, not the name.
5. **Name the failure mode in the prompt.** "Do not stop at the first duplicate. A review that leaves a
   listed unit without a row is incomplete."
6. **Keep the open search, labelled.** After the list, the model adds rows for what the lister cannot
   see: repeated literals, hardcoded design values beside a token, renamed copies of a body, rebuilt
   JSON nodes. Each one is marked `added`, so judgement is kept apart from coverage.
7. **Derive the binding from the verdict.** The machine-readable return contract comes last. MUST means
   `duplicate` and SHOULD means `should-extend`. The model does not choose a binding separately from its
   verdict.
8. **Bound the list.** At most 60 items are listed, followed by "... and N more; cover them as you read",
   so the prompt stays bounded on a large diff.

## Where else it applies

Any agent question whose answer is "every X that has property P" can be written this way: lister for
X, row per X, verdict for P. Two candidates in this build:
- **The pre-spec scout** (TOOL-aScoutedSeam-1) has no diff to list, but it could list the needs its
  framing finds, or a spec's data-model fields, and demand a nearest seam per need. This is untested.
- **A closing diff review lens** has the same population as T1.

## What it does not establish

- **No ablation.** T1 changed the lister, the per-row verdict, the no-stop line and the return contract
  together, so it does not say which of them carried the gain.
- **More volume.** Seams rose from 34 to 130 and MUSTs from 3 to 30. A blind judge reads their precision
  in the next step of this build.
- **One corpus, one run.**
