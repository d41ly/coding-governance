# PLAY-dOrderedCharter-54 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-54

Each line is a probe this pass ran at rev-3 of the spec, over `e15f0584c` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: a role agent's scratch guard refuses them, so the kickoff engine's suite is
the close's. The probe was a script over a scratch fixture under the user's temp folder: two repositories made
by `git init` with one empty commit, a folder of transcripts, and each payload piped to the checker the pass
changed, its transcript a Windows path with JSON's doubled backslashes from `cygpath`. It ran the checker
directly, never the suite's arms, and printed each second line and each `card-file — ` verdict line.

**Evidences:** PLAY-dOrderedCharter-54
- AC1 — `--card --write < s1.json` — the second line read `card-owner — s1 · <t1>`, the transcript spelled with `/` throughout.
- AC2 — `--card --replay --session s1` over that card kept `<t1>` on the second line; `--card --write --session s3` in a fresh scratch repository wrote `card-owner — s3 · absent`.
- AC3 — `--card --write < s2.json` over a card `s1` owns, `<t1>` touched just before, printed `card-file — skipped: another live session s1 owns this tree` once and left the second line `card-owner — s1 · <t1>`.
- AC4 — the same `s2` write over the five staged cards wrote `card-owner — s2 · <t2>` each time and printed one `card-file — took over: session` line: `s1 · transcript 3603s old` for the transcript dated 3600 seconds back (PINNED by the spec's AC4), the write's own three seconds included (deviation 543); `s1 · transcript absent` for a missing `<t1>`, for `card-owner — s1 · absent` and for unit 49's `card-owner — s1`; `none · transcript absent` for a card with no owner line.
- AC5 — `--card --write < s2-clear.json` over a live card `s1` owns wrote `card-owner — s2 · <t2>` and printed `card-file — took over: session s1 · source clear`.
- AC6 — `--card --write < s1b.json` over a card `s1` owns wrote `card-owner — s1 · <t1b>` and printed neither `card-file — skipped:` nor `card-file — took over:`.

**Owed to the close.** Every leg of the spec's Gates section, the `manifest-check self-test` above all, which runs
the moved card file arm and unit 49's two-session arm with its transcript, neither of which this probe ran inside
the suite; and the RED-first observation of the `New arm:` line, each failing case staged by reading every other
owner as live, by ignoring `source`, or by recording `absent` on a session's own payload-less write.
