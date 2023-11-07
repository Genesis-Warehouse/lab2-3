from sqlalchemy.orm import Session
import models, schemas

# CRUD для продуктов
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        update_data = product.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# CRUD для условий хранения
def get_storage_condition(db: Session, condition_id: int):
    return db.query(models.StorageCondition).filter(models.StorageCondition.id == condition_id).first()

def create_storage_condition(db: Session, storage_condition: schemas.StorageConditionCreate):
    db_storage_condition = models.StorageCondition(**storage_condition.model_dump())
    db.add(db_storage_condition)
    db.commit()
    db.refresh(db_storage_condition)
    return db_storage_condition

def update_storage_condition(db: Session, condition_id: int, storage_condition: schemas.StorageConditionCreate):
    db_condition = db.query(models.StorageCondition).filter(models.StorageCondition.id == condition_id).first()
    if db_condition:
        update_data = storage_condition.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_condition, key, value)
        db.commit()
        db.refresh(db_condition)
    return db_condition

def delete_storage_condition(db: Session, condition_id: int):
    db_condition = db.query(models.StorageCondition).filter(models.StorageCondition.id == condition_id).first()
    if db_condition:
        db.delete(db_condition)
        db.commit()
    return db_condition

# CRUD для секций склада
def get_warehouse_section(db: Session, section_id: int):
    return db.query(models.WarehouseSection).filter(models.WarehouseSection.id == section_id).first()

def create_warehouse_section(db: Session, warehouse_section: schemas.WarehouseSectionCreate):
    db_section = models.WarehouseSection(**warehouse_section.model_dump())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def update_warehouse_section(db: Session, section_id: int, warehouse_section: schemas.WarehouseSectionCreate):
    db_section = db.query(models.WarehouseSection).filter(models.WarehouseSection.id == section_id).first()
    if db_section:
        update_data = warehouse_section.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_section, key, value)
        db.commit()
        db.refresh(db_section)
    return db_section

def delete_warehouse_section(db: Session, section_id: int):
    db_section = db.query(models.WarehouseSection).filter(models.WarehouseSection.id == section_id).first()
    if db_section:
        db.delete(db_section)
        db.commit()
    return db_section

# CRUD для инвентаря
def get_inventory(db: Session, inventory_id: int):
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(**inventory.model_dump())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def update_inventory(db: Session, inventory_id: int, inventory: schemas.InventoryCreate):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        update_data = inventory.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_inventory, key, value)
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, inventory_id: int):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
    return db_inventory

# CRUD для партий продуктов
def get_batch(db: Session, batch_id: int):
    return db.query(models.Batch).filter(models.Batch.id == batch_id).first()

def create_batch(db: Session, batch: schemas.BatchCreate):
    db_batch = models.Batch(**batch.model_dump())
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch

def update_batch(db: Session, batch_id: int, batch: schemas.BatchCreate):
    db_batch = db.query(models.Batch).filter(models.Batch.id == batch_id).first()
    if db_batch:
        update_data = batch.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_batch, key, value)
        db.commit()
        db.refresh(db_batch)
    return db_batch

def delete_batch(db: Session, batch_id: int):
    db_batch = db.query(models.Batch).filter(models.Batch.id == batch_id).first()
    if db_batch:
        db.delete(db_batch)
        db.commit()
    return db_batch

# CRUD для QR-кодов
def get_qr_code(db: Session, qr_id: int):
    return db.query(models.QRCode).filter(models.QRCode.id == qr_id).first()

def create_qr_code(db: Session, qr_code: schemas.QRCodeCreate):
    db_qr_code = models.QRCode(**qr_code.model_dump())
    db.add(db_qr_code)
    db.commit()
    db.refresh(db_qr_code)
    return db_qr_code

def update_qr_code(db: Session, qr_id: int, qr_code: schemas.QRCodeCreate):
    db_qr_code = db.query(models.QRCode).filter(models.QRCode.id == qr_id).first()
    if db_qr_code:
        update_data = qr_code.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_qr_code, key, value)
        db.commit()
        db.refresh(db_qr_code)
    return db_qr_code

def delete_qr_code(db: Session, qr_id: int):
    db_qr_code = db.query(models.QRCode).filter(models.QRCode.id == qr_id).first()
    if db_qr_code:
        db.delete(db_qr_code)
        db.commit()
    return db_qr_code
