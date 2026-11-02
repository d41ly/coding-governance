**Serves:** research TOOL-dSafePassage-103

# Brief: the policy kit reads gov's source-mode receipt as the source tree

## The prompt

> The close's bar on the prepared landing merge `f14f0f72c` (log at `C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/close-f14f0f72c.log`) reds the `policy check` leg on `arm_cap_census`: four findings, `manifest-bytes`, `manifest-line`, `manifest-trap` and `orientation-card`, each "its enforcer is not a file at tools/manifest-check.sh, where kit kickoff-manifest installs it", with 8 rows announced. The same leg reads 0 findings and 0 announced at main `f4597719e`. The cause: TOOL-dSafePassage-8 makes the landing's govkit update write gov's source-mode receipt, `.governance/install.json` with `"mode": "source"`, and the prepare's merge carries it, the first landing that does (it is absent at `60d90cb71`, `f4597719e` and `37b3bf328`). `policy.derive_census_tree` (`tools/policy/policy.py:1043`) answers ("adopter", receipt) for ANY receipt, so on gov's own tree the census reads each row's `installed` path instead of its `enforcer` path. Adopted under UNATTENDED-PROTOCOL §11: a measured red at the landing, nothing this repo measures gets worse.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-103: `derive_census_tree` reads a receipt whose `"mode"` is `"source"` as gov's own tree, answering ("source", <tool root>) by the registry search it already makes when no receipt exists, so a source-mode receipt never reads as an adopter's. Run the candidate predicate over the real tree first, per the charter's class rule: list every other reader of `.governance/install.json` that branches adopter versus source (`git grep -n install.json -- 'tools/*.py'` and their callers), state for each whether it already handles `"mode": "source"` (TOOL-dSafePassage-8 S6's `check-receipt.py` does), and fix in this unit only the readers the bar or a probe shows misreading it. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-8` with this brief's finding in §9, §6 criteria each with a Red-when (the leg's own `arm_cap_census` line from the log), §7 gates naming the `policy check` leg and a `New arm:` line for the regression check, §10 reuse, §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it.

### Items
- **Id 1 (high):** on a tree carrying gov's source-mode receipt, `python tools/policy/check_policy.py` prints `arm_cap_census · 0 finding(s)` with 0 announced, as at `f4597719e`; its red case is the four findings above. The fixture: a scratch clone of the build commit with `.governance/install.json` written as the source-mode govkit update writes it.
- **Id 2 (regression arm):** a check in the policy kit's own suite that a source-mode receipt reads as "source" and an adopter receipt still reads as "adopter".

### Non-goals
No change to govkit's source-mode update or to the receipt's shape; no edit to a CLOSED spec; no product code; no commit, no stage into the real index, no RUN.md row.

### Acceptance
Both items are carried in 103's text. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path, a code fragment that embeds a repository path, or a regex-escaped path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
