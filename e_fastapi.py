from fastapi import FastAPI
from pydantic import BaseModel
from e_calculator import calculate

class User_input(BaseModel):
	operation : str                                                            
	x : int                                                
	y : int

app = FastAPI()

@app.get("/")
def root():
    return {'message':'This is Calculator API'}

@app.post("/calculate")
def operate(input:User_input):
	result = calculate(input.operation, input.x, input.y)
	return result