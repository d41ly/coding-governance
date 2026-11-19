**Serves:** journal TOOL-dWitnessedBar-16

# Build brief — TOOL-dWitnessedBar-16, pass 2

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 10.
- THIS IS PASS 2 of the two-pass unit. Pass 1 landed as `87bc9f615` and `6c989def1`, and the main loop committed the
  converted `memory/project/readme-contract.txt` in `1f4ce2c30`. Build S12: delete the transitional old-grammar read
  F15 names, observe AC14, and move the spec's status to `CLOSED` in this pass's commit.
- Pass 1's pass legs ran red, and their full output is the untracked log
  `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/unit16-pass1-pass-legs.log`.
  Fix every red there that pass 1 caused, in this pass, each the way its leg's own message directs:
  - install-prefix: the kit-path spellings in `tools/memory-tree/convert_registry.py`, the `[[ledger]]` and
    `[[upgrade]]` rows in `tools/memory-tree/kit.toml`, `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`
    and `tools/govkit/registry.toml`, `tools/drift-audit/selftest.py`, and `tools/check-dead-paths.sh`. Spell each
    through a token the reader resolves or route it through `resolve_kit_dir`; the leg takes no waiver. If a seed argv
    or a home cannot be spelled so the landed factory still runs it, say so in your return rather than route around
    the gate. The one carried red, the `conf-scalar-pins` seed argv at its unit 14 spelling, stays until unit 51.
  - dead-path carriers: the old names `memory/map/baseline.toml` and `memory/map/affordance-exempt.toml` still
    spelled in `.gitattributes`, `.governance/instructions.toml`, `AGENTS.md`, `WIRE-INTO-PROJECT.md`, a gotcha
    record and the codebase-map dossier. Repoint each where this unit owns the text; where unit 51 S5 owns the
    respelling, add a waiver row naming that unit.
  - shell hygiene: two new substitution-fed loops and two registry counts that fell; feed the loops from a scratch
    file and lower the counts in `memory/project/substitution-fed-loops.txt`.
  - verdict epoch: add `convert_registry.py` to the `DELEGATES` list `tools/memory-tree/check-verdict-epoch.sh` reads.
  - lexicon: verb offenders rose by eight; rename the new definitions to declared verbs (`lexicon.py --suggest`),
    and re-measure `.lexicon.conf`'s pin only for parity copies that cannot be renamed.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and `python tools/playbook/positional.py` over
  your own records before committing; they read only tracked files.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-16`, its trailer block carrying `Pass: TOOL-dWitnessedBar-16`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-16-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
