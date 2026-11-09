<!-- gov:rendered from tools/playbook/references.toml doc.reference.drive; edit the registry, not this page -->
# Drive

## `drive.start.main`
<!-- usage: drive:drive.start.main 5be231e5 -->
a new task from the owner; a resumed or compacted session, which re-reads its card before it acts; another harness without gov's hooks, which writes no card, so the kickoff runs by hand; a build is requested: it runs unattended by default, its committed README at BASE being the mandate; only when the owner asks to attend a build

```text
/session-kickoff
/unattended <slug>
/build
```

## `drive.start.gov-session`
<!-- usage: drive:drive.start.gov-session 1d79174e -->
a subagent's task, handed over as a prompt file

```text
python <prefix>/roles/handoff.py check <file>
```

## `drive.bookkeeping.main`
<!-- usage: drive:drive.bookkeeping.main b3bdaf92 -->
a record, an index or the run state changed

```text
python <prefix>/memory-tree/gen_build_index.py --write
```

## `drive.research.gov-researcher`
<!-- usage: drive:drive.research.gov-researcher 73e64b8b -->
a design choosing between candidates no seam decides

```text
python <prefix>/memory-recall/query.py "<question>" --terms "<8-14 words>"
```

## `drive.handoff.gov-session`
<!-- usage: drive:drive.handoff.gov-session e58717d2 -->
work leaving this session for another

```text
python <prefix>/roles/handoff.py render --role <role> --build <slug>
```

## `drive.orient.gov-orienter`
<!-- usage: drive:drive.orient.gov-orienter 23129e9e -->
once per session, before the first unit opens

```text
/session-kickoff
```

## `drive.reuse.gov-reuse-scout`
<!-- usage: drive:drive.reuse.gov-reuse-scout a2de08b3 -->
a new behaviour about to be designed

```text
python <prefix>/codebase-map/reuse_lookup.py "<behaviour>"
```

## `drive.spec-write.gov-spec-writer`
<!-- usage: drive:drive.spec-write.gov-spec-writer a5fa7dbf -->
a build whose units lack a spec or hold a thin one

```text
Workflow <prefix>/workflows/unattended-build.js
```

## `drive.spec-review.gov-spec-reviewer`
<!-- usage: drive:drive.spec-review.gov-spec-reviewer 0f65719a -->
a spec audit the build or its project declares

```text
Workflow <prefix>/workflows/tier2-review.js
```

## `drive.spec-review.gov-skeptic`
<!-- usage: drive:drive.spec-review.gov-skeptic 747de422 -->
a finding handed on to refute

```text
Workflow <prefix>/workflows/tier2-review.js
```

## `drive.build.gov-builder`
<!-- usage: drive:drive.build.gov-builder ed424782 -->
a unit whose spec is READY

```text
python <prefix>/roles/handoff.py render --role gov-builder --build <slug> --unit <id>
```

## `drive.closing-review.main`
<!-- usage: drive:drive.closing-review.main 89580cd5 -->
before any review, for the bug classes a diff can hit

```text
python <prefix>/memory-tree/gotchas.py --for-diff <base>..<head>
```

## `drive.closing-review.gov-diff-reviewer`
<!-- usage: drive:drive.closing-review.gov-diff-reviewer 48bb388b -->
the last unit terminal, over the cumulative diff

```text
Workflow <prefix>/workflows/tier2-review.js
```

## `drive.closing-review.gov-synthesizer`
<!-- usage: drive:drive.closing-review.gov-synthesizer 58df15ea -->
the verified findings, merged into one report

```text
Workflow <prefix>/workflows/tier2-review.js
```

## `drive.gate-bar.main`
<!-- usage: drive:drive.gate-bar.main e3f03708 -->
the close or the push boundary: the pre-push hook runs the full bar

```text
bash <prefix>/push-main.sh
```
