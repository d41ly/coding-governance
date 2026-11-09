# PLAY-dOrderedCharter-33 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-33

Each line is a probe this pass ran at rev-6 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `pins.py --fixture --plant` over a throwaway repository, the update criterion
through `fixtures/stale_edges.py` over a scratch gov and target, and the catalogue reads through the
criterion's own commands. Each plant was also run with one function of its path stubbed to a broken form, and
each went red. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-33
- AC1 — `meaning-editorial` — a record marking "never push" changed to "always push" `editorial` exited 1 naming the record, `unit.push` and `never`; `punctuation-editorial`, a comma added and a full stop made a semicolon, exited 0 with no stale line.
- AC2 — `spelling` — with no `[[spelling]]` row the respelling marked `editorial` exited 1 naming `colour`; with the row `colour` to `color` committed it exited 0; `ruling-unproven` — a meaning change marked `editorial` with a `**Ruling:**` and the door's `none — stand-in door` proof exited 1 naming the missing proof, and the same record under a `tty-cli` proof exited 0.
- AC3 — `editorial-behind` — two editorial records past the pinned `amends` printed an `amended` line and no `stale` line, and the composition read gov's newest text then the repository's.
- AC4 — `semantic-behind` — `order` rendered both texts and returned one order keyed `.governance/instructions.toml#repo.push`, titled as a stale edge, carrying both texts and the re-pin command, and wrote no journal; `refuse` exited 1, named the edge on a `held` line, returned no order and left the tree clean; `warn` under `--write` rendered both, printed the stale line, appended one journal line naming `repo.push`, `unit.push` and `warn`, and returned no order.
- AC5 — `empty` — with no overlay the verb printed no unit line and its `rows` read `0 row kinds registered`.
- AC6 — `rename` — the edge re-pointed to `unit.push-main` with its pin kept, no order, and the repository's unit composed after it; `split` orphaned an `amends`, absent from the composition with one order, and held the update under `refuse`; `retire` orphaned a `supersedes`, which composed alone, with one order.
- AC7 — owed: the step gate's `unit` class row lands in the later commit the fork record's F5 rules, once a gov unit row is tracked; this pass's `unit-class` plant observed the reader return both gov unit tags, the witness return the tag a removal record ends, and the plant remove one unit staged and name it `unit:unit.kept`.
- AC8 — `new-beside` — a level-0 gov unit new since the first release printed one `new-beside` line naming it and `repo.ships-charter`; the new level-4 unit printed nothing.
- AC9 — `stale_edges.py --plant order` — the read-only update exited 0 with one `stale` line among its verdicts and `unit:stale 1` in its tally, and `--write` exited 0 writing one `update-unit-<slug>.md`; `--plant refuse`, with `instructions.stale = "refuse"` committed in the target's policy file, exited 1 with the stale line and nothing written; with `--stub no-handler` each plant missed its observations.
- AC10 — the criterion's catalogue probe printed one row, `order`, `dOrderedCharter`, `True`, `True`; the fixed-string line match over `unsummarised-keys.txt` found no line after `policy.py lists --write` drained the name; the fixed-string grep for the mode read over `govkit.py` found one line.
- AC11 — owed: the `usage.toml` row lands in the same later commit as AC7's class row (F5).

**Owed to the close.** The bar, and the RED-first observation of each `New arm:` line: the render selftest's
arm running `pins.py --fixture` over every plant, the deployer's self-test arm running `stale_edges.py` over
both plants with and without the `no-handler` stub, and the step gate's `unit` class row's arm, which arms only
at F5's later commit. That later commit lands the `unit` row in `surface-classes.toml` and the `usage.toml`
row, and records AC7 and AC11 from it.

**The later commit (F5).** Each line below is a probe the later-commit pass of PLAY-dOrderedCharter-33 ran, with
the `unit` rows applied over the tree that tracks unit 40's gov unit rows (c91c26904). No leg, suite or bar ran.

**Evidences:** PLAY-dOrderedCharter-33
- AC7 — later commit — `step_gate.py --list` over the worktree printed `unit · 4 members` beside the other classes; in a scratch clone carrying the rows committed, `step_gate.py --fixture --plant unit` exited 1 naming `unit:unit.policy-schema`, and a sparse clone with the same plant and then a change record ending `unit.policy-schema` with `Successor: none` committed exited 0, `1 vanished · 1 witnessed`, the witness reading that tag. Before the plant fix of deviation 336 the same fixture exited 0 with nothing vanished, because the plant matched no bytes in a CRLF checkout.
- AC11 — later commit — `git grep -n -A3 -F 'class = "unit"' -- tools/govkit/usage.toml` printed the one `[[class]]` row with `usage = "none"` and its `why`, and `git grep -n -F 'id = "unit"' -- tools/govkit/surface-classes.toml` printed the registered class it joins.

**Owed to the close.** The step gate's `unit` class row's `New arm:` RED-first observation, the `step-gate` and
docs legs over the two rows, and the bar.
