from database import engine
from models.model_hipizza import Item

from sqlmodel import Session
from sqlmodel import select

def allItems():
    with Session(engine) as session:
        statement = select(Item)
        
        results = session.exec(statement).all()
        return results
    
def createItem(item:Item):
    with Session(engine) as session:
        new_item = Item(id=None, 
                        name=item.name, 
                        price=item.price, 
                        description=item.description, 
                        image=item.image)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item

def findItem(itemID: int):
    with Session(engine) as session:
        statement = select(Item).where(Item.id == itemID)

        results = session.exec(statement).first()
        return results
    
def editItem(itemID, item:Item):
    with Session(engine) as session:
        statement = select(Item).where(Item.id == itemID)
        results = session.exec(statement).first()
        results.name = item.name
        results.price = item.price
        results.description = item.description
        results.image = item.image

        session.add(results)
        session.commit()
        session.refresh(results)
        return results

def deleteItem(itemID):
    with Session(engine) as session:
        statement = select(Item).where(Item.id == itemID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        return True