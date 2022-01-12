print('Привет, мы рады приветствовать на нашем банке!')
summa1 = float(input('Vvedite summu: '))
summa2 = float(input("percent :"))
summa3 = float(input("end summa:"))
month = 0

while summa1 < summa3 :
    month += 1
    deposit_amount = (summa2/100)/12*summa1+summa1
    print(f'{month}  {summa1}')


print(f'необходимо:{month} месяцев для накопления {summa3}')




