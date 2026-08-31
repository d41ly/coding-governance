# Acceptance ledger — TOOL-aGatheredDeclaration-2

**Serves:** journal TOOL-aGatheredDeclaration-2

One line per criterion in that spec's §6, answered by what was observed rather than by what was
intended. Criteria whose arms are not yet written say so; a ledger that reads green on an unwritten
arm is the shape this repo names `fixture-passes-by-finding-nothing`.

## The verification method, because it is unusual and worth stating once

Two of the strongest answers below come from **extracting the loader program out of `run-gates.sh`
and running it directly** against both real manifests, rather than from running the bar. That is not
a shortcut around the bar — the bar is owed and is queued — it is a sharper instrument for this
particular question: it compares the WIRE, field by field, over all 86 legs at once, where a bar run
would compare only the legs a guard happens to select and would report a verdict rather than a
tuple. The one thing it cannot see is whether the dispatcher below the loader behaves, which is what
the canary and the bar are for.

The extraction is a regex over the script's own source for the `legs=$("$PYBIN" -c '…'` block, so it
runs the shipped bytes and not a copy.

## The criteria

| AC | Status | What was observed |
|---|---|---|
| AC1 — TOML reports the same leg count and manifest order | **MET** | 86 rows from each manifest, in the same order, from the extracted loader. Zero field mismatches outside `subject`. |
| AC2 — TOML absent, legacy pair read, one deprecation line | **PARTIAL** | The branch is written and the message names both files and the reason. Not yet asserted by an arm in `run-gates.test.sh`. |
| AC3 — no `tomllib`, named refusal, legacy pair, no exit 2 | **PARTIAL** | The probe and the message are written and name the interpreter and its version. Not yet driven against a stub interpreter. RED-first not yet observed. |
| AC4 — a leg with no guard round-trips field-by-field | **MET** | 38 of 86 legs carry no effective guard (36 omit the key, 2 declare an empty list) and every one of them matches field-for-field across the two loaders. The RS/US separator survives the empty field, which is what a tab would have collapsed. |
| AC5 — the held SET from TOML equals the JSON union's set | **MET** | 46 in both, compared as SETS from the emitted wire rather than as a key. |
| AC6 — the dispatch loop holds exactly the declared set | **MET, on a fixture** | Three-leg fixture pair: under JSON `beta` (`chunk = selftests`, `subject = repo`) is HELD; under TOML the same leg with `opt_in = false` RUNS. `gamma` (`opt_in = true`) is held in both. That is the declaration becoming authoritative, observed rather than argued. |
| AC7 — `[bar]` booleans marshal to `0`/`1` | **NOT MET** | `[bar]` is parsed and INERT in this unit. The marshalling lands with the guards that read it, in units 4 and 5. |
| AC8 — `cwd` resolution and escape refusal | **NOT MET** | `cwd` is accepted by the schema validator and not yet consumed by the dispatcher. |
| AC9 — unknown key / undeclared lane refuse with exit 2 | **MET, unarmed** | Both refusals are written and name the leg and the offending key or lane. RED-first not yet observed and no arm asserts them. |
| AC10 / AC10b — the pre-push predicate pair | **NOT MET** | Unit 2 S8's predicate-6 pathspec edit is not in this commit. |
| AC11 — `GATE_OPTIN` and `GATE_SELFTESTS` write the same byte | **PARTIAL** | Both spellings feed one resolution at the dispatcher and one at the run-record `selftests` key. No arm asserts the pair yet. |
| AC12 — the pinned-knob arm grades the TOML profiles | **NOT MET** | `gate-profiles.txt` is still present and still the file that arm reads. It moves with unit 6's deletion. |
| AC13 — the bar is GREEN on this tree with the leg count unchanged | **PENDING** | The shipped canary is running. The full bar is owed at the push boundary. |
| AC14 — `turnstile_ttl` takes effect | **NOT MET** | Unit 5. |
| AC15 — no `[[profile]]` row refuses; a partial `[bar]` does not | **MET, unarmed** | The refusal is written; a `[bar]` may be absent entirely and every key in it is defaulted, which is what AC11 of unit 4 needs. |
| AC16 — the comments survived the migration | **NOT MET** | The generator carries each `gate-profiles.txt` comment block above the row it argues for, but no arm compares the two files. This is the criterion that expires: unit 6 deletes the source. |
| AC17 — `short_circuit` validated and defaulted | **PARTIAL** | Validated as a boolean by the schema check; the default is `false` in the shipped declaration. Nothing reads it until unit 8. |
| AC18 — `GATE_OPTIN` and govkit's policy regex | **NOT MET** | Unit 6 owns `govkit.py`. |
| AC19 — the resolved manifest path is exported, suites consume it | **NOT MET** | Unit 2 S13, not built. |
| AC20 — a ceiling over `default_ceiling` carries a comment | **MET by construction** | The generator emits one above every such leg. No arm parses for it yet. |

## Honest summary

Six criteria MET, three MET-but-unarmed, four PARTIAL, one PENDING, seven NOT MET. **The unit is not
closed.** What landed is the declaration, the dual-format loader, the interpreter floor and the
resolved hold field — the load-bearing half. What is missing is mostly ARMS: refusals that are
written and work but have no test asserting them, which is the difference between a mechanism and a
gated mechanism and is exactly what the charter means by a gate whose failing case has never been
observed.

The seven NOT MET rows are not gaps in this unit's implementation; each names the sibling unit that
owns it. AC7, AC8, AC10, AC12, AC14, AC18 and AC19 were written into unit 2's §6 during the audit
folds because that is where the mechanism is DECLARED, and their consumers live elsewhere. Whether
that split was right is a question for the closing review; what matters here is that no row above
claims a green it does not have.
