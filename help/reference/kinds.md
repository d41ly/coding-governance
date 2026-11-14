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
<!-- usage: kind:kind.command a64a6cbe -->
A slash command an adopter's harness runs.

```text
no factory has landed; dDeclaredLoop lands it, and until then the kind has no member
```

## `kind.instruction-unit`
<!-- usage: kind:kind.instruction-unit 28cb9d27 -->
One instruction unit: a [[unit]] row of a kit's instructions.toml, rendered by its level, scope and trigger.

```text
python <prefix>/playbook/core.py new instruction-unit <name> [factory flags]
```

## `kind.policy-key`
<!-- usage: kind:kind.policy-key 37cbbdaf -->
A policy key: a [[key]] row of the policy catalogue, read through policy.py get.

```text
a [[key]] row in <prefix>/policy/catalogue.toml, its name, allowed values, default, summary and usage
```

## `kind.preset`
<!-- usage: kind:kind.preset 8b503872 -->
A named preset of policy values an adopter selects at once.

```text
no factory has landed; dDeclaredLoop lands it, and until then the kind has no member
```

## `kind.gate-leg`
<!-- usage: kind:kind.gate-leg 1bc90e49 -->
A gate leg: a row of the leg manifest the merge bar runs.

```text
a row in <prefix>/gate-legs.json, its name, argv, chunk, subject and ceiling
```

## `kind.role`
<!-- usage: kind:kind.role e259cccd -->
A role an agent takes in the loop, rendered into its agent file.

```text
no factory has landed; dDeclaredLoop lands it, and until then the kind has no member
```

## `kind.workflow`
<!-- usage: kind:kind.workflow 519594eb -->
A Workflow script the harness runs as one program.

```text
a script <prefix>/workflows/<name>.js
```

## `kind.hook`
<!-- usage: kind:kind.hook eca119d0 -->
A harness hook script and the fragment that wires it.

```text
a script <prefix>/hooks/<name>.js with its fragment
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
<!-- usage: kind:kind.stage 405f4568 -->
A stage of the loop a drive row names.

```text
no factory has landed; dDeclaredLoop lands it, and until then the kind has no member
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
<!-- usage: kind:kind.scenario 7e1f2422 -->
A scenario the loop is exercised against.

```text
no factory has landed; dDeclaredLoop lands it, and until then the kind has no member
```
