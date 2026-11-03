# TOOL-dFairHearing-1 — the calibration: the known set and the scorer reproduce the baseline's own figures

**Serves:** research TOOL-dFairHearing-1

Pass (a) of this unit (spec S1 to S4, AC1 to AC3; the build brief's two-pass plan). Every figure below
is a probe's or the scorer's output, quoted after the command that printed it, at the commit that adds
this record.

## What was observed

- **AC1** — `parse_known_set` over the committed known set
  (`2026-11-03-build-TOOL-dFairHearing-1-known-set`) reads 65 rows, 59 escaped `no`, 6 escaped `yes`,
  8 graded `high` among the reviewed: the `replay: known-set` line of every score below. A scratch copy
  with the `limit-hold` row cut exits 2 naming `rows 64 against the population line's 65`, and one with
  `driver-schema` renamed `relaunch-replay` exits 2 naming `tag relaunch-replay is repeated`.
- **AC2** — a scratch matched list adding the pair `1 merge-back` exits 2 naming the pair: A1's ref cites
  `[supervise]`, `[spawn]` and `[tests]`, never `merge-back`'s `[isolate]`. A scratch list naming
  `relaunch-replay` twice, by A1 and A15, scores it once: `reviewed 1/59`.
- **AC3** — the two baseline matched lists (`…-matched-a`, `…-matched-b`) print `reviewed 46/59`,
  `escaped 0/6`, `high 6/8` for run A and `reviewed 45/59`, `escaped 0/6`, `high 8/8` for run B: the
  comparison record's `[numbers]` (A alone 46 of 59, B alone 45, B finding all eight highs and A
  missing `cycle-spawns` and `structured-output`). The weak candidate, every other pair of run A's list
  (`awk 'NR%2==1'` over its pair rows, 30 pairs), prints `reviewed 27/59`, under the bar's 45, once.
- **The known set's derivation** — `fh1-knownset.py` reads the comparison record's `[map]` and both
  reports' appendices with the factory's own `CELL_SPLIT`, `TAG_REF`, `derive_ref_parts` and
  `extract_tag_ref`, and writes the 59 reviewed rows and the two pair lists; the committed rows and
  lists are byte-equal to its output once line endings are folded. Under §8 F6's rule it moves
  `executor-map` and `inflight-count` to `[supervise]` and no other row.
- **Replay 4's control** — `fh1-control.py` applies §8 F4's rule and picks dSweptBranches round 1's
  id 23 (item B1, class `C10`), fixed by `f0e00195e`; the reading of the rule is stated in
  `…-replay-4-skeptic-control`.

The address-match lines, 371 for run A and 405 for run B, are the adjudicator's candidates and are left
out below; each command reprints them.

## The probes

Each runs from the repository root. `fh1-render.js` renders replays 3 and 4's staged inputs
(`…-replay-3-synthesis-a`, `-b`, `…-replay-4-skeptic-23`, `-control`); it reads the checklist from a
scratch file holding `gotchas.py --for-paths` over the subject in an export of commit `6cfd21619`.

### fh1-knownset.py

~~~~python
"""TOOL-dFairHearing-1 S1/S4: derive the known set's 59 reviewed rows and the two baseline matched lists.

python fh1-knownset.py <out-dir>   (run from the repository root)
Writes rows.md (the table body), matched-a.md and matched-b.md (pair rows) into <out-dir>, and prints the counts.
"""
import pathlib
import re
import sys

sys.path.insert(0, "tools/workflows")
import replay_scorer as rs  # noqa: E402

CMP = "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md"
REP = {r: f"memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-{r.lower()}.md" for r in "AB"}
HIGH = ("relaunch-replay merge-back chain-overlap fixture-2-population catalogue-duplicates fencing cycle-spawns "
        "structured-output").split()


def read_appendix(path):
    """Every appendix row (confirmed and refuted), by integer id, read with the factory's own cell split."""
    lines = pathlib.Path(path).read_text(encoding="utf-8").split(rs.APPENDIX_HEADING, 1)[1].split("\n")
    hdr, out = None, {}
    for line in lines:
        if not line.startswith("|"):
            if hdr:
                break
            continue
        cells = [c.strip().replace("\\|", "|") for c in rs.CELL_SPLIT.split(line.strip())[1:-1]]
        if hdr is None:
            hdr = cells
        elif not cells[0].startswith("---"):
            row = dict(zip(hdr, cells))
            out[int(row["id"])] = row
    return out


def read_map():
    block = pathlib.Path(CMP).read_text(encoding="utf-8").split("## [map]", 1)[1].split("\n## ", 1)[0]
    ids = lambda cell: [] if cell.strip() in ("—", "-", "") else [int(x) for x in re.split(r"[,\s]+", cell.strip()) if x]
    for line in block.splitlines():
        if line.startswith("| `"):
            cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
            yield cells[0].strip("`"), {"A": ids(cells[2]), "B": ids(cells[3])}


def cites(ref, tag):
    return tag in rs.TAG_REF.findall(ref.split(":", 1)[1])


rep = {r: read_appendix(REP[r]) for r in "AB"}
rows, pairs = [], {"A": [], "B": []}
for slug, placed in read_map():
    conf = {r: [i for i in placed[r] if rep[r][i]["verdict"] == "confirmed"] for r in "AB"}
    if not (conf["A"] or conf["B"]):
        continue
    run, src = ("A", min(conf["A"])) if conf["A"] else ("B", min(conf["B"]))
    ref = rep[run][src]["ref"]
    path = rs.derive_ref_parts(ref)[0]
    found = [r for r in "AB" if conf[r]]
    # F6 (a): the first [tag] of the source's ref which at least one confirmed finding of every finding round cites.
    tag = next((t for t in rs.TAG_REF.findall(ref.split(":", 1)[1])
                if all(any(cites(rep[r][i]["ref"], t) for i in conf[r]) for r in found)), None)
    if tag is None:
        raise SystemExit(f"{slug}: no qualifying tag")
    first = rs.extract_tag_ref(ref)[1]
    rows.append((slug, f"{path}:{tag}", "high" if slug in HIGH else "medium", run + str(src), first))
    for r in found:
        pairs[r] += [(i, slug) for i in conf[r] if cites(rep[r][i]["ref"], tag)]

out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
(out / "rows.md").write_text("".join(f"| {s} | {a} | {g} | no |\n" for s, a, g, _, _ in rows), encoding="utf-8")
for r in "AB":
    (out / f"matched-{r.lower()}.md").write_text("".join(f"| {i} | {s} |\n" for i, s in pairs[r]), encoding="utf-8")
print("rows", len(rows), "high", sum(g == "high" for _, _, g, _, _ in rows))
for s, a, g, src, first in rows:
    if a.rsplit(":", 1)[1] != first:
        print("moved", s, src, first, "->", a.rsplit(":", 1)[1])
for r in "AB":
    print(r, "pairs", len(pairs[r]), "tags", len({s for _, s in pairs[r]}), "high", len({s for _, s in pairs[r] if s in HIGH}))
~~~~

### fh1-control.py

~~~~python
"""TOOL-dFairHearing-1 §8 F4: replay 4's control fix, by the selection rule fixed in the spec.

python fh1-control.py   (run from the repository root; read-only)
The first round-1 confirmed finding, in `review_replay.py --corpus memory/builds` order, whose fix commit the
next round of the same build reviewed with no confirmed finding sharing its `classes` cell. Read here as:
the next round is a listed round-2 record of the same build whose range head descends from round 1's head;
a finding's fix commit is a commit inside that range whose subject or body names the report item holding
the finding's id; a finding whose `classes` cell is `-` names no class a fix could cover, so it is skipped.
"""
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, "tools/workflows")
import review_replay as rr  # noqa: E402
import replay_scorer as rs  # noqa: E402

HEAD = re.compile(r"^#{2,4} ([A-Z]+\d+)(?:\.| —) .*\((?:id|ids) ([0-9, ]+)\)\s*$")
listed, _, _ = rr.scan_corpus(["memory/builds"], ".")


def build_of(path):
    return path.split("/")[2]


def items(text):
    out = {}
    for line in text.splitlines():
        m = HEAD.match(line.strip())
        if m:
            for i in re.findall(r"\d+", m.group(2)):
                out.setdefault(i, m.group(1))
    return out


def classes(row):
    c = (row.get("classes") or "").strip()
    return set(c.split()) if c and c != "-" else set()


picked = None
for path, rnd, known in listed:
    if rnd != "1" or picked:
        continue
    nxt = [(p, k) for p, r, k in listed if r == "2" and build_of(p) == build_of(path) and k["range"][1] != known["range"][1]
           and subprocess.run(["git", "merge-base", "--is-ancestor", known["range"][1], k["range"][1]]).returncode == 0]
    text = pathlib.Path(path).read_text(encoding="utf-8")
    held = items(text)
    for p2, k2 in nxt:
        taken = set().union(*(classes(r) for r in (rs.parse_appendix_rows(pathlib.Path(p2).read_text(encoding="utf-8"))[0] or [])))
        out = subprocess.run(["git", "log", "-z", "--format=%H %s%n%b", f"{k2['range'][0]}..{k2['range'][1]}", "^" + known["range"][1]],
                             capture_output=True, text=True, check=True).stdout
        log = [c for c in out.split(chr(0)) if c.strip() and re.match(r"[0-9a-f]{40} (fix|fold)\(", c)]
        for row in sorted(rs.parse_appendix_rows(text)[0] or [], key=lambda r: int(r["id"])):
            cls, item = classes(row), held.get(row["id"])
            if not cls or not item:
                continue
            fixes = [c for c in log if re.search(r"\b" + item + r"\b", c.split(" ", 1)[1])]
            shared = cls & taken
            fix = fixes[-1][:9] + " " + fixes[-1][41:].splitlines()[0] if fixes else "none"
            print(f"{path} id {row['id']} item {item} classes {' '.join(sorted(cls))} · next {p2} · fix {fix} · shared {' '.join(sorted(shared)) or 'none'}")
            if fixes and not shared and picked is None:
                picked = (path, row["id"], item, p2, fixes[-1][:40])
        if picked:
            break
print("PICK", picked)
~~~~

### fh1-render.js

~~~~js
// TOOL-dFairHearing-1 S7/S8 (spec §4 Twins and Fix verdict): the prompts replays 3 and 4 hand their real agents,
// rendered by tools/workflows/tier2-review.js itself under stub agents, as tier2-review.test.sh's runReview drives it.
//   node fh1-render.js twins <A|B> <out-file>
//   node fh1-render.js fix <23|control> <out-file>
// Run from the repository root; reads committed records only, writes <out-file> alone. Exit 1 on any id mismatch.
const fs = require('fs')
const SCRIPT = 'tools/workflows/tier2-review.js'
const src = fs.readFileSync(SCRIPT, 'utf8')
const whole = src.replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
const die = (m) => { console.error('fh1-render: ' + m); process.exit(1) }

// The harness's own fold, sliced from the script so no second copy decides what a prompt line is.
const rpl = /\nfunction renderPromptLine\(v\) \{\n[\s\S]*?\n\}\n/.exec(src)
if (!rpl) die('renderPromptLine moved')
const renderPromptLine = new Function(rpl[0] + '\nreturn renderPromptLine')()

function resolveStub(stubs, label) {
  if (Object.prototype.hasOwnProperty.call(stubs, label)) return stubs[label]
  let best = null
  for (const k of Object.keys(stubs)) if (label.indexOf(k) === 0 && (best === null || k.length > best.length)) best = k
  return best === null ? undefined : stubs[best]
}
async function runReview(args, stubs) {
  const trace = []
  const logs = []
  const agent = async (prompt, opts) => {
    const full = (opts && opts.label) || '(unlabelled)'
    const label = full.split(' · ').pop()
    trace.push({ label: label, prompt: String(prompt), schema: opts && opts.schema })
    let v = resolveStub(stubs, label)
    if (typeof v === 'function') v = v(label, String(prompt))
    return v === undefined || v === null ? null : JSON.parse(JSON.stringify(v))
  }
  const parallel = async (thunks) => Promise.all(thunks.map((t) => t()))
  let result = null
  let threw = null
  try {
    result = await new AsyncFunction('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'workflow', whole)(
      args, agent, parallel, async () => [], () => {}, (m) => logs.push(String(m)), {}, async () => ({}))
  } catch (e) { threw = e.message }
  return { trace, logs, result, threw }
}

// ---- committed sources -------------------------------------------------------------------------------
const read = (p) => fs.readFileSync(p, 'utf8').replace(/\r\n/g, '\n')
function readAppendix(text) {
  const lines = text.split('\n')
  const at = lines.findIndex((l) => l.trim() === '## Appendix — every finding')
  if (at === -1) die('no appendix')
  const rows = []
  let header = null
  for (const l of lines.slice(at + 1)) {
    if (!l.trim().startsWith('|')) { if (header) break; continue }
    const cells = l.trim().split(/(?<!\\)\|/).slice(1, -1).map((c) => c.trim().replace(/\\\|/g, '|'))
    if (!header) { header = cells; continue }
    if (/^-+$/.test(cells[0])) continue
    rows.push(Object.fromEntries(header.map((h, i) => [h, cells[i]])))
  }
  return rows
}
// The report item holding an id: the `###` heading whose `(id N)` or `(ids …)` names it, to the next heading.
function readItem(text, id) {
  const lines = text.split('\n')
  const at = lines.findIndex((l) => /^#{2,4} /.test(l) && (/\((?:id|ids) ([0-9, ]+)\)\s*$/.exec(l) || [, ''])[1].split(/[, ]+/).indexOf(String(id)) !== -1)
  if (at === -1) return null
  const end = lines.findIndex((l, i) => i > at && /^#{1,4} /.test(l))
  return lines.slice(at + 1, end === -1 ? undefined : end)
}
// A top-level `- **<label>:**` bullet whose label `test` accepts, with its continuation lines and sub-bullets,
// each line's markdown indentation dropped, folded by renderPromptLine; the empty string when the item has none.
function readBullet(item, test) {
  const at = item.findIndex((l) => { const m = /^- \*\*([^*]+?):\*\*/.exec(l); return m && test(m[1]) })
  if (at === -1) return ''
  const end = item.findIndex((l, i) => i > at && (/^- /.test(l) || /^\S/.test(l)))
  const body = item.slice(at, end === -1 ? undefined : end).map((l) => l.trim()).filter((l) => l)
  body[0] = body[0].replace(/^- \*\*[^*]+?:\*\*\s*/, '')
  return renderPromptLine(body.join('\n'))
}
const CLAIM = (l) => ['What is wrong', 'What', 'Defect'].indexOf(l) !== -1
const IMPACT = (l) => ['Consequence', 'Impact'].indexOf(l) !== -1
const FIX = (l) => /^Fix\b/.test(l)
function readFinding(text, id, need) {
  const item = readItem(text, id)
  if (!item) die('no report item holds id ' + id)
  const claim = readBullet(item, CLAIM)
  if (need && (claim === '' || claim === '-')) die('the item holding id ' + id + ' has no claim bullet: a divergence, not a guess')
  return { claim, impact: readBullet(item, IMPACT), fix: readBullet(item, FIX) }
}
const splitRef = (ref) => { const i = ref.indexOf(':'); return [ref.slice(0, i), ref.slice(i + 1)] }

const [mode, which, out] = process.argv.slice(2)
if (!out) die('usage: twins <A|B> <out> | fix <23|control> <out>')
const CMP = 'memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md'
const SCRATCH = 'C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad'
const CLONE = 'C:/Users/DAILY-~1/AppData/Local/Temp/fh1'
const runB = JSON.parse(/```json\n([\s\S]*?)\n```/.exec(read(CMP))[1])
const probe = (base, head) => ({ 'resume:probe': { commonDir: '/cd', base: base, head: head, finds: [], verifies: [] } })

async function renderTwins() {
  const report = read(`memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-${which.toLowerCase()}.md`)
  const rows = readAppendix(report)
  const LENSES = ['coherence', 'grounding', 'reuse', 'blast-radius', 'failure-envelope']
  const byLens = {}
  for (const r of rows) (byLens[r.lens] = byLens[r.lens] || []).push(r)
  if (Object.keys(byLens).some((l) => LENSES.indexOf(l) === -1)) die('a lens outside the unit-spec preset')
  // Ids are assigned lens by lens in dispatch order; the appendix must already number that way.
  const order = LENSES.flatMap((l) => byLens[l] || [])
  order.forEach((r, i) => { if (Number(r.id) !== i + 1) die(`appendix row ${r.id} sits at harness id ${i + 1}`) })
  const finding = (r) => {
    const [file, where] = splitRef(r.ref)
    const f = r.verdict === 'confirmed' ? readFinding(report, r.id, true) : { claim: r.reason, impact: '', fix: '' }
    return { file, where, severity: r.severity, claim: f.claim, impact: f.impact, fix: f.fix, evidence: '' }
  }
  const stubs = Object.assign(probe(), {
    'find:': (label) => {
      const lens = label.slice('find:'.length)
      return { lens: lens, path: '', findings: (byLens[lens] || []).map(finding) }
    },
    'verify:': (label, prompt) => {
      const m = /ids ([0-9, ]+)\)/.exec(prompt)
      const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
      return { path: '', verdicts: ids.map((id) => {
        const r = rows.find((x) => Number(x.id) === id)
        const v = { id: id, verdict: r.verdict, reason: r.reason, fixVerdict: r.fixVerdict, fixNote: '' }
        if (r.skepticSeverity && r.skepticSeverity !== '-' && r.verdict === 'confirmed') v.severity = r.skepticSeverity
        return v
      }) }
    },
    synth: { path: '', summary: '', items: [], twinFlags: [] },
  })
  const args = Object.assign({}, runB, {
    repo: CLONE, scratch: SCRATCH, addressTwins: 'shown',
    // Today's harness pins every subject by id (TOOL-dTrueNorth-5, -13): a design record's id is the one its
    // `**Serves:**` line names, bare, which run B's 2026-10-15 arguments predate.
    subjects: runB.subjects.map((s) => Object.assign({}, s, { id: 'PLAY-dClosedLoop-1' })),
    context: runB.context.replace('this is run B', 'this is run ' + (which === 'A' ? '1' : '2')),
    checklist: fs.readFileSync(SCRATCH + '/fh1-checklist.txt', 'utf8'),
  })
  const r = await runReview(args, stubs)
  const synth = r.trace.find((t) => t.label === 'synth')
  if (!synth) die('no synthesis call: ' + r.threw)
  // The id check: every rendered `- id=N [` line carries appendix row N's lens and ref, or the probe stops.
  let checked = 0
  for (const line of synth.prompt.split('\n')) {
    const m = /^- id=(\d+) \[[^\]]*\](?: \([^)]*\))? lens=(\S+) (.*?) — /.exec(line)
    if (!m) continue
    const row = rows.find((x) => Number(x.id) === Number(m[1]))
    if (!row || row.lens !== m[2] || row.ref !== m[3]) die(`rendered id=${m[1]} reads lens ${m[2]} ref ${m[3]}, appendix row reads ${row && row.lens} ${row && row.ref}`)
    checked++
  }
  return { prompt: synth.prompt, schema: synth.schema, note: `ids checked ${checked} of ${rows.length} appendix rows · threw ${r.threw || 'no'}` }
}

async function renderFix() {
  const SRC = which === '23'
    ? { report: 'memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md', id: 23,
        base: 'ff0b3dc327514e020eb47009de931d4dfd78c608', head: '5b4f964d50a85656029a7bd6a58f795f7717661a' }
    : { report: 'memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md', id: 23,
        base: '0ac2418c05fad32467e20a93f04b8546383a1c4d', head: 'f0e00195e8b4745a2165baadd4444cb32b735591' }
  const text = read(SRC.report)
  const row = readAppendix(text).find((x) => Number(x.id) === SRC.id)
  const [file, line] = splitRef(row.ref)
  const f = readFinding(text, SRC.id, true)
  const finding = { file, line: Number(line), severity: row.severity, claim: f.claim, impact: f.impact, fix: f.fix }
  const stubs = Object.assign(probe(SRC.base, SRC.head), {
    'find:': (label) => ({ lens: label.slice('find:'.length), path: '', findings: label === 'find:' + row.lens ? [finding] : [] }),
  })
  const args = { repo: process.cwd().replace(/\\/g, '/'), base: SRC.base, head: SRC.head, round: 1, fixJudge: 'class',
    reviewDir: SCRATCH + '/fh1-reviews', scratch: SCRATCH,
    context: `the fix ${SRC.base.slice(0, 9)}..${SRC.head.slice(0, 9)} of the finding ${row.ref} that ${SRC.report} confirmed as id ${SRC.id}`,
    roles: { skeptic: 'gov-skeptic' }, efforts: { skeptic: 'medium' }, checklist: ['- none'] }
  const r = await runReview(args, stubs)
  const v = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
  if (v.length !== 1) die(`${v.length} skeptic call(s), not one: ${r.threw}`)
  if (!/^id=1 \[/m.test(v[0].prompt) || v[0].prompt.indexOf(' lens=' + row.lens + ' ' + row.ref + ' — ') === -1) die('the skeptic line is not id 1 at the row ref')
  return { prompt: v[0].prompt, schema: v[0].schema, note: `finder lens ${row.lens} · ref ${row.ref} · threw ${r.threw || 'no'}` }
}

// With a head file, <out> is the staged record: the head, then the prompt and the schema the harness passed, each fenced.
const headFile = process.argv[5]
;(mode === 'twins' ? renderTwins() : renderFix()).then((x) => {
  const sha = require('crypto').createHash('sha256').update(x.prompt, 'utf8').digest('hex')
  const line = `${mode} ${which}: ${Buffer.byteLength(x.prompt, 'utf8')} bytes · sha256 ${sha} · ${x.note}`
  fs.writeFileSync(out, !headFile ? x.prompt
    : fs.readFileSync(headFile, 'utf8').replace(/\r\n/g, '\n').replace('<RENDER-LINE>', line) +
      '\n## The prompt, verbatim\n\nThe bytes between the two fence lines, the newline before the closing fence excluded.\n\n````text\n' + x.prompt +
      '\n````\n\n## The schema the harness passed with it\n\n````json\n' + JSON.stringify(x.schema, null, 1) + '\n````\n')
  console.log(line)
})
~~~~

### Output: python fh1-knownset.py <scratch>/fh1ks

~~~~text
rows 59 high 8
moved executor-map A5 [extend] -> [supervise]
moved inflight-count A8 [invariants] -> [supervise]
A pairs 60 tags 46 high 6
B pairs 61 tags 45 high 8
~~~~

### Output: the scorer, run A and run B, the weak list, the two cut known sets and the two scratch matched lists

~~~~text
$ python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-a.md
replay: known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md · rows 65 · reviewed 59 · escaped 6 · high 8
replay: candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md · address matches 371
replay: matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-a.md · adjudicator the main loop of 2026-10-15, whose `[map]` placement in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` is read here and never revised · pairs 60 · tags 46
MATCHED         relaunch-replay  <-  1, 15
MATCHED         driver-schema  <-  2
MATCHED         driver-cwd  <-  20
MATCHED         calls-per-act  <-  21
MATCHED         merge-back  <-  3
MATCHED         chain-overlap  <-  4, 32, 44
MATCHED         return-check-owner  <-  33
MATCHED         executor-map  <-  5
MATCHED         renewal-keys  <-  6, 37
MATCHED         fixture-2-population  <-  7, 17, 52
MATCHED         hidden-spawns  <-  8, 16
MATCHED         inflight-count  <-  8, 16, 54
MATCHED         unfailing-fixtures  <-  9
MATCHED         fail-closed-policy  <-  10, 60
MATCHED         binding-events  <-  10, 23
MATCHED         extension-enums  <-  11
MATCHED         compaction-checks  <-  12
MATCHED         invariant-8-fixture  <-  13
MATCHED         cli-binary  <-  18
MATCHED         cli-floor-decision  <-  29
MATCHED         supervisor-host  <-  19
MATCHED         codex-events  <-  22
MATCHED         dispatcher-latency  <-  24
MATCHED         fanout-carrier  <-  25, 40, 60
MATCHED         reap-key  <-  26
MATCHED         resume-tick-seed  <-  27
MATCHED         hookspath  <-  28
MATCHED         hookspath-readers  <-  42
MATCHED         permission-mode  <-  30
MATCHED         parallel-cleared  <-  31
MATCHED         core-sweep  <-  34
MATCHED         journal-owner  <-  35
MATCHED         hook-fragments  <-  36, 41
MATCHED         resume-tick-consumers  <-  38
MATCHED         next-readers  <-  39
MATCHED         catalogue-duplicates  <-  43
MATCHED         gap-keys  <-  47
MATCHED         relaunch-cap  <-  48
MATCHED         hold-bound  <-  55
MATCHED         command-idempotence  <-  49
MATCHED         fencing  <-  50
MATCHED         reap-predicate  <-  51
MATCHED         deferral-fixtures  <-  53
MATCHED         cadence-period  <-  56
MATCHED         next-answers  <-  57
MATCHED         bash-improvisation  <-  58
reviewed 46/59
escaped 0/6
high 6/8
exit 0 · address-match lines 371

$ python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md --matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-b.md
replay: known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md · rows 65 · reviewed 59 · escaped 6 · high 8
replay: candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md · address matches 405
replay: matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-b.md · adjudicator the main loop of 2026-10-15, whose `[map]` placement in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` is read here and never revised · pairs 61 · tags 45
MATCHED         relaunch-replay  <-  1, 16, 50
MATCHED         driver-schema  <-  53
MATCHED         calls-per-act  <-  23
MATCHED         merge-back  <-  2
MATCHED         chain-overlap  <-  9, 31, 48
MATCHED         return-check-owner  <-  32
MATCHED         executor-map  <-  10
MATCHED         renewal-keys  <-  3
MATCHED         fixture-2-population  <-  4, 17, 40
MATCHED         hidden-spawns  <-  4, 20
MATCHED         inflight-count  <-  12, 54
MATCHED         unfailing-fixtures  <-  6
MATCHED         fail-closed-policy  <-  11
MATCHED         extension-enums  <-  13
MATCHED         invariant-8-fixture  <-  7
MATCHED         invariant-coverage  <-  7
MATCHED         cli-binary  <-  18
MATCHED         supervisor-host  <-  22
MATCHED         codex-events  <-  13
MATCHED         dispatcher-latency  <-  27
MATCHED         fanout-carrier  <-  29, 41
MATCHED         reap-key  <-  30, 42
MATCHED         resume-tick-seed  <-  28
MATCHED         hookspath  <-  26
MATCHED         hookspath-readers  <-  45
MATCHED         hook-fragments  <-  33
MATCHED         resume-tick-consumers  <-  43
MATCHED         catalogue-duplicates  <-  2, 37
MATCHED         relaunch-cap  <-  52
MATCHED         hold-bound  <-  52
MATCHED         fencing  <-  51
MATCHED         next-answers  <-  57
MATCHED         bash-improvisation  <-  58
MATCHED         cycle-spawns  <-  5
MATCHED         instance-witness  <-  8
MATCHED         structured-output  <-  15, 49
MATCHED         headless-workflow  <-  19
MATCHED         compact-target  <-  24, 46
MATCHED         user-guards  <-  25, 55
MATCHED         stopfailure-packs  <-  34, 39
MATCHED         deferral-seam  <-  35, 44
MATCHED         owner-rulings  <-  36
MATCHED         git-witness-readers  <-  56
MATCHED         return-write-path  <-  59
MATCHED         limit-hold  <-  60
reviewed 45/59
escaped 0/6
high 8/8
exit 0 · address-match lines 405

$ python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched fh1cal/weak-a.md
replay: known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md · rows 65 · reviewed 59 · escaped 6 · high 8
replay: candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md · address matches 371
replay: matched fh1cal/weak-a.md · adjudicator the main loop of 2026-10-15, whose `[map]` placement in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` is read here and never revised · pairs 30 · tags 27
MATCHED         relaunch-replay  <-  1
MATCHED         driver-schema  <-  2
MATCHED         calls-per-act  <-  21
MATCHED         chain-overlap  <-  4, 44
MATCHED         executor-map  <-  5
MATCHED         renewal-keys  <-  37
MATCHED         fixture-2-population  <-  17
MATCHED         hidden-spawns  <-  8
MATCHED         inflight-count  <-  8, 54
MATCHED         fail-closed-policy  <-  10
MATCHED         binding-events  <-  10
MATCHED         extension-enums  <-  11
MATCHED         invariant-8-fixture  <-  13
MATCHED         cli-floor-decision  <-  29
MATCHED         codex-events  <-  22
MATCHED         fanout-carrier  <-  25, 60
MATCHED         resume-tick-seed  <-  27
MATCHED         hookspath-readers  <-  42
MATCHED         parallel-cleared  <-  31
MATCHED         journal-owner  <-  35
MATCHED         hook-fragments  <-  41
MATCHED         next-readers  <-  39
MATCHED         gap-keys  <-  47
MATCHED         hold-bound  <-  55
MATCHED         fencing  <-  50
MATCHED         deferral-fixtures  <-  53
MATCHED         next-answers  <-  57
reviewed 27/59
escaped 0/6
high 4/8
exit 0 · address-match lines 371

$ python tools/workflows/review_replay.py --known-set fh1cal/cut.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-a.md
replay: REFUSED — known set: rows 64 against the population line's 65; reviewed 58 against the population line's 59
exit 2 · address-match lines 0

$ python tools/workflows/review_replay.py --known-set fh1cal/rep.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-matched-a.md
replay: REFUSED — known set: tag relaunch-replay is repeated
exit 2 · address-match lines 0

$ python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched fh1cal/cross.md
replay: REFUSED — pair 1 merge-back: the candidate's ref 'memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] Relaunch, [spawn] first bullet, [tests] fixture 3' cites no [isolate] of memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md
exit 2 · address-match lines 0

$ python tools/workflows/review_replay.py --known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md --candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md --matched fh1cal/twice.md
replay: known-set memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-known-set.md · rows 65 · reviewed 59 · escaped 6 · high 8
replay: candidate memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md · address matches 371
replay: matched fh1cal/twice.md · adjudicator the main loop of 2026-10-15, whose `[map]` placement in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` is read here and never revised · pairs 2 · tags 1
MATCHED         relaunch-replay  <-  1, 15
reviewed 1/59
escaped 0/6
high 1/8
exit 0 · address-match lines 371

~~~~

### Output: python fh1-control.py

~~~~text
memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md id 6 item H1 classes decision-re-derived-by-a-second-process · next memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-1-closing-diff-round2.md · fix none · shared none
memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md id 18 item M1 classes two-answers-to-one-question · next memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-1-closing-diff-round2.md · fix none · shared none
memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md id 19 item M6 classes a-merged-in-check-can-refuse-a-pinned-record · next memory/builds/aQuotedBrief/reviews/2026-10-09-review-TOOL-aQuotedBrief-1-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 3 item M4 classes a-grep-for-a-word-is-a-presence-probe · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 10 item M1 classes two-answers-to-one-question · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 11 item M3 classes decision-re-derived-by-a-second-process · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 13 item M6 classes two-answers-to-one-question · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 14 item L2 classes decision-re-derived-by-a-second-process · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 15 item L1 classes two-answers-to-one-question · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 16 item M2 classes two-guards-one-question-two-answers · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 17 item M1 classes two-guards-one-question-two-answers · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 18 item M7 classes containment-tested-one-way · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 20 item L2 classes two-guards-one-question-two-answers · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 22 item L6 classes two-guards-one-question-two-answers · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 24 item M2 classes sourced-conf-blank-overrides-the-default · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 25 item M1 classes two-readers-of-one-config-one-re-derived · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md id 26 item M9 classes two-readers-of-one-config-one-re-derived · next memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-3-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md id 8 item H4 classes C3 · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md id 9 item H1 classes C3 · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md id 11 item L1 classes C3 · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md id 2 item M1 classes two-answers-to-one-question · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md id 5 item M1 classes check-grades-one-layer-of-a-layered-config · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md id 7 item L1 classes amendment-leaves-its-other-half-standing · next memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md · fix none · shared none
memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md id 6 item L1 classes guard-above-a-fold-makes-its-fallback-dead · next memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md · fix none · shared none
memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md id 12 item M6 classes held-suite-guard-misses-a-sibling-kit · next memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md · fix none · shared none
memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md id 15 item M7 classes ab-arm-never-did-the-work · next memory/builds/dRedressedBar/reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md · fix none · shared ab-arm-never-did-the-work
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 1 item M1 classes name-search-resolves-a-namesake · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared none
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 4 item M3 classes decision-re-derived-by-a-second-process · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared none
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 5 item M2 classes fixture-passes-by-finding-nothing · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared fixture-passes-by-finding-nothing
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 6 item L3 classes invariant-held-on-one-admission-path · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared none
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 8 item M2 classes staged-break-substitutes-a-synthetic-value · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared none
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 11 item L4 classes two-answers-to-one-question · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared two-answers-to-one-question
memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md id 12 item L5 classes two-answers-to-one-question · next memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md · fix none · shared two-answers-to-one-question
memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md id 14 item L2 classes C17 · next memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md · fix none · shared none
memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md id 21 item M3 classes C9 · next memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md · fix none · shared none
memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md id 23 item B1 classes C10 · next memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md · fix f0e00195e fold(dSweptBranches): TOOL-dSweptBranches-3 rev-3 — the closing review's two blockers · shared none
PICK ('memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md', '23', 'B1', 'memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md', 'f0e00195e8b4745a2165baadd4444cb32b735591')
~~~~
