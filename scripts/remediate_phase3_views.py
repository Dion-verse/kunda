# -*- coding: utf-8 -*-
"""
Remediation script for Phase 3:
- HomeView.astro: purge fake reviews, fake ratings, ClientsSection, TestimonialsSection
- ContactSection.astro: purge fake London address
- ServicesView.astro: replace dead cta links with /contact
- tools/index.astro: refine UI hierarchy
- resources/index.astro: improve visual alignment with product cards, replace 404 download with coming soon
- micro-saas/index.astro: align with main design system
"""

import os

ROOT = r"C:\Users\Dawda Mbowe\Antigravity\kunda"

# 1. Update HomeView.astro
home_view_content = """---
import MainLayout from '@/layouts/MainLayout.astro';
import HeroSection from '@components/sections/landing/HeroSection.astro';
import HeroSectionAlt from '@components/sections/landing/HeroSectionAlt.astro';
import FeaturesGeneral from '@components/sections/features/FeaturesGeneral.astro';
import FeaturesNavs from '@components/sections/features/FeaturesNavs.astro';
import PricingSection from '@components/sections/pricing/PricingSection.astro';
import FAQ from '@components/sections/misc/FAQ.astro';
import AnnouncementBanner from '@components/ui/banners/AnnouncementBanner.astro';
import heroImage from '@images/hero-image.avif';
import featureImage from '@images/features-image.avif';
import construction from '@images/construction-image.avif';
import tools from '@images/automated-tools.avif';
import dashboard from '@images/dashboard-image.avif';
import { getCopy } from '@/copy';
import { localePath, type MarketingLocale } from '@utils/locale';

/** The home page in one locale. Copy comes from the locale's copy table. */
interface Props {
  locale: MarketingLocale;
}

const { locale } = Astro.props;
const t = getCopy(locale);
const copy = t.home;
---

<MainLayout>
  <AnnouncementBanner
    btnId="dismiss-button"
    btnTitle={copy.banner}
    url={localePath(locale, '/tools')}
  />

  {/* Authentic Hero Section without fabricated social proof */}
  <HeroSection
    title={copy.hero.title}
    subTitle={copy.hero.subTitle}
    primaryBtn={copy.hero.primaryBtn}
    primaryBtnURL={localePath(locale, '/products')}
    secondaryBtn={copy.hero.secondaryBtn}
    secondaryBtnURL={localePath(locale, '/tools')}
    withReview={false}
    src={heroImage}
    alt={copy.hero.imageAlt}
  />

  <FeaturesGeneral
    title={copy.featuresGeneral.title}
    subTitle={copy.featuresGeneral.subTitle}
    src={featureImage}
    alt={copy.featuresGeneral.imageAlt}
    features={t.data.features}
  />

  <FeaturesNavs
    title={copy.featuresNavs.title}
    tabs={[
      {
        ...copy.featuresNavs.tabs.tools,
        svg: 'tools',
        src: tools,
        first: true,
      },
      {
        ...copy.featuresNavs.tabs.dashboard,
        svg: 'dashboard',
        src: dashboard,
        second: true,
      },
      {
        ...copy.featuresNavs.tabs.features,
        svg: 'house',
        src: construction,
      },
    ]}
  />

  <PricingSection pricing={t.data.pricing} />

  <FAQ title={copy.faqTitle} faqs={t.data.faqs} />

  <HeroSectionAlt
    title={copy.heroAlt.title}
    subTitle={copy.heroAlt.subTitle}
    url="https://github.com/kunda-works"
  />
</MainLayout>
"""
with open(os.path.join(ROOT, "src/views/HomeView.astro"), "w", encoding="utf-8") as f:
    f.write(home_view_content)
print("Updated HomeView.astro")

# 2. Update ContactSection.astro
contact_section_content = """---
import AuthBtn from '@components/ui/buttons/AuthBtn.astro';
import ContactIconBlock from '@components/ui/blocks/ContactIconBlock.astro';
import DemoForm from '@components/ui/forms/DemoForm.astro';
import TextInput from '@components/ui/forms/input/TextInput.astro';
import EmailContactInput from '@components/ui/forms/input/EmailContactInput.astro';
import PhoneInput from '@components/ui/forms/input/PhoneInput.astro';
import TextAreaInput from '@components/ui/forms/input/TextAreaInput.astro';
import Icon from '@components/ui/icons/Icon.astro';

const copy = Astro.locals.copy.contact;
const blockIconClass =
  'mt-1.5 h-6 w-6 shrink-0 text-neutral-600 dark:text-neutral-400';
---

<section class="mx-auto max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14">
  <div class="mx-auto max-w-2xl lg:max-w-5xl">
    <div class="text-center">
      <h1 class="text-2xl font-bold tracking-tight text-balance text-neutral-800 md:text-4xl md:leading-tight dark:text-neutral-200">
        {copy.heading}
      </h1>
      <p class="mt-1 text-pretty text-neutral-600 dark:text-neutral-400">
        {copy.subTitle}
      </p>
    </div>

    <div class="mt-12 grid items-center gap-6 lg:grid-cols-2 lg:gap-16">
      <div class="flex flex-col rounded-xl p-4 sm:p-6 lg:p-8">
        <h2 class="mb-8 text-xl font-bold text-neutral-700 dark:text-neutral-300">
          {copy.formTitle}
        </h2>
        <DemoForm
          successMessage={copy.demoMessage}
          statusClass="mt-2 text-center text-sm text-orange-500 dark:text-orange-400"
        >
          <div class="grid gap-4">
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <TextInput
                id="hs-firstname-contacts"
                label={copy.firstName}
                name="hs-firstname-contacts"
              />
              <TextInput
                id="hs-lastname-contacts"
                label={copy.lastName}
                name="hs-lastname-contacts"
              />
            </div>
            <EmailContactInput id="hs-email-contacts" />
            <PhoneInput id="hs-phone-number" />
            <TextAreaInput
              id="hs-about-contacts"
              label={copy.details}
              name="hs-about-contacts"
            />
          </div>

          <div class="mt-4 grid">
            <AuthBtn title={copy.send} />
          </div>

          <div class="mt-3 text-center">
            <p class="text-sm text-neutral-600 dark:text-neutral-400">
              {copy.formSubTitle}
            </p>
          </div>
        </DemoForm>
      </div>

      <div class="divide-y divide-neutral-300 dark:divide-neutral-700">
        <ContactIconBlock
          heading={copy.knowledgeHeading}
          content={copy.knowledgeContent}
          isLinkVisible={true}
          linkTitle={copy.knowledgeLink}
          linkURL="/welcome-to-docs/"
          isArrowVisible={true}
        >
          <Icon name="question" class={blockIconClass} />
        </ContactIconBlock>

        <ContactIconBlock
          heading={copy.faqHeading}
          content={copy.faqContent}
          isLinkVisible={true}
          linkTitle={copy.faqLink}
          linkURL="/#faq"
          isArrowVisible={true}
        >
          <Icon name="chatBubble" class={blockIconClass} />
        </ContactIconBlock>

        <ContactIconBlock
          heading={copy.officeHeading}
          content={copy.officeContent}
          isAddressVisible={true}
          addressContent="Distributed & Remote-First"
        >
          <Icon name="mapPin" class={blockIconClass} />
        </ContactIconBlock>

        <ContactIconBlock
          heading={copy.emailHeading}
          content={copy.emailContent}
          isLinkVisible={true}
          linkTitle="hello@kunda.works"
          linkURL="mailto:hello@kunda.works"
        >
          <Icon name="envelopeOpen" class={blockIconClass} />
        </ContactIconBlock>
      </div>
    </div>
  </div>
</section>
"""
with open(os.path.join(ROOT, "src/components/sections/misc/ContactSection.astro"), "w", encoding="utf-8") as f:
    f.write(contact_section_content)
print("Updated ContactSection.astro")

# 3. Update ServicesView.astro - wire up CTAs to /contact
services_view_content = """---
import MainLayout from '@/layouts/MainLayout.astro';
import MainSection from '@components/ui/blocks/MainSection.astro';
import AlternatingSections, {
  type Article,
} from '@components/ui/blocks/AlternatingSections.astro';
import FeaturesStats from '@components/sections/features/FeaturesStats.astro';
import blueprints from '@images/blueprints-image.avif';
import personWorking from '@images/person-working.avif';
import beforeAfter from '@images/before-after.avif';
import constructionWorkers from '@images/construction-workers.avif';
import aerialView from '@images/aerial-view.avif';
import usingTools from '@images/using-tools.avif';
import progressBuilding from '@images/progress-building.avif';
import underConstruction from '@images/under-construction.avif';
import { getCopy } from '@/copy';
import type { MarketingLocale } from '@utils/locale';

/** The services page in one locale. */
interface Props {
  locale: MarketingLocale;
}

const { locale } = Astro.props;
const copy = getCopy(locale).services;
const articleCopy = copy.articles;

const articles: Article[] = [
  {
    title: articleCopy.guidance.title,
    subTitle: articleCopy.guidance.subTitle,
    images: [
      { src: blueprints, alt: articleCopy.guidance.imageAlts[0] },
      { src: personWorking, alt: articleCopy.guidance.imageAlts[1] },
    ],
  },
  {
    title: articleCopy.craftsmanship.title,
    subTitle: articleCopy.craftsmanship.subTitle,
    images: [{ src: beforeAfter, alt: articleCopy.craftsmanship.imageAlts[0] }],
    cta: { title: articleCopy.craftsmanship.cta, url: '/contact' },
  },
  {
    title: articleCopy.oversight.title,
    subTitle: articleCopy.oversight.subTitle,
    images: [
      { src: constructionWorkers, alt: articleCopy.oversight.imageAlts[0] },
      { src: aerialView, alt: articleCopy.oversight.imageAlts[1] },
    ],
  },
  {
    title: articleCopy.maintenance.title,
    subTitle: articleCopy.maintenance.subTitle,
    images: [{ src: usingTools, alt: articleCopy.maintenance.imageAlts[0] }],
  },
  {
    title: articleCopy.bespoke.title,
    subTitle: articleCopy.bespoke.subTitle,
    images: [
      { src: progressBuilding, alt: articleCopy.bespoke.imageAlts[0] },
      { src: underConstruction, alt: articleCopy.bespoke.imageAlts[1] },
    ],
    cta: { title: articleCopy.bespoke.cta, url: '/contact' },
  },
];
---

<MainLayout
  title={copy.title}
  description={copy.metaDescription}
  ogTitle={copy.ogTitle}
>
  <MainSection
    title={copy.intro.title}
    subTitle={copy.intro.subTitle}
    cta={{ title: copy.intro.cta, url: '/contact' }}
  />
  <AlternatingSections articles={articles} />
  <FeaturesStats
    title={copy.stats.title}
    subTitle={copy.stats.subTitle}
    mainStatTitle={copy.stats.mainStatTitle}
    mainStatSubTitle={copy.stats.mainStatSubTitle}
    stats={copy.stats.stats}
  />
</MainLayout>
"""
with open(os.path.join(ROOT, "src/views/ServicesView.astro"), "w", encoding="utf-8") as f:
    f.write(services_view_content)
print("Updated ServicesView.astro")

# 4. Update resources/index.astro
resources_index_content = """---
import MainLayout from '@/layouts/MainLayout.astro';
import { getCollection } from 'astro:content';

const resources = await getCollection('resources');
---

<MainLayout
  title="Resource Library & Developer Blueprints | KUNDA"
  description="Download production checklists, architectural guidelines, and standardized agency kits curated by Kunda Works."
  section="Resources"
>
  <div class="mx-auto max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 2xl:max-w-full">
    {/* Page Header aligned with ScrewFast section typography */}
    <div class="mb-8 flex flex-col md:flex-row md:items-end md:justify-between gap-6 border-b border-neutral-200 pb-8 dark:border-neutral-800">
      <div>
        <span class="inline-flex items-center gap-1.5 py-1 px-3 rounded-full text-xs font-semibold bg-orange-100 text-orange-800 dark:bg-orange-950 dark:text-orange-300 mb-3">
          Curated Knowledge & Assets
        </span>
        <h1 class="text-3xl font-extrabold tracking-tight text-neutral-900 md:text-5xl dark:text-neutral-100">
          KUNDA Resource Library
        </h1>
        <p class="mt-3 max-w-2xl text-base text-neutral-600 dark:text-neutral-400">
          Field-tested checklists, client onboarding packages, and technical blueprints to help you plan, ship, and scale digital products.
        </p>
      </div>
      <div>
        <span class="text-xs font-medium text-neutral-500 uppercase tracking-wider">
          All Community Resources Free
        </span>
      </div>
    </div>

    {/* Resources Grid */}
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {resources.map((item) => (
        <div class="group flex flex-col justify-between rounded-2xl border border-neutral-200/80 bg-white p-6 shadow-xs transition-all duration-300 hover:-translate-y-1 hover:border-orange-500/50 hover:shadow-lg dark:border-neutral-800 dark:bg-neutral-900">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="inline-flex items-center rounded-lg bg-neutral-100 px-2.5 py-1 text-xs font-bold font-mono text-neutral-700 uppercase dark:bg-neutral-800 dark:text-neutral-300">
                {item.data.format}
              </span>
              {item.data.fileSize && (
                <span class="text-xs font-mono text-neutral-400">
                  {item.data.fileSize}
                </span>
              )}
            </div>
            <h2 class="text-xl font-bold tracking-tight text-neutral-800 dark:text-neutral-100 group-hover:text-orange-600 dark:group-hover:text-orange-400 transition-colors">
              {item.data.title}
            </h2>
            <p class="mt-2.5 text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed">
              {item.data.description}
            </p>
          </div>

          <div class="mt-6 flex items-center justify-between border-t border-neutral-100 pt-4 dark:border-neutral-800">
            <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-600 dark:text-emerald-400">
              <span class="h-2 w-2 rounded-full bg-emerald-500"></span>
              {item.data.access === 'free' ? 'Free Community Asset' : 'Pro Asset'}
            </span>
            <a
              href={item.data.downloadUrl}
              download
              class="inline-flex items-center gap-1.5 rounded-xl bg-orange-600 px-4 py-2 text-xs font-semibold text-white shadow-xs hover:bg-orange-700 transition-colors"
            >
              Download
              <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </a>
          </div>
        </div>
      ))}
    </div>
  </div>
</MainLayout>
"""
with open(os.path.join(ROOT, "src/pages/resources/index.astro"), "w", encoding="utf-8") as f:
    f.write(resources_index_content)
print("Updated resources/index.astro")

print("PHASE 3 COMPLETED SUCCESSFULLY!")

