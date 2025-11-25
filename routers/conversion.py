from fastapi import APIRouter, Query, HTTPException

router = APIRouter()

length_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mile": 1609.34
}

weight_units = {
    "g": 1,
    "kg": 1000,
    "t": 1_000_000
}

speed_units = {
    "m/s": 1,
    "km/h": 1/3.6,
    "mph": 0.44704
}

time_units = {
    "s": 1,
    "min": 60,
    "h": 3600,
    "day": 86400
}

temperature_units = ["C", "F", "K"]


@router.get("/convert")
def convert_units(
    value: float = Query(..., description="Число для конвертації"),
    from_unit: str = Query(..., description="Одиниця джерела"),
    to_unit: str = Query(..., description="Одиниця призначення")
):
    def convert_dict(value, from_u, to_u, units_dict):
        return value * units_dict[from_u] / units_dict[to_u]

    if from_unit in length_units and to_unit in length_units:
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": convert_dict(value, from_unit, to_unit, length_units),
            "converted_unit": to_unit
        }

    if from_unit in weight_units and to_unit in weight_units:
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": convert_dict(value, from_unit, to_unit, weight_units),
            "converted_unit": to_unit
        }

    if from_unit in speed_units and to_unit in speed_units:
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": convert_dict(value, from_unit, to_unit, speed_units),
            "converted_unit": to_unit
        }

    if from_unit in time_units and to_unit in time_units:
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": convert_dict(value, from_unit, to_unit, time_units),
            "converted_unit": to_unit
        }

    if from_unit in temperature_units and to_unit in temperature_units:
        if from_unit == "C":
            if to_unit == "F":
                converted = value * 9/5 + 32
            elif to_unit == "K":
                converted = value + 273.15
            else:
                converted = value
        elif from_unit == "F":
            if to_unit == "C":
                converted = (value - 32) * 5/9
            elif to_unit == "K":
                converted = (value - 32) * 5/9 + 273.15
            else:
                converted = value
        elif from_unit == "K":
            if to_unit == "C":
                converted = value - 273.15
            elif to_unit == "F":
                converted = (value - 273.15) * 9/5 + 32
            else:
                converted = value
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": converted,
            "converted_unit": to_unit
        }

    raise HTTPException(status_code=400, detail="Непідтримувані одиниці для конвертації")