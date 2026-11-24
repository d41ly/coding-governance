# TOOL-dQuietDisk-1 leg-tail 23 — memory-recall kit selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** memory-recall kit selftest
- **Hash:** 814b5197baf95112b060bd8a7970f27607b1e225
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
 8 passed, 0 failed
ok   kit version constant and the gov:kit marker agree — 2 marker(s) == 1.38
ok   union.py is byte-identical upstream; bench.py matches its recorded digest (one delta) — 2 file(s) unmodified: bench.py, union.py
FAIL the whole selftest passes from the ADOPTER layout (kit at <root>/memory-recall/) — AssertionError: exit 1 from memory-recall/selftest.py:
FAIL every invocation the CLI and the --with-hook remedy print resolves to a real file — AssertionError: the --with-hook remedy printed no invocation
ok   a DECLARED conf source reaches the corpus as chunks, and un-declaring returns it — chunks 1 -> 2 -> 1, records held at 2
ok   a declared source that does not exist is skipped with a line, not a crash — index built with an absent declared source (1 chunks)
ok   an UNDECLARED repo-root file stays out of the corpus — declared-only 2 chunks, both 3
ok   RECALL_EXCLUDE: a live line answers, its archived versioned copies do not, blank returns them — declared: live only; blank: live + both copies
ok   the ONE walk still serves two callers: untracked visible to query, absent at a rev — query sees 2 file(s), measurement sees 1
ok   bench: a chunk is credited for an id it ANCHORS, never for merely sharing its file — 1 of 3 documents credited
ok   bench: r@k, f@k, rr and b@k over a synthetic ranking — r@k, f@k, rr and b@k all move on the cases that should move them
ok   bench: full@k counts TARGETS, not the documents that satisfy them — one target, five satisfying chunks, one retrieved -> full@1 = 1.0
ok   bench: FTS5 punctuation is query SYNTAX — a hostile question is a miss, never a crash — 5 hostile strings survived, the quoted phrase still retrieves
ok   bench: the alias column is separate, searchable, and weighted below the body — ALIAS_WEIGHT=0.4, searchable, and it does not displace a body hit
ok   union: an ensemble spec is a spec, and a Windows path is not one — 5 specs accepted, 7 non-specs rejected including both drive-letter forms
ok   union.SUBS is a subset of what bench.rank_with can dispatch — 11 advertised substrates, all dispatchable
ok   bench: rollup keeps ONE chunk per parent, and a chunk with no record rolls up to its file — 4 chunks, 3 distinct parents
ok   bench.build_index still defaults db_path to ':memory:' for its benchmark callers — signature default held at ':memory:'
ok   query_expr refuses an all-stopword question and phrases an id adjacently — stopword-only refused, id phrased, three destroyable terms survived
ok   rrf fuses on RANKS, so cross-set agreement outranks a strong position in one set — agreement at rank 3 beat rank 1 of one set; the record view carried the id
ok   the rrf key separates two windows of ONE section, and still merges one passage — two windows stay two; one passage across two sets stays one
ok   emit: the byte budget bounds emission, names its overflow, and beats full documents — snippets 2313 B against 51373 B for the same 20 hits
ok   emit: snippets stop at SNIPPET_SHARE of the budget and every later hit is a pointer line — 3 snippets + 17 pointers in 1107 B of 1624 B; 10 of 20 at the small budget
ok   supplied --terms bypass terms() verbatim, and the refusal LEADS with --terms — 6 destroyable terms survived; the refusal leads with --terms
ok   argv is ONE left-to-right scan, and the refusal is reachable and logged — 4 orderings resolve one question; 4 refusals fire and the bare one logs
ok   the result cap shrinks `results` and does NOT clamp `n_hits` — 14 hits, 5 kept in `results`
ok   shown_paths carries one entry per EMITTED hit, so a rank past the cap is recoverable — n_shown 14 against RESULT_CAP 5, every rank recoverable
ok   --export is byte-stable and leaks no raw query text — 7 rows, byte-stable, none of their questions echoed
ok   --export per-day counts agree with a count that shares no code with the export — 3 days, 4 queries each, hand-counted against the table
ok   --opened attaches to an EXPLICIT qid, the query prints it, an unknown qid writes nothing — qid 1 printed and attachable while 2 was the newest
ok   the alias join lands on the NAMED record and on nothing else — 1 of 2 records aliased, text pinned, the other untouched
ok   the alias join reaches the QUERY index, not only extract.py's output dir — a query built only from bridge vocabulary reached the aliased record
ok   --aliases <file> versus --aliases none differs in the records' alias key and nowhere else — chunks and record text identical, 4 spine document(s) alias-free
ok   the arm-count pin ends an unbroken provenance chain, and main() actually reads the verdict — the live chain ends at 86; three synthetic failure directions all red
ok   repo_root() resolves the root from inside a LINKED WORKTREE with GIT_DIR inherited — worktree root resolved under an inherited GIT_DIR
ok   extract.py refuses a flag in a positional PATH slot rather than materialising it — rc=2, nothing materialised
ok   DURABLE admits one segment AFTER archive/, and still refuses a non-index file there — after-, before- and flat archive layouts match; a non-index file does not
ok   RECALL_NODE_TAG_CLASS narrows the id grammar, prints, defaults to a-z, and refuses a bad class — a-f narrows both id readers, absent = a-z, `a-f]` and `f-a` exit 2 naming the key
ok   RECALL_CITED_FAMILIES makes ids and never durable homes, and refuses a homed family — PKG is an id in both readers, PKG.md is no home, ARCH twice exits 2
ok   RECALL_BUILD_QID_CUTOFF feeds build_cutoff per node, and refuses a malformed pair — a:163 -> 163 for a and 0 for b; `a163` exits 2 naming the key
ok   RECALL_EXPORT_DIR moves --export inside the root, refuses an escape, and defaults to git — declared dir honoured with an honest header, `../out` exits 2 writing nothing, absent = git dir
ok   the live-log baseline precedes every arm, and main() appends its row unconditionally — baseline 34121 < first arm 36376, 86 arm(s), main() at 204454; 1 argument-free append, defaults ['_LIVE_LOG', '_LIVE_LOG_BEFORE']
ok   the live-log verdict is total over its five states — skip / skip / ok / ok / FAIL, and the FAIL names both digests
ok   CONF_DIGEST moves with the two grammar keys and ONLY with them — base 8e55c1c61fff; tag and cited move it, cutoff and export do not
ok   a spec H1 anchors the id it defines, by the index generator's own predicate — H1-anchored ['TOOL-aQuill-6', 'TOOL-aQuill-9'] == spec_ids; the journal H1, the fenced H1 and the citation do not
ok   a query for a spec-defined id returns the defining spec's record first — [1] TOOL-aQuill-9 · memory/builds/bQuill/spec/2026-09-28-spec-TOOL-aQuill-9.md:1; the citation comes back as [4]
ok   --used joins logged answers to the worktree's next commit, held ids excluded, read-only — answer-used: 1 of 2 attributable query row(s) cite a shown record id in the worktree's next commit
ok   --used attributes a removed worktree's query row by its logged head's one child — answer-used: 1 of 1 attributable query row(s) cite a shown record id in the worktree's next commit
ok   --used counts a head with two children after the query as ambiguous, crediting neither — attributed by head ancestry: 0 · ambiguous head: 1
ok   supersession: P1 possessive, for and bare, P2, a two-id P3 header, a self-edge, an undefined id — 7 cases; map 3 ids, unresolved ['TOOL-aQuill-99']
ok   supersession order: a whole hit moves under its lowest listed successor, and nothing else moves — 5 placement cases; every unmoved hit kept its relative order
ok   supersession tag: emit's full branch tags a superseded hit, and two successors share one tag — full, snippet and pointer headers tagged; two successors in one tag; partial says partly
ok   the declared arm count matches its pin — 86 == SELFTEST_ARMS
ok   the arm-count pin ends an unbroken provenance chain — ends at 86
ok   the live query log is byte-identical after this run — d733ad1fb0e8
ok   git's exported repository pointers were scrubbed before any arm ran — 8 checked
ok   every scratch repo this run created was removed — 86 swept
---- memory-recall selftest: 89/91 checks passed
```
