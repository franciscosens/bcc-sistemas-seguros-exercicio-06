import re

# Cifra de Vigenère

class ConversorCifraVigenere:
    def __init__(self, caracteres):
        self.caracteres = caracteres

    def cifrar(self, texto):
        if not re.fullmatch(r'([a-zA-Z\s]*)', texto):
            raise Exception("Texto deve conter somente letras do alfabeto")
        letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        indice = 0
        cifra = ''
        for i in range(0, len(texto)):
            letra = texto[i]
            letraAux = letra.upper()
            codigo_ascii_letra = ord(letraAux)
            valor_letra = ord(self.caracteres[indice]) - 65
            if codigo_ascii_letra == 32:
                codigo_ascii_letra_nova = 32
            elif codigo_ascii_letra + valor_letra > 90:
                codigo_ascii_letra_nova = 65 + (((90 - codigo_ascii_letra) - valor_letra) * -1) - 1
            elif codigo_ascii_letra + valor_letra > 122:
                codigo_ascii_letra_nova = 97 + (((122 - codigo_ascii_letra) - valor_letra) * -1) - 1
            else:
                codigo_ascii_letra_nova = codigo_ascii_letra +  valor_letra
            cifrado = chr(codigo_ascii_letra_nova)
            cifra = cifra + cifrado
            if indice + 1 >= len(self.caracteres):
                indice = 0
            else:
                indice = indice + 1
        return cifra

    def decifrar(self, cifra):
        texto = ''
        indice = 0
        quantidade_caracteres = len(cifra)
        for i in range(0, quantidade_caracteres):
            letra = cifra[i].upper()
            letra_codigo_ascii = ord(letra)

            letra_caracter = self.caracteres[indice]
            letra_caracter_codigo_ascii = ord(letra_caracter)
            valor_letra = letra_caracter_codigo_ascii - 65
            
            if letra_codigo_ascii == 32:
                nova_letra_codigo_ascii = 32
            elif letra_codigo_ascii - valor_letra < 65:
                nova_letra_codigo_ascii = 90 - (letra_caracter_codigo_ascii - letra_codigo_ascii) + 1
            else:
                nova_letra_codigo_ascii = letra_codigo_ascii - valor_letra
            nova_letra = chr(nova_letra_codigo_ascii)
            texto = texto + nova_letra
            indice = 0 if indice + 1 >= len(self.caracteres) else indice + 1
        return texto

if __name__ == "__main__":

    opcao = 1
    print('Informe os caracteres separando com espaço os caracteres: ', end='')
    chave = input().split(' ')
    conversor = ConversorCifraVigenere(chave)
    while opcao != 3:

        print('1 - Cifrar\n2 - Decrifrar\n3 - Sair')
        opcao = int(input())
        if opcao == 1:
            print('Digite o texto para cifrar: ', end='')
            texto = input()
            cifrado = conversor.cifrar(texto)
            print('Cifrado: ' + cifrado)
        elif opcao == 2:
            print('Digite o texto para decifrar: ', end='')
            cifrado = input()
            texto = conversor.decifrar(cifrado)
            print('Cifrado: ' + texto)