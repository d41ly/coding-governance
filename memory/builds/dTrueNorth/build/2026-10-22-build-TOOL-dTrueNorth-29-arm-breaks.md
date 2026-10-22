**Serves:** journal TOOL-dTrueNorth-29

# TOOL-dTrueNorth-29 — the staged breaks the close's arm observations used

The arm observations BUILD-METHOD owes each `New arm:` line ran in scratch clones of `e583a7f42` on node d. A break is a text replacement confined to one function, applied by `mutate.py` below; a splice puts each function a unit's pass changed back to its pre-pass text with `splice.py`. Each unit's ledger records what its breaks redded; the green half is `92a0dcb96`.

## The breaks

```json
{
 "u9-three-value-expand": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "_expand_ids",
  "old": "    return ids, bad\n",
  "new": "    return ids, bad, {}\n"
 },
 "u16-pair-contract": {
  "file": "tools/memory-tree/backlog.py",
  "func": "read_header_verbs",
  "old": "        if not (isinstance(got, tuple) and len(got) == 2):",
  "new": "        if False:"
 },
 "u4-kind-name-join": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "read_bindings",
  "old": "if named and rec[\"state\"] in (\"bound\", \"unbound\") and rec[\"kind\"] != \"deviation\":",
  "new": "if False:"
 },
 "u4-name-grammar": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "read_bindings",
  "old": "elif rec[\"kind\"] == \"deviation\" and not deviation_name.match(rel):",
  "new": "elif False:"
 },
 "u4-kind-token": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "",
  "old": "\"journal\", \"research\", \"deviation\")",
  "new": "\"journal\", \"research\")"
 },
 "u8-record-input": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "check_index_input",
  "old": "    return len(parts) >= 3 and parts[1] in RECORD_KINDS\n",
  "new": "    return len(parts) >= 3 and parts[1] in RECORD_KINDS and \"-deviation-\" not in rel\n"
 },
 "u17-kit-input": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "check_index_input",
  "old": "    if kit and (rel == kit or rel.startswith(kit + \"/\")):\n",
  "new": "    if False:\n"
 },
 "u27-usage": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "main",
  "old": "    if with_verdicts and (mode != \"--check\" or \"--staged\" in argv[2:]):",
  "new": "    if False:"
 },
 "u27-sections": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "print_check_verdicts",
  "old": "    print(\"build-index: verdicts end\")",
  "new": "    pass"
 },
 "u27-head-names": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "derive_head_names",
  "old": "    if not unit:\n        raise DesignRefusal(",
  "new": "    if not unit and False:\n        raise DesignRefusal("
 },
 "u23-leaks": {
  "file": "tools/memory-tree/tree_lib.py",
  "func": "",
  "old": "    \"GIT_LITERAL_PATHSPECS\",\n    \"GIT_GLOB_PATHSPECS\",\n    \"GIT_NOGLOB_PATHSPECS\",\n    \"GIT_ICASE_PATHSPECS\",\n)",
  "new": ")"
 },
 "u8-view-records": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "render_asbuilt_view",
  "old": "asbuilt_view.render_view(sha, clauses, records, rel)",
  "new": "asbuilt_view.render_view(sha, clauses, [], rel)"
 },
 "u3-no-pair": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "plan",
  "old": "if coverage[\"state\"] == \"armed\":",
  "new": "if False:"
 },
 "u3-verb-never-refuses": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "cmd_check_coverage",
  "old": "    return 1 if refused else 0",
  "new": "    return 0"
 },
 "u3-carries-input": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "check_index_input",
  "old": "    if carries and rel == carries:\n",
  "new": "    if False:\n"
 },
 "u16-stub-ignored": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "read_carries_coverage",
  "old": "            if resolve is not None:\n                derive = resolve(path)",
  "new": "            if False:\n                derive = resolve(path)"
 },
 "u27-head-fixed": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "derive_head_names",
  "old": "    return unit, f\"build/{date}-build-{unit}-asbuilt.py\"",
  "new": "    return \"PLAY-dClosedLoop-1\", \"build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py\""
 },
 "u18-later-path-head": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "resolve_clause_rows",
  "old": "        if len({(r.get(\"after\") or \"\").strip() for r, _row in members}) > 1:",
  "new": "        if False:"
 },
 "u18-no-stray": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "resolve_clause_rows",
  "old": "        stray = [(r[\"id\"], r[\"supersedes\"]) for r, _row in members\n                 if r.get(\"supersedes\") and r[\"supersedes\"] not in ids]",
  "new": "        stray = []"
 },
 "u23-own-spawn": {
  "file": "tools/memory-tree/row_grammar.py",
  "func": "derive_first_seen",
  "old": "out = read_git_output(root, [\"log\",",
  "new": "out = (lambda a: __import__(\"subprocess\").run([\"git\"] + a, cwd=root, capture_output=True).stdout)([\"log\","
 },
 "u23-table": {
  "file": "tools/memory-tree/gen_build_index.py",
  "func": "scan_glob_readers",
  "old": "    return sorted(found)",
  "new": "    return sorted(found)[1:]"
 },
 "u6-checkview": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "check_view",
  "old": "    return findings\n",
  "new": "    return []\n"
 },
 "u27-ref": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_decision_ref",
  "old": "    if refusal:\n        return None, refusal\n",
  "new": "    if False:\n        return None, refusal\n"
 },
 "u18-supersedes-any": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_record",
  "old": "    if supersedes is not None and not named:",
  "new": "    if False:"
 },
 "u4-material": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "check_material",
  "old": "    return extract_authored(before) != extract_authored(after)",
  "new": "    return True"
 },
 "u4-approver": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "check_approver",
  "old": "    a = (rec[\"approver\"] or \"\").strip()",
  "new": "    return None\n    a = (rec[\"approver\"] or \"\").strip()"
 },
 "u12-stub-ignored": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_gen_region_awk",
  "old": "(resolve or backlog.resolve_kit_dir)(",
  "new": "(backlog.resolve_kit_dir)("
 },
 "u16-pipe": {
  "file": "tools/memory-tree/asbuilt_view.py",
  "func": "resolve_clause_rows",
  "old": "        piped = [r[\"id\"] for r, _row in members if \"|\" in (r.get(\"after\") or \"\")]",
  "new": "        piped = []"
 },
 "u16-pin-commit": {
  "file": "tools/memory-tree/design_lib.py",
  "func": "read_design_keys",
  "old": "    if run_git(root, \"cat-file\", \"-e\", f\"{pin}^{{commit}}\").returncode:",
  "new": "    if False:"
 },
 "u20-awk-count": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_gen_region_awk",
  "old": "    if len(found) != 1:\n",
  "new": "    if False:\n"
 },
 "u24-file-pickaxe": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "",
  "old": "read_row_commit(root, m.group(0), scope)",
  "new": "read_row_commit(root, m.group(0), rel)"
 },
 "u26-untracked": {
  "file": "tools/memory-tree/design_lib.py",
  "func": "read_tracked_builds",
  "old": "r = run_git(root, \"ls-files\", \"-z\", \"--\", f\"{memory_root}/builds\")",
  "new": "r = run_git(root, \"ls-files\", \"-z\", \"--cached\", \"--others\", \"--\", f\"{memory_root}/builds\")"
 },
 "u16-dj-pipe": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_record",
  "old": "        if key == \"After\" and \"|\" in value:",
  "new": "        if False:"
 },
 "u16-trailer-ignored": {
  "file": "tools/memory-tree/deviation_join.py",
  "func": "read_first_passes",
  "old": "        if c[\"trailer\"]:",
  "new": "        if False:"
 }
}
```

## mutate.py

```python
"""Apply named staged breaks to the arm clone. Each break is a text replacement confined to one
top-level function's span (or the whole file when `func` is empty), applied exactly once.

usage: python mutate.py <clone> <breaks.json> <id> [<id> ...]
breaks.json: {"<id>": {"file": "...", "func": "...", "old": "...", "new": "..."}, ...}
Restore with `git -C <clone> checkout -- .`.
"""
import ast
import json
import sys

clone, spec = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
for bid in sys.argv[3:]:
    b = spec[bid]
    path = f"{clone}/{b['file']}"
    src = open(path, encoding="utf-8", newline="").read()
    lo, hi = 0, len(src)
    if b.get("func"):
        tree = ast.parse(src)
        node = next((n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                     and n.name == b["func"]), None)
        if node is None:
            sys.exit(f"{bid}: no function {b['func']} in {b['file']}")
        lines = src.split(chr(10)) and [x + chr(10) for x in src.split(chr(10))]
        lo = sum(len(x) for x in lines[: node.lineno - 1])
        hi = sum(len(x) for x in lines[: node.end_lineno])
    seg = src[lo:hi]
    if seg.count(b["old"]) != 1:
        sys.exit(f"{bid}: `old` occurs {seg.count(b['old'])} times in {b['file']}:{b.get('func') or '*'}")
    src = src[:lo] + seg.replace(b["old"], b["new"]) + src[hi:]
    open(path, "w", encoding="utf-8", newline="").write(src)
    if path.endswith(".py"):
        compile(src, path, "exec")
    print(f"staged {bid}: {b['file']}:{b.get('func') or '*'}")
```

## splice.py

```python
"""Stage one unit's break in the arm clone: every top-level product function the unit changed goes
back to its text at the unit's base (the parent of its first Pass commit); every function the unit
added becomes a stub raising, as at a base that lacked it. Shell files the unit changed go back whole.

usage: python splice.py <clone> <unit-number> [--files a,b]   (prints what it staged)
Restore with `git -C <clone> checkout -- .`.
"""
import ast
import subprocess
import sys

SKIP_PREFIX = ("test_", "run_", "cmd_selftest", "_arm", "arm", "_fixture", "fixture", "plant", "_plant",
               "selftest", "_selftest", "make_fixture", "build_fixture", "main")


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, encoding="utf-8",
                          check=True).stdout


def funcs(src):
    out = {}
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    lines = src.split(chr(10)) and [x + chr(10) for x in src.split(chr(10))]
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = (node.decorator_list[0].lineno if node.decorator_list else node.lineno) - 1
            out[node.name] = (start, node.end_lineno, "".join(lines[start:node.end_lineno]))
    return out


def main():
    clone, n = sys.argv[1], sys.argv[2]
    only = None
    if "--files" in sys.argv:
        only = set(sys.argv[sys.argv.index("--files") + 1].split(","))
    shas = git(clone, "log", "--format=%H", "--reverse", f"--grep=^Pass: TOOL-dTrueNorth-{n}$",
               "271aa59de..HEAD").split()
    if not shas:
        sys.exit(f"no Pass commit for unit {n}")
    base, last = shas[0] + "^", shas[-1]
    files = set()
    for s in shas:
        files.update(git(clone, "show", "--format=", "--name-only", s).split())
    files = sorted(f for f in files if f.startswith("tools/") and ".test." not in f
                   and not f.endswith(("selftest.py", ".md", ".json", ".js", ".toml", ".txt")))
    if only:
        files = [f for f in files if f in only]
    for f in files:
        try:
            old = git(clone, "show", f"{base}:{f}")
        except subprocess.CalledProcessError:
            old = None
        new = git(clone, "show", f"{last}:{f}")
        path = f"{clone}/{f}"
        if f.endswith(".sh"):
            if old is not None and old != new:
                open(path, "w", encoding="utf-8", newline="").write(old)
                print(f"staged {f}: whole file at {base[:9]}")
            continue
        if not f.endswith(".py"):
            continue
        fo, fn = funcs(old or ""), funcs(new)
        changed = [k for k in fn if not k.startswith(SKIP_PREFIX) and not any(w in k for w in ('fixture', 'plant', 'selftest', '_arm'))
                   and (k not in fo or fo[k][2] != fn[k][2])]
        head = open(path, encoding="utf-8", newline="").read()
        fh = funcs(head)
        edits = []
        for k in changed:
            if k not in fh:
                continue
            s, e, text = fh[k]
            if k in fo:
                repl = fo[k][2]
                how = "base text"
            else:
                node = ast.parse(text).body[0]
                indent = " " * (node.body[0].col_offset)
                sig = text[: text.index(":\n", text.index("def ")) + 2] if ":\n" in text else text.splitlines(True)[0]
                repl = sig + f"{indent}raise RuntimeError('staged break: {k} is absent at the base of TOOL-dTrueNorth-{n}')\n"
                how = "absent stub"
            edits.append((s, e, repl, k, how))
        lines = [x + chr(10) for x in head.split(chr(10))]
        for s, e, repl, k, how in sorted(edits, reverse=True):
            if not repl.endswith("\n"):
                repl += "\n"
            lines[s:e] = [repl]
        open(path, "w", encoding="utf-8", newline="").write("".join(lines))
        print(f"staged {f}: " + ", ".join(f"{k} ({how})" for _, _, _, k, how in sorted(edits)))
        try:
            compile("".join(lines), path, "exec")
        except SyntaxError as exc:
            print(f"  WARN {f} no longer compiles: {exc}")


main()
```

## The runs

```
A-u9: STAGE FAILED u9-three-value-expand: `old` occurs 0 times in tools/memory-tree/gen_build_index.py:_expand_ids
A-u16pair: 1 of 1 arms matching (TOOL-dTrueNorth-16 AC15) red · 1 red overall · breaks u16-pair-contract
A-u4: 3 of 3 arms matching (TOOL-dTrueNorth-4) red · 3 red overall · breaks u4-kind-name-join u4-name-grammar u4-kind-token
A-u8: STAGE FAILED u8-record-input: `old` occurs 0 times in tools/memory-tree/gen_build_index.py:check_index_input
A-u17: STAGE FAILED u17-kit-input: `old` occurs 0 times in tools/memory-tree/gen_build_index.py:check_index_input
A-u27: STAGE FAILED u27-head-names: `old` occurs 0 times in tools/memory-tree/asbuilt_view.py:derive_head_names
A-u23: STAGE FAILED u23-leaks: `old` occurs 0 times in tools/memory-tree/tree_lib.py:*
green-A rc=0 PASS — gen_build_index: all arms held
A-u9: 3 of 3 arms matching (TOOL-dTrueNorth-9) red · 47 red overall · breaks u9-three-value-expand
A-u8: 0 of 3 arms matching (TOOL-dTrueNorth-8) red · 1 red overall · breaks u8-record-input
A-u17: 1 of 2 arms matching (TOOL-dTrueNorth-17) red · 4 red overall · breaks u17-kit-input
A-u27: 4 of 5 arms matching (TOOL-dTrueNorth-27) red · 4 red overall · breaks u27-usage u27-sections u27-head-names
A-u23: 2 of 5 arms matching (TOOL-dTrueNorth-23) red · 2 red overall · breaks u23-leaks
A-u8b: 2 of 3 arms matching (TOOL-dTrueNorth-8) red · 10 red overall · breaks u8-view-records
A-u3: 4 of 24 arms matching (TOOL-dTrueNorth-3) red · 6 red overall · breaks u3-no-pair u3-verb-never-refuses u3-carries-input
A-u16b: 2 of 18 arms matching (TOOL-dTrueNorth-16) red · 2 red overall · breaks u16-stub-ignored
A-u27b: 2 of 5 arms matching (TOOL-dTrueNorth-27) red · 2 red overall · breaks u27-head-fixed
A-u18: 3 of 4 arms matching (TOOL-dTrueNorth-18) red · 3 red overall · breaks u18-later-path-head u18-no-stray
A-u23b: 4 of 5 arms matching (TOOL-dTrueNorth-23) red · 4 red overall · breaks u23-own-spawn u23-table
C-av u6 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: render_fixture is absent at the base of TOOL-dTrueNo
C-av u16 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: build_view_fixture is absent at the base of TOOL-dTr
C-av u18 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: ValueError: not enough values to unpack (expected 5, got 4)
C-av u26 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: check_merge_arm is absent at the base of TOOL-dTrueN
C-av u27 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: NameError: name 'REF' is not defined
C-av u6 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: read_view_inputs is absent at the base of TOOL-dTrue
C-av u16 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: NameError: name 'VIEW_KEYS' is not defined. Did you mean: 'VIEW_HEAD'?
C-av u18 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: KeyError: 'instrument'
C-av u26 splice: 1 of 1 own lines red · 1 FAIL lines overall · tail: as-built view selftest: 14 of 15 arm(s) held
C-av u27 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: NameError: name 'REF' is not defined
C-av-u6: 2 of 8 unit-6 lines red · 2 FAIL lines overall · breaks u6-checkview · tail: as-built view selftest: 13 of 15 arm(s) held
C-av-u18: 3 of 4 unit-18 lines red · 3 FAIL lines overall · breaks u18-later-path-head u18-no-stray · tail: as-built view selftest: 12 of 15 arm(s) held
C-av-u27: 1 of 1 unit-27 lines red · 1 FAIL lines overall · breaks u27-head-fixed u27-head-names · tail: as-built view selftest: 14 of 15 arm(s) held
C-av-u16: 0 of 1 unit-16 lines red · 0 FAIL lines overall · breaks u16-stub-ignored · tail: as-built view selftest: 15 of 15 arm(s) held
C-rc-u4: 24 of 86 unit-4 lines red · 43 FAIL lines overall · breaks u4-material u4-approver · tail: routed-commits selftest: 42 arm(s) FAILED
C-rc-u18: 0 of 0 unit-18 lines red · 5 FAIL lines overall · breaks u18-supersedes-any · tail: routed-commits selftest: 4 arm(s) FAILED
C-rc-u27: 1 of 1 unit-27 lines red · 3 FAIL lines overall · breaks u27-ref · tail: routed-commits selftest: 2 arm(s) FAILED
C-rc u12 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: read_gen_region_awk is absent at the base of TOOL-dT
C-rc u16 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: NameError: name 'JOIN_KEYS' is not defined
C-rc u20 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: RuntimeError: staged break: read_blobs_at is absent at the base of TOOL-dTrueNor
C-rc u24 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: ValueError: too many values to unpack (expected 2)
C-rc u26 splice: 0 of 0 own lines red · 0 FAIL lines overall · tail: TypeError: read_decision_rows() missing 1 required positional argument: 'ref'
C-rc-u12: 1 of 2 unit-12 lines red · 5 FAIL lines overall · breaks u12-stub-ignored · tail: routed-commits selftest: 4 arm(s) FAILED
C-rc-u16: 0 of 3 unit-16 lines red · 0 FAIL lines overall · breaks u16-pipe u16-pin-commit · tail: routed-commits selftest: all arms held
C-rc-u20: 1 of 5 unit-20 lines red · 2 FAIL lines overall · breaks u20-awk-count · tail: routed-commits selftest: 1 arm(s) FAILED
C-rc-u24: 1 of 1 unit-24 lines red · 7 FAIL lines overall · breaks u24-file-pickaxe · tail: routed-commits selftest: 6 arm(s) FAILED
C-rc-u26: 1 of 4 unit-26 lines red · 3 FAIL lines overall · breaks u26-untracked · tail: routed-commits selftest: 2 arm(s) FAILED
C-rc-u16b: 1 of 3 unit-16 lines red · 17 FAIL lines overall · breaks u16-dj-pipe u16-trailer-ignored · tail: routed-commits selftest: 16 arm(s) FAILED
```
