#!/usr/bin/env python3
"""Check plan/ consistency and (re)generate INDEX tables.

Usage:
  python3 plan/check.py          check only, exit 1 on problems (used in CI)
  python3 plan/check.py --write  regenerate tables in INDEX.md, then check

Tables in INDEX.md between <!-- gen:NAME --> and <!-- /gen:NAME --> are generated
from the YAML headers. Do not edit them by hand. No external dependencies.
"""
import re
import sys
from pathlib import Path

PLAN = Path(__file__).resolve().parent
INDEX = PLAN / "INDEX.md"

FEATURE_STATUS = {"todo", "in-progress", "blocked", "done", "dropped"}
DECISION_STATUS = {"open", "proposed", "decided", "superseded"}
RISK_STATUS = {"open", "mitigated", "accepted", "closed"}
PHASE_LABEL = {"0": "0 setup"}

FEATURE_KEYS = ["id", "title", "status", "phase", "depends_on", "decisions", "questions", "created", "updated"]
DECISION_KEYS = ["id", "title", "status", "date", "features", "supersedes", "superseded_by"]


def parse_header(path):
    """Minimal YAML front matter parser: `key: value`, `key: [a, b]`, comments."""
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        line = re.sub(r"\s+#.*$", "", line).strip()
        if not line or line.startswith("#"):
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        elif val in ("", "null", "~"):
            val = None
        else:
            val = val.strip("\"'")
        data[key.strip()] = val
    return data


def load(folder, keys, prefix):
    items, errors = {}, []
    for path in sorted((PLAN / folder).glob("*.md")):
        h = parse_header(path)
        rel = path.relative_to(PLAN)
        if h is None:
            errors.append(f"{rel}: missing YAML header")
            continue
        missing = [k for k in keys if k not in h]
        if missing:
            errors.append(f"{rel}: missing keys {missing}")
        if not path.name.startswith(f"{h.get('id')}-") or not str(h.get("id", "")).startswith(prefix):
            errors.append(f"{rel}: id '{h.get('id')}' does not match file name")
        h["_path"] = rel.as_posix()
        items[h.get("id")] = h
    return items, errors


def table_ids(path, prefix):
    """IDs from the first column of markdown tables, e.g. | Q1 | ..."""
    if not path.exists():
        return {}
    rows = {}
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(prefix + r"\d+", cells[0]):
            rows[cells[0]] = cells
    return rows


def as_list(v):
    return v if isinstance(v, list) else []


def gen_features(features):
    out = ["| ID | Feature | Phase | Status | Depends on |", "|---|---|---|---|---|"]
    for fid, f in features.items():
        deps = ", ".join(as_list(f.get("depends_on"))) or "–"
        phase = PHASE_LABEL.get(str(f.get("phase")), str(f.get("phase")))
        out.append(f"| [{fid}]({f['_path']}) | {f.get('title')} | {phase} | {f.get('status')} | {deps} |")
    return out


def gen_decisions(decisions):
    out = ["| ID | Decision | Status | Date |", "|---|---|---|---|"]
    for did, d in decisions.items():
        out.append(f"| [{did}]({d['_path']}) | {d.get('title')} | {d.get('status')} | {d.get('date') or '–'} |")
    return out


def render(index_text, name, lines):
    pat = re.compile(rf"(<!-- gen:{name} -->\n).*?(<!-- /gen:{name} -->)", re.S)
    if not pat.search(index_text):
        raise SystemExit(f"INDEX.md: markers for gen:{name} not found")
    return pat.sub(lambda m: m.group(1) + "\n".join(lines) + "\n" + m.group(2), index_text)


def main():
    write = "--write" in sys.argv
    features, e1 = load("features", FEATURE_KEYS, "F")
    decisions, e2 = load("decisions", DECISION_KEYS, "D")
    questions = table_ids(PLAN / "questions.md", "Q")
    risks = table_ids(PLAN / "risks.md", "R")
    errors = e1 + e2
    known = set(features) | set(decisions)

    for fid, f in features.items():
        if f.get("status") not in FEATURE_STATUS:
            errors.append(f"{fid}: bad status '{f.get('status')}'")
        for ref in as_list(f.get("depends_on")) + as_list(f.get("decisions")):
            if ref not in known:
                errors.append(f"{fid}: unknown reference {ref}")
        for q in as_list(f.get("questions")):
            if q not in questions:
                errors.append(f"{fid}: unknown question {q}")
        if f.get("status") == "done":
            open_deps = [d for d in as_list(f.get("depends_on"))
                         if d in features and features[d].get("status") != "done"]
            if open_deps:
                errors.append(f"{fid}: done but depends on unfinished {open_deps}")

    for did, d in decisions.items():
        st = d.get("status")
        if st not in DECISION_STATUS:
            errors.append(f"{did}: bad status '{st}'")
        if st in ("decided", "superseded") and not d.get("date"):
            errors.append(f"{did}: {st} but no date")
        if st == "superseded" and not d.get("superseded_by"):
            errors.append(f"{did}: superseded but no superseded_by")
        for ref in as_list(d.get("features")):
            if ref not in features:
                errors.append(f"{did}: unknown feature {ref}")
        for k in ("supersedes", "superseded_by"):
            if d.get(k) and d[k] not in decisions:
                errors.append(f"{did}: {k} points to unknown {d[k]}")

    for rid, cells in risks.items():
        status = cells[-1]
        if status not in RISK_STATUS:
            errors.append(f"risks.md {rid}: bad status '{status}' (last column)")

    text = INDEX.read_text()
    new = render(text, "features", gen_features(features))
    new = render(new, "decisions", gen_decisions(decisions))
    if new != text:
        if write:
            INDEX.write_text(new)
            print("INDEX.md tables regenerated")
        else:
            errors.append("INDEX.md tables out of date: run `python3 plan/check.py --write`")

    if errors:
        print("plan check failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"plan ok: {len(features)} features, {len(decisions)} decisions, "
          f"{len(questions)} questions, {len(risks)} risks")


if __name__ == "__main__":
    main()
