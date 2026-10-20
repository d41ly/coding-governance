# Research: the owner's hypothesis against gov's own history: how often updates would collide with tag-keyed edits

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 121's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-4-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md`.

---

Gov's own history mostly supports the hypothesis, with two corrections. A bare tag is not enough: 778 of the 797 text edits gov landed happened while the unit's anchor stayed the same, so a tag-only overlay would have reapplied the adopter's edit over changed text without telling anyone. And most orphaned edits came from four commits that restructured the charter or the role definitions, where the content was rewritten; no anchoring scheme or matcher can follow those. My pick is the tag plus a hash of gov's base text.

Every probe only read the repository. The scripts and their outputs lived in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors/`, and I deleted that directory at the end. The history covers the whole repository: 2026-07-01 to 2026-10-19, 6,094 commits, of which 686 touch these sources.

## 1. The segmenter, its commands, and unit counts

**Scope.**
- **Included:**
  - the charter `coding-governance-agents.template.md`, plus its earlier names `parallel-coding-governance.template.md`, `.domain-rules.md` and `.customize.md`, which were folded into it in 5b00666a2;
  - `tools/**/*.template.md`, except fixtures;
  - `tools/roles/agents/*.md` and `tools/roles/house/*.md`;
  - `tools/**/SKILL.template.md` and `skills/*/SKILL.md`;
  - HYGIENE and SPEC-TEMPLATE, at both `tools/memory-tree/` and the older `memory-tree/` path.
- **Excluded:** the `memory/guides/*.md` renders, the dated `-v-x-y` snapshots, and `tools/codebase-map/reuse-lookup.agent.md`.
- **Stamps stripped:** after a first run, I strip version-stamp lines such as `<!-- gov:kit unattended@1.106 -->`. They are rewritten on every version bump, so they had made the "(preamble)" unit the most-edited unit in every file.

`seg.py`, as run (it was a `<<'PYEOF'` heredoc plus a one-line patch for STAMP):
```python
TAG = re.compile(r'^\s*- \[([a-z0-9][a-z0-9-]*)\]\s')
HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
FIELD = re.compile(r'^([A-Za-z_][A-Za-z0-9_-]*):(\s|$)')
FENCE = re.compile(r'^\s*(```|~~~)')
STAMP = re.compile(r'^\s*<!-- (gov:kit |governance-template)')   # machine version stamps: not instructions

def segment(text):
    lines = text.replace('\r\n', '\n').split('\n')
    units = []          # [anchor, kind, [lines]]
    i = 0
    if lines and lines[0].strip() == '---':          # front matter: role fields
        j = 1
        while j < len(lines) and lines[j].strip() != '---':
            m = FIELD.match(lines[j])
            if m:
                units.append(['field:' + m.group(1), 'field', [lines[j][m.end(1)+1:]]])
            elif units:
                units[-1][2].append(lines[j])
            j += 1
        i = j + 1
    cur = ['(preamble)', 'preamble', []]
    units.append(cur)
    in_fence = False
    in_tag = False
    for ln in lines[i:]:
        if STAMP.match(ln):
            continue
        if FENCE.match(ln):
            in_fence = not in_fence
        if not in_fence:
            h = HEAD.match(ln)
            t = TAG.match(ln)
            if h:
                cur = ['H%d %s' % (len(h.group(1)), h.group(2)), 'heading', []]
                units.append(cur); in_tag = False; continue
            if t:
                cur = ['[%s]' % t.group(1), 'tag', [ln[t.end():]]]
                units.append(cur); in_tag = True; continue
            if in_tag and (ln.strip() == '' or re.match(r'^\s*([-*]|\d+\.)\s', ln) or ln.startswith('<!--')):
                parent = next(u for u in reversed(units) if u[1] in ('heading', 'preamble'))
                cur = parent; in_tag = False
        cur[2].append(ln)
    out, seen = [], {}
    for a, k, ls in units:
        body = '\n'.join(ls).strip('\n')
        if not ' '.join(body.split()):
            continue                                  # structural-only unit: dropped
        seen[a] = seen.get(a, 0) + 1
        out.append((a if seen[a] == 1 else '%s#%d' % (a, seen[a]), k, body))
    return out
```
`group_of(path)` sorts each path into one of five groups: charter, guides, hygiene+spec, roles or skills.

**Commands** (python3, chosen by `tools/lib/resolve-python.sh`; run from the worktree):
- `python3 count.py` gives the HEAD counts.
- `python3 walk.py landings landings.json` walks the first-parent chain: 215 commits listed, 214 with a change at unit level, in 1m24s.
- `python3 walk.py commits commits.json` walks every non-merge commit: 686 listed, 685 with a change at unit level, in 4m03s.
- `table.py`, `model.py`, `windows.py`, `schemes.py`, `simtest.py`, `retire_probe.py`, `bykind.py` and `sizes.py` then read those two JSON files.

**Unit counts at HEAD:**

| group | files | units | by anchor kind |
|---|---|---|---|
| charter | 1 | 56 | tag 46, heading 10 |
| guides | 8 | 105 | heading 105 |
| hygiene+spec | 2 | 29 | heading 29 |
| roles | 20 | 120 | field 110, body 10 (the 10 `house/*.md` files are empty) |
| skills | 9 | 91 | field 18, heading 73 |
| **total** | **40** | **401** | |

- **Unit size:** the median unit is 52 words, the 90th percentile 461 and the largest 5,321.
- **Largest units:** VERBS' whole H1 (5,321 words), HYGIENE's "The check catalog" (5,262) and PROTOCOL's "8. What a project declares" (2,131).

## 2. History table

Counts are unit events.

**Every non-merge commit** (685 updates, 2026-07-02 to 2026-10-13):

| group | text edits | anchor renames | splits | merges | moves | retirements | (added) |
|---|---|---|---|---|---|---|---|
| charter | 203 | 7 | 7 | 7 | 6 | 46 | 81 |
| guides | 485 | 6 | 2 | 1 | 2 | 1 | 102 |
| hygiene+spec | 180 | 3 | 0 | 1 | 0 | 0 | 28 |
| roles | 24 | 0 | 1 | 0 | 0 | 16 | 135 |
| skills | 290 | 6 | 4 | 0 | 0 | 6 | 97 |
| **total** | **1182** | **22** | **14** | **9** | **8** | **69** | 443 |

**First-parent landings** (214 updates):

| group | text edits | anchor renames | splits | merges | moves | retirements |
|---|---|---|---|---|---|---|
| charter | 168 | 7 | 7 | 7 | 6 | 46 |
| guides | 296 | 5 | 3 | 1 | 0 | 1 |
| hygiene+spec | 126 | 3 | 0 | 1 | 0 | 0 |
| roles | 18 | 0 | 1 | 0 | 0 | 10 |
| skills | 189 | 6 | 5 | 0 | 1 | 6 |
| **total** | **797** | **21** | **16** | **9** | **7** | **63** |

Other counts:
- Two files in the source set were renamed, which touched 23 units: the charter rename and `memory-tree/` moving to `tools/memory-tree/`.
- Whitespace-only edits: 6 per commit, 0 per landing.
- Edits that only changed a placeholder: 0.

**How the matcher works.** For each commit, it compares the parent and child versions of the files that changed. Git's `-M` detection follows file renames.
1. A unit matches when it keeps the same file and the same anchor.
2. Left-over old and new units are paired best-first by word-level similarity of at least 0.6. A pair counts as a rename, or as a move if the file changed.
3. A left-over unit whose 4-word shingles are at least 50% inside one new unit counts as merged into it. One spread across two or more new units (each at least 15%, together at least 50%) counts as split. A new unit at least 50% drawn from a unit that survived counts as split off from it.
4. Anything left over is retired, or added.

**What the matcher cannot see.**
- **Renames whose body was also rewritten.** These count as a retirement plus an addition. 50 of the 69 retirements keep less than 10% of their shingles anywhere, for example:
  - every §-section in 817ce1890 (v2.0) and 9ae1d023e (v4.0);
  - the roles' `charter: §3, §7, §9, §11, §12` field becoming `rules: yagni, reuse, …` in b61ec1c49 (10 fields).
- **Content moved to files outside the set,** for example kit bullets moved to `WIRE-INTO-PROJECT.md`.
- **Changes to meaning without a text change.**
- **Edits inside very large units.** A change anywhere in a 5,000-word section counts as one edit.
- **A heading's level change.** H2 to H3 counts as a rename.
- **Conflict resolutions made inside merge commits,** in the per-commit grain only. The landings grain includes them.
- **The tags have almost no history.** Rule tags only exist since v4.0 (9ae1d023e, 2026-10-09).

**Orphans come in bursts.** Only 34 of 685 commits orphan anything. Four commits carry 63 of the 102 orphan events: 817ce1890 (v2.0), 5b00666a2 (the charter fusion), 9ae1d023e (v4.0) and b61ec1c49 (the roles' `charter` field becoming `rules`).

## 3. Conflict and orphan rates

**Definitions.**
- **Conflict:** an amended unit's text changed while its anchor stayed.
- **Orphan:** an amended unit was renamed, moved, split, merged or retired. The parenthesised figure also counts file renames.
- **Uniform choice of units:** exact hypergeometric probability over the base.
- **Weighted choice:** the chance of picking a unit is proportional to its lineage's text-edit count over the whole history (floor 0.05), sampled 4,000 times per update. It uses future edits, so it is look-ahead.

| grain | k | uniform P(conflict) | uniform P(orphan) | weighted P(conflict) | weighted P(orphan) |
|---|---|---|---|---|---|
| per landing (214) | 5 | 0.131 | 0.0158 (0.0202) | 0.261 | 0.0152 (0.0205) |
| per landing | 20 | 0.334 | 0.0400 (0.0448) | 0.498 | 0.0478 (0.0527) |
| per commit (685) | 5 | 0.062 | 0.0053 (0.0066) | 0.167 | 0.0048 (0.0065) |
| per commit | 20 | 0.200 | 0.0136 (0.0151) | 0.405 | 0.0154 (0.0168) |
| landings, last 30 days (81) | 5 | 0.086 | 0.0094 | 0.237 | 0.0104 |
| landings, last 30 days | 20 | 0.222 | 0.0293 | 0.424 | 0.0360 |
| landings, tag era (22, includes v4.0) | 5 | 0.056 | 0.0212 | 0.269 | 0.0165 |
| landings, tag era | 20 | 0.179 | 0.0593 | 0.480 | 0.0579 |
| weekly pull (15 ISO weeks) | 5 | 0.700 | 0.176 | 0.858 | 0.207 |
| weekly pull | 20 | 0.936 | 0.326 | 0.975 | 0.353 |

**Edit and orphan rate per unit, each time its file is touched, by anchor kind (landings):**

| anchor kind | edited | orphaned | occurrences |
|---|---|---|---|
| heading | 0.071 | 0.0077 | 10,891 |
| field | 0.036 | 0.0273 | 366 |
| tag | 0.012 | 0 | 171 |

**What drives the conflict rate is unit size.** The units gov edits most are also the largest: PROTOCOL "8. What a project declares" was edited 68 times, and HYGIENE's check catalog 60 times.

## 4. The candidates, each with its losing test

**A. Tag only** (the key is file plus anchor).
- **Mechanism:** the adopter's edit attaches to the unit's tag and is reapplied on every update.
- **Test that would make it lose:** count updates where gov changed an amended unit's text while its anchor held. Tag-only cannot notice these.
- **Result: it loses.** 778 of 797 landing edits fall in this case and would pass silently. In 36 of them the anchor stayed but the body was largely replaced (similarity below 0.3).
- Its orphans are the same as B's.

**B. Tag plus a hash of the base text.**
- **Mechanism:** the edit also stores the hash of the gov text it was written against, so any later change to that text is flagged for re-review.
- **Test that would make it lose:** count false drift flags, then compare its orphan count with A's.
- **Result: it does not lose.**
  - A raw-byte hash gives 6 whitespace-only flags out of 1,182 commit-grain edits. A whitespace-normalised hash gives 0. Placeholder-only flags: 0.
  - It orphans exactly what A orphans: 22 renames or moves where the body survived, plus 72 other orphans per landing. In the tag era, tag units had 0 orphans; tags only moved position, for example when `[r1]` to `[links]` moved into section 1 in 05b48c3cb.
  - Its cost is that flags are coarse: 65% of flagged edits change less than 10% of the unit's words.

**C. Heading text, or position.**
- **Mechanism:** heading text is the same key as A, for every file except the charter. Position keys an edit by the unit's place in its file.
- **Test that would make heading text lose:** compare its orphan rate with the tag's, per anchor kind.
- **Result for heading text: it loses to the tag.**
  - Heading units are orphaned at 0.0077 per touch, tags at 0.
  - Heading text carries facts that change. Of the 22 renames, 12 kept their ID prefix (Step 5b, M4, "7.", Tier 1) but changed descriptive wording such as "≤5 agents" or "— 24".
  - Numbers are not stable either. §14 became §7, v2.0 renumbered all 16 § sections, and gov's own `charter: §3, …` references died at v4.0. That last case is gov itself losing an anchor of exactly this kind.
- **Test that would make position lose:** count units that survived but now sit at a different file or ordinal.
- **Result for position: it loses.** 268 of 11,366 surviving units moved, which is about 12 times the 22 anchor renames. Each of those would misapply an adopter edit silently.

**D. Content similarity.**
- **Mechanism:** the edit carries no key; the overlay finds its unit again by best fuzzy match on the base text.
- **Test T1:** re-find each edited unit whose anchor held.
- **Result T1: it loses.** 29 of 778 were matched to the wrong unit and 48 were lost below 0.6, a 9.9% failure rate. The ground truth here is anchor identity, which favours anchors.
- **Test T2:** look for near-duplicates at HEAD.
- **Result T2: it loses.** 34 of 401 units have a near-twin (similarity at least 0.8) somewhere else, such as role fields like `model: inherit` and `tools: Read, Grep, …`; 2 have one within their own file.
- It also cannot recover the bulk of the orphans, because 50 of the 69 retirements were rewritten beyond recognition.

## 5. Pick, and what it cannot see

**My pick is B: the tag plus a whitespace-normalised hash of the base text.**
- The key should be a declared ID that contains neither the heading wording nor a number.
- On an update, a changed hash raises a re-review flag. A missing anchor raises an orphan.
- Similarity is used only to suggest where an orphaned edit might belong, never to apply it.
- Because orphans come in bursts, the deployer should carry a rename and retirement map with each update that restructures. The v4.0 commit says it shipped "with a disposition for every v3.5 rule", so gov has produced such a map before. I have only seen that commit message, not the map.

**What this pick cannot see:**
- **Changes in meaning without a text change,** including a change elsewhere that alters what an amended unit means.
- **Restructures.** It turns them into orphans and cannot repair them; repair needs that map.
- **How noisy the re-review flags will be.** That depends on how big units are, and the hot units are thousands of words. Finer units would cut conflicts, but I did not measure that.
- **Long-term tag stability.** The tag evidence is 10 days and 22 landings long.
- **Template versus rendered text.** The hash covers template text, while adopters edit what was rendered from it.
- **Additive overlays, which these rates do not cover.** Two such seams exist today: `tools/roles/house/<role>.md`, read by `render_agents.py` (all 10 are empty), and `{{ADOPTER_RULES}}` in charter section 2. They append rather than amend, so they cannot collide with gov's text by construction.
