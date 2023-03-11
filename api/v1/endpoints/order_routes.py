from controller.order_controller import allOrders, createOrder, findOrder, editOrder, deleteOrder
from fastapi import APIRouter, Response
from fastapi import status
from models.model_hipizza import Order

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Optional

router = APIRouter(
    prefix='/order',
    tags=['order']
)

# Busca Lista de Orders
@router.get(
    '/',
    summary='Retorna uma lista de pedidos',
    description='Retorna uma lista de pedidos',
    response_description='Lista de Pedidos Cadastrados',
    status_code=status.HTTP_200_OK
)

def all_orders(response: Response):
    all_orders = allOrders()
    if all_orders:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(all_orders))
    else:
        response.status = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    
@router.post(
    '/',
    summary='Cadastrar um Novo Pedido',
    status_code=status.HTTP_200_OK
)

def create_order(userID: int, itemID: int, quantity: int, order: Order, response: Response):
    created_order = createOrder(userID, itemID, order, quantity)
    if created_order:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(created_order))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    
@router.get(
    '/{id}',
    summary='Busca um Pedido pelo ID',
    status_code=status.HTTP_200_OK
)

def find_order(orderID: int, response: Response):
    finded_order = findOrder(orderID)
    if finded_order:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(finded_order))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

@router.patch(
    '/{id}',
    summary='Editar um Pedido pelo ID',
    status_code=status.HTTP_200_OK
)

def edit_order(orderID: int, order: Order, quantity: int, response: Response):
    edited_order = editOrder(orderID, order, quantity)
    if edited_order:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(edited_order))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    
@router.delete(
    '/{id}',
    summary='Deleta um Pedido pelo ID',
    status_code=status.HTTP_200_OK
)

def delete_order(orderID: int, response: Response):
    delete_order = deleteOrder(orderID)
    if delete_order:
        response.status_code = status.HTTP_200_OK
        return {
            "Message": f"Pedido com ID {orderID} apagado com sucesso."
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    

