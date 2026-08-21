---
name: id-matched-as-a-substring
description: every id ending in a 1-up sequence is a prefix of nine others, so an unanchored match joins the wrong record
kind: class
universal: false
---

# `-1` is a prefix of `-10`, and the join is always wrong in the same direction

## Symptom

A check that joins a record to a commit, a roster to a ledger, or a declaration to its subject
returns the wrong pair. It does not error. It reports a clean, confident result about a unit that
never had anything to do with the evidence it was handed.

## Where it bit

This repo mints ids as `FAMILY-<slug>-<seq>` with a plain 1-up `<seq>`. A build with ten or more
units therefore contains `TOOL-dUnstalledConvoy-1` and `TOOL-dUnstalledConvoy-10` at once, and the
first is a substring of the second.

The closing review found five hand-written id tests across `tools/unattended/check-unattended.sh`
and three were unanchored:

- `grep -qF -- "$rsid"` against the baseline roster — an ADDED `-1` reads as already present
  whenever the roster carries `-10`, so an unrecorded scope change passes.
- `case "$subject" in *"$dsunit"*)` in the write-set check — pass `-1` is credited with `-10`'s
  commit, and its declared write set is graded against a diff it did not make.

Every one of these fails OPEN. The substring match makes the check believe it found what it was
looking for, so the arm that would have reported a violation never runs.

## The fix

Anchor on a token boundary, and write it ONCE:

```sh
id_rows() { printf '%s\n' "$1" | grep -E "(^|[^A-Za-z0-9-])$2([^A-Za-z0-9-]|\$)" || true; }
id_in()   { [ -n "$(id_rows "$1" "$2")" ]; }
```

The trailing class must exclude digits — that is the whole of the `-1`/`-10` case — and excluding
`-` as well keeps a hyphenated suffix from matching. `grep -w` is not enough: `-` is a word
character to some greps and not others, and the id contains two of them.

## The rule

A convention that says "anchor your id matches" was followed at two of five sites by the person who
wrote all five in one sitting. A helper is followed at five of five. When the same relation is
needed more than twice, the fix for getting it wrong is a function, not a resolution — the same
argument [[two-answers-to-one-question]] makes about facts, applied to predicates.

## Gate

Gated by construction rather than by a predicate: both id tests in
`tools/unattended/check-unattended.sh` now route through `id_rows`/`id_in`, so the anchoring exists in
exactly one place and a new site inherits it by calling the helper.

The arms that keep it honest are the `-10` fixtures in
`tools/unattended/check-unattended.test.sh` and `tools/unattended/unattended.test.sh`: a unit whose id
is a prefix of another's, exercised through the real join. They were observed RED against the
unanchored code before being trusted.

What is NOT gated is somebody writing a fresh `grep -F "$id"` beside the helper. That is the residual,
and it is why this record exists rather than the helper alone.
