# TOOL-dQuietDisk-1 leg-tail 36 — loop factories fixtures failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** loop factories fixtures
- **Hash:** daebb55cc426e218ce3c973e84c4ff6bbcfbcf3e
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg loop factories fixtures | exit 1
factories: selftest · PASS check-commands · exit 0 · factories: check-commands · green · 1 row(s) over 30 descriptor(s)
factories: selftest · PASS command-new · exit 0 · factories: fixture · command-new · factory exit 0 · gate green
factories: selftest · PASS command-hand · exit 1 · factories: gate · factories: refused · tools/loop/kit.toml command.loop.hand: its run 'no-such-file.py' names no file git holds under tools/loop
factories: selftest · PASS policy-key-new · exit 0 · factories: fixture · policy-key-new · factory exit 0 · gate green
factories: selftest · PASS policy-key-hand · exit 1 · factories: gate ·   fixture.hand: lacks the required field `owner`
factories: selftest · PASS hook-new · exit 0 · factories: fixture · hook-new · nothing staged · gate green
factories: selftest · PASS hook-hand · exit 1 · factories: gate · hook-dest: FAIL tools/hooks/fixture-hand.fragment.json declares hook_path '{kit}/hooks/fixture-hand.js' -> 'tools/hooks/fixture-hand.js', which NO kit.toml rule ships.
factories: selftest · PASS role-new · exit 0 · factories: fixture · role-new · factory exit 0 · gate green
factories: selftest · PASS role-hand · exit 1 · factories: gate · roles: tools/roles/agents/gov-hand.agent.md: R2 — front-matter key 'writes' is missing
factories: selftest · FAIL workflow-new · exit 1, owed 0 and a line 'factories: fixture · workflow-new' naming 'gate green': Data/Local/Temp/gate-work.U2uJ4tRR/tmp/pol-hlsp8or4/memory/builds/dWellOiledMachine/README.md
    factories: gate · loop: refused · the list row DOD_CORE parked-decisions-surfaced names the build dShippedRelease, which has no C:/Users/d41ly/AppData/Local/Temp/gate-work.U2uJ4tRR/tmp/pol-hlsp8or4/memory/builds/dShippedRelease/README.md
factories: fixture · workflow-new · FAIL · the factory exited 1

factories: selftest · PASS workflow-hand · exit 1 · factories: gate · roles: tools/roles/workflows.toml: R8 — entry 11 (handoff-hand) lists 'gov-nobody', which names no role file
factories: selftest · PASS factory-restores · exit 1 · factories: fixture · factory-restores · factory exit 1 · porcelain clean
factories: selftest · PASS factory-restores-create · exit 1 · factories: fixture · factory-restores-create · factory exit 1 · no created file on disk · porcelain clean
factories: selftest · PASS scenario-new · exit 0 · factories: fixture · scenario-new · factory exit 0 · gate green
factories: selftest · PASS scenario-hand · exit 1 · factories: gate · loop: refused · scenario.hand · entry step.nowhere is no gov step
factories: selftest · PASS factory-interrupt · exit 0 · factories: fixture · factory-interrupt · held paths at prior bytes · porcelain clean · leftover named
factories: selftest · FAIL · 16 case(s) · 1 failed: workflow-new
```
