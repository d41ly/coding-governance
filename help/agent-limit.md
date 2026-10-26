# The agent limit, `runtime.agents-in-flight`

**What it is.** How many agents one session may have running at once, its direct `Agent` spawns and
the agents of a `Workflow` run. It is one key in the policy file, `.governance/policy.toml`, with a
default in the policy kit's catalogue. The harness enforces it, through two of its own settings the
policy kit writes into `.claude/settings.json`: `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` refuses a direct
spawn over the limit, and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` queues a Workflow agent over
it. The harness counts agents in flight and knows when each one ends, which a hook cannot.

This is not the verify-stage total. How many agents a review's verify stage may spawn at all is the
agent-cap hook's `MAX_VERIFIERS`, unchanged by this key: see the review protocol.

## How to use it

- **Read it:** `python tools/policy/policy.py get runtime.agents-in-flight --explain` prints the
  limit at the landed revision and names where it came from, a `.agent-cap.conf` lowering included.
- **Raise or lower it:** write the key in `.governance/policy.toml` and commit it.

  ```toml
  [runtime]
  agents-in-flight = 4
  ```

  Then render the harness's settings from it and commit them with the policy write:

  ```sh
  python tools/policy/policy.py settings --write   # both variables at the limit HEAD resolves
  python tools/policy/policy.py settings --check   # exit 1 naming each variable that differs
  ```

  `--write` keeps every other key of the file and its order, adds `env` when it is absent, writes
  only when a value differs, and replaces the file whole through a temporary file beside it, so the
  harness never reads half a file. It writes the settings file in force: the file you name, else the
  one `GOV_SETTINGS_JSON` names, else `.claude/settings.json`, the order `check-wiring.sh` reads them
  in. Every landing re-runs `--write`, so the landed settings always carry the landed limit, and the
  policy kit's adopter, `adopt-policy.sh --scaffold`, runs it too wherever the repository has a commit.
  UNVERIFIED: that a session keeps the settings it started with until it restarts. Hook settings are
  live on the next tool call (memory/gotchas/settings-edit-takes-effect-mid-session.md), and whether
  the two concurrency variables are too is undecided until the two-halves probe that record names is
  run against them: raise a variable mid-session and observe the next spawn obey it, then lower it and
  observe the same probe refuse, so a session that never re-read the file cannot pass as one that did.
  The file `--write` writes is one layer, not all rule 7 reads: rule 7 reads `.claude/settings.local.json`,
  `.claude/settings.json` and the file `GOV_SETTINGS_JSON` names, and never the `--settings` flag
  layer, the managed-policy layer or an exported variable (see below).
- **What `.agent-cap.conf` does:** a `FANOUT_CAP=<n>` line in it, at the repository root, LOWERS the
  limit and never raises it; `--explain` says which. A value that is not a whole number of at least 1
  makes the reader refuse, naming the line. The agent-cap hook no longer reads the file.

## What the agent-cap hook refuses

Its rule 7 checks, on every `Agent` and `Workflow` call, that the settings this checkout's harness
starts from hold the limit landed on the default branch. It reads three settings layers at the
checkout root: `.claude/settings.local.json`, `.claude/settings.json`, and the file `GOV_SETTINGS_JSON`
names when that variable is set, a relative path read against the root. Each variable must be set in
at least one of them, and every layer that sets it must hold a whole number no higher than the limit,
so a declared file never hides a project value above it, nor the project file a declared one. Otherwise
it refuses the call, naming the first such layer, the variable and both numbers; a lower layer the
harness never applies is refused too. A `GOV_SETTINGS_JSON` that names no file is refused, naming the
path and `not a file`. A call whose working directory lies in no git checkout is refused too, and so is a settings file that does not parse, or any step of the rule that
fails, naming the step: a rule that cannot finish does not admit. A refusal over the limit reads:

```
BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this Workflow call — the settings this checkout's harness starts from do not hold the landed agent limit.
  .claude/settings.json: env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS is 8, above runtime.agents-in-flight 6.
```

To clear it, run `python tools/policy/policy.py settings --write` in that checkout; it writes one
file, so a refusal naming another layer is cleared by naming that file after `--write`, or by
removing the value from it. A branch that
raises the key renders the raise into its own settings, and rule 7 refuses them until the raise lands,
because it reads the landed limit, never the branch's. Remove a hand-set value from
`.claude/settings.local.json` the same way. Three layers the harness applies are layers rule 7 does
not read, so a value there runs past the limit unrefused: a file passed with the `--settings` flag,
the managed-policy layer an administrator installs, and an exported environment variable that sets
either harness variable. A set `AGENT_CAP` changes nothing.

A refused policy read is not a settings refusal. When the policy reader cannot read the landed limit,
rule 7 prints the reader's refusal under its own header, and `policy.py settings --write` does not
clear it. In a repository whose default branch is not `main` and that names it nowhere, it reads:

```
BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this Agent call — the landed agent limit cannot be read, so the settings in force were not compared, and a rule that cannot read does not admit. Clear the policy reader's refusal, which names its cause:
  policy: refused · .governance/policy.toml:0 · refs/remotes/origin/main names no commit in this repository, and main is only the fallback: refs/remotes/origin/HEAD names no branch and GOV_DEFAULT_BRANCH is unset. Name the default branch: git remote set-head origin -a, or export GOV_DEFAULT_BRANCH=<branch>.
```

To clear it, run `git remote set-head <remote> -a` so the remote's HEAD names its default branch, or
`export GOV_DEFAULT_BRANCH=<branch>`; with no remote, the export alone names the local default branch.
