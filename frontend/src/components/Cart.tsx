import { CartItem } from '../types';
import CartItemLayout from "./CartItemLayout";
import { useCart } from '../contexts/CartContext';

interface CartProps {
  items: CartItem[];
}

export default function Cart({items}: CartProps) {
  const {calculateTotal} = useCart();
  
  return (
    <div className="bg-transparent p-4 rounded-lg">
      {/* Cart Items */}
      {items.map((item: CartItem) => (
        <CartItemLayout item={item} />
      ))}


      {/* Footer Button */}
      <div className="bg-[#242e56] text-white rounded-full p-3 mt-2 flex items-center justify-between px-6 shadow-md">
        <span className="text-sm font-medium"> {calculateTotal().toLocaleString()} vnđ</span>
        <button className="font-semibold text-sm flex items-center gap-1">
          Xem giỏ hàng <span className="ml-1">➝</span>
        </button>
      </div>
    </div>
  );
}
