def addition(a: float,b:float) -> float:
    return a+b


def subtraction(a: float , b: float) -> float:
    return a-b




def multiplication(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float | str:
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return "division by zero not permissible"