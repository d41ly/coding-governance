# PLAY-dOrderedCharter-55 deviation 558 — the pin verb's one ask is a tree listing, since a peel after a path is part of the path

**Serves:** deviation PLAY-dOrderedCharter-55

- **Departs from:** `PLAY-dOrderedCharter-55@rev-7` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S19 has `read_oid` in `tools/playbook/positional.py#run_pin` ask once with `rev-parse --verify --quiet --short=8 "<rev>:<path>^{blob}"`.
- **After:** `read_oid` asks once with `git ls-tree --full-tree --abbrev=8 <rev> -- <path>` and takes the entry's id where its type is `blob`, and nothing otherwise; still one ask, still no `cat-file`.
- **Cause:** builder discovery
- **Reason:** git reads everything after the colon of `<rev>:<path>` as the path, so the spelled peel names a path that does not exist and every citation is refused; the fixture's `positional-pin` plant redded with it, `pin did NOT rewrite the citation`, and greened with the tree listing.
- **Evidence:** in gov's tree `git rev-parse --verify --quiet --short=8 "HEAD:README.md^{blob}"` exited 1 while the same ask without the peel printed the blob's id; `gov_tag.py --fixture --plant positional-pin` printed `pin rewrote the citation to the blob at HEAD` after the change.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-26
