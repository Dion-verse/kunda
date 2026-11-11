# -*- coding: utf-8 -*-
"""
Remediation script for Phase 1: Products, Blog, Insights, Features, Pricing, FAQs.
Transforms legacy construction data into pure KUNDA software/digital product data.
"""

import json
import os

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update features.json
features_data = [
  {
    "heading": "Focused Micro-SaaS",
    "content": "Targeted, lightweight software tools engineered to solve specific operational headaches without enterprise bloat.",
    "svg": "groups"
  },
  {
    "heading": "Free Online Utilities",
    "content": "Instant client-side developer and creator tools including JSON Formatter, Password Entropy Analyzer, and QR Code Generator.",
    "svg": "tools"
  },
  {
    "heading": "Curated Resource Library",
    "content": "Production checklists, technical specifications, and agency onboarding guides built to accelerate your product launches.",
    "svg": "dashboard"
  },
  {
    "heading": "Modern Serverless Architecture",
    "content": "Blazing fast global edge delivery with zero-maintenance, zero-cold-start reliability powered by modern cloud native infrastructure.",
    "svg": "house"
  }
]
with open(os.path.join(ROOT, "src/data_files/features.json"), "w", encoding="utf-8") as f:
    json.dump(features_data, f, indent=2, ensure_ascii=False)
print("Updated features.json")

# 2. Update pricing.json
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
    "btnText": "Start Using Free Tools",
    "purchaseBtnStyle": "border-neutral-200 bg-neutral-100 text-neutral-800 hover:bg-neutral-200 dark:border-neutral-700 dark:bg-neutral-800 dark:text-neutral-100"
  },
  "professionalPack": {
    "name": "Pro Maker",
    "description": "Ideal for independent developers, founders, and boutique digital agencies shipping products.",
    "price": "29",
    "cents": ".00",
    "billingFrequency": "per month",
    "features": [
      "Priority early access to all Micro-SaaS tools",
      "Full access to QueuePass & AssetSnag beta",
      "All editable agency kits (DOCX, Figma, Notion)",
      "Continuous feature updates and bugfixes",
      "Direct founder support via email"
    ],
    "btnText": "Explore Pro Access",
    "purchaseBtnStyle": "border-transparent bg-orange-500 text-white hover:bg-orange-600 focus-visible:ring-orange-500 dark:focus-visible:ring-orange-500"
  }
}
with open(os.path.join(ROOT, "src/data_files/pricing.json"), "w", encoding="utf-8") as f:
    json.dump(pricing_data, f, indent=2, ensure_ascii=False)
print("Updated pricing.json")

# 3. Update faqs.json
faqs_data = {
  "subTitle": "Common questions about KUNDA products, free utilities, and our digital ecosystem.",
  "faqs": [
    {
      "question": "What is KUNDA?",
      "answer": "KUNDA is an independent digital ecosystem and parent brand uniting targeted micro-SaaS applications, free developer utilities, curated resources, and technical guides under one central digital roof."
    },
    {
      "question": "Are the online tools really 100% free?",
      "answer": "Yes. Our JSON Formatter, Password Analyzer, and QR Code Generator require no account creation, no subscription, and run client-side in your browser with strict data privacy."
    },
    {
      "question": "What is Micro-SaaS and how does it work at KUNDA?",
      "answer": "Micro-SaaS products are lean, focused software applications designed to solve one specific workflow problem exceptionally well (e.g., QueuePass for waiting lines, AssetSnag for client uploads) without bloated enterprise overhead."
    },
    {
      "question": "How can I access downloadable resources?",
      "answer": "Visit our Resources directory to browse developer checklists and client onboarding templates. Free resources are unlocked directly for community download."
    },
    {
      "question": "How do I request a custom digital tool or integration?",
      "answer": "Reach out through our Contact page or email hello@kunda.works to discuss custom software development, tool partnerships, or digital consulting."
    }
  ]
}
with open(os.path.join(ROOT, "src/data_files/faqs.json"), "w", encoding="utf-8") as f:
    json.dump(faqs_data, f, indent=2, ensure_ascii=False)
print("Updated faqs.json")

# 4. Products: item-a765 (QueuePass)
item_a765_en = """---
title: 'QueuePass'
description: 'Smart SMS Waitlist & Mobile Queue Management'
main:
  id: 1
  content: |
    QueuePass eliminates physical congestion and front-desk friction for walk-in services, boutique clinics, popups, and community venues. Customers scan a QR code to join an SMS-notified virtual waitlist with real-time countdown updates.
  imgCard: '@/images/product-image-2.avif'
  imgMain: '@/images/product-image-main-2.avif'
  imgAlt: 'QueuePass interface preview on mobile and tablet'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Overview'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Architecture'
longDescription:
  title: 'Streamline Customer Flow Without Expensive Hardware'
  subTitle: 'QueuePass delivers a frictionless customer queue experience powered by lightweight web technology and low-latency SMS updates.'
  btnTitle: 'Join the Beta Waitlist'
  btnURL: '/contact'
descriptionList:
  - title: 'Frictionless QR Check-In'
    subTitle: 'Guests scan a counter QR code to join without downloading any native app or creating a permanent account.'
  - title: 'Automated SMS Alerts'
    subTitle: 'Keep guests informed of their position and receive automated call-back notifications when ready.'
  - title: 'Live Merchant Dashboard'
    subTitle: 'Staff manage entries from any tablet or phone browser with one-tap status toggles and wait estimation.'
specificationsLeft:
  - title: 'Target Market'
    subTitle: 'Walk-in salons, independent medical clinics, urgent care, pop-up events, food trucks'
  - title: 'Deployment'
    subTitle: 'Cloud-hosted edge application with zero on-premise hardware required'
  - title: 'Notifications'
    subTitle: 'Direct transactional SMS and mobile web dashboard status'
specificationsRight:
  - title: 'Status'
    subTitle: 'Active Beta & Early Access'
  - title: 'Tier Pricing'
    subTitle: '$29/mo flat rate per location with included SMS allowance'
  - title: 'Integrations'
    subTitle: 'Webhooks, Zapier, and custom POS exports'
tableData:
  - feature: ['Cloud Edge Latency', '< 50ms Global']
    description:
      - ['Client App Requirement', 'None (Mobile Browser)']
      - ['Custom Branding', 'Yes (Logo & Theme)']
blueprints:
  first: '@/images/product-image-2.avif'
  second: '@/images/product-image-main-2.avif'
---
"""

# 5. Products: item-b203 (AssetSnag)
item_b203_en = """---
title: 'AssetSnag'
description: 'Agency Client File Intake & Format Pre-flight Validator'
main:
  id: 2
  content: |
    AssetSnag stops the endless email back-and-forth of missing client assets. Branded upload portals automatically validate file dimensions, vector formats, color spaces, and font requirements before allowing the upload to complete.
  imgCard: '@/images/product-image-3.avif'
  imgMain: '@/images/product-image-main-3.avif'
  imgAlt: 'AssetSnag file validation portal interface'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Overview'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Specifications'
longDescription:
  title: 'No More Low-Resolution Logos or Corrupt Files'
  subTitle: 'Set strict asset requirements for clients and let automated validation do the tedious enforcement.'
  btnTitle: 'Request Early Access'
  btnURL: '/contact'
descriptionList:
  - title: 'Format & Dimension Gatekeeper'
    subTitle: 'Enforce minimum pixel dimensions, exact SVG specifications, and CMYK/RGB profile requirements automatically.'
  - title: 'White-Label Portals'
    subTitle: 'Send clients to a beautiful portal carrying your creative agency domain and brand identity.'
  - title: 'Cloud Storage Sync'
    subTitle: 'Accepted assets sync instantly to organized client folders in Google Drive, Dropbox, or S3.'
specificationsLeft:
  - title: 'Target Audience'
    subTitle: 'Web design studios, digital branding agencies, marketing teams'
  - title: 'File Types Handled'
    subTitle: 'PNG, SVG, AI, EPS, PDF, MP4, WebP, ZIP packages'
specificationsRight:
  - title: 'Validation Rules'
    subTitle: 'Resolution, aspect ratio, color profile, file size limits'
  - title: 'Pricing'
    subTitle: '$39/mo per agency with unlimited client upload portals'
tableData:
  - feature: ['Max File Size', '500MB per upload']
    description:
      - ['Security', 'Encrypted in transit & at rest']
      - ['Client Friction', 'Drag-and-drop web UI']
blueprints:
  first: '@/images/product-image-3.avif'
  second: '@/images/product-image-main-3.avif'
---
"""

# 6. Products: item-f303 (SeatSentry)
item_f303_en = """---
title: 'SeatSentry'
description: 'SaaS Inactive User & Seat Waste Monitor'
main:
  id: 3
  content: |
    SeatSentry hooks into your team workspace accounts (Google Workspace, Microsoft 365, Slack, GitHub) to instantly detect dormant users, orphaned seats, and offboarding oversights that silently inflate your monthly software bills.
  imgCard: '@/images/product-image-1.avif'
  imgMain: '@/images/product-image-main-1.avif'
  imgAlt: 'SeatSentry license optimization overview dashboard'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Overview'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Governance'
longDescription:
  title: 'Recover Wasted SaaS Spend Automatically'
  subTitle: 'Stop paying for licenses assigned to ex-employees, contractors who finished months ago, or unused accounts.'
  btnTitle: 'Join Waitlist'
  btnURL: '/contact'
descriptionList:
  - title: 'Dormancy Detection'
    subTitle: 'Flags any account inactive for 30, 60, or 90 days across connected SaaS providers.'
  - title: 'Offboarding Assurance'
    subTitle: 'Verifies complete account decommissioning when an employee leaves the company.'
  - title: 'Instant ROI Dashboard'
    subTitle: 'Calculate exact dollar savings achieved each month through reclaimed seat licenses.'
specificationsLeft:
  - title: 'Connected Platforms'
    subTitle: 'Google Workspace, Microsoft 365, Slack, Notion, GitHub, Zoom'
  - title: 'Audit Cadence'
    subTitle: 'Continuous weekly scans with real-time Slack/Email digests'
specificationsRight:
  - title: 'Target Market'
    subTitle: 'Startups, IT managers, distributed teams of 15 to 250 seats'
  - title: 'Pricing'
    subTitle: '$49/mo flat rate monitor for up to 100 seats'
tableData:
  - feature: ['Scan Overhead', 'Read-Only API Tokens']
    description:
      - ['Data Stored', 'Metadata only (zero document access)']
      - ['Compliance', 'SOC-2 compliant security standards']
blueprints:
  first: '@/images/product-image-1.avif'
  second: '@/images/product-image-main-1.avif'
---
"""

# 7. Products: item-t845 (KUNDA Free Tools)
item_t845_en = """---
title: 'KUNDA Developer Utilities'
description: 'Free, Client-Side Developer & Creator Web Tools'
main:
  id: 4
  content: |
    A cohesive suite of fast, lightweight online utilities engineered for privacy. Format JSON payloads, analyze password cryptographic entropy, and generate customizable QR codes directly in your browser with zero network transmission.
  imgCard: '@/images/product-image-2.avif'
  imgMain: '@/images/product-image-main-2.avif'
  imgAlt: 'KUNDA Developer Utilities tool suite'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Included Tools'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Privacy Architecture'
longDescription:
  title: 'Tools That Respect Your Data and Never Send It to a Cloud Server'
  subTitle: 'Engineered entirely with WebCrypto and client-side processing for instant execution without latency.'
  btnTitle: 'Open Free Tools'
  btnURL: '/tools'
descriptionList:
  - title: 'JSON Formatter & Validator'
    subTitle: 'Clean, validate, beautify, and minify complex JSON files with syntax validation and instant clipboard copy.'
  - title: 'Password Entropy Analyzer'
    subTitle: 'Calculate cryptographic bits of entropy, brute-force crack time estimates, and generate secure random passwords.'
  - title: 'Instant QR Code Generator'
    subTitle: 'Generate clean QR codes for links and contact cards with custom dimensions and direct image exports.'
specificationsLeft:
  - title: 'Privacy Level'
    subTitle: '100% Client-Side Processing for JSON & Password tools'
  - title: 'Cost'
    subTitle: 'Free Forever with unlimited use'
specificationsRight:
  - title: 'Registration'
    subTitle: 'No account, sign-in, or tracking required'
  - title: 'Availability'
    subTitle: 'Publicly active on kunda.works/tools'
tableData:
  - feature: ['Execution Environment', 'Client Web Browser']
    description:
      - ['Offline Capable', 'Yes (via Service Worker caching)']
      - ['Telemetry', 'Zero sensitive payload tracking']
blueprints:
  first: '@/images/product-image-2.avif'
  second: '@/images/product-image-main-2.avif'
---
"""

# Write English products
for fname, content in [
    ("item-a765.md", item_a765_en),
    ("item-b203.md", item_b203_en),
    ("item-f303.md", item_f303_en),
    ("item-t845.md", item_t845_en)
]:
    with open(os.path.join(ROOT, "src/content/products/en", fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT, "src/content/products/fr", fname), "w", encoding="utf-8") as f:
        # Use English as high-fidelity fallback until French strings are localized
        f.write(content)
print("Updated all 4 products in en and fr")

# 8. Blog posts
post_1_en = """---
title: "Building Your First Micro-SaaS: A Practical Developer Guide"
description: "From idea validation to your first paying customer — a no-nonsense roadmap to shipping focused software without burning out."
author: 'Dawda Mbowe'
role: 'Founder, KUNDA'
authorImage: '@/images/blog/jacob.avif'
authorImageAlt: 'Dawda Mbowe portrait'
pubDate: 2025-11-01
cardImage: '@/images/blog/post-1.avif'
cardImageAlt: 'Software development workspace and code editor'
readTime: 6
tags: ['microsaas', 'software', 'bootstrapping', 'architecture']
---

Building a software product today does not require venture capital, a large engineering team, or six months of architectural contemplation. The proliferation of modern edge hosting, serverless databases, and performant web frameworks like Astro makes it entirely feasible for a solo engineer to conceptualize, construct, and monetize a micro-SaaS in under four weeks.

### What Makes a Micro-SaaS Viable?

A micro-SaaS is not a miniature version of Salesforce or Jira. It is a razor-sharp software tool that executes one specific workflow exceptionally well. When evaluating potential ideas, prioritize problems that exhibit three distinct characteristics:

1. **High Discomfort:** The problem is annoying enough that people seek out solutions (e.g., chasing missing client file formats or tracking unassigned software seats).
2. **Deterministic Inputs and Outputs:** The business logic is clean and predictable, minimizing edge cases and ongoing maintenance burdens.
3. **Low Migration Friction:** Customers can adopt the product without altering their entire workflow or exporting legacy databases.

### Choosing the Right Stack

Keep operational complexity at absolute zero. When your infrastructure is serverless and bills are near zero at idle, you remove financial pressure and give your product time to find market traction.

At KUNDA, our micro-applications emphasize lightweight web standards, Cloudflare serverless backends, and client-side processing wherever possible.
"""

post_2_en = """---
title: "The Case for Client-Side Tools: Privacy, Speed, and Simplicity"
description: "Why processing sensitive payloads inside the user browser is the superior architectural model for modern developer utilities."
author: 'Dawda Mbowe'
role: 'Founder, KUNDA'
authorImage: '@/images/blog/jacob.avif'
authorImageAlt: 'Dawda Mbowe portrait'
pubDate: 2025-10-20
cardImage: '@/images/blog/post-2.avif'
cardImageAlt: 'Clean developer workspace with dual monitors'
readTime: 5
tags: ['privacy', 'architecture', 'devtools', 'security']
---

Every day, developers and creators routinely paste JSON objects containing real customer emails, unreleased schema definitions, and internal API keys into third-party web tools to format or inspect them. Similarly, millions of users evaluate passwords on third-party web pages without asking where their keystrokes travel.

This status quo is fraught with risk and completely unnecessary.

### The Power of Modern Web APIs

Modern browsers possess astonishing computing power. With native JSON serialization, the `crypto.getRandomValues()` WebCrypto API, and client-side Web Workers, virtually every utility calculation can execute directly inside the user's browser sandbox.

### Why Client-Side First Matters

1. **Absolute Data Privacy:** When zero bytes leave the browser, GDPR, CCPA, and compliance questions dissolve completely.
2. **Instant Response Times:** Eliminating network round-trips drops formatting and validation latency from 250ms to 0ms.
3. **Resilience & Scalability:** A client-side tool cannot crash under traffic surges. Every client provides its own compute.

This is the philosophy behind KUNDA Free Tools: useful digital utilities that work instantly and keep your data where it belongs.
"""

post_3_en = """---
title: "Zero-Cost SaaS Stack: Launching Under $10/Month"
description: "A curated guide to building and operating scalable web applications using modern cloud-native free tiers."
author: 'Dawda Mbowe'
role: 'Founder, KUNDA'
authorImage: '@/images/blog/jacob.avif'
authorImageAlt: 'Dawda Mbowe portrait'
pubDate: 2025-10-10
cardImage: '@/images/blog/post-3.avif'
cardImageAlt: 'Cloud infrastructure diagram on laptop screen'
readTime: 7
tags: ['saas', 'cloud', 'architecture', 'startups']
---

One of the greatest shifts in software development over the past five years is the collapse in baseline hosting costs. A decade ago, deploying a resilient, high-availability web service required multiple reserved EC2 instances, load balancers, and a managed database cluster costing hundreds of dollars every month before receiving a single visit.

Today, the modern edge stack lets you build globally distributed, enterprise-grade applications with zero upfront infrastructure cost.

### The Foundation Layers

- **Static & SSR Layer:** Astro deployed on Cloudflare Workers or Pages provides instantaneous global edge delivery with zero cold starts.
- **Data Persistence:** Serverless relational engines (like Cloudflare D1) and object storage (Cloudflare R2 or Backblaze B2) deliver generous monthly free tiers capable of serving millions of requests.
- **Authentication:** Standardized JWTs and lightweight Auth providers enable secure access without dedicated auth servers.

By keeping fixed overhead under $10 per month, builders preserve the stamina required to iterate until their product achieves authentic product-market fit.
"""

for fname, content in [
    ("post-1.md", post_1_en),
    ("post-2.md", post_2_en),
    ("post-3.md", post_3_en)
]:
    with open(os.path.join(ROOT, "src/content/blog/en", fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT, "src/content/blog/fr", fname), "w", encoding="utf-8") as f:
        f.write(content)
print("Updated all 3 blog posts in en and fr")

# 9. Insights
insight_1_en = """---
title: 'The Future of Browser-First Developer Tooling'
description: 'How client-side execution and WebAssembly are transforming how engineers interact with everyday utilities.'
cardImage: '@/images/insights/insight-1.avif'
cardImageAlt: 'Modern laptop showing software architecture diagram'
---

Developer tooling is undergoing a silent revolution. As privacy awareness intensifies and client hardware becomes increasingly capable, cloud-dependent utility platforms are being systematically replaced by browser-first architectures.

At KUNDA, our commitment is to prove that powerful digital tools do not need to hoard user telemetry or inspect private payloads to provide lasting utility.
"""

insight_2_en = """---
title: 'Micro-SaaS vs Enterprise SaaS: The Power of Focus'
description: 'Why concentrated software tools with single-problem workflows consistently outperform sprawling enterprise suites.'
cardImage: '@/images/insights/insight-2.avif'
cardImageAlt: 'Clean desktop setup with tablet and notebook'
---

Enterprise software suites often suffer from creeping feature fatigue. In their quest to satisfy every department, they accumulate layers of navigation, configuration menus, and unneeded complexity.

Micro-SaaS represents the antidote: purposeful, focused utilities engineered for swift execution and immediate return on investment.
"""

insight_3_en = """---
title: 'The Anatomy of a Truly Useful Digital Product'
description: 'Deconstructing what separates temporary software novelties from enduring daily workflow fixtures.'
cardImage: '@/images/insights/insight-3.avif'
cardImageAlt: 'Minimalist tech accessories on clean timber desk'
---

What makes a digital tool truly useful? It is rarely the quantity of features it lists on its landing page. Instead, usefulness is defined by the elimination of cognitive friction: how quickly a user can arrive, accomplish their objective, and move forward with their day.
"""

for fname, content in [
    ("insight-1.md", insight_1_en),
    ("insight-2.md", insight_2_en),
    ("insight-3.md", insight_3_en)
]:
    with open(os.path.join(ROOT, "src/content/insights/en", fname), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(ROOT, "src/content/insights/fr", fname), "w", encoding="utf-8") as f:
        f.write(content)
print("Updated all 3 insights in en and fr")
print("ALL PHASE 1 CONTENT & DATA UPDATES COMPLETED SUCCESSFULLY!")

