# memory/gotchas/ — the recurring bug-class catalogue

One authored record per class. The table below is GENERATED from each record's front matter
and its DERIVED anchors — do not hand-edit between the markers.

Hand a reviewer the classes their diff can hit:

```bash
python tools/memory-tree/gotchas.py --for-diff <base>..<head>
```

<!-- BEGIN GENERATED -->

| Class | Kind | Anchors | Universal | Description |
|---|---|---:|---|---|
| [absence-assertion-over-whole-file-text](absence-assertion-over-whole-file-text.md) | class | 3 |  | a ban that greps whole file text reds on the comment documenting its own fix |
| [fixture-passes-by-finding-nothing](fixture-passes-by-finding-nothing.md) | class | 1 | yes | a test arm whose fixture never triggers the rule passes, and proves nothing |
| [gate-green-by-accident-on-generated-bytes](gate-green-by-accident-on-generated-bytes.md) | class | 2 |  | a byte-compare gate over a generated file is CRLF-red on Windows and green only right after a render |
| [grammar-bound-to-the-wrong-root](grammar-bound-to-the-wrong-root.md) | class | 2 |  | a module-level grammar resolved at import describes the repo the KIT lives in, not the tree being classified |
| [pin-copied-from-another-corpus](pin-copied-from-another-corpus.md) | class | 2 |  | a threshold measured on one tree is vacuous or permanently red on another |
| [subprocess-resolves-a-different-shell](subprocess-resolves-a-different-shell.md) | class | 1 |  | Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem |
| [two-answers-to-one-question](two-answers-to-one-question.md) | class | 6 | yes | a fact stated in two places drifts, and the copies need not disagree loudly to be wrong |
| [vacuous-selector-empty-population](vacuous-selector-empty-population.md) | class | 2 |  | a path selector that matches nothing prints nothing, and nothing is what a passing check prints |

8 record(s): 8 class, 0 note, 0 superseded · 2 universal · 0 unanchored

<!-- END GENERATED -->
