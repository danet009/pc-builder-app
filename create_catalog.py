catalog_html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Каталог — Компьютерный Мир</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; }
        .header { background: #1a2a6c; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
        .logo { font-size: 24px; font-weight: bold; }
        .logo span { color: #fdbb4d; }
        .nav a { color: white; text-decoration: none; margin: 0 15px; }
        .container { max-width: 1400px; margin: 20px auto; padding: 20px; }
        h1 { text-align: center; color: #1a2a6c; margin-bottom: 30px; }
        .section-title { font-size: 28px; color: #1a2a6c; margin: 40px 0 20px; padding-bottom: 10px; border-bottom: 3px solid #fdbb4d; display: flex; justify-content: space-between; align-items: flex-end; }
        .section-count { font-size: 14px; color: #666; font-weight: normal; }
        .catalog { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }
        .product-card { background: white; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.2s, box-shadow 0.2s; cursor: pointer; }
        .product-card:hover { transform: translateY(-5px); box-shadow: 0 8px 20px rgba(0,0,0,0.15); }
        .product-title { font-size: 18px; font-weight: bold; margin-bottom: 12px; color: #1a2a6c; border-left: 4px solid #fdbb4d; padding-left: 12px; }
        .product-specs { font-size: 13px; color: #555; margin: 10px 0; line-height: 1.5; }
        .product-specs span { display: inline-block; background: #f0f2f5; padding: 3px 8px; border-radius: 12px; margin: 3px 3px 0 0; font-size: 11px; }
        .product-price { font-size: 22px; font-weight: bold; color: #b21f1f; margin: 12px 0 8px; }
        .product-rating { color: #fdbb4d; margin: 8px 0; font-size: 14px; }
        a { text-decoration: none; color: inherit; display: block; }
        footer { background: #1a2a6c; color: white; text-align: center; padding: 25px; margin-top: 50px; }
        @media (max-width: 768px) { .header { flex-direction: column; text-align: center; } .catalog { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">🖥️ <span>Компьютерный</span> Мир</div>
        <div class="nav">
            <a href="/">Конфигуратор</a>
            <a href="/catalog">Каталог</a>
            <a href="/profile">Мои сборки</a>
            <a href="/login">Войти</a>
            <a href="/register">Регистрация</a>
        </div>
    </header>
    <div class="container">
        <h1>📦 Каталог компьютерных комплектующих</h1>
        <p style="text-align:center; color:#666; margin-bottom:30px;">Подробные технические характеристики всех компонентов</p>
        
        <div class="section-title">⚙️ Процессоры <span class="section-count">{{ cpus|length }} моделей</span></div>
        <div class="catalog">
            {% for cpu in cpus %}
            <a href="/product/cpu/{{ cpu.id }}">
                <div class="product-card">
                    <div class="product-title">{{ cpu.name }}</div>
                    <div class="product-specs"><span>🔌 {{ cpu.socket }}</span> <span>⚡ {{ cpu.tdp }} Вт</span></div>
                    <div class="product-rating">⭐ {{ cpu.reliability }} / 5</div>
                    <div class="product-price">{{ cpu.price }} ₽</div>
                </div>
            </a>
            {% endfor %}
        </div>
    </div>
    <footer>© 2025 «Компьютерный Мир» — Ваш надёжный помощник в сборке ПК</footer>
</body>
</html>'''

with open('templates/catalog.html', 'w', encoding='utf-8') as f:
    f.write(catalog_html)

print("✅ Файл templates/catalog.html создан!")
