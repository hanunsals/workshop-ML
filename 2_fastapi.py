from fastapi_first import FastAPI
import uvicorn
import joblib
from caruser_pydantic import CarUser

app = FastAPI()

model = joblib.load('trainedmodel_cars.joblib')

@app.get("/")
def root():
    return {'message':'This is Car predition API to give reccomendation car'}

@app.post("/predict")
def predict_car_type(data:CarUser):
    data = data.dict()
    age = data['age']
    gender = data['gender']
    
    predict = model.predict([[age,gender]])
    
    return {
        'prediction' :predict[0]
    }

if __name__ == "__main__" :
    uvicorn.run(app,host='127.0.0.1',port=8000)