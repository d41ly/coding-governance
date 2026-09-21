# Build brief — DEPL-cMendedVintage-16

**Serves:** journal DEPL-cMendedVintage-16

This unit closes spec-audit finding H1. It was PROMOTED rather than folded, and it has been MOVED
from order 25 to order 7 so it runs immediately after the unit that opened the hole. Read the spec
whole first.

## Why this cannot wait for its original slot

`DEPL-cMendedVintage-5` landed one unit ago and declared a lexicon `[[outcome]]` of `code = 1` plus
`must_not_exist = ".lexicon.conf"` plus `ok = true`. The accepted state it MEANS is the unconfigured
posture. The state it actually MATCHES also includes a failed first scaffold, because the conf is
precisely the file the failing program was trying to write — the failure and the posture are
shape-identical under that probe.

And `classify_outcome` reads the kit-level `outcome` list with no per-step scoping, so this is not
confined to the re-render path: `apply`'s CONFIGURE consults it too. The hole is open in the tree
right now, on an adopter-facing verb, which is why this unit sits here rather than twenty places
downstream.

## The load-bearing half is S2, not S1

S1 adds a `must_exist` term so the block names something a decline leaves behind and a failure never
writes. But S2 is what makes it mean anything: **a block declaring both terms today matches on the
second alone.** So adding `must_exist` without fixing the conjunction changes nothing, and the unit
would close green having moved no behaviour.

Verify the conjunction directly. The RED you want is a block whose `must_exist` fails and whose
`must_not_exist` holds, still matching before your change and not after.

## S4 is the part that outlives this unit

S3 stages one failure for lexicon. S4 is the CLASS assertion: for every registry entry declaring an
`[[outcome]]` with `ok = true` and a `must_not_exist` term, the named path may not be a file that
entry's own adopter writes. That is what stops the next kit re-opening this hole by declaring the
same shape. Gate the class, not the instance — fixing lexicon alone and asserting only lexicon is
the shape this repo names as could-not-fail one level up.

## Bounds

Do not touch the regenerate argv `-5` declared; they are correct and this unit is only about the
outcome probe. Do not widen `classify_outcome`'s per-step scoping into a general fix — that is a
larger design change, and if you conclude the narrow fix is insufficient, say so in your return
rather than taking it.

## Traps measured in this build

The lexicon gate is a two-sided equality on an offender pin, and one new non-conforming function name
reds it — that already happened once here, from a fixture helper, and was only caught by a targeted
re-measurement. If you add a function, lead it with a declared verb from `.lexicon.conf`.

A fixture can stage a condition the tool does not actually refuse; confirm the RED is the red you
meant. A first cut can be vacuously green when the artifact it inspects is absent; assert existence
first. Any `govkit.py` line number in the spec has drifted — six units have landed in that file.
