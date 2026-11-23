# TOOL-dQuietDisk-1 leg-tail 2 — kickoff-manifest ratchet failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** kickoff-manifest ratchet
- **Hash:** 22f692fb107c1151efcc2d8e0597568f6b842845
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
# run-gates | leg kickoff-manifest ratchet | exit 1
MANIFEST check 5 FAILED — watched files changed since last-audit with no re-stamp at/after the change:
  memory/guides/BUILD-METHOD.md
  tools/memory-tree/check-memory-hygiene.sh
  tools/run-gates/run-gates.sh
  For each file, re-check the §B claims derived from it, update the manifest where stale, then
  re-stamp last-audit (sha = HEAD on any branch) — bundled with the watched change or as a follow-up in the
  same PR. After a merge that brought in watch-touching commits, the fresh post-merge audit +
  re-stamp is the close.
MANIFEST check 9 FAILED — the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha: 12 non-merge commits since 2c621083fd91278f33ba1baba1ea15f4dada31b0
```
