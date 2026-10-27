# TOOL-dRankedPlan-60 — a JavaScript argv element naming a same-file binding resolves to that binding's strings

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 22 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-60-deviation-601.md](../build/2026-10-27-build-TOOL-dRankedPlan-60-deviation-601.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 31 at HIGH**, item **H7**. `TOOL-dRankedPlan-48` S3 has an array element name `ratify.py` only
through its own `str` tokens. A script path bound by `const s = path.join(kit, "ratify.py")` reaches the
array as a `word` token and never matches, so `spawnSync(py, [s, slug])` passes the deny-by-default ban,
and unit 48 §3 names only template literals as unread. `TOOL-dRankedPlan-49` adds the shell twin of
`TOOL-dRankedPlan-45` S3's bound-name rule, and no spec gives the JavaScript one. The tree's JS hooks
pass scripts exactly this way. This unit adds it. It repairs `TOOL-dRankedPlan-48`, so it sits one
order above it.

## 2. Scope (IN)

- **S1** — The JavaScript bindings. `read_js_callers` collects, over the `scan_ts_tokens(text,
  strs=True)` stream of `TOOL-dRankedPlan-48` S1, each declaration `const NAME =`, `let NAME =` or `var
  NAME =`: a `word` token `const`, `let` or `var`, a `word` token for the name, and an `=` op. The
  binding's tokens run from that `=` to the first `;` op at bracket depth 0 or to the last token on the
  declaration's line at depth 0, whichever comes first. Observed by AC1 and AC2.
- **S2** — The resolution. An array element of `TOOL-dRankedPlan-48` S3 that is a single `word` token
  names `ratify.py` when any declaration of that name anywhere in the file has a binding holding a
  `str` token ending in `ratify.py`. One such declaration is enough, so declarations that disagree fail
  closed, as `TOOL-dRankedPlan-49` S2 reads shell. Unit 48 S3's mode-flag rule applies to the array
  unchanged. Observed by AC1 and AC2.
- **S3** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-js-bound` plants a `.js` file holding `const s = path.join(kit, "ratify.py");` and then
    `spawnSync(py, [s, slug]);`. It is refused.
  - `caller-js-bound-exit` plants the same with `"--exit"` as the array's last element. It is admitted.

## 3. Non-goals (OUT)

- A plain re-assignment `s = …` outside a declaration, a member such as `opts.script`, and a binding in
  another module. Each is unread, the reader's ceiling, named in §4's table.
- A template literal binding: unread, as `TOOL-dRankedPlan-48` §3 states.
- Scoping a binding to its block. The file-wide reading fails closed.

### Edges

- **consumes-from** `TOOL-dRankedPlan-48` — S1's `str` tokens and S3's array elements, over which S1 collects the bindings and S2 resolves an element; without them there is no string text to compare

## 4. Design

### Evidence

- `tools/policy/policy-mirror.js:48` reads `const SHIM = path.join(__dirname, "policy-shim.sh")…`, and
  :85 reads `spawnSync(bash, [SHIM, ...args], …)`. `tools/unattended/stop-guard.js:108` reads `const
  driver = path.join(kitDir, 'unattended.sh')…`, and :111 reads `spawnSync('bash', [driver,
  '--liveness', slug],`.
- `scan_ts_tokens('const s = path.join(kit, "ratify.py");\nspawnSync(py, [s, slug]);\n')`, run
  2026-10-27 at base 0689e7fa from `tools/lexicon/lexicon.py`, printed `('word','const',1)
  ('word','s',1) ('op','=',1) ('word','path',1) ('word','join',1) ('op','(',1) ('word','kit',1)
  ('op',',',1) ('op',')',1) ('op',';',1)` for the first line, and `('word','s',2)` as the array's first
  element. The output is PINNED.
- No tracked `*.js` file invokes a kit's Python script at base (`TOOL-dRankedPlan-32` S3).

### The reading after this unit

| JavaScript | Element | Answer |
|---|---|---|
| `const s = path.join(kit, "ratify.py");` then `[s, slug]` | `s`, bound to a `ratify.py` string | caller |
| the same with `"--exit"` last | the same | not a caller |
| `let s; s = path.join(kit, "ratify.py");` then `[s, slug]` | `s`, never declared with a value | unread, the ceiling |
| `[opts.script, slug]` | a member | unread, the ceiling |

The upgrade is a plain assignment read as a binding, once the tree writes one before a kit-script call.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound`, `caller-js-bound-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 22. Units 52, 55, 57, 58 and 60 share order 22 and all write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Name the bound-name form as unread.** It is how the tree's JS hooks pass a script, so the ban would
  certify an absence over the shape the next JS caller copies.
- **Parse JavaScript with a real parser.** It is a new external dependency, which BUILD-METHOD M3's
  veto 2 refuses, and the tokenizer already in the block reads every token S1 needs.

## 5. Production-readiness checklist

- security — narrows: a JS argv array naming `ratify.py` through a declared name is refused.
- perf / scale — one pass over each `*.js` file's tokens for its declarations.
- error / empty / loading states — an element naming no declared binding is read as
  `TOOL-dRankedPlan-48` S3 reads it.
- observability — the refusal names the file and the array's first line.
- risks — a name declared twice for unrelated paths is refused when one names `ratify.py`, which fails
  closed.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound` runs, the check exits 1 naming the
  planted `.js` file.
  Red when: an element bound by `const s = path.join(kit, "ratify.py")` passes.
- **AC2** — When the plant `caller-js-bound-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a bound JS `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `caller-js-bound` and `caller-js-bound-exit`, staged by a reader that compares an element's own `str` tokens only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 31 (HIGH,
  item H7), repairing `TOOL-dRankedPlan-48`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-48`'s `read_js_callers` over `scan_ts_tokens(strs=True)`, and
the rule mirrored is `TOOL-dRankedPlan-49` S2's file-wide shell resolution. `python
tools/codebase-map/reuse_lookup.py "read a javascript const bound to a path and invoked in an argv
array"`, run 2026-10-27, ranked name stems only (`read`, `read_text`, `read_conf`), none of which reads a
JavaScript declaration, so no existing seam fits beyond unit 48's reader. The recall query returned
units 47 to 52 and dWitnessedBar's resolver scouts, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve bound variables wrappers and inline sources to a script invocation" --terms "assignment binding resolver substitution wrapper timeout here-string bash -c interpreter option caller ratify"`
