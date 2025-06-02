import Layout from "../components/Layout";
import FoodItem from "../components/FoodItem";
import { useState } from "react";

// Define the food category data structure
interface FoodCategory {
  name: string;
  items: {
    id: number;
    name: string;
    price: string;
    image: string;
    description: string;
  }[];
}

export default function Menu() {
  // Sample menu data - replace with your actual data or API call
  const [menuCategories] = useState<FoodCategory[]>([
    {
      name: "Appetizers",
      items: [
        {
          id: 1,
          name: "Spring Rolls",
          price: "$8.99",
          image: "/dishes/spring-rolls.jpg",
          description: "Fresh vegetables and herbs wrapped in rice paper with a sweet chili dipping sauce."
        },
        {
          id: 2,
          name: "Garlic Bread",
          price: "$5.99",
          image: "/dishes/garlic-bread.jpg",
          description: "Warm baguette with garlic butter and herbs."
        },
        {
          id: 3,
          name: "Chicken Wings",
          price: "$10.99",
          image: "/dishes/chicken-wings.jpg",
          description: "Crispy wings tossed in your choice of sauce: Buffalo, BBQ, or Honey Garlic."
        },
        {
          id: 4,
          name: "Calamari",
          price: "$11.99",
          image: "/dishes/calamari.jpg",
          description: "Lightly breaded squid served with marinara sauce and lemon."
        },
      ]
    },
    {
      name: "Main Courses",
      items: [
        {
          id: 5,
          name: "Grilled Salmon",
          price: "$22.99",
          image: "/dishes/grilled-salmon.jpg",
          description: "Fresh salmon fillet grilled with lemon herb butter, served with seasonal vegetables."
        },
        {
          id: 6,
          name: "Pasta Carbonara",
          price: "$18.99",
          image: "/dishes/pasta-carbonara.jpg",
          description: "Al dente pasta with creamy sauce, pancetta, and parmesan cheese."
        },
        {
          id: 7,
          name: "Beef Tenderloin",
          price: "$29.99",
          image: "/dishes/beef-tenderloin.jpg",
          description: "8oz beef tenderloin cooked to your preference, served with mashed potatoes and roasted vegetables."
        },
        {
          id: 8,
          name: "Chicken Parmesan",
          price: "$19.99",
          image: "/dishes/chicken-parmesan.jpg",
          description: "Breaded chicken breast topped with marinara sauce and melted mozzarella, served with spaghetti."
        },
      ]
    },
    {
      name: "Desserts",
      items: [
        {
          id: 9,
          name: "Chocolate Cake",
          price: "$7.99",
          image: "/dishes/chocolate-cake.jpg",
          description: "Rich chocolate cake with a molten center, served with vanilla ice cream."
        },
        {
          id: 10,
          name: "Cheesecake",
          price: "$6.99",
          image: "/dishes/cheesecake.jpg",
          description: "Creamy New York style cheesecake with berry compote."
        },
        {
          id: 11,
          name: "Tiramisu",
          price: "$8.99",
          image: "/dishes/tiramisu.jpg",
          description: "Coffee-flavored Italian dessert made of ladyfingers dipped in coffee, layered with mascarpone cheese."
        },
        {
          id: 12,
          name: "Apple Pie",
          price: "$6.99",
          image: "/dishes/apple-pie.jpg",
          description: "Warm apple pie with a flaky crust, served with a scoop of vanilla ice cream."
        },
        {
          id: 13,
          name: "Chocolate Cake",
          price: "$7.99",
          image: "/dishes/chocolate-cake.jpg",
          description: "Rich chocolate cake with a molten center, served with vanilla ice cream."
        },
        {
          id: 14,
          name: "Cheesecake",
          price: "$6.99",
          image: "/dishes/cheesecake.jpg",
          description: "Creamy New York style cheesecake with berry compote."
        },
        {
          id: 15,
          name: "Tiramisu",
          price: "$8.99",
          image: "/dishes/tiramisu.jpg",
          description: "Coffee-flavored Italian dessert made of ladyfingers dipped in coffee, layered with mascarpone cheese."
        },
        {
          id: 16,
          name: "Apple Pie",
          price: "$6.99",
          image: "/dishes/apple-pie.jpg",
          description: "Warm apple pie with a flaky crust, served with a scoop of vanilla ice cream."
        },
      ]
    },
  ]);

  return (
    <Layout title="Menu | Cooking Mama">
      <div className="bg-[#f8f5f0] min-h-screen py-16">
        <div className="w-full">
          <h1 className="lg:text-6xl text-4xl font-bold text-center mb-16 text-gray-800">Our Menu</h1>
          
          {menuCategories.map((category) => (
            <div key={category.name} className="mb-16">
              <div className="flex items-center justify-between mb-6">
                <h2 className="lg:text-4xl text-2xl font-semibold text-gray-800 lg:pl-32 pl-4">{category.name}</h2>
                {/* <div className="hidden md:flex space-x-2">
                  <button 
                    className="p-2 rounded-full bg-white shadow hover:bg-gray-100"
                    onClick={() => {
                      const container = document.getElementById(`scroll-${category.name}`);
                      if (container) container.scrollLeft -= 300;
                    }}
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                  </button>
                  <button 
                    className="p-2 rounded-full bg-white shadow hover:bg-gray-100"
                    onClick={() => {
                      const container = document.getElementById(`scroll-${category.name}`);
                      if (container) container.scrollLeft += 300;
                    }}
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                    </svg>
                  </button>
                </div> */}
              </div>
              
              <div 
                id={`scroll-${category.name}`} 
                className="flex overflow-x-auto pb-6 lg:px-32 px-4 gap-6 scrollbar-hide scroll-smooth"
                style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
              >
                {category.items.map((item) => (
                  <FoodItem
                    key={item.id}
                    name={item.name}
                    price={item.price}
                    image={item.image}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </Layout>
  );
}