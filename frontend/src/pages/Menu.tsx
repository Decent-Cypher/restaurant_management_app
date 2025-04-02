import Layout from "../components/Layout";

export default function Menu() {
  return (
    <Layout title="Menu | Cooking Mama">
      <div className="container mx-auto py-16 px-4">
        <h1 className="text-4xl font-bold text-center mb-12">Our Menu</h1>
        
        <div className="mb-16">
          <h2 className="text-3xl font-semibold mb-6">Appetizers</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Spring Rolls</h3>
                <span className="text-xl font-medium text-red-600">$8.99</span>
              </div>
              <p className="mt-2 text-gray-600">Fresh vegetables and herbs wrapped in rice paper with a sweet chili dipping sauce.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Garlic Bread</h3>
                <span className="text-xl font-medium text-red-600">$5.99</span>
              </div>
              <p className="mt-2 text-gray-600">Warm baguette with garlic butter and herbs.</p>
            </div>
          </div>
        </div>
        
        <div className="mb-16">
          <h2 className="text-3xl font-semibold mb-6">Main Courses</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Grilled Salmon</h3>
                <span className="text-xl font-medium text-red-600">$22.99</span>
              </div>
              <p className="mt-2 text-gray-600">Fresh salmon fillet grilled with lemon herb butter, served with seasonal vegetables.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Pasta Carbonara</h3>
                <span className="text-xl font-medium text-red-600">$18.99</span>
              </div>
              <p className="mt-2 text-gray-600">Al dente pasta with creamy sauce, pancetta, and parmesan cheese.</p>
            </div>
          </div>
        </div>
        
        <div>
          <h2 className="text-3xl font-semibold mb-6">Desserts</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Chocolate Cake</h3>
                <span className="text-xl font-medium text-red-600">$7.99</span>
              </div>
              <p className="mt-2 text-gray-600">Rich chocolate cake with a molten center, served with vanilla ice cream.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md">
              <div className="flex justify-between items-start">
                <h3 className="text-xl font-medium">Cheesecake</h3>
                <span className="text-xl font-medium text-red-600">$6.99</span>
              </div>
              <p className="mt-2 text-gray-600">Creamy New York style cheesecake with berry compote.</p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}