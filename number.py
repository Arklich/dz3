x = int(input("Введите число для проверки:"))
#отрицательное четное число, отрицательное нечетное число, нулевое число, положительное четное число, положительно нечетное число
if(x % 2) == 0 and (x < 0):
    print("Отрицательное четное число")
elif(x % 2) == 0 and (x > 0):
    print("Положительное четное число")
elif (x % 2) != 0 and (x > 0):
    print("Положительное нечетное число")
elif(x == 0):
    print("Нулевое число")
else:
    print("Отрицательное нечетное число")
    