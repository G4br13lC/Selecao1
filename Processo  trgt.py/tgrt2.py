numero = int(input("Informe um número: "))

a = 0
b = 1

while b <= numero:
    if b == numero:
        print("O número informado pertence à sequência de Fibonacci!")
        break
    a, b = b, a + b
else:
    print("O número informado não pertence à sequência de Fibonacci.")