from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float)
    production_date = Column(Date)
    expiration_date = Column(Date)
    inventory = relationship("Inventory", back_populates="product")
    batches = relationship("Batch", back_populates="product")

class StorageCondition(Base):
    __tablename__ = "storage_conditions"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    special_requirements = Column(Text)
    warehouse_sections = relationship("WarehouseSection", back_populates="storage_condition")

class WarehouseSection(Base):
    __tablename__ = "warehouse_sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    capacity = Column(Integer)
    condition_id = Column(Integer, ForeignKey("storage_conditions.id"))
    storage_condition = relationship("StorageCondition", back_populates="warehouse_sections")

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    stock_date = Column(Date)
    product = relationship("Product", back_populates="inventory")

class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    number = Column(String, index=True)
    date = Column(Date)
    product = relationship("Product", back_populates="batches")
    qr_code = relationship("QRCode", back_populates="batch", uselist=False)

class QRCode(Base):
    __tablename__ = "qr_codes"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Text)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    batch = relationship("Batch", back_populates="qr_code")
