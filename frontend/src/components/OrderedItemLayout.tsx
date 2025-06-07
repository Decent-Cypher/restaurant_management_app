import { CartItem } from "../types";
import { useCart } from '../contexts/CartContext';

interface OrderedItemProps {
  item: CartItem;
}
export default function MenuItemLayout({ item }: OrderedItemProps) {
  const { getItemPrice } = useCart();

  return (
    <div className="bg-white rounded-lg shadow p-4 flex flex-col items-center text-center">
      <img 
        src={item.image}
        alt={item.name}
        className="w-full aspect-square object-cover rounded mb-2"
      />
      <p className="font-semibold text-gray-700 mb-1">{item.name}</p>
      <p className="text-sm text-gray-600 mb-2">{getItemPrice(item.price, item.quantity).toLocaleString()} VND</p>
    </div>
  );
}