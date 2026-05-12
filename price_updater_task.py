# price_updater_task.py (без циклических импортов)
import random
import requests
from bs4 import BeautifulSoup
import re

def update_all_prices():
    """Обновляет цены всех компонентов в базе данных"""
    # Импортируем внутри функции, чтобы избежать циклического импорта
    from app import app, db
    from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case
    
    print("🔄 Начинаем обновление цен...")
    
    with app.app_context():
        updated_total = 0
        
        # Обновляем процессоры
        cpus = CPU.query.all()
        for cpu in cpus:
            change = random.uniform(-0.03, 0.05)
            new_price = int(cpu.price * (1 + change))
            new_price = round(new_price / 100) * 100
            if cpu.price != new_price:
                cpu.price = new_price
                updated_total += 1
        
        # Обновляем материнские платы
        for mb in Motherboard.query.all():
            change = random.uniform(-0.02, 0.04)
            new_price = int(mb.price * (1 + change))
            new_price = round(new_price / 100) * 100
            if mb.price != new_price:
                mb.price = new_price
                updated_total += 1
        
        # Обновляем ОЗУ
        for ram in RAM.query.all():
            change = random.uniform(-0.01, 0.03)
            new_price = int(ram.price * (1 + change))
            new_price = round(new_price / 50) * 50
            if ram.price != new_price:
                ram.price = new_price
                updated_total += 1
        
        # Обновляем видеокарты
        for gpu in VideoCard.query.all():
            change = random.uniform(-0.05, 0.07)
            new_price = int(gpu.price * (1 + change))
            new_price = round(new_price / 500) * 500
            if gpu.price != new_price:
                gpu.price = new_price
                updated_total += 1
        
        # Обновляем блоки питания
        for psu in PowerSupply.query.all():
            change = random.uniform(-0.02, 0.04)
            new_price = int(psu.price * (1 + change))
            new_price = round(new_price / 100) * 100
            if psu.price != new_price:
                psu.price = new_price
                updated_total += 1
        
        # Обновляем накопители
        for storage in Storage.query.all():
            change = random.uniform(-0.03, 0.05)
            new_price = int(storage.price * (1 + change))
            new_price = round(new_price / 50) * 50
            if storage.price != new_price:
                storage.price = new_price
                updated_total += 1
        
        # Обновляем корпуса
        for case in Case.query.all():
            change = random.uniform(-0.02, 0.03)
            new_price = int(case.price * (1 + change))
            new_price = round(new_price / 100) * 100
            if case.price != new_price:
                case.price = new_price
                updated_total += 1
        
        db.session.commit()
        print(f"✅ Обновлено {updated_total} компонентов")
        return updated_total

def manual_update():
    """Функция для вызова из Flask-маршрута"""
    return update_all_prices()
