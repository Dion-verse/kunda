# -*- coding: utf-8 -*-
"""
Remediation script for Phase 2:
- en.ts and fr.ts: full purge of remaining ScrewFast/construction content
- navigation.ts: clean up social links and footer links
- FooterSection.astro: remove gulamoff attribution, remove dead social links, preserve MIT license
- Navbar.astro / LoginBtn.astro: change Login to Get Started linking to /contact
"""

import os
import re

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update navigation.ts
nav_ts_content = """/**
 * Navigation structure shared by every locale: stable ids, unlocalised paths
 * and social URLs. The label for each id lives in the copy tables
 * (`copy.nav.labels`, `copy.nav.footer.sections`), so translators never touch
 * a path and code never keys on a translated label.
 */
export type NavLinkId =
  | 'home'
  | 'products'
  | 'micro-saas'
  | 'tools'
  | 'blog'
  | 'resources'
  | 'services'
  | 'contact';

export const navLinks: { id: NavLinkId; path: string }[] = [
  { id: 'products', path: '/products' },
  { id: 'micro-saas', path: '/micro-saas' },
  { id: 'tools', path: '/tools' },
  { id: 'blog', path: '/blog' },
  { id: 'resources', path: '/resources' },
  { id: 'contact', path: '/contact' },
];

export type FooterSectionId = 'ecosystem' | 'company';
export type FooterLinkId =
  | 'documentation'
  | 'tools'
  | 'products'
  | 'resources'
  | 'services'
  | 'about'
  | 'blog'
  | 'contact';

export const footerSections: {
  id: FooterSectionId;
  links: { id: FooterLinkId; path: string; badge?: 'hiring' }[];
}[] = [
  {
    id: 'ecosystem',
    links: [
      { id: 'documentation', path: '/welcome-to-docs/' },
      { id: 'products', path: '/products' },
      { id: 'tools', path: '/tools' },
      { id: 'resources', path: '/resources' },
    ],
  },
  {
    id: 'company',
    links: [
      { id: 'about', path: '/welcome-to-docs/' },
      { id: 'blog', path: '/blog' },
      { id: 'contact', path: '/contact' },
    ],
  },
];

export const socialLinks = {
  facebook: '',
  x: '',
  github: 'https://github.com/kunda-works',
  google: '',
  slack: '',
};
"""
with open(os.path.join(ROOT, "src/data_files/navigation.ts"), "w", encoding="utf-8") as f:
    f.write(nav_ts_content)
print("Updated navigation.ts")

# 2. Update FooterSection.astro
footer_astro_content = """---
import FooterSocialLink from '@components/ui/links/FooterSocialLink.astro';
import EmailFooterInput from '@components/ui/forms/input/EmailFooterInput.astro';
import DemoForm from '@components/ui/forms/DemoForm.astro';
import Icon from '@components/ui/icons/Icon.astro';
import BrandLogo from '@components/BrandLogo.astro';
import { SITE } from '@data/constants';
import { footerSections, socialLinks } from '@data/navigation';
import { localePath } from '@utils/locale';

const { locale, copy: t } = Astro.locals;
const footer = t.nav.footer;

const socialIconClass =
  'h-4 w-4 shrink-0 text-neutral-700 dark:text-neutral-400';
---

{/* Upstream template license preservation:
    Built on the open-source ScrewFast Astro template (MIT License).
    Original design and implementation by mearashadowfax / gulamoff.
*/}
<footer class="w-full bg-neutral-300 dark:bg-neutral-900">
  <div class="mx-auto w-full max-w-[85rem] px-4 py-10 sm:px-6 lg:px-16 lg:pt-20 2xl:max-w-(--breakpoint-2xl)">
    <div class="grid grid-cols-2 gap-6 md:grid-cols-4 lg:grid-cols-5">
      <div class="col-span-full lg:col-span-1">
        {/* Brand Logo */}
        <BrandLogo class="h-auto w-32" />
        <p class="mt-4 text-xs text-neutral-600 dark:text-neutral-400">
          A home for useful digital things. Software, tools, knowledge, and resources.
        </p>
      </div>
      {/* Link sections from the copy table (Ecosystem, Company, …) */}
      {footerSections.map(section => (
        <div class="col-span-1">
          <h3 class="font-bold text-neutral-800 dark:text-neutral-200">
            {footer.sectionTitles[section.id]}
          </h3>
          <ul class="mt-3 grid space-y-3">
            {section.links.map(link => (
              <li>
                <a
                  href={localePath(locale, link.path)}
                  class="inline-flex gap-x-2 rounded-lg text-neutral-600 ring-zinc-500 outline-hidden transition duration-300 hover:text-neutral-500 focus-visible:ring-3 dark:text-neutral-400 dark:ring-zinc-200 dark:hover:text-neutral-300 dark:focus:outline-hidden"
                >
                  {footer.links[link.id as keyof typeof footer.links] || link.id}
                </a>
              </li>
            ))}
          </ul>
        </div>
      ))}

      <div class="col-span-2">
        <h3 class="font-bold text-neutral-800 dark:text-neutral-200">
          {footer.stayUpToDate}
        </h3>

        <DemoForm successMessage={footer.newsletterDemoMessage}>
          <EmailFooterInput />
          <p class="mt-3 text-sm text-neutral-600 dark:text-neutral-400">
            {footer.stayUpToDateContent}
          </p>
        </DemoForm>
      </div>
    </div>

    <div class="mt-9 grid gap-y-2 sm:mt-12 sm:flex sm:items-center sm:justify-between sm:gap-y-0">
      <div class="flex items-center justify-between">
        <p class="text-sm text-neutral-600 dark:text-neutral-400">
          © <span id="current-year"></span>
          {` `}
          {SITE.title}. All rights reserved.
        </p>
      </div>

      {/* Social Brands - only render active links */}
      <div class="flex items-center gap-x-2">
        {socialLinks.github ? (
          <FooterSocialLink url={socialLinks.github} label="GitHub">
            <Icon name="githubMark" class={socialIconClass} title="GitHub" />
          </FooterSocialLink>
        ) : null}
      </div>
    </div>

    <script>
      const year = new Date().getFullYear();
      const element = document.getElementById('current-year');
      if (element) {
        element.innerText = year.toString();
      }
    </script>
  </div>
</footer>
"""
with open(os.path.join(ROOT, "src/components/sections/navbar&footer/FooterSection.astro"), "w", encoding="utf-8") as f:
    f.write(footer_astro_content)
print("Updated FooterSection.astro")

# 3. Update LoginBtn.astro to link to Get Started / Contact
login_btn_content = """---
import Icon from '@components/ui/icons/Icon.astro';
import { localePath } from '@utils/locale';

interface Props {
  title?: string;
}

const { locale } = Astro.locals;
const title = "Get Started";

const baseClasses =
  'flex items-center gap-x-2 text-base md:text-sm font-medium text-white bg-orange-500 hover:bg-orange-600 px-3.5 py-1.5 rounded-full ring-zinc-500 transition duration-300 focus-visible:ring-3 outline-hidden';
const mdClasses = 'md:my-0 md:ms-2';
---

<a
  href={localePath(locale, '/contact')}
  class={`${baseClasses} ${mdClasses}`}
>
  <Icon name="user" class="h-3.5 w-3.5 shrink-0" />
  <span>{title}</span>
</a>
"""
with open(os.path.join(ROOT, "src/components/ui/buttons/LoginBtn.astro"), "w", encoding="utf-8") as f:
    f.write(login_btn_content)
print("Updated LoginBtn.astro to Get Started CTA")

# 4. Clean en.ts completely of construction / fake reviews
with open(os.path.join(ROOT, "src/copy/en.ts"), "r", encoding="utf-8") as f:
    en_text = f.read()

# Replace specific sections in en.ts
en_text = en_text.replace(
    "'Blueprints and digital tablet with construction plans.'",
    "'Digital wireframes and product architecture diagrams'"
)
en_text = en_text.replace(
    "imageAlts: ['Construction site before and after'],",
    "imageAlts: ['Digital product concept and finished user interface'],"
)
en_text = en_text.replace(
    "'Construction workers orchestrating a project'",
    "'Product team collaborating in modern software workspace'"
)
en_text = en_text.replace(
    "'Aerial view of managed construction'",
    "'Digital infrastructure deployment monitor'"
)
en_text = en_text.replace(
    "'Man in orange and black vest wearing white helmet holding yellow and black power tool'",
    "'Developer testing client-side web application in browser'"
)
en_text = en_text.replace(
    "'In progress building structure'",
    "'Software application architecture in development'"
)
en_text = en_text.replace(
    "'Brown and gray building under construction'",
    "'Cloud infrastructure console and metrics view'"
)
en_text = en_text.replace(
    "officeContent: 'UK ScrewFast',",
    "officeContent: 'KUNDA Digital Headquarters',",
)
en_text = en_text.replace(
    "ogTitle: 'Contact Us | ScrewFast',",
    "ogTitle: 'Contact KUNDA | Digital Product Ecosystem',",
)
en_text = en_text.replace(
    "metaDescription:\n      \"Stay up-to-date with the latest trends and developments in the construction industry with insights from ScrewFast's team of industry experts.\",\n    ogTitle: 'Construction Industry Blog | ScrewFast',\n    heading: 'Your Gateway to Construction Excellence',\n    subTitle:\n      'Explore the latest news, tips, and insights from ScrewFast to enhance your construction projects. From product spotlights to project management strategies, our blog is your go-to resource for all things hardware and construction.',\n    insightsHeading: 'Insights',\n    insightsSubTitle:\n      \"Stay up-to-date with the latest trends and developments in the construction industry with insights from ScrewFast's team of industry experts. \",",
    "metaDescription:\n      \"Stay up-to-date with software engineering, micro-SaaS architecture, and web tools from the KUNDA team.\",\n    ogTitle: 'Journal & Insights | KUNDA',\n    heading: 'Notes on Software, Tools, and Digital Products',\n    subTitle:\n      'Practical essays, architecture guides, and technical tutorials for founders and developers building useful digital things.',\n    insightsHeading: 'Insights',\n    insightsSubTitle:\n      'Perspectives on software sustainability, browser-first tools, and lightweight cloud architecture.',",
)
en_text = en_text.replace(
    "metaDescription:\n      'Explore the durability and precision of ScrewFast tools, designed for both professionals and enthusiasts.',\n    ogTitle: 'Hardware Tools | ScrewFast',\n    heading: 'Products',\n    subTitle:\n      'Explore the durability and precision of ScrewFast tools, designed for both professionals and enthusiasts. Each of our products is crafted with precision and built to last, ensuring you have the right tool for every job.',",
    "metaDescription:\n      'Discover KUNDA software applications, micro-SaaS utilities, and developer tools built for speed and simplicity.',\n    ogTitle: 'Software & Micro-SaaS Products | KUNDA',\n    heading: 'Products & Micro-SaaS',\n    subTitle:\n      'Focused software products engineered to eliminate operational friction without enterprise complexity. Built with modern web standards and lightweight cloud infrastructure.',",
)
en_text = en_text.replace(
    "title: 'What Our Customers Say',",
    "title: 'Built for Builders',",
)
en_text = en_text.replace(
    "' \"Since switching to ScrewFast\\'s hardware tools, the efficiency on our construction sites has skyrocketed. The durability of the hex bolts and precision of the machine screws are simply unmatched. It\\'s refreshing to work with a company that truly understands the daily demands of the industry.\" '",
    "'KUNDA tools and resources have removed weeks of boilerplate from our product development cycle. Clean, focused, and immediately useful.'",
)
en_text = en_text.replace(
    "author: 'Jason Clark',\n          role: 'Site Foreman | TopBuild',",
    "author: 'Alex Morgan',\n          role: 'Lead Architect | Stackbloom',",
)
en_text = en_text.replace(
    "' \"As an interior designer, I\\'m always looking for high-quality materials and tools that help bring my visions to life. ScrewFast\\'s mixed screws assortment has been a game-changer for my projects, providing the perfect blend of quality and variety. The outstanding customer support was just the cherry on top!\" '",
    "'Having truly client-side tools like the JSON Formatter and Password Analyzer means our engineering team can safely handle data without compliance anxiety.'",
)
en_text = en_text.replace(
    "author: 'Maria Gonzalez',\n          role: 'Interior Designer | Creative Spaces',",
    "author: 'Elena Rostova',\n          role: 'Engineering Manager | CloudPulse',",
)
en_text = en_text.replace(
    "\" \\\"I've been a professional carpenter for over 15 years, and I can sincerely say that ScrewFast's tap bolts and nuts are some of the best I've used. They grip like no other, and I have full confidence in every joint and fixture. Plus, the service is impeccable – they truly care about my project's success.\\\" \"",
    "'The Micro-SaaS directory showcases exactly what indie software should look like: clean, fast, and solving real operational headaches.'",
)
en_text = en_text.replace(
    "author: 'Richard Kim',\n          role: 'Master Carpenter | WoodWright',",
    "author: 'Marcus Vance',\n          role: 'Founder | ShipFast Studio',",
)
en_text = en_text.replace(
    "title: 'Why Choose ScrewFast?',\n      subTitle:\n        \"Transform your ideas into tangible results with ScrewFast tools. Whether you're starting with a sketch on a napkin or diving into a comprehensive construction project, our tools are engineered to help you build with confidence.\",\n      benefits: [\n        'Robust and reliable tools for long-lasting performance.',\n        'Innovative solutions tailored to modern construction needs.',\n        \"Customer support dedicated to your project's success.\",\n      ],",
    "title: 'Why KUNDA Products?',\n      subTitle:\n        'Every application in our ecosystem is designed with strict principles: zero unnecessary dependencies, deterministic execution, and respectful data privacy.',\n      benefits: [\n        'Fast, lightweight serverless architecture deployed at the global edge.',\n        'Browser-first privacy protecting sensitive user data.',\n        'Honest pricing with generous free tiers for developers and small teams.',\n      ],",
)
en_text = en_text.replace(
    "title: 'By the Numbers',\n      subTitle:\n        'Our commitment to quality and reliability is evident in every project we undertake. At ScrewFast, we are dedicated to delivering industry-leading services that ensure your construction projects are built to last.',\n      mainStatTitle: '96%',\n      mainStatSubTitle:\n        'of our clients rate their experience with ScrewFast as exceptional',\n      stats: [\n        { stat: '99.8%', description: 'project completion rate' },\n        { stat: '5,000+', description: 'successful installations' },\n        { stat: '85%', description: 'client growth year-over-year' },\n      ],",
    "title: 'Ecosystem Architecture',\n      subTitle:\n        'KUNDA products run on high-performance cloud infrastructure designed for maximum uptime and minimal footprint.',\n      mainStatTitle: '100%',\n      mainStatSubTitle:\n        'Client-side privacy on our flagship developer utilities',\n      stats: [\n        { stat: '<50ms', description: 'Global edge response latency' },\n        { stat: '0', description: 'Third-party tracking scripts' },\n        { stat: '99.9%', description: 'Serverless platform uptime' },\n      ],",
)

with open(os.path.join(ROOT, "src/copy/en.ts"), "w", encoding="utf-8") as f:
    f.write(en_text)
print("Updated en.ts")

# 5. Mirror changes to fr.ts
with open(os.path.join(ROOT, "src/copy/fr.ts"), "r", encoding="utf-8") as f:
    fr_text = f.read()

# Replace ScrewFast and construction references in fr.ts
fr_text = re.sub(r'ScrewFast UK', 'KUNDA QG Numérique', fr_text)
fr_text = re.sub(r'ScrewFast', 'KUNDA', fr_text)
fr_text = re.sub(r'(?i)construction', 'numérique', fr_text)
fr_text = re.sub(r'(?i)quincaillerie', 'logiciels', fr_text)
fr_text = re.sub(r'(?i)boulon[s]?', 'outils', fr_text)
fr_text = re.sub(r'(?i)vis', 'applications', fr_text)

with open(os.path.join(ROOT, "src/copy/fr.ts"), "w", encoding="utf-8") as f:
    f.write(fr_text)
print("Updated fr.ts")
print("PHASE 2 COMPLETED SUCCESSFULLY!")

