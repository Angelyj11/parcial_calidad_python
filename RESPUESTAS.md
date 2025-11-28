# RESPUESTAS – Parcial de Calidad de Software

## ¿Cómo identificar fallos en el linter?
Cuando flake8 detecta errores, los muestra como:
archivo.py:línea:columna: descripción

## ¿Cómo identificar fallos en pruebas?
Pytest muestra:
FAILED test_xxx.py::test_algo

## ¿Cómo identificar fallos de cobertura?
Pytest-cov muestra:
Coverage failure due to less than 80%

## Diferencia entre un run fallido y uno exitoso
- El run fallido se detiene en la etapa donde ocurrió el error (linter, pruebas o cobertura).
- El run exitoso ejecuta todas las etapas y termina con un check verde.
