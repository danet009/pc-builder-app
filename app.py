# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import os
import atexit

# Импорты для автобновления цен
from apscheduler.schedulers.background import BackgroundScheduler
from price_updater_task import update_all_prices, manual_update

# =============================================
# СОЗДАНИЕ ПРИЛОЖЕНИЯ И КОНФИГУРАЦИЯ
# =============================================
app = Flask(__name__)
# PostgreSQL подключение (замените пароль на ваш)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/pc_builder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here-change-it'

db = SQLAlchemy(app)

# =============================================
# НАСТРОЙКА FLASK-LOGIN
# =============================================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Пожалуйста, войдите в систему'

# =============================================
# МОДЕЛИ БАЗЫ ДАННЫХ
# =============================================

class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    socket = db.Column(db.String(50), nullable=False)
    tdp = db.Column(db.Integer, default=65)
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    socket = db.Column(db.String(50), nullable=False)
    form_factor = db.Column(db.String(20))
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ram_type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class VideoCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    chipset = db.Column(db.String(50))
    power_consumption = db.Column(db.Integer)
    min_psu_wattage = db.Column(db.Integer)
    length = db.Column(db.Integer, default=250)
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class PowerSupply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wattage = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(20))
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    storage_type = db.Column(db.String(20))
    interface = db.Column(db.String(20))
    capacity = db.Column(db.Integer)
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    form_factor = db.Column(db.String(50))
    max_gpu_length = db.Column(db.Integer)
    max_cooler_height = db.Column(db.Integer)
    psu_position = db.Column(db.String(20))
    fans_included = db.Column(db.Integer)
    price = db.Column(db.Integer, default=0)
    reliability = db.Column(db.Float, default=4.0)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SavedBuild(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), default="Моя сборка")
    cpu_id = db.Column(db.Integer)
    motherboard_id = db.Column(db.Integer)
    ram_id = db.Column(db.Integer)
    gpu_id = db.Column(db.Integer)
    psu_id = db.Column(db.Integer)
    storage_id = db.Column(db.Integer)
    case_id = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    avg_reliability = db.Column(db.Float)
    total_power = db.Column(db.Integer)
    profit_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='builds')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =============================================
# ФУНКЦИИ ДЛЯ СЕРИАЛИЗАЦИИ ОБЪЕКТОВ В JSON
# =============================================

def to_dict(component, comp_type):
    base = {
        'id': component.id,
        'name': component.name,
        'price': component.price,
        'reliability': component.reliability,
        'type': comp_type
    }
    if comp_type == 'cpu':
        base['socket'] = component.socket
        base['tdp'] = component.tdp
    elif comp_type == 'motherboard':
        base['socket'] = component.socket
        base['form_factor'] = component.form_factor
    elif comp_type == 'ram':
        base['ram_type'] = component.ram_type
    elif comp_type == 'gpu':
        base['chipset'] = component.chipset
        base['power_consumption'] = component.power_consumption
        base['min_psu_wattage'] = component.min_psu_wattage
        base['length'] = component.length
    elif comp_type == 'psu':
        base['wattage'] = component.wattage
        base['rating'] = component.rating
    elif comp_type == 'storage':
        base['storage_type'] = component.storage_type
        base['interface'] = component.interface
        base['capacity'] = component.capacity
    elif comp_type == 'case':
        base['form_factor'] = component.form_factor
        base['max_gpu_length'] = component.max_gpu_length
        base['max_cooler_height'] = component.max_cooler_height
        base['fans_included'] = component.fans_included
    return base

# =============================================
# ФУНКЦИЯ РАСЧЁТА ВЫГОДНОСТИ
# =============================================
def calculate_profit_score(cpu, mb, ram, gpu, psu, storage, case, total_price, avg_reliability):
    price_score = max(0, 100 - (total_price / 20000))
    reliability_score = avg_reliability * 10
    component_score = 50
    if cpu and ('X3D' in cpu.name or 'K' in cpu.name):
        component_score += 10
    if psu and psu.rating in ['Gold', 'Platinum', 'Titanium']:
        component_score += 10
    if storage and 'Pro' in storage.name:
        component_score += 10
    if case and case.fans_included >= 3:
        component_score += 5
    return round((price_score * 0.4) + (reliability_score * 0.4) + (component_score * 0.2), 1)

# =============================================
# НАСТРОЙКА ПЛАНИРОВЩИКА ОБНОВЛЕНИЯ ЦЕН
# =============================================
def configure_scheduler():
    """Запускает фоновый планировщик для обновления цен"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=update_all_prices,
        trigger="interval",
        hours=24,
        id="price_updater_job",
        max_instances=1,
        replace_existing=True
    )
    scheduler.start()
    print("✅ Планировщик обновления цен запущен (каждые 24 часа)")
    atexit.register(lambda: scheduler.shutdown())
    return scheduler

# =============================================
# МАРШРУТЫ
# =============================================

@app.route('/')
def home():
    cpus = [to_dict(cpu, 'cpu') for cpu in CPU.query.all()]
    motherboards = [to_dict(mb, 'motherboard') for mb in Motherboard.query.all()]
    rams = [to_dict(ram, 'ram') for ram in RAM.query.all()]
    gpus = [to_dict(gpu, 'gpu') for gpu in VideoCard.query.all()]
    psus = [to_dict(psu, 'psu') for psu in PowerSupply.query.all()]
    storages = [to_dict(storage, 'storage') for storage in Storage.query.all()]
    cases = [to_dict(case, 'case') for case in Case.query.all()]
    
    return render_template('index.html',
                           cpus=cpus,
                           motherboards=motherboards,
                           rams=rams,
                           gpus=gpus,
                           psus=psus,
                           storages=storages,
                           cases=cases)

@app.route('/catalog')
def catalog():
    cpus = [to_dict(cpu, 'cpu') for cpu in CPU.query.all()]
    motherboards = [to_dict(mb, 'motherboard') for mb in Motherboard.query.all()]
    rams = [to_dict(ram, 'ram') for ram in RAM.query.all()]
    gpus = [to_dict(gpu, 'gpu') for gpu in VideoCard.query.all()]
    psus = [to_dict(psu, 'psu') for psu in PowerSupply.query.all()]
    storages = [to_dict(storage, 'storage') for storage in Storage.query.all()]
    cases = [to_dict(case, 'case') for case in Case.query.all()]
    
    return render_template('catalog.html',
                           cpus=cpus,
                           motherboards=motherboards,
                           rams=rams,
                           gpus=gpus,
                           psus=psus,
                           storages=storages,
                           cases=cases)

@app.route('/builder')
def builder():
    return redirect(url_for('home'))

@app.route('/test')
def test():
    return "<h1>Тест</h1><p>Flask работает!</p>"

@app.route('/product/<string:category>/<int:id>')
def product_detail(category, id):
    model_map = {
        'cpu': CPU, 'motherboard': Motherboard, 'ram': RAM,
        'gpu': VideoCard, 'psu': PowerSupply, 'storage': Storage,
        'case': Case
    }
    model = model_map.get(category)
    if not model:
        return redirect(url_for('catalog'))
    product = model.query.get_or_404(id)
    return render_template('product_detail.html', product=product, category=category)

@app.route('/check', methods=['POST'])
def check_compatibility():
    cpu_id = request.form.get('cpu_id')
    mb_id = request.form.get('motherboard_id')
    ram_id = request.form.get('ram_id')
    gpu_id = request.form.get('gpu_id')
    psu_id = request.form.get('psu_id')
    storage_id = request.form.get('storage_id')
    case_id = request.form.get('case_id')
    
    cpu = CPU.query.get(cpu_id)
    mb = Motherboard.query.get(mb_id)
    ram = RAM.query.get(ram_id)
    gpu = VideoCard.query.get(gpu_id)
    psu = PowerSupply.query.get(psu_id)
    storage = Storage.query.get(storage_id)
    case = Case.query.get(case_id)
    
    if not all([cpu, mb, ram, gpu, psu, storage, case]):
        return jsonify({'compatible': False, 'message': '❌ Ошибка: не все компоненты выбраны!'})
    
    errors = []
    warnings = []
    
    if cpu.socket != mb.socket:
        errors.append(f"❌ Сокет процессора '{cpu.socket}' не подходит к сокету материнской платы '{mb.socket}'.")
    
    if mb.socket == 'AM5' and ram.ram_type != 'DDR5':
        errors.append(f"❌ Материнская плата с сокетом {mb.socket} требует память типа DDR5.")
    elif mb.socket == 'LGA1700' and ram.ram_type not in ['DDR4', 'DDR5']:
        warnings.append(f"⚠️ Для материнской платы {mb.name} уточните тип памяти.")
    
    total_power = cpu.tdp + gpu.power_consumption + 50
    if psu.wattage < total_power:
        errors.append(f"❌ Блок питания {psu.wattage}Вт слишком слабый. Нужно минимум {total_power}Вт.")
    
    if psu.wattage < gpu.min_psu_wattage:
        warnings.append(f"⚠️ Производитель видеокарты рекомендует БП от {gpu.min_psu_wattage}Вт.")
    
    if mb.form_factor not in case.form_factor:
        errors.append(f"❌ Корпус '{case.name}' не поддерживает форм-фактор материнской платы '{mb.form_factor}'.")
    
    if gpu.length > case.max_gpu_length:
        errors.append(f"❌ Видеокарта '{gpu.name}' (длина {gpu.length}мм) не помещается в корпус '{case.name}' (макс. {case.max_gpu_length}мм).")
    
    total_price = cpu.price + mb.price + ram.price + gpu.price + psu.price + storage.price + case.price
    avg_reliability = (cpu.reliability + mb.reliability + ram.reliability + 
                       gpu.reliability + psu.reliability + storage.reliability + case.reliability) / 7
    
    if errors:
        return jsonify({'compatible': False, 'message': '\n'.join(errors), 
                       'total_price': total_price, 'avg_reliability': round(avg_reliability, 1)})
    
    message = f"✅ СБОРКА СОВМЕСТИМА!\n\n📊 Состав:\n"
    for item in [(cpu.name, cpu.price, cpu.reliability), (mb.name, mb.price, mb.reliability), 
                 (ram.name, ram.price, ram.reliability), (gpu.name, gpu.price, gpu.reliability),
                 (psu.name, psu.price, psu.reliability), (storage.name, storage.price, storage.reliability),
                 (case.name, case.price, case.reliability)]:
        message += f"  • {item[0]} — {item[1]}₽ ★{item[2]}\n"
    message += f"\n💰 ИТОГО: {total_price:,} ₽\n"
    message += f"⭐ СРЕДНИЙ РЕЙТИНГ: {avg_reliability:.1f} / 5.0\n"
    message += f"⚡ ЭНЕРГОПОТРЕБЛЕНИЕ: ~{total_power} Вт (БП {psu.wattage} Вт)"
    
    if warnings:
        message += "\n\n⚠️ Предупреждения:\n" + "\n".join(warnings)
    
    return jsonify({'compatible': True, 'message': message, 
                   'total_price': total_price, 'avg_reliability': round(avg_reliability, 1)})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form.get('confirm_password', '')
        
        if password != confirm_password:
            flash('Пароли не совпадают')
            return redirect(url_for('register'))
        if User.query.filter_by(username=username).first():
            flash('Пользователь с таким именем уже существует')
            return redirect(url_for('register'))
        if User.query.filter_by(email=email).first():
            flash('Пользователь с таким email уже существует')
            return redirect(url_for('register'))
        
        hashed = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed)
        db.session.add(new_user)
        db.session.commit()
        flash('Регистрация успешна! Теперь вы можете войти')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for(request.args.get('next', 'home')))
        else:
            flash('Неверное имя пользователя или пароль')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы')
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    builds = SavedBuild.query.filter_by(user_id=current_user.id).order_by(SavedBuild.created_at.desc()).all()
    builds_data = []
    for build in builds:
        builds_data.append({
            'build': build,
            'cpu': CPU.query.get(build.cpu_id),
            'mb': Motherboard.query.get(build.motherboard_id),
            'ram': RAM.query.get(build.ram_id),
            'gpu': VideoCard.query.get(build.gpu_id),
            'psu': PowerSupply.query.get(build.psu_id),
            'storage': Storage.query.get(build.storage_id),
            'case': Case.query.get(build.case_id)
        })
    return render_template('profile.html', user=current_user, builds=builds_data)

@app.route('/save_build', methods=['POST'])
@login_required
def save_build():
    data = request.get_json()
    cpu = CPU.query.get(data['cpu_id'])
    mb = Motherboard.query.get(data['motherboard_id'])
    ram = RAM.query.get(data['ram_id'])
    gpu = VideoCard.query.get(data['gpu_id'])
    psu = PowerSupply.query.get(data['psu_id'])
    storage = Storage.query.get(data['storage_id'])
    case = Case.query.get(data['case_id'])
    
    total_price = cpu.price + mb.price + ram.price + gpu.price + psu.price + storage.price + case.price
    avg_reliability = (cpu.reliability + mb.reliability + ram.reliability + gpu.reliability + 
                       psu.reliability + storage.reliability + case.reliability) / 7
    total_power = cpu.tdp + gpu.power_consumption + 50
    
    profit_score = calculate_profit_score(cpu, mb, ram, gpu, psu, storage, case, total_price, avg_reliability)
    
    saved = SavedBuild(
        user_id=current_user.id,
        cpu_id=cpu.id, motherboard_id=mb.id, ram_id=ram.id,
        gpu_id=gpu.id, psu_id=psu.id, storage_id=storage.id, case_id=case.id,
        total_price=total_price, avg_reliability=avg_reliability,
        total_power=total_power, profit_score=profit_score,
        name=f"Сборка от {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    )
    db.session.add(saved)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Сборка сохранена!', 'profit_score': profit_score})

@app.route('/export_pdf', methods=['POST'])
@login_required
def export_pdf():
    data = request.get_json()
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Спецификация сборки ПК")
    c.setFont("Helvetica", 12)
    y -= 30
    for line in data['report'].split('\n')[:30]:
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)
        c.drawString(50, y, line[:100])
        y -= 20
    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='sbornik.pdf', mimetype='application/pdf')

@app.route('/export_txt', methods=['POST'])
@login_required
def export_txt():
    data = request.get_json()
    return send_file(BytesIO(data['report'].encode('utf-8')), as_attachment=True,
                    download_name='sbornik.txt', mimetype='text/plain')

# =============================================
# АДМИН-МАРШРУТ ДЛЯ РУЧНОГО ОБНОВЛЕНИЯ ЦЕН
# =============================================
@app.route('/admin/update_prices')
@login_required
def admin_update_prices():
    if current_user.username != 'admin':
        flash('Доступ запрещён')
        return redirect(url_for('home'))
    result = manual_update()
    flash(result)
    return redirect(url_for('home'))

# =============================================
# ЗАПУСК ПРИЛОЖЕНИЯ
# =============================================
if __name__ == '__main__':
    # Запускаем планировщик только один раз (решаем проблему двойного запуска в debug)
    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        configure_scheduler()
    app.run(debug=True)
