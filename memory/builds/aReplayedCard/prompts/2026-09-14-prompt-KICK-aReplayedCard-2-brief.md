# Brief — KICK-aReplayedCard-2, the append and the citation check

**Serves:** journal KICK-aReplayedCard-2

What this pass is handed: the unit's spec at rev-4, the build README, and
`skills/session-kickoff/manifest-check.sh` as `KICK-aReplayedCard-1` left it at `711332c3` — the
`--card --write|--replay|--path` verbs, `CARD_CAP_BYTES`, the `render_card`/`derive_node_tag`/
`write_card`/`print_replay` functions, a self-test at `FLOOR_ASSERTIONS=109` whose fixture is a
scratch clone with a linked worktree and a per-run nonce, and its acceptance ledger under `build/`
that names how each arm was staged RED.

What it builds: `--card --append --session <sid>` and `--card --check --session <sid>` on the same
checker, the batched citation check, and one print verb on `tools/memory-tree/corpus_ids.py`.

What is not obvious, each verified at the base:

- **Reuse unit 1's fixture, verbs and refusal shape.** The self-test already builds the scratch
  clone and the linked worktree AC10 needs; add arms to it, do not build a second fixture. Refusals
  are the `MANIFEST env ERROR — …` shape with exit 1 or 2 as the spec says, never `fail N`;
  `ARMS_FLOORS` stays at `manifest-check.sh:28:28` and `FLOOR_ASSERTIONS` moves by your arms.
- **Two spawns, not a per-token loop**: one `git ls-files -- <paths>` for the path tokens and one
  `python tools/memory-tree/corpus_ids.py --print-defined-ids` for the id tokens; AC1's arm shadows
  `git` and `python` with counting functions. `corpus_ids.py` is `tools/memory-tree/`'s and its
  own self-test (`--selftest`) and the `gotchas selftest`/`memory-hygiene self-test` legs are held;
  run `python tools/memory-tree/corpus_ids.py --selftest` yourself after adding the verb, and the
  hygiene-parity test beside it if one names the verb list. The verb prints the DEFINED set — the
  ids a spec H1, a backlog row or a decision row defines — one per line, and nothing else.
- **A path token is a slash plus an extension**, the rule at `tools/check-spec-tokens.py:142`, plus
  a basename with an extension followed by `:<line>`, resolved against `git ls-files` when exactly
  one tracked file has that basename and annotated `(ambiguous: <n> matches)` otherwise. The id
  regex comes from the families `.memory-tree.conf` declares, as `corpus_ids.py` exposes it.
- **The card the append writes is what `TOOL-aReplayedCard-1` reads**: exactly one `READY —`
  line; the sentinel `READY — none yet` replaced only by a real READY line; a second real READY
  append REPLACES the previous READY line and the six sections beneath the startup lines, so the
  card carries one body; the `tree —` cell REWRITTEN to the toplevel the append runs in, spelled as
  `git rev-parse --show-toplevel` prints before the script's `pwd` normalisation, exactly as
  `write_card` spells it; and the header line untouched, because the deny reads its writer verb.
- **A READY line whose `base <sha>` is not `git rev-parse HEAD` at append time is refused** naming
  both shas; a body with no path-shaped and no id-shaped token is `DEAD PROBE`, exit 1; an append
  that would exceed `CARD_CAP_BYTES` is refused with the overage and the file is byte-identical.
- **`--check` skips its own `UNVERIFIED —` lines**, and refuses a card carrying a real READY line
  and no `## task` heading. It writes nothing.
- **The card home is the shared common dir**; every arm runs in the scratch clone and its linked
  worktree, and unit 1's cleanup arm keeps holding after your arms.
- **Function names lead with a table verb** (`sh:shell-tokens:parser`): the spec's are
  `extract_card_tokens`, `check_card_citations`, `add_card_body`; the python one is
  `print_defined_ids`. Ask `python tools/lexicon/lexicon.py --suggest <name> --as sh` before
  inventing another.
- **The manifest owes `last-audit`** — `manifest-check.sh` is in `watch:` — with the delta line in
  the commit message; the body does not change, so `last-body-change` stays. Run the checker plain
  and `--staged` before committing.
- **The acceptance ledger** is `2026-09-14-build-KICK-aReplayedCard-2-1-acceptance-ledger.md` under
  `build/`, `**Serves:** journal KICK-aReplayedCard-2`, one `**Evidences:**` block, AC1–AC11 in the
  OBSERVED form, every backticked token on the bullet's first physical line — check 23 joins per
  line, which unit 1 learned the expensive way; `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md`.
- **Author with the Write tool, LF; `tr -dc '\r' | wc -c` counts CR bytes, `grep -c` does not on
  this node** (`memory/gotchas/msys-grep-counts-cr-on-every-line.md`). Finish with the records:
  spec status CLOSED with today's date, `gen_build_index.py --write`, `git add -A`, the hygiene
  gate (minutes, never through `tail`), `python tools/check-spec-tokens.py`, the checker's own
  self-test, `python tools/memory-tree/check-arms.py --check`, and commit with the unit id in the
  subject. No push, no merge.
