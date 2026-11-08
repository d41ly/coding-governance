**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-15

# Edge-fix brief — the thirteen one-way §3 edges memory hygiene check 12 reports

`bash tools/memory-tree/check-memory-hygiene.sh` fails check 12 over the spec set: thirteen specs declare a
`**consumes-from**` edge in §3 whose sibling declares no matching `**hands-off**` edge back. Add each missing
`**hands-off**` bullet to the sibling's §3, in the shape the set already uses
(`- **hands-off** `TOOL-dCalibratedLens-<n>` — <what is handed, its tokens in backticks>`), and change nothing
else. The specs are unaudited at `rev-1`: edit them in place, with no rev bump and no §9 line.

The edges, consumer → the sibling that owes the bullet:

- units 4, 6, 8, 9, 10, 12, 14, 15, 16 and 17 consume from `TOOL-dCalibratedLens-3`;
- units 4 and 17 consume from `TOOL-dCalibratedLens-2`;
- unit 4 consumes from `TOOL-dCalibratedLens-15`.

For each one, read the consumer's `**consumes-from**` bullet and write the sibling's `**hands-off**` bullet as its
mirror: name the same tokens (functions, verbs, fields, constants) the consumer says it reads. Each token you put in
a hands-off bullet must already be named somewhere in the consumer's own spec, because `check-spec-tokens.py`'s
hands-off join reds a handed token the receiver never names. Where the consumer's bullet names a token the sibling's
own spec never defines, that is a disagreement on the interface axis (BUILD-METHOD M2): correct whichever of the
two documents is wrong, and say which in your return.

Do not commit, do not stage, and do not run the build-index generator or any gate; the main loop runs
`check-spec-tokens.py` and memory hygiene after you return. Return the thirteen bullets you added, by spec, and any
disagreement you corrected.
