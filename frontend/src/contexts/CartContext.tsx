import React, { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { CartItem, MenuItem } from '../types'; // adjust the path as needed

interface CartContextType {
  cartItems: CartItem[];
  addToCart: (id: number) => void;
  removeFromCart: (id: number) => void;
  clearCart: () => void;
  calculateTotal: () => number;
  decreaseQuantity: (id: number) => void;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider = ({ children }: { children: ReactNode }) => {
  const [cartItems, setCartItems] = useState<CartItem[]>([]);
  const [allMenuItems, setAllMenuItems] = useState<MenuItem[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/menuitems/")
      .then((res) => res.json())
      .then((data) => setAllMenuItems(data))
      .catch((error) => console.error("Failed to fetch menu items:", error));
  
  }, []);

  const addToCart = (id: number) => {
    const item = allMenuItems.find((i) => i.id === id);
    if (!item) return;

    setCartItems((prevCart) => {
      const existing = prevCart.find((ci) => ci.id === id);
      if (existing) {
        return prevCart.map((ci) =>
          ci.id === id ? { ...ci, quantity: ci.quantity + 1 } : ci
        );
      } else {
        return [...prevCart, { ...item, quantity: 1 }];
      }
    });
  };


  const removeFromCart = (id: number) => {
    setCartItems((prevCart) => prevCart.filter((item) => item.id !== id));
  };

  const clearCart = () => {
    setCartItems([]);
  };

  const calculateTotal = () => {
    return cartItems.reduce((total, item) => {
      const price = parseFloat(item.price.replace(/[^0-9.-]+/g, '')); // Handle prices with "vnđ"
      return total + price * item.quantity;
    }, 0);
  };

  const decreaseQuantity = (id: number) => {
    setCartItems((prevCart) =>
      prevCart.map((item) =>
        item.id === id
          ? { ...item, quantity: Math.max(1, item.quantity - 1) }
          : item
      )
    );
  };

  return (
    <CartContext.Provider value={{ cartItems, addToCart, removeFromCart, clearCart, calculateTotal, decreaseQuantity }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = (): CartContextType => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
};
