#!/usr/bin/env bash
# The envelope's shell writer, canonical copy (PLAY-dOrderedCharter-8 S8).
#
# The shell twin of `render_envelope` in `envelope.py` beside this file, for the writers that are bash
# in a copy-installed kit: the card engine renders the orientation card file inside its level-1
# envelope with it. Same format, byte for byte: the opener `[<path> · Level <n> · <direction>]`, the
# body with a final newline added where it lacks one, and the closer `[/<path>]`.
#
# USAGE: `<prefix>/lib/` ships nothing, so a writer cannot source this file. Each one carries the block
# between the markers below INLINE, byte-identical, and the parity table in `resolve-python.test.sh`
# beside this file reds a copy that drifts; its cross-language arm holds this file and `envelope.py`
# to one byte form. Run as a script it renders one envelope:
#   bash envelope.sh <path> <level> <direction> [<body-file>]

# >>> envelope_sh — canonical copy: envelope.sh in the gov lib dir (byte-identical; gated)
# `render_envelope_sh <path> <level> <direction> [<body-file>]` prints the opener, the body file's
# bytes with a final newline added where it lacks one, and the closer: `render_envelope` of the Python
# twin byte for byte. No body file, or an empty one, renders the two lines alone. A level that is no
# unsigned integer returns 2 printing nothing; a body file that does not read returns 1.
render_envelope_sh() {
  case "${2:-}" in ''|*[!0-9]*) return 2 ;; esac
  printf '[%s · Level %s · %s]\n' "$1" "$((10#$2))" "$3"
  if [ -n "${4:-}" ] && [ -s "$4" ]; then
    cat -- "$4" || return 1
    [ -z "$(tail -c 1 -- "$4")" ] || printf '\n'
  fi
  printf '[/%s]\n' "$1"
}
# <<< envelope_sh

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  render_envelope_sh "$@"
fi
