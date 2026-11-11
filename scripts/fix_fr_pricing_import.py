# -*- coding: utf-8 -*-
with open(r"C:\Users\Dawda Mbowe\Antigravity\kunda\src\copy\fr.ts", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("import pricing from '@data/pricing.json';", "import pricing from '@data/fr/pricing.json';")

with open(r"C:\Users\Dawda Mbowe\Antigravity\kunda\src\copy\fr.ts", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated fr.ts import")

