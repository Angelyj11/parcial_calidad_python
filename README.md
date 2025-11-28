# Proyecto de Calidad – CI/CD con GitHub Actions

Este proyecto implementa una calculadora simple en Python y un pipeline de CI con:

- Linter: flake8
- Pruebas unitarias: pytest
- Cobertura: pytest-cov (mínimo 80%)
- Ejecución automática con GitHub Actions

## Ejecutar localmente
py -m pip install -r requirements.txt
py -m pytest --cov=src

## Ejecutar workflow localmente con act
Requiere Docker y act instalado.

Comando:
act push
