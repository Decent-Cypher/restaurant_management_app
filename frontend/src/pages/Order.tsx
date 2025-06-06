import OrderLayout from "../components/OrderLayout";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { Menu, MenuItem } from "../types";

export default function Order() {
  const [serviceType, setServiceType] = useState("");
  const [tableNumber, setTableNumber] = useState("");
  const [tableError, setTableError] = useState("");
  const [feedback, setFeedback] = useState<string | null>(null);
  const [menus, setMenus] = useState<Menu[]>([]);
  const [menuItems, setMenuItems] = useState<MenuItem[]>([]);
  const [showFollowUp, setShowFollowUp] = useState(false);
  const navigate = useNavigate();

  const handleTableNumberChange = (e: any) => {
    const value = e.target.value;
    setTableNumber(value);
    if (!/^([1-9]|1\d|20)$/.test(value)) {
      setTableError("Please enter a number between 1 and 20");
    } else {
      setTableError("");
    }
  };

  useEffect(() => {
    fetch("http://localhost:8000/api/menu/menus/")
      .then((res) => res.json())
      .then((data) => setMenus(data))
      .catch((error) => {
        console.error("Failed to fetch menus:", error);
      });

    fetch("http://localhost:8000/api/menu/menu-items/")
      .then((res) => res.json())
      .then((data) => setMenuItems(data))
      .catch((error) => console.error("Failed to fetch menu items:", error));
  
  }, []);

  return (
    <OrderLayout>
      <div className="bg-[#e5ddce] min-h-screen pb-8 pt-8">
        {/* Single container for both image and welcome note */}
        <div className="flex flex-col md:flex-row gap-6 rounded-2xl overflow-hidden shadow-lg bg-white max-w-[69rem] mx-auto mb-4">
          {/* Banner Image with text overlay */}
          <div className="relative w-full md:w-2/3">
            <img
              src="/banner.jpg"
              alt="Seasonal Menu"
              className="w-full h-full object-cover"
            />
          </div>

          {/* Service Type Section */}
          <div className="w-full md:w-1/3 p-6 bg-white flex flex-col justify-center">
            {/* Welcome Note */}
            <h2 className="text-lg font-bold text-gray-800 text-center mb-2">
              Welcome to <br /> <span className="text-xl text-blue-900">Cooking Mama</span>
            </h2>
            {/* Service type input field*/}
            <p className="text-sm font-medium text-gray-700 text-center mb-2 mt-8">Choose your service type:</p>
            <div className="flex flex-col text-sm font-medium text-gray-700 mx-auto gap-2">
              {['Dine-in', 'Delivery', 'Take-away'].map((type) => (
                <label key={type} className="flex items-center gap-2">
                  <input
                    type="radio"
                    name="serviceType"
                    value={type}
                    checked={serviceType === type}
                    onChange={() => setServiceType(type)}
                  />
                  {type}
                </label>
              ))}
            </div>

            {serviceType === 'Dine-in' && (
              <div className="mt-4">
                <input
                  type="text"
                  placeholder="Enter your table number"
                  className="rounded-full placeholder:font-medium placeholder:text-sm placeholder-gray-300 text-gray-700 px-4 py-2 w-full border"
                  value={tableNumber}
                  onChange={handleTableNumberChange}
                />
                {tableError && <p className="text-red-500 text-sm mt-1 ml-4">{tableError}</p>}
              </div>
            )}

            {serviceType === 'Delivery' && (
              <div className="mt-4">
                <input
                  type="text"
                  placeholder="Enter your delivery destination"
                  className="rounded-full  placeholder:font-medium placeholder:text-sm placeholder-gray-300 text-gray-700 px-4 py-2 w-full border"
                />
              </div>
            )}

          </div>
        </div>

        {/* Menu Categories */}
        <div className="max-w-6xl mx-auto px-4">
          <h3 className="text-2xl font-bold mb-4 text-gray-800">Menu</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
            {menus.map((menu) => (
              <button
                key={menu.id}
                onClick={() => navigate("/order/menu", { state: { category: menu.name } })}
                className="bg-white rounded-lg shadow hover:shadow-lg transition duration-200 p-3 text-center"
              >
                <img
                  src={menu.image}
                  alt={menu.name}
                  className="h-24 w-full object-cover mb-2 rounded"
                />
                <p className="text-sm font-semibold text-gray-700">{menu.name}</p>
              </button>
            ))}
          </div>

          {/* Popular Dishes */}
          <h3 className="text-2xl font-bold mb-4 text-gray-800">Popular Dishes</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-6">
            {menuItems.slice(0, 5).map((item) => (
              <div
                key={item.id}
                className="bg-white rounded-lg shadow p-4 flex flex-col items-center text-center"
              >
                <img
                  src={item.image}
                  alt={item.name}
                  className="w-full aspect-square object-cover rounded mb-2"
                />
                <p className="font-semibold text-gray-700 mb-1">{item.name}</p>
                <p className="text-sm text-gray-600 mb-2">{item.price} vnđ</p>
                <button className="bg-white border border-gray-400 rounded-full w-8 h-8 flex items-center justify-center text-xl text-gray-800 shadow">
                  +
                </button>
              </div>
            ))}
          </div>

          {/* Feedback Section */}
          <div className="bg-white p-6 rounded-2xl shadow-md max-w-2xl mx-auto mt-8">
            {!feedback ? (
              <>
                <h4 className="font-medium text-sm text-center text-gray-800 mb-4">How was your experience with our service?</h4>
                <div className="flex justify-around">
                  {["😠", "🙁", "😐", "🙂", "😄"].map((face, idx) => (
                    <button
                      key={idx}
                      className="text-4xl hover:scale-110 transition"
                      onClick={() => setFeedback(face)}
                    >
                      {face}
                    </button>
                  ))}
                </div>
              </>
            ) : (
              <>
                <h4 className="font-medium text-sm text-gray-800 text-center mb-4">
                  {feedback === "😄" || feedback === "🙂"
                    ? "Great! Can you share your throughts with us?"
                    : "We're sorry. Can you tell us what's wrong?"}
                </h4>
                <div className="flex justify-center gap-4">
                  <button
                    className="bg-white px-6 py-2 rounded-full shadow text-gray-700"
                    onClick={() => setFeedback(null)}
                  >
                    No, thank you!
                  </button>
                  <button
                    className="bg-[#1e2a59] text-white px-6 py-2 rounded-full shadow"
                    onClick={() => navigate("/feedback")}
                  >
                    Yes, of course!
                  </button>
                </div>
              </>
            )}
          </div>

        </div>
      </div>
    </OrderLayout>
  );
}
