salary = float(input("Введіть заробітну плату: "))
experience = float(input("Введіть стаж роботи (в роках): "))

if experience < 1:
    print("Премія не передбачена")
elif 1 <= experience <= 3:
    bonus = salary * 0.05
    print(f"Сума премії (5%): {bonus}")
elif 3 < experience <= 5:
    bonus = salary * 0.10
    print(f"Сума премії (10%): {bonus}")
else:
    bonus = salary * 0.15
    print(f"Сума премії (15%): {bonus}")
