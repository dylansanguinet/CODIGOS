from fastapi import FastAPI

app = FastAPI(title="API de Tareas")

tareas = []

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/tareas")
def obtener_tareas():
    return tareas

@app.post("/tareas")
def crear_tarea(tarea: dict):
    tareas.append(tarea)
    return {"mensaje": "Tarea creada", "tarea": tarea}
