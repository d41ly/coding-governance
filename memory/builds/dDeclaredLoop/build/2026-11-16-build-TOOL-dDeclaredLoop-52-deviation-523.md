# TOOL-dDeclaredLoop-52 deviation 523 — the hold's gate read prints its own refusal, and an unread answer holds

**Serves:** deviation TOOL-dDeclaredLoop-52

- **Departs from:** `TOOL-dDeclaredLoop-52@rev-3` [§4]
- **Hand-off:** spec-to-code
- **Before:** §4 "The hold" calls `read_held_gates <slug> "<crossed tags>" >/dev/null` and names no answer for a `phase` line that carries no `· crosses ` field; §5's sweep keeps the driver suite green because its `--phase` moves are `RUNNING` to `BUILDING` or are refused before the call, and its last command counts this spec's rows of the positional registry as two.
- **After:** `check_phase_gates` calls `read_held_gates` with no redirect, so where the fork cutoff does not load its numbered refusal prints and the move is refused; a first line carrying no `· crosses ` field is relayed as the hold's why, so an answer the hold cannot read holds the move rather than passing it. The suite's in-place fixture also moves `BUILDING` to `VERIFYING`, crossing `item.build.exit`, which no owner gate holds under the defaults, so those moves print what they printed; the registry holds no row for this spec, the commit landing rev-3 having shrunk them.
- **Cause:** builder discovery
- **Reason:** `fail` prints on stdout, so the redirect the spec wrote would swallow the fork cutoff's refusal and leave `--phase` exiting 1 with nothing said; `run_loop_verb` prints nothing, so the redirect hides nothing else, and deny by default is the charter's posture for a read the hold does not recognise.
- **Evidence:** `tools/unattended/unattended.sh#fail`, `tools/unattended/unattended.sh#load_fork_cutoff`, `tools/unattended/unattended.sh#check_phase_gates`, the in-place fixture helper `iprun` of the driver suite, and a probe of `breakpoints.py list --build tRun` in a bare scratch repository printing the plan gate released by `authorization` and no `held` line.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the suite's in-place `--phase` arms read the default policy, observed at the close's suite run
- **Caused-by:** TOOL-dDeclaredLoop-19
