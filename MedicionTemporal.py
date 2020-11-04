import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
    
    def f(x):

        respuesta = 0

        for i in range(1000):
            respuesta += 1

        for i in range(x):
            respuesta += x

        for i in range(x):
            for j in range(x):
                respuesta += 1
                respuesta += 1

        return respuesta

