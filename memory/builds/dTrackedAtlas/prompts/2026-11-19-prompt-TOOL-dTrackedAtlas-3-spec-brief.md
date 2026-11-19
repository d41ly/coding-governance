**Serves:** research TOOL-dTrackedAtlas-3

# Spec brief — TOOL-dTrackedAtlas-3: the page knows what it was generated from, and `--check` reds a stale one

You author ONE spec and write no product code. Read first, whole: the build README
`memory/builds/dTrackedAtlas/README.md`, the prompt record
`memory/builds/dTrackedAtlas/prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md`, the committed spec of
TOOL-dTrackedAtlas-1 under `memory/builds/dTrackedAtlas/spec/`, `memory/TEMPLATE-SPEC.md`, and
`memory/guides/BUILD-METHOD.md` at `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`,
`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse` and
`doc.build-method#m12-research-test-choose-when-the-solution-is-not-given`.

## The mechanism

The generator `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py` embeds in the page
the commit it was generated from and a digest of every input it read (dClosedLoop's records, unit 1's derivation
inputs, the template), and the page shows them. `--check` given a page path reads that stamp and reds (exit 1,
naming what moved) when the tree at the ref it checks has moved past it; `--check` with no page keeps today's
meaning. Decide in §8 whether the digest or the commit decides staleness (a commit that touches no input moves the
sha and not the digest), and record the candidates and the observation that chose (M12).

## Facts and constraints

- Today `--check` derives and writes nothing; `--out` writes the page; data is spliced after the
  `<script id="atlas-data" type="application/json">` marker. Unit 2 (specced beside you) changes the derived data
  and the template's rendering of chain state; do not spec that. Keep your change to the stamp, its rendering line
  and the page check, and name in §3 the functions you touch.
- The page home is `C:/projects/coding-governance-atlas/closed-loop-atlas.html`, outside every git tree; the page
  is never committed. Unit 4 (specced beside you) regenerates on a landing and may call your check to decide
  whether to regenerate: give it a CLI it can call and an exit code it can read, stated exactly in §3.
- No new file under `memory/builds/dClosedLoop/build/`; nothing under `tools/`.
- Acceptance: a page generated at a ref passes `--check` against that ref; a planted landing on a fixture ref (a
  scratch clone) reds the old page's `--check`, naming the commits; a page with no stamp reds as unstamped and
  never passes; each red observed before green. No gate, suite or bar in a criterion.
