from pydantic import BaseModel
from typing import Optional
from datetime import date

# Схема для продукта
class ProductBase(BaseModel):
    name: str  # Название продукта
    category: str  # Категория продукта
    price: float  # Цена продукта

class ProductCreate(ProductBase):
    production_date: date  # Дата производства
    expiration_date: date  # Срок годности

class Product(ProductBase):
    id: int  # Уникальный идентификатор продукта
    production_date: date
    expiration_date: date

    class Config:
        orm_mode = True

# Схема для условий хранения
class StorageConditionBase(BaseModel):
    temperature: float  # Температура хранения
    humidity: float  # Влажность хранения
    special_requirements: Optional[str] = None  # Особые требования

class StorageConditionCreate(StorageConditionBase):
    pass

class StorageCondition(StorageConditionBase):
    id: int  # Уникальный идентификатор условий хранения

    class Config:
        orm_mode = True

# Схема для секции склада
class WarehouseSectionBase(BaseModel):
    section_name: str  # Название секции
    capacity: int  # Вместимость секции

class WarehouseSectionCreate(WarehouseSectionBase):
    condition_id: int  # ID условий хранения

class WarehouseSection(WarehouseSectionBase):
    id: int  # Уникальный идентификатор секции
    condition_id: int

    class Config:
        orm_mode = True

# Схема для инвентаря
class InventoryBase(BaseModel):
    quantity: int  # Количество товара на складе
    stock_date: date  # Дата поступления на склад

class InventoryCreate(InventoryBase):
    product_id: int  # ID продукта

class Inventory(InventoryBase):
    id: int  # Уникальный идентификатор инвентаря
    product_id: int

    class Config:
        orm_mode = True

# Схема для партии продуктов
class BatchBase(BaseModel):
    batch_number: str  # Номер партии
    batch_date: date  # Дата производства партии

class BatchCreate(BatchBase):
    product_id: int  # ID продукта

class Batch(BatchBase):
    id: int  # Уникальный идентификатор партии
    product_id: int

    class Config:
        orm_mode = True

# Схема для QR-кода
class QRCodeBase(BaseModel):
    qr_data: str  # Данные QR-кода

class QRCodeCreate(QRCodeBase):
    batch_id: int  # ID партии

class QRCode(QRCodeBase):
    id: int  # Уникальный идентификатор QR-кода
    batch_id: int

    class Config:
        orm_mode = True
