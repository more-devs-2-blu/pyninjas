from controller.item_controller import allItems, createItem, findItem, editItem, deleteItem
from fastapi import APIRouter, Response
from fastapi import status
from models.model_hipizza import Item

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Optional

router = APIRouter(
    prefix='/item',
    tags=['item']
)

# Busca Lista de Items
@router.get(
    '/',
    summary='Retorna uma lista de items',
    description='Retorna uma lista de items',
    response_description='Lista de Items Cadastrados',
    status_code=status.HTTP_200_OK
)
def all_items(response: Response):
    all_items = allItems()
    if all_items:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(all_items))
    else:
        response.status = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

@router.post(
    '/',
    summary='Cadastrar Novo Item',
    status_code=status.HTTP_200_OK
)

def create_item(item: Item, response: Response):
    newItem = createItem(item)
    if newItem:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(newItem))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    

@router.get(
    '/{id}',
    summary='Buscar um Item do Menu',
    status_code=status.HTTP_200_OK
)

def find_item(itemID: int, response: Response):
    finded_item = findItem(itemID)
    if finded_item:
        response.status_code=status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(finded_item))
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

@router.patch(
    '/{id}/',
    summary='Editar um Item do Menu',
    status_code=status.HTTP_200_OK        
)

def edit_item(itemID: int, item: Item, response: Response):
    edited_item = editItem(itemID, item)
    if edited_item:
        response.status_code=status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(edited_item))
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    
@router.delete(
    '/{id}',
    summary='Deleta um Item pelo ID',
    status_code=status.HTTP_200_OK
)

def delete_Item(itemID: int, response: Response):
    deletedItem = deleteItem(itemID)
    if deletedItem:
        response.status_code = status.HTTP_200_OK
        return {
            "Message": f"Item com ID {itemID} apagado com sucesso."
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
