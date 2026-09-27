# playbook — the charter renderer

Fills `coding-governance-agents.template.md` into a target repo's charter, as a re-renderable region.

```bash
python tools/govkit/govkit.py intake --target <repo> --kits playbook,playbook-render,…
bash  tools/playbook/adopt-playbook.sh --target <repo>
bash  tools/playbook/adopt-playbook.sh --target <repo> --check
```

## Why this exists

The charter used to ship with a prose companion telling an agent to fill every placeholder by hand
and delete the conditional blocks their project had no kit for. A catalogue and a program are two
answers to one question, and the catalogue is the copy that rots — so the catalogue is now a
declaration the engine reads, and what a program genuinely cannot decide moved to
`WIRE-INTO-PROJECT.md`.

## What it refuses

It never guesses. Every refusal names what the operator must supply:

- a placeholder the descriptor declares nowhere;
- an `asked` placeholder with no answer in `deploy.toml`;
- a `derived` placeholder whose probe returned nothing and that nothing answers — it does NOT fall
  back to a default it never declared, because a probe quietly returning the empty string is how a
  charter ships with a blank where a branch name belongs;
- a template that is its own charter: `playbook_path` resolving to the `--charter` file;
- a `[charter]` entry that fails its grading (below);
- a `kit:` fence naming something that is not a registry entry;
- a `when:` fence naming a block the descriptor does not declare;
- a `drop_blocks` member that matches no fence.

## Where a value comes from

In order: `deploy.toml`'s `[charter]` table, then `[answers]`, then the probe for a `derived`
placeholder or the declared default for a `defaulted` one. **An answer outranks a probe**, so a probe
that answers wrongly can be corrected without forking the descriptor. The render prints the answer
beside what the probe would have derived, and says when the two are equal. That is a note, never a
failure.

## `playbook_path` has two modes

With `playbook-render` selected, `playbook_path` is where the TEMPLATE lives, and the render writes
the charter named by `--charter` (default `AGENTS.md`). The two may not be one file. Without
`playbook-render`, `playbook_path` is the copied charter itself, and the `playbook-placeholders`
hole probes it for a surviving `{{`. In render mode that hole stands down, because the template
always carries placeholders and `--check` already reports one that survives.

## The `[charter]` table

`[charter]` holds values whose only consumer is this renderer. govkit's token context never reads
it, so nothing in it reaches an argv, and it may carry prose `[answers]` refuses: an em dash, a
backtick, angle brackets. That is where a commit trailer such as
`Co-Authored-By: Name <address>` belongs. The render refuses, naming the key:

- a key that names no declared placeholder;
- a key that names a token an argv or destination needs (it belongs in `[answers]`, where the argv
  can read it; `govkit check` makes the same join over every selected kit);
- a control character other than a newline, the `{{` opener, or a `gov:playbook` region marker.

## Two namespaces, and neither reads a boolean

`kit:<id>` drops when the target did not select that kit. `when:<name>` drops when the name is a
MEMBER of `drop_blocks`. Membership rather than truthiness is load-bearing: govkit writes every
answer as a quoted string, so a key "answered false" would arrive as the string `false`, read as
true, and leave the block standing.

## `--check` asserts two things, separately

Region parity and placeholder completeness are different questions, and they fail with different
messages. A target whose descriptor declares nothing for a key renders a region that is perfectly in
sync and still tells the agent to invoke a placeholder's name. The comparison normalises line
endings first — this fleet runs `core.autocrlf=true`, and a charter with no `eol` attribute holds
CRLF in the worktree against an LF blob.

## The region reader is this kit's own

The memory-tree kit's region helper raises when no marker pair is present, so it serves neither the
absent-charter nor the charter-without-a-region state. This engine CONFORMS to the marker-region
contract and is a fifth reader in its case table; it does not import that implementation, which
would be the cross-kit edge the contract forbids.
