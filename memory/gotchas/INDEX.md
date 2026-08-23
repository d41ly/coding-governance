# memory/gotchas/ — the recurring bug-class catalogue

One authored record per class. The table below is GENERATED from each record's front matter
and its DERIVED anchors — do not hand-edit between the markers.

Hand a reviewer the classes their diff can hit:

```bash
python tools/memory-tree/gotchas.py --for-diff <base>..<head>
python tools/memory-tree/gotchas.py --for-paths <path>...
```

<!-- BEGIN GENERATED -->

| Class | Kind | Anchors | Universal | Description |
|---|---|---:|---|---|
| [absence-assertion-over-whole-file-text](absence-assertion-over-whole-file-text.md) | class | 3 |  | a ban that greps whole file text reds on the comment documenting its own fix |
| [allowlist-narrower-than-the-root-it-guards](allowlist-narrower-than-the-root-it-guards.md) | class | 7 |  | a guard keyed on a path prefix denies the sanctioned destination too, because on this platform the sanctioned destination is INSIDE the prefix |
| [arm-literal-strands-on-message-edit](arm-literal-strands-on-message-edit.md) | class | 2 |  | editing a fail message strands its arm silently — the branch stays armed-looking, the count drops by one, and only the arms gate notices |
| [armed-but-unreachable-rule](armed-but-unreachable-rule.md) | class | 4 |  | a declaration can be non-empty, well-formed and still impossible to violate — testing that a rule EXISTS is not testing that it can FIRE |
| [assertion-between-two-derived-values](assertion-between-two-derived-values.md) | class | 4 |  | a check comparing two values the same code derives from one source is a tautology, and it arms cleanly |
| [bounded-through-a-pipe-is-unbounded](bounded-through-a-pipe-is-unbounded.md) | class | 6 |  | a wall-clock timeout captured through a command substitution bounds the verdict and not the clock, and reports success on schedule while the caller blocks |
| [concurrency-is-not-a-budget](concurrency-is-not-a-budget.md) | class | 3 |  | a per-item verify fan-out passes a concurrency cap and still spawns one agent per finding |
| [containment-tested-one-way](containment-tested-one-way.md) | class | 5 |  | a guard asking only "is this path under the protected one" refuses the narrow declarations and admits the one that claims everything |
| [fixture-inherits-ambient-machine-state](fixture-inherits-ambient-machine-state.md) | class | 2 |  | a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not |
| [fixture-passes-by-finding-nothing](fixture-passes-by-finding-nothing.md) | class | 1 | yes | a test arm whose fixture never triggers the rule passes, and proves nothing |
| [gate-green-by-accident-on-generated-bytes](gate-green-by-accident-on-generated-bytes.md) | class | 2 |  | a byte-compare gate over a generated file is CRLF-red on Windows and green only right after a render |
| [grammar-bound-to-the-wrong-root](grammar-bound-to-the-wrong-root.md) | class | 2 |  | a module-level grammar resolved at import describes the repo the KIT lives in, not the tree being classified |
| [heredoc-escape-reaches-the-regex](heredoc-escape-reaches-the-regex.md) | class | 0 | yes | source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem |
| [id-matched-as-a-substring](id-matched-as-a-substring.md) | class | 3 |  | every id ending in a 1-up sequence is a prefix of nine others, so an unanchored match joins the wrong record |
| [inputs-inside-the-subjects-reach](inputs-inside-the-subjects-reach.md) | class | 2 |  | a check whose inputs are all supplied by the thing it distrusts is not a check, however sound its logic |
| [pin-copied-from-another-corpus](pin-copied-from-another-corpus.md) | class | 2 |  | a threshold measured on one tree is vacuous or permanently red on another |
| [process-creation-is-the-suite-cost](process-creation-is-the-suite-cost.md) | class | 2 |  | a shell suite that is 93% not-CPU is paying an on-access antivirus scanner per exec, so its cost is spawn count and nothing in the code reads that way |
| [second-implementation-is-not-a-second-opinion](second-implementation-is-not-a-second-opinion.md) | class | 5 |  | a gate that recomputes the driver's answer from the driver's inputs confirms it rather than checking it, and the same hole opens at the READ path |
| [spec-names-code-its-base-lacks](spec-names-code-its-base-lacks.md) | class | 1 |  | a spec written from review records instead of from the code names machinery a commit ancestral to its own base already deleted |
| [staged-break-substitutes-a-synthetic-value](staged-break-substitutes-a-synthetic-value.md) | class | 1 | yes | an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value |
| [status-set-in-a-subshell](status-set-in-a-subshell.md) | class | 2 |  | a gate that prints FAILED from inside a pipeline sets a status the parent never sees, so it reports the violation and exits 0 |
| [structured-record-split-on-whitespace](structured-record-split-on-whitespace.md) | class | 1 |  | a multi-field record iterated with an unquoted shell expansion degenerates into its first field, and every assertion built on the later fields becomes unfalsifiable |
| [subprocess-resolves-a-different-shell](subprocess-resolves-a-different-shell.md) | class | 4 |  | Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem |
| [trace-profile-measures-itself](trace-profile-measures-itself.md) | class | 1 |  | a per-line set -x profile charges its own write overhead to the next line, so its seconds rank by call count and an optimisation aimed at them moves nothing |
| [trailing-comma-counted-as-an-element](trailing-comma-counted-as-an-element.md) | class | 5 |  | a counter scoring one-plus-every-top-level-comma reads a trailing comma as a real item, so every multi-line literal measures one too many |
| [two-answers-to-one-question](two-answers-to-one-question.md) | class | 6 | yes | a fact stated in two places drifts, and the copies need not disagree loudly to be wrong |
| [vacuous-selector-empty-population](vacuous-selector-empty-population.md) | class | 2 |  | a path selector that matches nothing prints nothing, and nothing is what a passing check prints |

27 record(s): 27 class, 0 note, 0 superseded · 4 universal · 0 unanchored

<!-- END GENERATED -->
