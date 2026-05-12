import random
from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage

# ==================================================
# РЕАЛЬНЫЕ ЦЕНЫ (май 2026) на основе данных из поиска
# Источники: PCNEWS.ru, Чип и Дип, camelcamelcamel
# ==================================================

# 1. ПРОЦЕССОРЫ (реальные цены)
def generate_cpus():
    cpus = []
    # [name, socket, tdp, price, reliability]
    models = [
        # Intel LGA1700
        ('Intel Core i3-12100', 'LGA1700', 60, 9000, 4.3),
        ('Intel Core i3-13100', 'LGA1700', 60, 11000, 4.4),
        ('Intel Core i3-14100', 'LGA1700', 60, 12000, 4.4),
        ('Intel Core i5-12400', 'LGA1700', 65, 14000, 4.5),
        ('Intel Core i5-13400', 'LGA1700', 65, 15500, 4.6),
        ('Intel Core i5-13500', 'LGA1700', 65, 19000, 4.6),
        ('Intel Core i5-13600K', 'LGA1700', 125, 24000, 4.7),
        ('Intel Core i5-14400', 'LGA1700', 65, 17000, 4.6),
        ('Intel Core i5-14600K', 'LGA1700', 125, 28000, 4.7),
        ('Intel Core i7-12700K', 'LGA1700', 125, 26000, 4.6),
        ('Intel Core i7-13700K', 'LGA1700', 125, 32000, 4.8),
        ('Intel Core i7-14700K', 'LGA1700', 125, 37000, 4.8),
        ('Intel Core i9-12900K', 'LGA1700', 125, 38000, 4.7),
        ('Intel Core i9-13900K', 'LGA1700', 125, 48000, 4.8),
        ('Intel Core i9-14900K', 'LGA1700', 125, 54000, 4.8),
        # Intel LGA1851 (новые)
        ('Intel Core Ultra 5 225F', 'LGA1851', 65, 16000, 4.5),
        ('Intel Core Ultra 5 245K', 'LGA1851', 125, 28000, 4.6),
        ('Intel Core Ultra 7 265K', 'LGA1851', 125, 39000, 4.7),
        ('Intel Core Ultra 9 285K', 'LGA1851', 125, 58000, 4.8),
        # AMD AM5
        ('AMD Ryzen 5 7500F', 'AM5', 65, 11500, 4.5),
        ('AMD Ryzen 5 7600', 'AM5', 65, 16000, 4.6),
        ('AMD Ryzen 5 7600X', 'AM5', 105, 18000, 4.6),
        ('AMD Ryzen 7 7700', 'AM5', 65, 21000, 4.7),
        ('AMD Ryzen 7 7700X', 'AM5', 105, 24000, 4.7),
        ('AMD Ryzen 7 7800X3D', 'AM5', 120, 35000, 4.9),
        ('AMD Ryzen 7 9700X', 'AM5', 65, 29000, 4.7),
        ('AMD Ryzen 9 7900', 'AM5', 65, 32000, 4.7),
        ('AMD Ryzen 9 7900X', 'AM5', 170, 37000, 4.7),
        ('AMD Ryzen 9 7950X', 'AM5', 170, 50000, 4.8),
        ('AMD Ryzen 9 7950X3D', 'AM5', 120, 60000, 4.9),
        ('AMD Ryzen 9 9900X', 'AM5', 120, 43000, 4.8),
        ('AMD Ryzen 9 9950X', 'AM5', 170, 65000, 4.8),
    ]
    
    for name, socket, tdp, price, reliability in models:
        cpus.append(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=reliability))
    
    return cpus

# 2. МАТЕРИНСКИЕ ПЛАТЫ
def generate_motherboards():
    mbs = []
    # [name, socket, form_factor, price, reliability]
    models = [
        # LGA1700
        ('ASUS PRIME B660M-K D4', 'LGA1700', 'mATX', 8500, 4.4),
        ('MSI PRO B760M-A DDR4', 'LGA1700', 'mATX', 12000, 4.5),
        ('ASUS TUF GAMING B760-PLUS WIFI', 'LGA1700', 'ATX', 15200, 4.6),
        ('Gigabyte B760 AORUS ELITE', 'LGA1700', 'ATX', 14500, 4.5),
        ('MSI MPG Z790 CARBON WIFI', 'LGA1700', 'ATX', 28000, 4.7),
        ('ASUS ROG STRIX Z790-A', 'LGA1700', 'ATX', 31000, 4.8),
        ('Gigabyte Z790 AORUS MASTER', 'LGA1700', 'ATX', 35000, 4.7),
        # LGA1851
        ('ASUS PRIME B860M-A', 'LGA1851', 'mATX', 14000, 4.4),
        ('MSI PRO B860-VC WIFI', 'LGA1851', 'ATX', 16500, 4.5),
        ('Gigabyte Z890 AORUS ELITE', 'LGA1851', 'ATX', 28000, 4.7),
        # AM5
        ('ASUS PRIME B650M-R', 'AM5', 'mATX', 8000, 4.4),
        ('MSI PRO B650M-A', 'AM5', 'mATX', 9000, 4.4),
        ('Gigabyte B650 AORUS ELITE', 'AM5', 'ATX', 14000, 4.5),
        ('ASUS TUF GAMING B650-PLUS', 'AM5', 'ATX', 15500, 4.6),
        ('ASRock B650 PG Lightning', 'AM5', 'ATX', 11000, 4.4),
        ('MSI MPG B650 CARBON WIFI', 'AM5', 'ATX', 22000, 4.6),
        ('ASUS ROG STRIX X670E-E', 'AM5', 'ATX', 35000, 4.8),
        ('Gigabyte X670E AORUS MASTER', 'AM5', 'ATX', 38000, 4.7),
        ('ASRock X870E Taichi', 'AM5', 'ATX', 42000, 4.8),
    ]
    
    for name, socket, form_factor, price, reliability in models:
        mbs.append(Motherboard(name=name, socket=socket, form_factor=form_factor, price=price, reliability=reliability))
    
    return mbs

# 3. ОПЕРАТИВНАЯ ПАМЯТЬ
def generate_rams():
    rams = []
    # [name, ram_type, price, reliability]
    models = [
        # DDR4
        ('Kingston FURY 16GB DDR4-3200', 'DDR4', 5500, 4.5),
        ('Corsair Vengeance LPX 16GB DDR4-3200', 'DDR4', 5800, 4.5),
        ('G.Skill Aegis 16GB DDR4-3200', 'DDR4', 5200, 4.4),
        ('Crucial Ballistix 16GB DDR4-3600', 'DDR4', 6500, 4.6),
        ('Kingston FURY 32GB DDR4-3200', 'DDR4', 11000, 4.6),
        ('Corsair Vengeance 32GB DDR4-3600', 'DDR4', 13000, 4.7),
        ('G.Skill Trident Z 32GB DDR4-3600', 'DDR4', 12500, 4.6),
        # DDR5
        ('Kingston FURY 16GB DDR5-5600', 'DDR5', 7500, 4.6),
        ('Corsair Vengeance 16GB DDR5-6000', 'DDR5', 8500, 4.7),
        ('G.Skill Ripjaws S5 16GB DDR5-6000', 'DDR5', 8200, 4.6),
        ('TeamGroup T-Force 16GB DDR5-6000', 'DDR5', 7800, 4.5),
        ('Kingston FURY 32GB DDR5-5600', 'DDR5', 14500, 4.7),
        ('Corsair Vengeance 32GB DDR5-6000', 'DDR5', 16000, 4.7),
        ('G.Skill Trident Z5 32GB DDR5-6400', 'DDR5', 17500, 4.8),
        ('Kingston FURY 32GB DDR5-6000', 'DDR5', 15500, 4.7),
    ]
    
    for name, ram_type, price, reliability in models:
        rams.append(RAM(name=name, ram_type=ram_type, price=price, reliability=reliability))
    
    return rams

# 4. ВИДЕОКАРТЫ
def generate_gpus():
    gpus = []
    # [name, chipset, power, min_psu, price, reliability]
    models = [
        # NVIDIA
        ('Palit GeForce RTX 3050', 'RTX 3050', 130, 500, 19000, 4.3),
        ('MSI GeForce RTX 3060', 'RTX 3060', 170, 550, 25000, 4.4),
        ('ASUS GeForce RTX 3060 Ti', 'RTX 3060 Ti', 200, 600, 30000, 4.5),
        ('Gigabyte GeForce RTX 4060', 'RTX 4060', 115, 550, 31000, 4.6),
        ('MSI GeForce RTX 4060 Ti', 'RTX 4060 Ti', 160, 600, 38000, 4.6),
        ('ASUS GeForce RTX 4070', 'RTX 4070', 200, 650, 50000, 4.7),
        ('Gigabyte GeForce RTX 4070 Ti', 'RTX 4070 Ti', 285, 700, 65000, 4.7),
        ('MSI GeForce RTX 4080', 'RTX 4080', 320, 750, 90000, 4.8),
        ('ASUS GeForce RTX 4080 Super', 'RTX 4080 Super', 320, 750, 100000, 4.8),
        ('Palit GeForce RTX 4090', 'RTX 4090', 450, 850, 140000, 4.9),
        ('MSI GeForce RTX 5060', 'RTX 5060', 130, 550, 33000, 4.6),
        ('ASUS GeForce RTX 5070', 'RTX 5070', 220, 650, 58000, 4.7),
        ('Gigabyte GeForce RTX 5080', 'RTX 5080', 360, 800, 120000, 4.8),
        # AMD
        ('Sapphire Radeon RX 6600', 'RX 6600', 132, 500, 20000, 4.4),
        ('PowerColor Radeon RX 6700 XT', 'RX 6700 XT', 230, 650, 27000, 4.5),
        ('Sapphire Radeon RX 7600', 'RX 7600', 165, 550, 28000, 4.5),
        ('ASUS Radeon RX 7600 XT', 'RX 7600 XT', 190, 600, 32000, 4.5),
        ('PowerColor Radeon RX 7700 XT', 'RX 7700 XT', 245, 650, 40000, 4.6),
        ('Sapphire Radeon RX 7800 XT', 'RX 7800 XT', 263, 700, 50000, 4.7),
        ('XFX Radeon RX 7900 GRE', 'RX 7900 GRE', 260, 700, 55000, 4.7),
        ('ASRock Radeon RX 7900 XT', 'RX 7900 XT', 300, 750, 70000, 4.7),
        ('Sapphire Radeon RX 7900 XTX', 'RX 7900 XTX', 355, 800, 90000, 4.8),
        ('PowerColor Radeon RX 9060 XT', 'RX 9060 XT', 200, 650, 43000, 4.6),
        ('Sapphire Radeon RX 9070', 'RX 9070', 220, 650, 55000, 4.7),
        ('ASUS Radeon RX 9070 XT', 'RX 9070 XT', 300, 750, 65000, 4.8),
    ]
    
    for name, chipset, power, min_psu, price, reliability in models:
        gpus.append(VideoCard(name=name, chipset=chipset, power_consumption=power, 
                              min_psu_wattage=min_psu, price=price, reliability=reliability))
    
    return gpus

# 5. БЛОКИ ПИТАНИЯ
def generate_psus():
    psus = []
    # [name, wattage, rating, price, reliability]
    models = [
        ('be quiet! System Power 9 500W', 500, 'Bronze', 3500, 4.4),
        ('Cougar STX 550W', 550, 'Standard', 3000, 4.2),
        ('Montech BETA 650W', 650, 'Bronze', 4000, 4.4),
        ('Corsair CV650', 650, 'Bronze', 5500, 4.6),
        ('Deepcool PK650D', 650, 'Bronze', 5000, 4.5),
        ('Chieftec Proton 650W', 650, 'Bronze', 4800, 4.4),
        ('Cooler Master MWE 750W', 750, 'Bronze', 7000, 4.5),
        ('Corsair RM750e', 750, 'Gold', 9500, 4.7),
        ('be quiet! Pure Power 12 M 750W', 750, 'Gold', 10500, 4.7),
        ('Chieftec Proton 750W', 750, 'Gold', 7000, 4.5),
        ('Corsair RM850e', 850, 'Gold', 11000, 4.7),
        ('SeaSonic FOCUS GX-850', 850, 'Gold', 12000, 4.8),
        ('be quiet! Dark Power 13 1000W', 1000, 'Titanium', 25000, 4.9),
        ('Corsair RM1000e', 1000, 'Gold', 16000, 4.8),
        ('Chieftec Proton 1000W', 1000, 'Gold', 10000, 4.6),
    ]
    
    for name, wattage, rating, price, reliability in models:
        psus.append(PowerSupply(name=name, wattage=wattage, rating=rating, price=price, reliability=reliability))
    
    return psus

# 6. НАКОПИТЕЛИ
def generate_storages():
    storages = []
    # [name, storage_type, interface, capacity, price, reliability]
    models = [
        # SSD SATA
        ('Kingston A400 240GB', 'SSD', 'SATA III', 240, 2500, 4.3),
        ('Kingston A400 480GB', 'SSD', 'SATA III', 480, 3500, 4.3),
        ('Samsung 870 EVO 500GB', 'SSD', 'SATA III', 500, 5000, 4.5),
        ('Crucial BX500 1TB', 'SSD', 'SATA III', 1024, 6000, 4.4),
        ('Samsung 870 QVO 2TB', 'SSD', 'SATA III', 2048, 13000, 4.5),
        # SSD NVMe
        ('Samsung 980 500GB NVMe', 'SSD', 'M.2 PCIe 3.0', 500, 4500, 4.5),
        ('Kingston NV2 500GB', 'SSD', 'M.2 PCIe 4.0', 500, 4500, 4.4),
        ('Samsung 980 Pro 1TB NVMe', 'SSD', 'M.2 PCIe 4.0', 1024, 9500, 4.9),
        ('Western Digital SN770 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 8500, 4.7),
        ('Kingston KC3000 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 9000, 4.7),
        ('Samsung 990 Pro 1TB', 'SSD', 'M.2 PCIe 5.0', 1024, 12000, 4.9),
        ('Western Digital SN850X 2TB', 'SSD', 'M.2 PCIe 4.0', 2048, 16000, 4.8),
        ('Samsung 990 Pro 2TB', 'SSD', 'M.2 PCIe 5.0', 2048, 20000, 4.9),
        ('Kingston KC3000 2TB', 'SSD', 'M.2 PCIe 4.0', 2048, 14000, 4.7),
        # HDD
        ('Western Digital Blue 1TB', 'HDD', 'SATA III', 1024, 4000, 4.2),
        ('Seagate BarraCuda 2TB', 'HDD', 'SATA III', 2048, 5500, 4.3),
        ('Western Digital Blue 2TB', 'HDD', 'SATA III', 2048, 6000, 4.3),
        ('Seagate BarraCuda 4TB', 'HDD', 'SATA III', 4096, 9000, 4.3),
        ('Toshiba X300 4TB', 'HDD', 'SATA III', 4096, 10000, 4.2),
    ]
    
    for name, storage_type, interface, capacity, price, reliability in models:
        storages.append(Storage(name=name, storage_type=storage_type, interface=interface, 
                                capacity=capacity, price=price, reliability=reliability))
    
    return storages

# ==================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ==================================================
def add_all_components():
    with app.app_context():
        print("🔄 Удаляем старые данные...")
        CPU.query.delete()
        Motherboard.query.delete()
        RAM.query.delete()
        VideoCard.query.delete()
        PowerSupply.query.delete()
        Storage.query.delete()
        db.session.commit()
        print("✅ Старые данные удалены!")
        
        print("🔄 Добавляем компоненты с реальными ценами...")
        
        cpus = generate_cpus()
        print(f"   + Добавлено {len(cpus)} процессоров")
        
        mbs = generate_motherboards()
        print(f"   + Добавлено {len(mbs)} материнских плат")
        
        rams = generate_rams()
        print(f"   + Добавлено {len(rams)} модулей ОЗУ")
        
        gpus = generate_gpus()
        print(f"   + Добавлено {len(gpus)} видеокарт")
        
        psus = generate_psus()
        print(f"   + Добавлено {len(psus)} блоков питания")
        
        storages = generate_storages()
        print(f"   + Добавлено {len(storages)} накопителей")
        
        db.session.add_all(cpus + mbs + rams + gpus + psus + storages)
        db.session.commit()
        
        print("\n" + "="*50)
        print("🎉 ГОТОВО! В базу данных добавлено:")
        print(f"   • Процессоров: {CPU.query.count()}")
        print(f"   • Мат. плат: {Motherboard.query.count()}")
        print(f"   • ОЗУ: {RAM.query.count()}")
        print(f"   • Видеокарт: {VideoCard.query.count()}")
        print(f"   • Блоков питания: {PowerSupply.query.count()}")
        print(f"   • Накопителей: {Storage.query.count()}")
        print("="*50)

if __name__ == '__main__':
    add_all_components()