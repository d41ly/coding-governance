# TOOL-dHonouredPark-3 — build record

**Serves:** journal TOOL-dHonouredPark-3

Node `d`, 2026-08-25, base `bd0348f3`. Re-keys `tools/dead-path-waivers.txt` from `<path>:<line>` to
`<path>\t<ordinal>\t<line-text>\t<reason>`. Spec: `../spec/2026-08-25-spec-dHonouredPark-3.md`.

## What actually changed, and what deliberately did not

The restructure is ONE idea. Each registry row is RESOLVED to the `<path>:<line>` token it names, and
every set difference downstream is untouched. That is what keeps "stale" meaning MEMBERSHIP in the
derived hit set — a row whose line survives but whose needle left the derivation still reds — which
rev-1's "a row whose text matches no line in that file" would have silently dropped.

Three refusals exist where two did. MALFORMED (the ordinal is absent, zero, negative or not a number)
is distinct from STALE, because line numbers were unique by construction and an occurrence index is
not, so the property is asserted rather than inherited. UNRESOLVED rows — the file is gone, or the
text was reworded — report by their own reason rather than vanishing from the waived set, which would
have made a waiver that stopped covering anything indistinguishable from a row nobody wrote.

`ENVIRON`, never `awk -v`. A `-v` assignment expands backslash sequences, and one carrier on this
tree holds a literal `\n`. Measured on that exact row before the code was written this way: `awk -v`
reported 0 matches where Python reported 1.

The registry gained an LF pin in `.gitattributes`. It never had one and did not need one while a row
was a path, a colon and free whitespace; a TAB-separated grammar makes the bytes load-bearing.

## Every arm was observed against the REAL tree before it was written

Not against the fixture. The charter's rule is to run a candidate predicate over the real tree first,
and it earned its keep: the first pass of this observation ran against a registry that a stray
`git restore --staged --worktree` had silently reverted to its pre-migration state, and every row
came back unwaived. The confusing result was the artifact, not the mechanism — which is exactly the
trap `memory/gotchas/checkout-restores-the-whole-file.md` records, hit by the session that owns it.

## Acceptance ledger

**Evidences:** TOOL-dHonouredPark-3

- **AC1** — OBSERVED. `bash tools/check-dead-paths.sh` on the migrated tree: `clean — 17 derived
  needle(s), 8 declared waiver(s), no undeclared carrier`.
- **AC2** — OBSERVED, `rc=0`. A different line inserted above the carrier at
  `check-memory-hygiene.sh:288`, staged: still 8 waivers. This is the failure the ruling
  exists to remove and it is the one arm that would have redded under line keying.
- **AC3** — OBSERVED. That carrier reworded: `rc=1`, and the message is the UNWAIVED one
  (`names a path this repo DELETED`), not the stale one, because that report comes first and exits.
  Asserted as it behaves rather than as it reads better.
- **AC4** — OBSERVED. A tracked `tools/probe/STATUS.md` added, removing `STATUS.md` from the derived
  needle set: `rc=1`, `stale waiver(s)`, naming exactly the four rows that carry it
  (`check-memory-hygiene.sh:554` and `.test.sh:1314/1319/1375`). This is the property rev-1's
  predicate would have dropped.
- **AC5** — OBSERVED both ways. Two identical carriers with ONE row: `rc=1` on the unwaived
  occurrence at line 289. The same tree with a SECOND row at ordinal 2: `rc=0`, `2 declared
  waiver(s)`.
- **AC6** — OBSERVED for all four shapes. Ordinals `0`, `zero`, empty and `-1` each give `rc=1` and
  `MALFORMED waiver row`, distinct from the stale message.
- **AC7** — OBSERVED. An IDENTICAL line inserted above a waived carrier: `rc=1`. This is the residual
  the ordinal does NOT survive, named in the registry header and armed rather than argued away.
- **AC8** — OBSERVED. A row naming `NO-SUCH-FILE.md` with text that is not a carrier anywhere:
  `rc=1`, `stale waiver(s)`, `NO-SUCH-FILE.md:<file is gone>`. Staged deliberately with no carrier of
  its own, because the ordinary spelling of that break leaves an unwaived hit whose report exits
  first — the branch is reachable, and proving it took a fixture designed to reach it.
- **AC9** — OBSERVED, `git diff` over the migration. All eight rows keep their reason verbatim and
  each resolves to ordinal 1: no text on this tree occurs twice in its own file, so the ambiguous case has an EMPTY
  population here. `bash tools/check-dead-paths.sh` exits 0 on the migrated tree.
- **AC10** — OBSERVED. `bash tools/check-dead-paths.sh` rc=0 · `bash tools/check-dead-paths.test.sh`
  `PASS (30 assertions)` · `python tools/govkit/govkit.py selfcheck` rc=0 · `python3
  tools/codebase-map/test_codebase_map.py` rc=0.
- **AC11** — OBSERVED. `python tools/memory-tree/corpus_ids.py --report`: 134405 B before, 134659
  after, so one decision row cost 254 B. `.memory-tree.conf` carries this unit's movement line,
  134558 to 134812.

## The three other grammar sites, and the sibling left alone

`check-dead-paths.sh`'s own header pinned the grammar as "matching `install-prefix-waivers.txt`
exactly", which this unit makes permanently false rather than merely stale. It now says the
divergence is DELIBERATE and warns against restoring the parity: that sibling carries twelve rows in
the same `<path>:<line>` shape with the same exposure, and the owner ruled ONE file. A registry moves
when its own keying has actually failed, not by association.

`tools/govkit/registry.toml`'s exemption reason for the registry read "Its rows are gov paths and gov
line numbers", which S1 falsified. `memory/map/features/install-prefix.md` claims this unit's three
paths and both its gate legs, so its prose records the divergence too — a reader finding two grammars
is looking at a decision rather than at drift.

The registry header's own line-keyed re-stamp protocol is replaced by an ordinal-shaped one: a merge
landing edits above a carrier no longer touches a row, and a row goes stale only when the carrier's
TEXT changed or it stopped being a hit. Re-pointing such a row at whatever now sits nearby is the
proximity error that earned this whole re-key.
