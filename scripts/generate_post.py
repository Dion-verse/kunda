#!/usr/bin/env python3
"""
KUNDA Automated Journal Publishing Engine.
Powered by Google Gemini API via official google-genai SDK.
Generates structured Markdown blog posts conforming strictly to KUNDA's content schema.
"""

import os
import sys
import json
import time
import re
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env")

TOPICS_FILE = REPO_ROOT / "blog-automation" / "topics.txt"
STATE_FILE = REPO_ROOT / "blog-automation" / "state.json"
BLOG_EN_DIR = REPO_ROOT / "src" / "content" / "blog" / "en"
BLOG_FR_DIR = REPO_ROOT / "src" / "content" / "blog" / "fr"

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    print("[ERROR] GEMINI_API_KEY environment variable is missing.", file=sys.stderr)
    sys.exit(1)


def get_next_topic():
    """Read the top unhandled topic from topics.txt."""
    if not TOPICS_FILE.exists():
        raise FileNotFoundError(f"{TOPICS_FILE} not found.")

    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not lines:
        return None, []

    return lines[0], lines[1:]


def determine_next_post_id():
    """Inspect existing posts and determine the next post-N identifier."""
    existing_en = list(BLOG_EN_DIR.glob("post-*.md"))
    nums = []
    for p in existing_en:
        match = re.search(r"post-(\d+)\.md$", p.name)
        if match:
            nums.append(int(match.group(1)))
    next_num = max(nums, default=0) + 1
    return f"post-{next_num}"


def generate_article_with_gemini(topic: str):
    """Generate article content and frontmatter using Gemini."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=API_KEY)

    prompt = f"""You are the lead engineering editor at KUNDA (kunda.works), an independent digital software company building privacy-first developer tools and micro-SaaS applications.

Topic: "{topic}"

Write an authoritative, highly practical, and engaging developer article about this topic.
Requirements:
1. Genuine technical insight without fabricated quotes, fake research citations, or corporate AI filler.
2. Structure:
   - Compelling introductory hook explaining the real-world operational problem.
   - 3 to 4 detailed sections with clear H2 (##) and H3 (###) headers.
   - Code snippets, architectural comparisons, or practical tips where applicable.
   - Practical conclusions and key takeaways for engineers/founders.
3. Length: Between 650 and 1000 words.
4. Output MUST be clean Markdown starting directly with YAML frontmatter:
---
title: "<Engaging title without quotes>"
description: "<One crisp summary sentence, under 150 characters>"
author: "Dawda Mbowe"
role: "Founder, KUNDA"
authorImage: "@/images/blog/jacob.avif"
authorImageAlt: "Dawda Mbowe portrait"
pubDate: {datetime.now().strftime('%Y-%m-%d')}
cardImage: "@/images/blog/post-1.avif"
cardImageAlt: "<Descriptive alt text for article card visual>"
readTime: 5
tags: ["<3 to 5 lowercase tags>"]
---

[Followed by the article body in Markdown]
"""

    print(f"[INFO] Requesting article generation from Gemini ({MODEL_NAME})...")
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
        )
    )

    content = response.text.strip()
    # Strip any accidental ```markdown wrapper or leading yaml tag
    if content.startswith("```markdown"):
        content = content[len("```markdown"):].strip()
    elif content.startswith("```yaml"):
        content = content[len("```yaml"):].strip()
    elif content.startswith("```"):
        content = content[len("```"):].strip()
    if content.endswith("```"):
        content = content[:-3].strip()
    if content.startswith("yaml\n"):
        content = content[len("yaml\n"):].strip()

    return content


def translate_article_to_french(english_content: str):
    """Generate French localized edition of the article."""
    from google import genai

    client = genai.Client(api_key=API_KEY)
    prompt = f"""Translate and adapt this technical article into professional French for French-speaking software developers.
Preserve the exact YAML frontmatter structure, keeping the same keys (title, description, author, role, authorImage, authorImageAlt, pubDate, cardImage, cardImageAlt, readTime, tags), but translate title, description, cardImageAlt, tags, and article body.
Ensure the author is 'Dawda Mbowe'.

Original Content:
{english_content}
"""
    print(f"[INFO] Generating French translation...")
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    content = response.text.strip()
    if content.startswith("```markdown"):
        content = content[len("```markdown"):].strip()
    elif content.startswith("```yaml"):
        content = content[len("```yaml"):].strip()
    elif content.startswith("```"):
        content = content[len("```"):].strip()
    if content.endswith("```"):
        content = content[:-3].strip()
    if content.startswith("yaml\n"):
        content = content[len("yaml\n"):].strip()

    return content


def update_state_and_queue(topic: str, remaining_topics: list, post_id: str, title: str):
    """Update state.json and remove published topic from topics.txt."""
    # 1. Update topics.txt
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        header_lines = [l for l in f if l.startswith("#")]
    with open(TOPICS_FILE, "w", encoding="utf-8") as f:
        for h in header_lines:
            f.write(h)
        for t in remaining_topics:
            f.write(t + "\n")

    # 2. Update state.json
    state = {"last_run_timestamp": int(time.time()), "published_posts": []}
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
        except Exception:
            pass

    state["last_run_timestamp"] = int(time.time())
    state["published_posts"].append({
        "id": post_id,
        "title": title,
        "topic": topic,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def main():
    topic, remaining = get_next_topic()
    if not topic:
        print("[INFO] Topic queue is empty. Nothing to generate.")
        sys.exit(0)

    print(f"[INFO] Next topic: '{topic}'")
    post_id = determine_next_post_id()
    print(f"[INFO] Target identifier: {post_id}")

    en_content = generate_article_with_gemini(topic)

    # Extract title from generated frontmatter
    title_match = re.search(r'title:\s*["\']?([^"\']+)["\']?', en_content)
    title = title_match.group(1) if title_match else topic

    # Write English Post
    en_file = BLOG_EN_DIR / f"{post_id}.md"
    with open(en_file, "w", encoding="utf-8") as f:
        f.write(en_content + "\n")
    print(f"[SUCCESS] Wrote English post: {en_file}")

    # Generate and Write French Post
    try:
        fr_content = translate_article_to_french(en_content)
        fr_file = BLOG_FR_DIR / f"{post_id}.md"
        with open(fr_file, "w", encoding="utf-8") as f:
            f.write(fr_content + "\n")
        print(f"[SUCCESS] Wrote French post: {fr_file}")
    except Exception as e:
        print(f"[WARN] French translation failed ({e}); writing English fallback.", file=sys.stderr)
        fr_file = BLOG_FR_DIR / f"{post_id}.md"
        with open(fr_file, "w", encoding="utf-8") as f:
            f.write(en_content + "\n")

    # Update Queue
    update_state_and_queue(topic, remaining, post_id, title)
    print(f"[DONE] Successfully published and queued {post_id} ('{title}').")


if __name__ == "__main__":
    main()
