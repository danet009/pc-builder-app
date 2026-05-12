from app import app, db
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case

print("1. Удаляем все старые таблицы...")
with app.app_context():
    db.drop_all()
    print("   Старые таблицы удалены.")

    print("2. Создаём новые таблицы с правильной структурой...")
    db.create_all()
    print("   Новые таблицы созданы.")

    print("3. Заполняем базу данных тестовыми компонентами...")
    
    for i in range(1, 31):
        db.session.add(CPU(name=f"CPU Model {i}", socket="LGA1700", tdp=65, price=10000 + i*500, reliability=4.0))
        db.session.add(Motherboard(name=f"MB Model {i}", socket="LGA1700", form_factor="ATX", price=8000 + i*300, reliability=4.0))
        db.session.add(RAM(name=f"RAM {i}GB", ram_type="DDR4", price=4000 + i*200, reliability=4.0))
        db.session.add(VideoCard(name=f"GPU {i}", chipset="Chipset", power_consumption=150, min_psu_wattage=500, length=250, price=15000 + i*1000, reliability=4.0))
        db.session.add(PowerSupply(name=f"PSU {i}00W", wattage=400 + i*50, rating="Bronze", price=3000 + i*300, reliability=4.0))
        db.session.add(Storage(name=f"Storage {i}GB", storage_type="SSD", interface="SATA III", capacity=256 + i*100, price=2000 + i*150, reliability=4.0))
        db.session.add(Case(name=f"Case {i}", form_factor="ATX, mATX", max_gpu_length=300 + i*10, max_cooler_height=160, fans_included=2, price=4000 + i*300, reliability=4.0))
    
    db.session.commit()
    print("   Все компоненты добавлены!")

    print("\n" + "="*50)
    print("✅ ГОТОВО! База данных успешно пересоздана и заполнена!")
    print(f"   Процессоров: {CPU.query.count()}")
    print(f"   Материнских плат: {Motherboard.query.count()}")
    print(f"   ОЗУ: {RAM.query.count()}")
    print(f"   Видеокарт: {VideoCard.query.count()}")
    print(f"   Блоков питания: {PowerSupply.query.count()}")
    print(f"   Накопителей: {Storage.query.count()}")
    print(f"   Корпусов: {Case.query.count()}")
    print("="*50)