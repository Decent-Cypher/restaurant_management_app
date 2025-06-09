export interface MenuItem {
  id: number;
  name: string;
  price: string;
  image: string;
  menu: number;
}

export interface Menu {
  id: number;
  name: string;
  description: string;
  image: string;
}

export interface CartItem {
  id: number;
  name: string;
  price: string;
  quantity: number;
  image: string;
}

export interface Order {
  order_id: number;
  service_type: string;
  order_status: string;
  total_price: number;
  time_created: string;
  last_modified: string;
  address: string | null;
  note: string;
  items: CartItem[];
}

export interface Diner {
  name: string;
  email: string;
  phone_number: string;
}