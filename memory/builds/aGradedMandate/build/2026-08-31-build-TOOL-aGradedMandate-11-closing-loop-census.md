# TOOL-aGradedMandate-11 — the closing-loop census, MEASURED

**Serves:** journal TOOL-aGradedMandate-1 TOOL-aGradedMandate-11

*Node `a`, 2026-08-31. This is the charter's own rule executed rather than invoked: **run a candidate
gate predicate over the real tree before wiring it, and print hits AND near-misses.**
`TOOL-aGradedMandate-1` AC7 invoked that rule and then answered it from memory, pinning three
expected hits. Round 2 of the spec audit executed the predicate and got twenty-one. This record is the
measurement, and AC7 now reads it instead of a number nobody re-ran.*

## The predicate

`TOOL-aGradedMandate-1` S1, exactly: the `review` rows in a run-state file whose ` · item ` subject
EQUALS the build slug; at least one must exist; and the LAST must carry a terminal token from
`CONVERGED` / `NON-CONVERGENT` / `CEILING`. The subject comparison is `!=` in awk, the same shape
`review_counts` uses at `tools/unattended/unattended.sh:3438`, so a spec-audit round keyed
`<slug>-specs` does not satisfy a join on the bare slug.

The bytes are here rather than described, so a later reader re-runs them instead of reconstructing
them from prose:

```bash
# TOOL-aGradedMandate-1 S1's predicate, run over every tracked RUN.md.
n=0; npass=0; nrefuse=0
for f in $(git ls-files 'memory/builds/*/RUN.md'); do
  n=$((n+1))
  slug=${f#memory/builds/}; slug=${slug%/RUN.md}
  phase=$(awk -F': ' '/^phase: /{sub(/\r$/,"",$2); print $2; exit}' "$f")
  case " LANDED ABORTED " in *" $phase "*) live="terminal" ;; *) live="NON-TERMINAL" ;; esac
  last=$(awk -v subj="$slug" '
    $0 ~ /^[0-9][0-9-]*T[0-9:]*Z review · item / {
      line=$0; sub(/\r$/,"",line)
      i=index(line," · item "); if(i==0) next
      rest=substr(line,i+length(" · item "))
      j=index(rest," · reason "); if(j==0) next
      if (substr(rest,1,j-1)!=subj) next
      last=substr(rest,j+length(" · reason "))
    } END { if(last!="") print last }' "$f")
  if [ -z "$last" ]; then
    verdict="REFUSE  no --review round whose subject is the bare slug"
    nrefuse=$((nrefuse+1))
  else
    case "$last" in
      *CONVERGED*|*NON-CONVERGENT*|*CEILING*)
        verdict="PASS    $last"; npass=$((npass+1)) ;;
      *) verdict="REFUSE  last round carries no terminal token: $last"; nrefuse=$((nrefuse+1)) ;;
    esac
  fi
  printf '%-26s %-12s %-12s %s\n' "$slug" "$phase" "$live" "$verdict"
done
echo "----"
echo "examined $n tracked RUN.md · pass $npass · refuse $nrefuse"
[ "$n" -gt 0 ] || echo "LIVENESS FAILURE: the selector matched NOTHING, so this is not a clean corpus, it is a broken probe"
```

## The result

```
aBoundedCeiling            LANDED       terminal     REFUSE  last round carries no terminal token: verdict BLOCKED · blockers 1
aBoundedVerdict            LANDED       terminal     PASS    verdict BLOCKED · blockers 3 · NON-CONVERGENT
aBranchedMandate           LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aDeclaredBound             LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aDeclaredCeiling           LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aFusedCharter              LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aGradedMandate             BUILDING     NON-TERMINAL REFUSE  no --review round whose subject is the bare slug
aGroundedOrientation       LANDED       terminal     PASS    verdict CLEAN WITH FIXES · blockers 0 · CONVERGED
aLexedStripper             LANDED       terminal     PASS    verdict BLOCKED · blockers 2 · NON-CONVERGENT
aMeteredTurnstile          ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
aPacedTurnstile            LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aPrimedKeepalive           LANDED       terminal     REFUSE  last round carries no terminal token: verdict BLOCKED · blockers 2
aPromptedMandate           LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aScannedThrottle           LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aScouredKit                LANDED       terminal     PASS    verdict BLOCKED · blockers 4 · NON-CONVERGENT
aSealedCaravan             LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aSiftedPlaybook            LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
aThawedCorpus              LANDING      NON-TERMINAL REFUSE  no --review round whose subject is the bare slug
aWalkedCorpus              ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
cBriefedPilot              ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
dCarriedReceipt            LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
dClosedLexicon             ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
dFramedEntrypoint          LANDED       terminal     PASS    verdict BLOCKED · blockers 0 · CONVERGED
dPromptedSeam              LANDED       terminal     PASS    verdict BLOCKED · blockers 2 · NON-CONVERGENT
dScaffoldedMirror          LANDED       terminal     PASS    verdict BLOCKED · blockers 0 · CONVERGED
dScriptedRepeat            ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
dTieredTribunal            ABORTED      terminal     REFUSE  no --review round whose subject is the bare slug
dUnstalledConvoy           LANDED       terminal     REFUSE  no --review round whose subject is the bare slug
----
examined 28 tracked RUN.md · pass 7 · refuse 21
```

## Reading it

**Twenty-one of twenty-eight refuse, and nineteen of those carry no bare-slug review row at all.**
That is not a corpus of abandoned reviews. It is a corpus that predates the convention: `--review`
landed recently, and most tracked records key their rounds on a unit id or a suffixed handle rather
than on the slug. `dCarriedReceipt` carries nineteen review rows and refuses; `dTieredTribunal` and
`dUnstalledConvoy` carry several and refuse. The predicate is measuring adoption, not misconduct.

**A refusal on a TERMINAL record costs nothing, and that is the whole argument
`TOOL-aGradedMandate-1` §4 is making.** `--close` is the only reader of this term, no verb re-closes
a record at `LANDED` or `ABORTED`, and `--preflight` ROTATES a finished record rather than reopening
it. Nineteen of the twenty-one refusers are terminal and are not rewritten, because rewriting a
finished record is what the protocol forbids.

**TWO refusers are NON-TERMINAL, and each is owed an answer rather than a shrug.**

- `memory/builds/aGradedMandate/RUN.md`, phase `BUILDING` — this run's own. Its review rows are keyed
  `aGradedMandate-specs` and `aGradedMandate-promoted`, which are spec-audit subjects and correctly do
  not satisfy a closing-review term. `TOOL-aGradedMandate-1` AC8 is the answer: this build's CLOSING
  diff review records its rounds under the bare slug, so the record satisfies S1 before `--close`
  evaluates it. If it does not, this unit's own item blocks its own close, which is the correct
  behaviour and not an exemption.
- `memory/builds/aThawedCorpus/RUN.md`, phase `LANDING` — another build's, with `--close` already run
  and its `gates-green` override already recorded. Nothing re-evaluates it: `LANDING` is written by
  `--close` and only `--landed` or `--abort` moves it on. Its disposition is therefore the same as a
  terminal record's, reached by a different route, and it is named here rather than counted silently.

**Two records refuse on the TERMINAL-TOKEN arm rather than the no-row arm**, and they are the finding
the whole unit exists for: `aBoundedCeiling` ends `BLOCKED · blockers 1` and `aPrimedKeepalive` ends
`BLOCKED · blockers 2`, both at `LANDED`, both with `closing-review-recorded` MET at the time. A
closing loop stopped mid-convergence with blockers standing, and the Definition of Done said yes.

## Liveness

The probe examined **28** tracked `RUN.md` and refused **21**. It prints a `LIVENESS FAILURE` line
when its selector matches nothing, because a probe that cannot move reporting a clean corpus is
indistinguishable from a clean corpus. It did not print one.

**This is dated evidence, not a live query.** The census moves as records land, and a later reader
re-runs the block above rather than trusting these counts. That is the same status every measurement
in this repo's build records carries.
