# TOOL-dWitnessedBar-1 leg-tail 5 — shell hygiene (a quoting hazard) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** shell hygiene (a quoting hazard)
- **Hash:** 5ea619ee557a5e2d2881e78a0979a77a6829edcd
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg shell hygiene (a quoting hazard) | exit 1
sh-hygiene: quoting — 151 tracked shell source(s) scanned, 151 site(s) in 54 key(s)
sh-hygiene: 8 quoting finding(s).
  tools/lib/gov-feed.sh: 1 `tab-ifs-read` site(s) and no registry row declares them — split the line with `${line%%$'\t'*}` and `${line#*$'\t'}`: a tab is IFS whitespace, so `read` collapses an empty field and shifts every field after it
    tools/lib/gov-feed.sh@8d79823f:283  while IFS=$'\t' read -r r k t c; do
  tools/lib/gov-ref.sh: 1 `tab-ifs-read` site(s) and no registry row declares them — split the line with `${line%%$'\t'*}` and `${line#*$'\t'}`: a tab is IFS whitespace, so `read` collapses an empty field and shifts every field after it
    tools/lib/gov-ref.sh@166f6911:72  { IFS=$'\t' read -r tok _ <"$rf"; } 2>/dev/null || :
  tools/push-main.sh: the registry declares 3 site(s) at `tab-ifs-read` and the scan measures 4 — the count may fall with the sites and may not rise
    tools/push-main.sh@3a5bf825:290  [ -f "$refusal" ] && IFS=$'\t' read -r tok msg < "$refusal"
    tools/push-main.sh@3a5bf825:384  [ -f "$allowfile" ] && IFS=$'\t' read -r sha run < "$allowfile"
    tools/push-main.sh@3a5bf825:434  [ -f "$barfile" ] && IFS=$'\t' read -r bar barpath barblob < "$barfile"
    tools/push-main.sh@3a5bf825:905  while IFS=$'\t' read -r r k t c; do
  tools/push-main.test.sh: the registry declares 3 site(s) at `heredoc-source` and the scan measures 4 — the count may fall with the sites and may not rise
    tools/push-main.test.sh@496727ed:234  cat > "$tmp/stub.sh" <<STUB
    tools/push-main.test.sh@496727ed:464  cat > "$tmp/noise.sh" <<'NOISE'
    tools/push-main.test.sh@496727ed:1282  cat > "${KIT_REL}$_rg_k/regen.py" <<'PY'
    tools/push-main.test.sh@496727ed:1583  cat > "${KIT_REL}$_rg_k/regen.py" <<'PY'
  tools/run-gates/post-merge.sh: the registry declares 1 site(s) at `tab-ifs-read` and the scan measures 2 — the count may fall with the sites and may not rise
    tools/run-gates/post-merge.sh@eb32abcc:338  { IFS=$'\t' read -r tok _ <"$rf"; } 2>/dev/null || :
    tools/run-gates/post-merge.sh@eb32abcc:626  while IFS=$'\t' read -r r k t c; do
  tools/run-gates/run-gates.sh: the registry declares 13 site(s) at `tab-ifs-read` and the scan measures 12 — the count may fall with the sites and may not rise
    tools/run-gates/run-gates.sh@db46050c:972  while IFS=$'\t' read -r pname pcores pram pknobs || [ -n "$pname" ]; do
    tools/run-gates/run-gates.sh@db46050c:2639  { IFS=$'\t' read -r nm st _ < "$f"; } 2>/dev/null || [ -n "$nm" ] || continue
    tools/run-gates/run-gates.sh@db46050c:2643  [ -f "$RUNDIR/$i.retry.leg" ] && { IFS=$'\t' read -r _ st _ < "$RUNDIR/$i.retry.leg"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:3953  { IFS=$'\t' read -r _st _es _er _eh _ee _age _ < "$REUSE_CACHE/${_key:0:2}/$_key"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:4042  while IFS=$'\t' read -r _hk _hv; do
    tools/run-gates/run-gates.sh@db46050c:4657  { IFS=$'\t' read -r _ _c _ < "$_f"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:4698  while IFS=$'\t' read -r ts c _; do
    tools/run-gates/run-gates.sh@db46050c:4790  [ -n "$RUNDIR" ] && [ -f "$RUNDIR/$i.leg" ] && { IFS=$'\t' read -r _ _ _ _ _ e _ < "$RUNDIR/$i.leg"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:4799  { IFS=$'\t' read -r _ _ _ _ js je _ < "$RUNDIR/$j.leg"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:5592  _st=""; { IFS=$'\t' read -r _st _ < "$REUSE_CACHE/${_key:0:2}/$_key"; } 2>/dev/null
    tools/run-gates/run-gates.sh@db46050c:5750  IFS=$'\t' read -r _ lst _ _ _ lend lkey _ < "$RUNDIR/$i.leg" 2>/dev/null || { lst=ok; lkey=-; }
    tools/run-gates/run-gates.sh@db46050c:5762  && IFS=$'\t' read -r _ lrst _ _ _ lend _ < "$RUNDIR/$i.retry.leg" 2>/dev/null
  tools/unattended/lib-unattended.sh: the registry declares 2 site(s) at `tab-ifs-read` and the scan measures 1 — the count may fall with the sites and may not rise
    tools/unattended/lib-unattended.sh@9d2e1e71:511  while IFS=$'\t' read -r _gp_k _gp_v || [ -n "$_gp_k" ]; do
  tools/unattended/unattended.sh: the registry declares 15 site(s) at `tab-ifs-read` and the scan measures 19 — the count may fall with the sites and may not rise
    tools/unattended/unattended.sh@670e49e1:954  while IFS=$'\t' read -r _tk_s _tk_i; do
    tools/unattended/unattended.sh@670e49e1:2741  refs=$(printf '%s\n' "$CLAIM_ROWS" | while IFS=$'\t' read -r nm _ _ _ _ sha _ _ _ _ _ _ kd _; do
    tools/unattended/unattended.sh@670e49e1:2843  IFS=$'\t' read -r c_slug c_node c_status c_age c_verdict c_sha c_sess c_ka c_host c_lease c_beat c_epoch c_kind c_renews c_wit c_offer c_odl c_lf c_bsha c_rest <<<"$row"
    tools/unattended/unattended.sh@670e49e1:3053  { IFS=$'\t' read -r tok _ <"$rf"; } 2>/dev/null || :
    tools/unattended/unattended.sh@670e49e1:3341  while IFS=$'\t' read -r r k t c; do
    tools/unattended/unattended.sh@670e49e1:4065  IFS=$'\t' read -r ref tip c utc <<<"$l"
    tools/unattended/unattended.sh@670e49e1:4347  IFS=$'\t' read -r c_slug c_node c_status c_age c_verdict c_sha c_sess c_ka c_host c_lease c_beat c_epoch c_rest <<<"$row"
    tools/unattended/unattended.sh@670e49e1:6030  while IFS=$'\t' read -r ref sha ct <&3; do
    tools/unattended/unattended.sh@670e49e1:6077  while IFS=$'\t' read -r _co_q _co_g; do
    tools/unattended/unattended.sh@670e49e1:7437  while IFS=$'\t' read -r p i st; do
    tools/unattended/unattended.sh@670e49e1:8502  while IFS=$'\t' read -r _cp _ _cid; do
    tools/unattended/unattended.sh@670e49e1:8967  while IFS=$'\t' read -r _ar_id _ar_sum; do
    tools/unattended/unattended.sh@670e49e1:11465  while IFS=$'\t' read -r u iso g decl; do
    tools/unattended/unattended.sh@670e49e1:11522  while IFS=$'\t' read -r name iso beat; do
    tools/unattended/unattended.sh@670e49e1:12733  while IFS=$'\t' read -r leg ver _ _ _ age _ _ blk _; do
    tools/unattended/unattended.sh@670e49e1:13128  while IFS=$'\t' read -r leg ver _ _ _ age own8 ownid blk _; do
    tools/unattended/unattended.sh@670e49e1:13363  IFS=$'\t' read -r _ suite sha run concl <<< "$line"
    tools/unattended/unattended.sh@670e49e1:13466  while IFS=$'\t' read -r leg ver _; do
    tools/unattended/unattended.sh@670e49e1:18314  while IFS=$'\t' read -r _c_kind _c_what; do
```
