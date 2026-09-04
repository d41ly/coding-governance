# Build brief — TOOL-dRetiredFork-12

**Serves:** journal TOOL-dRetiredFork-12

Recorded after the pass, like unit 11's. The order is stated rather than implied.

## What the unit is

`playbook.fixture.md` shipped `role = "engine"` — verbatim, no placeholder pass — with this kit's own
directory spelled five times in its `outputs`, `grain`, `records` and `legs`. At any other prefix
`check-playbook.sh` exited 1 and the suite above it could not follow a variable the fixture did not
have. TOOL-dScrubbedConduit-2.

## ONE token, and the reason a second is forbidden

`KIT_DIR`. All five spellings sat under the kit dir, so one covers them. `TOOL_ROOT` is computed
ONLY by the memory-tree adopter; this kit's adopter never computes it, so declaring it would ship an
unresolved brace to every adopter.

## What the spec did not know, found by running it

**The records carry the prefix in their FILENAMES and their bodies.** Each is named for its piece
with `/` written as `~`. Rendering the fixture alone left every record describing a piece that does
not exist, which the gate reports as an orphan record — coverage nobody has. The adopter repaths
both halves. This is what inCMS's two `engine`-declared fixture-record forks actually were.

**A template is not a playbook, and the gate did not know that generally.** It excluded
`PLAYBOOK-TEMPLATE.*` by name. The moment a second template existed, the gate scanned it, found
`{{KIT_DIR}}` in a leg target and redded check 6 — in gov's own tree. The exclusion is widened to any
`*.template.md`, which is the reason the narrow one was written in the first place.

## The instrument error worth not repeating

`bash gate.sh | tail -2; echo rc=$?` reports TAIL's status, not the gate's. It read rc=0 over a gate
that was exiting 1. Redirect, then check `$?` on the command itself.
