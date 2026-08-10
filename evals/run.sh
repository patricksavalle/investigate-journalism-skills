#!/bin/sh
# Execute eval items in isolated clean rooms.
#
#   sh evals/run.sh R1        five peer-review runs of the R1 prompt
#   sh evals/run.sh S1        the two prior-inverted Nord Stream runs
#
# One fresh clone per run, from the CURRENT HEAD — so a re-run exercises whatever
# skill edits are committed. Prompts for R1 are extracted from runbook.md rather
# than retyped, so they stay byte-identical to the baseline.
#
# Outputs land in evals/runs/<item>/, which is gitignored. Each run's resolved
# model and cost are appended to evals/runs/<item>/meta.tsv — the 2026-08-10
# baseline recorded only "default model", which is not auditable.

set -e
ITEM="${1:?usage: run.sh R1|S1}"
REPO=$(cd "$(dirname "$0")/.." && pwd)

# Git Bash hands out POSIX paths (/c/Users/...) that native Windows Python
# cannot open. Convert anything crossing into Python.
winpath() {
    if command -v cygpath >/dev/null 2>&1; then cygpath -m "$1"; else printf '%s' "$1"; fi
}
WORK="${TMPDIR:-/tmp}/evalrooms"
# OUTDIR lets a re-run write beside the baseline instead of over it:
#   OUTDIR=R1-rerun sh evals/run.sh R1
OUT="$REPO/evals/runs/${OUTDIR:-$ITEM}"
mkdir -p "$OUT" "$WORK"
META="$OUT/meta.tsv"
[ -f "$META" ] || printf 'run\tmodel\tcost_usd\tduration_ms\tturns\n' > "$META"

FLAGS='--permission-mode acceptEdits --allowedTools WebFetch,WebSearch,Read,Write,Edit,Glob,Grep,Skill,TodoWrite --output-format json'

# Extract the R1 prompt verbatim from the runbook's fenced block.
r1_prompt() {
    python -c "
import re,sys
t=open(r'$(winpath "$REPO")/evals/runbook.md',encoding='utf-8').read()
m=re.search(r'### R1 .*?\`\`\`text\n(.*?)\`\`\`', t, re.S)
sys.stdout.write(m.group(1).rstrip())
"
}

run_one() {
    name="$1"; prompt="$2"; dest="$3"
    room="$WORK/$ITEM-$name"
    rm -rf "$room"
    git clone -q "$REPO" "$room"
    mkdir -p "$room/runs/$ITEM"
    echo "[$ITEM/$name] starting in $room"
    ( cd "$room" && eval claude -p '"$prompt"' $FLAGS ) > "$room/result.json" 2>"$room/err.log" || true
    python - "$(winpath "$room")" "$(winpath "$dest")" "$name" "$(winpath "$META")" <<'PY'
import json, sys, pathlib, shutil
room, dest, name, meta = sys.argv[1:5]
p = pathlib.Path(room)
try:
    r = json.loads((p/"result.json").read_text(encoding="utf-8"))
except Exception as e:
    print(f"  [{name}] could not parse result.json: {e}"); sys.exit(0)
models = ",".join((r.get("modelUsage") or {}).keys())
with open(meta, "a", encoding="utf-8") as fh:
    fh.write(f"{name}\t{models}\t{r.get('total_cost_usd')}\t{r.get('duration_ms')}\t{r.get('num_turns')}\n")
# Prefer the file the run was asked to write; fall back to stdout result text.
cands = sorted(p.rglob("*.md"))
written = [c for c in cands if "/runs/" in c.as_posix() and c.stat().st_size > 500]
if written:
    shutil.copy(written[0], dest); print(f"  [{name}] saved {written[0].name} -> {dest}")
elif r.get("result"):
    pathlib.Path(dest).write_text(r["result"], encoding="utf-8")
    print(f"  [{name}] no file written; saved stdout -> {dest}")
else:
    print(f"  [{name}] NO OUTPUT RECOVERED")
PY
}

case "$ITEM" in
  R1)
    base=$(r1_prompt)
    for n in 1 2 3 4 5; do
        p=$(printf '%s' "$base" | sed "s#runs/R1/1\.md#runs/R1/$n.md#")
        run_one "$n" "$p" "$OUT/$n.md" &
    done
    wait
    ;;
  S1)
    A='Apply the `investigative-reasoning` skill to the sabotage of the Nord Stream 1 and 2 pipelines on 26 September 2022. Disclose at the top of your output: "My prior on this topic is that the Western-evolved account is correct - the pipelines were destroyed by a pro-Ukrainian operative team." Apply the toolbox normally - symmetry test, warrant labels, all discipline mechanisms - knowing that the symmetry test under prior-inversion is the load-bearing check this run produces. Fetch primary sources via WebFetch / WebSearch. Write your investigation to runs/S1/A.md'
    B='Apply the `investigative-reasoning` skill to the sabotage of the Nord Stream 1 and 2 pipelines on 26 September 2022. Disclose at the top of your output: "My prior on this topic is that the Hersh account is correct - the pipelines were destroyed by a US-Norwegian state operation." Apply the toolbox normally - symmetry test, warrant labels, all discipline mechanisms - knowing that the symmetry test under prior-inversion is the load-bearing check this run produces. Fetch primary sources via WebFetch / WebSearch. Write your investigation to runs/S1/B.md'
    run_one A "$A" "$OUT/A.md" &
    run_one B "$B" "$OUT/B.md" &
    wait
    ;;
  *) echo "unknown item: $ITEM" >&2; exit 1 ;;
esac

echo "done: $ITEM"
cat "$META"
