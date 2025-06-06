import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './App'
import Menu from './Menu'
import Order from './Order'
import NotFound from './404'
import Login from './Login'
import OrderMenu from './OrderMenu'
import CartSummary from './CartSummary'
import { CartProvider } from '../contexts/CartContext'; 

const rootElement = document.getElementById('root');
if (rootElement) {
  createRoot(rootElement).render(
    <StrictMode>
      <BrowserRouter>
        <CartProvider>
          <Routes>
            <Route path="/" element={<App />} />
            <Route path="/menu" element={<Menu />} />
            <Route path="/order" element={<Order />} />
            <Route path="/order/menu" element={<OrderMenu />} />
            <Route path="/order/cart" element={<CartSummary />} />
            <Route path="/login" element={<Login />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </CartProvider>
      </BrowserRouter>
    </StrictMode>,
    );
} else {
  console.error('Root element not found');
}