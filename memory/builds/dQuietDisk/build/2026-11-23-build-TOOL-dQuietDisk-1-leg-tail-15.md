# TOOL-dQuietDisk-1 leg-tail 15 — python resolver (behaviour + inline parity + idiom ban) failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** python resolver (behaviour + inline parity + idiom ban)
- **Hash:** 1245927273e5b023e877c7fc2619cbfa170dc926
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
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
FAIL a governance ref writer skips the change feed: tools/push-main.sh@3a5bf825:1768
FAIL the census passed a planted writer that never appends to the feed: /tmp/gate-work.U2uJ4tRR/tmp/tmp.XX0O0qakFU/feed-writers/plant.sh line 2 | tools/push-main.sh@3a5bf825:1768
FAIL the census passed a plain push of a governance ref beside an append: tools/push-main.sh@3a5bf825:1768 | /tmp/gate-work.U2uJ4tRR/tmp/tmp.XX0O0qakFU/feed-writers/plain.sh line 3
FAIL the census read a pusher through a declared helper as a hit: tools/push-main.sh@3a5bf825:1768
FAIL the census passed a pusher through a helper the list does not name: /tmp/gate-work.U2uJ4tRR/tmp/tmp.XX0O0qakFU/feed-writers/helper.sh line 5 | tools/push-main.sh@3a5bf825:1768
FAIL the census passed a stale helper entry: FEED_WRITER_HELPER_FNS names no_such_fn(), which is no function of the files read | tools/push-main.sh@3a5bf825:1768
FAIL a python launcher is invoked without being resolved:
    .githooks/pre-push.test.sh@f5dd3019:1863:  _p=$(python "$KIT_REL/$PK/policy.py" get verdict.blocks --rev HEAD 2>/dev/null) || _p=every-red
    tools/check-spec-tokens.test.sh@2ef2c9a3:1236:  'cd t && python over.py --selftest'
    tools/check-spec-tokens.test.sh@2ef2c9a3:1239:  'x=$(python t/over.py --selftest)'
    tools/check-spec-tokens.test.sh@2ef2c9a3:1240:  '(cd t && python over.py --selftest)'
    tools/check-spec-tokens.test.sh@2ef2c9a3:1241:  '`python t/over.py --selftest`'
    tools/check-spec-tokens.test.sh@2ef2c9a3:1299:sed -i 's|`'"${PFX}gate-legs.json"'` exists|`python '"${PFX}x/slow.py"' --selftest` answers|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
    tools/unattended/gate-guard.test.sh@4f45a9d0:813:M_FLAG='python3 '"${PFX}"'zz-kit/planted_suite.py --selftest'
    tools/unattended/gate-guard.test.sh@4f45a9d0:814:M_FIX='python '"${PFX}"'zz-kit/planted_cases.py --fixture'
    tools/unattended/gate-guard.test.sh@4f45a9d0:836:run_planted "D6 the leg by its file name after a cd -> deny"              2 "$B" "cd ${PFX}zz-kit && python3 planted_suite.py --selftest"
    tools/unattended/unattended.test.sh@d825755e:17128:_w=$( cd "$_ih_top" && python "$HERE/../$IH_PK/policy.py" get verdict.blocks --rev HEAD 2>/dev/null ); _w=${_w%$'\r'}
    tools/workflows/unattended-build.test.sh@7d95ece0:3991:has    "DL20 AC7 the prompt runs the class count under the left-shift value" "$p" "RUN \`python ${PFX}${KIT}/review_dispose.py classes --builds memory/builds --record r.md --left-shift second-occurrence\`"
FAIL a {prefix} token is resolved by hand outside a marked block:
    tools/loop/stage_coverage.py@5a7404bf:112:        hooks[str(row.get("key")).replace("{prefix}/", parts["prefix"])] = row.get("stage")
    tools/loop/stage_coverage.py@5a7404bf:161:                              if str(r.get("key")).replace("{prefix}/", parts["prefix"]) != first]
    tools/playbook/core.py@61f36dc9:353:    words = shlex.split(command.replace("{prefix}", prefix))
    tools/playbook/core.py@61f36dc9:467:    glob = row.get("population", "").replace("{prefix}", prefix)
    tools/playbook/core.py@61f36dc9:505:        rel = row.get("population", "").replace("{prefix}", prefix)
    tools/playbook/core.py@61f36dc9:613:            home = row.get("population", "").replace("{prefix}", prefix).split("/*")[0].lstrip("*")
    tools/playbook/core.py@61f36dc9:619:            rel = row.get("population", "").replace("{prefix}", prefix)
    tools/playbook/core.py@61f36dc9:625:    words = shlex.split(row["factory"].replace("{prefix}", prefix))
    tools/playbook/render_playbook.py@60901555:3783:    path = (root / path_s.replace('{prefix}', load_units_module().derive_kit_prefix() or '.')).resolve()
    tools/playbook/render_playbook.py@60901555:3825:        usage = str(row['usage']).replace('{prefix}/', '<prefix>/')
    tools/run-gates/py_reads.py@19b62888:212:        argv, guard = leg.get("argv") or [], [g.replace("{prefix}", prefix) for g in leg.get("guard") or []]
    tools/run-gates/py_reads.py@19b62888:216:        entry = root / word.replace("{prefix}", prefix)
```
