# TOOL-dRedressedBar-2 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-2

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 2 rev-3, which is
still its current revision, in the one pass commit `c7a9213d1`. The readings below are the
builder's, from that commit's body and from its return in
`2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
`2026-10-14T14:23:16 · gov-builder · wf_eb13c24a-b41/af59039234e86d2c9` at line 4655. No merge
bar, no self-test suite and no gate leg ran in the build pass. Every reading is a direct probe, and
the section 7 legs were owed to the close.

**Evidences:** TOOL-dRedressedBar-2
- AC1 — `grep -nw clean` — over `tools/unattended/gate-guard.js` it printed nothing, and
  `grep -n renderAskQuote` printed exactly lines 689, 694 and 696: the declaration and the two
  calls, all inside `extractAskQuestions`.
- AC2 — `extractAskQuestions` — a node probe ran it on the tip's file and on
  `git show ebce889c:tools/unattended/gate-guard.js` written to scratch, over a payload with a
  400-character question carrying a BEL and a C1 byte, a label carrying a NUL, a non-string label,
  a blank question and a null question, then `{}`. The two outputs were byte-identical. The first
  question read 300 characters, and `{}` read `[{"question":"(no question text)","labels":[]}]`.
- AC3 — `--measure` — it printed `VERB_OFFENDER_PIN="1087"`, matching `.lexicon.conf:268`.
  `--suggest renderAskQuote --as js.function` printed `OK — renderAskQuote leads with render...`,
  and `--offenders` listed 1087 verb offenders and no line naming the gate guard. The builder ran
  the three again after the map regeneration and read the same.
- AC4 — `memory/map/generated/symbols.json` — at the tip it held `renderAskQuote` once and `clean`
  zero times for the gate guard, and the `3d1adca9` copy held `renderAskQuote` zero times and
  `clean` once. `gen_map.py --check` exited 0. `git show --name-only --format= c7a9213d1` listed
  the gate guard and `symbols.json`, and no other path under `memory/map/`.
