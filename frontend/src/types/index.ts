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