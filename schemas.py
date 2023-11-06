from pydantic import BaseModel
from typing import Optional
from datetime import date

# Схемы для продуктов
class ProductBase(BaseModel):
    name: str  # Название продукта
    category: str  # Категория продукта
    price: float  # Цена продукта

class ProductCreate(ProductBase):
    production_date: date  # Дата производства продукта
    expiration_date: date  # Срок годности продукта

class Product(ProductBase):
    id: int  # Уникальный идентификатор продукта
    production_date: date
    expiration_date: date

    class Config:
        orm_mode = True  # Разрешает схеме работать с ORM объектами

# Схемы для условий хранения
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

# Схемы для секций склада
class WarehouseSectionBase(BaseModel):
    name: str  # Название секции
    capacity: int  # Вместимость секции

class WarehouseSectionCreate(WarehouseSectionBase):
    condition_id: int  # Внешний ключ на условия хранения

class WarehouseSection(WarehouseSectionBase):
    id: int  # Уникальный идентификатор секции
    condition_id: int

    class Config:
        orm_mode = True

# Схемы для инвентаря
class InventoryBase(BaseModel):
    quantity: int  # Количество товара
    stock_date: date  # Дата поступления на склад

class InventoryCreate(InventoryBase):
    product_id: int  # Внешний ключ на продукт

class Inventory(InventoryBase):
    id: int  # Уникальный идентификатор записи инвентаря
    product_id: int

    class Config:
        orm_mode = True

# Схемы для партий продуктов
class BatchBase(BaseModel):
    number: str  # Номер партии
    date: date  # Дата производства партии

class BatchCreate(BatchBase):
    product_id: int  # Внешний ключ на продукт

class Batch(BatchBase):
    id: int  # Уникальный идентификатор партии
    product_id: int

    class Config:
        orm_mode = True

# Схемы для QR-кодов
class QRCodeBase(BaseModel):
    data: str  # Данные QR-кода

class QRCodeCreate(QRCodeBase):
    batch_id: int  # Внешний ключ на партию

class QRCode(QRCodeBase):
    id: int  # Уникальный идентификатор QR-кода
    batch_id: int

    class Config:
        orm_mode = True
