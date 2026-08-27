# Owner prompt — aGroundedOrientation

**Serves:** research TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2

Handed to `/unattended --prompt`, node `a`, 2026-08-27. The value carried whitespace and named no
readable file, so by the Skill's value table it is the prompt itself and is recorded verbatim below.
There is no source path to record.

## The prompt, verbatim

> The unattended prompt mode doesn't use any of available CG toolkits during initial orientation: no
> memory recall, no gotchas, no lexicon for allowed verbs, no reuse probe - if any of the kits are
> wired and available. Understand if using any of the tools is meaningful during the early build
> orientation and build it in if the answer is YES.

## What orientation established, before the roster was written

The prompt names four kits. Orientation ran each against this build's own subject, which is the test
that discriminates between them, and the answers are not uniform.

- **`codebase-map` reuse probe** — MEANINGFUL, and already named in the kickoff engine's Step 4.
  Returned the `unattended` affordance seam and `UNATTENDED-PROTOCOL.md` for this build's phrase.
- **`memory-recall`** — MEANINGFUL, and already named in that same Step 4. It surfaced
  `TOOL-aPromptedMandate-5`, the spec that designed the prompt path, and the review note recording
  that leg check 18 orders the first `--preflight` against the first `/session-kickoff` across the
  template — a constraint this build's own edit had to respect.
- **`gotchas --for-paths`** — MEANINGFUL, and already named there. Returned six classes over
  `SKILL.template.md` and the kickoff engine, `two-answers-to-one-question` among them, which then
  decided the shape of the fix.
- **`lexicon`** — NOT meaningful at orientation, refused with a measurement. `--suggest` needs an
  identifier nobody has written yet; `--brief` needs an armed language, and `.lexicon.conf` declares
  `md::dark` and `sh::dark`, so every file in scope returns `COVERAGE: dark`. Wiring it into
  orientation would install a probe that cannot move.

So three of the four are reachable but LATE — the engine that runs them is invoked at step 6, after
step 3 has written and step 4 has pushed the roster. That timing, not an absence, is what this build
fixes, and the fourth is recorded as a loss rather than built.
