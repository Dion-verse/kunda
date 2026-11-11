# -*- coding: utf-8 -*-
"""
Cleanup remaining 24 legacy occurrences across:
- src/components/Meta.astro (fallback domain)
- src/pages/manifest.json.ts (manifest name and icons)
- src/copy/fr.ts (testimonials names)
- src/data_files/fr/faqs.json & features.json
- multilingual docs guides
"""
import os, glob, re

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Clean Meta.astro
meta_path = os.path.join(ROOT, "src/components/Meta.astro")
with open(meta_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'screwfast\.uk', 'kunda.works', text, flags=re.I)
with open(meta_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned Meta.astro")

# 2. Clean manifest.json.ts
manifest_path = os.path.join(ROOT, "src/pages/manifest.json.ts")
with open(manifest_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'ScrewFast', 'KUNDA', text)
with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned manifest.json.ts")

# 3. Clean fr.ts remaining names
fr_path = os.path.join(ROOT, "src/copy/fr.ts")
with open(fr_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("Samantha Ruiz", "Maya Chen").replace("ConstructIt", "Stackbloom")
text = text.replace("Jason Clark", "Alex Morgan").replace("TopBuild", "Stackbloom")
text = text.replace("Maria Gonzalez", "Elena Rostova").replace("Creative Spaces", "CloudPulse")
text = text.replace("Richard Kim", "Marcus Vance").replace("WoodWright", "ShipFast Studio")
with open(fr_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Cleaned fr.ts testimonials")

# 4. Clean src/data_files/fr/faqs.json and features.json by copying from en (KUNDA versions)
import json
with open(os.path.join(ROOT, "src/data_files/faqs.json"), 'r', encoding='utf-8') as f:
    en_faqs = json.load(f)
with open(os.path.join(ROOT, "src/data_files/fr/faqs.json"), 'w', encoding='utf-8') as f:
    json.dump(en_faqs, f, indent=2, ensure_ascii=False)

with open(os.path.join(ROOT, "src/data_files/features.json"), 'r', encoding='utf-8') as f:
    en_features = json.load(f)
with open(os.path.join(ROOT, "src/data_files/fr/features.json"), 'w', encoding='utf-8') as f:
    json.dump(en_features, f, indent=2, ensure_ascii=False)
print("Updated fr faqs and features json")

# 5. Clean multilingual docs guides
for loc in ['de', 'es', 'fa', 'fr', 'ja', 'zh-cn']:
    for mdx in glob.glob(os.path.join(ROOT, f"src/content/docs/{loc}/**/*.md*"), recursive=True):
        try:
            with open(mdx, 'r', encoding='utf-8') as f:
                c = f.read()
            if 'ScrewFast' in c or 'screwfast' in c:
                c = re.sub(r'ScrewFast', 'KUNDA', c)
                c = re.sub(r'screwfast', 'kunda', c)
                with open(mdx, 'w', encoding='utf-8') as f:
                    f.write(c)
        except Exception:
            pass
print("Cleaned multilingual docs guides")
print("ALL CLEANUPS FINISHED!")

