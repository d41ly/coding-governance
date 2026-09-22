# TOOL-dUnstalledConvoy-28 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-28

The defect was a category error rather than a bug: `-26` rev-2 resolved "where does this repo set
`GATE_SELFTESTS`?" with `.githooks/pre-push`, and govkit ships that hook VERBATIM as engine payload
to every push-main adopter. The mechanism may travel; the choice may not.

`AC4` was already true when this unit started — the hook only ever READ the variable, never assigned
it — so what shipped here is the location plus the assertion that keeps it honest.

## The arms, and the break each one was observed against

| arm | red-first verdict |
|---|---|
| AC2 a bare assignment inside a kit's payload REDS | RED against `govkit.py` at `ee2c58de` |
| AC2 the refusal names the file and the kit that would ship it | RED, same |
| CONTROL the same assignment in a path no kit ships is GREEN | **passes without the mechanism** |
| an INVOCATION inside the payload is not a policy and stays GREEN | **passes without the mechanism** |

Both controls pass either way, and both are load-bearing anyway. The first stops the check being a
ban on the variable — the sanctioned shape is exactly a bare assignment, just somewhere else, and a
predicate that redded on it would leave nowhere to put the policy. The second stops it being red on
its own source: `GATE_SELFTESTS=1 bash …` is an INVOCATION, it appears 54 times across this tree in
docs, arms and refusal strings, and calling those policies would make the check permanently red.

## The real-tree observation, which is the one that matters

`export GATE_SELFTESTS=1` appended to `.githooks/pre-push`, selfcheck run, line restored:

```
govkit: '.githooks/pre-push' carries a bare GATE_SELFTESTS assignment AND is shipped by kit
'push-main' — a repo-local gate policy written into a file a kit copies is a policy every adopter
inherits without choosing it.
```

That is the exact configuration `-26` rev-2 prescribed, refused by name.

## The predicate, run over the real tree before it was wired

0 hits and 54 near-misses. Every near-miss is an invocation, a read (`${GATE_SELFTESTS:-}`), a
refusal string or a doc line. Records under the memory root and every `.md` are excluded from the
scan: a decision log quoting a policy line is not executing one.

## The defect the first draft shipped, and what caught it

The shipped set was derived from each file rule's `claims` key. Measured: **13 of 58** file rules in
this tree declare `claims` at all. The check therefore quantified over 20 paths and reported a
confident green over the other 157 — the could-not-fail shape arriving as an under-derived
population rather than as a wrong predicate, and the fixture arm would have passed regardless
because `tools/demo/` happens to declare `claims`.

Resolved by resolving each rule the way `apply` resolves it, including expanding `include = "**"`
against the entry's home exactly as check 7i does. 20 → 177 shipped paths.

## The cost this decision accepts, stated because nobody will find it later

Gov's push boundary now sets the switch, so `TOOL-dUnstalledConvoy-27`'s predicate 8 forces a FULL
run whenever the recorded green did not cover the self-tests. `GATE_FULL` ignores guards, so that
run executes all 42 kit-subject legs. Within the declared lag bound the following pushes are scoped
again, so the shape is roughly one self-test-covering full bar per build rather than per push —
which is the same bargain `GATE_FULL_MAX_LAG` was set to strike. Adopters pay none of it.
