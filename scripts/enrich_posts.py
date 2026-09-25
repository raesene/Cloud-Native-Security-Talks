#!/usr/bin/env python3
"""Add structured front matter to talk posts.

Parses the conference name, speakers, YouTube ID and Sched URL out of each
post in _posts/ and writes them as front matter fields that the site layouts
use. The "## Abstract" heading, Sched link and "## Video" embed are removed
from the body, because the talk layout renders them from front matter.

Safe to re-run: fields that already exist are left alone, so hand fixes
(e.g. to a speaker split that the heuristic got wrong) are preserved.

Usage: python3 scripts/enrich_posts.py [--check]
"""

import json
import re
import sys
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "_posts"

# (series id, series label, short code, matcher)
SERIES = [
    ("security-day", "Cloud Native Security Day", "CNSD", re.compile(r"Security Day", re.I)),
    ("securitycon", "CloudNativeSecurityCon", "CNSC", re.compile(r"Security ?Con", re.I)),
    ("kubecon-china", "KubeCon China", "KC-CN", re.compile(r"China|中国", re.I)),
    ("kubecon-eu", "KubeCon Europe", "KC-EU", re.compile(r"Europe", re.I)),
    ("kubecon-na", "KubeCon North America", "KC-NA", re.compile(r"North America|KubeCon 2016", re.I)),
]

# Regions named on the non-KubeCon events, which ran both sides of the Atlantic
REGIONS = [("Europe", "EU"), ("North America", "NA")]

FIELDS = ["talk_title", "speakers", "event", "series", "event_code", "year", "youtube_id", "sched_url"]


def classify(category):
    for sid, label, code, rx in SERIES:
        if rx.search(category):
            year = re.search(r"(20\d\d)", category).group(1)
            virtual = " (Virtual)" if "Virtual" in category or "线上" in category else ""
            if not sid.startswith("kubecon"):
                for name, short in REGIONS:
                    if name in category:
                        label, code = f"{label} {name}", f"{code}-{short}"
            return {
                "series": sid,
                "event": f"{label} {year}{virtual}",
                "event_code": f"{code}-{year[2:]}",
                "year": int(year),
            }
    raise ValueError(f"unknown conference: {category}")


def split_title(title):
    """'Talk Title - Speaker, Org' -> ('Talk Title', 'Speaker, Org')."""
    m = re.match(r"^(.*\S)\s*-\s+(.+)$", title)
    if m and "," in m.group(2):
        speakers = re.sub(r"\s*\((?:[^()]*Skill Level|Slides Attached)\)", "", m.group(2))
        speakers = re.sub(r"^Moderated by\s+", "", speakers)
        return m.group(1), speakers
    return title, ""


def parse(path):
    text = path.read_text(encoding="utf-8")
    _, fm, body = text.split("---\n", 2)
    return fm, body


def fm_value(fm, key):
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    return m.group(1).strip() if m else None


def enrich(path):
    fm, body = parse(path)
    title = json.loads(fm_value(fm, "title"))
    category = json.loads(fm_value(fm, "categories"))[0]

    data = classify(category)
    data["talk_title"], data["speakers"] = split_title(title)

    yt = re.search(r"youtube\.com/embed/([\w-]{11})", body)
    data["youtube_id"] = yt.group(1) if yt else ""
    sched = re.search(r"\[Sched URL\]\((\S+?)\)", body)
    data["sched_url"] = sched.group(1) if sched else ""

    new_fm = fm.rstrip("\n") + "\n"
    for key in FIELDS:
        if fm_value(fm, key) is None:
            val = data[key]
            new_fm += f"{key}: {val if isinstance(val, int) else json.dumps(val, ensure_ascii=False)}\n"

    new_body = body
    new_body = re.sub(r"^## Abstract\s*\n", "", new_body, flags=re.M)
    new_body = re.sub(r"^\[Sched URL\]\(.*?\)\s*\n?", "", new_body, flags=re.M)
    if data["youtube_id"]:
        new_body = re.sub(r"^## Video\s*\n.*", "", new_body, flags=re.M | re.S)
    else:
        new_body = re.sub(r"^## Video\s*\n?", "", new_body, flags=re.M)
    new_body = "\n" + new_body.strip() + "\n"

    return f"---\n{new_fm}---\n{new_body}", data


def main():
    check = "--check" in sys.argv
    changed, warnings = 0, []
    for path in sorted(POSTS.glob("*.md")):
        out, _ = enrich(path)
        fm, _ = out.split("---\n", 2)[1:]
        if fm_value(fm, "speakers") == '""':
            warnings.append(f"no speakers parsed: {path.name}")
        if fm_value(fm, "youtube_id") == '""':
            warnings.append(f"no video: {path.name}")
        if out != path.read_text(encoding="utf-8"):
            changed += 1
            if not check:
                path.write_text(out, encoding="utf-8")
    for w in warnings:
        print(w, file=sys.stderr)
    print(f"{changed} post(s) {'need updating' if check else 'updated'}")
    return 1 if check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
