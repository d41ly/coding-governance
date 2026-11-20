# TOOL-dPlacedRequest-4 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-4

The unit was built from its spec at rev-7 (PINNED) on base `7936d33ed`. `tools/loop/placement.py` is new:
the verbs `place`, `check` and `record`, the functions `tools/loop/placement.py#place_request`,
`tools/loop/placement.py#check_placement`, `tools/loop/placement.py#read_placement`,
`tools/loop/placement.py#print_claim_lines` and `tools/loop/placement.py#check_reenters_item`, the table
`tools/loop/placement.py#STAND_INS`, and fifteen (DERIVED) fixture plants, the fifteenth, `refusals`, added
by the checklist pass. The unattended driver gains
`tools/unattended/unattended.sh#check_prompt_placement`, called at the first preflight beside
`check_prompt_brief`, refusing by check 119 (DERIVED, the next code free after 118); the two (DERIVED) `fail 31`
sites of the `--landed` verb's LANDING test were merged into one, byte for byte, to pay for it under the
driver's refusal ceiling. The orienter role's `returns:` line and body gain the placement return, its render
and the roles catalogue re-rendered; the prompt path's step 3 gains its placement sentence in the verbs
template and its copy; `help/loop.md` gains a placement section. The leg `loop placement fixtures` is
registered as `loop probe fixtures` is, with `enforces = ["principle.p22"]`; the pending list held no
`principle.p22` row, so `tools/playbook/core-pending.txt` is unchanged.

No gate, suite or bar ran in this pass, and no `--selftest`: the role hook refuses one. Each criterion
below was observed by a probe of the changed code: one `--fixture --plant` case of `tools/loop/placement.py`
run by direct CLI, or `--fixture` over every plant, which printed `placement: fixtures · PASS · 14 case(s) ·
0 failed` (DERIVED) in 27 s (PINNED, the run's node, 2026-11-20).

**Evidences:** TOOL-dPlacedRequest-4
- AC1 — `--plant each-disposition` placed one request per member of the nine (DERIVED), each block
  reading that `disposition:` and a `reason:` line, and a return with no reason exited 1 writing no block.
- AC2 — `--plant unknown-word`: `adopt` exited 1 naming the word with no placement file written, and
  `attach` was written `disposition: amend`.
- AC3 — `--plant agent-places`, `--plant declared-checked` and `--plant owner-places` read `placer:`
  `agent`, `declared` and `owner`; under `owner-places` with no record `place` printed `placement: owner
  item — <key>` and the return as evidence, and wrote no block.
- AC4 — `grep -n "disposition · reason · evidence · observations"` over the role file found its
  `returns:` line, and `python tools/roles/check_roles.py --write` reported 0 defects (DERIVED) after
  rendering the catalogue region; `render_agents.py --write` wrote the orienter's render.
- AC5 — `--plant secret-reason`: the reason read `ghp_<redacted:github-token>`, the token absent, and a
  reason of 1024 bytes (PINNED) was written as 240 bytes (DERIVED, `VALUE_CAP`).
- AC6 — `--plant continue-closed` and `--plant amend-leased` each exited 1 under `refuse`, naming
  `is CLOSED, not live` and `the build lease of dLive reads`, and 0 under `record` with the block's `check:`
  opening `recorded`; the leased plant pushed a foreign build lease to a bare remote and read it through
  the driver's `--claims`.
- AC7 — `--plant observation`: `place` opened the request's probe trigger, `check` exited 1 naming
  `observations-unverified`, and passed once the plant wrote the probe record's `Verdict`.
- AC8 — `--plant claim-lines`: `record` on the passed `new` block printed exactly the four (DERIVED)
  lines `disposition`, `build`, `playbook` and `reason`, and on the refused `patch` block printed nothing
  and exited 1.
- AC9 — `--plant routes-to-plan` answered `held-owner` and printed the owner item naming
  `refs/gov/claims/dLive`; `--plant owner-released` answered `pass` once the owner's disposition record
  naming `item.entry.place` with the placement's own word was committed, after a record disposing `ask`
  refused it.
- AC10 — `--plant prompt-continue` sourced the driver and called `check_prompt_placement` over a
  prompt-mode README opened past the conf's cutoff: `disposition: continue` exited 1 printing `UNATTENDED
  check 119 FAILED` naming `the disposition continue` and `dLive`, and `disposition: new` with a placed,
  passing block exited 0. The suite arm in `tools/unattended/unattended.test.sh` is OWED at the close,
  waived for this build's landing by the README's last build-level rule.
- AC11 — `python -m json.tool gate-legs.json`, run in the tools folder, printed the row named
  `loop placement fixtures` with `enforces` holding `principle.p22` and the argv
  `{prefix}/loop/placement.py --fixture`.
- AC12 — `--plant late-answer`: `TOOL-tFix-1` was refused by `check_reenters_item` with no block written;
  the `reenters: TOOL-tFix-1#F2` block was returned by `read_placement`, kept by a passing `check`, and
  printed by `record` right after `disposition`; a block without the line read `none` and `record` printed
  no `reenters:` line.

**The checklist pass.** `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` over the build commit
selected 65 (DERIVED) classes. Acted on: refusal-branch-with-no-arm, by the `refusals` plant, which reaches
a bad key, no placement, an unreadable return line, a key given twice, a bad slug, an escaping playbook
path, a mode mismatch, each disposition's failing fact and a filed ask's pass, and two bad owner records,
and by an unreadable-lease case in `amend-leased`, the remote removed and the fact recorded;
owner-item-without-its-reject-outcome, by `check` refusing a held placement whose owner record disposes
another word, observed by `owner-released`; two-answers-to-one-question, by
`tools/unattended/unattended.sh#read_readme_opened`, the one reader of a README's `opened:` the three
prompt-mode grades share; criterion-asserts-what-its-own-command-cannot-show, by AC11's own command above;
budget-row-not-remeasured-after-added-arms, by re-pricing the leg's row from 42 s (PINNED) over every
plant by direct CLI. The leg itself is no longer run whole in this pass: once registered, the role hook
refuses `--fixture` without a plant.

**Owed at the close:** the `loop placement fixtures` leg and its RED-first observation, staged by
`continue-closed` with the check reading the return's text; the `unattended.test.sh` arm of AC10 and its
RED-first observation, staged by removing `check_prompt_placement`'s call; the existing prompt-mode arms of
that suite, whose records now carry `## Placement` over a block planted once in the fixture's store; and
the pass legs over this commit.
