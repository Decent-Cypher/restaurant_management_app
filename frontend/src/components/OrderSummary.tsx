import { Info } from "lucide-react";

export default function OrderSummary() {
  return (
    <div className="bg-white rounded-2xl shadow p-6 w-full max-w-sm mx-auto text-[#242e56]">
      <h2 className="text-xl font-bold text-center mb-4">Thông tin đơn hàng</h2>

      <div className="border-t border-b py-4 space-y-2 text-sm">
        <p className="font-semibold">
          Các món giao tức thì <span className="text-[#242e56]">(2)</span>
        </p>

        <div className="flex justify-between">
          <span>Tổng đơn:</span>
          <span className="font-medium">949,000 vnd</span>
        </div>

        <div className="flex justify-between items-center">
          <span className="flex items-center gap-1">
            Phí vận chuyển: <Info className="w-4 h-4 text-orange-500" />
          </span>
          <span className="text-green-600 font-semibold">Miễn phí</span>
        </div>

        <div className="flex justify-between">
          <span>Thuế 8%:</span>
          <span className="font-medium">75,920 vnd</span>
        </div>

        <div className="flex justify-between border-t pt-2 font-bold">
          <span>Tổng tiền:</span>
          <span>1,024,920 vnd</span>
        </div>
      </div>

      <div className="mt-4 space-y-1 text-sm">
        <p className="font-medium">Giao hàng tới:</p>
        <p className="text-gray-700">
          Nguyễn Đình Chiểu, District 3, Ho Chi Minh City, Vietnam
        </p>

        <p className="font-medium mt-2">Dự kiến giao:</p>
        <p className="text-gray-700">
          6:34 PM 24/04 (<span className="font-semibold text-black">Hôm nay</span>)
        </p>
      </div>

      <p className="text-xs text-gray-600 mt-4">
        Bằng việc bấm nút, tôi đồng ý với những{" "}
        <span className="font-semibold underline">Điều kiện và điều khoản</span>
      </p>

      <div className="flex justify-between items-center bg-[#242e56] text-white rounded-full mt-4 px-6 py-2 shadow-md">
        <span className="font-semibold">1,024,920 vnd</span>
        <button className="bg-white text-[#242e56] px-4 py-1 rounded-full font-semibold hover:bg-gray-100 transition">
          Thanh toán
        </button>
      </div>

      <p className="text-center mt-3 text-blue-600 font-medium cursor-pointer hover:underline">
        Hủy
      </p>
    </div>
  );
}
