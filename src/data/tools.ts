/**
 * Central tools manifest — single source of truth for the 48-tool platform.
 * Used by: search index, nav mega-menu, category pages, homepage popular grid.
 * All tools are 100% client-side / browser-based.
 */

export type ToolCategory =
  | 'pdf'
  | 'image'
  | 'text'
  | 'business'
  | 'calculator'
  | 'developer';

export type ToolDifficulty = 'easy' | 'medium' | 'advanced';

export interface Tool {
  slug: string;
  title: string;
  description: string;
  category: ToolCategory;
  icon: string;
  tags: string[];
  featured: boolean;
  popular: boolean;
  difficulty: ToolDifficulty;
  relatedTools?: string[];
  seoTitle?: string;
  seoDescription?: string;
  availability?: 'available' | 'in-development' | 'beta';
  execution?: 'client' | 'external' | 'hybrid';
}

export interface Category {
  id: ToolCategory;
  label: string;
  description: string;
  icon: string;
  color: string;          // Tailwind text color class
  bgColor: string;        // Tailwind bg color class (light)
  darkBgColor: string;    // Tailwind bg color class (dark)
  borderColor: string;    // Tailwind border color class
  toolCount: number;
}

/** Category definitions with consistent design tokens */
export const CATEGORIES: Category[] = [
  {
    id: 'pdf',
    label: 'PDF Tools',
    description: 'Merge, split, compress, convert and manipulate PDF files entirely in your browser.',
    icon: '📄',
    color: 'text-red-600',
    bgColor: 'bg-red-50',
    darkBgColor: 'dark:bg-red-950/30',
    borderColor: 'border-red-200 dark:border-red-900/50',
    toolCount: 8,
  },
  {
    id: 'image',
    label: 'Image Tools',
    description: 'Compress, resize, convert and crop images using the Canvas API — no uploads needed.',
    icon: '🖼️',
    color: 'text-violet-600',
    bgColor: 'bg-violet-50',
    darkBgColor: 'dark:bg-violet-950/30',
    borderColor: 'border-violet-200 dark:border-violet-900/50',
    toolCount: 8,
  },
  {
    id: 'text',
    label: 'Text Tools',
    description: 'Count words, convert case, generate placeholder text, diff and clean up text content.',
    icon: '📝',
    color: 'text-blue-600',
    bgColor: 'bg-blue-50',
    darkBgColor: 'dark:bg-blue-950/30',
    borderColor: 'border-blue-200 dark:border-blue-900/50',
    toolCount: 8,
  },
  {
    id: 'business',
    label: 'Business Tools',
    description: 'Generate invoices, receipts, quotes and payslips as downloadable PDFs instantly.',
    icon: '💼',
    color: 'text-amber-600',
    bgColor: 'bg-amber-50',
    darkBgColor: 'dark:bg-amber-950/30',
    borderColor: 'border-amber-200 dark:border-amber-900/50',
    toolCount: 8,
  },
  {
    id: 'calculator',
    label: 'Calculator Tools',
    description: 'Calculate percentages, loan repayments, BMI, age, currency conversions and more.',
    icon: '🔢',
    color: 'text-teal-600',
    bgColor: 'bg-teal-50',
    darkBgColor: 'dark:bg-teal-950/30',
    borderColor: 'border-teal-200 dark:border-teal-900/50',
    toolCount: 8,
  },
  {
    id: 'developer',
    label: 'Developer Tools',
    description: 'Format JSON, minify CSS/JS, encode URLs and Base64, generate UUIDs, analyze passwords and QR codes.',
    icon: '</>',
    color: 'text-orange-600',
    bgColor: 'bg-orange-50',
    darkBgColor: 'dark:bg-orange-950/30',
    borderColor: 'border-orange-200 dark:border-orange-900/50',
    toolCount: 9,
  },
];

/** Full 48-tool manifest */
export const TOOLS: Tool[] = [
  // ── PDF TOOLS ──────────────────────────────────────────────────────────────
  {
    slug: 'merge-pdf',
    title: 'Merge PDF',
    description: 'Combine multiple PDF files into a single document in seconds.',
    category: 'pdf',
    icon: '📎',
    tags: ['pdf', 'merge', 'combine', 'documents'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['split-pdf', 'compress-pdf'],
  },
  {
    slug: 'split-pdf',
    title: 'Split PDF',
    description: 'Extract individual pages or page ranges from any PDF file.',
    category: 'pdf',
    icon: '✂️',
    tags: ['pdf', 'split', 'extract', 'pages'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['merge-pdf', 'rotate-pdf'],
  },
  {
    slug: 'compress-pdf',
    title: 'Compress PDF',
    description: 'Reduce PDF file size without losing visible quality.',
    category: 'pdf',
    icon: '🗜️',
    tags: ['pdf', 'compress', 'optimize', 'size'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'pdf-to-jpg',
    title: 'PDF to JPG',
    description: 'Convert each PDF page to a high-quality JPG image.',
    category: 'pdf',
    icon: '🖼️',
    tags: ['pdf', 'jpg', 'convert', 'image'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['jpg-to-pdf'],
  },
  {
    slug: 'jpg-to-pdf',
    title: 'JPG to PDF',
    description: 'Bundle one or more JPG images into a single PDF file.',
    category: 'pdf',
    icon: '📄',
    tags: ['jpg', 'pdf', 'convert', 'image'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['pdf-to-jpg'],
  },
  {
    slug: 'word-to-pdf',
    title: 'Word to PDF',
    description: 'Convert Word documents to PDF using your browser\'s print engine.',
    category: 'pdf',
    icon: '📝',
    tags: ['word', 'docx', 'pdf', 'convert'],
    featured: false,
    popular: false,
    difficulty: 'medium',
  },
  {
    slug: 'rotate-pdf',
    title: 'Rotate PDF',
    description: 'Rotate pages in your PDF clockwise, counter-clockwise or 180°.',
    category: 'pdf',
    icon: '🔄',
    tags: ['pdf', 'rotate', 'orientation', 'pages'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },
  {
    slug: 'unlock-pdf',
    title: 'Unlock PDF',
    description: 'Remove password protection from PDFs you own and are authorised to edit.',
    category: 'pdf',
    icon: '🔓',
    tags: ['pdf', 'unlock', 'password', 'remove'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },

  // ── IMAGE TOOLS ────────────────────────────────────────────────────────────
  {
    slug: 'compress-image',
    title: 'Image Compressor',
    description: 'Reduce image file size while preserving visual quality using Canvas API.',
    category: 'image',
    icon: '🗜️',
    tags: ['image', 'compress', 'optimize', 'jpg', 'png'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['resize-image', 'webp-converter'],
  },
  {
    slug: 'resize-image',
    title: 'Image Resizer',
    description: 'Resize images to exact pixel dimensions or by percentage.',
    category: 'image',
    icon: '📐',
    tags: ['image', 'resize', 'dimensions', 'scale'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['compress-image', 'crop-image'],
  },
  {
    slug: 'jpg-to-png',
    title: 'JPG to PNG',
    description: 'Convert JPEG images to PNG format with transparency support.',
    category: 'image',
    icon: '🔀',
    tags: ['jpg', 'png', 'convert', 'image', 'transparency'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['png-to-jpg'],
  },
  {
    slug: 'png-to-jpg',
    title: 'PNG to JPG',
    description: 'Convert PNG images to JPEG format with customisable quality.',
    category: 'image',
    icon: '🔀',
    tags: ['png', 'jpg', 'convert', 'image'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['jpg-to-png'],
  },
  {
    slug: 'webp-converter',
    title: 'WebP Converter',
    description: 'Convert JPG/PNG images to WebP format for faster web loading.',
    category: 'image',
    icon: '⚡',
    tags: ['webp', 'convert', 'optimize', 'web', 'performance'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['compress-image'],
  },
  {
    slug: 'crop-image',
    title: 'Image Cropper',
    description: 'Crop images to custom dimensions or preset aspect ratios.',
    category: 'image',
    icon: '✂️',
    tags: ['image', 'crop', 'trim', 'aspect ratio'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['resize-image'],
  },
  {
    slug: 'image-to-base64',
    title: 'Image to Base64',
    description: 'Encode any image as a Base64 data URL for embedding in HTML or CSS.',
    category: 'image',
    icon: '🔡',
    tags: ['image', 'base64', 'encode', 'embed', 'data url'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['base64-encoder'],
  },
  {
    slug: 'favicon-generator',
    title: 'Favicon Generator',
    description: 'Generate multi-size .ico favicon files from any image in your browser.',
    category: 'image',
    icon: '⭐',
    tags: ['favicon', 'ico', 'icon', 'web', 'generate'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },

  // ── TEXT TOOLS ─────────────────────────────────────────────────────────────
  {
    slug: 'word-counter',
    title: 'Word Counter',
    description: 'Count words, characters, sentences and reading time for any text.',
    category: 'text',
    icon: '🔢',
    tags: ['text', 'word count', 'characters', 'reading time'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['character-counter'],
  },
  {
    slug: 'character-counter',
    title: 'Character Counter',
    description: 'Count characters with and without spaces, plus social media limits.',
    category: 'text',
    icon: '📊',
    tags: ['text', 'characters', 'count', 'twitter', 'social media'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['word-counter'],
  },
  {
    slug: 'case-converter',
    title: 'Case Converter',
    description: 'Convert text to UPPER, lower, Title, camelCase, snake_case and more.',
    category: 'text',
    icon: '🔡',
    tags: ['text', 'case', 'upper', 'lower', 'camel', 'snake'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'text-reverser',
    title: 'Text Reverser',
    description: 'Reverse text, words or lines — useful for encodings and creative writing.',
    category: 'text',
    icon: '🔃',
    tags: ['text', 'reverse', 'flip', 'mirror'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },
  {
    slug: 'remove-duplicates',
    title: 'Remove Duplicate Lines',
    description: 'Eliminate repeated lines from lists, logs or any multiline text.',
    category: 'text',
    icon: '🧹',
    tags: ['text', 'duplicates', 'lines', 'clean', 'deduplicate'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },
  {
    slug: 'lorem-ipsum',
    title: 'Lorem Ipsum Generator',
    description: 'Generate placeholder text in paragraphs, sentences or words.',
    category: 'text',
    icon: '📄',
    tags: ['lorem ipsum', 'placeholder', 'dummy text', 'design'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'grammar-checker',
    title: 'Grammar Checker',
    description: 'Check spelling and grammar using the free LanguageTool public API.',
    category: 'text',
    icon: '✅',
    tags: ['grammar', 'spell check', 'writing', 'proofreading'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },
  {
    slug: 'text-diff',
    title: 'Text Diff Checker',
    description: 'Compare two blocks of text and highlight the differences between them.',
    category: 'text',
    icon: '⚖️',
    tags: ['diff', 'compare', 'text', 'differences'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },

  // ── BUSINESS TOOLS ─────────────────────────────────────────────────────────
  {
    slug: 'invoice-generator',
    title: 'Invoice Generator',
    description: 'Create professional PDF invoices with line items, taxes and your logo.',
    category: 'business',
    icon: '🧾',
    tags: ['invoice', 'pdf', 'billing', 'freelance', 'business'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['receipt-generator', 'quotation-generator'],
  },
  {
    slug: 'receipt-generator',
    title: 'Receipt Generator',
    description: 'Generate and download printable receipts as PDF instantly.',
    category: 'business',
    icon: '🧾',
    tags: ['receipt', 'pdf', 'payment', 'business'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['invoice-generator'],
  },
  {
    slug: 'quotation-generator',
    title: 'Quotation Generator',
    description: 'Create formal price quotes for clients with itemised breakdown.',
    category: 'business',
    icon: '💬',
    tags: ['quote', 'quotation', 'proposal', 'pdf', 'pricing'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['invoice-generator'],
  },
  {
    slug: 'business-name-generator',
    title: 'Business Name Generator',
    description: 'Generate creative, available-sounding business names based on keywords.',
    category: 'business',
    icon: '💡',
    tags: ['business name', 'startup', 'brand', 'creative', 'naming'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'profit-calculator',
    title: 'Profit Calculator',
    description: 'Calculate gross and net profit from revenue and costs in real time.',
    category: 'business',
    icon: '📈',
    tags: ['profit', 'revenue', 'costs', 'calculator', 'finance'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['profit-margin', 'vat-calculator'],
  },
  {
    slug: 'vat-calculator',
    title: 'VAT Calculator',
    description: 'Add or remove VAT at any rate. See tax amount and totals instantly.',
    category: 'business',
    icon: '🏦',
    tags: ['vat', 'tax', 'calculator', 'finance', 'gst'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['profit-calculator'],
  },
  {
    slug: 'profit-margin',
    title: 'Profit Margin Calculator',
    description: 'Calculate gross margin percentage from cost price and selling price.',
    category: 'business',
    icon: '📊',
    tags: ['margin', 'profit', 'pricing', 'calculator'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['profit-calculator'],
  },
  {
    slug: 'payslip-generator',
    title: 'Payslip Generator',
    description: 'Create basic payslips for employees or contractors as downloadable PDFs.',
    category: 'business',
    icon: '💳',
    tags: ['payslip', 'payroll', 'salary', 'pdf', 'hr'],
    featured: false,
    popular: false,
    difficulty: 'medium',
    relatedTools: ['invoice-generator'],
  },

  // ── CALCULATOR TOOLS ───────────────────────────────────────────────────────
  {
    slug: 'percentage-calculator',
    title: 'Percentage Calculator',
    description: 'Calculate percentages, percentage change and what percent X is of Y.',
    category: 'calculator',
    icon: '%',
    tags: ['percentage', 'calculator', 'math', 'discount'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['discount-calculator'],
  },
  {
    slug: 'age-calculator',
    title: 'Age Calculator',
    description: 'Calculate exact age in years, months and days from any birthdate.',
    category: 'calculator',
    icon: '🎂',
    tags: ['age', 'birthday', 'date', 'calculator'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['date-calculator'],
  },
  {
    slug: 'bmi-calculator',
    title: 'BMI Calculator',
    description: 'Calculate Body Mass Index and get a healthy range interpretation.',
    category: 'calculator',
    icon: '⚖️',
    tags: ['bmi', 'body mass', 'health', 'weight', 'calculator'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'loan-calculator',
    title: 'Loan Calculator',
    description: 'Calculate monthly loan repayments, total interest and amortisation schedule.',
    category: 'calculator',
    icon: '🏦',
    tags: ['loan', 'mortgage', 'repayment', 'interest', 'calculator'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['percentage-calculator'],
  },
  {
    slug: 'discount-calculator',
    title: 'Discount Calculator',
    description: 'Find sale prices, discount amounts and savings percentages instantly.',
    category: 'calculator',
    icon: '🏷️',
    tags: ['discount', 'sale', 'savings', 'price', 'calculator'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['percentage-calculator', 'vat-calculator'],
  },
  {
    slug: 'date-calculator',
    title: 'Date Calculator',
    description: 'Calculate days between dates, add or subtract days from a date.',
    category: 'calculator',
    icon: '📅',
    tags: ['date', 'days', 'deadline', 'calendar', 'calculator'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['age-calculator'],
  },
  {
    slug: 'currency-converter',
    title: 'Currency Converter',
    description: 'Convert between 170+ currencies using live exchange rates.',
    category: 'calculator',
    icon: '💱',
    tags: ['currency', 'exchange rate', 'convert', 'money', 'forex'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },
  {
    slug: 'scientific-calculator',
    title: 'Scientific Calculator',
    description: 'Full scientific calculator with trigonometry, logarithms and constants.',
    category: 'calculator',
    icon: '🔬',
    tags: ['scientific', 'calculator', 'math', 'trigonometry', 'logarithm'],
    featured: false,
    popular: false,
    difficulty: 'easy',
  },

  // ── DEVELOPER TOOLS ────────────────────────────────────────────────────────
  {
    slug: 'json-formatter',
    title: 'JSON Formatter',
    description: 'Prettify, validate and minify JSON data with syntax error detection.',
    category: 'developer',
    icon: '{}',
    tags: ['json', 'format', 'validate', 'minify', 'developer'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['html-formatter', 'base64-encoder'],
  },
  {
    slug: 'html-formatter',
    title: 'HTML Formatter',
    description: 'Beautify or minify HTML markup with configurable indentation.',
    category: 'developer',
    icon: '</>',
    tags: ['html', 'format', 'beautify', 'minify', 'developer'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['css-minifier', 'json-formatter'],
  },
  {
    slug: 'css-minifier',
    title: 'CSS Minifier',
    description: 'Remove whitespace, comments and redundant code from CSS files.',
    category: 'developer',
    icon: '🎨',
    tags: ['css', 'minify', 'optimize', 'compress', 'developer'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['js-minifier', 'html-formatter'],
  },
  {
    slug: 'js-minifier',
    title: 'JavaScript Minifier',
    description: 'Minify JavaScript code to reduce file size for production.',
    category: 'developer',
    icon: '⚡',
    tags: ['javascript', 'js', 'minify', 'optimize', 'developer'],
    featured: false,
    popular: false,
    difficulty: 'easy',
    relatedTools: ['css-minifier'],
  },
  {
    slug: 'url-encoder',
    title: 'URL Encoder / Decoder',
    description: 'Encode or decode URL components and query strings instantly.',
    category: 'developer',
    icon: '🔗',
    tags: ['url', 'encode', 'decode', 'query string', 'developer'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['base64-encoder'],
  },
  {
    slug: 'base64-encoder',
    title: 'Base64 Encoder / Decoder',
    description: 'Encode strings or files to Base64, or decode Base64 back to text.',
    category: 'developer',
    icon: '🔡',
    tags: ['base64', 'encode', 'decode', 'developer', 'string'],
    featured: false,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['url-encoder', 'image-to-base64'],
  },
  {
    slug: 'uuid-generator',
    title: 'UUID Generator',
    description: 'Generate RFC 4122 compliant UUIDs (v4) using the browser crypto API.',
    category: 'developer',
    icon: '🎲',
    tags: ['uuid', 'guid', 'generate', 'random', 'developer'],
    featured: false,
    popular: true,
    difficulty: 'easy',
  },
  {
    slug: 'qr-generator',
    title: 'QR Code Generator',
    description: 'Generate QR codes for URLs, text, Wi-Fi and contact cards.',
    category: 'developer',
    icon: '📱',
    tags: ['qr code', 'generate', 'url', 'barcode', 'developer'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['uuid-generator'],
  },
  {
    slug: 'password-checker',
    title: 'Password Strength & Entropy Analyzer',
    description: 'Calculate password entropy bits, brute-force crack time estimates, and vulnerability analysis in real-time.',
    category: 'developer',
    icon: '🔒',
    tags: ['password', 'entropy', 'security', 'strength', 'developer'],
    featured: true,
    popular: true,
    difficulty: 'easy',
    relatedTools: ['uuid-generator', 'base64-encoder'],
  },
];

/** Tools filtered by category, in popular-first order */
export function toolsByCategory(category: ToolCategory): Tool[] {
  return TOOLS.filter(t => t.category === category).sort(
    (a, b) => Number(b.popular) - Number(a.popular)
  );
}

/** Tools marked as featured for the homepage grid */
export function featuredTools(): Tool[] {
  return TOOLS.filter(t => t.featured);
}

/** Look up a single tool by slug (category-agnostic) */
export function findTool(slug: string): Tool | undefined {
  return TOOLS.find(t => t.slug === slug);
}

/** Category metadata by id */
export function findCategory(id: ToolCategory): Category | undefined {
  return CATEGORIES.find(c => c.id === id);
}

/** Build the absolute URL path for a tool */
export function toolPath(tool: Tool): string {
  return `/tools/${tool.category}/${tool.slug}`;
}

/** Build the absolute URL path for a category */
export function categoryPath(category: ToolCategory): string {
  return `/tools/${category}`;
}

