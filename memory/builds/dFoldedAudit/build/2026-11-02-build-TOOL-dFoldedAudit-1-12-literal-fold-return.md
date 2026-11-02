# dFoldedAudit — unit 1's rev-7 fold return

**Serves:** journal TOOL-dFoldedAudit-1

**TOOL-dFoldedAudit-1 is at rev-7. Its status stays INPROGRESS, it has a §9 line, and nothing is committed.** I edited this one spec only.

**One choice for you to check: item 4 uses neither of the brief's two options.** Both only cover the memory root, and a longer install prefix causes the same red with no fix. The prefix reaches 13 sites (6 `{{KIT_DIR}}`, 7 `{{TOOL_ROOT}}`), so a prefix 12 characters longer than `tools` also passes the ceiling, with 155 bytes of headroom.

The Budget clause now runs only where `.governance/deploy.toml` declares `gov_source = "."`, and everywhere else it prints `not graded here`. Three things back this:
- It is the source-repo test the same script already uses at `:298-299`.
- `tools/template-size-limits.txt:110-116` says the gate is a property of this repo.
- `build-method size` is already an `[[exempt_leg]]`.

The cost is stated in §4: no gate reports an adopter's render past the ceiling. The two named options are under Alternatives rejected. If you want one of them instead, only the predicate, AC15 and the arm's case change.

| Item | Change | Observation |
|---|---|---|
| 1 | The fence now spells `policy.py get review.spec-audit.disposal`, and §4 says why | AC12: `tools/policy` prints 0 in the template and its render; the leg is owed to the close |
| 2 | `install-prefix (shipped surface)` added to the §7 line | `tools/check-spec-tokens.py` reads the line; the AC12 clause covers the leg |
| 3 | Manifest added to Files touched, with S15, a "The kickoff manifest" sub-head and the exact delta line | AC16, on the pass commit, owed to the close |
| 4 | Clause scoped by `gov_source`, S13 updated | AC15 runs the block alone in a scratch fixture; the parity `New arm:` gains a 30-character-root case that reds with `gov_source = "."` and stays green with `.governance/deploy.toml` absent |

**Additions beyond the brief:**
- §7 also names `kickoff-manifest ratchet`, the leg that reds a missing stamp.
- A case in AC15 counts only if the render really measures past the Budget line, so a small render can't pass by accident.

**The saved patch is not ready to apply as it stands.** Besides the two banned literal lines, the header flip and the ledger, the rebuild must:
- wrap the Budget clause in the §4 predicate;
- stamp `last-audit`;
- put the delta line in the commit message;
- declare the manifest at dispatch.

**Gates I ran:**
- **`memory hygiene`:** exits 1 on check 9 only, a stale `memory/builds/dFoldedAudit/README.md`. That is the main loop's regeneration, and no finding names this spec.
- **`lexicon naming predicates`:** exits 1, with 1214 verb offenders over a pin of 1212. I edited only a spec, and the offenders listed are in other builds' `.sh` files, so this doesn't come from rev-7. It will still show at the bar.
- **Not run:** `tools/check-spec-tokens.py`, which is the main loop's after this pass. I also ran no fixture for the new clause, because that would mean running the parity leg. Its size figures are arithmetic, and AC15 and the arm observe them.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-1.md`
