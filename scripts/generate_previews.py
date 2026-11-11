#!/usr/bin/env python3
"""
Generate high-fidelity, modern visual preview images for KUNDA Tools and Resources.
Adheres strictly to the UI/UX design guide:
- Real visual asset (IMG) previewing what the tool creates or what the resource contains.
- Professional modern dark/light contrast, typography, and styling tokens.
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"C:\Users\Dawda Mbowe\Antigravity\kunda\src\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_font(size, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\segoeui.ttf" if not bold else r"C:\Windows\Fonts\segoeuib.ttf",
        r"C:\Windows\Fonts\arial.ttf" if not bold else r"C:\Windows\Fonts\arialbd.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def get_mono_font(size):
    font_paths = [
        r"C:\Windows\Fonts\consola.ttf",
        r"C:\Windows\Fonts\cour.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def create_json_formatter_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (18, 20, 29, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, w, h], radius=16, fill=(24, 27, 38, 255))
    draw.rounded_rectangle([0, 0, w, 52], radius=16, fill=(30, 34, 48, 255))
    draw.rectangle([0, 36, w, 52], fill=(30, 34, 48, 255))

    draw.ellipse([24, 20, 36, 32], fill=(239, 68, 68, 255))
    draw.ellipse([46, 20, 58, 32], fill=(245, 158, 11, 255))
    draw.ellipse([68, 20, 80, 32], fill=(16, 185, 129, 255))

    title_font = get_font(13, bold=True)
    draw.text((w // 2 - 70, 18), "response.formatted.json", font=title_font, fill=(156, 163, 175, 255))

    draw.rounded_rectangle([w - 140, 14, w - 24, 38], radius=6, fill=(16, 185, 129, 35), outline=(16, 185, 129, 100))
    status_font = get_font(11, bold=True)
    draw.text((w - 128, 18), "✓ Valid JSON", font=status_font, fill=(52, 211, 153, 255))

    mono_font = get_mono_font(15)
    line_num_font = get_mono_font(13)

    code_lines = [
        (1, '{\n', (229, 231, 235)),
        (2, '  "status": "success",', (249, 115, 22)),
        (3, '  "code": 200,', (249, 115, 22)),
        (4, '  "platform": "KUNDA Micro-SaaS",', (249, 115, 22)),
        (5, '  "privacy": {', (249, 115, 22)),
        (6, '    "client_side_only": true,', (56, 189, 248)),
        (7, '    "zero_cloud_logs": true,', (56, 189, 248)),
        (8, '    "latency_ms": 0.42', (56, 189, 248)),
        (9, '  },', (229, 231, 235)),
        (10, '  "payload": [', (249, 115, 22)),
        (11, '    { "id": "tools", "active": true },', (167, 139, 250)),
        (12, '    { "id": "resources", "ready": true }', (167, 139, 250)),
        (13, '  ]', (229, 231, 235)),
        (14, '}', (229, 231, 235)),
    ]

    draw.rectangle([0, 52, 58, h], fill=(22, 25, 35, 255))
    y = 68
    for num, line, col in code_lines:
        draw.text((20, y), f"{num:2d}", font=line_num_font, fill=(75, 85, 99, 255))
        draw.text((74, y), line, font=mono_font, fill=col)
        y += 26

    draw.rectangle([0, h - 34, w, h], fill=(20, 22, 31, 255))
    bar_font = get_font(11)
    draw.text((24, h - 25), "UTF-8   |   Spaces: 2   |   14 lines, 342 chars", font=bar_font, fill=(107, 114, 128, 255))
    draw.text((w - 150, h - 25), "⚡ 0.2ms parse time", font=bar_font, fill=(249, 115, 22, 255))

    out_path = os.path.join(OUTPUT_DIR, "tool-json-formatter-preview.png")
    img.save(out_path, "PNG")

def create_password_checker_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, w, h], radius=16, fill=(23, 32, 54, 255))
    draw.rounded_rectangle([0, 0, w, 52], radius=16, fill=(30, 41, 67, 255))
    draw.rectangle([0, 36, w, 52], fill=(30, 41, 67, 255))
    draw.ellipse([24, 20, 36, 32], fill=(239, 68, 68, 255))
    draw.ellipse([46, 20, 58, 32], fill=(245, 158, 11, 255))
    draw.ellipse([68, 20, 80, 32], fill=(16, 185, 129, 255))

    title_font = get_font(13, bold=True)
    draw.text((w // 2 - 80, 18), "Entropy & Security Audit", font=title_font, fill=(148, 163, 184, 255))

    draw.rounded_rectangle([40, 75, w - 40, 125], radius=10, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=2)
    mono_font = get_mono_font(16)
    draw.text((60, 90), "k9#xR!9mQ$vL2@zP_2026", font=mono_font, fill=(241, 245, 249, 255))

    badge_font = get_font(11, bold=True)
    draw.rounded_rectangle([w - 170, 85, w - 55, 115], radius=6, fill=(16, 185, 129, 40), outline=(16, 185, 129, 200))
    draw.text((w - 156, 92), "VERY STRONG", font=badge_font, fill=(52, 211, 153, 255))

    bar_y = 145
    seg_w = (w - 80 - 30) // 4
    for i in range(4):
        x0 = 40 + i * (seg_w + 10)
        x1 = x0 + seg_w
        color = (16, 185, 129, 255)
        draw.rounded_rectangle([x0, bar_y, x1, bar_y + 8], radius=4, fill=color)

    card_y = 175
    card_w = (w - 80 - 40) // 3
    metrics = [
        ("ENTROPY BITS", "98.4 bits", "Exceeds NIST Guidelines", (56, 189, 248)),
        ("CRACK TIME", "3.4 × 10¹⁴ yrs", "Immune to brute-force", (52, 211, 153)),
        ("LEAK STATUS", "0 Breaches", "Clean in HIBP database", (167, 139, 250)),
    ]

    for i, (label, val, sub, col) in enumerate(metrics):
        cx0 = 40 + i * (card_w + 20)
        cx1 = cx0 + card_w
        draw.rounded_rectangle([cx0, card_y, cx1, card_y + 110], radius=12, fill=(30, 41, 67, 255), outline=(51, 65, 85, 255))
        draw.text((cx0 + 16, card_y + 16), label, font=get_font(10, bold=True), fill=(148, 163, 184, 255))
        draw.text((cx0 + 16, card_y + 38), val, font=get_font(20, bold=True), fill=col)
        draw.text((cx0 + 16, card_y + 76), sub, font=get_font(11), fill=(148, 163, 184, 255))

    check_y = 310
    checks = [
        ("✓ Length (22 chars)", True),
        ("✓ Uppercase & Lowercase", True),
        ("✓ Special Characters (!@#$)", True),
        ("✓ Numeric Digits (0-9)", True),
    ]
    for i, (text, ok) in enumerate(checks):
        col_x = 40 + (i % 2) * (w // 2 - 20)
        row_y = check_y + (i // 2) * 36
        draw.rounded_rectangle([col_x, row_y, col_x + (w // 2 - 50), row_y + 28], radius=6, fill=(20, 29, 47, 255))
        draw.text((col_x + 12, row_y + 6), text, font=get_font(12, bold=True), fill=(52, 211, 153, 255))

    draw.rectangle([0, h - 34, w, h], fill=(13, 20, 36, 255))
    draw.text((24, h - 25), "🔒 Calculated entirely on client via WebCrypto API · Zero keystrokes sent over network", font=get_font(11), fill=(100, 116, 139, 255))

    out_path = os.path.join(OUTPUT_DIR, "tool-password-checker-preview.png")
    img.save(out_path, "PNG")

def create_qr_generator_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (24, 24, 27, 255))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, w, h], radius=16, fill=(30, 30, 36, 255))
    draw.rounded_rectangle([0, 0, w, 52], radius=16, fill=(39, 39, 45, 255))
    draw.rectangle([0, 36, w, 52], fill=(39, 39, 45, 255))
    draw.ellipse([24, 20, 36, 32], fill=(239, 68, 68, 255))
    draw.ellipse([46, 20, 58, 32], fill=(245, 158, 11, 255))
    draw.ellipse([68, 20, 80, 32], fill=(16, 185, 129, 255))

    draw.text((w // 2 - 80, 18), "High-Density Vector QR Asset", font=get_font(13, bold=True), fill=(161, 161, 170, 255))

    draw.rounded_rectangle([36, 75, 330, h - 45], radius=12, fill=(24, 24, 27, 255), outline=(63, 63, 70, 255))
    draw.text((54, 95), "Target URL / Payload", font=get_font(12, bold=True), fill=(212, 212, 216, 255))
    draw.rounded_rectangle([54, 120, 312, 156], radius=6, fill=(39, 39, 45, 255))
    draw.text((64, 130), "https://kunda.works/access", font=get_mono_font(11), fill=(249, 115, 22, 255))

    settings = [
        ("Correction Level", "High (30% redundancy)"),
        ("Render Format", "SVG & PNG @ 1024px"),
        ("Margin / Padding", "4 modules quiet zone"),
        ("Dark Module Color", "#EA580C (Kunda Brand)"),
    ]
    sy = 175
    for label, val in settings:
        draw.text((54, sy), label, font=get_font(11), fill=(113, 113, 122, 255))
        draw.text((54, sy + 16), val, font=get_font(11, bold=True), fill=(228, 228, 231, 255))
        sy += 42

    draw.rounded_rectangle([54, sy + 10, 312, sy + 48], radius=8, fill=(234, 88, 12, 255))
    draw.text((115, sy + 22), "Download 1024px PNG ↓", font=get_font(12, bold=True), fill=(255, 255, 255, 255))

    qr_card_x0, qr_card_y0 = 360, 75
    qr_card_x1, qr_card_y1 = w - 36, h - 45
    draw.rounded_rectangle([qr_card_x0, qr_card_y0, qr_card_x1, qr_card_y1], radius=14, fill=(255, 255, 255, 255))

    qr_size = 240
    qx = qr_card_x0 + (qr_card_x1 - qr_card_x0 - qr_size) // 2
    qy = qr_card_y0 + 40

    def draw_corner_finder(px, py):
        draw.rounded_rectangle([px, py, px + 56, py + 56], radius=8, fill=(234, 88, 12, 255))
        draw.rounded_rectangle([px + 8, py + 8, px + 48, py + 48], radius=4, fill=(255, 255, 255, 255))
        draw.rounded_rectangle([px + 16, py + 16, px + 40, py + 40], radius=3, fill=(234, 88, 12, 255))

    draw_corner_finder(qx, qy)
    draw_corner_finder(qx + qr_size - 56, qy)
    draw_corner_finder(qx, qy + qr_size - 56)

    import random
    rng = random.Random(42)
    grid_dim = 19
    cell_w = qr_size / grid_dim
    for row in range(grid_dim):
        for col in range(grid_dim):
            if (row < 7 and col < 7) or (row < 7 and col >= grid_dim - 7) or (row >= grid_dim - 7 and col < 7):
                continue
            if rng.random() > 0.52:
                cx = qx + col * cell_w
                cy = qy + row * cell_w
                draw.rectangle([cx + 1, cy + 1, cx + cell_w - 1, cy + cell_w - 1], fill=(24, 24, 27, 255))

    center_w = 44
    draw.rounded_rectangle([qx + qr_size//2 - center_w//2, qy + qr_size//2 - center_w//2,
                            qx + qr_size//2 + center_w//2, qy + qr_size//2 + center_w//2],
                           radius=6, fill=(255, 255, 255, 255), outline=(234, 88, 12, 255), width=2)
    draw.text((qx + qr_size//2 - 14, qy + qr_size//2 - 8), "KD", font=get_font(13, bold=True), fill=(234, 88, 12, 255))

    draw.text((qr_card_x0 + 40, qy + qr_size + 15), "⚡ Instant camera scan verified", font=get_font(11, bold=True), fill=(16, 185, 129, 255))

    out_path = os.path.join(OUTPUT_DIR, "tool-qr-generator-preview.png")
    img.save(out_path, "PNG")

def create_agency_onboarding_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (244, 244, 246, 255))
    draw = ImageDraw.Draw(img)

    for gx in range(0, w, 32):
        draw.line([gx, 0, gx, h], fill=(230, 230, 235, 255))
    for gy in range(0, h, 32):
        draw.line([0, gy, w, gy], fill=(230, 230, 235, 255))

    doc_x0, doc_y0 = 60, 40
    doc_x1, doc_y1 = w - 60, h - 40
    draw.rounded_rectangle([doc_x0 + 6, doc_y0 + 8, doc_x1 + 6, doc_y1 + 8], radius=12, fill=(210, 213, 220, 180))
    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y1], radius=12, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255))

    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y0 + 12], radius=12, fill=(234, 88, 12, 255))
    draw.rectangle([doc_x0, doc_y0 + 6, doc_x1, doc_y0 + 12], fill=(234, 88, 12, 255))

    draw.rounded_rectangle([doc_x0 + 40, doc_y0 + 35, doc_x0 + 110, doc_y0 + 58], radius=6, fill=(234, 88, 12, 30))
    draw.text((doc_x0 + 48, doc_y0 + 39), "DOCX / PDF", font=get_font(11, bold=True), fill=(234, 88, 12, 255))

    draw.text((doc_x0 + 125, doc_y0 + 38), "KUNDA AGENCY SPECIFICATION V2.4", font=get_font(12, bold=True), fill=(100, 116, 139, 255))
    draw.text((doc_x0 + 40, doc_y0 + 72), "Client Intake & Asset Handover Blueprint", font=get_font(22, bold=True), fill=(15, 23, 42, 255))
    draw.text((doc_x0 + 40, doc_y0 + 108), "Standardized templates, vector checklists, brand intake questionnaire, and approval milestones.", font=get_font(12), fill=(100, 116, 139, 255))

    col_w = (doc_x1 - doc_x0 - 80 - 40) // 3
    sections = [
        ("01. BRAND ASSETS", [
            "• Vector SVG / AI Logos",
            "• Color Palette & Hex Codes",
            "• Typography Licensing",
            "• Photography Library",
        ], (234, 88, 12)),
        ("02. TECHNICAL SCOPE", [
            "• Domain & DNS Delegation",
            "• Cloudflare Zero-Trust Auth",
            "• CMS & Headless APIs",
            "• Analytics & Meta Pixel",
        ], (56, 189, 248)),
        ("03. SIGN-OFF SLA", [
            "• Milestone Acceptance",
            "• Scope Boundary Policy",
            "• Revision Turnaround (48h)",
            "• Final Handoff Protocol",
        ], (16, 185, 129)),
    ]

    sec_y = doc_y0 + 150
    for i, (title, items, col) in enumerate(sections):
        sx0 = doc_x0 + 40 + i * (col_w + 20)
        sx1 = sx0 + col_w
        draw.rounded_rectangle([sx0, sec_y, sx1, sec_y + 180], radius=8, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255))
        draw.text((sx0 + 14, sec_y + 14), title, font=get_font(11, bold=True), fill=col)
        iy = sec_y + 44
        for item in items:
            draw.text((sx0 + 14, iy), item, font=get_font(11), fill=(71, 85, 105, 255))
            iy += 28

    draw.text((doc_x0 + 40, doc_y1 - 32), "850 KB · Includes Editable .DOCX + Notion Workspace Template · Commercial License", font=get_font(10), fill=(148, 163, 184, 255))

    out_path = os.path.join(OUTPUT_DIR, "resource-agency-onboarding-preview.png")
    img.save(out_path, "PNG")

def create_saas_launch_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    for gx in range(0, w, 32):
        draw.line([gx, 0, gx, h], fill=(25, 36, 60, 255))
    for gy in range(0, h, 32):
        draw.line([0, gy, w, gy], fill=(25, 36, 60, 255))

    doc_x0, doc_y0 = 60, 40
    doc_x1, doc_y1 = w - 60, h - 40
    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y1], radius=14, fill=(23, 32, 54, 255), outline=(51, 65, 85, 255))

    draw.rounded_rectangle([doc_x0 + 40, doc_y0 + 30, doc_x0 + 105, doc_y0 + 54], radius=6, fill=(16, 185, 129, 30))
    draw.text((doc_x0 + 52, doc_y0 + 35), "PDF GUIDE", font=get_font(11, bold=True), fill=(52, 211, 153, 255))

    draw.text((doc_x0 + 120, doc_y0 + 35), "PRODUCTION READINESS AUDIT", font=get_font(12, bold=True), fill=(148, 163, 184, 255))
    draw.text((doc_x0 + 40, doc_y0 + 68), "Zero-Cost Micro-SaaS Launch Checklist", font=get_font(22, bold=True), fill=(248, 250, 252, 255))
    draw.text((doc_x0 + 40, doc_y0 + 104), "48 critical pre-flight checks: DNS, Strict SSL, HSTS, D1 backups, transactional email & edge caching.", font=get_font(12), fill=(148, 163, 184, 255))

    check_cols = [
        ("INFRASTRUCTURE", [
            ("[✓] Cloudflare DNS + Proxied CNAME", True),
            ("[✓] Full (Strict) SSL / TLS 1.3", True),
            ("[✓] Security Headers (HSTS, CSP)", True),
            ("[✓] D1 Distributed SQL Replication", True),
        ]),
        ("TRANSACTIONAL & OPS", [
            ("[✓] DKIM, SPF, DMARC 100% Pass", True),
            ("[✓] Resend / SendGrid Webhooks", True),
            ("[✓] Sentry Edge Error Tracking", True),
            ("[✓] Automated Stripe Tax Rules", True),
        ]),
    ]

    col_w = (doc_x1 - doc_x0 - 80 - 30) // 2
    sec_y = doc_y0 + 145
    for i, (title, items) in enumerate(check_cols):
        sx0 = doc_x0 + 40 + i * (col_w + 30)
        sx1 = sx0 + col_w
        draw.rounded_rectangle([sx0, sec_y, sx1, sec_y + 190], radius=10, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255))
        draw.text((sx0 + 16, sec_y + 16), title, font=get_font(11, bold=True), fill=(249, 115, 22, 255))
        iy = sec_y + 48
        for item, _ in items:
            draw.text((sx0 + 16, iy), item, font=get_mono_font(12), fill=(226, 232, 240, 255))
            iy += 32

    draw.text((doc_x0 + 40, doc_y1 - 30), "1.2 MB · Verified for Cloudflare Pages, Workers & Astro 5 · Instant Download", font=get_font(10), fill=(100, 116, 139, 255))

    out_path = os.path.join(OUTPUT_DIR, "resource-saas-launch-preview.png")
    img.save(out_path, "PNG")

def create_cloudflare_guide_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (17, 24, 39, 255))
    draw = ImageDraw.Draw(img)

    for gx in range(0, w, 32):
        draw.line([gx, 0, gx, h], fill=(31, 41, 55, 255))
    for gy in range(0, h, 32):
        draw.line([0, gy, w, gy], fill=(31, 41, 55, 255))

    doc_x0, doc_y0 = 60, 40
    doc_x1, doc_y1 = w - 60, h - 40
    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y1], radius=14, fill=(24, 31, 47, 255), outline=(55, 65, 81, 255))

    draw.rounded_rectangle([doc_x0 + 40, doc_y0 + 30, doc_x0 + 115, doc_y0 + 54], radius=6, fill=(249, 115, 22, 35))
    draw.text((doc_x0 + 48, doc_y0 + 35), "ARCH GUIDE", font=get_font(11, bold=True), fill=(251, 146, 60, 255))

    draw.text((doc_x0 + 130, doc_y0 + 35), "EDGE INFRASTRUCTURE BLUEPRINT", font=get_font(12, bold=True), fill=(156, 163, 175, 255))
    draw.text((doc_x0 + 40, doc_y0 + 68), "Cloudflare Free-Tier Micro-SaaS Stack", font=get_font(22, bold=True), fill=(243, 244, 246, 255))
    draw.text((doc_x0 + 40, doc_y0 + 104), "Complete architecture topology: Pages, Workers, D1 SQL, R2 Storage, and KV caching without recurring server bills.", font=get_font(12), fill=(156, 163, 175, 255))

    boxes = [
        ("EDGE CDN & PAGES", "Static Assets · Global SSR Cache", (249, 115, 22)),
        ("WORKERS API", "Low-latency compute (<10ms global)", (56, 189, 248)),
        ("D1 RELATIONAL SQL", "Serverless SQLite at the edge", (16, 185, 129)),
        ("R2 OBJECT STORE", "S3-compatible · Zero egress fee", (167, 139, 250)),
    ]
    bw = (doc_x1 - doc_x0 - 80 - 30) // 2
    for i, (btitle, bsub, bcol) in enumerate(boxes):
        bx0 = doc_x0 + 40 + (i % 2) * (bw + 30)
        by0 = doc_y0 + 150 + (i // 2) * 85
        draw.rounded_rectangle([bx0, by0, bx0 + bw, by0 + 70], radius=8, fill=(17, 24, 39, 255), outline=(55, 65, 81, 255))
        draw.text((bx0 + 16, by0 + 14), btitle, font=get_font(12, bold=True), fill=bcol)
        draw.text((bx0 + 16, by0 + 38), bsub, font=get_font(11), fill=(156, 163, 175, 255))

    draw.text((doc_x0 + 40, doc_y1 - 30), "2.4 MB · Includes Wrangler.toml templates, D1 migration schemas & CI/CD workflow", font=get_font(10), fill=(107, 114, 128, 255))

    out_path = os.path.join(OUTPUT_DIR, "resource-cloudflare-guide-preview.png")
    img.save(out_path, "PNG")

def create_pricing_matrix_preview():
    w, h = 800, 480
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    for gx in range(0, w, 32):
        draw.line([gx, 0, gx, h], fill=(241, 245, 249, 255))
    for gy in range(0, h, 32):
        draw.line([0, gy, w, gy], fill=(241, 245, 249, 255))

    doc_x0, doc_y0 = 60, 40
    doc_x1, doc_y1 = w - 60, h - 40
    draw.rounded_rectangle([doc_x0 + 6, doc_y0 + 8, doc_x1 + 6, doc_y1 + 8], radius=12, fill=(203, 213, 225, 180))
    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y1], radius=12, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255))

    draw.rounded_rectangle([doc_x0, doc_y0, doc_x1, doc_y0 + 12], radius=12, fill=(16, 185, 129, 255))
    draw.rectangle([doc_x0, doc_y0 + 6, doc_x1, doc_y0 + 12], fill=(16, 185, 129, 255))

    draw.rounded_rectangle([doc_x0 + 40, doc_y0 + 35, doc_x0 + 130, doc_y0 + 58], radius=6, fill=(16, 185, 129, 30))
    draw.text((doc_x0 + 48, doc_y0 + 39), "FINANCIAL MODEL", font=get_font(11, bold=True), fill=(16, 185, 129, 255))

    draw.text((doc_x0 + 145, doc_y0 + 38), "SPREADSHEET & NOTION CALCULATOR", font=get_font(12, bold=True), fill=(100, 116, 139, 255))
    draw.text((doc_x0 + 40, doc_y0 + 72), "Micro-SaaS Pricing & Unit Economics Matrix", font=get_font(22, bold=True), fill=(15, 23, 42, 255))
    draw.text((doc_x0 + 40, doc_y0 + 108), "Interactive formulas for MRR expansion, churn tolerance, lifetime value (LTV), and break-even modeling.", font=get_font(12), fill=(100, 116, 139, 255))

    col_w = (doc_x1 - doc_x0 - 80 - 40) // 3
    tiers = [
        ("SOLO STARTER", "$19/mo", ["• 1,000 monthly credits", "• Client-side encryption", "• Email support (48h)"], (100, 116, 139)),
        ("GROWTH PRO", "$49/mo", ["• 25,000 monthly credits", "• Custom domain CNAME", "• Webhook integrations"], (234, 88, 12)),
        ("AGENCY SCALE", "$149/mo", ["• Unlimited monthly runs", "• White-label exports", "• 1-on-1 Slack channel"], (16, 185, 129)),
    ]

    sec_y = doc_y0 + 150
    for i, (name, price, bullets, col) in enumerate(tiers):
        sx0 = doc_x0 + 40 + i * (col_w + 20)
        sx1 = sx0 + col_w
        draw.rounded_rectangle([sx0, sec_y, sx1, sec_y + 180], radius=8, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255))
        draw.text((sx0 + 14, sec_y + 14), name, font=get_font(10, bold=True), fill=col)
        draw.text((sx0 + 14, sec_y + 36), price, font=get_font(20, bold=True), fill=(15, 23, 42, 255))
        iy = sec_y + 75
        for b in bullets:
            draw.text((sx0 + 14, iy), b, font=get_font(11), fill=(71, 85, 105, 255))
            iy += 26

    draw.text((doc_x0 + 40, doc_y1 - 32), "950 KB · Google Sheets + Excel (.XLSX) + Interactive Notion Template", font=get_font(10), fill=(148, 163, 184, 255))

    out_path = os.path.join(OUTPUT_DIR, "resource-pricing-matrix-preview.png")
    img.save(out_path, "PNG")

if __name__ == "__main__":
    create_json_formatter_preview()
    create_password_checker_preview()
    create_qr_generator_preview()
    create_agency_onboarding_preview()
    create_saas_launch_preview()
    create_cloudflare_guide_preview()
    create_pricing_matrix_preview()
    print("All 7 visual asset previews generated successfully!")
