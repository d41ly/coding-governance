---
name: structured-record-split-on-whitespace
description: a multi-field record iterated with an unquoted shell expansion degenerates into its first field, and every assertion built on the later fields becomes unfalsifiable
kind: class
universal: false
---

# A record with spaces in it, read by a loop that splits on spaces

## Symptom

A table of `field|field|field` rows lives in one shell variable and is iterated `for row in $TABLE`.
Word-splitting cuts each row at every space, so the loop body sees fragments rather than rows. The
first fragment still looks like a row — it starts with the key — so the lookup that matches on the key
keeps working, and only the LATER fields are wrong. Every assertion built on them becomes
unfalsifiable while continuing to look exactly like a working one.

## Where it bit

`tools/unattended/check-unattended.sh`, check 28b's key-exemption table. Rows are
`key|file|literal-that-must-still-be-present`, and the literal is a `grep -oE` invocation with spaces
in it. `for _e in $KEY_EXEMPT` split it into three tokens, so the parsed literal was the 4-byte string
`grep` — present nineteen times in the file the row names. The freshness assertion therefore had no
failing input at all: it could not detect a rewritten reader, which is the only thing it existed to
detect. Found in round 6 of the `dScriptedRepeat` diff review; the rule it guards is the one covering
the single template key no parser reads.

## The fix

Hold the table newline-separated and read it with `while IFS= read -r row`, which splits on nothing but
newlines. In `tools/unattended/check-unattended.sh` that is a `KEY_EXEMPT=$(cat <<'EOF' … EOF)` and a
`done <<EOF\n$KEY_EXEMPT\nEOF` around the lookup.

Mechanically detectable: a `for <var> in $<NAME>` whose `<NAME>` is assigned a value containing a
space is the whole class. There is NO MACHINE GATE for it in this tree — the predicate would have to
resolve an assignment across a heredoc to know whether the value holds a space, and nothing here does
that today. It is a documented check: when a shell table grows a second field, read it with
`while IFS= read -r`.

## The half that made it survive review

The staged break that was supposed to prove the freshness assertion could fail replaced the shipped
row with `legs|check-playbook.sh|THIS_LITERAL_IS_GONE` — a value with no spaces in it, which cannot
exhibit a split. The arm passed green over a vacuous construct for a whole round. See
[staged-break-substitutes-a-synthetic-value](staged-break-substitutes-a-synthetic-value.md).
