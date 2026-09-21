# Build brief — DEPL-cMendedVintage-21

**Serves:** journal DEPL-cMendedVintage-21

Read the spec whole first. This unit exists because the build almost shipped a mitigation nobody
could observe, so read §1 carefully — it is an argument about your own predecessor, not background.

*Standing note: thirteen briefs in this build carried a figure or mechanism measurement disproved,
and every one of the last six units amended its own spec mid-build after measuring. Treat this as
evidence, not authority, and mark anything you did not run.*

## Your predecessor landed an hour ago and already wrote half of S1

`DEPL-cMendedVintage-13` shipped `write_gate_legs`, and the manifest write-back inside it is already
`write_text` to a sibling temp path followed by `os.replace`. It recorded AC6 as OWED and named this
unit as what closes it.

So your job is NOT to invent the atomicity. It is to make it ONE helper every adopter-bar write
routes through, and — the actual point — to give it an observer that goes red when it is absent.
Read what that unit landed before you write anything; if it already satisfies S1 in substance, say
so and lift it rather than writing a second one beside it.

## S4 is the unit. S1 to S3 without it are the shape this build exists to close

A helper that is present, correct and unobserved is exactly what §1 is complaining about: AC6
compared two runs of `apply` and an ordinary in-place `write_text` passes that comparison
identically, so the mitigation could have been dropped silently and the build would still have
closed green.

Stage the break, confirm RED, unstage. A gate you have only ever seen pass is an assertion about
nothing, and that rule is in the charter because this repo kept breaking it.

## The declared set is DERIVED, and you should run the predicate before you wire it

S2 says the adopter-bar write set is derived at build time rather than pinned in the spec. Run your
candidate predicate over the real tree BEFORE wiring it and print hits AND near-misses — doing that
routinely surfaces live instances the original symptom never reached, and it catches a predicate
that would red an innocent file. Report both lists in your ledger even if the answer is one file.

## S3's arm asserts two things, and one of them is easy to forget

The previous runner file survives byte-identical, AND no temp sibling is left in the directory. An
arm that checks only the first passes for a helper that leaks a temp file on every failure.

## The helper's name

`write` is a declared verb in `.lexicon.conf` — *persist to a store* — so a `write_`-leading name is
available to you, unlike the last two units, whose specs each proposed a name the gate would have
redded. Ask `--suggest` anyway; it is the authority and I have not run it for your name.

## You close another unit's criterion

If your observer discharges `DEPL-cMendedVintage-13`'s AC6, say so EXPLICITLY in your ledger and add
its own `**Evidences:**` block, as `DEPL-cMendedVintage-15` did for `-10`'s AC4. That unit's ledger
currently records the mechanism as built and unexecuted.

## Every line number in the spec is stale

Six units have edited `tools/govkit/govkit.py` since this spec was written, the most recent within
the hour and directly in the code you are about to touch. Locate every site by symbol.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`**. Spell no `tools/<kit>/…` path in shipped prose and check your own new
comments against the carried-prefix predicate.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo — each needs a scratch fixture target under the run's scratch root. Write the
acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-21-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows; `--dispatch` refuses a
declaration naming `RUN.md`. Bound every command at 900s or more.
