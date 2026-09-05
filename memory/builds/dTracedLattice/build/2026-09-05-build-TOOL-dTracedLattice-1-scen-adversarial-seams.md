**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7

# The adversarial scenario set — real seams whose names are common words

This is the set that decided the re-ranking question. Every row is a seam established by
READING THE CODE, paired with the behaviour phrase a session would plausibly type when it
needed that seam. It is the set on which the confidence re-rank takes recall@5 from 11/28
to 2/28, and `TOOL-dTracedLattice-1` AC1 requires any ranking change to score at least the
shipped 11/28 against it.

It is carried here as evidence, fenced rather than as a bare `.json`, because a record
under `build/` owes a binding line and JSON cannot carry one. The unit that builds AC1
extracts it to a fixture beside the kit, the way `recall-fixture.json` sits beside
`memory-recall` — and inherits that fixture's constraint, which is that a set measured
against THIS corpus must not ship to an adopter who never measured it.

Rows: 28.

```json
{
 "$schema_note": "lens-3 adversarial scenarios for reuse_lookup ranking; see the .md companion",
 "$generated_by": "build_scen3.py over the tracked tree",
 "$repo_head": "991153457d30c923151d749e12afedd4e9176689",
 "$tree_dirty": false,
 "$seam_fanin_threshold": 3,
 "$n_scenarios": 28,
 "$corpus": {
  "tracked_py_files": 49,
  "symbols_json_entries": 769,
  "reference_index_tokens": 4934
 },
 "scenarios": [
  {
   "query": "split a camelCase or snake_case identifier into lowercase word pieces",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "subtokens",
   "why_it_is_a_real_seam": "Its own docstring calls it 'the single tokenizer behind both the recall corpus (S3) and the collision stem-compare (S5)'. Four m.subtokens(...) call sites outside its file, plus a deliberate second copy at tools/lexicon/subtokens.py whose header states the direction of truth and names the gov-internal parity leg that asserts the two agree.",
   "name_class": "common-word",
   "id": "ADV-01",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 607,
   "also_acceptable": [
    "tools/lexicon/subtokens.py::subtokens"
   ],
   "same_name_definers": 2,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py",
    "tools/lexicon/subtokens.py"
   ],
   "shipped_fan_in": 4,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 5,
    "doc_freq_text_corpus": 46,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 3,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 4
    }
   },
   "established_by": "read tools/codebase-map/map_lib.py:607-613 and tools/lexicon/subtokens.py:1-30; receiver census shows m.subtokens x4",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 20
  },
  {
   "query": "decide whether two names are talking about the same thing",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "stems",
   "why_it_is_a_real_seam": "Docstring: 'the one definition of lexically related used by the lookup shortlist AND the --converge collision check, so a match means the same thing in both.' Eight m.stems(...) sites across reuse_lookup.py and map_lib's own detect_collisions. Re-implementing it silently forks the two consumers.",
   "name_class": "common-word",
   "id": "ADV-02",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 621,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py"
   ],
   "shipped_fan_in": 2,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 3,
    "doc_freq_text_corpus": 24,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 8
    }
   },
   "established_by": "read tools/codebase-map/map_lib.py:621-628, callers at reuse_lookup.py:194,204,210 and map_lib.py:1231,1238",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 45
  },
  {
   "query": "normalise line endings before byte-comparing a generated file",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "lf",
   "why_it_is_a_real_seam": "Docstring: 'LF-normalize before byte-comparing a committed artifact (CRLF-checkout defense).' Three m.lf(...) sites, one of them the freshness gate in gen_map.py and two the shipped + template freshness tests. A Windows checkout that skips it reds a green tree, which is the gotcha this repo already records.",
   "name_class": "short-abbrev",
   "id": "ADV-03",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 1538,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py"
   ],
   "shipped_fan_in": 4,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 5,
    "doc_freq_text_corpus": 99,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 3
    }
   },
   "established_by": "read tools/codebase-map/map_lib.py:1538-1540; callers gen_map.py:262, test_codebase_map.py:146, test_codebase_map.template.py:146",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 55
  },
  {
   "query": "resolve the kit's project configuration once and cache it",
   "expected_file": "tools/memory-recall/recall_conf.py",
   "expected_symbol": "resolve",
   "why_it_is_a_real_seam": "Docstring: 'The kit's project layer, or a ConfError carrying the printable refusal. Cached per process: every module in the kit calls this at import.' It is the kit's single entry to MEMORY_ROOT, FAMILIES and the cache budget, and it owns the refusal text. A second reader loses both the refusal and the cache.",
   "name_class": "common-word-ambient",
   "id": "ADV-04",
   "adversarial_role": "harm-ambient-filter",
   "expected_line": 236,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-recall/recall_conf.py"
   ],
   "shipped_fan_in": 26,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": false,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 27,
    "doc_freq_text_corpus": 531,
    "tier_identifier_index": 0,
    "tier_text_corpus": 0
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "pathlib.Path(__file__)": 30,
     "Path(__file__)": 8,
     "target": 7,
     "pathlib.Path(root)": 3,
     "recall_conf": 3,
     "pathlib.Path(argv[i + 1])": 2
    }
   },
   "established_by": "read tools/memory-recall/recall_conf.py:236-268; three recall_conf.resolve attribute sites",
   "shipped_rank": 1,
   "shipped_points_at_file": "tools/memory-recall/recall_conf.py",
   "shipped_file_correct": true,
   "shortlist_len": 95
  },
  {
   "query": "query the full-text index and get ranked passages back",
   "expected_file": "tools/memory-recall/query.py",
   "expected_symbol": "search",
   "why_it_is_a_real_seam": "The kit's ONE FTS5 read path: opens the db read-only by URI, orders by bm25 with B.ALIAS_WEIGHT as the third column weight, and returns the dict shape rrf() fuses. A second query that omits the weight or the snippet columns silently changes ranking and breaks fusion.",
   "name_class": "common-word-stdlib-shadow",
   "id": "ADV-05",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 647,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-recall/query.py"
   ],
   "shipped_fan_in": 23,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 24,
    "doc_freq_text_corpus": 119,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "re": 17,
     "_re": 5,
     "_STATUS": 3,
     "_OWN_ID": 3,
     "rx": 3,
     "_numv": 3
    }
   },
   "established_by": "read tools/memory-recall/query.py:647-674; both rrf call sites at query.py:1177,1181 consume its output",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 51
  },
  {
   "query": "combine two ranked result lists into one ordering",
   "expected_file": "tools/memory-recall/query.py",
   "expected_symbol": "rrf",
   "why_it_is_a_real_seam": "Reciprocal-rank fusion at bench.RRF_K, the instrument's own constant, keyed on (path, line) rather than rowid because two FTS sets' rowids are unrelated integers. A second fusion would grade differently from the benchmark that sets the recall floor.",
   "name_class": "short-abbrev",
   "id": "ADV-06",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 675,
   "also_acceptable": [
    "tools/memory-recall/bench.py::rrf"
   ],
   "same_name_definers": 2,
   "same_name_definer_files": [
    "tools/memory-recall/bench.py",
    "tools/memory-recall/query.py"
   ],
   "shipped_fan_in": 1,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": true
    },
    "doc_freq_identifier_index": 2,
    "doc_freq_text_corpus": 4,
    "tier_identifier_index": 2,
    "tier_text_corpus": 2
   },
   "edge_split": {
    "bare_name_files": 2,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-recall/query.py:675-690 and the sibling copy at tools/memory-recall/bench.py:284",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 41
  },
  {
   "query": "print results until a byte budget runs out",
   "expected_file": "tools/memory-recall/query.py",
   "expected_symbol": "emit",
   "why_it_is_a_real_seam": "Owns the budget contract, including the one deliberate exception: a budget too small for even the first hit emits that hit alone and reports the overflow, rather than printing an empty list that reads as 'no such record'. Re-implementing the loop loses that exception.",
   "name_class": "common-word",
   "id": "ADV-07",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 719,
   "also_acceptable": [],
   "same_name_definers": 2,
   "same_name_definer_files": [
    "tools/govkit/govkit.py",
    "tools/memory-recall/query.py"
   ],
   "shipped_fan_in": 1,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 2,
    "doc_freq_text_corpus": 196,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "r": 20
    }
   },
   "established_by": "read tools/memory-recall/query.py:719-740",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 79
  },
  {
   "query": "find out which record id a line in the decision log belongs to",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "key",
   "why_it_is_a_real_seam": "'The record id this line anchors, or None if it anchors none.' It is the row key the whole three-way merge driver is built on: skeleton(), census(), sections() and reconcile() all key off it, and the driver exists because the playbook forbids per-node index shards. A second id-extractor forks the merge semantics.",
   "name_class": "common-word-stdlib-shadow",
   "id": "ADV-08",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 213,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 28,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 29,
    "doc_freq_text_corpus": 752,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 22,
    "kwarg_label_files": 14,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:213 plus its consumers at :286,:311,:388,:590,:747",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 71
  },
  {
   "query": "get the id-anchor regexes for this repo's record families",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "anchors",
   "why_it_is_a_real_seam": "'The ONE anchor grammar, imported lazily and never re-typed.' The laziness is load-bearing: at module scope an import failure kills the driver before main() can write anything, which is the silent-take-ours shape. Re-typing the regex in a caller reproduces exactly that.",
   "name_class": "common-word",
   "id": "ADV-09",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 184,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 4,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 5,
    "doc_freq_text_corpus": 176,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 5,
    "kwarg_label_files": 1,
    "attribute_receivers": {
     "g": 1
    }
   },
   "established_by": "read tools/memory-tree/merge-rows.py:184-200",
   "shipped_rank": 2,
   "shipped_points_at_file": "tools/memory-tree/merge-rows.py",
   "shipped_file_correct": true,
   "shortlist_len": 45
  },
  {
   "query": "read a markdown file while skipping anything inside a code fence",
   "expected_file": "tools/memory-tree/gen_build_index.py",
   "expected_symbol": "unfenced_lines",
   "why_it_is_a_real_seam": "row_grammar.py imports it with the inline comment 'the kit's ONE fence reader; see scan()'. It strips one trailing CR, recognises tilde fences, and closes a fence only with the marker that opened it. row_grammar shipped its own reader once and the delegation is the fix.",
   "name_class": "compound-common",
   "id": "ADV-10",
   "adversarial_role": "control-signal-agrees",
   "expected_line": 291,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/gen_build_index.py"
   ],
   "shipped_fan_in": 1,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": true,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": true
    },
    "doc_freq_identifier_index": 2,
    "doc_freq_text_corpus": 6,
    "tier_identifier_index": 3,
    "tier_text_corpus": 3
   },
   "edge_split": {
    "bare_name_files": 2,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/row_grammar.py:39,163 and gen_build_index.py:321-323",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 87
  },
  {
   "query": "list the files git is tracking in this repo",
   "expected_file": "tools/govkit/govkit.py",
   "expected_symbol": "tracked",
   "why_it_is_a_real_seam": "git ls-files -z split on NUL, the only spelling that survives a path with a space or a newline in it; eight bare call sites inside govkit. This repo's own memory records that gates see only tracked files, so this is the population every govkit check is asserted against.",
   "name_class": "common-word",
   "id": "ADV-11",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 118,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/govkit/govkit.py"
   ],
   "shipped_fan_in": 7,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 8,
    "doc_freq_text_corpus": 729,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 8,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/govkit/govkit.py definition of tracked(root); 8 bare-name call files",
   "shipped_rank": 3,
   "shipped_points_at_file": "tools/govkit/govkit.py",
   "shipped_file_correct": true,
   "shortlist_len": 55
  },
  {
   "query": "run a git subcommand and get stdout as text",
   "expected_file": "tools/memory-recall/query.py",
   "expected_symbol": "git",
   "why_it_is_a_real_seam": "Five per-kit copies of the same helper exist, one per kit, because kits are copy-installed and a kit file names nothing outside itself by literal. The right answer is 'your own kit already has one' and never 'import another kit's'. A tool that returns a single winner across kits is giving the wrong SHAPE of answer, not merely the wrong row.",
   "name_class": "common-word",
   "id": "ADV-12",
   "adversarial_role": "disambiguation",
   "expected_line": 193,
   "also_acceptable": [
    "tools/govkit/govkit.py::git",
    "tools/memory-recall/extract.py::git",
    "tools/govkit/matrix.py::git",
    "tools/govkit/selftest.py::git"
   ],
   "same_name_definers": 5,
   "same_name_definer_files": [
    "tools/govkit/govkit.py",
    "tools/govkit/matrix.py",
    "tools/govkit/selftest.py",
    "tools/memory-recall/extract.py",
    "tools/memory-recall/query.py"
   ],
   "shipped_fan_in": 7,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 8,
    "doc_freq_text_corpus": 943,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 8,
    "kwarg_label_files": 1,
    "attribute_receivers": {
     "ctx": 23,
     "self": 1
    }
   },
   "established_by": "defs at govkit.py:109, matrix.py:84, selftest.py:194, extract.py:160, query.py:193",
   "shipped_rank": 4,
   "shipped_points_at_file": "tools/memory-recall/query.py",
   "shipped_file_correct": true,
   "shortlist_len": 71
  },
  {
   "query": "read a file from the memory tree as text",
   "expected_file": "tools/memory-tree/gotchas.py",
   "expected_symbol": "read",
   "why_it_is_a_real_seam": "Three of the five memory-tree read copies are byte-identical (binary open, utf-8 with errors=replace, CRLF folded to LF). The other two are deliberately NOT: row_grammar.read uses text mode and strict utf-8, and merge-rows.read uses newline='' with surrogateescape because site 1 of its newline contract needs the real bytes. Wiring through the wrong one silently changes newline and decode behaviour.",
   "name_class": "common-word",
   "id": "ADV-13",
   "adversarial_role": "disambiguation-semantics-differ",
   "expected_line": 70,
   "also_acceptable": [
    "tools/memory-tree/check-arms.py::read",
    "tools/memory-tree/corpus_ids.py::read"
   ],
   "same_name_definers": 6,
   "same_name_definer_files": [
    "tools/memory-recall/extract.py",
    "tools/memory-tree/check-arms.py",
    "tools/memory-tree/corpus_ids.py",
    "tools/memory-tree/gotchas.py",
    "tools/memory-tree/merge-rows.py",
    "tools/memory-tree/row_grammar.py"
   ],
   "shipped_fan_in": 9,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 10,
    "doc_freq_text_corpus": 1169,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 6,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "fh": 6,
     "io.open(path, encoding='utf-": 1,
     "_fh": 1,
     "io.open(os.path.join(t7y, '.": 1,
     "sys.stdin": 1,
     "open(runner_path, encoding='": 1
    }
   },
   "established_by": "compared all five defs: check-arms.py:68, corpus_ids.py:100, gotchas.py:70, merge-rows.py:1084, row_grammar.py:56",
   "shipped_rank": 4,
   "shipped_points_at_file": "tools/memory-tree/row_grammar.py",
   "shipped_file_correct": false,
   "shortlist_len": 101
  },
  {
   "query": "write text to a file, creating the parent directory if it is missing",
   "expected_file": "tools/memory-tree/gotchas.py",
   "expected_symbol": "write",
   "why_it_is_a_real_seam": "The kit's paired writer for its read: makedirs(exist_ok) then a binary utf-8 write, so a generated artifact never picks up CRLF from a Windows text-mode handle. It is the write half of the newline contract the memory-tree gates assert.",
   "name_class": "common-word-stdlib-shadow",
   "id": "ADV-14",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 75,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/gotchas.py"
   ],
   "shipped_fan_in": 19,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 20,
    "doc_freq_text_corpus": 808,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 2,
    "kwarg_label_files": 1,
    "attribute_receivers": {
     "sys.stderr": 18,
     "fh": 18,
     "_LOG": 4,
     "args": 1,
     "io.open(os.path.join(t7y, '.": 1
    }
   },
   "established_by": "read tools/memory-tree/gotchas.py:75-81",
   "shipped_rank": 2,
   "shipped_points_at_file": "tools/memory-tree/gotchas.py",
   "shipped_file_correct": true,
   "shortlist_len": 64
  },
  {
   "query": "parse this kit's KEY=VALUE conf file the same way bash would source it",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "load_conf",
   "why_it_is_a_real_seam": "Nine same-named definers, and they are NOT interchangeable: map_lib's and memory-tree's parse the one-conf-both-worlds KEY=VALUE grammar with bash quoting semantics, drift_report's is a stated deliberate COPY of map_lib's, and lexicon_conf's parses a block grammar that map_extractors explicitly warns is not the sibling KEY=VALUE one. The correct answer is per-kit, so a single ranked winner across all nine is wrong eight times out of nine.",
   "name_class": "compound-common",
   "id": "ADV-15",
   "adversarial_role": "disambiguation",
   "expected_line": 180,
   "also_acceptable": [
    "tools/memory-tree/gotchas.py::load_conf",
    "tools/drift-audit/drift_report.py::load_conf",
    "tools/memory-tree/corpus_ids.py::load_conf",
    "tools/memory-tree/check-arms.py::load_conf",
    "tools/memory-tree/gen_build_index.py::load_conf",
    "tools/memory-tree/row_grammar.py::load_conf"
   ],
   "same_name_definers": 9,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py",
    "tools/drift-audit/drift_report.py",
    "tools/lexicon/lexicon_conf.py",
    "tools/memory-recall/recall_conf.py",
    "tools/memory-tree/check-arms.py",
    "tools/memory-tree/corpus_ids.py",
    "tools/memory-tree/gen_build_index.py",
    "tools/memory-tree/gotchas.py",
    "tools/memory-tree/row_grammar.py"
   ],
   "shipped_fan_in": 18,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": true,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 19,
    "doc_freq_text_corpus": 69,
    "tier_identifier_index": 2,
    "tier_text_corpus": 2
   },
   "edge_split": {
    "bare_name_files": 12,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 4,
     "recall_conf": 2,
     "lxc": 1,
     "dr": 1
    }
   },
   "established_by": "read map_lib.py:180-203, gotchas.py:83+, drift_report.py:78-115 (its comment states the copy), map_extractors.py:142-164",
   "shipped_rank": 2,
   "shipped_points_at_file": "tools/memory-tree/row_grammar.py",
   "shipped_file_correct": true,
   "shortlist_len": 111
  },
  {
   "query": "register a named case in this kit's self-test harness",
   "expected_file": "tools/codebase-map/selftest.py",
   "expected_symbol": "check",
   "why_it_is_a_real_seam": "Every kit's selftest.py defines its own check(name, fn) registration helper, and a session adding a self-test case must call its own kit's. The name is also the check=True keyword argument of subprocess.run, which is where most of its fan-in comes from, so the seam and the noise are the same token.",
   "name_class": "common-word-stdlib-shadow",
   "id": "ADV-16",
   "adversarial_role": "disambiguation",
   "expected_line": 84,
   "also_acceptable": [
    "tools/drift-audit/selftest.py::check",
    "tools/lexicon/selftest.py::check",
    "tools/memory-recall/selftest.py::check",
    "tools/govkit/selftest.py::check",
    "tools/govkit/matrix.py::check",
    "tools/memory-recall/test_recall_floor.py::check"
   ],
   "same_name_definers": 7,
   "same_name_definer_files": [
    "tools/codebase-map/selftest.py",
    "tools/drift-audit/selftest.py",
    "tools/govkit/matrix.py",
    "tools/govkit/selftest.py",
    "tools/lexicon/selftest.py",
    "tools/memory-recall/selftest.py",
    "tools/memory-recall/test_recall_floor.py"
   ],
   "shipped_fan_in": 19,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 20,
    "doc_freq_text_corpus": 1324,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 9,
    "kwarg_label_files": 15,
    "attribute_receivers": {
     "a": 4,
     "args": 1
    }
   },
   "established_by": "defs at codebase-map/selftest.py:84, drift-audit/selftest.py:37, govkit/matrix.py:68, govkit/selftest.py:186, lexicon/selftest.py:70, memory-recall/selftest.py:69, test_recall_floor.py:57",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 183
  },
  {
   "query": "shell out to a command and capture its stdout",
   "expected_file": "tools/memory-tree/gotchas.py",
   "expected_symbol": "run",
   "why_it_is_a_real_seam": "PARTIALLY, and that is the point. gotchas.run(*argv, cwd=None) is a genuine one-line subprocess wrapper the memory-tree kit reuses, but twelve of the thirteen other run definers are CLI bodies or per-selftest harnesses with unrelated signatures. Demoting the merged run row is mostly CORRECT; the set includes it so a re-ranker earns no credit for burying a name that deserved burying.",
   "name_class": "common-word-stdlib-shadow",
   "id": "ADV-17",
   "adversarial_role": "control-correct-demotion",
   "expected_line": 66,
   "also_acceptable": [],
   "same_name_definers": 18,
   "same_name_definer_files": [
    "tools/check-spec-tokens.py",
    "tools/codebase-map/selftest.py",
    "tools/drift-audit/drift_report.py",
    "tools/drift-audit/selftest.py",
    "tools/govkit/census.py",
    "tools/govkit/matrix.py",
    "tools/govkit/selftest.py",
    "tools/lexicon/lexicon.py",
    "tools/memory-recall/selftest.py",
    "tools/memory-tree/check-arms.py",
    "tools/memory-tree/corpus_ids.py",
    "tools/memory-tree/gen_build_index.py",
    "tools/memory-tree/gotchas.py",
    "tools/memory-tree/row_grammar.py",
    "tools/settings-merge.py"
   ],
   "shipped_fan_in": 28,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 29,
    "doc_freq_text_corpus": 1354,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 15,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "subprocess": 194,
     "ctx.git": 15,
     "git": 2,
     "self": 2
    }
   },
   "established_by": "read tools/memory-tree/gotchas.py:66-67 against the other 12 defs; receiver census shows subprocess.run x194 vs a local git.run x2",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 43
  },
  {
   "query": "the entry point that parses argv and returns an exit code",
   "expected_file": "tools/codebase-map/reuse_lookup.py",
   "expected_symbol": "main",
   "why_it_is_a_real_seam": "IT IS NOT, and no scoring should reward recalling it. Thirty-eight per-file CLI bodies with no shared contract; nothing imports another file's main. It carries the highest fan-in in the whole population, so it is the purest test that a re-ranker demotes a high-fan-in non-seam.",
   "name_class": "common-word",
   "id": "ADV-18",
   "adversarial_role": "control-correct-demotion",
   "expected_line": 457,
   "also_acceptable": [],
   "same_name_definers": 35,
   "same_name_definer_files": [
    "tools/check-kit-placeholders.py",
    "tools/check-spec-tokens.py",
    "tools/codebase-map/gen_map.py",
    "tools/codebase-map/map_diff.py",
    "tools/codebase-map/reuse_lookup.py",
    "tools/codebase-map/selftest.py",
    "tools/drift-audit/drift_report.py",
    "tools/drift-audit/selftest.py",
    "tools/gate-lint/ps-hygiene.py",
    "tools/govkit/census.py",
    "tools/govkit/check_runbook_parity.py",
    "tools/govkit/fixtures/make_incms_receipt.py",
    "tools/govkit/govkit.py",
    "tools/govkit/matrix.py",
    "tools/govkit/refusal_join.py",
    "tools/govkit/selftest.py",
    "tools/lexicon/lexicon.py",
    "tools/lexicon/scaffold_lexicon.py",
    "tools/memory-recall/bench.py",
    "tools/memory-recall/check-recall.py",
    "tools/memory-recall/extract.py",
    "tools/memory-recall/query.py",
    "tools/memory-recall/recall_conf.py",
    "tools/memory-recall/selftest.py",
    "tools/memory-recall/test_recall_floor.py",
    "tools/memory-recall/union.py",
    "tools/memory-tree/check-arms.py",
    "tools/memory-tree/corpus_ids.py",
    "tools/memory-tree/gen_build_index.py",
    "tools/memory-tree/gotchas.py",
    "tools/memory-tree/merge-rows.py",
    "tools/memory-tree/row_grammar.py",
    "tools/playbook/render_playbook.py",
    "tools/run-gates/profile_bar.py",
    "tools/settings-merge.py"
   ],
   "shipped_fan_in": 37,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": false,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 38,
    "doc_freq_text_corpus": 580,
    "tier_identifier_index": 1,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 35,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "rl": 1,
     "md": 1,
     "_dr": 1
    }
   },
   "established_by": "38 defs enumerated from ast; zero cross-file bare references beyond each file's own __main__ guard",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 52
  },
  {
   "query": "merge two sides of a conflicted append-only log without picking a side",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "merge",
   "why_it_is_a_real_seam": "This is the row-keyed merge driver the playbook mandates for an authored index several nodes append to. The collision is that tools/settings-merge.py also defines merge, for splicing a hook fragment into a settings JSON, an unrelated operation. A name-merged candidate row cannot tell a session which of the two it is offering.",
   "name_class": "common-word",
   "id": "ADV-19",
   "adversarial_role": "harm-collision",
   "expected_line": 1018,
   "also_acceptable": [],
   "same_name_definers": 3,
   "same_name_definer_files": [
    "tools/codebase-map/reuse_lookup.py",
    "tools/memory-tree/merge-rows.py",
    "tools/settings-merge.py"
   ],
   "shipped_fan_in": 2,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 3,
    "doc_freq_text_corpus": 742,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 3,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:1018 and tools/settings-merge.py:138",
   "shipped_rank": 2,
   "shipped_points_at_file": "tools/settings-merge.py",
   "shipped_file_correct": false,
   "shortlist_len": 46
  },
  {
   "query": "drop the conflict regions from a merged file to see what the author reads as decided",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "settled",
   "why_it_is_a_real_seam": "Its docstring records a reproduced defect: running the postconditions on the raw output instead of on settled let one unrelated both-sides row edit switch the duplicate detector off for the whole file, and the duplicate was then written OUTSIDE the markers. The seam encodes a fix somebody would otherwise re-lose.",
   "name_class": "common-word",
   "id": "ADV-20",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 286,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 0,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 1,
    "doc_freq_text_corpus": 143,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:286-310",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 96
  },
  {
   "query": "count how many times each row line appears, ignoring line-ending differences",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "census",
   "why_it_is_a_real_seam": "Keyed on the stripped text on purpose: the driver's newline contract means a CRLF region survives as CRLF, so a raw-byte census answers 'not a duplicate' for the same row arriving from a CRLF side and an LF side. A hand-rolled Counter over raw lines reproduces that exact miss.",
   "name_class": "common-word",
   "id": "ADV-21",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 311,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 1,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 2,
    "doc_freq_text_corpus": 152,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 2,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:311-330",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 57
  },
  {
   "query": "replace every record row with a placeholder so a structural diff sees only the shape",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "skeleton",
   "why_it_is_a_real_seam": "It owns site 5 of the newline contract: bodies rather than lines, because a row substituted back takes the terminator of the TOKEN's position in the merged skeleton, and carrying the source terminator any further is what fuses two records onto one line when the merge relocates a formerly-final row.",
   "name_class": "common-word",
   "id": "ADV-22",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 590,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 0,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 1,
    "doc_freq_text_corpus": 49,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:590-605",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 75
  },
  {
   "query": "work out which heading each record sits under across a whole file",
   "expected_file": "tools/memory-tree/merge-rows.py",
   "expected_symbol": "sections",
   "why_it_is_a_real_seam": "Scans the WHOLE file including the preamble on purpose: memory/DECISIONS.md opens its first PLAY heading before the first anchored row, so a scan scoped to the rows reports None for every PLAY row and sees no misfiling when one moves out.",
   "name_class": "common-word",
   "id": "ADV-23",
   "adversarial_role": "harm-low-fanin",
   "expected_line": 388,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/merge-rows.py"
   ],
   "shipped_fan_in": 0,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 1,
    "doc_freq_text_corpus": 206,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/merge-rows.py:388-400",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 66
  },
  {
   "query": "grade an identifier's leading verb against the declared table",
   "expected_file": "tools/lexicon/subtokens.py",
   "expected_symbol": "leading_verb",
   "why_it_is_a_real_seam": "The one place that decides what token P1 grades: it strips dunder and single-underscore prefixes first, and returns empty for a name with no word characters, which the caller MUST treat as ungradeable rather than as a violation. drift_report.py depends on that contract by name in a comment.",
   "name_class": "compound-rare",
   "id": "ADV-24",
   "adversarial_role": "control-signal-agrees",
   "expected_line": 29,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/lexicon/subtokens.py"
   ],
   "shipped_fan_in": 4,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": true,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 5,
    "doc_freq_text_corpus": 21,
    "tier_identifier_index": 3,
    "tier_text_corpus": 2
   },
   "edge_split": {
    "bare_name_files": 2,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "lex": 4
    }
   },
   "established_by": "read tools/lexicon/subtokens.py:31-38; callers lexicon.py:575,801,1090 and drift_report.py:836,1053,1065",
   "shipped_rank": 1,
   "shipped_points_at_file": "tools/lexicon/subtokens.py",
   "shipped_file_correct": true,
   "shortlist_len": 52
  },
  {
   "query": "find this repo's root from inside a copy-installed kit",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "repo_root",
   "why_it_is_a_real_seam": "Anchored on the kit file rather than the cwd, with an env override, because the kit dir lives at any prefix inside an adopter and a throwaway-repo test that copies the kit in must resolve to that repo. Four per-kit definers, same contract. It is the highest-confidence real seam in the set and exists to prove the signal is not merely anti-correlated with fan-in.",
   "name_class": "compound-rare",
   "id": "ADV-25",
   "adversarial_role": "control-signal-agrees",
   "expected_line": 113,
   "also_acceptable": [
    "tools/memory-recall/recall_conf.py::repo_root"
   ],
   "same_name_definers": 4,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py",
    "tools/drift-audit/drift_report.py",
    "tools/govkit/govkit.py",
    "tools/memory-recall/recall_conf.py"
   ],
   "shipped_fan_in": 13,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": true,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 14,
    "doc_freq_text_corpus": 47,
    "tier_identifier_index": 3,
    "tier_text_corpus": 2
   },
   "edge_split": {
    "bare_name_files": 4,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 13,
     "recall_conf": 5,
     "_G": 1
    }
   },
   "established_by": "read tools/codebase-map/map_lib.py:113-119 and tools/memory-recall/recall_conf.py:50-60",
   "shipped_rank": 1,
   "shipped_points_at_file": "tools/memory-recall/recall_conf.py",
   "shipped_file_correct": true,
   "shortlist_len": 92
  },
  {
   "query": "count how many files reference a symbol",
   "expected_file": "tools/codebase-map/map_lib.py",
   "expected_symbol": "fan_in",
   "why_it_is_a_real_seam": "The ranking primitive under test, and its own docstring already declares the limitation this scenario set exists to measure: an import/identifier-scoped HEURISTIC, not a resolved call graph, which over-counts a common id. Shared by the lookup's hot-seam ranking and by --converge.",
   "name_class": "compound-rare",
   "id": "ADV-26",
   "adversarial_role": "control-signal-agrees",
   "expected_line": 823,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/codebase-map/map_lib.py"
   ],
   "shipped_fan_in": 3,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": true,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 4,
    "doc_freq_text_corpus": 23,
    "tier_identifier_index": 3,
    "tier_text_corpus": 2
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "m": 8
    }
   },
   "established_by": "read tools/codebase-map/map_lib.py:823-829",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 47
  },
  {
   "query": "extract the functions, types and imports declared in one source file",
   "expected_file": "tools/lexicon/lexicon.py",
   "expected_symbol": "extract",
   "why_it_is_a_real_seam": "Returns (functions, types, imports) for one file, or None when the mode declares no extractor, and that None is the coverage-mode contract the playbook requires: an undeclared language is a named refusal, never a silent skip. A caller that returns an empty tuple instead of None converts the refusal into green-by-absence.",
   "name_class": "common-word",
   "id": "ADV-27",
   "adversarial_role": "harm-if-demoted",
   "expected_line": 272,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/lexicon/lexicon.py"
   ],
   "shipped_fan_in": 7,
   "seam_by_shipped_threshold": true,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 8,
    "doc_freq_text_corpus": 155,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 3,
    "kwarg_label_files": 0,
    "attribute_receivers": {
     "lex": 3,
     "lx": 1
    }
   },
   "established_by": "read tools/lexicon/lexicon.py:272; three lex.extract / lx.extract sites",
   "shipped_rank": 1,
   "shipped_points_at_file": "tools/lexicon/lexicon.py",
   "shipped_file_correct": true,
   "shortlist_len": 79
  },
  {
   "query": "get the text-only view of a document with fenced blocks removed",
   "expected_file": "tools/memory-tree/gen_build_index.py",
   "expected_symbol": "unfenced",
   "why_it_is_a_real_seam": "'The text-only view, kept as the one fence machine's facade rather than a second copy.' Its fan-in is ZERO by the tool's own measure because its only consumer is its own module, yet it is explicitly documented as the facade nobody should duplicate. Fan-in cannot represent this seam at all, at any ranking.",
   "name_class": "common-word",
   "id": "ADV-28",
   "adversarial_role": "harm-zero-fanin",
   "expected_line": 321,
   "also_acceptable": [],
   "same_name_definers": 1,
   "same_name_definer_files": [
    "tools/memory-tree/gen_build_index.py"
   ],
   "shipped_fan_in": 0,
   "seam_by_shipped_threshold": false,
   "confidence": {
    "signals": {
     "not_ambient": true,
     "compound": false,
     "rare_by_identifier_index": true,
     "rare_by_text_corpus": false
    },
    "doc_freq_identifier_index": 1,
    "doc_freq_text_corpus": 29,
    "tier_identifier_index": 2,
    "tier_text_corpus": 1
   },
   "edge_split": {
    "bare_name_files": 1,
    "kwarg_label_files": 0,
    "attribute_receivers": {}
   },
   "established_by": "read tools/memory-tree/gen_build_index.py:321-323",
   "shipped_rank": null,
   "shipped_points_at_file": null,
   "shipped_file_correct": false,
   "shortlist_len": 58
  }
 ],
 "$shipped_baseline": {
  "measured_on": "the shipped assemble_shortlist, seeds-first then fan-in desc then name",
  "recall_any_rank": "11/28",
  "recall_at_5": 11,
  "recall_at_10": 11,
  "file_correct_when_surfaced": 9,
  "note": "a MISS is a recall failure upstream of any ranking; re-ordering cannot fix one"
 }
}
```
