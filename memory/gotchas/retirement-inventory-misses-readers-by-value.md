---
name: retirement-inventory-misses-readers-by-value
description: an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing
kind: class
universal: false
---

# What reads a retired thing is not only what names it

## Symptom

A spec retires an identifier, a row kind, a column or a vocabulary member, and it does the responsible
thing: it inventories the readers first, one table row per reader, so nothing is left pointing at a
name that no longer exists. The inventory was built by searching for the name. Every reader it found
is real. Then the retirement lands and a test suite reds somewhere the table never mentioned — on a
count that used to be four, on a time that used to be a fixture's twelfth minute, on a string of
twelve `a`s that used to be a row's head.

Those expectations read the retired thing as loudly as any of the named readers. They simply do not
spell it, so no search for the name can find them, and the inventory reports full coverage.

## Where it bit

The `dLoggedFlight` build, on the spec that retires eight Timeline row kinds. Its inventory table was
built by a probe over names and listed every arm that mentioned a retired kind. A spec audit then read
the same arms by hand and confirmed five assertions the table could not hold: a withheld-value count
whose four values included two riding retired rows, a liveness block indexing a vocabulary the same
spec deleted, a shaped-value map taking its time from appended rows and its sha from a retired row's
head, and a cap arm whose row counts included five wide rows a builder adds. All five were literals
typed beside a fixture builder in `tools/runlog/selftest.py`, and every one of them would have gone red
on a retirement the inventory called complete.

The same shape is why a build's own records are searched by grep rather than by path: a repository-wide
sweep touches every folder under `memory/builds/`, and a reader keyed on the folder's name finds none
of it.

## Cause

Inventorying is a search, and a search needs a term. The name is the only term available, so the
inventory silently becomes "readers that spell it" rather than "readers that depend on it". A
dependency on a VALUE — a count of rows a builder placed, a time it chose, a digest of what it wrote —
leaves no token behind. It is a reader all the same, and it is the one that fails last, after the
retirement has landed and the diff has been reviewed.

## The fix

Make the dependency impossible rather than findable. Where an assertion is about what a shared builder
placed, have the builder RECORD its placements and derive the expectation from that record, so the
number moves with the builder and a retirement that moves a carrier moves the expectation with it.
Where a value is genuinely fixed, read it off the artifact under test rather than typing it beside the
thing that produces it — the same rule as deriving a figure instead of authoring it, applied to a test
arm rather than to a document.

Then keep the carriers themselves out of the way: an intruder, a fixture value or a probe target that
must survive a retirement is placed on a row kind or a table the retirement KEEPS, so the two questions
stay separate. A count that proves a renderer withholds a read field should not also record which row
kinds happened to survive.

## How to see it before shipping

Read the retirement's inventory and ask, of each retired thing: what does a reader of this look like if
it does not spell the name? Then go and find those readers the way they can be found — by the builder
or the fixture they are typed beside, not by the name they never carry.

## Detection

No machine gate for the inventory itself; that would have to read a spec's prose against a tree, and it
is parked as the owner's, since it changes a governance carrier. The documented check for a spec audit
is a MUTATION: remove one kind of thing from each shared fixture builder's model, one at a time, and
re-check every literal an arm asserts over it. An expectation that survives the removal of what
produced it was never reading the builder. Run it over every kind the builder can place, never only the
kinds a particular retirement names, or the sweep inherits the blind spot it exists to close.
