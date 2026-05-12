from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case

with app.app_context():
    CPU.query.delete()
    Motherboard.query.delete()
    RAM.query.delete()
    VideoCard.query.delete()
    PowerSupply.query.delete()
    Storage.query.delete()
    Case.query.delete()
    
    # Процессоры
    cpus = [
        ("Intel Core i5-13400", "LGA1700", 65, 16500, 4.6),
        ("Intel Core i7-13700K", "LGA1700", 125, 31500, 4.8),
        ("AMD Ryzen 5 7600", "AM5", 65, 15500, 4.6),
        ("AMD Ryzen 7 7800X3D", "AM5", 120, 34500, 4.9),
    ]
    for name, socket, tdp, price, rel in cpus:
        db.session.add(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=rel))
    
    # Материнские платы
    mbs = [
        ("ASUS TUF B760-PLUS", "LGA1700", "ATX", 13500, 4.6),
        ("ASUS ROG STRIX Z790-A", "LGA1700", "ATX", 30500, 4.8),
        ("Gigabyte B650 AORUS ELITE", "AM5", "ATX", 14500, 4.6),
        ("MSI PRO B650M-A", "AM5", "mATX", 9500, 4.5),
    ]
    for name, socket, ff, price, rel in mbs:
        db.session.add(Motherboard(name=name, socket=socket, form_factor=ff, price=price, reliability=rel))
    
    # ОЗУ
    rams = [
        ("Kingston FURY 16GB DDR5-5600", "DDR5", 7500, 4.7),
        ("Corsair Vengeance 16GB DDR5-6000", "DDR5", 8500, 4.8),
        ("Kingston FURY 16GB DDR4-3200", "DDR4", 5500, 4.5),
        ("Corsair Vengeance 16GB DDR4-3200", "DDR4", 5800, 4.5),
    ]
    for name, rtype, price, rel in rams:
        db.session.add(RAM(name=name, ram_type=rtype, price=price, reliability=rel))
    
    # Видеокарты
    gpus = [
        ("Gigabyte GeForce RTX 4060", "RTX 4060", 115, 550, 240, 31000, 4.7),
        ("MSI GeForce RTX 4060 Ti", "RTX 4060 Ti", 160, 600, 250, 38000, 4.7),
        ("Sapphire Radeon RX 7600", "RX 7600", 165, 550, 240, 28000, 4.6),
        ("Sapphire Radeon RX 7800 XT", "RX 7800 XT", 263, 700, 290, 50000, 4.8),
    ]
    for name, chip, power, min_psu, length, price, rel in gpus:
        db.session.add(VideoCard(name=name, chipset=chip, power_consumption=power, min_psu_wattage=min_psu, length=length, price=price, reliability=rel))
    
    # Блоки питания
    psus = [
        ("Corsair CV650", 650, "Bronze", 5500, 4.5),
        ("Corsair RM750e", 750, "Gold", 9500, 4.8),
        ("Chieftec Proton 750W", 750, "Gold", 7000, 4.6),
        ("be quiet! Dark Power 1000W", 1000, "Platinum", 18000, 4.9),
    ]
    for name, watt, rating, price, rel in psus:
        db.session.add(PowerSupply(name=name, wattage=watt, rating=rating, price=price, reliability=rel))
    
    # Накопители
    storages = [
        ("Samsung 980 Pro 1TB", "SSD", "M.2 PCIe 4.0", 1024, 9500, 4.9),
        ("Samsung 990 Pro 2TB", "SSD", "M.2 PCIe 5.0", 2048, 20000, 4.9),
        ("Kingston NV2 500GB", "SSD", "M.2 PCIe 4.0", 500, 4500, 4.4),
        ("Seagate BarraCuda 2TB", "HDD", "SATA III", 2048, 5500, 4.3),
    ]
    for name, stype, interface, cap, price, rel in storages:
        db.session.add(Storage(name=name, storage_type=stype, interface=interface, capacity=cap, price=price, reliability=rel))
    
    # Корпуса
    cases = [
        ("Corsair 4000D Airflow", "ATX, mATX, Mini-ITX", 360, 170, 2, 9000, 4.7),
        ("NZXT H510 Flow", "ATX, mATX", 360, 165, 2, 8500, 4.6),
        ("Fractal Design Meshify 2 Compact", "ATX, mATX, Mini-ITX", 341, 169, 2, 11000, 4.8),
        ("Lian Li LANCOOL 216", "ATX, mATX, Mini-ITX", 380, 180, 2, 10000, 4.7),
    ]
    for name, ff, max_gpu, cooler, fans, price, rel in cases:
        db.session.add(Case(name=name, form_factor=ff, max_gpu_length=max_gpu, max_cooler_height=cooler, fans_included=fans, price=price, reliability=rel))
    
    db.session.commit()
    
    print("=" * 50)
    print("✅ БАЗА ДАННЫХ ЗАПОЛНЕНА!")
    print(f"Процессоров: {CPU.query.count()}")
    print(f"Материнских плат: {Motherboard.query.count()}")
    print(f"ОЗУ: {RAM.query.count()}")
    print(f"Видеокарт: {VideoCard.query.count()}")
    print(f"Блоков питания: {PowerSupply.query.count()}")
    print(f"Накопителей: {Storage.query.count()}")
    print(f"Корпусов: {Case.query.count()}")
    print("=" * 50)