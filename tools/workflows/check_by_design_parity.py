#!/usr/bin/env python3
"""check_by_design_parity.py — the by-design head the catalogue PRINTS is the head the harness FINDS.

    python <prefix>/<this kit>/check_by_design_parity.py <the memory-tree kit's directory>
    python <prefix>/<this kit>/check_by_design_parity.py --selftest

TOOL-aGraftedHelix-28. The head of the by-design block is spelled twice, in two kits: the memory-tree
kit's `gotchas.py` prints it through `render_by_design` (a Python format string), and this kit's
`tier2-review.template.js` finds it with `BY_DESIGN_HEAD` (a JS regex) in `extractByDesign`. A head
reworded in either makes the harness find no block and log `none supplied`, which a reader takes for
"no invariant touched": a zero that reads as clean. So this RUNS both spellings rather than comparing
them as text, which would need a translator — a third spelling. It imports the catalogue by file
location and calls its own `render_by_design` at each count in `SAMPLE_COUNTS`, then evaluates the
template's one `const BY_DESIGN_HEAD = /…/` literal in `node`, right-trims each head and calls `test`
then `exec` the way `extractByDesign` does. Python's `re` is not used for the pattern: its `\\d` takes
Unicode digits and its `$` matches before a trailing newline, so it is not the harness's behaviour.

PASSES only when the pattern matches every rendered head, captures exactly that head's count, and does
NOT match the count-12 head behind one leading space — `gotchas.py` indents each checklist item's
description, and a description quoting the head must never open a block.

    exit 0  parity, or SKIP: a catalogue with no `render_by_design` and no `invariant` in `KINDS`
            predates the block, renders none, and the harness truthfully logs none
    exit 1  DRIFT, quoting the head and the pattern; a catalogue declaring `invariant` with no
            `render_by_design` is drift too, since a renamed renderer would otherwise skip forever
    exit 2  REFUSING: a template with zero or two declarations, or one not a one-line literal; a
            catalogue that cannot be imported; a renderer that raises; no `node`; evaluator output
            that is malformed or answers any number of heads but the number sent

WHAT THIS DOES NOT CHECK. The block's entry lines (a drifted `- ` makes the harness's count check
refuse before any agent spawns, which is loud). The render `tier2-review.js`, whose identity with the
template is the parity leg's own pair. A pattern loosened but still anchored and still capturing the
digits, whose mis-cut of the entries that count check refuses loudly. A pattern declared in any shape
but a one-line regex literal, which REFUSES here rather than passes. Prose copies of the head.

The catalogue is imported with bytecode writing off, so a run leaves no `__pycache__` beside it.
"""
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile

# Zero is the head every miss prints; twelve is a second, MULTI-DIGIT count, so a pattern capturing
# one digit, or a head that lost its count field, cannot pass. The leading-space negative uses the last.
SAMPLE_COUNTS = (0, 12)
ARMS_DECLARED = 13
# The evaluator, run as `node -e EVALUATOR <template>` with the heads as ASCII-escaped JSON on stdin,
# so no code page ever meets the em dash. RAW, because an escape in a non-raw string reaches the
# regex as a control byte. It answers one JSON object: {refuse} or {pattern, results}.
EVALUATOR = r"""
const fs = require('fs')
const say = (o) => process.stdout.write(JSON.stringify(o))
let heads, lines
try {
  heads = JSON.parse(fs.readFileSync(0, 'utf8'))
  lines = fs.readFileSync(process.argv[1], 'utf8').split(/\r?\n/)
} catch (e) { say({ refuse: 'could not read the heads or the template ' + process.argv[1] + ': ' + e.message }); process.exit(0) }
const decl = lines.filter((l) => /^\s*(?:const|let|var)\s+BY_DESIGN_HEAD\b/.test(l))
if (decl.length !== 1) {
  say({ refuse: process.argv[1] + ' carries ' + decl.length + ' declaration(s) of BY_DESIGN_HEAD, and exactly one is required' })
  process.exit(0)
}
const lit = /^const BY_DESIGN_HEAD = (\/.+\/[a-z]*)\s*;?\s*$/.exec(decl[0])
if (!lit) { say({ refuse: 'the BY_DESIGN_HEAD declaration is not a one-line regex literal: ' + decl[0] }); process.exit(0) }
let re
try { re = new Function('return ' + lit[1])() } catch (e) { say({ refuse: 'the BY_DESIGN_HEAD literal does not evaluate: ' + e.message }); process.exit(0) }
if (!(re instanceof RegExp)) { say({ refuse: 'the BY_DESIGN_HEAD literal is not a RegExp: ' + lit[1] }); process.exit(0) }
say({ pattern: String(re), results: heads.map((h) => {
  const t = String(h).replace(/\s+$/, '')
  if (!re.test(t)) return { matched: false, group: null }
  const m = re.exec(t)
  return { matched: true, group: m && m[1] !== undefined ? m[1] : null }
}) })
"""


def load_checker(mt_dir):
    """Import `<mt_dir>/gotchas.py` by file location -> the module. Raises whatever the import raises."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("by_design_catalogue", pathlib.Path(mt_dir) / "gotchas.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def render_heads(mod):
    """-> the head the catalogue's own renderer prints at each count in SAMPLE_COUNTS: the first
    non-blank line of its block, or '' when it prints none (which no pattern under test matches)."""
    heads = []
    for n in SAMPLE_COUNTS:
        recs = [{"name": f"r{i}", "sections": {}, "decision": f"X-r-{i}"} for i in range(n)]
        heads.append(next((ln for ln in mod.render_by_design(recs) if ln.strip()), ""))
    return heads


def run_pattern(heads, template, node="node", evaluator=EVALUATOR):
    """-> (the pattern's source, one {matched, group} per head). OSError when node cannot start;
    ValueError on a refusal, or on output that is not one well-formed result per head sent."""
    proc = subprocess.run([node, "-e", evaluator, str(template)], input=json.dumps(heads),
                          capture_output=True, encoding="utf-8", errors="replace", timeout=120)
    try:
        out = json.loads(proc.stdout)
    except ValueError:
        raise ValueError(f"the node evaluator's output is not JSON (exit {proc.returncode}): "
                         f"stdout {proc.stdout[:200]!r}, stderr {proc.stderr[:200]!r}") from None
    if isinstance(out, dict) and "refuse" in out:
        raise ValueError(str(out["refuse"]))
    res = out.get("results") if isinstance(out, dict) else None
    good = isinstance(res, list) and all(
        isinstance(r, dict) and isinstance(r.get("matched"), bool) and (r.get("group") is None or isinstance(r["group"], str))
        for r in res)
    if not good or len(res) != len(heads):
        raise ValueError(f"the node evaluator answered {len(res) if good else 'no well-formed'} result(s) "
                         f"for {len(heads)} head(s) sent: {proc.stdout[:200]!r}")
    return str(out.get("pattern")), res


def check_parity(mt_dir, template, node="node", evaluator=EVALUATOR):
    """-> (exit code, verdict lines). 0 parity or SKIP · 1 DRIFT · 2 REFUSING."""
    cat = (pathlib.Path(mt_dir) / "gotchas.py").as_posix()
    tpl = pathlib.Path(template).name  # always the template beside this checker
    try:
        mod = load_checker(mt_dir)
    except (Exception, SystemExit) as exc:  # an import that exits or raises could not run, never a pass
        return 2, [f"REFUSING — the catalogue {cat} could not be imported: {exc!r}"]
    if not callable(getattr(mod, "render_by_design", None)):
        if "invariant" in (getattr(mod, "KINDS", None) or ()):
            return 1, [f"DRIFT — {cat} declares the `invariant` kind in KINDS and defines no render_by_design, "
                       f"so its checklist carries no by-design block and the harness logs `none supplied` "
                       f"for invariants it was never shown"]
        return 0, [f"SKIP — {cat} declares no `invariant` kind and no render_by_design: it renders no "
                   f"by-design block, and the harness truthfully logs none"]
    try:
        heads = render_heads(mod)
    except Exception as exc:
        return 2, [f"REFUSING — {cat}'s render_by_design raised over synthetic records: {exc!r}"]
    sent = heads + [" " + heads[-1]]
    try:
        pat, res = run_pattern(sent, template, node, evaluator)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        return 2, [f"REFUSING — the harness's pattern in {tpl} could not be run: {exc}"]
    drift = []
    for n, head, r in zip(SAMPLE_COUNTS, heads, res):
        if not r["matched"]:
            drift.append(f"DRIFT — the harness's pattern {pat} does not match the head the catalogue renders at count {n}: {head!r}")
        elif r["group"] != str(n):
            drift.append(f"DRIFT — the harness's pattern {pat} matches the count-{n} head {head!r} but captures "
                         f"{r['group']!r}, which is not the count {n}")
    if res[-1]["matched"]:
        drift.append(f"DRIFT — the harness's pattern {pat} matches the count-{SAMPLE_COUNTS[-1]} head behind a "
                     f"leading space, {sent[-1]!r}, so an indented description quoting the head would open a block")
    if drift:
        return 1, drift + [f"the head is printed by {cat} and parsed by {tpl}; a rewording of one is owed in the other"]
    said = ", ".join(f"count {n} matched and captured {n}" for n in SAMPLE_COUNTS)
    return 0, [f"agreement — {pat} in {tpl} over the heads {cat} renders: {said}; "
               f"the count-{SAMPLE_COUNTS[-1]} head behind a leading space not matched"]


def print_verdict(rc, lines):
    for line in lines:
        print(f"by-design parity: {line}")
    return rc


def build_fixture(root, catalogue, decl):
    """Write `<root>/gotchas.py` and `<root>/tier2-review.template.js` -> (catalogue dir, template)."""
    root.mkdir(parents=True)
    (root / "gotchas.py").write_text(catalogue, encoding="utf-8")
    tpl = root / "tier2-review.template.js"
    tpl.write_text(f"// a fixture template\n{decl}\nfunction extractByDesign(v) {{ return v }}\n", encoding="utf-8")
    return root, tpl


def run_selftest():
    # A FIXTURE head, never the real one: the self-test proves the mechanism, and a copy of the real
    # spelling here would be a third answer to the question this file exists to keep at two.
    head = "# fixture head — {n} entry(s)"
    ok_cat = ('KINDS = ("class", "invariant")\nHEAD = ' + repr(head) + '\n\n'
              'def render_by_design(inv):\n    return ["", HEAD.format(n=len(inv))] + ["- " + r["name"] for r in inv]\n')
    ok_decl = r"const BY_DESIGN_HEAD = /^# fixture head — (\d+) entry\(s\)$/"
    short = "process.stdout.write(JSON.stringify({ pattern: '/x/', results: [{ matched: true, group: '0' }] }))"
    with tempfile.TemporaryDirectory() as tmp:

        def arm(name, catalogue, decl, want_rc, want, **kw):
            rc, lines = check_parity(*build_fixture(pathlib.Path(tmp) / name, catalogue, decl), **kw)
            text = "\n".join(lines)
            return None if rc == want_rc and want in text else f"rc {rc}, want {want_rc} carrying {want!r}: {text!r}"

        arms = [
            ("parity", lambda: arm("parity", ok_cat, ok_decl, 0, "count 12 matched and captured 12")),
            ("drift-no-match", lambda: arm("nomatch", ok_cat.replace("fixture head", "fixture-head"), ok_decl, 1, "does not match")),
            ("drift-capture", lambda: arm("capture", ok_cat, "const BY_DESIGN_HEAD = /^(.*)$/", 1, "which is not the count")),
            ("drift-leading-space", lambda: arm("unanchored", ok_cat, ok_decl.replace("/^", "/"), 1, "behind a leading space")),
            ("drift-invariant-no-renderer", lambda: arm("norender", 'KINDS = ("class", "invariant")\n', ok_decl, 1, "`invariant` kind")),
            ("skip-predates-the-block", lambda: arm("predates", 'KINDS = ("class",)\n', ok_decl, 0, "SKIP")),
            ("refuse-no-declaration", lambda: arm("nodecl", ok_cat, "// none here", 2, "0 declaration(s)")),
            ("refuse-two-declarations", lambda: arm("twodecl", ok_cat, ok_decl + "\n" + ok_decl, 2, "2 declaration(s)")),
            ("refuse-import", lambda: arm("noimport", 'raise RuntimeError("fixture import failure")\n', ok_decl, 2, "could not be imported")),
            ("refuse-render-raises", lambda: arm("raises", 'def render_by_design(inv):\n    raise KeyError("decision")\n',
                                                 ok_decl, 2, "raised over synthetic records")),
            ("refuse-no-node", lambda: arm("nonode", ok_cat, ok_decl, 2, "could not be run", node="by-design-parity-no-such-node")),
            ("refuse-malformed-output", lambda: arm("malformed", ok_cat, ok_decl, 2, "not JSON", evaluator="process.stdout.write('x')")),
            ("refuse-short-answer", lambda: arm("short", ok_cat, ok_decl, 2, "1 result(s) for 3 head(s) sent", evaluator=short)),
        ]
        passed = ran = 0
        for name, fn in arms:
            ran += 1
            try:
                why = fn()
            except Exception as exc:  # an arm that crashes is a red arm, never a dead runner
                why = f"raised {exc!r}"
            print(f"ok {name}" if why is None else f"FAIL {name}: {why}")
            passed += why is None
    print(f"selftest: {passed}/{ARMS_DECLARED} arms")
    if ran != ARMS_DECLARED:
        print(f"FAIL selftest: {ran} arm(s) ran against {ARMS_DECLARED} declared")
    return 0 if passed == ran == ARMS_DECLARED else 1


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")  # the head carries an em dash, which cp1252 cannot print
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) != 1 or argv[0].startswith("-"):
        print("usage: python check_by_design_parity.py <the memory-tree kit's directory> | --selftest")
        return 2
    return print_verdict(*check_parity(argv[0], pathlib.Path(__file__).resolve().parent / "tier2-review.template.js"))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
