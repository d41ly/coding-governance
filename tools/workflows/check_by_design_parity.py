#!/usr/bin/env python3
"""check_by_design_parity.py — the by-design head the catalogue PRINTS is the head the harnesses FIND.

    python <prefix>/<this kit>/check_by_design_parity.py <the memory-tree kit's directory>
    python <prefix>/<this kit>/check_by_design_parity.py --selftest

TOOL-aGraftedHelix-28, widened by TOOL-aGraftedHelix-32. The head of the by-design block is printed by
the memory-tree kit's `gotchas.py` through `render_by_design` (a Python format string), and this kit
spells it in every template `EVALUATED_TEMPLATES` names: each declares a `BY_DESIGN_HEAD` (a JS
regex) that finds the block, and the build harness also declares `BY_DESIGN_FORMAT`, the one string
`renderChecklistUnion` emits the merged head from. A head reworded in one place makes a harness find
no block and log `none supplied`, which a reader takes for "no invariant touched": a zero that reads
as clean. So this RUNS every spelling rather than comparing them as text, which would need a
translator, one more spelling. It imports the catalogue by file location and calls its own
`render_by_design` at each count in `SAMPLE_COUNTS`, evaluates each template's one
`const BY_DESIGN_HEAD = /…/` literal in `node`, right-trims each head and calls `test` then `exec` the
way `extractByDesign` does, and renders the build harness's one `BY_DESIGN_FORMAT` string literal at
each count, requiring it byte-equal to the catalogue's head. Python's `re` is not used for a pattern:
its `\\d` takes Unicode digits and its `$` matches before a trailing newline, so it is not the
harness's behaviour.

THE POPULATION IS DERIVED, never stated (`scan_head_spellings`). The checker walks its own directory
and the memory-tree directory for every file carrying the head's fixed tail, the trailing run of
letters-only words of the head the catalogue renders, and reds on a file outside the evaluated set:
the catalogue plus `EVALUATED_TEMPLATES`. A new spelling therefore joins the check or reds the bar.
It spells no word of the head itself, and a tail shorter than two words REFUSES, because an empty
needle is found in every file.

PASSES only when every pattern matches every rendered head, captures exactly that head's count, and
does NOT match the count-12 head behind one leading space — `gotchas.py` indents each checklist item's
description, and a description quoting the head must never open a block — and the format renders
each head byte for byte, and the scan finds no spelling outside the evaluated set.

    exit 0  parity, or SKIP: a catalogue with no `render_by_design` and no `invariant` in `KINDS`
            predates the block, renders none, and the harnesses truthfully log none
    exit 1  DRIFT, quoting the head and the pattern or format, or naming a file the scan found outside
            the evaluated set; a catalogue declaring `invariant` with no `render_by_design` is drift
            too, since a renamed renderer would otherwise skip forever
    exit 2  REFUSING: a template absent, or with zero or two declarations of the pattern or the
            format, or one not a one-line literal; a catalogue that cannot be imported; a renderer
            that raises; no `node`; evaluator output that is malformed or answers any number of heads
            but the number sent; a head whose letters-only tail is shorter than two words; a scan
            that finds no file of the evaluated set, a DEAD PROBE

WHAT THIS DOES NOT CHECK. The block's entry lines (a drifted `- ` makes the harness's count check
refuse before any agent spawns, which is loud). The renders beside each template, whose identity with
the template is the parity leg's own pair, and which the scan skips for that reason. A pattern
loosened but still anchored and still capturing the digits, whose mis-cut of the entries that count
check refuses loudly. A pattern or format declared in any shape but a one-line literal, which REFUSES
here rather than passes. Prose copies of the head: the scan skips `*.md` and `*.test.sh`, and a
spelling in a file the scan never reaches, outside the two directories, is not seen. A spelling that
differs from the catalogue's in its tail, which the needle misses.

The catalogue is imported with bytecode writing off, so a run leaves no `__pycache__` beside it.
"""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile

# Zero is the head every miss prints; twelve is a second, MULTI-DIGIT count, so a pattern capturing
# one digit, or a head that lost its count field, cannot pass. The leading-space negative uses the last.
SAMPLE_COUNTS = (0, 12)
# Every template beside this checker that spells the head, in the order they are reported. The build
# harness is also the one whose `BY_DESIGN_FORMAT` is rendered.
EVALUATED_TEMPLATES = ("tier2-review.template.js", "unattended-build.template.js")
FORMAT_TEMPLATE = "unattended-build.template.js"
ARMS_DECLARED = 18
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
# The format evaluator, run as `node -e FORMAT_EVALUATOR <template>` with the counts as JSON on stdin.
# It renders the one `BY_DESIGN_FORMAT` string literal the way `renderChecklistUnion` does, replacing
# `{n}` with the count. It answers one JSON object: {refuse} or {format, rendered}.
FORMAT_EVALUATOR = r"""
const fs = require('fs')
const say = (o) => process.stdout.write(JSON.stringify(o))
let counts, lines
try {
  counts = JSON.parse(fs.readFileSync(0, 'utf8'))
  lines = fs.readFileSync(process.argv[1], 'utf8').split(/\r?\n/)
} catch (e) { say({ refuse: 'could not read the counts or the template ' + process.argv[1] + ': ' + e.message }); process.exit(0) }
const decl = lines.filter((l) => /^\s*(?:const|let|var)\s+BY_DESIGN_FORMAT\b/.test(l))
if (decl.length !== 1) {
  say({ refuse: process.argv[1] + ' carries ' + decl.length + ' declaration(s) of BY_DESIGN_FORMAT, and exactly one is required' })
  process.exit(0)
}
const lit = /^const BY_DESIGN_FORMAT = ('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")\s*;?\s*$/.exec(decl[0])
if (!lit) { say({ refuse: 'the BY_DESIGN_FORMAT declaration is not a one-line string literal: ' + decl[0] }); process.exit(0) }
let f
try { f = new Function('return ' + lit[1])() } catch (e) { say({ refuse: 'the BY_DESIGN_FORMAT literal does not evaluate: ' + e.message }); process.exit(0) }
if (typeof f !== 'string') { say({ refuse: 'the BY_DESIGN_FORMAT literal is not a string: ' + lit[1] }); process.exit(0) }
say({ format: f, rendered: counts.map((n) => f.replace('{n}', String(n))) })
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


def derive_needle(head):
    """-> the head's fixed tail: its trailing run of letters-only words, joined by one space. ValueError
    when that run is shorter than two words, because a one-word or empty needle matches nearly every file."""
    tail = []
    for word in reversed(head.split()):
        if not word.isalpha():
            break
        tail.insert(0, word)
    if len(tail) < 2:
        raise ValueError(f"the head's letters-only tail is {len(tail)} word(s), {' '.join(tail)!r}, and a "
                         f"needle shorter than two words would find the head in nearly every file: {head!r}")
    return " ".join(tail)


def run_node(evaluator, template, payload, node):
    """-> the evaluator's JSON object. OSError when node cannot start; ValueError on a refusal or on
    output that is not JSON."""
    proc = subprocess.run([node, "-e", evaluator, str(template)], input=json.dumps(payload),
                          capture_output=True, encoding="utf-8", errors="replace", timeout=120)
    try:
        out = json.loads(proc.stdout)
    except ValueError:
        raise ValueError(f"the node evaluator's output is not JSON (exit {proc.returncode}): "
                         f"stdout {proc.stdout[:200]!r}, stderr {proc.stderr[:200]!r}") from None
    if isinstance(out, dict) and "refuse" in out:
        raise ValueError(str(out["refuse"]))
    return out


def run_pattern(heads, template, node="node", evaluator=EVALUATOR):
    """-> (the pattern's source, one {matched, group} per head). OSError when node cannot start;
    ValueError on a refusal, or on output that is not one well-formed result per head sent."""
    out = run_node(evaluator, template, heads, node)
    res = out.get("results") if isinstance(out, dict) else None
    good = isinstance(res, list) and all(
        isinstance(r, dict) and isinstance(r.get("matched"), bool) and (r.get("group") is None or isinstance(r["group"], str))
        for r in res)
    if not good or len(res) != len(heads):
        raise ValueError(f"the node evaluator answered {len(res) if good else 'no well-formed'} result(s) "
                         f"for {len(heads)} head(s) sent: {json.dumps(out)[:200]!r}")
    return str(out.get("pattern")), res


def run_format(template, node="node", evaluator=FORMAT_EVALUATOR):
    """-> (the format string, the head it renders at each count in SAMPLE_COUNTS). OSError when node
    cannot start; ValueError on a refusal, or on output that is not one string per count."""
    out = run_node(evaluator, template, list(SAMPLE_COUNTS), node)
    got = out.get("rendered") if isinstance(out, dict) else None
    if not (isinstance(got, list) and len(got) == len(SAMPLE_COUNTS) and all(isinstance(s, str) for s in got)):
        raise ValueError(f"the format evaluator answered no string per count sent: {json.dumps(out)[:200]!r}")
    return str(out.get("format")), got


def scan_head_spellings(dirs, needle):
    """-> every file under `dirs`, recursively, whose text carries `needle`, as resolved paths. Skips
    `__pycache__`, `*.md`, `*.test.sh` and each `X.js` beside an `X.template.js`, the render of a
    template whose identity with it the parity leg holds."""
    hits = set()
    for top in dirs:
        for here, subdirs, names in os.walk(top):
            subdirs[:] = [d for d in subdirs if d != "__pycache__" and d != ".git"]
            for name in names:
                if name.endswith(".md") or name.endswith(".test.sh"):
                    continue
                if name.endswith(".js") and not name.endswith(".template.js") and (name[:-3] + ".template.js") in names:
                    continue
                path = pathlib.Path(here) / name
                try:
                    text = path.read_bytes().decode("utf-8", errors="replace")
                except OSError:
                    continue
                if needle in text:
                    hits.add(path.resolve())
    return sorted(hits)


def check_parity(mt_dir, tpl_dir, node="node", evaluator=EVALUATOR, format_evaluator=FORMAT_EVALUATOR):
    """-> (exit code, verdict lines). 0 parity or SKIP · 1 DRIFT · 2 REFUSING. `tpl_dir` holds every
    template in EVALUATED_TEMPLATES; outside the self-test it is this checker's own directory."""
    cat = (pathlib.Path(mt_dir) / "gotchas.py").as_posix()
    tpl_dir = pathlib.Path(tpl_dir)
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
    try:
        needle = derive_needle(heads[-1])
    except ValueError as exc:
        return 2, [f"REFUSING — the scan has no needle: {exc}"]
    sent = heads + [" " + heads[-1]]
    drift, agree = [], []
    for tpl in EVALUATED_TEMPLATES:
        if not (tpl_dir / tpl).is_file():
            return 2, [f"REFUSING — the evaluated template {tpl} is absent from {tpl_dir.as_posix()}, so its "
                       f"spelling of the head cannot be run"]
        try:
            pat, res = run_pattern(sent, tpl_dir / tpl, node, evaluator)
        except (OSError, ValueError, subprocess.SubprocessError) as exc:
            return 2, [f"REFUSING — the harness's pattern in {tpl} could not be run: {exc}"]
        bad = []
        for n, head, r in zip(SAMPLE_COUNTS, heads, res):
            if not r["matched"]:
                bad.append(f"DRIFT — the pattern {pat} in {tpl} does not match the head the catalogue renders at count {n}: {head!r}")
            elif r["group"] != str(n):
                bad.append(f"DRIFT — the pattern {pat} in {tpl} matches the count-{n} head {head!r} but captures "
                           f"{r['group']!r}, which is not the count {n}")
        if res[-1]["matched"]:
            bad.append(f"DRIFT — the pattern {pat} in {tpl} matches the count-{SAMPLE_COUNTS[-1]} head behind a "
                       f"leading space, {sent[-1]!r}, so an indented description quoting the head would open a block")
        said = ", ".join(f"count {n} matched and captured {n}" for n in SAMPLE_COUNTS)
        line = (f"agreement — {pat} in {tpl} over the heads {cat} renders: {said}; "
                f"the count-{SAMPLE_COUNTS[-1]} head behind a leading space not matched")
        if tpl == FORMAT_TEMPLATE:
            try:
                fmt, rendered = run_format(tpl_dir / tpl, node, format_evaluator)
            except (OSError, ValueError, subprocess.SubprocessError) as exc:
                return 2, [f"REFUSING — the harness's format in {tpl} could not be run: {exc}"]
            for n, head, got in zip(SAMPLE_COUNTS, heads, rendered):
                if got != head:
                    bad.append(f"DRIFT — the format {fmt!r} in {tpl} renders {got!r} at count {n}, and the catalogue "
                               f"renders {head!r}")
            line += f"; its BY_DESIGN_FORMAT {fmt!r} renders the catalogue's head at " + \
                ", ".join(f"count {n}" for n in SAMPLE_COUNTS)
        drift += bad
        if not bad:
            agree.append(line)
    declared = {(pathlib.Path(mt_dir) / "gotchas.py").resolve()} | {(tpl_dir / t).resolve() for t in EVALUATED_TEMPLATES}
    hits = scan_head_spellings([tpl_dir, pathlib.Path(mt_dir)], needle)
    # THE SCAN'S LIVENESS: every evaluated template exists by now and spells the tail in its pattern,
    # so a scan holding none of the evaluated set reached nothing, and would find a stray no better.
    if not declared & set(hits):
        return 2, [f"REFUSING — DEAD PROBE: the scan for the head's tail {needle!r} found no file of the "
                   f"evaluated set, so it cannot see a spelling outside it either: {len(hits)} hit(s)"]
    for h in hits:
        if h not in declared:
            drift.append(f"DRIFT — {h.as_posix()} carries the head's tail {needle!r} and is not in the evaluated set, "
                         f"so a rewording would leave its spelling behind; add it to EVALUATED_TEMPLATES or drop the spelling")
    if drift:
        return 1, drift + [f"the head is printed by {cat} and spelled in {', '.join(EVALUATED_TEMPLATES)}; "
                           f"a rewording of one is owed in every other"]
    return 0, agree + [f"population — {len(hits)} file(s) carry the head's tail {needle!r}, each evaluated: "
                       + ", ".join(h.name for h in hits)]


def print_verdict(rc, lines):
    for line in lines:
        print(f"by-design parity: {line}")
    return rc


def build_fixture(root, catalogue, decl, fmt):
    """Write `<root>/gotchas.py` and both EVALUATED_TEMPLATES -> (catalogue dir, template dir). `fmt` is
    the build harness's format declaration line, or '' for none."""
    root.mkdir(parents=True)
    (root / "gotchas.py").write_text(catalogue, encoding="utf-8")
    (root / "tier2-review.template.js").write_text(
        f"// a fixture template\n{decl}\nfunction extractByDesign(v) {{ return v }}\n", encoding="utf-8")
    (root / FORMAT_TEMPLATE).write_text(
        f"// a fixture build harness\n{decl}\n{fmt}\nfunction renderChecklistUnion(v) {{ return v }}\n", encoding="utf-8")
    return root, root


def run_selftest():
    # A FIXTURE head, never the real one: the self-test proves the mechanism, and a copy of the real
    # spelling here would be one more answer to the question this file exists to hold.
    head = "# fixture head — {n} entry(s) in the fixture"
    ok_cat = ('KINDS = ("class", "invariant")\nHEAD = ' + repr(head) + '\n\n'
              'def render_by_design(inv):\n    return ["", HEAD.format(n=len(inv))] + ["- " + r["name"] for r in inv]\n')
    ok_decl = r"const BY_DESIGN_HEAD = /^# fixture head — (\d+) entry\(s\) in the fixture$/"
    ok_fmt = "const BY_DESIGN_FORMAT = '# fixture head — {n} entry(s) in the fixture'"
    short = "process.stdout.write(JSON.stringify({ pattern: '/x/', results: [{ matched: true, group: '0' }] }))"
    # The DEAD-PROBE fixture spells the tail only through pieces and escapes, so every spelling agrees
    # and no file carries the tail as text: the scan's population is empty with the declared set present.
    dead_cat = ('KINDS = ("class", "invariant")\nHEAD = ' + repr(head[:-4]) + ' + "ture"\n\n'
                'def render_by_design(inv):\n    return ["", HEAD.format(n=len(inv))] + ["- " + r["name"] for r in inv]\n')
    dead_decl = r"const BY_DESIGN_HEAD = /^# fixture head — (\d+) entry\(s\) in the fix\x74ure$/"
    dead_fmt = r"const BY_DESIGN_FORMAT = '# fixture head — {n} entry(s) in the fix\x74ure'"
    with tempfile.TemporaryDirectory() as tmp:

        def arm(name, catalogue, decl, want_rc, want, fmt=ok_fmt, extra=None, drop=None, **kw):
            root, tpl_dir = build_fixture(pathlib.Path(tmp) / name, catalogue, decl, fmt)
            if extra:
                (root / extra[0]).write_text(extra[1], encoding="utf-8")
            if drop:
                (root / drop).unlink()
            rc, lines = check_parity(root, tpl_dir, **kw)
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
            ("drift-format", lambda: arm("fmtdrift", ok_cat, ok_decl, 1, "DRIFT — the format",
                                         fmt=ok_fmt.replace("fixture head", "fixture-head"))),
            ("refuse-format-missing", lambda: arm("nofmt", ok_cat, ok_decl, 2, "0 declaration(s) of BY_DESIGN_FORMAT", fmt="")),
            ("drift-undeclared-spelling", lambda: arm("extra", ok_cat, ok_decl, 1, "extra.py carries the head's tail",
                                                      extra=("extra.py", "X = 'in the fixture'\n"))),
            ("refuse-short-needle", lambda: arm("needle", ok_cat.replace("in the fixture", "x9"), ok_decl, 2, "the scan has no needle")),
            ("refuse-dead-probe", lambda: arm("dead", dead_cat, dead_decl, 2, "DEAD PROBE", fmt=dead_fmt)),
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
    return print_verdict(*check_parity(argv[0], pathlib.Path(__file__).resolve().parent))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
