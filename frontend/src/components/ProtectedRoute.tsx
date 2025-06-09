// src/components/ProtectedRoute.jsx
import { useAuth } from "../contexts/AuthContext";
import { Navigate, useLocation } from "react-router-dom";

const ProtectedRoute = ({ children }) => {
  const { user} = useAuth();
  const location = useLocation();

  if (user === null) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }
  alert("ProtectedRoute: user is not null, user = " + JSON.stringify(user));

  return children;
};

export default ProtectedRoute;
