import os
import json
import re
content = "pyq" # notes, pyq
ROOT_DIR = "/sdcard/.workspace/web/knowlet/" + content   # folder where your HTML files are stored
OUTPUT_FILE = "/sdcard/.workspace/web/knowlet/assets/" + content + ".json"

notes = []
total = 0

def clean_text(text):
  return re.sub(r"\s+", " ", text).strip()

# Regex patterns for <title> and first <h1>
title_pattern = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
h1_pattern = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)

for root, _, files in os.walk(ROOT_DIR):
  for file in files:
    # if re.match(r"unit_(\d+)\.html", file):
      path = os.path.join(root, file)

      with open(path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

      # Extract title
      title_match = title_pattern.search(html)
      title = clean_text(title_match.group(1)) if title_match else file

      # Extract first h1
      h1_match = h1_pattern.search(html)
      h1 = clean_text(h1_match.group(1)) if h1_match else ""

      # Clean relative path
      rel_path = path.replace(ROOT_DIR.removesuffix('notes'), "").replace("\\", "/").removesuffix('.html')
      
      notes.append({
        "title": title,
        "h1": h1,
        "path": content + rel_path
      })
      total += 1
      
# Write notes.json
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
  json.dump(notes, f, indent=2, ensure_ascii=False)

print(f"{OUTPUT_FILE} Generated ✔️ With {len(notes)} notes.")