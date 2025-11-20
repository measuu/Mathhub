from fastapi import APIRouter
from math import factorial, isqrt, cbrt, pi, e, pow
import math

router = APIRouter()

@router.get("/add")
def add(a: float, b: float):
    return {
        "операція": "додавання",
        "перший_операнд": a,
        "другий_операнд": b,
        "результат": a + b
    }


@router.get("/subtract")
def subtract(a: float, b: float):
    return {
        "операція": "віднімання",
        "перший_операнд": a,
        "другий_операнд": b,
        "результат": a - b
    }


@router.get("/multiply")
def multiply(a: float, b: float):
    return {
        "операція": "множення",
        "перший_операнд": a,
        "другий_операнд": b,
        "результат": a * b
    }


@router.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"помилка":"Ділити на нуль не можна!"}
    return {
        "операція": "ділення",
        "перший_операнд": a,
        "другий_операнд": b,
        "результат": a / b
    }

@router.get("/factorial")
def factorial(a: float):
    return {
        "операція": "факторіал",
        "операнд": a,
        "результат": factorial(a)
    }

@router.get("/square_root")
def square_root(a: float):
    if a < 0:
        return {"помилка":"Квадратний корінь з від'ємного числа!"}
    return {
        "операція": "квадратний корінь",
        "операнд": a,
        "результат": isqrt(a)
    }

@router.get("/cube_root")
def cube_root(a: float):
    if a < 0:
        return {"помилка":"Кубічний корінь з від'ємного числа!"}
    return {
        "операція": "кубічний корінь",
        "операнд": a,
        "результат": cbrt(a)
    }

@router.get("/extent")
def extent(a: float, b: float):
    return {
        "операція": "Зведення числа a в степені b",
        "перший_операнд": a,
        "другий_операнд": b,
        "результат": a ** b
    }

@router.get("/log")
def log(a: float, base: float = 10):
    if a <= 0 or base <= 0:
        return {"помилка": "Логарифм визначений тільки для додатних чисел!"}
    return {"операція": f"логарифм числа {a} за основою {base}",
            "результат": math.log(a, base)}

@router.get("/sin")
def sin(a: float):
    return {"операція": "синус", "результат": math.sin(a)}

@router.get("/cos")
def cos(a: float):
    return {"операція": "косинус", "результат": math.cos(a)}

@router.get("/tan")
def tan(a: float):
    return {"операція": "тангенс", "результат": math.tan(a)}

@router.get("/const")
def const():
    return {"Повернення числа π": pi,
            "Повернення числа e": e,
            "Золотий_перетин_φ": (1 + 5 ** 0.5)/2}


from math import pow


@router.get("/root_n")
def root_n(a: float, n: float):
    if n == 0:
        return {"помилка": "Неможливо взяти корінь нульового степеня!"}
    if a < 0 and n % 2 == 0:
        return {"помилка": "Неможливо взяти парний корінь з від’ємного числа!"}

    result = pow(a, 1 / n)
    return {
        "операція": f"{n}-й корінь",
        "операнд": a,
        "ступінь": n,
        "результат": result
    }