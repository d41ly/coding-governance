---
name: grammar-bound-to-the-wrong-root
description: a module-level grammar resolved at import describes the repo the KIT lives in, not the tree being classified
kind: class
universal: false
---

# A grammar that recognises nothing produces the same output as a clean corpus

## Symptom

A classifier reports a scratch corpus as CLEAN. Every check passes. Nothing is wrong with the corpus
and nothing is wrong with the checks — the grammar matched zero ids, so the classification was empty,
and an empty classification is exactly what a clean corpus produces.

## Cause

`tools/memory-recall/extract.py` binds its conf at IMPORT time and anchors on its OWN file, which is
correct for its CLI and deliberate. A caller classifying a different tree inherits the wrong family
alternation, and no working-directory change can move it.

## The fix

`grammar_for(root)` — one accessor, so there is still ONE grammar and it can be bound to an explicit
root. `tools/memory-tree/corpus_ids.py` calls it with the tree it is classifying.

Gated by `tools/memory-tree/corpus_ids.py --selftest`, whose scratch fixtures use a family the host
repo does not declare, so a re-binding regression makes every id arm fail rather than pass silently.
