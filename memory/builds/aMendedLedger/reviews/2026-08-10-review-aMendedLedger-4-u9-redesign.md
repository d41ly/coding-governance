# Adversarial review — aMendedLedger U9, the driver redesign, `a851e85..e03ac48`

- **subject** — one commit (`e03ac48`, "the merge driver stops guessing at structure — two planes,
  kit 2.0"), 15 files, +1599/-663. `tools/memory-tree/merge-rows.py` is rewritten around a two-plane
  skeleton pipeline; `merge-rows.test.sh` is rebuilt on a never-worse-than-`git merge-file` bar;
  `check-wiring.sh` gains a keyed-count assertion with a new self-test state; the kit version, the
  epoch gate's DELEGATES, the dossier and the charter follow.
- **question** — the same one three rounds asked and this one had to answer differently: **is there
  an input where the driver loses, duplicates or misfiles content that `git merge-file` on the
  identical three blobs does not?**
- **review shape** — four finder lenses (never-worse-than-git · reconciliation internals · the
  newline and encoding contract · suite integrity), each in its own `git clone --shared`, each
  required to reproduce by EXECUTION against a live control. No verify stage was spawned: the
  orchestrator reproduced every finding itself before accepting it, which is the same refutation
  discipline at one agent instead of five.
- **counts** — 8 upheld (5 content-destroying · 2 refusals where git resolves · 2 terminator) ·
  7 suite-honesty findings upheld · 1 upheld and deliberately NOT fixed · several refuted.

## Why the finders were told not to reason

Three rounds of this driver were passed by argument and each shipped corruption; two of those
regressions passed a green 38-leg bar. So the brief made execution mandatory and cloning free, and
it paid: **every one of the eight defects below was found by running the driver, and none of them is
visible by reading.** Two finders independently fuzzed — 1078 and 6000 generated triples — and both
convergent findings came from the fuzz, not the read.

## Upheld — content destroyed, all at rc 0 or outside the markers

| # | defect | control | mine? |
|---|---|---|---|
| 1 | a byte that is not valid UTF-8 replaced by U+FFFD and committed; two sides with DIFFERENT invalid bytes decoded EQUAL and auto-resolved to a third value neither wrote | git preserves the bytes | pre-existing, amplified |
| 2 | the `raw:` digest hashed `line.strip()`, so `- notes` and `  - notes` were one key; rule 4 substituted one side's body for the other's and destroyed a line all three inputs carried | rc 0, correct | **yes** |
| 3 | a key placed both inside a rule-4 region and outside it: two independent cursors, one entry written twice and one never; `region_keys` excused the key from conservation so all five postconditions were silent | rc 0/1, correct | **yes** |
| 4 | a conflicted key carried in TWO sections collapsed into one block under the first heading and emptied the second — the record leaves its section whichever side the author picks | two scoped conflicts, in place | **yes** |
| 5 | an input already carrying a COMMITTED conflict block was read as a region this merge produced; rule 3 concatenated it, erased all three markers and accepted both wordings at rc 0 | rc 0, markers preserved | **yes** |

Defect 1 is the one worth dwelling on. It predates the redesign — the retired driver mangles the
same bytes — but the redesign auto-resolves strictly more inputs, so a corruption that used to land
at rc 1 now lands at rc 0 with a `clean` audit line. "Pre-existing" is not the same as "unchanged in
blast radius", and the fix (surrogateescape at every one of the six encode/decode sites) is what the
never-worse bar demands.

Defect 5 is the subtlest. `settled()`, `_MARKER_RE` and the region walker all matched on marker
TEXT, and a governed index can already contain a committed unresolved block — this build's own risk
section records two merges auto-committed before anyone looked. The fix is structural rather than
another predicate: git's own markers now carry the token sentinel in their `-L` labels, and no input
line may contain that sentinel, so a sentinel-labelled marker is git's BY CONSTRUCTION. The labels
are rewritten to the plain `ours`/`theirs` an author reads before anything is written.

## Upheld — a refusal where git returns a scoped hunk

6. **One cursor shared across a region's ours/base/theirs sections.** Each section indexes a
   different body dict, so a key on both sides — two nodes renaming a heading while each appends a
   row, the most ordinary rule-4 shape there is — consumed ours' only body and then ran off the end
   on theirs'. A `StructureDrift` whose own comment called it "unreachable by construction", and a
   whole-file sandwich over git's ten-line hunk. Per side, byte-identical to git.
7. **`str.splitlines()` breaks on eight characters `_split_term` does not** (VT, FF, FS, GS, RS,
   NEL, U+2028, U+2029). A file carrying a U+2028 soft break — the ordinary Word/macOS paste —
   failed its OWN identity merge and the fail-closed body wrote the line back split in two by a
   newline that was never in the input. One splitter now, over the three terminators this driver
   honours; `str.splitlines` appears nowhere.

## Upheld — terminators

8. A conflict block applied the dominant terminator to its row BODIES as well as its markers,
   rewriting an LF row inside a CRLF file (and the mirror). `_dominant` read only `%A`, so an
   emptied `%A` put LF markers into an all-CRLF file on the fail-closed path — precisely the
   asymmetry newline site 6 exists to remove.

## Upheld — the suite overclaimed about itself

This is the finding that matters most for the next round, because it is this build's own failure
class turned on the instrument. The header said the mechanical bar binds "IN EVERY CASE". Measured
by instrumenting `never_worse()`: **it bound on 12 of 34 cases.** The arithmetic comparison can only
bind where the control EXITS 0 — only then is its output an answer rather than a conflict to resolve
by hand — and nothing said so or floored it. Also upheld and fixed:

- the group-count floor counted `# --- ` COMMENT BANNERS: deleting two groups whole, or commenting
  out every executable line of one while keeping its banner, both still printed PASS. There is now a
  second floor on real `run` cases and a third on the binding count, all reported in the PASS line.
- the identity population guard counted STRINGS, so an unmatched glob (which stays literal in sh)
  satisfied a floor of 3 with zero backlog shards in the arm. It counts files that exist now.
- three "git refuses this input" premises were prose, in a file where seven others are measured.
- `&& c=0 || c=1` collapsed a git ERROR (rc ≥ 128) into "git refuses" — the two states this arm
  exists to distinguish.

Refuted or already-disclosed, listed so the next round does not re-report them: group 13 and group
23 DO assert bytes on both halves (the brief suspected rc-only arms; there are none); `ctl_wrong` has
exactly one call site and measures its own premise; group 33's injections inject and fail closed;
`|||||||` is unreachable under the pinned style; a setext `=======` mis-splits a region but always
falls to rule 4 and is byte-preserving.

## Upheld and deliberately NOT fixed

**A row MOVED by one side and DELETED by the other is dropped at rc 0, where `git merge-file` keeps
it.** The delete branch compares the key's row BODIES, which a relocation does not change, so the
side that moved it reads as having left it alone. Confirmed through a real `git merge`:
auto-committed, `1 deletion(-)`, no markers. It predates this unit — the retired driver loses it
too — so the redesign does not regress it, and closing it needs a placement rule the row plane
deliberately does not have. Adding one, unreviewed, at the end of a redesign is exactly how rounds
one through three shipped corruption. Recorded in the dossier Gaps and as `TOOL-aMendedLedger-9`.

Two smaller limits are recorded with it: a file that already carries a committed conflict block now
REFUSES where git resolves (loud and lossless, on a file hygiene reds anyway), and the delete/modify
branch's scoped block is unplaceable for the plain shape because a row edit is invisible to the
skeleton by design, so that shape ends in a whole-file refusal rather than git's scoped hunk.

## What the bar reads at the end

`PASS — merge-rows: 47 groups / 37 run cases held, 13 under the arithmetic never-worse bar,
0 conservative (cap 0)` · `tools/check-wiring.test.sh` 56/56 · `tools/run-gates.sh` 38/38.

The number that should be read first is **0 conservative**: across every case in the suite, there is
no input where the driver refuses and `git merge-file` resolves correctly. The number that should be
read second is **13 of 37** — because the previous version of that sentence claimed 42 of 42, and a
suite that reads stronger than it is, is how this driver shipped rc-0 corruption twice.
