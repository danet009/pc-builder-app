import sqlite3

conn = sqlite3.connect('computers.db')
cursor = conn.cursor()

tables = ['cpu', 'motherboard', 'ram', 'video_card', 'power_supply', 'storage']

for table in tables:
    try:
        cursor.execute(f'ALTER TABLE {table} ADD COLUMN price INTEGER DEFAULT 0')
        print(f'✅ price добавлена в {table}')
    except Exception as e:
        print(f'⚠️ price в {table}: {e}')
    
    try:
        cursor.execute(f'ALTER TABLE {table} ADD COLUMN reliability FLOAT DEFAULT 4.0')
        print(f'✅ reliability добавлена в {table}')
    except Exception as e:
        print(f'⚠️ reliability в {table}: {e}')

conn.commit()
conn.close()
print('\n🎉 Готово!')