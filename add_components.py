from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case

with app.app_context():
    # Удаляем старые данные
    CPU.query.delete()
    Motherboard.query.delete()
    RAM.query.delete()
    VideoCard.query.delete()
    PowerSupply.query.delete()
    Storage.query.delete()
    Case.query.delete()
    
    # Добавляем 8 процессоров
    for i in range(1, 9):
        cpu = CPU(name=f"CPU Model {i}", socket="LGA1700", tdp=65, price=10000 + i*500, reliability=4.0)
        db.session.add(cpu)
    
    # Добавляем 8 материнских плат
    for i in range(1, 9):
        mb = Motherboard(name=f"MB Model {i}", socket="LGA1700", form_factor="ATX", price=8000 + i*300, reliability=4.0)
        db.session.add(mb)
    
    # Добавляем 8 ОЗУ
    for i in range(1, 9):
        ram = RAM(name=f"RAM {i}GB", ram_type="DDR4", price=4000 + i*200, reliability=4.0)
        db.session.add(ram)
    
    # Добавляем 8 видеокарт
    for i in range(1, 9):
        gpu = VideoCard(name=f"GPU {i}", chipset="Chipset", power_consumption=150, min_psu_wattage=500, length=250, price=15000 + i*1000, reliability=4.0)
        db.session.add(gpu)
    
    # Добавляем 8 блоков питания
    for i in range(1, 9):
        psu = PowerSupply(name=f"PSU {i}00W", wattage=400 + i*50, rating="Bronze", price=3000 + i*300, reliability=4.0)
        db.session.add(psu)
    
    # Добавляем 8 накопителей
    for i in range(1, 9):
        storage = Storage(name=f"Storage {i}GB", storage_type="SSD", interface="SATA III", capacity=256 + i*100, price=2000 + i*150, reliability=4.0)
        db.session.add(storage)
    
    # Добавляем 8 корпусов
    for i in range(1, 9):
        case = Case(name=f"Case {i}", form_factor="ATX, mATX", max_gpu_length=300 + i*10, max_cooler_height=160, fans_included=2, price=4000 + i*300, reliability=4.0)
        db.session.add(case)
    
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