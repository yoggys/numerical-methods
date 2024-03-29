import time
import matplotlib.pyplot as plt

def f(x):
    return x**6-x**3+x**2-1

def sieczne(f, x0, x1, N):
    tmp = 0 
    for _ in range(N):
        plt.scatter(x0, f(x0), marker='+', color='r')
        plt.scatter(x1, f(x1), marker='+', color='b')
        plt.plot([x0,x1], [f(x0),f(x1)])
        plt.pause(0.1)
        
        if (f(x0)-f(x1)) == 0:
            x1 -= 1
        if f(x1) == 0:
            return x1
        elif f(x0) == 0:
            return x0
        else:
            tmp = x1-(f(x1)*(x0-x1)/(f(x0)-f(x1)))
            if tmp > x0:
                x1 = x0
                x0 = tmp
            else:
                x0 = x1
                x1 = tmp
    return x1
        
if __name__ == "__main__":
    plt.axis()

    while True:
        try:
            try:
                x0 = float(input("Podaj x0: "))
                x1 = float(input("Podaj x1: "))
                n = int(input("Podaj liczbę iteracji: "))
            except:
                raise ValueError("[ERROR] podano błędne dane!")
            if n<=0 or x0==x1:
                raise ValueError("[ERROR] liczba iteracji powinna być >0, a x0 nie może być równe x1!")

            if x0<x1:
                tmp = x0
                x0 = x1
                x1 = tmp
                del tmp
                 
            begin = time.time()
            out = sieczne(f, x0, x1, n)
            end = time.time()

            print(f"Miejsce zerowe: {out}") 
            print(f"Trwało to: {(end-begin):.20f} sekund")
            plt.show()    
            break
        except ValueError as E:
            print(E)
