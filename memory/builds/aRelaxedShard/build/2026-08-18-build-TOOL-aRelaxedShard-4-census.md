# The backlog census — the derivation behind TOOL-aRelaxedShard-4 §4

**Serves:** research TOOL-aRelaxedShard-4

This is S1: the measurement of record, as commands rather than prose, because its figures have already
moved three times. Re-run these instead of re-inventing a method. Every number in the spec's §4 comes
from here, and the spread between methods is the point rather than an embarrassment.

## The census — the figure of record

```bash
# distinct ids ever minted, across the live shard and every archived rotation
cat memory/backlog/TOOL.md memory/archive/TOOL.*.md \
  | grep -oE '^- TOOL-[A-Za-z]+-[0-9]+[a-z]?' | sort -u | wc -l      # -> 170
# live (non-terminal) rows in the live shard
grep -E '^- TOOL-' memory/backlog/TOOL.md | grep -cvE '(CLOSED|WONTDO)'   # -> 81
# therefore terminal
# 170 - 81 = 89   (88 CLOSED + 1 WONTDO, verified separately)
```

Over the nine active days the corpus covers: **18.9 minted/day, 9.9 closed/day, net +9.0 live rows/day.**
At the row length below that is about 2,228 B/day.

## Row length, measured on TODAY's rows and not inherited

```bash
grep -E '^- TOOL-' memory/backlog/TOOL.md > /tmp/rows.txt
awk -v b="$(wc -c < /tmp/rows.txt)" -v n="$(wc -l < /tmp/rows.txt)" \
    'BEGIN{printf "%.1f B/row\n", b/n}'                              # -> 247.6
```

rev-2 of the spec carried 253.7 B/row over from `TOOL-aRelaxedShard-1`, which measured 73 rows. This is
the same figure re-measured on 82. **Use `wc -c`, never `awk length()`** — the `·` separators are two
bytes each in UTF-8, and counting characters is how unit 1's first measurement came out 205 B low.

## Why the runway is a RANGE and not a number

Four methods over one corpus:

| method | net rows/day | runway to 61,440 |
|---|---|---|
| census, above | +9.0 | ~18 days |
| per-commit diff scan | +6.7 | ~24 days |
| live rows accumulated over the window | +8.8 | ~18 days |
| trailing three days only | ~+16 | ~11 days |

```bash
# the daily series, which is what makes a single mean misleading
git log --reverse --format='%H %ad' --date=short -- memory/backlog/TOOL.md \
  | while read c d; do
      n=$(git show --format='' -U0 "$c" -- memory/backlog/TOOL.md 2>/dev/null \
            | grep -cE '^\+- TOOL-')
      [ "$n" -gt 0 ] && echo "$d $n"
    done | awk '{a[$1]+=$2} END{for(k in a) print k, a[k]}' | sort
```

Daily net runs from +1 to +25 and arrives in merge STEPS, not as a slope: one day of this window
consumed 15.8% of the remaining headroom by itself. **Distrust the per-commit diff scan** — it
double-counts rows a merge re-adds and misses rows closed by an in-place edit, which is how most rows
close.

## The area attribution, and the trap in it

```bash
# WRONG — this is what rev-1 and rev-2 did. It measures whether an author
# happened to SPELL a kit's directory name, not which area a row concerns.
for k in memory-tree codebase-map unattended drift-audit govkit lexicon; do
  printf '%-14s %s\n' "$k" "$(grep -cE "^- TOOL-.*($k)" memory/backlog/TOOL.md)"
done
# -> 53 of 82 rows "name no kit", largest cluster 11%

# RIGHT — attribute by TOPIC keywords. Buckets overlap, so this is a tally
# and not a partition; the two robust figures are the unmatched count and the
# largest cluster.
grep -icE 'hygiene|check [0-9]|backlog|rotat|spec|index|corpus_ids|gotcha|cap' \
  memory/backlog/TOOL.md
# -> memory-tree 44 (54%); only 13 rows (16%) match nothing at all
```

The corrected figures do **not** rescue sharding as a budget remedy — that is rejected on the slope, and
splitting ten ways leaves the same +9.0/day arriving. What they do is remove the false claim that no
natural partition exists. One does, and it is dominated by `memory-tree`.

## What this supersedes

`.memory-tree.conf`'s `ROW_DOC_CAP_BYTES` comment states "8.1 live rows/day (~2,057 B): about 21 days",
measured during unit 1. That figure came from the weaker method and a 73-row width. The comment is
corrected in the same change that adds this record; the cap value it justifies, 61,440, is unaffected —
it is 250 rows at measured width either way.
