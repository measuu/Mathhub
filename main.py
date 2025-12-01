from fastapi import FastAPI
from routers.auth import router as auth_router
from database import Base, engine
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers.calculator import router as calc_router
from routers import formulas
from routers.games import router as games_router
from routers.conversion import router as conv_router
from routers.math_facts import router as facts_router
from routers.memes import router as mem_router
from routers.feedback import router as feedback_router
from routers.plot import router as plot_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Авторизація"])
app.include_router(calc_router, prefix="/calculator", tags=["Калькулятор"])
app.include_router(conv_router, prefix="/conversation", tags=["Перетворення одиниць"])
app.include_router(plot_router, prefix="/func", tags=["Графіки"])
app.include_router(formulas.router, prefix="/formulas", tags=["Формули фігур на площині і в об'ємі"])
app.include_router(facts_router, prefix="/facts", tags=["Рандомні математичні факти"])
app.include_router(mem_router, prefix="/memes", tags=["Математичні меми"])
app.include_router(games_router, prefix="/games", tags=["Міні-ігри"])
app.include_router(feedback_router, prefix="/feedback", tags=["Відгуки"])