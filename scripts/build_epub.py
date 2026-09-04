#!/usr/bin/env python3
"""
books/<slug>/chapters/*.md → epub (내부 판매용, 한국어).
  python3 scripts/build_epub.py books/<slug> [--title "제목"] [--author "이선일"]
의존: pip3 install ebooklib markdown   (Pillow 있으면 cover.jpg 자동 삽입)
"""
import sys, os, re, glob, argparse
LANG="en"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("book"); ap.add_argument("--title"); ap.add_argument("--author", default="Author"); a = ap.parse_args()
    try:
        from ebooklib import epub; import markdown
    except ImportError:
        print("pip3 install ebooklib markdown"); sys.exit(2)
    global LANG
    slug = os.path.basename(os.path.normpath(a.book))
    bp = os.path.join(a.book, "brief.md")
    if os.path.exists(bp) and re.search(r"언어[:：]\s*한국어", open(bp, encoding="utf-8").read()): LANG = "ko"
    chapters = sorted(glob.glob(os.path.join(a.book, "chapters", "*.md")))
    if not chapters: print("chapters/ 비어 있음"); sys.exit(2)
    title = a.title
    if not title:
        m = re.search(r"^#\s*(.+)", open(os.path.join(a.book, "brief.md"), encoding="utf-8").read(), re.M) if os.path.exists(os.path.join(a.book, "brief.md")) else None
        title = (m.group(1).split("—")[0].strip() if m else slug)
    bk = epub.EpubBook(); bk.set_identifier(f"morningwalk-{slug}"); bk.set_title(title); bk.set_language(LANG); bk.add_author(a.author)
    cover = os.path.join(a.book, "cover.jpg")
    if os.path.exists(cover): bk.set_cover("cover.jpg", open(cover, "rb").read())
    css = epub.EpubItem(uid="style", file_name="style.css", media_type="text/css",
        content="body{font-family:'Noto Serif KR',serif;line-height:1.7} h1{font-family:'Noto Sans KR',sans-serif;color:#1e3a8a} blockquote{border-left:3px solid #1e3a8a;padding-left:1em;color:#444} table{border-collapse:collapse} td,th{border:1px solid #ccc;padding:4px 8px}")
    bk.add_item(css); items = []
    for i, path in enumerate(chapters, 1):
        md = open(path, encoding="utf-8").read()
        md = re.sub(r"<!--.*?-->", "", md, flags=re.S).strip()
        if not re.search(r"status:\s*final", open(path, encoding="utf-8").read()):
            print(f"경고: {os.path.basename(path)} 는 final 아님")
        h = re.search(r"^#\s*(.+)", md, re.M); ch_title = h.group(1) if h else f"{i}장"
        html = markdown.markdown(md, extensions=["tables", "fenced_code"])
        c = epub.EpubHtml(title=ch_title, file_name=f"ch{i:02d}.xhtml", lang=LANG); c.content = html; c.add_item(css)
        bk.add_item(c); items.append(c)
    bk.toc = items; bk.add_item(epub.EpubNcx()); bk.add_item(epub.EpubNav()); bk.spine = ["nav"] + items
    out = os.path.join(a.book, f"{slug}.epub"); epub.write_epub(out, bk); print(f"생성: {out} ({len(items)}장)")

if __name__ == "__main__":
    main()
