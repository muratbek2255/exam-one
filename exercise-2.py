print('Привет, мы рады приветствовать на нашем банке!')
summa2 = float(input('Vvedite summu: '))
summa3 = float(input("percent :"))
summa4 = float(input("end summa:"))
month = 0

x = ((summa3/12)*summa2)
x += 1

while x < summa4:
    x += ((summa3/12)*x)
    month+=1

print(month)




