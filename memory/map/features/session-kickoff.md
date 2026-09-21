# session kickoff — one engine, one manifest, and the list they both read

```toml
feature = "session-kickoff"
title = "the /session-kickoff engine, its project manifest, and the ratchet that keeps the manifest true"
status = "shipped"
streams = ["kickoff"]
decisions = []

[claims]
gate-legs = ["kickoff engine size <=18KiB"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["shipped-checker-edit-is-an-adopter-contract-change.md", "msys-grep-counts-cr-on-every-line.md"]
guides = ["SESSION-KICKOFF.md"]
backlog-shards = []
lexicon-verbs = []
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

The checker is also the writer of the session's orientation card (`--card --write`, `--card
--replay`, `--card --path`; `KICK-aReplayedCard-1`). The card lives under the git common dir, so
every worktree of one repository shares the directory and a card names the tree it was written in;
every startup cell is derived, the `node —` cell through the manifest's own `registry:` key, so the
kit spells no charter path. The verbs run no manifest check and no fetch: those stay in the engine's
Steps 1 and 2b, where each costs a kickoff rather than every session start.

The engine's kickoff lands on the card through `--card --append` (`KICK-aReplayedCard-2`), which
checks every cited path, line range and record id for EXISTENCE in two spawns — one
`git ls-files -- …` and one `corpus_ids.py --print-defined-ids`, the memory-tree reader that owns
the id grammar and prints it on its first line, so this kit spells none — annotates each miss
`UNVERIFIED — <token>` beneath its row, and refuses a body with nothing to check, one over the cap,
or a READY line whose BASE is not HEAD. A real READY line replaces the sentinel and the previous
body, and re-renders the `tree —` cell in the tree the append runs in. `--card --check` re-runs the
same check over the stored card. Neither judges relevance, scope, tier, or truth at the cited line.
The engine consumes the card at Step 1 — its node tag, tree kind, worktree count and recent subjects
replace `git worktree list` and the log in the batch, while the branch, `status --short`, the
fast-forward and `rev-parse HEAD` as the BASE still run — and appends at Step 5, piping its six
sections and the READY line through that verb before Step 2b's staged repair is committed
(`KICK-aReplayedCard-3`), so the deny reads a READY line when the engine's own commit reaches it.

The engine also puts the spec-audit question to the owner, once, at Step 3 (`KICK-aBlindedTrial-1`):
only when the DoR is a design pass and the build method the manifest names makes `spec-audit:` opt-in,
recommending yes for two or more units or an open §8 fork and no otherwise, because the owner decides
and the engine may only recommend. A yes writes `spec-audit: <today>` into the build README front
matter before the spec pass; either answer lands on the card's `## open` section as one line. The
unattended hand-back never asks it — the README at BASE has already decided, and the unattended kit's
preflight line states the posture.

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
