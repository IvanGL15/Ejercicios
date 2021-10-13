number = int(input("Introduce un número: "))

result = number % 2
by_4 = number % 4

if result == 0:
    if by_4 == 0:
        print("El número es par y divisible por 4")

    else:
        print("El número es par pero no divisible por 4")
else:
    print("El número es impar")