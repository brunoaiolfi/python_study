a = int(input('Valor A:'))
b = int(input('Valor B:'))
try:
    print(a/b)
except: ZeroDivisionError
print("Divisao por zero")