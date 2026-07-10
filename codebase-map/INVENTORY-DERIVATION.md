# Deriving a project's inventories — the checklist

The map's coverage is exactly as good as the inventory set in `map_extractors.py`. This
checklist is distilled from a full ground-truth mapping pass + two adversarial reviews of the
reference implementation (inCMS, ARCH-dWovenAtlas-1); every rule below was a shipped bug or a
confirmed review finding once. Work through it ONCE at adoption; revisit when the stack grows
a new registry.

## 1. Enumerate the candidate surfaces

Walk your stack and list everything that is a NAMED, ADDABLE moving part. Typical surfaces:

| Surface | Typical ground truth | Extractor style |
|---|---|---|
| Feature flags / config gates | a flags registry module; gate-shaped config fields | import the registry |
| HTTP surface | router/handler FILES (not live routes — env-sensitive) | file glob / module list |
| Frontend routes/screens | route/page files by convention (Next/SvelteKit/…) | `walk_file_keys` / `walk_dir_keys` |
| CLI commands | the CLI framework's command table | import the registry |
| DB migrations | the migration tool's chain walker (IDs, never filenames) | import the walker |
| Background jobs / queues | the scheduler/queue registration table | import the registry |
| Plugin/extension points | manifest schema enums, contribution tables | import or read schema |
| Generated artifacts | committed JSON manifests | `json_artifact_inventory` |
| Docs pages | one file per feature convention | `glob_inventory` |
| Service/domain modules | package directories | `module_inventory` |

Aim for the surfaces where "somebody added one and nobody recorded it" actually hurts. 8-12
inventories is a healthy set; 2 is better than 0.

## 2. Pick the mechanics — in this preference order

1. **Import the code's own registry** (a flags list, command table, migration walker): can't
   drift from runtime truth.
2. **Read a committed generated artifact** — but FAIL-CLOSED (`json_artifact_inventory`), even
   if the runtime loader of the same artifact is deliberately fail-open.
3. **File glob** — last resort, and note it enumerates files, not wiring: pair it with a
   census assert where registration is an import side effect (see rule 5).

## 3. The rules that were bugs

- **Fail closed, always.** An extractor that returns FEWER keys on an unexpected state is a
  silent coverage hole forever (the green-by-absence class). The helpers raise `MapError`;
  keep custom extractors doing the same. The freshness gate byte-compares two runs of the SAME
  function — it structurally cannot see a fail-open extractor.
- **Extension sets, not literal filenames.** `route.ts` alone silently drops `route.tsx`.
  Pass the full set the framework accepts.
- **Flat walks guard against nesting.** If you enumerate `dir/*.py`, assert no subdirectory
  exists (`no_subdirs`) — a future `dir/sub/` must break the gate, not escape it.
- **IDs over filenames** for anything with a chain/merge semantics (migrations): filename
  prefixes collide and reorder; the tool's revision ids don't.
- **POSIX keys, LF compares, `fnmatchcase`.** Windows dev nodes + Linux CI must produce
  byte-identical artifacts and identical glob attribution. The helpers handle this — don't
  bypass them with raw `pathlib.glob` (brackets in dirnames like `[id]` are char classes!).
- **Registration-by-import needs a census.** If tools/handlers register as an import side
  effect of a hand-maintained import list, a new module missing from that list registers
  NOTHING and is invisible to a registry read. Add a per-module assert (every module
  contributes >= 1 registration) alongside the registry inventory.
- **Don't hardcode today's enum of anything documented as forward-only** (node letters, id
  prefixes, plugin kinds): the gate must accept tomorrow's valid member without a code patch.
- **Name-shaped censuses miss non-shaped members.** A `*_enabled`-pattern config census
  misses `debug`-style gates; note the escape hatch in the extractor docstring so the next
  reader widens ONE place.

## 4. Wire the two claim planes

- The RATCHET gates on the keys your extractors emit — never on path globs.
- Globs (per dossier `paths.globs`) feed only the digest. Shared mega-modules that many
  features touch are documented in dossiers' `## Shared seams` prose, never glob-claimed —
  exclusive glob ownership of a shared file is impossible, and the keyed plane already carries
  that ownership through the keys each feature registers.
- Add `KEYED_ATTRIBUTORS` for path families whose filename embeds a claim key (migrations:
  `db/migrations/<rev>_*.sql` -> the `migrations` inventory) — keyed attribution beats globs.

## 5. Accepted residuals (know them; don't rediscover them)

- Baseline additions are socially enforced — stateless CI can't tell backfill from evasion;
  the baseline lives where diffs are conspicuous.
- Dossier PROSE can rot; keyed claims cannot. Refresh prose when touching the feature.
- DB/content-defined surfaces (provisioned pages, user data) are not file-enumerable: record
  them as prose notes or an explicit non-goal.
- The gate fails in CI, not pre-commit, for claim errors — say so in your contributing doc.
