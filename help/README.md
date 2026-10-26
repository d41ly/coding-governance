# Help

One task-oriented page per user-facing feature: what it is, how to use it, a short example.

- [Role agents and `/build`](roles.md) — how a task reaches a role agent, and how to adjust a role.
- [Profiling the gate legs](measure-legs.md) — run every leg clean and see what each one costs.
- [The policy file](policy.md) — where a repository's policy lives, how to set a key, how to read one with `policy.py get`, and how it is checked.
- [The agent limit](agent-limit.md) — how many agents run at once, how to raise or lower it, what `policy.py settings --write` renders, and what the agent-cap hook refuses.
- [Upgrade steps and retired kits](upgrade-steps.md) — what an `[[upgrade]]` step and a `[[retired]]` kit are, what `update` does with a kit that has a successor, and where `.agent-cap.conf`'s value now lives.
- [The size caps](size-caps.md) — one switch, `budgets.enforce`, over every size cap a gate enforces; the pins that keep a cap refusing; which caps sit outside the switch; and where each cap's value is declared.
