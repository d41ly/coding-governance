# session kickoff — one engine, one manifest, and the list they both read

```toml
feature = "session-kickoff"
title = "the /session-kickoff engine, its project manifest, and the ratchet that keeps the manifest true"
status = "shipped"
streams = ["kickoff"]
decisions = []

[claims]
gate-legs = []
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = ["SESSION-KICKOFF.md"]
backlog-shards = []
[paths]
globs = [
  "memory/guides/SESSION-KICKOFF.md",
]
```

## Constraints & why

The engine is project-agnostic and the manifest is the project layer it reads. Everything specific to
a repo — branch conventions, the id protocol, the gate fence, the pointer map — lives in the manifest,
so the engine can ship unchanged to every adopter and the manifest can say something different in each
one.

The manifest lives at `memory/guides/SESSION-KICKOFF.md`, beside the other binding protocol documents
rather than in an assistant-specific directory. That home was chosen for tool-agnosticism and it is
not free: it puts the manifest onto the charter's read path, which hygiene check 16 bounds, so the
manifest's size is now a budget item rather than a matter of taste.

**The list of places a manifest may live is declared once**, in `manifest-check.sh`, and every other
reader asks for it rather than restating it. It was previously spelled in five files that did not
agree — two of them naming directories no live install had ever used, and one of them promising a
fallback the checker never implemented. The verb that prints it answers before the script's own repo
probe, because its whole purpose is to be readable from outside a repository.

## Shared seams

The checker is the single source for three different questions, and the engine invokes it for all
three rather than reimplementing any: where a manifest may live (`--locations`), whether this one is
still true (the default run), and what a pre-commit may cheaply verify (`--staged`). The engine's own
instructions say never to reimplement its checks inline, because the script IS the semantics.

Membership is decided by git identity — the file's toplevel compared against the script's, both
normalised through the same `cd … && pwd` chain — never by comparing path strings. Under MSYS one
directory has two spellings and mount points are not symlinks, so a string comparison answers
differently depending on which flavor the caller happened to use.

## Gaps

- **The third manifest location cannot be gated, by construction.** The engine honours a manifest at
  the skill's own base directory as a machine-global fallback for repos that have none. That
  directory is outside every repository, so the checker refuses it and no project gate can reach it.
  The engine skips the audit for it and labels it unaudited on the READY card, which makes a stale one
  visible every kickoff rather than silently authoritative — but visible is not checked.
- **The engine itself is installed per machine, not per repo**, so the tracked copy and the running
  copy can differ with nothing to notice. `check-wiring.sh` now compares them by content and reports
  at SessionStart; it is deliberately not a merge-bar leg, because machine state travels with no
  commit and would red the bar for a reason no diff can fix.
- **The `governance-template:` marker fallback is engine-only.** The checker does not implement it, so
  it is absent from `--locations` and is documented as engine behaviour instead. That is one fact in
  two documents, which is the shape this feature otherwise exists to remove; it survives because
  dropping it would silently change behaviour for adopters who have an instantiated playbook and no
  manifest.

## Reuse affordance

seam: manifest-check.sh `--locations` — reuse the shape whenever two or more readers need the same
list and one of them is a document. Declare the list once in the script that enforces it, expose a
read-only verb that prints it and exits 0 before any environment probe, and have every document
invoke the verb instead of restating the list. A print-only verb adds no failure branch, so it costs
nothing against a harness meta-gate that counts them, and the not-found message can be BUILT from the
same array the search walks — which is what makes it impossible for the error to describe a different
list than the one that was searched.
