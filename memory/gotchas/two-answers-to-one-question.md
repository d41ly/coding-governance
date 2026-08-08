---
name: two-answers-to-one-question
description: a fact stated in two places drifts, and the copies need not disagree loudly to be wrong
kind: class
universal: true
---

# One fact, one home

## Symptom

A value is declared twice — a pattern in a shell gate and the same pattern in a Python module, a
status in front matter and a status derived from records, a set transcribed from one script into
another. The copies drift. Often neither is obviously wrong; they simply answer slightly different
questions.

## Where it bit

Upstream typed the declares-a-gate alternation twice and the two disagreed on scope: the shell
grepped the whole file while the module searched only the body, so a description carrying the word
gated satisfied one and not the other. Upstream also transcribed a byte-capped index set from shell
into Python and had to guard the transcription in BOTH directions, because a shell-side addition the
Python side still excluded left a file under no cap at all.

Here, `tools/memory-tree/SPEC-TEMPLATE.template.md` described a nine-section canon while the
installed copy and the gate had required ten for four days. Nothing connected them.

## The fix

Ask, do not copy. `tools/memory-tree/check-memory-hygiene.sh` owns the append-only set and the index
set and prints them on demand; `tools/memory-tree/corpus_ids.py` asks. The id grammar lives in
`tools/memory-recall/extract.py` and is imported. `tools/memory-tree/gotchas.py` exposes a single
declares predicate. Where a fact genuinely has two possible sources — a build status derived from
specs versus declared in front matter — one is an ERROR whenever the other is available.

Gated by `tools/memory-tree/kit-dogfood-parity.test.sh` for the document pair, and by construction
elsewhere: the second copy does not exist.
