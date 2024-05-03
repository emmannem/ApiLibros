from fastapi import FastAPI
# Validación de datos
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    # Dato opcional
    editorial: Optional[str]

# creamos 1ra ruta


@app.get("/")
def index():
    return {"message": "Hola Mundo"}


@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}


@app.post("/libros")
def insertar_libros(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}
