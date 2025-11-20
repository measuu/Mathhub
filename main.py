from fastapi import FastAPI
from routers.auth import router as auth_router
from database import Base, engine
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers.calculator import router as calc_router
from routers import formulas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Авторизація"])
app.include_router(calc_router, prefix="/calculator", tags=["Калькулятор"])
app.include_router(formulas.router, prefix="/formulas", tags=["Формули фігур на площині і в об'ємі"])