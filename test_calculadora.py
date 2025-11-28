from src.calculadora import Calculadora


def test_suma():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5


def test_resta():
    calc = Calculadora()
    assert calc.restar(5, 3) == 2


def test_multiplicacion():
    calc = Calculadora()
    assert calc.multiplicar(4, 3) == 12


def test_division():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5


def test_division_por_cero():
    calc = Calculadora()
    assert calc.dividir(10, 0) == "Error: división por cero"
