import Layout from "../components/Layout";

export default function App() {
  return (
    <Layout title="Home | Cooking Mama" transparentHeader={true}>
      {/* Background image or video */}
      <div className="
      h-screen w-full bg-cover bg-center bg-no-repeat -z-[1] fixed opacity-50
      bg-[url('https://images.unsplash.com/photo-1555396273-367ea4eb4db5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80')]">
      </div>

      {/* Welcome screen overlay */}
      <div className="h-screen w-full">

      </div>
      
      {/* Content Section */}
      <div className="py-16 px-4 md:px-8 bg-white">
        <div className="text-center max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold mb-6">Why Choose Cooking Mama?</h2>
          <p className="text-xl mb-12 text-gray-600">Experience the best restaurant management solution designed to boost your business.</p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <div className="text-red-500 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="text-2xl font-semibold mb-3">Manage Orders</h3>
              <p className="text-gray-600">Efficiently manage customer orders and keep track of order status in real-time.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <div className="text-red-500 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <h3 className="text-2xl font-semibold mb-3">Menu Management</h3>
              <p className="text-gray-600">Easily update your menu items, categories, and pricing with our intuitive interface.</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <div className="text-red-500 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <h3 className="text-2xl font-semibold mb-3">Analytics</h3>
              <p className="text-gray-600">Get insights into your sales, popular items, and peak hours with detailed reports.</p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}