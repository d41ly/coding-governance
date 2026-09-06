**Serves:** journal TOOL-aHoistedPass-5

# Acceptance ledger — TOOL-aHoistedPass-5

Tier-2 · node a · 2026-09-05 · landed at `01c07a97`

`tools/workflows/unattended-unit.js`: one unit, one agent, oriented in that unit's spec and brief and
never in the roster. Under the hoist the parent ends after DISPOSAL and returns the ordered roster;
without this file the hoist has no callee.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-5

- AC1 — MET — `node tools/workflows/check-workflow-syntax.js` exits 0 with the file landed.
- AC2 — MET — the staged break. With `export default async function run() {}` added, the same gate
  exits **1**. Restored after, and it exits 0 again.
- AC3 — MET — `bash tools/workflows/check-verifier-fanout.sh` exits 0 with the file in its
  discovered population.
- AC4 — MET — the staged break for the fan-out guard, `agent-cap.js` on stdin. The landed file plus
  `for (const u of cfg.units) { await agent('x') }` exits **2** from
  `node tools/hooks/agent-cap.js`, with the verify-stage cap message. The pristine file exits **0**
  in BOTH `script` and `scriptPath` input modes, so the mode is not doing the work.
- AC5 — MET — `python3 tools/codebase-map/test_codebase_map.py` exits 0 and
  `gen_map.py --check` exits 0 with the file landed and claimed.
- AC6 — MET — the staged break for the liveness floor in `gen_map.py --check`, F1's whole argument. With the
  one top-level definition replaced by a bare `const`, `gen_map.py --check` exits **1**; restored, it
  exits 0. That is the floor doing its job, and it is why the child yields rather than the floor.
- AC7 — MET — `bash tools/check-install-prefix.sh` exits 0 and the carrier file is unchanged: this
  file needs no row.
- AC8 — MET — `grep -c 'tools/'` over the landed script prints `0`.
- AC9 — MET — with `//` comment lines removed the file holds exactly one `await agent(` and no loop,
  array method, Promise combinator or arrow.
- AC10 — MET — the prompt names the `CLOSED` / `WONTDO` flip and says why it is load-bearing: the
  status header is the only fact `--plan` reads to decide a unit is finished.
- AC11 — MET — there is no `roster` KEY and no `reportPath` key. The two textual hits are prose, in
  `meta.description` and in the prompt's sentence about the parent roster, and neither is an args key.
- AC12 — MET — `bash tools/workflows/check-review-join.sh` exits 0.
- AC13 — MET — the header claims no enforcer the inventory does not support. `export const meta` is a
  SELECTOR, so deleting it removes the file from both readers rather than failing either;
  that nothing checks it never nests; that the straight-line rule has no enforcer and now carries one
  deliberate exception, argued in place; and that `function`, `=>` and a non-receiver `.map` all
  ADMIT at the shipped hook.
- AC14 — MET — evaluated the way the runtime does, `export` stripped and the five globals supplied,
  the script runs to its return with all eight keys present.
- AC15 — MET — handed `args` as a JSON STRING, the parse guard accepts it; a string missing a key
  throws naming that key and its reason — observed on `{"repo":"."}`, which threw
  `args must carry an explicit \`slug\`. Every driver verb in the prompt below is slug-addressed.`
- AC16 — MET — all five of S4's acts are greppable in the landed prompt, `--brief` among them: the
  read-both-whole step, the CHANGE THE SPEC FIRST divergence rule, `--dispatch` with `--writes`, and the
  checklist command token. Added at rev-5, because S4 had five acts and no criterion, and no standing
  leg calls this file at all.

## What the spec could not have known

**F1's resolution named a function the merge bar would have refused.** rev-4 fold-confirmed the one
top-level definition as `function need(key, why)`. Measured live: `lexicon.py --check` reports
`P1 verb graded=1060 offenders=467` against `VERB_OFFENDER_PIN="467"` — AT the ceiling with zero
headroom — and `.lexicon.conf` declares this suffix a probe layer whose functions pattern grades that
definition, on a leg guarded at `tools/`. The commit landing this file would have reached 468 and
redded. Section 7 named the leg nowhere and the words "lexicon" and "verb table" appeared nowhere in
the spec.

The definition is `check`, which the declared table carries and whose gloss — assert a predicate and
return a verdict — is exactly what the eight argument refusals do. Raising the pin was refused in
writing: a pin raised so one name may sit outside the table turns the table into a synonym list,
which is the failure the lexicon's own rules name. Post-landing measurement: offenders still 467,
`lexicon.py --check` exit 0.

**The map claim pushed a dossier over its cap.** Adding `"unattended-unit.js"` to
`memory/map/features/unattended.md` took it to 20500 bytes against a 20480 cap. Trimmed by
compressing a paragraph that gave the same three-carrier count twice, not by raising the cap.
