from app import app, db  
from app import CPU, Motherboard, RAM, VideoCard, PowerSupply, Storage, Case  
  
with app.app_context():  
    CPU.query.delete()  
    Motherboard.query.delete()  
    RAM.query.delete()  
    VideoCard.query.delete()  
    PowerSupply.query.delete()  
    Storage.query.delete()  
    Case.query.delete()  
  
    # CPU (30 шт)  
    cpus_data = [('Intel Core i5-13400','LGA1700',65,16500,4.6),('Intel Core i7-13700K','LGA1700',125,31500,4.8),('AMD Ryzen 5 7600','AM5',65,15500,4.6),('AMD Ryzen 7 7800X3D','AM5',120,34500,4.9)]  
    for n,s,t,p,r in cpus_data: db.session.add(CPU(name=n, socket=s, tdp=t, price=p, reliability=r))  
  
    # Motherboard (4 шт)  
    mb_data = [('ASUS TUF B760-PLUS','LGA1700','ATX',13500,4.6),('Gigabyte B650 AORUS ELITE','AM5','ATX',14500,4.6)]  
    for n,s,f,p,r in mb_data: db.session.add(Motherboard(name=n, socket=s, form_factor=f, price=p, reliability=r))  
  
    # RAM (4 шт)  
    ram_data = [('Kingston FURY 16GB DDR5','DDR5',7500,4.7),('Corsair Vengeance 16GB DDR5','DDR5',8500,4.8)]  
    for n,t,p,r in ram_data: db.session.add(RAM(name=n, ram_type=t, price=p, reliability=r))  
  
    # GPU (4 шт)  
    gpu_data = [('NVIDIA RTX 4060','RTX 4060',115,550,240,31000,4.7),('AMD RX 7600','RX 7600',165,550,240,28000,4.6)]  
    for n,c,pw,mp,l,pr,r in gpu_data: db.session.add(VideoCard(name=n, chipset=c, power_consumption=pw, min_psu_wattage=mp, length=l, price=pr, reliability=r))  
  
    # PSU (4 шт)  
    psu_data = [('Corsair CV650',650,'Bronze',5500,4.5),('Corsair RM750e',750,'Gold',9500,4.8)]  
    for n,w,r,p,re in psu_data: db.session.add(PowerSupply(name=n, wattage=w, rating=r, price=p, reliability=re))  
  
    # Storage (2 шт)  
    storage_data = [('Samsung 980 Pro 1TB','SSD','M.2',1024,9500,4.9)]  
    for n,st,i,c,p,r in storage_data: db.session.add(Storage(name=n, storage_type=st, interface=i, capacity=c, price=p, reliability=r))  
  
    # Case (2 шт)  
    case_data = [('Corsair 4000D','ATX, mATX',360,170,2,9000,4.7)]  
    for n,f,mg,mc,fi,p,r in case_data: db.session.add(Case(name=n, form_factor=f, max_gpu_length=mg, max_cooler_height=mc, fans_included=fi, price=p, reliability=r))  
  
    db.session.commit()  
    print("OK: CPU", CPU.query.count(), "MB", Motherboard.query.count(), "RAM", RAM.query.count(), "GPU", VideoCard.query.count(), "PSU", PowerSupply.query.count(), "Storage", Storage.query.count(), "Case", Case.query.count()) 
