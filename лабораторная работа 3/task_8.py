money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend:
    money_capital -= spend
    money_capital += salary
    spend *= (1 + increase)
    month += 1
# применив формулу, где salary вычитается из расходов, будет ответ 5
print(month)
