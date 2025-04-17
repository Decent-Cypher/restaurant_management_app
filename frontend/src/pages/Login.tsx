import Layout from "../components/Layout";
import { useState } from "react";

export default function Login() {
  const [userType, setUserType] = useState<string>("customer");
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [showPassword, setShowPassword] = useState<boolean>(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch("http://localhost:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify({
          username,
          password,
          userType
        }),
      });
      
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Login failed");
      }
      
      // Handle successful login
      console.log("Login successful:", data);
      // Redirect or update state as needed
      
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setIsLoading(false);
    }
  };
  
  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch("http://localhost:8000/api/signup/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
          userType: "customer"
        }),
      });
      
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Signup failed");
      }
      
      // Handle successful signup
      console.log("Signup successful:", data);
      // Redirect or update state as needed
      
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout title="Login | Cooking Mama">
      <div className="flex items-center justify-center min-h-screen bg-[#e5ddce] px-4 py-12">
        <div className="w-full max-w-4xl bg-white rounded-2xl shadow-xl overflow-hidden flex flex-col md:flex-row">
          {/* Left Section */}
          <div className="w-full md:w-1/2 bg-[#1e2a59] text-white p-8 flex flex-col">
            <h1 className="text-3xl font-bold mb-8 leading-tight">
              Access the system for more features
            </h1>
            
            <div className="mt-8">
              <p className="text-lg font-medium mb-4">I'm a...</p>
              <div className="space-y-3">
                {["customer", "staff", "manager"].map((type) => (
                  <label key={type} className="flex items-center space-x-3 cursor-pointer">
                    <input
                      type="radio"
                      name="userType"
                      value={type}
                      checked={userType === type}
                      onChange={() => setUserType(type)}
                      className="form-radio h-5 w-5 text-blue-600"
                    />
                    <span className="capitalize">{type}</span>
                  </label>
                ))}
              </div>
            </div>
          </div>
          
          {/* Right Section */}
          <div className="w-full md:w-1/2 p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Welcome Back
            </h2>
            
            {error && (
              <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                {error}
              </div>
            )}
            
            <form onSubmit={handleLogin}>
              <div className="mb-4">
                <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-2">
                  Username
                </label>
                <input
                  type="text"
                  id="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                  className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900"
                  placeholder="Enter your username"
                />
              </div>
              
              <div className="mb-4">
                <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
                  Password
                </label>
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900"
                  placeholder="Enter your password"
                />
              </div>

              <div className="mb-6 flex items-center">
                <div className="relative inline-block h-4 w-4">
                  <input
                    type="checkbox"
                    id="showPassword"
                    checked={showPassword}
                    onChange={() => setShowPassword(!showPassword)}
                    className="sr-only"
                  />
                  <div className="absolute inset-0 bg-gray-100 border border-gray-300 rounded cursor-pointer">
                    {showPassword && (
                      <div className="absolute inset-0 flex items-center justify-center text-gray-700">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                          <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                        </svg>
                      </div>
                    )}
                  </div>
                </div>
                <label htmlFor="showPassword" className="ml-2 block text-sm text-gray-700 cursor-pointer">
                  Show password
                </label>
              </div>
              
              <div className="flex space-x-3">
                <button
                  type="submit"
                  disabled={isLoading}
                  className={`flex-1 bg-[#1e2a59] text-white font-semibold py-3 px-6 rounded-lg hover:bg-blue-900 transition duration-200 ${
                    isLoading ? "opacity-70 cursor-not-allowed" : ""
                  }`}
                >
                  {isLoading ? "Processing..." : "Login"}
                </button>
                
                {userType === "customer" && (
                  <button
                    type="button"
                    onClick={handleSignup}
                    disabled={isLoading}
                    className={`flex-1 bg-white border-2 border-[#1e2a59] text-[#1e2a59] font-semibold py-3 px-6 rounded-lg hover:bg-gray-100 transition duration-200 ${
                      isLoading ? "opacity-70 cursor-not-allowed" : ""
                    }`}
                  >
                    Sign Up
                  </button>
                )}
              </div>
            </form>
            
            <div className="mt-8 text-center text-sm text-gray-500">
              <p>
                Need help? <a href="#" className="text-blue-600 hover:underline">Contact support</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}