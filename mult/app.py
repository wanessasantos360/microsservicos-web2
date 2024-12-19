from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mult(BaseModel):
 op1: float
 op2: float


@app.get("/mult")
def multiplicacao(op1: float, op2: float):
    resultado = op1 * op2
    return {"resultado": f"O resultado de {op1} x {op2} é: {resultado}"}

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)