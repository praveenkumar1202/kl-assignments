from fastapi import FastAPI

app = FastAPI()


@app.post("/addition/")
async def addition(num1: float, num2: float):
    result = num1 + num2
    return {"Addition of 2 numbers :", result}


@app.post("/subtraction/")
async def subtract(num1: float, num2: float):
    result = num1 - num2
    return {"subtraction of 2 numbers :", result}


@app.post("/multiplication/")
async def multiple(num1: float, num2: float):
    result = num1 * num2
    return {"multiplication of 2 numbers :", result}


@app.post("/division/")
async def divide(num1: float, num2: float):
    result = num1 / num2
    return {"division of 2 numbers :", result}
