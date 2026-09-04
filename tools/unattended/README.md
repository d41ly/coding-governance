<!-- gov:kit unattended@1.17 -->
# The unattended-run kit

The binding contract is not here. It is `UNATTENDED-PROTOCOL.md` together with
`UNATTENDED-VERBS.md`, both installed under the project's memory root by this kit's adopter. This
file covers only what a reader cannot get from those: what the adopter installs, and which of those
artifacts are generated rather than copied.

## What the adopter installs

Run `adopt-unattended.sh` from this directory; `--check` verifies without writing and is a gate leg.

| artifact | how it is produced |
|---|---|
| the `unattended` Skill | **rendered** from `SKILL.template.md` + `.unattended.conf` |
| the protocol | copied from `PROTOCOL.template.md` |
| the verb carrier | copied from `VERBS.template.md` |
| the playbook template | copied from `PLAYBOOK-TEMPLATE.template.md` |
| the playbook **fixture** | **rendered** from `playbook.fixture.template.md` |

Copied artifacts carry no placeholder, so rendering them would be a second spelling of `cat`. The
two rendered ones do carry placeholders, and for them a render is the only correct install.

## The fixture is rendered, and this is the one thing to know about it

`playbook.fixture.md` is a **generated artifact**. Do not edit it — edit
`playbook.fixture.template.md` and re-run the adopter, or `--check` reds.

It became rendered in `TOOL-dRetiredFork-12`. Before that it shipped verbatim with this kit's own
directory spelled out five times in its `outputs`, `grain`, `records` and `legs`, so an adopter who
installed the kit anywhere other than the default prefix got a fixture describing a tree they did
not have: `check-playbook.sh` exited 1, reported both pieces as unrecorded, and the suite above it
could not follow a variable the fixture did not have.

**It carries exactly ONE token, `KIT_DIR`**, and deliberately not a second. All five spellings sat
under this kit's own directory, so one token covers every one of them. `TOOL_ROOT` is *not*
declared here and must not be: only the memory-tree kit's adopter computes that value, so declaring
it would ship an unresolved `{{TOOL_ROOT}}` brace to every adopter of this one.

**The fixture RECORDS move with it.** Each is named for the piece it describes with `/` written as
`~`, so the prefix lives in their filenames as well as their bodies. The adopter repaths both.
Renaming without rewriting leaves each record describing a piece that does not exist, which
`check-playbook.sh` reports as an orphan record — coverage nobody has.

**An unresolved token is a refusal, and no file is written.** Catching it at `--check` time alone
would still leave a rendered artifact on disk carrying a literal brace, and something reads that
file before anything runs `--check`.

## Two things the validity gate does not treat as playbooks

`check-playbook.sh` grades every tracked markdown carrying a `step_selector` and a `toml` block,
minus two exclusions. `PLAYBOOK-TEMPLATE.md` is the canon, whose values are a specimen. And **any
`*.template.md`** is excluded for the same reason one level up: a template for a rendered artifact
necessarily carries unresolved braces, so grading one reds on a target that is not meant to resolve
until render time. That second exclusion was widened from the first the moment a second template
existed.

## Running the kit's own checks

```
adopt-unattended.sh --check      # the five artifacts are installed and in sync
check-unattended.sh              # the kit gate
check-playbook.sh                # playbook validity, including the fixture
run-unattended-gates.sh          # the kit's self-tests, ON DEMAND ONLY
```

The self-tests are deliberately **not** on the merge bar. A suite that stages breaks into a copy of
a checker has a job only when that checker's source changes, and none at all in an adopter's repo
that copy-installs this kit and never edits it. The three legs whose subject is the *repository* —
run-state records, playbooks, skill wiring — stayed on the bar, because those go stale with nobody
editing the kit.
