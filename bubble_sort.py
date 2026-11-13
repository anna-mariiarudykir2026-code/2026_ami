#19_варіант_1

fruit = "pear"
print(fruit)

#19_варіант_2
score = 67
if score > 60 :
    print("Мій бал вищий ніж 60")
else :
     print("Мій бал нижчий ніж 60")

#19_варіант_3
is_even = False
is_odd = True
print("Логічне 'І' (AND):", is_even and is_odd)
print("Логічне 'АБО' (OR):", is_even or is_odd)
print("Логічне 'НЕ' (NOT) для is_even:", not is_even)
print("Логічне 'НЕ' (NOT) для is_odd:", not is_odd)

#таблиця_2
import math
x = 4.123
y = 2.395
pryklad = math.log(x ** 3) + math.tan(y) + ((y + x) ** 3) - (x * math.sin(y + 1.6)) / 177 * (x ** 2 )
print("Результат = " ,pryklad )
