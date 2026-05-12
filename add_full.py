from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case

with app.app_context():
    # Очищаем старые данные
    CPU.query.delete()
    Motherboard.query.delete()
    RAM.query.delete()
    VideoCard.query.delete()
    PowerSupply.query.delete()
    Storage.query.delete()
    Case.query.delete()
    
    # ===== 1. ПРОЦЕССОРЫ (30 шт) =====
    cpus = [
        ("Intel Core i3-12100", "LGA1700", 60, 8500, 4.3),
        ("Intel Core i3-12100F", "LGA1700", 60, 7500, 4.2),
        ("Intel Core i3-13100", "LGA1700", 60, 10500, 4.4),
        ("Intel Core i3-13100F", "LGA1700", 60, 9500, 4.3),
        ("Intel Core i5-12400", "LGA1700", 65, 13500, 4.5),
        ("Intel Core i5-12400F", "LGA1700", 65, 12500, 4.4),
        ("Intel Core i5-13400", "LGA1700", 65, 16500, 4.6),
        ("Intel Core i5-13400F", "LGA1700", 65, 15500, 4.5),
        ("Intel Core i5-13500", "LGA1700", 65, 18500, 4.6),
        ("Intel Core i5-13600K", "LGA1700", 125, 23500, 4.7),
        ("Intel Core i5-13600KF", "LGA1700", 125, 22500, 4.7),
        ("Intel Core i5-14600K", "LGA1700", 125, 27500, 4.7),
        ("Intel Core i7-12700K", "LGA1700", 125, 25500, 4.6),
        ("Intel Core i7-13700K", "LGA1700", 125, 31500, 4.8),
        ("Intel Core i7-13700KF", "LGA1700", 125, 30500, 4.7),
        ("Intel Core i7-14700K", "LGA1700", 125, 36500, 4.8),
        ("Intel Core i7-14700KF", "LGA1700", 125, 35500, 4.8),
        ("Intel Core i9-12900K", "LGA1700", 125, 37500, 4.7),
        ("Intel Core i9-13900K", "LGA1700", 125, 47500, 4.8),
        ("Intel Core i9-13900KF", "LGA1700", 125, 46500, 4.8),
        ("Intel Core i9-14900K", "LGA1700", 125, 53500, 4.8),
        ("Intel Core i9-14900KF", "LGA1700", 125, 52500, 4.8),
        ("AMD Ryzen 5 5500", "AM4", 65, 8500, 4.3),
        ("AMD Ryzen 5 5600", "AM4", 65, 11000, 4.4),
        ("AMD Ryzen 5 5600X", "AM4", 65, 12500, 4.5),
        ("AMD Ryzen 7 5700X", "AM4", 65, 16500, 4.5),
        ("AMD Ryzen 7 5800X", "AM4", 105, 18500, 4.6),
        ("AMD Ryzen 5 7500F", "AM5", 65, 11500, 4.5),
        ("AMD Ryzen 5 7600", "AM5", 65, 15500, 4.6),
        ("AMD Ryzen 5 7600X", "AM5", 105, 17500, 4.6),
    ]
    for name, socket, tdp, price, rel in cpus:
        db.session.add(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=rel))
    
    # ===== 2. МАТЕРИНСКИЕ ПЛАТЫ (30 шт) =====
    motherboards = [
        ("ASUS PRIME H610M-K", "LGA1700", "mATX", 6500, 4.3),
        ("ASUS PRIME H610M-A", "LGA1700", "mATX", 7000, 4.3),
        ("ASUS PRIME B660M-K", "LGA1700", "mATX", 8500, 4.4),
        ("ASUS PRIME B660M-A", "LGA1700", "mATX", 9000, 4.4),
        ("MSI PRO B660M-A", "LGA1700", "mATX", 8800, 4.4),
        ("MSI PRO B760M-A", "LGA1700", "mATX", 9500, 4.5),
        ("MSI PRO B760M-G", "LGA1700", "mATX", 9000, 4.4),
        ("Gigabyte B760 GAMING X", "LGA1700", "ATX", 11500, 4.5),
        ("Gigabyte B760 AORUS ELITE", "LGA1700", "ATX", 12500, 4.6),
        ("ASUS TUF B760-PLUS", "LGA1700", "ATX", 13500, 4.6),
        ("ASUS TUF B760-PRO", "LGA1700", "ATX", 14500, 4.6),
        ("ASUS ROG STRIX B760-F", "LGA1700", "ATX", 16500, 4.7),
        ("MSI MPG Z790 CARBON", "LGA1700", "ATX", 27500, 4.7),
        ("ASUS ROG STRIX Z790-A", "LGA1700", "ATX", 30500, 4.8),
        ("Gigabyte Z790 AORUS MASTER", "LGA1700", "ATX", 34500, 4.8),
        ("ASUS PRIME Z790-P", "LGA1700", "ATX", 18500, 4.6),
        ("MSI PRO Z790-A", "LGA1700", "ATX", 20500, 4.6),
        ("Gigabyte Z790 UD", "LGA1700", "ATX", 17500, 4.5),
        ("ASRock Z790 Steel Legend", "LGA1700", "ATX", 19500, 4.6),
        ("ASUS PRIME A520M-K", "AM4", "mATX", 5000, 4.2),
        ("MSI B550M PRO-VDH", "AM4", "mATX", 8500, 4.4),
        ("Gigabyte B550 AORUS ELITE", "AM4", "ATX", 11500, 4.5),
        ("ASUS ROG STRIX B550-F", "AM4", "ATX", 14500, 4.6),
        ("MSI MPG B550 CARBON", "AM4", "ATX", 16500, 4.6),
        ("ASUS PRIME A620M-K", "AM5", "mATX", 7500, 4.3),
        ("ASUS PRIME B650M-R", "AM5", "mATX", 8500, 4.4),
        ("ASUS PRIME B650M-A", "AM5", "mATX", 9500, 4.4),
        ("MSI PRO B650M-A", "AM5", "mATX", 9500, 4.5),
        ("MSI PRO B650M-G", "AM5", "mATX", 9000, 4.4),
        ("Gigabyte B650 AORUS ELITE", "AM5", "ATX", 14500, 4.6),
    ]
    for name, socket, ff, price, rel in motherboards:
        db.session.add(Motherboard(name=name, socket=socket, form_factor=ff, price=price, reliability=rel))
    
    # ===== 3. ОПЕРАТИВНАЯ ПАМЯТЬ (30 шт) =====
    rams = [
        ("Kingston FURY 8GB DDR4-2666", "DDR4", 3200, 4.2),
        ("Kingston FURY 8GB DDR4-3200", "DDR4", 3500, 4.3),
        ("Kingston FURY 16GB DDR4-2666", "DDR4", 5200, 4.4),
        ("Kingston FURY 16GB DDR4-3200", "DDR4", 5500, 4.5),
        ("Kingston FURY 32GB DDR4-3200", "DDR4", 11000, 4.5),
        ("Corsair Vengeance 8GB DDR4-3200", "DDR4", 3000, 4.3),
        ("Corsair Vengeance 16GB DDR4-3200", "DDR4", 5800, 4.5),
        ("Corsair Vengeance 32GB DDR4-3200", "DDR4", 11500, 4.6),
        ("Corsair Vengeance 16GB DDR4-3600", "DDR4", 6500, 4.6),
        ("Corsair Vengeance 32GB DDR4-3600", "DDR4", 13000, 4.6),
        ("G.Skill Aegis 8GB DDR4-3200", "DDR4", 2800, 4.2),
        ("G.Skill Aegis 16GB DDR4-3200", "DDR4", 5200, 4.4),
        ("G.Skill Trident Z 16GB DDR4-3600", "DDR4", 7000, 4.6),
        ("G.Skill Trident Z 32GB DDR4-3600", "DDR4", 13500, 4.7),
        ("Crucial Ballistix 16GB DDR4-3600", "DDR4", 6500, 4.5),
        ("Kingston FURY 8GB DDR5-5600", "DDR5", 4500, 4.5),
        ("Kingston FURY 16GB DDR5-5600", "DDR5", 7500, 4.7),
        ("Kingston FURY 32GB DDR5-5600", "DDR5", 14500, 4.7),
        ("Kingston FURY 16GB DDR5-6000", "DDR5", 8200, 4.7),
        ("Kingston FURY 32GB DDR5-6000", "DDR5", 16500, 4.8),
        ("Corsair Vengeance 16GB DDR5-5600", "DDR5", 8000, 4.6),
        ("Corsair Vengeance 16GB DDR5-6000", "DDR5", 8500, 4.8),
        ("Corsair Vengeance 32GB DDR5-5600", "DDR5", 15000, 4.7),
        ("Corsair Vengeance 32GB DDR5-6000", "DDR5", 16000, 4.8),
        ("G.Skill Ripjaws 16GB DDR5-6000", "DDR5", 8200, 4.7),
        ("G.Skill Ripjaws 32GB DDR5-6000", "DDR5", 15500, 4.7),
        ("G.Skill Trident Z5 16GB DDR5-6400", "DDR5", 9500, 4.8),
        ("G.Skill Trident Z5 32GB DDR5-6400", "DDR5", 17500, 4.9),
        ("TeamGroup T-Force 16GB DDR5-6000", "DDR5", 7800, 4.6),
        ("TeamGroup T-Force 32GB DDR5-6000", "DDR5", 14800, 4.7),
    ]
    for name, rtype, price, rel in rams:
        db.session.add(RAM(name=name, ram_type=rtype, price=price, reliability=rel))
    
    # ===== 4. ВИДЕОКАРТЫ (30 шт) =====
    gpus = [
        ("Palit GeForce RTX 3050", "RTX 3050", 130, 500, 200, 19000, 4.3),
        ("MSI GeForce RTX 3060", "RTX 3060", 170, 550, 250, 25000, 4.5),
        ("ASUS GeForce RTX 3060 Ti", "RTX 3060 Ti", 200, 600, 260, 30000, 4.6),
        ("Gigabyte GeForce RTX 3060 Ti", "RTX 3060 Ti", 200, 600, 260, 29500, 4.6),
        ("MSI GeForce RTX 3070", "RTX 3070", 220, 650, 270, 35000, 4.6),
        ("ASUS GeForce RTX 3070 Ti", "RTX 3070 Ti", 290, 700, 280, 40000, 4.7),
        ("Gigabyte GeForce RTX 4060", "RTX 4060", 115, 550, 240, 31000, 4.7),
        ("MSI GeForce RTX 4060 Ti", "RTX 4060 Ti", 160, 600, 250, 38000, 4.7),
        ("ASUS GeForce RTX 4070", "RTX 4070", 200, 650, 260, 50000, 4.8),
        ("Gigabyte GeForce RTX 4070 Ti", "RTX 4070 Ti", 285, 700, 280, 65000, 4.8),
        ("MSI GeForce RTX 4080", "RTX 4080", 320, 750, 310, 90000, 4.8),
        ("ASUS GeForce RTX 4080 Super", "RTX 4080 Super", 320, 750, 310, 100000, 4.8),
        ("Palit GeForce RTX 4090", "RTX 4090", 450, 850, 330, 140000, 4.9),
        ("MSI GeForce RTX 4090", "RTX 4090", 450, 850, 330, 145000, 4.9),
        ("ASUS GeForce RTX 4090", "RTX 4090", 450, 850, 330, 150000, 4.9),
        ("Sapphire Radeon RX 6600", "RX 6600", 132, 500, 220, 20000, 4.4),
        ("PowerColor Radeon RX 6600 XT", "RX 6600 XT", 160, 550, 230, 23000, 4.5),
        ("ASUS Radeon RX 6650 XT", "RX 6650 XT", 180, 550, 240, 24000, 4.5),
        ("PowerColor Radeon RX 6700 XT", "RX 6700 XT", 230, 650, 270, 27000, 4.5),
        ("Sapphire Radeon RX 6750 XT", "RX 6750 XT", 250, 650, 280, 30000, 4.6),
        ("Sapphire Radeon RX 7600", "RX 7600", 165, 550, 240, 28000, 4.6),
        ("ASUS Radeon RX 7600 XT", "RX 7600 XT", 190, 600, 250, 32000, 4.6),
        ("PowerColor Radeon RX 7700 XT", "RX 7700 XT", 245, 650, 280, 40000, 4.6),
        ("Sapphire Radeon RX 7800 XT", "RX 7800 XT", 263, 700, 290, 50000, 4.8),
        ("XFX Radeon RX 7900 GRE", "RX 7900 GRE", 260, 700, 280, 55000, 4.7),
        ("ASRock Radeon RX 7900 XT", "RX 7900 XT", 300, 750, 300, 70000, 4.8),
        ("Sapphire Radeon RX 7900 XTX", "RX 7900 XTX", 355, 800, 320, 90000, 4.8),
        ("PowerColor Radeon RX 7900 XTX", "RX 7900 XTX", 355, 800, 320, 92000, 4.8),
        ("ASUS Radeon RX 7900 XTX", "RX 7900 XTX", 355, 800, 320, 95000, 4.8),
        ("XFX Radeon RX 7900 XTX", "RX 7900 XTX", 355, 800, 320, 93000, 4.8),
    ]
    for name, chip, power, min_psu, length, price, rel in gpus:
        db.session.add(VideoCard(name=name, chipset=chip, power_consumption=power, min_psu_wattage=min_psu, length=length, price=price, reliability=rel))
    
    # ===== 5. БЛОКИ ПИТАНИЯ (30 шт) =====
    psus = [
        ("be quiet! System Power 9 400W", 400, "Standard", 3000, 4.1),
        ("be quiet! System Power 9 500W", 500, "Standard", 3500, 4.2),
        ("be quiet! System Power 9 600W", 600, "Standard", 4000, 4.2),
        ("Cougar STX 550W", 550, "Standard", 3000, 4.1),
        ("Cougar STX 650W", 650, "Standard", 3500, 4.2),
        ("Montech BETA 550W", 550, "Bronze", 3500, 4.2),
        ("Montech BETA 650W", 650, "Bronze", 4000, 4.3),
        ("Montech BETA 750W", 750, "Bronze", 5000, 4.3),
        ("Corsair CV550", 550, "Bronze", 4500, 4.4),
        ("Corsair CV650", 650, "Bronze", 5500, 4.5),
        ("Corsair CV750", 750, "Bronze", 6500, 4.5),
        ("Deepcool PK550D", 550, "Bronze", 4200, 4.3),
        ("Deepcool PK650D", 650, "Bronze", 5000, 4.4),
        ("Deepcool PK750D", 750, "Bronze", 6000, 4.4),
        ("Chieftec Proton 550W", 550, "Bronze", 4000, 4.3),
        ("Chieftec Proton 650W", 650, "Bronze", 4800, 4.4),
        ("Chieftec Proton 750W", 750, "Gold", 7000, 4.6),
        ("Chieftec Proton 850W", 850, "Gold", 8500, 4.6),
        ("Cooler Master MWE 550W", 550, "Bronze", 5000, 4.3),
        ("Cooler Master MWE 650W", 650, "Bronze", 6000, 4.4),
        ("Cooler Master MWE 750W", 750, "Bronze", 7000, 4.5),
        ("Corsair RM550e", 550, "Gold", 8500, 4.7),
        ("Corsair RM650e", 650, "Gold", 9000, 4.7),
        ("Corsair RM750e", 750, "Gold", 9500, 4.8),
        ("Corsair RM850e", 850, "Gold", 11000, 4.8),
        ("Corsair RM1000e", 1000, "Gold", 16000, 4.8),
        ("be quiet! Pure Power 12 M 550W", 550, "Gold", 8500, 4.7),
        ("be quiet! Pure Power 12 M 650W", 650, "Gold", 9500, 4.7),
        ("be quiet! Pure Power 12 M 750W", 750, "Gold", 10500, 4.8),
        ("be quiet! Pure Power 12 M 850W", 850, "Gold", 12500, 4.8),
    ]
    for name, watt, rating, price, rel in psus:
        db.session.add(PowerSupply(name=name, wattage=watt, rating=rating, price=price, reliability=rel))
    
    # ===== 6. НАКОПИТЕЛИ (30 шт) =====
    storages = [
        ("Kingston A400 120GB", "SSD", "SATA III", 120, 2000, 4.1),
        ("Kingston A400 240GB", "SSD", "SATA III", 240, 2500, 4.2),
        ("Kingston A400 480GB", "SSD", "SATA III", 480, 3500, 4.3),
        ("Kingston A400 960GB", "SSD", "SATA III", 960, 5500, 4.4),
        ("Kingston NV1 500GB", "SSD", "M.2 PCIe 3.0", 500, 4000, 4.3),
        ("Kingston NV1 1TB", "SSD", "M.2 PCIe 3.0", 1024, 6500, 4.4),
        ("Kingston NV2 250GB", "SSD", "M.2 PCIe 4.0", 250, 3000, 4.3),
        ("Kingston NV2 500GB", "SSD", "M.2 PCIe 4.0", 500, 4500, 4.4),
        ("Kingston NV2 1TB", "SSD", "M.2 PCIe 4.0", 1024, 7000, 4.5),
        ("Kingston NV2 2TB", "SSD", "M.2 PCIe 4.0", 2048, 12000, 4.5),
        ("Samsung 870 EVO 250GB", "SSD", "SATA III", 250, 4000, 4.5),
        ("Samsung 870 EVO 500GB", "SSD", "SATA III", 500, 5000, 4.6),
        ("Samsung 870 EVO 1TB", "SSD", "SATA III", 1024, 8000, 4.7),
        ("Samsung 970 EVO Plus 500GB", "SSD", "M.2 PCIe 3.0", 500, 5500, 4.7),
        ("Samsung 970 EVO Plus 1TB", "SSD", "M.2 PCIe 3.0", 1024, 9000, 4.8),
        ("Samsung 980 500GB", "SSD", "M.2 PCIe 3.0", 500, 4500, 4.6),
        ("Samsung 980 1TB", "SSD", "M.2 PCIe 3.0", 1024, 7500, 4.6),
        ("Samsung 980 Pro 500GB", "SSD", "M.2 PCIe 4.0", 500, 6500, 4.8),
        ("Samsung 980 Pro 1TB", "SSD", "M.2 PCIe 4.0", 1024, 9500, 4.9),
        ("Samsung 980 Pro 2TB", "SSD", "M.2 PCIe 4.0", 2048, 16500, 4.9),
        ("Samsung 990 Pro 1TB", "SSD", "M.2 PCIe 5.0", 1024, 12000, 4.9),
        ("Samsung 990 Pro 2TB", "SSD", "M.2 PCIe 5.0", 2048, 20000, 4.9),
        ("Western Digital SN770 500GB", "SSD", "M.2 PCIe 4.0", 500, 5000, 4.6),
        ("Western Digital SN770 1TB", "SSD", "M.2 PCIe 4.0", 1024, 8500, 4.7),
        ("Western Digital SN770 2TB", "SSD", "M.2 PCIe 4.0", 2048, 15000, 4.7),
        ("Western Digital Blue 500GB", "HDD", "SATA III", 500, 3000, 4.2),
        ("Western Digital Blue 1TB", "HDD", "SATA III", 1024, 4000, 4.2),
        ("Seagate BarraCuda 1TB", "HDD", "SATA III", 1024, 4200, 4.2),
        ("Seagate BarraCuda 2TB", "HDD", "SATA III", 2048, 5500, 4.3),
        ("Seagate BarraCuda 4TB", "HDD", "SATA III", 4096, 9000, 4.3),
    ]
    for name, stype, interface, cap, price, rel in storages:
        db.session.add(Storage(name=name, storage_type=stype, interface=interface, capacity=cap, price=price, reliability=rel))
    
    # ===== 7. КОРПУСА (30 шт) =====
    cases = [
        ("Fractal Design Define 7", "ATX, mATX, Mini-ITX", 315, 185, 2, 12000, 4.8),
        ("NZXT H510 Flow", "ATX, mATX", 360, 165, 2, 8500, 4.6),
        ("be quiet! Pure Base 500DX", "ATX, mATX, Mini-ITX", 369, 190, 3, 10000, 4.7),
        ("Corsair 4000D Airflow", "ATX, mATX, Mini-ITX", 360, 170, 2, 9000, 4.7),
        ("Lian Li LANCOOL 215", "ATX, mATX, Mini-ITX", 370, 166, 3, 9500, 4.8),
        ("Cooler Master MasterBox MB511", "ATX, mATX, Mini-ITX", 410, 165, 3, 6500, 4.5),
        ("Deepcool MATREXX 55 V3", "ATX, mATX", 370, 165, 2, 4500, 4.3),
        ("Phanteks Eclipse P400A", "ATX, mATX, Mini-ITX", 420, 160, 3, 8500, 4.6),
        ("Fractal Design Meshify 2 Compact", "ATX, mATX, Mini-ITX", 341, 169, 2, 11000, 4.8),
        ("Corsair 5000D Airflow", "ATX, mATX, Mini-ITX", 400, 170, 2, 13000, 4.8),
        ("NZXT H7 Flow", "ATX, mATX, Mini-ITX", 400, 185, 3, 11000, 4.7),
        ("Lian Li O11 Dynamic", "ATX, mATX, Mini-ITX", 420, 155, 0, 14000, 4.8),
        ("be quiet! Silent Base 802", "ATX, mATX, Mini-ITX", 287, 185, 3, 15000, 4.9),
        ("Cooler Master HAF 500", "ATX, mATX, Mini-ITX", 410, 165, 4, 12000, 4.7),
        ("Deepcool CK560", "ATX, mATX", 380, 175, 4, 7000, 4.5),
        ("Fractal Design Pop Air", "ATX, mATX, Mini-ITX", 405, 170, 3, 8000, 4.6),
        ("NZXT H9 Elite", "ATX, mATX, Mini-ITX", 435, 165, 4, 18000, 4.8),
        ("Corsair 7000D Airflow", "ATX, mATX, Mini-ITX", 450, 190, 3, 19000, 4.8),
        ("Lian Li LANCOOL 216", "ATX, mATX, Mini-ITX", 380, 180, 2, 10000, 4.7),
        ("be quiet! Pure Base 500", "ATX, mATX, Mini-ITX", 318, 190, 2, 8000, 4.6),
        ("Thermaltake View 200 TG", "ATX, mATX, Mini-ITX", 400, 160, 3, 7500, 4.4),
        ("Antec DF700 Flux", "ATX, mATX, Mini-ITX", 405, 175, 5, 8000, 4.5),
        ("Phanteks Eclipse G360A", "ATX, mATX, Mini-ITX", 400, 162, 3, 9500, 4.6),
        ("Deepcool CC560", "ATX, mATX", 370, 165, 4, 5000, 4.3),
        ("Fractal Design North", "ATX, mATX, Mini-ITX", 355, 170, 2, 13000, 4.8),
        ("NZXT H510 Elite", "ATX, mATX", 360, 165, 2, 12000, 4.5),
        ("Corsair iCUE 4000X RGB", "ATX, mATX, Mini-ITX", 360, 170, 3, 11500, 4.7),
        ("Lian Li O11 Air Mini", "ATX, mATX, Mini-ITX", 362, 170, 3, 11000, 4.7),
        ("Cooler Master NR200", "Mini-ITX", 330, 155, 2, 7000, 4.6),
        ("Fractal Design Torrent Compact", "ATX, mATX, Mini-ITX", 330, 174, 4, 14000, 4.9),
    ]
    for name, ff, max_gpu, max_cooler, fans, price, rel in cases:
        db.session.add(Case(name=name, form_factor=ff, max_gpu_length=max_gpu, max_cooler_height=max_cooler, fans_included=fans, price=price, reliability=rel))
    
    db.session.commit()
    
    print("=" * 50)
    print("✅ БАЗА ДАННЫХ ЗАПОЛНЕНА РЕАЛЬНЫМИ КОМПОНЕНТАМИ!")
    print(f"📊 Процессоров: {CPU.query.count()}")
    print(f"📊 Материнских плат: {Motherboard.query.count()}")
    print(f"📊 ОЗУ: {RAM.query.count()}")
    print(f"📊 Видеокарт: {VideoCard.query.count()}")
    print(f"📊 Блоков питания: {PowerSupply.query.count()}")
    print(f"📊 Накопителей: {Storage.query.count()}")
    print(f"📊 Корпусов: {Case.query.count()}")
    print("=" * 50)