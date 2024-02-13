from typing import Callable
from functools import reduce
import re 


#створюємо функцію, що відбере всі числа з рядка 
def generator_numbers(text: str) :
    pattern = r'(\d+\.\d*)|(\d+)'
    numbers_float = map(float, filter(lambda x: re.fullmatch(pattern,x), text.split(" ")))
    for numb in numbers_float :
        yield numb

#Створюємо функцію, що додасть всі елементи генератора 
def sum_profit(text: str, func: Callable) :
     sum_number = reduce(lambda x,y: x+y, func(text))
     return sum_number



text = "Загальний дохід працівника складається з декількох частин 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")