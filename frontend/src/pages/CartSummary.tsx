import { useState } from 'react';
import { useCart } from '../contexts/CartContext';
import { Link, useNavigate } from 'react-router-dom';
import OrderLayout from '../components/OrderLayout';
import CartItemLayout from '../components/CartItemLayout';
import { CartItem } from '../types';

export default function CartSummary() {
  const { cartItems, calculateSubTotal, clearCart, calculateTotal, calculateTax, getTotalQuantity } = useCart();
  const [isCheckout, setIsCheckout] = useState(false);
  const navigate = useNavigate();
  const [note, setNote] = useState("");

  const handleNoteChange = (e: any) => {
    const value = e.target.value;
    setNote(value);
  };

  const handleCheckout = () => {
    setIsCheckout(true);
    // Here you can add logic to handle the checkout process
    // For example, redirecting to a payment page or showing a confirmation message
  };

  return (
    <OrderLayout>
      <div className="px-8 pt-6 pb-8 flex gap-6 items-start">
        {/* Left Panel */}
        <div className="flex-1">
          {/* Top row: breadcrumb + cart title */}
          <div className="flex justify-between items-center mb-6 ">
            <div className="text-sm text-gray-700 font-medium">
              <Link to="/order">
                <span className="text-blue-600 cursor-pointer">Order</span>
              </Link> &gt; My Cart
            </div>
          </div>

          {/* Cart Items */}
          <div className="bg-white rounded-lg shadow p-4">
            {cartItems.length === 0 ? (
              <p className="text-gray-500">Your cart is empty.</p>
            ) : (
              cartItems.map((item: CartItem) => (
                <CartItemLayout item={item} />
              ))
            )}
          </div>
        </div>

        {/* Right Panel: Cart Summary */}
        <div className="w-full max-w-sm shrink-0">
          <div className="bg-white shadow-md rounded-2xl p-6 w-full max-w-sm">
            <h2 className="text-xl font-bold text-center text-gray-600 mb-4">Order Information</h2>

            <div className="text-sm text-gray-700 space-y-4">
              <div>
                <p className="font-semibold">Ordered items ({getTotalQuantity()})</p>
                <div className="flex justify-between pt-2">
                  <span>Sub-total:</span>
                  <span>{calculateSubTotal().toLocaleString()} VND</span>
                </div>
                <div className="flex justify-between items-center pt-1">
                  <span>Delivery fee:</span>
                  <span className="flex items-center gap-1">
                    Free
                    <span className="text-orange-500 cursor-help">ⓘ</span>
                  </span>
                </div>
                <div className="flex justify-between pt-1">
                  <span>Tax 8%:</span>
                  <span>{calculateTax().toLocaleString()} VND</span>
                </div>
                <hr className="my-2" />
                <div className="flex justify-between font-semibold text-base">
                  <span>Total:</span>
                  <span>{calculateTotal().toLocaleString()} VND</span>
                </div>
              </div>

              <div>
                <p className="font-semibold pt-2">Giao hàng tới:</p>
                <p className="text-gray-600">
                  Nguyễn Đình Chiểu, District 3, Ho Chi Minh City, Vietnam
                </p>
              </div>

              <div>
                <p className="font-semibold pt-2">Dự kiến giao:</p>
                <p className="text-gray-800 font-medium">
                  10:35 AM 03/06 (<span className="font-bold">Hôm nay</span>)
                </p>
              </div>

              <div className="mt-4">
                <input
                  type="text"
                  placeholder="Enter your note (optional)"
                  className="rounded-full placeholder:font-medium placeholder:text-sm placeholder-gray-300 text-gray-700 px-4 py-2 w-full border"
                  value={note}
                  onChange={handleNoteChange}
                />
              </div>
            </div>

            <div className="mt-4">
              <button className="w-full flex items-center justify-between bg-[#121c4a] text-white px-4 py-3 rounded-full font-semibold text-sm">
                {calculateTotal().toLocaleString()} VND
                <span className="ml-2 bg-white text-[#121c4a] rounded-full p-1 w-6 h-6 flex items-center justify-center text-sm font-bold">→</span>
              </button>
              <button 
              onClick={() => navigate('/order')}
              className="w-full text-center text-sm text-blue-600 font-semibold mt-3">Cancel</button>
            </div>
          </div>
        </div>

      </div>
    </OrderLayout>
  );
}