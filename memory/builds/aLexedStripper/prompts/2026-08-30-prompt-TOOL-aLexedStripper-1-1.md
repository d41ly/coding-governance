# The owner's prompt — two kit degradations another session found

**Serves:** research TOOL-aLexedStripper-1

Handed to `/unattended --prompt` on 2026-08-30, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is reproduced VERBATIM below. The bytes travel rather
than a reference: the build folder is the authorization, so it may not point at a file that can be
edited after the run starts.

## Verbatim

> Another session found two serious kit degradations:
>
> * codebase-map's _identifier_tokens (ABL-bCandidLoupe-1) is the worst functional damage here —
>   main.py goes 1616 identifier tokens → 88, so the charter-mandated DoR reuse audit is effectively
>   blind on Python. But map_lib.py is role engine. Patching it means flipping the role, inserting a
>   KIT_CODEBASE_MAP_DELTA marker, which moves the blob OID, which reds kit-sync's check 8, which
>   needs the install.index regeneration that ABL-dPinnedVintage-3 owns — and that row is BLOCKED.
>   ABL-dPinnedVintage-5 §8 F3 already walked exactly this trap for extract.py and chose upstream
>   instead.
> * agent-cap's false-positive denial is gov-side by the same logic.
>
> Review the findings, verify, resolve any blockers and fix them.

## What the prompt names, and where each id lives

The `ABL-` family is NOT this repo's. It is the adopter `d41ly/incms`, checked out at
`C:/projects/incms/main`, whose backlog is `memory/backlog/ABL.md` there. Every id the prompt cites
resolves in that tree and none of them resolves here, which is why they are recorded rather than
looked up:

| Id | Where | What it says |
|---|---|---|
| `ABL-bCandidLoupe-1` | `memory/backlog/ABL.md:263` · OPEN | `_identifier_tokens` strips C block comments from Python too; `main.py` loses 81.3% of identifiers; 24 `.py` files affected; corrupts the DoR reuse audit; survived the kit 1.1 sync |
| `ABL-dPinnedVintage-3` | `memory/backlog/ABL.md:444` · BLOCKED | `kits.json` sheds its `files` array, `install.index` and `row-count.txt` retire — the regeneration the local-patch route would have to wait on |
| `ABL-dPinnedVintage-4` | `memory/backlog/ABL.md:445` · OPEN | the agent-cap half, filed explicitly as a **gov ask**: 1.6 denies a correct 5-lens harness because its bounded proof blanks quoted strings per line |
| `ABL-dPinnedVintage-5` | `memory/backlog/ABL.md:446` · OPEN | check 13's join algebra — the row whose §8 F3 set the choose-upstream precedent the prompt cites |

The adopter's own proposed fix for the first is `bHonedPlumbline` S1 in that tree: gate
`_BLOCK_COMMENT_RE` on a C-family suffix set, take the language from the file being scanned at both
call sites, and add a selftest. This build goes further than that S1 for a measured reason recorded
in the unit's spec — a suffix gate on the block regex alone leaves four of the five over-strip
classes standing, including the two that damage C-family files.

The adopter's gotcha for the second is
`memory/gotchas/guard-blanks-quoted-strings-before-counting-brackets.md` there. Its prescribed
workaround — write U+2019 instead of ASCII `'` — is measured INEFFECTIVE at gov 1.8 against the
class that actually still fires, and the correction belongs in that adopter's tree once this lands.
