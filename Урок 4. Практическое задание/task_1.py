"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

# Пытаемся получить три входящих параметра и присвоить их соотвествующим переменным
try:
    working_hour, rate_s, bonus = map(float, argv[1:])
    print(f' Заработная плата сотрудника за расчетный период: {format(working_hour * rate_s + bonus,".2f")}')
# Выводим сообщение при ошибке получения параметров
except ValueError:
    print("Введите РОВНО три параметра для расчета: часы, ставка, премия ")

