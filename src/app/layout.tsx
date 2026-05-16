import { RootProvider } from 'fumadocs-ui/provider/next';
import './global.css';
import { Inter } from 'next/font/google';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { source } from '@/lib/source';
import { baseOptions } from '@/lib/layout.shared';
import type { Metadata } from 'next';
import { Analytics } from '@vercel/analytics/next';

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
