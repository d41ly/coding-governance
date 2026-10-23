# TOOL-dGroundRules-30 — the writer-marker floor decided by the installed hook's own verdict, never by a kit version the lander has not minted

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-30-deviation-18.md](../build/2026-10-23-build-TOOL-dGroundRules-30-deviation-18.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 18 at HIGH**, item **H3**, which no other id shares. This unit is
id 18's promotion. It repairs `TOOL-dGroundRules-25`, which sits at order 8, so it builds at order 9.

`TOOL-dGroundRules-25` S18 renders the spec-writer split under `gov:fixed-writers` only for a hook at
or above "the version `TOOL-dGroundRules-18` ships", read at build. Kit versions are minted at the
landing and never on a branch, so at build the hook still reads `1.40`, the version of every adopter
hook that predates the writer marker: a floor read then admits those hooks, and their rule 2 denies
every `unattended-build` call. A floor guessed ahead cannot hold on the branch. This unit decides the
floor by feature: the render asks the installed hook to judge the writer split it is about to write,
and falls back when the hook does not admit it.

## 2. Scope (IN)

- **S1** — The verdict. In the render of `tools/workflows/check-protocol-parity.test.sh`, the
  candidate `unattended-build.js`, with its spec-writer split under `// gov:fixed-writers` as
  `TOOL-dGroundRules-18` S3 renders it, is written under the render's temporary directory and judged
  by `bash "$HERE/check-verifier-fanout.sh" <that file>`, which hands it to the resolved agent-cap
  hook. Exit 0 keeps the writer render. Any other exit renders the fallback `TOOL-dGroundRules-25`
  S18 states, the split under `// gov:fixed-verifiers` with `Math.min(`, and prints one stderr line
  naming the hook's first output line and `govkit update --kits agent-cap`. Observed by AC1, AC2.
- **S2** — No version is read. The render reads no `KIT_AGENT_CAP_VERSION` and carries no version
  floor for the writer marker. Observed by AC3.
- **S3** — The fallback is judged too. The fallback render goes through the same probe; a hook that
  denies it as well makes the render exit 2 naming the hook's answer and write nothing, as the render
  already exits 2 on a hook that will not answer `--print-cap`. Observed by AC4.

## 3. Non-goals (OUT)

- `WRITER_MARK`, the writer bound and the template's marker: `TOOL-dGroundRules-18`.
- The fallback's own shape and its stderr wording beyond S1: `TOOL-dGroundRules-25` S18.
- A version mint for the floor through a `[[regenerate]]` row (§8 F1).
- A new flag on `agent-cap.js`. The hook is asked through the probe its kit already ships.

### Edges

- **consumes-from** `TOOL-dGroundRules-25` — the render's writer-marker floor and its fallback (S18), whose deciding predicate this unit replaces
- **consumes-from** `TOOL-dGroundRules-18` — `WRITER_MARK`, the writer bound rule 2 judges and the template's `gov:fixed-writers` split, which the probe asks the hook to admit

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `tools/hooks/agent-cap.js:104` is `const KIT_AGENT_CAP_VERSION = '1.40'`.
- `tools/push-main.sh:26-31`: kit versions are minted by the landing, "a branch therefore owes no
  bump".
- `tools/workflows/check-protocol-parity.test.sh:324` pins the playbook-render floor `(1, 11)`,
  chosen after that version was minted; `:529-545` take the fan-out cap from the hook's own answer,
  "never parsed here", and exit 2 when the hook will not answer.
- `tools/workflows/check-verifier-fanout.sh:163-166` judges the files it is named, and `:196-213`
  feeds each to `node "$HOOK" --only=scripts`, the predicate the `PreToolUse` hook applies; `:139`
  resolves the hook through the inlined `resolve_kit_dir`.

### The render after this unit

```text
cand = render(unattended-build.template.js, writer split under gov:fixed-writers)
if probe(cand) == 0:                      # bash $HERE/check-verifier-fanout.sh <tmp>/cand.js
    out = cand
else:
    out = render(..., split under gov:fixed-verifiers, Math.min as TOOL-dGroundRules-25 S18)
    stderr "the agent-cap hook does not admit the writer split: <its first line>. " \
           "Update it: govkit update --kits agent-cap"
    if probe(out) != 0: exit 2 naming the hook's answer
```

The probe runs in both modes, `--check` and `--render`, because both compare against the same render.

### Inventory

No identifier is minted; the probe is a call to an existing gate in the same kit.

### Files touched (estimate)

- `tools/workflows/check-protocol-parity.test.sh`

### Alternatives rejected

- **Read the hook's source for a `WRITER_MARK` definition.** It answers whether the constant exists,
  not whether the hook admits this split under this checkout's limit, and the render's own rule is
  that the hook answers and the render does not parse it.
- **A version floor.** No value is both true on the branch and safe for skewed adopters.

## 5. Production-readiness checklist

- security — the probe runs the hook already installed beside the kit, on a file the render wrote
  under its temporary directory; nothing new is executed.
- perf / scale — one `node` run per render, beside the one `--print-cap` already costs.
- error / empty / loading states — a denied writer split falls back with one stderr line; a denied
  fallback exits 2 and writes nothing, never a harness the hook would deny.
- observability — the stderr line carries the hook's own first line and the update command.
- risks — a hook that denies the writer split for its bound rather than its version also falls back,
  which is the safe reading: the bounded verifier split runs under every hook.
- testing — the render in a scratch clone, AC1 to AC4.
- migration — none.
- user docs — N/A: the stderr line is the user-facing text, and the hooks README's rule-2 paragraph
  is `TOOL-dGroundRules-25`'s.

## 6. Acceptance criteria

Every command runs from the repository root of the clone it names.

- **AC1** — When the workflows kit's `--render` mode runs in a scratch clone of the built tree whose
  `agent-cap.js` has the marker its `WRITER_MARK` constant names staged to another string, the rendered
  `unattended-build.js` carries `gov:fixed-verifiers` and `Math.min(` on the spec-writer split, and
  stderr names `govkit update --kits agent-cap`.
  Red when: a hook that does not admit the writer split is handed it.
- **AC2** — When the same mode runs in an unchanged clone of the built tree, the rendered
  `unattended-build.js` carries `gov:fixed-writers` on the spec-writer split and stderr holds no
  `govkit update --kits agent-cap` line.
  Red when: a hook that admits the split is handed the fallback, the floor guessed ahead of it.
- **AC3** — When `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh`
  runs, it prints `0`.
  Red when: the render keys the marker on a version the lander has not minted.
- **AC4** — When the clone's `agent-cap.js` is staged to deny every script and the `--render` mode
  runs, it exits 2 naming the hook's answer and leaves `unattended-build.js` unchanged.
  Red when: the render writes a harness its own hook denies.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `agent-cap self-test` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/workflows/check-protocol-parity.test.sh · covers AC1 AC4 · the hook's writer marker staged to another string in a scratch clone, then a hook staged to deny every script · none

## 8. Open questions

- **F1 — How does the render decide that a hook admits the writer split?** (a) The hook's own
  verdict on the candidate render, through `check-verifier-fanout.sh`. (b) A grep of the hook's
  source for a `WRITER_MARK` definition. (c) A version floor the mint writes through a
  `[[regenerate]]` row run after `govkit.py mint`. (c) is unsatisfiable on the branch, where nothing
  is minted, so AC2 cannot hold before the landing (veto 1). (b) meets AC1 to AC3 and admits a hook
  that defines the marker yet denies the split for its bound, so the harness it writes is denied,
  which fails AC4 (veto 1). (a) meets every criterion. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 18 (HIGH, item H3) of the round-1 spec
  audit of units 22 to 25, from the review's sound fix, feature detection, taken through the hook's
  own verdict, with the hook, the lander's mint note and both workflows gates read at base `3708a705`.

## 10. Reuse audit

The seams extended are the render's own rule that the hook answers and the render does not parse it
(`tools/workflows/check-protocol-parity.test.sh:529-545`), and `check-verifier-fanout.sh`'s
explicit-file mode, the kit's one way to ask the hook to judge a script.
`python tools/codebase-map/reuse_lookup.py "an adopter step that defers a render until the install is committed"`
ranked `render` in this same file among its seams, and the playbook-render floor at `:324` is the
version-floor precedent this unit declines, because that floor was set after its version was minted.
The recall probe returned this audit's H3 and the round-2 finding that `tools/workflows/kit.toml`
requires `agent-cap` with no version while the memory-tree kit keeps its playbook-render floor in a
render because govkit cannot express one; both agree with source and with this design. It also
returned `TOOL-aBoundedCeiling-13`, a carried-forward ceiling key on gate legs, which does not bear
on the floor.

Recall terms used: `python tools/memory-recall/query.py "how does a render floor an older adopter hook
by feature detection rather than version" --terms "agent-cap KIT_AGENT_CAP_VERSION floor WRITER_MARK
mint landing version render fallback playbook-render"`
