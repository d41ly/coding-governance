# TOOL-dQuietDisk-1 leg-tail 31 — selftest harness self-test failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** selftest harness self-test
- **Hash:** 819ea3f7b32a96f828ae3fe5b439ae92cc99a64d
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
ok   a --template clone keeps no remote, copies no object, and carries the builder's config
ok   and build_fixture --template says once that it built the template
ok   one builder and one input set give one key twice
ok   two builders of one name but two definitions never share a key
ok   one byte of one input file moves the key
ok   two build_fixture --template batches of one builder with two arguments each grade their own value
ok   two direct resolve_template calls of one key with arguments x and y print two templates, each its own value
ok   and a call with no argument still prints <root>/<key>/repo
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
ok   an exported GIT_DIR keeps the scratch repository's HEAD and its origin remote unmoved
ok   and the clone holds the builder's tree and no remote
ok   and the key equals the key derived with GIT_DIR unset
ok   both racers built, so the arm below grades a real collision
ok   two racing builds leave one key directory, and no stage beside it or inside it
ok   and both racers get the same template
ok   the cache root is the named directory, else the owned gate-work, else SELFTEST_ROOT
ok   eight clones of one template spend fewer git processes than eight builds (32 against 48)
ok   a reading arm that writes FAILs the suite, naming the arm and the read checkout
nope a clean reader exited 1 — template: 103098df reused
ok    a mutating arm
ok    a reader
FAIL  a reading arm wrote into the read checkout /tmp/gate-work.U2uJ4tRR/tmp/tmp.zeqhWdW3DD/read — a reader: hint: Support for <GIT_DIR>/info/grafts is deprecated hint: and will be removed in a future Git version. hint: hint: Please use "git replace --convert-graft-file" hint: to convert the grafts into replace refs. hint: hint: Turn this message off by running hint: "git config set advice.graftFileDeprecated false"
----
FAIL (1 of 2 arms, width 1)
ok   the arm lines are identical under shared and per-case, the same arm red in both
ok   per-case builds no template and runs a reading arm in its own copy, as arm does

FAILED (lib-selftest, 38 assertions)
```
