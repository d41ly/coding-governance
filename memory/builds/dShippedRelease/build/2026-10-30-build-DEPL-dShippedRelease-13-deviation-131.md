# DEPL-dShippedRelease-13 deviation 131 — `deploy.core` starts or finds the bar and reads its verdict; the lander does neither

**Serves:** deviation DEPL-dShippedRelease-13

- **Departs from:** `cl-dClosedLoop-0423@a58b92bf` [deploy.core]
- **Hand-off:** design-to-spec
- **Before:** the lander running the core checks on the landed tree before it releases the build
- **After:** the lander starting the full bar where the landed tip declares one and the item `deploy.core` starting or finding that bar on the landed SHA and reading its verdict keyed by that SHA before `deploy.unlease` releases the build, so a core red the landing merge introduced files a patch build through the entry-point table's post-close row before that build closes, the landing recorded red meanwhile, and that build closes only once the patch build's core checks are green for a SHA that contains the landed one or an exception under `core.exceptions` is recorded, seen red on a planted red landed tree whose build closes with no filing and on a planted red landing whose patch is filed and not yet green (foundations K1)
- **Cause:** design defect
- **Reason:** The clause says the lander runs the checks. Source shows the lander starts a bar, detached, and returns, its header saying it does not check whether that bar finished, and an undeclared key starts nothing. A lander that held its process for the whole bar would lose the check to the same killed process cl-dClosedLoop-0508 plants, and its exit is already what `deploy.land` routes on. So the check moves to the item the flow already names, `deploy.core`, and the clause's intent holds: nothing releases the build until the landed tree's verdict is read, since the build's lease stays live until `deploy.unlease` (pin C4) and `deploy.close` reads the settlement. The clause's two seen-red cases are observed unchanged. Also follows through as: gap gap-deploy-02.
- **Evidence:** `tools/push-main.sh:43-47` and `:427-465`; `flow-steps.md:438` and `:452-456`, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`; scout A disagreement 3, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md:93`; DEPL-dShippedRelease-13 §8 F2
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0423@a58b92bf
- **Caused-by:** DEPL-dShippedRelease-13
