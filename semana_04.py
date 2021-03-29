def exercicio_um(numero):
    contador = 0

    while numero < 101:
        numero = (numero + 3)
        contador = contador + 1
    print(' Sera necessario somar 3, mais \033[1;33m{} \033[m vezes para ultrapassar o numero 100.'.format(contador))
    print(' ')
    print('-=-'* 35)

def exercicio_dois():
    lista3 = [n for n in range(1,11)]
    lista4 = []
    for n in lista3:
        if n != 3 and n != 5:
            lista4.append(n)
    print(lista4)

print("EX 1")
exercicio_um(50)

print("EX 2")
exercicio_dois()
