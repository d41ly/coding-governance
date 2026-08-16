# TOOL-aMouldedFolio-3 — the three follow-up units: control transcripts and AC evidence

**Serves:** journal TOOL-aMouldedFolio-3

*2026-08-16 · node a · the build record for units 3, 4 and 5, landed across `1edceeb`, `de4611c`,
`4981193`, `826b133` and the post-review fix pass.*

*Written because three acceptance criteria — unit 4's AC3 and AC6, unit 5's AC7 — require their
negative controls to be "recorded in the build report", and no build report existed. A commit
message is not retrievable from the corpus; a reviewer grading those ACs had nothing to read.*

---

## 0 · Why this record is mostly about controls

Every substantive defect in this build was found by a control failing, and **five separate times a
control was itself broken and read as a pass.** That is the finding worth carrying forward, so the
transcripts below lead with the controls rather than the features.

The rule that fell out of it: **an arm is worth nothing until its control has failed it**, and the
control must be shown to have applied — a `sed` that silently matched nothing, or a mutation that
broke the module outright, is not a control.

## 1 · Controls that were themselves broken

| # | The control | What it actually proved | How it was caught |
|---|---|---|---|
| 1 | `sed` reverting the Python marker predicate | nothing — the pattern never matched, 0 failures reported | re-ran targeting the line by index and got 4 failures |
| 2 | a Python patch reverting `rstrip` | only that a crashed import fails — it hit the wrong `rstrip` line and broke the module | module-imports check added before trusting the result |
| 3 | AC7/AC8 of unit 3, run against the live corpus | nothing — the corpus was already migrated, so disabling the remover changed no bytes | moved both to fixtures that build their own tree |
| 4 | both dot arms | nothing — `md`. The table below is` CONTAINS `The table below is`, so they passed over the corruption they were written to catch | negative control against `[^.]*`; arm now asserts the exact surviving line |
| 5 | the CR-tolerance assertion | nothing — a per-FILE `grep -c >= 1` is satisfied by a sibling reader in the same file | deleting one reader's strip left it green; assertion rebound per reader |

## 2 · Unit 4 — AC3 and AC6 transcripts

**AC3 — the conformance test fails when the Python reader is reverted to `.strip()`.**

Two invalid attempts preceded the valid one, and both are recorded because each looked like evidence:

```
attempt 1  sed 's|return line.rstrip("\r") == mark|return line.strip() == mark|'
           -> marker-contract: PASS, 0 failures      # the sed matched nothing
attempt 2  replace the first line containing "rstrip"
           -> 4 failures, but python printed ""      # wrong line; module no longer imported
attempt 3  replace the line containing "== mark", by index
           -> module imports OK
           -> FAIL [trailing space]    python said accept, contract says refuse
              FAIL [trailing tab]      python said accept, contract says refuse
              FAIL [close trailing ws] python said accept, contract says refuse
              FAIL [indented open]     python said accept, contract says refuse
```

**AC6 — the test binds the SHIPPED readers.** A revert control is unavailable for the awk side
because the unit leaves those readers unchanged, so each got a MUTATION control instead — deleting
the `if (ln != o) bad = 1` guard from its shipped bytes:

```
unattended.sh        -> 6 failures
check-unattended.sh  -> 3 failures
bad slice offsets    -> marker-contract: reader 'r_check' was not sliced …, exit 2
```

That last one is the post-review hardening: before it, a slice that failed to define its function
left the reader silently undefined and every nonzero exit mapped to `refuse`, so a reader that could
not run at all was indistinguishable from one correctly rejecting a document.

## 3 · Unit 5 — AC7 transcripts

Four fence arms, and the first control covered only three of them:

```
revert the fence reader to the private boolean toggle
  -> arm FAIL  a ~~~ fence is a fence
     arm FAIL  an unterminated fence REDS instead of silently hiding the rest
     arm FAIL  the unterminated fence names the line it opened on
     (the nested-fence arm PASSED — that toggle never recognises ~~~ at all, so it
      cannot discriminate; it needed its own control)

recognise ~~~ but toggle on ANY marker
  -> arm FAIL  a ``` marker inside a ~~~ block is content, not a toggle
```

An arm proven against the wrong reversion is not proven. The post-review pass added the terminal
refusal and its control:

```
remove the terminal refusal from the open-fence branch
  -> arm FAIL  an open fence stops --check before any pin comparison
```

That fixture is the danger in miniature: a fence hiding the one duplicate a pin exists for, where
the non-terminal version emits `lower it to 0` — an instruction to unpin a real duplicate, derived
from a corpus the scanner could not finish reading.

## 4 · Unit 3 — the measured effect, and the mutant that used to survive

```
folder-claim disagreements   before 21   after 0
surviving prose (AC3)        "The table below is" intact in all 17 carriers
physical lines deleted (AC4) 0
idempotence (AC9)            two consecutive writes, zero changed bytes
```

The mutant that mattered: collapsing `if rest.strip(): … else: del lines[i]` to `lines[i] = rest`
passed the ENTIRE selftest while changing the render, because the arm asserted an occurrence count
the derived sentence satisfies on its own. It now asserts the rendered shape and the mutant reds.

## 5 · What the closing review found after all this

Its verify stage died on a usage limit, so 21 findings returned unverified. Re-run against landed
main: **14 confirmed, 7 fixed, 0 refuted.** Every one was real — the lenses were 21 for 21, and the
7 marked fixed were genuinely removed by the interim fix pass rather than mistaken.

The 14 confirmed are closed by the pass this record accompanies. Their shapes, for the next reader:
four were arms that could not fail, three were the same unarmed branch reached three ways, two were
refusals that were not terminal, two were records stating something the code had stopped doing, and
one was a cross-kit path spelled rather than derived.

## 6 · Still open

- The `unkeyed` assertion remains zero-tolerance with no waiver. Correct while the measured count is
  0; a registry over an empty population would be the vacuous-selector class.
- The five shell replicas of `_unfenced` keep the unterminated-fence defect this build closed for
  check 20. Named as a non-goal in unit 5's spec, not fixed.
- The intra-kit awk lift the marker contract defers: three readers in one kit could share a
  primitive, which the kit-independence argument does not forbid.
