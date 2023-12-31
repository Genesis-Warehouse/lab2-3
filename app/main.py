from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:8080", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)


# Dependency для создания сессии с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Эндпоинт для создания продукта
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.create_product(db=db, product=product)
    return db_product


@app.get("/products/all")
def read_product_all(db: Session = Depends(get_db)):
    db_products = crud.get_product_all(db)
    return db_products


# Эндпоинт для получения продукта по ID
@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# Эндпоинт для обновления продукта
@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# Эндпоинт для удаления продукта
@app.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.post("/storage_conditions/", response_model=schemas.StorageCondition)
def create_storage_condition(condition: schemas.StorageConditionCreate, db: Session = Depends(get_db)):
    return crud.create_storage_condition(db=db, storage_condition=condition)


@app.get("/storage_conditions/all")
def read_storage_conditions_all(db: Session = Depends(get_db)):
    db_condition = crud.get_storage_condition_all(db)
    return db_condition


@app.get("/storage_conditions/{condition_id}", response_model=schemas.StorageCondition)
def read_storage_condition(condition_id: int, db: Session = Depends(get_db)):
    condition = crud.get_storage_condition(db, condition_id=condition_id)
    if condition is None:
        raise HTTPException(
            status_code=404, detail="Storage condition not found")
    return condition


@app.put("/storage_conditions/{condition_id}", response_model=schemas.StorageCondition)
def update_storage_condition(condition_id: int, condition: schemas.StorageConditionCreate, db: Session = Depends(get_db)):
    return crud.update_storage_condition(db, condition_id, condition)


@app.delete("/storage_conditions/{condition_id}", response_model=schemas.StorageCondition)
def delete_storage_condition(condition_id: int, db: Session = Depends(get_db)):
    return crud.delete_storage_condition(db, condition_id)


@app.post("/warehouse_sections/", response_model=schemas.WarehouseSection)
def create_warehouse_section(section: schemas.WarehouseSectionCreate, db: Session = Depends(get_db)):
    return crud.create_warehouse_section(db=db, warehouse_section=section)


@app.get("/warehouse_sections/all")
def read_warehouse_section_all(db: Session = Depends(get_db)):
    db_section = crud.get_warehouse_section_all(db)
    return db_section


@app.get("/warehouse_sections/{section_id}", response_model=schemas.WarehouseSection)
def read_warehouse_section(section_id: int, db: Session = Depends(get_db)):
    section = crud.get_warehouse_section(db, section_id=section_id)
    if section is None:
        raise HTTPException(
            status_code=404, detail="Warehouse section not found")
    return section


@app.put("/warehouse_sections/{section_id}", response_model=schemas.WarehouseSection)
def update_warehouse_section(section_id: int, section: schemas.WarehouseSectionCreate, db: Session = Depends(get_db)):
    return crud.update_warehouse_section(db, section_id, section)


@app.delete("/warehouse_sections/{section_id}", response_model=schemas.WarehouseSection)
def delete_warehouse_section(section_id: int, db: Session = Depends(get_db)):
    return crud.delete_warehouse_section(db, section_id)


@app.post("/inventory/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)


@app.get("/inventory/all")
def read_inventory_all(db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory_all(db)
    return db_inventory


@app.get("/inventory/{inventory_id}", response_model=schemas.Inventory)
def read_inventory_item(inventory_id: int, db: Session = Depends(get_db)):
    inventory_item = crud.get_inventory(db, inventory_id=inventory_id)
    if inventory_item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return inventory_item


@app.put("/inventory/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.update_inventory(db, inventory_id, inventory)


@app.delete("/inventory/{inventory_id}", response_model=schemas.Inventory)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    return crud.delete_inventory(db, inventory_id)


@app.post("/batches/", response_model=schemas.Batch)
def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    return crud.create_batch(db=db, batch=batch)


@app.get("/batches/all")
def read_batches_all(db: Session = Depends(get_db)):
    db_batches = crud.get_batch_all(db)
    return db_batches


@app.get("/batches/{batch_id}", response_model=schemas.Batch)
def read_batch(batch_id: int, db: Session = Depends(get_db)):
    batch = crud.get_batch(db, batch_id=batch_id)
    if batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch


@app.put("/batches/{batch_id}", response_model=schemas.Batch)
def update_batch(batch_id: int, batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    return crud.update_batch(db, batch_id, batch)


@app.delete("/batches/{batch_id}", response_model=schemas.Batch)
def delete_batch(batch_id: int, db: Session = Depends(get_db)):
    return crud.delete_batch(db, batch_id)


@app.post("/qrcodes/", response_model=schemas.QRCode)
def create_qr_code(qrcode: schemas.QRCodeCreate, db: Session = Depends(get_db)):
    return crud.create_qr_code(db, qrcode)


@app.get("/qrcodes/all")
def read_qr_code_all(db: Session = Depends(get_db)):
    db_qrcodes = crud.get_qr_code_all(db)
    return db_qrcodes


@app.get("/qrcodes/{qrcode_id}", response_model=schemas.QRCode)
def read_qr_code(qrcode_id: int, db: Session = Depends(get_db)):
    qrcode = crud.get_qr_code(db, qrcode_id)
    if qrcode is None:
        raise HTTPException(status_code=404, detail="QRCode not found")
    return qrcode


@app.put("/qrcodes/{qrcode_id}", response_model=schemas.QRCode)
def update_qr_code(qrcode_id: int, qrcode: schemas.QRCodeCreate, db: Session = Depends(get_db)):
    return crud.update_qr_code(db, qrcode_id, qrcode)


@app.delete("/qrcodes/{qrcode_id}", response_model=schemas.QRCode)
def delete_qr_code(qrcode_id: int, db: Session = Depends(get_db)):
    return crud.delete_qr_code(db, qrcode_id)
