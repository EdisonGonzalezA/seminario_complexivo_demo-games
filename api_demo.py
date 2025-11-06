from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = True
    description: Optional[str] = None
    tax: Optional[float] = None


app = FastAPI()


@app.get("/", description="Este es el endpoint principal. Devuelve el saludo de bienvenida")
def saludo():
    return {"message": "Hola Mundo! Esto es FastAPI"}


@app.post("/items/", description="Este endpoint crea un nuevo item. Recibe un Json con 'name' y 'price' y devuelve el item procesado con IVA")
def create_item(item: Item):
    precio_con_iva = item.price * 1.15
    return {
        "item_name_recibido": item.name,
        "precio_con_iva": precio_con_iva,
        "oferta_aplicada": item.is_offer
    }
