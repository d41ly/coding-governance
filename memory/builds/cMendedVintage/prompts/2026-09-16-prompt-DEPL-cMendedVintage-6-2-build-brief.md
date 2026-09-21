# Build brief — DEPL-cMendedVintage-6

**Serves:** journal DEPL-cMendedVintage-6

This is the data-loss fix the `GOVKIT_RERENDER` flip is gated behind. Read the spec whole first.

*Standing note: two briefs in this build asserted a mechanism measurement later disproved. Anything
below I have not run myself is marked UNVERIFIED — measure before acting on it.*

## Why this one blocks the flip

`DEPL-cMendedVintage-7` turns `GOVKIT_RERENDER` on by default, at which point `update` starts running
every declared `[[regenerate]]` argv on every adopter. Until this unit lands, one of those argv
DESTROYS adopter files.

The mechanism, recorded open against `govkit.py` before this build began: `tools/unattended/` ships
two fixture piece-records whose FILENAMES spell the install prefix, carried as engine rows by the
descriptor's `**` rule. At any prefix but gov's own, `update` restores gov's spelling as a `missing`
row, and the adopter's repath loop then renames that file over the target's own copy. Every update
destroys whatever the target held there. Reproduced on a fixture installed at prefix `scripts`.

So the flip and this fix are ordered, and the order is in the build README as a rule rather than an
accident of the roster.

## The shape of the fix is already in this descriptor

The same file closed this exact class once before, for the fixture playbook: a `rendered` row whose
destination carries the prefix, written by the adopter rather than renamed by it. Follow that
precedent rather than inventing a second mechanism — a kit with two answers to one question is the
class this repo gates against, and the precedent is three rules up in the file you are editing.

The repath loop goes with it. A rename loop that exists only to fix up filenames the descriptor
should never have shipped at the wrong prefix is the defect, not the remedy.

## What to be careful about

The two fixture records are REAL fixtures used by the unattended kit's own suite. Changing how they
land must not change what the suite reads — if the suite resolves them by the gov-spelled name,
converting them to rendered rows moves that name. Check the suite's resolution before you convert,
and if it breaks, that is a finding to report rather than a suite edit to slip in.

UNVERIFIED by me: whether the piece-record bodies are identical at both prefixes. The spec says
"body unchanged; a template sibling added", which implies they are, but I have not read them.

## Bans this build has already tripped

Lead any new function with a declared verb from `.lexicon.conf` — the offender pin is a two-sided
equality and one bad name reds an unguarded merge-bar leg.

Spell no `tools/<kit>/…` path in anything this kit ships, prose included. The carried-prefix arm is a
BAN: a count may fall and never rise, so `--write-ratchet` is not a remedy. This unit is ABOUT prefix
spelling, so it is the likeliest one yet to trip that.

A fixture can stage a condition the tool does not actually refuse — confirm a RED is the red you
meant. A first cut can be vacuously green when the artifact it inspects is absent.
