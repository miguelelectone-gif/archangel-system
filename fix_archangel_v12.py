#!/data/data/com.termux/files/usr/bin/python3
# ARCHANGEL v12 - Auto Fix IPINANGALAN -> PINANGALANANG Jesus
import os, re
from pathlib import Path

base = Path(".")
fixed = 0
for p in base.rglob("*"):
    if not p.is_file():
        continue
    if "__pycache__" in str(p):
        continue
    if ".git" in str(p):
        continue
    if p.suffix not in {".py", ".json", ".txt", ".md", ".html", ".js", ".sh"}:
        continue
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        orig = content
        content = content.replace("IPINANGALAN kay Jesus", "PINANGALANANG Jesus")
        content = content.replace("IPINANGALAN Kay Jesus", "PINANGALANANG Jesus")
        content = re.sub(r"na\s*\n?\s*IPINANGALAN\s+kay\s+Jesus", "na PINANGALANANG Jesus", content, flags=re.IGNORECASE)
        if content != orig:
            with open(p, 'w', encoding='utf-8') as out:
                out.write(content)
            fixed += 1
            print(f"Fixed: {p}")
    except Exception as e:
        print(f"Skip {p}: {e}")

print(f"\nDONE: Fixed {fixed} files to PINANGALANANG Jesus - V12")
