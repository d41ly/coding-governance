# The whole-design walk's key

**Serves:** research PLAY-dClosedLoop-1

The sealed walk's key: the twelve plants the seeding script made in the sealed copy, committed when the seal was
lifted (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md` `[recall-scored]`). It was committed as
`build/2026-10-20-build-PLAY-dClosedLoop-1-walk-key.json` and moved into this record at the build's landing,
2026-10-20, because a JSON file cannot carry the Serves line hygiene check 21 reads. The tilde-fenced block below
holds the committed blob's bytes unchanged: its lines, each ending in a newline, are the key, and their SHA-256
is the pinned `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Check it with
`git cat-file -p HEAD:<this record> | python -c "import sys,hashlib;l=sys.stdin.buffer.read().split(b'\n');i=l.index(b'~~~json');j=l.index(b'~~~',i+1);print(hashlib.sha256(b'\n'.join(l[i+1:j])+b'\n').hexdigest())"`.

~~~json
{
 "base": "747a2af2292f1f9253ff1f019db9c241b25444dc",
 "plants": [
  {
   "id": "P01",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0018",
    "cl-dClosedLoop-0019",
    "cl-dClosedLoop-0021"
   ],
   "words": [
    "fail",
    "killed",
    "interrupt",
    "stop"
   ],
   "mechanical": false,
   "source": "the shape audit's walk-failure-route"
  },
  {
   "id": "P02",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0229",
    "cl-dClosedLoop-0231"
   ],
   "words": [
    "alias",
    "journal",
    "rename"
   ],
   "mechanical": false,
   "source": "the shape audit's journal-rename"
  },
  {
   "id": "P03",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0284",
    "cl-dClosedLoop-0303",
    "cl-dClosedLoop-0310"
   ],
   "words": [
    "restart",
    "second act",
    "two act",
    "duplicate",
    "re-adopt",
    "reconcil"
   ],
   "mechanical": false,
   "source": "the shape audit's supervisor-restart"
  },
  {
   "id": "P04",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0305",
    "cl-dClosedLoop-0377"
   ],
   "words": [
    "origin",
    "ratif"
   ],
   "mechanical": false,
   "source": "the shape audit's intake-ratification"
  },
  {
   "id": "P05",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0488",
    "cl-dClosedLoop-0478"
   ],
   "words": [
    "declin",
    "refus",
    "reject"
   ],
   "mechanical": false,
   "source": "the shape audit's declined-retirement"
  },
  {
   "id": "P06",
   "record": "flow-steps",
   "tag": "entry",
   "anchors": [
    "entry.claim"
   ],
   "words": [
    "unreachable",
    "offline",
    "remote"
   ],
   "mechanical": false,
   "source": "the design audit's M13"
  },
  {
   "id": "P07",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0283",
    "cl-dClosedLoop-0378"
   ],
   "words": [
    "drain",
    "fallback",
    "in flight",
    "migrat"
   ],
   "mechanical": false,
   "source": "the design audit's M15"
  },
  {
   "id": "P08",
   "record": "flow-steps",
   "tag": "entry",
   "anchors": [
    "entry.intake"
   ],
   "words": [
    "agent",
    "typed",
    "verbatim",
    "scout",
    "hook",
    "witness"
   ],
   "mechanical": false,
   "source": "the session model's H2"
  },
  {
   "id": "P09",
   "record": "flow-steps",
   "tag": "plan",
   "anchors": [
    "plan.exit"
   ],
   "words": [
    "ratif",
    "typed",
    "planner",
    "agent"
   ],
   "mechanical": false,
   "source": "the session model's H1"
  },
  {
   "id": "P10",
   "record": "architecture-v2",
   "tag": "chain",
   "anchors": [
    "cl-dClosedLoop-0289",
    "cl-dClosedLoop-0318",
    "build.worktree"
   ],
   "words": [
    "index",
    "lock",
    "concurren",
    "serial",
    "commit queue",
    "parallel"
   ],
   "mechanical": false,
   "source": "the session model's H6"
  },
  {
   "id": "P11",
   "record": "layer-memory",
   "tag": [
    "contract",
    "design"
   ],
   "anchors": [
    "dupes"
   ],
   "words": [
    "writer"
   ],
   "mechanical": true,
   "source": "mechanical: a kind's writer dropped"
  },
  {
   "id": "P12",
   "record": "architecture-v2",
   "tag": [
    "chain",
    "enforcement",
    "principles"
   ],
   "anchors": [
    "cl-dClosedLoop-0093",
    "P23"
   ],
   "words": [
    "P23",
    "claim",
    "trusted",
    "enforc"
   ],
   "mechanical": true,
   "source": "mechanical: a principle's only enforcing clause dropped"
  }
 ]
}
~~~
