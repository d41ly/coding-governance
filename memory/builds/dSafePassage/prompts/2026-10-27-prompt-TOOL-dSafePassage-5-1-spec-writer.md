**Serves:** research TOOL-dSafePassage-5

# Brief: TOOL-dSafePassage-5's release-0 applies at the pin — F3's take-out rule applied to what the pin refuses

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-5 back as a DIVERGENCE before code (`wf_03aacba1-129`), and the run revises the spec under M2 by the rule §8 F3 already records.

## The brief

### Goal

Release-0 applies with exit 0 at the pin `60d90cb71db51e651aa1c5efe3f6d48ba21a997d` (S2, AC2): §4's fixture deploy.toml and the seed carry what the pin's adopters need, and every kit whose adopter cannot exit 0 there is taken out by a `kits` line and named with its refusal — F3's own resolution — so the unit is buildable.

**The defect.** §4 "The fixture files" gives deploy.toml "no `kits` line, since `apply --all` derives the selection". At the pin, `playbook-render`'s adopter refuses any deploy.toml with no `kits` (`tools/playbook/render_playbook.py:967`, `read_kits`: "declares no `kits`, so every kit: fence in the template would drop ... Intake cannot write an empty selection, so this is a hand edit"). F3 (RESOLVED, agent, 2026-10-23) already says: "a kit whose adopter cannot exit 0 at the pin with the seed is taken out by a `kits` line and a rev bump of this spec naming the kit and its refusal, never silently".

**What the builder measured** (the pinned clone's own `govkit.py apply --target <t> --all` into a bare scratch target):
- Gov's deploy.toml answers, rewritten to `ANSWER_VALUE_RE`'s characters `[A-Za-z0-9_./~@+:, =-]`, are not enough: `apply` exits 2 until `playbook_path`, `playbook_dir` and `memory_root` are given. Gov's deploy.toml carries none of the three.
- With those added, `apply` exits 1 with 19 problems: `playbook-render` (the refusal above); `process-monitor` (`PROCMON_ROOTS` blank); `unattended` (`no-project-layer`); `agent-instructions` (exit 2, nothing on stderr); `review-harness` (its 5 rendered files absent; `unattended` leaves its rendered files absent too); 20 `lf_pin` patterns resolving to no tracked path; the leg `agent-cap restatement` withheld for want of `tools/agent-cap-restatement-waivers.txt`.
- `memory-tree` (seed-and-stop) and `roles` (exit 3) were accepted stops.
- A plain `git clone` carries `archive/*` tags; the untagged clone of S2 and S11 needs `--no-tags` or tag deletion.
- The floor step's down (`python_floor.py down 3.11`) over the committed release-0 target printed "no finding", exit 0.

### Items

1. **Revise TOOL-dSafePassage-5** as a rev bump dated 2026-10-27, still `DEFERRED`, applying F3's rule: §4's deploy.toml carries a `kits` line — every non-conditional registry entry at the pin minus each kit whose adopter cannot exit 0 there with the seed — and F3 gains a line per taken-out kit naming it and its refusal (as measured above; re-measure at the pin where a reason is unclear, by reading the pinned adopter, never by building). Say whether the selection still counts as `apply --all` for S2 and F3 once a `kits` line is present, and make S2/AC2's wording match. The seed or fixture deploy.toml supplies `playbook_path`, `playbook_dir` and `memory_root`. Each remaining problem is answered by the seed or by taking its kit out — none left standing; the `lf_pin` and `agent-cap restatement` items say which. S2/S11's clone is untagged (`--no-tags`). One §9 line names this brief.
2. **Cross-read** TOOL-dSafePassage-26 and -61 (consumers of 5) on M2's axes; a disagreement in a DEFERRED spec is fixed there with a rev bump and §9 line.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- §4's deploy.toml row carries a `kits` line, and F3 names each taken-out kit with its refusal.
- No problem in the measured list is left without a disposition in the spec.
- With 5 (and any spec you changed) flipped to `INPROGRESS` in a scratch working tree, `python tools/check-spec-tokens.py` prints no line naming them; restore the status. If the scratch guard refuses the checker for your role, say so.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no change to a pinned adopter; no edit of a CLOSED spec.
- No commit, no stage into the real index, no deviation record.
