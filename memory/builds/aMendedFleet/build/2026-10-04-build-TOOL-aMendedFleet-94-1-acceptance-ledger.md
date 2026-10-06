# TOOL-aMendedFleet-94 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-94

**Evidences:** TOOL-aMendedFleet-94
- AC1 — `git ls-files --` — `sed -n 1,8p` over the rule printed the frontmatter with the four globs, and each glob's listing piped to `head -1` printed a tracked path; the staged spelling `tool/**` printed nothing
- AC2 — `git show` — the base section body cut between `## What ships here` and `## Layout` diffed empty against the rule body between its H1 and the first moved bullet; the grep for the two bullets printed 0 over the wrapper and 2 over the rule; a scratch copy of the rule with two words rewritten made the diff exit 1
- AC3 — `bash tools/check-template-size.sh AGENTS.md` — after the bump it exited 0 with no WARN at 54231 bytes against 56632 at base, a shrink of 2401 against a floor of 2261 (moved 2661 less 400); the high-water row prints 54231; the wrapper section measures 303 bytes, heading and the next heading included
- AC4 — `path_glob_match` — a headless `claude -p --settings` run from this tree, CLI 2.1.178, reading `tools/lib/resolve-python.sh` logged one record with that load reason naming `.claude/rules/product.md`; with the key staged as `path` the same run logged the file only under `session_start`, unscoped, and no such record
