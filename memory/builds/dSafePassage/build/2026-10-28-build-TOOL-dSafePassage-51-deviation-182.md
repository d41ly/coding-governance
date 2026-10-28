# TOOL-dSafePassage-51 deviation 182 — the arm does not run the FIFO plant over the staged `.gitmodules` read copy

**Serves:** deviation TOOL-dSafePassage-51

- **Departs from:** TOOL-dSafePassage-51@rev-4 [§7]
- **Hand-off:** spec-to-code
- **Before:** §7's `New arm:` line stages a `.gitmodules` read copy that spawns its `config -f` read before its `stat`, "which AC9's `ast` half names and under which, on POSIX only, the FIFO plant runs to its bound".
- **After:** `tools/govkit/selftest.py` stages that copy and its `ast` half names it (the `[dSP-51] AC9 ... — reds` check); it does not run `fixture isolation --plant gitmodules-fifo` over the copy on any host. Over the module as built it runs the plant, which exits 1 refused naming `.gitmodules` where `os.mkfifo` exists and prints its `skip —` line elsewhere.
- **Cause:** builder discovery
- **Reason:** over the copy, git's `config -f` opens the FIFO and blocks with no writer; a timeout kills the fixture's python but not that git child, so the suite would leave a blocked process on every POSIX run. Every host this repo runs is Windows (§6 AC9's fixture note), so the run would never execute here either.
- **Evidence:** this unit's acceptance ledger, AC9: the `ast` probe read the module's `os.lstat` and `os.stat` before its one `git` spawn and no `open`, and over the copy the spawn first.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-51, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-59
- **Caused-by:** TOOL-dSafePassage-51
