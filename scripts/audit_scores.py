import os
import glob
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Collect score files
search_dirs = [
    Path.home() / "Downloads",
    Path(r"c:\Users\felip\OneDrive - uc.cl\Yo\IA\GitHub\mi_musica_app\static\media")
]

score_files = []
for d in search_dirs:
    if d.exists():
        for ext in ["*.musicxml", "*.xml", "*.mxl"]:
            score_files.extend(list(d.glob(ext)))

print(f"Total score files found: {len(score_files)}")

issues_found = []

for sf in score_files:
    # Skip our generated files
    if "_Cantamus" in sf.name:
        continue
    try:
        if sf.suffix.lower() == ".mxl":
            with zipfile.ZipFile(str(sf), "r") as z:
                candidates = [f for f in z.namelist() if f.endswith(".xml") or f.endswith(".musicxml")]
                if not candidates:
                    continue
                root = ET.fromstring(z.read(candidates[0]))
        else:
            tree = ET.parse(str(sf))
            root = tree.getroot()
    except Exception as e:
        issues_found.append((sf.name, f"Error parsing: {e}"))
        continue

    file_issues = []

    # 1. Check for multiple verses / lyrics numbers
    lyric_numbers = set()
    for l in root.findall(".//lyric"):
        num = l.get("number")
        if num and num != "1":
            lyric_numbers.add(num)
    if lyric_numbers:
        file_issues.append(f"Multiple lyric verses: numbers={sorted(list(lyric_numbers))}")

    # 2. Check for melisma / extend
    extends = root.findall(".//lyric/extend")
    if extends:
        file_issues.append(f"Contains <extend/> (melisma): {len(extends)} occurrences")

    # 3. Check for multiple voices in vocal parts
    voices = set()
    for v in root.findall(".//note/voice"):
        if v.text and v.text.strip() not in ["", "1"]:
            voices.add(v.text.strip())
    if voices:
        file_issues.append(f"Multiple voices found: {voices}")

    # 4. Check for chords (divisi) in notes
    chords = root.findall(".//note/chord")
    if chords:
        file_issues.append(f"Chords (<chord/>) found: {len(chords)} notes")

    # 5. Check for repeats or voltas (1st/2nd ending)
    repeats = root.findall(".//repeat")
    endings = root.findall(".//ending")
    if repeats or endings:
        file_issues.append(f"Repeats/Endings: {len(repeats)} repeats, {len(endings)} endings")

    # 6. Check for pickup measure (anacrusis)
    measures = root.findall(".//part[1]/measure")
    if measures:
        first_m = measures[0]
        m_num = first_m.get("number", "1")
        if m_num == "0":
            file_issues.append("Pickup measure detected (number='0')")

    # 7. Check for fermatas
    fermatas = root.findall(".//fermata")
    if fermatas:
        file_issues.append(f"Fermatas found: {len(fermatas)}")

    # 8. Check for unusual lyric characters
    unusual_lyrics = []
    for l in root.findall(".//lyric/text"):
        if l.text:
            t = l.text
            if re.search(r"[0-9]\.", t) or "..." in t or re.search(r"[^\w\sÁÉÍÓÚáéíóúÑñÜü]", t):
                unusual_lyrics.append(t)
    if unusual_lyrics:
        file_issues.append(f"Unusual lyrics tokens (sample): {unusual_lyrics[:8]}")

    # 9. Check for tempo markings and words
    words = []
    for w in root.findall(".//direction/direction-type/words"):
        if w.text and any(k in w.text.lower() for k in ["rit", "accel", "tempo", "a tempo", "lento", "allegro", "andante"]):
            words.append(w.text.strip())
    if words:
        file_issues.append(f"Tempo words found: {words[:6]}")

    if file_issues:
        issues_found.append((sf.name, file_issues))

print("\n=== AUDIT RESULTS ACROSS EXISTING SCORES ===")
for name, issues in issues_found:
    print(f"\n[{name}]")
    if isinstance(issues, list):
        for iss in issues:
            print(f"  - {iss}")
    else:
        print(f"  - {issues}")
