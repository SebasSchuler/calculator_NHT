# calculator_NHT

Calculadora que tiene como fin realizar las operaciones aritméticas básicas
de numeros enteros sin el uso de operadores aritméticos

## Instalación
La instalación se explica a continuación

### Entorno virtual
Se debe instalar el paquete `virtualenv` para la configuracion del entorno virtual

```
# Se instala el paquete
pip install virtualenv
# Se crea un entorno virtual
virtualenv venv
```
Para el siguiente paso será necesario activar el entorno virtual
```
cd venv
source bin/activate
```
### Instalación de dependencias
Debe posicionarse en el directorio que contiene el entorno virtual
```
pip install -r requirements.txt
```

## Tests

Para ejecutar los test tan solo debe posicionarse en el directorio `Prueba-NHT`
y ejecutar
```
python3 -m unittest test.py
```