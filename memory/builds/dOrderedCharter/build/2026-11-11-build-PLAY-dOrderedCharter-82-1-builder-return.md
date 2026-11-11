# dOrderedCharter — unit 82's builder return

**Serves:** journal PLAY-dOrderedCharter-82

Runs wf_8d330831-103 and wf_ad78e485-066, summarized from their returns.

- The first run built rev-1, the matrix leg's guard widened file by file, and handed back without a commit: that guard made the
  spec-token join red on another build's open spec, which lists one of the guarded files. The spec's rev-2 removed the cause
  instead, and the second run built it as pass commit `a5741d9ad` with no divergence.
- What landed: the renderer gains a flag that prints the placeholder keys filling one-line bullet regions, and the matrix reads
  them from a child process instead of importing the renderer, so the matrix leg's import closure is back to the two govkit
  files and its guard is unchanged.
- Probes it ran, none a gate: the flag's output and both refusal paths, the stub probe, the matrix helper raising on a failed
  child, and a grep showing the import gone.
- The main loop then ran the legs the close's three fix units trip, over the pass: python reads, install-prefix, govkit
  selfcheck, harness arms, runbook parity, kit epoch and the acceptance matrix all exit 0; dead-path carriers reds only on gov's
  install receipt, which the lander rewrites.
- Owed to the close: every leg on the gates line. Two new refusal sites carry no arm: the flag's refusal and the matrix's error on
  a failed child.
