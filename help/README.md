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
