---
name: a-spelling-change-strands-its-readers
description: a shared file changes how it SPELLS its values, the readers someone migrated resolve the new spelling, and every reader nobody listed compares the raw one and matches nothing
kind: class
---

# A spelling change strands the readers nobody listed

## Symptom

A shared declaration file changes how it spells a value: a path becomes `{prefix}/x.sh` instead of
`tools/x.sh`, a carrier becomes `${MT_DIR}/check-memory-hygiene.sh`, a descriptor path gains the
same token, a `home` becomes kit-relative. The readers the change was written for resolve the new
spelling and stay green. Every other reader keeps comparing the value as it is written, and the
written value now names nothing.

Nothing errors. A reader that compared the value against a population reports a false red, which a
held suite hides; one that grepped for it matches nothing and reports `ok`; one that read it as a
path gets an empty file and `continue`s. The first two are loud only when their suite happens to run.

## Where it bit

`aRepatriatedFork`'s round-1 closing diff review, where eight of twelve confirmed findings were this
one migration. `tools/gate-legs.json` moved to the `{prefix}` token and the run-gates canary's
guard arm read 114 guards as untracked while its hardcoded-path arm could no longer fire.
`tools/check-kit-versions.sh` moved to resolver-fed `${XX_DIR}` carriers and govkit selfcheck 5b
turned into 28 notes of noise. `tools/govkit/registry.toml` moved its descriptors to the token and
the adopter-fixture regenerator read every one as empty and returned no homes. The playbook
renderer's bar deriver read `prefix` from the `[answers]` table when intake writes it at the top.

## Cause

A migration's inventory is built by asking where the value is RESOLVED, because that is the code
the change has to edit. A reader that only COMPARES the value, greps for it or hands it to another
program resolves nothing, so it is not in that inventory. It is the same blindness as
`retirement-inventory-misses-readers-by-value.md`, turned on a spelling instead of a deletion.

## The fix

Resolve at the reader, through the one canonical resolver for that spelling
(`tools/lib/resolve_prefix_token.py`, `tools/lib/resolve_kit_dir.py`), inlined where the kit cannot
import. And give each reader a liveness assertion over what it resolved: every value names a tracked
path, or no value still carries the token. A reader that resolved nothing then reds instead of
reporting a clean pass over a population of spellings.

## How to see it before shipping

Before landing a change to a shared file's spelling, list every tracked file that NAMES that file
and every program that is handed a value read from it, not only the ones that parse it. For each,
ask what it does with the value: resolve, compare, grep or open. Every compare, grep and open needs
the resolution too.

## A renumber is a spelling change

`TOOL-aGraftedHelix-32` (the closing review of that build, L4). The run-claim refusals in
`tools/unattended/unattended.sh` moved from checks 89 to 93 up to 107 to 111 before a merge brought
in other checks at 89 and 90. The renumbering commit built its inventory from the driver, its
suites, the confs and the templates, and exempted only the build records, so the codebase map's
`memory/map/features/unattended-stops.md` went on sending a reader of the claim refusals to two
unrelated live checks. A check number is a value other files spell, and a renumber strands every
reader that spells it in prose. The documented check for a renumber: grep the whole tracked tree for
each old number in that check's context, excluding only the build records, which are history,
and list every hit in the commit message, fixed or left with a reason.

## Detection

No machine gate. The candidate predicate, "a file naming the manifest carries the resolver block or
declares that it reads the raw spelling", was run over the tree first. Measured at `7de665e5`:
30 tracked scripts named `tools/gate-legs.json` outside a comment and 6 carried the resolver. Most
of the other 24 are suites writing their own fixture manifests, where the raw spelling is correct,
the near-misses that sink the predicate. It also cannot see a reader handed the value through a
variable or an argument. A per-file declaration would be a list of claims nothing checks. The documented check is the inventory above, run by a closing review
over any diff that changes a shared file's spelling, plus the liveness assertion in each reader.
