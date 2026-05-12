from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage

with app.app_context():
    # Добавляем процессоры
    cpu1 = CPU(name='Intel Core i5-13400', socket='LGA1700', tdp=65, price=16500, reliability=4.5)
    cpu2 = CPU(name='Intel Core i7-13700K', socket='LGA1700', tdp=125, price=31500, reliability=4.7)
    cpu3 = CPU(name='AMD Ryzen 5 7600', socket='AM5', tdp=65, price=15500, reliability=4.6)
    cpu4 = CPU(name='AMD Ryzen 7 7800X3D', socket='AM5', tdp=120, price=34500, reliability=4.9)
    
    # Материнские платы
    mb1 = Motherboard(name='ASUS TUF B760-PLUS', socket='LGA1700', form_factor='ATX', price=13500, reliability=4.6)
    mb2 = Motherboard(name='Gigabyte B650 AORUS', socket='AM5', form_factor='ATX', price=14500, reliability=4.5)
    
    # ОЗУ
    ram1 = RAM(name='Kingston FURY 16GB DDR5', ram_type='DDR5', price=7500, reliability=4.8)
    ram2 = RAM(name='Corsair Vengeance 16GB DDR4', ram_type='DDR4', price=5800, reliability=4.7)
    
    # Видеокарты
    gpu1 = VideoCard(name='NVIDIA GeForce RTX 4060', chipset='RTX 4060', power_consumption=115, min_psu_wattage=550, price=31000, reliability=4.6)
    gpu2 = VideoCard(name='AMD Radeon RX 7600', chipset='RX 7600', power_consumption=165, min_psu_wattage=550, price=28000, reliability=4.5)
    
    # Блоки питания
    psu1 = PowerSupply(name='Corsair CV650', wattage=650, rating='Bronze', price=5500, reliability=4.6)
    psu2 = PowerSupply(name='Corsair RM750e', wattage=750, rating='Gold', price=9500, reliability=4.8)
    
    # Накопители
    ssd1 = Storage(name='Samsung 980 Pro 1TB', storage_type='SSD', interface='M.2 PCIe 4.0', capacity=1024, price=9500, reliability=4.9)
    ssd2 = Storage(name='Kingston NV2 500GB', storage_type='SSD', interface='M.2 PCIe 4.0', capacity=500, price=4500, reliability=4.4)
    
    # Очищаем старые данные и добавляем новые
    CPU.query.delete()
    Motherboard.query.delete()
    RAM.query.delete()
    VideoCard.query.delete()
    PowerSupply.query.delete()
    Storage.query.delete()
    
    db.session.add_all([cpu1, cpu2, cpu3, cpu4, mb1, mb2, ram1, ram2, gpu1, gpu2, psu1, psu2, ssd1, ssd2])
    db.session.commit()
    
    print('✅ Добавлено:')
    print(f'   Процессоров: {CPU.query.count()}')
    print(f'   Материнских плат: {Motherboard.query.count()}')
    print(f'   ОЗУ: {RAM.query.count()}')
    print(f'   Видеокарт: {VideoCard.query.count()}')
    print(f'   Блоков питания: {PowerSupply.query.count()}')
    print(f'   Накопителей: {Storage.query.count()}')