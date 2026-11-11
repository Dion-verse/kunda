# -*- coding: utf-8 -*-
"""
Fix typing errors in copy files and clean up tool page syntax
"""
import os

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update en.ts
with open(os.path.join(ROOT, "src/copy/en.ts"), "r", encoding="utf-8") as f:
    en_text = f.read()

if "'micro-saas': 'Micro-SaaS'" not in en_text:
    en_text = en_text.replace(
        "products: 'Products',",
        "products: 'Products',\n      'micro-saas': 'Micro-SaaS',"
    )
    with open(os.path.join(ROOT, "src/copy/en.ts"), "w", encoding="utf-8") as f:
        f.write(en_text)
    print("Fixed en.ts: added 'micro-saas' label")

# 2. Update fr.ts
with open(os.path.join(ROOT, "src/copy/fr.ts"), "r", encoding="utf-8") as f:
    fr_text = f.read()

if "'micro-saas': 'Micro-SaaS'" not in fr_text:
    fr_text = fr_text.replace(
        "products: 'Produits',",
        "products: 'Produits',\n      'micro-saas': 'Micro-SaaS',"
    )

fr_text = fr_text.replace(
    "import pricing from '@data/fr/pricing.json';",
    "import pricing from '@data/pricing.json';"
)

with open(os.path.join(ROOT, "src/copy/fr.ts"), "w", encoding="utf-8") as f:
    f.write(fr_text)
print("Fixed fr.ts: added 'micro-saas' label and updated pricing import")

