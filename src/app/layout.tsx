import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

import { baseOptions } from '@/lib/layout.shared';
import { source } from '@/lib/source';
import { Analytics } from '@vercel/analytics/next';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { RootProvider } from 'fumadocs-ui/provider/next';

import './global.css';

const inter = Inter({
  subsets: ['latin'],
});

export const metadata: Metadata = {
  icons: {
    icon: '/favicon.svg',
  },
};

export default function Layout({ children }: LayoutProps<'/'>) {
  return (
    <html lang="en" className={inter.className} suppressHydrationWarning>
      <body className="flex flex-col min-h-screen">
        <RootProvider>
          <DocsLayout tree={source.pageTree} {...baseOptions()}>
            <Analytics />
            {children}
          </DocsLayout>
        </RootProvider>
      </body>
    </html>
  );
}
