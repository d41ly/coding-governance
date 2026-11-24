**Serves:** research KICK-dKeptSession-13

# Brief — dKeptSession: KICK-dKeptSession-13's reference re-render takes its docs-undocumented row

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Spec 41's writer (orders 27 to 29 re-ground) found that re-rendering `help/reference/policy.md` for a catalogue member
also requires taking that member's row off `memory/project/docs-undocumented.txt`, or the `docs` leg reds; spec 41
rev-3 does so for `policy:actions.free` and `policy:notify.owner`. Spec 13 rev-4's S5 re-renders the reference page
for `card.pointers` and does not take the `policy:card.pointers` row (or whatever row that file holds for it) off the
list. Fold that into spec 13 so its builder does not diverge on it.

### Items

1. F-docs-row: probe `memory/project/docs-undocumented.txt` for the row naming `card.pointers`; if one stands, spec 13's S5 takes it off, `memory/project/docs-undocumented.txt` joins Files touched, and a criterion observes the row gone and the `docs` leg's anchor present; if none stands, say so in the revision log and change nothing else.
2. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap, pin every figure with DERIVED or PINNED, and leave no fork open.

### Acceptance

Spec 13 at a new rev carries the fold and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-13` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays DEFERRED), and no spec other than
KICK-dKeptSession-13's.
