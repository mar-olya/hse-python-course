print(18 <= (age := int(input("Ваш возраст: "))) <= 65)


print((n1 := int(input("Введите число: "))) > (n2 := int(input("Введите число: "))) > (n3 := int(input("Введите число: "))))


year = 2024
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if x > 0 and x < 10:
    print("ok")