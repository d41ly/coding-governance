# The policy file, `.governance/policy.toml`

**What it is.** One file holds a repository's policy: one value per key, such as whether a size
cap's breach warns or refuses. The policy kit's catalogue, `tools/policy/catalogue.toml` in this
repository, is the file's schema. It has one row per key, giving the values the key admits, its
default, and the build that owns it. A key the file does not set takes its default.

One reader reads the file: `python tools/policy/policy.py get <key>`, below. These keys have <!-- usage: script:tools/policy/policy.py#get af650e87 -->
consumers today, each family documented on its own page:

- `runtime.agents-in-flight`, which `policy.py settings --write` renders into the harness's
  settings and the agent-cap hook holds them to ([the agent limit](agent-limit.md));
- `budgets.enforce`, `budgets.pinned` and `budgets.<cap>`, which every gate that enforces a size
  cap reads ([the size caps](size-caps.md));
- `help.enforce`, which the docs leg reads ([the docs leg](docs-leg.md));
- `review.spec-audit.disposal`, `review.spec-audit.chain-stop` and
  `review.spec-audit.chain-ceiling`, which the unattended driver reads
  ([spec-audit chains](spec-audit.md));
- `install.on-shim-call` and `install.deprecation-window`, which a forwarder and gov's forwarder
  hold read ([forwarders for a moved path](shims.md));
- `install.retired-edits`, which `update` reads
  ([what update does with your edits](update-edits.md));
- `platforms.provision`, which the Python resolver reads ([the Python floor](python-floor.md));
- `pass.fast-legs`, which the pass-leg runner reads ([the pass legs](pass-legs.md));
- `bar.inline-red-fixes`, which the write gate and the commit grader read
  ([the red-fix lane](red-fix-lane.md));
- `memory.staged-render`, which the build-index generator's `--write-staged` reads
  ([the commit render](commit-render.md));
- `policy-file.on-invalid`, which the reader itself reads ([below](#how-to-use-it)).

Every other key has no consumer yet: the build its catalogue row names as `owner` adds one, so a
value you set for any other key today is checked but changes no behaviour.
The one exception is an invalid file, which the push gate refuses when it has nothing to fall back
to, below.

The kit README, `tools/policy/README.md`, is the full reference: the row fields, the grammar of
allowed values and every check.

## How to use it

- **Set a key:** a key `a.b.c` is a dotted TOML path, so `budgets.enforce` is written

  ```toml
  [budgets]
  enforce = "refuse"
  ```

- **Read a key:** `python tools/policy/policy.py get budgets.enforce` prints the key's value: a
  string as itself, a number or `true`/`false` as TOML spells it, a list one member per line. It
  reads the file **as committed at the landed revision**: the tip of the branch
  `refs/remotes/<remote>/HEAD` names. A clone sets that ref, and `git remote set-head <remote> -a`
  sets it after a first push; `export GOV_DEFAULT_BRANCH=<branch>` names the branch outright. In a
  clone with no remote it is the local branch `GOV_DEFAULT_BRANCH` names. When neither names one,
  `main` is the fallback, and a repository with no `main` refuses, naming the missing ref and these
  remedies. It never reads your working tree, so an edit
  you have not committed and pushed does not change what it prints, and once a gate reads its
  policy through it, an uncommitted edit cannot change what that gate enforces.
  - `--rev <rev>` reads the file at that commit instead, `--rev HEAD` for your last commit.
  - `--explain` adds one line on stderr naming where the value came from and the commit:
    `policy: budgets.enforce · file · set in .governance/policy.toml at 3708a705, <remote>/main, the landed revision`.
  - It refuses, exit 2 with one `policy: refused · <path>:<line> · <why>` line, a key no catalogue
    row names, a string that is not one TOML key, a revision that names no commit, an invalid file
    it cannot fall back from (below), and a key whose catalogue row carries no default when the
    file does not set it.
  - With several remotes and none chosen it refuses too: `export GOV_REMOTE=<remote>` names one.
  - With no default branch named and no `main` it refuses naming the missing ref: `git remote set-head <remote> -a`, or `export GOV_DEFAULT_BRANCH=<branch>`, names one.
  - The file is parsed as TOML and never run, so a line in it cannot execute anything.
- **Where a value comes from:** every key resolves in one order, `RESOLUTION_ORDER` in
  `tools/policy/policy.py`: the value the file sets, else the catalogue default. `--explain` says
  which, after the sha and how the revision was found:
  - the file sets the key: `file · set in .governance/policy.toml at <sha>, <how>`;
  - the file does not set it: `default · not set in .governance/policy.toml at <sha>, <how>; the catalogue default`;
  - there is no file at that revision: `default · .governance/policy.toml is absent at <sha>, <how>; the catalogue default`.

  A file that names a `preset` reads the catalogue default too, for now: the reason adds
  `; the file names preset <name>, not applied until dKeptSession adds presets to this reader`.
  A value you set in the file always wins over the default.
- **When the file is invalid:** a file that is not TOML, sets a value outside its key's allowed
  values, or sets a key no catalogue row names is invalid, and an invalid file NEVER reads the
  catalogue defaults, because a default may be looser than what you chose. `policy-file.on-invalid` <!-- usage: policy:policy-file.on-invalid 89965eb1 -->
  decides what it reads instead, and it is itself read from the last valid revision of the file,
  never from the invalid one, so an out-of-set value of it is one more problem:
  - `last-valid` (the default): every key reads the newest earlier commit whose file was present and
    valid, the whole file and never one key, with source `last-valid` and a reason naming the
    invalid commit, the line, the problem and the valid commit. With no valid commit before it, the
    read refuses, naming the line.
  - `refuse`: every read refuses, naming the invalid file's line.

  A missing file is not invalid: every key reads its default. A key the file does not set reads its
  default too, except a key whose catalogue default is prose, `{ derived = "..." }`: no reader
  computes it yet, so `get` refuses it, naming the row, until the file sets the key. A file saved in
  another encoding than UTF-8, as a PowerShell redirect writes it, is invalid, and a clone too
  shallow to reach a valid commit refuses saying `history is shallow`; fetch more history.
- **Check the committed file:** `python tools/policy/policy.py check` checks the file as committed at <!-- usage: script:tools/policy/policy.py#check a787d169 -->
  `HEAD`, the commit a push lands; `--rev <rev>` checks another commit. It exits 0 with one
  `policy: check · ...` line when the file is valid, missing, or invalid with a valid commit to fall
  back to under `last-valid`, the line saying which, and exits 2 with the refusal otherwise. The
  `policy check` gate runs the same check on every push and landing, so an invalid file with nothing
  to fall back to blocks the push.
- **Check the file:** `python tools/policy/check_policy.py`. It refuses a value outside its key's <!-- usage: script:tools/policy/check_policy.py 49bb87e8 -->
  allowed values, an empty set for a key that is never empty, and a key no catalogue row names. Each
  check prints one line with the number it read; a check that read nothing is red too, unless reading
  nothing is a legal state, no policy file yet, no tracked code, no owner build landed, or no landed
  revision yet, which it prints as `not graded`.
- **Start a file in another repository:** see [Install](#install), below.
- **See which keys are documented:** a catalogue row with no `summary` or no `usage` is named on
  `tools/policy/unsummarised-keys.txt`. That list may only shrink. To document a key, give its row a
  `summary` and a `usage`, then run `python tools/policy/policy.py lists --write` to drain it from the <!-- usage: script:tools/policy/policy.py#lists 54ff8bae -->
  list. `python tools/policy/policy.py lists --check` reds a list that grew past the one the default
  branch carries.
- **See which keys no build has picked up:** a catalogue key that no clause on its owner build's row
  of the design view names is listed in `tools/policy/unnamed-keys.txt`. The list is generated,
  coding-governance's own, and never installed into another repository; it may only shrink. A key
  leaves unnamed-keys.txt one way: its owner build records a deviation that moves a clause naming the
  key, in backticks, onto that build's row; then `python tools/policy/policy.py lists --write` drains it.
  `lists --check` reds a listed key a clause now names (`stale`), a new key no clause names, and a key
  the default branch's list did not carry. Where the design is not declared, as in every other
  repository, the check prints `policy lists: unnamed-keys.txt · not graded`.
- **Know which keys are loop bounds or deadlines:** raising one loosens the policy, so its catalogue
  row says so with `direction = "raise-loosens"`. A row is one when its allowed values are a retry,
  round or route-back count, or a number of hours, days or seconds. The check reds such a row that
  says nothing, and any row with another `direction`. Adding a new key of one of those kinds? Give
  its row `direction = "raise-loosens"`.

## Presets

A preset is a named, complete set of values for the policy keys, so a repository can pick a posture
with one key, `preset`. Four ship in `tools/policy/presets.toml`: `velocity`, `standard`, `strict`
and `guarded`. `standard` sets every key to its catalogue default. The reader does not apply a
preset yet, so until dKeptSession's reader step lands a named preset changes no value you read.

Some keys stay out of every preset: the file's `never` list names the keys presets never touch, such
as `floor`, `preset` itself and `policy-file.guard`, because loosening the guard or switching an
invariant off stays the owner's own choice. Every other key with a literal default has a value in
every preset, and so do `maintain.fixes` and the six review stage keys, `review.plan` to
`review.maintain`, though their defaults are derived: the store's `literal` list names those two
rows. Every other key with a derived default, such as `budgets.*`, `roles.effort.<role>` and
`review.<stage>.effort`, has a value in no preset, and a preset of yours may not set one either.

The store also holds pairs of keys where one must be at least the other, such as `review.max-rounds`
over `review.design.round-count`. Each pair rule is checked over the four presets only. Your own
policy file may set a round count above its ceiling and still read valid; the review loop refuses
that count when it runs, as it did before presets existed.

- **Check the presets:** `python tools/policy/presets.py check` prints each preset with how many keys <!-- usage: script:tools/policy/presets.py#check daa13502 -->
  it sets, then one `unassigned` line naming the derived-default keys no preset sets, and exits 1
  naming the preset and the key for a missing key, a value the key's row refuses, a derived
  default's text used as a value, a review stage key one preset sets and another lacks, a
  `standard` value off its default, or a broken pair.
- **Declare your own preset:** add a `[presets.<name>]` table to `.governance/policy.toml` with
  `extends` naming a shipped preset and the keys you change, then set `preset = "<name>"`:

  ```toml
  preset = "ours"

  [presets.ours]
  extends = "strict"
  "leases.expiry-hours" = 12
  ```

  `python tools/policy/policy.py check` refuses an `extends` naming no shipped preset and a key
  presets may not set.
- **Load a preset:** `python tools/policy/presets.py load strict --repo .` judges each of the <!-- usage: script:tools/policy/presets.py#load 8cba698f -->
  preset's values by the loop kit's expansion rule, the same rule the loop guard applies, and exits 2
  naming each value it refuses. On a core-only install `strict` and `guarded` still load, because the
  release slot `build.closes = "after-release-verifies"` needs is a core point; refusing them there
  waits on the loop kit's ask TOOL-dDeclaredLoop-101.
- **Add a preset to the shipped store:** the kinds register's one verb copies a shipped preset into a
  new table and adds its name to the `preset` key's values, then checks the store, putting both files
  back when the check is red:

  ```text
  python <prefix>/playbook/core.py new preset <name> --from <preset>
  ```

## Install

`bash tools/policy/adopt-policy.sh --scaffold --target <repo>` starts the policy file in another <!-- usage: script:tools/policy/adopt-policy.sh f6cd6f1b -->
repository. It writes the starter file only where none exists, then renders the harness settings
from the agent limit and the policy mirror wherever the repository has a commit, so the first agent
spawn passes and the merge bar finds the mirror fresh. `--check --target <repo>` checks that
repository.

The mirror renders a commit, so on install day, while the install and the policy file are not
committed yet, `--scaffold` prints
`adopt-policy: mirror deferred · <file> has uncommitted changes · commit, then re-run --scaffold`
and still exits 0. In that order:

1. commit the install and the policy file;
2. run `--scaffold` again, which writes `.governance/policy.json`.

A policy file that is invalid on install day is never deferred: `--scaffold` runs `check_policy.py`,
and when its `arm_schema` check finds a problem, a value outside its key's allowed values say, it
exits 2 printing that check's findings and no deferral line. Fix the file, then re-run `--scaffold`.
Any other refusal of the mirror stops it, exit 1, with the refusal's own line.

## Every key whose build has landed has a reader

Each catalogue row names the build that owns the key. Once that build has landed, a key no code
reads is a setting you can change to no effect, so `python tools/policy/check_policy.py` reds it:

```
reader coverage: budgets.enforce (owner dGroundRules, landed at 3708a705) has no reader
```

- **Landed** means: on the default branch as `policy.py get` reads it, either the build's folder
  `memory/builds/<owner>/spec/` holds at least one spec and every spec there is `CLOSED` or
  `WONTDO`, or a build run of it landed. A build run landed when one of the build's run records,
  `RUN.md` or a rotated `RUN.LANDED.<8 hex>.md`, carries a `base:` that names a commit, the run at
  that base was a build run rather than a spec run, and a merge on the default branch touched the
  build's `RUN.md` with that same base. So a build run that landed with a unit carried forward as
  `DEFERRED` counts as landed. A spec run, which carries every unit `DEFERRED`, does not: at its base
  the build still had an open ask and a roster unit with no spec. Your working tree never counts:
  only what is committed on the default branch does.
- **A reader** is a line of tracked code that passes the key to the policy reader, in one of three
  shapes: a call whose first argument is the key in quotes, such as `resolve("budgets.enforce")` in
  Python or `mirror.get('budgets.enforce')` in JavaScript; `policy.py get budgets.enforce` in a
  shell script or a git hook; or, in Python, a call passing the name of a module constant that holds
  the key, such as `resolve(KEY)` in a file whose line `KEY = "budgets.enforce"` starts at column 0.
  That call may sit inside another call's arguments, and may pass the name as `key=KEY`. A comment, a test file, a help page, the memory tree, the JSON mirror
  and the catalogue never count. For a key with a `*` or `<name>` part, such as `budgets.*`, a
  variable in that part counts too: `policy.py get "budgets.$cap"`, or a quoted part holding the
  variable, `resolve(f'budgets."{cap}"')`.
- **To clear it,** do one of three things: add the reader, a call of that shape where the code uses
  the value; or, if the key's build has not really landed, make the row's `owner` a build that has
  not landed yet; or, if the only code that uses the key sits where the check does not look, under
  the memory tree say, declare it in `tools/policy/unscanned-readers.txt`.
- **A declared key** is one row of `unscanned-readers.txt`: `<key> <path> <reason>`, split on the
  first two runs of whitespace, spaces or tabs, so the path holds no whitespace and the reason is the
  rest of the line. Lines
  opening `#` and blank lines are skipped. A declared key is never counted as read. Instead every run
  prints its row after the summary line:

  ```
  reader coverage: <key> (owner <owner>) declared outside the scan at <path>: <reason>
  ```

  The row must stay true. Each of these reds the check: a line that is not a row
  (`unscanned-readers.txt:<n> is not a row`), a key no catalogue row names, a key on a second row,
  a declared key the scan now reads (`drop its row`), a path that is not a tracked file, and a path
  the check already reads (`give the scan its shape instead`). The last three apply once the key's
  owner has landed. The check does not confirm the file really uses the key: the printed reason is
  your claim, there for anyone to read. The list is gov's own, and no install receives it.
- **Every run says what it graded:** `reader coverage: graded <n> of <m> catalogue key(s); landed
  owners: <builds>`, and while no owner build has landed,
  `reader coverage: graded 0, so this arm checked nothing at <commit>`, which passes. A git read
  the check makes that fails stops it with one finding naming the read:
  `git <arguments> failed, so reader coverage cannot read the tree`.
- **What it does not see:** a reader in another language, or one that builds the key's name at run
  time from pieces, reds as unread. So does a key passed through a constant from another file, a
  variable set inside a function, a constant in JavaScript or shell, a name inside a tuple or a loop
  rather than a call's arguments, or a call whose arguments span lines. A call that only mentions the
  key, in a message say, counts as a reader, and so does any call that passes the constant's name,
  `print(KEY)` included.

## Who may change the policy file

An agent that could commit any change to the policy file could loosen any rule, so the policy file has
one door, a guard on every commit that changes it, a check on every push that lands it, and a floor
the guard protects. The owner ruled on 2026-11-12 that no file is owner-only to a run working under
its build's mandate, so a live unattended run's branch is admitted throughout, and every change it
makes is recorded.

**The door: `policy_edit.py`.** The harness refuses an agent's Edit, Write, MultiEdit or NotebookEdit
of `.governance/policy.toml`, naming this command; it writes the file, writes the change record and
stages both:

- `python tools/loop/policy_edit.py set <key> <value> --build <slug> --unit <id>` sets one key. Its <!-- usage: script:tools/loop/policy_edit.py#set 46041bd3 -->
  value is checked against the key's catalogue row, and a `floor` member against the four members.
  It writes when the owner proves themselves, standard error an interactive terminal and then the
  word `yes` typed at its prompt, or when the branch is a live run's branch, which needs no prompt.
  Otherwise it prints the proposal and exits 1, writing nothing.
- `python tools/loop/policy_edit.py raise <cap> <new> --build <slug> --unit <id> --argument <text>` <!-- usage: script:tools/loop/policy_edit.py#raise 9a04e39d -->
  is the agent's door for one measured-file cap, below, and needs no proof.
- `python tools/loop/policy_edit.py propose <key> <value>` writes nothing: it prints the row diff <!-- usage: script:tools/loop/policy_edit.py#propose 25930781 -->
  and the `set` command that would apply it.

Every write prints `Proof: <proof>` (`tty-cli`, `none — run mandate <run-state file>` or
`none — budgets raise`) and the trailer line the commit must carry, one per changed key:
`Gov-Policy: policy.<key> <old> -> <new>`, each value as compact JSON and `none` for a key the file
did not set. Its change record, under the build's `build/` folder, names the key's catalogue row
(`policy.review.max-rounds`, or `policy.budgets.<cap>` for any cap). A value the policy file selects whose
component is not installed, `policy-file.proof = "signed"` say, is refused, or read as its default
with one line saying so, as `policy-file.on-missing-expansion` says.

**The guard.** This repository's pre-commit hook guards four paths, listed in
`tools/policy/guarded-paths.txt`:

- `.governance/policy.toml`, the policy file;
- `.governance/policy.json`, its JSON mirror;
- `.governance/instructions.toml`, the instruction manifest;
- `.governance/deploy.toml`, the deployer's answers.

- **The owner commits from a terminal.** A commit made at a terminal is the owner's proof, and the
  hook admits it, printing `policy guard — <paths> staged, admitted on the owner's terminal proof.`
  An agent's shell has no terminal, so the hook judges its commit instead, through the loop kit's
  `guard.py --staged` where the loop kit is installed, else the policy kit's minimal guard alone. The
  verdict reads its rule from the landed revision, never the staged file, so a commit cannot loosen
  the rule that judges it. In order:
  1. **The guard's own switch.** A change to `policy-file.guard`, `policy-file.proof`, any `floor`
     member, or the list of guarded paths is refused, naming `floor.guard-self`, for every agent commit
     off a live run's branch, whatever `policy-file.guard` reads.
  2. **Every change recorded.** Each changed key needs a staged change record naming its row, and a
     change to the list one naming `kit.policy`; a missing one is refused, naming the key.
  3. **The value of `policy-file.guard`.** Under `owner-only`, the default, and under
     `agents-within-mandate`, which the ruling widened to the same, an agent's commit is admitted in
     the shapes below: one cap raised, the mirror's render, or a live run's branch. Under
     `agents-with-reason` a commit changing the policy file alone is also admitted when it adds a row
     to `memory/DECISIONS.md`.

  The verdict prints `loop-guard: admitted · <rule>`, or `loop-guard: refused · <path> · <why>` per
  reason with the remedy; the minimal guard's own `policy-guard:` lines pass through.
- **An agent may change the policy file one way: raise one measured-file cap.** One key under
  `[budgets]` whose name is the path of a tracked file, set to a larger whole number, and nothing
  else in the four files changed. The commit must carry its argument and its record:
  - comment lines added directly above the cap, one of them `RAISED <old> -> <new>`;
  - at least one row added to `memory/DECISIONS.md`, with no row removed;
  - the change record naming `policy.budgets.<cap>`, and the `Gov-Policy:` trailer.

  `policy_edit.py raise` writes all but the decision row, which it prints for the caller to add. It
  writes only on the four conditions of the paragraph "WHEN A RUN MAY RAISE A ROW" of
  `tools/template-size-limits.txt`, each refusal naming its condition: the file, measured without CR
  bytes, exceeds the old cap; no comment above the cap reads `reserved: owner`; the `RAISED` line; and
  the record. The cap must be set in the policy file at `HEAD`: a cap still in its legacy home is the
  owner's to move into the file. Other files may ride in the same commit: a raise belongs in the
  commit of the unit whose change needed it. Worked example, raising the cap on `AGENTS.md` from
  20480 to 24576:

  ```toml
  [budgets]
  # RAISED 20480 -> 24576, 2026-10-24, TOOL-x-1: the new role section measured 21900 bytes
  "AGENTS.md" = 24576
  ```

  with a row such as `- TOOL-x-1 · AGENTS.md cap 20480->24576: the role section needs it` added to
  `memory/DECISIONS.md`. The hook prints
  `policy-guard: admitted · budgets."AGENTS.md" 20480 -> 24576 · its change record attached`.
- **An agent may also commit the mirror it regenerated, in a commit of its own.** A change to the
  policy file or to `tools/policy/catalogue.toml` leaves the mirror stale, so it takes two commits:
  first the policy or catalogue change, then `python tools/policy/policy.py mirror --write` and a <!-- usage: script:tools/policy/policy.py#mirror f4887510 -->
  commit of `.governance/policy.json` with neither of those two files staged beside it. The hook
  renders the mirror at `HEAD` itself and admits the staged one only when its bytes are that render,
  printing `policy-guard: admitted · .governance/policy.json · equals its render at HEAD`.
- **An agent's commit on a live run's branch is admitted.** Any change to the four files that the
  shapes above would refuse is admitted when the branch being committed on is the `run-branch:` of
  an unattended run's run-state file, `builds/<slug>/RUN.md`, committed at `HEAD`, and that file's
  `phase:` at `HEAD` is not one of the `PHASES_TERMINAL` phases the unattended driver at `HEAD`
  declares. The guard reads `HEAD`, never the staged run-state file, so a commit cannot admit itself.
  It prints `policy-guard: admitted · <paths> · the run-branch of <run-state file>, phase <PHASE>`,
  and asks for no decision row: every commit on a run branch is already joined to a specced unit.
  When no live run names the branch, the refusal lines below are followed by one
  `policy-guard: not a live run's branch · <why>` line per reason: a detached `HEAD`, no run-state
  file at `HEAD` naming the branch, no driver declaring the terminal set, or a terminal phase.
- **Everything else is refused**, each reason on its own `policy-guard: refused · <path> · <why>`
  line: a lowered cap, two caps changed, a cap added or removed, a class row such as
  `memory/builds/*/spec/` (it names no one file), `budgets.enforce` or `budgets.pinned`, any other
  key, a raise missing its `RAISED` line or its decision row, another line of the file changed, and
  any change to the instruction manifest or the deployer's answers. A mirror staged beside a change
  to any file it is rendered from, the policy file, the catalogue or a key of the mirror's
  `legacy_blobs` record (today `.agent-cap.conf` alone), is refused
  with `the mirror renders HEAD and its input <path> is staged changed: commit <path> first, then
  regenerate`; one that is
  not its render, a hand edit say, with `differs from its render at HEAD`. Unstage it with
  `git restore --staged --worktree .governance/policy.json`; the landing renders it too.
- **A merge that takes one side's file** writes nothing new and is admitted; a merge that writes a
  third text is judged like any other change.
- **What the guard does not catch.** It stops forgetting, not evasion: `git commit --no-verify`, a
  wrapper that gives an agent's commit a terminal, a line removed from the list in one commit and the
  file changed in the next, a commit made in another clone, a cherry-pick or a rebase (no pre-commit
  runs), the guard file deleted from the working tree, and a run-state file committed naming the
  agent's own branch with a live phase, which admits every commit after it, all pass it. It reads
  the phase a run-state file records, not the one the unattended kit derives, so a run that has
  landed reads live until a terminal phase is committed. The hook binds once it is on
  `main` in the primary checkout, whose hooks every worktree runs. The push gate does not re-check
  who made a change. A live run may switch a floor member off, or change `policy-file.guard` or
  `policy-file.proof`: only its change record and the push check below witness it. A change to the
  list of guarded paths alone stages no guarded path, so the hook never calls the verdict for it.

**The push check.** The pre-push hook, on a push to the default branch the remote already holds, runs
the loop kit's `guard.py --push-range` over the pushed commits: each commit that changes a key of the
policy file must carry one `Gov-Policy:` trailer line per changed key and add a change record naming
the key's row. One that does not is refused as `policy-unrecorded`, naming the commit and the key. A
commit that adds the policy file, as an adopter's scaffold does, is printed and not graded, and so is a
merge none of whose parents holds the file. A merge any of whose parents holds the file is graded as
below, a parent lacking it read as setting no key, so a merge whose first parent is an orphan branch or
deleted the file is graded too. Merges are graded too. A two-parent merge whose clean re-merge git
computes owes the trailer and the change record itself for each key its result sets to a value other
than that re-merge's, a key set back to
one side's old value included, the trailer's old value the re-merge's, and is refused as the merge's
own change when it lacks them. A merge equal to its re-merge, a clean merge of two sides' different
keys say, owes nothing, since its sides' own commits are graded in the same push. A merge whose
clean re-merge's policy file does not parse, two sides declaring the same table apart say, is refused
naming the merge and `does not parse at C`, never graded against its parents; one whose own file does
not parse is refused naming `at M`. A merge whose clean re-merge fails, an unrelated-history merge
or a broken object store say, is graded against every parent, with one line naming the failure: it
owes the trailer and the change record for each key that differs from one parent, the trailer's old
value the first such parent's. A git whose usage probe fails, cannot start or prints no usage text is
graded as a failed re-merge too, and only a usage text lacking `--write-tree` reads as a git without
it; a probe exiting other than 0 or 129, or printing no `usage: git merge-tree` line, is a failed
probe whatever else it prints. A re-merge that conflicts only on other files still holds the policy file's clean merge, so the
merge is graded against that re-merge as above. Only an octopus merge, a merge whose re-merge conflicts
on the policy file itself, or a git
without `merge-tree --write-tree` is graded against its parents alone,
with one line saying so: it owes for each key its result sets to a value no parent holds, the
trailer's old value the first parent's. With no python launcher or no loop kit, the hook prints one
line saying the check did not run.

**The floor.** Four invariants hold whatever else the file says, each switched by a member of the
`[floor]` table and every one `on` until the file sets it `off`; `python tools/loop/floor.py get <member>` <!-- usage: script:tools/loop/floor.py#get 8ed45f24 -->
prints a member's value:

| Member | What it keeps | Switched `off`, it reports instead of refusing at |
|---|---|---|
| `verdict-before-move` | a binding verdict runs before the default branch moves | the pre-push hook's `gate RED` refusal: the push goes through printing `floor: verdict-before-move off`, and no green record is written |
| `record-changes` | every policy change and stage transition recorded | the verdict's record step, the push check, and the loop kit's transition check |
| `guard-self` | the guard protects its own switch off a live run's branch | the verdict's first step |
| `no-actor-witness` | no stage witness reads a fact the acting agent typed | the loop kit's two refusals of an actor witness no list row names |

Switching a member `off` is a change to the guard's own switch, so off a live run's branch it is the
owner's, committed from a terminal.

## The keys the file holds today

| Key | Default | What it sets |
|---|---|---|
| `policy-file.on-invalid` | `last-valid` | what a malformed file or an out-of-set value reads as: the last valid landed revision, or `refuse` |
| `budgets.enforce` | `warn` | whether a size cap's breach warns or refuses, for every cap not pinned |
| `budgets.pinned` | `[]` | the caps that refuse on a breach whatever `budgets.enforce` says |
| `runtime.agents-in-flight` | `6` | how many agents one session may have in flight; at least 1 |

## The policy that still lives elsewhere

Some policy has not moved into `.governance/policy.toml` yet. It lives in three older places: the
kit settings files at the repository root (`.unattended.conf`, `.memory-tree.conf` and the other
`.*.conf` files), the gate settings file `.githooks/gate-env.sh`, and the roles kit's
`house/policy.toml`. `tools/policy/legacy-homes.txt` lists every key those places hold. It is
generated, never typed: `python tools/policy/policy.py lists --write` writes it.

The list is coding-governance's own and is never installed into another repository. There the policy
check prints `arm_legacy_homes · not graded · the list is gov's own and is withheld from installs; …`,
even if that repository writes a list of its own, and `lists --write` does not create the file.
`lists --check` there prints `policy lists: legacy-homes.txt · not graded` and grades the summary
list alone. The
deployer's `plan` shows the list as an `ORDER [project-owned]` row: that row is for information, and
the list is not yours to write.

- **A row** is `<place> <key> <mark>`, for example `.unattended.conf GATE_BOUND owner-policy`. The
  roles file's place is written `<tool-root>/roles/house/policy.toml`, which means the roles kit
  wherever this repository installed it, and its keys are its tables, `[effort]` and `[gates]`.
- **The marks.** `owner-policy` is a choice the owner makes, which a later build moves into
  `.governance/policy.toml`. `mechanic` is plumbing that stays where it is, such as which Python the
  hooks use. Every settings-file and roles-file key is `owner-policy`; a gate settings key takes the
  mark `GATE_ENV_MARKS` in `tools/policy/policy.py` gives it, and a key that table does not name is
  `unmarked`, which `lists --check` reds until someone adds it there.
- **Left off on purpose:** a settings key ending `_CUTOFF` or `_PIN`, which a later build converts
  rather than moves.
- **The list only shrinks.** `python tools/policy/policy.py lists --check` compares it with the places
  it is read from and with the copy on the default branch. Removed a key from its place? The check
  says `stale list at <row>`; run `lists --write` and the row goes. Added a key? The check says
  `<place> <key> is a new legacy home and the list is shrink-only`, and `lists --write` refuses to add
  it. Do not add the key to the old place: carry it as a key in `tools/policy/catalogue.toml`
  instead. A row typed into the list by hand reads `typed row <row>`.

## Example

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
python tools/policy/check_policy.py
# policy-check: arm_schema · 0 finding(s) · 4 key(s) of .governance/policy.toml against 267 row(s)
# policy-check: arm_shape · 0 finding(s) · 267 row(s), 19 set-valued, 10 never-empty
# policy-check: arm_summaries · 0 finding(s) · 263 of 267 row(s) unsummarised · ...
# policy-check: arm_direction · 0 finding(s) · 19 loop bound and deadline row(s)
# policy-check: arm_on_invalid · 0 finding(s) · .governance/policy.toml at 7c8c0c4f is valid
```

With `runtime.agents-in-flight = 0` in the file, the first line reads `1 finding(s)` and the next
line names the key: `runtime.agents-in-flight: 0 is below the minimum 1`.
