# -*- coding: utf-8 -*-
"""
Remediation script for Phase 5:
Injects clean "Explore More KUNDA Tools" section into each tool page
right before <script is:inline>
"""

import os

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

related_for_json = """
    {/* Related Tools Navigation */}
    <div class="mt-14 pt-10 border-t border-neutral-200 dark:border-neutral-800">
      <div class="mb-6 flex items-center justify-between">
        <h3 class="text-xl font-bold tracking-tight text-neutral-800 dark:text-neutral-200">
          Explore More Free KUNDA Tools
        </h3>
        <a href="/tools" class="text-sm font-semibold text-orange-600 hover:text-orange-500 dark:text-orange-400">
          View All Tools &rarr;
        </a>
      </div>
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <a
          href="/tools/password-checker"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-emerald-600 dark:text-emerald-400">Security</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            Password Strength & Entropy Analyzer
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Measure password resilience and calculate cryptographic entropy client-side.
          </p>
        </a>
        <a
          href="/tools/qr-generator"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-blue-600 dark:text-blue-400">Utility</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            Instant QR Code Generator
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Generate clean, scannable QR codes for web links, text, or vCards.
          </p>
        </a>
      </div>
    </div>
  </div>

"""

related_for_password = """
    {/* Related Tools Navigation */}
    <div class="mt-14 pt-10 border-t border-neutral-200 dark:border-neutral-800">
      <div class="mb-6 flex items-center justify-between">
        <h3 class="text-xl font-bold tracking-tight text-neutral-800 dark:text-neutral-200">
          Explore More Free KUNDA Tools
        </h3>
        <a href="/tools" class="text-sm font-semibold text-orange-600 hover:text-orange-500 dark:text-orange-400">
          View All Tools &rarr;
        </a>
      </div>
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <a
          href="/tools/json-formatter"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-purple-600 dark:text-purple-400">Developer</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            JSON Formatter & Validator
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Clean, validate, beautify, and minify JSON payloads in your browser.
          </p>
        </a>
        <a
          href="/tools/qr-generator"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-blue-600 dark:text-blue-400">Utility</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            Instant QR Code Generator
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Generate clean, scannable QR codes for web links, text, or vCards.
          </p>
        </a>
      </div>
    </div>
  </div>

"""

related_for_qr = """
    {/* Related Tools Navigation */}
    <div class="mt-14 pt-10 border-t border-neutral-200 dark:border-neutral-800">
      <div class="mb-6 flex items-center justify-between">
        <h3 class="text-xl font-bold tracking-tight text-neutral-800 dark:text-neutral-200">
          Explore More Free KUNDA Tools
        </h3>
        <a href="/tools" class="text-sm font-semibold text-orange-600 hover:text-orange-500 dark:text-orange-400">
          View All Tools &rarr;
        </a>
      </div>
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <a
          href="/tools/json-formatter"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-purple-600 dark:text-purple-400">Developer</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            JSON Formatter & Validator
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Clean, validate, beautify, and minify JSON payloads in your browser.
          </p>
        </a>
        <a
          href="/tools/password-checker"
          class="group rounded-2xl border border-neutral-200 bg-white p-5 shadow-xs transition-all duration-300 hover:-translate-y-0.5 hover:border-orange-500/50 hover:shadow-md dark:border-neutral-800 dark:bg-neutral-900"
        >
          <span class="text-xs font-semibold uppercase text-emerald-600 dark:text-emerald-400">Security</span>
          <h4 class="mt-1 text-lg font-bold text-neutral-800 group-hover:text-orange-600 dark:text-neutral-200 dark:group-hover:text-orange-400">
            Password Strength & Entropy Analyzer
          </h4>
          <p class="mt-1 text-xs text-neutral-600 dark:text-neutral-400">
            Measure password resilience and calculate cryptographic entropy client-side.
          </p>
        </a>
      </div>
    </div>
  </div>

"""

def inject(path, snippet):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Explore More Free KUNDA Tools" in content:
        print(f"Skipping {path}, already present")
        return
    idx = content.find("  <script is:inline>")
    if idx != -1:
        # Insert right before <script is:inline>
        new_content = content[:idx] + snippet + content[idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully injected into {path}")
    else:
        print(f"Could not find insertion target in {path}")

inject(os.path.join(ROOT, "src/pages/tools/json-formatter.astro"), related_for_json)
inject(os.path.join(ROOT, "src/pages/tools/password-checker.astro"), related_for_password)
inject(os.path.join(ROOT, "src/pages/tools/qr-generator.astro"), related_for_qr)
print("PHASE 5 COMPLETED!")
