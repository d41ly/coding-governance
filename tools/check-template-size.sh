#!/usr/bin/env bash
# check-template-size.sh — STRICT size gate for the governance playbook template.
# The template is the operational ruleset an agent reads every session; it must stay lean.
# Prose that doesn't affect instruction clarity belongs in a companion
# (parallel-coding-governance.customize.md / .domain-rules.md), never inflating the template.
#
#   tools/check-template-size.sh            # gate the tracked template
#   MAX_BYTES=32768 tools/check-template-size.sh <file>   # override target / limit
#
# Exit 0 = within budget (prints one line). Exit 1 = over budget. Exit 2 = file missing.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || ROOT=.
FILE=${1:-"$ROOT/parallel-coding-governance.template.md"}
MAX_BYTES=${MAX_BYTES:-32768}     # 32 KiB — the STRICT ceiling; never raise to fit new prose, externalize instead

[ -f "$FILE" ] || { echo "TEMPLATE-SIZE env ERROR — file not found: $FILE"; exit 2; }
# Measure LF-NORMALIZED bytes (strip CR) so the gate is checkout-independent — a Windows autocrlf
# smudge to CRLF must not inflate the count and spuriously fail the limit.
bytes=$(tr -d '\r' < "$FILE" | wc -c | tr -d '[:space:]')
name=$(basename "$FILE")

if [ "$bytes" -gt "$MAX_BYTES" ]; then
  over=$((bytes - MAX_BYTES))
  echo "TEMPLATE-SIZE FAILED — $name is $bytes bytes, $over over the $MAX_BYTES-byte limit."
  echo "  Do NOT raise the limit. Trim non-instructional prose, or move an activity-scoped section"
  echo "  to parallel-coding-governance.domain-rules.md (leaving a §-stub pointer), per the v2.3 pattern."
  exit 1
fi
printf 'template-size OK — %s: %d / %d bytes (%d under, %.1f%%)\n' "$name" "$bytes" "$MAX_BYTES" "$((MAX_BYTES - bytes))" "$(awk "BEGIN{print $bytes/$MAX_BYTES*100}")"
