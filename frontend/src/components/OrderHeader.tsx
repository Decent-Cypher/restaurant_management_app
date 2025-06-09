import { Search, User, Globe, ShoppingCart,  MessageSquare } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export default function OrderHeader() {
  const navigate = useNavigate();

  return (
    <header className="sticky top-[83px] z-40 bg-[#242e56] text-white px-6 py-3 flex items-center justify-between">
      {/* Left: Search Bar */}
      <div className="flex-1 max-w-xl ml-6">
        <div className="flex items-center bg-gray-100 rounded-full px-4 py-1 text-gray-800">
          <Search className="w-5 h-5 mr-2" />
          <input
            type="text"
            placeholder="Search for an item"
            className="bg-transparent outline-none w-full"
          />
        </div>
      </div>

      {/* Right: Icons */}
      <div className="flex items-center gap-12 ml-12 mr-6">
        <User onClick={() => navigate("/profile")} className="w-6 h-6" />
        {/* <div className="flex items-center gap-1">
          <Globe className="w-6 h-6" />
          <span className="text-white">English</span>
        </div> */}
        <div className="relative">
          <MessageSquare onClick={() => navigate("/feedback")} className="w-6 h-6" />
          {/* <span className="absolute -top-2 -right-2 bg-red-500 text-xs text-white w-5 h-5 rounded-full flex items-center justify-center">
            2
          </span> */}
        </div>
        <div className="relative">
          <ShoppingCart onClick={() => navigate("/order/cart")} className="w-6 h-6" />
          {/* <span className="absolute -top-2 -right-2 bg-red-500 text-xs text-white w-5 h-5 rounded-full flex items-center justify-center">
            2
          </span> */}
        </div>
      </div>
    </header>
  );
}
