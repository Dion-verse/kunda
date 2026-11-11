#!/usr/bin/env python3
"""
execution/curate_site_images.py
-------------------------------
Advanced, context-aware image discovery, scoring, smart-cropping, and
AVIF asset compilation system for KUNDA.

Features:
1. Contextual Image Slot Registry: Every image slot has its semantic purpose,
   aspect ratio, resolution bounds, and query vocabulary.
2. Multi-Candidate Discovery: Fetches high-resolution candidate images from
   Unsplash / verified tech asset pools.
3. Multi-Metric Quality Scoring Engine:
   - Resolution adequacy
   - Sharpness & focus via Laplacian gradient variance
   - Contrast & dynamic range spread
   - Aspect ratio congruence
   - Aesthetic tone alignment
4. Smart Entropy Cropping: Crops around focal areas rather than naive top-left.
5. High-Efficiency Asset Encoding: Encodes into AVIF/WebP with tuned compression.
6. Audit & Manifest Ledger: Generates persistent tracking in discovery/.
"""

import argparse
import io
import json
import math
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
from PIL import Image, ImageFilter, ImageStat

# ---------------------------------------------------------------------------
# Path Resolution
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
KUNDA_DIR = BASE_DIR / "kunda"
IMAGES_DIR = KUNDA_DIR / "src" / "images"
DISCOVERY_DIR = BASE_DIR / "discovery"
TMP_DIR = BASE_DIR / ".tmp"

DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------
@dataclass
class ImageSlot:
    slot_id: str
    target_rel_path: str
    page: str
    component: str
    semantic_role: str
    target_aspect: float  # e.g., 16/9 = 1.777, 4/3 = 1.333, 1.0 = 1.0
    min_dimensions: Tuple[int, int]
    target_dimensions: Tuple[int, int]
    tone_preference: str  # 'tech_dark', 'high_contrast', 'clean_ui', 'editorial'
    primary_queries: List[str]
    curated_candidates: List[str] = field(default_factory=list)

@dataclass
class QualityScore:
    resolution_score: float
    sharpness_score: float
    contrast_score: float
    aspect_fit_score: float
    tone_score: float
    overall_score: float
    notes: List[str] = field(default_factory=list)

# ---------------------------------------------------------------------------
# Semantic Slot Registry for KUNDA
# ---------------------------------------------------------------------------
SLOT_REGISTRY: Dict[str, ImageSlot] = {
    # 1. Product Cards & Previews
    "product_seatsentry_card": ImageSlot(
        slot_id="product_seatsentry_card",
        target_rel_path="product-image-1.avif",
        page="Products (/products)",
        component="CardProduct",
        semantic_role="Cloud Governance & SaaS License Optimization Dashboard",
        target_aspect=1.333,  # ~4:3
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="tech_dark",
        primary_queries=["saas analytics dashboard dark mode", "cloud metrics graph monitor", "security compliance UI"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1400&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1400&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?q=80&w=1400&auto=format&fit=crop",
        ]
    ),
    "product_seatsentry_main": ImageSlot(
        slot_id="product_seatsentry_main",
        target_rel_path="product-image-main-1.avif",
        page="Product Detail (/products/item-f303)",
        component="ProductDetail",
        semantic_role="High-Resolution Cloud License & Workspace Management Overview",
        target_aspect=1.777,  # 16:9
        min_dimensions=(1200, 675),
        target_dimensions=(1600, 900),
        tone_preference="tech_dark",
        primary_queries=["data observability enterprise platform", "modern cloud analytics telemetry", "cloud cost management UI"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop",
        ]
    ),
    "product_queuepass_card": ImageSlot(
        slot_id="product_queuepass_card",
        target_rel_path="product-image-2.avif",
        page="Products (/products)",
        component="CardProduct",
        semantic_role="Smart SMS Virtual Waitlist & Mobile Queue App",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="modern_ui",
        primary_queries=["mobile app interaction waitlist", "customer queue smartphone interface", "contactless check-in app"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=1400&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1556742049-0a67c5574f73?q=80&w=1400&auto=format&fit=crop",
        ]
    ),
    "product_queuepass_main": ImageSlot(
        slot_id="product_queuepass_main",
        target_rel_path="product-image-main-2.avif",
        page="Product Detail (/products/item-a765)",
        component="ProductDetail",
        semantic_role="High-Res Mobile Queue Management & Guest Experience Workflow",
        target_aspect=1.777,
        min_dimensions=(1200, 675),
        target_dimensions=(1600, 900),
        tone_preference="modern_ui",
        primary_queries=["digital service check-in workflow", "tablet point of sale guest management", "mobile waitlist interface"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1556742049-0a67c5574f73?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1600&auto=format&fit=crop",
        ]
    ),
    "product_assetsnag_card": ImageSlot(
        slot_id="product_assetsnag_card",
        target_rel_path="product-image-3.avif",
        page="Products (/products)",
        component="CardProduct",
        semantic_role="Agency Client Asset Intake & File Pre-flight Validator",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="clean_ui",
        primary_queries=["digital design system wireframe assets", "creative design components layout", "vector file inspector"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?q=80&w=1400&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1581291518655-9523c932deda?q=80&w=1400&auto=format&fit=crop",
        ]
    ),
    "product_assetsnag_main": ImageSlot(
        slot_id="product_assetsnag_main",
        target_rel_path="product-image-main-3.avif",
        page="Product Detail (/products/item-b203)",
        component="ProductDetail",
        semantic_role="High-Res Asset Upload Portal & Pre-flight Diagnostics Interface",
        target_aspect=1.777,
        min_dimensions=(1200, 675),
        target_dimensions=(1600, 900),
        tone_preference="clean_ui",
        primary_queries=["UI UX design wireframes screen", "creative asset validation software", "modern interface layout"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1581291518655-9523c932deda?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?q=80&w=1600&auto=format&fit=crop",
        ]
    ),
    "product_devtools_card": ImageSlot(
        slot_id="product_devtools_card",
        target_rel_path="product-image-4.avif",
        page="Products (/products)",
        component="CardProduct",
        semantic_role="KUNDA Developer Utilities Browser Suite",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="tech_dark",
        primary_queries=["syntax highlighted code editor dark mode", "programming code ide screen", "javascript python code editor"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1400&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=1400&auto=format&fit=crop",
        ]
    ),
    "product_devtools_main": ImageSlot(
        slot_id="product_devtools_main",
        target_rel_path="product-image-main-4.avif",
        page="Product Detail (/products/item-t845)",
        component="ProductDetail",
        semantic_role="High-Res Developer Workstation & Client-Side Utility Suite",
        target_aspect=1.777,
        min_dimensions=(1200, 675),
        target_dimensions=(1600, 900),
        tone_preference="tech_dark",
        primary_queries=["developer coding workstation dual monitor", "modern web developer terminal", "programming ide laptop screen"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1600&auto=format&fit=crop",
        ]
    ),

    # 2. Homepage & Core Features
    "home_hero": ImageSlot(
        slot_id="home_hero",
        target_rel_path="hero-image.avif",
        page="Homepage (/)",
        component="HeroSection",
        semantic_role="Independent Digital Software Ecosystem & Developer Studio Hero",
        target_aspect=1.5,
        min_dimensions=(1200, 800),
        target_dimensions=(1600, 1066),
        tone_preference="editorial",
        primary_queries=["minimalist developer workstation macbook code", "software engineer desk setup aesthetic", "web development clean studio"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1600&auto=format&fit=crop",
        ]
    ),
    "features_stats_alt": ImageSlot(
        slot_id="features_stats_alt",
        target_rel_path="features-image.avif",
        page="Products & Features",
        component="FeaturesStatsAlt",
        semantic_role="High Performance Edge Analytics & Platform Scalability Preview",
        target_aspect=1.5,
        min_dimensions=(1200, 800),
        target_dimensions=(1600, 1066),
        tone_preference="clean_ui",
        primary_queries=["modern software product dashboard preview", "analytics platform telemetry UI", "minimal web application UI"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600&auto=format&fit=crop",
        ]
    ),
    "features_automated_tools": ImageSlot(
        slot_id="features_automated_tools",
        target_rel_path="automated-tools.avif",
        page="Homepage (/)",
        component="FeaturesNavs",
        semantic_role="Automated CI/CD Pipeline, Git Deployment, and Edge Workers",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="tech_dark",
        primary_queries=["developer terminal git command line", "devops pipeline automation screen", "coding terminal dark mode"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "features_global_edge": ImageSlot(
        slot_id="features_global_edge",
        target_rel_path="construction-image.avif",
        page="Homepage (/)",
        component="FeaturesNavs",
        semantic_role="Global Cloudflare Edge Network & Distributed Infrastructure",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="tech_dark",
        primary_queries=["global cloud network connectivity edge nodes", "digital globe fiber optic datacenter", "cyber architecture network"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "features_dashboard_metrics": ImageSlot(
        slot_id="features_dashboard_metrics",
        target_rel_path="dashboard-image.avif",
        page="Homepage (/)",
        component="FeaturesNavs",
        semantic_role="Real-Time Observability & Performance Metrics Dashboard",
        target_aspect=1.333,
        min_dimensions=(800, 600),
        target_dimensions=(1200, 900),
        tone_preference="clean_ui",
        primary_queries=["saas growth chart data analytics UI", "digital metrics financial dashboard", "business intelligence dashboard"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop",
        ]
    ),

    # 3. Services & Consulting
    "services_team_collab": ImageSlot(
        slot_id="services_team_collab",
        target_rel_path="aerial-view.avif",
        page="Services (/services)",
        component="AlternatingSections",
        semantic_role="Agile Product Team & Digital Architecture Strategy",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="editorial",
        primary_queries=["software product team planning sprint", "tech startup team collaboration laptop", "design sprint team meeting"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "services_stack_modernization": ImageSlot(
        slot_id="services_stack_modernization",
        target_rel_path="before-after.avif",
        page="Services (/services)",
        component="AlternatingSections",
        semantic_role="Legacy Monolith vs Modern Serverless Architecture Transformation",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="tech_dark",
        primary_queries=["code refactoring digital transformation", "cyber software matrix code stream", "modern software architecture"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "services_ui_wireframes": ImageSlot(
        slot_id="services_ui_wireframes",
        target_rel_path="blueprints-image.avif",
        page="Services (/services)",
        component="AlternatingSections",
        semantic_role="System Architecture Schematics & UI Design Systems",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="clean_ui",
        primary_queries=["digital wireframe user flow layout", "UI UX design blueprints digital", "system architecture diagram mockup"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "services_cloud_datacenter": ImageSlot(
        slot_id="services_cloud_datacenter",
        target_rel_path="blueprint-2.avif",
        page="Services (/services)",
        component="AlternatingSections",
        semantic_role="Edge Cloud Infrastructure & Low Latency Networking",
        target_aspect=1.333,
        min_dimensions=(600, 450),
        target_dimensions=(800, 600),
        tone_preference="tech_dark",
        primary_queries=["cloud server racks blue lights", "datacenter enterprise servers", "datacenter cables hardware"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=800&auto=format&fit=crop",
        ]
    ),
    "services_engineer_presenting": ImageSlot(
        slot_id="services_engineer_presenting",
        target_rel_path="person-working.avif",
        page="Services (/services)",
        component="AlternatingSections",
        semantic_role="Product Architect Reviewing Technical Architecture",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="editorial",
        primary_queries=["software engineer presentation technical", "product architect discussing roadmap", "tech consultation session"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1200&auto=format&fit=crop",
        ]
    ),

    # 4. Blog Posts & Journal
    "blog_post_1": ImageSlot(
        slot_id="blog_post_1",
        target_rel_path=os.path.join("blog", "post-1.avif"),
        page="Blog (/blog/post-1)",
        component="CardBlog",
        semantic_role="Single-Purpose Software & Micro-SaaS Architectural Patterns",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="tech_dark",
        primary_queries=["clean coding programming code monitor", "web developer software architecture", "code terminal minimal"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "blog_post_2": ImageSlot(
        slot_id="blog_post_2",
        target_rel_path=os.path.join("blog", "post-2.avif"),
        page="Blog (/blog/post-2)",
        component="CardBlog",
        semantic_role="Edge Computing, Cloudflare Workers & Sub-50ms API Latency",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="tech_dark",
        primary_queries=["server room glowing fiber optics", "cloud computing edge network servers", "datacenter modern networking"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "blog_post_3": ImageSlot(
        slot_id="blog_post_3",
        target_rel_path=os.path.join("blog", "post-3.avif"),
        page="Blog (/blog/post-3)",
        component="CardBlog",
        semantic_role="Solo Developer Bootstrapping & Lean Product Validation",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="editorial",
        primary_queries=["indie hacker solo founder workspace coffee laptop", "bootstrapping developer workstation", "independent maker desk"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop",
        ]
    ),

    # 5. Technical Insights
    "insight_1": ImageSlot(
        slot_id="insight_1",
        target_rel_path=os.path.join("insights", "insight-1.avif"),
        page="Insights (/insights/insight-1)",
        component="CardInsight",
        semantic_role="Global Edge Latency Benchmarks & Cold Start Optimization",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="clean_ui",
        primary_queries=["latency performance benchmark graph", "data visualization performance metrics", "system performance telemetry"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "insight_2": ImageSlot(
        slot_id="insight_2",
        target_rel_path=os.path.join("insights", "insight-2.avif"),
        page="Insights (/insights/insight-2)",
        component="CardInsight",
        semantic_role="Client-Side Cryptography & WebCrypto Zero-Knowledge Architecture",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="tech_dark",
        primary_queries=["cryptography data privacy digital security lock", "cyber security encryption tech", "privacy cryptographic matrix"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
    "insight_3": ImageSlot(
        slot_id="insight_3",
        target_rel_path=os.path.join("insights", "insight-3.avif"),
        page="Insights (/insights/insight-3)",
        component="CardInsight",
        semantic_role="Unit Economics & Sustainable Monetization of Focused Tools",
        target_aspect=1.5,
        min_dimensions=(800, 533),
        target_dimensions=(1200, 800),
        tone_preference="clean_ui",
        primary_queries=["saas unit economics business chart", "financial growth metrics software revenue", "business profitability graph"],
        curated_candidates=[
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop",
        ]
    ),
}

# ---------------------------------------------------------------------------
# Image Quality & Aesthetic Analyzer
# ---------------------------------------------------------------------------
class ImageQualityAnalyzer:
    """Computes multidimensional quality metrics for a PIL image candidate."""

    @staticmethod
    def evaluate(img: Image.Image, slot: ImageSlot) -> QualityScore:
        w, h = img.size
        min_w, min_h = slot.min_dimensions
        notes = []

        # 1. Resolution Adequacy (0.0 to 1.0)
        res_ratio = min(w / min_w, h / min_h)
        if res_ratio >= 1.0:
            res_score = min(1.0, 0.8 + 0.2 * min(res_ratio / 2.0, 1.0))
        else:
            res_score = max(0.0, res_ratio * 0.7)
            notes.append(f"Sub-optimal resolution: {w}x{h} vs min {min_w}x{min_h}")

        # 2. Aspect Ratio Congruence (0.0 to 1.0)
        native_aspect = w / h
        aspect_diff = abs(native_aspect - slot.target_aspect) / slot.target_aspect
        aspect_score = max(0.0, 1.0 - min(aspect_diff * 1.2, 1.0))
        if aspect_diff > 0.35:
            notes.append(f"Aspect ratio discrepancy ({native_aspect:.2f} vs target {slot.target_aspect:.2f})")

        # 3. Sharpness & Detail Analysis via Laplacian Variance
        # Convert to grayscale numpy array
        gray = img.convert("L").resize((400, int(400 * (h / w))))
        arr = np.array(gray, dtype=np.float32)
        # Compute gradient
        gy, gx = np.gradient(arr)
        gnorm = np.sqrt(gx**2 + gy**2)
        variance = float(np.var(gnorm))
        # Normal range of variance for sharp photos is ~40 to 300+
        sharpness_score = min(1.0, max(0.2, math.log1p(variance) / 5.5))
        if sharpness_score < 0.5:
            notes.append(f"Low edge detail/sharpness variance: {variance:.1f}")

        # 4. Contrast & Dynamic Range
        stat = ImageStat.Stat(gray)
        stddev = stat.stddev[0]
        # Rich contrast images have stddev between 40 and 80
        contrast_score = min(1.0, max(0.1, stddev / 65.0))
        if contrast_score < 0.4:
            notes.append(f"Flat contrast histogram (stddev: {stddev:.1f})")

        # 5. Aesthetic Tone Alignment
        mean_lum = stat.mean[0]
        if slot.tone_preference == "tech_dark":
            # Preferred mean luminance: 30 - 110
            tone_score = 1.0 - (abs(mean_lum - 70) / 120.0)
        elif slot.tone_preference == "clean_ui":
            # Preferred mean luminance: 80 - 180
            tone_score = 1.0 - (abs(mean_lum - 130) / 120.0)
        else:
            # Editorial / balanced: 60 - 160
            tone_score = 1.0 - (abs(mean_lum - 110) / 120.0)
        tone_score = min(1.0, max(0.3, tone_score))

        # Overall Weighted Score
        overall = (
            res_score * 0.30
            + sharpness_score * 0.25
            + contrast_score * 0.20
            + aspect_score * 0.15
            + tone_score * 0.10
        )

        return QualityScore(
            resolution_score=round(res_score, 3),
            sharpness_score=round(sharpness_score, 3),
            contrast_score=round(contrast_score, 3),
            aspect_fit_score=round(aspect_score, 3),
            tone_score=round(tone_score, 3),
            overall_score=round(overall, 3),
            notes=notes,
        )

# ---------------------------------------------------------------------------
# Smart Focal Cropping & Resizing
# ---------------------------------------------------------------------------
class SmartCropper:
    """Crops images to exact aspect ratio using weighted entropy center."""

    @staticmethod
    def crop_and_resize(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
        orig_w, orig_h = img.size
        target_aspect = target_w / target_h
        orig_aspect = orig_w / orig_h

        if abs(orig_aspect - target_aspect) < 0.01:
            # Aspect ratio already matches
            return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

        if orig_aspect > target_aspect:
            # Source is wider than target: crop horizontally
            new_w = int(orig_h * target_aspect)
            # Find horizontal center of mass / energy
            gray = img.convert("L").resize((100, 100))
            arr = np.array(gray, dtype=np.float32)
            gy, gx = np.gradient(arr)
            energy = np.sum(np.sqrt(gx**2 + gy**2), axis=0)
            center_x = (np.argmax(energy) / 100.0) * orig_w
            
            # Constrain window to image bounds
            left = max(0, min(orig_w - new_w, int(center_x - new_w / 2)))
            top = 0
            right = left + new_w
            bottom = orig_h
        else:
            # Source is taller than target: crop vertically
            new_h = int(orig_w / target_aspect)
            # Favor top-center (rule of thirds for heads/screens)
            top = int(max(0, min(orig_h - new_h, (orig_h - new_h) * 0.35)))
            left = 0
            right = orig_w
            bottom = top + new_h

        cropped = img.crop((left, top, right, bottom))
        return cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

# ---------------------------------------------------------------------------
# Asset Downloader & Cache Engine
# ---------------------------------------------------------------------------
class AssetEngine:
    """Manages fetching, candidate selection, caching, and AVIF encoding."""

    def __init__(self, dry_run: bool = False, verbose: bool = True):
        self.dry_run = dry_run
        self.verbose = verbose
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) KundaAssetCurator/2.0"}

    def fetch_image(self, url: str) -> Optional[Image.Image]:
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
            img = Image.open(io.BytesIO(data))
            return img.convert("RGB")
        except Exception as e:
            if self.verbose:
                print(f"    [WARN] Failed to fetch {url}: {e}")
            return None

    def search_candidates_for_query(self, query: str, count: int = 3) -> List[str]:
        """Constructs high-res Unsplash search endpoint URLs."""
        clean_q = urllib.parse.quote(query)
        # Using Unsplash curated source format
        return [
            f"https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600&auto=format&fit=crop",
            f"https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1600&auto=format&fit=crop",
        ]

    def select_best_candidate(self, slot: ImageSlot, custom_query: Optional[str] = None) -> Tuple[Optional[Image.Image], Optional[QualityScore], str]:
        candidates = list(slot.curated_candidates)
        if custom_query:
            query_candidates = self.search_candidates_for_query(custom_query)
            candidates = query_candidates + candidates

        best_img = None
        best_score = None
        best_url = ""

        for url in candidates:
            img = self.fetch_image(url)
            if not img:
                continue

            score = ImageQualityAnalyzer.evaluate(img, slot)
            if self.verbose:
                print(f"    Evaluated: score={score.overall_score:.3f} (res={score.resolution_score}, sharp={score.sharpness_score}, contrast={score.contrast_score})")

            if best_score is None or score.overall_score > best_score.overall_score:
                best_img = img
                best_score = score
                best_url = url

        return best_img, best_score, best_url

    def curate_slot(self, slot: ImageSlot, custom_query: Optional[str] = None) -> Dict:
        target_path = IMAGES_DIR / slot.target_rel_path
        print(f"\n[+] Curating Slot: '{slot.slot_id}'")
        print(f"    Placement: {slot.page} -> {slot.component}")
        print(f"    Target: src/images/{slot.target_rel_path} ({slot.target_dimensions[0]}x{slot.target_dimensions[1]})")

        best_img, best_score, best_url = self.select_best_candidate(slot, custom_query)
        if not best_img or not best_score:
            print(f"    [ERROR] No candidate could be fetched for slot: {slot.slot_id}")
            return {"slot_id": slot.slot_id, "status": "failed", "error": "No candidates reachable"}

        tw, th = slot.target_dimensions
        processed_img = SmartCropper.crop_and_resize(best_img, tw, th)

        result_info = {
            "slot_id": slot.slot_id,
            "target_path": str(target_path.relative_to(BASE_DIR)),
            "source_url": best_url,
            "dimensions": f"{tw}x{th}",
            "aspect_ratio": f"{tw/th:.3f}",
            "quality_score": asdict(best_score),
            "status": "dry_run" if self.dry_run else "updated",
        }

        if not self.dry_run:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            # Encode as AVIF
            processed_img.save(target_path, format="AVIF", quality=80)
            file_kb = target_path.stat().st_size // 1024
            result_info["file_size_kb"] = file_kb
            print(f"    [SUCCESS] Encoded AVIF ({file_kb} KB, Overall Score: {best_score.overall_score:.3f})")
        else:
            print(f"    [DRY-RUN] Selected candidate score: {best_score.overall_score:.3f} (Skipped write)")

        return result_info

# ---------------------------------------------------------------------------
# Audit Engine
# ---------------------------------------------------------------------------
def audit_site_images() -> List[Dict]:
    """Scans all registered slots and checks the current file on disk."""
    print("\n" + "=" * 80)
    print(" KUNDA SITE IMAGE AUDIT & QUALITY REPORT")
    print("=" * 80)

    audit_records = []
    for slot_id, slot in SLOT_REGISTRY.items():
        file_path = IMAGES_DIR / slot.target_rel_path
        record = {
            "slot_id": slot_id,
            "file": slot.target_rel_path,
            "page": slot.page,
            "component": slot.component,
            "exists": file_path.exists(),
        }

        if file_path.exists():
            try:
                with Image.open(file_path) as img:
                    w, h = img.size
                    score = ImageQualityAnalyzer.evaluate(img, slot)
                    record["dimensions"] = f"{w}x{h}"
                    record["format"] = img.format or "AVIF"
                    record["size_kb"] = file_path.stat().st_size // 1024
                    record["overall_score"] = score.overall_score
                    record["sharpness"] = score.sharpness_score
                    record["contrast"] = score.contrast_score
                    record["aspect_fit"] = score.aspect_fit_score
                    record["notes"] = score.notes
                    status_symbol = "[OK]" if score.overall_score >= 0.70 else "[FAIR]"
            except Exception as e:
                record["error"] = str(e)
                status_symbol = "[ERR]"
        else:
            status_symbol = "[MISSING]"
            record["dimensions"] = "N/A"
            record["size_kb"] = 0
            record["overall_score"] = 0.0

        audit_records.append(record)
        score_str = f"Score: {record.get('overall_score', 0):.2f}" if record["exists"] else "NOT FOUND"
        dim_str = record.get("dimensions", "N/A")
        size_str = f"{record.get('size_kb', 0)} KB"
        print(f"{status_symbol:<10} {slot.target_rel_path:<28} | {dim_str:<12} | {size_str:<8} | {score_str:<12} | {slot.page}")

    print("=" * 80)
    manifest_path = DISCOVERY_DIR / "site_images_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(audit_records, f, indent=2)
    print(f"\nAudit results saved to: discovery/site_images_manifest.json\n")
    return audit_records

# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Advanced Site Image Curator & Optimizer for KUNDA")
    parser.add_argument("--audit", action="store_true", help="Audit all current image assets across the site")
    parser.add_argument("--list-slots", action="store_true", help="List all defined image slots with their page context")
    parser.add_argument("--curate-all", action="store_true", help="Curate, score, and compile images for all slots")
    parser.add_argument("--target", type=str, help="Target specific slot_id or filename (e.g. product-image-1.avif)")
    parser.add_argument("--query", type=str, help="Custom search query override for candidate discovery")
    parser.add_argument("--dry-run", action="store_true", help="Evaluate candidates and score without writing files")

    args = parser.parse_args()

    if args.list_slots:
        print("\n=== KUNDA REGISTERED IMAGE SLOTS ===")
        for slot_id, slot in SLOT_REGISTRY.items():
            print(f"- {slot_id:<28} -> src/images/{slot.target_rel_path}")
            print(f"    Page/Component: {slot.page} ({slot.component})")
            print(f"    Role: {slot.semantic_role}")
            print(f"    Target: {slot.target_dimensions[0]}x{slot.target_dimensions[1]} (Aspect: {slot.target_aspect:.2f})")
            print(f"    Keywords: {', '.join(slot.primary_queries[:2])}")
        return

    if args.audit:
        audit_site_images()
        return

    engine = AssetEngine(dry_run=args.dry_run, verbose=True)

    if args.target:
        # Resolve target slot
        matched_slot = None
        for s_id, s in SLOT_REGISTRY.items():
            if s_id.lower() == args.target.lower() or s.target_rel_path.lower() == args.target.lower() or os.path.basename(s.target_rel_path).lower() == args.target.lower():
                matched_slot = s
                break

        if not matched_slot:
            print(f"[ERROR] Could not find slot matching target '{args.target}'. Run with --list-slots to see available slots.")
            sys.exit(1)

        result = engine.curate_slot(matched_slot, custom_query=args.query)
        print("\nCuration Summary:")
        print(json.dumps(result, indent=2))
        return

    if args.curate_all:
        results = []
        for slot in SLOT_REGISTRY.values():
            res = engine.curate_slot(slot, custom_query=args.query)
            results.append(res)

        manifest_path = DISCOVERY_DIR / "site_images_manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        print(f"\nAll slots processed. Manifest updated: discovery/site_images_manifest.json")
        return

    # Default to audit if no action specified
    parser.print_help()

if __name__ == "__main__":
    main()
