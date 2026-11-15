from fastapi import FastAPI,HTTPException
from calculator import addition,subtraction,division,multiplication


app=FastAPI(title="Calculator App")

@app.get("/")
def root():
    return {"message": "app is running"}

@app.get("/add")
def add(a:float , b: float) -> dict:
    return {"result":addition(a,b)}

@app.get("/sub")
def sub(a:float, b: float) -> dict:
    return {"result" : subtraction(a,b)}

@app.get("/mul")
def mul(a:float ,b: float) -> dict:
    return {"result" : multiplication(a,b)}


@app.get("/div")
def div(a:float,b:float) -> dict:
    return {"result": f"{division(a,b):.2f}"}


