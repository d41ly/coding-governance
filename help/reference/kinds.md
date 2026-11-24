<!-- gov:rendered from tools/playbook/references.toml doc.reference.kinds; edit the registry, not this page -->
<!-- unit: unit.kinds-register -->
# Kinds

## `kind.tool-kit`
<!-- usage: kind:kind.tool-kit 4915fc1b -->
A deployable kit: a directory under the tool root with a kit.toml descriptor and its own adopter.

```text
a directory <prefix>/<kit>/ holding kit.toml, its adopter and its engine, with an [[entry]] row in the govkit registry
```

## `kind.command`
<!-- usage: kind:kind.command ce0a41ad -->
A command a kit declares: a [[command]] row of its kit descriptor, its verb and the file it runs.

```text
python <prefix>/playbook/core.py new command <verb> --kit <id> --run <path>
```

## `kind.instruction-unit`
<!-- usage: kind:kind.instruction-unit 28cb9d27 -->
One instruction unit: a [[unit]] row of a kit's instructions.toml, rendered by its level, scope and trigger.

```text
python <prefix>/playbook/core.py new instruction-unit <name> [factory flags]
```

## `kind.policy-key`
<!-- usage: kind:kind.policy-key 282e334d -->
A policy key: a [[key]] row of the policy catalogue, read through policy.py get.

```text
python <prefix>/playbook/core.py new policy-key <name> --allowed <toml> --default <toml> --summary <text> --usage <text> --owner <build>
```

## `kind.preset`
<!-- usage: kind:kind.preset 3bfd7fac -->
A named preset of policy values an adopter selects at once: one table of the policy kit's preset store assigning every presettable key, complete, inside each key's schema and inside the pair rules.

```text
python <prefix>/playbook/core.py new preset <name> --from <preset>
```

## `kind.gate-leg`
<!-- usage: kind:kind.gate-leg a899edef -->
A gate leg: a row of the leg manifest the merge bar runs.

```text
python <prefix>/playbook/core.py new gate-leg <name> --kit <id> --argv <json> --subject <kit|repo> --purpose <text> --enforces <tag>
```

## `kind.role`
<!-- usage: kind:kind.role 626337da -->
A role an agent takes in the loop: a role file of the roles kit, listed by its workflow and priced by its body ceiling.

```text
python <prefix>/playbook/core.py new role <slot> --workflow <name> --writes <class> --description <text> --reads <keys> --returns <text> --output <text> --ceiling <bytes>
```

## `kind.workflow`
<!-- usage: kind:kind.workflow d22b7cd9 -->
A workflow the loop runs: a [[workflow]] row of the roles kit's table, placed by its row of the loop definition.

```text
python <prefix>/playbook/core.py new workflow <name> --driver <driver> --harness <path|none> --roles <slots> --enforced-by <text> --trigger <text> --order <n> --step <step tag|none>
```

## `kind.hook`
<!-- usage: kind:kind.hook 821942a3 -->
A harness hook script and the fragment that wires it, shipped by its kit's descriptor.

```text
python <prefix>/playbook/core.py new hook <name> --kit <id> --event <event> [--matcher <m>]
```

## `kind.skill`
<!-- usage: kind:kind.skill 820c4989 -->
A Skill under skills/&lt;name&gt;/, made by the core's factory.

```text
python <prefix>/playbook/core.py new skill <name> --description <text>
```

## `kind.charter-practice`
<!-- usage: kind:kind.charter-practice 694994c6 -->
A charter practice: a [[practice]] row of practices.toml, one rule line of the charter.

```text
python <prefix>/playbook/core.py new charter-practice <name> --line <text>
```

## `kind.record-kind`
<!-- usage: kind:kind.record-kind f55fbc8e -->
A kind of record the memory tree holds.

```text
no factory has landed; dConvergedCharter lands it, and until then the kind has no member
```

## `kind.stage`
<!-- usage: kind:kind.stage 7fdd6f5a -->
A stage of the loop: one of gov's steps, or a repository's own spliced between two adjacent ones from its overlay.

```text
python <prefix>/playbook/core.py new stage <name> --after <step> --before <step> --actor <kind:name> --witness-by <text> --owner <build> [--input <layer:what> --allowance <text> --returns <record>]
```

## `kind.product-layer`
<!-- usage: kind:kind.product-layer 42f61144 -->
A product layer: a row of layers.toml the layer check grades, the core never depending on an expansion.

```text
python <prefix>/playbook/check_layers.py --new <tag> --kind <kind> [--of <tag>] --definition <text>
```

## `kind.item`
<!-- usage: kind:kind.item af468ce7 -->
A work item of a gov step's program: an [[item]] row of the loop definition, or a repository's own in its overlay.

```text
python <prefix>/playbook/core.py new item <name> --step <step> --actor <kind:name> --witness-by <text> --owner <build> [--input <layer:what> --allowance <text> --returns <record>]
```

## `kind.lens`
<!-- usage: kind:kind.lens eb6fe2f2 -->
A review lens a Tier-2 review primes.

```text
no factory has landed; dCalibratedLens lands it, and until then the kind has no member
```

## `kind.scenario`
<!-- usage: kind:kind.scenario f87dc072 -->
A scenario a build runs under: what kind of work it is, the request facts that admit it, its entry step and the rows of other kinds it activates.

```text
python <prefix>/playbook/core.py new scenario <name> --extends <tag|none> --admit <fact>=<value> --entry <step tag>
```
