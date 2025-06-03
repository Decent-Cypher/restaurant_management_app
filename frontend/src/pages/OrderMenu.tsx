import { useEffect, useState } from "react";
import FilteredMenuLayout from '../components/FilteredMenuLayout';
import OrderLayout from "../components/OrderLayout";
import Cart from "../components/Cart";
import { Link, useLocation } from "react-router-dom";
import { Menu, MenuItem } from "../types";

export default function OrderMenu() {
  const location = useLocation();
  const selectedCategory = location.state?.category || "Korean Food Menu";

  const [menus, setMenus] = useState<Menu[]>([]);
  const [allMenuItems, setAllMenuItems] = useState<MenuItem[]>([]);
  const [filteredItems, setFilteredItems] = useState<MenuItem[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const menusRes = await fetch("http://localhost:8000/api/menus/");
        const menusData: Menu[] = await menusRes.json();
        setMenus(menusData);

        const itemsRes = await fetch("http://localhost:8000/api/menuitems/");
        const itemsData: MenuItem[] = await itemsRes.json();
        setAllMenuItems(itemsData);

        // Find menu ID based on selected category
        const selectedMenu = menusData.find(menu => menu.name === selectedCategory);
        if (selectedMenu) {
          const filtered = itemsData.filter(item => item.menu === selectedMenu.id);
          setFilteredItems(filtered);
        } else {
          setFilteredItems([]);
        }

      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };

    fetchData();
  }, [selectedCategory]);

  return (
  <OrderLayout>
    <div className="px-8 pt-6 pb-8 flex gap-6 items-start">
      {/* Left Panel */}
      <div className="flex-1">
        {/* Top row: breadcrumb + cart title */}
        <div className="flex justify-between items-center mb-6">
          <div className="text-sm text-gray-700 font-medium">
            <Link to="/order">
              <span className="text-blue-600 cursor-pointer">Order</span>
            </Link> &gt; {selectedCategory}
          </div>
        </div>

        {/* Content below breadcrumb */}
        <FilteredMenuLayout
          categories={menus}
          items={filteredItems}
        />
      </div>

      {/* Right Panel (Cart) */}
      <div className="w-full max-w-sm shrink-0">
        <h2 className="text-xl font-bold text-[#242e56] ml-4">My Cart</h2>
        <Cart />
      </div>
    </div>
  </OrderLayout>
  );
}
