# TOOL-aQuotedBrief-1 — build brief

**Serves:** journal TOOL-aQuotedBrief-1

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry.

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-1.md`, then the prompt-path
  section of `tools/unattended/VERBS.template.md` and `verb_preflight` in `tools/unattended/unattended.sh`.
- **Write set.** Declare exactly these with `--dispatch` before writing:
  `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/VERBS.template.md`, `tools/unattended/SKILL.template.md`,
  `tools/unattended/PROTOCOL.template.md`, `tools/unattended/.unattended.conf.example`,
  `memory/guides/UNATTENDED-VERBS.md`, `memory/guides/UNATTENDED-PROTOCOL.md`,
  `.claude/skills/unattended/SKILL.md`, `.unattended.conf`, `memory/map/generated/symbols.json`.
  Declare no generated memory index; the main loop owns those.
- **Placement.** `check_prompt_brief` is called in `verb_preflight` right after
  `check_waiver_scope || true`, as `check_prompt_brief "$slug" "${base:-}" || true`. It returns 0 at
  once when `AUTH_MODE` is not `prompt`, when `base` is empty, or when the cutoff does not apply.
  It reports through `fail <n>` so it joins the one-pass refusal list. Take the next free fail numbers
  above the highest in the file; put every interpolation LAST in each message, because
  `check-arms.py` keys on the literal text before the first one.
- **The cutoff.** `PROMPT_BRIEF_CUTOFF` blank means OFF, announced once on stderr. Compare the README's
  `opened:` date read from the README blob at BASE, not the working copy. Declare
  `PROMPT_BRIEF_CUTOFF="2026-10-09"` in this repo's `.unattended.conf`; ship it blank in the example
  conf; add its §8 row to the protocol template and the render byte-identically.
- **Renders.** The two guides and the skill are renders of the templates. Regenerate them the way the
  kit does (find the render command in `tools/unattended/README.md` or `adopt-unattended.sh`); never
  hand-edit a render into a state the template does not produce.
- **Verification, fast and direct only.** Write the arms §7 names into `unattended.test.sh`, raise its
  `FLOOR_ASSERTIONS` by the assertions added, and observe them by SLICING the suite: the suite's
  prologue plus your new block in a temp script under `tools/unattended/`, deleted before commit.
  Observe each new arm RED against the pre-pass driver first, then green. Also run
  `python tools/memory-tree/check-arms.py`, `python tools/lexicon/lexicon.py`,
  `python tools/codebase-map/gen_map.py --write` and `bash tools/unattended/check-unattended.sh --only 22`
  if that flag exists, else skip it and say so. **Run no merge bar and no whole suite** — the main
  loop runs those once at VERIFYING.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-1 — <what>`, trailer
  `Pass: TOOL-aQuotedBrief-1`. In the same commit, set the spec's status to CLOSED only when every AC
  was observed (otherwise leave it SPECCED and say which AC is unobserved), and write the acceptance
  ledger at `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-1-2-acceptance-ledger.md`
  per `memory/HYGIENE.md` "Acceptance ledger": one `**Evidences:** TOOL-aQuotedBrief-1` line directly
  above the `- AC1 — …` lines, each carrying a backticked observation. Report the sha.
