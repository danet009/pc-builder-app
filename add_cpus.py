from app import app, db
from app import CPU

with app.app_context():
    # Очищаем старые данные
    CPU.query.delete()
    
    # Список процессоров
    cpus = [
        ("Intel Core i3-12100", "LGA1700", 60, 8500, 4.3),
        ("Intel Core i3-12100F", "LGA1700", 60, 7500, 4.2),
        ("Intel Core i3-13100", "LGA1700", 60, 10500, 4.4),
        ("Intel Core i5-12400", "LGA1700", 65, 13500, 4.5),
        ("Intel Core i5-12400F", "LGA1700", 65, 12500, 4.4),
        ("Intel Core i5-13400", "LGA1700", 65, 16500, 4.6),
        ("Intel Core i5-13400F", "LGA1700", 65, 15500, 4.5),
        ("Intel Core i5-13600K", "LGA1700", 125, 23500, 4.7),
        ("Intel Core i7-12700K", "LGA1700", 125, 25500, 4.6),
        ("Intel Core i7-13700K", "LGA1700", 125, 31500, 4.8),
        ("Intel Core i7-14700K", "LGA1700", 125, 36500, 4.8),
        ("Intel Core i9-13900K", "LGA1700", 125, 47500, 4.8),
        ("Intel Core i9-14900K", "LGA1700", 125, 53500, 4.8),
        ("AMD Ryzen 5 5500", "AM4", 65, 8500, 4.3),
        ("AMD Ryzen 5 5600", "AM4", 65, 11000, 4.4),
        ("AMD Ryzen 5 5600X", "AM4", 65, 12500, 4.5),
        ("AMD Ryzen 7 5700X", "AM4", 65, 16500, 4.5),
        ("AMD Ryzen 7 5800X", "AM4", 105, 18500, 4.6),
        ("AMD Ryzen 5 7500F", "AM5", 65, 11500, 4.5),
        ("AMD Ryzen 5 7600", "AM5", 65, 15500, 4.6),
        ("AMD Ryzen 5 7600X", "AM5", 105, 17500, 4.6),
        ("AMD Ryzen 7 7700", "AM5", 65, 20500, 4.7),
        ("AMD Ryzen 7 7700X", "AM5", 105, 23500, 4.7),
        ("AMD Ryzen 7 7800X3D", "AM5", 120, 34500, 4.9),
    ]
    
    # Добавляем процессоры
    for name, socket, tdp, price, rel in cpus:
        db.session.add(CPU(name=name, socket=socket, tdp=tdp, price=price, reliability=rel))
    
    # Сохраняем
    db.session.commit()
    
    print("=" * 50)
    print(f"✅ Добавлено процессоров: {CPU.query.count()}")
    print("=" * 50)