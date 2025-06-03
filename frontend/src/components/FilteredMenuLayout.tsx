import { useNavigate } from "react-router-dom";
import { Menu, MenuItem } from "../types";


interface FilteredMenuProps {
  categories: Menu[];
  items: MenuItem[];
}

export default function FilteredMenuLayout({categories, items }: FilteredMenuProps) {
  const navigate = useNavigate();

  return (
    <div>
      {/* Menu category buttons */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6 mt-0">
        {categories.map((menu) => (
          <button
            key={menu.id}
            onClick={() => navigate("/order/menu", { state: { category: menu.name } })}
            className="bg-white rounded-lg shadow hover:shadow-lg transition duration-200 p-3 text-center text-sm font-semibold text-gray-700"
          >
            {menu.name}
          </button>
        ))}
      </div>

      <div className="h-1 w-full bg-[#242e56] rounded mb-6"></div>

      {/* Menu items */}
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-6">
        {items.map((item) => (
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
    </div>
  );
}
