from app import app, db

with app.app_context():
    # CPU
    try:
        db.session.execute('ALTER TABLE cpu ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE cpu ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    # Motherboard
    try:
        db.session.execute('ALTER TABLE motherboard ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE motherboard ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    # RAM
    try:
        db.session.execute('ALTER TABLE ram ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE ram ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    # VideoCard
    try:
        db.session.execute('ALTER TABLE video_card ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE video_card ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    # PowerSupply
    try:
        db.session.execute('ALTER TABLE power_supply ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE power_supply ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    # Storage
    try:
        db.session.execute('ALTER TABLE storage ADD COLUMN price INTEGER DEFAULT 0')
    except: pass
    try:
        db.session.execute('ALTER TABLE storage ADD COLUMN reliability FLOAT DEFAULT 4.0')
    except: pass
    
    db.session.commit()
    print('✅ Колонки price и reliability добавлены!')