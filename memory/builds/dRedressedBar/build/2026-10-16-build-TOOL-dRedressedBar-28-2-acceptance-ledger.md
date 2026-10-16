# TOOL-dRedressedBar-28 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-28

This is the build pass of unit 28, built from spec 28 rev-2 with its §8 F1 resolved as (a). `<w28>`
is `1b1661434`, the spec-writer pass that resolved F1 and took specs 10 and 11 to rev-7. `<p28>` is
the commit this ledger lands in, and `<p28>~1` is `1b1661434`, whose two product files equal
`b1eb9737`'s: `git diff --stat b1eb9737 HEAD` over both printed nothing before the first edit.

The pass commit takes the `must_not_exist` term out of the code-2 `[[outcome]]` block of
settings-merge's descriptor and rewrites the comment above it, respells the measured landing in
unit 14's comment in `govkit.py` through `{prefix}`, moves spec 28's status to CLOSED, and carries
this ledger. The build README's rows, spec 28's records row and `memory/LIVE.md` came from
`gen_build_index.py --write` over the CLOSED header. No function or class moved, so the symbol
index did not.

No merge bar, gate leg or self-test suite was run by this pass. The section 7 legs are owed to the
close, and this unit declares no new arm. Every criterion was observed by a direct probe on this
Windows host under Python 3.12.10, each program saved under the session scratchpad, which sits
under `%TEMP%`, and each scratch target a fresh directory there.

**Evidences:** TOOL-dRedressedBar-28
- AC1 — `ban.py` — the counter probe of spec 28 §4, saved verbatim, run over the tip's
  `tools/govkit/govkit.py` and `tools/govkit/entries/settings-merge.kit.toml`, exited 0 and printed
  one line, the clean summary ending `0 kit-path spelling(s) on 0 line(s)`. Red half: over the two
  files as `git show b1eb9737:<path>` wrote them to the scratchpad, it exited 1, printed the brief's
  two hit lines, at `:7950` and `:48`, against the scratch paths, and ended
  `2 kit-path spelling(s) on 2 line(s)`. The unedited working copy read the same before the edit.
- AC2 — `refusing to wire` — a probe imported `govkit.py`, loaded settings-merge's descriptor with
  `govkit.load_toml` from the tip and from the `1b1661434` copy, and printed the verdict over a
  fresh scratch target per row of spec 28 §4's table. Rows 1 to 10 read the same at both: 1, 6 and
  10 ACCEPTED, the rest REFUSED. Rows 11 and 12 read REFUSED at `<p28>~1` and ACCEPTED at the tip.
  Rows 13 and 14, staged with `_winapi.CreateJunction`, read ACCEPTED and REFUSED at both, as the
  table states. gov's `tools/settings-merge.py`, copied into a scratch target holding `.git` and a
  directory at `tools/hooks/agent-cap.js` and run from its root, exited 2 with
  `refusing to wire agent-cap — tools/no-agent-cap-kit-resolved/agent-cap.js does not exist` on
  stderr, printed nothing on stdout, and wrote nothing. The POSIX residual stays UNVERIFIED.
- AC3 — `check_outcome_probes` — with `matrix.check` replaced by a recorder, the call over a fresh
  scratch directory recorded 39 labels, every one true, at the tip. With `govkit.read_descriptors`
  wrapped to hand back the `1b1661434` descriptor, it recorded the same 39, all true, and the eight
  labels opening `settings-merge exit 2` were the same eight with the same verdicts. Red half: with
  the wrap taking `must_not_resolve` out of the tip's code-2 probe as well, it recorded 36 true and
  3 false, the hook beside it, the prefix's parent home only and a hook only the receipt locates.
- AC4 — `code = 2` — the grep printed one block: `code = 2`, the probe carrying `must_exist` and
  `must_not_resolve` alone, `means = "no-agent-cap-to-wire"` and `ok = true`. The count of
  `must_not_exist =`, `three terms` and `any of the three` printed 0, and 3 over the `b1eb9737`
  copy. The `[adopt]`-to-`[[outcome]]` range carries `must_not_resolve`, `.governance/install.json`
  and `TOOL-dRedressedBar-28`. The diff against `1b1661434`, as committed, touches the six comment
  lines that counted three terms, now eight, and the probe line, and nothing else.
- AC5 — `{prefix}/hooks/agent-cap.js` — `grep -c 'scripts/hooks/agent-cap.js'` over `govkit.py`
  printed 0, and 1 over the `b1eb9737` copy. The receipt block's range carries `prefix = "scripts"`
  and `{prefix}/hooks/agent-cap.js`. The diff's changed lines, filtered of `# ---- ` comment lines,
  printed nothing: two comment lines became three, and no `def` or `class` moved.
- AC6 — `CLOSED · rev-7` — at `<w28>`, the Edges range of spec 10 and of spec 11 each printed one
  hands-off bullet naming this unit. Spec 11's C5 row carries the id, and
  `grep -c 'term may. Each fails closed'` over spec 11 printed 0. Both status headers read
  `CLOSED · rev-7`, each spec's last revision line is rev-7 naming this unit, and
  `git diff --stat 1b1661434~1 1b1661434` names only paths under `memory/builds/dRedressedBar/`.
