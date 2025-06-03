import pytest
# Este es un ejemplo de prueba unitaria en Python utilizando pytest
# La función test_demo verifica si la suma de dos números es correcta
# el decorador @pytest.mark.parametrize permite ejecutar 
        #la misma prueba con diferentes entradas y resultados esperados
# La función test_demo toma dos argumentos: entrada y esperado
# la parametrizacion relaciona un nombre para cada elemento individual 
       # para cada elemento que de una tupla dentro de una lista
@pytest.mark.ensayo
@pytest.mark.parametrize("entrada,esperado", [
    (3+5, 8),
    (2+4, 6),
    (6*9, 54)
    ])
def test_demo(entrada, esperado):
    assert entrada == esperado

#Un fixture es codigo de configuracion que prepara el entorno para pruebas
# como crear datos iniciales o configurar conexiones, usan el siguiente decorador
# Los fixtures tienen un scope que determina su ciclo de vida
# el scope puede ser: class,module,session,package, function (por defecto)

@pytest.fixture
def lista_vacia():
    return []

def test_add_elemento(lista_vacia):
    lista_vacia.append(54)
    assert len(lista_vacia) == 1
    assert lista_vacia[0] == 54

# @pytest.mark.skip omite la ejecucon de un test si no se cumpla una condicion externa
# Segun la documentacion un skip se usa cuando el test SOLO DEBE CORRER  si se cumple cierta 
# condicion, caso contrario se omite.

@pytest.mark.ensayo
@pytest.mark.skip(reason="No se puede ejecutar en este momento")
def test_por_implementar():
    assert funcion_cotizacion_para_cliente() == True


