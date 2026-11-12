<!-- gov:rendered from tools/playbook/references.toml doc.reference.units; edit the registry, not this page -->
<!-- unit: unit.unit-registry -->
# Units

## `unit.policy-schema`
<!-- usage: unit-usage:unit.policy-schema 76ca1499 -->
MUST declare a policy key as a [[key]] row of &lt;prefix&gt;/policy/catalogue.toml, with its summary and usage, before any policy file sets it.

```text
python <prefix>/policy/policy.py get <key> --explain
```

## `unit.drive-table`
<!-- usage: unit-usage:unit.drive-table e8066771 -->
MUST declare a drive row as a [[drive]] row of its kit's descriptor, never in the charter's drive section by hand.

```text
python <prefix>/playbook/instruction_units.py drive --check
```

## `unit.kinds-register`
<!-- usage: unit-usage:unit.kinds-register f439a032 -->
MUST make a member of a registered kind through the factory its row in &lt;prefix&gt;/playbook/kinds.toml names, never by hand.

```text
python <prefix>/playbook/core.py new <kind> <name>
```

## `unit.unit-registry`
<!-- usage: unit-usage:unit.unit-registry 9c811f32 -->
MUST write an instruction unit as a [[unit]] row of its kit's instructions.toml, in the grammar the schema leg reads, never as prose in a guide.

```text
python <prefix>/playbook/instructions_edit.py propose add --manifest <kit> --tag <tag>
```
