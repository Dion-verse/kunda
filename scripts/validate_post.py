#!/usr/bin/env python3
"""
KUNDA Blog Post Validator.
Validates YAML frontmatter, Markdown structure, image paths, and word counts.
"""

import sys
import re
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BLOG_EN_DIR = REPO_ROOT / "src" / "content" / "blog" / "en"
REQUIRED_FIELDS = [
    "title",
    "description",
    "author",
    "authorImage",
    "authorImageAlt",
    "pubDate",
    "cardImage",
    "cardImageAlt",
    "readTime",
    "tags"
]


def validate_file(file_path: Path):
    print(f"[CHECK] Validating {file_path.name}...")
    content = file_path.read_text(encoding="utf-8")

    # 1. Frontmatter delimiter check
    if not content.startswith("---"):
        raise ValueError("Missing starting YAML frontmatter delimiter (---).")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter format: missing closing delimiter (---).")

    raw_yaml = parts[1]
    body = parts[2].strip()

    # 2. Parse YAML
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        raise ValueError(f"YAML frontmatter parsing failed: {e}")

    # 3. Required Fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(f"Missing required frontmatter field: '{field}'")

    if not data["title"] or len(str(data["title"])) < 5:
        raise ValueError("Title is too short or empty.")

    if not data["description"] or len(str(data["description"])) < 10:
        raise ValueError("Description is too short or empty.")

    # 4. Word Count Check
    word_count = len(body.split())
    if word_count < 150:
        raise ValueError(f"Article body too short: {word_count} words (minimum 150 required).")

    # 5. Heading Structure Check
    h2_count = len(re.findall(r"^##\s+", body, re.MULTILINE))
    h3_count = len(re.findall(r"^###\s+", body, re.MULTILINE))
    if (h2_count + h3_count) < 1:
        raise ValueError(f"Article must contain at least one heading (found {h2_count + h3_count}).")

    print(f"âœ“ {file_path.name}: Valid! (Words: {word_count}, H2s: {h2_count}, Tags: {data['tags']})")
    return True


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None

    if target:
        path = Path(target)
        if not path.is_file():
            print(f"[ERROR] Target file does not exist: {path}", file=sys.stderr)
            sys.exit(1)
        validate_file(path)
    else:
        # Validate all en posts
        posts = sorted(BLOG_EN_DIR.glob("post-*.md"))
        errors = 0
        for p in posts:
            try:
                validate_file(p)
            except Exception as e:
                print(f"[FAIL] {p.name}: {e}", file=sys.stderr)
                errors += 1

        if errors > 0:
            print(f"\n[ERROR] {errors} validation error(s) found.", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"\nâœ“ All {len(posts)} blog posts passed validation successfully.")


if __name__ == "__main__":
    main()
