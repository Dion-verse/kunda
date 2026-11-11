# -*- coding: utf-8 -*-
import json
import os

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

pricing_data = {
  "title": "Simple, Transparent Ecosystem Plans",
  "subTitle": "Choose the right tier to access KUNDA micro-applications, premium resources, and developer tooling.",
  "badge": "Community Favorite",
  "thirdOption": "Custom Digital Solutions?",
  "btnText": "Get in Touch",
  "starterKit": {
    "name": "Community & Free Tools",
    "description": "Complete access to all browser-first utilities, public checklists, and open knowledge resources.",
    "price": "0",
    "cents": "",
    "billingFrequency": "Free Forever",
    "features": [
      "Access to all 3+ free browser tools",
      "No account or credit card required",
      "Standard resource downloads",
      "Public documentation and guides",
      "100% client-side privacy protection"
    ],
    "purchaseBtnTitle": "Start Using Free Tools",
    "purchaseLink": "/tools"
  },
  "professionalToolbox": {
    "name": "Pro Maker",
    "description": "Ideal for independent developers, founders, and boutique digital agencies shipping products.",
    "price": "29",
    "cents": ".00",
    "billingFrequency": "per month",
    "features": [
      "Priority early access to all Micro-SaaS tools",
      "Full access to QueuePass & AssetSnag beta",
      "All editable agency kits (DOCX, Notion)",
      "Continuous feature updates and bugfixes",
      "Direct founder support via email"
    ],
    "purchaseBtnTitle": "Explore Pro Access",
    "purchaseLink": "/contact"
  }
}

# Update en pricing.json
with open(os.path.join(ROOT, "src/data_files/pricing.json"), "w", encoding="utf-8") as f:
    json.dump(pricing_data, f, indent=2, ensure_ascii=False)
print("Updated src/data_files/pricing.json with professionalToolbox and purchaseBtnTitle/Link")

# Update fr pricing.json
with open(os.path.join(ROOT, "src/data_files/fr/pricing.json"), "w", encoding="utf-8") as f:
    json.dump(pricing_data, f, indent=2, ensure_ascii=False)
print("Updated src/data_files/fr/pricing.json")

