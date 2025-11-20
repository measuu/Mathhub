from fastapi import APIRouter
import math

router = APIRouter()

# --- Площинні фігури ---
@router.get("/rectangle")
def rectangle(length: float, width: float):
    area = length * width
    perimeter = 2 * (length + width)
    return {
        "фігура": "Прямокутник",
        "формула_площі": "length * width",
        "формула_периметру": "2 * (length + width)",
        "параметри": {"length": length, "width": width},
        "площа": area,
        "периметр": perimeter
    }

@router.get("/circle")
def circle(radius: float):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return {
        "фігура": "Коло",
        "формула_площі": "π * r^2",
        "формула_периметру": "2 * π * r",
        "параметри": {"radius": radius},
        "площа": area,
        "периметр": circumference
    }

@router.get("/triangle")
def triangle(a: float, b: float, c: float):
    # формула Герона для площі
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return {
        "фігура": "Трикутник",
        "формула_площі": "√(s*(s-a)*(s-b)*(s-c)), де s=(a+b+c)/2",
        "формула_периметру": "a + b + c",
        "параметри": {"a": a, "b": b, "c": c},
        "площа": area,
        "периметр": perimeter
    }

@router.get("/right_triangle")
def right_triangle(a: float, b: float):
    # a і b — катети
    area = (a * b) / 2
    hypotenuse = math.sqrt(a**2 + b**2)
    perimeter = a + b + hypotenuse
    return {
        "фігура": "Прямокутний трикутник",
        "формула_площі": "(a*b)/2",
        "формула_периметру": "a + b + √(a^2 + b^2)",
        "параметри": {"a": a, "b": b},
        "площа": area,
        "периметр": perimeter
    }

@router.get("/parallelogram")
def parallelogram(base: float, height: float, side: float):
    area = base * height
    perimeter = 2 * (base + side)
    return {
        "фігура": "Паралелограм",
        "формула_площі": "base * height",
        "формула_периметру": "2 * (base + side)",
        "параметри": {"base": base, "height": height, "side": side},
        "площа": area,
        "периметр": perimeter
    }

@router.get("/rhombus")
def rhombus(diagonal1: float, diagonal2: float, side: float):
    area = (diagonal1 * diagonal2) / 2
    perimeter = 4 * side
    return {
        "фігура": "Ромб",
        "формула_площі": "(d1 * d2)/2",
        "формула_периметру": "4 * side",
        "параметри": {"diagonal1": diagonal1, "diagonal2": diagonal2, "side": side},
        "площа": area,
        "периметр": perimeter
    }

@router.get("/trapezoid")
def trapezoid(a: float, b: float, height: float, c: float, d: float):
    # a і b — основи, c і d — бокові сторони
    area = ((a + b) / 2) * height
    perimeter = a + b + c + d
    return {
        "фігура": "Трапеція",
        "формула_площі": "((a+b)/2)*h",
        "формула_периметру": "a + b + c + d",
        "параметри": {"a": a, "b": b, "c": c, "d": d, "height": height},
        "площа": area,
        "периметр": perimeter
    }

# --- Об'ємні фігури ---
@router.get("/cube")
def cube(side: float):
    volume = side**3
    surface_area = 6 * side**2
    return {
        "фігура": "Куб",
        "формула_об'єму": "side^3",
        "формула_площі_поверхні": "6 * side^2",
        "параметри": {"side": side},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }

@router.get("/sphere")
def sphere(radius: float):
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return {
        "фігура": "Сфера",
        "формула_об'єму": "(4/3) * π * r^3",
        "формула_площі_поверхні": "4 * π * r^2",
        "параметри": {"radius": radius},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }

@router.get("/pyramid")
def pyramid(base_area: float, height: float, base_perimeter: float):
    volume = (1/3) * base_area * height
    surface_area = base_area + (1/2) * base_perimeter * math.sqrt((height**2) + ((base_area/base_perimeter)**2))
    return {
        "фігура": "Піраміда",
        "формула_об'єму": "(1/3)*BaseArea*height",
        "формула_площі_поверхні": "BaseArea + 1/2*Perimeter*slant_height",
        "параметри": {"base_area": base_area, "height": height, "base_perimeter": base_perimeter},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }

@router.get("/prism")
def prism(base_area: float, height: float, base_perimeter: float):
    volume = base_area * height
    surface_area = 2 * base_area + base_perimeter * height
    return {
        "фігура": "Призма",
        "формула_об'єму": "BaseArea * height",
        "формула_площі_поверхні": "2*BaseArea + Perimeter*height",
        "параметри": {"base_area": base_area, "height": height, "base_perimeter": base_perimeter},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }

@router.get("/cylinder")
def cylinder(radius: float, height: float):
    volume = math.pi * radius**2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return {
        "фігура": "Циліндр",
        "формула_об'єму": "π * r^2 * h",
        "формула_площі_поверхні": "2 * π * r * (r+h)",
        "параметри": {"radius": radius, "height": height},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }

@router.get("/cone")
def cone(radius: float, height: float):
    slant_height = math.sqrt(radius**2 + height**2)
    volume = (1/3) * math.pi * radius**2 * height
    surface_area = math.pi * radius * (radius + slant_height)
    return {
        "фігура": "Конус",
        "формула_об'єму": "(1/3) * π * r^2 * h",
        "формула_площі_поверхні": "π * r * (r + l)",
        "параметри": {"radius": radius, "height": height},
        "об'єм": volume,
        "площа_поверхні": surface_area
    }