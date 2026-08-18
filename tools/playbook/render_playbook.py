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
undeclared block, and a `drop_blocks` member matching no fence are each a refusal. An unrecognised
name that merely left the block in place would be a silent no-op.

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
    return root.resolve().name


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


def derive_machine(_r: Path, _a: dict) -> str:
    user = os.environ.get('USERNAME') or os.environ.get('USER') or ''
    host = os.environ.get('COMPUTERNAME') or os.environ.get('HOSTNAME') or ''
    return f'{user} @ {host}'.strip(' @') if (user or host) else ''


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
    'machine': derive_machine,
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
    out, skip_depth, keep_fences = [], 0, True
    for line in text.splitlines(keepends=True):
        m = OPEN_RE.match(line.rstrip('\n'))
        if m:
            key = (m.group(1), m.group(2))
            if skip_depth or key in drop:
                skip_depth += 1
                continue
            keep_fences = False  # a surviving block loses its markers in the render
            continue
        m = CLOSE_RE.match(line.rstrip('\n'))
        if m:
            if skip_depth:
                skip_depth -= 1
                continue
            continue
        if not skip_depth:
            out.append(line)
    del keep_fences
    return ''.join(out)


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
def load_declarations(gov_root: Path) -> tuple[dict, list[dict], set[str]]:
    desc = tomllib.loads((gov_root / 'tools' / 'govkit' / 'entries' / 'playbook.kit.toml')
                         .read_text(encoding='utf-8'))
    reg = tomllib.loads((gov_root / 'tools' / 'govkit' / 'registry.toml').read_text(encoding='utf-8'))
    entries = {e['id'] for e in reg.get('entry', [])}
    return desc, desc.get('block', []), entries


def render(gov_root: Path, target: Path, template: Path) -> tuple[str, list[str]]:
    desc, blocks, entries = load_declarations(gov_root)
    dep = target / '.governance' / 'deploy.toml'
    if not dep.is_file():
        raise Refusal(f'{dep.as_posix()} does not exist. Run `govkit intake` first — it writes the '
                      f'answers this render reads, once, and refuses to overwrite them afterwards')
    cfg = tomllib.loads(dep.read_text(encoding='utf-8'))
    answers = {k.lower(): v for k, v in (cfg.get('answers') or {}).items()}
    kits = set(cfg.get('kits') or [])
    drop_names = list(cfg.get('drop_blocks') or [])

    declared_blocks = {b['name'] for b in blocks}
    for d in drop_names:
        if d not in declared_blocks:
            raise Refusal(f'drop_blocks names `{d}`, which the descriptor declares nowhere. A member '
                          f'that drops nothing is a typo or a block that has already gone')

    text = template.read_text(encoding='utf-8')
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
        text = text.replace('{{' + key + '}}', str(val))
    for ns, name in sorted(set(present)):
        if (ns, name) in drop:
            notes.append(f'dropped   {ns}:{name}')
    return text, notes


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--target', required=True)
    ap.add_argument('--charter', default='AGENTS.md')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)

    gov_root = Path(__file__).resolve().parent.parent.parent
    target = Path(a.target).resolve()
    template = gov_root / 'coding-governance-agents.template.md'
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
        body, notes = render(gov_root, target, template)
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
