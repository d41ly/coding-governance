**Serves:** journal TOOL-dBoundRoles-14

# TOOL-dBoundRoles-14 — the first builder's return, a divergence

Run `wf_0b85ec90-051`, builder agent `aac04179ddc0b16bc`, started at `0b2529ccd`. It wrote no product path and
committed nothing; `diverged: true`.

## The divergence, as returned

(1) S4 and §4 "The read-key vocabulary": the spec says READ_FAMILIES holds "the same 23 keys READ_KEYS holds at base",
and its literal leaves out `brief:prompt` and `upstream:rows`. READ_KEYS at HEAD (tools/roles/roles_lib.py@d35faceb:36-43) holds
25 keys. `brief:prompt` is read by tools/roles/agents/gov-spec-writer.agent.md:7, and `upstream:rows` was added by
TOOL-dDeclaredLoop-29. Building the literal drops both, R3 then reds gov-spec-writer, and AC6's "exits 0" cannot hold.
The literal needs "prompt" in the brief tuple and an `"upstream": ("rows",)` family. The §4 count table needs 25 read
keys. The sentence "A later family (TOOL-dDeclaredLoop-29 S5's upstream) joins by one READ_FAMILIES entry" needs
rewording, because that family has already joined. The spec should also say that R3's must-be-optional checks for
`card:reuse` and `upstream:rows` (tools/roles/check_roles.py@b486e821:218-222, which compare the raw entry) apply to the native key that
parse_read_key returns, so either spelling is graded.

(2) S7, AC6 and §4's table and Migration paragraph all say gov has ten role files. HEAD has eleven: TOOL-dWitnessedBar-23
added tools/roles/agents/gov-tester.agent.md, which reads `input:spec, input:diff?, input:question?`. The spec needs
"eleven" and a `role` count of 11.

(3) §4 "The extractors" describes extractors as `(path, text)` yielding `(tag, "member", line)`. HEAD's contract is
`fn(ctx, path, text=None)`. A text of None is the applicability probe and returns "" or None (tools/playbook/tag_index.py@7e8c889f:756-764).
Given text, the extractor returns 5-tuples `(tag, kind, line, end, text)` (derive_tag_rows at :343-347, inserted at
:727-729). Only kinds in DEFINE_KINDS = ("doc", "section", "tag") (:97) declare a member to check_namespace_joins
(:1276-1280). A "member" row declares nothing, so in AC1 both `role.gov-builder` and `role.gov-buildr` would read as
undeclared. The spec needs kind `tag` and the ctx/path/text contract.

(4) §4 "The two rows": `purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"`
is a `<path>#<field>` source on a .md file. That file exists, so check_namespace_purpose (tools/playbook/tag_index.py@7e8c889f:1427-1432) reds
both rows on the tags leg: "reads a field in a .md file, which the arm reads no field in". The spec needs a path-only
source (no `#design-tags`), or a `.toml`/`.py`/`#<field>` form the arm reads. Also, `source` should write the tool root
as `{prefix}/roles/...` rather than `tools/roles/...`, as the registry header says (tools/playbook/namespaces.toml@1d6e69b2:11).

## What held

F4 discharged: PLAY-dOrderedCharter-19 S2, S4, S13 and PLAY-dOrderedCharter-10 S3, S4, S7 all have code at HEAD: the
registry tools/playbook/namespaces.toml with tag_index.read_namespaces, the index _write_parsed and build_index,
`gov_tag.py --fixture --plant` with PLANTS at :382, check_tag_shape at tools/playbook/tag_index.py@7e8c889f:1243, check_namespace_joins at :1260,
and `lexicon.py --tags` at :4055. `layer.roles` is a row of layers.toml, dBoundRoles is a row of
memory/project/chain.toml, and the playbook README table that names `role` is at tools/playbook/README.md:304-309. The
stage keys still fold to 7 distinct (tools/roles/workflows.toml@1d4a4348:37, :46, :55, :64). Moved lines only: STAGE_KEY_RE at
tools/roles/check_roles.py@b486e821:121 (spec :110), parse_front_matter at tools/roles/roles_lib.py@d35faceb:450, check_rule_tags at :401, R3 at
tools/roles/check_roles.py@b486e821:209-224.
