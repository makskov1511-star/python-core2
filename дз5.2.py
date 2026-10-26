
salary1 = 200
salary2 = 200
salary3 = 200

sales1 = float(input("Введіть продажі першого менеджера: "))
sales2 = float(input("Введіть продажі другого менеджера: "))
sales3 = float(input("Введіть продажі третього менеджера: "))

if sales1 < 500:
    salary1 += sales1 * 0.03
elif sales1 <= 1000:
    salary1 += sales1 * 0.05
else:
    salary1 += sales1 * 0.08

if sales2 < 500:
    salary2 += sales2 * 0.03
elif sales2 <= 1000:
    salary2 += sales2 * 0.05
else:
    salary2 += sales2 * 0.08

if sales3 < 500:
    salary3 += sales3 * 0.03
elif sales3 <= 1000:
    salary3 += sales3 * 0.05
else:
    salary3 += sales3 * 0.08

if salary1 >= salary2 and salary1 >= salary3:
    salary1 += 200
    print("Найкращий менеджер: перший")
elif salary2 >= salary1 and salary2 >= salary3:
    salary2 += 200
    print("Найкращий менеджер: другий")
else:
    salary3 += 200
    print("Найкращий менеджер: третій")

print("Зарплата першого менеджера:", salary1, "$")
print("Зарплата другого менеджера:", salary2, "$")
print("Зарплата третього менеджера:", salary3, "$")
