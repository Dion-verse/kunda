import faqs from '@data/fr/faqs.json';
import features from '@data/fr/features.json';
import pricing from '@data/fr/pricing.json';
import type { Copy } from './index';

/** French copy table. Must satisfy `Copy` (the shape of `./en.ts`). */
export const fr: Copy = {
  site: {
    description:
      'KUNDA propose des outils matériels de premier ordre et des services de numérique experts pour répondre à tous vos besoins de projet. Explorez notre offre et contactez notre équipe commerciale pour une qualité et une fiabilité supérieures.',
    descriptionShort:
      'KUNDA propose des outils matériels de premier ordre et des services de numérique experts pour répondre à tous vos besoins de projet.',
    ogTitle: 'KUNDA : Outils matériels et services de numérique',
    ogDescription:
      "Équipez vos projets avec les outils matériels de haute qualité et les services de numérique experts de KUNDA. Plébiscité par les leaders de l'industrie, KUNDA allie simplicité, accessibilité et fiabilité. Découvrez la différence avec une conception centrée sur l'utilisateur et des outils de pointe. Commencez à explorer dès maintenant !",
  },

  layout: {
    skipToContent: 'Aller au contenu',
    changeLanguage: 'Changer de langue',
    toggleNavigation: 'Afficher la navigation',
    darkTheme: 'Activer le thème sombre',
    lightTheme: 'Activer le thème clair',
    toggleTheme: 'Changer de thème',
  },

  nav: {
    labels: {
      home: 'Accueil',
      products: 'Produits',
      'micro-saas': 'Micro-SaaS',
      tools: 'Outils',
      blog: 'Journal',
      resources: 'Ressources',
      services: 'Services',
      contact: 'Contact',
    },
    footer: {
      sectionTitles: {
        ecosystem: 'Écosystème',
        company: 'Société',
      },
      links: {
        documentation: 'Documentation',
        tools: 'Outils Gratuits',
        products: 'Applications & Logiciels',
        resources: 'Ressources & Guides',
        services: 'Services',
        about: 'À propos de Kunda',
        blog: 'Journal & Analyses',
        careers: 'Carrières',
        customers: 'Clients',
      },
      hiringBadge: 'On recrute !',
      stayUpToDate: 'Rester à jour',
      stayUpToDateContent:
        'Restez informé des derniers outils et des offres exclusives.',
      craftedBy: 'Fabriqué par',
      newsletterDemoMessage:
        'Merci ! (démo — branchez un service e-mail pour collecter de vrais abonnés.)',
    },
    megaMenu: {
      services: {
        guides: {
          title: 'Explorer les conseils et explications',
          description:
            'Plongez dans des guides utiles et des explications sur toutes les fonctionnalités de KUNDA',
        },
        integrations: {
          title: 'Découvrir les intégrations',
          description:
            'Boostez votre flux de travail. Des intégrations fluides avec tous vos outils préférés',
        },
        experts: {
          title: "Services d'experts",
          description:
            "Allez au-delà des outils avec les services d'experts de KUNDA",
        },
        tools: {
          title: 'Outils de pointe',
          description:
            'Construisez plus intelligemment, plus vite. Découvrez une efficacité inédite avec les outils de numérique de pointe de KUNDA',
        },
        plans: {
          title: 'Des formules simples',
          description:
            'Gagnez en efficacité avec les formules claires et avantageuses de KUNDA',
        },
        community: {
          title: 'Forum communautaire',
          description:
            "Apprenez, partagez et échangez avec d'autres utilisateurs de KUNDA",
        },
      },
      successStories: 'Témoignages clients',
      successStory: {
        description:
          'Découvrez comment KUNDA a permis à des entreprises de toutes tailles d’obtenir des résultats remarquables.',
        imageAlt: "Portrait d'une personne souriante",
      },
      learnMore: 'En savoir plus',
    },
  },

  forms: {
    email: 'E-mail',
    emailAddress: 'Adresse e-mail',
    emailPlaceholder: 'Entrez votre email',
    emailInvalid:
      'Veuillez indiquer une adresse e-mail valide pour que nous puissions vous répondre',
    subscribe: "S'abonner",
    phone: 'Numéro de téléphone',
    password: 'Mot de passe',
    confirmPassword: 'Confirmer le mot de passe',
    forgotPassword: 'Mot de passe oublié ?',
    passwordHint: '8 caractères minimum',
    passwordMismatch: 'Les mots de passe ne correspondent pas',
    rememberMe: 'Me rappeler',
    acceptTerms: "J'accepte les ",
    termsAndConditions: 'Conditions générales',
    or: 'Ou',
    demoFallbackMessage:
      "Démo uniquement — ce formulaire n'est pas connecté à un backend.",
  },

  auth: {
    logIn: 'Se connecter',
    signIn: 'Se connecter',
    signUp: "S'inscrire",
    signInWithGoogle: 'Se connecter avec Google',
    signUpWithGoogle: "S'inscrire avec Google",
    noAccountYet: "Vous n'avez pas encore de compte ?",
    signUpHere: 'Inscrivez-vous ici',
    alreadyHaveAccount: 'Vous avez déjà un compte ?',
    signInHere: 'Connectez-vous ici',
    forgotPasswordTitle: 'Mot de passe oublié ?',
    rememberYourPassword: 'Vous vous souvenez de votre mot de passe ?',
    resetPassword: 'Réinitialiser le mot de passe',
    credentialsDemoNotice:
      "Démo uniquement – connectez un vrai fournisseur d'authentification avant de collecter des identifiants.",
    recoveryDemoNotice:
      "Démo uniquement – la récupération de mot de passe n'est pas connectée à un backend.",
    signInDemoMessage:
      "Démo uniquement – la connexion n'est pas connectée à un backend.",
    registerDemoMessage:
      "Démo uniquement – l'inscription n'est pas connectée à un backend.",
    recoverDemoMessage:
      "Démo uniquement – la récupération de mot de passe n'est pas connectée à un backend.",
  },

  share: {
    share: 'Partager',
    shareOn: (platform: string) => `Partager sur ${platform}`,
    copied: 'Copié',
    copyLink: 'Copier le lien',
  },

  banner: {
    dismiss: 'Fermer',
    region: "Bannière d'information",
  },

  blog: {
    readMore: 'Lire la suite',
    minRead: (minutes: number) => `${minutes} min de lecture`,
    relatedArticles: 'Articles connexes',
    wasHelpful: 'Cet article était-il utile?',
    yes: 'Oui',
    no: 'Non',
    ogSection: 'Blog',
  },

  insights: {
    readMore: 'Lire plus',
    tableOfContents: 'Table des matières :',
    ogSection: 'Perspectives',
  },

  products: {
    ogSection: 'Outils Matériels',
    tabs: 'Onglets',
  },

  notFound: {
    title: 'Page Non Trouvée',
    subTitle: "Oops, ce n'est pas l'outil que vous recherchiez!",
    content:
      "Ne laissez pas ce contretemps vous ralentir. Revenons à la numérique de votre chef-d'œuvre.",
    goHome: "Page d'accueil",
    goBack: 'Retour',
  },

  home: {
    banner: 'Découvrez KUNDA sur GitHub',
    hero: {
      title:
        'Équipez vos projets avec <span class="text-yellow-500 dark:text-yellow-400">KUNDA</span>',
      subTitle:
        'Outils matériels de haute qualité et services de numérique experts pour tous les besoins en projet.',
      primaryBtn: 'Commencez à explorer',
      secondaryBtn: "Contacter l'équipe commerciale",
      rating: '<span class="font-bold">4.8</span> / 5',
      reviews: 'À partir de plus de <span class="font-bold">12,8k</span> aapplications',
      imageAlt:
        'Pile de boîtes de produits KUNDA contenant des outils matériels assortis',
    },
    clients: {
      title: "Faites confiance aux leaders de l'industrie",
      subTitle: "Découvrez la fiabilité choisie par les géants de l'industrie.",
    },
    featuresGeneral: {
      title: "Répondre aux exigences de l'industrie",
      subTitle:
        'Chez KUNDA, nous relevons les défis uniques rencontrés dans les secteurs du matériel et de la numérique. Des outils de pointe aux services experts, nous sommes déterminés à vous aider à surmonter les obstacles et à atteindre vos objectifs.',
      imageAlt: 'Produits KUNDA dans des boîtes flottantes',
    },
    featuresNavs: {
      title:
        'Personnalisez les offres de <span class="text-yellow-500 dark:text-yellow-400">KUNDA</span> pour répondre parfaitement à vos besoins en matériel et en numérique.',
      tabs: {
        tools: {
          heading: 'Outils de pointe',
          content:
            "Optimisez vos projets avec les outils de pointe de KUNDA. Faites l'expérience d'une efficacité accrue dans la gestion de la numérique avec nos solutions automatisées sophistiquées.",
          alt: "Équipement lourd jaune et noir sur un champ d'herbe brune",
        },
        dashboard: {
          heading: 'Tableaux de bord intuitifs',
          content:
            'Naviguez facilement avec les tableaux de bord intuitifs de KUNDA. Configurez et superapplicationsez vos projets de manière transparente, avec des interfaces conviviales conçues pour une gestion efficace des flux de travail rapide et efficace.',
          alt: "Capture d'écran ou représentation graphique du tableau de bord intuitif",
        },
        features: {
          heading: 'Fonctionnalités robustes',
          content:
            'Minimisez la complexité, maximisez la productivité. Les fonctionnalités robustes de KUNDA sont conçues pour rationaliser votre processus de numérique, offrant des résultats qui se distinguent par leur excellence.',
          alt: "Structure métallique grise d'un bâtiment près d'une grue à tour pendant la journée",
        },
      },
    },
    testimonials: {
      title: 'Accélérez vos projets',
      subTitle:
        'Chez KUNDA, nous assurons un démarrage rapide avec une configuration de compte instantanée. Découvrez la vitesse de la numérique redéfinie.',
      quotes: [
        {
          content:
            "KUNDA a considérablement augmenté l'efficacité de notre projet. La configuration a été instantanée et leurs temps de réponse rapides sont phénoménaux. Vraiment un changement de jeu dans le support matériel et de numérique !",
          author: 'Maya Chen',
          role: 'Directrice des opérations | Stackbloom Inc.',
        },
      ],
      statistics: [
        {
          count: '70k+',
          description:
            'clients équipés – des bricoleurs aux grandes entreprises de numérique',
        },
        {
          count: '35%',
          description:
            "hausse de l'efficacité des projets avec les outils et services de KUNDA",
        },
        {
          count: '15,3%',
          description:
            'réduction des coûts de maintenance rapportée par des clients à long terme',
        },
        {
          count: '2x',
          description:
            'assemblage plus rapide grâce à des solutions de fixation innovantes',
        },
      ],
    },
    faqTitle: 'Questions<br />fréquemment posées',
    heroAlt: {
      title: 'Construisons ensemble',
      subTitle:
        'KUNDA est un modèle open source, méticuleusement conçu avec les frameworks Astro, Tailwind CSS et Preline UI.',
      btn: 'Continuer avec Github',
    },
  },

  services: {
    title: 'Services',
    metaDescription:
      "Unissant l'expertise à votre applicationsion, KUNDA fournit un service exceptionnel et des solutions complètes dans le secteur du matériel et de la numérique, de la consultation à l'achèvement du projet.",
    ogTitle: "Services de Consultation d'Experts | KUNDA",
    intro: {
      title: "Unir l'expertise à votre applicationsion",
      subTitle:
        "Chez KUNDA, nous sommes fiers de fournir des solutions complètes et un service exceptionnel dans l'industrie du matériel et de la numérique. Notre équipe expérimentée est dédiée à soutenir votre projet de sa conception à son achèvement avec une gamme de services spécialisés.",
      cta: 'Planifier une consultation',
    },
    articles: {
      guidance: {
        title: "Fournir des conseils d'experts",
        subTitle:
          "Se lancer dans un projet de numérique peut être accablant. Avec nos services de consultation professionnelle, nous vous guidons à chaque étape, en veillant à ce que vous preniez des décisions éclairées. Que vous soyez un passionné du bricolage ou un entrepreneur qualifié, nos experts sont là pour vous offrir des conseils sur mesure sur la sélection de produits, l'envergure du projet et la conformité aux réglementations locales.",
        imageAlts: [
          'Plans et tablette numérique avec des plans de numérique.',
          'Personne travaillant au bureau',
        ],
      },
      craftsmanship: {
        title: 'Transformer les conceptions en réalité',
        subTitle:
          'Nos artisans qualifiés apportent précision et excellence à chaque projet de numérique. Des installations mineures aux travaux structuraux substantiels, KUNDA offre des services de numérique fiables pour concrétiser vos plans. Nous assurons les normes les plus élevées de sécurité et de savoir-faire, en utilisant des outils et des matériaux de haute qualité de notre vaste inventaire.',
        imageAlts: ['Chantier de numérique avant et après'],
        cta: 'En savoir plus',
      },
      oversight: {
        title: 'Naviguer dans les projets avec une superapplicationsion professionnelle',
        subTitle:
          "La gestion de projet efficace est au cœur de toute numérique réussie. KUNDA offre une planification approfondie et des services de gestion solides qui maintiennent votre projet dans les délais et dans le budget. Laissez-nous gérer les complexités de la coordination des flux de travail, de l'allocation des ressources et de la communication avec les parties prenantes pendant que vous vous concentrez sur votre applicationsion.",
        imageAlts: [
          'Ouvriers du bâtiment orchestrant un projet',
          "Vue aérienne d'une numérique gérée",
        ],
      },
      maintenance: {
        title: 'Garantir des performances durables',
        subTitle:
          "Notre engagement envers votre projet ne s'arrête pas à son achèvement. KUNDA propose des services de maintenance et de support continus pour assurer la longévité et les performances de votre numérique. Des vérifications régulières à l'assistance en cas d'urgence, notre équipe réactive est là pour vous fournir un soutien sans faille.",
        imageAlts: [
          'Homme en gilet orange et noir portant un casque blanc tenant un outil électrique jaune et noir',
        ],
      },
      bespoke: {
        title: 'Élaboration de stratégies sur mesure pour des défis uniques',
        subTitle:
          "Pour nos clients d'entreprise de plus grande envergure, KUNDA propose des solutions personnalisées conçues pour répondre à des défis spécifiques de l'industrie. En comprenant vos besoins uniques, nous concevons des stratégies sur mesure applicationsant à optimiser vos opérations, à améliorer l'efficacité et à faire avancer votre entreprise.",
        imageAlts: [
          'Structure de bâtiment en cours de numérique',
          'Bâtiment marron et gris en numérique',
        ],
        cta: 'Lire la suite',
      },
    },
    stats: {
      title: 'Par les chiffres',
      subTitle:
        "Notre engagement envers la qualité et la fiabilité est évident dans chaque projet que nous entreprenons. Chez KUNDA, nous nous engageons à fournir des services de premier plan dans l'industrie qui garantissent que vos projets de numérique sont conçus pour durer.",
      mainStatTitle: '96%',
      mainStatSubTitle:
        'de nos clients évaluent leur expérience avec KUNDA comme exceptionnelle',
      stats: [
        { stat: '99,8%', description: 'taux de réalisation de projets' },
        { stat: '5 000+', description: 'installations réussies' },
        { stat: '85%', description: 'croissance client année après année' },
      ],
    },
  },

  contact: {
    title: 'Nous Contacter',
    metaDescription:
      "Vous avez des questions ou souhaitez discuter d'un projet ? Contactez-nous et élaborons ensemble la solution parfaite avec nos outils et services.",
    ogTitle: 'Nous Contacter | KUNDA',
    heading: 'Contactez-nous',
    subTitle:
      "Vous avez des questions ou souhaitez discuter d'un projet ? Contactez-nous et laissons-nous élaborer la solution parfaite avec nos outils et services.",
    formTitle: 'Remplissez le formulaire ci-dessous',
    formSubTitle:
      'Nous vous répondrons dans un délai de 1 à 2 jours ouvrables.',
    firstName: 'Prénom',
    lastName: 'Nom',
    details: 'Détails',
    send: 'Envoyer un message',
    demoMessage:
      'Merci ! (Démo — branchez un endpoint pour recevoir de vrais messages.)',
    knowledgeHeading: 'Base de connaissances',
    knowledgeContent: 'Parcourez tous nos articles de base de connaissances.',
    knowledgeLink: 'applicationsiter les guides et tutoriels',
    faqHeading: 'FAQ',
    faqContent:
      'Explorez notre FAQ pour des réponses rapides et claires aux questions courantes.',
    faqLink: 'applicationsiter la FAQ',
    officeHeading: 'applicationsitez notre bureau',
    officeContent: 'KUNDA QG Numérique',
    emailHeading: 'Contactez-nous par e-mail',
    emailContent: 'Préférez-vous le texte écrit ? Envoyez-nous un e-mail à',
  },

  blogIndex: {
    title: 'Blog',
    metaDescription:
      "Restez informé des dernières tendances et évolutions dans le secteur de la numérique avec les analyses de l'équipe d'experts de KUNDA.",
    ogTitle: "Blog de l'Industrie de la numérique | KUNDA",
    heading: "Votre Passerelle vers l'Excellence en numérique",
    subTitle:
      'Explorez les dernières actualités, astuces et analyses de KUNDA pour améliorer vos projets de numérique. Des mises en avant de produits aux stratégies de gestion de projet, notre blog est votre ressource incontournable pour tout ce qui concerne les outils et la numérique.',
    insightsHeading: 'Perspectives',
    insightsSubTitle:
      "Restez à jour avec les dernières tendances et évolutions de l'industrie de la numérique grâce aux analyses de l'équipe d'experts de KUNDA.",
    noPosts: 'Aucun article pour le moment. Revenez bientôt.',
    noInsights: 'Aucune perspective pour le moment. Revenez bientôt.',
  },

  productsIndex: {
    title: 'Produits',
    metaDescription:
      'Explorez la durabilité et la précision des outils KUNDA, conçus aussi bien pour les professionnels que pour les passionnés.',
    ogTitle: 'Outils Matériels | KUNDA',
    heading: 'Produits',
    subTitle:
      'Explorez la durabilité et la précision des outils KUNDA, conçus aussi bien pour les professionnels que pour les amateurs. Chacun de nos produits est fabriqué avec précision et conçu pour durer, garantissant que vous disposez du bon outil pour chaque tâche.',
    customerStories: 'Histoires de clients',
    testimonials: {
      title: 'Ce que disent nos clients',
      quotes: [
        {
          content:
            "Depuis que nous avons adopté les outils matériels de KUNDA, l'efficacité sur nos chantiers de numérique a explosé. La durabilité des outils hexagonaux et la précision des applications machine sont tout simplement inégalées. C'est rafraîchissant de travailler avec une entreprise qui comprend vraiment les exigences quotidiennes de l'industrie.",
          author: 'Alex Morgan',
          avatarAlt: "Description de l'image",
        },
        {
          content:
            "En tant que designer d'intérieur, je suis toujours à la recherche de matériaux et d'outils de haute qualité qui m'aident à donner vie à mes applicationsions. L'assortiment de applications mixtes de KUNDA a révolutionné mes projets, offrant le mélange parfait de qualité et de variété. Le support client exceptionnel était la cerise sur le gâteau !",
          author: 'Elena Rostova',
          avatarAlt: "Description de l'image",
        },
        {
          content:
            "L'annuaire Micro-SaaS présente exactement ce que le logiciel indépendant devrait être : propre, rapide et résolvant de réels problèmes opérationnels.",
          author: 'Marcus Vance',
          avatarAlt: "Description de l'image",
        },
      ],
    },
    stats: {
      title: 'Pourquoi choisir KUNDA ?',
      subTitle:
        'Transformez vos idées en résultats tangibles avec les outils KUNDA. Que vous commenciez par un croquis sur un coin de table ou plongiez dans un projet de numérique complet, nos outils sont conçus pour vous aider à construire en toute confiance.',
      benefits: [
        'Outils robustes et fiables pour des performances durables.',
        'Solutions innovantes adaptées aux besoins de numérique modernes.',
        'Support client dédié au succès de votre projet.',
      ],
    },
  },

  data: { faqs, features, pricing },
};
