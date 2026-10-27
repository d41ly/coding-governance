# TOOL-dLinkedLibrary-83 — the CI census tests the `default:` line's own value for an indirection, in block or flow style

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 25 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-83-deviation-831.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-83-deviation-831.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
finding **id 32 at HIGH**, report item **H2**. No other id shares the item.

`TOOL-dLinkedLibrary-76` S1 runs `TOOL-dLinkedLibrary-71` S1's indirection test over `default:` "at any
depth below it", and every 76 S4 plant is block-style. The `default:` line's own value is outside that
scope: `default: *base`, `default: !reference [.defaults]`, and the flow mapping `default: {
before_script: !reference [.publish, script] }` that 76's own §1 gives as its motivating example.
`TOOL-dLinkedLibrary-63` S1 reads a key "as a scalar, a list of scalars, or a block scalar", never a flow
mapping. A builder walking the child lines of `default:` never sees an indirection written on the line
itself, so the §1 file leaves every plain job `importable` and no criterion goes red.

This unit makes the test read a line's whole value, flow collections included, on the `default:` line
and on every line below it, and plants §1's example. It repairs `TOOL-dLinkedLibrary-76` and builds one
step after it (order 25).

## 2. Scope (IN)

- **S1** — What is read. In `tools/memory-tree/adopt_program.py`'s `ci-job` class, 76 S1's test for a
  `!reference` tag, an alias `*<name>` or a merge key `<<:` reads the `default:` line's own value and every
  line below it, and on each line the whole value text: a block scalar's header line, a plain scalar,
  and a flow mapping `{ ... }` or flow sequence `[ ... ]` to its closing bracket, across lines where the
  flow collection continues. An anchor definition `&<name>` stays readable, as 76 S3 states. Observed by
  AC1 to AC4.
- **S2** — The reading. A hit refuses every job in the file as 76 S2 states, each reading `refused: opaque
  step <key> default:<child>`. `<child>` is the key that holds the token: a block key below `default:`
  as 76 S2 states; inside a flow mapping, the nearest key before the token at the token's own flow
  depth; and empty where the token is `default:`'s whole value, so `default: *base` reads `refused: opaque
  step alias default:`. Observed by AC1 to AC3.
- **S3** — What stays readable. A `default:` whose line value is a flow mapping holding none of S1's
  tokens, `{ image: node:20 }` say, or an anchor alone, `default: &defaults` over block lines with none,
  leaves its plain jobs graded as 63 S1 to S3 state. Observed by AC4.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of
  its own with two plain jobs, `test` running `npm test` before the `default:` block and `lint` running
  `npm run lint` after it: `default: *base` following a hidden `.base: &base` whose `script:` runs `npm
  publish`, the anchor first as YAML requires; `default: !reference [.defaults]` over a hidden `.defaults` running `npm publish`; the one-line
  flow mapping `default: { before_script: !reference [.publish, script] }` over a hidden `.publish`
  running `npm publish`; and `default: { image: node:20 }`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- GitLab's other top-level blocks that reach every job: `TOOL-dLinkedLibrary-84` (id 33), which applies
  this unit's reading to each of them.
- Resolving an alias, a `!reference` or a flow collection's values: the census stays a text reader, as
  63 §3 and 71 §3 keep it.
- The job-level keys: 71 S1, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-76` — S1's indirection test over `default:`, S2's file-wide refusal and S4's plant trees, which S1 and S2 extend to the `default:` line's own value and to flow style (id 32)
- **hands-off** `TOOL-dLinkedLibrary-84` — S1's whole-value reading of a block's own line and its flow collections, which unit 84 applies to every other top-level block that reaches every job (id 33)

## 4. Design

### Evidence

- 76 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-76.md:34-36`): "the job's own keys and the top-level
  `default:` map, at any depth below it".
- 76 §1 (`:24-25`) names `default: { before_script: !reference [.publish, script] }` as the bypass; 76 S4
  (`:44-48`) plants three block-style trees and no flow mapping.
- 63 S1 reads each key "as a scalar, a list of scalars, or a block scalar".

### A GitLab file after S1 and S2

```yaml
test:
  script: [npm test]          # S2: refused, opaque step !reference default:before_script
default: { before_script: !reference [.publish, script] }   # S1: the line's own flow value
.publish:
  script: [npm publish]
lint:
  script: [npm run lint]      # S2: refused, the same reading
```

### Rollout

Order 25 beside `TOOL-dLinkedLibrary-84` and `TOOL-dLinkedLibrary-85`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences them, and unit 84 consumes this unit's
reading, so this pass precedes 84's.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **A flow-collection parser.** 63 §3 and unit 8 §5 keep the census a text reader with no new
  dependency; a token search over the value text finds every indirection a parser would, and the census
  needs no value.
- **Refusing any flow-style `default:`.** It refuses `{ image: node:20 }`, which injects nothing; S4's last
  plant keeps that file's jobs `importable`.

## 5. Production-readiness checklist

- security — closes the import of a publish injected through an indirection on the `default:` line;
  deny by default.
- perf / scale — one more line's value read per file.
- error / empty / loading states — a flow collection left unclosed at the end of the file is read to the
  end, and a token in it refuses as any other.
- observability — each refusal names the key and the `default:` child holding it.
- risks — a token inside a quoted string on the `default:` line refuses the file; the owner may rule a
  job in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: 76 S5's sentence says an indirection under `default:` refuses every job,
  and the line's own value is under it.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both plain jobs
  of the tree holding `default: *base` read `refused: opaque step alias default:`.
  Red when: 76's below-the-line walk leaves an alias on the `default:` line unread.
- **AC2** — When the same plant runs, both plain jobs of the tree holding `default: !reference
  [.defaults]` read `refused: opaque step !reference default:`.
  Red when: a tag on the `default:` line passes.
- **AC3** — When the same plant runs, both plain jobs of the tree holding the one-line flow mapping read
  `refused: opaque step !reference default:before_script`.
  Red when: the flow mapping of 76's own §1 leaves a job `importable`.
- **AC4** — When the same plant runs, both plain jobs of the tree holding `default: { image: node:20 }`
  read `importable`.
  Red when: the whole-value read refuses a flow value that holds no indirection.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's four `default:`-line trees, the failing case staged by 76's below-the-line walk · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, id 32 (HIGH, item
  H2).

## 10. Reuse audit

The seam extended is 76 S1's indirection test, itself 71 S1's, inside `TOOL-dLinkedLibrary-8`'s `ci-job`
class in `tools/memory-tree/adopt_program.py`: the same test over one more line and its flow value.
`python tools/codebase-map/reuse_lookup.py "find a gitlab reference tag or alias on the default line itself
in flow style"` ranked `build_reference_index`, `check_line`, `render_line` and `parse_conf_line`, none a
YAML or CI reader, so no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse an indirection on the default line or a global gitlab block" --terms "census ci-job gitlab default flow alias reference merge-key global before_script variables refused"`
