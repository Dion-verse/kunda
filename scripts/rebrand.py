import os
import re

KUNDA_DIR = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update src/data_files/constants.ts
constants_path = os.path.join(KUNDA_DIR, "src", "data_files", "constants.ts")
with open(constants_path, "r", encoding="utf-8") as f:
    constants_content = f.read()

constants_content = constants_content.replace(
    "title: 'ScrewFast',", "title: 'KUNDA',"
).replace(
    "tagline: 'Top-quality Hardware Tools',",
    "tagline: 'A home for useful digital things',",
).replace(
    "ScrewFast offers top-tier hardware tools and expert construction services to meet all your project needs. Start exploring and contact our sales team for superior quality and reliability.",
    "Kunda brings useful digital products and ideas together in one connected ecosystem: software applications, practical online tools, learning resources, and guides. One home. Many useful possibilities.",
).replace(
    "ScrewFast offers top-tier hardware tools and expert construction services to meet all your project needs.",
    "A home for useful digital things. Software, tools, knowledge, and digital resources.",
).replace(
    "url: 'https://screwfast.uk',", "url: 'https://kunda.works',"
).replace(
    "author: 'Emil Gulamov',", "author: 'Kunda Works',"
)

with open(constants_path, "w", encoding="utf-8") as f:
    f.write(constants_content)

print("[OK] constants.ts updated")

# 2. Update src/components/BrandLogo.astro
brand_logo_path = os.path.join(KUNDA_DIR, "src", "components", "BrandLogo.astro")
brand_logo_content = """---
interface Props {
  class?: string;
  showWordmark?: boolean;
}

const { class: className = 'h-auto w-28', showWordmark = true } = Astro.props;
---

<svg
  {...Astro.props}
  class={className}
  viewBox={showWordmark ? "0 0 340 100" : "0 0 100 100"}
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  aria-label="KUNDA Logo"
>
  <!-- KUNDA Compound Symbol -->
  <g id="kunda-symbol">
    <!-- Top-Left Quadrant: Deep Ink -->
    <path
      d="M10 44L44 44L44 28L28 10C16 10 10 20 10 44Z"
      fill="#202723"
      class="fill-[#202723] dark:fill-neutral-200"
    />
    <!-- Top-Right Quadrant: Burnt Orange -->
    <path
      d="M90 44L56 44L56 28L72 10C84 10 90 20 90 44Z"
      fill="#E56D43"
    />
    <!-- Bottom-Left Quadrant: Sage -->
    <path
      d="M10 54L44 54L44 90L26 90C14 90 10 84 10 54Z"
      fill="#9AA795"
    />
    <!-- Bottom-Right Quadrant: Stone -->
    <path
      d="M90 54L56 54L56 90L74 90C86 90 90 84 90 54Z"
      fill="#E9E5DC"
      class="fill-[#E9E5DC] dark:fill-neutral-400"
    />
  </g>

  {showWordmark && (
    <!-- KUNDA Wordmark -->
    <g id="kunda-wordmark">
      <text
        x="115"
        y="68"
        font-family="'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-weight="900"
        font-size="54"
        letter-spacing="0.05em"
        class="fill-[#202723] dark:fill-neutral-50"
      >
        KUNDA
      </text>
    </g>
  )}
</svg>
"""
with open(brand_logo_path, "w", encoding="utf-8") as f:
    f.write(brand_logo_content)

print("[OK] BrandLogo.astro updated")

# 3. Update src/assets/styles/global.css to add Plus Jakarta Sans and KUNDA colors
global_css_path = os.path.join(KUNDA_DIR, "src", "assets", "styles", "global.css")
with open(global_css_path, "r", encoding="utf-8") as f:
    global_css = f.read()

kunda_theme_tokens = """  /* KUNDA Brand Tokens */
  --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --color-kunda-ink: #202723;
  --color-kunda-orange: #E56D43;
  --color-kunda-orange-dark: #B94F2F;
  --color-kunda-sage: #9AA795;
  --color-kunda-stone: #E9E5DC;
  --color-kunda-cream: #F7F5EF;
"""

if "--color-kunda-ink" not in global_css:
    global_css = global_css.replace("@theme {", f"@theme {{\n{kunda_theme_tokens}")
    with open(global_css_path, "w", encoding="utf-8") as f:
        f.write(global_css)
    print("[OK] global.css updated with KUNDA tokens")

# 4. Add Plus Jakarta Sans font in Meta.astro
meta_path = os.path.join(KUNDA_DIR, "src", "components", "Meta.astro")
with open(meta_path, "r", encoding="utf-8") as f:
    meta_content = f.read()

font_links = """{/* Plus Jakarta Sans Typography for KUNDA */}
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap"
  rel="stylesheet"
/>
"""

if "Plus+Jakarta+Sans" not in meta_content:
    meta_content = meta_content.replace("<title>{metadata.title}</title>", f"{font_links}\n<title>{{metadata.title}}</title>")
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(meta_content)
    print("[OK] Meta.astro updated with Plus Jakarta Sans")

# 5. Update Navbar brand aria-label
navbar_path = os.path.join(KUNDA_DIR, "src", "components", "sections", "navbar&footer", "Navbar.astro")
with open(navbar_path, "r", encoding="utf-8") as f:
    navbar_content = f.read()
navbar_content = navbar_content.replace('aria-label="ScrewFast"', 'aria-label="KUNDA"')
with open(navbar_path, "w", encoding="utf-8") as f:
    f.write(navbar_content)
print("[OK] Navbar.astro updated")

# 6. Update astro.config.mjs
astro_config_path = os.path.join(KUNDA_DIR, "astro.config.mjs")
with open(astro_config_path, "r", encoding="utf-8") as f:
    astro_config = f.read()
astro_config = astro_config.replace("title: 'ScrewFast Docs',", "title: 'KUNDA Docs',").replace("site: 'https://screwfast.uk',", "site: 'https://kunda.works',")
with open(astro_config_path, "w", encoding="utf-8") as f:
    f.write(astro_config)
print("[OK] astro.config.mjs updated")

# 7. Update English copy
copy_en_path = os.path.join(KUNDA_DIR, "src", "copy", "en.ts")
with open(copy_en_path, "r", encoding="utf-8") as f:
    copy_en = f.read()

# Replace site OG and description
copy_en = copy_en.replace(
    "'ScrewFast offers top-tier hardware tools and expert construction services to meet all your project needs. Start exploring and contact our sales team for superior quality and reliability.'",
    "'Kunda brings useful digital products and ideas together in one connected ecosystem: software applications, practical online tools, learning resources, and guides. One home. Many useful possibilities.'"
).replace(
    "'ScrewFast offers top-tier hardware tools and expert construction services to meet all your project needs.'",
    "'A home for useful digital things. Software, tools, knowledge, and digital resources.'"
).replace(
    "'ScrewFast: Hardware Tools & Construction Services'",
    "'KUNDA — A home for useful digital things'"
).replace(
    '"Equip your projects with ScrewFast\'s top-quality hardware tools and expert construction services. Trusted by industry leaders, ScrewFast offers simplicity, affordability, and reliability. Experience the difference with user-centric design and cutting-edge tools. Start exploring now!"',
    '"Kunda is an independent digital product company building a connected ecosystem of software, online tools, knowledge and resources. One home. Many useful possibilities."'
)

# Hero section replacement
copy_en = copy_en.replace(
    "'Equip Your Projects with <span class=\"text-yellow-500 dark:text-yellow-400\">ScrewFast</span>'",
    "'A home for <span class=\"text-orange-500 dark:text-orange-400\">useful digital things</span>'"
).replace(
    "'Top-quality hardware tools and expert construction services for every project need.'",
    "'Software, tools, resources and ideas designed to help you work smarter, create more and solve everyday problems.'"
).replace(
    "primaryBtn: 'Start Exploring',",
    "primaryBtn: 'Explore Products',"
).replace(
    "secondaryBtn: 'Contact Sales Team',",
    "secondaryBtn: 'Discover Free Tools',"
).replace(
    "banner: 'Explore ScrewFast on GitHub',",
    "banner: 'Welcome to KUNDA — Discover Our Ecosystem',"
)

with open(copy_en_path, "w", encoding="utf-8") as f:
    f.write(copy_en)

print("[OK] copy/en.ts updated with KUNDA copy")

print("\\n[SUCCESS] Phase 1 rebrand scripts completed successfully!")

