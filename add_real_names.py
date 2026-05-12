from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage

with app.app_context():
    # Очищаем старые данные
    CPU.query.delete()
    Motherboard.query.delete()
    RAM.query.delete()
    VideoCard.query.delete()
    PowerSupply.query.delete()
    Storage.query.delete()
    
    # ===== ПРОЦЕССОРЫ (28 шт) =====
    cpus = [
        ('Intel Core i3-12100', 'LGA1700', 60, 8500, 4.3),
        ('Intel Core i3-12100F', 'LGA1700', 60, 7500, 4.2),
        ('Intel Core i3-13100', 'LGA1700', 60, 10500, 4.4),
        ('Intel Core i5-12400', 'LGA1700', 65, 13500, 4.5),
        ('Intel Core i5-12400F', 'LGA1700', 65, 12500, 4.4),
        ('Intel Core i5-13400', 'LGA1700', 65, 16500, 4.6),
        ('Intel Core i5-13400F', 'LGA1700', 65, 15500, 4.5),
        ('Intel Core i5-13600K', 'LGA1700', 125, 23500, 4.7),
        ('Intel Core i7-12700K', 'LGA1700', 125, 25500, 4.6),
        ('Intel Core i7-13700K', 'LGA1700', 125, 31500, 4.8),
        ('Intel Core i7-14700K', 'LGA1700', 125, 36500, 4.8),
        ('Intel Core i9-13900K', 'LGA1700', 125, 47500, 4.8),
        ('Intel Core i9-14900K', 'LGA1700', 125, 53500, 4.8),
        ('AMD Ryzen 5 5500', 'AM4', 65, 8500, 4.3),
        ('AMD Ryzen 5 5600', 'AM4', 65, 11000, 4.4),
        ('AMD Ryzen 5 5600X', 'AM4', 65, 12500, 4.5),
        ('AMD Ryzen 7 5700X', 'AM4', 65, 16500, 4.5),
        ('AMD Ryzen 7 5800X', 'AM4', 105, 18500, 4.6),
        ('AMD Ryzen 5 7500F', 'AM5', 65, 11500, 4.5),
        ('AMD Ryzen 5 7600', 'AM5', 65, 15500, 4.6),
        ('AMD Ryzen 5 7600X', 'AM5', 105, 17500, 4.6),
        ('AMD Ryzen 7 7700', 'AM5', 65, 20500, 4.7),
        ('AMD Ryzen 7 7700X', 'AM5', 105, 23500, 4.7),
        ('AMD Ryzen 7 7800X3D', 'AM5', 120, 34500, 4.9),
        ('AMD Ryzen 9 7900', 'AM5', 65, 31500, 4.7),
        ('AMD Ryzen 9 7900X', 'AM5', 170, 36500, 4.7),
        ('AMD Ryzen 9 7950X', 'AM5', 170, 49500, 4.8),
        ('AMD Ryzen 9 7950X3D', 'AM5', 120, 59500, 4.9),
    ]
    for name, socket, tdp, price, rel in cpus:
        db.session.add(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=rel))
    
    # ===== МАТЕРИНСКИЕ ПЛАТЫ (20 шт) =====
    motherboards = [
        ('ASUS PRIME H610M-K', 'LGA1700', 'mATX', 6500, 4.3),
        ('ASUS PRIME B660M-K', 'LGA1700', 'mATX', 8500, 4.4),
        ('MSI PRO B760M-A', 'LGA1700', 'mATX', 9500, 4.5),
        ('Gigabyte B760 GAMING X', 'LGA1700', 'ATX', 11500, 4.5),
        ('ASUS TUF B760-PLUS', 'LGA1700', 'ATX', 13500, 4.6),
        ('MSI MPG Z790 CARBON', 'LGA1700', 'ATX', 27500, 4.7),
        ('ASUS ROG STRIX Z790-A', 'LGA1700', 'ATX', 30500, 4.8),
        ('Gigabyte Z790 AORUS MASTER', 'LGA1700', 'ATX', 34500, 4.8),
        ('ASUS PRIME A520M-K', 'AM4', 'mATX', 5000, 4.2),
        ('MSI B550M PRO-VDH', 'AM4', 'mATX', 8500, 4.4),
        ('Gigabyte B550 AORUS ELITE', 'AM4', 'ATX', 11500, 4.5),
        ('ASUS ROG STRIX B550-F', 'AM4', 'ATX', 14500, 4.6),
        ('ASUS PRIME A620M-K', 'AM5', 'mATX', 7500, 4.3),
        ('ASUS PRIME B650M-R', 'AM5', 'mATX', 8500, 4.4),
        ('ASUS PRIME B650M-A', 'AM5', 'mATX', 9500, 4.4),
        ('MSI PRO B650M-A', 'AM5', 'mATX', 9500, 4.5),
        ('Gigabyte B650 AORUS ELITE', 'AM5', 'ATX', 14500, 4.6),
        ('ASUS TUF B650-PLUS', 'AM5', 'ATX', 15500, 4.6),
        ('ASRock B650 PG Lightning', 'AM5', 'ATX', 11500, 4.5),
        ('MSI MPG B650 CARBON', 'AM5', 'ATX', 22500, 4.7),
    ]
    for name, socket, ff, price, rel in motherboards:
        db.session.add(Motherboard(name=name, socket=socket, form_factor=ff, price=price, reliability=rel))
    
    # ===== ОПЕРАТИВНАЯ ПАМЯТЬ (10 шт) =====
    rams = [
        ('Kingston FURY 16GB DDR4-3200', 'DDR4', 5500, 4.5),
        ('Corsair Vengeance 16GB DDR4-3200', 'DDR4', 5800, 4.5),
        ('Kingston FURY 32GB DDR4-3200', 'DDR4', 11000, 4.5),
        ('Corsair Vengeance 32GB DDR4-3600', 'DDR4', 13000, 4.6),
        ('Kingston FURY 16GB DDR5-5600', 'DDR5', 7500, 4.7),
        ('Corsair Vengeance 16GB DDR5-6000', 'DDR5', 8500, 4.8),
        ('Kingston FURY 32GB DDR5-5600', 'DDR5', 14500, 4.7),
        ('Corsair Vengeance 32GB DDR5-6000', 'DDR5', 16000, 4.8),
        ('G.Skill Ripjaws 16GB DDR5-6000', 'DDR5', 8200, 4.7),
        ('G.Skill Trident Z5 32GB DDR5-6400', 'DDR5', 17500, 4.9),
    ]
    for name, rtype, price, rel in rams:
        db.session.add(RAM(name=name, ram_type=rtype, price=price, reliability=rel))
    
    # ===== ВИДЕОКАРТЫ (10 шт) =====
    gpus = [
        ('Palit GeForce RTX 3050', 'RTX 3050', 130, 500, 19000, 4.3),
        ('MSI GeForce RTX 3060', 'RTX 3060', 170, 550, 25000, 4.5),
        ('Gigabyte GeForce RTX 4060', 'RTX 4060', 115, 550, 31000, 4.7),
        ('MSI GeForce RTX 4060 Ti', 'RTX 4060 Ti', 160, 600, 38000, 4.7),
        ('ASUS GeForce RTX 4070', 'RTX 4070', 200, 650, 50000, 4.8),
        ('MSI GeForce RTX 4080', 'RTX 4080', 320, 750, 90000, 4.8),
        ('Palit GeForce RTX 4090', 'RTX 4090', 450, 850, 140000, 4.9),
        ('Sapphire Radeon RX 6600', 'RX 6600', 132, 500, 20000, 4.4),
        ('Sapphire Radeon RX 7600', 'RX 7600', 165, 550, 28000, 4.6),
        ('Sapphire Radeon RX 7800 XT', 'RX 7800 XT', 263, 700, 50000, 4.8),
    ]
    for name, chip, power, min_psu, price, rel in gpus:
        db.session.add(VideoCard(name=name, chipset=chip, power_consumption=power, min_psu_wattage=min_psu, price=price, reliability=rel))
    
    # ===== БЛОКИ ПИТАНИЯ (6 шт) =====
    psus = [
        ('Corsair CV650', 650, 'Bronze', 5500, 4.5),
        ('Corsair RM750e', 750, 'Gold', 9500, 4.8),
        ('Chieftec Proton 750W', 750, 'Gold', 7000, 4.6),
        ('be quiet! Dark Power 1000W', 1000, 'Platinum', 18000, 4.9),
        ('Cooler Master MWE 750W', 750, 'Bronze', 7000, 4.5),
        ('Deepcool PK650D', 650, 'Bronze', 5000, 4.4),
    ]
    for name, watt, rating, price, rel in psus:
        db.session.add(PowerSupply(name=name, wattage=watt, rating=rating, price=price, reliability=rel))
    
    # ===== НАКОПИТЕЛИ (5 шт) =====
    storages = [
        ('Samsung 980 Pro 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 9500, 4.9),
        ('Samsung 990 Pro 2TB', 'SSD', 'M.2 PCIe 5.0', 2048, 20000, 4.9),
        ('Kingston NV2 500GB', 'SSD', 'M.2 PCIe 4.0', 500, 4500, 4.4),
        ('Western Digital SN770 1TB', 'SSD', 'M.2 PCIe 4.0', 1024, 8500, 4.7),
        ('Seagate BarraCuda 2TB', 'HDD', 'SATA III', 2048, 5500, 4.3),
    ]
    for name, stype, interface, cap, price, rel in storages:
        db.session.add(Storage(name=name, storage_type=stype, interface=interface, capacity=cap, price=price, reliability=rel))
    
    db.session.commit()
    print('=' * 50)
    print('✅ БАЗА ДАННЫХ ОБНОВЛЕНА!')
    print(f'Процессоров: {CPU.query.count()}')
    print(f'Материнских плат: {Motherboard.query.count()}')
    print(f'ОЗУ: {RAM.query.count()}')
    print(f'Видеокарт: {VideoCard.query.count()}')
    print(f'Блоков питания: {PowerSupply.query.count()}')
    print(f'Накопителей: {Storage.query.count()}')
    print('=' * 50)