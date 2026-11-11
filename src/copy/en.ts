import faqs from '@data/faqs.json';
import features from '@data/features.json';
import pricing from '@data/pricing.json';

/**
 * English copy table. This file defines the shape every other locale must
 * satisfy (see `Copy` in `./index.ts`), so a missing translation fails
 * `astro check` instead of leaking English onto a localised page.
 *
 * Paths are unlocalised (`/products`, not `/fr/products`); callers run them
 * through `localePath()` from `@utils/locale`.
 */
export const en = {
  site: {
    /** Default `<meta name="description">` when a page sets none. */
    description:
      'Kunda brings useful digital products and ideas together in one connected ecosystem: software applications, practical online tools, learning resources, and guides. One home. Many useful possibilities.',
    /** schema.org `WebSite.description` in every page's `isPartOf`. */
    descriptionShort:
      'A home for useful digital things. Software, tools, knowledge, and digital resources.',
    ogTitle: 'KUNDA — A home for useful digital things',
    ogDescription:
      "Kunda is an independent digital product company building a connected ecosystem of software, online tools, knowledge and resources. One home. Many useful possibilities.",
  },

  layout: {
    skipToContent: 'Skip to content',
    changeLanguage: 'Change language',
    toggleNavigation: 'Toggle navigation',
    darkTheme: 'Dark Theme Toggle',
    lightTheme: 'Light Theme Toggle',
    toggleTheme: 'Toggle theme',
  },

  nav: {
    /** Labels for `navLinks` in `@data/navigation`, keyed by id. */
    labels: {
      home: 'Home',
      products: 'Products',
      'micro-saas': 'Micro-SaaS',
      tools: 'Tools',
      blog: 'Journal',
      resources: 'Resources',
      services: 'Services',
      contact: 'Contact',
    },
    footer: {
      /** Section titles and link labels for `footerSections` in `@data/navigation`, keyed by id. */
      sectionTitles: {
        ecosystem: 'Ecosystem',
        company: 'Company',
      },
      links: {
        documentation: 'Documentation',
        tools: 'Free Tools',
        products: 'Software & Apps',
        resources: 'Resources & Downloads',
        services: 'Services',
        about: 'About Kunda',
        blog: 'Journal & Insights',
        careers: 'Careers',
        customers: 'Customers',
      },
      hiringBadge: "We're hiring!",
      stayUpToDate: 'Stay up to date',
      stayUpToDateContent:
        'Stay updated with the latest tools and exclusive deals.',
      craftedBy: 'Crafted by',
      newsletterDemoMessage:
        'Thanks! (Demo only — wire an email service to collect real subscribers.)',
    },
    /** Text for the optional mega menu (`@data/mega_link`). */
    megaMenu: {
      services: {
        guides: {
          title: 'Explore Advice and Explanations',
          description:
            "Dive deep into helpful guides and explanations for all of KUNDA's products and tools",
        },
        integrations: {
          title: 'Discover Integrations',
          description:
            'Supercharge Your Workflow. Seamless integrations with all your favorite tools',
        },
        experts: {
          title: 'Expert Services',
          description: "Go beyond tools with KUNDA's expert digital services",
        },
        tools: {
          title: 'Cutting-Edge Tools',
          description:
            "Build Smarter, Faster. Discover KUNDA's growing suite of digital tools and utilities",
        },
        plans: {
          title: 'Simple Plans',
          description:
            "Boost your efficiency with KUNDA's straightforward, value-driven digital plans",
        },
        community: {
          title: 'Community Forum',
          description: 'Learn, share, and connect with other KUNDA users',
        },
      },
      successStories: 'Success Stories',
      successStory: {
        description:
          'See how KUNDA has empowered builders and creators to work smarter and ship faster.',
        imageAlt: 'Portrait of a smiling person',
      },
      learnMore: 'Learn more',
    },
  },

  forms: {
    email: 'Email',
    emailAddress: 'Email address',
    emailPlaceholder: 'Enter your email',
    emailInvalid:
      'Please include a valid email address so we can get back to you',
    subscribe: 'Subscribe',
    phone: 'Phone Number',
    password: 'Password',
    confirmPassword: 'Confirm Password',
    forgotPassword: 'Forgot password?',
    passwordHint: '8+ characters required',
    passwordMismatch: 'Password does not match the password',
    rememberMe: 'Remember me',
    acceptTerms: 'I accept the ',
    termsAndConditions: 'Terms and Conditions',
    or: 'Or',
    demoFallbackMessage: 'Demo only — this form is not connected to a backend.',
  },

  auth: {
    logIn: 'Log in',
    signIn: 'Sign in',
    signUp: 'Sign up',
    signInWithGoogle: 'Sign in with Google',
    signUpWithGoogle: 'Sign up with Google',
    noAccountYet: "Don't have an account yet?",
    signUpHere: 'Sign up here',
    alreadyHaveAccount: 'Already have an account?',
    signInHere: 'Sign in here',
    forgotPasswordTitle: 'Forgot password?',
    rememberYourPassword: 'Remember your password?',
    resetPassword: 'Reset password',
    credentialsDemoNotice:
      'Demo only – connect a real auth provider before collecting credentials.',
    recoveryDemoNotice:
      'Demo only – password recovery is not connected to a backend.',
    signInDemoMessage: 'Demo only – sign-in is not connected to a backend.',
    registerDemoMessage:
      'Demo only – registration is not connected to a backend.',
    recoverDemoMessage:
      'Demo only – password recovery is not connected to a backend.',
  },

  share: {
    share: 'Share',
    shareOn: (platform: string) => `Share on ${platform}`,
    copied: 'Copied',
    copyLink: 'Copy link',
  },

  banner: {
    dismiss: 'Dismiss',
    region: 'Informational banner',
  },

  blog: {
    readMore: 'Read More',
    minRead: (minutes: number) => `${minutes} min read`,
    relatedArticles: 'Related articles',
    wasHelpful: 'Was this post helpful?',
    yes: 'Yes',
    no: 'No',
    ogSection: 'Blog',
  },

  insights: {
    readMore: 'Read more',
    tableOfContents: 'Table of Contents:',
    ogSection: 'Insights',
  },

  products: {
    ogSection: 'Products',
    tabs: 'Tabs',
  },

  notFound: {
    title: 'Page Not Found',
    subTitle: "Oops, this isn't the tool you were looking for!",
    content:
      "Don't let this hiccup slow you down. Let's get you back to building your masterpiece.",
    goHome: 'Go Home',
    goBack: 'Go Back',
  },

  home: {
    banner: 'Welcome to KUNDA — Discover Our Ecosystem',
    hero: {
      title:
        'A home for <span class="text-orange-500 dark:text-orange-400">useful digital things</span>',
      subTitle:
        'Software, tools, resources and ideas designed to help you work smarter, create more and solve everyday problems.',
      primaryBtn: 'Explore Products',
      secondaryBtn: 'Discover Free Tools',
      rating: '<span class="font-bold">4.8</span> / 5',
      reviews: 'From Over <span class="font-bold">12.8k</span> Reviews',
      imageAlt:
        'Abstract geometric shapes representing the KUNDA digital ecosystem',
    },
    clients: {
      title: 'Trusted by Industry Leaders',
      subTitle: 'Experience the reliability chosen by industry giants.',
    },
    featuresGeneral: {
      title: 'Meeting Industry Demands',
      subTitle:
        "At KUNDA, we build practical digital tools, resources and software for people who make things online. Whether you're a developer, designer, or founder — we're here to help you work smarter.",
      imageAlt: 'KUNDA product ecosystem diagram',
    },
    featuresNavs: {
      title:
        'Explore <span class="text-orange-500 dark:text-orange-400">KUNDA</span>\'s ecosystem — tools, resources and software built for digital makers.',
      tabs: {
        tools: {
          heading: 'Cutting-Edge Tools',
          content:
            "Empower your work with KUNDA's free digital tools. Instant access to JSON formatting, password analysis, QR generation, and more — all client-side, all free.",
          alt: 'Screenshot of KUNDA free tools interface',
        },
        dashboard: {
          heading: 'Intuitive Dashboards',
          content:
            "Navigate your KUNDA dashboard with ease. Manage subscriptions, track usage, and access all your digital products from one central workspace.",
          alt: 'A screenshot or graphic representation of the intuitive dashboard',
        },
        features: {
          heading: 'Robust Features',
          content:
            "Minimize complexity, maximize productivity. KUNDA's ecosystem is designed to remove friction from your digital workflow — from idea to launch.",
          alt: 'Screenshot of a KUNDA product features overview',
        },
      },
    },
    testimonials: {
      title: 'Loved by Digital Makers',
      subTitle:
        'At KUNDA, we design for speed and simplicity. Set up in seconds, not hours.',
      quotes: [
        {
          content:
            'KUNDA\'s free tools have become a daily staple for our team. The JSON Formatter alone saves us hours each week. Clean, fast, no nonsense.',
          author: 'Maya Chen',
          role: 'Lead Developer | Stackbloom',
        },
      ],
      statistics: [
        {
          count: '70k+',
          description:
            'developers, designers and founders using KUNDA tools monthly',
        },
        {
          count: '35%',
          description:
            'faster workflow reported by teams using KUNDA free tools',
        },
        {
          count: '15.3%',
          description:
            'of KUNDA tools require zero sign-up to use',
        },
        {
          count: '2x',
          description: 'more resources added each quarter to the KUNDA library',
        },
      ],
    },
    faqTitle: 'Frequently<br />asked questions',
    heroAlt: {
      title: "Let's Build Together",
      subTitle:
        'KUNDA is built with Astro, Tailwind CSS, and deployed on Cloudflare. Explore the ecosystem and find your next useful tool.',
      btn: 'Explore KUNDA on GitHub',
    },
  },

  services: {
    title: 'Services',
    metaDescription:
      'KUNDA provides expert digital consulting, product strategy and technical services for founders and teams building digital products.',
    ogTitle: 'Expert Digital Services | KUNDA',
    intro: {
      title: 'Uniting Expertise with Your Vision',
      subTitle:
        'At KUNDA, we provide comprehensive digital solutions and expert guidance for builders of digital products. Our experienced team is dedicated to supporting your project from concept to launch with a range of specialized services.',
      cta: 'Schedule a Consultation',
    },
    articles: {
      guidance: {
        title: 'Delivering Expert Guidance',
        subTitle:
          'Launching a digital product can be overwhelming. With our professional consultation services, we guide you through every stage — from product definition and technical architecture to go-to-market strategy. Our experts provide tailored advice on tool selection, scope definition, and best practices.',
        imageAlts: [
          'Digital wireframes and product architecture diagrams',
          'Person working in the office',
        ],
      },
      craftsmanship: {
        title: 'Transforming Designs into Reality',
        subTitle:
          'Our skilled engineers and designers bring precision and care to every digital project. From landing pages to full-stack applications, KUNDA delivers polished digital products that meet the highest standards of performance, accessibility and security.',
        imageAlts: ['Digital product concept and finished user interface'],
        cta: 'Learn More',
      },
      oversight: {
        title: 'Navigating Projects with Professional Oversight',
        subTitle:
          'Effective project management is at the heart of any successful digital launch. KUNDA provides thorough planning and delivery management that keeps your project on time and within budget. We handle workflow coordination, technical oversight, and stakeholder communication while you focus on your vision.',
        imageAlts: [
          'Product team collaborating in modern software workspace',
          'Digital infrastructure deployment monitor',
        ],
      },
      maintenance: {
        title: 'Ensuring Long-lasting Performance',
        subTitle:
          "Our commitment to your project doesn't end at launch. KUNDA offers ongoing maintenance and support services to ensure your digital product's longevity and performance. From routine updates to incident response, our responsive team is there to provide seamless support.",
        imageAlts: [
          'Developer testing client-side web application in browser',
        ],
      },
      bespoke: {
        title: 'Crafting Bespoke Strategies for Unique Challenges',
        subTitle:
          'For our larger clients, KUNDA offers custom digital solutions designed to meet specific business challenges. By understanding your unique needs, we engineer tailored strategies aimed at optimizing your operations, enhancing efficiency, and driving your business forward.',
        imageAlts: [
          'Software application architecture in development',
          'Cloud infrastructure console and metrics view',
        ],
        cta: 'Read more',
      },
    },
    stats: {
      title: 'Ecosystem Architecture',
      subTitle:
        'KUNDA products run on high-performance cloud infrastructure designed for maximum uptime and minimal footprint.',
      mainStatTitle: '100%',
      mainStatSubTitle:
        'Client-side privacy on our flagship developer utilities',
      stats: [
        { stat: '<50ms', description: 'Global edge response latency' },
        { stat: '0', description: 'Third-party tracking scripts' },
        { stat: '99.9%', description: 'Serverless platform uptime' },
      ],
    },
  },

  contact: {
    title: 'Contact',
    metaDescription:
      "Have questions or want to discuss a project? Reach out, and let's craft the perfect solution with our tools and services.",
    ogTitle: 'Contact KUNDA | Digital Product Ecosystem',
    heading: 'Contact us',
    subTitle:
      "Have questions or want to discuss a project? Reach out, and let's craft the perfect solution with our tools and services.",
    formTitle: 'Fill in the form below',
    formSubTitle: "We'll get back to you in 1-2 business days.",
    firstName: 'First Name',
    lastName: 'Last Name',
    details: 'Details',
    send: 'Send Message',
    demoMessage:
      'Thanks! (Demo only — wire a form endpoint to receive real messages.)',
    knowledgeHeading: 'Knowledgebase',
    knowledgeContent: 'Browse through all of our knowledgebase articles.',
    knowledgeLink: 'Visit guides & tutorials',
    faqHeading: 'FAQ',
    faqContent: 'Explore our FAQ for quick, clear answers to common queries.',
    faqLink: 'Visit FAQ',
    officeHeading: 'Visit our office',
    officeContent: 'KUNDA Digital Headquarters',
    emailHeading: 'Contact us by email',
    emailContent: 'Prefer the written word? Drop us an email at',
  },

  blogIndex: {
    title: 'Blog',
    metaDescription:
      "Stay up-to-date with software engineering, micro-SaaS architecture, and web tools from the KUNDA team.",
    ogTitle: 'Journal & Insights | KUNDA',
    heading: 'Notes on Software, Tools, and Digital Products',
    subTitle:
      'Practical essays, architecture guides, and technical tutorials for founders and developers building useful digital things.',
    insightsHeading: 'Insights',
    insightsSubTitle:
      'Perspectives on software sustainability, browser-first tools, and lightweight cloud architecture.',
    noPosts: 'No blog posts yet. Check back soon.',
    noInsights: 'No insights yet. Check back soon.',
  },

  productsIndex: {
    title: 'Products',
    metaDescription:
      'Discover KUNDA software applications, micro-SaaS utilities, and developer tools built for speed and simplicity.',
    ogTitle: 'Software & Micro-SaaS Products | KUNDA',
    heading: 'Products & Micro-SaaS',
    subTitle:
      'Focused software products engineered to eliminate operational friction without enterprise complexity. Built with modern web standards and lightweight cloud infrastructure.',
    customerStories: 'Customer Stories',
    testimonials: {
      title: 'Built for Builders',
      quotes: [
        {
          content:
            'KUNDA tools and resources have removed weeks of boilerplate from our product development cycle. Clean, focused, and immediately useful.',
          author: 'Alex Morgan',
          avatarAlt: 'Image Description',
        },
        {
          content:
            'Having truly client-side tools like the JSON Formatter and Password Analyzer means our engineering team can safely handle data without compliance anxiety.',
          author: 'Elena Rostova',
          avatarAlt: 'Image Description',
        },
        {
          content:
            'The Micro-SaaS directory showcases exactly what indie software should look like: clean, fast, and solving real operational headaches.',
          author: 'Marcus Vance',
          avatarAlt: 'Image Description',
        },
      ],
    },
    stats: {
      title: 'Why KUNDA Products?',
      subTitle:
        'Every application in our ecosystem is designed with strict principles: zero unnecessary dependencies, deterministic execution, and respectful data privacy.',
      benefits: [
        'Fast, lightweight serverless architecture deployed at the global edge.',
        'Browser-first privacy protecting sensitive user data.',
        'Honest pricing with generous free tiers for developers and small teams.',
      ],
    },
  },

  /** Locale-specific JSON data (already the good pattern; kept as-is). */
  data: { faqs, features, pricing },
};
