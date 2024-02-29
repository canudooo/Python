def contagem_vogais_consoantes(frase):
    vog=0
    cons=0
    for letra in frase:
        if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
            vog += 1
        elif letra.isalpha():
            cons += 1
    return(vog, cons)

frase = (input('insira uma frase qualquer: '))
resultado=contagem_vogais_consoantes(frase)

print(resultado)

