# KICK-aRoutedQuill-1 — acceptance ledger

**Serves:** journal KICK-aRoutedQuill-1

No merge bar and no self-test suite ran in this pass. The suite's new block ran as a scratch slice on
node a: the suite's prologue, its card-fixture prologue and K2 spawn shims, then the block alone, in a
`git clone --local` of the run branch under a short `%TEMP%` root. Against the built checker it
printed `pass=31 fail=0`. Against the base checker, copied out of `HEAD` before the pass, it printed
`pass=10 fail=20` on the block as first written: AC1, AC3 to AC8 red; AC2's append and AC10's spawn
pair hold on both, since the base appends any route. The close still owes `manifest-check self-test`
run whole, with its raised `FLOOR_ASSERTIONS`, `scratch-guard self-test`, and the other legs §7 names.

**Evidences:** KICK-aRoutedQuill-1
- AC1 — `--brief-skeleton` — run from a directory under `GIT_CEILING_DIRECTORIES`, where `git rev-parse` exits 128, it exited 0 and printed the four `##` sections, the seven `###` sub-heads in order under `## The brief`, then `## route` and its three line shapes. Base: exit 2, "not a git repository".
- AC2 — `--card --append` — a conforming route with no READY line, appended to a card holding a real READY line, exited 0, and the card's last two lines were the route's `- brief:` line and the READY line.
- AC3 — `grep -c '^## route'` — after a second route naming `TOOL-zCardFixture-12`'s tracked spec, it read 1, and only the second unit line was on the card. Base: two route sections.
- AC4 — `--card --append` — exit 1 and a byte-identical card for an undefined id (R3), an id paired with a spec whose H1 defines another (R4), an untracked spec (R4, no `UNVERIFIED` line written), a spec in another build's `spec/` (R4), `AGENTS.md` as the brief (R5) and the unit's own spec as the brief (R5), each naming its line and rule. Base: all six appended.
- AC5 — `--brief-skeleton` — no `- build:` line, no `- unit:` line, two `- brief:` lines, a stray `- note:` line and two `## route` sections each exited 1 naming the shape and `--brief-skeleton`, the card byte-identical. Base: all five appended.
- AC6 — `READY — none yet` — a conforming route on a fresh card exited 1 with R6, naming the missing kickoff, the card byte-identical. Base: appended.
- AC7 — `DEAD PROBE` — a body with a real READY line, a tracked path and no `## task` exited 1 naming the missing section, the card byte-identical; the K2 AC3 token-free body's `DEAD PROBE` arm and its check are untouched. Base: appended.
- AC8 — amended rev-5 — with no `MEMORY_ROOT`, the id reader itself exits 1 and the append exits 2 before the route rules; with the reader also hidden, R0 named `MEMORY_ROOT`; with `extract.py` hidden the reader took its exit-3 branch and R0 named the missing id set. Each exit 2, the card byte-identical.
- AC9 — `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` — it printed `template-size OK — SKILL.md: 18256 / 18432 bytes` and no `WARN` line, under the recorded high-water of 18369; `grep -n -- '--brief-skeleton'` hit the Step 3 sentence, and Step 5 names `## Owner confirmation` and `## route`.
- AC10 — `SPAWN_LOG` — AC2's append under the K2 shims logged one `ls-files -- ` line and one `corpus_ids.py --print-defined-ids` line.
