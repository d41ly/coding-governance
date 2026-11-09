# Help

One task-oriented page per user-facing feature: what it is, how to use it, a short example.

- [Role agents and `/build`](roles.md) — how a task reaches a role agent, and how to adjust a role.
- [Profiling the gate legs](measure-legs.md) — run every leg clean and see what each one costs.
- [The policy file](policy.md) — where a repository's policy lives, how to set a key, how to read one with `policy.py get`, and how it is checked.
- [The agent limit](agent-limit.md) — how many agents run at once, how to raise or lower it, what `policy.py settings --write` renders, and what the agent-cap hook refuses.
- [Upgrade steps and retired kits](upgrade-steps.md) — what an `[[upgrade]]` step and a `[[retired]]` kit are, what `update` does with a kit that has a successor, and where `.agent-cap.conf`'s value now lives.
- [The step gate](step-gate.md) — the `step-gate` leg: what it reds when a landing makes an adopter-visible member vanish, how a landing answers it with an `[[upgrade]]` or `[[retired]]` row, and how a later class joins.
- [The size caps](size-caps.md) — one switch, `budgets.enforce`, over every size cap a gate enforces; the pins that keep a cap refusing; which caps sit outside the switch; and where each cap's value is declared.
- [Forwarders for a moved path](shims.md) — what a call to a moved command, hook or module path does, the two `install.on-shim-call` modes, where the journal is, and how long `install.deprecation-window` holds a forwarder.
- [The Python floor](python-floor.md) — the interpreter floor every gate and hook runs at, what the resolver's refusal says, how to install the floor, and what `platforms.provision`'s three values do.
- [What `update` does with your edits](update-edits.md) — an edited file gov stopped shipping (`retired-edited`, ordered or kept as `install.retired-edits` says), an edited render (`render-edited`, its kit held back), and a withdrawn hook fragment unwired from your settings.
- [The docs leg](docs-leg.md) — the `docs` leg: how a page under `help/` is kept current with the usage it documents, what `docs_leg.py` reds, how to answer a stale page, what `help.enforce` does, and how a later class joins.
- [Spec-audit chains](spec-audit.md) — how a spec audit's round disposes its findings, how `--record-round` and `--chain-verdict` record a round and answer CONTINUE, STOP or HOLD, and what `review.spec-audit.disposal`, `.chain-stop` and `.chain-ceiling` do.
- [The charter's practices](charter.md) — what the practice catalogue is, how to read the active set, how `charter.practices` chooses it, and what stops a render.
- [The instruction overlay](overlay.md) — how a repository adds, amends, replaces and excludes an instruction unit in `.governance/instructions.toml`, which units are fixed, and how it declares a policy key of its own under `adopter.`.
- [Composition](composition.md) — where a repository's units render in the charter and the marked parts, how `budgets.enforce` and a harness's own limit act at render, how to read the delta report, and what the practice census moved.
- [Overlay rows](overlay-rows.md) — how a repository adds, amends, replaces and excludes one of gov's structured rows, what a pin is, and what each `instructions.stale` value does to a row at update.
- [Tags and the resolver](tags.md) — what a tag and a citation are, how to find, read and cite one with `gov_tag.py`, what `check` reds, and what `tags.slice`, `tags.retired-cites` and `tags.bare-refs` do.
- [The instruction layer](concepts/instruction-layer.md) — the ladder, units, the overlay and composition, and the reference pages rendered from each registry's rows.
- [Change one of gov's rules](tasks/change-a-gov-rule.md) — amend, replace, exclude and re-pin one of gov's instruction units from your overlay, with the commands.
- [Adopt gov in an empty repository](tutorial/adopt-gov.md) — install the charter kits, add a rule of your own, render the charter and read the delta report.

Reference pages, rendered from their registries by `python tools/playbook/render_playbook.py --reference`:

- [Policy keys](reference/policy.md) — each policy key's summary and usage, and the keys not yet summarised.
- [Drive](reference/drive.md) — each stage and role of the loop, when it runs and the command that starts it.
- [Kinds](reference/kinds.md) — each kind of extension and how a member of it is made.
