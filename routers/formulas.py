import math

from fastapi import APIRouter

router = APIRouter()


formulas_info = {
    "трикутник": {
        "площа": "S = (a * h) / 2, де a – основа, h – висота",
        "периметр": "P = a + b + c, де a, b, c – сторони трикутника",
    },
    "прямокутний_трикутник": {
        "площа": "S = (a * b) / 2, де a і b – катети",
        "периметр": "P = a + b + √(a^2 + b^2), де a і b – катети, гіпотенуза c = √(a^2 + b^2)",
    },
    "паралелограм": {
        "площа": "S = a * h, де a – основа, h – висота",
        "периметр": "P = 2 * (a + b), де a і b – сторони паралелограма",
    },
    "ромб": {
        "площа": "S = (d1 * d2) / 2, де d1 і d2 – діагоналі",
        "периметр": "P = 4 * a, де a – сторона ромба",
    },
    "трапеція": {
        "площа": "S = ((a + b) / 2) * h, де a і b – основи, h – висота",
        "периметр": "P = a + b + c + d, де a, b – основи, c, d – бічні сторони",
    },
    "піраміда": {
        "площа_бокова": "S_b = (P_base * l) / 2, де P_base – периметр основи, l – апофема",
        "площа_повна": "S = S_base + S_b",
        "об'єм": "V = (1/3) * S_base * h",
    },
    "призма": {
        "площа_бокова": "S_b = P_base * h, де P_base – периметр основи, h – висота",
        "площа_повна": "S = 2 * S_base + S_b",
        "об'єм": "V = S_base * h",
    },
    "циліндр": {
        "площа_бокова": "S_b = 2 * π * r * h",
        "площа_повна": "S = 2 * π * r * (r + h)",
        "об'єм": "V = π * r^2 * h",
    },
    "конус": {
        "площа_бокова": "S_b = π * r * l, де l – твірна конуса",
        "площа_повна": "S = π * r * (r + l)",
        "об'єм": "V = (1/3) * π * r^2 * h",
    },
}


@router.get("/formulas_info/{figure_name}")
def get_formulas_info(figure_name: str):
    info = formulas_info.get(figure_name.lower())
    if not info:
        return {"помилка": f"Фігура '{figure_name}' не знайдена. Спробуйте іншу."}
    return info


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
        "периметр": perimeter,
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
        "периметр": circumference,
    }


@router.get("/triangle")
def triangle(a: float, b: float, c: float):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return {
        "фігура": "Трикутник",
        "формула_площі": "√(s*(s-a)*(s-b)*(s-c)), де s=(a+b+c)/2",
        "формула_периметру": "a + b + c",
        "параметри": {"a": a, "b": b, "c": c},
        "площа": area,
        "периметр": perimeter,
    }


@router.get("/right_triangle")
def right_triangle(a: float, b: float):
    area = (a * b) / 2
    hypotenuse = math.sqrt(a**2 + b**2)
    perimeter = a + b + hypotenuse
    return {
        "фігура": "Прямокутний трикутник",
        "формула_площі": "(a*b)/2",
        "формула_периметру": "a + b + √(a^2 + b^2)",
        "параметри": {"a": a, "b": b},
        "площа": area,
        "периметр": perimeter,
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
        "периметр": perimeter,
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
        "периметр": perimeter,
    }


@router.get("/trapezoid")
def trapezoid(a: float, b: float, height: float, c: float, d: float):
    area = ((a + b) / 2) * height
    perimeter = a + b + c + d
    return {
        "фігура": "Трапеція",
        "формула_площі": "((a+b)/2)*h",
        "формула_периметру": "a + b + c + d",
        "параметри": {"a": a, "b": b, "c": c, "d": d, "height": height},
        "площа": area,
        "периметр": perimeter,
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
        "площа_поверхні": surface_area,
    }


@router.get("/sphere")
def sphere(radius: float):
    volume = 4 / 3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return {
        "фігура": "Сфера",
        "формула_об'єму": "(4/3) * π * r^3",
        "формула_площі_поверхні": "4 * π * r^2",
        "параметри": {"radius": radius},
        "об'єм": volume,
        "площа_поверхні": surface_area,
    }


@router.get("/pyramid")
def pyramid(base_area: float, height: float, base_perimeter: float):
    volume = (1 / 3) * base_area * height
    surface_area = base_area + (1 / 2) * base_perimeter * math.sqrt(
        (height**2) + ((base_area / base_perimeter) ** 2)
    )
    return {
        "фігура": "Піраміда",
        "формула_об'єму": "(1/3)*BaseArea*height",
        "формула_площі_поверхні": "BaseArea + 1/2*Perimeter*slant_height",
        "параметри": {
            "base_area": base_area,
            "height": height,
            "base_perimeter": base_perimeter,
        },
        "об'єм": volume,
        "площа_поверхні": surface_area,
    }


@router.get("/prism")
def prism(base_area: float, height: float, base_perimeter: float):
    volume = base_area * height
    surface_area = 2 * base_area + base_perimeter * height
    return {
        "фігура": "Призма",
        "формула_об'єму": "BaseArea * height",
        "формула_площі_поверхні": "2*BaseArea + Perimeter*height",
        "параметри": {
            "base_area": base_area,
            "height": height,
            "base_perimeter": base_perimeter,
        },
        "об'єм": volume,
        "площа_поверхні": surface_area,
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
        "площа_поверхні": surface_area,
    }


@router.get("/cone")
def cone(radius: float, height: float):
    slant_height = math.sqrt(radius**2 + height**2)
    volume = (1 / 3) * math.pi * radius**2 * height
    surface_area = math.pi * radius * (radius + slant_height)
    return {
        "фігура": "Конус",
        "формула_об'єму": "(1/3) * π * r^2 * h",
        "формула_площі_поверхні": "π * r * (r + l)",
        "параметри": {"radius": radius, "height": height},
        "об'єм": volume,
        "площа_поверхні": surface_area,
    }
