x = []
y = []
a = 0
b = 0
sum_X = 0
sum_Y = 0
sum_XY = 0
sum_XX = 0
pogr = 0 # <- Погрешность

input_data = input("Введите значения X(через пробел): ").split(' ')

for num in input_data:
    x.append(int(num))

input_data = input("Введите значения Y(через пробел): ").split(' ')

for num in input_data:
    y.append(int(num))

n = len(x)

# Считаем суммы
for i in range(0, n):
    sum_X += x[i]
    sum_Y += y[i]
    sum_XY += x[i]*y[i]
    sum_XX += x[i]*x[i]

# Расчёт 'a' и 'b'
a = (n*sum_XY - sum_X*sum_Y)/(n*sum_XX - sum_X*sum_X)
b = (sum_Y - a*sum_X)/n

# Считаем погрешность
for i in range(0, n):
    pogr += pow(y[i]-(a*x[i]+b), 2)

# Вывод данных
print("Сумма всех X: " + str(sum_X))
print("Сумма всех Y: " + str(sum_Y))
print("Сумма всех X*Y: " + str(sum_XY))
print("Сумма всех X^2: " + str(sum_XX))
print("a = " + str(a) + "; b = " + str(b))
print("Погрешность = " + str(pogr))
input()
