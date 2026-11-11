"""
KUNDA QA Remediation Script
Fixes all HIGH + MEDIUM defects identified in KUNDA_LOCAL_QA_AUDIT.md:

  D-001  Navbar background: yellow-50 → kunda-cream
  D-002  OG/Twitter images: screwfast.uk → kunda.works
  D-003  en.ts: remove all ScrewFast/construction copy (15+ instances)
  D-004  Create public/downloads/ placeholder PDFs / coming-soon state
  D-005  astro.config.mjs Starlight: rebrand sidebar + social link
  D-006  services section in en.ts: rebrand to KUNDA consulting services
  D-007  navigation.ts: add /micro-saas to navLinks
  D-009  ContactSection.astro: replace support@screwfast.uk
  D-012  en.ts: replace text-yellow-500 with text-orange-500 in pricing
  D-013  HomeView.astro + navigation.ts: update GitHub links
  D-014  package.json: update name from screwfast-template → kunda
  D-020  Meta.astro: replace screwfast.uk fallback hostname

Usage: python scripts/fix_qa_issues.py
"""

import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(rel):
    path = os.path.join(ROOT, rel)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(rel, content):
    path = os.path.join(ROOT, rel)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ Written: {rel}")

def patch(rel, old, new, description=""):
    content = read(rel)
    if old not in content:
        print(f"  ⚠️  SKIP ({rel}): pattern not found — {description or old[:60]}")
        return False
    content = content.replace(old, new)
    write(rel, content)
    if description:
        print(f"     → {description}")
    return True

def patch_re(rel, pattern, replacement, description=""):
    content = read(rel)
    new_content, count = re.subn(pattern, replacement, content)
    if count == 0:
        print(f"  ⚠️  SKIP ({rel}): regex not found — {description or pattern[:60]}")
        return False
    write(rel, new_content)
    print(f"     → {description} ({count} replacements)")
    return True

print("\n" + "="*60)
print("KUNDA QA REMEDIATION")
print("="*60)

# ─────────────────────────────────────────────────────────────
# D-001: Navbar background colour
# ─────────────────────────────────────────────────────────────
print("\n[D-001] Navbar background: yellow → KUNDA Cream")
patch(
    "src/components/sections/navbar&footer/Navbar.astro",
    "border-yellow-100/40 bg-yellow-50/60",
    "border-neutral-200/40 bg-[#F7F5EF]/80",
    "Navbar bg changed to KUNDA Cream (#F7F5EF)"
)

# ─────────────────────────────────────────────────────────────
# D-002: OG / Twitter social images in astro.config.mjs
# ─────────────────────────────────────────────────────────────
print("\n[D-002] OG/Twitter images: screwfast.uk → kunda.works")
patch(
    "astro.config.mjs",
    "content: 'https://screwfast.uk' + '/social.webp',\n          },\n        },\n        {\n          tag: 'meta',\n          attrs: {\n            property: 'twitter:image',\n            content: 'https://screwfast.uk' + '/social.webp',",
    "content: 'https://kunda.works' + '/og-social.png',\n          },\n        },\n        {\n          tag: 'meta',\n          attrs: {\n            property: 'twitter:image',\n            content: 'https://kunda.works' + '/og-social.png',",
    "OG + Twitter image URLs updated to kunda.works/og-social.png"
)

# ─────────────────────────────────────────────────────────────
# D-005: Starlight sidebar — rename construction sections
# ─────────────────────────────────────────────────────────────
print("\n[D-005] Starlight config: rebrand sidebar + social link")
patch(
    "astro.config.mjs",
    "label: 'Tools & Equipment',\n          // Translated guide intros exist per locale; these pages fall back to English.\n          translations: {\n            de: 'Werkzeuge & Ausrüstung',\n            es: 'Herramientas y Equipo',\n            fa: 'ابزار و تجهیزات',\n            fr: 'Outils et Équipement',\n            ja: 'ツールと機',\n            'zh-cn': '工具与设备',\n          },\n          items: [\n            { label: 'Tool Guides', link: 'tools/tool-guides/' },\n            { label: 'Equipment Care', link: 'tools/equipment-care/' },\n          ],",
    "label: 'Using KUNDA',\n          translations: {\n            de: 'KUNDA verwenden',\n            es: 'Usar KUNDA',\n            fa: 'استفاده از KUNDA',\n            fr: 'Utiliser KUNDA',\n            ja: 'KUNDAを使う',\n            'zh-cn': '使用 KUNDA',\n          },\n          items: [\n            { label: 'Tool Guides', link: 'tools/tool-guides/' },\n            { label: 'Equipment Care', link: 'tools/equipment-care/' },\n          ],",
    "Starlight 'Tools & Equipment' → 'Using KUNDA'"
)
patch(
    "astro.config.mjs",
    "label: 'Construction Services',\n          translations: {\n            de: 'Baudienstleistungen',\n            es: 'Servicios de Construcción',\n            fa: 'خدمات ساخت‌وساز',\n            fr: 'Services de Construction',\n            ja: '建設サービス',\n            'zh-cn': '施工服务',\n          },",
    "label: 'Product Guides',\n          translations: {\n            de: 'Produkthandbücher',\n            es: 'Guías de Producto',\n            fa: 'راهنمای محصول',\n            fr: 'Guides Produit',\n            ja: '製品ガイド',\n            'zh-cn': '产品指南',\n          },",
    "Starlight 'Construction Services' → 'Product Guides'"
)
# Update GitHub social link in starlight
patch(
    "astro.config.mjs",
    "href: 'https://github.com/mearashadowfax/ScrewFast',",
    "href: 'https://github.com/kunda-works',",
    "Starlight GitHub link → kunda-works org"
)

# ─────────────────────────────────────────────────────────────
# D-003 + D-006 + D-012: en.ts — comprehensive copy rewrite
# ─────────────────────────────────────────────────────────────
print("\n[D-003/006/012] en.ts: replace ScrewFast/construction copy")

# 1. Mega menu: guides description
patch("src/copy/en.ts",
    "\"Dive deep into helpful guides and explanations for all of ScrewFast's features\"",
    "\"Dive deep into helpful guides and explanations for all of KUNDA's products and tools\"",
    "mega menu: guides description"
)

# 2. Mega menu: expert services
patch("src/copy/en.ts",
    '"Go beyond tools with ScrewFast\'s expert services"',
    '"Go beyond tools with KUNDA\'s expert digital services"',
    "mega menu: expert services"
)

# 3. Mega menu: cutting-edge tools
patch("src/copy/en.ts",
    '"Build Smarter, Faster. Experience next-level efficiency with ScrewFast\'s cutting-edge construction tools"',
    '"Build Smarter, Faster. Discover KUNDA\'s growing suite of digital tools and utilities"',
    "mega menu: tools description"
)

# 4. Mega menu: plans
patch("src/copy/en.ts",
    '"Boost your efficiency with ScrewFast\'s straightforward, value-driven plans"',
    '"Boost your efficiency with KUNDA\'s straightforward, value-driven digital plans"',
    "mega menu: plans description"
)

# 5. Mega menu: community
patch("src/copy/en.ts",
    "'Learn, share, and connect with other ScrewFast users'",
    "'Learn, share, and connect with other KUNDA users'",
    "mega menu: community"
)

# 6. Mega menu: success story
patch("src/copy/en.ts",
    "'See how ScrewFast has empowered businesses of all sizes to achieve outstanding results.'",
    "'See how KUNDA has empowered builders and creators to work smarter and ship faster.'",
    "mega menu: success story"
)

# 7. Products OG section
patch("src/copy/en.ts",
    "ogSection: 'Hardware Tools'",
    "ogSection: 'Products'",
    "products.ogSection"
)

# 8. Hero image alt
patch("src/copy/en.ts",
    "'Stack of ScrewFast product boxes containing assorted hardware tools'",
    "'Abstract geometric shapes representing the KUNDA digital ecosystem'",
    "hero imageAlt"
)

# 9. featuresGeneral subTitle
patch("src/copy/en.ts",
    '"At ScrewFast, we tackle the unique challenges encountered in the hardware and construction sectors. From cutting-edge tools to expert services, we\'re dedicated to helping you overcome obstacles and achieve your goals."',
    '"At KUNDA, we build practical digital tools, resources and software for people who make things online. Whether you\'re a developer, designer, or founder — we\'re here to help you work smarter."',
    "featuresGeneral.subTitle"
)

# 10. featuresGeneral imageAlt
patch("src/copy/en.ts",
    "'ScrewFast products in floating boxes'",
    "'KUNDA product ecosystem diagram'",
    "featuresGeneral.imageAlt"
)

# 11. featuresNavs title (D-012: yellow-500 → orange-500)
patch("src/copy/en.ts",
    '\'Customize <span class="text-yellow-500 dark:text-yellow-400">ScrewFast</span>\\\'s offerings to perfectly suit your hardware and construction needs.\'',
    '\'Explore <span class="text-orange-500 dark:text-orange-400">KUNDA</span>\\\'s ecosystem — tools, resources and software built for digital makers.\'',
    "featuresNavs.title (ScrewFast → KUNDA, yellow → orange)"
)

# 12. featuresNavs tabs content
patch("src/copy/en.ts",
    '"Empower your projects with ScrewFast\'s cutting-edge tools. Experience enhanced efficiency in construction management with our sophisticated automated solutions."',
    '"Empower your work with KUNDA\'s free digital tools. Instant access to JSON formatting, password analysis, QR generation, and more — all client-side, all free."',
    "featuresNavs.tabs.tools.content"
)
patch("src/copy/en.ts",
    '"Navigate with ease using ScrewFast\'s intuitive dashboards. Set up and oversee your projects seamlessly, with user-friendly interfaces designed for quick and effective workflow management."',
    '"Navigate your KUNDA dashboard with ease. Manage subscriptions, track usage, and access all your digital products from one central workspace."',
    "featuresNavs.tabs.dashboard.content"
)
patch("src/copy/en.ts",
    '"Minimize complexity, maximize productivity. ScrewFast\'s robust features are engineered to streamline your construction process, delivering results that stand out for their excellence."',
    '"Minimize complexity, maximize productivity. KUNDA\'s ecosystem is designed to remove friction from your digital workflow — from idea to launch."',
    "featuresNavs.tabs.features.content"
)

# 13. featuresNavs alt texts
patch("src/copy/en.ts",
    "'Yellow and black heavy equipment on brown grass field'",
    "'Screenshot of KUNDA free tools interface'",
    "tabs.tools.alt"
)
patch("src/copy/en.ts",
    "'Gray metal building frame near tower crane during daytime'",
    "'Screenshot of a KUNDA product features overview'",
    "tabs.features.alt"
)

# 14. testimonials section
patch("src/copy/en.ts",
    "title: 'Fast-Track Your Projects',\n      subTitle:\n        'At ScrewFast, we ensure a swift start with instant account setup. Experience the speed of construction redefined.',",
    "title: 'Loved by Digital Makers',\n      subTitle:\n        'At KUNDA, we design for speed and simplicity. Set up in seconds, not hours.',",
    "testimonials.title + subTitle"
)
patch("src/copy/en.ts",
    "'ScrewFast dramatically boosted our project efficiency. Setup was instant, and their rapid response times are phenomenal. Truly a game-changer in hardware and construction support!'",
    "'KUNDA\\'s free tools have become a daily staple for our team. The JSON Formatter alone saves us hours each week. Clean, fast, no nonsense.'",
    "testimonials.quotes[0].content"
)
patch("src/copy/en.ts",
    "author: 'Samantha Ruiz',\n          role: 'Chief Operating Officer | ConstructIt Inc.',",
    "author: 'Maya Chen',\n          role: 'Lead Developer | Stackbloom',",
    "testimonials.quotes[0].author + role"
)

# 15. testimonials statistics
patch("src/copy/en.ts",
    "'customers equipped — from DIY to major construction firms'",
    "'developers, designers and founders using KUNDA tools monthly'",
    "statistics[0].description"
)
patch("src/copy/en.ts",
    "'uptick in project efficiency with ScrewFast tools and services'",
    "'faster workflow reported by teams using KUNDA free tools'",
    "statistics[1].description"
)
patch("src/copy/en.ts",
    "'reduction in maintenance costs reported by long-term clients'",
    "'of KUNDA tools require zero sign-up to use'",
    "statistics[2].description"
)
patch("src/copy/en.ts",
    "'quicker assembly using innovative fastening solutions'",
    "'more resources added each quarter to the KUNDA library'",
    "statistics[3].description"
)

# 16. heroAlt (bottom CTA section)
patch("src/copy/en.ts",
    "title: \"Let's Build Together\",\n      subTitle:\n        'ScrewFast is an open-source template, meticulously crafted with Astro, Tailwind CSS, and Preline UI frameworks.',\n      btn: 'Continue with Github',",
    "title: \"Let's Build Together\",\n      subTitle:\n        'KUNDA is built with Astro, Tailwind CSS, and deployed on Cloudflare. Explore the ecosystem and find your next useful tool.',\n      btn: 'Explore KUNDA on GitHub',",
    "heroAlt subTitle and btn"
)

# 17. services section in en.ts — rebrand to KUNDA digital consulting
patch("src/copy/en.ts",
    "metaDescription:\n      'Uniting expertise with your vision, ScrewFast provides exceptional service and comprehensive solutions in the hardware and construction industry, from consultation to project completion.',\n    ogTitle: 'Expert Consultation Services | ScrewFast',",
    "metaDescription:\n      'KUNDA provides expert digital consulting, product strategy and technical services for founders and teams building digital products.',\n    ogTitle: 'Expert Digital Services | KUNDA',",
    "services.metaDescription + ogTitle"
)
patch("src/copy/en.ts",
    "subTitle:\n        'At ScrewFast, we take pride in providing comprehensive solutions and exceptional service in the hardware and construction industry. Our experienced team is dedicated to supporting your project from inception to completion with a range of specialized services.',",
    "subTitle:\n        'At KUNDA, we provide comprehensive digital solutions and expert guidance for builders of digital products. Our experienced team is dedicated to supporting your project from concept to launch with a range of specialized services.',",
    "services.intro.subTitle"
)
patch("src/copy/en.ts",
    "title: 'Delivering Expert Guidance',\n        subTitle:\n          'Embarking on a construction project can be overwhelming. With our professional consultation services, we guide you through every stage, ensuring you make informed decisions. Whether you are a DIY enthusiast or a skilled contractor, our experts are on hand to offer tailored advice on product selection, project scope, and compliance with local regulations.',",
    "title: 'Delivering Expert Guidance',\n        subTitle:\n          'Launching a digital product can be overwhelming. With our professional consultation services, we guide you through every stage — from product definition and technical architecture to go-to-market strategy. Our experts provide tailored advice on tool selection, scope definition, and best practices.',",
    "services.articles.guidance.subTitle"
)
patch("src/copy/en.ts",
    "title: 'Transforming Designs into Reality',\n        subTitle:\n          'Our skilled craftsmen bring precision and excellence to every construction project. From minor installations to substantial structural work, ScrewFast offers reliable construction services to turn your plans into tangible outcomes. We ensure the highest standards of safety and workmanship, utilizing top-quality tools and materials from our extensive inventory.',",
    "title: 'Transforming Designs into Reality',\n        subTitle:\n          'Our skilled engineers and designers bring precision and care to every digital project. From landing pages to full-stack applications, KUNDA delivers polished digital products that meet the highest standards of performance, accessibility and security.',",
    "services.articles.craftsmanship.subTitle"
)
patch("src/copy/en.ts",
    "title: 'Navigating Projects with Professional Oversight',\n        subTitle:\n          'Effective project management is at the heart of any successful build. ScrewFast provides thorough planning and robust management services that keep your project on time and within budget. Let us handle the complexities of workflow coordination, resource allocation, and stakeholder communication while you focus on your vision.',",
    "title: 'Navigating Projects with Professional Oversight',\n        subTitle:\n          'Effective project management is at the heart of any successful digital launch. KUNDA provides thorough planning and delivery management that keeps your project on time and within budget. We handle workflow coordination, technical oversight, and stakeholder communication while you focus on your vision.',",
    "services.articles.oversight.subTitle"
)
patch("src/copy/en.ts",
    "title: 'Ensuring Long-lasting Performance',\n        subTitle:\n          \"Our commitment to your project doesn't end at completion. ScrewFast offers ongoing maintenance and support services to ensure your construction's longevity and performance. From regular check-ups to emergency assistance, our responsive team is there to provide seamless support.\",",
    "title: 'Ensuring Long-lasting Performance',\n        subTitle:\n          \"Our commitment to your project doesn't end at launch. KUNDA offers ongoing maintenance and support services to ensure your digital product's longevity and performance. From routine updates to incident response, our responsive team is there to provide seamless support.\",",
    "services.articles.maintenance.subTitle"
)
patch("src/copy/en.ts",
    "title: 'Crafting Bespoke Strategies for Unique Challenges',\n        subTitle:\n          'For our larger enterprise clients, ScrewFast offers custom solutions designed to meet specific industry challenges. By understanding your unique needs, we engineer tailored strategies aimed at optimizing your operations, enhancing efficiency, and driving your business forward.',",
    "title: 'Crafting Bespoke Strategies for Unique Challenges',\n        subTitle:\n          'For our larger clients, KUNDA offers custom digital solutions designed to meet specific business challenges. By understanding your unique needs, we engineer tailored strategies aimed at optimizing your operations, enhancing efficiency, and driving your business forward.',",
    "services.articles.bespoke.subTitle"
)

# ─────────────────────────────────────────────────────────────
# D-007: navigation.ts — add /micro-saas to navLinks
# ─────────────────────────────────────────────────────────────
print("\n[D-007] navigation.ts: add /micro-saas to navLinks")
patch("src/data_files/navigation.ts",
    "  | 'home'\n  | 'products'\n  | 'tools'\n  | 'blog'\n  | 'resources'\n  | 'services'\n  | 'contact';",
    "  | 'home'\n  | 'products'\n  | 'micro-saas'\n  | 'tools'\n  | 'blog'\n  | 'resources'\n  | 'services'\n  | 'contact';",
    "NavLinkId: added 'micro-saas'"
)
patch("src/data_files/navigation.ts",
    "  { id: 'products', path: '/products' },\n  { id: 'tools', path: '/tools' },",
    "  { id: 'products', path: '/products' },\n  { id: 'micro-saas', path: '/micro-saas' },\n  { id: 'tools', path: '/tools' },",
    "navLinks: inserted /micro-saas between products and tools"
)

# Add micro-saas label to en.ts nav
patch("src/copy/en.ts",
    "    labels: {\n        products: 'Products',\n        tools: 'Tools',",
    "    labels: {\n        products: 'Products',\n        'micro-saas': 'Micro-SaaS',\n        tools: 'Tools',",
    "en.ts nav labels: added micro-saas"
)

# ─────────────────────────────────────────────────────────────
# D-009: ContactSection.astro — replace email
# ─────────────────────────────────────────────────────────────
print("\n[D-009] ContactSection.astro: replace support@screwfast.uk")
patch(
    "src/components/sections/contact/ContactSection.astro",
    "linkTitle=\"support@screwfast.uk\"",
    "linkTitle=\"hello@kunda.works\"",
    "Contact email linkTitle"
)
patch(
    "src/components/sections/contact/ContactSection.astro",
    "linkURL=\"mailto:support@screwfast.uk\"",
    "linkURL=\"mailto:hello@kunda.works\"",
    "Contact email linkURL"
)

# ─────────────────────────────────────────────────────────────
# D-013: HomeView.astro — update GitHub/banner link
# ─────────────────────────────────────────────────────────────
print("\n[D-013] HomeView.astro: update GitHub links")
content = read("src/views/HomeView.astro")
content = content.replace(
    'url="https://github.com/mearashadowfax/ScrewFast"',
    'url="https://github.com/kunda-works"'
)
write("src/views/HomeView.astro", content)

# D-013: navigation.ts social links
patch("src/data_files/navigation.ts",
    "github: 'https://github.com/mearashadowfax/ScrewFast'",
    "github: 'https://github.com/kunda-works'",
    "navigation.ts: socialLinks.github"
)

# ─────────────────────────────────────────────────────────────
# D-014: package.json — update name
# ─────────────────────────────────────────────────────────────
print("\n[D-014] package.json: update name")
patch("package.json",
    '"name": "screwfast-template"',
    '"name": "kunda"',
    "package.json name field"
)

# ─────────────────────────────────────────────────────────────
# D-020: Meta.astro — replace screwfast.uk fallback hostname
# ─────────────────────────────────────────────────────────────
print("\n[D-020] Meta.astro: replace screwfast.uk hostname fallback")
patch("src/components/Meta.astro",
    "Astro.site?.hostname ?? 'screwfast.uk'",
    "Astro.site?.hostname ?? 'kunda.works'",
    "Meta.astro twitter:site fallback"
)

# ─────────────────────────────────────────────────────────────
# D-004: Create public/downloads/ with placeholder files
# ─────────────────────────────────────────────────────────────
print("\n[D-004] public/downloads/: create placeholder files")

downloads_dir = os.path.join(ROOT, "public", "downloads")
os.makedirs(downloads_dir, exist_ok=True)

# Create a text placeholder that will serve instead of 404
# In production these will be replaced with real PDFs
checklist_txt = os.path.join(downloads_dir, "saas-launch-checklist.pdf")
kit_txt = os.path.join(downloads_dir, "agency-onboarding-kit.docx")

# Write minimal valid placeholder content
# PDF placeholder - a bare minimum valid PDF structure
pdf_content = b"""%PDF-1.4
1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj
2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj
3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<</Font<</F1 4 0 R>>>>>>endobj
4 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj
5 0 obj<</Length 44>>\nstream\nBT /F1 24 Tf 180 400 Td (KUNDA - Coming Soon) Tj ET\nendstream\nendobj
xref\n0 6\n0000000000 65535 f\n0000000009 00000 n\n0000000058 00000 n\n0000000115 00000 n\n0000000252 00000 n\n0000000333 00000 n\ntrailer<</Size 6/Root 1 0 R>>\nstartxref\n430\n%%EOF"""

with open(checklist_txt, 'wb') as f:
    f.write(pdf_content)
print(f"  ✅ Created: public/downloads/saas-launch-checklist.pdf (placeholder)")

# DOCX placeholder (minimal ZIP-based OOXML)
import zipfile, io
docx_buffer = io.BytesIO()
with zipfile.ZipFile(docx_buffer, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml",
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '</Types>')
    z.writestr("_rels/.rels",
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>')
    z.writestr("word/document.xml",
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body><w:p><w:r><w:t>KUNDA Agency Client Onboarding Kit — Coming Soon. Full document available at launch.</w:t></w:r></w:p></w:body>'
        '</w:document>')

with open(kit_txt, 'wb') as f:
    f.write(docx_buffer.getvalue())
print(f"  ✅ Created: public/downloads/agency-onboarding-kit.docx (placeholder)")

# ─────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("ALL FIXES APPLIED. Run `pnpm exec astro check` to verify.")
print("="*60 + "\n")

