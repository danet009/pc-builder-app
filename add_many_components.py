from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage

def add_many():
    with app.app_context():
        # Удаляем старые данные
        CPU.query.delete()
        Motherboard.query.delete()
        RAM.query.delete()
        VideoCard.query.delete()
        PowerSupply.query.delete()
        Storage.query.delete()
        
        # ===== ПРОЦЕССОРЫ (25 шт) =====
        cpus = []
        intel_models = [
            ('Intel Core i3-12100', 'LGA1700', 60, 8500),
            ('Intel Core i3-13100', 'LGA1700', 60, 10500),
            ('Intel Core i3-14100', 'LGA1700', 60, 11500),
            ('Intel Core i5-12400', 'LGA1700', 65, 13500),
            ('Intel Core i5-12400F', 'LGA1700', 65, 12500),
            ('Intel Core i5-13400', 'LGA1700', 65, 16500),
            ('Intel Core i5-13400F', 'LGA1700', 65, 15500),
            ('Intel Core i5-13500', 'LGA1700', 65, 18500),
            ('Intel Core i5-13600K', 'LGA1700', 125, 23500),
            ('Intel Core i5-14400', 'LGA1700', 65, 17500),
            ('Intel Core i5-14500', 'LGA1700', 65, 19500),
            ('Intel Core i5-14600K', 'LGA1700', 125, 27500),
            ('Intel Core i7-12700K', 'LGA1700', 125, 25500),
            ('Intel Core i7-13700K', 'LGA1700', 125, 31500),
            ('Intel Core i7-14700K', 'LGA1700', 125, 36500),
            ('Intel Core i9-12900K', 'LGA1700', 125, 37500),
            ('Intel Core i9-13900K', 'LGA1700', 125, 47500),
            ('Intel Core i9-14900K', 'LGA1700', 125, 53500),
            ('Intel Core Ultra 5 225F', 'LGA1851', 65, 15500),
            ('Intel Core Ultra 5 245K', 'LGA1851', 125, 27500),
            ('Intel Core Ultra 7 265K', 'LGA1851', 125, 38500),
            ('Intel Core Ultra 9 285K', 'LGA1851', 125, 57500),
            ('AMD Ryzen 5 5500', 'AM4', 65, 8500),
            ('AMD Ryzen 5 5600X', 'AM4', 65, 12500),
            ('AMD Ryzen 7 5700X', 'AM4', 65, 16500),
            ('AMD Ryzen 5 7500F', 'AM5', 65, 11500),
            ('AMD Ryzen 5 7600', 'AM5', 65, 15500),
            ('AMD Ryzen 5 7600X', 'AM5', 105, 17500),
            ('AMD Ryzen 7 7700', 'AM5', 65, 20500),
            ('AMD Ryzen 7 7700X', 'AM5', 105, 23500),
            ('AMD Ryzen 7 7800X3D', 'AM5', 120, 34500),
            ('AMD Ryzen 9 7900', 'AM5', 65, 31500),
            ('AMD Ryzen 9 7900X', 'AM5', 170, 36500),
            ('AMD Ryzen 9 7950X', 'AM5', 170, 49500),
            ('AMD Ryzen 9 7950X3D', 'AM5', 120, 59500),
        ]
        for name, socket, tdp, price in intel_models:
            cpus.append(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # ===== МАТЕРИНСКИЕ ПЛАТЫ (20 шт) =====
        mbs = []
        mb_models = [
            ('ASUS PRIME H610M-K', 'LGA1700', 'mATX', 6500),
            ('ASUS PRIME B660M-K', 'LGA1700', 'mATX', 8500),
            ('MSI PRO B760M-A', 'LGA1700', 'mATX', 9500),
            ('Gigabyte B760 GAMING X', 'LGA1700', 'ATX', 11500),
            ('ASUS TUF B760-PLUS', 'LGA1700', 'ATX', 13500),
            ('MSI MPG Z790 CARBON', 'LGA1700', 'ATX', 27500),
            ('ASUS ROG STRIX Z790-A', 'LGA1700', 'ATX', 30500),
            ('Gigabyte Z790 AORUS MASTER', 'LGA1700', 'ATX', 34500),
            ('ASRock B760 Pro RS', 'LGA1700', 'ATX', 11500),
            ('MSI PRO H610M-G', 'LGA1700', 'mATX', 7500),
            ('ASUS PRIME B760M-A', 'LGA1700', 'mATX', 10500),
            ('ASUS PRIME B650M-R', 'AM5', 'mATX', 8500),
            ('MSI PRO B650M-A', 'AM5', 'mATX', 9500),
            ('Gigabyte B650 AORUS ELITE', 'AM5', 'ATX', 14500),
            ('ASUS TUF B650-PLUS', 'AM5', 'ATX', 15500),
            ('ASRock B650 PG Lightning', 'AM5', 'ATX', 11500),
            ('MSI MPG B650 CARBON', 'AM5', 'ATX', 22500),
            ('ASUS ROG STRIX X670E-E', 'AM5', 'ATX', 35500),
            ('Gigabyte X670E AORUS MASTER', 'AM5', 'ATX', 38500),
            ('ASUS PRIME A620M-K', 'AM5', 'mATX', 7500),
        ]
        for name, socket, form_factor, price in mb_models:
            mbs.append(Motherboard(name=name, socket=socket, form_factor=form_factor, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # ===== ОПЕРАТИВНАЯ ПАМЯТЬ (20 шт) =====
        rams = []
        ram_models = [
            ('Kingston FURY 8GB DDR4-3200', 'DDR4', 3500),
            ('Corsair Vengeance 16GB DDR4-3200', 'DDR4', 5800),
            ('Kingston FURY 16GB DDR4-3200', 'DDR4', 5500),
            ('G.Skill Aegis 16GB DDR4-3200', 'DDR4', 5200),
            ('Corsair Vengeance 32GB DDR4-3600', 'DDR4', 13000),
            ('Kingston FURY 32GB DDR4-3600', 'DDR4', 11500),
            ('Kingston FURY 8GB DDR5-5600', 'DDR5', 4500),
            ('Kingston FURY 16GB DDR5-5600', 'DDR5', 7500),
            ('Corsair Vengeance 16GB DDR5-6000', 'DDR5', 8500),
            ('G.Skill Ripjaws 16GB DDR5-6000', 'DDR5', 8200),
            ('Kingston FURY 32GB DDR5-5600', 'DDR5', 14500),
            ('Corsair Vengeance 32GB DDR5-6000', 'DDR5', 16000),
            ('G.Skill Trident Z5 32GB DDR5-6400', 'DDR5', 17500),
            ('TeamGroup T-Force 16GB DDR5-6000', 'DDR5', 7800),
            ('Patriot Viper 16GB DDR4-3600', 'DDR4', 6200),
            ('Crucial Ballistix 16GB DDR4-3600', 'DDR4', 6500),
            ('ADATA XPG 16GB DDR5-6000', 'DDR5', 8000),
            ('Kingston FURY 64GB DDR5-5600', 'DDR5', 28000),
        ]
        for name, ram_type, price in ram_models:
            rams.append(RAM(name=name, ram_type=ram_type, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # ===== ВИДЕОКАРТЫ (15 шт) =====
        gpus = []
        gpu_models = [
            ('Palit GeForce RTX 3050', 'RTX 3050', 130, 500, 19000),
            ('MSI GeForce RTX 3060', 'RTX 3060', 170, 550, 25000),
            ('ASUS GeForce RTX 3060 Ti', 'RTX 3060 Ti', 200, 600, 30000),
            ('Gigabyte GeForce RTX 4060', 'RTX 4060', 115, 550, 31000),
            ('MSI GeForce RTX 4060 Ti', 'RTX 4060 Ti', 160, 600, 38000),
            ('ASUS GeForce RTX 4070', 'RTX 4070', 200, 650, 50000),
            ('Gigabyte GeForce RTX 4070 Ti', 'RTX 4070 Ti', 285, 700, 65000),
            ('MSI GeForce RTX 4080', 'RTX 4080', 320, 750, 90000),
            ('ASUS GeForce RTX 4080 Super', 'RTX 4080 Super', 320, 750, 100000),
            ('Palit GeForce RTX 4090', 'RTX 4090', 450, 850, 140000),
            ('Sapphire Radeon RX 6600', 'RX 6600', 132, 500, 20000),
            ('PowerColor Radeon RX 6700 XT', 'RX 6700 XT', 230, 650, 27000),
            ('Sapphire Radeon RX 7600', 'RX 7600', 165, 550, 28000),
            ('ASUS Radeon RX 7600 XT', 'RX 7600 XT', 190, 600, 32000),
            ('Sapphire Radeon RX 7800 XT', 'RX 7800 XT', 263, 700, 50000),
            ('XFX Radeon RX 7900 GRE', 'RX 7900 GRE', 260, 700, 55000),
            ('ASRock Radeon RX 7900 XT', 'RX 7900 XT', 300, 750, 70000),
        ]
        for name, chipset, power, min_psu, price in gpu_models:
            gpus.append(VideoCard(name=name, chipset=chipset, power_consumption=power, min_psu_wattage=min_psu, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # ===== БЛОКИ ПИТАНИЯ (15 шт) =====
        psus = []
        psu_models = [
            ('be quiet! System Power 9 500W', 500, 'Standard', 3500),
            ('Cougar STX 550W', 550, 'Standard', 3000),
            ('Montech BETA 650W', 650, 'Bronze', 4000),
            ('Corsair CV650', 650, 'Bronze', 5500),
            ('Deepcool PK650D', 650, 'Bronze', 5000),
            ('Chieftec Proton 650W', 650, 'Bronze', 4800),
            ('Cooler Master MWE 750W', 750, 'Bronze', 7000),
            ('Corsair RM750e', 750, 'Gold', 9500),
            ('be quiet! Pure Power 12 M 750W', 750, 'Gold', 10500),
            ('Chieftec Proton 750W', 750, 'Gold', 7000),
            ('Corsair RM850e', 850, 'Gold', 11000),
            ('SeaSonic FOCUS GX-850', 850, 'Gold', 12000),
            ('be quiet! Dark Power 13 1000W', 1000, 'Titanium', 25000),
            ('Corsair RM1000e', 1000, 'Gold', 16000),
            ('Chieftec Proton 1000W', 1000, 'Gold', 10000),
        ]
        for name, wattage, rating, price in psu_models:
            psus.append(PowerSupply(name=name, wattage=wattage, rating=rating, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # ===== НАКОПИТЕЛИ (15 шт) =====
        storages = []
        storage_models = [
            ('Kingston A400 240GB', 'SSD', 'SATA III', 240, 2500),
            ('Kingston A400 480GB', 'SSD', 'SATA III', 480, 3500),
            ('Samsung 870 EVO 500GB', 'SSD', 'SATA III', 500, 5000),
            ('Crucial BX500 1TB', 'SSD', 'SATA III', 1024, 6000),
            ('Samsung 980 500GB NVMe', 'SSD', 'M.2 PCIe 3.0', 500, 4500),
            ('Kingston NV2 500GB', 'SSD', 'M.2 PCIe 4.0', 500, 4500),
            ('Samsung 980 Pro 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 9500),
            ('Western Digital SN770 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 8500),
            ('Kingston KC3000 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 9000),
            ('Samsung 990 Pro 1TB', 'SSD', 'M.2 PCIe 5.0', 1024, 12000),
            ('Western Digital SN850X 2TB', 'SSD', 'M.2 PCIe 4.0', 2048, 16000),
            ('Samsung 990 Pro 2TB', 'SSD', 'M.2 PCIe 5.0', 2048, 20000),
            ('Western Digital Blue 1TB', 'HDD', 'SATA III', 1024, 4000),
            ('Seagate BarraCuda 2TB', 'HDD', 'SATA III', 2048, 5500),
            ('Seagate BarraCuda 4TB', 'HDD', 'SATA III', 4096, 9000),
        ]
        for name, stype, interface, capacity, price in storage_models:
            storages.append(Storage(name=name, storage_type=stype, interface=interface, capacity=capacity, price=price, reliability=round(4.0 + (price/100000), 1)))
        
        # Сохраняем всё
        db.session.add_all(cpus + mbs + rams + gpus + psus + storages)
        db.session.commit()
        
        print(f"✅ Добавлено:")
        print(f"   - Процессоров: {CPU.query.count()}")
        print(f"   - Материнских плат: {Motherboard.query.count()}")
        print(f"   - ОЗУ: {RAM.query.count()}")
        print(f"   - Видеокарт: {VideoCard.query.count()}")
        print(f"   - Блоков питания: {PowerSupply.query.count()}")
        print(f"   - Накопителей: {Storage.query.count()}")

if __name__ == '__main__':
    add_many()