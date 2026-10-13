#!/usr/bin/env python3
"""Walk Commons categories (depth 2) → research/commons.json: file, thumb 1600, size, author, licence, category."""
import json, sys, time, urllib.parse, urllib.request
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "motdang.net minisite builder (nan@motdang.net)"}
def get(**p):
    q = API + "?" + urllib.parse.urlencode({**p, "format": "json"})
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(q, headers=UA), timeout=30))
        except Exception as e: time.sleep(2)
    return {}
def members(cat):
    out, cont = [], {}
    while True:
        r = get(action="query", list="categorymembers", cmtitle=cat, cmlimit=500, **cont)
        out += r.get("query", {}).get("categorymembers", [])
        if "continue" not in r: return out
        cont = {"cmcontinue": r["continue"]["cmcontinue"]}
files, seen = {}, set()
def walk(cat, depth):
    if cat in seen: return
    seen.add(cat)
    for m in members(cat):
        if m["ns"] == 6: files.setdefault(m["title"], cat)
        elif m["ns"] == 14 and depth > 0: walk(m["title"], depth - 1)
for c in sys.argv[1:]: walk("Category:" + c, 2)
print(len(files), "files in", len(seen), "categories", file=sys.stderr)
rows, titles = [], [t for t in files if t.lower().endswith((".jpg", ".jpeg", ".png"))]
for i in range(0, len(titles), 40):
    r = get(action="query", titles="|".join(titles[i:i+40]), prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=1600)
    for p in r.get("query", {}).get("pages", {}).values():
        if "imageinfo" not in p: continue
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        rows.append({"title": p["title"], "cat": files[p["title"]], "thumb": ii.get("thumburl"), "w": ii["width"], "h": ii["height"],
                     "page": ii["descriptionurl"], "author": m.get("Artist", {}).get("value", ""),
                     "lic": m.get("LicenseShortName", {}).get("value", ""), "desc": m.get("ImageDescription", {}).get("value", "")[:300]})
json.dump(rows, open("research/commons.json", "w"), ensure_ascii=False, indent=1)
print(len(rows), "images", file=sys.stderr)
