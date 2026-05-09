# Trabajo 4 - Gestion de la Configuracion - ITM

def saludar(nombre):
    return f'Hola {nombre}, bienvenido al Trabajo 4'

def calcular_promedio(notas):
    if not notas:
        raise ValueError('Lista vacia')
    return sum(notas) / len(notas)

def estado_nota(promedio):
    if promedio >= 4.0:
        return 'Aprobado - Excelente'
    elif promedio >= 3.0:
        return 'Aprobado'
    else:
        return 'Reprobado'

def nota_maxima(notas):
    return max(notas)

def nota_minima(notas):
    return min(notas)

def validar_nota(nota):
    if nota < 0.0 or nota > 5.0:
        return False
    return True

if __name__ == '__main__':
    print(saludar('ITM'))
    notas = [4.5, 3.8, 4.2, 3.9, 4.0]
    promedio = calcular_promedio(notas)
    print(f'Promedio: {promedio:.2f}')
    print(f'Estado: {estado_nota(promedio)}')
    print(f'Nota mas alta: {nota_maxima(notas)}')
    print(f'Nota mas baja: {nota_minima(notas)}')
