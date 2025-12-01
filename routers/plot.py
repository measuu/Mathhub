import io
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.get("/plot")
def plot_function(function: str):
    try:
        x = sp.symbols("x")

        expr = sp.sympify(function)

        f = sp.lambdify(x, expr, "numpy")

        xs = np.linspace(-10, 10, 400)

        ys = f(xs)

        plt.figure(figsize=(6, 4))
        plt.plot(xs, ys)
        plt.grid(True)
        plt.title(f"Графік: y = {function}")

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close()

        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Помилка у функції: {str(e)}")


@router.get("/plot3d", summary="Налаштовуваний 3D-графік")
def plot_3d(
    formula: str = Query(
        "np.sin(np.sqrt(x**2 + y**2))", description="Функція від x та y"
    ),
    min_val: float = Query(-4),
    max_val: float = Query(4),
    step: float = Query(0.1),
    cmap: str = Query("viridis"),
):
    try:
        x = np.arange(min_val, max_val, step)
        y = np.arange(min_val, max_val, step)
        X, Y = np.meshgrid(x, y)
    except Exception:
        raise HTTPException(status_code=400, detail="Невірні параметри сітки")

    try:
        allowed = {
            "np": np,
            "math": math,
            "x": X,
            "y": Y,
        }
        Z = eval(formula, {"__builtins__": {}}, allowed)
    except Exception:
        raise HTTPException(status_code=400, detail="Помилка у формулі функції")

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor="none")
    ax.set_title(f"3D surface: z = {formula}")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close(fig)

    return StreamingResponse(buf, media_type="image/png")
