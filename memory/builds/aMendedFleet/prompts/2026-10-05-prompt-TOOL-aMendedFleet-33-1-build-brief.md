# Build brief — TOOL-aMendedFleet-33

**Serves:** journal TOOL-aMendedFleet-33

The build's shared brief, `2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md`, binds this pass
in full; read it first. This brief adds one stale figure the spec did not list.

- `tools/memory-recall/recall_conf.py` (near line 180) still types "one cache here is 2.4 MB". Unit 32
  removed the same figure from `.memory-tree.conf` and found this second copy outside its write set.
  It is a stale typed figure of exactly this unit's class: drop or point it at its source in this
  pass, widening the `--dispatch` write set to include the file.
