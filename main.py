summ = 0
s = 0
while True:
    n = int(input('Введите целое число:'))
    s = 0
    k = n
    if k == 0:
        print(summ)
        break
    while k != 0:
      s += k % 10
      k //= 10
    print('Сумма цифр:', s)
    if s > summ:
      summ = s
      m = n
print('Число', m)
print('Максимальная сумма цифр', summ)








