---
name: hand-typed-count-of-an-enumerated-population
description: prose types the size of a population that code beside it enumerates, and the count goes wrong when a row is added or a sentence is rewritten around it
kind: class
universal: false
---

# A typed count of rows the code already lists

## Symptom

A comment or a help line says "those four" or "these six" about a list that the code right beside it
enumerates: `run_one` rows, legs in a manifest, arms in a table. The number is a second copy of a
fact the rows already state. A row is added, or the sentence is rewritten around it for another
reason, and the number stays. The prose then disagrees with the code it sits on, and nothing reads
the number, so nothing reds.

## Where it bit

The aShelvedLeg closing review, round 1 item 4. The `--checks` comment in
`tools/unattended/run-unattended-gates.sh` said "those four are REPOSITORY checks" above five
`run_one ... checks` rows. TOOL-aShelvedLeg-1 had just rewritten that same sentence to say the kit
gate is held, and kept the count. TOOL-aShelvedLeg-2 replaced the count with the rows' own name.
The file's header already records the same lesson for the list of names the count replaced.

## The fix

Name the population, not its size: "the `run_one ... checks` rows above". Where a count is the point,
derive it at run time from the rows and print it, never type it.

## Gate

There is no machine gate for this. A count word in prose cannot be bound to the population it
describes without parsing the sentence, and most count words in comments are about something else.
A reviewer reads every typed count in a changed sentence against the rows beside it.
