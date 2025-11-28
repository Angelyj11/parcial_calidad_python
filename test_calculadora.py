import pytest
from src.calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5

def test_restar():
    calc = Calculadora()
    assert calc.restar(5, 2) == 3

def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 4) == 12

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5

def test_dividir_por_cero():
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.dividir(10, 0)
