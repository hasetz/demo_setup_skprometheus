from fastapi import FastAPI
import prometheus_client
from prometheus_client import Counter, Histogram
from fastapi import Response
from pydantic import BaseModel
import time
import random
import pickle
from scikitProm.utils import get_project_root


app = FastAPI()
model_path = get_project_root() / "models" / "decision_tree_0.1.pkl"
iris_model = pickle.load(open(model_path, 'rb'))

request_count = Counter('requests_index', 'Amount of requests for index page.')
request_latency = Histogram('Latency_hist', 'Histogram for tracking latency.')


@app.get('/')
def index():
    tic = time.time()
    request_count.inc()
    time.sleep(random.randint(0, 4))
    toc = time.time()
    request_latency.observe(toc-tic)
    return {
        "data": "Hello worlds",
        "time": toc - tic,
    }


class IrisInputModel(BaseModel):
    input: list


@app.post('/iris')
def iris(iris_input: IrisInputModel):
    time.sleep(random.randint(0, 4))
    print(type(iris_input.input))
    prediction = iris_model.predict([iris_input.input])
    return {
        "prediction": str(prediction[0])
    }


@app.get('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), media_type="text/plain")  #to normal text --geen json