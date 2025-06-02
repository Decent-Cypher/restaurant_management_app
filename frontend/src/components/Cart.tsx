import { Plus, Minus, X, Info } from 'lucide-react';

export default function Cart() {
  return (
    <div className="bg-transparent p-4 rounded-lg">


      {/* Cart Item 1 */}
      <div className="bg-white rounded-xl p-4 mb-4 shadow-sm relative">
        <button className="absolute top-2 right-2 text-gray-500 hover:text-black">
          <X size={18} />
        </button>
        <div className="flex gap-3 mb-2">
          {/* <img
            src="/your-image-path.jpg"
            alt="Happy Family"
            className="w-16 h-16 object-cover rounded"
          /> */}
          <div className="w-12 h-12 object-cover rounded" />
          <div>
            <p className="font-semibold text-gray-700">Happy Family</p>
          </div>
        </div>
        <div className="text-blue-600 text-sm mt-2 flex items-center gap-1 cursor-pointer hover:underline">
          <Info size={14} />
          Thêm ghi chú
        </div>
        <div className="flex items-center justify-between mt-3">
          <div className="flex items-center gap-2">
            <button className="border rounded-full w-6 h-6 flex items-center justify-center text-gray-700">
              <Minus size={12} />
            </button>
            <span className="text-sm font-medium  text-gray-700"> 1 </span>
            <button className="border rounded-full w-6 h-6 flex items-center justify-center text-gray-700">
              <Plus size={12} />
            </button>
          </div>
          <p className="font-semibold text-sm text-gray-700">695,000 vnđ</p>
        </div>
      </div>


      {/* Footer Button */}
      <div className="bg-[#242e56] text-white rounded-full p-3 mt-2 flex items-center justify-between px-6 shadow-md">
        <span className="text-sm font-medium">1,024,920 vnđ (VAT)</span>
        <button className="font-semibold text-sm flex items-center gap-1">
          Xem giỏ hàng <span className="ml-1">➝</span>
        </button>
      </div>
    </div>
  );
}
