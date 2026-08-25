#!/usr/bin/env python3
# gov:kit lexicon@1.1
"""canon.py — the SHIPPED concept clusters a proposed verb table may draw from.

THE RULE, and it is the whole point of this file:

    Which CLUSTERS enter a proposed table is decided by the CORPUS — a cluster with at least one
    live site enters. Which FORM represents a cluster is decided by the CANON — always element 0,
    unconditionally, at every frequency and every dominance.

Two questions, two different deciders, and conflating them is the defect this kit shipped with. The
scaffold used to rank the corpus's own leading tokens and adopt the top rows as an ALLOWLIST, which
legalises whatever a repo already does most: measured on a fresh 19-file repo, it proposed 25 verbs
of which four were not verbs, and every deliberately-bad name in the fixture passed green because
the frequency count had promoted `do`, `is`, `get`, `fetch`, `validate` and `calculate` into the
vocabulary on the strength of those very names. A derived standard points the same direction as the
thing it is meant to grade.

A dominance threshold does NOT fix that — it is the same defect one indirection down. A repo whose
sessions all wrote `get_*` has dominance near 1.0, so `get` is adopted silently and with more
ceremony. The corpus is admitted as evidence for exactly ONE thing: which spellings become debt.

WHY THIS IS SAFE WHERE A DERIVED TABLE IS NOT. Companion §12 bans a gate whose vocabulary is a
hand-kept mirror of the code it grades. This list is PRESCRIPTIVE and frozen in the kit: it says what
code should be called, was written without reading any adopter's corpus, and an adopter cannot edit
it (`role = "engine"` in kit.toml — an upgrade overwrites it). It is the exogenous reference the kit
had nowhere before.

THREE MEASUREMENTS SAY THIS IS NOT ONE AGENT'S TASTE, and they are worth keeping beside the data:

  1. Every one of the eleven negative definitions a human wrote for this repo's table on 2026-08-16
     is exactly a NON-FIRST element of the cluster containing its verb — build NOT create, load NOT
     fetch, read NOT get, write NOT save, parse NOT convert, render NOT format, check NOT validate,
     scan NOT search, init NOT setup, remove NOT delete, set NOT update. The canon reproduces a
     curated table it never saw.
  2. 55.2% of the 14,659 definitions measured on a real adopter (`incms/main`, 2026-08-24) already
     lead with a verb from this repo's table, in a repo that has never carried a declaration — and
     all six of that corpus's commonest off-table leaders land in a cluster (get, list -> read;
     validate, require -> check; create, make -> build).
  3. Of the ten non-verbs the 2026-08-16 curation deleted from the derived seed, SEVEN are in no
     cluster and are unnominatable by ABSENCE, and the other three (`t`, `do`, `is`) are non-first
     elements of `test`, `run` and `check` and are unnominatable by the FIRST-ELEMENT rule. Two
     closing mechanisms with no gap between them, which is the claim that matters and survives.
     The first cut of this line said eight and two, which the data forty lines below refutes: `t`
     is element 3 of the `test` cluster. A docstring arguing that this canon is not one agent's
     taste is the worst place in the file to be counting badly. Found by the round-2 review.

WHAT THIS DOES NOT BOUND. A human may ratify a row outside the canon — this repo's own table carries
`seed` and `arm`, which no cluster holds. The canon bounds what a MACHINE may propose, never what an
owner may declare; a row outside it simply carries a hand-written negative rather than a derived one.
"""

#: Element 0 is the representative and is the only form a proposal may name. Every other form in a
#: tuple is a spelling of the same concept and becomes DEBT when the corpus uses it.
CLUSTERS = (
    ("build", "create a new value and return it", ("create", "make", "construct", "generate", "new")),
    ("load", "read a store into memory", ("fetch", "retrieve", "hydrate", "pull")),
    ("read", "pull bytes or records from a named source", ("get", "list", "access", "obtain", "consume")),
    ("write", "persist to a store", ("save", "store", "persist", "put", "flush")),
    ("parse", "turn text into structure, raising on text that is not that structure",
     ("decode", "deserialize", "unmarshal", "convert")),
    ("render", "turn structure into text", ("format", "serialize", "encode", "stringify", "marshal")),
    ("resolve", "turn a name into the thing it denotes", ("lookup", "locate", "dereference")),
    ("check", "assert a predicate and return a verdict",
     ("validate", "verify", "ensure", "require", "assert", "is", "has")),
    ("scan", "walk a population looking for matches",
     ("search", "walk", "traverse", "iterate", "crawl", "find")),
    ("extract", "pull a declared shape out of a larger one", ("pluck", "strip", "harvest", "mine")),
    ("measure", "count a population and report the number, deciding nothing", ("count", "tally", "size")),
    ("derive", "compute a value from a source so it never has to be authored",
     ("compute", "calculate", "infer", "deduce")),
    ("init", "set up state at construction", ("setup", "configure", "prepare", "install", "bootstrap")),
    ("run", "execute a process to completion and report its outcome",
     ("execute", "invoke", "perform", "dispatch", "call", "do", "process", "handle")),
    ("add", "append to an existing collection", ("append", "insert", "push", "register", "attach")),
    ("remove", "detach without destroying", ("delete", "drop", "destroy", "purge", "detach", "unregister")),
    ("set", "assign a known value", ("update", "assign", "apply", "modify", "mutate", "patch")),
    ("print", "write to stdout for a human", ("echo", "emit", "output", "log", "dump", "report")),
    ("main", "a module's CLI entry point; reserved, one per module", ("entrypoint", "start", "boot", "cli")),
    ("test", "a test function; reserved for harnesses", ("spec", "should", "it", "t", "case")),
)


def build_form_index() -> dict:
    """`{surface form: representative}` over every cluster, including each representative itself.

    A form appearing in two clusters would make the answer depend on iteration order, so the
    selftest asserts the forms are disjoint rather than leaving it to review.
    """
    out = {}
    for rep, _gloss, others in CLUSTERS:
        out[rep] = rep
        for form in others:
            out[form] = rep
    return out


def read_gloss(rep: str) -> str:
    """The declared gloss for a representative, or `""` when it names no cluster."""
    for r, gloss, _others in CLUSTERS:
        if r == rep:
            return gloss
    return ""


def render_negative(rep: str) -> str:
    r"""The NOT clause for a representative, from its own cluster's first alternative.

    A SEED THAT CARRIES NO NEGATIVE IS BORN FAILING THE GATE. The assert in `lexicon.py` refuses a
    row with only a positive gloss, so a scaffold emitting bare glosses would hand every adopter a
    declaration its own checker rejects on the first run — measured on a fresh repo before this
    existed: fourteen rows, fourteen findings. The cluster already knows the boundary word, so the
    seed states it and the curator sharpens it rather than inventing it.
    """
    for r, _gloss, others in CLUSTERS:
        if r == rep:
            return " — NOT `%s`" % others[0] if others else ""
    return ""
