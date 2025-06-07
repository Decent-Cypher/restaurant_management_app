import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

interface HeaderProps {
  transparent?: boolean;
}

export default function Header({ transparent = false }: HeaderProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  
  useEffect(() => {
    if (!transparent) return;
    
    const handleScroll = () => {
      setIsScrolled(window.scrollY > window.innerHeight - 80);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, [transparent]);
  
  const headerClasses = transparent 
    ? `fixed w-full z-50 transition-all duration-300 ${
        isScrolled 
          ? 'bg-white text-gray-800 shadow-md' 
          : 'bg-transparent text-white'
      }`
    : 'sticky top-0 w-full z-50 bg-gray-800 text-white';
  
  return (
    <header className={`py-6 px-12 ${headerClasses}`}>
      <div className="flex justify-between items-center">
        <div className="flex items-center">
          <Link to="/" className="text-3xl font-bold">Cooking Mama</Link>
        </div>
        
        <nav className="hidden md:block">
          <ul className="flex xl:space-x-24 space-x-14 text-xl">
            <li><Link to="/" className={`hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Home</Link></li>
            <li><Link to="/menu" className={`hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Menu</Link></li>
            <li><Link to="/order" className={`hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Order</Link></li>
            <li><Link to="/login" className={`hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Login</Link></li>
          </ul>
        </nav>
        
        <button 
          className="md:hidden"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
      
      {isMenuOpen && (
        <div className="md:hidden">
          <ul className="flex flex-col space-y-2 mt-2 text-right">
            <li><Link to="/" className={`block hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Home</Link></li>
            <li><Link to="/menu" className={`block hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Menu</Link></li>
            <li><Link to="/order" className={`block hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Order</Link></li>
            <li><Link to="/login" className={`block hover:${isScrolled ? 'text-gray-600' : 'text-gray-300'}`}>Login</Link></li>
          </ul>
        </div>
      )}
    </header>
  );
}