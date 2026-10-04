# Run mandate — aWindowedPass

**Serves:** journal TOOL-aWindowedPass-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-04. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The owner's turns that produced it

The owner asked, after build aHalvedInstall was held on check 23: *"UNDECLARED_WRITE_CEILING has been
a problem for the unattended builds - both in this repo and its adopters. Unattended builds get
aborted because of this. What can be done to fix this for good without taking away from its intended
purpose?"* The session answered with five parts, and the owner replied *"build this fix in full"*.

## The prompt

> Build in full the fix for UNDECLARED_WRITE_CEILING (unattended kit gate check 23) proposed in the
> previous turn, so it stops aborting unattended builds here and in adopters without losing its
> purpose (the disjointness proof concurrent passes rest on). The five parts: (1) count only passes
> that actually overlapped a sibling pass, derived inside check 23 from the dispatch rows' windows; a
> solo pass's undeclared write is reported, never counted. (2) catch it while repair is legal: a
> pre-commit step refuses a commit that belongs to an open dispatched pass and stages paths outside
> its declared set (plus generated outputs), printing the exact --dispatch --writes re-declare
> command. (3) generated outputs self-declare: kits that own generators declare their outputs and
> check 23 reads those declarations instead of a hand-typed GENERATED_INDEXES list, so adopters
> inherit them; keep the index-with-its-generator refusal. (4) attribute pass commits structurally (a
> Pass: <unit-id> trailer the harness writes and the pre-commit step requires), not by unit-id
> substring in the subject. (5) grade each run against zero on its own, retiring the repo-global
> shrink-only ceiling. Measured basis: 8 of 397 dispatch groups in this repo ever held more than one
> pass.

## The diagnosis the parts answer

Measured over this repo's run records before the build: 8 of 397 dispatch groups held more than one
pass, so check 23 graded solo passes about 98% of the time. The violations that held or aborted runs
were hook-forced generated writes (aSightedSkeptic: 60 against 53; aHalvedInstall's `symbols.json`),
a records commit taken as a pass because its subject named the unit as a substring
(aHalvedInstall's `DEPL-aHalvedInstall-1..4`), and a ceiling counted across every live run, which no
run can repair after the commit and only the owner can raise.

## No owner turn was taken

Acceptance and gates derive from the five parts: each is observable as a check-23 or pre-commit arm
over a fixture, and the kit gate and its suites are the gates.
