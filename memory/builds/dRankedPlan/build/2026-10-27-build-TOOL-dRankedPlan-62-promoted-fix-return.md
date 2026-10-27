**Serves:** research TOOL-dRankedPlan-62

# The promoted-fix pass's return — dRankedPlan round 5

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-62-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-62-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

I fixed the one `[path]` hit in `TOOL-dRankedPlan-62`. It's not confirmed yet: the spec-token checker refused to run under my role (scratch-guard blocks gates for a spec writer), so you need to run it to verify.

**What the hit was.** The checker splits each backticked token in §6 into words and grades any word that looks like a path. `tools/loop/ratify.py` appeared twice in §6 and isn't tracked at HEAD:
- in AC4, inside the reported output `loop selftest <- tools/loop/ratify.py`
- in AC20, inside the command `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`

**What I changed**, in `C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-62.md`, §6 only:
- **AC4** now reads: it reports the `loop selftest` leg owed for the loop kit's `ratify.py` on unit 46's spec, and nothing for it once that leg line names `loop selftest`.
- **AC20** now reads: when `python tools/check-spec-tokens.py --legs-for` runs over the loop kit's `ratify.py` in S4's clone, it prints… The rest is unchanged except for a rewrap to stay near 100 columns.
- The full path stays in §2, §4 (Files touched included) and §7. The status header, `**Carries:**` line, §3 edges and §8 marks are untouched, and there is no rev bump, as the brief asked.

**Why the bare `ratify.py` won't become a new hit.**
- No tracked file is named `ratify.py`. The bare-filename check only runs when the checker sits at the repo root. Here `tools/gate-legs.json` sits beside the checker, so that check is off.
- AC8's existing `ratify.py` tokens confirm this: they were never flagged.
- The other §6 word, `"$0")/ratify.py` in AC8, opens with a quote, which the checker never grades as a path.

**Checks run:**
- I ran a probe copying the checker's §6 word-splitting and path-shape rule against `git ls-files`. It found no hits.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exited 0. No finding names a dRankedPlan file. The only dRankedPlan lines are check 25's notices that `READER NOT IN TREE` covers a name (on units 2, 3, 10, 16, 29 and 51), which means a waiver applied, not a finding.

**Still to run:** `tools/check-spec-tokens.py` in the main session, to confirm the hit is gone. Nothing is committed.
