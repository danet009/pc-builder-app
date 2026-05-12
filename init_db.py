from app import app, db  
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage  
with app.app_context():  
    CPU.query.delete()  
    Motherboard.query.delete()  
    RAM.query.delete()  
    VideoCard.query.delete()  
    PowerSupply.query.delete()  
    Storage.query.delete()  
    for i in range(30):  
        db.session.add(CPU(name=f"CPU {i+1}", socket="LGA1700", tdp=65, price=10000 + i*500, reliability=4.0))  
        db.session.add(Motherboard(name=f"MB {i+1}", socket="LGA1700", form_factor="ATX", price=8000 + i*300, reliability=4.0))  
        db.session.add(RAM(name=f"RAM {i+1}", ram_type="DDR4", price=4000 + i*200, reliability=4.0))  
        db.session.add(VideoCard(name=f"GPU {i+1}", chipset="Generic", power_consumption=150, min_psu_wattage=500, price=15000 + i*800, reliability=4.0))  
        db.session.add(PowerSupply(name=f"PSU {i+1}", wattage=500 + i*20, rating="Gold", price=4000 + i*200, reliability=4.0))  
        db.session.add(Storage(name=f"Storage {i+1}", storage_type="SSD", interface="M.2", capacity=256 + i*100, price=2000 + i*150, reliability=4.0))  
    db.session.commit()  
    print("OK") 
