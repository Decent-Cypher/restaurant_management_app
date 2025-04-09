import { ReactNode } from 'react';
import Head from './Head';
import Header from './Header';
import Footer from './Footer';

interface LayoutProps {
  children: ReactNode;
  className?: string;
  title?: string;
  transparentHeader?: boolean;
}

export default function Layout({ children, className, title, transparentHeader = false }: LayoutProps) {
  return (
    <>
      <Head title={title} />
      <div className={`flex flex-col min-h-screen w-full ${className}`}>

        <Header transparent={transparentHeader} />
        
        <main className="flex-grow w-full">
          {children}
        </main>
        
        <Footer />
      </div>
    </>
  );
}