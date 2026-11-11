#!/usr/bin/env python3
"""
fix_docs.py - KUNDA docs rebranding script
Fixes: astro.config.mjs Starlight sidebar, all docs content, SiteTitle.astro
"""

import os
import re

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"
DOCS = os.path.join(ROOT, "src", "content", "docs")

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  WROTE: {os.path.relpath(path, ROOT)}")

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# ============================================================
# STEP 1: Fix astro.config.mjs Starlight sidebar
# ============================================================
print("\n=== STEP 1: astro.config.mjs Starlight sidebar fixes ===")

config_path = os.path.join(ROOT, "astro.config.mjs")
config = read(config_path)

# a) Fix "Using KUNDA" items: tools/tool-guides/ -> guides/getting-started/, tools/equipment-care/ -> guides/intro/
config = config.replace(
    "{ label: 'Tool Guides', link: 'tools/tool-guides/' },",
    "{ label: 'Getting Started', link: 'guides/getting-started/' },"
)
config = config.replace(
    "{ label: 'Equipment Care', link: 'tools/equipment-care/' },",
    "{ label: 'Introduction', link: 'guides/intro/' },"
)

# b) Fix "Product Guides" autogenerate from 'construction' -> 'guides'
config = config.replace(
    "items: [{ autogenerate: { directory: 'construction' } }],",
    "items: [{ autogenerate: { directory: 'guides' } }],"
)

# c) The "Quick Start Guides" section also uses autogenerate: guides — now "Product Guides" would be duplicate.
# Remove the entire "Quick Start Guides" section since Product Guides now covers guides/
# Find and remove Quick Start Guides block
quick_start_pattern = re.compile(
    r"\s*\{\s*\n\s*label:\s*'Quick Start Guides',.*?items:\s*\[\{[^\]]*\}\],?\s*\},",
    re.DOTALL
)
config_after = quick_start_pattern.sub("", config)

if config_after != config:
    print("  Removed duplicate 'Quick Start Guides' sidebar section")
    config = config_after
else:
    # Try a simpler approach - if Quick Start Guides still there after the product guides rename,
    # it's a duplicate: both point to 'guides'. Keep only one.
    # The pattern might vary; let's try a more targeted replacement
    print("  Quick Start Guides pattern not matched - attempting targeted removal")
    # Remove just the Quick Start Guides block
    qs_start = config.find("label: 'Quick Start Guides'")
    if qs_start != -1:
        # Find opening brace before the label
        brace_pos = config.rfind("{", 0, qs_start)
        # Find the matching closing brace
        depth = 0
        pos = brace_pos
        while pos < len(config):
            if config[pos] == "{":
                depth += 1
            elif config[pos] == "}":
                depth -= 1
                if depth == 0:
                    end_pos = pos + 1
                    # skip optional comma
                    if end_pos < len(config) and config[end_pos] == ",":
                        end_pos += 1
                    config = config[:brace_pos] + config[end_pos:]
                    print("  Removed 'Quick Start Guides' sidebar section (manual brace matching)")
                    break
            pos += 1

with open(config_path, "w", encoding="utf-8") as f:
    f.write(config)
print("  SAVED: astro.config.mjs")

# ============================================================
# STEP 2: Rewrite docs content files
# ============================================================
print("\n=== STEP 2: Rewriting docs content files ===")

# --- welcome-to-docs.mdx (English root) ---
write(os.path.join(DOCS, "welcome-to-docs.mdx"), """\
---
title: Welcome to KUNDA Docs
description: Documentation hub for the KUNDA digital ecosystem
template: splash
editUrl: false
lastUpdated: false
next: false
hero:
  title: KUNDA Documentation
  tagline: Guides, references and resources for the KUNDA ecosystem
  actions:
    - text: Get Started
      link: /guides/getting-started/
      icon: right-arrow
      variant: primary
---

import { Card, CardGrid } from '@astrojs/starlight/components';

Welcome to the KUNDA documentation hub. Find guides for free tools, product references, and ecosystem documentation.

<CardGrid stagger>

<Card title="Quick Start Guides" icon="document">
  Get up and running with KUNDA's free tools and ecosystem in minutes. Clear,
  concise guides for new and returning users alike.
</Card>

<Card title="Free Tools" icon="seti:config">
  Explore KUNDA's browser-based utilities: JSON Formatter, Password Strength
  Checker, and QR Code Generator — no account required.
</Card>

<Card title="Product Ecosystem" icon="seti:puppet">
  Browse KUNDA's growing suite of SaaS and Micro-SaaS products designed for
  indie developers, freelancers, and small teams.
</Card>

<Card title="Advanced Topics" icon="seti:terraform">
  Technical specifications, architecture decisions, and in-depth references
  for developers building on or integrating with KUNDA.
</Card>

</CardGrid>
""")

# --- guides/getting-started.mdx ---
write(os.path.join(DOCS, "guides", "getting-started.mdx"), """\
---
title: Getting Started with KUNDA
description: How to use KUNDA's free tools and explore the ecosystem
sidebar:
  label: Getting Started
  order: 1
---

import {
  Card,
  CardGrid,
  LinkCard,
  Steps,
  Aside,
} from '@astrojs/starlight/components';

Welcome to KUNDA! This guide will walk you through the ecosystem so you can get the most out of KUNDA's free tools, resources, and products from day one.

## What Is KUNDA?

KUNDA is a digital ecosystem built for indie developers, freelancers, and small teams. It combines free browser-based utilities, a curated resource library, a journal of product-building insights, and a suite of focused SaaS and Micro-SaaS products — all under one roof at [kunda.works](https://kunda.works).

## Using the Free Tools

KUNDA currently offers three free tools, each running entirely in your browser — no account, no server, no data leaving your device.

<CardGrid>
  <Card title="JSON Formatter" icon="seti:json">
    Paste any JSON and get a cleanly formatted, syntax-highlighted result. Validate structure and copy in one click.
    <LinkCard title="Open JSON Formatter" href="https://kunda.works/tools/json-formatter/" />
  </Card>
  <Card title="Password Strength Checker" icon="seti:lock">
    Evaluate password strength using the WebCrypto API — entirely client-side. Get entropy scores and improvement tips.
    <LinkCard title="Open Password Checker" href="https://kunda.works/tools/password-checker/" />
  </Card>
  <Card title="QR Code Generator" icon="seti:crystal">
    Generate QR codes for any URL or text. Download as PNG or SVG instantly.
    <LinkCard title="Open QR Generator" href="https://kunda.works/tools/qr-generator/" />
  </Card>
</CardGrid>

<Aside type="tip">
  All KUNDA tools are client-side only. Your data never leaves your browser — no telemetry, no storage, no account needed.
</Aside>

## Finding Resources

The KUNDA Resource Library is a curated collection of templates, checklists, and guides for indie product builders.

<Steps>

1. **Browse the Resource Index**
   Visit [kunda.works/resources](https://kunda.works/resources/) to find the full list of available resources.

2. **Filter by Category**
   Resources are grouped into categories: Launch, Marketing, Development, Legal, and Finance.

3. **Download or Use Directly**
   Most resources are available as Markdown, PDF, or Google Docs templates — ready to adapt to your project.

</Steps>

## Browsing Products

KUNDA's product suite is a growing collection of focused software tools.

<Steps>

1. **Visit the Products Page**
   Head to [kunda.works/products](https://kunda.works/products/) to see all current and upcoming KUNDA products.

2. **Filter by Status**
   Products are tagged by status: **Available**, **In Development**, or **Concept & Validation** — so you know what's ready to use now and what's coming.

3. **Explore Product Detail Pages**
   Each product has its own page with a description, pricing, feature list, and a waitlist or direct signup link.

</Steps>

## Next Steps

<LinkCard
  title="Introduction to KUNDA"
  description="Learn about the full KUNDA ecosystem and its six core modules."
  href="/guides/intro/"
/>

<LinkCard
  title="Product Launch Checklist"
  description="A step-by-step checklist for launching your digital product."
  href="/guides/first-project-checklist/"
/>
""")

# --- guides/intro.mdx ---
write(os.path.join(DOCS, "guides", "intro.mdx"), """\
---
title: Introduction to KUNDA
description: What KUNDA is and what it offers
sidebar:
  label: Introduction to Services
  order: 2
---

import { Tabs, TabItem } from '@astrojs/starlight/components';

KUNDA is a digital ecosystem purpose-built for indie developers, freelancers, and small product teams. Rather than a single product, KUNDA is a collection of complementary modules — each solving a specific problem that comes with building and running digital products independently.

## The Six KUNDA Modules

<Tabs>
  <TabItem label="SaaS Products">
    KUNDA's SaaS products are fully hosted, subscription-based tools targeting
    specific operational pain points. Each product is scoped narrowly enough to
    be genuinely useful without feature bloat. Examples include tools for queue
    management, file intake validation, and license waste monitoring. Products
    are designed to serve small teams and freelancers — not enterprise buyers.
  </TabItem>
  <TabItem label="Micro-SaaS">
    Micro-SaaS products in the KUNDA ecosystem are lightweight, single-purpose
    tools with a focused user base. They ship fast, iterate on real feedback,
    and are priced accessibly. The Micro-SaaS module is where KUNDA experiments
    with new product ideas before they graduate to full SaaS status or are
    retired based on traction.
  </TabItem>
  <TabItem label="Free Tools">
    KUNDA Free Tools are browser-based utilities that require no account, no
    login, and no data transmission. All processing happens client-side using
    standard Web APIs. Current tools include a JSON Formatter, Password
    Strength Checker, and QR Code Generator. These tools are KUNDA's way of
    providing immediate value to the developer community while building trust
    and audience.
  </TabItem>
  <TabItem label="Journal">
    The KUNDA Journal is a collection of essays, case studies, and commentary
    on building digital products. Topics include product strategy, pricing
    models, indie bootstrapping, tech stack choices, and the realities of
    solo/small-team product development. The journal is written from the
    perspective of someone actually building — not advising from the sidelines.
  </TabItem>
  <TabItem label="Resources">
    The KUNDA Resource Library contains practical templates, checklists, and
    guides distilled from real product-building experience. Resources cover
    the full product lifecycle: from idea validation and launch preparation to
    marketing, legal basics, and financial planning. All resources are free
    and available without an account.
  </TabItem>
  <TabItem label="Docs">
    KUNDA Docs (this site) is the technical and functional documentation hub
    for the entire KUNDA ecosystem. It covers tool usage, product references,
    API documentation (where applicable), and ecosystem-wide concepts. The
    docs are built with Astro Starlight and hosted on Cloudflare Pages.
  </TabItem>
</Tabs>

## Why KUNDA Exists

The indie product landscape is fragmented. Useful free tools are buried across dozens of sites. SaaS products are over-engineered for large teams. Resources are scattered and often outdated. KUNDA brings these together into a single, coherent ecosystem — one that grows with the builder rather than demanding they outgrow it.

## Who KUNDA Is For

- **Indie developers** looking for practical tools and honest resources
- **Freelancers** who need focused software without enterprise pricing
- **Small teams** who want SaaS products scoped to their actual workflow
- **Product builders** interested in the KUNDA journal and community

## The KUNDA Philosophy

KUNDA is built on three principles: **simplicity** (do one thing well), **privacy** (client-side first, minimal data collection), and **transparency** (open about what's built, how, and why). Every module in the ecosystem reflects these principles.
""")

# --- guides/first-project-checklist.mdx ---
write(os.path.join(DOCS, "guides", "first-project-checklist.mdx"), """\
---
title: Product Launch Checklist
description: A step-by-step checklist for launching your digital product
sidebar:
  label: Product Launch Checklist
  order: 3
---

import { Aside } from '@astrojs/starlight/components';

A practical pre-launch checklist for indie developers and small teams shipping a digital product. Use this to avoid the most common launch-day failures.

<Aside type="caution">
  Complete each section in order. Infrastructure and auth issues discovered after launch are expensive to fix under real traffic.
</Aside>

## 1. Domain & DNS

- [ ] Domain registered and confirmed in your registrar dashboard
- [ ] DNS records configured: A/CNAME pointing to your host, MX for email
- [ ] TTL set appropriately (lower TTL before launch for faster propagation control)
- [ ] `www` subdomain redirects to apex (or vice versa) — no duplicate content
- [ ] DNS propagation confirmed with [dnschecker.org](https://dnschecker.org)

## 2. SSL / TLS

- [ ] SSL certificate issued and valid (check with browser padlock or `openssl s_client`)
- [ ] HTTPS redirect enforced — HTTP requests return 301 to HTTPS
- [ ] HSTS header set (`Strict-Transport-Security: max-age=31536000`)
- [ ] Certificate auto-renewal configured (Let's Encrypt / Cloudflare)

## 3. Authentication

- [ ] Sign-up flow tested end-to-end: registration → email verification → login
- [ ] Password requirements communicated clearly to users
- [ ] Rate limiting on login endpoint (brute force protection)
- [ ] "Forgot password" flow tested
- [ ] Session expiry configured and tested
- [ ] OAuth providers (if used) tested in production environment (dev keys ≠ prod keys)

## 4. Analytics

- [ ] Analytics provider integrated (Plausible, Fathom, or similar privacy-first option)
- [ ] Key events tracked: sign-up, first action, conversion
- [ ] Dashboard access confirmed before launch
- [ ] Privacy policy updated to reflect analytics use

## 5. Error Monitoring

- [ ] Error tracking service configured (Sentry, BugSnag, or similar)
- [ ] Source maps uploaded for readable stack traces
- [ ] Alert thresholds set — you should know when errors spike
- [ ] Test error captured and visible in dashboard before launch

## 6. Email

- [ ] Transactional email provider configured (Resend, Postmark, SendGrid)
- [ ] SPF, DKIM, and DMARC DNS records set for your sending domain
- [ ] Welcome email tested end-to-end
- [ ] Password reset email tested
- [ ] Unsubscribe link present in all marketing emails (legal requirement)

## 7. Payments

- [ ] Payment provider integrated and tested in production mode
- [ ] Webhook endpoint configured and verified (Stripe/Paddle/Lemon Squeezy)
- [ ] Failed payment flow tested — what happens to the user's access?
- [ ] Refund policy documented and accessible
- [ ] Receipts/invoices sent automatically after payment

## 8. Deployment

- [ ] Environment variables set in production (not `.env` committed to repo)
- [ ] Build succeeds from clean checkout with no local artifacts
- [ ] Database migrations run successfully on production schema
- [ ] Health check endpoint returns 200 (`/health` or `/api/status`)
- [ ] Rollback plan documented — how do you revert if launch goes wrong?
- [ ] CDN/cache invalidated after deploy
- [ ] Performance baseline measured (Lighthouse, Web Vitals)

## Post-Launch

- [ ] Monitor error dashboard for first 24 hours
- [ ] Check analytics are receiving real data
- [ ] Confirm payment webhooks firing correctly
- [ ] Send launch announcement (Product Hunt, newsletter, social)
""")

# --- tools/tool-guides.mdx ---
write(os.path.join(DOCS, "tools", "tool-guides.mdx"), """\
---
title: KUNDA Free Tools Guide
description: Complete guide to KUNDA's free online utilities
---

import { Card, CardGrid, LinkCard, Aside } from '@astrojs/starlight/components';

KUNDA provides a set of free, browser-based utilities for developers and digital product builders. All tools run entirely client-side — your data never leaves your device.

<Aside type="tip">
  No account required. No data transmitted. All processing happens in your browser using standard Web APIs.
</Aside>

## Available Tools

<CardGrid>
  <Card title="JSON Formatter & Validator" icon="seti:json">
    Paste any JSON string to get a formatted, syntax-highlighted, indented result.
    Invalid JSON is caught immediately with a clear error message.

    **Features:**
    - Format and indent JSON automatically
    - Validate structure — highlights syntax errors
    - Copy formatted output with one click
    - Minify JSON for compact output

    <LinkCard title="Open JSON Formatter →" href="https://kunda.works/tools/json-formatter/" />
  </Card>

  <Card title="Password Strength Checker" icon="seti:lock">
    Evaluate the strength of any password without transmitting it. Uses entropy
    calculation and pattern analysis to give actionable feedback.

    **Features:**
    - Entropy-based strength scoring
    - Pattern detection (keyboard walks, repeated chars, common words)
    - Improvement suggestions
    - WebCrypto API — zero server contact

    <LinkCard title="Open Password Checker →" href="https://kunda.works/tools/password-checker/" />
  </Card>

  <Card title="QR Code Generator" icon="seti:crystal">
    Generate QR codes for any URL, text, email, or vCard. Download as PNG or SVG.

    **Features:**
    - Supports URLs, plain text, email addresses, phone numbers
    - Adjustable size and error correction level
    - Download as PNG or SVG
    - Works offline once the page is loaded

    <LinkCard title="Open QR Generator →" href="https://kunda.works/tools/qr-generator/" />
  </Card>
</CardGrid>

## Upcoming Tools

KUNDA's tool suite is growing. Planned additions include a Base64 encoder/decoder, a UUID generator, a colour palette extractor, and a Cron expression builder. Follow the [KUNDA Journal](https://kunda.works/blog/) for announcements.
""")

# --- tools/equipment-care.mdx ---
write(os.path.join(DOCS, "tools", "equipment-care.mdx"), """\
---
title: Tool Privacy & Security
description: How KUNDA tools protect your data
---

import { Aside } from '@astrojs/starlight/components';

KUNDA's free tools are designed with a privacy-first architecture. Here's exactly how your data is handled — and why it's safe.

## Client-Side Processing

Every KUNDA tool performs all computation directly in your browser. When you paste a JSON string, type a password, or enter text for a QR code, that data is processed by JavaScript running locally on your machine. It is never sent to a KUNDA server, logged, or stored.

This is not just a privacy policy claim — it is an architectural fact. KUNDA's tool pages have no backend API endpoints that accept user input.

## No Data Transmission

<Aside type="note">
  You can verify this yourself: open your browser's DevTools → Network tab, use a KUNDA tool, and observe that no network requests carry your input data.
</Aside>

The only network requests made by KUNDA tool pages are:
- Initial page load (HTML, CSS, JS assets from Cloudflare CDN)
- Optionally, analytics page-view events (no input data included)

Your passwords, JSON payloads, and QR content are never transmitted.

## WebCrypto API

The Password Strength Checker uses the browser's built-in [WebCrypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) for any cryptographic operations. This API is implemented natively by the browser — no third-party cryptography library with potential supply-chain risks.

## Open Source Approach

KUNDA's tools are open source. You can review the source code, audit the client-side logic, and verify that no data exfiltration occurs. The repository is available on [GitHub](https://github.com/kunda-works).

## Analytics

KUNDA uses privacy-respecting analytics (no cookies, no cross-site tracking, no personal data collection) to understand which tools are used most. Analytics events contain only:
- Page URL visited
- Referrer (if present)
- Approximate country (from IP, not stored)

No input data is ever included in analytics events.
""")

# --- advanced/technical-specifications.mdx ---
write(os.path.join(DOCS, "advanced", "technical-specifications.mdx"), """\
---
title: Technical Reference
description: Technology stack and specifications for the KUNDA platform
---

import { Aside } from '@astrojs/starlight/components';

This document describes the technology stack, architecture decisions, and deployment configuration for the KUNDA platform.

## Frontend Framework

**Astro** is the core framework powering kunda.works. KUNDA targets Astro 5+ with the Cloudflare adapter, enabling edge-rendered pages and static output.

Key Astro features used:
- **Content Collections** — type-safe Markdown/MDX content for blog, insights, and docs
- **View Transitions** — smooth page transitions with the `<ViewTransitions />` component
- **Image Optimization** — built-in `<Image />` component with Cloudflare image transformations
- **Starlight** — Astro's official documentation theme, used for this docs site

## Styling

**Tailwind CSS 4** is used for utility-first styling across all pages. KUNDA uses the Vite plugin approach (`@tailwindcss/vite`) rather than PostCSS, which provides faster HMR and better integration with Astro's build pipeline.

**Preline UI** provides accessible, unstyled component primitives (dropdowns, modals, accordions) built on top of Tailwind classes. Preline is initialized via a client-side script.

## Documentation

**Astro Starlight** powers this documentation site. Starlight features used:
- Multi-language (i18n) support with 7 locales
- Custom `SiteTitle`, `Head`, `ThemeSelect`, and `MobileMenuFooter` components
- Custom CSS via `starlight.css`
- Sidebar with autogenerated sections from content directories

## TypeScript

All KUNDA source code is written in **TypeScript**. The project uses strict mode with Astro's recommended tsconfig. Content collection schemas are defined with Zod for runtime validation.

## Deployment

KUNDA is deployed on **Cloudflare Pages** using the `@astrojs/cloudflare` adapter. This provides:
- Edge rendering via Cloudflare Workers
- Global CDN distribution
- Automatic HTTPS and DDoS protection
- Zero cold-start latency for edge functions

<Aside type="note">
  Static assets (images, fonts, downloadable files) are served from Cloudflare's CDN. Dynamic routes (server-rendered pages) execute at the edge via Workers.
</Aside>

## Build Pipeline

| Step | Tool |
|------|------|
| Package manager | pnpm |
| Build | `astro build` |
| Type check | `astro check` |
| Lint | ESLint + Prettier |
| Deploy | Cloudflare Pages CI/CD |

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `PUBLIC_SITE_URL` | Canonical site URL for OG tags and sitemaps |
| `STRIPE_SECRET_KEY` | Stripe payment integration (product pages) |
| `RESEND_API_KEY` | Transactional email via Resend |

## Performance Targets

- Lighthouse Performance: ≥ 95
- Largest Contentful Paint: < 1.5s
- Cumulative Layout Shift: < 0.05
- First Input Delay: < 50ms
""")

# --- construction/custom-solutions.mdx ---
write(os.path.join(DOCS, "construction", "custom-solutions.mdx"), """\
---
title: Custom Digital Solutions
description: Tailored digital product development for indie builders and small teams
sidebar:
  label: Custom Digital Solutions
---

KUNDA's custom solutions module helps indie developers and small teams move from idea to shipped product faster. Rather than starting from scratch, builders can leverage KUNDA's ecosystem — tools, templates, and frameworks — as the foundation for their custom digital products.

## What "Custom" Means at KUNDA

Custom solutions at KUNDA are not bespoke agency engagements. They are opinionated starting points: pre-configured tech stacks, validated architecture patterns, and reusable modules that dramatically reduce the time from idea to first user.

## Available Building Blocks

- **Astro + Cloudflare starter** — Full-stack template with auth, payments, and DB wired up
- **Micro-SaaS boilerplate** — Subscription billing, user management, and a landing page
- **Free tool template** — Client-side tool scaffold with privacy-safe architecture built in
- **Documentation starter** — Starlight-based docs site pre-configured for multi-language

## When to Use Custom vs. Off-the-Shelf

| Scenario | Recommendation |
|----------|---------------|
| Need a tool that doesn't exist in KUNDA's suite | Custom solution |
| Need a KUNDA product with minor adjustments | Contact KUNDA for roadmap input |
| Building a new Micro-SaaS from scratch | Use KUNDA Micro-SaaS boilerplate |
| Need full custom UI/UX | Custom solution with KUNDA design tokens |

## Getting Started

Explore the available templates on [GitHub](https://github.com/kunda-works) or reach out via the [KUNDA contact page](https://kunda.works/contact/) to discuss your specific requirements.
""")

# --- construction/project-planning.mdx ---
write(os.path.join(DOCS, "construction", "project-planning.mdx"), """\
---
title: Product Planning Guide
description: How to plan and scope your digital product before building
sidebar:
  label: Product Planning Guide
---

Good product planning is the difference between a product that ships and one that never does. This guide covers KUNDA's recommended approach to planning a digital product — from idea validation to scope definition.

## 1. Idea Validation

Before writing a line of code, validate that the problem is real and that people will pay (or at least use) a solution.

**Validation methods:**
- Post in relevant communities and count genuine interest signals (not "cool idea" replies)
- Run a waitlist landing page for 2–4 weeks before building
- Interview 5–10 people who match your target user profile
- Check if people are already paying for a worse solution

**Red flags:**
- Only you and your friends think it's a good idea
- The "market" is a single company you're hoping will buy it
- The problem only exists in edge cases

## 2. Scope Definition

Scope creep kills indie products. Define your MVP with brutal honesty.

**MVP rule:** If a user can get value without it, it's not in the MVP.

Write a one-paragraph description of what your product does for who, in what situation, and why they'd pay for it over alternatives. If you can't write that paragraph clearly, your scope isn't defined yet.

## 3. Technical Planning

Choose your stack based on what you can ship fastest, not what's most impressive.

| Decision | KUNDA Default |
|----------|--------------|
| Framework | Astro (static) or Next.js (dynamic) |
| Database | Cloudflare D1 (SQLite at edge) |
| Auth | Better Auth or Lucia |
| Payments | Stripe or Lemon Squeezy |
| Email | Resend |
| Deployment | Cloudflare Pages |

## 4. Launch Planning

Set a launch date before you start building. Work backwards from it. Cut scope to meet the date — never extend the date to fit the scope.

See the [Product Launch Checklist](/guides/first-project-checklist/) for a comprehensive pre-launch checklist.
""")

# --- construction/safety.mdx ---
write(os.path.join(DOCS, "construction", "safety.mdx"), """\
---
title: Security & Privacy Guide
description: Security and privacy best practices for KUNDA products and ecosystem
sidebar:
  label: Security & Privacy Guide
---

import { Aside } from '@astrojs/starlight/components';

Security and privacy are not afterthoughts in the KUNDA ecosystem — they are design requirements. This guide covers KUNDA's security model and privacy practices.

## KUNDA's Security Model

### Client-Side First

Where computation can happen in the browser, it does. This eliminates an entire class of server-side vulnerabilities and means user data never reaches KUNDA's infrastructure. All free tools follow this model.

### Minimal Data Collection

KUNDA collects the minimum data required to operate each product:
- **Free tools**: No data collected. No account required.
- **SaaS products**: Email (for auth), billing info (via Stripe — not stored by KUNDA), and usage metrics (anonymised).
- **Analytics**: Page views only, no personal identifiers, no cross-site tracking.

### Authentication Security

KUNDA products that require accounts implement:
- Password hashing with bcrypt (cost factor ≥ 12)
- Rate limiting on authentication endpoints
- CSRF protection on form submissions
- Secure, HttpOnly, SameSite cookies
- Email verification before account activation

## Privacy Practices

<Aside type="note">
  KUNDA does not sell user data. Period.
</Aside>

### What KUNDA Collects

| Data Type | Collected? | Purpose |
|-----------|-----------|---------|
| Input data (tools) | ❌ No | N/A — client-side only |
| Email address | ✅ Auth products only | Account login |
| Payment data | Via Stripe only | Billing (not stored by KUNDA) |
| IP address | Briefly (Cloudflare) | DDoS protection, rate limiting |
| Page views | ✅ Anonymised | Usage analytics |

### Data Retention

User account data is deleted within 30 days of account closure. Anonymised analytics data is retained for up to 24 months.

## Reporting a Vulnerability

If you discover a security vulnerability in any KUNDA product, please report it responsibly via email to security@kunda.works. Do not disclose publicly until a fix is released.
""")

# --- construction/service-overview.mdx ---
write(os.path.join(DOCS, "construction", "service-overview.mdx"), """\
---
title: KUNDA Services Overview
description: A complete overview of products and services available in the KUNDA ecosystem
sidebar:
  label: KUNDA Services Overview
---

import { Card, CardGrid } from '@astrojs/starlight/components';

KUNDA is a digital ecosystem offering a range of services, tools, and products for indie developers, freelancers, and small teams. This page provides a complete overview of everything available under the KUNDA umbrella.

## Free Services

<CardGrid>
  <Card title="JSON Formatter" icon="seti:json">
    Browser-based JSON formatting and validation. No account required.
  </Card>
  <Card title="Password Checker" icon="seti:lock">
    Client-side password strength analysis using WebCrypto API.
  </Card>
  <Card title="QR Generator" icon="seti:crystal">
    Generate QR codes for any URL or text. Download as PNG or SVG.
  </Card>
  <Card title="Resource Library" icon="document">
    Templates, checklists, and guides for indie product builders. Free to download.
  </Card>
</CardGrid>

## SaaS Products

| Product | Category | Status | Pricing |
|---------|----------|--------|---------|
| QueuePass | Productivity & Operations | In Development | $29/mo |
| AssetSnag | Agency Productivity | Concept & Validation | $39/mo |
| SeatSentry | IT & Cloud Governance | In Development | $49/mo |

## Content & Community

- **KUNDA Journal** — Essays and case studies on building digital products
- **KUNDA Docs** — Technical documentation for the ecosystem (this site)

## Ecosystem Principles

All KUNDA services are built around three principles:
1. **Simplicity** — Do one thing well. No feature bloat.
2. **Privacy** — Client-side first. Minimal data collection.
3. **Transparency** — Open about what's built, how, and why.

For product-specific documentation, use the sidebar navigation. For questions not covered here, visit [kunda.works/contact](https://kunda.works/contact/).
""")

# ============================================================
# Multilingual docs
# ============================================================
print("\n=== Multilingual docs ===")

LANG_CONFIGS = {
    "de": {
        "name": "Deutsch",
        "welcome_title": "Willkommen bei KUNDA Docs",
        "welcome_desc": "Dokumentations-Hub für das KUNDA-Ökosystem",
        "welcome_body": "Willkommen im KUNDA-Dokumentations-Hub. Hier finden Sie Leitfäden für kostenlose Tools, Produktreferenzen und Ökosystem-Dokumentation.",
        "see_english": "Zur englischen Dokumentation",
        "intro_title": "Einführung in KUNDA",
        "intro_body": "KUNDA ist ein digitales Ökosystem für Indie-Entwickler, Freelancer und kleine Teams. Es umfasst sechs Module: SaaS-Produkte, Micro-SaaS, kostenlose Tools, ein Journal, eine Ressourcenbibliothek und diese Dokumentation. Weitere Informationen finden Sie in der englischen Dokumentation.",
        "gs_title": "Erste Schritte mit KUNDA",
        "gs_body": "Entdecken Sie KUNDAs kostenlose Tools (JSON-Formatierer, Passwort-Checker, QR-Generator), die Ressourcenbibliothek und die Produktsuite. Alle Tools laufen direkt im Browser — kein Konto erforderlich.",
        "checklist_title": "Produkt-Launch-Checkliste",
        "checklist_body": "Eine praktische Schritt-für-Schritt-Checkliste für den Launch Ihres digitalen Produkts. Behandelt: Domain/DNS, SSL, Authentifizierung, Analytik, Fehlerverfolgung, E-Mail, Zahlungen und Deployment.",
    },
    "es": {
        "name": "Español",
        "welcome_title": "Bienvenido a KUNDA Docs",
        "welcome_desc": "Centro de documentación para el ecosistema digital KUNDA",
        "welcome_body": "Bienvenido al centro de documentación de KUNDA. Encuentra guías para herramientas gratuitas, referencias de productos y documentación del ecosistema.",
        "see_english": "Ver documentación en inglés",
        "intro_title": "Introducción a KUNDA",
        "intro_body": "KUNDA es un ecosistema digital para desarrolladores independientes, freelancers y pequeños equipos. Comprende seis módulos: productos SaaS, Micro-SaaS, herramientas gratuitas, un journal, una biblioteca de recursos y esta documentación. Consulte la documentación en inglés para más detalles.",
        "gs_title": "Comenzando con KUNDA",
        "gs_body": "Explora las herramientas gratuitas de KUNDA (formateador JSON, verificador de contraseñas, generador de QR), la biblioteca de recursos y la suite de productos. Todas las herramientas funcionan directamente en el navegador — sin cuenta necesaria.",
        "checklist_title": "Lista de verificación para el lanzamiento",
        "checklist_body": "Una lista de verificación paso a paso para lanzar tu producto digital. Cubre: dominio/DNS, SSL, autenticación, analíticas, monitoreo de errores, email, pagos y despliegue.",
    },
    "fr": {
        "name": "Français",
        "welcome_title": "Bienvenue dans KUNDA Docs",
        "welcome_desc": "Centre de documentation pour l'écosystème numérique KUNDA",
        "welcome_body": "Bienvenue dans le centre de documentation KUNDA. Trouvez des guides pour les outils gratuits, des références produits et la documentation de l'écosystème.",
        "see_english": "Voir la documentation en anglais",
        "intro_title": "Introduction à KUNDA",
        "intro_body": "KUNDA est un écosystème numérique pour les développeurs indépendants, les freelances et les petites équipes. Il comprend six modules : produits SaaS, Micro-SaaS, outils gratuits, un journal, une bibliothèque de ressources et cette documentation. Consultez la documentation anglaise pour plus de détails.",
        "gs_title": "Débuter avec KUNDA",
        "gs_body": "Découvrez les outils gratuits de KUNDA (formateur JSON, vérificateur de mot de passe, générateur QR), la bibliothèque de ressources et la suite de produits. Tous les outils fonctionnent directement dans le navigateur — aucun compte requis.",
        "checklist_title": "Liste de contrôle pour le lancement",
        "checklist_body": "Une liste de contrôle étape par étape pour lancer votre produit numérique. Couvre : domaine/DNS, SSL, authentification, analytics, suivi des erreurs, email, paiements et déploiement.",
    },
    "ja": {
        "name": "日本語",
        "welcome_title": "KUNDA Docsへようこそ",
        "welcome_desc": "KUNDAデジタルエコシステムのドキュメントハブ",
        "welcome_body": "KUNDAドキュメントハブへようこそ。無料ツールのガイド、製品リファレンス、エコシステムドキュメントをご覧ください。",
        "see_english": "英語のドキュメントを見る",
        "intro_title": "KUNDAの概要",
        "intro_body": "KUNDAは、個人開発者、フリーランサー、小規模チーム向けのデジタルエコシステムです。6つのモジュールで構成されています：SaaS製品、Micro-SaaS、無料ツール、ジャーナル、リソースライブラリ、このドキュメント。詳細は英語ドキュメントをご参照ください。",
        "gs_title": "KUNDAを始める",
        "gs_body": "KUNDAの無料ツール（JSONフォーマッター、パスワードチェッカー、QRコードジェネレーター）、リソースライブラリ、製品スイートを探索してください。すべてのツールはブラウザ上で直接動作します—アカウント不要。",
        "checklist_title": "製品ローンチチェックリスト",
        "checklist_body": "デジタル製品をローンチするためのステップバイステップチェックリスト。ドメイン/DNS、SSL、認証、分析、エラーモニタリング、メール、決済、デプロイをカバー。",
    },
    "fa": {
        "name": "فارسی",
        "welcome_title": "به KUNDA Docs خوش آمدید",
        "welcome_desc": "مرکز مستندات اکوسیستم دیجیتال KUNDA",
        "welcome_body": "به مرکز مستندات KUNDA خوش آمدید. راهنماهای ابزارهای رایگان، مراجع محصول و مستندات اکوسیستم را پیدا کنید.",
        "see_english": "مشاهده مستندات انگلیسی",
        "intro_title": "معرفی KUNDA",
        "intro_body": "KUNDA یک اکوسیستم دیجیتال برای توسعه‌دهندگان مستقل، فریلنسرها و تیم‌های کوچک است. شش ماژول دارد: محصولات SaaS، Micro-SaaS، ابزارهای رایگان، مجله، کتابخانه منابع و این مستندات. برای جزئیات بیشتر به مستندات انگلیسی مراجعه کنید.",
        "gs_title": "شروع با KUNDA",
        "gs_body": "ابزارهای رایگان KUNDA (فرمت‌کننده JSON، بررسی‌کننده رمز عبور، مولد QR)، کتابخانه منابع و مجموعه محصولات را کاوش کنید. همه ابزارها مستقیماً در مرورگر کار می‌کنند — بدون نیاز به حساب کاربری.",
        "checklist_title": "چک‌لیست راه‌اندازی محصول",
        "checklist_body": "یک چک‌لیست گام به گام برای راه‌اندازی محصول دیجیتال شما. شامل: دامنه/DNS، SSL، احراز هویت، تحلیل‌ها، نظارت بر خطاها، ایمیل، پرداخت‌ها و استقرار.",
    },
    "zh-cn": {
        "name": "简体中文",
        "welcome_title": "欢迎来到 KUNDA Docs",
        "welcome_desc": "KUNDA 数字生态系统文档中心",
        "welcome_body": "欢迎来到 KUNDA 文档中心。在这里查找免费工具指南、产品参考文档和生态系统文档。",
        "see_english": "查看英文文档",
        "intro_title": "KUNDA 简介",
        "intro_body": "KUNDA 是面向独立开发者、自由职业者和小团队的数字生态系统。包含六个模块：SaaS 产品、Micro-SaaS、免费工具、日志、资源库和本文档。详细信息请参阅英文文档。",
        "gs_title": "开始使用 KUNDA",
        "gs_body": "探索 KUNDA 的免费工具（JSON 格式化器、密码强度检查器、QR 码生成器）、资源库和产品套件。所有工具均在浏览器中直接运行——无需账户。",
        "checklist_title": "产品发布清单",
        "checklist_body": "发布数字产品的逐步清单。涵盖：域名/DNS、SSL、身份验证、分析、错误监控、电子邮件、支付和部署。",
    },
}

for lang, cfg in LANG_CONFIGS.items():
    lang_docs = os.path.join(DOCS, lang)
    guides_dir = os.path.join(lang_docs, "guides")

    # welcome-to-docs.mdx
    write(os.path.join(lang_docs, "welcome-to-docs.mdx"), f"""\
---
title: {cfg['welcome_title']}
description: {cfg['welcome_desc']}
template: splash
editUrl: false
lastUpdated: false
next: false
hero:
  title: KUNDA Documentation
  tagline: {cfg['welcome_desc']}
  actions:
    - text: Get Started
      link: /guides/getting-started/
      icon: right-arrow
      variant: primary
---

{cfg['welcome_body']}

[{cfg['see_english']}](/welcome-to-docs/)
""")

    # guides/intro.mdx
    write(os.path.join(guides_dir, "intro.mdx"), f"""\
---
title: {cfg['intro_title']}
description: {cfg['intro_title']}
sidebar:
  label: {cfg['intro_title']}
  order: 2
---

{cfg['intro_body']}

[{cfg['see_english']}](/guides/intro/)
""")

    # guides/getting-started.mdx
    write(os.path.join(guides_dir, "getting-started.mdx"), f"""\
---
title: {cfg['gs_title']}
description: {cfg['gs_title']}
sidebar:
  label: {cfg['gs_title']}
  order: 1
---

{cfg['gs_body']}

[{cfg['see_english']}](/guides/getting-started/)
""")

    # guides/first-project-checklist.mdx
    write(os.path.join(guides_dir, "first-project-checklist.mdx"), f"""\
---
title: {cfg['checklist_title']}
description: {cfg['checklist_title']}
sidebar:
  label: {cfg['checklist_title']}
  order: 3
---

{cfg['checklist_body']}

[{cfg['see_english']}](/guides/first-project-checklist/)
""")

# ============================================================
# STEP 3: Fix SiteTitle.astro ScrewFast references
# ============================================================
print("\n=== STEP 3: Fix SiteTitle.astro ===")

site_title_path = os.path.join(ROOT, "src", "components", "ui", "starlight", "SiteTitle.astro")
site_title = read(site_title_path)

original = site_title
site_title = site_title.replace('aria-label="ScrewFast"', 'aria-label="KUNDA"')
site_title = site_title.replace('aria-label="ScrewFast Docs"', 'aria-label="KUNDA Docs"')

if site_title != original:
    with open(site_title_path, "w", encoding="utf-8") as f:
        f.write(site_title)
    print("  Fixed SiteTitle.astro aria-labels: ScrewFast → KUNDA")
else:
    print("  SiteTitle.astro had no ScrewFast references to fix")

print("\n=== All file writes complete. ===")
print("Run astro check and pnpm build to validate.")
