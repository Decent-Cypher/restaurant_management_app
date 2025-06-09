import { CartItem } from "../types";
import { useCart } from '../contexts/CartContext';

interface OrderedItemProps {
  item: CartItem;
}
export default function OrderedItemLayout({ item }: OrderedItemProps) {
  const { getItemPrice } = useCart();
  return (
    <div className="bg-white rounded-xl p-4 mb-4 shadow-sm relative">
      <div className="flex justify-between">
        <div className="flex gap-3">
          <img 
            src={"http://localhost:8000/media/" + item.image}
            alt={item.name}
            className="w-16 h-16 object-cover rounded"
          />
          <div className="flex flex-col justify-between">
            <p className="font-semibold text-gray-700">{item.name}</p>
          </div>
        </div>
        <p className="font-semibold text-sm text-gray-700 self-end">
          {getItemPrice(item.price, item.quantity).toLocaleString()} VND
        </p>
      </div>
    </div>
  );
}