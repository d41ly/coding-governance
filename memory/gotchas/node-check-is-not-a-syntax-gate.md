---
name: node-check-is-not-a-syntax-gate
description: node --check exits 0 on a file whose parse fails, because module auto-detection retries the parse and swallows the failure, so a gate built on it cannot go red
kind: class
---

# `node --check` is not a syntax gate on node v24

## Symptom

A gate runs `node --check <file>` over the workflow scripts and reports green. A script with a
genuine parse error — `export const x=1` followed by `let y=(` — exits 0 with no output. Module
auto-detection retries the parse in the other dialect and swallows the failure, so the command is
a gate that cannot go red.

## Where it bit

Written into a unit's acceptance criteria as the syntax gate and caught by RUNNING it during the
round-1 review of the unit that shipped `tools/workflows/check-workflow-syntax.js`; that file's
header carries the measurement. A workflow script is neither CommonJS nor an ES module — it uses
`export const meta`, top-level `await` and top-level `return` together — so no standard parser
mode accepts it, and the auto-detecting one hides that.

## The fix

Parse in the dialect the RUNTIME evaluates: strip the leading `export`, hand the source to the
`AsyncFunction` constructor with the runtime's hooks as parameters, and treat a `SyntaxError` from
construction as the verdict. Constructing does not execute. The population is every file exporting
`meta`, derived from the marker rather than a path list, so a new script under `tools/workflows/`
is covered the day it lands.

Gated by the `workflow script syntax` leg, which is `tools/workflows/check-workflow-syntax.js`
itself; the failing case was observed before it landed, which is what the header's example is.
