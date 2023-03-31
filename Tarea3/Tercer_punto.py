def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
def app():
    n=int(input('Ingrese un número: '))
    for i in range(n):
        factorial(i)
    print(f'El Factorial de {n} es', factorial(n))

if __name__ == '__main__':
    app()
    