# TOOL-dAlignedCarrier-2 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-2

The protocol's `gates-green` row now says the full bar ran on the landed tip and its verdict is one
the inherited-red policy of `UNATTENDED-STOPS.md` §13 lands, and the no-override paragraph of §4 ends
by naming check 83 and that section as where a `gates-green` override is refused. The template was
re-copied to its render by the adopter. Greps, a byte comparison, the adopter's `--check`, the size
checker and one scoped kit-gate run stood in for the `unattended protocol size`, `unattended skill
wiring` and `unattended kit gate` legs; no suite ran.

**Evidences:** TOOL-dAlignedCarrier-2
- AC1 — `grep -c 'on the tip being landed and passed'` — printed 0 over the render after the pass
  and 1 over the BASE blob; the `^| .gates-green. |` grep printed one row, line 343, naming
  `UNATTENDED-STOPS.md` and §13.
- AC2 — `grep -c 'check 83'` — printed 1 over the render after the pass and 0 over the BASE blob;
  the `awk` range from the no-override paragraph's opening sentence printed seven lines whose last
  sentence names check 83 and `UNATTENDED-STOPS.md` §13.
- AC3 — `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` — exited 0
  after the adopter's render, and `bash tools/unattended/adopt-unattended.sh --check` exited 0
  printing `in sync`.
- AC4 — `template-size OK — UNATTENDED-PROTOCOL.md: 65301 / 65692 bytes` — the size checker
  exited 0; `wc -c` read 65110 at BASE and 65301 after the pass, a growth of 191 bytes against the
  300-byte share.
- AC5 — `rc=0 secs=583` — `bash tools/unattended/check-unattended.sh --skip 28` over the staged
  pass tree exited 0 after 583 s and its log held no `FAILED` line. The unscoped leg, the 28
  region's verdict and the grading of this commit's writes against its declaration are the close
  bar's.
