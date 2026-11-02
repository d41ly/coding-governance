# dFoldedAudit — the first flagged bar on the branch, and its reds attributed

**Serves:** journal TOOL-dFoldedAudit-16

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at `bf773d490`, before the merge of `main`, 2026-11-02 07:02 to 08:05 UTC. Verdict: `gates RED — 9/144 legs failed (1 retried after timeout)`, rc 1.

## Attribution

| Leg | Reading | Evidence |
|---|---|---|
| shell hygiene (a fork spent on builtin work) | OWN | five registry rows measured above their counts, every one in a file this build changed |
| drift-audit records | OWN | `cutoff_keys_armed = 37 (pin 36)`: `SPEC_SUPERSEDE_CUTOFF`, TOOL-dFoldedAudit-4's key |
| spec-tokens self-test | INHERITED | the same two parity assertions fail at BASE `74274869` in a scratch clone |
| recall floor arms | INHERITED | `--audit-fixture` fails at BASE in the same clone |
| push-main self-test | HOST | every case printed ok; it timed out twice at its 580 s ceiling |
| measure-legs selftest | HOST | AC6, AC7 and AC15 are timing reads; the past run recorded this leg inherited |
| foreign-prefix parity | INHERITED by its contents | measure-legs again, and policy fixtures' probe marker |
| pre-push self-test | HOST | green at BASE and at HEAD `0e3c26cf9` in fresh clones; the worktree run read the lexicon kit's install location, not this build's code |
| govkit selftest | pending | OC8 and OC13 read `KIT_DIR derived empty — no .git above the kit`, a scratch-target read |

## Every leg line

    GATE ok    kickoff-manifest ratchet
    GATE ok    build README slot contract
    GATE ok    process-monitor wiring
    GATE ok    memory hygiene
    GATE ok    template size <=48KiB
    GATE ok    charter size
    GATE ok    micro-format definitions
    GATE ok    line length
    GATE ok    playbook parity
    GATE ok    build-method size
    GATE ok    unattended protocol size
    GATE ok    unattended skill size
    GATE ok    kickoff engine size <=18KiB
    GATE ok    shell hygiene (a loop fed by a command substitution)
    GATE ok    shell hygiene (a location probe asked from a moved directory)
    GATE FAIL  shell hygiene (a fork spent on builtin work)  (exit 1)
    GATE ok    shell hygiene (a fixed-name temp renamed into place)
    GATE ok    spawn budget (forks per hot entrypoint)
    GATE ok    encoding posture (text IO names its encoding)
    GATE ok    install-prefix (shipped surface)
    GATE ok    hook destinations (every declared hook path ships)
    GATE ok    agent-cap restatement
    GATE ok    playbook placeholder catalogue
    GATE ok    micro-format gate selftest
    GATE ok    line-length gate selftest
    GATE ok    playbook parity selftest
    GATE ok    template size gate selftest
    GATE ok    shell-hygiene selftest
    GATE ok    verdict-epoch self-test
    GATE ok    manifest-check self-test
    GATE ok    agent-cap self-test
    GATE ok    scratch-guard self-test
    GATE ok    format-guard self-test
    GATE ok    agent-instructions self-test
    GATE ok    memory-hygiene self-test
    GATE ok    row-keyed merge driver replay
    GATE ok    method-carriers self-test
    GATE ok    build-index selftest
    GATE ok    corpus-ids selftest
    GATE ok    gotchas selftest
    GATE ok    routed-commits selftest
    GATE ok    row-grammar selftest
    GATE ok    backlog migration selftest
    GATE ok    check-arms selftest
    GATE ok    branch-guard self-test
    GATE FAIL  pre-push self-test  (exit 1)
    GATE ok    pre-push run-log line
    GATE ok    pre-push bar self-test
    GATE retry  push-main self-test  (timed out after 580s beside 7 neighbours; retried in the pool's tail, and alone after it drains unless that passes)
    GATE ok    check-wiring self-test
    GATE ok    verifier fan-out self-test
    GATE ok    tier2-review self-test
    GATE ok    unattended-build self-test
    GATE ok    review-join self-test
    GATE ok    review-replay selftest
    GATE ok    pytest-guardrails self-test
    GATE ok    codebase-map kit selftest
    GATE ok    settings-merge selftest
    GATE ok    memory-recall kit selftest
    GATE FAIL  recall floor arms  (exit 1)
    GATE ok    drift-audit selftest
    GATE ok    process-monitor census selftest
    GATE ok    process-monitor adopter selftest
    GATE ok    runlog selftest
    GATE ok    branch-reconcile selftest
    GATE ok    run-gates canary
    GATE ok    run-gates evidence
    GATE ok    run-gates turnstile
    GATE ok    run-gates gov canary
    GATE FAIL  foreign-prefix parity (every self-test at three prefixes)  (exit 1)
    GATE ok    run-gates run-log line
    GATE ok    profile-bar selftest
    GATE ok    held-halves selftest
    GATE FAIL  measure-legs selftest  (exit 1)
    GATE ok    hook destinations self-test
    GATE ok    agent-cap restatement self-test
    GATE ok    install-prefix self-test
    GATE ok    dead-path carriers self-test
    GATE ok    remote literals self-test
    GATE FAIL  govkit selftest  (exit 1)
    GATE ok    lexicon selftest
    GATE ok    placeholder-catalogue self-test
    GATE ok    testsuite counts self-test
    GATE ok    playbook render selftest
    GATE ok    roles render selftest
    GATE ok    roles adopter self-test
    GATE ok    policy fixtures
    GATE FAIL  spec-tokens self-test  (exit 1)
    GATE ok    kit-placeholders self-test
    GATE ok    selftest harness self-test
    GATE ok    extract-arms self-test
    GATE ok    run-selftests self-test
    GATE ok    kit version markers
    GATE ok    verdict epoch (kit version dates the engine)
    GATE ok    row-driver view refusal
    GATE ok    kit/dogfood doc parity
    GATE ok    method carriers (every pointer declared)
    GATE ok    harness arms (fail branches armed or pinned)
    GATE ok    review-protocol parity (kit vs dogfood)
    GATE ok    review-join ban (no ref-keyed join)
    GATE ok    codebase-map gate coverage
    GATE ok    codebase-map coverage + freshness
    GATE ok    recall floor
    GATE ok    runlog record schema
    GATE FAIL  drift-audit records  (exit 1)
    GATE ok    unattended kit gate
    GATE ok    pass-order history
    GATE ok    routed commits name a specced unit
    GATE ok    brief-recorded
    GATE ok    playbook validity gate
    GATE ok    dead-path carriers (deleted files still named)
    GATE ok    remote literals (kit code names no remote)
    GATE ok    govkit selfcheck
    GATE ok    kit epoch (shipped bytes move, the version moves)
    GATE ok    lexicon naming predicates
    GATE ok    transition-audit arms
    GATE ok    straggler-guard arms
    GATE ok    marker contracts
    GATE ok    verifier fan-out
    GATE ok    govkit refusal join
    GATE ok    govkit runbook parity
    GATE ok    govkit acceptance matrix
    GATE ok    testsuite counts (every bar self-test prints one)
    GATE ok    spec tokens (a spec's own names resolve)
    GATE ok    kit placeholders (a declared token its adopter substitutes)
    GATE ok    roles catalogue
    GATE ok    policy check
    GATE ok    leg ceilings clear their evidenced maximum
    GATE ok    every held leg is budgeted, every budget row resolves
    GATE ok    receipt sync (installed files match the receipt)
    GATE ok    agent-instructions wiring
    GATE ok    python resolver (behaviour + inline parity + idiom ban)
    GATE ok    workflow script syntax
    GATE ok    memory-recall skill wiring
    GATE ok    drift-audit wiring
    GATE ok    runlog skill wiring
    GATE ok    cleanup skill wiring
    GATE ok    unattended skill wiring
    GATE ok    run-gates wiring
    GATE ok    lexicon wiring
    GATE ok    playbook render wiring
    GATE ok    roles render wiring
    GATE ok    codebase-map adopter e2e
    GATE ok    run-gates adopter e2e
    GATE FAIL  push-main self-test  (timed out after 580s, again on its serial retry; a spawn cost 1.2x this clone's floor, under the 4x HOST ratio)
