import re

# Cifra de Vigenère

class ConversorCifraVesemir:
    def __init__(self):
        pass

    def cifrar(self, texto, caracteres):
        if not re.fullmatch(r'([a-zA-Z\t]*)', texto):
            raise Exception("Texto deve conter somente letras do alfabeto")
        letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        indice = 0
        cifra = ''
        for i in range(0, len(texto)):
            letra = texto[i]
            letraAux = letra.upper()
            codigo_ascii_letra = ord(letraAux)
            valor_letra = ord(caracteres[indice]) - 65
            if codigo_ascii_letra + valor_letra > 90:
                codigo_ascii_letra_nova = 65 + (((90 - codigo_ascii_letra) - valor_letra) * -1) - 1
            elif codigo_ascii_letra + valor_letra > 122:
                codigo_ascii_letra_nova = 97 + (((122 - codigo_ascii_letra) - valor_letra) * -1) - 1
            else:
                codigo_ascii_letra_nova = codigo_ascii_letra +  valor_letra

            print(str(codigo_ascii_letra)  + ' - ' + str(codigo_ascii_letra)  + ' - ' + str(codigo_ascii_letra_nova) + ' - ' + str(valor_letra)) 
            cifrado = chr(codigo_ascii_letra_nova)
            cifra = cifra + cifrado
            print(letra + '  -  ' + cifrado)
            if(indice + 1 >= len(caracteres)):
                indice = 0
            else:
                indice = indice + 1
        return cifra

    def decifrar(self, cifra):
        pass

if __name__ == "__main__":
    conversor = ConversorCifraVesemir()
    # cifrado = conversor.cifrar("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    cifrado = conversor.cifrar("abcdefghijklmnopqrstuvwxyz", ['D', 'U', 'H'])
    cifrado = conversor.cifrar("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", ['D', 'U', 'H'])
    print(cifrado)
    # texto = conversor.decifrar(cifrado)
    # print(texto)

    