/**
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
  | 'services'
  | 'contact';

export const navLinks: { id: NavLinkId; path: string }[] = [
  { id: 'products', path: '/products' },
  { id: 'micro-saas', path: '/micro-saas' },
  { id: 'tools', path: '/tools' },
  { id: 'blog', path: '/blog' },
  { id: 'contact', path: '/contact' },
];

export type FooterSectionId = 'ecosystem' | 'company';
export type FooterLinkId =
  | 'documentation'
  | 'tools'
  | 'products'
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
