from typing import Optional, List, Type
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    email: str = Field(index=True)
    phone: int = Field(index=True)
    whatsapp: Optional[bool] = Field(index=True)
    password: str = Field(index=True)
    address: str = Field(index=True)
    

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False, index=True)
    price: float = Field(nullable=False, index=True)
    description: str = Field()
    image: Optional[str] = Field(default='image.jpg')
    

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    status: str = Field(default="Em Preparação", index=True)
    shipping_value: float = Field(index=True)
    payment_method: str = Field(index=True)
    order_date: Optional[datetime] = Field(index=True)
    total_price: Optional[float] = Field(index=True)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")

    order_items: List["Order_Item"] = Relationship(back_populates="order")

    def calculate_total_price(self, items: List[Item]):
        total = self.shipping_value or 0.0
        for item in items:
            for order_item in self.order_items:
                if order_item.item.id == item.id:
                    total += order_item.quantity * item.price
        self.total_price = total


class Order_Item(SQLModel, table=True):
    __tablename__ = "order_item"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    quantity: int = Field(index=True)
    price: float = Field(index=True)

    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")

    order: Optional[Order] = Relationship(back_populates="order_items")




