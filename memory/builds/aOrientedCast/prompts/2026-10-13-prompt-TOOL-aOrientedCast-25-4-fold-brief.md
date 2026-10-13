**Serves:** journal TOOL-aOrientedCast-25

# Brief record — fold TOOL-aOrientedCast-25 on its builder's second divergence

## The prompt

TOOL-aOrientedCast-25's second build attempt returned `committed: false`: its spec's §4 "The source
refusal" (S7), the `fail 9` bullet, cannot be built without turning the `shell hygiene (a loop fed by
a command substitution)` leg red.

## The brief

### Goal

TOOL-aOrientedCast-25's `fail 9` check is specified in a form the shell-hygiene registry admits, so
the unit builds green on every leg its §7 names.

### Items

1. **Respecify the `fail 9` bullet of §4 "The source refusal".** As written, it reads each head that
   `sort | uniq -d` prints in a heredoc-fed loop "as the loop reads `$defs`". But
   `tools/gate-lint/sh_hygiene.py` already counts the `$defs` loop as substitution-fed (class
   `loop-var-sub`, through its one-hop follow), and `memory/project/substitution-fed-loops.txt` pins
   `tools/check-microformats.sh EOF 2`, a count that may fall and may not rise. Any new heredoc-fed
   loop over that output adds a third site. The builder probed a form that adds no loop: inside the
   existing per-definition loop, check each head against the newline-joined list of heads already
   seen with a fork-free `case`; a head's second definition takes `fail 9` with the same message, and
   a second list of reported heads stops a third definition from reporting it again. Specify that
   form, or the scratch-file form the leg itself suggests, by M3. Keep the file at exactly its two
   registered sites, and add a criterion that observes the count stays at two.
2. Change any criterion that quotes the old wording to match.
3. Bump the rev with its §9 line. The spec sits near the 49152-byte ceiling; trim if the change needs room.

### Acceptance

`python tools/check-spec-tokens.py` reports no hit on the spec, its size included, and the new form
keeps `tools/check-microformats.sh` at its two registered substitution-fed sites.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.

### Non-goals

- Any change to the unit's other scope items.
- Any spec other than TOOL-aOrientedCast-25's.
