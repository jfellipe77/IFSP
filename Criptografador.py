def criptografar(texto, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''
    
    for letra in texto:
        if letra.isalpha():  
            letra_min = letra.lower()
            nova_letra = alfabeto[(alfabeto.index(letra_min) + chave) % 26]
            if letra.isupper():
                resultado += nova_letra.upper()
            else:
                resultado += nova_letra
        else:
            resultado += letra 

    return resultado

texto_original = input("Digite o texto a ser criptografado: ")
chave = int(input("Digite a chave de criptografia: "))
texto_criptografado = criptografar(texto_original, chave)
print("Texto criptografado:", texto_criptografado)
