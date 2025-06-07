import { useNavigate } from "react-router-dom";
import { Menu, MenuItem } from "../types";
import MenuItemLayout from "./MenuItemLayout";

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
          <MenuItemLayout
            key={item.id}
            item={item}
          />
        ))}
      </div>
    </div>
  );
}
