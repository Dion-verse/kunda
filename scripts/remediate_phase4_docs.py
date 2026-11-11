# -*- coding: utf-8 -*-
"""
Remediation script for Phase 4: Starlight documentation & navigation.
Transforms docs from ScrewFast construction manuals to KUNDA technical knowledge hub.
"""

import os
import glob

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update SiteTitle.astro to render KUNDA wordmark and docs label cleanly
site_title_astro = """---
import BrandLogo from '@components/BrandLogo.astro';
import type { Props } from '@astrojs/starlight/props';

const main = '/';
const locale = Astro.props.locale ? Astro.props.locale + '/' : '';
const docs = '/' + locale + 'welcome-to-docs/';
---

<span class="site-title flex items-center gap-3">
  <a class="main-logo flex items-center" href={main} aria-label="KUNDA Home">
    <BrandLogo class="h-auto w-24" />
  </a>
  <span class="text-neutral-400 font-light">/</span>
  <a class="docs-label text-sm font-bold tracking-wider text-orange-600 dark:text-orange-400 uppercase" href={docs}>
    Docs
  </a>
</span>

<style>
  .site-title {
    gap: 0.75rem;
    margin-right: 1rem;
    display: flex;
    align-items: center;
  }
  .site-title a {
    display: flex;
  }
</style>
"""
with open(os.path.join(ROOT, "src/components/ui/starlight/SiteTitle.astro"), "w", encoding="utf-8") as f:
    f.write(site_title_astro)
print("Updated SiteTitle.astro")

# 2. Update welcome-to-docs.mdx (English)
welcome_docs_en = """---
title: KUNDA Docs
head:
  - tag: title
    content: KUNDA Documentation Hub
description: Guides, technical specifications, and reference architecture for KUNDA software, micro-SaaS, and online tools.
template: splash
editUrl: false
lastUpdated: false
next: false
hero:
  title: KUNDA Documentation Hub
  tagline: Your central reference for digital products, client-side tools, and developer guides.
  actions:
    - text: Get Started
      icon: right-arrow
      variant: primary
      link: /guides/getting-started/
    - text: Explore Free Tools
      icon: external
      variant: minimal
      link: /tools/
---

import '@styles/starlight_main.css';
import { Card, CardGrid } from '@astrojs/starlight/components';

<CardGrid stagger>

<Card title="Quick Start Guides" icon="document">
  Step-by-step walkthroughs to quickly understand the KUNDA ecosystem and integrate its utilities into your product workflow.
</Card>

<Card title="Free Online Tools" icon="seti:eslint">
  Comprehensive guides and privacy architecture for the JSON Formatter, Password Entropy Analyzer, and QR Code Generator.
</Card>

<Card title="Micro-SaaS Blueprints" icon="seti:puppet">
  Architecture documentation, API specifications, and operational roadmaps for QueuePass, AssetSnag, and SeatSentry.
</Card>

<Card title="Architecture & Specs" icon="seti:terraform">
  Technical specifications covering Astro edge rendering, WebCrypto implementation, and serverless edge deployment.
</Card>
</CardGrid>
"""
with open(os.path.join(ROOT, "src/content/docs/welcome-to-docs.mdx"), "w", encoding="utf-8") as f:
    f.write(welcome_docs_en)
print("Updated welcome-to-docs.mdx")

# 3. Update guides/intro.mdx
intro_mdx = """---
title: Introduction to KUNDA
description: What KUNDA is, how it is organized, and our digital ecosystem philosophy.
---

KUNDA is an independent digital ecosystem engineered to produce focused software applications, practical online utilities, and actionable developer knowledge.

### The Problem We Solve

The modern internet is saturated with bloated, opaque enterprise software and utility websites riddled with intrusive advertisements, tracking scripts, and heavy server latency. 

KUNDA provides an authentic alternative:
- **Zero unnecessary compute:** Client-side execution where possible.
- **Privacy by default:** Sensitive payloads remain strictly on your machine.
- **Focused functionality:** Micro-applications that solve one problem with extreme elegance.

### The Six Ecosystem Pillars

1. **Software Products:** Core SaaS applications built for longevity and reliability.
2. **Micro-SaaS:** Lean, specialized tools engineered for specific business bottlenecks.
3. **Free Tools:** Instant web utilities with zero accounts, zero tracking, and zero cost.
4. **Journal & Insights:** Thoughtful technical essays on architecture, privacy, and bootstrapping.
5. **Resource Library:** Production checklists and client intake frameworks.
6. **Documentation:** Transparent technical guides covering every tool and platform feature.
"""
with open(os.path.join(ROOT, "src/content/docs/guides/intro.mdx"), "w", encoding="utf-8") as f:
    f.write(intro_mdx)
print("Updated guides/intro.mdx")

# 4. Update guides/getting-started.mdx
getting_started_mdx = """---
title: Getting Started with KUNDA
description: How to use the free tools, access resources, and navigate the KUNDA ecosystem.
---

Getting started with KUNDA requires zero setup, zero credit cards, and zero onboarding calls.

### Accessing Free Utilities

All KUNDA free tools run directly in modern web browsers:
- **JSON Formatter & Validator:** Paste, validate, and beautify arbitrary JSON payloads with instantaneous client-side syntax checking.
- **Password Strength Analyzer:** Calculate NIST-compliant cryptographic entropy and estimate brute-force cracking resistance using native WebCrypto RNG.
- **QR Code Generator:** Generate scalable QR code matrixes for website links, contact cards, and Wi-Fi configurations.

### Accessing Curated Resources

Navigate to the **Resources** section to access production launch checklists and agency onboarding packages. All public community downloads are provided free in universal formats (PDF, DOCX).
"""
with open(os.path.join(ROOT, "src/content/docs/guides/getting-started.mdx"), "w", encoding="utf-8") as f:
    f.write(getting_started_mdx)
print("Updated guides/getting-started.mdx")

# 5. Update guides/first-project-checklist.mdx
first_project_checklist_mdx = """---
title: Digital Product Launch Checklist
description: Comprehensive pre-flight launch verification for modern web products.
---

Before opening your digital product or micro-SaaS to public users, execute this production readiness audit:

### Infrastructure & DNS
- [ ] Root domain and `www` CNAME records configured with DNSSEC enabled.
- [ ] Automated SSL/TLS certificates active with HSTS preloaded.
- [ ] Edge caching rules established for static asset delivery.

### Security & Privacy
- [ ] Content Security Policy (CSP) headers restricting unauthorized script injection.
- [ ] All sensitive cryptographic calculations utilizing `window.crypto.getRandomValues()`.
- [ ] Zero telemetry or tracking cookies active without user consent.

### Operational Resilience
- [ ] Global 404 and exception boundary pages configured.
- [ ] Automated weekly database backup verification routine active.
"""
with open(os.path.join(ROOT, "src/content/docs/guides/first-project-checklist.mdx"), "w", encoding="utf-8") as f:
    f.write(first_project_checklist_mdx)
print("Updated guides/first-project-checklist.mdx")

# 6. Update tools/tool-guides.mdx
tool_guides_mdx = """---
title: Free Online Tools Guide
description: Complete user and developer documentation for KUNDA free browser utilities.
---

KUNDA Free Tools are purpose-built utilities that solve common developer tasks without latency or privacy compromises.

### JSON Formatter & Validator (`/tools/json-formatter`)
- Validates RFC 8259 compliant JSON data structures.
- Detects line and column syntax errors with descriptive error reporting.
- Offers 2-space indentation, 4-space indentation, and compact minification.
- Never sends your JSON input over the network.

### Password Strength & Entropy Analyzer (`/tools/password-checker`)
- Computes character set pool size ($R$) and length ($L$) to calculate entropy: $E = L \times \log_2(R)$.
- Estimates cracking resistance across offline brute-force attack scenarios.
- Integrates a cryptographically strong pseudo-random generator powered by WebCrypto.

### Instant QR Code Generator (`/tools/qr-generator`)
- Encodes URLs, plain text, and contact information into standard matrix codes.
- Supports high-resolution PNG image downloads.
"""
with open(os.path.join(ROOT, "src/content/docs/tools/tool-guides.mdx"), "w", encoding="utf-8") as f:
    f.write(tool_guides_mdx)
print("Updated tools/tool-guides.mdx")

# 7. Update tools/equipment-care.mdx
equipment_care_mdx = """---
title: Tool Privacy & Security Architecture
description: How KUNDA ensures zero network transmission and client-side isolation for browser utilities.
---

When handling confidential JSON payloads, API secrets, or passwords, trust is not an assumption—it is an architectural guarantee.

### Client-Side Sandbox Model

1. **No Backend Persistence:** The web pages hosting our tools contain zero tracking webhooks, zero telemetry logging, and zero server-side storage endpoints.
2. **Local Storage Ephemerality:** All input fields are transient and cleared upon window close or explicit user reset.
3. **Open-Source Auditing:** The full implementation source is auditable in our public code repositories.
"""
with open(os.path.join(ROOT, "src/content/docs/tools/equipment-care.mdx"), "w", encoding="utf-8") as f:
    f.write(equipment_care_mdx)
print("Updated tools/equipment-care.mdx")

# 8. Update advanced/technical-specifications.mdx
tech_specs_mdx = """---
title: KUNDA Platform Technical Specifications
description: Technical architecture, framework choices, and performance specifications.
---

The KUNDA web ecosystem is built on a high-efficiency static and edge runtime stack designed for global sub-50ms latency.

### Core Architecture
- **Framework:** Astro 5 / 7 (Content Collections, Starlight integration, zero client JS by default)
- **Styling:** Tailwind CSS v4 with OKLCH color spaces and custom KUNDA design tokens
- **UI System:** Preline UI component conventions with full keyboard navigation and light/dark theme persistence
- **Global Edge Delivery:** Static pre-rendering with Cloudflare Edge compatibility
"""
with open(os.path.join(ROOT, "src/content/docs/advanced/technical-specifications.mdx"), "w", encoding="utf-8") as f:
    f.write(tech_specs_mdx)
print("Updated advanced/technical-specifications.mdx")

# 9. Update construction/*.mdx docs files to KUNDA digital services docs
construction_files = {
    "custom-solutions.mdx": """---
title: Custom Digital Solutions
description: Bespoke web tools, automated pipelines, and workflow software built by Kunda Works.
---

When off-the-shelf software falls short, KUNDA partners with growing teams to engineer purpose-built internal utilities and customer-facing web applications.
""",
    "project-planning.mdx": """---
title: Digital Product Planning Guide
description: Architectural planning, roadmap scoping, and technical execution strategies.
---

Every successful software product begins with rigorous scoping: identifying non-negotiable user workflows and eliminating architectural debt before writing code.
""",
    "safety.mdx": """---
title: Security, Privacy & Compliance
description: Our standards for data isolation, secret management, and user confidentiality.
---

Security is embedded into every layer of the KUNDA ecosystem: from client-side zero-knowledge utilities to secure serverless API boundaries.
""",
    "service-overview.mdx": """---
title: KUNDA Digital Services Overview
description: Overview of specialized digital engineering, tool development, and consulting capabilities.
---

KUNDA provides specialized technical consulting in web performance optimization, serverless edge architecture, and automated developer tooling.
"""
}

for fname, content in construction_files.items():
    with open(os.path.join(ROOT, "src/content/docs/construction", fname), "w", encoding="utf-8") as f:
        f.write(content)
print("Updated all 4 construction doc files to KUNDA equivalents")

# 10. Update multilingual welcome-to-docs.mdx files
for loc in ['de', 'es', 'fa', 'fr', 'ja', 'zh-cn']:
    loc_welcome = f"""---
title: KUNDA Docs ({loc.upper()})
description: KUNDA Documentation Hub
template: splash
hero:
  title: KUNDA Docs
  tagline: Documentation hub for KUNDA software, tools, and digital resources.
  actions:
    - text: English Documentation
      icon: right-arrow
      variant: primary
      link: /welcome-to-docs/
---

Welcome to KUNDA Docs. For comprehensive reference documentation, please visit our [English documentation hub](/welcome-to-docs/).
"""
    fpath = os.path.join(ROOT, f"src/content/docs/{loc}/welcome-to-docs.mdx")
    if os.path.exists(fpath):
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(loc_welcome)
print("Updated multilingual welcome docs")
print("PHASE 4 COMPLETED SUCCESSFULLY!")

