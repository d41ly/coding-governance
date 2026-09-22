**Serves:** journal TOOL-dScriptedRepeat-1

# dScriptedRepeat — what the grounding found

Moved out of `memory/builds/dScriptedRepeat/README.md` on 2026-08-24 to keep that index under its
byte cap. Verbatim; nothing was rewritten. It is the read-once history of the grounding pass, which
is exactly the shape that belongs in a record rather than in the file a session opens first.

**The mode mechanism already exists and is gated.** `TOOL-aPromptedMandate-1` put an
`authorized-by:` key in the build README's front matter, read at the pinned BASE, recorded as `mode:`
in Run facts, over a CLOSED set the driver refuses to default outside of. `TOOL-aPromptedMandate-4`
then made directives SCOPE-TAGGED — `<handle>:<section>[:<scope>]`, absent field meaning `all` — with
`researched:M12:prompt` and `solution-tested:M12:prompt` as the first two scoped members, and a
driver refusal when a waiver names a handle out of scope. Playbook mode is a third member of that
closed set plus its own scoped directives. No authorization primitive is invented.

**What is portable, and what is not.** Portable: the mode declaration and its closed-set refusal, the
scoped-directive layer, `PHASES_CORE` as the phase vocabulary, the `--park` register and its
`parked-decisions-surfaced` DoD item, the run-state generated/authored split, and M12's
research→test→choose loop, which is exactly what "no playbook exists yet, do research" describes. Not
portable: the DoD item `build-complete`, which reads the units table and therefore counts units, not
pieces.

**The reference playbooks are two different shapes and both are evidence.** `PLAYBOOK.md` is a step
checklist where every step carries `GATE <leg>` or `CHECK <why>`, with its own I21 invariant redding a
step that is untagged or names no runnable leg. `HYBRID-PLAYBOOK.md` is a recipe: an exact parameter
table, a prompt scaffold with named slots, hard rules each traced to an owner correction, an
accepted-instance library, a "what was ruled out — don't re-try" section, and a dated bake-off marked
don't-redo. The GATE/CHECK tagging is the same discipline this repo already states as a rule (a gate's
own header names what it does not check; a skip must announce itself), which is why it is the
template's spine rather than an import. Every count over either file is DERIVED by the research
records under `build/`, never restated here — the first draft of this paragraph carried three and one
of them was already wrong.
