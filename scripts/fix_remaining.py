"""Fix remaining patches that failed in the first pass."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(rel):
    p = os.path.join(ROOT, rel)
    with open(p, 'r', encoding='utf-8') as f: return f.read()

def write(rel, content):
    p = os.path.join(ROOT, rel)
    with open(p, 'w', encoding='utf-8') as f: f.write(content)
    print(f"  ✅ {rel}")

def patch(rel, old, new, desc=""):
    c = read(rel)
    if old not in c:
        print(f"  ⚠️  SKIP ({rel}): not found — {desc or old[:60]}")
        return False
    write(rel, c.replace(old, new))
    if desc: print(f"     → {desc}")
    return True

print("\n[D-009] ContactSection.astro — correct path")
patch("src/components/sections/misc/ContactSection.astro",
    'linkTitle="support@screwfast.uk"',
    'linkTitle="hello@kunda.works"', "linkTitle")
patch("src/components/sections/misc/ContactSection.astro",
    'linkURL="mailto:support@screwfast.uk"',
    'linkURL="mailto:hello@kunda.works"', "linkURL")

print("\n[D-003] en.ts statistics[0] — encoding fix")
# The em dash in the file is encoded as â€" (UTF-8 mojibake of —)
c = read("src/copy/en.ts")
# Search for the actual string with any em-dash variant
old1 = "'customers equipped \u00e2\u0080\u0094 from DIY to major construction firms'"
new1 = "'developers, designers and founders using KUNDA tools monthly'"
old2 = "customers equipped \u2014 from DIY to major construction firms"  # actual em-dash
new2 = "developers, designers and founders using KUNDA tools monthly"

if old1 in c:
    write("src/copy/en.ts", c.replace(old1, new1))
    print("  ✅ statistics[0] fixed (UTF-8 encoding variant)")
elif old2 in c:
    write("src/copy/en.ts", c.replace(old2, new2))
    print("  ✅ statistics[0] fixed (em-dash variant)")
else:
    # Try regex
    new_c, n = re.subn(r"customers equipped.*?construction firms", 
                       "developers, designers and founders using KUNDA tools monthly",
                       c)
    if n:
        write("src/copy/en.ts", new_c)
        print(f"  ✅ statistics[0] fixed via regex ({n} replacements)")
    else:
        print("  ⚠️  statistics[0]: could not find pattern")

print("\n[D-007] en.ts nav labels — add micro-saas")
c = read("src/copy/en.ts")
# Find the labels block
old_labels = "    labels: {\n      products: 'Products',"
new_labels = "    labels: {\n      products: 'Products',\n      'micro-saas': 'Micro-SaaS',"
if old_labels in c:
    write("src/copy/en.ts", c.replace(old_labels, new_labels))
    print("  ✅ micro-saas nav label added")
else:
    # Try alternative whitespace
    old_labels2 = "    labels: {\r\n      products: 'Products',"
    new_labels2 = "    labels: {\r\n      products: 'Products',\r\n      'micro-saas': 'Micro-SaaS',"
    if old_labels2 in c:
        write("src/copy/en.ts", c.replace(old_labels2, new_labels2))
        print("  ✅ micro-saas nav label added (CRLF variant)")
    else:
        # Find by regex
        new_c, n = re.subn(
            r"(labels:\s*\{[^\n]*\n\s*products:\s*'Products',)",
            r"\1\n      'micro-saas': 'Micro-SaaS',",
            c
        )
        if n:
            write("src/copy/en.ts", new_c)
            print(f"  ✅ micro-saas nav label added via regex")
        else:
            print("  ⚠️  could not find labels block to insert micro-saas")

print("\n[D-005] astro.config.mjs Starlight 'Tools & Equipment' → 'Using KUNDA'")
c = read("astro.config.mjs")
# Try with literal & and without encoding
old_te = "label: 'Tools & Equipment',"
new_te = "label: 'Using KUNDA',"
if old_te in c:
    write("astro.config.mjs", c.replace(old_te, new_te))
    print("  ✅ Starlight label 'Tools & Equipment' → 'Using KUNDA'")
else:
    print(f"  ⚠️  'Tools & Equipment' label not found as plain text")
    # Show what's around that area
    idx = c.find("Tool Guides")
    if idx > -1:
        print(f"  Context around 'Tool Guides': ...{repr(c[idx-100:idx+50])}...")

print("\nDone.")

