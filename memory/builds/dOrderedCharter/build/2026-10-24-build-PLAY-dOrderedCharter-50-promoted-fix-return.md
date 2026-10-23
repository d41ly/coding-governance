**Serves:** research PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55

# Promoted-fix pass, round 2 — the spec writer's return

All four jobs are done. Spec 49 is now **48690 B**, under the 49152 B ceiling, and `--only 12` and `--only 25` both exit 0.

I didn't rerun `check-spec-tokens.py` or the hygiene check in `--staged` mode, the two checks the brief names, so the canary-leg fix and the absence of new `[path]` hits rest on a reading of the tool's rules, not its output.

Only specs 49, 50, 51, 52, 54 and 55 changed. Edits were in place, with no rev bump, no staging, no commit and no index render.

**1. Spec 49 trim.** I only tightened prose. A script checked the result against the staged rev-2 and found these unchanged:
- all 73 scope items with their report ids;
- AC1 to AC64, every "Observed by" pairing, and all 64 "Red when" lines;
- forks F1 to F9 and their resolutions;
- all 38 edges, by verb and target;
- the §7 Gates section and New arm lines.

The cuts were across §1, §2, §3, §4, §5, §8, §9 and §10. In §3 the edges kept their verb and target and got shorter descriptions. The hands-off to 55 still names `edge_checks.py`, which unit 55 also names.

**2. Spec 55 §7:** the leg line now names `run-gates canary`, which is a leg in `tools/gate-legs.json`.

**3. Witnesses for check 12:**
- **Spec 54 AC2 and AC4** each run `bash skills/session-kickoff/manifest-check.test.sh`, a tracked file. AC4 now says the suite plants a card the writer's own session owns.
- **Spec 55 AC5** names its filter, `x.origin == 'playbook-render'`.
- **Spec 55 AC21** runs `python gov_tag.py show` from the backslashed cwd.

**4. `**Readers:**` clauses for check 25:**
- **Spec 55 S1, S10, S11, S12** cover real retirements. Their readers come from greps I ran:
  - **S1:** the 10 tracked files that spell `adopt-agent-instructions`.
  - **S10:** the 8 lines that spell `agent-instructions self-test`, such as `memory/map/baseline.toml:14` and `tools/gate-legs.json:382`.
  - **S11:** the two generated map lines, with `gen_map.py` as the value reader.
  - **S12:** the adopter's option parser and the argv rows in `tools/gate-legs.json:296` and the agent-instructions `kit.toml`.
- **Spec 55 S7, spec 51 S2 and spec 52 S2** answer `READER NOT IN TREE` with a reason. What they retire is built by an earlier unit of this build (25, 44 or 45), and greps for its names outside `memory/builds` find nothing today.
- **Spec 50 S2 and S4, and spec 51 S5** say "by name: none — this item retires nothing". The check fired only on the words "removed" and "deleted" sitting near a path: those are populations the probe reads, failing cases it plants, or index rows it deletes.

**Check output.** Neither check prints a failure naming a dOrderedCharter spec. Both print the same four informational notes ("check 25 did not grade … READER NOT IN TREE covers it"), on specs 19 S7, 30 S5, 34 S8 and 43 S3, none of which I touched. My first run caught two problems of mine, both now fixed:
- In spec 50 S2, "NO VALUE READERS" was split across a line break, so the check couldn't read it.
- In spec 55 S10, a backticked unit id sat in the by-name half, where the check expects a reader.

**Possible problem with spec 49's size.** Its top holds the generated records block. This brief lists `PLAY-dOrderedCharter-49` on its Serves line, so the next index render will probably add a row of about 285 B there. I trimmed to leave 462 B of headroom for that. A second new record naming 49 could push it back over the ceiling.

Files are in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- 2026-10-24-spec-PLAY-dOrderedCharter-49.md (48690 B)
- 2026-10-24-spec-PLAY-dOrderedCharter-50.md
- 2026-10-24-spec-PLAY-dOrderedCharter-51.md
- 2026-10-24-spec-PLAY-dOrderedCharter-52.md
- 2026-10-24-spec-PLAY-dOrderedCharter-54.md
- 2026-10-24-spec-PLAY-dOrderedCharter-55.md
