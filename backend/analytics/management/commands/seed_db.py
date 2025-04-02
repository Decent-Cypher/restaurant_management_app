# filepath: /home/baku/Coding/restaurant_management_app/backend/orders/management/commands/seed_db.py
from django.core.management.base import BaseCommand
from accounts.models import Staff, Diner
from menu.models import Menu, MenuItem
from orders.models import Order, OrderItem, Payment
from reviews.models import Feedback

import os

class Command(BaseCommand):
    help = 'Seeds the database with initial data if it is empty'

    def handle(self, *args, **kwargs):
        database_seeding = os.getenv('DATABASE_SEEDING', 'False').lower() in ['true', '1', 't']
        
        if database_seeding:
            self.stdout.write(self.style.WARNING('DATABASE_SEEDING is set to True. Deleting all current data...'))
            Staff.objects.all().delete()
            Diner.objects.all().delete()
            Menu.objects.all().delete()
            MenuItem.objects.all().delete()
            Order.objects.all().delete()
            OrderItem.objects.all().delete()
            Payment.objects.all().delete()
            Feedback.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Seeding database...'))
            
            # Add your seeding logic here
            # Example seeding for Staff
            staff_fieri = Staff.objects.create(name="Guy Fieri", role="Manager", email="fieri@example.com")
            staff_ray = Staff.objects.create(name="Rachael Ray", role="Chef", email="ray@example.com")
            staff_caines = Staff.objects.create(name="Michael Caines", role="Waiter", email="caines@example.com")
            staff_oliver = Staff.objects.create(name="Jamie Oliver", role="Waiter", email="oliver@example.com")
            staff_ramsay = Staff.objects.create(name="Gordon Ramsay", role="Chef", email="ramsay@example.com")
            staff_fieri.set_password("123")
            staff_ray.set_password("123")
            staff_caines.set_password("123")
            staff_oliver.set_password("123")
            staff_ramsay.set_password("123")
            staff_fieri.save()
            staff_ray.save()
            staff_caines.save()
            staff_oliver.save()
            staff_ramsay.save()
            
            # Example seeding for Diner
            diner_giap = Diner.objects.create(name="nhugiap", email="giap.nn225441@sis.hust.edu.vn", phone_num="1234567890")
            diner_binh = Diner.objects.create(name="ducbinh", email="binh.nd225475@sis.hust.edu.vn", phone_num="0987654321")
            diner_khanh = Diner.objects.create(name="ankhanh", email="khanh.ta225447@sis.hust.edu.vn")
            diner_bao = Diner.objects.create(name="vietbao", email="bao.mv225474@sis.hust.edu.vn", phone_num="0123456789")
            diner_tu = Diner.objects.create(name="anhtu", email="tu.pa225463@sis.hust.edu.vn", phone_num="0123457789")
            diner_mbappe = Diner.objects.create(name="Kylian Mbappe", phone_num="9876543210", email="mbappe@example.com")
            diner_messi = Diner.objects.create(name="Lionel Messi", email="messi@example.com")
            diner_giap.set_password("123")
            diner_binh.set_password("123")
            diner_khanh.set_password("123")
            diner_bao.set_password("123")
            diner_tu.set_password("123")
            diner_mbappe.set_password("123")
            diner_messi.set_password("123")
            diner_giap.save()
            diner_binh.save()
            diner_khanh.save()
            diner_bao.save()
            diner_tu.save()
            diner_mbappe.save()
            diner_messi.save()
            
            # Example seeding for Menu and MenuItem
            menu_drink = Menu.objects.create(name="Drink Menu", description="Quench your thirst with our Drink Menu, featuring a selection of refreshing beverages. Choose from fruity, herbal-infused teas or zesty citrus drinks that are perfect complements to your meal. Served in elegant glasses, these drinks are both a visual and flavorful treat.", image="menu_images/menu-drink.png")
            menu_kimbap = Menu.objects.create(name="Kimbap Menu", description="Delight in the fresh and flavorful rolls of our Kimbap Menu, crafted with premium ingredients. Each roll is packed with a perfect combination of seasoned vegetables, fresh seafood, and tender meat, all wrapped in seaweed and rice. Served with our special dipping sauces, these rolls are as beautiful as they are delicious.", image="menu_images/menu-kimbap.png")
            menu_korean_food = Menu.objects.create(name="Korean Food Menu", description="Savor the rich and complex flavors of our Korean Food Menu, featuring a variety of traditional dishes. From spicy kimchi to savory bulgogi, each dish is a celebration of Korean culinary heritage. Served with a side of steamed rice, these dishes are sure to satisfy your cravings.", image="menu_images/menu-korean-food.png")
            menu_set = Menu.objects.create(name="Set Menu", description="Indulge in our Set Menu, a curated selection of our most popular dishes. Each set is thoughtfully designed to offer a balanced and satisfying meal, with a main course, side dish, and drink. Perfect for a quick and delicious meal, these sets are sure to leave you feeling full and happy.", image="menu_images/menu-set.png")
            
            # Example seeding for MenuItem
            menu_item_box_7_3 = MenuItem.objects.create(name="Set box 7.3", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-7_3.png")
            menu_item_box_ga_3_vi = MenuItem.objects.create(name="Set box Gà 3 vị", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-ga-3-vi.png")
            menu_item_box_han_1_5 = MenuItem.objects.create(name="Set box Hàn 1.5", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-han-1_5.png")
            menu_item_box_han_1 = MenuItem.objects.create(name="Set box Hàn 1", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-han-1.png")
            menu_item_box_han_2 = MenuItem.objects.create(name="Set box Hàn 2", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-han-2.png")
            menu_item_box_han_3 = MenuItem.objects.create(name="Set box Hàn 3", description="Delicious Korean set meal", price=150000, menu=menu_set, image="menu_item_images/box-han-3.png")
            menu_item_box_mandu = MenuItem.objects.create(name="Box Mandu", description="Tasty dumplings", price=120000, menu=menu_set, image="menu_item_images/box-mandu.png")
            
            menu_item_carbonara_tteokbokki = MenuItem.objects.create(name="Carbonara Tteokbokki", description="Cheesy rice cakes", price=170000, menu=menu_korean_food, image="menu_item_images/carbonara-tteokbokki.png")
            menu_item_com_ca_ri_thit_cot_let_chien_xu = MenuItem.objects.create(name="Cơm cà ri thịt cốt lết chiên xù", description="Crispy fried pork cutlet with curry", price=180000, menu=menu_korean_food, image="menu_item_images/com-ca-ri-thit-cot-let-chien-xu.png")
            menu_item_com_tron_bibimbap = MenuItem.objects.create(name="Cơm trộn Bibimbap", description="Mixed rice with vegetables and beef", price=160000, menu=menu_korean_food, image="menu_item_images/com-tron-bibimbap.png")
            menu_item_mien_tron = MenuItem.objects.create(name="Miến trộn", description="Stir-fried vermicelli", price=120000, menu=menu_korean_food, image="menu_item_images/mien-tron.png")
            menu_item_ram_don = MenuItem.objects.create(name="Ram Don", description="Spicy instant noodles", price=120000, menu=menu_korean_food, image="menu_item_images/ram-don.png")
            menu_item_tteokbokki_cha_ca = MenuItem.objects.create(name="Tteokbokki chả cá", description="Fish cake Tteokbokki", price=140000, menu=menu_korean_food, image="menu_item_images/tteokbokki-cha-ca.png")
            
            menu_item_kimbap_bo_bulgogi = MenuItem.objects.create(name="Kimbap bò Bulgogi", description="Kimbap with Bulgogi beef", price=130000, menu=menu_kimbap, image="menu_item_images/kimbap-bo-bulgogi.png")
            menu_item_kimbap_bo_pho_mai_chay = MenuItem.objects.create(name="Kimbap bò phô mai cháy", description="Burnt cheese and beef kimbap", price=140000, menu=menu_kimbap, image="menu_item_images/kimbap-bo-pho-mai-chay.png")
            menu_item_kimbap_ca_ngu_cai_vang = MenuItem.objects.create(name="Kimbap cá ngừ cải vàng", description="Tuna and pickled mustard leaf kimbap", price=130000, menu=menu_kimbap, image="menu_item_images/kimbap-ca-ngu-cai-vang.png")
            menu_item_kimbap_chien = MenuItem.objects.create(name="Kimbap chiên", description="Crispy fried kimbap", price=150000, menu=menu_kimbap, image="menu_item_images/kimbap-chien.png")
            menu_item_kimbap_ga_gion_cajun = MenuItem.objects.create(name="Kimbap gà giòn Cajun", description="Cajun crispy chicken kimbap", price=150000, menu=menu_kimbap, image="menu_item_images/kimbap-ga-gion-cajun.png")
            menu_item_kimbap_heo_nuong_galbi = MenuItem.objects.create(name="Kimbap heo nướng Galbi", description="Kimbap with grilled pork Galbi", price=150000, menu=menu_kimbap, image="menu_item_images/kimbap-heo-nuong-galbi.png")
            menu_item_kimbap_pho_mai = MenuItem.objects.create(name="Kimbap phô mai", description="Cheesy kimbap", price=140000, menu=menu_kimbap, image="menu_item_images/kimbap-pho-mai.png")
            menu_item_kimbap_suon_bo_bbq = MenuItem.objects.create(name="Kimbap sườn bò BBQ", description="BBQ beef rib kimbap", price=160000, menu=menu_kimbap, image="menu_item_images/kimbap-suon-bo-bbq.png")
            menu_item_kimbap_tom_sot_guyumi = MenuItem.objects.create(name="Kimbap tôm sốt Guyumi", description="Shrimp kimbap with Guyumi sauce", price=150000, menu=menu_kimbap, image="menu_item_images/kimbap-tom-sot-guyumi.png")
            menu_item_kimbap_xa_xiu = MenuItem.objects.create(name="Kimbap xá xíu", description="Char siu pork kimbap", price=150000, menu=menu_kimbap, image="menu_item_images/kimbap-xa-xiu.png")
            menu_item_kimbibi = MenuItem.objects.create(name="Kimbibi", description="Special Bibimbap-style kimbap", price=150000, menu=menu_kimbap, image="menu_item_images/kimbibi.png")
            
            menu_item_tra_cam_buoi_nhiet_doi = MenuItem.objects.create(name="Trà cam bưởi nhiệt đới", description="Tropical orange and grapefruit tea", price=50000, menu=menu_drink, image="menu_item_images/tra-cam-buoi-nhiet-doi.png")
            menu_item_tra_chanh_leo = MenuItem.objects.create(name="Trà chanh leo", description="Passionfruit tea", price=45000, menu=menu_drink, image="menu_item_images/tra-chanh-leo.png")
            menu_item_tra_dao_cam_xa = MenuItem.objects.create(name="Trà đào cam sả", description="Peach, orange, and lemongrass tea", price=45000, menu=menu_drink, image="menu_item_images/tra-dao-cam-xa.png")
            menu_item_tra_hoa_qua_dac_biet = MenuItem.objects.create(name="Trà hoa quả đặc biệt", description="Special fruit tea", price=50000, menu=menu_drink, image="menu_item_images/tra-hoa-qua-dac-biet.png")
            menu_item_tra_kiwi_hoa_com_chay = MenuItem.objects.create(name="Trà kiwi hoa cơm cháy", description="Kiwi tea", price=50000, menu=menu_drink, image="menu_item_images/tra-kiwi-hoa-com-chay.png")
            menu_item_tra_sua_gao_nho = MenuItem.objects.create(name="Trà sữa gạo nho", description="Milk tea with grape and rice", price=55000, menu=menu_drink, image="menu_item_images/tra-sua-gao-nho.png")
            menu_item_tra_sua_tran_chau = MenuItem.objects.create(name="Trà sữa trân châu", description="Milk tea with pearls", price=55000, menu=menu_drink, image="menu_item_images/tra-sua-tran-chau.png")
            menu_item_tra_vai = MenuItem.objects.create(name="Trà vải", description="Lychee tea", price=45000, menu=menu_drink, image="menu_item_images/tra-vai.png")
           

            
            # Example seeding for Order and OrderItem
            order_k = Order.objects.create(service_type="Dine-In", diner=diner_khanh, status='PENDING', note='Cho em ít hành với ạ', total_price=390000)
            order_item_k_carbonara = OrderItem.objects.create(order=order_k, menu_item=menu_item_carbonara_tteokbokki, quantity=2)
            order_item_k_special = OrderItem.objects.create(order=order_k, menu_item=menu_item_tra_hoa_qua_dac_biet, quantity=1)
            
            order_b = Order.objects.create(service_type="Dine-In", diner=diner_binh, status='PENDING', note='', total_price=280000)
            order_item_b_com_tron = OrderItem.objects.create(order=order_b, menu_item=menu_item_com_tron_bibimbap, quantity=1)
            order_item_b_mien_tron = OrderItem.objects.create(order=order_b, menu_item=menu_item_mien_tron, quantity=1)
            
            order_messi = Order.objects.create(service_type="Dine-In", diner=diner_messi, status='COMPLETED', note='I would like less ice in my drinks', total_price=710000)
            order_item_messi_ram_don = OrderItem.objects.create(order=order_messi, menu_item=menu_item_ram_don, quantity=3)
            order_item_messi_kimbap = OrderItem.objects.create(order=order_messi, menu_item=menu_item_kimbap_xa_xiu, quantity=2)
            order_item_messi_tra = OrderItem.objects.create(order=order_messi, menu_item=menu_item_tra_kiwi_hoa_com_chay, quantity=1)
            
            order_mbappe = Order.objects.create(service_type="Takeout", diner=diner_mbappe, status='COMPLETED', note='Extra spicy, please!', total_price=380000)
            order_item_mbappe_tteokbokki = OrderItem.objects.create(order=order_mbappe, menu_item=menu_item_tteokbokki_cha_ca, quantity=1)
            order_item_mbappe_kimbap = OrderItem.objects.create(order=order_mbappe, menu_item=menu_item_kimbap_bo_bulgogi, quantity=1)
            order_item_mbappe_tra = OrderItem.objects.create(order=order_mbappe, menu_item=menu_item_tra_sua_gao_nho, quantity=2)
            
            
            # Example seeding for Payment
            payment_k = Payment.objects.create(order=order_k, method='CASH', status='unpaid')
            payment_b = Payment.objects.create(order=order_b, method='CASH', status='unpaid')
            payment_messi = Payment.objects.create(order=order_messi, method='ONLINE_BANKING', status='paid')
            payment_mbappe = Payment.objects.create(order=order_mbappe, method='CASH', status='paid')
            
            # Example seeding for Feedback
            feedback_mbappe = Feedback.objects.create(order=order_mbappe, rating=5, comment="Great service!")
            feedback_messi = Feedback.objects.create(order=order_messi, rating=4, comment="The food was delicious, but the drinks were too sweet.")
            
            self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('DATABASE_SEEDING is set to False or not given. Skipping seeding...'))