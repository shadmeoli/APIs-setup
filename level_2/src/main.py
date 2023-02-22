from fastapi import FastAPI

from routes import route_1


app = FastAPI()

app.include(route_1.route)