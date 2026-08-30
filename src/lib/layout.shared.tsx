import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

import { ThemeToggle } from '@/components/theme-toggle';

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: 'DSA',
    },
    themeSwitch: {
      component: <ThemeToggle className="ms-auto" mode="light-dark-single-button" />,
    },
  };
}
