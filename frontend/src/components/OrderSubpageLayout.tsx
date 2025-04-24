import OrderLayout from "./OrderLayout";
import Cart from "./Cart";

export default function OrderSubpageLayout() {
  return (
    <OrderLayout>
      {/* Main content layout */}
      <div className="px-8 pt-6 pb-8 flex gap-6 items-start">
        {/* Menu */}
        <div className="text-sm text-gray-700 font-medium flex-1"> 
          {/*Bread crumb*/}
          <span className="text-blue-600 cursor-pointer">Order</span> &gt; Drinks
          {/* Menu list */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6 mt-6">
            {['Drinks', 'Combo', 'Food', 'Snacks'].map((name) => (
              <div className="bg-white rounded-lg shadow hover:shadow-lg transition duration-200 p-3 text-center text-sm font-semibold text-gray-700"> {name}
              </div>
            ))}
          </div>
          
          <div className="h-1 w-full bg-[#242e56] rounded mb-6"></div>

          {/* Menu items */}

          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-6">
            {[
              {
                name: "Mì Ý cua và xốt kem cà chua",
                price: "254,000",
              },
              {
                name: "Pizza 3 loại phô mai nhà làm",
                price: "198,000",
              },
              {
                name: "Gà rán với gia vị phương Đông, 2 miếng",
                price: "98,000",
              },
              {
                name: "Pizza 4 loại phô mai nhà làm",
                price: "248,000",
              },
              {
                name: "Mì Ý bò bằm và phô mai hun khói",
                price: "168,000",
              },
            ]
            .map((item) => (
              <div
                // key={item.id}
                className="bg-white rounded-lg shadow p-4 flex flex-col items-center text-center"
              >
                {/* <img
                  src={item.image}
                  alt={item.name}
                  className="h-32 w-full object-cover rounded mb-2"
                /> */}
                <div className="w-full aspect-square object-cover rounded mb-2"/>
                <p className="font-semibold text-gray-700 mb-1">{item.name}</p>
                <p className="text-sm text-gray-600 mb-2">{item.price} vnđ</p>
                <button className="bg-white border border-gray-400 rounded-full w-8 h-8 flex items-center justify-center text-xl text-gray-800 shadow">
                  +
                </button>
              </div>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12"></div>
        <div className="w-full max-w-sm shrink-0">
          <h2 className="text-xl font-bold text-[#242e56] ml-4 ">Giỏ hàng của tôi</h2>
          <Cart />
        </div>
      </div>
    </OrderLayout>
  );
}
