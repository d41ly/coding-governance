**Serves:** journal TOOL-aOrientedCast-1 PLAY-aOrientedCast-1

# Resume handoff — aOrientedCast's second addendum, as an unattended feature build

## Role

You are the main loop of the unattended run `aOrientedCast`, resumed in its own session on node `a`.
You orient, add units, dispatch, keep the records and close. You write no spec and no product code
yourself: spec writing, spec review, building and the closing review run only in role agents, and
the hooks refuse the rest. Follow `memory/guides/UNATTENDED-PROTOCOL.md`,
`memory/guides/UNATTENDED-VERBS.md` and `memory/guides/BUILD-METHOD.md`; this handoff adds the task,
not a second copy of their rules.

## Where the run stands

- `memory/builds/aOrientedCast/RUN.md` reads phase HELD, `hold-code: host-degraded`,
  `hold-until: probe host`. Every unit of the first eighteen is CLOSED.
- The build merged onto local `main` at `6081d92e4`, unpushed. The run branch,
  `branch/deterministic-attended-workflows-943570`, is local `main` plus the owner's second addendum.
- That merge kept main's v4.3 charter, which has no `## §<n> — ` headings. Every role's `charter`
  id now resolves to nothing: `tools/roles/check_roles.py` reports one R4 defect per id, and
  `tools/roles/render_agents.py --check` refuses on the first. `handoff.py render` refuses too, so
  the spawn guard admits no direct `Agent` spawn until this build repairs it. Dispatch every stage
  through the harnesses by `scriptPath`, passing `handoff.py harness-args <stem>` as `roles` and
  `handoff.py stage-efforts <workflow>` as `efforts`. Both still answer: they read the workflow
  table and the policy file, not the charter. The stem is the script's name without its extension,
  such as `unattended-build`; a path is refused.

## The task

**The design is the owner's, already decided:**
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md`.
Read it whole. Its four forks are settled; do not re-open them.

1. **Resume.** Probe the host first: the hold names node `a`'s kernel pool leak, which makes every
   spawn cost a second. Read `LastBootUpTime` and time one `git rev-parse HEAD`. If the host is still
   degraded, stay HELD and say so in one line; do not build on it.
2. **Add the units** with `unattended.sh --rescope aOrientedCast --act add`, one per unit, before
   any spec exists. A suggested split, which the spec writer may refine:
   - a tooling unit for the roles kit: the `rules` key replacing `charter`, the `mandatory` and
     `output` fields and their checker rules, R4 re-keyed to section 1 rule tags, the `roster` verb,
     agent types carrying the cited rules and the whole rendered `## Protocols` section, and
     `handoff.py` following suit;
   - a playbook unit: the `[roles]` rule in section 1, the `## Agent roles` subsection with its
     derived `{{ROLE_ROSTER}}` placeholder and probe, the `Tools to rely on` line trimmed to `/build`,
     and the charter re-rendered. It consumes the roster verb, so it follows the roles unit;
   - a tooling unit for the exception: the owner waiver registry for an inline stand-in, graded like
     the other waiver registries under `memory/project/`, and the no-spawning case stated in the rule.
3. **Spec, then build, then the closing review,** through `tools/workflows/unattended-build.js`,
   `tools/workflows/unattended-unit.js` and `tools/workflows/tier2-review.js`. The spec audit is the
   owner's opt-in and is not declared; do not declare it.
4. **Done means:** the catalogue checker exits 0 and `render_agents.py --check` reads fresh on the
   reconciled tree; the playbook render writes the roster; `help/roles.md` describes the new section
   and fields; each new refusal is observed RED on a staged break and GREEN once restored, by the
   main loop. At minimum: a roster line past 200 characters, a rule tag naming no section 1 rule, a
   mandatory role whose workflow names no enforcing hook, and an inline stand-in with no waiver row.

## Constraints this run has already paid for

- **Passes run fast, diff-scoped checks only.** No bar, no self-test suite and no suite slice in a
  pass; role agents run only what the policy file's `[gates]` allows.
- **A pass commits its spec before its code,** carries `RUN.md` in its commit, and declares at
  `--dispatch` every generated path the hooks will write. An inline unit still owes its `--brief` row.
- **A kit file names no sibling kit by literal.** The playbook probe reaches the roles kit through a
  render token, never a path.
- **Bump each kit's version once, after its last move:** the roles and playbook kits, every carrier
  `tools/check-kit-versions.sh` and `tools/govkit/govkit.py` read. The template is in the kickoff
  manifest's `watch:` list, so touching it owes the manifest's `last-audit` re-stamp in that commit.
- **A spec's §6 cannot cite a file not yet built** by its repo path; use the basename form.
- **A new shell function or Python symbol stales the codebase map;** run `gen_map.py --write`
  before the close.
- **Read every gate's result line from a file,** never through `tail`; a filtered red cost this build
  a refused dispatch.

## The close

Run the closing review over the cumulative diff of the new units. Then merge the run branch
`--no-ff` into local `main` and stop: no push, and no full bar, because the owner runs the gates on
the reconciled tree. Leave `RUN.md` stating what the close still owes.

**Return:** the units added, each with its final status; the merge sha; every staged break observed,
with its red and green lines; and what the close leaves owed.
