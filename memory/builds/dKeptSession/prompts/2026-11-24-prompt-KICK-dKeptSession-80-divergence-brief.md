**Serves:** research KICK-dKeptSession-80

# Brief — dKeptSession: KICK-dKeptSession-80's divergence, its merge cannot carry the unit's Pass trailer

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-80's builder resolved the merge by its rev-1 spec, and the main loop's commit of it was refused.
S1 and AC2 say the merge commit itself carries `Pass: KICK-dKeptSession-80`. Check 49 can admit no such commit:
- `--check-commit` grades a trailered commit's whole index against the pass's declaration, and the merge's index
  holds every path main's side moved;
- one of them, `memory/project/readme-contract.txt`, is a shared record by `SHARED_RECORDS` of `.unattended.conf`,
  and `--dispatch` refused the widening the refusal itself printed, naming that record.

TOOL-aSparedSpawn-32 §4 states the same wall and the same route, and this run's first reconcile, `ad02f1a6a`,
took it: the merge carries `Pass: none` and the unit's pass commit follows it. The main loop has committed the
merge that way, as `dcb75b59e`, with the CLOSED flip and the ledger held out of it. Revise the spec to that.

### Items

1. S1: the main loop commits the merge with `Pass: none`, hooks running. The unit's pass commit follows it, carries
   `Pass: KICK-dKeptSession-80`, and holds this spec's CLOSED flip, the acceptance ledger and the indexes their
   render moves. Say why in §4, citing TOOL-aSparedSpawn-32 and the two checks above by `path#symbol`.
2. AC2: the second parent and first parent are read at the merge commit, `dcb75b59e`, found as the one merge commit
   whose second parent is `525f3ab97`. The trailer is read in two halves: the merge prints `Pass: none`, and the
   pass commit that follows it prints `Pass: KICK-dKeptSession-80` once.
3. AC1, AC3, AC9 and AC10 read "at the commit". Say which commit each reads, the merge or the pass commit, and keep
   every figure as it stands. The sha AC10's stamp names is the merge's first parent.
4. §7's last sentence: the pass legs run over the merge commit, after it and not over the staged merge.
   `pass-legs.sh` exits 2 over the staged one, because `tools/policy/policy.py#cmd_mirror` renders a committed
   revision. They read RED at `dcb75b59e` on two legs: `kickoff-manifest ratchet`, red by §3's own words, and
   `govkit selfcheck`, a merged-tree red §3 gives the close.
5. "Files touched": name what the pass commit writes as its declaration: this spec, the acceptance ledger,
   `memory/builds/dKeptSession/README.md`, `memory/LIVE.md`, `memory/backlog/KICK.md`. The paths already listed stay
   as the merge's. Name `.governance/instructions.lock` too: the window's render moved its `renderer` line.
6. The superseded "Alternatives rejected" reasoning that the brief allows one commit is corrected by this brief.
7. Bump the spec to rev-2, with one §9 line naming this brief by its file stem. The unit's code has started, so say
   in that line that the departure was found at the merge's commit. Leave the status cell INPROGRESS.

### Acceptance

These report nothing for the spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- `python tools/check-spec-tokens.py --spec <path>`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-80`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`

### Gates

The specs' own checks above. No suite and no bar.

### Non-goals

- No edit to any other spec, and no product code.
- No commit: the main loop commits the revision.
- No change to what the merge resolved: S2 to S6 stand as built.
