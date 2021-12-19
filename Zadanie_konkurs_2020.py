def Metoda_1():
    a = input("podaj a: ")
    b = input("podaj b: ")
    a = int(a)
    b = int(b)
    i=0
    while True:
        
        if a==b:
            i = str(i)
            print(a)
            print("Liczba iteracji: " + i)
            break
        elif a>b:
            a = a-b
        elif b>a:
            b = b-a
        i = i+1



def Metoda_2():
    a = input("podaj a: ")
    b = input("podaj b: ")
    a = int(a)
    b = int(b)
    i=0
    while True:
        if b==0:
            print(a)
            i = str(i)
            print("Liczba iteracji: " + i)
            break
        else:
            r = a%b
            a = b
            b = r
        i = i+1

Metoda_1()


