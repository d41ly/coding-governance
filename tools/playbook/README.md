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
- a `derived` placeholder whose probe returned nothing — it does NOT fall back to a default it
  never declared, because a probe quietly returning the empty string is how a charter ships with a
  blank where a branch name belongs;
- a `kit:` fence naming something that is not a registry entry;
- a `when:` fence naming a block the descriptor does not declare;
- a `drop_blocks` member that matches no fence.

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
