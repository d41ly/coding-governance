# Acceptance ledger — TOOL-aNimbleMend-1

**Serves:** journal TOOL-aNimbleMend-1

Built against spec rev-1 in the pass commits `2121531db` and `27cd3a9da`. Each line is a probe of the changed code the builder made in the pass and returned; the main loop wrote this record from that return. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section. The spec declares no new arm.

**Evidences:** TOOL-aNimbleMend-1
- AC1 — `python tools/policy/policy.py get bar.inline-red-fixes` — printed `on` and exited 0; the same verb printed `on` for `pass.fast-legs`.
- AC2 — `get pass.fast-legs --explain` — stderr named the key as a default, not set in the policy file at the landed revision 97e0841d.
- AC3 — `%TEMP%` — in a scratch fixture with both keys set to `off`, the reader printed `off` for each.
- AC4 — `fast-legs = "sometimes"` — in a second fixture the reader exited 2 with empty stdout and a refusal naming the line, the key and the allowed pair.
- AC5 — `python tools/policy/policy.py lists --check` — green with no finding, and the grep of `unsummarised-keys.txt` for either key printed 0.
- AC6 — `python tools/policy/policy.py mirror --check` — printed `mirror stale` after the first commit and `policy: mirror fresh` after the write; the grep of the mirror for the two keys printed 2. (PINNED, 2026-11-12)
- AC7 — `node tools/policy/policy-mirror.js get pass.fast-legs` — printed `on` and exited 0.
- AC8 — `tools/policy/README.md` — the criterion's grep printed 4 and its heading grep printed 1. (PINNED, 2026-11-12)
