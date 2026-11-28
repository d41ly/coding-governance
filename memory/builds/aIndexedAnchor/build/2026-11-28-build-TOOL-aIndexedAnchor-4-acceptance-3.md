# TOOL-aIndexedAnchor-4 acceptance 3 — re-run at 01218460

**Serves:** acceptance TOOL-aIndexedAnchor-4

- **Sha:** 01218460099d53393b9df5c2ab120c41a02883c8
- **Writer:** stand-in
- **Caused-by:** TOOL-aIndexedAnchor-4

run · 0 · e3b0c44298fc · bash -c '. tools/lib/resolve-python.sh && $(resolve_python) -c "import pathlib,subprocess,sys,tempfile,tomllib; sys.path.insert(0,\"tools/memory-tree\"); import record_kinds as rk; rows=tomllib.loads(pathlib.Path(sys.argv[1]).read_text(encoding=\"utf-8\"))[\"record-kind\"]; d=tempfile.mkdtemp(); subprocess.run([\"git\",\"init\",\"-q\",d],check=True); pathlib.Path(d,\".git\",\"push-main-active\").touch(); l,r=rk.check_pockets(d,rows); print(chr(10).join(l+r))" tools/memory-tree/record-kinds.toml | grep -q "push-main-active · lander-marker"'
