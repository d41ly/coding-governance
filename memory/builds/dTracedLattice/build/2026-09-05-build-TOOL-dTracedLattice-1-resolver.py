# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
"""A stdlib-ast import+reference resolver prototype over the SAME file set the heuristic scans.
Measures: how much of a true reference graph is reachable with `ast` alone, and what necessarily
falls back to the token heuristic."""
from __future__ import annotations
import ast, collections, json, sys
from pathlib import Path
import harness as h

ROOT = h.ROOT
rows = h.symbols()
sym_files = sorted({r["file"] for r in rows})
scanned = [p.relative_to(ROOT).as_posix() for p in h.scanned_files()]
py = [f for f in scanned if f.endswith(".py")]
js = [f for f in scanned if f.endswith(".js")]

# defs from symbols.json (the map's own export set) + a full ast def set (incl. private names)
defs_by_file = collections.defaultdict(set)
for r in rows:
    defs_by_file[r["file"]].add(r["id"])

trees = {}
for f in py:
    try:
        trees[f] = ast.parse((ROOT / f).read_text(encoding="utf-8"), filename=f)
    except SyntaxError as e:
        print("PARSE FAIL", f, e, file=sys.stderr)

# every top-level + nested def/class name per file (ast ground truth for "what this file defines")
astdefs = collections.defaultdict(set)
for f, t in trees.items():
    for n in ast.walk(t):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            astdefs[f].add(n.name)

# module name -> file, resolved the way this repo's sys.path.insert(kit_dir) actually works
mod_to_file = collections.defaultdict(set)
for f in py:
    mod_to_file[Path(f).stem].add(f)

edges = collections.defaultdict(set)          # (symbol_id) -> {referencing file}
resolved_sites = 0
alias_sites = collections.Counter()
unresolved_attr = collections.Counter()       # receiver token -> count of attr accesses we can't bind
bare_name_hits = 0
subprocess_scripts = collections.Counter()
import_edges = collections.Counter()          # file -> #repo modules imported
extern_import = collections.Counter()

for f, t in trees.items():
    d = Path(f).parent.as_posix()
    modalias = {}   # alias -> target file
    namebind = {}   # local name -> (target file, orig name)
    for n in ast.walk(t):
        if isinstance(n, ast.Import):
            for a in n.names:
                cands = {c for c in mod_to_file.get(a.name.split(".")[0], set()) if Path(c).parent.as_posix() == d}
                if cands:
                    modalias[a.asname or a.name.split(".")[0]] = sorted(cands)[0]
                    import_edges[f] += 1
                else:
                    extern_import[a.name.split(".")[0]] += 1
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
            cands = {c for c in mod_to_file.get(n.module.split(".")[0], set()) if Path(c).parent.as_posix() == d}
            if cands:
                tgt = sorted(cands)[0]
                import_edges[f] += 1
                for a in n.names:
                    namebind[a.asname or a.name] = (tgt, a.name)
            else:
                extern_import[n.module.split(".")[0]] += 1
    for n in ast.walk(t):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name):
            base = n.value.id
            if base in modalias:
                tgt = modalias[base]
                if n.attr in astdefs.get(tgt, set()) or n.attr in defs_by_file.get(tgt, set()):
                    edges[n.attr].add(f); resolved_sites += 1; alias_sites[base] += 1
                else:
                    edges[n.attr].add(f); resolved_sites += 1  # module-level const/var
            else:
                unresolved_attr[base] += 1
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            if n.id in namebind:
                tgt, orig = namebind[n.id]
                edges[orig].add(f); resolved_sites += 1; bare_name_hits += 1
        elif isinstance(n, ast.Call):
            fn = n.func
            nm = getattr(fn, "attr", None) or getattr(fn, "id", None)
            if nm in ("run", "check_call", "check_output", "Popen"):
                for a in ast.walk(n):
                    if isinstance(a, ast.Constant) and isinstance(a.value, str) and (a.value.endswith(".py") or a.value.endswith(".sh")):
                        subprocess_scripts[a.value] += 1

out = dict(
    py_files=len(py), js_files=len(js), parsed=len(trees),
    resolved_sites=resolved_sites, bare_name_hits=bare_name_hits,
    unresolved_attr_sites=sum(unresolved_attr.values()),
    edges={k: sorted(v) for k, v in edges.items()},
)
json.dump(out, open("resolver.json", "w"), indent=0)
print(f"python files scanned: {len(py)}  parsed OK: {len(trees)}  js files (unparsed by ast): {len(js)}")
print(f"intra-repo import statements resolved: {sum(import_edges.values())} across {len(import_edges)} files")
print(f"resolved reference sites (module-alias attr + from-import name): {resolved_sites} "
      f"(of which bare from-import names: {bare_name_hits})")
print(f"attribute sites with an UNRESOLVED receiver: {sum(unresolved_attr.values())}")
print("top unresolved receivers:", unresolved_attr.most_common(12))
print("subprocess-invoked scripts seen as string constants:", sum(subprocess_scripts.values()),
      subprocess_scripts.most_common(6))
print("top external module imports:", extern_import.most_common(10))
