**Serves:** research PLAY-dOrderedCharter-37

# Brief: spec 37 — a buildability pre-check against HEAD, while unit 31 builds

## The prompt

> why are the specs being reviews (and 11 times at that) instead of building?

— owner, 2026-11-09. Eight of the last ten units handed their spec back on first dispatch, each for a claim the tree no longer held. This
pre-check reads the next spec against HEAD while the current unit builds, so its fixes fold before its builder starts.

## The brief

### Goal

Find every place spec 37 cannot be built as written over this tree, before its builder is dispatched.

### Items

1. Read spec 37 whole, and the code each scope item, design paragraph and acceptance criterion names, at HEAD.
2. For each claim about the tree, check it: a symbol, file, row, signature, return shape, key or count. Read the code; probe where a read
   cannot settle it, with `python -I` in a scratch folder of your own.
3. Check what units built since the spec's last revision changed under it, PLAY-dOrderedCharter-31 aside, which is building now: units 29,
   23, 32, 33, 46, 35, 36 and 34 landed on this branch since spec 37's rev-6.
4. Check each minted function name with `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, each new fact for a pin, and
   each Readers clause for readers only.
5. Name, for each finding, what the spec says, what HEAD holds, and the narrowest change that makes the spec buildable. A real design
   choice is a finding too, named as a fork.

### Acceptance

- Every finding cites the spec's text and the code at HEAD, and says whether it blocks a build or only misleads.
- No finding is an opinion about the design that the spec has already ruled.

### Gates

None: this is read-only.

### Non-goals

- No edit to any file. No finding about a spec other than 37.
