# aCarriedStop — the closing review's promotions, handed to the spec writer

**Serves:** research TOOL-aCarriedStop-2 TOOL-aCarriedStop-3

Write two Tier-2 specs, status SPECCED, one file each under memory/builds/aCarriedStop/spec/, dated 2026-11-13: TOOL-aCarriedStop-2 and TOOL-aCarriedStop-3. Both are promoted from the closing diff review, memory/builds/aCarriedStop/reviews/2026-11-13-review-TOOL-aCarriedStop-1-diff-review-round1.md: read it whole, with the CLOSED spec of TOOL-aCarriedStop-1 and the code at HEAD. A CLOSED spec stays frozen. Never write under memory/builds/dDeclaredLoop/.

TOOL-aCarriedStop-2 closes the review's HIGH item, ids 3, 5 and 11: the `--owner-stop` writer in `write_chain_round` holds only the file name to a charset while `derive_chain_verdict`'s awk holds the whole path, so under a MEMORY_ROOT outside the reader's charset the writer appends a row its own reader refuses and blames on a hand edit. One rule, stated once: the writer refuses, before any byte, a whole path the reader's grammar would not admit. Take the review's fix where its skeptic judged it sound. It orders first.

TOOL-aCarriedStop-3 batches every MEDIUM and LOW the review confirmed, each named by its id in the spec: the count test reached with empty operands on the owner-stop route (ids 4, 12), the missing suite arms (ids 6, 7, 8, 9, taking the skeptic's corrected fixes where the report says the finder's were unsound), the suite header's unrecorded observation claim (id 10) and the usage header's padding (id 15). It orders after unit 2, because both write tools/unattended/unattended.sh and its suite.

Each spec declares its edge to the other, its `New arm:` lines, and what it does not check. Neither adds a refusal site or a check number: the driver's census stays 319. Each acceptance criterion is an observation with its command in the probe-fixture style of unit 1's spec. Run `python tools/check-spec-tokens.py --spec <path>` over each and fix every hit; run no full memory hygiene gate. Do not commit.

Return: both spec paths and status lines, and anything in the review you found wrong.
