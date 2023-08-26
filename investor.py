maik =int(input("Бюджет Майкла:"))
ivan =int(input("Бюджет Ивана:"))
min =int(input("Минимальная сумма инвестиций:"))

if (maik >= min) and (ivan >= min):
    print(2)
elif (maik < min) and (ivan >= min):
    print("Ivan")
elif (maik >= min) and (ivan < min):
    print("Maik")
elif (maik + ivan) >= min:
    print(1)
else:
    print(0)
