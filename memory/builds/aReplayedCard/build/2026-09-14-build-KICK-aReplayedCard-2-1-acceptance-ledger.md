# Acceptance ledger — KICK-aReplayedCard-2, the append and the citation check

**Serves:** journal KICK-aReplayedCard-2

Every observation below was made at the dispatched base tree (`c95fe32a`, the branch tip the unit
was handed) with the unit's working-tree changes applied, by running the self-test whole and by
running its card section against staged mutants of the checker. No figure is copied from the brief
or the spec; where the spec's shape was changed before the code, the rev-5 line in its section 9
says what and why.

## What was built

- `skills/session-kickoff/manifest-check.sh`: `--card --append --session <sid>` and
  `--card --check --session <sid>`, dispatched beside the three verbs of `KICK-aReplayedCard-1`.
  Six functions — the spec'd `extract_card_tokens`, `check_card_citations`, `add_card_body`, plus
  `check_card`, `render_tree_cell` (lifted out of `render_card`, so the append re-renders the
  `tree —` line with the one spelling) and `extract_card_parts`, and a seventh helper,
  `resolve_id_reader`. Two spawns per run: one `git ls-files -- <paths> <basename> */<basename>`
  and one `corpus_ids.py --print-defined-ids`, whose first line is the id grammar as a POSIX ERE,
  so the script spells no grammar. A miss is one `UNVERIFIED — <token>` line beneath its row, with
  `(ambiguous: <n> matches)` or `(past end: <n> lines)` where the reason is one of those. Zero new
  `fail` call sites: every refusal is the `MANIFEST env ERROR — …` shape, exit 1 for DEAD PROBE and
  the `--check` verdicts, exit 2 for the cap, a stale BASE, a missing card, two READY lines, and a
  reader that could not answer. The header states what the verbs do not check. This is the copy
  every adopter installs: both verbs are inert until a hook or the engine calls them, and no
  existing check moved.
- `skills/session-kickoff/manifest-check.test.sh`: 56 arms in a `K2` section, in the clone's two
  linked worktrees; the fixture commit in the clone carries the working tree's `corpus_ids.py` and
  a spec whose H1 defines unit 10 of a fixture slug, `zCardFixture`, and whose prose cites its unit
  11 — spelled here without the family, because a record citing a full id defines or orphans it;
  four helpers `render_ready_line`, `read_next_line`, `check_card_unchanged` and
  `render_big_body`, two PATH shims for the spawn count; the `--card` no-verb arm's expected text
  gains the two verbs; `FLOOR_ASSERTIONS` 109 → 165.
- `tools/memory-tree/corpus_ids.py`: the `--print-defined-ids` verb, `print_defined_ids` over
  `_render_defined_ids` (the assertable split `_measure_lines` uses), one selftest arm that runs the
  printed ERE against a defined id and asserts no `(?` or `\d` survived the translation.
- `tools/memory-tree/README.md`: the verb in `corpus_ids.py`'s row.
- `tools/install-prefix-waivers.txt`: the two rows waiving `corpus_ids.py`'s selftest fixture are
  line-keyed and the verb's lines land above them, so they are re-keyed 935 → 971 and 939 → 975.
  `tools/install-prefix-carried.txt`: the file's carried count falls 8 → 4, because the ban refuses
  a new `tools/<kit>/…` literal and the docstring's five usage lines now derive the kit path.
- `memory/map/features/session-kickoff.md`: the append and the check in the card paragraph.
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped at the merge-base `c4f02308`;
  `last-body-change` unchanged, the body did not move.

## The wall, measured

One append of three tokens in a scratch clone's linked worktree on node `a`: **9.4 s** with 30 bash
processes resident and no suite running, **17.7 s** with two self-test suites running beside it
(36 resident). The reader spawn alone, `corpus_ids.py --print-defined-ids` over this repository's
1133 defined ids, is **3.3–3.7 s** of that: a corpus walk plus the reader's own bash probe of the
hygiene engine for the append-only set, not the one interpreter start the spec's section 5 priced.
The rest is the checker's own git spawns — the toplevel, the common dir, `ls-files`, and the three
`derive_head_state` makes for the re-rendered cell — at the 0.75–1.1 s a loaded node charges each.
Not measured on a quiet host: none existed during the pass. The whole self-test was 16m52s and
14m42s on its two green runs.

## RED before it landed — how each arm was staged

The card section was extracted into a partial suite (fixture helpers + the card arms, the floor
dropped) and run against the checker as committed at `c95fe32a` and against four mutants of the
working-tree checker. Every K2 arm went red in at least one run:

- **Run A — the checker at HEAD, no append and no check.** `--append` and `--check` fell into the
  manifest-path catch-all (`'--append' not found`, exit 2): 43 of the 56 arms red, plus the
  no-verb arm whose expected text names the two new verbs — the same 43 on the re-run after the
  spawn counters became PATH shims. The 13 that stayed green are the three
  `--card --write` setups (armed by `KICK-aReplayedCard-1`) and the ten absence-shaped ones —
  byte-identical after a refusal, one READY line, the sentinel last, no `## open` survivor, the
  startup lines untouched — staged in run B.
- **Run B1 — every refusal writes before it exits** (DEAD PROBE, the cap, the stale base, the
  three reader refusals): the four byte-identical arms red, and again on the re-run after the AC4
  arm's own fix below.
- **Run B2a — both append paths put the body AFTER the whole tail:** the sentinel-last arm, the
  real-replaces-the-sentinel count, the `## open` survivor, and AC10's second body (two READY lines,
  and the cap two bodies breach) red.
- **Run B2b — the body's own `READY — none yet` line stored rather than dropped:** the
  exactly-one-READY-line arm red.
- **Run B3 — the append rewrites the `worktrees —` line:** AC10's byte-identical startup arm red.
- **The reader arm** in `corpus_ids.py --selftest` was staged by deleting the `\d` translation:
  the arm red with the verb's own refusal (`carries a construct this verb cannot translate`),
  green again with it restored.

One arm the first full run found red was the suite's own defect: AC4 fed a real-READY body, which
REPLACES the tail and made the card smaller than the cap the arm had set from the larger card
before it; the arm now feeds a body without a READY line, the path that grows the card.

**Evidences:** KICK-aReplayedCard-2

- AC1 — `--card --append --session t2` — a body citing `skills/session-kickoff/SKILL.md:47-60` and `TOOL-cBriefedPilot-11` with a READY line at `git rev-parse HEAD`, run as `--card --append --session <nonce>-k2a` in the clone's linked worktree: exit 0, the body in the card, no `UNVERIFIED` line, the card ending with the body's READY line; `git` and `python` shims on PATH logged each argv, and exactly one `ls-files -- …` line and one `…corpus_ids.py --print-defined-ids` line were counted (the reader's own hygiene probe is a bash grandchild that logs `ls-files memory/` on its own account, which is why the count keys on the argv shape; python's subprocess spawns never reach a shim). Red in run A.
- AC2 — `UNVERIFIED — <token>` — `nope/missing.md:1-2`, `skills/session-kickoff/SKILL.md:1-99999`, the fixture slug's cited-only unit 11 and its unit 1 (beside its defined unit 10) each got its own annotation line directly beneath its row — the range one reading `(past end: 274 lines)`, the count `awk` took from the file — while `skills/session-kickoff/SKILL.md:1-3` and the defined unit 10 got none; exit 0; stdout named four misses. Red in run A.
- AC3 — `DEAD PROBE` — a body of one prose line and a READY line: stdout `MANIFEST env ERROR — DEAD PROBE: nothing to check …`, exit 1, `cmp` found the card byte-identical. Red in run A (the verdict) and run B1 (the bytes).
- AC4 — `CARD_CAP_BYTES` — `CARD_CAP_BYTES` set to the card's size plus 8 and a no-READY body piped: exit 2, the message `the card would be <n> bytes, <m> over the <cap>-byte cap`, the card byte-identical. Red in run A and run B1.
- AC5 — `READY —` — a fresh card: a body whose only READY line is `READY — none yet` exited 0 and left one READY line, the sentinel, last; a body with a real READY line left one READY line, the body's, and the earlier `## open` section went with the tail; a second body without one sat directly before that real READY line, the card holding one READY line and one `## task`. Red in run A (the body's line), run B2a (last, replaces, survivor) and run B2b (exactly one).
- AC6 — `--card --check --session t2` — over the card after AC1, exit 0 and empty stdout; over the card after AC2, exit 1, one line per miss such as `UNVERIFIED — <fixture unit 1> · line <n>`, and exactly four `UNVERIFIED —` lines, so the stored annotations were skipped rather than re-reported. Red in run A.
- AC7 — `bash skills/session-kickoff/manifest-check.test.sh` — `PASS (166 assertions)` on node `a` against `FLOOR_ASSERTIONS=165` (the floor counts every arm that runs on every node; the exact-tag arm is node `a`'s alone); `python tools/memory-tree/check-arms.py --check` exit 0 with `ARMS_FLOORS` untouched at `manifest-check.sh:28:28`, no refusal being a `fail` call.
- AC8 — `git rev-parse HEAD` — a READY line at `git rev-parse HEAD~8`: exit 2, the message naming `base <that sha> is not HEAD <HEAD>`, the card byte-identical. Red in run A and run B1.
- AC9 — `manifest-check.sh:60` — resolved to the one tracked file with that basename and got no annotation; `README.md:1` got `UNVERIFIED — README.md:1 (ambiguous: 129 matches)`, 129 being the count the suite took from `git ls-files` by basename at observation. Red in run A.
- AC10 — `--card --append` — a card written by `--card --write` in worktree A, appended from linked worktree B with a 60-row body under a cap of the card plus one and a half bodies: exit 0, the `tree —` line equal to the one the suite composed from B's `git rev-parse --show-toplevel`, `worktree`, `branch card-wt2`, B's HEAD and B's dirty count, the other startup lines byte-identical to A's card; a second 60-row body from B exited 0 under the same cap and left one READY line, one `## task` and the second title only. Red in run A (the cell, the counts), run B2a (the second body) and run B3 (the startup lines).
- AC11 — `--card --check` — the AC5 card with `## task` renamed by the suite's `sed`: exit 1, `carries a real READY line and no '## task' section`; renamed back: exit 0.
