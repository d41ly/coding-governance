# Revision — dTrackedAtlas: specs 3 and 4 name every new function with a declared verb

**Serves:** research TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4

## The prompt

> Unit 3's builder returned `diverged: true` before writing code: three function names its spec fixes would raise the lexicon's verb-offender count past its pin. Rename them, and unit 4's two of the same kind, in the specs.

## The brief

### Goal
Specs 3 and 4 name new functions whose leading token `.lexicon.conf` does not declare as a verb, and the `lexicon wiring` leg reds any new offender over its pin, as it did for unit 1 (`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-red-fix-3.md`). Rename each in its spec, so both units build without moving the pin.

### Items
1. In `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-3.md`, rename `git`, `input_digest` and `stamp_page` everywhere the spec names them (section 3, the section 4 inventory, prose and acceptance), each to a name whose leading token is a declared verb; candidates the builder offered are `read_git`, `derive_input_digest` and `build_stamp`. `read_stamp` and `check_page` already pass and stay.
2. In `…-TOOL-dTrackedAtlas-4.md`, rename `regenerate` and `sidecars` the same way, in camel case for the `js.function` cell; `readConf`, `runHook` and `runRunner` already pass and stay.
3. Grade every name you choose, and every other new function or method name either spec declares, with `python tools/lexicon/lexicon.py --suggest <name> --as py.function` or `--as js.function`, and keep only names it answers OK for.
4. In spec 3, say plainly in section 4 that the git helper may read unit 1's `GIT_TIMEOUT` from the module at `STATE_PATH`, as it does today; that is a use of unit 1's interface, not a second derivation.
5. Bump both specs' rev and add one revision-log line each naming this record and the renames; no other design change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades units 3 and 4 READY; `--check-specs dTrackedAtlas TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean for both; every function name the two specs declare gets an OK line from the lexicon's `--suggest`.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
No design change beyond the renames and item 4's sentence; no product code; no commit and no index render, which the main loop does.
