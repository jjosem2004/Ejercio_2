# ------------------------------------------------------
# Convierte un número decimal positivo a binario usando un 
#   determinado número de bits.
# El binario resultante es un string e.g. "101"
# Se usa la función bin() que transforma e.g. 3 en "0b11".
# En esta función se quita el "0b" para dejar el "11"
# ------------------------------------------------------
def dec2bin(numero_decimal, numero_bits):
    numero_binario = bin(numero_decimal)
    
    if numero_decimal >= 0:
        # Quita el "0b" del principio
        numero_binario = numero_binario[2:]
        # Añade 0's a la izquierda si hace falta
        while len(numero_binario) < numero_bits:
            numero_binario = "0" + numero_binario
    else:
        # Quita el "-0b" del principio
        numero_binario = numero_binario[3:]
        # Añade 1's a la izquierda si hace falta
        while len(numero_binario) < numero_bits:
            numero_binario = "1" + numero_binario
    
    return numero_binario
    
#comprobacion de funcionamiento
print (dec2bin(-1, 4))
print (dec2bin(-1, 8))
#soy Jordi y he comentado otra vez

