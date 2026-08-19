#!/usr/bin/env python3
"""render_playbook.py — fill the governance charter template into a target's charter.

WHAT THIS REPLACES. The charter used to ship with a prose companion telling an agent to fill 28
placeholders by hand and delete the conditional blocks their project had no kit for. That companion
is retired: filling is mechanical, so it is a program's job, and what a program cannot decide moved
to the runbook.

THE THREE CLASSES. Every placeholder is DECLARED in the playbook entry's govkit descriptor as one of:

  derived    a named probe here computes it from the target repo. The render PRINTS what it derived,
             so a wrong derivation is visible rather than silent. A probe returning nothing falls
             through to REFUSAL, never to a default it did not declare — a probe that quietly returns
             the empty string is how a charter ships with a blank where a branch name belongs.
  asked      it must come from the target's deploy.toml answers table. Absent is a refusal NAMING the
             key. Nothing is guessed; that posture is govkit's and this engine inherits it.
  defaulted  a declared default applies, and the render RECORDS that it defaulted. A default silently
             identical to an answer is how an operator ships a value they never chose.

TWO FENCE NAMESPACES, AND NEITHER READS A BOOLEAN.
  <!-- kit:<id> -->      drops when <id> is absent from deploy.toml's `kits`.
  <!-- when:<name> -->   drops when <name> is a MEMBER of deploy.toml's `drop_blocks`.

`drop_blocks` is a LIST, not a set of booleans, and that is load-bearing. govkit's intake writes
every answer as `key = "value"`, so a key "answered false" arrives as the STRING `false` — truthy
under every natural reading — and the block would survive. That is the failure that reads as success,
arriving through type coercion rather than through a name. Membership has no such reading.

Both namespaces REFUSE rather than skip: a `kit:` fence naming a non-entry, a `when:` fence naming an
undeclared block, a `drop_blocks` member matching no fence, and a `kits` member that is not a
registry entry id are each a refusal. An unrecognised name that merely left the block in place would
be a silent no-op.

THE TWO NAMESPACES ARE NOT SYMMETRIC ON THE FENCE SIDE, and that is measured rather than sloppy. A
`drop_blocks` member matching no fence is a typo by construction — the list exists only to name
fences. A `kits` member matching no fence is the NORMAL case: gov selects twenty entries and the
charter carries three `kit:` fences, because most kits have no conditional ruleset. So `kits` is
graded against the REGISTRY, which is the population it is drawn from, and an empty `kits` under an
existing deploy.toml is itself a refusal — it silently drops every conditional block, and intake
cannot write one (`resolve_selection` refuses an empty selection), so it can only be a hand edit.

WHERE THE INPUTS COME FROM, AND WHY IT IS NOT `__file__`'s GRANDPARENT. This engine ships into a
target at `{prefix}/playbook/`, so its grandparent there is the TARGET's repo root — which holds
neither `tools/govkit/entries/playbook.kit.toml` (a registry exemption that never lands in a target)
nor a repo-root charter template (the deployer lands it at the operator-chosen `playbook_path`).
Resolving from the grandparent worked in gov and died in every adopter with an uncaught
FileNotFoundError, straight past `main`'s `except Refusal`. So: the DECLARATIONS are read from beside
the engine when the kit shipped them there and from gov's own tree otherwise, the TEMPLATE from the
target's `playbook_path` answer when it has one, and every one of those reads REFUSES naming the path
it wanted. A missing input is a stated reason, never a traceback.

THE REGION READER IS THIS FILE'S OWN. The memory-tree kit's region helper RAISES when no marker pair
is present, so it serves neither the absent-charter nor the charter-without-a-region state. This
engine therefore CONFORMS to the marker-region contract and adds a fifth reader to its case table; it
does not import that implementation, which would be a cross-kit edge the contract itself forbids.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

OPEN_RE = re.compile(r'^[ \t]*<!--\s*(kit|when):([A-Za-z0-9_-]+)\s*-->[ \t]*$')
CLOSE_RE = re.compile(r'^[ \t]*<!--\s*/(kit|when):([A-Za-z0-9_-]+)\s*-->[ \t]*$')
PLACEHOLDER_RE = re.compile(r'\{\{([A-Z][A-Z0-9_]*)\}\}')
REGION_OPEN = '<!-- gov:playbook -->'
REGION_CLOSE = '<!-- /gov:playbook -->'


class Refusal(Exception):
    """A stated reason to write nothing. Every one names what the operator must supply."""


# --------------------------------------------------------------------------- derivation probes
def read_git(root: Path, *args: str) -> str:
    """Run git in the target and return stdout, or the empty string when it cannot answer."""
    try:
        r = subprocess.run(['git', '-C', root.as_posix(), *args],
                           capture_output=True, text=True, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ''
    except (OSError, subprocess.SubprocessError):
        return ''


def read_conf(root: Path, name: str, key: str) -> str:
    """Read one KEY=value out of a shell-style conf, without sourcing it."""
    p = root / name
    if not p.is_file():
        return ''
    for line in p.read_text(encoding='utf-8', errors='replace').splitlines():
        line = line.strip()
        if line.startswith(f'{key}='):
            return line[len(key) + 1:].strip().strip('"').strip("'")
    return ''


def derive_project_name(root: Path, _a: dict) -> str:
    # The PRIMARY tree's name, never the current directory's. `root.resolve().name` answers whatever
    # worktree the render ran in, so a render from a throwaway branch dir baked that dir's name into a
    # committed charter as the product's identity — and the next render from anywhere else produced a
    # different region, redding the unguarded wiring leg. Same worktree-sensitivity `derive_primary_tree`
    # already carries a comment about, missed one function away.
    return Path(derive_primary_tree(root, _a)).name or root.resolve().name


def derive_default_branch(root: Path, _a: dict) -> str:
    ref = read_git(root, 'symbolic-ref', '--short', 'refs/remotes/origin/HEAD')
    if ref:
        return ref.split('/', 1)[-1]
    for cand in ('main', 'master'):
        if read_git(root, 'rev-parse', '--verify', '--quiet', cand):
            return cand
    return ''


def derive_memory_root(root: Path, _a: dict) -> str:
    return read_conf(root, '.memory-tree.conf', 'MEMORY_ROOT') or 'memory'


def derive_memory_disciplines(root: Path, _a: dict) -> str:
    return read_conf(root, '.memory-tree.conf', 'DISCIPLINES')


def derive_id_families(root: Path, _a: dict) -> str:
    return read_conf(root, '.memory-tree.conf', 'FAMILIES')


def derive_ci_file(root: Path, _a: dict) -> str:
    d = root / '.github' / 'workflows'
    if d.is_dir():
        hits = sorted(p.name for p in d.iterdir() if p.suffix in ('.yml', '.yaml'))
        if hits:
            return f'.github/workflows/{hits[0]}'
    return ''


def derive_gate_runner(root: Path, _a: dict) -> str:
    for cand in ('tools/run-gates.sh', 'scripts/run-gates.sh', 'scripts/gate.sh'):
        if (root / cand).is_file():
            return f'bash {cand}'
    return ''


def derive_lexicon_conf(root: Path, _a: dict) -> str:
    return '.lexicon.conf' if (root / '.lexicon.conf').is_file() else ''


def derive_node_tag(_r: Path, _a: dict) -> str:
    return 'a'


# NO `derive_machine`. It read $USERNAME/$COMPUTERNAME and baked one node's identity into a charter
# committed to a shared remote, so every other node's render differed and the unguarded wiring leg
# red for them — and the only in-band fix rewrites a file with no row-merge driver, hard-conflicting
# on every cross-node merge. MACHINE_A is an ASKED placeholder now: the node registry is fleet data
# the operator states, exactly like VARIANCES_A beside it. Ambient environment is not a derivation.


def derive_primary_tree(root: Path, _a: dict) -> str:
    # The PRIMARY tree, not whichever worktree this render runs from. `--show-toplevel` answers the
    # linked worktree, so a render performed inside one would register that worktree as the node's
    # primary tree — measured on gov's own first render. `--git-common-dir` points at the main
    # repository's .git wherever it is run, and its parent is the primary checkout.
    common = read_git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir')
    if common:
        return Path(common).parent.as_posix()
    top = read_git(root, 'rev-parse', '--show-toplevel')
    return top or root.resolve().as_posix()


def derive_worktree_root(root: Path, _a: dict) -> str:
    primary = derive_primary_tree(root, _a)
    return f'{primary}/.claude/worktrees' if primary else ''


PROBES = {
    'project_name': derive_project_name,
    'default_branch': derive_default_branch,
    'memory_root': derive_memory_root,
    'memory_disciplines': derive_memory_disciplines,
    'id_families': derive_id_families,
    'ci_file': derive_ci_file,
    'gate_runner': derive_gate_runner,
    'lexicon_conf': derive_lexicon_conf,
    'node_tag': derive_node_tag,
    'primary_tree': derive_primary_tree,
    'worktree_root': derive_worktree_root,
}


# --------------------------------------------------------------------------- the fence pass
def check_fences(text: str, entries: set[str], blocks: set[str]) -> list[tuple[str, str]]:
    """Return every (namespace, name) fence, refusing on an unbalanced or undeclared one."""
    stack, seen = [], []
    for n, line in enumerate(text.splitlines(), 1):
        m = OPEN_RE.match(line)
        if m:
            ns, name = m.group(1), m.group(2)
            if ns == 'kit' and name not in entries:
                raise Refusal(f'line {n}: a kit fence names `{name}`, which is not a registry entry '
                              f'id. An unrecognised id would leave the block in place, which is the '
                              f'failure that reads as success')
            if ns == 'when' and name not in blocks:
                raise Refusal(f'line {n}: a when fence names `{name}`, which the descriptor declares '
                              f'nowhere. Declare it as a [[block]] row or remove the fence')
            stack.append((ns, name, n))
            seen.append((ns, name))
            continue
        m = CLOSE_RE.match(line)
        if m:
            if not stack:
                raise Refusal(f'line {n}: a closing fence with no opener: {m.group(1)}:{m.group(2)}')
            ons, oname, _ = stack.pop()
            if (ons, oname) != (m.group(1), m.group(2)):
                raise Refusal(f'line {n}: fence closes {m.group(1)}:{m.group(2)} but the open one is '
                              f'{ons}:{oname}')
    if stack:
        ns, name, n = stack[-1]
        raise Refusal(f'line {n}: fence {ns}:{name} is never closed')
    return seen


def remove_fenced(text: str, drop: set[tuple[str, str]]) -> str:
    """Remove every fenced block whose (namespace, name) is in `drop`, fences included."""
    out, skip_depth = [], 0
    for line in text.splitlines(keepends=True):
        m = OPEN_RE.match(line.rstrip('\n'))
        if m:
            key = (m.group(1), m.group(2))
            if skip_depth or key in drop:
                skip_depth += 1
            continue          # a SURVIVING block loses its markers; a dropped one loses its body too
        m = CLOSE_RE.match(line.rstrip('\n'))
        if m:
            if skip_depth:
                skip_depth -= 1
            continue
        if not skip_depth:
            out.append(line)
    return ''.join(out)


# --------------------------------------------------------------------------- substitution
TABLE_ROW_RE = re.compile(r'^[ \t]*\|')


def build_substitution(text: str, key: str, val: str) -> str:
    """Replace every `{{KEY}}` with `val`, escaped for the HOST CONTEXT of each occurrence.

    A markdown TABLE ROW is a structured host and a verbatim substitution corrupts it: an unescaped
    `|` opens a cell the template never declared, and a newline ends the row early. Measured on gov's
    own §2 node registry, which is the table an agent is told to identify its node from.

    Per OCCURRENCE, not per key: one key can land in a table cell and in prose in the same charter,
    and `\\|` in prose is a backslash a reader sees. What is NOT handled, said plainly rather than
    implied away: a backtick in a value the TEMPLATE wrapped in backticks mangles the code span, and
    no escape fixes that inside one — CommonMark's answer is a longer delimiter run, which is the
    template author's decision. The fix for that class is to stop wrapping free-text cells, which is
    what `{{VARIANCES_A}}` now is.
    """
    token = '{{' + key + '}}'
    if token not in text:
        return text
    out = []
    for line in text.split('\n'):
        if token in line and TABLE_ROW_RE.match(line):
            if '\n' in val or '\r' in val:
                raise Refusal(f'the answer for {key} carries a newline and the template puts it in a '
                              f'table row, which the newline would end early. Give a single-line '
                              f'answer for a cell')
            out.append(line.replace(token, val.replace('|', r'\|')))
        else:
            out.append(line.replace(token, val))
    return '\n'.join(out)


# --------------------------------------------------------------------------- the region reader
def build_region(charter: str | None, body: str) -> str:
    """Write `body` between the region markers. THREE states, and this reader serves all of them.

    absent charter          -> a file holding only the region
    charter, no region      -> the region appended, every authored byte untouched
    charter with a region   -> the region's contents replaced and nothing else
    """
    block = f'{REGION_OPEN}\n{body.rstrip()}\n{REGION_CLOSE}\n'
    if charter is None:
        return block
    if REGION_OPEN not in charter:
        sep = '' if charter.endswith('\n\n') else ('\n' if charter.endswith('\n') else '\n\n')
        return charter + sep + block
    if charter.count(REGION_OPEN) != 1 or charter.count(REGION_CLOSE) != 1:
        raise Refusal('the charter carries more than one gov:playbook region, so which one the render '
                      'replaces is a matter of scan order')
    head = charter.split(REGION_OPEN)[0]
    tail = charter.split(REGION_CLOSE, 1)[1]
    return head + block.rstrip('\n') + tail


# --------------------------------------------------------------------------- the render
def read_input(path: Path, what: str) -> str:
    """Read a REQUIRED input, or refuse naming the path. Every miss here used to be a traceback."""
    try:
        return path.read_text(encoding='utf-8')
    except OSError as e:
        raise Refusal(f'{what} is not readable at {path.as_posix()} ({e.strerror}). Supply that '
                      f'path — the render has nothing to read and will not guess one')


def resolve_declaration_paths(engine_dir: Path, gov_root: Path) -> tuple[Path, Path]:
    """The descriptor and the registry, from the INSTALLED layout first and gov's own second.

    An installed kit carries both beside the engine, because `tools/govkit/` is a registry exemption
    that never lands in a target. Gov has no copy beside the engine and falls through to its own
    tree, which is what keeps one source of truth for these two files.
    """
    desc = engine_dir / 'playbook.kit.toml'
    reg = engine_dir / 'registry.toml'
    return (desc if desc.is_file() else gov_root / 'tools' / 'govkit' / 'entries' / desc.name,
            reg if reg.is_file() else gov_root / 'tools' / 'govkit' / reg.name)


def resolve_template_path(gov_root: Path, target: Path, answers: dict) -> Path:
    """The charter TEMPLATE this render reads.

    The deployer lands it at the operator-chosen `playbook_path`, so that answer is authoritative
    when a target has one — and when it names a file that is not there, the read REFUSES rather than
    silently falling back to gov's copy, which would render somebody else's template.
    """
    p = answers.get('playbook_path')
    if isinstance(p, str) and p:
        return target / p
    return gov_root / 'coding-governance-agents.template.md'


def load_declarations(desc_path: Path, reg_path: Path) -> tuple[dict, list[dict], set[str]]:
    desc = tomllib.loads(read_input(desc_path, "the playbook entry's descriptor"))
    reg = tomllib.loads(read_input(reg_path, 'the govkit registry'))
    entries = {e['id'] for e in reg.get('entry', [])}
    return desc, desc.get('block', []), entries


def render(engine_dir: Path, gov_root: Path, target: Path) -> tuple[str, list[str]]:
    desc, blocks, entries = load_declarations(*resolve_declaration_paths(engine_dir, gov_root))
    dep = target / '.governance' / 'deploy.toml'
    if not dep.is_file():
        raise Refusal(f'{dep.as_posix()} does not exist. Run `govkit intake` first — it writes the '
                      f'answers this render reads, once, and refuses to overwrite them afterwards')
    cfg = tomllib.loads(dep.read_text(encoding='utf-8'))
    answers = {k.lower(): v for k, v in (cfg.get('answers') or {}).items()}
    kits = set(cfg.get('kits') or [])
    drop_names = list(cfg.get('drop_blocks') or [])

    # THE `kits` ARRAY IS GRADED, and it was not. A member is a registry entry id — that is the
    # population it is drawn from — and an unrecognised one selects nothing, so the whole kit section
    # it was meant to keep is DROPPED and `--check` re-renders from the same file and stays green
    # forever. Measured: rewriting `codebase-map` to `codebasemap` deleted the entire codebase-map
    # ruleset from the charter with no word said. The adjacent `drop_blocks` loop refused exactly
    # this shape two lines down; the symmetry gap between them is the defect.
    if not kits:
        raise Refusal(f'{dep.as_posix()} declares no `kits`, so every kit: fence in the template '
                      f'would drop and the charter would lose every conditional ruleset silently. '
                      f'Intake cannot write an empty selection, so this is a hand edit')
    unknown = sorted(k for k in kits if k not in entries)
    if unknown:
        raise Refusal(f'`kits` names {", ".join(unknown)}, which {"is" if len(unknown) == 1 else "are"} '
                      f'not a registry entry id. An unrecognised member selects nothing, so a kit '
                      f'fence it was meant to keep drops instead — the failure that reads as success')

    declared_blocks = {b['name'] for b in blocks}
    for d in drop_names:
        if d not in declared_blocks:
            raise Refusal(f'drop_blocks names `{d}`, which the descriptor declares nowhere. A member '
                          f'that drops nothing is a typo or a block that has already gone')

    template = resolve_template_path(gov_root, target, answers)
    text = read_input(template, 'the charter template')
    present = check_fences(text, entries, declared_blocks)
    for d in drop_names:
        if ('when', d) not in present:
            raise Refusal(f'drop_blocks names `{d}` but no when fence in the template carries it')

    drop = {('kit', name) for ns, name in present if ns == 'kit' and name not in kits}
    drop |= {('when', d) for d in drop_names}
    text = remove_fenced(text, drop)

    notes = []
    rows = desc.get('placeholder', [])
    by_key = {r['key']: r for r in rows}
    for key in sorted(set(PLACEHOLDER_RE.findall(text))):
        row = by_key.get(key)
        if row is None:
            raise Refusal(f'the template carries {{{{{key}}}}} and the descriptor declares no '
                          f'[[placeholder]] row for it, so nothing can supply a value')
        cls = row.get('class')
        if cls == 'derived':
            probe = PROBES.get(row.get('probe', ''))
            if probe is None:
                raise Refusal(f'{key} declares probe `{row.get("probe")}`, which this engine does '
                              f'not define')
            val = probe(target, answers)
            if not val:
                # AN EXPLICIT ANSWER OVERRIDES A PROBE THAT CANNOT SEE. Gov's own first render found
                # this: it has no CI workflow yet, so `ci_file` derived to nothing and the refusal
                # told the operator to "supply it as an answer" — which the engine then did not
                # honour. A message naming an escape the code does not implement is worse than no
                # escape. What is still refused is the SILENT case: probe empty AND no answer.
                val = answers.get(key.lower()) or ''
                if not val:
                    raise Refusal(f'{key} is derived by probe `{row["probe"]}`, it returned nothing '
                                  f'for this target, and no answer overrides it. Supply it under '
                                  f'[answers] rather than shipping a blank')
                notes.append(f'override  {key} = {val}   (probe saw nothing)')
            else:
                notes.append(f'derived   {key} = {val}')
        elif cls == 'asked':
            val = answers.get(key.lower())
            if val in (None, ''):
                raise Refusal(f'{key} is an ASKED placeholder and {dep.as_posix()} supplies no value '
                              f'for it. Refusing to invent one: an answer this tool guesses is one '
                              f'the operator never made and cannot audit')
            notes.append(f'answered  {key}')
        elif cls == 'defaulted':
            val = answers.get(key.lower()) or row.get('default', '')
            if not val:
                raise Refusal(f'{key} is defaulted and its declared default is empty')
            if not answers.get(key.lower()):
                notes.append(f'DEFAULTED {key} = {val}   (no answer supplied)')
            else:
                notes.append(f'answered  {key}')
        else:
            raise Refusal(f'{key} declares class `{cls}`, which is not derived, asked or defaulted')
        text = build_substitution(text, key, str(val))
    for ns, name in sorted(set(present)):
        if (ns, name) in drop:
            notes.append(f'dropped   {ns}:{name}')
    return text, notes


# --------------------------------------------------------------------------- the arms
# WHY THE FIXTURE IS NOT GOV'S OWN TREE. Every arm below is about a WRONG input, and gov's committed
# `deploy.toml` is a right one — so proving a refusal here would mean corrupting the repo's own
# answers and putting them back. The fixture is a three-file scratch target instead: a descriptor, a
# registry and a template, each holding only what the arm under test reads.
DESC_FIXTURE = '''
[[placeholder]]
key = "VARIANCES_A"
class = "asked"

[[block]]
name = "security"
'''
REG_FIXTURE = '[[entry]]\nid = "lexicon"\n\n[[entry]]\nid = "codebase-map"\n'
TPL_FIXTURE = '''| Tag | Variances |
|-----|-----------|
| `a` | {{VARIANCES_A}} |

<!-- kit:codebase-map -->
the codebase-map ruleset
<!-- /kit:codebase-map -->
'''


def _write_fixture(tmp: Path, kits: str, variances: str) -> tuple[Path, Path]:
    """Write a scratch engine dir + target and return both. `kits` is TOML array source."""
    eng, tgt = tmp / 'engine', tmp / 'target'
    (eng).mkdir(parents=True, exist_ok=True)
    (tgt / '.governance').mkdir(parents=True, exist_ok=True)
    (eng / 'playbook.kit.toml').write_text(DESC_FIXTURE, encoding='utf-8')
    (eng / 'registry.toml').write_text(REG_FIXTURE, encoding='utf-8')
    (tgt / 'CHARTER.md').write_text(TPL_FIXTURE, encoding='utf-8')
    (tgt / '.governance' / 'deploy.toml').write_text(
        f'kits = {kits}\n\n[answers]\nplaybook_path = "CHARTER.md"\n'
        f'variances_a = {variances}\n', encoding='utf-8')
    return eng, tgt


def run_selftest() -> int:
    import tempfile
    passed, failed = 0, 0

    def arm(name: str, kits: str, variances: str, want: str | None, in_body: str = ''):
        nonlocal passed, failed
        with tempfile.TemporaryDirectory() as td:
            eng, tgt = _write_fixture(Path(td), kits, variances)
            try:
                body, _ = render(eng, Path(td), tgt)
                got = None
            except Refusal as e:
                body, got = '', str(e)
        if want is None:
            ok = got is None and in_body in body
            detail = f'refused: {got}' if got else f'body lacks {in_body!r}'
        else:
            ok = got is not None and want in got
            detail = 'no refusal at all' if got is None else f'refused with: {got}'
        if ok:
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL {name} — {detail}')
    ok_kits, ok_var = '["codebase-map", "lexicon"]', '"plain"'

    # H2 — the `kits` array is graded against the registry, in both failing directions.
    arm('a green render survives its own fixture', ok_kits, ok_var, None,
        in_body='the codebase-map ruleset')
    arm('a misspelled kit id is a refusal, not a silently dropped section',
        '["codebasemap", "lexicon"]', ok_var, 'not a registry entry id')
    arm('the misspelling does NOT reach the render', '["codebasemap"]', ok_var, 'codebasemap')
    arm('an empty kits array is a refusal, not a charter with every block dropped',
        '[]', ok_var, 'declares no `kits`')

    # M2 — substitution into a table row is escaped, and a newline in a cell is refused.
    arm('a pipe in a table-cell answer is escaped, so the row keeps its cells',
        ok_kits, '"a | pipe"', None, in_body=r'| `a` | a \| pipe |')
    arm('a backtick in a table-cell answer survives as its own code span',
        ok_kits, '"remote `origin`"', None, in_body='| `a` | remote `origin` |')
    arm('a newline in a table-cell answer is a refusal',
        ok_kits, '"""two\nlines"""', 'carries a newline')

    # The escape is per OCCURRENCE: prose must not gain a backslash.
    with tempfile.TemporaryDirectory() as td:
        eng, tgt = _write_fixture(Path(td), ok_kits, '"a | pipe"')
        (tgt / 'CHARTER.md').write_text('prose {{VARIANCES_A}} here\n', encoding='utf-8')
        body, _ = render(eng, Path(td), tgt)
        if body.strip() == 'prose a | pipe here':
            passed += 1
        else:
            failed += 1
            print(f'  arm FAIL a pipe in PROSE is left alone — got {body.strip()!r}')

    if failed:
        print(f'render_playbook.selftest FAILED — {failed} of {passed + failed} arm(s)')
        return 1
    print(f'render_playbook.selftest OK — {passed} arm(s)')
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--target')
    ap.add_argument('--charter', default='AGENTS.md')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args(argv)

    if a.selftest:
        return run_selftest()
    if not a.target:
        ap.error('--target is required')

    engine_dir = Path(__file__).resolve().parent
    gov_root = engine_dir.parent.parent
    target = Path(a.target).resolve()
    charter_path = target / a.charter

    # NOT ADOPTED is exit 0, and only in --check. A wiring leg runs unguarded against a tree that
    # has not run intake yet — gov's own, until its charter is rendered — and a leg that refuses
    # there is red for a reason that is not drift. It says so explicitly rather than passing
    # silently, because a leg green for "nothing was measured" is the shape this repo refuses.
    # Writing without a descriptor still REFUSES: that is an operator asking for a render.
    if a.check and not (target / '.governance' / 'deploy.toml').is_file():
        print(f'render-playbook: NOT ADOPTED — {target.as_posix()} has no .governance/deploy.toml, '
              f'so no region was rendered here and there is nothing to compare')
        return 0

    try:
        body, notes = render(engine_dir, gov_root, target)
    except Refusal as e:
        print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
        return 1

    survived = PLACEHOLDER_RE.findall(body)

    if a.check:
        rc = 0
        # PARITY and PLACEHOLDER COMPLETENESS are two questions, and a render whose descriptor
        # declares nothing for a key is perfectly in sync while telling the agent to invoke a
        # placeholder's name. They fail separately, with separate messages.
        if not charter_path.is_file():
            print(f'render-playbook: {charter_path.as_posix()} does not exist, so there is no region '
                  f'to compare', file=sys.stderr)
            return 1
        cur = charter_path.read_text(encoding='utf-8')
        want = build_region(cur, body)
        # NORMALISE line endings before comparing. This fleet runs core.autocrlf=true and a charter
        # with no eol attribute holds CRLF in the worktree against an LF blob, so a raw compare
        # mismatches on every line for a reason that has nothing to do with drift.
        if cur.replace('\r\n', '\n') != want.replace('\r\n', '\n'):
            print('render-playbook: DRIFT — the charter region differs from a fresh render',
                  file=sys.stderr)
            rc = 1
        if survived:
            print(f'render-playbook: SURVIVING PLACEHOLDER in the render: '
                  f'{", ".join(sorted(set(survived)))}', file=sys.stderr)
            rc = 1
        if rc == 0:
            print(f'render-playbook OK — region matches a fresh render, no placeholder survived')
        return rc

    if survived:
        print(f'render-playbook: REFUSED — placeholders survived the render: '
              f'{", ".join(sorted(set(survived)))}', file=sys.stderr)
        return 1
    cur = charter_path.read_text(encoding='utf-8') if charter_path.is_file() else None
    charter_path.parent.mkdir(parents=True, exist_ok=True)
    charter_path.write_text(build_region(cur, body), encoding='utf-8', newline='\n')
    for n in notes:
        print(f'  {n}')
    print(f'render-playbook — wrote the gov:playbook region into {charter_path.as_posix()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

KIT_PLAYBOOK_RENDER_VERSION = "1.0"
