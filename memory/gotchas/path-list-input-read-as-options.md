---
name: path-list-input-read-as-options
description: a program reads file names one per line from a list input that also takes options or splits on a line break, so a tracked name opening a dash or holding a line break arrives as an option or as two names
kind: class
universal: false
---

# A tracked name on a list input arrives as an option or as two names

## Symptom

A program reads a list of file names, one per line, from a list input: `ctags -L -`, a `git cat-file --batch`
request stream, an `xargs` argv. That input also takes options, or splits on a line break. A tracked name is
whatever a committer chose, so a name opening `-` arrives as an option, and a name holding a line feed arrives as
two names. On a batch stream every later request then reads the answer meant for the one before, and git drops a
closing carriage return, so a request naming `ok.py` and a CR reads another file's bytes.

## Where it bit

The dTotalRecall closing review, round 3, of 2026-11-26
(`memory/builds/dTotalRecall/reviews/2026-11-26-review-TOOL-dTotalRecall-122-closing-diff-review-round3.md`,
finding 2). `tools/playbook/code_record.py#read_ctags_defs` wrote each tracked path to ctags's `-L -` input bare,
so a tracked `-fZ.go` set a ctags option. One input further on, `tools/memory-tree/tree_lib.py#read_blobs_at`
wrote a `kit.toml` path holding a line feed to `git cat-file --batch` as two requests, and every later request read
the header pushed down to it (TOOL-dTotalRecall-124). Before it, `TOOL-dQuietDisk-37` S9 met the carriage-return
instance in govkit's `tools/govkit/upgrade_steps.py#blob_at` batch handle, which that review classed
`two-answers-to-one-question`.

## The fix

- Prefix each name so it cannot open `-`: a dot and a slash before the path, which no option opens.
- Read any name holding a line feed or a carriage return off a line-split input, through its own one-shot call.
- Or use a NUL-ended input where the program has one, as `git check-attr --stdin -z` is.
- Plant one name per shape, each seen red with its guard cut.

## Gated by

`tools/playbook/code_record.py`, whose `ctags list input` arm plants `-fZ.go`, a line-break code path and a
line-break `kit.toml`, for `read_ctags_defs` and `tree_lib.read_blobs_at` alone. Ungated: the sites
TOOL-dTotalRecall-124 §4 "The call sites" leaves open, which are `tools/codebase-map/map_diff.py`'s own
`cat-file --batch`, `tools/drift-audit/drift_report.py`'s held-open batch, `tools/check-wiring.sh`'s newline-ended
`check-attr --stdin`, and govkit's `derive_kit_attestations` `--batch-check` lines, the owner's ask
`TOOL-dQuietDisk-41`.

## What this does NOT say

- It does not cover a pathspec read from a file: pathspec magic is a neighbouring class, not a path read as an option.
- It coexists-with `read-allowlist-admits-a-writing-option`: there a classifier reads a call's own option as a
  read; here no option was typed, and a tracked name on a list input becomes one.
