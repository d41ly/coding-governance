# The owner's prompt — verbatim

**Serves:** research TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11

The run was started with `/unattended --prompt <value>`, where the value carried whitespace and named
no readable file, so it is the prompt itself and is taken verbatim. The bytes travel here rather than
a reference, because the build folder IS the authorization and may not point at a file that can be
edited after the run starts.

## Verbatim

> Run an adversarial review on the unattended kit with the purpose of improving the quality of
> unattended sessions and the code they write, then build the findings per the protocol. Any
> recommendations are accepted, changes to any layer of the kit.

## How it was read

- **The subject** is the unattended-run kit, every layer: driver, gate leg, playbook gate, adopter,
  Skill template, protocol template, kit descriptor, self-tests, and this project's
  `.unattended.conf`. "Any layer" is explicit.
- **The lens is narrow and is not "is this kit correct".** It is: what lets an unattended run produce
  worse work than an attended one would, and land it green. That question has not been asked of this
  kit before — prior rounds asked about authorization integrity and refusal correctness.
- **"Any recommendations are accepted"** is a blanket scope grant, so no owner turn was spent on
  scope. The build's roster is therefore the review's own CONFIRMED set, bounded by the build
  method's M3 vetoes: a finding whose fix needs a new external dependency, a new install location, a
  new public surface, or a change to a governance carrier is an owner turn and is PARKED rather than
  built.
- **"per the protocol"** routes the build through `memory/guides/UNATTENDED-PROTOCOL.md` and the
  build method, which is what this run did.

## The one assumption this run made without asking

The owner's single turn was not spent. Every field the kickoff task skeleton asks for derived from the
prose, the tree and the records — acceptance and gates included, which are the two that would have
been disqualifying. Asking anyway would have cost the turn the owner was walking away from.
