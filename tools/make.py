#!/usr/bin/env python3
"""Pathum Thani → mot-dang/assets/sites/pathum-thani/ (index.html, th/index.html, pt.js, img/, fonts/, card.json, icon.svg).

The page is also the home of pathumthani.motdang.net: the city build copies this folder to the subdomain root,
so the page's own files are relative, motdang.net pages are absolute, place pages go to motdang.net/pth/ (301s later).

    python3 tools/make.py
"""
import datetime
import html
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import content as C  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
MD = HERE.parent / "mot-dang"
OUT = MD / "assets" / "sites" / "pathum-thani"
FONTS = MD / "assets" / "sites" / "lanna-craft" / "fonts"
URL = "https://motdang.net/sites/pathum-thani/"
MAP = "https://motdang.net/sites/doodle-pathum-thani/"
E = html.escape
PICS = json.loads((HERE / "research" / "pics.json").read_text())


def L(d, lang):
    return d[lang] if isinstance(d, dict) else d


# ------------------------------------------------------------------ calendar
def events():
    rows = []
    src = MD / "_incoming" / "pt-pp-dates-2026-10-13.json"
    if src.exists():
        for r in json.loads(src.read_text()).get("pth", []):
            rows.append({"start": r["start"], "end": r.get("end"), "t": {"en": r["title_en"], "th": r["title_th"]},
                         "w": {"en": r["venue_en"], "th": r["venue_th"]}, "u": r.get("source_url"), "s": r.get("source_name", ""), "kind": ""})
    sky = json.loads((MD / "data" / "sky.json").read_text())["days"]
    for day, v in sky.items():
        m = v.get("moon", {})
        if m.get("wan_phra"):
            rows.append({"start": day, "t": {"en": "Wan phra · " + m["phase_en"].lower(), "th": "วันพระ · " + m["thai_label_th"]},
                         "w": {"en": "Every wat: morning alms and the precepts", "th": "ทุกวัด ตักบาตรเช้า รักษาศีล"}, "kind": "moon"})
    for r in C.HOLIDAYS:
        rows.append({**r, "kind": "hol"})
    rows.sort(key=lambda r: r["start"])
    return rows


def cal_json(lang):
    out = [{"start": r["start"], "end": r.get("end"), "t": L(r["t"], lang), "w": L(r["w"], lang), "u": r.get("u"), "s": r.get("s", ""), "kind": r.get("kind", "")} for r in events()]
    return json.dumps(out, ensure_ascii=False).replace("</", "<\\/")


# ------------------------------------------------------------------ pieces
def src_link(item, lang):
    if not item.get("src"):
        return ""
    return f'<a class="src" href="{E(item["src"])}" rel="noopener">{E(item.get("src_name") or ("source" if lang == "en" else "ที่มา"))}</a>'


def place_link(item, lang):
    if not item.get("place"):
        return ""
    t = "Mot Dang page" if lang == "en" else "หน้ามดแดง"
    return f' · <a class="src" href="https://motdang.net{E(item["place"])}">{t}</a>'


def credit(i):
    m = PICS[str(i)]
    return f'{E(m["author"] or "Wikimedia Commons")} · <a href="{E(m["page"])}" rel="noopener">{E(m["lic"])}</a>'


def img(i, alt, cap, cls=""):
    m = PICS[str(i)]
    return (f'<img src="{{R}}img/c{i}-800.jpg" srcset="{{R}}img/c{i}-800.jpg 800w, {{R}}img/c{i}-1600.jpg 1600w" sizes="(max-width:800px) 100vw, 50vw" '
            f'width="{m["w"]}" height="{m["h"]}" loading="lazy" decoding="async" alt="{E(alt)}" data-full="{{R}}img/c{i}-1600.jpg" '
            f'data-cap="{E(cap + " · ")}{E(credit(i))}"{cls}>')


def band(b, lang):
    i, cap = b["pic"], L(b["cap"], lang)
    return f'<figure class="band">{img(i, cap, cap)}<figcaption>{E(cap)}<small>{credit(i)}</small></figcaption></figure>'


def toy(t, lang):
    btns = "".join(f'<button id="{bid}"{" class=alt" if k else ""}>{E(L(lab, lang))}</button>' for k, (bid, lab) in enumerate(t.get("buttons", [])))
    return (f'<div class="toy"><h3>{E(L(t["h"], lang))}</h3><p>{E(L(t["p"], lang))}</p>'
            f'<canvas id="{t["id"]}" aria-label="{E(L(t["h"], lang))}"></canvas>'
            f'<div class="bar">{btns}<span class="read" id="{t["read"]}" aria-live="polite"></span></div></div>')


def face(name):
    """A drawn monogram for a person: a lotus-petal ring and their initial, spins on tap."""
    ch = E(name.strip()[0])
    petals = "".join(f'<ellipse cx="32" cy="9" rx="5" ry="9" transform="rotate({a} 32 32)" fill="#f6b3c8"/>' for a in range(0, 360, 45))
    return f'<svg class="face" viewBox="0 0 64 64" aria-hidden="true">{petals}<circle cx="32" cy="32" r="17" fill="#0f3b45"/><text x="32" y="39" text-anchor="middle" font-family="Prompt,sans-serif" font-size="20" fill="#fff">{ch}</text></svg>'


def cards(items, lang, kind=""):
    out = []
    for it in items:
        tag = f'<span class="tag">{E(L(it["tag"], lang))}</span>' if it.get("tag") else ""
        other = it["name"]["th" if lang == "en" else "en"]
        fc = face(it["name"][lang]) if kind == "person" else ""
        out.append(f'<article class="card {kind}">{fc}{tag}<h3>{E(it["name"][lang])}</h3><p class="th">{E(other)}</p>'
                   f'<p>{E(L(it["text"], lang))}</p>{src_link(it, lang)}{place_link(it, lang)}</article>')
    return f'<div class="cards">{"".join(out)}</div>'


def section(sid, kicker, h, dek, body, lang):
    return (f'<section id="{sid}"><div class="wrap"><p class="kicker">{E(L(kicker, lang))}</p><h2>{E(L(h, lang))}</h2>'
            + (f'<p class="dek">{E(L(dek, lang))}</p>' if dek else "") + body + '</div></section>')


def fonts_css(R):
    faces = [("Prompt", 600, "prompt-600"), ("Sarabun", 400, "sarabun-400"), ("Sarabun", 600, "sarabun-600")]
    thai, latin = "U+0E01-0E5B,U+200C-200D,U+25CC", "U+0000-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212,U+0E3F"
    out = []
    for fam, wt, stem in faces:
        for sub, rng in (("thai", thai), ("latin", latin)):
            out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};font-display:swap;src:url({R}fonts/{stem}-{sub}.woff2) format('woff2');unicode-range:{rng}}}")
    return "".join(out)


def page(lang):
    R = "" if lang == "en" else "../"
    S = C.SITE
    other = "th/" if lang == "en" else "../"
    nav = "".join(f'<a href="#{a}">{E(L(t, lang))}</a>' for a, t in C.NAV)
    canon = URL + ("" if lang == "en" else "th/")
    title = L(S["title"], lang)
    desc = L(S["desc"], lang)
    tldr = "".join(f'<li>{L(x, lang)}</li>' for x in C.TLDR)
    slab = "".join(f'<div class="num" role="button" tabindex="0"><b>{E(n["v"])}</b><span>{E(L(n["l"], lang))}</span></div>' for n in C.NUMBERS)
    tl = "".join(f'<li><b>{E(L(t["y"], lang))}</b>{E(L(t["text"], lang))} {src_link(t, lang)}</li>' for t in C.TIMELINE)
    pics = "".join(f'<figure>{img(p["pic"], L(p["cap"], lang), L(p["cap"], lang))}<figcaption>{E(L(p["cap"], lang))}</figcaption></figure>' for p in C.PICS)
    srcs = sorted({(it.get("src_name") or it["src"], it["src"]) for grp in (C.TIMELINE, C.LEGENDS, C.PEOPLE, C.SITES, C.CULTURE, C.FOOD, C.NUMBERS) for it in grp if it.get("src")})
    srcl = "".join(f'<li><a href="{E(u)}" rel="noopener">{E(n)}</a></li>' for n, u in srcs)
    T = C.TOYS
    body = f"""
<nav class="top" aria-label="{'Sections' if lang == 'en' else 'หมวด'}"><a class="home" href="https://motdang.net/">{'มดแดง' if lang == 'th' else 'Mot Dang'}</a>{nav}<a class="lang" href="{other}" hreflang="{'th' if lang == 'en' else 'en'}">{'ไทย' if lang == 'en' else 'EN'}</a></nav>
<header class="wrap mast"><h1>{E(L(S['h1'], lang))}<small>{E(L(S['h1small'], lang))}</small></h1><p>{E(L(S['lede'], lang))}</p></header>
<div class="wrap top2" id="map">
<div class="mapbox"><iframe src="{MAP}?embed=1" title="{E(L(S['map_t'], lang))}" loading="lazy" allow="geolocation"></iframe><a class="open" href="{MAP}">{E(L(S['map_open'], lang))}</a></div>
<div class="cal" id="calendar"><h2>{E(L(S['cal_h'], lang))}</h2><div id="evlist"><p class="empty">…</p></div><h2 class="soon">{E(L(S['soon_h'], lang))}</h2><ul class="soonl">{''.join(f"<li>{E(L(x, lang))}</li>" for x in C.SOON)}</ul></div>
</div>
<script type="application/json" id="evdata">{cal_json(lang)}</script>
<div class="hero"><canvas id="pond" aria-label="{E(L(S['pond_a'], lang))}"></canvas><div class="herotext"><p class="kicker">{E(L(S['pond_k'], lang))}</p><h2>{E(L(S['pond_h'], lang))}</h2><p>{E(L(S['pond_p'], lang))}</p><p class="count" id="lotuscount" aria-live="polite"></p></div></div>
{section('tldr', S['tldr_k'], S['tldr_h'], None, f'<ul class="tldr">{tldr}</ul><div class="slab">{slab}</div>', lang)}
{section('history', S['hist_k'], S['hist_h'], S['hist_d'], f'<ol class="tl">{tl}</ol>' + toy(T['canals'], lang), lang)}
{band(C.BANDS['history'], lang)}
{section('legends', S['leg_k'], S['leg_h'], S['leg_d'], cards(C.LEGENDS, lang, 'legend') + toy(T['jar'], lang), lang)}
{band(C.BANDS['legends'], lang)}
{section('people', S['ppl_k'], S['ppl_h'], S['ppl_d'], cards(C.PEOPLE, lang, 'person'), lang)}
{section('sites', S['site_k'], S['site_h'], S['site_d'], cards(C.SITES, lang) + toy(T['storks'], lang), lang)}
{band(C.BANDS['sites'], lang)}
{section('culture', S['cul_k'], S['cul_h'], S['cul_d'], cards(C.CULTURE, lang), lang)}
{band(C.BANDS['culture'], lang)}
{section('food', S['food_k'], S['food_h'], S['food_d'], cards(C.FOOD, lang) + toy(T['noodles'], lang), lang)}
{section('pics', S['pic_k'], S['pic_h'], S['pic_d'], f'<div class="pics">{pics}</div>', lang)}
{section('sources', S['src_k'], S['src_h'], S['src_d'], f'<ul class="sources">{srcl}</ul>', lang)}
<footer><a href="https://motdang.net/">มดแดง · Mot Dang</a> · <a href="https://motdang.net/pth/">{E(L(S['dir'], lang))}</a> · <a href="https://motdang.net/sites/">{'All minisites' if lang == 'en' else 'มินิไซต์ทั้งหมด'}</a></footer>
<dialog id="lb"><form method="dialog"><button class="x" aria-label="Close">×</button></form><img alt=""><p></p></dialog>
<script src="{R}pt.js" defer></script>"""
    body = body.replace("{R}", R)
    css = (HERE / "tools" / "style.css").read_text()
    head = f"""<!doctype html><html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0b2a31">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{URL}"><link rel="alternate" hreflang="th" href="{URL}th/"><link rel="alternate" hreflang="x-default" href="{URL}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Mot Dang · มดแดง">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{URL}card.jpg"><meta property="og:image:alt" content="{E(L(S['pond_a'], lang).split('.')[0])}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'th_TH'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{URL}card.jpg">
<link rel="icon" href="{R}icon.svg" type="image/svg+xml">
<style>{fonts_css(R)}{css}</style>
</head><body>"""
    return head + body + "\n</body></html>\n"


ICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b2a31"/>'
        + "".join(f'<path d="M32 50C{32 + w} {40} {32 + w * 0.8} {22} 32 {14}C{32 - w * 0.8} 22 {32 - w} 40 32 50Z" fill="{c}" transform="rotate({a} 32 50)"/>'
                  for a, w, c in ((-50, 9, "#f6b3c8"), (50, 9, "#f6b3c8"), (-25, 10, "#f39ab8"), (25, 10, "#f39ab8"), (0, 11, "#d9306f")))
        + '<rect x="10" y="52" width="44" height="4" rx="2" fill="#2e8c9a"/></svg>')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "th").mkdir(exist_ok=True)
    (OUT / "img").mkdir(exist_ok=True)
    (OUT / "fonts").mkdir(exist_ok=True)
    for f in FONTS.iterdir():
        if not (OUT / "fonts" / f.name).exists():
            shutil.copy2(f, OUT / "fonts" / f.name)
    for f in (HERE / "src" / "img").iterdir():
        dst = OUT / "img" / f.name
        if not dst.exists() or dst.stat().st_mtime < f.stat().st_mtime:
            shutil.copy2(f, dst)
    shutil.copy2(HERE / "tools" / "pt.js", OUT / "pt.js")
    (OUT / "icon.svg").write_text(ICON)
    (OUT / "index.html").write_text(page("en"))
    (OUT / "th" / "index.html").write_text(page("th"))
    if (HERE / "card.jpg").exists():
        shutil.copy2(HERE / "card.jpg", OUT / "card.jpg")
    card = {"id": "pathum-thani", "th": C.SITE["title"]["th"].split(" · ")[0], "en": C.SITE["title"]["en"].split(" · ")[0],
            "line_th": C.SITE["card_line"]["th"], "line_en": C.SITE["card_line"]["en"], "icon": "i-map",
            "shipped": datetime.date.today().isoformat(), "group": "go", "where": "pth", "served": "docs", "words": C.WORDS}
    (OUT / "card.json").write_text(json.dumps(card, ensure_ascii=False, indent=1))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
