# TOOL-dDeclaredLoop-53 deviation 532 — the sweep's stale figures, and the plant list on the help page

**Serves:** deviation TOOL-dDeclaredLoop-53

- **Departs from:** `TOOL-dDeclaredLoop-53@rev-3` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep reads the driver's census ceiling as 340 PINNED at its tip, raised to 342 PINNED by `TOOL-dDeclaredLoop-19`; §5 "Dependency" reads `TOOL-dDeclaredLoop-52` on its rev-2, which builds no `--phase` hold of its own; S5 gives `help/loop.md` a paragraph and names no other edit on that page.
- **After:** the census ceiling reads 343 PINNED at this pass's base, `TOOL-dDeclaredLoop-52` having landed `check_phase_gates` over the extracted `read_held_gates`; no `*.sh` is edited, so the sites read are unchanged and the ceiling does not move. That hold reads only a `held` release, so it inherits the rule as §3 says, and its `driver-plan` plant runs this tree's module over a scratch, which reads as after the placement. The help page's fixture bullet also lists the two new plants, and its list bullet names the new release beside the other three.
- **Cause:** builder discovery
- **Reason:** the sweep was read at an older tip; the figures moved and the design claim did not. A help page that lists a script's plants and its release words is stale the moment the module gains one, which the charter's `[docs]` rule forbids.
- **Evidence:** the ceiling token of the driver in `.memory-tree.conf`, `tools/unattended/unattended.sh#check_phase_gates`, `tools/unattended/unattended.sh#read_held_gates`, and the `pre-placement` and `driver-pre-placement` plants run by direct CLI, each printing `held`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the close's `docs` and `memory hygiene` legs read the page and this record
- **Caused-by:** TOOL-dDeclaredLoop-52
