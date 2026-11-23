# TOOL-dQuietDisk-1 leg-tail 7 — playbook render selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** playbook render selftest
- **Hash:** 40871e5679e47515fbb4b97f73f413893d5aa640
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
arm ok    tags plant no-purpose-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant bad-purpose-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant member-no-field --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant pending-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant pending-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant pending-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant pending-source --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant registry-ghost --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant registry-missing --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant registry-joined --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant new-no-purpose --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant new-no-purpose --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant git-env
arm ok    tags plant toml-row
arm ok    tags plant dirty-rename
arm ok    tags plant dirty-revert
arm ok    tags plant worktree-recreate
arm ok    tags plant charter-warm
arm ok    tags plant charter-warm
arm ok    tags plant charter-dirty
arm ok    tags plant charter-dirty
arm ok    tags plant reference-row --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant reference-row --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant reference-no-h1 --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant reference-no-h1 --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
PASS — the tag resolver's plants
arm ok    tags plant policy-catalogue --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
arm ok    tags plant policy-family --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new
PASS — the policy namespace's plants
arm ok    edges plant good-block
arm ok    edges plant good-block
arm ok    edges plant good-block
arm ok    edges plant good-block
arm ok    edges plant fenced-edge
arm ok    edges plant space-target
arm ok    edges plant space-target
arm ok    edges plant comma-in-pair
arm ok    edges plant comma-in-pair
arm ok    edges plant bracket-target
arm ok    edges plant bracket-target
arm ok    edges plant two-types-one-line
arm ok    edges plant two-types-one-line
arm ok    edges plant no-equals
arm ok    edges plant no-equals
arm ok    edges plant unregistered-type
arm ok    edges plant declared-inverse
arm ok    edges plant declared-cites
arm ok    edges plant outside-to
arm ok    edges plant pin-on-none
arm ok    edges plant selector-registered
arm ok    edges plant selector-registered
arm ok    edges plant selector-describes
arm ok    edges plant promoted-elsewhere
arm ok    edges plant pin-no-at
arm ok    edges plant pin-bad-hash
arm ok    edges plant pin-no-text
arm ok    edges plant pin-other-type
arm ok    edges plant resolve-pinned-tag
arm ok    edges plant clause-no-rev
arm ok    edges plant resolve-pinned-clause
```
