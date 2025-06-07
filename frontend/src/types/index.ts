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
  id: number;
  service_type: string;
  diner_id: number;
  total_price: number;
  created_at: string;
  last_modified: string;
  address: string | null;
  note: string | null;
  items: CartItem[];
}