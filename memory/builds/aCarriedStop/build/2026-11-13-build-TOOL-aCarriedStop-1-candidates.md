# aCarriedStop — the candidates, their tests and the design handed to the spec

**Serves:** research TOOL-aCarriedStop-1

Write the Tier-2 spec for TOOL-aCarriedStop-1 at memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md, status SPECCED. Read the build README and the prompt record under memory/builds/aCarriedStop/ first. Never write under memory/builds/dDeclaredLoop/.

THE DEFECT. `check_chain_dispatch` in tools/unattended/unattended.sh refuses every `--dispatch` at check 118 while `read_chain_verdict` is not STOP. A chain build whose spec run landed before `--record-round` existed has no tracked `-chain-rounds.md`, so its build run reads `round 0 · CONTINUE · reason unreviewed` and dispatches nothing, although the owner ended the chain in a tracked record under the build's `prompts/` folder.

THE MECHANISM THE MAIN LOOP CHOSE BY M12 AND M3 (verify each claim against the code and correct the spec, not the code, where I am wrong):
- One new row kind in the chain record: `round <N> · owner-stop · record <repo-relative path>`.
- Writer: `--record-round <slug> --owner-stop <path>`. With `--owner-stop`, the four flags `VERB_REQUIRES` lists for `--record-round` are not owed and `--subject`, `--audited`, `--blockers`, `--highs`, `--finding` and `--sibling` are each refused, so the row is never mixed with an audit round. N is the record's last round plus one, counted over EVERY `round <N> · ` row (today `write_chain_round` counts `subject` rows only, so a round after an owner-stop row would reuse its number: fix that count). The path must be a file `git ls-files` tracks under `<memory root>/builds/<slug>/prompts/`, holding no separator ` · `, no whitespace and no newline. Every refusal is a value of `check_chain_fault`, check 118: no new check number, because the census is at its ceiling. A new record is named from the first roster id, since no audited id exists. The verb still needs no run-state file and stages the record as today.
- Reader: `derive_chain_verdict`'s awk admits the row, and when the LAST round of the record is an owner-stop row the verdict is `STOP · reason owner-stop`, read before the unreviewed test and before the ceiling. A later audit round appended after it supersedes it, since the verdict reads the last round: that is how the owner's "one more round" reverses it. `print_chain_verdict` and `check_chain_dispatch` both print it through the one derivation; add ` · record <path>` to the verdict line and the dispatch line if that fits the existing line grammar.
- `read_unrecorded_exits` and the leg in tools/unattended/check-unattended.sh read `subject` rows only and skip other rows: verify, and state it.
- Documents: the `--record-round` and `--chain-verdict` entries of tools/unattended/VERBS.template.md, the usage synopsis at the top of unattended.sh, and the command block of tools/unattended/SKILL.template.md; memory/guides/UNATTENDED-VERBS.md and .claude/skills/unattended/SKILL.md are their rendered copies, re-rendered by the kit's own render. BUILD-METHOD M4 is a governance carrier and is NOT edited.
- What it does not check: that the owner wrote the cited record (a forged row passes, as a forged STOP round does today); that the record says "stop".

CANDIDATES TESTED AND THE TEST EACH LOST (record in §10 per M12; I ran these on 2026-11-13 at d646814e4):
- A, dispatch reads a `specs-audited` override row from the spec run's run-state record. Test: over the 16 DEFERRED chain builds declaring `spec-audit:` with no chain record, does every `override · item specs-audited` row name an owner ruling? LOST: memory/builds/dSafePassage/ holds two such rows and the second (2026-11-02) cites the M4 precision floor and no owner ruling, so the row kind cannot tell an owner stop from an ordinary unaudited close without parsing free prose. Also 15 of the 16 have no rotated `RUN.LANDED.*.md` yet, only `RUN.md`.
- B, the gate honours a preflight waiver of `specs-reviewed`. Test: can a waiver tell a chain the owner ended from a chain whose record reads CONTINUE? LOST: a waiver is a per-run fact with no chain state, so it would also pass a live CONTINUE and a HOLD, reopening TOOL-dFoldedAudit-9's H1; and an attended run has no preflight. No waiver row exists in memory/builds/dScopedBuild/RUN.md to carry either.
- C, the owner-stop row. Test: do all 16 builds hold a tracked record under `prompts/` the row could cite? PASSED: each one's override reason cites such a file (names vary: `owner-review-stop`, `owner-stop-chain`, `owner-review-until-no-high`, `owner-audit-cap`), which is why the row cites a path and matches no file name.

ACCEPTANCE the spec must carry as observations, each with its command, in the existing fixture style of tools/unattended/unattended.test.sh (the `run_chain` and `check_gate_refused` helpers near its check 118 arms):
1. RED case: fixture past the cutoff, `spec-audit` pinned, no chain record: `--dispatch` refuses at check 118 naming the audit (today's bytes, unchanged).
2. GREEN case: same fixture after `--record-round <slug> --owner-stop <tracked prompts record>` and a commit: `--chain-verdict` prints `round 1 · STOP · reason owner-stop` and `--dispatch` admits the pass.
3. The writer refuses an untracked path, a path outside the build's `prompts/`, and `--owner-stop` beside `--subject`.
4. An audit round recorded after the owner-stop row gets the next number and the verdict follows that round.
5. An existing record with rounds reading CONTINUE, then an owner-stop row: STOP.
6. Both rendered documents name `--owner-stop`.
Declare each new suite arm on a `New arm:` line. New refusal texts must be assertable whole by an arm (check-arms reads the longest literal slice), so no `${var%%…}` expansion inside a message.

§8: decide these here as RESOLVED forks with the M3 reasoning, or correct me: (a) owner-stop passes a HOLD at the ceiling too, because the owner's ruling is the answer a HOLD waits for; (b) a flag on `--record-round`, not a new verb, because the verb list and its census gates grow with a verb and the row belongs to the one record that verb owns.

Return: the spec path, its status line, and every claim of mine you found wrong.
