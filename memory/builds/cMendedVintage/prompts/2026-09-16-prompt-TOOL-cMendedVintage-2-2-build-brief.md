# Build brief — TOOL-cMendedVintage-2

**Serves:** journal TOOL-cMendedVintage-2

gate-lint stops writing into the adopter's memory tree. Read the spec whole first.

*Standing note: briefs in this build have carried four claims measurement disproved. Anything below
I have not run is marked UNVERIFIED.*

## The live failure, and why it is un-fixable at the adopter's end

gate-lint ships a `seed` rule landing `substitution-fed-loops.txt` under `{memory_root}/project/`.
Both adopter hygiene gates refuse it structurally, so the file cannot be committed there — the
reporting session landed it with `--no-verify` at both repos specifically so the refusal survived as
evidence.

The kit's own descriptor says the quiet part: until that rule existed, NO kit wrote anything under
`{memory_root}/project`. Nobody asked an adopter's hygiene gate whether it would accept one.

There IS a mechanism for admitting a new file there — `PROJECT_REGISTRY_EXTRA`, which gov sets for
itself. It cannot reach these adopters: the key lives in `.memory-tree.conf`, which is target-owned,
and inCMS's checker is a FORK, which `update` writes in neither direction. So widening the gate is
not available and the seed has to go.

## THE ORDERING IS THE WHOLE RISK — steps 2 and 3 are ONE commit

Dropping the seed rule while the `[[gate_leg]]` argv still names the registry path re-creates
`apply` exit 1 at every adopter, through `silenced_legs`: the leg's argv resolves a path no rule
ships, so the leg is withheld and `apply` fails. That is the exact failure the seed was added to fix,
re-created in the other direction.

Delete the rule, delete the template, and drop the third argv element from the descriptor's
`[[gate_leg]]` — together, in one commit. Do not land a tree where one is done and the other is not,
not even transiently.

## What does NOT move

UNVERIFIED by me but stated in the plan this build came from, so check it before relying on it:
gov's own `tools/gate-legs.json` row keeps its third argv element, because the descriptor-to-manifest
parity arm compares name, subject and chunk and never argv. Gov's own
`memory/project/substitution-fed-loops.txt` and its `PROJECT_REGISTRY_EXTRA` row both stay — gov is
entitled to its own registry; what it may not do is ship one into somebody else's tree.

## The engine half

`sh_hygiene.py` takes the registry positionally and REFUSES when it is absent, reasoning that a scan
with no declaration reports the whole population as new. But that is byte-identically what the
shipped EMPTY template produces, and the template's own prose documents that as the correct first
install. So the refusal forbids the state the kit ships. Make the positional optional and delete the
refusal; fold the template's first-install prose into the README, since the template is going.

Add a selftest arm for the absent-registry path and raise the floor — an arm that exists but is not
counted is one a later deletion removes silently.

## Standing bans, each tripped once here

Lead any new function with a declared verb from `.lexicon.conf`. Spell no `tools/<kit>/…` path in
shipped prose — this unit edits a README, which is where that ban was tripped before. Re-declare with
`--dispatch` if your write set grows.

Observe the RED before wiring anything: a fixture can stage a condition the tool does not actually
refuse, and a first cut can be vacuously green when the artifact it inspects is absent.
