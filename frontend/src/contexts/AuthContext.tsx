import { createContext, useContext, useEffect, useState } from "react";
import { getUserInfo } from "../api/auth";

interface AuthContextType {
  user: any;
  setUser: React.Dispatch<React.SetStateAction<any>>;
  fetchUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);


export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // user = { role, staff_id or diner_id }

  const fetchUser = async () => {
    try {
      const data = await getUserInfo();
      setUser(data);
    } catch {
      setUser(null);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser, fetchUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
};

