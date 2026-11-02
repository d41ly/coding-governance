# TOOL-dFoldedAudit-11 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-11

The acceptance criteria were observed by this unit's builder over the tree of this commit, on fixture R of section 6 at `%TEMP%/fa11`, built fresh per criterion, by one scratch probe of the driver as a CLI. No gate, suite or bar ran. Each new arm's RED-first observation is the close's, and it is not recorded here.

The arm blocks share the probe's rows and sed scripts, and they never ran. The probe is the evidence for the criteria, and the arms are owed as written.

**Evidences:** TOOL-dFoldedAudit-11

- AC1 — `stands at rev-1, below the rev-99` — with every spec at rev-1 the row refused, exit 1 printing `UNATTENDED check 118 FAILED`, `git ls-files '*-chain-rounds.md'` printed nothing, `--chain-verdict` printed `round 0`, and rev 100 refused the same way.
- AC2 — `no Revision log entry at rev-2` — printed with the `- rev-2` line cut from one spec and its header at rev-3.
- AC3 — `rev-1 is a spec's first draft` — printed for a `local` row claiming rev 1 and for `--sibling FIX-dFix-3@rev-1`, both on rev-1 specs.
- AC4 — `no tracked spec carries that id` — printed for the MEDIUM `local` row on `FIX-dFix-9`, and the same row as `new-mechanism` at rev 1 exited 0.
- AC5 — `below the rev-99` — printed for `--sibling FIX-dFix-3@rev-99`, and `--sibling FIX-dFix-3@rev-3` exited 0.
- AC6 — `**rev-3**` — exit 0 on an older logged rev with the header at rev-3, on that entry spelling, on a spec of nine CRLF lines, and under `## Revision log` with no ordinal. The CR cut is not separated from its absence here, because no anchor of the reader's grammar reads the line's end.
- AC7 — `a --sibling is outside` — a good row beside rev 99 refused and the tracked record's digest did not move, and the same call with a bad `--sibling` printed this, the digest still unmoved. `grep -c 'fail 118'` printed 1, and the census grep printed 318 before the pass and after it.

Beyond section 6, the same probe refused rev 0 and `rev-01` as a first draft, refused a rev above 64 bits on the header test, and read `rev-02` as rev 2. A spec with no status rev printed `stands at rev-0`. An entry past the section's closing heading, and a `rev-12` line standing for rev-2, both took the log refusal. A spec under `_working/` and an untracked spec both took the missing-spec refusal, and a round with no fold row exited 0.

Owed at the close: the bar, and the five `New arm:` lines of section 7, each RED on its staged break and GREEN once restored. `FLOOR_ASSERTIONS` moved 3041 to 3082 and `FLOOR_SHARD_1` 524 to 565, 41 assertions counted off the block's own lines.
