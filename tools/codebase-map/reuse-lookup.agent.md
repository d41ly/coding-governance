# reuse-lookup — agent instruction (behaviour -> seam)

**When:** before building any non-trivial new behaviour (a Definition-of-Ready step). The goal is
convergence: wire the new work through a seam that already exists instead of reinventing one that
drifts into a permanent island. This is the semantic half of `codebase-map`'s reuse layer — the CLI
assembles a candidate shortlist, and YOU decide from it.

## Run it

```
python codebase-map/reuse_lookup.py "<one sentence describing the BEHAVIOUR you are about to build>"
```

Describe the behaviour, not a name you already picked — say "turn a display name into a url-safe
slug", not "add a slugify2". The tool matches token stems, so a good behavioural phrase surfaces
seams whose names you would never have guessed.

## Read the output

The CLI prints a ranked shortlist, not an answer:

- **candidates (ranked)** — each line is `name  [kind | file | fan-in N | SEAM]  (why it is listed)`.
  - **seeds** (top of the list) share a token stem with your query.
  - **neighbours** live in the same file or are the same kind as a seed — the tool widens beyond a
    literal name match on purpose (a pure top-K lexical cut has ~0% behavioural recall).
  - **SEAM** marks a symbol whose fan-in is at/above the repo's threshold — a hot, already-reused
    seam. Prefer wiring through a SEAM over a cold symbol.
- **sources to open** — the def files / dossiers / inventories behind the candidates. **Open them.**
  The shortlist is a pointer set; the decision needs the actual code and the dossier's
  `## Reuse affordance` / `## Shared seams` prose.

## Decide

After reading the sources, do exactly one of:

1. **Wire through a seam.** Extend the existing symbol (via the extension point its affordance line
   names) instead of writing a parallel one. Record it in your feature's `## Reuse affordance`:
   `seam: <id> — reuse for <need>; extend via <point>`.
2. **Build new — deliberately.** If nothing fits the behaviour, that is a legitimate answer: reply
   `no seam fits` and record `none — <why feature-specific>` in the dossier's `## Reuse affordance`.
   The point is a recorded decision, not a forced reuse.

## Heed the partial-recall notice

If the output ends with `recall partial: layers X, Y have no symbol extractor`, those layers are
**recall-dark** (declared in `.codebase-map.conf` `RECALL_DARK_LAYERS`) — their symbols are NOT in the
corpus. A `no seam fits` is then **not** authoritative: check those layers by hand before concluding
nothing exists. An empty shortlist plus recall-dark layers means "I could not see everything", never
"nothing is there".

## Ceilings (so you trust it correctly)

- The stemmer is crude (no NLP): it will miss synonyms and irregular plurals. That is precisely why a
  human/agent read follows the shortlist — the tool recalls candidates, you judge behaviour.
- Fan-in is an import/identifier heuristic, not a resolved call graph: it over-counts common names and
  under-counts registry/dynamic-dispatch seams (which look cold but are heavily reused). Treat fan-in
  as a ranking hint, not ground truth.
- The lookup is **advisory** — it never fails a build. The closing loop that catches reinvention you
  shipped anyway is `map_diff --converge` at review time.
