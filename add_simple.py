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
    
    # 30 процессоров
    for i in range(30):
        cpu = CPU(name=f'CPU {i+1}', socket='LGA1700', tdp=65, price=10000 + i*500, reliability=4.0)
        db.session.add(cpu)
    
    # 30 материнских плат
    for i in range(30):
        mb = Motherboard(name=f'Motherboard {i+1}', socket='LGA1700', form_factor='ATX', price=8000 + i*300, reliability=4.0)
        db.session.add(mb)
    
    # 30 ОЗУ
    for i in range(30):
        ram = RAM(name=f'RAM {i+1}', ram_type='DDR4', price=4000 + i*200, reliability=4.0)
        db.session.add(ram)
    
    # 30 видеокарт
    for i in range(30):
        gpu = VideoCard(name=f'GPU {i+1}', chipset='Chipset', power_consumption=150, min_psu_wattage=500, price=15000 + i*800, reliability=4.0)
        db.session.add(gpu)
    
    # 30 блоков питания
    for i in range(30):
        psu = PowerSupply(name=f'PSU {i+1}', wattage=500 + i*20, rating='Gold', price=4000 + i*200, reliability=4.0)
        db.session.add(psu)
    
    # 30 накопителей
    for i in range(30):
        storage = Storage(name=f'Storage {i+1}', storage_type='SSD', interface='M.2', capacity=256 + i*100, price=2000 + i*150, reliability=4.0)
        db.session.add(storage)
    
    # Сохраняем
    db.session.commit()
    
    print('=' * 50)
    print('✅ БАЗА ДАННЫХ ЗАПОЛНЕНА!')
    print('=' * 50)
    print(f'📊 Процессоров: {CPU.query.count()}')
    print(f'📊 Материнских плат: {Motherboard.query.count()}')
    print(f'📊 ОЗУ: {RAM.query.count()}')
    print(f'📊 Видеокарт: {VideoCard.query.count()}')
    print(f'📊 Блоков питания: {PowerSupply.query.count()}')
    print(f'📊 Накопителей: {Storage.query.count()}')
    print('=' * 50)