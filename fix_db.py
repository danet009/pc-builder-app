from app import app, db

with app.app_context():
    # Добавляем колонку phone
    try:
        db.session.execute('ALTER TABLE user ADD COLUMN phone VARCHAR(20) DEFAULT ""')
        print('✅ Колонка phone добавлена')
    except Exception as e:
        print(f'⚠️ Колонка phone: {e}')
    
    # Добавляем колонку fullname
    try:
        db.session.execute('ALTER TABLE user ADD COLUMN fullname VARCHAR(100) DEFAULT ""')
        print('✅ Колонка fullname добавлена')
    except Exception as e:
        print(f'⚠️ Колонка fullname: {e}')
    
    db.session.commit()
    print('✅ Готово!')