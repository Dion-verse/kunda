# -*- coding: utf-8 -*-
import os

view_path = r"C:\Users\Dawda Mbowe\Antigravity\kunda\src\views\HomeView.astro"
with open(view_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "import heroImage from '@images/hero-image.avif';",
    "import heroImage from '@images/kunda-brand-board.jpg';"
)
text = text.replace(
    "import featureImage from '@images/features-image.avif';",
    "import featureImage from '@images/kunda-brand-board.jpg';"
)

with open(view_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("HomeView.astro successfully updated to use KUNDA brand visual!")

