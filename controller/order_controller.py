from database import engine
from models.model_hipizza import Order, Item, Order_Item, User

from sqlmodel import Session
from sqlmodel import select

from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import selectinload


def allOrders():
    teste = []
    with Session(engine) as session:
        statement = select(Order).options(selectinload(Order.order_items))

        results = session.exec(statement).all()
        # print(results)
        print(results[0].order_items)
        resultsJSON = (jsonable_encoder(results))
        print(resultsJSON)
        for order in resultsJSON:
            statement_user = select(User).where(User.id == order["user_id"])
            result_user = session.exec(statement_user).first()
            
            order["user"] = jsonable_encoder(result_user)
            order["order_details"] = findOrder(order["id"])
            print("Order\n", order)

        return resultsJSON

def createOrder(userID, itemID, order: Order, quantity: int):
    with Session(engine) as session:
        item = session.get(Item, itemID)
        total_price = item.price * quantity + order.shipping_value
        statement_user = select(User).where(User.id == userID)
        
        user_ordering = session.exec(statement_user).first()
        new_order = Order(id=None, 
                        status=order.status,
                        shipping_value=order.shipping_value,
                        payment_method=order.payment_method,
                        order_date=datetime.now(),
                        total_price=total_price,
                        user_id=userID,
                        user=user_ordering,
                        item_id=itemID)
        
        session.add(new_order)
        session.commit()
        session.refresh(new_order)

        order_item = Order_Item(id=None,            
                                quantity=quantity,
                                price=item.price,                                                        
                                item_id=itemID,
                                order_id=new_order.id)
        
        session.add(order_item)
        session.commit()

        return new_order
    
def findOrder(orderID: int = None):
    with Session(engine) as session:
        statement = select(Order).where(Order.id == orderID).options(selectinload(Order.order_items))

        results = session.exec(statement).first()
        print(results)
        return results
    
def editOrder(orderID: int, order:Order, quantity: int):
    with Session(engine) as session:
        statement = select(Order).where(Order.id == orderID)
        results = session.exec(statement).first()

        results.status = order.status
        results.shipping_value = order.shipping_value
        results.payment_method = order.payment_method
        results.user_id = order.user_id
        results.item_id = order.item_id

        # Calcula o novo valor total baseado no preço e quantidade
        item = session.get(Item, results.item_id)
        results.total_price = item.price * quantity + order.shipping_value

        order_item = session.query(Order_Item).filter_by(order_id=orderID).first()

        order_item.quantity = quantity
        order_item.price = item.price
        order_item.item_id = order.item_id

        session.add(results)
        session.commit()
        session.refresh(results)
        return results


def deleteOrder(orderID):
    with Session(engine) as session:
        statement = select(Order, Order_Item).join(Order_Item).where(Order.id == orderID)
        results = session.exec(statement).all()

        for order, order_item in results:
            session.delete(order)
            session.delete(order_item)

        session.commit()
        return True
    

