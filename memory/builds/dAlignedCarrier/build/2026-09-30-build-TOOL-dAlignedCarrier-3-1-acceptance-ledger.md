# TOOL-dAlignedCarrier-3 — acceptance ledger

**Serves:** journal TOOL-dAlignedCarrier-3

`researched` and `solution-tested` now carry scope `all` in the driver's directive registry and in
the Skill's table, the Skill's three carrier paragraphs say both bind every mode with M12 deciding
when, and protocol §10 states the scope as `all` or an authorization mode with no prompt-only
rationale. Greps, the `scope_of` probe, `cmp`, the adopter's `--check`, the size checker and two
scoped kit-gate runs stood in for the `unattended kit gate`, `unattended skill wiring` and
`unattended protocol size` legs; no suite ran.

**Evidences:** TOOL-dAlignedCarrier-3
- AC1 — `researched:M12` — the `grep -o -E` over the driver printed `researched:M12` and
  `solution-tested:M12` and nothing carrying a third field; over the BASE blob it printed both with
  `:prompt`.
- AC2 — `M12 | all` — the row grep printed 2 over the template and 2 over the render after the
  pass, and 0 over the BASE template.
- AC3 — `UNATTENDED check 16 FAILED` — with the `researched` Scope cell set back to `prompt` and
  staged over the pass tree, `bash tools/unattended/check-unattended.sh --skip 28` exited 1 after
  569 s with that line the only `FAILED` line, naming `researched:all` against `researched:prompt`.
  Restored from a byte-identical scratchpad backup (`cmp` exited 0), then the Scope paragraph's
  prose rewrapped where an edit had joined two lines and the Skill re-rendered, the same run exited
  0 after 547 s with no `FAILED` line, and the adopter's `--check` exited 0 printing `in sync`.
- AC4 — `grep -c -i -E 'scoped .prompt.|not the slug path|two scoped directives'` — printed 0 over
  the template after the pass and 3 over the BASE blob; `grep -n -i 'every mode'` printed lines 151
  and 394, the Scope paragraph and the prompt-path paragraph, each naming M12, where BASE printed 0.
- AC5 — `template-size OK — UNATTENDED-PROTOCOL.md: 65171 / 65692 bytes` — the size checker
  exited 0; the §10 grep printed 0 over the render and 2 over the BASE blob, `cmp` of template and
  render exited 0, and `wc -c` read 65301 before the pass and 65171 after it, 130 bytes smaller.
- AC6 — `researched=all` — the three definitions `sed` printed, written to a scratchpad file and
  sourced with `DIRECTIVES_EXTRA` empty, answered `all`, `all` and `recipe` for `researched`,
  `solution-tested` and `playbook-followed`; the BASE definitions answered `prompt`, `prompt` and
  `recipe`.
- AC7 — `grep -c 'M12 | prompt | D9'` — printed 0 over the kit-gate suite after the pass and 1
  over the BASE blob; the `-A3` read of the `tFresh` `--waive researched` arm shows `preflight OK`
  and `waiver · item researched · reason does not apply here` with no check 45 text. Neither
  suite's RUN was observed: both are waived for this landing by the build README's rule.
